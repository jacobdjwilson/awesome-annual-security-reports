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

If there’s one thing 2025 made clear, it’s that speed matters more than ever—and I don’t just mean how fast threat actors move.

The gap between detecting a threat and actually doing something about it is where breaches happen. We saw it play out across our customer base all year: Many intrusions succeeded simply because the “basics”—like multifactor authentication (MFA) or proper configurations—weren’t fully optimized.

This year’s report digs into the data behind nearly a million alerts. You’ll see how identity remains the primary attack surface, and which endpoint and cloud threats continue to evolve. But beyond the numbers, you’ll find practical insights from our analysts who handled these threats in real time. What worked. What didn’t. What you can do about it.

We’re sharing this because cybersecurity is a team effort. The more we learn from each other’s experiences, the harder we make it for adversaries. We hope this report helps you head into 2026 with clearer direction and a few less unknowns.

Greg Notch
CSO, Expel

**Letter from the Director of Threat Operations:**

Effective security is the disciplined pursuit of prioritization. It’s not an abstract exercise in pursuing the art of the possible in understanding attacks—that doesn’t deliver impactful results. It’s the concrete and systematic work of risk mitigation and remediation. To deliver measurable results, we must progress from speculative threat modeling to a defensive strategy in tune with active threats in the wild.

This past year reaffirms an ever-present concern in cybersecurity: The vast majority of attacks that work today are not novel or sophisticated. They are successful because they exploit known and preventable gaps. The humbling truth is the attackers’ wins align to gaps in deployed security controls and configuration weakness, not technical gaps in security solutions.

So where should we focus in 2026?

There are some changes that can’t be ignored. AI doesn’t feature prominently in our attack data—but this is not to say it has no place in defense considerations. There are, of course, data loss prevention (DLP) and governance, risk, and compliance (GRC) considerations, but two other noteworthy areas demand attention.

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

Here in our 2026 Annual Threat Report, we see the threat landscape through three primary attack surfaces: identity, endpoint, and cloud infrastructure. Most incidents we see fall into one of these three categories. To set the table and give you the broadest perspective possible, here’s how our incidents divided between those three buckets versus prior years:

![Chart showing incident distribution across identity, endpoint, and cloud infrastructure]

The primary threat by volume comes from identity-based attacks, where actors successfully steal user credentials and authentication tokens for accessing accounts. This year, 68.6% of incidents involved identity. Each of these incidents represent gaps in security which can have a massive impact on an organization.

However, some good news: more than half of the identity-based attacks (52.3%) where attackers used legitimate credentials failed immediately thanks to security controls and MFA. Even so, attackers still managed to gain access in far too many of these incidents (47.7%).

To the surprise of no one, identity threats take the throne (again) and continue to wreak havoc on organizations. But has identity security been solved? Hold that thought; we’ll cover that in one of our many security practitioners’ “field notes” write-ups that we’ve included this year.

Following identity, the next most common incident type originated from endpoints (enterprise computers and servers), making up 29% of incidents. This category largely consists of opportunistic malware (63.9%), hands-on hacking attempts (21.4%), and server-side vulnerability exploitation (2.3%).

Endpoint attacks in 2025 were more “jazz standards” than groundbreaking; bad actors improvised on what already works. If it’s not broken, don’t fix it, right? Hot tactics in this category include suspicious PDF editors (which bundled legitimate functionality with malware installation) and the ever-effective ClickFix social engineering technique (which we’ve researched extensively), where users were tricked into copying, pasting, and executing malicious scripts.

Last but not least, cloud infrastructure comprised a small but growing portion (2.5%) of the types of incidents that we detected. And it’s an important one to defend, considering this is where proprietary data often lives and vital applications run. A cloud compromise could mean widespread organizational disruption. Many of these incidents involved unauthorized access to cloud resources through misconfigurations, vulnerabilities, and exposed cloud secrets.

### A peek behind the (data) curtain

