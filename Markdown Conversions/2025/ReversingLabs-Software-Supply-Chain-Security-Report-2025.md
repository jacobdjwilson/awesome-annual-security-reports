# ReversingLabs Software Supply Chain Security Report 2025

The official report URL is: https://www.reversinglabs.com/sscs-report

## Table of Contents
- [A Message from Our CEO](#a-message-from-our-ceo)
- [Report Highlights](#report-highlights)
- [Executive Summary](#executive-summary)
- [Key Trends](#key-trends)
  - [Software Supply Chain Attacks Level Up](#software-supply-chain-attacks-level-up)
  - [Crypto: A Canary in the Coalmine for Supply Chain Security](#crypto-a-canary-in-the-coalmine-for-supply-chain-security)
  - [Focus: Crypto in the Crosshairs](#focus-crypto-in-the-crosshairs)
  - [The XZ Utils Backdoor](#the-xz-utils-backdoor)
  - [State-Actor Attacks on Development Organizations](#state-actor-attacks-on-development-organizations)
- [Serious Cyber Risks Lurk in Commercial Binaries](#serious-cyber-risks-lurk-in-commercial-binaries)
  - [Commercial Binaries: What You Don’t Know Is Already Hurting You](#commercial-binaries-what-you-dont-know-is-already-hurting-you)
  - [Focus: Commercial Software’s Seven Deadly Sins](#focus-commercial-softwares-seven-deadly-sins)
- [Hack of JAVS Highlights Risks Lurking in Commercial Apps](#hack-of-javs-highlights-risks-lurking-in-commercial-apps)
  - [Implanted Backdoor Delivers RustDoor Malware](#implanted-backdoor-delivers-rustdoor-malware)
  - [JAVS Differential Analysis Exposes Signs of Tampering](#javs-differential-analysis-exposes-signs-of-tampering)
  - [Links to Ransomware Groups](#links-to-ransomware-groups)
  - [Lesson Learned: Don’t Trust, but Verify Commercial Binaries](#lesson-learned-dont-trust-but-verify-commercial-binaries)
- [The Great Unpatched: Open-Source Risks Persist](#the-great-unpatched-open-source-risks-persist)
  - [Vulnerable and Popular: Serious Risks Lurk In Open-Source Packages](#vulnerable-and-popular-serious-risks-lurk-in-open-source-packages)
  - [Critical and Patch-Mandated Flaws Taint Popular Packages](#critical-and-patch-mandated-flaws-taint-popular-packages)
  - [Mind the Rot](#mind-the-rot)
  - [Who Pays for Vulnerable Code? Customers.](#who-pays-for-vulnerable-code-customers)
  - [Focus: Serious Risks Lurk in Torchvision Python Package](#focus-serious-risks-lurk-in-torchvision-python-package)
  - [Leaked Secrets Persist on Open-Source Repositories](#leaked-secrets-persist-on-open-source-repositories)
  - [Development Secrets Leaks Jump 12%](#development-secrets-leaks-jump-12)
  - [Google, AWS (Still) Fertile Ground for Exposed Secrets](#google-aws-still-fertile-ground-for-exposed-secrets)
  - [Secrets Leaks a Common Thread in Supply Chain Attacks](#secrets-leaks-a-common-thread-in-supply-chain-attacks)
  - [GitGot? GitHub Features Exploited by Malicious Actors](#gitgot-github-features-exploited-by-malicious-actors)
  - [Malicious Campaigns Crop Up on NuGet, VS Code](#malicious-campaigns-crop-up-on-nuget-vs-code)
  - [A Drop in Open-Source Malware](#a-drop-in-open-source-malware)
- [CVEs Lose Relevance](#cves-lose-relevance)
  - [Cracks in the NVD Emerge](#cracks-in-the-nvd-emerge)
  - [Vulnrichment to the Rescue?](#vulnrichment-to-the-rescue)
  - [Imagining a Post-CVE Future](#imagining-a-post-cve-future)
- [Supply Chain Incidents 2024](#supply-chain-incidents-2024)
- [What Comes Next](#what-comes-next)
  - [AI/ML Supply Chain Risks Get Real](#ai/ml-supply-chain-risks-get-real)
  - [Organizations Level Up Their Software Supply Chain Security](#organizations-level-up-their-software-supply-chain-security)
  - [Nth Party Risk: Thinking Beyond the SBOM](#nth-party-risk-thinking-beyond-the-sbom)
- [Our Methodology](#our-methodology)
  - [CVE and Vulnerability Data](#cve-and-vulnerability-data)
  - [Security Policies](#security-policies)
  - [OpenSSF Malicious Packages Repository Ratings](#openssf-malicious-packages-repository-ratings)
  - [Malicious Package Statistics](#malicious-package-statistics)
- [About RL](#about-rl)

---

1

©2025 ReversingLabs, Inc. — All Rights ReservedTRUST DELIVERED

Table of Contents

[A Message from Our CEO](#a-message-from-our-ceo)

[Report Highlights](#report-highlights)

[Executive Summary](#executive-summary)

[Key Trends](#key-trends)

[Software Supply Chain Attacks Level Up](#software-supply-chain-attacks-level-up)

[Crypto: A Canary in the Coalmine for Supply Chain Security](#crypto-a-canary-in-the-coalmine-for-supply-chain-security)
[Focus: Crypto in the Crosshairs](#focus-crypto-in-the-crosshairs)
[The XZ Utils Backdoor](#the-xz-utils-backdoor)
[State-Actor Attacks on Development Organizations](#state-actor-attacks-on-development-organizations)

[Serious Cyber Risks Lurk in Commercial Binaries](#serious-cyber-risks-lurk-in-commercial-binaries)

[Commercial Binaries: What You Don’t Know Is Already Hurting You](#commercial-binaries-what-you-dont-know-is-already-hurting-you)
[Focus: Commercial Software’s Seven Deadly Sins](#focus-commercial-softwares-seven-deadly-sins)

[Hack of JAVS Highlights Risks Lurking in Commercial Apps](#hack-of-javs-highlights-risks-lurking-in-commercial-apps)

[Implanted Backdoor Delivers RustDoor Malware](#implanted-backdoor-delivers-rustdoor-malware)
[JAVS Differential Analysis Exposes Signs of Tampering](#javs-differential-analysis-exposes-signs-of-tampering)
[Links to Ransomware Groups](#links-to-ransomware-groups)
[Lesson Learned: Don’t Trust, but Verify Commercial Binaries](#lesson-learned-dont-trust-but-verify-commercial-binaries)

[The Great Unpatched: Open-Source Risks Persist](#the-great-unpatched-open-source-risks-persist)

[Vulnerable and Popular: Serious Risks Lurk In Open-Source Packages](#vulnerable-and-popular-serious-risks-lurk-in-open-source-packages)
[Critical and Patch-Mandated Flaws Taint Popular Packages](#critical-and-patch-mandated-flaws-taint-popular-packages)
[Mind the Rot](#mind-the-rot)
[Who Pays for Vulnerable Code? Customers.](#who-pays-for-vulnerable-code-customers)
[Focus: Serious Risks Lurk in Torchvision Python Package](#focus-serious-risks-lurk-in-torchvision-python-package)
[Leaked Secrets Persist on Open-Source Repositories](#leaked-secrets-persist-on-open-source-repositories)
[Development Secrets Leaks Jump 12%](#development-secrets-leaks-jump-12)
[Google, AWS (Still) Fertile Ground for Exposed Secrets](#google-aws-still-fertile-ground-for-exposed-secrets)
[Secrets Leaks a Common Thread in Supply Chain Attacks](#secrets-leaks-a-common-thread-in-supply-chain-attacks)
[GitGot? GitHub Features Exploited by Malicious Actors](#gitgot-github-features-exploited-by-malicious-actors)
[Malicious Campaigns Crop Up on NuGet, VS Code](#malicious-campaigns-crop-up-on-nuget-vs-code)
[A Drop in Open-Source Malware](#a-drop-in-open-source-malware)

[CVEs Lose Relevance](#cves-lose-relevance)

[Cracks in the NVD Emerge](#cracks-in-the-nvd-emerge)
[Vulnrichment to the Rescue?](#vulnrichment-to-the-rescue)
[Imagining a Post-CVE Future](#imagining-a-post-cve-future)

[Supply Chain Incidents 2024](#supply-chain-incidents-2024)

2

©2025 ReversingLabs, Inc. — All Rights Reserved

[What Comes Next](#what-comes-next)

[AI/ML Supply Chain Risks Get Real](#ai/ml-supply-chain-risks-get-real)

[Organizations Level Up Their Software Supply Chain Security](#organizations-level-up-their-software-supply-chain-security)

[Nth Party Risk: Thinking Beyond the SBOM](#nth-party-risk-thinking-beyond-the-sbom)

[Our Methodology](#our-methodology)

[CVE and Vulnerability Data](#cve-and-vulnerability-data)

[Security Policies](#security-policies)

[OpenSSF Malicious Packages Repository Ratings](#openssf-malicious-packages-repository-ratings)

[Malicious Package Statistics](#malicious-package-statistics)

[About RL](#about-rl)

3

©2025 ReversingLabs, Inc. — All Rights Reserved

<a name="a-message-from-our-ceo"></a>
## A Message from Our CEO

Software
Supply
Chain Risk
Is Evolving.
Be Prepared.

Mario Vuksan
CEO AND CO-FOUNDER,
REVERSINGLABS

This year’s ReversingLabs Software Supply Chain
Security Report has a clear message — “Software
supply chain risk is evolving” — and a clear moral:
“Your organization needs to be ready!”

ReversingLabs (RL’s) 2025 report shows that
the security of software supply chains lags, even
as malicious actors score bigger and bigger
wins targeting the commercial and open-source
software running in homes, businesses, and
powering critical infrastructure. RL’s research
over the past year identified compromises of
open-source libraries and modules that are
widely used in both the cryptocurrency and
artificial intelligence sectors. We also uncovered
widespread and exploitable flaws in commonly
used open-source packages and third-party,
commercial software binaries.

Unaddressed security risks such as these set the
stage for bigger attacks in 2025. The question
is: Are we ready to stare them down? The key
to answering that question — and getting our
response right — is changing the status quo for
software security, which lacks incentives for
software producers to secure their software and
IT assets, and complicates efforts by end-user
organizations to assess the risks lurking in the
software and services their business relies on.

Incidents like recent campaigns by state
actors targeting critical infrastructure and
telecommunications networks underscore the
urgency of efforts by both public- and
private-sector entities to accurately assess
the cyber risks facing them and take proper
steps to secure their IT assets and data. To do
so, however, both private- and public-sector
organizations need to acknowledge a shift in
threats and attacks, including growing instances
of software supply chain compromises.

To help underscore this growing risk, RL
researchers explored the attack vectors and
methods that are favored by both cybercriminal
and nation-state actors. Their work provides
valuable insights into the evolving cyber-risk
landscape and a useful preview of the kinds of
threats and attacks that organizations will face
in 2025.

Like any good report, our Software Supply Chain
Security Report also provides recommendations
on how to best address those risks: leveling up
your software supply chain security tools and
methods, while also pushing back on suppliers
for more transparency about their secure
development practices and any risks that may
lurk in both the open source and proprietary code
that powers their solutions.

I hope you enjoy reading this report. We here at
RL look forward to continuing our work helping to
secure organizations from software supply chain
threats in 2025.

4

©2025 ReversingLabs, Inc. — All Rights Reserved

<a name="report-highlights"></a>
## Report Highlights

1

Software supply chain attacks got more sophisticated in 2024 as malicious actors launched attacks
on the build pipelines of prominent open-source projects, singled out AI and machine-learning
software supply chains, and took advantage of epidemic, exploitable flaws in black-box, commercial
software binaries.

2

Open-source software risks shifted noticeably. Incidents of open-source malware dropped, while
leaks of developer secrets and other sensitive information rose by 12%, fueling high-profile
open-source supply chain compromises.

12%

increase

3

A survey of 30 npm, PyPI, and RubyGems packages found that large numbers of critical and
exploitable flaws lurk in the latest versions of leading open-source packages that account for more
than 650 million total downloads across the 30 packages and three package managers. The median
number of security flaws discovered per package was 27 (avg. 68), with 2 critical-severity flaws per
package (avg. 6).

million650

PACKAGE

27 security ﬂaws

2 critical
severity

4

Supply chain attacks on cryptocurrency applications and infrastructure were frequent in 2024, as
attackers sought (and got) access to sensitive IT assets and diverted funds from cryptocurrency
wallets. The shape and frequency of the crypto attacks are a warning sign that other industries
should take note of.

5

The cybersecurity industry’s heavy focus on Common Vulnerabilities and Exposures (CVEs) as
the measure of cyber risk was called into question following a breakdown at NIST’s National
Vulnerability Database (NVD) and the CVE reporting system. New ways of assessing cyber risk are
needed as organizations face growing risks from undisclosed software flaws, code tampering, and
compromised or malicious software modules.

6

AI’s explosive growth in the enterprise and the growing reliance of software development
organizations on AI-generated code was accompanied by increased AI and ML supply chain
cyberthreats, as malicious actors look to infiltrate widely used AI ecosystems.

5

©2025 ReversingLabs, Inc. — All Rights Reserved

<a name="executive-summary"></a>
## Executive Summary

Research conducted by RL finds evidence of growing software supply chain risks affecting both software
publishers and end-user organizations in the past year. Those include increasingly sophisticated “hands-
on-keyboard” campaigns to compromise software supply chains and the targeting of applications
and infrastructure linked to both AI and cryptocurrency. Noteworthy incidents in 2024 included the
hack of the XZ Utils open-source package in March 2024, the compromise of the Justice AV Solutions
(JAVS) commercial video software in May 2024, and the insertion of malicious code into the open-
source libraries Solana, Ultralytics, and Rspack, which support millions of downloads and thousands of
dependent applications.

Putting aside extreme incidents like software supply chain compromises, the past year saw an epidemic
of vulnerable and insecure software continue. An analysis of 30 open-source packages accounting for
hundreds of millions of annual downloads found the packages rife with critical-severity as well as patch-
mandated CVEs that were being actively exploited by malicious actors. Beyond software vulnerabilities,
the past year saw a 12% jump in instances of developer secrets and other sensitive data that were
exposed via open-source repositories, according to data compiled by RL Spectra platform.

Add to those factors the vast and vulnerable population of closed-source, black-box commercial
software. An analysis that RL conducted of more than three dozen common commercial binaries
licensed to enterprises found clear evidence of insecure design, insufficient application hardening, and
exposed data and development secrets. This mix of vulnerable open-source and commercial software
makes enterprises and other end-user organizations a soft target for malicious actors. They are a big
problem for organizations that hope to safely manage their software supply chain risks.

Making things worse: the proliferation of software supply chain attacks is occurring at the same time
as a longstanding pillar of enterprise defenses, vulnerability management, is beginning to crumble.
Specifically, the past year witnessed a startling drop in the number and quality of vulnerability
disclosures from the NVD and a declaration in February 2024 by the National Institute of Standards and
Technology (NIST) that it would cease enriching CVEs with critical information such as CVSS criticality
scores, patching status, vulnerability descriptions, and the names of affected products — all critical
information for security teams.

This proliferation of exploitable software flaws, leaked developer secrets, and faltering software-risk
information helps explain why the parade of sophisticated supply chain and cyberattacks did not
slow, despite what appears to be a steep decline in instances of malware on open-source package
managers over the past year. Data compiled by RL’s Spectra Assure™ platform shows what instances
of malicious packages declined by more than 70% from 2023 to 2024 across three major open-source
package managers: npm, Python Package Index (PyPI), and RubyGems. Discovered malware instances
dropped by more than 85% on PyPI, alone. That’s an impressive dip in a trend line that has been moving
sharply upward in recent years and may reflect tighter developer security policies implemented by those
platforms, as well as closer monitoring for threats across many of the major repositories.

Looking ahead, we’re concerned. We are concerned about a favorable environment for malicious actors:
one marked by an increase in supply chain risks, AI-powered threat actors, and waning public-sector
support. The question is, what can companies do to address these growing risks? This report attempts
to answer that question by exploring the many dimensions of the shifting software supply chain security
landscape and highlighting strategies your organization can modernize to take on today’s software threats.

6

©2025 ReversingLabs, Inc. — All Rights Reserved

<a name="key-trends"></a>
## Key Trends

<a name="software-supply-chain-attacks-level-up"></a>
### Software Supply Chain Attacks Level Up

Despite widespread media attention in the last year to the problem of software supply chain security
and concerted efforts by regulatory bodies and government agencies to promote supply chain security,
attacks on both open source code and commercial-software vendors have grown. Among notable
incidents in the last year were:

<a name="crypto-a-canary-in-the-coalmine-for-supply-chain-security"></a>
### Crypto: A Canary in the Coalmine for Supply Chain Security

RL researchers observed a steady stream of malicious campaigns that targeted the infrastructure
and assets for cryptocurrency in 2024. The motivations for these attacks are clear enough. The quote
attributed to Willie Sutton that he robbed banks because ‘that’s where the money is,’ also explains why
cybercriminals and nation-state actors are targeting cryptocurrency exchanges and wallets.

Many of these supply chain attacks are straightforward. For example, a number of campaigns employed
typosquatting to fool developers working on crypto-related apps to add compromised file dependencies
that would enable the theft of cryptocurrency from users’ wallets. We saw this happen in March 2024,
when RL threat researcher Karlo Zanki exposed BIPClip, a malicious PyPI campaign targeting developers
working on projects related to generating and securing cryptocurrency wallets.[^1]

But crypto-focused attackers also employed more sophisticated and high-touch techniques to gain
access to sensitive cryptocurrency applications and infrastructure. For instance, in November 2024,
RL detected malicious code in a legitimate-looking Python package, aiocpa. That package had been
originally engineered as a legitimate crypto-client in order to attract a user base, only to have a
subsequent malicious-version update compromise cryptocurrency wallets using the client.[^2]

The firm Checkmarx reported in November 2024, on the open-source package @0xengine/xmlrpc, an
XML-RPC implementation that was first published in a benign, functional form in October 2023. As with
the aiocpa package, the malicious actors behind @0xengine/xmlrpc subtly altered their package in the
course of 16 updates, transforming it into a malicious tool capable of stealing secrets and sensitive data
while also mining cryptocurrency on infected systems.

Shortly after that, unknown malicious actors compromised the npm package @solana/web3.js, a
JavaScript API for use with the Solana blockchain platform, implanting malicious functions in two
versions of the package, which ranks among the top 10,000 projects in the npm community, with more
than 3,000 dependent projects generating 400,000 weekly downloads.[^3]

Incidents such as these underscore the growing sophistication and diversity of software supply chain
attacks and serve as a warning of what’s to come for other sectors. While typosquatting campaigns and
malware posted by sock puppet developer accounts are problems that won’t disappear anytime soon,
the past year’s attacks on cryptocurrency infrastructure and applications show that software supply
chain risks go well beyond malicious file dependencies to include sophisticated, long-horizon, hands-on-
keyboard attacks, with malicious actors cultivating users and code dependencies before flipping their
creation, or targeting high-profile projects and maintainers to blast malicious wares to thousands of
dependent applications and millions of developers.

[^1]: Karlo Zanki, “BIPClip: Malicious PyPI packages target crypto wallet recovery passwords,” ReversingLabs, March 12, 2024
[^2]: Karlo Zanki, “Malicious PyPI crypto pay package aiocpa implants infostealer code,” ReversingLabs, November 28, 2024
[^3]: Paul Roberts, “Malware found in Solana npm library raises the bar for crypto security,” ReversingLabs, December 5, 2024

7

©2025 ReversingLabs, Inc. — All Rights Reserved

<a name="focus-crypto-in-the-crosshairs"></a>
### Focus: Crypto in the Crosshairs

2024 saw a long list of software supply chain attacks targeting cryptocurrency applications and
infrastructure via open-source repositories. Looking at the findings from both RL’s threat research team
and other security firms, we counted 23 crypto-related malicious campaigns involving malicious code
being uploaded to open-source repositories. In the chart below, we categorize each of these discoveries
by the platforms they lived on.

Percentage of Total Malicious Crypto Campaigns Discovered

PyPI

39.1%

npm
60.9%

![Figure 1: Source of Malicious Open-Source Campaigns Targeting Cryptocurrency.]

Most of the malicious, crypto-related campaigns were on npm, which accounted for 14 of the 23
crypto-focused campaigns documented by security teams in 2024 (61%). Nine malicious campaigns
were found on the PyPI platform (39%), with attackers posting packages designed to target sensitive
cryptocurrency data and assets.

Two discoveries not included in the above chart are worth mentioning: the attack on the open-source
Tornado Cash platform,[^4] and the exploitation of Docker API.[^5] Both campaigns exhibited sophisticated
efforts by threat actors to either tamper with the platform’s source code or exploit misconfigurations that
gave bad actors access to carry out their malicious activities.

[^4]: Yehuda Gelb, “Tornado Cash Theft Uncovered: Malicious Code Drains Funds for Months,” Checkmarx blog, February 26, 2024
[^5]: Ravie Lakshmanan, “Cybercriminals Exploiting Docker API Servers for SRBMiner Crypto Mining Attacks,” The Hacker News, October 22, 2024

8

©2024 ReversingLabs, Inc. — All Rights Reserved

Check Out a Timeline of Crypto-Focused
Supply Chain Attacks in 2024

9

©2025 ReversingLabs, Inc. — All Rights Reserved

![Figure 2: Timeline of Crypto-Focused Supply Chain Attacks in 2024.]

<a name="the-xz-utils-backdoor"></a>
### The XZ Utils Backdoor

First disclosed in April, the backdoor in the widely used XZ Utils open-source compression library
(versions 5.6.0 and 5.6.1) was one of the most prominent supply chain compromises in recent memory.
The malicious code allowed attackers with a private key to gain unauthorized access to affected
Linux systems.

The hack hinged on a years-long, coordinated social-engineering campaign aimed at XZ Utils’ longtime
maintainer, Lasse Collin. That campaign featured several presumably phony developer accounts that
carried out a pressure campaign aimed at getting Collin to allow code contributions from “Jia Tan”
(JiaT75), a developer account that had become an active contributor to XZ Utils in the preceding
months. The campaign eventually saw Collin handing control of the XZ Utils project to Tan, who then
placed malware within the XZ Utils code.[^6]

“The most amazing thing about this campaign is how the legit developer was slowly but continuously
pushed to put maintenance rights into the hands of the threat actor behind this campaign,” said Karlo
Zanki, a threat researcher at RL.

<a name="state-actor-attacks-on-development-organizations"></a>
### State-Actor Attacks on Development Organizations

While the origin of the XZ Utils attack isn’t known, it points in the direction of another notable
development in the software supply chain threat space in 2024: efforts by state-backed threat actors to
infiltrate development organizations in the guise of legitimate software developers.

In recent months, RL threat researchers, along with those from other firms, uncovered evidence of active
campaigns by threat actors, likely linked to North Korea, to implant agents and code within development
organizations. The campaigns include efforts to push malicious code to developers in the form of
compiled Python (PYC) files that pose as developer skills tests given to candidates as part of phony
job interviews. In these attacks, threat actors use fake user accounts on business platforms such as
LinkedIn and pretend to be job recruiters from well-established companies. RL’s analysis of the files in
September 2024 showed a clear connection to the VMConnect campaign from 2023, also affiliated with
North Korea.[^7]

[^6]: Paul Roberts, “XZ Trojan highlights software supply chain risk posed by ‘sock puppets,” ReversingLabs, April 11, 2024
[^7]: Karlo Zanki, “Fake recruiter coding tests target devs with malicious Python packages,” ReversingLabs, September 10, 2024

10

©2025 ReversingLabs, Inc. — All Rights Reserved

<a name="serious-cyber-risks-lurk-in-commercial-binaries"></a>
## Serious Cyber Risks Lurk in Commercial
Binaries

Much of the conversation about software supply chain security focuses on the risks lurking within
open-source software packages — and the efforts by cybercriminals and nation-state actors to leverage
open source code and platforms to their advantage. But open-source software does not represent
the only risk in software supply chains — or even the most prominent. That risk lies in closed-source,
commercial software.

“They say the world runs on open source,” observes Saša Zdjlear, “but your business runs on commercial
software.”

<a name="commercial-binaries-what-you-dont-know-is-already-hurting-you"></a>
### Commercial Binaries: What You Don’t Know Is Already Hurting You

When it comes to commercial software, what you don’t know can — and will — hurt you. In fact, it already
is hurting you.

<a name="focus-commercial-softwares-seven-deadly-sins"></a>
### Focus: Commercial Software’s Seven Deadly Sins

Malware

Though less prevalent than
the other deadly sins of
commercial software, a number
of cybercriminal campaigns in
the last year implanted malware
in commercial applications such
as the Justice AV Solutions
(JAVS) video surveillance
software and iPany, a South
Korean made VPN client.[^8]

Tampering

Instances of unexplained
or malicious tampering are
relatively common in our scans
of commercial software binaries,
ranging from failed integrity
validation checks that flag
incomplete or corrupted file
content to suspicious callouts to
external command-and-control
(C2) infrastructure.

Improperly
implemented file-
hardening features

This covers a wide range of security
lapses often linked to hasty or
insecure development practices
such as poorly implemented address
space layout randomization (ASLR)
features, inadequate protections for
exploits such as buffer overflows,
and other security misconfigurations.

File rot

Old and outdated files were
common within the modules
we analyzed, including files
containing known, exploitable
vulnerabilities. Malicious
actors prey on older software
packages, since those are likely
to have known or undiscovered
security holes.

Exposed data

Commercial software binaries
that RL scanned were found
to harbor a large number of
sensitive software secrets,
including embedded and plaintext
credentials, API tokens, private
keys, and proprietary information
that can be abused
by threat actors to further
malicious activity.

Known and exploitable
or patch-mandated
vulnerabilities

RL detected more than 100 known,
exploitable vulnerabilities (KEV)
or patch-mandated vulnerabilities
spread across the packages we
analyzed.

Licensing issues

Many of the commercial software
binaries researchers scanned had
licensing compliance issues. For
example, code covered by “copyleft”
licenses was common. These can
expose organizations to legal liability
for copyright infringement or breach
of contract.

[^8]: Bill Toulas, “IPany VPN breached in supply-chain attack to push custom malware,” BleepingComputer, January 22, 2025

11

©2025 ReversingLabs, Inc. — All Rights Reserved

To illustrate that risk, RL analyzed 30, widely used commercial software binaries using Spectra Assure.
The applications we scanned included widely used commercial and open-source operating systems, web
browsers, and virtual private network (VPN) software.

Malware

Tampering

Vulnerabilities

Hardening

Secrets

Licenses

SBOM

Spectra Assure SAFE Report
Findings

As part of their research, RL’s experts scanned client executables as well as installer and setup files for
the applications in question. And, to be sure that the analysis captured risks that are likely to be present
in current enterprise environments, researchers limited themselves to files that were released within
the last three years. Evidence of one or more of the “seven deadly sins” was common, with many of the
scanned packages receiving a grade of “Fail” from Spectra Assure.

For example, our scans included 20 distinct versions of VPN clients from six, prominent vendors and
found worrying trends. Among them:

• Seven of the 20 VPN packages contained one or more software vulnerabilities that are patch-

mandated and/or that are being actively exploited by malware.

• Four of the 20 VPN packages we scanned contained exposed developer secrets - a popular target for

malicious actors.

• A recently released Windows VPN client from a prominent vendor contained more than 50 distinct

CVEs including:

• Four CVEs that are rated “critical” and actively exploited by malware, and another 12 assigned a

“high” criticality

• Vulnerabilities dating back as far as 2009  - all with patches available, but not applied by the vendor

in question

The prevalence of such severe software security issues — and the lack of attention they receive — shines
a spotlight on serious risks that hide in commercial software packages distributed to and deployed
within enterprises. Overlooked or disregarded by software producers and largely undetectable by their
customers, these flaws provide cybercriminal and nation-state actors avenues for both initial access to
sensitive networks and the lateral movement needed to carry out damaging offensive operations.

12

©2025 ReversingLabs, Inc. — All Rights Reserved

<a name="hack-of-javs-highlights-risks-lurking-in-commercial-apps"></a>
## Hack of JAVS Highlights Risks Lurking in
Commercial Apps

RL has opted to keep the names of the commercial vendors and applications we analyzed confidential.
However, our analysis of software named in the publicly disclosed breach of Justice AV Solutions (JAVS)
echoes and affirms many of the findings of our commercial software scans.

First detected in April 2024, the hack of the JAVS video-recording software involved malware placed
within an installer application that allowed malicious actors to take over systems running the JAVS
software[^9], which is used in courtrooms, legal offices, correctional facilities, and government agencies
around the world.

![Figure 3: Spectra Report on JAVS Viewer & Installer Showing the Presence of Malware.]

<a name="implanted-backdoor-delivers-rustdoor-malware"></a>
### Implanted Backdoor Delivers RustDoor Malware

Analysis conducted by the firm Rapid7[^10] determined that attackers compromised JAVS Viewer v8.3.7
with a backdoored installer that allowed attackers to gain full control of affected systems. The Trojan-
style installer contained malicious functionality embedded in the fffmpeg.exe file, with execution
triggered through the NSIS installer script. Once executed, the malware could bypass or disable security
features, including Anti-Malware Scan Interface (AMSI) and Event Tracing for Windows (ETW), before
downloading the intended payload, Rapid7 said in its report. Identified as the RustDoor/GateDoor
malware, it collects credentials and disables security measures.

RL performed a differential analysis of the JAVS installer using our Spectra solution to determine
whether any changes in the compromised installer were observable prior to release and deployment. The
scan produced a failing grade for the installer, with 34 separate security-related issues discovered.

[^9]: Sergiu Gatlan,