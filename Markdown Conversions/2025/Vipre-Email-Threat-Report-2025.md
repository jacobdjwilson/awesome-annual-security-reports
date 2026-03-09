# Email Threat Trends Report: 2025:Q2

## Table of Contents
- [Executive Introduction](#executive-introduction)
- [5 Biggest Takeaways From Q2 2025](#5-biggest-takeaways-from-q2-2025)
- [New Trends in the Anatomy of an Attack: From Start to Finish](#new-trends-in-the-anatomy-of-an-attack-from-start-to-finish)
- [Feature: Attackers Use Legit Login Pages to Throw Us Off the Trail](#feature-attackers-use-legit-login-pages-to-throw-us-off-the-trail)
- [Feature: Malicious Emails Spike Worldwide in June](#feature-malicious-emails-spike-worldwide-in-june)
- [Concluding Thoughts: Personalization Is Public Enemy #1 in Phishing](#concluding-thoughts-personalization-is-public-enemy-1-in-phishing)

---

## Executive Introduction

We have seen it coming for a while. And now it’s crystal clear. The trend towards human-centered attacks is established, and we are seeing the data to prove it.

Attackers are very much favoring social engineering schemes as their tactics evolve, using technology to deceive us rather than dupe our technological defenses.

From diversified forms of phishing to mining the ever-giving BEC cash cow, adversaries are just getting started when it comes to using technology in new and human-proof ways. Employees are faced with a difficult choice every time they open their inbox – to click or not to click – and hold the well-being of their organizations at the tips of their fingers.

It is important to define these human-centric trends so that organizations know which way to invest and how to adjust their strategy. There may be a lot of hype in the news about sophisticated new forms of attack, advanced ransomware, and more. But when we look at the vast majority of threats and how they are getting in, the smart money says invest in what will give you the biggest bang for your buck. In other words, categorize the risks, and prioritize accordingly.

Right now, those are email-centered attacks, and specifically ones that slide past traditional signature-based defenses with apparent ease. You can’t train your employees enough to keep up with AI-based dupes at scale. But by understanding the types of social engineering scams out there, you can know where to act next and with what solutions.

Every quarter, VIPRE sounds the alarm with data-driven anomalies we see in our customer landscape. With over 25 years of experience and insights gained from round-the-clock detection worldwide, we make it our mission to share with the community what we’ve found. And once again, the VIPRE Email Threat Trends Report is published to inform global cybersecurity professionals of the trends, techniques, and attacks only someone with our vantage point can see.

We encourage you to review this report and take the action you see fit.

---

## 5 Biggest Takeaways From Q2 2025

We track trends to see where attackers are heading. Our Q2 2025 data leads us to emphasize some significant happenings that represent a departure from this time last year and even last quarter. And, just as interesting, certain pieces that refuse to move.

### 1. Manufacturing and Retail – Still Top Targets for the Second Year in a Row

Last year in Q1, Manufacturing overtook Finance in an upset no one saw coming. Unfortunately for the world’s manufacturers, they have stayed in the lead ever since. The trend continues to this day, six consecutive quarters later.

Last year, attacks against Manufacturing increased by a staggering 71%. This year, our data show that the Manufacturing sector suffered the most email attacks in Q2 (26%) across a range of vectors, including BEC, phishing, and malspam – you name it. Close behind (as in last year and the last quarter) was Retail (20%), followed by Healthcare (19%).

The fact that Manufacturing received the highest number of email-based attacks aligns perfectly with its current landslide of cyberattacks in general. When we look at the latest Verizon 2025 Data Breach Investigations Report, we note that phishing was the initial access vector in 16% of all cases; credential theft came in with the most at 22% with vulnerability exploitation taking second at 20%.

![Chart showing Email Attack Breakdown: Credential Theft 22%, Vulnerability Exploitation 20%, Phishing Emails 16%]

This would indicate that phishing is a significant, but not the largest, issue. However, when you consider that phishing is a major factor in threat actors obtaining stolen credentials in the first place, you see how much of a problem it really is. By tamping down on email-based threats, the manufacturing sector could drastically reduce its number of cyber compromises overall.

### 2. Phishing Kits are Out. Customized Deployments are In

For digital “ages,” phishing kits have been a powerful way to propagate malicious campaigns at scale. This quarter, it’s no surprise that we continue to see them, underpinning a substantial number of phishing sites.

*   Evilginx (20%)
*   Tycoon 2FA (10%)
*   16shop (7%)
*   Other generic kits (5%)

However, what was surprising was that more than half (58%) of the phishing sites we analyzed this quarter did not use identifiable phishing kits. Indicating a trend towards custom-made or obfuscated deployments, this shift is something we anticipate seeing more of in the future.

Phishing-as-a-Service tools have their pros and cons; while a great way for low-level hackers to launch spray-and-pray campaigns at low cost, they are also established pieces of software that can be reverse-engineered, tracked, and caught. A bespoke phishing deployment doesn’t run the same risks, and thanks to AI, even those are affordable, too.

### 3. Call Me Maybe: Callback Phishing

Callback phishing scams are a dark horse that first appeared in our crosshairs only last quarter. Sighted in the wild since 2021, callback scams had yet to make our “list” of top phishing vectors. In Q1 2025, that changed, with this once-obscure method rising to take responsibility for 16% of phishing attacks overall.

This quarter, the trend continues. Callback scams keep their spot as the third most prevalent phishing type in Q2 2025. For the uninitiated, callback scams “[are] a social engineering attack that tricks the recipient into calling a phone number included in a deceptive email,” to quote our last report. Also referred to as TOAD attacks (“telephone-oriented attack delivery”), these ploys lean on lies like:

*   You bought something, sending a fake confirmation for a payment never received
*   You didn’t buy something, because your payment didn’t go through
*   Your subscription is due for renewal, along with a handy link to renew it

### 4. BEC Targets Scandinavia

BEC scams are high on attackers’ priority lists for the damage they can do and the rewards they can bring. In this quarter’s report, BEC accounted for 42% of scam emails overall.

**Impersonation breakdown:**
*   CEO/Executive: 82%
*   Director/Manager: 9%
*   Human Resource: 4%
*   IT Personnel: 3%
*   School Head: 2%

**BEC Scams Target English, Danish, Swedish, and Norwegian Speakers:**
On closer examination, we see that executives in a few select countries were targeted the most.
*   English accounts for 42% of BEC samples
*   Danish takes home 38%
*   Swedish and Norwegian BEC scams make up 19% collectively

The notable use of Danish, Swedish, and Norwegian in BEC emails reflects a strategic shift by threat actors towards regional targeting and language localization.

### 5. Malware Family of the Quarter: Lumma Stealer

Our telemetry and malicious spam campaign analysis indicated that Lumma Stealer was the most encountered malware family found in the wild during Q2. This infostealer continues to evolve rapidly, frequently seen distributed through emails containing malicious attachments or download links.

*   **Primary Delivery Method**: Malicious .docx, .html, or .pdf attachments, or phishing links.
*   **Data Theft Capabilities**: Browser-stored credentials, cryptocurrency wallets, system information, saved passwords.
*   **Attribution**: Sold as Malware-as-a-Service (MaaS).

---

## New Trends in the Anatomy of an Attack: From Start to Finish

### 1. The Bait: How Attackers Lure Us In?
Financial lures were the number one ploy used to get users to open malicious emails (35%). Next were Package/Delivery (25%), Account Verification/Update (20%), Legal or HR Notices (10%), Travel-themed (5%), and Urgent Requests (5%).

### 2. Closing the Trap: Links and Attachments
Among phishing link delivery types, the majority (54%) utilized open redirect mechanisms. The next most prevalent was compromised websites (30%), followed by URL shorteners (7%).

When it comes to attachments:
*   PDFs (64%) - The majority contained QR codes.
*   HTML (14%) - Used for fake login forms.
*   DOCX (13%) - Frequently containing QR codes or macros.
*   SVG (9%) - Plummeted from 34% last quarter.

### 3. Where the Rubber Hits the Road: Exfiltration Methods
*   52% HTTP POST to remote server
*   30% Email Exfiltration
*   10% Telegram Bots/Webhooks
*   8% Unknown/Obfuscated

---

## Feature: Attackers Use Legit Login Pages to Throw Us Off the Trail

Our analysis of Q2 data reveals that no less than 60% of all credential harvesting pages redirect to an actual, legitimate Microsoft login page. When the victim has to enter their account credentials twice, it will seem like the page is just reloading, or that double authentication was required. This tactic not only evades human detection but also delivers an edge against security solutions designed to spot anomalies in the flow.

---

## Feature: Malicious Emails Spike Worldwide in June

Between June 9 and June 12, there was a pronounced spike in the number of spam emails. Another sharp increase occurred on June 16th. The timing of the spikes corresponds with critical end-of-quarter financial closing activity such as budget reviews, invoicing, and reporting deadlines.

---

## Concluding Thoughts: Personalization Is Public Enemy #1 in Phishing

Thanks to AI, malicious hackers can take powerful and personalized spear-phishing techniques that target high-value individuals over time and apply those same customizable tactics to everyone.

Spear phishing campaigns boast incredible click-through rates of over 53%, while regular phishing emails hover around 18%. Since the release of ChatGPT, phishing has increased by 4,151%.

If employees can’t catch these phishing ploys, organizations need to turn to technology that can. Integrated cloud email security (ICES) solutions like VIPRE Integrated Email Security (IES) are built to catch behavioral patterns, giveaways in semantics, and red flags in attacker language and tone to spot social engineering threats that otherwise evade detection.