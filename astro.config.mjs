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
  '/phiala': '/kuenstlerportraits/#phiala',
  '/marie-dahmen': '/kuenstlerportraits/',
  '/synergy': '/kuenstlerportraits/#synergy',
  '/trish-reflections-of-identity': '/kuenstlerportraits/#trish',
  '/silent-escape': '/kampagnen/',
  '/pnts': '/kampagnen/',
  '/pntsbeach': '/kampagnen/',
  '/monano-schmuck': '/kampagnen/',
  '/new-icons-club-magazine': '/rock-fairyland/',
  '/new-icons-club-magazine-2': '/rock-fairyland/',
  '/appelrathcuepper': '/kampagnen/',
  '/scholl-iconic': '/kampagnen/',
  '/scholl-comfort': '/kampagnen/',
  '/scholl-comfort-2': '/kampagnen/',
  '/the-wants': '/kampagnen/',
  '/bundesliga': '/kampagnen/',
  '/mood-2': '/',
  '/flashes': '/ueber/',
};

export default defineConfig({
  site: 'https://kilianamrehn.com',
  base,
  trailingSlash: 'always',
  redirects: Object.fromEntries(Object.entries(redirects).map(([k, v]) => [k, (base.replace(/\/$/, '') + v)])),
  integrations: [sitemap({ filter: (p) => !p.includes('/impressum') && !p.includes('/datenschutz') })],
  image: { responsiveStyles: false },
});
