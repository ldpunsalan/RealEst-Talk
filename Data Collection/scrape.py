from bs4 import BeautifulSoup
import requests
import pandas as pd
import unicodedata

# create empty dataframe as a container for our data later on

df = pd.DataFrame(columns = ['Description','Location','Price (PHP)','Bedrooms',
                            'Bath','Floor_area (sqm)','Land_area (sqm)','Latitude','Longitude',
                            'Link'])

# initialize page as zero

page = 0
max_page = 50

# function below taken from stack overflow to convert latin n to english n

def strip_accents(text):
    return ''.join(char for char in
                   unicodedata.normalize('NFKD', text)
                   if unicodedata.category(char) != 'Mn')

# main routine to sift through pages and take real estate info then load it into dataframe

while page in range(0,max_page):
    page += 1
    html_text = requests.get(f'https://www.lamudi.com.ph/buy/?page={page}').text
    soup = BeautifulSoup(html_text, 'lxml')
    all_info_main = soup.find_all('div', class_='ListingCell-AllInfo ListingUnit')

    for all_info in all_info_main:
        header = all_info.find('h3', class_='ListingCell-KeyInfo-title').text.strip()
        location = all_info.find('span', class_='ListingCell-KeyInfo-address-text').text.strip()
        try:
            price = all_info.find('span', class_='PriceSection-FirstPrice').text.strip()
        except AttributeError:
            price ="na"
        
        bed = "na"
        bath = "na"
        floor_area = "na"
        land_area = "na"

        key_information_div = all_info.find('div', class_='KeyInformation_v2')
        attribute_divs = key_information_div.find_all('div', class_='KeyInformation-attribute_v2')
        for attribute_div in attribute_divs:
            label_span = attribute_div.find('span', class_='KeyInformation-label_v2')
            if label_span:
                label = label_span.get_text(strip=True)
                value_span = attribute_div.find('span', class_='KeyInformation-value_v2')
                if value_span:
                    value = value_span.get_text(strip=True)
                    if label == 'Bedrooms':
                        bed = value
                    elif label == 'Baths':
                        bath = value
                    elif label == 'Floor area' or label == 'Floor Area':
                        floor_area = value
                    elif label == 'Land Size':
                        land_area = value


        start = str(all_info).index('data-geo-point=')
        geo_location = str(all_info)[start+17:start+39]
        geo_location = geo_location.replace(']','')
        geo_location = geo_location.replace('"','')
        geo_location = geo_location.replace(' ','')
        geo_location = geo_location.replace('d','')
        geo_location = geo_location.replace('a','')
        geo = geo_location.split(",")
        longitude = geo[0]
        latitude = geo[1]
        link = all_info.a['href']
        new_row = {
                'Description' : strip_accents(header),
                'Location' : strip_accents(location),
                'Price (PHP)' : price.lstrip("₱ "),
                'Bedrooms' : bed,
                'Bath' : bath,
                'Floor_area (sqm)' : floor_area.rstrip(" m²"),
                'Land_area (sqm)' : land_area.rstrip(" m²"),
                'Latitude' : latitude,
                'Longitude' : longitude,
                'Link' : link}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    print(f'finished page {page}')

# output dataframe into CSV file

df.to_csv('2024_RE_data.csv', encoding='utf-8', index=False)



        #print(header)
        #print(location)
        #print(price)
        #print(bedrooms)
        #print(floor_area)
        #print(land_area)
        #print(link)
        #print("\n")
