2023
GLOBAL
THREAT
REPORT

---

CrowdStrike

2

The latest edition of the CrowdStrike Global Threat Report comes at an important time for protectors around the world. As organizations focus on managing remote and hybrid teams, operationalizing years of digital transformation and navigating an uncertain global economy, adversaries have become more sophisticated, relentless and damaging in their attacks. As a result, a number of disruptive trends emerged in 2022 that threaten productivity and global stability.

These growing nation-state attacks coincided with organizations struggling to manage an explosive landscape of vulnerabilities that amplified systemic risk. The constant disclosure of vulnerabilities affecting legacy infrastructure like Microsoft Active Directory continued to burden security teams and present an open door to attackers, while the ubiquitous Log4Shell vulnerability ushered in a new era of “vulnerability rediscovery,” during which adversaries modify or reapply the same exploit to target other similarly vulnerable products.

The year started ominously as Russia’s deadly war of aggression in Ukraine brought about a terrible human toll, threatened international order and put countless global organizations at risk of spillover cyberattacks. At the same time, China state-nexus adversaries ramped up their cyber espionage campaigns, and Iranian actors launched destructive “lock-and-leak” operations using ransomware.

Even our wins on the security front were tempered by the adversaries’ ability to adapt. Collaboration between the government and private sector dramatically improved, resulting in the arrest and dismantling of some of the world’s most notorious ransomware gangs — only to see splinter groups recalibrate and flourish.

Stopping breaches requires an understanding of the adversary, including their motivations, techniques and how they’re going to target your organization. Developed based on the firsthand observations of our elite cyber responders and analysts, CrowdStrike’s annual Global Threat Report provides this actionable intelligence to protectors around the world.

Last year, CrowdStrike’s Global Threat Report highlighted that 80% of cyberattacks leveraged identity-based techniques to compromise legitimate credentials and try to evade detection. This year, the report shows adversaries are doubling down on stolen credentials, with a 112% year-over-year increase in advertisements for access-broker services identified in the criminal underground. Organizations armed with this knowledge last year were able to harden their defenses and stay a step ahead of the adversary.

2023 GLOBAL THREAT REPORT

CrowdStrike

3

Other details and insight you’ll learn from this year’s report include:

*   How a new, emerging class of eCrime threat actors is using fileless attacks to target high-profile organizations with devastating campaigns
*   Why identity protection continues to be a core requirement for risk mitigation as adversaries ramp up attacks on multifactor authentication
*   Why adversaries are accelerating cloud exploitation and the tactics they’re using to compromise cloud infrastructure
*   How adversaries have created a new “state of the art” for vulnerability exploitation to sidestep patches and why the industry needs to demand more secure software

These are just a few of the critical takeaways from this year’s report that will help you improve your business resilience and harden your security posture.

The report shows that security must parallel the slope of technology innovation. As technology matures, security has to mature and match the innovation of the technology running our organizations. The same thing can be said for the adversary. With every innovation we achieve, we can expect the adversary to actively seek ways to exploit it. From the cloud to Kubernetes, from AI to applications and more, as technology gets more complex and provides tremendous operational gains, security must evolve to protect the productivity we gain.

At CrowdStrike, our mission today is the same as when we started: to stop breaches so our customers can move forward. Our focus is on delivering the platform, technology and intelligence needed to keep you ahead of the adversary. This is why we’ve unified and delivered critical protections like endpoint and extended detection and response (EDR and XDR), identity threat protection, cloud security, vulnerability and risk management, threat intelligence and much more — all from a single platform.

I hope you find this report instructive in how we can continue to work together to protect the world from those who mean to do harm. Security starts with knowledge — of the adversaries targeting us, their tactics and the vulnerabilities they’ll seek to exploit. With that knowledge comes resolve, that together we can prevail.

George Kurtz
CrowdStrike CEO and Co-Founder

2023 GLOBAL THREAT REPORT
CrowdStrike

4

## Table of Contents
7 NAMING CONVENTIONS

### THREAT LANDSCAPE OVERVIEW
F
O
E
L
B
A
T

