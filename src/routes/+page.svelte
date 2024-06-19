<script>
  import Card from "./Card.svelte";
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Real(i)ty Check" />
</svelte:head>

<main>
  <section class="hero-container">
    <Card>
      <div class>
        <div class="flex flex-col">
          <h1
            style="font-size: 5rem;"
            class="text-center leading-none font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#cba6f7] to-[#89b4fa] px-4"
          >
            Real<span class="text-[#cdd6f4]">(i)</span>ty Check
          </h1>
          <br />
          <p class="text-center">
            An analysis of real estate prices across different cities in the
            Philippines <br /> by
            <span
              class="bg-clip-text text-transparent bg-gradient-to-r from-[#cba6f7] to-[#89b4fa]"
              >RealEst Talk</span
            >
          </p>
        </div>
      </div></Card
    >
  </section>
  <section id="overview" class="pt-32">
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
        Overview
      </h1>
    </div>
    <div class="flex flex-col">
      <Card class="flex">
        <p class="text-center">
          The Philippine real estate market is influenced by various factors,
          including economic growth, infrastructure development, and population
          density. There is a pressing issue of housing affordability,
          particularly in urban areas, where real estate prices continue to
          rise, and making homeownership increasingly inaccessible for many
          segments of the population. This has led to housing insecurity, forced
          evictions, informal settlements, and social exclusion, exacerbating
          inequalities and hindering sustainable urban development.
        </p>
      </Card>
      <div class="flex flex-row">
        <Card>
          <div class="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="size-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3 3v1.5M3 21v-6m0 0 2.77-.693a9 9 0 0 1 6.208.682l.108.054a9 9 0 0 0 6.086.71l3.114-.732a48.524 48.524 0 0 1-.005-10.499l-3.11.732a9 9 0 0 1-6.085-.711l-.108-.054a9 9 0 0 0-6.208-.682L3 4.5M3 15V4.5"
              />
            </svg>
            <h2>Objective</h2>
          </div>
          <p>
            The aim is to assess the affordability of housing, state of urban
            planning and economic health of the different regions in the
            country.
          </p>
        </Card>
        <Card>
          <div class="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="size-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 5.25h.008v.008H12v-.008Z"
              />
            </svg>
            <h2>Problem</h2>
          </div>
          <p>
            Affordable housing is increasingly becoming a problem amidst the
            rising prices of real estate in across the country.
          </p>
        </Card>
        <Card>
          <div class="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="size-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z"
              />
            </svg>

            <h2>Solution</h2>
          </div>
          <p>
            Pinpoint areas where housing is becoming inaccessible and expensive
            through a statistical comparative analysis of real estate prices and
            the price-to-floor area ratio among property types across different
            Philippine cities.
          </p>
        </Card>
      </div>
      <div class="flex flex-row">
        <Card>
          <div class="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="size-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M15 12H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
              />
            </svg>
            <h2>Null Hypothesis</h2>
          </div>
          <p>
            There is no significant difference between prices of similar types
            of real estate in highly urbanized cities compared to non-highly
            urbanized areas.
          </p>
        </Card>
        <Card>
          <div class="flex items-center space-x-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="size-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
              />
            </svg>

            <h2>Alternative Hypothesis</h2>
          </div>
          <p>
            Real estate in more highly urbanized cities of the Philippines are
            more expensive than their counterparts in non-highly urbanized areas
            of the country.
          </p>
        </Card>
      </div>
    </div>
  </section>
  <br /><br />

  <section id="data" class="pt-32">
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
      Data Gathering
    </h1>
    </div>
    <div class="flex flex-row space-x-4 items-center">
      <Card>
        <div class="justify-center">
        <h2>We mined 1,500 entries from <a href="https://www.lamudi.com.ph/" style="color:#89b4fa"><u>Lamudi</u></a> for real estate data.</h2>
        <br />
        <p class="text-center">Lamudi is a real estate agency with a website for listings for 
          real estate properties. The data was scraped using a modified 
          version of 
          <a href="https://github.com/arl7d/portfoilioprojects/tree/main/Web_scraping_Philippine_real_estate" style="color:#89b4fa">
            <u>this python script.</u>
          </a>
        </p>
        <br> <br>
        <button>
          <a href="https://docs.google.com/spreadsheets/d/1kvwDaHs-RAxw1JMh26u4GkBeTQdy41mho1BkSPY33Pg/edit?usp=sharing" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Let's take a look at our data</a>
        </button>
        </div>
      </Card>
    </div>
  </section>

  <br />   <br />

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
    <div class="flex flex-row space-x-4">
      <div class="grid grid-cols-3 gap-x-3">
      <Card>
        <h2>Data Cleansing</h2>
        <br />
        <ul style="list-style-type:disc;">
          <li>
            Duplicate entries and entries with a missing price were removed.
          </li>
        </ul>
      </Card>
      <Card>
        <h2>Data Reduction</h2>
        <br />
        <ul style="list-style-type:disc;">
          <li>
            Unnecessary columns were removed (e.g longitude and latitude).
          </li>
        </ul>
      </Card>
      <Card>
        <h2>Data Transformation</h2>
        <br />
        <ul style="list-style-type:disc;">
          <li>
            Real estate type (House/Lot/Condo Unit), province, region, and
            degree of urbanization (Highly Urbanized/Non-highly Urbanized) were
            added as new features
          </li>
          <li>Houses include Duplexes, Houses, and Townhouses</li>
          <li>Lots include Residential Lots and Commercial Lots</li>
        </ul>
      </Card>
    </div>
    <h2>We ended up with 1196 entries and 10 features.</h2>
  </section>

  <br />   <br />


  <section>
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
            <br>
            <ul style="list-style-type:disc;">
            <li><strong>Highest Average Price per sqm (Overall & Highly Urbanized):</strong> 
              <p>The City of Lapu-lapu with <strong>₱175,326.50/sqm</strong></p>
            </li>
            <br>
            <li><strong>Highest Average Price per sqm (Non-highly Urbanized):</strong> 
              <p>The Municipality of Nasugbu with <strong>₱64,056.94/sqm</strong></p>
            </li>
            <br>
            <li><strong>Lowest Average Price per sqm (Highly Urbanized):</strong> 
              <p>The City of Zamboanga with <strong>₱25,705.08/sqm</strong></p>
            </li>
            <br>
            <li><strong>Lowest Average Price per sqm (Overall & Non-highly Urbanized):</strong> 
              <p>The Island Garden City of Samal with <strong>₱17,605.63/sqm</strong></p>
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
            <h2>House Listings</h2>	
            <p>This graph shows that for House Listings:</p>
            <br>
            <ul style="list-style-type:disc;">
            <li><strong>Highest Average Price per sqm (Overall & Highly Urbanized):</strong> 
              <p>The City of Lapu-lapu with <strong>₱175,326.50/sqm</strong></p>
            </li>
            <br>
            <li><strong>Highest Average Price per sqm (Non-highly Urbanized):</strong> 
              <p>The Municipality of Nasugbu with <strong>₱64,056.94/sqm</strong></p>
            </li>
            <br>
            <li><strong>Lowest Average Price per sqm (Highly Urbanized):</strong> 
              <p>The City of Zamboanga with <strong>₱25,705.08/sqm</strong></p>
            </li>
            <br>
            <li><strong>Lowest Average Price per sqm (Overall & Non-highly Urbanized):</strong> 
              <p>The Island Garden City of Samal with <strong>₱17,605.63/sqm</strong></p>
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
            <h2>House Listings</h2>	
            <p>This graph shows that for House Listings:</p>
            <br>
            <ul style="list-style-type:disc;">
            <li><strong>Highest Average Price per sqm (Overall & Highly Urbanized):</strong> 
              <p>The City of Lapu-lapu with <strong>₱175,326.50/sqm</strong></p>
            </li>
            <br>
            <li><strong>Highest Average Price per sqm (Non-highly Urbanized):</strong> 
              <p>The Municipality of Nasugbu with <strong>₱64,056.94/sqm</strong></p>
            </li>
            <br>
            <li><strong>Lowest Average Price per sqm (Highly Urbanized):</strong> 
              <p>The City of Zamboanga with <strong>₱25,705.08/sqm</strong></p>
            </li>
            <br>
            <li><strong>Lowest Average Price per sqm (Overall & Non-highly Urbanized):</strong> 
              <p>The Island Garden City of Samal with <strong>₱17,605.63/sqm</strong></p>
            </li>
            </ul>
        </div>
        </div>
      </Card>
    </div>
    <h2>We ended up with 1196 entries and 10 features.</h2>
  </section>
</main>

<style>
  svg {
    color: var(--color-theme-1);
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

  h2 {
    font-weight: bold;
    text-align: center;
  }

  button {
    position: relative;
    left: 50%;
  -ms-transform: translate(-50%, -50%);
  transform: translate(-50%, -50%);
  }
  .hero-container {
    width: 100%; /* Full width */
    min-height: 100vh; /* Full height */
    display: flex;
    align-items: center;
    justify-content: center;
    background-image: url("your-image-url.jpg");
    background-size: cover;
    background-position: center;
  }
</style>
