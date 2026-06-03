# Annual Threat Report 2025

## Table of Contents
- [Letter from the CEO](#letter-from-the-ceo)
- [Letter from the CSO](#letter-from-the-cso)
- [Executive summary](#executive-summary)
- [2024 by the numbers](#2024-by-the-numbers)
- [Identity threats](#identity-threats)
- [Cloud platform threats](#cloud-platform-threats)
- [Computer-based threats](#computer-based-threats)
- [Phishing threats](#phishing-threats)
- [Annual spotlight](#annual-spotlight)
- [Looking ahead to 2025](#looking-ahead-to-2025)
- [2024 at Expel](#2024-at-expel)
- [Reference highlights](#reference-highlights)

---

## Letter from the CEO

“Regardless of your org’s security maturity, there’s something here for everyone.”

Expel’s customer base runs the gamut, spanning organizations across almost every industry. This diversity grants our operators unique access to a wealth of data, which is crucial for staying ahead of threat actors and driving innovation.

This access also comes with serious responsibility. Namely, in protecting and maintaining the trust of our customers, but also in how we use our access and insights to share our learnings to continue fighting cybercriminals together as defenders.

As we delve into trends from 2024—ranging from cloud to phishing and everything in between—we’ll share what the data told us, how to detect (and protect yourself) against similar threats, and what that might look like in the coming year. Additionally, we’ll share thoughts and predictions for 2025 from our Expel experts, based on both their personal experiences and what they’re seeing throughout the industry.

Regardless of your org’s security maturity, there’s something here for everyone. Whether you’re strengthening your cloud environment, working to identify specific threats, or just exploring the data, we hope this report helps you start 2025 more informed and better equipped as we face the looming challenges ahead together.

Dave Merkel
CEO, Expel

---

## Letter from the CSO

“Cybersecurity is a team sport, and it’s a game of inches—not yards. Slow, continuous progress is the key to creating a sustainable security strategy that scales with your business.”

In an industry that’s oversaturated with digital content, I want to thank you for carving out some time from your likely overbooked schedule to review our Expel Annual Threat Report. Cybersecurity isn’t a slow industry, and, again, we know your spare time is limited. Your day-to-day consists of nothing but complex, nonstop problem-solving, so hopefully this report makes your day job a little bit easier.

While the data presented here is based on technology, it’s colored by the experiences, challenges, and successes our analysts saw throughout 2024. This team of experts works 24x7, every day of the year to keep us and our customers safe. In this report, you’ll see the threats they encountered and how they overcame them, so we can all learn together as we work towards a more secure future.

Cybersecurity is a team sport, and it’s a game of inches—not yards. Slow, continuous progress is the key to creating a sustainable security strategy that scales with your business. Our goal is to translate our data into strategic guidelines you can use to better protect your business, while, in the process, sharing information and contributing to the betterment of our cybersecurity community.

Greg Notch
CSO, Expel

---

## Executive summary

### Key insights and takeaways
For the last four years, we’ve published this report detailing the attack trends our security operations center (SOC) analysts protect against every day. This is an analysis of the incidents, email submissions, vulnerability tracking, and threat hunting leads that our team investigated from January 1 to December 31, 2024.

We break down the trends into four essential threat categories: identity, cloud infrastructure, computer-based, and phishing. We do this to keep the report easy to digest and take action on, but keep in mind these threats are often tightly related. For example, attackers using endpoint phishing to deploy malware can lead to compromised user identities, impacting an organization’s cloud assets. We’ll highlight this interconnectivity throughout the report. But first, let’s review what we saw as the top trends in each threat category.

### OUR TOP TAKEAWAYS:

**Identity trends continue to dominate incident investigations**
Identity-based incidents made up 68% of all incidents among Expel customers, up four percentage points from 2023. While attempting to access email accounts is the most classic form of account abuse, successful identity attacks can be used to modify payroll settings, access cloud environments, or connect new (and malicious) devices to a network. Identity-based threats are highly lucrative for attackers, and should continue to be a high priority for defense.

**Leaked and stolen credentials cause most cloud incidents**
Attackers abusing leaked or stolen secrets caused the most cloud incidents this year, continuing previous years’ trends. It’s easy for users to expose keys inadvertently, and these keys typically provide high levels of access to attackers, making them attractive targets.

**New malware scams drive most endpoint threats**
Infostealing malware—which is malware that targets user credentials—made up the highest number of endpoint incidents. Stolen information often ends up on the dark market, where adversaries can buy and leverage it for new attacks. If credentials don’t change or accounts aren’t disabled, attackers can abuse them years after the original malware execution.

A popular means to deploy malware is a tactic tricking users into executing malicious scripts on their own machines (like presenting the user with a fake CAPTCHA). This tactic has become the most frequent means of installing malware onto a device because it bypasses the need for a user to download and run a program.

**Credential harvesting has become the most prominent form of phishing**
Of the phishing trends our SOC saw in 2024, about 41% of malicious phishing submissions were attempts to deploy credential harvesters, and about 34% of submissions were other forms of social engineering. These rates were consistent across industries.

In addition to hearty amounts of credential harvesters and social engineering attempts, we also saw extortion attempts across several industries. This tactic typically involves a phishing email sent to a user’s corporate email account, which includes pieces of personal information in an attempt to scare the targeted user into completing a desired action for the attacker. The activity appears to be a steady campaign with no signs of diminishing any time soon.

**Vulnerability trends**
The newest and most severe vulnerabilities in 2024 were in firewall and VPN appliances. Firewall and VPN appliances normally gate access to an environment, but can provide a springboard for attackers when compromised. However, despite these new and powerful vulnerabilities, we also observed attackers frequently leveraging vulnerabilities from years past. Older vulnerabilities still being leveraged include Log4j (CVE-2021-44228), Oracle WebLogic remote code execution (CVE-2020-14882), and Microsoft Office Outlook privilege escalation (CVE-2023-23397).

**Spotlight: Microsoft Teams setting allows malicious external messages**
A default setting in Microsoft Teams allows users to receive messages from external organizations, and attackers abused this tactic throughout 2024 to gain unauthorized network access. These attacks abuse a built-in remote access tool—Quick Assist—and leverage other commercial remote access tools to gain and keep access to target systems.

---

## 2024 by the numbers

### Incident types detected by Expel’s SOC
This year’s incident data compared to last year:

- **Identity-based incidents dominated again this year**, making up 68% of all incidents in 2024—four percentage points higher than in 2023.
    - In the context of this report, we define identity-based attacks as attempts by cybercriminals to gain access to a user’s identity to perpetuate fraud.
- **Endpoint-based incidents accounted for 22% of threats**, likely only decreasing from 2023 due to the increase in identity threats.
    - The highest subcategory was malware, driven up by a tactic called ClickFix, which we’ll discuss in depth on page 16.
- **Attacks specifically targeting cloud infrastructure accounted for approximately 2% of threats**, which was identical to 2023. While a few actors are specializing in targeting these assets, this category doesn’t have the volume of incidents that other categories have.
    - The highest volume of cloud infrastructure incidents are the result of leaked or stolen cloud secrets.
- **Targeted threats account for 1% of incidents.** These attacks involve a bad actor who has their eyes set on a very specific organization or goal.

![Chart 1: Breakdown of incidents detected by the Expel SOC in 2023 and 2024]

### Why measure a category that’s only 1% of incidents?
Even though targeted attacks make up a small percentage of incidents, these attacks deserve special attention in detection and response. Most incidents are opportunistic, and cast a wide net to identify any vulnerable target. With targeted attacks, they’re incredibly persistent because attackers have their sights set on a specific target, and this persistence makes them a bit more dangerous.

Targeted attacks are tailored to a specific organization and may rely on open source intelligence collected about employees. Attackers are likely to make several attempts if one fails, using any learnings from failed attacks to adapt and improve. Although they make up a small number of incidents, this determination to succeed means analysts should be extra vigilant when a targeted attack is spotted.

### Incidents across industries
Identity compromise, most often the result of phishing, is a threat seen across all industries. While some sectors face higher volumes, no industry is immune. This is a major reason that identity incidents feature prominently in this report.

![Chart 2: Incidents across top 10 industries]

### Initial alert sources in 2023 and 2024
Cloud resources managing identity, data, and infrastructure provided the highest number of leads to identify malicious activity, with identity being the foremost. This is consistent with identity being the most common entry point for cyber attacks, and it trended the same in both 2023 and 2024.

Endpoint detection and response (EDR) systems continued to be the primary source of monitoring and means of finding threats within networks in 2024. EDR systems identified 25% of all incidents, while SIEM and network monitoring systems provided alert leads for 3% and 1%, respectively.

![Chart 3: Initial alert sources identifying incidents]

---

## Identity threats

### Stealing and abusing credentials
Year-over-year, identity-based attacks continue to be the most common attack type we see across our customer base, with increasing volume. Barring major changes in cybercrime, we expect this trend to continue into 2025. Threat actors will continue to innovate, finding new ways to iterate on tried-and-true methods to steal and abuse credentials.

### How are credentials stolen?
This year, we observed three primary contributors to the theft and abuse of credentials: phishing-as-a-service (PhaaS) platforms, traditional phishing, and infostealing malware.

**PhaaS platforms**
PhaaS platforms provide an aspiring criminal with an easy introduction into cybercrime. Just like platform-as-a-service (PaaS) software products used by legitimate businesses, PhaaS offers access to a service without requiring the buyer to set up their own infrastructure. These platforms offer many of the necessary components for running a phishing campaign, such as templates, infrastructure, and victim tracking. The buyer is only responsible for providing a target list and then acting on any stolen credentials.

PhaaS platforms work by creating a webpage that can proxy information to and from the legitimate login domain. This type of proxying is classified as an adversary-in-the-middle (AiTM) tactic, since it allows an attacker to intercept traffic.

Since the webpage is proxying traffic, it’s often configured to load the same graphics as the legitimate login page. If the target organization has a specific background or logo, the malicious page will also use this information to make it look legitimate. The fake page then submits any information supplied by the user and returns any results provided by the real login page. So if the real login page requests an MFA token or a one-time pass (OTP), the fake one will request this information too.

The proxying page intercepts session cookies, which can then be used by an attacker to access the account and bypass MFA. We most frequently see this attempt to access the account occur from a hosting provider.

![Chart 4: Authentication sources over time]

### How are stolen credentials leveraged?
For credentials to be leveraged, they first must be stolen. The graph below represents incidents where credentials have been successfully compromised. In most identity incidents we observed this year (56%), the bad actor was blocked from accessing the account via customer security controls after the credentials were compromised. The other 44% of the time, attackers most often used stolen credentials to access email accounts and single-sign-on (SSO) applications.

![Chart 5: Type of identity compromise tracked in 2024]

### Protecting your organization from PhaaS platforms
- **Triggering alerts for newly added MFA devices:** Give special attention to MFA devices added after passwords resets, and MFA devices added while connected to a proxy or VPN.
- **Triggering alerts for the creation of new inbox rules:** Attackers commonly use simple names for inbox rules. Many attacker-created rules can be caught by looking for rules consisting of two to three characters or only containing a single repeating character. Monitor for rules created containing keywords like “payroll”, “malware”, or “virus”.
- **Advising employees to know their payroll information:** Report any abnormal or suspicious activity to the security team. Changes resulting in unexplained variances in paychecks are evidence of an identity compromise.

---

## Cloud platform threats

### Increased cloud adoption leads to increased cloud threats
Cloud infrastructure attacks target assets hosted on cloud platforms such as Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Kubernetes. The techniques and frequency of these attacks continue to evolve, reflecting the growing adoption of cloud environments and the expanding attack surface that comes with them.

Expel defines cloud infrastructure activity as an incident where an attacker can gain access to the control plane or data plane of a cloud platform. In 2024, 86% of our cloud infrastructure incidents impacted assets in AWS, while only 9% impacted assets in Google Cloud and Azure.

![Chart 6: Cloud infrastructure incident types in 2024]

### Protecting your organization from cloud infrastructure threats
Just like with other technologies, it’s important to ensure your cloud infrastructure is monitored with a defense-in-depth strategy. That is, build your detections to spot suspicious activity at multiple stages of the attack lifecycle.

Secrets are most often exposed accidentally. We recommend using secret scanning to prevent key exposure. This process can identify accidentally exposed access keys in code repositories during development, or after publishing. Secret scanning can also be performed through paid services, or can be configured with open source tools.

For AWS specifically, you can create detections around long-term and short-term access keys (beginning with AKIA and ASIA, respectively) to detect early stages of unauthorized access to your environment.

---

## Computer-based threats

### Trending malware and popular vulnerabilities
In the neverending game of cat-and-mouse, both attackers and defenders study each other to understand what tactics might outwit their opponent. Just like defenders, successful cybercriminals learn from one another and adopt effective techniques.

### Malware trends
At Expel, we break malware into two major categories based on risk: high-risk malware and latent-risk malware. High-risk malware can take off fast and cause a lot of damage. This category includes remote access tools (RATs), initial access tools (IATs), and USB initial access tools. Latent-risk malware is all about the long game: the cybercriminals deploying malware aren’t acting immediately on their objectives. This category includes infostealers, cryptocurrency miners, and banking trojans.

![Chart 7: Malware type prevalence 2024 vs. 2023]
![Chart 8: 2023 and 2024 malware types by quarter]

### Development and growth of the ClickFix tactic
With the decline of Qakbot and Gootloader malware, the most consistent IAT threat is SocGholish malware. The criminal group maintaining the malware consistently relies on infected websites to deliver it.

In this approach, the infected website displays a message instructing the user to download and run malware disguised as a browser update. If the user attempts to download the fake update, they’ll receive a JavaScript file which, when executed, loads malware onto their system.

![Image 1: Example of SocGholish phishing designed to execute JavaScript and deploy IAT malware]

Attackers continued to innovate on this tactic throughout 2024. New versions simplified the instructions and started to use other scenarios such as fake CAPTCHAs, documents, and system errors. These versions automatically modified the user’s clipboard and instructed them to run the code using the Windows Run application (launched with the Windows + R key combination).

![Image 2: Examples of the ClickFix tactic]

### Protecting your organization against the ClickFix tactic
- **Use secure web gateways to block traffic from attacker-controlled domains.**
- **Ensure hosts are monitored with EDR and have the EDR in blocking mode.**
- **Consider disabling the Windows Run program for users who don’t need it using the Group Policy Editor.**

---

## Phishing threats

### Credential harvesters and social engineering
Throughout the year, credential harvesters made up, on average, 41% of malicious submissions. Another 34% of submissions were other forms of social engineering, such as fake invoices aiming to get targets on the phone to then install RATs on their computers, CEO impersonations asking for gift cards, or emails requesting sensitive information under the guise of a government organization.

![Chart 11: Percentage of malicious submissions]

### Protecting your organization from phishing
- **Ensure users rely on MFA wherever possible.** The most secure forms of MFA follow the Fast Identity Online 2 (FIDO2) standard.
- **Ensure users have training to identify and report suspicious emails.**
- **Use secure email gateways and similar products.** These products can filter out a substantial amount of phishing emails.

---

## Annual spotlight

### Microsoft Teams continues to be a phishing target
Throughout the year, threat actors leveraged Microsoft Teams to gain access to targeted networks. A campaign using this tactic—which was seen first in April and then throughout the year—performed social engineering under the guise of being helpful. The attacker would sign their target up to receive spam emails and then contact the user through a Teams message, offering support to resolve the spam. The invite usually came from an account disguised as a tech support team. If the victim accepted the invite, the attacker would request to connect to the user’s computer using Microsoft’s built-in remote access support tool, Quick Assist.

---

## Looking ahead to 2025

### Thoughts from Expel experts
David Merkel is a unique market where competitors really... [Content truncated in source]

---

do come
together for the greater good. I expect this trend to continue
Chief Executive Officer
as we see both the consolidation of existing cybersecurity
solutions for normalization, storage, and integration, as well
“We’ve seen a steady increase in geopolitical tensions (a
as the emergence of new solutions emerging focused on
massive understatement, considering a land war in Europe
data analysis, governance, and applied AI.”
and large-scale Middle East conflict are just the tip of the
iceberg). There’s no simple solution here, and, unfortunately,
I think these situations will become more intense—the next
geopolitical hotbed to emerge is anyone’s guess. Whether Greg Notch
these activities will increase the likelihood of cyber threat Chief Security Officer
activity is a given…and not just from nation states. Activist
groups advocating for either side of a conflict are also a “Protection against identity threats will remain the single
factor, as are criminal actors looking to take advantage of the most important part of most companies’ security posture.
chaos. This year will be interesting, to say the absolute least.” Attacks will continue increasing in sophistication and speed,
especially powered by artificial intelligence, which is aiding
attackers to carry out tried and true methods more efficiently.
Cat Starkey This will only exacerbate onboarding and hiring fraud as a
significant problem for most companies, especially those
Chief Technology Officer
with large remote workforces. Validating and revalidating the
identity of authorized users, especially for third- and fourth-
“The use of common data schemas is a foundational element
party providers, will be a continued challenge. The rise of
of scalable technology. T hey allow your platform to support
deepfakes and generated identities will also make identity
a vast number of use cases without a lot of specialized
adjacent security technologies critical.”
code, making technology far less brittle and new features
far easier to build. As cybersecurity technology evolves to
cover more and more attack surfaces, defining a common
data schema that’s standard enough, and flexible enough, Aaron Walton
is a tricky exercise. Y ou’re not just working with apples and Threat Intelligence Analyst
oranges—you’re working with apples, oranges, apple carts,
and giraffes. “Attacker implementation of AI and ML will have a heavy
impact on small-to-medium businesses. These smaller
“A community of folks from cybersecurity and technology
businesses lack the resources of larger organizations and,
companies are collaborating to standardize security data
thus, are slower to innovate, giving attackers the advantage.
formats through the Open Cybersecurity Schema Framework
Attackers can easily scale and iterate on their attacks, and
(OCSF) project. As this schema matures to cover more and
without equal innovation and acquisition of defenses, smaller
more data categories, we’d expect to see wider adoption
businesses risk exposure.”
across security lakes and security vendors, making it easier
to integrate across technologies. This type of collaboration
in the cybersecurity space demonstrates how cybersecurity
Annual Threat Report 2025 28

Amy Rossi Alex Glass
Chief People Officer VP, Global Channel & Alliances
“Where companies really need to prepare for change is in the “As we move into 2025, partners will need to understand
rapid adoption of generative AI tools like ChatGPT, Claude, what risk generative AI poses within their customers and
Gemini, DALL-E, and Sora. We’re now in an era where most help them to define policies to best mitigate their risk. One
employees can benefit from GenAI to enhance how they of the major challenges they will face will be having to
work. They will use AI assistants for research, drafting fight through all of the ‘vendor noise’ related to leveraging
documents, coding, business analysis, creative ideation, and AI as a marketing buzz word, similar to the ‘zero-trust’
more—whether their employers condone it for professional phrase seven to eight years ago. In reality, businesses
use or not. Think BYOD concerns from the early 2000s but shouldn’t have to shell out more cash to security vendors
multiplied a thousandfold by the power of generative AI. just because they slapped an AI label on their solutions.
AI should make security smarter and quicker, but that’s a
“AI tools don’t just store or transmit information—they learn
functionality upgrade, not a revolution. If a vendor claims AI
from, transform, and reproduce it in ways that cascade
is transforming their product and asks for more money to flip
beyond our ability to predict or control. This creates a
the switch, it’s time to raise an eyebrow.”
security risk for companies, especially as most people will
be ‘dangerous novices,’ not understanding the implications
of their exploration of these tools. This is no longer a future
Matt Jastram
hypothetical. Security and HR teams must work together to
provide consistent education on how to safely use these Senior Managed VM Analyst
tools to enhance work product and output—or risk major
security consequences for their businesses.” “To meet financial goals, businesses must operationally
maintain their externally-facing infrastructure. In 2025, we’ll
continue to see threat actor tactics evolve. Attackers will
seek to advance their methods to actively leverage exploits,
to ultimately create impactful outcomes on their targets. Only
vigilant businesses who identify their whole attack surface,
and comprehensively mitigate risk, will achieve outcomes
that minimize cyber impacts.”
Annual Threat Report 2025 29

2024 at Expel
Headlines, accolades, and research
AWARDS PARTNERSHIPS
 Expel clinches Gold at the 2024 Globee® Awards,  Expel and ivision partner to deliver industry-leading
named top cybersecurity vendor of the year managed detection and response outcomes to
 Expel celebrates fourth consecutive ranking on the
ivision clients
Deloitte Technology Fast 500™  Expel and modePUSH forge strategic partnership to
provide MDR and IR capabilities
INDUSTRY RECOGNITION  Expel double downs on cloud leadership with Wiz
strategic partnership
 Expel again recognized in the Gartner® Market Guide
for Managed Detection and Response Services
 Expel’s new partner program earns spot in 2024 CRN®
EXPEL QUARTERLY
THREAT REPORTS 2024
Partner Program Guide
 IDC names Expel a Leader in 2024 MarketScape for  Q1 QTR
worldwide emerging MDR services  Q2 QTR
 Q3 QTR
RESEARCH
 From exhaustion to equilibrium: battling burnout in WANT TO LEARN MORE
your SOC ABOUT EXPEL?
 Subscribe to our blog
NEWS
 Request a demo
 Cybersecurity pioneer Kevin Mandia joins Expel’s
 Contact us
board of directors
 Expel announces expansion into Ireland with creation
of 50 cybersecurity jobs
PRODUCT UPDATES
& FEATURED LAUNCHES
 Expel unveils updated NIST CSF 2�0 getting
started toolkit to help companies on their security
maturity journey
 Expel unveils new, flexible offerings to allow
organizations of any size and budget to benefit from
leading MDR technology
 Expel MDR has new advanced identity threat
detection & response
Annual Threat Report 2025 30

Reference highlights
Sources consulted and our authors
Sources Report contributors
This report wouldn’t be possible without Expletives
 https://www�justice�gov/opa/pr/qakbot-malware-
dedicated to sharing this information with our
disrupted-international-cyber-takedown
community to empower practitioners creating safer
 https://gootloader�wordpress�com/2024/11/07/ cyber environments. Thank you!
gootloaders-pivot-from-seo-poisoning-pdf-
converters-become-the-new-infection-vector/
Authors
Aaron Walton, Christine Billie, Matt Jastram
 https://www�rapid7�com/blog/post/2024/05/10/
ongoing-social-engineering-campaign-linked-to-
black-basta-ransomware-operators/ Technical reviewers
Joe Choi, Amar Rekic, Girish Mukhi
 https://www�proofpoint�com/us/blog/threat-
insight/clipboard-compromise-powershell-self-
pwn Editors
Andrew Rodger, Ben Baker, Brooke McClary,
 https://www�thewindowsclub�com/enable-or-
Scout Scholes
disable-run-command-winr-box-in-windows-10
 https://spycloud�com/blog/lummac2-malware- Designer
stealthier-capabilities/ Mel Todas
Annual Threat Report 2025 31

ABOUT EXPEL
Expel is the leading managed detection and response (MDR) provider trusted by some
of the world’s most recognizable brands to expel their adversaries, minimize risk,
and build security resilience. Expel’s 24x7x365 coverage spans the widest breadth
of attack surfaces, including cloud, with 100% transparency. We combine world-class
security practitioners and our AI-driven platform, Expel Workbench™, to ingest billions
of events monthly and still achieve a 20-minute critical alert MTTR. Expel augments
existing programs to help customers maximize their security investments and focus on
building trust—with their customers, partners, and employees. For more information,
visit our website, check out our blog, or follow us on LinkedIn.
© 2025 Expel, Inc�
01/30/25