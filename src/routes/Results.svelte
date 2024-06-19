<script>
  import Card from "./Card.svelte";
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
              d="M3 3v1.5M3 21v-6m0 0 2.77-.693a9 9 0 0 1 6.208.682l.108.054a9 9 0 0 0 6.086.71l3.114-.732a48.524 48.524 0 0 1-.005-10.499l-3.11.732a9 9 0 0 1-6.085-.711l-.108-.054a9 9 0 0 0-6.208-.682L3 4.5M3 15V4.5"
            />
          </svg>
          <h2>Strong demand but limited supply exacerbates housing unaffordability. </h2>
        </div>
        <p>
          Looking at the bar graph above, it can be seen that in general, when
          it comes to the different types of real estate (lots, houses, condo
          units), the difference is significantly larger between lots in highly
          urbanized locations compared to less urbanized locations. The larger
          price difference for lots suggests a higher demand for land in urban
          centers, which might be due to commercial development opportunities.
          On the other hand, the difference is least observed for condo units.
          The observed differences in price gaps between highly and less
          urbanized areas for different real estate types (especially lots and
          houses) indicate a strong demand but limited supply of affordable land
          and housing. This imbalance exacerbates housing unaffordability as
          more people compete for fewer available properties, pushing prices
          higher.
        </p>
      </Card>
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
              d="M9.879 7.519c1.171-1.025 3.071-1.025 4.242 0 1.172 1.025 1.172 2.687 0 3.712-.203.179-.43.326-.67.442-.745.361-1.45.999-1.45 1.827v.75M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 5.25h.008v.008H12v-.008Z"
            />
          </svg>
          <h2>Good investment opportunities.</h2>
        </div>
        <p>
          The tree maps for each real estate type also reinforce the fact that
          real estate located in highly urbanized cities (colored blue) have a
          more expensive price per square meter compared to less urbanized
          cities (colored yellow) since across different real estate types, most
          of the blue squares are larger. For houses, Zamboanga proves to be an
          outlier by being a highly urbanized city with house pricing on the
          cheaper side. Recognizing outliers like Zamboanga, where house prices
          are cheaper despite being a highly urbanized city, can inform the
          public of good investment opportunities.
        </p>
      </Card>
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
              d="M12 9v3.75m9-.75a9 9 0 1 1-18 0 9 9 0 0 1 18 0Zm-9 3.75h.008v.008H12v-.008Z"
            />
          </svg>

          <h2>High-end developments can lead to gentrification.</h2>
        </div>
        <p>
          The tree map for lots show that the average price per sqm for real
          estate lots in Muntinlupa is a lot larger than the rest of the
          locations represented in the data. Upon closer look, the listings for
          Muntinlupa fall under Alabang which is home to luxury properties such
          as real estate within the Ayala Alabang Village (one of the most
          expensive subdivisions in the Philippines). Interestingly, for condo
          units, the top two cities with a high average price per sqm are
          non-highly urbanized cities, particularly Malay and San Vicente.
          However, these two cities are in Boracay and Palawan respectively,
          which are top tourist destinations in the Philippines which could
          explain the increase in real estate pricing. These data highlight how
          specific local factors can influence real estate markets. These luxury
          properties in Alabang and tourist destinations in Boracay and Palawan,
          illustrates how high-end developments can lead to gentrification. This
          process often results in the displacement of lower-income residents
          who can no longer afford to live in these areas.
        </p>
      </Card>
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
              d="M15 12H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"
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
            d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6"
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
