#!/usr/bin/env python3
"""Generates the static pages for taskrak.com. Run: python3 _src/build.py (from repo root)."""
import os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMAIL = "arcticautonomy@gmail.com"
MAILTO = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'
SUPPORT = "support@taskrak.com"
SUPPORT_MAILTO = f'<a href="mailto:{SUPPORT}">{SUPPORT}</a>'
GOOGLE_PRIVACY = '<a href="https://policies.google.com/privacy" rel="noopener">Google&rsquo;s Privacy Policy</a>'
ADDR = "12110 Business Blvd STE 6 PMB 162, Eagle River, AK 99577, USA"
EFFECTIVE = "October 7, 2026"

NAV = [("privacy", "Privacy"), ("terms", "Terms"), ("guidelines", "Guidelines"), ("delete-account", "Delete account")]

def page(slug, title, desc, body, prefix):
    """prefix: relative path to site root ('' for root, '../' for subfolders, '/' for 404)."""
    nav = "".join(
        f'<a href="{prefix}{s}/"' + (' aria-current="page"' if s == slug else "") + f">{label}</a>"
        for s, label in NAV)
    canon = "https://taskrak.com/" + (f"{slug}" if slug not in ("", "404") else "")
    full_title = f"{title} | Taskr" if slug else "Taskr: local task marketplace"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{'' if slug == '404' else f'<link rel="canonical" href="{canon}">'}
<meta name="theme-color" content="#0E4A46">
<link rel="icon" href="{prefix}favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="{prefix}assets/favicon-32.png">
<link rel="apple-touch-icon" href="{prefix}assets/apple-touch-icon.png">
<link rel="stylesheet" href="{prefix}assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="{prefix or './'}"><img src="{prefix}assets/logo-96.png" alt="" width="40" height="40">Taskr</a>
    <nav class="site-nav" aria-label="Site">{nav}</nav>
  </div>
</header>
<main id="main">
  <div class="wrap">
{body}
  </div>
</main>
<footer class="site-footer">
  <div class="wrap">
    <nav aria-label="Footer"><a href="{prefix}privacy/">Privacy Policy</a><a href="{prefix}terms/">Terms of Service</a><a href="{prefix}guidelines/">Community Guidelines</a><a href="{prefix}delete-account/">Delete your account</a></nav>
    <p>&copy; 2026 Arctic Autonomy Ventures LLC d/b/a Taskr &middot; Alaska, USA</p>
    <p>Help &amp; support: {SUPPORT_MAILTO} &middot; We reply within 24 hours.</p>
  </div>
</footer>
</body>
</html>
"""

def write(slug, html):
    path = os.path.join(ROOT, slug, "index.html") if slug not in ("", "404") else os.path.join(ROOT, "index.html" if slug == "" else "404.html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(html)
    print("wrote", os.path.relpath(path, ROOT))

# ---------------------------------------------------------------- landing
LANDING = f"""
<section class="hero">
  <img src="assets/taskr-icon-512.png" alt="Taskr logo" width="112" height="112">
  <h1>Taskr</h1>
  <p class="lead">A local task marketplace. Post a one-off task near you, or book one and get paid to help a neighbor.</p>
</section>
<div class="card">
  <ul>
    <li><strong>Seekers</strong> post local tasks with photos, a price, and a neighborhood. The street address stays private until the booking is confirmed.</li>
    <li><strong>Taskrs</strong> browse the board or map, request a task, and coordinate in a private booking chat. The Seeker pays to confirm.</li>
    <li>Payments are held securely through Stripe until both sides confirm the job is done. Tips go 100% to the Taskr.</li>
  </ul>
  <p>One account can do both. Taskr is for people 18 and older in the United States.</p>
</div>
<div class="links">
  <a href="privacy/"><strong>Privacy Policy</strong><span>What we collect and how we use it</span></a>
  <a href="terms/"><strong>Terms of Service</strong><span>The rules for using Taskr</span></a>
  <a href="delete-account/"><strong>Delete your account</strong><span>How to delete your Taskr account and data</span></a>
</div>
<p>Need help with a task, a payment, or your account? Email {SUPPORT_MAILTO}. We reply within 24 hours.</p>
<p class="meta">Taskr is operated by Arctic Autonomy Ventures LLC d/b/a Taskr, an Alaska limited liability company.</p>
"""

# ---------------------------------------------------------------- privacy
PRIVACY = f"""
<h1>Taskr Privacy Policy</h1>
<div class="meta">
  <p><strong>Effective date:</strong> {EFFECTIVE}</p>
  <p><strong>Operator:</strong> Arctic Autonomy Ventures LLC d/b/a Taskr ("Taskr," "we," "us"), {ADDR}</p>
  <p><strong>Contact:</strong> {MAILTO}</p>
  <p><strong>Support:</strong> {SUPPORT_MAILTO}</p>
</div>

<p>This policy explains what personal information the Taskr mobile app and service (the "Service") collect, how we use and share it, and the choices you have. Taskr is a marketplace where people ("Seekers") post local one-off tasks and other people ("Taskrs") book and complete them. One account can do both.</p>

<h2>1. Information we collect</h2>
<h3>Account information you provide</h3>
<ul>
  <li><strong>Email address.</strong> We use it to sign you in with one-time codes sent to your email, to send you emails about your bookings, and to reply if you contact us.</li>
  <li><strong>Display name</strong> (shown to other users). If you don't set one, we create one from your email.</li>
  <li><strong>Home ZIP code</strong> (optional), and <strong>skills</strong> you choose to list.</li>
