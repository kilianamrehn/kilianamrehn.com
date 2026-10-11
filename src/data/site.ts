// Zentrale Angaben. Texte und Namen hier ändern, nicht in den Seiten.
export const site = {
  name: 'Kilian Amrehn',
  role: 'Fotograf und App-Entwickler',
  city: 'Köln',
  url: 'https://kilianamrehn.com',
  // E-Mail wird nur zusammengesetzt angezeigt und erst per Klick zur echten Adresse (Schutz vor Bots)
  mailUser: 'hello',
  mailDomain: 'kilianamrehn.com',
  instagram: 'https://www.instagram.com/casual_kilian/',
  linkedin: 'https://www.linkedin.com/in/kilianamrehn/',
  // Name der Zeitungs-Rubrik (noch offen). Adresse bleibt /reportage/ wegen SEO.
  newsTitle: 'Was bleibt',
  newsTitleEn: 'What Remains',
  newsIssue: 'Nº 03',
};

export type Lang = 'de' | 'en';

// Adressen pro Sprache (ohne Base-Pfad, ohne führenden Slash). Deutsch bleibt wegen SEO unverändert.
export const routes = {
  home: { de: '', en: 'en/' },
  artists: { de: 'kuenstlerportraits/', en: 'en/artists/' },
  campaigns: { de: 'kampagnen/', en: 'en/campaigns/' },
  reportage: { de: 'reportage/', en: 'en/reportage/' },
  about: { de: 'ueber/', en: 'en/about/' },
  flashes: { de: 'flashes/', en: 'en/flashes/' },
} as const;
// Kampagnen-Projektseiten: deutsch direkt unter /<slug>/ (alte Adressen), englisch unter /en/campaigns/<slug>/
export const campaignPath = (slug: string, lang: Lang) => (lang === 'de' ? '' : routes.campaigns.en) + slug + '/';

export const nav: Record<Lang, { label: string; href: string }[]> = {
  de: [
    { label: 'Porträts', href: routes.artists.de },
    { label: 'Arbeiten', href: routes.campaigns.de },
    { label: site.newsTitle, href: routes.reportage.de },
    { label: 'Über', href: routes.about.de },
  ],
  en: [
    { label: 'Portraits', href: routes.artists.en },
    { label: 'Work', href: routes.campaigns.en },
    { label: 'Reportage', href: routes.reportage.en },
    { label: 'About', href: routes.about.en },
  ],
};

export const clients = [
  ['VW', 1], ['Coca-Cola', 1], ['TikTok', 1], ['Bundesliga', 1], ['Peek & Cloppenburg', 1], ['Ellesse', 0], ['Copenhagen Studios', 0], ['Eres', 0], ['Scholl', 0], ['AppelrathCüpper', 0],
  ['JBL', 1], ['25hours Hotels', 1], ['Kaufland', 1], ['Hitschler', 0], ['LINDBERG', 0], ['Waterdrop', 0], ['YPS', 0], ['KCA London', 0], ['Imperial', 0], ['IMP Deluxe', 0], ['PNTS', 0],
  ['The Wants', 0], ['Please', 0], ['First Magazine', 0], ["New Icons' Club", 0], ['Morley', 0], ['Bianca Berding', 0],
  ['Bündnis Entwicklung Hilft', 0], ['Kindernothilfe', 0], ['Tagesspiegel', 1],
] as const;
