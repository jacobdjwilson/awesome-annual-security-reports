# Zscaler ThreatLabz 2024 AI Security Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [Key GenAI and ML Usage Trends](#key-genai-and-ml-usage-trends)
  - [AI transactions continue to accelerate](#ai-transactions-continue-to-accelerate)
  - [Enterprises are blocking more AI transactions than ever](#enterprises-are-blocking-more-ai-transactions-than-ever)
  - [Industry AI breakdown](#industry-ai-breakdown)
  - [Healthcare and AI](#healthcare-and-ai)
  - [Finance](#finance)
  - [Government](#government)
  - [Manufacturing](#manufacturing)
  - [Education and AI](#education-and-ai)
  - [ChatGPT usage trends](#chatgpt-usage-trends)
  - [AI usage by country](#ai-usage-by-country)
  - [Regional breakdown: EMEA](#regional-breakdown-emea)
  - [Regional breakdown: APAC](#regional-breakdown-apac)
- [Enterprise AI Risk and Real-World Threat Scenarios](#enterprise-ai-risk-and-real-world-threat-scenarios)
  - [Enabling AI in the enterprise: top 3 risks](#enabling-ai-in-the-enterprise-top-3-risks)
  - [AI-driven threat scenarios](#ai-driven-threat-scenarios)
  - [AI impersonation: deepfakes, misinformation, and more](#ai-impersonation-deepfakes-misinformation-and-more)
  - [AI-generated phishing campaigns](#ai-generated-phishing-campaigns)
  - [Dark chatbots: uncovering WormGPT and FraudGPT on the dark web](#dark-chatbots-uncovering-wormgpt-and-fraudgpt-on-the-dark-web)
  - [AI-driven malware and ransomware across the attack chain](#ai-driven-malware-and-ransomware-across-the-attack-chain)
  - [AI worm attacks and “viral” AI jailbreaking](#ai-worm-attacks-and-viral-ai-jailbreaking)
  - [AI and US elections](#ai-and-us-elections)
- [All Eyes on AI Regulations](#all-eyes-on-ai-regulations)
  - [United States](#united-states)
  - [European Union](#european-union)
- [AI Threat Predictions](#ai-threat-predictions)

---

## Executive Summary

AI is more than a pioneering innovation—it’s now business as usual. As generative AI tools like ChatGPT transform business in large and small ways, AI is being woven deep into the fabric of enterprise life. However, questions about how to securely adopt these AI tools while defending against AI-driven threats are not settled.

Enterprises are rapidly adopting AI and ML tools across departments like engineering, IT, marketing, finance, customer success, and more. Yet, they must balance the numerous risks that come with AI tools to reap their fullest rewards. Indeed, to unlock the transformative potential of AI, enterprises must enable secure controls to protect their data, prevent the leakage of sensitive information, mitigate ‘Shadow AI’ sprawl, and ensure the quality of AI data.

Drawing on more than 18 billion transactions from April 2023 to January 2024 across the Zscaler Zero Trust Exchange™, ThreatLabz analyzed how enterprises are using AI and ML tools today. These insights reveal key trends across business sectors and geographies in how enterprises are adapting to the shifting AI landscape and securing their AI tools.

These AI risks to enterprises are bidirectional: outside enterprise walls, AI has become a driving force for cyberthreats. Indeed, AI tools are allowing cybercriminals and nation state-sponsored threat actors to launch sophisticated attacks, more quickly, and at greater scale. Despite this, AI holds promise as a key piece of the cyber defense puzzle as enterprises grapple with a dynamic threat landscape.

Throughout, you’ll find insights into top-of-mind AI topics including business risk, AI-driven threat scenarios and adversary tactics, regulatory considerations, and predictions for the AI landscape in 2024 and beyond.

Just as critically, this report offers best practices on two fronts: how enterprises can securely embrace generative AI transformation while protecting critical data, and how AI-powered tools are working to deliver layered, zero trust security to face the new landscape of AI-driven threats.

The ThreatLabz 2024 AI Security Report offers key insights into these critical AI challenges and opportunities.

---

## Key Findings

- AI/ML tool usage skyrocketed by 594.82%, rising from 521 million AI/ML-driven transactions in April 2023 to 3.1 billion monthly by January 2024.
- Enterprises are blocking 18.5% of all AI/ML transactions—a 577% increase in blocked transactions over nine months—reflecting growing concerns around AI data security and companies’ reluctance to establish AI policies.
- The most widely used AI applications by transaction volume are ChatGPT, Drift, OpenAI*, Writer, and LivePerson. The top three blocked applications by transaction volume are ChatGPT, OpenAI, and Fraud.net.
- The top 5 countries generating the most AI and ML transactions are the US, India, the UK, Australia, and Japan.
- Manufacturing generates the most AI traffic with 20.9% of all AI/ML transactions in the Zscaler cloud, followed by Finance and Insurance (19.9%) and Services (16.8%).
- Enterprises are sending significant volumes of data to AI tools, with a total of 569 TB exchanged between AI/ML applications between September 2023 and January 2024.
- ChatGPT usage continues to soar, with 634.1% growth, even though it is also the most-blocked AI application by enterprises, based on Zscaler cloud insights.
- AI is empowering threat actors in unprecedented ways, including for AI-driven phishing campaigns, deepfakes and social engineering attacks, polymorphic ransomware, enterprise attack surface discovery, automated exploit generation, and more.

*NOTE: The Zscaler Zero Trust Exchange tracks ChatGPT transactions independently from other OpenAI transactions at large.*

---

## Key GenAI and ML Usage Trends

![Graph showing AI and ML transaction trends from April 2023 to January 2024]

### AI transactions continue to accelerate

From April 2023 to January 2024, enterprise AI and ML transactions grew by nearly 600%, rising to more than 3 billion monthly transactions across the Zero Trust Exchange in January. This underscores the fact that, despite a rising number of security incidents and data risks associated with enterprise AI adoption, its transformative potential is too great to ignore. Note that while AI transactions saw a brief lull over the December holidays, transactions continued at an even greater pace at the start of 2024.

Even as AI applications proliferate, however, the majority of AI transactions are being driven by a relatively small set of market-leading AI tools. Overall, ChatGPT accounts for more than half of all AI and ML transactions, while the OpenAI application itself comes in third place, with 7.82% of all transactions. Meanwhile, Drift, the popular AI-powered chatbot, generated nearly one-fifth of enterprise AI traffic (the LivePerson and BoldChat Enterprise chatbots also breached the top apps in spots 5 and 6). Meanwhile, Writer remains a favored generative AI tool in the creation of written enterprise content, such as marketing materials. Finally, Otter, an AI transcription tool often used in video calls, drives a significant portion of AI traffic.

![Chart showing top AI applications by transaction volume]

### Enterprises are blocking more AI transactions than ever

Even as enterprise AI adoption continues to surge, organizations are increasingly blocking AI and ML transactions because of data and security concerns. Today, enterprises block 18.5% of all AI transactions, a 577% increase from April to January, for a total of more than 2.6 billion blocked transactions.

Some of the most popular AI tools are also the most blocked. Indeed, ChatGPT holds the distinction of being both the most-used and most-blocked AI application. This indicates that despite—or even because of—the popularity of these tools, enterprises are working actively to secure their use against data loss and privacy concerns. Another notable trend is that bing.com, which has an AI-enabled Copilot functionality, is blocked from April to January. In fact, bing.com accounts for 25.02% of all blocked AI and ML domain transactions.

---

## Enterprise AI Risk and Real-World Threat Scenarios

### Enabling AI in the enterprise: top 3 risks

1. **Protecting intellectual property and non-public information**: Generative AI tools can lead to inadvertent leakage of sensitive and confidential data. Sensitive data disclosure is number six on the OWASP Top Ten for AI Applications.
2. **Data privacy and security risks of AI applications**: As the number of AI applications grows, enterprises must consider that terms and conditions vary. Some tools use queries to train models, while others may sell data to third parties.
3. **Data quality concerns: garbage in, garbage out**: The quality of data used to train AI is tied to the trustworthiness of outputs. Enterprises must be aware of "data poisoning," where training data is contaminated.

### AI-driven threat scenarios

#### AI impersonation: deepfakes, misinformation, and more
The era of AI-generated videos, live avatars, and voice impersonations that are near-indistinguishable from reality has arrived. In 2023, Zscaler thwarted an AI vishing and smishing scenario where threat actors impersonated the voice of Zscaler CEO Jay Chaudhry in WhatsApp messages.

#### AI-generated phishing campaigns
Threat actors are using generative AI to launch sophisticated, highly convincing phishing and social engineering attacks at greater speed and scale. Typical "tells" (incorrect grammar, awkward syntax) are largely disappearing.

#### Dark chatbots: uncovering WormGPT and FraudGPT on the dark web
"Dark chatbots" like WormGPT and FraudGPT have no security guardrails. They are predominantly used by threat actors to generate malicious code like malware with AI.

#### AI-driven malware and ransomware across the attack chain
AI is helping threat actors launch ransomware attacks with greater ease. Attackers use AI to identify an enterprise’s attack surface and internet-facing vulnerabilities, then generate or optimize code exploits for those vulnerabilities.

#### AI worm attacks and “viral” AI jailbreaking
Researchers have demonstrated the viability of "AI worm" attacks—self-propagating malware that can spread organically through an AI ecosystem to extract sensitive user data.

#### AI and US elections
The emergence of deepfakes makes it significantly easier for bad actors to spread misinformation and influence the voting public. US intelligence agencies have warned that state-sponsored entities will likely leverage AI to create confusion and undermine trust in the electoral process.

---

## All Eyes on AI Regulations

### United States
The focus has been on the White House Executive Order on the Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence, which compels developers of the largest AI systems to report safety test results to the Department of Commerce.

### European Union
The European Parliament has approved the AI Act, which will establish the world’s first comprehensive AI legislation. Expected to take effect in 2026, the laws will require general-purpose AI tools to comply with transparency requirements and will apply stricter policies to "high risk" AI applications.

---

## AI Threat Predictions

1. **Nation-states’ AI dilemma**: State-sponsored threat groups are poised to develop a complex relationship with AI, using it to generate more sophisticated threats while also striving to block access to anti-regime content.
2. **Dark chatbots and AI-driven attacks**: The scourge of "AI for bad" will grow as the dark web serves as a breeding ground for malicious chatbots like WormGPT and FraudGPT.
3. **Fighting AI with AI**: Enterprises will increasingly adopt AI technologies to combat AI-driven cyberattacks, including a focus on using deep learning and AI/ML models to detect malware and ransomware hidden in encrypted traffic.

[^1]: Statista, Future Use Cases for AI in Healthcare, September 2023.
[^2]: The Hill, AI already plays a vital role in medical imaging and is effectively regulated, February 23, 2024.
[^3]: McKinsey, Capturing the full value of generative AI in banking, December 5, 2023.
[^4]: TechCrunch, India reverses AI stance, requires government approval for model launches, March 3, 2024.
[^5]: OWASP, OWASP Top 10 For LLM Applications, Version 1.1, October 16, 2023.
[^6]: The Hacker News, Three Tips to Protect Your Secrets from AI Accidents, February 26, 2024.
[^7]: The Hacker News, Over 225,000 Compromised ChatGPT Credentials Up for Sale on Dark Web Markets, March 5, 2024.
[^8]: SC Magazine, Concerns over AI data quality gives new meaning to the phrase: ‘garbage in, garbage out’, February 2, 2024.
[^9]: Wired, Here Come the AI Worms, March 1, 2024.
[^10]: ComPromptMized, Unleashing Zero-click Worms that Target GenAI-Powered Applications, accessed March 12, 2024.
[^11]: arXiv, Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast, February 13, 2024.
[^14]: OECD, Policies, data and analysis for trustworthy artificial intelligence, accessed March 12, 2024.
[^15]: Deloitte, The AI regulations that aren’t being talked about, accessed March 12, 2024.
[^16]: White House, Executive Order on the Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence, October 30, 2023.
[^17]: NAIRR Pilot, The National Artificial Intelligence Research Resource (NAIRR) Pilot, accessed March 12, 2024.
[^18]: Reuters, Healthcare providers to join US plan to manage AI risks - White House, December 14, 2023.
[^19]: Pennsylvania Office of Attorney General, FTC Bans Use of A.I. to Impersonate Government Agencies and Businesses, February 26, 2024.
[^20]: European Parliament, EU AI Act: first regulation on artificial intelligence, December 19, 2023.
[^21]: CNBC, Singapore’s AI ambitions get a boost with $740 million investment plan, February 19, 2024.
[^22]: World Economic Forum, Global Risks Report 2024: The risks are growing — but so is our capacity to respond, January 10, 2024.
[^23]: ZDNet, Cybercriminals are using Meta’s Llama 2 AI, February 21, 2024.

---

en

as a critical means to gain visibility into cyber risk as well as create actionable, quantifiable

playbooks to prioritize and remediate security vulnerabilities. Translating noise into practical

signals has long been a top challenge for CISOs, because correlating risk and threat information

across dozens of tools can take a month or more. As such, in 2024, enterprises will look

eagerly to generative AI as a way to bring order to chaos, defray cyber risk, and drive leaner,

more efficient security organizations.

4

Data poisoning in AI supply chains: the risk
of garbage AI data will grow

Data poisoning will become a top concern as AI supply chain attacks gain momentum. AI

companies as well as their training models and downstream suppliers will be increasingly

targeted by malicious actors.

The OWASP Top 10 for LLM Applications highlights training data poisoning and supply chain

attacks as significant risks, running the risk of compromising the security, reliability, and

performance of AI applications. Simultaneously, vulnerabilities in AI application supply chains—
including technology partners, third-party data sets, and AI tool plugins or APIs—are ripe for

exploitation.

Enterprises reliant on AI tools will face heightened scrutiny as they assume these tools are

secure and produce accurate results. Greater vigilance in ensuring the quality, integrity, and

scalability of training data sets will be essential, particularly in the realm of AI cybersecurity.

029

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024AI THREAT PREDICTIONS

5

To leash or unleash: enterprises will weigh
productivity vs. security in their use of
AI tools

By now, many enterprises are past the early phases of AI tool adoption and integration, and

many will have carefully considered their AI security policies. Even so, this is a fluid situation for

most companies, and questions around which AI tools they will allow, which they will block,

and how they will secure their data remain open.

As the number of AI tools continues to skyrocket, enterprises will need to pay close attention

to the security concerns of each—at a minimum, seeking deep insight into their employees’ AI

usage, with an ability to enable granular access controls by department, team, and even at the

user level. Enterprises may also seek more granular security controls over AI apps themselves,

such as by enforcing data loss prevention policies in AI apps—preventing sensitive data from

leaking—or preventing user actions such as copy and paste.

6

AI-driven deception and distortion: viral
deepfakes will fuel election interference and
disinformation campaigns

Emerging technologies like deepfakes pose significant threats, including election interference

and the spread of misinformation. AI has already been implicated in misleading tactics

during US elections, such as generating robocalls impersonating candidates to discourage

voter turnout. These instances, while alarming, likely represent the tip of the AI-driven

disinformation iceberg.

Furthermore, the use of AI in such schemes may not be limited to domestic actors. State-

sponsored entities could also exploit these tactics to sow confusion and undermine trust in
the electoral process. In a notable case, attackers utilized AI-generated deepfakes to trick an

employee into transferring $25 million, demonstrating the real-world impact of this technology.

Similarly, illicit deepfake images of celebrities like Taylor Swift have gone viral on social media,

calling attention to how easily manipulated content can spread before content moderation

measures can catch up.

030

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024Case Study: Securely Enable
ChatGPT in the Enterprise

Best practices for AI integration and enterprise
security policy.

C AS E   ST U DY

5 steps to integrate and secure generative
AI tools

By now, enterprises have had plenty of exposure to AI tools. But as the number of AI

Enterprises seeking to securely adopt AI applications should take a measured approach.

applications continues to grow dramatically and adoption continues apace, enterprises can

Broadly speaking, they can first block all AI applications to eliminate the risk of data

adopt certain best practices to keep their data, employees, and customers safe. Overall,

leakage, and then take thoughtful steps to adopt specific, vetted AI applications with tight

enterprises must proactively and continually adapt their AI usage and security strategies to

security controls and access control measures to maintain complete control over enterprise

stay ahead of evolving risks while ushering in the transformative potential of AI.

data. For simplicity’s sake, the following journey focuses on OpenAI’s LLM ChatGPT.

Step 1:

Block all AI and ML domains and applications

To eliminate known and unknown risks associated with the thousands of AI applications

available, enterprises can take a proactive zero trust approach, blocking all AI and ML

domains and applications at the global enterprise level. This way, they can focus on
adopting a minimum set of transformative AI applications while closely controlling their

risks.

Step 2:

Selectively vet and approve generative AI applications

Next, the organization should identify a set of generative AI applications that exceed

high standards for certain criteria, such as the ability to create robust data protection,

security, and contractual measures to protect enterprise and customer data, as well as the

transformative potential of the applications themselves. For many enterprises, ChatGPT will

be one of these applications.

Step 3:

Create a private ChatGPT server instance in the
corporate/DC environment

To ensure complete control over their data, organizations should host ChatGPT in a

dedicated, secure tenant (such as a private Microsoft Azure AI server) hosted fully within

the organization. Then, through security controls and contractual obligations, enterprises
should ensure that neither Microsoft and OpenAI (in this example) has access to enterprise

031

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024

ZSCALER’S AI JOURNEY

or customer data, nor will enterprise user queries be used to train ChatGPT at large. This ensures

the organization retains control over its training data, allowing for highly relevant, accurate answers

AI best practices

for enterprise users while minimizing the risk of data poisoning from a public data lake.

In general, enterprises can adopt a few key best practices when it comes to

Step 4:

Move the LLM behind single sign-on (SSO) with strong multifactor
authentication (MFA)

Next, the organization should move ChatGPT behind a zero trust cloud proxy architecture, such as

the Zscaler Zero Trust Exchange, to enforce zero trust security controls over access to ChatGPT.

This might also include moving ChatGPT behind an identity provider (IdP) with SSO authentication

and strong MFA that includes biometric authentication. This will enable secure and fast user login

to ChatGPT while also allowing the enterprise to configure granular access controls at the user,

team, and department levels. This also ensures a separation of concerns between user queries at

those same user, team, and departmental levels.

Placing ChatGPT behind a cloud proxy like the Zero Trust Exchange further enables the organization

to inspect all TLS/SSL traffic between users and ChatGPT to detect cyberthreats and data leakage

while applying seven distinct layers of zero trust security.

Step 5:

Enforce the Zscaler DLP engine to prevent data leakages

integrating AI tools into the business.

•  Continually assess and mitigate the risks that come with

AI-powered tools to protect intellectual property, personal data, and
customer information.

•  Ensure that the use of AI tools complies with relevant laws and ethical standards,

including data protection regulations and privacy laws.

•  Establish clear accountability for AI tool development and deployment, including

defined roles and responsibilities for overseeing AI projects.

•  Maintain transparency when using AI tools—justify their use and communicate

their purpose clearly to stakeholders.

AI policy guidelines

Finally, the organization should enforce a DLP engine for the ChatGPT instance to prevent accidental

Enterprises should go behind these best practices and establish a clear policy

leakage of critical information, including proprietary data and code, customer data, personal data,
financial and legal data, and more. This ensures that any highly sensitive data will never leave the

framework that governs enterprise-wide acceptable use, integration and product
development, security and data policies, and employee best practices when

production environment.

using AI tools. The following best practices can form a useful starting point for

By following this journey, enterprise users can reap the full benefits of a generative AI tool like

establishing clear AI policies.

ChatGPT while eliminating the most critical data risks of adopting an AI application.

•  Do not provide AI models with personally identifiable information (PII) or any

non-public, proprietary, or confidential information.

•  AI cannot replace a human being, and it should not be used to make decisions

without appropriate human intervention.

•  AI-generated content should not be used without human review and approval,

especially when the content represents your organization.

•  Development and integration of AI tools should follow a Secure Product Lifecycle

Framework to guarantee the highest level of security.

•  Perform thorough product due diligence before implementing AI solutions,

making sure to evaluate their security and ethical implications.

032

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024

How Zscaler Delivers AI + Zero Trust
and Secures Generative AI

The transformative power of AI in cybersecurity lies in its ability to be
harnessed to combat the evolving landscape of AI-driven threats. At
Zscaler, we’re leveraging AI to help enterprises stop attacks across all
stages of the attack chain as well as easily diagnose and mitigate risk.

The key to AI-driven cybersecurity:
high-quality data at scale

Enterprises generate a vast wealth of log data that can contain high-fidelity signals that may indicate likely avenues for a
breach. However, signal-to-noise challenges have historically made it a challenge to isolate these signals quickly. Using

generative AI, Zscaler can leverage this data to effectively enhance triage and protection measures by understanding

the vulnerabilities and weaknesses attackers are likely to exploit. This not only allows Zscaler to predict breaches before

they happen, but also gives executives a holistic way to visualize and quantify cyber maturity and risk while prioritizing

cybersecurity remediation steps with Zscaler Risk360.

Generative AI capabilities not only extend to meta-analysis of enterprise cyber risk—they are also directly inserted into

cybersecurity products to better detect and disrupt advanced threats across the attack chain. Directly integrated into the

world’s largest security cloud, Zscaler LLMs and AI models take advantage of a data lake that sees more than 390 billion

daily transactions, with more than 9 million blocked threats and 300 trillion signals. Far from “garbage in, garbage out,”

this is “large-scale, high-fidelity data and threat intelligence in, finely-tuned, hyper-aware AI cybersecurity out.” All of
this translates to more powerful, more effective cybersecurity outcomes for IT and security practitioners.

033

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024HOW ZSCALER DELIVERS AI + ZERO TRUST AND SECURES GENERATIVE AI

Leveraging AI across the
attack chain

A I - P OWE R E D   P H I S H I N G  A N D   C 2   P R E VE N T I O N

Zscaler AI models detect known and patient-zero phishing sites to prevent credential theft

and browser exploitation, as well as analyze traffic patterns, behavior, and malware to

detect never-before-seen command-and-control (C2) infrastructure in real time. These

We’ve discussed numerous ways threat actors are using AI to launch sophisticated

models draw on a combination of threat intelligence, ThreatLabz research, and dynamic

threats at greater speed and scale. Zscaler deploys AI capabilities across the Zero Trust

browser isolation to detect suspicious sites. As a result, enterprises are even more efficient

Exchange platform and cyber product suite to identify and stop both AI-driven and

and effective in detecting new phishing attacks, including AI-generated attacks, and C2

conventional attacks at each stage of the attack chain.

domains.

Stage 1:

Attack surface discovery

F I L E - BAS E D  A I   SA N D B OX  D E F E N S E

The first stage of a cyberattack typically involves threat actors probing the internet-

The AI-powered inline Zscaler Sandbox instantly detects malicious files while keeping

connected enterprise attack surface to identify exploitable weaknesses. Often, this

employees productive. Traditional sandbox technologies make users wait while files are

includes things like VPN or firewall vulnerabilities and misconfigurations or unpatched

analyzed, or else assume patient-zero risk when files are allowed on first pass. Our AI

servers. Generative AI has made this once-arduous task significantly easier for attackers,

Instant Verdict technology instantly identifies, quarantines, and prevents high-confidence

who can simply query a list of known vulnerabilities associated with these assets.

malicious files—including zero-day threats—while removing the need to wait for analysis

Leveraging AI-driven insights in Zscaler Risk360, enterprises can instantly see these

discoverable (and thus risky) applications and assets—their internet-connected attack

surface—and hide them from the public internet behind the Zero Trust Exchange.

This instantly and dramatically reduces the enterprise attack surface while preventing
attackers from ever discovering weak entry points.

Stage 2:

Risk of compromise

on these files. This includes threats that are delivered over encrypted channels (TLS and

HTTPs) and other file transfer protocols. Meanwhile, benign files are delivered safely and

instantly.

A I  TO   B LO C K  WE B  T H R E AT S

AI-powered Zscaler Browser Isolation blocks zero-day threats while ensuring employees

can access the right sites to do their jobs. In practice, enterprise URL filtering often requires

more granular controls than allow/block; blocked sites are often safe and required for

During the compromise stage, attackers work to exploit vulnerabilities to gain

work, resulting in needless help desk tickets. Our AI Smart Isolation can identify when a site

unauthorized access to enterprise systems or applications. Zscaler AI innovations help

may be risky and open it in isolation for the user—safely streaming the site as pixels in a

reduce the risk of compromise, breaking up sophisticated attacks while prioritizing

secure, containerized environment. This effectively stops web-based threats like malware,

productivity.

ransomware, phishing, and drive-by downloads, creating a strong web security posture

without requiring enterprises to overblock sites as a default.

034

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024

HOW ZSCALER DELIVERS AI + ZERO TRUST AND SECURES GENERATIVE AI

Stage 3:

Lateral movement

Once attackers have a foothold inside an

organization, they will try to move laterally

to access sensitive data and applications.

And for many organizations, user access is

vastly overprovisioned to dozens of critical

applications—meaning that their internal

attack surface is substantial.

Zscaler AI capabilities reduce the potential

blast radius of attacks by analyzing user

access patterns and recommending intelligent

application segmentation policies to limit

lateral risk. For example, it’s common to

see that only 200 users out of 30,000

with access to a finance application actually

need it. Zscaler can automatically create an

application segment that limits access to only

those 200 employees, reducing threat actors’

lateral movement opportunities by more

than 99%.

Stage 4:

Data exfiltration

Summary of Zscaler’s
AI-infused offerings

Zscaler Internet Access™ provides AI-powered

protection for enterprise users, devices, and web and

SaaS applications across all locations as part of the Zero

Trust Exchange, delivering:

•  AI-powered phishing and C2 detection against never-
before-seen phishing sites and C2 infrastructure, using

M O R E OVE R,  Z S C A L E R   B LO C KS :

URLs and IPs observed in the Zscaler cloud as well as natively
integrated open source and commercial threat intel sources.

This includes policy-defined, high-risk URL categories

commonly used for phishing, such as newly observed and

newly activated domains.

IPS signatures developed from ThreatLabz analysis of phishing
kits and pages.

Zscaler Risk360 delivers a comprehensive and actionable risk

inline AI-based detection from the Zscaler Secure Web

framework that helps security and business leaders to quantify

Gateway (SWG).

and visualize cyber risk across the enterprise.

•  AI-powered sandboxing with comprehensive malware

and zero-day threat prevention.

•  Dynamic, risk-based policy with continuous analysis
of user, device, application, and content risk to fuel

dynamic security and access policy.

•  AI-powered segmentation with Zscaler

Private Access™, with automated access policy

recommendations to minimize the attack surface and

stop lateral movement using user context, behavior,

location, location, and private app telemetry.

Data Protection with DLP and CASB delivers AI-powered data

classification and data protection across all channels, including

endpoint, email, workloads, BYOD, and cloud posture.

Advanced Threat Protection blocks all known C2 domains.

Zscaler ITDR (Identity Threat Detection and Response)

mitigates the risk of identity-based attacks without ongoing

visibility, risk monitoring, and threat detection.

Zscaler Firewall extends C2 protection to all ports and

protocols, including emerging C2 destinations.

In the final stage of an attack, threat actors

•  AI-powered browser isolation, which creates a safe gap

DNS Security defends against DNS-based attacks and

work to exfiltrate sensitive data. Zscaler

between users and malicious web categories, rendering

exfiltration attempts.

uses AI to allow organizations to deploy data

content as a stream of picture-perfect images to

protections more quickly. AI-driven data

eliminate data leaks and delivery of active threats.

discovery eliminates the time-consuming task

of data fingerprinting and classification, which

can otherwise delay or prevent deployment.

Zscaler AI automatically discovers and

classifies all data across an organization

right out of the box, enabling enterprises to

immediately classify sensitive information

while configuring Data Loss Prevention (DLP)

policies to prevent that data from ever leaving
the organization in an attack or breach.

Zscaler Private Access™ safeguards applications by limiting

lateral movement with least-privileged access, user-to-app

segmentation, and full inline inspection of private app traffic.

AppProtection with Zscaler Private Access provides high-

performance, inline security inspection of the entire application

payload to expose threats.

Zscaler Deception™ detects and contains attackers attempting

to move laterally or escalate privileges by luring them with

decoy servers, applications, directories, and user accounts.

035

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024

HOW ZSCALER DELIVERS AI + ZERO TRUST AND SECURES GENERATIVE AI

Enabling the enterprise AI transition:
control is in your hands

Zscaler provides a way for enterprises to foster innovation, creativity, and productivity

with AI applications while keeping users and data safe among emerging channels for data

exfiltration. This empowers enterprises to embrace the transformative potential of AI to

accelerate their business without outright blocking AI applications and domains.

Securing the use of AI/ML apps

AI Apps

Company-wide visibility of AI app usage

AI APP Risk scoring for security & privacy

Selective access controls
AI/ML URL Category - 3200+ domain, 100+Cloud Apps

Prevent Data Loss to Generative AI Apps

Inline DLP: Blocks IP, PII, etc. from leaking out (ChatGPT Prompts)
Remote Browser Isolation: restrict uploads, downloads,
clipboard controls

FIGURE 23 Zscaler delivers innovative, fine-tuned security
controls designed for enterprise AI

Z S C A L E R   E N A B L E S   E N T E R P R I S E S  TO :

01  Drive full visibility into AI tool usage
01

Detailed logs provide complete visibility into how enterprise teams are using AI,

including the applications and domains they’re visiting as well as the data and prompts

being used in tools like ChatGPT.

02  Create flexible policies to fine-tune the use of AI
02

Powerful, tailored URL filtering for AI and ML applications let enterprises easily

define and enforce granular AI access controls and segmentation—blocking access

when necessary, while allowing access with acceptable levels of risk using AI App

Risk Scoring. Enterprises can allow access at the enterprise, department, team, and

user levels as well as enable caution-based access that coaches users on the risks of

generative AI tools. AI-driven segmentation makes it easy to identify appropriate user

segments for access to particular AI applications while minimizing the internal attack

surface associated with AI tools.

03  Enforce granular data security for ChatGPT and other AI applications
03

Enterprises can prevent the leakage of sensitive data uploaded to AI applications with

granular Zscaler Cloud Application controls for generative AI. By enforcing the Zscaler

DLP engine, enterprises can ensure that no data is accidentally shared when using any

AI tool. Meanwhile, AI-powered data discovery and classification lets enterprises easily
identify and create DLP policies around their most critical data, including their corporate

code base, financial and legal documents, personal data, customer data, and more.

This video demonstrates how the DLP engine prevents users from inputting credit card

information into ChatGPT.

04  Enable powerful controls using Browser Isolation
04

Zscaler Browser Isolation renders AI applications in a secure environment, adding a layer

of protection that allows user prompts and queries to AI tools while restricting copy/

paste, uploads, and downloads. This helps mitigate the risk of sensitive data being

accidentally shared with generative AI tools.

Enterprise and security leaders are at a crossroads: they must work to embrace AI to drive
innovation and stay competitive, but they must also ensure that their data only powers

the business, not breaches. Zscaler empowers enterprises to navigate this transition with

confidence, leveraging a full-suite of AI-powered zero trust security controls that protect

against AI-driven attacks while offering fine-tuned AI policies and data protections required
to harness the full potential of generative AI.

036

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024Appendix

ThreatLabz research
methodology

The Zscaler global security cloud processes over 300 trillion daily signals and

blocks 9 billion threats and policy violations per day, with over 250,000 daily

security updates. Analysis of 18.09 billion AI and ML transactions from April

2023 to January 2024 in the Zscaler cloud, the Zero Trust Exchange.

About Zscaler
ThreatLabz

ThreatLabz is the security research arm of Zscaler. This world-class team is responsible

for hunting new threats and ensuring that the thousands of organizations using the global

Zscaler platform are always protected. In addition to malware research and behavioral

analysis, team members are involved in the research and development of new prototype

modules for advanced threat protection on the Zscaler platform, and regularly conduct

internal security audits to ensure that Zscaler products and infrastructure meet security

compliance standards. ThreatLabz regularly publishes in-depth analyses of new and
emerging threats on its portal, research.zscaler.com.

037

©2024 Zscaler, Inc. All rights reserved.ZSCALER THREATLABZ REPORT 2024Experience your world, secured.

About Zscaler
Zscaler (NASDAQ: ZS) accelerates digital transformation so that customers can be more agile, efficient, resilient, and secure. The
Zscaler Zero Trust Exchange™ protects thousands of customers from cyberattacks and data loss by securely connecting users,
devices, and applications in any location. Distributed across more than 150 data centers globally, the SASE–based Zero Trust
Exchange is the world’s largest inline cloud security platform. To learn more, visit www.zscaler.com.

© 2024 Zscaler, Inc. All rights reserved. Zscaler™, Zero Trust Exchange™, Zscaler
Internet Access™, ZIA™, Zscaler Private Access™, ZPA™ and other trademarks listed
at zscaler.com/legal/trademarks are either (i) registered trademarks or service marks
or (ii) trademarks or service marks of Zscaler, Inc. in the United States and/or other
countries. Any other trademarks are the properties of their respective owners.

+1 408.533.0288

Zscaler, Inc. (HQ)  •  120 Holger Way  •  San Jose, CA 95134

zscaler.com