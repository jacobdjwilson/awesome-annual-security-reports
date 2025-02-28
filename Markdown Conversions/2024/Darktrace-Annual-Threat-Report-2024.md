# Annual Threat Report 2024

## Table of Contents
- [Foreword](#foreword)
- [Methodology and Caveats](#methodology-and-caveats)
- [Preface](#preface)
- [Campaign overview](#campaign-overview)
- [Ransomware: Persistent threats and emerging strains](#ransomware-persistent-threats-and-emerging-strains)
- [RansomHub](#ransomhub)
- [Critical exploited vulnerabilities according to Darktrace](#critical-exploited-vulnerabilities-according-to-darktrace)
- [Email threats](#email-threats)
- [LOTL techniques](#lotl-techniques)
- [A view from the SOC](#a-view-from-the-soc)
- [The SOC’s Monthly Breakdown](#the-socs-monthly-breakdown)
- [Threats to Operational Technology (OT) and Industrial Control Systems (ICS)](#threats-to-operational-technology-ot-and-industrial-control-systems-ics)
- [Energy](#energy)
- [Healthcare](#healthcare)
- [Uncovering state-linked espionage](#uncovering-state-linked-espionage)
- [Recommendations from the Darktrace Threat Research team](#recommendations-from-the-darktrace-threat-research-team)
- [Community interest efforts](#community-interest-efforts)
- [Paris Olympic Games 2024 and the US presidential election](#paris-olympic-games-2024-and-the-us-presidential-election)
- [References](#references)

## Foreword

from Darktrace’s Threat Research team

It is with great interest and growing concern that we
present our findings for the 2024 Annual Darktrace
Threat report. At Darktrace, we approach threat
intelligence with a non-traditional perspective,
rooting in the belief that identifying behavioral
anomalies is crucial for identifying both known
and emerging threats in the landscape.

While continuing to understand the threat landscape, we also
have shifted to a more proactive approach to applying our
methodologies across different data elements, threat hunting
techniques, and community engagement across the cyber indus-
try. We believe this type of approach will not only improve early
warnings to our customers but also provide insight to different
critical infrastructure sector issues for the broader community.

As we continue to evolve in an increasingly digital world, there are
a few takeaways and observations that we would like to highlight.
Attackers are focusing more on evasion via edge device vulner-
abilities, Living-off-the-Land (LOTL), while also taking advantage
of compromised Software-as-a-Service (SaaS) credentials,
highlighting that identity continues to be an expensive problem
across the estate and a persistent source of pain across
enterprise and business networks.

Throughout 2024, we observed multiple threat trends across
Critical National Infrastructure (CNI), with one key observation
being the intensified race to identify software vulnerabilities.
In 2020 MITRE listed roughly 18,000 vulnerabilities, while the
current list for 2024 exceeds 29,000 [1].

There are a few explanations for this increase: the growth in
Common Vulnerabilities and Exposures (CVE) Numbering Au-
thorities (CNAs), with greater emphasis on finding vulnerabilities
through academic research, maturing “bug bounty” programs,
and ongoing research.

While the total number of vulnerabilities worldwide is around
240,000, it is important to note that the U.S. Cybersecurity and
Infrastructure Agency’s (CISA) Known Exploited Vulnerability
(KEV) catalog lists just over 1,200 vulnerabilities as being
actively exploited [2]. While threat actors continue to evade
detection as much as ever, understanding a smaller scope of
edge network technology allows for repeated reverse engineer-
ing and continued exploit findings, enabling zero-day discoveries
and initial access [3].

Ransomware groups are evolving their tactics beyond phishing to
include interactions with IT teams to elicit information to improve
access, SaaS-based attacks, and even studying file-transfer
technology for rapid exploitation and double extortion methods.

For IT administrators and practitioners, it is crucial to prioritize
your vulnerability management program and establish possible
attack paths across your estate to prevent unauthorised access.
This includes applying best practices across the business and
wider IT teams. Impact to CNI is a continued and growing concern
with the applications of AI-based capabilities for both offensive
and defensive teams [4].

The following sections of our Threat Report discuss these
broader concerns at a landscape level and how the Darktrace
Threat Research team’s findings mirrored a number of these
concerns.

A huge thank you
to the Darktrace Analyst team members and colleagues
across the wider business for their invaluable insights
and contributions to this report:
Adam Potter, Alexandra Sentenac, Anna Gilbertson,
Daniela Alvarado, Dylan Hinz, Emma Foulger, Freek Klein,
Iris Isac, Justin Frank, Justin Torres, Maria Geronikolou,
Min Kim, Nahisha Nobregas, Nathaniel Jones, Nicole Wong,
Ryan Traill, Safiy Soel, Sam Lister, Steven Sosa, Vivek Rajan,
Weronika Walczak and Zoe Tilsiter.

## Methodology and Caveats

This 2024 Annual Darktrace Threat Report is intended
for informational purposes only and is based on data,
trends, and analysis available at the time of publi-
cation. The contents of this report reflect the best
understanding of current and emerging threats in the
cybersecurity landscape. The information provided
is not exhaustive, and the nature of cybersecurity
threats can evolve rapidly.

While efforts have been made to ensure the accuracy and
reliability of the data and insights presented, Darktrace does
not guarantee the completeness or accuracy of the information.
Furthermore, Darktrace makes no representations or warranties,
either express or implied, regarding the effectiveness, sufficiency,
or applicability of the information provided in this report.

The findings and conclusions expressed in this report are
those of Darktrace and do not necessarily reflect the views or
endorsement of any third parties. Readers are encouraged to
conduct their own independent assessments and consult with
cybersecurity professionals to address specific security needs.
Darktrace is not liable for any direct, indirect, or consequential
damages arising from the use of or reliance on the information
provided in this report.

Darktrace’s Threat Research methodology
Darktrace’s Threat Research team conducts extensive research
across customer deployments to identify active threats, pinpoint
key Indicators of Compromise (IoCs), and provide relevant threat
intelligence.

This research leverages Darktrace’s anomaly-based detection
and involves thorough analysis and contextualization by the
Threat Research team. Detected threats are promptly reported
to the relevant customer security teams. When a customer has
Darktrace’s Autonomous Response technology enabled, these
threats are swiftly mitigated to prevent escalation.

Between January 1 and December 31, 2024, Darktrace investi-
gated a wide range of cyber threats. Many were identified as
campaign-like activities targeting multiple customers. All insights
from Darktrace’s analysis are based on detections and specific
data from our AI-driven applications and anomaly investigations.

‘Critical exploited vulnerabilities
according to Darktrace’ methodology
The ‘Most commonly observed exploited vulnerabilities’ listed
in the ‘Critical Exploited Vulnerabilities According to Darktrace’
section are based on confirmed exploitation attempts identified
across multiple customers using Darktrace / NETWORK. These
vulnerabilities, which affected the most Darktrace customers
between January 1 and December 31, 2024, are those where we
have triaged compromise activities that align with confirmed
IoCs, ascertained through our internal threat research and
Open-Source Intelligence (OSINT).

‘A view from the SOC’ methodology
The observations in the ‘A View from the SOC’ section of
this report are based on high-fidelity inputs analyzed through
Darktrace’s Managed Threat Detection and Security Operations
Support services. This analysis, conducted between January 1 and
December 31, 2024, involves both pattern analysis and assess-
ment of data significance. These insights are primarily qualitative
and reflect our SOC team’s evaluation of the most significant
cyber threats in 2024.

‘Email threats’ methodology
The statistics highlighted in the ‘Email threats’ section are derived
from analysis of monitored Darktrace / EMAIL model data for all
customer deployments hosted in the cloud between December
21, 2023, and December 18, 2024. Around 90% of the global
Darktrace customer base’s email environments are cloud-based.
Darktrace / EMAIL models are designed to alert for emails that
were considered 100% anomalous for a customer’s environment
and contained “phishing indicators”. For the purpose of this
report, and indeed Darktrace’s analysis of email environments,
“phishing indicators” refers to emails that are confirmed as mali-
cious, as opposed to merely unwanted spam emails. Darktrace /
EMAIL data is currently collected and processed every 28 days,
rather than monthly. Consequently, this analysis includes data
from outside the specified reporting period, specifically the last 10
days of December 2023. For the same reason, it does not include
December 19 through December 31, 2024, either.

## Preface

Darktrace’s Threat Research team has observed a
significant increase in sophisticated threat actors
targeting organizations within designated CNI globally
over the past year.

This trend is informed both by the heightened warnings from
national intelligence agencies as well as an overall focus of threat
analysis on activity identified within customers in these industries.
The targeting of CNI entities, and the subsequent operations
following access, suggest threat actors may be building strategic
pathways to yield geopolitical leverage in the event of conflict.
This reality manifests in both the focus and content of Darktrace’s
threat investigations throughout 2024.

The past year saw multiple high-profile public disclosures of
malicious activity within CNI sectors. The Darktrace Threat
Research team conducted threat hunting investigations across
the customer base driven by information suggesting Advanced
Persistent Threats (APTs) infiltrating CNI organizations.

For example, analysts searched for evidence of Salt Typhoon and
LiminalPanda activity in response to the public disclosure that
these groups were targeting Internet Service Providers (ISPs).
Additionally, 2024 saw the emergence of new ICS/OT native
malware like Fuxnet and FrostyGoop, as well as the continued
prevalence of ransomware groups targeting vulnerable industries
like healthcare. The Darktrace Threat Research team also con-
ducted multiple in-depth investigations for specific customers
in defense and government services showing indications of
compromise. These investigations yielded distinct evidence of
sophisticated threat actors operating within the networks of
high-profile defense and government customers that could be
leveraged in emerging geopolitical conflicts.

The varying methods of attack and long-term orientation of goals
by such threat actors will pose unique challenges to CNI organi-
zations. Many instances of CNI compromise have stemmed from
the exploitation of internet-facing devices through both zero-day
and known exploits.

Even when CVE exploitation was not present, threat actors can
and will rely on perimeter devices running external remote ser-
vices for access. IoCs are also increasingly proving less effective
at deterring such attacks. Groups such as VoltTyphoon continue
to build vast botnets of Internet of Things (IoT) (KV Botnet) and
internet-facing devices by exploiting unpatched systems. Usage
of these botnets and operational relay networks will assist in
evading detection and attribution, as evidenced in specific cases
investigated by the Darktrace team. Generally, APTs targeting CNI
sectors are also increasingly relying on LOTL tactics to remain
undetected.

Moreover, malicious groups exploiting CNI networks may have
differing aims based on their operating context. Some APT
groups may not have immediate objectives once persistence is
obtained within CNI networks. Potentially state-sponsored actors
may take a lay-and-wait approach: opting to sit within networks
with minimal activity beyond beaconing only increasing activity
when outside strategic conditions change [5].

Alternatively, threat actors targeting CNI organizations may
pursue a more aggressive approach by attempting to exfiltrate
sensitive data that can support broader strategic goals for
sponsor nations. Darktrace observed this pattern of behavior in
June-July 2024 when a government agency in the Asia-Pacific
(APAC) region was likely exploited by Mustang Panda to exfiltrate
sensitive data to cloud storage providers. Similarly, Darktrace
research identified evidence of a potential North Korean APT
exfiltrating data from a manufacturing organization, likely in
response to geopolitical developments. This trend extends even
to actors targeting sectors such as healthcare where Darktrace
analysts have observed a shift towards favoring data exfiltration
over traditional encryption during ransomware events.

Certain threat actors will also leverage malware aimed at causing
immediate disruption to suit their goals. This threat is particularly
relevant for organizations with Operational Technology (OT)
and Industrial Control Systems (ICS) environments, such as
customers within the energy sector, as well as traditional targets
of ransomware like hospitals and financial institutions.

Darktrace Threat Research analysts noted an uptick in attacks
in the energy sector motivated by disruption. The means of
disruption observed by Darktrace ranged from an OT specific
attack on Canadian energy provider’s PLC motor in the SCADA
environment at a field substation, to multiple Fog ransomware
attacks that successfully led to encryption. APT groups also are
increasingly targeting healthcare organizations for non-financial
goals. OSINT suggests many of these compromises attempted
to inhibit public health services to promote general instability.
This trend also became apparent in the evolution of Ransom-
ware-as-a-Service (RaaS) groups are leveraging such services in
furtherance of nation-state aims, targeting both healthcare and
non-medical organizations via ransomware platforms.

The following sections will further discuss and expand the trends
noted here by providing a review of Darktrace’s investigation into
specific industries and threats. Ultimately, the work Darktrace’s
Threat Research team has conducted during 2024 highlights the
increasing risk advanced cyber actors may pose to CNI organiza-
tions in 2025.

## Campaign overview

The most significant campaigns observed in 2024 involved the on-
going exploitation of zero-day and n-day vulnerabilities in edge and
perimeter network technologies. This widespread exploitation across
the threat landscape was consistent with Darktrace’s observations
throughout the year.

Operation Lunar Peek: Palo Alto Network firewall
devices (CVE 2024-0012 and 2024-9474

-   The second campaign observed related to PAN-OS firewall
    exploitation. Darktrace observed exploit validation and initial
    payload retrieval, C2 connectivity, among other activities.

-   The use of the Sliver C2 platform further differentiates the
    latest round of PAN-OS compromises, with evidence of Sliver
    activity in about half of the investigated cases.

-   For more information, read: Darktrace’s Inside the SOC Blog -
    Darktrace’s view on Operation Lunar Peek: Exploitation of Palo
    Alto firewall devices (CVE 2024-0012 and 2024-9474).

Honorable Mentions: Cleo and Jet Brains

-   2024 vulnerabilities in Cleo’s MFT software, namely CVE-
    2024-50623, and JetBrains TeamCity CVE 2024- 27198.

-   Highlights that ransomware groups particularly like to target file
    transfer applications, such as Cleo, for exfiltration and double
    extortion due to the significant amount of business information
    in these appliances. Meanwhile, JetBrains highlights that short-
    ened time-to-exploit has become fairly common for software
    deeply embedded in an organization’s supply chain.

-   For more information, read: Darktrace’s Inside the SOC Blogs -
    Race Against Time: Detecting JetBrains’ TeamCity Exploitation
    Activity with Darktrace and Cleo File Transfer Vulnerability:
    Patch Pitfalls and Darktrace’s Detection of Post-Exploitation
    Activities.

Beyond the specific campaigns observed and documented
by Darktrace, the following have become universal use cases
demonstrating how attackers continue to achieve success:

-   Adversary-in-the-Middle (AiTM) phishing threats like Mamba 2FA

-   Remote monitoring and management (RMM) tool usage
    (Supremo, AnyDesk, UltraVNC, SplashTop, N-able - formerly
    Solarwinds MSP, SimpleHelp) in ransomware campaigns,
    including Fog ransomware.

-   DNS tunneling in many campaigns, including the cryptomining
    operation CoinLoader.

Ivanti Connect Secure (CS) and Ivanti Policy Secure
(PS) appliances - CVE-2023-46805 and CVE-2024-21887

-   Amongst the observed activities, the following threads were
    identified as salient: exploit validation activity, exfiltration of
    system information, delivery of C2 implant from AWS, delivery
    of JavaScript credential stealer, SimpleHelp usage, and encrypt-
    ed C2 on port 53. ￼

-   For more information, read: Darktrace’s Inside the SOC Blog -
    The Unknown Unknowns: Post-Exploitation Activities of Ivanti
    CS/PS Appliances.

Palo Alo Network (PAN-OS)
Firewall Devices - CVE 2024-3400

-   A critical vulnerability in PAN-OS firewall devices was publicly
    disclosed on April 11, 2024. Due to anomaly-based detection,
    Darktrace’s Threat Research team identified a range of
    suspicious behavior as early as March 26, related to the
    exploitation of PAN-OS devices, including C2 connectivity,
    data exfiltration, and brute-forcing activity.

-   For more information, read: Darktrace’s Inside the SOC Blog
    - Post-Exploitation Activities on PAN-OS Devices: A Net-
    work-Based Analysis.

Fortinet - FortiManager CVE 2024-47575

-   This analysis focuses on the September 2024 exploitation of
    FortiManager via CVE-2024-47575, along with related malicious
    activity observed in June and September.

-   Campaign Comparison: Both Mandiant and Darktrace sources
    acknowledge the June exploitation attempts. The Darktrace
    article expands upon wider industry reporting by revealing a
    potentially broader campaign occurring earlier.

-   For more information, read: Darktrace’s Inside the SOC Blog

-   Post-Exploitation Activities on Fortinet Devices: A Net-
    work-Based Analysis.

Throughout 2024, Darktrace’s Threat Research team
sent out notifications to customers detailing cam-
paign activities observed on their deployments. In the
first half of the year, 40% of identified campaign
activity involved the exploitation of internet-facing
devices.

However, from June to December 2024, informa-
tion-stealer activity became the most prominent
campaign type identified by the Darktrace Threat
Research team.

Remote Access Trojans (RATs) also saw a significant
increase in the latter half of the year, representing
46% of campaigns identified, compared to only
12% in the first half.

Malware-as-a-Service (MaaS) accounted for 57%
of campaign activity identified by the Darktrace
Threat Research team in the latter half of 2024, up
from 40% between January and June.

![Image description: Model Alert in Darktrace / NETWORK showing the detection of malicious activity associated with the exploitation of PAN-OS prior to the vulnerability’s public disclosure.]

![Image description: Model Alert in Darktrace / NETWORK showing the detection of malicious connections associated with FortiManager devices in June 2024.]

## Ransomware: Persistent threats and emerging strains

While 2024 saw fewer ransomware cases globally compared to
the year before, the average payment per ransomware case rose
to USD 2.73 million, a USD 1 million increase from 2023 [6].
This rise is unsurprising given the continued adoption of the RaaS
model, providing even less experienced threat actors with the
tools needed to carry out disruptive attacks, significantly lowering
the barrier to entry.

Darktrace’s Threat Research team tracked several ransomware
threats across the fleet throughout 2024, observing novel strains
like Lynx, as well as re-emerging threats such as Akira, Ransom-
Hub, Black Basta, Fog, and Qilin (Agenda). Notable trends observed
by the team included the frequent use of phishing emails as an

attack vector and the use of legitimate tools like AnyDesk, Atera,
and Splashtop to mask malicious C2 communication.
LOTL techniques, such as using Windows Management
Instrumentation (WMI) and PSEXESVC for lateral movement,
are frequently employed, with administrative credentials often
used for privilege escalation. Data exfiltration to cloud storage
services like MEGA and Rclone is another trend, as these
services are commonly used for legitimate purposes.

This section will highlight five ransomware actors that the
Darktrace Threat Research team identified as significant
threats to organizations in 2024, and which are expected to
remain prominent in the threat landscape moving forward.

1.  Akira Ransomware

    -   Background: RaaS strain first observed in the wild in 2023,
        re-emerged in 2024 [7]

    -   Affected Customer Countries: Australia, Canada,
        South Africa, United Kingdom, United States

    -   Observed TTPs: Double extortion, incoming connections
        to Remote Desktop Protocol (RDP) servers, leveraging RDP
        during lateral movement and VMWare usage, encrypting
        files with “.akira” extension

2.  LockBit Ransomware

    -   Background: RaaS group described by the US Department of
        Justice as “the most active and destructive ransomware group
        in the world,” affecting over 2,500 victims in more than 120
        countries and accumulating more than USD 500 million ransom
        payments [8]. Despite the arrest of its members and developers
        [9], LockBit has remained a persist threat that Darktrace has
        continued to observe

    -   Affected Customer Countries: Global impact

    -   Observed TTPs: Abusing NetScan for reconnaissance,
        exploiting vulnerabilities in VMware ESXi devices

3.  Lynx Ransomware

    -   Background: First observed in the wild in 2024 as a successor
        to INC ransomware. Targets organizations across multiple
        sectors including real estate, retail, financial, and environmental
        services [10]

    -   Affected Customer Countries: United Kingdom and United
        States

    -   Observed TTPs: Phishing emails and malicious payloads as
        initial access, double extortion, encrypting files with “.LYNX”
        extension, likely using Restart Manager [10]. If encryption fails,
        actors attempt to escalate privileges. RDP connections to
        domain controller using administrator credentials

4.  Fog Ransomware

    -   Background: First observed in the wild around April/May 2024
        with most of its victims located in the United States and within
        the education sector. Variants of Fog ransomware exist for both
        Linux and Windows platforms [11][12][13]

    -   Affected Customer Countries: United States

    -   Observed TTPs: Compromised Virtual Private Network (VPN)
        credentials, unusual default admin credential usage, SMBv1
        lateral movement, anomalous connections to AnyDesk, large
        volumes of data exfiltration, and ‘.flocked’ or ‘.flock’ extensions

5.  RansomHub Ransomware

    -   Background: RaaS group first observed in the wild in February
        2024; known to target cloud storage backups and misconfigured
        Amazon S3 instances. Believed to have absorbed BlackCat/AL-
        PHV affiliates [14]. Darktrace observed ShadowSyndicate using
        RansomHub in multiple attacks in late 2024, affecting education
        manufacturing and social services sectors

    -   Affected Customer Countries: Global impact but avoids
        targeting entities in Commonwealth of Independent States
        (CIS), China, North Korea, or Cuba [15]

    -   Observed TTPs: Gains initial access via vulnerabilities in Win-
        dows, Linux, ESXI, NAS, and Zerologon (CVE-2020-1472), use of
        legitimate tools like Atera and Splashtop for C2 and NetScan for
        reconnaissance [16] [17]. Double extortion tactics

## RansomHub

-   Ransomware spotlight:
    Understanding
    RansomHub through
    the Diamond Model 

Organizations and entities face increasing chal-
lenges from sophisticated ransomware actors like
RansomHub. To better understand and analyze such
adversary activities, security analysts and researchers
widely use the Diamond Model of Intrusion Analysis, a
cybersecurity framework designed for this purpose.

By applying the Diamond Model and combining it with Darktrace’s
capabilities, Darktrace’s Threat Research team enhances its ability
to understand the behavior of these persistent adversaries.
This approach provides organizations with deeper insights and
proactive defense strategies.

The group operates under a RaaS model, recruiting affiliates to
execute attacks and providing them with the necessary tools,
infrastructure, and support.

Like most ransomware actors, they are financially motivated,
with their primary goal being to extort victims through double
extortion tactics—encrypting critical data and threatening to
release sensitive information unless a ransom is paid [15].

Darktrace’s Threat Research team investigated several customer
networks impacted by RansomHub in 2024. Attacks have contin-
ued into early 2025, with Darktrace’s Security Operations Center
(SOC) team investigating at least three additional cases.

Infrastructure analysis
RansomHub employs HTTPS and DNS-based communication
protocols to encrypt the data flow between compromised sys-
tems and their C2 servers, complicating efforts for defenders to
monitor or intercept these exchanges [17]. Additionally, RansomHub
frequently registers numerous domains through anonymized
services such as Tor to conceal ownership information, making
attribution increasingly challenging [17].

When the group drops their ransom note, it usually only con-
tains information directing the victim to a unique “.onion” URL
for payment and communication [17].

For the stolen data, the group employs dedicated servers and
cloud storage services to temporarily store the exfiltrated data, us-
ing this as leverage in their double extortion tactics by threatening
victims with public exposure. Once the victim agrees to make the

payment, they must do so using Bitcoin or Monero, as RansomHub
only accepts ransom payments exclusively in cryptocurrency [18].

Victim profiling 
RansomHub has reportedly attacked around 500 organizations
and entities, including high-profile attacks on Mexico’s presidential
legal counsel [19] and a Scottish housing society [20]. RansomHub
specifically targets victims across North America, Europe, and Asia,
with a particular focus on government agencies, financial institu-
tions, and healthcare providers, likely due to the critical nature of
their data and the potential financial impact [21] [22].

However, other sectors, including information technology,
emergency services, food and agriculture, and telecommunica-
tions, have also been targeted [23]. Alongside targeting critical
infrastructures, the group also targets specific individuals such
as C-level executives and IT administrators, aiming to obtain
privileged credentials that grant full network access [15].

The group does not attack non-profit organizations and has a
rule not to target victims who have already paid. Additionally,
RansomHub does not allow their affiliates to target members of
the Commonwealth of Independent States (CIS), Cuba, North
Korea, and China [15], potentially indicating the group’s location or
alignment.

Adversary identification 
Despite being a relatively young ransomware group, RansomHub
have quickly become known globally due to their aggressive
tactics and high-profile attacks. Their approach mirrors that of
predecessor groups like LockBit and ALPHV (BlackCat), with
reports suggesting that former members of these groups now
operate under RansomHub [14].

![Image description: The Diamond Model of Intrusion Analysis]

Capability analysis 
For initial access, RansomHub exploits known vulnerabilities in
internet-facing applications and uses phishing and spear-phishing
attacks to gain entry, along with credential stuffing and brute-
force attacks to exploit weak authentication mechanisms [17].
Once inside, RansomHub uses advanced exploitation techniques,
such as leveraging ZeroLogon (CVE-2020-1472) and deploying
EDRKillShifter, a tool designed to disable endpoint detection and
response (EDR) defenses [16] [24].

They use PowerShell scripts to execute malicious commands
and perform network reconnaissance, manipulating existing ac-
counts and re-enabling disabled accounts to escalate privileges.
Additionally, RansomHub uses tools such as Mimikatz to extract
credentials from compromised systems and exploits vulnerabilities
in SMBExec, AnyDesk, and Cobalt Strike to move laterally.

For encryption, the ransomware group typically employs an Elliptic
Curve Encryption algorithm called “Curve 25519”, which appends
unique 6-digit alphanumeric code extensions to encrypted files
[17]. For data exfiltration, they have been observed using tools such
as BITSAdmin, HTTP POST requests, and WinSCP to transfer
stolen data over web services [17].

Darktrace’s coverage of RansomHub
Focusing on the attacks observed by Darktrace, in the three
cases, the compromised devices were observed triggering multi-
ple C2-related models in Darktrace / NETWORK as they were
detected communicating with external C2 infrastructure. Further
investigation revealed that the devices were also communicating
on unusual TCP ports. These connections were detected based
on Darktrace’s ability to identify the rarity of the domains in
question, as well as the unusualness of the TCP ports used in
some of these connections.

As one of these customers was subscribed to Darktrace’s Man-
aged Threat Detection service, the SOC team promptly alerted
them about the observed activities when the first signs of an
emerging compromise were detected on the network.

In this case, Darktrace’s SOC analysts informed the customer of a

device receiving incoming connections using AnyDesk, performing
network scanning, and lateral movement on the network.
Following the first alert, Darktrace’s SOC sent multiple additional
alerts as the attack propagated rapidly on the network. Through-
out the course of the attack, Darktrace also detected affected
devices uploading a large amount of data to external endpoints,
including legitimate cloud services such as MEGA and Atera. This
activity was consistent with threat actors exfiltrating data as part
of their double extortion methods.

This malicious activity was detected due to the anomalous nature
of the device transferring a large volume of data externally. It is
important to note that the rarity of the external domain is not a
primary parameter for triggering models related to external data
transfer in Darktrace, as legitimate services can be exploited by
attackers, as seen with the use of MEGA and Atera in this case.

In contrast, the other two customers were not subscribed to
the Managed Threat Detection service and therefore were not
notified when the attackers gained access to their respective
networks. However, Darktrace’s SOC team was still able to
support them through the Security Operations Support service,
giving the customers direct access to Darktrace’s expert analysts.
The SOC analysts provided information on how the attack may
have started, a list of infected devices, details on how the attack
propagated, and a record of the files encrypted with the code
extension “.b2202a” by the attackers.

For more information, you can read Darktrace’s full
investigation into the deployment of RansomHub by the
ShadowSyndicate threat actor in late 2024, which features
a breakdown of the IoCs and TTPs observed and the
associated Darktrace / NETWORK models.

## Critical exploited vulnerabilities according to Darktrace

It is increasingly common for threat actors to
identify and exploit newly discovered vulnera-
bilities in widely used services and applications.
Attackers often prioritize developing exploits
for severe and global CVEs but typically find the
most success with known vulnerabilities within
the first couple of years after public disclosure.
In some cases, exploit validation occurs
within hours of disclosure.

Darktrace’s most commonly observed
exploited vulnerabilities in 2024

CVE-2024-3400

-   Vulnerable products: Palo Alto Networks firewall appliances
    running PAN-OS

-   Type of vulnerability: Command injection and improper
    input validation

-   Associated malware: Spark (backdoor)

-   Activity seen: Exploit validation activity, retrieval of binaries
    and shell scripts, data exfiltration via HTTP POST activity, and
    ongoing C2 communication with rare external endpoint

-   [Technical details and IoCs](#)

CVE-2023-46805 and CVE-2024-21887

-   Vulnerable products: Ivanti Connect Secure (CS)
    and Ivanti Policy Secure (PS)

-   Type of vulnerability: Authentication bypass via
    improper authentication and command injection

-   Associated malware: WARPWIRE, Monero cryptocurrency
    miner

-   Activity seen: Usage of Out-of-Band Application Security
    Testing (OAST) services for exploit validation, exfiltration of
    system information, delivery of AWS-hosted C2 implants,
    delivery of JavaScript credential stealers, usage of SimpleHelp
    (remote support software), usage of SSL-based C2, and the
    delivery of cryptocurrency miners

-   [Technical details and IoCs](#)

In 2024, the Darktrace Threat Research team identified
multiple campaigns where threat actors targeted vulnera-
bilities in internet-facing systems, as discussed earlier,
such as Ivanti CS/PS appliances, Palo Alto firewalls, Fortinet
appliances, Cleo software, ScreenConnect servers, and
TeamCity on-premises servers. These exploited vulnerabil-
ities were strongly associated with malware such as Spark,
WARPWIRE, Spectre RAT and CACTUS ransomware, as
well as malicious cryptocurrency activities.

Timely addressing these vulnerabilities reduces their effec-
tiveness, slowing malicious operations and forcing attackers
to pursue more costly and time-consuming methods, such
as zero-day exploits or software supply chain attacks. While
actors develop tools for other vulnerabilities, exploiting
critical and publicly known vulnerabilities provides them
with impactful, low-cost tools for extended use.

CVE 2024-23113 and CVE-2024-47575

-   Vulnerable products: FortiGate and FortiManager

-   Type of vulnerability: Use of externally controlled format
    string and missing authentication for critical function

-   Activity seen: Command execution on host, payload
    retrieval, and sensitive data exfiltration

-   [Technical details and IoCs](#)

CVE-2024-0012 and CVE-2024-9474

-   Vulnerable products: Palo Alto Networks Firewalls
    and PAN-OS (Web Management Interface)

-   Type of vulnerability: Authentication bypass via missing au-
    thentication for critical function and OS command injection

-   Associated malware: Spectre RAT

-   Activity seen: Exploit validation, initial payload retrieval, C2
    connectivity potentially featuring further binary downloads,
    potential reconnaissance and cryptocurrency mining activity

-   [Technical details and IoCs](#)

CVE-2023-48788

-   Vulnerable products: FortiClient EMS

-   Type of vulnerability: SQL Injection

-   Activity seen: Exploit validation, use of Sliver C2 framework,
    use of various RMM tools such as Splashtop, Atera, and
    AnyDesk, internal reconnaissance, privilege escalation, lateral
    movement, and sensitive data exfiltration

-   [Technical details and IoCs](#)

CVE-2024-1708 and CVE-2024-1709

-   Vulnerable products: ConnectWise Screen Connect

-   Type of vulnerability: Improper limitation of a pathname to a
    restricted directory (path traversal) and authentication bypass
    vulnerability

-   Activity seen: Outbound connections to suspicious end-
    points, use of PowerShell, executable file downloads

-   [Technical details and IoCs](#)

CVE-2024-50623

-   Vulnerable products: Cleo’s Managed File Transfer
    (MFT) Software

-   Type of vulnerability: Unrestricted upload