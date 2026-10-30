# X thread draft — quoting @iam_anandv (2026-10-22)

**Trigger post:** https://x.com/iam_anandv/status/2113139835980710149 — "For anyone who wants to track how bad the eMudhra certificate impact mess is on Indian Banks just look at what @CashlessCnsmr maintains (the entire .bank.in cert logs squirreled from various scripts) … 185+ hits on eMudhra."

**Mechanics:** X API cannot post quote-tweets. Two options — (a) you post tweet 1 manually as a QT of Anand's post and continue the thread there, or (b) I post the whole chain as replies under his post. Draft below; every judgement qualified per the damage note (`CyberOpsec/notes/2026-10-22-bankin-emudhra-damage.md`).

---

**1/10**
Thanks @iam_anandv for pointing at our .bank.in cert logs. We assessed it today: TLS scan of all 3,355 live HTTPS hosts + all currently-valid certs in CT. The 185+ eMudhra hits are real. They are not damage. Zero direct damage found. The forward risk has names. 🧵

**2/10**
Context: 8 eMudhra/emSign intermediates had private keys that were tiny integers: 4, 56, 66, 115, 155, 156, 230, 237. Recoverable from the public cert in under a second. Reported 17 Oct, blocked within hours by Firefox/Chrome. Chrome removes emSign ECC Root CA - G3 on Oct 27.

**3/10**
Method (all reproducible from github.com/CCAgentOrg/bank-in-domains): one TLS handshake per live HTTPS .bank.in host (3,355) + all 3,529 currently-valid .bank.in certs in Certificate Transparency. Every chain's issuer and terminating root checked on the wire.

**4/10**
Finding 1: zero .bank.in domains chain through the compromised intermediates (EM DV/EV/OV TLS CA - G3B/G3C). All 120 valid eMudhra certs in CT sit on legacy G1/G2A-1 chains. This matches Chrome's global finding: no leaf cert was ever CT-logged under the compromised CAs.

**5/10**
Finding 2: the Oct 27 root removal breaks nobody in this namespace. We openssl'd the served chains: the eMudhra certs at Bandhan and Bank of India terminate at emSign Root CA - G1 / Root TLS CA - G1, not the G3 root being removed. No .bank.in site fails on the 27th from this.

**6/10**
Finding 3: real exposure is Chrome's open review of eMudhra's remaining roots. Every live chain ends at emSign Root CA - G1. If it goes, these break: Bandhan (13 hosts: retail + corporate netbanking, KYC), Bank of India (3), Jharkhand RGB, J&K Bank, 2 co-ops.

**7/10**
Plus 12 institutions hold valid eMudhra certs in CT, not yet deployed: Canara, Central Bank, Federal, Indian Bank, PNB, Saraswat, South Indian Bank (6 vault hosts), Karnataka Grameena, Odisha Grameen. The re-issue pool if Chrome's review lands hard.

**8/10**
Qualifying our own claims: CT cannot see unlogged certs; the wire scan is the binding check and a point-in-time snapshot. Covers .bank.in web TLS only: not bank.com domains, not app-pinned CAs, not IDRBT's emCA platform. We allege no misuse; only CCA/CERT-In can test that.

**9/10**
What to watch: Chrome's decision on the remaining eMudhra roots; whether Bandhan and Bank of India re-issue early. Their current certs are safe today; this is planning, not panic. If a bank login throws a cert error after an update next week, this is the first place to look.

**10/10**
Data (CC0, daily): github.com/CCAgentOrg/bank-in-domains · Full damage note + chains: cyber.cashlessconsumer.in/pages/emudhra/ · Check your own phone: TrustCheck: zo.pub/cashlessconsumer/trustcheck

---

## Qualification ledger (what each tweet claims and on what evidence)

| Tweet | Claim | Basis | What it does NOT claim |
| --- | --- | --- | --- |
| 1 | zero direct damage found | wire scan + CT, 22 Oct | not "no risk"; not "no misuse anywhere" |
| 4 | no compromised-chain certs in namespace | 0/3,355 served; 0/120 CT G3 | CT blind to unlogged certs (stated in 8/10) |
| 5 | Oct 27 removal breaks nobody here | openssl chain dumps (retail.bandhan, bandhan, e-ots) | other namespaces unaffected |
| 6/7 | named-bank forward risk | served issuers + CT stock | not prediction of Chrome's outcome; Bandhan named because data says so — its certs are on unaffected chains today |
| 8 | scope limits | — | explicitly no misuse allegation |
