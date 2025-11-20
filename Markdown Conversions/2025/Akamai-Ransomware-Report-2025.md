# AI Instruction Set for Converting Technical PDFs to Markdown

## Purpose
Ensure technical PDFs are converted to Markdown with complete fidelity, preserving all content, structure, and formatting.
## Goals
1. **Full Conversion**: Include all text, quotations, footnotes, references, and technical terminology without omission or summarization.  
2. **TOC Format**: Include a fully functional Table of Contents with proper linking.  
3. **Markdown Conventions**: Use clear, consistent, and professional formatting.  
4. **Images**: Describe image contents without embedding.
## Conversion Instructions
### Content
- **Include All Text**: Retain all sections, preserving the original structure and content.  
- **Headings**: Format with `#` for main headings, `##` and `###` for subheadings.  
- **Lists**: Use `1.` for ordered lists, `-` for unordered lists.  
- **Emphasis and Formatting**: Apply `_italic_`, `**bold**`, `>` for block quotes, and \`\`\` for code blocks.  
- **Links**: Format as `[text](URL)` and ensure accuracy.
### Images
- **Do Not Embed**: Replace with descriptive text: `![Image description]`.
### Table of Contents
- Place after the document title but before the main content:
  ## Table of Contents
  - [Section Title](#section-title)
  - [Subsection Title](#subsection-title)
- Ensure anchor links work and follow the format `(#section-title)`.
### Footnotes and References
- Use Markdown footnote syntax:  
  Content with a footnote[^1].  
  [^1]: Footnote content here.
- Retain all technical and academic terms exactly.
## Verification and Quality Assurance
1. **Accuracy**: Verify the entire document is converted without omissions.  
2. **TOC Functionality**: Check all links point to the correct headings.  
3. **Readability**: Ensure professional formatting and adherence to Markdown standards. DO NOT enclose the top and bottom of the content in ```markdown and ``` . 
4. **Fidelity**: Confirm the output matches the original PDF exactly.  
---
# Report Content Below

The official report URL is: https://www.akamai.com/lp/soti/ransomware-trends-2025

# Report Content Below

# Ransomware Report 2025

V11 ISSUE 03

Building Resilience Amid a Volatile Threat Landscape

State of the Internet/Security

## Table of Contents
- [Introduction](#introduction)
- [Key insights of the report](#key-insights-of-the-report)
- [Overview of attack patterns and the impact on customers](#overview-of-attack-patterns-and-the-impact-on-customers)
- [Evolving extortion tactics](#evolving-extortion-tactics)
- [Inside the RaaS ecosystem](#inside-the-raas-ecosystem)
- [Putting the RaaS in hacktivism](#putting-the-raas-in-hacktivism)
- [Security spotlight: A malicious treat with TrickBot (Guest contributor: Or Zuckerman)](#security-spotlight-a-malicious-treat-with-trickbot-guest-contributor-or-zuckerman)
- [Industry trends](#industry-trends)
- [Security spotlight: Cryptominers (Guest contributor: Maor Dahan)](#security-spotlight-cryptominers-guest-contributor-maor-dahan)
- [The impact of ransomware attacks on operational continuity](#the-impact-of-ransomware-attacks-on-operational-continuity)
- [Security spotlight: Ransomware and the law (Guest contributor: James A. Casey)](#security-spotlight-ransomware-and-the-law-guest-contributor-james-a-casey)
- [Building ransomware resilience around the world](#building-ransomware-resilience-around-the-world)
- [Mitigation](#mitigation)
- [Conclusion](#conclusion)
- [Methodology](#methodology)
- [Guest contributors](#guest-contributors)
- [Credits](#credits)

## Introduction
The ransomware landscape has grown even more complex and volatile in 2025.

Groups like FunkSec and Black Basta have reportedly used generative artificial

intelligence (GenAI) and large language models (LLMs) to create ransomware code

and enhance their social engineering attacks, respectively. Although adversaries

are using multiple extortion techniques — sometimes even quadruple extortion —

double extortion remains the attackers’ favored method. Despite high-profile law

enforcement takedowns, threat actors show strong resilience — regrouping,

rebranding, or forming new groups to quickly fill any vacuum created by the

dissolution of a dominant group.

### How attackers are harnessing AI and LLMs
Adversaries are rapidly integrating AI and LLMs to increase the scale, sophistication,

and efficiency of their operations. Ransomware groups such as FunkSec use GenAI to

generate malicious code, create new ransomware variants, and deploy chatbots to

negotiate with victims. Attackers also employ AI to craft convincing phishing emails

and conduct voice phishing (“vishing”) attacks that impersonate company personnel.

Advanced persistent threat groups have also begun using GenAI on a limited scale.

Forest Blizzard (aka Fancy Bear) and Emerald Sleet reportedly leveraged LLMs to

mimic official documents in phishing campaigns and to conduct vulnerability research,

respectively, and emerging tools like WormGPT, DarkGPT, and FraudGPT are helping

cybercriminals increase both the scale and effectiveness of their attacks.

### Adding distributed denial of service to the extortion mix
Beyond traditional encryption, attackers are also deploying sophisticated multi-extortion

methods that create compound pressure points. Simultaneous encryption, data theft,

and distributed denial-of-service (DDoS) threats give attackers more leverage against

organizations. To maximize profits, some ransomware groups auction off stolen “crown

jewels” or confidential company data to the highest bidders on dark web marketplaces.

[Akamai.com](https://www.akamai.com/)   |   2

Ransomware Report 2025  I  Volume 11, Issue 03

### The fading line between cybercrime and hacktivism
While the majority of ransomware groups primarily pursue financial extortion, traditional

boundaries between profit-driven cybercrime and ideologically motivated hacktivism are

dissolving in troublesome ways. Ransomware as a service (RaaS) relies on a wider criminal

ecosystem that consists of developers, affiliates, the zero-day market, and initial access

brokers who are key to orchestrating attacks. The broader criminal ecosystem has become

a service industry, with criminal groups building their brands or specializing in functions like

money laundering. RaaS groups with hacktivist motivations are using ransom payments to

fund their campaigns to advance ideological or political objectives. Moreover, hacktivists such

as Head Mare, Twelve, and NullBulge have adopted ransomware tactics to cause greater

disruption in the countries they are targeting, which further complicates the threat landscape.

### Partners join the fight against ransomware
As organizations become more cyber resilient by putting a Zero Trust architecture and other

security controls in place, they are better positioned to proactively mitigate ransomware. But

they need more help, and it’s beginning to arrive. Public—private partners of defenders and

law enforcement are sharing threat intelligence and best practices and making a difference.

Since 2022, FBI-provided decryption keys have saved victims more than US$800 million in

payments. Governments are also introducing legislation aimed at banning organizations

from paying threat actors. These policies benefit organizations since paying the ransom

does not ensure the return of their data. Finally, cyber insurance providers are incentivizing

organizations to strengthen security programs and offering their negotiating skills to lower

ransomware payments.

### Akamai’s thought leadership and research
Akamai security research is committed to shining a light on the cybercriminal ecosystem by

analyzing the emerging techniques used by adversarial groups. In this State of the Internet

(SOTI) report, we spotlight two key threats:

- TrickBot malware, which is leveraged by certain ransomware groups,

including Ryuk, Conti, and Diavol
- Cryptominers, which our researchers have identified as one of the critical

intersection points within the ransomware landscape because their goals and

strategies are similar to those of ransomware groups

Additionally, our threat experts provide strategic, actionable insights that empower security

leaders and defenders to fortify organizational resilience, deploy robust protection, and

proactively counter today’s increasingly sophisticated ransomware threats.

[Akamai.com](https://www.akamai.com/)   |   3

Ransomware Report 2025  I  Volume 11, Issue 03

## Key insights of the report
- Ransomware extortion tactics have been evolving. Quadruple extortion is the

newest tactic, while double extortion is currently the most common tactic.

And ransomware groups continue to seek additional ways to generate profit,

such as by pressuring victims and weaponizing compliance.
- More than US$724 million in cryptocurrency was extorted from strains linked

to the TrickBot malware family, which is used by ransomware groups. The Akamai
Hunt Team recently observed this malware in connection with four malicious

scheduled tasks on five customer assets.
- GenAI and LLMs increase the frequency and scale of ransomware attacks

by enabling individuals with less technical expertise to launch sophisticated

campaigns, as demonstrated by groups like FunkSec.
- The emergence of hybrid ransomware hacktivist groups that are leveraging

RaaS platforms to amplify impact (e.g., CyberVolk, Stormous, KillSec,

Dragon RaaS, and DragonForce) demonstrates a significant shift in the

ransomware landscape in which political and ideological motives are

becoming more intertwined with financial crime.
- The hacktivist groups Head Mare, Twelve, and NullBulge often use LockBit

ransomware (built from leaked or publicly available builders) for political disruption.

NullBulge specifically uses it to target online communities and platforms that

are operating with AI and online gaming tools.
- Although cryptominers pose a unique danger, their goals and the strategies

they employ are similar to those of ransomware groups. Notably, nearly 50%

of the cryptomining attacks we analyzed targeted nonprofit and educational

organizations, likely because they possess substantial computational resources

and are less secure than other industries.

[Akamai.com](https://www.akamai.com/)   |   4

Ransomware Report 2025  I  Volume 11, Issue 03

## Overview of attack patterns
and the impact on customers

Akamai research has observed a concerning trend: Multiple ransomware groups are

increasingly targeting the same organizations simultaneously, heightening the risks to those

organizations. Additionally, our research revealed significant fluctuations, with noticeable

peaks and valleys in the number of global customers targeted by ransomware during 2024

(Figure 1). These fluctuations may also be evidence of volatility within and among the major

ransomware groups, which frequently dissolve into smaller operations or rebrand in
an effort to evade law enforcement and remain undetected.

![Figure 1: The number of global customers targeted by ransomware attacks]

Fig. 1: The number of global customers targeted by ransomware attacks

The ransomware activity and trends we see regionally (Figure 2) mirror the global

patterns in Figure 1.

![Figure 2: The number of customers in the Asia-Pacific (APAC) and Europe, the Middle East, and Africa (EMEA) regions targeted by ransomware attacks]

Fig. 2: The number of customers in the Asia-Pacific (APAC) and Europe, the Middle East,
and Africa (EMEA) regions targeted by ransomware attacks

[Akamai.com](https://www.akamai.com/)   |   5

Ransomware Report 2025  I  Volume 11, Issue 03

In 2024, ransomware spiked by 37%, accounting for 44% of the data breaches globally and

for 51% in Asia-Pacific (APAC), according to the Verizon 2025 Data Breach Investigations

Report. In Europe, the Middle East, and Africa (EMEA), the proportion of enterprises that

experienced a ransomware attack grew to 27% in 2024. And in Latin America (LATAM),

29% of enterprises reported an attack in 2024, with a growing wave targeting small and

medium-sized businesses.

To mitigate these risks, companies should prioritize strengthening their cyber resilience.

This includes implementing segmentation to contain the attack and prevent threat actors

from moving laterally within the network to compromise sensitive data.

## Evolving extortion tactics
Ransomware extortion tactics have been evolving from single extortion (which is intrinsic to

all traditional ransomware operations) to double extortion (e.g., the Maze ransomware group

in 2019) to triple extortion (notably with the ALPHV/BlackCat in 2021) to quadruple extortion

(e.g., CL0P in 2024; Figure 3).

![Figure 3: Ransomware extortion tactics]

 Fig. 3: Ransomware extortion tactics

[Akamai.com](https://www.akamai.com/)   |   6

Ransomware Report 2025  I  Volume 11, Issue 03

This evolution of tactics has proven effective for ransomware groups, resulting in escalated

average ransom payments. While triple and quadruple extortion are growing more frequent,

double extortion still appears to be the most common tactic (Figure 4). And a new trend

among ransomware groups that are using double and quadruple extortion tactics is the

use of government regulations as leverage.

![Figure 4: Akamai researchers have observed these ransomware groups employing various extortion tactics]

Fig. 4: Akamai researchers have observed these ransomware groups
employing various extortion tactics

The three groups that have historically been among the most prominent ransomware groups

— ALPHV/BlackCat, CL0P, and LockBit — have all conducted quadruple extortion. And in

February 2025, CL0P claimed responsibility for 385 attacks in just a few weeks, setting a new
record for the most attacks ever attributed to a single group in one month. CL0P remains the

most stable group of the three, given last year’s shutdowns of ALPHV/BlackCat and LockBit.

This is despite LockBit’s return, which later led to the fragmentation of the group, its code

being widely reused by others, and, most recently, the group being hacked.

Yet, the ransomware landscape has been shifting significantly over recent months with

new and emerging groups becoming major threats. Similar to ALPHV/BlackCat, CL0P, and

LockBit, many of these newer groups are also weaponizing compliance regulations as part

of their tactical approach, whether implicitly (e.g., double extortion) or more explicitly (similar

to ALPHV/BlackCat). Regardless, organizations need to be vigilant of such tactics and remain

aware and in compliance with specific regulations regarding ransomware attacks.

[Akamai.com](https://www.akamai.com/)   |   7

Ransomware Report 2025  I  Volume 11, Issue 03

### Notable groups within regions
The most active groups in regions outside of North America include the top variants reported

to the FBI’s Internet Crime Complaint Center (IC3) in 2024 — Akira, LockBit, RansomHub, and

Play — which underscores their global dominance. As an example, from 2024 through early

2025, Akamai researchers confirmed that LockBit was a persistent threat in APAC (surging

in October 2024) and EMEA, despite having experienced various disruptions (Figure 5).

![Figure 5: LockBit remained an active threat in APAC and EMEA from January 2024 to May 2025]

Fig. 5: LockBit remained an active threat in APAC and EMEA from January 2024 to May 2025

(Note: The decrease in April 2025 is not an accurate representation; there was a data collection issue at this time.)

[Akamai.com](https://www.akamai.com/)   |   8

Ransomware Report 2025  I  Volume 11, Issue 03

#### Active groups in APAC
In APAC, well-known global ransomware syndicates such as LockBit, ALPHV/BlackCat,

and CL0P are active, as are newer groups such as Royal/BlackSuit, RansomHub, Akira,

Abyss Locker, and Play.

Abyss Locker leaked 1.5 terabytes of data from the Australian Nursing Home Foundation.

And a Singapore-based law firm reportedly paid nearly US$1.9 million in a sophisticated

ransomware attack by the Akira group.

Other regionally active threat actors also have had an impact across APAC. Termite

(a Babuk affiliate) and Anubis actively targeted victims across the APAC region over
the past year. Notable incidents include a ransomware attack on an Australian in vitro

fertilization clinic in early 2025 by Termite, and Anubis’s exfiltration and public release

of sensitive patient records from multiple Australian medical clinics.

#### Active groups in EMEA
In EMEA, LockBit, RansomHub, Medusa, and Akira are some of the most active groups.

January 2025 started with Medusa posting stolen documents from a U.K. government

agency on a leak site. Akira published a list of data leakages impacting organizations across

the region. Other public reports of specific incidents by these groups include an attack on

a German manufacturer, a wave of attacks in Italy, and strikes against the industrial control

systems of an energy plant in Spain.

A spate of attacks against U.K. retailers has been attributed to both Scattered Spider,

a known affiliate of RansomHub, and DragonForce, which claims to be taking over

RansomHub’s infrastructure. Additionally, amid various takedowns by authorities and

attacks by rival groups, LockBit and Black Basta have used adaptability and shifting

tactics to maintain operations.

#### Active groups in LATAM
In LATAM, RansomHub, FunkSec, and Akira have been the most active ransomware groups

recently. In one month, Akira led the number of LATAM extortion disclosures with six

victims in Brazil, two in Argentina, and two in Colombia. Akira was also behind the notable

2024 attack against a LATAM airline. RansomHub activity included an attack against a

government office in Mexico. Medusa is also having an impact, with a breach against

a financial solutions provider in Brazil.

[Akamai.com](https://www.akamai.com/)   |   9

Ransomware Report 2025  I  Volume 11, Issue 03

### Regulation violation revelation: A trending threat
Recently, we’ve seen a growing trend in ransomware groups’ threats to reveal that a company is

in violation of regulations. This tactic raises the stakes on reputational damage to the brand and the

potential cost of the attack (adding fines from regulators and legal fees). But weaponizing compliance

is not entirely new. For example, in December 2019, REvil posted on a Russian hacker forum that if

companies refused to pay ransom, then their data breach disclosures could lead to severe regulatory fines,

potentially 10 times more than the ransom demand itself.[^1] Also, near the end of 2023, the ALPHV/BlackCat

ransomware group submitted a formal complaint to the U.S. Securities and Exchange Commission (SEC)

against a digital lending solutions provider, alleging that the company failed to disclose a cybersecurity

breach within the required time frame.

The Anubis ransomware group (which began operations in late 2024) often highlights regulatory violations,

such as for healthcare privacy breaches, to shame organizations publicly (e.g., via the social platform X, a

leak site, or direct communication) and thus focuses its efforts on industries in which compliance risks are

high (e.g., healthcare and engineering). Also, RansomHub (which was first detected in February 2024) has

become a major threat with its high-profile ransomware attacks and rapid growth. This group has explicitly

encouraged affiliates to leverage the threat of regulatory penalties (e.g., the General Data Protection

Regulation [GDPR], the Personal Information Protection Law [PIPL], and the Personal Data Protection

Law [PDPL]) to increase pressure on victims. The ransomware group known as WereWolves (which

emerged in May 2023) also weaponizes compliance in addition to using other aggressive tactics (e.g.,

double extortion, use of LockBit 3.0, and public communication with victims) on their targets.

The impact of these regulation violation threats has been felt worldwide, as Anubis, RansomHub,

WereWolves, and ALPHV have explicitly threatened victims by weaponizing compliance (Table 1).

| Ransomware Group | Regions Targeted | Industries Targeted | Regulatory Exposure (Laws/Regulations Threatened) | Where Threatening to Report |
|---|---|---|---|---|
| Anubis | Global, especially U.S. and Europe | Healthcare, government | HIPAA (U.S.), GDPR and Data Protection Act 2018 (U.K.),  and GDPR (EU) | U.S. Department of Health and Human Services (HHS), U.K. Information Commissioner's Office (ICO), and European Data Protection Board (EDPB) |
| RansomHub | Global, especially Europe, China, and Saudi Arabia | Spread widely across industries with concentration in IT and critical infrastructure | GDPR (EU), PIPL (China), and PDPL (Saudi Arabia) | EDPB, Cyberspace Administration of China (CAC), and the Saudi Data and Artificial Intelligence Authority (SDAIA) |
| WereWolves | Russia, Europe, North America, and Africa | Spread widely across industries with concentration in IT, financial services, and hospitality | Not specific but likely to threaten: GDPR (EU) ePrivacy (EU), GLBA (U.S.), SEC rules (U.S.), Federal Law 152-FZ (Russia), Data Protection Act, 2012 (Act 843; Ghana) | Not specific but likely to threaten: National Data Protection Authorities (DPAs), SEC, Roskomnadzor, and Data Protection Commission |
| ALPHV (ceased operations in 2024) | Global, especially U.S. | High technology and healthcare | SEC (U.S.) disclosure rules and HIPAA (U.S.) | SEC and HHS (U.S.) |

Table 1: Ransomware groups that are weaponizing compliance

[^1]: The message stated, “GDPR. Do not want to pay us – pay x10 more to the government. No problems.”

[Akamai.com](https://www.akamai.com/)   |   10

Ransomware Report 2025  I  Volume 11, Issue 03

Note that the list in the table only details specific regulation threats received. It’s

likely that these groups weaponize other regulations in other regions as well. Even

if these groups only engage in double extortion and don’t go to the authorities, they

are exposing sensitive information that may trigger regulation violations for the

victim anyway. That’s why we included the other potential regulation violations that

may be exposed (such as those triggered by WereWolves) and their associated

governing authorities.

Cybersecurity regulations have been beneficial in promoting a more secure digital

and operational environment for businesses, and in enhancing data protection,

continuity, trust, and compliance across industries. Yet, as cybersecurity regulations

continue to tighten across various industries and regions, the playing field widens

with more opportunities for cybercriminals to find compliance violations to extort

and use as leverage in demanding ransom payments.

### Regional pain
Threat actors do their homework and gravitate toward regions where the threat

of regulatory exposure could cause the most damage. For example, in EMEA,

government-driven regulatory bodies drive compliance within the EU and the United

Kingdom, creating greater consistency in reporting time frames, enforcement, and

financial penalties. Similarly, in North America, industry councils or associations,

federal agencies, and states/provinces actively drive regulations, and enforcement

is typically rigorous.

In contrast, LATAM’s rapid digital transformation, coupled with the vulnerabilities

of increasingly connected systems, makes the region an attractive target for

ransomware attacks. However, inconsistent cybersecurity regulations and

enforcement across the region diminish the impact of this type of extortion. The

same is true in APAC, where the region is a patchwork of new compliance mandates,
with stricter enforcement in some areas and inconsistent consequences for failure

to report in others. As such, we have yet to see evidence that LATAM and certain

areas in APAC have been impacted by groups that threaten regulatory exposure,

and some newer regulations such as NIS2 have yet to be leveraged. However,

we know how quickly threat actors can shift their focus, so it is worth tracking

broader trends.

[Akamai.com](https://www.akamai.com/)   |   11

Ransomware Report 2025  I  Volume 11, Issue 03

Our researchers continue to track the evolving use of regulation extortion tactics by

ransomware groups. It can be complex for international companies to stay attuned to regional

reporting requirements to ensure their security capabilities provide compliance artifacts in

a way that supports their audit and crisis management actions. However, it’s important to

remove this arrow from the threat actor’s quiver. Some key pieces of regulation to track in

various regions include:

- APAC: The reporting time frames range from 12 to 72 hours, depending on the

severity of the impact of the attack. Some countries, such as Japan, do not currently

impose fines. In other countries, such as Singapore, failure to comply with PDPA can

result in fines of 10% of annual revenue. In India, criminal penalties are also possible.
- EMEA: The requirements for timely reporting and financial penalties are similar

to those in APAC. For example, failure to comply with NIS2’s 24-hour reporting

deadline can result in fines up to €10 million or 2% of the company’s global annual

revenue, whichever is greater. Under GDPR, organizations have more time to report

(within 72 hours), but the fines can double. Additional ransomware reporting

requirements in both the United Kingdom and the European Union are currently

under review.
- LATAM: Regulations vary from country to country. Brazil has one of the most

stringent policies under the Lei Geral de Proteção de Dados Pessoais (LGPD), with

initial reporting required within 72 hours and supplemental information due within

20 days. Fines for failure to report can be 2% of annual revenue per infraction.
- North America: Failure to report within 24 hours has resulted in SEC fines of US$10

million. Nondisclosure of Health Insurance Portability and Accountability Act of

1996 (HIPAA) breaches can result in fines from US$100 up to US$1.5 million per

incident, depending on the severity of the infraction, in addition to criminal penalties.

The Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA), expected to
go into effect in 2026, mandates ransomware reporting.

[Akamai.com](https://www.akamai.com/)   |   12

Ransomware Report 2025  I  Volume 11, Issue 03

## Inside the RaaS ecosystem
RaaS has revolutionized ransomware operations, transforming them from highly specialized

attacks into scalable, subscription-based services accessible to a broader range of

cybercriminals. This pivotal shift eliminates technical barriers that previously impeded

ransomware deployment, enabling cybercriminals with minimal technical expertise to

execute sophisticated attacks. The democratization of ransomware allows developers in

criminal groups to earn steady revenue while enabling less technically savvy threat actors to

participate in high-stakes digital extortion campaigns. The proliferation of RaaS significantly

increases both the scale and frequency of attacks, compelling organizations to implement

more resilient security architectures to withstand this threat.

RaaS platforms like REvil, Ryuk, and DarkSide, which emerged in the mid-2010s,

pioneered the concept of providing ready-to-use ransomware kits to affiliates for a share

of the proceeds. Beyond financial gain, the real-world ramifications of this business model

became evident in high-profile operations like the Colonial Pipeline incident (attributed

to the DarkSide group), which disrupted essential services and critical infrastructure in

the United States while generating substantial profits for its operators.

### Key entities in the RaaS business model
The rapid growth and success of RaaS stems from its accessibility, operational efficiency,

and organizational structure that mirror legitimate businesses. These criminal enterprises

employ a division of labor with specialized roles that optimize their overall operations.

Figure 6 illustrates the primary players in the RaaS ecosystem and their specific functions.

![Figure 6: The critical players that make up the RaaS chain]

Fig. 6: The critical players that make up the RaaS chain

[Akamai.com](https://www.akamai.com/)   |   13

Ransomware Report 2025  I  Volume 11, Issue 03

### Ransomware developers
RaaS developers or operators are responsible for creating, updating, and maintaining the

ransomware software that they subsequently sell or lease to affiliates. Additionally, they design

robust malware strains (many with user-friendly interfaces and 24/7 support for their customers),

manage the supporting infrastructure, and establish secure communication channels for affiliates.

These highly skilled cybercriminals frequently implement new features and capabilities to remain

undetected and to ensure operational reliability.

Financial arrangements typically follow a profit-sharing model, with splits ranging from 60/40 to as

favorable as 90/10 — with the larger percentage going to the affiliate who implements the attacks.

### Affiliates
Affiliates acquire ransomware from developers through dark web marketplaces and identify

targets, deploy attacks, and sometimes negotiate with victim organizations. These cybercriminals

may pay a monthly fee to lease the ransomware software, or they may obtain a lifetime license.

Unlike developers, affiliates generally possess fewer technical skills, increasing their risk of

operational errors and exposure to law enforcement.

Although affiliates select the targets, the developers provide a set of rules that the affiliates

need to abide by; for example, target restrictions to certain countries or industries. Breaking such

rules could mean expulsion from the group — or, in some cases, the developers will provide the

decryptor to the victim for free. For a time, several ransomware groups avoided targeting

healthcare organizations, particularly during the COVID-19 pandemic. DragonForce, with code

that is an amalgamation of LockBit 3.0 and Conti code, claims to follow a moral code that excludes

some types of healthcare targets.

### Initial access brokers
To expedite victim identification and reconnaissance, affiliates often engage initial access brokers

(IABs) who specialize in breaching targets and selling network access to cybercriminals, including

ransomware operators.

IABs have a specific set of skills that allow them to streamline RaaS operations by performing

the work of gaining footholds without launching attacks themselves, thus avoiding attention

from law enforcement. They sell various access types, including Remote Desktop Protocol (RDP),

VPN access, email access, and file share access. Although RDP is the most common type of

access sold, it’s worth noting that VPN access is also gaining momentum, potentially because

it provides stealthier and more direct access to corporate networks.

The price of access depends on the target organization’s revenue, with more valuable

environments commanding higher prices. In 2024, 86% of access listings were

priced at US$3,000 or less.

[Akamai.com](https://www.akamai.com/)   |   14

Ransomware Report 2025  I  Volume 11, Issue 03

### Major players in the RaaS ecosystem
The following profiles describe some of the most notable RaaS groups active from 2024

through early 2025 and emphasize their innovative tactics. The groups are organized

according to the severity of their methods and their impact on companies as of this

writing. Their innovations demonstrate how RaaS continues to evolve, and how operators

and affiliates continue to adapt, despite increasing pressure from security defenders and

law enforcement agencies.

#### RansomHub
RansomHub, first observed in early 2024, quickly rose to prominence for its multi-OS

ransomware that targets Windows, VMware ESXi, and SFTP servers. The group, which

uses double extortion, has impacted more than 200 organizations across healthcare,

education, and the public sector industries.

Earlier this year, we saw a significant increase in RansomHub activity in our customers’

environments, with some periods recording close to 700,000 events and some periods

that even exceeded that number (Figure 7).

![Figure 7: RansomHub’s growing prevalence since January 2025 is evident in the increased traffic observed among our customers]

Fig. 7: RansomHub’s growing prevalence since January 2025 is evident
in the increased traffic observed among our customers

[Akamai.com](https://www.akamai.com/)   |   15

Ransomware Report 2025  I  Volume 11, Issue 03

RansomHub’s prevalence stems from its use of evasion tools like EDRKillShifter to disable

endpoint protections and its exploitation of vulnerabilities such as CVE-2024-1709. Like most

groups, RansomHub uses a double extortion tactic, encrypting data and threatening to leak

exfiltrated information unless victims pay. As part of its extortion mechanism, RansomHub

also instructs affiliates on its leak site to report victims to regulatory bodies, such as the GDPR

authorities, to pressure organizations to pay the ransom to avoid regulatory penalties.

Additionally, the operators supply affiliates with customized tooling and support, enabling

them to steal confidential information as a separate step. In some cases, affiliates re-target

previously compromised organizations, leveraging stolen data for additional financial gain.

RansomHub’s structure and business model, including a generous 90/10 ransom split, attract

both experienced threat actors and novice cybercriminals. RansomHub’s infrastructure went

offline on April 1, 2025, with several affiliates migrating to groups such as DragonForce and Qilin.

#### CL0P
CL0P distinguishes itself through the systematic exploitation of zero-day vulnerabilities in file

transfer systems. These include attacks targeting a file transfer appliance (CVE-2021-27101,

CVE-2021-27102, CVE-2021-27103, CVE-2021-27104), GoAnywhere MFT (CVE-2023-0669),

and PaperCut (CVE-2023-27350 and CVE-2023-27351). Most notably, CL0P exploited MOVEit

Transfer (CVE-2023-34362), compromising more than 2,500 vulnerable servers. Recently, the

group claimed to have siphoned and leaked data from a cloud services provider and exploited

zero-day vulnerabilities in Cleo-managed file transfer products, enabling remote code execution.

CL0P employs a distinctive strategy: Remain dormant between carefully orchestrated campaigns

that coincide with zero-day vulnerability discoveries. This approach effectively enables the group

to breach high-value targets while maintaining a relatively low overall victim count, except during

exploitation spikes. Additionally, it uses a triple extortion mechanism — and sometimes even a

quadruple extortion tactic in which it reaches out to customers and threatens to release their

information to further pressure the affected organizations to pay the ransom.

#### FunkSec
The RaaS group FunkSec exemplifies how GenAI and LLMs are reshaping ransomware

operations. Emerging in late 2024, FunkSec, which follows a double extortion model, quickly

gained attention by reportedly leveraging AI tools to develop its ransomware code, enhance

support chats and communications, and rapidly generate new iterations. Its latest version, still

in development, may include multiple extortion schemes, such as auctioning stolen data to the

highest bidder, targeting victims’ personal networks and families, and launching DDoS attacks

to intensify pressure on targets. Researchers believe FunkSec’s heavy reliance on AI stems from

the group’s lack of technical expertise.

[Akamai.com](https://www.akamai.com/)   |   16

Ransomware Report 2025  I  Volume 11, Issue 03

FunkSec has moved away from traditional leak sites by employing an auction platform, FunkBID, which

allows the sale of stolen data to maximize profits. Their Rust-based ransomware frequently targets

organizations that were previously compromised by other groups, using data stolen in prior breaches,

which complicates efforts to verify the legitimacy of their claimed attacks. Many researchers question

whether FunkSec’s activities represent genuine threats or are simply noise to boost their visibility.

The group has formed strategic collaborations with other ransomware threat actors, such as FSociety,

to expand its criminal network. Some reports trace FunkSec’s activities to Algeria and suggest possible

hacktivist motives in addition to financial motives. Despite their inexperience, FunkSec’s innovative use

of AI in digital extortion could signal an emerging trend in the ransomware landscape.

#### LockBit 3.0