5

8

11

2022 THEMES

S INTRODUCTION
T
N
E
T
N
O
C

11

*   eCRIME ACTORS GAINED NOTORIETY FOR
    HIGH-PROFILE ATTACKS

14  THE CONTINUED RISE OF CLOUD EXPLOITATION

17   DISCOVERY, REDISCOVERY AND CIRCUMVENTION:

THE 2022 VULNERABILITY INTELLIGENCE LANDSCAPE

20   HIGH-EFFORT, LIMITED RETURN: RUSSIAN CYBER

OPERATIONS ARE SUPPORTING THE WAR IN UKRAINE

25   DOMINATING THE ESPIONAGE LANDSCAPE:

CHINA-NEXUS ADVERSARIES SIGNIFICANTLY
INCREASED 2022 OPERATIONAL SCALE

30

CROWDSTRIKE eCRIME INDEX

32

CONCLUSION

34

RECOMMENDATIONS

36

CROWDSTRIKE PRODUCTS AND SERVICES

42

ABOUT CROWDSTRIKE

CrowdStrike
2023 GLOBAL THREAT REPORT

---

5

N
O
I
T
C
U
D
O
R
T
N

I

The 2022 cyber threat landscape was defined by persistence, increased target scope and relentless determination. As businesses began to ease pandemic-driven operating environments and adjust to geopolitical shifts and growing economic hardships, adversaries supporting nation-state, eCrime and hacktivist motivations started 2022 with a relentless show of effort that endured throughout the year.

Nation-state adversaries engaged in relentless computer network operations throughout 2022, emphasizing the integral role these operations play in supporting state goals. Russian state-nexus adversaries combined destructive, espionage and information operations (IO) attacks in constant support of the Ukraine war, and China state- nexus adversaries dominated the cyber threat landscape with a significant increase in espionage operation volume and target scope. Iran continued to focus on regional espionage campaigns and their now-signature destructive “lock-and-leak” operations leveraging ransomware, and Democratic People’s Republic of Korea (DPRK) state-nexus adversaries persisted in cryptocurrency theft campaigns to supplement state funds in the wake of the COVID-19 pandemic and the nation’s long-standing economic hardship.

Over the course of 2022, eCrime adversaries continued to prove their ability to adapt, splinter, regroup and flourish in the face of defensive measures. After some of the biggest and most notorious ransomware enterprise shutdowns, ransomware affiliates moved to new ransomware-as-a-service (RaaS) operations. Additionally, more than 2,500 advertisements for access were identified across the criminal underground, representing a 112% increase compared to 2021 and demonstrating a clear demand for access broker services.

CrowdStrike Intelligence also observed an increase in social engineering using human interaction, such as vishing, to successfully download malware or circumvent multifactor authentication (MFA), proving direct interaction with victims remains a valuable asset to eCrime operations.

Hacktivists in 2022 embraced an environment of misinformation, capitalizing on major geopolitical shifts to relentlessly stoke national unrest and promote specific ideologies. While much of their activity concentrated on entities within the Russo-Ukrainian region, increased spillover activity involving targeting of near-abroad, European and U.S. entities occurred throughout the latter half of 2022 into 2023.

MORE THAN 2,500 ADVERTISEMENTS FOR

ACCESS WERE IDENTIFIED ACROSS THE CRIMINAL

UNDERGROUND, REPRESENTING A 112% INCREASE

COMPARED TO 2021 AND DEMONSTRATING

A CLEAR DEMAND FOR ACCESS BROKER SERVICES.

CrowdStrike
2023 GLOBAL THREAT REPORT

---

6

CROWDSTRIKE
INTELLIGENCE
BEGAN TRACKING

33

NEW ADVERSARIES,
RAISING THE TOTAL
NUMBER OF ACTORS
TRACKED TO

200+

“CrowdStrike has more
than 10 years in the
Cyber Threat Intelligence
industry and it continues
to dominate in this space.
Its threat intelligence is
actionable, automated,
and built into daily
workflows, powering
the company’s broad
cybersecurity portfolio.”

