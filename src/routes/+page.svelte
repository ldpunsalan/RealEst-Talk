<script>
  import Card from "./Card.svelte";
  import Hero from "./Hero.svelte";
  import Overview from "./Overview.svelte";
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Real(i)ty Check" />
</svelte:head>

<main>
  <Hero />
  <Overview />
  <section id="data" class="pt-32">
    <div class="flex flex-row items-center space-x-4">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="currentColor"
        class="size-12"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M10.5 6a7.5 7.5 0 1 0 7.5 7.5h-7.5V6Z"
        />
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="M13.5 10.5H21A7.5 7.5 0 0 0 13.5 3v7.5Z"
        />
      </svg>
      <h1
        class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
      >
        Data Gathering
      </h1>
    </div>
    <div class="flex flex-row space-x-4 items-center">
      <Card>
        <div class="justify-center">
          <h2>
            We mined 1,500 entries from <a
              href="https://www.lamudi.com.ph/"
              style="color:#89b4fa"><u>Lamudi</u></a
            > for real estate data.
          </h2>
          <br />
          <p class="text-center">
            Lamudi is a real estate agency with a website for listings for real
            estate properties. The data was scraped using a modified version of
            <a
              href="https://github.com/arl7d/portfoilioprojects/tree/main/Web_scraping_Philippine_real_estate"
              style="color:#89b4fa"
            >
              <u>this python script.</u>
            </a>
          </p>
          <br /> <br />
          <button>
            <a
              href="https://docs.google.com/spreadsheets/d/1kvwDaHs-RAxw1JMh26u4GkBeTQdy41mho1BkSPY33Pg/edit?usp=sharing"
            >
              Let's take a look at our data!</a
            >
          </button>
        </div>
      </Card>
    </div>
  </section>

  <section class="pt-32">
    <div class="flex flex-row items-center space-x-4">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="var(--color-theme-2)"
        class="size-12"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
        />
      </svg>
      <h1
        class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
      >
        Data Preprocessing
      </h1>
    </div>
    <div class="grid grid-cols-4 text-center">
          <Card>
            <h2>Data Cleansing</h2>
            Duplicate entries and entries with a missing price were removed.
            <br><br>
          </Card>
          <Card>
            <h2>Data Reduction</h2>
            Unnecessary columns were removed (e.g longitude and latitude).
          </Card>
        <div class="grid col-span-2 row-span-2">
          <Card>
            <h2>Data Transformation</h2>
            <br>
            <p>Added real estate type as a feature (house / condo unit / lot)  - house type encompasses houses, 
              townhouses, duplexes while lots encompasses commercial and residential </p>
              <br>
            <p>Added degree of urbanization (highly urbanized / non-highly urbanized) 
              based on <a href="https://cmci.dti.gov.ph/rankings-data.php?unit=Highly%20Urbanized%20Cities" style="color:#89b4fa"><u>DTI 2023 city rankings.</u></a>
            </p>
          </Card>
        </div>
          <div class="grow items-center justify-center text-center">
            <Card>
              <p class="font-bold text-4xl">1196</p>
              <p class="text-2xl">entries</p>
            </Card>
          </div>
          <div class="grow items-center justify-center text-center">
            <Card>
              <p class="font-bold text-4xl">10</p>
              <p class="text-2xl">features</p>
            </Card>
          </div>
    </div>
  </section>

  <section class="pt-32">
    <div class="flex flex-row items-center space-x-4">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="var(--color-theme-2)"
        class="size-12"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
        />
      </svg>
      <h1
        class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
      >
        Answering our Research Questions
      </h1>
    </div>
    <br />

    <h2>
      1. How do real estate prices vary across different cities in the
      Philippines?
    </h2>
    <div class="grid grid-rows-3 grid-flow-col gap-4">
      <Card>
        <div class="flex flex-row gap-10">
          <div class="mb-4 w-3/4 z-20">
            <img
              src="src\lib\images\charts\house_opaque.png"
              class="h-auto hover:scale-150 ease-in duration-500"
              alt=""
            />
          </div>
          <div>
            <h2>House Listings</h2>
            <p>This graph shows that for House Listings:</p>
            <br />
            <ul style="list-style-type:disc;">
              <li>
                <strong
                  >Highest Average Price per sqm (Overall & Highly Urbanized):</strong
                >
                <p>
                  The City of Lapu-lapu with <strong>₱175,326.50/sqm</strong>
                </p>
              </li>
              <br />
              <li>
                <strong
                  >Highest Average Price per sqm (Non-highly Urbanized):</strong
                >
                <p>
                  The Municipality of Nasugbu with <strong
                    >₱64,056.94/sqm</strong
                  > 
                </p>
              </li>
              <br />
              <li>
                <strong>Lowest Average Price per sqm (Highly Urbanized):</strong
                >
                <p>
                  The City of Zamboanga with <strong>₱25,705.08/sqm</strong>
                </p>
              </li>
              <br />
              <li>
                <strong
                  >Lowest Average Price per sqm (Overall & Non-highly
                  Urbanized):</strong
                >
                <p>
                  The Island Garden City of Samal with <strong
                    >₱17,605.63/sqm</strong
                  >
                </p>
              </li>
            </ul>
          </div>
        </div>
      </Card>
      <Card>
        <div class="flex flex-row gap-10">
          <div class="mb-4 w-3/4 z-20">
            <img
              src="src\lib\images\charts\condo_opaque.png"
              class="h-auto hover:scale-150 ease-in duration-500 object-cover"
              alt=""
            />
          </div>
          <div>
            <h2>Condo Unit Listings</h2>
            <p>This graph shows that for Condo Unit Listings:</p>
            <br />
            <ul style="list-style-type:disc;">
              <li><strong>Highest Average Price per sqm (Overall & Non-highly Urbanized):</strong> 
                <p>The Municipality of Malay with <strong>₱545,733.33/sqm</strong></p>
              </li>
              <br>
              <li><strong>Highest Average Price per sqm (Highly Urbanized):</strong> 
                <p>The City of Makati with <strong>₱361,331.92/sqm</strong></p>
              </li>
              <br>
              <li><strong>Lowest Average Price per sqm (Highly Urbanized):</strong> 
                <p>The City of Bacolod with <strong>₱143,808.05/sqm</strong></p>
              </li>
              <br>
              <li><strong>Lowest Average Price per sqm (Overall & Non-highly Urbanized):</strong> 
                <p>The Municipality of Silang with <strong>₱34,814.81/sqm</strong></p>
              </li>
            </ul>
          </div>
        </div>
      </Card>
      <Card>
        <div class="flex flex-row gap-10">
          <div class="mb-4 w-3/4 z-20">
            <img
              src="src\lib\images\charts\lot_opaque.png"
              class="h-auto hover:scale-150 ease-in duration-500"
              alt=""
            />
          </div>
          <div>
            <h2>Lot Listings</h2>
            <p>This graph shows that for Lot Listings:</p>
            <br />
            <ul style="list-style-type:disc;">
              <li><strong>Highest Average Price per sqm (Overall & Highly Urbanized):</strong> 
                <p>The City of Muntinlupa with <strong>₱435,000.00/sqm</strong></p>
              </li>
              <br>
              <li><strong>Highest Average Price per sqm (Non-highly Urbanized):</strong> 
                <p>The City of Carmona with <strong>₱54,296.00/sqm</strong></p>
              </li>
              <br>
              <li><strong>Lowest Average Price per sqm (Highly Urbanized):</strong> 
                <p>The City of Zamboanga with <strong>₱39,234.95/sqm</strong></p>
              </li>
              <br>
              <li><strong>Lowest Average Price per sqm (Overall & Non-highly Urbanized):</strong> 
                <p>The Municipality of Polomolok with <strong>₱330.00/sqm</strong></p>
              </li>
            </ul>
          </div>
        </div>
      </Card>
    </div>
    <h2>
      2. How do real estate prices vary across different cities in the
      Philippines?
    </h2>
    <Card>
      <div class="grid grid-cols-2 gap-10">
        <div class="mb-4 z-20">
          <img
            src="src\lib\images\charts\barchart_opaque.png"
            class="h-auto hover:scale-150 ease-in duration-500"
            alt=""
          />
        </div>
        <div>
          <h2>Insights</h2>	
          <br>
          <p>This graph shows that, on average:</p>
          <br>
          <ul style="list-style-type:disc;">
            <li>House Listings in Highly Urbanized Locations are more expensive than in Non-highly Urbanized Locations by <strong>₱54,995.12</strong> (~2.81x more).
            </li>
            <br>
            <li>Lot Listings in Highly Urbanized Locations are more expensive than in Non-highly Urbanized Locations by <strong>₱304,695.60</strong> (~10.50x more).
            </li>
            <br>
            <li>Condo Unit Listings in Highly Urbanized Locations are more expensive than in Non-highly Urbanized Locations by <strong>₱90,200.02</strong> (~1.57x more).
            </li>
            </ul>
        </div>
      </div>
    </Card>
  </section>

  <section id="team" class="pt-32">
    <div class="flex flex-row items-center space-x-4">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="size-12">
        <path stroke-linecap="round" stroke-linejoin="round" d="M15.182 15.182a4.5 4.5 0 0 1-6.364 0M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Z" />
      </svg>      
      <h1
        class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
      >
        The Team
      </h1>
    </div>
    <Card>
    <p class="text-center">We are a team of 3 people studying data science that aim to use data science to gain insights 
      about the country's current economical state. In our project, Real(i)ty Check, we aim to delve 
      into the landscape of property prices in the Philippines. We are interested in how the urbanization 
      of different Philippine cities has affected the price of real estate. With this, we hope that we are 
      able to successfully identify the areas where housing is becoming unaffordable.</p>
      </Card>
    <div class="flex flex-row space-x-4 items-center">
      <Card>
          <img
            src="src\lib\images\team\ray.png"
            class="h-auto hover:scale-150 ease-in duration-500 object-cover rounded-full"
            alt=""
          />
          <h2>Ray Nuñez</h2>
          <p class="text-center">a computer science student interested in data science, bioinformatics, and web development. </p>
      </Card>
      
      <Card>
          <img
            src="src\lib\images\team\chase.png"
            class="h-auto hover:scale-150 ease-in duration-500 object-cover rounded-full"
            alt=""
          />
          <h2>Chase Gonzaga</h2>
          <p class="text-center">a computer science student interested in web development, game development, and data science. </p>
      </Card>
      <Card>
          <img
            src="src\lib\images\team\lara.png"
            class="h-auto hover:scale-150 ease-in duration-500 object-cover rounded-full"
            alt=""
          />
          <h2>Lara Punsalan</h2>
          <p class="text-center">a computer science student interested in UI/UX, web development, and app development.</p>
      </Card>
    </div>
  </section>

</main>

<style>
  svg {
    color: var(--color-theme-2);
  }
  section {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    flex: 0.6;
  }

  h1 {
    width: 100%;
  }

  button {
    position: relative;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
    border-radius: 15px;
    padding: 10px 20px;
    border: 1px solid transparent;
    color: var(--color-bg-1);
    background: linear-gradient(to right, #cba6f7, #89b4fa) border-box;
  }

  button:hover {
    color: var(--color-text);
    background:
      linear-gradient(#1e1e2e 0 0) padding-box padding-box,
      linear-gradient(to right, #cba6f7, #89b4fa) border-box;
  }
</style>
