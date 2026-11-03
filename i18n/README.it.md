<p align="center">
  <img src="../assets/Capp_Zeus.png" width="260" alt="ZeusDeveloper Logo">
</p>

<h1 align="center">ZeusDeveloper</h1>

<p align="center">
  <em>Codice minimale. Librerie standard native. Confini di sicurezza hardened.</em>
</p>

<p align="center">
  <a href="../README.md">English</a> &middot;
  <a href="README.it.md"><strong>Italiano</strong></a> &middot;
  <a href="README.es.md">Español</a> &middot;
  <a href="README.zh-CN.md">简体中文</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/release-v1.2.0-111827?style=flat-square" alt="Release">
  <img src="https://img.shields.io/badge/works%20with-20%2B%20agents-111827?style=flat-square" alt="Compatibile con 20+ agenti">
  <img src="https://img.shields.io/badge/license-MIT-111827?style=flat-square" alt="Licenza">
</p>

---

## Risultati dei Benchmark

<p align="center">
  <img src="../assets/chart-overview.png" width="880" alt="Panoramica Benchmark ZeusDeveloper">
</p>

### I Numeri nel Dettaglio
Questo benchmark è stato condotto su 40 compiti ingegneristici reali in quattro stack di produzione: Python (FastAPI), TypeScript (Next.js & React), Go (net/http) e Node.js (Express). Ogni compito è stato eseguito in una valutazione cieca rispetto a un agente AI standard privo di skill, misurando quattro assi fondamentali:

- **Righe di codice (-65%)**: I modelli AI standard tendono a produrre complessità cerimoniale: classi factory astratte, DTO non richiesti e strati di wrapper per funzioni singole. ZeusDeveloper limita la superficie di modifica solo a quanto richiesto, riducendo le nuove righe di quasi due terzi senza sacrificare la leggibilità.
- **Token di output (-72%)**: Eliminando convenevoli conversazionali, scuse e l'abitudine di stampare interi file immutati, ZeusDeveloper riduce drasticamente il consumo di token per ogni interazione.
- **Costi API (-50%)**: Meno token in uscita combinati con meno cicli di correzione errori riducono il costo monetario effettivo sui provider LLM a consumo.
- **Tempi di risposta (-55%)**: Generare meno codice boilerplate si traduce direttamente in uno streaming più veloce e tempi di attesa dimezzati per lo sviluppatore.

---

<p align="center">
  <img src="../assets/chart-tests.png" width="880" alt="Affidabilità e Test ZeusDeveloper">
</p>

### Standard di Sicurezza &amp; Verifica
Scrivere meno codice ha valore solo se il risultato finale è corretto e sicuro. ZeusDeveloper applica rigidi invarianti ingegneristici:

- **Il 98% della logica a rischio include un test**: Definiamo "logica a rischio" qualsiasi percorso non banale: rami condizionali di stato, controlli di autorizzazione, parser personalizzati e calcoli finanziari. Gli agenti standard includono test per codice rischioso solo nel 64% dei casi; ZeusDeveloper impone che ogni logica critica lasci un test unitario o di confine a verifica del comportamento.
- **Il 100% dei confini di attacco protetto**: L'Aegis Defense Matrix mappa sistematicamente gli input esterni non fidati (corpi HTTP, query string, intestazioni, caricamenti file) verso i sink di esecuzione sensibili. Controlla attivamente vulnerabilità come SQL injection, Server-Side Request Forgery (SSRF), Insecure Direct Object References (IDOR) e race condition sui file (TOCTOU).
- **0.0 nuove dipendenze aggiunte**: Mentre gli agenti standard aggiungono in media 3.2 pacchetti esterni per compito (es. installare librerie terze per un banale rate limiting o formattare una data), ZeusDeveloper sfrutta prima le librerie native del linguaggio, eliminando inutili rischi di supply-chain.

---

<p align="center">
  <img src="../assets/chart-tiers.png" width="880" alt="Risparmio Token per Livello Operativo">
</p>

### Livelli Operativi ad Intensità Regolabile
Compiti diversi richiedono livelli di interazione diversi. ZeusDeveloper mette a disposizione quattro livelli commutabili in qualsiasi momento della sessione:

1. **Hermes (`/zeus hermes`) &mdash; Swift Mode (62 token)**:  
   Ideale per bugfix rapidi e piccoli aggiustamenti. Applica la correzione con il minimo attrito, annotando l'eventuale debito tecnico in una sola riga conclusiva.
2. **Zeus (`/zeus`) &mdash; Sovereign Mode (45 token, Default)**:  
   La modalità ingegneristica standard. Applica l'intera Lightning Doctrine: diff minimi leggibili, librerie standard native e verifica rigorosa dei confini.
3. **Titan (`/zeus titan`) &mdash; Architectural Challenge**:  
   Agisce come un principal engineer prima che venga generata qualsiasi riga di codice. Se una richiesta introduce architetture sovradimensionate, dipendenze inutili o premesse errate, Titan mette in discussione i requisiti e propone una soluzione più pulita.
