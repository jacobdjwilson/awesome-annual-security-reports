# Global Threat Intelligence Report H2 2024

## Table of Contents
- [Introduction](#introduction)
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [The Threat Landscape](#the-threat-landscape)
    - [The Threat Landscape in Charts](#the-threat-landscape-in-charts)
    - [Top Threats and Campaigns](#top-threats-and-campaigns)
    - [Mimecast Risk Radar](#mimecast-risk-radar)
    - [Major Event Timeline](#major-event-timeline)
- [Recommendations](#recommendations)
    - [Threat-Specific Countermeasures](#threat-specific-countermeasures)
    - [Best Practices and Advisories](#best-practices-and-advisories)
    - [Steps Specific to Mimecast Clients](#steps-specific-to-mimecast-clients)
- [Conclusion](#conclusion)

---

## Introduction

Strong threat intelligence has become critical for companies and organizations to defend against attackers’ increasing agility. Organizations of every size should educate themselves on the latest trends, track the threats targeting their industry and suppliers, and harden defenses and update their processes to prevent their business communications and people from being used against them.

In the second half of 2024, Mimecast processed more than 90 billion data points for its over 42,000 customers, flagging more than 5 billion threats during the six-month period. The total number of protected interactions greatly exceeded that by many multiples. Email and collaboration tools continue to be the channels through which most attackers start their effort to compromise targeted organizations, allowing Mimecast to detect and analyze many threats before they become widely known.

In our H2 2024 Global Threat Intelligence report, Mimecast has accumulated data from our systems protecting tens of millions of users, provided insights from our intelligence analysts, and added open-source intelligence on the latest threats. The report includes analysis of threat activity, statistics revealing attack trends, and a series of recommendations for small businesses and large enterprises to protect their employees and mitigate the impact of risky users.

We invite you to explore our H2 2024 threat intelligence report and look forward to sharing more insights in the future.

![In the second half of 2024, Mimecast processed more than 90 billion data points for its nearly 43,000 customers, flagging more than 5 billion threats during the six-month period.]

---

## Executive Summary

IN THE SECOND HALF OF 2024, THREAT ACTORS INCREASINGLY USED LEGITIMATE SERVICES AS A WAY TO OBSCURE THEIR ATTACKS AND ATTEMPT TO EVADE DEFENSES.

The trend of living off trusted services (LOTS) means that businesses will have to rely on more than just reputation and authentication systems to protect themselves from messaging and human-centered attacks. In addition, threat actors are exploiting third-party suppliers — whether a service provider or a software product — to more easily slip into a targeted network.

GEOPOLITICS HAVE GIVEN THREAT ACTORS BOTH MOTIVE FOR MORE FREQUENT ATTEMPTED COMPROMISES AND A FERTILE SUPPLY OF SUBJECT MATTER WITH WHICH TO CRAFT ATTACKS.

Nation-state actors continued to resort to cyberattacks and cyber-espionage to pursue deniable actions against their rivals. China compromised US and Canadian[^1] infrastructure, Iran and Israel each targeted the other nation’s infrastructure[^2], and Russia continued to target European and US organizations[^3] after its invasion of Ukraine stalled.

AI TECHNOLOGIES CONTINUE TO OFFER UNIQUE BENEFITS TO BOTH DEFENDERS AND ATTACKERS.

Cybersecurity analysts can more quickly analyze potential security events with the help of AI assistants, while incident responders can use AI to block and remediate an attack more quickly and completely. Attackers are benefiting as well: Mimecast research[^4] using linguistic analysis found that about 12% of emails — including phishing attacks — showed signs of being written by large language models (LLM). Deepfake audio and video have been effectively used to imitate CEOs and instruct employees to make fraudulent payments into cybercriminal accounts.

ALL THESE TRENDS WILL CONTINUE IN 2025.

The number of attacks that used the cloud to some degree more than doubled in 2024, while geopolitics continues to become more chaotic with France and Germany both facing elections in Europe, U.S. President Donald Trump seated for a second, non-consecutive term, and Russia and China continuing to flex their militaries on the world stage. Both security researchers and attackers are pioneering new ways to exploit AI systems, either taking advantage of security weaknesses or augmenting their own attack strategies.

[^1]: Tunney, Catharine. “China ‘compromised’ Canadian government networks and stole valuable info: spy agency.” CBC. 30 October 2024. https://www.cbc.ca/news/politics/cse-cyber-threats-china-1.7367719
[^2]: Lemos, Robert. “As Geopolitical Tensions Mount, Iran’s Cyber Operations Grow.” Dark Reading. News article. 18 September 2024. https://www.darkreading.com/cyberattacks-data-breaches/geopolitical-tensions-mount-iran-cyber-operations-grow
[^3]: Eddy, Nathan. “Ukraine-Russia Cyber Battles Tip Over Into the Real World.” Dark Reading. News article. 3 October 2024. https://www.darkreading.com/cyberattacks-data-breaches/ukraine-russia-cyber-battles-tip-over-into-real-world
[^4]: Lee, Evonne. “New Mimecast Threat Intelligence: How ChatGPT Upended Email.” Mimecast Threat Intelligence Blog. 30 September 2024. https://www.mimecast.com/blog/how-chatgpt-upended-email/.

---

## Key Findings

While threat actor activity has increased across almost all metrics, some trends stand out.

### K-1: ATTACKERS ARE INCREASINGLY LIVING OFF TRUSTED SERVICES (LOTS).
Microsoft’s, Google’s, and Evernote’s cloud services commonly play hosts for threat actors’ payloads and landing pages. However, other cloud services are frequently being used for specific components of attack infrastructure: Cloudflare’s Turnstyle CAPTCHAs are regularly used to prevent threat analysis; DocuSign, TeamViewer, and Wave Compliance inadvertently host attackers’ content; and Google’s Gmail and Microsoft Outlook (formally Hotmail) are used to send phishing attacks.

### K-2: GEOPOLITICS RAISES THE LIKELIHOOD OF CYBERATTACKS.
The French and German elections, and the continued uncertainty of the Russia-Ukraine war, will raise the tension of European Union politics. The departure of U.S. government from predictable norms could also result in greater activity in the cyber domain. Business, political, and cybersecurity experts have increasingly warned that geopolitical tensions and cybersecurity risks are linked. The top two risks identified for 2025 in the annual Systemic Risk Barometer Survey conducted by the Depository Trust and Clearing Corporation were Geopolitical Risk and Cyber Risk.[^5]

### K-3: KEY EMAIL AUTHENTICATION TECHNOLOGIES HAVE INCREASED CHALLENGES FOR ATTACKERS, WHILE AI HAS LOWERED THE BAR FOR CYBERCRIME.
By using trusted services, attackers can meet the increasing authentication requirements of email technologies — such as SPF, DKIM, and DMARC — and appear to come from a trusted source. While the technologies make their attacks more complicated, the attackers continue to find services to pass authentication and alignment checks. In addition, the spread of AI chat bots allows even would-be cybercriminals to gain the skills necessary for hacking.

### K-4: MEDIA & PUBLISHING, ENTERTAINMENT & RECREATION, LEGAL SERVICES, AND THE ARTS INDUSTRIES SAW THE MOST THREATS PER USER IN H2 2024.
Most industries saw a distinctive threat profile, including a greater proportion of malicious files targeting the Arts, Entertainment & Recreation sectors, while workers in the Media & Publishing sector encountered larger number of malicious links. Impersonation attacks dominated the threat profile for the software & SaaS sector.

### K-5: HUMANS CONTINUE TO HAVE A PRIMARY ROLE IN MOST BREACHES.
Most breaches are enabled by an insider taking an action that allows attackers access to sensitive or protected resources. The 2024 version of the annual Data Breach Investigations Report (DBIR) found that more than two-thirds (68%) of breaches that occurred in 2023[^6] had “a non-malicious human element.” A 2024 survey of 1,000 employees found that a third (34%) worried that they would be the vulnerability exploited by attackers, even though the vast majority (86%) considered themselves knowledgeable about cybersecurity[^7]. More than half of respondents fear they would lose their job if they left their organization open to a cyberattack.

[^5]: “Geopolitical and Cyber Risks Remain Top Threats to the Financial Services Sector in 2025.” DTCC. 4 December 2024. https://www.dtcc.com/news/2024/december/04/geopolitical-and-cyber-risks-remain-top-threats-to-the-financial-services-sector-in-2025
[^6]: Verizon Data Breach Investigations Report, 2024. https://www.verizon.com/business/resources/reports/dbir/#takeaways
[^7]: Why AI fuels cybersecurity anxiety, particularly for younger employees. https://www.ey.com/en_us/consulting/human-risk-in-cybersecurity

---

## The Threat Landscape

### 4.1 The Threat Landscape in Charts

The threat landscape in the second half of 2024 showed increasing use of consumer and business cloud services as a way for attackers to avoid detection. As a result, several major cloud services are being used to host attackers’ content, and links continue to grow as a mechanism for delivering payloads.

#### CLOUD SERVICE ABUSE
Attackers are increasingly living off trusted services (LOTS) in their efforts to bypass defenses that rely on identifying attacks by spotting untrusted code, resources, and online services. While some choices to host attackers’ infrastructure are obvious — such as Google Docs, Evernote, and Dropbox DocSend — other online services are less well-known, such as interactive publication site Publuu, online webinar host Wave Compliance, and slide-deck presentation site Gamma.

![Chart 1: Most initial domains map to similar final domains, such as most attacks using Evernote initially, also hosting a payload there.]

#### TPUS BY ATTACK TYPE
While spam continues to account for the vast majority of messages blocked by Mimecast in H2 2024, the summer saw a surge in Unwanted email messages. While that surge abated by the end of the year, phishing attacks, which typically include a URL to an attacker-controlled site or service, saw slow growth through the half.

![Chart 2a: The significant increase in spam detections follows the integration of spam held at the gateway, as opposed to solely relying on spam rejections.]
![Chart 2b: Removing the overwhelming influence of the spam dataset shows that Phishing is on the rise, and a surge in Malware attacks late in the second half of 2024.]

#### TOP TARGETED INDUSTRIES BY TPUS
Every industry encounters a significant volume of spam as well as threats that are detected because of the attackers’ use of low-reputation infrastructure. As part of the analysis, Mimecast removed bulk email messages — detected as Spam or Low Reputation — which accounted for 17 TPUs and 5 TPUs, respectively.

![Chart 3: The threat profile for the Top-10 industries, without the Spam and Low Reputation categories.]

#### THREAT GROUPS
Attributing cyber threats is inherently complex, especially with the blended tactics many threat actors employ and the rise of cybercrime-as-a-service models. Mimecast focuses on analyzing Tactics, Techniques, and Procedures (TTPs) to categorize and reference threat operations systematically.

#### TOP VULNERABILITIES OVER TIME
While the vast majority of attacks attempting to exploit software issues focused on two popular vulnerabilities (CVE-2017-0199 and CVE-2022-42889), attackers attempted to exploit 89 different issues in the second half of 2024.

![Chart 5: The Top 10 vulnerabilities detected in messages, compared by EPSS and CVSS scores.]

---

### 4.2 Top Threats and Campaigns

1. **OPEN SPOOFING**: Compromised consumer routers proxying spoofed phishing emails through ISP services.
2. **COPYRIGHT INFRINGEMENT/SUBSCRIPTION NOTIFICATION**: Impersonating law firms with copyright notice bait for info stealing.
3. **USER LINK COPY AND PASTE - ACCOUNT PAYABLE SCAM**: Convincing users to copy and paste a link to evade defenses.
4. **TARGETED BEC SCAM WITH AUDIO DEEPFAKE**: Audio deepfake, business email compromise (BEC).
5. **MISSING A DELIVERY**: Living off trusted services (LOTS) using S3 buckets on AWS to host HTML files.
6. **FACEBOOK ACCOUNT TAKEOVER — BRAND IMPERSONATION**: Job lure impersonating brands such as Victoria’s Secret, Red Bull and Coca-Cola.

---

### 4.3 Mimecast Risk Radar

**ATTACKERS INCREASINGLY LIVE OFF TRUSTED SERVICES (LOTS)**
From legitimate email providers to file-sharing sites to webinar-hosting services, attackers have extended their use of trusted services to bypass defenses that rely on reputation and trust.

**GEOPOLITICAL RISKS RISE**
As geopolitical tensions rise worldwide, the threat landscape is changing. Cyber attackers have become more active, using the cyber domain for intelligence collection, compromising rival nations’ assets, and generating income.

![Figure 1: Since mid-year 2022, through the end of 2024, CISA has added about 4 vulnerabilities per week to the KEV catalog.]

---

### 4.4 Major Event Timeline

- **July**: 10 Billion Passwords Leaked (RockYou2024).
- **Sept**: Asian Cryptocurrency Exchanges hit with thefts; Internet Archive breached.
- **Oct**: Salt Typhoon worries grow (Chinese state-sponsored infiltration of U.S. telecommunications).
- **Nov**: Iranian “Fake Workers” target sensitive industries; Cyber resilience enhancement (CISA Red Team insights).
- **Dec**: U.S. Treasury hacked through third party; Phished developers allow browser extension compromise.

---

## Recommendations

### 5.1 Threat-Specific Countermeasures

- **Human Risk Management**: Implement a framework that aligns security objectives with business goals.
- **Provide Awareness Training**: Educate staff on how global events influence phishing and social engineering.
- **Mandate More Security from Third Parties**: Review service-level agreements to set minimum security standards.
- **Block Images in Email Messages**: Configure email clients to prevent the loading of images.
- **Scan Environment for Misconfigurations**: Use tools like Cloud Security Posture Management to identify open ports.
- **Segment the Network and Log Internal Traffic**: Reduce lateral movement by isolating critical assets.
- **Harden User Credentials, Deploy MFA**: Enforce robust passwords and multifactor authentication.

### 5.2 Best Practices and Advisories

- **APT40 Advisory**: Tactics used by Chinese state-sponsored threat actor APT40.
- **Detecting and Mitigating Active Directory Compromises**: 17 techniques for attacking Microsoft Active Directory.
- **Russian Military Cyber Actors**: Targeting U.S. and global critical infrastructure with WhisperGate.
- **2023 Top Routinely Exploited Vulnerabilities**: Information on the top 15 vulnerabilities from 2023.
- **IRGC-Affiliated Cyber Actors**: Attacks on programmable logic controllers in water and wastewater systems.

### 5.3 Steps Specific to Mimecast Clients

- **Email Security Cloud Gateway**: Use SSO/MFA, optimize Impersonation Protection, implement Advanced BEC Protection, and utilize SIEM/XDR integrations.
- **Email Security Cloud Integrated**: Enable Browser Isolation, customize Allow/Block rules, and review weekly reports.

---

## Conclusion

In the latter half of 2024, threat analysis revealed an intensification of sophisticated disinformation campaigns and coordinated hacktivist operations. The identification of malicious activity has become technically complex due to adversaries blending malicious actions with legitimate operations. Organizations require dedicated incident response capabilities, including advanced forensic tooling, network analysis systems, and automated detection mechanisms. Perimeter security remains a critical concern, with threat actors consistently exploiting vulnerabilities in edge infrastructure.