Across our customer base, organizations experienced an average of 13 incidents during 2025, with a median of three incidents. Why the gap between median and mean? The reason becomes clear when we look at company size:

| Size | Incidents |
| :--- | :--- |
| Small (0-1,000) | 6.3 |
| Medium (1,001 – 10,000) | 23.8 |
| Enterprise (10,001+) | 67.8 |

When we break this down by organization size, the pattern becomes clear. Small organizations with fewer than 1,000 employees saw an average of six incidents per year—manageable, but still requiring vigilant monitoring. Medium-size organizations experienced 24 incidents on average, reflecting the larger attack surface and visibility to attackers. Meanwhile, enterprise customers with over 10,000 employees faced the largest burden of an average of 68 incidents per year.

This change based on organization size demonstrates exactly why managed detection and response (MDR) is useful across all organization sizes. The challenge faced by small organizations isn’t volume, it’s staffing. Teams often lack the ability to staff up for round-the-clock monitoring, yet even a handful of incidents can be devastating without a proper response. In contrast, the challenge for enterprises is sustaining high-quality responses at volume, all the while avoiding burnout.

This is where MDR delivers a key advantage. It can transform security from a cost center into a predictable operational expense with adequate coverage.

Looking at the data, it’s clear our detections engineers have been doing their part to stop attackers. Three quarters (75.6%) of the detections we monitored to protect our customers were either Expel-written detections or Expel-enhanced vendor detections. Most significantly, for high and critical severity incidents—where response speed is critical to avoid severe impacts—Expel’s custom detections were responsible for 78.8% of the detections.

As mentioned above, early detection and quick action are equally important. When dealing with high and critical incidents, with our auto remediation features enabled, our SOC’s current mean time to respond (MTTR) is an astonishing 13 minutes. This speed, combined with our early-stage detection capabilities, creates a defensive advantage that significantly reduces the window of opportunity for bad actors.

To round out the report, we prove that defensive advantage by plotting last year’s incidents across MITRE ATT&CK tactics. We found that these incidents were primarily identified by detections that alert early in the kill chain, focusing most on the initial access and early execution phases.

This early-stage detection provides security teams with critical opportunities to contain threats before attackers can get to more damaging activities, like exfiltrating data or deploying ransomware. Expel’s ability to capture incidents at this early stage fundamentally improves security outcomes by minimizing the impact of successful intrusions.

---

## Cybersecurity events in 2025

![Timeline graphic showing key events]

- **January 8**: Ivanti Connect Secure identified and patched a remote code execution (RCE) zero-day vulnerability.
- **February 2**: One of two days in 2025 with the fewest number of incidents our SOC investigated.
- **March**: Ransomware gang Black Basta’s chats were leaked, giving defenders insight into their code-signing certificate tactics.
- **March 10**: One of two days in 2025 with the fewest number of incidents our SOC investigated.
- **March 14**: Security researchers found that a GitHub action (tj-actions) used by 23,000 repositories was trojanized, impacting the down-stream repositories.

---

## Identity attacks: Credentials are valuable, protect them accordingly

Identity is a frequently targeted attack surface that—as our data shows—drives a substantial portion of security incidents. When a user’s account is compromised, an attacker can leverage that to access email, business applications, or collaboration applications.

Over the past several quarterly threat reports, we’ve split identity-based attacks into two categories:

- **Access denied**: Legitimate credentials have been stolen and were used, but the attacker was unable to gain access.
- **Access granted**: Legitimate credentials have been stolen and were used, and the attacker was able to gain access.

### Access denied

Most identity incidents we saw this year (52.3%) were instances where valid credentials were stolen but attackers failed to gain account access. In these cases, the attackers were blocked by existing security controls such as conditional access policies, which restrict user login locations or require company-managed devices to log in.

