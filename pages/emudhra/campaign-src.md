# Open the books on eMudhra {#top}

*Public audit campaign · CashlessConsumer · 23 October 2026*

When you press "pay", sign a company filing, or bid on a government tender, an eMudhra product sits somewhere in the chain: the certificate, the signing software, or the platform that issued both. Eight of that company's "secret" signing keys turned out to be small enough to guess. One of them was the number 4. The licence that lets this company operate India's trust infrastructure is renewed every five years. A licence renewal is not an audit. It is a subscription.

We are asking for the subscription to come with proof of service: a transparent public audit of eMudhra's role across Indian banking and government technology. Below is the evidence, the demands, and a two-minute way to add your name.

## Why now

On 17 October 2026, a researcher using the name Wayne reported to browser vendors that eight intermediate CA certificates operated by eMudhra's emSign programme had private keys recoverable by anyone from the public certificate. The keys were generated at a key ceremony on 30 April 2025 with 3 to 8 bits of entropy instead of the expected 384; the eight values were 4, 56, 66, 115, 155, 156, 230 and 237 (public record: the incident tracker at emudhra.we-have-a-problem.com and CCADB entries).[^1] Firefox, Chrome, Apple and Microsoft blocked the affected chains within days. eMudhra revoked the certificates on 18 and 19 October 2026.

Three facts make this a campaign and not just an incident.

**First, the window.** The weak keys worked for roughly seventeen and a half months. Certificate Transparency logs contain zero certificates issued from them, which proves desktop browsers with CT enforcement were not attacked through logged issuance. It does not prove non-CT clients, including most Android banking apps, were not.[^2] The incident's own coordinator writes: "We do not know if attackers exploited the flawed key generation to target these clients."[^1] No one can say "no misuse" from the outside. Only a forensic audit with issuance logs and network telemetry can.

**Second, the footprint.** eMudhra is not one vendor among many. It is the vendor behind (verified by us on 22 October 2026 unless noted):

| Where | What eMudhra supplies | Evidence |
| --- | --- | --- |
| IDRBT Certifying Authority | The emCA and emRA platform that issues certificates for RBI, banks and financial institutions on INFINET and national payment systems | eMudhra's own case study PDF; the IDRBT CA subscriber portal runs at praman.idrbtca.org.in/emRASubscriber/ [^3] |
| IDRBT CA operations | The 19 January 2026 cutover to the new platform, which required reissue and revocation of every certificate issued before that date | idrbtca.org.in notices [^3] |
| .bank.in domains | 120 currently valid certificates across 49 bank hostnames, on eMudhra chains | Our CT and TLS scans, 22 October 2026 [^4] |
| Banks' signing workflows | The emSigner multi-tenant SaaS; hostnames visible in CT logs include iciciapp, iciciweb, kotak, rbl, sbicards (plus an admin host), iob, aubank, muthootmicrofin, asirvadmicrofinance, hindujahousingfinance | Our CT observations, 22 October 2026 [^4] |
| Digital signing at desks | emBridge, the localhost signing middleware installed on officials' computers, including the one proxied by IDRBT's own portal | Our June 2026 investigation [^5]; CDSL's public installation guide [^6] |
| eSign | eSign Service Provider empanelled since 25 June 2015 | CCA service providers page [^7] |
| Government e-marketplace | GeM's buyer onboarding routes eSign through eMudhra registration and requires the emBridge app | GeM buyer FAQ [^8] |
| Certification of its own security | ISO/IEC 27001 certificate that expired 4 May 2026, issued by a certifier whose IAS accreditation was cancelled in 2023 | Our verification, 22 October 2026 [^9] |

