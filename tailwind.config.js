/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/**/*.js",
    "./app/static/**/*.css",
  ],
  theme: {
    extend: {
      // colors: {
      //   primary: "#0046b5",
      //   "primary-hover": "#003580",
      //   bg: "#f8f9fe",
      //   border: "#e5e7eb",
      //   text: "#4b5563",
      //   "text-dark": "#1a1a1a",
      //   "active-bg": "#e7efff",
      //   "active-text": "#0046b5",
      // },
    },
  },
  plugins: [],
};
