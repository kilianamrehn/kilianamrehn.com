// Artists in Reihenfolge der Bekanntheit. Pro Person 1 bis 3 Bilder.
// layout: 'pairfull' (2 nebeneinander + 1 breit), 'pair23', 'pair32', 'pair11', 'trio', 'full'
export type Pic = { src: string; alt: string; pos?: string };
export type Artist = { id: string; name: string; meta: string; color: string; layout: string; pics: Pic[]; line?: string };

export const artists: Artist[] = [
  { id: 'morley', name: 'Morley', meta: 'Band · EP-Cover, Pressefotos · 2025', color: '#c9973f', layout: 'pairfull',
    pics: [
      { src: 'morley-band-ep-cover-koeln', alt: 'Morley, EP-Cover der Band, fotografiert in Köln' },
      { src: 'morley-band-mehrfachbelichtung-schwarzweiss', alt: 'Morley, drei Musikerinnen in Mehrfachbelichtung, Schwarzweiß' },
      { src: 'morley-band-pressefoto-von-oben', alt: 'Morley, Pressefoto von oben auf goldenem Stoff', pos: 'center 45%' },
    ],
    line: 'Drei Stimmen · <em>ein Licht von oben</em> · goldener Stoff · ein Cover, das man in der Hand halten will' },
  { id: 'bianca-berding', name: 'Bianca Berding', meta: 'Musik · Pressefotos · 2025', color: '#a5a8ad', layout: 'pair23',
    pics: [
      { src: 'bianca-berding-musikerin-portraet-schwarzweiss', alt: 'Bianca Berding, Musikerin, Porträt auf dem Sofa in Schwarzweiß', pos: 'center 20%' },
      { src: 'bianca-berding-musikerin-pressefoto-studio', alt: 'Bianca Berding, Pressefoto im Studio, Schwarzweiß', pos: 'center 30%' },
    ],
    line: 'Schwarzweiß · <em>Ruhe statt Pose</em> · ein Lächeln, das niemand bestellt hat' },
  { id: 'slavko-popadic', name: 'Slavko Popadic', meta: 'Schauspiel · 2022', color: '#a88e86', layout: 'full',
    pics: [{ src: 'slavko-popadic-schauspielportraet', alt: 'Slavko Popadic, Schauspielporträt', pos: 'center 35%' }],
    line: 'Schauspiel · <em>ein Blick, der eine Rolle offen lässt</em>' },
  { id: 'pia-stutzenstein', name: 'Pia Stutzenstein', meta: 'Schauspiel · 2022', color: '#d9822b', layout: 'trio',
    pics: [
      { src: 'pia-stutzenstein-schauspielportraet', alt: 'Pia Stutzenstein, Schauspielerin, im schwarzen Pullover', pos: 'center 30%' },
      { src: 'pia-stutzenstein-schauspielerin-lampenlicht', alt: 'Pia Stutzenstein im Lampenlicht am Ledersofa' },
      { src: 'pia-stutzenstein-portraet-koeln', alt: 'Pia Stutzenstein mit verschränkten Armen', pos: 'center 30%' },
    ],
    line: 'Lampenlicht · drei Stimmungen · <em>eine Person</em>' },
  { id: 'lea-mende', name: 'Lea Mende', meta: 'Künstlerporträt · 2023', color: '#d9705e', layout: 'pair11',
    pics: [
      { src: 'lea-mende-kuenstlerportraet-koeln-rotlicht', alt: 'Lea Mende, Künstlerporträt im roten Raum unter einer Lampe', pos: 'center 38%' },
      { src: 'lea-mende-portraet-bewegung', alt: 'Lea Mende in Bewegungsunschärfe' },
    ],
    line: 'Ein roter Raum · eine Lampe · <em>wie lange man ins Licht sehen kann</em>' },
  { id: 'david-vormweg', name: 'David Vormweg', meta: 'Schauspiel', color: '#a88e86', layout: 'pair23',
    pics: [
      { src: 'david-vormweg-schauspielportraet', alt: 'David Vormweg, Schauspielporträt', pos: 'center 30%' },
      { src: 'david-vormweg-portraet', alt: 'David Vormweg, Porträt', pos: 'center 35%' },
    ] },
];

export const more: Artist[] = [
  { id: 'phiala', name: 'Phiala', meta: 'Musik · 2024', color: '#a88e86', layout: 'single', pics: [{ src: 'phiala-musikportraet', alt: 'Phiala, Musikporträt' }] },
  { id: 'trish', name: 'Trish', meta: 'Freie Serie · 2024', color: '#2f9e98', layout: 'single', pics: [{ src: 'trish-portraet-tuerkises-licht', alt: 'Trish im türkisen Licht', pos: '62% 50%' }] },
  { id: 'synergy', name: 'Synergy', meta: 'Editorial · 2024', color: '#a88e86', layout: 'single', pics: [{ src: 'synergy-editorial-rabe-schwarzweiss', alt: 'Synergy, Editorial mit Rabe, Schwarzweiß', pos: 'center 35%' }] },
];
