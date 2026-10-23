# Padlocked By Guesswork: Who Really Vouches For The Vouchers?

*Dek: The padlock in your browser is a promise: this really is your bank. Last week, one of the companies that keeps that promise admitted its "unknowable" security keys included the number 4. The repair was swift and global. The accountability has been neither.*

**Draft for Decode (bloomlive submission) — same register as "Free To Use, Costly To Run: Who Really Pays For UPI?" (7 Sept 2026). Byline: Srikanth Lakshmanan. All facts verified against CERT-In Advisory CIAD-2026-0050, Mozilla bug 2083449, Google's Chrome Root Program statement, the incident disclosure site and eMudhra's press release, as available on 22 October 2026.**

---

Every time you open your bank's website and see a padlock, you are trusting a company you have never heard of to vouch for a company you have. On 30 April 2025, eMudhra — a Bengaluru firm licensed by the government to certify digital identities, and trusted by every major browser to certify websites — created eight security keys that were supposed to be impossible to guess. Their values were 4, 56, 66, 115, 155, 156, 230 and 237. One of the internet's secrets, held by one of India's largest trust companies, was the number 4.

The world learned this on 17 October 2026, when a researcher proved he could compute the keys from the public certificates. Browsers fixed it within hours. India's licensing regulator has still not said a word.

The public argument this week has mostly been reduced to one question: was anyone attacked? That question matters, but it is also the wrong place to start — because the more answerable questions are who was supposed to be watching, who actually did the watching, and what a government licence means when the licensee fails this publicly.

### What is a certificate authority, and why does it matter to you?

A certificate authority (CA) is the passport office of the internet. Your browser cannot itself know that a website really belongs to your bank. So it outsources the checking: a CA verifies the applicant and issues a TLS certificate — a signed identity document — and the browser, trusting the CA, shows the padlock. The padlock is not a guarantee that the shop is honest. It is a promise about the pipe: nobody between you and the website can read or alter your traffic. Passwords, OTPs, card numbers, Aadhaar submissions — all of it travels inside that promise.

Consumers do not shop for certificate authorities. No one compares CAs the way they compare UPI apps. The choice is made for you, inside trust lists curated by Google, Mozilla, Apple and Microsoft, and you act on the result every day. Which is what makes a failure here different from a failed app or a hidden fee: you never got to choose the intermediary that failed, and you cannot switch away from it.

### What actually broke?

In short: the secrets that make the padlock mean anything were never secrets at all.

The padlock works because the website presents an identity document, and the document is only as convincing as its signature. Behind every certificate sits a private key — a secret number held by whoever is allowed to issue documents in that name. Guard it, and only you can sign. Lose it, and anyone can sign as you. Everything the padlock promises rests on that one number being unguessable.

For this class of key, "unguessable" is engineered, not assumed. A well-made key of this type has about 2^384 possible values — a number so large that no computer could try them all. That is the entire premise. Certificate authorities generate these keys inside tamper-proof hardware, in a formal ritual called a key ceremony — witnessed, scripted, audited — because everything downstream depends on the secret never leaking.

Except, by the company's own account, the failure happened inside exactly that ritual. eMudhra told CERT-In that a flaw in the ceremony's "wrap/unwrap" step produced a second set of weak keys alongside the original strong ones — and the weak keys were the ones published to browser trust stores. Instead of 2^384 possibilities, the eight keys carried between 3 and 8 bits of actual randomness — somewhere between eight and a few hundred possibilities. The difference is not a weaker vault. It is the difference between a vault and a luggage lock with the combination already showing.

And because a certificate is public by design — browsers must be able to download and inspect it — anyone could fetch these certificates and compute the "secrets" inside. The honest arithmetic gets worse: they sat there, recoverable by anyone with a laptop, from 30 April 2025 until 17 October 2026 — nearly eighteen months. Security researcher Scott Helme reproduced the recovery in under a second; a one-line prompt to an AI agent recovered them too. eMudhra revoked the certificates on 18 October and says its broader infrastructure was not compromised and no data was breached. Those are the company's claims, not independently established facts.

