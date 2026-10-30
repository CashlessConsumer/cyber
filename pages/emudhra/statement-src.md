
We are CashlessConsumer, a consumer collective working on digital payments and public digital infrastructure. Below is a failure most Indians will never see, in a system everyone depends on. Every claim here is sourced. Where we checked something ourselves, we say so.

**What happened.** The padlock in your browser stands for a promise: this really is your bank. Keeping that promise is the job of companies called Certificate Authorities, which browsers agree to trust. One of the most embedded of them in India is eMudhra Ltd of Bengaluru: licensed by the Controller of Certifying Authorities (CCA India),[^5] listed on the stock exchanges, and a certificate supplier to government websites.

eMudhra created these eight intermediate certificates on 30 April 2025, and Sectigo cross-signed them on 14 May 2025. Their private keys were not random. A key of this class should allow about 2³⁸⁴ possible values; these eight contained 3 to 8 bits of actual randomness. Their values were 4, 56, 66, 115, 155, 156, 230 and 237. One of the "unknowable" keys of one of India's largest trust companies was the number 4. An AI agent recovered a key on its first attempt with a one-line prompt, as recorded in the Mozilla incident tracker by the researcher coordinating the response.[^1][^2]

Anyone holding such a key can mint a credential for any website on earth (your bank, Gmail, UIDAI), and browsers will call it genuine. The padlock shows. No warning appears. From 30 April 2025 until the researcher's proof surfaced on 17 October 2026 — nearly eighteen months — anyone could have recovered these keys from the public certificates. This is not a forecast: the keys are public, and deriving all eight takes minutes on a laptop.

**Who caught it.** A researcher known as "Wayne" reported the flaw on 17 October 2026, proving control of the keys by signing a message with each one. Firefox and Chrome stopped trusting all eight intermediates within hours. Apple followed on 19 October. A public disclosure site with test endpoints went up on 20 October.[^2] The system worked. It worked because of a volunteer researcher, an AI agent, and browser security teams sitting outside India.

**What we are not saying.** We make no allegation of misuse. We did not investigate whether anyone exploited these keys; that requires powers and access we do not have. Certificate Transparency shows nothing was minted from them across the entire exposure window — but CT binds only CT-enforcing browsers, and the disclosure coordinator's own site states: "We do not know if attackers exploited the flawed key generation to target these clients."[^2] We treat that as a reason to investigate calmly, not as a certificate of innocence. Our demand stands whether or not any harm occurred: the failure itself, and the silence around it, are the case.

**What no Indian authority has said.** As of 21 October 2026, we could not find a public statement, order or incident record on this matter from CCA India, RBI, IDRBT, UIDAI or GeM. The statutory body that licenses eMudhra has published nothing. There is no public incident process for Indian-licensed CAs at all. Certificate auditors in India are chosen and paid by the companies they audit.

The vendor's own account, on the public record, does not comfort. Keys meant to stay locked inside tamper-proof hardware were made exportable under an "approved deviation" and shipped to data centres in the US and EU, in the name of "data sovereignty". Indian policy insists data stay in India; the vendor made the keys portable instead. When revocation lists signed with the correct keys failed verification, eMudhra re-signed them with the broken keys rather than halting issuance and investigating.[^3] We ask the obvious question: if a licensed trust company cannot stop itself from signing with a key it knows is broken, what exactly did the licence certify?

**Why this lands on Indian desks.** Our own desk checks, 20–21 October 2026, from Indian and sandbox vantages:[^8]

- uidai.gov.in and gem.gov.in, the Government e-Marketplace, serve website certificates issued by eMudhra. We offer this as a fact of jurisdiction, not as evidence of compromise: these chains are different from the compromised ones and remain trusted.
- IDRBT, the RBI-established institute that certifies Indian banking, builds its issuance on eMudhra's emCA platform, with over 3,00,000 certificates issued for interbank messaging and national payment systems.[^6][^7]
- Chrome is formally reviewing "the status of eMudhra's remaining CA certificate".[^4] If that root goes, these websites stop loading in updated browsers until they migrate. Consumers would bear a vendor's failure.
- The devices least likely to ever receive a trust update are years-old Android phones, smart TVs and forgotten servers. That is also a fair description of what most Indians use. The long tail of this incident is Indian.

