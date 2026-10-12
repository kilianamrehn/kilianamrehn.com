// Gemeinsame Bausteine der SEO-Seiten: Ablauf und häufige Fragen (Antworten nach Kilians Angaben).
// Antworten dürfen einfache Links enthalten (<a href="__B__...">), __B__ wird durch die Basis-URL ersetzt.
export type QA = [string, string];
export type Step = [string, string];

export const STEPS: Step[] = [
  ['Idee', 'Du erzählst mir, wofür du die Bilder brauchst. Hast du schon eine Vorstellung, sammelst du sie am besten in einem Pinterest-Moodboard. Wenn nicht, entwickeln wir die Idee zusammen von Anfang an.'],
  ['Planung', 'Wir legen Ort, Licht, Kleidung und Accessoires fest. Studio, draußen oder bei dir. Hair & Make-up und Styling hole ich auf Wunsch dazu.'],
  ['Shooting', 'Ein typisches Porträt-Shooting dauert drei Stunden. Wir nehmen uns die Zeit, bis die Bilder nach dir aussehen.'],
  ['Auswahl', 'Du bekommst alle Bilder unbearbeitet zur Auswahl. Deine Favoriten bearbeite ich fertig.'],
];

export const FAQ_PRICE: QA = ['Was kostet ein Shooting?', 'Beim fokussierten Shooting fotografieren wir drei Stunden, zehn bearbeitete Bilder sind dabei. Beim Intensiv-Shooting sind es fünf Stunden und 15 Bilder. Weitere Bilder kannst du dazubuchen. Alle Preise stehen in der <a href="__B__media/kilian-amrehn-buch-preise-portraet.pdf" target="_blank" rel="noopener">Preisliste</a>.'];
export const FAQ_TIME: QA = ['Wie lange dauert ein Shooting?', 'Ab zwei Stunden für zwei oder drei verschiedene Bilder. Ein typisches Porträt-Shooting dauert drei Stunden. Je nach Ort, Licht und Aufwand kann es auch ein ganzer Tag werden.'];
export const FAQ_SPEED: QA = ['Wann bekomme ich die Bilder?', 'Das hängt davon ab, wie viel gerade los ist. Gibt es eine Deadline, halte ich sie ein.'];
export const FAQ_USE: QA = ['Wofür darf ich die Bilder nutzen?', 'Presse, Social Media und Website sind immer dabei, ohne Aufpreis. Sollen die Bilder verkauft werden oder auf großen Werbeflächen laufen, sprechen wir über die Rechte.'];
export const FAQ_STUDIO: QA = ['Wo fotografierst du?', 'Im Studio, draußen oder bei dir. Ein eigenes Studio habe ich nicht, dafür kenne ich viele in Köln und suche das passende aus. Für Orte bei dir helfen mir vorab Fotos oder ein kurzes Video. Und ich reise, wohin das Shooting gehört.'];
export const FAQ_HMU: QA = ['Gibt es Hair & Make-up und Styling?', 'Wenn du möchtest. Ich arbeite mit Hair & Make-up Artists und Stylist:innen, die ich dazuholen kann. Du kannst dich aber auch selbst fertig machen.'];
export const FAQ_WEAR: QA = ['Was ziehe ich an?', 'Das besprechen wir vorher, zusammen mit Ort und Licht. Referenzbilder aus deinem Moodboard helfen dabei am meisten.'];
export const FAQ_UNFOTOGEN: QA = ['Ich bin total unfotogen. Geht das trotzdem?', 'Die Medien zeigen uns ein ziemlich langweiliges Bild davon, was schön ist. Wer dem nicht entspricht, muss sich deshalb nicht schlecht fühlen. Jeder Mensch hat eine Menge Schönheit an sich. Genau die suchen wir.'];

export const FAQ_BASE: QA[] = [FAQ_PRICE, FAQ_TIME, FAQ_SPEED, FAQ_USE, FAQ_STUDIO, FAQ_HMU, FAQ_WEAR, FAQ_UNFOTOGEN];
