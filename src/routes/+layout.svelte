<script>
  import Header from "./Header.svelte";
  import "./styles.css";
  import { page } from "$app/stores";
</script>

<div class="app">
  <Header />

  <main>
    <slot />
  </main>

  <footer
    class="flex fixed bottom-10 right-10 rounded-full bg-[#1e1e2e99] border-[1px] border-[#89b4fa55] backdrop-blur-md p-1 px-4"
  >
    <div>
      <a
        aria-current={$page.url.pathname === "/" ? "page" : undefined}
        href="#top"
        class="flex justify-center items-center text-center flex-col"
        ><svg
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
            d="M8.25 6.75 12 3m0 0 3.75 3.75M12 3v18"
          />
        </svg>
        <div>Top</div></a
      >
    </div>
  </footer>
</div>

<style>
  .app {
    display: flex;
    flex-direction: column;
    min-height: 100vh;
  }

  main {
    flex: 1;
    display: flex;
    flex-direction: column;
    padding: 1rem;
    width: 100%;
    max-width: 64rem;
    margin: 0 auto;
    box-sizing: border-box;
  }

  svg {
    width: 2em;
    height: 3em;
    display: block;
  }

  footer a {
    display: flex;
    height: 100%;
    align-items: center;
    padding: 0.5rem 0.5rem;
    color: var(--color-text);
    font-size: 0.7rem;
    text-decoration: none;
    transition: color 0.2s linear;
  }
  a:hover {
    color: var(--color-theme-1);
  }

  path {
    fill: var(--background);
  }
</style>