</ul>
<h3>Task, booking, and community content</h3>
<ul>
  <li><strong>Listings:</strong> title, description, labor price or "negotiate," materials mode and budget, <strong>photos you upload</strong> (up to 8 per listing), and the <strong>work address</strong> (street, city, state, ZIP). The public board and map show only a neighborhood-level area (the ZIP-code area) and never your street address. The street address is shown only to the Taskr, after the Seeker pays to confirm the booking.</li>
  <li><strong>Requests and bookings:</strong> requests (including the price a Taskr includes on a negotiable task), the scheduled start time, status (such as awaiting payment, withdrawn, declined, expired, confirmed, completed, released, cancelled, refunded), the price the Seeker paid, platform fee, payout amount, confirmations, cancellations (who cancelled and when), late cancellation fees, &ldquo;Taskr didn&rsquo;t show&rdquo; reports, disputes and the reasons you give, and tips. We use a Taskr&rsquo;s cancellations and no-shows to flag accounts for review.</li>
  <li><strong>Messages</strong> you send in a booking's chat thread.</li>
  <li><strong>Ratings</strong> (1&ndash;5 stars and an optional comment) that you give and receive.</li>
</ul>
<h3>Board search and nearby results</h3>
<ul>
  <li><strong>Board search:</strong> the words you type into Board search are sent to our servers, together with your filters, to find matching tasks.</li>
  <li><strong>ZIP code for nearby results:</strong> the ZIP code used on the board (one you type, your home ZIP, or one filled in from your approximate location) and the search radius are sent to our servers to find tasks near you.</li>
</ul>
<h3>Reports and blocks</h3>
<ul>
  <li><strong>Reports</strong> you file about a listing, photo, message, or user: what you reported (the target), the reason you pick, and any optional details you write.</li>
  <li><strong>Blocks</strong> you set: the list of users you've blocked, so we can hide their content from you.</li>
</ul>
<h3>Location</h3>
<p>If you allow location access, the app uses your device's <strong>approximate location</strong> (not precise GPS location), and only <strong>while you're using the app</strong>, to fill in your board ZIP code and to center the map near you. Taskr asks only for approximate location. The app converts your approximate location to a ZIP code on your device using the phone's built-in geocoder (on Android, provided by Google; see {GOOGLE_PRIVACY}), and that ZIP code is sent to our servers to find nearby tasks. When you browse the map, the map's center point (which can be close to you) is sent to our servers to find nearby tasks. We use it only to answer that request and don't save it. We never collect location in the background. You can deny or revoke location access and enter a ZIP code instead.</p>
<h3>Payments</h3>
<p>Card payments are collected directly by <strong>Stripe</strong> in Stripe's payment sheet. <strong>Taskr never receives or stores your full card number.</strong> Payouts to Taskrs go through <strong>Stripe Connect</strong>: Stripe collects your identity and bank details on its own hosted onboarding pages. We store Stripe reference IDs (for example payment and transfer IDs, and your Connect account ID and status), amounts, and payout status.</p>
<h3>Technical information</h3>
<ul>
  <li>Our servers and hosting provider process technical data needed to run and secure the Service, such as IP address, request times, and error logs. We use rate limits to prevent abuse of sign-in codes.</li>
  <li>Third-party components in the app collect some technical data on their own: the <strong>Google Maps SDK</strong> (device and SDK metadata, IP address, a Maps-specific pseudonymous ID, map interaction events such as panning and zooming, and SDK crash data; see {GOOGLE_PRIVACY}), and the <strong>Stripe SDK</strong> (device characteristics used for fraud prevention during payment). We don't use advertising SDKs or advertising IDs, and we don't add analytics or crash-reporting tools of our own.</li>
</ul>
<p><strong>What we don't collect:</strong> contacts, calendar, SMS or call logs, microphone or camera recordings (the app doesn't access the camera; photos come from your photo library when you choose them), health data, precise (GPS-level) location, or background location.</p>

