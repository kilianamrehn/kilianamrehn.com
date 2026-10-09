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
  newsIssue: 'Nº 03',
};

export const nav = [
  { label: 'Artists', href: 'kuenstlerportraits/' },
  { label: 'Kampagnen', href: 'kampagnen/' },
  { label: site.newsTitle, href: 'reportage/' },
  { label: 'Über', href: 'ueber/' },
];

export const clients = [
  ['VW', 1], ['Coca-Cola', 1], ['TikTok', 1], ['Bundesliga', 1], ['Peek & Cloppenburg', 1], ['Ellesse', 0], ['Copenhagen Studios', 0], ['Eres', 0], ['Scholl', 0], ['AppelrathCüpper', 0],
  ['JBL', 1], ['25hours Hotels', 1], ['Kaufland', 1], ['Hitschler', 0], ['LINDBERG', 0], ['Waterdrop', 0], ['YPS', 0], ['KCA London', 0], ['Imperial', 0], ['IMP Deluxe', 0], ['PNTS', 0],
  ['The Wants', 0], ['Please', 0], ['First Magazine', 0], ["New Icons' Club", 0], ['Morley', 0], ['Bianca Berding', 0],
  ['Bündnis Entwicklung Hilft', 0], ['Kindernothilfe', 0], ['Tagesspiegel', 1],
] as const;
