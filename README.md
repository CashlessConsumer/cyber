# cyber.cashlessconsumer.in — Security Investigations

Central hub for CashlessConsumer's independent cyber security research on India's
financial and government infrastructure.

**Site:** [cyber.cashlessconsumer.in](https://cyber.cashlessconsumer.in)

## What's here

| Page | Topic |
|------|-------|
| `index.html` | Hub — index of all cyber efforts |
| `pages/bank-in-report.html` | `.bank.in` namespace security audit + IDRBT registry investigation |
| `pages/toll-shadow-apps.html` | Shadow Toll — 'The FASTag Toll Scam: Press Release vs. Reality' (v2 neutral-analysis report PDF) + open plaza-registry datasets |
| `pages/breaches.html` | Ransomware breach verification index (BoB / Triple X, Dodo / DireWolf) |
| `pages/bob-breach.html` | Bank of Baroda breach verification gateway (links to bobbreach.cashlessconsumer.in) |
| `pages/cert-in-dotenv.html` | CERT-In responsible disclosures — `.env` files on `.bank.in` |
| `pages/about.html` | Methodology, ethics, disclosure policy |
| `pages/toll-shadow-apps-explainer.pdf` | 25-page LaTeX (Eisvogel) explainer: cover, TOC, index, 5 charts, 22 sections |

## Structure

| Path | Purpose |
|------|---------|
| `index.html` | Landing / hub page |
| `pages/` | Individual investigation pages |
| `data/` | Open datasets referenced by pages (CSV) |
| `css/style.css` | Shared stylesheet (dark security theme) |
| `js/main.js` | Shared nav + theme toggle |
| `CNAME` | Custom domain: cyber.cashlessconsumer.in |
| `.github/workflows/deploy.yml` | GitHub Pages build & deploy |

## Data provenance

- **bank-in:** `Projects/bank-in-research/bank_domains_status.csv`,
  `bank_domains_ct_expansion.csv`, `bank_tld_domains_status.csv` — plus the
  live data repos `CCAgentOrg/bank-in-domains` and `bank-domains-ui`.
- **bob-breach:** Verbatim headline stats match `BoBBreach` (metadata-level;
  names/paths/volume only).
- **toll-shadow-apps:** IHMCL NH fee-plaza list (Aug 2025 PDF, gov source) parsed via
  `pdftotext -layout` — 1,129 plazas, 22 states. Scam-plaza crosswalk from STF/ED
  press coverage (see `Documents/research/FASTagScam/` for the full evidence folder).
- **cert-in-env:** `Projects/bank-in-research/bank_in_env_scan.csv`,
  `bank_in_env_exposure.md`, `CERT-In-reply-draft.md`.
- **toll-shadow-apps:** `data/toll-plazas-ihmcl-aug2025.csv` — parsed from
  IHMCL's official "List of Fee Plazas on NH" PDF (Aug 2025, 1,129 plazas,
  22 states) via `pdftotext -layout` + row-wrap-tolerant parser (source PDF +
  script in `Documents/research/FASTagScam/`, public copy at
  https://zo.pub/cashlessconsumer/fastagscam-open-data). Scam-plaza NETC
  crosswalks (Atraila 320132, Patni Pratappur 536051, Baleni 320137, Faridpur
  520036, Madanpur 378006) verified against press lists. All data public-domain
  government material; no PII.

## Maintainers

CashlessConsumer — independent fintech & digital public infrastructure research. X: [@logic](https://x.com/logic)

## License

Published for research and education. No PII from any investigation is distributed in this repo.
