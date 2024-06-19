<script>
  import Card from "./Card.svelte";
  import barchart_opaque from "$lib/images/charts/barchart_opaque.png";
  import condo_opaque from "$lib/images/charts/condo_opaque.png";
  import condohisto from "$lib/images/charts/condohisto.png";
  import house_opaque from "$lib/images/charts/house_opaque.png";
  import househisto from "$lib/images/charts/househisto.png";
  import lot_opaque from "$lib/images/charts lot_opaque.png";
  import lothisto from "$lib/images/charts lothisto.png";
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
                src={house_opaque}
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
                src={condo_opaque}
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
                src={lot_opaque}
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
              src={barchart_opaque}
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
          d="m16.862 4.487 1.687-1.688a1.875 1.875 0 1 1 2.652 2.652L10.582 16.07a4.5 4.5 0 0 1-1.897 1.13L6 18l.8-2.685a4.5 4.5 0 0 1 1.13-1.897l8.932-8.931Zm0 0L19.5 7.125M18 14v4.75A2.25 2.25 0 0 1 15.75 21H5.25A2.25 2.25 0 0 1 3 18.75V8.25A2.25 2.25 0 0 1 5.25 6H10"
        />
      </svg>

      <h1
        class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
      >
        Statistical Test
      </h1>
    </div>
    <br />

    <div class="flex flex-col">
      <Card>
        <p class="text-center">
          We want to test if there is a significant difference in the average
          price per sqm in highly urbanized cities vs non-highly urbanized
          cities for different real estate types. Since we are dealing with a
          categorical variable (highly urbanized or not) and continuous variable
          (price per square meter), we can use either the independent t-test or
          the Mann-Whitney U test depending on the normality of our data.
        </p>
        <br /> <br />
        <button class="flex flex-row space-x-2">
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
              d="M13.19 8.688a4.5 4.5 0 0 1 1.242 7.244l-4.5 4.5a4.5 4.5 0 0 1-6.364-6.364l1.757-1.757m13.35-.622 1.757-1.757a4.5 4.5 0 0 0-6.364-6.364l-4.5 4.5a4.5 4.5 0 0 0 1.242 7.244"
            />
          </svg>

          <a
            href="https://github.com/ldpunsalan/RealEst-Talk/blob/main/Data%20Analysis/StatisticalTest.ipynb"
          >
            Let's take a look at our tests!</a
          >
        </button>
      </Card>
      <Card>
        <div class="text-center">
          <div class="flex flex-row space-x-4 justify-center">
            <svg
              width="100px"
              height="100px"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="var(--color-theme-1)"
              class="size-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="m2.25 12 8.954-8.955c.44-.439 1.152-.439 1.591 0L21.75 12M4.5 9.75v10.125c0 .621.504 1.125 1.125 1.125H9.75v-4.875c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21h4.125c.621 0 1.125-.504 1.125-1.125V9.75M8.25 21h8.25"
              />
            </svg>
            <h2>House</h2>
          </div>

          <p>We check the normality to determine which test to use.</p>
          <br />
          <img src={househisto} alt="" class="mx-auto" />
          <br />
          <p>
            Since our histogram fails to show a bell curve, we cannot assume
            normality of data. <br />
            Hence we use the <b>Mann-Whitney U test</b> to obtain a p-value.
          </p>
          <p>
            With a significance level of 0.05 and a p-value of 1.5365x10<sup
              >-29</sup
            >,
            <b>we reject our null hypothesis</b>. Therefore, the price per sqm
            for houses in highly-urbanized areas are
            <b>significantly different</b> from less urbanized areas.
          </p>
        </div>
      </Card>
      <Card>
        <div class="text-center">
          <div class="flex flex-row space-x-4 justify-center">
            <svg
              width="100px"
              height="100px"
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
                d="M2.25 21h19.5m-18-18v18m10.5-18v18m6-13.5V21M6.75 6.75h.75m-.75 3h.75m-.75 3h.75m3-6h.75m-.75 3h.75m-.75 3h.75M6.75 21v-3.375c0-.621.504-1.125 1.125-1.125h2.25c.621 0 1.125.504 1.125 1.125V21M3 3h12m-.75 4.5H21m-3.75 3.75h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Zm0 3h.008v.008h-.008v-.008Z"
              />
            </svg>
            <h2>Condo Unit</h2>
          </div>

          <p>We check the normality to determine which test to use.</p>
          <br />
          <img src={condohisto} alt="" class="mx-auto" />
          <br />
          <p>
            Since our histogram fails to show a bell curve, we cannot assume
            normality of data. <br />
            Hence we use the <b>Mann-Whitney U test</b> to obtain a p-value.
          </p>
          <p>
            With a significance level of 0.05 and a p-value of 1.7498x10<sup
              >-13</sup
            >,
            <b>we reject our null hypothesis</b>. Therefore, the price per sqm
            for condo units in highly-urbanized areas are
            <b>significantly different</b> from less urbanized areas.
          </p>
        </div>
      </Card>
      <Card>
        <div class="text-center">
          <div class="flex flex-row space-x-4 justify-center">
            <svg
              width="100px"
              height="100px"
              mlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="size-6"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M6.429 9.75 2.25 12l4.179 2.25m0-4.5 5.571 3 5.571-3m-11.142 0L2.25 7.5 12 2.25l9.75 5.25-4.179 2.25m0 0L21.75 12l-4.179 2.25m0 0 4.179 2.25L12 21.75 2.25 16.5l4.179-2.25m11.142 0-5.571 3-5.571-3"
              />
            </svg>
            <h2>Lot</h2>
          </div>

          <p>We check the normality to determine which test to use.</p>
          <br />
          <img src={lothisto} alt="" class="mx-auto" />
          <br />
          <p>
            Since our histogram fails to show a bell curve, we cannot assume
            normality of data. <br />
            Hence we use the <b>Mann-Whitney U test</b> to obtain a p-value.
          </p>
          <p>
            With a significance level of 0.05 and a p-value of 9.0916x10<sup
              >-9</sup
            >,
            <b>we reject our null hypothesis</b>. Therefore, the price per sqm
            for lots in highly-urbanized areas are
            <b>significantly different</b> from less urbanized areas.
          </p>
        </div>
      </Card>
    </div>
  </section>
</main>

<style>
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

  button:hover > * {
    color: var(--color-text);
  }

  svg {
    color: var(--color-bg-0);
  }
</style>