**Third, the audit gap.** eMudhra's Certifying Authority operation is audited every year by an auditor empanelled by the Controller of Certifying Authorities. The audit criteria state the report is issued "solely for the information and use of the Controller of Certifying Authorities and management" of the CA, "not intended to be... used for any other purposes".[^10] The public has never seen one. IDRBT procures its own CA annual audit through GeM (bid GEM/2023/B/3388421, May 2023), and that outcome is not public either.[^11] So the company whose keys were the numbers 4 through 237 operates under a regime where the only public quality signal is a five-year licence renewal. We could not find a published tender, RFP or award record for the emCA/emRA contract itself, only tenders for the hardware and audits around it. That absence is a fact about public records, not proof of wrongdoing in procurement.

## What we did not find

For the record, because fairness is a discipline and not a mood: we found no evidence that eMudhra's India DSC chain, which roots at CCA's India PKI, was touched by the emSign G3 flaw, which lived in the global browser-trusted hierarchy. We found no evidence of misuse of the compromised keys; as stated above, no one outside a forensic investigation can find such evidence either way. IDRBT's registrar portal was patched after our June 2026 disclosure, and CERT-In acknowledged the report; we have not verified the patch covers all 33-plus endpoints, only that the monitored ones were fixed. We found no indication that RBI or IDRBT has published any statement on the compromise as of 22 October 2026. That silence is itself part of this campaign.

## The track record: what proactive looks like

This campaign sits on two years of proactive audit by this collective, because the model works.

In June 2026 we published the .bank.in registry investigation: 33-plus unauthenticated API endpoints on IDRBT's registrar portal exposing 5,576 bank-employee records, 6,752 bcrypt password hashes, 1,535 invoices worth ₹4.72 crore, and 1,072 orphan super-admin accounts.[^5] We disclosed to CERT-In. It was patched. In the same report we red-teamed the "DSC defence", the claim that physical tokens made the exposure harmless, and documented four unauthenticated DSC-signing endpoints on the portal's eMudhra middleware proxy.[^5]

In October 2026, when the emSign keys broke, we ran the wire before writing the headline: fresh TLS handshakes on all 3,355 live .bank.in HTTPS hosts and CT queries for 3,529 valid certificates. Result: zero certificates from the compromised chains, no direct damage, and a precisely named forward-risk pool if browsers remove eMudhra's remaining roots (Bandhan Bank's retail netbanking is the largest consumer).[^4] We shipped TrustCheck, an Android app that tells any user whether their own phone still trusts the affected chains.[^12] We published an open letter to RBI and MeitY with numbered demands.[^13]

Read-only scans, published evidence, named consequences. No breach required. That is the posture we are asking the state to adopt toward its own trust vendor.

## Why proactive is the only way now

Attackers automate; so must assurance. The G3 flaw was found by an outside researcher, not by the licensed auditor, the certifier, or the regulator. The window in which the weak keys were live was 17.5 months; the window in which the world fixed its browsers was about 72 hours. Machines now audit at the speed the attack runs, which is what this collective's pipeline does, and what a public audit regime would institutionalise. The alternative is learning about the front door from a foreign bug tracker. Who pays when assurance lags: every consumer whose app trusts a chain nobody outside CCA and the CA has examined, with no notification, no advisory, and no recourse.

## The demands

Numbered, verb-led, answerable. Deadline: **14 days, 5 November 2026**. Where an office does not answer, we publish the non-response and pursue the same questions by RTI, whose appeal route ends at the same door.

**To the Controller of Certifying Authorities** (cca@cca.gov.in, info@cca.gov.in):

1. Publish executive summaries of the annual CA audits of eMudhra for FY2024-25 and FY2025-26, redacted only for subscriber data.
2. Commission an incident audit of the emSign G3 compromise covering the 30 April 2025 key ceremony, the "approved deviation" that allowed weak keys, and issuance and HSM access logs, and publish its findings.
3. State whether any misuse of the compromised keys was found, or state plainly that it cannot be ascertained.
4. Publish the empanelment review of SCK Certifications, eMudhra's ISO 27001 certifier, and the CCA position on expired certificates still claimed on vendor websites.

**To IDRBT** (cahelp@idrbt.ac.in):

