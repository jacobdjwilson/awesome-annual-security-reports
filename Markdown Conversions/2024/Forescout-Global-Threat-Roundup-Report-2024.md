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
- **Emphasis and Formatting**: Apply `_italic_`, `**bold**`, `>` for block quotes, and ```` ``` ```` for code blocks.
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

The official report URL is: https://www.forescout.com/press-releases/forescout-announces-2024-threat-roundup-report/

# Report Content Below

## Table of Contents
- [Executive Summary](#executive-summary)
- [Main Findings](#main-findings)
  - [Location – Russia Retakes China’s Position](#location--russia-retakes-chinas-position)
  - [Autonomous Systems – New Techniques for Routing Attacks](#autonomous-systems--new-techniques-for-routing-attacks)
  - [Attacked Services – the Web Is the Undisputed Leader](#attacked-services--the-web-is-the-undisputed-leader)
  - [Weak Credentials – a Return to Generic Usernames](#weak-credentials--a-return-to-generic-usernames)
  - [Exploits – There’s Still Much Beyond KEV](#exploits--theres-still-much-beyond-kev)
  - [OT Attacks – Increased Focus on Building Automation](#ot-attacks--increased-focus-on-building-automation)
  - [Attacker Actions/TTPs – the Rise of Discovery](#attacker-actionsttps--the-rise-of-discovery)
  - [Malware – Botnets Again at the Top](#malware--botnets-again-at-the-top)
  - [Threat Actors – More Conflicts Bring More Threat Actors to the Scene](#threat-actors--more-conflicts-bring-more-threat-actors-to-the-scene)
- [Evolution of Attacks on Critical Infrastructure](#evolution-of-attacks-on-critical-infrastructure)
  - [Who Is Being Attacked?](#who-is-being-attacked)
  - [Who Is Attacking?](#who-is-attacking)
- [Conclusion](#conclusion)

3

5

6

7

9

10

12

15

17

19

21

23

23

26

30

2024 Threat Roundup | 2

1. Executive Summary
From the financial impact of attacks to geopolitical tensions that lead to cyber warfare, cybersecurity is top of
mind for enterprise and government organizations in 2025. In this report, we look back at the 900 million attacks
we analyzed in the threat landscape of 2024. Additionally, we offer organizations tactical insights and strategic
recommendations for improving defenses this year.

Cyber attacks are on the rise once again – including an uptick of targets in critical infrastructure in the last year.
Since 2022, however, reported incidents in critical infrastructure rose from 50 to 384 globally – or 668%,
according to data from the European Repository of Cyber Incidents, an independent research consortium that
provides scientific analysis of cyber incidents.

Take note: We also include information on vulnerabilities and exploits that are not on the CISA-KEV list but are
being exploited today.

2024 Threat Roundup | 3

2024 Threat Roundup | 4

Where Does Our Data Come From?
Most data used for our analysis comes from the Vedere Labs Adversary Engagement Environment
(AEE), a set of honeypots on the open internet luring attackers and recording their interactions. Data
points in the AEE are called attacks. They can represent a multitude of malicious actions, including port
scanning and brute forcing. The AEE recorded more than 900 million attacks between January and
December 2024. A subset of these attacks contains exploits – attempts to exploit vulnerabilities.

Our data differs from what is seen in many other threat reports because it comes from specialized IT/OT/
IoT honeypots that either mimic realistic device profiles – including exposed protocols, banners and parts
of the filesystem – or are real specialized devices, instead of generic honeypots capturing every kind of
attack.

Our Malware Analysis Lab (MAL) collects and analyzes samples dropped by attackers on the AEE or
shared on public repositories. Our goal is not to analyze as many samples as possible, but to focus on
those that are unique. We analyzed more than 100,000 unique malware samples between January
and December 2024.

Also, we constantly hunt for new command and control (C2) infrastructure and maintain a threat actor
knowledgebase with data about more than 800 threat actors.

![Diagram showing the flow of data from Attackers, Malware Analysis Lab (MAL), Adversary Engagement Environment (AEE), Threat Actor Knowledgebase, Infrastructure, C2 Hunting, Security Researcher, Intel Factory to the 2024 Threat Roundup report.]

2024 Threat Roundup | 5

2. Main Findings
2.1. Location – Russia Retakes China’s Position

![Graph showing the distribution of attacks by IP address country of origin, with Russia at 16% and China at 8%.]

Figure 1 – Distribution of attacks by IP address country of origin

Figure 1 shows the distribution of attacks detected by country of origin. We detected attacks originating from 213
countries and territories (1 more than in 2023 and 22 more than in 2022). Countries appear in this list due to the
presence of legitimate hosting providers being abused by attackers; the presence of bulletproof hosting providers
that cater specifically to cybercriminal activities; or the use of compromised hosts to launch attacks.

This year, the top 10 countries accounted for 78% of the malicious traffic. This is a negligible difference of
1% more than in 2023 but consistent with the growth observed since 2022 (73%). The top 10 list of countries
originating attacks has only one entry different from 2023: Poland replaced Singapore. However, the ranks have
changed considerably. The most notable change: Russia rose from 9% to 16% of attacks. China decreased from
18% to 8%.

It is important to stress that it is not direct attribution for attack locations. It is only where we can see attacks
coming from as they hit our honeypots. Our threat actor database shows that most actors are still located in
China — although it does not necessarily mean it is the source of individual attacks.

Fact: China and Russia have been in the top 3 of IP address attack origin since 2022.

Insight for Defenders: Country of origin alone continues to be ineffective to judge the
risk of a particular IP address. However, if your organization does not do business with –
or in – countries with the highest number of IP addresses that attack, blocking those IP
ranges may help reduce SOC noise.

2024 Threat Roundup | 6

2.2. Autonomous Systems – New Techniques for Routing Attacks

![Graph showing the distribution of attacks by originating Autonomous System, with ISPs at 57%, Business/Government/Others at 33%, and Hosting/Cloud providers at 10%.]

Figure 2 – Distribution of attacks by originating Autonomous System

Attacks again originated from more than 500 autonomous systems (AS), which are blocks of IP addresses under
the control of an organization. Figure 2 shows the percentage of attacks coming from the three types of AS we
observe:

*   Internet Service Providers (ISPs) increased from 53% in 2023 to 57% in 2024
*   Business, Government, and others decreased from 36% to 33%.
*   Hosting or cloud providers decreased from to 11% to 10%.

Note that the percentages shown above differ from what was presented in last year’s report because we removed
the “unknown” category of AS and only show the numbers of those we can classify.

As we discussed last year, the large chunk of attacks coming from ISPs as well as business, government and
other organizations signifies an increase in the use of compromised devices to launch attacks as opposed to
leasing infrastructure from dedicated providers.

In 2023, we attributed this to the increased popularity of “residential proxy” services, where threat actors proxy
their traffic via applications running on residential devices, which typically have IP addresses managed by ISPs.
Residential proxies continue to be popular, with emerging threat actors specializing in selling access to hijacked
IoT devices for this very purpose, something we predicted in early 2023. However, advanced persistent threat
actors have now gone even further and developed Operational Relay Boxes (ORB) networks, where they mix
virtual private servers, compromised IoT and hijacked network perimeter devices, creating layers of proxying to
make detection and attribution of attacks more challenging.

On the cloud side, the use of Amazon and Google infrastructure continued to be significant, with those two alone
accounting for more than 11% of the attacks we observed. A notable change was that the major Chinese cloud
provider Alibaba jumped from 22nd most popular AS in 2023 to sixth in 2024.

Overall, the top 10 ASes are responsible for 48% of attacks (4% less than in 2023). Six ASes from the top 10
in 2023 remain in the list in 2024: Xhost Internet Solutions Lp, GOOGLE-CLOUD-PLATFORM, LIONLINK-
NETWORKS, DIGITALOCEAN-ASN, Contabo GmbH and Chang Way Technologies Co. Limited.

Fact: Autonomous Systems continue to be a better sign of risk than country of origin.

Insight for Defenders: IPs belonging to known risky autonomous systems should always
be treated with care — especially those that remain in the top 10 for years, such as
Digital Ocean. Continued attacker interest in compromised devices to route action shows
organizations need real-time threat intelligence about compromised devices in the wild
and the types of device attackers focus on. This goes beyond APTs targeting a specific
organization. Be wary of opportunistic Initial Access Brokers (IAB) that breach as many
organizations as possible and sell that access.

2024 Threat Roundup | 7

2.3. Attacked Services – the Web Is the Undisputed Leader

![Graph showing the distribution of attacked ports and services, with Web applications at 41%, Remote management at 33%, Remote storage at 19%, Networking at 3%, and Database at 1%.]

Figure 3 – Distribution of attacked ports and services

Figure 3 shows the share of traffic targeting each type of network service, classified according to assigned or
well- known IPv4 TCP destination ports: Web applications increased from 26% in 2022 and 2023 to 41% in 2024,
continuing to be the most attacked service type and widening with the gap with the other targets. Most attacks
against these services are either scanning or attempts at vulnerability exploitation (see section 2.5).

Remote management protocols, such as RDP and VNC for remote desktop, and SSH and Telnet for remote
terminals, increased from 26% in 2023 to 33% this year. It was 43% in 2022. Attacks on these protocols are
mainly brute forcing or password spraying (see section 2.4).

Remote storage protocols, such as SMB and FTP, remained relatively stable, changing from 20% to 19%,
continuing their decrease from 23% in 2022. Networking protocols, such as DNS, DHCP and CWMP/TR-069,
decreased from 10% to 3%, returning to the baseline in 2022 of 1%.

Database services, such as Microsoft SQL Server, Redis, mongoDB, MySQL and PostgreSQL, decreased from
6% to 1%, returning to 2022 levels.

E-mail services, such as IMAP, POP3 and SMTP, remained unchanged since 2022 at less than 1% of attacks.

Fact: Web applications are, without a doubt, the most attacked service type, continuing
the trend from 2023.

Insight for Defenders: Ensure that defenses, such as web application firewalls, are in
place to detect and prevent attacks such as command injections, cross-site scripting and
SQL injections as early as possible. The increase in attacks on remote management
protocols is also significant because most of those are related to credential-based attacks.
Best practices in credentials are paramount, such as avoiding default and easily guessed
passwords.

2024 Threat Roundup | 9

2.4. Weak Credentials – a Return to Generic Usernames

![Graph showing the percentage of generic usernames used in attacks, increasing from 85% in 2023 to 95% in 2024.]
![Graph showing the breakdown of specific usernames abused by attackers, with IoT devices at 35% in 2023 and Database, DevOps, and Cloud becoming more relevant in 2024.]
![Graph showing the top abused credentials by category, with generic usernames being the most prevalent.]
![Graph showing the top abused credentials by specific username type, highlighting IoT devices, Database, DevOps, and Cloud.]

Figure 4 – Top abused credentials

Figure 4 shows the most abused credentials we observed, divided in two categories:

Generic usernames include “root,” “admin,” “user,” “guest” and several other such credentials. The increase from
85% in 2023 to 95% in 2024 shows that attackers are again relying more heavily on brute-forcing and simple
dictionary attacks than on targeting specific devices. This is even higher than the 87% we observed in 2022.
Specific usernames (decreased from 15% to 5%) can be associated to specific roles, such as “www,” “backup,”
“deployer” or even specific applications and devices, such as “odoo,” “rpi,” “kafka,” “zabbix” or “ec2-user”

Even though the overall percentage of specific usernames decreased, it’s still relevant to analyze the breakdown
of types of specific usernames that attackers are abusing. In 2023, the most popular category was IoT devices
(35%), which is now the fourth most abused type of username. Database, DevOps and Cloud all became much
more relevant than in previous years. The data is consistent with what we discussed in section 2.3, since often
these types of services are web applications.

In the IoT category, the most popular usernames were “ubnt” (for Ubiquiti routers), “moxa” (for industrial
networking) and “zyfwp” (for Zyxel firewalls). In February 2024, we published an analysis of botnets targeting
Ubiquiti routers since there was a takedown of Moobot which had been commandeered by Russia’s APT28.

Fact: Best practices for credential management are crucial to prevent attacks leveraging
weak credentials.

Insight for Defenders: NIST released an updated version of its digital identity guidelines
in August 2024 that challenges some long-held assumptions in the cybersecurity
community about password complexity and the need for periodic changes.

2024 Threat Roundup | 10

2.5. Exploits – There’s Still Much Beyond KEV

![Graph showing the percentage of exploit attempts against web servers and applications, increasing from 14% in 2022 to 56% in 2024.]
![Graph showing the distribution of exploited vulnerabilities by category, with web applications at 56%, network infrastructure at 14%, software libraries at 14%, and IoT devices at 16%.]
![Table listing the top 10 most exploited vulnerabilities, including CVEs affecting Hikvision, Redis, Microsoft Windows, GitLab, Citrix NetScaler, and ConnectWise ScreenConnect.]

Figure 5 – Vulnerabilities exploited during the study period

Exploit attempts against web servers and applications have been on a steady rise since 2022, and continue as
the largest category we see:

*   2022: 14%
*   2023: 36%
*   2024: 56%

This is in line with what we observed for targeted services in section 2.3.

Exploits against network infrastructure devices, such as firewalls, routers, and VPN appliances increased from
3% in 2022 to 11% in 2023 and now 14%, becoming the second most popular category. We discussed this
ongoing trend in our 2024H1 threat review. Software libraries continue to decrease as a percentage of targets for
exploitation:

*   2022: 76%
*   2023: 29%
*   2024: 14%

Several categories of IoT devices and other applications known to be often exposed and vulnerable are also
routinely targeted, but this category decreased from 24% to 16%.

Three other observations are relevant: Five of the top 10 most exploited vulnerabilities we reported in 2023
remained in the list in 2024:

*   CVE-2021-36260 affecting Hikvision
*   CVE-2022-0543 affecting Redis
*   CVE-2021-38647 affecting Microsoft Windows
*   CVE-2020-0796 affecting Microsoft Windows
*   CVE-2021-22205 affecting GitLab

Two new entries are especially relevant: CVE-2023-4966 and CVE-2024-1709. CVE-2023-4966 which affects
Citrix NetScaler appeared as a 0-day in 2023 but continued to be heavily exploited in 2024. CVE-2024-1709,
affecting ConnectWise ScreenConnect, is notoriously easy to exploit and was used in ransomware campaigns.
Only one of these has been on the list since 2022: CVE-2022-0543 which affects Redis on Debian systems.

The percentage of exploited vulnerabilities not in CISA’s Known Exploited Vulnerabilities (KEV) increased from
65% to 73%. We published a study in May detailing this phenomenon and predicting that it would continue to
increase as attackers explore more of organizations’ attack surface beyond traditional endpoints.

When we merge our AEE data with observations from the Shadowserver foundation, we come up with a list of at
least 25 vulnerabilities affecting OT and Industrial IoT devices that are exploited by botnets or automated attacks
and which are not included in CISA’s KEV (shown below).

| Vendor           | Products                                    | CVEs