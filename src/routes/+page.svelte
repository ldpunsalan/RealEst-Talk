<script>
  import Card from "./Card.svelte";
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Real(i)ty Check" />
</svelte:head>

<main>
  <section class="hero-container px-20">
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
  <section id="overview" class="px-20">
    <div class="flex flex-row items-center space-x-4">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke-width="1.5"
        stroke="var(--color-theme-1)"
        class="size-12"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
        />
      </svg>
      <h1
        class="text-left bg-clip-text bg-clip-text text-transparent bg-gradient-to-r from-[#cba6f7] to-[#89b4fa]"
      >
        Overview
      </h1>
    </div>
    <p class="text-center">
      The Philippine real estate market is influenced by various factors,
      including economic growth, infrastructure development, and population
      density. There is a pressing issue of housing affordability, particularly
      in urban areas, where real estate prices continue to rise, and making
      homeownership increasingly inaccessible for many segments of the
      population. This has led to housing insecurity, forced evictions, informal
      settlements, and social exclusion, exacerbating inequalities and hindering
      sustainable urban development.
    </p>
    <div class="flex flex-row space-x-4">
      <Card>
        <h2>Objective</h2>
        <p>
          The aim is to assess the affordability of housing, state of urban
          planning and economic health of the different regions in the country.
        </p>
      </Card>
      <Card>
        <h2>Problem</h2>
        <p>
          Affordable housing is increasingly becoming a problem amidst the
          rising prices of real estate in across the country.
        </p>
      </Card>
      <Card>
        <h2>Solution</h2>
        <p>
          Pinpoint areas where housing is becoming inaccessible and expensive
          through a statistical comparative analysis of real estate prices and
          the price-to-floor area ratio among property types across different
          Philippine cities.
        </p>
      </Card>
    </div>
  </section>
  <br /><br />
  <section id="overview" class="px-20">
    <h1
      class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
    >
      Hypotheses
    </h1>
    <div class="flex flex-row space-x-4">
      <Card>
        <h2>Null</h2>
        <p>
          There is no significant difference between prices of similar types of
          real estate in highly urbanized cities compared to non-highly
          urbanized areas.
        </p>
      </Card>
      <Card>
        <h2>Alternative</h2>
        <p>
          Real estate in more highly urbanized cities of the Philippines are
          more expensive than their counterparts in non-highly urbanized areas
          of the country.
        </p>
      </Card>
    </div>
  </section>
</main>

<style>
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
