// Bildbeschreibungen pro Bild (tools/alt/merge.py). Endung wird je nach Bereich angehängt.
import data from './alts.json';
const A = data as Record<string, [string, string]>;
export type AltKind = 'photo' | 'flash' | 'reportage';
const END = { photo: [', fotografiert von Kilian Amrehn', ', photographed by Kilian Amrehn'], flash: [', Flash von Kilian Amrehn', ', flash by Kilian Amrehn'], reportage: [', Reportage von Kilian Amrehn', ', reportage by Kilian Amrehn'] } as const;
export const altOf = (slug: string, en: boolean, fallback: string, kind: AltKind = 'photo') => {
  const a = A[slug];
  return a ? (en ? a[1] : a[0]) + END[kind][en ? 1 : 0] : fallback;
};
