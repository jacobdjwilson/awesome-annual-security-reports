# Annual Cyber-Threat Report 2025

## Table of Contents
- [Introduction: 2024 in Review—Fast Threats Demand Faster Responses](#introduction-2024-in-review-fast-threats-demand-faster-responses)
- [Inadequate Logging Responsible for Most Breaches in 2024](#inadequate-logging-responsible-for-most-breaches-in-2024)
- [Breaking In: The Trends Shaping Initial Access Tactics](#breaking-in-the-trends-shaping-initial-access-tactics)
- [Old Habits Die Hard: Attackers’ Most Frequent Initial Access Techniques](#old-habits-die-hard-attackers-most-frequent-initial-access-techniques)
- [Phishing Trends: The Tactics Honing Cybercrime’s Most Reliable Weapon](#phishing-trends-the-tactics-honing-cybercrimes-most-reliable-weapon)
- [Session Hijacking Bypassed MFA in Every Successful BEC Incident in 2024](#session-hijacking-bypassed-mfa-in-every-successful-bec-incident-in-2024)
- [Social Engineering: How Attackers Weaponize Microsoft Teams](#social-engineering-how-attackers-weaponize-microsoft-teams)
- [GreyMatter Automations for Combatting Email Attacks](#greymatter-automations-for-combatting-email-attacks)
- [Critical Entry Points: VPN and Voice Phishing Among Most-Successful Techniques](#critical-entry-points-vpn-and-voice-phishing-among-most-successful-techniques)
- [Abuse of External Remote Services Led to 45% of Hands-on-Keyboard Intrusions](#abuse-of-external-remote-services-led-to-45-of-hands-on-keyboard-intrusions)
- [23% of Active Intrusions Initiated via Exploitation of Public-Facing Applications](#23-of-active-intrusions-initiated-via-exploitation-of-public-facing-applications)
- [Voice Phishing Behind 14% of Breaches](#voice-phishing-behind-14-of-breaches)
- [Access via Cloud Accounts and Trusted Relationships Achieved in 9% of Intrusions](#access-via-cloud-accounts-and-trusted-relationships-achieved-in-9-of-intrusions)
- [GreyMatter Automations for Combatting Unauthorized Access](#greymatter-automations-for-combatting-unauthorized-access)
- [SocGholish Secures Top Spot Again in 2024 Malware List](#socgholish-secures-top-spot-again-in-2024-malware-list)
- [SocGholish Persists in First Place with Python](#socgholish-persists-in-first-place-with-python)
- [ScreenConnect Abuse Propels AsyncRAT to Second Place](#screenconnect-abuse-propels-asyncrat-to-second-place)
- [Copy, Paste, Compromised: Lumma Rises to Third Place with Innovative Tactics](#copy-paste-compromised-lumma-rises-to-third-place-with-innovative-tactics)
- [GreyMatter Automations for Combatting Malware](#greymatter-automations-for-combatting-malware)
- [48 Minutes to Breakout: Unmasking Post-Compromise Trends](#48-minutes-to-breakout-unmasking-post-compromise-trends)
- [An Attacker’s Route to Control](#an-attackers-route-to-control)

---

## Introduction: 2024 in Review—Fast Threats Demand Faster Responses

In 2024, speed became more important than ever in defending against cyber threats. Attackers are moving at unprecedented speeds—last year, upon gaining initial access, they achieved lateral movement in an average of 48 minutes and managed to exfiltrate data in as little as 4 hours.

Attackers are also getting better at adapting to and evading the latest security controls, making the adoption of AI and automation imperative for organizations. Using AI and automation to tackle initial access attempts not only strengthens defenses but also empowers analysts to focus on what matters most: detecting and investigating the stealthiest and most impactful intrusions.

Though attackers are moving faster, they’re still using tried-and-tested methods like phishing to achieve initial access. They cast a wide net, indiscriminately targeting organizations with minimal effort and often causing significant damage. The year’s high count of disclosed vulnerabilities provided cybercriminals with entry points, while software suppliers remained a top target as a way to infiltrate organizational networks.

Ransomware and extortion remained critical threats compared to 2023, but the dynamics have shifted. Affiliates splintered into smaller groups, while leaked ransomware source code on cybercriminal forums sparked a wave of new attackers on the scene, with many focused entirely on data exfiltration. The result is a more fragmented, but no less dangerous, ransomware ecosystem.

ReliaQuest customers using Automated Response Playbooks in 2024 saw a dramatic improvement in response times, with the fastest mean time to contain (MTTC) cyber threats as low as 3 minutes. In comparison, customers yet to implement Automated Response Playbooks reported an average MTTC of 6.3 hours.

Additionally, in August 2024, ReliaQuest launched its first-of-its-kind AI agent for security operations, further speeding up containment of threats with better accuracy and consistency. By seamlessly handling routine Tier 1 and Tier 2 tasks and executing response actions securely, the GreyMatter AI Agent eliminates errors and delivers unparalleled efficiency in accelerating remediation times, allowing security teams to upskill by focusing on more critical tasks. By automating 100% of the investigation process—including data aggregation, analysis, and response—the GreyMatter AI Agent has reduced the average MTTC for ReliaQuest customers to less than 5 minutes.

## Inadequate Logging Responsible for Most Breaches in 2024

Our analysis of 2024 customer breaches revealed five critical security control failures at the core of these incidents:

1. **Insufficient Logging**: Insufficient monitoring or logging leaves parts of the system vulnerable, making it impossible to detect or investigate malicious activity.
2. **Insecure VPN**: VPNs lacking essential protections like multifactor authentication (MFA) or device-based certificates allow attackers to exploit stolen credentials and gain network access.
3. **Unmanaged Devices**: Devices without security controls like endpoint protection or monitoring agents create security gaps, providing attackers with open pathways throughout networks.
4. **Help-Desk Procedural Flaws**: Weak help-desk protocols make organizations easy targets for social engineering attacks, with 14% of breaches in 2024 involving social engineering for initial access or privilege escalation.
5. **External Exposure**: Vulnerabilities in internet-facing devices serve as entry points for attackers to infiltrate the network.

## Breaking In: The Trends Shaping Initial Access Tactics

Initial access is the critical first step of every cyber attack. It’s the moment attackers breach any configured defenses to gain a foothold in a network and set their plans into motion.

## Old Habits Die Hard: Attackers’ Most Frequent Initial Access Techniques

The consistency in top-ranked initial access techniques from 2023 to 2024 highlights their effectiveness and reflects attackers’ strategy of indiscriminately targeting a wide pool of victims. Phishing and drive-by compromise remain go-to methods, powered by the scalability and affordability of phishing-as-a-service (PaaS) and malware-as-a-service (MaaS) offerings.

- **2024 vs 2023**: Phishing with Link (25% vs 33%), Drive-By Compromise (24% vs 22%), Phishing with Attachment (9% vs 19%).

## Phishing Trends: The Tactics Honing Cybercrime’s Most Reliable Weapon

Data from the GreyMatter Phishing Analyzer revealed that nearly 30% of phishing messages that made it past traditional email security tools involved credential harvesters, often disguised as fake Microsoft login portals.

- **Credential Harvesters**: Dominated as the most reported category of malicious emails.
- **Scam Emails**: Crafted to solicit money or extract confidential employee information.
- **Reconnaissance Emails**: Single-word or blank emails used to verify if an account is active.
- **Malware-Laden Emails**: Containing attachments or URLs to deploy malicious files.

![Figure 1: Top subject line keywords]
![Figure 2: Top filename keywords]
![Figure 3: Top sender domains]

## Session Hijacking Bypassed MFA in Every Successful BEC Incident in 2024

BEC is one of the most dangerous methods attackers use to achieve their financial objectives. These attacks often start with a phishing email containing a link to an adversary-in-the-middle (AiTM) site, which intercepts MFA requests and session tokens.

![Figure 4: How AiTM phishing bypasses MFA and steals session tokens]

## Social Engineering: How Attackers Weaponize Microsoft Teams

Throughout 2024, ReliaQuest observed the ransomware group “Black Basta” employing a new social engineering tactic that leverages Microsoft Teams for initial access. By compromising legitimate Microsoft Entra ID tenants or creating fraudulent ones, the group impersonates IT support or help-desk staff to deceive targeted users into engaging with malicious Teams messages.

![Figure 5: Sample external Microsoft Teams message request]

## GreyMatter Automations for Combatting Email Attacks

ReliaQuest offers its customers a proactive defense strategy through its Automated Response Playbooks, which automatically contain and respond to threats.

- **Recommended Threat Hunting Packages**:
    - **Phishing—Microsoft Teams**: Identifies malicious messages from external domains.
    - **Phishing—Spearphishing Attachments**: Detects spearphishing attachments with uncommon file extensions.
    - **Hygiene—MFA Modifications**: Monitors unauthorized actions like registering new MFA devices.

## Critical Entry Points: VPN and Voice Phishing Among Most-Successful Techniques

In 2024, only 0.02% of initial access attempts managed to bypass defenses. The successful methods were:
- **External Remote Services**: 45%
- **Public-Facing Applications**: 23%
- **Phishing with Voice**: 14%
- **Cloud**: 9%
- **Trusted Relationship**: 9%

![Figure 6: Successful initial access methods in 2024]

## Abuse of External Remote Services Led to 45% of Hands-on-Keyboard Intrusions

Threat actors were most successful in gaining network access via external remote services like VPN portals, Remote Desktop Protocol (RDP), and virtual desktop infrastructure (VDI). IAB listings offering access via VPNs surged by 250% between 2023 and 2024.

![Figure 7: IAB listings in 2024 by sector]

## 23% of Active Intrusions Initiated via Exploitation of Public-Facing Applications

Between 2023 and 2024, adversaries targeting public-facing applications increased by 3%, a trend highly likely fueled by the 2,000-plus critical vulnerabilities identified last year.

## Voice Phishing Behind 14% of Breaches

Voice phishing (vishing) circumvents all technical defenses, instead directly targeting an organization’s people. Attackers gather employee information to deceive help-desk personnel into resetting credentials and disabling MFA.

![Figure 8: A user offers corporate calling services in multiple languages on forum XSS]

## Access via Cloud Accounts and Trusted Relationships Achieved in 9% of Intrusions

Attacks on customer cloud services like AWS and Azure rose by 4% between 2023 and 2024. Adversaries are also abusing trusted relationships, like those with third-party service providers, to infiltrate organizations.

## GreyMatter Automations for Combatting Unauthorized Access

- **Recommended Automated Response Playbooks**:
    - **Block IP**: Denies communication with specific IP addresses.
    - **Reset Password**: Forces a password change to invalidate stolen credentials.
- **Recommended Threat Hunting Packages**:
    - **Successful MFA from High-Risk Country**
    - **AWS Enumeration**
    - **Password Manager Access to Sensitive Secrets**

## SocGholish Secures Top Spot Again in 2024 Malware List

1. **SocGholish** (23%)
2. **AsyncRAT** (7%)
3. **Lumma** (5%)
4. **GootLoader** (4%)
5. **Cobalt Strike** (3%)

## SocGholish Persists in First Place with Python

SocGholish remains a dominant force, primarily distributed through infected websites. In February 2024, it introduced a new infection chain that uses Python for persistence, likely as a means to evade traditional security tools.

![Figure 9: Top command and scripting interpreters]

## ScreenConnect Abuse Propels AsyncRAT to Second Place

AsyncRAT gives attackers full control over infected hosts. In 2024, it contributed to the second-most customer incidents. It uses the guise of legitimate software (ScreenConnect) to infiltrate systems.

![Figure 10: AsyncRAT x ScreenConnect infection chain]

## Copy, Paste, Compromised: Lumma Rises to Third Place with Innovative Tactics

Lumma is an infostealer malware that harvests sensitive data. In May 2024, ReliaQuest observed Lumma being installed via a novel execution technique: coercing users into manually copying and pasting malicious PowerShell code into the console via fake browser errors or CAPTCHAs.

![Figure 11: Fake prompt containing malicious code]

## GreyMatter Automations for Combatting Malware

- **Recommended Detection Rules**:
    - **PowerShell Obfuscated Script**: Identifies obfuscated PowerShell commands.
    - **WScript Executing Suspicious File**: Monitors drive-by download activity.
- **Recommended Automated Response Playbooks**:
    - **Isolate Host**: Disconnects compromised hosts.
    - **Delete File**: Removes malicious files from endpoints.

## 48 Minutes to Breakout: Unmasking Post-Compromise Trends

Post-exploitation is where the real damage happens, and attackers are moving faster than ever, with lateral movement now taking an average of just 48 minutes.

## An Attacker’s Route to Control

- **RDP**: Became the most common method for lateral movement.
- **Internal Spearphishing**: Doubled year over year.
- **Privilege Escalation**: Centered around valid accounts, with 85% of breaches involving compromised service accounts.
- **Legitimate Tools**: Attackers used tools like Impacket, WinRAR, and RMM software in 60% of hands-on-keyboard incidents to stay hidden.

---

rmal
to compromise multiple accounts. of initial access. activity, making their abuse significantly harder to detect.
The period between initial access and lateral movement is known as breakout time. In our analysis of customer incidents from 2024, we found that attackers achieved an average breakout time
of just 48 minutes.
Percentage of 2024 Incidents by Lateral Movement Technique Percentage of 2023 Incidents by Lateral Movement Technique
32
Why RDP Became the Tool of Choice
for Lateral Movement
26%
In 2024, RDP topped the list as the most-used tool for 23%
lateral movement, giving attackers a straightforward
method to connect to other internal systems within an
16%
environment. Originally designed as a legitimate remote
15%
14%
management tool for IT help desks to assist global
workforces, RDP’s built-in presence on Windows systems
has made it a favorite among attackers.
8%
Armed with stolen credentials, attackers can use RDP
to discreetly move between systems, blending into
regular network activity without triggering alarms
that malware might. Its simplicity, stealth, and ability Remote Desktop Internal SSH & SMB/Windows SMB/Windows Remote Desktop Internal
to easily connect to systems makes RDP a go-to tactic Protocol Spearphishing Admin Shares Admin Shares Protocol Spearphishing
for lateral movement—and its misuse shows no signs
of slowing down.
32

Figure 12: RAMP forum user selling access and suggesting phishing internal users
Internal spearphishing, a technique sometimes used in BEC
attacks, doubled in frequency from 2023 to 2024, rising to
become the second most common tactic for lateral movement.
Internal spearphishing involves attackers compromising a user account
and using it to send phishing emails to other users within the same
organization, potentially compromising multiple accounts at once.
The significant rise in internal spearphishing can likely be attributed
to the 200% increase in phishing kit mentions on the dark web
between 2023 and 2024.
These phishing kits—tools designed to help attackers with little to no technical expertise launch phishing attacks—can bypass MFA and lower the barrier to entry for attackers.
This is especially true when paired with services on cybercriminal forums that offer or sell access to hundreds of active email accounts (see Figure 12).
33
As a result, advanced phishing campaigns have become accessible to attackers of any skill level.
By exploiting the inherent trust that employees place in internal emails, attackers achieve far higher success rates with internal phishing compared to external campaigns.
Given its success, this growing threat demands that organizations prioritize security awareness training and implement internal phishing simulations to assess system
and user readiness.
Enforce MFA for RDP and, to minimize exposure to potential threats, limit its use to essential systems only.
Take Action
Enable the scanning of internal emails to analyze messages exchanged between internal accounts and those
Against Lateral
sent externally to detect phishing attempts and malicious activity originating from compromised accounts.
Movement
Techniques
Use tools like AllowUsers or AllowGroups in sshd_config to restrict Secure Shell (SSH) access to specific
users or groups.
33

Valid Accounts, Invalid Intent: Easy Access to Privilege Escalation
Attackers are abusing high-privileged, valid accounts at both the domain and local levels to achieve short breakout times. Once inside an environment, attackers quickly assess the
permissions of the compromised account. Basic accounts rarely provide the keys to the castle, so to establish persistence or move laterally, attackers must escalate privileges to
gain the elevated access they need.
Our findings revealed that when attackers needed to escalate privileges, valid domain accounts were their primary targets—a trend unchanged from 2023. These accounts, whether owned by users,
administrators, or services, are frequently exploited because they offer the access and stealth attackers need to advance their operations without detection. This trend is reflected on cybercriminal
forums: For instance, we observed a user on the Russian-language forum XSS seeking advice on how to gain admin-level privileges to compromise a domain controller (DC) (see Figure 13).
Control over a DC opens the door to countless opportunities for attackers—they can map the network, access most connected devices, and steal sensitive data—making them a prized target.
Percentage of 2024 Incidents by Privilege Escalation Technique Percentage of 2023 Incidents by Privilege Escalation Technique
34
23%
22%
11% 11%
7%
6%
Domain Accounts Local Accounts Setuid and Setgid Domain Accounts Local Accounts DLL Injection
Local accounts also remain a key focus for threat actors, ranking second place for most-common privilege escalation technique year after year. Stored on individual systems, local accounts
include standard user accounts, service accounts, and the Windows default administrator account, and are often targeted in brute-force attacks. Because systems are guaranteed to have
local accounts, attackers can bypass the need to identify specific users, speeding up their efforts to compromise systems.
34

Figure 13: XSS user turns to other forum users for help on escalating privileges
Scattered Spider’s Web of Social
Engineering Unravels Privileges
In October 2024, Scattered Spider convinced a customer’s
IT help-desk staff to reset the CFO’s password in a social
engineering attack. The group later convinced another
help-desk employee to reset MFA controls and successfully
enrolled its own device.
Although the CFO’s account lacked the privileges necessary
Malware- or exploit-based attacks are noisy and can be easy to detect. But, by exploiting valid accounts,
to further its attack, Scattered Spider identified a domain
attackers make it difficult for organizations to distinguish malicious actions from legitimate activity,
administrator account in SharePoint that could provide
a fact they take advantage of.
elevated privileges. Recontacting the help desk, it achieved
a password reset, which granted the group access to the
organization’s password manager.
The longer attackers remain undetected, the greater the risk they pose—whether
through lateral movement, data theft, or deploying malicious payloads.
35
Within six hours of initial access, Scattered Spider began
encrypting the organization’s systems. The group created
Without strong security controls, these trusted accounts can turn into an organization’s biggest
a virtual machine within the organization’s VMware ESXi
vulnerability. Between January and July 2024, 85% of customer breaches involved compromised
environment to maintain persistence, concealing its activities
service accounts, allowing attackers to operate under the radar for extended periods. until encryption was complete and backups were sabotaged.
To mitigate the risk of domain account compromise, restrict domain account permissions, harden administrator accounts, implement
Take Action
stringent help-desk procedures, regularly clean up unused service accounts, and implement group managed service accounts (gMSAs).
Against Privilege
To secure systems from local account abuse, enforce strong and unique passwords for all local accounts and disable unused
Escalation
or default accounts, such as the Windows Administrator account.
To secure systems against Setuid and Setgid abuse, audit files using find
/ -perm -4000 and find / -perm -2000
to identify risky binaries. Remove unnecessary Setuid and Setgid bits with chmod u-s or chmod g-s to prevent attacks
from abusing them for privilege escalation.
35

The Adversary’s Toolkit:
Post-Exploitation Essentials
Legitimate RMM Tools Top Choice to Maintain C2 Impacket Now Go-To Post-Compromise Tool
Originally designed for IT professionals to manage Originally designed to interact with network protocols
In the past, adversaries relied heavily on frameworks
infrastructure, RMM tools pose serious security risks like SMB, New Technology Local Area Network
like Cobalt Strike and PowerShell exploits for C2.
when left unsecured. Their legitimacy allows attackers Manager (NTLM), and Lightweight Directory
However, enhanced detection measures have made
to slip past defenses, evading detection by appearing Access Protocol (LDAP), Impacket has become a
these methods increasingly risky for attackers.
benign. Attackers also exploit RMM tools in social go-to post-compromise tool for attackers, appearing
in 33% of breaches in 2024.
engineering campaigns, posing as help-desk support
To evade modern defenses, they are now turning to
to trick users into granting remote access.
commercial applications for malicious operations
This Python-based tool set is favored for lateral
(CAMO), leveraging legitimate tools such as AnyDesk
movement but also offers extensive capabilities—such
By mimicking routine IT operations, they seamlessly
and PDQ Deploy to maintain C2 and progress through
as credential dumping, Kerberoasting, and more—that
integrate into workflows, maximizing the effectiveness
every stage of the kill chain—from scanning networks
make it highly versatile and portable for
of their attacks while avoiding suspicion.
to deploying ransomware.
post-compromise operations.
To mitigate these risks, organizations must recognize
Between January and August 2024, ReliaQuest
Although Impacket is susceptible to signature-based
saw a 16% increase in the use of legitimate tools the risks of RMM tool abuse, incorporate it into their 36
detections, adversaries often exploit poorly monitored
in hands-on-keyboard incidents compared to 2023, threat models, and establish a baseline for normal
environments and take advantage of Impacket’s use of
with such tools accounting for 60% of cases. RMM tool usage to quickly distinguish normal activity
legitimate protocols like SMB, Windows Management
and malicious behavior.
These trusted tools have become the backbone of Instrumentation (WMI), and LDAP. It’s realistically
modern attacks, enabling attackers to avoid detection possible that adversaries adapt how they use Impacket
while inflicting maximum damage. Cybercriminals’ to mimic normal network activity, making their actions
increased reliance on legitimate tools outlines the harder to distinguish from legitimate behavior and
1. AnyDesk 2. TeamView 3. QuickAssist
need for organizations to understand how these appear non-malicious.
applications are being weaponized to bypass defenses.
These shifting tactics emphasize the importance of
4. Jwrapper 5. Dameware 6. ATERA
ensuring comprehensive network traffic logging and
Next, we'll detail the most common tools attackers
adequate security tool coverage to detect Impacket
used in breaches during 2024 and steps you can
itself as well as the network behaviors it generates.
take to mitigate these risks.
Figure 14: RMM tools favored by attackers
36

Medusa Turns Everyday Tools into Weapons
File-Compression Tools Gain Popularity Among Attackers
In April 2024, a customer in the information sector was
Attackers are increasingly using legitimate file-compression tools like WinRAR and 7-Zip to
infiltrated through an insecure VPN. In June, a “Medusa”
compress staged data before exfiltration, replacing the compression features traditionally
ransomware affiliate launched follow-on attacks. While
built into C2 frameworks.
not confirmed, it’s realistically possible that an IAB obtained
network access and later sold it to the Medusa affiliate.
Adversaries often use these tools in combination with cloud utilities like Rclone and MegaSync
to exfiltrate data to cloud storage. Because the activity generated by these tools often doesn’t
appear inherently malicious, organizations should establish a baseline for their usage and
The Medusa affiliate used legitimate tools to compromise
implement security controls to differentiate between legitimate and malicious activity.
the organization’s network: Netscan and PDQ Inventory
The message is clear: Attackers lean on legitimate tools because they’re easily accessible—many
Scanner for network discovery, AnyDesk for C2, and PDQ
are open source—and incredibly versatile, allowing them to execute multiple actions at once. By
Deploy to spread ransomware across the environment,
using trusted tools, attackers blend seamlessly into legitimate network traffic, avoiding suspicion
all while remaining hidden.
and complicating detection efforts, especially if an organization has no baselines for normal
use in place. For businesses, this camouflage can have devastating consequences. The longer
attackers remain undetected in a network, the greater the risk of major data breaches or
The organization’s vulnerabilities—including an insecure VP3N,7
operational disruptions—both of which can shatter an organization’s reputation and result
significant blind spots, and unmanaged devices—contributed
in the loss of key talent or critical business opportunities.
to the success of the attack, resulting in the encryption of a
portion of the environment.
Implement endpoint segmentation by blocking SMB communication from workstations to servers that don’t require it.
Take Action
This measure reduces the attack surface and helps prevent Impacket-based intrusions.
Against Abuse of
Implement an Active Directory (AD) Group Policy or application control tool that can be used to add approved RMM
Legitimate Tools
software to the allowlist.
Implement firewall rules to block domains associated with unauthorized cloud syncing and RMM tools.
37

Recommended Automated Response Playbooks
GreyMatter Automations
Reset MFA: Resets the user’s MFA, effectively
Terminate Active Sessions: Ends the user’s
for Combatting Legitimate active sign-ins and revokes session cookies, blocking attackers who may have intercepted
tokens or bypassed MFA during a phishing attack.
cutting off any unauthorized access in real time.
Tool Abuse
To combat threat actors' misuse
of legitimate tools, ReliaQuest
customers can leverage GreyMatter
Recommended Threat Hunting Packages
Automated Response Playbooks to
quickly contain attacker activity.
Additionally, GreyMatter threat Network Discovery Tooling: Detects the use of common network discovery tools, such as Advanced IP Scanner and
38
Angry IP Scanner, which threat actors use to map network topology and identify targets for lateral movement. By
hunting packages enable customers
analyzing telemetry from network traffic logs and EDR tools, organizations can identify reconnaissance efforts and
to proactively detect abuse of
mitigate risks early in the intrusion process.
legitimate tools within their
networks.
Together, these actionable measures
empower security teams to disrupt Remote Desktop Audit: Identifies suspicious RDP activity, such as unusual logins or session behaviors, that may
indicate access or lateral movement by threat actors. By analyzing event logs, processes, and registry changes,
attacker access and put a stop to
this threat hunting package helps organizations detect potential threats and strengthen defenses against
the unauthorized use of commonly
RDP-based attacks.
trusted tools.
Impacket Utilization: Detects the use of Impacket, a tool set often leveraged by threat actors to exploit
Windows network protocols. By analyzing telemetry from Windows Event logs and command-line logging
on destination hosts, organizations can detect malicious activity involving Impacket tools.
38

Ransomware Decoded: Exfiltration Is the New Encryption
Ransomware tactics have undergone a dramatic transformation. What began as straightforward extortion through system encryption grew into “double extortion,” where
attackers compounded encryption with the threat of leaking stolen data to maximize pressure on victims. Now, many attackers are abandoning encryption altogether,
focusing solely on data theft—a faster, more profitable approach. In 2024, this trend accelerated, with only 20% of breaches still featuring encryption. In this section, we’ll...
Examine this rise of Uncover the tools and methods Break down the major developments
exfiltration-only attacks driving these campaigns in the 2024 ransomware landscape
From the decline of key players to the emergence of new ones, we’ll explore the twists, turns, and trends to watch. Most importantly, we’ll provide actionable
recommendations to help organizations defend against these evolving threats—and demonstrate how ReliaQuest can keep organizations ahead of the curve.
Exfiltration Outpaces Encryption in Modern Breaches
39
When most people think of ransomware, they picture locked systems, black screens, and ransom notes—but that’s no longer
always the case.
Our data reveals a major shift in ransomware tactics: Of all breaches we observed in 2024, 80% involved data exfiltration,
while only 20% included encryption.
This sea change is almost certainly driven by the growing adoption of advanced security tools and robust backups, which have
Fastest Exfiltration in 2024
diminished the impact of encryption-based attacks. Additionally, the process of restoring encrypted systems can be so lengthy
and complex that organizations are likely choosing to rebuild their systems instead. This approach has the added benefit of
4 hours 29 mins
ensuring that any persistence mechanisms left by the attacker are completely removed. As encryption becomes less effective,
groups like “Inc Ransom” now weaponize stolen data for extortion, resale, or access to additional targets, preying on organizations’
fears of reputational damage, regulatory fines, and the exposure of sensitive information.
Fastest Encryption in 2024
The time required for an adversary to progress from initial access to executing data exfiltration is 34% faster than the time needed
for encryption; the quickest exfiltration time we saw in 2024 clocked in at just 4 hours and 29 minutes, compared to 6 hours for 6 hours
encryption. This leaves defenders with even less time to detect and respond before critical data is stolen. By bypassing the
technical complexities of encryption, attackers have embraced data exfiltration as their ultimate tool to strike quickly, inflict
maximum harm, and maintain leverage over their victims.
39

These services are highly useful for stealthy exfiltration, as stolen data can be uploaded quickly and
In 2024, 60% of attackers who successfully disguised within legitimate traffic from commonly used platforms. This makes detection more difficult for
defenders because the exfiltration activity blends in with normal business operations. Given the potential
exfiltrated data in the incidents we
for business disruption, blocking access to widely used cloud platforms is rarely a viable option for
examined sent the stolen data to cloud businesses. This limits defenders’ ability to be proactive, instead forcing them to rely on advanced
monitoring and alerting to identify and respond to malicious activity.
storage platforms such as Google Drive,
Accounting for the remaining 40% of attacks, exfiltration over C2 channels enables attackers to funnel
Mega, or Amazon S3.
data directly to their own infrastructure.
This method requires a direct connection from the compromised system to the attacker’s infrastructure, making the malicious activity more likely to be detected. However, despite this
increased risk, C2-based exfiltration offers attackers greater control over the stolen data compared to third-party platforms like cloud services. This method is utilized by adversaries
40
who don’t use legitimate tools in their operations, such as RMM tools, and instead prefer the built-in capabilities of C2 frameworks to compress, encrypt, and exfiltrate data.
Looking ahead to 2025, we expect the trend of exfiltration-only attacks to persist, with exfiltration times likely to drop even further. For organizations, this shift demands a rethink of
ransomware recovery strategies. The focus can no longer be solely on restoring encrypted systems—strategies must also address protecting data privacy, managing reputational risks,
and ensuring compliance with regulatory requirements. To prepare, CISOs must implement defenses to detect and prevent exfiltration attempts while developing playbooks that
prioritize business continuity and resilience against these evolving ransomware tactics.
Deploy web proxies to block access to malicious or unauthorized websites that attackers could use for data exfiltration.
Take Action
Enforce strict access control policies to prevent connections to unapproved external services, reducing the risk of data
Against
leaks or unauthorized data transfers.
Exfiltration
Regularly monitor cloud service usage for unusual behavior like unexpected file uploads or downloads and
block unauthorized cloud services at the network edge to prevent abuse.
40

In 2024, the names of 5,253 organizations were listed
Ransomware in 2024: Increased 11.9%, Hit New Highs
on ransomware data-leak sites—559 more than in 2023.
Although this growth may seem modest, much of 2024 actually saw a slowdown in ransomware activity. Instability within the ransomware ecosystem played a significant role,
as ransomware-as-a-service (RaaS) providers focused more on competing for affiliates than refining their attack techniques. Operations were further disrupted by law enforcement
actions dismantling key ransomware infrastructure, improvements in security tool detection capabilities, and advancements in cybersecurity practices.
But the slowdown didn’t last. December 2024 marked a grim turning point, recording the highest-ever victim count in a single month. This surge can be attributed to the explosion of new
ransomware groups, which have grown from around 60 active groups in 2022 to nearly 100 today. To avoid the spotlight and scrutiny faced by larger operations like LockBit, smaller,
decentralized groups are forming, fueling an increasingly crowded and competitive landscape. As a result, attackers are likely to push for higher ransoms and adopt more sophisticated
strategies to outpace defenses and secure their share of the profits.
621
600
2024
584
542
527
2023
483 41
463
457 459
439
424
404
400 401
382
379
357
347
317
316
314
299
271
161
January February March April May June July August September October November December
Figure 15: Ransomware volume trends, 2024 vs. 2023
41

From Extortion to Exit Scams: The Big Ransomware Group Shake-Up of 2024
LockBit Affects 93% Fewer Organizations ALPHV Exits with Big Profits RansomHub Ups the Ante
2024 marked the year that LockBit—the omnipresent “ALPHV’s” sudden exit in March 2024, following a “RansomHub” wasted no time capitalizing on the void
ransomware threat throughout 2023—became the
reported $22 million payday from its attack on Optum, left by declining giant, LockBit. Its game-changing
target of multiple law enforcement operations that
added to the turbulence in the ransomware landscape. affiliate model—paying affiliates 90% of the profits
disrupted its infrastructure.3
upfront while retaining just 10%—made it a top choice
With LockBit in decline and “Clop” sticking to its
among cybercriminals, driving a surge in activity.
While LockBit attempted a comeback in May by
strategy of infrequent but high-reward attacks, the
naming 176 organizations on its data-leak site, it failed
absence of these dominant players created an opening By the second half of 2024, RansomHub had firmly
to sustain momentum, ending the year with only 19
for smaller, fragmented groups to rise to prominence established itself as the most active ransomware
victims in its final quarter—a staggering 93% decrease
throughout 2024. group, naming 326 more victims than LockBit.
compared to the same period in 2023.
42
1038
2024
2023
543
534
422
369
342
294
267
235 234
217 211
172 175
171 166 166
155 149
145
LockBit RansomHub ALPHV Clop Play 8Base Black Basta Malas Akira Medusa Qilin Hunters Inc BlackSuit BianLian
International Ransom
Figure 16: Top ransomware groups by number of data-leak postings, 2024 vs. 2023
42

Groups to Watch Out for in 2025
The “BlackLock” (aka Eldorado) ransomware group, active since at least March In September 2024, new group “FunkSec” emerged on the ransomware scene,
2024, gained prominence in July but truly made its mark in October. Its victim count making a major impact by December by listing 82 victims—more than any other
skyrocketed by over 1,000% from Q3 to Q4 2024. group that month.
Likely tied to Russia (evidenced by its refusal to target countries in the FunkSec targeted a wide range of sectors, including retail, manufacturing, health
care, education, and professional services, across countries like the US, France, India,
Commonwealth of Independent States), BlackLock’s rapid ascent mirrors
and Thailand. The group promotes its technical expertise on cybercriminal forums,
that of groups like RansomHub, proving how quickly a group can move from
boasting a free distributed denial-of-service (DDoS) tool, a Tor-based data-leak site,
obscurity to dominance.
and a suite of self-developed tools.
It’s realistically possible that both BlackLock and FunkSec stockpiled victims and chose to publish them all on their respective data-leak sites before the year ended. However, our analysis
suggests it’s more likely that both groups capitalized on the turbulence amongst ransomware groups, scooping up affiliates from faltering groups and thriving in the absence of dominant players.
43
The constantly changing ransomware threat means that traditional defenses won’t cut it anymore. Organizations must adopt proactive, multi-layered strategies that combine technology, processes,
and people. In 2025, ransomware will remain largely opportunistic, but the explosion of new groups and affiliates will make attacks more unpredictable and widespread than ever before.
2760 Ransomware Mostly Targets US, Manufacturing, and PSTS 2024
2134
2023
252 293
198
296 158 183 121 158 137 142 107 92 121 73 114 67
US UK Canada Germany France Italy Spain Brazil India
Figure 17: Number of victims by region added to ransomware data-leak sites, 2024 vs 2023
43

Figure 18: Number of victims by industry added to ransomware data-leak sites, 2023 vs 2024
964
As anticipated, the US remained the overwhelmingly Manufacturing
1098
popular target for ransomware operators and
Professional, Scientific,
855
1079
and Technical Services
affiliates in 2024.
396
Construction
524
This trend is highly likely to continue, as attackers perceive that
381 Health Care and
organizations in English-speaking countries have the financial means
500
Social Assistance
to pay ransoms.
345
Finance and Administration
347
Additionally, well-developed insurance markets and heightened cybersecurity awareness
296
Educational Services
in these countries have driven higher adoption of ransomware insurance, making these
246
regions more attractive to attackers.
219
Retail Trade
396
Ransomware operators are acutely aware that the manufacturing sector is highly vulnerable to operational disruptions.
173 Accommodation and
The integration of IT with operational technology (OT) in this sector exacerbates the problem, as downtime can lead 195 Food Services
to major productivity, financial, or legal consequences. These factors make ransom demands more effective, boosting 170
Public Administration
241
ransomware groups’ profits and attack success rates.
153
Information
177
44
The PSTS sector is a lucrative target because of the sensitive data it handles and its reliance on digital resources for operations like
152 Arts, Entertainment,
client collaboration and secure file transfers. Its dependence on file-transfer software and other tools makes it especially vulnerable
149 and Recreation
to exploitation. This vulnerability was evident in multiple supply-chain attacks conducted by the Clop ransomware group, where
120 Mining, Quarrying,
adversaries compromised widely used tools to target numerous organizations—a growing trend that mustn’t go unnoticed.
118 and Oil and Gas
104 Real Estate and
107 Rental and Leasing
94
Wholesale Trade
69
68
Utilities
64
Use GreyMatter Digital Risk Protection (DRP) to detect exposed credentials on cybercriminal forums and thwart initial
Take Action
access attempts by ransomware groups.
Against Prioritize employee awareness training on social engineering tactics, as groups like Black Basta and RansomHub
continue to exploit human vulnerabilities with success.
Ransomware
Use GPOs to restrict PowerShell usage to only those users who require it for their role. This will prevent
ransomware actors from abusing PowerShell to execute malicious scripts.
44

Recommended Detection Rules
GreyMatter Detections and
Rclone Execution via Command Line: Rclone is a powerful and effective tool for copying data to various cloud
Automations for Combatting
storage providers, making it a popular choice for ransomware operators to facilitate exfiltration. This rule detects
the use of Rclone by looking for common arguments in PowerShell or the Command Prompt.
Ransomware
Data Exfiltration via Command Line: After retrieving the information they want to exfiltrate—such as credentials or
To combat ransomware and data
sensitive documents—threat actors can use the command line to execute data exfiltration commands. This rule
exfiltration threats, we advise
specifically detects the different methods threat actors use to leverage command-line arguments for exfiltrating data.
customers to use the following
targeted detection rules and
GreyMatter threat hunting packages
Ransomware File Extension: Once ransomware is deployed, it encrypts many files at once with a unique file
that are designed to identify
extension typically only associated with ransomware attacks. This rule identifies file modifications that change
specific malicious activity, such
extensions to those known to be used in ransomware operations.
45
as the use of exfiltration tools and
ransomware-specific behaviors.
These solutions help organizations
Recommended Threat Hunting Packages
detect and disrupt data theft,
unauthorized access, and
ransomware deployments, Exfiltration Tools: Identifies the use of legitimate or native tools abused by threat actors to exfiltrate data.
By detecting unusual patterns or activity from unexpected sources, this threat hunting package helps uncover
minimizing the impact of attacks
malicious intent and mitigate the risk of data breaches.
and protecting critical assets.
Proxy and Protocol Tunneling Tools: Detects unauthorized or suspicious use of proxy and tunneling software within
an environment. By analyzing endpoint telemetry, this threat hunting package identifies deviations from normal usage
patterns, enabling organizations to uncover malicious activities such as bypassing security controls, data exfiltration,
or maintaining stealthy persistence.
RMM Software: Identifies suspicious or unauthorized use of RMM software within an environment by analyzing
process events. This threat hunting package detects threat actors abusing RMM software as backdoors or for
data exfiltration by focusing on deviations from expected usage baselines, exposing malicious activity disguised
as legitimate business operations.
45

Next Steps:
A CISO’s Checklist
The biggest takeaway from 2024? Cyber threats are outpacing
and outsmarting traditional or poorly implemented security controls.
Attackers are now averaging just 48 minutes to move Armed with this knowledge, it’s time to act. Throughout
46
laterally, adapting to security controls, bypassing MFA this report, we’ve shared targeted recommendations to
in 100% of successful BEC incidents we investigated, mitigate the threats we’ve identified—but there’s more
and blending into environments by exploiting the very that organizations can do.
software and tools organizations rely on daily.
We've compiled the main takeaways every CISO needs
In 80% of breaches, attackers exfiltrated data by to know. By adopting these measures, organizations
mimicking normal activity, thereby avoiding detection. will be better positioned to minimize their exposure
Our analysis also revealed that the top cause of and outmaneuver this year’s biggest threats.
major incidents was visibility gaps.
Read on to explore our top strategies for tackling the three core issues highlighted in this report.

To Respond at Top Speed, Automate Block Initial Access by Shoring Up Foundations Disrupt and Contain Attackers with Defense-in-Depth
Automated responses excel in scenarios Implement MFA, but don’t rely on it as a silver Rotate potentially compromised credentials at
the earliest opportunity. Acting quickly prevents
where speed is critical. GreyMatter Automated bullet solution. Strengthen MFA by incorporating
attackers from exploiting valid accounts to move
Response Playbooks can reduce MTTC to as additional safeguards, such as conditional access
laterally within compromised networks.
low as three minutes when incorporated into policies, restricting access to trusted devices, and
incident response plans. shortening token expiration times.
Verify that service accounts are not overprivileged
with domain admin rights, enforce password
Alternatively, set GreyMatter Response For VPNs, implement client-based certificates and length and complexity requirements for service
Playbooks to “RQ Approved” to allow ReliaQuest access policies to restrict authentication, which accounts, and enable Advanced Encryption
Standard (AES) encryption for Kerberos to
to remediate incidents directly, significantly will reduce the likelihood of unauthorized access.
mitigate cracking.
improving MTTC and accelerating response times. Make an inventory of public-facing devices,
prioritize patching to address vulnerabilities, and
47
prepare continuity plans if critical devices must be
temporarily disconnected to prevent exploitation.
Ensure comprehensive logging and coverage for
Implement the GreyMatter AI Agent to entirely
endpoint security tools, including critical assets.
eliminate the Tier 1 and Tier 2 tasks that slow This approach will eliminate blind spots and
down analysts. enhance security monitoring, allowing for faster
Train employees to recognize social engineering threat detection.
tactics, particularly employees in IT help-desk
roles. Focus on robust training programs, testing,
and clear standard operating procedures to
Use GreyMatter Phishing Analyzer to automate
prevent successful social engineering attacks. Implement detection rules to identify the
the analysis of user-submitted phishing emails.
unauthorized use of tools or software and engage
This significantly accelerates the triage and
in frequent threat hunting to detect anomalous
remediation process for phishing email inboxes,
activities. Serious threats fly under the radar, so a
executing actions like email deletion, URL
defense-in-depth strategy is key to staying ahead.
blocking, and host isolation.
47

Our Threat Forecast for 2025 ReliaQuest Exists to Make Security Possible
ReliaQuest‘s AI-powered security operations platform,
The last year in cyber threats has emphasized again
GreyMatter, is purpose-built to confront these challenges,
Looking ahead, ransomware attacks are and again the critical importance of speed, automation,
providing customers with the capabilities they need to secure
set to surge throughout 2025, surpassing visibility, and proactiveness in modern security operations.
their environments against the threats detailed in this report.
their 2024 levels and rivaling December’s
Organizations must have the right weapons in their
record-breaking activity. To accelerate containment and response, we’ve created
arsenal to defend against attackers who are getting
our own agentic AI Agent as well as developed Automated
smarter and more efficient.
Response Playbooks that prevent cybercriminals from
gaining or maintaining a foothold—all without manual effort.
While RansomHub may dominate early in
the year, we expect BlackLock to take the
lead by Q3.
Meanwhile, we anticipate that 8–10% of
investigations will likely involve threat
actors leveraging large language model
48
The GreyMatter AI Agent autonomously handles 100% of security alerts end-to-end. Combining this capability with
(LLM) tools, alongside a projected 10%
Automated Response Playbooks has enabled our customers to achieve containment and response times as low as
increase in non-human identity (NHI)-based
3 minutes. When customers pair Digital Risk Protection with GreyMatter, they achieve 360-degree visibility into the
attacks, such as the compromise of API
threats facing their organization, both within their environment and outside it. DRP identifies threats on the open, deep,
keys, service accounts, and digital
and dark web, allowing customers to counter them before they reach their attack surface.
certificates.
GreyMatter also uses external threat data, including the latest threat actor TTPs, to develop threat hunting packages
Spearphishing, exploiting public-facing
that customers can use to proactively identify early indicators of compromise. By spotting known tactics early,
applications, and targeting external remote
customers prevent attacks from progressing.
services will remain key tactics, fueled by
rapid vulnerability exploitation, human error,
exposed credentials, and ever-expanding
attack surfaces.
With GreyMatter, ReliaQuest customers are well armed against the threats facing us in 2025 and beyond.
To see how GreyMatter can help protect your organization, visit reliaquest.com to request a demo tailored
to your environment.
48

About ReliaQuest
ReliaQuest exists to Make Security Possible.
Our agentic AI-powered security operations platform, GreyMatter,
allows security teams to detect threats at the source, and contain,
investigate, and respond in less than 5 minutes—eliminating Tier 1
and Tier 2 security operations work.
GreyMatter uses data-stitching, detection-at-source, AI, and
automation to seamlessly connect telemetry from across cloud,
multi-cloud, and on-premises technologies.
ReliaQuest is the only cybersecurity technology company that
delivers outcomes specific to each organization’s unique
49
architecture, technology, and business needs.
With over 1,000 customers and 1,200 teammates across six
global operating centers, ReliaQuest Makes Security Possible
for the most trusted enterprise brands in the world.
Learn more at www.reliaquest.com
ReliaQuest’s ShadowTalk is a weekly podcast featuring discussions Listen to the latest episodes on
on the latest cybersecurity news and threat research. your favorite podcast channels.
reliaquest.com 800.925.2159 info@reliaquest.com
Copyright © 2025 ReliaQuest, LLC. All Rights Reserved. ReliaQuest, GreyMatter, Digital Shadows, and all related logos, product and services names, designs, and slogans are trademarks or registered trademarks of ReliaQuest,
LLC or its affiliates or licensors. All other product names or slogans mentioned in this document may be trademarks or registered trademarks of their respective owners or companies. The ReliaQuest software, platform,
portal and its entire contents, features, and functionality are owned by ReliaQuest, LLC and its affiliates. These materials are protected by United States and international copyright, trademark, patent, trade secret, and other
intellectual property or proprietary rights laws. All other information presented is provided for informational purposes with no representations or warranties provided of any kind and should not be relied upon for any purpose.
ReliaQuest has no obligation to amend, modify, or update the information contained in this document in the event that such information changes or subsequently becomes inaccurate. Printed in the USA.

Endnotes
1. hxxps://nvd.nist[.]gov/vuln/search/statistics?form_type=Advanced&results_type=statistics&search_type=all&isCpeNameSearch=false&cvss_version=3&cvss_v3_metrics=AV%3AN%-
2FAC%3AL%2FPR%3AN%2FUI%3AN&cvss_v3_severity=CRITICAL
2. hxxps://www.darkreading[.]com/cyberattacks-data-breaches/canadian-authorities-arrest-snowflake-data-thief
3. hxxps://www.europol.europa[.]eu/media-press/newsroom/news/law-enforcement-disrupt-worlds-biggest-ransomware-operation
50