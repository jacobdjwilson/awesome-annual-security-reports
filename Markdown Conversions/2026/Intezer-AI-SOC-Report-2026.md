AI SOC

Report
2026

Foreword
In 2025, Intezer AI SOC analyzed more than 25 million security alerts across live enterprise
SOC environments. This report is grounded in the triage, investigation, and resolution of every
one of those alerts, at a forensic level, across Intezer’s global customer base.

With this massive scale of alert volume analyzed, reality is revealed about how attacks actually
unfold, where defenses fail, and how SOCs spend their time under pressure.
The big reset F o r years, security leaders have made tradeoffs in the face of an
unsolvable equation where alert volumes rapidly grow and human teams
of "acceptable
do not. Whether operated in-house or through an MDR, most SOCs are
security risk" forced to triage aggressively, ignoring and auto-closing a majority of alerts,
particularly those that are low-severity or informational.
Surveys consistently show that over 60% of alerts are never reviewed, simply because it is
mathematically impossible for human analysts to investigate everything. This reality has become the
accepted status quo, and understandably so.
But the emergence of AI-driven SOC platforms that can perform high-fidelity analysis at scale,
completely resets the definition of “acceptable risk”. It’s now an imperative to reexamine long-
standing risk tolerance, especially when data shows that real threats originate in places we
historically had no choice but to ignore.
Nearly 1% of all incidents are traced back to
alerts classified at the lowest severity levels.
Real threats One of the most consequential findings in this report is how frequently
genuine threats originate from alerts initially labeled as low-severity or
hiding in low-
informational. Across endpoint, cloud, identity, network, and phishing
severity alerts categories, nearly 1% of all incidents are traced back to alerts classified
at the lowest severity levels. At scale, this is far from trivial.
With enterprises generating an average of 450,000 alerts annually, this equates to roughly 54 real
threats per year, or about one per week, slipping by unnoticed.
This equates to roughly 54 real threats per year,
or about one per week, slipping by unnoticed.
02

Within endpoint alerts, that number rose to nearly 2% low-severity endpoint alerts representing
genuine threats.
In practice, these threats are rarely uncovered by in-house or external SOC teams. Most AI SOC
platforms that exclusively rely on AI agents, are also limited to triaging high- and medium-severity
alerts. These “below the radar” alerts can only be identified through highly scalable, automated and
forensic-grade triage that can examine behavior, lineage, and intent, for 100% of all ingested alerts.
Noise, stealth, Beyond severity misclassification, the data highlights a threat landscape
dominated by noise masking meaningful activity. Scanning of public-facing
and misjudged
infrastructure generated some of the highest alert volumes, while identity
risk telemetry was flooded with “impossible travel” detections.
In cloud environments, however, the most frequent alerts related to defense evasion and
persistence, reflecting attackers’ focus on stealth, long-term access, and abuse of legitimate
services through token manipulation and obfuscation.
Taken together, these findings point to a consistent pattern. While alert volume is increasing,
severity and risk are often misaligned with meaningful threats frequently hidden among signals that
are deprioritized or ignored.
The sections that follow break down these patterns in detail and translate them into operational
lessons drawn from a year of large-scale forensic triage. This is the State of the SOC as it exists in
practice, shaped by millions of alerts, real adversaries, and the constraints security teams face
every day.
As always, Intezer’s AI SOC platform along with our experienced security analysts and researchers,
stand ready to deliver stronger security outcomes and real risk reduction that scales with your
business.
Severity and risk are often misaligned with
meaningful threats frequently hidden among
signals that are deprioritized or ignored.
Itai Tevet
Intezer CEO and Co-Founder
03

25,000,000
alerts analyzed by Intezer
60%
Over of alerts are
ignored by SOC and MDR teams,
especially low-severity ones
1%
nearly
real threats
of come

from low-severity alerts
What this means for enterprise security?
54 real threats
per year
(~1 per week)
are never investigated by SOC or MDR
For organizations with 450K alerts per year

Table of contents
Data & methodology
 07

Bottom line up front (BLUF) 08
Endpoint What 9.25M alerts revealed about triage shortcomings
 10

Malware deep dive
 11

Windows
 12

Stealers
 12

Ransomware
 13

Linux
 14

Installers
 15

Weaponized software 15
Network Noise masking real threats, exposure risks, and emerging abuse
 16

Scanners
 16

Code Sandboxes
 18

I see plain-text passwords
 20

Internal networks
 20

External networks 21
Phishing Scale, signal, and evolving techniques
 22

User reporting creates volume, but not always signal
 22

Attackers are shifting focus from endpoint to users’ browser
 22

Brand impersonation and callback scams dominate
 23

Brand impersonation breakdown
 23

Callback Scams
 24

Phishing infrastructure is becoming harder to detect
 26

New phishing threats and attack vectors 26
05

Table of contents
| Identity          | High-value signals, high false-positive volume
 | 29
 |
| ----------------- | ----------------------------------------------- | --- |
|                   | Most identity alerts are benign                 | 29  |
| Impossible travel | High volume, low risk                           | 30  |
31

| Cloud         | Persistence, evasion, and configuration drift
 |     |
| ------------- | ---------------------------------------------- | --- |
|               | Not the best practices
                        | 32  |
| About Intezer |                                                | 33  |
| Appendix      | The Rise and Fall of CrazyHunter               | 34  |
06

