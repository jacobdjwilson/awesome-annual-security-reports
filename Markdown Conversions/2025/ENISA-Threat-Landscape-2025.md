# ENISA THREAT LANDSCAPE 2025

The official report URL is: https://www.enisa.europa.eu/publications/enisa-threat-landscape-2025

# Report Content Below

ENISA THREAT
LANDSCAPE 2025

OCTOBER 2025

0

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

ABOUT ENISA

The European Union Agency for Cybersecurity, ENISA, is the Union’s agency dedicated to achieving a high
common level of cybersecurity across Europe. Established in 2004 and strengthened by the EU Cybersecurity
Act, the European Union Agency for Cybersecurity contributes to EU cyber policy, enhances the
trustworthiness of ICT products, services and processes with cybersecurity certification schemes, cooperates
with Member States and EU bodies, and helps Europe prepare for the cyber challenges of tomorrow. Through
knowledge sharing, capacity building and awareness raising, the Agency works together with its key
stakeholders to strengthen trust in the connected economy, to boost resilience of the Union’s infrastructure,
and, ultimately, to keep Europe’s society and citizens digitally secure. More information about ENISA and its
work can be found here: www.enisa.europa.eu.

CONTACT

For contacting the authors please use etl@enisa.europa.eu
For media enquiries about this paper, please use press@enisa.europa.eu.

AUTHORS

Jamila BOUTEMEUR, Ifigeneia LELLA, Ilias BAKATSIS, Georgios CHATZICHRISTOS, Kevin FOLEY, Jussi
LESKINEN, Jakub OTCENASEK, Dominik ZIOLEK, ENISA.

EEAS STRATCOM.

CONTRIBUTORS

The ENISA Threat Landscape authors would like to express their appreciation to the EEAS STRATCOM and
Europol EC3 colleagues, as well as the ENISA Incident and Vulnerability reporting services (IVS) and CIRCL
colleagues for their active support to the report.

ACKNOWLDGEMENTS

The ENISA Threat Landscape authors would like to acknowledge the valuable feedback and validation of the
members of the National Liaison Officers (NLO) network, of the CSIRTs Network (CNW), and of the ENISA
Cyber Partnership Programme, as well as the comments received from our European Union Aviation Safety Agency
(EASA) colleagues, I4C+ (Information and Analysis Center for Cities), the Financial Services
Information and Analysis Center (FI-ISAC), and the European Rail Operators Information and Analysis Center
(Rail-ISAC).

We also want to thank our ENISA colleagues, Apostolos MALATRAS, Stefano DE CRESCENZO , Razvan
GAVRILA, Erika MAGONARA, Eleni PHILIPPOU, Edgars TAURINS, and Johannes CLOS for their input and
overall support.

LEGAL NOTICE

This publication represents the views and interpretations of ENISA, unless stated otherwise. It does not
endorse a regulatory obligation of ENISA or of ENISA bodies pursuant to the Regulation (EU) No 2019/881.
ENISA has the right to alter, update or remove the publication or any of its contents. It is intended for
information purposes only and it must be accessible free of charge. All references to it or its use as a whole or
partially must contain ENISA as its source.

1

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

Third-party sources are quoted as appropriate. ENISA is not responsible or liable for the content of the
external sources including external websites referenced in this publication.

Neither ENISA nor any person acting on behalf of ENISA is responsible for the use that might be made of the
information contained in this publication.

ENISA maintains its intellectual property rights in relation to this publication.

COPYRIGHT NOTICE
© European Union Agency for Cybersecurity (ENISA), 2025

