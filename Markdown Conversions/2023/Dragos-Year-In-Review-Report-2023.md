# OT CYBERSECURITY
# THE 2023 YEAR IN REVIEW

FEBRUARY 2024

## Table of Contents
- [INTRODUCTION](#introduction)
- [THE RISING TIDE OF INDUSTRIAL CYBER THREAT ACTIVITY](#the-rising-tide-of-industrial-cyber-threat-activity)
- [KEY HIGHLIGHTS: INSPIRING ACTION](#key-highlights-inspiring-action)
- [LEARNING FROM ROCKWELL AUTOMATION VULNERABILITIES](#learning-from-rockwell-automation-vulnerabilities)
- [KEY HIGHLIGHTS: BY THE NUMBERS](#key-highlights-by-the-numbers)
- [OT CYBER THREAT LANDSCAPE](#ot-cyber-threat-landscape)
- [NEW THREAT GROUP ACTIVITY](#new-threat-group-activity)
- [VOLTZITE](#voltzite)
- [GANANITE](#gananite)
- [LAURIONITE](#laurionite)
- [UPDATES ON SOME OF THE MOST ACTIVE THREAT GROUPS](#updates-on-some-of-the-most-active-threat-groups)
- [2023 INDUSTRIAL RANSOMWARE ANALYSIS](#2023-industrial-ransomware-analysis)
- [INDUSTRIAL RANSOMWARE TRENDS](#industrial-ransomware-trends)
- [LEVERAGING LIVING OFF THE LAND TECHNIQUES TO FURTHER ACCESS](#leveraging-living-off-the-land-techniques-to-further-access)
- [OT VULNERABILITIES](#ot-vulnerabilities)
- [VULNERABILITY ASSESSMENT OVERVIEW](#vulnerability-assessment-overview)
- [VULNERABILITY ACCURACY](#vulnerability-accuracy)
- [VULNERABILITY RISK MITIGATION](#vulnerability-risk-mitigation)
- [NOW, NEXT, NEVER PRIORITIZATION](#now-next-never-prioritization)
- [VULNERABILITY SEVERITY](#vulnerability-severity)
- [VULNERABILITY EXPLOITABILITY](#vulnerability-exploitability)
- [VULNERABILITY TRENDS](#vulnerability-trends)
- [TREND ANALYSIS BY VULNERABILITY TYPE](#trend-analysis-by-vulnerability-type)
- [USE OF HARD-CODED CREDENTIALS – CWE-798](#use-of-hard-coded-credentials--cwe-798)
- [PATH TRAVERSAL – CWE-22](#path-traversal--cwe-22)
- [NEIGHBORHOOD KEEPER VULNERABILITY DATA](#neighborhood-keeper-vulnerability-data)
- [ASSESSING CYBER READINESS](#assessing-cyber-readiness)

# INTRODUCTION

In 2023, a surge in global tension resulted in an increase in cyber threat activity and disruptions in critical infrastructure worldwide. Escalating conflicts, including those between Ukraine and Russia, Israel and Hamas, and countries in the South China Sea, emboldened adversaries and hacktivists to develop new capabilities and reuse old techniques. Simultaneously, ransomware attacks affected more industrial organizations, with a nearly 50 percent increase in reported incidents. Asset owners must take necessary precautions to address these threats or fall victim to them.

Among the threats that organizations must consider are the capabilities developed in conflict areas. A year after Russia’s invasion of Ukraine, cyber threat activity in the region continues to escalate. Dragos and the community became aware of new destructive malware capabilities as ELECTRUM conducted targeted cyber operations against Ukrainian critical infrastructure. The mixture of traditional kinetic warfare with cyber-focused capabilities has created a new testbed for increased threat capabilities worldwide.

Similarly, the conflict that erupted in the Middle East included cyber attacks on critical infrastructure. Pro-Israeli hacktivists claimed responsibility for the attacks that claimed to disrupt over 70 percent of the gas stations in Iran, while pro-Hamas hacktivists targeted Israeli-manufactured operational technology (OT) hardware and software. The impact of these attacks on industrial equipment spread beyond the conflict zone and affected various sectors, such as water and manufacturing, around the globe.

Throughout the year, Dragos continued to track threat groups as they developed capabilities and gained access. Mounting tensions between China and Taiwan contributed to the environment where Dragos observed VOLTZITE target several industrial organizations in the Asia-Pacific region, Africa, and North America — including entities in electric, satellite communications, telecommunications, emergency management, and defense industrial base sectors — with cyber attack campaigns assessed to be aimed at long-term espionage objectives. VOLTZITE’s actions towards U.S. electric entities, telecommunications, and GIS systems signify clear objectives to identify vulnerabilities within the country’s critical infrastructure that can be exploited in the future with destructive or disruptive cyber attacks. Dragos tracked 21 threat groups targeting industrial organizations including three new threat groups.

Although threat groups and hacktivists posed significant risks in 2023, ransomware was the primary concern for many organizations globally. This concern is well founded, considering the rise in ransomware attacks and the industrial impact observed by Dragos during incidents this year. These trends, along with new reporting requirements, saw an increased focus on response from many organizations. Regulatory changes in the United States, Europe, Australia, Asia, and the Middle East required organizations to develop capabilities to meet reporting obligations. To this end, Dragos conducted more exercises with a wider range of participants and industries in 2023.

Another major focus area for organizations this year was understanding what risks vulnerabilities posed and how best to respond to them. 2023 saw a 14 percent increase in vulnerabilities advisories, with 31 percent of advisories that Dragos analyzed having incorrect data. The year also saw the discovery of a major vulnerability impacting Rockwell Automation’s ControlLogix communication modules, reminiscent of the zero-day that XENOTIME exploited in the TRISIS attack. However, this event exemplified how vendors, governments, and our community leverage communication and visibility to enable a unified, risk-based response.

Dragos started the Year in Review to highlight significant trends in the OT cybersecurity community. This year’s report aims to go further by offering practitioners and leaders the most up-to-date data, along with perspectives from the field, to help them better defend critical infrastructure around the world. These perspectives are focused on providing actionable insights that have been tried and tested to help organizations effectively defend against and respond to industrial cyber threats.

# THE RISING TIDE OF INDUSTRIAL CYBER THREAT ACTIVITY

The Dragos Platform provides visibility and insight through OT Watch and Neighborhood Keeper data. The Dragos threat intelligence teams assess and research vulnerabilities and actively track adversaries impacting operational technology. Dragos consultants and responders provide frontline perspectives from various engagements, including assessments, exercises, and incident response. Since Dragos first started gathering data for Year in Review in 2017, many trends have remained consistent with notable milestones along the way. The data and perspectives presented in this report are focused on the global industries that Dragos serves.

## 2016 – CRASHOVERRIDE
Not identified until months later, CRASHOVERRIDE malware was used in 2016 as the first malicious code to attack electric substations – the facilities and equipment that are designed to protect bulk electric systems were manipulated to have the opposite effect. The CRASHOVERRIDE legacy lives on with a series of attacks utilizing INDUSTROYER2 malware observed as recently as October 2022.

## 2017 – TRISIS
The threat group XENOTIME deployed the TRISIS malware against a Safety Instrumentation System (SIS) at a petrochemical plant in Saudi Arabia. TRISIS represents the expansion of malware targets and methods of execution, and the first time system safety features have been targeted and compromised directly.

## 2018 – EXPANDED THREAT GROUPS
In 2018, Dragos expanded the number of Threat Groups tracked from 3 to 8. This trend continued over time — to date there are 21 Dragos-designated Threat Groups with the intent to gain access to OT environments and potentially disrupt them.

## 2019 – INCREASED RANSOMWARE IN OT
In 2019, Dragos tracked a 50 percent uptick in ransomware within OT. The first ransomware case Dragos responded to occurred within the electric sector also in 2019.

## 2020 – EKANS RANSOMWARE
Dragos analyzed EKANS malware variants with capabilities to stop ICS-related Windows processes before initiating encryption. This functionality represents a natural but troubling consequence of target expansion. Ransomware groups increase the odds of victims paying a ransom when business is disrupted.

## 2021 - RANSOMWARE ATTACK IMPACTS OT
In 2021, Colonial Pipeline was impacted by ransomware, causing a precautionary shutdown of OT operations. Again, ransomware instances continued to balloon in 2023 with 905 instances, an increase of nearly 50 percent over the last year.

## 2022 – ENTER CHERNOVITE
In 2022 Dragos discovered the CHERNOVITE Threat Group, developer of the PIPEDREAM malware, a highly motivated and well-funded entity, that is skilled in software development methods and well versed in industrial control systems (ICS) intrusion techniques.

## 2023 – EVOLVING THREAT LANDSCAPE
Rising tensions and financial opportunity continued to spur a wide variety of actors to target industrial environments - including hactivists, criminal gangs, and three new Dragos-designated Threat Groups.

# KEY HIGHLIGHTS: INSPIRING ACTION

*   If you haven’t assessed your external infrastructure for critical systems yet, 2024 is the time. This includes identifying your organization’s internet routable netblocks and IP space, including what contractors or vendors may have set up for you. Network scan your public spaces and compare it against Shodan, Whois, and your documentation. Ensure critical assets or assets connected to your process environment are not discoverable from the internet. Learn more about why this guidance is important from the 2023 attack on Unitronics PLC devices by the CyberAv3ngers on page 11.

*   If you haven’t segmented your network yet, the best time for that was in the 2000s; the second best time is now. This network segmentation includes separating devices with network and host-based firewalls by function, not just systems from the internet, but systems from each other and critical processes. Do not merely focus on IPv4 when your systems also use IPv6. When operators traverse network zones to log in using a virtual private network (VPN), remote desktop protocol (RDP), or other remote access tools, they should leverage separate authentication. In 2023, increased ransomware impacts on OT environments highlight the necessity of this old but still useful guidance. Read more on Ransomware on page 21.

*   Restricting and monitoring outbound communication is also important in addition to segmentation. This includes evaluating default routes, gateways, and firewall rules to external networks and proxy configurations. In 2023, several adversaries, such as VOLTZITE, GANANITE, and ransomware groups, leveraged communication to external networks for command and control (C2) communication, allowing exfiltration of data and remote control of network assets. For more on this see the OT Cyber Threat Landscape section of this report on page 9.

*   If your organization already regularly assesses standard guidance, such as auditing segmentation rules and configuration, you still have work to do. As defensible architecture continues to mature, adversary techniques shift with it. Learn which techniques our penetration testers leverage in OT assessments in the Frontline Perspective section on page 20, as well as which techniques still work for ransomware groups on page 21 and threat groups on page 9. Understanding the attack surface is vital for prioritizing a response or identifying adversaries within your network. Hunting for evidence of these techniques in use within your monitoring system is the best way to identify unwanted operators hiding in your OT environment.

*   Lastly, reduce the risk of vulnerable equipment used in OT processes, but do it in a systematic way. In 2023, Dragos prioritized and wrote mitigation guidance for 531 OT-related advisories, 2010 vulnerabilities. Read more on key insights, trends, and mitigations from vulnerabilities on page 27.

# LEARNING FROM ROCKWELL AUTOMATION VULNERABILITIES

In 2023, the U.S. Government informed Rockwell Automation of two vulnerabilities impacting a subset of ControlLogix communication modules. These communication modules are part of a significant Rockwell Automation product line and assist in controlling processes in many industrial verticals. In coordination with their government partners, Rockwell Automation organized a defensive working group comprised of various vendors, including Dragos. The working group’s goal: develop detections for these vulnerabilities and search for evidence of exploitation.

As part of the working group, Dragos analysts studied the vulnerabilities and the impacted communications modules. With Rockwell Automation and other community members, they developed detection signatures that would alert on artifacts specific to varying methods of potential exploitation. Dragos vulnerability analysts deployed these signatures to Neighborhood Keeper and OT Watch to find signs of malicious activity. They triaged any alerts, paying attention to false positives and tuning signatures accordingly.

Dragos analysts passed the detection results back to the working group so that the rest of the community could tune their signatures for their respective platforms. In this way, Neighborhood Keeper helped the community to avoid unnecessary alerting once the detections and vulnerabilities were made public. Aside from signature tuning, Neighborhood Keeper provided visibility into the number of vulnerable devices and how widespread their use is in different industries and regions. Dragos passed this information back to the working group so that they could assess the vulnerabilities’ risk and potential impact.

The collaboration between the U.S. Government and Rockwell Automation, along with the formation of a working group of security vendors to ensure a defensive front before public release, and the coordinated publishing of vulnerability information, represents a significant accomplishment for the industrial control systems (ICS) community. Product owners and OEMs can look to Rockwell Automation as an excellent example of community and defense-forward practice and consider following this path for vulnerability disclosure. This new approach of blending U.S. Government intelligence with security industry expertise and OEM knowledge is undoubtedly the way forward in combating future cyber adversary threats to critical infrastructure.

### THE VULNERABILITIES
Rockwell Automation and the U.S. Government disclosed two vulnerabilities:

*   **CVE-2023-3595**: This vulnerability in 1756 EN2* and 1756 EN3* products allows a malicious user to perform remote code execution with persistence on the target system through maliciously crafted CIP messages.
*   **CVE-2023-3596**: In the 1756-EN4* products, this vulnerability allows a malicious user to cause a denial of service through maliciously crafted CIP messages.

### Dragos Frontline Perspective
Dragos OT Watch customers and Neighborhood Keeper participants were protected by monitoring for this threat before it was publicly announced. If a situation like this were to happen again, Dragos Community Defense Program members would benefit via the program’s emerging threat monitoring.

13% of Rockwell Automation assets were ControlLogix communication modules, across manufacturing, paper and pulp, automotive, mining, chemical, food and beverage, electric, oil and gas, etc.

# KEY HIGHLIGHTS: BY THE NUMBERS

## Threat Group Highlights – 2023
*   21 Total Threat Groups
*   10 Active Threat Groups
*   3 New Threat Groups

## Key Vulnerabilities Findings
*   80% of vulnerabilities reside deep within the ICS network.
*   16% of advisories were network exploitable and perimeter facing in 2023.
*   53% of the advisories that Dragos analyzed could cause both a loss of view and loss of control, up from 51% last year.
*   31% of advisories contained errors in 2023.
*   49% of advisories had none. Dragos provided mitigations for 49% of the advisories that had none.

## Key Ransomware Findings
*   Ransomware attacks against industrial organizations increased 50 percent over last year.
*   Dragos tracked 28% more ransomware groups impacting ICS/OT in 2023.
*   70% of all ransomware attacks targeted 638 manufacturing entities in 33 unique manufacturing subsectors.

## 2023 Dragos Threat Groups Summary
*   Three new threat groups: GANANITE, LAURIONITE and VOLTZITE
*   10 active threat groups: BENTONITE, ELECTRUM, GANANITE, KAMACITE, LAURIONITE, MAGNALLIUM, PETROVITE, RASPITE, TALONITE and VOLTZITE
*   ELECTRUM demonstrates Stage 1 & 2 aspects of the ICS Cyber Kill Chain
*   Threat Group Statistics from 2022 Year in Review:
    *   9 threat groups demonstrate at least Stage 1 of the ICS Cyber Kill Chain: BENTONITE, ELECTRUM, GANANITE, KAMACITE, LAURIONITE, MAGNALLIUM, PETROVITE, RASPITE, and VOLTZITE
    *   2 new threat groups: BENTONITE and CHERNOVITE
    *   2 threat groups, ERYTHRITE and COVELLITE, were retired in 2023. 11 threat groups were dormant
    *   8 active threat groups: BENTONITE, CHERNOVITE, ELECTRUM, ERYTHRITE, KAMACITE, KOSTOVITE, WASSONITE and XENOTIME

# OT CYBER THREAT LANDSCAPE

The OT cyber threat landscape continued to evolve in 2023, with an increase in tracked threat groups, ransomware events, and other threat activities driven by global conflict. The adversaries involved in these activities varied widely in terms of their level of sophistication, deployed capabilities, and intended targets.

On one end of the spectrum, some threat groups used advanced techniques, such as leveraging native functionality, including living off the land (LOTL) techniques, to conduct reconnaissance and intelligence operations. Conversely, some adversaries targeted low-hanging fruit such as internet-accessible devices that lacked proper hardening, thus making them easy to damage and cause operational disruptions.

Threat groups continued to use publicly disclosed vulnerabilities and discover and develop their own capabilities. Most of the observed threat activity targeted IT-centric devices that are commonly used in OT, such as Sierra Wireless modems or Citrix. In 2023, Dragos worked with one of our strategic partners, Rockwell Automation, on a community response to a set of adversary-developed vulnerabilities targeting OT devices. The identified vulnerabilities have the potential to result in loss/denial of view (T0829, T0815), denial/manipulation of control (T0813, T0831), theft of operational information (T0882), and loss of productivity and revenue (T0828).

## CONFLICT-DRIVEN THREAT ACTIVITY
The overlaps of OT cybersecurity threats with regional and global kinetic events have never been more evident than in 2023. Cyber adversaries with a range of capabilities have used the Ukraine-Russia and Israel-Hamas wars to conduct targeted operations against critical infrastructure, and less sophisticated hacktivists have used the same conflicts to cause panic and negatively impact public perception of the resilience of critical services. Geopolitical tensions worldwide, including in Asia and Africa, have also driven intelligence gathering and capability staging activity.

The Ukraine-Russia conflict drove the activity of more mature threat groups, such as ELECTRUM, which conducted targeted cyber operations against Ukrainian critical infrastructure entities. A new destructive wiper malware attributed to ELECTRUM was observed in the wild in June 2023. Later, in September 2023, Dragos reported on a spear-phishing campaign that targeted Ukrainian critical infrastructure organizations linked with ELECTRUM and KAMACITE. Lastly, in November 2023, a cybersecurity vendor published a report providing evidence of destructive malware activity targeting Ukrainian electric substations in October 2022. Dragos assessed with moderate confidence that ELECTRUM conducted the October 2022 destructive malware activity.

According to multiple sources, the mounting tension between China and Taiwan also contributed to increased targeted cyber espionage attacks against multiple industrial organizations in the Asia-Pacific region and the United States.¹ One threat group in particular, VOLTZITE, has targeted numerous critical infrastructure entities in Guam, the United States, and other countries since at least 2021. VOLTZITE overlaps with Volt Typhoon, a group that the U.S. Government has publicly linked to the People’s Republic of China. VOLTZITE heavily uses living off the land (LOTL) techniques and, in some cases, has been observed conducting “hands-on keyboard” post-compromise actions within a victim’s networks.

VOLTZITE has shown continued interest in the electric and telecommunications sectors in the United States, evidenced by the long-term reconnaissance of multiple electric entities. If VOLTZITE establishes an initial foothold on the network perimeter of a target, it may then be able to pivot further into a victim’s information technology (IT) network and then move laterally onto the victim’s OT network. Dragos has only observed VOLTZITE operations achieving Stage 1 of the ICS Cyber Kill Chain. They have not displayed actions or capabilities designed to disrupt, degrade, or destroy ICS/OT assets or operations.

Dragos leverages its intelligence to drive hunting with our customer environment and the community. This was used to track and analyze indicators of compromise and behavioral tactics, techniques, and procedures relevant to the VOLTZITE threat group. A significant outcome of this is finding a high confidence indicator within a Dragos Platform customer’s environment, allowing OT Watch to better assist the client during their incident response efforts and providing Dragos Intelligence with real-world behavioral elements surrounding the VOLTZITE indicator, including activity suggesting remote desktop protocol (RDP) usage and server message block (SMB) directory traversal. Another interesting finding was VOLTZITE overlaps with infrastructure associated with the Mirai Botnet and another activity cluster that differs from VOLTZITE but may be operationally connected.

Dragos’s analysis of VOLTZITE operations underscores the need for ongoing vigilance among organizations operating in the global electric sector, as the observed activity suggests continued and specific interest in these networks. Further, VOLTZITE’s actions involving prolonged surveillance and data gathering align with Volt Typhoon’s assessed objectives of reconnaissance and gaining geopolitical advantage in the Asia-Pacific region.

¹ https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-144a; https://www.microsoft.com/en-us/security/blog/2023/05/24/volt-typhoon-targets-us-critical-infrastructure-with-living-off-the-land-techniques/

Throughout 2023, hacktivists and other unsophisticated, opportunistic threat groups have conducted widespread distributed denial of service (DDoS) attacks against various industrial organizations and critical infrastructure. Pro-Russia groups like CyberArmyofRussia_Reborn attacked industrial organizations in Europe in May 2023. NoName057(16) attacked European and North Atlantic Treaty Organization (NATO) aligned countries and their manufacturing and transportation organizations. Additionally, Anonymous Sudan was also observed attacking the United States and other NATO-aligned entities. Similar activity has been observed with pro-Hamas hacktivist groups such as the CyberAv3ngers and Team Insane Pakistan claiming disruptive attacks against Israeli Railways, an Israeli town’s power grid system, and an Israeli hydroelectric plant. In late December 2023, the hacktivist group Predatory Sparrow allegedly disrupted Iranian gas stations with an unspecified cyber attack.

These operations also included the successful compromise of public-facing OT devices, as was observed in late November with the attack on Unitronics devices. The CyberAv3ngers successfully compromised numerous U.S., European, and Australian industrial companies using internet-accessible Unitronics PLC devices. Dragos assesses with moderate confidence that the adversaries scanned the open internet to identify publicly accessible Unitronics devices and then attempted to log into the devices using the Unitronics default password. This adversary appears not to possess OT capabilities; however, this attack still led to a Loss of View and Control (T0829, T0827) for some of those impacted.

### Dragos Frontline Perspective
The hacktivists’ DDoS attacks had minimal impacts and primarily disrupted the organization’s websites. In many cases, Dragos found that claims of disruptive attacks against critical infrastructure were wildly exaggerated or completely fabricated. However, most hacktivist groups aim to gain notoriety, spread misinformation, cause fear, uncertainty, and doubt (FUD), and draw international media attention to geopolitical and social causes.

### Dragos Frontline Perspective
Dragos identified over 1800 internet-exposed Unitronics devices, but only 0.0001 percent of Neighborhood Keeper monitored assets are Unitronics. Dragos assesses with moderate confidence that Unitronics devices are more common in environments with limited visibility, such as remote locations or smaller organizations. This type of device is often deployed without proper visibility or hardening. Basic hygiene and device management are critical to stopping this activity, including understanding what is publicly accessible.

![Figure 1: Findings Severity per Vertical](https://i.imgur.com/example1.png)

# NEW THREAT GROUP ACTIVITY

Dragos observed 10 active Threat Groups during 2023, including three new Dragos-identified Threat Groups: GANANITE, VOLTZITE, and LAURIONITE. These new threat groups conduct primarily long-term reconnaissance and intellectual property theft operations. Of the three, VOLTZITE has been most active in targeting critical infrastructure organizations. Dragos has not identified VOLTZITE, GANANITE, or LAURIONITE utilizing any ICS-specific capabilities; however, their persistent interest and activities within critical infrastructure sectors warrant monitoring and preparedness by ICS/OT organizations.

Dragos observed all three threat groups conducting diverse operations against various organizations, including cybersecurity research firms, government and military defense entities, rail, manufacturing, automotive, and utilities. GANANITE and LAURIONITE have exhibited an opportunistic approach to their initial access operations; however, VOLTZITE’s operations strongly indicate espionage and reconnaissance objectives in the Asia-Pacific region and the United States – particularly the electric sector.

All three newly identified threat groups possess capabilities that target and exploit public-facing infrastructure used or owned by victim organizations. More Severe Types of infrastructure included but were not limited to targeting public internet-facing Sierra Wireless Airlink devices, Fortinet FortiGate, VPN infrastructure, and Oracle eBusiness Suite iSupplier Web Services.

### Dragos Frontline Perspective
Dragos observed threat groups, including GANANITE and LAURIONITE, targeting some of these sectors with the least mature environments (transport, manufacturing, water utilities). Dragos assesses a sector’s level of maturity based on the number and severity of findings observed by Dragos during its assessment in those respective environments. Organizations in these sectors should understand the elevated risk this presents. Threat groups have been observed using certain MITRE ATT&CK techniques. Dragos uses these TTPs to correlate threat actor behavior with field observations.

![Figure 2: Findings and MITRE TTPs by Threat Groups Using Public Exploits](https://i.imgur.com/example2.png)

### Dragos Frontline Perspective
Exploiting public-facing devices and external services is a common technique that Dragos observed four Threat Groups utilizing in 2023. A defensible architecture to protect against this technique includes multiple layers of defense, secure remote access setup with MFA, and monitoring.

*   Dragos issued findings related to externally facing networks such as the internet in 20 percent of engagement reports.
*   Dragos found inadequately configured firewalls protecting OT environments in 28 percent of engagements in 2023.

# VOLTZITE

TARGETS: UNITED STATES, ASIA, AFRICA

VOLTZITE, a Dragos-tracked threat group that has operational overlaps with Volt Typhoon (first reported on by the U.S. Cybersecurity and Infrastructure Security Agency and Microsoft in May 2023), was performing reconnaissance and enumeration of multiple US-based electric companies, and since then has been observed targeting electric power transmission and distribution, emergency services, telecommunications, defense industrial bases, and satellite services. VOLTZITE’s actions towards US electric entities, telecommunications, and GIS systems signify clear objectives to identify vulnerability within the country’s critical infrastructure that can be exploited in the future with destructive or disruptive cyber attacks.

While VOLTZITE has traditionally targeted US facilities, we also are aware of the group targeting organizations in Africa and Southeast Asia. This group heavily uses living off the land (LOTL) techniques, which can make detection and response efforts more difficult. This strategy, paired with slow and steady reconnaissance, enables VOLTZITE to avoid detection from security teams.

## Impact and Implications
VOLTZITE conducts enumeration against victims’ internet-facing assets in a slow and sustained fashion, likely to lessen the chance of being detected. Once they have exploited a victim’s internet-facing asset, they exhibit consistent use of living off the land techniques, making detection more difficult for defenders. VOLTZITE’s 2023 behavior suggested operational objectives of espionage and information gathering. Data stolen from operational technology (OT) networks may result in unintended disruption to critical industrial processes or provide the adversary with crucial intelligence to aid in follow-up offensive tool development or attacks against ICS networks.

### KEY HIGHLIGHTS
*   Heavily utilized living off the land techniques to inhibit the potential identification of malicious activity.
*   Conducts offensive operations with a significant focus on detection evasion and sophisticated operational security tradecraft.
*   Conducts slow and steady reconnaissance against a target focusing on credential theft, lateral movement, and long-term espionage.
*   Exploits internet accessible SOHO routers, using them as intermediary hops back to adversary controlled infrastructure.

## NOTABLE ACTIVITY
*   **June 2023**: Compromise of network and video surveillance through Sierra Wireless Airlink
*   **July 2023**: Exploitation attempts against African electric entity
*   **November 2023**: Enumeration of U.S. Energy Organizations
*   VOLTZITE exploited public internet-facing Sierra Wireless Airlink devices of a U.S. emergency management and traffic monitoring entity in a June 2023 campaign.
*   Possible exploitation attempts in July 2023 against an African electric transmission, distribution, and retailer entity.
*   VOLTZITE conducted extensive reconnaissance of U.S. energy organizations in November 2023.

# OT Watch Threat Hunting Uncovers VOLTZITE

*   The Dragos Intelligence team started tracking VOLTZITE’s activities at the beginning of 2023.
*   A new utility customer deployed the Dragos Platform in response to a pre-existing network compromise with a potential ICS/OT impact. The platform was positioned to monitor the IT-OT interface (Level 3-4) and OT-OT communications (Level 2).
*   Following deployment, Dragos OT Watch utilized the Dragos Platform to identify malicious activity within the environment working with Dragos Intelligence using tactics, techniques, and procedures (TTPs) and threat hunt analytics.
*   The threat hunt confirmed adversary evidence adjacent to the OT network; and incident response analysis found evidence of adversary discovery actions with a focus on SCADA related information. This was seen in the Dragos Platform as server message block (SMB) traversal with the group pivoting within the environment, and likely, looking for information about the environment as a further means of persistence.
*   Consistent with OT Watch operations, findings were promptly escalated to the customer with a full summary of all threat hunt findings after the full investigation. The recommendations further empowered the customer’s incident response efforts in cleaning up the incident to eliminate the adversary from the environment. The environment continues to be monitored via the Dragos Platform and OT Watch.
*   Taking the success of the threat hunt and the detailed understanding on the tactics of this threat group provided by the Dragos Intelligence team, OT Watch extended the hunt across all relevant OT Watch customers.
*   The Dragos Intelligence team enhanced the effort by analyzing Neighborhood Keeper data for indications of VOLTZITE behaviors and then notifying impacted parties anonymously. With these findings, Dragos threat detections engineers developed high-fidelity detections back into the Platform deployed via Dragos Knowledge Packs for continuous monitoring.

The overall response to the VOLTZITE threat highlights the importance of coordinated efforts and the advantage of ICS/OT capabilities unique to Dragos. This engagement not only addressed a complex threat but also strengthened the protective measures across critical infrastructure customers.

### Dragos Frontline Perspective
Asset owners often deploy cellular gateways such as the Sierra Wireless devices in remote locations where wired connections are not practical or economical. These gateways are usually connected directly to OT devices, exposing those devices to misconfiguration or vulnerabilities of the gateway. Given the limited visibility and reliance on a single layer of protection when a gateway and connected device are compromised, long adversary dwell times are possible.

![Diagram of a Cellular Gateway connected to OT devices](https://i.imgur.com/example3.png)

Dragos has seen these devices used by utilities for pole-top deployments connected to CAP banks and reclosers and at remote pump stations, storage tanks, and lift stations. Further, Dragos has seen their use in MET towers, small hydro, distributed solar, and storage in generation environments. The most concerning instances are when Dragos has found cellular gateways connected to larger control systems such as a DCS or PLC Process Control Network (PCN) as a remote access mechanism that bypasses standard security controls. Organizations must have an accurate asset inventory and visibility to protect against the risk that these types of devices introduce to an industrial environment.

# GANANITE

TARGETS: ASIA

GANANITE is a Dragos-designated Threat Group that targets critical infrastructure and government entities in the Commonwealth of Independent States and Central Asian nations. GANANITE focuses on espionage and data theft, with the possibility of handing off initial access to other threat groups. GANANITE focuses persistently on its target sets by employing many known tools to infiltrate its victims.

Building on the use of StinkRAT and publicly available proof of concept exploits for internet-exposed endpoints, GANANITE also exhibits use of tooling such as TELEMIRIS and JLORAT, which has been attributed by Kasperky as being exclusively used by a threat group under the direction of or working with TURLA.

## Impact and Implications
GANANITE has been observed conducting multiple attacks against key personnel related to ICS operations management in a prominent European oil and gas company, rail organizations in Turkey and Azerbaijan, multiple transportation and logistics companies, an automotive machinery company, and at least one European government entity overseeing public water utilities. Although GANANITE has not yet shown evidence of moving into OT networks or an elevated capability resembling Stage 2 actions, their assessed capabilities show efficient use of multiple phases across Stage 1 of the ICS Cyber Kill Chain.

### KEY HIGHLIGHTS
*   Leveraged publicly available proof of concept (POC) exploits for internet-exposed endpoints, along with many remote access trojans (RAT), such as Stink Rat, LodaRAT, WarzoneRAT, and JLORAT.
*   Use of energy -focused phishing lures.
*   Exfiltrated web browser information from victim machines using Telegram in addition to traditional C2 methods over HTTP and HTTPS.
*   Conducted in-depth reconnaissance of target organizations through Shodan and FOFA to build a profile of the target and potential vulnerabilities of the exposed asset.

## NOTABLE ACTIVITY
*   **January 2023**: Recon and infiltration of EU critical infrastructure orgs
*   **May 2023**: CIS Targeting with espionage and data theft
*   On January 13, 2023, TR-2023-01 documented reconnaissance against and infiltrated various European critical infrastructure organizations. Along with credential capture via masqueraded domain phishing pages, the adversary utilizes an open-source Python RAT named Stink.
*   In May of 2023, GANANITE continued targeting government and industrial organizations in the Commonwealth of Independent States with a focus on espionage and data theft, with the potential to hand off initial access to other threat groups.

### Dragos Frontline Perspective
ICS attacks comprise of two parts: a penetration of the enterprise IT environment (Stage 1) which allows for a crossing into the ICS network, culminating in final reconnaissance and penetration of control system resources (Stage 2). It’s worth noting that Stage 1 does not always take place in a victim’s IT environment, but the compromise may be in a vendor’s environment that has access to the enterprise’s OT environment.

Further, GANANITE’s operations have displayed extensive research and use of known exploits against the external perimeter of its targets. GANANITE uses tools such as Shodan and FOFA search engines that contain data about internet-facing assets to build a profile of its target. After identifying the IP netblocks of its target, they then utilize data from Shodan and FOFA to identify any presence of devices exhibiting known exploitable vulnerabilities. GANANITE then moves on to exploit those vulnerabilities with publicly available exploits. For those reasons, industrial organizations in Europe and Central Asia face a significant risk from GANANITE due to their initial intrusion capabilities, post-compromise espionage TTPs, and intellectual property theft, all of which can be used in follow-on attacks against the victim organizations.

### Dragos Frontline Perspective
Adversaries use command and control (C2) to communicate with and control compromised systems by leveraging standard protocols like HTTP, HTTPS, or DNS for communication channels. C2 capabilities have progressed to the point where some frameworks can integrate third-party applications or non-traditional network protocols to facilitate or hide C2 traffic. Dragos researches how threat groups use common OT protocols for C2 operations and develop capabilities as part of a proof of concept.

Dragos focused on open platform communication unified architecture (OPC UA) and DNP3, given its widespread utilization across a range of critical industrial environments and the availability of robust open-source libraries for each protocol. These OT C2 capabilities enabled the Dragos penetration testing team to operate covertly in industrial environments by blending in with normal OT network traffic.

#