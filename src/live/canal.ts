// Canalul de comunicare dintre tablă și telefoane.
// Cu Supabase configurat (public/config/live.json): canal Realtime „broadcast”, servere în UE, fără bază de date.
// Fără configurare: BroadcastChannel – merge doar între ferestre ale aceluiași browser (demonstrație, teste).

import { incarca } from '../content';
import type { Mesaj } from './protocol';

export interface Canal {
  tip: 'supabase' | 'local';
  trimite: (m: Mesaj) => void;
  asculta: (f: (m: Mesaj) => void) => () => void;
  inchide: () => void;
}

interface ConfigLive { supabaseUrl: string; supabaseAnonKey: string }

export async function configLive(): Promise<ConfigLive | null> {
  try {
    const c = await incarca<ConfigLive>('config/live.json');
    return c.supabaseUrl && c.supabaseAnonKey ? c : null;
  } catch { return null; }
}

export async function deschideCanal(pin: string): Promise<Canal> {
  const cfg = await configLive();
  const ascultatori = new Set<(m: Mesaj) => void>();
  const emite = (m: Mesaj) => ascultatori.forEach((f) => f(m));

  if (cfg) {
    const { createClient } = await import('@supabase/supabase-js');
    const client = createClient(cfg.supabaseUrl, cfg.supabaseAnonKey, {
      auth: { persistSession: false, autoRefreshToken: false },
      realtime: { params: { eventsPerSecond: 20 } },
    });
    const ch = client.channel(`geoquest-${pin}`, { config: { broadcast: { self: false, ack: false } } });
    ch.on('broadcast', { event: 'm' }, ({ payload }) => emite(payload as Mesaj));
    await new Promise<void>((ok, nu) => {
      const t = setTimeout(() => nu(new Error('Nu m-am putut conecta la serverul jocului. Verifică internetul.')), 10000);
      ch.subscribe((status) => {
        if (status === 'SUBSCRIBED') { clearTimeout(t); ok(); }
        if (status === 'CHANNEL_ERROR' || status === 'TIMED_OUT') { clearTimeout(t); nu(new Error('Conexiunea la serverul jocului a eșuat.')); }
      });
    });
    return {
      tip: 'supabase',
      trimite: (m) => { ch.send({ type: 'broadcast', event: 'm', payload: m }); },
      asculta: (f) => { ascultatori.add(f); return () => ascultatori.delete(f); },
      inchide: () => { client.removeChannel(ch); },
    };
  }

  const bc = new BroadcastChannel(`geoquest-${pin}`);
  bc.onmessage = (e) => emite(e.data as Mesaj);
  return {
    tip: 'local',
    trimite: (m) => bc.postMessage(m),
    asculta: (f) => { ascultatori.add(f); return () => ascultatori.delete(f); },
    inchide: () => bc.close(),
  };
}
