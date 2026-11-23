analysis tools often fail to provide complete context, but a manual review of browser history or logs can quickly clarify the root cause.	ƒEducate users on malvertising. Show them what search engine ads look like, and teach them to scroll past the ads to the search results (or, better yet, use an ad blocker).	ƒMonitor download activity. Endpoint telemetry often captures the exact URL where a file was downloaded, which can reveal whether the user clicked an ad or visited a legitimate site.	ƒAdvise employees to be extremely careful with cracked software. Remind them of the risks associated with downloading it—not just to the individual, but to the entire organization.	ƒDeploy EDR and configure it to block execution of files from unusual locations, such as temporary directories or user profile folders.	ƒDeploy an ad blocker across organization-managed devices to prevent users from accidentally clicking on malicious search ads.Annual Threat Report 2024

File types

Among the files our SOC observed in 2023 associated
with malicious activity, script-based files were heavily
represented. JavaScript made up the highest volume at 39%,
followed by executables (EXE—20%), LNK (12%), and VBS
(7%). See Chart 11 for the complete breakdown.

JS and VBS are text files that receive less scrutiny from
automated analysis mechanisms than EXE files. Unlike
EXE, attackers can hide their functionality among benign
content or by command obfuscation. By default, the native
Windows program, `wscript.exe`, will execute these scripts
when a user double-clicks the files. Attackers use this
setting to their advantage, so we highly recommend changing
this default setting, which can be done using a Group Policy
Object (GPO).

Chart 11: File types observed by the Expel SOC

Let’s talk about OneNote files: At the very end of 2022, we
saw the beginning of a new trend toward leveraging OneNote
files in attacks. In January 2023, Microsoft pushed a patch
to slow down the exploitation, and ultimately implemented
much stronger controls in March, virtually killing the
technique. This not only illustrates how Microsoft can
eliminate a threat vector, but it also proves that if
organizations adopt tight controls, they also have the power
to fully stop a threat vector.

24

File typePercentagePercentage010203040OtherHTM/HTMLZIP/RARVBSLNKINGEXEJSAnnual Threat Report 202425

How to protect your organization from computer-based threats	ƒChange the default file association for script files. By default, Windows opens script files (like JS, VBS, and WSF) using Windows Script Host (`wscript.exe` or `cscript.exe`), which executes the script when double-clicked. You can change this behavior so that these files open in a text editor (like Notepad) instead. This simple change stops many drive-by script attacks dead in their tracks.		Deploy this change using a Group Policy Object (GPO) or mobile device management (MDM) solution across your environment.	ƒMonitor PowerShell execution. Attackers frequently use PowerShell to download payloads, execute commands, or perform discovery. Enable script block logging (`Event ID 4104`) and module logging to capture the full content of PowerShell commands. Monitor for suspicious patterns, such as encoded commands (`-EncodedCommand`), obfuscated strings, or downloads from untrusted URLs.	ƒImplement application control. Use tools like Microsoft Defender Application Control (WDAC) or AppLocker to restrict which applications are allowed to run on endpoints. This prevents unauthorized software—including infostealers and RATs—from executing, even if a user manages to download it.	ƒMaintain a vulnerability management program. Regularly scan your environment for missing patches and known vulnerabilities, prioritizing systems exposed to the Internet (like VPN gateways, email servers, and web applications). Establish a rapid patching cadence for critical vulnerabilities, especially zero-days under active exploitation.	ƒMonitor endpoint telemetry for living-off-the-land binaries (LotLBs). Attackers love using legitimate administrative tools already present on the system (like `rundll32.exe`, `regsvr32.exe`, or `certutil.exe`) to execute malicious payloads or download files. Create detections for anomalous command-line arguments passed to these binaries.	ƒImplement network segmentation. Limit lateral movement by segmenting your network into zones, isolating critical assets (like domain controllers and database servers) from general user workstations. Require strict access controls between segments to prevent an attacker from pivoting easily after compromising a single endpoint.Annual Threat Report 2024Phishing threats
Trends, qishing, and industry targeting

Phishing remains one of the most reliable and
cost-effective initial access vectors for threat actors.
In 2023, we saw phishing incidents triple as a
percentage of overall alerts investigated by our SOC,
moving from 2% in 2022 to 6% in 2023.

While phishing campaigns often culminate in identity
compromise or malware execution, we track dedicated
phishing submissions and email-borne threats to understand
how adversaries are attempting to trick users.

Industry targeting