Data

and methodology
This report is based on a comprehensive analysis of threat activity observed across Intezer’s
global customer base throughout 2025. To identify emerging attack patterns, evasion
techniques, and security weaknesses, a broad and diverse dataset was examined.
25M
10M monitored
endpoints and identities
alerts triaged
180M
files analyzed
3M domains and URLs 7M IP addresses
analyzed investigated
82K endpoint forensic
550K
investigations, including
emails analyzed
live memory scans
All data used in this study were processed in accordance with strict privacy and security standards.
Intezer’s research methodology is designed to ensure no sensitive, personal, or customer-identifying
information is accessed, retained, or included in the analysis.
Findings are aggregated and anonymized, focusing solely on technical threat indicators and behavioral
trends. This enables Intezer to deliver accurate, large-scale threat intelligence insights while maintaining the
confidentiality and trust of our customers.
07

Bottom line up front (BLUF)
Intezer AI SOC overall stats
Less than 2% of all the alerts were escalated by Intezer to a human.
98% verdict accuracy.

Sub-minute median triage time.

Across all alert types, 0.6% of escalations came from low-severity or
informational events.
Triaged alert type breakdown
EDR Email SIEM
14% 2% 84%
25 Million alerts
37% 34% 14% 6% 6% 2.5% <1%
Endpoint Network Identity Phishing DLP Cloud Specific Other
Endpoint stats
2% of escalations came from low-severity or informational endpoint alerts.

180 million files analyzed. This is across all major operating systems: Windows,
Linux, MacOS, iOS, and Android.
Over 82,000 forensic investigations performed on endpoints, including live
memory scans. In over 1.6% of the forensic scans, we found that the endpoint
was still compromised even though the EDR reported the threat had been
mitigated.
Threat actors deploying stealers and RATs use increasingly complex, multi-stage
loaders to disguise familiar malware strains.

Akira Ransomware has topped our results as one of the most active ransomware
groups in 2025. Ransomware is still being created with flawed cryptography.
Strains of Mirai were the most prevalent malware identified on Linux hosts.
08

Network stats
Over 1M alerts on IP addresses (out of the 7M investigated) were for scanning
activity. 88% were blocked at the source by the firewall.
Of the remaining 12% that required triage, only 6% were confirmed as malicious.
Code sandboxes are being heavily abused to host phishing sites targeting the
theft of cryptocurrency.
A significant amount of internal network traffic remains unencrypted during
transit. Indicates that many companies still rely on perimeter security rather than
zero-trust security.
Phishing stats
Over half a million user-reported phishing emails were analyzed. The most
common technique used in phishing emails was brand impersonation, followed
by callback scams and credential phishing links.
Over 3 million phishing and malware-related URLs investigated. Microsoft was
the most impersonated brand.
Threat actors have increased their use of CAPTCHA to make the detection of
phishing pages more difficult.
PayPal's infrastructure is being heavily abused for callback scams.
Malicious content is being concealed within trusted file formats to bypass
security measures.
Identity stats
The most common identity alert was for location or session anomalies. Over 36%
of identity alerts fall into this category. Most "impossible travel" alerts are false
positives, mainly caused by VPNs and mobile phones.
Cloud alert stats
Most of the cloud-based alerts fall in the defense evasion and persistence
category.
Amazon S3 is involved in the majority of AWS misconfigurations. Many legacy
features are still being used.
09

Endpoint: What 9.25M alerts revealed
about triage shortcomings
In 2025, Intezer AI SOC investigated 9.25M endpoint alerts, analyzing over 175 million files,
combining data from the alerts with Intezer’s proprietary endpoint scans to achieve a verdict.
Of these endpoint alerts, 43% were classified as informational or low-severity.
Of these informational or low-severity alerts, nearly 2% of them were real incidents.
25M alerts investigated
| 9.25M           | 3.9M              |     | 77K            |
| --------------- | ----------------- | --- | -------------- |
| endpoint alerts | low-severity or
 |     | real incidents |
informational alerts
(from low-severity/informational)
1.9%
| 37% | 43% |     |     |
| --- | --- | --- | --- |
Additionally, over half of all endpoint alerts were not automatically mitigated by their endpoint
protection solution. Of these non-mitigated alerts, almost 9% were confirmed as malicious.
25M alerts investigated
| 9.25M           | 4.8M                |     | 428K           |
| --------------- | ------------------- | --- | -------------- |
| endpoint alerts | were not mitigated
 |     | real incidents |
by source vendor
8.9%
| 37% | 52% |     |     |
| --- | --- | --- | --- |
Alerts that required additional analysis, underwent live endpoint scans with Intezer’s proprietary endpoint
scanner. In more than half of the confirmed compromised endpoints, the endpoint protection reported the
alert as mitigated!
25M alerts investigated
| 9.25M           | 82K             | 2.6K        | 1.3K |
| --------------- | --------------- | ----------- | ---- |
| endpoint alerts | underwent live  | had active  |      |
were reported as
|     | endpoint scans | infection |     |
| --- | -------------- | --------- | --- |
mitigated by
source vendor
51%
| 37% | 1%  | 3.2% |     |
| --- | --- | ---- | --- |
While it’s possible these numbers reflect a vendor issue when it comes to mitigating or
Note
correctly labeling threats, there can be many other legitimate factors at play causing this
behavior. All that is certain is that SOC teams need to be vigilant in light of these realities.
10

