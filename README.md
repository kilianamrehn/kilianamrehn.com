# kilianamrehn.com

Website von Kilian Amrehn. Astro, statisch, ausgeliefert über GitHub Pages.

## Inhalte ändern
- `src/data/site.ts`: E-Mail, Instagram, Name der Zeitungs-Rubrik, Kundenliste
- `src/data/artists.ts`: Artists, Reihenfolge, Bilder, Textzeilen
- `src/data/kampagnen.ts`: Kampagnen mit Abspann (Slugs = alte WordPress-Adressen)
- `src/data/flicker.ts`: Bilder für den Stopp-Knopf auf /ueber/
- Bilder: `src/assets/img/<sprechender-name>.jpg`. AVIF/WebP werden beim Build erzeugt.

## Seiten
`/` Start · `/kuenstlerportraits/` Artists · `/kampagnen/` + Kampagnenseiten · `/reportage/` Zeitung · `/ueber/` · `/portraitfotografie/` (SEO) · `/impressum/` · `/datenschutz/` · `/en/`

Alte Adressen werden in `astro.config.mjs` (`redirects`) auf die neuen Seiten umgeleitet.

## Umzug auf die eigene Domain
1. `public/CNAME` mit `kilianamrehn.com` anlegen
2. In `.github/workflows/deploy.yml` die Zeile `BASE_PATH` entfernen
3. DNS bei All-Inkl auf GitHub Pages umstellen (MX-Einträge für E-Mail nicht anfassen)

## Lokal
`npm install` · `npm run dev`