### Has anyone been attacked?

Almost certainly not en masse — and, honestly, nobody outside a forensic investigation can prove even that. Both halves of that sentence matter.

The reassuring half: Certificate Transparency logs, which record certificates issued in the open, show nothing fraudulent minted from these keys across the entire window. eMudhra says the affected intermediates never issued an ordinary website certificate at all, and only one of the eight was even deployed in production. CERT-In's advisory, unusually candid for an Indian incident notice, states that as of 21 October the public disclosures "do not establish confirmed malicious exploitation".

The honest caveat is that a targeted attack would never show up in any public log. An attacker who mints one fake certificate for one victim's banking session has left no certificate trail — only a victim who saw a normal padlock. And the clients least protected by the public safeguards are exactly where Indian users live: banking apps validate against Android's system trust store, which does not enforce the transparency checks that protected desktop browsers. Seventeen and a half months is a long window, and state and criminal collectors stockpile precisely this class of capability.

Absence of public evidence is a reason to investigate calmly. It is not a certificate of innocence — a phrase worth remembering when the investigation itself has no announced owner.

### Who caught it, and who fixed it?

A pseudonymous researcher known as "Wayne" reported the compromise to Mozilla and Chrome on 17 October, proving control of every key by signing a message with each one. Mozilla independently recovered the keys within two hours. Chrome blocked the affected certificates the same evening; Firefox finished pushing the block by night. Apple followed on 19 October, Microsoft and an emergency Go update on 20 October, alongside Firefox 158.0.1, updated Ubuntu packages and a public test site anyone can use to check their own machines. Sectigo, which had co-signed the same keys in May 2025 — extending the set of browsers prepared to accept them — took revocation steps too.

It worked — because of a volunteer researcher, a public bug tracker and browser security teams sitting outside India, none of them obliged by Indian law to care about Indian users. Meanwhile the market delivered its verdict before the regulator managed its first sentence: eMudhra's shares fell 20% to the lower circuit — the exchange's maximum permitted daily fall — on 21 October, the same day CERT-In finally published.

### Why was India's regulator silent?

This is the question that matters more than the key values themselves.

India does have a regulator for this. Under the IT Act, 2000, the Controller of Certifying Authorities (CCA) licenses and supervises CAs; eMudhra has held its licence since November 2008, with renewal to 2028. But the eight broken keys lived in eMudhra's *international* emSign hierarchy — the side that browsers trust — which is governed not by the CCA but by foreign root programs and international WebTrust audits. In practice, the world's trust in this Indian company was policed from Mountain View, San Francisco and Cupertino, not New Delhi.

CERT-In broke the official silence on day four with a competent advisory. The CCA — the statutory body whose licence covers this company — had published nothing findable as of 22 October. Nor does the Indian regime offer the public anything to check against: there is no incident process for licensed CAs, and the auditors who certify a CA's fitness are chosen and paid by the CA itself. Compare Mozilla's bug tracker — public, dated, answerable to everyone — and the asymmetry is stark. CERT-In's six-hour incident-reporting rule applies to events like this; whether eMudhra reported within it is not publicly known.

The dependence itself is Indian, even where the failure was not. A simple check of UIDAI's and the government marketplace GeM's websites shows both serving certificates from an eMudhra issuer — different, valid chains, not the broken ones, and not an accusation. IDRBT, the RBI-established institute that runs the banking sector's certifying authority, builds its issuance on eMudhra's emCA platform, with over three lakh certificates for interbank messaging. The company's Rs 701.6 crore of FY2026 revenue includes about a third from government and defence customers. The state is this vendor's largest customer, and its supervisory apparatus had nothing to say for four days while foreign volunteer infrastructure did the firefighting.

### What happens on 27 October?

This is where the incident stops being abstract. Chrome is not just blocking the eight keys; it is removing their parent root — the master certificate they were all issued under, emSign ECC Root CA – G3 — from its trust store entirely, reaching all users on 27 October. Mozilla has already done the same. The point is to protect devices that never receive interim revocations, but the side effect is real: some 30,000 legitimate certificates chaining to that root — most issued automatically — will simply stop working in Chrome until the sites migrate, and eMudhra has committed to moving its subscribers.

