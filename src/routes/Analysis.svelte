<script>
  import Card from "./Card.svelte";
</script>

<main>
  <section id="analysis" class="pt-32">
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
          d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
        />
      </svg>

      <h1
        class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
      >
        Exploratory Data Analysis
      </h1>
    </div>
    <br />
    <div class="flex flex-col">
      <Card>
        <div class="flex flex-row space-x-4 items-center justify-left">
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
              d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 5.25h.008v.008H12v-.008Z"
            />
          </svg>
          <h2 class="text-[#89b4fa]">
            How do real estate prices vary across different cities in the
            Philippines?
          </h2>
        </div>
      </Card>

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
                  <strong
                    >Lowest Average Price per sqm (Highly Urbanized):</strong
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
                <li>
                  <strong
                    >Highest Average Price per sqm (Overall & Non-highly
                    Urbanized):</strong
                  >
                  <p>
                    The Municipality of Malay with <strong
                      >₱545,733.33/sqm</strong
                    >
                  </p>
                </li>
                <br />
                <li>
                  <strong
                    >Highest Average Price per sqm (Highly Urbanized):</strong
                  >
                  <p>
                    The City of Makati with <strong>₱361,331.92/sqm</strong>
                  </p>
                </li>
                <br />
                <li>
                  <strong
                    >Lowest Average Price per sqm (Highly Urbanized):</strong
                  >
                  <p>
                    The City of Bacolod with <strong>₱143,808.05/sqm</strong>
                  </p>
                </li>
                <br />
                <li>
                  <strong
                    >Lowest Average Price per sqm (Overall & Non-highly
                    Urbanized):</strong
                  >
                  <p>
                    The Municipality of Silang with <strong
                      >₱34,814.81/sqm</strong
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
              <h2>Lot Listings</h2>
              <p>This graph shows that for Lot Listings:</p>
              <br />
              <ul style="list-style-type:disc;">
                <li>
                  <strong
                    >Highest Average Price per sqm (Overall & Highly Urbanized):</strong
                  >
                  <p>
                    The City of Muntinlupa with <strong>₱435,000.00/sqm</strong>
                  </p>
                </li>
                <br />
                <li>
                  <strong
                    >Highest Average Price per sqm (Non-highly Urbanized):</strong
                  >
                  <p>
                    The City of Carmona with <strong>₱54,296.00/sqm</strong>
                  </p>
                </li>
                <br />
                <li>
                  <strong
                    >Lowest Average Price per sqm (Highly Urbanized):</strong
                  >
                  <p>
                    The City of Zamboanga with <strong>₱39,234.95/sqm</strong>
                  </p>
                </li>
                <br />
                <li>
                  <strong
                    >Lowest Average Price per sqm (Overall & Non-highly
                    Urbanized):</strong
                  >
                  <p>
                    The Municipality of Polomolok with <strong
                      >₱330.00/sqm</strong
                    >
                  </p>
                </li>
              </ul>
            </div>
          </div>
        </Card>
      </div>
      <br />
      <Card>
        <div class="flex flex-row space-x-4 items-center justify-left">
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
              d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 5.25h.008v.008H12v-.008Z"
            />
          </svg>
          <h2 class="text-[#89b4fa] text-left leading-none">
            Is there a notable variation in the price-to-floor area ratio among
            different types of properties in different Philippine locations?
          </h2>
        </div>
      </Card>
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
            <br />
            <p>This graph shows that, on average:</p>
            <br />
            <ul style="list-style-type:disc;">
              <li>
                House Listings in Highly Urbanized Locations are more expensive
                than in Non-highly Urbanized Locations by <strong
                  >₱54,995.12</strong
                > (~2.81x more).
              </li>
              <br />
              <li>
                Lot Listings in Highly Urbanized Locations are more expensive
                than in Non-highly Urbanized Locations by <strong
                  >₱304,695.60</strong
                > (~10.50x more).
              </li>
              <br />
              <li>
                Condo Unit Listings in Highly Urbanized Locations are more
                expensive than in Non-highly Urbanized Locations by <strong
                  >₱90,200.02</strong
                > (~1.57x more).
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
</style>
