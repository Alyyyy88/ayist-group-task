/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/js/*.js",
    "./app/static/**/*.css",
  ],
  theme: {
    extend: {
      colors: {
        // primarybackground: "var(--primary-background)",
        // cardbackground: "var(--card-background)",
        // elevatedcarddialog: "var(--elevated-card-dialog)",
        // secondarybackground: "var(--secondary-background)",
        // primarytext: "var(--primary-text)",
        // secondarytext: "var(--secondary-text)",
        // subtletext: "var(--subtle-text)",
        // verysubtletext: "var(--very-subtle-text)",
        // primaryborder: "var(--primary-border)",
        // subtleborder: "var(--subtle-border)",
        // primarybutton: "var(--primary-button)",
        // primarybuttonhover: "var(--primary-button-hover)",
        // secondarybutton: "var(--secondary-button)",
        // secondarybuttonhover: "var(--secondary-button-hover)",
        // regularshadow: "var(--regular-shadow)",
        // hovershadow: "var(--hover-shadow)",
      },
    },
  },
  plugins: [],
  darkMode: "class",
};