Chrome is also reviewing whether eMudhra's remaining root should stay trusted at all. If that review goes the way of the first, public-interest websites that chose this vendor will stop loading for updated browsers — and ordinary users, who never chose any of this, will bear the outage. That is why migration needed to start this week, sequenced with the browser makers, not after the first government website fails to open.

### What should you do?

Update your browser, phone and laptop. That single step covers most of the risk, because current Chrome and Firefox already reject the broken chains.

Then test your own machine: opening https://dv-g3b-emudhra.we-have-a-problem.com/ should produce a certificate error. An error is good news — it means your tooling refuses the compromised keys. If the page loads anyway, your system still trusts them and needs updating. On Android the honest position is uncomfortable: stock Android offers no switch to turn off a built-in authority, so the fix is the system update, and until it lands a browser with its own trust store (Firefox for Android, for example) is the safer route for banking. A small free tool from CashlessConsumer, TrustCheck, tests whether your specific phone still accepts the chains.

If you run servers or a business, the browser is the least of it. Build pipelines, dependency installers, container images and monitoring boxes carry their own copies of internet trust, and each needs its patched bundle — this is the long tail that will outlive the news cycle. If you buy eMudhra certificates, ask for the root-cause analysis in writing, and migrate anything chaining to the removed root before 27 October.

### What should India take from this?

In 2016, when Facebook's Free Basics tried to split the internet into a free tier and a paid one, a million emails to TRAI forced an open consultation, and the country set itself a standard: decisions about shared digital infrastructure are made in the open, with the people who use them in the room. Your previous correspondent argued, in these pages, that UPI pricing will be tested against that bar. The same test applies here, with more force — because trust is the one infrastructure you cannot see, choose or exit.

A licence is a public claim that someone verified something. The CCA licensed eMudhra as fit to hold India's digital trust until 2028; IDRBT builds banking PKI — the public-key machinery behind interbank messaging — on the company's platform; UIDAI and GeM serve its certificates. This week the company signed with the number 4, re-signed revocation lists — the internet's do-not-trust bulletins — rather than halt, and explained it in a foreign bug tracker — and the licence has said nothing. Whether anyone was harmed cannot yet be known. Whether the licence means anything can be, and it is the easier of the two questions to answer in public.

Crores of us bank and pay online every day and never think about the padlock. It should not take a foreign bug tracker for the country to learn that its own bank's front door is sound — or to hear, from its own regulator, what the licence actually certified.

---

**Editor notes (not for publication):**

- Length: \~2,200 words body. Decode ran the UPI op-ed at similar length with 9 question-heads; this has 8.
- All figures verifiable: CERT-In advisory CIAD-2026-0050 (21 Oct 2026) for the company claims, BDO/WebTrust context, revocation date and "do not establish confirmed malicious exploitation" line; Mozilla bug 2083449 for the \~30,000-cert/97%-ACME figure and response timeline; Google Chrome blog for the 27 Oct root removal; thehackernews.com (20 Oct) for the Microsoft/Go/Ubuntu/Firefox 158.0.1 dates and the six-TLS-plus-two-code-signing split; Scott Helme's "Eight Bits of Trust" for the sub-second recovery and AI-agent recovery; Moneycontrol (21 Oct) for the 20% lower-circuit fall; corporate figures (Rs 701.6 crore, 32% government/defence, 50M+ certificates, licence to Nov 2028) from eMudhra filings as compiled at cyber.cashlessconsumer.in/pages/emudhra/company.html; UIDAI/GeM/IDRBT dependencies from our own desk verification of 20–21 Oct (live TLS handshakes, sandbox + Mumbai vantage).
- Companion formats available on request: a 101-style fact-checked explainer (already published on cashlessconsumer.in), X-thread cut of this piece, and TrustCheck (Android app that tests a user's own device).