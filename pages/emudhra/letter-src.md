## Open letter to the Reserve Bank of India and the Ministry of Electronics and Information Technology — the state's own trust infrastructure rests on a vendor that signed with the number 4

**From:** CashlessConsumer (consumer collective) · cashlessconsumerin@gmail.com
**To:** The Governor, Reserve Bank of India, Central Office, Mumbai · The Hon'ble Minister for Electronics and Information Technology, Government of India, New Delhi
**CC:** Secretary, MeitY · Controller of Certifying Authorities (CCA India) · Director-General, CERT-In · Director, IDRBT · CEO, UIDAI · CEO, GeM · MD, NPCI · Mozilla Root Program · Google Chrome Root Program · Apple Product Security · MD, eMudhra Ltd (right of reply)

**Date: 21 October 2026 · This is a draft for internal review; not yet sent or published.**

To the Governor of the Reserve Bank of India and the Minister for Electronics and Information Technology,

We are a consumer collective that works on digital payments and public digital infrastructure. We make no allegation that any Indian system was attacked; we did not investigate misuse, and we are not positioned to. This letter asks for two things: an open, verifiable investigation into a public failure at a licensed Indian trust company, and a remediation path for consumers if that investigation finds harm. We add one observation no one else has put on the record: no Indian authority has said anything about this incident that the public can read.

## 1. What happened (all independently verifiable)

On 30 April 2025, eMudhra Ltd, an Indian company licensed by the Controller of Certifying Authorities under the IT Act,[^5] whose emSign brand is trusted by every major browser, issued eight intermediate CA certificates whose private keys carried 3 to 8 bits of randomness. The keys were recoverable by anyone from that day until revocation on 18 October 2026 — nearly eighteen months. A NIST P-384 key of this class should have about 2³⁸⁴ possible values. The eight keys are 4, 56, 66, 115, 155, 156, 230 and 237. One key was the number 4. An AI agent recovered a key on its first attempt using a one-line prompt; the Mozilla researcher coordinating the response recorded this in the incident tracker.[^1][^2]

The fix came from outside the country. A researcher known as "Wayne" proved key control on 17 October by signing a message with each key. Firefox and Chrome distrusted all eight intermediates within hours; Apple followed on 19 October; a public disclosure site with test endpoints went up on 20 October.[^2] Certificate Transparency shows no certificates were minted from the compromised keys. We make no claim of interception or misuse, and we did not attempt a forensic assessment of any Indian system. That work belongs to the authorities we are writing to.

eMudhra's own account, on the public record, is as follows. The keys were meant to be non-exportable inside tamper-proof hardware. An "approved deviation" made them exportable because these keys were "meant for export" to US and EU data centres for "data sovereignty" reasons. Seven of the eight intermediates, by the vendor's account, never reached operational production; one did.[^3] A script flaw used test keys as real issuer keys. When revocation lists signed with the correct keys failed verification, the company re-signed them with the broken keys instead of halting issuance and investigating.[^3] The compromised intermediates are held by the company's Netherlands and US entities.[^3]

## 2. What we verified about Indian dependency (our own desk work)

On 20–21 October 2026 we ran live TLS handshakes against government and banking endpoints from sandbox and India-based (Oracle Cloud Mumbai) vantages, and inspected the served chains:[^8]

- **uidai.gov.in** serves its web certificate from an eMudhra issuer (EM OV TLS CA - G2A-1, chaining to emSign Root CA - G1); so does **gem.gov.in**, the Government e-Marketplace.
- **IDRBT**, the RBI-established institute that certifies Indian banking, publicly documents its issuance on eMudhra's emCA/emRA platform, with over 3,00,000 certificates for interbank messaging on INFINET and national payment systems.[^6][^7]
- Chrome's root program is explicitly reviewing "the status of eMudhra's remaining CA certificate".[^4] If root programs remove eMudhra's roots, these websites stop loading in updated browsers until they migrate. That outage would be avoidable if migration is sequenced now.

We list these chains as jurisdiction, not as evidence of compromise: none of them is among the compromised intermediates, and all remain trusted today. Our point is narrower. A licensed Indian vendor sits inside the certificate paths of public infrastructure you govern, it has just failed a basic competence test in public, and the supervisory apparatus has said nothing. As of 21 October 2026, we could locate no public statement, order or incident record from CCA India, RBI, IDRBT, UIDAI or GeM on this matter. The IT Act's licensed-CA regime publishes audit summaries; it has no public incident process. Certificate auditors in India are engaged and paid by the CAs they audit.

## 3. Why this is a trust problem, not a technicality

Consumers do not choose certificate authorities. They are told the padlock means "safe", and they act on that. The promise held this week because of Mozilla's bug tracker, browser revocation feeds and an outside researcher: three mechanisms that sit outside Indian law.

The same week, IDRBT stands as the exclusive registrar for .bank.in, the trust-marked banking domain authorised by NIXI under MeitY.[^9] A trust mark is a claim that someone verified something. The same institute's certificate platform runs on the vendor that could emit the number 4 as a "secret" key and re-sign broken revocation lists rather than stop. Consumers are entitled to ask: who audits the trust mark?

There is also a sovereignty contradiction we ask MeitY to address head-on. Indian policy mandates data localisation. The vendor's keys, the root of trust itself, were made exportable to serve foreign data centres, and now sit with overseas group entities. Data residency rules did not bind the thing that actually matters: the keys. And the licence regime does not even try: the Controller's own CA Licensing Guidelines list key export among the key-management controls its audits examine, yet prescribe no territorial rule on where an Indian-rooted CA's trust keys may live.[^11] We ask what those audits recorded of the wrap/unwrap deviation and of the export arrangement itself.