Hospitality held onto the top spot for industries targeted by
phishing attacks for the second year in a row, accounting for
55% of targeted phishing volume. It was followed by travel
(12%), technology (9%), financial services (5%), and
healthcare (5%). See Chart 12 for the breakdown.

Hospitality organizations are uniquely vulnerable because
their business models rely on open communication channels
with the public, making it easy for attackers to pose
as customers, vendors, or partners seeking assistance or
lodging complaints.

Chart 12: Phishing targets by industry vertical

W H A T   O T H E R   T R E N D S
D I D   W E   S E E ?

	ƒ **QR code phishing (qishing)** surged in 2023.
Attackers embedded malicious QR codes in PDF
attachments or image files within emails, forcing users
to scan them with personal mobile devices. This
technique successfully bypassed traditional email
gateway filters and endpoint security controls.

	ƒ **Business Email Compromise (BEC)** tactics
continued to evolve. Attackers increasingly leveraged
compromised accounts to send internal phishing emails
or reply-chain attacks, making the messages appear
highly legitimate to recipients.

	ƒ **AI-generated phishing content** became more
prevalent. Phishing emails featured better grammar,
more natural phrasing, and convincing context tailored
to specific roles within an organization, reducing the
tells that users previously relied upon to spot scams.

26

IndustryPercentagePercentage0102030405060OtherHealthcareFinancial servicesTechnologyTravelHospitalityAnnual Threat Report 202427

How to protect your organization from phishing threats	ƒImplement robust email authentication protocols. Ensure Sender Policy Framework (SPF), DomainKeys Identified Mail (DKIM), and Domain-based Message Authentication, Reporting, and Conformance (DMARC) are fully configured and enforced with strict policies (e.g., `p=reject`) to prevent email spoofing.	ƒDeploy advanced email security solutions. Use AI-driven email security tools that analyze communication patterns, detect anomalies, display warning banners for external or newly registered domains, and automatically neutralize malicious links or attachments.	ƒConduct regular phishing simulations. Train employees to recognize evolving tactics, including qishing, reply-chain attacks, and social engineering lures. Tie training directly to real-world threats observed in your environment.	ƒEncourage a reporting culture. Make it as easy as possible for users to report suspicious emails with a single-click reporting button. Acknowledge and reward users who successfully report malicious emails to reinforce positive security behaviors.	ƒImplement link rewriting and safe links. Use email gateway features that rewrite URLs and scan destination pages in real time when clicked, blocking access if the site is determined to be a credential harvester or malicious payload host.Annual Threat Report 2024Annual spotlight
Emerging trends and focal points for 2024

Each year, our security operators, researchers, and
threat hunters take a step back to analyze the broader
forces shaping the threat landscape. In 2024, several
emerging themes demand the attention of security
leaders and practitioners alike.

The weaponization of generative AI

Generative artificial intelligence has transitioned from a novel
technology to a weaponized toolset for cyber adversaries.
While security defenders leverage AI to accelerate triage
and detection engineering, threat actors are using large
language models (LLMs) to scale their operations.

What we are seeing:
- **Spearphishing at scale**: Attackers are using LLMs to
generate highly personalized, grammatically flawless phishing
emails tailored to specific individuals by scraping their
public profiles and social media activity.
- **Vishing and impersonation**: As noted with groups
like "The Com," attackers are exploring voice synthesis and
deepfake technologies to mimic executives and IT staff during
helpdesk phone calls, bypassing verbal verification checks.
- **Code obfuscation**: Adversaries are leveraging AI to
rapidly write and refactor malicious scripts, making it harder
for static analysis tools to signature the code.

Defense recommendations:
- **Assume zero trust for communications**: Implement strict
out-of-band verification procedures for high-risk requests,
such as wire transfers, direct deposit changes, and password
resets, regardless of how convincing the caller or email appears.
- **Invest in behavioral analytics**: Focus detections on user
behavior and transactional anomalies rather than relying solely
on content inspection, as AI-generated text will continue to
look and sound legitimate.

Software supply chain risks

The software supply chain remains a fragile foundation for
modern enterprise technology. The exploitation of zero-days
in widely used enterprise software—such as MOVEit Transfer
and Citrix NetScaler—demonstrates that compromising a
single vendor can grant attackers immediate access to
hundreds of downstream organizations.

What we are seeing:
- **Upstream targeting**: Threat actors increasingly
invest time in auditing commercial software, open-source
libraries, and IT management tools for undocumented
vulnerabilities.
- **Rapid exploitation windows**: The time between a
vulnerability disclosure and active exploitation has shrunk
to hours, leaving organizations precious little time to patch.

