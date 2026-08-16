# X Content Playbook

Referenzprofil: [@tornikegomareli](https://x.com/tornikegomareli). Stand der Analyse: 16.08.2026.
Eigenes Profil: [@marcmantei](https://x.com/marcmantei) (vorher @evermeld).

## 1. Was am Referenzprofil messbar funktioniert

Erhoben über die X-Suche (`from:tornikegomareli`, sortiert nach Likes) am 16.08.2026:

| Likes | Post | Muster |
|---|---|---|
| 16.414 | "Ilia Topuria has gained 1M+ followers since he lost to Justin Gaethje" | Persönliches Nicht-Tech-Interesse (MMA, Georgien) |
| 13.995 | "For anyone who used a computer between 1990 & 2005… what's the one game you still think about?" | Offene Frage an die Timeline |
| 1.796 | "I built Talkify, an 8.2 MB macOS dictation app with 123 ms median release-to-text latency. Fastest of five apps tested, ahead of superwhisper, voiceink, wispr flow, macwhisper." | Fertiges Produkt + harte Zahl + Vergleich gegen Bekanntes |
| 462 | "reverse engineered SiriUICore and implemented custom shaders" | Technisches Kunststück, das man sehen kann |
| 442 | "Ported Cheng Lou's Pretext to Swift. 2x less CPU, 2x less battery on redraws." | Portierung + Messwert |

Vier Muster, die das tragen:

1. **Zahl im ersten Satz.** Nicht "schnell", sondern "123 ms median, P95 140 ms". Jede Behauptung hat eine Einheit.
2. **Vergleich gegen Bekanntes.** Der Talkify-Post nennt vier Konkurrenzprodukte namentlich. Das gibt Fremden einen Maßstab, den sie schon kennen.
3. **Fertige Sache statt Fortschrittsbericht.** Es wird ein benutzbares Ding gezeigt, keine Nachtschicht.
4. **Antwortdisziplin.** Die letzten 13 Posts im Live-Feed sind fast alle *Antworten* auf Nutzerfeedback ("Just released 0.4.2, please update"). Zwischen Launch und Folgetag: drei Releases, jeweils öffentlich beantwortet. Der Launch ist der Anfang der Konversation, nicht das Ende.

Dazu kommt: Der Account ist nicht rein technisch. MMA und Nostalgie-Fragen bringen dort das mit Abstand größte Engagement und machen ihn als Person greifbar.

## 2. Wo Marcs bisheriger Content abweicht

Erhoben über `from:evermeld`, letzte Posts vor der Umstellung. Alle mit **0 Likes**:

| Post | Problem |
|---|---|
| "7 commits between 11pm and 5:40am … The indie dev night shift hits different. #buildinpublic" | Prozess statt Ergebnis. Für Fremde ist der Nutzen null. |
| "Caught a race condition in ChargePilot's notification system tonight … Nobody would've noticed." | Selbst entwertet ("nobody would've noticed"). |
| "Menu bar apps have an onboarding problem … Small thing." | Verkleinert die eigene Arbeit im letzten Satz. |
| "ChargePilot is entering beta. Want in? #buildinpublic #indiedev" | Ankündigung einer Ankündigung, ohne zeigbares Ergebnis. |

Die drei konkreten Unterschiede:

- **Keine Zahlen.** Marcs stärkste Assets sind messbar (99,8 % Token-Reduktion, 10,1 % Orchestrierungs-Overhead, ~450 PRs in 9 Wochen), aber die Posts handeln von Nachtschichten.
- **Selbstverkleinerung.** "Small thing", "nobody would've noticed" nimmt dem Post die Berechtigung, gelesen zu werden.
- **Falsches Projekt im Schaufenster.** Gepostet wird ChargePilot (Batterieanzeige). Die Arbeit mit echtem Neuigkeitswert ist Myceliums und Shipyard, und dazu passt auch die neue Bio.

Hashtags wie `#buildinpublic` und `#indiedev` bringen bei diesem Followerstand nichts. Das Referenzprofil nutzt in seinen Top-Posts keinen einzigen.

## 3. Regeln für die nächsten Posts

1. Erster Satz enthält eine Zahl mit Einheit oder einen Vergleich.
2. Kein Post ohne zeigbares Artefakt: Screenshot, GIF, Benchmark-Tabelle oder Link zum Repo.
3. Nie die eigene Arbeit im letzten Satz kleinreden. Streiche "small thing", "nobody would've noticed", "just".
4. Keine Hashtags.
5. Launch heißt antworten: 48 Stunden lang jede Antwort beantworten, Bugs sichtbar fixen, Version hochzählen.
6. Ein Post pro Woche darf reine Person sein, ohne Tech.
7. Threads nur, wenn Post 1 allein schon standhält.

## 4. Konkrete Entwürfe aus echten Zahlen

**A. Myceliums, Aufhänger Benchmark**

> AI agents read files to understand a codebase. That is why they burn tokens.
>
> Myceliums parses the repo into a knowledge graph first. Benchmarked over 34 queries against Django, FastAPI, Tokio, Express, Zod and Gin:
>
> 1,692,356 → 2,978 tokens (-99.8%)
> 578 → 34 tool calls (-94%)
> cached lookups ~50 ms
>
> Rust, local only, no telemetry: crates.io/crates/myc

**B. Shipyard, Aufhänger Kostenmessung**

> Everyone guesses what AI orchestration costs on top of the actual work. I measured it.
>
> 10.1% of total spend, tracked per generation in Grafana.
>
> That is the overhead for routing, RBAC, retries and review across ~450 PRs in 9 weeks. 77 of those commits were authored by the platform's own bots.

**C. Shipyard, Aufhänger Selbstheilung**

> My build platform filed its own architecture issue.
>
> A watchdog kept catching the same worker timeout, classified the root cause, and opened an issue for it. That issue became the PR that fixed the healer.
>
> The system proposes. It never merges its own work.

**D. Persönlich, ein Post pro Woche**

> Started as a digital artist, ended up building the pipeline the artists ship on. Ten years later I write Rust at night.
>
> Anyone else here who came into engineering sideways?

## 5. Was am Profil noch offen ist

- **Anzeigename** steht auf "Marc", soll "Marc Mantei" werden. X sperrt das Feld, solange nach dem Handle-Wechsel die Profilprüfung läuft.
- **Avatar** ist ein KI-Bild. Das Referenzprofil nutzt ein echtes Portrait, und bei einem Account, der über Handwerk Vertrauen aufbaut, arbeitet ein generiertes Bild dagegen. Auf Wunsch von Marc vorerst unverändert.
- **Gepinnter Post** fehlt. Sobald einer der Entwürfe oben läuft, gehört der beste ans Profil gepinnt.