Malware deep dive
One of Intezer’s proprietary investigative tools is an This capability makes our endpoint analysis not only
endpoint scanner which performs live memory comprehensive but also highly effective in
forensics on a host and identifies malicious code uncovering memory-resident threats, backdoors,
running within a process. and advanced persistent activity that may originate
from seemingly low-severity alerts.
Top malware families compromising endpoints (detected in memory)
Mimikatz
Meterpreter
Metasploit
Cobalt Strike
Winos
SharpHound
Donut Injector
XMRig Miner
StrelaStealer
Other
0.00% 10.00% 20.00% 30.00% 40.00%
11

Windows Breakdown of operating systems
Windows remains the most popular operating Windows 51%
system for endpoints, accounting for 51% of all
endpoints. As such, we also see a wide range of
Linux 46%
threats targeting these endpoints. In this section,
we will highlight the most common types of threats
macOS 1.5%
that we saw in the past year.
iOS <1%
Android <1%
Breakdown of devices
Desktop 53%
Server 46%
Virtual <1%
Phone/tablet <1%
Stealers
2.1%
2.8%
Credential and information stealers remained a
prevalent threat throughout the year, with Agent
Agent Tesla
Tesla dominating the landscape, accounting for 39%
14.4%
of all detections. It was followed by Snake Snake Keylogger
Keylogger and Formbook, which together accounted 40.3% Formbook
for more than a third of activity, highlighting
Mimikatz
attackers’ continued focus on harvesting sensitive
18.0%
LummaC2
data and credentials for follow-on intrusions or
Stealer
resale. Other notable families, such as Mimikatz,
RedLine Stealer
LummaC2, and RedLine Stealer, further illustrate the
19.9%
widespread use of credential theft as an initial
access and persistence mechanism across both
criminal and state-aligned campaigns.
12

Ransomware
The ransomware activity observed over the past active, alongside smaller but persistent clusters like
year shows a clear concentration around a few Phobos, AvosLocker, and Rhysida. Even lower-
dominant families with Akira, INC, and LockBit volume families such as CHAOS, Pay2Key, and
appearing as the most active groups by a significant Trigona demonstrated continued activity, illustrating
margin. These operations continued to drive a large the diverse and evolving nature of the ransomware
portion of global ransomware incidents, reflecting ecosystem. The data shows a ransomware
their mature infrastructure, rapid development landscape dominated by mature RaaS operations
cycles, and broad targeting across various while new variants continue to appear, creating a
industries. Beyond these leading families, well- mix of stable, high-impact groups and ongoing
known groups such as Babuk, Lynx, and STOP also experimentation by threat actors.
remained
Common ransomware families
300
200
100
0
Akira INC LockBit Babuk Lynx STOP Phobos AvosLocker Rhysida Snatch CHAOS Pay2Key Trigona
Ransomware
13

Linux
Mirai remains the most prevalent threat in Linux adaptation for different architectures make it a
environments, reflecting the continued exploitation versatile tool for both low-level and organized threat
of vulnerable IoT and server infrastructure. Its actors. Its continued activity underscores ongoing
dominance stems from the widespread use of weak weaknesses in IoT security and highlights the need
credentials, exposed services, and unpatched for stronger authentication, segmentation, and
devices, enabling the automated propagation of proactive monitoring across Linux-based systems.
malware at scale. Despite the emergence of
We also observe ransomware families targeting
ransomware and cryptominer families like Akira and
Linux systems alongside Windows environments,
XMRig, none rival Mirai’s persistence or reach. The
with Akira and INC remaining the most dominant
malware’s open-source availability and frequent
across Linux machines.
Malware threats in Linux
300
200
100
0
Mirai Mettle XMRig Akira CoinMiner INC CoinStomp Metasploit ChinaZ Plague InterlockFINALDRAFT Gafgyt BPFDoor Babuk
Miner Ransomware Ransomware Frame… ransomware
14

Installers
3.1%
The pie chart here shows the installers most 4.1%
commonly used as the initial delivery mechanism in 6.7%
malware cases observed on our platform. Because NSIS
many malicious payloads are packaged inside 6.9%
WinRAR.SFX
legitimate installer frameworks, the root file often
45.8%
WEXTRACT
appears benign while the installed components are
not. With Intezer’s unique sandboxing and genetic InnoSetup
analysis data, the installer family was tracked when 7-Zip.SFX
33.4%
the resulting installed file was confirmed as
Other
malware. The breakdown highlights how frequently
specific installers are abused for this purpose.
Weaponized software
Newly observed multi-stage loader called PNGPlug delivers the well-known remote access
trojan, ValleyRAT
Our research team uncovered a campaign that utilized a newly observed multi-stage loader called
PNGPlug to deliver the well-known remote access trojan, ValleyRAT. The attack began with a
phishing page that distributed a malicious MSI installer posing as legitimate software. Once
executed, it unpacked and decrypted additional components, using a large loader DLL that injected
payloads hidden within PNG files before launching ValleyRAT. This discovery highlights a growing
trend where stealers and RATs use increasingly complex, multi-stage loaders to disguise familiar
malware strains. Attackers are focusing on layered execution and loader obfuscation to bypass
traditional detections, making behavioral and memory-based analysis critical for identifying threats
early in the infection chain. Read the full report.
Zero-day vulnerabilities actively exploited by the XE Group
threat group In collaboration with Solis, a U.S.based MSSP, Intezer identified two previously
unknown zero-day vulnerabilities that were being actively exploited by the XE Group threat group.
The investigation revealed that XE Group had evolved from conducting web-skimming campaigns to
leveraging advanced zero-day exploits targeting the VeraCore warehouse management platform.
These exploits (CVE-2024-57968 and CVE-2025-25181) enabled attackers to upload malicious
ASPX web shells, execute obfuscated payloads, and deploy in-memory shellcode using reflective
PowerShell loaders and Meterpreter, thereby allowing for stealthy persistence and data exfiltration.
Read the full report.
The rise and fall of CrazyHunter
In early 2025, Intezer and Taiwan-based AIShield collaborated on an investigation into a newly
emerged ransomware group dubbed CrazyHunter, which launched a wave of coordinated attacks
against Taiwan’s healthcare, education, and energy sectors. The campaign stood out for its
sophistication, despite the group’s apparent newness, blending traditional double-extortion tactics
with modern evasion techniques. See appendix for full details.
15

