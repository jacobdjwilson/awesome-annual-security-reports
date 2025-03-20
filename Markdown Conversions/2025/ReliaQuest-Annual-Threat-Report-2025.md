# ReliaQuest Annual Cyber-Threat Report 2025

## Table of Contents
- [Executive Summary: 2024 At A Glance](#executive-summary-2024-at-a-glance)
- [Introduction: 2024 in Review—Fast Threats Demand Faster Responses](#introduction-2024-in-reviewfast-threats-demand-faster-responses)
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
- [Why RDP Became the Tool of Choice for Lateral Movement](#why-rdp-became-the-tool-of-choice-for-lateral-movement)
- [Valid Accounts, Invalid Intent: Easy Access to Privilege Escalation](#valid-accounts-invalid-intent-easy-access-to-privilege-escalation)
- [The Adversary’s Toolkit: Post-Exploitation Essentials](#the-adversarys-toolkit-post-exploitation-essentials)
- [GreyMatter Automations for Combatting Legitimate Tool Abuse](#greymatter-automations-for-combatting-legitimate-tool-abuse)
- [Ransomware Decoded: Exfiltration Is the New Encryption](#ransomware-decoded-exfiltration-is-the-new-encryption)
- [Exfiltration Outpaces Encryption in Modern Breaches](#exfiltration-outpaces-encryption-in-modern-breaches)
- [Ransomware in 2024: Increased 11.9%, Hit New Highs](#ransomware-in-2024-increased-119-hit-new-highs)
- [GreyMatter Detections and Automations for Combatting Ransomware](#greymatter-detections-and-automations-for-combatting-ransomware)
- [Next Steps: A CISO’s Checklist](#next-steps-a-cisos-checklist)
- [About ReliaQuest](#about-reliaquest)
- [Endnotes](#endnotes)

# ReliaQuest Annual Cyber-Threat Report 2025

## Executive Summary: 2024 At A Glance

**Initial Access Techniques**

- Phishing Top Initial Access Technique for the 2nd Year Running
- 30% Of Phishing Messages Involved Credential Harvesters

**Malware and Threat Actors**

- SocGholish Top Malware Thanks to New Python Tactics
- Microsoft Teams Abused for Social Engineering by Black Basta
- AsyncRAT Rises From 4th to 2nd Place Among Top Malware Threats
- Lumma Listings on Criminal Marketplaces: 478,000

**Incident Metrics and Breach Details**

- 3 Minutes Lowest Mean Time to Contain (MTTC) Using Automated Response Playbooks
- 85% Of Incidents Involved Compromised Service Accounts
- Inadequate Logging Top Cause of Breaches
- Two-Thirds Of Critical Hands-on-Keyboard Incidents Involved Legitimate Software
- 48 Minutes Average Time from Initial Access to Lateral Movement, or “Breakout Time”
- 45% Of Hands-on-Keyboard Intrusions Began with Abuse of External Remote Services Like VPNs
- 100% Of Deployed MFA Controls Bypassed via Session Hijacking in Successful Business Email Compromise (BEC) Attacks
- 1 in 4 Active Intrusions Started with Exploitation of Public-Facing Applications
- United States Region with the Most Targeted Victims
- Manufacturing & Professional Services Sectors with the Most Targeted Victims
- Fastest Exfiltration Time: 4 hr 29 min
- 80% Of Breaches Featured Exfiltration vs 20% with Encryption
- 5,253 Organizations Named on Ransomware Data-Leak Sites

## 3 Recommendations Organizations Can’t Afford to Ignore

1.  **Barricade Common Entry Points:** Phishing, Drive-By Compromise, Public-Facing Assets, and External Remote Services

    -   Phishing and drive-by compromise were the top initial access methods, while public-facing assets and internet-facing external remote services fueled active intrusions.
    -   Mitigate these risks by securing remote services (e.g., with client-based certificates) and monitoring public-facing assets.
    -   Patching promptly is key; attackers are moving faster than ever, fueled by an abundance of available credentials.

2.  **Incorporate AI and Automation into Security Operations**

    -   Attackers are adopting AI and automation to supercharge common attacks. That means it’s no longer optional for organizations to use AI and automation to their own advantage.
    -   When integrated into a security operations platform, these technologies can help contain threats rapidly, drive down response times, and allow security teams to focus on tackling more complex challenges.
    -   Agentic AI, which can autonomously handle alerts end-to-end, shows particular promise for SecOps.

3.  **Eliminate Blind Spots:** Deny Attackers Any Opportunity

    -   Most “hands-on-keyboard” breaches resulted from insufficient logging and unmanaged devices.
    -   Manage your attack surface and eliminate blind spots by deploying an endpoint security solution across all assets.
    -   Enable detailed logging for all devices, including endpoints and servers, to capture user activity, system changes, and network traffic.
    -   Review log retention periods for hot and cold storage and establish clear procedures for retrieving cold storage logs during investigations.

## Introduction: 2024 in Review—Fast Threats Demand Faster Responses

In 2024, speed became more important than ever in defending against cyber threats.

-   **48 Minutes:** Attackers are moving at unprecedented speeds—last year, upon gaining initial access, they achieved lateral movement in an average of 48 minutes and managed to exfiltrate data in as little as 4 hours.

Attackers are also getting better at adapting to and evading the latest security controls, making the adoption of AI and automation imperative for organizations. Using AI and automation to tackle initial access attempts not only strengthens defenses but also empowers analysts to focus on what matters most: detecting and investigating the stealthiest and most impactful intrusions.

Though attackers are moving faster, they’re still using tried-and-tested methods like phishing to achieve initial access. They cast a wide net, indiscriminately targeting organizations with minimal effort and often causing significant damage. The year’s high count of disclosed vulnerabilities provided cybercriminals with entry points, while software suppliers remained a top target as a way to infiltrate organizational networks.

Ransomware and extortion remained critical threats compared to 2023, but the dynamics have shifted. Affiliates splintered into smaller groups, while leaked ransomware source code on cybercriminal forums sparked a wave of new attackers on the scene, with many focused entirely on data exfiltration. The result is a more fragmented, but no less dangerous, ransomware ecosystem.

In a world of accelerated attacks, automation is the ultimate ally for defenders. ReliaQuest customers using Automated Response Playbooks in 2024 saw a dramatic improvement in response times, with the fastest mean time to contain (MTTC) cyber threats as low as 3 minutes. In comparison, customers yet to implement Automated Response Playbooks reported an average MTTC of 6.3 hours.

Additionally, in August 2024, ReliaQuest launched its first-of-its-kind AI agent for security operations, further speeding up containment of threats with better accuracy and consistency. By seamlessly handling routine Tier 1 and Tier 2 tasks and executing response actions securely, the GreyMatter AI Agent eliminates errors and delivers unparalleled efficiency in accelerating remediation times, allowing security teams to upskill by focusing on more critical tasks.

By automating 100% of the investigation process—including data aggregation, analysis, and response—the GreyMatter AI Agent has reduced the average MTTC for ReliaQuest customers to less than 5 minutes.

At ReliaQuest, we remain committed to helping organizations strengthen their security posture and take control of their defenses.

Our Annual Cyber-Threat Report presents an in-depth analysis of the most critical cyber threats observed from January 1 to December 31, 2024. Find out the emerging tactics, techniques, and procedures (TTPs) employed by adversaries and benchmark your security defenses against our findings to identify key areas for improvement.

Security leaders can use these findings to refine their cybersecurity strategies, address coverage gaps, and enhance employee awareness of evolving threats.

## Inadequate Logging Responsible for Most Breaches in 2024

Our analysis of 2024 customer breaches revealed five critical security control failures at the core of these incidents. Neglecting or underestimating these foundational security practices leaves organizations exposed—regardless of how sophisticated or varied an attacker’s methods may be. Addressing these weaknesses within networks is essential to avoid becoming the next target.

**Five Critical Security Control Failures**

-   **Unmanaged Devices:** Devices without security controls like endpoint protection or monitoring agents create security gaps, providing attackers with open pathways throughout networks.
-   **External Exposure:** Vulnerabilities in internet-facing devices serve as entry points for attackers to infiltrate the network.
-   **Insufficient Logging:** Insufficient monitoring or logging leaves parts of the system vulnerable, making it impossible to detect or investigate malicious activity.
-   **Insecure VPN:** VPNs lacking essential protections like multifactor authentication (MFA) or device-based certificates allow attackers to exploit stolen credentials and gain network access.
-   **Help-Desk Procedural Flaws:** Weak help-desk protocols make organizations easy targets for social engineering attacks, with 14% of breaches in 2024 involving social engineering for initial access or privilege escalation.

Before advancing to sophisticated response strategies, fortifying foundational defenses is critical. Ensure comprehensive endpoint security coverage—prioritizing critical assets— and implement robust logging to maintain full visibility across the network.

To counter the risks of social engineering and stolen credentials, enforce strong identity controls like device-based certificate authentication. Bolster these efforts with regular penetration testing, including social engineering scenarios, to uncover and address procedural gaps—particularly in help-desk operations. Though basic, these steps form the bedrock of a resilient security posture.

## Breaking In: The Trends Shaping Initial Access Tactics

Initial access is the critical first step of every cyber attack.

It’s the moment attackers breach any configured defenses to gain a foothold in a network and set their plans into motion. In this section of the report, we analyze key findings from GreyMatter customer alerts to reveal how attackers attempted to gain network access and which techniques proved most effective.

**Read On To** find out the tactics adversaries are using to compromise systems, learn how to defend against these threats, and discover how ReliaQuest empowers enterprises to stop incidents before they escalate into full-scale breaches.

**First...** We'll examine phishing and business email compromise (BEC) attacks, which are increasingly bolstered by advanced tactics like bypassing MFA and abusing Microsoft Teams for social engineering.

**Then...** We’ll dissect the initial access techniques with the highest success rates, including targeting external remote services (boosted by a 250% surge in initial access brokers [IABs] offering VPN access), compromising cloud accounts, and conducting voice phishing attacks.

**Finally...** We’ll review the top malware shaping today’s threat landscape, with “SocGholish” leading the charge.

## Old Habits Die Hard: Attackers’ Most Frequent Initial Access Techniques

The consistency in top-ranked initial access techniques from 2023 to 2024 highlights their effectiveness and reflects attackers’ strategy of indiscriminately targeting a wide pool of victims. Phishing and drive-by compromise remain go-to methods, powered by the scalability and affordability of phishing-as-a-service (PaaS) and malware-as-a-service (MaaS) offerings.

These services allow attackers to flood inboxes with phishing campaigns or lure victims to malicious websites through manipulated search engine results.

While most initial access attempts are blocked early, when successful, these broad-spectrum attacks can pave the way for more advanced threats, highlighting the importance of understanding their mechanics.

Through our analysis of phishing emails reported to the GreyMatter Phishing Analyzer, we uncovered:

-   The most prevalent types of malicious email sent
-   The trigger words used to boost email open rates
-   The tactics designed to trick recipients into clicking malicious links

We’ll also look at one of the top concerns for CISOs—BEC—by demonstrating how attackers leverage simple phishing techniques to bypass MFA and execute these high-impact attacks.

Finally, we’ll explore adversaries' weaponization of a trusted communication platform to worm their way into networks.

| Technique                     | 2023  | 2024  |
| :---------------------------- | :---- | :---- |
| Phishing with Link            | 25%   | 33%   |
| Drive-By Compromise          | 24%   | 22%   |
| Phishing with Attachment     | 9%    | 19%   |
|Replication via Removable Media|       |       |

## Phishing Trends: The Tactics Honing Cybercrime’s Most Reliable Weapon

To expose the tactics behind the number-one cyber threat facing enterprises today, we turned to the GreyMatter Phishing Analyzer:

A tool designed to automate the triage of employee-reported phishing emails, enabling faster identification and remediation of malicious activity.

This data is collected from phishing emails that evaded detection by email security gateways and provides insight into adversaries’ phishing techniques.

Data from the GreyMatter Phishing Analyzer revealed that nearly 30% of phishing messages that made it past traditional email security tools involved credential harvesters, often disguised as fake Microsoft login portals.

We also identified any financial-themed keywords attackers used to create a sense of urgency and the trusted platforms they abused to make phishing campaigns appear more legitimate. Knowing what to look for in phishing emails not only helps predict attacker strategies but also sharpens employee training, turning your workforce into a powerful first line of defense against phishing attacks.

**Nearly 30% of Reported Phishing Emails Contained Credential Harvesters**

-   **Credential Harvesters:** Dominated as the most reported category of malicious emails, with fake Microsoft login portals being the most common type. These emails lure victims to fraudulent websites designed to steal credentials, often to lay the groundwork for larger attacks like BEC. Enhanced by AI, credential harvesting emails now feature much more polished language, fewer errors, and highly convincing designs, making them an increasingly effective and scalable weapon for cybercriminals.
-   **Scam Emails:** Crafted to solicit money or extract confidential employee information, scam emails were also widespread in 2024.
-   **Malware-Laden Emails:** Attackers also sent a significant volume of malware-laden emails containing attachments or URLs to deploy malicious files upon download.
-   **Reconnaissance Emails:** Another common type of email sent was single-word or blank emails—known as reconnaissance emails—which are used to verify whether an account is active (i.e., no bounce-backs are received) or to gauge the likelihood that the inbox owner might respond.

**URGENT: Keywords That Hook**

Attackers use deceptively urgent language to manipulate victims into engaging with phishing emails.

They understand that a sense of urgency often overrides caution, causing recipients to act hastily without evaluating risks.

Financial keywords like “payment,” “invoice,” and “statement” dominated phishing email subject lines and filenames last year.

This tactic is particularly effective because phishing emails that mimic financial statements blend seamlessly into routine tasks, like processing invoices or reviewing account statements, catching users off guard.

_Training end users to pause, verify suspicious emails, and think critically before taking action is key to disrupting attackers’ strategies and reducing the success of phishing attempts._

**Figure 1: Top subject line keywords**

1.  Invoice
2.  Order
3.  Payment
4.  Request
5.  Receipt
6.  Purchase
7.  Statement
8.  Tax
9.  Transfer
10. Bank
11. Account
12. Remittance

**Figure 2: Top filename keywords**

1.  Request
2.  Invoice
3.  Account
4.  Payment
5.  Required
6.  Review
7.  Action
8.  Reminder
9.  Notification
10. Order
11. Update
12. Document
13. Ref
14. PDF
15. Please
16. Notice
17. Business
18. Password
19. Sign
20. Report

**Attackers’ Favorite Email Providers and File-Sharing Platforms**

Free email providers like Gmail and file-sharing platforms like Dropbox and Docusign were among the top tools used in phishing campaigns last year.

These platforms are highly trusted and widely used in business, making it easy for attackers to exploit the trust users place in them.

Phishing emails leveraging these tools appear more genuine and are therefore harder to spot.

Free email services allow attackers to remain anonymous by enabling them to quickly create new accounts and replace blocked ones, while file-sharing platforms are perfect for hosting malicious files or hiding phishing links.

To counter these tactics, businesses must fine-tune their email security tools to catch suspicious activity that hides behind a veil of legitimacy. Employees must also carefully scrutinize links or emails from trusted platforms, as attackers rely on this very trust to bypass defenses and infiltrate organizations.

**Figure 3: Top sender domains**

-   fakedEmail.com

**Take Action Against Phishing**

-   Rather than just blocking specific file types, configure email security tools to inspect the contents of HTML files for malicious links, scripts, or QR codes.
-   Configure email security tools to flag unusual activity from trusted platforms like free email providers and file-sharing services.
-   Use banners to highlight attention-grabbing terms like "payment," "invoice," and "statement" to educate employees on common phishing tactics.

## Session Hijacking Bypassed MFA in Every Successful BEC Incident in 2024

BEC is one of the most dangerous methods attackers use to achieve their financial objectives.

These attacks often start with a phishing email—frequently sent from a compromised partner—containing a link to an attacker-controlled website. This site acts as an adversary-in-the-middle (AiTM), intercepting MFA requests and session tokens from the legitimate login portal.

With the stolen session tokens, the attacker can authenticate to the service without needing credentials or access to the MFA-enrolled device, effectively bypassing both.

To stay under the radar while executing their strategies, attackers often use commercial VPNs to mask their activities:

-   Express VPN
-   SurfEasy VPN
-   Private Internet Access VPN
-   Nord VPN
-   Hide My Ass VPN
-   Surfshark VPN

The combination of a high success rate and devastating impact makes BEC a top security concern for organizations.

By analyzing real-world compromises of corporate employee email accounts, we’ve identified the key tactics attackers rely on, what makes them so successful, and, most importantly, the steps defenders must take to stop them.

**Here are our key takeaways**

-   **MFA Isn’t Foolproof:** In every incident where MFA was configured, attackers managed to bypass it by stealing session tokens through AiTM phishing. Session token interception is now a standard feature in modern phishing toolkits, reducing the level of technical expertise required to bypass MFA.
-   **Trust Is a Weapon:** 9 out of 10 phishing emails came from hacked accounts at trusted partner organizations, exploiting established relationships to successfully deceive targets.
-   **Attackers Hide Their Tracks:** After hijacking a session, attackers used VPNs to conceal their location, allowing them to bypass location-based detections and evade regional access-control policies.
-   **Compromised Accounts Spread the Attack Internally:** In 80% of cases, compromised accounts were used to send phishing emails to other employees within the same organization.

**Figure 4: How AiTM phishing bypasses MFA and steals session tokens**

1.  User enters their password into phishing site
2.  Phishing site forwards the credentials to legitimate site
3.  Legitimate site sends MFA screen in response
4.  Phishing site displays MFA prompt from legitimate site to the user
5.  User completes MFA authentication
6.  Phishing site forwards MFA response to legitimate site
7.  Legitimate site issues a session cookie
8.  Phishing site redirects the user to another page

**Business Email Camouflage**

In February 2024, we identified a compromised email account belonging to a customer in the information sector. The account had been compromised after a user inadvertently provided their credentials in response to a phishing email impersonating a legitimate IT consulting company.

We promptly informed the customer’s security team, who contacted the user to verify the activity. However, the threat actor, posing as the user, misled the security team by claiming the activity was legitimate.

We immediately followed up with the customer to confirm that the account had been compromised and that the security team had unknowingly been communicating with the threat actor. The attacker’s access was swiftly revoked, and the credentials for the compromised account were changed.

**Take Action Against BEC**

-   Train users to recognize common phishing keywords, understand procedures for reporting suspicious emails, and be aware that even trusted partner email accounts can be compromised and used for phishing attacks. Incorporate internal phishing scenarios into security awareness training to help employees effectively identify and respond to these threats.
-   Block anomalous top-level domains (TLDs), such as “.ru,” “.xyz,” and “.ly,” as these TLDs are commonly used to host credential harvesters.
-   Implement conditional access policies to block authentication from noncompliant devices. Deploy phishing-resistant MFA, such as Fast IDentity Online (FIDO), for administrators or other high-risk accounts. Additionally, shorten session timeouts for Microsoft 365 to minimize the window of opportunity for attackers to exploit stolen session tokens and maintain access.

## Social Engineering: How Attackers Weaponize Microsoft Teams

**Black Basta Exploits Microsoft Teams for Initial Access**

Throughout 2024, ReliaQuest observed the ransomware group “Black Basta” employing a new social engineering tactic that leverages Microsoft Teams for initial access.

By compromising legitimate Microsoft Entra ID tenants or creating fraudulent ones, the group impersonates IT support or help-desk staff to deceive targeted users into engaging with malicious Teams messages.

Black Basta typically begins the attack by spamming users with hundreds of phishing emails. Shortly after, the attackers follow up with either a phone call or a Teams chat message (see Figure 5).

These messages often originate from external accounts with display names like “Help Desk” or “Support Team,” intentionally crafted to appear both legitimate and urgent to increase the likelihood of user interaction.

Once attackers establish contact, they manipulate victims into downloading remote monitoring and management (RMM) tools, such as Quick Assist or AnyDesk, under the guise of providing support sessions. These tools grant attackers the ability to install and execute malicious files, facilitating initial access to the organization’s network.

In some cases, attackers have also been observed persuading users to download malicious files themselves—such as scripts or executables—via QR codes, further expanding their arsenal of social engineering techniques.

**Figure 5: Sample external Microsoft Teams message request**

![Image description: Sample external Microsoft Teams message request from microsoft[.]com]

**Manipulating Trust: Social Engineering Through Familiar Platforms**

As this is a relatively new technique, most organizations have yet to take appropriate defensive measures. Unlike phishing, which is commonly mitigated with security controls and user training, this approach targets less-secured communication channels where users are more likely to engage with malicious activity.

We predict with high confidence that this technique will gain popularity among cybercriminals, largely due to the ease of creating new Microsoft Entra ID tenants, making these accounts disposable and easily replaced if blocked. This tactic highlights why social engineering remains one of the most effective forms of initial access.

_By exploiting human trust in familiar platforms, threat actors significantly increase their chances of success compared to traditional phishing techniques._

As Black Basta and other threat groups continue to innovate, organizations must prioritize addressing these vulnerabilities. Implementing strict controls on external Teams communication, monitoring for anomalous activity—such as messages originating from unexpected locations or using suspicious naming conventions—and providing robust user training are critical. Without these preventative measures in place, these increasingly sophisticated social engineering campaigns are likely to be successful.

**Take Action Against Microsoft Teams Social Engineering**

-   Limit Microsoft Teams messaging to approved external tenants only to block malicious actors from impersonating legitimate organizations.
-   Train employees to identify fake support messages, avoid unverified downloads, and recognize QR code scams on platforms like Teams and Slack.
-   Deploy advanced email filtering solutions, such as email security gateways, spam filtering, and advanced threat protection for email, to detect and block mass spam campaigns before they reach user inboxes.

## GreyMatter Automations for Combatting Email Attacks

To counter the evolving tactics behind phishing, BEC, and social engineering attacks, ReliaQuest offers its customers a proactive defense strategy through its Automated Response Playbooks. These Playbooks automatically contain and respond to threats, significantly improving MTTC and minimizing potential damage.

Additionally, GreyMatter offers out-of-the-box and custom threat hunting packages that are built to identify specific attacker techniques and behaviors.

By leveraging the end-to-end automation capabilities of GreyMatter, organizations can detect, respond to, and neutralize threats in minutes.

**Recommended Automated Response Playbooks**

-   **Block Domain:** Prevents access to a specific malicious domain, which disrupts phishing campaigns, malware delivery, and command-and-control (C2) communications.
-   **Block Email Domain:** Blocks emails originating from malicious domains, reducing phishing attempts and preventing attackers from using compromised or fake domains to target users.

**Recommended Threat Hunting Packages**

-   **Phishing—Microsoft Teams:** Identifies malicious messages from external domains in Microsoft Teams to detect and block phishing attempts that deliver credential-harvesting links or malicious files through Teams. By monitoring these messages, customers can stop attackers from using tools like “TeamsPhisher” before users interact with harmful links, reducing the risk of compromised accounts or data breaches.
-   **Phishing—Spearphishing Attachments:** Detects spearphishing attachments with uncommon but business-relevant file extensions. This threat hunting package leverages telemetry from email gateways and endpoints to identify malicious emails that mimic legitimate communications. This allows customers to quickly spot and block these threats, minimizing attackers’ foothold in the network and reducing the risk of compromise.
-   **Hygiene—MFA Modifications:** Monitors unauthorized actions, such as threat actors registering new MFA devices or tricking users into resetting their MFA. By auditing MFA changes, customers can ensure MFA is implemented correctly, confirm that changes follow proper procedures, and quickly identify suspicious activity.

## Critical Entry Points: VPN and Voice Phishing Among Most-Successful Techniques

In 2024, GreyMatter continued to serve as a critical line of defense, swiftly detecting and containing the vast majority of initial access attempts observed. Among all the attempts analyzed in the previous section, only a tiny fraction—just 0.02%—managed to bypass its defenses.

While these successful techniques represent only a very small proportion, they demand close attention, as they allowed threat actors to engage in hands-on-keyboard activity, taking real-time control of compromised systems.

In this section, we focus on the critical 0.02% of successful attempts, examining how attackers used social engineering tactics in addition to exploiting external services, public-facing applications, cloud infrastructure, and trusted relationships.

We’ve also included real-world examples to illustrate the damage these techniques can inflict and outlined clear steps to mitigate these risks.

By prioritizing defenses against these methods, organizations can significantly reduce the risk of attacks escalating into lateral movement, privilege escalation, or data exfiltration.

**Figure 6: Successful initial access methods in 2024**

-   External Remote Services: 45%
-   Public-Facing Applications: 23%
-   Phishing with Voice: 14%
-   Trusted Relationship: 9%
-   Cloud: 9%

## Abuse of External Remote Services Led to 45% of Hands-on-Keyboard Intrusions

Last year, threat actors were most successful in gaining network access via external remote services like VPN portals, Remote Desktop Protocol (RDP), and virtual desktop infrastructure (VDI).

These trusted services act as gateways to an organization’s internal network, allowing attackers to slip past traditional perimeter defenses and gain direct access to sensitive systems and data.

Once inside, adversaries exploit the trust inherent in these services to operate under the radar, carrying out data theft, lateral movement, or ransomware attacks—all while evading detection. In some cases, they also plant backdoors for future intrusions.

External remote services rely on valid account credentials for authentication, but attackers can easily overcome this hurdle by:

-   Brute-Forcing Passwords
-   Mining Data Breaches
-   Purchasing Credentials from Online Marketplaces

IABs are the middlemen in this ecosystem, selling stolen credentials—often obtained through information-stealing malware (infostealers)—to various threat actors, including ransomware affiliates, so they can launch devastating attacks with ease.

Once exposed, data may be leaked or sold online, leaving organizations to face severe reputational and regulatory consequences.

_The rise in attacks targeting external services has fueled a growing demand for accesses, and IABs are meeting this demand at premium prices:_

-   IAB listings offering access via VPNs surged by 250% between 2023 and 2024.
-   The average “buy now” price for these listings climbed 46%, increasing from $2,370 to $3,455.

While all industries are targeted for initial access, certain sectors are more heavily sought after than others.

Manufacturing, for example, is a prime target due to its reliance on legacy systems, extensive use of remote access, and prioritization of operational continuity over credential hygiene best practices. If IABs can easily infiltrate a network in a particular industry, they are more likely to target other organizations in the same sector, assuming they have the same weaknesses in security practices.

**Figure 7: IAB listings in 2024 by sector**

-   Manufacturing: 74%
-   Construction: 63%
-   Retail: 55%
-   Education: 39%
-   Finance: 37%
-   Software: 33%
-   Health Care: 33%
-   Government: 28%
-   Business Services: 22%
-   Media & Internet: 21%

**Take Action Against VPN Attacks**

-   Implement device-based certificate authentication for VPNs to verify devices before they connect.
-   Combine this with MFA for an added layer of security against unauthorized access.
-   Enforce conditional access policies for VPN authentication, such as location and device compliance.

## 23% of Active Intrusions Initiated via Exploitation of Public-Facing Applications

Between 2023 and 2024, adversaries targeting public-facing applications increased by 3%, a trend highly likely fueled by the 2,000-plus critical vulnerabilities identified last year.1

These critical vulnerabilities—which are remotely exploitable, require no privileges or user interaction, and are characterized by low complexity—are an attractive opportunity for attackers. With minimal effort, a single exploit can breach multiple organizations, delivering significant returns on investment for cybercriminals.

Although fewer critical vulnerabilities were identified in 2024 compared to the 4,000-plus seen in 2023, a surge in proof-of-concept (PoC) exploits likely leveled the playing field, giving lower-skilled attackers more opportunities to strike. PoC exploits are easily deployable bits of code designed to demonstrate vulnerabilities, making it easier to test or exploit security weaknesses.

In 2024, PoC exploits were released for all three of the most-exploited vulnerabilities, turning opportunistic attacks into focused campaigns. With these ready-made tools in hand, attackers—regardless of skill level—had a clear and easy path to exploitation.

**Most Exploited Vulnerabilities of 2024**

-   CVE-2024-1708 affecting ConnectWise ScreenConnect
-   CVE-2024-50623 impacting Cleo Harmony, VLTrader, and LexiCom
-   CVE-2024-3400 targeting Palo Alto GlobalProtect

_When PoCs are released, the clock starts ticking; attackers rush to exploit vulnerabilities at scale before organizations can respond. To stay ahead, organizations across all sectors must prioritize securing external-facing assets, as these are prime targets for rapid, opportunistic attacks the moment exploits become available._

The information sector emerged as the primary target for public-facing application attacks, largely due to its reliance on software that often inadvertently leaves critical assets exposed, like customer service platforms, hosting infrastructure, and interconnected systems.

**LockBit Finds a Key in ScreenConnect**

In February 2024, a “LockBit” ransomware affiliate successfully exploited CVE-2024-1708 to gain access to a customer's on-premises ConnectWise ScreenConnect server.

Using this access, the adversary executed a ransomware encryptor via ScreenConnect, impacting numerous hosts within the environment.

The affected hosts had adequate visibility through logging and endpoint security tools, enabling a swift and effective response that ultimately prevented a successful attack.

**Take Action Against Exploitation of Public-Facing Applications**

-   Maintain an accurate inventory of public-facing software like VPNs, firewalls, and file-transfer software. Minimize the external attack surface by disabling unused services or applications and limiting the public exposure of systems to only those that are essential for business operations. For devices that need to be externally facing, enforce strict access controls and incorporate a web application firewall (WAF) to monitor and block malicious requests.
-   Prioritize patching these critical systems and establish fallback plans to mitigate risks when patching isn’t immediately possible.
-   Equip internal devices and servers relying on this software with adequate logging and security tools to enhance visibility and enable swift responses to threats.

## Voice Phishing Behind 14% of Breaches

Social engineering is far from new, but it remains one of threat actors’ most effective tools, allowing them to exploit human trust to infiltrate organizations.

Attackers frequently deceive users into downloading malicious software or manipulate IT help desks into resetting credentials and disabling MFA.

To deceive help-desk personnel, attackers gather employee information such as full names, addresses, and Social Security numbers.

Voice phishing is especially concerning.

It circumvents all technical defenses, instead directly targeting an organization’s people. Employees tricked by these tactics not only risk exposing sensitive information