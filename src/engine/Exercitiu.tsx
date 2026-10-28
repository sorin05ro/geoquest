import { useEffect, useMemo, useRef, useState } from 'react';
import type { Item } from '../types';
import { Pin } from './Pin';
import { Denumeste, Alegere } from './Alegere';
import { Etichete } from './Etichete';
import { Ordoneaza } from './Ordoneaza';
import { Asociaza } from './Asociaza';
import { Lacunar } from './Lacunar';
import { GraficEx } from './Grafic';

export interface PropsTip<T extends Item = Item> {
  item: T;
  verificat: boolean;
  /** scorul răspunsului curent (0..1) dacă răspunsul e complet, altfel null */
  onScor: (scor: number | null) => void;
}

export interface Rezultat { scor: number; corect: boolean; indiciu: boolean; durataMs: number }

const COMPONENTE: Record<Item['tip'], (p: PropsTip<never>) => JSX.Element> = {
  pin: Pin as never,
  denumeste: Denumeste as never,
  alegere: Alegere as never,
  etichete: Etichete as never,
  ordoneaza: Ordoneaza as never,
  asociaza: Asociaza as never,
  lacunar: Lacunar as never,
  grafic: GraficEx as never,
};

export function citesteCuVoce(text: string) {
  try {
    if (!('speechSynthesis' in window)) return;
    speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(text);
    u.lang = 'ro-RO';
    const voce = speechSynthesis.getVoices().find((v) => v.lang?.startsWith('ro'));
    if (voce) u.voice = voce;
    speechSynthesis.speak(u);
  } catch { /* fără voce pe acest dispozitiv */ }
}

interface Props {
  item: Item;
  /** false în Boss: feedback-ul apare abia la final */
  feedbackImediat?: boolean;
  onGata: (r: Rezultat) => void;
  textContinua?: string;
}

/** Afișează un item, verifică răspunsul și arată feedback explicativ. */
export function Exercitiu({ item, feedbackImediat = true, onGata, textContinua = 'Continuă' }: Props) {
  const [scor, setScor] = useState<number | null>(null);
  const [verificat, setVerificat] = useState(false);
  const [indiciu, setIndiciu] = useState(false);
  const start = useRef(performance.now());
  const C = useMemo(() => COMPONENTE[item.tip], [item.tip]);
  const titlu = useRef<HTMLParagraphElement>(null);

  useEffect(() => {
    setScor(null); setVerificat(false); setIndiciu(false); start.current = performance.now();
    titlu.current?.focus();
  }, [item.id]);

  const rezultat = (): Rezultat => ({
    scor: scor ?? 0, corect: (scor ?? 0) >= 0.999, indiciu, durataMs: Math.round(performance.now() - start.current),
  });

  const verifica = () => {
    if (scor === null) return;
    if (!feedbackImediat) { onGata(rezultat()); return; }
    setVerificat(true);
  };

  const corect = (scor ?? 0) >= 0.999;
  return (
    <div className="exercitiu">
      <div className="rand" style={{ alignItems: 'flex-start' }}>
        <p className="enunt" tabIndex={-1} ref={titlu} style={{ flex: 1, margin: 0 }}>{item.enunt}</p>
        <button className="buton-icon" onClick={() => citesteCuVoce(item.enunt)} aria-label="Citește enunțul cu voce">
          <svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path fill="currentColor" d="M3 9v6h4l5 5V4L7 9H3zm13.5 3A4.5 4.5 0 0 0 14 7.97v8.05A4.5 4.5 0 0 0 16.5 12z"/></svg>
        </button>
      </div>
      <C item={item as never} verificat={verificat} onScor={setScor} />
      {indiciu && item.indiciu && !verificat && <p className="feedback ok" role="note"><strong>Indiciu de la Geo</strong>{item.indiciu}</p>}
      {verificat && (
        <div className={`feedback ${corect ? 'ok' : 'nu'}`} role="status" aria-live="polite">
          <strong>{corect ? 'Corect!' : (scor ?? 0) > 0 ? 'Aproape.' : 'Nu chiar.'}</strong>
          {corect ? item.feedback.corect : item.feedback.gresit}
        </div>
      )}
      <div className="rand" style={{ justifyContent: 'flex-end' }}>
        {!verificat && item.indiciu && feedbackImediat && (
          <button className="buton secundar" onClick={() => setIndiciu(true)} disabled={indiciu}>Indiciu</button>
        )}
        {!verificat
          ? <button className="buton" onClick={verifica} disabled={scor === null}>{feedbackImediat ? 'Verifică' : 'Răspunde'}</button>
          : <button className="buton" onClick={() => onGata(rezultat())} autoFocus>{textContinua}</button>}
      </div>
    </div>
  );
}