Frost & Sullivan

While it’s clear adversaries were persistent in pursuit of their goals in 2022, the year also demonstrated how relentless determination works both ways. CrowdStrike Intelligence began the year with a flying start, outpacing adversaries throughout 2022 with expansive reporting that captured new developments in real time as well as identified and tracked new adversaries. Over the course of the year, CrowdStrike Intelligence began tracking 33 new adversaries, raising the total number of actors tracked to over 200. While most CrowdStrike-tracked eCrime emanates from Eastern Europe and Russia, CrowdStrike Intelligence continues to name new adversaries operating from different regions, demonstrating the ubiquity of the threat. In 2022, CrowdStrike Intelligence introduced its first Syria-nexus adversary, DEADEYE HAWK, which was formerly tracked as DEADEYE JACKAL.

CrowdStrike Intelligence continues to expand its threat landscape coverage beyond targeted intrusion, eCrime, hacktivist, vulnerability intelligence and mobile mission areas. In 2022, CrowdStrike Intelligence increased support for cloud intelligence across all products and will introduce threat intelligence coverage for industrial control systems in 2023.

CrowdStrike relentlessly focused on empowering customers by releasing new services and features throughout 2022. CrowdStrike Falcon® Intelligence Recon — a tool that enables customers to uncover potentially malicious criminal underground activity — gained new features including underground trends reporting, typosquatting detection, complex historical search functionality and Falcon Intelligence Recon support for managed security service providers (MSSPs). The year 2022 also saw the launch of CrowdStrike Falcon® Surface, an external attack-surface management product resulting from CrowdStrike’s acquisition of Reposify.

Also in 2022, CrowdStrike created a Vulnerability Intelligence module to help customers quickly identify information associated with vulnerabilities and provide relevant intelligence reporting to support their understanding of vulnerability context. For further customer-driven research and analysis, CrowdStrike released the MITRE ATT&CK® Navigator¹ for tracked adversaries, which provides customers with particular actors’ MITRE ATT&CK techniques and sub-techniques as well as links to associated MITRE information and relevant CrowdStrike Intelligence reporting.

The CrowdStrike 2023 Global Threat Report summarizes the entirety of the CrowdStrike Intelligence team’s analysis performed throughout a relentless 2022, including descriptions of notable themes, trends and events across the cyber threat landscape. This report also includes anticipatory threat assessments to help prepare and protect organizations through the coming year.

¹ MITRE ATT&CK and ATT&CK are registered trademarks of the MITRE Corporation

CrowdStrike
2023 GLOBAL THREAT REPORT

---

7

I G N M A N S N O I T N E V N O C ADVERSARY

NATION-STATE OR CATEGORY

BEAR

RUSSIA

BUFFALO

VIETNAM

CHOLLIMA

DPRK (NORTH KOREA)

CRANE

ROK (REPUBLIC OF KOREA)

HAWK

SYRIA

JACKAL

HACKTIVIST

KITTEN

IRAN

LEOPARD

PAKISTAN

LYNX

GEORGIA

OCELOT

COLOMBIA

PANDA

PEOPLE’S REPUBLIC OF CHINA

SPIDER

ECRIME

TIGER

INDIA

WOLF

TURKEY

CrowdStrike
2023 GLOBAL THREAT REPORT

---

CrowdStrike

8

THREAT
LANDSCAPE
OVERVIEW

CrowdStrike

9

Every Second Counts
The CrowdStrike® Falcon OverWatch™ team measures breakout time — the time an adversary takes to move laterally, from an initially compromised host to another host within the victim environment. The average breakout time for interactive eCrime intrusion activity declined from 98 minutes in 2021 to 84 minutes in 2022.

Lateral
Movement

By responding within the breakout time window, defenders can minimize the costs and other damages caused by attackers. Security teams are encouraged to meet the 1-10-60 rule: detecting threats within the first minute, understanding the threats within 10 minutes and responding within 60 minutes.

eCRIME BREAKOUT TIME

84'

Initial
Access

