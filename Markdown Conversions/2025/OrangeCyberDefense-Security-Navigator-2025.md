```markdown
# Security Navigator 2025
Research-driven insights to build a safer digital society

© Orange Cyberdefense

In the world of cybersecurity, resilience is more than just a concept—it is a necessity. Over the past year, our teams at Orange Cyberdefense have observed an increasingly volatile and complex threat landscape, one that calls for both constant vigilance and innovative adaptation. The Security Navigator 2025 report presents a detailed examination of these challenges and, importantly, the proactive measures that can transform vulnerabilities into opportunities for stronger defense.

The data we have gathered over the past twelve months reveals stark shifts. Cyber extortion, hacktivism, AI-driven attacks, and threats to operational and mobile networks are not merely emerging trends; they are realities that are reshaping the cyber landscape. As malicious actors exploit new technologies and adopt increasingly aggressive tactics, the potential for harm extends beyond digital boundaries, impacting the very fabric of businesses and societies worldwide.

What makes this year’s Security Navigator unique is our expanded focus on the role of Artificial Intelligence in cybersecurity. From enhancing threat detection capabilities to mitigating complex vulnerabilities, we leverage AI to improve both offensive and defensive strategies. However, the rise of adversarial AI techniques—models specifically trained for malicious purposes—reminds us that innovation must be matched by responsibility. Our goal is not only to adopt the latest technologies but to do so thoughtfully, balancing progress with caution to secure a safer digital world. AI is not only a land of promises, and we need to remain careful on investing in and using these new technologies. It is all about balance and analyzing the hidden side of any wide-spreading technology; just like IT, shadow AI is now at stake.

This year, we also delve deeper into the threats facing critical infrastructure, particularly within Operational Technology and mobile networks. With increased connectivity and the adoption of IoT and 5G, these systems offer an expanded attack surface that calls for comprehensive, cross-functional defenses. At Orange Cyberdefense, we understand that building cyber resilience requires collaboration at every level—from industry alliances and partnerships to close work with our clients. This is also a matter of public-private cooperation. In 2025, regulation will make the European cybersecurity ecosystem go one step up and we are ready to support this movement.

Cybersecurity today is less about containment and more about anticipation. Informed by 135,225 analyzed incidents, a robust understanding of attacker behavior, and pioneering threat intelligence, our Security Navigator provides actionable insights to help our clients stay a step ahead. I am immensely proud of the dedicated work that went into this report, and I am confident that the insights it contains will empower you to face the challenges of an ever-evolving cyber threat landscape.

As we continue to confront these cyber threats together, let us remain focused on our mission: to build a safer digital society. Our commitment to this mission is stronger than ever, and we are honored to partner with you in securing a resilient digital future.

Hugues Foulon
Executive Director at Orange
and CEO Orange Cyberdefense

Foreword

Hugues Foulon
Executive Director at Orange and
CEO Orange Cyberdefense

> More than ever our 2025 edition of the Security Navigator will enable you to turn challenges into opportunities. The growing but ambiguous role of AI highlights the importance of creating an ecosystem of anticipation.”

www.orangecyberdefense.com

## Table of Contents
- [Summary: The Year 2024 in a Nutshell](#summary-the-year-2024-in-a-nutshell)
- [Basic Data Analysis: Key Data of the Year](#basic-data-analysis-key-data-of-the-year)
- [Threat Detection](#threat-detection)
- [Incidents per Month per Client](#incidents-per-month-per-client)
- [Threat Actions, Sources, Targets and False Positives](#threat-actions-sources-targets-and-false-positives)
- [Incidents by Business Size](#incidents-by-business-size)
- [Mean Time to Resolve](#mean-time-to-resolve)
- [Vulnerability Scanning](#vulnerability-scanning)
- [Severity of Findings](#severity-of-findings)
- [Criticality of Findings by Operating System](#criticality-of-findings-by-operating-system)
- [Cyber Extortion](#cyber-extortion)
- [Threat Actors](#threat-actors)
- [Regional Shift](#regional-shift)
- [World Watch](#world-watch)
- [Paris Olympics](#paris-olympics)
- [Long-Running Conflicts](#long-running-conflicts)
- [Industries](#industries)
- [Industry Comparisons](#industry-comparisons)
- [Scorecard: Retail and Trade](#scorecard-retail-and-trade)
- [Scorecard: Construction](#scorecard-construction)
- [Scorecard: Manufacturing](#scorecard-manufacturing)
- [Scorecard: Professional, Scientific and Technical Services](#scorecard-professional-scientific-and-technical-services)
- [Scorecard: Health Care and Social Assistance](#scorecard-health-care-and-social-assistance)
- [Scorecard: Educational Services](#scorecard-educational-services)
- [Scorecard: Finance and Insurance](#scorecard-finance-and-insurance)
- [Scorecard: Public Administration](#scorecard-public-administration)
- [Regions](#regions)
- [Region Perspective](#region-perspective)
- [Europe Region](#europe-region)
- [Nordics Region](#nordics-region)
- [Africa & Middle East](#africa--middle-east)
- [APAC Region](#apac-region)
- [North America Region (US & CA)](#north-america-region-us--ca)
- [Research](#research)
- [Artificial Intelligence – What's All the Fuss?](#artificial-intelligence--whats-all-the-fuss)
- [Expert Insight: Tricking the AI – How to Outsmart LLMs](#expert-insight-tricking-the-ai--how-to-outsmart-llms)
- [Expert Insight: Enhancing Beacon Detection](#expert-insight-enhancing-beacon-detection)
- [Beyond Vulnerability Management](#beyond-vulnerability-management)
- [Expert Insight: Vulnerability-Prone Network](#expert-insight-vulnerability-prone-network)
- [Trends, Targeting, and Testing of Operational Technology: Ransomware Ripples & Real Risks](#trends-targeting-and-testing-of-operational-technology-ransomware-ripples--real-risks)
- [Exploring the Intersection of Cyber Activism and State-sponsored Operations](#exploring-the-intersection-of-cyber-activism-and-state-sponsored-operations)
- [Expert Insight: Human-Driven Threat Hunting](#expert-insight-human-driven-threat-hunting)
- [Mobile Security – Carriers, Networks and Security](#mobile-security--carriers-networks-and-security)
- [Expert Insight: A Hierarchy of Needs – Incident Response Readiness](#expert-insight-a-hierarchy-of-needs--incident-response-readiness)
- [Security predictions: A story of convergence, intelligence and resilience](#security-predictions-a-story-of-convergence-intelligence-and-resilience)
- [APTs Will Not Leave Room for Ransomware](#apts-will-not-leave-room-for-ransomware)
- [Generative AI Boosts Automation](#generative-ai-boosts-automation)
- [Regulations: Ensuring Security Success](#regulations-ensuring-security-success)
- [Resilience 2.0](#resilience-20)
- [Security ROI in Focus](#security-roi-in-focus)
- [Summary: What Have We Learned?](#summary-what-have-we-learned)
- [Appendix](#appendix)
- [Glossary](#glossary)
- [Contributors, Sources & Links](#contributors-sources--links)

---

← You can always return to this page by clicking here!

## Introduction
### Summary: The Year 2024 in a Nutshell
#### Cynical Security
I was so relieved when experts confirmed that the widely reported exploding-pager against Hezbollah did not involve a significant cyber component. The attacks in Lebanon and Syria involved modified radio pagers and other electronic devices that exploded, resulting in dozens of deaths and hundreds of injuries[^1]. Israeli intelligence is suspected to be behind the incidents[^2]. The modifications for the attacks were reportedly achieved by altering the devices at the production level to include small amounts of explosives. This allowed the attackers to distribute the modified pagers and other electronic devices widely before triggering them remotely.

When news of the incident began to emerge, people like me in cybersecurity all instinctively wondered if it had involved some kind of cyber-attack. It seemed highly unlikely, but many of us have become so cynical. And with good reason.

Cybersecurity failures – albeit not in a form suited to a Grisham novel – are indeed threatening lives. The cyber extortion attack against the South African National Health Laboratory Service (NHLS) in June this year impacted the service’s ability to generate lab reports and send them to clinicians. The disruption lasted several weeks, resulting in reports about clinics coming to a standstill, and patients in emergency wards and intensive care units in fatal danger[^3]. In an unusual twist , someone who described himself as “the middleman” called the press in South Africa to warn that related patient deaths would be “on the NHLS for not engaging”.

Introduction: This is what happened
Charl van der Walt
Head of Security Research
Orange Cyberdefense

[^1]: https://www.bbc.com/news/articles/cz04m913m49o
[^2]: https://www.reuters.com/world/middle-east/israel-planted-explosives-hezbollahs-taiwan-made-pagers-say-sources-2024-09-18/
[^3]: https://therecord.media/south-africa-national-health-laboratory-service-ransomware-recovery

www.orangecyberdefense.com

#### Extortionate Security
As cyber extortion continues to increase globally, we note this year that it is also becoming increasingly cynical. This year Diana Selck-Paulsson examines over 13,000 cyber extortion incidents, and reports how extortion tactics are demonstrating increased aggression and moral decline, abandoning previous restraints on targeting sensitive sectors like healthcare. Once considered off-limits, hospitals and essential care facilities now face a surge in attacks. Small and medium-sized businesses are also becoming more frequent targets, accounting for over two thirds of all victims. Small businesses saw a 53% increase in cyber extortion attacks, while medium-sized businesses experienced a 52% rise. Vulnerable, smaller countries are not immune either. This year for the first time we report Cy-X victims in countries like Afghanistan, Djibouti, Tokelau, Nepal, Uzbekistan and Maldives. Attackers are also exploiting cynical “revictimization” strategies, where stolen data is reused across multiple extortion platforms and amplifying the psychological burden on victims.

#### Subversive Security
This year we also explore shifts in hacktivism, which is becoming increasingly cynical and aggressive. Once grounded in activism, hacktivism now bears a closer resemblance to cyber extortion, with a focus on destabilizing communities and weaponizing fear against both individuals and institutions.

Diana also continues her excellent work on this phenomenon, examining over 6,500 hacktivist incidents to reveal how the emerging hacktivist model focuses on public manipulation, societal division, and the erosion of trust. Hacktivists are aligning with state-sponsored agendas, targeting critical infrastructure like election systems - seeking not only to disrupt essential services but also to undermine public confidence in government and democratic institutions. By attacking election-related systems and other symbolic institutions, the hacktivist groups aim to undermine public trust, disrupt the flow of information, and potentially influence the outcome of a key democratic process. By leveraging sophisticated DDoS-for-hire services and anonymous cryptocurrency incentives, hacktivists are blending public shaming with extortion techniques to exploit fear and amplify public pressure. While Europe is the primary focus for the group Diana studied, everyone is a potential target, and the problem threatens societies as a whole.

#### Cyber Physical Security
Hacktivists are a significant threat to cyber-physical environments like factories, plants and utilities. In fact, our research attributes 23% of targeted attacks against operational technology environments to hacktivist actors.

Ric Derbyshire is a specialist in operational technology (OT) and industrial control systems. He’s expanded his OT security dataset to cover 119 recorded cyber-attacks over a period of 35 years. This year his unique dataset expanded with 47 incidents from the last 12 months.

This year’s insights again underscore the prevalence and impact of cyber extortion (Cy-X) on OT systems. Attacks originating in IT environments frequently cascade into OT systems, disrupting essential operations and causing downtime. Despite rarely being the primary targets, OT environments face unintended consequences due to interconnected IT and OT networks. Correspondingly, the manufacturing sector accounts for 20% of all cyber extortion victims this year and has seen a 25% increase from the previous year.

81% of this year’s documented attacks were perpetrated by criminals and primarily impacted IT systems, not OT. But, as we posited last year, threat actors will start to focus on OT systems directly when the environmental factors align.

An attack impacting Spanish bioenergy plant Matadero de Gijón in April this year is an early indicator that this may be happening already. The attack is recorded in Diana’s dataset (Cy-X) and in Ric’s dataset (OT) but stands out because it directly impacted the plant’s Supervisory Control and Data Acquisition (SCADA) system.

In this year’s report, Ric focuses on “category 2” incidents in OT - those directly targeting OT systems through adversarial tactics unique to these environments- a category that only accounts for 16% of recorded incidents. These category 2 attacks are more intentional and sophisticated, often involving advanced tactics by state-sponsored groups and sophisticated cybercriminals, who aim to directly compromise OT operations. Ric points out that 46% of category 2 attacks resulted in “manipulation of control” as an impact. This means that the adversary manipulated the physical process in their attack. This is clearly a frightening outcome, and most category 2 attacks have equally severe impacts.

Category 2 incidents, while relatively infrequent, force our risk models to consider the unthinkable. This pressure places enormous additional responsibility on those responsible for protecting cyber-physical systems.

Ric argues that category 2 OT attacks tend to exploit native functionality within the victim’s environment—a technique known as living off the land. As with IT-attacks, this approach allows adversaries to blend in and evade detection, but it places the adversary in the optimal position to cause real damage in an environment. For example, exploiting a programmable logic controller (PLC) by using expected functions is safer and more stable for attackers than risking a memory abuse vulnerability, but also allows attackers to abuse the ability of that PLC to manipulate the physical environment. This reality has significant implications for how we approach security in OT environments.

For example, simply accessing an OT environment doesn’t mean that an attacker can achieve a desired cyber-physical impact. This raises an essential question: how can asset owners assess their OT environment’s resilience against category 2 threats?

Ric explores significant challenges and gaps in current OT security, and specifically penetration testing approaches. The discipline is still in its infancy, with limited research and ambiguous guidance that fails to fully account for unique OT tactics, techniques, and procedures (TTPs), especially those seen in category 2 attacks. Ric critiques the reliance on IT-oriented penetration testing practices, which often focus on gaining OT access and declaring success, overlooking the complexities of truly emulating OT-focused adversaries. He questions whether current testing approaches effectively capture the nuanced tactics used in real OT attacks, such as those exploiting native functionality for stealth and control.

Our report this year highlights the need for security approaches that anticipate complex OT-specific kill chains and TTPs to more accurately ensure resilience against genuine threats. As with so many things that need to be rethought in contemporary cybersecurity, we argue this year the traditional IT frameworks are not appropriate for addressing OT’s particular threats and vulnerabilities.

#### Mobile Security
In a new section of this year’s report, Orange mobile network security specialists Emmanuelle Bernard, Stéphane Gorse, and Sébastien Roché outline the evolution of mobile network vulnerabilities, describing how each generation of mobile technology (2G through 5G) has introduced advanced features alongside an expanded attack surface. While early networks primarily faced issues from weak 2G encryption, newer generations brought complex protocols like SS7 in 3G and Diameter in 4G, which attackers now exploit. With 5G, increased virtualization, APIs, and IoT integration have introduced new risks, including supply chain attacks and vulnerabilities accessible remotely through Internet-connected devices.

Our report identifies three primary attack domains: SIM cards, devices, and infrastructure. SIM-based attacks use techniques like SIM swapping, cloning, and USSD protocol misuse to intercept data or impersonate users.

Device-based threats center around malware and mobile OS exploitation, especially through alternative app stores that lack strict security. Infrastructure attacks target network protocols and exploit carrier interoperability to intercept communications . We note that MFA use on mobile devices has also complicated the risk by giving threat actors motive and opportunity to compromise network-linked authentication methods.

Our report emphasizes a layered security approach that includes enhanced standardization and collaboration among network operators, device manufacturers, and regulatory bodies. But given the cross-functional nature of mobile networks today, enterprises are also being forced to consider comprehensive security responses that range from securing devices and infrastructure to raising user awareness about safe practices.

#### Struggling Security
While our adversaries are becoming more cynical, and the impact of security failures more profound, we as the defenders are still struggling to stem the flood.

This year veteran security researchers Wicus Ross and Rogan Dawes study 1.3 million vulnerabilities across 69,000 customer assets to surface a critical message: We need to change the way we think about security vulnerabilities.

Wicus’ work focuses on how businesses tackle vulnerabilities. He illustrates that vulnerabilities are emerging at such a pace that traditional, reactive measures simply aren’t keeping up. As Wicus shows, for example, vulnerability management teams face an increasingly daunting task as they contend with the overwhelming volume and velocity of new vulnerabilities. With endless new vulnerabilities emerging continuously, we are forced into a reactive mode, obliged to prioritize and address threats without control over the cadence or velocity of intelligence. Organizations with already-limited capacity are left to scramble from the back foot, unable to make sense of an ever-evolving threat landscape.

The complexity of large enterprise environments adds to these challenges, as even high-probability vulnerabilities identified by metrics like EPSS are difficult to mitigate at scale. In this report we argue that covering all potential exploits across vast networks is fundamentally impractical, meaning that crucial decisions must be made about which systems to patch first. But we argue that the “risk-focused” approach isn’t effective either. Wicus’ study of EPSS and statistical probabilities argues that even low-severity issues at sufficient scale leave the business vulnerable to compromise. The problem calls for a fresh approach, and in this year’s report we argue that must start with a clarification of fundamental terms.

“Vulnerability Management” needs to go. Wicus proposes that new approaches with new descriptions are urgently needed.

#### Security From the Source
Wicus and Rogan both also put the responsibility on software vendors to prioritize security in software development, and throughout a products lifecycle.

As I write this, our CERT, Vulnerability Management, Threat Detection and Managed Services teams are wrestling to contain the threat and impact of “FortiJump[^4]” – a severity 9.8 vulnerability in Fortinet FortiManager.

In mid-October, Fortinet alerted key partners and select clients, including Orange Cyberdefense, to a critical 0-day vulnerability actively exploited in FortiManager, a product essential for managing security tools like FortiGate firewalls. The vulnerability allows remote attackers to execute commands on vulnerable devices by exploiting a missing authentication check in the FortiManager-to-FortiGate protocol. Fortinet has since released patches, which we and others are of course rushing to deploy. Meanwhile the bug has been actively exploited – apparently by Chinese APT actors - for some time already. Reconnaissance likely began as early as July this year, with widespread exploitation following in September. Fortinet and others are sharing specific indicators that defenders are scouring their systems for.

It feels like a fitting soundtrack for this report.

Despite this urgency, many products — including those explicitly designed for cybersecurity — continue to exhibit fundamental flaws that leave clients exposed. This gap is more than technical; as we detail in this report, there’s a clear and urgent need for secure-by-design principles to become an industry standard, addressing vulnerabilities at the source instead of relying on patches and workarounds after release.

Rogan’s work highlights the significant number of troubling examples of security products — firewalls, endpoint protection, intrusion prevention systems — shipping with exploitable weaknesses. These vulnerabilities are often in products that sit directly exposed to the internet, where their primary function is to facilitate secure authenticated access to sensitive areas inside an organization. Every new vulnerability uncovered in these trusted tools not only threatens the systems they protect, but also erodes confidence in the very solutions meant to safeguard our digital infrastructure.

Wicus’ study of almost 500 security advisories released by our World Watch team this year illustrates just how pervasive this problem has become. Last year security vendor Ivanti was truly in the crosshairs, but vendors in general are letting us down,

- 11 Jan 2024 – Two new 0-day vulnerabilities actively exploited against Ivanti Connect Secure VPN. This saw the start of several weeks of updates by Ivanti to release fixes for all their impacted products.
- 7 Feb 2024 – Dutch Military Intelligence and Security Service (MIVD) disclosed that Chinese state-sponsored threat actors infiltrated the Ministry of Defense of the Netherlands in 2023. Attackers were exploiting an old vulnerability in FortiOS SSL-VPN affecting FortiGate devices. In June 2024 – the MoD announced that a Chinese threat actor had compromised up to 20,000 FortiGate instances linked to the original announcement.
- 9 Feb 2024 – Fortinet fixed two critical vulnerabilities in FortiOS SSL-VPN, of which one was exploited in the wild prior to the fix.
- 18 Mar 2024 – Proof of Concept emerged for critical vulnerability in FortiOS SSL-VPN module. At the time ShadowServer identified nearly 130,000 vulnerable instances and noted exploitation attempts.
- 14 Apr 2024 – Critical vulnerability in GlobalProtect firewall from Palo Alto Networks linked to targeted 0-day exploitation. This was the only Critical (5/5) advisory from World Watch during this report period.
- 29 May 2024 – Check Point disclosed an exploited 0-day vulnerability in its remote access VPN solution. Attackers had already been attempting to exploit the vulnerability a month earlier.
- 19 Jul 2024 – CrowdStrike's Falcon Sensor update crashed Windows machines all over the world. The outage was linked to an update that had a malformed channel file.

As an industry, Rogan argues, we should be solving these problems, not creating them. As we have since 2022, we call on our partners and competitors in the security industry to come together to work on this challenge.

#### Struggling to Respond
In the face of this barrage of threats, Wicus Ross’ analysis of our threat detection data highlights the several challenges in detecting and responding to security incidents. One key observation is the increased misuse of systems by employees. Such “insider” activity makes distinguishing between benign and malicious activities even more difficult, particularly as attackers increasingly use "Living off the Land" (LOL) methods that resemble normal user behavior. As detection teams are finding it difficult to distinguish between benign user actions and actual threats, Wicus’ report suggests that fostering "pervasive cyber judgment" across the organization is essential.

The need to respond to LOL and other “insider threats” forces detection teams to collect and analyze yet more, subtle indicators. This additional load makes separating real signals from the noise even more challenging. Our report shows that confirmed incidents, or "True Positives," comprised only 14.98% of the incidents we analyzed. The remaining incidents were classified as: 12.36% "True Legitimates" (genuine activity that posed no threat), and 61.74% "False Positives" (mistaken detections). 10.92% remained uncategorized.

The impact of this load and complexity has a measurable impact on our collective ability to detect and respond to potential incidents. This year for the first time we present insight in our Mean Time to Resolve (MTTR) statistics. This metric is complex due to varied incident types and the necessity for client coordination, but analysis reveals that while many incidents are resolved quickly, the loop on priority incidents can take over a day to close.

We remind readers of our 2024 research piece titled “Fake News and False Positives”, where we pointed out that over time there are detection efficiency gains as the relationship between our detection teams and our client teams grows and matures.

[^4]: https://www.techtarget.com/searchSecurity/news/366614476/Fortinet-discloses-critical-zero-day-flaw-in-FortiManager

Improved feedback loops are essential in refining detection systems and improving confirmed incident rates.

In light of these challenges, Senior CSIRT Analyst Simone Kraus examines the critical role of human analysts in threat hunting, stressing the unique value that human insights bring to the detection of sophisticated threats. While automated detection tools are useful, they cannot fully replace the intuition and adaptability of skilled security analysts who can recognize nuanced attack patterns and respond effectively. Simone introduces the concept of “threat-informed defense,” where understanding an organization’s specific threat landscape helps tailor defense strategies. This approach integrates knowledge from actual incidents and threat intelligence, allowing defenders to anticipate likely attack vectors and prioritize resources accordingly.

We also examine common organizational challenges in Incident Response in a study by Saskia Kuschke, a Senior CSIRT Investigator. Saskia’s work notes that many companies struggle with foundational elements like asset mapping. But incident readiness can also be stymied by unclear roles, lack of communication, and low user awareness, all of which contribute to slower responses and higher risks during actual incidents. Saskia proposes a structured approach to building incident response readiness. She emphasizes a hierarchy of needs, starting with essential tasks such as role assignment and incident communication protocols. Her proposed model progresses through asset mapping, visibility enhancements, and eventually, complex detection and response capabilities. This tiered approach allows organizations to scale their security efforts methodically.

#### Artificial Intelligence
Like almost every research team in security, this year we consider the impact of LLMs and GenAI on the security landscape. Large Language Models - born out of advancements in natural language processing and machine learning - have transformed from rudimentary text-processing tools to sophisticated systems capable of generating human-like responses.

Anis Trabelsi is a team lead on Data and AI. This year he discusses how AI can help address the challenge of detecting beaconing—subtle, periodic communications that malware uses to connect with command-and-control servers—by leveraging AI to enhance detection capabilities. These beaconing signals often blend in with legitimate traffic, making them difficult to spot with traditional methods. Anis describes an AI-driven approach his team developed, centered on analyzing proxy logs to capture network activity in real time. By identifying repetitive requests or unusual traffic patterns, the system generates rapid alerts, enabling faster defensive actions. This research shows how AI can strengthen detection accuracy and scalability, significantly narrowing the window for attackers to exploit these covert channels.

The impact of LLMs on security defense is clearly exciting, but we make the argument this year that new technologies often favor the offensive side, so technologies like GenAI are likely to benefit attackers more than defenders.

Summary: this is what happened

Introduction: This is what happened

While these tools may enable more effective response by businesses, the same capabilities can be weaponized by malicious actors, allowing them to conduct more sophisticated attacks with greater ease. If AI is generally thought of as a productivity tool, then we can expect it to make attackers more productive also. Despite these risks, our research suggests that existing security practices are often sufficient for mitigating many of the threats associated with GenAI, although consistency is crucial.

Rather than focusing on GenAIs power for attacker or defenders, however, our report this year is primarily concerned with the broader risks that emerge when businesses and individuals adopt LLM and GenAI technologies. With continuous reports about how threat actors may (ab)use LLMs, the less colorful risk introduced in the application of the very young LLM technology as an interface by businesses is being underestimated, especially where these systems serve as a bridge between the open internet and critical business assets.

Untested, opaque AI interfaces deployed as an interface pose a significant risk to the internal systems they interface with. We cite the recent example of a breach at an NSFW AI chatbot service. Here, a hacker exploited vulnerabilities in the platform, which they described as “a handful of open-source projects duct-taped together.” This complex, poorly engineered system allowed easy access to the platform’s backend systems and data. We expect to be reporting on many more incidents like this over the next year and urge readers to be extremely cautious about how and where they deploy AI on top of their own backend systems.

Research by pentester Geoffrey Sauvageot Berland’s in this report examines the specific risk of prompt injection - manipulated inputs that can mislead or disrupt GenAI behavior. By exploiting the predictive nature of LLMs, attackers can bypass ethical and security controls, causing the model to generate unintended outputs. Techniques include “context switching,” which introduces abrupt topic shifts to elicit unauthorized responses, and obfuscation, where forbidden terms are disguised through encoding to evade content filters. Geoffrey also warns of denial-of-service attacks that overload models with complex tasks, as well as the risks posed by multimodal applications where malicious commands can be hidden in images or audio, expanding the AI attack surface.

In the face of enormous pressure to integrate LLMs into business operations, we argue for a cautious, guarded approach that begins with a clear definition of the use-cases and desired outcomes an AI is expected to deliver, so that risks can be assessed and objectively weighed against potential benefits. We need to heed lessons from previous technology revolutions, perform rigorous security testing and thoughtful deployment of LLMs to ensure the necessary balance between security, safety and any productivity and the promised operational benefits GenAI may deliver.

#### What Are We defending?
A recurring theme in this year’s report is a critical shift as attackers increasingly target perception and trust through cognitive attacks. These attacks, which go beyond traditional technical disruptions, are aimed at manipulating public opinion, undermining trust in institutions, and destabilizing societal confidence. One example involves pro-Russian hacktivist groups, who align their campaigns with major geopolitical events such as elections and summits to amplify their impact. By targeting symbolic infrastructure and leveraging public platforms like Telegram, these groups blur the line between cybercrime and influence operations. Their ultimate objective isn’t solely system disruption, but rather the erosion of trust in democratic systems and processes.

In a similar vein, cyber extortion actors employ psychological tactics to manipulate perceptions. Following a major law enforcement crackdown under Europol’s Operation Cronos, which significantly limited their operational capabilities, the Cy-X group LockBit countered by inflating their victim numbers and projecting an image of resilience and strength. This tactic aimed to maintain confidence among affiliates and instill fear in potential targets. Along with our findings on the cyber extortion phenomenon of “revictimization”, these examples exemplify how cyber extortion tactics are increasingly perception-focused, using narrative control to affect both victims’ and the criminal ecosystem’s responses.

It's into this context that Artificial intelligence (AI) is emerging as a powerful tool for attackers in cognitive operations, adding a new dimension to misinformation campaigns. State-sponsored actors from countries such as China, Russia, and Iran leverage generative AI to create realistic phishing content, fake images, and deepfakes that can deceive large audiences[^5][^6]. These AI-supported attacks aim to influence public perception on a mass scale, from disrupting elections to discrediting political candidates, eroding trust in democratic institutions. The integration of AI into existing campaigns increases the role of cognitive attacks in the threat landscape, providing actors with scalable tools to craft highly convincing, tailored narratives to suit their needs.

These shifts represent a significant new challenge for security defenders. In addition to “simply” countering technical threats, we must now broaden our approach to incorporate strategies to counter cognitive and perception-based threats and psychology-driven attacks, which target minds as much as systems.

Security is not an objective state, it’s the subjective expression of our freedom to pursue shared visions and construct a society that is equitable and rewarding. Cognitive attacks leverage technical compromises, not as an end in themselves, but as a means of launching an assault on the fabric of trust on which “secure” systems are built. Cognitive attacks require us to not only counter technical intrusions, but also safeguard the public perception of trust we need for our digital and interconnected world to flourish.

[^5]: https://blogs.microsoft.com/on-the-issues/2024/07/30/protecting-the-public-from-abusive-ai-generated-content/
[^6]: https://www.dhs.gov/sites/default/files/2023-09/23_0913_ia_23-333-ia_u_homeland-threat-assessment-2024_508C_V6_13Sep23.pdf, page 14

---

## Intelligence and Operations Data
### Basic Data Analysis: Key data of the year
#### From Reactive to Proactive: Continuous Threat Exposure Management (CTEM)
Given the observations made in this section of the report and the constant shifts throughout the years we have observed, we see a need more than ever for managed detection and response to evolve into something more than a “last line of defense”.

We continue to see the common avenues of attack through classification of incident data but can we do more? In an approach we will also discuss in our section “Beyond Vulnerability Management” we believe strategically that threat detection and response should evolve and move towards continuous threat exposure management, a shift from a reactive function to a more proactive practice; integrating threat detection and response activities and the data they provide into a continuous process of actually trying to fix the problems at source, not just detect them.

#### Key Data of the Year
www.orangecyberdefense.com

#### Funnel: Alert to Incident
About the Data

- Total number of incidents: 135,225 (compared with 129,395 in 2023)
- Out of these incidents, 20,706 were confirmed as true positive Incidents (14.98%)
However, not all clients include VERIS categories
- Analyzed period from October 2023 to September 2024
- Data sources: Endpoint / extended detection and response (EDR / XDR), network detection and response and SIEM platforms, as well as the enriched incident data from Orange Cyberdefense Core Fusion platform

![Funnel: Alert to Incident]

### Threat Detection
![Threat Detection]
* Overview flow with major categories, rounded to full numbers, for details see following pages

Actors
Entities causing
an incident

Action
What the threat
actor(s) did

Asset
The asset that
was affected

© Orange Cyberdefense 2024/2025

### Key Data of the Year: Threat Detection
#### Types of Incidents
Incidents are categorized according to the VERIS (Vocabulary for Event Records and Incident Sharing) framework. We record actors, actions, assets and attributes affected by an incident.

The threat action categories used in the VERIS framework consist of the following 7 primary categories: malware, hacking, social, misuse, physical, error and environmental. More information can be found in the glossary on page 116.

#### A Global View
We have grown the client base and expanded our dataset to include 21.5% more clients. Across this enlarged set we report 13.8 confirmed incidents per month per customer for the past 12 months. This number is significantly lower than the same period the previous year and the year before that. As we will explain later, this is largely because of a larger, more diverse client base, and the fact that “younger” clients generally record fewer incidents while still being onboarded.

As always, we strive to provide a global overview of what we are seeing in our incident data with the aim being to highlight trends that can also be applied to the global threat landscape. To facilitate this, a broad data set is collected from across all of the operational teams within Orange Cyberdefense including our 15 global CyberSOCs .

We consider a years’ worth of managed threat detection services data, from 1st October 2023 to 30th September 2024. The distribution between internal and external incidents is basically even this year, with incidents originating internally having increased from 37% in last year’s report.

Hacking, misuse, and malware have remained the most prominent Threat Actions, but incidents classed as “misuse” have increased substantially from 16% last year, in line with the increase in incidents originating internally. Malware incidents have increased by about 2%, and “social” incidents have retained their previous level.

End user devices have remained the most impacted assets, but have increased from 28% last year. Again, this is in line with the increase in incidents originating internally. Incidents impacting servers have decreased by about 10 percentage points from last year. Incidents impacting accounts have decreased a little from last year, while network-impacting Incidents have retained their previous level.

#### Events, Incidents, Confirmed Incidents
We log an event that has met certain conditions and is thus considered an indicator of compromise (IoC), attack or vulnerability. An incident is when this logged event, or several events, are correlated or flagged for investigation