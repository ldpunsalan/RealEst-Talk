<script>
  import { page } from "$app/stores";
</script>

<header>
  <div class="flex fixed top-4 px-4 w-full justify-center z-50">
    <nav
      class="flex flex-row rounded-full bg-[#1e1e2e99] border-[1px] border-[#89b4fa55] backdrop-blur-md p-1 px-4"
    >
      <div>
        <a
          aria-current={$page.url.pathname === "/" ? "page" : undefined}
          href="#overview"
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
              d="m2.25 15.75 5.159-5.159a2.25 2.25 0 0 1 3.182 0l5.159 5.159m-1.5-1.5 1.409-1.409a2.25 2.25 0 0 1 3.182 0l2.909 2.909m-18 3.75h16.5a1.5 1.5 0 0 0 1.5-1.5V6a1.5 1.5 0 0 0-1.5-1.5H3.75A1.5 1.5 0 0 0 2.25 6v12a1.5 1.5 0 0 0 1.5 1.5Zm10.5-11.25h.008v.008h-.008V8.25Zm.375 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Z"
            />
          </svg>

          <div>Overview</div></a
        >
      </div>
      <div>
        <a
          aria-current={$page.url.pathname === "/" ? "page" : undefined}
          href="#data"
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
              d="M10.5 6a7.5 7.5 0 1 0 7.5 7.5h-7.5V6Z"
            />
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              d="M13.5 10.5H21A7.5 7.5 0 0 0 13.5 3v7.5Z"
            />
          </svg>

          <div>Data</div></a
        >
      </div>
      <div>
        <a
          aria-current={$page.url.pathname === "/" ? "page" : undefined}
          href="#analysis"
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
              d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z"
            />
          </svg>

          <div>Analysis</div></a
        >
      </div>
      <div>
        <a
          aria-current={$page.url.pathname === "/" ? "page" : undefined}
          href="#results"
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
              d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6"
            />
          </svg>

          <div>Results</div></a
        >
      </div>
      <div>
        <a
          aria-current={$page.url.pathname === "/" ? "page" : undefined}
          href="#team"
          class="flex justify-center items-center text-center flex-col"
        >
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
              d="M15.182 15.182a4.5 4.5 0 0 1-6.364 0M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Z"
            />
          </svg>
          <div>Team</div></a
        >
      </div>
    </nav>
  </div>
</header>

<style>
  svg {
    width: 2em;
    height: 3em;
    display: block;
  }

  nav a {
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