Access Broker Boom
Accelerated in 2022
Access brokers are threat actors who acquire access to organizations and provide or sell this access to other actors, including ransomware operators. The popularity of their services increased in 2022, with more than 2,500 advertisements for access identified — a 112% increase compared to 2021.

Several brokers advertised accesses in bulk during 2022, while others continued to use the “one-access one-auction” technique. Access methods used by brokers have remained relatively consistent since 2021; a particularly popular tactic involves abusing compromised credentials that were acquired via information stealers or purchased in log shops on the criminal underground.

ACCESS BROKER ADVERTISEMENTS BY MONTH, 2022

400

300

200

100

0

y r a u n a J y r a u r b e F h c r a M l i r p A y a M e n u J l y u J r e b m e t p e S t s u g u A r e b o t c O r e b m e v o N r e b m e c e D

TOP 10 SECTORS ADVERTISED BY ACCESS BROKERS, 2022

300

200

100

0

i c m e d a c A l y g o o n h c e T l s a i r t s u d n I g n i r u t c a f u n a M i s e c v r e S l i a n o s s e f o r P i s e c v r e S l i a n c a n F i i s n o i t a c n u m m o c e e T l t n e m n r e v o G e r a c h t l a e H l i a t e R

2023 GLOBAL THREAT REPORT
CrowdStrike

10

Adversaries Continued
to Move Beyond Malware
to Gain Initial Access and
Persistence
There was a continued shift away from malware use, with malware-free activity accounting for 71% of all detections in 2022 (up from 62% in 2021). This was partly related to adversaries’ prolific abuse of valid credentials to facilitate access and persistence in victim environments. Another contributing factor was the rate at which new vulnerabilities were disclosed and the speed with which adversaries were able to operationalize exploits.

ADVERSARY TACTICS

Malware-Free

71%
62%

51%

40%

39%

  2022
  2021
  2020
  2019
  2018

50%increase in interactive

intrusion campaigns

Technology

Financial

Healthcare

Telecommunications

Retail

Manufacturing

Academic

Services

Government

Pharmaceutical

Interactive Intrusions Gained Speed
and Momentum
Compared to 2021, CrowdStrike observed a 50% increase in the number of interactive intrusion campaigns with accelerating activity into the fourth quarter.

In addition, the technology sector was the most frequently targeted vertical in which Falcon OverWatch uncovered interactive intrusion activity in 2022. This reflects an increase compared with the relative frequency of intrusions in the top 10 industry verticals from the prior 12 months.

TOP 10 VERTICALS BY INTRUSION FREQUENCY

21.6%

8.4

8.3

7.5

7.0

6.0

5.5

5.2

5.0

3.2

2023 GLOBAL THREAT REPORT
CrowdStrike

---

2023 GLOBAL THREAT REPORT

CrowdStrike

11

2022
THEMES

ECRIME ACTORS GAINED
NOTORIETY FOR HIGH-PROFILE
ATTACKS

eCrime actors constantly search for new ways to increase revenue, and they often seek out novel techniques or tools to expand their target reach or impact. Over the course of 2022, CrowdStrike Intelligence observed two newly named adversaries — SLIPPY SPIDER and SCATTERED SPIDER — pushing operational limits by targeting high-profile victims and impacting associated employees, customers and partners.

Adversaries must possess high skill levels and significant resources in order to thwart takedowns, arrests and potential extradition while sustaining operations against multinational and global entities. SLIPPY SPIDER and SCATTERED SPIDER have both successfully used a variety of techniques including MFA fatigue, vishing and SIM swapping.

CrowdStrike
2023 GLOBAL THREAT REPORT

---

12

SLIPPY
SPIDER

TARGETED TECHNOLOGY GIANTS
WITH DATA THEFT AND EXTORTION

In 2022, CrowdStrike Intelligence observed a 20% increase in the number of adversaries conducting data theft and extortion campaigns without deploying ransomware. Ransomware adversaries seeking to exert additional pressure on victims have commonly leaked victim data as a leverage tactic since 2019; CrowdStrike Intelligence has observed this “double extortion” model as the most common tactic exhibited by tracked big game hunting (BGH) adversaries. For many organizations, the threat of a data leak — which may impact sensitive proprietary data as well as customers’ and employees’ personally identifiable information (PII) — can prove as compelling an incentive to pay a ransom as the disruption caused by ransomware.²

