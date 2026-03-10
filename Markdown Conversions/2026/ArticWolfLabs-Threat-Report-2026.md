# Threat Report 2026

## Table of Contents
- [Foreword](#foreword)
- [Key Takeaways](#key-takeaways)
- [2026 Predictions Preview](#2026-predictions-preview)
- [Data Sourcing & Methodology](#data-sourcing--methodology)
- [The Threat Landscape in 2025](#the-threat-landscape-in-2025)
- [Ransomware Ecosystem Shifts](#ransomware-ecosystem-shifts)
- [Initial Access Trends](#initial-access-trends)
- [Edge Device Abuse & Infrastructure Exploitation](#edge-device-abuse--infrastructure-exploitation)
- [Trusted Platform & Supply Chain Abuse](#trusted-platform--supply-chain-abuse)
- [Ransomware Impact Analysis](#ransomware-impact-analysis)
- [Ransomware Economics & Extortion Trends](#ransomware-economics--extortion-trends)
- [2026 Predictions](#2026-predictions)
- [12 Recommendations for 2026](#12-recommendations-for-2026)
- [Conclusion](#conclusion)
- [How Arctic Wolf Can Help](#how-arctic-wolf-can-help)

---

## Foreword

The past year has reinforced a lesson defenders often learn the hard way: Attackers don’t need new tricks when the old ones still work. Whether it’s ransomware crews abusing remote access, social engineers weaponizing trust and timing, or affiliates pivoting to pure data theft when encryption loses its edge, the pattern is the same. Attackers follow the path of least resistance — and they follow it at scale.

From the vantage point of Arctic Wolf® Labs, where we analyze thousands of real-world intrusions, three signals stand out:

- Attackers are compressing the kill chain through automation
- They are bypassing controls by logging in, not breaking in
- They are exploiting identity, remote access, and trusted platforms long before they need an exploit

Most modern intrusions, in other words, are not technical surprises. They are architectural consequences.

This year, organizations that hardened remote access, segmented their environments, and invested in strong identity controls consistently stopped attacks that would have become headline-level incidents elsewhere. At the same time, threat actors continued to adapt — shifting toward data-only extortion, abusing trusted platforms and developer ecosystems, and operating with increasing speed and specialization.

That’s why this report matters. Its insights come not from hypothetical trends, but from the most disruptive incidents our teams were called in to contain and investigate — revealing how attackers actually behave under pressure, and which controls consistently buy defenders time.

If there’s one takeaway, it’s this: Defensibility beats novelty. Organizations that invested in the fundamentals — identity, segmentation, logging, disciplined remote access, and monitoring of trusted platforms — fared dramatically better, regardless of size or industry.

This report is designed to give you two advantages: better decisions and more time. You don’t need perfect security — you need defenses built for how attacks really unfold.

Think Red. Act Blue.

**Ismael Valenzuela**
Vice President of Labs, Threat Research & Intelligence, Arctic Wolf

---

## Key Takeaways

We understand that your time is in high demand, so for those readers in a rush, here’s a summary of this report’s major takeaways and predictions.

### 92%
**Three common cyber incident types account for 92% of Arctic Wolf IR cases**
Organizations typically reserve third-party IR engagements for only the most disruptive and damaging incidents, so it’s telling that our cases are dominated by ransomware (44% of cases), business email compromise (BEC) (26%), and data incidents (22%). While the relative contribution of ransomware and BEC to our caseload remained essentially consistent, data incidents surged 20% from our prior report, as cybercriminals adapt to improved organizational resilience and recovery capabilities by focusing solely on exfiltrating sensitive data and extorting victims to prevent publication.

### Improved defenses are stopping ransomware before detonation
Pre-ransomware incidents accounted for 5% of Arctic Wolf IR cases (in these incidents, an intrusion was detected and contained prior to detonation of what was later confirmed to be an attempted ransomware attack). In particular, behavioral analytics and endpoint telemetry allowed defenders to identify reconnaissance and privilege escalation attempts, and timely and effective response prevented ransomware detonation.

### 77%
**Professional incident response pays off**
Engaging with a ransomware actor is best left to the experts, as they generally have a great deal more experience with handling these events than any in-house personnel. In 77% of ransomware IR cases handled by Arctic Wolf, the impacted organization elected not to pay a ransom. In the 23% of ransomware IR cases in which the victim made the business decision to pay a ransom, Arctic Wolf’s IR team secured an average reduction (compared to the initial demand) of 67%. For larger organizations, this represents an important savings; for smaller organizations, it can be the difference between survival and insolvency.

### Blurred lines and shifting allegiances define the modern ransomware landscape
Ransomware groups continue to operate like profit-driven business enterprises, offering structured affiliate programs, tiered revenue models, and operational support to attract and retain a broader pool of cybercriminals. These developments have contributed to a more competitive and interconnected ecosystem, where the boundaries between distinct ransomware groups and brands are becoming increasingly difficult to delineate.

### 65%
**Attackers are abusing common remote access tools to gain initial access**
Nearly two-thirds of our non-BEC IR cases (65%) are attributable to abuse of external remote access products and services including remote desktop protocol (RDP), virtual private networks (VPN), and remote monitoring and management (RMM) tools. This dramatic surge from 24% just two years ago underscores a broader trend: Threat actors are increasingly prioritizing accessible and low-complexity entry points, rather than investing in sophisticated exploits.

### 85%
**To stop BEC fraud, invest in phishing defenses**
A whopping 85% of BEC fraud incidents were traced to email phishing, an 11% jump from last year’s report. As AI empowers threat actors to build efficient workflows and craft more convincing lures, robust phishing defenses — including security awareness training — are necessary for combating BEC.

### Prioritized patching remains effective, but don’t forget to rotate credentials
Each of the 10 CVEs we encountered in the majority of non-BEC IR cases date to 2024 or earlier, indicating that patching even just the most-exploited vulnerabilities can significantly improve an organization’s security posture. However, organizations must rotate credentials following any known vulnerability exposure, otherwise cybercriminals can simply return later and log in using stolen credentials.

### 180+
**Threat actors are targeting key roles by abusing trusted channels**
A number of campaigns (notably GPUGate, Oyster/Broomstick, and the compromise of 180+ npm packages) specifically targeted IT personnel and developers to gain initial access into organizations’ environments. Particularly in the second half 2025, threat actors employed SEO poisoning and trojanized tooling, and in 2026 they will likely explore generative engine optimization (GEO) and large language model (LLM) poisoning to directly surface malicious links in search engines’ AI summaries.

---

## 2026 Predictions Preview

Below, you’ll find summaries of our predictions for the near future (see “2026 Predictions” for full explanations):

1. Ransomware will remain the most significant threat, but data incidents may overtake BEC
2. Social engineers will increasingly incorporate real-time voice and video manipulation
3. AI will become less of a novelty tool for threat actors and more of an everyday utility
4. Information warfare will reach new heights
5. Threat actors will take advantage of major global events

---

## Data Sourcing & Methodology

The insights and data presented herein are drawn from 12 months of active global digital forensics and incident response (DFIR) engagements conducted by the Arctic Wolf Incident Response (IR) team. To enable the holistic analysis within this report, all data is aggregated without any identifying characteristics or attributes.

The IR case data is supplemented with telemetry from the Arctic Wolf Aurora Platform and insights from Arctic Wolf Labs: a cross-functional set of industry-leading professionals in threat intelligence, digital forensics, incident response, and experts in ransomware tactics and negotiations. Additionally, Arctic Wolf partnered with eCrime, ecrime.ch, for all leak site data and insights.

Unless otherwise stated, all data (e.g., from IR cases, leak site research, or other sources) pertains to the 12-month period running from November 1st, 2024, through November 1, 2025 (which we refer to as “this reporting period” or by similar language).

Any mention of “last year’s threat report” (or similar) is in reference to the Arctic Wolf 2025 Threat Report. Accordingly, analysis and explanations invoking a “report-over-report” change compare this 2026 Threat Report to the 2025 Threat Report.

### Case Classification

We classify cases by the focal point of the incident, or the best answer to the question, “What is the most impactful aspect of the attack?” This year’s report divides IR cases into six categories:

- **Ransomware**: Malware intended to render systems, services, data, and other assets unusable, usually via encryption.
- **Business email compromise (BEC)**: Email-borne phishing fraud in which a threat actor attempts to trick members of an organization into transferring funds, sensitive data, or something else of value.
- **Data incident**: A cyber incident involving unauthorized access to and/or exfiltration of potentially sensitive data, but without the use of ransomware or attribution to an insider threat.
- **Pre-ransomware**: Unauthorized activity/access that has not yet led to ransomware detonation, but which — via behavior; tactics, techniques, and procedures (TTPs); indicators of compromise (IOCs); or some other factor — is assessed with confidence to be part of a ransomware attack.
- **Malware**: Malicious software not directly associated with a ransomware or data incident. Examples include cryptocurrency miners, infostealers, and remote access trojans (RATs).
- **Other**: A catchall for incidents not attributable to one of the causes listed above. Examples include insider threats and distributed denial of service (DDoS) attacks originating from an external network (i.e., as opposed to denying service via ransomware encryption).

---

## The Threat Landscape in 2025

- **44%**: Ransomware continues its reign as the most common cause of IR cases: 44% of Arctic Wolf IR cases during this reporting period pertained to deployed/detonated ransomware, the fourth consecutive threat report where ransomware topped the list.
- **26%**: Business email compromise remains an all-too-common and impactful threat: BEC incidents represented 26% of Arctic Wolf IR cases this period, underscoring the staying power and costly impact of this often-misunderstood threat.
- **22%**: In lieu of operational disruption, some cybercriminals are specializing in data theft and extortion: Data incidents surged from 2% of IR cases in our prior report to 22% in this reporting period, as cybercriminals adapt to improved organizational resilience and recovery capabilities by focusing solely on exfiltrating sensitive data and extorting victims to prevent publication.
- **5%**: Improved detection capabilities are thwarting ransomware attacks before detonation: In 5% of Arctic Wolf IR cases, ransomware attacks were contained before the payload could be detonated, thereby preventing greater impact.

As we revealed in the Arctic Wolf 2025 Human Risk Report — which was based on a survey of more than 1,700 IT leaders and end users worldwide — 68% of IT leaders indicated that their organization “suffered a breach in the past year.”

However, not every breach is severe enough to require a full-scale incident response engagement, as mitigation strategies such as 24x7 managed detection and response (MDR) can quickly contain threats before they reach an enterprise-critical level.

This is why the majority of our IR engagements originate through our insurance provider relationships and privacy law practitioners, who are called in when incidents are so damaging and disruptive that they lead to insurance claims. Consequently, studying IR cases is an effective way to better understand the most dangerous threats.

![Chart: Arctic Wolf Incident Response Cases by Category]

> “We’re seeing a clear pivot in attacker behavior. As organizations improve their ability to recover from encryption events, some threat actors are skipping ransomware altogether and moving straight to data theft and extortion. From an incident response perspective, this shift fundamentally changes how impact is assessed and managed.”
> — **Kerri Shafer-Page**, VP of Incident Response at Arctic Wolf

### Ransomware and BEC remain the most common incidents

Although the threat landscape is shaped by a broad mix of actors, financially motivated cybercriminals are behind the majority of attacks severe enough to require help from an IR team. In this reporting period, ransomware (excluding pre-ransomware incidents, discussed below) and BEC incidents combined to account for 70% of our IR cases. For context, in the prior reporting period this figure stood at 71%, and two reports ago it was 78%.

#### Against headwinds, ransomware groups continue to wreak havoc
Ransomware accounted for 44% of our IR incidents — exactly the same portion as in our 2025 Threat Report. This dominance reflects the continued profitability and operational impact of ransomware attacks, which often force organizations into urgent response scenarios.

Notably, this is our third consecutive threat report in which ransomware has topped our IR charts, a streak that continues despite organizations’ improved ability to detect ransomware, a number of significant law enforcement takedowns, and a shifting ransomware ecosystem (see Ransomware Ecosystem Shifts).

The sectors with the most representation in our ransomware IR cases are:
1. Manufacturing
2. Legal
3. Education & Nonprofit
4. Finance & Insurance
5. Healthcare

#### BEC groups might not steal headlines, but they’re still stealing funds
Business email compromise also showed impressive year-over-year consistency, falling by only a single percentage point to 26% of cases. Again, this persistence comes despite BEC headwinds, including increased awareness and improved detection of email-borne threats.

Based on case investigations, Arctic Wolf IR experts believe some of the staying power of BEC can be attributed to the use of artificial intelligence (AI) to increase both the efficiency of an attack campaign (driving scale) and its effectiveness (i.e., through improved impersonation).

The most represented sectors within our BEC IR case catalog:
1. Finance & Insurance
2. Legal
3. Education & Nonprofit
4. Manufacturing
5. Business Services

---

## Ransomware Ecosystem Shifts

- **31.4%**: Akira, Fog, and Play continued as leaders: These three groups are the only holdovers from our previous threat report leaderboard, and collectively accounted for 31.4% of Arctic Wolf ransomware IR cases where confident attribution was possible.
- **Six ransomware groups climbed onto the leaderboard**: Underscoring the dynamism of the ransomware ecosystem, six groups (Qilin, RansomHub/DragonForce, INC, Silent Ransom, Lynx, and Rhysida) enjoyed enough success to emerge among the leaders.
- **Law enforcement takedowns made an impact**: LockBit, ALPHV/BlackCat, and BlackSuit were among the most successful ransomware groups in our previous threat report; but have fallen off the leaderboard in this reporting period.
- **Attribution is a growing challenge**: Between affiliate migrations, shifting partnerships, overlapping TTPs, frequent rebrands, and ongoing mergers and acquisitions, the shifting ransomware ecosystem is making firm attribution increasingly difficult.

### A maturing affiliate ecosystem
During this reporting period, we observed that ransomware groups are increasingly operating like business enterprises, offering structured affiliate programs, tiered revenue models, and operational support to attract and retain a broader pool of cybercriminals.

These developments have contributed to a more competitive and interconnected ecosystem, where the boundaries between distinct groups and brands are becoming increasingly difficult to delineate. This is especially true as individual groups may operate more than one brand, or even rebrand when necessary (e.g., Hunters International rebranded to World Leaks).

### Affiliate diversification
A prominent trend is the diversification of affiliate offerings. Ransomware-as-a-Service (RaaS) model — which typically offers affiliates up to 80% of ransom proceeds — remains foundational, many groups have expanded their services to include data extortion and access monetization.

These models allow affiliates to profit from stolen data or compromised credentials without necessarily deploying ransomware. Some groups now assist affiliates in publishing exposés of victim data or provide intelligence packages to help increase pressure during extortion. As with enterprise partner programs, these services often impose specific requirements, such as geographic restrictions or sector exclusions (e.g., healthcare), reflecting a more segmented and disciplined approach to operations.

### Blurring lines
Another noteworthy development is the increasing overlap between affiliates, infrastructure, and tactics across different ransomware brands. We have observed a number of cases in which threat actors seemingly operate across group boundaries, deploying one group’s ransomware while leveraging another’s infrastructure or negotiation channels.

This affiliate fluidity is further complicated by the evolution of community-driven collectives, such as The Com, also known as The Community. According to the FBI, The Com is an expansive global affiliation composed of several overlapping networks of criminals (primarily hackers, SIM swappers, and extortionists). Existing as a collective extends this group’s activities beyond the digital world and into areas such as violent crime as a service (e.g., shootings, robbery, assault, SWATing, crypto-related kidnappings, etc.).

---

## Initial Access Trends

- **65%**: Attackers are maliciously leveraging the very tools organizations deploy to secure remote access: 65% of this report’s non-BEC IR cases are attributable to abuse of external remote access products and services, including RDP, VPN, and RMM tools — a steady climb from just 24% three years ago.
- **11%**: External exploits remain a dangerous threat but are behind comparatively fewer cases: Perhaps due to improved patching programs, external exploits of known vulnerabilities for which patches were already available drove 11% of non-BEC IR cases, a sharp decline from 29% in the previous threat report.
- **85%**: BEC threat actors continue to have success with low-cost, low-complexity attack vectors: Among Arctic Wolf BEC IR cases with a confirmed root case, email phishing accounted for a whopping 85% of cases and previously compromised accounts or credentials drove 10%.

Where the root cause of an IR case can be determined, two conclusions stand out:
- Non-BEC incidents (e.g., ransomware, data incidents, pre-ransomware, and malware attacks) are mostly due to external remote access.
- BEC incidents are largely caused by phishing emails.

---

## Edge Device Abuse & Infrastructure Exploitation

- **Edge devices remain prime targets**: Owing to their exposure, inconsistent patching, and often weak credential hygiene, edge devices can provide an effective and stealthy means for attackers to gain access.
- **Skilled attackers can achieve full domain compromise in minutes**: Automation and operational maturity on the part of cybercriminals underscores the importance of highly effective detection, containment, and response capabilities.
- **Patching pays off**: While new exploits rightfully deserve attention, every single one of the CVEs we encountered the most in this report’s non-BEC IR cases dates from 2024 or earlier.
- **…But patching alone is insufficient if compromised credentials aren’t rotated**: Organizations must rotate credentials and audit access logs following any known vulnerability exposure, especially for edge devices that serve as entry points into the network, otherwise criminals can simply return later and log in using stolen credentials.

---

## Trusted Platform & Supply Chain Abuse

- **Threat actors are targeting high-value demographics by abusing trusted channels**: Compromising a developer or IT account or device can allow an attacker to bypass perimeter defenses and endpoint detection systems, and threat actors target these users through code repositories, SEO poisoning, and other trusted channels.
- **180+**: Self-replication is back: In a throwback to the early 2000s, a self-replicating malware campaign compromised over 180 npm packages, many of which were widely used in developer environments.

---

## Ransomware Impact Analysis

- **Manufacturers beware**: The manufacturing sector suffered, by far, the highest number of successful ransomware attacks (nearly 70% more than the second-place sector, construction).
- **Cybercriminals follow the money**: The top six countries represented on leak sites are all G7 nations, and are joined by other economic powers like Brazil, Spain, Australia, and India. Suspiciously absent? Russia and the CIS nations.

---

## Ransomware Economics & Extortion Trends

- **20%**: For the first time in the history of our threat report, the median initial ransom demand declined: After steadily growing for years and then staying flat for two reporting periods, the median initial ransom demand (across all industries) fell by 20% to $414,000 (USD), perhaps in an attempt to increase the overall rate of payouts.
- **77%**: Professional incident response should be a no-brainer: In 77% of ransomware IR cases handled by Arctic Wolf, the impacted organization elected not to pay a ransom.
- **67%**: Expertise in ransomware tactics and negotiation is invaluable: In the 23% of ransomware IR cases in which the victim made the business decision to pay a ransom, Arctic Wolf’s IR team secured an average reduction (compared to the initial demand) of 67%.

---

## 2026 Predictions

The predictions below highlight areas of concern, but please note that they’re not presented in a ranked or hierarchical order. We suggest determining the priority of each topic based on the specifics of your environment.

1. **Ransomware will remain the most significant threat, but data incidents may overtake BEC**
2. **Social engineers will increasingly incorporate real-time voice and video manipulation**
3. **For threat actors, AI will become less of a novelty tool and more of an everyday utility**
4. **Information warfare will reach new heights**
5. **Threat actors will take advantage of major global events**

---

## 12 Recommendations for 2026

As we’ve seen, the threat landscape continued to evolve during the timeline of this report, with attackers leveraging both traditional and modern techniques across hybrid environments. Consequently, these 12 recommendations are designed to help organizations reduce risk and improve resilience, while retaining the ability to adapt in response to ever-changing threats.

1. **Minimize internet exposure**
2. **Implement robust identity controls**
3. **Prioritize vulnerability management**
4. **Segment your network**
5. **Enhance logging and monitoring**
6. **Strengthen phishing defenses**
7. **Rotate credentials regularly**
8. **Develop an incident response plan**
9. **Invest in security awareness training**
10. **Secure remote access tools**
11. **Audit supply chain dependencies**
12. **Engage with professional IR services**

---

## Conclusion

The threat landscape of 2025 was defined by the persistence of ransomware, the evolution of extortion tactics, and the strategic abuse of trusted platforms. As we look toward 2026, the challenges will only grow in complexity. However, by focusing on the fundamentals of defensibility—identity, visibility, and rapid response—organizations can effectively mitigate these risks and build a more resilient future.

---

## How Arctic Wolf Can Help

Arctic Wolf provides the security operations, incident response, and threat intelligence necessary to protect your organization in an increasingly hostile digital landscape. Our team of experts is ready to help you defend against the threats of today and prepare for the challenges of tomorrow.

©2026 Arctic Wolf Networks, Inc. All rights reserved. | Public ARCTIC WOLF | 2026 THREAT REPORT

---

ives, or other motivations
can cause network perimeters to become cluttered with outdated or redundant systems, creating easy entry points for
attackers.

•  Decommission unused systems: Remove temporary, duplicate, or end-of-life infrastructure

•  Disable unnecessary services: Turn off legacy protocols, unused VPN types, and features not essential to operations

2

Prioritize patching in general, and vulnerability management specifically

As we’ve seen, edge devices such as firewalls and VPNs are high-value targets due to their privileged access and
limited visibility (e.g., gaps in monitoring, opaque proprietary systems, excessive noise).

•  Patch known exploited vulnerabilities: Focus on flaws actively used in attacks, as most already have fixes available

•  Maintain a complete asset inventory: Visibility is key to prioritizing patching and reducing risk

•  Secure management interfaces: Ensure they are isolated from public access and properly configured

•  Subscribe to advisories: Use vendor updates and CISA’s Known Exploited Vulnerabilities (KEV) catalog to stay

ahead of emerging threats

•  Reset credentials after patching: Rotate passwords and keys if a vulnerability may have exposed them

•  Keep firmware updated: Firmware updates often include critical security improvements not covered by

standard patches

3

Harden infrastructure

Strengthen infrastructure to increase resilience and improve defense-in-depth.

•  Restrict admin access: Block internet-facing management interfaces and limit access to trusted internal networks

•  Apply IP-based filtering: Allow access only from known safe regions and IP ranges

•  Filter botnet traffic: Use vendor-provided rules to block known, malicious sources

•  Enforce strong encryption: Use secure standards like AES-256 and disable outdated cipher suites

26

©2026 Arctic Wolf Networks, Inc. All rights reserved.  |  Public ARCTIC WOLF   |   2026 THREAT REPORT4

Strengthen authentication controls

Credential-based attacks remain a favorite tactic of threat actors, but correctly implementing strong authentication
controls reduces the risk of unauthorized access.

•  Centralize authentication: Use SSO and SAML to manage access through trusted identity providers (IdPs)

•  Audit VPN accounts: Regularly review user lists and remove access for inactive users and third parties

•  Require strong multi-factor authentication (MFA): Use phishing-resistant methods (e.g., hardware tokens) backed

by modern WebAuthn standards

•  Promote credential hygiene: Enforce strong passwords (i.e., long and not guessable), password rotation, and

password manager usage

5

Monitor and log strategically

Visibility into edge devices and user activity is essential for detecting and responding to threats.

•  Log as much as is possible (or practical): If you’re working with a solution or solution provider that can

accommodate high data volume without incurring/imposing punitive costs, then log everything — otherwise,
prioritize logs that provide visibility not available from other systems

•  Centralize log collection: Send logs to external systems to prevent tampering and to support investigations

•  Deploy behavioral analytics: Detect lateral movement and persistence techniques that bypass traditional controls

6

Promote safe software practices

User behavior can introduce risk, especially when downloading tools from unverified sources (or simply by being tricked).

•  Educate users: Raise awareness about the risks of downloading software from search engines or unofficial sites,

and teach users to be vigilant of watering hole-style attacks (e.g., malvertising, typo squatting)

•  Enforce acquisition policies: Require software to be sourced through approved internal or vendor channels

7

Monitor trusted platform abuse

Attackers increasingly use legitimate platforms to distribute malicious content or to hide malicious activity.

•  Watch for misuse of platforms: Monitor traffic and usage patterns involving GitHub, Google Ads, and IT tool repositories

•  Understand your own dependencies: A supply chain compromise might affect your organization via a dependency chain

27

©2026 Arctic Wolf Networks, Inc. All rights reserved.  |  Public ARCTIC WOLF   |   2026 THREAT REPORT8

Manage third-party risk

Third-party vendors and service providers often have access to sensitive systems and data, making them attractive targets.

•  Assess vendor security posture: Include security requirements in contracts and conduct regular reviews

•  Limit and monitor access: Apply least-privilege access principles and segment external connections to reduce risk

9

Implement network segmentation and zero trust principles

Flat networks make it easier for attackers to move laterally once inside.

•  Segment critical systems: Isolate sensitive environments from general user networks

•  Adopt zero trust: continuously verify access requests and monitor trust levels

10

Prepare for incident response and recovery

Being prepared for incidents reduces impact and recovery time.

•  Maintain and test IR plans: Ensure playbooks are current and exercised regularly

•  Protect and test backups: Ensure backups are secure, reliable, and recoverable

•  Define communication protocols: Include internal teams, legal counsel, and external stakeholders in planning

11

Leverage threat intelligence

Timely, relevant intelligence helps security teams anticipate and respond to threats more effectively.

•  Operationalize threat intelligence: Integrate feeds into SIEM, SOAR, and detection workflows

•  Use contextual enrichment: Apply intelligence to prioritize alerts and guide investigations

•  Collaborate with trusted sources: Participate in Information Sharing and Analysis Centers (ISACs) or similar

industry-specific sharing groups

12

Continually foster a security-aware culture

Technology alone isn’t enough: people play a critical role in defense.

•  Run regular awareness campaigns: Focus on phishing, social engineering, and secure behaviors

•  Tailor training to roles: Provide specialized guidance for high-risk groups like IT admins or finance teams

•  Encourage reporting: Make it easy and safe for employees to report suspicious activity

28

©2026 Arctic Wolf Networks, Inc. All rights reserved.  |  Public ARCTIC WOLF   |   2026 THREAT REPORTConclusion

Most threat actor groups are financially motivated operations,
and changing their ROI calculations is essential for protecting
your organization.

One problem we encounter when preparing our

But defenders must also augment these

annual threat report is trying to avoid restating

proactive measures with:

the phrase "threat actors continue…” in one form

or another dozens of times.

• Reactive capabilities designed to quickly and

effectively detect and respond to attacks that

The reason for this problem? Threat actors

break through outer defenses.

continue to stick with what works. Finding

vulnerabilities, crafting exploits, and weaponizing

them at production scale is time-consuming,

expert-driven, and expensive work. That means

it’s much cheaper to stick with tried-and-true

TTPs. Only when these offer scarce returns will a

group be motivated to build or buy some hot new

exploit or develop a new attack chain.

For cyber defenders, this means that protecting

against known TTPs (including CVEs that have

been exploited for literally years) can make your

organization a much more challenging target.

Nevertheless, preventative measures are what

engineers call “necessary but insufficient.”

Yes, defenders must build and maintain a

foundation of fundamentals and continually adapt

and evolve their security posture such that, over

time, those novel defenses are integrated into the

new normal.

• Robust and reliable backup and restoration

capabilities to enable fast and full recovery

(and to help avoid paying ransoms).

• Risk transfer measures, including leveraging

warranties and insurance, in response to the

reality that incidents do happen (even to well-

prepared organizations).

It can all seem overwhelming — but you’re

not alone.

An entire cybersecurity community stands with

you and is committed to sharing and learning,

lifting and helping, and working together to

withstand attacks and intrusions.

If you’d like to augment your internal capabilities

with external expertise, we’re ready for you to join

the Pack.

29

©2026 Arctic Wolf Networks, Inc. All rights reserved.  |  Public ARCTIC WOLF   |   2026 THREAT REPORTHow Arctic Wolf Can Help

The outcomes you need, the convenience you’ll love.

When we speak with organizations around the world, we’re often asked for three things:

1

2

3

An effective cybersecurity solution that will provide end-to-end protection against cyber threats, that

will be easy to manage, and that will integrate with the security products they’ve already deployed.

A way to financially offset the remaining risk.

Expert assistance to help evolve their security posture over time, aligned with their specific

priorities and operating context.

In response, we’ve created the Arctic Wolf Security Operations Bundles.

These bundles provide the full suite of technology, security expertise, and risk transfer options to help you
End Cyber Risk®.

Whether it’s proactive security offerings like security awareness training, vulnerability scanning, and incident
readiness planning; or reactive detection, remediation, and active response capabilities to minimize the severity
of an incident, the Security Operations Bundles provide full coverage across all your attack surfaces.

Best of all, some of the remaining risk may be financially transferred to Arctic Wolf through our industry-leading
Security Operations Warranty. With up to $3 million (USD) in financial coverage and the ability to fund your
cyber insurance deductible, your out-of-pocket costs after a severe cyber attack may be mitigated.

If you aren’t getting the outcomes you’re looking for from the solutions you have today — or if you just need some
support in putting your existing investments to work — we would love to help.

For more information about Arctic Wolf, visit arcticwolf.com

About Arctic Wolf

Arctic Wolf® is a global leader in security operations, delivering the first cloud-native security operations platform
to end cyber risk. Built on open XDR architecture, the Arctic Wolf Aurora™ Platform operates at a massive scale and
combines the power of artificial intelligence with world-class security experts to provide 24x7 monitoring, detection,
response, and risk management. We make security work.

Arctic Wolf and its employees are not licensed producers and therefore are not engaging in the sale, solicitation or negotiation of insurance and are NOT offering advice regarding
insurance terms, conditions, premium rates or claims. Customers interested in purchasing Cyber Insurance coverage should consult with an appropriately licensed insurance broker.

Informational Use Only. This content is for general information and does not constitute legal, accounting, or other professional advice.

No Warranty/No Reliance. It is provided “as is” without warranties of any kind; do not place undue reliance on a single metric or example.

Methodology & Scope. Statistics reflect Arctic Wolf engagements and telemetry for the period [November 1, 2024–November 1, 2025], may be influenced by case mix (e.g.,
insurer/counsel referrals), and may differ from broader market experience. Sanctions/Payments. Any engagement with threat actors may implicate sanctions or other laws. Arctic
Wolf does not advise paying ransoms; decisions rest with the customer in consultation with counsel and relevant authorities.

The predictions and outlooks in this publication reflect Arctic Wolf’s observations and analyst judgment as of January 2026. They are inherently uncertain and involve assumptions
about attacker behavior, technology adoption, regulation, and macro conditions. They are not guarantees of future events, may change without notice, and we undertake no
obligation to update them. Readers should not rely on any single prediction and should consider alternative scenarios and local legal constraints.

©2026 Arctic Wolf Networks, Inc., All Rights Reserved. Arctic Wolf, Arctic Wolf Platform, Arctic Wolf Security Operations Cloud, Arctic Wolf Managed Detection and Response,
Arctic Wolf Managed Risk, Arctic Wolf Managed Security Awareness, Arctic Wolf Incident Response, and Arctic Wolf Concierge Security Team are either trademarks or registered
trademarks of Arctic Wolf Networks, Inc. or Arctic Wolf Networks Canada, Inc. and any subsidiaries in Canada, the United States, and/or other countries.

AW_RP_2026 THREAT REPORT_0226ARCTIC WOLF   |   2026 THREAT REPORT