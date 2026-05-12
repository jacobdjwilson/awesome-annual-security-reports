analysis techniques can make it difficult to understand the full scope of an incident, but reviewing logs and browser history can help you understand the user’s actions and the source of the malware.	ƒImplement application control policies to prevent users from running unauthorized software.	ƒUse endpoint detection and response (EDR) tools to monitor for suspicious activity, such as unusual process execution or network connections.	ƒEducate users on the risks of downloading software from untrusted sources and the dangers of malvertising.	ƒConsider using a browser-based security solution that can block access to malicious websites and prevent the download of malicious files.	ƒRegularly update and patch software to protect against known vulnerabilities.	ƒMaintain a robust backup strategy to ensure that data can be recovered in the event of a ransomware attack or other data loss incident.

### Hospitality, travel, tech, and financial services stand out as heavily targeted industries

Hospitality held onto the top spot for industries targeted by phishing attacks for the second year in a row with the highest volume at 55%. It’s followed—but not closely—by travel (12%), technology (9%), financial services, and healthcare (5% each).

#### Infostealer campaign targeting hospitality customers since 2022

Since 2022, our SOC has observed an infostealing campaign targeting our hospitality customers with the goal of gaining administrative access to sites like Booking.com to commit fraud.

The campaign has developed over time, but it generally looks like this: an attacker uses a Gmail account to request information about a booking, ask for help, or to lodge a complaint. Instead of an attachment, the email contains a link to a file storage service such as Dropbox, Google Drive, and Mega.nz.

In most situations, the files in the storage service are a file archive (ZIP, RAR, etc.), which is password-protected to prevent the storage provider from scanning its contents. When the user opens the file, the archive typically contains an inflated EXE file which is an infostealer.

Though this campaign targets hospitality companies, understanding it is extremely valuable for organizations in other industries, too. As a common threat vector, infostealing malware can affect any organization.

### Bad actors trended toward script-based files for pre-ransomware initial access

JavaScript made up the highest volume of files at 39%, but we also saw lots of other scripting types, including executable (EXE—20%), LNK (12%), and VBS (7%) files.

JS and VBS are text files that receive less scrutiny from automated analysis mechanisms than EXE files. Unlike EXE, attackers can hide their functionality among benign content or by command obfuscation. By default, the native Windows program, wscript.exe, will execute these scripts when a user double-clicks the files. Attackers use this setting to their advantage, so we highly recommend changing this default setting, which can be done using a group policy object (GPO).

### Witness the power of secure-by-default to fully stop threat vectors

At the very end of 2022, we saw the beginning of a new trend toward leveraging OneNote files in attacks. In January 2023, Microsoft pushed a patch to slow down the exploitation, and ultimately implemented much stronger controls in March, virtually killing the technique.

This not only illustrates how Microsoft can eliminate a threat vector, but it also proves that if organizations adopt tight controls, they also have the power to fully stop a threat vector.

---

## Phishing threats

![Chart showing phishing incident trends]

The recent uptick in QR code phishing—or qishing—is cause for concern because it takes the activity off endpoints and puts it on mobile devices, which may not be managed with tight security controls—allowing the attacker to bypass endpoint security. We found that Microsoft’s threat intelligence can reliably identify phishing pages created with PhaaS platforms. However, Microsoft’s effectiveness in identifying these pages may have inadvertently contributed to an increase in threat actors’ use of QR codes for phishing.

Personal devices typically lack the same level of protection as endpoint devices, meaning threat actors may be able to bypass the usual security barriers more easily. It’s pivotal users become as wary of unexpected QR codes as they are URLs (or at least, as they should be).

---

## Annual spotlight

![Image representing the annual spotlight theme]

In this section, we reflect on the broader shifts in the threat landscape. The move toward "Cybercrime-as-a-Service" has lowered the barrier to entry for attackers, making sophisticated campaigns accessible to less skilled actors. We have observed that the speed at which threat actors adapt to new security controls—such as the shift from OneNote to QR codes—is accelerating. Organizations must prioritize agility in their security operations to keep pace with these evolving tactics.