## 4. What we ask (numbered for answer; we request a response within 14 days)

**To MeitY and CCA India:**

1. **Commission an open, verifiable, published investigation** into eMudhra's licensed-CA operations: the key-generation ceremonies for the affected intermediates, the "approved deviation" that made keys exportable, the shipment of keys to overseas data centres, and the re-signing of revocation lists with a known-broken key. Preserve all evidence, engage independent experts, and publish findings and remediation orders in full.
2. **Confirm CERT-In reporting:** was this incident reported within the 6-hour window mandated by the April 2022 Directions, and what action followed? Publish the answer.[^10]
3. **Establish a public incident process** for licensed CAs: a public tracker, root-cause statements, remediation timelines, equivalent to what Mozilla and Chrome already provide for the same vendors free of charge.
4. **Reform the auditor conflict:** certification audits of CAs should be appointed and paid by CCA India, not by the CA.
5. **Require UIDAI and GeM to publish their TLS issuer inventories** and pre-position migration away from eMudhra roots, sequenced with root programs so that no distrust decision lands on consumers unannounced. We offer this as continuity planning, not as a finding of compromise.

**To the Reserve Bank of India:**

6. **Direct IDRBT to publish the key-ceremony record** of its emCA deployment: who generated the banking sector's keys, on what hardware, witnessed by whom, audited by whom.
7. **Stand up a consumer remediation framework for certificate-related harm:** if any investigation establishes interception through a compromised certificate, affected consumers are notified and made whole, the vendor carries the cost, and liability between certificate authority, website operator and payment provider is fixed by rule in advance rather than litigated after the fact. Route complaints through the Banking Ombudsman scheme in the interim.
8. **Commission and publish an independent exposure assessment of banking PKI**, issue supervisory guidance to regulated entities on trust-store updates for banking apps and channels, and condition the .bank.in trust mark on verifiable, published PKI hygiene for the registry and its suppliers.

**Joint / ecosystem:**

9. **Issue a national PKI incident-reporting and public-disclosure standard** for certificate authorities and critical digital-infrastructure suppliers, including a consumer-notification threshold, harmonised with CERT-In's directions.
10. **Coordinate with Mozilla, Chrome and Apple root programs now** on sequencing, so any future distrust decision cannot break public-interest websites for ordinary users.

To be plain about our own limits: we are a consumer collective, not a forensics lab. We have not alleged misuse by anyone. We ask that the investigation be open enough that neither suspicion nor reassurance needs to be taken on faith.

If this letter receives no public response within 14 days, we will file Right to Information applications on items 1–7 and publish the letter with a non-response annotation. We would rather have your answers than your files.

We are available for any clarification. Every figure in this letter is sourced below or marked as our own verification.

Yours sincerely,

**CashlessConsumer** (consumer collective) · cashlessconsumer.in · cashlessconsumerin@gmail.com

*\[signatory name to be added\]*

[^1]: Dan Goodin, "The Internet goes on high alert after discovery of 8 compromised TLS certs," Ars Technica, 20 Oct 2026 — https://arstechnica.com/security/2026/10/the-internet-goes-on-high-alert-after-discovery-of-8-compromised-tls-certs/
[^2]: "eMudhra Intermediate CA Compromise" public disclosure site, 20 Oct 2026 — https://emudhra.we-have-a-problem.com/
[^3]: eMudhra statement and Mozilla researcher verification, Mozilla bug 2083449 — https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
[^4]: Chrome root program statement; Hacker News discussion, 20–21 Oct 2026 — https://news.ycombinator.com/item?id=50166579
[^5]: CCA India, eMudhra Certification Practice Statement and eSign empanelment records — https://cca.gov.in/sites/files/pdf/Licensed-CA/eMudhra-CPS-v2.1.pdf · https://cca.gov.in/service-providers.html
[^6]: IDRBT, "Certifying Authority" — https://www.idrbt.ac.in/certifying-authority
[^7]: eMudhra case study, "IDRBT Secures Banking PKI Infrastructure" (emCA/emRA deployment) — https://emudhra.com/en/resources/idrbt-india-pki
[^8]: Desk verification, CashlessConsumer/Kaarana, 20–21 Oct 2026: live TLS handshakes for uidai.gov.in, gem.gov.in, esign.emudhra.com, idrbt.ac.in, idrbtca.org.in, npci.org.in, rbi.org.in, mca.gov.in, digilocker (sandbox + Oracle Cloud Mumbai vantage); compromised-chain structure from https://emudhra.we-have-a-problem.com/chains.zip
[^9]: RBI operationalisation of .bank.in; IDRBT appointed exclusive registrar, authorised by NIXI under MeitY — RBI press release/notifications, 2024–25; bank migration guidance via IDRBT (sahyog@idrbt.ac.in).
[^10]: CERT-In Directions under section 70B(6) of the IT Act, 28 April 2022 (CIR/2022/11) — six-hour incident reporting requirement — https://www.cert-in.org.in/
[^11]: CCA India, CA Licensing Guidelines v2.2, 9 September 2025 — audit criteria list "Key Management: Key Generation, Key Storage, Key Destruction, and Key Export"; no territorial restriction on CA key location appears in the guidelines — https://cca.gov.in/sites/files/pdf/guidelines/CCA-CALIC.pdf