5. Publish the procurement record for the emCA/emRA platform behind the IDRBT CA: RFP, evaluation, award, and vendor risk assessment.
6. Publish the post-compromise vendor review of eMudhra components in IDRBT CA operations, including any code-lineage relationship between emCA and the affected emSign tooling, and the scope of the January 2026 certificate reissue.

**To the Reserve Bank of India** (supervisory route; public contact dpss@rbi.org.in):

7. Issue a public statement on PKI vendor concentration in banking and advise supervised entities on exposure through emSigner, emBridge and emCA, as RBI's outsourcing circulars already require vendors to be assessable.

**To MeitY** (via CPGRAMS, pgportal.gov.in):

8. Re-examine eSign ESP empanelment conditions to require published audit outcomes, a software bill of materials for emSigner and emBridge, and a public security whitepaper for the emBridge localhost API, whose unauthenticated proxying we documented in June 2026.

## Send a mail: two minutes

Pick a target. The link opens your mail client with the letter filled in. Add your name; send as yourself.

<p class="mailbtn-row">
  <a class="mailbtn" id="btn-cca">Mail CCA</a>
  <a class="mailbtn" id="btn-idrbt">Mail IDRBT</a>
  <a class="mailbtn" id="btn-rbi">Mail RBI</a>
  <a class="mailbtn" id="btn-certin">Mail CERT-In</a>
</p>
<p class="noscript-note">No JavaScript? Copy the letters below into mail to cca@cca.gov.in, cahelp@idrbt.ac.in, dpss@rbi.org.in or incident@cert-in.org.in.</p>

<details>
<summary><b>Letter to CCA</b> (cca@cca.gov.in, info@cca.gov.in)</summary>
<pre>Subject: Demand: publish eMudhra CA audit summaries and G3 incident audit

To the Controller of Certifying Authorities,

eMudhra's emSign programme issued intermediate CA certificates on 30 April 2025 whose private keys had 3-8 bits of entropy; one key value was the number 4. The keys were recoverable by anyone for about 17.5 months before researchers reported them on 17 October 2026. Annual CA audits are submitted to your office but never published.

We ask you, as the licensing authority under the IT Act:
1. Publish executive summaries of eMudhra's annual CA audits for FY2024-25 and FY2025-26.
2. Commission and publish an incident audit of the emSign G3 compromise, including the April 2025 key ceremony and the approved deviation that permitted weak keys.
3. State whether any misuse was found, or state plainly that it cannot be ascertained.
4. Publish your review of SCK Certifications, the certifier whose ISO 27001 certificate for eMudhra expired on 4 May 2026 and whose IAS accreditation was cancelled in 2023.

Please respond by 5 November 2026. Non-responses will be published and pursued by RTI.

Yours sincerely,
[Name]
[Citizen of India]</pre>
</details>

<details>
<summary><b>Letter to IDRBT</b> (cahelp@idrbt.ac.in)</summary>
<pre>Subject: Demand: publish emCA procurement record and post-compromise vendor review

To the Director, IDRBT,

IDRBT's Certifying Authority issues digital certificates for RBI, banks and payment systems, and runs on eMudhra's emCA and emRA platform, as eMudhra's own case study and the praman.idrbtca.org.in/emRASubscriber portal show. On 19 January 2026 the CA cut over to this platform and reissued certificates. In October 2026, eight eMudhra intermediate keys in the emSign programme were found to be weak; one was the number 4.

We ask IDRBT to publish:
1. The procurement record for the emCA/emRA platform: RFP, evaluation, award and vendor risk assessment.
2. Your post-compromise vendor review, including whether any IDRBT CA component shares code lineage with the affected emSign tooling, and the scope and rationale of the January 2026 certificate reissue.

Please respond by 5 November 2026. Non-responses will be published and pursued by RTI.

Yours sincerely,
[Name]</pre>
</details>

<details>
<summary><b>Letter to RBI</b> (dpss@rbi.org.in)</summary>
<pre>Subject: Demand: statement on PKI vendor concentration in banking

