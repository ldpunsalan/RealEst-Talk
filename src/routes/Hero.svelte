<script>
  import Card from "./Card.svelte";
</script>

<main>
  <section class="hero-container">
    <div class>
      <img
        src="/src/lib/images/logo.svg"
        alt="Logo"
        class="w-1/2 h-1/2 mx-auto"
      />
      <br />
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
    </div>
  </section>
</main>

<style>
  .hero-container {
    width: 100%; /* Full width */
    min-height: 100vh; /* Full height */
    display: flex;
    align-items: center;
    justify-content: center;
    background-size: cover;
    background-position: center;
  }
</style>
