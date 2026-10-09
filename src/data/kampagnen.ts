export type Credit = [string, string];
export type Kampagne = { slug: string; title: string; titleHtml: string; meta: string; color: string; accent: string; hero: string; heroAlt: string; pics: { src: string; alt: string }[]; intro: string; credits: Credit[] };

// Slugs = alte Adressen von kilianamrehn.com, damit Google-Ranking erhalten bleibt
export const kampagnen: Kampagne[] = [
  { slug: 'copenhagen-studios', title: 'Copenhagen Studios', titleHtml: 'Copenhagen<br>Studios', meta: 'Kampagne · 2022', color: '#6a2a0c', accent: '#e8a27e',
    hero: 'copenhagen-studios-kampagne', heroAlt: 'Copenhagen Studios Kampagne, Model mit orangen Sandalen', pics: [],
    intro: '[2 bis 3 Sätze zur Kampagne.]',
    credits: [['Produktion', 'The Wants Social'], ['Creative Director', 'Karla Jenders'], ['Models', 'Margot Davy, Jason Grotjahn'], ['Hair & Make-up', 'Melanie Bulu'], ['Styling', 'Johanna Löer'], ['Fotoassistenz', 'Eno de Witt'], ['Foto', 'Kilian Amrehn']] },
  { slug: 'peek-cloppenburg-x-ellesse', title: 'Peek & Cloppenburg x Ellesse', titleHtml: 'Peek &amp; Cloppenburg<br>x Ellesse', meta: 'Kampagne · 2022', color: '#2b3020', accent: '#c5cfa6',
    hero: 'peek-cloppenburg-ellesse-kampagne', heroAlt: 'Peek und Cloppenburg x Ellesse Kampagne', pics: [],
    intro: '[2 bis 3 Sätze zur Kampagne.]',
    credits: [['Produktion', 'Feelming'], ['Regie', 'Mario Bürger'], ['1st AD', 'Nico Pékar'], ['DOP', 'Pasindu Goldmann'], ['Styling', 'Peninah Amanda'], ['Hair & Make-up', 'Kristin Belger'], ['Movement', 'Tim Schmitz'], ['Talents', 'Nora Nova, Rowdy Eyez, Mecnun'], ['Foto', 'Kilian Amrehn']] },
  { slug: 'rock-fairyland', title: 'Rock Fairyland', titleHtml: 'Rock<br>Fairyland', meta: "Editorial · New Icons' Club · 2023", color: '#161616', accent: '#bdbdbd',
    hero: 'rock-fairyland-editorial', heroAlt: 'Rock Fairyland, zwei Gesichter in Tüll', pics: [{ src: 'the-wants-editorial-schwarzweiss', alt: 'Editorial in Schwarzweiß' }],
    intro: '[2 bis 3 Sätze zum Editorial.]',
    credits: [['Produktion', 'Kilian Amrehn'], ['Styling', 'Jacqueline Tamm'], ['Models', 'Marie Wehder, Louis Joerissen'], ['Hair & Make-up', 'Kathrin Hupertz'], ['Veröffentlicht', "First Magazine, New Icons' Club Magazine"]] },
];

export const weitere = [
  { name: 'Scholl', color: '#3a2f22' },
  { name: 'AppelrathCüpper', color: '#26303a' },
];
