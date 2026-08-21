# ARCHITECTURE — cyber.cashlessconsumer.in

> Status: LIVE · Owner: CashlessConsumer · Host: GitHub Pages (+ custom domain)

## Positioning

This is the **index surface** for CashlessConsumer's independent cyber security
research. It showcases three flagship efforts and links outward to full
investigations. It is deliberately **static** (plain HTML/CSS/JS, no build
step at deploy) — matching the proven `BoBBreach` deployment pattern and
removing runtime dependencies. Nothing here stores or surfaces PII.

## Bounded contexts (the three pillars)

| Context | Responsibility | Where the depth lives |
|---|---|---|
| `bank-in` | `.bank.in`/financial-TLD namespace audit + IDRBT registry investigation | live data at CCAgentOrg/bank-in-domains + bank-domains-ui; IDRBT report at bankin-report.cashlessconsumer.in |
| `bob-breach` | Verification gateway only — signs the key facts, points to the full investigation | CashlessConsumer/BoBBreach → bobbreach.cashlessconsumer.in |
| `cert-in-env` | Responsibly-disclosed `.env`/actuator/phpinfo/log exposures on `.bank.in` | evidence distilled from bank-in-research scan + CERT-In timeline |

A **reporter plane** (about + methodology + disclosure policy) is a shared
context referenced by all three pages.

## Content contract

The three pillar pages expose a stable, machine-checkable fact surface so the
site can be regenerated from data without hand-edited HTML absorbing drift:

- `bank-in`: math-critical tables (`top banks`, `UAT count`, `TLD parallels`).
- `bob-breach`: signed headline stats (162,111 files · 16,474 dirs · ~1.07 TB ·
  1,088+ branches · Triple X · 24 Jul 2026).
- `cert-in-env`: the exposure ledger + remediation status column.

`ARCHITECTURE.md` is the single reference for column semantics and for which
source CSV feeds each figure, so re-runs and corrections stay deterministic.

## Data provenance

- **bank-in:** `Projects/bank-in-research/bank_domains_status.csv`,
  `bank_domains_ct_expansion.csv`, `bank_tld_domains_status.csv`
  (Wayback CDX · HackerTarget CT · live DNS/HTTPS probes).
- **bob-breach:** BoBBreach crawl/`investigation_worthy/` metadata (names &
  paths only, no file contents).
- **cert-in-env:** `Projects/bank-in-research/bank_in_env_scan.csv`,
  `bank_in_env_exposure.md`, `CERT-In-reply-draft.md`.

## Ethics constraints (non-negotiable)

1. **No PII.** Only key *names* and response metadata were recorded for `.env`
   exposures — never credential values.
2. **Responsible disclosure first.** All findings reported to CERT-In / RBI /
   affected institutions before publication.
3. **Metadata only for BoB.** The breach page describes file names/paths/volume,
   not file contents.

## Deployment

- GitHub Pages under `CashlessConsumer/cyber`, branch `main`.
- Workflow `.github/workflows/deploy.yml` copies the static tree to `_site`
  and deploys. Custom domain via `CNAME` (`cyber.cashlessconsumer.in`).
- DNS: the domain's `cashlessconsumer.in` manager keeps a `cyber` CNAME →
  `cashlessconsumer.github.io` record (same mechanism as `bobbreach`).

## Repository layout

```
cyber/
├── index.html            hub
├── pages/                bank-in-report · bob-breach · cert-in-dotenv · about
├── css/style.css         shared theme
├── js/main.js            nav + theme toggle
├── CNAME
├── .github/workflows/deploy.yml
```
