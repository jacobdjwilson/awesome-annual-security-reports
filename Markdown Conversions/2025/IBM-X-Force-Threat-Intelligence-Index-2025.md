# IBM X-Force 2025 Threat Intelligence Index

IBM Institute for Business Value  |  Research Insights

## Table of Contents
- [Foreword](#foreword)
- [Key takeaways](#key-takeaways)
- [Introduction](#introduction)
- [The intersection of AI and cybersecurity](#the-intersection-of-ai-and-cybersecurity)
- [Top initial access vectors](#top-initial-access-vectors)
- [Phishing as a shadow infection vector for valid account compromise](#phishing-as-a-shadow-infection-vector-for-valid-account-compromise)
- [Infostealers, a persistent and growing threat](#infostealers,-a-persistent-and-growing-threat)
- [Cloud-hosted phishing](#cloud-hosted-phishing)
- [PDFs and URLs taking over malware spam](#pdfs-and-urls-taking-over-malware-spam)
- [The success of vulnerability exploitation](#the-success-of-vulnerability-exploitation)
- [Vulnerabilities and the dark web](#vulnerabilities-and-the-dark-web)
- [Cybercrime marketplaces](#cybercrime-marketplaces)
- [Red Hat Enterprise Linux vulnerabilities](#red-hat-enterprise-linux-vulnerabilities)
- [Top actions on objectives](#top-actions-on-objectives)
- [The impact of takedowns on the malware landscape](#the-impact-of-takedowns-on-the-malware-landscape)
- [Proxy malware and obfuscation tactics](#proxy-malware-and-obfuscation-tactics)
- [Malware payloads delivered via SEO poisoning and malvertising](#malware-payloads-delivered-via-seo-poisoning-and-malvertising)
- [Top impacts on victim organizations](#top-impacts-on-victim-organizations)
- [Geographic trends](#geographic-trends)
- [Industry trends](#industry-trends)
- [Action guide](#action-guide)
- [Contributors](#contributors)
- [Notes & sources](#notes-&-sources)

---

## Foreword
The pattern is familiar. Organizations devote ever-growing resources to detect threats, protect networks, and deter disruption. And despite this, cyberattacks continue to grow in scale, speed, and sophistication.

But over the past 18-24 months, there has been a marked change in tactics. Threat actors are pursuing broader-scale campaigns—demonstrating a level of coordination, automation, and prowess not seen before—and raising the likelihood and impact associated with operational risks. Unlike incidents of the past, where data breaches and reputational harm were the greatest concern, widescale business disruption is now a real possibility—something every boardroom needs to be aware of and act upon.

A campaign conducted by Salt Typhoon, an advanced persistent threat (APT) group, exemplifies this troubling trend. In 2024, this threat actor group compromised virtually every major US telecommunications provider—in addition to targets in dozens of other countries—impacting supply chains, energy infrastructure, transportation, healthcare, and other critical services, including breaches of highly sensitive government systems.[^1]

As the Salt Typhoon attack demonstrates, threat actors are becoming more proficient at hiding illicit activity. They are massively increasing their use of compromised credentials to log in to networks, precluding any need to hack in. And doing so makes this activity much harder to detect and isolate. When threat actors use public cloud infrastructure, it becomes far more difficult for cyberdefenders to discern between safe and unsafe workloads.

The new litmus test is how well we can defend against resourceful threat actors conducting campaign-oriented, supply chain attacks. While we can use standard cyber risk practices to mitigate individual threats, what we are seeing is the emergence of a categorically different kind of risk—one that seeks to exploit our growing reliance on interconnectivity and common digital services.

To see things differently, we ourselves need to change. CISOs can play a decisive role in advocating change—starting with the C-suite and boardroom—but also raising awareness and accountability across the organization and in collaboration with ecosystem partners.

The growing coordination and complexity of attacks points to a need for a multifaceted and multilateral response. Awareness and accountability need to extend to every partner in our ecosystem—so we are standing together. Many sentries make a vital, more secure community. This isn’t such a radical notion. In fact, it’s exactly what cyber adversaries are doing by building crime-as-a-service communities and malware marketplaces on the dark web.

When executives understand that “what happens to my partners also happens to me,” they can take the necessary steps to support greater supply chain and ecosystem-level awareness and accountability. Coordination is critical to preventing intrusions, enabling rapid response, and mitigating the impact of attacks. Real-time threat intelligence, advanced multilayered defense platforms, zero trust network segmentation, and AI-powered monitoring are all essential components.

As stewards of trust, we are protecting not only our organizations and each other, but the integrity, values, and opportunities that bind us.

Since 1993, IBM has gathered, analyzed, and shared information and expertise about cyber attackers to help organizations navigate the evolving threat landscape. The IBM X-Force 2025 Threat Intelligence Index focuses on observations from our expert team of analysts, researchers, and hackers, tracking how threat actors get in, what they do when they’re in, and the impact caused by each breach. With these insights, we look forward to helping you stay one step ahead of cyberthreats, reinforce your organization’s operational resilience, and build strong, strategic partnerships that create cyber advantage now and into the future.

[^1]: Francis, Joel. “Briefing 29: Implications of the Ongoing Salt Typhoon Campaign on Telecommunications and Space.” Kratos. January 15, 2025. https://www.kratosdefense.com/constellations/articles/implications-of-the-ongoing-salt-typhoon-campaign-on-telecommunications-and-space

## Key takeaways
- **Manufacturing is the #1-targeted industry, four years in a row.**
  Manufacturing organizations continued to experience significant impacts from attacks, including extortion (29%) and data theft (24%), targeting financial assets and intellectual property. Defying the declining trend in malware, manufacturing had the highest number of ransomware cases in 2024 as attackers continue to exploit outdated legacy technology in this industry.
- **Number of infostealers delivered via phishing emails per week increases by 84%.**
  Year-over-year, X-Force is seeing a rise in infostealers delivered via phishing emails and credential phishing. Both result in active credentials that may be used in follow-on, identity-based attacks. Phishing has emerged as a shadow infection vector for valid account compromises. By clicking on links that seem legitimate, users can unknowingly open the door to infostealer malware that siphons sensitive data from victims. Because adversaries hide and deliver malware payloads more cleverly, it can take longer to detect than ransomware and data breaches.
- **Asia-Pacific region sees a 13% increase in attacks.**
  Asia-Pacific (APAC) experienced the largest share of incidents in 2024 (34%). This underscores APAC’s growing exposure to cyberthreats, likely due to its critical role in global supply chains and its position as a technology and manufacturing hub.
- **Threat actors add AI to their toolboxes.**
  Our analysts have documented that threat actors are using AI to build web sites and incorporate deepfakes in phishing attacks. We have also observed threat actors applying gen AI to create phishing emails and write malicious code.[^2]
- **Identity-based attacks make up 30% of total intrusions.**
  For the second year in a row attackers adopted more stealthy and persistent attack methods, with nearly one in three attacks that X-Force observed using valid accounts. A surge in phishing emails distributing infostealer malware and credential phishing fuels this trend, which may be attributed to attackers leveraging AI to scale attacks.
- **26% of attacks against critical infrastructure exploit public-facing applications.**
  One in four attacks exploited vulnerabilities in common public-facing or internet accessible applications. After gaining access, threat actors use active scanning techniques post-compromise to identify new vulnerabilities, gain additional access, and move laterally in compromised environments. Most importantly, attackers seek to escalate privileges to gain access to core services. The longer a threat remains undetected, the greater the risk. Long dwell times allow adversaries to mask their activity by “living off the land”—stealing data weeks or even months after an initial breach.[^3]
- **Ransomware makes up 28% of malware cases.**
  While ransomware made up the largest share of malware cases in 2024 at 28%, X-Force observed a decline in ransomware incidents overall. This is the third year that ransomware incidents have declined. This may be part of a larger decline in ransomware attacks due to businesses being more reluctant to pay ransoms and increased government actions against ransomware groups.
- **4 out of top 10 vulnerabilities most mentioned on the dark web are linked to sophisticated threat actors.**
  All top 10 vulnerabilities had publicly available exploit code or were being exploited in the wild, with 60% of these having a public exploit available from less than two weeks after disclosure -- including several zero day vulnerabilities. This raises the risks for businesses as sophisticated threat actors, including nation-state actors, leverage dark web anonymity to acquire new tools and resources.

[^2]: Mühr, Golo, and Joe Fasulo. “Hive0137 and AI-supplemented malware distribution.” Security Intelligence. July 26, 2024. https://www.ibm.com/think/x-force/hive0137-on-ai-journey
[^3]: “Combatting Cyber Threat Actors Perpetrating Living Off the Land Intrusions.” National Security Agency press release. February 7, 2024. https://www.nsa.gov/Press-Room/Press-Releases-Statements/Press-Release-View/Article/3669159/combatting-cyber-threat-actors-perpetrating-living-off-the-land-intrusions/

## Introduction
This year, we’ve seen shape-shifting cyber adversaries gain more access, move across networks more easily, and create new outposts in relative obscurity.

Equipped with advanced tools, threat actors are increasingly using compromised log-in credentials rather than brute-force hacking. The damage they inflict continues to grow as the global average cost of a data breach hit a record $4.88 million in 2024.[^4] What’s even more concerning is that data breaches are often only the start of larger and more coordinated campaigns. Threat actors openly trade exploits on the dark web to target critical infrastructure such as power grids, health networks, and industrial systems. Ransomware and infostealer operators exfiltrate millions of credentials from enterprises and extort victim organizations in multiple ways. And as businesses manage multiple cloud environments and accelerate AI adoption, attack surfaces expand and create new gaps in identity that attackers exploit to steal critical data.

Cybercriminals are increasingly adopting stealthy tactics and prioritizing data theft over encryption and exploiting identities at scale. A surge in phishing emails delivering infostealer malware and credential phishing are fueling this trend—and may be attributed to attackers leveraging AI to scale distribution.

Generative AI is emerging as a new and growing addition to the toolbox of nation-state-backed threat actors, cybercriminals, hacktivists, and others. These adversaries are avid adopters, especially as they launch social engineering campaigns and high-tempo information operations. AI and automated solutions can magnify the impact of infostealers, expedite the fabrication of credentials, and make it easier to amplify the speed and scale of intrusions at lower cost.

[^4]: “Cost of a data breach 2024.” IBM Security and Ponemon Institute. July 2024. https://www.ibm.com/reports/data-breach

## The intersection of AI and cybersecurity
2023 was the “breakout year” for generative AI (or gen AI). And what we expected began to take shape—threat actors are using AI to build web sites and incorporate deepfakes in phishing attacks. X-Force found threat actors applying gen AI to create phishing emails and write malicious code.[^5]

However, in terms of attackers building at-scale attacks targeting specific AI technologies, last year we predicted that once the technologies establish market dominance—when a single technology approaches 50% market share or when the market consolidates to three or fewer technologies—attackers will be incentivized to invest in attack toolkits targeting AI models and solutions.[^6] Are we there yet? Not quite, but adoption is growing. The percentage of companies integrating AI into at least one business function has dramatically increased to 72% in 2024, up 55% from the previous year.[^7]

New technologies, such as gen AI, create new attack surfaces. Security researchers are sprinting to find and help fix vulnerabilities before attackers do. We expect vulnerabilities in AI frameworks to become more common over time, such as the remote code execution vulnerability X-Force found in a framework for building AI agents.[^8] Recently, an active attack campaign targeting a widely used open source AI framework was discovered, affecting education, cryptocurrency, biopharma, and other sectors.[^9] Weaknesses in AI technology translate into vulnerabilities for attackers to exploit.

Another example of potential attack surfaces exposed in this new landscape is through machine learning operations (MLOps) platforms. These are used by enterprises of all sizes to develop, train, deploy, and monitor large language models (LLMs) and other foundation models (FMs), as well as the gen AI applications built on these models.[^10]

As adoption grows, attacks on AI infrastructure and tools will gain traction. Organizations should prepare now for threats by securing the AI pipeline from the start, including underlying training data, models, and the broader infrastructure surrounding the models. Yet, this doesn’t appear to be the current practice across many organizations, with only 24% of generative AI projects secured.[^11]

However, despite the evolving tools and different technologies attackers leverage—whether new gen AI tools or new AI infrastructure—the security fundamentals to thwart these attacks remain the same.

Our research shows threat actors are using valid credentials to log in; exploit unpatched vulnerabilities; and to a slightly lesser extent, phish their way in—with or without AI assistance. Organizations need to develop and run their own cybersecurity playbooks—seeking to identify exposures, assess risks, and mitigate incident impacts. But playbooks also need to account for who is responsible for specific actions, such as which party is accountable (and potentially liable) for securing a genAI solution offered by a third-party.

> “Cybercriminals are most often breaking in without breaking anything – capitalizing on identity and access management gaps proliferating from complex hybrid cloud environments. Compromised credentials offer attackers multiple potential entry points with effectively no risk.”
>
> Mark Hughes,
> Global Managing Partner for Cybersecurity Services, IBM

[^5]: Mühr, Golo, and Joe Fasulo. “Hive0137 and AI-supplemented malware distribution.” Security Intelligence. July 26, 2024. https://www.ibm.com/think/x-force/hive0137-on-ai-journey
[^6]: IBM X-Force Threat Intelligence Index 2024. IBM Security. February 2024. https://www.ibm.com/reports/threat-intelligence
[^7]: “Adoption of artificial intelligence among organizations worldwide from 2017 to 2024, by type.” Statista. May 2024. https://www.statista.com/statistics/1545783/ai-adoption-among-organizations-worldwide/
[^8]: Merrill, Josh. “Smoltalk: RCE in open source agents.” Security Intelligence. February 14, 2025. https://www.ibm.com/think/x-force/smoltalk-rce-in-open-source-agents
[^9]: Lumelsky, Avi, Guy Kaplan, and Gal Elbaz. “ShadowRay: First Known Attack Campaign Targeting AI Workloads Actively Exploited in the Wild.” Oligo. March 26, 2024. https://www.oligo.security/blog/shadowray-attack-ai-workloads-actively-exploited-in-the-wild
[^10]: Hawkins, Brett and Chris Thompson. “Disrupting the Model: Abusing MLOps Platforms to Compromise ML Models and Enterprise Data Lakes.” IBM X-Force Red. January 6, 2025. https://www.ibm.com/downloads/documents/us-en/11630e2cbc302316
[^11]: Rodgers, Clarke, Moumita Saha, Dimple Ahluwalia, Kevin Skapinetz, and Gerald Parham. Securing generative AI: What matters now. IBM Institute for Business Value. May 2024. https://ibm.co/securing-generative-ai

## Top initial access vectors
The top initial access vector observed in 2024 was a tie between exploitation of public facing applications and use of valid account credentials, both representing 30% of X-Force incidence response engagements.

The abuse of valid account credentials is an area we highlighted last year after observing a dramatic rise, continuing the theme of “hackers don’t break in, they log in.” This continues to be a problem and an initial access vector that adversaries are quick to exploit.

Threat actors obtain valid credentials to use during attacks via a range of methods. Data from our dark web analysis and incident response engagements continue to point to infostealer malware as being prevalent across industries. Additionally, credentials are still purchased and sold in large quantities on dark web marketplaces.

While multifactor identification (MFA) adoption has grown, we observed attackers selling adversary-in-the-middle (AITM) phishing kits and custom AITM attack services on the dark web to help bypass typical defensive measures. In 2024, X-Force specifically responded to cases involving this technique, globally and cross-industry. Widescale availability of credentials on the dark web, along with increased access to MFA codes and services to circumvent MFA, suggests a thriving access-as-a-service criminal market.

Phishing, whether through attachment or links, rounded out the top three compromises. The share of successful phishing compromises has declined steadily over the last several years from 46% in 2022 to 29% in 2023 to now just 25% of all incidents remediated by X-Force in 2024. Despite the development of some cybercriminals investing in AI to carry out phishing attacks, this method continues to be a less successful method for compromising environments than exploiting vulnerabilities or using valid credentials.

This is likely because enterprises continue to thwart phishing attempts—regardless of whether the phish used AI or not—by adopting and revaluating phishing mitigation techniques and strategies.

![Image description: Figure 1 Top methods used by threat actors to gain access to victim environments. The figure describes access methods according to the MITRE ATT&CK framework for enterprise, a globally accessible knowledge base of adversary tactics drawn from real-world observations. Percentages are based on number of X-Force incident response engagements. ]

FIGURE 1
Top methods used by threat actors to gain access to victim environments

The figure describes access methods according to the MITRE ATT&CK framework for enterprise, a globally accessible knowledge base of adversary tactics drawn from real-world observations.[^12] Percentages are based on number of X-Force incident response engagements.

[^12]: Initial access: the adversary is trying to get into your network.” Mitre Att&ck. July 19, 2019. https://attack.mitre.org/tactics/TA0001/

## Phishing as a shadow infection vector for valid account compromise
Compared to previous years, the volume of phishing emails distributing persistent backdoor malware has declined significantly. High-volume distributors of malware leading to ransomware attacks – including Emotet, TrickBot, IdedID, Qakbot, Gozi, and Pikabot – have largely dropped off the radar. Deploying persistent malware on an endpoint through an email is much more likely to be detected by endpoint detection and response (EDR) solutions, forcing threat actors to adapt strategies and focus on identities. This manifested in an increase in the use of infostealers and a shift towards credential phishing.

Infostealer bot frameworks enable attackers to design infostealer behaviors and create server-based management panels where infostealers send data. We observed a rise of 84% more infostealers delivered on average via phishing emails per week in 2024 versus 2023. Early data from 2025 suggests an even greater increase of 180% of weekly volume compared to 2023.

By using infostealers, threat actors can quickly exfiltrate credentials before detection without keeping a persistent backdoor as an initial foothold. The most common infostealer malware distributed directly via phishing was AgentTesla, followed by FormBook, SnakeKeylogger, and PureLogs Stealer.

We also observed an increase in Hive0145 email campaigns distributing the Strela Stealer infostealer. Hive0145 is an initial access broker focused on targeting victims throughout Europe with Strela Stealer malware. This infostealer has been in existence since at least 2022 and has always been purely focused on exfiltrating email credentials, leading to business email compromise. Since then, Hive0145 has experimented with several advanced techniques to improve campaign effectiveness.

Throughout 2024, we recorded a significant increase in volume, especially in the second half of the year. As of July 2024, this threat actor began using a new technique—dubbed attachment hijacking—to weaponize legitimate invoice-related emails which were previously stolen to further spread Strela Stealer.[^13]

![Image description: Figure 2 Top five infostealers seen on dark web forums. Analysis of dark web data reveals listings of infostealer advertisements increased 12% in 2024 over the previous year. The number one infostealer listing by a wide margin was Lumma, followed by RisePro, Vidar, Stealc and RedLine. Each listing can contain hundreds of credentials. Sources: IBM X-Force and Cybersixgill.]

FIGURE 2
Top five infostealers seen on dark web forums

Analysis of dark web data reveals listings of infostealer advertisements increased 12% in 2024 over the previous year. The number one infostealer listing by a wide margin was Lumma, followed by RisePro, Vidar, Stealc and RedLine. Each listing can contain hundreds of credentials. Sources: IBM X-Force and Cybersixgill.

[^13]: Mühr, Golo, Joe Fasulo, and Charlotte Hammond. “Strela Stealer: Today’s invoice is tomorrow’s phish.” Security Intelligence. November 12, 2024. https://securityintelligence.com/x-force/strela-stealer-todays-invoice-tomorrows-phish/

Additional infostealers analyzed in 2024 include well-established names such as Lumma, RisePro, Vidar, Stealc, Amadey, AgentTesla, AZORult, LokiBot, DanaBot, newer families such as Byakugan, FireStealer, ACR Stealer, DoomStealer, and WhiteSnake, and even MacOS targeted stealers such as MetaStealer and CloudChat.

The second change we observed in 2024 is an increase in credential phishing. Malicious URLs redirect victims to fake login sites for popular applications and harvest credentials.Both credential phishing and infostealer malware harvest active credentials for use in follow-on attacks.. For second-stage attacks, the vector is use of valid accounts, one of the most common initial access vectors during the last two years.

However, it is almost impossible to trace back to the origin of the compromised credentials. It is likely, that for many valid accounts incidents, the actual infection vector was a premeditated credential phishing or infostealer malware campaign, a fact that cannot be accurately reflected in the statistic of initial access vectors.

Although by the numbers it might seem like phishing risks are decreasing, it’s just become more challenging to determine where the risk originated. Valid credentials still must be sourced from somewhere. While it can be difficult to prove, most compromised credentials came from infostealers and credential harvesting campaigns, of which an increasing amount is delivered via phishing.

> Deploying persistent malware on an endpoint through an email is much more likely to be detected by EDR solutions, forcing threat actors to adapt strategies and focus on identities.

## Infostealers, a persistent and growing threat
Infostealers are malicious software programs designed to steal valuable information. Attack vectors typically include phishing emails, malicious websites, or infected software downloads.

Increasingly, infostealers are distributed through techniques such as SEO poisoning and Google Ads, drive-by attacks, and software supply chain compromises.

Once installed, infostealers run in the background to take screenshots, capture keystrokes, access passwords, and compromise financial and personal information without user knowledge. They have also been frequently linked to more impactful attacks against enterprises by allowing attackers to gain access through stolen login credentials. Infostealers have long been a staple of the criminal marketplace, and many operate as a malware-as-a-service (MaaS) model.

## Cloud-hosted phishing
In one of our most significant findings, our research reveals that over the past year, threat actors have shifted to using cloud hosting services to facilitate mass phishing campaigns. These campaigns have increased significantly in volume. The abuse of cloud hosting services often guarantees attackers a trusted URL, domain, and IP for use in their phishing campaigns—at least as long as the cloud hosting service fails to detect the abuse and act. For most providers, the sheer mass of abused accounts can be overwhelming. Adversaries require payloads to stay up only until victims click the link.

Latin America (LATAM) is one of the most severely impacted regions for phishing campaigns. Throughout 2024 threat actors have significantly ramped up the volume of LATAM-targeted campaigns abusing cloud hosting services.

These landscape changes make it much more difficult for defenders to prevent successful phishing attacks. Organizations cannot realistically block PDFs and URLs in emails because they are used everywhere across everyday operations. Furthermore, organizations cannot block legitimate cloud hosting services.

The only way to help avoid this is using time-sensitive threat intelligence tools to block URLs flagged as malicious and by relying on layered defenses to reduce impact if users take the phishing email bait. This means using endpoint detection and response (EDR) to detect info-stealing malware and using passkeys and MFA to reduce the risk of credential harvesting campaigns. The LATAM region is especially targeted and should remain vigilant against phishing campaigns. An effective way to counter the scale of these attacks is through the use of AI tools and automation.

**What is cloud-hosted malware?**

Attackers use malware hosting services to house and distribute malware and support browser exploits and drive-by downloads to infiltrate vulnerable computers.

Cloud-hosted malware attacks have proliferated because of increased reliance on cloud services, the inherent vulnerabilities of cloud estates, and the ease of distribution and persistence enabled by cloud infrastructure. Although cloud environments provide security features, they can be exploited when not properly configured, when vulnerabilities are not patched, or when policies are not updated.

Cloud-hosted malware refers to malicious software, including worms, trojans, ransomware, or infostealers that use cloud services for hosting, distribution and/or command and control operations.

![Image description: Figure 3 Incidence of spam and malware hosted on major public cloud environments. Number of observed spam email messages with links to a given cloud hosting provider. Threat actors seek to mask malicious activity by using popular cloud hosting services. The cloud hosting services secureserver.net (purple), publiccloud.com.br belonging to Locaweb Serviços de Internet (blue) and Microsoft Azure Blob Storage (white) have been abused heavily as a means to distribute credential phishing sites and banking trojan malware such as Grandoreiro, Mekotio and Guildma. NOTE: The use of a specific cloud provider for hosting malicious content is not indicative of a security flaw in the platform but illustrates where attackers choose to stage malware. Often, attackers choose well-known and established providers as a way to fool victims by hiding nefarious activities amongst other legitimate workloads, making those activities harder to identify and isolate. Source: IBM X-Force.]

FIGURE 3
Incidence of spam and malware hosted on major public cloud environments

Number of observed spam email messages with links to a given cloud hosting provider. Threat actors seek to mask malicious activity by using popular cloud hosting services. The cloud hosting services secureserver.net (purple), publiccloud.com.br belonging to Locaweb Serviços de Internet (blue) and Microsoft Azure Blob Storage (white) have been abused heavily as a means to distribute credential phishing sites and banking trojan malware such as Grandoreiro, Mekotio and Guildma. NOTE: The use of a specific cloud provider for hosting malicious content is not indicative of a security flaw in the platform but illustrates where attackers choose to stage malware. Often, attackers choose well-known and established providers as a way to fool victims by hiding nefarious activities amongst other legitimate workloads, making those activities harder to identify and isolate. Source: IBM X-Force.

## PDFs and URLs taking over malware spam
In 2024, we observed a clear decrease in direct malware attachments such as ZIP archives or maldocs in phishing emails. Malicious ZIP and RAR attachments dropped by 70% and 45% respectively, with a similar drop observed for Excel and Word documents.[^14] Malware is increasingly distributed via malicious URLs, both directly in phishing emails and through PDF attachments. This may be a result of better malware scanners in email solutions, which have become more accurate at detecting malware, but often cannot classify URLs or URLs inside benign attachments as malicious.

Obfuscation is becoming an important tactic for threat actors, and PDF malware disguises malicious URLs by encrypting them, hiding them in compressed streams or using hexadecimal representations which can also hinder automated analysis of email security solutions. Of all PDFs, 42% used obfuscated URLs, 28% hid their URLs in PDF streams, and 7% were delivered in an encrypted form along with a password.

Several threat actors were observed using PDFs to deliver malware through malicious URLs, including Hive0118 and Hive0137. These are ex-ITG23 affiliated distributors, which used PDFs with embedded links in several campaigns in the first half of 2024 to deliver malware and AITM links.[^15] These distributors have started experimenting with new attachment types such as PDFs with obfuscated URLs, documents with embedded URLs and others to load a wide arsenal of malware including Pikabot, DarkGate, NetSupport, T34-Loader and Warmcookie.

In 2024, PDF files were also commonly used in LATAM-targeted phishing campaigns to deliver links leading to banking trojan malware.

> Obfuscation is becoming an important tactic and PDF malware disguises malicious URLs by encrypting them, hiding them in compressed streams, or using hexadecimal representations to hinder automated analysis.

![Image description: Figure 4 PDFs rank as the top malicious attachment file type. PDFs are a common file format, with a complex structure that makes it easier for threat actors to hide malicious code. They are a popular choice for attackers to deliver malware via email and other means because many potential victims use PDFs frequently and may not be as suspicious of PDF attachments. Source: IBM X-Force.]

FIGURE 4
PDFs rank as the top malicious attachment file type

PDFs are a common file format, with a complex structure that makes it easier for threat actors to hide malicious code. They are a popular choice for attackers to deliver malware via email and other means because many potential victims use PDFs frequently and may not be as suspicious of PDF attachments. Source: IBM X-Force.

[^14]: Based on IBM X-Force telemetry. 2024.
[^15]: Mühr, Golo and Joe Fasulo. “Hive0137 and AI-supplemented malware distribution.” Security Intelligence. July 26, 2024. https://www.ibm.com/think/x-force/hive0137-on-ai-journey

## The success of vulnerability exploitation
30% of the incidents X-Force responded to in 2024 involved the exploitation of public-facing applications. For many organizations, this is magnified by vulnerability patch management challenges. Furthermore, in 25% of these cases, we observed active scanning post-compromise—meaning attackers used vulnerability scanning tools to identify additional vulnerabilities, gain additional access, and move laterally in the compromised environment.

Threat actors exploit known vulnerabilities in common applications and infrastructure services and the attack vector is simply a matter of acting on this knowledge. Bots and automation tools acquired on the dark web can target an organization’s key infrastructure applications and services.

Unfortunately for cyber defenders, there is no shortage of vulnerabilities to exploit. Since 1993, we have categorized over 300,000 unique vulnerabilities. Included are nearly 65,000 vulnerabilities with a publicly available exploit, many of which attackers have used to compromise environments. In other words, nearly a quarter of all vulnerabilities have an associated weaponized exploit that can be leveraged by threat actors.

Also, of note, the number of vulnerabilities has increased rapidly over the past eight years and grown threefold. This could be attributed to many factors. Perhaps the most likely is a growing reliance on shared cloud infrastructure and services. Attacking common cloud infrastructure is a prized opportunity for threat actors to deploy malware at scale and expand their potential for disruption. This is another compelling reason why zero trust principles, such as network segmentation, are essential for cyberdefenders. By isolating workloads, we limit the potential blast radius of attacks.

**What are common vulnerabilities and exposures (CVEs), weaponized exploits, and zero days?**

The CVE system provides a unique way to identify publicly known cybersecurity vulnerabilities and exposures occurring in software, hardware, and other digital systems.

It allows organizations to track security issues effectively and share knowledge, enabling security teams to refer to the same vulnerability in a consistent manner, even across different systems.

MITRE Corporation maintains a publicly listed catalog of CVEs, and the CVE list feeds the US National Vulnerability Database (NVD) which quickly enriches each CVE once it has been published.

In addition to pooling intelligence about common vulnerabilities and threat vectors, organizations also benefit from sector and industry-specific resources such as information sharing and analysis centers (ISACs). Typically managed by non-profit organizations, ISACs help critical infrastructure operators protect facilities, employees, and customers from cyber and physical security threats.

Weaponized exploits, often involving malicious payloads or malware, are attack tools used by threat actors to exploit vulnerabilities and target specific systems.

![Image description: Figure 5 Growth of vulnerabilities, exploits, and zero days. The growth of vulnerabilities, exploits and zero days since 2000. The IBM X-Force Vulnerability Database is one of the oldest and largest vulnerability databases in the world. Source: IBM X-Force.]

FIGURE 5
Growth of vulnerabilities, exploits, and zero days

The growth of vulnerabilities, exploits and zero days since 2000. The IBM X-Force Vulnerability Database is one of the oldest and largest vulnerability databases in the world. Source: IBM X-Force.

## Vulnerabilities and the dark web
In collaboration with Cybersixgill, X-Force has reviewed the 10 most mentioned common vulnerabilities and exposures (CVEs) on the dark web. These include mentions from numerous dark web marketplaces. According to our research, out of hundreds of vulnerabilities, the top three mentioned CVEs in 2024 were:

1. **CVE-2024-21762 (27%)**—Fortinet FortiOS could allow a remote attacker to execute arbitrary code on the system, caused by an out-of-bounds write flaw in a secure sockets layer virtual private network (SSNVPN). By sending specially crafted HTTP requests, an attacker could exploit this vulnerability to execute arbitrary code or commands on the system.
2. **CVE-2024-3400 (14%)**— Palo Alto Networks PAN-OS could allow a remote attacker to execute arbitrary command on the system, caused by a command injection vulnerability in the GlobalProtect feature. An attacker could exploit this vulnerability to inject and execute arbitrary code on the system with root privileges.
3. **CVE-2024-23113 (11%)**—Fortinet FortiOS could allow remote attackers to execute arbitrary code on systems, by using an externally controlled format string in the fgfmd daemon. By sending specially crafted requests, an attacker could exploit this vulnerability to execute arbitrary code or commands.

![Image description: Figure 6 Top 10 CVEs discussed on dark web forums. Shown as a percentage of the top 10 CVEs discussed on the dark web. Sources: IBM X-Force and Cybersixgill.]

FIGURE 6
Top 10 CVEs discussed on dark web forums

Shown as a percentage of the top 10 CVEs discussed on the dark web. Sources: IBM X-Force and Cybersixgill.

All top 10 vulnerabilities had publicly available exploit code or were found being actively exploited in the wild last year. 60% of these vulnerabilities had a public exploit available less than two weeks after disclosure— including several zero day vulnerabilities. Remote code execution is possible with eight of these vulnerabilities. The remaining two allow for an attacker to obtain sensitive information.

Apart from CVE-2024-9680, a remote code execution vulnerability affecting Mozilla Firefox, all top 10 CVEs were disclosed in the first half of 2024. And readers should understand that the disclosure date of a vulnerability plays a factor in terms of placement in the top 10, as earlier disclosure means more time for dark web discussions. The fact that