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
  linkedin: '', // TODO: LinkedIn-URL eintragen
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
  ['Copenhagen Studios', 0], ['Peek & Cloppenburg x Ellesse', 1], ['Scholl', 0], ['AppelrathCüpper', 0], ['Bundesliga', 1], ['VW', 0], ['JBL', 0], ['25hours Hotels', 0],
  ['Morley', 1], ['Bianca Berding', 0], ["New Icons' Club", 0], ['Bündnis Entwicklung Hilft', 1], ['Kindernothilfe', 0], ['Tagesspiegel', 0],
] as const;