Network: Noise masking real threats,
exposure risks, and emerging abuse
The network layer provides broad visibility into attacker behavior but also generates significant
noise. In 2025, Intezer AI SOC triaged alerts involving over 7 million IP addresses, 3 million
domains, and 3 million URLs, with contextual analysis enabling us to distinguish routine activity
from meaningful risk.
Scanners
Web scanners account for a significant portion of
12%
the alerts triaged by Intezer AI SOC with over one
million alerts this year alone. This volume reflects
the extensive number of public-facing servers we
monitor and the constant probing activity that
Mitigated
targets exposed infrastructure across the internet.
Not Mitigated
Most scanner activity we observed was
automatically mitigated by firewall products with 88%
many cases traced to benign scanners such as Mitigated 88.0%
Shodan and Censys. Of the 12% of alerts not
mitigated by firewalls, 6% were confirmed as
genuine threats.
16

The following table highlights the ten most active malicious scanners observed throughout the
year, ranked by the number of alerts in which they appeared. This view illustrates the
persistence of automated reconnaissance activity across monitored environments
| IP Address          | Number of Alerts  | Type                    |
| ------------------- | ----------------- | ----------------------- |
| 79.124.62[.]122
   | 4,462
           | Port Scanner
          |
| 45.224.42[.]19
    | 1,095
            | SSH Brute Force
       |
| 46.17.96[.]38
     | 656
             | Port Scanner
         |
| 185.44.76[.]10
    | 564
             | Port Scanner
          |
| 45.142.193[.]107
   | 519
             | Port Scanner
          |
| 139.144.52[.]241
   | 478
             | Vulnerability Scanner
 |
| 195.140.213[.]28
   | 474
             | Port Scanner
          |
| 141.98.80[.]118
   | 438
             | Password Brute Force
 |
| 172.245.163[.]134
 | 417
             | Port Scanner
         |
| 45.134.26[.]32      | 414               | Port Scanner            |
Any system exposed to the internet will inevitably attract scanner activity, whether benign or
malicious. The key to effective triage lies in context: combining alert data with threat
intelligence and insight into the affected device or account to determine whether an actual
breach has occurred.
17

Code Sandboxes
While reviewing network alerts from XDR and SIEM Code sandboxes are attractive to attackers
sources, we noticed recurring references to well- because they offer immediate deployment, a
known code sandboxes. Initially, the findings trusted domain, and no infrastructure cost. The
appeared benign. These domains are legitimate content they host runs as intended, which allows a
platforms used by developers to share and test malicious page to operate without technical
code, and they maintain a solid reputation across restrictions. These characteristics make the
most threat intelligence feeds. Yet despite that, environments ideal for short-lived phishing
Intezer AI SOC was returning malicious verdicts. campaigns that benefit from built-in credibility.
We examined the alerts and found that although the The platform most frequently abused in our data
parent domains were reputable, the individual was Vercel. It appeared across a wide range of
projects hosted on them often served phishing phishing themes, including social media, email,
pages. In several cases, the pages were live banking, streaming, and gambling. One example
credential-harvesting sites using the sandbox as involved a link sent by email that led to a Vercel
free, trusted hosting. page imitating Adobe Cloud, prompting users to
sign in to view a fake document.
Attachment Phishing Page
Credentials
18

A large number of incidents also involved cryptocurrency scams. We found sites asking victims
to enter recovery phrases or credentials for platforms such as MetaMask, Coinbase,
Binance, and Uniswap. Several targeted NFT marketplaces, such as OpenSea, are indicating
that attackers are expanding their focus to the broader Web3 ecosystem.
Exodus Wallet Opensea Uniswap
Metamask Binance Coinbase
Vercel was not the only platform misused. Similar activity appeared on CodePen, JSitor, and
JSBin, each hosting copies of phishing kits or redirect pages; all of which have been very
reactive at taking down malicious content. The pattern suggests a continuing shift toward the
abuse of legitimate developer services as disposable infrastructure for credential theft.
19

