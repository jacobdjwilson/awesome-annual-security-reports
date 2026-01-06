# Cybersecurity Report 2026

## About Hornetsecurity

Hornetsecurity empowers companies and organizations of all sizes to focus on their core business by protecting M365 workloads, email communications, securing data, and ensuring business continuity and compliance with next-generation cloud-based solutions.

Our flagship product, 365 Total Protection, is the most comprehensive cloud security solution for Microsoft 365 on the market and includes email security, compliance, governance, and backup.

## What is the Cybersecurity Report?

The Cybersecurity Report by Hornetsecurity is an annual analysis of the current threat landscape based on real-world data collected and studied by Hornetsecurity’s dedicated Security Lab team. Hornetsecurity processes more than 6 billion emails every month. By analyzing the threats identified in these communications, combined with a detailed knowledge of the wider threat landscape, the Security Lab reveals major security trends, threat actor campaigns, and formulates informed projections for the future of Microsoft 365 security threats, enabling businesses to act accordingly.

Findings and data from 2025 and projections for 2026 are contained within this report.

## What is the Security Lab?

The Security Lab is a division of Hornetsecurity that conducts forensic analysis of the most current and critical security threats, specializing in email security and the Microsoft 365 ecosystem. This multinational team of security specialists has extensive experience in security research, software engineering, and data science.

An in-depth understanding of the threat landscape established through hands-on examination of real-world phishing attacks, malware, ransomware gangs and more, is critical to developing effective countermeasures. The detailed insights uncovered by the Security Lab serve as the foundation for Hornetsecurity’s next-gen cyber-security solutions.

## How to Use This Report

This report contains five main sections:

*   Chapter 1 is the Executive Summary.
*   Chapter 2 focuses on the current threat landscape of the Microsoft 365 platform.
*   Chapter 3 covers current concerns and discussions regarding the biggest threats and trends from 2025.
*   Chapter 4 contains predictions from the Security Lab about cyber-security threats in 2026, along with advice and guidelines to help protect your business.
*   Chapter 5 lists all the references and supporting links used in this report.

## Table of Contents