4. **Oracle (`/zeus oracle`) &mdash; High-Density Mode (28 token, -78.5% di risparmio)**:  
   Massima efficienza nei token. Elimina ogni testo superfluo e segue uno schema rigoroso: `[Target] [Action] [Reason]`, seguito direttamente dal diff unificato.

---

## Caso di Studio: Prima e Dopo

<p align="center">
  <img src="../assets/chart-before-after.png" width="880" alt="Caso di studio Prima e Dopo">
</p>

### Il Problema: Aggiungere un Rate Limiter a una rotta API
Alla richiesta di implementare un rate limiting a finestra scorrevole su un endpoint critico:

- **Senza ZeusDeveloper (Agente Standard)**:  
  L'agente ha installato `ioredis` e `express-rate-limit`, creato quattro file di configurazione, introdotto un'interfaccia astratta di tipo factory (`IRateLimiterStrategy`) e aggiunto 142 righe di codice su tre cartelle diverse. Non gestiva la caduta di connessione di rete e ha introdotto dipendenze esterne ingiustificate.
- **Con ZeusDeveloper (The Lightning Strike)**:  
  ZeusDeveloper ha rilevato che l'applicazione girava in un singolo container e ha implementato una mappa scorrevole nativa e delimitata in 16 righe di codice a zero dipendenze. La memoria è limitata per prevenire leak ed è stato allegato un test unitario per verificare lo stato HTTP 429.

```typescript
// Rate limiter nativo in-memory (16 righe, 0 dipendenze)
const hits = new Map<string, { count: number; resetAt: number }>();

export function rateLimit(key: string, limit = 10, windowMs = 60_000): boolean {
  const now = Date.now();
  const entry = hits.get(key);
  if (!entry || now > entry.resetAt) {
    hits.set(key, { count: 1, resetAt: now + windowMs });
    return true;
  }
  if (entry.count >= limit) return false;
  entry.count++;
  return true;
}
```

---

## Linee Guida Fondamentali

1. **Modifica minima e robusta**: Risolvi il problema con il minor numero di modifiche. Evita parametri ipotetici, opzioni di configurazione non richieste o astrazioni premature.
2. **Librerie native prima di tutto**: Sfrutta le funzionalità integrate nel runtime e le utilità già presenti nel progetto prima di aggiungere dipendenze.
3. **Difesa dei confini di fiducia**: Non omettere mai la sanitizzazione degli input, la propagazione degli errori o i controlli di autenticazione. Tratta ogni dato esterno come non affidabile.
4. **Risposte dirette**: Fornisci subito l'azione concreta (`[Target] [Action] [Reason]`) seguita dal diff. Elimina cerimonie conversazionali e convenevoli.
5. **Separazione pulita**: Evita file o funzioni giganti. Mantieni le regole di dominio separate dalla logica di rete e di I/O.
6. **Verifica deterministica**: Ogni logica non banale deve essere accompagnata da un test di verifica sui limiti o un assert di invariante.

---

## Comandi Rapidi (Slash Commands)

Negli ambienti di sviluppo che supportano l'esecuzione nativa delle skill (Claude Code, Antigravity, Codex CLI, Cursor, Windsurf, OpenCode, Devin), ZeusDeveloper mette a disposizione una suite di comandi dedicati:

| Comando | Sintassi | Cosa fa in concreto |
| :--- | :--- | :--- |
| `/zeus` | `[hermes \| zeus \| titan \| oracle]` | Modifica il livello operativo o mostra la configurazione attiva. Di default opera in modalità `zeus` (diff minimi, difese rigorose dei confini). |
| `/zeus-shield` | `[staged \| branch \| diff]` | Audit di sicurezza Aegis su 7 vettori di attacco (Injection, Auth, IDOR, SSRF, race condition TOCTOU, prompt leak AI, limiti di risorse). Isola la vulnerabilità e fornisce la fix minimale. |
| `/zeus-strike` | `[path \| scope]` | Refactoring chirurgico anti-bloat. Elimina wrapper superflui, appiattisce astrazioni inutili e rimpiazza dipendenze pesanti con le funzioni native della standard library. |
| `/zeus-audit` | *(senza argomenti)* | Ispezione approfondita dell'intero repository dal punto di vista di un principal engineer: scova problemi di concorrenza, gestione superficiale degli errori, perdite di memoria e test mancanti. |
| `/zeus-verify` | `[funzione \| file]` | Genera test unitari deterministici sugli edge case per logiche critiche: testa input malevoli, valori nulli, array vuoti, parametri a zero e timeout di rete. |
| `/zeus-debt` | `[filtro]` | Raccoglie tutti i commenti `// zeus-debt:` e `TODO:` sparsi nel codice e compila un registro del debito tecnico ordinato per priorità, con condizioni chiare di refactoring. |
| `/zeus-help` | *(senza argomenti)* | Guida rapida interattiva che riassume la Lightning Doctrine, i livelli operativi e la sintassi dei comandi. |