**What we ask.** Two things, in order: an open and verifiable investigation, and a remediation path for consumers if it finds harm. The full open letter to RBI and MeitY follows below. In summary:

1. An open, verifiable, published investigation into eMudhra's licensed operations: the key-generation ceremonies behind the eight certificates, the "approved deviation" that made keys exportable, the transfer of keys overseas, and the re-signing of revocation lists with a known-broken key. Evidence preserved, findings public.
2. CERT-In: confirm whether this incident was reported within the 6-hour window the April 2022 directions require, and publish the action taken.[^10]
3. A standing public incident process for licensed CAs, on the model Mozilla and Chrome already run free of charge for the same vendors.
4. Certificate audits appointed and paid by the regulator, not the vendor.
5. A consumer remediation framework agreed in advance: if the investigation establishes any interception, affected people are notified and made whole, the cost falls on the responsible vendor, and liability between certificate authority, website operator and payment provider is settled by rule, not by fight.
6. UIDAI, GeM and IDRBT: publish your certificate issuers and pre-position migration away from eMudhra roots, sequenced with browser makers so no distrust decision lands on users unannounced.
7. RBI: guidance to regulated entities on trust-store updates in banking apps and channels.

**What you should do today.** Update your browser, phone and computer. That one step covers most of the risk. If you run servers, containers or CI systems, list everything that checks certificates and update its trust stores. If your organisation buys eMudhra certificates, ask for the root-cause analysis in writing.

Crores of us press "pay" every day and never think about the padlock. The machinery that keeps the padlock honest sits mostly outside India, and the part inside India has no public way to prove it works. It should not take a foreign bug tracker for the country to learn its own bank's front door is sound.

*— CashlessConsumer · cashlessconsumer.in · cashlessconsumerin@gmail.com*

[^1]: Dan Goodin, "The Internet goes on high alert after discovery of 8 compromised TLS certs," Ars Technica, 20 Oct 2026 — https://arstechnica.com/security/2026/10/the-internet-goes-on-high-alert-after-discovery-of-8-compromised-tls-certs/
[^2]: "eMudhra Intermediate CA Compromise" public disclosure site, 20 Oct 2026 — https://emudhra.we-have-a-problem.com/
[^3]: eMudhra statement and Mozilla researcher verification, Mozilla bug 2083449 — https://bugzilla.mozilla.org/show_bug.cgi?id=2083449
[^4]: Chrome root program statement; Hacker News discussion, 20–21 Oct 2026 — https://news.ycombinator.com/item?id=50166579
[^5]: CCA India, eMudhra Certification Practice Statement and eSign empanelment records — https://cca.gov.in/sites/files/pdf/Licensed-CA/eMudhra-CPS-v2.1.pdf · https://cca.gov.in/service-providers.html
[^6]: IDRBT, "Certifying Authority" — https://www.idrbt.ac.in/certifying-authority
[^7]: eMudhra case study, "IDRBT Secures Banking PKI Infrastructure" (emCA/emRA deployment) — https://emudhra.com/en/resources/idrbt-india-pki
[^8]: Desk verification, CashlessConsumer/Kaarana, 20–21 Oct 2026: live TLS handshakes for uidai.gov.in, gem.gov.in, esign.emudhra.com, idrbt.ac.in, idrbtca.org.in, npci.org.in, rbi.org.in, mca.gov.in, digilocker (sandbox + Oracle Cloud Mumbai vantage); compromised-chain structure from https://emudhra.we-have-a-problem.com/chains.zip
[^10]: CERT-In Directions under section 70B(6) of the IT Act, 28 April 2022 (CIR/2022/11) — six-hour incident reporting requirement — https://www.cert-in.org.in/