I see plain-text passwords
Plain-text password alerts usually originate from
products that inspect network traffic, such as DLP
systems, XDR engines with network visibility, or SIEM
17.2%
pipelines that analyze packet metadata.
When we reviewed our own data, we found roughly a
five-to-one ratio of internal detections vs. external ones
Internal
(In this analysis, “internal” traffic refers to
communication where both the source and destination External
use internal (private) IP addresses, such as RFC1918
82.8%
ranges (e.g., 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16).
“External” traffic refers to communication where at least
one side uses a public IP address, even if both systems
belong to the same organization).

This ratio reflects the difference in how often internal
and external traffic is encrypted as these alerts are
raised when authentication information is sent without
transport-layer encryption.
Internal networks
Within internal networks, most plaintext-password
Rank Top Apps with Leaked Passwords (Internal)
detections were linked to directory services and
other authentication mechanisms that still rely on
1
 Lightweight Directory Access Protocol (LDAP)
unencrypted LDAP. LDAP is widely used within
organizations for user lookups, access control, and 2 Hypertext Transfer Protocol (HTTP)
interactions with shared resources. When it is not
3
 File Transfer Protocol (FTP)
configured with LDAPS or StartTLS, it transmits
credentials in cleartext.

4
 Databases (TNS/Postgres/TDS)
This made it the most common source of internal
5 Telnet
alerts. We also saw cleartext passwords in internal
web services, file-transfer utilities, and database
connections. These internal exposures were
consistent throughout the year, reflecting long-
standing configurations and legacy applications
rather than short-term mistakes.
20

External networks
Rank Top Apps with Leaked Passwords (External)
External plaintext-password alerts showed a very 1
 Databases (TNS/Postgres/TDS)
different pattern. The most frequent cases involved
2 File Transfer Protocol (FTP)
database protocols, unencrypted file transfer traffic,
and HTTP sessions without TLS encryption. In many
3
 Hypertext Transfer Protocol (HTTP)
of these alerts, both endpoints actually belonged to
the same organization but communicated with each
4
 Simple Mail Transfer Protocol (SMTP)
other through the public IP address of the service
rather than the internal one. 5 Apache Subversion (SVN)
This behavior is common in cloud or containerised
deployments, where services are exposed externally
through load balancers or NodePort-style
configurations and then inadvertently used by
internal components. Many external alerts also
appeared in spikes and then stopped, which
suggests temporary misconfigurations that were
corrected quickly after detection.
Taken together, the datasets show two distinct behaviors. Internal plaintext-password traffic
tends to come from established systems that have not yet been modernized to use
encrypted transport. External plaintext-password traffic is usually the result of deployment
or routing mistakes in more dynamic environments, and is often corrected once noticed.
These exposures relate directly to the OWASP Top Ten categories of Cryptographic Failures
and Security Misconfiguration, which highlight the risks created when sensitive data is
transmitted without encryption or when services are unintentionally exposed or configured
without proper safeguards.
21

Phishing: Scale, signal, and evolving
techniques
Phishing remains a persistent challenge for security In 2025, Intezer AI SOC processed 550,000
teams, not because of detection gaps alone, but phishing emails reported by end-users that
due to volume, user behavior, and rapidly evolving bypassed standard email security controls. A bit
attacker techniques. less than 8% were confirmed as malicious,
highlighting both the value and the operational cost
of user-driven reporting.
Number of emails analyzed Number of confirmed phishing emails
550,000 42,000
Count Count
Malicious emails with URL Malicious emails with attachments
13,000 2,500
Count Count
User reporting creates volume, but not always signal
While security awareness training encourages reporting suspicious emails, a small number of overzealous
users can generate disproportionate reporting volume, creating noise that can overwhelm security teams
and slow response to genuine threats.
Attackers are shifting focus from endpoint to
users’ browser
Less than 6% of reported phishing emails had an attachment and around 30% used links. This means that
artifact-based analysis is less efficient at triaging phishing emails, as most of them are language-based and
require a language model analysis process. The higher prevalence of links over attachments indicates that
threat actors are shifting their focus from gaining a foothold on the endpoint, which is well-protected, to
instead staying within the user's web browser, where today's security products have limited visibility.
22

Brand impersonation and callback scams dominate
Among confirmed malicious phishing emails:
Brand
Impersonation
Brand impersonation was the most common
Callback Scam
technique.
Credential
phishing link
Callback scams ranked second, often abusing
25.3% BEC
legitimate services to appear credible. 28.7%
New domain
Taken together with brand impersonations, more
QR Code
7.8%
than a third of malicious phishing emails are
Fake voicemail
abusing users' trust in well-known brands. notification
8.1% Victim
Impersonation
2%
9.4% Filesharing
2.8%
Service
2.3%
2.7% 4.1%
Other
Brand impersonation breakdown
Microsoft and DocuSign accounted for nearly 85%
of brand impersonation cases, underscoring how 3.1%
2.5% 6%
attackers exploit trusted brands to increase success
rates. While DocuSign essentially provides one
3.9%
Microsoft
product, Microsoft offers many products and
DocuSign
services that are being impersonated by threat
actors. Victim Org
46.1%
Paypal
Right behind impersonations of someone within the
victim’s organization (6%), PayPal, accounted for 38.3% Adobe
almost 4% of all brand impersonation phishing Norton
emails. While PayPal was more popular in callback
scams since those emails were sent by PayPal, we
don't classify them as impersonation emails.
23

