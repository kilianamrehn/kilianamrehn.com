# Website kilianamrehn.com · Übergabe für den nächsten Chat (Stand 13.10.2026)

Lies zuerst diese Datei, dann Website_Handbuch.md (Textfassung des PDFs, aktuell). Website_Masterliste.md ist ein historisches Protokoll bis 11.10., viele dort als OFFEN markierte Punkte sind inzwischen erledigt. Was wirklich offen ist, steht unten.

## Status
- **Live seit 13.10.2026 auf https://kilianamrehn.com** (GitHub Pages, HTTPS erzwungen). Die alte github.io-Adresse leitet auf die Domain um. noindex ist aus.
- Repo `kilianamrehn/kilianamrehn.com` (Astro 5), lokal `/home/claude/kilianamrehn.com`. Push auf main = Deploy, ca. 12 Minuten. Baut auf Root, `public/CNAME` = kilianamrehn.com.
- DNS bei all-inkl (KAS → Tools → DNS-Einstellungen): A-Records 185.199.108/109/110/111.153, www CNAME kilianamrehn.github.io, MX bei mailbox.org (Mail unberührt). kilianamrehn.de und kilianphotography.com leiten auf https://kilianamrehn.com/ um (KAS → Domain). Alter WordPress-Ordner `/kilianamrehn.com/` bleibt ein paar Wochen als Sicherung.
- Handbuch-PDF (9 Seiten): Drive `_Fotografie/Homepage Kilian Amrehn/Website_Handbuch_kilianamrehn.pdf` und Repo `docs/`. Quelle `docs/handbuch.html`, gerendert mit Playwright (A4).

## Arbeitsweise mit Kilian
- Deutsch, kurz, keine Gedankenstriche nach außen, genderfrei (auch Englisch, britische Schreibweise).
- Bilder nie beschneiden. Ausnahmen: KIL03822-Startbild, Augenstreifen, Teilen-Bilder.
- Keine erklärenden Texte, nichts sagen, was nicht da ist, nichts Zeitgebundenes (Zeitung ausgenommen).
- Nichts über Fotos malen. Originale aus Drive `_Fotografie`.
- Ähnliche Farben nie nebeneinander, Schwarzweiß nie neben- oder übereinander.
- Interne Links gleicher Tab, externe Links und PDFs neuer Tab.
- Kilian ist rot/grün- und blau/lila-farbenschwach.
- Alles direkt online stellen. Intime Flashes bleiben ("edgy"). "Manchmal farbig", nicht nur düster.

## Was seit 12.10. dazukam (alles live)
- **SEO-Landingpages** (DE + EN, Komponente `src/views/Leistung.astro`, Texte `src/data/leistung.ts`): Portraitfotografie, Musik (ohne Namen), Schauspiel (Slavko zuerst), Moderationsfotografie (Bianca), Personal Branding, Porträts Kunst und Literatur (Nicole), Kampagnen (mit Dessous). Aufbau: Hero, Beispiele (unbeschnitten), So läuft ein Shooting (4 Schritte), Häufige Fragen aus Kilians Antworten (FAQ-Schema). Footer verlinkt alle sieben, DE und EN getrennt.
- **Englisch** komplett, Impressum und Datenschutz auch EN (en/legal-notice, en/privacy). Datenschutz neu geschrieben.
- **Teilen-Bilder** pro Seite in `public/media/og/` (Start KIL03822 mit Logo, Porträts Slavko, Flashes verstreute Polaroids, jede Arbeit eigenes Bild).
- **Alt-Texte**: 673 in `src/data/alts.json` über `altOf()` in `src/data/alts.ts`.
- **Mail-Schutz**: `src/components/Mail.astro`, Adresse verschlüsselt, erst im Browser zusammengesetzt.
- **Porträts**: Mischen-Knopf mittig, Kicker mit Moderation, Sprung zur Person, SEO-Zeile verlinkt. Nicole Da Silva mit drittem Bild (Nici und Nati, schwarzweiß), Augen davon. Nicole Malerin: neues Bild an der Staffelei.
- **Startseite**: Türen-Überschriften über den Streifen, Nicole-Augen neu.
- **Über**: Bio mit Moderation und Licht-Absatz, Verge-Text neu, "Halt es an" mit allen 358 Bildern außer Flashes.
- **Flashes**: größer (Handy 1,5x, Rechner 1,75x), Dichte am Rechner nachjustiert, f-080 bis f-103 sind Dänemark.
- **Arbeiten**: Art-Labels "Kampagne" statt "Kampagnen", Silent Escape Kampagne/Modefotografie mit KI-Video des Mannes, Phiala Dessousfotografie, Bundesliga "Sport · Bundesliga" mit neuem Text, Untamed ohne KI-Videos Hahn und Rabe, NI'C-Duplikat raus, Marie mit neuem Schwarzweißbild (DSC02915) und ohne Kopfüber-Augenbild.

## Abspann (14.10.)
- Jede Arbeit hat den Abspann in einer Kinoleinwand 21:9. Passt er nicht hinein, rollt er von unten nach oben (Schleife, nur sichtbar), man kann selbst scrollen, dann pausiert er kurz.
- Zusammengelegte Arbeiten (Scholl, Copenhagen, PNTS, NI'C): oben was für alle gilt, darunter ein Kapitel je Shooting mit dem Bogen-Titel. Nur belegte Credits (alte Seite, Instagram). Ohne Beleg kein Kapitel.
- Scholl und Copenhagen komplett aus Callsheets (14.10.). Neue Kapitel in `CH[...]` in tools/arbeiten_content.py, dann tisch.py.
- Styling Fuerteventura: Johanna Löer und Henni Schaefer (beide, Kilian). @modiandbloss = Serife Cigdem Güney.

## Technik-Notizen
- Arbeiten: erst `tools/arbeiten_content.py`, dann `tools/tisch.py`.
- Neue w-Bilder brauchen WebP (640, 1200, max) in public/img, Eintrag in imgmeta.json und imgcolor.json.
- Build `npx astro build`, Preview `npx astro preview --port 4329`. Playwright-Skripte in /tmp/pw. Der Container erreicht kilianamrehn.com nicht (Proxy).
- SEO-Werkstatt (Artifact): https://claude.ai/artifact/HJ2XWHk4WFc6TmARjkQf2q

## Offen
- Bilder auf den einzelnen Projektseiten durchgehen.
- Alle Arbeiten in einem Rutsch prüfen (Randschrift, Rahmen, Texte).
- Ozean der Stille: Models in den Credits.
- Kairo: vier Originale fehlen (DSC02485, DSC03132, DSC03185, DSC03302).
- Poetische Zeilen bei den Porträts.
- Preisliste-PDF enthält die Mail im Klartext, Kilian exportiert neu.
- SSL (Let's Encrypt) für kilianamrehn.de und kilianphotography.com (Kilian, all-inkl → SSL-Schutz).
- Google Search Console und Google-Unternehmensprofil einrichten.
- Optional: eigene Alias-Adresse für die Website.
- Alten WordPress-Ordner in ein paar Wochen löschen.