<h2>2. How we use information</h2>
<ul>
  <li>Create and secure your account, and sign you in with one-time codes sent to your email.</li>
  <li>Run the Service: show nearby tasks and Board search results, let you post, request, pay to confirm, chat, confirm, rate, and tip, show the Seeker a message in the app when a Taskr requests their task, and show the work address to the Taskr after the Seeker pays.</li>
  <li>Process the Seeker&rsquo;s payment when they pay to confirm, hold funds in escrow until both parties confirm the job is done, release payouts 48 hours later unless a dispute is opened (90% of the labor price goes to the Taskr and 10% is Taskr's platform fee; tips go 100% to the Taskr), handle disputes and refunds, issue refunds and late cancellation fees for cancellations and no-shows, and freeze held funds after a chargeback or a ban.</li>
  <li>Prevent fraud, abuse, and security incidents, and enforce our <a href="../terms/">Terms</a> and <a href="../guidelines/">Community Guidelines</a> (including reviewing reports you file, applying blocks you set, and reviewing messages, photos, and confirmations when you open a dispute).</li>
  <li>Email you one-time sign-in codes and messages about your bookings: a new request on your task, a confirmed booking, a chat message you haven't read for a while, a request about to expire, a reminder to confirm the job is done, a dispute, a cancellation, or a refund. Each booking email links back into the app. If your account is banned, we email you the reason and how to appeal.</li>
  <li>Comply with law, taxes, and accounting obligations.</li>
</ul>
<p>We <strong>do not sell</strong> your personal information and do not use it for targeted advertising.</p>

<h2>3. How we share information</h2>
<ul>
  <li><strong>Other users:</strong> your display name, ratings, skills, and your listings (text, photos, neighborhood area) are visible to other Taskr users. Messages are visible to the other person in that booking. The work address is shared with the Taskr after you pay to confirm the booking.</li>
  <li><strong>Service providers</strong> that process data for us under contract:
    <ul>
      <li><strong>Stripe</strong> (payments and payouts, including escrow, Stripe Connect payouts, and fraud prevention). We give Stripe your email and account ID when you set up payouts.</li>
      <li><strong>Resend</strong> (sends sign-in code and booking emails).</li>
      <li><strong>Cloudflare R2</strong> (listing photo storage). Listing photos are served from a public web address so other users can see them.</li>
      <li><strong>Render</strong> (application hosting and database, USA).</li>
      <li><strong>Google Maps</strong> (a service provider we use to show maps and places in the app, through the Google Maps SDK; on Android, the phone's built-in geocoder that turns your approximate location into a ZIP code is also provided by Google). See {GOOGLE_PRIVACY}.</li>
    </ul>
  </li>
  <li><strong>Legal and safety:</strong> when required by law or to protect the rights, safety, and property of users, the public, or Taskr.</li>
  <li><strong>Business transfers:</strong> in connection with a merger, sale, or reorganization, under this policy's protections.</li>
</ul>

<h2>4. Retention</h2>
<p>We keep account data while your account is active. When you delete your account (Section 6), your personal information (including your name, email address, photos, and addresses) is deleted right away and removed from our backups within 30 days, and you can no longer sign in. We keep payment and booking records (for example booking and payment ledgers, typically up to 7 years) with your identity removed, for legal, tax, and fraud-prevention reasons. Bookings you have when you delete are handled under <a href="../terms/">Terms Section 8</a>: a booking where work hasn't started is cancelled and the Seeker gets a full refund; a booking that has started but isn't confirmed stays frozen until support decides it; and a finished, confirmed job is released to the Taskr as usual. <strong>Blocks</strong> you set are deleted with your account. <strong>Reports</strong> you filed are kept with your identity removed, for safety, moderation, and legal reasons, on the same retention terms as other records. Reports other people filed about you may be kept for moderation. Sign-in codes expire after 10 minutes, and any you have are deleted with your account.</p>

<h2>5. Security</h2>
<p>All data between the app and our servers, and between our servers and our providers, is encrypted in transit (HTTPS/TLS). Sign-in codes are stored only as salted hashes. Access to production systems is restricted. No system is 100% secure.</p>

<h2>6. Your choices and rights</h2>
<ul>
  <li><strong>Delete your account:</strong> in the app, go to <strong>Profile &rarr; Delete account</strong>, or email {SUPPORT_MAILTO} from the email address on your account. Deletion always works, even if your account is banned or you have bookings in progress. Section 4 and <a href="../terms/">Terms Section 8</a> explain what happens to your bookings. Blocks you set are deleted with your account; reports you filed are kept with your identity removed (see Section 4). Full instructions, including what is deleted and what is kept, are at <a href="../delete-account/">taskrak.com/delete-account</a>.</li>
  <li><strong>Access or correct:</strong> you can edit your display name, home ZIP, and skills in the app, and unblock users in <strong>Profile</strong>. For other requests, email {SUPPORT_MAILTO}.</li>
  <li><strong>Location:</strong> turn location access off at any time in your device settings.</li>
  <li>Depending on where you live, you may have extra rights (for example access, deletion, correction, portability, or appeal). We'll respond within the time required by law.</li>
</ul>

<h2>7. Children</h2>
<p>Taskr is only for people <strong>18 and older</strong>. We don't knowingly collect information from anyone under 18. If you believe a minor has an account, contact {SUPPORT_MAILTO} and we'll delete it.</p>

<h2>8. Location of processing</h2>
<p>Taskr is offered in the United States and data is processed in the United States.</p>

<h2>9. Changes</h2>
<p>We'll post updates here and change the effective date. If changes are material, we'll notify you in the app.</p>

<h2>10. Contact</h2>
<p>{MAILTO}<br>Arctic Autonomy Ventures LLC d/b/a Taskr<br>12110 Business Blvd STE 6 PMB 162<br>Eagle River, AK 99577, USA</p>
<p>Support: {SUPPORT_MAILTO}</p>
"""

# ---------------------------------------------------------------- terms
TERMS = f"""
<h1>Taskr Terms of Service</h1>
<div class="meta">
  <p><strong>Effective date:</strong> {EFFECTIVE}</p>
  <p><strong>Operator:</strong> Arctic Autonomy Ventures LLC d/b/a <strong>Taskr</strong> (an Alaska limited liability company)</p>
  <p><strong>Contact:</strong> {MAILTO} &middot; 12110 Business Blvd STE 6 PMB 162, Eagle River, AK 99577</p>
  <p><strong>Support:</strong> {SUPPORT_MAILTO}</p>
</div>

<h2>1. Agreement</h2>
<p>By creating an account, accessing, or using the Taskr mobile or web application (the "<strong>Service</strong>"), you agree to these Terms of Service (the "<strong>Terms</strong>") and our <a href="../privacy/">Privacy Policy</a>. If you do not agree, do not use Taskr.</p>
<p>You must be at least <strong>18</strong> years old and able to form a binding contract under applicable U.S. and Alaska law.</p>

<h2>2. What Taskr Is, and How Pricing, Booking, and Payment Work</h2>
<p>Taskr is an online marketplace that connects:</p>
<ul>
  <li><strong>Seekers</strong>: people who post tasks (listings) they need done; and</li>
  <li><strong>Taskrs</strong>: people who request and perform those tasks.</li>
</ul>
<p>Taskr is a platform. It is not the employer, contractor, or agent of Seekers or Taskrs, except as needed to process payments and hold funds in escrow as described in these Terms. Seekers and Taskrs contract with each other for the task. Taskr provides the tools, messaging, and payment processing.</p>
<p><strong>2.1 Price types.</strong> Every listing uses one of two price types:</p>
<ul>
  <li><strong>Fixed price:</strong> the Seeker sets the price. A Taskr can request the task only at that price and can&rsquo;t propose a different one.</li>
  <li><strong>Negotiable:</strong> the Seeker leaves the price open. A Taskr who requests the task includes their price with the request.</li>
</ul>
<p>There is no open bidding. Each request is for one task at one price.</p>
<p><strong>2.2 Requesting a task.</strong> A Taskr requests a task by tapping <strong>Book</strong>. With the request, the Taskr proposes a date and start time for the job. The booking then shows as <strong>awaiting payment</strong>, and the listing is held for that Taskr while the request is pending. The work address stays hidden. We let the Seeker know in the app and by email, and ask them to pay to confirm. Taskrs never pay to book a task. Before requesting a task, a Taskr must finish payout setup with Stripe Connect, because the Seeker&rsquo;s payment goes to the Taskr&rsquo;s payout account.</p>
<p><strong>2.3 The Seeker confirms by paying.</strong> The Seeker always pays for the task. To confirm, the Seeker pays the requested price in the app through Stripe. On a negotiable task, paying the Taskr&rsquo;s price means the Seeker agrees to that price. When payment succeeds:</p>
<ul>
  <li>the booking is confirmed;</li>
  <li>the payment is held in escrow;</li>
  <li>the Taskr&rsquo;s proposed date and start time becomes the booking&rsquo;s scheduled start (Section 2.5); and</li>
  <li>the work address is shared with the Taskr.</li>
</ul>
<p><strong>2.4 Withdrawing, declining, and expiry.</strong> Until the Seeker pays:</p>
<ul>
  <li>the <strong>Taskr</strong> can withdraw the request at any time;</li>
  <li>the <strong>Seeker</strong> can decline the request; and</li>
  <li>if the Seeker doesn&rsquo;t pay within <strong>24 hours</strong>, the request <strong>expires</strong>.</li>
</ul>
<p>In each case, the request ends, no one is charged, and the listing goes back on the board.</p>
<p><strong>2.5 Start time, escrow, and release.</strong> When a Taskr requests a task, they propose a date and start time. When the Seeker pays to confirm (Section 2.3), they accept that time, and it becomes the booking&rsquo;s <strong>scheduled start</strong>. Start times are shown in your local time (Alaska Time for Alaska bookings). The scheduled start can&rsquo;t be changed after payment (Section 8).</p>
<p>The Seeker is charged when they pay, and the payment is held in escrow until the job is confirmed done. When both the Seeker and the Taskr confirm the job is complete, the payment is released <strong>48 hours</strong> later, unless either party opens a dispute during that window. On release, the Taskr receives 90% and Taskr keeps a 10% platform fee (Section 2.6).</p>
<p>If one party confirms the job is complete and the other party doesn&rsquo;t confirm or open a dispute within <strong>48 hours</strong>, the job is treated as confirmed. The 48-hour dispute window then begins, and if no one opens a dispute, the payment is released to the Taskr. If neither party confirms, the payment stays held until Taskr support resolves it.</p>
<p><strong>Disputes.</strong> Either party can open a dispute in the app any time after the Seeker pays, until the payment is released. You don&rsquo;t have to confirm the job is complete first. While a dispute is open, the held payment is not released (Section 7). After the payment is released, a dispute can&rsquo;t be opened in the app. Email {SUPPORT_MAILTO} instead.</p>
<p><strong>Frozen funds.</strong> If a card chargeback is filed on a booking, or a Taskr&rsquo;s account is banned, any held payment that hasn&rsquo;t been released yet is frozen while we review it. When a Taskr is banned, any listing they were booked on goes back on the board as Open, and their open requests are withdrawn.</p>
<p><strong>Banned Seekers.</strong> If a Seeker&rsquo;s account is banned, each of their paid bookings is handled this way:</p>
<ul>
  <li>if the Taskr hasn&rsquo;t marked the job as started, the booking is cancelled and the Seeker gets a <strong>full refund</strong>, with no late fee;</li>
  <li>if the job has started and the Seeker hasn&rsquo;t confirmed it complete (including when only the Taskr has confirmed), the held payment is frozen and Taskr support decides whether to refund the Seeker or release the payment to the Taskr (Section 7); and</li>
  <li>if the Seeker has confirmed the job complete (alone or together with the Taskr), or the job is treated as confirmed under this section, the payment is released to the Taskr as usual.</li>
</ul>
<p>The banned Seeker&rsquo;s listings close.</p>
<p>Cancellations, late cancellations, and no-shows are covered in Section 8. We also email both parties about booking events, such as a new request, a confirmed booking, a cancellation, a refund, or a dispute.</p>
<p><strong>2.6 Payout and platform fee.</strong> When the payment is released, the <strong>Taskr receives 90%</strong> of the task price through Stripe Connect, and Taskr keeps a <strong>10% platform fee</strong>. If a Seeker cancels late, the late cancellation fee is split the same way: 90% to the Taskr and 10% to Taskr (Section 8). To receive payouts, the Taskr must complete Stripe Connect setup. Exact amounts are shown in the app before the Seeker pays.</p>
<p><strong>2.7 Tips.</strong> After the payment is released, the Seeker can choose to tip the Taskr in the app. Tips are paid by the Seeker, go <strong>100% to the Taskr</strong> (Taskr takes no fee on tips), and are optional.</p>
<p>Payments, escrow, payouts, and tips are processed by Stripe and are also covered by Section 5 and Stripe&rsquo;s terms.</p>

<h2>3. Accounts and dual roles</h2>
<ol>
  <li>You must provide accurate information and keep it current.</li>
  <li>You are responsible for activity under your account and for safeguarding login/OTP access.</li>
  <li>One account may act as <strong>both</strong> Seeker and Taskr (<strong>dual-role</strong>), subject to these Terms and any in-app role rules.</li>
  <li>We may suspend or terminate accounts that violate these Terms, applicable law, or our <a href="../guidelines/">Community Guidelines</a>. If we ban your account, we&rsquo;ll email you the reason. You can appeal by writing to {SUPPORT_MAILTO}. You can still delete your account while it is banned. Section 2.5 explains what happens to bookings and held payments after a ban.</li>
  <li>You can delete your account at any time in the app under <strong>Profile &rarr; Delete account</strong>, even if it is banned or you have bookings in progress. Your personal details (your name, email address, photos, and addresses) are deleted right away and removed from our backups within 30 days, and you can&rsquo;t sign in to the account again. Your bookings are handled as described in Section 8, item 9. We keep payment and booking records with your identity removed, for legal, tax, and fraud-prevention reasons. See <a href="../delete-account/">Delete your account</a>.</li>
</ol>

<h2>4. Listings, booking, and address privacy</h2>
<ol>
  <li>Seekers may create listings with task details, a fixed price or a negotiable price (see Section 2), skills/materials notes, and work location.</li>
  <li><strong>Street-level address privacy:</strong> Before a booking is confirmed, public board/map views may show approximate location (for example pins using coordinates) <strong>without</strong> revealing the full street address. Full work address is shared with the Taskr <strong>after</strong> the Seeker pays and the booking is confirmed, as needed to perform the task.</li>
  <li>Taskrs request open listings (see Section 2). A request holds the listing until the Seeker pays, declines, or the request is withdrawn or expires. Taskrs never pay to request a task. Escrow starts when the Seeker pays.</li>
  <li>While another Taskr&rsquo;s request is pending, the listing isn&rsquo;t available. It returns to the board if that request is withdrawn, declined, or expires.</li>
  <li>Seekers may cancel eligible <strong>draft/open</strong> listings per in-app rules before a booking is confirmed. If a request is pending, decline it first. After a booking is confirmed, cancellation and refunds follow Section 8 (including the 24-hour cancellation rule) and our dispute process.</li>
</ol>

<h2>5. Payments, escrow, platform fee, and tips</h2>
<p>Payments are processed by <strong>Stripe</strong> (including Stripe Connect for Taskr payouts). By using paid features you also agree to applicable Stripe terms.</p>
<h3>5.1 Escrow and split (platform fee)</h3>
<ol>
  <li>The Seeker&rsquo;s payment is charged when the Seeker pays to confirm a request (Section 2.3) and is held in <strong>escrow</strong> via Stripe until it is released (Section 5.2) or refunded.</li>
  <li>On release, the task price is split:
    <ul>
      <li><strong>90%</strong> to the Taskr (payout via Stripe Connect); and</li>
      <li>a <strong>10%</strong> platform fee to Arctic Autonomy Ventures LLC d/b/a Taskr.</li>
    </ul>
    Amounts are rounded to the cent and shown in the app before the Seeker pays. If a Seeker cancels late, the late cancellation fee is split the same way: 90% to the Taskr and 10% to Taskr (Section 8).
  </li>
  <li>Exact amounts, timing, and currency are shown in-app. Taxes (if any) are your responsibility unless we state otherwise in writing.</li>
</ol>
<h3>5.2 Dual confirmation and release</h3>
<ol>
  <li>Completion requires <strong>dual confirmation</strong>: the Seeker and the Taskr both confirm the work is done.</li>
  <li>The payment is released <strong>48 hours</strong> after both confirm (or after the job is treated as confirmed under Section 2.5), unless either party opens a dispute during that window (Section 7). Payment isn&rsquo;t released while a dispute is open, or while funds are frozen after a chargeback or a Taskr ban (Section 2.5).</li>
  <li>After release, escrow is paid out per the split above. We may adjust release timing with notice in the app.</li>
</ol>
<h3>5.3 Tips</h3>
<ol>
  <li>After escrow <strong>release</strong>, Seekers may optionally tip the Taskr.</li>
  <li>Tips are paid <strong>100% to the Taskr</strong> (platform fee <strong>0%</strong> on tips), subject to Stripe processing and Taskr Connect payout readiness.</li>
  <li>Tips are voluntary and generally non-refundable once paid, except as required by law or a successful dispute determination.</li>
</ol>
<h3>5.4 Failed or incomplete payouts</h3>
<p>Taskrs must finish Stripe Connect payout setup before requesting a task. If a Taskr&rsquo;s Connect account later can&rsquo;t receive transfers, the Taskr&rsquo;s <strong>payout</strong> may be delayed until onboarding is finished; the Seeker&rsquo;s payment stays in escrow meanwhile. We may show an in-app message asking the Taskr to finish onboarding.</p>

<h2>6. Ratings, messaging, and conduct</h2>
<ol>
  <li>After eligible bookings, users may leave ratings/reviews that must be honest and lawful.</li>
  <li>In-app chat is for coordinating the booked task. Do not harass, spam, or solicit off-platform payments to evade fees.</li>
  <li>You must follow our <a href="../guidelines/">Community Guidelines &amp; Acceptable Use</a>.</li>
</ol>

<h2>7. Disputes between Seekers and Taskrs</h2>
<ol>
  <li>If something goes wrong (quality, incomplete work, payment issues), open a dispute in the app any time after payment, until the payment is released. After the payment is released, email {SUPPORT_MAILTO} instead. For a Taskr no-show, use <strong>Taskr didn&rsquo;t show</strong> (Section 8, item 7).</li>
  <li>Taskr support reviews each dispute. We may look at evidence (messages, photos, confirmations) and then either refund the Seeker or release the payment to the Taskr. We may also limit accounts or take other steps allowed by these Terms. To reach support, email {SUPPORT_MAILTO}.</li>
  <li>Our decision on platform escrow disputes is final as between you and the platform for escrow disposition, without limiting your rights against the other party under law.</li>
  <li>Opening multiple disputes on the same matter may be rejected as already disputed/resolved.</li>
</ol>

<h2>8. Cancellations and refunds</h2>
<ol>
  <li><strong>Before a request:</strong> Seekers may cancel eligible open/draft listings per in-app rules.</li>
  <li><strong>Pending requests (awaiting payment):</strong> a Taskr can withdraw and a Seeker can decline a request before payment, and unpaid requests expire after <strong>24 hours</strong>. No one is charged and the listing reopens.</li>
  <li><strong>Seeker cancels 24 hours or more before the scheduled start:</strong> the Seeker gets a <strong>full refund</strong>. <strong>1-hour grace period:</strong> a Seeker who cancels within <strong>1 hour</strong> of paying also gets a <strong>full refund</strong>, with no late fee, as long as the scheduled start hasn&rsquo;t passed. This applies even if the start is less than 24 hours away. The listing then closes.</li>
  <li><strong>Seeker cancels less than 24 hours before the scheduled start:</strong> unless the 1-hour grace period in item 3 applies, the Seeker is refunded the price minus a <strong>late cancellation fee</strong> of <strong>20% of the price, up to $25</strong>. The Taskr receives 90% of the late fee, and Taskr keeps 10%. The Taskr&rsquo;s share is released <strong>48 hours</strong> after the cancellation, unless either party opens a dispute during that window. For example, on a $60 task the late fee is $12: the Seeker gets $48 back and the Taskr receives $10.80. On a $200 task the fee is capped at $25: the Seeker gets $175 back and the Taskr receives $22.50. The listing then closes.</li>
  <li><strong>After the scheduled start:</strong> the Seeker can no longer cancel. If something goes wrong, open a dispute (Section 7), or use <strong>Taskr didn&rsquo;t show</strong> if item 7 applies.</li>
  <li><strong>Taskr cancels:</strong> if the Taskr cancels a booking at any time, the Seeker gets a <strong>full refund</strong>, with no late fee. The listing goes back on the board as Open automatically. If a Taskr cancels 3 bookings within 30 days, their account is flagged for review. A no-show (item 7) counts as a cancellation for this purpose. If the Seeker asked the Taskr in the booking chat to cancel, Taskr support can clear that cancellation so it doesn&rsquo;t count. To ask, email {SUPPORT_MAILTO}.</li>
  <li><strong>Taskr no-show:</strong> if the Taskr hasn&rsquo;t marked the job as started <strong>2 hours</strong> after the scheduled start, a <strong>Taskr didn&rsquo;t show</strong> button appears for the Seeker in the app. It stays until the Taskr marks the job as started. If the Seeker taps it, the booking is cancelled and the Seeker gets an instant <strong>full refund</strong>, with no late fee. The listing goes back on the board as Open automatically. The refund stands even if the Taskr marks the job as started afterward. If the Taskr marks the job as started before the Seeker taps the button, the button goes away, and the Seeker can still open a dispute (Section 7).</li>
  <li><strong>Changing the time:</strong> the scheduled start can&rsquo;t be changed after payment. To change it, either party cancels under the rules above. If the Taskr cancels, the listing goes back on the board and the Taskr can request it again with the new time. If the Seeker cancels, the listing closes, and the Seeker posts the task again.</li>
  <li><strong>Account deletion:</strong> if the Seeker or the Taskr deletes their account, each of their paid bookings is handled this way:
    <ul>
      <li>if the Taskr hasn&rsquo;t marked the job as started, the booking is cancelled and the Seeker gets a <strong>full refund</strong>, with no late fee, no matter which side deleted;</li>
      <li>if the job has started but isn&rsquo;t confirmed complete, the held payment stays frozen until Taskr support decides whether to refund the Seeker or release the payment to the Taskr (Section 7); and</li>
      <li>if the job is confirmed complete, or treated as confirmed, the payment is released to the Taskr as usual. Payouts go to the Taskr&rsquo;s own Stripe account, which the Taskr can still reach through Stripe after deleting their Taskr account.</li>
    </ul>
    If the Seeker deletes their account, their listings close. If the Taskr deletes their account, any listing they were booked on goes back on the board as Open.
  </li>
  <li><strong>Banned accounts:</strong> if an account is banned, its bookings and held payments are handled as described in Section 2.5.</li>
  <li><strong>Disputes:</strong> in any other case, whether you get a refund depends on the outcome of the dispute (Section 7).</li>
  <li><strong>Chargebacks:</strong> if a card chargeback is filed, any held payment that hasn&rsquo;t been released yet is frozen while we review it. Chargebacks filed in bad faith may lead to account suspension.</li>
</ol>
<p>Card refunds may take 5&ndash;10 business days to appear on your statement.</p>

<h2>9. Independent contractors; no employment</h2>
<p>Taskrs are independent contractors (or otherwise self-employed) relative to Seekers and to Taskr, unless a written agreement says otherwise. Nothing in these Terms creates an employment, partnership, or joint-venture relationship. Taskrs are responsible for their own tools, licenses, insurance, and taxes as required by law (including Alaska local requirements where applicable).</p>

<h2>10. Prohibited uses</h2>
<p>You may not use Taskr to:</p>
<ul>
  <li>violate law (including safety, licensing, discrimination, or fraud laws);</li>
  <li>post illegal, dangerous, or deceptive tasks;</li>
  <li>scrape, reverse engineer, or abuse the Service;</li>
  <li>evade escrow/fees via off-app payment for Taskr-originated tasks;</li>
  <li>share another person&rsquo;s private address or personal data without authorization;</li>
  <li>interfere with payments, ratings, or disputes in bad faith.</li>
</ul>

<h2>11. Intellectual property</h2>
<p>Taskr, its branding, and software are owned by Arctic Autonomy Ventures LLC or its licensors. You retain rights to content you post, and grant us a worldwide, non-exclusive license to host, display, and use that content to operate and improve the Service.</p>

<h2>12. Disclaimers</h2>
<p>THE SERVICE IS PROVIDED <strong>"AS IS"</strong> AND <strong>"AS AVAILABLE."</strong> TO THE MAXIMUM EXTENT PERMITTED BY LAW, WE DISCLAIM WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NON-INFRINGEMENT. We do not guarantee that every Seeker or Taskr is reliable, skilled, or insured, or that every task will be completed satisfactorily.</p>

<h2>13. Limitation of liability</h2>
<p>TO THE MAXIMUM EXTENT PERMITTED BY LAW, ARCTIC AUTONOMY VENTURES LLC AND ITS AFFILIATES WILL NOT BE LIABLE FOR INDIRECT, INCIDENTAL, SPECIAL, CONSEQUENTIAL, OR PUNITIVE DAMAGES, OR FOR LOST PROFITS, DATA, OR GOODWILL. OUR TOTAL LIABILITY FOR CLAIMS RELATING TO THE SERVICE WILL NOT EXCEED THE GREATER OF (A) AMOUNTS YOU PAID TO US IN PLATFORM FEES IN THE <strong>12 MONTHS</strong> BEFORE THE CLAIM OR (B) <strong>$100</strong>.</p>
<p>Some jurisdictions (including consumer protections) do not allow certain limits; in those cases our liability is limited to the fullest extent allowed.</p>

<h2>14. Indemnity</h2>
<p>You will defend and indemnify Arctic Autonomy Ventures LLC against claims arising from your content, tasks, performance or non-performance of work, misuse of the Service, or violation of these Terms or law&mdash;except to the extent caused by our willful misconduct.</p>

<h2>15. Governing law and venue</h2>
<p>These Terms are governed by the laws of the <strong>State of Alaska</strong>, excluding conflict-of-law rules. Courts located in the <strong>Municipality of Anchorage</strong>, Alaska, will have exclusive jurisdiction, unless applicable law requires otherwise.</p>

<h2>16. Changes</h2>
<p>We may update these Terms by posting a new version with an updated effective date. Continued use after the effective date means you accept the changes. Material changes may also be announced in the app.</p>

<h2>17. Contact</h2>
<p>Questions about these Terms: {MAILTO} &middot; Arctic Autonomy Ventures LLC, 12110 Business Blvd STE 6 PMB 162, Eagle River, AK 99577.</p>
<p>For help with a task, a payment, a dispute, or your account, email {SUPPORT_MAILTO}.</p>
"""

# ---------------------------------------------------------------- guidelines
GUIDELINES = f"""
<h1>Community Guidelines &amp; Acceptable Use</h1>
<div class="meta">
  <p><strong>Effective date:</strong> {EFFECTIVE}</p>
  <p><strong>Operator:</strong> Arctic Autonomy Ventures LLC d/b/a <strong>Taskr</strong></p>
</div>
<p>These guidelines are part of the <a href="../terms/">Taskr Terms of Service</a>.</p>

<h2>Be a good neighbor</h2>
<p>Taskr is for real local help at a clear price: a fixed price set by the Seeker, or, on a negotiable task, the price a Taskr includes with their request, which the Seeker accepts by paying. Treat people the way you&rsquo;d want to be treated on a task in your own community (including across Alaska&rsquo;s towns and cities).</p>
<p>You must be <strong>18+</strong> to use Taskr.</p>

<h2>Do</h2>
<ul>
  <li>Post accurate listings and show up on time. If you need to cancel, follow the rules in <a href="../terms/">Terms Section 8</a>. Taskrs who cancel or don&rsquo;t show up for 3 bookings within 30 days are flagged for review.</li>
  <li>Keep chat focused on the task.</li>
  <li>Protect privacy: don&rsquo;t share someone&rsquo;s full address or personal info beyond what&rsquo;s needed.</li>
  <li>Use escrow and in-app payments for Taskr tasks.</li>
  <li>Leave honest ratings after eligible tasks.</li>
</ul>

<h2>Don&rsquo;t</h2>
<ul>
  <li>Harass, threaten, discriminate, or scam anyone.</li>
  <li>Post illegal, unsafe, or deceptive tasks.</li>
  <li>Post sexual, nude, or explicit content.</li>
  <li>Move payment off-app to dodge fees, or fake confirmations/tips/disputes.</li>
  <li>Spam, scrape, or abuse sign-in codes, messaging, or reports.</li>
  <li>Upload others&rsquo; private photos or documents without permission.</li>
</ul>

<h2>Enforcement</h2>
<p>We may warn, limit features, suspend, or ban accounts that break these guidelines, our Terms, or the law. Serious safety or fraud issues may be reported to authorities. If you&rsquo;re banned, we&rsquo;ll email you the reason, and you can appeal at {SUPPORT_MAILTO}.</p>
<p>Questions: {SUPPORT_MAILTO}</p>
"""

# ---------------------------------------------------------------- delete account
DELETE = f"""
<h1>Delete your Taskr account</h1>
<p class="meta">This page explains how to delete your account in the <strong>Taskr</strong> app, developed by <strong>Arctic Autonomy Ventures LLC</strong>, and what happens to your data.</p>

<h2>Option 1: Delete in the app</h2>
<div class="card">
<ol>
  <li>Open the Taskr app and sign in.</li>
  <li>Go to <strong>Profile</strong>.</li>
  <li>Tap <strong>Delete account</strong>.</li>
  <li>Review what will be deleted and what will be kept, then confirm. You may be asked to enter a one-time code sent to your email to confirm it's you.</li>
</ol>
<p>You'll be signed out and won't be able to sign in to the deleted account again.</p>
</div>

<h2>Option 2: Request deletion by email</h2>
<div class="card">
<p>If you can't use the app, email <a href="mailto:{SUPPORT}?subject=Delete%20my%20Taskr%20account">{SUPPORT}</a>:</p>
<ul>
  <li>Send it <strong>from the email address on your Taskr account</strong>, so we can confirm the request is yours.</li>
  <li>Use the subject line <strong>"Delete my Taskr account"</strong>.</li>
</ul>
<p>We may reply to confirm before we delete anything. We won't ask for your card number or password.</p>
</div>

<div class="card callout">
<p><strong>You can always delete your account</strong>, even if it is banned or you have bookings in progress. Here's what happens to your bookings when you delete (see <a href="../terms/">Terms Section 8</a>):</p>
<ul>
  <li><strong>Work hasn't started:</strong> the booking is cancelled and the Seeker gets a full refund, with no late fee, no matter which side deleted.</li>
  <li><strong>Work has started but isn't confirmed:</strong> the payment stays frozen until Taskr support decides whether to refund the Seeker or release the payment to the Taskr.</li>
  <li><strong>Finished and confirmed:</strong> the payment is released to the Taskr as usual.</li>
</ul>
<p>Requests still waiting for payment end, and no one is charged. If you're a Seeker, your listings close. If you're a Taskr, any listing you were booked on goes back on the board as Open.</p>
</div>

<h2>What we delete</h2>
<p>These are deleted right away when you delete your account, and removed from our backups within 30 days:</p>
<ul>
  <li>Your display name, email address, home ZIP code, and listed skills. Your profile is replaced with "Deleted user."</li>
  <li>Your photos, and the addresses on your tasks.</li>
  <li>Your draft and open listings, which are cancelled.</li>
  <li>Blocks you set.</li>
  <li>Your ability to sign in, and your sign-in codes (which expire after 10 minutes anyway). You can't sign in to a deleted account again.</li>
</ul>
<p>If you set up payouts, your identity and bank details are held by Stripe, not Taskr. Payouts for finished jobs still go to your own Stripe account, and you can still reach that account through Stripe after you delete your Taskr account. Stripe keeps its own records of your Connect account under <a href="https://stripe.com/privacy" rel="noopener">Stripe's privacy policy</a>.</p>

<h2>What we keep, and for how long</h2>
<ul>
  <li><strong>Booking, payment, and dispute records</strong> (for example amounts, platform fees, payouts, tips, refunds, cancellations, confirmations, and dispute outcomes), which we must keep for legal, tax, accounting, fraud-prevention, and dispute purposes. We keep these for <strong>up to 7 years</strong>, with your identity removed.</li>
  <li>Ratings and booking chat messages that are part of those records may stay attached to the booking, shown as from "Deleted user."</li>
  <li><strong>Reports you filed</strong>, kept with your identity removed for safety, moderation, and legal reasons, on the same retention terms as the records above. Reports other people filed about you may be kept for moderation.</li>
  <li>Information we must keep to comply with a legal obligation or to resolve an open legal claim, only for as long as that requires.</li>
</ul>

<h2>Timeline</h2>
<p>Your personal details are deleted right away when you delete your account, and removed from our backups within <strong>30 days</strong>. Booking and payment records are kept with your identity removed, and are deleted at the end of their retention period (up to 7 years).</p>

<h2>Delete some data without deleting your account</h2>
<ul>
  <li>Edit or clear your display name, home ZIP, and skills in <strong>Profile</strong>.</li>
  <li>Unblock users in <strong>Profile</strong>.</li>
  <li>Cancel your draft or open listings in the app to remove them and their photos.</li>
  <li>Turn off location access in your device settings at any time.</li>
  <li>For anything else, email {SUPPORT_MAILTO} from your account email.</li>
</ul>

<p>See our <a href="../privacy/">Privacy Policy</a> for more on how Taskr handles your data.</p>
"""

NOT_FOUND = """
<h1>Page not found</h1>
<p>Sorry, we couldn't find that page.</p>
<div class="links">
  <a href="/"><strong>Home</strong><span>About Taskr</span></a>
  <a href="/privacy/"><strong>Privacy Policy</strong><span>What we collect and why</span></a>
  <a href="/terms/"><strong>Terms of Service</strong><span>The rules for using Taskr</span></a>
  <a href="/delete-account/"><strong>Delete your account</strong><span>How to delete your account</span></a>
</div>
"""

write("", page("", "Taskr", "Taskr is a local task marketplace: post a one-off task near you, or book one and get paid to help a neighbor.", LANDING, ""))
write("privacy", page("privacy", "Privacy Policy", "Taskr Privacy Policy: what the Taskr app collects, how we use and share it, and your choices.", PRIVACY, "../"))
write("terms", page("terms", "Terms of Service", "Taskr Terms of Service.", TERMS, "../"))
write("guidelines", page("guidelines", "Community Guidelines", "Taskr Community Guidelines and Acceptable Use.", GUIDELINES, "../"))
write("delete-account", page("delete-account", "Delete your account", "How to delete your Taskr account and what happens to your data.", DELETE, "../"))
write("404", page("404", "Page not found", "Page not found.", NOT_FOUND, "/"))
