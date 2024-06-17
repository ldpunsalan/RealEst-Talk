export default {
  plugins: [],
  theme: {
    extend: {
      colors: {
        "cat mauve": "#cba6f7",
        "cat blue": "#89b4fa",
      },
    },
  },
  purge: ["./index.html", "./src/**/*.{svelte,js,ts}"], //for unused css
  variants: {
    extend: {},
  },
  darkmode: false, // or 'media' or 'class'
};