These “failed attempts” are treated as incidents since not all of the risk has been mitigated. When these failed logins occur, it can indicate the user has fallen victim to an attack such as a credential harvester or infostealing malware. The blocked login may have only been blocked temporarily, and a persistent actor may overcome the security policy by changing their user-agent or geo-location using a VPN. It’s essential for security teams to take these cases seriously, investigate the impacted account, and assess the potential impact.

The following behaviors were most frequently identified and blocked during incidents:
- Attempts to connect from known phishing infrastructure
- Connections from suspicious locations (e.g. not where the user resides)
- Logins through TOR nodes or unauthorized VPN applications
- Connections from unrecognized devices (e.g. not a work laptop)

### FIELD NOTES: Identity alerts in action–identifying and stopping them
*Josh Carter, Manager, SOC Operations*

Identity alerts are strong indicators of attackers attempting to gain access to an environment. We know that detecting and stopping these login attempts are critical to preventing further reconnaissance, persistence, lateral movement, and post-exploitation activities from happening. This past year, 68.6% of all incidents reported by the Expel SOC were identity-based.

One of the easiest ways to identify suspicious logins is by either adding approved (or “expected”) geographic locations to allow lists or blocklisting unapproved (or “unexpected”) geographic locations. If you’re an organization that works within a specific geography, this is a pretty easy task to undertake using your existing security tools.

Incidents involving a suspicious location accounted for 12% of identity incidents in 2025. However, it’s worth noting that if you’re a larger enterprise, hire contractors from outside your geographical region, and/or have employees that travel to other locations, you can open yourself up to lots of false positive alerts. If you’re writing your own login detections, make sure to consider factors such as acceptable VPN usage, active sessions, and user agents.

Speaking of user agents, Axios user agents continue to be a strong indicator of attacker activity. This past year, 9.5% of incidents were identified simply by a login attempt from an Axios user agent. So if you know that Axios isn’t something your organization uses, consider adding conditional access blocks for that user agent.

Of course, known malicious indicators are always a great way to quickly identify attacker activity. Expel’s Threat Intel and Threat Hunting teams work in tandem with the SOC to create new detections based on real-world, in-the-moment attacker behaviors. Last year, Expel identified 2% of incidents with detection rules written by the Threat Intel and Threat Hunting teams.

Finally, phishing emails continue to be the primary tool used by attackers to trick users into handing over their credentials. 12% of incidents last year were attributed to successful phishing attacks. Employee training continues to be the number one way to fight social engineering techniques. However, adopting additional tools to mitigate phishing attacks will help when a human inevitably makes a mistake.

### Access granted

What happens when entry isn’t denied? This was the case for 47.7% of identity incidents in 2025–access was granted to platforms by using valid (albeit stolen) credentials. In our role, it’s in our (and our customers’) greatest interest to shut attackers out. When identified, our team investigated and responded to the activity. We immediately shut down the compromised accounts, stopping the attackers in their tracks before they could cause further damage.

However, there is more nuance in the severity of these attacks. While bad actors do gain access to sensitive data at times, in the vast majority of incidents, no further activity is observed after they log in.

In order to distinguish between these two types of incidents, we began sorting these attacks into two further classifications in the second half of 2025:

- **Access granted**: A legitimate user session was accessed using valid credentials and MFA responses. There was no immediate evidence of secondary malicious activity (such as data exfiltration or lateral movement).
- **Access granted, malicious activity**: A bad actor successfully accessed a user account and performed malicious actions through the account.

### Phishing-as-a-service (PhaaS) trends

In the last few years, we’ve observed the commoditization of phishing infrastructure—primarily through phishing-as-a-service (PhaaS). PhaaS platforms are criminal service offerings that provide infrastructure and templates to carry out phishing campaigns. PhaaS is the leading contributor to increases in the volume of phishing emails.

Not only do these platforms facilitate more volume, they provide more capability. PhaaS platforms provide cybercriminals means to phish for MFA or steal session tokens, allowing attackers to intercept and authenticate despite the use of MFA.

### FIELD NOTES: Identity: a solved problem?
*James Shank, Director of Threat Operations*

