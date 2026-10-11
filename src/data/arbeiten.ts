// Arbeiten-Daten (aus tools/arbeiten_content.py + tools/tisch.py)
import list from './arbeiten.json';
const sheets = import.meta.glob<{ default: any }>('./tisch/a-*.json', { eager: true });
export const arbeiten = list as any[];
export const sheetsFor = (slug: string) => sheets[`./tisch/a-${slug}.json`].default;
export const arbeitPaths = () => arbeiten.map((p, i) => ({ params: { kampagne: p.slug }, props: { p, prev: arbeiten[(i - 1 + arbeiten.length) % arbeiten.length], next: arbeiten[(i + 1) % arbeiten.length], data: sheetsFor(p.slug) } }));
