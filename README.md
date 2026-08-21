# cyber.cashlessconsumer.in — Security Investigations

Central hub for CashlessConsumer's independent cyber security research on India's
financial and government infrastructure.

**Site:** [cyber.cashlessconsumer.in](https://cyber.cashlessconsumer.in)

## What's here

| Page | Topic |
|------|-------|
| `index.html` | Hub — index of all cyber efforts |
| `pages/bank-in-report.html` | `.bank.in` namespace security audit + IDRBT registry investigation |
| `pages/bob-breach.html` | Bank of Baroda breach verification gateway (links to bobbreach.cashlessconsumer.in) |
| `pages/cert-in-dotenv.html` | CERT-In responsible disclosures — `.env` files on `.bank.in` |
| `pages/about.html` | Methodology, ethics, disclosure policy |

## Structure

| Path | Purpose |
|------|---------|
| `index.html` | Landing / hub page |
| `pages/` | Individual investigation pages |
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
- **cert-in-env:** `Projects/bank-in-research/bank_in_env_scan.csv`,
  `bank_in_env_exposure.md`, `CERT-In-reply-draft.md`.

## Maintainers

CashlessConsumer — independent fintech & digital public infrastructure research. X: [@logic](https://x.com/logic)

## License

Published for research and education. No PII from any investigation is distributed in this repo.
