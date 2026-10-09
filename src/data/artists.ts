// Artists in Reihenfolge der Bekanntheit. Pro Person 1 bis 3 Bilder.
// layout: 'pairfull' (2 nebeneinander + 1 breit), 'pair23', 'pair32', 'pair11', 'trio', 'full'
// Englische Texte jeweils im Feld mit Endung En (metaEn, lineEn, altEn)
export type Pic = { src: string; alt: string; altEn: string; pos?: string };
export type Artist = { id: string; name: string; meta: string; metaEn: string; color: string; layout: string; pics: Pic[]; line?: string; lineEn?: string };

export const artists: Artist[] = [
  { id: 'morley', name: 'Morley', meta: 'Band · EP-Cover, Pressefotos · 2025', metaEn: 'Band · EP cover, press photos · 2025', color: '#c9973f', layout: 'pairfull',
    pics: [
      { src: 'morley-band-ep-cover-koeln', alt: 'Morley, EP-Cover der Band, fotografiert in Köln', altEn: 'Morley, the band’s EP cover, photographed in Cologne' },
      { src: 'morley-band-mehrfachbelichtung-schwarzweiss', alt: 'Morley, drei Musikerinnen in Mehrfachbelichtung, Schwarzweiß', altEn: 'Morley, three musicians in a multiple exposure, black and white' },
      { src: 'morley-band-pressefoto-von-oben', alt: 'Morley, Pressefoto von oben auf goldenem Stoff', altEn: 'Morley, press photo from above on golden fabric', pos: 'center 45%' },
    ],
    line: 'Drei Stimmen · <em>ein Licht von oben</em> · goldener Stoff · ein Cover, das man in der Hand halten will',
    lineEn: 'Three voices · <em>one light from above</em> · golden fabric · a cover you want to hold in your hands' },
  { id: 'bianca-berding', name: 'Bianca Berding', meta: 'Musik · Pressefotos · 2025', metaEn: 'Music · Press photos · 2025', color: '#a5a8ad', layout: 'pair23',
    pics: [
      { src: 'bianca-berding-musikerin-portraet-schwarzweiss', alt: 'Bianca Berding, Musikerin, Porträt auf dem Sofa in Schwarzweiß', altEn: 'Bianca Berding, musician, portrait on a sofa in black and white', pos: 'center 20%' },
      { src: 'bianca-berding-musikerin-pressefoto-studio', alt: 'Bianca Berding, Pressefoto im Studio, Schwarzweiß', altEn: 'Bianca Berding, press photo in the studio, black and white', pos: 'center 30%' },
    ],
    line: 'Schwarzweiß · <em>Ruhe statt Pose</em> · ein Lächeln, das niemand bestellt hat',
    lineEn: 'Black and white · <em>calm instead of a pose</em> · a smile nobody asked for' },
  { id: 'slavko-popadic', name: 'Slavko Popadic', meta: 'Schauspiel · 2022', metaEn: 'Acting · 2022', color: '#a88e86', layout: 'full',
    pics: [{ src: 'slavko-popadic-schauspielportraet', alt: 'Slavko Popadic, Schauspielporträt', altEn: 'Slavko Popadic, actor portrait', pos: 'center 35%' }],
    line: 'Schauspiel · <em>ein Blick, der eine Rolle offen lässt</em>',
    lineEn: 'Acting · <em>a look that leaves the role open</em>' },
  { id: 'pia-stutzenstein', name: 'Pia Stutzenstein', meta: 'Schauspiel · 2022', metaEn: 'Acting · 2022', color: '#d9822b', layout: 'trio',
    pics: [
      { src: 'pia-stutzenstein-schauspielportraet', alt: 'Pia Stutzenstein, Schauspielerin, im schwarzen Pullover', altEn: 'Pia Stutzenstein, actor, in a black sweater', pos: 'center 30%' },
      { src: 'pia-stutzenstein-schauspielerin-lampenlicht', alt: 'Pia Stutzenstein im Lampenlicht am Ledersofa', altEn: 'Pia Stutzenstein in lamplight by a leather sofa' },
      { src: 'pia-stutzenstein-portraet-koeln', alt: 'Pia Stutzenstein mit verschränkten Armen', altEn: 'Pia Stutzenstein with arms crossed', pos: 'center 30%' },
    ],
    line: 'Lampenlicht · drei Stimmungen · <em>eine Person</em>',
    lineEn: 'Lamplight · three moods · <em>one person</em>' },
  { id: 'lea-mende', name: 'Lea Mende', meta: 'Künstlerporträt · 2023', metaEn: 'Artist portrait · 2023', color: '#d9705e', layout: 'pair11',
    pics: [
      { src: 'lea-mende-kuenstlerportraet-koeln-rotlicht', alt: 'Lea Mende, Künstlerporträt im roten Raum unter einer Lampe', altEn: 'Lea Mende, artist portrait in a red room under a lamp', pos: 'center 38%' },
      { src: 'lea-mende-portraet-bewegung', alt: 'Lea Mende in Bewegungsunschärfe', altEn: 'Lea Mende in motion blur' },
    ],
    line: 'Ein roter Raum · eine Lampe · <em>wie lange man ins Licht sehen kann</em>',
    lineEn: 'A red room · one lamp · <em>how long you can look into the light</em>' },
  { id: 'david-vormweg', name: 'David Vormweg', meta: 'Schauspiel', metaEn: 'Acting', color: '#a88e86', layout: 'pair23',
    pics: [
      { src: 'david-vormweg-schauspielportraet', alt: 'David Vormweg, Schauspielporträt', altEn: 'David Vormweg, actor portrait', pos: 'center 30%' },
      { src: 'david-vormweg-portraet', alt: 'David Vormweg, Porträt', altEn: 'David Vormweg, portrait', pos: 'center 35%' },
    ] },
];