For the phishing URLs that performed brand 2.9%1.8%
3.2%
impersonation, we see a similar trend. Microsoft
3.3% Generic
Microsoft was the most impersonated brand
representing nearly one-third of impersonation 3.6% 13.3% Cloudflare
URLs. Generic login pages represent almost 15% Other
5.9%
and Cloudflare almost 14% of URL impersonations.
Facebook
6% Crypto
31.8%
Scam
14.4% American
Express
WeTransfer
13.8%
Sendgrid
Fake store
Callback Scams
At the beginning of 2025, we started to see a
callback scam that abused both PayPal's and
Microsoft's infrastructure. Fortinet described how
the attack is performed in their January blog post.
In summary, the threat actor registers for a test
domain on Outlook 365 and creates a
distribution list.
In PayPal, the threat actor creates a payment
request that is sent to the distribution list. This
allows the threat actor to send one legitimate email
from PayPal to multiple victims that passes all the
standard email security checks.
This phishing email has two attacks. First, as
Fortinet described in the blog, if the victim clicks
the Pay Now link, they are redirected to PayPal's
website. PayPal wants to make it easy for users; it
will link the receiving email address to your PayPal
account if you choose to log in. Because the
attacker sent the phishing to their controlled email
address, this is the email address that will be added
to the victim's PayPal account.
24

The second attack is in the email. In the note Throughout the year, we have seen threat actors
section of the payment request, the attacker places evolving this attack. The recent phishing emails are
a message that encourages the victim to call a also using G-Suite in the delivery chain. The
specific phone number. The message is designed to phishing email in the figure was sent from PayPal to
appear as if it is from PayPal and requests the a mailbox hosted on G-Suite that bounced the email
recipient of the email to call the provided phone to an email address hosted on Outlook 365. The
number if they don't recognize the payment or have Outlook 365 mailbox is used to forward the email to
any questions. a distribution list that contains the victim’s email
address. You can also see in the screenshot that
Unicode homoglyphs are being used to make
signature-based detection harder.
25

Phishing infrastructure is becoming harder to detect
Threat actors have increased their use of CAPTCHA to make the detection of
phishing pages more difficult and apparently prefer Cloudflare's Turnstile over
Google's reCAPTCHA. The majority of URLs that use Google CAPTCHA could be
classified as safe, while the opposite is true for sites using Cloudflare Turnstile.
Safe Not safe
125000
100000
75000
50000
25000
0
Google Cloudflare
Recaptcha Turnstile
New phishing threats and attack vectors
As a benefit of analyzing a large amount of phishing These campaigns increasingly conceal malicious
emails and URLs, Intezer uncovered a striking shift content within trusted file formats, cloud services,
in attacker strategy, from simple deception to and dynamic web components, which are designed
structural and contextual evasion. to evade modern email and endpoint defenses.
26

Our research team identified four emerging phishing techniques that successfully
bypassed multiple email security gateways and reached end users:
Encoded JavaScript in SVG images. Obfuscated Base64 payloads redirect
victims to phishing sites, appearing as harmless graphics.
Hidden URLs in PDF annotations. Links are embedded in metadata fields (/
Annots arrays), making them invisible to scanners that rely on surface-level
content parsing.
Malicious URLs in OneDrive shares.
Cloud-hosted files dynamically load
phishing pages at runtime, exploiting
Microsoft’s trusted domain reputation.
27

MHT files embedded in OpenXML
documents. DOCX attachments conceal
archived HTML content or QR codes
leading to credential-harvesting portals.
These techniques highlight a growing
preference among attackers for non-
traditional delivery vectors that
exploit file format flexibility,
embedded scripting, and encoding,
sometimes in combination with the
trust associated with legitimate file-
sharing platforms.

By manipulating the structure of
formats like SVG, PDF, and OpenXML,
attackers conceal malicious content
in layers that most scanners
overlook, allowing phishing payloads
to penetrate even well-defended
environments.
28

Identity: High-value signals, high false-positive volume
Identity remains one of the most targeted and These alerts are primarily related to suspicious
valuable control planes in modern environments. In authentication activity, such as brute-force
2025, Intezer AI SOC analyzed millions of identity- attempts, failed multi-factor authentication (MFA)
related alerts from major identity providers, challenges, and sign-ins from unusual geographic
including Okta, JumpCloud, and Microsoft Entra ID. locations or unfamiliar devices.
The majority of identity alerts were driven by location-based anomalies (37%) and login failures (22%),
followed by MFA issues and brute-force attempts. Alerts also covered policy changes, privilege
modifications, and access enforcement events.
Rank Percent
Location / Geo / Session Anomalies 36.70%

Login Failures 22.00%

Brute Force / Password Attacks 8.20%

Account Lockouts 6.20%

MFA Issues
 11.90%

Privilege & Group Changes
 3.90%

Kerberos / Cert Thumbprint Activity
 2.50%

Access Policy Blocks
 2.60%

Other 6.00%
Most identity alerts are benign
Login verdicts
To better understand the nature of identity-related
activity, we analyzed output from our AI classifier,
7.1%
which integrates directly with customers’ identity
providers and evaluates recent authentication
events. The classifier examines login behavior,
contextual signals, and historical patterns to identify 18.6% Likely benign
unusual or risky activity. The breakdown below
Suspicious
shows how these events were ultimately classified. activity
Likely
From our data, we can see that most identity alerts malicious
are false positives. AI is good at recognising normal 74.1%
variability. The real threats show up only when
behavior sharply deviates across IP, geography,
and timing.
29