In February and March 2022, SLIPPY SPIDER attracted significant attention in the security community for a series of high-profile data theft and extortion incidents targeting technology companies including Microsoft, Nvidia, Okta and Samsung. The adversary used their public Telegram channels to leak data including victim source code, employee credentials and PII. Although SLIPPY SPIDER made large ransom demands in exchange for not leaking the stolen data, CrowdStrike Intelligence has no evidence to suggest any of those demands were met. This targeting of high-profile victims and the large volume of stolen and leaked data drew the focus of various law enforcement operations in mid-2022.

Once they had the attention of law enforcement, SLIPPY SPIDER was likely not sufficiently skilled or resourced to sustain their targeting and ultimately recover their operations. CrowdStrike Intelligence has not observed SLIPPY SPIDER activity since June 2022.

² https://www.crowdstrike.com/blog/double-trouble-ransomware-data-leak-extortion-part-1/

CrowdStrike
---

2023 GLOBAL THREAT REPORT

13

SCATTERED
SPIDER

USED SOCIAL ENGINEERING TO
OVERCOME MFA

Since at least March 2022, SCATTERED SPIDER has conducted targeted social engineering campaigns primarily against firms specializing in customer relationship management and business process outsourcing. The adversary primarily uses phishing pages to capture authentication credentials for Okta, VPNs or edge devices, and socially engineers users to share one-time password multifactor authentication (MFA) codes or overwhelms them using MFA notification fatigue.

After achieving initial access, SCATTERED SPIDER deploys a vast array of legitimate remote monitoring and management tools or utilities such as PuTTY to maintain persistent access. In one case, the adversary demonstrated fluency with lateral movement and credential access across cloud-provider environments, including harvesting credentials using instance metadata service. To evade detection, the adversary has employed several different tools to bypass or terminate endpoint security software.

SCATTERED SPIDER leverages access to technology companies to target third- party companies, such as victims’ customers, with a heavy focus on accessing cellular service providers. While SCATTERED SPIDER’s operational goal is not entirely known, the adversary has been observed swapping SIMs using access to cellular service providers. The adversary’s SIM swapping likely enables follow-on third-party compromise. In some cases, the adversary has also captured individual user account data for resale, or targeted data relating to cryptocurrency companies.

SCATTERED SPIDER has gained attention due to the high-profile nature of their victims.

CrowdStrike
---

14

I E S R D E U N I T N O C E H T

TOP CLOUD-CONSCIOUS TTPs OF 2022

increase as more businesses moved operations to cloud environments and more adversaries became “cloud-conscious” — a term referring to threat actors aware of the ability to compromise cloud workloads and who use this knowledge to abuse features unique to the cloud for their own purposes. Over the course of 2022, cloud exploitation increased as expected: Observed cloud exploitation cases grew by 95%, and cases involving cloud-conscious actors nearly tripled from 2021. This growth indicates a larger trend of eCrime and nation-state actors adopting knowledge and tradecraft to increasingly exploit cloud environments.

Throughout 2022, cloud-conscious actors deployed a variety of tactics, techniques and procedures (TTPs) to exploit cloud environments. CrowdStrike Intelligence observed actors continuing to rely on valid cloud accounts but also increasingly looking to public- facing applications for initial access. More actors were seen moving toward cloud account discovery, compared to the heavier reliance on cloud infrastructure discovery observed in 2021. Actors were also identified using valid higher-privileged accounts for privilege escalation in 2022. Notably, in terms of defense evasion tactics, CrowdStrike Intelligence saw actors shift away from the deactivation of antivirus and firewall technologies, as well as from log-tampering efforts. Instead, they were observed seeking ways to modify authentication processes and attack identities.

N THE 2022
O
I
T
A
T
I
O
L
P
X
E
D
U
O
L
C
F
O

