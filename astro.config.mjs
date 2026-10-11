import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Solange die Seite unter kilianamrehn.github.io/kilianamrehn.com/ läuft, setzt der Deploy
// BASE_PATH=/kilianamrehn.com. Sobald die eigene Domain aktiv ist, fällt BASE_PATH weg.
const base = process.env.BASE_PATH || '/';

// Alte WordPress-Adressen -> neue Seiten (erhält das Google-Ranking beim Umzug)
const redirects = {
  '/about-kilian-amrehn': '/ueber/',
  '/de/ueber': '/ueber/',
  '/contact': '/ueber/#kontakt',
  '/de/kontakt': '/ueber/#kontakt',
  '/journal': '/reportage/',
  '/journal-alt': '/reportage/',
  '/imprint': '/impressum/',
  '/de/impressum-datenschutz': '/impressum/',
  '/home-2': '/',
  '/de': '/',
  '/lea-mende': '/kuenstlerportraits/#lea-mende',
  '/pia-stutzenstein': '/kuenstlerportraits/#pia-stutzenstein',
  '/slavko-popadic': '/kuenstlerportraits/#slavko-popadic',
  '/david-vormweg': '/kuenstlerportraits/#david-vormweg',
  '/pntsbeach': '/pnts/',
  '/scholl-comfort': '/scholl-iconic/',
  '/scholl-comfort-2': '/scholl-iconic/',
  '/mood-2': '/',
};

export default defineConfig({
  site: 'https://kilianamrehn.com',
  base,
  trailingSlash: 'always',
  redirects: Object.fromEntries(Object.entries(redirects).map(([k, v]) => [k, (base.replace(/\/$/, '') + v)])),
  integrations: [sitemap({ filter: (p) => !p.includes('/impressum') && !p.includes('/datenschutz') })],
  image: { responsiveStyles: false },
});
