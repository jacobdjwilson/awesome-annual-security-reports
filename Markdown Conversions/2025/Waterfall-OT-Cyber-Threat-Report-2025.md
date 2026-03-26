# 2025 OT Cyber Threat Report
Navigating the Future of OT Security

## Table of Contents
- [Key Takeaways](#key-takeaways)
- [Introduction & Methodology](#introduction--methodology)
- [OT Incident Macro Trends](#ot-incident-macro-trends)
- [SEC Filings](#sec-filings)
- [Nation States & Hacktivists](#nation-states--hacktivists)
- [Number Of Sites Impacted](#number-of-sites-impacted)
- [Impacted Industries](#impacted-industries)
- [Impacted Regions](#impacted-regions)
- [How was OT Impacted?](#how-was-ot-impacted)
- [Implications For Cybersecurity Programs](#implications-for-cybersecurity-programs)
- [Incident Costs](#incident-costs)
- [Supply Chain – CrowdStrike Incident](#supply-chain--crowdstrike-incident)
- [Global Navigation & IRS Jamming and Spoofing](#global-navigation--irs-jamming-and-spoofing)
- [Near Misses](#near-misses)
- [Volt Typhoon and Salt Typhoon](#volt-typhoon-and-salt-typhoon)
- [New ICS-Capable Malware](#new-ics-capable-malware)
- [Defensive Developments in 2024](#defensive-developments-in-2024)
  - [Hardware-Enforced Remote Access](#hardware-enforced-remote-access)
  - [OT Security Principles](#ot-security-principles)
  - [Credibility, not Likelihood](#credibility-not-likelihood)
- [Conclusion](#conclusion)
- [APPENDIX A – The Complete Data Set](#appendix-a--the-complete-data-set)
  - [Field Descriptions](#field-descriptions)
  - [Incidents 2010-2024](#incidents-2010-2024)
- [APPENDIX B – Sources and Acknowledgements](#appendix-b--sources-and-acknowledgements)

Authors:
Rees Machtemes, Director Industrial Security, Waterfall Security Solutions
Gregory Hale, Editor & Founder, Industrial Safety and Security Source, ICS STRIVE
Monique Walhof, Consultant, Industrial Safety and Security Source, ICS STRIVE
Andrew Ginter, VP Industrial Security, Waterfall Security Solutions

---

## Key Takeaways
Compared to 2023, 2024 saw a smaller increase in cyber attacks that caused physical consequences on OT organizations. Nevertheless, there were sharp jumps in the number of sites affected by the hacks, as well as in the number of attacks by nation states. attributed to nation state threat actors. Key findings in this report include:

- 2024 saw a 146% increase in sites suffering physical impairment of operations because of cyber attacks, rising from 412 sites in 2023 to 1,015 in 2024. Most attacks impacted multiple physical locations.
- Nation-state attacks with physical consequences tripled in 2024 compared to the previous year.
- There were 76 attacks which caused physical consequences on OT organizations. This is a 5% increase over the previous year.
- Making up 37% of all attacks, the transportation industry was the single biggest vertical impacted by OT cyber attacks with physical consequences in 2024.
- The discrete manufacturing and transportation industries continue to dominate OT attacks with physical consequences.
- New ICS/OT-designed malware are increasingly being discovered in the wild.

In short, the OT threat environment and its consequences continues to worsen.

> 146% increase in sites impacted by cyber attacks with physical consequences.

## Introduction & Methodology
This report documents cyber attacks with physical consequences. Security teams seeking funding for cybersecurity initiatives and business decision makers responsible for allocating such funding each need accurate data as to what attacks have occurred in the past and what we should reasonably expect of the attack environment in the future. Planning for the future is especially challenging and important for high-consequence operations where every change can pose a threat to safe and correct operations, which means changes and upgrades to our security programs can be made only at long intervals.

In support of understanding today’s threats and projecting tomorrow’s, this report documents cyber attacks on physical operations and infrastructure that:

- are deliberate in nature – not errors and omissions, not equipment nor software failures;
- produce physical consequences including production delays and outages, equipment damage, environmental disasters, injuries or casualties – not just data theft or computer system clean-up costs;
- impacted manufacturing, building automation, heavy industry, and critical industrial infrastructures, including transportation of people and goods;
- are found in public – not private – disclosures;
- and which the research team agrees meet the above criteria with a high degree of confidence.

This report’s data is a conservative estimate, underreporting actual attack activity. Many incidents were excluded due to disclosure restrictions, insufficient confidence in authenticity, or lack of access to reports in certain languages or regions. Additionally, numerous attacks likely went unreported or were unreliable, particularly in censored or conflict zones. As a result, the actual severity of today’s threat environment is certain to be higher than the figures presented.

> In 2024, there were 76 attacks that met the strict inclusion criteria for this report.

Any reader wishing to verify the data can consult Appendix A, which contains the full data set of all incidents since 2010 and their public descriptions.

This report also touches on important developments in the threat environment in 2024 in addition to the incident data above, including:

- near misses – important incidents that did not cause physical consequences but are noteworthy for other reasons;
- so-called “living off the land” attacks that are very difficult to detect;
- and three new ICS-capable types of malware discovered in 2024.

We conclude with defensive highlights of 2024 and recent developments in ICS defenses including:

- New advice from multiple agencies that encourages more secure remote access and solutions than VPNs, including hardware-enforced remote access protections for OT systems.
- New advice that describes principles of OT security, especially the safety imperative.
- The beginning of a shift of terminology to “credible threats” rather than “attack likelihood” in OT security standards and guidance.

As the threat environment worsens, more kinds of attacks which were previously ignored are becoming credible threats that must be addressed in security programs.

This report is a cooperative effort between Waterfall Security Solutions and the ICS Strive OT incident repository. We hope you find the material useful.

> The incident database numbers in this report regarding attack and outage activity are certain to be an underestimation.

## OT Incident Macro Trends
In 2024, there were 76 attacks that met the strict inclusion criteria for this report. Most attacks affected multiple physical sites. This is a 5% increase over the 72 attacks in the data set for 2023.

![Graph showing Incidents with physical consequences (2010 - 2024) and FBI-reported OT Ransomware incidents. The left Y-axis (Incident Count) ranges from 0 to 140, and the right Y-axis (FBI Reported OT Ransomware) ranges from 0 to 800. The X-axis shows years from 2010 to 2024. The graph indicates a general upward trend for both types of incidents over the years, with a notable increase in physical consequences incidents in recent years.](Figure-1-Incidents-with-physical-consequences-2010-2024.png)
Figure 1: Incidents with physical consequences (2010 - 2024)

The complete count of attacks in the data set since 2010 is illustrated in Figure (1). Most of these attacks were ransomware. Most of the attacks impaired physical operations at multiple sites. For comparison, the line in the chart also indicates the number of OT ransomware incidents reported to the Federal Bureau of Investigation[^1] for the years where this data exists[^2], not all of which resulted in physical consequences.

[^1]: Note that the scale for incidents with physical consequences is at the left of the chart, and the different scale for FBI-reported incidents is at the right.
[^2]: The FBI’s IC3 group releases their annual report by mid-March, and so 2024 statistics are not available at the time of this report’s writing.

> In 2024, 87% of identifiable attacks were ransomware.

For 2024, the ICS STRIVE OT incident repository also reported 390 incidents, not all of which met the inclusion criteria for this report. Readers interested in the broader set of incidents impacting businesses with physical operations should consult ICS Strive.

> 16hrs: The average time it takes between a ransomware criminal gaining remote control of some machine on a network and encryption activity starting. Half of attacks are even faster than that.

## SEC Filings
What is the reason for the slowing rate of increase in OT security incidents? One likely factor is that in late 2023 the US Securities and Exchange Commission (SEC) started enforcing regulations that require publicly traded businesses to disclose “material” cybersecurity incidents; incidents that reasonable investors might use as cause to buy, sell or value shares in the victim company. Similar rules are already in place or are coming soon in many jurisdictions. These new rules for incident disclosures may well affect the number of incidents in the public record.

> New SEC & other incident disclosure rules may be reducing, rather than increasing, public reports of cyber attacks with physical consequences.

In December 2023, the SEC reduced somewhat the level of detail needed in these reports out of concern that too much public disclosure might either impede incident response or provide other attackers too much of a road map as to how to attack similar sites. On the other hand, the SEC is prosecuting businesses who fail to disclose cyber incidents adequately. In June 2024, the SEC accepted a $2.1 million civil penalty settlement offer from R. R. Donnelley & Sons in part for disclosure violations from 2021-2022, predating the new, even stronger disclosure rules.

Given these new public disclosure rules in many jurisdictions, one might assume public reports of cyber attacks causing physical consequences would increase sharply during 2024 over 2023. But this was not the case. Why?

> New disclosure rules may be prompting legal teams to get involved in cyber incident investigations earlier and requiring a minimal level of public disclosure. Following the prosecution of SolarWinds executives for improper disclosure of details of cybersecurity programs, legal teams may have decided to limit public reporting to only what is legally required to reduce the risk of similar legal consequences. If this is occurring, it would tend to reduce the number of non-material incident disclosures and reduce the level of detail published for potentially material incidents.

## Nation States & Hacktivists
Nation state and hacktivist attacks both seek to bring about physical consequences with cyber attacks. This is in contrast with ransomware criminal groups who are financially motivated and generally seek to extort cryptocurrency.

In ransomware attacks, physical consequences are most often accidental side effects of extortion attempts. While the numbers involved are still small, Figure (2) shows what appears to be a marked change in the frequency of hacktivist and nation state attacks since 2022 – attacks deliberately targeting physical operations and often critical infrastructures.

![Graph showing Nation State and Hacktivist Attacks with Physical Consequences (2010 - 2024). The Y-axis (Count) ranges from 0 to 10. The X-axis shows years from 2010 to 2024. Two lines represent "Nation State" and "Hacktivists". Both show a significant increase in attacks from 2022 to 2024, with Nation State attacks reaching 9 and Hacktivist attacks reaching 6 in 2024.](Figure-2-Nation-state-and-hacktivist-attacks-with-physical-consequences-2010-2024.png)
Figure 2: Nation state and hacktivist attacks with physical consequences (2010 – 2024)

Most attacks relate to three ongoing geopolitical conflicts:
1. The Russo – Ukrainian war
2. The Israel – Hamas (Iranian proxy) war
3. The Western Democracy-Chinese Grey Zone Conflict

> “The greatest long-term threat facing our country, in my view, is represented by the People’s Republic of China … which I consider to be the defining threat of our generation.” … “[The] Chinese government [is] pre-positioning on American civilian critical infrastructure. To lie in wait on those networks, to be in a position to wreak havoc, can inflict real-world harm at a time and place of their choosing.”
> FBI Director Christopher Wray
> Source: CBS News

In 2024, we saw significant incidents and near misses in all three conflicts which are detailed in this report. In addition, sophisticated Russian and Chinese nation-state attacks are targeting a wide array of Western infrastructures, thus far without serious physical consequences. The most important development in 2024 regarding nation state attacks is the near-universal conclusion by Western intelligence agencies and governments that the ongoing threats from China are the most significant and of greatest concern. See the section “Volt Typhoon’ and Salt Typhoon” for additional details.

## Number Of Sites Impacted
There was a year-over-year increase of 146% in the number of sites impacted by attacks with physical consequences. The number of sites affected per incident is also increasing.

> 146% increase in sites impacted by cyber attacks with physical consequences.

![Graph showing Number of Sites Impacted (2010 - 2024, excluding “outliers”). The Y-axis (Count) ranges from 0 to 1200. The X-axis shows years from 2010 to 2024. The graph shows a significant increase in the number of sites impacted, especially from 2022 to 2024, reaching over 1000 sites in 2024.](Figure-3-Number-of-Sites-Impacted-2010-2024-excluding-outliers.png)
Figure 3: Number of Sites Impacted (2010 – 2024, excluding “outliers”)

Figure (3) excludes "outlier" incidents where the concept of "number of affected sites" is unclear. For example, if the Russian military jams or spoofs GPS signals across a large region, how should we count the affected "sites"? Should every cell phone be counted? For a more detailed breakdown of site counts, see Appendix A.

## Impacted Industries
Much like in 2023, 2024’s cyber attacks with physical consequences, illustrated in Figure 4, continue to disproportionately impact the transportation and discrete manufacturing industries. In 2024, these industries make up 69% of all incidents. While transportation is the single biggest impacted vertical at 37% in 2024, transportation and discrete manufacturing have alternated in “first place” for the last three years.

> 69% of attacks with physical consequences hit the transportation and discrete manufacturing industries.

![Pie chart showing Impacted Industries (2024). The largest segments are Transportation (37%) and Discrete Manufacturing (32%). Other segments include Water, Building Automation, Process Manufacturing, Food & Beverage, Power, Metals and Mining, and Pharma.](Figure-4-Industries-Impacted-2024.png)
Figure 4: Industries Impacted (2024)

Attacks on North America’s water and wastewater sector increased in significance and number in 2024. This report documents seven (7) new consequential attacks and near misses on water utilities. While the number of attacks causing OT impacts remained the same as last year (2 incidents), the overall threat level increased with all but one of the seven attacks attributed as nation-state sponsored. Five of the seven attacks in 2024 were attributed to Russia’s Sandworm group, a group notorious for attacks on Ukraine’s power grid. These attacks were part of a “grey zone” campaign where Sandworm masqueraded as hacktivists who called themselves the Cyber Army of Russia Reborn (CARR). See the ‘Near Misses’ section below for more information about attacks on water utilities.

Other industry trends:
- Both the power and metals & mining industries disclosed a small number of incidents this year (5 combined), with similar numbers last recorded in 2022 (6 combined).
- Incident counts remain steady in the process manufacturing, food & beverage, and pharmaceuticals verticals.
- 2024 saw two more incidents in automated “smart” buildings, both on the hospitality industry.
- The oil and gas sectors saw no new disclosed incidents in 2024.

![Two pie charts side-by-side showing Impacted Industries for 2022 and 2023. Both charts show Transportation and Discrete Manufacturing as the largest segments, with other industries like Water, Food & Beverage, Process Manufacturing, Power, Metals and Mining, Pharma, Building Automation, and Oil & Gas making up smaller portions. The distribution varies slightly between the two years.](Figure-5-Impacted-Industries-2022-2023.png)
Figure 5: Impacted Industries (2022 & 2023)

## Impacted Regions
Regionally, the USA and Germany suffered the largest number of incidents with physical consequences in 2024, in first and second place respectively, followed by Japan, the UK and Canada.

> The USA and Germany suffered the largest number of incidents with physical consequences in 2024.

![Bar chart showing Impacted Regions 2024. The USA and Germany have the highest number of incidents, followed by Japan, UK, Canada, and other regions including Taiwan, Russia, Lebanon, Finland, France, Sweden, Italy, and Belgium.](Figure-6-Impacted-Regions-2024.png)
Figure 6: Impacted Regions (2024)

While the reasons for these regional numbers and trends are unclear, it may be that criminal ransomware is exploring new territories with strong economies and a willingness to pay ransoms, or it may also be that politically supported ransomware criminals and nation state threats are strategically targeting victims in the US, Europe, and Asia-Pacific.

## How was OT Impacted?
For attacks where the attack pattern could be determined from public records, 13% of attacks with physical consequences directly impacted OT automation systems. Nearly 90% of attacks caused physical consequences indirectly. This is very similar to data from 2023.

> Almost 90% of indirect attacks on OT had physical consequences.

![Two pie charts side-by-side showing OT Impacts for 2023 and 2024. Both charts show a large "Indirect" segment (around 87-88%), a smaller "Direct" segment (around 13%), and a very small "Unknown" segment.](Figure-7-How-cyber-attacks-caused-physical-consequences-2023-2024.png)
Figure 7: How cyber attacks caused physical consequences (2023 & 2024)

To generally clarify how these types of attacks are defined:
- Direct attacks are those where malware was found on OT systems or impacted OT systems directly, or where remote-controlled attacks reached into OT systems to sabotage them or shut them down.
- Indirect attacks are those where there was no direct impact on OT systems, but physical operations still suffered physical consequences because operations depended on access to or services from impaired IT systems.
- Unknown attacks are incidents where there was not enough detail in the public record to determine how the attack impaired operations.

Analyzing the entire 2010-2024 data set in more detail, we determine there are eight ways in which physical operations have been impacted – five direct and three indirect, namely:

Direct attack types:
1. Attacks on OT are local or remote attacks where attack software or manual attack actions directly affect OT automation systems or networks.
2. Poor segmentation are attacks where there is no evidence the OT network is distinct from an IT network – i.e. the network is “flat” – so any attack on IT is also an attack on OT.
3. IT pivoting attacks first compromise IT assets and then use the compromised assets to attack other IT or OT assets.
4. Supply chain attacks are where a threat actor surreptitiously inserts malware or vulnerabilities into software or firmware for assets deployed on OT networks.
5. Malicious insiders are where an insider uses their credentials and/or position of privilege to attack OT systems.

Indirect attack types:
6. Abundance of caution shutdowns occur when an attack compromises IT systems and the business pre-emptively shuts down OT systems for safety reasons, to reduce risk, to preserve forensic evidence, on the advice of third parties, or for other reasons.
7. IT dependencies are where OT systems or physical operations depend on services provided by IT networks and servers, and those IT assets are impaired or crippled by a cyber attack.
8. 3rd party outages where an enterprise suffers no cyber attack, but one of their suppliers does, and the loss of production, or loss of trust in the supplier, or other consequence of the compromised supplier cause the affected enterprise to reduce, delay or halt production.

Of all the attacks in our data set (2010-2024) where the attack type could be determined reliably from the public record, OT shutdowns due to “abundance of caution” and OT dependencies on IT networks were the most common ways that attacks on IT networks impacted operations. When attacks deliberately targeted OT – Direct OT attacks – nearly all those attacks were attributed to either hacktivists or nation state threat actors.

> Nearly all Direct OT attacks are attributed to either hacktivists or nation-state threat actors.

## Implications For Cybersecurity Programs
What does this mean for cybersecurity programs? A naïve interpretation might suggest that, since most attacks with physical consequences target IT networks, incremental spend on cybersecurity programs should focus primarily on strengthening IT networks. However, the authors of this report argue that this interpretation is flawed for several reasons.

> IT networks are constantly exposed to the Internet, making them intrinsically vulnerable. Safety-critical networks require a level of security that goes beyond what is possible for IT networks.

1. Safety-critical OT networks must be designed and secured to be extremely robust in the face of all possible inputs and threats. IT networks are exposed to constant interaction with the Internet and thus it is not possible to secure IT networks to the extent that safety-critical networks must be secured. Furthermore, there is a general expectation that less-consequential IT networks can be more flexible about network and cybersecurity program designs than OT networks, but this flexibility and its benefits vanish if we demand they be secured to safety-critical standards.
2. The best way to eliminate “abundance of caution” shutdowns (attack type #6) is to strengthen OT security programs, and especially protections at the IT/OT interface to the point where it becomes practically impossible for cyber attacks to pivot from IT networks into OT networks.
3. The best way to eliminate “IT dependency” shutdowns (attack type #7) is to understand dependencies and take steps either to eliminate those dependencies, or to put network engineering and incident response measures in place to reduce to acceptable levels all cyber incident downtime for reliability-critical IT components.

> It should be physically impossible for cyberattacks to pivot from IT networks into high-consequence OT networks.

The norm today in industrial enterprises is IT cybersecurity programs are much more mature than OT cybersecurity programs. It is in this context that we observe cyber attacks with physical consequences nearly doubling annually. Doubling down on this practice of continuing to emphasize IT protections over OT will not reduce the slope of the OT incidents curve (in Figure 1).

## Incident Costs
While costs continue to be difficult to identify, there were some noteworthy costs that were disclosed or could be calculated in 2024. In one high-profile attack, OT systems and services provider Halliburton had IT systems taken offline. The company has not shared many details about the attack, causing other customers to disconnect from Halliburton due to the lack of details provided. To date, costs related to the attack total a reported $35 million.

In another case, global contract manufacturer, Keytronic, reported an incident in May after disruptions at its Mexico and U.S. sites impacted business applications supporting operations and corporate functions. Keytronic was forced to shut down domestic and Mexican operations for two weeks during the incident response. To date, the attack has cost Keytronic over $17 million. The Stoli Group USA filed for Chapter 11 in US Bankruptcy Court after a malicious cyber attack forced the company to operate its global business manually while the systems are rebuilt. While there were multiple reasons for the bankruptcy, the cyber attack was cited as a top reason.

## Supply Chain – CrowdStrike Incident
The July 2024 CrowdStrike failure was not a cyber attack, but the incident highlighted many industries’ vulnerability to supply chain attacks. The incident was a defect in a software update pushed out to customers configured for automatic updates, causing some 8.5 million devices to crash and have difficulty rebooting. Thousands of flights were cancelled, Tesla halted production at a large factory for four hours, the Port of Houston closed briefly, and a Swedish mine briefly shut down and evacuated as a precaution, just to name a few.

> When worst-case consequences are unacceptable, all non-trivial changes and updates must be tested and evaluated for security as well as reliability.

The obvious lesson widely drawn from the incident is, when the consequences of malfunction or unavailability of computer equipment and networks are unacceptable, owners and operators should test software and security updates for reliability before deploying those updates. As the 2020 SolarWinds incident showed, however, the same lesson should be applied to malicious cyber attacks. All changed software or non-trivial updates must be tested and evaluated for security as well as reliability, to prevent malicious updates from impairing operations.

Cost estimates of the CrowdStrike incident to IT & OT owners and operators range from $5 billion to $10 billion.

## Global Navigation & IRS Jamming and Spoofing
The 2024 data set includes three navigation system jamming and spoofing events, colloquially called “GPS” events[^3]:

- Finnair cancelled all flights between Helsinki and Tartu, Estonia for 6 weeks because widespread GPS spoofing made the route unsafe, and until a certified alternative navigational system could be deployed.
- GPS jamming contributed to the crash of Azerbaijan Airlines Flight 8243 near Aktau, Kazahkstan and the death of 38 passengers.
- A nearly 64-hour stretch of GPS jamming over Poland, Sweden and Germany in March affected 1600 flights with Russia considered the prime suspect.

[^3]: When we use the acronym “GPS” in the report, we mean all satellite navigation which is termed global navigation satellite systems (GNSS). This includes the US GPS, EU Galileo, Russian GLONASS, and China’s Beidou.

> GPS jamming affected 1,600 flights over Poland, Sweden, and Germany in 64 hours.

Despite an international treaty banning GPS jamming, Russian forces routinely jam and spoof satellite navigation signals. Furthermore, while Inertial Reference Systems (IRS) are back-ups for GPS signal loss in many aircraft, IRS can be confused by GPS spoofing. Many IRS use the higher accuracy of GPS positioning to periodically reset their internal position estimates to account for drift over time and other errors in the aircraft’s position. Thus, when GPS signals are spoofed rather than jammed, IRS systems reset their own understanding of their current location to match the spoofed (false) GPS locations, causing potentially serious safety problems.

Owners and operators of systems that rely on GPS are advised to have plans in place to both detect and ride through GPS outages and falsified GPS signals.

## Near Misses
While near misses are not the focus of this report, we select and report on eleven such attacks that were significant indicators of threat activity. Grey zone attacks are often multiple incidents in sophisticated campaigns that are well resourced and deliberately planned to test an opponent’s defenses and response time. These new nation-state grey-zone campaigns are like the aircraft sorties that routinely test an opponent’s control over their air space. In such sorties, military aircraft routinely and deliberately fly along the edge of an opponent’s airspace to test response times, strength, and other defensive capabilities and tactics. More frequent grey zone attacks do not necessarily imply physical conflict between nations are imminent, but they do represent an escalation in threat and risk to OT systems that should not be ignored.

For example, Sandworm (or CARR) attacks on water utilities appear to have come short of causing significant consequences. In Muleshoe Texas, however, they did cause water tanks to overflow for 30 minutes. After these incidents, credible evidence emerged from Google’s Mandiant team revealing that CARR was directly supported by Unit 74455 of Russia's GRU military intelligence directorate.

In several of their attacks, CARR bragged and taunted their victims on Telegram and social media that they could have done much worse. These types of nation state attacks are often called grey zone attacks and are becoming more frequent.

**2024**
- **Jan**
  - Industry: Water
  - Attack Type: Direct on OT
  - Victim & Description: Abernathy, Texas Water - An attack attempted to mis-operate control systems by exploiting an active VPN. Staff detected the attempt and cut off the session in 30 seconds, blocking the attack.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **Jan**
  - Industry: Water
  - Attack Type: Direct, first pivoting through IT
  - Victim & Description: Hale Center, Texas Water – The city reported 37,000 attempted logins to their firewall in 4 days. Amongst many source IPs were several originated in St. Petersburg. Once discovered, the city isolated its water systems from the internet and operated manually.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **Jan**
  - Industry: Water
  - Attack Type: Not applicable
  - Victim & Description: Lockney, Texas Water – The city manager said an attack on their water system was detected and thwarted, causing only a minor nuisance.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **Apr**
  - Industry: Water
  - Attack Type: Direct, first pivoting through IT
  - Victim & Description: Tipton Municipal Utilities (TMU) -- Sandworm-linked group CARR infiltrated and claimed to have mis-operated an operator's HMI controlling the water treatment process. The utility reports remaining operational.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **June**
  - Industry: Telecom
  - Attack Type: IT only
  - Victim & Description: SingTel -- Systems were breached in Singapore by Volt Typhoon group in an ongoing campaign against the USA and their allies. Experts believe this was a test-run for future attacks on the USA.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **Sep**
  - Industry: Transport
  - Attack Type: Not applicable
  - Victim & Description: German Air Traffic Control (DFS) -- DFS suffered a cyber attack by Russia's Fancy Bear nation state threat actor. While no physical consequences occurred, and few details were released the threat actor’s capabilities are so high this counts as a credible near miss.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **Sep**
  - Industry: Water
  - Attack Type: Unknown
  - Victim & Description: Arkansas City Water -- Water treatment at Arkansas City reverted to manual operations in a cyber attack attributed to ransomware.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **Oct**
  - Industry: Telecom
  - Attack Type: Not applicable
  - Victim & Description: 21 global telcos -- Described as the "worst telecom hack” in history, a new Chinese nation state threat actor is found to have deeply penetrated telecom networks as far back as two years ago in dozens of countries. This campaign exfiltrated call metadata, text messages, and audio content for over 150 top US officials including Trump, Harris and Vance running in both presidential campaigns.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **Oct**
  - Industry: Power
  - Attack Type: Unknown
  - Victim & Description: Fortum Oyj -- Finland's largest company owning and operating over one hundred hydro, CHP, condensing, nuclear, solar and wind generating plants reports daily attempts to penetrate their cyber systems and reported finding many drones hovering over their critical infrastructure sites.
  - Incident Entry: [icsstrive.com](https://strive.com)
- **Nov**
  - Industry: Oil & Gas
  - Attack Type: Unknown
  - Victim & Description: RECOPE -- After a ransomware attack hit Costa Rica's state energy company, safety concerns were cited as the reason for switching to manual operations. This impacted service quality for loading and unloading cargo terminals, at both land (trucking) and sea (tankers).
  - Incident Entry: [icsstrive.com](https://icsstrive.com)
- **Dec**
  - Industry: Oil & Gas
  - Attack Type: Not applicable
  - Victim & Description: Lukoil -- Cyber specialists of Ukraine’s Main Intelligence Directorate (HUR) carried out a cyber attack on Russian oil company Lukoil, which impacted online and retail POS payments at the pumps and during the holiday shopping season.
  - Incident Entry: [icsstrive.com](https://icsstrive.com)

## Volt Typhoon and Salt Typhoon
Other significant grey zone attack campaigns either disclosed in 2024 or continuing into 2024 include two significant campaigns by China. Western intelligence agencies and governments have repeatedly expressed alarm and have declared these the most significant threats to their national security. They include ongoing campaigns by two threat actor groups:

> “Living off the land” attacks operate by remote control without using RAT malware. Instead, the attackers use normal tools built into operating systems to attack other systems. This makes attacks extremely difficult to detect because anti-virus software shows no malware on the machines, only the normal operating system tools.

**Volt Typhoon**
Now recognized as a campaign of nation state attacks on privately-owned critical infrastructure in service and supply agreements to US government and global military operations:

- Early in 2024, the FBI obtained a rare court order to silently clean malware from devices owned by US citizens and organizations, and declared the infections eradicated.
- The FBI, however, cannot clean botnets from non-US owned devices and asked the wider public to be aware of the threat. The threat actor(s) then attempted to maintain persistence in the targeted networks.
- In the summer of 2024, the SingTel (Singapore) breach exposed efforts by the threat actor to create a SE Asia – located pivot point to obscure attack traffic on Western networks.

**Salt Typhoon**
A campaign on telecommunication infrastructure was exposed in the USA and dozens of other nations, persisting in networks dating back at least two years:

- The attacks not only perpetrated widespread metadata collection but also carried out targeted communications interception on the highest levels of government, including Democratic Presidential candidate Kamala Harris, Republican Presidential candidate Donald Trump, and Republican Vice-Presidential candidate JD Vance in the 2024 presidential campaign.
- It’s unclear how Salt Typhoon did this. Did they penetrate telecom switches and backbone routers? Did they install malware? Was this a supply chain attack or work of malicious insiders?
- Telecom is a type of OT that this report does not explicitly track, but the industry’s equipment, expected system reliability, and importance to national security and public safety parallels that of industrial control systems.

The Volt Typhoon attack was also noteworthy in that it was a so-called “living off the land” attack. Such attacks operate by remote control but do not deploy the Remote Access Trojan (RAT) malware that is typically used to maintain remote control. Instead, the attackers use facilities built into the operating systems of compromised IT machines to maintain remote control. This makes the attacks extremely difficult to detect, because any anti-virus or other scan of the affected machines showed no malware resident on the machines, only normal operating system tools.

Volt Typhoon was seen reaching into OT networks and then pulling back to its IT persistence base. The consensus of US intelligence agencies is that the Chinese government is using these footholds in IT networks of US government-linked utilities to establish and maintain a capability to act in future kinetic conflicts.

## New ICS-Capable Malware
2024 saw the discovery of three new ICS-capable malware variants. This is a material increase to the six such malwares discovered in the preceding 14 years (2010-2023):

- **2010**: Stuxnet – cyber-sabotage – autonomous malware destroyed ~1000 uranium gas centrifuges
- **2013**: Havex – cyber-espionage – remote access trojan (RAT) with OPC scanning capabilities
- **2016**: CrashOverride – cyber-sabotage – RAT with the ability to issue commands in four ICS protocols, depending on the version of the malware – turned off the power to Kiev for an hour.
- **2017**: Triton – cyber-sabotage – RAT with the ability to write to SE Triconex Safety Instrumented System controllers – malfunctions triggered safety shutdowns at two petrochemical sites
- **2022**: Pipedream – cyber-sabotage – a RAT with a “Swiss army knife” of ICS hacking tools that was detected before it caused physical consequences
- **2023**: CosmicEnergy – cyber-sabotage – a RAT able to write IEC 60870-5-104 commands, though it may have been used only as an educational tool for Russian penetration testers
- **2024**: FrostyGoop – cyber-sabotage – a RAT able to write Modbus TCP commands – disrupted heating to 600 apartment buildings in Ukraine
- **2024**: IOControl – cyber-sabotage – a RAT targeting ARM-based Linux IoT devices – disrupted fuel pumps in thousands of Iranian gas stations
- **2024**: Fuxnet – cyber-sabotage – autonomous malware that carried out denial of service attacks via Meter-Bus (MBus) RS485 communications and bricked over 500 sensor gateways by repeatedly writing to their NAND-flash firmware repositories.

> Three new ICS-capable malware variants were discovered in 2024, compared to just six found in the previous 14 years.

With discoveries of this kind of malware, ICS-capable malware is becoming an increasingly credible threat to industrial operations.

## Defensive Developments in 2024
Tools, techniques and perspectives for defending industrial control systems continue to evolve as

---

|      |
| ----------- | -------- | --------- | ------- | --------- | ----------- | ----------- | ------ | ----------- | --- | ------------ | --------- | ----------------- | ---------- | ---- |
|             |          |           |         |           |             |             |        | in  series  |     | with         | the       | above-recommended |            |      |
| well.       | In  the  | sections  | below,  |           | we  sample  |             | three  |             |     |              |           |                   |            |      |
|             |          |           |         |           |             |             |        | software    |     | protections  | provides  |                   | OT  sites  | with |
highlights of 2024.
physical control over when and for how long
software-mediated remote access is enabled.
• Again, for attended OT sites, unidirectional
The multi-agency report Modern
remote screen view transmits real-time screen
Approaches to Network Access
images through unidirectional hardware to
Security now recommends  remote service providers. Those providers can
hardware-enforced remote access  then interact with on-site personnel, usually
over the phone, providing real-time advice to
for high-consequence OT networks,
diagnose and correct complex problems.
rather than VPNs and jump hosts.
• For unattended remote access to OT sites, the
guidance recommends hardware-enforced
remote access systems with independent
Hardware-Enforced Remote Access
unidirectional hardware control channels for
American, Canadian and New Zealand authorities
keystrokes and mouse movement that are
issued a joint publication Modern Approaches to
separate from and independent of
| Network  | Access  | Security.  |     | The  | document  |     | is  |     |     |     |     |     |     |     |
| -------- | ------- | ---------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
unidirectional monitoring channels for screen
designed to improve remote access to both IT and
images.
OT networks. For example, for the first time these
| authorities  | recommend  |     |     | moving  | away  | from  | the  |     |     |     |     |     |     |     |
| ------------ | ---------- | --- | --- | ------- | ----- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
In all cases, the new recommendations specify
traditional VPN and jump host designs that are still
remote access solutions that are much stronger
the foundation for other advice, including the NERC
than VPN and jump host technology.
CIP 005 standard. The agencies encourage owners
and operators to adopt more powerful techniques.
OT Security Principles
The document recommends a range of Zero-Trust
|              |     |       |      |     |           |     |      | The  Principles  |     | of     | Operational  |              | Technology  |         |
| ------------ | --- | ----- | ---- | --- | --------- | --- | ---- | ---------------- | --- | ------ | ------------ | ------------ | ----------- | ------- |
| Cloud-based  |     | Tech  | for  | IT  | networks  |     | and  |                  |     |        |              |              |             |         |
|              |     |       |      |     |           |     |      | Cybersecurity    |     | is  a  | joint        | publication  |             | of  16  |
low-consequence OT networks.
|                        |     |     |     |            |     |      |        | government  |     | agencies      | in  | nine  | nations.  | The      |
| ---------------------- | --- | --- | --- | ---------- | --- | ---- | ------ | ----------- | --- | ------------- | --- | ----- | --------- | -------- |
|                        |     |     |     |            |     |      |        | document    | is  | significant,  | in  | part  | because   | of  the  |
| For  high-consequence  |     |     | OT  | networks,  |     | the  | guide  |             |     |               |     |       |           |          |
endorsement of the same set of concepts by such
| recommends  |     | hardware-enforced  |     |     |     |     | network  |     |     |     |     |     |     |     |
| ----------- | --- | ------------------ | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
a wide array of agencies and nations, and in part
segmentation, such as is provided by unidirectional
because of the engineering-centric nature of the
| gateway  | technology.  |     | For  | remote  |     | access  | into  |     |     |     |     |     |     |     |
| -------- | ------------ | --- | ---- | ------- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
principles outlined there.
| unidirectionally  |     | protected  |     | networks,  |     | the  | guide  |     |     |     |     |     |     |     |
| ----------------- | --- | ---------- | --- | ---------- | --- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
recommends:
| 23  |     |     | 2025 OT Cyber Threat Report |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Many statements in this high-level document echo  Credibility, not Likelihood
concepts in the Cyber-Informed Engineering (CIE)
|             |     |            |      |      |                  |     |       | A  key  | principle  | of  | CIE  | is  that  | risk  |     | management  |
| ----------- | --- | ---------- | ---- | ---- | ---------------- | --- | ----- | ------- | ---------- | --- | ---- | --------- | ----- | --- | ----------- |
| initiative  | –   | precisely  | the  | mix  | of  engineering  |     | risk  |         |            |     |      |           |       |     |             |
should start with the highest-consequence threats,
| management  |     | and  | cyber  |     | risk  | management  |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ---- | ------ | --- | ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
not the highest-frequency threats. To reflect this
| concepts     |     | that  | is  being   | so        | well  | received  | by      |            |     |         |     |            |     |     |              |
| ------------ | --- | ----- | ----------- | --------- | ----- | --------- | ------- | ---------- | --- | ------- | --- | ---------- | --- | --- | ------------ |
|              |     |       |             |           |       |           |         | emphasis,  | a   | number  | of  | standards  |     |     | bodies  and  |
| engineering  |     | and   | enterprise  | security  |       | teams     | in  so  |            |     |         |     |            |     |     |              |
authorities that issue OT risk assessment and risk
many businesses with physical operations.
management guidance are considering a change
|     |     |     |     |     |     |     |     | to  the  | terminology  |     |     | of  | their  |     | publications,  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------------ | --- | --- | --- | ------ | --- | -------------- |
The first principle in the document for example is  focusing  on  the  concept  of  “credibility”
that  safety  is  paramount  –  not  confidentiality,  rather  than  “likelihood.”
integrity or availability of data. The document asks
| questions  |     | never  | before  | seen  | in  | government  |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | ------- | ----- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Threats that were not considered
| guidance  | –   | questions  |     | such  | as  “If  | software  | is  |     |     |     |     |     |     |     |     |
| --------- | --- | ---------- | --- | ----- | -------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
essential to the safety of a physical process, and  credible a decade ago are now
there is a real risk that an adversary has taken over
pervasive.
that software, how will the organization assure the
safety of incident responders sent to the site to
| investigate  |     | the  | breach?”  | And  |     | the  guidance  |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ---- | --------- | ---- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Standard thinking about cyber risk holds that given
| acknowledges  |     | the  | importance  |     | of              | deterministic  |     |          |        |        |           |     |          |      |               |
| ------------- | --- | ---- | ----------- | --- | --------------- | -------------- | --- | -------- | ------ | ------ | --------- | --- | -------- | ---- | ------------- |
|               |     |      |             |     |                 |                |     | enough   | time,  | money  | and       |     | talent,  | any  | defensive     |
| protections   |     | in   | addition    | to  | software-based  |                |     |          |        |        |           |     |          |      |               |
|               |     |      |             |     |                 |                |     | posture  | can    | be     | breached  |     | by       | a    | sufficiently  |
protection.
sophisticated attack. In our 2024 data we observe
|     |     |     |     |     |     |     |     | that  | attacks  |     | are  | becoming  |     |     | increasingly  |
| --- | --- | --- | --- | --- | --- | --- | --- | ----- | -------- | --- | ---- | --------- | --- | --- | ------------- |
If software is essential to the safety
sophisticated.
of a physical process, and there is a
Types of attacks that were not considered credible
real risk that an adversary has taken
|     |     |     |     |     |     |     |     | threats  | a  decade  |     | ago  | have  | become  |     | pervasive.  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | ---- | ----- | ------- | --- | ----------- |
over that software, how will the
|     |     |     |     |     |     |     |     | Effective  | discussion  |     | and  | decision  |     | making  | about  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ----------- | --- | ---- | --------- | --- | ------- | ------ |
organization assure the safety of
sophisticated, high-consequence threats demands
incident responders sent to the site  that decision-makers decide what types of attacks
and consequences constitute credible threats to
to investigate the breach?
physical operations today and in the near future,
and what defenses are reasonable to implement,
The document is ground-breaking in that it is the
given these credible threats.
first time that such a wide array of agencies and
authorities have issued cybersecurity guidance
The research team looks forward to much greater
with such a strong engineering focus and with such
use of words like “judgement,” “reasonable,” and
a clear explanation of the role of engineering
“credible” in future standards and guidance.
principles, tools, and approaches in cybersecurity
programs.
| 24  |     |     | 2025 OT Cyber Threat Report |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Conclusion
With only a small increase in incidents that caused ICS-focused/ICS-capable malware discoveries in
physical consequences, one might be tempted to 2024 as in all the previous decade and a half.
argue we are winning the cyber war, at least on OT
networks. In fact, the sophistication and Increasingly capable cyber attacks are becoming
capabilities of our adversaries continue to increase credible threats. Owners and operators are advised
with near-miss/living-off-the-land techniques to re-evaluate what threats they regard as credible
applied at over 50 utilities, a steadily increasing today, as well as threats which are likely to become
number of impacted sites, and one third as many credible in the years ahead, and take reasonable
new actions to address those credible threats.
Owners and operators are advised to re-evaluate what threats they
regard as credible and take reasonable actions to address those threats.
25 2025 OT Cyber Threat Report

APPENDIX A – The Complete Data Set
Field Descriptions Type = OT Attack Type: How the attack caused
physical consequences:
• DO: Direct, on OT – malware or threat actor
Date: Date the incident was detected or occurred.
manipulated OT systems,
Victim: The impacted organization’s name.
• DS: Direct, poor segmentation – no separate OT
Region: Region of impacted sites. When sites are
network existed,
impacted in multiple regions, the region of the head
• DIP: Direct, IT pivot – an attack “pivoted”
office is reported.
through compromised IT assets to attack OT
Industry: Industry of the affected sites.
assets,
TA = Threat Actor: The type of threat actor, one of:
• DSC: Direct, supply chain – the attack inserted
• R: Ransomware
malware or vulnerabilities into products
• H: Hacktivist
deployed on OT networks,
• I: Insider
• DM: Direct, malicious insider – an insider used
• NS: Nation state
their credentials or privilege to bring about
• SC: Supply chain
physical OT consequences,
• U: Unknown
• IA: Indirect, abundance of caution – the victim
Attribution: Specific threat actor publicly reported
shuts down physical operations pre-emptively
or claimed responsibility.
after the attack was detected,
• ID: Indirect, IT dependency – physical
Sites: Total number of sites affected.
consequences were realized when only IT
Cost: Lower-bound estimate of financial impact on
systems were compromised, because physical
victim organization, in USD unless otherwise
operations depended on one or more IT systems
indicated.
or services, and
FD = Financial Disclosure: Entity to which financial
• I3: Indirect, third party – victim suffered no
disclosure was required or made, if any:
cyber attack but shut down because a supplier
• SEC: Securities and Exchange Commission (US),
was attacked.
• NSE: National Stock Exchange (Mumbai, India),
OT / ICS Physical Consequences: how the victim
• EU MAR: Market Abuse Regulation No 596/2014
suffered.
Article 17 (EU),
Incident Summary: summary of what happened.
• LSE: London Stock Exchange (UK).
References: Links to public reports on the incident.
• PIPC: Personal Information Protection
Commission (Kojin Jōhō Hogo Iinkai)
• TASE: Tel Aviv Stock Exchange (ְךרֶ עֵ תוֹריָיְנִל הסָ רְ וּבּהַ
ביבִ אָ לתֵ בְּ
26 2025 OT Cyber Threat Report

Incidents in 2024
Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor | Actor Attack  | Physical  |     |     |
| ----- | ------------- | --------- | --- | --- |
Type Consequences
2024-01-07 Beirut  Lebanon Transport U Unknown 1 U Disrupted the  A breach of the airport's  https://icsstrive.com/incident/cy
(Rafik- Flight  cybersecurity resulted in  berattack-on-beirut-airport-
| Hariri)  |     | Information     | baggage belts malfunctioning  | lebanon/ |
| -------- | --- | --------------- | ----------------------------- | -------- |
| Int’l    |     | Display System  | and a hostile message to      |          |
https://today.lorientlejour.com/a
Airport (FIDS) network  Hezbollah showing on screens  rticle/1364771/lasting-
|     |     | and reduced the  | meant to display flight details.                            | consequences-at-beirut-airport-   |
| --- | --- | ---------------- | ----------------------------------------------------------- | --------------------------------- |
|     |     | Baggage          | A source at national airline MEA following-cyberattack.html |                                   |
|     |     | Handling System  | confirmed the Flight                                        |                                   |
|     |     | (BHS) to 20%     | Information Display System                                  | https://today.lorientlejour.com/a |
rticle/1363591/cyberattack-at-
|     |     | capacity for 10+  | (FIDS) network had been  | beirut-airport-what-happened- |
| --- | --- | ----------------- | ------------------------ | ----------------------------- |
|     |     | days              | penetrated.              |                               |
and-what-are-the-potential-
risks.html
2024-01-18 Muleshoe, USA Water NS Cyber Army 1 DIP Impacted  Originally attributed to  https://icsstrive.com/incident/cy
Texas  of Russia  operations by  hacktivist group CARR,  berattack-on-three-rural-texas-
Water Reborn  mis-operating  Sandworm-supported  water-facilities/
|     | [CARR] &  | the control  | hacktivists bragged online  |     |
| --- | --------- | ------------ | --------------------------- | --- |
Sandworm  system and  about their attack on  https://www.wired.com/story/cy
ber-army-of-russia-reborn-
[GRU Unit  causing water  Muleshoe’s ICS.  sandworm-us-cyberattacks/
|     | 74455]  | tanks to overflow Mandiant/Google published  |     |     |
| --- | ------- | -------------------------------------------- | --- | --- |
(Russia) for 30+ mins detailed analysis linking CARR  https://cloud.google.com/blog/t
|     |     |     | to nation-state group  | opics/threat-intelligence/apt44- |
| --- | --- | --- | ---------------------- | -------------------------------- |
unearthing-sandworm
Sandworm and the Russian
GRU. In late July, the US
https://therecord.media/cyber-
|     |     |     | Treasury sanctioned Yuliya  | army-russia-us-sanctions |
| --- | --- | --- | --------------------------- | ------------------------ |
Pankratova and Denis
Degtyarenko, holding them
responsible for this incident
and a series of similar
"unsophisticated" attacks on
critical infrastructure in the US
and the EU.
2024-01-20 Tietoevry  Finland,  Transport R Akira 200 30M  I3 Impacted  Finnish cloud service provider  https://icsstrive.com/incident/nu
Oyj /  Sweden,  kr. logistics  Tietoevrywas hit by a  merous-customers-suffer-from-
ransomware-attack-at-cloud-
Rusta Norway,  (inventory  ransomware attack, which  provider-tietoevry/
| Germany |     | tracking and     | impacted their customers like                                      |                                  |
| ------- | --- | ---------------- | ------------------------------------------------------------------ | -------------------------------- |
|         |     | replenishment)   | Rusta. Rusta, a discount hard                                      | https://www.bleepingcomputer.c   |
|         |     | and order        | goods retailer, relied on                                          | om/news/security/tietoevry-      |
|         |     | fulfilment,      | Titoeveryfor all business                                          | ransomware-attack-causes-        |
|         |     | materially       | functions including supply chain outages-for-swedish-firms-cities/ |                                  |
|         |     | impacted sales,  | (logistics) management.                                            | https://investors.rusta.com/en/r |
for 2+ wks
ustas-business-systems-are-
fully-operational-after-
disruptions/
https://investors.rusta.com/en/u
pdate-on-operational-
disruptions-in-rustas-it-system-2/
27

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2024-01-22 Lvivteplo Ukraine Power U FrostyGoop  600 DIP Disconnected  In July, a novel malware called  https://icsstrive.com/incident/m
energo (Unknown) heating services  FrostyGoop was found by  alware-caused-ukranian-energy-
company-to-disconnect-heating-
|     |     | to 324 "heating  | Dragos to be exploiting a zero   |                                 |
| --- | --- | ---------------- | -------------------------------- | ------------------------------- |
|     |     | points" or 600   | day in internet-facing Mikrotik  | services-impacting-over-100000- |
people/
|     |     | homes in Lviv's  | routers at an un-named heating  |     |
| --- | --- | ---------------- | ------------------------------- | --- |
|     |     | Sykhiv           | utility. This malware is        |     |
https://www.sans.org/blog/what
|     |     | neighbourhood  | reportedly the first to send  | s-the-scoop-on-frostygoop-the- |
| --- | --- | -------------- | ----------------------------- | ------------------------------ |
|     |     | for 2 days     | Modbus commands directly      | latest-ics-malware-and-ics-    |
into the victim’s network to mis-controls-considerations/
operate ENCO controllers,
https://www.wired.com/story/ru
|     |     |     | among other capabilities. It is  | ssia-ukraine-frostygoop- |
| --- | --- | --- | -------------------------------- | ------------------------ |
also uniquely located on the
malware-heating-utility/
threat actor's systems, and not
|     |     |     | deployed in the victim's  | https://www.epravda.com.ua/ne |
| --- | --- | --- | ------------------------- | ----------------------------- |
ws/2024/01/23/709063/
network, making it harder to
detect. Ukraine's SBU confirmed
FrostyGoop malware was
responsible for this attack.
Andy Greenberg (Wired) notes
how attack TTP bears hallmarks
of Unit 74455 of the GRU
(Sandworm), but this cannot be
confirmed.
2024-02-02 Etesia  France Discrete  R Unknown 1 €100K ID Shutdown  A small equipment machinery  https://icsstrive.com/incident/fre
nch-ride-on-mower-
| SAS | Mfg. | production for 2+  | manufacturer was hit by a    |                                |
| --- | ---- | ------------------ | ---------------------------- | ------------------------------ |
|     |      | months, and        | cyberattack that caused its  | manufacturer-tries-to-recover- |
from-ransomware-attack/
|     |     | placed the                                   | systems to be encrypted. This                                   |                             |
| --- | --- | -------------------------------------------- | --------------------------------------------------------------- | --------------------------- |
|     |     | company into                                 | prevented systems, essential to https://www.servicedealer.co.uk |                             |
|     |     | receivership for 6 production, from working. |                                                                 | /latest-news/etesia-suffer- |
|     |     | months                                       |                                                                 | crippling-cyber-attack      |
https://www.linkedin.com/posts/
etesia-uk_etesia-uk-statement-
were-pleased-to-announce-
activity-7178434317021286402-
3xMb/
https://www.lesechos.fr/pme-
regions/grand-est/espaces-
verts-etesia-tente-de-se-relever-
de-sa-cyberattaque-2087045
2024-02-02 Welch  USA Food &  R Unknown 1 ID Shut down  An unknown TA, alleged to be a  https://icsstrive.com/incident/w
Food Bev. operations for 1  "criminal group", attempted to  eeks-of-operational-shutdown-
|     |     | month and sent  | extort Welch by encrypting        | at-welch-foods-plant           |
| --- | --- | --------------- | --------------------------------- | ------------------------------ |
|     |     | 200+ workers    | plant systems critical to their   | https://www.goerie.com/story/n |
|     |     | home            | juice, jam and jelly production.  |                                |
ews/2024/02/28/north-east-pa-
|     |     |     | These critical systems were       | welch-foods-plant-victim-cyber- |
| --- | --- | --- | --------------------------------- | ------------------------------- |
|     |     |     | essential to operations at their  | attack-halted-                  |
|     |     |     | North East (lit.) plant in Erie   | production/72750164007/         |
County, PA.

2024-02-11 Ignitis ON Lithuania Power U Unknown 156 ID Disabled publicly  Ignitis' charging services are  https://icsstrive.com/incident/ig
nitis-on-customers-unable-to-
|     |     | located and                                        | implemented on a cloud-based      |                                  |
| --- | --- | -------------------------------------------------- | --------------------------------- | -------------------------------- |
|     |     | privately-owned                                    | SaaS model, making their          | charge-cars-in-lithuania/        |
|     |     | charging stations operations critically dependant  |                                   | https://www.delfi.lt/en/business |
|     |     | for several hours                                  | on those external IT services. A  |                                  |
/data-of-20-000-ignitis-on-
|     |     |     | suspected ransomware attack   | clients-leaked-in-cyber-incident- |
| --- | --- | --- | ----------------------------- | --------------------------------- |
|     |     |     | ad subsequent data breach on  | 95857777                          |
those cloud services caused
|     |     |     | their smartphone app to stop  | https://balticnews.com/hackers- |
| --- | --- | --- | ----------------------------- | ------------------------------- |
leak-data-data-of-around-
|     |     |     | working, preventing customers  | 20000-ignitis-on-customers-in- |
| --- | --- | --- | ------------------------------ | ------------------------------ |
from charging their cars as the
lithuania/
app was critical to the
|     |     |     | charger's functionality. This  | https://madeinvilnius.lt/en/news |
| --- | --- | --- | ------------------------------ | -------------------------------- |
|     |     |     | attack also disabled and       | /Lithuanian-news/On-Sunday,-     |
|     |     |     | disconnected all Ignitis ON's  | the-company-Ignitis-             |
experienced-an-attack,-most-of-
|     |     |     | publicly accessible charging  | the-customers-cannot-charge- |
| --- | --- | --- | ----------------------------- | ---------------------------- |
stations across Lithuania.
their-electric-cars/
28

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack Physical
Type Consequences
2024-02-12 Varta Germany Discrete  U Unknown 5 EU  IA Shut down  Following a cyberattack, Varta  https://icsstrive.com/incident/ge
Mfg. MAR production, for 2+ proactively shutdown their  rman-battery-maker-varta-
|     | weeks | production plants and IT  | group-hit-in-cyberattack/ |
| --- | ----- | ------------------------- | ------------------------- |
systems for "security reasons“
https://www.csoonline.com/artic
|     |     | and to "ensure data integrity." | le/1307574/hackers-paralyze- |
| --- | --- | ------------------------------- | ---------------------------- |
battery-maker-varta-in-
cyberattack.html
https://www.securityweek.com/c
yberattack-disrupts-production-
in-varta-battery-factories/
https://www.csoonline.com/artic
le/3494349/cyberattacke-auf-
batterieherstellerhacker-legen-
varta-lahm.html
2024-02-19 HAL Allergy  Netherlands Pharma R RansomHouse 1 ID Delayed order  A statement on HAL Allergy's  https://icsstrive.com/incident/ra
nsomware-attack-at-hal-allergy-
| Group | processing and   | website admits they were      |                              |
| ----- | ---------------- | ----------------------------- | ---------------------------- |
|       | delivery 32 days | victims of a ransomware       | impacts-customer-deliveries/ |
|       |                  | attack, that could result in  | https://www.hal-             |
large numbers of customers not allergy.com/2024/02/22/notifica
|     |     | receiving their prescription  | tion-statement/ |
| --- | --- | ----------------------------- | --------------- |
products. They blamed their
https://www.hal-
lack of access to data for the
|     |     | service interruption. In an  | allergy.com/2024/03/22/first- |
| --- | --- | ---------------------------- | ----------------------------- |
deliveries-have-been-
|     |     | update on March 22, HAL said  | successfully-resumed/ |
| --- | --- | ----------------------------- | --------------------- |
that orders have resumed
|     |     | shipping but offers few           | https://www.redpacketsecurity.c |
| --- | --- | --------------------------------- | ------------------------------- |
|     |     | additional details on the nature  | om/ransomhouse-ransomware-      |
|     |     | of the attack.                    | victim-hal-allergy/             |
2024-02-20 Continental  USA Discrete  R Play /  1 U Shutdown  Company reports that it  https://icsstrive.com/incident/co
Aeropace  Mfg. PlayCrypt operations suffered an attack that  ntinental-aerospace-discloses-
cyberattack/
| Tech |     | impacted their daily operations  |     |
| ---- | --- | -------------------------------- | --- |
at their Mobile, Alabama HQ. A
|     |     | customer publicly posted that  | https://www.avweb.com/aviatio |
| --- | --- | ------------------------------ | ----------------------------- |
their order for a new engine has n-news/continental-hacked/
been delayed, without being
given any reason. PLAY
https://www.redpacketsecurity.c
|     |     | ransomware later claimed  | om/play-ransomware-victim- |
| --- | --- | ------------------------- | -------------------------- |
responsibility for the attack
continental-aerospace-Tech/
and published exfiltrated data.
2024-02-21 Casino del  USA Bldg.  U Unknown 1 ID Shut down ops  A hotel and casino in Tucson,  https://icsstrive.com/incident/cyberatt
Sol Automati for 7 days,  AZ suffered a cyber attack that ack-causes-widespread-outage-at-
casino-del-sol-az/
on including elec.  disabled door keycards and  https://www.casino.org/news/casino-
|     | access to rooms  | telephones in a widespread  | del-sol-in-tucson-fighting-cyber- |
| --- | ---------------- | --------------------------- | --------------------------------- |
attack/
|     | and phones | outage. |     |
| --- | ---------- | ------- | --- |
https://www.kold.com/2024/02/28/tucs
on-area-casino-victim-attempted-
cyberattack/
https://www.kvoa.com/news/cybersec
urity-expert-sheds-light-on-casino-del-
sol-cyberattack/article_7afbcd50-
d753-11ee-981b-b31776f14851.html
29

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2024-02-22 Int’l Paper / IP USA Process  U Unknown 1 IA Shut down mill  IP Riegelwood Mill was targeted https://icsstrive.com/incident/Int’l-
Riegelwood  Mfg. operations in an  in an attack and decided to  paper-takes-operations-offline-after-
cyberattack/
Mill abundance of  initiate an orderly shutdown in  https://cybermaterial.com/papers-
|     | caution | an abundance of caution. The  | riegelwood-mill-hit-by-cyberattack/ |
| --- | ------- | ----------------------------- | ----------------------------------- |
attacker gained access through https://www.nrcolumbus.com/news/bu
siness/ip-riegelwood-mill-shuts-down-
a third-party vendor.
after-cyberattack/article_df5a0cec-
d17e-11ee-9a58-7f96ccce8480.html
2024-02-23 Sprimoglass Belgium Process  R 8BASE 1 U Shut down  A ransomware attack brought  https://icsstrive.com/incident/producti
Mfg. production for  production to a standstill at  on-halted-at-glass-plant-in-belgium/
https://www.hln.be/tech/hackers-
|     | 10+ days,        | one of the largest glass   | eisen-aanval-sprimoglass-op-wij-    |
| --- | ---------------- | -------------------------- | ----------------------------------- |
|     | furloughed 350+  | manufacturers in Belgium,  | straffen-bedrijven-die-privacy-van- |
werknemers-en-klanten-
|     | workers | preventing a large proportion  | verwaarlozen~aca8516c/?referrer=https |
| --- | ------- | ------------------------------ | ------------------------------------- |
|     |         | of workers from making glass.  | %3A%2F%2Fwww.google.com%2F            |
https://www.hln.be/binnenland/na-
With over 600 computers in
|     |     | their OT network, it will take  | cyberaanval-duvel-moortgat-ook-bij- |
| --- | --- | ------------------------------- | ----------------------------------- |
tweede-grote-belgische-bedrijf-
more than two weeks to restore sprimoglass-ligt-productie-grotendeels-
|     |     | all plant operations. | stil-om-zelfde-reden~a185872d/ |
| --- | --- | --------------------- | ------------------------------ |
2024-02-23 ThyssenKrupp Germany Discrete  U Unknown 3 IA Halted  After suffering an attack on  https://icsstrive.com/incident/hackers-
Automotive  Mfg. production at 3  their autobody manufacturing  breach-systems-at-steel-giant-
thyssenkrupp/
| Body  | autobody plants  | division, the company took IT  |     |
| ----- | ---------------- | ------------------------------ | --- |
Solutions (Heilbronn,  systems offline in response,  https://www.bitdefender.com/blog/hot
forsecurity/cybercriminals-halt-car-
|     | Burghaun, and  | which halted production. | body-production-at-thyssenkrupp-    |
| --- | -------------- | ------------------------ | ----------------------------------- |
|     | Wadern-        |                          | automotive-division/                |
|     | Lockweiler)    |                          | https://www.bleepingcomputer.com/ne |
ws/security/steel-giant-thyssenkrupp-
confirms-cyberattack-on-automotive-
division/
https://www.saarbruecker-
zeitung.de/saarland/saar-
wirtschaft/hacker-angriff-auf-
thyssenkrupp-auch-werk-im-saarland-
betroffen_aid-107637793
2024-03-05 Duvel  Belgium,  Food &  R Stormous 5 IA Shut down  After detecting ransomware in  https://icsstrive.com/incident/belgian-
Moortgat USA Bev. production of 5  their US Subsidiary's network,  duvel-brewery-halts-production-after-
ransomware-attack/
|     | beer brands in  | Duvel's security systems     |                                       |
| --- | --------------- | ---------------------------- | ------------------------------------- |
|     | Belgium and USA | automatically halted global  | https://www.vrt.be/vrtnws/en/2024/03/ |
11/cyber-attack-production-at-all-
|     |     | production as a precautionary  | duvel-moortgat-plants-restarted/ |
| --- | --- | ------------------------------ | -------------------------------- |
safety measure. Shutdown
https://www.techzine.eu/news/security
|     |     | breweries included four Belgian  | /117352/ransomware-pauses-beer- |
| --- | --- | -------------------------------- | ------------------------------- |
locations and their American
production-at-duvel-la-chouffe-and-
|     |     | subsidiary Boulevard Brewing.  | liefmans/ |
| --- | --- | ------------------------------ | --------- |
Duvel refused to pay the
https://www.techzine.eu/news/security
|     |     | ransom and resumed               | /119038/belgian-brewery-duvel-      |
| --- | --- | -------------------------------- | ----------------------------------- |
|     |     | production after restoring from  | moortgats-data-made-public-because- |
company-refused-to-pay/
backup.
2024-03-07 Leicester City UK Power R Inc.  1 ID Lost control over  A ransomware attack shutdown https://icsstrive.com/incident/pr
Council Ransom streetlights,  IT systems at the city, forcing  olonged-effects-of-cyberattack-
|     | leaving them    | the street light system into an  | on-city-of-leicester-almost-two- |
| --- | --------------- | -------------------------------- | -------------------------------- |
|     | permanently on  | uncontrolled "default" mode,     | months-after-initial-attack/     |
|     | for 2+ months   | among other unspecified          | https://www.infosecurity-        |
|     |                 | operational impacts.             | magazine.com/news/leicester-     |
council-documents-leaked/
https://www.bbc.com/news/uk-
england-leicestershire-68881057
2024-03-14 Radiant  Canada Transport U Unknown 3 SEC  IA Delayed delivery  After detected a cyber attack  https://icsstrive.com/incident/ra
Logistics, Inc. 8K and logistical  impacting their Canadian  diant-logistics-isolates-
canadian-operations-after-
|     | services for 1 wk  | operations, they isolated     |                    |
| --- | ------------------ | ----------------------------- | ------------------ |
|     | in Canada          | Canadian systems from the     | cyberattack/       |
|     |                    | rest of their global network  | https://www.board- |
resulting in a local service
cybersecurity.com/incidents/trac
|     |     | outage. | ker/20240320-radiant-logistics- |
| --- | --- | ------- | ------------------------------- |
inc-cybersecurity-incident/
https://therecord.media/radiant-
logistics-cyberattack-canada-
operations
30

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2024-03-16 BerlinerLuft  Germany Discrete  R Unknown 1 IA Shut down  This HVAC parts and equipment https://icsstrive.com/incident/op
erations-severely-disrupted-at-
| Technik  | Mfg. | production 3+  | manufacturer shutdown and  |     |
| -------- | ---- | -------------- | -------------------------- | --- |
GmbH weeks and  isolated systems in an  berlinerluft-manufacturing/
|     |     | delayed product  | abundance of caution to        | https://www.berlinerluft.de/info- |
| --- | --- | ---------------- | ------------------------------ | --------------------------------- |
|     |     | deliveries       | contain a cyber attack, which  |                                   |
cyberangriff/
resulted in operational impacts.
Ops resumed April 8th.
2024-03-22 GPS  Poland,  Transport NS Unknown  1600 DO Jammed GPS for  Russia is the prime suspect of a https://icsstrive.com/incident/air
Jamming  Sweden,  (Russia) 63h40m total,  record-long 63-hour jam on GPS craft-unable-to-receive-gps-
and  Germany impacting flights  signals in the Baltic. From the  signals-in-baltic-sea-the-black-
sea-and-eastern-mediterranean/
| Spoofing |     | over Europe: first  | evening of March 22 to the  |     |
| -------- | --- | ------------------- | --------------------------- | --- |
|          |     | 24 hours over all   | afternoon of March 25,      |     |
https://www.newscientist.com/a
|     |     | three countries,  | interference was spread across rticle/2424678-unprecedented- |                             |
| --- | --- | ----------------- | ------------------------------------------------------------ | --------------------------- |
|     |     | then remainder    | three countries before settling                              | gps-jamming-attack-affects- |
|     |     | solely over       | on Poland for 40 hours,                                      | 1600-aircraft-over-europe/  |
|     |     | Poland            | impacting more than 1600                                     |                             |
https://x.com/rundradion/status
flights.
/1772366665583337827

2024-03-27 Intermarché Belgium Transport R Unknown 2 ID Impacted  A cyber attack hit former  https://icsstrive.com/incident/int
|     |     | logistics at some  | Groupe Mestdagh-branch  | ermarche-hackers-took- |
| --- | --- | ------------------ | ----------------------- | ---------------------- |
advantage-of-mestdagh-brand-
|     |     | stores for 2 days | supermarkets of grocery-giant   |                                   |
| --- | --- | ----------------- | ------------------------------- | --------------------------------- |
|     |     |                   | Intermarché, leading to supply  | take-over-phase/                  |
|     |     |                   | problems at some stores.        | https://www.retaildetail.be/nl/ne |
Attackers targeted IT systems
ws/food/cyberaanval-op-
|     |     |     | that were not fully integrated  | mestdagh-winkels-van- |
| --- | --- | --- | ------------------------------- | --------------------- |
|     |     |     | after Mestdagh was recently     | intermarche/          |

acquired by their new parent a
year prior and demanded a
ransom. Operations were back
to normal days later.
2024-03-29 Omni Hotels USA,  Bldg.  R Daixin  50 $40M ID Disrupted the  Customers who had been  https://icsstrive.com/incident/na
& Resorts Canada Automation Team entire hotel  staying at Omni hotels when  tional-outage-at-omni-hotels-
|     |     | chain's ops.  | the incident started reported  | after-cyberattack/ |
| --- | --- | ------------- | ------------------------------ | ------------------ |
including keycard check-ins being done on paper,
https://www.securityweek.com/c
|     |     | access to rooms,  | room keys not working, and       | yberattack-causes-disruptions- |
| --- | --- | ----------------- | -------------------------------- | ------------------------------ |
|     |     | for 11 days       | being unable to pay with credit  | at-omni-hotels/                |
|     |     |                   | cards.They later resumed April   |                                |
|     |     |                   | 8th.                             | https://www.theregister.com/20 |
24/04/03/omni_hotels_it_outag
e/
https://www.bleepingcomputer.c
om/news/security/daixin-
ransomware-gang-claims-
attack-on-omni-hotels/
2024-03-30 Hoya  Japan Discrete  R Hunters  2 IA Shut down  A ransomware attack on its IT  https://icsstrive.com/incident/at
Corporation Mfg. Int’l production and  network caused the optical  tack-shuts-down-production-at-
lens-maker-hoya/
|     |     | delayed order       | manufacturer to disconnect       |     |
| --- | --- | ------------------- | -------------------------------- | --- |
|     |     | fulfillment for 3+  | servers and bring in a response  |     |
https://www.securityweek.com/l
|     |     | wks | team. As a result, production  | ens-maker-hoya-scrambling-to- |
| --- | --- | --- | ------------------------------ | ----------------------------- |
and ordering systems were
restore-systems-following-
|     |     |     | impacted. Hoya told customers  | cyberattack/ |
| --- | --- | --- | ------------------------------ | ------------ |
to expect ordering delays.
https://www.bleepingcomputer.c
om/news/security/optics-giant-
hoya-hit-with-10-million-
ransomware-demand/
https://www.hoyavision.com/ab
out-hoya/hoya-vision-care-
news/news/it-system-incident-
update-2/
31

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor | Actor Attack  | Physical  |     |     |
| ----- | ------------- | --------- | --- | --- |
Type Consequences
2024-04-09 Moscollector Russia Water NS Blackjack  500 DIP Destroyed or  BlackJack claimed to have  https://icsstrive.com/incident/ics
-malware-fuxnet-disrupts-
|     | [Security  | disabled  | significantly impacted  |     |
| --- | ---------- | --------- | ----------------------- | --- |
Services of  thousands of IIoT Moscollector’s IOT sensor  russian-infrastructure/
Ukraine] /  devices deployed gateway network deployed  https://www.securityweek.com/
Fuxnet throughout  throughout underground utility  destructive-ics-malware-fuxnet-
|     |     | underground         | corridors, providing          | used-by-ukraine-against-russian- |
| --- | --- | ------------------- | ----------------------------- | -------------------------------- |
|     |     | utility corridors,  | telecommunications, district  | infrastructure/                  |

|     |     | impacting  | heating, water, and sewage   |                                 |
| --- | --- | ---------- | ---------------------------- | ------------------------------- |
|     |     | supply,    | services throughout Moscow.  | https://claroty.com/team82/rese |
arch/unpacking-the-blackjack-
|     |     | monitoring and  | Claroty analyzed a Fuxnet  | groups-fuxnet-malware |
| --- | --- | --------------- | -------------------------- | --------------------- |
|     |     | emergency       | malware sample from the    |                       |

|     |     | response | attack adding credibility to    | https://moscollector.ru/%D0%BE- |
| --- | --- | -------- | ------------------------------- | ------------------------------- |
|     |     |          | BlackJack’s claims. Fuxnet has  | %D0%BA%D0%BE%D0%BC%D0%B         |
F%D0%B0%D0%BD%D0%B8%D0%B
the capability of sending
|     |     |     | spurious commands over RS- | 8/  |
| --- | --- | --- | -------------------------- | --- |
485/MBus protocols and
bricking sensor gateways by
destroying their flash memory
chips.
2024-04-11 United  Taiwan Discrete  U Unknown 1 ID Shut down  This solar power panel module  https://icsstrive.com/incident/tai
Renewable  Mfg. production manufacturing company  wan-united-renewable-energy-
Energy Co.,  announced a cyberattack on  corporation-confirms-
cyberattack/
| Ltd. (URECO,  |     |     | their IT systems caused their   |     |
| ------------- | --- | --- | ------------------------------- | --- |
| 聯合再生)         |     |     | factory to shut down, and that  |     |
http://www.aastocks.com/tc/sto
|     |     |     | the financial cost of this  | cks/news/glh-      |
| --- | --- | --- | --------------------------- | ------------------ |
|     |     |     | shutdown was still being    | news/GLH1482129L/1 |
|     |     |     | evaluated.                  |                    |
2024-04-12 Barnett's  Australia Transport R Unknown 1 Bankru U Shut down  A North Wollongong, Australia  https://icsstrive.com/incident/ba
Couriers pt freight  trucking company was hit by a  rnetts-couriers-shuts-down-
|     |     | operations for 2+  | cyber attack. In an automated  | operations-after-cyberattack/ |
| --- | --- | ------------------ | ------------------------------ | ----------------------------- |
|     |     | weeks, and laid-   | message, they informed         |                               |
https://www.illawarramercury.co
|     |     | off staff and                              | customers and employees that      | m.au/story/8601158/wollongong- |
| --- | --- | ------------------------------------------ | --------------------------------- | ------------------------------ |
|     |     | contractors; then they intended to resume  |                                   | firm-barnetts-couriers-left-   |
|     |     | bankrupted and                             | operations by April 19th, but on  | reeling-from-cyber-attack/     |

|     |     | permanently  | Monday April 22, they gave  |                                 |
| --- | --- | ------------ | --------------------------- | ------------------------------- |
|     |     | closed the   | notice of another week of   | https://bigrigs.com.au/2024/05/ |
08/illawarra-trucking-company-
|     |     | company | expected downtime. In May,  | closes-doors-after-cyber-attack/ |
| --- | --- | ------- | --------------------------- | -------------------------------- |
they announced the attack has
|     |     |     | made the business            | https://www.illawarramercury.co |
| --- | --- | --- | ---------------------------- | ------------------------------- |
|     |     |     | unprofitable, causing it to  | m.au/story/8652381/police-      |
investigating-cyber-attack-on-
permanently close after
|     |     |     | operating for 40 years. | barnetts-couriers/ |
| --- | --- | --- | ----------------------- | ------------------ |
2024-04-15 Octapharma Switzerla Pharma R BlackSuit 182 ID Shutdown 180  A ransomware attack on a  https://icsstrive.com/incident/pl
asma-donation-company-
| Group nd, USA |     | donation centers  | blood plasma processing                                 |     |
| ------------- | --- | ----------------- | ------------------------------------------------------- | --- |
|               |     | for 6 days        | company shut down operations octapharma-shuts-down-180- |     |
centers-worldwide/
at their donation centers and
may have shutdown their
https://therecord.media/plasma-
|     |     |     | European factories as a result.  | donation-company-cyberattack-  |
| --- | --- | --- | -------------------------------- | ------------------------------ |
|     |     |     | BlackSuit managed to gain        | blacksuit                      |
|     |     |     | initial access through VMWare    |                                |
|     |     |     | ESXi servers.                    | https://www.theregister.com/20 |
24/04/18/ransomware_octaphar
ma_plasma/
2024-04-16 Norrmejerier Sweden Food &  R Unknown 1 IA Shutdown  After discovering their Umeå  https://icsstrive.com/incident/pr
Bev. production 4+  plant suffered a cyberattack,  oduction-shut-down-at-swedish-
|     |     | days | they chose to shutdown all  | dairy/ |
| --- | --- | ---- | --------------------------- | ------ |
production in an abundance of
|     |     |     | caution. Because of how high  | https://www.svt.se/nyheter/lokal |
| --- | --- | --- | ----------------------------- | -------------------------------- |
t/vasterbotten/cyberangrepp-
|     |     |     | tech their industry is, nearly  | mot-norrmejerier-i-umea- |
| --- | --- | --- | ------------------------------- | ------------------------ |
|     |     |     | everything is computerized.     | produktionen-nere        |
https://www.mynewsdesk.com/s
e/norrmejerier_ek/news/norrmej
erier-har-utsatts-foer-ett-
cyberangrepp-482617
32

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2024-04-20 Puerto  Puerto  Transport R Unknown 1 U Delayed cargo  A ransomware attack on the https://icsstrive.com/incident/ranso
Nuevo  Rico movement and  main port consortium in  mware-attack-at-puerto-nuevo-
terminals-in-puerto-rico/
| Terminals  | truck dispatch  | Puerto Rico impacted  |     |
| ---------- | --------------- | --------------------- | --- |
consortium /  for several days;  operations. The FBI's office
https://www.transportation.gov/site
Luis Ayala  caused traffic  in Puerto Rico is  s/dot.gov/files/2024-07/20240711-
| Colón-Tote  | jam on Kennedy  | investigating. |     |
| ----------- | --------------- | -------------- | --- |
FINAL-
| Maritime | Ave into capital  |     | MARAD_Responses_House_CGMT_Q |
| -------- | ----------------- | --- | ---------------------------- |
|          | San Juan; caused  |     | FRs_April%2030_2024_508.pdf  |
empty shelves
|     | and shortages at  |     | https://www.elnuevodia.com/english |
| --- | ----------------- | --- | ---------------------------------- |
/news/story/fbi-assists-in-the-
|     | retail |     | investigation-on-a-cyberattack- |
| --- | ------ | --- | ------------------------------- |
against-the-company-that-operates-
cargo-docks-in-san-juan/

https://web.archive.org/web/202405
26050313/https://www.sanjuandailys
tar.com/post/union-chief-empty-
shelves-can-be-observed-following-
cyberattack-at-docks
2024-04-22 Finnair /  Estonia Transport NS Unknown  1 I3 Cancelled flights  A popular flight route  https://icsstrive.com/incident/finnair
Tartu Airport (Russia) between Helsinki  between Helsinki and Tartu  -suspends-flights-between-helsinki-
and-tartu-after-gps-jamming/
Finland and Tartu was suspended for 6 weeks
Estonia until June after widespread GPS
https://www.cbc.ca/news/world/gp
|     | 2 (6 wks.) | jamming and spoofing made s-interference-airlines-1.7213538 |     |
| --- | ---------- | ----------------------------------------------------------- | --- |
operating the route safely
impossible. After two Finnair https://www.politico.eu/article/esto
|     |     | flights in Estonia had to  | nia-blames-russia-for-gps- |
| --- | --- | -------------------------- | -------------------------- |
interference-that-forces-finnair-to-
return to Helsinki after their
|     |     | GPS stopped working, the  | suspend-flights/                    |
| --- | --- | ------------------------- | ----------------------------------- |
|     |     | route was shelved until   | https://www.reuters.com/world/euro  |
|     |     | there was a certified     | pe/finnair-pauses-flights-tartu-    |
|     |     | alternative navigation    | estonia-amid-gps-interference-2024- |
|     |     | system in place.          | 04-29/                              |
2024-04-22 Systembolag Sweden Transport R North  1 ID Impacted wine  Skanlog, Sweden's critical  https://icsstrive.com/incident/ranso
et, Skanlog Korea and spirit  distributor for government- mware-attack-on-skanlog-triggered-
|     | distribution to  | owned retail liquor stores  | nationwide-alcohol-shortage/ |
| --- | ---------------- | --------------------------- | ---------------------------- |

|     | retail stores      | Systembolaget, was hit by  |                                  |
| --- | ------------------ | -------------------------- | -------------------------------- |
|     | nation-wide for 1  | ransomware that disrupted  | https://www.euronews.com/next/20 |
24/04/25/alcohol-sales-disrupted-in-
|     | month | operations. Skanlog's CEO    | sweden-after-reported-ransomware- |
| --- | ----- | ---------------------------- | --------------------------------- |
|     |       | Mona Zuko claimed that a     | attack                            |
|     |       | North Korean ransomware      | https://therecord.media/sweden-   |
|     |       | gang was responsible. As of  | ransomware-liquor-shortage-       |
skanlog-systembolaget
May 17, System Bolaget still
reported supply issues for
https://press.systembolaget.se/pres
|     |     | wine | smeddelanden/2024/leveranser-fran- |
| --- | --- | ---- | ---------------------------------- |
drabbad-distributor-aterupptas/
2024-04-23 BECOM  Austria Discrete  R Unknown 1 IA Shut down  BECOM admitted to an  https://icsstrive.com/incident/cyber
Electronics  Mfg. production attack and were able to  attack-on-austrian-electronics-
| GmbH |     | prevent systems from being  | company-becom/ |
| ---- | --- | --------------------------- | -------------- |
encrypted, but they did so
|     |     | by isolating systems and  | https://www.meinbezirk.at/oberpulle |
| --- | --- | ------------------------- | ----------------------------------- |
ndorf/c-wirtschaft/becom-
|     |     | disconnecting from the      | electronics-wurde-ziel-eines- |
| --- | --- | --------------------------- | ----------------------------- |
|     |     | internet. This had impacts  | cyberangriffs_a6655617        |
|     |     | on production.              |                               |
https://burgenland.orf.at/stories/325
4332/

2024-04-25 Kansas City  USA Transport R Play /  1 U Disrupted "KC  On a day with many  https://icsstrive.com/incident/kansa
Highway  PlayCrypt Scout" motor  dangerous severe storms in  s-city-scout-system-systems-shut-
down/
| Traffic     | vehicle    | the forecast, critical      |     |
| ----------- | ---------- | --------------------------- | --- |
| System (KC  | emergency  | information on Kansas City  |     |
https://www.foxweather.com/weath
Scout) information and  metro area's highway traffic er-news/cyberattack-missouri-dot-
|     | alert systems for  | system KC Scout was       | highway-signs-kc-scout            |
| --- | ------------------ | ------------------------- | --------------------------------- |
|     | 6+ wks.            | disrupted by ransomware.  |  https://www.modot.org/node/49616 |
Digital road sign boards that
https://www.kctv5.com/2024/06/11/
|     |     | show real-time information,  | still-crippled-by-cyberattack-kc- |
| --- | --- | ---------------------------- | --------------------------------- |
such as emergency road
scout-test-initial-phases-restoration/
and lane closures, and road
cameras that monitor road
conditions, have faded to
black reducing motorist's
safety.
33

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack Physical
Type Consequences
2024-05-06 Port of Sao  Brazil Transport R RansomHub 1 U Shut down port  This port in Brazil suffered  https://icsstrive.com/incident/cyberat
Francisco Do Sul  for 1 day an attack that encrypted  tack-at-brazilian-port-of-sao-
francisco-do-sul/
| (Porto de São  |     |     | systems and data. To       |     |
| -------------- | --- | --- | -------------------------- | --- |
| Francisco do   |     |     | prevent the spread of the  |     |
https://portosaofrancisco.com.br/saib
| Sul) |     |     | malware, they shut down  | a-mais/id/293 |
| ---- | --- | --- | ------------------------ | ------------- |
in an abundance of
|     |     |     | caution. They restored  | https://www.halcyon.ai/attacks/ranso |
| --- | --- | --- | ----------------------- | ------------------------------------ |
|     |     |     | operations by the next  | mware-attack-on-administration-of-   |
day. RansomHub later took the-port-of-sao-francisco-do-sul
responsibility and
threatened to release
leaked data.
2024-05-06 Key Tronic  USA,  Discrete  R BlackBasta 2 $17M SEC  IA Shut down  A printed circuit board  https://isssource.com/ransomware-
Corporation  Mexico Mfg. 8K production in the  manufacturer shut down  attack-shuts-key-tronic-operations/
| (Keytronic) |     | US and Mexico  | operations after detecting  |     |
| ----------- | --- | -------------- | --------------------------- | --- |
https://therecord.media/key-tronic-
|     |     | for two weeks | unusual activity on their IT  |                                     |
| --- | --- | ------------- | ----------------------------- | ----------------------------------- |
|     |     |               | network. Later, they filed    | cyberattack-cost-17-million-sec     |
|     |     |               | $2.3m in related expenses     | https://www.techradar.com/pro/secur |
and $15m in revenue losses ity/keytronic-confirms-data-breach-
|     |     |     | with the SEC. | after-black-basta-ransomware-gang- |
| --- | --- | --- | ------------- | ---------------------------------- |
strikes-again
2024-05-11 Wehrle-Werk AG German Process  U Unknown 1 U Shut down  Cybercriminals attacked  https://icsstrive.com/incident/operati
y Mfg. production the Emmendinger plant,  ons-down-at-water-complex-waste-
water-plant-manufacturer-wehrle/
impacting production and
communications. Response
https://www.sentiguard.eu/wissen/we
|     |     |     | teams were brought in to  | hrle-werk-ag-schraenkt-nach-  |
| --- | --- | --- | ------------------------- | ----------------------------- |
|     |     |     | help with restoration.    | hackerangriff-produktion-ein/ |
2024-05-11 LEMKEN German Discrete  R 8BASE 4 IA Shut down  After detecting the attack  https://icsstrive.com/incident/german
y,  Mfg. production on all worldwide locations, -machinery-manufacturer-lemken-
halts-production-sites/
|     | Netherl |     | LEMKEN chose to protect  |     |
| --- | ------- | --- | ------------------------ | --- |
|     | ands,   |     | themselves by shutting   |     |
https://lemken.com/en-
|     | India |     | down all IT systems to  | en/news/agriculture- |
| --- | ----- | --- | ----------------------- | -------------------- |
prevent further access and news/detail/lemken-affected-by-
|     |     |     | called in a response team.  | cyberattack |
| --- | --- | --- | --------------------------- | ----------- |
On May 21, ransomware
https://www.farmersjournal.ie/machin
group 8BASE took
|     |     |     | responsibility and  | ery/news/lemken-resumes-production- |
| --- | --- | --- | ------------------- | ----------------------------------- |
after-cyberattack-822249
|     |     |     | threatened to leak data. |     |
| --- | --- | --- | ------------------------ | --- |
https://www.csoonline.com/article/34
94185/produktion-lahmgelegt-
hackerangriff-auf-lemken.html
2024-05-18 Matadero de  Spain Food &  R RansomHub 1 DO Shut down  Ransomhub claimed they  https://icsstrive.com/incident/ransom
Gijón Bev. operations and  accessed the SCADA  hub-targets-scada-system-of-spanish-
|     |     | sent workers  | system at Matadero de      | meat-processing-plant/ |
| --- | --- | ------------- | -------------------------- | ---------------------- |
|     |     | home          | Gijón, specifically their  |                        |
https://www.lne.es/gijon/2024/05/22/
|     |     |     | wastewater treatment     | matadero-paralizado-lunes-hackeo- |
| --- | --- | --- | ------------------------ | --------------------------------- |
|     |     |     | systems, which shutdown  | depuradora-102715618.html         |
the beef plant. Workers
https://cybersecuritynews.com/ranso
were sent home mid-shift.
|     |     |     | Production later resumed  | mhub-ics-attack/ |
| --- | --- | --- | ------------------------- | ---------------- |
https://cyble.com/blog/ransomware-
|     |     |     | after systems were  | menace-amplifies-for-vulnerable- |
| --- | --- | --- | ------------------- | -------------------------------- |
switched to manual
industrial-control-systems-heightened-
|     |     |     | operation. | threats-to-critical-infrastructure/ |
| --- | --- | --- | ---------- | ----------------------------------- |
2024-05-28 CDEK Russia Transport R Head Mare 1 U Disrupted  A ransomware attack on  https://icsstrive.com/incident/alleged-
|     |     | shipments and  | CDEK by Head Mare, a  | cyberattack-on-delivery-service-in- |
| --- | --- | -------------- | --------------------- | ----------------------------------- |
russia/
|     |     | deliveries for 3  | Russian-speaking   |                                  |
| --- | --- | ----------------- | ------------------ | -------------------------------- |
|     |     | days and caused   | ransomware group,  | https://therecord.media/russian- |
delivery-company-cdek-down-
|     |     | further delivery  | interrupted logistical  | cyberattack                         |
| --- | --- | ----------------- | ----------------------- | ----------------------------------- |
|     |     | delays            | services and caused     |                                     |
|     |     |                   | delivery delays by      | https://x.com/head_mare/status/1795 |
encrypting systems critical 072931489345946
to operations.
34

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor Actor Attack  | Physical  |     |     |
| --- | ------------------- | --------- | --- | --- |
Type Consequences
2024-06-04 Vietnam  Vietnam Transport R Unknown 1 IA Impacted postal  Ransomware infected systems  https://icsstrive.com/incident/ra
Post and delivery  at Vietnam Post and were  nsomware-attack-at-vietnam-
quickly detected. Systems were post-takes-systems-offline/
services for 4
|     |     | days | shutdown to contain and stop  |     |
| --- | --- | ---- | ----------------------------- | --- |
https://therecord.media/vietnam
|     |     |     | the spread of the malware,  | -claims-restore-services- |
| --- | --- | --- | --------------------------- | ------------------------- |
impacting operations, which
cyberattack
were restored days later.
https://theinvestor.vn/vietnam-
postal-services-crippled-by-
ransomware-attack-d10489.html
https://baotintuc.vn/van-de-
quan-tam/he-thong-dich-vu-buu-
dien-viet-nam-co-ban-hoat-
dong-tro-lai-sau-khi-bi-tan-cong-
mang-20240608093324588.htm
2024-06-08 Kadokawa  Japan Process  R BlackSuit 1 $3M ID Decreased  A large publisher in Japan  https://icsstrive.com/incident/cy
Corporation Mfg. production  suffered a ransomware attack  berattack-impacted-kadokawas-
|     |     | (printing), and   | that infected IT systems. This  | and-its-subsidiarys-operations/ |
| --- | --- | ----------------- | ------------------------------- | ------------------------------- |
|     |     | reduced shipping  | consequently impacted the       |                                 |
|     |     | volume down to    | physical printing and           | https://www.animenewsnetwork.   |
com/news/2024-07-
|     |     | 1/3 for 2 months | distribution of books, comics   | 30/kadokawa-gradually-        |
| --- | --- | ---------------- | ------------------------------- | ----------------------------- |
|     |     |                  | and magazines. Falling back to  | resumes-shipping-of-books-in- |
|     |     |                  | manual operations lessened,     | august/.213718                |
but did not avoid, physical
https://english.kyodonews.net/n
consequences. Kyodonews
ews/2024/12/fffebe5585f1-
|     |     |     | reported that while Kadokawa  | japanese-publisher-paid-3- |
| --- | --- | --- | ----------------------------- | -------------------------- |
paid a $3m ransom to BlackSuit million-to-hacker-group-after-
|     |     |     | in bitcoin, BlackSuit leaked  | cyberattack.html |
| --- | --- | --- | ----------------------------- | ---------------- |
|     |     |     | 1.5TB of stolen data anyways. |                  |
2024-06-08 Crown  USA Discrete  R Unknown 24 ID Shut down  Forklift manufacturer shutdown https://isssource.com/cyberatta
after a ransomware attack. The ck-halts-oh-forklift-makers-
| Equipment  | Mfg. | production and  |                                               |                                |
| ---------- | ---- | --------------- | --------------------------------------------- | ------------------------------ |
|            |      | sent workers    | TA gained initial access after an operations/ |                                |
|            |      | home for 3 wks  | employee was social                           | https://therecord.media/crown- |
engineered, allowing the TA to
equipment-shuts-down-systems-
|     |     |     | plant a RAT on their system. On  | forklifts |
| --- | --- | --- | -------------------------------- | --------- |
July 1st, Crown announced they
https://www.bleepingcomputer.c
resumed production at all 24
|     |     |     | plants. | om/news/security/crown- |
| --- | --- | --- | ------- | ----------------------- |
equipment-confirms-a-
cyberattack-disrupted-
manufacturing/
https://www.daytondailynews.co
m/local/cyberattack-
temporarily-halts-operations-at-
crown-
equipment/RIPZJ4HWKJDKJN65J
QMTGVKUTE/
2024-06-12 GlobalWafer Taiwan Discrete  U Unknown 1 IA Halted  The world's third-largest silicon  https://isssource.com/productio
s Co. / GW /  Mfg. production and  wafer maker reported that a  n-hurt-in-attack-on-silicon-
wafer-maker
| 環球晶圓 |     | disrupted        | cyberattack caused them to     |     |
| ---- | --- | ---------------- | ------------------------------ | --- |
|      |     | shipments for 6  | lower risk and "shut down its  |     |
https://www.tomshardware.com
|     |     | days | operating systems," halting  | /news/silicon-wafer-giant- |
| --- | --- | ---- | ---------------------------- | -------------------------- |
|     |     |      | production and disrupting    | globalwafers-resumes-      |
shipments. Everything was back production-days-after-hack-
|     |     |     | to normal by June 18th. NB in  | attack |
| --- | --- | --- | ------------------------------ | ------ |
March 2022, Pandora
|     |     |     | ransomware attacked  | https://focustaiwan.tw/sci- |
| --- | --- | --- | -------------------- | --------------------------- |
tech/202406170020
|     |     |     | GlobalWafers resulting in a  |     |
| --- | --- | --- | ---------------------------- | --- |
data breach.
2024-06-17 Rekah /  Israel Pharma U Unknown 1 TASE IA Halted  Rekah suffered a cyberattack  https://icsstrive.com/incident/cy
Ophir &  pharmaceutical  impacting pharmaceutical  berattack-shuts-down-
Shalpharm  distribution  distribution throughout Israel  distribution-at-israeli-pharma-
company-rekah/
| Medicines  |     | nation-wide | after several systems were    |     |
| ---------- | --- | ----------- | ----------------------------- | --- |
| and        |     |             | shutdown. Production was not  |     |
https://www.isssource.com/israe
| Cosmetics |     |     | affected. | li-pharma-firm-suffers- |
| --------- | --- | --- | --------- | ----------------------- |
cyberattack/
https://www.calcalistech.com/ct
echnews/article/sjyk8iab0
35

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor | Actor Attack  | Physical  |     |     |
| --- | ----- | ------------- | --------- | --- | --- |
Type Consequences
2024-06-26 CO-OP  Canada Transport U Unknown 380 IA Shut down  Local CO-OP retail and  https://icsstrive.com/incident/op
Cardlock  cardlock and  cardlocks (unmanned fleet- erations-disrupted-at-co-op-
gas stations  retail gas  only) gas stations shutdown  locations-in-western-canada/
| & retail food  |     |     | stations, and  | across western Canada after a  |     |
| -------------- | --- | --- | -------------- | ------------------------------ | --- |
https://www.cbc.ca/news/canad
stores  caused supply  cybersecurity incident. Also,  a/saskatchewan/federated-co-
(Federated  problems which  retail grocery locations saw  operatives-limited-cybersecurity-
Co- varied by retail  empty shelves and logistical  incident-1.7249723
| operatives  |     |     | store location,  | delivery delays. The company  |     |
| ----------- | --- | --- | ---------------- | ----------------------------- | --- |
Limited, FCL) for 3+ wks released few details, but  https://www.moosejawtoday.co
m/local-news/federated-co-
|     |     |     |     | admitted they were forced to  | operatives-limited-announces- |
| --- | --- | --- | --- | ----------------------------- | ----------------------------- |
shutdown "customer-facing
all-systems-normal-following-
|     |     |     |     | systems" at locations across  | cyberattack-9287743 |
| --- | --- | --- | --- | ----------------------------- | ------------------- |
|     |     |     |     | Western Canada.               |                     |
2024-06-30 RideMovi Italy Transport SC Ride’n Godi 1 DSC Rendered 80% of  A pirate app called Ride’n Godi  https://icsstrive.com/incident/ill
egal-app-renders-80-of-bicycles-
|     |     |     | RideMovi's bike  | allowed users to unlock bikes      |                               |
| --- | --- | --- | ---------------- | ---------------------------------- | ----------------------------- |
|     |     |     | fleet damaged,   | without needing to pay and         | out-of-use-in-bologna-italy/  |
|     |     |     | untraceable, or  | subscribe to the official service  | https://www.redhotcyber.com/p |
|     |     |     | unusable         | RideMovi, severely disrupting      |                               |
ost/bologna-gli-hacker-scrivono-
this large bike sharing service in unapp-illegale-che-paralizza-il-
|     |     |     |     | Bologna. Bikes were reported      | bike-sharing-l80-delle-biciclette- |
| --- | --- | --- | --- | --------------------------------- | ---------------------------------- |
|     |     |     |     | being left in unforeseen places,  | fuori-uso/                         |
with empty batteries, or
https://bologna.repubblica.it/cro
|     |     |     |     | physically damaged, leaving  | naca/2024/06/27/news/bologna |
| --- | --- | --- | --- | ---------------------------- | ---------------------------- |
them untraceable and
_app_pirata_bike_sharing-
|     |     |     |     | inoperable. | 423289317/ |
| --- | --- | --- | --- | ----------- | ---------- |
2024-07-02 AKG Group  Germany Discrete  U Unknown 11 IA Shut down  After discovering that  https://icsstrive.com/incident/cy
(Heat  Mfg. production for 11  operators in India could not  berattack-at-akg-group-shuts-
down-of-it-infrastructure-and-
| Exchangers) |     |     | days | login to their computers, the   |                                |
| ----------- | --- | --- | ---- | ------------------------------- | ------------------------------ |
|             |     |     |      | company discovered it was the   | restricts-production/          |
|             |     |     |      | result of an attack. After the  | https://www.hna.de/lokales/hof |
problem got worse, AKG chose
geismar/hofgeismar-
|     |     |     |     | to shutdown systems to          | ort73038/nach-cyber-angriff- |
| --- | --- | --- | --- | ------------------------------- | ---------------------------- |
|     |     |     |     | contain the attack. This        | produktion-bei-akg-laeuft-   |
|     |     |     |     | resulted in production outages  | wieder-93184688.html         |
|     |     |     |     | until July 13.                  |                              |
2024-07-08 Sibanye- USA Metals &  R RansomHo 1 ID Shut down  South-Africa based Sibanye  https://icsstrive.com/incident/si
banye-stillwater-reports-limited-
| Stillwater | Mining | use | smelter        | Stillwater suffered a    |                            |
| ---------- | ------ | --- | -------------- | ------------------------ | -------------------------- |
|            |        |     | operations in  | ransomware attack which  | disruptions-in-mining-and- |
metals-processing-operations/
|     |     |     | Columbus, OH,  | disrupted their IT systems  |     |
| --- | --- | --- | -------------- | --------------------------- | --- |
USA; halted some globally. While the company
https://www.ktvq.com/news/loc
|     |     |     | mining         | claimed only business systems    | al-news/sibanye-stillwater-hit-  |
| --- | --- | --- | -------------- | -------------------------------- | -------------------------------- |
|     |     |     | operations in  | were impacted, a union official  | by-ransomware-attack             |
|     |     |     | Montana        | said some automated systems      |                                  |
|     |     |     |                | stopped working in Ohio. Also,   | https://thecyberexpress.com/stil |
lwater-data-breach-info-of-
|     |     |     |     | their mine in Montana reported  | employees/ |
| --- | --- | --- | --- | ------------------------------- | ---------- |
an operational shutdown due to
the attack. In late July,
RansomHouse claimed
responsibility for the attack in a
large data leak.
2024-07-10 Bassett  USA Discrete  R Unknown 5 $2M SEC  ID Shut down  Due to an attack on their IT  https://icsstrive.com/incident/ra
Furniture Mfg. 8K production at all  network, some systems were  nsomware-attack-shuts-down-
|     |     |     | plants for 27     | encrypted. The company       | large-us-furniture-company/    |
| --- | --- | --- | ----------------- | ---------------------------- | ------------------------------ |
|     |     |     | days, impacting   | responded by investigating,  | https://www.retaildive.com/new |
|     |     |     | order fulfillment | isolating and shutting down  |                                |
s/bassett-furniture-cyberattack-
|     |     |     |     | some systems. As a result,  | shuts-down-manufacturing- |
| --- | --- | --- | --- | --------------------------- | ------------------------- |
|     |     |     |     | manufacturing stopped, and  | facilities/721681/        |
orders could not be fulfilled.
|     |     |     |     | Customer facing IT -assets, like  | https://www.woodworkingnetwo |
| --- | --- | --- | --- | --------------------------------- | ---------------------------- |
rk.com/news/woodworking-
ordering and retail systems,
|     |     |     |     | were not impacted. | industry-news/bassett-furniture- |
| --- | --- | --- | --- | ------------------ | -------------------------------- |
hit-cyberattack-manufacturing-
affected
https://therecord.media/furnitur
e-giant-manufacturing-shut-
down-cyberattack
36

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2024-07-15 Cadre  USA Discrete  U Unknown 1 SEC  IA Impacted  In a quarterly 10Q filling with  https://icsstrive.com/incident/sa
Holdings Inc. Mfg. 8K production and  the SEC, Cadre admitted that a  fety-equipment-giant-cadre-
holdings-shut-down-some-
|     | order fulfillment | cyber incident caused them to     |                                   |
| --- | ----------------- | --------------------------------- | --------------------------------- |
|     |                   | shutdown certain systems in an    | systems-after-cyberattack/        |
|     |                   | abundance of caution. This        | https://www.cadre-                |
|     |                   | impacted their operations,        | holdings.com/sec-filings/all-sec- |
|     |                   | incurred restoration and          | filings/content/0001558370-24-    |
|     |                   | remediation costs, and is likely  | 011750/0001558370-24-             |
011750.pdf
to negatively impact their
financial results.
https://www.securityweek.com/s
afety-equipment-giant-cadre-
holdings-hit-by-cyberattack/
2024-07-22 Split (Saint  Croatia Transport R Akira 1 ID Canceled all  Akira ransomware encrypted  https://icsstrive.com/incident/op
Jerome)  flights and  key IT systems at the airport,  erations-disrupted-at-split-
Airport diverted planes  disrupting flights. Refusing to  airport/
|     | for 2 days.                                       | negotiate, they restored a  |                                 |
| --- | ------------------------------------------------- | --------------------------- | ------------------------------- |
|     | Disrupted ground critical IT system for aircraft  |                             | https://seenews.com/news/split- |
airport-restoring-functions-after-
|     | handling and the  | handling two days later and  | cyberattack-1261006               |
| --- | ----------------- | ---------------------------- | --------------------------------- |
|     | passenger         | resumed operations.          |                                   |
|     | information       |                              | https://glashrvatske.hrt.hr/en/do |
|     | system, and       |                              | mestic/split-airport-after-the-   |
hacker-attack-we-will-not-
forced airport to
|     | operate manually  |     | negotiate-11673909 |
| --- | ----------------- | --- | ------------------ |

|     | for days |     | https://n1info.hr/english/news/s |
| --- | -------- | --- | -------------------------------- |
plit-airport-key-it-system-
restored-after-cyber-attack/
2024-08-17 Microchip  USA Discrete  R Play /  2 SEC  IA Disrupted  In an SEC filing, Microchip said  https://icsstrive.com/incident/mi
Technology Mfg. PlayCrypt 8K operations at  that a cyber incident impacted  crochip-technology-
production and order fulfilment, manufacturing-operations-
multiple sites,
|     | reduced         | causing them to isolate         | disrupted-after-cyberattack/      |
| --- | --------------- | ------------------------------- | --------------------------------- |
|     | production      | systems and shut down some      | https://www.isssource.com/prod    |
|     | output, and     | services. On August 24th, Play  | uction-hurt-in-attack-on-silicon- |
|     | impacted order  | claimed responsibility for the  | wafer-maker                       |
|     | fulfilment      | attack on their dark web leak   |                                   |
https://www.bleepingcomputer.c
site and threatened to publish
|     |     | stolen data. | om/news/security/microchip- |
| --- | --- | ------------ | --------------------------- |
technology-discloses-
cyberattack-impacting-
operations/
https://www.reuters.com/techno
logy/microchip-technologys-
certain-operations-disrupted-by-
cyber-incident-2024-08-20/
2024-08-19 BVI  British  Power R Unknown 1 ID Prolonged power  While recovering from Hurricane https://icsstrive.com/incident/op
Electricity  Virgin  distribution  Ernesto, BVIEC has been  erations-disrupted-at-bvi-
electricity-corporation-bviec/
Corporation  Islands outage for 10+  working hard to restore power
| (BVIEC) | days | infrastructure for a week when  |     |
| ------- | ---- | ------------------------------- | --- |
https://www.virginislandsnewson
|     |     | they were suddenly hit by a  | line.com/en/news/bviec-falls- |
| --- | --- | ---------------------------- | ----------------------------- |
ransomware attack that made
victim-to-cyber-attack
restoration much more difficult.
|     |     | The attack hit both "internal  | https://bvinews.com/bviec-  |
| --- | --- | ------------------------------ | --------------------------- |
|     |     | and external operations,"      | warns-residents-check-your- |
|     |     | meaning both IT and OT         | credit-cards/               |
|     |     | networks. A large customer     | https://bvinews.com/bviecs- |
data breach followed.
online-payment-platform-
restored-after-cyber-attack/
2024-08-24 Seattle- USA Transport R Rhysida 1 IA Delayed Flights  After discovering a breach in  https://icsstrive.com/incident/cy
Tacoma Int’l  and shutdown or  their computer systems, and  berattack-disrupts-seattle-
airport-for-days-affecting-labor-
| Airport  | impaired the  | noticing some systems being  |     |
| -------- | ------------- | ---------------------------- | --- |
(SeaTac) /  baggage  encrypted, The Port of Seattle  day-weekend-rush

Port of  handling system  began disconnecting systems  https://www.theregister.com/20
| Seattle | (BHS), check-in  | from the internet. This  |     |
| ------- | ---------------- | ------------------------ | --- |
24/08/26/seattle_airport_cyber
|     | kiosks, and       | impacted passenger services at attack |                                  |
| --- | ----------------- | ------------------------------------- | -------------------------------- |
|     | passenger flight  | logistics at both the airport and     |                                  |
|     | information       | seaport.                              | https://therecord.media/seattle- |
|     | display system    |                                       | port-rhysida-ransom-refused      |
|     | (FIDS) for weeks  |                                       | https://www.portseattle.org/ne   |
ws/port-cyberattack-archive
37

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2024-08-27 JAS  Italy, USA Transport R Unknown 1 U Disrupted or  After a ransomware attack,  https://icsstrive.com/incident/global
Worldwide delayed freight  operations were impacted  -freight-forwarder-jas-confirms-
malware-disrupts-operations/
| and logistics  | at one of the largest Int’l  |     |
| -------------- | ---------------------------- | --- |
| forwarding     | freighter forwarders. Post-  |     |
https://theloadstar.com/jas-
|     | incident, JAS reported that  | forwarding-recovers-from-cyber- |
| --- | ---------------------------- | ------------------------------- |
backlogged requests were
attack-but-saw-many-stolen-
|     | being worked through,  | credentials/ |
| --- | ---------------------- | ------------ |
implying there were some
https://www.freightwaves.com/news
delays.
/global-freight-forwarder-confirms-
malware-attack-for-technical-
disruptions
https://www.freightcaviar.com/jas-
worldwide-confirms-malware-attack-
cause-of-technical-disruptions/
2024-08-30 Ekomobil Turkey Transport H Cund El  1 IA Disrupted public  A hacktivist group sent  https://icsstrive.com/incident/bus-
Aksa bus services in  threatening messages to  services-disrupted-after-turkish-
| the city of  | municipal bus commuters    | transportation-app-hack/            |
| ------------ | -------------------------- | ----------------------------------- |
| Kocaeli      | by hijacking the Ekomobil  |                                     |
|              | smart-phone app and        | https://www.turkiyetoday.com/turkiy |
e/anti-semitic-group-hacks-turkish-
|     | displaying threatening  | transportation-app-46954/ |
| --- | ----------------------- | ------------------------- |
messages. Also, bus card
|     | readers' displays were    | https://www.cagdaskocaeli.com.tr/h |
| --- | ------------------------- | ---------------------------------- |
|     | compromised to display a  | aber/21477453/e-komobil-hacklendi  |
bomb threat. As a
precaution, all bus services
in the city were temporarily
halted.
2024-09-03 Elektroskand Sweden Transport R BlackSuit 1 100M  ID Halted logistical  IT systems at  https://icsstrive.com/incident/large-
ia Sverige AB kr. operations for 2+  Elektroskandia's large  swedish-electrical-wholesalers-
elektroskandia-loses-millions/
| wks | central warehouse in  |     |
| --- | --------------------- | --- |
Örebro were shutdown in a
https://info.elektroskandia.se/underh
|     | ransomware attack. This   | all/                                 |
| --- | ------------------------- | ------------------------------------ |
|     | impacted logistical       |                                      |
|     | operations and prevented  | https://www.elinstallatoren.se/2024/ |
|     | the company from picking  | 10/elektroskandiachefen-om-          |
hackerattacken-vi-sa-till-vara-
or delivery orders.
kunder-att-ga-till-konkurrenterna/
2024-09-12 KANTSU (関 Japan Transport R Unknown 1 U Halted and  Kantsu reported that  https://icsstrive.com/incident/cybera
通) delayed logistical ransomware was detected  ttack-at-japanese-logistics-
company-kantsu/
| operations for 1  | on their server which    |     |
| ----------------- | ------------------------ | --- |
| month             | caused a system outage,  |     |
https://www.kantsu.com/news/6573/
|     | impacting multiple systems  |     |
| --- | --------------------------- | --- |
related to the custody of
https://www.kantsu.com/news/6615/
|     | customer items in their  |                                  |
| --- | ------------------------ | -------------------------------- |
|     | logistical system. The   | https://www.kantsu.com/news/6620 |
attack originated externally /
and pivoted into their IT and
OT networks and delayed
the storage and retrieval of
warehoused items.  Full
operations were restored a
month later on October
12th.
2024-09-14 ZACROS (藤 Japan Discrete  R Argonauts  1 PIPC ID Impacted  A leading Japanese  https://icsstrive.com/incident/japane
森工業株式会 Mfg. Group production and  manufacturer of packaging  se-manufacturer-zarcos-hit-by-
ransomware-attack/
社) delivery  materials suffered a  https://securityonline.info/zacros-
| operations | ransomware attack that  |     |
| ---------- | ----------------------- | --- |
corporation-discloses-personal-
|     | affected servers critical to  | information-leak-following- |
| --- | ----------------------------- | --------------------------- |
|     | ERP and production            | ransomware-attack/          |
management. A data
|     | breach resulted, which was  | https://www.cyjax.com/resources/bl |
| --- | --------------------------- | ---------------------------------- |
og/new-argonauts-extortion-group-
reported to Japan’s' PIPC,
|     | and acknowledged an  | emerges/                         |
| --- | -------------------- | -------------------------------- |
|     | impact on financial  | https://cybersecurity-           |
|     | performance. The     | info.com/news/zacros-ransomware/ |
Argonauts ransomware
group claimed responsibility
and said they leaked data
over ZACROS' refusal to pay
a ransom.
38

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor | Actor Attack  | Physical  |     |     |
| ----- | ------------- | --------- | --- | --- |
Type Consequences
2024-09-22 Schumag AG Germany Discrete  U Unknown 1 Bankrupt U Shut down  A precision engineering and  https://icsstrive.com/incident/germ
Mfg. production, and  tooling company filed for  an-steel-manufacturer-shuts-down-
|     |     | filed for     | bankruptcy and self-directed   | systems-and-cancels-annual-       |
| --- | --- | ------------- | ------------------------------ | --------------------------------- |
|     |     | bankruptcy &  | restructuring in mid October,  | shareholder-meeting/              |
|     |     | restructuring | after a cyberattack a month    | https://www.csoonline.com/article |
|     |     |               | prior caused production        | /3559206/schumag-von-             |
|     |     |               | outages. The threat actor      | cyberattacke-betroffen.html       |
was not identified.
https://www.boerse-
frankfurt.de/nachrichten/Schumag-
Aktiengesellschaft-Cyberangriff-
Absage-der-fuer-den-25-
September-2024-einberufenen-
ordentlichen-Hauptversammlung-
63c6812b-71f9-4407-b14a-
589dc8f3ab55
2024-09-27 Smeg Italy Discrete  U Unknown 1 IA Shut down  High-End home appliances  https://icsstrive.com/incident/prod
Mfg. production due  maker Smeg proactively  uction-at-standstill-at-italian-high-
end-home-appliances-
|     |     | to dependencies  | halted production after a                                       | manufacturer/                 |
| --- | --- | ---------------- | --------------------------------------------------------------- | ----------------------------- |
|     |     | on their SAP     | cyber attack, saying it was                                     |                               |
|     |     | system, and      | forced to suspend operations https://cyberinsider.com/high-end- |                               |
|     |     | furloughed       | as its SAP system was                                           | appliances-maker-smeg-halts-  |
|     |     | hundreds of      | interrupted, which then went                                    | production-after-cyberattack/ |
|     |     | employees        | on to impact logistics.                                         |                               |
https://www.wired.it/article/cybera
ttacco-smeg-elettrodomestici/
2024-09-28 Beirut (Rafik- Lebanon Transport NS Israel  1 DO Diverted civilian  After learning that an Iranian  https://icsstrive.com/incident/israe
Hariri) Int’l  Defense  plane Qasem Air  plane was due to land at the  l-hacks-beirut-airport-control-
tower/
| Airport | Force  | Flight No.                           | airport, Israel's IDF breached  |     |
| ------- | ------ | ------------------------------------ | ------------------------------- | --- |
|         | [IDF]  | QFZ9964 back to the control tower's  |                                 |     |
https://www.jpost.com/middle-
(Israel) its origin of  communication network in a  east/article-822208
|     |     | Tehran, Iran | cyber attack and warned  |     |
| --- | --- | ------------ | ------------------------ | --- |
operators not to allow the
plane to land. Otherwise,
they would launch an attack
on the airport. Lebanon's
transport minister, Ali Hamieh
intervened and directed the
incoming plane to divert its
flight path and return to Iran.
2024-10-05 Casio Japan Discrete  R Undergrou 1 IA Halted  After a ransomware attack  https://icsstrive.com/incident/japa
Mfg. nd manufacturing,  on this Japan-based  nese-technology-giant-casio-
|     |     | suspended repair watchmaker both production  |                               | computer-confirmed-cyberattack/ |
| --- | --- | -------------------------------------------- | ----------------------------- | ------------------------------- |
|     |     | services, and                                | and repair services were      |                                 |
|     |     | delayed product                              | impacted. In response, Casio  | https://therecord.media/japan-  |
casio-delays-watchmaker-
|     |     | delivery inside   | took servers offline which      | ransomware                        |
| --- | --- | ----------------- | ------------------------------- | --------------------------------- |
|     |     | Japan for over a  | affected receiving and          |                                   |
|     |     | month             | placing orders with suppliers,  | https://techcrunch.com/2024/10/17 |
/casio-says-no-prospect-of-
|     |     |     | and the scheduling of  | recovery-yet-after-ransomware- |
| --- | --- | --- | ---------------------- | ------------------------------ |
product shipments.
attack/
2024-10-11 Hubergroup Germany Discrete  U Unknown 1 U Limited  The Celle manufacturing  https://icsstrive.com/incident/cybe
Mfg. production for 2+ plant suffered a cyber attack rattack-at-german-printing-ink-
that had impacts on their SAP manufacturer-hubergroup/
weeks, delayed
|     |     | delivery | system, internet connectivity,  |     |
| --- | --- | -------- | ------------------------------- | --- |
https://www.celleheute.de/post/cy
|     |     |     | production, and delivery for    | berangriff-auf-hubergroup- |
| --- | --- | --- | ------------------------------- | -------------------------- |
|     |     |     | weeks. The company said         | regionale-it-systeme-      |
|     |     |     | other Int’l locations have not  | beeintr%C3%A4chtigt/       |
|     |     |     | been impacted.                  |                            |
2024-10-19 CERP Bretagne France Pharma R Hunters  1800 ID Shut down  Due to a cyber attack, this  https://icsstrive.com/incident/frenc
Atlantique Int’l distribution and  key pharma wholesaler and  h-pharmacy-wholesaler-hit-by-
|     |     | delayed orders 1  | distributor suffered a 24-hour cyberattack/ |                                   |
| --- | --- | ----------------- | ------------------------------------------- | --------------------------------- |
|     |     | day               | outage before resuming                      | https://www.letelegramme.fr/cotes |
orders and deliveries to
-d-armor/saint-brieuc-
|     |     |     | pharmacies across Western  | 22000/victime-dune-cyberattaque- |
| --- | --- | --- | -------------------------- | -------------------------------- |
|     |     |     | France.                    | le-grossiste-en-pharmacie-cerp-  |
devrait-rapidement-retrouver-une-
activite-normale-6686412.php
https://www.zdnet.fr/actualites/ap
res-la-cyberattaque-la-
reconstruction-pas-a-pas-du-
grossiste-en-pharmacie-cerp-
bretagne-atlantique-400030.htm
39

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor Actor Attack  | Physical  |     |     |
| --- | ------------------- | --------- | --- | --- |
Type Consequences
2024-10-28 AEP GmbH Germany Pharma R Unknown 6000 ID Disrupted  After the company's own  https://icsstrive.com/incident/ranso
|     |     | pharmaceutical     | systems detected a breach,   | mware-attack-threatens-disrupting- |
| --- | --- | ------------------ | ---------------------------- | ---------------------------------- |
|     |     | distribution and   | some systems were            | medicine-supply-to-pharmacies-in-  |
|     |     | order fulfillment  | encrypted before they pre-   | germany/                           |
|     |     | to 6,000           | emptively "disconnected all  | https://therecord.media/ransomwar  |
|     |     | pharmacies         | external connections and     | e-attack-hits-german-              |
|     |     | across Germany     | shut down all affected IT    | pharmaceutical-wholesaler-         |
disruptions
|     |     | for 9 days. | systems". Services were  |     |
| --- | --- | ----------- | ------------------------ | --- |
restored Nov. 6th.
https://www.pharmazeutische-
zeitung.de/massiver-cyberangriff-
auf-aep-151028/
https://www.br.de/nachrichten/bay
ern/cyberattacke-auf-
pharmagrosshaendler-
lieferprobleme-fuer-
apotheken,UShteGL
2024-10-31 Microlise  UK Transport R SafePay /  3 LSE I3 Disrupted  Microlise, a software  https://icsstrive.com/incident/tracki
ng-in-prison-vans-and-courier-
Group plc  LockBit tracking services company that DHL relies on
(DHL, Serco,  at DHL, globally,  for its global delivery  vehicles-affected-by-microlise-
cyberattack/
| NISA) |     | thereby         | tracking operations, was hit  |     |
| ----- | --- | --------------- | ----------------------------- | --- |
|       |     | impacting NISA  | by a ransomware attack.       |     |
https://www.betterretailing.com/dhl
|     |     | and other                | This impacted Nisa's              | -cyber-attack/                    |
| --- | --- | ------------------------ | --------------------------------- | --------------------------------- |
|     |     | logistical               | logistics which relies, in turn,  |                                   |
|     |     | operations, some on DHL. |                                   | https://www.securityweek.com/micr |
|     |     | customer                 |                                   | olise-confirms-data-breach-as-    |
ransomware-group-steps-forward/
companies
reported
https://motortransport.co.uk/cybera
|     |     | logistiical delays |     | ttack-on-microlise-hits-operators- |
| --- | --- | ------------------ | --- | ---------------------------------- |
triggering-call-for-stronger-
continuity-plans/24912.article
2024-11-08 Ahold Delhaize USA Transport U Unknown 2040 IA Impacted and  Delhaize's US operations  https://icsstrive.com/incident/opera
(Stop & Shop,  delayed food  were impacted after a  tions-disrupted-at-us-branch-of-
Food Lion,  and  cyberattack on their IT  grocery-giant-ahold-delhaize/
| Hannaford,  |     | pharmaceutical  | systems. Security experts  |     |
| ----------- | --- | --------------- | -------------------------- | --- |
Giant Food,  distribution to  were brought in that  https://cybernews.com/news/ahold-
delhaize-cyberattack-stop-shop-
Giant  stores and online recommended isolating and  hannaford-food-lion-impacted-/
| Company) |     | customers for  | taking systems offline. The  |                                    |
| -------- | --- | -------------- | ---------------------------- | ---------------------------------- |
|          |     | 12+ days. A    | incident and subsequent      | https://www.theregister.com/2024/1 |
response impacted logistical 1/12/ahold_delhaize_cybersecurity_i
|     |     | dozen New                 |                             | ssue_blamed/                       |
| --- | --- | ------------------------- | --------------------------- | ---------------------------------- |
|     |     | England                   | operations. Delhaize        |                                    |
|     |     | locations report          | released very few incident  | https://www.msn.com/en-            |
|     |     | bare shelves and details. |                             | us/money/companies/inventory-at-   |
|     |     | shortages.                |                             | worcester-area-stop-shops-remains- |
limited-after-cyberattack/ar-
AA1urPDb
2024-11-14 Vossko Germany Food &  R BlackBasta 1 ID Shut down  This food processing  https://icsstrive.com/incident/cyber
attack-on-vossko-food-company-in-
|     | Bev. | production for 8  | company suffered a      |          |
| --- | ---- | ----------------- | ----------------------- | -------- |
|     |      | days.             | ransomware attack that  | germany/ |

|     |     |     | shutdown production after  | https://www.vossko.de/2024/11/22/ |
| --- | --- | --- | -------------------------- | --------------------------------- |
first encrypting IT systems
cyberangriff-bei-vossko-systeme-
|     |     |     | including databases. After  | und-produktion-wiederhergestellt/ |
| --- | --- | --- | --------------------------- | --------------------------------- |
bringing in external response
https://www.comparitech.com/new
team specialists including
|     |     |     | law enforcement, their  | s/ransomware-gang-says-its- |
| --- | --- | --- | ----------------------- | --------------------------- |
responsible-for-data-breach-at-
|     |     |     | systems were restored and  | pennsylvania-food-producer/ |
| --- | --- | --- | -------------------------- | --------------------------- |
rebuilt to strengthen them

against future attacks. In
December, BlackBasta took
responsibility for the attack
in a data breach.
2024-11-18 Henley  UK Process  U Unknown 1 U Shut down  A cyber attack impacted the https://icsstrive.com/incident/local-
Standard,  Mfg. production  publisher's production and IT uk-newspaper-production-shut-
Higgs Group (printing),  systems, preventing the  down-after-cyberattack/
|     |     | delayed       | distribution of one weekly  | https://www.henleystandard.co.uk/n |
| --- | --- | ------------- | --------------------------- | ---------------------------------- |
|     |     | publishing &  | edition of their newspaper  |                                    |
ews/home/193821/this-week-s-
|     |     | distribution 4  | on time. They hoped to      | paper-delayed.html |
| --- | --- | --------------- | --------------------------- | ------------------ |
|     |     | days            | produce and distribute it,  |                    |
late, on Thursday, the 21st.
40

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2024-11-21 Morrisons,  UK, USA Transport R Termite/Bab 3 I3 Impacted  A supply chain ransomware  https://icsstrive.com/incident/big-
Sainsbury's,  uk multiple Blue  attack on MSP provider Blue  ripple-effects-after-supply-chain-
software-supplier-blue-yonder-
| BIC  |     | Yonder  | Yonder impacted multiple  |     |
| ---- | --- | ------- | ------------------------- | --- |
(Panasonic  customers'  customers including BIC, the  cyberattack/
https://therecord.media/starbucks-
Blue Yonder) logistical  pen manufacturer, who  bic-morrisons-blue-yonder-supply-
operations for 3+ experienced shipping delays. chain-attack-ransomware
|     |     | weeks | Sainsbury's and Morrisons   |                                   |
| --- | --- | ----- | --------------------------- | --------------------------------- |
|     |     |       | stated the attack impacted  | https://www.securityweek.com/star |
|     |     |       | warehouse management        | bucks-grocery-stores-hit-by-blue- |
|     |     |       | systems.                    | yonder-ransomware-attack/         |
https://therecord.media/blue-
yonder-cyberattack-customer-
systems-returning
2024-11-21 Artivion USA Discrete  R Unknown 1 SEC  IA Disrupted order  A ransomware attack  https://icsstrive.com/incident/medic
Mfg. 8K fulfillment impacted operations and  al-device-maker-artivion-hit-in-
ransomware-attack/
forced the medical device
|     |     |     | manufacturer to take some  | https://therecord.media/artivion- |
| --- | --- | --- | -------------------------- | --------------------------------- |
medical-device-company-
|     |     |     | systems offline in response. | cyberattack-notice-sec |
| --- | --- | --- | ---------------------------- | ---------------------- |
https://thecyberexpress.com/artivio
n-cyberattack/

2024-12-16 LKQ  Canada,  Discrete  U Unknown 1 SEC  U Impacted  LKQ, an aftermarket auto  https://icsstrive.com/incident/auto-
Corporation  USA Mfg. 8K operations "for a parts manufacturer, made  parts-company-lkq-hit-in-
cyberattack-halts-operations/
| (Keystone, Tri  |     | few weeks" | an SEC 8K filing reporting    |     |
| --------------- | --- | ---------- | ----------------------------- | --- |
| Star, ADL)      |     |            | their Canadian business unit  |     |
https://www.securityweek.com/maj
|     |     |     | fell victim to unauthorized  | or-auto-parts-firm-lkq-hit-by- |
| --- | --- | --- | ---------------------------- | ------------------------------ |
|     |     |     | access, impacting            | cyberattack/                   |
operations. On the date of
|     |     |     | their filing, they reported  | https://www.isssource.com/cyberat |
| --- | --- | --- | ---------------------------- | --------------------------------- |
having resumed operating at tack-halts-operations-at-auto-
parts-maker-lkq/
near full capacity.
2024-12-19 Pittsburg  USA Transport R Unknown 1 U Disrupted rail  A ransomware attack  https://icsstrive.com/incident/ranso
disrupted light passenger rail mware-attack-at-pittsburgh-
| Regional  |     | services  |     |     |
| --------- | --- | --------- | --- | --- |
Transit (PRT) temporarily;  train operations on Thursday regional-transit/
|     |     | delayed trains  | morning and launched an     | https://therecord.media/pittsburgh- |
| --- | --- | --------------- | --------------------------- | ----------------------------------- |
|     |     | 20+ mins        | investigation. On Jan. 7th  |                                     |
regional-transit-attributes-
2025, they announced a data disruptions-to-ransomware-attack
breach had occurred but
|     |     |     | have not named those       | https://www.wpxi.com/news/local/i   |
| --- | --- | --- | -------------------------- | ----------------------------------- |
|     |     |     | responsible or given more  | nternet-outage-that-delayed-t-rail- |
cars-was-result-ransomware-
|     |     |     | details. | attack-prt- |
| --- | --- | --- | -------- | ----------- |
says/4YCKQXPINJBQRB765RWXZZG
CTY/
https://www.trains.com/trn/news-
reviews/news-wire/pittsburgh-
transit-agency-victim-of-
ransomware-attack/
2024-12-25 Azerbaijan  Azerbaija Transport NS Russia 1 DO Disabled GPS  En route to destination  https://icsstrive.com/incident/azerb
aijani-jet-confused-for-ukrainian-
Airlines Flight  n,  navigation and  Grozny, an Embraer 190 lost
| J2-8243 | Chechny | ADS-B  | both GPS navigation and  | drone/ |
| ------- | ------- | ------ | ------------------------ | ------ |

a  transponder;  their ADS-B transponder. This  https://www.cnn.com/2024/12/26/a
|     | (Russia) | contributed to a  | was deliberate, as Russian  |     |
| --- | -------- | ----------------- | --------------------------- | --- |
sia/kazakhstan-plane-crash-
|     |     | crash; killed 38  | forces jammed GPS over      | questions-intl/index.html |
| --- | --- | ----------------- | --------------------------- | ------------------------- |
|     |     | passengers        | Grozny while defending the  |                           |
https://www.iata.org/en/pressroom
city against possible
|     |     |     | Ukrainian drone attacks, but  | /2024-releases/2024-12-29-01/        |
| --- | --- | --- | ----------------------------- | ------------------------------------ |
|     |     |     | they had not yet closed the   | https://en.wikipedia.org/wiki/Azerba |
airspace to civilian flights.
ijan_Airlines_Flight_8243
The aircraft contacted ATC
and attempted landing twice
but without GPS. Heavy fog
caused ATC to order them to
abort and return to Baku.
Minutes later, the Embraer
was hit by Russian anti-
aircraft fire and lost controls
ultimately crashing near
Aktau while attempting an
emergency landing.
41

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor Actor Attack  | Physical  |     |     |
| --- | ------------------- | --------- | --- | --- |
Type Consequences
2024-12-26 Japan Airlines  Japan Transport U Unknown 74 ID Canceled 4  A cyberattack impacted  https://icsstrive.com/incident/d
dos-attack-delays-flights-at-
| (JAL) |     | domestic flights,                               | systems by overwhelming them     |                                 |
| ----- | --- | ----------------------------------------------- | -------------------------------- | ------------------------------- |
|       |     | delayed 70                                      | with network requests during     | japan-airlines/                 |
|       |     | domestic and                                    | the busy year-end travel         | https://english.kyodonews.net/n |
|       |     | Int’l flights up to                             | season. This caused the airline  | ews/2024/12/33b9ee9a0030-       |
|       |     | 4 hours, and                                    | to temporarily halt operations   | urgent-jals-system-under-       |
|       |     | suspended ticket because internal and external  |                                  | cyberattack-domestic-and-intl-  |
flights-delayed.html
|     |     | sales for several  | systems began malfunctioning,  |     |
| --- | --- | ------------------ | ------------------------------ | --- |
|     |     | hours              | including baggage handling     |     |
https://www.securityweek.com/j
|     |     |     | systems (BHS). JAL said system  | apan-airlines-was-hit-by-a- |
| --- | --- | --- | ------------------------------- | --------------------------- |
outages totaled 6 hours.
cyberattack-delaying-flights-
during-the-year-end-holiday-
season/
https://www.japantimes.co.jp/n
ews/2024/12/26/japan/jal-
cyberattack/
2024-12-29 Peikko Group  Finland Discrete  R Akira 12 ID Halted  An attack on a manufacturer of  https://icsstrive.com/incident/cy
berattack-impacts-operations-
| Corp. | Mfg. | manufacturing    | pre-cast and in-cast concrete    |                                 |
| ----- | ---- | ---------------- | -------------------------------- | ------------------------------- |
|       |      | and deliveries,  | floor structures impacted their  | at-finnish-manufacturer-peikko- |
group/
|     |     | with some   | Microsoft D365 ERP systems  |     |
| --- | --- | ----------- | --------------------------- | --- |
|     |     | countries'  | and Telka 3D structural     |     |
https://www.isssource.com/atta
|     |     | operations        | modelling software. In turn, this  | ck-slows-manufacturing-for-   |
| --- | --- | ----------------- | ---------------------------------- | ----------------------------- |
|     |     | operating         | impacted manufacturing and         | finlands-peikko-group/        |
|     |     | manually, for 12  | customer deliveries for days. On   |                               |
|     |     | days              | January 13, the Akira              | https://www.peikko.com/news/p |
eikko-encounters-a-cyber-
|     |     |     | ransomware group took  | attack/ |
| --- | --- | --- | ---------------------- | ------- |
responsibility for the attack in a
|     |     |     | data breach. | https://www.breachsense.com/ |
| --- | --- | --- | ------------ | ---------------------------- |
breaches/peikko-data-breach/
42

Incidents in 2023
Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2023-01-09 VDM  Germany Process  U Unknown 4 U Production  Attack crippled operations https://icsstrive.com/incident/cyberatt
Metals Mfg. halted; workers  for weeks, requiring all on- ack-affects-all-locations-of-german-
|     | sent home 3 wks. | premises and virtual IT   | vdm-steel/ |
| --- | ---------------- | ------------------------- | ---------- |
|     |                  | systems to be rebuild or  |            |
https://come-
|     |     | replaced. Specialty ZAC  | on.de/lennetal/werdohl/vdm-kaempft- |
| --- | --- | ------------------------ | ----------------------------------- |
|     |     | (cybercrime) police in   | sich-zurueck-92061669.html          |
NRW investigate.
https://hellwegeranzeiger.de/unna/ha
cker-vdm-metals-lohnabschlag-
cyberangriff-w687619-1000725900/
https://come-
on.de/lennetal/werdohl/cyberangriff-
auf-vdm-metals-92030607.html
2023-01-10 UK Postal  UK Transport R LockBit 3.0 11500 £42M ID Disabled label  After a LockBit  https://icsstrive.com/incident/ransom
Service  printers; prevents ransomware attack,  ware-attack-at-royal-mail-disrupts-
(Royal  sending Int’l  custom label printers and  international-operations-more-than-a-
| Mail) | letters or parcels systems were disabled  |     | month/ |
| ----- | ----------------------------------------- | --- | ------ |

|     | for 6 wks. | and hijacked to print      | https://www.telegraph.co.uk/business/ |
| --- | ---------- | -------------------------- | ------------------------------------- |
|     |            | ransom notes, halting all  | 2023/01/12/russia-linked-hackers-     |
|     |            | mail export services       | behind-royal-mail-cyber-attack/       |
nation-wide.
https://bankinfosecurity.com/royal-
mail-refused-absurd-lockbit-extortion-
demand-a-21214

https://theguardian.com/business/202
3/feb/21/royal-mail-international-
deliveries-cyber-attack-ransom-strikes
2023-01-11 Morgan  UK Discrete  U Unknown 2 £8M LSE U Halted  Production and shipping  https://icsstrive.com/incident/uk-
Advanced  Mfg. production and  were affected at multiple  manufacturer-morgan-advanced-
Materials shipping sites following a  materials-hit-in-cyberattack/
|     |     | cyberattack. | https://therecord.media/morgan- |
| --- | --- | ------------ | ------------------------------- |
advanced-materials-cyberattack-
shares-drop
https://therecord.media/british-
company-that-helps-make-
semiconductors-hit-by-cyber-incident
https://cybernews.com/news/morgan-
advanced-materials-cyberattack/
2023-01-13 Super  Portugal Food &  U Unknown 1 U Impaired  Portugal's largest brewer  https://icsstrive.com/incident/cyberatt
Bock  Bev. operations,  gave notice that a  ack-at-super-bock-brewery-affects-
| Group | product supply,  | cyberattack has impaired  | operations/ |
| ----- | ---------------- | ------------------------- | ----------- |

|     | and delivery | operations, causing "major  | https://theportugalnews.com/news/20 |
| --- | ------------ | --------------------------- | ----------------------------------- |
restrictions in its supply
23-01-31/restrictions-with-super-bock-
|     |     | chain." | after-cyber-attack/74342 |
| --- | --- | ------- | ------------------------ |

https://theregister.com/2023/02/02/su
per_bock_cyberattack/?utm_source=t
witter&utm_medium=twitter&utm_cam
paign=auto&utm_content=article
https://linkedin.com/posts/superbockg
roup_superbockgroup-activity-
7025903123470725122-ZHY2/
2023-01-17 Exco Tech Canada Discrete  R LockBit 3.0 3 IA Shutdown  An attack on three plants  https://icsstrive.com/incident/producti
Mfg. production at 3  in Exco's large mould  on-at-canadian-tool-manufacturer-
exco-technologies-interrupted/
|     | plants for 2  | group, prompting a pre- |     |
| --- | ------------- | ----------------------- | --- |
|     | weeks         | emptive shutdown to     |     |
https://insurancebusinessmag.com/ca
|     |     | contain the incident.  | /news/cyber/canadian-manufacturer- |
| --- | --- | ---------------------- | ---------------------------------- |
|     |     | LockBit claimed        | takes-debilitating-cyber-hit-      |
|     |     | responsibility.        | 434108.aspx                        |

https://excocorp.com/2023/01/23/exc
o-technologies-limited-announces-
cyber-security-incident/
https://itworldcanada.com/article/can
adian-tool-manufacturer-hit-by-cyber-
attack/523620
43

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2023-01-17 Fritzmeier  Germany Discrete  U Unknown 15 U Halted  A criminal  https://icsstrive.com/incident/operations-
Gruppe &  Mfg. production for 7  investigation is  paralyzed-across-all-locations-of-german-
automotive-supplier-fritzmeier-gruppe/
| M1        | days & took 4  | ongoing into a       |     |
| --------- | -------------- | -------------------- | --- |
| Sporttech | wks. for full  | cyberattack at this  |     |
https://merkur.de/lokales/muenchen-
nik restoration auto, truck and bike  lk/aying-ort28266/fritzmeier-hacker-angriff-
manufacturer that
internet-telefon-aying-firma-cybercrime-
halted production and 92037641.html
took weeks to return
https://merkur.de/lokales/muenchen-
to normal levels.
lk/hackerangriff-auf-fritzmeier-group-noch-
keine-spur-zu-den-erpressern-92105466.html
https://radmarkt.de/update-fritzmeier-
group-cyber-attacke-m1-produktion-laeuft-
wieder/
2023-01-18 Benetton  Italy Transport U Unknown 1 ID Delayed and  An attack impaired  https://icsstrive.com/incident/operations-
disrupted-at-italian-clothing-giant-
| Group    | impaired product Benetton's main  |                       |           |
| -------- | --------------------------------- | --------------------- | --------- |
| (United  | shipments and                     | logistical centre in  | benetton/ |
Colors of  orders for 4 days, Castrette di Villorba,  https://thecyberexpress.com/italian-
| Benetton) | and furloughed  | where it ships  |     |
| --------- | --------------- | --------------- | --- |
clothing-giant-benetton-cyber-attack/
|     | employees | products to over 5K     |                                            |
| --- | --------- | ----------------------- | ------------------------------------------ |
|     |           | global outlets, and is  | https://trevisotoday.it/economia/benetton- |
attacco-hacker-22-gennaio-2023.html
fundamental to its
business.
2023-01-29 Tribhuvan  Nepal Transport U Unknown 1 ID Delayed Int’l  A DDoS attack on  https://icsstrive.com/incident/weekend-
(Kathman arrival and  Nepal's Government  ddos-attack-on-400-nepal-government-
du) Int’l  departure flights  Integrated Data  sites-airport-most-affected/

| Airport | for 3 hours | Centre took down       |                                      |
| ------- | ----------- | ---------------------- | ------------------------------------ |
|         |             | services at the Dept.  | https://nepalitimes.com/latest/open- |
season-on-hacking-into-gov-np
of Immigration and
Passport office,
impaired airport
kiosks and travel
document processing,
thereby delaying Int’l
flights.
2023-02-01 MKS  USA Discrete  R Unknown 1 $450M SEC IA temporarily  “The incident has  https://icsstrive.com/incident/mks-
Instrument Mfg. suspended  affected […]  suspends-operations-to-contain-
| s &  | manufacturing  | production-related  | ransomware-attack/ |
| ---- | -------------- | ------------------- | ------------------ |

| Applied  | operations | systems, and as part  |     |
| -------- | ---------- | --------------------- | --- |
Materials of the containment  https://csoonline.com/article/3687098/mks-
instruments-falls-victim-to-ransomware-
|     |     | effort, the company  | attack.html |
| --- | --- | -------------------- | ----------- |
has elected to
|     |     | temporarily suspend  | https://therecord.media/applied-materials- |
| --- | --- | -------------------- | ------------------------------------------ |
|     |     | operations” -- SEC   | supply-chain-mks-ransomware-attack         |
filing.
https://www.bankinfosecurity.com/mks-
instruments-ransomware-attack-results-in-
200m-sales-hit-a-21442
2023-02-02 Häfele  Germany Discrete  R LockBit 3.0 180 IA Halted order  The kitchen and  https://icsstrive.com/incident/ransomware-
(Hafele,  Mfg. fulfilment; forced furniture fitting  attack-at-german-furniture-company-
| Haefele) | to pre-emptively  | manufacturer  | hafele/ |
| -------- | ----------------- | ------------- | ------- |

|     | shut down  | shutdown their IT  |                                             |
| --- | ---------- | ------------------ | ------------------------------------------- |
|     | systems    | systems worldwide  | https://itsecurityguru.org/2023/05/03/hafel |
e-recovers-from-ransomware-attack-using-
|     |     | and disconnected  | sase/ |
| --- | --- | ----------------- | ----- |
from the internet
|     |     | after the attack. | https://kbbreview.com/52078/news/hafele- |
| --- | --- | ----------------- | ---------------------------------------- |
it-systems-down-after-cyber-attack/
https://techepages.com/hafele-suffers-
ransomware-attack/
2023-02-09 Ziegler  Germany Discrete  R ALPHV /  2 IA Halted ops 11d,  All systems went  https://icsstrive.com/incident/ransomware-
Feuerwehr Mfg. BlackCat with complete  offline following the  attack-halts-operations-at-ziegler-fire-
engine-manufacturer/
| fahrzeuge  | restoration     | attack. Remediation  |     |
| ---------- | --------------- | -------------------- | --- |
|            | taking 24 days  | and restoration      |     |
https://b2b-cyber-security.de/en/alphv-
|     | more | efforts took weeks to  | publishes-data-from-ziegler-fire-brigade- |
| --- | ---- | ---------------------- | ----------------------------------------- |
check, clean and
vehicles/
replace all hardware
|     |     | and software  | https://hz.de/lokales/giengen/nach- |
| --- | --- | ------------- | ----------------------------------- |
cyberangriff-im-februar-alle-systeme-
components before
|     |     | resuming ops. | wiederhergestellt |
| --- | --- | ------------- | ----------------- |

https://hz.de/lokales/giengen/alle-systeme-
offline-giengener-unternehmen-nur-stark-
eingeschraenkt-arbeitsfaehig
44

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor Actor | Attack  | Physical     |     |     |
| --- | ----------- | ------- | ------------ | --- | --- |
|     |             | Type    | Consequences |     |     |
2023-02-11 Gates  USA Discrete  R BlackBasta 30 SEC,  IA Impacted  Worldwide production https://icsstrive.com/incident/gates-
Industrial  Mfg. State  production and  facilities were  industrial-corporation-takes-systems-
offline-temporarily/
| Corporation  |     | of    | shipments | shutdown in an        |     |
| ------------ | --- | ----- | --------- | --------------------- | --- |
| plc          |     | Maine |           | abundance of caution  |     |
https://cybernews.com/security/gates-
|     |     |     |     | after a ransomware  | corporation-ransomware/ |
| --- | --- | --- | --- | ------------------- | ----------------------- |
attack and were

|     |     |     |     | unable to produce or  | https://bizjournals.com/denver/news/2023/ |
| --- | --- | --- | --- | --------------------- | ----------------------------------------- |
|     |     |     |     | ship product.         | 02/27/gates-corp-malware-attack-recovery- |
systems.html

https://breachsense.com/breaches/gates-
data-breach/
2023-02-23 Dole Food  USA Food &  R Unknown 4 $11M SEC IA Shut down North  Following the attack,  https://icsstrive.com/incident/dole-suffers-
| Company | Bev. |     | American     | Dole shutdown       | ransomware-attack/                       |
| ------- | ---- | --- | ------------ | ------------------- | ---------------------------------------- |
|         |      |     | production,  | systems throughout  |                                          |
|         |      |     | halted and   | North America and   | https://bleepingcomputer.com/news/securi |
ty/fruit-giant-dole-suffers-ransomware-
|     |     |     | delayed          | operated some          | attack-impacting-operations             |
| --- | --- | --- | ---------------- | ---------------------- | --------------------------------------- |
|     |     |     | shipments up to  | manually, leading to   |                                         |
|     |     |     | 2 wks.           | fresh food shortages,  | https://malwarebytes.com/blog/news/2023 |
|     |     |     |                  | like lettuce,          | /03/food-giant-dole-reveals-more-about- |
ransomware-attack
throughout North
|     |     |     |     | America. |     |
| --- | --- | --- | --- | -------- | --- |
https://cybersecuritydive.com/news/dole-
ransomware-breached-data-
workers/653650/
2023-02-24 Rosenbauer Austria Discrete  R LockBit 3.0 1 IA Shut down  As a precaution, the  https://icsstrive.com/incident/all-
Mfg. production at all  company shut down  rosenbauer-group-locations-affected-by-
|     |     |     | locations,  | all IT systems.  | cyberattack-claimed-by-lockbit/ |
| --- | --- | --- | ----------- | ---------------- | ------------------------------- |

including Neidling However, they also
|     |     |     | factory, for 2+  | said that affected  | https://www.noen.at/st-poelten/neidling- |
| --- | --- | --- | ---------------- | ------------------- | ---------------------------------------- |
nach-cyber-attacke-rosenbauer-faehrt-it-
|     |     |     | weeks | production, including  | schrittweise-wieder-hoch-neidling-        |
| --- | --- | --- | ----- | ---------------------- | ----------------------------------------- |
|     |     |     |       | at their Neidling      | 358205756                                 |
|     |     |     |       | factory west of St.    |                                           |
|     |     |     |       | Polten.                | https://www.noen.at/st-poelten/auch-werk- |
in-noe-betroffen-cyber-attacke-auf-
feuerwehr-ausruester-rosenbauer-neidling-
cyberangriff-rosenbauer-it-infrastruktur-
redaktion-356154463
https://feuerwehrmagazin.de/nachrichten/n
ews/rosenbauer-ziel-einer-cyber-attacke-
120280
2023-03-01 Steico Group Germany Discrete  U Unknown 1 EU  U Shut down  Steico discloses in an  https://icsstrive.com/incident/steico-group-
Mfg. MAR production for  EU market filing that a operations-disrupted-after-cyberattack/
|     |     |     | several days | cyberattack halted  |     |
| --- | --- | --- | ------------ | ------------------- | --- |
https://csoonline.com/de/a/cyberangriff-
|     |     |     |     | both operations and  | auf-deutschen-baustoffproduzent,3674479 |
| --- | --- | --- | --- | -------------------- | --------------------------------------- |
IT systems.

https://web.archive.org/web/202303060602
23/www.steico.com/de/

https://bnnbloomberg.ca/steico-owner-is-
said-to-weigh-sale-of-wood-insulation-
maker-1.1919432
2023-03-14 Fiege Logistik Italy Transport R LockBit 3.0 3 U Disrupted logistic Lockbit took out 15%  https://icsstrive.com/incident/ransomware-
(Logistics) operations in  of Fiege's Italian  attack-at-fiege-logistik-italian-sites/
logistics. After rushing
|     |     |     | Italy for 3 days |     | https://eurotransport.de/artikel/hacker- |
| --- | --- | --- | ---------------- | --- | ---------------------------------------- |
to isolate the 3 sites,
greifen-fiege-logistik-an-interne-daten-im-
|     |     |     |     | the spread stopped,  | darknet-aufgetaucht-11221630.html          |
| --- | --- | --- | --- | -------------------- | ------------------------------------------ |
|     |     |     |     | and restoration      |                                            |
|     |     |     |     | began.               | https://redpacketsecurity.com/lockbit-3-0- |
ransomware-victim-fiege-com/
https://verkehrsrundschau.de/nachrichten/t
ransport-logistik/cyber-angriff-auf-fiege-
3349093
2023-03-17 Alliance  Spain Transport U Unknown 850 U Disrupted  The attack impacted  https://icsstrive.com/incident/cyberattack-
Healthcare distribution of  the distribution of  at-drug-distributor-alliance-healthcare-
|     |     |     | medicine to  | medicine to 850  | impacts-pharmacies-in-spain/ |
| --- | --- | --- | ------------ | ---------------- | ---------------------------- |

|     |     |     | pharmacies; 1/4   | pharmacies, causing  | https://cybernews.com/news/cyberattack-  |
| --- | --- | --- | ----------------- | -------------------- | ---------------------------------------- |
|     |     |     | of pharmacies in  | supply chain         | alliance-healthcare/                     |
|     |     |     | Catalonia         | disruptions and      |                                          |
|     |     |     | hardest hit       | delays throughout    | https://scmagazine.com/news/cyberattack- |
hits-spanish-pharmaceutical-company-
Spain.
alliance-healthcare

https://thelocal.es/20230323/cyberattack-
disrupts-spanish-medicine-distribution
45

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor Actor Attack Physical  |     |     |     |
| ---------------------------- | --- | --- | --- |
Type Consequences
2023-03-17 Hahn Group Germany Discrete  U Unknow 1 IA Shut down  After an attack, all  https://icsstrive.com/incident/hahn-
Mfg. n production 10+  systems were switched  group-shuts-down-network-and-
systems-after-cyberattack/
|     | days | off as a safety          |                                     |
| --- | ---- | ------------------------ | ----------------------------------- |
|     |      | precaution, and rebuilt  | https://csoonline.com/de/a/automati |
onsspezialist-von-cyberattacke-
|     |     | from a clean-room  | betroffen,3674530  |
| --- | --- | ------------------ | ------------------ |
environment, with full
https://hahn.group/en/2023/04/14/up
|     |     | restoration expected to  | date-cyber-attack/ https:// |
| --- | --- | ------------------------ | --------------------------- |
take weeks.
2023-03-24 NZZ Mediengruppe  Switzerland Process  R Play /  2 ID Shut down  A Play ransomware  https://icsstrive.com/incident/swiss-
Zürich Mfg. PlayCry printing for 2+  attack halted NZZ's  german-language-newspaper-nzz-
shut-down-production/
| pt  | weeks, then  | printing presses and  |                                       |
| --- | ------------ | --------------------- | ------------------------------------- |
|     | capacity     | impacted their        | https://swissinfo.ch/eng/business/hac |
ker-group-publishes-stolen-swiss-
|     | reduced, for  | customers who depend     | media-data/48504626                  |
| --- | ------------- | ------------------------ | ------------------------------------ |
|     | both NZZ and  | on their print services. | https://breakinglatest.news/technolo |
|     | customer CH-  |                          | gy/nzz-has-to-shut-down-the-         |
|     | Media-Verlag  |                          | newspaper-production-system-after-   |
a-cyber-attack/
2023-03-25 SAF-Holland Group Germany Discrete  R ALPHV /  2 €41M EU  U Interrupted  Filed a 17. 596/2014 MAR https://icsstrive.com/incident/cyberat
Mfg. BlackCa MAR production for 7- report to the EU  tack-at-saf-holland-causes-three-
month-production-backlog/
| t   | 14 days, caused  | Parliament following an  |              |
| --- | ---------------- | ------------------------ | ------------ |
|     | 3-month backlog  | attack that halted       | https://eqs- |
news.com/news/adhoc/saf-holland-
|     |     | production at multiple  | se-saf-holland-se-affected-by- |
| --- | --- | ----------------------- | ------------------------------ |
locations and disclosed
cyberattack/1783179
|     |     | heavy sales losses and  | https://www.breachsense.com/breac |
| --- | --- | ----------------------- | --------------------------------- |
|     |     | remediation expenses.   | hes/saf-holland-data-breach/      |
https://globaltrailermag.com/2023/05
/09/unexpected-strong-financial-
year-start-for-saf-holland/
2023-03-27 CommScope USA Discrete  R Vice  1 U Shut down  According to employees, https://icsstrive.com/incident/vice-
Mfg. Society production for 2  CommScope suffered a  society-disrupts-operations-at-
commscope-and-publishes-employee-
|     | days | ransomware incident        |       |
| --- | ---- | -------------------------- | ----- |
|     |      | that resulted in "several  | pii/  |
https://techcrunch.com/2023/04/27/c
|     |     | days of widespread  | ommscope-ransomware-data/  |
| --- | --- | ------------------- | -------------------------- |
disruption, including
https://techcrunch.com/2023/04/17/h
|     |     | plant production." | ackers-publish-sensitive-employee- |
| --- | --- | ------------------ | ---------------------------------- |
data-stolen-during-commscope-
ransomware-attack/
https://therecord.media/commscope-
network-infrastructure-cyberattack-
vice-society
2023-03-31 Ustra  Germany Transport R Unknow 1 ID Delayed start  A new passenger rail  https://icsstrive.com/incident/public-
Deutschlandticket n and operation of service in Hannover  transportation-deutschlandticket-
|     | new rail service  | suffered an attack  | launch-in-germany-disrupted-by- |
| --- | ----------------- | ------------------- | ------------------------------- |
ransomware-attack/
|     | for 3+ days | disabling digital signage,  | https://bild.de/regional/hannover/han |
| --- | ----------- | --------------------------- | ------------------------------------- |
telephone, computer,
nover-aktuell/cyberattacke-auf-
|     |     | and ticket systems. The  | uestra-hacker-stoppen-deutschland-     |
| --- | --- | ------------------------ | -------------------------------------- |
|     |     | service's start was      | ticket-in-hannover-83439654.bild.html  |
|     |     | delayed despite trains   | https://csoonline.com/de/a/cyberatta   |
being capable of moving cke-auf-hannoversche-
verkehrsbetriebe,3674537 https://
down the track.
https:// https:// https:// https://
2023-04-05 Israel Postal  Israel Transport H Anonym 1 ID Halted some  As part of the annual  https://icsstrive.com/incident/disrupti
Company ous  postal services,  #OPIsrael hacktivist  on-at-israel-postal-company-after-
cyberattack-last-for-6-days/
| Sudan /  | including Int’l  | campaign, several  |     |
| -------- | ---------------- | ------------------ | --- |
#OPIsra mail and local  services including the  https://jns.org/cyberattack-shutters-
galilee-farm-water-controllers/
el courier, for 6+  sending of Int’l mail and  https://calcalistech.com/ctechnews/
|     | days | courier services were  | article/hj000lsgm3 |
| --- | ---- | ---------------------- | ------------------ |
interrupted, then
proactively shut down,
while the Cyber
Directorate was brought
in to assist with
investigations and
recovery.
46

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor Actor Attack  | Physical  |     |     |
| --- | ------------------- | --------- | --- | --- |
Type Consequences
2023-04-08 Bobst  Switzerla Discrete  R BlackBasta 1 IA Disrupted  The sewing machine  https://icsstrive.com/incident/operations-
nd Mfg. operations 9  manufacturer suffered  disrupted-at-machine-manufacturer-bobst/

|     |     | days | an attack that       |                                           |
| --- | --- | ---- | -------------------- | ----------------------------------------- |
|     |     |      | impacted operations  | https://24heures.ch/bobst-resiste-a-deux- |
piratages-informatiques-788144530362
|     |     |     | over the Easter long  |     |
| --- | --- | --- | --------------------- | --- |
weekend, forcing them https://inside-it.ch/mutmassliche-abb-
to isolate systems and hacker-stecken-auch-hinter-angriff-auf-
|     |     |     | halting production. | bobst-20230607 |
| --- | --- | --- | ------------------- | -------------- |

https://letemps.ch/economie/cyber/bobst-
reussi-dejouer-deux-cyberattaques-ciblees
2023-04-09 Galil Sewage  Israel Water H GhostSec / 1 DO Disabled and  Internet-exposed  https://icsstrive.com/incident/israel-water-
Corp. #OPIsrael defaced water  Unitronics pump  monitoring-systems-in-cyber-attack/
|     |     | pump controllers  | controllers, in         |                                       |
| --- | --- | ----------------- | ----------------------- | ------------------------------------- |
|     |     | 1-day,            | operation at farms and  | https://jns.org/cyberattack-shutters- |
galilee-farm-water-controllers/
|     |     | interrupting  | the Galil's wastewater  |     |
| --- | --- | ------------- | ----------------------- | --- |
|     |     | wastewater    | facility in the Jordan  |     |
https://securityweek.com/irrigation-
|     |     | treatment | valley, were defaced  | systems-in-israel-disrupted-by-hacker- |
| --- | --- | --------- | --------------------- | -------------------------------------- |
attacks-on-ics/
and disabled by
|     |     |     | hacktivists of the  |     |
| --- | --- | --- | ------------------- | --- |
https://labs.yarix.com/2023/08/ghostsec-
|     |     |     | annual #OPIsrael  | the-hacktivist-collective-targeting-icss/ |
| --- | --- | --- | ----------------- | ----------------------------------------- |
campaign. While farms
were unaffected and
able to run manually, it
took Galil a day to
resume treatment ops.
2023-04-12 Fincantieri  USA Discrete  R Unknown 1 ID Disabled CNC  Ransomware infected  https://icsstrive.com/incident/ransomware
-attack-delays-shipyard-production-at-
| Marinette  | Mfg. | manufacturing  | the network,  |     |
| ---------- | ---- | -------------- | ------------- | --- |
Marine  machines 1-2  encrypting not only file marinette-marine-shipyard/

(FMM) days; delayed  servers essential to  https://news.usni.org/2023/04/20/ransom
|     |     | production | the shipyard's CNC  |     |
| --- | --- | ---------- | ------------------- | --- |
ware-attack-hits-marinette-marine-
|     |     |     | machines, but other   | shipyard-results-in-short-term-delay-of- |
| --- | --- | --- | --------------------- | ---------------------------------------- |
|     |     |     | services like email,  | frigate-freedom-lcs-construction         |
implying an OT
dependency on IT
services, or a flat
network.
2023-04-12 Lürssen Germany Discrete  R Unknown 1 U Shut down  Ransomware  https://icsstrive.com/incident/operations-
halted-at-german-superyacht-maker-by-
|     | Mfg. | shipyard       | shutdown large parts    |                    |
| --- | ---- | -------------- | ----------------------- | ------------------ |
|     |      | operations in  | of shipyard operations  | ransomware-attack/ |

|     |     | Bremen | at the superyacht and  | https://therecord.media/german-builder- |
| --- | --- | ------ | ---------------------- | --------------------------------------- |
military ship builder for of-superyachts-and-military-boats
an undisclosed amount
|     |     |     | of time. | https://news.yahoo.com/german- |
| --- | --- | --- | -------- | ------------------------------ |
superyacht-maker-targeted-ransomware-
123518896.html
2023-04-15 Evotec SE Germany Pharma R ALPHV /  1 > €10M IA Shut down  Pre-emptively chose to https://icsstrive.com/incident/german-
BlackCat proteomics  shutdown systems to  biotechnology-company-evotec-shuts-
down-it-systems/
|     |     | machines,        | protect company and  |     |
| --- | --- | ---------------- | -------------------- | --- |
|     |     | interrupted new  | partner data,        |     |
https://scbio.org/biotech-ceo-gets-hands-
|     |     | drug control   | temporarily ceasing      | on-after-cyberattack-to-protect-business/ |
| --- | --- | -------------- | ------------------------ | ----------------------------------------- |
|     |     | studies, lost  | operations, including    |                                           |
|     |     | customers,     | proteomics machines      | https://therecord.media/german-drug-      |
|     |     | caused         | and ongoing              | company-says-cyberattack-causing-delays   |
|     |     | production     | automated drug           |                                           |
|     |     | delays         | control studies. Evotec  |                                           |
lost contract
customers requiring
rapid results which
sought out other firms.
2023-04-20 Badische  Germany Process  U Unknown 1 IA Shut down  Police are investigating https://icsstrive.com/incident/german-
Stahlwerke  Mfg. production,  after BSW reported  steelmaker-hacked/
| (BSW) |     | furloughed 850  | "unauthorized access  |     |
| ----- | --- | --------------- | --------------------- | --- |
https://stadtanzeiger-ortenau.de/kehl-
(Baden Steel  employees to its network," then  stadt/c-lokales/hacker-angriff-auf-
| Works) |     |     | pre-emptively initiated  |     |
| ------ | --- | --- | ------------------------ | --- |
badischen-stahlwerke_a87063
a controlled shut-down
|     |     |     | of all systems,       | https://csoonline.com/de/a/cyberattacke- |
| --- | --- | --- | --------------------- | ---------------------------------------- |
|     |     |     | affecting production. | auf-badische-stahlwerke,3674567          |
https://bo.de/lokales/ortenau/hackerangrif
f-auf-badische-stahlwerke-in-kehl#
47

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor Actor Attack  | Physical  |     |     |
| --- | ------------------- | --------- | --- | --- |
Type Consequences
2023-04-25 Americold USA Bldg.  R Cactus 250 IA Shut down all 250 The cold storage company  https://icsstrive.com/incident/opera
Automati warehouses  shut down their network to  tions-impacted-at-americold-after-
network-breach/
|     | on  | globally for 1+   | contain a ransomware          |     |
| --- | --- | ----------------- | ----------------------------- | --- |
|     |     | wks, halting all  | attack and began to rebuild.  |     |
https://bleepingcomputer.com/news
|     |     | inbound and    | Meanwhile, they were         | /security/cold-storage-giant- |
| --- | --- | -------------- | ---------------------------- | ----------------------------- |
|     |     | most outbound  | unable to accept logistical  |                               |
americold-discloses-data-breach-
|     |     | cold storage | inbound and all-but critically after-april-malware-attack/ |     |
| --- | --- | ------------ | ---------------------------------------------------------- | --- |
|     |     |              | perishable outbound                                        |     |
https://therecord.media/cold-
deliveries at their cold
|     |     |     | storage facilities. Employees  | storage-company-americold- |
| --- | --- | --- | ------------------------------ | -------------------------- |
reports-cyberattack
and customers reported on
reddit that global ops were
https://reddit.com/r/supplychain/co
|     |     |     | shutdown. | mments/12zjaup/americold_north_a |
| --- | --- | --- | --------- | -------------------------------- |
merica_shutdown/
2023-04-27 Elysée  France Process  R Unknown 1 €3M U Shut down  The manufacturer of  https://icsstrive.com/incident/french
-cosmetics-factory-at-standstill-
| Cosmétiques | Mfg. | production 13+    | cosmetic aerosols reported   |                    |
| ----------- | ---- | ----------------- | ---------------------------- | ------------------ |
|             |      | days; furloughed  | that Russian cybercriminals  | after-cyberattack/ |

|     |     | 300 employees | attacked their centralized  | https://radiomelodie.com/a/18085- |
| --- | --- | ------------- | --------------------------- | --------------------------------- |
servers in Germany and
elysee-cosmetiques-face-a-une-
|     |     |     | shutdown production. | cyberguerre-selon-son-directeur- |
| --- | --- | --- | -------------------- | -------------------------------- |
general
https://republicain-
lorrain.fr/economie/2023/05/04/serv
eurs-pirates-par-des-russes-l-usine-
elysee-cosmetiques-a-l-arret
2023-04-29 Maxim  Germany Process  R BlackBasta 1 IA Shut down  An attack encrypted the  https://icsstrive.com/incident/emerg
Cosmetics Mfg. production corporate network, caused  ency-operational-shutdown-at-
the cosmetics manufacturer maxim-german-cosmetics-
manufacturer/
to pre-emptively shut down

|     |     |     | all systems and begin       | https://ksta.de/region/rhein-       |
| --- | --- | --- | --------------------------- | ----------------------------------- |
|     |     |     | remediation. This caused a  | erft/pulheim/pulheimer-             |
|     |     |     | production shutdown also    | kosmetikhersteller-maxim-will-sich- |
|     |     |     | implying an OT dependency   | gegen-neuen-hackerangriff-          |
schuetzen-567732
on IT systems.
https://csoonline.com/de/a/ransom
ware-angriff-auf-kosmetikhersteller-
maxim,3680898
https://breachsense.com/breaches/
maxim-data-breach/
2023-05-06 Orqa FPV Croatia Discrete  SC Swarg 1 DM Bricked  A contracted developer  https://icsstrive.com/incident/contr
actor-inserts-cyber-time-bomb-
|     | Mfg. | manufactured      | planted malicious code into                                    |     |
| --- | ---- | ----------------- | -------------------------------------------------------------- | --- |
|     |      | devices, after a  | the firmware of Orqa's drone attack-in-firmware-of-orqa-drone- |     |
goggle/
|     |     | specified date  | goggles, designed to brick                                   |                                   |
| --- | --- | --------------- | ------------------------------------------------------------ | --------------------------------- |
|     |     | had been        | devices after a timestamp is https://cyware.com/news/drone-  |                                   |
|     |     | reached (time-  | reached. Later, the bad                                      | goggles-maker-orqa-hit-with-time- |
|     |     | bomb attack)    | actor offers an unauthorized bomb-ransomware-attack-821e7295 |                                   |

binary firmware fix, for sale
|     |     |     | online, marketed as a  | https://theregister.com/2023/05/03/ |
| --- | --- | --- | ---------------------- | ----------------------------------- |
orqa_goggles_borked/
"license extension and
renewal" update. A complex
https://bleepingcomputer.com/news
|     |     |     | case of ransomware            | /technology/drone-goggles-maker- |
| --- | --- | --- | ----------------------------- | -------------------------------- |
|     |     |     | deployed into the supply      | claims-firmware-sabotaged-to-    |
|     |     |     | chain by a malicious insider. | brick-devices/                   |
2023-05-07 ABB Switzerla Discrete  R BlackBasta 1 IA Lost production  Windows AD was attacked  https://icsstrive.com/incident/abb-
nd Mfg. and shut down  by ransomware causing ABB  hit-in-cyberattack-operations-suffer/
|     |     | external network  | to shut their VPN            |                                   |
| --- | --- | ----------------- | ---------------------------- | --------------------------------- |
|     |     | connections to    | connections to customers to  | https://bleepingcomputer.com/news |
/security/multinational-tech-firm-
|     |     | customers, in an  | contain the spread.     | abb-hit-by-black-basta- |
| --- | --- | ----------------- | ----------------------- | ----------------------- |
|     |     | abundance of      | Manufacturing was also  |                         |
ransomware-attack/
|     |     | caution | disrupted. |     |
| --- | --- | ------- | ---------- | --- |
https://cyberplace.social/@GossiTh
eDog/110355364010961428
https://securityweek.com/industrial-
giant-abb-confirms-ransomware-
attack-data-theft/
48

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor Actor | Attack  | Physical  |     |     |
| --- | ----------- | ------- | --------- | --- | --- |
Type Consequences
2023-05-10 Suzuki  India Discrete  U Unknown 1 20,000  U lost production  Shutdown  https://icsstrive.com/incident/cyberattack-
Motorcycle  Mfg. units of 20,000+ units,  manufacturing  halts-production-at-factories-of-suzuki-
motorcycle-india/
| India |     |     | 10+ days  | facilities due to a  |     |
| ----- | --- | --- | --------- | -------------------- | --- |
|       |     |     | downtime  | cyberattack.         |     |
https://auto.hindustantimes.com/auto/two
-wheelers/suzuki-motorcycle-india-plant-
shut-after-cyber-attack-production-
affected-41684581981220.html

https://autocarpro.in/news/exclusive-
suzuki-motorcycle-india-plant-shut-for-a-
week-due-to-cyber-attack-115136

https://livemint.com/news/india/hit-by-
cyberattack-suzuki-motorcycle-india-halts-
production-at-its-factories-report-
11684537524538.html
2023-05-11 The  USA Process  U Unknown 1 IA Lost production  Suffered a  https://icsstrive.com/incident/philadelphia
Philadelphia  Mfg. for 3 days; halted cyberattack,  -inquirer-unable-to-print-sunday-paper/
| Inquirer |     |     | printing and  | impacting both IT and  |     |
| -------- | --- | --- | ------------- | ---------------------- | --- |
https://theguardian.com/us-
|     |     |     | distribution | OT systems, and         |                                         |
| --- | --- | --- | ------------ | ----------------------- | --------------------------------------- |
|     |     |     |              | prevented the printing  | news/2023/may/15/philadelphia-inquirer- |
cyber-attack
and distribution of the
|     |     |     |     | regular Sunday May 14  | https://inquirer.com/news/philadelphia/phi |
| --- | --- | --- | --- | ---------------------- | ------------------------------------------ |
|     |     |     |     | edition.               | ladelphia-inquirer-hack-cyber-disruption-  |
20230514.html
2023-05-12 Lacroix France Discrete  R Unknown 3 ID 3 factories in  Intercepted a targeted https://icsstrive.com/incident/lacroix-hit-
in-cyberattack/
|     | Mfg. |     | France, Germany   | attack on the French  |     |
| --- | ---- | --- | ----------------- | --------------------- | --- |
|     |      |     | and Tunisia shut  | (Beaupréau), German   |     |
https://techmonitor.ai/technology/cyberse
|     |     |     | for 10 days | (Willich) and Tunisian  | curity/lacroix-cyberattack-factories-closed |
| --- | --- | --- | ----------- | ----------------------- | ------------------------------------------- |
(Zriba) sites.

|     |     |     |     | Downtime was mostly  | https://securityweek.com/lacroix-closes- |
| --- | --- | --- | --- | -------------------- | ---------------------------------------- |
|     |     |     |     | restoration from     | production-sites-following-ransomware-   |
attack/
backups, as all
|     |     |     |     | systems were  |     |
| --- | --- | --- | --- | ------------- | --- |
https://cybernews.com/news/lacroix-data-
|     |     |     |     | encrypted. | breach/ |
| --- | --- | --- | --- | ---------- | ------- |
2023-05-20 Granules  India Pharma R LockBit 3.0 1 NSE ID Shut down  Regulatory and quality  https://icsstrive.com/incident/significant-
India production 40+  standards could not be revenue-loss-at-indian-pharmaceutical-
giant-after-cyberattack/
|     |     |     | days, reported a   | met due to major    |     |
| --- | --- | --- | ------------------ | ------------------- | --- |
|     |     |     | 'significant loss  | disruptions in the  |     |
https://reuters.com/business/healthcare-
|     |     |     | of revenue' | company's IT systems. | pharmaceuticals/paracetamol-maker- |
| --- | --- | --- | ----------- | --------------------- | ---------------------------------- |
granules-india-q1-profit-hurt-by-cyber-
attack-disruptions-2023-08-09/
https://thehindubusinessline.com/compani
es/cyber-attack-has-caused-significant-
loss-to-revenue-profitability-granules-
india/article67022628.ece

https://techcrunch.com/2023/06/15/lockbi
t-ransomware-granules-india/
2023-06-10 Haynes Int’l USA Process  R LockBit 3.0 1 quarte SEC U Shut down  The attack temporarily https://icsstrive.com/incident/haynes-
Mfg. rly  production for 11  disrupted  international-cyberattack-estimated-cost-
is-18-20-million/
|     |     | $18M  | days and delayed manufacturing ops.  |                 |     |
| --- | --- | ----- | ------------------------------------ | --------------- | --- |
|     |     | net   | shipments                            | and production  |     |
https://finance.yahoo.com/news/haynes-
|     |     | revenu |     | shipments. | hit-cybersecurity-incident-disrupts- |
| --- | --- | ------ | --- | ---------- | ------------------------------------ |
e or
035900431.html
|     |     | $3.7M   |     |     |                                            |
| --- | --- | ------- | --- | --- | ------------------------------------------ |
|     |     | EBITDA  |     |     | https://twitter.com/FalconFeedsio/status/1 |
687789436266848256
loss

https://channelchek.com/news-
channel/haynes-international-hayn-
lowering-estimates-to-reflect-near-term-
impact-of-a-cyberattack
2023-06-13 Brunswick  USA Discrete  U Unknown 2 up to  U Halted  An attack on the  https://icsstrive.com/incident/brunswick-
Corporation Mfg. $85M production &  Mercury Marine  corp-recovering-from-serious-cyberattack/

distribution for 17 outboard motor maker
|     |     |     | workdays | forced them to  | https://maritime- |
| --- | --- | --- | -------- | --------------- | ----------------- |
executive.com/article/brunswick-corp-
|     |     |     |     | shutdown during  | works-to-recover-from-cyberattack |
| --- | --- | --- | --- | ---------------- | --------------------------------- |
restoration. The CEO

|     |     |     |     | stated lost production  | https://boatingindustry.com/top-    |
| --- | --- | --- | --- | ----------------------- | ----------------------------------- |
|     |     |     |     | cannot be recovered     | news/2023/06/27/brunswick-provides- |
operations-update-following-cyber-attack/
due to a full
|     |     |     |     | production schedule  |     |
| --- | --- | --- | --- | -------------------- | --- |
https://cyware.com/news/marine-industry-
|     |     |     |     | until end-of-year. | giant-brunswick-corporation-lost-85- |
| --- | --- | --- | --- | ------------------ | ------------------------------------ |
million-in-cyberattack-ceo-confirms-
e32f91b2/
49

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor | Actor Attack  | Physical  |     |     |
| --- | ----- | ------------- | --------- | --- | --- |
Type Consequences
2023-06-15 KNP Logistics  UK Transpor R Akira 1 Bankru ID 730 jobs lost,  An attack forced KNP  https://icsstrive.com/incident/uk-based-
Group t pt bankrupted  to lay off 730 workers  knp-logistics-business-shuts-down-700-
jobs-lost/
|     |     |     | company, forced     | and close the         |     |
| --- | --- | --- | ------------------- | --------------------- | --- |
|     |     |     | to sell off assets  | company, because the  |     |
https://bbc.com/news/uk-england-
|     |     |     | and subsidiaries | ransomware impacted  | cambridgeshire-66997691 |
| --- | --- | --- | ---------------- | -------------------- | ----------------------- |
key systems and
|     |     |     |     | processes, preventing  | https://therecord.media/knp-logistics- |
| --- | --- | --- | --- | ---------------------- | -------------------------------------- |
|     |     |     |     | them from securing     | ransomware-insolvency-uk               |
additional investment
|     |     |     |     | and funding. | https://cybertalk.org/ransomware-forces- |
| --- | --- | --- | --- | ------------ | ---------------------------------------- |
large-logistics-firm-to-close/
2023-06-16 Rheinische  Germany Process  U Unknown 1 U Halted print (and One of the top 5  https://icsstrive.com/incident/cyberattack-
Post  Mfg. online)  newspaper publishers  causes-widespread-operational-disruption-
Mediengruppe newspaper  in Germany was forced at-rheinische-post-mediagruppe/
|     |     |     | production and  | to halt operations and  |     |
| --- | --- | --- | --------------- | ----------------------- | --- |
https://tagesschau.de/wirtschaft/unterneh
|     |     |     | distribution for at pre-emptively cut  |                      | men/rheinische-post-hackerangriff- |
| --- | --- | --- | -------------------------------------- | -------------------- | ---------------------------------- |
|     |     |     | least 1 day                            | themselves off from  |                                    |
100.html
the internet following
https://zeit.de/news/2023-
a cyberattack.
06/19/cyberangriff-auf-mediengruppe-
zeitungen-mit-
notausgaben?utm_referrer=https%3A%2F%
2Ficsstrive.com%2F
2023-06-22 Livingston Int’l Canada Transpor R Royal 125 DS Shut down  Livingston stated they  https://icsstrive.com/incident/giant-north-
t operations at  shutdown because  american-freight-forwarder-livingstone-hit-
|     |     |     | CAN-US border,  | protecting clients'   | by-ransomware-attack/                     |
| --- | --- | --- | --------------- | --------------------- | ----------------------------------------- |
|     |     |     | and delayed     | systems and data was  |                                           |
|     |     |     | shipments by    | of paramount          | https://trucknews.com/transportation/cust |
oms-broker-systems-shutdown-causes-
|     |     |     | truck for 2 days | importance,  | border-delays/1003176137/ |
| --- | --- | --- | ---------------- | ------------ | ------------------------- |
highlighting the lack of
segmentation between https://thecyberexpress.com/royal-
|     |     |     |     | business data and  | ransomware-group-adds-livingston-victim/ |
| --- | --- | --- | --- | ------------------ | ---------------------------------------- |
physical ops.
2023-07-02 Montpellier- France Transpor U Unknown 1 U Shut down all  The attack, while only  https://icsstrive.com/incident/operations-
Méditerranée  t internal systems,  causing the airport to  disrupted-at-montpellier-airport-after-
weekend-cyberattack/
| (Fréjorgues)  |     |     | forcing airport  | operate manually for  |     |
| ------------- | --- | --- | ---------------- | --------------------- | --- |
| Airport       |     |     | ops to operate   | several hours, had a  |     |
https://midilibre.fr/2023/07/02/nos-
|     |     |     | manually for    | much longer-term      | systemes-ont-ete-hs-durant-plusieurs- |
| --- | --- | --- | --------------- | --------------------- | ------------------------------------- |
|     |     |     | several hours;  | impact of cancelling  |                                       |
heures-une-cyberattaque-tres-violente-
|     |     |     | cancelled and    | and delaying flights for contre-laeroport-de-montpellier- |              |
| --- | --- | --- | ---------------- | --------------------------------------------------------- | ------------ |
|     |     |     | delayed flights  | a week.                                                   | 11316240.php |
for a week
2023-07-04 Port of NagoyaJapan Transpor NS Unknown  2 ID Shut down port  Caused disruption to  https://icsstrive.com/incident/container-
processing-halted-at-the-port-of-nagoya/
|     | t   | (China) | for 3 days and a  | the circulation of  |     |
| --- | --- | ------- | ----------------- | ------------------- | --- |
|     |     |         | Toyota parts      | goods to and from   |     |
https://bleepingcomputer.com/news/secur
|     |     |     | export plant 1  | Japan. Toyota auto     | ity/japans-largest-port-stops-operations- |
| --- | --- | --- | --------------- | ---------------------- | ----------------------------------------- |
|     |     |     | day             | shipments and a parts  |                                           |
after-ransomware-attack/
export plant were also
|     |     |     |     | affected. Originally  | https://cnn.com/2023/07/06/tech/japan- |
| --- | --- | --- | --- | --------------------- | -------------------------------------- |
port-ransomware-attack/index.html
attributed to LockBit
3.0 ransomware,
https://www.ft.com/content/de0042f8-
|     |     |     |     | sources suggested a  | a7ce-4db5-bf7b-aed8ad3a4cfd |
| --- | --- | --- | --- | -------------------- | --------------------------- |
month later to the
Financial Times that
this was a disguised
attack by the Chinese
government, testing
Japan's critical infra.
2023-07-14 Wildeboer Germany Discrete  R Unknown 1 ID Production  While the company  https://icsstrive.com/incident/ransomware
Mfg. halted and 350  says the attack  -attack-shuts-down-operations-at-german-
manufacturer-wildeboer/
|     |     |     | employees         | affected its IT      |     |
| --- | --- | --- | ----------------- | -------------------- | --- |
|     |     |     | temporarily laid  | systems, production  |     |
https://csoonline.com/de/a/deutscher-
|     |     |     | off with benefits  | was halted, suggesting bauproduzent-wildeboer-von-    |                                     |
| --- | --- | --- | ------------------ | ----------------------------------------------------- | ----------------------------------- |
|     |     |     | (Kurtzarbeit) for  | operations depends on hackerangriff-betroffen,3681028 |                                     |
|     |     |     | 4+ wks.            | IT. 350 employees                                     |                                     |
|     |     |     |                    | were temporarily laid                                 | https://wildeboer.de/en/important-  |
|     |     |     |                    | off and put on state-                                 | information-attack-on-wildeboer-it- |
|     |     |     |                    | sponsored benefits.                                   | systems/                            |

https://ga-
online.de/artikel/1391624/Ostfriesisches-
Unternehmen-nach-Cyberattacke-immer-
noch-lahmgelegt
50

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor | Actor Attack  | Physical  |     |     |
| ----- | ------------- | --------- | --- | --- |
Type Consequences
2023-07-20 Campbell  USA Food &  U Unknown 1 ID Shut down  Campbell's Napoleon,  https://icsstrive.com/incident/campbell-
Soup Co. Bev. production 3  OH plant shutdown  soup-shuts-down-oh-site-after-
cyberattack/
|     |     | days, sent     | due to "IT related  |     |
| --- | --- | -------------- | ------------------- | --- |
|     |     | employees home | complications,"     |     |
https://toledoblade.com/business/labor/2
|     |     |     | exposing an OT  | 023/08/03/three-day-campbell-s- |
| --- | --- | --- | --------------- | ------------------------------- |
dependency on IT
napoleon-plant-outage-due-to-it-
|     |     |     | systems. | problems-company- |
| --- | --- | --- | -------- | ----------------- |
says/stories/20230803129
https://cybersecuritydive.com/news/camp
bell-soup-cyberattack-limited-
impact/694758/
2023-07-23 Tempur Sealy USA Discrete  R ALPHV /  1 SEC U Temporarily  In an SEC 8K disclosure https://icsstrive.com/incident/tempur-
Int’l Mfg. BlackCat interrupted  filing, Tempur Sealy  sealy-international-suffers-cyberattack/
|     |     | operations,  | admitted to the  |     |
| --- | --- | ------------ | ---------------- | --- |
https://thecyberexpress.com/tempur-
|     |     | losing 1 wk       | attack. Workers took     | sealy-cyber-attack-blackcat-ransomware/ |
| --- | --- | ----------------- | ------------------------ | --------------------------------------- |
|     |     | production; sent  | to social media to talk  |                                         |

|     |     | workers home | of being sent home  | https://therecord.media/mattress-giant- |
| --- | --- | ------------ | ------------------- | --------------------------------------- |
|     |     |              | amid production     | tempur-sealy-cyberattack                |
outages.
2023-08-15 Clorox USA Discrete  R ALPHV/Sca 1 $49M SEC IA Disrupted  In an SEC filing, the  https://icsstrive.com/incident/cleaning-
Mfg. ttered  operations,  company said damage products-maker-clorox-suffers-attack/
|     | Spider | delayed  | to the IT network  |     |
| --- | ------ | -------- | ------------------ | --- |
https://theregister.com/2023/09/19/the_cl
|     |     | production >1    | "caused widescale       |                            |
| --- | --- | ---------------- | ----------------------- | -------------------------- |
|     |     | month, lost CISO | disruption of Clorox's  | orox_company_admits_cyber/ |

|     |     |     | operations." Clorox's    | https://finance.yahoo.com/news/clorox- |
| --- | --- | --- | ------------------------ | -------------------------------------- |
|     |     |     | CISO left during the     | cyber-chief-leaves-recovery-           |
|     |     |     | crisis and the role was  | 191819607.html                         |

|     |     |     | filled by a temp. | https://www.bnnbloomberg.ca/clorox- |
| --- | --- | --- | ----------------- | ----------------------------------- |
security-breach-linked-to-group-behind-
casino-hacks-1.1980331
2023-08-25 Polish Rail Poland Transport H 2 Polish  20 DO Halted 20+ trains  Two Polish citizens  https://icsstrive.com/incident/polish-
citizens and denied  shut down trains using  railways-hack-paralyzed-freight-and-
passenger-trains/
|     |     | service for 2+  | simple radio           |     |
| --- | --- | --------------- | ---------------------- | --- |
|     |     | hours           | equipment, through an  |     |
https://bbc.com/news/world-europe-
|     |     |     | outdated system  | 66630260?blaid=4990964 |
| --- | --- | --- | ---------------- | ---------------------- |
designed to wireless

|     |     |     | engage onboard     | https://wired.com/story/poland-train- |
| --- | --- | --- | ------------------ | ------------------------------------- |
|     |     |     | emergency brakes.  | radio-stop-attack/                    |
This un-authenticated,
|     |     |     | un-encrypted VHF  | https://railjournal.com/technology/unauth |
| --- | --- | --- | ----------------- | ----------------------------------------- |
orised-radio-stop-signal-disrupts-pkp-
|     |     |     | 150MHz-band radio  | operations/ |
| --- | --- | --- | ------------------ | ----------- |
protocol was already
scheduled for
replacement by 2025.
2023-08-29 20+ Civilian  Iraq Transport U Unknown 20 DO Loss of  A novel type of GPS  https://icsstrive.com/incident/fake-gps-
and private  navigation,  and IRS signal spoofing signals-in-middle-east-lead-multiple-
aircrafts-astray/
| Jets |     | diverted aircraft  | attack caused over 20  |     |
| ---- | --- | ------------------ | ---------------------- | --- |
|      |     | from intended      | aircraft to suffer     |     |
https://timesofindia.indiatimes.com/world/
|     |     | path into      | complete loss of                                        | rest-of-world/fake-gps-signals-sent-20- |
| --- | --- | -------------- | ------------------------------------------------------- | --------------------------------------- |
|     |     | restricted or  | navigational capability aircraft-off-course-in-iranian- |                                         |
|     |     | dangerous      | over restricted or                                      | airspace/articleshow/104074703.cms?from |
|     |     | airspace, &    | dangerous airspace,                                     | =mdr                                    |

|     |     | endangered lives  | and unintended flight  |                                      |
| --- | --- | ----------------- | ---------------------- | ------------------------------------ |
|     |     | and flight safety | path divergences in    | https://ops.group/blog/gps-spoofing- |
update-08nov2023/
airspace along the Iran  https://gcmap.com/featured/20230929
/ Iraq border.
2023-09-06 KIA Motors USA Discrete  R Unknown 1 I3 Shut down  A 3rd party data and  https://icsstrive.com/incident/kia-motors-
Mfg. production for 1  services provider to  ga-plant-hit-in-cyber-incident/
|     |     | day: disrupted  | KIA was hit by  |     |
| --- | --- | --------------- | --------------- | --- |
https://wrbl.com/news/cybersecurity-
|     |     | shifts and  | ransomware, which    | incident-disrupting-kia-production-in-west- |
| --- | --- | ----------- | -------------------- | ------------------------------------------- |
|     |     | deliveries  | halted and canceled  |                                             |
point-georgia/
|     |     |     | the first and second     |                                          |
| --- | --- | --- | ------------------------ | ---------------------------------------- |
|     |     |     | shifts at KIA's Georgia  | https://lagrangenews.com/2023/09/06/kia  |
|     |     |     | plant.                   | -hack-temporarily-shuts-down-production/ |
51

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor | Actor Attack  | Physical  |     |     |
| --- | ----- | ------------- | --------- | --- | --- |
Type Consequences
2023-09-08 MGM Resorts USA Bldg.  R ALPHV/Sc 19 $110M IA Shut down ops  Attackers gained initial  https://icsstrive.com/incident/mgm-
Automation attered  for 10 days,  access through by social  shuts-down-operations-for-10-days-
across-las-vegas-properties/
|     |     | Spider | including phys.  | engineering a help desk  |     |
| --- | --- | ------ | ---------------- | ------------------------ | --- |
|     |     |        | access and       | operator, then           |     |
https://thedeepdive.ca/mgm-resorts-
|     |     |     | phones, to all  | subsequently encrypting  | battles-ongoing-cyberattack- |
| --- | --- | --- | --------------- | ------------------------ | ---------------------------- |
|     |     |     | MGM Resort      | up to 100 Vmware ESXi    |                              |
disruption-scattered-spider-claims-
|     |     |     | properties in  | servers. After discovering  | responsibility/ |
| --- | --- | --- | -------------- | --------------------------- | --------------- |
|     |     |     | Vegas          | signs of intrusion on Sep   |                 |
10, MGM chose to contain https://apnews.com/article/mgm-
|     |     |     |     | and isolate many  | cyberattack-las-vegas-100-million- |
| --- | --- | --- | --- | ----------------- | ---------------------------------- |
clorox-
|     |     |     |     | systems, exacerbating  | 087726961b5366065b6231d1d223b4eb |
| --- | --- | --- | --- | ---------------------- | -------------------------------- |
the situation. Guests

|     |     |     |     | reported that hotel room  | https://blog.morphisec.com/mgm- |
| --- | --- | --- | --- | ------------------------- | ------------------------------- |
locks were unsecured and resorts-alphv-spider-ransomware-
|     |     |     |     | telephones inoperable. | attack |
| --- | --- | --- | --- | ---------------------- | ------ |
2023-09-10 ALPS Alpine  USA Discrete  R Blackbyte 2 IA Partially  ALPS' North American  https://icsstrive.com/incident/operatio
nal-impact-at-electronics-company-
| Co. Ltd. | Mfg. |     | impacted North   | production operations  |                                     |
| -------- | ---- | --- | ---------------- | ---------------------- | ----------------------------------- |
|          |      |     | American         | and delivery were      | alps-alpine-group/                  |
|          |      |     | production and   | impacted by a          | https://www.alpsalpine.com/cms.medi |
|          |      |     | shipping for 2+  | ransomware incident.   |                                     |
a/September_12th_Cyber_Attack_ver1
|     |     |     | days | When they discovered the  | _11_31306d3123.pdf |
| --- | --- | --- | ---- | ------------------------- | ------------------ |
breach, they took steps to
https://www.alpsalpine.com/cms.medi
isolate systems from the
|     |     |     |     | network and began  | a/September_14th_Cyber_Attack_ver0 |
| --- | --- | --- | --- | ------------------ | ---------------------------------- |
_7_5d102b80e5.pdf
restoration.
https://redpacketsecurity.com/blackby
te-ransomware-victim-alps-alpine/
2023-09-14 Canada  Canada Transport H NoName0 10 DO Shut down  La Presse reported that  https://icsstrive.com/incident/borderch
Border  57(16) automated  the automated kiosk  eck-point-outages-in-canada/

| Services  |     |     | border arrival  | systems should be on a  |     |
| --------- | --- | --- | --------------- | ----------------------- | --- |
Agency  check-in kiosks  closed circuit and not  https://lapresse.ca/actualites/2023-09-
18/une-attaque-informatique-
(CBSA) at multiple  connected to the internet. revendiquee-contre-l-agence-des-
|     |     |     | Canadian  | Nevertheless, the attack  |     |
| --- | --- | --- | --------- | ------------------------- | --- |
services-frontaliers.php
|     |     |     | airports for a  | caused significant real- |                                    |
| --- | --- | --- | --------------- | ------------------------ | ---------------------------------- |
|     |     |     | "few hours"     | world delays and wait    | https://thecyberexpress.com/cyber- |
attacks-on-canadian-airports-disrupt-
|     |     |     | causing                                | times at heavily  |                                         |
| --- | --- | --- | -------------------------------------- | ----------------- | --------------------------------------- |
|     |     |     | significant delays automated Canadian  |                   | ops/                                    |
|     |     |     | in processing                          | airports.         | https://lapresse.ca/actualites/national |
travellers
/2023-09-19/agence-des-services-
frontaliers/la-panne-dans-les-
aeroports-provenait-bien-d-une-
attaque-informatique.php
2023-09-18 Somagic France Discrete  R MedusaLo 1 ID Shut down  Employees were surprised https://icsstrive.com/incident/operatio
Mfg. cker production when they showed up at  nal-impact-at-electronics-company-
|     |     |     |     | work on Monday morning  | alps-alpine-group/ |
| --- | --- | --- | --- | ----------------------- | ------------------ |

only to discover all their IT
|     |     |     |     | systems were rendered  | https://csidb.net/csidb/incidents/8182c |
| --- | --- | --- | --- | ---------------------- | --------------------------------------- |
50d-ec4b-4cc9-8ecb-d589e8563b69/
|     |     |     |     | unusable and encrypted,  |                                       |
| --- | --- | --- | --- | ------------------------ | ------------------------------------- |
|     |     |     |     | halting production.      | https://lejsl.com/economie/2023/09/21 |
/l-entreprise-bressane-somagic-
victime-d-une-cyberattaque-de-grande-
ampleur
https://redpacketsecurity.com/medusa
locker-ransomware-victim-somagic/
2023-09-23 Johnson  USA Discrete  R Dark  6 $27M SEC ID Shut down  VMWare ESXi encryptor  https://icsstrive.com/incident/massive-
ransomware-attack-at-johnson-
Controls and  Mfg. Angels manufacturing  malware, designed to
| subsidiaries  |     |     | and disrupted  | spread through a  | controls/ |
| ------------- | --- | --- | -------------- | ----------------- | --------- |
York, Tyco,  operations,  compromised Windows  https://bleepingcomputer.com/news/s
| Coleman,  |     |     | weakened US  | AD server, infected  |     |
| --------- | --- | --- | ------------ | -------------------- | --- |
ecurity/building-automation-giant-
Ruskin, and  DHS physical  interconnected IT systems johnson-controls-hit-by-ransomware-
| Simplex |     |     | security | at Johnson Controls and  | attack/ |
| ------- | --- | --- | -------- | ------------------------ | ------- |

subsidiaries. This
|     |     |     |     | prompted Johnson to  | https://cnn.com/2023/09/28/politics/d |
| --- | --- | --- | --- | -------------------- | ------------------------------------- |
hs-investigating-ransomware-
|     |     |     |     | make 3 SEC filings, and  | attack/index.html |
| --- | --- | --- | --- | ------------------------ | ----------------- |
lead to a DHS

|     |     |     |     | investigation to examine  | https://reddit.com/r/HVAC/comments/ |
| --- | --- | --- | --- | ------------------------- | ----------------------------------- |
|     |     |     |     | claims that federal       | 16t2876/comment/k2cwwvl             |
building's schematics and
security info were leaked.
52

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2023-09-28 Leonardo Russia Transport H IT Army  227 DS Delayed flights  A massive DDoS attack on https://icsstrive.com/incident/dodds-
(Ukraine) at 3 Russian  the Leonardo online  attack-at-russian-flight-booking-
system-leonardo-disrupts-airports/
|     | carriers at                                     | booking system, used by  |     |
| --- | ----------------------------------------------- | ------------------------ | --- |
|     | Airports in Russia, 50 air carriers in Russia,  |                          |     |
https://therecord.media/russia-flight-
|     | up to 1 hour | caused delays of up to 1  | booking-system-leonardo-ddos |
| --- | ------------ | ------------------------- | ---------------------------- |
hour in Moscow. Big air
carriers include Rossiya,
Pobeda, and Aeroflot.
2023-10-10 Simpson  USA Discrete  U Unknown 1 SEC IA Caused "wide  After the building  https://icsstrive.com/incident/simpson-
manufacturing-a-building-materials-
Manufacturing Mfg. scale disruption"  materials manufacturer
|     | to operations for  | realized their IT network  | maker-attacked/                     |
| --- | ------------------ | -------------------------- | ----------------------------------- |
|     | 3 days             | problems were in fact a    | https://bleepingcomputer.com/news/s |
cyberattack, the
ecurity/simpson-manufacturing-shuts-
|     |     | manufacturer chose to  | down-it-systems-after-cyberattack/ |
| --- | --- | ---------------------- | ---------------------------------- |
shutdown systems and
https://ir.simpsonmfg.com/financials/s
ops and begin
|     |     | remediation. | ec-filings/sec-filings- |
| --- | --- | ------------ | ----------------------- |
details/default.aspx?FilingId=16995846
2023-10-14 Henry Schein USA Discrete  R ALPHV /  1 $500M SEC U Up to three  Henry Schein's operations  https://icsstrive.com/incident/cyber-
Mfg. BlackCat ransomware  were encrypted on three  incident-at-healthcare-solutions-giant-
henry-schein/
|     | attacks    | separate occasions by a  |     |
| --- | ---------- | ------------------------ | --- |
|     | encrypted  | ransomware gang. First   |     |
https://www.bleepingcomputer.com/ne
|     | systems and  | initially, then by Nov. 3 as  | ws/security/henry-schein-discloses- |
| --- | ------------ | ----------------------------- | ----------------------------------- |
|     | impacted     | negotiations faltered,        |                                     |
data-breach-a-year-after-ransomware-
|     | manufacturing      | then a third time on Nov.  | attack                              |
| --- | ------------------ | -------------------------- | ----------------------------------- |
|     | and distribution   | 22, just as systems were   |                                     |
|     | operations for 3+  | nearing full restoration.  | https://www.bleepingcomputer.com/ne |
|     | months             |                            | ws/security/healthcare-giant-henry- |
schein-hit-twice-by-blackcat-
ransomware

https://cybernews.com/news/alphv-
blackcat-re-encrypt-henry-schein-
ransom-negotiations-third-time-
2023-10-16 10+ Civilian  Egypt Transport U Unknown 10 DO Loss of  (Similar to 2023-8-29  https://icsstrive.com/incident/wide-
and private  navigation,  incident) A novel type of  concern-over-gps-spoofing-incidents-
Jets diverted aircraft  GPS and IRS signal  previously-thought-to-be-impossible-in-
middle-east/
|     | from intended  | spoofing attack caused 10  |     |
| --- | -------------- | -------------------------- | --- |
|     | path into      | aircraft to suffer         |     |
https://ops.group/blog/gps-spoofing-
|     | restricted or  | complete loss of          | update-08nov2023/                      |
| --- | -------------- | ------------------------- | -------------------------------------- |
|     | dangerous      | navigational capability,  |                                        |
|     | airspace, &    | caused unintended flight  | https://www.forbes.com/sites/erictegle |
r/2023/12/05/gps-spoofing-in-the-
|     | endangered lives  | path divergences over  | middle-east-is-now-capturing- |
| --- | ----------------- | ---------------------- | ----------------------------- |
|     | and flight safety | Cairo.                 |                               |
avionics/?sh=6550d5c23a6f
https://www.businessinsurance.com/H
enry-Schein-cuts-annual-profit-
forecast-as-cyberattack-impact-
lingers/
2023-10-25 4+ Civilian and  Israel Transport U Unknown 4 DO Loss of  (Similar to 2023-8-29  https://icsstrive.com/incident/wide-
concern-over-gps-spoofing-incidents-
| private Jets | navigation,        | incident) A novel type of  |                                         |
| ------------ | ------------------ | -------------------------- | --------------------------------------- |
|              | diverted aircraft  | GPS and IRS signal         | previously-thought-to-be-impossible-in- |
middle-east/
|     | from intended  | spoofing attack caused 4  |     |
| --- | -------------- | ------------------------- | --- |
|     | path into      | aircraft to suffer        |     |
https://ops.group/blog/gps-spoofing-
|     | restricted or  | complete loss of         | update-08nov2023/ |
| --- | -------------- | ------------------------ | ----------------- |
|     | dangerous      | navigational capability  |                   |
https://www.forbes.com/sites/erictegle
|     | airspace, &       | and caused unintended    |                                   |
| --- | ----------------- | ------------------------ | --------------------------------- |
|     | endangered lives  | flight path divergences  | r/2023/12/05/gps-spoofing-in-the- |
middle-east-is-now-capturing-
|     | and flight safety | over Israel, Lebanon, and  | avionics/?sh=6550d5c23a6f |
| --- | ----------------- | -------------------------- | ------------------------- |
Jordan.
2023-10-30 Ace Hardware USA Transport U Unknown 17 ID Shut down order  Ace Hardware's  https://icsstrive.com/incident/cyberatt
|     | fulfilment and  | warehousing was hit by a  | ack-cripples-operations-at-ace- |
| --- | --------------- | ------------------------- | ------------------------------- |
|     | warehouse       | cyberattack that had a    | hardware-in-us                  |

|     | distribution  | wide-ranging impact on  |                                      |
| --- | ------------- | ----------------------- | ------------------------------------ |
|     | operations    | the company including   | https://www.theregister.com/2023/10/ |
31/ace_hardware_cyberattack/
|     | company-wide,    | warehouse managing   |                                      |
| --- | ---------------- | -------------------- | ------------------------------------ |
|     | sent workers     | systems and other    | https://www.reddit.com/r/sysadmin/co |
|     | home for over a  | software crucial to  | mments/17jwvtz/ace_hardware_corp_    |
cybersecurity_incident_10302023/
|     | week | physical ops. |     |
| --- | ---- | ------------- | --- |
https://www.bleepingcomputer.com/ne
ws/security/ace-hardware-says-1-202-
devices-were-hit-during-cyberattack/
53

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor | Actor Attack  | Physical  |     |     |
| ----- | ------------- | --------- | --- | --- |
Type Consequences
2023-11-01 Bircher  Switzerland Food &  R Unknown 1 6K Fr. I3 Caused livestock  The third-party company  https://icsstrive.com/incident/small-
Farm Bev. loss (death) of  that supplies robotic  swiss-farmer-refuses-to-pay-
ransomware/
|     |     | one animal (1  | milking machines also       |     |
| --- | --- | -------------- | --------------------------- | --- |
|     |     | cow)           | monitors the cattle herd's  |     |
https://www.csoonline.com/article/3
|     |     |     | health. As this third-party  | 484349/ransomware-attack- |
| --- | --- | --- | ---------------------------- | ------------------------- |
was compromised by
paralyzes-milking-robots-cow-
|     |     |     | ransomware, it was  | dead.html |
| --- | --- | --- | ------------------- | --------- |
encrypted and stopped
https://www.schweizerbauer.ch/politi
operating. Even though the
|     |     |     | milking machine at Val  | k-  |
| --- | --- | --- | ----------------------- | --- |
wirtschaft/betriebsfuehrung/gehackt
|     |     |     | Bircher's farm were  | er-melkroboter-loesegeldforderung- |
| --- | --- | --- | -------------------- | ---------------------------------- |
switched to manual
und-eine-tote-kuh
operation, an alarm failed
to alert to a pregnant cow
that had a calf die in her
womb. The cow was unable
to be saved and had to be
put down by a vet.
2023-11-10 DP World  Australia Transport U Unknown 4 >$1M IA Shut down 4  Ports pre-emptively  https://icsstrive.com/incident/cyberat
Australia ports in Australia  disconnected systems from tack-crippled-facilities-of-large-
the internet, which stopped australia-port-operator/
|     |     | for 3 days:  |                        |     |
| --- | --- | ------------ | ---------------------- | --- |
|     |     | Melbourne,   | the initial attack on  |     |
https://msn.com/en-
|     |     | Freemantle,                                | Australian port ops. This  | ae/news/world/dp-world-australia- |
| --- | --- | ------------------------------------------ | -------------------------- | --------------------------------- |
|     |     | Botany, Brisbane; resulted in operational  |                            | makes-significant-progress-to-    |
|     |     | caused 10-day                              | downtime. No trace of      | restore-operations-after-cyber-   |
|     |     | backlog of 30K                             | ransomware was found in    | attack/ar-AA1jMEHJ                |

|     |     | containers | systems and the incident  |                                    |
| --- | --- | ---------- | ------------------------- | ---------------------------------- |
|     |     |            | investigation continues.  | https://theguardian.com/australia- |
news/2023/nov/13/australian-port-
operator-hit-by-cyber-attack-says-
cargo-may-be-stranded-for-days
https://reuters.com/technology/cybe
rsecurity/dp-world-says-hackers-
stole-australian-ports-employee-
data-2023-11-28/
2023-11-15 Stellantis / USA,  Discrete  U Qlin 4 $26M I3 Disrupted  Stellantis manufacturing  https://icsstrive.com/incident/yanfen
Yanfeng  Mexico Mfg. Stellantis'  plants shut down after a  g-cyberattack-disrupts-production-
at-stellantis/
| Automotiv   |     | production of  | cyberattack hit their        |     |
| ----------- | --- | -------------- | ---------------------------- | --- |
| e Interiors |     | Jeep and RAM   | external supplier Yangfeng,  |     |
https://automotivelogistics.media/oe
|     |     | trucks at 3 plants a vehicle interior  |     | ms/yanfeng-cyberattack-disrupts- |
| --- | --- | -------------------------------------- | --- | -------------------------------- |
in Detroit and 1 in manufacturer. In April '24,
production-at-stellantis/44893.article
|     |     | Mexico, due to  | Stellantis demanded       |                                      |
| --- | --- | --------------- | ------------------------- | ------------------------------------ |
|     |     | lack of parts   | millions in damages from  | https://carscoops.com/2023/11/stella |
ntis-production-disrupted-after-
|     |     | supplied from  | supplier Yanfeng over the  |                                  |
| --- | --- | -------------- | -------------------------- | -------------------------------- |
|     |     | Yanfeng        | incident and related       | cyberattack-on-chinese-interior- |
supplier/
|     |     |     | shutdown, which kicked off  |     |
| --- | --- | --- | --------------------------- | --- |
a bitter contract dispute
https://carscoops.com/2024/04/stell
|     |     |     | between the two parties. | antis-demands-26m-in-damages- |
| --- | --- | --- | ------------------------ | ----------------------------- |
from-chinese-supplier-sparking-
lawsuit
2023-11-30 Drum /  Ireland Water NS CyberAv3n 1 DS Shut down water  Residents lost water after  https://icsstrive.com/incident/pro-
Binghamst gers (Iran)  distribution to  an attack on Unitronics  iran-hackers-cut-water-supply-for-2-
own Group  / Islamic  180 residents for  water pump controllers at  days-in-remote-irish-town/
| Water  | Revolution | 2 days | a local station. The Erris  |     |
| ------ | ---------- | ------ | --------------------------- | --- |
Scheme  ary Guard  area utility said they did  https://westernpeople.ie/news/hacke
rs-hit-erris-water-in-stance-over-
| Co-        | Corps  |     | not have the budget for        | israel_arid-4982.html |
| ---------- | ------ | --- | ------------------------------ | --------------------- |
| Operative  | (IRGC) |     | cybersecurity like firewalls,  |                       |
Society and that after the attack,  https://securityweek.com/cyberattac
|     |     |     | they struggled to bypass  | k-on-irish-utility-cuts-off-water- |
| --- | --- | --- | ------------------------- | ---------------------------------- |
supply-for-two-days/
the pump to run manually,
leading to the outage.
2023-12-07 Serwis  Poland Transport SC Newag SA 1 DSC Impaired  After SPS was contracted  https://icsstrive.com/incident/polish-
Pojazdów  operations:  to maintain rolling stock for train-builder-denies-sabotaging-plc-
code/
| Szynowych  |     | Sabotaged      | operator Koleje     |     |
| ---------- | --- | -------------- | ------------------- | --- |
| (SPS)      |     | rolling stock  | Dolnośląskie, they  |     |
https://theregister.com/2023/12/08/p
when serviced by discovered deliberate code olish_trains_geofenced_allegation/
|     |     | third-party  | in firmware designed to  |     |
| --- | --- | ------------ | ------------------------ | --- |

|     |     | workshops | "brick" controllers, planted  | https://badcyber.com/dieselgate- |
| --- | --- | --------- | ----------------------------- | -------------------------------- |
|     |     |           | by the manufacturer           | but-for-trains-some-heavyweight- |
hardware-hacking/
Newag, to enforce vendor
maintenance lock-in.
54

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor | Actor Attack  | Physical  |     |     |
| ----- | ------------- | --------- | --- | --- |
Type Consequences
2023-12-13 Erfo Germany Discrete  U Unknown 1 Bankru U Shut down  This textile fashion brand  https://icsstrive.com/incident/hackers
Mfg. pt production and  and manufacturer reported -paralyzed-operations-of-textile-
manufacturer-erfo/
|     |     | filed for  | that a cyber attack          |     |
| --- | --- | ---------- | ---------------------------- | --- |
|     |     | bankruptcy | impacted not only IT but OT  |     |
https://www.csoonline.com/article/3
|     |     |     | systems, impacting  | 495589/erfohackerangriff-fuhrt-zu- |
| --- | --- | --- | ------------------- | ---------------------------------- |
production. The impacts
insolvenz-bei-textilkonzern.html
were so severe, they
pushed the brand to file for
insolvency with local courts
and seek out new
investment to continue
operating.
2023-12-17 Socadis Canada Transport U Unknown 1 IA Halted deliveries  The company was a victim  https://icsstrive.com/incident/large-
|     |     | and distribution,  | of a spear phishing attack  | canadian-book-distributor-suspends- |
| --- | --- | ------------------ | --------------------------- | ----------------------------------- |
operations-after-cyberattack/
|     |     | 4+ days | and isolated all systems to  |     |
| --- | --- | ------- | ---------------------------- | --- |
avoid spreading the
https://ledevoir.com/economie/80416
|     |     |     | malware to industry  | 2/informatique-cyberattaque-      |
| --- | --- | --- | -------------------- | --------------------------------- |
|     |     |     | partners.            | paralyse-maillon-important-livre- |
quebecois?

https://lapresse.ca/arts/litterature/2
023-12-20/probleme-de-
cybersecurite/les-activites-du-
distributeur-de-livres-socadis-sur-
pause.php

https://facebook.com/socadis/posts/
831533385645938?ref=embed_post
2023-12-18 Iranian  Iran Oil & Gas H Predatory  2150 DO Disrupted 70% of  Predatory Sparrow took  https://icsstrive.com/incident/iranian-
petrol-stations-hit-by-cyberattack/
| Gas      | Sparrow   | national gas  | responsibility for another  |     |
| -------- | --------- | ------------- | --------------------------- | --- |
| Stations | (Gonjeshk | stations      | attack on most gas          |     |
https://bbc.com/persian/articles/c51
|     | e Darande) |     | stations in Iran (different  | zv8ek8vxo |
| --- | ---------- | --- | ---------------------------- | --------- |
from the last one in 2021).

|     |     |     | Analysis by DarkCell AB   | https://reuters.com/world/middle- |
| --- | --- | --- | ------------------------- | --------------------------------- |
|     |     |     | suggest that this recent  | east/software-problem-disrupts-   |
attack is remarkably similar iranian-gas-stations-fars-2023-12-18/
except the attack vector
https://sites.google.com/darkcell.se/
|     |     |     | and entry point are  | www/sparrows |
| --- | --- | --- | -------------------- | ------------ |
different.
2023-12-18 Yusen  Japan Transport R ALPHV /  2 ID Delayed delivery;  Reported a "major problem  https://icsstrive.com/incident/cyberat
Logistics BlackCat impacted  with IT infrastructure" after  tack-at-yusen-logistics-partner-of-
big-kitchen-manufacturers-spells-
|     |     | logistics and    | an attack impacted       | delays-for-applicance-retailers/ |
| --- | --- | ---------------- | ------------------------ | -------------------------------- |
|     |     | partner BSH (UK) | invoicing and delivery.  |                                  |

|     |     |     | Home appliance retailer      | https://kbbreview.com/56802/news/a    |
| --- | --- | --- | ---------------------------- | ------------------------------------- |
|     |     |     | BSH, a Yusen partner in the  | ppliance-delivery-woes-return-big-    |
|     |     |     | UK, was similarly impacted.  | brands-as-tech-glitch-hits-logistics- |
partner/

https://kbbreview.com/56927/news/a
ppliance-supplier-confirms-delays-
due-to-cyber-attack/
https://ransomwareattacks.halcyon.a
i/attacks/blackcat-alphv-attacks-
yusen-logistics
55

Incidents in 2022
Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack Physical
Type Consequences
2022-01-07 CPH Chemie & Switzerland,  Process  R Unknown 1 IA 6 days of  Newsprint, packaging, and https://icsstrive.com/incident/hackers-
Papier Holding Germany Mfg. downtime; lost  lightweight coated paper  paralyze-only-newsprinting-facility-in-
|     |     | 8,400 tons in  | (LWC) producer in Perlen  | switzerland/ |
| --- | --- | -------------- | ------------------------- | ------------ |
|     |     | paper output   | and Müllheim was forced   |              |
https://euwid-
into a controlled shutdown paper.com/news/markets/cph-to-
|     |     |     | after a cyberattack. | restart-operations-in-perlen-and- |
| --- | --- | --- | -------------------- | --------------------------------- |
muellheim-by-tomorrow

https://www.pulpapernews.com/20220
111/13176/cyber-attack-it-systems-cph-
group
2022-01-28 Kenyon  UK Food &  R Conti 1 ID Halted  Hit by Conti ransomware,  https://icsstrive.com/incident/uk-
snack-provider-hit-by-ransomware-
| Produce (KP)  | Bev. | production,       | the snack maker "cannot   |                                      |
| ------------- | ---- | ----------------- | ------------------------- | ------------------------------------ |
| Snacks        |      | delayed           | safely process orders or  | attack/                              |
|               |      | deliveries for 2  | dispatch goods." Orders   | https://foodprocessing.com/industryn |
|               |      | months, &         | were capped while         |                                      |
ews/2022/hackers-cripple-kp-snacks
|     |     | capped orders | existing stocks consumed. |     |
| --- | --- | ------------- | ------------------------- | --- |
2022-01-29 Marquard &  Germany Oil & Gas R ALPHV /  11 U Declared force  BlackCat (ALPHV)  https://icsstrive.com/incident/german-
Bahls  BlackCat majeure, halted  ransomware halted  oil-tank-farm-shut-down/
| subsidiaries  |     | operations for 2  | loading and unloading of  |     |
| ------------- | --- | ----------------- | ------------------------- | --- |
https://bbc.com/news/technology-
| Mabanaft &  |     | weeks | fuel and bulk oil at port  |          |
| ----------- | --- | ----- | -------------------------- | -------- |
| Oiltanking  |     |       | and had a minor impact on  | 60215252 |
automotive fuel
distribution in Germany.
2022-01-30 SEA-Tank &  Belgium,  Oil & Gas R ALPHV /  24 U Halted  Every SEA-Tank or SEA- https://isssource.com/oil-terminals-in-
SEA-Invest  Africa BlackCat operations at all  Invest port terminal in  europe-suffer-cyberattack
| Group |     | European and  | Europe and Africa could   |     |
| ----- | --- | ------------- | ------------------------- | --- |
|       |     | African ports | not unload fuel due to a  |     |
reported BlackCat
(ALPHV) ransomware
attack.
2022-02-02 Evos Group Malta,  Oil & Gas U Unknown 3 U Delayed  Cyberattack delayed  https://icsstrive.com/incident/malta-
Belgium,  unloading fuel at  loading and unloading of  oil-terminal-run-by-evos-one-of-
fuel and bulk oil at port for several-european-facilities-hit-by-a-
Netherlands 3 ports:
|     |     | Terneuzen,  | the storage logistics  | cyberattack/                          |
| --- | --- | ----------- | ---------------------- | ------------------------------------- |
|     |     | Ghent, and  | company. The Malta     | https://insurancejournal.com/news/int |
|     |     | Birzebbuga  | operation was just     | ernational/2022/02/03/652169.htm      |
recently acquired from
Oiltanking.
2022-02-03 Swissport Switzerland Transport R ALPHV /  1 ID Delayed 22  BlackCat (ALPHV)  https://icsstrive.com/incident/ransom
BlackCat flights, cargo,  ransomware attack forced ware-attack-at-swiss-airport-services-
|     |     | and freight      | Swissport to revert to  | firm                                  |
| --- | --- | ---------------- | ----------------------- | ------------------------------------- |
|     |     | services for 20  | manual ops and backup   |                                       |
|     |     | min              | procedures.             | https://spiegel.de/netzwelt/web/swiss |
port-hackerangriff-stoert-zeitweise-
flugbetrieb-in-der-schweiz-a-
44285ac8-ad73-42ea-b751-
91559c2ff4c8
2022-02-21 Jawaharlal  India Transport R Unknown 1 ID Diverted  Management Information  https://icsstrive.com/incident/ransom
Nehru Port  incoming vessels  System (MIS) knocked out  ware-attack-cripples-indian-port-
container-terminal-jncpt/
| Container  |     | and halted in- | by ransomware at JNPCT,  |     |
| ---------- | --- | -------------- | ------------------------ | --- |
| Terminal   |     | progress       | one of five marine       |     |
https://theloadstar.com/ransomware-
(JNPCT) loading/unloadin facilities at the Nhava  attack-hits-nhava-sheva-container-
|     |     | g at port | Sheva container gateway. | terminal |
| --- | --- | --------- | ------------------------ | -------- |
2022-02-22 Expeditors USA Transport R Unknown 1 $60M ID Shut down  Cannot ship freight or  https://icsstrive.com/incident/expedito
|     |     | operations for 3+  | manage customs       | rs-intl-hit-by-ransomware-attack/ |
| --- | --- | ------------------ | -------------------- | --------------------------------- |
|     |     | weeks              | processing, thereby  |                                   |
https://bleepingcomputer.com/news/s
|     |     |     | halting ops. The financial  | ecurity/expeditors-shuts-down-global- |
| --- | --- | --- | --------------------------- | ------------------------------------- |
cost to restore systems
operations-after-likely-ransomware-
|     |     |     | and in lost business was  | attack |
| --- | --- | --- | ------------------------- | ------ |
significant. Occurred two
days before the Invasion
of Ukraine.
56

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor | Actor Attack Physical  |     |     |     |
| --- | ----- | ---------------------- | --- | --- | --- |
Type Consequences
2022-02-24 Caledonian  UK Discrete  R Unknown 1 Bankrupt U Shut down  Modular building  https://icsstrive.com/incident/cyber
Modular Mfg. manufacturing  manufacturer's lost  attack-significantly-reduced-
production output due to the caledonian-modulars-operating-
ops.
|     |     |     |     | attack and was a major   | capability/                         |
| --- | --- | --- | --- | ------------------------ | ----------------------------------- |
|     |     |     |     | factor in the company's  | https://theconstructionindex.co.uk/ |
March insolvency. Occurred
news/view/jrl-buys-caledonian-
|     |     |     |     | the day of the Invasion of  | modular-out-of-administration |
| --- | --- | --- | --- | --------------------------- | ----------------------------- |
Ukraine.
2022-02-27 Bridgestone N. & S.  Process  R LockBit 23 IA 10 days lost  LockBit ransomware  https://icsstrive.com/incident/tire-
America Mfg. production, and  prompted the shut down all  manufacturer-bridgestone-hit-in-
|     |     |     | workers sent        | plants in the western        | ransomware-attack |
| --- | --- | --- | ------------------- | ---------------------------- | ----------------- |
|     |     |     | home, at all 23     | hemisphere, in an abundance  |                   |
|     |     |     | tire plants in the  | of caution, and begin        |                   |
|     |     |     | Americas            | recovery.                    |                   |
2022-02-28 Belarus  Belarus Transport H Cyber  1 DO Halted trains in  The Belarusian "Cyber  https://icsstrive.com/incident/belar
Railway Partisans  Minsk, Orsha, and Partisans" encrypt and  us-rail-network-disrupted-by-
|     |     | (Belarus) | Osipovichi | disable routing and switching hacktivist-group/ |     |
| --- | --- | --------- | ---------- | ----------------------------------------------- | --- |
devices, stranding trains at
|     |     |     |     | station, to slow Russian  | https://bqprime.com/amp/technolo |
| --- | --- | --- | --- | ------------------------- | -------------------------------- |
gy/belarus-hackers-allegedly-
|     |     |     |     | troops transiting to the  | disrupted-trains-to-thwart-russia |
| --- | --- | --- | --- | ------------------------- | --------------------------------- |
Ukrainian front.
2022-02-28 Toyota,  Japan Discrete  R Unknown 14 I3 Shut down all  When 3rd party supplier  https://isssource.com/toyota-halts-
production-after-cyberattack-on-
| Hino,  | Mfg. |     | Japanese auto  | Kojima was hit by  |     |
| ------ | ---- | --- | -------------- | ------------------ | --- |
Daihatsu,  and truck plants  ransomware, Toyota chose  supplier
| Kojima     |     |     | for 1 day, and   | to shut down all their  |     |
| ---------- | --- | --- | ---------------- | ----------------------- | --- |
| Industries |     |     | lost production  | Japanese plants in an   |     |
|            |     |     | of 10K units     | abundance of caution.   |     |
2022-02-28 Rosetti  Russia Power H AutoEnterp 2 DO Deactivated all  Hacktivists remotely disable  https://icsstrive.com/incident/russia
Energy  rise  EV charging  all electric vehicle charging  n-electric-vehicle-chargers-hacked-
on-m11-highway-as-political-protest
|     |     | (Ukraine) | stations between stations along the M-11  |                         |                                    |
| --- | --- | --------- | ----------------------------------------- | ----------------------- | ---------------------------------- |
|     |     |           | Moscow and St.                            | motorway and reprogram  | https://www.vice.com/en/article/ru |
ssian-electric-vehicle-chargers-
|     |     |     | Petersberg | displays criticizing Russian  | hacked-tell-users-putin-is-a- |
| --- | --- | --- | ---------- | ----------------------------- | ----------------------------- |
President Putin.
dickhead/
2022-03-11 H.P. Hood  USA Food &  U Unknown 13 IA Shut down  Cyberattack prompted  https://icsstrive.com/incident/dairy-
Dairy LLC Bev. production 1  taking Hood's 13 plants  plant-operations-offline-no-milk-at-
schools-in-new-england/
|     |     |     | week, disposed      | offline in an abundance of  |     |
| --- | --- | --- | ------------------- | --------------------------- | --- |
|     |     |     | all dairy product,  | caution and could not       |     |
https://boston.com/news/local-
|     |     |     | canceled orders  | receive materials to        | news/2022/03/18/most-hood-         |
| --- | --- | --- | ---------------- | --------------------------- | ---------------------------------- |
|     |     |     | & deliveries     | manufacture dairy products. | plants-up-and-running-after-cyber- |
event
2022-03-20 ELTA  Greece Transport R Unknown 1 ID Disrupted postal  Unpatched vulnerability led  https://icsstrive.com/incident/ranso
(Hellenic  services for 17  to reverse shell &  mware-attack-halts-public-postal-
services-in-greece/
| Post) |     |     | days, nationally | ransomware deployment,  |     |
| ----- | --- | --- | ---------------- | ----------------------- | --- |
disrupting all mail, financial,
https://therecord.media/greeces-
|     |     |     |     | and bill payment services  | national-postal-service-restoring- |
| --- | --- | --- | --- | -------------------------- | ---------------------------------- |
processed through the Greek systems-after-ransomware-attack
Post.
2022-03-23 METRANS  Italy Transport R Hive/Crypt 3 U Suspended all  A ransomware attack  https://icsstrive.com/incident/wides
Rail, HUPAC,  olocker METRANS, HUPAC impacted the IT systems at  pread-fallout-after-cyberattack-
hits-italys-national-railway-
| Italian State  |     |     | and LINEAS  | Italian State Railways (FS)  |     |
| -------------- | --- | --- | ----------- | ---------------------------- | --- |
Railways  freight rail  and subsidiary Trenitalia and  company/
(FS), Italian  operations in  Italian Rail Network (RFI),  https://www.railjournal.com/infrastr
| Rail  |     |     | Italy 1 day | disrupting ticket sales,  |     |
| ----- | --- | --- | ----------- | ------------------------- | --- |
ucture/italian-railway-it-system-
| Network  |     |     |     | passenger information     | suffers-major-cyber-attack/ |
| -------- | --- | --- | --- | ------------------------- | --------------------------- |
| (RFI)    |     |     |     | screens, and tablets for  |                             |
https://metrans.eu/hacker-attack-
railway staff. As a result,
|     |     |     |     | Tenitalia shut down IT  | on-the-italian-railway- |
| --- | --- | --- | --- | ----------------------- | ----------------------- |
infrastructure/
services, but passenger train
services remained
https://www.railfreight.com/railfrei
|     |     |     |     | operational. However,  | ght/2022/03/25/cyber-attack-on- |
| --- | --- | --- | --- | ---------------------- | ------------------------------- |
|     |     |     |     | Czech-based freight    | italian-railway-company-stops-  |
traffic
operator METRANS said this
caused the suspension of all
their Italian train operations.
HUPAC and LINEAS also said
their rail freight ops. were
suspended for 24 hours.
57

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack  Physical
Type Consequences
2022-03-24 TAVR  Russia Food &  U Unknown 1 U Shut down  TAVR makes 50K tons of  https://icsstrive.com/incident/opera
Corporate  Bev. production and  meat and sausage in Rostov- tional-impact-after-cyberattack-at-
tavr-food-processing-group-in-
| Group | recorded a     | on-don, close to the Ukraine  |        |
| ----- | -------------- | ----------------------------- | ------ |
|       | "significant   | border. A rep assessed the    | russia |
|       | economic loss" | event as “meticulously        |        |
planned and significant
sabotage.”
2022-04-16 Bulgarian  Bulgaria Transport R Unknown 1 DIP 2+ week outage  Russian-originated  https://icsstrive.com/incident/comp
lete-state-postal-system-outage-in-
| State Post  | of 26 national    | ransomware attack to the    |                                      |
| ----------- | ----------------- | --------------------------- | ------------------------------------ |
| Office      | postal services,  | Bulgarian Post, where       | bulgaria/                            |
|             | including         | attackers moved laterally   | https://euractiv.com/section/politic |
|             | deliveries        | into all IT and OT systems  |                                      |
s/short_news/russian-style-hackers-
|     |     | affecting all 26 offered  | ruin-bulgarian-post-office |
| --- | --- | ------------------------- | -------------------------- |
services.
2022-04-17 Costa  Costa Rica Transport R Conti &  1 ID Slowed  Small part of a massive  https://icsstrive.com/incident/costa
Rican  Hive shipments for > 1  Conti and Hive ransomware  -rica-declares-national-emergency-
Customs  month, and shut  attack on Costa Rica's  in-response-to-ransomware-attack/

Service down Customs'  government, and container  https://fas.usda.gov/data/costa-
|     | systems | freight shipments to slow to  |     |
| --- | ------- | ----------------------------- | --- |
rica-costa-rica-customs-delays-
|     |     | a trickle at the port of Limón. | affect-imports |
| --- | --- | ------------------------------- | -------------- |
2022-04-18 Sunwing  Canada Transport U Unknown 1 ID Shut down  Discount holiday carrier's  https://icsstrive.com/incident/check
-in-systems-offline-for-days-at-
| Airlines | check-in                                | passengers stranded during  |                   |
| -------- | --------------------------------------- | --------------------------- | ----------------- |
|          | systems, delay or the busy Easter long  |                             | sunwing-airlines/ |

|     | cancel 188 flights | weekend, where “a system  | https://infosecurity- |
| --- | ------------------ | ------------------------- | --------------------- |
that is running all the time,
magazine.com/news/cyberattacker
|     |     | which never fails, was  | s-hit-sunwing-airlines |
| --- | --- | ----------------------- | ---------------------- |
hacked."
2022-05-05 AGCO USA &  Discrete  R Unknown 1 ID Shut down maj.  Attack on major tractor and  https://icsstrive.com/incident/ranso
Europe Mfg. of production in  equipment manufacturer  mware-attack-at-agco/
|     | for 15+ days, and  | occurs at the start of  |     |
| --- | ------------------ | ----------------------- | --- |
https://theregister.com/2022/05/09
|     | sent workers  | planting season, during peak  | /farm_machinery_giant_agco_hit |
| --- | ------------- | ----------------------------- | ------------------------------ |
|     | home          | global demand for new         |                                |
equipment and parts from
dealers.
2022-05-25 SpiceJet India Transport R Unknown 1 ID Grounded or  Attempted ransomware  https://icsstrive.com/incident/spicej
|     | delayed planes  | attack on SpiceJet caused  | ets-low-cost-airline-in-india-   |
| --- | --------------- | -------------------------- | -------------------------------- |
|     | for 5+ hours    | major delays for air       | systems-and-operations-impacted- |
by-ransomware-attack
travellers, causing a
cascading effect on future
flight schedules.
2022-05-31 Foxconn  Mexico Discrete  R LockBit 1 U Disrupted  LockBit gang ransomed the  https://icsstrive.com/incident/foxco
Baja  Mfg. production for 2  plant in Tijuana, which  nn-hit-in-ransomware-attack-for-
California weeks, & forced  supplies most of California's  second-time/

|     | production  | brand-labeled consumer      | https://therecord.media/foxconn- |
| --- | ----------- | --------------------------- | -------------------------------- |
|     | capacity    | electronics. 2nd time in 2  |                                  |
mexico-factory-operations-
|     | adjustment | years this plant was hit by  | gradually-returning-to-normal-after- |
| --- | ---------- | ---------------------------- | ------------------------------------ |
|     |            | ransomware.                  | ransomware-attack                    |
2022-05-31 CMC  Canada Discrete  R ALPHV/Unk 1 IA Disrupted and  ALPHV ransomware  https://icsstrive.com/incident/alphv
Electronics Mfg. nown delayed ops. encrypted systems and  -ransomware-gang-attacks-
|     |     | "disrupted operations" to a  | canadian-defense-contractor/ |
| --- | --- | ---------------------------- | ---------------------------- |
key supplier of avionics of
|     |     | Canada's Department of  | https://itworldcanada.com/article/ |
| --- | --- | ----------------------- | ---------------------------------- |
canadian-military-provider-suffered-
|     |     | National Defense. | ransom-attack-says-news- |
| --- | --- | ----------------- | ------------------------ |
report/487654
2022-06-22 Yodel UK Transport U Unknown 1 ID Delayed parcel  Suspected but unconfirmed  https://icsstrive.com/incident/millio
|     | delivery for  | ransomware attack shuts       | ns-of-yodel-customers-in-uk-face- |
| --- | ------------- | ----------------------------- | --------------------------------- |
|     | millions of   | down critical operations,     | parcel-delivery-delays/           |
|     | customers     | including delivery tracking,  | https://bleepingcomputer.com/new  |
for millions awaiting home
s/security/yodel-parcel-company-
|     |     | delivery of goods and  | confirms-cyberattack-is-disrupting- |
| --- | --- | ---------------------- | ----------------------------------- |
|     |     | services.              | delivery                            |
2022-06-25 Apetito  UK Food &  R Hive 1 ID 5-day halt to  Hive ransomware hits Meals- https://icsstrive.com/incident/apeti
(Wiltshire  Bev. food deliveries,  on-wheels serving  tos-security-systems-breached-in-
Food  and rebuilt  institutions and the  sophisticated-cyberattack
| Farms   | systems | vulnerable. Apetito reverted  |     |
| ------- | ------- | ----------------------------- | --- |
| parent) |         | to manual procedures and a    |     |
complete system rebuild to
restore ops.
58

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor | Actor Attack  | Physical  |     |     |
| --- | ----- | ------------- | --------- | --- | --- |
Type Consequences
2022-06-25 Macmillan  UK, USA Transport R Unknown 2 ID Halted orders &  Ransomware attack on a  https://icsstrive.com/incident/cyber
Publishers shipments;  major publisher closed  attack-forces-macmillan-publishers-
to-take-operations-offline-and-
|     |     |     | backlogged      | offices in NYC and London,     |                        |
| --- | --- | --- | --------------- | ------------------------------ | ---------------------- |
|     |     |     | regional        | disrupting order processing,   | close-physical-offices |
|     |     |     | warehouses for  | and causing months of          |                        |
|     |     |     | months          | delivery backlogs at regional  |                        |
warehouses.
2022-06-27 Khuzestan  Iran Metals &  H Predatory  1 DO Damaged  Predatory Sparrow group  https://icsstrive.com/incident/khuze
claimed responsibility set the stan-steel-hit-in-cyber-attack-
| Steel (KSC),  | Mining | Sparrow  | equipment and  |     |     |
| ------------- | ------ | -------- | -------------- | --- | --- |
Mobarakeh  (Gonjeshk halted  KSC plant on fire and posted  production-halts/

Steel (MSC),  e Darande) production at the CCTV of the incident on  https://timesofisrael.com/large-
| &   |     |     | KSC plant. | twitter. Damage reports on  |     |
| --- | --- | --- | ---------- | --------------------------- | --- |
cyberattack-on-iranian-industrial-
Hormozgan  MSC and HOSCO remain  sector-targets-three-steel-plants
| Steel  |     |     |     | unconfirmed. |     |
| ------ | --- | --- | --- | ------------ | --- |
(HOSCO)
2022-06-29 Knauf UK Process  R BlackBasta 2 IA Shut down  After a BlackBasta  https://icsstrive.com/incident/large
Mfg. production for 3+  ransomware attack, Knauf  st-building-material-producer-
attacked-by-black-basta/
|     |     |     | weeks; Delayed  | pre-emptively shut down to  |     |
| --- | --- | --- | --------------- | --------------------------- | --- |
|     |     |     | existing and    | facilitate recovery and     |     |
https://techmonitor.ai/technology/c
|     |     |     | canceled all new  | forensics, and operated both ybersecurity/knauf-cyberattack- |     |
| --- | --- | --- | ----------------- | ------------------------------------------------------------ | --- |
|     |     |     | orders            | plants manually.                                             |     |
blackbasta-ransomware
2022-07-18 Eglo Austria Discrete  R Unknown 1 U Shut down  Lighting manufacturer's CEO  https://icsstrive.com/incident/hacke
Mfg. production, order confirmed the ransomware  rs-paralyzed-computer-system-at-
austrian-light-manufacturer-eglo/
|     |     |     | processing and   | attack but noted that no  |     |
| --- | --- | --- | ---------------- | ------------------------- | --- |
|     |     |     | shipping for 12  | ransom note had been      |     |
https://diepresse.com/6167688/tirol
|     |     |     | days | received by the time they  | er-leuchtenhersteller-eglo-von- |
| --- | --- | --- | ---- | -------------------------- | ------------------------------- |
|     |     |     |      | begun recovery.            | cyber-angriff-getroffen         |
2022-07-29 Semikron- Germany Discrete  R Unknown 8 U Shut down  A power-electronics  https://icsstrive.com/incident/semik
Danfoss Mfg. production for  semiconductor maker for  ron-holding-production-after-cyber-
|     |     |     | months | ICS, EVs and wind turbines  | attack/ |
| --- | --- | --- | ------ | --------------------------- | ------- |
suffered a LV ransomware
https://bleepingcomputer.com/new
|     |     |     |     | attack, and was not fully  | s/security/semiconductor-        |
| --- | --- | --- | --- | -------------------------- | -------------------------------- |
|     |     |     |     | restored months after the  | manufacturer-semikron-hit-by-lv- |
|     |     |     |     | incident.                  | ransomware-attack                |
2022-08-05 Ontario  Canada Transport U Unknown 1 U Halted delivery &  Through the OCS crown  https://icsstrive.com/incident/us-
Cannabis  distribution  corporation, the provincial  supply-chain-cyberattack-affects-
ontario-cannabis-retail-corporation-
Retail  province-wide for government of Ontario  ocs-deliveries/
| Corporation  |     |     | 5 days | controls and regulates the  |     |
| ------------ | --- | --- | ------ | --------------------------- | --- |
(OCS) supply of cannabis to all  https://cbc.ca/news/canada/toront
|     |     |     |     | retail stores. | o/ontario-cannabis-store-1.6549657 |
| --- | --- | --- | --- | -------------- | ---------------------------------- |
2022-08-08 Bombardier  Austria,  Discrete  R RansomExx 4 I3 Shut down  The malware infection was  https://icsstrive.com/incident/brp-
Recreationa Canada,  Mfg. production and  traced to a service provider.  suspends-operations-following-
l Products  Finland,  halted order  RansomExx gang published  ransomware-attack/
| (BRP) USA |     |     | fulfillment for 1  | all exfiltrated data from BRP                              |                                   |
| --------- | --- | --- | ------------------ | ---------------------------------------------------------- | --------------------------------- |
|           |     |     | week               | after they refused to pay the s/security/ransomexx-claims- | https://bleepingcomputer.com/new  |
|           |     |     |                    | ransom.                                                    | ransomware-attack-on-sea-doo-ski- |
doo-maker
2022-08-13 Apex  USA Transport R BlackByte 1 ID Shut down  BlackByte ransomware on  https://icsstrive.com/incident/syste
Capital /  operations for 1  TCS Fuel impacted small- m-outage-at-apex-capital-affects-
TCS Fuel week business truckers, who were  medium-and-small-size-trucking-
companies
unable to fuel their trucks or
access funds to pay their
owner-operators.
2022-09-02 Novosibirsk  Russia Transport H Team  1 DO Shut down and  Pro-Ukrainian activists Team  https://icsstrive.com/incident/novos
OneFist causes traffic chaos, ibirsk-transportation-system-
| City  |     | OneFist  | disrupted public  |     |     |
| ----- | --- | -------- | ----------------- | --- | --- |
Transport  (Ukraine) transportation  by halting and damaging the  attacked-by-pro-ukranian-hacker-
group/
| Traffic   |     |     | for 2+ days | public transit scheduling  |     |
| --------- | --- | --- | ----------- | -------------------------- | --- |
| Managemen |     |     |             | system and signage, to     |     |
https://ibtimes.com/russians-
| t System |     |     |     | prevent a quick recovery. | novosibirsk-forced-pound- |
| -------- | --- | --- | --- | ------------------------- | ------------------------- |
pavements-team-onefist-paralyzes-
traffic-exclusive-3611628
2022-09-03 Yandex Taxi Russia Transport H Anonymou 1 DO Disrupted  Hacktivists caused traffic  https://icsstrive.com/incident/chao
s  Moscow traffic  chaos, in an attack that  s-in-moscow-traffic-caused-by-
[OpRussia] for 3+ hours simultaneously dispatched  yandex-taxis-software-hack

all Yandex's Taxi cars to the
|     |     |     |     | same location, resulting in a  | https://securityaffairs.com/135280/ |
| --- | --- | --- | --- | ------------------------------ | ----------------------------------- |
hacktivism/anonyomus-hacked-
|     |     |     |     | massive traffic jam. | yandex-taxi.html |
| --- | --- | --- | --- | -------------------- | ---------------- |
59

Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor | Actor Attack  | Physical  |     |     |
| ----- | ------------- | --------- | --- | --- |
Type Consequences
2022-09-05 Läderach  Switzerland Food &  R Unknown 1 DS Halted  A ransomware attack on the  https://icsstrive.com/incident/opera
Bev. production,  chocolatier causes a long- tions-impacted-at-swiss-chocolate-
manufacturer-laderach
|     |     | logistics and  | term outage and impacts  |     |
| --- | --- | -------------- | ------------------------ | --- |
administration for logistics. After Läderach
|     |     | 67 days | refuses to pay the ransom,  |     |
| --- | --- | ------- | --------------------------- | --- |
all data is leaked.
2022-09-26 Electricity  Ghana Power R Unknown 1 ID 5+ days of power  A ransomware attack  https://icsstrive.com/incident/ranso
disables ECG's billing system mware-attack-at-electric-company-
| Company of  |     | outages for pre- |     |     |
| ----------- | --- | ---------------- | --- | --- |
Ghana (ECG) paid customers and the IT network, leaving  of-ghana-left-customers-without-
power-for-days
commercial and residential
customers in the dark and
unable to purchase power.
2022-10-05 HiPP Germany Food &  U Unknown 1 DS Shut down  Pfaffenhofen, Bavaria based  https://icsstrive.com/incident/ot-
Bev. production for  baby food manufacturer,  systems-impacted-at-german-baby-
food-manufacturer/
|     |     | days, and 1000  | which sells worldwide, was  |     |
| --- | --- | --------------- | --------------------------- | --- |
|     |     | employees sent  | hit by an attack which      |     |
https://csoonline.com/de/a/hipp-
|     |     | home | shutdown both IT and OT  | gehackt,3674208 |
| --- | --- | ---- | ------------------------ | --------------- |
systems.
2022-10-12 Undisclosed  Ukraine Power NS Sandworm 1 DO Caused two  Sandworm (Russian GRU  https://icsstrive.com/incident/russia
Ukrainian  [GRU Unit  power outages Main Intelligence  n-sandworm-behind-operational-
disruption-of-ukraine-energy-
| Power  | 74455]  |     | Directorate) caused two  |     |
| ------ | ------- | --- | ------------------------ | --- |
Facilities (Russia) separate power outages on  facility-in-october-2022/
|     |     |     | Oct. 12 and 14th. Coincided  | https://mandiant.com/resources/bl |
| --- | --- | --- | ---------------------------- | --------------------------------- |
|     |     |     | with a kinetic strike on     | og/sandworm-disrupts-power-       |
|     |     |     | critical infra. Mandiant     | ukraine-operational-technology    |
released details in a
November 2023 public
report.
2022-10-14 Heilbronner  Germany Process  R Unknown 1 DS Shut down  Printing presses halted after  https://icsstrive.com/incident/ranso
Stimme &  Mfg. operations and  a ransomware attack,  mware-attack-cripples-printing-
Stimme  sent employees  stopping distribution of the  systems-at-german-newspaper/
| Mediengruppe |     | home; impacted    | Heilbronner Stimme and       |                                  |
| ------------ | --- | ----------------- | ---------------------------- | -------------------------------- |
|              |     | regional partners | other regional publications  | https://bleepingcomputer.com/new |
s/security/ransomware-attack-
|     |     |     | printed under contract. | halts-circulation-of-some-german- |
| --- | --- | --- | ----------------------- | --------------------------------- |
newspapers
2022-10-28 Aurubis AG Germany,  Metals &  U Unknown 1 IA Production and  Europe's largest copper  https://icsstrive.com/incident/hacke
USA Mining delivery halted,  smelter admitted to isolating rs-shut-down-production-at-
|     |     | and employees  | from the internet, and  | cartonnerie-gondardennes-in- |
| --- | --- | -------------- | ----------------------- | ---------------------------- |
france/
|     |     | sent home, in  | operating manually, but local  |     |
| --- | --- | -------------- | ------------------------------ | --- |
|     |     | Buffalo, NY    | news in Buffalo reported       |     |
https://hackread.com/copper-
|     |     |     | their copper wire plant was  | producer-aurubis-cyberattack |
| --- | --- | --- | ---------------------------- | ---------------------------- |
shutdown.
2022-10-29 Danish Rails  Denmark Transport R Unknown 1 I3 Shut down train  Denmark's largest rail  https://isssource.com/trains-halted-
(DSB) / Supeo service for  operator halted due to  in-denmark-after-cyberattack
|     |     | several hours | cyberattack on 3rd party  |     |
| --- | --- | ------------- | ------------------------- | --- |
https://reuters.com/technology/dan
Supeo. Supeo was unable to
|     |     |     | offer their critical, real-time  | ish-train-standstill-saturday-caused- |
| --- | --- | --- | -------------------------------- | ------------------------------------- |
by-cyber-attack-2022-11-03/
safety data to train drivers.
2022-10-31 Cartonnerie  France Process  R Unknown 1 DS Shut down  This cardboard maker  https://icsstrive.com/incident/hacke
rs-shut-down-production-at-
Gondardennes Mfg. production for 3  avoided paying a ransom as
|     |     | days, and  | systems were decrypted by  | cartonnerie-gondardennes-in- |
| --- | --- | ---------- | -------------------------- | ---------------------------- |
france/
|     |     | workers sent  | a local journalist and cyber  |     |
| --- | --- | ------------- | ----------------------------- | --- |
|     |     | home          | expert Damien Bancal.         |     |
https://lavoixdunord.fr/1250765/arti
cle/2022-11-07/le-piratage-
cartonnerie-gondardennes-
decrypte-par-damien-bancal-
journaliste
2022-11-02 Jeppesen, a  Global Transport R Unknown 1 I3 Delayed flights at Ransomware shutdown 6  https://icsstrive.com/incident/cyber
wholly owned  multiple airlines & Electronic Flight Bag (EFB)  attack-attack-at-boeing-subsidiary-
causes-widespread-flight-
| Boeing  |     | impacted flight  | apps & services provided by  |     |
| ------- | --- | ---------------- | ---------------------------- | --- |
subsidiary planning for 14  Jeppesen, increasing pilot's  disruptions

|     |     | days | workloads in flight planning  | https://ops.group/blog/jeppesen- |
| --- | --- | ---- | ----------------------------- | -------------------------------- |
|     |     |      | and navigation.               | ransomware-attack-update         |
2022-11-05 Uponor Oyj  Finland Discrete  R Unknown 1 IA Shut down  The manufacturer of HVAC,  https://icsstrive.com/incident/opera
Mfg. production for 1  plumbing, and infrastructure  tional-shutdown-at-uponor-
intelligent-plumbing-climate-
|     |     | week, then  | products shutdown all OT  | solutions |
| --- | --- | ----------- | ------------------------- | --------- |
reduced capacity systems as a precaution, and
|     |     | for 2+ weeks | restoration took weeks. |     |
| --- | --- | ------------ | ----------------------- | --- |
60

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor | Actor Attack Physical  |     |     |     |
| --- | ----- | ---------------------- | --- | --- | --- |
Type Consequences
2022-11-05 PGT  USA Discrete  R Unknown 2 $12M U Impacted  A ransomware attack  https://icsstrive.com/incident/ranso
Innovations Mfg. production at 2  impacted 2 window and door mware-attack-at-window-and-door-
|     |     |     | plants, and       | manufacturing plants in      | manufacturer-pgt-innovations |
| --- | --- | --- | ----------------- | ---------------------------- | ---------------------------- |
|     |     |     | contributed to a  | Florida and contributed to   |                              |
|     |     |     | $12m loss         | $12m quarterly revenue loss. |                              |
2022-11-06 Maple Leaf  Canada Food &  R BlackBasta 1 U Disrupted  BlackBasta lists MapleLeaf  https://icsstrive.com/incident/syste
Foods Bev. operations and  as one of its victims on the  m-outage-at-maple-leaf-food-
|     |     |     | services at  | dark web, but Maple Leaf  | manufacturer-in-canada/ |
| --- | --- | --- | ------------ | ------------------------- | ----------------------- |

|     |     |     | multiple sites | releases little else about the  | https://just- |
| --- | --- | --- | -------------- | ------------------------------- | ------------- |
attack other than the impact food.com/news/canadas-maple-
|     |     |     |     | to ops. | leaf-foods-hit-by-cyberattack |
| --- | --- | --- | --- | ------- | ----------------------------- |
2022-11-17 Taxis Coop  Canada Transport R Unknown 1 IA Shut down taxi  Ransomware breached Taxi  https://icsstrive.com/incident/taxi-
Québec dispatch system  Coop Quebec's ride hailing  ride-hailing-service-in-quebec-
|     |     |     | for 2.5 hours in  | back-end systems, so staff   | hacked/ |
| --- | --- | --- | ----------------- | ---------------------------- | ------- |
|     |     |     | the early morning | pre-emptively shut down all  |         |
https://ici.radio-
|     |     |     |     | servers and began recovery. | canada.ca/nouvelle/1933690/taxi- |
| --- | --- | --- | --- | --------------------------- | -------------------------------- |
coop-quebec-cyberattaque-
informatique
2022-11-17 Europea  Italy Discrete  R Unknown 1 U Shut down  EMA, a precision investment  https://icsstrive.com/incident/cyber
attack-shuts-down-operations-at-
Microfusioni  Mfg. production line  casting leader, was hit by
Aerospaziali  for 6+ days, and  ransomware production lines precision-casting-foundry-europea-
(EMA) sent employees  were shutdown. 40 techs and microfusioni-aerospaziali
|     |     |     | home | specialists were sent in to  |     |
| --- | --- | --- | ---- | ---------------------------- | --- |
assist.
2022-11-21 Communauto Canada Transport U Unknown 1 DS Shut down ride- A cyberattack prevented  https://icsstrive.com/incident/cyber
|     |     |     | sharing  | users from starting or ending attack-hits-communauto- |     |
| --- | --- | --- | -------- | ----------------------------------------------------- | --- |
operations-already-struggling-with-
|     |     |     | operations &       | a ride, during an existing  |                      |
| --- | --- | --- | ------------------ | --------------------------- | -------------------- |
|     |     |     | services for 1 day | industry shortage of        | frustrated-customers |
vehicles, frustrating users
struggling to reserve a car.
2022-11-25 Prophete /  Germany Discrete  R Unknown 1 Bankru ID Shut down  Ransomware attack meant  https://icsstrive.com/incident/down
VSF  Mfg. pt operations for 3+  that parts did not arrive,  time-caused-by-cyberattack-final-
straw-for-german-bicycle-
Fahrradmanu weeks and lead  bicycles were not fully  manufacturer
| faktur,      |     |     | to insolvency | assembled and delivered,    |     |
| ------------ | --- | --- | ------------- | --------------------------- | --- |
| Rabeneick    |     |     |               | and shareholder injections  |     |
| and Kreidler |     |     |               | could not be secured.       |     |
2022-11-25 Cobolux Luxembourg Food &  R Unknown 1 €400K ID 1 day production  Ransomware attack made it  https://icsstrive.com/incident/produ
Bev. loss; Estimated  impossible to continue  ction-halted-at-meat-processing-
|     |     |     | €400K - €500K in  | operating, because meat   | factory-in-luxembourg |
| --- | --- | --- | ----------------- | ------------------------- | --------------------- |
|     |     |     | damages and       | products could not be     |                       |
|     |     |     | restoration costs | labeled, a regulated and  |                       |
food safety requirement.
2022-12-10 UNOX Italy Discrete  U Unknown 1 IA Shut down  Hit by a cyberattack, the  https://icsstrive.com/incident/italia
Mfg. production for 2  company activated  n-oven-manufacturer-suspends-
|     |     |     | days | emergency procedures,  | production-after-cyberattack |
| --- | --- | --- | ---- | ---------------------- | ---------------------------- |
suspended production as a
safety measure, and initiated
"appropriate checks."
2022-12-11 Fruttagel Italy Food &  R ALPHV /  1 U Shut down  A BlackCat (ALPHV)  https://icsstrive.com/incident/produ
ction-outage-after-massive-
|     | Bev. | BlackCat | production for 4+  | ransomware attack on         |                               |
| --- | ---- | -------- | ------------------ | ---------------------------- | ----------------------------- |
|     |      |          | days               | Fruttagel halted production  | ransomware-attack-at-italian- |
|     |      |          |                    | and prevented customer       | fruttagel                     |
deliveries.
2022-12-13 Empresas  Colombia Water R ALPHV /  1 ID Trucked in water  A BlackCat (ALPHV)  https://isssource.com/ransomware-
Públicas de  BlackCat for 28k  ransomware attack shut off  attack-at-colombian-utility
| Medellín  |     |     | customers on      | water for 28K customers  |     |
| --------- | --- | --- | ----------------- | ------------------------ | --- |
| (EPM)     |     |     | pre-paid service  | unable to pre-pay for    |     |
|           |     |     | plans             | service, due to an OT    |     |
dependence on IT and billing
systems.
2022-12-22 Technolit  Germany Discrete  U Unknown 1 U Shut down  A German manufacturer and  https://icsstrive.com/incident/cyber
GmbH, in  Mfg. operations and  distributor of welding  attack-at-technolit-gmbh-
Grossenlüder sent employees  supplies and products was  employees-sent-home
|     |     |     | home | shutdown by an unknown  |     |
| --- | --- | --- | ---- | ----------------------- | --- |
cyberattack.
2022-12-27 Copper  Canada Metals &  R Unknown 1 IA Shut down  CMMC shutdown mining ops  https://isssource.com/copper-
Mountain  Mining operations for 5  out of an abundance of  miner-hit-in-ransomware-attack
| Mining       |     |     | days (pre-        | caution, after an attack  |     |
| ------------ | --- | --- | ----------------- | ------------------------- | --- |
| Corporation  |     |     | emptive), then    | possibly enabled by       |     |
| (CMMC)       |     |     | reduced           | passwords leaked on the   |     |
|              |     |     | production for 4  | dark web weeks earlier.   |     |
days
61

Incidents in 2021
Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack Physical
Type Consequences
2021-01-23 Westrock USA Process  R Unknown 1 IA Forced manual  After the packaging  https://icsstrive.com/incident/ransom
Mfg. ops, reduced  manufacturer was hit by  ware-attack-on-westrock/
|     |     |     | production by  | ransomware, they        |                                |
| --- | --- | --- | -------------- | ----------------------- | ------------------------------ |
|     |     |     | 85K tons, and  | shutdown systems in an  | https://ir.westrock.com/press- |
releases/press-release-
|     |     |     | delayed   | abundance of caution,    | details/2021/WestRock-Provides- |
| --- | --- | --- | --------- | ------------------------ | ------------------------------- |
|     |     |     | shipments | which impacted           | Update-on-Ransomware-Incident-  |
|     |     |     |           | production and shipment  | 8dfde2fca/default.aspx          |

volumes.
https://securityweek.com/packaging-
giant-westrock-says-ransomware-
attack-impacted-ot-systems
2021-01-26 Palfinger AG Europe, N. & S. Discrete  R Unknown 31 IA Lost nearly 2  The world's largest crane  https://icsstrive.com/incident/austria-
crane-maker-under-attack/
|     | America, Asia | Mfg. | weeks crane        | manufacturer. All global  |     |
| --- | ------------- | ---- | ------------------ | ------------------------- | --- |
|     |               |      | production at all  | plants were affected.     |     |
https://bitdefender.com.au/blog/hotfo
|     |     |     | plants |     | rsecurity/worlds-largest-crane-maker- |
| --- | --- | --- | ------ | --- | ------------------------------------- |
suffers-global-cyber-attack-
operations-at-a-halt
https://www.internationalcranes.medi
a/news/palfinger-attack-highlights-
escalation-in-cyber-
crimes/8013885.article
2021-02-18 Beneteau SA France Discrete  R Unknown 2 IA Shut down for 3- Boat manufacturer hit by  https://icsstrive.com/incident/french-
boat-maker-beneteau-hit-by-
|     |     | Mfg. | 4 weeks at     | ransomware, impacting    |              |
| --- | --- | ---- | -------------- | ------------------------ | ------------ |
|     |     |      | several plants | OT. Production shutdown  | cyberattack/ |

|     |     |     |     | or delayed at "several  | https://boatindustry.com/news/36934/ |
| --- | --- | --- | --- | ----------------------- | ------------------------------------ |
sites". Wiped out 2021
beneteau-2021-growth-almost-
|     |     |     |     | growth, according to CEO. | evaporated-in-cyber-attack |
| --- | --- | --- | --- | ------------------------- | -------------------------- |

https://press.beneteau-
group.com/assets/210221-beneteau-
information-regarding-a-cyberattack-
5e06-49529.html
2021-03-11 Molson Coors USA, Canada,  Food &  R Unknown 13 $120M IA Disrupted  Took all systems offline to  https://icsstrive.com/incident/major-
UK Bev. brewery  contain the spread. By end brewer-molson-coors-hit-by-
|     |     |     | production and  | of the month was still   | cyberattack/                        |
| --- | --- | --- | --------------- | ------------------------ | ----------------------------------- |
|     |     |     | shipments,      | dealing with delays and  | https://bleepingcomputer.com/news/s |
|     |     |     | delaying 120-   | disruptions UK, Canada,  |                                     |
ecurity/molson-coors-brewing-
|     |     |     | $140m in  | and USA. | operations-disrupted-by-cyberattack |
| --- | --- | --- | --------- | -------- | ----------------------------------- |
|     |     |     | earnings  |          |                                     |
https://securityweek.com/molson-
coors-cyberattack-storms-could-cost-
company-140-million
2021-03-20 Sierra Wireless Canada Discrete  R Unknown 1 IA Halted  IoT, cellular, and wireless  https://isssource.com/sierra-wireless-
hit-by-ransomware-attack
|     |     | Mfg. | production at all  | device manufacturer with  |     |
| --- | --- | ---- | ------------------ | ------------------------- | --- |
|     |     |      | manufacturing      | an unknown number of      |     |
|     |     |      | sites              | manufacturing sites.      |     |
2021-03-25 Asteelflash  France Discrete  R REvil 20 IA Shut down  A leading Electronics  https://icsstrive.com/incident/revil-
ransomware-shut-down-multiple-
| Group SA |     | Mfg. | multiple printed  | Manufacturing Services                         |     |
| -------- | --- | ---- | ----------------- | ---------------------------------------------- | --- |
|          |     |      | circuit board     | (EMS) company suffered a plants-at-asteelflash |     |
|          |     |      | plants            | REvil ransomware attack.                       |     |
2021-04-01 JBI Bike USA Transport R Unknown 11 ID Delayed  A wholesale bicycle and  https://icsstrive.com/incident/jbi-
|     |     |     | shipments for 7+  | parts distributor, with 11  | bicycle-retailer-halts-shipments-due- |
| --- | --- | --- | ----------------- | --------------------------- | ------------------------------------- |
to-cyberattack/
|     |     |     | days | warehouses, where only  |     |
| --- | --- | --- | ---- | ----------------------- | --- |
|     |     |     |      | some were back up a     |     |
https://bicycleretailer.com/industry-
|     |     |     |     | week after the attack. | news/2021/04/07/jbi-back-online- |
| --- | --- | --- | --- | ---------------------- | -------------------------------- |
limited-capacity-after-ransomware-
attack#.ZBip3PbMKdY
2021-04-04 Bakkier  Netherlands Transport R Unknown 1 ID Disrupted new  Caused shortages of  https://icsstrive.com/incident/ransom
Logistiek orders, delayed  packaged cheese at retail. ware-attack-at-bakker-logistiek-
caused-cheese-shortage-in-dutch-
shipments to
|     |     |     | retail outlets for  |     | supermarkets |
| --- | --- | --- | ------------------- | --- | ------------ |
5 days
62

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor Actor Attack Physical  |     |     |     |
| ---------------------------- | --- | --- | --- |
Type Consequences
2021-05-07 Colonial  USA Oil & Gas R DarkSide 1 $52M IA Shut down  DarkSide ransomware  https://icsstrive.com/incident/colonial-
Pipeline pipeline for 6  behind attack on the  pipeline-ops-shut-down-after-
ransomware-attack
|     | days, paid a     | largest gasoline pipeline  |     |
| --- | ---------------- | -------------------------- | --- |
|     | $4.4M ransom, &  | in USA, triggering         |     |
|     | lost (WF)        | widespread gasoline        |     |
|     | estimated $50m   | shortages in US            |     |
|     | in revenue (FBI  | Northeast.                 |     |
recovered $2.2M)
2021-05-20 Ardagh  UK Process  R Unknown 1 $34M ID Slowed  Metal and glass  https://isssource.com/eu-packaging-
Group Mfg. production and  beverage packaging  maker-hit-by-cyberattack
|     | delayed   | facilities remained    |     |
| --- | --------- | ---------------------- | --- |
|     | shipments | operational, but some  |     |
processes reverted to
manual operation
causing shipment delays.
2021-05-21 Siegfried  Switzerland,  Pharma U Unknown 2 U Shut down  A cyberattack cause  https://icsstrive.com/incident/swiss-
Group Germany operations and  several sites to shutdown drug-manufacturer-siegfried-shuts-
|     | impacted  | operations. The company down-production-after-cyberattack/ |     |
| --- | --------- | ---------------------------------------------------------- | --- |
said production shortfalls
|     | production |                          | https://www.siegfried.ch/siegfried-     |
| --- | ---------- | ------------------------ | --------------------------------------- |
|     |            | are expected to be made  | restarts-production-after-cyber-attack/ |
up by end-of-year.
https://cen.acs.org/business/specialty-
chemicals/Siegfried-Brenntag-Symrise-
hit-cyberattacks/99/i20
2021-05-30 JBS SA Australia,  Food &  R REvil 5 $11M IA Several large  Plants in Nebraska,  https://icsstrive.com/incident/attack-
Canada,  Bev. meatpacking  Colorado, Texas, Brooks,  shuts-operations-of-global-meat-
provider/
USA plants shut down and Australia canceled
|     | and sent workers production shifts. REvil  |     |     |
| --- | ------------------------------------------ | --- | --- |
https://cbc.ca/news/business/jbs-
|     | home | the top suspect. | meat-cyberattack-1.6048942 |
| --- | ---- | ---------------- | -------------------------- |
https://www.cbc.ca/news/canada/calg
ary/jbs-canada-cyberattack-1.6060121
 https://cnn.com/2021/07/13/tech/revil-
ransomware-disappears/index.html
2021-07-09 Iran Rails Iran Transport H Predatory  1 DO Impaired service  Targeted by the  https://icsstrive.com/incident/irans-rail-
Sparrow  by  Predatory Sparrow group, service-delayed-with-fake-messages/

| (Gonjeshke  | reprogramming  | infected with wiper  |     |
| ----------- | -------------- | -------------------- | --- |
Darande) signs and wiping  malware, and  https://nytimes.com/2021/08/14/world/
middleeast/iran-trains-cyberattack.html
|     | computers | reprogrammed rail      |                                        |
| --- | --------- | ---------------------- | -------------------------------------- |
|     |           | signage causing        | https://theguardian.com/world/2021/jul |
|     |           | “unprecedented chaos.” | /11/cyber-attack-hits-irans-transport- |
ministry-and-railways
2021-07-22 Transnet South Africa Transport R Unknown 4 U Declared Force  Transnet said ports at  https://icsstrive.com/incident/attacks-
|     | Majeure and  | Durban, Ngqura, Port     | shuts-south-africa-port-ops/ |
| --- | ------------ | ------------------------ | ---------------------------- |
|     | halted       | Elizabeth and Cape Town  |                              |
https://reuters.com/article/us-transnet-
|     | operations for 7  | were affected. | cyber-idUSKBN2EZ0RQ |
| --- | ----------------- | -------------- | ------------------- |
days
2021-09-17 New  USA Food &  R BlackMatte 1 IA Delayed grain  A BlackMatter  https://icsstrive.com/incident/ia-ag-
Cooperative Bev. r receipts &  ransomware attack  cooperative-hit-in-ransomware-attack
shipments, & shut impacted grain
|     | down fertigation  | transactions during      |     |
| --- | ----------------- | ------------------------ | --- |
|     | optimization      | harvest season. Systems  |     |
|     | system            | were pre-emptively       |     |
shutdown to stop the
spread.
2021-09-19 Crystal  USA Food &  R Unknown 1 IA Shut down for 4  During harvest season  https://icsstrive.com/incident/ransomw
Valley  Bev. days and  were unable to mix  are-attack-forces-agricultural-grain-
firm-in-minnesota-to-take-systems-
Cooperative reverted to  fertilizer, fulfil livestock  offline
|     | manual ops. | feed orders, and  |     |
| --- | ----------- | ----------------- | --- |
switched to manual ops
for receiving grain by
issuing paper receipts.
2021-09-21 Weir Group UK Discrete  R Unknown 1 £20M IA Disrupted  When the attack was  https://icsstrive.com/incident/weir-
Mfg. manufacturing,  detected, "systems  group-ransomware-incident
|     | engineering, and  | promptly responded by  |     |
| --- | ----------------- | ---------------------- | --- |
|     | shipping          | shutting down core     |     |
operations." Loss
projected at £20-30m.
2021-10-09 Ferrara USA Food &  R Unknown 2 U Shut down  Candymaker suffered  https://icsstrive.com/incident/ransomw
Bev. operations and  production shutdowns  are-strikes-candymaker/
|     | delayed  | prior to Halloween, but  |     |
| --- | -------- | ------------------------ | --- |
https://cyberscoop.com/candy-corn-
|     | shipments for  | had only resumed       | hack-halloween |
| --- | -------------- | ---------------------- | -------------- |
|     | more than two  | production in "select  |                |

|     | weeks | facilities" two weeks  | https://manufacturing.net/home/news/1 |
| --- | ----- | ---------------------- | ------------------------------------- |
|     |       | later.                 | 3165782/ferrero-to-acquire-ferrara-   |
candy-company
63

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor | Actor Attack Physical  |     |     |     |
| --- | ----- | ---------------------- | --- | --- | --- |
Type Consequences
2021-10-22 Schreiber  USA,  Food &  R Unknown 30 U Shut down  Large cheese and yogurt  https://icsstrive.com/incident/ransomw
Foods Europe, S.  Bev. production and  manufacturer could not  are-attack-disrupted-entire-milk-supply-
chain-at-scheiber-foods-for-days/
|     | America |     | delivery for 5  | receive, produce, or ship  |     |
| --- | ------- | --- | --------------- | -------------------------- | --- |
|     |         |     | days, and       | dairy product due to an    |     |
https://cyberscoop.com/schreiber-
|     |     |     | disrupted dairy  | attack on their plants   | foods-cyber-event-ransomware- |
| --- | --- | --- | ---------------- | ------------------------ | ----------------------------- |
|     |     |     | supply chain     | and distribution centers |                               |
agriculture-food

https://wisfarmer.com/story/news/2021
/10/26/schreiber-foods-hit-cyberattack-
plants-closed/8558252002
2021-10-24 Eberspaecher  Germany Discrete  R Unknown 80 $60M ID Impacted parts  Attack encrypted  https://icsstrive.com/incident/cyberatta
Group Mfg. production,  systems across their  ck-cost-eberspacher-automotive-
supplier-60million-says-ceo/
|     |     |     | closed factories,  | global IT network,       |     |
| --- | --- | --- | ------------------ | ------------------------ | --- |
|     |     |     | and impacted       | impacted manufacturing,  |     |
https://rvbusiness.com/report-
|     |     |     | workers | and cited in annual report eberspaecher-still-delivering-parts- |                   |
| --- | --- | --- | ------- | --------------------------------------------------------------- | ----------------- |
|     |     |     |         | as reason for a 2022 net                                        | amid-cyberattack/ |
loss.
https://www.eberspaecher.com/fileadm
in/data/corporatesite/pdf/en/7_compa
ny/EB_Annual_Report_01.pdf
2021-10-26 Gas stations in Iran Oil & Gas H Predatory  4300 ID Long line-ups and Predatory Sparrow group  https://icsstrive.com/incident/iran-says-
Iran Sparrow  closed stations  disabled system  cyberattack-closes-gas-stations-
|     |     | (Gonjeshke  | for 4-5 days | supporting cards used to  | across-country/ |
| --- | --- | ----------- | ------------ | ------------------------- | --------------- |

|     |     | Darande) |     | buy discounted gasoline. |     |
| --- | --- | -------- | --- | ------------------------ | --- |
https://bbc.com/news/world-middle-
east-59062907

https://iranprimer.usip.org/blog/2021/n
ov/02/israel-iran-cyber-war-gas-station-
attack
2021-11 Madix Inc USA Discrete  R Unknown 2 U Shut down  Manufacture of store  https://icsstrive.com/incident/ransomw
Mfg. production, sent  fixtures halted at both  are-hits-store-fixture-manufacturer/
|     |     |     | employees home | Goodwater and Eclectic  |                                     |
| --- | --- | --- | -------------- | ----------------------- | ----------------------------------- |
|     |     |     |                | plants.                 | https://newsbreak.com/news/24356334 |
63049-ransomware-attack-at-alabama-
manufacturing-plants-send-hundreds-
of-employees-home-with-no-specified-
date-of-return
2021-11-07 Diamond  USA Transport R Unknown 1 DS Delayed retail  A top distributor for  https://icsstrive.com/incident/ransomw
Comic Book  shipments by 2-4  Marvel, Dark Horse and  are-attack-at-diamond-comic-
distributors-disrupts-retailer-shipments
| Distributors |     |     | days, twice | Image comics  |     |
| ------------ | --- | --- | ----------- | ------------- | --- |
temporarily halted
scheduled orders after a
ransomware attack
prevented delivery.
2021-11-08 Estrella Damm Spain Food &  R Unknown 2 DS Shut down  Had this occurred in the  https://icsstrive.com/incident/barcelon
as-damm-brewery-ransomware-attack
| Brewery | Bev. |     | production for 5  | summer, consequences        |     |
| ------- | ---- | --- | ----------------- | --------------------------- | --- |
|         |      |     | days at all       | would have been more        |     |
|         |      |     | breweries         | severe as stocks only last  |     |
|         |      |     | (impacted         | 3 days.                     |     |
bottling)
2021-12-01 Bay & Bay  USA Transport R Conti 1 IA Lost 1.5 weeks of  Hit by Conti ransomware, https://icsstrive.com/incident/mn-
Transportation production systems were taken  trucking-and-logistics-company-hit-by-
ransomware-attack-again/
offline and remediated.
https://freightwaves.com/news/minnes
ota-trucking-company-hit-in-2nd-
ransomware-attack
2021-12-21 Nortura Norway Food &  R Unknown 2 IA Production  Shutdown meat  https://icsstrive.com/incident/norwegia
Bev. halted at several  processing plants after a  n-food-producer-hit-in-cyberattack
|     |     |     | sites for more  | ransomware attack, with  |     |
| --- | --- | --- | --------------- | ------------------------ | --- |
https://web.archive.org/web/202207010
|     |     |     | than a week | one report of animals  |     |
| --- | --- | --- | ----------- | ---------------------- | --- |
83242/norwaytoday.info/news/slaughte
|     |     |     |     | destined for slaughter  | r-pigs-sent-to-a-competitor-after-the- |
| --- | --- | --- | --- | ----------------------- | -------------------------------------- |
|     |     |     |     | being diverted to       | data-attack-on-nortura                 |
competitors.
2021-12-28 Amedia Norway Process  U Unknown 1 U Shut down  Norway's largest local  https://icsstrive.com/incident/norway-
Mfg. printing presses  news publisher was  media-company-amedia-hit-in-
forced to shut down their cyberattack
for 1.5 days
presses after an
unspecified cyberattack
shut them down.
64

Incidents in 2020
Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack Physical
Type Consequences
2020-01-13 Picanol Belgium,  Discrete  R Unknown 3 €1M U Shut down  As a manufacturer of  https://icsstrive.com/incident/ransom
Romania,  Mfg. manufacturing  weaving machines,  ware-attack-shuts-down-production-
at-loom-manufacturer-in-belgium/
|     | China | plants for 1     | Picanol’s manufacturing  |     |
| --- | ----- | ---------------- | ------------------------ | --- |
|     |       | weeks, and sent  | plants are heavily       |     |
https://picanolgroup.com/en/investors
|     |     | workers home | automated. Financial     | /press-releases/press-release-cyber- |
| --- | --- | ------------ | ------------------------ | ------------------------------------ |
|     |     |              | impact amounts paid for  | attack-update-january-31-2020        |
external experts.
2020-01-31 Toll Group Australia Transport R Unknown 1 IA Shut down  Australian-based global  https://icsstrive.com/incident/toll-
|     |     | systems and  | logistics company    | group-has-large-portion-of-it- |
| --- | --- | ------------ | -------------------- | ------------------------------ |
|     |     | reverted to  | suffered a targeted  | infrastructre-taken-out-by-    |
ransomeware-attack/
|     |     | manual ops. | ransomware attack, and  |     |
| --- | --- | ----------- | ----------------------- | --- |
shutdown automation in
https://zdnet.com/article/deliveries-
|     |     |     | an abundance of caution. | stranded-across-australia-as-toll- |
| --- | --- | --- | ------------------------ | ---------------------------------- |
confirms-ransomware-attack

https://zdnet.com/article/toll-group-
shuts-down-it-systems-in-response-to-
cybersecurity-incident
2020-02-24 KHS Bicycles USA Discrete  R Unknown 1 ID Delayed  Could not process B2B  https://icsstrive.com/incident/khs-
Mfg. shipments for 2  orders and ship bikes  bicycle-shipments-delayed-for-2-days-
after-cyberattack/
|     |     | days | following a ransomware  |     |
| --- | --- | ---- | ----------------------- | --- |
attack over the weekend.
https://bicycleretailer.com/industry-
news/2020/02/25/khs-bicycles-
systems-hacked-distributor-halts-
shipments#.YG3-wC1h3ox
2020-03-04 EVRAZ  USA & Canada Process  R Unknown 2 ID Shut down  After an attack on IT  https://icsstrive.com/incident/evraz-
manufacturing  Mfg. operations at  systems, production was  infection/
|     |     | several plants,  | halted at least two sites in  |     |
| --- | --- | ---------------- | ----------------------------- | --- |
Canada. Ops depend on IT https://cbc.ca/news/canada/saskatch
|     |     | and sent 900+                             |                       | ewan/evraz-regina-shut-down- |
| --- | --- | ----------------------------------------- | --------------------- | ---------------------------- |
|     |     | workers home for which are "necessary to  |                       | ransomware-attack-1.5487017  |
|     |     | 3+ days                                   | ensure standards and  |                              |

|     |     |     | traceability." | https://globalnews.ca/news/6640313/ |
| --- | --- | --- | -------------- | ----------------------------------- |
evraz-regina-cyberattack-layoffs
2020-05-09 Shahid Rajaee  Iran Transport NS Unknown 1 DO Halted port  Sophisticated attack by  https://icsstrive.com/incident/shahid-
rajaee-port-terminal-maratime-attack/
| port |     | terminal,     | Israel and retaliation for  |                                         |
| ---- | --- | ------------- | --------------------------- | --------------------------------------- |
|      |     | abruptly and  | Iran's attacks on Israeli   |                                         |
|      |     | inexplicably  | water systems in April,     | https://timesofisrael.com/6-facilities- |
said-hit-in-irans-cyberattack-on-
|     |     |     | which were caught and  | israels-water-system-in-april |
| --- | --- | --- | ---------------------- | ----------------------------- |
|     |     |     | defeated in real-time. |                               |
https://timesofisrael.com/cyber-
attacks-again-hit-israels-water-
system-shutting-agricultural-pumps
2020-06-04 Fisher &  New Zealand Discrete  R Unknown 1 U Shut down  Victim of the Netfilim  https://icsstrive.com/incident/large-
Paykel  Mfg. appliance  ransomware group. They  amount-of-data-leaked-after-at-new-
zealand-manufacturer-refused-to-pay/
| Appliances |     | manufacturing     | refused to pay, then        |     |
| ---------- | --- | ----------------- | --------------------------- | --- |
|            |     | and distribution  | suffered a large data leak. |     |
https://stuff.co.nz/business/121849569
|     |     | ops. |     | /appliance-repairer-in-the-dark-after- |
| --- | --- | ---- | --- | -------------------------------------- |
ransomware-attack-on-fp-appliances
2020-06-09 Honda Japan, Turkey, Discrete  R EKANS 4 DS Shut down global Victim of EKANS ("Snake")  https://icsstrive.com/incident/honda-
UK, USA Mfg. plant  ransomware that spread  manufacturing-attack
|     |     | manufacturing    | to at least 4 plants. The  |                                       |
| --- | --- | ---------------- | -------------------------- | ------------------------------------- |
|     |     | ops. for 4 days  | malware spread from IT     | https://telegraph.co.uk/technology/20 |
20/06/09/hondas-global-factories-
|     |     | and delayed  | servers to the control   | brought-standstill-cyber-attack |
| --- | --- | ------------ | ------------------------ | ------------------------------- |
|     |     | vehicle      | network suggesting poor  |                                 |
|     |     | shipments    | network segmentation.    |                                 |
2020-06-09 Lion Australia Food &  R REvil 45 IA Shut down  Hit by two separate REvil  https://icsstrive.com/incident/aussie-
Bev. brewery  ransomware attacks  brewer-lion-production-hit-after-
|     |     | operations for 2+  | weeks apart, during the  | ransomware-attack/ |
| --- | --- | ------------------ | ------------------------ | ------------------ |

|     |     | weeks | early months of the Covid- |                                       |
| --- | --- | ----- | -------------------------- | ------------------------------------- |
|     |     |       | 19 pandemic.               | https://zdnet.com/article/lion-warns- |
of-beer-shortages-following-
ransomware-attack
https://smh.com.au/technology/cyber-
crisis-deepens-at-lion-as-second-
attack-bites-beer-giant-20200618-
p5540c.html
2020-07-05 X-FAB Germany,  Discrete  R Maze 6 IA Shut down all  X-FAB is a leading MEMS  https://icsstrive.com/incident/x-fab-
France,  Mfg. plants: down 2  analog/mixed-signal chip  group-targeted-by-cyberattack/
|     | Malaysia, USA | weeks at 5 sites,  | fab and fell victim to a  |                                     |
| --- | ------------- | ------------------ | ------------------------- | ----------------------------------- |
|     |               | and 1 week for     | Maze ransomware attack.   | https://businesswire.com/news/home/ |
20200705005045/en/X-FAB-Affected-
|     |     | another |     | by-Cyber-Attack |
| --- | --- | ------- | --- | --------------- |
65

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack Physical
Type Consequences
2020-09-06 Tower  Israel Discrete  R Unknown 2 IA Shut down  Tower Semi  https://icsstrive.com/incident/cyberattack-at-
Semiconductor Mfg. "several" plants manufactures  israeli-tower-semiconductor-manufacturer/

|     |     |     | integrated circuits,  | https://cisomag.com/tower-semiconductor- |
| --- | --- | --- | --------------------- | ---------------------------------------- |
and has 2 plants in
|     |     |     | Israel, 2 in the USA,  | cyberattack |
| --- | --- | --- | ---------------------- | ----------- |
and 3 in Japan.
Further details were
not made public.
2020-09-15 Bluescope Steel Australia Discrete  R Unknown 2 U Shut down  Ransomware  https://icsstrive.com/incident/bluescope-
|     | Mfg. | production, and  | infection was first  | event/ |
| --- | ---- | ---------------- | -------------------- | ------ |

|     |     | reverted to     | detected in their    | https://abc.net.au/news/2020-05-           |
| --- | --- | --------------- | -------------------- | ------------------------------------------ |
|     |     | manual          | USA-based            |                                            |
|     |     | operations for  | subsidiary, but the  | 15/bluescope-steel-cyber-attack-shut-down- |
kembla-ransomware/12251316
|     |     | some processes | attack eventually  |                                            |
| --- | --- | -------------- | ------------------ | ------------------------------------------ |
|     |     |                | impacted global    | https://securityweek.com/australian-steel- |
|     |     |                | production ops.    | maker-bluescope-hit-cyberattack/           |
2020-10-17 IPG Photonics USA Discrete  R RansomExx 2 U Shut down global The Oxford, MA  https://icsstrive.com/editorials/ransomware-
|     | Mfg. | parts          | based industrial,      | hits-ma-laser-maker                            |
| --- | ---- | -------------- | ---------------------- | ---------------------------------------------- |
|     |      | manufacturing  | medical, and military  | https://bleepingcomputer.com/news/security     |
|     |      | and shipping   | laser manufacturer     |                                                |
|     |      |                | was hit by             | /leading-us-laser-developer-ipg-photonics-hit- |
with-ransomware
RansomExx
malware.
2020-10-19 Société de  Canada Transport R RansomExx 1 $2M DS Shut down on- Montreal's transit  https://icsstrive.com/incident/montreals-
transit-service-hit-by-ransomexx-
| transport de  |     | call, door to      | service was hit by  |             |
| ------------- | --- | ------------------ | ------------------- | ----------- |
| Montréal(STM) |     | door, paratransit  | RansomExx           | ransomware/ |
https://cbc.ca/news/canada/montreal/stm-
|     |     | services for  | ransomware, and      | refused-to-pay-2-8-million-ransomware- |
| --- | --- | ------------- | -------------------- | -------------------------------------- |
|     |     | nearly a week | they refused to pay  | attack-1.5782838                       |
the $2.8 mil

|     |     |     | demanded. | https://stm.info/en/press/news/2020/the- |
| --- | --- | --- | --------- | ---------------------------------------- |
stm-completes-cyber-attack-investigation
2020-10-22 Steelcase USA Discrete  R Ryuk 1 $60M IA Shut down all  Office furniture  https://icsstrive.com/incident/ransomware-
|     | Mfg. | plants for 2    | maker was the      | shuts-furniture-maker/                     |
| --- | ---- | --------------- | ------------------ | ------------------------------------------ |
|     |      | weeks; delayed  | victim of a Ryuk   |                                            |
|     |      | $60m in         | ransomware attack  | https://bleepingcomputer.com/news/security |
/steelcase-furniture-giant-hit-by-ryuk-
|     |     | shipments to the  | that shutdown         | ransomware-attack                             |
| --- | --- | ----------------- | --------------------- | --------------------------------------------- |
|     |     | 4th quarter       | global order          |                                               |
|     |     |                   | management,           | https://mibiz.com/sections/manufacturing/cy   |
|     |     |                   | manufacturing and     | berattack-delays-60-million-in-shipments-for- |
|     |     |                   | distribution systems. | steelcase-as-pandemic-continues-to-batter-    |
office-furniture-orders
2020-10-22 Dr Reddy's  India, UK,  Pharma R Unknown 5 IA Shut down  A week after  https://icsstrive.com/incident/covid-vaccine-
Laboratories Brazil,  production at 5  agreeing to produce maker-dr-reddy-laboratories-hit-by-cyber-
attack/
|     | Russia,  | plants and     | the Sputnik V Covid-  |     |
| --- | -------- | -------------- | --------------------- | --- |
|     | USA      | stocks fell 3% | 19 vaccine for final  |     |
https://businessinsider.in/india/news/dr-
|     |     |     | trials, Dr Reddy's  | reddys-shares-fell-over-3-the-drug-maker-  |
| --- | --- | --- | ------------------- | ------------------------------------------ |
|     |     |     | was subject to a    | isolated-all-data-service-centers-after-a- |
|     |     |     | ransomware attack.  | cyber-attack/articleshow/78806238.cms      |
https://thehindu.com/business/Industry/oct-
22-data-breach-involved-a-ransomware-
attack-dr-reddys/article32962438.ece
2020-10-25 Stelco  Canada Discrete  U Unknown 1 U Shut down steel  The company has  https://icsstrive.com/incident/canadian-
Mfg. production,  reported the  stelco-temporarily-suspended-operations/
|     |     | temporarily | incident to law  |     |
| --- | --- | ----------- | ---------------- | --- |
enforcement and did https://insurancebusinessmag.com/ca/news/
cyber/stelco-reveals-information-systems-
|     |     |     | not give further  | were-subjected-to-a-criminal-attack- |
| --- | --- | --- | ----------------- | ------------------------------------ |
|     |     |     | details.          | 237287.aspx                          |
2020-12-13 Symrise  Germany Process  R Cl0p 1 IA Shut down  The flavor and  https://icsstrive.com/incident/german-flavor-
Mfg. production out of fragrance  manufacturer-symrise-preventively-shut-
down-operations/
|     |     | abundance of  | manufacturer was   |                                            |
| --- | --- | ------------- | ------------------ | ------------------------------------------ |
|     |     | caution       | hit by a Cl0p      |                                            |
|     |     |               | ransomware attack  | https://bleepingcomputer.com/news/security |
/flavors-designer-symrise-halts-production-
|     |     |     | which limited sales  | after-clop-ransomware-attack |
| --- | --- | --- | -------------------- | ---------------------------- |
growth below
https://handelsblatt.com/unternehmen/indust
target.
rie/mdax-konzern-hacker-legen-symrise-lahm-
warum-der-fall-besonders-schwerwiegend-
ist/26718680.html
2020-12-15 Forward Air  USA Transport R Hades 1 $7.5M ID Shut down  Hades ransomware  https://icsstrive.com/incident/ransomware-
|     |     | operations and  | gang attack  | attack-at-forward-air/ |
| --- | --- | --------------- | ------------ | ---------------------- |

|     |     | delayed          | impacted data  |                                           |
| --- | --- | ---------------- | -------------- | ----------------------------------------- |
|     |     | shipments for a  | exchange with  | https://freightwaves.com/news/news-alert- |
forward-air-reveals-ransomware-attack-
|     |     | week | customers, leading  | warns-of-revenue-hit |
| --- | --- | ---- | ------------------- | -------------------- |
|     |     |      | to delivery delays  |                      |
which impacted
https://freightwaves.com/news/news-alert-
|     |     |     | financial results. | forward-airs-systems-coming-back-online |
| --- | --- | --- | ------------------ | --------------------------------------- |

https://zdnet.com/article/trucking-company-
forward-air-said-its-ransomware-incident-
cost-it-7-5-million
66

Incidents from 2018-2019
Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack Physical
Type Consequences
2018-08-03 Taiwan  Taiwan Discrete  R WannaCry 3 $255 I3 Shut down  WannaCry ransomware  https://icsstrive.com/incident/tsmc-
Semiconductor  Mfg. m operations at  caused the outage.  hit-by-wannacry-variant/
Manufacturing  Tainan, Hsinchu  Supplier installed software
Co (TSMC) and Taichung;  on some machines  https://itpro.com/security/31629/tsmc
-cyber-attack-was-apparently-caused-
|     | Lost 3% in        | accidentally infected with  | by-wannacry |
| --- | ----------------- | --------------------------- | ----------- |
|     | quarterly revenue | the malware, without        |             |
running AV.
2019 Unknown gas  USA Oil & Gas R Unknown 1 DS Shut down  Attackers used spear  https://icsstrive.com/incident/us-
natural-gas-compression-facility-shut-
| pipeline | pipeline for 2  | phishing to gain initial   |                                  |
| -------- | --------------- | -------------------------- | -------------------------------- |
|          | days            | access to the IT network,  | down-entire-pipeline-for-2-days/ |

|     |     | easily pivoting into the OT  | https://securityweek.com/operations- |
| --- | --- | ---------------------------- | ------------------------------------ |
network due to poor
us-natural-gas-facilities-disrupted-
|     |     | segmentation. Then, they  | ransomware-attack |
| --- | --- | ------------------------- | ----------------- |
|     |     | planted ransomware.       |                   |
https://cisa.gov/news-
events/cybersecurity-advisories/aa20-
049a
2019-02-28 Hoya  Thailand Discrete  U Unknown 1 ID Partially shut  Around 100 computers  https://icsstrive.com/incident/hoya-
Corporation Mfg. down production  were infected by  corporation-hit-by-cyberattack/
|     | for 3 days,      | credential stealing  |                                    |
| --- | ---------------- | -------------------- | ---------------------------------- |
|     | dropping output  | malware, and         | https://www.bleepingcomputer.com/n |
ews/security/cyber-attack-shuts-
|     | by 60% | subsequently infected  | down-hoya-corps-thailand-plant-for- |
| --- | ------ | ---------------------- | ----------------------------------- |
with a cryptojacker
three-days/
|     |     | (mining) malware.         |                                      |
| --- | --- | ------------------------- | ------------------------------------ |
|     |     | Following the initial     | https://english.kyodonews.net/news/2 |
|     |     | attack, workers were not  | 019/04/7d3dc3094e3a-hoya-hit-by-     |
cyberattack-in-feb-disrupting-thai-
|     |     | able to keep up with  | factory-operations.html |
| --- | --- | --------------------- | ----------------------- |
orders and so
manufacturing output fell
for 3 days before
resuming.
2019-03-18 Norsk Hydro Norway Metals &  R LockerGog 10 $71m ID Halted  Infected by LockerGoga  https://icsstrive.com/incident/producti
Mining a production at all  ransomware. initially  on-lines-stopped
|     | rolled (sheet) &  | spread at Norsky Hydro     |                                      |
| --- | ----------------- | -------------------------- | ------------------------------------ |
|     | extruded          | through phishing email on  | https://news.microsoft.com/source/fe |
atures/digital-transformation/hackers-
|     | aluminum plants  | the IT network, then  | hit-norsk-hydro-ransomware-company- |
| --- | ---------------- | --------------------- | ----------------------------------- |
|     | and at their     | deploying via the AD  | responded-transparency              |
building products controller.
|     | plant |     | https://industrialcybersecuritypulse.co |
| --- | ----- | --- | --------------------------------------- |
m/facilities/throwback-attack-norsk-
hydro-gets-hit-by-lockergoga-
ransomware
2019-07-26 City Power  South  Power R Unknown 1 ID Power outage for Ransomware encrypts the  https://icsstrive.com/incident/ransom
Johannesburg Africa 250k customers  IT system, preventing  ware-attack-at-electricity-provider-for-
johannesburg-sa/
|     | and delayed  | customers on pre-paid  |     |
| --- | ------------ | ---------------------- | --- |
|     | restoration  | plans from purchasing  |     |
https://twitter.com/CityPowerJhb/stat
|     |     | electricity, and hampering  | us/1154277777950093313 |
| --- | --- | --------------------------- | ---------------------- |
line crews’ efforts to

|     |     | restore localized  | https://bbc.com/news/technology- |
| --- | --- | ------------------ | -------------------------------- |
|     |     | blackouts.         | 49125853                         |
2019-09-27 Rheinmetall Germany Discrete  U Unknown 3 €6M ID Disrupted  Rheinmetall's civilian  https://icsstrive.com/incident/malware
Mfg. production  automotive production  -attack-disrupts-multiple-sites-of-
|     | significantly for 2 business was impacted  |     | rheinmetal-ag-causing-shares-to-drop/ |
| --- | ------------------------------------------ | --- | ------------------------------------- |

|     | weeks at      | after a malware attack,  |                                     |
| --- | ------------- | ------------------------ | ----------------------------------- |
|     | locations in  | requiring a complete     | https://www.reuters.com/article/us- |
rheinmetall-malware-idUSKBN1WC0LH
|     | United States,  | rebuild of the IT network  |     |
| --- | --------------- | -------------------------- | --- |
|     | Mexico, and     | expected to take a         |     |
|     | Brazil          | minimum of 2 weeks.        |     |
67

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
Actor Actor Attack Physical
Type Consequences
2019-10-13 Pilz Germany Discrete  R BitPaymer 1 IA Shut down  Slowdown due to  https://icsstrive.com/incident/ransomware
Mfg. systems,  impaired order  -attack-automation-supplier-pilz-down/
| reverted to       | tracking, due to      |                                            |
| ----------------- | --------------------- | ------------------------------------------ |
| manual ops., and  | BitPaymer ransomware  | https://drivesncontrols.com/news/fullstory |
.php/aid/6191/Pilz_is_recovering_from_a_
| slowed  | attack. | _91major_92_ransomware_attack.html |
| ------- | ------- | ---------------------------------- |
production for 1
week
2019-12-16 Unknown MTSA  USA Transport R Ryuk 1 DS Infected ICS that  A MTSA-regulated  https://icsstrive.com/incident/ransomware
facility monitors cargo  facility suffered a  -takes-down-maritime-facility/
| transfer and      | ransomware attack       |                                       |
| ----------------- | ----------------------- | ------------------------------------- |
| encrypted files,  | that encrypted both IT  | https://www.bleepingcomputer.com/news |
/security/us-coast-guard-says-ryuk-
| lost critical    | and OT systems. The     | ransomware-took-down-maritime-facility/ |
| ---------------- | ----------------------- | --------------------------------------- |
| process control  | USCG said that initial  |                                         |
| and monitoring   | access was gained       | https://maritime-                       |
executive.com/article/uscg-cyberattack-
| systems, forced  | likely through phishing,  |                                        |
| ---------------- | ------------------------- | -------------------------------------- |
| an operational   | encrypted both IT and     | penetrated-operating-controls-of-isps- |
facility
| shutdown for  | OT networks, forcing  |     |
| ------------- | --------------------- | --- |
| more than 30  | an operational        |     |
https://www.dco.uscg.mil/Portals/9/DCO
| hours | shutdown. | %20Documents/5p/MSIB/2019/MSIB_10_19. |
| ----- | --------- | ------------------------------------- |
pdf?ver=2019-12-23-134957-667
2019-12-20 RavnAir Alaska USA Transport R Unknown 1 ID Canceled Dash- Canceled Dash-8  https://icsstrive.com/incident/airline-hit-
| 8-100 flights for  | flights because       | by-cyber-attack-cancels-flights/          |
| ------------------ | --------------------- | ----------------------------------------- |
| 24 hours           | cyberattack caused    |                                           |
|                    | outage of the Dash-8  | https://theregister.com/2020/01/02/ravnai |
r_ransomware_dhc_dash_8
maintenance system
and its backup, which
is required for flight.
68

Incidents from 2010-2017
Date Victim Region Industry Threat Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
| Actor | Actor Attack Physical  |     |     |     |
| ----- | ---------------------- | --- | --- | --- |
Type Consequences
2010-07-15 Natanz Nuclear Iran Process  NS Unknown/S 1 DO Destroyed 1000  Plant was infected by  https://icsstrive.com/incident/malware-
Enrichment  Mfg. tuxnet centrifuges at  the Stuxnet worm in a  targets-uranium-enrichment-facility/

| Plant |     | Natanz | targeted attack      |                                       |
| ----- | --- | ------ | -------------------- | ------------------------------------- |
|       |     |        | designed to disrupt  | https://en.wikipedia.org/wiki/Stuxnet |
Iran's nuclear
enrichment program.
2012-04-22 Iran's main oil  Iran Oil & Gas NS Unknown/F 6 DO Shut down 6  6 terminals ops.  https://icsstrive.com/incident/iranian-oil-
terminal-offline-after-malware-attack/
| export  | lame | terminals | affected by Flame  |     |
| ------- | ---- | --------- | ------------------ | --- |
terminals malware. News outlets  https://www.bbc.com/news/technology-
confirm outage, despite 17811565

|     |     |     | Iran downplaying the  | https://computerworld.com/article/27272 |
| --- | --- | --- | --------------------- | --------------------------------------- |
attack's effects.
19/attacks-on-iranian-oil-industry-led-to-
flame-malware-find.html
2012-07-22 Natanz and  Iran Process  U Unknown 2 DO Shut down 2  Mikko Hypponen at F- https://icsstrive.com/incident/natanz-and-
Fordow  Mfg. plants Secure reports a  fordo-facilities-closed-down-automation-
Nuclear  scientist claiming to be  network-after-new-worm-targeted-irans-
nuclear-program/
| Enrichment  |     |     | with Iran's Atomic   |     |
| ----------- | --- | --- | -------------------- | --- |
| Plants      |     |     | Energy Organization  |     |
https://web.archive.org/web/20150511100
|     |     |     | asked for help  | 332/ |
| --- | --- | --- | --------------- | ---- |
following an attack on
https://www.washingtonpost.com/blogs/
Siemens PLCs.
worldviews/post/iranian-nuclear-facilities-
are-hit-by-acdc-
virus/2012/07/25/gJQAqfRz8W_blog.html

https://web.archive.org/web/20160428132
811/
http://www.bloomberg.com/news/articles
/2012-07-25/iranian-nuclear-plants-hit-by-
virus-playing-ac-dc-website-says
2012-10 Unknown  USA Power U Unknown /  1 DO Delayed turbine  10 plant PCs were  https://icsstrive.com/incident/virun-
Power Plant Mariposa  restart (thus  infected by Mariposa  infection-in-turbo-control-system-at-us-
|     | BotNet | power  | malware variant,  | electric-utility/ |
| --- | ------ | ------ | ----------------- | ----------------- |

|     |     | generation) by 3  | transmitted through a  | https://us- |
| --- | --- | ----------------- | ---------------------- | ----------- |
|     |     | weeks             | USB stick. Occurred    |             |
cert.gov/sites/default/files/Monitors/ICS-
|     |     |     | during scheduled  | CERT_Monitor_Oct-Dec2012.pdf |
| --- | --- | --- | ----------------- | ---------------------------- |
shutdown for
maintenance.
2014-12-22 German steel  Germany Metals &  U Unknown 1 DO Caused "massive  Sophisticated attack  https://icsstrive.com/incident/cyber-
mill Mining damage" to plant using spear phishing  attack-at-german-steel-mill-damages-
|     |     | equipment | and ICS knowledge to  | equipment/ |
| --- | --- | --------- | --------------------- | ---------- |

|     |     |     | disable the control  | https://bbc.com/news/technology- |
| --- | --- | --- | -------------------- | -------------------------------- |
|     |     |     | system, causing an   | 30575104                         |
uncontrolled shutdown
of the blast furnace.
2015-12-23 Prykarpattyaob Ukraine Power NS Sandworm  32 DO Power outage  First publicly known  https://icsstrive.com/incident/225k-
lenergo,  [GRU Unit  lasts up to 6  attack on a power grid  customers-without-power-in-ukraine-
power-grid-hack/
Chernivtsioblen 74455]/Bla hours affecting  occurs when threat
| ergo, and  | ckEnergy 3  | 230K people | actor Sandworm  |     |
| ---------- | ----------- | ----------- | --------------- | --- |
https://en.wikipedia.org/wiki/2015_Ukraine
Kyivoblenergo  (Russia) deploys BlackEnergy 3  _power_grid_hack
|     |     |     | malware into the  |     |
| --- | --- | --- | ----------------- | --- |
utility's network.
https://arstechnica.com/information-
technology/2016/01/first-known-hacker-
caused-power-outage-signals-troubling-
escalation
2016-08-16 AW North  USA Discrete  R Unknown 1 $1M DS Shut down ops.  Just-in-time  https://icsstrive.com/incident/ransomwar
Carolina Mfg. for 4 hours, and  transmission  e-attack-at-aw-north-carolina-shuts-
down-operations-for-4-hours/
|     |     | caused a ripple  | component supplier to  |     |
| --- | --- | ---------------- | ---------------------- | --- |
|     |     | delay effect in  | Toyota, Honda and      |     |
https://www.isssource.com/users-
|     |     | the auto supply  | others is hit by  | learning-but-ransomware-still-a-problem/ |
| --- | --- | ---------------- | ----------------- | ---------------------------------------- |
|     |     | chain            | ransomware that   |                                          |
slipped through firewall https://industrialcybersecuritypulse.com/t
|     |     |     | and AV software  | hreats-vulnerabilities/throwback-attack- |
| --- | --- | --- | ---------------- | ---------------------------------------- |
|     |     |     | defenses.        | aw-north-carolina-attack-shows-dangers-  |
of-ransomware-and-just-in-time-
manufacturing

https://apnews.com/article/nc-state-wire-
north-america-us-news-ap-top-news-
north-carolina-
e316bd63f21a4fd181b3fb4a8dd7a5ba
69

Date Victim Region Industry Threat  Threat  Sites Cost SEC OT  OT / ICS  Incident Summary References
|     | Actor | Actor Attack Physical  |     |     |     |
| --- | ----- | ---------------------- | --- | --- | --- |
Type Consequences
2016-12-13 Ukrzaliznytsia  Ukraine Transport NS Sandworm  1 DIP Impacted online  A SandWorm attack on  https://icsstrive.com/incident/ukrainian-
(Ukrainian State  [GRU Unit  ticket purchasing Ukrainian rail used the  railway-company-ukrzaliznytsia-hit-by-
cyberattack/
| Railway) |     | 74455]/Bla  | and train    | KillDisk wiper malware  |     |
| -------- | --- | ----------- | ------------ | ----------------------- | --- |
|          |     | ckEnergy 3  | scheduling;  | to disable online       |     |
https://www.industrialcybersecuritypulse.c
& KillDisk  delayed both  ticketing systems,  om/hacks-attacks/throwback-attack-
|     |     | (Russia) | passenger and  | creating chaos and  |     |
| --- | --- | -------- | -------------- | ------------------- | --- |
ukrainian-railway-hit-by-cyberattack-
|     |     |     | freight traffic  | confusion for        | stranding-passengers/ |
| --- | --- | --- | ---------------- | -------------------- | --------------------- |
|     |     |     | during the       | passengers and rail  |                       |
|     |     |     | holiday season   | staff.               |                       |
2016-12-17 Pivnichna  Ukraine Power NS Sandworm  1 DO Power outage for Sandworm suspected  https://icsstrive.com/incident/attack-on-
substation, Kyiv [GRU Unit  20% of Kyiv for  in deploying  kyiv-power-substation-shut-down-remote-
|     |     | 74455]/Ind | over 1 hour | Industroyer (also:  | terminals/ |
| --- | --- | ---------- | ----------- | ------------------- | ---------- |

ustroyer  CrashOverride)  https://en.wikipedia.org/wiki/2016_Kyiv_cy
|     |     | (Russia) |     | malware, by exploiting  | berattack                            |
| --- | --- | -------- | --- | ----------------------- | ------------------------------------ |
|     |     |          |     | a vulnerability in      |                                      |
|     |     |          |     | Siemens SIPROTEC        | https://arstechnica.com/information- |
technology/2017/06/crash-override-
relays.
malware-may-sabotage-electric-grids-but-
its-no-stuxnet
2017-05-12 Renault-Nissan France,  Discrete  R WannaCry  5 DS Shut down plants WannaCry  https://icsstrive.com/incident/wannacry-
Slovenia,  Mfg. /  in Douai,  ransomware, spread by affects-operations-at-several-renault-
plants/
|     | Romania,  | EternalBlue | Sandouville,        | the EternalBlue exploit  |     |
| --- | --------- | ----------- | ------------------- | ------------------------ | --- |
|     | India     |             | Slovenia, Pitesti,  | originally developed by  |     |
https://industrialcybersecuritypulse.com/f
|     |     |     | and Chennai for 1 the NSA and later  |            | acilities/throwback-attack-wannacry- |
| --- | --- | --- | ------------------------------------ | ---------- | ------------------------------------ |
|     |     |     | day                                  | leaked by  |                                      |
ransomware-takes-renault-nissan-plants-
|     |     |     |     | ShadowBrokers, hit 5  | offline |
| --- | --- | --- | --- | --------------------- | ------- |
plants for 1 day.
2017-06-27 Many, incl. AP  Global Multi NS NotPetya 1 $10B I3 Outages  NotPetya malware,  https://icsstrive.com/incident/petya-
Moller-Maersk,  throughout many created by Russian  ransomware-attack-affects-operations-at-
JNPT Gateway  industries: one  actors targeting  terminal-of-indias-largest-container-port-
jnpt/
| Terminals India  |     |     | incident,  | Ukraine, spreads  |     |
| ---------------- | --- | --- | ---------- | ----------------- | --- |
| (GTI), Merck     |     |     | countless  | indiscriminately  |     |
https://wired.com/story/notpetya-
Pharmaceutical,  victims; Shut  through networks using cyberattack-ukraine-russia-code-crashed-
Royal Canin down ops. At  the EternalBlue exploit,  the-world
|     |     |     | JNPT GTI  | permanently  |     |
| --- | --- | --- | --------- | ------------ | --- |
https://timesofindia.indiatimes.com/india/i
|     |     |     | Terminal. | encrypting data. | ndias-largest-container-port-jnpt-hit-by- |
| --- | --- | --- | --------- | ---------------- | ----------------------------------------- |
ransomware/articleshow/59346704.cms

https://www.ebervet.com/pet-food-
impacted-cyber-attack/
2017-08 Petro Rabigh  Saudi  Oil & Gas NS Central  1 DO Shut down one  Triton malware  https://icsstrive.com/incident/safety-
Petrochemical  Arabia Scientific  plant, twice employed to infect and instrumented-system-is-disabled-by-
| Refinery |     | Research  |     | reprogram Triconex  | malware/ |
| -------- | --- | --------- | --- | ------------------- | -------- |

|     |     | Institute of  |     | safety systems. This  |     |
| --- | --- | ------------- | --- | --------------------- | --- |
Chemistry  triggered an automatic dec/15/triton-hackers-malware-attack- https://theguardian.com/technology/2017/
|     |     | and        |     | shutdown, alerting    | safety-systems-energy-plant      |
| --- | --- | ---------- | --- | --------------------- | -------------------------------- |
|     |     | Mechanics  |     | operations. Occurred  |                                  |
|     |     | [CNIIHM]/T |     | twice.                | https://cbsnews.com/news/russia- |
cyberattacks-60-minutes-2022-04-17
riton
(Russia)
70

APPENDIX B –
Sources and Acknowledgements
The authors thank and acknowledge the contributions of many incident repositories, reports,
blogs, reporters, and other data sources that the authors drew upon to create this data set,
including but not limited to:
Alerts and advisories From the Canadian Centre for cyber.gc.ca/en/alerts-advisories
Cyber Security
BlackFog - The State of Ransomware 2024 blackfog.com/the-state-of-ransomware-2024
Center for Strategic & Int'l Studies: Significant csis.org/programs/strategic-Tech-program/significant-cyber
Cyber Incidents incidents
CERT-EU Cyber Security Briefs and Threat cert.europa.eu/publications/threat-intelligence/2023
Intelligence Reports
Check Point Research - 2024 research.checkpoint.com/2024
CIO Magazine (Germany): “These companies have www.cio.de/a/diese-unternehmen-hat-s-schon-erwischt
already been hit”
Cloudian - Ransomware Attack List and Alerts cloudian.com/ransomware-attack-list-and-alerts
Cyber Management Alliance - Cybersecurity Blog cm-alliance.com/cybersecurity-blog
Cyber Security Incident Database (dot net) csidb.net
Cybercrime Info NL - Actuele cyberaanvallen, ccinfo.nl/menu-nieuws-trends/actuele-cyberaanvallen
datalekken, dreigingen en trends - Deze week
CyberMaterial - Incidents cybermaterial.com/incidents
DataBreaches.Net The Office of Inadequate databreaches.net
Security
DSGVO Portal Data breaches, cyber attacks and dsgvo-portal.de/sicherheitsvorfall-datenbank
vulnerabilities
European Repository of Cyber Incidents (EuRepoC) eurepoc.eu
Halcyon Recent Ransomware Attacks ransomwareattacks.halcyon.ai
ICS STRIVE Industrial Control System incident icsstrive.com
repository
ICS-SCADA incidents securityaffairs.co/wordpress/category/ics-scada
71

Jam Cyber List of Successful Cyber Attacks and jamcyber.com/discover/cyber-attacks
Data Breaches
KonBriefing / Cyberattacks, Hacker attacks, konbriefing.com/en-topics/cyberattacks.html
Ransomware attacks
Monthly Data Breaches and Cyber Attacks Archive itgovernance.co.uk/blog/category/monthly-data-breaches-and-
cyber-attacks
NHL Stenden's MCAD Maritime Cyber Attack maritimecybersecurity.nl
Database (Dr. Stephen McCombie)
Office of the Information and Privacy oipc.ab.ca/decisions/breach-notification-decisions
Commissioner of Alberta - Breach Notification
Decisions
Publicly disclosed U.S. ransomware attacks in 2023 techtarget.com/searchsecurity/feature/Publicly-disclosed-US-
ransomware-attacks-in-2023
Ransomware Attack List and Alerts cloudian.com/ransomware-attack-list-and-alerts
Ransomware Report: Latest Attacks And News cybersecurityventures.com/ransomware-report
Red Hot Cyber - Italian Cyber Attacks redhotcyber.com/post/category/attacchi-informatici-italiani
RedPacket Security: Ransomware www.redpacketsecurity.com/category/ransomware
TechTarget's LeMagIT – Recherche lemagit.fr/recherche
Ti Safe Incident Hub hub.tisafe.com/base-de-dados
Upstream AutoThreat Intelligence Cyber Incident upstream.auto/research/automotive-cybersecurity
Repository
Dominic Aliveri, Cybersecurity analyst and security @AlvieriD (Twitter/X)
researcher
Eduardo Kovacs, Contributing Editor, SecurityWeek @EduardKovacs (Twitter/X)
FalconFeeds.io’s Twitter/X feed @FalconFeedsio (Twitter/X)
72