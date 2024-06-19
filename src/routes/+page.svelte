<script>
  import Counter from "./Counter.svelte";
  import Card from "./Card.svelte";
  import welcome from "$lib/images/svelte-welcome.webp";
  import welcome_fallback from "$lib/images/svelte-welcome.png";
</script>

<svelte:head>
  <title>Home</title>
  <meta name="description" content="Svelte demo app" />
</svelte:head>

<section class="hero-container">
  <div class="flex xs:flex-col xs:items-center md:flex-row md:space-x-10">
    <div class="flex flex-col">
      <h1
        style="font-size: 5rem;"
        class="text-left leading-none font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#cba6f7] to-[#89b4fa]"
      >
        Real<span class="text-white">(i)</span>ty Check
      </h1>
      <p>
        An analysis of real estate prices across different cities in the
        Philippines
      </p>
      <p>by RealEst Talk</p>
    </div>

    <Card id="Background">
      <h1
        class="text-left font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
      >
        Background
      </h1>
      <p class="text-left">
        The Philippine real estate market is influenced by various factors,
        including economic growth, infrastructure development, and population
        density. There is a pressing issue of housing affordability,
        particularly in urban areas, where real estate prices continue to rise,
        and making homeownership increasingly inaccessible for many segments of
        the population. This has led to housing insecurity, forced evictions,
        informal settlements, and social exclusion, exacerbating inequalities
        and hindering sustainable urban development.
      </p>
    </Card>
  </div>
</section>
<br /><br />
<section>
  <h1
    class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
  >
    Overview
  </h1>
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
        Affordable housing is increasingly becoming a problem amidst the rising
        prices of real estate in across the country.
      </p>
    </Card>
    <Card>
      <h2>Solution</h2>
      <p>
        Pinpoint areas where housing is becoming inaccessible and expensive
        through a statistical comparative analysis of real estate prices and the
        price-to-floor area ratio among property types across different
        Philippine cities.
      </p>
    </Card>
  </div>
</section>
<br /><br />
<section>
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
        real estate in highly urbanized cities compared to non-highly urbanized
        areas.
      </p>
    </Card>
    <Card>
      <h2>Alternative</h2>
      <p>
        Real estate in more highly urbanized cities of the Philippines are more
        expensive than their counterparts in non-highly urbanized areas of the
        country.
      </p>
    </Card>
  </div>
</section>

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
