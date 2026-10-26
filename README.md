# cyber.cashlessconsumer.in — Security Investigations

Central hub for CashlessConsumer's independent cyber security research on India's
financial and government infrastructure. The index splits into **Our work**
(original research: audits, disclosures, reverse-engineering) and **Our
verifications** (other parties' claims checked against evidence — leak sites,
breach chatter, institutional statements). The `.bank.in` audit and CERT-In
.env disclosures are our original work, not verifications.

**Site:** [cyber.cashlessconsumer.in](https://cyber.cashlessconsumer.in)

## What's here

| Page | Topic |
|------|-------|
| `index.html` | Hub — index of all cyber efforts |
| `pages/bank-in-report.html` | `.bank.in` namespace security audit + IDRBT registry investigation |
 | `pages/toll-shadow-apps.html` | Shadow Toll — 'The FASTag Bypass' (v2.1 report PDF) + open plaza-registry datasets |
| `pages/breaches.html` | Ransomware breach verification index (BoB / Triple X, Dodo / DireWolf) |
| `pages/bob-breach.html` | Bank of Baroda breach verification gateway (links to bobbreach.cashlessconsumer.in) |
| `pages/cert-in-dotenv.html` | CERT-In responsible disclosures — `.env` files on `.bank.in` |
| `pages/sharepoint-structural-gaps.html` | "SharePoint, Structurally Quiet" — on-prem SharePoint's exfiltration gap as design property (pattern-level, no incident referenced) |
| `pages/emudhra.html` | eMudhra CA compromise — eight intermediate certificates with guessable private keys (Oct 2026); gateway to the full consumer investigation + statement + open letter |
| `pages/npci-cl.html` | NPCI UPI Common Library — 17 APKs (2016–2026) reverse-engineered; expired signer certificates; verification kit at CashlessConsumer/npci-cl-evolution |
| `pages/cbi-sfms.html` | Central Bank of India SFMS/RTGS incident (Oct 2026) — ₹13.97 cr in 187 unauthorised transfers; claim-level verification (transfers L4 corroborated / IFTAS-central-SFMS vector L1 disputed by IFTAS), disclosure-gap timeline, consumer explainer; 26 Oct: doors-and-keys section — RTGS Regs 4.21 access channels, IDRBT-CA CPS certificate/token rules, no public MFA mandate for SFMS consoles, one-bank estate documentation (BoB leak, aggregate) |
| `pages/emudhra/` | Full eMudhra investigation site (self-contained brand): consumer guide, public statement, open letter, corporate history of eMudhra |
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
- **emudhra-ca:** master note `Kaarana/notes/2026-10-21-emudhra-statement-open-letter-rbi-meity.md`; desk verification of live TLS handshakes 20-21 Oct 2026; sources footnoted per page (Ars Technica, disclosure site, Mozilla bug, CCA India, IDRBT, RBI). Markdown sources + build script for the section live in the workspace at `Projects/cyber/pages/emudhra/`; this repo carries the served HTML.
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
