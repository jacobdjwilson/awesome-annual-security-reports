# X-Force Threat Intelligence Index 2026

Published 25 February 2026

## Table of Contents
- [Executive summary](#executive-summary)
- [Report highlights](#report-highlights)
- [Top initial access vectors](#top-initial-access-vectors)
- [Supply chain and third party compromises](#supply-chain-and-third-party-compromises)
- [Actions on objective](#actions-on-objective)
- [Blurring lines: the convergence of APT and cybercriminal techniques](#blurring-lines-the-convergence-of-apt-and-cybercriminal-techniques)
- [Impact](#impact)
- [Security 101: still lacking](#security-101-still-lacking)
- [AI in offensive cybersecurity](#ai-in-offensive-cybersecurity)
- [Geographic trends](#geographic-trends)
- [Industry trends](#industry-trends)
- [Recommendations](#recommendations)

## Executive summary
The biggest trends the IBM X-Force team observed in 2025 were a surge in broad‑based exploitations of exposed systems, weaknesses in software supply chains and growing systemic dependencies across cloud and application ecosystems.

Last year, attackers refined their techniques for infiltrating software distribution channels, cloud services and open‑source ecosystems. By doing this, they demonstrated how a single weak point in an interconnected environment can enable large‑scale or high‑privilege access.

X-Force, which pulled data from incident response and penetration tests, the dark web and other threat intelligence sources for this report, identified the leading initial access vector: the exploitation of public-facing applications. The team noted the growing number and complexity of software vulnerabilities—combined with misconfigurations in applications—and AI adoption broadened the attack surface for intrusions. Many vulnerabilities didn’t require authentication at all, highlighting the critical need for stronger access controls, rigorous patching and secure deployment practices.

X-Force also found credential theft remained at the center of many prominent campaigns. Meanwhile, the rapid adoption of AI chatbot platforms for consumers and workplace users introduced a new layer of exposure; credentials tied to these chatbots increasingly surfaced in underground marketplaces, driven largely by infostealer infections on end-user devices.

Threat actors often publicly exaggerate their reach and successes, which can inflate the perceived scale of these compromises. That said, the underlying trend X-Force identified is a clear warning for security leaders: organizations are accumulating sensitive authentication data on systems that may not be adequately secured. Law-enforcement takedowns managed to disrupt portions of the infostealer ecosystem in 2025, but these malware families continue to offer adversaries easy and effective means of gathering high-value credentials.

The ransomware ecosystem also shifted in 2025, becoming more fragmented and volatile, with many small groups conducting lower volume but widespread attacks. Data extortion, supply‑chain compromise and opportunistic targeting of smaller organizations remained prominent trends as well.

The tactics between nation‑state actors and cybercriminal groups continued to converge. X-Force noted tools, techniques and operational patterns increasingly overlapped between these threat communities, complicating attribution and potentially delaying appropriate response actions. In several instances, activity that initially appeared mundane later proved to be part of highly sophisticated, persistent operations.

Artificial intelligence also continued to reshape attacker operations in 2025. While AI has not changed playbooks, it has dramatically increased the speed, scale and efficiency of those operations. Adversaries are now using generative AI to shrink decision cycles, scale social engineering and iterate on attack paths in real time. As multimodal models mature, the barrier to entry will shrink further, allowing lower-skilled workers to automate reconnaissance, privilege escalation and lateral movement, resulting in faster‑moving, and more adaptive threats.

Despite these evolving trends and sometimes sophisticated threats, basic lapses in cybersecurity hygiene contributed to many compromises; X-Force incident response and penetration testing engagements found misconfigured access controls, weak authentication practices, incomplete logging and insufficient vulnerability management as recurring issues. These foundational weaknesses continued to provide attackers with opportunities that are far easier to exploit than advanced or novel techniques.

Overall, 2025 highlighted a clear message: identity protection, secure configuration and visibility across applications, development pipelines and cloud environments are increasingly central to cyber resilience. As attackers continue to refine credential‑driven and supply‑chain‑focused operations, strengthening these fundamentals remains the most effective defense.

The IBM X-Force Threat Intelligence Index 2026 focuses on observations from our expert team of analysts, researchers, and hackers, tracking how threat actors get in, what they do when they’re in, and the impact caused by each breach. X-Force offers these insights as a resource to IBM clients, cybersecurity researchers, policy makers, the media and the broader community of security professionals and business leaders. Through the work of our global team, we aim to deliver a data-driven view of the current threat landscape. It’s our intent to keep all parties informed of the current threat landscape so they can make the best decisions for reducing risk.

## Report highlights
- **44% increase in the exploitation of public-facing applications**: X-Force observed a rise in the exploitation of public-facing applications as an initial access vector in 2025 due to an increase in supply-chain attacks targeting development ecosystems and trusted infrastructure.
- **56% of disclosed vulnerabilities did not require authentication to successfully exploit**: The number of vulnerabilities tracked by X-Force approached 40,000 in 2025 and over half didn’t require authentication for an attacker to successfully exploit. This finding may reflect gaps in secure-by-design implementation as attackers are finding success without using credentials, MFA bypass or even end user interaction.
- **>300K ChatGPT credentials observed for sale on the dark web**: In 2025, infostealer malware enabled the exposure of over 300,000 ChatGPT credentials, demonstrating that AI platforms have reached the same credential risk as other core enterprise SaaS solutions. While none of the credentials posted were still valid, the credentials consistently corresponded to infostealer infections and leaked credentials collections observed in 2024 and earlier.
- **~4x increase in the number of major supply chain or third party breaches over 5 years**: Adversaries increasingly exploited developer trust and identity integrations to steal credentials, pivot into cloud environments and maintain persistence across interconnected systems. Sprawling third‑party dependencies create hard‑to‑secure attack surfaces—where one weak link can expose many targets.
- **49% increase in active ransomware groups compared to 2024**: Fragmentation continues in the space, with 109 different ransomware extortion groups identified by X-Force in 2025.
- **Manufacturing was the top-targeted industry for the fifth year in a row**: The sector accounted for 27.7% of incidents.
- **29% of attacks targeted North America**: North America became the most attacked region for the first time in 6 years.

![Chart: X-Force tracked nearly 40,000 vulnerabilities in 2025. Over half didn’t require authentication for an attacker to successfully exploit.]

## Top initial access vectors
### Rise of vulnerability exploitation
For the past 2 years, X-Force reported on the abuse of valid credentials as a top initial access vector. However, in 2025, X-Force observed a 44% increase in incidents caused by the exploitation of public-facing applications. This increase accounted for 40% of cases, whereas use of valid credentials made up only 32% of cases.

![Chart: Top initial access vectors X-Force observed in 2025 and 2024.]

This trend was compounded by a rise in supply‑chain attacks increasingly targeting development ecosystems and trusted infrastructure. This shift may also be connected to weaknesses in client environments where misconfigurations, weak authentication and insecure code—identified by Common Attack Pattern Enumeration and Classification’s CAPEC‑180, CAPEC‑49 and CAPEC‑242—consistently provided easy entry points.

![Chart: The growth of vulnerabilities since 2020.]

### Continued use of valid credentials
Although no longer the leading initial access vector, the misuse of valid accounts represented nearly a third of the cases. Campaigns built around credential theft as the enabling step show the same pattern:
- **Hive0145’s 2025 operation**: Delivered Strela Stealer to harvest Microsoft Outlook and Mozilla Thunderbird logins.
- **France-focused spear-phishing**: Used leaked ISP customer data to lure victims into entering Amazon credentials on a fake login page.

Beyond phishing, attackers target systems that store or manage high‑value credentials, such as Microsoft’s System Center Configuration Manager (SCCM). Once an attacker gains a foothold on a Configuration Manager site server, they can extract and decrypt service-account passwords stored in the SCCM database.

### AI chatbot credentials
The proliferation of AI chatbots in business operations created a new attack vector for cybercriminals utilizing infostealer malware. In 2025, over 300,000 ChatGPT credentials were observed for sale. Additionally, in February 2025, a threat actor claimed to have stolen over 20 million accounts. While none of the example credentials posted were still valid, the credentials consistently corresponded to infostealer infections and leaked credentials collections observed in 2024 and earlier.

## Supply chain and third party compromises
Throughout 2025, supply chain and third-party compromises took the form of coordinated, multi-stage campaigns targeting the core of modern open-source ecosystems, CI/CD platforms and cloud infrastructure.

### Supply chain attack vectors
- **Open-source registries**: npm and PyPI packages remain high-risk due to their scale and decentralized governance.
- **CI/CD platforms**: GitHub Actions and GitLab CI have become prime targets for credential theft and workflow abuse.
- **Cloud environments**: Once attackers obtain developer or CI/CD credentials, they can easily pivot into cloud platforms using legitimate API calls.

![Chart: The growth of major supply chain or third-party compromises since 2015.]

### Notable threat actors
- **Scattered Spider**: A social-engineering-driven intrusion crew that exploits help desks, identity providers and cloud access pathways.
- **LAPSUS$**: An extortion group that targets telecoms, outsourcing firms and identity providers, using MFA reset abuse and insider recruitment.
- **ShinyHunters**: A prolific data-theft collective breaching SaaS platforms and consumer services.

## Actions on objective
According to X-Force incident response data, the deployment of malware was the most observed action on objectives (41% of cases). The next most observed action was the use of legitimate tools for malicious purposes (28% of cases).

![Chart: Top actions on objectives observed in 2025 compared to 2024.]

### Ransomware landscape
The 2025 ransomware ecosystem has become highly fragmented and decentralized. We identified 109 active ransomware or extortion groups. Victim counts on ransomware leak sites increased approximately 12% year over year.

![Chart: A ransomware event on the dark web is defined as a claim made by a threat actor group that an organization has been impacted by ransomware.]

### Infostealer landscape
Well-known stealers such as Lumma, RisePro, Vidar, Stealc and Rhadamanthys remained widespread. Lumma continued to dominate the ecosystem, maintaining roughly 50% of all observed activity.

![Chart: Top 5 infostealers seen on dark web forums based on credentials for sale.]

## Blurring lines: the convergence of APT and cybercriminal techniques
The traditional distinctions between nation-state groups and cybercriminals are becoming increasingly blurred. Tactics, techniques and procedures (TTPs) from each respective group are being used by others. This blurring presents a significant challenge for security professionals, as the similarities in TTPs muddy the evidence gathered when responding to an incident.

## Impact
The distribution of cybercrime impacts reveals most attacks are driven by data-centric and credential-focused objectives.

![Chart: Top impacts X-Force observed in incident response engagements in 2025 vs. 2024.]

- **Credential harvesting (26%) and data leaks (19%)**: Indicate attackers primarily seek to gain access to sensitive systems and exfiltrate valuable information.
- **Reconnaissance (17%)**: Suggests a significant portion of activity involves preparatory stages.
- **Illicit financial gain (14%) and data theft (14%)**: Highlights ongoing monetization motives.

## Security 101: still lacking
Organizations continue to face security incidents not due to sophisticated adversary techniques, but because foundational security controls are often inconsistently implemented or poorly maintained. X-Force Red categorized the results of their penetration testing engagements into the MITRE Corporation’s Common Attack Pattern Enumeration and Classification (CAPEC) framework.

![Chart: Top 10 attack patterns discovered by X-Force Red in 2025.]

## AI in offensive cybersecurity
Artificial intelligence is a force multiplier actively used by both defenders and adversaries. What AI has changed is the speed, scale and efficiency of these attacks. Adversaries increasingly use AI to accelerate research, analyze large data sets and iterate on attack paths in real time. As multimodal AI models mature, adversaries will be able to automate increasingly complex tasks—including reconnaissance, privilege escalation and lateral movement.

## Geographic trends
- **North America (29%)**: Most affected region; focus on system control and persistence.
- **Asia-Pacific (27%)**: Nexus of global manufacturing and logistics; high reliance on exploitation of public-facing applications.
- **Europe (25%)**: Finance and insurance sector led with 39% of incidents.
- **Middle East and Africa (10%)**: Finance and energy sectors were the most-targeted industries.
- **Latin America (9%)**: Finance and insurance sector led with 47% of incidents.

![Chart: Share of incidents by geographic region in 2025 and 2024.]

## Industry trends
- **Manufacturing (27.7%)**: Top-targeted industry for the fifth year in a row.
- **Finance and insurance (27%)**: High-value target for financial data and assets.
- **Professional, business and consumer services (9%)**: High-value target due to reliance on sensitive data.
- **Energy (8%)**: Persistent target due to critical role in sustaining global operations.
- **Transportation (8%)**: Target for both financially motivated attackers and those seeking to disrupt operations.

![Chart: Share of incidents by industry in 2025 and 2024.]

## Recommendations
Cyber adversaries continue to achieve scale and impact by exploiting fundamental weaknesses in identity, access control and credential management. Organizations should:
1. **Prepare for AI‑accelerated attacks**: Security leaders need a proactive rather than reactive approach to these threats.
2. **Future-proof with AI-driven security**: Shift from a reactive, tactical response to a proactive plan, gaining a holistic view of the threat landscape.
3. **Strengthen fundamentals**: Prioritize identity security, data protection and threat detection capabilities to reduce exposure.

---

With AI Security Posture Management (AISPM), organizations can gain greater

visibility and protection for AI-powered applications across cloud environments, enabling organizations to monitor
and govern AI assets while safeguarding deployments against threats such as data poisoning and adversarial
attacks.
Shifting left should also take into account an organization’s business context—and its risk appetite. It should
prioritize securing critical assets and data by business impact, understanding adversary motivations and capabilities,
and identifying and actively managing supply‑chain and third‑party dependencies.
The recent rise of autonomous security operation centers, which use agentic AI to augment the roles of security
workers, can orchestrate multiple agents to work across the entire threat lifecycle—from threat hunting to
remediation—giving organizations the tools they need to detect and mitigate increasingly complex AI-generated
attacks.
Monitor human and non-human identities—and detect threats—with AI
For organizations, protecting identities has always posed a challenge. It’s about to get harder. As attackers fine-
tune their credential‑driven operations, IT and security leaders must turn to AI to help them gain visibility into
identity-based risks and threats across their IT landscape. By combining AI-powered identity threat detection and
response (ITDR) and identity security posture management (ISPM) services and solutions, organizations can move
more quickly and efficiently to identify vulnerabilities and prevent attacks from happening.
If it still needs saying: identity must be treated as critical
infrastructure. Security leaders who haven’t already
should elevate their identity systems to the same level of
resilience, governance and monitoring as core
infrastructure components.
If it still needs saying: identity must be treated as critical infrastructure. Given the sensitivity of AI-driven data and
agentic workflows, security leaders who haven’t already should elevate their identity systems to the same level of
resilience, governance and monitoring as core infrastructure components. They should centralize identity access
management and governance across workforce, customer, partner and machine identities.
They should also apply continuous, risk-based access controls informed by context such as user behavior,
device posture and workload characteristics. This shift will also require specialized threat-hunting capabilities, AI-
specific protections and infrastructure-level security controls to defend against increasingly sophisticated external
attacks.
Embed identity controls in application and API security

Beyond the risk of compromised credentials, the rise in vulnerabilities not requiring authentication shows the
importance of integrating identity directly into application architectures.
To secure those architectures, security teams should provide strong authentication and authorization
enforcement for public-facing and internal applications, APIs and service-to-service communications. Identity-
aware access policies should be used to limit exposure and prevent application-level exploits from escalating into
broader compromise.
Test and hunt for vulnerabilities
There’s nothing attackers like more than an overlooked or ignored vulnerability. Fortunately, security leaders
know how to handle this—by getting back to foundational, first principles. That means adopting a continuous,
proactive approach to identifying weaknesses across environments, such as looking for:
- Insecure code
- Weak or reused credentials
- Misconfigurations
- Unauthorized changes
- Insecure defaults
- Risky user behavior
- Missing patches
If an attacker does break through, here are three things that can help prevent an initial exploitation from
progressing into credential harvesting or data exfiltration: proactive remediation, strong configuration hygiene
and continuous monitoring of application behavior.
Regular penetration testing across the full technology stack—including applications, networks, cloud infrastructure,
AI models, mainframes, hardware and even personnel—is also needed to uncover vulnerabilities and
configuration gaps that could lead to unauthorized access or exposure of sensitive systems and data.
Prioritize AI platform security
AI chatbots and agentic workflows must be secured and governed with the same—or even greater—rigor as
other enterprise SaaS platforms. Too often, in the high-pressure rush to deploy, this is not what happens. That’s
a problem because the risks and threats from AI present significant challenges for organizations.

Agentic AI has introduced new risks, and amplified others. Security leaders need a comprehensive AI governance
solution to scale AI with trust and transparency, and in a way that generates value. To avoid vendor lock in, the
solution should be open, hybrid and platform-agnostic, meaning organizations can use the right model for the
right use case, and deploy their AI where it makes the most sense.
Model governance allows for evaluation of underlying AI, to test for performance, accuracy and safeguard against
inappropriate behavior. Keeping up with regulations that pertain to the use of AI is critical to maintain compliance
and reduce risk.
Organizations should assess AI adoption across the enterprise, including enforcing strong authentication and
conditional access controls, securing AI systems, protecting AI service credentials and tokens, and monitoring for
abnormal access patterns or credential exposure.
Map your footprint and track the signals that attackers watch
Security misconfigurations, data breaches, and plain old human error can lead to the public exposure of an
organization’s valued brand, domain, IP addresses or client-specific assets. This highlights the risk that resides
outside your network perimeter’s control. Security teams should work with a trusted partner to identify the
exposure of these valuable assets across the public-facing surface web, the unindexed deep web and black-
market sites on the dark web. These specialized services include monitoring capabilities for credential theft,
suspicious domains, CVEs and security bulletins.
Accelerate data security
As data and AI play an increasingly vital role in today’s digitized organizations, and across our digital economy,
security leaders must innovate and adapt at the speed of AI-driven change. To do this, they and their teams
should make sure they have the right data protection controls—such as encryption, access controls, data loss
prevention, monitoring and auditing, and secure data classification—to secure the organizational data and
manage what data is being fed into AI to prevent inadvertent exposure of sensitive data.
While data security has always been important, it gains even more importance in the AI world—discovering
where the sensitive data lives, understanding how it’s used and exposed, prioritizing data risks based on context
and using proactive controls—all while meeting the stringent compliance requirements such as GDPR, CCPA,
PCI-DSS and many more.
NEXT: About us

X-Force Threat Intelligence Index 2026
About us
IBM X-Force
IBM X-Force is a threat-centric team of hackers, responders, researchers and analysts. The X-Force portfolio
includes offensive and defensive products and services, fueled by a 360-degree view of threats.
In an age of relentless cyberattacks, a connected everything and increasing regulatory mandates, organizations
need a focused security approach. X-Force believes the threat should be the focal point. Through penetration
testing, vulnerability management and adversary simulation services, the IBM X-Force Red team of hackers
assumes the role of threat actors to find security vulnerabilities—exposing your most important assets.
Through incident preparedness, detection and response and crisis management services, the IBM X-Force
Incident Response team knows where threats may hide and how to stop them. X-Force researchers create
offensive techniques for detecting and preventing threats, while X-Force analysts collect and translate threat data
into actionable information for reducing risk.
With a deep understanding of how threat actors think, strategize and strike, X-Force can help you prevent,
detect, respond to and recover from incidents and focus on business priorities.
If your organization would like support strengthening your security posture, schedule a one-on-one briefing with
an IBM X-Force expert.
Schedule a briefing
Contributors
| Alejandro Solano   | David McMillen   | Michelle Alvarez  |
| ------------------ | ---------------- | ----------------- |
| Austin Zeizel      | Evan Babwah      | Omari Jones       |
| Benjamin Shipley   | Jeff Kuo         | Sandra Hill       |
| Christopher Caridi | Joshua Chung     | Sophie Cunningham |
| Cole Robbins       | Kaila Washington |                   |
| Colin Connor       | Kelsey Oliver    |                   |
About IBM
© Copyright IBM Corporation 2026

IBM Corporation
New Orchard Road
Armonk, NY 10504
Produced in the United States of America | February 2026
IBM, the IBM logo, IBM Security, and X-Force are trademarks or registered trademarks of International Business
Machines Corporation, in the United States and/or other countries. Other product and service names might be
trademarks of IBM or other companies. A current list of IBM trademarks is available on ibm.com/trademark.
Amazon is a trademark or registered trademark of Amazon.com, Inc. or its affiliates in the United States and
other countries.
Anthropic and Claude AI are trademarks or registered trademarks of Anthropic PBC in the United States and
other countries.
AnyDesk is a trademark or registered trademark of AnyDesk Software GmbH in Germany and other countries.
Apple is a trademark or registered trademark of Apple Inc. in the United States and other countries.
ASUS is a trademark or registered trademark of ASUSTeK Computer Inc. in Taiwan and other countries
Cisco and Duo are trademarks or registered trademarks of Cisco Systems, Inc. in the United States and other
countries.
Codecov is a trademark or registered trademark of Codecov, LLC in the United States and other countries.
ConnectWise is a trademark or registered trademark of ConnectWise, LLC in the United States and other
countries.
Docker is a trademark or registered trademark of Docker, Inc. in the United States and other countries.
Fortra GoAnywhere is a trademark or registered trademark of Fortra, LLC in the United States and other
countries.
Gainsight is a trademark of Gainsight, Inc. in the United States and other countries.
GITHUB is a registered trademark owned by GitHub, Inc. It is registered in the United States and other countries,
GitLab is a registered trademark owned by GitLab Inc.
Google and Gemini are trademarks of Google LLC.
Kaseya is a trademark or registered trademark of Kaseya Limited in the United States and other countries.

Kiteworks is a trademark or registered trademark of Kiteworks, Inc. in the United States and other countries.
LastPass is a trademark or registered trademark of GoTo Group, Inc. in the United States and other countries.
“npm” is a registered trademark of npm, Inc.
Okta is a trademark or registered trademark of Okta, Inc. in the United States and other countries.
OpenAI and ChatGPT are trademarks or registered trademarks of OpenAI OpCo, LLC in the United States and
other countries.
Oracle is a trademark or registered trademark of Oracle Corporation and/or its affiliates in the United States and
other countries.
Perplexity is a trademark of Perplexity AI, Inc.
Progress MOVEit is a trademark or registered trademark of Progress Software Corporation in the United States
and other countries.
Python and PyPI are trademarks of the Python Software Foundation in the United States and other countries.
Salesforce is a trademark or registered trademark of Salesforce, Inc.
Salesloft is a trademark or registered trademark of Salesloft, Inc.
Snowflake is a trademark or registered trademark of Snowflake Inc. in the United States and other countries.
SolarWinds is a trademark or registered trademark of SolarWinds Worldwide, LLC in the United States and other
countries.
SonicWall is a trademark or registered trademark of SonicWall Inc. in the United States and other countries.
Tyler Technologies is a trademark or registered trademark of Tyler Technologies, Inc. in the United States and
other countries.
Wipro is a trademark or registered trademark of Wipro Limited in India and other countries.
3CX is a trademark or registered trademark of 3CX Ltd. in Cyprus and other countries
This document is current as of the initial date of publication and may be changed by IBM at any time. Not all
offerings are available in every country in which IBM operates.
It is the user’s responsibility to evaluate and verify the operation of any other products or programs with IBM
products and programs. THE INFORMATION IN THIS DOCUMENT IS PROVIDED “AS IS” WITHOUT ANY

WARRANTY, EXPRESS OR IMPLIED, INCLUDING WITHOUT ANY WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND ANY WARRANTY OR CONDITION OF NON-INFRINGEMENT.
IBM products are warranted according to the terms and conditions of the agreements under which they are
provided.
Statement of Good Security Practices: No IT system or product should be considered completely secure, and no
single product, service or security measure can be completely effective in preventing improper use or access.
IBM does not warrant that any systems, products or services are immune from, or will make your enterprise
immune from, the malicious or illegal conduct of any party.
The client is responsible for ensuring compliance with laws and regulations applicable to it. IBM does not provide
legal advice or represent or warrant that its services or products will ensure that the client is in compliance with
any law or regulation.
NEXT: Appendix

X-Force Threat Intelligence Index 2026
Appendix
Table 1:
Major supply chain or third-party compromises since 2015
| Year | Incidents |     |
| ---- | --------- | --- |
2015
XcodeGhost
| 2016 | MeDoc (pre-NotPetya malicious updates) |     |
| ---- | -------------------------------------- | --- |
2017
CCleaner compromise
NotPetya via MeDoc
2018
ASUS Live Update compromise
EventStream NPM compromise
| 2019 | Wipro vendor breach |     |
| ---- | ------------------- | --- |
Docker Hub credential leak
| 2020 | SolarWinds Orion |     |
| ---- | ---------------- | --- |
Accellion FTA
Tyler Technologies
| 2021 | Kaseya VSA |     |
| ---- | ---------- | --- |
CodeCov Bash Uploader
Accellion FTA fallout
| 2022 | Okta/Sitel breach (LAPSUS) |     |
| ---- | -------------------------- | --- |
GitHub OAuth tokens
NPM/PyPI package poisoning
| 2023 | MOVEit (Clop) |     |
| ---- | ------------- | --- |
GoAnywhere MFT
3CX (Lazarus)
LastPass

2024 XZ Utils backdoor
Snowflake credential compromise
Cisco Duo/SMS provider breach
Microsoft/Midnight Blizzard OAuth theft
2025 ConnectWise ScreenConnect
AnyDesk compromise
Salesforce OAuth token compromise
Salesloft S3 exposure
Salesforce Gainsight
GitHub Action
Shai-Hulud Worm
Oracle Cloud SSO/LDAP
Sonicwall Firewall Configuration Breach
Shai-Hulud Worm 2.0
react2shell
Source: IBM X-Force. All links in table reside outside ibm.com.