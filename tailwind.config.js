/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./app/templates/**/*.html",
      "./app/static/js/**/*.js"
    ],
    theme: {
      extend: {
        colors: {
          'wood': {
            light: '#8B4513',
            DEFAULT: '#654321',
            dark: '#3B2610'
          }
        }
      },
    },
    plugins: [],
  }