/**
 * @format
 * @type {import('tailwindcss').Config}
 */

export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      fontFamily: {
        inter: ['"Quicksand"', "sans-serif"],
      },
      colors: {
        primary: "#B3225F",
        secondary: "#47A1C4",
        darkBg: "#0A2B42",
        textGray: "#84848c",
      },
      // backgroundImage: {
      //   Hero: '#111',
      // },
    },
    // screens: {
    //   // => @media (max-width: 1279px) { ... }
    //   lg: { min: '1025px' },
    // },
  },
  plugins: [],
};
