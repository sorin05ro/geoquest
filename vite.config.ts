import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { VitePWA } from 'vite-plugin-pwa';

// base './' => aplicația merge din orice subfolder (GitHub Pages: utilizator.github.io/geoquest/)
export default defineConfig({
  base: './',
  plugins: [
    react(),
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['icons/*.svg', 'icons/*.png'],
      manifest: {
        name: 'GeoQuest – geografie pentru gimnaziu',
        short_name: 'GeoQuest',
        description: 'Geografie pentru clasele V–VIII, ca o expediție.',
        lang: 'ro',
        start_url: './',
        scope: './',
        display: 'standalone',
        background_color: '#f3f7f6',
        theme_color: '#12355b',
        icons: [
          { src: 'icons/icon-192.png', sizes: '192x192', type: 'image/png' },
          { src: 'icons/icon-512.png', sizes: '512x512', type: 'image/png' },
          { src: 'icons/icon-maskable-512.png', sizes: '512x512', type: 'image/png', purpose: 'maskable' },
        ],
      },
      workbox: {
        // codul și fonturile se salvează la instalare; conținutul unei lumi, la prima intrare în ea
        globPatterns: ['**/*.{js,css,html,svg,png,woff2}'],
        runtimeCaching: [
          {
            urlPattern: ({ url }) => /\/(content|calendar|config)\//.test(url.pathname),
            handler: 'StaleWhileRevalidate',
            options: { cacheName: 'geoquest-continut', expiration: { maxEntries: 200 } },
          },
        ],
      },
    }),
  ],
  test: { environment: 'node' },
});
