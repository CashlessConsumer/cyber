#!/usr/bin/env python3
"""Assemble statement.html, letter.html, company.html and campaign.html."""
import pathlib
from urllib.parse import quote

ROOT = pathlib.Path(__file__).parent

NAV5 = """      <a href="index.html#consumers">For consumers</a>
      <a href="statement.html">Statement</a>
      <a href="letter.html">Open letter</a>
      <a href="index.html#videos">Videos</a>
      <a href="index.html#sources">Sources</a>"""

NAV6 = """      <a href="index.html#consumers">For consumers</a>
      <a href="statement.html">Statement</a>
      <a href="letter.html">Open letter</a>
      <a href="company.html">The company</a>
      <a href="index.html#videos">Videos</a>
      <a href="index.html#sources">Sources</a>"""

NAV7 = """      <a href="index.html#consumers">For consumers</a>
      <a href="statement.html">Statement</a>
      <a href="letter.html">Open letter</a>
      <a href="company.html">The company</a>
      <a href="campaign.html">Campaign</a>
      <a href="index.html#sources">Sources</a>"""

def mailto(to, cc="", subject="", body=""):
    q = f"mailto:{to}?subject={quote(subject)}"
    if cc:
        q += f"&cc={quote(cc)}"
    if body:
        q += f"&body={quote(body)}"
    return q

CCA_S = "Demand: publish eMudhra CA audit summaries and G3 incident audit"
CCA_B = ("To the Controller of Certifying Authorities,\n\n"
    "eMudhra's emSign programme issued intermediate CA certificates on 30 April 2025 whose private keys had 3-8 bits of entropy; one key value was the number 4. The keys were recoverable by anyone for about 17.5 months before researchers reported them on 17 October 2026. Annual CA audits are submitted to your office but never published.\n\n"
    "We ask you, as the licensing authority under the IT Act:\n"
    "1. Publish executive summaries of eMudhra's annual CA audits for FY2024-25 and FY2025-26.\n"
    "2. Commission and publish an incident audit of the emSign G3 compromise, including the April 2025 key ceremony and the approved deviation that permitted weak keys.\n"
    "3. State whether any misuse was found, or state plainly that it cannot be ascertained.\n"
    "4. Publish your review of SCK Certifications, the certifier whose ISO 27001 certificate for eMudhra expired on 4 May 2026 and whose IAS accreditation was cancelled in 2023.\n\n"
    "Please respond by 5 November 2026. Non-responses will be published and pursued by RTI.\n\n"
    "Yours sincerely,\n[Name]\n[Citizen of India]")
IDRBT_S = "Demand: publish emCA procurement record and post-compromise vendor review"
IDRBT_B = ("To the Director, IDRBT,\n\n"
    "IDRBT's Certifying Authority issues digital certificates for RBI, banks and payment systems, and runs on eMudhra's emCA and emRA platform, as eMudhra's own case study and the praman.idrbtca.org.in/emRASubscriber portal show. On 19 January 2026 the CA cut over to this platform and reissued certificates. In October 2026, eight eMudhra intermediate keys in the emSign programme were found to be weak; one was the number 4.\n\n"
    "We ask IDRBT to publish:\n"
    "1. The procurement record for the emCA/emRA platform: RFP, evaluation, award and vendor risk assessment.\n"
    "2. Your post-compromise vendor review, including whether any IDRBT CA component shares code lineage with the affected emSign tooling, and the scope and rationale of the January 2026 certificate reissue.\n\n"
    "Please respond by 5 November 2026. Non-responses will be published and pursued by RTI.\n\n"
    "Yours sincerely,\n[Name]")
RBI_S = "Demand: statement on PKI vendor concentration in banking"
RBI_B = ("To the Reserve Bank of India,\n\n"
    "Banking-sector certificate infrastructure is concentrated with one vendor: eMudhra supplies the emCA/emRA platform behind IDRBT's CA, emSigner signing workflows used by banks, and the emBridge middleware on officials' desktops. In October 2026 eight emSign intermediate keys were found recoverable; the incident coordinator states misuse cannot be ruled in or out. RBI's outsourcing circulars require vendors to be assessable; nothing public exists for this vendor.\n\n"
    "We ask RBI to:\n"
    "1. Issue a public statement on PKI vendor concentration in banking.\n"
    "2. Advise supervised entities on assessing exposure through emSigner, emBridge and emCA, and on notification duties to customers.\n\n"
    "Please respond by 5 November 2026.\n\n"
    "Yours sincerely,\n[Name]")
CERTIN_S = "Request: public advisory on eMudhra emSign G3 exposure in India"
CERTIN_B = ("To CERT-In,\n\n"
    "The eMudhra emSign intermediate CA key compromise (reported 17 October 2026) affects non-browser clients that do not enforce Certificate Transparency, including Android banking apps. Browsers have blocked the chains; no Indian advisory has been published for Indian users and enterprises.\n\n"
    "We request CERT-In to:\n"
    "1. Publish an advisory naming affected chains and remediation for non-CT clients.\n"
    "2. State whether any exploitation targeting Indian entities was observed, or that observation is not possible.\n"
    "3. Confirm coordination with CCA on the incident audit.\n\n"
    "Yours sincerely,\n[Name]")

MAIL_BUTTONS = f"""<p class="mailbtn-row">
  <a class="mailbtn" href="{mailto('cca@cca.gov.in','info@cca.gov.in',CCA_S,CCA_B)}">Mail CCA</a>
  <a class="mailbtn" href="{mailto('cahelp@idrbt.ac.in','',IDRBT_S,IDRBT_B)}">Mail IDRBT</a>
  <a class="mailbtn" href="{mailto('dpss@rbi.org.in','',RBI_S,RBI_B)}">Mail RBI</a>
  <a class="mailbtn" href="{mailto('incident@cert-in.org.in','',CERTIN_S,CERTIN_B)}">Mail CERT-In</a>
</p>"""