export const more: Artist[] = [
  { id: 'phiala', name: 'Phiala', meta: 'Musik · 2024', metaEn: 'Music · 2024', color: '#a88e86', layout: 'single', pics: [{ src: 'phiala-musikportraet', alt: 'Phiala, Musikporträt', altEn: 'Phiala, music portrait' }] },
  { id: 'trish', name: 'Trish', meta: 'Freie Serie · 2024', metaEn: 'Personal series · 2024', color: '#2f9e98', layout: 'single', pics: [{ src: 'trish-portraet-tuerkises-licht', alt: 'Trish im türkisen Licht', altEn: 'Trish in turquoise light', pos: '62% 50%' }] },
  { id: 'synergy', name: 'Synergy', meta: 'Editorial · 2024', metaEn: 'Editorial · 2024', color: '#a88e86', layout: 'single', pics: [{ src: 'synergy-editorial-rabe-schwarzweiss', alt: 'Synergy, Editorial mit Rabe, Schwarzweiß', altEn: 'Synergy, editorial with a raven, black and white', pos: 'center 35%' }] },
  { id: 'paula', name: 'Paula', meta: 'DJ · 2026', metaEn: 'DJ · 2026', color: '#2fb8b0', layout: 'single', pics: [{ src: 'paula-dj-musikportraet', alt: 'Paula, DJ, im türkisen Licht', altEn: 'Paula, DJ, in turquoise light', pos: 'center 30%' }] },
  { id: 'juliette', name: 'Juliette', meta: 'Porträt · 2022', metaEn: 'Portrait · 2022', color: '#a88e86', layout: 'single', pics: [{ src: 'juliette-portraet', alt: 'Juliette, Porträt mit hochgezogenem Pullover', altEn: 'Juliette, portrait with a pulled-up sweater', pos: 'center 40%' }] },
  { id: 'jeremiah', name: 'Jeremiah', meta: 'Editorial · Silent Escape · 2024', metaEn: 'Editorial · Silent Escape · 2024', color: '#a88e86', layout: 'single', pics: [{ src: 'jeremiah-portraet', alt: 'Editorial für Jeremiah, Porträt durch eine runde Öffnung', altEn: 'Editorial for Jeremiah, portrait through a round opening', pos: 'center 30%' }] },
];
