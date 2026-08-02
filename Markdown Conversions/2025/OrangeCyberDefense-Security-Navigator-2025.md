# Security Navigator 2025: Research-driven insights to build a safer digital society

## Table of Contents
- [Foreword](#foreword)
- [Introduction: The Year 2024 in a Nutshell](#introduction-the-year-2024-in-a-nutshell)
- [Key Data of the Year: Intelligence and Operations Data](#key-data-of-the-year-intelligence-and-operations-data)
  - [Threat Detection](#threat-detection)
  - [Incidents per Month per Client](#incidents-per-month-per-client)
  - [Mean Time to Resolve](#mean-time-to-resolve)
  - [Vulnerability Scanning](#vulnerability-scanning)

---

Security Navigator 2025  
© Orange Cyberdefense  

## Foreword

> "More than ever our 2025 edition of the Security Navigator will enable you to turn challenges into opportunities. The growing but ambiguous role of AI highlights the importance of creating an ecosystem of anticipation."
> 
> — Hugues Foulon, Executive Director at Orange and CEO Orange Cyberdefense

In the world of cybersecurity, resilience is more than just a concept—it is a necessity. Over the past year, our teams at Orange Cyberdefense have observed an increasingly volatile and complex threat landscape, one that calls for both constant vigilance and innovative adaptation. The Security Navigator 2025 report presents a detailed examination of these challenges and, importantly, the proactive measures that can transform vulnerabilities into opportunities for stronger defense.

The data we have gathered over the past twelve months reveals stark shifts. Cyber extortion, hacktivism, AI-driven attacks, and threats to operational and mobile networks are not merely emerging trends; they are realities that are reshaping the cyber landscape. As malicious actors exploit new technologies and adopt increasingly aggressive tactics, the potential for harm extends beyond digital boundaries, impacting the very fabric of businesses and societies worldwide.

What makes this year’s Security Navigator unique is our expanded focus on the role of Artificial Intelligence in cybersecurity. From enhancing threat detection capabilities to mitigating complex vulnerabilities, we leverage AI to improve both offensive and defensive strategies. However, the rise of adversarial AI techniques—models specifically trained for malicious purposes—reminds us that innovation must be matched by responsibility. Our goal is not only to adopt the latest technologies but to do so thoughtfully, balancing progress with caution to secure a safer digital world.

AI is not only a land of promises, and we need to remain careful on investing in and using these new technologies. It is all about balance and analyzing the hidden side of any wide-spreading technology; just like IT, shadow AI is now at stake.

This year, we also delve deeper into the threats facing critical infrastructure, particularly within Operational Technology and mobile networks. With increased connectivity and the adoption of IoT and 5G, these systems offer an expanded attack surface that calls for comprehensive, cross-functional defenses. At Orange Cyberdefense, we understand that building cyber resilience requires collaboration at every level—from industry alliances and partnerships to close work with our clients. This is also a matter of public-private cooperation. In 2025, regulation will make the European cybersecurity ecosystem go one step up and we are ready to support this movement.

Cybersecurity today is less about containment and more about anticipation. Informed by 135,225 analyzed incidents[^1], a robust understanding of attacker behavior, and pioneering threat intelligence, our Security Navigator provides actionable insights to help our clients stay a step ahead. I am immensely proud of the dedicated work that went into this report, and I am confident that the insights it contains will empower you to face the challenges of an ever-evolving cyber threat landscape.

As we continue to confront these cyber threats together, let us remain focused on our mission: to build a safer digital society. Our commitment to this mission is stronger than ever, and we are honored to partner with you in securing a resilient digital future.

Hugues Foulon  
Executive Director at Orange and CEO Orange Cyberdefense  

[www.orangecyberdefense.com](https://www.orangecyberdefense.com)

2 Security Navigator 2025

---

## Introduction: The Year 2024 in a Nutshell

Charl van der Walt  
Head of Security Research  
Orange Cyberdefense  

### Cynical Security

I was so relieved when experts confirmed that the widely reported exploding-pager against Hezbollah did not involve a significant cyber component. The attacks in Lebanon and Syria involved modified radio pagers and other electronic devices that exploded, resulting in dozens of deaths and hundreds of injuries. Israeli intelligence is suspected to be behind the incidents. The modifications for the attacks were reportedly achieved by altering the devices at the production level to include small amounts of explosives. This allowed the attackers to distribute the modified pagers and other electronic devices widely before triggering them remotely.

When news of the incident began to emerge, people like me in cybersecurity all instinctively wondered if it had involved some kind of cyber-attack. It seemed highly unlikely, but many of us have become so cynical. And with good reason.

Cybersecurity failures – albeit not in a form suited to a Grisham novel – are indeed threatening lives. The cyber extortion attack against the South African National Health Laboratory Service (NHLS) in June this year impacted the service’s ability to generate lab reports and send them to clinicians. The disruption lasted several weeks, resulting in reports about clinics coming to a standstill, and patients in emergency wards and intensive care units in fatal danger. In an unusual twist, someone who described himself as “the middleman” called the press in South Africa to warn that related patient deaths would be “on the NHLS for not engaging”.

6 Security Navigator 2025

### Extortionate Security

As cyber extortion continues to increase globally, we note this year that it is also becoming increasingly cynical. This year Diana Selck-Paulsson examines over 13,000 cyber extortion incidents, and reports how extortion tactics are demonstrating increased aggression and moral decline, abandoning previous restraints on targeting sensitive sectors like healthcare. Once considered off-limits, hospitals and essential care facilities now face a surge in attacks. Small and medium-sized businesses are also becoming more frequent targets, accounting for over two thirds of all victims. Small businesses saw a 53% increase in cyber extortion attacks, while medium-sized businesses experienced a 52% rise. Vulnerable, smaller countries are not immune either. This year for the first time we report Cy-X victims in countries like Afghanistan, Djibouti, Tokelau, Nepal, Uzbekistan and Maldives. Attackers are also exploiting cynical “revictimization” strategies, where stolen data is reused across multiple extortion platforms and amplifying the psychological burden on victims.

### Subversive Security

This year we also explore shifts in hacktivism, which is becoming increasingly cynical and aggressive. Once grounded in activism, hacktivism now bears a closer resemblance to cyber extortion, with a focus on destabilizing communities and weaponizing fear against both individuals and institutions.

Diana also continues her excellent work on this phenomenon, examining over 6,500 hacktivist incidents to reveal how the emerging hacktivist model focuses on public manipulation, societal division, and the erosion of trust. Hacktivists are aligning with state-sponsored agendas, targeting critical infrastructure like election systems - seeking not only to disrupt essential services but also to undermine public confidence in government and democratic institutions. By attacking election-related systems and other symbolic institutions, the hacktivist groups aim to undermine public trust, disrupt the flow of information, and potentially influence the outcome of a key democratic process. By leveraging sophisticated DDoS-for-hire services and anonymous cryptocurrency incentives, hacktivists are blending public shaming with extortion techniques to exploit fear and amplify public pressure. While Europe is the primary focus for the group Diana studied, everyone is a potential target, and the problem threatens societies as a whole.

### Cyber Physical Security

Hacktivists are a significant threat to cyber-physical environments like factories, plants and utilities. In fact, our research attributes 23% of targeted attacks against operational technology environments to hacktivist actors.

Ric Derbyshire is a specialist in operational technology (OT) and industrial control systems. He’s expanded his OT security dataset to cover 119 recorded cyber-attacks over a period of 35 years. This year his unique dataset expanded with 47 incidents from the last 12 months.

This year’s insights again underscore the prevalence and impact of cyber extortion (Cy-X) on OT systems. Attacks originating in IT environments frequently cascade into OT systems, disrupting essential operations and causing downtime. Despite rarely being the primary targets, OT environments face unintended consequences due to interconnected IT and OT networks. Correspondingly, the manufacturing sector accounts for 20% of all cyber extortion victims this year and has seen a 25% increase from the previous year.

81% of this year’s documented attacks were perpetrated by criminals and primarily impacted IT systems, not OT. But, as we posited last year, threat actors will start to focus on OT systems directly when the environmental factors align.

An attack impacting Spanish bioenergy plant Matadero de Gijón in April this year is an early indicator that this may be happening already. The attack is recorded in Diana’s dataset (Cy-X) and in Ric’s dataset (OT) but stands out because it directly impacted the plant’s Supervisory Control and Data Acquisition (SCADA) system.

In this year’s report, Ric focuses on “category 2” incidents in OT - those directly targeting OT systems through adversarial tactics unique to these environments- a category that only accounts for 16% of recorded incidents. These category 2 attacks are more intentional and sophisticated, often involving advanced tactics by state-sponsored groups and sophisticated cybercriminals, who aim to directly compromise OT operations. Ric points out that 46% of category 2 attacks resulted in “manipulation of control” as an impact. This means that the adversary manipulated the physical process in their attack. This is clearly a frightening outcome, and most category 2 attacks have equally severe impacts.

Introduction: This is what happened 7

Category 2 incidents, while relatively infrequent, force our risk models to consider the unthinkable. This pressure places enormous additional responsibility on those responsible for protecting cyber-physical systems.

Ric argues that category 2 OT attacks tend to exploit native functionality within the victim’s environment—a technique known as living off the land. As with IT-attacks, this approach allows adversaries to blend in and evade detection, but it places the adversary in the optimal position to cause real damage in an environment. For example, exploiting a programmable logic controller (PLC) by using expected functions is safer and more stable for attackers than risking a memory abuse vulnerability, but also allows attackers to abuse the ability of that PLC to manipulate the physical environment.

This reality has significant implications for how we approach security in OT environments.

For example, simply accessing an OT environment doesn’t mean that an attacker can achieve a desired cyber-physical impact. This raises an essential question: how can asset owners assess their OT environment’s resilience against category 2 threats?

Ric explores significant challenges and gaps in current OT security, and specifically penetration testing approaches. The discipline is still in its infancy, with limited research and ambiguous guidance that fails to fully account for unique OT tactics, techniques, and procedures (TTPs), especially those seen in category 2 attacks. Ric critiques the reliance on IT-oriented penetration testing practices, which often focus on gaining OT access and declaring success, overlooking the complexities of truly emulating OT-focused adversaries. He questions whether current testing approaches effectively capture the nuanced tactics used in real OT attacks, such as those exploiting native functionality for stealth and control.

Our report this year highlights the need for security approaches that anticipate complex OT-specific kill chains and TTPs to more accurately ensure resilience against genuine threats. As with so many things that need to be rethought in contemporary cybersecurity, we argue this year the traditional IT frameworks are not appropriate for addressing OT’s particular threats and vulnerabilities.

### Mobile Security

In a new section of this year’s report, Orange mobile network security specialists Emmanuelle Bernard, Stéphane Gorse, and Sébastien Roché outline the evolution of mobile network vulnerabilities, describing how each generation of mobile technology (2G through 5G) has introduced advanced features alongside an expanded attack surface. While early networks primarily faced issues from weak 2G encryption, newer generations brought complex protocols like SS7 in 3G and Diameter in 4G, which attackers now exploit. With 5G, increased virtualization, APIs, and IoT integration have introduced new risks, including supply chain attacks and vulnerabilities accessible remotely through Internet-connected devices.

Our report identifies three primary attack domains: SIM cards, devices, and infrastructure. SIM-based attacks use techniques like SIM swapping, cloning, and USSD protocol misuse to intercept data or impersonate users.

Device-based threats center around malware and mobile OS exploitation, especially through alternative app stores that lack strict security. Infrastructure attacks target network protocols and exploit carrier interoperability to intercept communications. We note that MFA use on mobile devices has also complicated the risk by giving threat actors motive and opportunity to compromise network-linked authentication methods.

Our report emphasizes a layered security approach that includes enhanced standardization and collaboration among network operators, device manufacturers, and regulatory bodies. But given the cross-functional nature of mobile networks today, enterprises are also being forced to consider comprehensive security responses that range from securing devices and infrastructure to raising user awareness about safe practices.

### Struggling Security

While our adversaries are becoming more cynical, and the impact of security failures more profound, we as the defenders are still struggling to stem the flood.

This year veteran security researchers Wicus Ross and Rogan Dawes study 1.3 million vulnerabilities across 69,000 customer assets to surface a critical message: We need to change the way we think about security vulnerabilities.

Wicus’ work focuses on how businesses tackle vulnerabilities. He illustrates that vulnerabilities are emerging at such a pace that traditional, reactive measures simply aren’t keeping up. As Wicus shows, for example, vulnerability management teams face an increasingly daunting task as they contend with the overwhelming volume and velocity of new vulnerabilities. With endless new vulnerabilities emerging continuously, we are forced into a reactive mode, obliged to prioritize and address threats without control over the cadence or velocity of intelligence. Organizations with already-limited capacity are left to scramble from the back foot, unable to make sense of an ever-evolving threat landscape.

The complexity of large enterprise environments adds to these challenges, as even high-probability vulnerabilities identified by metrics like EPSS are difficult to mitigate at scale. In this report we argue that covering all potential exploits across vast networks is fundamentally impractical, meaning that crucial decisions must be made about which systems to patch first.

But we argue that the “risk-focused” approach isn’t effective either. Wicus’ study of EPSS and statistical probabilities argues that even low-severity issues at sufficient scale leave the business vulnerable to compromise. The problem calls for a fresh approach, and in this year’s report we argue that must start with a clarification of fundamental terms.

“Vulnerability Management” needs to go. Wicus proposes that new approaches with new descriptions are urgently needed.

www.orangecyberdefense.com

8 Security Navigator 2025

### Security From the Source

Wicus and Rogan both also put the responsibility on software vendors to prioritize security in software development, and throughout a products lifecycle.

As I write this, our CERT, Vulnerability Management, Threat Detection and Managed Services teams are wrestling to contain the threat and impact of “FortiJump” — a severity 9.8 vulnerability in Fortinet FortiManager.

In mid-October, Fortinet alerted key partners and select clients, including Orange Cyberdefense, to a critical 0-day vulnerability actively exploited in FortiManager, a product essential for managing security tools like FortiGate firewalls. The vulnerability allows remote attackers to execute commands on vulnerable devices by exploiting a missing authentication check in the FortiManager-to-FortiGate protocol. Fortinet has since released patches, which we and others are of course rushing to deploy. Meanwhile the bug has been actively exploited – apparently by Chinese APT actors - for some time already. Reconnaissance likely began as early as July this year, with widespread exploitation following in September. Fortinet and others are sharing specific indicators that defenders are scouring their systems for.

Despite this urgency, many products — including those explicitly designed for cybersecurity — continue to exhibit fundamental flaws that leave clients exposed. This gap is more than technical; as we detail in this report, there’s a clear and urgent need for secure-by-design principles to become an industry standard, addressing vulnerabilities at the source instead of relying on patches and workarounds after release.

Rogan’s work highlights the significant number of troubling examples of security products — firewalls, endpoint protection, intrusion prevention systems — shipping with exploitable weaknesses. These vulnerabilities are often in products that sit directly exposed to the internet, where their primary function is to facilitate secure authenticated access to sensitive areas inside an organization. Every new vulnerability uncovered in these trusted tools not only threatens the systems they protect, but also erodes confidence in the very solutions meant to safeguard our digital infrastructure.

Wicus’ study of almost 500 security advisories released by our World Watch team this year illustrates just how pervasive this problem has become. Last year security vendor Ivanti was truly in the crosshairs, but vendors in general are letting us down:

- **11 Jan 2024** – Two new 0-day vulnerabilities actively exploited against Ivanti Connect Secure VPN. This saw the start of several weeks of updates by Ivanti to release fixes for all their impacted products.
- **7 Feb 2024** – Dutch Military Intelligence and Security Service (MIVD) disclosed that Chinese state-sponsored threat actors infiltrated the Ministry of Defense of the Netherlands in 2023. Attackers were exploiting an old vulnerability in FortiOS SSL-VPN affecting FortiGate devices. In June 2024 – the MoD announced that a Chinese threat actor had compromised up to 20,000 FortiGate instances linked to the original announcement.
- **9 Feb 2024** – Fortinet fixed two critical vulnerabilities in FortiOS SSL-VPN, of which one was exploited in the wild prior to the fix.
- **18 Mar 2024** – Proof of Concept emerged for critical vulnerability in FortiOS SSL-VPN module. At the time ShadowServer identified nearly 130,000 vulnerable instances and noted exploitation attempts.
- **14 Apr 2024** – Critical vulnerability in GlobalProtect firewall from Palo Alto Networks linked to targeted 0-day exploitation. This was the only Critical (5/5) advisory from World Watch during this report period.
- **29 May 2024** – Check Point disclosed an exploited 0-day vulnerability in its remote access VPN solution. Attackers had already been attempting to exploit the vulnerability a month earlier.
- **19 Jul 2024** – CrowdStrike's Falcon Sensor update crashed Windows machines all over the world. The outage was linked to an update that had a malformed channel file.

As an industry, Rogan argues, we should be solving these problems, not creating them. As we have since 2022, we call on our partners and competitors in the security industry to come together to work on this challenge.

It feels like a fitting soundtrack for this report.

### Struggling to Respond

In the face of this barrage of threats, Wicus Ross’ analysis of our threat detection data highlights the several challenges in detecting and responding to security incidents. One key observation is the increased misuse of systems by employees. Such “insider” activity makes distinguishing between benign and malicious activities even more difficult, particularly as attackers increasingly use "Living off the Land" (LOL) methods that resemble normal user behavior. As detection teams are finding it difficult to distinguish between benign user actions and actual threats, Wicus’ report suggests that fostering "pervasive cyber judgment" across the organization is essential.

The need to respond to LOL and other “insider threats” forces detection teams to collect and analyze yet more, subtle indicators. This additional load makes separating real signals from the noise even more challenging. Our report shows that confirmed incidents, or "True Positives," comprised only 14.98% of the incidents we analyzed. The remaining incidents were classified as: 12.36% "True Legitimates" (genuine activity that posed no threat), and 61.74% "False Positives" (mistaken detections). 10.92% remained uncategorized.

The impact of this load and complexity has a measurable impact on our collective ability to detect and respond to potential incidents. This year for the first time we present insight in our Mean Time to Resolve (MTTR) statistics. This metric is complex due to varied incident types and the necessity for client coordination, but analysis reveals that while many incidents are resolved quickly, the loop on priority incidents can take over a day to close.

We remind readers of our 2024 research piece titled “Fake News and False Positives”, where we pointed out that over time there are detection efficiency gains as the relationship between our detection teams and our client teams grows and matures.

Introduction: This is what happened 9

Improved feedback loops are essential in refining detection systems and improving confirmed incident rates.

In light of these challenges, Senior CSIRT Analyst Simone Kraus examines the critical role of human analysts in threat hunting, stressing the unique value that human insights bring to the detection of sophisticated threats. While automated detection tools are useful, they cannot fully replace the intuition and adaptability of skilled security analysts who can recognize nuanced attack patterns and respond effectively. Simone introduces the concept of “threat-informed defense,” where understanding an organization’s specific threat landscape helps tailor defense strategies. This approach integrates knowledge from actual incidents and threat intelligence, allowing defenders to anticipate likely attack vectors and prioritize resources accordingly.

We also examine common organizational challenges in Incident Response in a study by Saskia Kuschke, a Senior CSIRT Investigator. Saskia’s work notes that many companies struggle with foundational elements like asset mapping. But incident readiness can also be stymied by unclear roles, lack of communication, and low user awareness, all of which contribute to slower responses and higher risks during actual incidents. Saskia proposes a structured approach to building incident response readiness. She emphasizes a hierarchy of needs, starting with essential tasks such as role assignment and incident communication protocols. Her proposed model progresses through asset mapping, visibility enhancements, and eventually, complex detection and response capabilities. This tiered approach allows organizations to scale their security efforts methodically.

### Artificial Intelligence

Like almost every research team in security, this year we consider the impact of LLMs and GenAI on the security landscape. Large Language Models - born out of advancements in natural language processing and machine learning - have transformed from rudimentary text-processing tools to sophisticated systems capable of generating human-like responses.

Anis Trabelsi is a team lead on Data and AI. This year he discusses how AI can help address the challenge of detecting beaconing—subtle, periodic communications that malware uses to connect with command-and-control servers—by leveraging AI to enhance detection capabilities. These beaconing signals often blend in with legitimate traffic, making them difficult to spot with traditional methods. Anis describes an AI-driven approach his team developed, centered on analyzing proxy logs to capture network activity in real time. By identifying repetitive requests or unusual traffic patterns, the system generates rapid alerts, enabling faster defensive actions. This research shows how AI can strengthen detection accuracy and scalability, significantly narrowing the window for attackers to exploit these covert channels.

The impact of LLMs on security defense is clearly exciting, but we make the argument this year that new technologies often favor the offensive side, so technologies like GenAI are likely to benefit attackers more than defenders.

www.orangecyberdefense.com

10 Security Navigator 2025

While these tools may enable more effective response by businesses, the same capabilities can be weaponized by malicious actors, allowing them to conduct more sophisticated attacks with greater ease. If AI is generally thought of as a productivity tool, then we can expect it to make attackers more productive also. Despite these risks, our research suggests that existing security practices are often sufficient for mitigating many of the threats associated with GenAI, although consistency is crucial.

Rather than focusing on GenAIs power for attacker or defenders, however, our report this year is primarily concerned with the broader risks that emerge when businesses and individuals adopt LLM and GenAI technologies. With continuous reports about how threat actors may (ab)use LLMs, the less colorful risk introduced in the application of the very young LLM technology as an interface by businesses is being underestimated, especially where these systems serve as a bridge between the open internet and critical business assets.

Untested, opaque AI interfaces deployed as an interface pose a significant risk to the internal systems they interface with. We cite the recent example of a breach at an NSFW AI chatbot service. Here, a hacker exploited vulnerabilities in the platform, which they described as “a handful of open-source projects duct-taped together.” This complex, poorly engineered system allowed easy access to the platform’s backend systems and data. We expect to be reporting on many more incidents like this over the next year and urge readers to be extremely cautious about how and where they deploy AI on top of their own backend systems.

Research by pentester Geoffrey Sauvageot Berland’s in this report examines the specific risk of prompt injection - manipulated inputs that can mislead or disrupt GenAI behavior. By exploiting the predictive nature of LLMs, attackers can bypass ethical and security controls, causing the model to generate unintended outputs. Techniques include “context switching,” which introduces abrupt topic shifts to elicit unauthorized responses, and obfuscation, where forbidden terms are disguised through encoding to evade content filters.

Geoffrey also warns of denial-of-service attacks that overload models with complex tasks, as well as the risks posed by multimodal applications where malicious commands can be hidden in images or audio, expanding the AI attack surface.

In the face of enormous pressure to integrate LLMs into business operations, we argue for a cautious, guarded approach that begins with a clear definition of the use-cases and desired outcomes an AI is expected to deliver, so that risks can be assessed and objectively weighed against potential benefits. We need to heed lessons from previous technology revolutions, perform rigorous security testing and thoughtful deployment of LLMs to ensure the necessary balance between security, safety and any productivity and the promised operational benefits GenAI may deliver.

### What Are We defending?

A recurring theme in this year’s report is a critical shift as attackers increasingly target perception and trust through cognitive attacks. These attacks, which go beyond traditional technical disruptions, are aimed at manipulating public opinion, undermining trust in institutions, and destabilizing societal confidence. One example involves pro-Russian hacktivist groups, who align their campaigns with major geopolitical events such as elections and summits to amplify their impact. By targeting symbolic infrastructure and leveraging public platforms like Telegram, these groups blur the line between cybercrime and influence operations. Their ultimate objective isn’t solely system disruption, but rather the erosion of trust in democratic systems and processes.

In a similar vein, cyber extortion actors employ psychological tactics to manipulate perceptions. Following a major law enforcement crackdown under Europol’s Operation Cronos, which significantly limited their operational capabilities, the Cy-X group LockBit countered by inflating their victim numbers and projecting an image of resilience and strength. This tactic aimed to maintain confidence among affiliates and instill fear in potential targets. Along with our findings on the cyber extortion phenomenon of “revictimization”, these examples exemplify how cyber extortion tactics are increasingly perception-focused, using narrative control to affect both victims’ and the criminal ecosystem’s responses.

It's into this context that Artificial intelligence (AI) is emerging as a powerful tool for attackers in cognitive operations, adding a new dimension to misinformation campaigns. State-sponsored actors from countries such as China, Russia, and Iran leverage generative AI to create realistic phishing content, fake images, and deepfakes that can deceive large audiences. These AI-supported attacks aim to influence public perception on a mass scale, from disrupting elections to discrediting political candidates, eroding trust in democratic institutions. The integration of AI into existing campaigns increases the role of cognitive attacks in the threat landscape, providing actors with scalable tools to craft highly convincing, tailored narratives to suit their needs.

These shifts represent a significant new challenge for security defenders. In addition to “simply” countering technical threats, we must now broaden our approach to incorporate strategies to counter cognitive and perception-based threats and psychology-driven attacks, which target minds as much as systems.

Security is not an objective state, it’s the subjective expression of our freedom to pursue shared visions and construct a society that is equitable and rewarding. Cognitive attacks leverage technical compromises, not as an end in themselves, but as a means of launching an assault on the fabric of trust on which “secure” systems are built. Cognitive attacks require us to not only counter technical intrusions, but also safeguard the public perception of trust we need for our digital and interconnected world to flourish.

© Orange Cyberdefense 2024/2025

---

## Key Data of the Year: Intelligence and Operations Data

### From Reactive to Proactive: Continuous Threat Exposure Management (CTEM)

Given the observations made in this section of the report and the constant shifts throughout the years we have observed, we see a need more than ever for managed detection and response to evolve into something more than a “last line of defense”.

We continue to see the common avenues of attack through classification of incident data but can we do more? In an approach we will also discuss in our section “Beyond Vulnerability Management” we believe strategically that threat detection and response should evolve and move towards continuous threat exposure management, a shift from a reactive function to a more proactive practice; integrating threat detection and response activities and the data they provide into a continuous process of actually trying to fix the problems at source, not just detect them.

www.orangecyberdefense.com

---

## Threat Detection

### About the Data

- Total number of incidents: 135,225 (compared with 129,395 in 2023)
- Out of these incidents, 20,706 were confirmed as true positive Incidents (14.98%)
- However, not all clients include VERIS categories
- Analyzed period from October 2023 to September 2024
- Data sources: Endpoint / extended detection and response (EDR / XDR), network detection and response and SIEM platforms, as well as the enriched incident data from Orange Cyberdefense Core Fusion platform

| Funnel | Potential Incidents | Confirmed Incidents |
| :--- | :--- | :--- |
| Alert to Incident | 135,225 | 20,706 |

#### Overview Breakdown by Actors, Actions, and Assets
- **Actors**: External (39%), Internal (48%), Other/Unknown Assets (16%)
- **Action**: Hacking (29%), Misuse (29%), Malware (15%), Social (13%), Account (12%), Error (8%), Other Action (4%), Partner (1%), Cloud (3%), Physical (1%), People (3%), Environment (1%), Media (1%)
- **Asset**: End user device (36%), Server (20%), Network (6%), Other (4%)

*(Overview flow with major categories, rounded to full numbers, for details see following pages)*

© Orange Cyberdefense 2024/2025

---

## Incidents per Month per Client

### Detection Efficiency for Clients Older Than 36 Months Over Time

*(Confirmed vs Other / false positives, etc.)*

- **SN21**: 148.26
- **SN22**: 88.90
- **SN23**: 87.73
- **SN24**: 67.50
- **SN25**: 49.17 (Confirmed & Other metrics blended over historical tracking)

The chart above explains the changes we are seeing by comparing the incidents for “loyal” customers who have been with us for 36 months or more. The chart shows clearly how the total number of incidents has grown as a result of heightened activity and improved detections, while the number of “confirmed incidents” has decreased as triage and analysis processes have improved.

In our Security Navigator 2024 research piece titled “Fake news and false positives”, we pointed out that over time there are detection efficiency gains as the relationship between us and our clients grows and matures. Improved feedback from the client in response to incidents helps us tune technology and processes and boosts the overall confirmed incident rate.

Another notable change this year is that “misuse” as a percentage of threat actions has increased from 16.61% to 28.27% and thus almost matches hacking as a threat action.

---

## Mean Time to Resolve

This year for the first time we are pleased to include mean time to resolve (MTTR) statistics in this report. In our operation we record the time it takes in minutes from when an alert is raised, through triage, analysis and reporting, to when it can be categorized and closed with the approval of the client. MTTR is a prickly metric and can easily mislead.

We’ve taken a page from the Cyentia playbook and opted to present our data in the form of a “survival analysis", which is illustrated below. The criticism laid against MTTR is that it can be opaque. Since an uneven distribution of MTTR values, especially those on a “long tail”, can easily skew the mean, it must be expressed in a transparent manner. Using “survival analysis” goes beyond the mean and median and allows us to present a full and transparent view of MTTR performance.

### Summary:
- 27.6% of True Positive incidents are confirmed and resolved within an hour of being raised.
- 58.36% are confirmed and resolved within a day.
- On average, Priority 1 incidents are confirmed and resolved 35 hours after the initial alert was received. Bear in mind that the incident priority can only be determined during the course of the investigation and is confirmed when the incident is closed.
- 79.5% of incidents are confirmed and resolved within 5 days.
- At the end of the long tail, there are incidents that are only confirmed and resolved after 35 days.

---

## Vulnerability Scanning

The Orange Cyberdefense managed vulnerability scanning service is delivered by our vulnerability operations centers (VOC) worldwide. We are pleased to share that this year we are able to include an additional vulnerability operations center...

[^1]: Incident analysis based on data gathered globally across Orange Cyberdefense operations.

---

(VOC) to our dataset, doubling the number of VOCs Our VOC dataset consists of 68,509 unique assets, with
contributing. This addition increases the scope and range 1,337,797 unique findings.
of unique assets, geographies, and industries, and the total
number of unique assets increased 2.72 times as a result. The average finding per host is lower across all severities. Most
Unfortunately, the addition of new assets will influence or notably, the high severity findings that previously averaged
distort historical patterns. A pure like for like analysis is further 21.93 per asset are down to 11.14 in this extended dataset.
hampered due to the partitioning and anonymization of entities Similarly, the average number of critical findings decreased
in the data. Note also that each environment is different, as is almost by half from 7.05 previously to 3.72 now.
each business, and what is true for one business may not hold
We welcome this apparently rosier outlook, but bear in mind
for another, even in the same industry in another region.
that the additional assets distort these figures, so this should
The other chapter in this report on vulnerability research - titled be seen as new perspective, rather than an “improvement”.
“Beyond vulnerability management” – is complimentary to this
The distribution of severity level across findings has changed
one, and we urge you to consider that in combination with our
less dramatically than the average severity. Severities “medium”
analysis of the VOC data here.
and “high” swapped places, with medium – now ranked first -
increasing from 38.4% to 40.65%.
Findings by Severity
Meanwhile high severity findings, now ranked second,
Before we start, we need to clarify some terminology. We will decreased their proportion from 41% to 37.25%. The share
use “unique assets” and “unique findings” throughout this of low and critical issues occupied the same rankings at third
section. Unique findings are always associated with an asset and fourth respectively. While the share of findings rated low
and the unique asset is defined in terms of the client. increased from 11.2% to 15.4%, the share of critical rated
findings declined from 9.4% to 6.69%. These proportions are
Unique assets are defined in terms of:
across all findings.
▪ Client
▪ Asset Name
▪ IP Address
▪ Host Type
Severity of Findings
Average Findings per Unique Asset and Total Severity Distribution
Critical High Medium Low
12
6.69%
15.41%
11.14
10
10.37
8
6
37.25%
4
3.72 3.88 40.65%
2
0
Critical High Medium Low
www.orangecyberdefense.com

22 Security Navigator 2025
Readers with good memories will spot the increase in this The ratio between the medium and low severity findings is
year’s maximum age and the increase in the overall average similarly spaced for this year and last regarding maximum age.
age of vulnerabilities. The extreme maximum age is attributed The ratio for critical to medium and high to medium is slightly
to findings associated with assets from specific clients in the better for this year than before.
Retail Trade industry. This eccentricity is due to one client
The average age across all findings is higher, most noticeably
whose existing vulnerability scanning records were included
for critical and high severity findings. In both these cases,
when they were onboarded to our service, thus skewing
the average age of findings is more than double the previous
the curve. Excluding this client from the dataset lowers the
dataset. The average age in days of critical rated findings
maximum age for all severity types to between 1809 and
increases from 88 to 215, and the average age in days for high
1855 days, or 5 years. In the previous Security Navigator, we
severity findings increases from 82 to 189.86. These numbers
reported a maximum age between 1441 and 1486 days. This
are opaque as they only speak to what we observe in the
age is somewhat arbitrary, however, since it generally simply
environments we scan and are not a reflection on Orange
reflects the time elapsed since we started scanning those
Cyberdefense’s service levels on patch management.
assets. These old vulnerabilities just keep getting older, in
other words. The average age of medium and low severity findings is higher,
from 185 to 247.48 and 208 to 267.82.
Removing "retail & trade" clients from the mix lowers
the maximum age, but it remains concerning that these The expansion of our dataset with the inclusion of a second
vulnerabilities have “survived” for yet another year. The average VOC exposes the long tail of vulnerabilities that persist without
age across all severities is actually slightly lower in this year’s remediation. This, beyond just the 162 day median age for all
dataset, suggesting that our clients in the retail & trade have a findings, skews the distribution.
particular challenge with eliminating some vulnerabilities.
Age of Findings
Average and Maximum Age of Vulnerabilities Found (in Days)
Maximum age Average age
4,000
3,512 3,512
3,500
3,053
3,000
2,694
2,500
2,000
1,500
1,000
500
214.61 189.86 247.48 267.82
0
Critical High Medium Low
Age of Findings
Average and Maximum Age of Vulnerabilities Found (in Days), Excluding Retail & Trade
Maximum age Average age
2,000
1,809 1,809 1,855 1,827
1,800
1,600
1,400
1,200
1,000
800
600
400
214.27 188.8 245 261.21
200
0
Critical High Medium Low
© Orange Cyberdefense 2024/2025

Key Data of the Year: Vulnerability Scanning
Severity Over Time
Proportions of Severity Along the Age Axis (in Days)
Critical High Medium Low
An eye-catching feature in this year’s data is how many more In this comparison we examine assets that are accessible
high severity findings we see on external (internet) facing through the web browser (web) versus non-web assets
assets. The average number of high severity findings on (infrastructure). As with our previous analysis, the contrast
external hosts is 10.5 in this year’s data, compared to 2.83 is clear and there is a similar trend. Our clients are dealing
before. The average number of critical, medium, and low with far fewer unique vulnerabilities on web assets than on
findings per unique asset is also higher, most notably for infrastructure, desktops and servers.
critical.
Both infrastructure and web are 20 points lower compared to
Compared to last year, the average number of findings on the previous year. Examining the severity ratios for the web
Internal is lower overall, across all severities. Critical, high and category reveals that there are fewer critical severities as a
low rated severities are almost as common as for external proportion this year, but proportionally more findings rated
assets. Medium rated severities on average are more common high. Comparing ratios on infrastructure to the previous year
on Internal assets, however. shows that the proportion of high severity findings is lower this
year, aligned with the medium severity findings now.
Findings for assets grouped under internal are 21 points lower
than before, whereas the average unique findings for assets The expanded VOC dataset has a lower level of average
under external are 6 points higher. findings for both internal and web groupings. As cautioned
earlier, however, it would be too soon to celebrate this as a win.
sgnidniF
fo
.oN
350000
300000
250000
200000
150000
100000
50000
0
0 021 042 063 084 006 027 048 069 0801 0021 0231 0441 0651 0861 0081 0891 0012 0522 0342 0552 0072 0192 0303
23
The shape of the age-versus-severities chart is somewhat different to last year. The long “tail” depicted by the
severities starting at 840 days (about 2 and a half years) is now very evident, even if it is concentrated in one industry.
Also, the “body” of the distribution has bulked up at the median age, balancing the volume at 162 days (about 5 and a
half months). This illustration also shows that the “meat” of unpatched findings consists primarily of medium findings.
Finding Severity by Target Exposure Finding Severity by Target Type
Critical High Medium Low Critical High Medium Low
35 35
30 30
25 25
20 20
15 15
10 10
5 5
0 0
External Internal Infrastructure Web
www.orangecyberdefense.com

24 Security Navigator 2025
Criticality of Findings by Operating System
Critical and High Findings (Sorted by Highest Percentage of Critical Findings)
Critical High
Windows 10
Windows Server 2012 R2
Windows Server 2008 R2
Windows Server 2022
Windows Server 2016
Windows Server 2019
Windows 2008
Windows 2016
Windows 11
Windows 7
Linux
Windows
Windows 2003
Windows Server 2008
Windows 2012
Windows Server 2003
Windows Vista
Unknown
0% 5% 10% 15% 20% 25% 30% 35% 40% 45%
Findings by Operating System How does this relate to vulnerability characteristics associated
with Windows 10, which accounts for the majority of high and
The conversation around software quality and how that relates critical vulnerabilities in our dataset?
to software vulnerabilities has been put in the spotlight in
First, we identify all the unique common vulnerability
2024, specifically around topics such as “secure by design”
enumerations (CVEs) identified by our VOC on assets running
and “security debt”[10][11][12]. These topics are touched on in our
Windows 10. Next, we examine the associated common
research chapter titled “Beyond Vulnerability Management”.
weakness enumeration (CWE) assigned to these CVEs[13]. A
We can dip briefly into this topic by examining which operating CWE is a class of software or hardware weakness that could
system (OS) ranks the most prominent in our VOC dataset be exploited by an attacker. CWEs are rather technical and rich
regarding number of vulnerabilities. This is also useful for in annotation and are represented by a hierarchy of cascading
determining how the introduction of additional unique assets technical specifics.
may have influenced the ranking compared to our previous
examination. Spoiler alert - not much changed!
One aspect of the “secure by design” best practice guidelines
is memory safety, such as using programming languages that
eliminate certain classes of vulnerabilities as well as other
defensive programming techniques.
© Orange Cyberdefense 2024/2025

Key Data of the Year: Vulnerability Scanning 25
Finally, we map each CWE to the topmost abstract CWE class. W eaknesses in Win 10
In the case of Windows 10 the two most prominent CWEs point
to resource mismanagement (CWE-707 and CWE-664)[14][15]. I.e. Most Prominent Common Weakness Enumeration
weaknesses in how software is handling memory during
(CWE-787) and after (CWE-416) use. C
W
▪ CWE-707, 'Improper Neutralization', is a top level C W E -1
E 9
CWE abstraction and occurs when a product handles -2 0
0
malformed input that corrupts memory in a way that C
W
benefits the attacker and could possibly lead to security E-122
violations.
▪ CWE-787, 'Out-of-bounds Write', is a specialization of
C
w
W
he
E
n
- 7
th
0
e
7
p
th
ro
a
d
t i
u
s
c
c
t
a
is
u s
w
e
r
d
it in
b
g
y i
d
m
a
p
ta
r o
to
p e
m
r
e
b
m
ou
o
n
r
d
y,
s
c
c
a
h
u
e
s
c
in
k
g
in g
CWE-125
CWE-416
corruption that can lead to further security violation
CWE-707
such as malicious code execution.
▪ CWE-664, 'Improper Control of a Resource Through
CWE-664
its Lifetime', is a top level abstraction associated with
mismanagement of resources such as memory.
▪ CWE-416, 'Use after Free', is a specialization of CWE-
664 and is a programming fault wherein the product
WE-787
C
incorrectly interacts with memory that it explicitly
Eliminat m v i i n o a g l r a k t t h e io e d n s a s e s s k u u in n c d u h s s a e o s d f m v re u a s l l n i u c e l i t r o i a n u b g s i l i i c n ti o e p d s o e i t s e e n t x o t e i u a c g l u h s ti e o a c n n u . d r it p y r obably 8 0 9- E W C 0 0 2- E W C 9 5- E W C C W E -8 4 3
requires substantial redesign and rewriting of code. If by some
miracle Microsoft could hypothetically eliminate all Windows 10
vulnerabilities classified as either CWE-787 or CWE-416 then
our VOC data set will shrink by 3,974 CVEs.
To continue the hypothetical experiment, let’s assume we can
eliminate all vulnerabilities classified under CWE-707 and CWE-
664. This action will eliminate 13,596 vulnerabilities associated
with Windows 10 from our VOC dataset, and by extension other
versions of the Microsoft operating system that shares code
with it.
Conclusion
Vendors must strive to continuously improve their product design, development, and
quality assurance processes to actively seek out these classes of vulnerabilities.
A cultural shift is required to ensure usage of software development best practices. It
comes down to a combination of defensive programming, explicit fault finding through
test cases and code coverage, formal code reviews, static and dynamic code testing,
and more.
Introducing memory safe programming languages could potentially also eliminate
many of the problems.
www.orangecyberdefense.com

Cyber Extortion
Cyber extortion, or “Cy-X” is a form of computer crime in which
the security of a corporate digital asset (confidentiality, integrity
or availability) is compromised and exploited in a threat of some
Summary
form to extort a payment. Cy-X groups compromise, name,
shame and extort victims via dedicated data leak sites on the
A noteworthy observation is that for the first
dark web, which we can track. Since last year’s report, we have
time since 2020, the distinct actor count is not
added 40 unique leak sites to our tracking.
directly correlated with the victim count. Up
Since January 2020, we have recorded 13,308 victim until 2023, we could argue that the number
organizations exposed on leak sites. These leaks are from 141 of victims tracked the number of actors
distinct Cy-X brands. engaging in this form of crime. This might be
changing, as Q1 2024 recorded the largest
In the past 12 months, we documented 4,201 Cy-X victims.
number of actors we’ve seen so far (46) but not
This is an increase of 15.29% since we published the Security
proportionally more victims. While we tracked
Navigator 2024. In 2022 we observed a decrease in victim
an increase in active actors, we actually
volumes as major Cy-X brands were apparently distracted by
observed a slight decrease in victims.
the first year of the war against Ukraine. Activity accelerated
dramatically as the threat actors regrouped, and the volume of
victims appears to be “normalizing” since then.
1400 50
2020 2021 2022 2023 2024
1200
40
1000
30
800
600
20
400
10
200
0 0
Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3
09
842 915 556 024 725 095 957 875 665 394 665 528
5201 9801 5901 3601 7301 6001
26 Security Navigator 2025
Cy-X Over Time
Victims and Actors Count Observed on Double-Extortion Leak Sites Over Time
Victims count No. of actors
46
44 44
43
40
39
34
33
30
26 26
24 24 24
23
21
18
13
12
© Orange Cyberdefense 2024/2025

Key Data of the Year: Cyber Extortion
250
2020 2021 2022 2023 2024
200
150
100
50
0
A Criminal Career The Cy-X Recast – Who’s Next?
Must End at Some Point
After a major operation like LockBit becomes defunct or slows
down, we often see an increase in new brands popping up to fill
One potential explanation for the slowdown in victim count
the void. Since June 2024, therefore, we added 19 new leak
could be the continuous efforts of law enforcement to take
sites, 10 of them recorded victims before June 2024 but only
down LockBit - one of the most active Cy-X brands ever – that
became known to us then.
has been active since 2019.
It is difficult to know how new the threat actors really are, as the
In February 2024, it finally happened. Law enforcement
ecosystem is very flexible, and affiliates can choose to switch
released an announcement of their coordinated effort to take
between Cy-X brands. In the past 12 months, we have tracked
down LockBit, which was dubbed 'Operation Cronos'[16][17][18].
68 unique threat actor leak sites actively extorting victims. This
The Cronos operation was a major Europol-led initiative
shows an increase of 26% since last year’s report.
focused on dismantling the high-profile cybercrime network.
While Cronos significantly contributed to LockBit’s disruption, For those who monitor the Cy-X / ransomware space, it feels
it did not cause the group to cease activities completely. as if there are new leak sites and brands every week. In the
The operation led to server seizures, the arrest of key actors, section below, we explore what we’ve seen in actor activity over
and a notable decrease in LockBit's capacity, causing some the past 12 months.
operations to run at a limited scale.
During the initial waves of Cronos disruption, particularly in
May 2024, LockBit sought to project an image of resilience
by posting a high volume of alleged victims. However, many
Summary
of these claims could not be independently verified, raising
suspicions that the group was more focused on shaping a
The Cy-X threat landscape has seen
narrative of continued strength than conducting actual attack
significant shifts in the past 12 months, with
activity. Despite significant setbacks dealt by law enforcement,
some of the most notorious groups declining
LockBit has not been completely dismantled and continues to
while new actors emerge rapidly.
maintain a presence, albeit with diminished capacity.
The impact of operation Cronos likely undermined the trust of Law enforcement disruptions may have
LockBit’s affiliates and the broader cyber extortion ecosystem. contributed to the declines, but the rapid
Affiliates may hesitate to collaborate, fearing increased law emergence of new groups underscores the
enforcement scrutiny or diminished returns. This erosion of persistent and evolving nature of this highly
trust could lead affiliates to move to other ransomware-as-a- volatile ecosystem.
service (RaaS) operations, particularly as several new brands
have emerged in late summer.
peS tcO ceD luJ guA peS tcO voN ceD naJ beF raM rpA yaM nuJ luJ guA peS tcO voN ceD naJ beF raM rpA yaM nuJ luJ guA peS tcO voN ceD naJ beF raM rpA yaM nuJ luJ guA peS
27
Lockbit Activity Over time
LockBit LockBit2 LockBit3
www.orangecyberdefense.com

As expected, a few Cy-X groups have ceased drastically or Similarly, Akira emerged from the lower ranks last year to
disappeared entirely. We track this as “significant decrease become one of the most active groups of 2024, with 215
in activity”. This group includes major Cy-X brands like Cl0p, incidents reported. Black Basta also saw substantial growth,
who’s victim count dropped by 377 after being highly active in rapidly accelerating its activity over the past 12 months. Other
2023. It might be that they are still benefiting financially from notable risers include Hunters - which reported 187 incidents
last year’s mass exploitation campaigns. ALPHV (BlackCat) after a period of inactivity - and Play, which expanded from 187
ceased operations entirely following an attempted law incidents in 2023 to 359 in 2024.
enforcement disruption attempt and a subsequent exit scam.
Other groups with significant increases include BianLian (+161),
The threat actor Royal rebranded as BlackSuit, and we have
Qilin (+101), Black Suit (+112), incransom (+96), Medusa (+53),
already discussed LockBit.
and Rhysida (+47), illustrating the emergence of new and
In contrast to the groups experiencing declines, several Cy-X reactivated actors in the ransomware landscape.
groups have surged in activity over the past year. Ransomhub
recorded the largest increase, with 287 incidents in 2024 from
being inactive in 2023.
073-
polC
022-
)taCkcalB(
VHPLA
861-
layoR
951-
esaB8
521-
3tiBkcoL
301-
tsurttsol
27-
yteicoSeciV
46-
etyBkcalB
94-
trukaraK
03-
skaeLeviH
92-
rekcoLrangaR
82-
hctanS
51-
VL
1-
rekcoLsovA
11-
abuC
01-
cvdemosnar
9-
ecarkraD
9-
kaeL
llihgnuD
8-
suomrots
6-
spolcyc
6-
xollaM
5-
zneroL
5-
cileR
5-
attedneV
4-
mutnauQ
3-
2livER
2-
teNtpyrC
2-
zocnar
1-
kcoL
ssorC
1-
anogirt
0
nixiaD
0
epacseon
1
egasseM
yenoM
2
rotpyrcneatem
2
skaelacro
2
ytinirT
3
xyrP
3
cesirT
3
puorG
rinaV
4
agem0
5
tibhpic
7
)spolcyc(
thgink
8
XXEmosnaR
8
dnuorgrednU
8
tuokcalB
8
eramwosnaR
gnoluiQ
9
rotarebiL
daM
11
kaolc
11
rehpiC
niarB
21
puorG
AR
31
tunoD
51
esuohmosnaR
51
maeerht
51
goF
51
atadym
61
37tpa
61
puorG
erawmosnaR
deR
71
nwodlleH
81
n0nAd
02
woeM
22
tserevE
32
tluaV
kraD
72
xnyl
82
ITNOM
92
1033adaciC
53
aideM
sucrA
83
ssybA
93
ytiruceS
lliK
14
dlrow
AR
34
ecrofnogard
74
adisyhR
35
asudeM
59
sutcac
69
mosnarcni
101
niliQ
211
tiuS
kcalB
161
naiLnaiB
271
yalP
781
sretnuh
302
atsaB
kcalB
512
arikA
782
buhmosnaR
28 Security Navigator 2025
Cy-X Victims by Actor
Change in Victim Count of Different Actors – Winners and Losers
Increase Decrease
500
400
300
200
100
0
-100
-200
-300
-400
-500
Top 20 Actors in the Past 12 Months
The Most Active Extortion Groups Observed
23% Lockbit3 4% cactus
3%
3% 23% 10% Play 4% ALPHV (BlackCat)
3%
8% Ransomhub 3% Black Suit
4%
6% Akira 3% incransom
4%
6% Black Basta 3% Rhysidia
4%
6% 8Base 3% noescape
10%
4%
5% hunters 2% MONTI
5% 5% BianLian 1% dragonforce
8%
5% 4% Medusa 1% RA World
6% 6%
6% 4% Qilin 1% Kill Security
© Orange Cyberdefense 2024/2025

|     |     |     |     |     |     |     |     |     | Key Data of the Year: Cyber Extortion |     |     |     |     | 29  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
Regional Shift in Victim Count
Victims Count and Delta in Percent  Last 12 Months Prior 12 Months Delta %
| 3000 |     |     |     |     |     |     |     |     |     |     |     |     |     | 50% |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7832
38%
40%
2500
7191
30%
25%
| 2000 | 18% |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|      |     | 16% |     |     |     |     |     |     |     |     |     |     |     | 20% |
11%
| 1500 |     |     |     |     |     |     |     |     |     |     |     |     |     | 10% |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1%
1%
0%
547
| 1000 |     | 136     |      |       |              |     |       |      |          |      |                |                 |         |      |
| ---- | --- | ------- | ---- | ----- | ------------ | --- | ----- | ---- | -------- | ---- | -------------- | --------------- | ------- | ---- |
|      |     |         | -5%  |       |              |     |       |      | -5%      |      | -13%           |                 |         |      |
|      |     |         |      |       |              |     | -6%   |      |          |      |                | -7%             |         | -10% |
|      |     |         |      | -9%   |              |     |       |      |          |      | -19%           |                 |         |      |
| 500  |     | 152 712 | 102  | 112   |              |     |       |      |          |      |                |                 |         |      |
|      |     |         |      | 401   | 411 001 99   | 08  | 58 97 | 87   |          |      |                |                 |         | -20% |
|      |     |         |      |       |              |     |       | 56   | 74 95 26 | 75   | 07 12 42       | 31              | 41 01 9 |      |
| 0    |     |         |      |       |              |     |       |      |          |      |                |                 |         | -30% |
| C A  | p e | m       | c a  | Asia  | ni a         | C N | East  | dics | dia      | ic a | li c           | o n             | dia     |      |
| &    | o   | d o     | meri |       | ea Asia  ex  |     |       |      | n        | fr   | u b a          | g i             | n       |      |
| S    | ur  | g       |      | East  | Oc           |     | e     | or   | I        | A    | p h i n        | n r e Asia ex I |         |      |
| U    | E   | Ki n    | A    |       |              |     | dl    | N    |          |      | Re C           |                 |         |      |
|      |     | d       | n    | h-    |              |     | Mi d  |      |          |      | e’s  o f   bea |                 |         |      |
|      |     | ite ati | ut   |       | st           |     |       |      |          |      |                |                 |         |      |
|      | n   | L       | o    |       |              |     |       |      |          |      | pl r i b       | h               |         |      |
|      | U   |         | S    |       | E a          |     |       |      |          | e o  | C a            | u t             |         |      |
|      |     |         |      |       |              |     |       |      |          | P    |                | S o             |         |      |
North America and Europe remain the most heavily impacted  Over the past 12 months, Italy and Germany are the most
regions. The U.S. remains the most impacted country, which  impacted countries when excluding the “big 3”, followed by
aligns with its position as a global economic and technological  France, Spain, and Australia.  This dynamic highlights the
hub. Generally, we don’t see the steep growth rates we’ve  wide spread of victims across diverse regions, reinforcing
reported previously. We believe this is because last year’s  our findings from previous years that cyber extortion and
report documented the resurgence of this crime after  ransomware have become truly global threats. The diversity in
geopolitical events in 2022 disrupted the Cy-X ecosystem  affected countries underscores the increasingly indiscriminate
temporarily.  and global nature of the cyber extortion phenomenon.
In Europe we see France, Italy, Germany, Spain and the  In total  we observed victims in 116 unique countries over the
Netherlands impacted the most. The Nordic region (including  past 12 months, which equates to about 60% of the world.
Sweden, Denmark, Norway and Finland, Iceland and  Countries we recorded for the first time in our victim data were:
Greenland) has seen the highest growth in the past 12 months,  Afghanistan (Central Asia), Jersey (Europe), Djibouti (Africa),
although the count of victims is still low relative to other regions.   Georgia (West Asia), Timor-Leste (SEA), Myanmar (SEA),
Tokelau (Oceania), Nepal (South Asia ex India), Sudan (Africa),
Noteworthy is the observed decrease in victim numbers for
Saint Vincent and the Grenadines (Caribbean region), Curaçao
regions like South East Asia (SEA), East Asia (excluding China),
(Caribbean region), Palau (Oceania), Sierra Leone (Africa),
India, Africa, China and the Caribbean.
Uzbekistan (Central Asia), Maldives (South Asia ex India), Niger
As we have reported in the past, we note that large English- (Africa), and Cuba (Caribbean region).
speaking regions feature prominently in our victim dataset. We
present a country breakdown, excluding United States, Canada
and Great Britain, in the graphic below.
Top 30 countries
Excluding US, CA, GB
160
140
120
100
80
60
40
20
041 041 711 59 68 48 95 64 54 24 83 23 72 42 42 42 32 32 32 22 22 12 02 91 91
71 51
0
IT DE FR ES AU BR IN BE NL JP MX CH SE TW PL AE AR ZA ID DK TH CN SG CZ MY AT TR
www.orangecyberdefense.com

30 Security Navigator 2025
Business Size Victim Size
Number of Victim Organizations by Number of Employees
Organizations of all sizes have been affected by Cy-X attacks
over the past 12 months. In this analysis, business size is
classified according to the OECD standard: Small businesses
are defined as those with 1-49 employees, medium-sized
8% +53%
businesses range from 50 to 249 employees, and large +52%
organizations have 250 or more employees.
The distribution of impacted organizations across size is 32%
relatively balanced, with small businesses accounting for 32%
of affected entities, followed closely by large organizations and 32% Small
medium-sized businesses, each representing 30%. 30% 30% Medium
Compared to the previous year's data, we’ve recorded a 30% Large
substantial increase of 53% in small businesses victims. We 8% Unknown
also witnessed a 52% increase in medium-sized business
victims. On the other hand, we recorded 9% fewer victims that
could be classified as “large”. It’s too soon to say, but this shift
may indicate that ransomware affiliates are choosing to throw
their nets wider, perhaps in response to improved security by
larger organizations. Alternatively, perhaps it’s simply becoming 30%
harder to find large organizations that have not already been
compromised. This is a trend worth watching. -9%
Damaging Reputations
Beyond the trends we've described so far, there
has also been a noticeable shift in the tone
and behavior of threat actors on the dark web.
Listings have become increasingly aggressive,
with attackers resorting to more harassing
tactics. This includes naming individuals within
impacted organizations, exposing their own
“private” communications with the victims, and
publishing links to victims' professional social
media profiles.
Also discussed in our Cy-Xplorer report is the
growing phenomenon called “revictimization”
in which victims' stolen information is shared
across multiple Cy-X brands, amplifying the
harm. This approach not only maximizes
the psychological impact on the victims but
also opens every possible opportunity for
monetization. We will continue to monitor
this trend as brands maximize the victim's
distress and their own gain, by pushing to
extract as much value as possible from
each attack.
©© OOrraannggee CCyybbeerrddeeffeennssee 22002244//22002255

Key Data of the Year: World Watch 31
World Watch
The long arm of the law is starting to catch up. At the same
time cybercriminals and ransomware groups scatter to
About the data reform later.
▪ The protracted war against Ukraine has seen both Russia
▪ Period October 2023 to September 2024 and Ukraine leveraging their capabilities to influence and
▪ 474 World Watch advisories delivered disrupt the opponent. Hacktivism is further blurring the
▪ Themes: threat, vulnerability, breach, news lines between combatants and civilians.
▪ One critical advisory issued with 2 updates ▪ The conflict between Israel, Hamas, Hezbollah, and Iran
has escalated. This conflict is also waged in cyberspace.
▪ Category distribution: threat (68%),
Tactics like hack-and-leak, disruption, and disinformation
vulnerability (30%), breach (1%), news (1%)
are repeated here as well. Certain attacks are hybrid in
nature, whereby cyber is just one facet.
▪ Several critical vulnerabilities were disclosed throughout
The Orange Cyberdefense World Watch (WW) service gathers, the past year. We’re once again faced with a significant
examines, prioritizes, contextualizes, and summarizes the number of vulnerabilities reported in security vendor
crucial threat and vulnerability information that customers products. These vulnerabilities are often in products that
require to make well-informed decisions[19]. WW published 474 sit directly exposed to the internet, where their primary
advisories over the past 12 months, mostly covering threats function is to facilitate secure authenticated access to
and vulnerabilities, and (to a lesser extent) breaches and news sensitive areas inside an organization. Security flaws in
that is relevant to our clients. these products act like an open door that attackers can
walk through.
Major themes that emerged within the advisories we published
include: ▪ We reported on various state-backed attackers as well as
▪ France was the host of the Paris 2024 Olympics in July
financially and politically motivated attackers.
2024 and attackers from across cyberspace used the We continue to track and advise our customers on threat
opportunity to disrupt, influence, or capitalize on the intelligence regarding attacker behaviors and resulting
excitement around the event. We reported on several incidents as these continue to evolve.
instances of cybercrime, disruption, influence operations,
and hacktivism associated with the event.
▪ Law enforcement have continued intensifying their
fight against cybercriminals as we reported on various
successful takedowns and disruptions. The efforts of
multiple jurisdictions working in concert are starting to
make life difficult for miscreants.
World Watch Advisories per Month
New Advisories vs. Updates Published in the Past 12 Months
New Update
40
2023 2024
35 35
35
30
27
26
25 24
23
22
21 21
20 20
20 19 19
18 18
17 17
16 16 16
15 15
15
12 12
10
5
0
Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep
▪ July 2024 has 10 advisories that were posted in French in addition to English and relates to the Paris 2024 Olympics.
www.orangecyberdefense.com

32 Security Navigator 2025
World Watch Advisories by Severity
Criticality of Advisories (New and Updated) Over Time
Critical High Medium Low Very low Info
65
2023 2024
60
0.62%
55
50 2.69%
10.74%
45
19.83%
40
35
30
30.79%
25
20
15
35.33%
10
5
0
Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep
Law Enforcement Successes Infrastructure, decryption keys, crypto wallets, and source
code were seized, and two arrests were made. Over the course
In the research chapter titled “Why aren’t we more effective in of several months, we provided updates as law enforcement
defending against Cyber Extortion?” from last year’s Security proceeded to chip away at LockBit as the group wrestled
Navigator, we explored the challenges that law enforcement to recover from successive blows. LockBit continues to
faces in fighting Cyber Extortion. We did not anticipate the operate today, but not at the same volume as before the initial
subsequent series of law enforcement actions that eventually takedown.
led to the dismantlement and take down of key cyber-criminal
'Operation Endgame' is yet another example of law
enterprises.
enforcement working to disrupt cyber criminals with
In October 2023, joint action by Europol, FBI, and Eurojust coordinated activity. Between May 27 and May 29, Europol
resulted in the takedown of infrastructure linked to the and several partner agencies disrupted infrastructure
RagnarLocker ransomware group. One of the group’s main associated with malware spreading services such as IcedID,
developers was arrested and crypto assets were seized. SmokeLoader, Pikabot, Bumblebee, SystemBC, and Trickbot.
A large sum of cryptocurrency assets was seized. The
In last year’s report we highlighted that the Cy-X brand LockBit
amorphous nature of these cybercriminal operations allows
was an anomaly with respect to the expected “lifespan” of
the activities to resurface if the criminals are not arrested.
such groups, as it appeared to be somewhat “untouchable”
by law enforcement. In February 2024, Operation Cronos was
announced, showcasing the combined successes of several
jurisdictions in fighting LockBit.
©© OOrraannggee CCyybbeerrddeeffeennssee 22002244//22002255

Key Data of the Year: World Watch
Paris 2024 Olympics Incident Types
Anssi Tracking of Incidents During the Olympics
The Paris 2024 Olympics attracted enormous international
attention, as athletes from many nations competed for glory.
The WW coverage of the event spanned several weeks, as we
anticipated malicious activity related to cybercrime, hacktivism,
disruption, influence campaigns, and espionage.
Cybercrime, specifically scams and fraud like illegal ticket and
merchandise sales, was a continuous theme in our advisories.
There was also a cyber extortion attack impacting a network
of the Grand Palais exhibit hall, although this did not impact 258
the Olympic events held there. We also reported on numerous
hacktivist attacks involving distributed denial of service (DDoS)
impacting French organizations. For example, a hacktivist
persona known as “LulzSec Muslims” hacked a website 92
associated with the French National Olympic and Sports 65 64
Committee (Comité National Olympique et Sportif Français).
This assault also didn’t impact the Paris 2024 Olympic games.
DDoS Attacks Intrusion attempts
In another example, a pro-Russian hacktivist group called
Data leaks Compromised accounts
Beregini[20] reportedly leaked data from the Polish Anti-Doping
Agency, with names of Polish athletes allegedly linked to
performance-enhancing drugs[21].
Finally, there were a handful of reports on influence operations spreading disinformation regarding the Paris 2024 Olympic games.
DFRLab, NewsGuard, and Harfang Lab linked the activity to Russian actors[22][23][24]. The disinformation was spread through a
news network as well as actor-controlled social media accounts. This dynamic also involves coordination between technical
actors and disinformation agents, leveraging anonymized social media accounts, actor-controlled news networks, and cyber
techniques like redirection chains and botnets.
Summary as Summary by
consolidated by ANSSI Orange Cyberdefense
548 cybersecurity alerts from No increase in cyber incidents during the period
May 8 to September 8, 2024.
202 security alerts raised on the scope related to
Paris 2024 monitored by our CyberSOC, including
Leading to 83 incidents,
10 DDoS attacks that were mitigated
Resulting in minimal impact, Only one incident related to a direct supplier
no disturbance on the execution of the event itself of the Olympics
Phishing Cases During the Olympics
Cases Handled by Orange Cyberdefense CERT
140
22
luJ
32
luJ
42
luJ
52
luJ
62
luJ
72
luJ
82
luJ
92
luJ
03
luJ
13
luJ
1
guA
2
guA
3
guA
4
guA
5
guA
6
guA
7
guA
8
guA
9
guA
01
guA
11
guA
33
120
100
80
60
40
20
0
www.orangecyberdefense.com

34 Security Navigator 2025
Long-Running Conflicts In October 2023 the tension between Israel and Hamas
escalated beyond anything seen in the past. The result of
There are several World Watch advisories spanning many years Hamas’ attack on Israel and the ensuing reprisal spilled over
that track cyber related threats associated with war or armed into cyberspace. Both sides have reportedly targeted networks
conflict. with DDoS attacks, also exploiting hosts to deface websites or
leak stolen data[30]. Disinformation campaigns followed, trying
Russia’s war against Ukraine is one such conflict that we
to influence opinions and discredit the opposing side[31].
continue to track, and we have issued 8 updates relating to
malware, hacktivism, and disinformation associated with that Hacktivists responded to attack those on the opposite side,
conflict over the past year. State-backed actors continue to and this spilled over to Europe and elsewhere. DDoS attacks
leverage their past expertise, demonstrating well developed were directed at companies, airports, and government
tactics, techniques, and procedures when executing agencies in Europe.
cyberattacks and spreading disinformation.
Suspected pro-Hamas actors created a fake Android version
As we detail in the chapter on Hacktivism in this report, pro- of an emergency services app called RedAlert, which is used
Russian hacktivism groups continue to put pressure on Ukraine by Israeli citizens. The app harvested and stole data from
and its supporters. One group[25] has been attributed with over victims[32]. A few weeks later attackers claimed they breached
6,600 attacks since March 2022, mostly targeting symbolically the RedAlert API and stole between 10,000 to 20,000 users’
important entities in Europe. Distributed Denial of Service data[33]. We cited other reports[34] that claimed attackers were
(DDoS) attacks are an effective technique for drawing attention using the Israel-Hamas conflict to conduct spear phishing
to a cause or message. Specific groups make good use of this attacks. Other attacks managed to impact industrial control
through the DDoSia project[26], using the platform to recruit and systems in Israel[35].
coordinate attacks on victims. By the first half of 2023 they had
Later, Israel’s National Cyber Directorate (INCD) released a
executed more than 1,100 DDoS attacks in 32 countries. Direct
brief outlining a Lebanon-based advanced persistent threat
links between this group and the Russian government have not
they claimed were backed by Iran. The agency also claimed
yet been publicly confirmed, but our research suggests this is
that the Lebanon-based group’s activities were responsible
the case.
for cyberattacks against Israeli hospitals. Over several months
According to reports[27], Russia continues to employ various cyberattacks ensued, and reports attributed these to
disinformation as a technique to sow discord. One example is Israel, Iran, and regional proxies of Iran[36].
that on 17 February 2024, several Ukrainian media outlets were
On 17 September 2024, a coordinated attack led to the
abused to spread fake news, having had their websites hacked
explosion of thousands of pagers belonging to Hezbollah
and disinformation planted.
members in Lebanon and Syria, leading to fatalities and
In December 2023, we learned that Kyivstar -a major telecoms severe injuries. Two days later, a similar event occurred where
operator in Ukraine - was compromised. The attack allegedly two-way handheld radios (walkie-talkie) of Iran-backed militia
impacted 24 million users of the mobile network. A group called exploded. No one claimed responsibility for these explosions. It
Solntsepyok claimed responsibility but reports eventually is unclear whether this attack included any cyber elements, but
attributed the attack to the suspected Russian APT group it is believed that a large-scale covert supply-chain attack was
called Sandworm[28]. used to plant the deadly devices[37]. Still, the incident serves
as a cold reminder of the vulnerability of supply chains in any
Ukraine has responded in kind. In June 2024, reports[29]
context.
revealed that Ukraine had launched several cyberattacks
against Russian airports, defacing some local government For now, the conflict between Israel, Hezbollah, Iran and
websites and causing flight delays. This was followed Hamas has mostly played out in the physical world and is
up by cyberattacks that disrupted Crimea’s largest still contained in that region. Very few impactful or serious
telecommunication and internet providers. Later in July cyberattacks have been seen and have mostly manifested
2024, DDoS attacks were launched against major banking as threats of intimidation with a degree of influence or
infrastructure in Russia. Reports claim that many of these disinformation.
cyberattacks by Ukraine were jointly executed by hacktivist
groups and intelligence services.
©© OOrraannggee CCyybbeerrddeeffeennssee 22002244//22002255

KKeeyy  Ddaattaa  ooff  tthhee  Yyeeaarr::  WWoorrlldd  WWaattcchh 35
| 02/10/23 – Update 1 | 11/10/23 – Update 1 |     | 02/11/23 – Update 4 |     |
| ------------------- | ------------------- | --- | ------------------- | --- |
Critical vulnerability affecting  Atlassian patches critical  Second critical BIG-IP
WS_FTP Progress Software  vulnerability affecting Confluence  vulnerability chained
exploited in the wild  Server & Confluence Data Center  together with CVE-2023-
| CVE-2023-40044 | instances  |     | 46747 in ongoing attacks |     |
| -------------- | ---------- | --- | ------------------------ | --- |
CVE-2023-22515
11/01/24 – Initial 18/12/23 – Update 7 07/11/23 – Update 1 03/11/23 – Update 1
Two new 0-day vulnerabilities  New Qakbot variant  Confluence vulnerability  Critical vulnerability in
actively exploited against  deployed in test  CVE-2023-22518  ActiveMQ exploited in the
Ivanti Connect Secure VPN  malspam campaigns exploited in the wild wild including to deploy
| CVE-2023-46805/     |                     |                    | HelloKitty ransomware   |     |
| ------------------- | ------------------- | ------------------ | ----------------------- | --- |
| CVE-2024-21887      |                     |                    | CVE-2023-46604          |     |
| 23/01/24 – Update 1 | 07/02/24 – Update 2 | 09/02/24 – Initial |                         |     |
Critical trivial vulnerability  Dutch Military Intelligence  Critical vulnerabilities CVE-
in Confluence exploited in  and Security Service  2024-21762 and CVE-2024-
the wild   disclose details about  213113 in FortiOS exploited
| CVE-2023-22527 | Nov 2023 attack | in the wild |     |     |
| -------------- | --------------- | ----------- | --- | --- |
29/05/24 – Initial 12/04/24 – Initial 18/03/24 – Update 1 20/02/24 – Initial
Check Point disclosed  Critical 0day in Palo  PoC emerges for critical  Critical authentication
exploited 0-day in its  Alto's GlobalProtect  vulnerability CVE-2024- bypass vulnerability in
ScreenConnect
| Remote Access VPN  | gateway exploited in  | 21762 in FortiOS   |     |                     |
| ------------------ | --------------------- | ------------------ | --- | ------------------- |
| solution           | the wild              | SSL-VPN module     |     | CVE-2024-1708 and   |
| CVE-2024-24919     | CVE-2024-3400         |                    |     | CVE-2024-1709       |
13/06/24 – Update 3 19/06/24 – Update 4 19/07/24 – News 12/08/24 – Update 1
Dutch Ministry of Defense  Threat actor UNC3886  CrowdStrike's Falcon  Proof-of-Concept released
announces UNC3886 threat  secretly exploiting   Sensor update error  for critical vulnerability
actor compromised up to  CVE-2023-34048   blocks Windows CVE-2024-38077 in
20,000 FortiGate instances  since late 2021 Windows Server (using
| (CVE-2022-42475) |                    |                     |     | Remote Desktop Licensing) |
| ---------------- | ------------------ | ------------------- | --- | ------------------------- |
|                  | 5/09/24 – Update 2 | 27/08/24 – Update 1 |     | 14/08/24 –  Initial       |
Legend
|     | CVE-2024-38106  | Published PoC for  |     | 2024 August (Microsoft)  |
| --- | --------------- | ------------------ | --- | ------------------------ |
Newly-discovered or  vulnerability exploited  0-click IPv6 vulnerability  Patch Tuesday: Many
exploited vulnerabilities by North Korean  CVE-2024-38063 only  vulnerabilities require
|     | threat actor | enables DoS for now |     | your attention |
| --- | ------------ | ------------------- | --- | -------------- |
State-sponsored
espionage operations
Financially motivated
campaigns
News
www.orangecyberdefense.com

36 Security Navigator 2025
Industry Comparisons
Cy-X: Shifts in Victims by Industry
Change in Victim Count In Different Industries yoy.
2023 2024
Manufacturing +25%
Professional, Scientific, & Technical Services +20%
Wholesale Trade +65%
Health Care and Social Assistance +50%
Construction +25%
Finance and Insurance -27%
Information +5%
Educational Services -25%
Retail Trade +6%
Administrative, Support and Waste mgmnt. +19%
Transportation and Warehousing +7%
Public Administration +31%
Other Services (except Public Administration) +4%
Real Estate and Rental and Leasing +18%
Accommodation and Food Services +16%
Arts, Entertainment, and Recreation +36%
Mining, Quarrying, and Oil and Gas Extraction -2%
Agriculture, Forestry, Fishing and Hunting +76%
Management of Companies and Enterprises +40%
Utilities -19%
0 200 400 600 800 1000
Industry Ranking, Victim Delta, Educational Services ranks 8th with a 25% reduction in
victims, while Finance and Insurance ranks 6th, showing a
and Most Affected Sub-Industries
27% decrease, but with a concentration of victims in Credit
Intermediation and Securities sub-sectors.
Each industry has distinct exposure to cyber extortion (Cy-X),
with some experiencing significant growth in victim counts and Public Administration experienced a 31% increase,
varying degrees of impact on sub-industries. particularly in government support and justice sectors.
Construction ranks 5th with a 25% increase, primarily
Manufacturing leads as the most impacted, comprising 22%
impacting Specialty Trade Contractors and Civil Engineering.
of all Cy-X victims and showing a 25% increase in incidents.
Finally, Retail Trade ranks 9th, with a 6% increase in incidents,
Fabricated Metal Product and Machinery Manufacturing are
especially affecting Motor Vehicle Dealers and Food Retailers.
particularly affected.
Professional, Scientific, and Technical Services ranks
second with a 20% increase, showing concentrated incidents
in Legal and Accounting Services, sub-sectors that often
handle sensitive client data.
Healthcare, ranking 4th most impacted this year, saw a
substantial 50% increase in victims, as attackers abandoned
previous ethical constraints around targeting critical healthcare
services like Ambulatory Health Care and Hospitals.
© Orange Cyberdefense 2024/2025

Key Data of the Year: Industry Comparisons 37
MTTR, Coverage Score, True Positive/ Finance and Insurance holds the highest coverage score at
55.87%, indicative of robust monitoring, though its MTTR is still
False Positive Ratio
56 hours. External actors are the primary origin, responsible
for incidents that predominantly involve hacking and social
Our CyberSOC metrics across industries provide
engineering, targeting servers and accounts.
insights into incident response effectiveness and
Our client's in Public Administration had an average MTTR
monitoring depth.
of 38.32 hours, and an average coverage score of 41.43%. We
Manufacturing’s Mean Time To Resolve (MTTR[38]) is relatively
report a true positive ratio of 20.15%. Incidents are primarily
high at 97 hours, making it the second slowest sector, while
externally sourced, with hacking and misuse actions impacting
its coverage score of 36.77% is below the average for all
end-user devices and accounts.
industries. True positives account for 20.96% of alerts.
Incidents primarily originate internally (62.48%), with misuse as Construction shows a high coverage score of 45.71% and
the primary action, impacting primarily on end-user devices. a true positive rate of 14.46%, and an MTTR of 94.7 hours.
Most incidents in this sector involve internal actors and misuse
Professional Services, aligned with the industry median
actions, affecting end-user devices, servers, and networks.
MTTR of 49 hours, has one of the lowest coverage scores at
32.04%. Incidents mostly stem from external actors (52.77%), Retail has an MTTR of about 36 hours and a coverage score
with hacking and misuse primarily affecting end-user devices of 35.1%, and a true positive rate of 24.34%. Errors and misuse
and servers. are frequent in Retail, affecting cloud and end-user devices.
Healthcare’s MTTR is 50 hours with a low coverage score of
29.04. The sector’s true positive ratio is 16.45%. Incidents often
involve malware and misuse originating from external sources
(52.62%) and targeting end-user devices and networks.
CSOC Data: Incidents by Industry
Normalized Using the Coverage Score
Confirmed Incidents (TP adjusted) Other (adjusted) Coverage Score
40% 300000
35%
250000
30%
200000
25%
20% 150000
15%
100000
10%
50000
5%
Ma 0 n % ufa T c r t a u n ri s n p g or W t P a a t r i a r o o e n f n h e d o s a T s u n e i s d o c i n n h a g n l i , c S a c l i S e e n r t v i S fi i H c o c e c e s i a a l l t h A s C s a is r A e ta c & n c & o c F e m o m o P d o u d S b a e l t i r i c o v i n A c e d s ministration Re F ta in il a T n r c a e d e and Insurance Infor m Re a a ti l o E n stat a e M n , d i R n L i e n e n a g a t n , a s d Q l i n u G g a a r s r y E in x g tr , a O ct il i o C n onstruction Utilit W ie h s ole O sa th le P e u T r r b S a l e A i d c r e d v A m ic d i e m n s i W s i n ( t e a i r s x a s t c t t r e i e a v p e M t d i t , o i s a S n p n u ) o a p g s p a e o l m r s t e e a n r n v t i d o c a f e n s C d o E m n p te a r n p ie ri s s es 0
www.orangecyberdefense.com

38 Security Navigator 2025
VERIS Actors, Actions, Assets by Industry
Actors
100% Partner
90%
Other
80%
70%
Internal
60%
50% External
40%
30%
20%
10%
0%
Actions
100% Unknown
90%
Social
80%
Physical
70%
Other
60%
Misuse
50%
Malware
40%
30% Hacking
20% Error
10% Environ-
0% ment
Assets
100% Server
90%
People
80%
Other
70%
Network
60%
Multiple
50%
40% Media
30% End user
device
20%
Cloud
10%
Account
0%
A a c W A n c a d d o s m m F te o i m n o M i o s d g t d r S n a a e t t t . i r i o v v a n e i n c d a e n s R d e S m A A u r . g t p S s r p , e i c o F E r u i r v n s t l i t , h t c u e i e n r r s e t g a , i a F n n o m d re e H s n t u t r , n y a t , i n n d g Recreation Cons E tr d u u c c ti a o t n ional F S i H n e a r e v n a i c l c t e e h s a C n a d re In a s n u d r a S n o c c e ial Ass M is g ta n n t. c o e f C In o f m or p m an a i t e io s n a. Enterprise M s anufac O t M u il r i a n in n in g d g ( G , e Q a xc u s e a E p r x r t y t P r in a u c g O b t , . t i o h A n e d r P m S ro i e n f a r e i n v s s i t d c s r a i e T o t s e n i o c a n h l, ) n S ic c R a P i e e l u a n S b l t e l i E i fi r c v s c i A t , c a d e t m e s a in n is d t R ra e t n io t n al and Le T a ra s n in s g po R rt e a t t a io il n T r a a n d d e Warehousing Utilit W ie h s olesale Trade
VERIS Actor, Finance and Insurance also sees primarily external incidents
that affect servers and accounts, with hacking and social
Action, and Asset Analysis
engineering as predominant actions.
The VERIS framework provides clarity Public Administration’s external attack pattern also involves
on threat origins, actions, and asset impacts. hacking, and impacts end-user devices. Though Misuse is also
a common cause for recorded incidents.
In Manufacturing, incidents are largely internal (62.48%),
with misuse actions commonly impacting end-user devices In Construction, internal incidents involving misuse and
and servers. Professional Services faces a different profile, malware dominate, with incidents largely affecting end-user
with 52.77% of incidents initiated by external actors primarily devices.
through hacking, impacting both end-user devices and servers.
We report a high rate of error-related incidents for our Retail
Healthcare encounters a similar external focus, with 52.62% of clients, largely impacting end-user devices.
incidents driven by external actors. Malware tactics and misuse
are common, while incidents largely impact end-user devices
and networked systems.
© Orange Cyberdefense 2024/2025

Key Data of the Year: Industry Comparisons
16,000 14,863 45
14,255
14,000 40
35
12,000
30
10,000
25
8,000
20
5,426
6,000 4,866
15
4,000
10
1,991
1,368 2,000 336 225 564 613 45 5 1 5
A d mi n P 0 i u s b tr l A a ic a t c i n o c d n o m F o m o o d M d S i a n e t i i n r o v g n a ic , n Q e d s u G a a rr s y e i n x g tr , a O c i t l i o n Utiliti es Ma n ufact uri n g C o nstr ucti o n Ret a F i i l n T a r n a c d e e a n d I ns u E r d a u n c c a e ti o nal P S r e o r f v e i n c s d e s i s t o e n c a h l n , S ic c a i l e s n e ti r fi v R c R ic e e e n a s t l a E l s a t n a d te L a e n a d s i n g I nf or mati o H n e S a o l c t h ia C l A a s r e s i a s n t a d n c e 0
a
VOC Metrics Our data on clients in Educational Services is also limited.
Here we record the lowest findings-per-asset ratio at 1.82, with
Findings Per Asset, Vulnerability critical vulnerabilities addressed within about eight days.
Score, Max and Average Vulnerability Age Finance has a findings rate of 10.03 per asset, but with critical
VOC metrics shed light on each industry’s vulnerability vulnerabilities averaging 136 days before resolution.
management practices, tracking findings per asset and the
Public Administration has the highest findings-per-asset rate
persistence of unresolved vulnerabilities.
at 40.64, with critical vulnerabilities persisting for around 315
Manufacturing exhibits a high findings-per-asset rate at 24.15, days.
with critical vulnerabilities remaining open for an average of 204
Construction has a moderate findings rate of 15.88, but critical
days and a maximum age of 721 days. Clients in Professional
issues last around 120 days on average.
Services record a lower findings-per-asset ratio of 9.34, with
critical vulnerabilities lasting around 91 days on average. Retail’s findings-per-asset rate of 19.24 reflects a steady
vulnerability level, and the sector records a maximum critical
There are very few clients in Healthcare within our dataset, but
vulnerability age of 228 days.
we record a similar persistence in vulnerabilities, averaging 20
findings per asset, with critical issues remaining unresolved for
approximately 217 days.
tessA
rep
sgnidniF
SSVC
fo muS
39
Findings per Asset by Industry
Average Unique Findings per Unique Asset
Findings per asset Avg. Finding per Asset Avg. Sum of CVSS
Age of Findings by Industry
Average and Max. Age of Unique Findings for Different Verticals (Ordered by Average)
Avg. finding age Max. finding age
4,000
3,500
3,000
2,500
2,000
1,500
1,000
500
0
A a c n c d o m F o m o o d d S a e ti r o v n ic es I nf or ma R ti e o a n l Est at a e n , d R P e L u n e b t a l a i s c l i n A g d mi nistr ati o H n e S a o l c t h ia C l A a s r e s i a s n t a d n c e Utiliti es Ret ail Tr a d e Fi na n I c M n e s i n u a i n r n a d g a n , n c Q d e u G a a rr s y E i n x g tr , a O c i t l i o M n a n uf P a r c o t f u e n r s i d n s i g T o e n c a h l, n S ic c a i e l n S t e i fi rv c i , c es C o nstr u E c d t u i o c n ati o nal S ervic es
a
www.orangecyberdefense.com

40 Security Navigator 2025
Industry Scorecard
Retail and Trade
Cy-X Victim ranking (Avg: 200) Threat Detection: Mean time to resolve (Avg: 65h)
| 1   |     |     | 20  | 1   |     |     | 16  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | 166 |     |     |     |     | 36h |     |
Cy-X Victim delta (Avg: +19%) Threat Detection: Coverage (Avg: 37.5%)
| 1   |     |     | 20  | 1   |     |     | 8   |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | +6% |     |     |     | 35% |     |
VOC: Findings per asset (Avg: 22.1 findings) Threat Detection: True positives
| 1   |      |     | 13  | 0   |       |     | 100% |
| --- | ---- | --- | --- | --- | ----- | --- | ---- |
|     | 19.2 |     |     |     | 24.3% |     |      |
total no. of
ranking vs.
VOC: Total Vulnerability Score Ranking: higher is 'better'! other verticals verticals
compared
| 1   |     |     | 13  | 1                     |     |     | 13  |
| --- | --- | --- | --- | --------------------- | --- | --- | --- |
|     | 6   |     |     | value of the vertical |     | 34% |     |
VOC: Finding age by severity (in days)
| Low      |        |         |     |     |         | 428 |     |
| -------- | ------ | ------- | --- | --- | ------- | --- | --- |
| Medium   |        |         |     |     | 335     |     |     |
| High     |        |         | 238 |     |         |     |     |
| Critical |        |         | 229 |     |         |     |     |
| 0        | 50 100 | 150 200 | 250 | 300 | 350 400 | 450 |     |
Threat Detection: Threat Actor
| Internal | External Other | Partner |     |     |         |      |     |
| -------- | -------------- | ------- | --- | --- | ------- | ---- | --- |
| 0% 10%   | 20% 30%        | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
Threat Detection: Threat Action
Misuse Hacking Malware Social Error Other Physical Environment
| 0% 10% | 20% 30% | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | ------- | --- | --- | ------- | ---- | --- |
Threat Detection: Impacted Asset
End user device Server Other Account Network Multiple Media People Cloud
| 0% 10% | 20% 30% | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | ------- | --- | --- | ------- | ---- | --- |
Summary
The Retail Trade industry ranks 9th in terms of cyber extortion victims, with incidents
rising by 6% over the past year. Motor Vehicle Dealers and Food Retailers are frequently
targeted. CyberSOC metrics indicate a relatively fast MTTR (about 35 hours) and a
median coverage score of 35.1%. The true positive ratio is 24.34% to 75.66%. VOC
metrics show a relatively low findings-per-asset rate, though critical vulnerabilities often
remain unresolved for over 228 days.
© Orange Cyberdefense 2024/2025

|     |     |     |     |     |     | Industry Scorecards | 41  |
| --- | --- | --- | --- | --- | --- | ------------------- | --- |
Industry Scorecard
Construction
Cy-X Victim ranking (Avg: 200) Threat Detection: Mean time to resolve (Avg: 65h)
| 1   |     |     | 20  | 1   |     |     | 16  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 232 |     |     |     | 95h |     |     |     |
Cy-X Victim delta (Avg: +19%) Threat Detection: Coverage (Avg: 37.5%)
| 1   |      |     | 20  | 1   |     |       | 8   |
| --- | ---- | --- | --- | --- | --- | ----- | --- |
|     | +25% |     |     |     |     | 45.7% |     |
VOC: Findings per asset (Avg: 22.1 findings) Threat Detection: True positives
| 1   |     |      | 13  | 0     |     |     | 100% |
| --- | --- | ---- | --- | ----- | --- | --- | ---- |
|     |     | 15.9 |     | 14.5% |     |     |      |
total no. of
ranking vs.
VOC: Total Vulnerability Score Ranking: higher is 'better'! other verticals verticals
compared
|     |     |     |     | 1                     |     |     | 13  |
| --- | --- | --- | --- | --------------------- | --- | --- | --- |
| 1   |     |     | 13  |                       |     |     |     |
|     | 7   |     |     | value of the vertical |     | 34% |     |
VOC: Finding age by severity (in days)
| Low      |        | 148     |     |     |         |     |     |
| -------- | ------ | ------- | --- | --- | ------- | --- | --- |
| Medium   | 122    |         |     |     |         |     |     |
| High     | 91     |         |     |     |         |     |     |
| Critical | 120    |         |     |     |         |     |     |
| 0        | 50 100 | 150 200 | 250 | 300 | 350 400 | 450 |     |
Threat Detection: Threat Actor
| Internal | External Other | Partner |     |     |         |      |     |
| -------- | -------------- | ------- | --- | --- | ------- | ---- | --- |
| 0% 10%   | 20% 30%        | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
Threat Detection: Threat Action
Misuse Hacking Malware Social Error Other Physical Environment
| 0% 10% | 20% 30% | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | ------- | --- | --- | ------- | ---- | --- |
Threat Detection: Impacted Asset
End user device Server Other Account Network Multiple Media People Cloud
| 0% 10% | 20% 30% | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | ------- | --- | --- | ------- | ---- | --- |
Summary
In Construction, a 25% increase in cyber extortion incidents primarily
impacts Specialty Trade Contractors, Construction of Buildings, and
Civil Engineering. Our CyberSOCs report that misuse and malware
frequently affect end-user devices. Our metrics reveal a high coverage
score of 45.71% and an MTTR of 94.7 hours, with a true positive rate of
14.46%. VOC metrics show moderate findings per asset at 15.88, with
critical vulnerabilities persisting for around 120 days.
www.orangecyberdefense.com

42 Security Navigator 2025
Industry Scorecard
Manufacturing
Cy-X Victim ranking (Avg: 200) Threat Detection: Mean time to resolve (Avg: 65h)
| 1   |     |     | 20  | 1   |     |     | 16  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 920 |     |     |     | 97h |     |     |     |
Cy-X Victim delta (Avg: +19%) Threat Detection: Coverage (Avg: 37.5%)
| 1   |      |     | 20  | 1   |       |     | 8   |
| --- | ---- | --- | --- | --- | ----- | --- | --- |
|     | +25% |     |     |     | 38.5% |     |     |
VOC: Findings per asset (Avg: 22.1 findings) Threat Detection: True positives
| 1   |      |     | 13  | 0   |       |     | 100% |
| --- | ---- | --- | --- | --- | ----- | --- | ---- |
|     | 24.2 |     |     |     | 21.0% |     |      |
total no. of
ranking vs.
VOC: Total Vulnerability Score Ranking: higher is 'better'! other verticals verticals
compared
| 1   |     |     | 13  | 1                     |     |     | 13  |
| --- | --- | --- | --- | --------------------- | --- | --- | --- |
|     | 5   |     |     | value of the vertical |     | 34% |     |
VOC: Finding age by severity (in days)
| Low    |     |     | 244 |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- |
| Medium |     | 200 |     |     |     |     |     |
| High   |     | 199 |     |     |     |     |     |
205
Critical
| 0   | 50 100 | 150 200 | 250 | 300 | 350 400 | 450 |     |
| --- | ------ | ------- | --- | --- | ------- | --- | --- |
Threat Detection: Threat Actor
| Internal | External Other | Partner |     |     |         |      |     |
| -------- | -------------- | ------- | --- | --- | ------- | ---- | --- |
| 0% 10%   | 20% 30%        | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
Threat Detection: Threat Action
Misuse Hacking Malware Social Error Other Physical Environment
| 0% 10% | 20% 30% | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | ------- | --- | --- | ------- | ---- | --- |
Threat Detection: Impacted Asset
End user device Server Other Account Network Multiple Media People Cloud
| 0% 10% | 20% 30% | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | ------- | --- | --- | ------- | ---- | --- |
Summary
In the Manufacturing industry, cyber extortion and OT-specific attacks have made this
sector the most impacted by cyber threats, with a 25% increase in Cy-X incidents. Key
sub-sectors like Fabricated Metal Product and Machinery Manufacturing are especially
impacted. Manufacturing’s reliance on OT systems makes it highly vulnerable to
productivity loss, data encryption, and control manipulation, with both state actors and
hacktivists posing significant threats. CyberSOC metrics indicate that this industry has
a high mean time to resolve (MTTR) at 97 hours, ranking as the second slowest across
sectors. Coverage stands at 36.77%, near the median, with internal actors contributing
to 62.48% of CyberSOC incidents. VOC metrics reveal a higher-than-average findings
rate per asset, at 24.15, with critical vulnerabilities remaining open for over 204 days
on average.
© Orange Cyberdefense 2024/2025

|     |     |     |     |     |     | IInndduussttrryy  SSccoorreeccaarrddss | 43  |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | --- |
Industry Scorecard
Professional, Scientific, and
Technical Services
Cy-X Victim ranking (Avg: 200) Threat Detection: Mean time to resolve (Avg: 65h)
| 1   |     |     | 20  | 1   |     |     | 16  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 758 |     |     |     |     | 49h |     |     |
Cy-X Victim delta (Avg: +19%) Threat Detection: Coverage (Avg: 37.5%)
| 1   |      |     | 20  | 1   |     |       | 8   |
| --- | ---- | --- | --- | --- | --- | ----- | --- |
|     | +20% |     |     |     |     | 32.0% |     |
VOC: Findings per asset (Avg: 22.1 findings) Threat Detection: True positives
| 1   |     |      | 13  | 0     |     |     | 100% |
| --- | --- | ---- | --- | ----- | --- | --- | ---- |
|     |     | 9.34 |     | 16.5% |     |     |      |
total no. of
ranking vs.
VOC: Total Vulnerability Score Ranking: higher is 'better'! other verticals verticals
compared
|     |     |     |     | 1                     |     |     | 13  |
| --- | --- | --- | --- | --------------------- | --- | --- | --- |
| 1   |     |     | 13  |                       |     |     |     |
|     |     | 11  |     | value of the vertical |     | 34% |     |
VOC: Finding age by severity (in days)
| Low      |        | 162     |     |     |         |     |     |
| -------- | ------ | ------- | --- | --- | ------- | --- | --- |
| Medium   | 128    |         |     |     |         |     |     |
| High     | 83     |         |     |     |         |     |     |
| Critical | 92     |         |     |     |         |     |     |
| 0        | 50 100 | 150 200 | 250 | 300 | 350 400 | 450 |     |
Threat Detection: Threat Actor
| Internal | External Other | Partner |     |     |         |      |     |
| -------- | -------------- | ------- | --- | --- | ------- | ---- | --- |
| 0% 10%   | 20% 30%        | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
Threat Detection: Threat Action
Misuse Hacking Malware Social Error Other Physical Environment
| 0% 10% | 20% 30% | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | ------- | --- | --- | ------- | ---- | --- |
Threat Detection: Impacted Asset
End user device Server Other Account Network Multiple Media People Cloud
| 0% 10% | 20% 30% | 40% 50% | 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | ------- | --- | --- | ------- | ---- | --- |
Summary
For the Professional, Scientific, and Technical Services sector, cyber extortion
incidents have increased by 20%, particularly impacting sub-sectors such as
Legal and Accounting Services. High vulnerability ages and low coverage scores
suggest there is room for improvement for businesses in this industry. Hacking
and misuse are prevalent threats, often impacting end-user devices and servers.
CyberSOC metrics show an MTTR of 49 hours, the industry median, yet coverage
is low at 32.04%. Most incidents involve external actors, with hacking being a
primary action – this pattern being somewhat unusual in this year’s data. VOC
metrics show a lower findings-per-asset rate at 9.34, though critical issues can
linger around 91 days before remediation
www.orangecyberdefense.com

44 Security Navigator 2025
Industry Scorecard
Health Care and Social Assistance
Cy-X Victim ranking (Avg: 200) Threat Detection: Mean time to resolve (Avg: 65h)
| 1   |     |     | 20  | 1   |     |     | 16  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | 282 |     |     |     | 50h |     |     |
Cy-X Victim delta (Avg: +19%) Threat Detection: Coverage (Avg: 37.5%)
| 1    |     |     | 20  | 1   |     |     | 8   |
| ---- | --- | --- | --- | --- | --- | --- | --- |
| +50% |     |     |     |     |     | 29% |     |
VOC: Findings per asset (Avg: 22.1 findings) Threat Detection: True positives
| 1   |     |     | 13  | 0     |     |     | 100% |
| --- | --- | --- | --- | ----- | --- | --- | ---- |
|     | 20  |     |     | 16.5% |     |     |      |
total no. of
ranking vs.
VOC: Total Vulnerability Score Ranking: higher is 'better'! other verticals verticals
compared
| 1   |     |     | 13  | 1                     |     |     | 13  |
| --- | --- | --- | --- | --------------------- | --- | --- | --- |
|     |     |     | 13  | value of the vertical |     | 34% |     |
VOC: Finding age by severity (in days)
444
Low
| Medium |        |     |         |     | 362     |     |     |
| ------ | ------ | --- | ------- | --- | ------- | --- | --- |
| High   |        |     | 217     |     |         |     |     |
| 0      | 50 100 | 150 | 200 250 | 300 | 350 400 | 450 |     |
Threat Detection: Threat Actor
| Internal | External Other | Partner |         |     |         |      |     |
| -------- | -------------- | ------- | ------- | --- | ------- | ---- | --- |
| 0% 10%   | 20% 30%        | 40%     | 50% 60% | 70% | 80% 90% | 100% |     |
Threat Detection: Threat Action
Misuse Hacking Malware Social Error Other Physical Environment
| 0% 10% | 20% 30% | 40% | 50% 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | --- | ------- | --- | ------- | ---- | --- |
Threat Detection: Impacted Asset
End user device Server Other Account Network Multiple Media People Cloud
| 0% 10% | 20% 30% | 40% | 50% 60% | 70% | 80% 90% | 100% |     |
| ------ | ------- | --- | ------- | --- | ------- | ---- | --- |
Summary
Health Care and Social Assistance ranks as the fourth most impacted industry, with
a worrisome 50% rise in cyber extortion incidents. Sub-sectors such as Ambulatory
Health Care and Hospitals are now actively targeted as previous “moral” restraints
by attackers have eroded. Malware attacks, typically driven by external actors, are
common, which is somewhat unusual in this year’s client data. Persistent vulnerabilities
remain an issue, with critical findings often aging for over 217 days. CyberSOC metrics
indicate an MTTR of 50 hours, slightly above the median, with a low coverage score of
29.04% and a true positive rate of 16.45%. VOC metrics show an average of 20 findings
per asset, somewhat below the industry average of 22.43, although this is derived from
a small sample of clients.
© Orange Cyberdefense 2024/2025

|     |     |     |     |     |     |     |     | Industry Scorecards | 45  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
Industry Scorecard
Educational Services
Cy-X Victim ranking (Avg: 200) VOC: Findings per asset (Avg: 22.1 findings)
| 1                             |     |     |      | 20  | 1                              |     |     |     | 13  |
| ----------------------------- | --- | --- | ---- | --- | ------------------------------ | --- | --- | --- | --- |
|                               |     | 178 |      |     |                                |     |     |     | 1.8 |
| Cy-X Victim delta (Avg: +19%) |     |     |      |     | VOC: Total Vulnerability Score |     |     |     |     |
| 1                             |     |     |      | 20  | 1                              |     |     |     | 13  |
|                               |     |     | -25% |     |                                |     |     | 9   |     |
total no. of
ranking vs.
Threat Detection: True positives Ranking: higher is 'better'! other verticals verticals
compared
|     |       |     |     |      | 1                     |     |     |     | 13  |
| --- | ----- | --- | --- | ---- | --------------------- | --- | --- | --- | --- |
| 0   |       |     |     | 100% |                       |     |     |     |     |
|     | 31.0% |     |     |      | value of the vertical |     |     | 34% |     |
Threat Detection: Threat Actor
| Internal | External | Other | Partner |     |     |     |     |      |     |
| -------- | -------- | ----- | ------- | --- | --- | --- | --- | ---- | --- |
| 0% 10%   | 20%      | 30%   | 40% 50% | 60% | 70% | 80% | 90% | 100% |     |
Threat Detection: Threat Action
Misuse Hacking Malware Social Error Other Physical Environment
| 0% 10% | 20% | 30% | 40% 50% | 60% | 70% | 80% | 90% | 100% |     |
| ------ | --- | --- | ------- | --- | --- | --- | --- | ---- | --- |
Threat Detection: Impacted Asset
End user device Server Other Account Network Multiple Media People Cloud
| 0% 10% | 20% | 30% | 40% 50% | 60% | 70% | 80% | 90% | 100% |     |
| ------ | --- | --- | ------- | --- | --- | --- | --- | ---- | --- |
VOC: Finding age by severity (in days)
Low 9
| Medium 29 |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
High 12
Critical 8
| 0   | 50  | 100 | 150 200 | 250 | 300 | 350 | 400 | 450 |     |
| --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Summary
The Educational Services sector, ranking 8th most impacted, saw a 25% decrease in
cyber extortion victims, with elementary and secondary schools being heavily impacted.
CyberSOC clients in this sector have a relatively high true positive rate, demonstrating
accuracy in threat detection. The CSOC metrics reveal a high true positive rate at 30.99%,
though coverage remains low. VOC metrics show relatively few findings per asset,
averaging 1.82, and critical vulnerabilities are resolved within about 8 days (although these
metrics are derived from a small sample).
This year we highlight the Education sector as a target of modern hacktivist activity.
Hacktivists attack this sector due to its public significance and symbolic value, with goals
often focused on disrupting societal stability. Educational institutions are among the
essential service sectors targeted by a pro-Russian hacktivist group, with attacks timed
to coincide with geopolitical events and driven by the desire to influence public opinion or
cause societal disruptions. These attacks are typically ideologically motivated, aiming not
only to disrupt educational systems but also to manipulate public perception by targeting
institutions that influence societal narratives.
www.orangecyberdefense.com

46 Security Navigator 2025
Industry Scorecard
Finance and Insurance
Cy-X Victim ranking (Avg: 200) Threat Detection: Mean time to resolve (Avg: 65h)
| 1   |     |     |     | 20  | 1   |     | 16  |
| --- | --- | --- | --- | --- | --- | --- | --- |
|     | 196 |     |     |     |     | 56h |     |
Cy-X Victim delta (Avg: +19%) Threat Detection: Coverage (Avg: 37.5%)
| 1   |     |     |      | 20  | 1   |     | 8   |
| --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     |     | -27% |     | 56% |     |     |
VOC: Findings per asset (Avg: 22.1 findings) Threat Detection: True positives
| 1   |     |     |     | 13  | 0    |     | 100% |
| --- | --- | --- | --- | --- | ---- | --- | ---- |
|     |     | 10  |     |     | 8.3% |     |      |
total no. of
ranking vs.
VOC: Total Vulnerability Score Ranking: higher is 'better'! other verticals verticals
compared
| 1   |     |     |     | 13  | 1                     |     | 13  |
| --- | --- | --- | --- | --- | --------------------- | --- | --- |
|     |     | 8   |     |     | value of the vertical | 34% |     |
VOC: Finding age by severity (in days)
| Low      |        |     |     | 275 |         |         |     |
| -------- | ------ | --- | --- | --- | ------- | ------- | --- |
| Medium   |        |     |     |     | 301     |         |     |
| High     |        |     | 189 |     |         |         |     |
| Critical |        | 136 |     |     |         |         |     |
| 0        | 50 100 | 150 | 200 | 250 | 300 350 | 400 450 |     |
Threat Detection: Threat Actor
| Internal | External Other | Partner |     |     |         |          |     |
| -------- | -------------- | ------- | --- | --- | ------- | -------- | --- |
| 0% 10%   | 20%            | 30% 40% | 50% | 60% | 70% 80% | 90% 100% |     |
Threat Detection: Threat Action
Misuse Hacking Malware Social Error Other Physical Environment
| 0% 10% | 20% | 30% 40% | 50% | 60% | 70% 80% | 90% 100% |     |
| ------ | --- | ------- | --- | --- | ------- | -------- | --- |
Threat Detection: Impacted Asset
End user device Server Other Account Network Multiple Media People Cloud
| 0% 10% | 20% | 30% 40% | 50% | 60% | 70% 80% | 90% 100% |     |
| ------ | --- | ------- | --- | --- | ------- | -------- | --- |
Summary
In Finance and Insurance, Cy-X incident volumes have declined by 27%, but we still
recorded 196 victims this year, with a concentration in Credit Intermediation and
Securities. External actors are responsible for most reported CyberSOC incidents,
primarily targeting servers and accounts. We report a high proportion of hacking and
social engineering incidents, which is unusual to this section. The sector’s CSOC
metrics show the highest coverage score at 55.87% and an MTTR of 56 hours, with a
true positive ratio of 8.3%. VOC metrics reveal a low findings-per-asset rate at 10.03,
though critical vulnerabilities may persist unresolved for an average of 136 days.
© Orange Cyberdefense 2024/2025

|     |     |     |     |     |     |     | IInndduussttrryy  SSccoorreeccaarrddss | 47  |
| --- | --- | --- | --- | --- | --- | --- | -------------------------------------- | --- |
Industry Scorecard
Public Administration
Cy-X Victim ranking (Avg: 200) Threat Detection: Mean time to resolve (Avg: 65h)
| 1   |     |     |     | 20 1 |     |     |     | 16  |
| --- | --- | --- | --- | ---- | --- | --- | --- | --- |
|     |     | 141 |     |      |     |     | 38h |     |
Cy-X Victim delta (Avg: +19%) Threat Detection: Coverage (Avg: 37.5%)
| 1   |      |     |     | 20 1 |     |     |     | 8   |
| --- | ---- | --- | --- | ---- | --- | --- | --- | --- |
|     | +31% |     |     |      |     | 29% |     |     |
VOC: Findings per asset (Avg: 22.1 findings) Threat Detection: True positives
| 1    |     |     |     | 13 0 |       |     |     | 100% |
| ---- | --- | --- | --- | ---- | ----- | --- | --- | ---- |
| 40.6 |     |     |     |      | 20.2% |     |     |      |
total no. of
ranking vs.
VOC: Total Vulnerability Score Ranking: higher is 'better'! other verticals verticals
compared
|     |     |     |     | 1   |                       |     |     | 13  |
| --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
| 1   |     |     |     | 13  |                       |     |     |     |
| 1   |     |     |     |     | value of the vertical |     | 34% |     |
VOC: Finding age by severity (in days)
| Low      |     |     |     |     |     | 637 |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Medium   |     |     |     |     | 516 |     |     |     |
| High     |     |     | 330 |     |     |     |     |     |
| Critical |     |     | 316 |     |     |     |     |     |
| 0        | 100 | 200 | 300 | 400 | 500 | 600 | 700 |     |
Threat Detection: Threat Actor
| Internal | External Other | Partner |     |     |         |     |      |     |
| -------- | -------------- | ------- | --- | --- | ------- | --- | ---- | --- |
| 0% 10%   | 20%            | 30% 40% | 50% | 60% | 70% 80% | 90% | 100% |     |
Threat Detection: Threat Action
Misuse Hacking Malware Social Error Other Physical Environment
| 0% 10% | 20% | 30% 40% | 50% | 60% | 70% 80% | 90% | 100% |     |
| ------ | --- | ------- | --- | --- | ------- | --- | ---- | --- |
Threat Detection: Impacted Asset
End user device Server Other Account Network Multiple Media People Cloud
| 0% 10% | 20% | 30% 40% | 50% | 60% | 70% 80% | 90% | 100% |     |
| ------ | --- | ------- | --- | --- | ------- | --- | ---- | --- |
Summary
Public Administration experienced a 31% increase in Cy-X incidents, particularly
in governmental support and justice sectors. Hacktivist activity, often coinciding
with elections or geopolitical events, poses a significant risk, with attacks typically
linked to hacking and misuse by external actors. The sector’s CSOC metrics are
notable for an average MTTR of 38 hours and a high coverage score of 41.43%,
with incidents stemming largely from external sources. VOC metrics indicate a
high findings-per-asset score of 40.64, with critical vulnerabilities lingering for
an average of 315 days. The Navigator underscores the importance of fortified
cybersecurity frameworks, particularly to secure election systems and essential
government services, given the prevalence of legacy vulnerabilities.
www.orangecyberdefense.com

48 Security Navigator 2025
Region perspective
Cyber Extortion (Cy-X) Threat Detection
The Cy-X landscape reflects diverse regional vulnerabilities, CyberSOC data from Orange Cyberdefense’s Security
with North America, led by the United States, emerging as the Operations Centers provides insights into threat detection and
most impacted region globally. The USA alone accounted for incident response across regions. From our clients in North
2,154 of the 2,387 Cy-X cases reported across North America, America, CyberSOC metrics revealed a high false-positive rate
marking a 25% increase from the previous year. This high of 80.53% in the USA, with most incidents driven by internal
volume underscores the USA’s attractiveness as a target for misuse rather than external attacks. This is derived from a very
financially motivated cyber extortion, particularly within high- small sample, however, and should not be generalized.
value sectors that rely heavily on digital infrastructure.
In Europe, CyberSOC data reveals efficient incident response
In Europe, Cy-X incidents were widespread, with Germany for our clients in Germany, demonstrated by its swift Mean
experiencing 19% of regional cases, positioning it as a Time to Resolve (MTTR) of 50.5 hours.
significant target. This prominence aligns with Germany’s
China’s CyberSOC metrics in APAC showed a balanced false-
industrial and economic significance within Europe, which has
positive to true-positive ratio, with most incidents originating
made it a frequent target for cybercriminals seeking lucrative
internally and impacting end-user devices. The internal nature
payoffs. Cy-X incidents in Europe highlighted the extensive
of these threats points to the importance of user access
integration of IT across industries, further exacerbating the
controls and monitoring for insider threats within Chinese
spread and impact of cyber extortion events in high-risk
organizations.
sectors.
Across the APAC region, Cy-X impacts were uneven. Japan
Operational Technology (OT)
ranked as the 13th most affected country globally, probably
driven by both industrial vulnerabilities and high levels of Operational Technology (OT) security emerged as a critical
connectivity. In contrast, China showed a lower Cy-X victim. theme, particularly in sectors where IT and OT systems are
South Korea and Singapore also experienced moderate tightly integrated, creating vulnerabilities that adversaries can
levels of Cy-X incidents, with cyber extortion targeting high- exploit. The USA in North America experienced substantial
value manufacturing and industrial sectors, underscoring the OT impacts, with 49% of all OT-targeted attacks globally. The
importance of IT and OT protections in the region. manufacturing and transportation sectors were particularly
affected, as IT incidents frequently cascaded into OT
Hacktivism environments, leading to production downtimes and other
operational interruptions. This spillover effect underscores
Hacktivism incidents presented a different geographic focus, the need for comprehensive OT security protocols to protect
largely driven by political motivations and regional tensions. critical infrastructure from the ripple effects of ransomware and
Europe bore the brunt of hacktivist attacks, with 96% of other IT-originating incidents.
observed pro-Russian hacktivism cases targeting European
In Europe, Germany was significantly impacted, accounting for
countries. These attacks primarily impacted Ukraine, Czech
11% of all OT-targeted incidents. The country’s manufacturing
Republic, Spain, Poland, and Italy, reflecting the influence of
and utility sectors were key targets, with attackers exploiting
geopolitical tensions. Hacktivists in Europe primarily employed
IT-OT interdependencies to disrupt operations. Sophisticated
disruptive tactics, such as distributed denial-of-service (DDoS)
OT attacks used complex tactics to manipulate physical
attacks and website defacements, to publicize their causes and
processes, which caused substantial operational downtime.
destabilize critical services.
This level of targeting in Germany reflects the high value of its
In APAC, Japan was notably impacted, recording 71 hacktivist industrial sectors to both economically motivated and state-
attacks, many linked to pro-Russian groups. This significant backed threat actors.
focus on Japan aligns with its strategic importance in global
geopolitics and its robust digital infrastructure, which provides
ample targets for hacktivist campaigns.
The Middle East saw intensified hacktivist activity, particularly
Summary
in conflict areas which have led to reciprocal cyber offensives.
Pro-Hamas hacktivists targeted Israeli networks, launching
This thematic summary provides a comparative
DDoS attacks and exploiting social engineering to compromise
overview of how Cy-X, hacktivism, CyberSOC
personal data. Lebanon also reported hacktivist incidents,
observations, and OT security challenges
with activity allegedly linked to Iranian groups, underscoring
manifest differently across regions, shaped
the geopolitical complexities of hacktivism in the Middle
by unique geopolitical, industrial, and
East. These politically driven cyber actions signal the region’s
infrastructural factors. The findings underscore
heightened vulnerability to hacktivist campaigns amidst
the importance of tailored cybersecurity
ongoing conflict.
strategies that address both the direct and
spillover effects of cyber incidents, particularly
within critical infrastructure and high-risk
sectors.
© Orange Cyberdefense 2024/2025

RReeggiioonn SSccoorreeccaarrddss 49
Region Scorecard
Europe Region
Cy-X region ranking Cy-X victim delta
Europe had the second highest number In this region we saw an increase in the
of Cy-X victims with number of victim organizations of
745 victims + 18%
Most affected countries
Top 5 impacted countries were
▪ Italy (19%)
▪ Germany (19%)
▪ France (16%)
▪ Spain (13%)
▪ Belgium (8%).
CyberSOC Ranking ▪ For clients in this region the most common VERIS
▪ The Mean Time To Resolve (MTTR ) for clients in this Action classifications were Hacking (30.10%) and
region was 65 hours. Misuse (28.08%), followed by Malware (15.89%) and
▪ The countries with the lowest Mean Time To Social (12.94%).
Resolve (MTTR) were Austria (37.4 hours), Norway
Hacktivism Ranking
(37.7 hours), Germany (50.5 hours), and the United
▪ Our case study on one of the most active pro-
Kingdom (50.7 hours).
Russian hacktivist groups shows that 96% of all
▪ The VERIS Actor category for clients in this region is
attacks targeted victims in Europe.
nearly split down the middle for Internal (47.32%) and
▪ The top 5 countries attacked were: Ukraine (11%),
External (47.20%).
Czech Republic (9%), Spain (9%), Poland (8%), Italy
▪ The most impacted asset class for clients in this
(7%).
region is End User Devices (45.5%) followed by
Server (22.19%) and Account (12.39%).
Summary
A High Cy-X and Hacktivism Target
Europe ranked as the second most impacted region by Cy-X globally, experiencing 745 victim organizations,
an 18% increase over the previous year. Among European countries, Italy and Germany led the way
with 19% of Cy-X cases each, followed by France (16%), Spain (13%), and Belgium (8%). This escalation
in Cy-X incidents aligns with Europe’s prominence as a hub for business and technology, making it an
attractive target for financially motivated cyber extortion. Moreover, hacktivism was particularly prominent
in Europe, with 96% of attacks by the pro-Russian group we studied targeting European entities. Attacks
primarily impacted Ukraine (11%), Czech Republic (9%), Spain (9%), Poland (8%), and Italy (7%). CyberSOC
data reveals that the primary threat actions were hacking and misuse, both heavily impacting end-user
devices. The concentration of both Cy-X and hacktivism in Europe emphasizes the region’s complex threat
environment, especially as politically motivated groups escalate attacks amidst geopolitical tensions.
Industrial economies in Europe also feature as vulnerable to OT attacks. Germany recorded the second-
highest number of OT-targeted cyber incidents in the world, accounting for 11% of the recorded attacks.
Europe’s industrial and manufacturing sectors, which heavily rely on OT systems, are notably targets for
hacktivism, Cyber Extortion, and targeted attacks on OT.
www.orangecyberdefense.com

50 Security Navigator 2025
Region Scorecard
Nordics Region
Cy-X region ranking Cy-X victim delta
The Nordics region is the 9th most impacted, In this region we saw an increase in the
with a victim count of number of victim organizations of
65 victims + 38%
Most affected countries
Top impacted countries were
▪ Sweden (41%)
▪ Denmark (34%)
▪ Norway (20%)
▪ Finland (5%).
CyberSOC Ranking ▪ The most impacted assets by VERIS for clients in this
▪ Norwegian clients (37.7 hours) have the shortest Mean region were End user device (49.24%), followed by
Servers (22.67%), Account (16.70%), multiple assets
Time To Resolve (MTTR) in the Nordics region, followed
(6.63%), and Network (2.78%).
by Sweden (69.5 hours) and Denmark (209 hours). The
MTTR for our clients in Sweden is just longer than the
Hacktivism Ranking
European median (65 hours).
▪ The primary VERIS Actor source of attacks for
▪ The Nordic countries were notable in our data on one of
the most active pro-Russian hacktivist groups.
confirmed incidents at clients in this region is External
(52.44%) sources, but Internal (43.77%) sources are also ▪ The distribution across Nordic victims was: Finland
contributing substantially. (36%), Sweden (29%), Denmark (22%), Norway (12%)
▪ For clients in the Nordics cluster VERIS Actions Misuse
and Iceland (1%).
(36.16%) and Hacking (32.72%) are the most prominent,
followed by Social (13.9%) and Malware (11.44%).
Summary
Rapidly Rising Cy-X Incidents with Substantial Hacktivist Activity
In the Nordics, Cy-X activity has grown at a rapid pace, with a 38% increase in victim counts, making it the
fastest-growing region for cyber extortion. Sweden was the hardest hit (41% of regional cases), followed
by Denmark (34%) and Norway (20%). Hacktivism activity was notable in this region as well, with Finland
witnessing a significant share (36%) of observed pro-Russian hacktivist attacks. The Nordics’ cyber
landscape points to a dual need for managing rising extortion incidents while guarding against politicized
attacks that may increasingly target critical infrastructure.
© Orange Cyberdefense 2024/2025

Region Scorecards 51
Region Scorecard
Africa & Middle East
Cy-X region ranking Cy-X region ranking
The African region is 11th most impacted The Middle East is 8th most impacted globally,
globally, with a victim count of with a victim count of
57 (-19%) 79 (+1%)
Most affected countries
▪ Top 5 impacted countries in the Africa region were South Africa (40%), Egypt
(16%), Tunisia (7%), Kenya (5%) and Namibia (5%)
▪ South Africa ranks as 21st most impacted globally
▪ Top 5 impacted countries in the Middle East region were United Arab Emirates
(30%), Turkey (19%), Israel (15%), Saudi Arabia (11%) and Lebanon (8%)
▪ The United Arab Emirates ranks at 19th most impacted globally, ahead of
South Africa
CyberSOC Ranking ▪ Note that South Africa and Morocco’s contribution to
▪ Mean Time To Resolve for incidents for clients in the dataset is small and much more data is required
to make any meaningful deductions.
South Africa is 18 hours.
▪ The VERIS Actor distribution for clients in this region Hacktivism Ranking
is: Internal (54.84%), External (44.42%), Unknown
▪ By collecting data from one of the most active pro-
(0.74%).
Russian hacktivist groups, we found Africa & Middle
▪ For clients in the region the VERIS Action Hacking
East not to be impacted by this specific group.
(32.43%) is the most prominent, followed closely
by Misuse (31.44%), Error (20.30%), and Malware
(12.87%).
▪ Impacted Assets for clients in region are Server
(44.91%) in the lead with End user device (6.55%) and
Network (18.27%) trailing.
Summary
Cy-X Impact Amid Rising Hacktivism in conflict areas
The Africa and Middle East regions, while experiencing relatively low levels of Cy-X activity, revealed complex
dynamics in cyber extortion, hacktivism, and cyber response. The Middle East ranked as the 8th most impacted
globally, with 79 recorded Cy-X incidents, marking a 1% increase in cyber extortion cases. Key affected countries
included the UAE, Turkey, Israel, Saudi Arabia, and Lebanon, with the UAE experiencing the biggest impact
regionally. Africa, however, ranked 11th in Cy-X impact, recording 57 incidents—a 19% decrease from the previous
year. In Africa, South Africa bore the brunt with 40% of Cy-X cases, followed by Egypt and Tunisia.
Hacktivist activity by the groups we monitored in the Middle East has intensified due to escalating regional tensions,
especially amidst the Israel-Hamas conflict in October 2023. This clash spilled into cyberspace, with hacktivist
groups targeting networks across the region. Both sides launched distributed denial-of-service (DDoS) attacks,
defaced websites, and leaked stolen data[28]. Pro-Hamas actors reportedly exploited a fake version of the “RedAlert”
app, harvesting Israeli user data and exposing personal information. Lebanon also faced heightened hacktivism
activity, allegedly supported by Iran, with Israel reporting cyberattacks on its hospitals[30][31].
This landscape highlights the region’s diverse cyber threats, from extortion to hacktivism, reflecting an evolving
cybersecurity challenge amidst geopolitical and domestic unrest.
www.orangecyberdefense.com

52 Security Navigator 2025
Region Scorecard
APAC Region
Cy-X region ranking Cy-X region ranking Cy-X region ranking
The East Asia excluding China region is the South-East Asia ranks as the 5th most China still ranks low as the12th-most
7th most impacted, with a victim count of impacted region, with a victim count of impacted, with a victim count of
80 victims (+6%) 104 victims (-9%) 21 victims (-13%)
Most affected countries
▪ Australia accounts for 22.22% of victims in this region
▪ India (15.25%)
▪ Japan (10.85%)
▪ Indonesia (5.94%)
CyberSOC Ranking Hacktivism Ranking
▪ The Mean Time To Resolve (MTTR) incidents for clients ▪ In our data on one of the most active pro-Russian
from China was 18.45 hours. hacktivist groups, we found the only impacted country
▪ The VERIS Actor distribution for our Chinese clients from this region to be Japan. We registered 71 attacks
is Internal (55.15%), followed by External (43.84%), against Japanese organizations.
Unknown (0.29%), and Partners (0.29%).
▪ The VERIS Action allocation for Chinese clients is
Misuse (33.46%), Error (22.70%), Hacking (21.78%),
Social (12.07%), and Malware (9.19%).
▪ Impacted assets for Chinese clients is End user device
(28.82%), Server (23.06%), Cloud (16.29%), Account
(15.29%), multiple assets (9.02%), and Network (5.26%)
Summary
Mixed impact with East Asia
(excluding China) ranking highly in Cy-X
The Asia-Pacific region exhibited a complex mix of Cy-X and hacktivism impacts, with significant variability within
subregions. East Asia (excluding China) ranked as the 7th most impacted globally for Cy-X, recording 80 cases.
In contrast, Southeast Asia saw a 9% decrease in Cy-X incidents. Across the APAC region, Australia, India,
and Japan were among the most affected countries. Japan also experienced a significant share of hacktivist
activity, with 71 recorded incidents from one pro-Russian group. CyberSOC data on China revealed a heavy
concentration of internal threats, with misuse as the primary action affecting end-user devices. The varied Cy-X
and hacktivism landscape within APAC suggests that the region’s vast economic and technological diversity
demands flexible and localized security strategies. The operational landscape, especially in countries with critical
infrastructure, also faces increased threats to OT systems, which are vulnerable to both direct and spillover
impacts from IT-targeted attacks.
© Orange Cyberdefense 2024/2025

Region Scorecards 53
Region Scorecard
North America Region (US & CA)
Cy-X region ranking Cy-X victim delta
We consider the USA and Canada together The USA and Canada as a region have
as one “Region”, which again ranks as the recorded a victim count increase of
most impacted by Cy-X in the world, with
2,387 victims +25%
Most affected country
The USA is by far the most impacted country in North America with 2154
recorded victims for the period. Despite significantly trailing the US, Canada
on its own ranks 3rd most impacted in the world with 233 victims.
CyberSOC Ranking
Note: The volume of incidents is too low to draw any meaningful
conclusions.
▪ In terms of VERIS Actor the most prominent source of incidents is Internal
(65.17%) compared to External (17.98%), followed by Unknown (14.61%),
and Partners (2.25%).
▪ The VERIS Action allocation for the USA is Misuse (86.67%), Malware
(11.11%), and Unknown (2.22%).
▪ The VERIS Asset allocation for USA has End user assets (83.05%), Server
(15.25%), and multiple assets (1.69%).
Summary
U.S. impacted the most by Cy-X. Canada targeted by Hacktivists
North America, dominated by the U.S., was the most impacted region globally by Cy-X, with 2,387 victim
organizations and a 25% increase in cases. The U.S. recorded 2,154 incidents, making it the top-targeted
country, while Canada ranked third globally with 233 cases. While North America faced limited hacktivist
activity, some notable events were reported in Canada, but no significant hacktivist attacks were recorded
in the U.S. CyberSOC data indicates that end-user devices were frequently impacted.
The USA also saw the highest concentration of OT-targeted attacks globally, accounting for 49% of all
incidents.
North America’s prevalence as a Cy-X target reinforces its position as a top target for financially motivated
actors, with a corresponding focus on securing not only IT but also OT environments, as demonstrated by
recent attacks on North American critical infrastructure.
www.orangecyberdefense.com

54 Security Navigator 2025
© Orange Cyberdefense 2024/2025

Research Update 55
Research Update
Taking A
Closer Look
The Research Chapter of the Security Navigator 2025 presents key
insights into evolving cybersecurity challenges from Orange Cyberdefense
experts.
Wicus Ross critiques traditional vulnerability management, proposing
risk reduction and threat mitigation strategies to address systemic flaws.
Diana Selck-Paulsson and Ben Gibney analyze hacktivism’s geopolitical
alignment and its cognitive impacts on trust and cohesion. Charl van der
Walt explores AI’s growing role in defensive and offensive cybersecurity
applications. Ric Derbyshire examines OT-targeted attacks, advocating
for realistic testing and tailored defenses. Emmanuelle Bernard, Stéphane
Gorse, and Sébastien Roché highlight vulnerabilities across mobile
networks, from legacy systems to 5G risks.
www.orangecyberdefense.com

56 Security Navigator 2025
Charl van der Walt
Head of Security Research
Orange Cyberdefense
Research: Artificial Intelligence
What's All the Fuss?
Talking About AI: Definitions
Artificial Intelligence (AI) Large Language Models (LLM)
AI refers to the simulation of human intelligence in machines, LLMs are a type of AI model designed to understand and
enabling them to perform tasks that typically require human generate human-like text by being trained on extensive
intelligence, such as decision-making and problem-solving. text datasets. These models are a specific application of
AI is the broadest concept in this field, encompassing Deep Learning, focusing on natural language processing
various technologies and methodologies, including Machine tasks, and are integral to many modern AI-driven language
Learning (ML) and Deep Learning. applications.
Machine Learning (ML) Generative AI (GenAI)
ML is a subset of AI that focuses on developing algorithms GenAI refers to AI systems capable of creating new content,
and statistical models that allow machines to learn from such as text, images, or music, based on the data they have
and make predictions or decisions based on data. ML is been trained on. This technology often leverages LLMs and
a specific approach within AI, emphasizing data-driven other Deep Learning techniques to produce original and
learning and improvement over time. creative outputs, showcasing the advanced capabilities of AI
in content generation.
Deep Learning (DL)
Deep Learning is a specialized subset of ML that uses
neural networks with multiple layers to analyze and interpret
complex data patterns. This advanced form of ML is
particularly effective for tasks such as image and speech
recognition, making it a crucial component of many AI
applications.
Almost daily now we watch the hallowed milestone of the Like any technology, LLMs are neutral and can be used by both
“Turing Test” slip farther and farther into an almost naïve attackers and defenders. The key question is, which side will
irrelevance, as computer interfaces have evolved from being benefit more, or more quickly?
comparable to human language, to similar, to indistinguishable,
to arguably superior. But the journey here from early computer
AI for Good and Bad
vision and expert systems has been one of tall peaks and deep
valleys, with every “AI summer” apparently followed by a dark There is a strong argument that new technologies have an
and lifeless “winter”. asymmetric impact on security, strongly favoring the offensive
The development of large language models (LLMs) began with side. Thus, it seems likely that a general-purpose technology
natural language processing (NLP) advancements in the early (i.e. not developed for a security function) like LLMs will benefit
2000s, but the major breakthrough came with Ashish Vaswani’s attackers more than defenders.
2017 paper, “Attention is All You Need.” This allowed for training
larger models on vast datasets, greatly improving language
understanding and generation.
© Orange Cyberdefense 2024/2025

Research: Artificial Intelligence 57
Defensive
▪ May improve general office productivity and communication
▪ May improve search, research and Open-Source Intelligence
▪ May enable efficient international and cross-cultural communications
▪ May assist with collation and summarization of diverse, unstructured text datasets
▪ May assist with documentation of security intelligence and event information
▪ May assist with analyzing potentially malicious emails and files
▪ May assist with identification of fraudulent, fake or deceptive text, image or video content.
▪ May assist with security testing functions like reconnaissance and vulnerability discovery.
AI in one form or another has long been used in a variety of security technologies.
By way of example:
Intrusion Detection Systems (IDS) and Threat Detection. Security vendor Darktrace[39], employs ML
to autonomously detect and respond to threats in real-time by leveraging behavioral analysis and ML
algorithms trained on historical data to flag suspicious deviations from normal activity.
Phishing Detection and Prevention. ML models are used in products like Proofpoint[40] and Microsoft
Defender[41] that identify and block phishing attacks utilizing ML algorithms to analyze email content,
metadata, and user behavior to identify phishing attempts.
Endpoint Detection and Response (EDR). EDR offerings like CrowdStrike Falcon[42] leverage ML to
identify unusual behavior and detect and mitigate cyber threats on endpoints.
Microsoft Copilot for Security. Microsoft’s AI-powered solution[43] is designed to assist security
professionals by streamlining threat detection, incident response, and risk management by leveraging
generative AI, including OpenAI's GPT models.
Offensive
▪ May improve general office productivity and communication for bad actors as well
▪ May improve search, research and Open-Source Intelligence
▪ May enable efficient international and cross-cultural communications
▪ May assist with collation and summarization of diverse, unstructured text datasets
(like social media profiles for phishing/spear-phishing attacks)
▪ May assist with attack processes like reconnaissance and vulnerability discovery.
▪ May assist with the creation of believable text for cyber-attack methods like
phishing, waterholing and malvertising.
▪ Can assist with the creation of fraudulent, fake or deceptive text, image or
video content.
▪ May facilitate accidental data leakage or unauthorized data access
▪ May present a new, vulnerable and attractive attack surface.
Real-world examples of AI in offensive operations have been relatively rare. Notable instances include MIT’s Automated
Exploit Generation (AEG)[44] and IBM’s DeepLocker[45], which demonstrated AI-powered malware. These remain proof-
of-concepts for now. In 2019, our research team presented[46] two AI-based attacks using Topic Modelling, showing
AI’s offensive potential for network mapping and email classification. While we haven’t seen widespread use of such
capabilities, in October 2024, our CERT reported that the Rhadamanthys[47] Malware-as-a-Service (MaaS) incorporated
AI to perform Optical Character Recognition (OCR) on images containing sensitive information, like passwords,
marking the closest real-world instance of AI-driven offensive capabilities.
LLMs are increasingly being used offensively, especially in scams. A prominent example is the UK engineering
group Arup[48], which reportedly lost $25 million to fraudsters who used a digitally cloned voice of a senior
manager to order financial transfers during a video conference.
www.orangecyberdefense.com

58 Security Navigator 2025
AI and the Adversary ▪ AI-powered phishing and BEC tools designed to facilitate
the creation of phishing pages, social media contents and
In mid October 2024, our “World Watch” security intelligence email copies.
capability published an advisory that summarized the use of ▪ AI-powered voice phishing. In a report published on July
AI by offensive actors as follows: The adoption of AI by APTs
23, Google revealed[53] how AI-powered vishing (or voice-
remains likely in early stages but it is only a matter of time
spoofing), facilitated by commodified voice synthesizers,
before it becomes more widespread. One of the most common
was an emerging threat.
ways state-aligned and state-sponsored threat groups have
been adopting AI in their kill chains is by using Generative AI Vulnerability exploitation
chatbots such as ChatGPT for malicious purposes. We assess
AI still faces limits when used to write exploit code based on
that these usages differ depending on each group’s own
a CVE description. If the technology improves and becomes
capabilities and interests.
more readily available, it will likely be of interest to both
▪ North Korean threat actors have been allegedly
cybercriminals and state-backed actors. An LLM capable of
leveraging LLMs to better understand[49] publicly reported
autonomously finding a critical vulnerability, writing and testing
vulnerabilities, for basic scripting tasks and for target
exploit code and then using it against targets, could deeply
reconnaissance (including dedicated content creation
impact the threat landscape. Exploit development skills could
used in social engineering).
thus become accessible to anyone with access to an advanced
▪ Iranian groups were seen generating phishing emails and AI model. The source code of most products is fortunately not
used LLMs for web scraping[50]. readily available for training such models, but open source
▪ Chinese groups such as Charcoal Typhoon abused software may present a useful testcase.
LLMs for advanced commands representative of post-
compromise behavior[50]. Threats From AI
In October 9, OpenAI disclosed[51] that since the beginning of
the year it had disrupted over 20 ChatGPT abuses aimed at When considering threats from LLM technologies, we examine
debugging and developing malware, spreading misinformation, four perspectives: the risk of not adopting LLMs, existing AI
evading detection, and launching spear-phishing attacks. threats, new threats specific to LLMs, and broader risks as
These malicious usages were attributed to Chinese LLMs are integrated into business and society.
(SweetSpecter) and Iranian threat actors (CyberAv3ngers and
Storm-0817). The Chinese cluster SweetSpecter (tracked as The Risk of Non-adoption
TGR-STA-0043 by Palo Alto Networks) even targeted OpenAI
employees with spear-phishing attacks. Many clients we talk to feel pressure to adopt LLMs, with
CISOs particularly concerned about the “risk of non-adoption,”
Recently, state-sponsored threat groups have also been
driven by three main factors:
observed carrying out disinformation and influence campaigns
targeting the US presidential election for instance. Several ▪ Efficiency loss: Leaders believe LLMs like Copilot or
campaigns attributed to Iranian, Russian and Chinese threat ChatGPT will boost worker efficiency and fear falling
actors leveraged AI tools to erode public trust in the US behind competitors who adopt them.
democratic system or discredit a candidate. In its Digital ▪ Opportunity loss: LLMs are seen as uncovering new
Defense Report 2024, Microsoft confirmed[52] this trend, adding business opportunities, products, or market channels, and
that these threat actors were leveraging AI to create fake text, failing to leverage them risks losing a competitive edge.
images and videos. ▪ Marketability loss: With AI dominating discussions,
businesses worry that not showcasing AI in their offerings
Cybercrime
will leave them irrelevant in the market.
In addition to leveraging legitimate chatbots, cybercriminals
These concerns are valid, but the assumptions are often
have also created “dark LLMs” ( models trained specifically
untested. For example, a July 2024 survey by the Upwork
for fraudulent purposes) such as FraudGPT, WormGPT and
Research Agency[51] revealed that “96% of C-suite leaders
DarkGemini. These tools are used to automate and enhance
expect AI tools to boost productivity." However, the report
phishing campaigns, help low-skilled developers create
points out, “Nearly half (47%) of employees using AI say
malware, and generate scam-related content. They are typically
they have no idea how to achieve the productivity gains their
advertised on the DarkWeb and Telegram, with an emphasis on
employers expect, and 77% say these tools have actually
the model's criminal function.
decreased their productivity and added to their workload.
Some financially-motivated threat groups are also adding AI
The marketing value of being “powered by AI” is also still
to their malware strains. A recent World Watch advisory on
debated. A recent FTC report notes that consumers have
the new version of the Rhadamanthys infostealer describes
voiced concerns about AI’s entire lifecycle, particularly
new features relying on AI to analyze images that may contain
regarding limited appeal pathways for AI-based product
important information, such as passwords or recovery phrases.
decisions.
In our continuous monitoring of cybercriminal forums and
marketplaces we observed a clear increase in malicious
services supporting social-engineering activities, including:
▪ Deepfakes, notably for sextortion and romance schemes.
This technology is becoming more convincing and less
expensive over time.
1010000010100101010111110100110111101010101010100000100101010101111111001101010101111101010100101001010 1010000010100101010111110100110111101010101010100000100101010101111111001101010101111101010100101001000000100101010101111111001
© Orange Cyberdefense 2024/2025

Research: Artificial Intelligence 59
Businesses must consider the true costs of adopting LLMs,
including direct expenses like licensing, implementation,
testing, and training. There’s also an opportunity cost, as Summary
resources allocated to LLM adoption could have been invested
elsewhere. If AI is generally thought of as a productivity
tool, then we can expect it to make attackers
Security and privacy risks add further costs, alongside broader
more productive also. We have seen many
economic externalities—such as the massive resource
examples of this in the past, albeit seldom in
consumption of LLM training, which requires significant power
real incidents. These existing examples of AI
and water usage. According to one article[54], Microsoft’s AI
technologies in the hands of threat actors do
data centers may consume more power than all of India within
not warrant a substantial shift in enterprise
the next six years. Apparently “They will be cooled by millions
security strategy.
upon millions of gallons of water”.
Beyond resource strain, there are ethical concerns as creative
works are often used to train models without creators’ consent,
New Threats From LLMs
affecting artists, writers, and academics. Additionally, AI
concentration among a few owners could impact business,
The new threats emerging from widespread LLM adoption
society, and geopolitics, as these systems amass wealth,
will depend on how and where the technology is used. In this
data, and control. While LLMs promise increased productivity,
report, we focus strictly on LLMs and must consider whether
businesses risk sacrificing direction, vision, and autonomy
they are in the hands of attackers, businesses, or society at
for convenience. In weighing the risk of non-adoption, the
large. For businesses, are they consumers of LLM services or
potential benefits must be carefully balanced against the direct,
providers? If a provider, are they building their own models,
indirect, and external costs, including security. Without a clear
sourcing models, or procuring full capabilities from others?
understanding of the value LLMs may bring, businesses might
find the risks and costs outweigh the rewards. Each scenario introduces different threats, requiring tailored
controls to mitigate the risks specific to that use case.
Existing Threats From AI
Threats to Consumers
Like any powerful technology, we naturally fear the impact The key distinction between LLM users is between
LLMs could have in the hands of our adversaries. Much “Consumers” and “Providers” of LLM capabilities. A Consumer
attention is paid to the question of how AI might “accelerate the uses GenAI products and services from external providers,
threat”, and indeed a significant part of the report will consider while a Provider creates or enhances consumer-facing services
that question also. The uncertainty and anxiety that emerges that leverage LLMs, whether by developing in-house models or
from this apparent change in the threat landscape is of course using third-party solutions. Many businesses will likely adopt
exploited to argue for greater investment in security, sometimes both roles over time.
honestly, but sometimes also duplicitously.
It’s important to recognize that employees are almost certainly
However, while some things are certainly changing, many already using public or local GenAI for work and personal
of the threats being highlighted by alarmists today pre-exist purposes, posing additional challenges for enterprises. For
LLM technology and require nothing more of us than to keep those consuming external LLM services, whether businesses
consistently doing what we already know to do. For example, or individual employees, the primary risks revolve around data
all the following threat actions, whilst perhaps enhanced by security, with additional compliance and legal concerns to
LLMs, have already been performed with the support of ML consider. The main data-related risks include:
and other forms of AI[55]: ▪ Data leaks: Workers may unintentionally disclose
▪ Online Impersonation confidential data to LLM systems like ChatGPT, either
▪ Cheap, believable phishing mails and sites directly or through the nature of their queries.
▪ Voice fakes ▪ Hallucination: GenAI can produce inaccurate, misleading,
or inappropriate content that employees might incorporate
▪ Translation
into their work, potentially creating legal liability. When
▪ Predictive password cracking generating code, there’s a risk it could be buggy or
▪ Vulnerability discovery insecure[56].
▪ Technical hacking ▪ Intellectual Property Rights: As businesses use data to
▪ Backoffice automation train LLMs and incorporate outputs into their intellectual
property, unresolved questions about ownership could
The notion that adversaries may execute such activities expose them to liability for rights violations.
more often or more easily is a cause for concern, but it
The outputs of GenAI only enhance productivity if they are
does not necessarily require a fundamental shift in our
accurate, appropriate, and lawful. Unregulated AI-generated
security practices and technologies.
outputs could introduce misinformation, liability, or legal risks
Despite the ground-breaking innovations we’re observing, to the business.
security “Risk” is still comprised fundamentally from the
product of Threat, Vulnerability and Impact, and an LLM cannot
magically create these if they aren’t already there. If those
elements are already there, the business has a risk to deal
with that is independent of the existence of AI.
1010000010100101010111110100110111101010101010100000100101010101111111001101010101111101010100101001000000100101010101111111001
www.orangecyberdefense.com

60 Security Navigator 2025
Threats to providers The Open Web Application Security Project (OWASP)[57] has
identified “Prompt Injection” as the most critical vulnerability in
An entirely different set of threats emerge when businesses
GenAI applications. This attack manipulates language models
choose to integrate LLM into their own systems or processes.
by embedding specific instructions within user inputs to
These can be broadly categorized as follows:
trigger unintended or harmful responses, potentially revealing
Model Related Threats confidential information or bypassing safeguards. Attackers
craft inputs that override the model’s standard behavior.
A trained or tuned LLM has immense value to its developer
and is thus subject to threats to its Confidentiality, Integrity and Tools and resources for discovering and exploiting prompt
Availability. injection are quickly emerging, similar to the early days of web
application hacking. We expect that Chat Interface hacking
In the latter case, the threats to proprietary models include:
will remain a significant cybersecurity issue for years, given the
▪ Theft of the model.
complexity of LLMs and the digital infrastructure needed to
▪ Adversarial “poisoning” to negatively impact the accuracy connect chat interfaces with proprietary systems.
of the model.
As these architectures grow, traditional security practices—
▪ Destruction or disruption of the model.
such as secure development, architecture, data security, and
▪ Legal liability that may emerge from the model producing Identity & Access Management—will become even more crucial
incorrect, misrepresentative, misleading, inappropriate or to ensure proper authorization, access control, and privilege
unlawful content. management in this evolving landscape.
We assess, however, that the most meaningful new threats will When the “NSFW” AI chatbot site Muah.ai was breached in
emerge from the increased attack surface when organizations October 2024, the hacker described the platform as “a handful
implement GenAI within their technical environments. of open-source projects duct-taped together.” Apparently,
according to reports[58], “it was no trouble at all to find a
GenAI as Attack Surface vulnerability that provided access to the platform’s database”.
GenAI are complex new technologies consisting of millions of We predict that such reports will become commonplace in the
lines of code that expand the attack surface and introduce new next few years.
vulnerabilities.
Existing security practices like secure development,
As general GenAI tools like ChatGPT and Microsoft Copilot architecture, data security and Identity & Access Management
become widely available, they will no longer offer a significant will become even more critical as these complex hybrid
competitive advantage by themselves. The true power of LLM architectures need to assert authorization, access rights
technology lies in integrating it with a business’s proprietary and privileges.
data or systems to improve customer services and internal
processes. One key method is through interactive chat
interfaces powered by GenAI, where users interact with a
chatbot that generates coherent, context-aware responses.
To enhance this, the chat interface must leverage capabilities
like Retrieval-Augmented Generation (RAG) and APIs. GenAI
processes user queries, RAG retrieves relevant information
from proprietary knowledge bases, and APIs connect the Summary
GenAI to backend systems. This combination allows the
chatbot to provide contextually accurate outputs while With the strong focus on how threat actors may
interacting with complex backend systems. (ab)use LLMs, the less colorful risk introduced
in the application of the very young LLM
However, exposing GenAI as the security boundary between
technology as an interface by businesses is
users and a corporation’s backend systems, often directly to
being underestimated. It is crucial that we learn
the Internet, introduces a significant new attack surface. Like
the lessons of previous technology revolutions
the graphical Web Application interfaces that emerged in the
(like web applications and APIs) so as not
2000’s to offer easy, intuitive access to business clients, such
to repeat them by recklessly adopting an
Chat Interfaces are likely to transform digital channels. Unlike
untested and somewhat untestable technology
graphical web interfaces, GenAI’s non-deterministic nature
at the boundary between open cyberspace
means that even its developers may not fully understand its
and our critical internal assets. Enterprises are
internal logic, creating enormous opportunity for vulnerabilities
urged to be extremely cautious and diligent in
and exploitation. Attackers are already developing tools to
weighing up the potential (unknown) benefits
exploit this opacity, leading to potential security challenges
of deploying a GenAI as an interface, with the
similar to those seen with early web applications, that are still
potential (unknown) risks that such a complex,
plaguing security defenders today.
untested technology will surely introduce.
© Orange Cyberdefense 2024/2025

61
Research: Artificial Intelligence
Broader Impacts
Security is not an end in itself. It is fundamentally concerned with building and maintaining a foundation of
trust and trustworthiness on which businesses and societies can pursue a vision of the future. With this
benign, societal objective in mind, the broader potentially negative impacts of LLMs on the values that
shape our vision of the future must therefore also be considered.
We organize these into four categories – Technical, Business, Societal, and Rogue AI.
Business Technical
Beyond technical security risks, businesses adopting LLM Several new technical threats emerge as LLMs and GenAI
applications face three key higher-order business risks: become accessible to threat actors.
Data privacy and sovereignty LLM accelerate social engineering
The vast data required to develop, train, and run LLMs GenAI can quickly generate new images and content, making it a
results in unprecedented data collection and storage, raising useful tool for attackers creating phishing emails or fake websites.
significant privacy and sovereignty challenges as adoption While there’s no concrete evidence yet that GenAI-generated
grows. content is more effective than human-made content, it certainly
makes attackers more efficient.
Platform Provider Dependencies
Threat globalization
LLMs typically come from massive platform providers with
substantial data, compute, and engineering resources. This Social engineering, Business Email Compromise, Cyber Extortion,
creates dependency risks, that are well described by Bruce etc, all require the attacker to develop convincing and culturally
Schneier as “feudal security”[59]. And not all new providers will relevant content. GenAI allows attackers to overcome language
be sustainable. For example, despite OpenAI’s rapid revenue and cultural barriers, enabling them to create convincing, culturally
growth, it faces significant losses, projected to reach $5 relevant content and expand their reach into new geographies.
billion in 2024.
Acceleration of Existing Threats
Adoption Fatigue
GenAI will assist attackers at various stages of the kill-chain,
As AI evolves rapidly, new use cases constantly emerge, including Reconnaissance, Vulnerability Discovery, Exploit
creating pressure to adopt these technologies. Businesses Delivery, and exploitation of compromised assets.
should shift from a reactive approach to a strategic one to
avoid continuously responding to new AI industry trends and Data aggregation risks
offerings. LLM platforms collect vast amounts of data, exacerbating data
hoarding issues, which could lead to increased risks of theft or
leaks.
AI as an attack proxy
Just as attackers use VPNs and proxies, they may exploit public
LLMs that can access the internet to “proxy” their connections to
Summary
systems like web servers, adding a new layer to attack strategies.
LLMs are in their infancy, and as AI continues
to evolve in approaches, features and
capabilities, new use cases will continuously
be presented to business leaders. Given the Summary
indirect costs in human resources, focus and
creative energy that each new potential use- Apart from “deep fakes”, we don’t see much
case will demand, businesses are advised evidence of LLMs being used by threat actors
to avoid a cycle of reaction and develop a in a fundamentally revolutionary way. But there
controlled process whereby requirements and are several examples of how the technology
prerequisites are defined and documented can make attackers quicker, more effective,
upfront as a baseline against which new more efficient, or more difficult to spot. Given
technology offerings can be tested. the inherent asymmetry between attackers
and defenders, any technology that generally
improves “productivity” is likely to benefit
the attacker more than the defender. Thus,
the careless and unregulated release of such
capabilities onto the open market is a cause
for some concern, a matter that needs to be
brought to the attention of vendors, policy
makers and regulators.
www.orangecyberdefense.com

62 Security Navigator 2025
Societal This occurs in part because social media platforms act as
proxies between people, acting as mediators who decide
A widespread and thoughtless adoption of LLMs in a myriad of what we see and don’t see – who sees what and who gets to
domains – search, social, email, office productivity, customer speak. Large GenAI players are moving to position themselves
support, content creation, education and more – brings with it in a similar way – at the center of the public’s relationship with
several potential non-technical risks. information, communications, news, content, facts, truth, and
one another.
Some of these risks are apparent and widely discussed:
▪ The risks to privacy as data is sucked up to train models. Even the “simple” algorithmic mediation performed by
▪ The risks to privacy from people sharing personal social media platforms has caused significant damage. The
completely opaque and indecipherable workings of an LLM
information with GenAI.
do even more to coopt the essence of communications from
▪ The risks to professional creators being undermined by
between regular people. Eryk Salvaggio illustrates this point
cheap mass-produced content.
very powerfully when he describes the practice of “Shadow
▪ The gradual degradation of quality of research, creative Prompting”[62][63], in which GenAI providers apparently
content, reporting and other output as GenAI flood the (opaquely) modify the prompts entered by users to strip away
market and start to ingest themselves. potentially harmful questions, ensure diversity, or otherwise
▪ The risk of cultural and geopolitical over-influence by large “curate” a session between the user and the LLM. Thus, not
businesses who control the major LLMs. only do the answers emerge from an inevitably biased model,
▪ The risk of mistakes, like security vulnerabilities, even the questions are modified in a manner that suits the
provider.
introduced by LLMs into code, research, legal documents,
technical documents, etc.
Rogue AI
We’ve also already discussed how the security challenges we Some security and AI researchers[64] have raised concerns
face are exacerbated by the issue of economic “externalities”. about artificial AI that act against the interests of their creators,
GenAI purport to deliver significant increases in efficiency users, or humanity in general. Rogues could be accidental or
and productivity at the individual level, but do so by exploiting malicious, but they really come to fore when autonomous AI
several significant externalities: including the wanton mining of agents are empowered to query data, interact with APIs or
data, the assault on personal property, the cost of storage and perform other actions. The reasoning is that AIs are trained
computing, possible job losses, ecological impacts, and more. using reward models, which generally describe a desired
outcome, without fully defining the means by which they should
There are other risks to society, like the biases that LLM might
introduce into existing social inequalities. One recent study[60][61] be achieved. The risk that emerges is that an AI model goes
“rogue” and seeks to achieve its goals through unacceptable
for example demonstrated that speech-recognition systems
methods. The more reach the AI has through agents and
from leading tech companies were twice as likely to incorrectly
integration, the greater this threat becomes.
transcribe audio from Black speakers as opposed to white
speakers. Other research has shown that AI systems reinforce
long-held, untrue beliefs that there are biological differences
between Black and white people — untruths that lead clinicians
to misdiagnose health problems.
Another, less discussed, risk can be described as Summary
“intermediation”. There’s a joke that says GenAI are like arms
dealers – they sell to both sides. One person uses a GenAI to We need to think about the broader impacts
create bullet points from a long document, the other uses a on security, privacy and well-being for the
GenAI to make a long document from those same bullet points. whole of society. Our corporate and personal
The point is that GenAI are intermediating between both parties decisions to adopt, spend and invest with
– taking the role of a proxy or mediator in the communications enterprise LLM producers and providers will
process between two people. The same dynamic emerges empower those players to play an incredibly
when GenAI assist with search, write emails, summarize powerful role in shaping our understanding of
meetings, write reports, perform diagnosis, make bureaucratic the world, geopolitics, our communications,
decisions etc. and ultimately our futures.
Over the last decade we have witnessed how social media
platforms have struggled in their stated mission to “connect
the world” and have instead aggravated rifts and ideological
boundaries between people. Today, social media platforms are
the primary vehicles for delivering propaganda, disinformation,
social discord and other disruptors of society.
© Orange Cyberdefense 2024/2025

63
Research: Artificial Intelligence
Summary: LLM, Threats and You
While the Known Existing Threats identified in The goal of the CISO should be to provide employees
this report may intensify in volume, cadence and with safe access to appropriate LLM-based services that
sophistication, these threats are already accounted have been assessed to be safe, responsible, and in line
for by existing controls. The key to countering the with enterprise values, while equipping them to avoid
increased efficiency of threat actors armed with AI offerings that are unsafe or inappropriate.
technology is consistency. As has always been the
case, fundamental security technology, people and Education
processes need to be deployed consistently across
the enterprise. Develop training and coaching programs to equip
employees to think critically about the tension between
Countering the fundamentally New Threats that emerge opportunities and risks presented by implementations of
with the adoption of LLM applications will depend on how LLMs, and thus to select services and engage with them
the technology is adopted. in an appropriately cautious manner.
Mitigating the new threats that need to be anticipated as Data Leak Prevention
a provider is all about building solid security foundations.
The US National Security Agency’s Artificial Intelligence Implement training, technologies, assurance programs
Security Center (NSA AISC), in collaboration with and processes that minimize the potential for employees
several international cybersecurity agencies, provides to deliberately or inadvertently reveal sensitive or private
detailed guidelines[65] on securing AI systems. The report information to a 3rd party via a GenAI or LLM application.
emphasizes four key areas:
Data Security
1. Secure Design Involves incorporating security
LLMs cannot be depended on to enforce data security
measures from the outset of AI system
fundamentals like labelling or classification. Adoption of
development. It includes threat modeling, risk
an LLM that can access proprietary information must
assessment, and designing systems to be
therefore be regulated by ensuring that the underlying
resilient against attacks.
data security fundamentals are in place to restrict access
by an LLM capability as appropriate.
2. Secure Implementation Focuses on coding
practices and tools to ensure the AI system is
The broader set of new technical threats that emerge
built securely. It includes code reviews, static
from the more general adoption of LLMs can be
and dynamic analysis, and using secure coding
countered through education and empowerment efforts
standards to prevent vulnerabilities.
like those described above, and by consistently applying
known, existing security controls. However, there is
3. Secure Deployment Covers the strategies
also an opportunity for us to exercise our powers as
for safely deploying AI systems in production
voters and buyers in order to influence the priorities of
environments. It involves configuring systems
technology developers and the legislators who guide
securely, using encryption, and ensuring secure
them.
communication channels.
The risks of non-adoption in the form of productivity
4. Ongoing Maintenance Emphasizes the need
disadvantages, lost opportunities and lost marketing
for continuous monitoring and updating of AI
opportunities should be countered by exercising
systems to address new threats. It includes
cautious, rigorous processes that define metrics for
regular security audits, patch management, and
how new breakthroughs in LLM and other AI capabilities
incident response planning.
should be evaluated, and defining clear, necessary use
Other efforts, like the Coalition for SecureAI[66], are also cases with precisely defined criteria for success. Any
“dedicated to sharing best practices for secure AI”. As a framework for evaluating new AI opportunities should
business Consumer of LLM services, security is all about also pay attention to the true cost of adoption, including
enabling appropriate use safely. direct costs, economic externalities and the potential
negative impact on society.
www.orangecyberdefense.com

64 Security Navigator 2025
Tricking the AI
How to outsmart LLMs –
By Using Their Ability to ‘Think'
Over the past two years, the general public has become aware of the potential of generative AIs,
largely thanks to pioneers like ChatGPT, Claude, and Gemini, whose popularity has steadily increased.
These AI models, developed by tech giants, represent a major advancement in technological
evolution. At the heart of their functionality lies a key element: the prompt, an input provided by the
user or generated automatically, which the model analyzes to produce a response. However, in the
field of information systems security, the ability to submit arbitrary inputs to a program inevitably
raises concerns. Indeed, attacks both trivial and complex are gradually emerging.
Geoffrey Sauvageot-Berland, Computer Engineer, Pentester, Orange Cyberdefense
Prompt Injections: Obfuscation
The Achilles’ Heel of AI?
The use of obfuscated malicious instructions in a prompt allows
an attacker to lead the AI into reconstructing hidden directives,
Prompt injections, or prompt engineering, refer to instructions
exploiting its interpretative capabilities. This reconstruction
designed to provoke unexpected behavior in an AI model, a
is based on the prediction of the next word, which seems
"mathematical construct generating predictions from input
statistically most logical to the model. This process is called
data"[67]. LLMs (Large Language Models), a subcategory
"Next Token Prediction[72]." Several methods can be used to
of generative AI, specialize in natural language processing
achieve this:
(NLP), while generative AI encompasses a broader field,
including image, sound, or video creation. When a prompt
Modifying the spelling or syntax of words: Replacing or
injection succeeds, the model is considered "jailbroken." It
omitting certain letters in forbidden words to make them
then generates content outside the restrictions imposed by its
unrecognizable to filters. For example, "malware" can become
alignment policy[68], which aims to ensure ethical and secure
"m4lw4re" or "mlwr."
behavior.
Prompt injection techniques are influenced by the AI's intrinsic Encoding: Encoding a forbidden word in a format like base64.
functioning and its execution environment. Unlike classic The model can then be manipulated to decode this string, such
vulnerabilities, they are neither universal nor systematically as "bWFsd2FyZQ==" which, when decoded, means "malware."
reproducible. Due to the non-deterministic nature of AIs, the Other tricks like using emojis[73] or ASCII symbols[74] can help
same prompt may produce different results depending on mask these terms to evade detection and deceive the model.
previous prompts, making these attacks sometimes difficult to
anticipate. Thus, a deep understanding of the model's internal Autocompletion: By exploiting the model's autocompletion
workings is required to implement effective capabilities, the instruction is presented in the form of fill-in-
countermeasures. the-blank phrases that the model is led to complete, resulting in
the generation of instructions that were not initially authorized
This article explores the most widespread prompt injection
by the model. Here’s the proof of concept[75]
methods currently, deliberately omitting role-playing
I conducted on the mistral:7b model.
injections[69] (a simplistic form now corrected in most AIs).
Although the focus is on "direct" injections, where the
prompt is submitted directly to the AI, it is important to note
that researchers have also managed to carry out "indirect" Attacker Motivation
injections using an external resource, such as a website[70].
From an attacker's perspective, the motivations
Context Switching for carrying out such attacks can vary:
▪ Generation of offensive responses: Bypassing
Context switching is a tactic that disrupts the LLM with a
protections to produce undesirable or compromising
sudden change in topic. The AI first follows seemingly harmless
responses, such as harmful instructions or offensive
instructions (prefix) before continuing with harmful directives
content.
(suffix). This difficulty in managing sudden transitions can
lead to unauthorized content, as demonstrated in this proof ▪ Access to confidential information: Gaining
of concept[71] that I conducted on the open-source model access to internal data about the model's operation,
mistral:7b. such as its "system prompt"[76], which may facilitate
understanding its inner workings. In other use cases,
this can also enable extracting information that other
users have previously provided to the model.
▪ Service disruption: Exploiting prompt injection
techniques to trigger erratic behavior or, in severe
cases, to paralyze the LLM, leading to service
interruptions or degradation.
© Orange Cyberdefense 2024/2025

Expert Insight: France 65
Denial of Service
This method involves asking the AI to perform a long or complex task, such as a
particularly difficult calculation, to generate uncontrolled content production. This
overloads the underlying system, leading to excessive resource consumption (CPU,
GPU, RAM), compromising service availability.
Note: If the AI is running on a cloud instance with usage-based billing, this type of
attack can lead to a significant increase in operational costs.
An example involving the Gemma:2b[80] model used the capability to solve complex
mathematical problems. Initially, the LLM refused the prompt "Calculate: 10x100000000"
due to its policy alignment. But after some negotiation, it became possible to get the
model to calculate a large number incrementally. By starting with a simple multiplication
such as 8x8, then gradually increasing the complexity of the calculations, the model
eventually accepts larger operations[81]:
>>> Calculate 8*8888[...]22.2404704747432103521515613156165
This led to excessive consumption of system resources for several minutes, ultimately
producing an incorrect result. This significantly impacted the availability of the LLM in
production, as it was impossible to interact with it through another instance during that time.
Multimodal Approaches
More sophisticated, a multimodal injection targets AIs processing multiple data types. This
attack hides instructions in input data, like hidden text in images or malicious metadata,
triggering unexpected actions or leaks, which expands the attack surface.
On the right is a multimodal injection I conducted in September 2024 on ChatGPT (GPT-4o).
I inserted instructions on a post-it, exploiting the model's ability to interpret handwritten data
from an image. The main dangers of multimodal prompt injection include bypassing security
filters, where vulnerabilities in different input modes (text, image, audio, etc.) can be exploited
to evade moderation systems and generate malicious or inappropriate content. Similar cases
of prompt injection in multimodal models have also been observed. For example, researchers
have successfully made models solve CAPTCHAs[82] or execute prompt injections via audio
recordings[83]. These attacks highlight new security challenges for multimodal models, as
traditional text-based protections often prove ineffective against malicious visual or auditory
data. This opens up avenues for cybersecurity research, although no concrete
countermeasures have yet been disclosed.
What Stance to Take In the Face of These Threats?
With the rise of artificial intelligence in recent years, several reference guides have been published to raise awareness
among development teams about security issues. Among the most popular are the OWASP Top 10 for LLM[77], a ranking of
the main vulnerabilities related to language models, and ANSSI's guide[78], which offers measures for secure integration of
these technologies. The technical documentation provided by learnprompting.org[79] is also worth mentioning.
Key recommendations from these guides include:
1. Limit the size of responses:
Key Takeaways
To prevent Denial of Service attacks, it is very important to strictly limit
the size of an AI's response in terms of the number of characters.
Prompt injections pose a real challenge
2. Human intervention for sensitive operations:
to generative AI systems.
For actions like deleting or modifying data, it is recommended not to
allow an AI to perform these tasks autonomously. As these technologies evolve, attackers
develop increasingly sophisticated
3. Tracking LLM actions:
methods, making it difficult for developers
Model actions must be monitored to detect any behavior that violates to implement effective solutions to address
security policies or attempts at injection. these vulnerabilities. As the era of artificial
intelligence is just beginning, it is essential
4. Frequent updates:
to promote the secure and ethical use of
To improve detection of malicious prompts, models should be regularly these innovations.
updated or adjusted. Designers often release updates in response to new
research publications.
5. Security testing:
A complete security audit, including penetration testing and robustness
evaluations, should be conducted before any deployment in production.
www.orangecyberdefense.com

66 Security Navigator 2025
Enhancing Beaconing Detection
with AI-Driven Proxy Log Analysis
In the ever-evolving landscape of cybersecurity, detecting beaconing activities is paramount for
safeguarding networks. Beaconing refers to the periodic communication between compromised
systems and external command-and-control (C2) servers, often used by malware to receive
instructions or exfiltrate data. Leveraging AI algorithms for proxy log analysis represents a significant
breakthrough, enabling organizations to identify abnormal communication patterns that may indicate
malicious activities. This article delves into the project and the engineering behind AI-driven detection,
highlighting its transformative potential in cybersecurity.
Anis Trabelsi, AI expert and Lead Data Scientist, Orange Cyberdefense
The Challenge AI-driven Detection
of Beaconing Detection Engineering: System Overview
Detecting beaconing poses a unique challenge for This AI-driven system continuously monitors proxy logs for
cybersecurity professionals. Traditional detection signs of beaconing. Key components of this approach include:
methods, such as signature-based approaches, often 1. Data Ingestion: Collecting and aggregating proxy logs
struggle to identify these subtle yet harmful behaviors. from various sources, ensuring comprehensive coverage
Beaconing activities can be infrequent and may blend of network activity. This step is vital for creating a robust
in with legitimate traffic, making them difficult to spot. dataset for analysis.
As attackers become more sophisticated, relying solely
2. Pattern Recognition: Utilizing algorithms to identify
on conventional methods leaves networks vulnerable
abnormal communication patterns. These algorithms are
to undetected threats. This underscores the need for
applied in every batch of 15 minutes to be the closest to
advanced detection mechanisms that can adapt to
the real time.
evolving tactics employed by cybercriminals. To sum
up, two main difficulties are present: first one is to avoid 3. Alerting Mechanisms: Implementing real-time alerts
legitimate beaconing due to trusted sites which could be for detected anomalies, enabling security teams to take
considered as “noise” for the network system detection. immediate action. This feature ensures that potential
Second difficulty: some attackers could make malicious threats are addressed promptly, reducing the risk of data
beaconing through trusted sites. breaches.
The Role of AI in Detection
Real-Time Data Processing
AI algorithms excel in processing massive volumes of data in real-time, a critical capability for
effective beaconing detection. By analyzing proxy logs—records of web traffic that capture user
activity and external communications—these algorithms can swiftly isolate suspicious behaviors.
For instance, they can identify:
• Repetitive Requests: Frequent requests to specific servers, especially those that occur at
regular intervals, and can signal malware communication attempts. AI can flag these patterns for
further investigation.
• Anomalous Patterns: Deviations from established traffic behavior, such as sudden spikes in
requests to unfamiliar domains, can indicate potential threats. AI's ability to learn from historical
data enhances its accuracy in recognizing these anomalies.
Automation and Response Time
Automating the detection process drastically reduces response times, a crucial factor in mitigating
potential damage. With AI, organizations can swiftly identify and neutralize threats before they
escalate. For example, when an AI system detects suspicious activity, it can automatically
trigger alerts, allowing security teams to respond immediately. This proactive approach not
only enhances incident response but also minimizes the window of opportunity for attackers
to exploit vulnerabilities.
© Orange Cyberdefense 2024/2025

Expert Insight: France 67
C2Graph (C2G) Implementation
ThCr2eGaratp hH (Cu2nGt) iisn agn im–p lementation of "Malware Beaconing Detection by Mining Large-scale DNS Logs for Targeted
Attack Identification" (Andrii, Katrin, & Xiongwei, 2016). The original article focuses on DNS logs, but the principles were
Tracking and Communication
extended to proxy logs adding jitter consideration to request size and delta time communication.
During our threat hunting process, we carefully track each
Workflow Overview
hunt, documenting the execution time and any findings. If we
▪ Data Extraction: Parsing proxy logs to extract relevant features.
find suspicious ports, processes, user behavior, or unwanted
▪ Graph Construction: Building a graph of source and destination nodes to analyze communication patterns.
software, we promptly notify our customers to ensure rapid
improvements i▪n the B ir i n e n n i v n ir g o : n C m re e a n t t i . o E n v o e f r y te h m u p nt o i r s a l m a a n p d p q e u d a t n o t itative delta sequences which are binned into buckets tagged with
letters. This process catches jitters.
the MITRE ATT&CK framework and executed in a systematic,
step-by-step manner, mimicking an actual attack.
Key Metrics:
We use baselin▪e queNroiedse a Dloenggrseidee: Rneewprley scernetast ethde, snpuemcbifiecr of incoming connections to a node. For example, a high degree for a
threat hunts designeledg titoim daettee csti tteh leik teo ogloso agnled. ccoomm mcoanntdrass ts with a low degree for a C2 server.
used by the thr▪e at gErodugpe. WAdedigitihotn: aInlldy,i cwaete esx tahme ifnree qreuleantecdy of communication between nodes, helping to filter out trusted sites
procedures within thaen dM fIoTcRuEs AoTnT s&uCsKpi cfriaomuse wacotrivki ttyo. identify
similar behaviors from other ransomware groups. For example,
AI Process:
we search for hacking tools or remote monitoring tools known
to be used by o▪t her Hthyrpeoatt haecstoisrs: wweit hs uhpigpho spere ivt aisle tnhcee b.eginning of an infection.
▪ First step: the AI is looking to low node degree sources – destinations connections with high edge weight.
Best practices are applied to stop further lateral movement by
▪ Second step: For these selected couples of sources and destinations the AI adds two scores, one for the
blocking or detecting suspicious behavior. We also recommend
binning temporal periodicity and another to the binning quantitative periodicity.
customers block any tools commonly used by ransomware
▪ Alerting: it is made when the normalized score combined for these two precedents is in the top 10%.
affiliates if those tools are unnecessary within their environment.
▪ Expert Feedback Loop: Security analysts review alerts to provide feedback on the accuracy of the AI's
assessments, helping to refine the model and improve future detection capabilities.
Key findings Benefits of AI-Driven Detection
What type of key findings could this type of The advantages of AI-driven detection are manifold:
algorithm highlight? ▪ Increased Accuracy: AI can discern subtle patterns
that traditional methods may overlook, leading to
Post phishing infection:
more reliable threat identification. By continuously
AI can find infections of internal phishing campaigns just learning from new data, AI systems can adapt to
after the click on the malicious link. changing attack vectors.
▪ Scalability: The system can handle vast amounts
Malicious website tracking:
of data, making it suitable for organizations of
AI can track the use of known malicious sites or abuse of all sizes. As businesses grow, the AI can scale
trusted web pages. accordingly, maintaining effective monitoring without
compromising performance.
Proactive Threat Intelligence: ▪ Proactive Defense: Early detection allows for
proactive measures, reducing potential damage.
In some cases, infections are not known by threat
By identifying threats before they can execute their
intelligence sources which could highlight new types
malicious intent, organizations can safeguard their
of infection.
assets more effectively.
Key Takeaways
AI-driven proxy log analysis marks a transformative step in beaconing detection. By harnessing the
power of AI, organizations can enhance their security measures, safeguarding networks against
sophisticated attacks. This technology not only improves detection capabilities but also empowers
security teams to respond swiftly and effectively to emerging threats.
Investing in AI technology for beaconing detection not only improves threat identification but
also strengthens an organization’s overall cybersecurity posture. While AI enhances detection
capabilities, the invaluable insights and expertise of human analysts are essential for interpreting
complex data and making informed decisions. As cyber threats continue to evolve, embracing this
technology could be the key to staying one step ahead of cybercriminals.
www.orangecyberdefense.com

Wicus Ross
Senior Security Researcher
Orange Cyberdefense
Research: Vulnerabilities
Beyond Vulnerability
Management
We Cannot Patch Fast Enough Can You CVE What I CVE?
The reactive nature of vulnerability management, combined Western nations and organizations use the Common
with delays from policy and process, strains security teams, Vulnerability Enumeration (CVE) and Common Vulnerability
who have limited capacity and cannot patch everything Scoring System (CVSS) to track and rate vulnerabilities,
immediately. Our Vulnerability Operation Center (VOC) dataset overseen by US government-funded programs like MITRE
analysis found 32,585 distinct CVEs across 68,500 unique and NIST. By September 2024, the CVE program, active for 25
customer assets, with 10,014 having a CVSS score of 8 or years, had published over 264,000 CVEs, with 14,443 marked
higher. Among these, external assets have 11,605 distinct as “Rejected” or “Deferred.”
CVEs, while internal assets have 31,966. With this volume of
NIST’s National Vulnerability Database (NVD) relies on CVE
CVEs, it’s no surprise that some go unpatched and lead to
Numbering Authorities (CNAs) to record CVEs with initial
compromises.
CVSS assessments, which helps scale the process but also
Why are we stuck in this situation, what can be done, and is introduces biases. The disclosure of serious vulnerabilities
there a better approach for businesses? is complicated by disagreements between researchers and
vendors over impact, relevance, and accuracy, affecting the
We’ll explore the state of vulnerability reporting, how to
wider community[84][85].
prioritize vulnerabilities by threat and exploitation, examine
statistical probabilities, and briefly discuss risk. Lastly, we’ll In 2024, a backlog of 18,167 unenriched CVEs accumulated
consider solutions to minimize vulnerability impact while giving at the NVD[86][87] due to bureaucratic delays, halting CVE
management teams flexibility in crisis response. enrichment despite ongoing vulnerability reports, and
dramatically illustrating the fragility of this system.
NR of CVEs Published per Year
Published Date vs Recorded Year
Nr of CVEs by date Nr of CVEs by CVEID
40,000
35,000
30,000
25,000
20,000
15,000
10,000
5,000
0
9991 0002 1002 2002 3002 4002 5002 6002 7002 8002 9002 0102 1102 2102 3102 4102 5102 6102 7102 8102 9102 0202 1202 2202 3202 *4202 5202
68 Security Navigator 2025
© Orange Cyberdefense 2024/2025 * CVEs for 2024 incomplete (YTD)

Research: Vulnerabilities 69
EPSS Threshold
Thresholds in Terms of Coverage, Efficiency, and Effort, Relative to Known Exploited Vulnerabilities
Efficiency Coverage Effort
100%
80%
60%
40%
A
B
20%
0%
0.1% 1% 10% 100%
CVE and the NVD are not the sole sources of vulnerability Threat Informed
intelligence. Many organizations, including ours, develop
independent products that track far more vulnerabilities than Despite its shortcomings, the CVE system still provides
the NVD’s CVE program. valuable intelligence on vulnerabilities that could impact
security. However, with so many CVEs to address, we must
Since 2009, China has operated its own vulnerability database,
prioritize those most likely to be exploited by threat actors.
CNNVD[88], which could be a valuable technical resource[89][90],
though political barriers make collaboration unlikely. Moreover, The Exploit Prediction Scoring System (EPSS), developed by
not all vulnerabilities are disclosed immediately, creating blind the Forum of Incident Response and Security Teams (FIRST)
spots, while some are exploited without detection—so-called SIG[94], helps predict the likelihood of a vulnerability being
0-days. exploited in the wild. With EPSS intelligence, security managers
can either prioritize patching as many CVEs as possible for
In 2023, Google’s Threat Analysis Group (TAG) and
broad coverage or focus on critical vulnerabilities to maximize
Mandiant identified 97 zero-day exploits, primarily affecting
efficiency and prevent exploitation. Both approaches have pros
mobile devices, operating systems, browsers, and other
and cons.
applications.[91] Meanwhile, only about 6% of vulnerabilities in
the CVE dictionary have ever been exploited[92], and studies To demonstrate the tradeoff between coverage and efficiency,
from 2022 show that half of organizations patch just 15.5% or we need two datasets: one representing potential patches
fewer vulnerabilities monthly[93]. (VOC dataset) and another representing actively exploited
vulnerabilities, which includes CISA KEV[95], ethical hacking
While CVE is crucial for security managers, it’s an imperfect,
findings, and data from our CERT Vulnerability Intelligence
voluntary system, neither globally regulated nor universally
Watch service[96].
adopted.
This paper aims to explore how we might reduce reliance on it
in our daily operations.
www.orangecyberdefense.com

The EPSS threshold is used to select a set of CVEs to patch, Likely Choices
based on how likely they are to be exploited in the wild. The
overlap between remediation set and the exploited vulnerability EPSS predicts the likelihood of a vulnerability being exploited
set can be used to calculate the Efficiency, Coverage, and somewhere in the wild, not on any specific system. However,
Effort of a selected strategy. probabilities can “scale.” For example, flipping one coin gives a
50% chance of heads, but flipping 10 coins raises the chance
Coverage is the percentage of remediated vulnerabilities that
of at least one heads to 99.9%. This scaling is calculated using
are also present in the target exploit group.
the complement rule[98], which finds the probability of the
Efficiency is the number of remediated vulnerabilities from the desired outcome by subtracting the chance of failure from 1.
target exploit group as a proportion of the total remediation
As FIRST explains, “EPSS predicts the probability of a specific
group.
vulnerability being exploited and can be scaled to estimate
Effort is expressed as the number of vulnerabilities in the threats across servers, subnets, or entire enterprises by
remediation group that will be patched as a percentage of the calculating the probability of at least one event occurring.”[99][100]
vulnerability population.
With EPSS, we can similarly calculate the likelihood of at
If you wish to explore EPSS further, then we encourage you to least one vulnerability being exploited from a list by using the
read our blog post that covers the EPSS tool used here in this complement rule.
section[97].
To demonstrate, we analyzed 397 vulnerabilities from the VOC
Point A in the chart on the previous page is where the scan data of a Public Administration sector client. As the chart
EPSS threshold is 14.9% and represents the level where the below illustrates, most vulnerabilities had low EPSS scores
Efficiency and Coverage intersect. A lower EPSS threshold until a sharp rise at position 276. Also shown on the chart is
would yield better Coverage, but at the cost of Efficiency, since the scaled probability of exploitation using the complement
Effort increases as the number of CVEs that must be patched rule, which effectively reaches 100% when only the first 264
grows. The opposite is also true: If the EPSS threshold is vulnerabilities are considered.
increased we would remediate a smaller number of (potentially
exploitable) CVEs, but with a higher risk of missing something.
Point B on the chart is where Efficiency and Effort intersect,
and represents the lowest EPSS threshold that should be
considered for this example. Selecting an EPSS threshold
smaller than 1.9% will result in increased Coverage, but with a
noticeable increase in Effort.
The example here is theoretical but it serves to remind us that
the choices we make with regards to patching come with real
tradeoffs.
ytilibaborP
1,2
1
0,8
0,6
0,4
0,2
0
1 71 33 94 56 18 79 311 921 541 161 771 391 902 522 142 752 372 982 503 123 733 353 963 583
70 Security Navigator 2025
Scaled Probabilities
Increasing Likelihood of Expoitation With Inclusion of More Vulnerabilities
Scaled EPSS EPSS
© Orange Cyberdefense 2024/2025

Research: Vulnerabilities 71
As the second line on the chart indicates, as more CVEs are From there, attackers can navigate to valuable assets. Thus,
considered, the scaled probability that one of them will be defenders must not only patch vulnerabilities but also restrict
exploited in the wild increases very rapidly. By the time there access across the security graph to minimize the impact of any
are 265 distinct CVE under consideration, the probability that compromise.
one of them will be exploited in the wild is more than 99%. This
level is reached before any individual vulnerabilities with high
Attacker Odds
EPSS come into consideration. When the scaled EPSS value
crosses 99% (Position 260) the maximum EPSS is still under We’ve identified three critical truths that must be integrated into
11% (0.11). our examination of the vulnerability management process:
Vulnerabilities with high EPSS scores also do not necessarily ▪ Attackers aren’t focused on specific vulnerabilities; they
have a high CVSS score. The bulk (38) of vulnerabilities shown aim to compromise systems to access the graph.
on the chart have a CVSS score between 5 and 6.25. Only ▪ Exploiting vulnerabilities isn’t the only path to compromise,
15 vulnerabilities in the set have a score between 7.5 and 9.8. and often, it’s not the most common one.
The highest scoring vulnerability only had an EPSS of 0.37%
▪ Attackers’ skill and persistence levels vary.
(0.0037).
These factors allow us to extend our analysis of EPSS
This example, based on actual client data on vulnerabilities
and probabilities to consider the likelihood of an attacker
exposed to the Internet, shows how difficult prioritizing
compromising some arbitrary system, then scaling that to
vulnerabilities becomes as the number of systems increases.
determine the probability of compromising some system within
EPSS gives a probability that a vulnerability will be exploited in a network that grants access to the graph.
the wild, which is helpful for defenders, but we’ve shown how
We can assume each hacker has a certain “probability” of
quickly this probability scales when multiple vulnerabilities are
compromising a system, with this probability increasing based
involved. With enough vulnerabilities, there is a real probability
on their skill, experience, tools, and time. We can then continue
that one will get exploited, even when the individual EPSS
applying probability scaling to assess attacker success against
scores are low.
a broader computer environment.
Like a weather forecast predicting “chance of rain,” the larger
the area, the greater the likelihood of rain somewhere. s is the estimated probability of a successful attack
n= ln (1 - s) p is the chance of success based on judged skill
This scaling effect makes applying EPSS for vulnerability ln (1 - p) ln is the natural log function
management in large environments less practical, as even n is the number of occurrences
with extensive patching, it may be impossible to reduce the
probability of exploitation somewhere near to zero. Given a patient, undse iste thcet eedst ihmaatcekde prr,o hboabwili tmy oaf nay s uactcteesmsfuplt ast taacrek
stanti=sticlna l(l1y -r se)quiredp tios tbher ecahacnhc ea o sf yssuctecemss g braasnedti nong juadcgceed ssski ltlo the
graph? lAn n(1s -w pe)ring ~t l h n1i s i8s r t0e h=e q n u a ir tu e lnr s a (l 1 a l o- p g 0 p .f9u ly 9n9 i c n 9ti g o)n a reworked binomial
Attackers Think in Graphs n is the numlbne (r1 o-f 0o.c0c5u)rrences
distribution in the form of this equation:[104][105]
In 2015, Microsoft Security Engineer John Lambert shared
an immutable truth in a blog post titled, “Defenders think
in lists. Attackers think in graphs. As long as this is true, ~180= ln (1 - 0.9999)
attackers win.”[101] Lambert explained, “Defenders don’t have ln (1 - 0.05)
a list of assets—they have a graph. Assets are connected by
security relationships. Attackers breach a network by landing Using this equation, we can estimate how many attempts an
somewhere in the graph, using techniques like spearphishing, attacker of a certain skill level would need. For instance, if
and hack by navigating it.” He added, “The graph in your attacker A1 has a 5% success rate (1 in 20) per system, they
network is shaped by security dependencies, network design, would need to target up to 180 systems to be 99.99% sure of
management, software, services, and user behavior.” success.
In vulnerability management, Lambert’s insights highlight two Another attacker, A2, with a 10% success rate (1 in 10), would
key realities. First, vulnerabilities are just one factor attackers need about 88 targets to ensure at least one success, while
use to gain access. The MITRE ATT&CK framework[102] a more skilled attacker, A3, with a 20% success rate (1 in 5),
documents many observed attacker behaviors. In July 2024, would only need around 42 targets for the same probability.
SensePost, part of Orange Cyberdefense’s Ethical Hacking
team, described how an attacker can evade an Endpoint These are probabilities—an attacker might succeed on the
Detection and Response (EDR) system using “attack first try or require multiple attempts to reach the expected
decorrelation.”[103] By manipulating a system to disclose success rate. To assess real-world impact, we surveyed
separate innocuous pieces of information, the attacker can senior penetration testers in our business, who estimated their
combine them to compromise the system without triggering success rate against arbitrary internet-connected targets to be
alarms, demonstrating that a skilled, persistent attacker can around 30%.
bypass controls, even in environments without exploitable
Assuming a skilled attacker has a 5% to 40% chance of
CVEs. Even if an environment is seemingly devoid of exploitable
compromising a single machine, we can now estimate how
CVEs, a resourceful and experienced attacker with enough
many targets would be needed to nearly guarantee one
persistence may find a way to achieve a compromise, sidestep
successful compromise.
a control or avoid being detected.
Second, attackers don’t need to compromise a specific
system—any foothold in a homogenous network grants access
to Lambert’s “graph.”
www.orangecyberdefense.com

Use the Right Words
The current approach to vulnerability management is rooted
in its name: focusing on “vulnerabilities” (as defined by CVE,
CVSS, and EPSS) and their “management.” However, we have
The implications are striking: with just 100 potential targets,
no control over the volume, speed, or significance of CVEs,
even a moderately skilled attacker is almost certain to succeed
leading us to constantly react to chaotic new intelligence.
at least once. In a typical enterprise, this single compromise
often provides access to Lambert’s graph, and enterprises EPSS now helps us prioritize vulnerabilities likely to be
typically have thousands of computers to consider. exploited in the wild, representing real threats, which forces us
into a reactive mode. While mitigation addresses vulnerabilities,
our response is truly about countering threats—hence, this
Reimagining
process should be called Threat Mitigation.
Vulnerability Management
As discussed earlier, it’s statistically impossible to effectively
counter threats in large enterprises by merely reacting to
For the future, we need to conceive an environment and
vulnerability intelligence. Instead, we should focus on Risk
architecture that is immune to compromise from an individual
Reduction. Cyber risk results from a threat targeting a system’s
system. In the shorter term, we argue that our approach to
assets, leveraging vulnerabilities, and the potential impact of
vulnerability management needs to change.
such an attack. By addressing risk, we open up more areas
under our control to manage and mitigate.
sseccuS
fo
ytilibaborP
100%
90%
80%
70%
60%
50%
40%
30%
20%
10%
0%
1 4 7
01 31 61 91 22 52 82 13 43 73 04 34 64 94 25 55 85 16 46 76 07 37 67 97 28 58 88 19 49 79
001
72 Security Navigator 2025
Attacker Success
Based on the Probability of Success A1-5% A2-10% A3-20% A4-30% A5-40%
A1-5% A2-10% A3-20% A4-30% A5-40%
Attempts* 315 153 73 46 32
* The number of attempts will result in a 99.99999% probability of success
Objective Risk Reduction Threat Mitigation
▪ Reduce attack surface ▪ Respond to Vulnerability Intelligence
Strategies ▪ Deal with vulnerability classes ▪ Respond to Threat Intelligence
▪ Deal with asset classes ▪ Respond to attacks
Asset Intelligence
Intelligence Attack Intelligence
Vulnerability Intelligence
Threat Intelligence
Metrics Risk Metrics Threat Metrics
E.g. E.g.
▪ Deprecate unneeded ▪ Patch or mitigate vulnerable
systems Upgrade entire hosts systems
▪ Deprecate unneeded ▪ Suspend vulnerable
Tactics
software systems
▪ Upgrade application Adjust software/ ▪ Block threat
systems or BU vendor strategy ▪ Full Incident Response
▪ Improve patch automation
©© OOrraannggee CCyybbeerrddeeffeennssee 22002244//22002255

Research: Vulnerabilities 73
Threat Mitigation This approach is certain to be much less disruptive and more
efficient than responding to specific, new vulnerabilities.
Threat Mitigation is a dynamic, ongoing process that involves
Vulnerability Scanning remains important for creating an
identifying threats, assessing their relevance, and taking
accurate asset inventory and identifying non-compliant
action to mitigate them. This response can include patching,
systems, but it should support existing standardized
reconfiguring, filtering, adding compensating controls, or
processes, not trigger them.
even removing vulnerable systems. EPSS is a valuable tool
that complements other sources of threat and vulnerability
intelligence. Reimagining the Future
However, the scaling nature of probabilities makes EPSS less
The overwhelming barrage of randomly discovered and
useful in large internal environments. Since EPSS focuses
reported vulnerabilities as represented by CVE, CVSS and
on vulnerabilities likely to be exploited “in the wild,” it is
EPSS are stressing our people, processes and technology.
most applicable to systems directly exposed to the internet.
We’ve effectively been approaching vulnerability management
Therefore, Threat Mitigation efforts should primarily target
the same way for over two decades, but it hasn’t been
those externally exposed systems.
working and it’s not efficiently reducing risk, and so it too
must evolve.
Risk Reduction
It’s time to reimagine how we design, build, and maintain
systems.
Cyber risk is a product of Threat, Vulnerability, and Impact.
While the “Threat” is largely beyond our control, patching
specific vulnerabilities in large environments doesn’t
significantly lower the risk of compromise. Therefore, risk
reduction should focus on three key efforts:
A Template
1. Reducing the attack surface: As the probability of for a New Strategy
compromise increases with scale, it can be reduced by
shrinking the attack surface. A key priority is identifying Key factors to consider for security strategies toward
and removing unmanaged or unnecessary internet-facing 2030 and beyond:
systems.
1. Starting at the source
2. Limiting the impact: Lambert’s law advises limiting
2. Human Factor
attackers’ ability to access and traverse the “graph.” This
is achieved through segmentation at all levels—network, ▪ Leverage human strengths and anticipate their
permissions, applications, and data. The Zero Trust weaknesses.
architecture provides a practical reference model for this ▪ Gain support from senior management and
goal. executives.
▪ Be an enabler, not a blocker.
3. Improving the baseline: Instead of focusing on specific
vulnerabilities as they’re reported or discovered,
3. Threat-Informed Decision Making
systematically reducing the overall number and severity
▪ Learn from incidents and focus on what’s being
of vulnerabilities lowers the risk of compromise. This
exploited.
approach prioritizes efficiency and Return on Investment,
ignoring current acute threats in favor of long-term risk ▪ Use strategies to enhance remediation based on your
reduction. capabilities.
By separating Threat Mitigation from Risk Reduction, we 4. Threat Modeling and Simulation
can break free from the constant cycle of reacting to specific ▪ Use threat models to understand potential attack
threats and focus on more efficient, strategic approaches, paths.
freeing up resources for other priorities. ▪ Conduct Ethical Hacking to test your environment
against real threats.
An Efficient Approach
5. System Architecture and Design
The three Risk Reduction goals for internal enterprise ▪ Apply threat models and simulations to validate
networks aren’t driven by the random discovery of new assumptions in new systems.
Threats or Vulnerabilities but can be pursued systematically ▪ Reduce the attack surface systematically.
to optimize resources. The focus shifts from “managing
▪ Strengthen defense in depth by reviewing existing
vulnerabilities” to designing, implementing, and validating
systems.
resilient architectures and baseline configurations. Once
these baselines are set by the security function, IT can take ▪ Treat SASE and Zero-Trust as strategies, not just
over their implementation and maintenance, aligning with technology.
existing IT processes for greater efficiency. The security
6. Secure by Demand / Default
function can then validate compliance with the agreed
standards. ▪ Implement formal policies to embed security into
corporate culture.
The key here is that the “trigger” for patching internal systems
▪ Ensure vendors and suppliers have active security
is a predefined plan, agreed with system owners, to upgrade
improvement programs.
to a new, approved baseline.
wwwwww..oorraannggeeccyybbeerrddeeffeennssee..ccoomm

74 Security Navigator 2025
Starting at the Source System Architecture and Design
The first place to reduce the load of managing vulnerabilities, Existing system designs should be reviewed based on
is at the source, by reducing the number of vulnerabilities threat models, past incidents, or latent defects identified
in the technology products we deploy. CISA Director Jen by vulnerability management teams. There is always room
Easterly criticized vendors for producing poor-quality to strengthen ‘defense in depth’ through methods such as
software, describing the issues as ‘defects’ rather than just network segmentation, non-repudiable authentication, and
vulnerabilities.[106] Over 200 vendors have committed to least privilege for services and user accounts.
supporting the voluntary Secure by Design initiative for better
Reducing the attack surface methodically eases the burden on
self-regulation.
security operations, including vulnerability management. While
Google Android and Pixel have made headways over the past it may not always be feasible to remove or replace unsupported
few years to harden the mobile operating system (OS) and products, decommissioning unused assets in accordance with
mobile hardware platform[107]. These changes are directly policy is critical.
aimed at countering existing attacks or to make exploitation
Outdated systems tied to mission-critical processes often
considerably more difficult. The Google Android team indicated
require collaboration across teams to enhance confidentiality,
that most vulnerabilities in their mobile OS are present in
integrity, and availability. This ultimately becomes a business
new source code, while older source code has proportionally
decision, weighing time, cost, and resources.
fewer vulnerabilities[108]. They also believe that the number of
vulnerabilities will be reduced substantially over time due to As systems increasingly span on-premises and cloud services,
the introduction of memory safe techniques and memory safe businesses can operate with more flexibility. Secure Access
programming languages. Microsoft has also implemented Service Edge (SASE) and Zero-Trust should be approached
new standards, policies, and processes to ensure security is as strategies, not just technology stacks, to bolster defense in
integrated from the start of every project, with measures to depth by design.
track adherence and assess compliance. These changes were
Traditional principles like Confidentiality, Integrity, Availability
prompted by several serious incidents in 2023 and 2024.[109]
(CIA), and Non-repudiation remain essential, but newer
After a series of painful security missteps, VPN vendor Ivanti concepts such as Distributed, Immutable, and Ephemeral (DIE)
pledged[110] publicly to execute a plan “that accelerates can enhance security. DIE principles[111]:
security initiatives already underway and implements improved ▪ Distributed – no dependency on one host
practices to anticipate, prevent and protect against future
▪ Immutable – unable to modify assets
threats”. Every technology producer has the responsibility
to implement policies to explicitly state how products will be ▪ Ephemeral – short lived instances that are discarded help
created that are secure, and all buyers should pressure their address issues more efficiently.
vendors to commit to shipping more secure code.
Ephemeral hosts, in particular, benefit vulnerability
management, as each instance runs the latest baseline, with
Human Factors outdated or non-compliant versions quickly discarded.
For vulnerability management teams to succeed, gaining
Secure by Demand
support from key colleagues is essential. The program should
support the business, not create obstacles. Find a strategy or Secure by Default
aligned with the business’s goals, keeping that in focus. This
might require creativity and compromise. Start by having Technology commoditization has led to a race to the bottom,
conversations with key individuals to understand their needs. with vendors rushing to develop features and offer services at
Actively listen to their perspectives, as this could be the discount prices, often resulting in poor security outcomes for
foundation for your initial strategy. clients and collateral damage.
Corporate culture must shift through clear, formal policies that
Threat Informed Decision Making prioritize security at every level, ensuring it’s integrated into
every product or service. CISA’s ‘Secure by Design’[112] initiative
With the abundance of information on attacks, it’s easy to get encourages vendors to build security into products from
swept up in panic. The key is to assess how the published the start[113], while their ‘Secure by Demand’ guide provides
information applies to your environment and whether it resources to help buyers ensure security is central to their
warrants action. Understanding your environment and attack purchases. CISA also issued ‘Secure Design Alert’ advisories
surface is crucial in making informed decisions. to inform decision-makers about commonly exploited flaws in
specific technologies[114].
Threat Model and Simulate In the future, business-to-business relationships will evolve,
with vendors required to prove their security and quality
Ethical Hacking engagements provide a valuable opportunity
policies meet industry standards. Demanding secure products
to learn from experts by thinking like attackers. These services
and services will become standard practice.
are typically tailored to test specific systems or components
but can also be goal-oriented with broader objectives, like
assessing detection and response capabilities. The results
serve as highly localized threat intelligence, which should be
used to update threat models.
© Orange Cyberdefense 2024/2025

Research: Vulnerabilities 75
Summary
Security defenders are being overwhelmed Shifting this dynamic requires us to make
by a flood of erratic information about some fundamental changes to how we think
vulnerabilities that might need to be addressed. and work. This starts by abandoning the term
Not every vulnerability constitutes a threat, “Vulnerability Management” in favor of more
however, and it’s clear now that we may never specific and appropriate concepts – Threat
be able to respond to every vulnerability Mitigation (focused on exposed systems) and
that is reported. Given the scaling nature of Risk Reduction (focused on reducing impact
probabilities, addressing a limited number of and vulnerability overall).
specific vulnerabilities in a large environment
may not meaningfully reduce the chance that Both of these processes are supported by
attackers may compromise that vulnerability security practices like external attack surface
somewhere, and thus find a path to critical management (EASM) or a combination of
resources. vulnerability scanning and informed by threat-
and vulnerability intelligence, but these operate
Meanwhile the continuous cycle of collecting, in different environments and with different
assessing, and responding to vulnerability KPIs.
information is distracting from more impactful
efforts and exhausting our available resources.
www.orangecyberdefense.com

76 Security Navigator 2025
Vulnerability-
prone Network
Spotlight on VPN: Faulty by Design?
VPN gateways fill a unique role, exposed to all the hazards of the Internet, while at the same time,
having access to some of the most critical resources in the organization.
In many cases, software that has a track record of security vulnerabilities is deployed behind a VPN to
limit who can access it. What should one do if the problematic software is the VPN itself?
Rogan Dawes, SensePost Researcher, Orange Cyberdefense
In an April 2020 advisory, the U.S. Cybersecurity and But why are the vulnerabilities discovered in these products so
Infrastructure Security Agency (CISA) advised its stakeholders catastrophic? How is it that security products are repeatedly
to “immediately patch CVE-2019-11510 —an arbitrary file critically vulnerable to exploits, when software like OpenSSH,
reading vulnerability affecting Pulse Secure virtual private Postfix and Qmail which are equally exposed to the Internet
network (VPN) appliances”[115]. That same year, we reported have had only a handful of relatively low severity vulnerabilities
in our annual security Navigator report as noteworthy the over their extended lifetimes?
“visibility of several leading security product vendors in the
very short list of technology vendors who featured multiple
Vulnerabilities History
times in our intelligence advisories”. We further noted a four-
fold increase in vulnerabilities reported in selected security
CVE > 7
technologies between March and May 2020”. Four years Product All time CVEs
all time
later in February 2024, CISA issued another advisory about
another perimeter security product, this time going so far as
Postfix 1 11
to direct government agencies to “disconnect all instances” of
the affected VPN product”[116].
Qmail 2 5
The past five years have been characterized in a
significant way by the discovery and exploitation of
OpenSSH 25 116
vulnerabilities in perimeter security technologies, and
especially Virtual Private Networks (VPN).
While OpenSSH does appear to have a large number of
published vulnerabilities over its 25-year history, it is worth
Recent Vulnerabilities
keeping in mind the almost ubiquitous nature of OpenSSH,
making it an extremely high value target, and that many of the
Over the past several years, VPN software from multiple
published vulnerabilities are in non-default configurations,
vendors has been exploited repeatedly. For example, just in
or require misconfigurations in other products that leverage
2024:
OpenSSH as a component.
CVE > 7
Product in 2024 Announcements We posit that programs with a long history of good security
have been through an initial security architecture design
Ivanti Connect Secure 10 6 process, where the system has been decomposed into
elements, each responsible for a clearly defined aspect of
the system. These elements have been chosen to be as
Palo Alto Pan-OS 9 5
independent from each other as possible, communicating only
over carefully specified interfaces, so that a weakness in one
Fortinet FortiOS 15 8 element doesn’t compromise the entire system.
An example of this can be seen in Postfix’s documentation.
Each vulnerability advisory means that a team needs to drop
everything to deploy the relevant patches in their environment.
Example: Postfix
One VPN vendor even recommended that their own product
should be deployed behind a security gateway in order to Firstly, Postfix lists all the exposed entry points and documents
protect it from an actively exploited vulnerability! the components that require network access. Each of these
components performs a specific task, with only the code
required for that specific task present.
© Orange Cyberdefense 2024/2025

Expert Insight: South Africa 77
▪ Example of Postfix system architecture documentation from https://www.postfix.org/
This enables an administrator to decide which components Pan-OS similarly had HTTP endpoints vulnerable to directory
should be enabled or disabled, based on their specific traversal attack, as well as internal system processes
requirements, and limits the attack surface of the overall vulnerable to command injection using shell metacharacters,
system. The remaining components are inaccessible by design, another vulnerability class that has been known for decades.
running under unprivileged accounts, processing queues of
Many of the vulnerabilities listed for the products above were
files owned only by that account. In many cases, the individual
exacerbated by the services running as root, having full access
components are isolated with a limited view of the filesystem,
to the system, and handing those privileges to any successful
to prevent access to system or other files in the event of a
exploits. It has long been an axiom that services that do not
compromise.
need root privileges should not be run as root, to limit the
In other parts of the Postfix overview, specific mention is given damage caused in the event of a vulnerability.
to measures taken to limit resource consumption, which could
Looking at the vulnerability analyzes carried out by various
otherwise lead to a Denial of Service condition. Ways in which
parties, it appears that, either very little security architecture
an incoming email can result in command execution are also
design was carried out prior to building these systems, or that
highlighted, as a common source of security vulnerabilities.
the initial design has been modified so much over time as to
Other deliberate actions taken to eliminate vulnerability classes
be unrecognisable. Furthermore, fixes to vulnerabilities appear
include forbidding use of fixed-size memory buffers, a common
to have prioritised “point fixes” for just the specific identified
root cause of buffer overflow vulnerabilities.
weakness, rather than taking the opportunity for a broader
In contrast, an analysis of Fortinet done by Bishop Fox reveals fix, looking for other instances of that vulnerability type, and
that they deploy a monolithic binary that contains almost all of endeavoring to eliminate them from the system entirely.
its functionality in a single executable, run as the first process
Customers should require their vendors to provide details
on system startup. This eliminates any chance of process and
of the security architecture of their products, to ensure
privilege separation, implying that an exploited vulnerability
that they can make educated purchasing decisions. Lack
in a single function has access to all capabilities of the entire
of such documentation should be seen as an indicator
system. Other research reveals that Ivanti Connect Secure had
that they should be prepared for a never-ending cycle of
HTTP endpoints that were vulnerable to directory traversal
panicking, patching and praying.
attacks, a vulnerability class that has been known for at least
20 years.
Key Takeaways
Our adversaries are targeting and exploiting the technologies we install, develop and maintain to protect our
networks. The problem has been growing for several years now. As an industry, we should be solving these
problems, not creating them.
As we have since 2022, we call on our partners and competitors in the security industry to come together to
work on this challenge. We believe an industry-wide discussion needs to be had to determine whether the
problem is as real as we perceive it is, identify existing efforts that may already be underway to address the
issue, or create some form of partnership to work toward a better situation for ourselves and our customers.
If you want to discuss this and join our initiative, please do contact us:
partnerfortomorrow@orangecyberdefense.com
www.orangecyberdefense.com

78 Security Navigator 2025
Dr. Ric Derbyshire
Principal Security Researcher
Orange Cyberdefense
Trends, Targeting, and Testing of Operational Technology:
Ransomware Ripples & Real Risks
Introduction Historical Context
It has been well established that cyber extortion (Cy-X), or Last year, we presented the trends observed over 35 years
more specifically ransomware, is currently the main threat to of cyber-attacks impacting OT. We captured the data with a
operational technology (OT). Whether through dependencies strict set of criteria, including corroboration from at least 2
in the IT being impacted or an abundance of caution driving reputable sources that an incident was confirmed to be due
decisions to turn the OT off, IT-focused attacks dominate OT to a cyber-attack and caused an OT impact. We recorded a
datasets – including ours. relatively low volume of OT-impacting cyber-attacks because
of the strict criteria, but those we did record were well verified
We begin with this year’s overall roundup, noting all the
and contained enough data points to get a detailed view of
major trends we’ve seen. However, we wanted to focus on
the landscape. In total we recorded 119 cyber-attacks over
something different – the attacks where OT was the target,
the 35 years, and they were framed by a simple taxonomy that
not just the victim. We call these category 2 attacks, and what
we created to better understand which types of attack were
distinguishes them from others is the adversary’s use of tactics,
causing the impacts.
techniques, and procedures (TTPs) unique to OT. This focus
takes us into exploring what might motivate the adversaries The elephant in the room when visualizing the data was the
into conducting such attacks and the impacts they cause as a overwhelming volume of type 1a attacks from 2020 onwards.
result. This was due to cyber extortion (Cy-X) causing cascading
consequences all the way down to the physical process.
Finally, we ask the question ‘does OT penetration testing
Whether through dependencies being disrupted in the IT or the
effectively represent category 2 OT cyber-attacks?’. This is
OT process being shut down due to an abundance of caution,
answered with our ongoing research on the topic, funded by
OT has not escaped victimization when it comes to the scourge
the Research Institute in Trustworthy Inter-connected Cyber-
of Cy-X, or more specifically, encryption-based ransomware.
physical Systems.
Taxonomy for Types of OT Cyber Attack
1 2
Category
IT TTPs OT TTPs
1a 1b 1c 2a 2b
Type
OT targeted,
IT targeted IT/OT targeted OT targeted OT targeted, crude
sophisticated
IT attacked, IT attacked, Windows/Linux- Dedicated OT Dedicated OT
production Windows/Linux- based OT attacked devices attacked devices attacked
impacted indirectly based OT attacked with IT TTPs with OT-specific with OT-specific
Characteristics
as collateral with IT TTPs directly TTPs crudely, TTPs with
damage directly or as little precision or sophistication
collateral complexity
©© OOrraannggee CCyybbeerrddeeffeennssee 22002244//22002255

Research: OT-Security
50
45
40
35
30
25
20
15
10
5
0
It is important to note that despite their prominence, these There was just one incident represented by a type 1c attack,
attacks are rarely targeted directly at the OT. It is hard to where an adversary deliberately targeted OT with IT TTPs. In
ascertain the motivations of cyber criminals performing these this incident, the adversary deliberately deployed encryption-
Cy-X attacks, but due to the erratic targeting of Cy-X in general, based ransomware on the victim’s supervisory control and data
the OT impacts likely aren’t even intentional. acquisition (SCADA) server, which impacted the OT process.
Other than the Cy-X-focused category 1 attacks, there was a
small volume (19%) of category 2 cyber-attacks over our 35
years of data. The category 2 attacks were split evenly between
type 2a and 2b. The adversary demographics conducting
category 2 attacks has been quite fluid over time, with a
slight shift from insider threats to states. These attacks that
deliberately target the OT and include the use of specific TTPs,
are clearly much more intentional with their OT impact. What Has Changed?
Spoiler alert: much more of the same!
In collecting data between H2 2023 and H1 2024 our dataset
grew by 47 incidents, 29 incidents in the tail end of 2023 and 18
so far in 2024. This took our total from 119 to 166, meaning we
observed a staggering 39% increase in attacks between 2023
and 2024 relative to the 35-year period prior. This concerning
trend is the symptom of the accelerating volume of impacts
from Cy-X attacks.
Of the new cyber-attacks observed, an even greater proportion
of them were category 1 attacks, at 87% (41). One missing element is the presence of type 1b attacks, which involve an
opportunistic or accidental spillage into the OT by an adversary
using IT TTPs. This may be that adversaries haven’t managed
that over the past year, but it is more likely a result of articles
and reports focusing on impacts of events rather than the
details.
8891 2991 4991 6991 7991 9991 0002 1002 2002 3002 4002 5002 7002 8002 9002 0102 1102 2102 3102 4102 5102 6102 7102 8102 9102 0202 1202 2202 3202 4202
79
Count of Attacks From 1988 to 2024
39% Increase in Attacks Between 2023 and 2024 Relative to the 35-Year Period Prior
Category Proportions
Types of OT-Impacting Cyber-Attacks ‘23/’24
2% 1c:
O
6
T
%
-t
s
r
o
g
p
.
t h a is rg
t
2
i
e
c
b t
.
e : d O
,
T 6 %
1 3 %
c ru
T
d e
T P s
ta
2
rg
:
e t
O
e d ,
T
2 a : O T
8
1
7
:
%
IT
TTPs
85
ta
%
1
r
a
g
:
e
I
t
T
ed
www.orangecyberdefense.com

80 Security Navigator 2025
The Victims Adversaries
When it comes to victimology over the past year, we see Actors Conducting Cyber-Attacks on OT in ‘23/’24
much of the same. Geographically, we see a focus on the
USA with 49% (23) of all attacks. Germany experienced the
second highest number of incidents with 11% (5), which follows 2%
4%
on from the trend we reported last year, with its relatively
uncharacteristic prominence in cyber incident datasets. 6%
Manufacturing was the most victimized sector, with 57% (27) of
attacks over the past year. Interestingly, in our data regarding 6%
Cy-X victims this year, manufacturing has a share of 20% of
all victims and has grown 25% from last year. This share of
OT-impacting cyber-attacks follows on from the trend over
the past 35 years. Although that trend was heavily influenced
by the surge of Cy-X targeting manufacturing beginning in
2020. Transportation and warehousing was the second most
victimized sector and utilities third most, which is also similar to
last year’s results. However, manufacturing featured far more
significantly over the past year, with less diversity and share of
victimization from trailing sectors when compared to the full
dataset.
81%
As could probably be expected, 81% (38) of this year’s attacks
were perpetrated by criminals. States and unknown adversaries
share second spot, both responsible for 6% (3) each of the total
attacks over the past year. Unknown adversary types usually
stem from when the victim manages to respond to an event
Criminal State Unknown
quickly enough such that the adversary cannot complete any
Hacktivist Third party contractor
objectives, obscuring their motivations. Therefore, unknown
can be seen as a positive in some cases.
The Year in Context
Target Sectors
We’ll bring everything back together with a couple of
Affected by Ot-Impacting Cyber-Attacks ‘23/’24 visualizations using the whole dataset to give us an idea of how
the past year has contributed to overall trends.
2% When it comes to the various types of impacts experienced by
2% victims, it is no surprise that loss of productivity and revenue
2% still dominates. What else probably comes as no surprise is the
4%
second most prominent impact – data encrypted for impact.
4% Attacks that aren’t the result of encryption-based Cy-X tend
to have a more diverse range of impacts to be recorded. That
4% could be due to more detailed reporting on more interesting
attacks or a product of the attacks themselves - we’d guess
the former is a bigger contributing factor. Like last year,
7%
we have singled out the impacts unique to category 2 OT-
impacting cyber-attacks, which can be seen at the bottom
right of the visualization. Manipulation of control remains the
58% most prominent category 2-specific impact with the remaining
unique impacts fairly evenly distributed.
17% Finally, to wrap things up on this year’s round up of cyber-
attacks that impacted OT - the overview visualization. It depicts
flows of incidents by year (in 5 year bins), into the adversary
type that conducted it, into the category then type of cyber-
attack, and finally into the depth of the Purdue model[glossary]
reached by the adversary (although they all impacted level 0/1
in some way).
Manufacturing Transportation Utilities
a. Warehousing
Health Care and Information Mining, Quarrying,
Social Assistance Oil a. Gas Extraction
Professional, Scient., Public Retail and Trade
a. Technical Services Administration
© Orange Cyberdefense 2024/2025

|     |     |     | Research: OT-Security | 81  |
| --- | --- | --- | --------------------- | --- |
1a: IT targeted
T0829:
Loss of productivity
and revenue
1: IT TTPs
T1486:
Data encrypted
for impact
1b: IT/OT targeted
T0829: Loss of view
T0882: Theft of operational
1c: OT targeted information
T0827: Loss of control
T1499: Endpoint DoS
T1485: Data destruction
2a: OT/crude T0826: Loss of availability
T1561: Disk wipe
T0831: Manipulation of control
| 2: OT TTPs | 2b: OT/ |     |     |     |
| ---------- | ------- | --- | --- | --- |
T0880: Loss of safety
sophisticated
T0813: Denial of control
T0879: Damage to property
T0837: Loss of protection
T0832: Manipulation of view
For readers of last year’s Security Navigator, this might look  There is one very noteworthy positive to this dataset – tackling
familiar – and that’s because it is. Despite the 39% growth  the Cy-X issue will drastically reduce the number of impacts
in number of incidents in the dataset, the lack of diversity in  that OT experiences due to cyber-attacks. We will then be left
types of cyber-attacks impacting OT environments means  with predominantly category 2 attacks to concern ourselves
the visualization just gets bigger rather than changing in any  with, which tend to be much less frequent and require much
| notable way.  |     | more capability to execute. |     |     |
| ------------- | --- | --------------------------- | --- | --- |
The elephant in the room remains the same as last year, albeit
showing the biggest growth - that is criminals using IT TTPs
to perform IT targeted attacks predominantly reaching no
deeper than level 5 in the Purdue model. Of course, this is an
unfortunate reflection of the Cy-X acceleration.
| Year | Adversary | TTP category | Type | Purdue |
| ---- | --------- | ------------ | ---- | ------ |
level
|     | Criminal | 1: IT TTPs | 1a: IT targeted |     |
| --- | -------- | ---------- | --------------- | --- |
Level 5
2020
State
|      |            |     | 1b: IT/OT targeted | Level 4 |
| ---- | ---------- | --- | ------------------ | ------- |
| 2015 | Hacktivist |     |                    |         |
1c: OT targeted
Hacker
2010
Level 3
| 2005 | Insider |     |     |     |
| ---- | ------- | --- | --- | --- |
2a: OT targeted, crude
| 2000 |     |     |     | Level 2 |
| ---- | --- | --- | --- | ------- |
Unknown
| 1995 |     | 2: OT TTPs |     |     |
| ---- | --- | ---------- | --- | --- |
2b: OT targeted,
| 1990 | Third party  |     | sophisticated |         |
| ---- | ------------ | --- | ------------- | ------- |
|      | contractor   |     |               | Level 1 |
1985
www.orangecyberdefense.com

82 Security Navigator 2025
A Focus on Category 2 Cyber-Attacks But what about the actual category 2 attacks that have
occurred? Who is conducting them? What impacts are they
Last year, the focus of our OT article was on the Cy-X attacks achieving? And what might their motivations be? Let’s dig in…
because of their overwhelming presence in the dataset. The
How infrequent is infrequent? In our dataset it equates to 26
article revolved around category 1 OT cyber-attacks, with
attacks over 36 years, approximately 16% of our recorded
only a brief mention of what Cy-X may look like if the modus
OT-impacting cyber-attacks. This comes with the usual caveat
operandi was reimagined as a category 2 attack purposefully
that our dataset has limitations of public sources and only
targeting OT. This year we’ll shine a light on the attacks directly
concerns itself with cyber-attacks that have had an OT impact.
targeting OT with OT TTPs – category 2 attacks.
We may not have included attacks that were too sensitive to be
Cyber-attacks on OT, particularly category 2 attacks, are not reported or were focused entirely on espionage, which are both
as common as their IT counterparts. This is for a few possible particularly poignant for category 2 attacks. Regardless, those
reasons, including that OT is not encountered as frequently 26 attacks over time don’t show any pattern.
in victim environments, it is often segregated from the IT and
When it comes to whodunit the most frequent offenders are
Internet to some extent, and causing an impact to it generally
state actors, at 38% (10) of category 2 cyber-attacks, which
doesn’t fit into the motivations of most adversary archetypes.
makes sense given the scale and complexity of sophisticated
This comparative lack of frequency generally means that the
OT-targeted cyber-attacks. Following that are hacktivists
threat of an OT cyber-attack is low, which unfortunately has
with 23% (6) attacks. This appears to be a growing trend
created a common misconception that the resultant risk of an
with hacktivist groups either claiming to have attacked
OT cyber-attack is low. However, threat is only one factor that
OT or attempting to demonstrate capability, sometimes
contributes to cyber risk, the other factors are vulnerability and
successfully[117]. The third most frequent is the insider threat,
impact. When it comes to vulnerability, it is well established
at 19% (5) of category 2 attacks, which were more prevalent
that there are concessions made due to the requisite openness
earlier in the dataset.
and demand for uptime of OT, but the potential impact of
any cyber-attack on OT is what really drives the risk. Simply In terms of sectors most affected, manufacturing drops to
causing downtime in an OT environment has a quantifiably second place with 23% (6) category 2 attacks, as can be seen
substantial financial impact, but that is only part of the problem. in the chart below. Instead, utilities experienced the highest
Since OT cyber-attacks began, physical impacts have been felt volume of category 2 attacks at 46% (12). This shift might be
around the world, affecting a wide range of sectors. This threat indicative of the intentions of such attacks. Cy-X, the bulk
to human safety is what makes the lack of frequency of OT of category 1 attacks, may not target utilities as frequently
attacks almost irrelevant – the potential impact is so great that because of the attention it could attract as an attack on CNI.
the risk is unacceptable no matter how unlikely the threat is.
This is particularly true in critical national infrastructure (CNI).
Category 2: Adversaries Category 2: Sectors
Attacker Typology for OT Focused Cyber-Attacks ‘23/’24 Victimology of OT Focused Cyber-Attacks in ‘23/’24
4% 4%
4%
8%
4%
4%
8%
38%
15% 46%
19%
23%
23%
State Hacktivist Insider Utilities Manufacturing Transportation and
Warehousing
Hacker Unknown Third party contractor Health Care Information Multiple
Retail Trade
© Orange Cyberdefense 2024/2025

|     |     |     |     |     |     |     |     |     |     | Research: OT-Security |     |     | 83  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- |
Count
5
1
▪ Geographic distribution of category 2 attacks
The geographic spread of category 2 attacks looks quite  This means that the adversary manipulated the physical
different without the bias of Cy-X actors. Ukraine has  process in their attack, which from prominently reported
experienced 19% (5) of our recorded category 2 attacks, which  attacks the potential for damage should be clear. But it isn’t
probably comes as no surprise to those who have been paying  just manipulation of control, most types of impact caused by
attention to these types of attack given their publicity. Poland,  category 2 attacks are severe.
Russia, and USA share 12% (3) each, none of which follow any
pattern and tend to be isolated events.
When looking at the impacts caused by category 2 cyber-
attacks, we begin to see why the risk of these attacks is so high
despite the low frequency. 46% (12) of category 2 attacks in our
dataset experienced manipulation of control as an impact.
Impact of OT Cyber Attacks
Count of Impact Types From Category 2 Attacks
14
12
10
8
6
4
2
0
|     |     | y   | o   |     | y n |     |     |     | bility |     | w   | l   | n   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |
o n it e   t y ntr ol afe t otecti o pe r o l e w e n a n ucti o
|     | a t i o | l ti v u | g e r t |     |     | Wi  | nt  | Availa |     | V i | of  V i | ti o o |     |
| --- | ------- | -------- | ------- | --- | --- | --- | --- | ------ | --- | --- | ------- | ------ | --- |
u l n t r u c e n ma p e C o of  S Disk  C o of   a a t i Destr
|     | p o    | d e v Da | o of     | oss  | Pr  |     | of   |      | oss  |         | n   | pe r m |     |
| --- | ------ | -------- | -------- | ---- | --- | --- | ---- | ---- | ---- | ------- | --- | ------ | --- |
| Ma  | ni   C | Pr o R   | P r ial  |      | of  |     | oss  | of   |      | ulati o |     | O o r  |     |
|     | o f    |   d      |          | L    | ss  |     |      |      | L    |         | of  | n f a  |     |
|     |   o    | f a n    | e n      |      |     |     | L    | s s  |      | p       | ft  | I a t  |     |
|     | s s    |          | D        |      | L o |     |      | o    |      | n i     | e   | D      |     |
|     | o      |          |          |      |     |     |      | L    |      | M a     | h   |        |     |
|     | L      |          |          |      |     |     |      |      |      |         | T   |        |     |
www.orangecyberdefense.com

84 Security Navigator 2025
Country Industry Actor Impact
Loss of Availability
Loss of View
Australia
Theft of Operational Information
Ireland Utilities State
Data Destruction
Israel
Denial of Control
Iran
Manipulation of View
Disk Wipe
Ukraine
Insider
Information
Manipulation of Control
USA Retail Trade
Health Care
Unknown
Canada Loss of Safety
Manufacturing
Germany Hacktivist
Loss of Productivity and Revenue
Russia
Damage to Property
Transportation and Warehousing Hacker
Saudi Arabia
Loss of Protection
Venezuela Third party contractor
Loss of Control
Poland
Bringing It All Together Clandestine process degradation: Subtle, hard to detect TTPs
that make small changes in the victim’s process. Telemetry may
We can get an overview of category 2 attacks by visualizing be altered to make the attack look like an engineering issue.
their flows. This depicts victim country, into victim sector,
into adversary type, into impacts caused. What becomes Optimized, abrupt, and long-lasting process damage:
immediately clear is the diversity of category 2 attacks when Well researched attack that causes the biggest impact the
they are not overwhelmed with Cy-X. An interesting section adversary can achieve, typically happens quickly to limit the
to note is the utilities sector being targeted in conflict areas response, and causes as much downtime as possible.
– Israel, Iran, Ukraine, and Russia – targeted predominantly
by states. Russia also experienced category 2 attacks by Contemporary insider attacks are either less frequently
hacktivists toward their manufacturing and transportation and reported or simply less common. There hasn’t been a category
warehousing sectors. We pointed out earlier in the article that 2 insider attack recorded in our dataset since 2009. Insiders
category 2 attacks experienced manipulation of control as their tend to act on a motivation of revenge, which means a focus on
most frequent impact. This visualization shows that the lion’s damage to an organization’s physical infrastructure as well as
share of those impacts was from state and hacktivist actors. revenue – optimized, abrupt, and long-lasting process damage.
Insiders present some of the biggest potential for damage in a
One noticeable trend that isn’t directly apparent in the data is
category 2 OT cyber-attack because they already likely know
that of adversary motivation in relation to their desired impact
the environment they want to disrupt, meaning they know how
caused. Clearly, when including category 1 attacks, the main
to optimize their attack[120]. This phenomenon is similar for third-
motivation observed is financial gain by cyber criminals with
party contractors, too[121].
encryption and data exfiltration being the desired impact.
However, once we focus on category 2 attacks, we see such Which hacktivists are conducting OT-impacting cyber-attacks,
a diversity of victim countries, victim sectors, adversary types, and what that impact is, is up for debate. A crucial motivation
and impacts that it isn’t so clear-cut. Ignoring the hacker and of hacktivist groups tends to be notoriety, meaning they’re
unknown adversaries as they were never truly identified with a incentivized to embellish or even entirely fabricate stories of
cause, instead focusing specifically on state, insider, hacktivist, successful attacks. Category 2 attacks are no different from
and third-party contractor provides us with something more this trend, and discerning the valid ones is not without its
concrete. challenges. No less because the trend of hacktivists targeting
OT with category 2 attacks has seemingly accelerated since
Typically, states focus on strategic goals that are more overt in
2020, whereby perpetrators often align with a state on one
times of conflict. Espionage and prepositioning are two likely
side of a current conflict – in some cases, they align a little
goals of states, particularly prior to conflict, but they aren’t
bit too closely. This means that it is difficult to say whether
included in our data due to lack of OT impact. The impacts we
such attacks are strategic, state-sponsored/proxy attacks
have recorded suggest quite violent or disruptive motivation.
or legitimate, independent hacktivism fighting for a patriotic
More specifically, states have focused on clandestine process
cause. Regardless of who you believe is a hacktivist or what
degradation[118] or optimized, abrupt, and long-lasting process
attacks they achieved, they generally favor one type of impact –
damage[119].
optimized, abrupt, and long-lasting process damage[122].
© Orange Cyberdefense 2024/2025

Research: OT-Security 85
For every adversary type, the described examples of OT Kill chains and similar concepts aren’t directly OT penetration
impacts with category 2 attacks are best achieved with testing literature, but it is important to understand the industry’s
sophistication, capability, and resource – meaning type 2b OT interpretation of an OT cyber-attack first.
impacting cyber-attacks that involve understanding the victim
Guidance, such as that found in ISA/IEC 62443[126] or NIST
environment and crafting a bespoke attack with complex OT
SP 800-82r3[127], is sparse when it comes to OT penetration
TTPs. However, that does not diminish the potential damage
testing. This category of literature is intended to be holistic and
caused, and therefore risk posed, by type 2a attacks – those
not solely focused on penetration testing, so shouldn’t be held
that still involve the use of TTPs unique to OT but perhaps do
accountable for defining how it should be conducted. However,
not spend as much time optimizing.
the guidance provided generally recommends penetration
The majority of OT TTPs that distinguish category 2 attacks testing, but that comes with caveats about OT’s fragility. Often
involve the use of native functionality against the victim, known there are compensating controls recommended, including
as living off the land. However, living off the land in OT is often replicated, virtualized, or simulated environments instead of
distinct from in IT due to its focus on the process and physical testing in production, but as other guidance points out[128],
environment, so we have taken to making that distinction those all have tradeoffs in realism.
clearer by calling it “living off the plant”. An advantage of this
Methodologies are a nebulous topic in OT penetration
strategy is blending in with the victim environment to evade
testing. Unlike other forms of penetration testing such as IT
detection, but in OT it goes further. From an adversary’s
infrastructure or web applications, there are no formally defined
perspective, it is much safer to achieve their goals by using
methodologies. Instead, we turn to close approximations that
native functionality that a programmable logic controller (PLC)
are typically found in books such as Pentesting Industrial
expects than by abusing its memory with an exploit. This
Control Systems[129], Industrial Cybersecurity[130], Industrial
applies to anything in an OT environment that might be critical
Network Security[131]. The trend common among all of these
to the process and is particularly effective because of OT’s
methodology approximations is that in a ‘real test’ the provider
requisite openness. Although living off the plant techniques
would first gain initial access to the IT network, breach the
are effective, simply having access to an OT environment does
demilitarized zone, gain access to the OT and then it is ‘game
not mean using them is trivial nor that the desired impact is
over’ save for some possible IT TTPs against more IT-friendly
feasible. That then poses the question, how does an asset
devices in what would be considered level 3 of the Purdue
owner know their OT environment’s susceptibility to category 2
model. In fact, for most publications, any testing of OT systems
living off the plant techniques?
is simply not feasible in any way, with only isolated device
testing in a controlled environment. Not only is testing the OT
environment not feasible, it is often described as unnecessary
We’d like to thank the Research Institute in
based on the assumption that access guarantees the adversary
Trustworthy Inter-connected Cyber-physical
free reign to do what they want. This trivializes the complexity
Systems (RITICS) for funding this ongoing
of OT cyber-attacks that is even acknowledged by the kill
research. The following is not representative
chains mentioned earlier.
of the project’s overall outcomes and simply
represents work to date. Research is equally as sparse as the methodology literature,
with few publications working on improving the OT penetration
testing discipline. However, there are two areas of note.
The Efficacy of OT Penetration Testing The first is work looking to improve the scoping of OT
penetration tests by building in safety[132], which improves the
This year we embarked on a project to understand the state of methodological/process side of the discipline. The second is a
the art with regards to OT penetration testing. The main aims small body of literature that ingests PLC project files (their code
of the project are to identify key challenges of the discipline, or configuration) to identify how variables can be manipulated
along with pertinent areas for research and development to to cause impact[133], which helps our understanding of how
improve it. In identifying the challenges, one of the research adversaries may cause low-level chain reactions.
questions was ‘does OT penetration testing effectively test
As far as the literature is concerned, OT penetration testing
for TTPs encountered in real attacks?’. The primary research
is still very much in its infancy. The guidance is ambiguous
is still ongoing, but the background literature review provides
and non-committal, the research does not currently support
some clues that we’ll discuss here. In the literature there are 4
the growth of the discipline, and the lack of methodologies
approximate categories that contribute towards this area: Kill
means current providers do not have a standard to base
chains, guidance, methodologies, and research.
testing on. Moreover, the existing methodologies may be
Kill chains offer overviews of adversarial tactics, generally in working within the limitations of production environments, but
a linear fashion, to describe how an attack may occur. There they are overconfident in their assumption that reaching the
are various kill chains that pertain to OT cyber-attacks, such OT is enough. There is a focus on IT TTPs that are not fully
as the Industrial Control System Cyber Kill Chain[123] and the representative of category 2 OT attacks, evidenced by historical
Cyber-Physical Attack Lifecycle[124], but we have also included attacks and the kill chains that model them. So, who are we
more comprehensive offerings such as the TTP-focused MITRE emulating with our OT penetration testing, the adversaries we’re
ATT&CK® Matrix for ICS[125]. One feature that is recognizable looking to preempt and stop, or IT penetration testers?
immediately is their homage to the IT side of the attack that
As we’ve mentioned there is primary research to be done
generally precedes a category 2 OT attack. What this also
meaning our understanding of OT penetration testing may
means is the recognition that the IT and OT parts of the attack
change. We will continue to release those results as the
are distinctly different and the TTPs objectively shift when
project progresses, so stay tuned.
entering the OT environment.
www.orangecyberdefense.com

86 Security Navigator 2025
Diana Selck-Paulsson
Lead Security Researcher
Orange Cyberdefense
Ben Gibney
Security Analyst
Orange Cyberdefense
Research: Hacktivism
Exploring the Intersection
of Cyber Activism
and State-sponsored
Operations
Introduction Disclaimer
Since the war against Ukraine began in February 2022, Hacktivism is a complex issue, and this article doesn't cover
hacktivism has surged[134][135][136], impacting both private and all actors or activities from the past year. Our perspective,
public sectors through DDoS attacks, defacements, and shaped by Western, English-language viewpoints, may limit our
disinformation campaigns. These cyberattacks align with understanding of the broader phenomenon. We avoid naming
geopolitical events. As 2024 sees over 50 countries holding the Hacktivist group, as it thrives on attention.
elections[137], this creates particularly ripe conditions for
influence operations. DDoS attacks, driven by political tensions,
Historical Context of Hacktivism
have intensified, with one pro-Russian group alone claiming
over 6,000 attacks since March 2022. Driven by political Hacktivism has evolved through three key eras, which we
tensions and geopolitical conflicts[138][139], DDoS attacks in 2024 describe as follows. The first, the Digital Utopia era, was
have significantly increased in both volume and intensity[140]. driven by ideals of building a better internet, as seen with
Hacktivists are now more experienced, leveraging DDoS-for- groups like Chaos Computer Club (CCC)[143]. Next came the
hire services[141][142] and sophisticated tools. Anti-Establishment era, where hacktivists exposed the flaws
Last year, we tracked attacks by major pro-Russian hacktivist in how cyberspace developed, often opposing entrenched
groups, identifying regional patterns often linked to patriotism powers. The current Establishment era sees groups shifting
from actors in conflict zones. To better understand the complex from anti-establishment actions to aligning with state agendas.
threat landscape, we aim to explore current hacktivism more Traditional hacktivism, which rejects state control, differs
deeply, examining its various facets and connections to from this, as state-sponsored activities transform into cyber
geopolitical tensions, building on our previous findings. operations or warfare rather than true hacktivism.
This research explores how volunteer-based, multinational Evaluating the evolution of these groups offers key insights into
groups operate during warfare, comparing modern hacktivism the factors shaping today’s hacktivists. Understanding how
with past movements and examining its potential implications they differ from their predecessors reveals current motivations,
for the future. which can ultimately help in developing better strategies for
defending against them.
© Orange Cyberdefense 2024/2025

Research: Hacktivism 87
Beginning of the Digital Utopia Era
We begin in the mid-1980s and continue until the mid-2000s, with the Digital Utopia Era of hacktivism.
This was an era before the dot-com boom had occurred, only 42% of Americans had ever used a
computer in 1990 and only 22% of Europeans households having internet in 2001[144][145]. Given the
landscape had not been built, this allowed those involved – the early adopters - to act based upon
ideals. And while some of the ideals varied from group to group, the actions were normally grounded in
similar ideals. Examples include the Electronic Disturbance Theater (EDT) acting in accordance with civil
disobedience and pioneering digital protest tactics such as virtual sit ins and the Cult of the Dead Cow
(cDc) believing in free access to information, privacy rights, and the exposure of vulnerabilities in systems
used by powerful institutions[146]. Besides often being credited as pioneers of early hacktivism, cDc can
also be considered one of the first hacktivist groups testing influence campaigns and media manipulation.
Although not the first to manipulate the media, early hacker groups quickly understood the media's
hunger for sensationalism[147]. On the other side of the Atlantic, in Germany, there were groups such as
Bayrische HackerPost (BHP) who created information sheets to help educate people about technical
and political issues. At one point they attempted to hack into the German government to remove census
information, as they did not believe this type of personal information should be stored by the government.
Another German-based group is the Chaos Computer
Club (CCC) who promoted hacker ethics such as free
access to information, mistrust of authority, privacy
and ethical use of technology[148]. In the late 90s for
example, the CCC and others condemned the Legion
of Underground’s (LoU) for “declaring“ war on the
People’s Republic of China and Iraq[149] because they
violated human rights, as can be seen to the right.
Despite differences, these groups shared a belief in an
internet built on ideals benefiting society.
The 1986 Computer Fraud and Abuse Act (US)[150]
and the 1990 Computer Misuse Act (UK)[151] marked a
turning point by criminalizing some hacktivist activities.
These new legislations might thus have ushered in the
end of the Digital Utopian Era and set the stage for the
next.
Moving to the Anti-Establishment Era
Where the first era of hacktivism was filled with optimism, by the mid-2000s, the second wave was
characterized by cynicism, at times even bordering on nihilism[152]. Groups like Anonymous, Wikileaks,
and Lulzsec emerged, disrupting establishments like governments, corporations, and institutions without
aligning with any ideology. Lulzsec, driven by humor rather than political change, aimed to embarrass
companies. The vision of a digital utopia had faded, and the groups during the Anti-Establishment
Era focused on bringing down unjust systems and exposing establishment systems of oppression.
Hacktivism became reactionary, often retaliating against wars, as increasing digitalization widened
the attack surface. An anti-war focus began to emerge, more actions were taken by groups in direct
retaliation to ongoing wars[153]. Nevertheless, these activities were still executed from an anti-government
point of view, which was typical for this and the previous era. There is no universal answer as to what
brought an end to the Anti-Establishment era. One of the main causes could have been the number of
arrests occurring across the different groups[154]. It became very hard to recruit people to a group named
Anonymous when so many of the members were identified.
Arriving at the Establishment Era
Out of the ashes of the Anti-Establishment Era came the Establishment Era, which can be viewed
as emerging around 2014. From here many groups started to openly profess support for certain
establishments, like governments, religious institutions and nation-states. Modern hacktivism is more
often intertwined with geopolitical conflicts. The motivations have also expanded to include support
for state-affiliated campaigns, cyber protests, or disruptions tied to national or regional interests, thus
supporting an establishment. Earlier in this phase of hacktivist activity included geopolitical conflicts
such as the 2007 DDoS attack against Estonia[155], cyber operations during the Russo-Georgian War in
2008[156], and the Arab Spring where hacktivists supported pro-democracy movements across the Middle
East and North Africa[157]. But this era began revealing its true character from 2014, during Russia’s illegal
annexation of Crimea. In that year, volunteers began mobilizing themselves to take political action in
support of their government, carrying out defense-like activities. The mobilization of private capabilities
and non-state actors[158] in 2014 in Russia's war against Ukraine did not fully succeed in its strategy[159]
but did provide almost a decade of preparation for countries like Ukraine in terms of cyber resilience[160].
When Ukraine was attacked again in 2022, it was able to mobilize its cyber capabilities and digital
resistance movement more effectively.
www.orangecyberdefense.com

88 Security Navigator 2025
Modern Hacktivism Case Study:
How Does Modern Hacktivism Look?
In the modern era hacktivists utilize more advanced techniques.
This is partly due to technological advancements and the This study analyzes one of the most active pro-Russian
sharing of skills and tools in the shared economy model (albeit hacktivist groups since March 2022, focusing on its
at times with malicious intent), and partly because state- communication strategies, narrative construction, and
supported hacktivists might have opportunities to tap into geopolitical influence. It also examines the group’s alignment
better resources. DDoS attacks have consequently scaled with state actors, values, and its role within the broader
exponentially in size and sophistication, with modern groups ecosystem. While this report focuses on just this one group, its
claiming and executing DDoS attacks that generate billions prominence among peers offers valuable insights into similar
of requests per second[161][162] or consume 3.8 terabits per pro-government hacktivist groups, allowing the study to reflect
second (Tbps)[163][164] in bandwidth[165]. We also observe a broader behaviors and tactics seen across this threat actor
significant shift in the operational methods of hacktivist groups, landscape.
especially a growing reliance on DDoS-for-hire services and
crowdsourced DDoS tools[166].
Data Collection
The volunteer-based nature of these groups enables them to
scale attacks more effectively, as participants need minimal Our data was collected through systematic scraping of the
technical expertise and are incentivized through cryptocurrency hacktivist group’s Telegram channel monthly over a period
rewards. This is an interesting shift since early hacktivists of two years, from August 2022 to August 2024. The dataset
movements were primarily motivated by ideological or political renders:
causes, rather than financial rewards. One explanation for this ▪ 3,214 unique messages: These messages included
is that as the cybercrime economy evolved and DDoS-for-hire descriptions of the group’s targets and other contents
services became more accessible, the line between financially the group felt to share with the broader public. Thus, the
motivated attackers and ideologically driven hacktivists began messages serve to capture the group’s narratives.
to blur. Hacktivists in this era also started to cross the line to ▪ 6,674 unique targets: These targets encompass a wide
impacting critical infrastructure and Operational Technology
range of entities attacked by the group, provided and
(OT) systems[167][168]- previously the domain of organized
proven by the actors by posting a check-host link - an
cybercrime or state actors.
internet monitoring service commonly used by hacktivists
Today, hacktivist groups operate in smaller, and more as proof of the success of their Service DDoS attacks.
independent groups; and many of the more prominent
To ensure data consistency, scraping was conducted at the
hacktivist groups align themselves with major powers, allowing
same time each month. The data includes textual content
them to operate with less fear of authorities and prosecution
(reasons for targeting), metadata (timestamps, views, forwards),
compared to groups from previous eras.
and contextual information about the targets. After processing,
While most observed hacktivism attacks still focus on IT the exact number of targeted organizations and countries was
systems, the aim of hacktivism is increasingly less about determined.
technical disruption and more about shaping public opinion
and spreading fear, uncertainty and doubt (FUD) through
Data Processing
targeted manipulative campaigns[169][170]. For instance,
information operations in the Nordics escalated tensions during To analyze the communication patterns and geopolitical
Sweden and Finland's NATO accession. context of the hacktivist group, we analyzed the textual content
of each message using natural language processing (NLP). We
Modern hacktivists have shifted from anti-government
applied text preprocessing and named entity recognition (NER)
positions, like opposing censorship, to supporting pro-
to identify country references, refining the results with a custom
government agendas through cyber operations. Unlike earlier
list of known countries and nationalities. The extracted country
hacktivists who focused on individual rights and ethics, today’s
information was added to the dataset, allowing us to examine
groups often lack a history of activism. Hacktivism has evolved
the group's geopolitical focus and alignments.
through three phases: the digital utopian era, which envisioned
a better internet, the anti-establishment phase, which opposed
perceived injustices and an evil establishment, to the current Analysis
establishment era, where hacktivists align with state-backed
cyber objectives. In this new era, traditional hacktivism Before discussing the data, it’s important to summarize
that still operates and focuses on access to information, recurring themes in pro-Russian Telegram posts. These
privacy, fighting oppression and advocating for ethical use of narratives aren’t unique to one group but are common across
technology, is overshadowed. several pro-Russian cyber activists[171]. The group frames its
actions as retaliation for Russophobia[172], Western support for
Ukraine, or sanctions on Russia.
Messages often mock targeted nations, criticizing leaders for
prioritizing Ukraine over domestic issues.
© Orange Cyberdefense 2024/2025

Research: Hacktivism 89
They use militaristic language, praising Russia’s military and Their strategy aims to influence international perception while
positioning themselves as cyber warriors defending Russia's creating domestic instability. Attacks on services like public
interests, and aligning with broader narratives of resisting transport or banking systems highlight institutional vulnerability,
Western influence. reinforcing their narrative that the state is failing to protect its
citizens.
Consequently, it doesn’t necessarily matter who the victim is
“This is not the first year that we have been defending
at an operational level—it’s more about what the organization
Russia’s interests on the information front. We see how
symbolically represents in the context of a broader political or
the discontent of adequate citizens of foreign countries is
geopolitical message.
growing, whose authorities do not care about the problems
of their compatriots and spend huge amounts of money What does the data tell us?
on sponsoring Ukrainian terrorists. We also see total
In the following paragraphs we analyze how many targets this
censorship, which prevents the residents of these countries
specific hacktivist group has attacked over a two-year period.
from telling the truth. There it has become unacceptable to
The group posted 3,214 unique messages. Within these we
speak positively about Russia. There is absolutely nothing
identified 6,674 targets from the private and public sector,
left of freedom of speech in the West[...]”
averaging around 280 targets per month.
Excerpt from one of the
The volume of messages fluctuated, potentially suggesting
announcements on the Telegram channel
organized campaigns, likely timed to align with key political or
military events. The group's focus appears to shift in response
The group occasionally references subscriber requests and to geopolitical tensions, elections, or other notable events,
volunteer input, showing they incorporate follower feedback reflecting a calculated effort to exert influence. This we will
when selecting targets. This fosters community involvement investigate below (under Geopolitical impacts).
and introduces a crowd-sourcing aspect to their cyber
In September and October 2023, we see a significant increase
operations.
in activity. Analysis of the message contents indicates that
Germany, Finland, Czech Republic, Canada, United Kingdom
Victimology and Sweden were particularly heavily impacted. This surge
coincides with key events such as national holidays (e.g. Czech
Why we see specific targets being attacked – Republic’s national day), international meetings (such as the
a contextual analysis. Malta Peace Formula meeting) and high-profile scandals (such
as the Canadian Parliament incident[173]).The alignment allows
The group’s activities against targets serves both as a
the group to frame these cyber operations as symbolic acts of
disruption tool and a symbolic statement against specific
punishment.
nations. By attacking organizations tied to everyday services,
they retaliate against perceived wrongs and express
disapproval of the nation's political stance, particularly
regarding Russia and Ukraine.
Count of Targets Over Time
Number of Hacktivist Activities Observed Since 2022
2022 2023 2024
600
528 539
500
453
400 384
368
336 347 300
302
280
300 278 257 249
264 265 272 261
247 208
205
200
154
137
100
28
14
0
Aug Sep Oct Dec Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug
www.orangecyberdefense.com

90 Security Navigator 2025
Trigger: German Farmer’s protest (Dec 16-Jan 15)
Hacktivist reaction:
Attacks on German government websites
Attacks on German transport websites
Attacks on German logistics websites
Trigger: Finnish Presidential Elections (January 25) Attacks on German federal websites
Hacktivist reaction: J
Website belonging to presenidential candidate was attacked
Attacks on bank of Finland a Trigger: French Farmer’s protest (Jan 16-Feb1)
Attacks on transport and cybersecurity agency websites of Finland n Hacktivist reaction:
Attacks on local government websites
Trigger: Belgian Farmer’s protest (January 17) Attacks on more government websites
Hacktivist reaction:
Attacks on Belgium government websites
Trigger: EU Summit on Ukraine Aid (February 1)
Hacktivist reaction:
F Attacks on French energy companies and local governments
Trigger: Polish Farmer’s protest (Feb 9-Mar 6) e
Hacktivist reaction:
Polish websites were attacked in support of the farmers b
Polish transport sites were attacked multiple times
Trigger: Polish Elections (March 27)
Hacktivist reaction:
M
Polish transport sites were attacked in support
of Polish farmers protest a
r
Real-World Triggers
And Hacktivist Activity Trigger: Polish Farmer’s protest (16-17 April)
A Hacktivist reaction:
Protest/strike p Polish transport sites were attacked multiple times
Election r
Summit/conference
Anniversary
Trigger: Ukraine Victory Day (May 9)
Hacktivist reaction:
M Attacks on numerous Ukraining government websites
a
y
Trigger: Spainish Taxi strike (May 28)
Hacktivist reaction: Trigger: G7 summit (3-15 June)
Attacks on transport networks in major Spanish cities Hacktivist reaction:
Attacks in Italy for hosting G7 summit
Trigger: EU Parlament Election (6-9 June)
Hacktivist reaction: Trigger: Ukraine Recovery Conference (11-12 June)
Multiple EU-owned websites taken down J Hacktivist reaction:
u Attacks on German websites for hosting the conference
Hacktivist reaction:
Attacks on Dutch websites due to them being in the EU n Trigger: Ukraine peace summit (15-16 June)
Hacktivist reaction:
Hacktivist reaction: Attacks on Swiss websites for hosting the peace conference
Attacks on Irish websites due to them being in the EU
Hacktivist reaction:
Attacks on Polish websites due to statements made at this conference
Hacktivist reaction:
Attacks on Polish websites due to them being in the EU J
u Trigger: French national election (Jun 30)
Hacktivist reaction: Hacktivist reaction:
Attacks on Greek websites due to them being in the EU l Attacks seen on: 5th of July
"We continue to attack France ahead of the second round of parliamentary elections"
6th of July "Once again sending DDoS missiles to French websites"
Trigger: NATO Summit (9-11 July)
Hacktivist reaction:
Trigger: UK Parliamentary Election (4 July) Numerous Czech based websites were targeted related the upcoming summit
Hacktivist reaction: A
In collaboration with OverFlame the website of the
Democratic Unionist Party (DUP) was taken down u Hacktivist reaction:
Attacked numerous NATO hosted websites
g
Trigger: Austria Legislative Elections (September 29)
Hacktivist reaction:
Announcement of opAustria
S
Hacktivist reaction: e
Attacks on different political parties p
Hacktivist reaction:
Attack on voting applications
Trigger: Belgium Provincial Elections (13 October)
Hacktivist reaction:
Attacks on provincial Belgium websites
O
c Hacktivist reaction:
Last attack on Belgium websites
t
© Orange Cyberdefense 2024/2025

Research: Hacktivism 91
Finland
Netherlands
Ireland
Germany
UK Poland
Belgium
Czech Republic Ukraine
France
Austria
Switzerland
Italy
Spain Greece
Legend:
Number of circles: number of Hacktivist messages posted
Width of the circle: count of targets
Protest/strike
Election
Summit/conference
Anniversary
www.orangecyberdefense.com

92 Security Navigator 2025
Top 25 Targeted Countries
Between August 2022 and August 2024
800
683
700
599
600 540 535
500
413
393 378
400
302
278
300 244 233
206
200 188 171 156 151 131 126
105 98 87 86 82 76 74
100
0
Ukr ai n e
C
P ze o c la h n R d e p u blic S pai n It a L l i y t h u a ni G a er ma ny Fi nla n d M ol d ova S we d e
U
n nit L e a d t v K ia i n g d o m De n mark Est o nia Fr a nc e Ca n S a d w a itzerla n R d o m N a n et ia h erla n ds N or way Bel gi u m B ul g L a u r x i e a m b o ur g Sl ove nia A ustria
Our data shows that 42 distinct countries were targeted by Attacks on key transit hubs like Poland, or influential nations like
this threat actor over two years, with 96% located in Europe. Germany and France offer more immediate strategic gains than
The attacks are primarily geopolitical, targeting countries targeting the U.S.
rather than specific organizations. This becomes clear when
analyzing the messages where the actors address the country
Geopolitical Impacts
they meant to impact, while at the same time posting a list of
organizations that are meant to deliver the strategic message to To analyze factors influencing target choices, we first identified
a specific country and its civil society. relevant keywords linked to geopolitical events and extracted
In the context of the war against Ukraine, Ukraine and Eastern unique messages containing these keywords. Each message
European countries like Poland, Czech Republic, and Lithuania was then manually reviewed to confirm references to specific
are heavily targeted, reflecting geopolitical expectations. geopolitical events. This process enabled a focused analysis
Western European nations such as Germany, Italy, and France of how real-world developments may have shaped the group’s
also faced significant attacks, reflecting their NATO and EU decisions. A summary of the keywords we observed is shown
leadership roles. In France, the group exploited social unrest, below.
aligning with local farmer protest movements and public Our analysis reveals consistent support for anti-EU protests.
dissent. A surge in Spanish victims was triggered by the arrest In particular. the Farmers' Protests in Poland, Belgium, and
of two individuals in Spain tied to the group. Similarly, attacks Germany. Multiple European elections (United Kingdom,
on Germany carried anti-government sentiment and opposition France, Finland, Austria, Belgium and national independence
to its leadership. days (Ukraine and Poland) were frequent themes. Election
“As the rallies continue to rage in France, we support the interference marked an escalation, aiming to disrupt
[farmers] protesters and put down the communes” democratic processes.
(26th of January 2024) The group also reacted to international conferences, targeting
Finland and Moldova stand out for high attack volumes despite host countries or responding to specific comments made at
less direct involvement in the war against Ukraine. Finland's these events.
NATO membership and proximity to Russia drew increased Election interference represents an escalation beyond
attention, but Moldova saw almost 200 attacks in Q2 2024, typical DDoS attacks on infrastructure or military websites,
primarily DDoS attacks targeting state infrastructure and fueled as it directly targets the democratic process of a nation. By
by anti-government sentiment. Moldova's vulnerability due to attacking election-related websites and portals, the hacktivist
Transnistria likely contributes to its ranking. Spain and Italy also group aims to undermine public trust in the electoral system,
face frequent attacks, apparently in retaliation for their military disrupt the flow of information, and potentially influence the
support of Ukraine. Attacks focus on critical infrastructure and outcome of a key democratic process.
exploit internal dissent and are often framed as responses to
Russophobia and arrests of Russian sympathizers[174]. Canada The group frequently responded to international conferences
ranks unusually high among non-European targets, reflecting or summits by targeting the host country with cyberattacks.
Russia's global cyber reach against NATO-aligned countries. Occasionally, specific comments made during these events
The absence of the U.S. is notable, given its leading role in also triggered attacks against the countries involved. A
supporting Ukraine. summary of the events associated with selected keywords is
depicted on the previous two pages.
Pro-Russian hacktivists may focus on European countries due
to their proximity to the conflict, where disrupting supply chains
and infrastructure more directly impacts Ukraine.
© Orange Cyberdefense 2024/2025

|     |     |     |     |     |     |     |     |     |     |     | Research: Hacktivism |     |     | 93  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
Regional Breakdown
Geographic Regions and Countries Affected by Hacktivist Activities
Portugal 0.2%
Croatia 0.4%
Slovakia 0.5%
|     |       |          |         |      | C   | J a Is |     | %    |     |     |          |     |     |     |
| --- | ----- | -------- | ------- | ---- | --- | ------ | --- | ---- | --- | --- | -------- | --- | --- | --- |
|     |       |          |         |      | a n | p ra   |     |      |     |     |          |     |     |     |
|     |       |          |         | G    | a   | a e    |     | 0    |     |     |          |     |     |     |
|     |       |          |         |      | d   | n l 1  |     | e  1 |     |     |          |     |     |     |
|     |       |          | A       | r e  | a   |   1 %  |     |      |     |     |          |     |     |     |
|     |       | L        | S u s   | e    |  2  | %      |     | ai n |     |     |          |     |     |     |
|     |       | u        | lo tria | c e  | %   |        |     |      |     |     |          |     |     |     |
|     |       | x e      | v e     |  1   |     |        |     | kr   |     |     |          |     |     |     |
|     |       |          | m n     |  1 % |     |        |     | U    |     |     |          |     |     |     |
|     |       | B u      | b i a   | %    |     |        |     |      |     |     |          |     |     |     |
|     |       | l g      | o  1    |      |     |        |     |      |     |     |          |     |     |     |
|     |       | B e a    | u rg %  |      |     | N      |     |      |     |     |          |     |     |     |
|     |       | l g r ia |  1      |      |     |        |     |      |     |     |          |     |     |     |
|     | N     | i u      |  1 %    |      |     | o rth  |     |      |     |     |          |     |     |     |
|     | o     | m        | %       |      |     | A      |     |      |     |     | %        |     |     |     |
|     | r     | w   1 %  |         |      |     |  A s   |     |      |     |     | Poland 9 |     |     |     |
|     | N et  | a y      |         |      |     | ia     |     |      |     |     |          |     |     |     |
|     | h e   |   1      |         |      |     | m  2   |     |      |     |     |          |     |     |     |
|     | r la  | %        |         |      |     | e %    |     |      |     |     |          |     |     |     |
|     | n     | d        |         |      |     | ri     |     |      |     |     |          |     |     |     |
| Ro  |       | s   2    |         |      |     | c      |     |      |     |     |          |     |     |     |
|     | m a   | %        |         |      |     | a      |     |      |     |     |          |     |     |     |
|     | n i a |          |         |      |     | 2      |     |      |     |     |          |     |     |     |
|     |  2    | %        |         |      |     | %      |     |      |     |     |          |     |     |     |
Switzerland 2%
France 2%
|     |     |     |     |     |     |     |     |     |     |     | Czech  | R epublic |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | --- |
Estonia 3%
8 %
Denmark 3%
ingdom
United K
3%
Spain 8%
%
Latvia 3
E
u ro
|     |         | %   |     |     |     |     | p   |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     | weden 4 |     |     |     |     |     | e   |     |     |     |     |     |     |     |
 9
6
|     |     |     |     |     |     |     | %   |     |     | Ita   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- |
|     | S   |     | %   |     |     |     |     |     |     | ly 6% |     |     |     |     |
4
a
|     |     |     | o v |     |     |     |     | L    |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     | d   |     | %   |     |     | ith  |     |     |     |     |     |     |
|     |     |     | ol  |     | 5   |     |     |      |     |     |     |     |     |     |
|     |     | M   |     |     | d   |     | %   | u    |     |     |     |     |     |     |
|     |     |     |     | n   |     |     | 6   | a    |     |     |     |     |     |     |
|     |     |     |     | a   |     |     | y   | n ia |     |     |     |     |     |     |
|     |     |     |     | nl  |     |     | n   |      |     |     |     |     |     |     |
|     |     |     |     | Fi  |     |     | a   |  6   |     |     |     |     |     |     |
|     |     |     |     |     |     |     | m   |      | %   |     |     |     |     |     |
er
G
The #0409HACKEDOfBaltic campaign is similarly
|     |     |     |     |     | 11/07/24 |     | 06/08/24 | 05/08/24 | 23/07/24 |     | 23/07/24 |     | 24/07/24 |     |
| --- | --- | --- | --- | --- | -------- | --- | -------- | -------- | -------- | --- | -------- | --- | -------- | --- |
notable, involving multiple groups attacking  12:52 14:18 14:39 13:44 17:55 08:55
Latvia, Estonia, and Lithuania in response
to the 4th of September 2023 NATO military
exercises[175]. This attack lasted two days and
displayed an unusually high level of coordination
| and communication, compared to similar past  |     |     |     |     |                       | #              |           |                  | #             | #              | #                 |       | #             |            |
| -------------------------------------------- | --- | --- | --- | --- | --------------------- | -------------- | --------- | ---------------- | ------------- | -------------- | ----------------- | ----- | ------------- | ---------- |
|                                              |     |     |     |     | #                     |                | #         |                  |               |                |                   | #     |               | #          |
| events.                                      |     |     |     |     |                       |                | #         | Israel           |               |                |                   | Spain |               | #          |
|                                              |     |     |     |     |                       | #FreePalestine |           | #7_October_Union | #Holy_legue / | #NoName057(16) |                   |       | #RTF          |            |
|                                              |     |     |     |     | #breaker_of_illusions |                | #OpIsrael |                  | #HolyLeague   |                | #FuckGuardiaCivil |       | 7octoberunion | #FuckSpain |
The fluidity of the network dynamics is evident,  #Masters_of_the_fight #GLORYTORUSSIA
as campaigns like #0409HACKEDOfBaltic
focus on geopolitical targets, while others like
#FuckGuardiaCivil target law enforcement
efforts aimed at disrupting hacktivist activities.  04 / 0 9 / 23 04 / 0 9 / 23 04 / 0 9 / 2305 / 0 9 / 23 04 / 0 9 / 23 04 / 0 9 / 2304 / 0 9 / 23 04 / 0 9 / 23
|     |     |     |     |     | 2 0 : 4 8 | 1 5 : 3 | 9 1 7 : 0 6 1 4 | : 1 8 | 1 8 : 1 6 | 2 0 : 4 7 1 8 : | 4 9 |     | 1 3 : 3 7 |     |
| --- | --- | --- | --- | --- | --------- | ------- | --------------- | ----- | --------- | --------------- | --- | --- | --------- | --- |
Campaigns not directly tied to the Ukraine conflict
highlight the group's broader targeting strategy,
showing that they don’t only focus on states, but
|     |     |     |     |     |     |     |     |     |     |     | voskhod | rahdit | deadfoud | killnet |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------ | -------- | ------- |
also on specific law enforcement and societal
#
structures.
|     |     |     |     |     |     |           | #0409HACKEDOfBaltic  |     |     |                | zarya | wagner | xecatsha | beregini |
| --- | --- | --- | --- | --- | --- | --------- | -------------------- | --- | --- | -------------- | ----- | ------ | -------- | -------- |
|     |     |     |     |     |     | Lithuania |                      |     |     | Latvia Estonia |       |        |          |          |
0409hackedofbaltic
earspaw
www.orangecyberdefense.com

94 Security Navigator 2025
The Network  The graph shows connections when at least two of the nodes
(country, partner hacktivist group or hashtag) “have coincided”
We found a total of 48 other groups that were mentioned by  in one message, resulting in a graph with over 3,000 messages.
the hacktivist group in their messaging. The visualization below
shows a broad network of connections, with a focus on various  The connections between groups suggest a well-coordinated
collaborative network designed to enhance the impact of
hacktivist groups that joined attack campaigns, hashtags used
cyberattacks across multiple countries and sectors. Hashtags
and countries mentioned.
represent campaigns where various hacker groups, including
The yellow nodes show the countries mentioned in messages,  our research subject, converged for coordinated actions.
the blue nodes show hashtags included in the messages and
Spain stands out as a major target, surrounded by key
light green are the partners mentioned. The size of a node
hashtags, including #FuckGuardiaCivil. The arrest of two
gives an indication of how often it appears in messages, and
individuals in Spain tied to cyber activities driving this specific
the position of the node in the graph indicates how “central” it
focus. This hashtag is central, representing one of the group's
is amongst the messages published.
most visible campaigns.
#Masters_of_the_fight #Noname6669#SumatraSelatanCyberTeam
#OPIsrael Israel #FreePalestina
#All_Alliances WebSec #Hackforce
| Desin f o r mado  #noticias | Skillnet |     |     |     |
| --------------------------- | -------- | --- | --- | --- |
r u s o
|     | Federal Legion | #breaker_of_illusions |     |     |
| --- | -------------- | --------------------- | --- | --- |
RipperSec
#Z_BL4CX_H4T
| Finland |     |     |     | #BONDOWOSOBLACKHAT |
| ------- | --- | --- | --- | ------------------ |
The High Society
|     |               | AlixSec #FuckNATO | #7OctoberUnion | United States |
| --- | ------------- | ----------------- | -------------- | ------------- |
|     | The National  |                   | #Holy_legue    |               |
Cyber Army
United Kingdom
Belarus #7_October_Union #FuckGuardiaCivil The Holy LeagueNetForceZ
CyberDragon
313 Team
|     | UserSec |         | 7 October Union |                      |
| --- | ------- | ------- | --------------- | -------------------- |
|     |         | Ukraine |                 | Team Insane Pakistan |
PHOENIX
#FuckSpain
|     | Sweden |                  | Cybervolk | #Team_insane_pakistan |
| --- | ------ | ---------------- | --------- | --------------------- |
|     | 22C    | Japan #Cybervolk |           | #Spain                |
Unknowns group
Spain #OpSpain
Canada
France KyotoSH Czech Republic Luxembourg AzzaSec #GLORYTORUSSIA
NIGHTMARE
| Digital Revolt |     |     | Germany#spain | #RTF #NoName057 |
| -------------- | --- | --- | ------------- | --------------- |
Italy
Romania #HolyLeague
| Folk’s CyberArmy |     |     |     | #FuckNato |
| ---------------- | --- | --- | --- | --------- |
People’s CyberArmy
|                |         |     | Poland | #FuckEurope |
| -------------- | ------- | --- | ------ | ----------- |
| SERVER KILLERS | Moldova |     |        |             |
#GoalFromVolunteers
Denmark Lithuania
Latvia Estonia
Zarya
Black Wolfs
|     |     | Wagner | Vokshod |     |
| --- | --- | ------ | ------- | --- |
XakNet
#0409HACKEDofBaltic DEADFOUD
Team
Beregini
BEARSPAW
rAHDIt
|     |     | Joker DPR Killnet |     |     |
| --- | --- | ----------------- | --- | --- |
BEAR.IT.ARMY
Patr io t  B l ack  Xecatsha
M a t ri x
© Orange Cyberdefense 2024/2025
Hacker Council Global Cyber Army Of Russia #hackercouncil #weareknown VoltActivist #DataLeak #Pentest

Research: Hacktivism 95
Summary
This report offers insights into a pro-Russian Indeed, several fundamental similarities between
hacktivist group active for 2.5 years, which began modern hacktivism and cyber extortion can be
operations following the war against Ukraine. observed:
Between August 2022 and August 2024, the group
▪ Both invest heavily in building brand and
claimed over 6,600 attacks in more than 3,200
community for credibility.
messages, with 96% of their victims in Europe,
aligning with their anti-NATO and anti-Western ▪ Both operate publicly, offering real-time
stance. Surprisingly, despite frequent mentions, commentary on platforms like Telegram.
no attacks were observed on U.S. targets,
▪ Both are tolerated or even supported by nation-
possibly signaling an intentional avoidance. The
states when aligned with political objectives.
group focuses on sectors providing essential
services, such as financial, transportation, ▪ Both procure advanced tools or services in the
education, and government systems, with the aim dark economy to boost capabilities.
of disrupting societal stability. Notably, voting
▪ Both justify target selection retroactively, shaping
systems in countries like France, the UK, Finland,
narratives post-attack to maintain control over
Belgium and Austria were targeted during
the story.
elections, threatening electoral integrity and
sowing doubt about results. These attacks align ▪ Both use coercion, with hacktivism aiming to
closely with Russian state narratives, suggesting influence political outcomes and cyber extortion
potential state influence. threatening reputational damage through
document leaks.
Hacktivism has evolved from its early roots
of ideological protest, with modern groups Defending against these threats requires not
blurring the lines between hacktivism and state- only robust technical defenses but also strategic
sponsored cybercriminal activities. The pro- communication to counter disinformation and
Russian group’s actions are symbolically tied to maintain public trust. The cognitive element of
their targets, amplifying political messages or these attacks underscores the need for a holistic
undermining governance. Their campaigns often approach that includes safeguarding information
coincide with significant geopolitical events such integrity and strengthening public resilience.
as elections and summits. Like cyber extortion
groups that threaten to leak sensitive data,
hacktivists wield coercion to manipulate public
perception, shaping political outcomes.
Recommendations
From a technical standpoint:
▪ Implement standard security controls like DDoS protection, vulnerability mitigation, and attack surface
management.
▪ Continuously monitor evolving threats and use the latest threat intelligence.
▪ Develop incident response and crisis management plans that cover both technical recovery and public
communications.
▪ Engage in strategies to counter cognitive attacks that target public perception and trust:
▪ Monitor social and media channels for disinformation and respond quickly to debunk false claims.
▪ Communicate proactively with transparent updates to maintain stakeholder trust.
▪ Collaborate with public relations experts to craft consistent, credible messaging.
▪ Educate the public to recognize disinformation, fostering resilience against manipulation.
Given the escalation of hacktivism, particularly pro-Russian attacks targeting the West and NATO,
organizations in these regions should prepare for ongoing efforts to disrupt and destabilize.
www.orangecyberdefense.com

96 Security Navigator 2025
Human-Driven
Threat Hunting
A Real-World Approach To
Threat-Informed Defense
When discussing Threat-Informed Defense, the focus is on understanding the behaviour and
technology of threat actors to gain a deep technical insight. This approach supports proactive
threat hunting to prevent ransomware attacks, Advanced Persistent Threats (APTs) or criminal data
exfiltration and can also be applied post-incident to guard against future intrusions.
Simone Kraus, Senior CSIRT Analyst, Orange Cyberdefense
Knowing What to Look For Preparation For Threat Hunting
This method relies on a combination of human-driven threat To prepare for threat hunting, we leverage our analysis, create a
hunting and Threat-Informed Defense[176]. Skilled analysts TTP-based attack flow, and incorporate the latest Cyber Threat
actively search for real-world attacks, leveraging our own Intelligence (CTI) in collaboration with the wider cybersecurity
threat intelligence in combination with findings from our community[180]. We also hunt for vulnerabilities and tools
forensic investigations and reverse engineering of malware. commonly exploited by ransomware groups. We prioritize
vulnerabilities and tools based on their prevalence, focusing
By systematically analyzing Tactics, Techniques,
on those most relevant to the customer’s specific sector or
and Procedures (TTPs) and identifying Indicators of
country.
Compromise (IOCs) and behavioral patterns, we refine
our threat hunts. Further investigation, including reverse
engineering, often uncovers more IOCs, which we Key Questions
incorporate into our hunts. The goal is to detect anomalies, during preparation for a post-incident hunt include:
revealing suspicious activities related to specific incidents,
and ensure the attacker no longer has access. Our ▪ What was the initial access point, and how can it be
structured threat hunting approach is grounded in MITRE’s prevented in the future?
TTP-based method[177], which allows for a systematic
search. This is enhanced by David Bianco’s PEAK model[178] ▪ Are there any exploits tied to that initial access?
and MITRE Enginuity's “Summitting the Pyramid”[179], ▪ What are the CVE and EPSS scores of these
providing a clear, methodical approach to create robust vulnerabilities, and how many devices need
detection. A deeper understanding of these methodologies patching?
strengthens our technical capabilities.
▪ Are there any suspicious user accounts, GPO
During engagements, we assist customers by blocking changes, C2 connections, unusual login behaviors,
tools and IOCs, investigating suspicious activity, and or suspicious devices?
offering next-step recommendations. Post-hunt, we deliver
detailed documentation, including assessments and ▪ Are there other vulnerabilities commonly exploited
recommendations. In parallel, ongoing support is provided by ransomware groups?
if needed.
Additionally, we improve the Endpoint Detection and
Our approach starts with baseline threat hunting for suspicious
Response (EDR) system by refining detections and blocking
behaviors, using a structured attack flow model. This threat
IOCs, ensuring that the response targets specific threat
hunting plan is sequential and systematic, incorporating
actor behaviours. This not only blocks individual threats but
tools and techniques known to be used by ransomware and
also prevents further ransomware encryption and broader
other Cy-X groups or APTs. Our hunts span across various
attacks. Some EDR platforms also allow us to assess and
systems—ranging from specific EDR solutions to broader
prioritize potential vulnerabilities exploited by threat actors.
environments like network communication, logs, firewalls and
SIEM systems.
Once we’ve identified the specific procedures and MITRE
ATT&CK techniques in use, we convert them into YARA or
Sigma rules. These rules can then be applied across a variety
of systems, such as Cortex, Microsoft Defender, Splunk,
GoogleSecOps, Sentinel One, CrowdStrike and Elastic. We
either adapt existing queries from existing repositories or create
our own Sigma rules using David Bianco’s PEAK hypothesis-
driven methodology. This enables us to rapidly deploy effective
threat hunting across the environment and create detections if
they are unique, invariant and robust.
© Orange Cyberdefense 2024/2025

Expert Insight: Germany 97
Threat Hunting – Documentation and Further Steps
Tracking and Communication
After completing the threat hunting, we document all key
findings and provide a detailed record of each hunt we
During our threat hunting process, we carefully track each
conducted. We offer customized recommendations tailored to
hunt, documenting the execution time and any findings. If we
the customer’s environment. If we detect any potential security
find suspicious ports, processes, user behavior, or unwanted
issues, we collaborate closely with the customer to figure out
software, we promptly notify our customers to ensure rapid
whether they are false positives or true positives. This approach
improvements in their environment. Every hunt is mapped to
not only helps prioritize next steps for strengthening security
the MITRE ATT&CK framework and executed in a systematic,
but also enhances the customer’s understanding of their own
step-by-step manner, mimicking an actual attack.
infrastructure and tools.
We use baseline queries alongside newly created, specific
We also recommend conducting an M3TID (Maturity Model for
threat hunts designed to detect the tools and commands
Threat-Informed Defense)[181] assessment after the hunt. This
used by the threat group. Additionally, we examine related
assessment evaluates the maturity level of threat-informed
procedures within the MITRE ATT&CK framework to identify
defense across people, processes, and technology. Based
similar behaviors from other ransomware groups. For example,
on the findings, we provide recommendations to improve
we search for hacking tools or remote monitoring tools known
the customer’s infrastructure and security posture, helping
to be used by other threat actors with high prevalence.
to prioritize future security investments. Customers receive a
Best practices are applied to stop further lateral movement by separate briefing and documentation outlining their individual
blocking IOCs to detect and prevent suspicious behavior. We maturity scores and actionable recommendations.
also recommend customers block any tools commonly used by
Once threat hunts are created and executed, the queries can
ransomware affiliates if those tools are unnecessary within their
be saved in the EDR system, allowing customers to regularly
environment.
monitor for suspicious behaviour. This proactive approach
ensures continuous security checks and reduces the risk of re-
victimization. We recommend performing these checks more
often after an incident to prevent worst-case scenarios in case
of being attacked again.
Key Takeaways
Threat hunting is an ongoing, iterative process that should be
integrated into both the incident response plan and overall security
strategy. Like the testing and evaluation of threat actors and their
real-world behaviours, it requires continuous attention. Rather than
treating it as a one-time compromise assessment following a forensic
investigation, threat hunting should be a proactive method to prevent
threat actors from exploiting vulnerabilities unnoticed.
This approach enables rapid improvement, helping to maximize, mature, and measure the success
of security investments and overall security posture. A continuous threat hunting development
plan can be as effective as continuous testing, and when combined, these efforts ensure a deeper
understanding of your environment while naming defensive gaps. Knowing the adversary is one
aspect, but truly countering and understanding their behaviour is essential for a resilient defense.
www.orangecyberdefense.com

98 Security Navigator 2025
Emmanuelle Bernard
Mobile Network Security Expert
Orange
Stéphane Gorse
Senior Security Expert
Orange
Sébastien Roché
Corporate Internal Auditor / Senior Security Expert
Orange
Research: Mobile Security
Carriers,
Networks and Security
Mobile phones are essential tools in modern society, thanks to ▪ In January 2024, an attacker accessed Orange España’s
fast, affordable data making internet access convenient beyond infrastructure by compromising an employee account
Wi-Fi. Mobile networks, a remarkable engineering feat, support lacking MFA, with credentials obtained through
reliable, simultaneous wireless communication for hundreds or malware[186].
thousands of devices, with interoperability allowing seamless ▪ In March 2024, SS7 and Diameter vulnerabilities were
network access when traveling abroad. reportedly exploited to track individuals and intercept
Behind this ease of use lies complex technology, and with calls and texts, with potential abuse of the GSMA
complexity comes vulnerability. Intelligence agencies have Global Title feature, previously linked to NSO Group and
long been aware of these weaknesses, and criminals are
Intellexa[187][188].
increasingly exploiting well-known flaws. We previously ▪ In August 2024, the UK National Crime Agency revealed
raised concerns about managing vulnerabilities in enterprise that three men were sentenced for running an OTP-
mobile phone estates, predicting that as mobile phones stealing service, “OTP Agency.” This service phished
become central to enterprise security, criminals will adopt One Time Pins (OTPs) by calling victims and warning of
advanced hacking tactics to bypass controls like Multi-factor unauthorized account activity, prompting them to provide
Authentication. OTPs[189], which were then relayed to criminals.
In previous Security Navigators, we predicted that ▪ In September 2024, authorities arrested 17 suspects linked
mobile device attacks would increase as these devices to an international network using the “iServer” phishing-as-
become integral to personal, business, and cybersecurity a-service platform to unlock stolen or lost phones.
infrastructures. While sophisticated, targeted attacks on high- ▪ In October 2024, reports emerged that “Salt Typhoon”
profile individuals by private firms contracted to governments breached several major US telecom providers, allegedly
have intensified[182], we have not seen a significant rise accessing systems related to lawful communication
in vulnerabilities or exploits affecting mainstream mobile interception and other infrastructure areas[190][191].
platforms. However, there have been notable cases of mobile
In this chapter, we will pull the curtain back on the security
network infrastructure abuse—a topic we address for the first
risks associated with mobile phone networks. We’ll discuss
time in this report.
how mobile networks have evolved over the past two decades
and how technology has adapted to address emerging threats.
For example:
▪ In May 2024, UK police arrested two suspects for using Note: we use a lot of acronyms in this chapter. You can find
detailed explanations of these in the appendix on page 112.
a “homemade mobile antenna” to send phishing texts
directly to mobile phones, bypassing network protections
that typically block such messages[183]. The Mobile
▪ In early 2023, reports in Île-de-France described criminals Telecommunication Ecosystem
driving with IMSI catchers to send fraudulent texts[184].
▪ In September 2023, a man was arrested and charged with Mobile networks like Orange are operated by
espionage in Oslo for driving with an IMSI-catcher around telecommunications companies, but the underlying network
the office of Norway’s Prime Minister, the Defense Ministry functions are provided by network vendors like Ericsson, Nokia,
and other government buildings[185]. and Huawei.
© Orange Cyberdefense 2024/2025

Research: Mobile Security 99
The secure deployment and operation of a mobile network Established to support the standardization and interoperability
depends largely on the operator’s strategy, but is heavily of mobile networks, GSMA develops industry guidelines,
influenced by each vendor’s ability to meet these strategic promotes collaboration, and advocates for policies that foster
requirements. the growth and security of mobile communications.
The 3rd Generation Partnership Project (3GPP) is an It also develops key initiatives on security, IoT, 5G, and digital
organization that brings together several standards bodies identity. The GSMA continually enhances the security support
to develop protocols for mobile telecommunications. 3GPP offered to the telco community as the threats targeting the
standards are designed to ensure interoperability between mobile ecosystem evolve[192].
networks and network functions across different vendors.
The European Union Agency for Cybersecurity (ENISA) is
However, 3GPP does not specify all security mechanisms for
the EU’s agency dedicated to improving cybersecurity across
a network; it only defines those required for interoperability,
member states, including in mobile network security. ENISA
such as mobile authentication using SIM credentials. Security
provides strategic guidance, policy recommendations, and
features available in network functions can vary significantly by
technical standards to enhance the resilience and security
vendor, which is a key differentiator in the market.
of critical infrastructure like mobile networks. Through
The GSM Association (GSMA) is a global organization collaboration with national cybersecurity authorities, mobile
representing the interests of mobile network operators operators, and industry stakeholders, ENISA plays a pivotal
and companies in the mobile ecosystem, including device role in strengthening defenses against threats within the mobile
manufacturers, software providers, equipment vendors, and sector.
internet companies.
Support/Best
practices
Overall Security Level
Security
Operators
Requirements
End Users
Telco Suppliers: Standards
The security level
in mobile networks
Ericson,
varies widely, as
it depends on the Nokia, Huawei,
commitment of many TM
Oracle...
stakeholders, and
security features are
often optional.
www.orangecyberdefense.com

100 Security Navigator 2025
Mobile Telecommunications History In 2G, most reported attacks resulted from weak encryption
algorithms (known as A5/1) on air interfaces, leading to possible
Launched in the 1990s, 2G or GSM (Global System for Mobile “Attacker in The Middle” attacks. Tools like “IMSI Catchers" (or
Communications), marked the transition from analog to digital fake base stations) were used to mimic cell towers, allowing
telephony[193]. This technology introduced basic services such attackers to capture communications from unsuspecting users,
as voice calls and SMS. To support mobility of mobile users or send them SMS.
across networks and even international roaming, SS7[194][195]
In 2G and 3G, SS7/MAP was unauthenticated and unencrypted
protocol called MAP was introduced. MAP operates within
on interfaces between operators, allowing for data theft and
the SS7 framework, using SS7’s signaling to enable mobile-
denial-of-service attacks. As roaming was initially designed
specific functions across telecommunications networks.
within a “trust” relationship between operators, security was
3G – Universal Mobile Telecommunications System – was not considered in the SS7 protocol.
introduced in the early 2000s. It offered significantly higher data
Later, as 4G networks began to roll out, vulnerabilities in
speeds and enabled mobile internet access[196]. SS7 was used
the Diameter protocol were exploited[202]. Attackers could
again in 3G for core network signaling.
manipulate signaling messages to gain unauthorized access to
In 2010, 4G, or LTE (Long Term Evolution) was launched, user data or to disrupt services.
revolutionizing mobile connectivity with significantly improved
The 5G core network is virtualized and API-based, so the
download and browsing speeds[197]. 4G introduced a new
attack surface is also increasing and 5G networks still rely on
protocol called Diameter[198] for signaling exchange between
4G infra when 5GSA is not deployed. Threats such as software
core network functions.
supply chain attacks (e.g. via 3rd party dependencies), attacks
Currently being deployed worldwide, 5G promises even faster targeting critical infrastructure, and distributed denial of service
speeds, reduced latency, and the ability to connect a much attacks via IoT device vulnerabilities (like Mirai), all exacerbate
larger number of devices simultaneously. 5G uses advanced this threat.
technologies like Massive MIMO (Multiple Input Multiple Output)
In one 2020 report, for example, researchers from Positive
and beamforming. In the core network, HTTP/2 replaces
Technology cautioned that “Vulnerabilities in the GPRS
Diameter, and network functions now expose to other network
Tunnelling Protocol (GTP) expose 4G and 5G cellular networks
functions via API – whether in the same network or in a partner
to a variety of attacks, including denial-of-service, user
network for roaming[199][200][201].
impersonation, and fraud”[203].
New Tech, New Threats
The mobile operator ecosystem has evolved significantly over
the last 30 years – from 2G to 5G - and the attack surface has
evolved with it. As new generations of mobile technology are
deployed on top of older generations, not in place of them, the
risk continues to accumulate.
High Level View of the Attack Surface for Mobile Telecommunication
5G
4G
2G
3G
Attack
Attack surface #3.1:
Attack Attack surface #3: Interconnection
surface #1: surface #2: Mobile of Mobile
SIM Device Infrastructure Infrastructure
©© OOrraannggee CCyybbeerrddeeffeennssee 22002244//22002255

Research: Mobile Security 101
The Mobile Attack Surface With the OTP, the fraudsters logged into the app and initiated
SIM swaps on the victims' phone numbers. These swaps were
The mobile network attack surface emerges across 3 distinct primarily executed outside of working hours to avoid detection.
domains:
This specific incident affected at least 14 different phone
1. Universal Integrated Circuit Card (UICC)/SIM
numbers. Customers experienced unauthorized SIM swaps,
2. Device
leading to potential breaches of personal information
3. Infrastructure
and disruption of mobile services. Some customers even
terminated their contracts out of fear of being hacked again.
SIM
The situation prompted quick decisions and actions by the
SIM cards are vulnerable to various threats. For example, a operator’s security and fraud teams. Including:
fraudster can take over a bank customer’s telecom subscription ▪ Informing the authorities.
by misappropriating their SIM card. By doing so, the fraudster ▪ Blocking eSIM functionality via the provider's app.
gains control of the “possession” authentication factor,
▪ Improved Know Your Customer (KYC) measures to prevent
enabling access to the victim’s accounts when combined with
further incidents.
stolen personal data. This technique can be applied not only to
banking applications but also to any other applications on the Additionally, there were discussions about updating message
mobile phone, such as social media. Three primary methods templates to include warnings that the provider would never
are commonly used: ask for the OTP code.
SIM Swap The incident outlined above is not an isolated case. As the
chart below illustrates, over 30 days during May 2024, one
A SIM swap occurs when a fraudster requests the operator to
European operator recorded 110 fraudulent eSIM swaps and
produce and activate a new SIM card. Once activated, the new
337,000 fraudulent SMS messages.
SIM renders the original SIM inactive, causing the legitimate
subscriber to lose access to the mobile network and their
Fraudulent eSIM swaps
online services.
over time at one European operator
Portability
In this method, the fraudster uses the subscriber’s Number
Transfer PIN (NTP) to request outbound portability with a
different operator. The new operator then issues a new SIM 10
card for the transferred number.
Cloning
Cloning involves physically replicating a SIM card. Although
5
technically complex and rarely used for fraud today, research
has shown that it is possible to extract secret credentials from a
SIM card via side-channel attacks, even with physical security
modules in place[204][205].
0
May 2024 June 2024
Not so eSIMple
The shift to eSIMs introduces new fraud risks rather than
eSIM technology is also susceptible to fraud. Although the
eliminating them.
provisioning process is generally secure, the user controls
activation, creating an opportunity for phishing or smishing A recent University of Aalto study outlines over 12 root causes
attacks. Through these tactics, fraudsters can obtain of eSIM fraud and hacking, highlighting common vulnerabilities
credentials or one-time passwords (OTPs) used in the like phishing, smishing, caller ID (CLI) spoofing, and brute-force
enrolment process. attacks. Once hackers obtain a victim’s identity data, they can
exploit provisioning weaknesses to execute eSIM swaps. The
Case Study
study recommends implementing Know Your Customer (KYC)
In April 2024, a significant eSIM fraud incident was detected by solutions or temporarily blocking features until new anti-fraud
one of our European operators, involving multiple unauthorized tools are available. Vendors like Thales, Nokia, and Ericsson are
eSIM swaps. developing solutions, but current monitoring capabilities are
limited, requiring further investment and regular updates.
The fraud was initially flagged due to an unusual activity
involving eSIM swaps. Specifically, multiple swaps were For end-users, a compromised eSIM profile gives hackers
performed using the same device IMEI, which raised a red flag. control over the victim’s phone number, facilitating financial
fraud and bypassing two-factor authentication (2FA) for banking
The fraudsters employed social engineering techniques to
and other sensitive accounts. Hackers can also duplicate eSIM
deceive victims. They contacted the victims, pretending to be
profiles for identity theft. For operators, eSIM fraud threatens
representatives from the mobile service provider.
revenue and reputation, increasing the need for audits of eSIM
During the call, they generated an OTP (One-Time Password) and IoT B2B services and heightening GDPR compliance risks.
for the provider's app and convinced the victims to share this Operators face recurring costs to enhance fraud protection as
code. technology evolves.
www.orangecyberdefense.com

102 Security Navigator 2025
The Device Itself Google’s review processes may also be less strict than Apple’s,
and unofficial Android app stores adding further risks. Android
Modern mobile phones operate like powerful computers, users can also sideload apps. This feature, often exploited by
running operating systems and applications while connecting trojans, poses a major risk, particularly as alternative app stores
via mobile networks, Wi-Fi, Bluetooth, NFC, and even usually lack robust security.
satellite networks. As we reported in 2021, 547 vulnerabilities
While currently Android-only, iOS is expected to allow
were identified in Android and 357 in iOS, with 18 Android
sideloading in the EU by 2024 (starting with iOS 17) to meet EU
vulnerabilities rated critical, compared to 45 for iOS. This
regulations, potentially introducing new security challenges for
suggests Android has more vulnerabilities but fewer severe
Apple users.
ones, while iOS is harder to exploit yet offers greater reward.
Android exploits are widely used across devices, whereas
iOS exploits are often associated with sophisticated mobile Infrastructure
surveillance actors.
The attack surface in mobile infrastructure has expanded
Apple’s consistent ecosystem means iPhone users are
significantly with the advancement of mobile technology. A
more vulnerable when flaws are disclosed, though updates
quick overview of this complexity is provided below[206]:
are quicker, with 70% upgrading within 51 days. Android’s
fragmented system leaves older devices exposed to older The GSMA’s “Security Landscape 2024” report[207] highlights
vulnerabilities while somewhat protected from newer exploits. several critical areas of concern for the mobile telecommuni-
However, malware remains the most pressing threat for cations industry. Key points include the increasing frequency
everyday users. and sophistication of attacks on virtualized infrastructure, such
as virtual machines and container solutions. The report also
Both Apple and Android use dedicated marketplaces—the
emphasizes the vulnerabilities within supply chains, and the
App Store and Google Play—with security measures like app
growing issue of spyware.
reviews and sandboxing to limit exposure to malicious apps.
In 2022, Google Play had 781% more malicious apps than
the App Store, likely due to higher malicious submissions,
Android’s low-complexity vulnerabilities, and ready-made
exploits.
▪ Detailed view of the mobile network attack surface at infrastructure level
© Orange Cyberdefense 2024/2025

Research: Mobile Security 103
▪ Services identified on Dark Net related to signalling aspect
Pushing MFA Also increasingly popular, a dedicated MFA mobile app uses
push notifications provided by Google or Apple, a system
Given the inherent weaknesses in mobile network technologies, natively supported by Android and iOS [209][210][211]. In this model,
single-use passwords (OTP) sent via SMS, were deemed telecom operators are excluded from the process, which poses
insecure by NIST as early as 2016. Fraudsters have adapted to potential privacy risks for users, as Google and Apple retain the
bypass SMS OTP by using techniques like caller ID spoofing ability to collect usage data from backend interactions, even if
to impersonate banks, tricking customers into authorizing exchanges are encrypted.
fraudulent transactions.
More generally, third-party instant messaging and VOIP
Effective Multi-factor authentication (MFA) today therefore applications use the application layer to manage traffic
largely leverages two main methods for a second according to their own standards, with security and data
authentication factor beyond device possession: protection measures thus depending on the efforts and
success of the software vendor.
Third-party Authentication:
High value accounts such as banking often use their mobile
banking apps to provide a second factor via a PIN code
(knowledge) or smartphone biometrics (inherence).
Operator-Based Authentication:
An alternative method, standardized by GSMA as “Mobile
Connect”, uses SIM-based authentication and requires a PIN
code (knowledge). Sending OTPs via SMS is discouraged due
to vulnerability to SS7 rerouting attacks (as noted in NIST-800-
63B)[208].
www.orangecyberdefense.com

104 Security Navigator 2025
1 Notification
APNS
Cloud Messaging
Notification server
Application from Google or Apple
backend
n
A
n
p
ot
p
i
l
fi
i
c
c
3
a
a
t
t
i
i
o
o n
2
N oti fi c
ati o n
End user device
▪ Push notification channel
A Brief History Mitigations
Of Mobile Network Hacking
Defending the SIM
Intelligence Agency Exploits Mitigating SIM card vulnerabilities requires multiple strategies.
Mobile infrastructure has been a target for intelligence Operators should deploy GSMA-certified SIM cards with
agencies, with several incidents highlighting this fact since the a generic protection profile, and embedding a firewalling
2000s. For example: Java applet within the SIM can block unexpected external
interactions.
Mark Klein, a former AT&T technician, revealed his role in
exposing the U.S. National Security Agency’s (NSA) use of For SIM swaps, telecom operators like Orange have updated
AT&T’s infrastructure for mass surveillance. Klein revealed that customer processes with stricter controls. But SIM swap
the NSA had installed splitters to divert Internet traffic, allowing attacks often rely on social engineering, making customer
them to monitor communications without warrants[212]. awareness essential. Operators have also introduced APIs
allowing service providers to check if a SIM card was recently
The Greek wiretapping case of 2004–05 involved the
renewed.
illegal surveillance of over 100 mobile phones belonging to
high-ranking Greek officials, including the Prime Minister. Device manufacturers are also strengthening mobile security,
The surveillance was conducted through the exploitation implementing stricter controls in app stores and limiting API
of vulnerabilities in Vodafone Greece’s mobile network access for application developers to improve security.
infrastructure. The attackers, suspected to be state-supported
Solutions providing dynamic application analysis to detect
cyber threat actors, installed rogue software that intercepted
threats are now common, and mobile device management
calls and messages. This software exploited lawful interception
(MDM) systems are highly recommended for organizations to
capabilities meant for legal wiretaps, redirecting the data to
address major security risks.
unknown recipients[213].
Defending the Infrastructure
The Thales Group’s investigation[214] into the alleged hacking
of Gemalto’s SIM card encryption keys revealed significant Since security is not built into SS7/MAP and Diameter
vulnerabilities in mobile network. The breach, reportedly protocols, operators like Orange have implemented specialized
conducted by the NSA and GCHQ, involved the theft of protection solutions known as Signaling Firewalls. These
encryption keys, which allowed these agencies to intercept solutions provide key functions like Traffic Filtering, Anomaly
and decrypt mobile communications without the need for Detection, Protocol Validation, Access Control, Logging and
cooperation from telecom companies or legal warrants. Reporting.
Exploitation of these encryption keys enabled the attackers
One valuable feature for network security is “velocity checks,”
to bypass traditional security measures, gaining unauthorized
which prevent attacks by verifying that user mobility aligns
access to voice and data communications on a global scale.
with realistic speeds (e.g., not exceeding airplane travel). This
Vulnerabilities Exposed and abused rule helps detect and block attempts to impersonate a visited
network identity.
In 2016, researcher Karsten Nohl demonstrated[215] how to
intercept a voice call from a U.S. senator, following his 2014
Defending the Device
presentation at the Chaos Computer Club conference with
researcher Tobias Engel, where they exposed vulnerabilities Securing mobile devices against threats is challenging, as
in the SS7 protocol. Then in 2017, operator O2 confirmed that these devices are high-performance computers running
hackers targeted its network by exploiting SS7/SMS protocol complex operating systems. Like any computer, they require
weaknesses used in two-factor authentication. Combined with monitoring for malicious activity and malware.
phishing attacks, attackers managed to trigger money transfers
and redirect two-factor verification codes via SMS, resulting in
customer losses totaling approximately €200,000.
© Orange Cyberdefense 2024/2025

Research: Mobile Security 105
For individual users, solutions like antivirus software with added Passkeys are a replacement for passwords, always strong
services (e.g., personal fraud investigation) are available. In the and phishing resistant[216][217][218]. The Fast Identity Online
business sector, Mobile Device Management (MDM) systems (FIDO) alliance has published a specification that is based
like Checkpoint and Pradeo Mobile Threat Defense help protect on public-key cryptography where each passkey contains a
entire device fleets by collecting device data and enabling unique public/private key-pair. The passkey can be stored on
rapid mitigation. a dedicated hardware token or be integrated into a device that
supports the specification. Mobile devices such as Apple's
Attacks exploiting radio channels are harder to counter, as they
iPhone and Google's Pixel mobile phones are examples.
require access to the modem baseband, which is not available
Passkeys use the trusted relationship of the hardware and the
in standard consumer devices, necessitating specialized,
tightly bound identity of the user to facilitate authentication. The
hardened devices.
user uses the device to relay a cryptographically verifiable value
A good start for businesses may be to standardize on a mobile that cannot be faked.
device platform that can be trusted to be up to date and
monitored using a reliable MDM system. FiGHT or Flight
The MITRE FiGHT (5G Hierarchy of Threats) project is designed
Defending MFA
to identify and categorize potential security threats specific
In Europe, the Payment Services Directive 2 (PSD2), enacted to 5G networks and related technologies. FiGHT provides a
in 2018, mandates strong customer authentication (SCA) for structured framework for understanding the unique risks within
digital transactions by financial institutions, particularly banks, 5G environments by mapping out threat scenarios across
to enhance security. various layers of the 5G infrastructure[219].
By implementing proprietary applications, banks comply with
PSD2 and can legally reject customer claims in commercial
disputes, excluding fraud cases. The directive’s revision
presents an opportunity for the European Commission to
reinforce banks’ financial accountability in fraud cases, even
when strong authentication has been applied.
The revised directive also introduces implicit responsibilities
for telecom operators if a spoofed call is involved in fraud,
including caller ID spoofing (fake calls), sender ID spoofing (fake
SMS), or SIM-based actions (SIM swap, number portability, or
cloning).
Summary
In previous reports we have raised concerns But it is constantly evolving, and we continue to
about the challenges of managing vulnerabilities caution our clients that the challenge of mobile
in enterprise mobile phone estates. As mobile threat management must be considered in
phones assume a critical role in the enterprise medium-term security strategy considerations.
security stack, we postulated, criminals would
begin to adopt more sophisticated hacking Meanwhile, the mobile infrastructure is itself at
techniques to exploit phones and thus bypass risk; and Orange is proud to be a leader in this
controls like Multi-Factor Authentication. domain.
We have yet to see this threat emerging outside Mobile services are part of any CISOs attack
the world of targeted, state-sponsored espionage surfaces. There is a gradual shift in temperature,
operations. and the issue of mobile is increasingly finding its
way onto corporate risk registers.
The issue of mobile phone security has not yet
reached its zenith.
www.orangecyberdefense.com

106 Security Navigator 2025
A Hierarchy of Needs
Incident response readiness: Where to begin
It is quite the experience to sit across from a person – usually a CISO or an IT Security Manager – that
has not slept in days, and to be asked: “how can we stop this from ever happening again?”. Perhaps
we had spent the last two days containing a threat actor that had exploited an unpatched VPN
appliance and penetrated deep into the infrastructure. Or maybe it was the worst-case scenario: this
person’s entire infrastructure had been ransomwared, and there were no backups to rely upon. In all
these cases, my answer would be: “We can’t – but here’s how we can react better next time”.
The reality is that a cybersecurity incident is a matter of when, and not if. Organizations unwilling to
face this reality will be caught unprepared again. Incident response readiness is a complex beast, with
various areas of concern demanding attention. So where do we start?
Saskia Kuschke, Senior CSIRT Analyst, Orange Cyberdefense
Your Hierarchy of Needs A Roadmap for Response Readiness
A simple starting point may be the “Incident Response Part of the difficulty of organizing effective incident response is
Hierarchy of Needs” model, from the mind of Matt Swann[220]. because the building blocks are a mix of organizational, people,
process and technological considerations. To make the original
Similarly to Maslow’s hierarchy, the model depicts several
Hierarchy model more concrete, and taking these building
needs in the original diagram – inventory, telemetry, detection,
blocks into account, our CSIRT has developed a “roadmap” of
triage, threats, behaviours, hunt, track, act, all coming to a point
where to start on the journey to incident response readiness.
in collaboration. Each tier depicts a deceptively straightforward
For illustrative purposes, a simplified representation of this
question that - depending on the organization’s policy, budget,
roadmap is in the diagram below.
risk appetite and culture - likely has a complicated answer.
However, this way of ranking “needs” may present a simple and The reasoning behind the roadmap is simple: be practical.
practical way to prioritize your efforts. Each tier builds upon Complexity is the enemy during an incident, and many of the
the previous: for example, with a better view on your inventory preparatory activities on the road to IR readiness involves
position, you gain a better understanding of your coverage reducing ambiguity as far as possible in the decision-making
needs in terms of telemetry and visibility – and better telemetry process. To measure the distance travelled in the IR readiness
leads to increased detection opportunities (and so on). One of journey, we make use of the capability maturity model
the criticisms of this model is that one can still perform incident integration (CMMI) model as a guideline[221]. At each phase, one
response even if all the tiers do not have adequate controls – must consider the people, process and technology needed to
as such, it useful to recognize that while you do not need to achieve the goal.
finish off the entire tier before moving to the next, the activities
This is a good time to quote famous statistician George E.P
described higher up in the pyramid become significantly
Box: “All models are wrong, but some are useful”. In the spirit
smoother if you have invested in a solid prior foundation.
of this sentiment, take this diagram as a suggestion on how to
As far as models go, this simple breakdown of identifying structure and measure the journey of maturity, rather than a
“needs” can be an effective starting point in the journey concrete mapping of phases and absolute truths. In practice,
towards being incident response-ready in time for the next you will likely find yourself moving back and forth between the
attack. But if it is this simple, then why does our CSIRT still various tiers and associated activities, rather than having the
encounter multiple organizations that seem to struggle with luxury to complete all in sequential order.
even the foundational tiers?
‘Break-glass’ procedure 1. Initial
Can you name the assets you are defending? Inventory 2. Managed
Do you have visibility across your assets? Telemetry
Can you detect unauthorized activity? Detection 3. Defined
Can you accurately classify detection results? Triage
Who are your adversaries? What are their capabilities? Threats
Can you detect adversary activity within your environment? Behaviors 4. Quantitatively Managed
Can you detect an adversary that is already embedded? Hunt
During an intrusion, can you observe adversary activity in real time? Track
Can you deploy proven countermeasures to evict and recover? Act 5.Optimizing
Can you collaborate with trusted partners to disrupt adversary campaigns?
© Orange Cyberdefense 2024/2025

Expert Insight: Netherlands 107
1. Ready Your Fire Extinguisher 4. Conduct Your Fire Drills
In the Initial phase, it is about making sure you have a fire Reaching the quantitatively managed level means that you have
extinguisher that you know how to operate – in other words, a good grasp of your break-glass processes, environment and
addressing the very basics of incident response. Do you know information position available to you during an incident. This
who is responsible for what during an incident, and who needs is an ideal point to focus efforts into conducting “fire drills”
to be called and informed? Further still, do your operational and measuring the efficacy of your IR capability in the vein of
teams understand how to collect data from endpoints, how to tabletops and assessments. While continuous testing can (and
perform emergency firewall rule changes? And can all of this be should) be used to measure your response throughout the
recalled and performed under pressure? Examples of elements IR readiness journey, these activities will likely start revealing
to have in place are: less “obvious” improvements to be made at this point. In this
▪ Process, People: An IR plan clearly listing roles &
maturity phase, your capability should also be controlled
enough to dive into the more proactive parts of your “needs”
responsibilities assigned to specific individuals.
– such as the incorporation of strategic and operational cyber
▪ Process: Communication plan during an incident. threat intelligence (CTI) and proactive threat hunting to identify
▪ Process: Playbooks for containment and data collection threats and malicious behaviors directly relevant to your
(e.g. emergency firewall changes, endpoint isolation, organization. Consider:
running forensic collector software on affected systems). ▪ People, Process: tabletop exercises to test specific
elements of the IR process.
2. Map Your Environment ▪ Technology: assessments of configurations of security
tooling and related systems.
With the essentials in place, you can now tackle the challenge
▪ People, Process, Technology: proactive, continuous
of mapping your environment to progress towards the
CTI-driven threat hunting.
managed level, which aligns with the Inventory tier: where
are your assets, and what are your critical systems and data? ▪ People: additional training for personnel where gaps
Which systems are vital for your business, and how are they are identified.
configured? Are any internet-facing? Many clients struggle
with mapping and maintaining infrastructure knowledge 5. Iteration And
as environments grow in complexity. However, a thorough
Continuous Improvement
understanding of your setup is crucial for a stronger incident
response. Consider: And finally, the coveted Optimizing phase, where your
▪ Process, Technology: Creating & maintaining asset lists processes, people and technology are well-oiled enough so
(automated, where possible). that any improvements are essentially incremental instead of
▪ Process, Technology: Creating & maintaining IT instrumental. Tuning policies, designs and tooling to ensure that
tracking, acting and collaborating during an incident can run as
architecture documentation (e.g. network diagrams, cloud
unhindered as possible by preventable issues and poor starts.
architecture diagrams, Active Directory topology).
Here your focus may include:
▪ Process, People: Documenting system owners and how
▪ Process: Maintaining a robust lessons-learned cycle.
to contact them (especially out of hours).
▪ Technology: Understanding and mapping software and ▪ Process: Tuning and creating IT security policies.
configuration vulnerabilities. ▪ Process, Technology: Improving the design of your IT
infrastructure.
3. Tune Your Smoke Detectors
Once you understand your key systems and pressure points,
ensure you have the telemetry, detection, and triage capabilities
to assess activity on them. This defines the "defined" level:
knowing the completeness, accessibility, accuracy, and
retention of your data. First responders, analysts, and decision-
Key Takeaways
makers need information to identify threats, enact containment,
or even shut down the network if necessary. Logs, SIEM,
and EDR/XDR data are vital here, and knowing what data In our CSIRT’s experience, incident response is
is retrievable (even under pressure) is crucial for mastering something that improves via iteration – every incident
incident response. Considerations may include: you survive makes you better equipped for the next
▪ Technology: available log sources & forwarding to one, provided you put in the effort to learn from the
encounter. Preparing as best you can prior to an
centralized repository (e.g. to a SIEM).
incident puts you in an optimal position to fully leverage
▪ Technology: EDR/XDR coverage and capability.
this experience to identify what your organization needs
▪ Technology: detection engineering and monitoring use the most, at whatever maturity level you find yourself
cases configured for your available telemetry. occupying.
▪ Process: tuning your event & incident classification
frameworks to better suit your organization. Break your problem areas down into people, processes
▪ People: personnel trained to monitor, triage and analyze and technology, and prioritize your solutions and
mitigations in a way that supports the work to come.
data, events and alerts using security tooling.
Above all: be practical and be prepared, so that when
▪ Technology: data quality in terms of accuracy,
we reach the end of an incident, you are the one telling
completeness, coverage, accessibility & retention
me what your organization will do better
timeframes.
next time.
www.orangecyberdefense.com

108 Security Navigator 2025
© Orange Cyberdefense 2024/2025

Security predictions 109
Tatiana Chamis-Brown
SVP Global Strategic Marketing
Orange Cyberdefense
Vivien Mura
Global CTO
Orange Cyberdefense
Security predictions
A story of
Convergence,
Intelligence And
Resilience
Join us once more as we take a step back and try to predict how the big
picture presents itself and where the trends are going.
What will shape the digital world in the year to come? Which threats
should we prepare to face and how should we go about it? What will be
the major trends and tendencies our industry and others?
This year we will focus on five key trends we believe are going to be
relevant in the field of cybersecurity and associated risks.
www.orangecyberdefense.com

110 Security Navigator 2025
Apts Will Not
Leave Room for
Ransomware
The landscape of cyber threats is becoming increasingly Critical vulnerabilities discovered in security equipment
complex, with a notable rise in extortion victims, often are indeed exploited for this purpose. Advances in
compromised and subsequently threatened with a data quantum computing pose an additional risk to data
leak multiple times, often with the same set of stolen encrypted with current algorithms. The migration to
data. This escalation is not merely a trend; it reflects a quantum-resistant cryptographic systems will take time
broader shift in the tactics employed by cybercriminals, and must begin as soon as possible to account for the
who exploit sophisticated methods to achieve their retroactive effect of a future quantum threat on today's
goals, increase their resilience, and impose fewer moral encrypted communications.
or geographical limits on themselves. Disinformation
Furthermore, global outages triggered in 2024 by a
on the web is integrated into destabilization methods to
faulty update of Crowdstrike's Falcon solution remind us
amplify pressure on victims, and drastically improved
of the fragility of the digital space in the face of systemic
impersonation capabilities through generative AI allow
crisis risks, which could be caused by attacks on
for deception of even the most discerning individuals.
software maintenance chains. This type of attack is not
In this already concerning context, the conduct of new; numerous cases have been reported in the press
more discreet attacks, involving the infiltration of (NotPetya in 2017, SolarWinds in 2020, Kaseya in 2021),
information systems for espionage or to prepare for and the hyperconnectivity of physical assets (OT, IoT)
future aggressions, must remain on the defender's only increases the attack surface.
radar. In 2024, the accidental discovery of a backdoor
methodically introduced over several years into a
component of Linux systems (XZ utils, openssh)
highlights the determination of major powers to occupy
strategic positions in cyberspace without being
detected.
© Orange Cyberdefense 2024/2025

Security predictions 111
Generative AI
Boosts Automation
A Matter of Time In the future, we can expect generative AI systems
to become more interconnected with the rest of
The distance between the attacker and the defender the digital landscape, with increasingly elevated
is often temporal: the attacker has the advantage of action privileges (bank transactions, control of
surprise, forcing the defender to equip themselves physical systems, etc.). Securing this chain often
and prepare to react as quickly as possible whenever involves implementing traditional and proven
a vulnerability appears, or a security event arises. In security measures and solutions. However, certain
these circumstances, automating detection, alerting, characteristics unique to AI systems require
and response mechanisms (CyberSOC, SOC, CERT, adaptations of existing security products and
and VOC) allows for time savings that can make specifically trained expertise. Nonetheless, the
a difference in remediating critical vulnerabilities conveniences offered by new AI technologies should
and resolving incidents. This is why the significant not lead us to neglect data protection aspects.
advancements in artificial intelligence algorithms Typically, no software code generated by a virtual
present an opportunity to support the automation of assistant should escape secure development
services, thereby increasing the speed and quality of practices, and no ChatBot solution should be
our cyber defense. deployed without risk analysis and security measures.
Finally, social engineering techniques are greatly
Maintaining Control of Security
facilitated by generative AI, allowing criminals of all
levels to perfectly imitate a person's style, voice, or
The widespread use of generative AI solutions to
appearance. Therefore, we can expect a surge in
assist humans in handling increasingly complex tasks
fraud and scams in the coming months and years,
also expands the attack surface across a new value
which will require an adaptation of digital offerings to
chain: training databases, consultation data, prompts
better protect society.
and responses, LLM hosting infrastructures, RAG
systems, generative AI models, etc.
www.orangecyberdefense.com

112 Security Navigator 2025
The excellent preparation of the stakeholders involved in the
2024 Olympic Games has paid off: despite numerous security
events, the overall increase in security levels and operational
rigor have helped avoid a crisis. This outcome proves that Regulations:
security can be successful and that sufficient investment can
The More
protect against the worst. This is why regulations regarding
the protection of digital assets are strengthening.
Compliant,
From Theory to Practice the Better
Prepared
The year 2024 is pivotal in the European regulatory
landscape. First, the implementation of the NIS 2 directive in
member states expands the regulated scope to many entities,
categorized by their criticality into important and essential
entities. The directive aims to better protect small and
For example, these vulnerabilities can be exploited to
medium-sized enterprises, which are particularly affected by
orchestrate massive denial-of-service attacks or to steal
cybercrime (as evidenced by the Security Navigator figures).
valuable data, whether personal, strategic, or characteristic of
In effect since 2023, the DORA directive complements NIS2
intellectual property.
by specifically targeting the financial sector to enhance the
resilience of operators against threats.
Lernaean Hydra
Finally, the recently adopted Cyber Resilience Act by the
Additionally, there has been an increase in arrests and
Council of the European Union aims to raise the security level
dismantling of cybercriminal members and networks, thanks
of many digital products marketed in the European market,
to effective international collaboration, as recently seen with
based on their criticality.
the LockBit group. While law enforcement interventions are
Indeed, products with digital components can introduce commendable as they hinder the activities of mafia groups
vulnerabilities into uses or information systems that pose and sometimes recover seized data, the organizational model
cyber risks with economic and societal impacts. of cybercrime makes it particularly resilient, and we should
expect it to continue growing.
Resilience for larger organizations requires third-party
Resilience 2.0 contingency and incident response plans. Moreover,
larger organizations can increase their own resilience
by sharing best practices across their supply chain to
lift their capabilities, especially to SMBs.
Effective risk management has for some time involved
more than investment in prevention and protection – it
also needs deliberate investment on back-up, response
With only a few days to the opening of the Paris and recovery for resilience.
2024 Olympics, it was not a cyber attack that We see this shift accelerating in the year ahead given
caused significant disruption across the world. The events of 2024, with increased investment on crisis
CrowdStrike update of Friday, 19. July highlighted the management training and drills, recovery strategies
perils of concentration and supply chain risks, and the and solutions, third-party risk management and best
importance of a robust back-up and recovery plan. practice sharing.
In parallel, the Security Navigator 2025 report highlights And though automation boosted by AI is here to stay,
an increase of 15.29% in cyber extortion victims, IT systems are not fully autonomous. The capability
notably SMB victims increased by 62%. This is to confirm an anomaly, declare a crisis, implement an
especially concerning as many larger organizations incident response plan and manage impacts across
depend on SMBs in their supply chain. These smaller the direct scope of the organization are all powered by
organizations often lack advanced cybersecurity people. The human element remains a central element
practices, and due diligence of third party risks is not of the resilience equation.
infallible.
© Orange Cyberdefense 2024/2025

Security predictions 113
Many organizations suffer from so-called technology bloat. The problem stems not
only from the number of cybersecurity solutions adopted, but that these do not always
streamline. Consequently, in-house security teams are stretched, spending significant
time managing disparate tools that are not integrated, instead of deriving value
from this investment. This is aggravated by the fact that the cybersecurity vendor
ecosystem is characterized by a plethora of tools and technologies and a scarcity of Security ROI
skilled personnel to manage them effectively, according to Forrester[222].
in Focus
As security architecture matures, security leaders are increasingly undertaking
a critical review of existing solutions, identifying redundancies, gaps and under-
utilisation and pruning solutions that are not yielding value. In fact, Gartner[223]
estimates that 70% of organizations use 20% of the functionality of security products.
Improved security ROI may come from better utilising and integrating existing tools.
While Gen-AI may be leveraged to augment existing tools and bridge the resource
gap, many organizations are wary of further bloating their stack. Consolidation may be
a solution for some, though it does not necessarily entail adopting one single platform
and neglecting innovation. Partnering with a leading MSSP to bridge the gap is an
option to both derive further security ROI – via fusion of solutions, threat intelligence
enrichment and access to security experts that can deliver outcome-based services –
and to future-proof the security technology stack.
We believe ROI from security investments will be increasingly under scrutiny. Security
leaders will need to identify improvements and potential gains to secure buy-in for
further investments.
www.orangecyberdefense.com

114 Security Navigator 2025
Report Summary
What Have
Sara Puigvert
We Learned?
EVP Global Operations
Orange Cyberdefense
Essential Insights This involves equipping cybersecurity teams with monitoring
For CISOs, CTOs, and Security Managers tools to identify disinformation early and implementing rapid-
response protocols to counter false narratives effectively.
Security Navigator 2025 highlights critical cybersecurity trends,
It is paramount to protect high-visibility assets like public-
providing insights and strategic guidance tailored to address
facing websites and social media accounts, which Orange
the challenges faced by today’s CISOs, CTOs, and Security
Cyberdefense anti cybercrime teams work toward daily.
Managers. This year’s findings underscore how organizations
By managing public perception and maintaining a trusted
are increasingly exposed to aggressive cyber extortion (Cy-X),
information environment, organizations can mitigate the
sophisticated hacktivism, targeted Operational Technology (OT)
reputational damage that often accompanies these attacks.
threats, and the evolving demands of integrated threat and risk
management.
Operational Technology Security (OT):
Unique Risks for Critical Infrastructure
Cyber Extortion (Cy-X):
Growing Aggression and Targeted Attacks Operational Technology (OT) environments, which control
essential physical processes, are now vulnerable to cyber
Cyber extortion remains a pervasive threat, impacting
extortion and hacktivism, with attackers frequently using
organizations of all sizes and sectors, especially small and
techniques that specifically target OT systems. Unlike
medium-sized enterprises (SMEs). SMEs this year faced a
information technology (IT) systems, OT environments have
53% rise in ransomware incidents, and this year marks the
specialized requirements that make conventional cybersecurity
biggest ever ransom obtained by a ransomware group: 75
approaches inadequate.
million dollars were paid to Dark Angels. With the emergence
of AI tools designed specifically for fraud, extortion, and We highlight direct threats called “Category 2 attacks”, which
impersonation, AI has enabled an increase in the volume target OT directly and aim to interfere with physical processes.
and sophistication of extortion incidents across sectors. The The techniques tend to leverage existing, legitimate OT
impact of these attacks reaches beyond the immediate target, functionality, and are therefore very hard to detect or block.
with disruptions cascading through supply chains and posing We can’t simply copy the defenses we have for IT in an OT
risks to larger companies. We observe a growing cynicism as environment. Basic controls like network segmentation remain
criminals no longer avoid critical services like healthcare. essential, while more advanced practices like penetration
testing need to be carefully examined to ensure they add value
We need resilience-building strategies to counter these risks.
to OT.
This includes the implementation of robust recovery protocols
and reliable backup systems to reduce downtime and data loss
Evolving Threat and Risk Management:
after an attack. Our previous report[224] offers detailed guidance
A Shift Beyond “Vulnerability Management”
for CISOs.
With over 264,000 vulnerabilities cataloged globally, the load
Hacktivism and Cognitive Attacks: is impossible to manage. Moreover, threats like zero-day
A Rising Threat to Public Trust vulnerabilities in widely used products like Ivanti, Palo Alto, and
Cisco, continue to be exploited by actors reportedly backed
Hacktivism is still evolving from activism into destabilizing
by states like China[227]. 2024 has demonstrated that traditional
campaigns, often aligned with geopolitical conflicts like the
“vulnerability management” must evolve toward a dual
war against Ukraine, with a particular impact in Europe. In
strategy of threat-informed prioritization for publicly exposed
the Nordics, through a combination of distributed denial-
assets, combined with systemic risk reduction for internal
of-service (DDoS) attacks and disinformation tactics,
environments.
pro-Russian hacktivists have launched extensive attacks
targeting government services, critical infrastructure and other For large internal environments, we need to conceive
“symbolic” entities[225][226]. AI can be used to create fake news architectures that are immune to compromise via an individual
and digitally altered images as part of campaigns targeting system. This requires three strategies: firstly, minimizing attack
elections and eroding trust in democratic institutions. surfaces by removing unnecessary systems. Secondly, limiting
attack impact through robust segmentation and Zero Trust
Attackers increasingly target perception and trust through
architecture. Thirdly, defining and implementing appropriate
these “cognitive” attacks. These attacks aren’t technical
configurations, recorded in an asset inventory, and enrolled in
disruptions. They aim to manipulate public opinion, undermine
software management systems.
trust in institutions, and destabilize societal confidence.
To limit the spread of disinformation and safeguard institutional
credibility, the report recommends organizations prepare to
counter these “cognitive attacks”.
© Orange Cyberdefense 2024/2025

What Have We Learned? 115
Conclusion This means embracing not only technical solutions but also
cognitive defenses to safeguard public trust and prioritizing
As cybersecurity threats become more sophisticated and risk-informed management over sheer volume in vulnerability
unpredictable, today’s CISOs, CTOs, and Security Managers tracking. By adopting these approaches, security leaders can
stand at a pivotal crossroads. The cyber landscape demands transform challenges into opportunities for stronger, more
more than just defenses; it requires a proactive, intelligence- resilient infrastructures.
driven approach that anticipates and mitigates risks before
A strong security strategy requires adaptation and readiness to
they materialize. Cyber extortion, hacktivism, zero-day
address constantly evolving threats, supported by tools and an
exploits and OT-specific threats are no longer isolated issues
organization that can swiftly adjust to new circumstances.
but interconnected challenges that call for a cohesive and
adaptable strategy.
The path forward lies in building resilient organizations
equipped to protect, recover, and evolve in response to shifting
tactics and emerging vulnerabilities.
» The path forward lies in building resilient
organizations equipped to protect, recover, and
evolve in response to shifting tactics and emerging
vulnerabilities. «
Sara Puigvert, EVP Global Operations Orange Cyberdefense
www.orangecyberdefense.com

116 Security Navigator 2025
Terminology we use in the report
Glossary
Organizational Teams
CERT – Computer Emergency Response Team – produce threat intelligence and coordinate our response to critical
threats and vulnerabilieis
VOC – Vulnerability Operations Centers – deliver managed vulnerability scanning services for clients
CSOC – CyberSOC Operations Centers – deliver managed threat detection services for clients
SOC - Security Operations Centers – manage client security equipment like firewalls and VPN.
VERIS 4A Categories [p13]
Actors are entities that cause or contribute to an incident.
Actions describes what the threat actor(s) did to cause or contribute to the incident.
Asset describes the information assets that were compromised during the incident.
Attribute describes which security attributtes (CIA) were compromised during the incident.
Threat Actions [p13]
The Threat Action categories used in the VERIS framework consist of the following 7 primary categories:
Malware is any malicious software, script, or code run on a device that alters its state or function without the owner’s informed
consent. Examples include viruses, worms, spyware, keyloggers, backdoors, etc.
Hacking is defined within VERIS as all attempts to intentionally access or harm information assets without (or exceeding)
authorization by circumventing or thwarting logical security mechanisms. Includes brute force, SQL injection, cryptanalysis, denial
of service attacks, etc.
Social tactics employ deception, manipulation, intimidation, etc to exploit the human element, or users, of information assets.
Includes pretexting, phishing, blackmail, threats, scams, etc.
Misuse is defined as the use of entrusted organizational resources or privileges for any purpose or manner contrary to that
which was intended. Includes administrative abuse, use policy violations, use of non-approved assets, etc. These actions can
be malicious or non-malicious in nature. Misuse is exclusive to parties that enjoy a degree of trust from the organization, such
as insiders and partners.
Physical actions encompass deliberate threats that involve proximity, possession, or force. Includes theft, tampering, snooping,
sabotage, local device access, assault, etc.
Error broadly encompasses anything done (or left undone) incorrectly or inadvertently. Includes omissions, misconfigurations,
programming errors, trips and spills, malfunctions, etc.
Environmental not only includes natural events such as earthquakes and floods, but also hazards associated with the immediate
environment or infrastructure in which assets are located. The latter encompasses power failures, electrical interference, pipe
leaks, and atmospheric conditions.
Mobile Networks Acronyms [p96]
2G: The second generation of mobile networks, providing digital voice and basic data services with low-speed data transmission.
GSM: Global System for Mobile Communications, a standard developed to ensure compatibility between mobile networks
worldwide, widely used in 2G networks.
3G: The third generation of mobile networks, enabling faster data speeds and improved multimedia services over 2G networks.
SMS: Short Message Service, a text messaging protocol that allows brief text communication over mobile networks.
Air interface refers to the radio-based communication link between a mobile device (like a smartphone) and the cell tower (base
station).
© Orange Cyberdefense 2024/2025

Contributors, sources & links
SS7 (Signaling System No. 7) is a global telecommunications protocol standard used to enable communication between mobile
and fixed network carriers.
MAP (Mobile Application Part) is a key protocol within the SS7 suite, specifically responsible for handling mobile-related
services, like roaming, SMS, and subscriber data management.
A5/1 is an encryption algorithm used to secure voice and data communications over 2G GSM (Global System for Mobile
Communications) networks.
Diameter: A protocol that succeeded Radius to support authentication, authorization, and accounting in mobile networks, mainly
used in 4G and 5G.
MIMO: Multiple Input Multiple Output, a technology that uses multiple antennas at both transmitter and receiver to improve data
throughput and reliability.
HTTP/2: The second major version of the HTTP protocol, offering enhanced security and performance for web applications over
mobile networks.
IMSI: International Mobile Subscriber Identity, a unique identifier assigned to each mobile user, crucial for authenticating on
mobile networks.
3GPP: The 3rd Generation Partnership Project, a collaborative organization that creates technical standards for mobile
communications, including 3G, 4G, and 5G.
UICC: Universal Integrated Circuit Card, a smart card used in mobile devices to secure user identity, network access, and data.
SIM: Subscriber Identity Module, a card that securely stores information, like IMSI, to authenticate users on mobile networks.
eSIM: Embedded SIM, a digital version of a SIM card that is embedded in the device and can be reprogrammed remotely by
operators.
SIP: Session Initiation Protocol, a protocol for establishing and managing voice and video calls over IP networks, used in VoIP and
mobile network applications.
The Purdue Model [p80]
Level 5 Enterprise Network
Level 4 Business Planning/Logistic Network
Enterprise
Level 3.5 Demilitarized Zone (Historian, Jump Box, Patch/AV Server)
Operational
Level 3 Operations & Control (HMI, Engineering Workstation, Historian)
Technology
Level 2 Supervisory Control (HMI, Engineering Workstation)
Level 1 Basic Control (PLC)
Cell/Area Zone
Level 0 Process (Sensor, Actuator)
ZMD
117
The Purdue Enterprise Reference Architecture
www.orangecyberdefense.com

118 Security Navigator 2025
Contributors, Sources & Links
Sources
This report could not have been created without the hard work of many researchers,
journalists and organizations around the world. We’ve gratefully used their online
publications for reference or context.
Sources/links
[1] https://www.bbc.com/news/articles/cz04m913m49o
[2] https://www.reuters.com/world/middle-east/israel-planted-explosives-hezbollahs-taiwan-made-pagers-say-sourc-
es-2024-09-18/
[3] https://therecord.media/south-africa-national-health-laboratory-service-ransomware-recovery
[4] https://www.techtarget.com/searchSecurity/news/366614476/Fortinet-discloses-critical-zero-day-flaw-in-FortiManager
[5] https://blogs.microsoft.com/on-the-issues/2024/07/30/protecting-the-public-from-abusive-ai-generated-content/
[6] https://www.dhs.gov/sites/default/files/2023-09/23_0913_ia_23-333-ia_u_homeland-threat-assessment-2024_508C_
V6_13Sep23.pdf, page 14
[7] https://www.orangecyberdefense.com/global/blog/research/from-cyber-aware-to-cyber-judgement-how-cisos-can-use-the-
aida-marketing-model-to-drive-change
[8] https://www.gartner.com/en/newsroom/press-releases/2020-09-14-gartner-security---risk-management-summit--day-1-high
[9] https://www.cyentia.com/why-your-mttr-is-probably-bogus/
[10] https://www.cisa.gov/securebydesign
[11] https://www.cybersecuritydive.com/news/microsoft-security-debt-crashing-down/714685/
[12] https://www.ivanti.com/blog/our-commitment-to-security-an-open-letter-from-ivanti-ceo-jeff-abbott
[13] https://cwe.mitre.org/data/definitions/1000.html
[14] https://cwe.mitre.org/data/definitions/707.html
[15] https://cwe.mitre.org/data/definitions/664.html
[16] https://www.nationalcrimeagency.gov.uk/the-nca-announces-the-disruption-of-lockbit-with-operation-cronos
[17] https://slcyber.io/a-timeline-of-events-operation-cronos-and-lockbit/
[18] https://www.europol.europa.eu/media-press/newsroom/news/lockbit-power-cut-four-new-arrests-and-financial-sanctions-
against-affiliates
[19] https://www.orangecyberdefense.com/global/offering/managed-services/threat-and-risk-management/world-watch
[20] https://cloud.google.com/blog/topics/threat-intelligence/information-operations-surrounding-ukraine
[21] https://therecord.media/polish-anti-doping-agency-polada-hack-leak
[22] https://dfrlab.org/2024/08/01/russia-linked-operations-target-paris-2024-olympics/
[23] https://www.newsguardtech.com/special-reports/2024-paris-olympics-misinformation-tracking-center/
[24] https://harfanglab.io/insidethelab/doppelganger-operations-europe-us/
[25] We choose not to name these groups as we believe they benefit from excessive publicity.
[26] https://socradar.io/what-is-ddosia-project/
[27] https://news.liga.net/ua/politics/news/sait-liganet-bulo-zlamano-nevidomi-opublikuvaly-rosiisku-dezinformatsiiu-pro-avdiivku
https://www.welivesecurity.com/en/eset-research/operation-texonto-information-operation-targeting-ukrainian-speak-
ers-context-war/
https://informnapalm.org/en/website-networks-in-europe-used-as-tools-for-russian-information-warfare-osint-investiga-
tion-informnapalm-insight-news/
https://blogs.microsoft.com/on-the-issues/2024/04/17/russia-us-election-interference-deepfakes-ai/
© Orange Cyberdefense 2024/2025

Contributors, sources & links 119
[28] https://www.reuters.com/world/europe/russian-hackers-were-inside-ukraine-telecoms-giant-months-cyber-spy-
chief-2024-01-04/
https://portal.cert.orangecyberdefense.com/worldwatch/advisory/1478
[29] https://portal.cert.orangecyberdefense.com/worldwatch/advisory/1478
https://www.kyivpost.com/post/36471
https://www.kyivpost.com/post/36570
https://www.epravda.com.ua/news/2024/07/24/717061/
[30] https://blog.cloudflare.com/cyber-attacks-in-the-israel-hamas-war/
https://www.microsoft.com/en-us/security/security-insider/microsoft-digital-defense-report-2023
https://securelist.com/a-hack-in-hand-is-worth-two-in-the-bush/110794/
https://www.bloomberg.com/news/articles/2023-10-26/israel-taps-blacklisted-pegasus-maker-nso-to-track-gaza-hostages-and-hamas?
[31] https://www.bellingcat.com/news/2023/10/11/hamas-attacks-israel-bombs-gaza-and-misinformation-surges-online/
https://www.zerofox.com/blog/navigating-the-mis-and-disinformation-minefield-in-the-current-israel-hamas-war/
https://twitter.com/JohnHultquist/status/1711605715888955747?s=20
[32] https://blog.cloudflare.com/malicious-redalert-rocket-alerts-application-targets-israeli-phone-calls-sms-and-user-information/
[33] https://cybernews.com/cyber-war/israel-redalert-breached-anonghost-hamas/
[34] https://www.malwation.com/blog/new-muddywater-campaigns-after-operation-swords-of-iron
https://portal.cert.orangecyberdefense.com/worldwatch/advisory/1482
https://research.checkpoint.com/2024/new-bugsleep-backdoor-deployed-in-recent-muddywater-campaigns/
[35] https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-335a
https://www.westernpeople.ie/news/hackers-hit-erris-water-in-stance-over-israel_arid-4982.html
https://portal.cert.orangecyberdefense.com/worldwatch/advisory/1674
[36] https://www.gov.il/en/pages/ziv181223
https://intezer.com/blog/research/stealth-wiper-israeli-infrastructure/
https://www.securityjoes.com/post/bibi-linux-a-new-wiper-dropped-by-pro-hamas-hacktivist-group
[37] https://www.cbc.ca/news/world/hezbollah-pagers-explosions-1.7326969
[38] MTTR is “Mean Time To Resolve”. Once an alert is raised by a security technology and a case is created, MTTR measures the time
it takes for the case to be analyzed and then reported to the client, who must investigate, take action, and confirm the finding.
[39] https://darktrace.com/resources/darktrace-ai-combining-supervised-and-unsupervised-machine-learning
[40] https://www.proofpoint.com/us/solutions/nexusai
[41] https://www.microsoft.com/en-us/security/business/siem-and-xdr/microsoft-defender-office-365
[42] https://www.crowdstrike.com/falcon-platform/artificial-intelligence-and-machine-learning/
[43] https://www.microsoft.com/en-us/security/business/ai-machine-learning/microsoft-copilot-security
[44] https://dspace.mit.edu/bitstream/handle/1721.1/147544/Mihretie-yosefmih-meng-eecs-2022-thesis.pdf?sequence=1
[45] https://securityintelligence.com/deeplocker-how-ai-can-power-a-stealthy-new-breed-of-malware/
[46] https://www.rsaconference.com/Library/presentation/USA/2019/the-rise-of-the-machines-ai-and-mlbased-attacks-demonstrated
[47] https://securityaffairs.com/169253/malware/rhadamanthys-information-stealer-uses-ai.html
[48] https://www.ft.com/content/b977e8d4-664c-4ae4-8a8e-eb93bdf785ea
[49] https:/www.microsoft.com/en-us/security/blog/2024/02/14/staying-ahead-of-threat-actors-in-the-age-of-ai
[50] https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/
[51] https://openai.com/global-affairs/an-update-on-disrupting-deceptive-uses-of-ai/
[52] https://www.microsoft.com/en-us/security/security-insider/intelligence-reports/microsoft-digital-defense-report-2024
[53] https:/cloud.google.com/blog/topics/threat-intelligence/ai-powered-voice-spoofing-vishing-attacks/
[54] https://www.theatlantic.com/technology/archive/2024/09/microsoft-ai-oil-contracts/679804/
[55] https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/exploiting-ai-how-cybercriminals-misuse-
abuse-ai-and-ml
[56] https://arstechnica.com/science/2024/10/the-more-sophisticated-ai-models-get-the-more-likely-they-are-to-lie/
www.orangecyberdefense.com

120 Security Navigator 2025
[57] https://genai.owasp.org/llm-top-10/
[58] https://www.malwarebytes.com/blog/news/2024/10/ai-girlfriend-site-breached-user-fantasies-stolen
[59] https://www.schneier.com/blog/archives/2012/12/feudal_sec.html
[60] https://www.pnas.org/content/early/2020/03/17/1915768117
[61] https://techcrunch.com/2024/04/14/generative-ai-is-coming-for-healthcare-and-not-everyones-thrilled/
[62] https://www.techpolicy.press/shining-a-light-on-shadow-prompting/
[63] https://www.techpolicy.press/author/eryk-salvaggio
[64] https://www.trendmicro.com/en_us/research/24/j/rogue-ai-part-4.html
[65] https://www.cisa.gov/news-events/news/dhs-cisa-and-uk-ncsc-release-joint-guidelines-secure-ai-system-development
[66] https://www.coalitionforsecureai.org
[67] https://www.cnil.fr/fr/definition/modele-ia
[68] https://fr.wikipedia.org/wiki/Alignement_des_intelligences_artificielles
[69] https://www.cyberark.com/resources/threat-research-blog/operation-grandma-a-tale-of-llm-chatbot-vulnerability
[70] https://josephthacker.com/ai/2023/05/19/prompt-injection-poc.html
[71] https://x.com/LeGuideDuSecOps/status/1841180286836441499
[72] https://mistral.ai/fr/
[73] https://huggingface.co/blog/alonsosilva/nexttokenprediction
[74] https://medium.com/@munnangisravya/ascii-smuggler-the-invisible-prompt-injection-d4188d2ff951
[75] https://arxiv.org/pdf/2402.11753
[76] https://promptengineering.org/system-prompts-in-large-language-models/
[77] https://x.com/LeGuideDuSecOps/status/1844298679655727618
[78] https://x.com/literallydenis/status/1708283962399846459
[79] https://www.gladia.io/blog/prompt-injection-in-speech-recognition-explained
[80] https://ai.google.dev/gemma
[81] https://x.com/LeGuideDuSecOps/status/1844298679655727618
[82] https://x.com/literallydenis/status/1708283962399846459
[83] https://www.gladia.io/blog/prompt-injection-in-speech-recognition-explained
[84] https://www.phoronix.com/news/Linux-CVSS-9.9-Rating
[85] https://www.bleepingcomputer.com/news/security/automattic-blocks-wp-engines-access-to-wordpress-resources/
[86] https://therecord.media/vulnerability-database-backlog-nist-support
[87] https://cyberscoop.com/plan-to-resuscitate-beleaguered-vulnerability-database-draws-criticism/
[88] https://www.cnnvd.org.cn/home/childHome
[89] https://www.sentinelone.com/labs/labscon-replay-is-cnvd-%E2%89%A5-cve-a-look-at-chinese-vulnerability-discov-
ery-and-disclosure/
[90] https://www.atlanticcouncil.org/in-depth-research-reports/report/sleight-of-hand-how-china-weaponizes-software-vulnerability/
[91] https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Year_in_Review_of_ZeroDays.pdf
[92] https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Year_in_Review_of_ZeroDays.pdf
[93] Cyentia Institute and Kenna Security. 2022. Prioritization to Prediction Vol 8. (2022). https://www.kennasecurity.com/resourc-
es/prioritization-to-prediction-reports/
[94] https://www.first.org/cvss/
[95] https://www.cisa.gov/resources-tools/resources/kev-catalog
[96] https://www.orangecyberdefense.com/global/offering/managed-services/threat-and-risk-management/managed-vulnerabili-
ty-intelligence-watch
[97] https://www.orangecyberdefense.com/global/blog/research/exploring-the-exploit-prediction-scoring-system
[98] https://www.thoughtco.com/complement-rule-example-3126549
[99] https://www.first.org/epss/user-guide
[100] https://www.first.org/epss/user-guide#3-EPSS-Can-Scale-to-Produce-System-Network-and-Enterprise-level-Exploit-Predictions
© Orange Cyberdefense 2024/2025

Contributors, sources & links 121
[101] https://github.com/JohnLaTwC/Shared/blob/master/Defenders%20think%20in%20lists.%20Attackers%20think%20in%20
graphs.%20As%20long%20as%20this%20is%20true%2C%20attackers%20win.md
[102] https://attack.mitre.org/
[103] https://sensepost.com/blog/2024/dumping-lsa-secrets-a-story-about-task-decorrelation/
[104] https://math.stackexchange.com/questions/4624889/what-is-the-name-of-this-formula-1-1-pn-x
[105] https://www.mathsisfun.com/data/binomial-distribution.html
[106] https://www.theregister.com/2024/09/20/cisa_software_cybercrime_villains/
[107] https://security.googleblog.com/2024/10/pixel-proactive-security-cellular-modems.html
[108] https://security.googleblog.com/2024/09/eliminating-memory-safety-vulnerabilities-Android.html
[109] https://www.cybersecuritydive.com/news/microsoft-security-debt-crashing-down/714685/
[110] https://www.ivanti.com/blog/our-commitment-to-security-an-open-letter-from-ivanti-ceo-jeff-abbott
[111] https://www.fastly.com/blog/the-dept-of-know-live-sounil-yu-on-why-embracing-the-die-security-model-means-faster-innovation/
[112] https://www.cisa.gov/securebydesign
[113] https://www.cisa.gov/resources-tools/resources/secure-demand-guide
[114] https://www.cisa.gov/resources-tools/resources/secure-design-alert-eliminating-cross-site-scripting-vulnerabilities
[115] https://www.cisa.gov/news-events/cybersecurity-advisories/aa20-107a
[116] https://www.cisa.gov/news-events/directives/supplemental-direction-v1-ed-24-01-mitigate-ivanti-connect-se-
cure-and-ivanti-policy-secure
[117] https://cloud.google.com/blog/topics/threat-intelligence/hacktivists-targeting-ot-systems/
[118] Kushner, D., 2013. The real story of stuxnet. ieee Spectrum, 50(3), pp.48-53.
[119] https://www.dragos.com/blog/protect-against-frostygoop-ics-malware-targeting-operational-technology/
[120] https://www.mitre.org/sites/default/files/pdf/08_1145.pdf
[121] https://www.theregister.com/2023/12/08/polish_trains_geofenced_allegation/
[122] https://www.bbc.co.uk/news/technology-62072480
[123] https://icscsi.org/library/Documents/White_Papers/SANS%20-%20ICS%20Cyber%20Kill%20Chain.pdf
[124] https://www.cyberphysicalsecurity.info/
[125] https://attack.mitre.org/matrices/ics/
[126] https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
[127] https://csrc.nist.gov/News/2023/nist-publishes-sp-800-82-revision-3
[128] https://www.ccn-cert.cni.es/publico/InfraestructurasCriticaspublico/CPNI-Guia-SCI.pdf
[129] Smith, P., 2021. Pentesting Industrial Control Systems: An ethical hacker's guide to analyzing, compromising, mitigating,
and securing industrial processes. Packt Publishing Ltd.
[130] Ackerman, P., 2017. Industrial Cybersecurity: Efficiently secure critical infrastructure systems. Packt Publishing Ltd.
[131] Knapp, E.D., 2024. Industrial Network Security: Securing critical infrastructure networks for smart grid, SCADA, and other
Industrial Control Systems. Elsevier.
[132] Staves, A., Gouglidis, A., Maesschalck, S. and Hutchison, D., 2024. Risk-based safety scoping of adversary-centric
security testing on operational technology. Safety science, 174, p.106481.
[133] Castellanos, J.H., Ochoa, M. and Zhou, J., 2018, December. Finding dependencies between cyber-physical domains for
security testing of industrial control systems. In Proceedings of the 34th Annual Computer Security Applications
Conference (pp. 582-594).
[134] https://cloud.google.com/blog/topics/threat-intelligence/global-revival-of-hacktivism?hl=en
[135] https://www.trendmicro.com/vinfo/us/security/news/cyber-attacks/rising-from-the-underground-hacktivism-in-2024
[136] https://radar.cloudflare.com/reports/ddos-2024-q1
[137] https://www.weforum.org/agenda/2023/12/2024-elections-around-world/
[138] https://www.cbsnews.com/news/2-sudanese-nationals-charged-cyber-attack-for-hire-gang/
[139] https://www.radware.com/h1-2024-global-threat-analysis-report-lpc-39853846/
[140] https://www.enisa.europa.eu/publications/enisa-threat-landscape-for-dos-attacks
[141] https://www.radware.com/security/threat-advisories-and-attack-reports/hacktivism-unveiled-april-2023/
www.orangecyberdefense.com

122 Security Navigator 2025
[142] https://ir.netscout.com/investors/press-releases/press-release-details/2024/DDoS-Attacks-Skyrocket-and-Hacktivist-Activi
ty-Surges-Threatening-Critical-Global-Infrastructure-According-to-NETSCOUTs-1H2024-Threat-Intelligence-Report/default.aspx
[143] https://www.ccc.de/en/hackerethik
[144] https://www.pewresearch.org/internet/2014/03/11/world-wide-web-timeline/
[145] https://www.statista.com/forecasts/1137817/household-internet-penetration-forecast-in-europe
[146] https://www.wired.com/1999/06/coming-soon-back-orifice-2000/
[147] https://www.reuters.com/investigates/special-report/usa-politics-beto-orourke/
[148] https://www.ccc.de/en/hackerethik
[149] http://www.cultdeadcow.com/news/statement19990107.html
[150] https://www.congress.gov/bill/99th-congress/house-bill/4718
[151] https://www.legislation.gov.uk/ukpga/1990/18/contents
[152] Nihilism - The belief things are inherently meaningless.
[153] First activities like date back to the Kosovo war in 1999 where cyber actors targeted the North Atlantic Threat Organiza-
tion (NATO) and other government websites to protest NATO’s bombing of Yugoslavia; by the mid-2000s activities like this
became much more prominent. D. (2000) Activism, Hacktivism, and Cyberterrorism: The Internet as a Tool for Influencing
Foreign Policy.
[154] https://securityintelligence.com/posts/the-decline-of-hacktivism-attacks-drop-95-percent-since-2015/ https://www.
fbi.gov/contact-us/field-offices/newyork/news/press-releases/leading-member-of-the-international-cyber-crimi-
nal-group-lulzsec-sentenced-in-manhattan-federal-court
[155] Smith, M. (2023). The Irregulars: Third-Party Cyber Actors and Digital Resistance. CyCon 2023 Proceedings. DOI: 10.23919/
CyCon58705.2023.10182061 https://ccdcoe.org/uploads/2018/10/Ottis2008_AnalysisOf2007FromTheInformationWar-
farePerspective.pdf
[156] https://www.atlanticcouncil.org/blogs/ukrainealert/the-2008-russo-georgian-war-putins-green-light/
[157] https://www.washingtonpost.com/lifestyle/style/the-hacktivists-of-telecomix-lend-a-hand-to-the-arab-spring/2011/12/05/
gIQAAosraO_story.html
[158] Kostiantyn Korsun, former Head of Ukrainian CERT and former Deputy Head of Computer Crime Division at the Security
Service of Ukraine posted a request on LinkedIn asking for help on the cyber front.
https://docslib.org/doc/8087108/cyber-proxies-and-the-crisis-in-ukraine
[159] Maurer, T. (2018). Cyber mercenaries: The state, hackers, and power. Cambridge University Press.
[160] https://cyberforumkyiv.org/A_Decade_in_the_Trenches_of_Cyberwarfare.pdf
[161] https://therecord.media/ukraine-monobank-ddos-attack-donations
[162] The total number of requests sent to overwhelm a service
[163] https://blog.cloudflare.com/how-cloudflare-auto-mitigated-world-record-3-8-tbps-ddos-attack/
[164] The total data volume (in bits) sent per second
[165] Bandwidth-based attacks aim to saturate the network and can be more challenging to mitigate.
[166] https://www.radware.com/security/threat-advisories-and-attack-reports/project-ddosia-russias-answer-to-disbalancer/
[167] https://media.defense.gov/2024/May/01/2003454817/-1/-1/0/DEFENDING-OT-OPERATIONS-AGAINST-ONGO-
ING-PRO-RUSSIA-HACKTIVIST-ACTIVITY.PDF
[168] https://www.bleepingcomputer.com/news/security/us-govt-warns-of-pro-russian-hacktivists-targeting-water-facilities/
[169] https://www.lawfaremedia.org/article/what-impact-if-any-does-killnet-have
[170] Nissen, T. E. (2015). "The Weaponization of Social Media: Information Operations in the Context of 21st Century Warfare."
Royal Danish Defense College.
[171] https://bindinghook.com/articles-hooked-on-trends/russias-strategic-culture-drives-its-foreign-hacking/
[172] https://en.wiktionary.org/wiki/Russophobic
[173] https://www.reuters.com/world/americas/canadian-pm-apologises-after-parliamentary-speaker-publicly-praised-na-
zi-2023-09-27/
[174] https://en.wiktionary.org/wiki/Russophobic
[175] https://www.pravda.com.ua/eng/news/2023/09/9/7419101/
[176] https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/
© Orange Cyberdefense 2024/2025

Contributors, sources & links 123
[177] https://www.mitre.org/sites/default/files/2021-11/prs-19-3892-ttp-based-hunting.pdf
[178] https://www.splunk.com/en_us/blog/security/peak-threat-hunting-framework.html
[179] https://center-for-threat-informed-defense.github.io/summiting-the-pyramid/
[180] https://medium.com/detect-fyi/akira-in-the-chang-way-server-ecosystem-re-vicitimization-a9011fbc6dff
[181] https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/our-work/measure-maximize-and-mature-
threat-informed-defense-m3tid/
[182] https://citizenlab.ca/tag/nso-group/
https://blog.sekoia.io/active-lycantrox-infrastructure-illumination/
https://www.amnesty.org/en/documents/act10/7245/2023/en/
https://gijn.org/stories/the-rapid-rise-of-phone-surveillance/
https://www.amnesty.org/en/latest/press-release/2021/07/world-leaders-potential-targets-of-nso-group-pegasus-spyware/
https://www.business-humanrights.org/en/latest-news/nso-group-spyware-sold-to-governments-used-to-target-activ-
ists-politicians-journalists-according-to-pegasus-project-investigation-company-denies-allegations/
https://rm.coe.int/pegasus-and-similar-spyware-and-secret-state-surveillance/1680ac7f68
https://apnews.com/article/poland-spyware-pegasus-nso-group-israel-413bb3cb27daac011d52b524c6d16160
https://www.reuters.com/technology/cybersecurity/spain-reopens-israeli-spyware-probe-sharing-informa-
tion-with-france-2024-04-23/
[183] https://therecord.media/sms-blasting-arrests-uk-homemade-antenna
[184] https://www.francetvinfo.fr/faits-divers/escroquerie-aux-sms-de-l-assurance-maladie-les-suspects-volaient-les-numeros-de-
telephone-depuis-leur-voiture_5665943.html
[185] https://commsrisk.com/oslo-imsi-catcher-arrest-suspected-malaysian-spy-now-investigated-for-fraud-with-international-ram-
ifications/
[186] https://therecord.media/orange-espana-outage-hacker-internet-ripe-bgp-rpki
[187] https://www.gsma.com/solutions-and-impact/technologies/security/gtleasing/
[188] https://www.lighthousereports.com/investigation/ghost-in-the-network/
[189] https://krebsonsecurity.com/2021/09/the-rise-of-one-time-password-interception-bots/
[190] https://www.wsj.com/tech/cybersecurity/u-s-wiretap-systems-targeted-in-china-linked-hack-327fc63b
[191] https://www.rcrwireless.com/20241008/telecom-software/verizon-att-lumen-among-telcos-hacked-by-chinese-group-reports
[192] https://www.gsma.com/solutions-and-impact/technologies/security/
[193] https://networkencyclopedia.com/global-system-for-mobile-communications-gsm/
[194] https://ss7.info/
[195] https://en.wikipedia.org/wiki/Signalling_System_No._7
[196] https://www.umtsworld.com/umts/faq.htm
[197] https://www.thalesgroup.com/en/markets/digital-identity-and-security/technology/lte
[198] https://ss7.info/ss7-vs-diameter/
[199] https://www.gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions/
[200] https://www.gsma.com/solutions-and-impact/gsma-open-gateway/
[201] https://www.rcrwireless.com/20240625/5g/philippine-telcos-join-gsma-open-gateway-initiative
[202] https://www.enisa.europa.eu/publications/signalling-security-in-telecom-ss7-diameter-5g/@@download/fullReport
[203] https://www.securityweek.com/gtp-vulnerabilities-expose-4g5g-networks-high-impact-attacks/#:~:text=Positive%20Tech-
nologies%20performed%20security%20assessments%20on%20behalf%20of,it%20does%20not%20check%20the%20
user’s%20actual%20location.
[204] https://www.blackhat.com/docs/us-15/materials/us-15-Yu-Cloning-3G-4G-SIM-Cards-With-A-PC-And-An-Oscilloscope-Les-
sons-Learned-In-Physical-Security.pdf
[205] https://www.kaspersky.co.za/blog/sim-card-history-clone-wars/11091/
[206] https://github.com/nickel0/3GPP-Overall-Architecture/blob/master/diagram/3GPP_Overall_Architecture_and_Specifications.pptx
[207] https://www.gsma.com/solutions-and-impact/technologies/security/wp-content/uploads/2024/07/Security-Land-
scape-2024-Issue-intro-contents.pdf
www.orangecyberdefense.com

124 Security Navigator 2025
[208] https://pages.nist.gov/800-63-3/sp800-63b.html
[209] https://www.magicbell.com/blog/expert-guide-to-push-notifications
[210] https://www.airship.com/resources/explainer/ios-push-notifications-explained/
[211] https://medium.com/@KaushalVasava/push-notification-in-android-how-its-work-2679d0bc0720
[212] https://en.wikipedia.org/wiki/Mark_Klein
[213] https://en.wikipedia.org/wiki/Greek_wiretapping_case_2004–05
[214] https://www.thalesgroup.com/en/markets/digital-identity-and-security/press-release/gemalto-presents-the-find-
ings-of-its-investigations-into-the-alleged-hacking-of-sim-card-encryption-keys
[215] https://www.cbsnews.com/news/60-minutes-hacking-your-phone/
[216] https://fidoalliance.org/passkeys/
[217] https://support.google.com/accounts/answer/13548313?hl=en-EN
[218] https://support.apple.com/en-za/guide/iphone/iphf538ea8d0/ios
[219] https://fight.mitre.org/
[220] https://github.com/swannman/ircapabilities
[221] https://cmmiinstitute.com/learning/appraisals/levels
[222] https://www.forrester.com/blogs/2025-security-risk-budget-planning-guide/
[223] https://open.spotify.com/episode/7dNpU6mxd7UUou2pz2mxIN
[224] https://www.orangecyberdefense.com/global/cyber-crisis-management
[225] https://www.politico.eu/article/meet-killnet-russias-hacking-patriots-plaguing-europe/
[226] https://www.thalesgroup.com/en/worldwide/security/press_release/ukraine-whole-europecyber-conflict-reaches-turn-
ing-point
[227] https://www.securityweek.com/volexity-catches-chinese-hackers-exploiting-ivanti-vpn-zero-days/
© Orange Cyberdefense 2024/2025

125
www.orangecyberdefense.com

126 Security Navigator 2025
What are the
criminals doing?
Defenders
think in lists.
Attackers
think in graphs.
As long as
this is true,
attackers win.
John Lambert,
Microsoft
Understanding
cybercrime
#CybercrimeNow
https://www4.orangecyberdefense.com/cybercrime-now
© Orange Cyberdefense 2024/2025

127
Disclaimer
All content in this report, including text, graphics, logos, icons and images, is the property of Orange
Cyberdefense and is protected by copyright laws. The content may be used as a resource, stating clear
references. Any other use, including the reproduction, modification, distribution, transmission, republication,
display, or performance, of the content is strictly prohibited unless written consent is given.
Orange Cyberdefense makes this report available on an “as-is” basis with no guarantees of completeness,
accuracy, usefulness or timeliness. The information contained in this report is general in nature. Opinions
and conclusions presented reflect judgment at the time of publication and may change at any time. Orange
Cyberdefense assumes no responsibility or liability for errors, omissions or for the results obtained from the
use of the information. If you have specific security concerns, please contact Orange Cyberdefense via
https://orangecyberdefense.com/global/contact/ for more detailed analysis and security consulting services.
A very special thanks
to all our experts including
cyber hunters, researchers,
analysts, engineers, ethical
hackers and incident
responders.
www.orangecyberdefense.com

Why
Orange
Cyberdefense?
Orange Cyberdefense is the expert We wrap elite cybersecurity talent, unique
cybersecurity business unit of the Orange technologies and robust processes into an
Group, providing managed security, managed easy-to-consume, end-to-end managed
threat detection & response services to services portfolio.
organizations around the globe. As Europe’s
go-to security provider, we strive to build a At Orange Cyberdefense we embed
safer digital society. security into Orange Business solutions for
multinationals worldwide. We believe strongly
We are a threat research and intelligence- that technology alone is not a solution. It is
driven security provider offering unparalleled the expertise and experience of our people
access to current and emerging threats. that enable our deep understanding of
the landscape in which we operate. Their
Our organization retains a 25+ year track competence, passion and motivation to
record in information security, 250+ progress and develop in an industry that
researchers and analysts 17 SOCs, 15 is evolving so rapidly.
CyberSOCs and CERTs distributed across 11
location in the world and sales and services We are proud of our in-house research team
support in 160 countries. We are proud and proprietary threat intelligence thanks to
to say we can offer global protection with which we enable our customers to focus on
local expertise and support our customers what matters most, and actively contribute to
throughout the entire threat lifecycle. the cybersecurity community. Our experts
regularly publish white papers, articles and
Orange Cyberdefense has built close partner- tools on cybersecurity which are widely
ships with numerous industry-leading recognized and used throughout the industry
technology vendors. and featured at global conferences, including
Infosec, RSA, 44Con, BlackHat and DefCon.
www.orangecyberdefense.com