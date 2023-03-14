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
      'khaki': '#F6E288',
      'maximum-blue-green': '#2EC4B6',
      'alizarin-crimson': '#E71D36',
      'maastricht-blue': '#011627',
      'white': '#FFFFFF',
      'black': '#000000',
      'transparent': 'transparent',
    },
    extend: {
      fontSize: {
        '10xl': '156px',
      }
    },
  },
  plugins: [],
}