In many pursuits, the problems that arise in the operational day-to-day aren’t new and aren’t unsolved problems. They are normal, routine, or ordinary problems. Most problems aren’t new discoveries—they’re gaps.

For the last several years, identity-related compromises have been one of three top contenders for initial access vectors. Why hasn’t it been solved?

The truth is, most of these identity compromise situations do have solutions aligned towards them. The technology itself isn’t the gap—the gap is the lack of technology implementation.

Take password exposure, for example. How long have there been strong password storage solutions? Another example: MFA being bypassed through SIM swapping. Where were the passkeys or OAuth 2.0? And another: sign-ins using stolen cookies. What about behavior monitoring, geo-location checking, and device-bound session credentials (DBSC)?

Technology currently exists to solve these problems and to fill these gaps. However, it’s often not in place because security has to fight for resources against competing business interests.

---

## Endpoint attacks: Malware is king

Endpoints are the second largest attack surface. While many sensitive files and data have moved to the cloud, user endpoints and servers remain prominent targets.

By far, the most common endpoint incidents involved malware (63.9%). In the incidents we fielded, these attacks were successful despite existing security controls, leading to a security incident and subsequent human intervention.

The second most frequent threat type were opportunistic attacks (21.4%). These incidents include activity such as attempted portscanning from an unmanaged computer, hands-on-actor commands originating from a compromised asset, and anomalous remote access tool usage.

### Malware activity

The malware that we see and focus on in this report are malware families that evaded our customer’s first lines of defense and executed on hosts.

**The decline of the champion**
In 2024, we observed that Lumma infostealer was the most prominent infostealing malware by far. This was also true for the first few months of the year, until the infrastructure behind the malware was targeted by international law enforcement in cooperation with private industry. This was a huge win for law enforcement and the cybersecurity community, resulting in a significant drop in malicious activity.

**The hot tactic**
The hot tactic this year—like so many other years—isn’t new, but it’s still delivering wins for the actors. The ClickFix tactic bypasses several defenses by tricking the user into executing a script on their own system. This tactic leverages an infected webpage to display instructions for the user: most often suggesting for them to complete a CAPTCHA or follow other instructions on how to fix an issue. Following the commands results in malware being executed on the host.

Incidents leveraging the ClickFix tactic accounted for 35.4% of all malware driven incidents.

### FIELD NOTES: Stop downloading free PDF editors (please)
*Jake Downie, SOC Analyst*

Please, for the love of SOC analysts like me, make sure your employees stop downloading free PDF editors.

Here’s a story. Sue receives a form from her boss that needs to be filled out and sent to a client ASAP. The only issue is that her job doesn’t provide licensing for a PDF editor. So she goes looking for a free PDF editor online.

She has so many options. PDFast, PDFSkills, or even SupremePDF. Sue wants only the best, so she clicks on a link to download SupremePDF. The program installs, and she uses it. The software works enough for her to edit the form and ship it off without terribly inconveniencing her or her boss.

What Sue doesn’t know is that SupremePDF is just a disguise used by malware to maintain a persistent hold on your system. Some days later, the security team is alerted to an attacker laterally moving on their network and stealing data. Tracking the source leads them right to Sue’s machine.

These “PDF editors” are actually trojans, which use their safe-looking outer shell to establish a foothold on your endpoints. The malware maintains persistence, making sure that the software creates a service that runs on the endpoint, keeping the PDF editor running. We often see these editors then used as a backdoor to run malicious code on the host, commonly abusing encoded PowerShell to download a second payload.

---

## Cloud infrastructure attacks: Lower activity, higher risk

Attacks against cloud infrastructure remain a low volume but high impact threat.

### When a threat is not a threat
The largest category of observed cloud infrastructure incidents was red team testing (32.2%). These incidents simulate real attacks and gaps in defenses, often identifying vulnerabilities or exposed secrets before cybercriminals do.

