# Cyber Threats 2022: A Year in Retrospect

## Table of Contents
- [Cyber Threats 2022: A Year in Retrospect](#cyber-threats-2022-a-year-in-retrospect)
- [About us](#about-us)
- [Key events in 2022](#key-events-in-2022)
- [Fallout of Log4Shell](#fallout-of-log4shell)
- [Russian invasion of Ukraine](#russian-invasion-of-ukraine)
- [Sanctions and responses from the West](#sanctions-and-responses-from-the-west)
- [Sabotage operations and overlaps](#sabotage-operations-and-overlaps)
- [Wipers](#wipers)
- [Phishing operations](#phishing-operations)
- [Circling the cyber crime wagons](#circling-the-cyber-crime-wagons)
- [Dark Crystal RAT activity in Ukraine](#dark-crystal-rat-activity-in-ukraine)
- [China-based threat actors optimising operations](#china-based-threat-actors-optimising-operations)
- [Red Scylla, a Winnti-linked global threat](#red-scylla-a-winnti-linked-global-threat)
- [RedRelay, a shared proxy network](#redrelay-a-shared-proxy-network)
- [Country-specific targeting](#country-specific-targeting)
- [Persistent focus on telecommunications](#persistent-focus-on-telecommunications)
- [Iran’s internal and external challenges](#irans-internal-and-external-challenges)
- [Sanctions and enablers of cyber operations](#sanctions-and-enablers-of-cyber-operations)
- [Sabotage attacks](#sabotage-attacks)
- [Domestic and dissident targeting](#domestic-and-dissident-targeting)
- [Sector and regional targeting trends](#sector-and-regional-targeting-trends)
- [Other regional case studies](#other-regional-case-studies)
- [Black bag operations for the money](#black-bag-operations-for-the-money)
- [Talent Need Not Apply: Advanced Persistent Threats using job-themed lures](#talent-need-not-apply-advanced-persistent-threats-using-job-themed-lures)
- [WIRTING about White Dev 21](#wirting-about-white-dev-21)
- [An in-Tur-esting development](#an-in-tur-esting-development)
- [What’s up with White Dev 140?](#whats-up-with-white-dev-140)
- [A tailored response?](#a-tailored-response)
- [Notable developments of the overall cyber criminal ecosystem](#notable-developments-of-the-overall-cyber-criminal-ecosystem)
- [Ransomware developments](#ransomware-developments)
- [Leak site analysis](#leak-site-analysis)
- [White Janus with the lion’s share](#white-janus-with-the-lions-share)
- [Seeing BlackMatter in BlackCat](#seeing-blackmatter-in-blackcat)
- [An unwelcome professionalisation of RaaS programmes](#an-unwelcome-professionalisation-of-raas-programmes)
- [Bug bounty programme and searchable databases](#bug-bounty-programme-and-searchable-databases)
- [High pressure tactics in ransomware negotiations](#high-pressure-tactics-in-ransomware-negotiations)
- [Blue Cronus operations and updates](#blue-cronus-operations-and-updates)
- [Sizing up the precursors](#sizing-up-the-precursors)
- [Bumblebee](#bumblebee)
- [IcedID](#icedid)
- [Qakbot](#qakbot)
- [White Taranis’ reactivation by Blue Cronus](#white-taranis-reactivation-by-blue-cronus)
- [Hackers, fraudsters and stealers](#hackers-fraudsters-and-stealers)
- [LAPSUS$ in judgement](#lapsus-in-judgement)
- [Liars, cheats and thieving raccoons](#liars-cheats-and-thieving-raccoons)
- [Phishing with dynamite](#phishing-with-dynamite)
- [Not just a Glitch](#not-just-a-glitch)
- [Attack insights and trends](#attack-insights-and-trends)
- [Tooling and frameworks](#tooling-and-frameworks)
- [Detecting Cobalt Strike](#detecting-cobalt-strike)
- [Brute Ratel](#brute-ratel)
- [Detecting Brute Ratel](#detecting-brute-ratel)
- [Sliver](#sliver)
- [Detecting Sliver](#detecting-sliver)
- [No macros, no problem?](#no-macros-no-problem)
- [More MFA, more evasion](#more-mfa-more-evasion)
- [Lessons from the Blue Dev 5 (a.k.a. NOBELIUM) MFA evasion incident](#lessons-from-the-blue-dev-5-a-k-a-nobelium-mfa-evasion-incident)
- [Targeting the clouds](#targeting-the-clouds)
- [Lessons from the Blue Dev 5 (a.k.a. NOBELIUM) CSP compromise incident](#lessons-from-the-blue-dev-5-a-k-a-nobelium-csp-compromise-incident)
- [Additional insights from our incident response cases](#additional-insights-from-our-incident-response-cases)
- [White Baku case study](#white-baku-case-study)
- [Lessons from the White Baku (a.k.a. Cuba) incident involving ProxyShell](#lessons-from-the-white-baku-a-k-a-cuba-incident-involving-proxyshell)
- [Black Artemis case study](#black-artemis-case-study)
- [Lessons from the Andariel incident involving DTrack](#lessons-from-the-andariel-incident-involving-dtrack)
- [Looking ahead](#looking-ahead)
- [Threat actor-specific targeting anticipated in 2023](#threat-actor-specific-targeting-anticipated-in-2023)
- [PwC Cybersecurity](#pwc-cybersecurity)
- [Appendix A - Methodology](#appendix-a-methodology)
- [Appendix B - Threat actor reference](#appendix-b-threat-actor-reference)
- [Appendix C - Executive companion](#appendix-c-executive-companion)
- [Appendix D - Defender index](#appendix-d-defender-index)

1 | Cyber Threats 2022: A Year in Retrospect
Throughout 2022, the cyber threat landscape reflected real world
events and geopolitical tensions, with much of the year impacted by
the Russian invasion of Ukraine. Log4Shell ushered in a chaotic start
to 2022 and highlighted the positive impact of industry collaboration, as
well as the criticality of patching and understanding the footprint of
widely used software in environments.
Log4Shell was an edge case in terms of vulnerabilities disclosed in 2022, as threat actors
continued to make use of known vulnerabilities, exploits and tools (e.g. Cobalt Strike) when
conducting their attacks. However, throughout 2022 we also saw threat actors ranging in
motivation and sophistication employing enhanced tooling and frameworks, as well as
modifying their behaviours to outmanoeuvre security practices implemented by defenders.
Further, threat actors increasingly targeted cloud environments as well as identity and
privileged access capabilities in 2022.
As the Russian invasion escalated into full scale war, Ukraine along with other governments
and cyber security organisations around the world tracked and responded to a series of
sabotage efforts by Russia-based threat actors deploying multiple variants of wiperware.[^1], [^2], [^3] These sabotage attacks were largely contained within the immediate conflict zone, i.e.
within Ukraine and territories annexed by Russia, and did not have the same level of impact
as seen in 2015 and 2016 when Russia-based threat actors targeted Ukraine’s energy grid.
Whilst multiple espionage motivated threat actors reacted and aligned to this world-
changing event, as seen through notable shifts in phishing and targeting operations, the
war prompted some cyber criminal threat actors and hacktivists (e.g. Blue Kurama a.k.a.
Killnet) to react and respond in their operations and public statements, such as by declaring
[^1]: ‘ESET Research jointly presents Industroyer2 at Black Hat USA with Ukrainian government representative’, ESET, https://www.eset.com/int/about/newsroom/press-releases/events/eset-research-jointly-presents-industroyer2-at-black-hat-usa-with-ukrainian-government-representativ/ (25th August 2022)
[^2]: ‘NCSC advises organisations to act following Russia’s attack on Ukraine’, UK National Cyber Security Centre (NCSC), https://www.ncsc.gov.uk/news/organisations-urged-to-bolster-defences (18th March 2022)
[^3]: ‘Alert AA22-110A - Russian State-Sponsored and Criminal Cyber Threats to Critical Infrastructure’, US Cybersecurity & Infrastructure Agency (CISA), https://www.cisa.gov/uscert/ncas/alerts/aa22-110a (20th April 2022)

2 | Cyber Threats 2022: A Year in Retrospect
pro-Ukraine or pro-Russia stances and targeting government and private sector entities
perceived as opposition in the context of the war.
In addition to the Russian war in Ukraine, the cyber threat landscape in 2022 saw a
continued optimisation and sophistication of China-based threat actor operations, although
the targets of these operations did not significantly change from those seen in prior years.
These threat actors increasingly employed obfuscation-as-a-service capabilities, including
proxy networks (e.g. RedRelay) and shared malware, exploits and toolsets (e.g.
ShadowPad and ScanBox). The most prominent and prolific threat actor using these
capabilities was Red Scylla (a.k.a. CHROMIUM, ControlX, Earth Lusca, Aquatic Panda),
which targeted at least 70 organisations around the world. Other threat actors flexed
sophisticated operations impacting numerous regions, with some threat actors continuing
their focus on the telecommunications sector.
Iran-based threat actors continued to make headlines in 2022 for their involvement in
sabotage attacks against the Albanian government, their targeting of protesters and
dissidents and sectoral targeting against organisations largely in the Middle East, Europe
and the United States - activities which often aligned with priorities of the Iranian regime.
North Korea-based threat actors doubled down on financial theft through their continued
targeting of financial services, cryptocurrency and decentralised finance (DeFi)
organisations.
Overall, the advanced persistent threats (APTs) we analysed in 2022 appeared to largely
conform to previously observed targeting patterns despite continued efforts within corners
of the international community to economically isolate their respective countries, although
some threat actors made significant advancements in their operations. Whilst we presume
Western-based actions occurred in 2022, we did not identify adequate evidence of these
activities, and therefore they are not covered extensively in this report.
The cyber criminal ecosystem also demonstrated operational enhancements in some
cases, as well as new developments which challenged organisations around the world
throughout 2022. Whilst ransomware remained the top concern for many, we did see
indications of a potential regroup or recalibration among some of the more prolific and
prominent ransomware threat actors, and 2022 ended with a nearly identical number of
leak site victims compared to 2021.
One of the most concerning threat actors with high profile victims in 2022 was White Dev
111 (a.k.a. LAPSUS$ Group), which engaged in a string of “smash-and-grab” and “hack-
and-leak” operations against their targets. Many of these attacks used social engineering
and other tactics to exhaust security measures and users employed by victim
organisations. Cyber-enabled fraud was also rampant throughout 2022, further
underscoring the trend of threat actors commoditising access, exploits and tooling and
lowering the barrier to entry for a wider range of cyber criminals.

3 | Cyber Threats 2022: A Year in Retrospect
About us
PwC serves more than 200,000 clients in 152 countries, and we use our vantage point as one of
the largest international professional services networks to provide global threat intelligence
services, tailored and delivered locally to our clients. Our research underpins our security services
and is used by public and private sector organisations around the world to protect networks,
provide situational awareness and inform strategy.
PwC Threat Intelligence combines our detection capabilities with threat-focused research as well
as our proactive efforts to recognise emerging issues, building opportunities to identify and
counter gaps in our detection of malicious activity, enrich our threat knowledge and integrate
actionable intelligence into our reporting. Our Threat Intelligence team is comprised of members
spanning the globe, including Australia, Germany, Italy, the Netherlands, Norway, Sweden, the
United Kingdom and the United States. In this report, we provide numerous detection examples[^4]
that have fueled our threat intelligence and informed resilient cyber strategies.
[^4]: Please see Appendix D - Defender index for a quick guide to all detection content in this report.

4 | Cyber Threats 2022: A Year in Retrospect
Key events in 2022
- Fallout of Log4Shell
- Russian invasion of Ukraine
- China-based threat actors optimising operations
- Iran’s internal and external challenges
- Other regional case studies

5
Cyber criminal ecosystem shifts
39
Attack insights and trends
52
Looking ahead
68
Appendices
- Appendix A - Methodology
- Appendix B - Threat actor reference
- Appendix C - Executive companion
- Appendix D - Defender index
71
Detection Content
Incident response
More information
insights
available
Insights from specific
Key takeaways
Threat insights
PwC firms

5 | Cyber Threats 2022: A Year in Retrospect
Some of the events from 2022 detailed in this report:

6 | Cyber Threats 2022: A Year in Retrospect
Fallout of Log4Shell
Publicly disclosed in December 2021, the critical vulnerability known as Log4Shell (CVE-
2021-44228), present within certain versions[^5] of Apache Log4j software, initiated a chaotic
start to 2022 for organisations around the world.[^6] The ubiquitous nature of Apache Log4j
software meant entities across sectors and countries needed to respond to the Log4Shell
vulnerability disclosure. This urgency was further exacerbated by a proof of concept freely
available soon after the disclosure, providing instructions for exploiting this vulnerability and
allowing for any type of attacker to remotely execute code on an impacted system.
Organisations scrambled to discover Log4j instances within their environments and Apache
worked to develop a patch whilst threat actors began exploiting this opportunity within
hours of the disclosure.[^7]
Detecting Log4Shell exploitation
A simple, and broad, network detection option is to inspect all inbound traffic to exposed
servers for the string `${jndi: - or to account for some common evasion techniques by
looking for ${ followed shortly by jndi.
By the end of December 2021, Apache released numerous updates to address Log4Shell.
The international security community and various government agencies also provided
information regarding which versions of the popular software contained security fixes, as
well as which software still required attention.[^8], [^9] This collective effort likely made a
difference in quelling the chaos; however, threat actors still managed to exploit Log4Shell
throughout 2022, as well as the associated Log4j vulnerabilities CVE-2021-45046 and
CVE-2021-45105, discovered after initial remediation attempts were made.
Since the Log4Shell disclosure, dozens of espionage and financially motivated threat actors
have exploited this vulnerability across a variety of sectors.[^10] In one example from 2022,
eight months after the Log4Shell disclosure, Yellow Nix (a.k.a. MuddyWater, MERCURY)[^11]
[^5]: Note: When originally discovered, Log4Shell impacted Apache Log4j versions 2.0-beta9 to 2.14.1, and subsequent releases spawned additional vulnerabilities, remediated by version 2.17.0. Source: ‘Alert AA21-356A - Mitigating Log4Shell and Other Log4j-Related Vulnerabilities’, CISA, https://www.cisa.gov/uscert/ncas/alerts/aa21-356a (23rd December 2021)
[^6]: CTO-QRT-20211210-01A - Active scanning of CVE-2021-44228
[^7]: ‘Guidance for preventing, detecting, and hunting for CVE-2021-44228 Log4j 2 exploitation’, Microsoft, https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/ (11th December 2021)
[^8]: ‘Apache Log4j Vulnerability Guidance’, CISA, https://www.cisa.gov/uscert/apache-log4j-vulnerability-guidance (December 2021)
[^9]: ‘Alert: Apache Log4j vulnerabilities’, NCSC, https://www.ncsc.gov.uk/news/apache-log4j-vulnerability (10th December 2021)
[^10]: ‘Guidance for preventing, detecting, and hunting for CVE-2021-44228 Log4j 2 exploitation’, Microsoft, https://www.microsoft.com/security/blog/2021/12/11/guidance-for-preventing-detecting-and-hunting-for-cve-2021-44228-log4j-2-exploitation/ (11th December 2021)
[^11]: Note: We documented one such example in CTO-TIB-20221007-01A - Yellow Nix with a new access trick, alongside PowerShell scripts.

7 | Cyber Threats 2022: A Year in Retrospect
exploited the vulnerability in SysAid, an IT support and management product, to gain
access to organisations in Israel, according to a Microsoft report.[^12] Whilst instances of
unmitigated Log4j are still being exploited in the wild, routine exploitation of Log4Shell is
likely as prevalent as other well known vulnerabilities[^13] from 2022, including CVE-2022-
41040 and CVE-2022-41082, collectively known as ProxyNotShell.[^14]
Whilst numerous vulnerabilities were disclosed in 2022, Log4Shell reached peak
criticality due to the ubiquitous nature of Apache Log4j software, challenges in
identifying impacted systems and threat actor persistence in scanning for vulnerable
systems and exploiting those not updated or patched. The impact of Log4Shell
would likely have been far worse were it not for the impressive response of
defenders and the collective efforts of the international security community.
[^12]: ‘MERCURY leveraging Log4j 2 vulnerabilities in unpatched systems to target Israeli organizations’, Microsoft, https://www.microsoft.com/security/blog/2022/08/25/mercury-leveraging-log4j-2-vulnerabilities-in-unpatched-systems-to-target-israeli-organizations/ (25th August 2022)
[^13]: ‘Alert AA22-117A - 2021 Top Routinely Exploited Vulnerabilities’, CISA, https://www.cisa.gov/uscert/ncas/alerts/aa22-117a (27th April 2022)
[^14]: CTO-QRT-20221003-01A - ProxyNotShell

8 | Cyber Threats 2022: A Year in Retrospect
Russian invasion of Ukraine
On 24th February 2022, Russia invaded Ukraine and attacked Ukrainian infrastructure with
air and missile strikes.[^15] This invasion followed months of increasingly aggressive rhetoric
from the Russian government and years of Ukraine’s territorial integrity being violated,
including Russia’s 2014 annexation of the Crimean peninsula and the de facto separation of
the self-proclaimed, Moscow-backed Luhansk and Donetsk People’s Republic (L/DPR)
regions in eastern Ukraine. The invasion also set the stage for broader geopolitical
implications throughout 2022, such as additional countries requesting to join the North
Atlantic Treaty Organisation (NATO).[^16]
Ukraine has been a persistent target for Russia-based threat actors throughout the past
decade, including numerous cyber attacks against the Ukrainian power grid in 2015 and
2016.[^17] Blue Echidna’s (a.k.a. Sandworm) NotPetya attacks were initially thought to be
ransomware deployed against a Ukrainian finance management application; however,
NotPetya turned out to be destructive wiperware with devastating consequences for
companies beyond Ukraine’s borders that used the targeted software.
Memories of NotPetya weighed heavily as Russian wipers began propagating amongst
Ukrainian targets in January 2022 and continued during the initial months of the invasion,
although the impact of these was contained and much more limited than expected due to
the efforts of Ukraine, other governments and security industry partners.[^18] In particular,
Russia-based threat actors focused on the Ukrainian Defence Ministry and PrivatBank,
Ukraine’s largest commercial bank, in the first days of the invasion.[^19] Whilst many around
the world feared a major spillover of cyber activity outside of the conflict zone, as seen with
NotPetya, this did not materialise by the end of 2022.
[^15]: CTO-SIB-20220224-01A - Tensions escalate into invasion
[^16]: CTO-SIB-20221102-01A - NATO expansion - Finland and Sweden’s changing cyber threat landscape
[^17]: CTO-SIB-20220127-01A - Russia and Ukraine: on the brink
[^18]: ‘ESET Research jointly presents Industroyer2 at Black Hat USA with Ukrainian government representative’, ESET, https://www.eset.com/int/about/newsroom/press-releases/events/eset-research-jointly-presents-industroyer2-at-black-hat-usa-with-ukrainian-government-representativ/ (25th August 2022)
[^19]: ‘Ukraine defence ministry website, banks, knocked offline’, Reuters, https://www.reuters.com/world/europe/ukraine-reports-cyber-attack-defence-ministry-website-banks-tass-2022-02-15/ (15th February 2022)

9 | Cyber Threats 2022: A Year in Retrospect
In the following sections, we detail notable events and trends related to cyber threat actors
and their activities leading up to and during the war, such as sabotage operations, phishing
operations and intersections with cyber criminal threat actors and techniques.
The impact of threat actor operations had been anticipated, with numerous government
agencies publishing mitigation advice that broadly countered the key tools, techniques and
procedures (TTPs) of threat actors like Blue Athena (a.k.a. APT28, FANCY BEAR) and Blue
Overall, we observed Russia-based threat actors focusing their sabotage
operations on the immediate conflict zone, with few exceptions impacting entities
outside of Ukraine; however, broader phishing activities by Russia-based threat
actors targeted an array of countries and organisations around the world, and in
some cases used Ukraine-themed lures.

10 | Cyber Threats 2022: A Year in Retrospect
Kitsune (a.k.a. APT29, COZY BEAR), as well as provided threat actor indicators.[^20], [^21] The
private sector also contributed to these efforts, with examples from Mandiant[^22] and
Dragos[^23] demonstrating the collective support to defenders in exposing destructive
capabilities targeting operational technology (OT) systems.
Sanctions and responses from the West
Western responses to Russia’s invasion of Ukraine included a series of sanctions and
widespread public condemnation. These sanctions have resulted in significant economic
repercussions for Russia, with a variety of sanctions being imposed on organisations and
individuals, such as Russian President Vladimir Putin and other high ranking politicians and
officials. Immediately following the initial invasion, select Russian financial institutions were
excluded from the SWIFT network, the main global payment messaging system.[^24], [^25] European
Union member countries, the United Kingdom, the United States and other countries further
sanctioned Russia in the form of supply chain restrictions and other actions, whilst numerous
foreign brands elected to pause or withdraw Russian operations due to ethical considerations
and public sentiment.[^26]
For some strategic sectors, these restrictions have impacted Russia’s ability to
access key components and technologies, and Russia has since begun
investigating alternatives, such as replacement components and illicit supply
chains. As Russia protracts its war and becomes increasingly isolated, we assess
Russia-based, espionage motivated threat actors will likely pivot targeting
objectives to support Russia’s domestic production capabilities through economic
espionage, as well as to retaliate against organisations and countries which
expressed solidarity with Ukraine.[^27]
In our Looking ahead section later in this report, we explore how these scenarios may materialise
and the implications for specific sectors and countries.
[^20]: ‘NCSC advises organisations to act following Russia’s attack on Ukraine’, NCSC, https://www.ncsc.gov.uk/news/organisations-urged-to-bolster-defences (18th March 2022)
[^21]: ‘Alert AA22-110A - Russian State-Sponsored and Criminal Cyber Threats to Critical Infrastructure’, CISA, https://www.cisa.gov/uscert/ncas/alerts/aa22-110a (20th April 2022)
[^22]: ‘INCONTROLLER: New State-Sponsored Cyber Attack Tools Target Multiple Industrial Control Systems’, Mandiant, https://www.mandiant.com/resources/blog/incontroller-state-sponsored-ics-tool (13th April 2022)
[^23]: ‘PIPEDREAM: CHERNOVITE’s Emerging Malware Targeting Industrial Control Systems’, Dragos, https://hub.dragos.com/whitepaper/chernovite-pipedream (13th April 2022)
[^24]: ‘Joint Statement on Further Restrictive Economic Measures’, The White House, https://www.whitehouse.gov/briefing-room/statements- releases/2022/02/26/joint-statement-on-further-restrictive-economic-measures/ (26th February 2022)
[^25]: CTO-SIB-20220228-01A - Implications of isolation
[^26]: CTO-SIB-20220825-01A - Sanctions and sectoral impact
[^27]: CTO-SIB-20220825-01A - Sanctions and sectoral impact

11 | Cyber Threats 2022: A Year in Retrospect
Sabotage operations and overlaps
Sabotage operations have been observed throughout the Russian war in Ukraine, ranging
from information operations to destructive operations intended to degrade Ukrainian
communications and systems. The attack on the Viasat satellite network in February 2022,
attributed to Russia-based activity and coinciding with the onset of the Russian offensive,
is a notable example of cyber threat actors tactically supporting kinetic operations with
longer term strategic implications.[^28], [^29], [^30], [^31]
Leading up to the invasion, in late January and February 2022, we analysed samples of
bomb threat emails to Ukraine’s security services, which we assess were likely from
Russia-based threat actors intending to disrupt everyday activities in Ukraine.[^32] Since late
February 2022, these information operations have extended more broadly to promote both
pro-Russia and pro-Ukraine narratives in a variety of channels, as seen prominently on
social media.[^33] Since the invasion, cyber-enabled information operations and other online
activities coincided with a resurgence in hacktivism.
Wipers
Numerous Russia-based threat actors deployed destructive malware against Ukraine-
based entities as the invasion persisted.[^34] Through our analysis of available samples and
research published by others in the security industry, we found examples of code overlaps
and potential indicators of sharing across multiple Russia-based threat actors. For
example, in April 2022, researchers identified activity attributed to the threat actor we track
as Blue Echidna, which showed an Industroyer variant being used alongside a CaddyWiper
sample to target a Ukrainian energy organisation,[^35], [^36] and Mandiant researchers indicated
the threat actor we track as Blue Athena had executed CaddyWiper variants against
Ukrainian organisations.[^37] Given that the Russian government’s strategic priorities have
centred on its offensive into Ukraine, the potential for Russia-based threat actors to share
or crosspollinate malware and capabilities with each other is unsurprising, despite
intergroup competition and historical conflicts among security and intelligence services.
[^28]: CTO-WTU-20220513-01A - Ukraine Weekly Report
[^29]: ‘Russian cyber operations against Ukraine: Declaration by the High Representative on behalf of the European Union’, European Council, https://www.consilium.europa.eu/en/press/press-releases/2022/05/10/russian-cyber-operations-against-ukraine-declaration-by-the-high- representative-on-behalf-of-the-european-union/ (10th May 2022)
[^30]: ‘Russia behind cyber-attack with Europe-wide impact an hour before Ukraine invasion’, UK Government, https://www.gov.uk/government/news/russia-behind-cyber-attack-with-europe-wide-impact-an-hour-before-ukraine-invasion (10th May 2022)
[^31]: ‘Attribution of Russia’s Malicious Cyber Activity Against Ukraine’, US Department of State, https://www.state.gov/attribution-of-russias- malicious-cyber-activity-against-ukraine/ (10th May 2022)
[^32]: CTO-QRT-20220224-01A - Wiping and disruption in Ukraine
[^33]: CTO-WTU-20220311-01A - Ukraine Weekly Report
[^34]: ‘Wipermania: An All You Can Wipe Buffet’, Trellix, https://www.trellix.com/en-us/about/newsroom/stories/research/wipermania-an-all-you-can-wipe-buffet.html (15th November 2022)
[^35]: ‘Industroyer2: Industroyer reloaded’, ESET, https://www.welivesecurity.com/2022/04/12/industroyer2-industroyer-reloaded/ (12th April 2022)
[^36]: CTO-WTU-20220414-01A - Ukraine Weekly Report
[^37]: ‘GRU: Rise of the (Telegram) Mini0ns’, Mandiant, https://www.mandiant.com/resources/blog/gru-rise-telegram-minions (23rd September 2022)

12 | Cyber Threats 2022: A Year in Retrospect
Based on our visibility and collection, we analysed the following wipers:
WhisperGate wiper
Prior to the invasion, Microsoft released a report on 15th January 2022 concerning a
destructive malware family it tracks as WhisperGate,[^38] which we associate with Blue
Dev 7. WhisperGate combines several attack stages consisting of a Master Boot
Record (MBR) overwrite and a file corruption stage.[^39] When WhisperGate was first
discovered, its behaviour and design initially suggested ransomware; however, unlike
conventional financially motivated ransomware, WhisperGate’s corruption process is
irreversible, indicating a sabotage intention rather than extortion. Further, the primary
targets of WhisperGate were Ukrainian government organisations, as well as at least
one technology firm known to provide services to the Ukrainian government.
Hermetic wiper
Coinciding with Russia’s invasion, we analysed Hermetic wiper following initial public
reporting, and this wiper attempted to execute on Ukrainian infrastructure and,
if successful, would wipe partitions of infected machines, rendering them inoperable.
The binary drops an EaseUS Partition file to conduct wiping activities but can also wipe
files using the Windows application programming interface (API).[^40]
CaddyWiper
In mid-March 2022, security researchers discovered CaddyWiper executing on
environments in Ukraine.[^41] The wiper contained functionality to wipe files and eventually
the physical drive of all the drives mapped on the victim system if it was not the primary
domain controller. We assess the threat actor behind CaddyWiper likely manipulated
the rich header to cover up its original development fingerprint.[^42] Other security
researchers linked CaddyWiper to the threat actor we track as Blue Echidna, known for
manipulating rich Portable Executable (PE) headers, for example in Olympic Destroyer.[^43]
[^38]: ‘Destructive malware targeting Ukrainian organizations’, Microsoft, https://www.microsoft.com/security/blog/2022/01/15/destructive-malware-targeting-ukrainian-organizations/ (15th January 2022)
[^39]: CTO-TIB-20220121-01A - The WhisperGate Wiper
[^40]: CTO-QRT-20220224-01A - Wiping and disruption in Ukraine
[^41]: @ESETResearch, Twitter, https://twitter.com/esetresearch/status/1503436420886712321 (14th March 2022)
[^42]: CTO-QRT-20220315-03A - CaddyWiper hits Ukraine
[^43]: ‘The devil’s in the rich header’, Kaspersky, https://securelist.com/the-devils-in-the-rich-header/84348/ (8th March 2018)

13 | Cyber Threats 2022: A Year in Retrospect
ControlZero wiper
In mid-March 2022, we named a fourth wiper ControlZero (a.k.a. DoubleZero)[^44] for its
use of the API call NtFsControlFile to wipe files, and assessed the wiper was likely used
for disruption events on Ukrainian networks. In our analysis, we observed ControlZero
removing registry keys from the affected system, and the system eventually prompted a
restart due to important system resources being modified.[^45] From our observations,
ControlZero was the first wiper in 2022 to remove registry keys to cause further
disruption.
StarWiper
In April 2022, we analysed another wiper we refer to as StarWiper (a.k.a. ACIDRAIN),[^46]
which appeared to target embedded devices