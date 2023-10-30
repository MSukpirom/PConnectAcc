/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  darkMode: 'media',
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')({
      charts: true,
      forms: true,
      tooltips: true
    }),
    require('daisyui'),
  ],
}
