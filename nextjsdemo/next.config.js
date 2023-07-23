/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  publicRuntimeConfig: {
    staticFolder: '/public', // Change this to the correct path for your project
  },
}

module.exports = nextConfig