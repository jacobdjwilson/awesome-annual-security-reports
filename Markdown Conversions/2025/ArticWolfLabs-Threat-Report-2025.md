# Threat Report 2025

## Table of Contents
- [Foreword](#foreword)
- [Key Takeaways](#key-takeaways)
- [Introduction](#introduction)
- [Part 01: Ransomware & Data Extortion](#part-01-ransomware--data-extortion)
- [Part 02: Business Email Compromise](#part-02-business-email-compromise)
- [Part 03: Intrusions](#part-03-intrusions)
- [Part 04: Managing & Mitigating Threats](#part-04-managing--mitigating-threats)
- [Conclusion](#conclusion)

---

## Foreword

This Arctic Wolf® Threat Report draws upon the first-hand experience of Arctic Wolf’s security experts, augmented by Arctic Wolf Labs research into the cybercrime ecosystem and additional credited sources.

By deliberately focusing on cyber attacks that escalated to a level of requiring an incident response (IR) investigation by Arctic Wolf, we aim to:

- Highlight which attack types are responsible for severe incidents
- Uncover the tactics, techniques, and procedures (TTPs) that allow threat actors to evade detection long enough to pursue actions on objective (e.g., deploying ransomware, tricking organizations into transferring funds, conducting intrusions, etc.)
- Raise awareness of the cybersecurity practices needed to prevent, detect, and recover from such incidents

Very broadly, we see evidence that threat actors are adapting to target stronger cybersecurity postures by looking for novel methods of attack or embracing low-tech — but effective — means of bypassing high-tech safeguards. At the same time, competition within their own ranks and better resilience on the part of their victims has ransomware operators engaging in more aggressive tactics and taking a firmer stance on ransom payments. Business email compromise (BEC) continues to be a menace, especially for organizations that routinely transfer funds and use email to coordinate these activities. And although many intrusions we investigated appear to be failed ransomware attacks, others are more likely to be incidents of stealthy cyber espionage.

How do organizations protect themselves in the continuing cybersecurity arms race? By focusing on the fundamentals, including:

- An adaptable security posture
- Detection and response spanning the full attack surface
- An IR process and partner that enables fast and effective recovery

Our hope is that reading this report will equip you with insights and actions to bolster all three of these elements.

**Kerri Shafer-Page**, Vice President, Incident Response

---

## Key Takeaways

- **95%**: Three cyber incident types account for 95% of all IR cases.
- **96%**: 96% of ransomware cases included data theft, as threat actors adapt to stronger backup and restoration capabilities.
- **+50**: The ransomware landscape is a modern-day Hydra. We observed more than 50 unique ransomware threat actors in victim environments.
- **Professional Incident Response (IR) Pays Off**: Our IR professionals were able to reduce aggregate ransom demands by 64%. 70% of our clients who used our negotiation services did not pay their ransoms.
- **BEC**: When it comes to Business Email Compromise (BEC), fraudsters follow the money. Finance and insurance accounted for 26.5% of BEC IR cases.
- **Low-Tech vs. High-Tech**: Attackers embrace low-tech ways to bypass high-tech defenses. Unsecured RDP and compromised VPN credentials are the leading root causes of ransomware and intrusions.
- **76%**: In 76% of intrusion cases, threat actors employed at least one of 10 specific vulnerabilities.
- **Zero-Day Exploits**: Threat actors save their zero-day exploits for stealthy intrusions (6% of cases).

---

## Introduction

The insights and data presented are drawn from hundreds of global digital forensics and incident response (DFIR) engagements conducted by the Arctic Wolf Incident Response team from October 1, 2023, through September 30, 2024.

### Data sourcing and methodology
To enable the holistic analysis within this report, all data is aggregated without any identifying characteristics or attributes. The vast majority of these IR engagements were initiated as part of cyber insurance policies.

### Case classification
We classify cases by the focal point of the incident, or the best answer to the question, “What is the most impactful aspect of the attack?”

![Chart showing Incident Response Cases by Category: 44% Ransomware/Data Extortion, 27% BEC, 24% Intrusions, 2% Malware, 2% Data Incidents, 1% Other]

---

## Part 01: Ransomware & Data Extortion

Ransomware remains the biggest driver of IR cases (44%). As backup and restoration capabilities improve, double extortion is now the norm (96% of cases).

### Lower barriers to entry
The ransomware-as-a-service (RaaS) model has democratized access to ransomware software, intrusion tools, and IT environments. Any aspiring cybercriminal can purchase access from an Initial Access Broker (IAB) and deploy ransomware.

### Ransomware actors continue to target organizations with no tolerance for downtime
Manufacturing (18.6%), Healthcare (13.1%), and Construction (12%) are the top industries targeted.

### Ransoms: demands, negotiations, and potential payment
The median aggregate ransom demand remains at $600,000 (USD). While every case is unique, Arctic Wolf’s experienced ransomware negotiators were able to secure a 64% reduction in aggregate ransom demands.

### Unsecured RDP
Unsecured Remote Desktop Protocol (RDP) and compromised VPN credentials are the leading root causes of ransomware IR cases, with RDP alone being the culprit in 38% of such incidents.

### Spotlight: The usual suspects
We identified five major ransomware groups behind 42% of the cases investigated:
1. **Akira** (15% of cases)
2. **LockBit** (9% of cases)
3. **BlackSuit** (6% of cases)
4. **Fog** (5% of cases)
5. **Play** (4% of cases)

---

## Part 02: Business Email Compromise

BEC incidents are the second-largest cause of IR cases (27%). 

### Financial services organizations are the prime targets
The finance and insurance industry accounted for 26.5% of BEC IR cases. BEC accounted for 53% of IR cases pertaining to finance and insurance.

### Social engineering drives BEC
Phishing (72.9%) and previously compromised credentials (18.8%) are the leading root causes of BEC cases.

---

## Part 03: Intrusions

Intrusions were the third-leading factor behind IR cases (24%).

### Intrusions, the first step towards greater threats
Intrusions include network intrusions (targeting edge devices) and host-based intrusions (targeting endpoints).

### Prioritized patching can prevent intrusions
In 76% of intrusion cases, threat actors employed at least one of 10 specific vulnerabilities, none of which were zero-days. Seven of these were associated with remote access tools or other externally facing services.

---

## Part 04: Managing & Mitigating Threats

To protect against these threats, organizations should focus on:
- **Adaptable security posture**: Implementing phishing-resistant MFA.
- **Detection and response**: Spanning the full attack surface.
- **IR process**: Having a partner that enables fast and effective recovery.
- **Backup practices**: Following the 3-2-1 principle (3 copies, 2 media types, 1 off-site).

---

## Conclusion

The cybersecurity landscape remains a high-stakes arms race. By focusing on the fundamentals—patching critical infrastructure, implementing phishing-resistant MFA, and maintaining robust, tested backups—organizations can significantly reduce their risk profile and improve their resilience against the most common and damaging threats.

©2025 Arctic Wolf Networks, Inc. All rights reserved. | Public

---

f the top six for

• Legal & Government

ransomware, albeit in a different order.

• Manufacturing

29

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public Key TermsA Trio of TargetsARCTIC WOLF   |   2025 THREAT REPORTPART 03: INTRUSIONS

Intrusion IR Cases by Industry

Finance & Insurance

Education & Nonprofit

Legal & Government

Manufacturing

Healthcare

Construction

Business Services

Other

Retail

Energy & Natural Resources

Technology

4.0%

3.3%

Shipping & Logistics

1.3%

15.3%

15.3%

14.7%

11.3%

8.7%

8.7%

6.0%

6.0%

5.3%

Intruders disproportionately leverage a small number of vulnerabilities

Like many clichés, the threat landscape being described as dynamic, ever-changing, or ever-evolving is rooted in

real-world truth.

New vulnerabilities are constantly being discovered, new exploits — including potentially devastating zero-

days — are always being written, and threat actors are always refining their approaches. However, across all

IR cases, time and again, we observe attackers leveraging a favored subset of TTPs.

For example:

This reality is both:

• In 76% of cases, threat actors employed one

• Humbling, because patches exist for all 10; and

or more of 10 specific vulnerabilities (whether

to gain initial access or to perform subsequent
intrusion actions)

• Empowering, because it shows that a small

amount of prioritized patching can significantly

decrease an organization’s chances of becoming

• In 51% of cases, threat actors employed one or

a victim.

more of the top four.

The number of known vulnerabilities continues to climb rapidly, from just under 6,500 in 2015 to more than 40,000 in 2024.

With advances in AI — reasoning techniques, in particular — we expect threat actors to identify novel routes to initial access.

Thus far, even the most advanced AI models have failed to replicate human reasoning capabilities, but that may soon

change. Once it does, threat actors will undoubtedly harness this newfound power to uncover new ways to break into

protected environments.

Learn more about what we think the near-term future holds in our Arctic Wolf Labs 2025 Predictions Report.

30

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public  AI-Assisted Vulnerability DiscoveryARCTIC WOLF   |   2025 THREAT REPORTPART 03: INTRUSIONS

Vulnerabilities keep increasing

In another record-setting year, over 40,000

vulnerabilities were recorded in 2024.

In addition to that alarming number, 2024 was

also a record-breaking year in regard to the volume

of critical and high-severity vulnerabilities. Both

increased by 13.46% in 2024.

This continued growth, fueled by hybrid work

models, increasing reliance on web applications,

and the use of AI by threat actors, underscores the

importance of implementing a robust, risk-based

vulnerability management program.

Explore the 2024 vulnerability landscape in-depth
and learn how to better protect your organization.

#01 CVE-2024-40766

SonicWall SonicOS Improper Access Control Vulnerability

#02 CVE-2023-4966

Citrix NetScaler ADC & Gateway Buffer Overflow Vulnerability

#03 CVE-2024-1709

ConnectWise ScreenConnect Authentication Bypass Vulnerability

#04 CVE-2024-3400

Palo Alto Networks PAN-OS Command Injection Vulnerability

#05 CVE-2023-48788

FortiClientEMS Remote Code Execution Vulnerability

#06 CVE-2023-3519

Citrix ADC, Citrix Gateway/ Citrix Bleed Remote Code Execution Vulnerability

#07 CVE-2023-41266 Qlik Sense Remote Code Execution Vulnerability

#08 CVE-2023-20269

Cisco ASA Firewall VPN Authentication Vulnerability

#09 CVE-2021-31207

ProxyToken: On-Premises Microsoft Exchange Authentication Bypass Vulnerability

#10 CVE-2023-27532

Veeam Backup and Replication Authentication Vulnerability

YoY Vulnerability CVSS v3 Severity Breakdown

Low

Medium

High

Critical

31

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public 514521665591617144217982038277432901392352624043054293453493557339289721047810977111781284380391170918801768825111711951093277227132910286828652404116501395496191180811611352152815681419150511738605180513005000100001500020000250003000035000400002012Total:52972013Total:51912014Total:79392015Total:65042016Total:64542017Total:147142018Total:165572019Total:173442020Total:183252021Total:201712022Total:252262023Total:290652024Total:40289ARCTIC WOLF   |   2025 THREAT REPORTProtecting your organization against vulnerabilities

Vulnerability remediation is the act of removing a vulnerability through patching
or another process.

By focusing on remediation, organizations can greatly reduce their cyber risk and prevent threat actors

from utilizing vulnerability exploits as an attack vector.

There are four main questions an organization needs to ask itself as it sets out to conduct vulnerability

remediation:

Which vulnerabilities should I remediate first?

How can I efficiently remediate those vulnerabilities?

How do I prioritize vulnerabilities based on my resources and business risk tolerance?

How do I set realistic deadlines for my vulnerability remediation plan?

Of course, those questions are easier to ask than to answer, and for many organizations that lack resources,

time, or budget, vulnerability remediation can seem like an endless mountain to climb.

Compounding the challenge, it’s difficult to determine which vulnerability to remediate first if you

don’t have a clear understanding of your overall attack surface. Plus, efficient remediation is all but

impossible without contextualization of your entire environment.

Unfortunately, that contextualization — including your risk policies, asset context, and service level

objectives (SLOs) — is not easy to achieve when you have limited resources and an overwhelmed IT

team. Not to mention the time and resources needed to conduct security scans and do the actual

remediating.

That’s why remediation should just be one part of a full vulnerability management program, which

prioritizes continuous vulnerability remediation and assessment, with other components of the

program complementing and assisting overall remediation and mitigation.

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public

3232

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public    01020304ARCTIC WOLF   |   2025 THREAT REPORTPART 03: INTRUSIONS

External exposure is the root cause of the vast majority of intrusions

Over half (60%) of intrusions were ultimately traced to external exposure. Like the ransomware cases examined

earlier, most of these are attributable to:

• External remote access tools and services (38%)

• External exploits (22%)

The same general analysis and recommendations already discussed (in the ransomware section) with

respect to external remote access tools and services apply here.

Root Causes of Intrusion IR Cases

26.5%
External Exploit

40.2%
External Remote
Access (e.g., RDP,
VPN, RMM, etc.)

CATEGORIES

76.1%
External Exposure

23.9%
Human Risk

6.0%

Zero-Day Exploit

1.7%

Brute-Force Attack

1.7%

Misconfiguration

8.5%

Malicious Software Download

6.8%

Phishing

5.1%

Social Engineering (e.g., Tech Support
Scam, Account Creation, etc.)

3.4%

Previously Compromised Account / Credentials

When external exploits were the culprit, the threat actor exploited a vulnerability for which a patch was

available prior to the incident — notice that seven of the top 10 vulnerabilities listed above pertain to either
remote access tools or externally facing services.

Interestingly, intrusion cases have by far the highest attribution to zero-day exploits (6%, versus only 0.4% for

ransomware and no BEC cases).

In some instances where remote access tools were abused, attackers took advantage of misconfigurations

(e.g., open ports, externally facing internal websites, administrative accounts vulnerable to brute-force

tactics) to gain entry.

It’s also worth mentioning that user-initiated malicious software downloads also account for a larger
percentage of intrusion cases (8.5%) than they do for either ransomware (4.4%) or BEC (0%). These
intrusions may well be opportunistic, in that a threat actor has booby-trapped an application and is
simply waiting to be alerted when it’s activated within an organization. This approach could be somewhat
targeted to particular industries by compromising particular types of software or employing watering hole
techniques to attract downloads from certain industries or professional roles.

33

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public ARCTIC WOLF   |   2025 THREAT REPORTHow to manage the risks associated with credential theft

Credential theft is the stealing of passwords, usernames, or other information
that allows for access to networks, applications, assets, or accounts.

Cybercriminals employ several ways to acquire credentials, including:

Phishing (e.g., email, voice, SMS)

Infostealer malware and credential dumping tools (e.g., Redline Stealer, Mimikatz, Sassy)

Credential stuffing and other brute-force attacks against the login box or API

For organizations with hundreds or thousands of users, staying on top of credential protection can be an

overwhelming task, especially if those users are not security minded and are using personal accounts on

company devices or a work email address for personal accounts.

Nevertheless, there are proactive and reactive measures a security team can take to improve credential

security and to build resilience against threat actors equipped with valid credentials.

These measures include:

•  Implementing (and enforcing) strong, phishing-resistant MFA, for example using FIDO Alliance’s

FIDO2 specifications (e.g., WebAuthn)

•  Proactively hardening Active Directory using tools like PingCastle for visibility into configuration

weak spots

•  Using around-the-clock, real-time monitoring — like the kind offered by a managed detection and

response (MDR) solutions — to recognize unusual user behaviors

•  Delivering comprehensive employee security training

•  Ensuring login services include layers of specialized defenses, including bot detection capabilities, to

guard against identity attacks

•  Embracing the principle of least privilege access (PolP), supported by a zero trust access model, role-

based access control (RBAC), and privileged access management (PAM)

•  Conducting (or subscribing to) dark web monitoring

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public

3434

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public    010203ARCTIC WOLF   |   2025 THREAT REPORTPART 04: MANAGING & MITIGATING THREATS

A robust cybersecurity strategy is one that is not only tailored to each organization’s needs, but one that

also includes both proactive and reactive elements to limit the number and severity of incidents while

providing a strong recovery capability.

We’ve already covered:

•  The importance of reliable backup processes, especially for recovering from ransomware and intrusions

•  How to build resilience against social engineering, which remains a major root cause of IR cases

•  Why prioritized vulnerability management can make it much harder for attackers to achieve their

objectives

•  How to manage the risks associated with credential theft, which is crucial as threat actors increasingly

turn to credential abuse as a means of avoiding defenses

Here are some additional recommendations to help safeguard your
organization in 2025.

Develop a solid understanding of your IT environment and attack surface

One of the most important pillars of an organization’s security posture is understanding the full breadth and

depth of the attack surface.

This data enables organizations to prioritize and refine their security program with precision and develop a

stronger vulnerability and security posture management program.

  Create and maintain an approved software list: This helps you rein in shadow IT and (with

monitoring) identify intrusions. For example, if software not on the approved list is downloaded

within the environment, alert and triage the finding — especially if it’s an RMM tool.

  Create an inventory of assets and their exposure: By doing so, you can gain a better understanding
of the overall attack surface and can correct instances where applications and devices are mistakenly

exposed.

  Do not expose management interfaces to the Internet: We have seen a multitude of vulnerabilities

that would have a significantly lower impact if management interfaces weren’t exposed.

  Take control of the cloud: We asked an Amazon Web Services expert for their advice on how to best

take control of you cloud environment:

“From my perspective, many cloud security incidents are not rooted in vulnerabilities but instead
can be traced back to misconfigurations and/or overly permissive access policies. You should

leverage IAM least privileges policies and monitor configuration drift away from your security
baselines as a part of your standard operations.”

– Ryan Orsi, WW Cloud Foundations Partner Specialists

35

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public ARCTIC WOLF   |   2025 THREAT REPORT
PART 04: MANAGING & MITIGATING THREATS

Ensure you have broad visibility (monitoring) into your environment and
assets, and create a baseline of normal behavior

Arctic Wolf has consistently recognized that a lack of visibility allows security threats to go unnoticed for

far too long.

Expanding environmental visibility beyond endpoints alone increases the likelihood of detecting potential

threats at an early stage, allowing for those threats to be stopped before they have a chance to inflict

significant damage.

  Monitor logs: Log monitoring is critical to detect major threats. This includes logs from intrusion
detection systems (IDS)/network detection and response (NDR) systems, endpoint detection and

response (EDR) solutions, firewalls, identity and access management (IAM) systems, email services

(e.g., to monitor for changes in access and the creation of filtering rules), and the cloud-hosted

services that extend your organization’s environment beyond your own infrastructure.

  Monitor endpoints: Implementing endpoint monitoring across the environment will help you review
public ports, disable unnecessary ports, and restrict port destinations. This type of monitoring is

crucial to provide visibility into actions taken by potential threat actors. While other types of log

sources can complement this type of visibility, they cannot replace it.

  Create a baseline: The better your understanding of your environment, the better positioned you are

to spot deviations that could be signs of a cyber attack, including data exfiltration.

Enforce strong identity controls

Identity is becoming a major battleground in modern cybersecurity, and today’s threat actors are adept

at finding and leveraging credentials that allow them to log into services and move unnoticed around

victim environments.



Implement and require strong, phishing-resistant MFA: At this point, failing to implement MFA can
be seen as an unnecessarily risky decision. Similarly, relying on legacy MFA techniques introduces

further unnecessary risk while giving a false sense of protection. Safeguarding your organization

requires modern, phishing-resistant MFA (e.g., based on the FIDO2 set of specifications).

  Employ a zero trust security strategy: Zero trust limits all access unless identity and security posture
can be verified. This strategy can reduce the attack surface and limit an attacker’s ability to move

laterally through an organization’s network.

36

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public ARCTIC WOLF   |   2025 THREAT REPORT
PART 04: MANAGING & MITIGATING THREATS

Establish and continually foster a culture of security

Positive security outcomes don’t happen by chance — they result from a culture in which security is ingrained

and embodied within and by everyone.

  Lead by example: Executives should not be exempt from the security requirements that apply to the

rank and file — attackers routinely take advantage of such exceptional treatment.

  Hold employees, the extended workforce, and third parties to the same high standards: Anyone

who has access to any part of your IT environment should be subject to the same access controls and

security policies.



Implement a comprehensive security awareness program: This helps users understand how they
can be targeted and how they are a critical line of defense against threat actors and breach attempts.

  Talk about security: The need for security should be understood by everyone as an everyday reality
of doing business. Create forums where people can ask questions; designate experts who can be

consulted on specific decisions; review security metrics at all-hands meetings — whatever it takes to

keep security top of mind.

Consider an IR retainer with an organization that staffs ransomware negotiators

The hope is you will never need to activate this retainer or employ these professionals, but if you do, you’ll be

relieved that they are available.

  Prioritize incident readiness. Prepare for severe cyber attacks by creating an incident response plan,

utilize incident runbooks, and reference/update preparedness materials often.

  Find a partner you can trust. A full-service incident response (IR) team should provide everything

needed to stop an attack and quickly restore your organization to pre-incident business operations.

  Seek an IR team with negotiation expertise. When finding a trusted IR partner, examine the

negotiation services and expertise – specifically, data regarding reduced ransoms or not paying the

ransom at all.

  Have insurance and legal approval. Many cyber insurance and data privacy councils have preferred
incident response providers who have familiarity with legal processes and policy requirements that

ensure a collaborative engagement with any organization and third parties to address legal – and

insurance-related requirements.

37

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public ARCTIC WOLF   |   2025 THREAT REPORTCONCLUSION

Adapting and evolving, together.

In this report, we’ve examined aggregated IR case data pertaining to ransomware, business email

compromise, and intrusion incidents.

We hope the insights and recommendations herein will allow you to take a practical, prioritized, and

informed approach to reducing risk and increasing resilience.

Taking a broad view of the situation, the fact that such incidents continue to occur — that is, despite

massive effort and expense directed towards prevention — speaks to two important realities with

which today’s organizations must contend.

First, adversaries are committed to their ‘craft,’

Second, preventative measures alone are

adapting and evolving as needed to achieve

insufficient. Yes, defenders must build and

their goals.

With strong financial (and sometimes political)

motivations, and unencumbered by laws,

certain ethical standards, or institutional

maintain a foundation of fundamentals and

continually adapt and evolve their security

posture such that, over time, those novel

defenses are integrated into the new normal.

planning horizons, attackers of all types show a

But defenders must also augment these

willingness to:

proactive measures with:

•  Stick with what works: tried-and-tested
approaches including favored exploits,

•  Reactive capabilities designed to quickly and

effectively detect and respond to attacks

specific intrusion tools, and preferred

that break through outer defenses

strategies

•  Risk transfer measures, including leveraging

•  Constantly develop new TTPs: from

warranties and insurance, in response to the

low-tech methods of bypassing high-tech

reality that — as this report has shown —

tripwires to the most advanced zero-day

incidents do happen (even to well-prepared

exploits — and everything in between

organizations)

It can all seem overwhelming — but you’re not alone.

An entire cybersecurity community stands with you and is committed to sharing and learning, lifting

and helping, and working together to withstand attacks and intrusions.

If you’d like to augment your internal capabilities with external expertise, we’re ready for you to join

the Pack.

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public

3838

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public    ARCTIC WOLF   |   2025 THREAT REPORTHow Arctic Wolf can help

The outcomes you need, the convenience you’ll love.

When we speak with organizations around the world, we’re often asked for three things:

An effective cybersecurity solution that will provide end-to-end protection against cyber

threats, that will be easy to manage, and that will integrate with the security products they’ve

already deployed

A way to financially offset the remaining risk

Expert assistance to help evolve their security posture over time, aligned with their specific

priorities and operating context

In response, we’ve created the Arctic Wolf Security Operations Bundles.

These bundles provide the full suite of technology, security expertise, and risk transfer options to end your

cyber risk.

Whether it’s proactive security offerings like employee awareness training, vulnerability scanning, and

incident readiness planning, or reactive detection, remediation, and active response capabilities to

minimize the severity of an incident, the Security Operations Bundles provide full coverage across all

your attack surfaces.

Best of all, some of the remaining risk may be financially transferred to Arctic Wolf through our

industry-leading Security Operations Warranty. With up to $1.5 million (USD) in financial coverage

and the ability to fund your cyber insurance deductible, your out-of-pocket costs after a severe cyber

attack may be mitigated.

If you aren’t getting the outcomes you’re looking for from the solutions you have today — or if you just need

some support in putting your existing investments to work — we would love to help.

For more information about Arctic Wolf, visit arcticwolf.com

Arctic Wolf and its employees are not licensed producers and therefore are not engaging in the sale, solicitation or negotiation of

insurance and are NOT offering advice regarding insurance terms, conditions, premium rates or claims. Customers interested in purchasing

Cyber Insurance coverage should consult with an appropriately licensed insurance broker.

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public

3939

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public    010203ARCTIC WOLF   |   2025 THREAT REPORTE N D   C Y B E R   R I S K

About Arctic Wolf

Arctic Wolf® is a global leader in security operations, delivering the first cloud-native security
operations platform to end cyber risk.

Powered by threat telemetry spanning endpoint, network, identity, and cloud sources, the Arctic Wolf

Aurora Platform ingests and analyzes trillions of security events each week to enable critical outcomes

for most security use cases. By delivering automated threat protection, response, and remediation

capabilities, Arctic Wolf delivers world-class security operations with the push of a button so customers

can defend their greatest assets at the speed of data.

For more information about Arctic Wolf, visit arcticwolf.com.

REQUEST A DEMO

©2025 Arctic Wolf Networks, Inc., All Rights Reserved. Arctic Wolf, Arctic Wolf Platform, Arctic Wolf Security Operations Cloud, Arctic Wolf Managed Detection and Response,
Arctic Wolf Managed Risk, Arctic Wolf Managed Security Awareness, Arctic Wolf Incident Response, and Arctic Wolf Concierge Security Team are either trademarks or registered
trademarks of Arctic Wolf Networks, Inc. or Arctic Wolf Networks Canada, Inc. and any subsidiaries in Canada, the United States, and/or other countries.

©2025 Arctic Wolf Networks, Inc. All rights reserved.  |  Public AW_RP_2025 LABS THREAT REPORT_0125