Tactics supporting data access also began moving toward exfiltration from information repositories as well as cloud storage and local systems. Finally, in addition to previously reported resource-hijacking impacts, CrowdStrike Intelligence observed actors incorporating destructive actions such as account access removal, data destruction, resource deletion and service stoppage.

CrowdStrike Intelligence
saw actors shift away from
the deactivation of antivirus
and firewall technologies,
as well as from log-
tampering efforts. Instead,
they were observed
seeking ways to modify
authentication processes
and attack identities.

CrowdStrike
2023 GLOBAL THREAT REPORT

---

15

INITIAL
ACCESS

DISCOVERY

LATERAL
MOVEMENT

PRIVILEGE
ESCALATION

DEFENSE
EVASION

TOP CLOUD-CONSCIOUS
TTPs OF 2022

Throughout 2022, cloud-conscious actors primarily obtained initial access to the cloud by using existing, valid accounts, resetting passwords or placing webshells or reverse shells for persistence after exploiting public-facing applications such as web servers. Once on a machine, actors attempted to gain access primarily through credentials found in files, but also via the cloud provider's instance metadata services (IMDSs).

During initial environment discovery, actors primarily focused on cloud accounts — for persistence and potential privilege escalation — as well as reachable network services, but also searched for cloud permission groups, infrastructure and storage buckets.

To move laterally inside a cloud environment, actors used protocols such as RDP, SSH and SMB; actors with console access also leveraged services such as EC2 instance connect and the Systems Manager Session Manager to achieve this goal.

Actors escalated their privileges by gaining access to accounts with higher privileges, either by finding credentials for these accounts or resetting credentials that already existed.

Actors tried to evade defenses by deactivating security products running inside virtual machines. Other actors attempted to masquerade by choosing proxy exits close to expected victim locations or naming newly created virtual machines according to victims' naming scheme.

DATA
COLLECTION

To collect data, actors turned to local systems as well as internal information repositories such as code repositories, SharePoint, internal tooling and databases.

IMPACT

Despite industry reports claiming resource hijacking was the most common impact technique used in 2022, the most ubiquitous impact technique was actually destructive, with actors removing access to accounts, terminating services, destroying data and deleting resources.

Figure 1. Top cloud-conscious TTPs of 2022

CrowdStrike
2023 GLOBAL THREAT REPORT

---

16

As cloud integration continues to increase across business environments, adversaries are adding the cloud to their targeting aperture to expand the impact of their attacks. Though the goals of adversaries’ operations often remain identical or similar to their intrusion ambitions outside cloud environments — i.e., gain initial access, gain persistence and move laterally — the short-lived nature of some cloud environments means adversaries may need a more tenacious approach to succeed. CrowdStrike Intelligence expects cloud-conscious targeting to continue into 2023. This assessment is made with high confidence based on the three-fold increase in this targeting observed in 2022 as well as the ever-increasing need for entities to integrate the cloud into the daily working environment.

SUSPECTED PANDA BECOMING
CLOUD-CONSCIOUS

Successful exploitation of CVE-2022-29464 enables remote code execution and unrestricted file uploads. On the same day the vulnerability affecting multiple WSO2 products was disclosed, exploit code was made publicly available. Adversaries were quick to capitalize on the opportunity. Falcon OverWatch threat hunters began identifying multiple exploitation incidents in which adversaries used tools, infrastructure and TTPs consistent with China-nexus activity. There is increasing evidence that adversaries are growing more confident leveraging traditional endpoints to pivot to cloud infrastructure. The reverse is also true: Cloud infrastructure is being used as a gateway to traditional endpoints. Figure 2 shows three of the ways Falcon OverWatch has observed adversaries make this pivot in interactive intrusions.

d u o l C

INITIAL ACCESS
Falcon OverWatch observed valid
credentials being used by an
unknown adversary to achieve
execution on Windows endpoints
via a third-party cloud
management tool.

EXFILTRATION
Falcon OverWatch continued to track
the activity as the adversary used a
cloud storage platform to copy and
transfer collected data.

