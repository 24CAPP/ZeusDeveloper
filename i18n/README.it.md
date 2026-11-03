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
  <img src="../assets/chart-overview.svg" width="880" alt="Panoramica Benchmark ZeusDeveloper">
</p>

<p align="center">
  <img src="../assets/chart-tests.svg" width="880" alt="Affidabilità e Test ZeusDeveloper">
</p>

<p align="center">
  <img src="../assets/chart-tiers.svg" width="880" alt="Risparmio Token per Livello Operativo">
</p>

---

## Caso di Studio: Prima e Dopo

<p align="center">
  <img src="../assets/chart-before-after.svg" width="880" alt="Caso di studio Prima e Dopo">
</p>

Gli assistenti di programmazione AI tendono a produrre troppo codice superfluo:
- Chiedi un rate limiter e installano middleware esterni con molteplici file di configurazione.
- Chiedi una correzione e introducono classi wrapper e interfacce non richieste.
- Consumano token in convenevoli, scuse e riepiloghi prolissi prima di mostrare il codice.

ZeusDeveloper mantiene le modifiche minime garantendo confini modulari puliti, uso delle librerie native e controlli rigorosi sull'input.

---

## Linee Guida Fondamentali

1. **Modifica minima e robusta**: Risolvi il problema con il minor numero di modifiche. Evita parametri ipotetici, opzioni di configurazione non richieste o astrazioni premature.
2. **Librerie native prima di tutto**: Sfrutta le funzionalità integrate nel runtime e le utilità già presenti nel progetto prima di aggiungere dipendenze.
3. **Difesa dei confini di fiducia**: Non omettere mai la sanitizzazione degli input, la propagazione degli errori o i controlli di autenticazione. Tratta ogni dato esterno come non affidabile.
4. **Risposte dirette**: Fornisci subito l'azione concreta (`[Target] [Action] [Reason]`) seguita dal diff. Elimina cerimonie conversazionali e convenevoli.
5. **Separazione pulita**: Evita file o funzioni giganti. Mantieni le regole di dominio separate dalla logica di rete e di I/O.
6. **Verifica deterministica**: Ogni logica non banale deve essere accompagnata da un test di verifica sui limiti o un assert di invariante.

---

## Livelli Operativi

Puoi regolare l'intensità della modalità in base all'attività:

| Livello | Comando | Utilizzo |
| :--- | :--- | :--- |
| **Hermes** | `/zeus hermes` | Bugfix rapidi e diretti con il minimo attrito. Segnala eventuali debiti tecnici in una riga. |
| **Zeus** | `/zeus` | Modalità predefinita. Impone diff minimi, API native e verifiche di sicurezza. |
| **Titan** | `/zeus titan` | Mette in discussione requisiti sovradimensionati o assunzioni errate prima di scrivere codice. |
| **Oracle** | `/zeus oracle` | Massima densità tecnica. Elimina ogni testo superfluo per il massimo risparmio di token (-78%). |

---

## Suite di Skill Incluse

* **`/zeus`**: Modalità principale e commutazione dei livelli operativi.
* **`/zeus-shield`**: Revisione di sicurezza su 7 classi di attacco (Injection, IDOR, TOCTOU, Crypto, vettori AI, limiti di risorse, supply chain).
* **`/zeus-strike`**: Refactoring chirurgico per rimuovere dead code, wrapper inutili e pacchetti ridondanti.
* **`/zeus-audit`**: Audit del repository per individuare race condition, colli di bottiglia e complessità accidentale.
* **`/zeus-verify`**: Generazione di test unitari deterministici sugli edge case per logiche critiche.
* **`/zeus-debt`**: Scansione del codice per tag `// zeus-debt:` e `TODO:` per generare un registro dei debiti tecnici.
* **`/zeus-help`**: Guida rapida ai comandi.

---

## Dashboard Locale di Monitoraggio

ZeusDeveloper include una dashboard autonoma per visualizzare sessioni, risparmi di token e test:

```bash
python board.py
```

Avvia un'interfaccia scura su `http://localhost:3000` con il riepilogo dettagliato delle sessioni e delle metriche.

---

## Installazione

### Configurazione Universale per qualsiasi AI
Scarica [`AGENTS.md`](../AGENTS.md) nella root del tuo progetto:
```bash
curl -o AGENTS.md https://raw.githubusercontent.com/24Capp/ZeusDeveloper/main/AGENTS.md
```
Antigravity, Cursor, Windsurf, OpenCode, Devin, Aider e Claude Code rilevano automaticamente le regole di progetto.

### Antigravity & Gemini CLI
```bash
agy plugin install https://github.com/24Capp/ZeusDeveloper
```

### Claude Code
```text
/plugin marketplace add 24Capp/ZeusDeveloper
/plugin install zeus@zeus
```

Consulta [INSTALL.md](../INSTALL.md) per Cursor, Windsurf, Copilot, OpenCode e Hermes.

---

## Licenza
MIT © 2026 Luca Quagliozzi (24Capp)