Impossible travel: High volume, low risk
Impossible-travel alerts, common features of identity and DLP products, were
frequent but rarely malicious. Only ~2% were confirmed as real compromises.
Here are some of the causes of the high false-positive rates:
VPN Usage
A large portion of false positives can be attributed to VPN usage. Both
commercial VPN services and internally managed VPN gateways contribute to
this pattern. When a user switches between their normal connection and a VPN
endpoint, the identity provider interprets the traffic as coming from two distant
locations in rapid succession. Roughly 30% of all impossible-travel alerts
involved some form of VPN activity.The most popular commercial VPNs
observed are NordVPN, Proton, SurfShark, Private Internet Access (PIA) and
ExpressVPN.
To triage these cases, we rely on tuning informed by threat intelligence,
customer feedback, and observed patterns that differentiate legitimate VPN
usage from suspicious activity. iCloud Private Relay also appears frequently and
links directly to mobile behavior.
Mobile
Mobile phones are another major driver of false positives. A typical case involves
phones a user logged in on a workstation, where the traffic originates from the
organization’s normal geographic region.

The same user then checks email or a messaging application on their phone
while using mobile data. Since mobile operators often route traffic through data
centres far from the user’s physical location, the identity provider flags the login
as a separate, distant location. This behavior alone accounts for a significant
share of impossible-travel alerts.
Security tools
We also see a pattern where security tools unintentionally trigger alerts against
each other. "Zero Trust" solutions, secure web gateways, and some email-
security products route or inspect traffic through their own infrastructure. This
causes authentication events to originate from cloud locations associated with
those services rather than the user’s true location. Identity platforms, SIEMs, and
DLP systems interpret these as unexpected logins and generate impossible-
travel alerts. These cases emphasize the recurring theme of overlapping security
products creating noise or misleading signals for one another.
30

Cloud: Persistence, evasion, and configuration drift
Cloud environments continue to evolve rapidly, These patterns suggest that most threats in cloud
introducing new forms of telemetry, behavior, and environments primarily focus on maintaining long-
detection opportunities. Our AI-SOC processes a term access while evading detection, often through
wide variety of cloud alerts across multiple techniques such as obfuscation, token manipulation,
platforms, including AWS, Azure, and GCP, as well and the misuse of legitimate cloud features.
as events generated by SIEM systems and native Discovery, Credential Access, and Resource
detection frameworks such as AWS GuardDuty. Development follow as common tactics, reflecting
attackers’ efforts to explore the environment,
Cloud alerts differ from traditional network or
harvest credentials, and prepare infrastructure for
endpoint detections in that they often represent
further operations. In contrast, high-impact
behavioural signals rather than discrete
behaviors such as Lateral Movement and Privilege
malicious artifacts.
Escalation appear far less frequently, suggesting
that early-stage stealth and identity-driven
The cloud alert data shows a strong concentration
techniques dominate cloud intrusions. This
of activity around Defense Evasion and Persistence,
distribution highlights the importance of
which together account for the majority of
organizations enhancing visibility into identity
observed TTPs.
misuse, covert persistence mechanisms, and subtle
evasion behaviors within their cloud environments.
Cloud alerts: seen TTPS and tactics
Defense Evasion
Persistence
Discovery
Credential Access
Resource Development
Command & Control
Exfiltration
Execution
Collection
Initial Access
Impact
Reconnaissance
Lateral Movement
Privilege Escalation
0 50000 100000 150000
31

Not the best practices
1%
Cloud posture tools such as AWS Security Hub
continuously evaluate an environment against
established security controls.
22%
Low
These controls represent recommended safeguards
40%
for ensuring the confidentiality, integrity, and Medium
availability of cloud resources. Most of these
Informational
violations fall into the low or informational
High
categories, which is expected for posture-centric 37%
findings where misconfigurations are more common
than immediate threats.
Across all services, S3 accounts for the largest share of control violations. When the alerts are grouped by
service, roughly 70% of all findings relate to S3 security hardening. The most frequently violated S3 controls
are those requiring SSL for bucket access, enforcing server access logging, and restricting bucket policies to
prevent cross-account access.
Taken together, these patterns suggest a recurring theme: many organizations still operate S3 buckets with
default or legacy settings that pre-date modern security expectations. Missing access logs reduces visibility,
weak cross-account policies increase the chance of accidental exposure, and a lack of enforced encryption
in transit leaves room for downgrade attacks or insecure client behavior. These issues are typically
configuration oversights rather than malicious activity, but they represent the type of long-lived weaknesses
that attackers routinely exploit when they gain a foothold elsewhere in an environment.
Rank Control Code Control Description
1
 S3.12 ACLs should not be used to manage user access to S3 general purpose buckets
2
 S3.9 S3 general purpose buckets should have server access logging enabled
3 S3.6 S3 general purpose bucket policies should restrict access to other AWS accounts
EC2 findings form the next major cluster. The most common violations involve EC2 instances using multiple
network interfaces, the presence of instances with public IPv4 addresses, and workloads running on
paravirtual or otherwise outdated instance types. These issues point to operational debt and legacy design
patterns persisting in production. Multiple ENIs are often linked to older architectures, complex routing
setups, or automation that attaches extra interfaces by default, and they can expand the attack surface and
complicate segmentation. Public IPv4 assignments similarly increase exposure to external probing. The
repeated appearance of deprecated instance families suggests that some workloads remain on historical
templates or provisioning pipelines that have not been refreshed to modern defaults.
32

