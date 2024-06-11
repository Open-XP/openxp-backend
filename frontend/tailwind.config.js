/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      padding: {
        "dash-left": "32rem",
        "dash-top": "10rem",
      },
      fontFamily: {
        sans: ["Open Sans", "ui-sans-serif", "system-ui"],
      },
      boxShadow: {
        custom: " 0 1px 0 rgba(0, 0, 0, 0.5)",
        custom2: "0px 1px 21px 0px rgba(0, 0, 0, 0.08)",
      },
      backgroundImage: {
        "custom-gradient":
          "linear-gradient(167.66deg, #3F2A7D 5.71%, rgba(63, 42, 125, 0.8) 71.15%)",
      },
      borderColor: {
        "custom-border": "#281266",
      },
      borderWidth: {
        1: "1px",
      },
      colors: {
        "purple-primary": "#281266",
        "skyblue-secondary": "#2D9CDB",
      },
    },
  },
  plugins: [
    require("flowbite/plugin")({
      charts: true,
    }),
  ],
};