---

## Looking ahead to 2024…

As we look toward 2024, our leadership team and industry experts anticipate several key developments:

- **Generative AI in Social Engineering**: We expect attackers to leverage generative AI to create highly convincing, personalized phishing lures and to automate the impersonation of employees during helpdesk calls.
- **Continued Rise of PhaaS**: The ecosystem for phishing-as-a-service will likely expand, offering more sophisticated templates and evasion techniques.
- **Focus on Identity**: Identity will remain the primary battleground. Organizations that do not implement phish-resistant MFA will find themselves increasingly vulnerable.
- **Cloud Misconfigurations**: As cloud adoption continues to grow, so will the exploitation of misconfigured services like Amazon Cognito.

---

## 2023 at Expel

2023 was a year of significant growth and learning for our team. We expanded our coverage of cloud environments and deepened our integration with leading security technologies. Our SOC analysts processed millions of events, turning raw data into actionable intelligence for our customers. We remain committed to our mission of making security accessible and effective for everyone.

---

## Reference highlights

1.  **FBI Internet Crime Report (2022)**: Statistics on BEC and financial losses.
2.  **Microsoft Security Intelligence**: Reports on PhaaS and QR code phishing trends.
3.  **CVE-2023-34362**: Vulnerability details for Progress MOVEit Transfer.
4.  **CVE-2023-4966**: Technical analysis of CitrixBleed.
5.  **Expel Blog**: [Understanding Amazon Cognito Misconfigurations](https://expel.com/blog) (Link illustrative).

---

analysis often thwarts security or IT teams’ attempts to recreate the behavior.	Attackers also use different techniques to prevent automated analysis of downloaded files, such as inflating the size of the malware. Analysts can circumvent these inflation techniques using tools like debloat, which remove the added junk bytes, allowing for manual or automated analysis and triage to understand the malware’s behavior more easily.How to protect your organization from vulnerabilities	Constantly scrutinize all external-facing assets with frequent (as operationally feasible) scans that identify vulnerabilities and configuration risks. Additionally, only enable business-essential ports and services.	Security and IT teams should collaboratively monitor external-facing infrastructure for gaps in detection and defense. Use metrics to show work completed remediating incidents and bolstering defenses: these metrics can prove valuable at the executive level to show work the security team is performing and  support requests for more resources as needed. 	This data is valuable for risk assessments and tracking risk mitigation.	Attackers can’t easily leverage vulnerabilities, but if they’re severe enough, then attackers tend to move quickly toward exploiting exposed assets. If the sheer number of vulnerabilities overwhelms your team, the Expel Vulnerability Prioritization solution can help sift through alerts, automatically surfacing the highest-risk vulnerabilities to help teams focus on the threats that matter most.Annual Threat Report 2024
Ransomware

Threat actors who target businesses with ransomware
may steal data, threaten to leak data, or further harass the
targeted organization.

Ransomware happens at the end of an attack lifecycle.
Deployment depends on other threats we talk about in
this report: identity compromise, RATs, credential theft via
infostealers, exploitable vulnerabilities, phishing, and more.
When organizations don’t monitor and mitigate these other
threats, the risk of an attacker gaining access to systems and
ransoming critical data and computer systems grows.

In the next section, we discuss trends and lessons learned
over the year about monitoring and mitigating the threat
of ransomware.

Ransomware gangs

Before we get into tactics, it’s important to mention the
gangs associated with ransomware. Active gangs change
from year to year, and over time they may dissolve, change
names, disappear, or be taken down by law enforcement
(only to then re-emerge in a different form later). Gangs
have different organizational structures, and they differ in
their preferred tactics. Therefore, the following section talks
broadly about observed tactics and information gathered
from threat intelligence.

For information on specific ransomware gangs, we
recommend following the Cybersecurity & Infrastructure
Security Agency’s (CISA’s) news publications.

Ransomware actors often buy stolen
credentials, which they use to leverage the
organization’s own VPN or a remote access
tool to access the environment.

Initial access

Throughout the year, attackers used the following primary
tactics to access victim’s environments:

1.  Leveraging initial access malware. As discussed

previously, initial access malware affords attackers a door
into an environment. Access to that door is managed by
IABs; ransomware gangs commonly buy from IABs and
often invest in the development and deployment of initial
access malware.

2.  Exploitation of software vulnerabilities on perimeter
assets. Attackers may leverage a vulnerability to let
themselves into the environment. Some ransomware
gangs prefer this tactic and use it almost exclusively.

3.  Use of compromised credentials to access the

environment. As we’ve discussed, attackers find many
ways to compromise credentials. Ransomware actors
often buy stolen credentials, which they use to leverage
the organization’s own VPN or a remote access tool to
access the environment.

Security tech provides opportunities to detect an attack at
multiple stages. However, when visibility is limited, there’s a
high risk of compromise. These low-visibility situations often
allow an attacker to act without being seen or mitigated. It’s
essential to ensure you have sufficient monitoring in place for
all assets in your environment.

Pre-ransomware initial access

IABs, which trick users into running malware, were the top
access method for ransomware actors among our customers
in 2023. To defend against this tactic, organizations should
look for mitigation techniques for the malicious use of the
following file types:

1.

JavaScript

2.  EXE

3.  LNK

In 2023, bad actors trended toward script-based files for pre-
ransomware malware. JavaScript made up the highest volume
of files at 39%, but we also saw lots of other scripting types,
including EXE files (20%), LNK (12%), VBS (7%), and others, as
illustrated by Chart 11 on page 25.

JS and VBS are text files that receive less scrutiny from
automated analysis mechanisms than EXE files. Unlike EXE,
attackers can hide their functionality among benign content
or by command obfuscation. The malicious behavior is only
observable when the file is executed by another application.

By default the native Windows program, wscript.exe, executes
these scripts when a user double-clicks the files. Attackers
use this setting to their advantage.

The power of secure by default: At the very end of 2022,
we saw the beginning of a new trend toward leveraging
OneNote files. In January 2023, Microsoft pushed a patch to
slow down the exploitation, and ultimately implemented much
stronger controls in March, virtually killing the technique.
This not only illustrates how Microsoft can eliminate a threat

24

Annual Threat Report 2024Chart 11: Top file types used to deploy pre-ransomware malware in 2023

vector, but it also shows that if organizations adopt tight
controls, they also have the power to fully stop a threat vector.

Vulnerability exploitation

While some ransomware gangs rely on initial access tools,
others access environments by targeting vulnerabilities in
external-facing appliances. The ransomware gang Play, which
uses this technique, is known to exploit vulnerabilities in the
operating system of Fortigate’s firewalls (known as FortiOS)
and Microsoft Exchange Server.

Understanding how ransomware groups leverage
vulnerabilities highlights the importance of knowing
what vulnerabilities exist in the environment. Defense
against ransomware, then, also involves defense against
vulnerability exploitation.

Access by compromised credentials

Throughout 2023, multiple ransomware groups leveraged
compromised credentials to access customer environments.
Infostealers, vulnerabilities, social engineering, and other
methods can all lead to compromised credentials.

One ransomware gang in particular, Akira, targeted VPNs
which didn’t have MFA enabled. This insecure configuration
let the threat actor try multiple methods (like brute force,
password spraying, or buying stolen credentials) to access
accounts. Once attackers identified valid credentials, they
gained initial access and then worked to compromise
the network.

Earlier in this report, we discussed The Com. These actors
used social engineering to acquire valid credentials to then
access the victim’s environment. Once they had access,
the group deployed BlackCat ransomware against the
victim’s networks.

These three initial access methods highlight where an
organization needs to focus its defenses. Defending against
encryption is too late in an attack to protect an organization,
but defending against initial access methods can help deflect
the overall threat.

25

File typePercentage010203040VBSLNKEXEJavaScriptAnnual Threat Report 202426

How to protect your organization from ransomwareTop initial access patternsSome behaviors are much more suspicious than others. Alerting on behavioral patterns like the following helps spot all kinds of malicious activity, not just ransomware gangs trying to infiltrate your network.Endpoint behavioral patternsAlert when…	A scripting process other than PowerShell (like wscript.exe) launches a PowerShell process with encoded commands.	The Microsoft HTML application host utility, mshta.exe, loads a command line and makes network connections.	Scripting processes like wscript.exe or cscript.exe do the following:		Execute a .vbs, .vbscript, or .js file.		Initiate an external network connection.		Spawn a cmd.exe or PowerShell process.	PowerShell executes a base64 encoded command and the process initiates an external network connection.Network behavioral patternsAlert when…	PowerShell makes a network connection to a rare external destination.	A high volume of Kerberos ticket requests and DNS requests for internal host names come from the same source.When building behavioral detections, start with a threat hunting-based approach to answer questions like, “How often over a 30-day period do we see this type of behavior?” or, “When we see PowerShell initiate an outbound external connection, what are the typical destinations?” Then apply your insights and enable new network-based behavioral alerts for activity that’s not normal for your organization.Other recommendations for protecting against ransomware:	Configure JavaScript (.JS, .JSE), Windows Script Files (.WSF, .WSH), and HTML for application (.HTA) files to open with Notepad. By associating these file extensions with Notepad, you mitigate a common entry point for malware.		If you can’t use Notepad, change the wscript.exe default setting so it doesn’t auto-execute scripts when a user double-clicks the files. You can do this using a group policy object (GPO).	Unregister ISO file extensions in Microsoft Windows Explorer. Once this is done, Windows will no longer recognize ISO files and double-clicking won’t result in program execution.	Don’t expose remote desktop protocol (or any other service you don’t need to) directly to the Internet.	Keep an inventory of exposed assets, and update the list and assets regularly.	Prioritize vulnerabilities to patch in your environment. Have a flexible program that allows you to patch out of band when critical vulnerabilities are identified.One last piece of advice: have a ransomware incident response (IR) plan and test it. A real-life attack isn’t the best time to test your plan. A great one emphasizes roles and responsibilities, communication, reporting, how to handle data, and how to prepare for the emotions your team will experience. Stress test your plan regularly—we recommend once a quarter—to make sure everyone knows what to do when a bad thing happens. (If you need a starting point—or just want a fun and familiar structure for your IR tabletops—our updated Oh Noes! role-playing game can help.)One last piece of advice: have a ransomware incident response (IR) plan and test it.Annual Threat Report 2024Phishing threats
Qishing and credential harvesters

You may have noticed many of the risks mentioned
in this threat report use phishing as an attack
vector. That’s because it’s a means of targeting
user identity and introducing multiple types of
malware into a victim’s environment. Similar to how
web servers must be exposed to the Internet, it’s
commonly necessary for employees to receive and
open emails to perform their jobs—and there’s no
way around it. Both web servers and emails pose
inherent risks for organizations. But, like all risk, this
must be accepted or mitigated.

One option we provide for mitigation is to triage emails
submitted by end users in customer organizations. We’re then
able to investigate whether other users in the environment
received the same email or if there are signs anywhere in the
environment that the malware was successful.

Here’s how it works: end users submit emails they deem
suspicious and the Expel Phishing Team triages and
investigates to determine if they’re malicious, unwanted
spam, or legitimate communications. Our team can action
malicious emails on behalf of our customers, and this triage
not only relieves the burden from an organization, but affords
us unique visibility into the various phishing attacks launched
against a range of organizations.

The emails triaged by our team made it past other security
tools, such as email gateways, and landed in a user’s inbox.

Phishing incidents by industry

Among the industries we serve, hospitality saw the highest
volume of targeted phishing attacks at 55%. Hospitality is
followed—but not closely—by travel (12%), technology (9%),
financial services and healthcare (tied at 5%). See Chart 12 on
the next page for a full breakdown.

W H A T   W E   S A W   I N   O U R
P R E V I O U S   A N N U A L   R E P O R T

	 16% of phishing emails submitted by customer

employees proved malicious. Of those, 88% were
credential harvesters. Malware, banking fraud,
and gift cards scams combined to account for the
other 12% of malicious emails.

	 The PDF file format accounted for 84% of the

malicious attachments spotted by our phishing
team. The remainder compromised other
historically common file types (.ZIP, .DOCX,
.XLSX). Attackers don’t weaponize the majority
of these files with an exploit. Instead, they
embed an evil link in a PDF, nest an executable in
a ZIP file, or create a macro that must be “run.”

	 Organizations that frequently correspond with

a high number of third-party vendors were most
likely to experience a successful phishing attack.

27

Annual Threat Report 2024Chart 12: Phishing attacks by industry in 2023

If you recall, we noted earlier in the report that hospitality,
technology, and financial services also made it into the list
of the top industries where we identified the most high-risk
malware and identity incidents.

Top phishing trends

Over the year, attackers most frequently used HTML/
HTM attachments to direct targeted victims to a credential
harvester (see image below for an example). In their simplest
form, these documents only contain enough code to load the
harvesting website. The sites themselves frequently have bot
protection from CloudFlare or other anti-analysis settings to
prevent review of the malicious domain.

Qishing

Throughout 2023, our analysts noted a rise in the abuse of
QR codes for phishing (aka “qishing”). Similar to other tactics,
such as AiTM, the growth of this attack was made possible by

Image 3: HTML contents of a file that loads a credential harvester

popular phishing platforms, such as DadSec/Phoenix, which
added QR code support for its clients.

While easy to use, QR codes increase the danger associated
with phishing. With a URL, a user can visit the malicious
domain using the organization’s endpoint, giving operators
the opportunity to block connections using multiple
technologies. However, with a QR code, the activity moves off
of the workstation and onto the user’s mobile device.

These attacks are, again, best mitigated by security-in-depth,
ensuring security controls exist in different stages. Not all
users will accurately identify phishing, so security or IT teams
should review suspicious login activity for users. Malicious
logins may go undetected, so security teams need to create
and review suspicious activity associated with accounts,
such as suspicious inbox rules. Security-in-depth allows for
multiple opportunities to detect malicious activity.

28

IndustryPercentage0204060MediaEntertainmentDistributorPharmaceutical & chemicalConsumer goodsHealthcareFinancial servicesTechnologyTravelHospitalityAnnual Threat Report 202429

How to protect your organization from phishingSecurity control recommendations	Make sure you’re running MFA wherever possible and using phish-resistant FIDO security keys to significantly reduce the risks associated with credential theft.	Consider deploying a secure email gateway (SEG) to monitor incoming and outgoing emails for signs of an attack.	Use email anti-spoofing controls such as DMARC, SPF, and DKIM.	Organizations using Microsoft products should also consider Microsoft’s tool for handling QR codes, which is built into Microsoft Defender for Office 365. The exact details of their capability isn’t clear yet, but we recommend keeping up to date with developments and using the most secure settings.Other recommendations for protecting against phishing threats	As we head into an election year in the United States, organizations should reinforce the importance of phishing-related training—including how to recognize suspicious or unknown links and spot common lures. Threat actors will exploit users’ political leanings and loyalties to generate convincing phishing and spear phishing attacks, likely with the help of AI.		Additionally, educate specific business units on the phishing campaigns that might target them. For example, doctors might see medical-themed lures that prey on emerging health concerns, while finance teams might encounter financial-themed campaigns, with “URGENT:INVOICES” subject lines. Recruiters may see résumé-themed phishing lures.	Organizations in heavily targeted industries should take extra security measures, including phishing training, strong endpoint defenses, and regular reviews of the environment based on user-identified malicious emails.		Triaging user-submitted emails can also help uncover compromise within an organization.	Remind users to treat QR codes with the same suspicion they treat URLs. Never scan a code unless it’s received through a trusted, verified source. Inform your employees what forms of communication you will and won’t use, and whether they should expect QR codes from leadership or internal teams.		Open-source decoding tools, such as zxing.org, also exist to help both end users and security teams alike—telling you where the QR code leads before you follow the link.Remind users to treat QR codes with the same suspicion they treat URLs. Never scan a code unless it’s received through a trusted, verified source.Annual Threat Report 2024Annual spotlight
Infostealer campaign targets hospitality

Though this campaign targets hospitality companies,
understanding it is extremely valuable to organizations in
other industries, too. As a common threat vector, infostealing
malware can impact any organization. It’s important to
consider the potential implications and impacts for your
industry. What credentials, if stolen, could harm your
organization and/or your customers?

Since 2022, we’ve observed an infostealing
campaign targeting our hospitality customers with
the goal of gaining administrative access to sites
like Booking.com to commit fraud.

Campaign overview

The campaign has developed over time, but it generally
looks like this: an attacker uses a Gmail account to request
information about a booking, ask for help, or to lodge a
complaint. There’s a strong likelihood employees will interact
with these emails—engaging with communications like this
is the employee’s job, after all. Instead of an attachment, the
email contains a link to a file storage service such as Dropbox,
Google Drive, and Mega.nz.

In most situations, the files in the storage service are a file
archive (ZIP, RAR, etc.), which is password-protected to
prevent the storage provider from scanning its contents.
When the user opens the file, the archive typically contains an
inflated EXE file, which as we outlined above, is an infostealer.

Though this campaign targets hospitality
companies, understanding it is extremely
valuable to organizations in other
industries, too.

30

How to protect your organization from infostealersWe recommend using a dedicated password manager. Password managers generate and store passwords in an encrypted format until they’re needed; they also facilitate secure password sharing among team members, preventing credential compromise, and thus helping block infostealers.Annual Threat Report 2024Looking ahead to 2024…
Thoughts from our team

Greg Notch
Chief Information Security Officer

Ray Pugh
Director, Security Operations

Tried-and-true methods historically used by attackers will
remain in use as long as they’re effective. Over the past
several years, we’ve seen clever updates to their approaches
(QR code links in phishing emails, for example), and we’re
likely to see other incremental evolutions this year. It’s unlikely
that attackers will fully pivot away from email any time soon,
but other routine forms of communication (Slack, Zoom, and
other collaboration tools) may rise in popularity and add more
diversity as vectors for attackers to achieve their objectives.

Ben Brigida
Director, Security Operations

Everyone is looking for ways to maximize profits, and
attackers are no different. I believe attackers are going to
continue to look for ways to blend attacks to achieve the most
profitable outcome. An example might include trying to extort
individuals (even after a ransom is paid), and leaving some
ransomware or backdoors to return to the victims’ systems
later. This is already starting to happen in some cases, but it’s
possible it becomes standard operating procedure for more
threat actors in the near term. It’s more important than ever to
stop the attacker before they complete their mission, because
they’ll pivot to completing a second and third mission in the
same environment.

Identity has been and will continue to be the frontier for
risk. With location and infrastructure control no longer core
places where security controls are added, access and identity
controls are the new firewall. Adding to this complexity is
the rise of LLMs and generative AI technology, making the
determination and re-validation of someone’s identity much
more difficult (for example, onboarding a remote employee or
doing a password reset in a world with deepfake video tools).
We’re just starting to see the class of problems where third
parties are given access to company systems with no real
way to validate identity.

Daniel Clayton
VP, Security Operations

Bad actors aren’t hindered by a concern for the risks
associated with AI, so their use of the technology for
cybercrime will significantly outpace security team adoption.
Adversarial use of AI will supercharge social engineering
and a new generation of spear-phishing attacks. The
election cycle and emotive geopolitical situations provide
a particularly rich breeding ground for disinformation. As
such, fast-evolving, intricately personalized, and uniquely
convincing AI-driven spear-phishing attacks will mean more
compromised credentials and stolen sensitive information
than ever before.

“Adversarial use of AI will supercharge
social engineering and a new generation
of spear-phishing attacks. The election
cycle and emotive geopolitical situations
provide a particularly rich breeding ground
for disinformation.”

31

Annual Threat Report 2024Steve Edwards
Director, Detection and Response

Oscar De La Rosa
Detection and Response Analyst

Phishing will continue to remain prevalent as both an
effective and inexpensive means for attackers to compromise
organizations. This isn’t really a technical vulnerability, but a
human vulnerability. Phishing, at its core, is simply one human
lying to another. Whether the adversary’s desired outcome is
credential harvesting or deploying malware, the crux of the
attack is convincing targets to do something they know they
shouldn’t. Since there is no Patch Tuesday for the human OS,
security leaders will need to continue to find ways to allow
people to fail safely. Hardened credentials, modern EDRs, and
closely monitoring for signs of compromise continue to be the
critical “basics” for building a security program.

Christine Billie
Detection and Response Manager

I firmly believe that looking forward through the windshield
should be prioritized for any security organization, but I’m
always wary of what can happen if we fail to periodically
check the rearview mirror. This is especially important given
the recent trend of attackers recycling “old” attack vectors
that newer analysts may not have seen yet—and are least
expecting. For example, our managed phishing service saw a
homoglyph attack this year—and it’s unlikely that many of our
customers’ security teams have seen this tactic before. We
also recently saw an attempted HTML injection attack from
a threat actor who was hoping that email subject lines would
not be sanitized or converted to plain text prior to being
ingested and parsed. While both of these are considered “old
school” attacks by seasoned security professionals, it’s a fun
opportunity for SOC managers to take trips down memory
lane to teach analysts about attack vectors that aren’t
necessarily new or trendy, but are still potentially lethal.

Last year was AI’s coming-out party. In 2024, we should
expect to see it play a larger role, as it can streamline some
of the attacker’s infrastructure. From enabling better social
engineering attacks (phishing, smishing, vishing) or just
helping with the increased deployment of malicious activity,
AI is already out there and we can see it being integrated
within more attack flows.

“From enabling better social engineering
attacks (phishing, smishing, vishing) or just
helping with the increased deployment of
malicious activity, AI is already out there and
we can see it being integrated within more
attack flows.”

I also think that adaptation for security controls and tools
should follow, helping operators with all sorts of critical tasks.
Implementation will be paramount for minimizing dislocations
for security professionals and end users. With all of that being
said, we should keep in mind the basics tenets of proper
security practices for end users. Ongoing monitoring of
conditional access, MFA, and application-review policies are
great things to always have up to date within any system.

Aaron Walton
Threat Intelligence Analyst

Perhaps they’re not as flashy as AI, but the reality is that the
main threats for 2024 are pretty much the same threats—and
the same people—from years past. Year-over-year, we see
the same groups and individuals execute attacks successfully.
These adversaries have built infrastructure that allows them
to carry out attacks, and they have the skills to pull it off.

32

Annual Threat Report 20242023 at Expel
Headlines, accolades, and research

A W A R D S
	 Fortune Cyber 60
	 2023 Deloitte Technology Fast 500™
	 CRN® Security 100
	 CRN® Channel Chiefs 2023
	 CRN® Partner Program Guide 2023

I N D U S T R Y   R E C O G N I T I O N
	 Expel named a Leader in The Forrester Wave™:
Managed Detection And Response, Q2 2023

R E S E A R C H
	 The SANS Institute - Frameworks, Tools, and

Techniques: The Journey to Operational Security
Effectiveness and Maturity

	 Enterprise Strategy Group (ESG) - Analyzing the

Economic Benefits of Expel’s Managed Detection and
Response Services

	 The Cloud Security Alliance (CSA) - Security-Enabled

Innovation and Cloud Trends

N E W S
	 Visa Enters Strategic Partnership with Expel to Help

Clients Manage Cybersecurity Risk

P R O D U C T   A N D   F E A T U R E   L A U N C H E S
	 Expel Announces New Vulnerability

Prioritization Solution

	 Expel Advances Leadership in Cloud Security with

MDR for Kubernetes

	 Expel Workbench History = unparalleled

MDR transparency

	 Okta cross-tenant impersonation: a new Expel detection

G R E A T   P L A C E   T O   W O R K ®
	 Expel Named to Five 2023 Best Workplaces Lists

by Great Place to Work®

E X P E L   Q U A R T E R L Y
T H R E A T   R E P O R T S   2 0 2 3
	 Q1 2023
	 Q2 2023
	 Q3 2023

W A N T   T O   L E A R N   M O R E
A B O U T   E X P E L ?
	 Understand how Expel helps secure and grow

your business

	 Learn how to simplify your multi-cloud security

	 Expel Demonstrates Partner-first Commitment with

with Expel

Revamped Partner Program

	 Expel Appoints Seasoned Hyper-Growth Chief Product

Officer to Leadership Team

	 See why Expel was named a Leader in The Forrester
Wave™: Managed Detection And Response, Q2 2023

	 Subscribe to our blog
	 Request a demo
	 Contact us

33

Annual Threat Report 2024Reference highlights
Sources consulted and our author

Sources

	 FBI. (2023, August 29). FBI, Partners Dismantle Qakbot
Infrastructure in Multinational Cyber Takedown. FBI.gov.

	 Gandhi, U. (2023, December 12). Protect your organizations

against QR code phishing with Defender for Office
365. Microsoft.com.

	 Santos, O. (2023, October 24.) Akira Ransomware

Targeting VPNs without Multi-Factor Authentication.
Cisco.com.

	 Siddiqui, Z., Bing, C., & Satter, R. (2023, November 15).

FBI struggled to disrupt dangerous casino hacking gang,
cyber responders say. Reuters.

	 Tidy, J. (2023, December 21). Lapsus$: GTA 6 hacker

	 IC3. (2022). Federal Bureau of Investigation Internet Crime

handed indefinite hospital order. BBC.

Report 2022. Ic3.gov.

	 Lakshmanan, R. (2023, May 13). New Phishing-as-a-

Service Platform Lets Cybercriminals Generate Convincing
Phishing Pages. The Hacker News.com.

Meet the author

Aaron Walton
Analyst, Threat Intelligence

Aaron Walton is a Threat Intel Analyst at Expel. In this
role, he monitors threat actor trends and behaviors to
support Expel’s operations. He recommends following
Expel on LinkedIn for articles published by him or
his team.

Additional contributers: David Blanton, Ben Brigida,
Daniel Clayton, Oscar De La Rosa, Jennifer Maynard,
Kyle Pellett

	 MacCarthaigh, C. (2019, December 19). Add defense in
depth against open firewalls, reverse proxies, and SSRF
vulnerabilities with enhancements to the EC2 Instance
Metadata Service. Amazon.com.

	 Microsoft Incident Response. (2023, October 25).

Octo Tempest crosses boundaries to facilitate extortion,
encryption, and destruction. Microsoft.com.

	 Microsoft Threat Intelligence. (2023, November 30).

Microsoft has detected Danabot (Storm-1044)
infections leading to hands-on-keyboard activity
by ransomware operator Storm-0216 (Twisted Spider,
UNC2198), culminating in the deployment of Cactus
ransomware. In this campaign, Danabot is distributed
via malvertising. X.

	 Microsoft Threat Intelligence. (2023, December 15).

Microsoft has identified new Qakbot phishing campaigns
following the August 2023 law enforcement disruption
operation. The campaign began on December 11, was low
in volume, and targeted the hospitality industry. Targets
received a PDF from a user masquerading as an IRS
employee. X.

	 Proofpoint. (2023, May 12). Crime Finds a Way:

The Evolution and Experimentation of the Cybercrime
Ecosystem. Proofpoint.com.

34

Annual Threat Report 2024A B O U T   E X P E L

Expel helps companies of all shapes and sizes minimize business risk. Our technology and people work together
to make sense of security signals—with your business in mind—to detect, understand, and fix issues fast.
Powered by our security operations platform, Expel offers managed detection and response (MDR), remediation,
phishing, vulnerability prioritization, and threat hunting. For more information, visit our website, check out our
blog, or follow us on LinkedIn.

expel.com/contact-us