While these controls are often classified as low-severity, the associated risk compounds when combined
with other cloud misconfigurations, particularly in environments without strong network segmentation.
Rank Control Code Control Description
1
 EC2.17 EC2 instances should not use multiple ENIs
2
 EC2.24 EC2 paravirtual instance types should not be used
3 EC2.9 EC2 instances should not have a public IPv4 address
When comparing S3 and EC2 together, a clear pattern emerges. S3 violations tend to reflect broad,
environment-wide defaults that were never fully aligned with AWS recommendations. EC2 violations, on the
other hand, often reflect application- or team-specific decisions, legacy infrastructure, or under-maintained
automation pipelines. S3 issues cluster around access control and encryption; EC2 issues cluster around
exposure and outdated configuration. Both categories highlight the gap between theoretical cloud-security
best practices and the reality of fast-moving infrastructure that accumulates configuration drift over time.
Control Violations per AWS Product
S3
EC2
GuardDuty
Inspector
IAM
CloudTrail
Macie
Other
0.00% 20.00% 40.00% 60.00%
Intezer AI SOC delivers 24/7, forensic-grade cyber alert triage across 100% of
alerts, with only 2% escalated for human review, dramatically accelerating
About Intezer
incident response. Powered by ForensicAI™, Intezer specializes in deep
forensic investigation to deliver unmatched accuracy and speed, significantly
reducing cyber risk and enabling security teams to operate effectively without
reliance on outsourced services. Intezer is trusted by global enterprises
including NVIDIA, MGM Resorts, Equifax, Salesforce, and Ferguson.
33

Appendix
The Rise and Fall of CrazyHunter
In early 2025, Intezer and Taiwan-based AIShield
collaborated on an investigation into a newly
emerged ransomware group dubbed CrazyHunter,
which launched a wave of coordinated attacks
against Taiwan’s healthcare, education, and energy
sectors. The campaign stood out for its
sophistication, despite the group’s apparent
newness, blending traditional double-extortion
tactics with modern evasion techniques.
The joint investigation combined AIShield’s local
telemetry with Intezer’s deep malware analysis
expertise to deliver a full technical breakdown of
CrazyHunter’s toolset and infrastructure. The
group’s operations revealed the use of vulnerable
drivers for privilege escalation, Active Directory
Group Policy abuse for lateral movement, and a Tor-
based leak site and Telegram channel for ransom
negotiations and public exposure.
Among the tools analyzed were
the ZammOcide AV-killer, which
exploits CVE-2018-6606, a loader
called "Syscall Phantom" that
bypasses EDR hooks, and
GoStealthFile, a Golang utility for
file exfiltration and remote
access. Their main payload,
“Hunter Ransomware,” was
derived from an open-source
project but reconfigured with their
own branding and modifications.
While its encryption
implementation was not the most
robust, the campaign’s
orchestration demonstrated real
operational maturity. Dark Web extortion site used by CrazyHunter
34

CrazyHunters Arsenal

| Tool | Category | Description  |
| ---- | -------- | ------------ |
Open-source Prince-based encryptor rebranded as “Hunter”; encrypts files
| Hunter Ransomware (Prince)
 | Ransomware
 |     |
| --------------------------- | ----------- | --- |
and drops ransom note.
Exploits vulnerable anti-malware driver (CVE-2018-6606) to terminate
| ZammOcide (C)
 | AV-killer
 | antivirus processes. |
| -------------- | ---------- | -------------------- |
Golang ZammOcide
 AV-killer
 Golang port of ZammOcide used similarly to disable endpoint protection.
Syscall Phantom
 Loader / Evasion
 Uses manual syscalls to bypass EDR hooks and inject shellcode in memory.
Golang utility for selective file deletion or serving files via embedded HTTP
| GoStealthFile
 | Exfiltration / Cleanup
 |     |
| -------------- | ----------------------- | --- |
server.
Open source .NET toolset to manipulate Group Policy Objects and schedule
| SharpGPOAbuse
 | Lateral movement
 |     |
| -------------- | ----------------- | --- |
tasks for persistence.
Staged bootstrap script coordinating AV killers, loaders, and ransomware
| Batch Orchestrater
 | Orchestration
 | execution. |
| ------------------- | -------------- | ---------- |
Cobalt Strike HTTPS beacon used for command-and-control and post-
| Cobalt Strike Beacon
 | C2 / Beacon
 |     |
| --------------------- | ------------ | --- |
exploitation.
Rex::Powershell (modified)
 Loader script
 PowerShell loader performing XOR decryption and in-memory beacon loading.
Taiwanese authorities have identified the operator  The case has been handed to the Taipei District
behind the CrazyHunter ransomware as a man  Prosecutors’ Office, which issued a wanted notice
surnamed Luo (羅)  from Zhejiang, China. Using IP  for Luo on charges including computer misuse,
data, malware code similarities, and behavioral  data protection violations, and extortion. This
analysis, investigators linked him to attacks that  confirmation marks a rare and significant instance
compromised over 500 systems and exposed about  of clear attribution in a ransomware investigation.

32.5 GB of patient data affecting more than 16
million people.
35

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-28", "model": "gemini-3.5-flash-lite"} -->
