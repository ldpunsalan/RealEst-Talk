<script>
  import Card from "./Card.svelte";

  let point1 = false;
  let point2 = false;
  let point3 = false;

  const toggle1 = () => {
    point1 = !point1;
  };

  const toggle2 = () => {
    point2 = !point2;
  };

  const toggle3 = () => {
    point3 = !point3;
  };
</script>

<main>
  <section id="results" class="pt-32">
    <div
      class="flex xs:flex-col sm:flex-row items-center justify-center space-x-4"
    >
      <div>
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
            d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6"
          />
        </svg>
      </div>
      <div>
        <h1
          class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
        >
          Results
        </h1>
      </div>
    </div>
    <div class="flex flex-col">
      <Card class="flex">
        <p class="text-center">
          From the statistical testing and EDA in the analysis, real estate is
          indeed more expensive in highly urbanized areas of the Philippines
          compared to the less urbanized areas regardless of real estate type.
          This underscores the influence of urbanization on property values,
          which can be crucial for urban planning and development policies
          especially in light of more people being unable to afford homes in
          urban centers.
        </p>
      </Card>
      
      <button on:click={toggle1}>
        <Card>
          <div class="flex items-center space-x-2">
            <div class="flex grow">
              <h2>
                Strong demand but limited supply exacerbates housing
                unaffordability.
              </h2>
            </div>
            <div>
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
                    d="m19.5 8.25-7.5 7.5-7.5-7.5"
                  />
                </svg>
            </div>
          </div>
          {#if point1}
            <p>
              Looking at the bar graph above, it can be seen that in general, when
              it comes to the different types of real estate (lots, houses, condo
              units), the difference is significantly larger between lots in
              highly urbanized locations compared to less urbanized locations. The
              larger price difference for lots suggests a higher demand for land
              in urban centers, which might be due to commercial development
              opportunities. On the other hand, the difference is least observed
              for condo units. The observed differences in price gaps between
              highly and less urbanized areas for different real estate types
              (especially lots and houses) indicate a strong demand but limited
              supply of affordable land and housing. This imbalance exacerbates
              housing unaffordability as more people compete for fewer available
              properties, pushing prices higher.
            </p>
          {/if}
        </Card>
      </button>
      <button on:click={toggle2}>
      <Card>
        <div class="flex items-center space-x-2">
          <h2 class="flex grow">Good investment opportunities.</h2>
          <div>
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
                  d="m19.5 8.25-7.5 7.5-7.5-7.5"
                />
              </svg>
          </div>
        </div>
        {#if point2}
          <p>
            The tree maps for each real estate type also reinforce the fact that
            real estate located in highly urbanized cities (colored blue) have a
            more expensive price per square meter compared to less urbanized
            cities (colored yellow) since across different real estate types,
            most of the blue squares are larger. For houses, Zamboanga proves to
            be an outlier by being a highly urbanized city with house pricing on
            the cheaper side. Recognizing outliers like Zamboanga, where house
            prices are cheaper despite being a highly urbanized city, can inform
            the public of good investment opportunities.
          </p>
        {/if}
      </Card>
      </button>
      <button on:click={toggle3}>
      <Card>
        <div class="flex items-center space-x-2">
          <h2 class="flex grow">
            High-end developments can lead to gentrification.
          </h2>
          <div>
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
                  d="m19.5 8.25-7.5 7.5-7.5-7.5"
                />
              </svg>
          </div>
        </div>
        {#if point3}
          <p>
            The tree map for lots show that the average price per sqm for real
            estate lots in Muntinlupa is a lot larger than the rest of the
            locations represented in the data. Upon closer look, the listings
            for Muntinlupa fall under Alabang which is home to luxury properties
            such as real estate within the Ayala Alabang Village (one of the
            most expensive subdivisions in the Philippines). Interestingly, for
            condo units, the top two cities with a high average price per sqm
            are non-highly urbanized cities, particularly Malay and San Vicente.
            However, these two cities are in Boracay and Palawan respectively,
            which are top tourist destinations in the Philippines which could
            explain the increase in real estate pricing. These data highlight
            how specific local factors can influence real estate markets. These
            luxury properties in Alabang and tourist destinations in Boracay and
            Palawan, illustrates how high-end developments can lead to
            gentrification. This process often results in the displacement of
            lower-income residents who can no longer afford to live in these
            areas.
          </p>
        {/if}
      </Card>
      </button>
      <Card>
        <div class="flex items-center space-x-2">
          <svg
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
              d="M15.182 16.318A4.486 4.486 0 0 0 12.016 15a4.486 4.486 0 0 0-3.198 1.318M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Z"
            />
          </svg>

          <h2>Limitations</h2>
        </div>
        <p>
          While the data scraped from Lamudi provided some insights on the
          current state of real estate pricing in different parts of the
          Philippines, it is important to note the limitations of said data. The
          team scraped all available 1500 available listings in Lamudi which was
          further reduced to 1196 viable listings. The limited data was not able
          to represent different types of real estate for many other cities
          within the Philippines. Lamudi is also only one real estate listing
          website among many others and its content can be limited to agents
          using said website.
        </p>
      </Card>
    </div>
  </section>

  <section class="pt-32">
    <div
      class="flex xs:flex-col sm:flex-row items-center justify-center space-x-4"
    >
      <div>
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
            d="M9 12.75 11.25 15 15 9.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
          />
        </svg>
      </div>
      <div>
        <h1
          class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
        >
          Conclusion
        </h1>
      </div>
    </div>

    <Card>
      <p>
        The analysis confirms that real estate prices in the Philippines are
        significantly higher in highly urbanized areas compared to less
        urbanized regions, affecting all property types. This underscores the
        need for strategic urban planning to address housing affordability
        especially in urban centers in the country. The study was also able to
        pinpoint outliers with cheaper prices despite high urbanization,
        presenting investment opportunities for the public. Specific local
        factors, such as luxury developments in Alabang and tourism in Boracay
        and Palawan, are shown to influence the pricing of real estate
        regardless of urbanization. However, this promotes gentrification and
        leads to further housing problems by displacing lower-income residents.
        These insights can be further strengthened by incorporating a broader
        dataset for a more comprehensive analysis. Despite this, the study
        proves to be a start in analyzing the housing problem in the
        Philippines. Policymakers should develop and enforce urban planning
        strategies that address the disparities in real estate prices and ensure
        affordable housing in highly urbanized areas. Furthermore, the
        government must encourage inclusive development practices that prevent
        gentrification and displacement of lower-income residents, ensuring that
        all income groups have access to housing.
      </p>
    </Card>
  </section>
</main>

<style>
</style>