*   [Introduction](#introduction)
*   [Chapter 1: Executive Summary](#chapter-1-executive-summary)
*   [Chapter 2: The State of Security in the Industry](#chapter-2-the-state-of-security-in-the-industry)
*   [Chapter 3: An Analysis of the Major Security Incidents and Cybersecurity News of 2025](#chapter-3-an-analysis-of-the-major-security-incidents-and-cybersecurity-news-of-2025)
*   [Chapter 4: Forecasting the Threat Landscape in 2026](#chapter-4-forecasting-the-threat-landscape-in-2026)
*   [Chapter 5: Resources](#chapter-5-resources)

---

# Introduction

## Chapter 1: Executive Summary

2025 has been a year defined by acceleration. Threat actors embraced automation, artificial intelligence, and social engineering at unprecedented speed, while defenders raced to adapt governance, resilience, and awareness programs to match. What we observed across the Hornetsecurity ecosystem, via our analysis of over 72 billion emails processed, confirms a simple truth: the attack surface is expanding faster than most organizations can secure it.

Email remains the most consistent delivery vector for cyber threats, but tactics have evolved. Malware-laden emails surged by 131% year-over-year, accompanied by a rise in scams (+34.7%) and phishing (+21%). Attackers have traded blunt-force volume for precision evasion, leveraging legitimate infrastructure, obfuscated URLs, and stealthy HTML techniques to bypass filters and human visibility alike. Meanwhile, malicious TXT and legacy DOC attachments, once considered to be largely benign or outdated, have re-emerged as primary infection vehicles, highlighting how even “low-risk” file types can no longer be ignored.

Ransomware also made an aggressive comeback in 2025. After several years of relative decline, 24% of organizations reported being victims. This is a 29% increase from the previous year. While immutable backups and improved disaster recovery planning have lowered ransom payment rates to just 13% of cases, attackers have responded by diversifying entry points and objectives. Phishing, compromised credentials, and endpoint exploitation now share equal footing as infiltration paths, and new “Ransomware 3.0” variants are beginning to focus less on encryption and more on data integrity manipulation, corrupting trust itself rather than just availability.

Artificial Intelligence has reshaped both sides of the security equation. CISOs are optimistic but cautious: 61% believe AI has directly increased ransomware risk. CISO concerns around AI are vast. They include things like phishing automation to deepfake impersonation and model poisoning. AI’s potential for misuse has become a defining feature of the threat landscape. Yet the defensive side is catching up, with 68% of organizations investing in AI-powered detection and analytics. The challenge for organizations and security teams in 2026 is governance and working towards harnessing AI’s capabilities without amplifying the risks.

The Hornetsecurity Security Lab forecasts that the coming year will see continued uncontrolled adoption of AI tools across enterprises, often faster than legal or security teams can evaluate. This, paired with the weaponization of agentic AI, will magnify existing vulnerabilities while introducing new ones that defy traditional containment models. Identity, too, remains the primary battlefield: attacker-in-the-middle kits, compromised browser extensions, and OAuth abuse show that credentials and identity continue to be the weak link in modern cloud ecosystems.

Despite this rising complexity, there are reasons for optimism. Organizations are steadily maturing. The adoption of Zero Trust principles, immutable backup technologies, and phishing-resistant MFA are becoming baseline expectations rather than aspirational goals. Security awareness, once a compliance checkbox, is increasingly embedded in company culture. The path forward is clear: resilience, not perfection, is the new metric of success. Those who treat cybersecurity as a core element of business continuity and not just an IT issue will be best positioned to thrive in 2026’s evolving threat landscape.

## Chapter 2: The State of Security in the Industry

### Email Security Trends

Email remains the backbone of business communication and, as our data shows, it also continues to be the primary battleground for attackers. 2025’s classification and threat-type shifts reveal two simultaneous realities: attackers are experimenting with new file types and low-effort delivery methods (TXT and legacy DOC surged), and at the same time social engineering remains a consistent lever for compromise.

Put simply: quantity and quality are changing. While classic spam volumes have stabilized after normalization, higher-impact categories (Malware, Scam, Phishing, etc.) are growing substantially. That combination (more dangerous content delivered at scale) increases the likelihood that even well-defended organizations will face incidents unless they adjust detection, user awareness, and recovery practices.

#### Spam, Malware, & Advanced Threat Metrics

The headline numbers are unambiguous: Malware saw the largest relative increase (+130.92%), followed by Scams (+34.70%) and Phishing (+21%). Those three categories account for the bulk of the risk that results in operational impact (data theft, encryption, business disruption). Meanwhile, categories that traditionally represented lower business risk; legitimate Messages, Transactional, and Commercial Email moved only modestly, indicating that malicious actors are concentrating effort on higher-value attack types.

Key implications:

*   **Proliferation of malicious payloads.** A 131% jump in Malware classification means more emails are carrying active payloads (or at least payload indicators) rather than simple noise. Detection strategies must assume malicious intent either way.
*   **Scams and advanced social engineering are on the rise.** Scams (+34.7%) coupled with Phishing (+21.0%) signals that attackers are refining their lures and ROI. They’re making more convincing frauds, and more customized messages, likely enabled by generative AI technologies.
*   **“Dirty Commercial” growth undermines heuristic filters.** Dirty Commercial Emails (+17.72%) suggests attackers may be weaponizing lower-quality marketing templates to evade simple content filters and blend in with legitimate marketing traffic.
*   **Targeted spear-phishing share is down, but not gone.** Suspect/Spear-Phishing is down (-9.75%), which likely reflects a shift to more automated/commodity phishing and to credential-theft approaches that bypass classic spear phishing detection. Don’t be lulled into complacency: targeted attacks remain high-impact even at lower volume.

#### Email Classification Categories

| Category                | Adjusted YoY Change (2025 vs. 2024) |
| :---------------------- | :---------------------------------- |
| Malware                 | +130.92%                            |
| Scam                    | +34.70%                             |
| Phishing                | +20.97%                             |
| Dirty Commercial Emails | +17.72%                             |
| Commercial Email        | +2.37%                              |
| Legitimate Messages     | +3.38%                              |
| Transactional           | +3.19%                              |
| Spam                    | +0.03%                              |
| Social                  | -8.05%                              |
| Suspect / Spear Phishing| -9.75%                              |
| Pro Commercial Emails   | -13.73%                             |
| Bounce                  | -18.69%                             |

*Note: Calculations take into account and adjust for sample size changes from year to year.*

#### Category Classification Descriptions

*   **Spam**: Unsolicited bulk email messages sent to a large number of recipients, typically for advertising or malicious purposes.
*   **Phishing**: Fraudulent emails designed to trick recipients into revealing sensitive information such as passwords, credit card numbers, or personal data.
*   **Commercial Email**: Legitimate marketing or promotional emails sent by businesses to customers or prospects, often for product announcements or offers.
*   **Legitimate Messages**: Authentic, non-promotional emails exchanged between individuals or organizations for normal communication purposes.
*   **Pro Commercial Emails**: Professional-grade marketing emails, often highly targeted and personalized, typically used in B2B campaigns.
*   **Transactional**: Emails triggered by user actions or system events, such as order confirmations, password resets, or account notifications.
*   **Social**: Emails originating from social media platforms, including notifications, friend requests, and activity alerts.
*   **Bounce**: Emails that fail to deliver to the recipient’s inbox due to invalid addresses, full mailboxes, or server issues.
*   **Dirty Commercial Emails**: Marketing emails that violate compliance standards or best practices, often poorly formatted or misleading.
*   **Scam**: Emails intended to defraud recipients, often involving fake offers, lottery winnings, or impersonation schemes.
*   **Malware**: Emails containing malicious attachments or links designed to install harmful software on the recipient’s device.
*   **Suspect/Spear Phishing**: Highly targeted phishing attempts aimed at specific individuals or organizations, often using personalized details to appear credible.

### Attack Techniques Used in Email Attacks 2025

The 2025 attack-technique landscape shows a clear preference for evasion-first tactics: attackers are less focused on single flashy payloads and more on slipping past filters and human suspicion. The top techniques: header forgery, subtle HTML tricks, use of legitimate hosting, and URL obfuscation are all optimized to blend malicious intent into otherwise benign-looking mail. That shift explains why we’re seeing fewer obvious spear-phish samples but more successful credential-theft and multi-stage intrusions: the email is the first step, not the punchline.

Key observations:

*   **Header and metadata manipulation dominate.** Fake From and manipulated spam-related headers top the list, demonstrating that spoofing and metadata tampering remain low-cost, high-impact methods to defeat naive filtering and trigger human trust.
*   **Abuse of legitimate infrastructure is rising.** Sending campaigns via reputable hosting or email services (e.g., cloud platforms) makes malicious mail appear to come from trustworthy sources. This is a tactic that increases deliverability and reduces immediate filter suspicion.
*   **URL obfuscation is ubiquitous.** URL shortening, non-ASCII characters, exotic TLDs (Top Level Domains), and domain fuzzing are all simple ways to hide destination intent and bypass blocklists or visual inspection.
*   **HTML/MIME tricks aim to confuse detectors, not readers.** Empty `<a>` tags, multi-part messages, and zero-(size)-font insertion are designed to mislead signature and keyword-based scanning engines while preserving readability for recipients.
*   **Automated, high-volume evasion beats small-scale targeting.** These techniques scale: attackers can roll out many campaigns that individually look benign but collectively yield credential captures, account compromise, or chained downloads.

#### Top 10 Attack Techniques Used in Email Attacks in 2025

| Rank | Technique                                     |
| :--- | :-------------------------------------------- |
| 1    | Fake From Header Alteration                   |
| 2    | Fake Spamcause Header Alteration              |
| 3    | Leverage Legit Hosting Platform to Send Campaign |
| 4    | Use of Exotic or Non-Existent TLDs            |
| 5    | URL Shortening                                |
| 6    | HTML `<a>` Tag Empty                          |
| 7    | Multi-Parted Emails                           |
| 8    | URL with Non-ASCII Characters                 |
| 9    | Random Domains / URL Fuzzing                  |
| 10   | ZeroFont Technique                            |

#### Technique Descriptions

1.  **Fake From Header Alteration**: Attackers forge the “From” header in emails to impersonate trusted senders, tricking recipients into believing the email is legitimate.
2.  **Fake Spamcause Header Alteration**: Manipulation of spam-related headers to bypass spam filters and make malicious emails appear safe.
3.  **Leverage Legit Hosting Platform to Send Campaign**: Using reputable hosting or email services (e.g., cloud platforms) to distribute phishing or malicious campaigns, making detection harder.
4.  **Use of Exotic or Non-Existent TLDs**: Employing unusual or fake top-level domains (e.g., .xyz, .club) to create deceptive URLs that look legitimate.
5.  **URL Shortening**: Using URL shorteners (e.g., bit.ly) to hide the true destination of malicious links, making them harder to detect.
6.  **HTML `<a>` Tag Empty**: Embedding empty anchor tags in HTML emails to confuse spam filters or hide malicious links.
7.  **Multi-Parted Emails**: Sending emails with multiple MIME parts (e.g., text and HTML) to evade detection by security tools.
8.  **URL with Non-ASCII Characters**: Including special or Unicode characters in URLs to create visually deceptive links (e.g., homoglyph attacks).
9.  **Random Domains / URL Fuzzing**: Generating random or slightly altered domains to bypass domain-based filtering and detection systems.
10. **ZeroFont Technique**: Inserting zero-size font text in emails to manipulate keyword-based filters while keeping the message readable to humans.

### Attachment Use and Types in Attacks

Attachment trends in 2025 demonstrate a pronounced pivot in malware delivery strategy. The fastest-growing file carriers are TXT (+181.39%) and DOC (+118.25%), with ZIP and modern Office formats (DOCX, XLSX) also present but growing more modestly. Legacy or once-popular vectors (HTML, RAR, HTM, XLS) declined, while ICS and SHTML appear as new entries to our top-ten list. This is a sign attackers are searching for overlooked or under-inspected file types plus calendar files or server-side include vectors.

Key takeaways:

*   **TXT and legacy DOC are alarm bells.** TXT files, which are widely treated as “low risk”, are being weaponized as staging artifacts (containing obfuscated URLs or scripts). Legacy DOCs (with macro support) remain attractive because many environments still allow or fail to inspect office macros aggressively.
*   **Archives STILL matter.** ZIP (+29.82%) remains a vehicle for payload bundling and evasion; compressed archives continue to be a reliable attacker tactic.
*   **Emergence of ICS and SHTML is noteworthy.** Calendar invites (ICS) and server-include variants (SHTML) represent non-traditional vectors that can bypass some mail filters and user expectations. This is especially true for recipients who accept calendar items or preview HTML content.
*   **Decline in HTML/HTM/RAR/XLS likely reflects defensive hardening, but attackers are redirecting to less-monitored channels rather than abandoning email as a vector.**

#### File-Types for Malicious Payloads 2025

| File Type | Adjusted YoY Change (2025 vs. 2024) |
| :-------- | :---------------------------------- |
| TXT       | +181.39%                            |
| DOC       | +118.25%                            |
| ZIP       | +29.82%                             |
| DOCX      | +11.69%                             |
| XLSX      | +7.85%                              |
| PDF       | -3.32%                              |
| HTML      | -27.44%                             |
| RAR       | -36.93%                             |
| HTM       | Dropped from top 10                 |
| XLS       | Dropped from top 10                 |
| ICS       | New Entry to list in 2025           |
| SHTML     | New Entry to list in 2025           |

*Note: Calculations take into account and adjust for sample size changes from year to year.*

#### File Type Definitions

*   **PDF**: Portable Document Format – Commonly used for documents; attackers often embed malicious links or scripts within PDFs.
*   **DOC**: Microsoft Word Document (Legacy) – Older Word file format; can contain macros that execute harmful code.
*   **DOCX**: Microsoft Word Document (Modern) – Current Word format; supports embedded macros and scripts that can be exploited.
*   **XLS**: Microsoft Excel Spreadsheet (Legacy) – Older Excel format; often targeted for macro-based attacks.
*   **XLSX**: Microsoft Excel Spreadsheet (Modern) – Current Excel format; can include malicious macros or links.
*   **TXT**: Plain Text File – Simple text files; attackers may use them to deliver phishing content or scripts disguised as text.
*   **HTML**: HyperText Markup Language File – Web page format; often used in phishing emails with embedded malicious links.
*   **HTM**: HyperText Markup Language File (Variant) – The legacy file extension for HTML files; used for web content and phishing payloads.
*   **SHTML**: Secure HTML File – HTML variant supporting server-side includes; can be exploited for malicious redirects.
*   **ZIP**: Compressed Archive File – Commonly used to bundle files; attackers hide malware inside compressed archives.
*   **RAR**: Compressed Archive File (Alternative) – Similar to ZIP but uses different compression algorithm; often used for malware delivery.
*   **ICS**: Calendar File – iCalendar format; attackers use malicious calendar invites to deliver phishing links or payloads.

### The Ransomware Resurgence of 2025

After three consecutive years of decline, ransomware has returned to the forefront of cybersecurity concerns. Hornetsecurity data shows that in 2025, 24% of organizations reported being victims of a ransomware attack, up sharply from 18.6% in 2024. This reversal shows a flashing red light in the post-pandemic threat landscape and a warning that attackers are evolving with increasing speed.

Despite years of awareness campaigns and training programs, ransomware remains a critical business risk precisely because it adapts to our defenses. Threat actors are now combining AI-enhanced automation with tried-and-true social engineering to achieve greater reach, precision, and persistence.

#### Automation, AI, and the New Ransomware Playbook

Attackers are increasingly leveraging generative AI and automation to identify vulnerabilities, craft more convincing phishing lures, and orchestrate multi-stage intrusions with minimal human oversight. This sadly makes ransomware operations more scalable, and more personal.

Some key data points:

*   61% of CISOs believe that AI has directly increased the risk of ransomware attacks.
*   77% identify AI-generated phishing as an emerging and serious threat.
*   68% are now investing in AI-powered detection and protection capabilities.

The result is an arms race where both sides are using machine learning. For one side the goal is to deceive, the other to defend.

#### Entry Points: Phishing Loses Ground, Endpoints Rise

| Vector                | 2024    | 2025    | Δ      |
| :-------------------- | :------ | :------ | :----- |
| Phishing/Email-based  | 52.3 %  | 46 %    | -6.3 pp|
| Compromised Credentials | ~20 %   | ~25 %   | +5 pp  |
| Exploited Vulnerabilities | –       | 12 %    | n/a    |
| Endpoint Compromise   | –       | 26 %    | n/a    |

*pp = “Percentage Point”*

The data shows a clear pivot toward credential theft and endpoint compromise, particularly in hybrid and remote work environments where BYOD and patch gaps remain widespread. Ransomware is no longer just an email problem; it’s an ecosystem problem.

#### Training Fatigue and the “False Compliance” Trap

Organizations are still investing heavily in awareness training. 74% offer it but 42% of those feel it’s inadequate.

Many programs remain checkbox exercises: annual, unengaging, and quickly forgotten. The result is what Hornetsecurity terms “false compliance”. This is the illusion of preparedness without meaningful behavioral change.

#### Recovery and Resilience: The Silver Lining

That said, even as attacks increase, recovery capabilities are quietly improving:

*   62% of organizations now use immutable backup technologies. These are systems where data cannot be altered or encrypted once the data is written. Not even by administrators or a compromised admin account during an attack.
*   82% have implemented a Disaster Recovery Plan, which is quickly becoming the new baseline for operational resilience.
*   Also in good news, only 13% of victims paid the ransom in 2025, down from 16.3% in 2024.

The message is clear: organizations are learning to recover without negotiating.

Insurance, however, tells a different story. Ransomware insurance coverage dropped from 54.6% in 2024 to 46% this year, as premiums and exclusions rose and confidence in payouts declined. This market correction suggests that organizations can no longer outsource risk. They must architect security into their systems and build resilience into their culture.

#### Outlook: Resilience is Rising, But So Are the Threats

The 2025 data paints a nuanced picture: ransomware attacks are increasing, but so is our capacity to recover. The organizations that will weather this new wave are those that treat resilience as strategy, not compliance. Immutable backups, well-tested recovery plans, and meaningful user training are no longer optional, they’re the minimum viable defense.

Attackers don’t stand still, and neither can defenders. The challenge for 2026 won’t be preventing ransomware altogether, it will be making sure that when it hits, business continuity doesn’t fail.

#### Adoption: Rapid Growth, Uneven Governance

Small and mid-sized businesses (SMBs) are hit hardest. Many operate with minimal IT staffing and outdated infrastructure, relying on outsourced providers or unpatched cloud tenants. While more SMBs report having a DR plan, readiness on paper doesn’t always translate into resilience in practice.

#### Governance: Strategy Still Lags Behind Threat Reality

Cybersecurity is now a board-level concern, but many organizations are still catching up to the operational demands of ransomware-era governance. Few boards run cyber crisis simulations, and cross-functional playbooks remain the exception rather than the rule. As AI-driven misinformation and deepfake extortion become more plausible, communication readiness is now part of cybersecurity and, thankfully, not a PR afterthought.

### CISO Perspectives: Balancing AI Promise and Peril

Artificial Intelligence is reshaping cybersecurity, and not just as a defensive tool, but as a strategic question. Hornetsecurity’s 2025 CISO Insights Poll set out to capture how real-world security leaders are approaching AI: where it’s working, where it’s risky, and what challenges stand in the way of responsible adoption.

The findings reveal a complex picture. CISOs are enthusiastic, cautious, and in many cases, still experimenting. AI is everywhere but trust, governance, and understanding have, sadly, not yet caught up.

Most CISOs surveyed report significant experimentation with AI, but structured adoption remains rare. Some organizations are integrating AI into workflows such as triage, enrichment, and ticket management, while others restrict its use entirely.

A CISO from a global finance firm noted, “We’re seeing adoption as high as 75%+ within our organization over the last two years.” In contrast, a virtual CISO remarked, “Two years ago it was open bar on all AI services. This past year, we’ve started putting in more processes and internal LLMs.”

The variability shows the core challenge: AI adoption is moving faster than AI governance, like previous innovative trends in the tech space. Many leaders have begun to centralize control and develop internal tools, but others remain in a reactive posture and are chasing compliance rather than leading innovation.

Shadow IT, once a known irritant, has been redefined by AI into Shadow AI. Unapproved tools, browser extensions, and SaaS integrations are creating new, opaque risks. As one CISO summarized, “AI safety concerns have amplified the dangers of shadow IT.”

As one CISO summarized, “We still lack skills and specialized experts in AI.” Another added, “Detecting a port scan by reading ten lines of logs doesn’t bring much value.”

Despite the hurdles, CISOs remain pragmatic: AI isn’t hype, it’s an inevitable evolution. But adoption will remain on a case-by-case basis until transparency, skills, and governance catch up with ambition.

#### From Curiosity to Capability

AI in cybersecurity is no longer experimental, but neither is it fully mature. Across industries, the focus is shifting from “What can AI do?” to “How do we govern it?”

The coming year will define whether security teams can transform AI from a risk into a reliable ally.

#### Emerging Threats: Deepfakes, Model Poisoning, and Data Leaks

Nearly all CISOs surveyed agree that AI misuse will be a major source of cyber risk over the next 12 months.

The most pressing concerns include:

*   Synthetic identity fraud using AI-generated documents or credentials
*   Voice cloning and deepfake videos used for impersonation and fraud
*   Model poisoning, where malicious data corrupts internal AI systems
*   Sensitive data leakage through employee misuse of public AI tools

One CISO warned, “We’re most concerned about model poisoning attacks as we run our own models in-house.” Another noted that “the number one risk of AI is the voluntary leak of company data into public systems.”

AI has become both a tool and a target and the attack surface is clearly expanding faster than many realize.

#### Security Team Adoption: Careful, Controlled, and Tactical

Within security operations, AI adoption is measured but growing. CISOs describe limited deployments focused on specific, low-risk tasks. For instance, classifying tickets or enriching threat data. One finance-sector CISO shared a practical success story: “AI turned out great for customer-facing ticket notes. They’re concise and bias-free.”

This “cautious optimism” is characteristic of 2025. Security teams are embracing automation but remain wary of overreliance on opaque systems or immature models.

#### Challenges in Implementation: The Practical Barriers

The path to responsible AI adoption is far from smooth. Our CISO poll found that the top barriers include:

*   Uncertainty around AI risks and potential misuse
*   Compliance and legal constraints
*   Budget justification and ROI demonstration
*   Integration challenges with legacy tools
*   Talent shortages in AI and data science
*   Leadership buy-in

#### End-User Awareness: The New Human Risk Factor

If a company is only as strong as its least prepared employee, AI has lowered that bar. CISOs unanimously agree that end-user awareness of AI risk is dangerously low. While a few organizations boast strong compliance cultures with some scoring themselves “5 out of 5”, most CISOs estimate awareness levels closer to “1 or 2 out of 5.”

The primary issue? Employees enthusiastically using public AI tools without realizing the security or compliance implications. As one virtual CISO put it, “People haven’t understood the stakes, especially when they share company information in a public AI.”

The consensus: security awareness efforts in-house haven’t evolved at the same pace as AI adoption. Focused, scenario-based education is now as important as firewalls and filters.

#### Leadership Understanding: The Awareness Gap at the Top

CISOs also highlight a wide disparity in leadership understanding of AI-related risks. Our polling revealed the broadest spread of responses across this question, ranging from “deep awareness” to “no real understanding.” The median answer was a luke-warm “leadership somewhat knows the risks”. It’s clear that progress is inconsistent and varies widely from business to business.

Some organizations are moving forward collaboratively. A German tech-sector CISO credited joint Legal and Security initiatives for progress: “Management is beginning to understand the issues related to AI security.” Others, however, report the opposite. “Management sees the productivity gains but not the risks,” one virtual CISO said.

This uneven awareness leaves CISOs with dual responsibility: defending against external threats while educating leadership internally.

---

## Chapter 3: An Analysis of the Major Security Incidents and Cybersecurity News of 2025

It’s important to use major cybersecurity incidents that organizations suffer as a learning tool, looking at how your business would have handled a similar attack, and how to improve your resiliency going forward. There’s been no shortage of examples since our late 2024 report, here are the top eleven we picked.

### October 2024 – Internet Archive Breach and DDoS Attack

In early October 2024, the non-profit Internet Archive (known for the Wayback Machine) suffered a significant data breach affecting over 31 million user accounts. Attackers gained access to a 6.4 GB database containing users’ email addresses, usernames, and Bcrypt-hashed passwords, among other details. Around the same time, a hacktivist group dubbed BlackMeta launched a series of distributed denial-of-service (DDoS) attacks against the Archive’s websites, temporarily knocking them offline. This incident highlighted vulnerabilities in the Archive’s configuration management (an exposed GitLab configuration file was reportedly the attack vector).

There are two takeaways from this one. Even if you’re a not-for-profit or “too insignificant to be vulnerable”, you’re always a target. Additionally you should always check your developer’s configuration of their code repositories as sufficient MISconfiguration could negatively impact you down the road.

### December 2024 – U.S. Treasury Hack by Chinese APT

In late December 2024, the U.S. Department of the Treasury disclosed it had been the victim of a state-sponsored cyberattack attributed to the Chinese government. Attackers linked to a Chinese APT (Advanced Persistent Threat) group exploited a supply-chain weakness by compromising an identity and remote support platform from BeyondTrust, a vendor used by the Treasury. By obtaining a BeyondTrust admin key, the hackers were able to remotely access multiple Treasury employees’ workstations and steal unclassified documents. Treasury officials labelled it a “major cybersecurity incident” and notified U.S. cybersecurity authorities (CISA) on December 8, 2024, soon after BeyondTrust alerted them to the intrusion. The breach, coming on the heels of other China-linked attacks on U.S. targets, heightened tensions and prompted urgent reviews of third-party access security and government cyber defenses.

The main lesson here is understanding your threat model, and dependency risks. If you have implemented a security solution, where’s the “master key” for that security solution? What happens if it’s compromised, and how do you detect that before it’s too late?

### January 2025 – Critical VPN Zero Day Exploits (Ivanti & SonicWall)

January 2025 saw attackers actively exploiting critical zero-day vulnerabilities in two popular enterprise remote access products, prompting emergency security alerts worldwide. Ivanti (Pulse Secure) disclosed that its Connect Secure VPN appliance contained a critical authentication bypass flaw that was being exploited in the wild. This zero-day, which allowed remote code execution without login, was used to infiltrate at least 17 organizations (including Nominet, the U.K. domain registry) as early as December 2024. Mandiant researchers linked the Ivanti VPN exploits to a China-based threat actor, given the tools and malware used.

Around the same time, SonicWall warned that a zero-day in its Secure Mobile Access (SMA) 1000 series VPN was similarly exploited by attackers. Microsoft and CISA confirmed that the SonicWall flaw – also allowing unauthenticated remote code execution – had been used in attacks, with incidents later in July as well. These back-to-back VPN security failures revealed the alarming potential for adversaries to abuse trusted remote access systems, leading organizations worldwide to rush out critical patches and mitigations.

These are but two examples of a trend over the last few years, where the very technology you’ve deployed to protect your network (firewalls, VPN appliances) are so poorly architected and maintained that they instead serve as an easy access point for attackers into your environment. No matter the size of your vendor, you must demand better from them. Procuring security tech to protect you that makes you more vulnerable just isn’t acceptable.

### March 2025 – Juniper Networks Router Espionage Campaign

In March 2025, cybersecurity firm Mandiant revealed an ongoing espionage campaign targeting network infrastructure. A China-nexus APT group (UNC3886) had been exploiting a newly discovered vulnerability in Juniper Networks’ Junos OS, the operating system for Juniper routers. Starting in mid-2024, the attackers used this zero-day to gain access to enterprise and possibly government routers, then implanted custom backdoor malware on the devices. These stealthy backdoors allowed the hackers to monitor network traffic, and they potentially pivoted further into networks without detection. Juniper patched the flaw once it was discovered, but the incident drew comparisons to past supply chain and infrastructure attacks. It underscored that advanced threat actors are now directly targeting network routers and firewalls to conduct long-term espionage, bypassing traditional endpoint security.

This incident is something you can take directly to your networking team. Routers and switches are part of the “plumbing” of your infrastructure and once deployed tend to be mostly forgotten as long as they work. This also makes them a great place for attackers to hide, particularly as you can’t run Endpoint Detection and Response (EDR) on them, so make sure to monitor them for configuration changes, and keep them patched.

### June 2025 – UNFI Ransomware Attack Disrupts Food Supply Chain

In June 2025, a ransomware attack on United Natural Foods, Inc. (UNFI), a leading food distribution company, demonstrated the real-world impact of cyberattacks on supply chains. UNFI, known as the primary distributor for Whole Foods and other grocers, detected unauthorized activity on its IT systems on June 5. To contain the threat, the company took affected systems offline, which temporarily crippled its ability to process orders and make deliveries. As a result, some grocery retailers experienced product shortages and delivery delays. The disruption continued for multiple days, and UNFI stated that the incident would cause ongoing operational delays and additional costs. The food supply chain impact garnered attention from regulators and highlighted the need for stronger cyber defenses in distribution and manufacturing sectors, as even brief outages can have cascading effects on consumers.

If your business provides a service that’s part of larger mesh of companies where an interruption can cause a cascading effect, reaching the public or critical infrastructure, your risk modeling must include this, not only the immediate effect a cyber-attack can have on your own operations. Because in the public’s eye (and regulators’ view), you’ll be held responsible for those wider impacts.

### July 2025 – Scattered Spider Hacks (Airlines and Retail – Qantas Breach)

In some reporting of various incidents over the last few years, “Scattered Spider” has been called a hacking group. This isn’t quite accurate, as it’s more a loose affiliation of many different actors, with similar tactics, thus it’s more accurate to refer to “Scattered Spider-like” techniques. Their approach relies heavily on social engineering, tricking (often outsourced) helpdesk staff to reset credentials. It’s less about hacking computers, and more about hacking people. Another notable difference compared to many other threat actors is that they are young, they live in western countries and are native English speakers, predictably leading to many of them being arrested over the last year or two.

Earlier in 2025, Scattered Spider had been linked to attacks on major British retailers (Marks & Spencer, Co-op, Harrods) and insurance firms like Aflac. In July 2025, the group turned its attention to the aviation sector. Qantas Airways, Australia’s flag carrier, announced that a third-party contact