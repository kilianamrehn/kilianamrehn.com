export type Credit = [string, string];
// Englische Texte jeweils im Feld mit Endung En (metaEn, introEn, heroAltEn, altEn). Rollen im Abspann übersetzt roleEn.
export type Kampagne = { slug: string; title: string; titleHtml: string; meta: string; metaEn: string; color: string; accent: string; hero: string; heroAlt: string; heroAltEn: string; pics: { src: string; alt: string; altEn: string }[]; intro: string; introEn: string; credits: Credit[] };

// Slugs = alte Adressen von kilianamrehn.com, damit Google-Ranking erhalten bleibt
export const kampagnen: Kampagne[] = [
  { slug: 'copenhagen-studios', title: 'Copenhagen Studios', titleHtml: 'Copenhagen<br>Studios', meta: 'Kampagne · 2022', metaEn: 'Campaign · 2022', color: '#6a2a0c', accent: '#e8a27e',
    hero: 'copenhagen-studios-kampagne', heroAlt: 'Copenhagen Studios Kampagne, Model mit orangen Sandalen', heroAltEn: 'Copenhagen Studios campaign, model in orange sandals', pics: [],
    intro: '[2 bis 3 Sätze zur Kampagne.]', introEn: '[2 to 3 sentences about the campaign.]',
    credits: [['Produktion', 'The Wants Social'], ['Creative Director', 'Karla Jenders'], ['Models', 'Margot Davy, Jason Grotjahn'], ['Hair & Make-up', 'Melanie Bulu'], ['Styling', 'Johanna Löer'], ['Fotoassistenz', 'Eno de Witt'], ['Foto', 'Kilian Amrehn']] },
  { slug: 'peek-cloppenburg-x-ellesse', title: 'Peek & Cloppenburg x Ellesse', titleHtml: 'Peek &amp; Cloppenburg<br>x Ellesse', meta: 'Kampagne · 2022', metaEn: 'Campaign · 2022', color: '#2b3020', accent: '#c5cfa6',
    hero: 'peek-cloppenburg-ellesse-kampagne', heroAlt: 'Peek und Cloppenburg x Ellesse Kampagne', heroAltEn: 'Peek and Cloppenburg x Ellesse campaign', pics: [],
    intro: '[2 bis 3 Sätze zur Kampagne.]', introEn: '[2 to 3 sentences about the campaign.]',
    credits: [['Produktion', 'Feelming'], ['Regie', 'Mario Bürger'], ['1st AD', 'Nico Pékar'], ['DOP', 'Pasindu Goldmann'], ['Styling', 'Peninah Amanda'], ['Hair & Make-up', 'Kristin Belger'], ['Movement', 'Tim Schmitz'], ['Talents', 'Nora Nova, Rowdy Eyez, Mecnun'], ['Foto', 'Kilian Amrehn']] },
  { slug: 'rock-fairyland', title: 'Rock Fairyland', titleHtml: 'Rock<br>Fairyland', meta: "Editorial · New Icons' Club · 2023", metaEn: "Editorial · New Icons' Club · 2023", color: '#161616', accent: '#bdbdbd',
    hero: 'rock-fairyland-editorial', heroAlt: 'Rock Fairyland, zwei Gesichter in Tüll', heroAltEn: 'Rock Fairyland, two faces in tulle', pics: [{ src: 'the-wants-editorial-schwarzweiss', alt: 'Editorial in Schwarzweiß', altEn: 'Editorial in black and white' }],
    intro: '[2 bis 3 Sätze zum Editorial.]', introEn: '[2 to 3 sentences about the editorial.]',
    credits: [['Produktion', 'Kilian Amrehn'], ['Styling', 'Jacqueline Tamm'], ['Models', 'Marie Wehder, Louis Joerissen'], ['Hair & Make-up', 'Kathrin Hupertz'], ['Veröffentlicht', "First Magazine, New Icons' Club Magazine"]] },
];

// Rollen im Abspann auf Englisch. Nicht aufgeführte Rollen bleiben, wie sie sind.
export const roleEn: Record<string, string> = {
  Produktion: 'Production',
  Regie: 'Director',
  Fotoassistenz: 'Photo assistant',
  Foto: 'Photography',
  'Veröffentlicht': 'Published in',
};

export const weitere = [
  { name: 'Scholl', color: '#3a2f22' },
  { name: 'AppelrathCüpper', color: '#26303a' },
];