Defense recommendations:
- **Software Bill of Materials (SBOM)**: Maintain a comprehensive
inventory of third-party software components and dependencies
to quickly identify exposure when a new vulnerability drops.
- **Pervasive microsegmentation**: Even if an edge device
or third-party application is compromised, effective internal
segmentation can prevent lateral movement to core domain
controllers and sensitive data repositories.

28

Annual Threat Report 2024Looking ahead to 2024…
Predictions from the Expel leadership team

As we look toward the remainder of 2024 and beyond,
our leadership team shares their predictions on where the
cybersecurity landscape is heading.

**Dave Merkel, CEO**
"We’re going to see identity continue to be the primary battlefield.
As organizations get better at deploying MFA, attackers will double
down on bypass techniques like AiTM phishing, session hijacking,
and social engineering helpdesk attacks. The organizations that
succeed won't be the ones with the most expensive tools, but
the ones that master identity hygiene and least-privilege access."

**Daniel Clayton, VP, Security Operations**
"Automation is no longer optional for security operations centers—
it's survival. The volume of alerts and the speed at which attackers
move mean human analysts can't look at everything manually.
The winning SOCs in 2024 will be those that successfully blend
human expertise with intelligent automation to drive down dwell
time and stop attacks before they cause real harm."

**Steve Kelly, VP of Strategy and Threat Intelligence**
"The line between cybercrime and nation-state activity will
continue to blur. Financially motivated gangs are adopting the
sophistication, persistence, and evasion techniques previously
reserved for advanced persistent threat (APT) groups. At the
same time, ransomware operators will continue to experiment
with data exfiltration and extortion without necessarily deploying
locking ransomware, finding it a cleaner and equally effective
way to monetize intrusions."

**Dan Beavin, VP of Engineering**
"We’ll see continued fallout from shadow IT and unmanaged
devices accessing corporate resources. As remote and hybrid
workforces continue to rely on personal devices and browser-
based workflows, attackers will increasingly target the browser
as the new endpoint. Protecting the browser and securing
session tokens will become just as critical as managing the
operating system."

29

Annual Threat Report 20242023 at Expel
By the numbers

Behind every incident investigated, alert triaged, and
customer secured is a dedicated team of Expel security
operators working around the clock. Here is a snapshot
of our operational scale and impact throughout 2023:

- **64%** of all incidents investigated by our SOC were identity-based.
- **72%** increase in cloud infrastructure incidents handled year-over-year.
- **58%** of our customers experienced at least one identity-related threat attempt.
- **57%** of high-risk malware incidents involved pre-ransomware strains like Gootloader, Qakbot, and SocGholish.
- **3** major zero-day vulnerabilities dominated our perimeter investigations (MOVEit Transfer, Adobe ColdFusion, and CitrixBleed).
- **24/7/365** continuous monitoring and protection provided across cloud, endpoint, identity, and network layers.

30

Annual Threat Report 2024Reference highlights
Key advisories, blogs, and research

Throughout this report, we reference various research pieces,
advisories, and blog posts published by the Expel threat intel
and security research teams. Below are key highlights and
resources to help your organization dive deeper into specific
threat topics:

- **Expel Blog: "Amazon Cognito: What you need to know about misconfigurations"**
  Detailed analysis of AWS Cognito misconfigurations, auditing tools, and how threat actors abuse identity pools.
- **Expel Blog: "Six things to consider before starting a red team exercise"**
  Strategic guidance on scoping and preparing your organization for realistic adversarial simulations.
- **CISA Advisories on MOVEit Transfer (CVE-2023-34362)**
  Official guidance and indicators of compromise (IoCs) related to zero-day exploitation of managed file transfer software.
- **FBI Internet Crime Complaint Center (IC3) Annual Report**
  Comprehensive statistics on business email compromise (BEC) financial losses and global cybercrime trends.

---

### Table of Contents
- [Executive summary](#executive-summary)
- [2023 by the numbers](#2023-by-the-numbers)
- [Identity threats](#identity-threats)
- [Cloud platform threats](#cloud-platform-threats)
- [Computer-based threats](#computer-based-threats)
- [Phishing threats](#phishing-threats)
- [Annual spotlight](#annual-spotlight)
- [Looking ahead to 2024…](#looking-ahead-to-2024)
- [2023 at Expel](#2023-at-expel)
- [Reference highlights](#reference-highlights)

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

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-11-21", "model": "gemini-3.5-flash-lite"} -->