This publication is licenced under CC-BY 4.0 “Unless otherwise noted, the reuse of this
document is authorised under the Creative Commons Attribution 4.0 International (CC BY 4.0) licence
(https://creativecommons.org/licenses/by/4.0/). This means that reuse is allowed,
provided that appropriate credit is given and any changes are indicated”.

For any use or reproduction of photos or other material that is not under the ENISA copyright,
permission must be sought directly from the copyright holders.

ISBN: 978-92-9204-723-8 ISSN: 2363-3050 DOI: 10.2824/1946374

2

TABLE OF CONTENTS

1. EXECUTIVE SUMMARY

2. METHODOLOGY

3. THREAT LANDSCAPE OVERVIEW

4. GENERAL KEY TRENDS

4.1 PHISHING REMAINS A PRIMARY INITIAL INTRUSION VECTOR

4.2 INCREASINGLY TARGETED CYBER DEPENDENCIES

4.3 CONTINUOUS TARGETING OF MOBILE DEVICES

4.4 THREAT GROUPS CONVERGING

4.5 PREDICTABLE USE OF AI

5. SECTORIAL ANALYSIS

5.1 PUBLIC ADMINISTRATION

5.2 TRANSPORT

5.3 DIGITAL INFRASTRUCTURE AND SERVICES

5.4 FINANCE

5.5 MANUFACTURING

6. CYBERCRIME

6.1 KEY CYBERCRIME THREATS

6.2 CYBERCRIME SECTORIAL IMPACT

6.3 CYBERCRIME GEOGRAPHICAL IMPACT

6.4 KEY CYBERCRIME TRENDS

7. STATE-ALIGNED ACTIVITIES

7.1 KEY STATE-ALIGNED THREATS

7.2 KEY STATE-ALIGNED TRENDS

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

5

6

7

10

10

10

11

12

13

15

16

19

21

24

25

27

27

30

31

32

35

36

41

3

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

8. FOREIGN INFORMATION MANIPULATION AND INTERFERENCE

8.1 KEY FIMI THREATS

8.2 KEY FIMI TRENDS

9. HACKTIVISM

9.1 KEY HACKTIVISM THREATS

9.2 HACKTIVISM GEOGRAPHICAL TARGETING

9.3 HACKTIVISM SECTORIAL TARGETING

9.4 KEY HACKTIVISM TRENDS

10. TTPS & VULNERABILITIES

10.1 OBSERVED TACTICS, TECHNIQUES & PROCEDURES (TTPS)

10.2 VULNERABILITIES

10.3 RECOMMENDATIONS

10.4 SYSTEM HARDENING

10.5 ACCESS & PRIVILEGE

10.6 NETWORK PROTECTIONS

10.7 MONITORING

10.8 RESILIENCE

11. OUTLOOK & CONCLUSION

12. APPENDIX

12.1 TACTICS, TECHNIQUES & PROCEDURES (TTPS)

12.2 VULNERABILITIES

12.3 LEXICON

43

43

45

48

48

50

51

52

55

55

56

60

61

61

61

61

62

63

63

80

84

4

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

1. EXECUTIVE SUMMARY

This year’s ENISA Threat Landscape (ETL) introduces a revised and concise format designed to deliver
insights through a threat-centric approach and enhanced contextualisation. This edition integrates additional
analysis of adversary behaviours, vulnerabilities and geopolitical drivers, aimed at both strategic and
operational audiences, offering an actionable perspective on trends shaping the EU’s cyber threat
environment.

The ETL 2025 provides an overview of the European cyber threat ecosystem from July 2024 to June
2025, drawing on nearly 4 900 selected and curated incidents. The reporting period highlights a maturing
threat environment characterised by rapid exploitation of vulnerabilities and growing complexity in tracking
adversaries.

Intrusion activity remains significant, with ransomware at its core. Cybercriminal operators notably
responded to the actions of law enforcement by decentralising operations, adopting aggressive extortion
tactics and capitalising on regulatory compliance fears. The continuous proliferation of ransomware-as-a-
service models, builder leaks and the services of access brokers has further lowered barriers to entry and
diversified ransomware families, fuelling a professionalised and resilient criminal ecosystem.

In parallel, state-aligned threat groups intensified their long-term cyberespionage campaigns against
the telecommunications, logistics networks and manufacturing sectors in the EU, demonstrating advanced
tradecraft such as supply chain compromise, stealthy malware frameworks and abuse of signed drivers.

Hacktivist activity continues to dominate reporting, representing almost 80% of recorded incidents and
driven primarily by low-level distributed denial-of-service operations. While overall resulting in very low impact,
these campaigns demonstrate how low-cost tools are scaled for ideology-driven operations.

Sectoral targeting patterns reinforce the EU’s systemic exposure. Public administration networks remain the
primary focus (38%), notably for hacktivists and state-nexus intrusion sets, while transport emerged as a
high-value sector, particularly maritime and logistics. Aviation and freight operations have faced ransomware
disruptions, while digital infrastructure and services remain strategic targets for both cyberespionage and
ransomware operators.

Phishing remains the dominant intrusion vector (60%) and is evolving through techniques used in large-
scale campaigns. The availability of phishing-as-a-service platforms demonstrates the industrialisation of
phishing operations, enabling adversaries of all skill levels to launch complex campaigns. Abuse of cyber
dependencies have also intensified, as shown by compromises in open-source repositories, malicious browser
extensions and breaches of service providers, amplifying risk throughout interconnected digital ecosystems.

Across all campaigns, adversaries continue to rely on a consistent set of tactics, techniques and procedures.
Vulnerability exploitation remains a cornerstone of initial access (21.3%), with widespread campaigns
rapidly weaponising them within days of their disclosure—underscoring the need to ensure patch availability
and to implement and enforce basic measures for cyber hygiene.

Artificial intelligence has become a defining element of the threat landscape. By early 2025, AI-
supported phishing campaigns reportedly represented more than 80 percent of observed social engineering
activity worldwide, with adversaries leveraging jailbroken models, synthetic media and model poisoning
techniques to enhance their operational effectiveness.

The threat landscape depicted in this edition reflects how the cyber threat landscape is shifting toward
mixed, possibly convergent pressure, with fewer single high impact incidents, and more continuous,
diversified and convergent campaigns that collectively erode resilience.

5

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

2. METHODOLOGY

The ENISA Cybersecurity Threat Landscape (ENISA CTL) updated methodology published in August 2025[^1]
was used to write the ETL.

For the purpose of the ETL 2025 report, ENISA analysts collected and analysed 4 875 incidents, mainly based
on information from open sources, as well as anonymised information shared by EU Member States (EU MSs)
and members of the ENISA Cyber Partnership Programme[^2]. The reporting period referred to spans from 1
July 2024 to 30 June 2025, with the cut-off date being 30 June 2025.

As much as possible, primary sources are referenced in footnotes to substantiate ENISA’s analysis and
assessments. ENISA appreciate that open sources and information shared voluntarily do not constitute a
complete picture of the cyber threat landscape. Moreover, multiple caveats are inherent to open-source
reporting. Those notably include reporting depth and temporality. For instance, vague sectorial or geographic
reporting (i.e., ‘private companies’, ‘Europe’) is likely to impact ENISA’s dataset. Another caveat is the proper
sectorial categorisation, especially when one incident impacts an organisation operating in multiple sectors. To
avoid inflating the threat, ENISA analysts proceeded to a thorough curation of the dataset either by choosing
one specific sector or by registering the incident as ’unknown’. While particular attention was paid to the
matter, it is highly likely a deviation will remain.

It should be noted that incidents are not necessarily reported immediately or confirmed in open sources. For
instance, where ransomware and DDoS are more immediate ‘visible’ threats, often claimed directly by their
operators, cyberespionage campaigns are typically documented with a delay spanning from 6 months to more
than 4 years. It should also be noted that, to some extent, increased reporting of a specific threat does not
necessarily reflect an increased tempo but rather speaks to the audience’s interest.

The incidents analysed in the Foreign Information Manipulation and Interference (FIMI) section have been
shared by the European External Action Service (EEAS) and based on the strategic FIMI monitoring efforts of
the EEAS. They reflects patterns seen in known sources related to overt FIMI, or independently imputed
operations by selected actors and on priority issues of the EEAS. The totality of the incidents used in the
EEAS sample refers to activities suspected to be linked to Russian Information Manipulation Sets to different
degrees. Data on cyber-related FIMI activities by other threat groups are not systemically collected. The
evidence presented serves illustrative purposes and should not be used to draw conclusions about general
trends in FIMI, as it reflects only a limited subset of threat actors’ activity.

Hence, this report should be seen as an overview of prevailing trends, constituting a snapshot of threats
faced by EU MSs and EU-based organisations.

To differentiate between what was reported by other sources and ENISA’s assessments, words of estimative
probability are used, with a matrix available in the Appendix.

Finally, the association of a threat with a particular nexus is solely based on attribution done by national
authorities globally, and imputation (aka technical attribution) achieved by trusted private vendors, all
referenced accordingly.

[^1]: https://www.enisa.europa.eu/sites/default/files/2025-08/ENISA%20CTL%20Methodology_Updated%20August%202025.pdf
[^2]: https://www.enisa.europa.eu/topics/cyber-threats/situational-awareness/enisa-cyber-partnership-programme-cpp

6

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

3. THREAT LANDSCAPE OVERVIEW

Based on the analysis of the dataset, social engineering tactics remain the primary entry point for threat
actors, with phishing (including vishing, malspam, and malvertising) accounting for about 60% of observed
cases. Exploitation of vulnerabilities (21.3%) remains a prevalent intrusion vector, followed by botnets (9.9%).
Malicious applications represent 8%, showing that compromised or trojanised software and applications
continue to play a role in system intrusions, while unauthorised access by insider threats (0.8%) contribute
smaller but still relevant shares. Overall, the distribution underscores that while phishing dominates the threat
landscape, technical exploits, malware delivery mechanisms and insider risks remain meaningful concerns.

The data shows clear contrasts between phishing and
vulnerability exploitation as intrusion vectors. While phishing
is the most common pathway, its impact is diverse.
Approximately 73% of phishing cases are classified as
unknown, reflecting unclear or varied follow-up of malicious
activities, and 27% led to intrusions. In terms of payloads,
phishing leads to the deployment of malicious code in 23%
of cases, suggesting it might be primarily used for malware-
less objectives. Vulnerabilities, on the other hand, show a
more focused risk profile. Nearly 70% of vulnerability cases
culminate in intrusions, with 30% categorised as unknown,
and 68% of these vulnerability-based incidents result in the
deployment of malicious code, indicating that the exploitation
of vulnerabilities is often a direct precursor to the installation
of malware.

The distribution of incident types is dominated by DDoS
attacks, which make up about 76.7% of recorded
cases. This category is overwhelmingly driven by
hacktivist groups, which account for the majority of
collected DDoS incidents, with cybercrime groups
contributing a marginal fraction, often tied to extortion
(e.g., ransom DDoS). Intrusions follow with 17.8%,
dominated by cybercriminal activities, followed by state-
aligned intrusion sets, which typically pursue
persistence. Hacktivists appear only marginally in
intrusion cases. Defacements were almost exclusively
associated with hacktivists, underlining their role as a
symbolic tactic for visibility and protest rather than a
sustained intrusion method.

7

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

The prevalence of cybercriminal-led intrusions is illustrated
through the type of malicious code deployed following
intrusions, as well as the outcome of recorded intrusions.
The combined share of ransomware, banking trojan, and
infostealers accounts for 87.3% of these intrusions.

Out of recorded intrusions, 68.6% led to data
breaches leaked on cybercriminal forums for sale,
including 2.8% of these advertised breaches being
presented as a direct outcome of a ransomware
attack. Data exfiltration, including credential theft
(8.9%) and strategic data collection (21.3%)
accounted for 30.2%.

The distribution of threat categories shows a clear
concentration in a few areas. Mobile threats account for the
largest share at 42.4%, highlighting how mobile devices
continue to be a primary attack surface. Web threats follow
with 27.3%, underlining the persistent exploitation of online
services and applications. Operational technology threats
represent 18.2%, reflecting the growing exposure of
industrial and critical systems as they continue being
increasingly connected and targeted. Supply chain risks
make up 10.6%, showing that attackers are actively
leveraging indirect pathways through third-party providers
and dependencies.

8

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

Based on assessed objectives, cyber activities
targeting or impacting the EU mostly pertained to
ideology-driven incidents exclusively carried out
by hacktivists through DDoS. Financially
motivated operations were primarily carried out by
cybercriminal operators, while a few cases were
associated to hacktivist groups, and state-aligned
threats. Finally, cyberespionage campaigns
accounted for 7.2%.

9

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

4. GENERAL KEY TRENDS

4.1 PHISHING REMAINS A PRIMARY INITIAL INTRUSION VECTOR

Phishing continued to be the primary method for initial intrusion, remaining an effective technique to carry out
credential theft, session hijacking, payload deployment or command execution.

ClickFix-style scams appeared during the reporting period with the technique gaining momentum in Q1 2025
for both cybercriminal and state-aligned intrusion sets[^3], often disguised as fake CAPTCHA prompts on
compromised or fraudulent websites[^4]. These overlays tricked users into executing PowerShell commands
under the pretext of human verification, leading to the installation of information stealers and loaders[^5].

Another innovative technique was the weaponisation of compromised WordPress sites to distribute info-
stealers through drive-by downloads. From Q2 2025, threat actors embedded fake CAPTCHA and verification
prompts into compromised websites to lure users into executing malicious payloads. The ClearFake campaign
saw the distribution of credential-stealing malware including Lumma and Vidar, resulting in 9 300 confirmed
infections. These campaigns leveraged legitimate browser interfaces and social engineering to create
convincing lures[^6].

Phishing-as-a-Service (PhaaS) platforms, designed to automate the generation of branded phishing kits by
cloning login pages and distributing links through templated infrastructure, enable low-skill operators to
emulate trusted brands. This is illustrated by the Darcula platform, seen impersonating more than 200
organisations, whose services were seen leveraged to target victims in more than a hundred countries[^7]. Another PhaaS called Lucid expanded their portfolio by supporting phishing campaigns via mobile messaging
services—iMessage and RCS— enabling over 169 targets in 88 countries[^8] to be reached. Additional PhaaS
developments include FlowerStorm, an adversary-in-the-middle kit mimicking Microsoft 365 portals and
bypassing MFA[^9].

Enabling endpoint protections evasion and email filtering, QR code phishing (aka quishing) was also
reportedly seen, as observed in the Scanception campaign, where malicious QR codes embedded in PDF
attachments were aimed at redirecting victims to credential harvesting pages hosted on trusted cloud
platforms; these targeted users globally, including in the EU[^10][^11].

4.2 INCREASINGLY TARGETED CYBER DEPENDENCIES

During the reporting period, cybercriminals increasingly targeted third-party providers, such as Digital
Services, highly likely as an opportunity to optimise the efficiency of their attacks[^12][^13]. In mid-2024, the
cyberespionage campaign Operation Digital Eye targeted professional IT providers in Southern Europe,
aiming to infiltrate supply chains. Compromise attempts were reportedly unsuccessful[^14]. In March 2025, Plus
Service, an external provider managing the Telemaco platform for multiple Italian transport companies
suffered a data breach involving unauthorised exfiltration to a remote cloud, prompting temporary access
restrictions while remediation was carried out. This notably resulted in the Mobilita di Marca (MoM) ticketing
systems being paralysed for two days, impacting several thousand commuters[^15]. The same campaign

[^3]: https://www.proofpoint.com/us/blog/threat-insight/around-world-90-days-state-sponsored-actors-try-clickfix
[^4]: https://www.proofpoint.com/us/blog/threat-insight/clipboard-compromise-powershell-self-pwn
[^5]: https://blog.sekoia.io/clickfix-tactic-the-phantom-meet/
[^6]: https://thehackernews.com/2025/03/clearfake-infects-9300-sites-uses-fake.html
[^7]: https://www.beyondidentity.com/resource/darcula-phishing-as-a-service-platform-that-autogenerates-branded-kits
[^8]: https://thehackernews.com/2025/04/lucid-phaas-hits-169-targets-in-88.html
[^9]: https://www.darktrace.com/blog/from-rockstar2fa-to-flowerstorm-investigating-a-blooming-phishing-as-a-service-platform
[^10]: https://cyble.com/blog/scanception-a-qriosity-driven-phishing-campaign/
[^11]: https://www.darkreading.com/endpoint-security/criminals-send-qr-codes-phishing
[^12]: https://www.scworld.com/brief/cbs-affiliate-purportedly-compromised-by-lynx-ransomware-gang
[^13]: https://news.sophos.com/en-us/2025/05/27/dragonforce-actors-target-simplehelp-vulnerabilities-to-attack-msp-
customers/
[^14]: https://www.sentinelone.com/labs/operation-digital-eye-chinese-apt-compromises-critical-digital-infrastructure-via-visual-
studio-code-tunnels/
[^15]: https://www.tribunatreviso.it/cronaca/mon-hacker-attacco-biglietti-xueo4que

10

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

impacted the Busitalia Veneto app and subscription portal, and ATM Milano[^16][^17]. Other relevant examples
include the targeting of Berliner Verkehrsbetriebe (BVG)’s external service provider in May 2025, affecting the
data of 180 000 BVG customers[^18], and unauthorised access to Spanish energy company Repsol’s customers,
resulting from the compromise of one of the company’s providers[^19].

Adversaries were also seen exploiting the digital supply chain, notably by compromising software,
repositories or browser extensions[^20]. Since 2022, and increasingly observed over the reporting period, DPRK-
nexus Lazarus leveraged supply chain compromise, with its most recent activities pertaining to the
deployment of malicious Node Package Manager (npm) packages in GitHub repositories, mimicking legitimate
libraries to compromise developers’ environments[^21][^22][^23]. Of note, repositories remain particularly exposed to
secret sprawls stemming from insufficient protection with detected secrets reportedly increasing by 25%
between 2023 and 2024[^24]. A surge in attacks leveraging malicious browser extensions was observed in late
2024, with a campaign that compromised multiple companies’ Chrome browser extensions; these notably
targeted extensions related to Artificial Intelligence and Virtual Private Networks (VPN)[^25][^26][^27][^28].

4.3 CONTINUOUS TARGETING OF MOBILE DEVICES

Q1 2025 observed an increased level of reporting pertaining to the targeting of mobile devices, with Android
devices facing a higher level of threat.

Q3 2024 reportedly saw an uptick in the exploitation of outdated devices by the deployment of the Rafel
RAT, primarily targeting Android devices for financially-motivated and cyberespionage purposes, notably in
Czechia, France, Germany, Italy and Romania[^29], as well as the re-emergence of the Medusa banking trojan
updated with new features, and expanding their victimology to France and Italy[^30]. Medusa was notably
observed focusing on On-Device Fraud (ODF) through Account Takeover (ATO). Leveraging the same
technique, BingoMod RAT was observed draining bank accounts and wiping devices, a concerning
evolution[^31].

Android spyware for surveillance purposes used by State-aligned intrusion sets were also increasingly
documented, with Reaper’s Android spyware KoSpy[^32], or Android spyware BoneSpy and PlainGnome
leveraged by Uzbekistan-nexus Sandcat. Of particular interest is a report documenting EagleMsgSpy, a legal
intercept surveillance program targeting Android devices, reportedly developed by Wuhan Chinasoft Token
Information Technology Co., Ltd. and used by Chinese Public Security Bureaus since at least 2017[^33]. In
February, multiple cybersecurity vendors published reports pertaining to the targeting of mobile devices by
Russia-nexus intrusion sets. Google Threat Intelligence Group (GTIG) reportedly observed Sandworm,
UNC5792, UNC4221 (aka UAC-0185) targeting the WhatsApp, Signal and Telegram accounts of individuals in
Ukraine[^34]. Notably Sandworm was observed enabling Russian military forces to connect Signal accounts on
devices collected on the battlefield to actor-controlled infrastructure for follow-on exploitation. Sandworm was
also observed abusing the ‘linked devices’ feature, by crafting malicious QR codes to link a victim's account to
an actor-controlled Signal instance, and operating WAVESIGN. Volexity and Microsoft also reported on the

[^16]: https://www.fsbusitalia.it/it/veneto/news-veneto/2025/4/9/comunicazione-di-una-violazione-dei-dati-personali-agli-
interess.html
[^17]: https://www.atm.it/it/AtmNews/AtmInforma/Pagine/comunicazioneutentiappATM.aspx
[^18]: https://www.bvg.de/de/unternehmen/medienportal/pressemitteilungen/2025-05-15-statment-it-angriff-dienstleister
[^19]: https://www.publico.es/economia/repsol-sufre-ciberataque-compromete-datos-miles-clientes-electricidad-gas.html
[^20]: https://thehackernews.com/2025/05/over-70-malicious-npm-and-vs-code.html
[^21]: https://www.sonatype.com/hubfs/White_Papers/How-North-Korea-Backed-Lazarus-Group-is-Weaponizing-Open-Source-
Whitepaper.pdf
[^22]: https://socket.dev/blog/north-korean-apt-lazarus-targets-developers-with-malicious-npm-package
[^23]: https://socket.dev/blog/lazarus-strikes-npm-again-with-a-new-wave-of-malicious-packages
[^24]: https://blog.gitguardian.com/the-state-of-secrets-sprawl-2025/
[^25]: https://www.cyberhaven.com/blog/cyberhavens-chrome-extension-security-incident-and-what-were-doing-about-it
[^26]: https://www.darktrace.com/fr/blog/cyberhaven-supply-chain-attack-exploiting-browser-extensions
[^27]: https://www.malwarebytes.com/blog/news/2025/01/google-chrome-ai-extensions-deliver-info-stealing-malware-in-broad-
attack
[^28]: https://blog.sekoia.io/targeted-supply-chain-attack-against-chrome-browser-extensions/
[^29]: https://research.checkpoint.com/2024/rafel-rat-android-malware-from-espionage-to-ransomware-operations/
[^30]: https://www.cleafy.com/cleafy-labs/medusa-reborn-a-new-compact-variant-discovered
[^31]: https://www.cleafy.com/cleafy-labs/bingomod-the-new-android-rat-that-steals-money-and-wipes-data
[^32]: https://www.lookout.com/threat-intelligence/article/lookout-discovers-new-spyware-by-north-korean-apt37
[^33]: https://www.lookout.com/threat-intelligence/article/eaglemsgspy-chinese-android-surveillanceware
[^34]: https://cloud.google.com/blog/topics/threat-intelligence/russia-targeting-signal-messenger

11

ENISA THREAT LANDSCAPE 2025
TLP:CLEAR | October 2025

leveraging of Signal, as part of a recent spearphishing campaign conducted by CozyLarch UTA0304,
UTA0307 and Storm-2372[^35].

In October 2024, Qualcomm published a vulnerability impacting its Qualcomm’s Digital Signal Processor
(DSP) software[^36]. The vulnerability has an impact on chipsets widely used by various mobile devices and was
reported to have been exploited in the wild[^37].

In 2025, iVerify published an in-depth technical report revealing that state-linked telecommunications providers
continue to exploit vulnerabilities in outdated mobile signalling protocols—specifically SS7 and
Diameter[^38]. These protocols, which underpin global mobile communications, were not designed with
encryption or strong authentication, leaving them susceptible to interception, location tracking and session
hijacking. iVerify demonstrated that operators with privileged access to international telecom infrastructure—
such as China Mobile International and China Telecom Global—can remotely monitor and manipulate mobile
communications across borders without needing access to the target’s device. These operations are silent,
infrastructure-level and difficult to detect, posing significant risks to diplomats, journalists, and political actors.

4.4 THREAT GROUPS CONVERGING

Across the period, the lines between hacktivism, cybercrime and state-nexus activity continued to blur.
Intrusion sets historically distinguished by TTPs’ level of advancement. conducted activities, or assessed
objectives increasingly shared toolsets and modus operandi.

This was notably exemplified by hacktivist-led DDoS waves by pro-Russia groups around electoral events,
where increased activity was often observed as typical FIMI-aligned behaviour to associate disruption with
aspects of information operations. A prominent facet of this trend is faketivism, where state-aligned intrusion
sets leverage hacktivist personas and activities. Notable examples include Cyber Army of Russia Reborn,
associated to Russia-nexus Sandworm[^39], and the CyberAv3ngers group linked to Iran’s IRGC[^40].

In parallel, hacktivist tooling and criminal ecosystems increasingly intersect. FunkSec’s emergence in
late 2024 brought FunkLocker ransomware, blending political messaging with financial extortion, underscoring
how quickly ideology-driven branding can pivot to monetisation[^41][^42][^43]. Hacktivists, seeking funding and
visibility, embraced ransomware beyond DDoS and defacements. CyberVolk, operating in line with Russian
interests, has used and promoted multiple strains—AzzaSec, HexaLocker, Parano, as well as LockBit and
Chaos—since May 2024[^44][^45][^46]. KillSec, originally a pro-Russia hacktivist brand aligned with Anonymous,
debuted its platform in June 2024[^47].

Another aspect of this trend is the false-flag operation carried out by Turla, taking over Transparent Tribe’s
infrastructure[^48][^49], or cybercriminals masquerading as other cybercriminal groups or spoofing their brand,
as notably seen with email extortion campaigns impersonating the CL0P ransomware group[^50], physical

[^35]: https://www.volexity.com/blog/2025/02/13/multiple-russian-threat-actors-targeting-microsoft-device-code-authentication/
[^36]: https://docs.qualcomm.com/product/publicresources/securitybulletin/october-2024-bulletin.html
[^37]: https://securitylab.amnesty.org/latest/2024/12/a-digital-prison-surveillance-and-the-suppression-of-civil-society-in-serbia/
[^38]: https://iverify.io/blog/abusing-data-in-the-middle-surveillance-risks-in-china-s-state-owned-mobile-ecosystem
[^39]: https://cloud.google.com/blog/topics/threat-intelligence/apt44-unearthing-sandworm
[^40]: https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a
[^41]: https://research.checkpoint.com/2025/funksec-alleged-top-ransomware-group-powered-by-ai/
[^42]: https://therecord.media/funksec-ransomware-using-ai-malware
[^43]: https://research.checkpoint.com/2025/funksec-alleged-top-ransomware-group-powered-by-ai/
[^44]: https://www.rapid7.com/blog/post/2024/10/03/ransomware-groups-demystified-cybervolk-ransomware/
[^45]: https://detect.fyi/cybervolks-ransomware-ad38134b1b0a
[^46]: https://www.sentinelone.com/labs/cybervolk-a-deep-dive-into-the-hacktivists-tools-and-ransomware-fueling-pro-russian-
cyber-attacks/
[^47]: https://thecyberexpress.com/killsec-launches-raas-program/
[^48]: https://www.microsoft.com/en-us/security/blog/2024/12/04/frequent-freeloader-part-i-secret-blizzard-compromising-storm-
0156-infrastructure-for-espionage/
[^49]: https://blog.lumen.com/snowblind-the-invisible-hand-of-secret-blizzard/
[^50]: https://www.barracuda.com/