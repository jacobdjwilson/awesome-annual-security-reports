Organization: BeazleySecurity
Report Title:  Quarterly-Threat-Report-Q4
Year:          2025

# Quarterly Threat Report: Fourth Quarter, 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [Q4 2025 Key Takeaways](#q4-2025-key-takeaways)
- [Observations in the Threat Landscape](#observations-in-the-threat-landscape)
  - [Infostealer Trends: Operation ENDGAME Creates a Highly Dynamic Market](#infostealer-trends-operation-endgame-creates-a-highly-dynamic-market)
  - [Scattered Spider, LAPSUS$, and ShinyHunters Activity](#scattered-spider-lapsus-and-shinyhunters-activity)
  - [Agentic AI Trends Influencing the Threat Landscape](#agentic-ai-trends-influencing-the-threat-landscape)
- [Vulnerability Trends and Overview](#vulnerability-trends-and-overview)
  - [High-impact Breaches and Zero-day Vulnerabilities Exploited in the Wild](#high-impact-breaches-and-zero-day-vulnerabilities-exploited-in-the-wild)
- [Quarterly Ransomware Review](#quarterly-ransomware-review)
  - [Emerging Ransomware Actors and TTPs](#emerging-ransomware-actors-and-ttps)
  - [How Ransomware Attackers Gained Access in Q4](#how-ransomware-attackers-gained-access-in-q4)
- [Quarterly BEC Review](#quarterly-bec-review)
- [Beazley Security MDR Trends and Overview](#beazley-security-mdr-trends-and-overview)
- [Sources](#sources)

## Executive Summary

The final quarter of 2025 reinforced a hard truth for defenders: the window between exposure and impact is closing faster than most organizations can react. Across ransomware, business email compromise, and vulnerability exploitation incidents, attackers increasingly relied on speed, stolen credentials, and abusing trusted infrastructure rather than novel malware or complex exploits.

Beazley Security Labs observed a continued acceleration in the "time to exploit" cycle, with multiple vulnerabilities abused in the wild as “zero days”, that is, before vendors released patches —and often before public disclosure. Internet-facing systems, identity providers, and remote access infrastructure remained the most reliable entry points for threat actors. Organizations who use edge devices affected by a zero-day vulnerability should assume compromise and treat it as a potential breach.

Ransomware activity remained consistently high throughout Q4. While reported ransomware incidents stabilized after an August peak, leak site post activity surged nearly 50%, with threat actors increasingly willing to escalate public pressure when negotiations stall. Established groups Akira and Qilin continued to be the most active; however, Beazley Security observed a mix of newly branded operators and "lone wolf" actors enter the ecosystem. Trends suggest the ransomware community is growing slightly more dispersed, accommodating new opportunistic threat actors.

Business email compromise (BEC) accounted for more than a third of reported cyber incidents in Q4. Unlike ransomware deployments, these attacks rarely trigger alarms or display visible signs of compromise but can quickly lead to financial losses. Threat actors continued to abuse valid credentials, bypassing traditional MFA through session hijacking, token replay, and MFA fatigue. Nearly half of successful BEC cases investigated occurred in environments where MFA was already enabled, underscoring that identity attacks (not malware) remain an impactful attack vector.

Beazley Security's Managed Detection and Response (MDR) telemetry in Q4 mirrored this. Detections were increasingly concentrated in identity-based attacks and reconnaissance, which accounted for more than half of observed activity. While overall threat activity remained steady, improved security controls stopped more intrusions early, limiting attacker progression and reducing the impact of malware on endpoints. This reflects both progress and emerging risk: defenses are disrupting attacks sooner, but identity and perimeter-based campaigns are becoming faster, more automated, and more frequent.

Over 12,800 new vulnerabilities were disclosed in Q4, with a sharp increase in those that Beazley Security Labs (BSL) deemed critical enough to issue advisories for our clients and stakeholders. A concerning trend continued to grow, where a number of vulnerabilities were already being actively exploited by threat actors in the wild before vendors became aware of them. High-impact campaigns targeting firewalls, Windows update infrastructure, and commonly implemented web frameworks demonstrated how attackers continue to abuse widely deployed and trusted platforms to scale their attacks.

Attackers are moving faster and leaning more heavily on social engineering and identity attacks to gain access. In 2026, resilience will come from getting the fundamentals right, including phishing-resistant authentication, consistent patching, and awareness of emerging exploits, and the ability to quickly detect and disrupt intrusions before they escalate.

This report explores how these trends played out across observed incidents in Q4, and the insights drawn from these activities.

## Q4 2025 Key Takeaways

- **Patching speed now defines risk.** The gap between vulnerability disclosure and active exploitation continued to shrink in Q4, with multiple campaigns exploiting systems before patches were made available by vendors. Known exposure during a zero-day window should be treated as a potential breach scenario and investigated accordingly.
- **Identity is the primary attack surface.** Compromised credentials were the most common initial access vector across observed ransomware and business email compromise (BEC) incidents. Attackers increasingly bypassed traditional MFA using session hijacking, token replay, and push fatigue techniques. Nearly 50% of the BEC attacks that Beazley Security responded to in Q4 bypassed traditional MFA.
- **BEC represented over one third of reported incidents**, targeting service-heavy industries where trusted communications and financial workflows can be abused at scale.
- **Beazley Security MDR telemetry showed a marked shift toward early-stage detection and containment**, with fewer intrusions progressing to lateral movement or payload deployment. This reflects the effective controls and containment capabilities of our MXDR service, but also confirms attackers are accelerating their initial access attempts.
- **Threat actors continue to abuse trusted platforms to maximize reach.** Firewalls, update systems, identity services, and popular web frameworks remained frequently targeted, enhancing exploitation across the internet.
- **Law enforcement crackdowns continue to influence infostealer market stability**, with service and actor turnover being filled with emerging players like StealC.
- **The “SHSL” extortion collective continued to grow and escalate impact through the end of 2025** with aggressive social engineering campaigns and public data leak threats, including launch of the ShinySp1der RaaS platform.
- **Threat actors observed using AI-driven reconnaissance**, deepfake social engineering, and automated intrusion workflows to accelerate operations.

## Observations in the Threat Landscape

### Infostealer Trends: Operation ENDGAME Creates a Highly Dynamic Market

The cybercriminal infostealer market continues to be in a constant state of flux due to law enforcement pressure and continued attempts by law enforcement to disrupt the infostealer ecosystem. In Q2 of 2025, the US DOJ led an effort dubbed Operation ENDGAME to take down a large amount of infrastructure for Lumma Stealer, which at the time was the largest infostealer provider in cybercrime communities. While Lumma Stealer was disrupted temporarily, Operation ENDGAME did little to curb market demand for credential theft services, and for a time the “Rhadamanthys” infostealer was able to fill the void, as we highlighted in our Q3 Threat Report.

However, this infostealer’s reign was short-lived, as the next “season” of Operation ENDGAME targeted Rhadamanthys directly in November, resulting in infrastructure seizures by German law enforcement. While law enforcement activity hasn’t completely shut down either family, interruption to operations has reduced trust and caused reputational damage to these cybercriminals, resulting in an observable dip in adoption of their “products.”

By the end of Q4, Beazley Security Labs saw no clear successor as the dominant infostealer in the market, though many families are trying to establish dominance. One of the notable families observed by Beazley Security Labs in late 2025 is a new infostealer named “StealC.”

![Figure 1: VT Infostealer Submissions]

StealC has been advertised on Russian-speaking dark web forums since January 2023. A relatively newer malware reportedly based off older infostealers, StealC had a spike in submissions to VirusTotal starting after Operation Endgame “Season Three” takedowns against Rhadamanthys last quarter. The suspected creator of StealC, who goes by the handle “Plymouth,” originally advertised services on July 29th, 2025, but was relatively quiet throughout Q3 and Q4.

After observing a surge of infostealer samples within VirusTotal, Beazley Security Labs identified additional advertisement attempts by the threat actor in December, stating “we are returning” with the modern infostealer’s capabilities. We’ve included a screenshot of a post on a monitored dark web market below:

![Figure 2: StealC Infostealer advertisement on Cybercriminal Forum]

The ongoing churn within criminal marketplaces observed in Q4 illustrates that infostealer services continue to operate as mature commercial enterprises. As law enforcement creates disruptions to existing players, these voids are rapidly filled by the next cybercriminal motivated to cash in on the significant opportunity.

### Scattered Spider, LAPSUS$, and ShinyHunters Activity

Throughout the last half of 2025, activity tied to Scattered Spider and affiliated extortion groups has drawn increasing attention, with operations combining zero-day exploitation, insider access abuse, and data-leak-driven pressure campaigns. The group’s capabilities reflect an aggressive blend of technical capability, exploitation of business processes, and public reach to extort and maximize impact toward victims.

In August 2025, ShinyHunters began formalizing a high-visibility operational partnership with LAPSUS$ and Scattered Spider, forming the extortion-focused collective known as Scattered LAPSUS$ Hunters or SHSL. The collaboration expressly combined ShinyHunters’ access to large-scale stolen datasets and breach infrastructure with LAPSUS$’s high-visibility, media-driven extortion tactics and Scattered Spider’s advanced social engineering and SaaS intrusion capabilities. SHSL significantly enhanced ShinyHunters’ reach beyond underground data markets, increasing public exposure, intensifying ransom pressure, and enabling faster monetization of compromises.

A significant development in the latter half of 2025 involved the weaponization of an Oracle E-Business Suite (EBS) 0-day vulnerability, later tracked as CVE-2025-61882. The flaw enabled unauthenticated remote code execution on affected servers and was believed to have been exploited in the wild as early as August 2025 by the Cl0p ransomware group, with substantial impact on its victims. Tensions inside cybercriminal communities escalated after the exploit code surfaced on Telegram, where members associated with Scattered Spider claimed a low-level actor in their group had either leaked or sold the exploit to Cl0p ransomware operators. While the exact motive remains unclear, the disclosure likely served to gain attention, boost reputation, and undermine Cl0p as a competitor. Oracle publicly acknowledged the vulnerability on October 4th, after which Beazley Security Labs released a detailed advisory on the flaw.

As the group continued to gain attention, law enforcement operations intensified, targeting criminal infrastructure tied to the SHSL collective. One such disruption occurred when the FBI and international partners seized a high-visibility extortion leak site used to target Salesforce and its customers. The operators behind the site claimed to possess approximately one billion records associated with Salesforce customer data and issued ransom demands threatening public exposure. Listed victims included global brands such as Disney, McDonald’s, IKEA, and Home Depot.

![Figure 3: SHSL Leak site Later Seized by LawEnforcement]

Although the group later established new infrastructure, the initial takedown highlighted growing law enforcement pressure on the collective. Ultimately, Salesforce worked with customers and stated there was no evidence of a breach, publicly denying the actor’s claims and refusing to engage in ransom demands. As of this writing, none of the Salesforce customer data has been publicly leaked on the re-established SHSL site.

In Q4, “ShinySp1d3r” emerged as a new ransomware-as-a-service (RaaS) platform, with its leak site attributed to SHSL and other threat actors operating in the space. The collective is believed to have carried out the launch to strengthen extortion capability and drive payment from future victims.

A sample of the ShinySp1d3r ransomware locker surfaced on VirusTotal in November and is likely built with intentions to distribute to future affiliate operators. Below is an example sourced by Bleeping Computer showing the locker place a ransom notification in place of a Windows desktop wallpaper.

![Figure 4: ShinySp1d3r Wallpaper after Ransomware deployment - Credit: BleepingComputer]

While the RaaS platform does not appear widely active at this time, it claims to be backed by a full-featured locker, and its emergence may be attractive to future financially motivated affiliates that want in on the opportunity.

### Agentic AI Trends Influencing the Threat Landscape

The end of 2025 proved that AI capabilities continue to develop far faster than most organizations can securely adopt them. While we are not yet seeing armies of autonomous attack agents battle armies of automated defenders as some researchers predicted, Beazley Security has observed threat actors leveraging AI in ways that automate and enhance their operations.

The most visible examples are in AI-enhanced social engineering attacks over the past year, where increasingly convincing, AI-created “deepfake” voice and video media are used to improve the chances of obtaining sensitive data and credentials from intended victims. Moving beyond these social engineering attacks, threat actors have been observed creating fake productivity applications as demonstrated in the EvilAI toolset reported by Trend Micro.

Other efforts leveraging AI to automate and enhance existing attack capability were described by a much publicized Anthropic article detailing how they disrupted a threat actor using Claude Code in a real world cyber-attack campaign. The threat actor, assessed by Anthropic to be a nation state APT, used Claude in various stages of their attack to automate processes in nearly every step of the attack chain, from infrastructure reconnaissance to analysis of stolen data.

Beazley Security itself was also targeted by what appeared to be AI “vibe coded” phishing infrastructure in an attack attempt during the quarter. A phishing email sent to a Beazley Security email distribution group was quickly identified and shared with BSL for research. In-depth analysis of the attack revealed that a part of the phish kit’s infrastructure, specifically a routing component built in to verify its victims and evade security controls, had glaring security flaws in its coding indicating that its development may have been assisted by AI.

Beazley Security Labs expects to see threat actors in 2026 continue to experiment with AI assisted tradecraft in efforts to accelerate reconnaissance, develop realistic deepfakes and social engineering campaigns, and enhance the speed and scale of early-stage intrusions, specifically targeting Web Applications. Although AI may lower the bar of entry for some threat actors, the technology is undisputably making cyber criminals faster - though not necessarily making them smarter. At this stage, organizations need to continue focusing on the defensive fundamentals that disrupt these attacks.

We demonstrate later in this report that stolen valid credentials, paired weak MFA configurations and unpatched internet facing systems, resulted in the majority of ransomware compromises Beazley Security investigated in 2025. Investments in deploying and enforcing phishing resistant MFA controls, monitoring and blocking risky sign-ins, applying well planned conditional access controls to enterprise resources, maintaining disciplined patch management, and relevant security awareness training that prepare employees for deepfakes will help arm organizations against a majority of these opportunistic attackers.

## Vulnerability Trends and Overview

In support of our Exposure Management platform and broader risk reduction mission, Beazley Security Labs (BSL) continuously monitors the threat landscape to identify critical vulnerabilities likely to create material impact. For these vulnerabilities, Beazley Security Labs publishes advisories to help organizations understand and mitigate those risks.

In Q4 2025, over 12,800 new vulnerabilities were publicly disclosed with about 2,200 of them considered high risk, meaning they could be exploited remotely with potential to cause harm if unpatched. This is an increase from nearly 1,800 in Q3.

Among these, 28 vulnerabilities were confirmed to be actively exploited in the wild, according to the U.S. Cybersecurity and Infrastructure Security Agency (CISA). These “Known Exploited Vulnerabilities” (KEVs) are especially important because they represent real world threats and impacts.

| Vulnerability Trends Q4 2025 | Change from Q3 |
| :--- | :--- |
| New CVEs published by NIST: 12,859 | +9.2% |
| CVEs added to CISA KEV: 28 | -3% |
| Critical 0-Day advisories published by BSL: 13 | +18% |

*\*Critical BSL advisories are made publicly available here.*

The fourth quarter saw increases in both newly published vulnerabilities, which were up nearly 10% over Q3, and vulnerabilities critical enough to issue an advisory from Beazley Security Labs (BSL), up almost 20%. Slightly fewer vulnerabilities were added to CISA’s KEV, down just 3%. That said, a decline in additions to KEV does not necessarily indicate reduced risk from edge device vulnerabilities, as the corresponding exploit campaigns from the Q4 vulnerabilities demonstrate.

BSL published 13 advisory responses in Q4, an 18% increase over the previous quarter. A concerning number of the advisories that BSL published were for vulnerabilities that were known to be under active exploitation at time of discovery, meaning threat actors were abusing those vulnerabilities before they were publicly disclosed.

### High-impact Breaches and Zero-day Vulnerabilities Exploited in the Wild

#### MySonicWall Cloud Backup Data Breach

In early October, threat actors gained access to firewall configuration backup files for all SonicWall customers that used their cloud backup service. This was a significant exposure, as the configuration files included encrypted credentials and sensitive configuration data for all affected users.

Remediation efforts were extensive, requiring substantial modifications to an organization's security and authentication settings on backed-up devices. Because the list of affected products was large, organizations had to check device configurations and update any secrets or credentials stored in the configuration. Additionally, these exposures can lead to downstream breaches that are difficult to identify and trace, as threat actors may simply log into compromised devices using stolen administrative credentials, VPN secrets, or other sensitive information.

#### F5 Source Code and Documentation Stolen by Nation State APT

In mid-October, F5 reported an incident where a highly sophisticated nation-state threat actor had gained access to their networks and leveraged the unauthorized access to exfiltrate system source code, internal documentation, and undisclosed vulnerability data for some F5 systems and products. The threat actors leveraged custom designed and stealthy implants to remain hidden in F5’s environment for an extended period of time.

The stolen vulnerability data was quickly assessed to be of low to moderate risk, mostly comprised of denial-of-service bugs. The more concerning aspect of this incident was that a nation-state threat actor obtained source code for networking devices that are used by “80% of the Fortune 500,” according to F5. The nation state that gained this access will undoubtedly study the stolen source code to find vulnerabilities and develop private exploits for future espionage operations.

#### Microsoft Windows Server Update Services (WSUS) Exploited In-The-Wild (CVE-2025-59287)

In late October, Microsoft issued an emergency out-of-band security update for a critical vulnerability in the Windows Server Update Services (WSUS) subsystem. The vulnerability had been disclosed only days earlier but the potential impact escalated rapidly after a security researcher released proof of concept exploit code. Within hours, financially motivated threat actors began actively exploiting the vulnerability in the wild, using it to deploy malicious implants and ransomware.

WSUS functions as a central control point for distributing Windows updates across enterprise environments. A successful compromise hands attackers a trusted delivery mechanism into every managed system. By weaponizing the update process itself, threat actors could rapidly propagate malware across an entire organization, turning routine patching infrastructure into a network wide infection vector.

#### React2Shell Vulnerabilities

In early December, several critical vulnerabilities affecting applications built on the widely used React and Next.js frameworks were disclosed, quickly escalating after public proof of concept exploit code became available. Within days, threat actors began mass scanning and testing affected environments across the internet.

The flaws could allow unauthenticated attackers to expose server-side application source code and sensitive data such as secrets, potentially enabling additional access to an organization’s infrastructure. Because React and Next.js are foundational technologies for a large portion of modern web applications, the impact was widespread. Vulnerabilities in frameworks at this scale provide attackers with highly efficient entry points, enabling rapid, internet-wide exploitation campaigns and reinforcing the growing focus on popular web software ecosystems as primary attack vectors.

Throughout 2025, particularly in Q4, Beazley Security Labs observed continued shortening of the “time to exploit” window, where the timeframe between public disclosure of a vulnerability and active exploitation gets ever smaller. Given how quickly exploitation now follows disclosure, sometimes before vendors can release a fix, organizations must move fast to identify and remediate critical vulnerabilities. Internet-facing systems exposed during a 0-day window should be investigated and treated as potentially compromised.

## Quarterly Ransomware Review

While reported ransomware incidents stabilized after an August peak, leak site post activity surged nearly 50%, with threat actors increasingly willing to escalate public pressure when negotiations stall. Extortion-related leak site posts increased steeply beginning in October and continued through the rest of Q4, likely driven by the emergence of new ransomware groups and evolving alliances, including ShinySp1d3r discussed above.

As outlined in our Q3 Threat Report, reported ransomware incidents surged in August, attributed to widespread Akira ransomware campaigns. This reporting spike settled into a more consistent pattern to close out the rest of 2025.

![Figure 5: Reported Ransomware Incidents]

At the same time, activity on extortion leak sites ramped up 48% through Q4, starting in October. Ransomware operators use leak sites to post victim data as part of their extortion process, increasing the pressure on victims to pay a ransom for decryption and deletion of stolen data. The increase appears to suggest that threat actors may have delayed public disclosure from Q3 while negotiations with victims were ongoing.

![Figure 6: Threat Actor Leaksite Posts]

Another observation accounting for Q4 increases includes a surge of activity from an opportunistic ransomware group calling themselves "Sinobi." The group gained visibility toward the end of 2025 with over 140 public posts on their leak site in Q4 alone, putting them third in post activity. Qilin operators again had the most public posts in Q4 (551 victims on their leak site), followed by Akira with 234 posts.

Industry reporting of ransomware incidents remained mostly consistent with last quarter, with modest increases in Health Care and Financial Institutions. While Business Services and Professional Services accounted for a slightly smaller share of total reported ransomware incidents in Q4, dropping from about 46% in Q3 to 39%, these sectors continued to see the highest overall volumes, reflecting ongoing appeal to ransomware operators due to the volume of sensitive client data available for ransom.

![Figure 7: Reported Ransomware Incidents by Sector]

In the next section we will examine some of the ransomware groups driving these trends and highlight observations from within Beazley Security’s incident response engagements.

### Emerging Ransomware Actors and TTPs

Beazley Security routinely engages victims of reported ransomware attacks through data forensics and incident response (DFIR) and restoration services. During these investigations, incident responders document the tactics, techniques, and behaviors used by ransomware groups to give a clearer picture as to how these actors shift operations over time. The following data trends patterns observed throughout the second half of 2025.

In Q4, many of the same groups that dominated activity in the previous quarter remained highly active. Akira and Qilin again represented the largest share of Beazley Security ransomware investigations, continuing to take advantage of opportunistic credential-based attacks and weak authentication policies on VPN appliances. These two ransomware operators alone represented nearly 65% of ransomware cases taken on by Beazley Security this quarter. Other ransomware operators such as Cl0p, Rhysida, and a growing number of independent “lone wolf” operators showed up in Beazley Security investigations throughout Q4. Notably, Osiris ransomware operators emerged as a new and capable ransomware family, with incident responders observing custom malware and tooling specifically designed to disable endpoint security controls.

![Figure 8: Threat Actor Distribution in Ransomware Investigations]

Against the backdrop of attacker attribution, incident responders also work to collect information on how these operators gain access into victim environments prior to ransomware deployment. In the next section, we’ve compiled the most common intrusion methods observed across the last half of 2025.

### How Ransomware Attackers Gained Access in Q4

Understanding how attackers gain an initial foothold into their victim’s environments can help protect against future ransomware attacks, and Beazley Security’s incident responders have worked to trend this information over the span of 2025. Q4 data shows that most ransomware intrusions began the same way they did throughout the rest of the year, with compromised credentials.

![Figure 9: Ransomware Initial Access By Category]

After gaining access, threat actors rapidly deployed ransomware in line with today’s “smash and grab” intrusion patterns, creating impact within a median dwell time of just one day this quarter. A limited number of outliers showed substantially longer delays between initial access and ransomware deployment, involving lesser-known ransomware operators and suggesting possible reliance on initial access brokers.

Throughout 2025, Beazley Security responders observed attackers repeatedly taking advantage of weak authentication controls on perimeter devices explored in our Edge Device Report. Internet-facing systems such as VPNs and remote access services were frequent targets, with some intrusions linked to satellite offices.

In these environments, inconsistent MFA enforcement policy and unpatched VPN gateways created opportunities for attackers, especially in cases where valid credentials were already obtained through phishing campaigns, infostealers, or other data breaches. The trend illustrates how important it is that organizations regularly audit and monitor remote access and the controls around associated accounts. The risk is especially elevated where MFA is not enforced due to legacy exceptions on service accounts, as these gaps are often targeted by attackers and may reduce level of effort to gain entry.

Q4 also saw external service exploits up 9% from Q3. These cases frequently involved attackers exploiting vulnerable internet-facing systems such as firewalls and other remote access solutions. Many of the external service exploits were due to ongoing, widespread exploitation of SonicWall weaknesses that we reported on in detail within our Q3 Threat Report.

Overall, attackers continued to rely on weaknesses in internet-facing infrastructure where gaps in patching, authentication, and slow vendor response to 0-day exploits served as reliable entry points for ransomware deployment. More complex supply chain and social engineering attacks, comparatively, were observed less frequently in the quarter.

## Quarterly BEC Review

Business email compromise (BEC) continues to be one of the most common forms of cyber incidents reported and investigated by Beazley Security, making up almost 35% of total reported cyber incidents in Q4. Unlike ransomware, which often causes immediate and visible operational impact, BEC attacks are by nature stealthy and use stolen credentials to manipulate inboxes, send fraudulent emails to trick additional internal users, and maintain persistence.

The graph below represents insights on reported BEC incidents by sector over the last half of 2025.

![Figure 10: BEC Incidents By Sector]

In Q4 2025, Professional Services accounted for the largest share of BEC incidents at 27%, significantly up from 19% in Q3. Business Service followed at 18%, also rising from the previous quarter. Mirroring ransomware groupings above, these two major sectors represent almost half of all reported BEC incidents in Q4. As the sectors are service-heavy, they’re positioned as high-value targets to threat actors. With large volumes of external email traffic containing financial communications and other sensitive information, they are ideal candidates to compromise in hopes of committing invoice fraud, trusted vendor impersonation, and other payroll routing attacks. Naturally, healthcare and financial institutions are also highly targeted owing to the sensitivity of data they handle, including third-party financial transactions. Each represented 11% of reported incidents in Q4, respectively, and may also constitute redeployment opportunity for BEC attacks aimed toward downstream Professional and Business services.

Many organizations have made strides to implement modern multifactor authentication (MFA) standards to help mitigate BEC. Unfortunately, attackers have started adapting their social engineering tradecraft to bypass these controls. Beazley Security’s DFIR investigations from the quarter reflect this adaptation, with email-based social engineering attacks remaining a persistent early-stage threat used to gain access to organizations.

In nearly 50% of successful BEC attacks Beazley Security responded to, impacted organizations had multi-factor authentication (MFA) enabled, with threat actors leveraging MFA bypass techniques such as adversary-in-the-middle phishing, session hijacking, and token replay. In these attacks, phishing “proxies” transparently relay authentication requests between the victim and the legitimate service, capturing session cookies or OAuth tokens in real time and allowing attackers to hijack authenticated sessions without ever needing the MFA factor again.

Additionally, 17% of successful attacks were attributed to MFA fatigue. This social engineering technique overwhelms victims with repeated push notifications in attempt to induce accidental approval, often after attackers first obtain valid credentials via phishing, infostealers, or initial access brokers. These campaigns are becoming more frequently paired with live helpdesk or Service Desk impersonation to increase pressure and success rates. Together, these trends highlight a new reality; traditional MFA alone is no longer sufficient. Organizations must begin planning a transition to phishing-resistant authentication such as passwordless passkeys or hardware-backed security keys (e.g., YubiKeys) which eliminate shared secrets and prevent token replay entirely.

As modern MFA attack vectors become increasingly known and executed by threat actors, business email compromise continues to be a high-impact threat to organizations. In addition to the phishing-resistant MFA methods described above, organizations should continue to invest in advanced identity protection controls, behavioral analytic monitoring, alongside relevant security awareness training for employees.

## Beazley Security MDR Trends and Overview

Beazley Security monitors threat actor activity and trending within MDR environments to understand how adversary tactics evolve quarter to quarter and where organizations are being targeted the most. Our MDR telemetry highlights which attack patterns are shifting in response to clients’ defensive measures over time, and which attacker techniques may be becoming more effective. This visibility helps provide context that can arm defenders with control prioritization and counter threats adversaries are beginning to leverage.

![Figure 11: MDR MITRE ATT&CK Distribution]

Compared with Q3, Q4 MDR data revealed a shift toward identity and cloud-focused attacks, with less success targeting endpoints through malware downloads. In Q3, our telemetry illustrated some effectiveness from attackers leveraging search engine optimization (SEO) poisoning paired with trojanized tools to trick users into installing infostealers and detonating other malicious payloads.

While malicious and trojanized software attacks were still prevalent throughout Q4, we saw the distribution of detections flatten back to initial access tactics such as social engineering and credential stuffing.

The MITRE ATT&CK distribution graphic to the right shows this trend, with Initial Access events rising to 30% of MDR detections, while Credential Access Attempts and other identity-based attacks grew to 23%, with the two categories together making up a substantial portion of detections at 53%. This trend showed that Beazley Security MDR prevented and contained more attacks at the front door of organizations in Q4, primarily driven by credential theft phishing and password spraying targeting enterprise resources.

We’ve rolled these findings into a distribution of attack phases from Q3 and Q4 of 2025 in the table below.

| Attack Phase | Q4 | Q3 | Descriptions |
| :--- | :--- | :--- | :--- |
| Early-stage Attacks | 65% | 44% | Credential access attempts, recon, and discovery activity detected and contained |
| Middle-stage Attacks | 27% | 44% | Attempts to sustain and expand adversarial control into environments contained |
| Late-stage Attacks | 8% | 12% | High-risk threats contained such as infostealer persistence, data exfiltration, and attempted ransomware deployment |

The simplified trending in this table illustrates that more attacks detected in Q4 were stopped at the beginning of intrusion attempts and that threat actors targeting Beazley Security MDR clients were less successful moving laterally within organizations.

Overall, our telemetry shows that in Q4, attackers remained persistent, with detection indicators shifting away from campaigns that deploy malware and infostealer kits directly targeting endpoints in favor of recon and credential access attempts.

## Sources

- [https://labs.beazley.security/advisories/BSL-A1136](https://labs.beazley.security/advisories/BSL-A1136)
- [https://labs.beazley.security/advisories/BSL-A1138](https://labs.beazley.security/advisories/BSL-A1138)
- [https://labs.beazley.security/advisories/BSL-A1140](https://labs.beazley.security/advisories/BSL-A1140)
- [https://labs.beazley.security/advisories/BSL-A1142](https://labs.beazley.security/advisories/BSL-A1142)
- [https://labs.beazley.security/advisories/BSL-A1146](https://labs.beazley.security/advisories/BSL-A1146)
- [https://landing.beazley.security/in-focus-edge-devices-2025-report](https://landing.beazley.security/in-focus-edge-devices-2025-report)
- [https://beazley.security/insights/quarterly-threat-report-third-quarter-2025](https://beazley.security/insights/quarterly-threat-report-third-quarter-2025)
- [https://www.europol.europa.eu/media-press/newsroom/news/end-of-game-for-cybercrime-infrastructure-1025-servers-taken-down](https://www.europol.europa.eu/media-press/newsroom/news/end-of-game-for-cybercrime-infrastructure-1025-servers-taken-down)
- [https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf](https://assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf)
- [https://techcommunity.microsoft.com/blog/microsoft-entra-blog/defend-your-users-from-mfa-fatigue-attacks/2365677](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/defend-your-users-from-mfa-fatigue-attacks/2365677)
- [https://www.bleepingcomputer.com/news/security/meet-shinysp1d3r-new-ransomware-as-a-service-created-by-shinyhunters/](https://www.bleepingcomputer.com/news/security/meet-shinysp1d3r-new-ransomware-as-a-service-created-by-shinyhunters/)
- [https://www.bleepingcomputer.com/news/security/shinyhunters-starts-leaking-data-stolen-in-salesforce-attacks/](https://www.bleepingcomputer.com/news/security/shinyhunters-starts-leaking-data-stolen-in-salesforce-attacks/)

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-26", "model": "gemini-3.5-flash-lite"} -->
