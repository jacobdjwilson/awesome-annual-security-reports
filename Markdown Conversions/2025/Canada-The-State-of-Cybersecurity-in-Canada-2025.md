# The State of Cybersecurity in Canada 2025

**JAN. 2025**  
**PREPARED BY** Canadian Cybersecurity Network and Security Architecture Podcast  

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Config Chaos | How IoT and Cloud misconfigurations undermine security](#config-chaos--how-iot-and-cloud-misconfigurations-undermine-security)
- [Milestones that are important to Canada and cyber](#milestones-that-are-important-to-canada-and-cyber)
- [Facing the Cyber Storm: Canada’s Path to Building Resilience in 2025](#facing-the-cyber-storm-canadas-path-to-building-resilience-in-2025)
- [Securing Digital Frontiers: Tackling Cybersecurity and Privacy Challenges in 2025](#securing-digital-frontiers-tackling-cybersecurity-and-privacy-challenges-in-2025)

---

## Introduction
by François Guay, Evgeniy Kharam and Dmitry Raidman

Over the past year, Canadian organizations and institutions have witnessed a dramatic surge in cyber incidents, from ransomware attacks crippling critical infrastructure to the exploitation of vulnerabilities in cloud systems, IoT devices, and supply chain security. These attacks have inflicted financial damage, disrupted essential services, and eroded public trust. In a landscape where state-sponsored actors, cybercriminals, and opportunistic threat actors operate with increasing efficiency, the urgency to develop robust cybersecurity strategies has never been greater.

> As you navigate through the 2025 State of Cybersecurity Report, our hope is that it will serve as both an informative resource and a call to action.

The State of Cybersecurity Report in Canada 2025, serves as both an informative resource and a rallying cry for Canadian leaders. It challenges them to address cybersecurity not just as a challenge but as a driver of growth and innovation. It is also a celebration of Canadian thought leadership on very important business and technology topics that are directly impacting Canadians quality of life as well as their pocketbooks.

Supply chain security and asset risk-based management have emerged as critical focal points as organizations face growing threats stemming from third-party vulnerabilities and increasingly complex digital ecosystems. The security of supply chains—particularly in software dependencies and asset management—presents cascading risks that require advanced tools and strategies to address.

Emerging technologies like Agentic AI and advances in Identity Threat Detection and Response (ITDR) are reshaping the cybersecurity landscape. While these innovations offer tools to enhance defense capabilities, they also present new vulnerabilities, such as enabling sophisticated phishing campaigns, deepfake attacks, and the exploitation of digital identities. IoT and cloud misconfigurations have further amplified the attack surface, leaving critical industries such as healthcare, energy, retail, and education vulnerable to disruptions.

Compounding these challenges is a persistent cybersecurity talent gap, with 10,000 to 25,000 unfilled positions expected in the near term. This shortage affects the ability of organizations to adapt to the evolving threat landscape and undermines national resilience. Addressing this gap requires collaborative efforts to reskill professionals and make cybersecurity education more accessible across regions.

As you navigate through the 2025 State of Cybersecurity Report, our hope is that it will serve as both an informative resource and a call to action. Whether you are a business leader, policymaker, educator, or cybersecurity practitioner, this report is designed to equip you with the knowledge and insights needed to navigate today’s challenges and build resilience for the future. Together, we can safeguard Canada’s digital frontiers and turn cybersecurity from a reactive necessity into a strategic enabler of progress and innovation.

---

## Executive Summary

In the winter of 2024, a sophisticated ransomware attack brought one of Canada’s largest healthcare networks to a grinding halt. Patient care was disrupted, surgeries postponed, and sensitive data threatened. This breach, like many others in recent years, underscored the growing vulnerability of critical sectors across Canada. As organizations race to adopt advanced technologies, cybercriminals exploit gaps in security, leaving the nation’s economy and public trust at risk. These events serve as a stark reminder that Canada’s cybersecurity must evolve swiftly to keep pace with the escalating threat landscape.

The 2025 State of Cybersecurity Report delivers an in-depth analysis of the evolving cyber landscape in Canada, drawing on insights from various sectors and expert analyses. This report highlights urgent cybersecurity challenges while presenting actionable strategies for strengthening Canada’s digital resilience.

### Key Findings

**RISING THREATS:**  
Canadian sectors, especially healthcare, energy, education, and retail, have become prime targets for cybercriminals. Breaches are increasingly linked to human error and systemic vulnerabilities, with IoT and cloud misconfigurations accounting for 82% of breaches. As Paul Da Silva notes, “Ransomware is no longer a question of if but when. Canadian businesses must adopt a proactive, layered defense strategy to mitigate this inevitability.”

**TALENT SHORTAGE:**  
Canada’s cybersecurity workforce faces a significant deficit, producing fewer than 4,000 graduates annually compared to the demand for up to 25,000 roles. This gap threatens economic stability and public safety. Randy Purse emphasizes, “The cybersecurity skills gap is a national risk, threatening our economy and public safety. Mid-career transitions and regional training initiatives are essential for addressing this challenge.”

**EMERGING TECHNOLOGIES:**  
Generative AI, while aiding defensive measures, also enables sophisticated attacks like deepfake-based fraud and identity theft. ITDR (Identity Threat Detection and Response) has emerged as a critical strategy to combat these threats, addressing identity vulnerabilities in cloud and hybrid environments.

### Sector-Specific Challenges
- **Energy:** Legacy OT systems and supply chain dependencies make the sector vulnerable to ransomware and insider threats, with 75% of energy companies identifying supply chain risks as a top concern.
- **Education:** Insufficient funding and governance issues leave institutions exposed to ransomware and data breaches, disrupting academic operations.
- **Retail:** Third-party vulnerabilities and data breaches cost the sector $7.05 million per breach on average, with digital transformation heightening risks.

### Collaboration and Policy Innovation
Cross-sector collaboration is pivotal for cybersecurity resilience. Organizations must also focus on fostering a security culture and adopting standards like ISO/IEC 27001, which strengthen resilience through structured governance and proactive measures.

As Canada faces escalating cyber risks, this report underscores the importance of a national strategy integrating advanced technologies, policy innovation, and workforce development. With bold action and united efforts, Canada can secure its digital future against growing threats.

---

## Config Chaos | How IoT and Cloud misconfigurations undermine security
by Antoinette Hodes, Evangelist & Global Solution Architect, Presented by Check Point Software Technologies

In an increasingly connected world, IoT and cloud infrastructures are the backbone of modern innovation. As IoT evolves, it intertwines with hybrid APIs—essential for communication between IoT devices and the cloud—serve as both lifelines and attack vectors.

Yet, as these technologies integrate deeper into our lives and businesses, they introduce hidden vulnerabilities—misconfigurations—that few fully understand. These oversights are no longer merely technical glitches; they are amplifiers of systemic risk, creating cascading failures across the digital ecosystem and staggering costs. Human error is also a common cause for misconfiguration. According to Verizon’s Data Breach investigation report, human error is responsible for 82% of data breaches. Let’s explore how these vulnerabilities emerge and challenges emerging in IoT-cloud ecosystems.

### How simple mistakes lead to complex breaches

#### IOT | A GROWING ATTACK SURFACE
IoT devices are often rushed to market with minimal security considerations. This trend is driven by several factors, including the intense competition to be the first to offer a particular feature in the market, as well as budget constraints that often limit the resources allocated to thorough security testing and design. Default credentials, open ports and inadequate or even no update mechanisms are the most common issues. However, deeper misconfigurations like unsecured MQTT (Message Queuing Telemetry Transport) brokers can lead to unauthorized access and massive data leaks. Think of MQTT brokers like post offices that handle messages. The problem lies not only in the devices but also in how they interact with networks, and each other. Their widespread adoption means billions of devices are connected globally, ranging from smart home assistants to industrial control systems. Here’s why IoT security is particularly precarious:

- **Default credentials**: Many IoT devices are shipped with default usernames and passwords, which users often fail to change, making them easy targets for attackers.
- **Lack of updates**: Manufacturers frequently deprioritize firmware updates, leaving vulnerabilities unpatched.
- **Limited visibility**: IoT devices often operate in shadow IT environments, escaping the notice of security teams.

When IoT devices are integrated into cloud systems, these vulnerabilities don’t just remain localized, they are amplified.

#### CLOUD MISCONFIGURATIONS | A CATALYST FOR EXPLOITATION
Cloud services promise scalability and convenience but demand precision in setup. A simple misstep, such as leaving a storage bucket public or mismanaging Identity and Access Management (IAM) roles, can expose critical assets to the internet. Worse still, the nature of cloud environments means that vulnerabilities can propagate across regions and accounts, amplifying their impact. A report from XM Cyber which analysed 40 million exposures, states that 80% of cloud exposures are caused by identity and credential misconfigurations. Then we have improperly configured databases. Common missteps include:

- **Publicly accessible storage buckets**: Sensitive data stored in cloud buckets often lacks proper access controls, leading to breaches.
- **Weak identity and access management (IAM)**: Misconfigured permissions can allow attackers to escalate privileges and access critical resources.
- **Overlooked default settings**: Cloud services often come with default settings that prioritize usability over security.

These misconfigurations act as a gateway for attackers, who exploit IoT weaknesses to gain a foothold in the cloud.

> **80%** of security breaches are caused by identity and credential misconfiguration.

### The anatomy of misconfigurations
The role of APIs in IoT and cloud ecosystems cannot be overstated. APIs are the backbone of IoT and cloud integration, facilitating everything from device management to data transfer in real time. However, they are also one of the most exploited components in these environments. Misconfigured or poorly secured APIs can:
- Expose sensitive device telemetry to unauthorized users.
- Allow attackers to manipulate data streams or device functionality.
- Serve as entry points for lateral movement within hybrid cloud infrastructures.

For instance, API keys embedded in IoT firmware can be extracted and reused by attackers to compromise entire cloud-hosted IoT fleets.

### Open ports, open doors | How much of IoT security is misconfiguration-driven?
Microminder’s report is stating that 80% of security breaches are caused by identity and credential misconfiguration. This figure dwarfs other common IoT vulnerabilities such as unpatched software or outdated firmware. While the percentage varies depending on the industry and use case, misconfiguration is a dominant factor across smart homes, industrial IoT (IIoT), and healthcare devices.

### Why misconfigurations amplify threats
1. **ATTACK SURFACE MULTIPLICATION**: IoT ecosystems and cloud environments are vast, dynamic and interconnected. A misconfigured IoT camera, for instance, can serve as an entry point to an entire corporate network. A misconfigured cloud service, video stream can expose sensitive customer data.
2. **BLIND SPOTS IN DETECTION**: Misconfigurations often fly under the radar of traditional security monitoring tools. Attackers exploit these blind spots, leveraging tools like Shodan to scan for vulnerable IoT devices or misconfigured cloud assets.
3. **SPEED OF EXPLOITATION**: Once discovered, misconfigurations can be exploited within minutes. Attackers use automated tools to weaponize these errors at scale, launching botnets or ransomware campaigns.

### When IoT and Cloud turn into Toxic Combinations
IoT and the cloud can be a dangerous cocktail of risk when misconfigurations meet overprivileged access and insecure design. Picture a cloud-based virtual machine with exploitable vulnerabilities, exposed to the internet, with overprivileged access deeper into the cloud account or on-premises networks. This is granting attackers a bridge to the cloud or your network. Now, amplify that threat through IoT devices, like cheap cameras or sensors - offering cloud connectivity by default. These devices can become invisible conduits of risk, syncing to poorly configured cloud storage that leaks data or even pulling firmware updates from a compromised source. A single exploited IoT device connected to the cloud can transform into an entry point for attackers, propagating botnets, data breaches and supply chain havoc. As more OEM providers bake insecure cloud dependencies into their IoT products, the potential for unseen exploitation scales dramatically, endangering businesses and consumers alike.

### What no one talks about
1. **DEFAULT CONFIGURATIONS ARE EVERYWHERE**: Many IoT devices hold default usernames and passwords. These credentials are often available online, making them a goldmine for attackers. Shockingly, 15% of consumers never change default settings, exposing their devices to automated botnet scans.
2. **SHADOW IOT IS GROWING UNCHECKED**: Shadow IoT devices, unauthorized or unknown devices on a network worsen the misconfiguration problem.
3. **PROTOCOL PITFALLS**: Protocols like MQTT and CoAP, widely used in IoT, are often deployed without proper security measures.
4. **MISCONFIGURATIONS IN THE CLOUD BACKEND**: IoT devices often rely on cloud-based platforms. Misconfigured cloud storage buckets or APIs linked to IoT devices account are often ignored in traditional IoT security discussions.

> **15%** of consumers never change default settings.

### Why hybrid clouds complicate security
Hybrid cloud environments, combining public and private clouds, provide IoT ecosystems with scalability and resilience. However, their complexity introduces unique challenges:
- **Misaligned security policies**: Different security configurations across private and public clouds can create gaps. For example, an IoT device connecting to a private cloud might adhere to stringent encryption protocols, while its connection to a public cloud uses weaker settings.
- **Data residency and transfer risks**: Telemetry data often moves across borders in hybrid setups, potentially violating compliance rules if misconfigured.
- **Visibility challenges**: Traditional monitoring tools struggle to provide end-to-end visibility across hybrid clouds, making it harder to detect misconfigurations or breaches.

Other amplifications are data silos. Poorly configured APIs and access controls can isolate critical telemetry, leading to blind spots in monitoring. Attackers exploit these silos to remain undetected. Secondly, latency issues caused by misconfigured cloud regions can lead to delayed responses in IoT systems, impacting operations like predictive maintenance or real-time alerts. Lastly, misconfigurations in resource overlap can ripple through, affecting storage, compute, and network services simultaneously, as APIs often interact with multiple cloud resources.

### Behind the buzzwords
IoT and cloud misconfigurations create a cascade of challenges that extend far beyond initial breaches. For IoT systems, the consequences often include physical damages such as equipment failures, safety risks or operational disruptions, all of which compound financial losses. In cloud environments, the aftermath can involve regulatory fines, customer lawsuits, and reputational damage that far exceed the initial response costs. These issues are further amplified by stringent compliance requirements under frameworks like the GDPR and the EU’s Cyber Resilience Act (CRA), which impose heavy penalties for violations, especially on IoT products now under increased scrutiny. Worse still, misconfigurations rarely exist in isolation. In today’s interconnected ecosystems, a single misconfigured IoT device, such as a CCTV camera can trigger a chain reaction, providing attackers with lateral access to critical infrastructure and amplifying the overall impact. This convergence of compounding costs, regulatory risks, and chain reactions underscores the urgent need for meticulous configuration and proactive security management.

### Key takeaways
1. **MISCONFIGURATIONS ARE THE ACHILLES’ HEEL OF IOT SECURITY**: They are responsible for a significant portion of breaches yet are often overlooked in favour of more complex vulnerabilities.
2. **DEFAULT CREDENTIALS AND OPEN PORTS ARE LOW-HANGING FRUIT FOR ATTACKERS**: Basic hygiene like changing default passwords and closing unnecessary ports can mitigate many risks.
3. **VISIBILITY IS KEY**: Shadow IoT devices and poorly documented systems create blind spots in networks, increasing misconfiguration risks.
4. **AUTOMATION TOOLS CAN HELP**: Leveraging AI-powered tools to scan for misconfigurations can drastically reduce human error and enhance overall security.
5. **HOLISTIC SECURITY APPROACHES ARE ESSENTIAL**: It’s not just about securing the device but also the network, cloud backend, and protocols it interacts with.

### What Can We Do About It?
- **Educate users and organizations**: Many IoT vulnerabilities are avoidable with basic awareness and training.
- **Adopt strong device management**: Organizations must maintain visibility into connected devices and regularly audit configurations.
- **Advocate for secure defaults**: Manufacturers should ship devices with security-first configurations, minimizing user effort.
- **Regulate and enforce standards**: Policies like the EU Cyber Resilience Act (CRA) can incentivize better practices in device manufacturing and deployment.

Misconfigurations in IoT are often ignored until it’s too late. By understanding the scale of the issue and taking proactive steps, we can prevent the next wave of attacks and secure the interconnected future we envision.

---

## Milestones that are important to Canada and cyber
by Bob Gordon

Canada’s cyber environment has undergone significant changes over the past twenty years resulting in noteworthy milestones. This article briefly describes those changes and the resulting milestones.

Advances in technology, and its broad adoption by governments, businesses, and individuals, have resulted in significant societal benefits. Unfortunately, criminals and some nation states, for example The People’s Republic of China, Russia, and Iran, are using these advances for purposes that harm Canadians.[^1] These activities were part of the impetus in establishing the milestones outlined below. Changes to the cyber environment are continuing and these will create new, un-identified, milestones.

The initial environmental change occurred around the turn of the century with Canadians’ growing interest in the privacy of their personal information. Individuals wanted to feel confident about how their personal information was gathered, stored and used. It could be argued that this was the first indication of the nascent cyber security environment we know today.

The Government’s response to the demand for privacy became our first milestone – the introduction of the Personal Information Protection and Electronic Documents Act (PIPEDA) which received Royal Assent on April 13, 2000.[^2] PIPEDA was not a response to cyber attacks rather, it was concern about the collection, use and disclosure of personal information. Canadians were demanding adequate privacy protection in a new digital economy. The law has applicability nationally with the exception of Alberta, British Columbia, and Quebec, or within Ontario relating to personal health information, as their privacy laws were deemed to be substantially similar to PIPEDA.

> Canadians were demanding adequate privacy protection in a new digital economy.

While attention continued to be placed on the protection of personal information, there was mounting concern about increasing cyber attacks against government and business. The number of Canadians who were victims of identity theft was also rising. Nation states and cyber criminals were increasing their attacks in an effort to collect intellectual property. Concern was expressed about the vulnerability of Canada’s critical infrastructure (CI) which is dependent on automated systems and interconnected networks. Attacks such as the ILOVEYOU virus, the Blaster worm, the Conflicker worm, the SQL Slammer worm, and the Stuxnet worm became the bane of cyber security defenders worldwide. The result was the second milestone, the establishment of a Cyber Security Task Force (CSTF) within Public Safety Canada in 2006.

The CSTF’s mandate was to consult with the private sector and make recommendations on a cyber security strategy for Canada. The focus was to be on the management and control of cyber security risks, identifying CI interdependencies across sectors, and recommend mitigative measures.[^3] Simultaneously, Public Safety Canada continued to enhance the capability of its Canadian Cyber Incident Response Centre (CCIRC) which was responsible for providing cyber security mitigation strategies intended for government departments and agencies and the CI sector.[^4]

Public Safety Canada subsequently produced the third milestone, Canada’s Cyber Security Strategy in 2010 and related Action Plan 2010-2015 for Canada’s Cyber Security Strategy.[^5] The Strategy was significant as it was the first time the Government had articulated the national importance of cyber security, and committed financial resources to the implementation of the action plan. Much of the focus was on securing Government systems. Notable examples include establishment of the Cyber Threat Evaluation Centre in the Communications Security Establishment and Shared Services Canada’s efforts to consolidate the Government’s digital backbone and implement an enterprise approach for the delivery of IT security services. The strategy also identified the need for partnering to secure vital cyber systems outside the federal Government and helping Canadians be secure online.

In the period following the release of the strategy, the cyber threat environment and technology evolved. The scale and nature of cyber crime mushroomed. Cyber attacks employing ransomware marked a significant change in how cyber crime was conducted. Ransomware attacks became a victim equalizer. No longer were attackers only going after victims that possessed valuable intellectual property or huge financial resources. Attackers targeted data that only had value to the victim, where its loss, or inaccessibility, would severely impact a victim’s operational capability. During the early years of ransomware attacks, victim’s data was encrypted to make it unusable. Victims were willing to pay to have their data restored to enable their business to operate. Attack techniques evolved with attackers threatening to publicly release the victim’s data or to sell it. During COVID, attackers focused on particularly vulnerable and critical organizations such as hospitals. The goal of the attackers was to create a sense of urgency and fear to incentivize payment of the ransom.

Criminal gangs began conducting cyber operations as a business. Advances in technology enhanced their capability while at the same time making it easier to become a criminal. Cyber attack tools became readily available online and relatively easy to use, even for the non-technical criminal.

Concurrently, some nation states permit cyber criminals to operate with limited intervention providing they followed a couple of rules – do not attack entities within their country and when called upon, conduct operations to support their nation’s intelligence services. Identifying whether the attacker is a cyber criminal, or a nation state became increasingly difficult.

A milestone arose when foreign attackers successfully accessed Canadian government systems. In 2011, hackers using IP addresses from China infiltrated three Canadian government departments, exfiltrating classified data. In 2014, the National Research Council of Canada (NRC) was the target of a cyberattack from a “highly sophisticated Chinese state-sponsored actor.”[^6]

The 2010 Cyber Strategy included a review mechanism to assess its progress on improving Canada’s cyber resilience and to adjust as necessary. The subsequent 2017 Horizontal Evaluation of Canada’s Cyber Security Strategy led to the next milestone, the release of the 2018 National Cyber Security Strategy, and subsequent issuance of the National Cyber Security Action Plan (2019-2024). Three goals were identified: focusing on secure and resilient systems, developing an innovative and adaptive cyber ecosystem, and providing effective leadership and collaboration.[^7]

The National Strategy announced several subsequent milestones including the creation of two flagship organizations, the Canadian Centre for Cyber Security (CCCS) and the National Cybercrime Coordination Centre (NC3).

The launch of the CCCS (the Centre) marked a significant shift in the federal government’s effort to enhance the cyber resilience of the private sector. The Centre became the country’s unified source of expert advice, guidance, services and support on cybersecurity. While the Centre retained responsibility for the security of federal government systems, it created programs designed specifically to assist the private sector. Using its extensive technical expertise, the Centre started producing technical guidance, issuing alerts about cyber threat actors, and, on a bi-annual basis, publishing a National Cyber Threat Assessment. This marked an advancement in the government’s efforts to assist the private sector to be aware of and cope with the increasingly hostile cyber threat environment.

> The Centre became the country’s unified source of expert advice, guidance, services and support on cybersecurity.

As a National Police Service, NC3 provides an essential coordination function for all law enforcement investigations against cyber criminals. It also works with international partners to combat cyber crimes, which has become a key requirement as many cyber incidents have an international nexus. NC3 and law enforcement’s efforts are already becoming apparent with the conviction of major cyber criminals.[^8]

Consumers and businesses also required protection from the misuse of digital technology including spam and other electronic threats. Canada’s anti-spam legislation (CASL) was created in 2014 to address this issue. Although designed to reduce the volume of spam received by Canadians, the legislation also dealt with other threats including identity theft, phishing and the spread of malicious software, such as viruses, worms and trojans (malware).[^9]

2019 marked another significant milestone with the passage of the Communications Security Establishment Act. The Act was passed as part of the omnibus National Security Act 2017 that reformed the oversight on Canada’s national security organizations. CSE acquired new tools in the defence against foreign cyber attackers. Authorization was given to CSE to conduct defensive cyber operations “to help protect systems of importance and federal institutions during major cyber incidents when cyber security measures alone are not enough”. CSE’s 2023-2024 Annual Report revealed that its defensive cyber operations were used for the first time against a foreign ransomware group that was targeting multiple Canadian critical infrastructure organizations.[^10] Authority was also given for CSE to undertake active cyber operations to proactively disrupt foreign-based threats to Canada’s international affairs, defence or security interests.

Canada’s private sector also responded to the worsening cyber threat environment. Businesses realized that no organization can fully protect itself in this cyber threat environment – that a collaborative approach is required. The expression, ‘none of us are as smart as all of us’ characterized the call to action. The next milestone was the business community’s establishing the Canadian Cyber Threat Exchange (CCTX). It became Canada’s cross sector centre for collaboration through sharing cyber threat information, best practices and experiences.

> Businesses realized that no organization can fully protect itself in this cyber threat environment — that a collaborative approach is required.

Establishment of the CCTX represented a shift in the concept of cyber security. Cyber security was no longer seen as a competitive advantage. To mitigate this growing business risk, all businesses need to have an understanding of the cyber threat environment which is enabled through sharing and collaboration. Competition is left to the provisioning of goods and services. Businesses also began reevaluating their corporate governance of cyber security. There was a growing realization that cyber security had become a whole of business issue. Cyber moved out of the shadows and was no longer the sole domain and understanding of technical experts. Cyber resilience was recognized as a matter of assessing and managing this business risk. Like business continuity planning, this is the responsibility of business units. Overall, these changes represented a shift from the concept of cyber security to one of cyber resilience. Businesses need to be aware of, and prepare for, cyber attacks and subsequently plan for incident response and business recovery. The assumption has now shifted to a recognition that the business will be the scope of a successful cyber attack.

Meanwhile, international attention continued to be given to the increasing cyber threat, and the parallel need to protect personal data. There was a realization that data privacy and security were convening; it’s not possible to have one without the other. Canadian businesses are impacted by these efforts, e.g., by legislation such as the European Union’s rules and legislation on data protection, including the 2016 General Data Protection Regulation (GDPR) and the Data Protection Law Enforcement Directive.[^11] Action is also underway to counter the growing number of ransomware attacks.

For example, the United States organized what has become known as the International Counter Ransomware Initiative (CRI) with 68 members, including Canada. CRI is working to build resilience against ransomware attacks and leverage the ecosystem to disrupt the ransomware criminal industry. These efforts seek to “undercut the business model that underpins the ransomware ecosystem by driving forward work on secure software and labeling, methods to counter the use of virtual assets as part of the ransomware business model, policies to reduce ransom payments, increase and improve reporting, cyber insurance, and a playbook to guide businesses on how to prepare for, deal with, and recover from a ransomware attack.”[^12]

The United States and Canada recognized that they have a shared physical border and a shared infrastructure and that a coordinated approach to cyber security is required. Consequently, in 2022, Public Safety Canada and the Department of Homeland Security established a Cyber Security Action Plan. Elements of the Plan include enhancing incident management collaboration, joint engagement and information sharing with the private sector on cyber security and continued cooperation on ongoing cyber security public awareness efforts.[^13]

The cyber threat environment has not diminished. Attacks are becoming more sophisticated and the costs associated with successful breaches are mounting. Ransomware attacks remain a persistent threat. Nation states are increasing their cyber attacks, going beyond traditional espionage, seeking commercial advantage by stealing intellectual property for the benefit of their domestic industries. They are also prepositioning themselves in critical infrastructure for use at a time of their choosing, e.g., during a crisis.[^14]

The technology environment is also changing. Advances in machine learning combined with generative artificial intelligence (AI) have enhanced the ability of cyber attackers. Also, while AI is also proving to be a useful tool for cyber defenders, it fails to neutralize the benefits to the attackers. The drive to create quantum computing is accelerating. Businesses now need to consider the immediate implementation of quantum resistant cryptography to defend themselves against the phenomenon of ‘collect now and decrypt later.’

In response to the risk environment, the Canadian government introduced two additional legislative milestones, the Cyber Security Act (Bill C-26) and Countering Foreign Interference Act (Bill C-70). The former is being considered by the Senate and the latter received Royal Assent in June 2024. Both implicate the private sector. The Cyber Security Act includes mandatory reporting requirements of cyber security incidents by designated CI operators. They need to establish and implement cyber security programs and mitigate supply-chain and third-party risks. Designated operators are those falling within the legislative authority of Parliament, e.g. telecommunications services, interprovincial or international pipeline and powerline systems, nuclear energy systems, banking and clearing and settlement systems and some transportation systems.[^15] The Foreign Interference Act provides the Canadian Security Intelligence Service the ability to provide threat information to the private sector, something that has been sought by the private sector but formerly not allowed.

In this rapidly changing cyber threat environment, some immediate positive milestones are required: an updated national cyber security strategy, passage of Bill C-26, and updating PIPEDA. Going forward, governments, businesses, and academia will continue their efforts to create new milestones, enabling Canada to demonstrate leadership both nationally and internationally.

Robert (Bob) Gordon is the Executive Director of the Canadian Cyber Threat Exchange (CCTX). Prior to joining the CCTX, Bob held several senior leadership roles in the private and public sectors. Most recently, Bob was a Director, Global Cyber Security at CGI. Prior to this, he enjoyed a long and successful career in the Federal Government, which included being the architect of Canada’s first Cyber Security Strategy for which he received the Deputy Minister’s Achievement Award.

---

## Facing the Cyber Storm: Canada’s Path to Building Resilience in 2025
by J. Paul Haynes

In 2025, Canadian organizations are facing a perfect storm of escalating cyber threats, impacting sectors as varied as healthcare, finance, energy, and technology. From increasingly sophisticated ransomware attacks to state-sponsored espionage, the cyber threat landscape is now more complex and dangerous than ever before.

Canadian companies — particularly small and mid-sized businesses (SMBs) — are especially vulnerable due to under-resourced security measures and limited threat intelligence capabilities.

At the same time, ransomware attacks targeting critical supply chains have highlighted vulnerabilities that ripple across entire sectors, underscoring the need for a united approach. By identifying the top three emerging cyber threats in 2025, Canadian organizations can better assess their preparedness against these threats, particularly ransomware, which has become the most pervasive and costly type of cybercrime.

Moreover, as cyber threats rise in complexity, it’s clear that the Canadian government must collaborate with businesses to protect Canada’s digital future. This may occur through creating robust cybersecurity policies, taking recommendations from Canada’s top cyber experts, building cross-sector partnerships, and fuelling the cybersecurity talent pipeline.

### Top 3 Emerging Cybersecurity Threats Impacting Canadian Businesses in 2025

#### 1. RANSOMWARE AS A SERVICE (RAAS) AND SUPPLY CHAIN INFILTRATION
The evolution of ransomware has ushered in a new era of Ransomware-as-a-Service (RaaS), a business model that enables expert cybercriminals to research and develop new ransomware campaigns and sell, or rent, them to amateur hackers.

This trend has empowered threat actors, allowing them to target SMBs and enterprise organizations, especially within critical infrastructure and supply chains, with alarming efficiency.

Despite some progress, most Canadian organizations – especially SMBs – are unprepared for sophisticated ransomware attacks. Lack of budget, expertise, and access to advanced cybersecurity services leaves SMBs highly vulnerable.

On the other hand, while larger enterprises may have greater resources, they remain exposed due to expansive attack surfaces and the vast complexity of their supply chains, where smaller, less-secure vendors become weak links.

To combat ransomware and mitigate supply chain risks, the Canadian government must play a proactive role in bolstering defenses. For one, given the critical role that 24/7 threat detection and response capabilities play in a multi-layered cyber defense strategy, the Canadian government should consider providing some financial incentives that encourage Canadian businesses to partner with local Managed Detection and Response (MDR) providers.

As a July 2024 Centre for International Governance Innovation (CIGI) policy report points out, these partnerships will offer SMBs a practical defense by providing critical monitoring and response capabilities that are otherwise unaffordable.

#### 2. RANSOMWARE AND STATE-SPONSORED ADVANCED PERSISTENT THREATS (APTS) ACTIVITY
Canada’s critical infrastructure is increasingly under attack from ransomware groups and state-sponsored actors.

Initial access vectors used by threat actors to gain entry into North American organizations:
- Browser, Email, Misconfiguration, Remote exploit, Removable media, Valid credentials

Sophisticated state-sponsored threat actor groups from Iran, North Korea, Russia, and China use varied methods to gain initial access to organizations including, phishing, exploiting known vulnerabilities, and zero-day exploits to infiltrate corporate networks, where they can siphon sensitive data and positioning themselves for potential sabotage.

As stated in the Canadian Centre for Cyber Security’s National Cyber Threat Assessment 2023, and again in the National Cyber Threat Assessment in 2024, the impact of these state-sponsored attacks goes beyond financial loss, posing a strategic risk to Canada’s national security and sovereignty. Unfortunately, given that many Canadian organizations lack real-time threat response tools and threat intelligence resources to counter APT tactics, they remain highly susceptible to infiltration.

To counter ransomware groups and state-sponsored cyber threats, the Canadian government should develop and foster a centralized, collaborative approach that mirrors the U.S. Joint Cyber Defense Collaborative (JCDC).

As part of this initiative, Canadian MDR providers can work with the government as well as national defense and intelligence agencies to get the appropriate security clearances and conduct coordinated responses to APT activity.

#### 3. USE OF DRIVE-BY SOCIAL ENGINEERING TACTICS FOR BROWSER-BASED THREATS
Threat research from eSentire’s Threat Response Unit (TRU) has shown threat actors are increasingly using fake browser updates to lure employees into downloading malware and to gain initial access into an organization’s environment.

In addition, cybercriminals are also using drive-by social engineering tactics, such as search engine optimization (SEO) poisoning to lure employees searching for common documents like legal forms or invoicing templates into downloading the GootLoader and SolarMarker malware.

Once they have gained access, attackers can perform reconnaissance, exfiltrate data, and deploy ransomware, often without detection.

What’s more, the threat trend data observed by eSentire’s TRU team shows that browser-based attacks now represent 70% of all threats seen in our global customer base.

To protect against browser-based attacks, the Canadian government may consider providing subsidies to support advanced endpoint protection (EDR) and advocating for regular security awareness training for all employees. Moreover, funding incident response tabletop exercises that simulate social engineering attacks can further strengthen preparedness across Canadian businesses.

> By fostering a “whole-of-society” approach, the Canadian government would ensure that cyber resilience extends across all sectors.

---

### Key Recommendations to Bolster Canada’s Cybersecurity Posture

#### A. DOMESTIC MDR INCENTIVES
To meaningfully improve Canada’s cyber resilience, government-led incentives that prioritize the use of Canadian MDR providers are essential. By providing 24/7 monitoring, rapid detection, and expert-led incident response, MDR firms offer a vital service in the fight against ransomware and other advanced cyber threats, especially for SMBs that often lack in-house cybersecurity capabilities.

Furthermore, Canadian MDR providers bring local expertise and familiarity with the unique regulatory, threat, and business environments of Canada, making them highly relevant to addressing the specific needs of Canadian organizations.

Unfortunately, the costs associated with implementing a comprehensive cybersecurity strategy can be restrictive for many Canadian SMBs, and this is where government incentives could bridge the gap. By offering non-refundable tax credits or direct subsidies for Canadian businesses that partner with domestic MDR providers, the government can encourage broader adoption of critical cybersecurity services.

These incentives would make MDR services more accessible to SMBs, helping them benefit from real-time threat detection and response, 24/7 SOC-as-a-Service, and proactive threat intelligence and threat hunting services that may otherwise be beyond their financial reach.

This would empower SMBs to respond to ransomware and other cyber incidents with the same efficiency as larger enterprises, protecting their operations and reinforcing Canada’s economic stability in the face of cyber threats.

#### B. ESTABLISHING A NATIONAL CYBER DEFENSE COLLABORATIVE
In 2021, the Cybersecurity and Infrastructure Security Agency (CISA) launched the U.S. Joint Cyber Defense Collaborative (JCDC), creating a platform for real-time intelligence sharing, uniting public and private sectors to prevent, detect, and respond to cyber incidents on a national scale.

By leveraging the expertise and intelligence of private cybersecurity firms alongside government resources, the JCDC has accelerated the U.S.’s response to ransomware and other high-profile cyber threats.

Adopting a similar framework in Canada would create a centralized defense mechanism, enabling faster information sharing, coordinated responses, and policy alignment across sectors. Under this collaborative model, Canadian MDR providers and cybersecurity firms would act as strategic partners to government agencies, ensuring that actionable threat intelligence is disseminated quickly and securely to those on the front lines of cyber defense.

This approach would unify the cybersecurity efforts of Canadian private companies and public entities, creating a robust, national cyber defense ecosystem.

By fostering a “whole-of-society” approach, the Canadian government would ensure that cyber resilience extends across all sectors, from large enterprises to SMBs. This initiative would enable more robust responses to ransomware by coordinating private and public resources, reducing the impact of attacks on Canadian businesses, critical infrastructure, and government systems alike.

A collaborative defense model would also facilitate the creation of standardized best practices and incident response protocols that private companies could adopt, enhancing the security posture across all industries.

#### C. ADDRESSING THE CYBERSECURITY SKILLS GAP
Canada, like its North American and European peers, is currently facing a significant cybersecurity skills shortage. In fact, according to the Information and Communications Technology Council (ICTC), one in six positions in cybersecurity remain unfilled in Canada.

This skills gap presents a critical barrier to improving national resilience against ransomware and other cyber threats; it not only impacts operational security but also puts Canada at a disadvantage in defending against sophisticated cyber threats that require specialized expertise.

The Canadian government has a unique opportunity to address this skills gap by supporting training incentives and subsidies for cybersecurity education and certifications. By providing tax credits to companies investing in their cybersecurity workforce, the government could promote ongoing professional development, offsetting the high costs associated with industry-standard certifications and training programs.

With financial incentives, Canadian organizations can afford to train more specialists, contributing to a stronger, more competitive cybersecurity workforce that benefits the entire Canadian economy.

Beyond subsidies, the government could also consider partnerships with academic institutions and private sector firms to create specialized training programs and apprenticeships, particularly for entry-level cybersecurity roles. These programs would attract new talent into the cybersecurity field and provide hands-on experience, allowing trainees to work with experienced MDR providers to develop practical skills.

All in all, addressing the cybersecurity skills shortage is crucial to reducing Canada’s vulnerability to ransomware and other cyber threats, and it is one of the most effective long-term investments the government can make in the nation’s digital security infrastructure.

As we look to the future, one thing is clear: protecting Canada’s economic stability and digital sovereignty requires a proactive, unified approach.

The rising tide of ransomware, state-sponsored espionage, and sophisticated malware requires a whole-of-society approach to defense, one that prioritizes local partnerships, government support, and continuous collaboration.

Canada’s cyber resilience depends on decisive action from both public and private sectors. To secure Canada’s digital future, policymakers must act swiftly to foster an environment where businesses, cybersecurity providers, and government agencies work together to combat evolving threats.

J. Paul Haynes is the President and Chief Operating Officer at eSentire. In his role, he oversees all security operations and customer success functions and leads the Corporate Development team. J. Paul is a professional engineer with a 25-year entrepreneurial track record of success. His business acumen, in-depth understanding of technology, and strong leadership have made him a respected and reliable voice on the topic of cybersecurity in North America and Europe.

---

## Securing Digital Frontiers: Tackling Cybersecurity and Privacy Challenges in 2025
by Michael Argast

2024 saw an explosion in the adoption of industry frameworks and increase in government regulations in cybersecurity and privacy domains. The reason is simple — widespread adoption of cloud, SaaS, AI and interconnections of networks and data in business are dramatically increasing the data spread and risk for most organizations. Despite increased investments in cybersecurity, breaches and data losses reached unprecedented levels in 2024, underscoring critical gaps in existing measures.

Here are some highlights of this trend just in 2024.

### Regulatory Updates:
- DoD finalizes CMMC rule — this will lead to most DoD suppliers having to achieve this standard
- DORA implements cybersecurity resiliency requirements in EU sold products with “digital elements”
- NIS2 is now the first EU wide law on cybersecurity
- Continued fall-out over the demise of the EU-US Privacy Shield
- Texas TX-Ramp now in place for Texas public sector purchasing
- Compliance automation market leader Vanta raises $150M USD at $2.45B valuation
- Everybody is trying to regulate AI and come up with standards
- New privacy regulations in Delaware, Indiana, Iowa, Montana, New Jersey, Oregon, Tennessee, Washington and Texas
- NIST finally adds Governance to CSF V2
- FTC continues to step up enforcement, FBI successfully prosecutes Uber CISO for concealing breach information
- Third-party breaches accounted for 29% of incidents in 2024, highlighting the critical need for robust vendor risk management systems.

### Notable incidents and fines:
- Change Healthcare’s ransomware attack took down much of the US healthcare payments system
- Infosys McCamish’s incident resulted in losses at Bank of America
- AMEX suffered a card detail compromise from a merchant processor
- The Okta breach continues to cause fallout and downstream issues
- Snowflake customers were hit by targeted account compromises
- Lehigh Valley Health Network agreed to a $65M settlement over nude cancer scans
- 23andMe suffered a massive breach and paid $30M
- AT&T got hit once again for a $13M fine by the FTC.

---

### What do you need to do?

#### SMALL
Pre-revenue to $25M annually: If you work with 3rd party data, you need to plan to implement minimum security controls and standards (SOC2). Saas/Healthtech/Fintech/etc. Do this leveraging tools and service providers to help you keep costs down while putting core requirements in place. Why: Otherwise you shouldn’t expect to be able to sell to medium/larger enterprises or government clients.

#### MEDIUM
$25M-$100M annually: You need to start considering scaling your investments and addressing multiple frameworks. Ensure you have plans to address privacy and regulations, and bake these into your product/service development process. Fines get to be >$1M at this scale. You should be looking closely at 3rd party risk management — especially at smaller vendors. Solutions like trust pages and security questionnaire automation become high return investments at this scale. You may be operating in multiple geographies, so being aware of local variations like UK Cyber Essentials, DORA, NIS2 in EU, CPRA in California, becomes important.

#### LARGER
$100M annually: You become an interesting target for regulators. Public companies need to be aware of FTC rules, ITGC controls under SOX. You should have someone on your board who has responsibility for and competency in cybersecurity and enterprise risk management. In extreme cases rules can call for jail time for CISOs/executives who’ve shown gross negligence in security matters — in practice this has mostly related to failure to disclose breach information where required by law.

---

### Selecting technology and service partners

#### TECHNOLOGIES SHOULD AT A MINIMUM:
1. Provide you the ability to automate a wide range of evidence collection — critical as you scale standards, but saves tons of effort and makes it possible to achieve compliance for smaller firms. Look for key API integrations into areas like your Identity Provider, cloud stack, HRIS, MDM and key SaaS platforms. Also look for ability to pull in asset inventory and compliance posture.
2. Make it easy for auditors to conduct work without requiring manual evidence sharing. Look for a large number of integrated audit partners and make sure your selected auditor will actually use the platforms (this will save you time, effort and money).

> It is critical for businesses of all sizes to recognize the impending tidal wave of security demands.

Additionally, medium and larger firms will benefit from advanced capabilities.

### What about AI?
No conversation about security, compliance and regulation in 2024 could be complete without addressing the topic of AI. AI has a number of key impacts that every business should consider:
1. Threat actors Leveraging AI — enabling more sophisticated social engineering and other forms of attacks, invalidating traditional voice and video based verification techniques
2. Security for LLM models — testing and securing models against in-the-wild techniques like prompt injection attacks, data poisoning, bias scenarios, denial of service attacks and more
3. Governance and Privacy Challenges in AI Adoption — change in vendor behaviours in data usage for training purposes, updating data processing agreements, implementation of AI features in pr

[^1]: Reference to threat actors from The People’s Republic of China, Russia, and Iran.
[^2]: Personal Information Protection and Electronic Documents Act (PIPEDA), Royal Assent on April 13, 2000.
[^3]: Cyber Security Task Force (CSTF) mandate within Public Safety Canada, 2006.
[^4]: Canadian Cyber Incident Response Centre (CCIRC).
[^5]: Canada’s Cyber Security Strategy in 2010 and related Action Plan 2010-2015.
[^6]: National Research Council of Canada (NRC) cyberattack, 2014.
[^7]: 2018 National Cyber Security Strategy and National Cyber Security Action Plan (2019-2024).
[^8]: National Cybercrime Coordination Centre (NC3) operations and convictions.
[^9]: Canada’s anti-spam legislation (CASL), 2014.
[^10]: Communications Security Establishment Act and 2023-2024 Annual Report.
[^11]: General Data Protection Regulation (GDPR) and Data Protection Law Enforcement Directive, 2016.
[^12]: International Counter Ransomware Initiative (CRI).
[^13]: Cyber Security Action Plan, Public Safety Canada and Department of Homeland Security, 2022.
[^14]: National Cyber Threat Assessment.
[^15]: Cyber Security Act (Bill-26) and Countering Foreign Interference Act (Bill C-70).

---

e-ex-
1. Manage key workflows like risk assessments, employee
isting products, auto opt-in on privacy policy changes
onboarding and off boarding, access reviews, vendor risk
involving AI, data harvesting
management.
4. Data integrity/trustworthiness issues related to AI —
2. Provide cross-mapping of controls across multiple
hallucinations, quality control on AI chatbots and cus-
frameworks, collecting of custom controls/evidence,
tomer experience challenges, adoption speed vs. test
assigning control owners and sending notifications of out
case verification
of compliance controls
3. Easily share information on your security posture with
In conclusion
clients via tools like Trust Centers/Pages, automate secu-
rity questionnaire responses Given the continued challenges, it is critical for business-
es of all sizes to recognize the impending tidal wave of
PARTNERS SHOULD:
security demands from customers, partners, investors and
1. Be deeply versed in the tool you select to work regulators and incorporate plans to address these into their
with — not just have generic security expertise business strategies. Selecting automation tools, partnering
with services firms who specialize in security and privacy
2. Expertise in ISO27001/SOC2 and other relevant com-
compliance standards, baking certifications and regula-
pliance standards
tions into your product development and business strate-
3. Be able to provide a wide range of compliance related gies — these steps will allow you to stay ahead of the rising
services or a partner ecosystem — platform experience tide and build a resilient business in the years to come.
(as noted), pen testing, privacy support, audit partners,
By proactively integrating compliance and security mea-
managed threat detection, awareness training, policy
sures into their strategic plans, organizations can not
writing, vCISOs experienced in compliance, supporting
only mitigate risks but also gain a competitive edge in an
security questionnaires, vendor risk assessments, back-
increasingly regulated digital economy.
ground checks, etc, etc. More experienced partners will
have packages specifically for compliance and security
programs, less experienced providers will focus on hourly Michael Argast is Co-founder and CEO at Kobalt.io based out of
based billing models. Vancouver, BC. As the co-founder and CEO of Kobalt.io, Michael has
over five years of experience in providing cyber security programs that
4. Have a background in your particular industry or
address the needs of small and mid-sized organizations.
sector — B2B SaaS, health, financial, etc.
Securing Digital Frontiers by Michael Argast The State of Cybersecurity in Canada 2025 23

The State of AI
in Canada
by Helen Oakley
Introduction However, balancing opportunities with risks such as cyber-
security vulnerabilities and governance challenges remains
Artificial intelligence (AI) is revolutionizing industries and
critical to unlocking AI’s full potential.
reshaping operations worldwide. In Canada, AI is recog-
nized as a catalyst for economic growth, with transforma-
tive potential in sectors like healthcare, finance, manufac- Adoption Trends and Industry Efforts
turing, and cybersecurity. Significant federal and provincial
AI adoption in Canada is advancing, with notable variations
investments underline the country’s commitment to foster-
across industries. As of late 2023, 37% of large enterprises
ing innovation and addressing adoption challenges.
reported AI use, up from 34% earlier that year. Finance,
Globally, trends such as generative AI, platform engineer- healthcare, and technology sectors lead adoption, leverag-
ing, and autonomous systems are shaping the AI landscape. ing AI for applications such as fraud detection and person-
Canada’s strong foundation in AI research and talent alized healthcare solutions. In contrast, manufacturing and
development positions it well to capitalize on these trends. retail face barriers like high costs and skill shortages.
The State of Cybersecurity in Canada 2025 24

The federal government’s $2.4 billion initiative and pro- infrastructure, AI supports predictive maintenance and
vincial programs in Ontario, Quebec, and British Columbia resilience, underscoring the need for robust frameworks to
drive adoption and innovation. Initiatives such as the mitigate risks.
Pan-Canadian AI Strategy and the Artificial Intelligence
PLATFORM ENGINEERING AND GOVERNANCE
and Data Act (AIDA) aim to create a supportive ecosystem.
International frameworks like the NIST AI Risk Management Platform engineering simplifies AI integration, enabling
Framework and AI Integrity and Safe Use Foundation businesses, including smaller enterprises, to adopt AI with-
(AISUF framework) also guide responsible AI integration. out extensive expertise. Emerging AI governance platforms
address ethical and regulatory needs by offering tools for
monitoring, auditing, and risk mitigation. By aligning tech-
nological advancements with ethical considerations, these
The transformative
trends foster trust and accountability in AI systems.
potential of AI comes
Regulations for AI in Canada and Beyond
with significant risks AI regulation is a global priority as governments address
its rapid growth and associated risks. Canada’s proposed
that demand careful Artificial Intelligence and Data Act (AIDA) governs high-
impact AI systems in critical sectors like healthcare and law
enforcement, emphasizing risk management, transparency,
oversight.
and accountability. Businesses must prepare for compliance
by adopting robust governance frameworks.
Internationally, the EU AI Act enforces stringent, risk-
based regulations for high-risk systems, while the U.S.
Despite progress, concerns over data privacy, security, and
takes a flexible approach with initiatives like the National
workforce readiness persist. Addressing these challenges is
AI Initiative Act and evolving state-level laws in regions
essential for Canada to maintain its global competitiveness
such as California, Texas, and Colorado. Globally, nations
and fully realize AI’s transformative potential.
like Japan and Singapore focus on voluntary standards
emphasizing transparency and accountability. Canada
Technological Trends contributes to this alignment through initiatives like the
Global Partnership on Artificial Intelligence (G PAI) and the
AI technologies are advancing rapidly, transforming indus-
Canada–France Declaration, ensuring ethical AI standards
tries through key trends such as generative AI, cybersecuri-
and fostering innovation.
ty innovations, and platform engineering.
GENERATIVE AI AND AGENTIC SYSTEMS
Risks and Implications of AI
Generative AI combines creativity and autonomy, driving
The transformative potential of AI comes with significant
innovations in areas like fraud detection, personalized mar-
risks that demand careful oversight. For businesses, reli-
keting, and inventory management. Advancements in agen-
ance on AI for decision-making can introduce vulnerabili-
tic AI and multi-agent systems (MAS) enhance this auton-
ties such as algorithmic biases, data breaches, and adver-
omy. These systems independently perform complex tasks
sarial attacks. Governments face the challenge of ensuring
and collaborate toward shared goals, offering solutions in
that AI systems used in public services are fair, secure, and
supply chain management and smart cities. Together, they
aligned with societal values while maintaining public trust.
signal a shift toward more autonomous and collaborative
AI applications. For individuals, concerns about data privacy and the misuse
of AI remain paramount. The use of AI in surveillance rais-
CYBERSECURITY INNOVATIONS
es complex questions about balancing security needs with
AI-driven systems transform cybersecurity by enabling con- civil liberties. Additionally, the rise of agentic AI, which
tinuous threat detection and adaptive responses. Tools like refers to highly autonomous systems capable of operating
PentestGPT automate vulnerability assessments, enhancing with minimal human oversight, brings ethical concerns
defenses for both traditional and AI systems. For critical around accountability and control. These concerns are
The State of AI in Canada by Helen Oakley The State of Cybersecurity in Canada 2025 25

especially relevant when such systems influence critical decisions or operate in
high-stakes environments.
To illustrate the diverse risks associated with AI adoption, the table below
categorizes key challenges, highlighting their primary impacts and real-world
examples:
| Risk Name | Category | Primary Impact | Examples |
| --------- | -------- | -------------- | -------- |
AI-generated
Degradation of
| Misinformation  |     |     | misinformation,  |
| --------------- | --- | --- | ---------------- |
information ecosystems,
| and Erosion of  | Misinformation |     | clickbait headlines,  |
| --------------- | -------------- | --- | --------------------- |
loss of shared reality, and
| Trust |     |     | and manipulation in  |
| ----- | --- | --- | -------------------- |
reduced societal trust.
advertising ecosystems.
Automated hiring
Lack of accountability
decisions or legal
| Diffusion of  | Governance  | in societal-scale harm,  |     |
| ------------- | ----------- | ------------------------ | --- |
judgments influenced
| Responsibility | Failure | leading to systemic  |     |
| -------------- | ------- | -------------------- | --- |
by AI with unclear
biases and inequalities.
accountability.
|                |                | Creation of unreliable,   | LLMs generating         |
| -------------- | -------------- | ------------------------- | ----------------------- |
| Inaccurate AI  | Technological  | misleading, or incorrect  | hallucinated responses  |
Outputs Weakness results, reducing trust in  or incorrect outputs due
|     |     | AI systems. | to training limitations. |
| --- | --- | ----------- | ------------------------ |
AI assistants
Amplification of biases,
| Entrenched  |     |     | reinforcing user  |
| ----------- | --- | --- | ----------------- |
fragmentation of societal
| Biases and  | Fairness |     | preferences and biases,  |
| ----------- | -------- | --- | ------------------------ |
knowledge, and reduced
| Ideologies |     |     | hindering balanced  |
| ---------- | --- | --- | ------------------- |
political engagement.
decision-making.
Analysis of sensitive
Misuse of personal data,
personal data without
|                    | Privacy and  | undermining trust and  |                    |
| ------------------ | ------------ | ---------------------- | ------------------ |
| Privacy Violations |              |                        | consent, enabling  |
|                    | Security     | leading to potential   |                    |
unauthorized
exploitation.
surveillance.
|                |                | Strain on energy          | High energy demands       |
| -------------- | -------------- | ------------------------- | ------------------------- |
| Environmental  | Socioeconomic  |                           |                           |
|                |                | resources, societal       | for training AI models    |
| and Societal   | and            |                           |                           |
|                |                | disruptions, and growing  | impacting sustainability  |
| Costs          | Environmental  |                           |                           |
|                |                | resource inequalities.    | efforts.                  |
This table is not exhaustive but highlights critical risks and their implications.
Certain risks, such as misinformation, intersect with multiple categories, in-
cluding fairness and technological weaknesses, illustrating the complexity of AI
risk management. For a more detailed and exhaustive list of AI risks, resources
such as the AI Risk Repository and MITRE ATLAS provide comprehensive insights
and frameworks. These overlaps underline the importance of adopting holistic
approaches to AI governance.
Effectively addressing these risks requires collaboration among businesses,
governments, and civil society. By prioritizing transparency, accountability, and
fairness in AI systems, stakeholders can mitigate potential harms while fostering
trust, innovation, and societal resilience.
The State of AI in Canada by Helen Oakley The State of Cybersecurity in Canada 2025 26

Recommendations and Best Practices FOR EDUCATORS
To fully harness AI’s transformative potential while address- Educators play a vital role in preparing the workforce for
ing its risks, stakeholders must adopt a structured, collabo- AI-driven industries. Integrating AI ethics and applications
rative approach. into K-12 curricula builds foundational awareness, while
post-secondary programs should emphasize governance,
FOR POLICYMAKERS
cybersecurity, and critical infrastructure. Collaborations
Policymakers should advance frameworks like AIDA, har- with businesses for hands-on learning opportunities ensure
monizing them with international standards to strengthen alignment with industry needs and bridge talent gaps.
governance. Incentives such as grants and tax credits for
ethical AI research can drive adoption. Supporting initia-
Building a Resilient AI Ecosystem
tives like the AISUF framework helps businesses implement
maturity-based measures, ensuring secure scaling and By fostering collaboration among policymakers, businesses,
innovation. Engagement in international forums is essential and educators, Canada can create a resilient AI ecosys-
to align regulations and share best practices. tem. Foundational requirements, such as transparency and
compliance, provide a baseline for all stakeholders. For
FOR BUSINESSES
high-impact systems and critical infrastructure, applying
Businesses must build robust AI governance capabilities, advanced measures ensures resilience and public trust. This
starting with foundational measures like transparency, holistic approach will enable Canada to lead globally in AI
data privacy, and ethical principles. High-impact systems, governance, ensuring that AI supports growth, security, and
especially in critical sectors, require advanced practices equitable outcomes for all.
such as scenario-based testing, continuous monitoring, and
incident response frameworks.
Conclusion
CISOs play a vital role in securing AI systems. Key consider-
AI presents unparalleled opportunities for innovation and
ations include:
growth, but its adoption comes with challenges that must
• Addressing AI-Specific Vulnerabilities: be carefully managed. Canada is uniquely positioned to
Proactively mitigate risks like adversarial attacks, lead in AI research, development, and application, thanks
data poisoning, and model drift through tailored risk to its strong talent base, supportive policies, and ethical
management. focus.
• Ensuring Data Privacy: By addressing adoption barriers, mitigating risks, and fos-
Prioritize compliance with data protection regulations tering collaboration across sectors, Canada can ensure that
and embed privacy-by-design principles into AI systems. AI becomes a force for good — enhancing economic pros-
perity, improving public services, and safeguarding cyber-
• Promoting Ethical AI Use:
security in an increasingly digital world. The path forward
Establish policies to prevent biases and enhance AI ex-
requires vigilance, investment, and a shared commitment
plainability with fairness audits and ethical standards.
to ethical innovation.
• Continuous Threat Monitoring:
Use AI-driven tools for real-time anomaly detection and
Helen Oakley, CISSP, GPCS, GSTRT, recognized as one of the Top 20
dynamic system monitoring.
Canadian Women in Cybersecurity, is a leader in cybersecurity and AI
Maturity models, such as the AISUF framework, aim to transparency. She co-leads and contributes to groundbreaking pub-
offer a structured approach to scale securely and foster lications on AI and security for CISA.gov (AIBOM Tiger Team) and
innovation. Upskilling employees in AI, cybersecurity, and OWASPAI.org (Agentic AI Security initiative), shaping standards for
governance, along with partnerships with academia and transparency and security in the evolving AI landscape. As Director of
industry, can address talent gaps and prepare organizations Secure Software Supply Chains and Secure Development at SAP’s Global
for evolving regulations and threats. Security and Cloud Compliance, she champions security-by-design
across SAP’s engineering teams.
By aligning security with innovation, businesses can
ensure AI adoption drives growth while maintaining trust
and resilience.
The State of AI in Canada by Helen Oakley The State of Cybersecurity in Canada 2025 27

At Mastercard, we’re working to keep
people, businesses and governments more
secure as our digital ecosystem evolves
From AI-powered cybersecurity to biometric authentication, our technology
continuously assesses the landscape for evolving threats. Our innovations help
prevent fraud and financial crime before they happen, keeping people secure.
Our work doesn’t stop there. Learn how we are mobilizing partners across public
and private sectors to build trust, secure financial inclusion and pave the road to
financial health.

Bridging the cybersecurity
gaps: Preparing for change
in 2025
Presented by Mastercard
Generative AI is transforming the cybersecurity and fraud The Growing Impact of Generative AI
landscape, offering advanced tools to combat digital
Fraud has adapted to changing technologies, and genera-
threats, while enabling fraudsters to attack with unprece-
tive AI is accelerating this shift. By leveraging generative
dented sophistication. For Canadian businesses—particu-
AI, fraudsters can create sophisticated attacks using AI-
larly small and medium-sized enterprises (SMEs) in sectors
generated phishing emails or synthetic identities, which are
like retail, banking and forestry—this technological shift
harder to detect. They also scale operations with generative
presents both a challenge and an opportunity.
AI, which is enabling automation of account takeovers,
As fraud evolves alongside the rapid growth of digital authorization of push payment fraud and BIN attacks with
payments, it is essential for leading technology providers speed and precision.
to support Canadian businesses in navigating this complex
What’s even more disturbing is they can mimic human
risk environment. By embracing generative AI and building
behaviour using tools that generate lifelike text, voice and
a strategic, layered defence, SMEs can proactively prepare
even video, allowing them to impersonate legitimate users
for change and strengthen the future of their cybersecurity.
The State of Cybersecurity in Canada 2025 29

convincingly. For instance, card-not present (CNP) fraud 3. PARTNER WITH TRUSTED VENDORS
losses are estimated to reach $28 billion 1 by 2026, a 40
Generative AI deployment does not require a fully in-
per cent increase from 2023,1 driven by the rise of digital
house solution. Businesses can partner with industry
transactions. Generative AI allows fraudsters to leverage
leaders, leveraging tools such as Decision Intelligence Pro.
compromised data to exploit these vulnerabilities at scale.
This Mastercard generative AI-powered solution scans
However, the same technology offers fraud fighters a pow-
over 1 trillion data points to assess transaction risks in
erful tool to detect, predict and prevent attacks.
under 50 milliseconds.
Early modeling shows this technology improves fraud
Preparing for Change: A Practical Framework
detection rates by up to 300 per cent in some instances.
To combat rising threats, Canadian businesses can adopt a By working with trusted vendors, Canadian businesses
structured framework to integrate generative AI into their can enhance fraud mitigation without significant upfront
cybersecurity strategies. investments.
1. ASSESS CURRENT MATURITY
Addressing Challenges
Businesses must determine their readiness for
generative AI: Adopting advanced cybersecurity measures isn’t without
hurdles. Businesses must ensure regulatory compliance, by
• Stage 1: No generative AI strategies in place.
navigating adherence to Canadian data privacy laws, such
• Stage 2: Strategies exist but lack implementation. as PIPEDA. Generative AI tools must be implemented with
transparency and ethical oversight.
• Stage 3: Vendor-led AI tools are deployed.
• Stage 4: Internal teams manage custom
AI-driven solutions.
Technology alone
Today, most businesses fall somewhere between stage 1
and 2. For them, reliance on stage 3 provides an effective
and scalable entry point to combat evolving threats without cannot solve the
overwhelming internal resources.
2. MAP THREATS AND USE CASES
challenges posed
Businesses should map fraud risks across the transaction
lifecycle:
by generative
• Pre-transaction: Synthetic identity fraud, CAPTCHA
evasion and account takeovers.
AI-enabled fraud.
• Transaction: Authorized push payment fraud, unautho-
rized payments and BIN attacks.
• Post-transaction: Payout fraud and chargeback abuse.
By understanding where fraud risks are highest, business- There is also a great challenge with data transparency,
es can identify opportunities for generative AI solutions, as the “black-box” nature of AI can complicate decision-
such as: making processes. Businesses should prioritize tools that
provide explainability, ensuring accountability in fraud
• Behavioural Biometrics: Detecting identity fraud by
detection systems.
analyzing user behaviour.
Most importantly, there must be internal alignment.
• Anomaly Detection: Identifying irregular transactions to
Implementing generative AI solutions requires cross-
flag fraud before it occurs.
functional collaboration, where fraud teams, IT depart-
• Synthetic Identity Detection: Recognizing AI-generated ments and legal teams must align on objectives, risks
accounts at the pre-transaction stage. and implementation strategies.
The State of Cybersecurity in Canada 2025 30

Building a Resilient Cybersecurity Culture
Technology alone cannot solve the challenges posed by generative AI-enabled
fraud. A resilient cybersecurity culture requires:
1. EMPLOYEE TRAINING:
Tailored education helps staff identify AI-driven phishing attacks, fraudulent
communications and irregular behaviours.
2. CLEAR COMMUNICATION:
Open dialogue across departments ensures a proactive approach to evolving
threats.
3. METRICS AND KPIS:
Tracking key indicators like fraud losses, false positives and detection rates en-
ables continuous improvement.
By fostering vigilance across the organization, businesses can strengthen their
defenses while improving response times to emerging threats.
Bridging the Gaps
Generative AI has created a dynamic and complex risk environment for
Canadian businesses. With its industry-leading AI solutions, Mastercard can help
bridge critical cybersecurity gaps by:
• enhancing fraud detection with tools like Decision Intelligence Pro, which
improves real-time decisioning;
• supporting identity verification through behavioural biometrics and AI-driven
risk scoring; and
• leveraging generative AI to monitor cyber risks and combat fraud throughout
the transaction lifecycle.
• delivering actionable threat intelligence insights that help to classify malware
types, identify threat actor relationships and recognize spear-phishing cam-
paigns before they can impact business systems.
Generative AI is not just a tool for fraudsters—it is an opportunity for businesses
to build smarter, more proactive defenses.
The rise of generative AI presents Canadian businesses with both a challenge
and an opportunity. As fraudsters become more sophisticated, businesses must
adapt to stay ahead. By assessing risks, partnering with trusted providers and
fostering a resilient security culture, businesses can navigate the generative
AI era confidently.
This article is based on “Generative AI: Preparing your fraud organization,” a whitepaper devel-
oped by Mastercard in collaboration with Glenbrook. For deeper insights and actionable strate-
gies, visit mastercard.ca to access the full report.
1 Datos Insights, July 2023.
The State of Cybersecurity in Canada 2025 31

Providing Cyber
Security in Real
Time
by Paul Da Silva
Introduction The increase in identities, and the increasing focus on iden-
tities by threat actors changes the dynamic for cybersecuri-
Following the rise of cloud and cloud-native technologies
ty. Organizations need to adapt their methods for protect-
(such as containers and Kubernetes), identities have in-
ing sensitive identity data with new technologies because
creased both in number and complexity, and these changes
existing, on-premise security technology is just not capable
pose a direct risk to enterprise security. According to the
of providing the level of identity security needed—especial-
2024 Trends in Securing Digital Identities report from the
ly in the cloud.
Identity Defined Security Alliance (IDSA), identity-related
breaches are on the rise, with 90% of organizations expe- This article examines emerging cybersecurity disciplines
riencing at least one identity-related incident in the past and technologies and offers recommendations for orga-
year, and 84% suffering a direct business impact as a result. nizations seeking to strengthen their Identity and Access
The State of Cybersecurity in Canada 2025 32

Management (IAM) strategies against evolving cyber that are changing constantly. Modern organizations can
threats in the cloud. no longer rely on periodic snapshots or reactive measures.
They need real-time, adaptive cybersecurity approaches
that offer continuous monitoring and penetration testing,
Why Traditional Cybersecurity No Longer Suffices
real-time analysis, real-time vulnerability assessment scans,
Traditionally, cybersecurity has been a scheduled and real-time identification of identity security anomalies, and
batched process: immediate responses.
• Security updates, patches, and system scans were
scheduled at regular intervals (e.g., weekly, monthly) be- Emerging Cybersecurity Disciplines: ITDR
cause primarily on-premise systems were relatively static
Today, disciplines like Cloud Security Posture Management
and didn’t require continuous maintenance.
(CSPM) and Security Information and Event Management
• Threat detection and response involved collecting data (SIEM) have achieved modern cybersecurity goals in the
over time and analyzing it in “batches” during specific cloud. Other disciplines, like Identity Threat Detection
timeframes, for instance after an incident or as part of and Response (ITDR), are just emerging in response to the
routine audits, rather than in real time. explosion of distributed identities beyond the traditional
network perimeter and the resulting increase in identity-re-
• Vulnerability assessments, compliance checks, incident
lated vulnerabilities and attacks. In fact, Gartner recently
response, and other security processes were performed
labeled Identity Threat Detection and Response (ITDR) as
manually and on a set schedule because organizations
one of the top security and risk management trends.
didn’t need to adapt instantly to emerging threats.
ITDR refers to the combination of security tools and
• Security policies and configurations were static and,
processes required to adequately defend identity-based
once established, only revisited during scheduled reviews
systems. Gartner defines ITDR as “a security discipline
rather than being dynamically adjusted to new risks or
that encompasses threat intelligence, best practices, a
changes in the environment.
knowledge base, tools, and processes to protect identity
systems. It works by implementing detection mechanisms,
investigating suspicious posture changes and activities, and
Modern threats evolve
responding to attacks to restore the integrity of the identity
infrastructure.”
quickly, and modern cloud-
The modern security challenges ITDR addresses include:
native environments are • Real-Time Security Evolution
Shifts identity protection from a periodic to a continuous
dynamic, with workloads
process with behavioral analysis, event detection and
investigation, and real-time mitigation of threats and
and identities that are
non-compliant accounts.
changing constantly.
• Cloud-Native Identity Risks
Addresses the dynamic nature of cloud identities in
Kubernetes and hybrid environments.
• Over-Permissioned and Stale Accounts
Scheduled processes are too slow and static for today’s Mitigates risks by discovering, identifying, and remediat-
threat landscape, and the gaps created by delayed updates ing over-privileged or inactive accounts.
or periodic checks can allow threat actors to compromise
• Misconfigurations
environments.
Proactively detects and corrects vulnerabilities in identity
Modern threats evolve quickly, and modern cloud-native systems and configurations.
environments are dynamic, with workloads and identities
Providing Cyber Security in Real Time by Paul Da Silva The State of Cybersecurity in Canada 2025 33

cluster versions are common, leaving organizations vulner-
What are Some of the Top Emerging Technologies
able to identity-based threats.
Powering ITDR?
ITDR OFFERS ADVANCED TOOLS AND FEATURES THAT
• Behavioral Analytics and Machine Learning (ML)
CAN HELP IDENTIFY RBAC ATTACKS:
Analyze user and entity behavior to detect deviations
from normal activity. New developments include ML • Risk scoring evaluates the security posture of identities
models trained to adapt to dynamic and containerized by combining insights from runtime data, cloud miscon-
environments like Kubernetes. figurations, and container vulnerabilities. This holistic
approach helps prioritize threats and streamline remedi-
• Identity and Access Management (IAM) Integration
ation efforts.
Centralize visibility and control over hybrid identity sys-
tems like Active Directory, Entra ID, and Okta. Emerging • Admission controllers enforce policies that align with
IAM solutions support automated least-privilege policies the principle of least privilege. By doing so, they prevent
in dynamic cloud environments. unauthorized users or services from accessing sensitive
resources.
• Modern Privileged Access Management (PAM)
Secure and monitor privileged accounts, enforcing zero • Access audit logs make it easier to investigate failed
trust principles across the identity lifecycle. Emerging or suspicious login attempts. Regular reviews of stale
PAM solutions address dynamic privilege needs in or inactive identities further reduce the risk of unused
DevOps workflows and containerized environments. accounts becoming attack vectors.
• Threat Intelligence and Automation technologies use • The recent introduction of Common Expression
AI-powered automation to enforce security policies and Language (CEL) in Kubernetes version 1.30 further ex-
respond to threats in real-time. New platforms integrate panded ITDR’s capabilities. CEL simplifies policy valida-
global threat intelligence feeds with identity-centric tion and enforcement, offering an alternative to tradition-
threat detection. al webhooks. This feature not only reduces complexity
but also supports integration with CI/CD pipelines and
GitOps workflows, ensuring security policies are consis-
Tailoring ITDR to Critical Systems & Dynamic
tently applied throughout the development lifecycle.
Environments: Kubernetes, Active Directory,
and Entra ID
ITDR and Active Directory (AD)
To effectively enhancing identity security across modern IT
environments, organizations need to addresses the unique Microsoft released Active Directory with Windows Server
challenges of their specific platforms. Kubernetes, Active Edition in 2000, and it is still the main directory in use by or-
Directory, and Entra ID are foundational components of ganizations worldwide. With such widespread use, it is often
many organizations’ identity and access ecosystems, and a target for attackers who aim to take control of the directo-
each presents distinct vulnerabilities and operational ry and deploy ransomware or exfiltrate sensitive data.
nuances.
AD’s legacy nature makes it susceptible to misconfigu-
ITDR offers tools and methodologies that can be adapted rations and credential misuse, which can lead to unau-
and tailored to mitigate the specific risks of these systems, thorized access, privilege escalation, and domain-wide
enforce least-privilege access, and maintain a robust security compromises.
posture in real-time.
ITDR ADDRESSES THESE RISKS WITH:
• Event Monitoring
ITDR and Kubernetes Identity and Entitlements
Collecting and analyzing security logs, metadata, and
Management (KIEM)
access control lists (ACLs) to identify unusual activity and
Kubernetes environments present significant security detect misconfigurations.
challenges, particularly around Role-Based Access Control
• Active Directory Certificate Services (ADCS)
(RBAC). RBAC in Kubernetes allows administrators to set
Proactively uncovering vulnerabilities in certificate
granular permissions for resources, like pods and deploy-
management that attackers could exploit for privilege
ments. However, managing these permissions is complex,
escalation.
and misconfigurations, excessive privileges, and outdated
Providing Cyber Security in Real Time by Paul Da Silva The State of Cybersecurity in Canada 2025 34

• Privilege Management permissions they need, and continuously evaluate and
Tracking privileged accounts and ensuring least-privilege enforce these policies as your environment evolves.
principles are applied to prevent unauthorized access to
3. Leverage Automation
sensitive resources.
Replace manual processes with automated tools for
• Incident Response threat detection, risk scoring, and remediation.
Providing detailed visibility into events, such as failed
4. Integrate Real-Time Monitoring
authentications or unauthorized privilege escalations, to
Invest in solutions that offer continuous monitoring and
streamline threat investigation and remediation.
real-time insights. Focus on platforms that can detect
anomalies, identify misconfigurations, and provide ac-
ITDR and Entra ID (Azure AD) tionable recommendations.
Entra ID (formerly Azure AD) is a cloud-native identity 5. Secure Your Hybrid Environment
provider critical to securing access to modern cloud ap- Address the unique challenges of bridging on-premise
plications and services. As a cloud-native environment, it systems, like Active Directory, with cloud-native plat-
requires dynamic and context-aware threat detection. forms, like Kubernetes and Entra ID.
ITDR ENHANCES ENTRA ID SECURITY BY: 6. Educate Your Teams
Equip your IT and security teams with training on mod-
• Role and Scope Management
ern security principles and the tools they’ll use to im-
Monitoring role assignments and ensuring strict adher-
plement them, and foster a culture of proactive security
ence to least-privilege principles.
awareness across your entire organization—not just your
• Conditional Access Integration security team—to ensure the smooth adoption of re-
Enforcing dynamic access controls based on user behav- al-time security practices.
ior, location, and risk factors to minimize attack surfaces.
7. Plan for Scalability
• Privilege Escalation Mitigation Ensure your security solutions and processes can scale
Detecting and responding to attempts to misuse role with your organization’s growth and adapt to new tech-
assignments or administrative privileges. nologies or threats.
• Continuous Assessment In today’s complex cybersecurity landscape, where attackers
Evaluating identity security posture in real-time to are much more likely to log in than hack in, having a re-
identify and remediate risks across cloud services and al-time, adaptive approach to cybersecurity is not just ben-
applications. eficial—it’s essential. By leveraging advanced cybersecurity
disciplines that leverage emerging technologies, you can
build a more resilient defense that will keep your organiza-
Conclusion: Moving from Legacy to Real-Time Security
tion one step ahead of evolving threats.
For organizations to withstand the onslaught of modern
identity-based attacks, transitioning from scheduled, legacy
Paul Da Silva is a Sr Solutions Architect at BeyondTrust, with over
security models to real-time, adaptive disciplines like ITDR
15 years of experience. Paul’s expertise covers a wide range of skills
is essential. To make this transition successful, consider
including Cyber Security Identity and Access Management (IAM), security
these key tips:
architecture, incident response, all things Kubernetes & container and
1. Start with Visibility extreme curiosity in how everything works.
Identify all the accounts, privileges, and access points
across your environment. Leverage tools that can provide
you with unified visibility into your cloud and on-premise
systems so you can map out your comprehensive identity
security posture.
2. Adopt a Zero Trust Mindset
Implement least-privilege access policies for all iden-
tities, ensuring that users and services have only the
Providing Cyber Security in Real Time by Paul Da Silva The State of Cybersecurity in Canada 2025 35

Strengthening Cybersecurity in Canada’s
Public Sector: Key Insights and Strategic
Recommendations
by Deryck Greer
In today’s interconnected world, cybersecurity is a crit- Overview of Canada’s Cybersecurity Framework
ical national security priority. As digital transformation
At the federal level, the Canadian Centre for Cyber
accelerates, countries face escalating threats from both
Security (CCCS) within the Communications Security
nation-state actors and organized cybercriminal groups.
Establishment (CSE) leads the country’s cybersecurity
Nation-states often engage in cyber espionage to gain eco-
initiatives, managing strategic guidance and coordinat-
nomic or political advantage, while sophisticated criminal
ing responses to incidents. However, challenges remain,
networks exploit vulnerabilities to disrupt services, steal
such as gaps in inter-agency collaboration as highlight-
data, and hold critical infrastructure hostage for ransom.
ed in the Auditor General’s Report on Cybercrime. The
The impact of these cyber threats can be severe, with reper-
National Cyber Threat Assessment 2025–2026 also un-
cussions not only for economic stability but also for public
derscores the growing risks from state-sponsored actors
safety and trust. Strengthening cybersecurity resilience at
targeting Canada’s critical infrastructure, governmental
the national level is essential for safeguarding Canadas
operations, and innovative sectors. To complement CCCS,
infrastructure, maintaining the integrity of its institutions,
the National Cybercrime Coordination Centre (NC3)
and protecting citizens from the fallout of cyberattacks.
was launched in 2020 by the RCMP as part of Canada’s
These challenges require a cohesive approach across fed-
National Cyber Security and Cybercrime Strategy. The
eral, provincial, and municipal levels, drawing on lessons
NC3 collaborates with law enforcement agencies, local
from partners across the globe and the United States.
governments, and private sector partners to address
The State of Cybersecurity in Canada 2025 36

cybercrime more effectively. It also works closely with the  Threat Assessment 2025-2026. Provincial governments
Canadian Anti-Fraud Centre (CAFC) on public cybercrime  collaborate with federal bodies, but there is a need for
reporting and awareness. more standardized approaches and additional support for
provinces with fewer resources to ensure consistent cyber-
At the provincial level, each province is responsible for se-
security measures nationwide.
curing critical infrastructure sectors within its jurisdiction,
such as healthcare, energy, and transportation. However,  At the municipal level, cities manage essential local services
there are notable disparities in resources and capabilities  such as water, emergency systems, and transportation, but
across provinces, with smaller regions often facing more  municipalities often have constrained budgets and limited
significant limitations. For instance, the 2023 ransomware  access to advanced cybersecurity tools. The 2022 ransom-
attack on Alberta Health Services underscored vulnera- ware attack on Saint John, New Brunswick, exemplifies
bilities in the healthcare sector, which is a frequent ran- these risks, revealing the vulnerabilities faced by smaller
somware target according to the Canadian National Cyber  municipalities. As noted in the 2021 report An Industry
Canadian Federal organizations with Cybercrime responsibilities
Source: Auditor Generals Report Combatting Cybercrime
Canadian Radio-
Communications
|     | Royal Canadian   |     |     | television and  | Public Safety   |
| --- | ---------------- | --- | --- | --------------- | --------------- |
Security Establishment
|     | Mounted Police |     |     | Telecommunications  | Canada |
| --- | -------------- | --- | --- | ------------------- | ------ |
Canada
Commission
Lead federal organi- National foreign  Enforces Canada’s  Functions as a
zation that addresses  intelligence agency  anti-spam legislation  centralized hub for
cybercrime and  and technical au- to have a safer and  coordinating federal
investigates criminal  thority that provides  more secure online  policy in a variety
offences that fall  support and advice  marketplace and  of areas, including
under its Federal  on cybersecurity. reduce the harmful  cybercrime and
|     | Policing branch. |     |     | effects of spam and  | cybersecurity. |
| --- | ---------------- | --- | --- | -------------------- | -------------- |
related threats on
Canadians.
| Canadian Anti-  | National Cybercrime  | Federal Policing   | Canadian Centre    |     |     |
| --------------- | -------------------- | ------------------ | ------------------ | --- | --- |
| Fraud Centre    | Coordination Centre  | Branch             | for Cyber Security |     |     |
Helps Canadian citi- Cooperates with  Works to provide  Defends the federal
| zens and businesses   | law enforcement     | protection to           | government’s net-     |     |     |
| --------------------- | ------------------- | ----------------------- | --------------------- | --- | --- |
| in reporting fraud,   | and other partners  | Canada and              | work; advises and     |     |     |
| gathers intelligence  | to help reduce the  | Canadians against       | assists other levels  |     |     |
| on fraud across       | threat and impact   | domestic and            | of government and     |     |     |
| Canada, and assists   | of cybercrime that  | international criminal  | the operators of      |     |     |
| police with enforce-  | targets Canadian    | threats, and cyber-     | Canada’s critical     |     |     |
| ment and fraud        | companies.          | crime.                  | infrastructure,       |     |     |
| prevention efforts.   |                     |                         | such as banks and     |     |     |
telecommunications
companies; and
provides support for
Canadian businesses.
Cybercrime Unit
Investigates the
most significant
cyber-threats to the
federal government,
national critical in-
frastructure, and key
business assets.
Strengthening Cybersecurity in Canadas Public Sector by Deryck Greer The State of Cybersecurity in Canada 2025 37

Under Attack: Protecting the Oil & Gas Sector it stated Vulnerabilities and Emerging Threats Across
that interconnected operational technology (OT) systems Key Sectors
in industries like oil and gas increase cyber risks for cities
OIL AND GAS
dependent on these sectors. Municipalities can benefit
from greater funding and support to implement cybersecu- The oil and gas industry’s reliance on interconnected IT
rity programs, which would enhance local resilience and and OT systems makes it particularly vulnerable. According
provide a more uniform defense across Canada. to the world economic report cyber adversaries target
this sector for economic espionage, aiming to steal intel-
lectual property and disrupt production. A 2023 ransom-
Cybersecurity Structure in the United States:
ware attack on Suncor Energy underscores the substantial
Comparing our closest ally
financial and operational impacts these attacks can have.
The United States takes a coordinated approach to cyberse- Key challenges in this sector include legacy OT systems,
curity across federal, state, and local levels, with significant secure remote monitoring, and the high value of intellectu-
resources allocated to federal agencies that support broader al property.
cybersecurity efforts. The Cybersecurity and Infrastructure
HEALTHCARE
Security Agency (CISA) plays a central role at the nation-
al level. Established within the Department of Homeland Healthcare is highly vulnerable to ransomware due to the
Security (DHS), CISA provides guidance, resources, and sensitive nature of patient data. In 2023, Alberta Health
response capabilities to protect critical infrastructure Services suffered a ransomware attack that disrupted
across the country. Following high-profile incidents like the patient care, and healthcare accounted for over 25% of ran-
SolarWinds attack, CISA has received increased funding somware incidents reported in Canada in 2022, as noted by
and expanded its mission to include enhanced inter-agency the NCTA. Outdated infrastructure, extensive data-sharing
coordination and public-private collaboration, emphasizing needs, and the sensitivity of patient records present unique
the importance of resilience in critical sectors. cybersecurity challenges in this sector.
In addition to CISA’s role, the United States has implemented
federal programs like the State and Local Cybersecurity Grant Emerging Threats
Program to support state and municipal efforts to strength-
Both the NCTA and Combatting Cybercrime report empha-
en cybersecurity defenses. The program provides grants to
size several emerging threats:
state governments, which can allocate these resources to
local governments to improve cybersecurity training, secure 1. AI-Powered Phishing: AI-generated phishing messages
critical infrastructure, and enhance threat detection capa- are increasingly sophisticated and harder to detect.
bilities. Additionally, National Guard cyber units can assist
2. AI-Exposed Software Vulnerabilities: AI is now being
in emergency situations, providing technical expertise and
used by hackers to identify coding errors in software that
rapid response to cyber incidents at the state level.
could be exploited by malware toolkits.
CISA also plays a critical role in establishing security stan-
3. Supply Chain Attacks: Targeting third-party vendors is a
dards and sharing actionable threat intelligence across all
growing risk, with cybercriminals exploiting access points
levels of government and private sector partners. To support
to compromise entire supply chains. Increasingly, hackers
these efforts, CISA provides technical remediation recom-
are injecting malware directly into third-party software
mendations and even offers free cybersecurity tools, which
products that are consumed downstream by customers,
help organizations improve their defenses without addi-
creating widespread vulnerability. A prominent example
tional budgetary strain. These resources include scanning
of this type of attack is the SolarWinds breach in 2020,
and testing services, guidance on security practices, and
where attackers injected malware into the company’s
technical support aimed at preventing and mitigating cyber
Orion software update, affecting thousands of custom-
threats. Together, these initiatives foster a cohesive cyber-
ers, including U.S. federal agencies and large corpora-
security structure that bridges national resources with local
tions. This breach underscored the risks of supply chain
needs, ensuring a robust, layered defense across the U.S.
vulnerabilities, as malicious code embedded in trusted
software updates can infiltrate numerous organizations
simultaneously.
Strengthening Cybersecurity in Canadas Public Sector by Deryck Greer The State of Cybersecurity in Canada 2025 38

4. Advanced Ransomware Tactics: Attackers are increas- focus on enhancing public-private partnerships to support
ingly using “double extortion” strategies, where data is collaboration on threat intelligence, following models like
both encrypted and stolen to demand higher ransoms. the U.S. JCDC to boost defenses in key industries, including
oil and gas.
The WEF’s “Unpacking Cyber Resilience” report further
highlights the need for resilience in sectors like energy and Sector-specific resilience strategies would also be valuable.
healthcare, stressing preparedness and system redundancy For example, in the oil and gas sector, adopting Zero Trust
to maintain operational integrity under attack. Architecture and securing IT/OT integration would address
unique vulnerabilities. In healthcare, upgrading outdated
systems, conducting regular cybersecurity training, and
Economic Impact and Strategic Recommendations
strengthening data encryption protocols would bolster
Cyber incidents are estimated to cost the Canadian econ- defenses. Additionally, enhancing supply chain security
omy over CAD 5 billion annually, with operational disrup- through robust vendor assessment protocols would mitigate
tions, recovery expenses, and reputational damage affect- risks across critical sectors.
ing multiple sectors. Ransomware attacks, in particular,
As an example, The National Council of Information Sharing
impose significant financial burdens on industries such
and Analysis Centers (ISACs) in the United States of America
as healthcare and energy. Meanwhile, challenges in pros-
consists of 27 member organizations, each dedicated to en-
ecuting cybercrime persist, as highlighted by the Auditor
hancing cybersecurity resilience within specific sectors by fa-
General’s Report on Cybercrime, which notes limited
cilitating information sharing and threat intelligence among
law enforcement resources and the resulting difficulty in
companies in their respective industries. These ISACs
bringing cybercriminals to justice. To strengthen Canada’s
cover a wide range of sectors, including energy, healthcare,
cybersecurity posture, expanded federal resources and co-
financial services, and transportation, enabling industry-spe-
ordination would enhance the CCCS’s capacity to manage
cific collaboration to address common threats and vulner-
complex cyber threats. Establishing a centralized body, sim-
abilities. By providing timely, relevant intelligence, ISACs
ilar to the U.S. Joint Cyber Defense Collaborative (JCDC),
play a critical role in strengthening sector-specific defenses
could further improve inter-agency alignment.
and improving coordinated responses. Establishing similar
sector-focused information-sharing hubs in Canada would
Losses from Fraud in Canada
reinforce cross-industry defenses and improve coordinated
responses to sector-specific threats.
$567
2023
million Conclusion
Canada faces significant cybersecurity challenges, with
$530
critical sectors increasingly susceptible to complex cyberat-
2022
tacks. The National Cyber Threat Assessment 2025–2026
million
emphasizes the importance of a proactive, coordinated ap-
proach. Embracing strategies that draw on successful U.S.
$383
models, along with increased federal support and enhanced
2021 Source: sector-specific defenses, will be essential for Canada to for-
million National Cyber Threat tify its digital resilience and protect its essential infrastruc-
Assessment 2025-2026
ture against evolving cyber threats.
For provincial resilience, a standardized cybersecurity
framework with federal support could provide provinces Deryck Greer is the Chief Information Security Officer for Protexxa. He
with consistent protections across critical sectors. This is a former security cleared senior cybersecurity and intelligence leader
model, resembling U.S. state-level support structures, with over 18 years of professional practice across multiple domains
would ensure that smaller provinces have access to essen- including but not limited to; cyber intelligence, cyber operations, and
tial resources for defense. Similarly, a dedicated funding law enforcement.
program for municipalities could equip local governments
to build cybersecurity teams, improve threat monitoring,
and modernize critical infrastructure. Canada should also
Strengthening Cybersecurity in Canadas Public Sector by Deryck Greer The State of Cybersecurity in Canada 2025 39

Cyber risk can’t be solved with
technology alone
by David Shipley
For more than 50 years, since the advent of the first anti- terms of per cyber dollar spending, cybersecurity awareness
virus tool Reaper,1 the world has been more focused on has gone from 1.4 cents per cyber dollar spent to 3.5 cents
using technology tools to combat digital threats than it has per cyber dollar by 20276, a 150% increase but still only a
been in dealing with the human aspects of cybersecurity, tiny part of the overall spend.
by a significant margin.
While admittedly part of the reason for the escalating loss-
In the last 15 years, spending on cybersecurity global- es despite the surge of investment is an ever-increasingly
ly has surged from $31 billion in 20102 to an estimated hostile online environment driven by major geopolitical,
$285 billion by 20273, an 819% increase in spending, yet technological and criminal shifts over the past 30-years,
paradoxically the threat environment has failed to improve arguably the fact that we keep focusing mostly on tech-
in any appreciable way. Over the past decade, cybersecu- nological solutions to the problem (and getting the same
rity awareness spending is estimated to have grown from abysmal results) instead of increasing the money and time
$1 billion in 20154 to as much as $10 billion by 20275. In investment on the human side of cybersecurity is part of
the overall story.
Cybersecurity Global Spending
The clues hidden in the word cyber
The word cyber comes from the Greek word, kybernetes.7
$285B
Norbert Weiner, father of the field of cybernetics and an
$10B
MIT mathematician and philosopher, borrowed this Greek
word with deliberate intention. Weiner wanted to find
$31B
$1B a way to encapsulate the three critical elements and the
relationship between those elements that his new science
would study.
General Awareness Kybernetes, which means the helmsman or steersman on a
2027 2010 2027 2015
ship, perfectly captures this concept. If you picture in your
The State of Cybersecurity in Canada 2025 40

mind’s eye an ancient Greek ship, at the back of this ship is Often firms make bold claims about the efficacy of technol-
the first element of cyber: the human. In their hand is the ogy controls. Take e-mail filters, many of which claim to
oar, the rudder, the ship’s steering wheel, which represents have phish catch rates as high as 99.98%13, but in fact can
technology: the second element. The third and final ele- have false negative or phish leakage rates as high as 30%.
ment in this image is control. In Beauceron Security’s real-world testing over more than
six months, Microsoft’s Advanced Threat Protection had an
Humans in control of the technology they create is the
8.5% to 9% leakage range.
story of progress, from the earliest and most powerful
transformational technology we ever invented, fire, to The leakage range comes from a review of at all the e-mails
the modern digital economic nervous system that is the Microsoft said it stopped, including false positives, and
Internet today. then added all the real phishing e-mails that had been
delivered to employee’s inboxes that were then spotted and
The story of technology in control of humans rarely ends
reported by employees. We then used the employee report-
well, whether it’s Skynet and Terminators in the famous
ing rate percentage from phishing simulations to calculate
movie franchise, or Tesla “full self-driving” cars that keep
how many real phishes may have been delivered but not
killing people on highways, or the Boeing Max 8 disasters
reported.
where flawed sensors and software killed hundreds by
taking control from the jets’ pilots; the evidence is clear. We The reality of technology is that if it is built by humans,
can’t technology ourselves out of cyber risk. it will always be as beautifully flawed as its creators and
there will always be creative human minds that will find
ways to defeat it.
Humans in control of the
This isn’t to say that organizations should abandon technol-
technology they create is the ogy security controls or that technology security controls
built with a defense-in-depth approach do not provide
story of progress, from the
clear, demonstratable value.
earliest and most powerful
A well-educated and well-motivated team combined with a
transformational technology robust, positive security culture is the equivalent of a well-
trained defensive driver in a modern car in busy traffic. The
we ever invented, fire, to addition of technology controls in the car such as blind spot
assistance, adaptive cruise control and forward collision
the modern digital economic
alerts augment the drivers’ skill and enable the greatest
nervous system that is the possible safety.
Internet today.
The essential components of human-centric
cybersecurity
Even the current zeal around technology security focused There are four critical elements to human-centric cyberse-
concepts like zero trust8 ignores the reality that the tools curity: people, process, culture and technology. These four
we depend on to enforce that concept and ensure security aspects are critical to developing comprehensive approach-
themselves contain flaws as the products of humans. es that can enable organizations to reduce cyber risk and
thrive in a digital environment.
Take the example of a flaw in one of the world’s most popu-
lar e-mail filters that allowed millions of phishing e-mails
to impersonate well-known brands9 or the flaws in popular
firewalls10 that allowed them to be used against defending
organizations11. Then there’s also the human error that can
come from how client organizations implement security
1. PEOPLE
tools, such as cloud-based e-mail filters. In one academic
study, it was estimated that 80% of .com and .edu domains First and foremost, do the people in an organization have
using cloud-based e-mail filters had misconfigured them in the knowledge and the motivation to apply that knowledge
a way that attackers could use to deliver phishing attacks12. in their specific roles? This requires going beyond tired
Cyber risk can’t be solved with technology alone by David Shipley The State of Cybersecurity in Canada 2025 41

approaches of simply mandating peo-
ple to take computer-based training as
part of compliance regimes. It re-
quires going from security awareness 3. CULTURE
training (SAT) to security behavior
In a Forrester study in security cul-
and culture programs (SBCP) an ap-
ture, which included responses from
proach that merits further exploration
1,161 people, 758 unique definitions
on its own.
were given for security culture14. A
third of respondents said security
culture was compliance with secu-
rity policy. A quarter of respondents
said it had to do with awareness and
2. PROCESS understanding of security issues.
A fifth of respondents said it was
It’s one thing to ensure education is
the recognition that security was a
available and that people are motivated
shared responsibility throughout the
about security; it’s another to ensure
organization.
that processes are in place to support
and reinforce that work. A glaring In our work, Beauceron has proposed
example in most organizations is the a new definition of security culture.
lack of follow-up to end users who Our definition of security culture is
report suspicious e-mails as they have the norms and values in an organiza-
been educated to do through security tion, expressed and implied, in how
awareness and engagement programs. individuals and leadership make deci-
Less than 10 percent of organizations sions about their use of technology.
in our experience are doing this work,
We help measure this through metrics
though those who do it see as much as
around individuals’ knowledge, per-
a 50% higher report rate.
ception, motivation and the organiza-
Organizations that have tools to help tion’s process and technology related
automate the response to reported to cybersecurity. Organizations with
suspicious e-mails can scale this work a positive security culture not only
and tailor the responses with just- benefit from reduced risk, but they
in-time learning about the reported also make good decisions about when,
e-mail. In our experience, as many where and how to use technology to
as one in four reported e-mails can further their goals.
be legitimate business that requires
employee follow-up and attention.
Closing the feedback loop not only en-
courages reporting, but it also reduces
unintentional negative productivity 4. TECHNOLOGY
impacts of suspicious e-mail reporting.
As noted earlier, technology controls
Process goes beyond this specific to mitigate cyber risk remain essential
example and includes everything from within a human-centric cybersecuri-
ensuring people know the who and ty strategy. Relying on people alone
the how of getting help with a security would be ruinous for organizational
concern or question. It also involves productivity. This would be the equiv-
ensuring leadership knows how their alent of building a modern car and
incident response plan and processes expecting it to be propelled by the
work through regular practice via occupants with their feet, like the cars
tabletop exercises. in the Flintstones.
Cyber risk can’t be solved with technology alone by David Shipley The State of Cybersecurity in Canada 2025 42

Technology goes beyond mitigating that security awareness had to be
controls for cyber risk such as e-mail about more than knowledge dissem-
filters, firewalls and endpoint detec- ination. It must be about approaches
tion and response. It also involves and content that motivates people to
the design of the software and tools care about cybersecurity. Even in the
people use every day. For example, context of the US defense sector in
one of the greatest security innova- the cold war, motivation was noted as
tions Microsoft Outlook could include a persistent challenge:
would be a warning when someone
“For the vast majority of personnel,
has been reading and replying to
security concerns are a low priority…
e-mails for too long, encouraging
Even during the times that they are
them to take a break. Think the coffee
engaged in security-related tasks,
icon that modern cars can display if
their motivation to succeed in these
drivers are detected to be weaving in
tasks will be low. Security education
a lane potentially due to exhaustion.
must either find ways of raising mo-
It is worth noting that there’s a spe- tivation or of ensuring that security
cial caution about the intersection is protected even when motivation is
of technology controls for cyber risk low…”16
and the perceptions team members
What’s fascinating about the Security
have about the effectiveness of those
Awareness in the 90s symposium pa-
controls. In our research, employees
per published by the US Department
who believe security technologies
of Defense in December 1990 is how
such as e-mail filters, firewalls and
applicable it remains today and how
endpoint detection completely pro-
far ahead of its time it was in the
tect them from Internet threats have
context of the modern challenges of
average phishing e-mail click rates
information security, not only for the
that are up to 97% higher than those
defense sector, but now the entire
who don’t believe such tools provide
economy.
complete protection.
“Part of the motivation problem is the
The key to unlocking the potential
lack of natural rewards. Security mea-
of people, to help them understand
sures, by their nature, are successful
your processes and to leverage them
only when nothing happens. Feedback
to the best advantage, to creating and
on security related tasks is almost
sustaining a positive security culture
always negative. Because rewards are
and to enabling good choices about
far more effective training devices
technology, is robust security en-
than punishments, security educators
gagement, education and motivation
must find ways of introducing positive
(SBCP) program.
feedback into their efforts or ways
of living with the reduced training
From Security Awareness Training effectiveness provided by negative
(SAT) towards Security Behaviour reinforcement.”17
and Culture Programs (SBCP)
Somehow, over the past 30 years, as
The need for information security security awareness evolved beyond
awareness and the potential to build the defense sector and was adopted
platforms and use computer-based throughout every industry as they
training goes back more than 30 embraced digital technologies and the
years15. It’s worth noting that 30 years Internet to fulfill their missions, the
ago a key issue was identified that importance of motivation was lost.
has been lost over the years; the idea
Cyber risk can’t be solved with technology alone by David Shipley The State of Cybersecurity in Canada 2025 43

The loss of focus on motivation is likely tied to the initial The top 10% of organizations have median phishing simu-
evolution of security awareness as a largely unwelcomed lation report rates of 56%, which is more than double the
add-on to already overworked information technology overall median report rate across our entire customer base.
teams. As chief information security officers became a key
part of the leadership of organizations, as threat actors use
The components of an effective SBCP program
of social engineering (the expert use of emotional manipula-
tion via e-mail, known as phishing) exploded, security train- There are three key parts of an effective security behaviour
ing was seen as a way of dealing with the “people problem” and culture program. These components are tied to previ-
and or as mostly a compliance check-the-box activity. ous neuroscience work in the workplace, notably Dr. David
Rock’s SCARF model. The three components of a modern
SBCP program are: evaluate, motivate, and educate.
1. EVALUATION
People become more
For measurement, organizations must first establish a
qualitative baseline of employees’ knowledge and atti-
likely to click on phishing
tudes. Often such measures, conducted with surveys, are
dismissed by technology centric cybersecurity profession-
e-mails when they think
als in favour of qualitative data from systems. However,
that ignores that the only way to ascertain what someone
either their organization
knows and believe is to ask them about it and to listen to
what they tell you. Surveys can yield tremendous insights,
is not a target, or they
as our research has shown. Answers to these surveys can
be compared to qualitative security performance data (for
aren’t personally a target
example, phishing simulation click and report rates), to
understand the potential risks of some beliefs or attitudes.
for cybercrime.
One such example mentioned earlier is the framing bias
that people may have around the efficacy of technology
controls. People who see technology controls as 100%
protection become much more prone to click on phishing
e-mails, with the median click rate for that group being
The stupid people fallacy 7%, compared the median click rate for those who strongly
disagreed, which was 3%.
The “people problem,” also known as the “humans as the
weak link or stupid user problem” in security, remains Another bias we’ve seen from this data includes optimism
deeply flawed. First, it presumes that technology is not bias, which is the natural tendency for humans to think
flawed itself, which as noted earlier with examples of that bad things are more likely to happen to someone else
zero-day exploits for firewalls, e-mail filters and more, is rather than to themselves. People become more likely to
clearly not the case. There is however a deeper argument click on phishing e-mails when they think either their or-
against the “human as the weakest link” fallacy. If an orga- ganization is not a target, or they aren’t personally a target
nization was truly filled with stupid people, cybersecurity for cybercrime.
is not the biggest risk. The fact it’s filled with stupid people
Conversely, people who do believe they play an important
would be the biggest risk.
role in protecting their organizations or that cybersecurity
Most organizations are not full of stupid people. Most team is everyone’s business are much more likely report suspect
members in an organization not only want to do the right phishing e-mails.
thing, but they are also the organizations most valuable
2. MOTIVATION
competitive asset. Beauceron’s research has consistently
found 90%+ of organizational members care about the As humans, we’re incredibly sensitive to elevation or loss
important role they play in cybersecurity. of status and are intrinsically motivated to pay attention to
such changes. While employees can be motivated through
The challenge for security educators is ensuring people
quiz scores or thank you messages after they report
know why and how to apply security knowledge provided.
Cyber risk can’t be solved with technology alone by David Shipley The State of Cybersecurity in Canada 2025 44

phishing simulations, providing more Testing the effectiveness of knowledge
feedback creates a powerful motiva- dissemination is critical. Anti-phishing
tor. Our work has shown that systems education done with effective, fair
such as competitions or an easy-to-un- and rewarding phishing simulations
derstand cyber risk score can influ- are a continued critical component
ence learning and behaviour. This of an SBCP program. Our work has
effect, which we often compare to shown that organizations that do
what the Apple Watch or Fitbit did for monthly, adaptive difficulty phishing
exercise, allows us to tap in the status simulations on a per employee basis
portion of Dr. Rock’s SCARF model18. see the best risk reduction in terms
of lowest median click rates and the
A key component of this motivational
best results in report rates. While click
approach is reinforcement. As noted
rates can and do fluctuate based on
in the 1990s work, negative reinforce-
lure difficulty and will always contain
ment is a valuable tool, but it can only
an element of chance in that people
go so far. Organizations that do better
accidently click, report rates remain
at recognizing when people do the
a much more valuable indicator of
right thing – from reporting phishing
knowledge and attitude as people
e-mails to sharing security concerns
must recognize something is wrong
to using security tools like password
with the e-mail and are motivated to
managers well – will do better at cre-
report it.
ating motivational impact and positive
security cultures. A personal cyber This sequence of evaluate, motivate
risk score metric creates the mecha- and educate is a continuous cycle
nism to support positive and negative and it leads to measurable individual
reinforcement. cyber risk performance improvement
as well as positive security culture
3. EDUCATION
development and reinforcement.
When it comes to education, much
The work on the human side of cyber
more attention must be spent in SBCP
is not easy, quick, or something that
programs compared to old-school
can be solved with a technology
SAT approaches about the amount
platform alone. Yet it offers the single
of education provided at time, the
largest opportunity for further risk
key messaging, and frequency of
reduction with the best possible re-
education, as well as the delivery
turn on investment if done through a
mechanism. Recent studies claiming
modern, SBCP approach.
that anti-phishing simulations don’t
work were based on the failure of
one educational delivery mechanism: David Shipley is the CEO and Co-Founder of
post-click webpages that load static or Beauceron Security Inc., a New Brunswick-
interactive content. Those outdated based cybersecurity software firm with clients
methods do not engage people, with across North America. David is a certified
the vast majority staying on page less information security manager and frequently
than 30 seconds (and in some cases, writes and speaks about cybersecurity issues
less than 10 seconds). On the other across North America.
hand, educational modules focused on
emotional intelligence and assigned
through a learning portal were much
more likely to be engaged with and
much more likely to be successful.
Cyber risk can’t be solved with technology alone by David Shipley The State of Cybersecurity in Canada 2025 45

Building Digital Trust: A Strategic Imperative
Digital trust involves respecting privacy, safeguarding Certification to ISO standards offers numerous benefits to
data, managing cybersecurity threats, ensuring organizations across various industries.
transparency in data usage, and embedding trust in an
organization’s strategy and culture. There is a critical Whatever the size of your business, BSI can help establish,
link between digital trust, sustainable growth, implement, maintain, and continually improve your
competitiveness, and business success. information security and business management systems
to help you strengthen your operational resilience.
AI's impact on digital trust is significant; hence,
mitigating the potential risks associated with the
technology is essential. Trust in AI cannot be assured
by technical means alone and must involve the
development of ethical and transparent AI governance
structures.
Key standards fostering digital trust and
operational resilience include:
• ISO/IEC 27001:2022, Information security
management (cybersecurity)
• ISO/IEC 27701, Security techniques (data
governance and protection)
• ISO/IEC 20000-1:2018, Service management
(digital services)
• ISO/IEC 42001:2023, AI Management system
• ISO 22301:2019, Business continuity management
1-800-862-6752
Your partner in progress
inquiry.mscanada@bsigroup.com

Securing excellence: A guide to an
information security management
system
by Caio Cologni, Presented by BSI Group
Building cyber The average cost of a cyber breach in 2024 was USD
$4.88 million.
Data and connectivity are accelerating the extraordinary
transformation of organizations, from establishing digital The costs and disruptions caused by information securi-
ecosystems to optimizing supply chains and operational ty breaches are rising, leading to substantial damage to
procedures. However, as technology progresses, the cer- organizations.
tainty of cyberattacks, data breaches, and other operational
An ISMS can help protect organizations and reduce risk
disruptions grows.
by applying a robust and systematic approach to man-
The ability to manage information safely and securely has aging information. This standard can aid in defending
never been more critical. Organizations must build resil- an organization’s reputation, saving money, achieving
ience around their information security management sys- compliance, and reducing risks. Maintaining a secure
tems (ISMS) with an internationally recognized framework environment requires implementing industry standards,
like ISO/IEC 27001. This standard helps organizations demonstrating proper procedures, and promoting con-
prioritize safety, privacy, reliability, cybersecurity, and data fidence in clients, employees, and stakeholders through
ethics throughout their organization while maintaining an robust information security practices.
ISMS aligned with global best practices.
The State of Cybersecurity in Canada 2025 47

Top tips on making an ISMS impactful
There are 63 published standards
under the ISO/IEC 27000 family. They
provide information security best
practice recommendations covering
“The earlier that organizations talk to senior managers, the
privacy, confidentiality, and cybersecu- Top management
better it will go for them, so have those discussions early.”
commitment is key to
rity issues. Here are the most preva-
implementing ISO/IEC
lent standards organizations adhere 27001successfully. — John Scott, Manager, Overbury, leading UK fit-out and
refurbishment business
to:
• ISO/IEC 27001:2022
• ISO/IEC 27017:2015
• ISO/IEC 27018:2019
It’s important to make “The key to implementing the standard lay in getting staff
• ISO/IEC 27701:2019
sure an organization
to think about information security as an integral part of
works as a team for
the benefit of clients the daily business and not as an additional burden.”
Benefits and the organization,
avoiding silos. — Mr. Thamer, Ibrahim Ali Arab, Assistant General Manager, I.T.
Inspires digital trust in your
business
Provides greater reassurance to your
clients and stakeholders that data and
information are protected. “Don’t try and change your business to fit the standard.
Review systems, Think about how you do things and how that standard
Competitive advantage
policies, procedures, reflects on how you do it, rather than the other way
and processes in place –
Demonstrates robust controls are in it needs to add value. around.”
place to protect data.
— Paul Brazier, Commercial Director, Overbury
Protects your brand
Reduces the risk of adverse publicity
due to data breaches.
“This certification allows us to go one step further by
Helps reduce risks
Speak to clients and
offering our customers the peace of mind that we have
suppliers. They may
Adherence to the standard aids in be able to suggest the best controls in place to identify and reduce any risks
identifying risks by requiring the im- improvements and to confidential information.”
plementation of controls to manage or give feedback.
— Jitesh Bavisi, Director of Compliance, Exponential-eBavisi
reduce them.
Supports compliance
Supports compliance with local regu- Training staff to conduct
lations, reducing the risk of fines for internal audits of the “The course was loaded with practical exercises and
system can help them
data breaches. real-case scenarios and was structured in a way that it
better understand
encouraged participants to be interactive and share their
Fortifies business growth the requirements
and provide valuable experiences in information security.”
feedback on
Provides common guidelines across
potential problems — Nataliya Stephenson Manager, Information Security, NSW
different countries, making it easier to
or opportunities for Attorney General’s Department
do business globally and gain access achievement.
as a preferred supplier.
The State of Cybersecurity in Canada 2025 48

Certification to an ISMS Additionally, your certification serves
as a powerful distinguisher in the mar-
Obtaining ISO/IEC 27001 is a critical
ketplace. It provides tangible evidence
initiative that supports your compa-
to clients, partners, and stakeholders
ny’s ongoing success and resilience
that you take information security
in today’s ever-changing business
seriously and adhere to globally rec-
landscape. Adhering to the meticulous
ognized best practices. This can open
standards set forth by an internation-
doors to new business opportunities,
ally recognized framework helps to
bolster client trust, and give a compet-
fortify information security practices
itive edge in industries where security
and demonstrate a steadfast commit-
and confidentiality are vital.
ment to protecting your assets, main-
taining client trust, and supporting Adopting ISO 27001 is not just a
regulatory compliance. strategic move; it’s a proactive in-
vestment in your company’s future.
By prioritizing information security,
you can enhance your reputation,
safeguard assets, promote innovation,
Through regular
and drive sustainable growth in an
risk assessments, increasingly interconnected and digi-
tized world.
audits, and reviews,
Caio Cologni, Business Development
you can refine your
Manager, BSI Canada, is a recognized expert
in information security, cybersecurity, and pri-
security protocols,
vacy frameworks, with over a decade of experi-
adapt to evolving ence helping organizations with internationally
acclaimed standards like ISO/IEC 27001. As
threats, and stay business development manager at BSI Group
Canada, Caio works closely with organizations
ahead of emerging across industries to enhance organizational
resilience against cyber threats through certifi-
challenges.
cations, training, and strategic guidance.
His deep and comprehensive knowledge of
the ISO/IEC 27000 family of standards enables
him to provide actionable insights on building
a robust Information ISMS. His expertise,
This standard fosters a culture of con-
honed over years of dedicated work, has
tinuous improvement. Through regular
empowered countless businesses to safeguard
risk assessments, audits, and reviews,
data, build trust, and achieve compliance in a
you can refine your security protocols,
rapidly evolving digital landscape.
adapt to evolving threats, and stay
ahead of emerging challenges. This
process enhances your security posture
and promotes operational efficiency
and resilience across the business.
The State of Cybersecurity in Canada 2025 49

The Cyber Insurance Market
By Jonathan Weekes
Discussions around cyber over the past few years have Both New and Familiar Risks Threaten
shifted toward three areas: effective risk management, Company Profits
the pursuit of resiliency and the need to view cyber as an
Survey results from The Hub International 2025 Outlook
organizational risk rather than a technology risk. The in-
North American Report reveals that the key risks to prof-
surance industry has played a key role in not only driving
itability in 2025 continue to include cybersecurity risks,
an understanding of cyber risks across organizations in all
including deepfakes & AI fraud. While respondents report
industries but also providing practical solutions for com-
a high level of preparedness to managing the impact of
panies to assess, quantify and manage cyber risk, includ-
increased expenditures and business disruption on profit-
ing the use of risk transfer solutions such as insurance.
ability, they concede that they are less prepared to handle
climate change and cyber risks.
Key Risks Affecting Profitability in 2025
Canadian survey respondents expressed greater confidence
Increased expenditure 56%
in their preparedness to tackle key risks to profitability
Disruption to business operations 46% compared to their U.S. counterparts but rated themselves
as less prepared to respond to climate change, AI adoption
Climate change and natural disasters 45%
and regulatory changes. Of the executives surveyed, only
Deepfakes, AI fraud and 44% 44% stated that they are prepared to address cybersecurity
cybersecurity risks
risks and only 53% felt that they were prepared to tackle risk
Increasing use of artificial intelligence 35%
challenges tied to the increased use of artificial intelligence.
Governmental, regulatory
29%
and legislative changes
Economic challenges 19% Is Cyber Insurance Still Worth Exploring?
and unpredictability
Geopolitical risk 19% For years, cyber insurance has been an effective means for
Unpredictability of insurance organizations to transfer residual risk associated with pri-
8%
costs and availability
vacy and information security exposures. Cyber insurance
The State of Cybersecurity in Canada 2025 50

as a product has existed in one form or another since 1997, What does Cyber Insurance Coverage look like today?
when it was first offered by American International Group
With the average cost of a data breach in Canada sitting
(AIG), a US-based insurance company. Throughout the
at USD 4.66M, according to the IBM Cost of a Data Breach
years, these policies have evolved from offering coverage
Report 2024, cyber insurance remains one of the most
focused primarily on liability arising out of privacy breach-
effective ways for organizations to transfer financial risk
es, to comprehensive policies covering losses stemming
tied to cyber events. Cyber insurance policies continue
from everything from ransomware and data destruction to
to cover a broad range of risks through the provision of
non-malicious system outages.
coverage including:
Readiness to Tackle Risks and Mitigate Impact of Profitability • Cyber Event Management coverage, which reimburses
the policyholder for out-of-pocket expenses incurred to en-
Increased expenditure 61% gage legal support, computer forensics, public relations &
Disruption to business more, in the handling of a privacy or security breach. This
50%
operations
part of the policy also reimburses clients for costs to notify
Climate change and natural
41%
disasters and provide credit monitoring to impacted individuals,
Deepfakes, AI fraud and 44% whose confidential information may have been impacted.
cybersecurity risks
Increasing use of artificial 53% • Digital Asset Restoration Costs which, covers the
intelligence
costs to restore and/or repair lost or damaged data in
Governmental, regulatory
37%
and legislative changes the event of a network security failure and to determine
Economic challenges 60% what data cannot be restored, recollected, or recreated.
and unpredictability
This coverage is sometimes extended to include brick-
Geopolitical risk 31%
ing, which will replace network equipment, should it be
Unpredictability of insurance
costs and availability 38% rendered inoperable as a direct result of the information
security breach.
• Cyber Extortion, the area of coverage that has seen the
Any organization that has purchased cyber insurance for
highest severity of loss in recent years, reimburses the in-
an extended period would have seen drastic changes to the
sured for reasonable and necessary expenses incurred in
cyber insurance market over the past 5 years. The prolif-
responding to a network extortion threat, generally tied
eration of ransomware starting in 2018, amplified by the
to ransomware. This coverage includes negotiation costs
rapid expansion of remote work triggered by the global
and ransom payments to the party thought to be behind
COVID-19 pandemic, drove the cyber insurance industry
the threat, where permitted by law.
into a hard market. A “hard” insurance market refers to a
period during which the availability of insurance capacity is • Business Interruption & Extra Expense coverage
limited, and rates increase drastically, typically due to high- reimburses policy holders for lost income and extra
er-than-expected losses in any given underwriting year. expense resulting from a network security breach that
leads the actual and measurable interruption, suspen-
While cyber insurance has proven more onerous and costly
sion or impairment of an insured’s computer systems
for larger organizations to purchase over the past 3 to
or business operations. Coverage is often also extended
4 years, many buyers will agree that it not only forms a
to loss of income resulting from impairment of a third
critical part of their overall risk management strategy, but
party’s computer systems, SaaS, PaaS, IaaS on which the
also that the cyber insurance market has shown significant
insured relies upon for regular operation of its business.
signs of improvement over the past several quarters. Despite
The strongest policy wordings further expand coverage
the cyber insurance market softening over recent years, the
to include system failure as a trigger of coverage. While
HUB survey indicates no discernable increase in cyber insur-
the standard business interruption coverage will only
ance buyers year over year, with only 40% of respondents
respond when the cause of loss is a malicious third-party
reporting that they have some form of cyber coverage.
attack, the system failure coverage goes further include
loss of income resulting from any unplanned, uninten-
tional, or unscheduled network outage. A good example
of this is the widespread disruption tied to a CrowdStrike
update in summer 2024.
The Cyber Insurance Market by Jonathan Weekes The State of Cybersecurity in Canada 2025 51

• Privacy & Security Liability provides coverage for • Use advanced cyber benchmarking tools to help deter-
defence costs and damages arising out of the failure to mine the appropriate limits relative to an organization’s
protect sensitive personal or corporate information in any exposure
format, for which the insured is legally responsible. This
• Evaluate your organization’s exposure by considering
section would also cover insureds for defence costs and
important factors such as how much customer data your
damages arising out of the failure of network securi-
organization retains, your record retention policies and
ty, including unauthorized use of corporate systems, a
frequency of cyber security training for employees
denial-of-service attack, or the transmission of malicious
code.
What is next for cyber insurance?
• The Regulatory Proceedings coverage in cyber policies
responds to cover defence and investigation costs in the Much like cyber risks themselves, cyber insurance policies
event of an investigation by a governmental or regulatory will continue to see shifts in coverage, minimum require-
entity. Regulatory fines and penalties may be covered, but ments to qualify and value-added services offered by insur-
only where insurable by law. This is an aspect of coverage ers. The role of insurance brokers also continues to evolve,
where we have recently seen more claims, with changes with many of them focusing more on risk management
to privacy regulations in Canada and globally. services and solutions in addition to their core function of
placing insurance coverage on behalf of their clients.
When purchasing cyber insurance, it is critical for orga-
nizations to possess an understanding of what is covered In 2025, we will likely continue to see a further stabiliza-
as well as the types of events that might not be covered. tion of the cyber insurance market, with rates flattening,
Most cyber policies exclude things like telecommunica- coverage continuing to expand and more new buyers
tions and critical infrastructure failure, misconduct or entering the market. Cyber insurance should be considered
criminal acts of senior executives and bodily injury and when developing or revising an organization’s cyber risk
property damage. Cyber insurance buyers should dedi- management strategy, as it can help to address the residual
cate as much time to reviewing the exclusions under the financial risk that exists after implementing appropriate in-
policy as they do the insuring agreements. A good broker formation security governance and controls. We will likely
will take the time to walk through the various elements see continued pressure from boards and trading partners
of coverage, while comparing the offerings from various for organizations to procure or considering procuring the
insurance companies to pick the option that best aligns cyber insurance, so it is best to start the process sooner
with your needs. than later.
How can an insurance broker can help? Jonathan Weekes is HUB International Canada’s cyber practice leader,
Jonathan is responsible for developing client-specific product solutions,
• Brokers can provide insights into the health of your
advising clients on issues related to cyber risk, negotiating with insurers,
cyber security program through an objective, data-driven
and educating clients and colleagues on emerging technologies.
lens that identifies exposures and hidden risks
The Cyber Insurance Market by Jonathan Weekes The State of Cybersecurity in Canada 2025 52

Your data is everywhere.
Your defences aren’t.
Protect your hybrid environments and SaaS
applications with GlassHouse Systems
24/7 Managed Security (MSSP)
ghsystems.com/resilient-enterprise
Start with a no-cost data
resiliency assessment

A Novel Approach to Data Protection
by Christopher Lee, Presented by GlassHouse Systems
Cybersecurity attacks are all about data: paying $7.84 million on average, and the industrial sector
personal, corporate, healthcare, financial, pays $7.81 million on average.
or intellectual properties.
Interestingly, in most of the cases, breached organizations
Data-motivated attacks are becoming more frequent, ag- have security, controls, and policies in place, yet their criti-
gressive, and ultimately more costly. The attack style varies, cal data ended up in the wrong hands and was used against
but whether through ransomware, espionage, unauthorized them. The average financial damage caused by a single
disclosures, or destruction and denial of availability—cyber breach reaches startling heights, underscoring the reality
adversaries are fixated on acquiring your critical informa- that conventional approaches may be faltering.
tion, and they have a good reason.
Data Breach Costs in 2024 (CA $)
Sensitive information, such as personally identifiable in-
formation (PII), credit card numbers, corporate financials,
healthcare records, and intellectual property, is the orga-
nization’s bloodline and, in many cases, its secret sauce.
Once seized by an attacker, these assets quickly become the
organization’s largest threat.
According to the IBM Cost of Data Breach report, in 2024, $6.32 $9.28 $7.84 $7.81
Canadian organizations paid an average cost of CA $6.32
Million Million Million Million
million per data breach. The financial sector paid $9.28
Organization Financial Technology Industrial
million on average per breach, the technology sector is Average Sector Sector Sector
The State of Cybersecurity in Canada 2025 54

Despite deploying robust edge and seems to focus mostly on network se-
network security, threat intelligence curity, endpoint security and identity
tools, and security programs, orga- access management.
nizations across industries remain
For decades, information assets were
vulnerable. The facts suggest that
primarily stored as structured data
our traditional, and often dogmatic,
in database systems physically locat-
defence strategies might be failing to
ed inside secured data centres. The
offer real, long-term protection.
modality of a medieval castle defence
served as an excellent analogy for
It’s time to ask ourselves: are our data protection – establishing strong
efforts to prevent data breaches perimeter defence, employing com-
truly keeping pace with the petent guards to interrogate and
escalating threat? validate the identity and the permis-
sion of those who wish to access, and
We need to approach the problem with
ensuring they are not already com-
fresh eyes—ready to challenge existing
prised. Today, we are dealing with
assumptions and explore creative solu-
both structured and unstructured data
tions. Ask a cybersecurity expert today
(i.e. documents, spreadsheets, emails,
about their top priorities, and you will
etc.) containing sensitive information
hear them discuss areas such as ze-
subject to various regulatory compli-
ro-trust frameworks, employee educa-
ance requirements scattered all over
tion, and incident response. However,
the enterprise global computing eco-
the idea of fortifying the data itself
system: on-premises in the corporate
is noticeably absent from many “top
offices and employee home offices,
five” lists. This raises a critical ques-
end-user work and personal devices
tion: in a world where every system
(both managed and unmanaged),
is eventually breachable. This raises
cloud platforms (sanctioned and un-
a critical question: why aren’t more
sanctioned), and SaaS applications.
organizations placing the protection of
the data itself at the forefront of their The rapid adoption of a cloud-first
strategy? Perhaps it’s time to expand strategy for enterprise applications
our perspective and approach defence further complicates this. Due to the
in depth from both ends: perimeter-in complexity of software and cloud
and from the core outwards. technologies, developers may uninten-
tionally create vulnerabilities in the
enterprise data protection framework.
Most are still approaching it from a
No, I’m not talking about the quest
perimeter-in approach, focusing their
for secure software development - I’m
investments on network security,
referring to the separation of produc-
endpoint security, IAMs, etc.
tion data from test data, sanitization
Proportionally, we have witnessed a and protection of the test data, and
heightened recognition of the need extending protection to the data that
to improve the security posture and the cyber team might not know about
the protection of information as- (e.g., cloud storage under unofficial
sets. There has been an explosion cloud tenets).
of technological innovations to help
Hence, there has been a rise in Data
safeguard our information assets,
Security Posture Management (DSPM)
especially in today’s work-anywhere,
and Attack Surface Management
always-connected, agile, and hybrid
(ASM) products to expose data
computing world. However, the effort
and data assets. However, a holistic
The State of Cybersecurity in Canada 2025 55

approach is needed to address the How can we classify this data?
unstructured and shadow data across Analyze • PII, healthcare, financial, PCI, etc.
the entire organization’s technology
Discover How can we see what happens to
ecosystem (e.g. beyond the top three
this data over its lifecycle?
cloud providers and the most common
• Who/how it would be used, in-
SaaS applications) and to add the
Data Security tended retention, destruction, etc.
context (i.e. data owner, intended use,
Life Cycle
Protect
data classification, etc.) of the data it As we inventory the information as-
discovered/protects. Leveraging AI/ sets, we should also classify the data
Monitor
and
ML capabilities to automatically clas- according to their sensitivity, critical-
Manage
sify discovered data helps automate ity, value, and regulatory compliance
aspects of data discovery. Additionally, ratings. This ensures the ability to
Validate
an iterative interview approach with apply controls uniformly and con-
cross-functional stakeholders to con- sistently downstream. In addition to
textualize the results will ensure that data inventory, we should examine
4. Validate: Regularly assess the ade-
the best results are achieved. what controls have been implemented
quacy of controls and make neces-
for each asset. This concludes the
In their report, IBM found that the av- sary adjustments.
Discovery phase of the approach.
erage cost of a data breach jumped to
5. Monitor and Manage:
USD 4.88 million in 2024, a 10% spike ANALYZE
Continuously oversee the security
from 2023 and the highest increase
landscape, ensuring rapid incident The next step is to analyze the con-
since the pandemic. A rise in the cost
response. trols against the data classification to
of lost business, including operational
determine whether they are suffi-
downtime, lost customers, and cost of This systematic approach enhances
cient and robust. There are quite a
post-breach responses, totalled USD security and aligns with regulatory
few tools that we could leverage for
2.8 million, the highest over the past compliance and risk management
the analysis — CIS Critical Security
6 years. It’s clear that the typical ap- objectives, thereby safeguarding the
Controls (CSC), NIST Cybersecurity
proach, despite increased investment organization’s reputation.
Framework (CSF), etc. Personally,
and technological innovations, hasn’t
DISCOVER I prefer a holistic approach that
yielded the desired results.
overlays the Capability Maturity
You can’t protect what you don’t know.
Model (CMM) on top of the techni-
The first step is to establish an inven-
An inside-out approach designed cal prescriptive nature of CIS CSC
tory of data assets that your organiza-
to incorporate reasonable and and the breadth of NIST CSF. NIST
tion collects, process, and stores and
contextual security controls across CSF is the most adopted industry
answer the following questions:
the data lifecycle. standard for cybersecurity and maps
Who owns the data? very well to most (if not all) compli-
Let’s consider a data-centric approach
What types of data do we have? ance and risk management frame-
that applies security controls to how
• Structured data in a database, works. The result of the analysis
the information assets are collected,
files, emails, paper files, etc. can be refactored into the organiza-
where they are stored, and how they
tion’s Enterprise Risk Management
are used and managed. Where does this data come from?
(ERM) or Enterprise Security Risk
• End-users, employees, HR, fi-
1. Discover: Establish a comprehen- Management (ESRM) process for
nancial systems, R&D, 3rd party
sive inventory of data assets, identi- alignment and SLT support.
systems, etc.
fying ownership and classification.
PROTECT
Where is this data stored?
2. Analyze: Evaluate existing controls
• Personal devices, in the cloud, Common data protection controls
and their effectiveness against the
or on servers controlled by the include access control (i.e., access
classification of data.
organization. It will help identi- should only be provided to specific
3. Protect: Implement robust security fy potential vulnerabilities and job roles, on specific types of data,
measures such as access control, areas for improvement in data from specific endpoints, and at spe-
data encryption, and tokenization. security. cific times), data encryption (i.e., to
The State of Cybersecurity in Canada 2025 56

prevent unauthorized users from accessing the data even incident-handling program to take advantage of its around-
if they have access to the infrastructure hosting the data, the-clock coverage model and matured incident manage-
such as the file directory, database, email store, etc.), and ment and incident response process.
data tokenization (i.e., making the data usable for some
business processes without exposing it). There are tech-
Reduce the impact of data breaches with a process
nology solutions, like IBM’s Guardium for example, that
that aligns with business processes, regulatory
would accomplish them in a manner that works with most
compliance and enterprise risk management.
existing business processes and minimizes the burden on
the end-users (especially if data classification/labelling is The urgency of enhancing data protection measures is
done). In addition, it is vitally important to establish key more evident than ever. The combination of escalating
data management processes, such as data retention and cyber threats and the significant financial ramifications of
destruction policies. The most important thing here is to data breaches necessitates immediate action. By adopting a
ensure the investment level for data protection aligns with proactive, data-centric strategy, organizations can mitigate
the organization’s ERM/ESRM program. Sometimes, it can risks, reduce impact, and protect their most valuable assets.
be more straightforward and more economical to trans-
What is that proactive data-centric approach and how
fer the bulk of the risk to a 3rd party (e.g. cyber insurance
can you get started, you ask? Lean into an “inside-out”
underwriter, business process outsourcer, etc.) and focus on
approach to your program, with a good first step being to
residual risk internally.
execute a Data Security Assessment that focuses on discov-
VALIDATE ering your critical data, or at least a subset thereof. Take
an “agile” or iterative approach to Discovery, so that you
Now that we have completed the data discovery, assessed
do not get bogged down by trying to discover all of your
existing controls for adequacy, and implemented additional
data or all of your critical data. Discover a tranche of your
controls to bring the safeguards to an acceptable level, we
critical data, then follow the process outlined to Analyze,
need to ensure a cadence for repeated evaluation. This will
Protect, Validate, Monitor and Manage. Learn from the first
ensure that the controls remain effective despite techno-
data tranche and then rinse and repeat.
logical, organizational, and threat landscape changes and
that new data assets (especially those not stored in the Once started, the contextual insights gained and alignment
centralized data management solution, or Shadow Data) to various industry frameworks make it far easier to gain
are incorporated into the established data protection pro- senior leadership buy-in and support to sustain this for
gram. In addition, there needs to be a process for regularly years to come. Finally, the ability to convey data security
reviewing and auditing access to the data. in the context of business processes, regulatory compliance
and risk management language would surely enhance the
MONITOR AND MANAGE
level of engagement of business executives.
Lastly, data security incidents (e.g., policy violation,
suspected misuse, data breach, etc.) must be monitored
Christopher Lee works at Glasshouse Systems and has over twenty years
and responded to 24/7, 365 days a year. Incorporating
of extensive experience in cybersecurity, concentrating on advanced
artificial intelligence (AI) and machine learning (ML) to
threat detection and ensuring that client organizations strategically align
detect abnormal data usage would greatly improve detec-
their capabilities with their unique risk tolerance. He is a recognized
tion efficacy while reducing unnecessary burdens on the
subject matter expert in advanced Security Operations Center (SOC)
team due to false positives. It makes sense to integrate this
services and cybersecurity advisory services.
critical function with the organization’s existing security
The State of Cybersecurity in Canada 2025 57

Building Resilience
Through Cybersecurity
Awareness
by Junior Williams
The Growing Cost of Cyber Threats individual online safety can have cascading effects on orga-
nizational security, just as a company’s weak cybersecurity
In today’s digital age, cyber threats have become an un-
practices can jeopardize personal data. This interconnected
avoidable reality. Building resilience against these threats
reality demands constant vigilance and proactive measures
is critical for navigating an increasingly interconnected and
from everyone to navigate an ever-evolving and complex
challenging digital environment. The global average cost
digital ecosystem.
of a data breach reached $4.88 million in 2024, marking
the largest yearly increase since the pandemic (IBM Report).
This stark reality sets a n urgent tone for organizations of Personal Cybersecurity: A Vital Life Skill
all sizes. With most communication and financial transac-
On a personal level, staying ahead of online threats re-
tions conducted online, it’s essential for everyone to under-
quires learning new skills. For example, deepfakes—AI-
stand the basics of cybersecurity, regardless of their tech-
generated videos that impersonate real people—can trick
nical background. The boundaries between personal and
individuals into believing false information or even trans-
business cybersecurity are increasingly blurred. A lapse in
ferring money to scammers. Hands-on training becomes
The State of Cybersecurity in Canada 2025 58

invaluable for building practical knowledge and confidence consider their approach effective for the challenges of
in recognizing and avoiding these evolving threats. This today and tomorrow. This statistic highlights the urgency
training should be tailored to individual behaviors and for leadership to adopt more forward-looking strategies to
digital habits. For instance, users could practice identifying address the evolving threat landscape.
phishing emails, avoiding suspicious links, or managing
For businesses, cybersecurity awareness needs to be contin-
strong passwords to mitigate common personal cyber risks.
uously updated. One-off training sessions every year aren’t
According to Verizon, 68% of breaches involved a non-ma- enough because cyber threats are constantly evolving. To
licious human element, such as falling victim to a social en- address this, organizations must invest in dynamic training
gineering attack or making an error. This statistic highlights methods that engage employees meaningfully and regular-
the critical role of individual awareness and education in ly. Role-based gamified training modules, which use game-
reducing cyber risks. Websites like TryHackMe offer fun, like elements to simulate real-world scenarios tailored to
interactive lessons that help learners at all levels improve specific roles, can make this approach more impactful. For
their cybersecurity awareness and skills. For instance, the example, an employee in customer support could engage
free TryHackMe room ‘Web Application Basics’ explores in a simulation where they must manage a sudden surge of
topics such as HTTP, URLs, request methods, response customer complaints linked to a fake website impersonat-
codes, and headers, making it an excellent starting point ing their company, a scenario tailored to their daily inter-
actions, while IT staff might navigate a module designed to
detect unusual network activity in real time. This person-
alized approach ensures that training resonates with users,
6 8% making it both relevant and actionable.
Training should go beyond avoiding scam emails and focus
on role-specific threats and responsibilities. For instance,
employees in finance should learn about risks such as
fraudulent invoices and wire transfer scams, while HR staff
might explore vulnerabilities tied to sensitive employee
of breaches involved a non-
data. Tailored training ensures that cybersecurity feels
malicious human element, relevant and actionable, fostering deeper employee com-
mitment to organizational safety.
such as falling victim to a
Additionally, the new Govern function in NIST CSF 2.0
social engineering attack underscores cybersecurity as a critical enterprise risk.
Senior leadership is now expected to prioritize it alongside
or making an error.
financial and reputational considerations. By extending its
guidance beyond critical infrastructure to all organizations,
this framework highlights the necessity of universal cyber-
security vigilance, irrespective of an organization’s current
for understanding web-related cybersecurity concepts.
level of cyber maturity.
Similarly, their ‘Introduction to Ethical Hacking’ room
guides learners through the basics of penetration testing
and understanding system vulnerabilities, providing a prac- Technology as a Cybersecurity Ally
tical foundation for tackling real-world security challenges.
New technologies are also making cybersecurity education
Just like learning to drive or manage money, understanding
easier and more personalized. AI-powered chatbots are trans-
how to stay safe online is a vital life skill.
forming learning by offering interactive and tailored educa-
tional experiences. For instance, you could ask an AI, “Create
Tailored Business Training and Leadership in a five-question quiz about cybersecurity and provide a lesson
Cybersecurity based on my answers.” This kind of interaction makes learn-
ing more engaging and accessible for everyone, from execu-
The EY 2023 Global Cybersecurity Leadership Insights
tives to new hires. Importantly, this approach is not confined
Study (EY Report) found that only one in five Chief
to cybersecurity; it can extend to topics like programming or
Information Security Officers (CISOs) and C-suite leaders
financial literacy. Organizations can use these tools to build
Building Resilience Through Cybersecurity Awareness by Junior Williams The State of Cybersecurity in Canada 2025 59

cross-functional skills across teams, Human error accounts for more than
preparing individuals to navigate 80% of cyberattacks, according to the
diverse challenges. For example, em- National Institute of Standards and
ployees might utilize similar AI-driven Technology (NIST Blog). This under-
platforms to explore supply chain risk scores the importance of cultivating
management or improve strategic deci- habits like questioning unexpected
sion-making, creating a more adaptable messages, staying curious about po-
and capable workforce. tential threats, and proactively seek-
ing knowledge about emerging risks.
Such technologies play a transforma-
Building resilience against cyber threats
tive role in industries like financial
starts with fostering a culture that em-
services, where the stakes for cyber-
phasizes continuous learning and open
security are particularly high. Data
communication across all levels.
breaches in this sector can compro-
mise sensitive financial information, To move forward, organizations and
disrupt operations, and result in regu- individuals must actively invest in
latory penalties. According to Varonis their cybersecurity education and
(Financial Data Risk Report), financial practices. Whether by adopting ad-
services take an average of 233 days vanced technologies, implementing
to detect and contain a data breach. tailored training programs, or rein-
This prolonged timeframe—equiv- forcing everyday vigilance, the goal
alent to over eight months—allows is clear: build a resilient and secure
attackers ample opportunity to exploit digital environment. Now is the
vulnerabilities, damaging reputa- time to act—start by evaluating your
tion, revenue, and customer trust. current approach and taking steps
By leveraging AI tools that provide to strengthen your defenses today.
real-time threat analysis and integrat- It’s not just about memorizing a set
ing these with comprehensive aware- of best practices. It’s about staying
ness training, organizations can not informed and proactive. For organiza-
only shorten response times but also tions, this means embedding cyberse-
anticipate and prevent future breach- curity into the culture and ensuring
es. This proactive approach ensures a every employee understands their
more resilient security posture, critical role in maintaining security. It’s about
in an environment where agility and recognizing the connection between
foresight are essential. our actions—at home and at work—
and the broader digital world. With
the right tools and regular updates,
Building a Culture of Cybersecurity
cybersecurity learning can become an
Cybersecurity awareness hinges on active, engaging part of daily life.
adopting the right mindset, both
personally and organizationally. This
Junior Williams, a seasoned cybersecurity and
means fostering habits like regularly
AI professional with a wealth of experience
questioning the legitimacy of unexpect-
in programming, technology, investigations,
ed communications, staying informed
and consulting, has built an extensive career
about emerging threats, and taking
marked by adaptability to the rapid pace of
proactive steps to strengthen defenses.
technological advancements. His expertise
For example, an individual might devel-
has evolved from telecommunications to IT
op the practice of verifying unusual
infrastructure, where he developed a deep
requests through alternate channels,
understanding of computer systems, cyber-
while organizations could encourage
security, and the strategic implementation of AI
team discussions about recent phishing
solutions to drive impactful business outcomes.
tactics to build collective awareness.
Building Resilience Through Cybersecurity Awareness by Junior Williams The State of Cybersecurity in Canada 2025 60

cnI
snoituloS
ytiruceS
stpecnoCMAI
5202@
thgirypoC
Your Trusted IAM Partner:
Strategy, Implementation,
and Managed Services, all
in one place.
IAM | PAM | CIAM
www.iamconcepts.ca | info@iamconcepts.ca

Securing Digital Identity
in an AI-Driven World
by Fahad Kabir, Presented by IAMConcepts Security Solutions Inc.
The advent of artificial intelligence (AI) has profoundly One of the primary hurdles for IGA adoption has been
impacted numerous industries, and identity security is access certification fatigue. Employees often resort to “rub-
no exception. Generative AI, in particular, is revolutioniz- ber-stamping” approvals, bypassing the intended security
ing the way organizations approach Identity Governance checks. Similarly, role mining and role engineering have
and Administration (IGA), Identity Threat Detection and been persistent pain points, requiring vast amounts of data
Response (IDTR), and overall identity lifecycle manage- to identify meaningful patterns and ensure the right levels
ment. As the field evolves, the integration of AI promises of access.
not just efficiency but also meaningful innovation that
By leveraging generative AI, organizations will soon be
redefines user interactions and organizational security.
able to process large datasets more effectively and derive
actionable insights. For instance, an IGA tool powered by
Generative AI: Transforming Identity Governance generative AI will be able to recommend roles and access
levels based on historical data, risk patterns, and organiza-
Generative AI is emerging as a game-changer in identity
tional policies. A lot of this AI powered analysis capability
management, addressing longstanding challenges in IGA.
were available in leading IAM tools before. However, the
The State of Cybersecurity in Canada 2025 62

differentiator going forward will be making these tools tools often require specialized training, creating friction
much more user friendly and interactive by leveraging gen- between end-users and the technology. Generative AI flips
erative AI. This capability simplifies the decision-making this paradigm by making interactions more conversational
process, allowing users to ask intuitive questions such as, and intuitive. For example, instead of navigating complex
“What type of access should this new hire have?” or “What interfaces, users can pose natural language queries to the
risks are associated with this role?” Such user-friendly system. This shift not only increases adoption rates but also
interfaces, akin to interacting with ChatGPT, eliminate the ensures that identity management becomes a seamless part
need for end-users to possess technical expertise, democra- of daily operations.
tizing access to identity tools.
Imagine an HR professional onboarding a new employ-
ee. Instead of manually navigating the labyrinth of access
AI-Powered Enhancements by IAM Product Vendors permissions, they could simply ask, “What are the appropri-
ate access permissions for a junior analyst in the marketing
Leading Identity and Access Management (IAM) product
team?” The system, leveraging generative AI, would analyze
vendors are embedding AI fast into their solutions to deliv-
existing roles, assess potential risks, and offer tailored rec-
er more intelligent and efficient identity and access man-
ommendations. This streamlined approach empowers orga-
agement. These enhancements include:
nizations to maintain security without overburdening users.
1. Automated Role Mining and Engineering: Vendors are
incorporating AI to analyze access patterns, suggesting
optimal role structures, and simplifying the often tedious
One of the most
process of role engineering.
2. Intelligent Access Certification: AI-powered solutions
significant benefits
reduce certification fatigue by identifying high-risk access
points and prioritizing them for review, streamlining the
approval process. of AI in identity
3. Adaptive Risk Assessment: AI is being used to con-
tinuously evaluate risk in real-time, factoring in user management is
behavior, location, and device to provide dynamic access
decisions.
enhancing user
4. Enhanced Threat Detection: Vendors are leveraging
machine learning algorithms to detect anomalies, flag
suspicious activities, and provide actionable insights to interactions.
security teams.
5. Privileged Account Discovery and Protection:
Identifying privileged accounts across any large enter-
prises has been a challenge in the industry. AI powered
AI’s Role in Identity Threat Detection and Response
modern PAM tools will be much more advanced in scan-
ning an organization’s entire network efficiently, contin- Identity Threat Detection and Response (ITDR) is a crit-
uously analyzing and identifying privileged accounts that ical evolution in cybersecurity, as traditional tools like
might not be explicitly documented. SIEM and EDR have primarily focused on broader securi-
ty events and logs, often overlooking the vital context of
These innovations not only improve security but also en-
identity data. With cyber threats becoming increasingly
hance usability, making IAM solutions more intuitive and
sophisticated, leveraging identity-specific data has become
effective for organizations of all sizes.
essential for accurately detecting and mitigating risks.
ITDR focuses on the behaviors and activities tied to user
Redefining User Experience identities—such as login patterns, access permissions,
and authentication methods—to identify anomalies that
One of the most significant benefits of AI in identity man-
might indicate malicious activity or compromised accounts.
agement is enhancing user interactions. Traditional identity
Modern cybersecurity tools are starting to integrate ITDR
The State of Cybersecurity in Canada 2025 63

capabilities by incorporating ad- disparate systems, customize features,
vanced AI and machine learning, and train users, ensuring that deploy-
which can analyze vast amounts of ments achieve their intended out-
identity data in real-time. These tools comes. The ultimate goal is to make
can detect deviations like logins from identity tools as intuitive as consum-
unusual locations, sudden privilege er-grade applications, allowing users
escalations, or unauthorized access to focus on decision-making rather
attempts, enabling more precise and than the mechanics of the system.
timely responses. By blending identi-
ty-specific monitoring with traditional
The Path Forward
security frameworks, organizations
can strengthen their overall securi- As AI continues to evolve, the future
ty posture, ensuring a more holistic of identity security looks promising.
approach to threat detection and re- Generative AI has the potential to
sponse. This integration ensures that address some of the most pressing
identity-related risks are addressed challenges in IAM, IDTR and beyond.
as a core part of an organization’s By simplifying complex processes,
broader cybersecurity strategy. enhancing user experiences, and
delivering actionable insights, AI is re-
defining the role of identity in modern
organizations.
Organizations
To fully realize these benefits, organi-
must embrace
zations must embrace a collaborative
a collaborative approach, leveraging both cut-
ting-edge technology and expert guid-
approach, leveraging
ance. The evolution of identity in the
both cutting-edge age of AI is not just about automation;
it’s about empowering users, enhanc-
technology and
ing security, and driving innovation.
expert guidance.
Fahad Kabir is the CEO of IAMConcepts
Security Solutions Inc., a cybersecurity
professional services firm specializing in
Market Leaders and Professional digital identity and access management for
Services businesses. With over 20 years of experience
leading consulting organizations, he has a
Most product vendors are already
proven track record of delivering outstand-
integrating AI into their solutions,
ing results across various industries. Before
setting the stage for a competitive
joining IAMConcepts, Fahad held leadership
landscape in identity management.
roles at global consulting firms including EY,
However, deploying these advanced
Accenture, and Deloitte. He is recognized as a
tools requires more than just technical
visionary and thought leader in the cybersecu-
expertise and professional services
rity industry, having spoken at numerous glob-
will continue to play a crucial role in
al conferences on topics such as the future of
ensuring meaningful implementation.
Identity & Access Management, cyber threats
Even with AI-powered tools, organi- in the financial industry, and security program
zations will require guidance to tailor management.
these solutions to their specific needs.
Professional services help connect
The State of Cybersecurity in Canada 2025 64

The Canadian Threat Landscape
by Julien Richard
Digital technology powers every aspect of Canadian soci- adversaries are becoming more aggressive in cyberspace,
ety—from healthcare and critical infrastructure to small attempting to cause disruptive effects such as denying ser-
businesses and government services. As organizations vices, deleting or leaking data, and manipulating industrial
become more connected and dependent on technology, control systems. The CCCS states in the report that China,
they also become more vulnerable to an evolving array of Russia, and Iran remain primary concerns, while India has
cyber threats. These aren’t just technical challenges; they emerged as a new threat amid diplomatic tensions. These
represent real risks to essential services, economic stabil- state actors have shifted their tactics, often compromising
ity, and public safety. As cyber threats continue to evolve, domestic infrastructure like home and small office rout-
state-sponsored activities stand out as one of the most ers to mask their activities. This approach proved devas-
significant concerns facing Canadian organizations and tating when attackers breached Global Affairs Canada’s
institutions. VPN, maintaining access for over a month and potentially
exposing classified information. Even more concerning,
state-sponsored actors now very likely consider civilian crit-
State-Sponsored Threats
ical infrastructure as legitimate targets for cyber sabotage
State-sponsored cyber operations against Canada contin- in the event of military conflict. Along with state-sponsored
ue to intensify and evolve beyond traditional espionage. threats, ransomware has emerged as one of the most perva-
According to the Canadian Centre for Cyber Security’s sive and damaging forms of cyber attacks.
National Cyber Threat Assessment 2025-2026, state
The State of Cybersecurity in Canada 2025 65

Ransomware Trends Emerging technologies are also creating new points of
attack, fundamentally reshaping the nature of cybersecurity
Ransomware attacks remain a dominant cyber threat in
challenges in these sectors.
Canada. According to Mandiant, the median dwell time for
ransomware attacks dropped to just 5 days in 2023, under-
scoring attackers’ efficiency. Victims are frequently forced Emerging Threats
into ransom payments to regain access to data, although
Attackers now leverage AI to enhance phishing campaigns,
many organizations now prioritize incident response over
generate convincing deepfakes, and analyze stolen data
paying attackers. Despite this, ransomware tactics continue
with unprecedented efficiency. They create sophisticated
to evolve, with attackers increasingly targeting sensitive
fake news websites posing as local outlets while using
business operations rather than just data encryption. The
AI-powered analytics to identify and target victims with
impact of these and other cyber threats is amplified by the
precision. The rising value of cryptocurrency, with Bitcoin
dramatic increase in attack sophistication and speed.
up 133% in the past year to over 125,000.00 CAD, has co-
incided with increasingly expensive ransomware demands.
Evolution of Attack Sophistication According to Sophos’ State of Ransomware 2024 report, the
median ransom payment has increased five-fold from the
The sophistication and speed of cyberattacks have increased
previous year to $2,000,000 USD, while the mean payment
dramatically in recent years. According to Mandiant’s 2024
reached nearly $4,000,000 USD. Particularly concerning
analysis, the window between a vulnerability’s discovery
is that 63% of ransom demands are now for $1 million or
and exploitation has shrunk from 63 days in 2018 to just
more, with 30% demanding $5 million or more. The surge
5 days in 2023. Even more alarming is that 12% of vulnera-
in cryptocurrency values has not only increased the poten-
bilities are now exploited within 24 hours of discovery. The
tial payout for attackers but has also provided them with a
MOVEit attack campaign of 2023 demonstrated this rapid
larger pool of resources to fund sophisticated operations.
exploitation, affecting more than 2,700 organizations and
compromising over 93.3 million individual records glob-
ally. In Nova Scotia alone, 100,000 people were affected,
costing the province $3.8 million in response efforts. These $ 2 3
sophisticated attacks have particularly severe impacts on
.
critical sectors of Canadian society.
million
Sector-Specific Impacts
The healthcare sector has proven particularly vulnera- is the average recovery cost
ble to these evolving threats, especially ransomware and
on Canadian organizations,
state-sponsored activity. In 2023 alone, the sector faced
630 ransomware attacks globally. Healthcare data breach excluding ransom payments.
expenses have surged by 53.3% since 2020, with system
downtime alone costing medical organizations an estimat-
ed $15.5 million in 2023. The Toronto Hospital for Sick
Children ransomware attack demonstrated the sector’s
The impact on Canadian organizations is significant, with
vulnerability, disrupting patient care and lab results.
recovery costs averaging $2.73 million in 2024, excluding
Critical infrastructure faces an equally concerning threat ransom payments. This represents an increase of almost
from cyberattacks. Between January 2023 and January $1 million from the previous year. The cryptocurrency
2024, these vital systems experienced over 420 million at- connection is particularly relevant as ransoms are typically
tacks globally, averaging 13 attacks every second, as report- paid in cryptocurrency, making the rising values of digital
ed by Security Today. The utility sector has been especially currencies a direct multiplier of cyber risk.
targeted, with cyberattacks increasing by 70% compared
Quantum computing presents a looming threat to current
to 2023, according to U.S. News. This sharp rise is linked
cryptographic standards. Canada’s 2022 National Quantum
to growing digitization and reliance on outdated systems,
Strategy emphasizes the urgent need to prepare, with fed-
leaving critical components vulnerable to exploitation.
eral quantum readiness assessments suggesting that 2026
The Canadian Threat Landscape by Julien Richard The State of Cybersecurity in Canada 2025 66

could mark the earliest possible quantum threat to current without their challenges and have drawn criticism for their
encryption methods. potential implementation hurdles and broader implications.
Social media use also presents significant risks, both Bill C-26, the Act Respecting Cyber Security, represents
in terms of privacy and security. According to Statistics Canada’s first comprehensive attempt to protect critical
Canada, over 70% of Canadians aged 15 and older reported infrastructure through cybersecurity legislation. It creates
experiencing a cyber-related incident in 2022. Addressing new obligations for operators in telecommunications,
these evolving threats requires not only technological solu- finance, energy, and transportation sectors, requiring them
tions but also a skilled workforce capable of implementing to implement cybersecurity programs and report incidents
and maintaining robust cybersecurity measures. to the Canadian Centre for Cyber Security.
Bill C-63 addresses social media and online risks by enhanc-
ing protections against cyberbullying and online harms
70
%
while also implementing a framework for reporting and
investigating these incidents. These measures align with
the bill’s broader goal of ensuring a safer digital environ-
ment for Canadians. The financial implications of these
cyber threats extend across all sectors, resulting in signif-
icant economic impact for Canadian organizations and
governments.
of Canadians aged 15 and older
Economic Impact
reported experiencing a cyber-
Cybercrime continues to cost Canadian organizations
billions every year. The Canadian Centre for Cyber Security
related incident in 2022.
estimates that the economy lost $9.7 billion in 2023 due
to these threats. Industries like healthcare, manufacturing,
and finance often feel the biggest impact because they rely
so heavily on technology and can’t afford disruptions. For
Workforce and Skills Gap
example, the City of Hamilton faced $7.4 million in recov-
The cybersecurity challenges facing Canadian organiza- ery costs after a cyber attack, with another $30 million
tions are compounded by a significant workforce short- needed to strengthen its defenses.
age. According to the Information and Communications
The financial damage doesn’t stop at direct costs. Cyber
Technology Council’s Digital Talent Outlook for 2025,
incidents can lead to lost customers, downtime, and higher
Canada will need an additional 250,000 digitally skilled
insurance premiums, which all add up quickly. For indus-
workers by 2025, with the digital economy expected to
tries like healthcare and finance, a breach doesn’t just
employ 2.26 million workers—approximately 11% of all
disrupt operations—it can erode trust with patients and cli-
employment in the country. This shortage is particularly
ents, making recovery even harder. Add in the cost of legal
acute in cybersecurity roles, where specialized skills are
fees and regulatory fines, and it’s clear these threats have
essential for protecting critical systems and data. The
widespread implications for organizations and the economy
skills gap is especially challenging in sectors like advanced
as a whole.
manufacturing and healthcare, which are projected to need
14,000 additional workers each by 2025, while also facing
increasing cyber threats. Future Outlook
Cybercriminals are shifting their focus from merely en-
Canadian Legislation crypting data to targeting its integrity, manipulating critical
records such as financial ledgers, medical diagnoses, or op-
To address the growing complexities of cybersecurity,
erational parameters to coerce victims into paying ransoms
Canada has introduced key legislative measures aimed
to restore accuracy. This emerging tactic, as highlighted
at safeguarding critical infrastructure and protecting
by the IBM Security X-Force Threat Intelligence Index 2024,
Canadians online. However, these initiatives are not
undermines trust in organizational systems and creates
The Canadian Threat Landscape by Julien Richard The State of Cybersecurity in Canada 2025 67

complex challenges for detection and recovery, beyond
traditional ransomware attacks. The report also reveals an
alarming shift in attack methods, with deployment time for
ransomware attacks dropping from less than two days to
less than four hours, and notes that manufacturing has be-
come the most attacked industry for the third consecutive
year. To counter these threats, organizations must prioritize
data integrity monitoring and robust recovery processes to
ensure the authenticity of their information.
The path forward…Requires
integrating security into every
business decision, investing in
both technology and training ,
and preparing for threats that
have yet to emerge.
The rise of connected and autonomous vehicles (CAVs)
presents new cybersecurity challenges for Canada’s trans-
portation infrastructure. The integration of digital systems
in vehicles and networks creates vulnerabilities that mali-
cious actors can exploit. Transport Canada’s Vehicle Cyber
Security Guidance highlights the risks posed by intercon-
nected supply chains, while the Canadian Centre for Cyber
Security warns of potential threats throughout the digital
supply chain. Studies on LiDAR systems reveal how adver-
sarial attacks can disrupt autonomous navigation, affecting
not just vehicles but entire transportation networks. These
evolving threats demand robust cybersecurity measures to
protect Canada’s infrastructure.
As the Canadian Centre for Cyber Security notes, cyber-
security has evolved beyond a mere IT issue to become
a business survival imperative. The path forward for
Canadian organizations requires integrating security into
every business decision, investing in both technology and
training, and preparing for threats that have yet to emerge.
Success in this environment doesn’t require predicting
every threat but rather building systems and teams that
can adapt, recover, and learn from emerging challenges.
Understanding this reality is crucial, but it requires clear
action to protect organizations and their stakeholders from
persistent cyber risks.
Julien Richard is the Vice-President of Infosec at Lastwall. Julien also
operates BCK Security, a freelance consulting firm.
The Canadian Threat Landscape by Julien Richard The State of Cybersecurity in Canada 2025 68

The State of Third-Party
Cyber Risk Management
in Canada
Presented by BlueVoyant
Findings from a recent survey of Canadian C-level executives impacted by a cyber breach within their supply chain,
found a staggering 93% of Canadian organizations have been significantly more than the 81% of global respondents who
negatively impacted by a cyber breach within their supply said the same. On average, Canadian companies experi-
chain in the past twelve months, 10 percentage points greater enced 3.96 breaches in the prior 12 months, slightly higher
than global counterparts. than the global average of 3.68.
As enterprises become more interconnected and have more
suppliers and vendors, Canadian organizations are facing Vendor and Supplier Monitoring Practices
heightened challenges in managing supply chain cybersecu-
Canadian organizations have large vendor networks
rity. BlueVoyant’s recent The State of Supply Chain Defence
with the most common number of vendors being some-
report revealed 93% of Canadian organizations have been
where from 1,001 to 10,000 vendors (35%). Yet, most
The State of Cybersecurity in Canada 2025 70

organizations say they only evaluate 501 to 1,000 of them a major step in the right direction. Since Canadian organi-
for cyber risks (39%). Thirty-six percent of respondents zations say they are increasing budgets, we will hopefully
who know how many suppliers they work with say they see them implement more best practices to better monitor
regularly monitor between 1,001 and 10,000 vendors. their digital supply chains, and work with third parties to
quickly mitigate any issues.”
Working with third-party vendors remains a critical area of
concern, with only 36% of Canadian organizations say-
ing they engage with such partners, aligning with global The importance of analyst-
figures. Alarmingly, 31% of these companies say they have
no way to detect issues with third-party vendors, a slight driven decision making
increase over the global average of 30%.
and having a “human
Continuous monitoring is most reported solution for
third-party cyber risk management, adopted by 32% of
Canadian firms. However, many companies say they are in the loop,” cannot be
only monitoring vendors quarterly (31%).
understated.
Canadian organizations are less likely to have continuous
autonomous transparency (11% compared to 15% glob-
ally), indicating room for improvement in real-time risk
assessment. To help improve Canadian third-party cyber risk manage-
ment, organizations should consider increasing automation.
As with many other business functions, supply chain cyber
Budget Increases Reflect Growing Concerns
risk management will continue to see increased reliance
The silver lining is that things may begin to change with on automation and AI as a way of making effective risk
budgets increasing. More than nine-in-ten (92%) of management more accessible and scalable, especially for
Canadian organizations say they have increased their smaller- and medium-sized organizations that struggle with
cybersecurity budgets, compared to 86% globally. This personnel and resource limitations.
increase in funding reflects a growing recognition of the
At the same time, it has become evident that complete
need for robust defences against third-party cyber threats.
automation is not a viable solution. The importance of
Canadian firms are likely to channel these enhanced bud-
analyst-driven decision making and having a “human in the
gets into both internal (51%) and external (59%) third-par-
loop,” cannot be understated, especially for aspects of solu-
ty cybersecurity resources, showing demand for both
tions like following up with third parties to ensure effective
employees skilled in supply chain risk, and vendors to help
remediation.
monitor and respond to supply chain cyber threats.
As information security as an industry continues to mature,
Improving Canadian Third-Party Cyber Risk Management
there will be more focus put on the integration of various
The study findings suggest that while Canadian organiza- aspects of security operations. This means that third-party
tions are making strides in supply chain cybersecurity, there cyber risk will inevitably be folded into day-to-day SOC
is still a critical need for enhanced third-party risk manage- operations and wider risk management programs.
ment (TPRM) practices. Increased automation and inte-
As Canadian companies continue to navigate the complex-
gration of third-party cyber risk management into broader
ities of supply chain cybersecurity, the focus must remain
security and risk operations could provide more scalable
on proactive identification and working with vendors to
and effective solutions.
mitigate vulnerabilities quickly.
“More organizations than any previous year indicated
The research was conducted by Opinion Matters, with a sample of
that their primary focus is no longer on awareness of the
74 CTOs/CSOs/COOs/CIOs/CISOs/CPOs responsible for supply chain
third-party risk management problem or adoption of a pro-
& cyber risk management working in companies employing 1,000+
gram, but rather with the operational, day-to-day challeng-
employees in Canada. The data was collected between 20.08.24 -
es of managing an effective program,” said Joel Molinoff,
29.08.24 Opinion Matters abides by and employs members of the Market
global head of Supply Chain Defence at BlueVoyant. “While
Research Society and follows the MRS code of conduct and ESOMAR
this progress also brings many new challenges, it indicates
principles. Opinion Matters is also a member of the British Polling Council.
The State of Cybersecurity in Canada 2025 71

Cybersecurity for Canadian
Digital Infrastructure
by Albert Heine
Introduction
Furthermore, we are going to look at Canada’s Information,
In this article we are going to focus on the cybersecurity of
Communications and Technology (ICT) sector and take into
digital infrastructure that powers Canadian businesses and
account unique properties and their effect on the adoption of
government institutions. The goal is to understand where
technology and choice of digital infrastructure.
technology trends are heading towards, the associated
risks, and how it relates to other, more broad cyber-risks. After the outline on the focus-areas of digital infrastruc-
Based on that, a focused set of mitigation strategies related ture, we are going to describe the most common risks and
to infrastructure is proposed that should help future-proof misconceptions. For each risk, we are going to discuss the
the majority of Canadian businesses. most established mitigation strategies. This provides a clear
picture of what could and should be prioritized today in
Since the term “digital infrastructure” is broad and can mean
your organization.
a variety of different combinations of technologies, we are
going to highlight in the first section what the trends are We are going to finish this article with a subsection on
when setting up infrastructure to power modern applications. future trends and how to be prepared for them.
The State of Cybersecurity in Canada 2025 72

Digital infrastructure in Canada Risks and mitigation strategies
Similar to trends observed on a global scale, Canada’s Using the cloud comes most of the time with a general
cloud adoption has reached 48.5% in 2023,1 and is steadily misconception: The cloud provider will take care of the
growing across all enterprises. When focussing on the ICT security needs. That belief is very prevalent in Canada, with
sector, 95.5% of all companies in this sector are under the 31% of Canadian executives holding on to it.5 The truth is
category of “Software and Computer services”, and most that there is a shared responsibility model when it comes to
of ICT companies (84.9%) have less than 10 employees.2 utilizing the cloud (see e.g. the respective articles by AWS,
Hence, one can assume that the cloud adoption among ICT Azure and GCP).
companies in general is likely much higher than the overall
Hence, it is important for any team using cloud technol-
number across all enterprises.
ogy to understand the risks for any utilized service. And
In addition to the private enterprise sector, Canada is itself that awareness only covers the layer of the cloud itself.
committed to moving their infrastructure steadily to the Container orchestration, container security measures and
cloud since 2018.3 third party application security have to be considered as
well. For the longest time, cloud security posture manage-
For these reasons, cloud-related risks should be considered
ment was the sole focus, but the latter mentioned appli-
a major focus when considering cybersecurity of Canadian
cation configuration security is now also starting to come
digital infrastructure.
into the spotlight with the latest revision of the FedRamp
In addition to that, one needs to also study which technolo- security framework,6 where DoD Stigs and other bench-
gies are employed in the cloud, to further refine the overall marks require a monthly report. FedRamp is usually the first
image of infrastructure related tools. While there is no coun- framework that adopts new control criteria historically, and
try-specific study available there, the yearly Stack-overflow others tend to follow.
Developer survey sheds light on technology trends that
One of the reasons for this shift can also be directly correlat-
indicate which technologies are being used by developers.
ed to the cybersecurity situation in Canada. According to
Without surprise, Docker appears to be the No. 1 technology
the “Baseline cyber threat assessment: Cybercrime” report
with over 59% of Developers using it. It has transformed the
by the Canadian Center for Cybersecurity,7 “ransomware
way we are building and deploying code on any infrastruc-
[is] almost certainly the most disruptive form of cybercrime
ture, and draws the bridge between development and IT.
that Canadians face and has significant impacts beyond the
Further infrastructure related tools are Kubernetes (19.4%),
financial cost of the ransom itself.” According to a study by
Terraform (10.6%) and Ansible (7.9%).4 This leads to the
Microsoft,8 80% of ransomware attacks can be traced to
conclusion that containers are the major build and deploy-
misconfigurations in devices and operating systems. Hence,
ment vehicle on infrastructure today, including the cloud,
infrastructure security should be seen as the highest priority
and are growing in the future. The high use of containers
when trying to prevent ransomware attacks.
compared to the common container orchestration tools
leads to the conclusion that the processes, even when con- In addition to handling misconfigurations, on premise, or
tainers are involved, remain manual for the majority. on the cloud, or inside containers: Canadian organizations
will need to be able to update in case of a common vulner-
ability and exposure (CVE), and they need to be able to
Which technologies are being used by developers
update fast. This ability is crucial to avoid keeping doors
Source: Stack Overflow 2024 Developer Survey
open for potential attackers. The best known mitigations
59%
against that are known as the DevSecOps process and the
Docker use of infrastructure-as-code as much as possible. In this
way, your teams can update fast and with confidence, since
change management is automated and tested properly. At
the same time, misconfigurations and code quality can also
19.4%
be re-assessed with every change and deployment.
Kubernetes
10.6% May it be called DevSecOps or any other newly emerging
7.9%
Terraform term, at its core is one underlying principle: Automation.
Ansible
3.1%
The more infrastructure processes can be automated, and
Other
the more these automations follow commonly established
Cybersecurity for Canadian Digital Infrastructure by Albert Heinle The State of Cybersecurity in Canada 2025 73

even before the time of LLMs, when most AI-related efforts
standards, the more flaws, vulnerabilities and misconfig-
were targeted at machine learning, remains true:
urations can be caught in an organization, and the more
straightforward will be any auditing process for compli- In the DevSecOps process, one part should be to clearly de-
ance purposes. fine a Role Based Access Control (RBAC) architecture, and
Red Hat is even going one step further by calling auto-
mation now “mission-critical”, and correlates automation There is no AI (artificial intelligence)
efforts, besides the security benefits, with ROI in terms of
productivity, efficiency and downtime-reduction.9 without IA (information architecture).
Given that, as previously mentioned, most ICT companies in — Unknown
Canada are under 10 employees, the process change towards
automation on a large scale is more than feasible. This puts
this architecture should also control the data access and
Canada in a unique position by being able to be at the fore-
manipulation flow. If LLM models need to be trained on
front of innovation of business and technology processes.
company data, it is obvious that one needs to ensure that
Classic controls like proper network segmentation and only information that a user actually should have access to
well-defined entry points such as load-balancers also mit- is accessible to the user through the LLM. I.e., the training
igate the risk of attackers reaching sensitive data. While path needs to be clearly defined and isolated. The proper
many still view it as the cloud provider’s responsibility, it is architecture of such multi-models is in its infancy, but at its
not. A proper design and implementation of a network ar- core, independent of the implementation, there will always
chitecture lies with the development team, and also needs be the need to define access rights and an auditable process
to be reviewed and checked regularly. regarding where, when, and how user-data gets stored and
distributed. Especially in Canada and the European Union,
where the Personal Information Protection and Electronic
Documents Act (PIPEDA) and the General Data Protection
Cloud and Container
regulation (GDPR) are in place respectively, this is some-
Adoption
thing to get right today to be ready for the future.
The aforementioned trends in terms of Infrastructure
are providing the necessary functionality to aid this ef-
Infrastructure as Code
fort: Containers and their orchestration tools, such as
(IaC)
Kubernetes, come with a built-in RBAC functionality, and
the major cloud providers are allowing for fine-grained
access controls on their platforms. Furthermore, a new
Automation to Increase functionality across all major Cloud and IaC providers
called Policy as Code (PoC) is emerging, further assisting
Speed and Security
developers to enforce policies at all stages of the build and
deployment process.
Hence, at the core is automation. Nothing is better docu-
New technologies and future outlook mentation about data-flow and access controls than coded
automation processes. The more standardized these pro-
This is likely the first technology article you read since
cesses are, the more an organization can rely on automated
2023 that took more than two pages to mention the words
tools to catch misconfigurations or other problems and
Artificial Intelligence (AI). But here we are.
significantly reduce their risk of being hacked.
According to the largest survey in the developer industry,
76% of developers are planning to use AI in their develop-
Dr. Albert Heinle is driven by a mission to combat the global surge of
ment process4. Many other departments such as marketing
data breaches and misconfigurations. Albert co-founded CoGuard in
and customer success experienced a spike in AI tool use
2020 and serves as Chief Technology Officer. Prior to CoGuard, Albert
since 2023 as well.
held development positions at FLIR Systems, Inc., Aeryon Labs and
But with this new technology, demands for data privacy Sortable. He completed a Ph.D. in Computer Science at the University of
and IP protection are also coming forward. A principle from Waterloo in the area of Symbolic Computation.
Cybersecurity for Canadian Digital Infrastructure by Albert Heinle The State of Cybersecurity in Canada 2025 74

The State of Software Supply Chain Security
in Canada
by Dmitry Raidman
Introduction widely used components can expose organizations to global
risks, leading to significant disruptions in Canadian federal
Software supply chains have become critical targets for
agencies and private-sector firms.
cyber adversaries globally, and Canada is no exception.
These complex ecosystems, consisting of software de- KEY THREATS IDENTIFIED BY CCCS:
velopers, vendors, third-party suppliers, and end-users,
• Compromised Updates: Threat actors insert malicious code
are vulnerable to sophisticated attacks. The Canadian
during software updates, as seen in the SolarWinds breach.
Centre for Cyber Security (CCCS), through its publication
ITSM.10.071, highlights the risks and the steps organiza- • Open-Source Dependencies: Widely used libraries often
tions can take to mitigate these threats. Legislative frame- contain hidden vulnerabilities exploited by adversaries to
works like Bill C-26 further underscore Canada’s focus on gain persistent access.
bolstering its cyber defenses by addressing supply chain
• Vendor Privileges: Elevated access granted to ven-
risks. By comparing Canada’s efforts to initiatives in the
dors increases risks, particularly in cloud and SaaS
United States and the European Union (EU), this report
environments.
provides a comprehensive overview of the current state of
software supply chain security.
Global Perspectives: U.S. and EU
The Software Supply Chain Threat Landscape In the United States, Executive Order 14028 mandates the
adoption of a Software Bill of Materials (SBOM) to improve
CANADA: GROWING RISKS AND CHALLENGES
transparency and address software supply chain vulnerabil-
In Canada, cyber threat actors increasingly target software ities. Published by NIST, the Secure Software Development
supply chains, exploiting vulnerabilities in open-source Framework (SSDF) provides actionable guidance for secure
libraries, third-party dependencies, and trusted vendor software development and aligns closely with CCCS recom-
relationships. As ITSM.10.071 outlines, these attacks com- mendations. Notably, SBOMs are mandated for all software
promise systems by leveraging the trust between software sold to U.S. federal agencies for companies that develop
providers and consumers. Examples such as the Log4j products that require FDA approval and showcase a com-
vulnerability or xz supply chain attack demonstrate how mitment to proactive security.
The State of Cybersecurity in Canada 2025 75

The European Union adopts a regulatory-driven approach COMMON TYPES OF SBOMS:
through the Cyber Resilience Act, which imposes stringent
BOM Type Definition Purpose
requirements on software vendors to ensure product secu-
rity throughout its lifecycle. The EU’s emphasis on contin-
uous monitoring and transparency mirrors Canadian and Provides an inventory of all
Software Bill of software components in a product,
U.S. priorities, indicating a global alignment in combating SBOM enabling vulnerability detection and
Materials
supply chain risks. transparency.
Canada’s Approach to Mitigating Risks
LEGISLATIVE AND POLICY FRAMEWORKS: BILL C-26 Software Bill Identifies AI models, datasets,
and dependencies in AI-driven
AIBOM of Materials
applications to ensure responsible
Bill C-26, passed on Dec 5, 2024, represents a significant for AI and secure AI use.
step forward in Canada’s efforts to address cybersecurity
challenges. It mandates critical service operators to im-
plement comprehensive cybersecurity programs, mitigate Lists cryptographic algorithms,
Software Bill of keys, and certificates in software to
third-party risks, and report incidents. By requiring organi-
ensure encryption standards and
CBOM Materials for
zations to identify vulnerabilities in their supply chains and compliance. CBOM is also vital for
enforce rigorous monitoring, the legislation strengthens Cryptography Post-Quantum Cryptography (PQC)
and quantum resiliency.
Canada’s overall security posture.
Key provisions related to supply chain security include:
Details physical hardware
• Critical Cyber Systems Protection Act: Operators of vital HBOM Hardware Bill components to ensure a secure
of Materials supply chain and device integrity by
systems must mitigate supply chain risks, establish cyber-
detecting counterfeit components.
security programs, and comply with government directives.
• Telecommunications Security Enhancements: Directives to
secure telecommunications infrastructure include mandates
The adoption of SBOMs, while still emerging in Canada,
to mitigate third-party risks and adopt security standards.
mostly happens in the telecom and financial sectors. It
reflects a growing understanding of its role in supply chain
Adoption of SBOM for Visibility and Transparency resilience. Lessons from the U.S. and EU, where SBOMs are
integral to cybersecurity strategies, further validate their
The government regulation highlights the Software Bill of
importance and add them as pivotal building blocks in the
Materials (SBOM) as an essential tool for achieving supply
companies’ cybersecurity roadmaps.
chain transparency. An SBOM provides an inventory of
software components, enabling organizations to:
Challenges in Implementing Software Supply
1. Identify Vulnerabilities: By mapping dependencies, organi-
Chain Security
zations can quickly detect components affected by newly
discovered vulnerabilities, reducing the MTTD and MTTR. Despite progress, Canadian organizations face hurdles in
adopting robust supply chain security practices. Smaller
2. Enhance Collaboration: Sharing SBOMs between ven-
organizations often lack the technical expertise or resources
dors and clients facilitates better risk assessment and
to implement standards and tools such as SBOMs and VEX.
remediation.
The dynamic nature of software ecosystems, characterized
3. Enhance Asset Risk Management: Linking between SBOM by DevOps culture, continuous updates, and rapid develop-
data and assets management solutions by the end users ment cycles, demands ongoing monitoring that many orga-
will provide end-to-end operationalization of SBOMs. nizations find challenging to maintain. Additionally, the ab-
sence of universal standards for SBOM formats complicates
4. Streamline Compliance: Aligning with regulatory frame-
integration across diverse environments. Addressing these
works like Bill C-26, FDA, and U.S. federal mandates like
challenges requires collaboration between government
EO 14028 ensures compliance and strengthens overall
agencies, private-sector stakeholders, and international
security.
partners to develop scalable and interoperable solutions.
The State of Software Supply Chain Security in Canada by Dmitry Raidman The State of Cybersecurity in Canada 2025 76

Recommendations for a Resilient Future 2. Conduct Supply Chain Audits: Regularly assess the security
posture of third-party vendors and enforce contractual ob-
RECOMMENDATIONS FOR POLICYMAKERS
ligations for cybersecurity compliance and SBOM sharing.
1. Mandate SBOM Adoption: Require the use of SBOMs
3. Invest in Automation: Use automated tools to continu-
across critical infrastructure sectors to enhance software
ously monitor software dependencies and detect vulnera-
transparency and ensure compliance with evolving cyber-
bilities across the supply chain.
security regulations.
4. Implement Zero Trust Principles: Apply a zero-trust archi-
2. Develop Incentives: Provide financial or technical incen-
tecture to minimize the risk of lateral movement within
tives, such as grants or tax credits, to encourage small
your network in case of a breach.
and medium-sized enterprises (SMEs) to adopt supply
chain security measures. 5. Collaborate with Policymakers: Engage with government
initiatives and frameworks to shape policies that address
3. Foster Global Collaboration: Align Canadian policies
enterprise-specific challenges in supply chain security.
with international frameworks like the NIST SSDF and
EU Cyber Resilience Act to ensure interoperability and
Emphasizing Education and Awareness
cross-border consistency.
To mitigate risks, organizations must prioritize:
4. Strengthen Public-Private Partnerships: Create intelli-
gence-sharing mechanisms between government entities • Training: Educating teams on secure software develop-
and private organizations to improve real-time threat ment and supply chain risk management.
detection and mitigation.
• Awareness Campaigns: Highlighting the risks of third-
5. Invest in Research and Development: Fund initiatives to party dependencies and promoting a culture of vigilance
improve supply chain security technologies and meth- across the technical R&D and operations teams.
odologies, ensuring Canada remains at the forefront of
innovation. Conclusion
RECOMMENDATIONS FOR SMALL AND MEDIUM Canada’s evolving approach to software supply chain secu-
BUSINESSES (SMES) rity, exemplified by Bill C-26 and CCCS guidance, positions
the country along with the US and EU in addressing global
1. Start with SBOM Basics: Utilize open-source or com-
cybersecurity challenges. However, continued focus on
mercial tools to generate, ingest, and manage SBOMs,
transparency, collaboration, and regulatory alignment is es-
ensuring visibility into the software components used in
sential to mitigate the growing risks of supply chain attacks.
your environment.
By adopting tools like SBOM management platforms,
2. Leverage Managed Security Services: Partner with
learning from global frameworks, and addressing imple-
managed security service providers (MSSPs) to monitor
mentation barriers, Canadian organizations can strengthen
supply chain risks if in-house expertise is limited.
their defenses against increasingly sophisticated adversar-
3. Educate Teams: Train staff on basic cybersecurity hy- ies. As the software supply chain becomes a critical pillar
giene, focusing on the risks of third-party dependencies of national security, proactive measures today will ensure
and the importance of maintaining updated systems. resilience and the ability to respond and mitigate such
threats for years to come.
4. Establish Incident Response Plans: Develop plans to
address potential supply chain breaches, including clear For more information, refer to CCCS resources such as
guidelines for engaging with vendors and customers. ITSM.10.071, Common Criteria, and global standards like
NIST SP 800-218.
5. Adopt Scalable Solutions: Implement lightweight, open-
source security tools that fit within the budget and
resource constraints of SMEs. Dmitry Raidman is a Canadian-Israeli entrepreneur and cybersecurity
expert with over 20 years of experience in application security, cloud ar-
RECOMMENDATIONS FOR ENTERPRISES
chitecture, DevOps, and cyber-defense automation. As co-founder and
1. Integrate SBOMs into Asset Management: Ensure all SBOMs CTO of Cybeats, he has spearheaded innovations like the SBOM Studio
are linked to enterprise-wide asset management systems for and SBOM Consumer platforms that many Fortune 500 companies use
seamless tracking and vulnerability remediation. to enhance their software supply chain management.
The State of Software Supply Chain Security in Canada by Dmitry Raidman The State of Cybersecurity in Canada 2025 77

State of Cybersecurity
in Canadian Retail
by Isaac Wanzama
The Canadian retail sector stands at the crossroads of digital Guardlii captures diverse viewpoints across organizational
innovation and heightened cybersecurity risks. Employing levels, offering a nuanced understanding of cybersecurity
over 2 million people and contributing approximately 5% priorities and challenges in the retail industry.
to the national GDP, the industry is critical to the economic
fabric of the country. However, as retailers embrace ad-
Table of Contents
vanced technologies like e-commerce platforms, AI-driven
personalization, and contactless payments, they also expose 1. Introduction
themselves to increasingly sophisticated cyber threats. 2. The Canadian Retail Landscape
In this report, Guardlii examines the state of cybersecurity 3. Cybersecurity in Retail – Why It Matters
in Canada’s retail sector. Drawing insights from industry 4. The Rising Cybersecurity Threats
sources and our own ongoing survey of retail professionals, 5. Key Challenges in Canadian Retail Cybersecurity
including executives, IT managers, cybersecurity specialists,
6. Third-Party Vulnerabilities in Retail
and retail staff, we explore the financial, operational, and
7. Navigating Regulatory Compliance
reputational impacts of cyber threats.
8. Data Breaches and Their Cost
Additionally, we identify emerging trends and present 9. Strategic Solutions for Retail Cybersecurity
actionable strategies for senior executives to address these
10. Final Thoughts
challenges. By leveraging findings from this ongoing survey,
The State of Cybersecurity in Canada 2025 78

The Canadian Retail Landscape Data Breach Report investing in robust cybersecurity mea-
sures is a strategic imperative.
Canada’s retail sector is a diverse and dynamic contributor
to the national economy. From global giants like Walmart
Canada and Loblaw Companies Limited to innovative The Rising Cybersecurity Threats
e-commerce platforms such as Shopify, the industry is a
The retail sector remains one of the most targeted in-
blend of tradition and innovation. Regional differences
dustries globally, with an estimated 10% of cyberattacks
play a significant role in shaping the retail landscape. For
directed at retailers. Guardlii’s survey confirms this trend,
example, urban centers like Toronto and Vancouver are
with 51% of respondents frequently encountering customer
hubs for high-tech retail experiences, while rural areas rely
concerns about cybersecurity. Canadian businesses are no
on localized supply chains and smaller retailers.
exception. Recent years have seen a rise in ransomware,
phishing scams, and supply chain attacks, posing unprece-
dented challenges. Notably, the 2022 Sobeys ransomware
attack disrupted operations nationwide, resulting in signifi-
$70B
cant financial and reputational losses.
The shift to digital tools and processes in retail has creat-
ed new opportunities for cybercriminals to exploit. Our
survey found that 61% of respondents regularly check their
systems for weaknesses, showing they are actively working
to prevent risks. However, 16% of respondents admitted to
never performing these critical checks, putting them at risk.
is the approximate contribution
The shift to e-commerce, coupled with increasing reliance
the retail sector made to on third-party vendors, introduces additional vulnerabili-
ties. Guardlii’s data highlights that enhancing third-party
Canada’s GDP in 2023.
oversight is a top priority for many retailers, especially in
maintaining compliance with frameworks like PCI DSS.
As retailers adopt advanced technologies like AI-based
systems that identify threats and strategies that limit access
The industry also supports over 2 million jobs, ranging to trusted users, their cybersecurity strategies must evolve
from in-store personnel to logistics and IT professionals. to stay ahead of these threats. Guardlii’s survey revealed
Retail contributed approximately $70 billion to Canada’s that organizations investing in these innovations report
GDP in 2023, underscoring its significance, according to the significant improvements, such increases in threat detection
GDP by Industry Report 2023 by Statistics Canada reports. rates. However, 48% of respondents lacking cyber insur-
This scale and complexity make the industry a prime target ance underscores the critical need for financial risk mitiga-
for cybercriminals, who exploit vulnerabilities at every level tion alongside technological advancements.
of the supply chain.
Key Challenges in Canadian Retail Cybersecurity
Cybersecurity in Retail – Why It Matters
The Canadian retail industry faces a unique and evolving
The retail sector handles vast amounts of sensitive data, set of cybersecurity challenges, shaped by the interplay of
including payment information, personal customer details, physical stores, e-commerce platforms, and third-party ven-
and supply chain logistics. A breach in this data can lead to dors. Insights from Guardlii’s survey highlight critical areas
significant financial losses and harm customers’ confidence. that demand immediate and strategic action to mitigate
For C-level executives, the stakes are clear: cybersecurity is risks and safeguard operations.
not just an IT issue; it’s a critical business enabler.
UNDERFUNDED IT DEPARTMENTS
Retailers face unique challenges due to the high volume
For many retailers, particularly small to medium-sized
of transactions and the integration of third-party systems.
businesses, thin profit margins constrain investment in
With the average cost of a data breach in Canada reaching
cybersecurity. The survey revealed that 24% of respon-
$7.05 million in 2022 by IBM Security, The 2022 Cost of a
dents allocate less than 10% of their IT budgets to security,
State of Cybersecurity in Canadian Retail by Isaac Wanzama The State of Cybersecurity in Canada 2025 79

limiting their ability to implement THIRD-PARTY RISKS
advanced tools and training pro-
The retail industry’s reliance on
grams. This lack of resources leaves
third-party vendors, from payment
many organizations vulnerable to
processors to logistics providers, intro-
increasingly sophisticated attacks and
duces vulnerabilities that can com-
prevents them from addressing core
promise entire systems. While 50%
weaknesses effectively.
of respondents rely on vendor risk
LEGACY SYSTEMS assessments, many fall short in imple-
menting continuous monitoring and
Outdated infrastructure continues
contractual safeguards. Weaknesses in
to pose significant challenges for
vendor security can lead to breaches
Canadian retailers. According to the
that disrupt operations and damage
survey, 20% of respondents struggle
customer trust.
to integrate modern cybersecurity
solutions with legacy systems. POS
systems, which are critical for transac- Third-Party Vulnerabilities in Retail
tions, are especially at risk. Older POS
Third-party vendors are integral to
systems often lack the encryption and
the retail supply chain, supporting op-
security capabilities needed to defend
erations from payment processing to
against emerging threats like malware
logistics. However, these partnerships
and API exploitation. These vulner-
also introduce critical vulnerabilities.
abilities make them a primary target
Insights from Guardlii’s survey reveal
for attackers.
that while 50% of respondents assess
REGULATORY COMPLEXITY vendor cybersecurity through risk
assessments, only 25% rely on compli-
Canada’s fragmented regulatory land-
ance certifications, and 25% imple-
scape adds another layer of difficulty
ment continuous monitoring. This
for retailers. Navigating the differing
highlights gaps in vendor oversight
requirements of provincial and federal
that could leave retailers exposed to
laws, such as PIPEDA, while ensuring
cyber threats.
compliance with standards like PCI
DSS, demands dedicated resources A weak link in a vendor’s security can
and expertise. For smaller retailers, expose sensitive customer data or dis-
the challenge of keeping up with rupt operations. For instance, phish-
these requirements can divert focus ing scams targeting vendor systems
from broader security initiatives. or ransomware attacks on logistics
providers have previously halted de-
INSIDER THREATS
liveries and damaged customer trust.
Employee actions—whether malicious Guardlii’s data emphasizes the need
or inadvertent—pose a significant risk for proactive third-party risk manage-
to retailers, especially in an industry ment, especially as retailers increas-
characterized by high turnover. The ingly rely on external providers for
survey revealed that 31% of organiza- e-commerce and payment solutions.
tions do not provide employee cyber-
To mitigate these risks, continuous
security training, leaving businesses
monitoring systems are critical for
exposed to insider threats and social
identifying vulnerabilities in real-time.
engineering attacks. Building a cul-
Additionally, clear cybersecurity stan-
ture of security awareness is essential
dards in contracts, backed by regular
to mitigating these risks and ensuring
audits, ensure vendors adhere to the
that employees serve as the first line
retailer’s security expectations. The
of defense.
State of Cybersecurity in Canadian Retail by Isaac Wanzama The State of Cybersecurity in Canada 2025 80

survey further highlighted the importance of adopting Zero- access controls. Interestingly, 31% of survey participants
Trust principles, which help secure interactions between re- indicated that a lack of employee training on security pro-
tailers and their vendors by enforcing strict access controls. tocols undermines these efforts, underscoring the need for
integrated solutions.
Navigating Regulatory Compliance Cyber insurance also plays a pivotal role, providing fi-
nancial protection against the fallout from cyberattacks.
Compliance with regulations such as PIPEDA and GDPR is
However, the survey found that 48% of respondents lack
not just a legal requirement but a critical aspect of building
cyber insurance, exposing their organizations to significant
trust with customers. These frameworks set standards for
financial risks. Retailers that incorporate insurance along-
data protection and breach notification, ensuring account-
side robust prevention measures position themselves for
ability. For Canadian retailers, achieving SOC 2 compliance
greater resilience.
is particularly valuable, signaling a commitment to data
security and often serving as a differentiator in competitive
markets.
To navigate these regulations effectively, businesses should
Retailers that
invest in training, leverage automation tools for compliance
monitoring, and conduct regular audits. Compliance also
builds consumer confidence. incorporate insurance
Data Breaches and Their Cost alongside robust
The cost of data breaches extends far beyond the immedi-
prevention measures
ate financial losses. Direct costs include fines, legal fees,
and operational disruptions, while indirect costs encom-
pass customer churn and reputational damage. The Sobeys position themselves
ransomware attack of 2022 serves as a cautionary tale,
illustrating how a single incident can ripple across the orga-
for greater resilience.
nization, halting operations and eroding trust. Investing in
breach prevention and rapid response capabilities is critical
to minimizing these impacts.
Strategic Solutions for Retail Cybersecurity Employee training emerged as a recurring theme in the
survey, with 55% of organizations conducting monthly
Effective cybersecurity strategies demand a multi-faceted
training sessions. This reflects a growing recognition of the
approach that integrates advanced technologies, robust
role employees play in mitigating insider risks and reducing
policies, and proactive training. Insights from Guardlii’s
human errors. On the flip side, 31% of respondents admit-
survey of retail professionals reveal critical areas where
ted to never training employees, highlighting a critical gap.
these strategies can make the most impact.
Improving how companies monitor their external partners,
A key approach is using advanced AI systems that analyze
like vendors, is another critical area highlighted in the
data to quickly detect and stop cyberattacks in real-time.
survey. With many retailers relying on external vendors for
Retailers adopting AI enhanced tools have reported im-
supply chain and payment solutions, implementing con-
provements in detection rates, significantly reducing
tractual safeguards and deploying tools to monitor vendor
response times and minimizing potential damage. Survey
compliance has become essential. Respondents flagged
respondents in IT management roles emphasized the im-
third-party vulnerabilities as a top concern, especially in
portance of such tools in securing digital ecosystems.
maintaining PCI DSS compliance.
Another important tactic is using strict security systems
Finally, the survey emphasized the strategic importance of
that verify each user’s identity before granting access to
compliance. Many respondents noted that compliance is
any resource; “never trust, always verify.” This approach
increasingly being viewed not just as a regulatory obliga-
secures networks by strictly enforcing authentication and
tion but as a competitive advantage. Retailers that invest
State of Cybersecurity in Canadian Retail by Isaac Wanzama The State of Cybersecurity in Canada 2025 81

in meeting and exceeding compliance adequate training. Implementing
standards can strengthen custom- awareness programs can mitigate
er trust and bolster their market insider risks and reduce the likeli-
reputation. hood of human error. Investments in
modern technology are also essential
for addressing vulnerabilities in legacy
Future Trends to Watch
systems and adapting to evolving
Emerging technologies are reshap- threats. Strengthening third-party
ing the cybersecurity landscape. oversight through contractual safe-
Blockchain works like a digital ledger, guards and continuous monitoring
keeping transactions clear and secure, further protects supply chains.
much like a bank statement, while
Retailers that exceed baseline require-
quantum computing threatens to
ments can gain a competitive edge
render traditional encryption obso-
in today’s privacy-conscious mar-
lete Deloitte’s Cybersecurity Insights.
ket. Additionally, collaboration with
Retailers must also prepare for
industry consortia, like CCN, cyberse-
adaptive compliance, as regulatory
curity firms, and government bodies
frameworks evolve to address new
provides access to advanced threat
challenges.
intelligence and innovative solutions,
Additionally, robotics is transforming further enhancing resilience.
the way stores operate. Innovations
Cybersecurity must be central to every
like automated checkouts and in-
retail leader’s strategy. By investing in
ventory management tools enhance
people, technology, and partnerships,
efficiency but introduce unique cyber-
Canadian retailers can protect their
security risks, emphasizing the need
customers, secure operations, and en-
for robust security protocols.
sure long-term competitiveness in an
Staying ahead of these trends will increasingly digital marketplace.
require continuous investment in
research and development.
Isaac Wanzama is the Founder of Guardlii
Cyber Security Services, a firm specializing in
Call to Action: Prioritizing safeguarding organizations against the rapidly
Cybersecurity in the Canadian evolving digital threats. With a proven track
Retail Landscape record as an accomplished entrepreneur Isaac
is dedicated to empowering businesses, par-
The Canadian retail industry faces
ticularly within the retail sector—to strengthen
unique challenges that demand stra-
their resilience against challenges such as
tegic attention. High-profile incidents
ransomware, phishing attacks, and third-party
highlight the operational and repu-
vulnerabilities.
tational risks of inadequate defenses.
Dependence on third-party vendors
and fragmented federal and provincial
regulations further complicate secu-
rity efforts, requiring businesses to
adopt tailored approaches to mitigate
risks effectively.
Retail leaders must focus on building
a strong security culture to pro-
tect their business and customers.
Employees are often the first line of
defense against cyber threats, yet
many organizations lag in providing
State of Cybersecurity in Canadian Retail by Isaac Wanzama The State of Cybersecurity in Canada 2025 82

Safeguarding Canada’s Power:
Cybersecurity Landscape in Energy
and Utilities
by Denrich Sanada and Sonia Khan
Executive Summary also addresses regulatory responses, organizational blind
spots, and recommendations for resilience in a rapidly
The Canadian energy and utility sector is a critical pillar
evolving threat landscape.
of the nation’s economy and infrastructure, yet it faces
growing cybersecurity threats driven by both financially
motivated and state-sponsored actors. As reliance on digital Introduction
systems increases and supply chain complexities intensify,
As Canada embraces a transition to a digitalized energy
cyber threats to operational technology (OT) and third-par-
grid, cybersecurity in the energy and utility sector has
ty vulnerabilities present heightened risks. This article
become a critical concern. The increase in interconnected
provides an in-depth analysis of cybersecurity trends and
systems has brought efficiency and resilience to energy dis-
threats in the Canadian energy and utility sector, under-
tribution but also heightened the risk of cyberattacks. This
pinned by relevant statistics and strategic insights. With
article examines the state of cybersecurity in Canada’s en-
more than 75% of Canadian energy companies identifying
ergy sector, highlighting current trends, emerging threats,
supply chain risks as a primary cyber concern, proactive
and data on vulnerabilities impacting the landscape.
measures in cybersecurity have become essential. The piece
The State of Cybersecurity in Canada 2025 84

Trends Driving Cybersecurity in Canada’s Key Cybersecurity Threats Facing Canada’s
Energy Sector Energy and Utility Sector
1. Transition to Smart Grids and Renewable Energy
Percentage of critical infrastructure sectors in Canada reporting
According to the Canada Energy Regulator (CER), Canada
a cyber incident in 2019 Source: National Cyber Threat Assessment 2023-2024
is aggressively pursuing renewable energy sources, with
smart grids emerging as an essential component for man-
aging these resources. Smart grids rely on data-driven
insights to balance supply and demand across distributed
energy sources, making them vulnerable to cyber threats
targeting their operational technology (OT). The integra-
tion of renewable energy, however, also presents opportuni-
ties for cybersecurity, as distributed generation reduces the
concentration of critical assets in single locations, dispers-
ing risk.
2. Increasing Focus on Operational Technology (OT)
Security
Cybersecurity for OT systems, which control physical pro-
c
p
r
a
e
e
t
r
e
c
i
s
o
e
s
w
e
r
n
i
s
t
i
t
t
i
l
b
h
z
ik
a
u
l
e
t
l
e
i
l
g
o
e
e
a
t
n
l
i
e
c
n
d
c
y
.
t
u
r
i
U
e
n
ic
n
f
t
i
r
l
t
o
a
i
y
k
s
r
e
d
t
i
r
s
i
I
u
k
s
T
t
c
s
r
t
s
i
i
u
b
d
y
r
u
s
e
e
t
t
n
,
e
i
t
o
m
w
i
n
fi
h
s
,
e
,
i
d
h
c
O
h
a
i
T
s
n
c
s
s
a
t
e
y
h
n
e
s
e
t
n
b
e
C
e
m
a
y
c
n
b
s
h
e
i
o
a
n
r
f
l
c
l
t
C
e
r
e
e
n
e
n
a
n
g
o
s
t
i
e
n
r
p
e
g
e
i
’
n
s
r
t
-
o
Oil
&
Gas Healthcare
P
o
wer
Generati on
Finance
&
Insurance Minin g
Trans
p
ortati on Manufacturin g
A
griculture Water
protect against advanced cyber threats. In 2024, the focus
on protecting these systems is driving utility providers to
allocate greater resources toward risk mitigation and end- 1. Ransomware Attacks
point protection within OT environments.
Ransomware remains one of the most prevalent threats in
3. Investment in Artificial Intelligence (AI) and Predictive the Canadian energy sector. As demonstrated by the recent
Analytics cybersecurity incident at Suncor Energy, cybercriminals tar-
get energy companies for their critical role in national in-
In response to growing threats, energy companies are
frastructure, exploiting the high stakes to demand ransom
increasingly investing in AI and machine learning to
payments. In Suncor’s case, devices were swapped out after
monitor for anomalies and predict potential attacks. These
an attack to restore security. These incidents underscore the
technologies, driven by data gathered across the network,
vulnerability of energy systems to ransom-based extortion
enhance threat detection capabilities, allowing companies
tactics, which can disrupt service delivery and incur signifi-
to respond before incidents escalate. This shift aligns with
cant financial losses.
national cybersecurity objectives outlined in the National
Cyber Threat Assessment 2025-2026, which highlights 2. Insider Threats
predictive analytics as a key tool for defending critical
Insider threats, whether unintentional or malicious, are
infrastructure.
particularly concerning in energy environments, where em-
4. Supply Chain Security ployees and contractors often have access to sensitive OT
and IT systems. A Canadian Cyber Centre report highlights
A noteworthy trend in cybersecurity is the increased scru-
the importance of monitoring privileged access to prevent
tiny on third-party providers, as supply chain risks have
unauthorized actions that could compromise operation-
escalated with the increased interconnectivity of systems.
al integrity. Enhancing insider threat detection through
The interconnected nature of the energy supply chain ne-
role-based access control and continuous monitoring has
cessitates thorough vendor assessments and adherence to
therefore become a standard practice in the industry.
rigorous cybersecurity standards, as breaches originating in
supplier networks can compromise utility networks.
Safeguarding Canada’s Power by Denrich Sanada and Sonia Khan The State of Cybersecurity in Canada 2025 85

3. State-Sponsored Attacks weaknesses rapidly. Quantum comput- 4. Impact of State-Sponsored
ing could break modern cryptographic Cyber Activity:
State-sponsored cyberattacks pose a
ciphers, endangering encrypted com-
persistent risk due to the geopoliti- Canada’s National Cyber Threat
munications, while AI-driven phishing
cal importance of Canada’s energy Assessment highlights that geopo-
and deepfakes could lead to more
assets. The National Cyber Threat litical tensions have led to a surge
convincing disinformation campaigns
Assessment notes that state-sponsored in cyber espionage, with Canadian
and identity fraud. With AI relying on
actors, often aiming to cause disrup- oil and gas companies identified
vast datasets and quantum comput-
tion or gather intelligence, target as likely targets of state-sponsored
ing offering unparalleled processing
critical infrastructure. These highly cyber actors, who seek trade secrets
speeds, the risk of privacy breaches
coordinated and sophisticated attacks and potentially exploit OT systems to
and identity theft grows, exposing
can manipulate OT systems, making disrupt operations.
sensitive information from seemingly
them difficult to detect and prevent.
innocuous data. 5. Utility Cybersecurity Incidents:
Their potential to impact national
security necessitates collaboration Specific incidents, such as the recent
between government and industry to Key Data and Statistics cybersecurity breach at Suncor, reflect
safeguard critical assets. ongoing vulnerabilities. Suncor’s
1. Distribution of Cyber Threat Types
response involved the replacement of
4. Phishing and Social Engineering in the Canadian Energy Sector:
hardware and an overhaul of cyber-
Attacks
Ransomware attacks and phishing security protocols, underscoring the
Social engineering remains an effective scams comprise 62% of cyber inci- costly implications of such breaches
tactic for attackers targeting the energy dents reported by Canadian energy on operational continuity.
sector. The Canadian Cyber Security companies in recent years, making
Centre’s findings highlight phishing them primary attack vectors. Email
Cybersecurity Measures and
as a common initial access meth- fraud is a particular risk, with 77% of
Resilience Strategies
od for attackers, who then leverage Canadian energy organizations report-
compromised credentials to infiltrate edly lacking robust protections against 1. Risk Management and
networks. Utility providers are increas- these attacks. Resilience Planning
ingly deploying training programs
2. Supply Chain and Third-Party Risk Proactive risk management is now
to educate employees on identifying
Perceptions: foundational in Canada’s energy sec-
phishing attempts, as awareness can be
tor. Utility companies conduct thor-
a crucial first line of defense. According to PwC’s survey, over 75%
ough risk assessments that cover both
of energy and utility sector profes-
5. Vulnerabilities in Industrial IT and OT systems, enabling them to
sionals in Canada view supply chain
Control Systems (ICS) identify vulnerabilities and prioritize
complexity as a significant risk to cy-
resources effectively. The sector’s
ICS, which are essential to energy bersecurity. Efforts such as enhanced
focus on resilience ensures rapid re-
distribution, are especially susceptible third-party verification and cross-in-
covery in the event of an attack, with
to cyber threats due to their reliance dustry collaboration are emerging
many companies implementing conti-
on legacy technologies. The operation- strategies, but blind spots remain in
nuity plans and network segmentation
al continuity of these systems makes governance and accountability across
to isolate compromised segments.
them attractive targets, as disruptions supplier tiers.
can have severe consequences. Many 2. Implementation of Zero Trust
3. Sector Spending on
Canadian energy companies are up- Architecture
Cybersecurity:
grading these systems or adopting new
To combat insider threats, many en-
security measures, such as network Industry reports indicate that invest-
ergy organizations are adopting Zero
segmentation, to contain breaches. ments in cybersecurity have increased
Trust models, which require verifica-
across the sector, with energy compa-
6. AI and Quantum Computing tion at every access point and limit lat-
nies devoting approximately 10% of
eral movement within networks. Zero
AI, combined with quantum capabili- their IT budgets to cybersecurity in
Trust reduces the risk posed by com-
ties, may accelerate vulnerability dis- response to heightened threat levels
promised credentials, helping energy
covery, enabling attackers to exploit and regulatory requirements.
Safeguarding Canada’s Power by Denrich Sanada and Sonia Khan The State of Cybersecurity in Canada 2025 86

companies prevent attackers from measures to protect against evolv-
gaining access to critical systems even ing threats. Trends in AI, predictive
if they breach the network perimeter. analytics, and Zero Trust architecture,
alongside a focus on OT security
3. Enhanced Collaboration Between
and supply chain resilience, equip
Industry and Government
Canada’s energy sector to tackle a
To counter sophisticated threats, the complex threat landscape. By adopt-
Canadian energy sector relies on col- ing proactive risk management and
laboration with government agencies, fostering collaboration with govern-
particularly through initiatives like ment agencies, Canadian energy orga-
the Canadian Cyber Threat Exchange nizations are enhancing their cyberse-
(CCTX). Through such partnerships, curity posture, aiming to ensure a safe
energy companies share intelligence and resilient energy future.
on threats and vulnerabilities, build-
ing a collective defense posture that
References
benefits the entire sector.
Canada’s Energy Transition: Historical and
4. Employee Training and
Future Changes to Energy Systems –
Awareness Programs
Update – An Energy Market Assessment
Employee awareness is crucial in miti-
Suncor swaps out laptops after cybersecurity
gating phishing and social engineering
incident as energy sector takes stock of risks
threats. Training programs tailored
to the energy sector emphasize best National Cyber Threat Assessment 2025-2026
practices for recognizing phishing
Cyber threat bulletin: The cyber threat to
emails and understanding the im-
Canada’s electricity sector
portance of cybersecurity hygiene.
Companies also conduct regular sim- News & Insights: Cybersecurity Threat
ulations to test employee responses, Landscape in the Canadian Energy Industry
reinforcing a culture of vigilance.
The top 6 trends shaping the energy sector
in 2024
5. Adoption of AI and Machine
Denrich Sananda is a seasoned Industrial
Learning
Cybersecurity Consultant with extensive ex-
Predictive analytics powered by AI perience in securing Operational Technology
plays a growing role in the energy (OT) environments. With a background in
sector’s cybersecurity strategy. By an- automation and a deep understanding of stan-
alyzing vast amounts of network data, dards like NERC CIP, ISA/IEC 62443 etc., he
these technologies detect patterns that specializes in assessing and mitigating cyber
indicate potential attacks, allowing risks in critical infrastructure sectors across
for timely responses. Such tools align Canada and Middle East.
with the national strategy to strength-
en cyber defenses, as highlighted in Sonia Khan is a Cybersecurity Consultant
the National Cyber Threat Assessment at Arista Cybersecurity Services, special-
2025-2026. izing in safeguarding critical infrastructure
in Canada. With Master’s in Electrical and
Software Engineering, and years of experi-
Conclusion
ence in research and teaching, she focuses on
The Canadian energy and utility developing secure, innovative solutions for the
sector’s growing reliance on digital industrial and energy.
technologies and interconnectivity
requires heightened cybersecurity
Safeguarding Canada’s Power by Denrich Sanada and Sonia Khan The State of Cybersecurity in Canada 2025 87

Beyond the Badge: Cybercrime
Challenges and Solutions in
Modern Policing
by Lina Dabit
Cybercrime investigations pose unique challenges for law investigations. Determining which country has the au-
enforcement globally. Many agencies established special- thority to investigate and prosecute complicates efforts
ized units to combat computer-based in the early 2000s as to coordinate across borders. The collection of digital
the internet became widespread and cybercrime started to evidence, as well as the investigative processes utilized to
rise. As cybercrime continues to grow exponentially and collect it, can vary considerably. Additionally, legislative
threat actors capitalize on rapidly evolving technology, po- and legal frameworks vary by country which means that
licing capabilities have not kept pace. Let’s examine some the definitions of cybercrime, and the relevant statutes,
of the significant challenges facing law enforcement today, are not always consistent. Balancing the need for effective
but more importantly, the strategies being undertaken to cybercrime investigations with the protection of individual
effectively combat cybercrime. privacy rights is an ongoing challenge. For example, a re-
cent Canadian Supreme Court decision, R v. Bykovets, ruled
The borderless nature of cybercrime means that juris-
that Canadians have a reasonable expectation of privacy
dictional issues continue to have an outsized impact on
The State of Cybersecurity in Canada 2025 88

in their Internet Protocol (IP) addresses. As a result, law police have had to work under the constraints of a Supreme
enforcement agencies must obtain judicial authorization Court decision, R v. Jordan which established new rules
to compel internet service providers to disclose IP address for determining when a criminal trial is considered un-
information. This ruling in particular is significantly more reasonable. The Supreme Court set a presumptive ceiling
restrictive than many of our international partners and cre- of eighteen months for provincial court trial; this means
ates additional steps for Canadian law enforcement, which that from the moment a charge is laid, police and prose-
sometimes impacts how quickly information can be shared. cutors have eighteen months until the anticipated end of
a trial. This is balanced against R v. Stinchcombe, another
While digital investigations have been a part of criminal
Supreme Court ruling that stipulates that the Crown must
investigations for more than twenty-five years, they remain
disclose all relevant information to the accused in a timely
a highly specialized capability within policing. Police
officers often have excellent investigative skills that allow
them to apply their expertise to cases ranging from orga-
Had our investigative
nized crime to homicides and global drug investigations.
But many police officers do not have a tech background,
and policing is ever more reliant on a small number of team printed off
highly trained officers. Many law enforcement agencies
struggle with limited budgets and resources while the
all the evidence
development of effective cybercrime investigators takes a
significant investment of both time and money. All while
criminals rapidly change tactics to evade authorities and they gathered, the
exploit the opportunities available in the cyber realm. One
of the trends we are seeing is how cyber is fast becoming
volume of paper
the underpinning of a significant component of criminal-
ity beyond ransomware; data and cryptocurrency cartels,
money-laundering, organized crime trafficking in drugs, would have filled an
humans or data. If there is one thing I have learned in
thirty years of policing, it is that criminals are adept at
entire hockey arena.
identifying and utilizing opportunities. The lucrative
potential of cybercrime is seeing an emergence of “tradi-
tional” organized crime groups capitalizing on the reach
and availability cyber represents. Yet policing continually
takes a reactive rather than proactive approach, even while and meaningful way. These rules are in place regardless of
the pace of evolution in this space demands that we move whether the crime is shoplifting or a major cyber-enabled
more quickly to meet emerging threats. fraud. The difference is that in the majority of cybercrime
investigations, the volume of data is significant.
The rapid evolution of technology presents both opportu-
nities and challenges for law enforcement. As technology On our Netwalker affiliate investigation, had our investi-
advances, cybercriminals develop increasingly sophisticated gative team printed off all the evidence they gathered, the
methods to commit crimes, and makes it harder for police volume of paper would have filled an entire hockey arena.
to detect and respond to these threats. The emerge of AI in In another investigation, more than eight (8) terabytes of
particular, can be a bane or boon depending on who you data was seized and the significant resource draw to review
speak to. The reality is that AI is not one of the other; it is and prepare the disclosure was considerable. As policing
both, and can be leveraged for the power of good or bad. moves towards the use of AI and other cutting-edge tech-
The difference is that law enforcement has a number of nologies, I am confident this will greatly enhance both the
guardrails (rightfully so) to ensure that we operate within timeliness and effectiveness of investigative responses of
the confines of our legal authorities, while threat actors future investigations.
have ZERO rules.
So how is law enforcement responding to these challeng-
One of the ways that AI in particular can be utilized effec- es? The collaborative approach to cybercrime is one of the
tively is to address the sheer volume of data law enforce- most effective strategies we have in our arsenal. The will-
ment in Canada must contend with. Since 2016, Canadian ingness of international partnerships to share intelligence,
Beyond the Badge by Lina Dabit The State of Cybersecurity in Canada 2025 89

coordinate investigations, and work to apprehend cyber-
criminals greatly mitigates the impacts of cross-border
criminality. While Joint Force Operations (JFOs) are not
new, the ways in which policing have come together to
combat cybercrime demonstrates how effective we can be
when we work together. Additionally, the emergence of
public-private partnerships highlights a number of strate-
gies that can be utilized in the protection of Canadians. The
FBI recognized the value of public and private partnerships
to combat cybercrime decades ago. Private sector entities
have significantly more resources, both human and tech-
nology, than policing and their willingness to share these
resources means that we are better equipped to combat
threats to our critical infrastructure.
Many law enforcement agencies in Canada recognize the
importance of building partnerships with private sector,
academia and all levels of government. Both the National
Coordination Centre (NC3) and the Canadian Centre for
Cyber Security (CCCS) actively engage in public-private
partnerships to enhance cybersecurity across Canada. These
partnerships involve critical infrastructure owners and
all levels of government to share threat information and
strengthen Canada’s resilience against cyber threats.
When I started policing thirty years ago, I never imagined
a world where cybercrime was such a significant part of my
work because it seemed more sci-fi than reality. But I am
heartened to see how law enforcement has stepped up to
the challenge and I look forward to seeing the evolution of
policing in this space.
Inspector Lina Dabit joined the RCMP in 1994 and started her career in
BC working a variety of duties ranging from uniform patrol, drug section,
major crime, intelligence, and border integrity.
After transferring to Ontario in 2008, she focused on organized crime,
national security and established the RCMP interview team in Ontario.
She was commissioned in 2017 as commander of the Toronto Air
Marshals. Since 2021, she has led the Cybercrime Investigative Team
with a strong focus on operational collaboration between federal, inter-
national and private sector partnerships.
Beyond the Badge by Lina Dabit The State of Cybersecurity in Canada 2025 90

Canada’s Education Sector: A Low-Hanging
Fruit for Cyber Criminals?
by Lester Chng
Why is the education sector at risk? 1. IT AND CYBERSECURITY INVESTMENT.
Canada’s education sector – comprising K-12 schools, Corporations that manage large numbers of users and
post-secondary institutions, and specialized vocational sensitive information tend to have the budget to support
colleges – is highly reliant on technology for delivering and maintaining and upgrading technology. This is not the case
fulfilling key functions. The schools manage a vast amount for most educational institutions where lack of investments
of personal information and intellectual property. The has hindered technology maintenance, adoption of security
population of end users of the organization’s network and tools, and the manpower required to monitor and respond
information systems also challenges the administration. to cybersecurity alerts.
The users range from students, contractors, industry part-
2. MONITORING ABILITY.
ners, and staff. Building a security culture across a diverse
population of users, especially where a large proportion are The lack of awareness of user behavior, indicators, or the
constantly changing, will continue to be a challenge for all ability to interpret data provides a challenge to detect and
educational institutions. respond promptly. In a mature enterprise, tools are used
to track user behavior, analyze patterns, and take precau-
These are not unique challenges to the education sector.
tionary action to alert security teams of anomalous actions.
However, some conditions make them a more enticing tar- This is supported by policies for an employer to observe an
get for cybercriminals. employee’s actions on a corporate machine legally. Both
The State of Cybersecurity in Canada 2025 91

technology limitations and policy constraints hamper the were offline. Lengthy recovery times hampered student
education sector. learning outcomes and impacted institutional credibility.
3. CONTROL OF DIGITAL TOOLS. 2. FINANCIAL CONSEQUENCES:
The education sector has faced the onslaught of the ar- The financial impact was multifaceted. Direct costs includ-
tificial intelligence tools that the general population has ed forensic investigation, external IT support, hardware
rapidly adopted. Even if the IT teams have attempted to procurement, and legal fees. There were indirect costs, like
blacklist, educate, write policy, and enforce controls, it is damage to an institution’s reputation and the subsequent
likely students or staff have already misused these applica- loss of trust among current and prospective students.
tions. The challenge remains for educational institutions to
3. DATA PRIVACY CONCERNS:
govern the adoption and appropriate use of digital tools.
Breaches in educational contexts led to unauthorized access
4. PERSONAL INFORMATION AND INTELLECTUAL
to highly sensitive information. This included student IDs,
PROPERTY.
addresses, health records (if maintained by the institution),
Educational institutions manage information that is high- and financial information. In more severe cases, the institu-
ly valuable to cybercriminals. These range from personal tions also lost information from vendors, staff, recruitment
information, health information, financial information, applicants, and special research projects. Privacy violations
and intellectual property via research and collaboration have long-term consequences, including identity theft risks
with government and private sector organizations. There for affected individuals and permanent damage to the insti-
is also the risk that highly classified research or intellectual tution’s brand.
property can be stolen. The management and protection
4. LEGAL AND REGULATORY RAMIFICATIONS:
of information by classifying data, encryption, segregation
of duties, access control and other means will fall short of Institutions that failed to protect their data adequately
enterprise industry standards due to the lack of resources faced potential for legal consequences and risked running
and competing priorities. afoul of Canadian privacy laws, including the Personal
Information Protection and Electronic Documents Act
5. LACK OF TRAINING AND PRIORITIZATION.
(PIPEDA) and various provincial privacy statutes.
While most educational institutions have embarked on
basic cybersecurity hygiene training, it is likely insufficient.
What does the future hold?
The gap includes role-specific training for personnel with
cybersecurity responsibilities. This gap affects everyone - The threat actors remain active and constantly evolve
from the IT team members struggling with new tools, new their tradecraft and operating models, as reported by the
processes, and additional workload to leaders assigned cy- Canadian Centre for Cyber Security in their National Cyber
bersecurity responsibilities. The level of readiness required Threat Assessment 2025-2026. While the collaboration of
to respond to a significant cybersecurity incident adequate- private and public sectors to disrupt key criminal organi-
ly will take a concerted training regime and the support zations has yielded some promising results, cybersecurity
from leaders to prioritize resources. threats will likely persist in the foreseeable future.
The education sector also faces a challenging backdrop.
What were the impacts of recent cyber attacks With high rising costs and other competing areas of con-
on the sector? cern, there continues to be a resource allocation issue that
will hamper the technology upgrades and expertise needed
Cyberattacks on Canadian educational institutions pro-
to improve the cybersecurity posture of education institu-
duced a ripple effect of harm far beyond the immediate
tions. Along with that, the recent policy changes impact
technical disruption.
the number of international students and exacerbate the
1. OPERATIONAL DISRUPTIONS: problem as institutions are forced to tighten budgets.
During significant cybersecurity incidents, such as ransom- The cyber risks remain high. The operating environment is
ware, the educational process halts. Classes were suspend- far from ideal.
ed, assignments became inaccessible, and email services,
However, institutions cannot afford to remain passive.
school domains, internet services, and even phone systems
Canada’s Education Sector by Lester Chng The State of Cybersecurity in Canada 2025 92

What can be done? 4. INVEST IN INCIDENT RESPONSE PLANNING AND
EXERCISES.
Educational institutions need to continue the good fight.
Those responsible for protecting these institutions must be Preparation is the key to minimizing the impact of a cyber
resourceful, collaborative, and judicious in enhancing cyber incident. Every institution should have a well-document-
resilience. ed and regularly updated incident response plan (IRP).
Beyond documentation, conducting tabletop exercises and
1. FOSTER A CULTURE OF CYBERSECURITY AWARENESS.
simulated cyberattacks can prepare staff and leadership to
Building a robust cybersecurity culture is crucial. respond swiftly and effectively when an incident occurs.
Institutions should prioritize ongoing training and aware-
5. MAXIMIZE EXISTING TECHNOLOGY.
ness campaigns tailored to the diverse user base, including
students, staff, and contractors. Cybersecurity hygiene While budget constraints may limit the adoption of cut-
cannot only be a checkbox exercise but a core component ting-edge tools, institutions can maximize the use of
of the educational experience. Regular phishing simulations their current technology by configuring systems correctly,
and interactive learning opportunities can reinforce good applying patches promptly, and employing open-source or
security practices. low-cost cybersecurity solutions where appropriate.
6. ADVOCATE FOR SECTOR-WIDE SUPPORT.
Those responsible
Education leaders must advocate for increased govern-
for protecting these ment funding and support for cybersecurity in the sector.
Highlighting the potential long-term costs of inaction can
institutions must help stakeholders understand the importance of proactive
investment in cybersecurity measures.
be resourceful,
Conclusion
collaborative, and
Canada’s education sector sits at a precarious crossroads.
judicious in enhancing While it faces significant challenges, these challenges are
not insurmountable. With strategic investments, cross-sec-
cyber resilience. tor collaboration, and a steadfast commitment to fostering
cyber resilience, educational institutions can protect their
students, staff, and intellectual assets from the ever-present
threats posed by cybercriminals.
2. LEVERAGE PARTNERSHIPS AND SHARED SERVICES.
You don’t have to be at the top of the tree. Just don’t be the
Collaboration is essential for resource-constrained organi-
lowest-hanging fruit.
zations. Educational institutions can pool resources by par-
ticipating in shared cybersecurity services or collaborating
with sector-specific organizations like the Canadian Cyber Lester Chng is a Senior Cybersecurity Advisor at the Rogers Cybersecure
Threat Exchange (CCTX). Partnering with local government Catalyst, where he leverages his CISSP and PMP certifications to guide
and private sector entities can provide access to expertise, clients through complex cyber exercises and risk management initiatives.
tools, and threat intelligence that would otherwise be With extensive experience designing and implementing large-scale
unaffordable. exercise programs across North America’s financial services sector and
within military environments, he is well-versed in navigating high-stakes,
3. ADOPT A RISK-BASED APPROACH TO CYBERSECURITY.
security-critical scenarios.
Institutions should identify their most critical assets—
whether it’s sensitive student data, research projects, or op-
erational systems—and focus on securing these areas first.
Implementing basic security measures, such as multi-factor
authentication (MFA), network segmentation, and regular
vulnerability assessments, can significantly reduce risks
without requiring large investments.
Canada’s Education Sector by Lester Chng The State of Cybersecurity in Canada 2025 93

Addressing the talent gap:
Focusing on mid-career
transitions
by Randy Purse
The cybersecurity talent shortage continues to receive global survey of 1850 senior IT and cybersecurity deci-
significant attention. And rightly so. A lack of cybersecuri- sion makers (Fortinet, 2024).
ty talent creates additional risks for organizations and for
We should first define what we mean by cybersecurity talent
Canadians writ large. For individuals and organizations,
in workforce terms. The majority of the attention is on the
these risks translate to financial losses,
lack of cybersecurity professionals as defined by the National
personal harms, and reputational damage in addition to Occupation Classification (NOC) 21220. We also need to
other impacts. Beyond this, a lack of cybersecurity talent at keep in mind that there are many adjacent roles that require
the national level coupled with the increase in cybercrime critical cybersecurity knowledge, skills, and abilities (KSAs)
and state sponsored activities, creates risks to our economy, such as those in information technology, communications,
our democracy, and our national security. engineering, software, business, and management. This
latter group also warrants attention as they are a crucial
“70% of respondents agree that the cybersecurity skills
component to addressing the talent gap. However, for this
shortage creates additional risks for their organizations…
article, the focus will remain those we define as cybersecu-
The most difficult roles to fill continue to be security
rity professionals where most of their work effort is on the
operations and cloud security…54% of organizations say
application of KSA towards cybersecurity goals.
they struggle to recruit cybersecurity talent.” Based on a
The State of Cybersecurity in Canada 2025 94

Dependency on post-secondary graduate to generate Leveraging the existing workforce
the workforce
“While organizations worldwide certainly face substan-
Unfortunately, there is a paucity of reliable data on the cy- tial challenges when it comes to safeguarding their dig-
bersecurity talent gap or the available training and educa- ital assets, there are many strategies we can collectively
tion in Canada. Based on current reporting on cybersecurity pursue that will help to close the cybersecurity skills gap
positions, we can see a shortage of between 10,000 and and augment individuals with the talent they need, and
25,000 in the coming years. every organization needs. But recruiting and retaining
qualified professionals will inevitably require creative
Post-secondary institutions are the traditional workforce
strategies, and public and private sector organizations
generation channel. Based on the Canadian Centre for
must collaborate to bring many of these to fruition.”
Cybersecurity Post-secondary cyber security related pro-
(World Economic Forum, 2023)
grams guide, there are 144 Canadian cybersecurity courses
and programs; this is over a two-fold increase since incep- There is a large untapped pool of available talent – mid-ca-
tion. Despite this, the talent gap has only widened as the reer workers that are looking to transition to other careers.
demand across industry has increased. Presently, there are thousands of Canadian workers that are
eager to transition to new careers. Many are in declining
That said, even if all (125) diploma, degree and certificate
industries, are unemployed or feel underemployed. Others
programs including advanced degrees produced a 30-per-
are simply looking at their potential futures and are seeking
son cohort every year, this would create approximately
more sustainable work.
3,750 workers assuming all graduated. This is, however, an
optimistic estimate given the limited interest in cybersecuri- Broadly speaking, reskilling initiatives are intended to pro-
ty programs, student attrition, and the increasing numbers vide needs-based learning opportunities so individuals can
of graduates leaving Canada for better opportunities. obtain new or different KSAs that enable them to transition
to and perform effectively in a new field of work. In cyber-
security, reskilling initiatives have demonstrated significant
success at supporting over a thousand mid-career workers
If we are going to have a talent transition to cybersecurity work.
pipeline sufficient to address the While delivered within different business and funding mod-
els, reskilling initiatives have some common characteristics:
need, we should be looking to
• They target specific workforce gaps and provide rapid
reskilling focused on industry needs.
better leverage alternative talent
• Unlike most post-secondary programs, they actively
generation channels.
recruit into their programs including tapping into under-
employed or underrepresented populations.
• They will typically have an application and screening
Another factor contributing to post-secondary education- process to help ensure that candidates are the right fit for
al challenges is that the quality of the programming is at the work.
times suspect. Employers are often frustrated by “gaps in
• They recognize the value of experience and build on an
practical training and a misalignment between academic
individual’s existing competencies creating a far shorter
programs and job readiness.” (CCN, 2024)
learning pathway to proficiency.
So, while Canadian post-secondary programming has signifi-
• They often include industry recognized certifications
cantly increased over the past decade, both its ability to gener-
or credentials that provide assessment and evidence of
ate sufficient job-ready graduates and its ability keep pace with
graduate competency for the work.
the changing threat and technical landscape remain uncertain.
• They typically have industry sponsors or partners that
If we are going to have a talent pipeline sufficient to address
help define the program, ensuring currency and rele-
the need, we should be looking to better leverage alternative
vance as well as providing work experience or employ-
talent generation channels. One channel that has shown
ment opportunities for graduates.
tremendous promise is reskilling of the existing workforce.
Addressing the talent gap by Randy Purse The State of Cybersecurity in Canada 2025 95

• They provide learning pathway support using mentors or coaches that help
guide the candidates through the program and connect the learning to their
future work.
• They provide career transition support that assist candidates in identifying
and preparing for the job search and, critically, getting employment in their
new field.
• Finally, the costs of the programs may also be subsidized.
Examples of successful cybersecurity reskilling programs are provided in table 1.
Table 1 — Examples of effective reskilling programs
Rogers Cybersecure Catalyst Accelerated Cybersecurity Training
Program and Certifications for Leadership in Cybersecurity
Lighthouse Labs Cybersecurity Bootcamp
University of Ottawa’s Professional Development Institute,
Coding for Veterans
While not yet widely available or accessible across Canada, these programs have
been quite successful at helping mid-career workers rapidly update their skills
and transition to the cybersecurity field. A high percentage of the candidates
fully complete their programs, obtain an industry relevant certification. and find
employment within six months of completion. And based on reporting from the
program operators, most graduates are that they chose a new career in cyber-
security; they have a future-proof career, potential for continuous learning and
advancement, and garner well above average compensation and benefits.
Given the risks posed by the lack of cybersecurity talent, this seems to be a rea-
sonable return on investment and a win-win-win for the workers, the employers
and Canada. However, despite the growing need for cybersecurity talent, the
success of these programs and the large untapped pool of mid-career workers,
there is no sustained programming that is widely available.
Conclusion
“In Canada, we need to not only address the shortage (capacity) of cyberse-
curity talent, but also prepare for an expanding requirement and the evolu-
tion of the cybersecurity landscape (capability). Capacity means that Canada
has the right number of people to meet the broader societal and industrial
needs. Capability means that the people have the right competencies (knowl-
edge, skills, abilities, and other characteristics) that can meet the need.”
(Technation, 2019)
While post-secondary institutions are helping to close Canada’s cybersecurity tal-
ent gap, they struggle to generate sufficient graduates to meet the industry needs
of today and tomorrow. Continued investment in post-secondary institutions and
Addressing the talent gap by Randy Purse The State of Cybersecurity in Canada 2025 96

more agile approaches to curriculum References
design and program delivery will help
Canadian Centre for Cyber Security
ensure that they can produce more
(2024). Post-secondary cyber security
job-ready graduates.
related programs guide, retrieved 18
In the meantime, however, the lack of October, 2024
cybersecurity talent means that we re-
Canadian Cybersecurity Network (2024). The
main at risk. Reskilling programs have
cybersecurity skills crisis: Canada’s call
demonstrated the potential to:
to action, retrieved 10 December, 2024
• Rapidly generate development
Fortinet (2024). 2024 Cybersecurity skills
of cybersecurity professionals
gap: Global research report, retrieved
to help significantly reduce the
November 8, 2024
cybersecurity talent gap;
Technation (2019). Perspectives on a Canadian
• Offer opportunities for thousands
cybersecurity workforce development frame-
of people in the existing workforce
work: A literature review.
to pursue well-paid, sustaining
careers; and Statistics Canada (2021). National
Occupation Classification (NOC) 21220
• Provide a return on investment
Version 1.0, retrieved November 8, 2024
at all levels through meaningfully
employed, well- compensated work- World Economic Form (2023). How reskill-
ers, improved cybersecurity, and ing and upskilling talent can help shrink
reduced risks with organizations the cybersecurity skills gap, retrieved
and across the Canadian economy. November 8, 2024
So, there appears to be a sound
Randy Purse, CD, PhD, CTDP is a veteran of
business case to invest in and expand
the Royal Canadian Navy (RCN), with expe-
reskilling programs for mid-career
rience in several security roles, Randy is also
workers to help close the cyberse-
the former Strategic Advisor of Cybersecurity
curity talent gap. Yet, these types of
Training and Education at the Canadian Centre
programs are not widely accessible
for Cyber Security as well as the previous
across Canada and there appears
Director of Cybersecurity Standards and Vice
to be limited commitment to their
President of Future Workforce Development at
continuity in the face of several other
Technation. He joined the Rogers Cybersecure
competing priorities.
Catalyst at Toronto Metropolitan University in
Understanding the risks that the 2021 where he focuses on designing and facil-
cybersecurity talent gap presents to itating cyber security training & education for a
Canada and Canadians, this leaves variety of academic and professional audienc-
one question: why aren’t we con- es. He continues to research, write and consult
sidering a means to offer sustained, on cybersecurity, workforce development, and
nation-wide delivery of these types of workplace learning.
programs to more rapidly close the
talent gap?
Addressing the talent gap by Randy Purse The State of Cybersecurity in Canada 2025 97

Let us find you the best
senior tech talent
We put Canada’s largest
“
cybersecurity network
to work for you and
your company.”
François Guay
Founder of CCN and master recruiter
Learn more
canadiancybersecuritynetwork.com/recruitment-partner

Buggy Code: An In-Depth Look at the
Cybersecurity Job Market
by François Guay
The cybersecurity job market is in a state of rapid evolu- CanadianCybersecurityJobs.com, spanning three years,
tion, driven by increasing demand for skilled professionals further enriched the analysis. This robust approach allowed
to address complex and ever-growing security challenges. for a nuanced understanding of the challenges faced by both
However, much like a piece of buggy code that disrupts employers and job seekers, revealing areas where alignment
the functionality of a system, misalignments between job and strategic interventions are most needed — much like
seeker qualifications and employer expectations are cre- debugging a flawed system to improve overall performance.
ating inefficiencies in Canada’s cybersecurity workforce.
Canada’s urban centers have assumed control of cyber-
This report synthesizes key insights gathered from job
security, leaving people from rural and smaller regional
postings, employer surveys, and job seeker data to provide
centers on the outside. In a country that depends on
a comprehensive understanding of current trends, barri-
communications technology more than most due to its
ers, and opportunities.
size, regional centers need to be producing cyber ex-
pertise because everywhere in Canada depends on ICT
Survey and Data Overview to connect, provide essential services, and participate
in the digital economy. It is essential that we de-ur-
The research encompassed a wide range of participants
banize cybersecurity and move towards agile, smaller,
and methodologies to ensure a holistic perspective.
regional programs that support both cyber awareness
Surveys targeted thousands of job seekers and hundreds
and expertise if all of Canada is to benefit from digital
of employers, utilizing online distribution and in-per-
transformation.
son small group discussions to gather detailed insights.
— Timothy King, ICTC
Data on over 10,000 cybersecurity job postings from
The State of Cybersecurity in Canada 2025 99

Key Findings GEOGRAPHICAL CONCENTRATION
CERTIFICATIONS AND SKILLS The majority of cybersecurity jobs were concentrated in
Toronto (35%), Ottawa (22%), and Vancouver (15%). This
Certifications such as CISA, CISSP, and CompTIA Security+
regional focus creates accessibility challenges for candidates
were required in approximately 68% of job postings.
in other areas, while employers sought institutional partner-
Employers frequently highlighted deficiencies in certifica-
ships to bridge gaps in underserved regions. Like buggy code,
tions and technical abilities among candidates as major
this geographical concentration limits functionality across the
challenges, while job seekers expressed frustration with
broader system — in this case, Canada’s workforce.
unclear pathways to certification and limited access to
advanced technical training. This disconnect mirrors a
The majority of cybersecurity job concentration by city
scenario where buggy code causes breakdowns in commu-
nication between system components, leaving inefficiencies
in the cybersecurity talent pipeline.
Certification Requirements in Job Postings
Toronto Ottawa
35% 22%
EXPERIENCE REQUIREMENTS
The average job posting demanded 4.3 years of experience,
yet only 10% were entry-level roles. Employers cited long
training cycles and misalignment between educational
Vancouver Others
curricula and industry needs as concerns. Job seekers, on
15% 28%
the other hand, identified the lack of entry-level opportuni-
ties as a key barrier to entering the workforce. Addressing
this challenge is akin to debugging a program to ensure
SOFT SKILLS AND DIVERSITY
smoother interactions between inputs and outputs.
Employers identified communication, teamwork, and diver-
Trends in Experience Requirements
sity as critical gaps in the talent pool. Job seekers noted a
lack of mentorship and industry promotion, which hindered
the development of these vital professional skills. These
gaps are reminiscent of missing modules in a program,
leaving the system vulnerable and incomplete.
TECHNICAL SKILLS AND TOOLS
Skills in IAM, cloud security, SIEM platforms, penetra-
tion testing, and DevSecOps tools were in high demand.
Employers emphasized the need for practical, hands-on train-
ing to reduce onboarding time, while job seekers felt their ed-
ucation was overly theoretical, lacking exposure to real-world
tools. The lack of practical skills mirrors poorly tested code
that fails to operate effectively in live environments.
Buggy Code by François Guay The State of Cybersecurity in Canada 2025 100
)sraeY(
ecneirepxE
egarevA
30% 25% 13% 32%
CISA CISSP CompTIA Other
Security+
4.3
4.25
4.2
4.15
4.1
2021 2022 2023
Year

Top Challenges Identified 4.PROMOTE ENTRY-LEVEL OPPORTUNITIES
1. For Employers: Skills gaps, lengthy training cycles, limit- Collaborate with employers to create realistic entry-level
ed diversity, and soft skills deficiencies. roles and establish pipelines that combine training with
hiring.
2. For Job Seekers: Scarcity of entry-level roles, high certi-
fication demands, and misalignment between education 5.DIVERSITY AND REGIONAL ACCESSIBILITY
and practical job requirements.
Advocate for remote work and decentralized job creation to
reduce geographical barriers and increase inclusivity.
Challenges Identified by Job Seekers
“‘Gone’ needs to be the days of ‘two years’ experience
is required for entry-level positions. The path to na-
10%
Limited Diversity tional cyber-resilience may lie with a version of crowd-
25% sourcing at scale — developing provincial and national
Skills Gaps
programs that encourage or subsidize the appren-
30%
Long Training Cycles ticeship and employment of entry-level staff to critical
35% infrastructure and adjacent industries. With the threats
Soft Skills Deficiencies
currently noted nationally, the time is now.”
— James Cairns, Bow Valley College
Conclusion
Recommendations The cybersecurity job market demonstrates a critical need
for improved alignment between job seeker aspirations
To bridge these gaps and debug the “buggy code” of
and employer expectations. Much like debugging faulty
Canada’s cybersecurity job market, the following strategies
code, addressing gaps in certifications, practical training,
are proposed:
and regional accessibility will require coordinated efforts
1.CREATE CLEAR CAREER PATHWAYS between industry, academia, and government. By imple-
menting the strategies outlined in this report, Canada can
Develop role-specific roadmaps with defined skills and
foster a robust, inclusive, and future-ready cybersecurity
certifications, supported by interactive guides for job
workforce — one that is free of the inefficiencies currently
seekers.
slowing its progress.
2.EXPAND AWARENESS CAMPAIGNS
Target underrepresented groups through outreach efforts, François Guay is the visionary founder of Canada’s largest cybersecurity
showcasing the diversity and scope of cybersecurity careers. network, the Canadian Cybersecurity Network (CCN), which unites over
44,000 members from diverse sectors, including individuals, businesses,
3.ENHANCE PRACTICAL TRAINING
universities, professional associations, diversity groups, and government
Strengthen partnerships between academia and industry agencies, representing nearly 1,000,000 people across the country.
to embed hands-on experiences and apprenticeships into Under François’s leadership, CCN has become a cornerstone in fostering
educational programs. collaboration, innovation, and security in Canada’s rapidly evolving
cybersecurity ecosystem.
Buggy Code by François Guay The State of Cybersecurity in Canada 2025 101

Key Recommendations
Strengthening Canada’s Cyber Resilience 4. FOSTER A SECURITY CULTURE
The 2025 State of Cybersecurity Report underscores that • Invest in behavior-focused training to address human
a reactive approach to cyber threats is no longer sufficient. error, which accounts for 82% of breaches according to
Organizations must transition to operational resiliency, a Verizon report.
ensuring they can continue critical functions even in the
• Encourage leadership buy-in to cultivate a
aftermath of a major cybersecurity attack. This involves
cybersecurity-first mindset across organizations.
implementing contingency plans that prioritize business
Paul Da Silva aptly notes,
continuity alongside robust cybersecurity measures. To for-
tify Canada’s cybersecurity landscape, the report outlines “Modern organizations can no longer rely on periodic
the following actionable strategies: snapshots or reactive measures. They need real-time,
adaptive cybersecurity approaches.”
1. ADOPT REAL-TIME CYBERSECURITY MEASURES
5. HARNESS EMERGING TECHNOLOGIES
• Prioritize advancements like Identity Threat Detection
and Response (ITDR) to address evolving identity-based • Embrace innovations like AI-powered anomaly detec-
threats. As Gartner highlights, ITDR is a cornerstone for tion to enhance threat identification and mitigation .
managing risks in cloud and hybrid environments.
• Build frameworks to manage risks associated with gen-
• Implement continuous monitoring systems to detect erative AI and deepfake technologies, which fraudsters
and respond to threats instantaneously, minimizing dam- are exploiting with increasing sophistication.
age from attacks like ransomware.
2. ADDRESS THE TALENT GAP Conclusion
• Scale mid-career reskilling programs to tap into under- The findings and recommendations outlined in this report
utilized talent pools, such as professionals from declining are a clarion call for stakeholders across Canada’s cyber-
industries or underrepresented regions. security ecosystem. By adopting real-time security mea-
sures, addressing the talent gap, fostering public-private
• Expand regionalized training initiatives to ensure eq-
collaboration, and cultivating a robust security culture,
uitable access to cybersecurity education across Canada.
Canada can secure its digital future and maintain global
François Guay emphasizes, “We must de-urbanize
competitiveness.
cybersecurity to support a truly national digital economy.”
Organizations, educators, and policymakers must work in
3. STRENGTHEN PUBLIC-PRIVATE COLLABORATION
concert to ensure the strategies proposed here are imple-
• Create frameworks similar to the U.S. Joint Cyber mented effectively. Together, we can create a more resilient
Defense Collaborative (JCDC) to align government re- and secure Canada, paving the way for sustained innova-
sources with private-sector expertise. tion and trust in our digital landscape. With operational
resiliency as the cornerstone of a robust cybersecurity posture,
• Offer financial incentives for SMBs to adopt Managed
Canada can ensure that its critical systems remain functional,
Detection and Response (MDR) services, enhancing their
even under attack.
ability to detect and mitigate advanced threats.
The State of Cybersecurity in Canada 2025 102