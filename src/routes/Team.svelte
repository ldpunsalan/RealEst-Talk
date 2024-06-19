<script>
  import Card from "./Card.svelte";
</script>

<main>
  <section id="team" class="pt-32">
    <div class="flex flex-row justify-content items-center space-x-4">
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
          d="M15.182 15.182a4.5 4.5 0 0 1-6.364 0M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0ZM9.75 9.75c0 .414-.168.75-.375.75S9 10.164 9 9.75 9.168 9 9.375 9s.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Zm5.625 0c0 .414-.168.75-.375.75s-.375-.336-.375-.75.168-.75.375-.75.375.336.375.75Zm-.375 0h.008v.015h-.008V9.75Z"
        />
      </svg>
      <h1
        class="font-bold bg-clip-text text-transparent bg-gradient-to-r from-[#89b4fa] to-[#cba6f7]"
      >
        The Team
      </h1>
    </div>
    <Card>
      <p class="text-center">
        We are a team of 3 people studying data science that aim to use data
        science to gain insights about the country's current economical state.
        In our project, Real(i)ty Check, we aim to delve into the landscape of
        property prices in the Philippines. We are interested in how the
        urbanization of different Philippine cities has affected the price of
        real estate. With this, we hope that we are able to successfully
        identify the areas where housing is becoming unaffordable.
      </p>
    </Card>
    <div class="flex flex-row space-x-4">
      <Card>
        <img
          src="src\images\team\ray.png"
          class="h-auto hover:scale-150 ease-in duration-500 object-cover rounded-full"
          alt=""
        />
        <br />
        <h2>Ray Nuñez</h2>
        <p class="text-center">
          a computer science student interested in data science, bioinformatics,
          and web development.
        </p>
      </Card>

      <Card>
        <img
          src="src\images\team\chase.png"
          class="h-auto hover:scale-150 ease-in duration-500 object-cover rounded-full"
          alt=""
        />
        <br />
        <h2>Chase Gonzaga</h2>
        <p class="text-center">
          a computer science student interested in web development, game
          development, and data science.
        </p>
      </Card>
      <Card>
        <img
          src="src\images\team\lara.png"
          class="h-auto hover:scale-150 ease-in duration-500 object-cover rounded-full"
          alt=""
        />
        <br />
        <h2>Lara Punsalan</h2>
        <p class="text-center">
          a computer science student interested in UI/UX, web development, and
          app development.
        </p>
      </Card>
    </div>
  </section>
</main>

<style></style>
