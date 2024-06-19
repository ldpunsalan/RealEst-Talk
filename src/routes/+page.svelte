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
        Data Preprocessing
      </h1>
    </div>
    <div class="grid grid-cols-4 text-center">
      <Card>
        <h2>Data Cleansing</h2>
        Duplicate entries and entries with a missing price were removed.
        <br /><br />
      </Card>
      <Card>
        <h2>Data Reduction</h2>
        Unnecessary columns were removed (e.g longitude and latitude).
      </Card>
      <div class="grid col-span-2 row-span-2">
        <Card>
          <h2>Data Transformation</h2>
          <br />
          <p>
            Added real estate type as a feature (house / condo unit / lot) -
            house type encompasses houses, townhouses, duplexes while lots
            encompasses commercial and residential
          </p>
          <br />
          <p>
            Added degree of urbanization (highly urbanized / non-highly
            urbanized) based on <a
              href="https://cmci.dti.gov.ph/rankings-data.php?unit=Highly%20Urbanized%20Cities"
              style="color:#89b4fa"><u>DTI 2023 city rankings.</u></a
            >
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
        Answering our Research Questions
      </h1>
    </div>
    <br />
    <div class="flex w-full justify-center grow">
      <h2>
        1. How do real estate prices vary across different cities in the
        Philippines?
      </h2>
    </div>

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
              src="src\lib\images\charts\lot_opaque.png"
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