DISCOVERY
After achieving interactivity on the
host, the suspected PANDA
adversary was observed using the
awscli utility to perform advanced
AWS reconnaissance, including
enumeration of AWS conﬁg and
credentials ﬁles.

COMMAND
AND CONTROL
The adversary then used
PowerShell to download an
unknown executable to
Windows endpoints.

INITIAL ACCESS
AND DISCOVERY
Falcon OverWatch uncovered an
adversary exploiting an installation
vulnerable to Log4Shell to gain access.
The adversary proceeded to conduct
extensive reconnaissance, including
enumeration of password information
related to a cloud hosting platform.

INITIAL
ACCESS
A suspected PANDA adversary
exploited CVE-2022-29464 to
achieve remote code execution on
a Linux host. Falcon OverWatch
discovered the adversary deploy
.jsp webshells.

Figure 2. Interactive intrusion pivoting between cloud and traditional IT assets

s e t s s A T I l a n o i t i d a r T

2023 GLOBAL THREAT REPORT
CrowdStrike

---

17

Y R E V O C S I D E R , Y R E V O C S I D E R VULNERABILITY
INTELLIGENCE
LANDSCAPE

CrowdStrike Intelligence saw actors consistently focus on previously established attack vectors and components to achieve exploitation in 2022. There are two ways adversaries can pursue this approach to exploit development following vulnerability discovery. The actors can modify — or even reapply — the same exploit to target other similarly vulnerable products. Alternatively, the discovery process can identify a potential target and encourage actors to focus on these known vulnerable components, as well as circumvent patching by exploring other exploit vectors (see Figure 3). This is particularly true for edge devices, which are often vulnerable to various injection techniques and arbitrary file-delivery exploits.

N THE 2022
O
I
T
N
E
V
M
U
C
R
C
D
N
A

1. discovery
Identify vulnerable JNDI Log4j2
library components and develop
exploit for CVE-2021-44228

I

Apache Log4j2

VMware

2. Rediscovery
Identify vulnerable Log4j2 libraries in other vendor
products and tailor exploit for speciﬁc application

Cisco

Ubiquiti

1. Discovery
Identify vulnerable Exchange server
proxy components and develop
remote unauthenticated exploits
(ProxyShell and ProxyLogon)

2. Circumvention
Bypass patches by targeting previously identiﬁed
and vulnerable proxy components via multiple
authenticated vectors

Exchange Server V. 1
(ProxyLogon/ProxyShellexploits)

Exchange Server V. 2
(ProxyNotShell exploit)

Exchange Server V. 3
(CVE-2022-41080 exploit)

Patch:
Authentication
Controls

Patch:
Autodiscover
Requests

Figure 3. Iterative vulnerability discovery, rediscovery (top) and circumvention
(bottom) processes

CrowdStrike
2023 GLOBAL THREAT REPORT

---

18

VULNERABILITY DISCOVERY
AND REDISCOVERY

The notorious and prolonged nature of Log4Shell exploitation was the most prominent example of vulnerability discovery across numerous products in 2022. Log4Shell exploitation was initially opportunistic in nature, with actors seeking vulnerable products and targeting what they could find. However, variations of the exploit targeting other fields, leveraging other protocols and using obfuscation techniques rapidly allowed for tailored CVE-2021-44228 exploitation in other products where exploitation was not initially achievable. Falcon Intelligence Recon observed continued CVE-2021-44228 discussions among threat actors in the criminal underground during 2022, reflecting sustained interest in Log4Shell exploitation (see Figure 4).

Starting in January 2022, a similar discovery and exploitation process across myriad products unfolded in the context of the PwnKit exploit, which targeted the Polkit package most Linux platforms use to manage permissions using privilege escalation vulnerability CVE-2021-4034. While open-source projects are more likely to be impacted by vulnerability exploitation issues, integrating vulnerable packages from external sources also routinely contributed to proprietary software exploitation throughout 2022.

80

60

40

20

0

CVE-2021-44228 MENTIONS
CROWDSTRIKE INTELLIGENCE RECON DATA

