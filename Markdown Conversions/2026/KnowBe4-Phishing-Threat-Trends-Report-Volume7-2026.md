# Phishing Threat Trends Report - Volume 7

April 2026 | Vol. 7

## Table of Contents
- [Opening Stats](#opening-stats)
- [Attacker Attribution: Unmasking the Adversary](#attacker-attribution-unmasking-the-adversary)
- [Teams Phishing: The Inbox is No Longer the Only Frontline](#teams-phishing-the-inbox-is-no-longer-the-only-frontline)
- [Adversary-in-the-Middle (AiTM): The Stealthy New Standard](#adversary-in-the-middle-aitm-the-stealthy-new-standard)
- [The Agentic Shift: Anticipating the Era of AI-Driven Threats](#the-agentic-shift-anticipating-the-era-of-ai-driven-threats)
- [Calendar Invites: Infiltrating the Corporate Schedule](#calendar-invites-infiltrating-the-corporate-schedule)
- [2026 Intelligence Brief: Ask the Experts](#2026-intelligence-brief-ask-the-experts)
- [Wrapping Up: Staying One Step Ahead in a Shifting Landscape](#wrapping-up-staying-one-step-ahead-in-a-shifting-landscape)
- [Contributors](#contributors)

---

## How AI is Redefining the Phishing Frontier

2026 is off to a relentless start. The threat landscape is maturing rapidly, bringing new actors, novel tactics, and classic attacks supercharged by AI at scale.

Our 7th Phishing Threat Trends Report delivers actionable intelligence on this evolution. Modern phishing has transcended simple social engineering; today’s attackers ruthlessly exploit platform trust and manipulate systems to guarantee a return on investment.

This report dives deep into the diverse approaches of advanced persistent threats (APTs) and criminal groups. We explore the rise of multi-channel attacks targeting collaboration tools, and the mainstream adoption of Adversary-in-the-Middle (AiTM) and reverse proxies in criminal toolkits.

The message is clear: phishing in 2026 is disciplined, persistent, and increasingly AI-enabled. We hope these insights help you navigate this shifting frontier.

Unless otherwise stated, all statistics have been generated from KnowBe4’s Collaboration Security products. As always, please reach out if you have any questions or want to learn more about how Knowbe4 stops these threats.

**Jack Chapman**
SVP of Threat Intelligence, KnowBe4

---

## Opening Stats

![Chart showing opening statistics for Q1 2026]

---

## Attacker Attribution: Unmasking the Adversary

Cybersecurity professionals often struggle to address two critical questions: who is attacking my organization, and why?

Answering these questions is the foundation of proactive threat intelligence, allowing defenders to anticipate campaigns rather than just react to them. Yet, achieving this in the email space is notoriously difficult. Unlike malware analysis, which leaves concrete forensic artifacts, email is inherently transient. Attackers constantly rotate spoofed domains, sender IPs, and burner accounts to remain anonymous.

To overcome this, we have moved beyond tracking easily changed indicators and shifted our focus to the attackers’ actual behaviors. We combine a broad range of unique intelligence and detection data to provide enhanced visibility into adversary operations, basing our attribution on how these groups operate rather than on perishable data.

### Timing Is Everything

Examining these broad trends begins with the realization that modern threat actors operate on standard corporate schedules. The outdated stereotype of attacks occurring randomly in the middle of the night has been replaced by calculated precision.

![Graph: Attacks Started by Hour of Day - Q1 2026]

### Ask The Expert: James Dyer, Head of Threat Intelligence

> "We noticed a distinct increase in the number of attacks starting after lunch, with the volume beginning to surge around 1:00 PM (13:00) and accelerating rapidly until the peak at 5:00 PM (17:00) with 4,119 attacks started. The volume then gradually decreases through the late evening and overnight. This trend supports the insight that attackers are deliberately timing campaigns to target employees when they are likely fatigued and less scrutinizing as they wrap up their workday."

---

## Teams Phishing: The Inbox is No Longer the Only Frontline

As Microsoft Teams becomes the central nervous system for global collaboration within organizations, threat actors are following the action to exploit a unique trust gap. Unlike the formal pace of email, Teams is built for speed and informality.

Our Threat Research team has tracked a 41% surge in Teams-based attacks over the last six months (October 2025 – March 2026).

![Graph: Monthly Average Number of Teams Attacks Reported]

---

## Adversary-in-the-Middle (AiTM): The Stealthy New Standard

Adversary-in-the-Middle (AiTM) phishing is a technique that uses dedicated tooling to establish a proxy between a target user and a legitimate login portal for an application.

The deployment of a malicious proxy ensures that the spoofed login interface appears identical to the authentic site. This is because the target is, in fact, logging into the legitimate site, but their connection is routed through an attacker-controlled intermediary.

### MFA Bypass Attack Process
1. Victim sends Username/Password.
2. Attacker captures credentials via reverse proxy.
3. Attacker relays credentials to legitimate site.
4. MFA request is sent to victim by legitimate site.
5. MFA response is approved by victim.
6. Legitimate site sends authentication cookie back to attacker.
7. Attacker gains access.

---

## The Agentic Shift: Anticipating the Era of AI-Driven Threats

In the past six months alone, 85.8% of phishing attacks were AI driven. Attackers are now leveraging agentic tools to weaponize reconnaissance and scale high-fidelity threats that were previously impossible to automate.

### Cybercrime-as-a-Service Toolkits Found on Darkweb

| Tier | Toolkit | Price |
| :--- | :--- | :--- |
| 3 | Xanthorox AI (Xen) | $3,000 |
| 2 | FraudGPT (Lifetime) | $299 |
| 2 | WormGPT 4 | $220 |
| 1 | Hacking ChatGPT (2) | $50.96 |
| 1 | Unlock ChatGPT | $4.73 |

---

## Calendar Invites: Infiltrating the Corporate Schedule

Calendar Invite Phishing has surged by 49% in the last six months. By abusing the `.ics` file, attackers bypass standard security solutions that typically categorize these files as a benign scheduling tool.

![Diagram: How a malicious calendar invite appears in a user's schedule]

---

## 2026 Intelligence Brief: Ask the Experts

**Q: Are SEGs becoming obsolete?**
A: They certainly aren’t obsolete; however, they are struggling to keep up. We have witnessed a 31.4% increase in phishing attacks that are successfully evading SEGs.

**Q: Are humans writing these malicious emails or is it an LLM now?**
A: It’s a blended approach. The average length of a phishing email has nearly doubled since 2022, jumping from 497 to 1,011 characters. Attackers are using AI to write longer, more convincing narratives.

---

## Wrapping Up: Staying One Step Ahead in a Shifting Landscape

Relying solely on native security or legacy gateways is no longer a strategy—it’s a gamble. As cybercriminals pivot and equip their armory with sophisticated AiTM payloads and multi-platform attacks, your security stack needs to be as agile and adaptive as the adversaries themselves.

By moving toward a holistic ecosystem fueled by deep behavioral analytics and real-time threat intelligence, your employees become a line of defense.

---

## Contributors

- **James Dyer**: Head of Threat Intelligence
- **Lucy Gee**: Cyber Security Threat Researcher
- **Cameron Sweeney**: Cyber Security Threat Researcher
- **Louis Tiley**: Cyber Security Threat Researcher

Copyright © 2026 KnowBe4 All Rights Reserved.

---

odologies and builds tools to automate
threat intelligence gathering to identify industry
trends and shape cybersecurity messaging.

Jack Chapman
SVP Threat Intelligence

Dr. Martin J. Krämer
CISO Advisor

Jack leverages deep insights of the cyber-threat
landscape and his extensive R&D skillset to
oversee threat research and AI development for
KnowBe4 Defend to stop the advanced phishing
attacks that defeat traditional security solutions.
Jack maintains close ties with the global cyber
community, particularly the UK’s intelligence and
cyber agency GCHQ.

Martin is a CISO Advisor at KnowBe4. He has more
than 10 years of research and industry experience
in cybersecurity with a focus on human-centered
computing. Martin held roles in innovation,
research, and technology consulting. He has
worked with both public and private organizations
on information security and data protection.

Copyright © 2026  KnowBe4 All Rights Reserved.

36

About KnowBe4 Defend

An integrated cloud email security solution, Defend delivers AI-powered behavioral-based detection to eliminate
the attacks that get through native security and secure email gateways. Leveraging zero-trust and pre-generative
models, Defend provides the highest efficacy of detection against advanced threats, including zero-day and
emerging attacks, phishing emails sent from compromised accounts, and social engineering. Using dynamic
banners applied to neutralized threats, Defend provides real-time teachable moments that continually “nudge”
employees into good security behaviors to tangibly reduce risk and augment security awareness.

About KnowBe4

KnowBe4 empowers the modern workforce to make smarter security decisions every day. Trusted by more than
70,000 organizations worldwide, KnowBe4 is the pioneer of digital workforce security, securing both AI agents
and humans. The KnowBe4 Platform provides attack simulation and training, collaboration security, and agent
security powered by AIDA (Artificial Intelligence Defense Agents) and a proprietary Risk Score. The platform
leverages 15-years of behavioral data to combat advanced threats including social engineering, prompt injection,
and shadow AI. By securing humans and agents, KnowBe4 leads the industry in workforce trust and defense.

More information at KnowBe4.com.

KnowBe4, Inc.   |   33 N Garden Ave, Suite 1200, Clearwater, FL 33755
855-KNOWBE4 (566-9234)   |   www.KnowBe4.com   |   Sales@KnowBe4.com

Other product and company names mentioned herein may be trademarks and/or registered trademarks of their respective companies.

Copyright © 2026  KnowBe4 All Rights Reserved.