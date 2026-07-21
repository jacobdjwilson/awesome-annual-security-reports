# The Expel 2026 Annual Threat Report

An in-depth look at how last year’s attacks should inform your defense strategy today

## Table of Contents
- [Letters from leadership](#letters-from-leadership)
- [Executive summary](#executive-summary)
- [Cybersecurity events in 2025](#cybersecurity-events-in-2025)
- [Identity attacks: Credentials are valuable, protect them…](#identity-attacks-credentials-are-valuable-protect-them)
- [Endpoint attacks: Malware is king](#endpoint-attacks-malware-is-king)
- [Cloud infrastructure attacks: Lower activity, higher risk](#cloud-infrastructure-attacks-lower-activity-higher-risk)
- [Industry insights](#industry-insights)
- [Defending attack surfaces](#defending-attack-surfaces)
- [Signal vs. noise: making the most of alerts](#signal-vs-noise-making-the-most-of-alerts)
- [Predictions for 2026](#predictions-for-2026)

---

## Letters from leadership

### Welcome to our Expel 2026 Annual Threat Report

**Letter from the CSO:**
If there’s one thing 2025 made clear, it’s that speed matters more than ever—and I don’t just mean how fast threat actors move. The gap between detecting a threat and actually doing something about it is where breaches happen. We saw it play out across our customer base all year: Many intrusions succeeded simply because the “basics”—like multifactor authentication (MFA) or proper configurations—weren’t fully optimized.

This year’s report digs into the data behind nearly a million alerts. You’ll see how identity remains the primary attack surface, and which endpoint and cloud threats continue to evolve. But beyond the numbers, you’ll find practical insights from our analysts who handled these threats in real time. What worked. What didn’t. What you can do about it.

We’re sharing this because cybersecurity is a team effort. The more we learn from each other’s experiences, the harder we make it for adversaries. We hope this report helps you head into 2026 with clearer direction and a few less unknowns.

Greg Notch
CSO, Expel

**Letter from the Director of Threat Operations:**
Effective security is the disciplined pursuit of prioritization. It’s not an abstract exercise in pursuing the art of the possible in understanding attacks—that doesn’t deliver impactful results. It’s the concrete and systematic work of risk mitigation and remediation. To deliver measurable results, we must progress from speculative threat modeling to a defensive strategy in tune with active threats in the wild.

This past year reaffirms an ever-present concern in cybersecurity: The vast majority of attacks that work today are not novel or sophisticated. They are successful because they exploit known and preventable gaps. The humbling truth is the attackers’ wins align to gaps in deployed security controls and configuration weakness, not technical gaps in security solutions.

So where should we focus in 2026? There are some changes that can’t be ignored. AI doesn’t feature prominently in our attack data—but this is not to say it has no place in defense considerations. There are, of course, data loss prevention (DLP) and governance, risk, and compliance (GRC) considerations, but two other noteworthy areas demand attention.

AI systems themselves present a very prominent supply chain concern. Your data, automations, and implementations may be in the hands of a supplier that would be advantageous for an attacker to control. AI is also impacting attacker tooling and capabilities. Evidence is emerging that attackers are leveraging AI for tasks like obfuscating fingerprinting techniques, fuzzing code to identify exploitable bugs, and AI-assisted coding.

However, despite AI being new, the defensive strategy is still clear: keep focus on the fundamentals, and then audit the fundamentals again. Our data shows where the attacks are happening—align your budgets, your strategy, and your tactics using the data herein. Operationalize a lifecycle management strategy that includes an audit to make sure you’re delivering on your tactical plan. Find and fill your gaps as they overlap with our data.

For those keeping watch, stay vigilant!

James Shank
Director of Threat Operations, Expel

---

## Executive summary

At Expel, we see and field cybersecurity challenges every day, helping our customers identify, remediate, and prevent attacks. We’re on the front lines, and we see the latest attacks as they emerge.

Last year across our customer base, our security operations center (SOC) triaged nearly a million alerts generated across every major attack surface. And, of those alerts, our SOC investigated tens of thousands of incidents. As the SOC handled these alerts and incidents, they took notes; notes which were ultimately compiled into this report.

The next 10,000 words (give or take) paint a picture. They give a macro-level view of attacker trends and reveal behaviors you may have never considered.

We also finish the report by showing real data on how Expel-written detections (versus generic vendor detections) allowed our SOC to shut down the vast majority of observed incidents early in the MITRE ATT&CK framework kill chain. Detection is great. But early detection and quick action on those detections are equally key to business resilience.

Here in our 2026 Annual Threat Report, we see the threat landscape through three primary attack surfaces: identity, endpoint, and cloud infrastructure. Most incidents we see fall into one of these three categories.

![Chart showing incident distribution across identity, endpoint, and cloud infrastructure]

The primary threat by volume comes from identity-based attacks, where actors successfully steal user credentials and authentication tokens for accessing accounts. This year, 68.6% of incidents involved identity. Each of these incidents represent gaps in security which can have a massive impact on an organization.

However, some good news: more than half of the identity-based attacks (52.3%) where attackers used legitimate credentials failed immediately thanks to security controls and MFA. Even so, attackers still managed to gain access in far too many of these incidents (47.7%).

Following identity, the next most common incident type originated from endpoints (enterprise computers and servers), making up 29% of incidents. This category largely consists of opportunistic malware (63.9%), hands-on hacking attempts (21.4%), and server-side vulnerability exploitation (2.3%).

Last but not least, cloud infrastructure comprised a small but growing portion (2.5%) of the types of incidents that we detected.

### A peek behind the (data) curtain
Across our customer base, organizations experienced an average of 13 incidents during 2025, with a median of three incidents.

| Size | Incidents |
| :--- | :--- |
| Small (0-1,000) | 6.3 |
| Medium (1,001 – 10,000) | 23.8 |
| Enterprise (10,001+) | 67.8 |

Looking at the data, it’s clear our detections engineers have been doing their part to stop attackers. Three quarters (75.6%) of the detections we monitored to protect our customers were either Expel-written detections or Expel-enhanced vendor detections. Most significantly, for high and critical severity incidents, Expel’s custom detections were responsible for 78.8% of the detections.

---

## Cybersecurity events in 2025

![Timeline graphic showing key events: Jan 8 (Ivanti RCE), Feb 2 (Low incident day), Mar 2 (Black Basta leaks), Mar 10 (Low incident day), Mar 14 (GitHub action trojan)]

---

## Identity attacks: Credentials are valuable, protect them accordingly

Identity is a frequently targeted attack surface that—as our data shows—drives a substantial portion of security incidents.

### Access denied
Most identity incidents we saw this year (52.3%) were instances where valid credentials were stolen but attackers failed to gain account access. These “failed attempts” are treated as incidents since not all of the risk has been mitigated.

### FIELD NOTES: Identity alerts in action–identifying and stopping them
> "Identity alerts are strong indicators of attackers attempting to gain access to an environment. We know that detecting and stopping these login attempts are critical to preventing further reconnaissance, persistence, lateral movement, and post-exploitation activities from happening."
> — **Josh Carter, Manager, SOC Operations**

### Access granted
This was the case for 47.7% of identity incidents in 2025. We began sorting these into two classifications:
1. **Access granted**: A legitimate user session was accessed using valid credentials and MFA responses. No immediate evidence of secondary malicious activity.
2. **Access granted, malicious activity**: A bad actor successfully accessed a user account and performed malicious actions (e.g., registering a new MFA device, searching mailboxes, accessing cloud storage).

### Phishing-as-a-service (PhaaS) trends
In the last few years, we’ve observed the commoditization of phishing infrastructure. PhaaS platforms provide cybercriminals means to phish for MFA or steal session tokens, allowing attackers to intercept and authenticate despite the use of MFA.

### FIELD NOTES: Identity: a solved problem?
> "The truth is, most of these identity compromise situations do have solutions aligned towards them. The technology itself isn’t the gap—the gap is the lack of technology implementation."
> — **James Shank, Director, Threat Operations**

---

## Endpoint attacks: Malware is king

Endpoints are the second largest attack surface. By far, the most common endpoint incidents involved malware (63.9%).

### The decline of the champion
In 2024, Lumma infostealer was the most prominent infostealer. In 2025, following international law enforcement action, we saw a significant drop in its activity, with criminals navigating towards other infostealers such as Vidar and StealC.

### The hot tactic: ClickFix
The ClickFix tactic bypasses several defenses by tricking the user into executing a script on their own system. Incidents leveraging the ClickFix tactic accounted for 35.4% of all malware driven incidents.

### Backdoored productivity apps
We saw three primary categories of trojans: PDF editing tools, generic software apps, and AI helper apps. Each of these were primarily distributed through ads.

### FIELD NOTES: Stop downloading free PDF editors (please)
> "These 'PDF editors' are actually trojans, which use their safe-looking outer shell to establish a foothold on your endpoints. The malware maintains persistence, making sure that the software creates a service that runs on the endpoint."
> — **Jake Downie, SOC Analyst**

---

## Cloud infrastructure attacks: Lower activity, higher risk

Attacks against cloud infrastructure remain a low volume but high impact threat.

*   **Red team testing (32.2%)**: Simulations of real attacks.
*   **Unauthorized access (27.3%)**: Often involving the deployment of cryptominers like XMRig.
*   **Exposed cloud secrets (25.7%)**: Often identified by automated tools like TruffleHog.
*   **Server-side exploitation (11.5%)**: Including the critical React2Shell (CVE-2025-55182) vulnerability.

### Supply chains cloud over
The emergence of the **Shai Hulud 2.0 worm** marked a shift in supply chain attacks. It is a self-replicating entity that weaponizes the “trust layer” of the software supply chain, harvesting IAM secrets and injecting malicious GitHub Actions workflows.

---

## Industry insights

Organizations in every industry have their user accounts targeted, often making up 60–70% of the incidents seen within the industry. Manufacturing, financial services, and healthcare are the top three industries that saw the most incidents.

---

## Defending attack surfaces

Our 2025 data yet again proved that in security, the fundamentals should always be the top priority.

*   **Identity**: Implement conditional access policies, use FIDO2-standard MFA, and audit identity security controls.
*   **Endpoint**: Disable the Windows Run hotkey (Windows + R), use official channels for software downloads, and implement application whitelisting.
*   **Cloud**: Disable lifecycle scripts in package managers, implement proactive secret key monitoring, and harden AWS IMDS settings.

---

## Signal vs. noise: making the most of alerts

Vendor-provided detections are often built for the average organization, which means they’re optimized for no one. Expel’s detection framework is engineered to cut through noise.

*   **75.6%** of detections monitored were either written or enhanced by Expel.
*   **78.8%** of high and critical severity incidents were identified by Expel detections.

### FIELD NOTES: Developing new detections to combat remote monitoring and management tools (RMMs)
> "We set out to create something to help make this complex detection a little more manageable... We created five new detections in conjunction with Ruxie’s automation capabilities to help us address RMM complexity."
> — **Chris Wagner, Detection & Response Engineer**

---

## Predictions for 2026

*   **Dave Merkel (CEO & Co-founder)**: "I don’t think we’ll see AI eliminating existing cyber jobs... you can bet those open positions will be filled by people that have cyber and AI skillsets."
*   **Pierre Noel (EMEA Field CISO)**: "The key themes CISOs are concerned about remain the same: Managing identity risks, Budgetary pressures, Supply chain risks, and Getting their arms around AI risks and governance."

---
*12950 Worldgate Drive, Suite 200, Herndon, VA 20170 | (844) 397-3524*

---

SIEM |
| --- | --- | -------- | ---- |
24×7 Security
|     |     | Cyberspeak | Amazon Web Services (AWS) |
| --- | --- | ---------- | ------------------------- |
Operations
glossary
Google Cloud
AI &
Expel Intel
Kubernetes
Automation
|     | Engine |     | Microsoft |
| --- | ------ | --- | --------- |
Oracle Cloud Infrastructure (OCI)
Meet the SOC
experts
Workbench™
Operations
Platform
| ALSO OF |     | AI and Automation Engine for Defense |     |
| ------- | --- | ------------------------------------ | --- |
INTEREST
Phishing Detection and Prevention Solutions Security without compromise
Privacy | Compliance | Terms | EMEA Reseller © 2026 Expel, Inc. All Rights Reserved
Customer Terms | North America Reseller Customer
Terms | System Status