y r a u n a J y r a u r b e F h c r a M l i r p A y a M e n u J l y u J r e b m e t p e S t s u g u A r e b o t c O r e b m e v o N r e b m e c e D

Zero-day and N-day
vulnerabilities observed
in 2022  demonstrated
threat actors’ ability to
leverage specialized
knowledge to
circumvent mitigations
from previous patches
to target the same
vulnerable components.

Figure 4. CVE-2021-44228 mentions on forums, marketplaces and messenger
groups in 2022

CIRCUMVENTION OF EARLIER PATCHES

The disclosure of a vulnerability, particularly one acknowledged as previously exploited
in the wild, highlights potentially viable mechanisms for future exploitation. Zero-day and
N-day vulnerabilities observed in 2022 demonstrated threat actors’ ability to leverage
specialized knowledge to circumvent mitigations from previous patches to target the
same vulnerable components.

For example, the proxy mechanisms exploited to compromise Microsoft Exchange during
ProxyLogon and ProxyShell campaigns in 2021 were targeted again in Q4 2022, this time
using an authenticated variation called ProxyNotShell (CVE-2022-41040 and CVE-2022-
41082). ProxyNotShell mitigations were subsequently bypassed when ransomware-
affiliated actors used an alternative exploitation vector that abused CVE-2022-41080 to
accomplish the same objectives.

A similar pattern emerged among a series of zero-day exploits associated with the
Windows Common Log File System (CLFS) driver observed between March and August
2022. Demonstrating their expertise, developers of the CVE-2022-37969 exploit
employed a technique to identify and bypass mitigations intended for an earlier CLFS
vulnerability (CVE-2022-24521).

CrowdStrike
2023 GLOBAL THREAT REPORT

---

CrowdStrike

19

LOOKING DEEPER

FALCON OVERWATCH
CASE STUDY

Unattributed Adversary Exploits Zoho ManageEngine Vulnerability

In late 2022, Falcon OverWatch notified an organization
in the technology sector of an active hands-on intrusion.
The unattributed adversary achieved code execution
through abuse of a vulnerability in the Zoho ManageEngine
application. They used  this capability to install and execute
the ScreenConnect remote access tool, hiding this evidence

by saving it to a hidden directory, deleting several files
for anti-forensic purposes, and setting the display name
to Microsoft Network Management. The adversary then
generated an account list and attempted to connect to
additional remote sessions on the host.

INITIAL  ACCESS
The adversary exploited a vulnerability in
Zoho ManageEngine (CVE-2022-35405) to
achieve execution on the host.

PERSISTENCE
The adversary followed on from their
exploitation of Zoho ManageEngine by
installing the ScreenConnect agent as a
Windows service, set to automatically start.

DISCOVERY
The adversary attempted to enumerate
collections of system information including the
current system owner and user.

EXECUTION
The adversary used both the Windows Command
Shell and PowerShell to execute commands. The
ScreenConnect  agent, a remote administration tool,
was installed using an MSI file via MSIExec.

DEFENSE EVASION
The adversary attempted to disguise the
ScreenConnect agent and evade defenses by
renaming the ScreenConnect service as "Microsoft
Network Management."
The ScreenConnect service was installed into a
hidden directory.  The adversary deleted several files
on the host for anti-forensic purposes.

COMMAND AND CONTROL
The adversary installed a copy of the ScreenConnect
agent to the victim host. They were also observed
sending a request using the Telegram API.

LATERAL MOVEMENT
The adversary attempted to take over several
RDP sessions on the host via remote service
session hijacking and move laterally via RDP.

2023 GLOBAL THREAT REPORT

---

20

T R O F F E - H G H I

N RUSSIAN CYBER
R OPERATIONS ARE
U SUPPORTING THE
T WAR IN UKRAINE
E
D
E
T
I
M
I
L

The Russia-Ukraine war that began in 2022 has involved unprecedented use of cyber
capabilities sustained throughout the extended ongoing military campaign.
CrowdStrike Intelligence has observed a spectrum of Russia-nexus activity relating to
this conflict, including extensive intelligence collection activities, information operations
aiming to influence public sentiment