To the Reserve Bank of India,

Banking-sector certificate infrastructure is concentrated with one vendor: eMudhra supplies the emCA/emRA platform behind IDRBT's CA, emSigner signing workflows used by banks, and the emBridge middleware on officials' desktops. In October 2026 eight emSign intermediate keys were found recoverable; the incident coordinator states misuse cannot be ruled in or out. RBI's outsourcing circulars require vendors to be assessable; nothing public exists for this vendor.

We ask RBI to:
1. Issue a public statement on PKI vendor concentration in banking.
2. Advise supervised entities on assessing exposure through emSigner, emBridge and emCA, and on notification duties to customers.

Please respond by 5 November 2026.

Yours sincerely,
[Name]</pre>
</details>

<details>
<summary><b>Letter to CERT-In</b> (incident@cert-in.org.in)</summary>
<pre>Subject: Request: public advisory on eMudhra emSign G3 exposure in India

To CERT-In,

The eMudhra emSign intermediate CA key compromise (reported 17 October 2026) affects non-browser clients that do not enforce Certificate Transparency, including Android banking apps. Browsers have blocked the chains; no Indian advisory has been published for Indian users and enterprises.

We request CERT-In to:
1. Publish an advisory naming affected chains and remediation for non-CT clients.
2. State whether any exploitation targeting Indian entities was observed, or that observation is not possible.
3. Confirm coordination with CCA on the incident audit.

Yours sincerely,
[Name]</pre>
</details>

<p><a href="https://pgportal.gov.in" class="mailbtn">MeitY via CPGRAMS</a> — register the grievance with the CCA/MeitY text from the CCA letter above.</p>

## Sources

Everything above is public or marked as our own verification, with dates.

[^1]: emudhra.we-have-a-problem.com (incident tracker: affected intermediates, dates, entropy, coordinator quote)
[^2]: Mozilla bug 2083449; Chrome Root Program statement of 20 October 2026
[^3]: emudhra.com case study PDF (emudhra-case-study-idrbt.pdf); idrbtca.org.in notices observed 22 October 2026; IDRBT CA CPS v4.2.4 (July 2025)
[^4]: Our scans of 22 October 2026: 3,355 live .bank.in HTTPS hosts (TLS handshakes) and 3,529 valid certificates via crt.sh; run directories and evidence at zo.pub/cashlessconsumer/idrbt-open-data and the daily feed github.com/CCAgentOrg/bank-in-domains
[^5]: Our investigation, June 2026: bankin-report.cashlessconsumer.in and the dsc-defense page; evidence archive zo.pub/cashlessconsumer/idrbt-bankin-security
[^6]: CDSL emBridge troubleshooting guide (cdslindia.com); Odisha Treasury emBridge proxy manual
[^7]: cca.gov.in service-providers page, observed 22 October 2026
[^8]: gem.gov.in buyer FAQ, observed 22 October 2026
[^9]: Our threat note of 22 October 2026: the certificate SCK/05/EML/23/91/2406 expired 4 May 2026; IAS cancelled SCK's accreditation MSCB-244 on 17 October 2023
[^10]: CCA, Audit Criteria for Certifying Authorities (CCA-CAAC.pdf): report "solely for the information and use of the Controller... and management"
[^11]: IDRBT, Pre-Bid Queries and Responses, GeM bid GEM/2023/B/3388421, May 2023 (idrbt.ac.in)
[^12]: TrustCheck app: zo.pub/cashlessconsumer/trustcheck; source Projects/trustcheck
[^13]: Open letter to RBI and MeitY, 21 October 2026: cyber.cashlessconsumer.in/pages/emudhra/letter.html

---

**CashlessConsumer** (consumer collective) · cashlessconsumer.in · cashlessconsumerin@gmail.com

Drafted and verified by CashlessConsumer's agentic research pipeline (human-supervised AI on Zo Computer). Scan evidence and run directories are published; this page carries the campaign.
