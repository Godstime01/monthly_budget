/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './core/templates/**/*.html',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    colors: {
      'background': 'var(--base)',
      'white': 'var(--light)',
      'button': 'var(--yellow)',
      'accent': 'var(--green)',
      'box-bg': 'var(--box-bg)',
      'red': 'var(--error)',
    },
  },
  plugins: [
    require('flowbite/plugin')({
      charts: true,
  }),
  ]
}

