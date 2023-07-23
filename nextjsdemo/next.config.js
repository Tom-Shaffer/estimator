/** @type {import('next').NextConfig} */
const nextConfig = {
  basePath: '/estimator', 
  reactStrictMode: true,
  publicRuntimeConfig: {
    staticFolder: '/public',
  },
}

module.exports = nextConfig