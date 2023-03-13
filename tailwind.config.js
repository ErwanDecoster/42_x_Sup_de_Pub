module.exports = {
  mode: 'jit',
  content: [
    "./assets/**/*.css",
    "./components/*.{vue,js}",
    "./components/**/*.{vue,js}",
    "./pages/*.vue",
    "./pages/**/*.vue",
    "./plugins/**/*.{js,ts}",
    "./app.{vue,js,ts}",
  ],
  theme: {
    colors: {
      'almond': '#EEDECC',
    },
    extend: {
    },
  },
  plugins: [],
}