### Uninvited guests
The next largest category—unauthorized access (27.3%)—is made up of instances where attackers were able to access a device or deploy malware, due to cloud misconfigurations or other means. In these cases, attackers often deploy cryptominers like XMRig.

### Finding the skeleton key
Exposed cloud secrets remained a critical security issue, accounting for 25.7% of cloud infrastructure compromises. 54% percent of the incidents were caused by attackers leveraging the automated secret scanning tool, TruffleHog.

### Supply chains cloud over
The end of 2025 saw a fundamental shift in the nature of supply chain attacks with the emergence of the Shai Hulud 2.0 worm. Unlike previous attacks that relied on manual typosquatting or one-off compromises, Shai Hulud 2.0 is a self-replicating entity that weaponizes the “trust layer” of the software supply chain.

---

## Industry insights

Not all industries are targeted equally, and often the success of different attack tactics and techniques is different against various industries.

Organizations in every industry have their user accounts targeted, often making up 60–70% of the incidents seen within the industry. Manufacturing, financial services, and healthcare are the top three industries that saw the most incidents, respectively.

---

## Defending attack surfaces

Our 2025 data yet again proved something we’ve always known to be true: In security, the fundamentals should always be the top priority. Avoid chasing the headlines. Real-world attackers overwhelmingly favor the path of least resistance: unpatched systems, inadequate authentication verification, and basic social engineering.

### Identity
- Ensure there are conditional access policies for authentication in place at your organization.
- Use security policies and tools to minimize the threat of phishing.
- Audit and evaluate your current authentication requirements. When possible, use MFA following the FIDO2 standard.

### Endpoint
- Disable the use of the Windows Run hot key (Windows + R).
- Whenever possible, ensure employees have official means for downloading approved applications.
- Application whitelisting and Application Control for Windows can also block unwanted applications.

### Cloud infrastructure
- Configure your package manager to disable lifecycle scripts.
- Implement proactive secret key security and monitoring.
- Harden AWS instance metadata service (IMDS) settings.
- Monitor for cryptoming installations.

---

## Signal vs. noise: making the most of alerts

Alert fatigue is real. It’s a key challenge in cybersecurity, where understaffed security teams can become desensitized to the constant stream of alerts generated by security tools.

This is where Expel’s detection framework can make a clear difference. Across all detections that we monitor to protect our customers, 75.6% were either written from scratch by Expel or enhanced by Expel’s detection engine. Only 24.4% of the time did we rely on the vendor alert by itself.

### FIELD NOTES: Developing new detections to combat remote monitoring and management tools (RMMs)
*Chris Wagner, Detection & Response Engineer*

In 2025, we witnessed an increase in the malicious use of RMMs. On the surface, this is a difficult activity to build detections around, because RMMs also have many legitimate business use cases.

Instead, we created five new detections in conjunction with Ruxie’s automation capabilities to help us address RMM complexity:
1. Known RMM list detection.
2. Multiple RMM tools on a single host detection.
3. Multiple RMM-associated network connections detection.
4. Malicious-only RMM detection.
5. Non-standard port usage detection.

---

## Predictions for 2026

**Dave Merkel, CEO & Co-founder:**
“I don’t think we’ll see AI eliminating existing cyber jobs. We may see fewer open positions as companies navigate AI usage for efficiency, but you can bet those open positions will be filled by people that have cyber *and* AI skillsets. The adversary is still a human being. That human being will figure out how defenders are using AI, and exploit those behaviors to their advantage.”

**Greg Notch, CSO:**
“The key themes CISOs are concerned about remain the same: Managing identity risks, especially with third and fourth-party identities gluing together their SaaS estates; Budgetary pressures; Supply chain risks in both their own software supply chain and SaaS providers; Getting their arms around AI risks and governance.”

**Pierre Noel, EMEA Field CISO:**
“What to do, who to call, and react quickly. No organization is immune. AI may be the Trojan horse nation-state actors need to create massive disruption.”