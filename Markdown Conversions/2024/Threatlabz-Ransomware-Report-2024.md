# ThreatLabz 2024 Ransomware Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Ransomware Landscape: Top Trends and Targets](#ransomware-landscape-top-trends-and-targets)
- [Overall rise in ransomware attacks](#overall-rise-in-ransomware-attacks)
- [Industry verticals most impacted by ransomware](#industry-verticals-most-impacted-by-ransomware)
- [Geographical distribution of victim organizations](#geographical-distribution-of-victim-organizations)
- [Most active ransomware groups in 2023-2024](#most-active-ransomware-groups-in-2023-2024)
- [Major vulnerabilities used in ransomware attacks](#major-vulnerabilities-used-in-ransomware-attacks)
- [Ransomware Roundup: What’s Making Headlines](#ransomware-roundup-whats-making-headlines)
- [The ransomware plague in healthcare](#the-ransomware-plague-in-healthcare)
- [The impact of the SEC’s cybersecurity ruling](#the-impact-of-the-secs-cybersecurity-ruling)
- [Impact of law enforcement actions](#impact-of-law-enforcement-actions)
- [Top 5 Ransomware Families to Watch in 2024-2025](#top-5-ransomware-families-to-watch-in-2024-2025)
- [#1 Dark Angels](#1-dark-angels)
- [#2 LockBit](#2-lockbit)
- [#3 BlackCat](#3-blackcat)
- [#4 Akira](#4-akira)
- [#5 Black Basta](#5-black-basta)
- [ThreatLabz Ransomware Notes Archive](#threatlabz-ransomware-notes-archive)
- [2025 Predictions](#2025-predictions)
- [How Zscaler Simplifies Ransomware Protection](#how-zscaler-simplifies-ransomware-protection)
- [Holistic prevention at each stage of the attack chain](#holistic-prevention-at-each-stage-of-the-attack-chain)
- [Related Zscaler products](#related-zscaler-products)
- [Ransomware Prevention Guidance](#ransomware-prevention-guidance)
- [Report Methodology](#report-methodology)
- [About ThreatLabz](#about-threatlabz)
- [About Zscaler](#about-zscaler)

©2024 Zscaler, Inc. All rights reserved.

Ransomware attacks have reached new heights of ambition and audacity 
over the past year, marked by a notable surge in extortion attacks. 
Adding to the increase in ransomware attacks, ThreatLabz research 
uncovered an unprecedented ransom payout of US$75 million—the 
largest ever paid by one company. This amount is nearly double the 
highest publicly known ransom payment.
1 In 2023 alone, ransomware 
payments exceeded $1 billion, highlighting the escalating financial impact 
of these cybercrimes.

Ransomware threat actors’ tactics have become increasingly sophisticated 
and bold. Notably, they have surpassed the traditional boundaries of 
the corporations they attack, even going so far as to target the children 
of executives to provoke faster and higher ransoms.[^2] From critical 
infrastructure[^3] and major corporations[^4] to small and medium-sized 
enterprises, no organization is immune to finding themselves in the 
crosshairs of the next campaign or evolution of attacks.

Despite law enforcement takedowns of multiple initial access brokers 
under special ops “Operation Endgame” and “Operation Duck 
Hunt,” many of the largest active ransomware families continue to 
rapidly regroup and launch new attacks while barely skipping a beat. 
Unfortunately, many ransomware actors are beyond the reach of law 
enforcement, making them virtually immune to criminal prosecution. 
As detailed in this report, law enforcement agencies have augmented 
their pressure tactics through reward money, sanctions, trolling, and 
exposing the individuals behind ransomware using various forms of 
psychological tactics.

As ransomware actors continuously evolve their tactics, it is crucial to stay 
up to date on how the threat landscape is changing.

The Zscaler ThreatLabz 2024 Ransomware Report offers an overview of 
the ransomware threat landscape from April 2023 through April 2024, 
detailing the latest trends, targets, ransomware families, and effective 
defense strategies.

ThreatLabz found that ransomware attacks increased by 17.8% year-over-
year based on blocked attempts in the Zscaler cloud, while ransomware 
attacks identified through data leak site analysis surged by 57.8%. The 
most common targets were businesses in the manufacturing, healthcare, 
and technology sectors, putting critical operations and infrastructure 
squarely in the line of attack.

The findings presented in this report underscore the need for organizations 
to prioritize protection against the relentless tide of ransomware. The 
insights and strategies in the report serve as a crucial guide for improving 
your ransomware defenses. By understanding the latest trends and 
vulnerabilities, and implementing recommended best practices, you can 
significantly reduce the risk of becoming a ransomware victim and better 
protect your organization’s critical assets and data.

# Executive Summary
[^1]: Bloomberg, CNA Financial Paid $40 Million in Ransom After March Cyberattack, May 20, 2021.
[^2]: Business Insider, Hackers are now targeting the children of corporate executives in ransomware attacks, May 12, 2024.
[^3]: Dark Reading, Ascension Healthcare Suffers Major Cyberattack, May 10, 2024.
[^4]: CyberScoop, Boeing confirms attempted $200 million ransomware extortion attempt, May 8, 2024.

©2024 Zscaler, Inc. All rights reserved.

Zscaler ThreatLabz research 
uncovered a record-breaking 
ransom payment of US$75 million
—the largest ransomware payment by a 
company in history—nearly double the highest 
publicly known payout.

The manufacturing, healthcare, 
and technology sectors were the 
top targets of ransomware attacks,
while the energy sector experienced a 500% 
year-over-year spike as critical infrastructure 
and susceptibility to operational disruptions 
make it particularly attractive to cybercriminals.

Ransomware attacks blocked by 
the Zscaler cloud increased by 
17.8%, and the number of extorted 
companies on data leak sites 
grew by 57.8% in the same period 
year-over-year despite numerous law 
enforcement operations, including the seizure 
of infrastructure along with arrests, criminal 
indictments, and sanctions.

The United States remains the top 
target of ransomware, experiencing 
49.95% of overall attacks,
followed by the United Kingdom, Germany, 
Canada, and France.

# Key Findings

ThreatLabz identified 19 new 
ransomware families during the analysis 
period, bringing the total number to 391 since 
our tracking started.

The most active ransomware 
families were LockBit (22.1%), BlackCat 
(a.k.a. ALPHV) (9.2%), and 8Base (7.9%).

Vulnerabilities remain an all-too-
common ransomware attack vector,
emphasizing the importance of timely patching 
and unified vulnerability management, 
underpinned by a zero trust architecture to 
provide protection even when patches are 
not available.

Voice-based social engineering 
attacks are increasingly being used
to gain access to corporate networks—a 
technique used by Scattered Spider and the 
Qakbot threat group.

©2024 Zscaler, Inc. All rights reserved.

The dynamic nature of ransomware has placed it at the forefront of security concerns in recent years. 
Threat actors are constantly evolving their methods of attack and extortion, leveraging advances in 
artificial intelligence (AI) technology, leaked source code, and advanced encryption to maximize their 
impact and profitability. 
This report examines the following ransomware attack trends from April 2023 through April 2024:
- Overall rise in ransomware attacks
- Industry verticals most impacted by ransomware
- Geographical distribution of victim organizations 
- Increased law enforcement action against ransomware groups and initial access brokers
- Top ransomware threats and record-breaking ransom payments

# Ransomware Landscape: Top Trends and Targets

©2024 Zscaler, Inc. All rights reserved.

# Overall rise in ransomware attacks

The latest ThreatLabz analysis reveals a concerning trend, with a 17.84% 
year-over-year increase in ransomware attacks based on blocked 
attempts observed across the Zscaler cloud. The rise in ransomware 
activity translates to significant disruptions and financial impacts to victim 
organizations of all sizes. These attacks often disrupt business operations, 
causing extended downtime, substantial data loss, and high recovery 
costs. The financial burden is considerable; not only is there a ransom 
demand at play, but system restoration and damage control can come 
at a hefty price. In light of these escalating threats, the need for robust 
ransomware defense measures has never been greater.

![NUMBER OF ATTEMPTS BLOCKED IN ZSCALER CLOUD: A bar graph showing 1,502,175 attempts in 2021, 2,727,114 in 2022, 3,756,858 from April 2022 to April 2023, and 4,426,966 from April 2023 to April 2024, with a +17.84% increase from the previous period.]

©2024 Zscaler, Inc. All rights reserved.

# Industry verticals most impacted by ransomware

Ransomware attacks pose significant risks to businesses of all sizes and 
industries. These attacks can compromise sensitive data, lead to heavy 
financial losses, disrupt business continuity, and damage reputations. 
Different industries face unique ransomware challenges based on how they 
operate, the data they handle, and their technological infrastructure.

Despite the variables, ransomware extortion attacks have consistently 
surged, with the number of victim companies listed on data leak sites 
increasing by 57.81% since last year’s ThreatLabz report on ransomware 
trends. The manufacturing industry was by far the most targeted industry, 
accounting for 653 attacks—more than two times as many as any 
other industry.

![Ransomware attacks by industry based on data leak sites (top 20 industries only): A bar graph showing the number of attacks per industry, with Manufacturing at 653, Healthcare at 312, Technology at 265, Education at 217, Financial Services at 159, Retail & Wholesale at 156, Legal at 154, Other at 152, Construction at 144, Transportation Services at 144, Services at 108, Government at 95, Real Estate at 79, Industrial Machinery & Equipment at 69, IT Services at 69, Energy at 69, Insurance at 50, Recreation at 48, Hospitality at 47, and Consulting at 44.]

©2024 Zscaler, Inc. All rights reserved.

## Year-over-year trends

The energy sector experienced a 527.27% year-over-year increase in 
ransomware attacks, likely due to its critical nature and the high ransom 
potential it offers to attackers.

Similarly, the restaurants, bars, and food services industry saw a 
333.33% rise in such attacks. This may be attributed to the sector’s rapid 
digitization, driven by the adoption of advanced point-of-sales systems 
and online ordering platforms. While these technologies may streamline 
operations and improve customer experiences, they can also introduce 
potential vulnerabilities.

While this rise highlights the prevalence of ransomware attacks, it may 
not capture the full extent of ransomware incidents. Many attacks go 
unreported or are resolved privately through ransom payments without 
public disclosure. Thus, these figures should be seen as indicative of 
broader ransomware trends rather than a comprehensive representation of 
the entire threat landscape.

![Year-over-year percentage change in ransomware extortion attacks by industry: A bar graph showing the percentage change in ransomware attacks per industry. Energy at 527.27%, Restaurants, Bars & Food Services at 333.33%, Religious Organizations at 250.00%, Technology at 173.20%, Healthcare at 126.09%, Legal at 102.63%, Manufacturing at 93.77%, Real Estate at 75.56%, Arts, Entertainment & Recreation at 75.00%, Agriculture & Forestry at 72.22%, Financial Services at 55.88%, Government at 48.44%, Pharmaceuticals at 40.00%, Transportation Services at 35.85%, Media at 31.82%, Education at 25.43%, Retail & Wholesale at 15.56%, Insurance at 11.11%, Construction at 10.77%, Telecommunications at 0.00%, Other at -8.98%, Aerospace & Defense at -12.50%, Utilities at -47.06%, Oil & Gas at -54.05%, Food, Beverage & Tobacco at -56.67%, Services at -59.09%, Mining at -60.00%, Household & Personal Products at -69.23%, Nonprofit Institutions at -70.00%, Basic Materials and Chemicals at -86.27%, and Consumer Services at -94.12%.]

©2024 Zscaler, Inc. All rights reserved.

# Geographical distribution of victim organizations

The United States faced a markedly higher volume of ransomware attacks than any other country, accounting for about 50% 
of all incidents globally. In comparison, the United Kingdom was the second-most targeted nation, experiencing nearly 6% of 
ransomware attacks, followed by Germany (4.09%), Canada (3.51%), and France (3.26%). Figure 3 shows a heatmap illustrating 
countries impacted by ransom extortions between April 2023 and April 2024. 

![Breakdown of ransomware victims by country: A pie chart showing the percentage of ransomware victims by country. United States at 49.95%, United Kingdom at 5.92%, Canada at 3.51%, France at 3.26%, Italy at 3.24%, Germany at 4.09%, Australia at 2.00%, Spain at 1.70%, India at 1.65%, Mexico at 1.56%, Brazil at 1.56%, Netherlands at 1.37%, Switzerland at 1.18%, Japan at 1.15%, and Sweden at 0.99%.]

©2024 Zscaler, Inc. All rights reserved.

Understanding the distribution of ransomware attacks is essential for risk assessment, resource allocation, policy 
development, international cooperation, and public awareness efforts in combating ransomware threats.

## Risk assessment
Analyzing heavily targeted regions helps organizations in 
those areas to assess their own risk levels and implement 
stronger cybersecurity. In ThreatLabz research, the US 
accounts for 50% of global ransomware attacks, calling 
for organizations within its borders to prioritize stringent 
security protocols.

## Policy development
Governments can use insights from regional ransomware 
attacks to inform legislation, improve security standards, 
promote international cooperation, and facilitate public-
private sector information sharing. As a recent notable 
example, the SEC’s new cybersecurity rules mark a major 
step in enhancing transparency and accountability amid 
growing threats. 

## Resource allocation
Targeted data enables governments and organizations to 
strategically allocate resources, enhancing their security 
posture by prioritizing support, funding, and expertise in 
areas with the highest threat levels.

## International cooperation
Identifying the most targeted countries allows 
coordinated efforts between law enforcement, 
organizations, and governments to combat 
ransomware at the national and international levels.
Operation Duck Hunt and Operation Endgame 
exemplify how international cooperation can disrupt 
cybercriminal activities.

## Public awareness
Highlighting frequently targeted countries may urge 
individuals, organizations, and governments to take more 
proactive measures when it comes to cybersecurity 
training, incident response planning, and investment in 
defensive technologies.

©2024 Zscaler, Inc. All rights reserved.

## Year-over-year trends

ThreatLabz compared ransomware attacks from this year's report with the ThreatLabz 2023 Ransomware Report to assess rates of 
change. Among the top 15 most targeted countries, the US experienced a notable year-over-year increase of 101.88%, and Sweden saw 
a staggering 350% rise, although it accounted for a significantly smaller share of the total attacks.

While analyzing ransomware trends at a global level is invaluable, it is also important to examine the specific developments in different 
regions of the world. Studying regional breakdowns helps organizations create tailored security plans and aid governments in developing 
more effective cybersecurity policies.

![Year-over-year comparison of ransomware attacks by country: A table showing the ransomware attacks by country in 2023, 2024, and the percentage change. United States of America: 902, 1,821, 101.88%. United Kingdom: 144, 216, 50.00%. Germany: 110, 149, 35.45%. Canada: 151, 128, -15.23%. France: 87, 119, 36.78%. Italy: 63, 118, 87.30%. Australia: 69, 73, 5.80%. Brazil: 38, 57, 50.00%. Spain: 36, 62, 72.22%. Mexico: 31, 57, 83.87%. Netherlands: 17, 50, 194.12%. India: 62, 60, -3.23%. Switzerland: 32, 43, 34.38%. Japan: 44, 42, -4.55%. Sweden: 8, 36, 350.00%.]

![Year-over-year comparison of ransomware attacks by country in the EMEA region: A table showing the companies impacted by ransomware attacks in 2023, 2024, and the percentage change. United Kingdom: 144, 216, 50.00%. Germany: 110, 149, 35.45%. France: 87, 119, 36.78%. Italy: 63, 118, 87.30%. Spain: 36, 62, 72.22%. Netherlands: 17, 50, 194.12%. Switzerland: 32, 43, 34.38%. Sweden: 8, 36, 350.00%. Belgium: 16, 34, 112.50%. South Africa: 13, 24, 84.62%. Austria: 15, 24, 60.00%. United Arab Emirates: 12, 21, 75.00%.]

![Year-over-year comparison of ransomware attacks by country in the APAC region: A table showing the companies impacted by ransomware attacks in 2023, 2024, and the percentage change. Australia: 69, 73, 5.80%. India: 62, 60, -3.23%. Japan: 44, 42, -4.55%. Thailand: 13, 25, 92.31%. Indonesia: 15, 23, 53.33%. Malaysia: 14, 20, 42.86%. Taiwan: 23, 17, -26.09%. Philippines: 7, 16, 128.57%. Singapore: 8, 16, 100.00%. China: 21, 15, -28.57%. South Korea: 12, 10, -16.67%. Vietnam: 10, 10, 0.00%.]

©2024 Zscaler, Inc. All rights reserved.

# Most active ransomware groups in 2023-2024

LockBit (22.1%), BlackCat (9.2%), and 8Base (7.9%) were the most active ransomware extortion groups over the past year, each 
responsible for a significant number of attacks. Figure 8 shows the number of data leak victims per ransomware family during 
this period.

![Ransomware attacks revealed on maliciously operated data leak websites: A bar graph showing the number of data leak victims per ransomware family. LockBit at 988, BlackCat at 410, 8Base at 352, Play at 345, Clop at 291, BianLian at 268, Akira at 224, Black Basta at 202, Medusa at 169, NoEscape at 126, Hunters at 97, Stormous at 92, Rhysida at 90, and Qilin/AgendaCrypt at 84.]

## Newest ransomware groups on the scene 
Figure 9 showcases a timeline of new ransomware groups that began publishing data on leak sites as part of their extortion strategy.

![New ransomware groups with data leak sites: A timeline showing the emergence of new ransomware groups. April 2023: CiphBit. May 2023: Money Message. June 2023: Dark Angels. July 2023: RAworld. September 2023: Abyss. October 2023: Akira, BlackSuit, Rhysida. January 2024: Knight (rebrand of Cyclops), NoEscape, INC. February 2024: Underground, 3AM, Killsec. March 2024: Hunters International (rebrand of Hive), Slug, RansomHub, Cloak.]

©2024 Zscaler, Inc. All rights reserved.

# Major vulnerabilities used in ransomware attacks

Vulnerabilities in software, systems, and the overall digital infrastructure can serve as critical entry 
points for ransomware attacks. Organizations must be aware of these vulnerabilities and take 
proactive measures to address them.

The Cybersecurity & Infrastructure Security Agency (CISA) maintains a comprehensive list of 
vulnerabilities,[^5] including those actively exploited by ransomware groups. It is highly recommended 
that organizations closely monitor this list and prioritize the mitigation of vulnerabilities mentioned 
therein. Proactive vulnerability management is essential for strengthening the overall cybersecurity 
posture of an organization.

In many cases, the vulnerabilities exploited by ransomware groups impact internet-connected assets 
in organizations’ external attack surface, such as gateways, VPNs, and other remote connectivity 
technologies. Because they are internet-facing, these vulnerabilities are significantly easier for threat 
actors to scan for and exploit. CISA’s latest guidance[^6] further emphasizes vulnerabilities in VPNs and 
remote connectivity solutions as critical points of concern, advising the adoption of the most current 
approaches, such as zero trust architecture, SSE, and SASE, which are based on granular access 
control policies.

Over the past year, prominent ransomware families have targeted and exploited the vulnerabilities 
shown in figure 10, significantly impacting a wide range of systems.

Available patches for these vulnerabilities should be applied as 
soon as possible, along with the following mitigation measures: 
- Disable remote access to servers
- Use strong passwords and multifactor authentication
- Monitor servers for suspicious activity 

[^5]: Cybersecurity & Infrastructure Security Agency, Known Exploited Vulnerabilities Catalog, accessed June 25, 2024.
[^6]: Cybersecurity & Infrastructure Security Agency, Modern Approaches to Network Access Security, June 18, 2024.

![Prevalent vulnerabilities from April 2023-April 2024: A table outlining the vulnerabilities exploited by ransomware groups. Cisco's remote access VPN feature (exploited by Akira): CVE-2023-20269: Allows unauthenticated remote attackers to conduct brute-force attacks to identify valid username and password combinations, and authenticated remote attackers to establish a clientless SSL VPN session with an unauthorized user. Citrix NetScaler ADC and NetScaler Gateway (exploited by INC Ransom, LockBit, and BlackCat): CVE-2023-4966 (a.k.a. Citrix Bleed): Allows attackers to bypass password authentication and MFA to gain unauthorized access to networks using leaked session tokens. CVE-2023-3519: Allows attackers to exploit remote code execution flaws. ConnectWise ScreenConnect (exploited by LockBit, Black Basta, and Bl00dy): CVE-2024-1708: Allows attackers to gain unauthorized access to directories and files beyond restricted areas, resulting in information disclosure and control over compromised systems. CVE-2024-1709: Allows attackers to circumvent authentication mechanisms and directly access confidential information or critical systems. Cisco's ASA and FTD software (exploited by Akira): CVE-2020-3259: Allows unauthenticated remote attackers to retrieve memory contents from an impacted device, resulting in the disclosure of confidential information.]

©2024 Zscaler, Inc. All rights reserved.

# Ransomware Roundup: What’s Making Headlines

The ransomware plague 
in healthcare 

The healthcare industry faced significant challenges throughout 2023 
and into 2024 as it was heavily targeted by ransomware groups. The 
repercussions of disrupting healthcare operations are serious: ambulances 
get rerouted, prescriptions are delayed, and essential medical procedures 
have to be postponed. Moreover, the theft of sensitive health data can 
have far-reaching consequences, including identity theft and healthcare 
fraud, further exacerbating vulnerabilities in the healthcare ecosystem.

## UNFORESEEN CONSEQUENCES OF RANSOM PAYMENTS
A healthcare technology provider for payment solutions fell victim to a 
ransomware attack orchestrated by the BlackCat group. Despite complying 
with the attackers’ demands and paying a staggering $22 million ransom, 
the ordeal took an unexpected turn. BlackCat reneged on their promise 
to share a portion of the ransom with the affiliate behind the attack (a 
so-called “exit scam”), prompting the affiliate to threaten the healthcare 
provider with the release of sensitive data.

This is a stark reminder that the old adage “there is no honor among 
thieves” holds true for ransomware attacks. Even if ransoms are paid, there 
is no guarantee that the threat group will not still post or delete stolen 
data. In addition, some ransomware decryption tools contain bugs that 
prevent successful data recovery, and may take longer to recover data than 
from a backup.

## DOUBLE EXTORTION, DOUBLE VICTIMIZATION
In February 2023, a prominent US pharmaceutical distributor confirmed 
that their IT systems had been compromised. The breach affected one of 
the distributor’s subsidiaries, with the stolen files later leaked by the Lorenz 
ransomware group.[^7] Then, in February 2024, the same distributor faced 
another ransomware attack.[^8] This appears to be part of a growing trend 
ThreatLabz has observed, where a company has been subject to multiple 
ransomware incidents within one year.

Ransomware is pervasive and transcends industries—and when one group is shut down, another is reborn 
or emerges anew. Here are some recent stories highlighting the ever-evolving ransomware landscape.

[^7]: BleepingComputer, Drug distributor AmerisourceBergen confirms security breach, February 8, 2023.
[^8]: BleepingComputer, Pharmaceutical giant Cencora says data was stolen in a cyberattack, February 27, 2024.

©2024 Zscaler, Inc. All rights reserved.

Moreover, compliance timelines vary based on the size and reporting 
status of companies, adding another layer of complexity. Smaller reporting 
companies often have different, and typically longer, compliance deadlines 
compared to larger corporations. And while larger corporations must 
adhere to tighter deadlines, their scale also affords them more resources to 
analyze the materiality of a cybersecurity incident.

The new disclosure requirements also eliminate the possibility for public 
companies to pay ransoms quietly without incurring reputational damage 
and the backlash that follows after openly sharing information about 
a breach.

## SOME COMPANIES ARE ALREADY IN VIOLATION 
OF THE SEC’S RULES
Despite the SEC’s clear guidelines, some companies have already fallen 
short of compliance with the new cybersecurity rules. Recent disclosures 
from well-known companies have raised concerns about noncompliance 
and the adequacy of their incident reporting.[^9] Many of these disclosures 
lack ‌
quantitative data and detailed assessments of the financial and 
operational implications of the cyber incidents, which is precisely what the 
SEC now mandates. This trend, where companies provide deficient cyber 
incident disclosures despite the SEC ruling, may call for enhanced guidance 
and regulatory oversight to ensure consistent and effective compliance. 

The SEC’s cybersecurity rulings represent a significant regulatory 
shift aimed at improving transparency and accountability in incident 
reporting. Adhering to these new rules consistently and in good faith 
will require ongoing collaboration between regulators, companies, and 
industry stakeholders.

# The impact of the SEC’s cybersecurity ruling

In 2023, the SEC introduced new cybersecurity disclosure rules to enhance 
transparency and accountability among publicly traded companies. Effective 
December 15, 2023, these rules mandate the timely reporting of material 
cybersecurity incidents and require detailed information about a company’s 
cybersecurity risk management, strategy, and governance. Key components of 
the SEC rulings include the addition of Item 1.05 to for 8-K, which necessitates 
reporting of material cybersecurity incidents within four business days of the 
company’s determination of materiality. Additionally, Form 10-K now requires 
annual reporting on cybersecurity risk management and strategy, starting with 
fiscal years ending on or after December 15, 2023. Foreign private issuers must 
also comply with comparable disclosures on Form 6-K and Form 20-K. 

The rulings present a new challenge for ransomware actors offering 
publicly traded companies private payment resolution services, as the 
companies are now still required to fully disclose the attack. On the 
positive side, the new mandate undercuts encryptionless extortion attacks, 
an emerging trend by which ransomware actors rely solely on the threat of 
leaking stolen data to demand ransoms.

## HOW THE NEW RULES IMPACT COMPANIES
The SEC’s cybersecurity rulings can pose serious challenges for companies 
in terms of compliance and risk management. While intended to enhance 
transparency and investor protection, these rules require companies to 
navigate complex reporting requirements and provide prompt disclosure of 
material incidents.

One major impact is the increased pressure on companies to quantify and 
assess cyber incidents accurately. Determining materiality and the potential 
impact of cyber incidents requires careful analysis, which can be costly and 
may require companies (big and small) to rethink their incident response 
protocols and update their disclosures to meet the SEC’s requirements. 

[^9]: Forbes, Companies Are Already Not Complying With The New SEC Cybersecurity Incident Disclosure Rules, March 4, 2024.

©2024 Zscaler, Inc. All rights reserved.

# Impact of law enforcement actions

[^10]: US Department of Justice, Qakbot Malware Disrupted in International Cyber Takedown, August 29, 2023.
[^11]: TechCrunch, How the FBI took down the notorious Qakbot botnet, September 1, 2023.

## Qakbot disrupted by “Operation Duck Hunt”
On August 29, 2023, in a coordinated multinational effort, the Federal 
Bureau of Investigation (FBI) and the Department of Justice (DOJ) announced 
Operation Duck Hunt. Zscaler ThreatLabz provided significant technical 
assistance to law enforcement for this operation.
[^10] Qakbot’s infrastructure 
was designed to be resilient against takedown attempts through a multi-
tiered infrastructure, as shown in figure 11.

This infrastructure provided several layers of resiliency, with each tier 
requiring a coordinated effort to dismantle. The first tier of Qakbot’s 
infrastructure included infected systems running a supernode plugin that 
relayed traffic upstream to several proxies designed to hide the master 
Qakbot backend server.

Operation Duck Hunt redirected the supernode’s upstream proxy servers to 
a set of sinkhole servers to immediately take over Qakbot’s infrastructure 
as shown in figure 12.

Once the FBI hijacked the supernodes, the 
sinkhole servers instructed victim computers to 
download shellcode that reflectively loaded a DLL 
that neutralized the malware. This successfully 
disinfected the victim computers and prevented 
further attacks. 

At the time of the takedown, Qakbot had infected 
more than 700,000 computers worldwide, 
including more than 200,000 in the United 
States alone.
[^11] Prior to this operation, Qakbot was 
active for nearly 15 years, originally designed to 
facilitate credit card and wire fraud. In 2019, the 
group pivoted to serving as an initial access broker 
for ransomware groups including Conti, ProLock, 
Egregor, REvil, MegaCortex, and Black Basta.

Qakbot malware was typically distributed 
through spam emails containing malicious 
attachments or links. Once infected, Cobalt Strike 
was frequently deployed for lateral movement 
and the eventual deployment of ransomware.

Unfortunately, there were no arrests or unsealed 
indictments against any of the threat actors, 
and Qakbot resurfaced in December 2023. The 
group updated the malware to support 64-
bit versions of Windows, changed the internal 
configuration format, and modified the network 
communication to use AES encryption. As we 
will discuss later in the report, the Qakbot threat 
actor has significantly changed their TTPs since 
Operation Duck Hunt.

![Qakbot’s multi-tiered infrastructure: A diagram showing Qakbot infections, Qakbot infections with supermode module, upstream proxies, and the Qakbot master backend server.]

![Qakbot architecture after redirecting each supernode’s upstream proxies: A diagram showing Qakbot infections, Qakbot infections with supermode module, upstream proxies, sinkhole server(s), and the Qakbot master backend server.]

©2024 Zscaler, Inc. All rights reserved.

## “Operation Endgame” simultaneously 
targeted multiple initial access brokers

On May 28, 2024, in collaboration with numerous international law enforce-
ment agencies, Europol announced Operation Endgame, which simultane-
ously targeted multiple initial access brokers. This led to more than a dozen 
global searches, several arrests, and the shutdown of more than 100 serv-
ers used for criminal activity. These servers were integral to the operations of 
various malware downloaders (a.k.a. “loaders”) that had been used to infiltrate 
victims’ computers, deploying malicious software including ransomware.

The malware families targeted in this operation were responsible for in-
fecting millions of computers around the globe, including in healthcare fa-
cilities and critical infrastructure services. As part of the operation, action 
was taken against SmokeLoader, Pikabot, Bumblebee, and IcedID.

Zscaler ThreatLabz provided critical technical assistance for Operation 
Endgame’s SmokeLoader sinkhole and remediation efforts.

SmokeLoader,