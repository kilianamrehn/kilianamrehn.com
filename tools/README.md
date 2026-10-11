# Werkzeuge (nicht Teil des Builds)

- `tisch.py`: rechnet die Bögen für Arbeiten (src/data/tisch/*.json, src/data/arbeiten.json). Inhalte in `arbeiten_content.py` (Titel, Credits, Texte, Reihenfolge, Abschnitte).
- `portraits/`: Generator der Porträts-Seite (gen29.py + gen_site.py), Pinselspuren (marks2.py), Handschrift als Pinsel (brushhand.py). Brauchen die Arbeitsdaten aus dem alten Chat (Canvas-Items), hier nur zur Referenz.
- `jobs.json`: Quelle (Pfad im Drive `_Fotografie/`) → Web-Name für alle Bilder der Arbeiten (w-*), Flashes (f-*), Was bleibt (r-*).
- `arbeiten_groups.json`, `reportage.json`, `flashes.json`: Zuordnung Web-Name → Projekt/Kapitel/Original.
- `auswahl_master.json`, `flashes_final.json`: Kilians Bildauswahl mit A-/W-/F-Nummern.
- Bilder liegen als WebP in `public/img/<name>-<breite>.webp`, Maße in `src/data/imgmeta.json`, Farbe in `src/data/imgcolor.json`. Videos in `public/media/video/`, Maße in `src/data/vidmeta.json`.
- Web-Exporte (2000 px JPG) liegen auch im Drive: `Homepage Kilian Amrehn/Web Arbeiten`, `Web Flashes`, `Web Reportage`, `Web Portraets`, `Web Hero`, `Web Videos`.