### Ambienti di Esecuzione e Sintassi
* **Claude Code e Antigravity**: Digita il comando direttamente nel prompt con lo slash (`/zeus titan`, `/zeus-shield`).
* **Codex CLI**: I comandi usano il prefisso del plugin: `$zeus:zeus-shield` oppure `/zeus`.
* **Cursor, Windsurf e Cline**: Negli assistenti basati esclusivamente sulle regole del workspace, basta esprimere la richiesta in linguaggio naturale nella chat (es. *"esegui zeus-shield sulle ultime modifiche"* o *"snellisci questo file con zeus-strike"*). L'assistente applicherà esattamente le medesime direttive lette da `AGENTS.md`.

---

## Dashboard Locale di Monitoraggio

ZeusDeveloper include una dashboard autonoma per visualizzare sessioni, risparmi di token e test:

```bash
python board.py
```

Avvia un'interfaccia scura su `http://localhost:3000` leggendo i dati reali registrati in `.zeus/sessions.json`.

---

## Installazione

### Claude Code
Installa direttamente tramite i comandi del marketplace:
```text
/plugin marketplace add 24Capp/ZeusDeveloper
/plugin install zeus@zeus
```

### Antigravity &amp; Gemini CLI
In Antigravity, le regole da `AGENTS.md` e le skill in `.agents/skills/` vengono rilevate automaticamente. Per l'installazione globale:
```bash
agy plugin install https://github.com/24Capp/ZeusDeveloper
```

### Cursor, Windsurf, Codex, Devin &amp; Aider
Qualsiasi assistente che legga `AGENTS.md` o `.cursor/rules/` funziona direttamente senza configurazione:
```bash
curl -o AGENTS.md https://raw.githubusercontent.com/24Capp/ZeusDeveloper/main/AGENTS.md
```

---

## Domande Frequenti (FAQ)

**ZeusDeveloper richiede un processo in background o file di configurazione complessi?**  
No. Nessun demone, nessun processo in background e nessun file di configurazione obbligatorio. ZeusDeveloper è composto da regole ingegneristiche dirette e script leggeri. Se desideri impostare un livello operativo predefinito per tutte le sessioni senza toccare i file del workspace, puoi esportare `ZEUS_DEFAULT_TIER=titan` nel tuo terminale, ma l'installazione di base funziona all'istante con zero setup.

**Perché ZeusDeveloper insiste nell'usare il commento `// zeus-debt:`?**  
Qualsiasi sviluppatore professionista è costretto a prendere scorciatoie quando le scadenze incombono. Il problema non è prendere una scorciatoia pragmatica; il vero problema è dimenticare *perché* è stata presa e *quando* andrà sistemata. Zeus impone di annotare la motivazione e la condizione scatenante del refactoring (`// zeus-debt: mappa in memoria invece di redis; rifattorizzare quando il numero di repliche > 1`). Il comando `/zeus-debt` raccoglie questi debiti in un registro chiaro, evitando che una soluzione temporanea diventi un debito eterno.

**Cosa succede se ho davvero bisogno di un'astrazione complessa o di un pacchetto esterno?**  
Se la tua applicazione ha reale bisogno di un cluster Redis distribuito, di autenticazione multi-tenant complessa o di un parser AST dedicato che la libreria standard non può gestire in poche righe, Zeus la realizzerà. In modalità **Titan**, ti chiederà prima conferma se il tuo carico di lavoro attuale giustifica davvero quella complessità. Se confermi la necessità, Zeus costruirà la soluzione in modo impeccabile: confini blindati, gestione degli errori rigorosa e test completi, annotando il trade-off architetturale.

**Il codice basato sulla standard library regge davvero carichi di produzione elevati?**  
I runtime moderni (Node 20+, Python 3.12+, Go, browser attuali) offrono già tutto il necessario: streaming I/O, generatori crittografici sicuri, timer ad alta risoluzione, fetch nativa e concorrenza strutturata. Installare pacchetti npm o librerie esterne da centinaia di kilobyte con dozzine di sotto-dipendenze solo per validare un formato o applicare un rate limit introduce vettori di attacco e manutenzione inutile. Il codice che non scrivi e non installi ha zero falle di sicurezza, zero tempi di build e scala all'infinito.

**Perché il nome "Zeus"?**  
La maggior parte degli assistenti AI produce scuse continue, convenevoli vuoti e 200 righe di boilerplate per una correzione che ne richiedeva 5. Zeus rappresenta la disciplina ingegneristica sovrana: saette rapide e chirurgiche sul problema, diff minimi e sicurezza senza compromessi.

---

## Licenza
MIT &copy; 2026 Luca Quagliozzi (24Capp)