CAMPAIGN_CSS = """
<style>
.mailbtn-row { display:flex; flex-wrap:wrap; gap:12px; margin:22px 0 10px; }
.mailbtn { display:inline-block; background:#f0b429; color:#101418; font-weight:700; font-size:15px;
  padding:12px 22px; border-radius:8px; text-decoration:none; letter-spacing:.2px; }
.mailbtn:hover { background:#ffd166; }
.noscript-note { font-size:13.5px; color:#5a6a7a; }
.toplink { float:right; font-size:13px; }
div.footnotes { border-top:1px solid #d8dee6; margin-top:34px; padding-top:6px; font-size:14px; }
</style>
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — eMudhra CA Compromise — CashlessConsumer</title>
<meta name="description" content="{desc}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="hub-crumb"><a href="../../index.html">&#9670; cyber.cashlessconsumer.in</a><span class="sep">/</span>eMudhra CA compromise</div>
<header class="site-header">
  <div class="wrap-wide">
    <a class="brand" href="index.html">
      <span class="brand-badge">CC</span>
      <span class="brand-name">CashlessConsumer</span>
    </a>
    <nav class="site-nav">
{nav}
    </nav>
  </div>
</header>
<main>
  <section class="hero" style="padding:44px 0 40px;">
    <div class="wrap">
      <div class="hero-kicker">eMudhra CA compromise · 21 October 2026</div>
      <h1 style="font-size:clamp(24px,4vw,34px);">{h1}</h1>
    </div>
  </section>
  <section>
    <div class="wrap">
      <div class="banner-note">Draft for review, 21 October 2026. Numbers and quotes are sourced in the footnotes; what we verified ourselves is marked as our own verification.</div>
      <div class="prose">
{body}
      </div>
      <div class="callout">
        <h3>Related on this site</h3>
        <p><a href="index.html#consumers">What this means for consumers</a> · <a href="index.html#videos">Videos that explain the mechanics</a> · <a href="index.html#sources">Every source</a> · <a href="../../index.html">More security research at cyber.cashlessconsumer.in</a></p>
      </div>
    </div>
  </section>
</main>
<footer class="site-footer">
  <div class="wrap-wide">
    <div>CashlessConsumer · an Indian consumer collective for digital payments and public digital infrastructure.</div>
    <div><a href="https://cashlessconsumer.in">cashlessconsumer.in</a> · <a href="mailto:cashlessconsumerin@gmail.com">cashlessconsumerin@gmail.com</a></div>
  </div>
</footer>
</body>
</html>
"""

def body_text(path):
    t = pathlib.Path(path).read_text()
    # drop the markdown-draft banner line that pandoc carried over (first <p><strong>Draft...)
    return t

_missing = []
for name in ("statement", "letter", "company"):
    src = pathlib.Path(f"/tmp/{name}-body.html")
    if src.exists():
        globals()[name] = body_text(src)
    else:
        _missing.append(name)

if "statement" not in _missing:
    (ROOT / "statement.html").write_text(TEMPLATE.format(
        title="Public statement",
    desc="CashlessConsumer public statement on the eMudhra CA compromise: eight intermediate certificates with guessable private keys, and no word from Indian regulators.",
    h1="Public statement: eight &ldquo;secret&rdquo; keys anyone could guess. One was the number 4. And no Indian authority has said a word.",
    body=statement,
    nav=NAV5,
))

if "letter" not in _missing:
    (ROOT / "letter.html").write_text(TEMPLATE.format(
    title="Open letter to RBI and MeitY",
    desc="CashlessConsumer open letter to the Reserve Bank of India and MeitY on the eMudhra CA compromise and the silence of Indian trust-infrastructure supervision.",
    h1="Open letter to the Reserve Bank of India and the Ministry of Electronics and Information Technology",
    body=letter,
    nav=NAV5,
))

if "company" not in _missing:
    (ROOT / "company.html").write_text(TEMPLATE.format(
    title="The company behind the keys",
    desc="Who is eMudhra? A consumer-side corporate history: people, licence, business lines, listing, acquisitions, and what the October 2026 key compromise means for the trust it sells.",
    h1="The company behind the keys: a consumer history of eMudhra",
    body=company,
    nav=NAV6,
))

campaign = body_text("/tmp/campaign-body.html").replace(
    '<p class="mailbtn-row">\n  <a class="mailbtn" id="btn-cca">Mail CCA</a>\n  <a class="mailbtn" id="btn-idrbt">Mail IDRBT</a>\n  <a class="mailbtn" id="btn-rbi">Mail RBI</a>\n  <a class="mailbtn" id="btn-certin">Mail CERT-In</a>\n</p>',
    MAIL_BUTTONS)

(ROOT / "campaign.html").write_text(TEMPLATE.format(
    title="Campaign: open the books on eMudhra",
    desc="CashlessConsumer public-audit campaign: transparent public audit of eMudhra's role in Indian banking and government trust infrastructure. Evidence, demands, and a two-minute mail action.",
    h1="Open the books on eMudhra: a public audit campaign",
    body=campaign,
    nav=NAV7,
).replace("</head>", CAMPAIGN_CSS + "\n</head>").replace(
    'Draft for review, 21 October 2026. Numbers and quotes are sourced in the footnotes; what we verified ourselves is marked as our own verification.',
    'Live campaign, launched 23 October 2026. Numbers and quotes are sourced in the footnotes; what we verified ourselves is marked as our own verification.'))

print("wrote statement.html + letter.html + company.html + campaign.html")
