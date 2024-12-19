# X-Force Threat Intelligence Index 2022

## Table of Contents
  * [Executive summary](#executive-summary)
  * [Top attack types](#top-attack-types)
    * [Ransomware](#ransomware)
    * [Server access](#server-access)
    * [Business email compromise](#business-email-compromise)
  * [Top infection vectors](#top-infection-vectors)
    * [Phishing](#phishing)
    * [Vulnerability exploitation](#vulnerability-exploitation)
  * [Threats to operational technology and Internet of Things](#threats-to-operational-technology-and-internet-of-things)
    * [Threat actors accelerate reconnaissance against OT devices](#threat-actors-accelerate-reconnaissance-against-ot-devices)
    * [Manufacturing most targeted of OT industries, ransomware leads](#manufacturing-most-targeted-of-ot-industries-ransomware-leads)
    * [Mozi botnet continues to threaten IoT and OT assets](#mozi-botnet-continues-to-threaten-iot-and-ot-assets)
  * [Top threat actors of 2021](#top-threat-actors-of-2021)
    * [Suspected Iran-based ITG17 uses Aclip backdoor](#suspected-iran-based-itg17-uses-aclip-backdoor)
    * [ITG23—Trickbot Gang—enables Conti ransomware operations](#itg23trickbot-gangenables-conti-ransomware-operations)
    * [Hive0109 active in 2021](#hive0109-active-in-2021)
  * [Trends in malware development](#trends-in-malware-development)
    * [Next-level detection evasion](#next-level-detection-evasion)
    * [Malware focus on Docker](#malware-focus-on-docker)
    * [Ransomware focus on ESXi](#ransomware-focus-on-esxi)
    * [Nim is in](#nim-is-in)
    * [Linux threats continue to evolve](#linux-threats-continue-to-evolve)
    * [Threat actors target cloud environments](#threat-actors-target-cloud-environments)
    * [Fileless malware in the cloud](#fileless-malware-in-the-cloud)
  * [Geographic trends](#geographic-trends)
    * [Asia](#asia)
    * [Europe](#europe)
    * [North America](#north-america)
    * [Middle East and Africa](#middle-east-and-africa)
    * [Latin America](#latin-america)
  * [Industry trends](#industry-trends)
    * [#1  |  Manufacturing](#1--manufacturing)
    * [#2  |  Finance and insurance](#2--finance-and-insurance)
    * [#3  |  Professional and business services](#3--professional-and-business-services)
    * [#4  |  Energy](#4--energy)
    * [#5  |  Retail and wholesale](#5--retail-and-wholesale)
    * [#6  |  Healthcare](#6--healthcare)
    * [#7  |  Transportation](#7--transportation)
    * [#8  |  Government](#8--government)
    * [#9  |  Education](#9--education)
    * [#10 | Media](#10--media)
  * [Risk mitigation recommendations](#risk-mitigation-recommendations)
    * [Zero trust assists in decreasing risk of top attacks](#zero-trust-assists-in-decreasing-risk-of-top-attacks)
    * [Security automation enhances incident response](#security-automation-enhances-incident-response)
    * [Extended detection and response provides a significant advantage over attackers](#extended-detection-and-response-provides-a-significant-advantage-over-attackers)
    * [Recommendations](#recommendations)
  * [About IBM Security X-Force](#about-ibm-security-x-force)
  * [About IBM Security](#about-ibm-security)
  * [Contributors](#contributors)

The world continues to grapple with a lasting pandemic,  
shifts to work-from-home and back-to-office, and  
geopolitical changes spawning a constant drone of  
mistrust. All of this equates to chaos, and it is in chaos  
that cybercriminals thrive. In 2021, IBM Security® X-Force®  
saw how threat actors opportunistically used a shifting 
landscape to adopt tactics and techniques to successfully 
infiltrate organizations across the globe.

The IBM Security X-Force Threat Intelligence Index maps new trends and attack 
patterns we observed and analyzed from our data—drawing from billions of datapoints 
ranging from network and endpoint detection devices, incident response (IR) 
engagements, domain name tracking and more. This report represents the culmination 
of that research based on data collected from January to December 2021.

We offer these findings as a resource to IBM clients, researchers in the security industry, 
policy makers, the media and to the broader community of security professionals and 
business leaders. 

Given the volatile landscape and the evolution of both threat types and threat vectors, 
you need threat intelligence insights to stay ahead of attackers and fortify your critical 
assets more than ever.

<a id="executive-summary"></a>
## Executive summary

### Report highlights
*   **Top attack type:** Ransomware was again the top attack type in 2021, although the 
    percentage of attacks X-Force remediated that were ransomware decreased nearly 9% 
    year-over-year. REvil—a ransomware type X-Force also refers to as Sodinokibi—was 
    the most common ransomware strain X-Force observed for a second year, making up 
    37% of all ransomware attacks, followed by Ryuk at 13%. Law enforcement activity has 
    probably been the primary force driving down ransomware and IoT botnet attacks in 
    2021, but this does not preclude a potential resurgence in 2022.
*   **Supply chain vulnerabilities:** Supply chain security was pushed to the forefront of 
    government and policymakers’ attention, with the Biden administration’s executive 
    order on cybersecurity, and guidance from the U.S. Department of Homeland Security, 
    CISA, and NIST doubling down on zero trust guidance. These guidelines put a spotlight 
    on vulnerabilities and trusted relationships. Vulnerability exploitation was the top initial 
    attack vector in manufacturing, an industry grappling with the effects of supply chain 
    pressures and delays.
*   **Most phished brands:** X-Force closely tracked how cybercriminals are using phishing 
    kits throughout 2021, and our research revealed that Microsoft, Apple and Google were 
    the top three brands criminals attempted to mimic. These mega brands were used 
    repeatedly in phishing kits, with attackers likely seeking to capitalize on their popularity 
    and the trust many consumers place in them.
*   **Top threat groups:** Suspected Iranian nation-state threat actor ITG17 (MuddyWater), 
    cybercriminal group ITG23 (Trickbot), and Hive0109 (LemonDuck) were some of the 
    most active threat groups X-Force intelligence analysts observed in 2021. Threat groups 
    worldwide were seeking to augment their prowess and infiltrate more organizations. 
    Malware they used was embedded with greater defense-evasion techniques, in some 
    cases hosted via cloud-based messaging and storage platforms to get through security 
    controls. These platforms were abused to hide command and control communication 
    in legitimate network traffic. Threat actors also continued to develop Linux versions of 
    malware, to enable them to cross over to cloud environments more easily.

### Key stats
*   **21%**
    Ransomware share of attacks
    Ransomware was the number one attack type observed by X-Force last year, 
    decreasing to 21% of attacks from 23% in the previous year. REvil ransomware 
    actors (aka Sodinokibi) were responsible for 37% of all ransomware attacks.
*   **17 months**
    Average time before a ransomware gang rebrands or shuts down
    Ransomware gangs studied by X-Force had an average lifespan of 17 months 
    before rebranding or disbanding. REvil, one of the most successful gangs, shut 
    down in October 2021 after 31 months (two and a half years).
*   **41%**
    Percentage of attacks exploiting phishing for initial access 
    Phishing operations emerged as the top pathway to compromise in 2021, with 
    41% of incidents X-Force remediated using this technique to gain initial access.
*   **33%** 
    Increase in the number of incidents caused by  
    vulnerability exploitations from 2020 to 2021  
    Four out of the top five vulnerabilities exploited in 2021 were new vulnerabilities, 
    including the Log4j vulnerability CVE-2021-44228—which was ranked number 
    two, despite only being disclosed in December.
*   **3X**
    Click effectiveness for targeted phishing campaigns that add phone calls 
    The click rate for the average targeted phishing campaign was 17.8%, but targeted 
    phishing campaigns that added phone calls (vishing or voice phishing) were three 
    times more effective, netting a click from 53.2% of victims.
*   **146%** 
    Increase in Linux ransomware with new code
    The percentage of Linux ransomware with unique (new) code increased  
    year-over-year by 146%, according to Intezer, indicating an increase in the  
    level of Linux ransomware innovation.
*   **#1** 
    Manufacturing industry rank for attacks 
    Manufacturing replaced financial services as the top attacked industry in 2021, 
    representing 23.2% of the attacks X-Force remediated last year. Ransomware was 
    the top attack type, accounting for 23% of attacks on manufacturing companies.
*   **61%** 
    Manufacturing share of compromises on OT-connected organizations
    Sixty-one percent of incidents at OT-connected organizations last year were 
    in the manufacturing industry. In addition, 36% of attacks on OT-connected 
    organizations were ransomware.
*   **2,204%** 
    Increase in reconnaissance against OT
    Attackers increased their reconnaissance of SCADA Modbus OT devices  
    accessible via the internet by 2,204% between January and September 2021.
*   **74%** 
    Share of IoT attacks originating from Mozi botnet
    In 2021, attacks against IoT devices originated from the Mozi botnet  
    74% of the time.
*   **26%**
    Share of global attacks that targeted Asia
    Twenty-six percent of all attacks had targets in Asia in their crosshairs.  
    Asia was the most attacked geography of 2021.

<a id="top-attack-types"></a>
## Top attack types
For the purposes of this report, we categorize attack 
types by the end goal an attacker is seeking to 
achieve once they have gained access to a victim’s 
network. Attack types differ from initial infection 
vectors, with the latter being the initial method of 
entry into a network. 

As examples, some attack types include ransomware, data theft, and 
BEC, based on the end goal of the threat actor’s operation. Examples of 
initial infection vectors include phishing, using stolen credentials, and 
vulnerability exploitation.  

The following sections provide details and data on the most prolific 
attack types our data revealed in 2021.

<a id="ransomware"></a>
### Ransomware
For more than three years, ransomware has been the top attack type 
observed by X-Force, and 2021 was no exception. Twenty-one percent 
of attacks remediated by X-Force incident response in 2021 were 
ransomware attacks. This is down slightly from the year prior, when 23% 
of attacks X-Force remediated were ransomware attacks; however, the 
volume of ransomware attacks has remained steady year-over-year.

*Image description: A pie chart comparing top attack types in 2020 and 2021. In 2020, ransomware was 23%, data theft was 13%, BEC was 8%, server access was 10%, credential harvesting was 6%, RAT was 5%, misconfiguration was 5%, malicious insider was 5%, and other was 27%. In 2021, ransomware was 21%, data theft was 14%, BEC was 9%, server access was 11%, credential harvesting was 6%, RAT was 5%, misconfiguration was 5%, malicious insider was 5%, and other was 23%.*

**Figure 1**
Top attack types, 2021 vs. 2020
Breakdown of top attack types, 2020-2021 (Source: IBM Security X-Force)<sup>1</sup>

The frequency of ransomware attacks X-Force observes tends to shift throughout the 
year, with May and June tending to see higher frequencies of attacks, while January 
tends to see lower. In addition, ransomware attacks appear to decrease in late summer 
or early fall. In 2021, that drop largely came in August and again in November, likely 
spurred by the permanent or temporary shutdown of several groups in the months prior: 
DarkSide and Babuk in May, Avaddon in June, and REvil in October.

*Image description: A line graph comparing the percentage of IR incidents that were ransomware by month in 2020 and 2021. In 2020, the percentages were: January 6%, February 27%, March 27%, April 24%, May 22%, June 19%, July 13%, August 30%, September 36%, October 33%, November 50%, and December 25%. In 2021, the percentages were: January 18%, February 35%, March 10%, April 6%, May 25%, June 15%, July 5%, August 43%, September 29%, October 14%, November 0%, and December 20%.*

**Figure 2**
Percentage of IR incidents that were ransomware, by month, 2020 vs. 2021
Percentage of X-Force Incident Response engagements that were ransomware, 2020-2021 (Source: IBM Security X-Force)

According to X-Force research, 17 months is the average 
time before a ransomware group either rebrands or shuts 
down, with a median of 18 months. Ransomware groups 
often spring up and rebrand once there is a threat of 
arrest or action by law enforcement. In some cases, law 
enforcement action forces ransomware groups to shut 
down entirely. Despite this dynamic environment—or 
perhaps because of it—many ransomware actors remain 
at large, and X-Force assesses that criminal ransomware 
activity will continue into the foreseeable future, based 
on the high profits generated by this activity and current 
limitations on law enforcement for widely shutting 
down ransomware activity. X-Force is aware of many 
ransomware actors that have rebranded and continued 
operations under new names, with GandCrab to REvil, 
Maze to Egregor, and DoppelPaymer to Grief as examples.

Law enforcement activity is probably the primary factor 
driving down the percentage of ransomware attacks 
X-Force observed in 2021, but it is very likely that the 
groups we have seen disappear will rebrand and re-
emerge in 2022 under new names and that ransomware 
activity will continue.

> “Many ransomware 
> actors have continued 
> operations under  
> new names”

*Image description: A timeline showing the lifespan of various ransomware groups from 2017 to 2022. The groups and their lifespans are: GandCrab (Feb 2017 - May 2019), Hermes (Jan 2018 - May 2019), Maze (Aug 2019 - Apr 2020), DoppelPaymer (Aug 2019 - Jan 2021), Nemty (Jan 2020 - Aug 2021), NetWalker (Feb 2019 - Jun 2021), Ragnarok (Apr 2019 - Oct 2021), DarkSide (Aug 2020 - May 2021), Avaddon (Jul 2021 - Nov 2021), REvil/Sodinokibi (May 2019 - Nov 2020), Babuk (Sep 2020 - Feb 2021), BlackMatter (Oct 2020 - May 2021), and Egregor (Jul 2021 - Nov 2021). The average lifespan is 17 months, and the median lifespan is 18 months.*

**Figure 3**
Ransomware groups that have shut down
Sample of ransomware groups that have shut down, 2017-2021  
(Source: IBM Security X-Force)

Of the ransomware strains observed by X-Force in 2021, REvil made up 37%—over one-
third—of all ransomware incidents our team remediated. A strong second was Ryuk, 
making up 13% of attacks observed last year. REvil actors as of mid-October 2021 
appear to have permanently shut down operations, probably due to law enforcement 
activity. Both Ryuk and REvil constitute some of the longest-running ransomware 
operations, having emerged in April 2019 and August 2018, respectively.

*Image description: A pie chart showing the types of ransomware observed by X-Force Incident Response in 2021. REvil was 37%, Ryuk was 13%, LockBit 2.0 was 7%, Ragnar Locker was 3%, Nefilim was 3%, Medusa was 3%, Eking was 3%, DarkSide was 3%, Crystal was 3%, CryptoLocker was 3%, Conti was 3%, BlackMatter was 3%, BitLocker was 3%, AvosLocker was 3%, AtomSilo was 3%, and Xorist was 3%.*

**Figure 4**
Types of ransomware observed in 2021
Ransomware types observed by X-Force Incident Response in 2021  
(Source: IBM Security X-Force)

#### How ransomware attacks happen
Given the deep experience X-Force Incident Response (X-Force IR) has in remediating 
ransomware attacks, our team has observed a recent pattern emerge across the vast 
majority of ransomware attacks. In particular, we have been able to develop a five-stage 
model that defines the common pattern observed in most ransomware incidents.

*Image description: A diagram illustrating the five stages of a ransomware attack. Stage 1 is "Initial access" and includes phishing emails or exploits of internet-facing services. Stage 2 is "Post exploitation" and includes persistent access established via tasks, run keys, RATs, etc., as well as second stage malware/post-exploitation toolkits and interactive attacker establishing access to the system. Stage 3 is "Understand and expand" and includes gathering credentials, local reconnaissance (local users, groups, tasklist, etc.), Active Directory reconnaissance (gather list of domain admins and domain controllers), and SMB lateral movement. Stage 4 is "Data collection and exfiltration" and includes reconnaissance, gathering credentials, gathering lists of hostnames/subnets to target for ransomware, gathering lists of data sources, data exfiltration (WinSCP, Rclone, etc.), and obtaining domain administrator privileges. Stage 5 is "Ransomware deployment" and includes command and control, staging ransomware on a share, and deploying ransomware using domain administrator credentials via PsExec/SMB/group policy.*

**Figure 5**
Stages of a ransomware attack
Standard attack flow for ransomware attacks, as observed by  
X-Force Incident Response (Source: IBM Security X-Force)

A concerning new trend in ransomware has been the expansion of “triple extortion” 
tactics. In this type of attack, threat actors encrypt and steal data and also threaten 
to engage in a distributed denial of service (DDoS) attack against the affected 
organization. This kind of attack is particularly problematic for organizations 
because victims have their networks held hostage with two kinds of malicious 
attacks—often simultaneously—and are then further victimized by the theft (and 
often leak) of data.  

Ransomware gangs are beginning to look to their primary victim’s extended 
business partners to pressure them into paying a ransom to prevent their own  
data leakages or business disruptions caused by the ransomware attack.

<a id="server-access"></a>
### Server access
Server access attacks—where the attacker gained unauthorized access to a server,  
but the final end goal is unknown—was the second-most common attack type,  
making up 11% of all incidents X-Force IR team remediated in 2021. 

The majority of these attacks occurred in Asia, and in many cases the threat actors 
were successful in deploying malware or employing penetration testing tools on 
a server, including China Chopper Webshells, Black Orifice malware, Printspoofer, 
and Mimikatz. 

In some instances, the threat actors exploited a known vulnerability, such as  
CVE-2020-7961, which would allow for remote code execution on a server.  
In multiple cases threat actors exploited vulnerabilities in Microsoft Exchange  
servers to gain unauthorized access to networks of interest. These vulnerabilities  
are included in the top 10 vulnerabilities of 2021 listed below.

Some of the server access attacks observed by X-Force’s IR team may have  
been failed attempts to steal data or deploy ransomware. Thus, while companies 
aim to prevent attackers from gaining any level of unauthorized access to their 
networks, it’s likely that a high number of server access attacks indicates that 
organizations are identifying and eradicating attacks before they progress into 
more damaging operations.

> 11%
> of attacks were  
> server access

<a id="business-email-compromise"></a>
### Business email compromise
After a downturn in business email compromise (BEC) attacks in 2020, X-Force observed 
a decrease in this attack type again in 2021. BEC was the third-most common attack 
type remediated by our X-Force IR team. Last year, we theorized that widespread 
implementation of multifactor authentication (MFA) was decreasing the number of 
successful attacks BEC threat actors were able to execute. That theory held in 2021, 
since BEC attackers may have realized greater success by shifting focus to geographies 
where MFA is not as widely implemented.

For example, Latin American organizations appeared to be bearing the brunt of BEC 
attacks the X-Force IR team is remediating. North American organizations were still 
strongly in the crosshairs of BEC operations, but the surge we noticed against Latin 
American organizations suggests that BEC attackers shifted the geographic focus of their 
operations: zero percent of attacks against Latin American organizations were BEC in 
2019, but 19% of attacks were BEC in 2020 and 20% of attacks in 2021 were BEC.

*Image description: A bar chart showing the percentage of incidents that were BEC in each region in 2021. Latin America was 20.0%, Asia was 11.6%, Middle East and Africa was 0.0%, Europe was 5.9%, and North America was 4.3%.*

**Figure 6**
Percentage of incidents that were BEC, 2021
Percentage of incidents that were BEC in each region, 2021 (Source: IBM Security X-Force)

<a id="top-infection-vectors"></a>
## Top infection vectors
In addition to examining the end goal of threat actors X-Force 
observes, our team also tracks how threat actors gain initial 
access to victims’ networks. Phishing and vulnerability 
exploitation tend to be the most common methods we observe, 
followed by use of stolen credentials, brute force, remote 
desktop protocol (RDP), removable media and password 
spraying making up a small percentage of intrusions.

*Image description: A bar chart comparing top infection vectors in 2020 and 2021. In 2020, phishing was 34%, vulnerability exploitation was 33%, stolen credentials was 18%, brute force was 7%, remote desktop was 4%, removable media was 4%, and password spraying was 0%. In 2021, phishing was 41%, vulnerability exploitation was 35%, stolen credentials was 9%, brute force was 6%, remote desktop was 4%, removable media was 4%, and password spraying was 1%.*

**Figure 7**
Top infection vectors, 2021 vs. 2020
Breakdown of infection vectors observed by X-Force Incident Response, 2020-2021 (Source: IBM Security X-Force)

Part of X-Force Red’s focus areas include conducting social engineering penetration testing attacks 
through phishing emails. For targeted phishing campaigns in 2020 and 2021, the average click rate for 
an X-Force Red simulated campaign was 17.8%. When vishing (voice phishing) phone calls were added 
to the campaign, the click rate rose to 53.2%, three times as effective. 

BEC attackers have leveraged phishing campaigns and social engineering with great success.  
And particularly in 2021, X-Force observed ransomware actors rely even more heavily on phishing 
campaigns to gain initial access to victim networks for ransomware attacks.

<a id="phishing"></a>
### Phishing
Phishing emerged as the top infection vector in 2021, surpassing vulnerability exploitation, which took 
the lead in 2020. Phishing was observed in 41% of the incidents X-Force remediated. While vulnerability 
exploitation dominated in Q3 of 2021, the significant number of phishing-related incidents X-Force 
observed in Q1 and Q4 pushed this infection vector into the lead for the year.

*Image description: A line graph showing the percentage of attacks tied to phishing, vulnerability exploitation, and stolen credentials by quarter in 2021. In Q1, phishing was 37%, vulnerability exploitation was 5%, and stolen credentials was 47%. In Q2, phishing was 31%, vulnerability exploitation was 42%, and stolen credentials was 7%. In Q3, phishing was 30%, vulnerability exploitation was 52%, and stolen credentials was 23%. In Q4, phishing was 36%, vulnerability exploitation was 7%, and stolen credentials was 22%.*

**Figure 8**
Percentage of attacks tied to phishing, vulnerability exploitation,  
and stolen credentials, by quarter, 2021
Percentage of attacks linked with various infection vectors, by quarter, in 2021 (Source: IBM Security X-Force)

For example, multiple REvil ransomware incidents observed in 2021 began with a QakBot phishing 
email. These emails usually have very short messages, often refer to unpaid invoices, and occasionally 
will even hijack ongoing email conversations and reply all with only a malicious attachment. 
When opened, the document will instruct the recipient to enable macros which will drop the QakBot 
banking trojan, gaining an initial foothold on a system. The operation is then transferred to REvil 
ransomware actors who conduct reconnaissance and proceed with the operation from there.

*Image description: An example of a QakBot phishing email. The email is titled "Payment Invoice" and has a short message: "Please find attached the payment invoice. Regards." The email has a malicious attachment.*

**Figure 9**
Sample QakBot phishing email
Example of QakBot phishing email with malicious attachment (Source: IBM Security X-Force)

#### Phishing kit deployments short-lived, abuse technology and bank brands
IBM analyzed thousands of phishing kits from around the world to determine the 
frequency and effectiveness of this particular attack vector. Our investigation suggests 
that malicious actors who use phishing kits probably put in tedious hours with limited 
gains. In particular, our investigation showed that:
*   Phishing kit deployments generally had a short lifespan, with almost one-third of 
    deployed kits being used for no longer than a day. In some cases, an individual 
    deployment of a phishing kit lasted only seven-to-eight hours before most hosting 
    providers identified the site as malicious and blocked it.
*   Each deployment on average had no greater than 75 potential victims who visited  
    the site.
*   Phishing kits asked for user credentials (email/ID/password combinations) in nearly 
    every kit observed (close to 100%), followed in popularity by credit card data (61% 
    of requests), mailing address (40%), phone number (22%), date of birth (17%), 
    identity card number (15%), security questions (14%), and ATM PINs (3%). 

When the recipient attempts to open the attachment, they are prompted by a popup  
(see figure 10) to enable macros by choosing “Enable editing” and “Enable content.” 
This allows the threat actor to deploy malware on the victim’s machine with the 
assistance of malicious macros.

*Image description: A screenshot of a popup message from a QakBot phishing attachment. The message prompts the recipient to enable macros by choosing "Enable editing" and "Enable content".*

**Figure 10**
Sample popup message from QakBot phishing attachment
Message in malicious attachment prompting the recipient to enable macros (Source: IBM Security X-Force)

#### Top 11 most spoofed brands of 2021
1.  Microsoft
2.  Apple
3.  Google
4.  BMO Harris Bank (BMO)
5.  Chase
6.  Amazon
7.  Dropbox
8.  DHL
9.  CNN
10. Hotmail
11. Facebook

In addition, X-Force looked at which brands were most frequently 
spoofed in phishing kits. The top brands included large technology 
companies and large financial institutions. The top 11 brands are 
listed below.

The Anti Phishing Work Group (APWG) noted that June 2021 set an 
all-time record high with 222,127 phishing attacks that month alone. 
X-Force assesses with high confidence that phishing kits will continue to 
be used by threat actors due to their easy-to-use nature and low resource 
requirement. Monitoring for suspicious connections to likely spoofed 
brands can help organizations minimize the probability of impact from 
this attack vector.

Using a DNS service that’s dedicated to data privacy, like Quad9<sup>2</sup>, can 
also help mitigate the risk of phishing attacks.

> <sup>2</sup> IBM Security X-Force is a Quad9 partner.

> 222,127
> phishing attacks in  
> June 2021, setting an  
> all-time record high

<a id="vulnerability-exploitation"></a>
### Vulnerability exploitation
Despite dropping to the second-most common in 2021, the number of incidents  
that were caused by vulnerability exploitation this past year rose 33% from 2020, 
indicating this attack vector’s strong hold in threat actors’ arsenals. This vector  
allows threat actors to gain access to victim networks for further operations— 
in many cases with elevated privileges. 

X-Force observed actors leveraging multiple known vulnerabilities, such as  
CVE-2021-35464 (a Java deserialization vulnerability) and CVE-2019-19781  
(a Citrix path traversal flaw), to gain initial access to networks of interest. In addition,  
we observed threat actors leverage zero-day vulnerabilities in major attacks like  
the Kaseya ransomware attack and Microsoft Exchange Server incidents to access  
victim networks and devices. 

Near the end of 2021, widespread exploitation of the Log4j vulnerability  
CVE-2021-44228 also launched this vulnerability into second place in X-Force’s  
top 10 list for 2021. Several mitigation measures can assist your organization  
in avoiding becoming a victim of this vulnerability.

#### Number of vulnerabilities hit another record high
Over the past five years, the number of vulnerabilities discovered per year his risen 
steadily. Even more concerning is that the number of exploits—tools threat actors can 
use to exploit a vulnerability—are also rising steadily, creating an ever-expanding array  
of options for threat actors seeking to exploit vulnerabilities. 

Vulnerabilities related to Internet of Things (IoT) and industrial control systems (ICS) 
increased at an even faster rate than overall vulnerabilities, with these two categories 
experiencing a 16% and 50% year-over-year increase respectively, compared to a 0.4% 
growth rate in the number of vulnerabilities overall.

*Image description: A line graph showing the number of vulnerabilities discovered per year from 2011 to 2021, as well as the cumulative number of vulnerabilities. In 2011, 7,380 new vulnerabilities were discovered, with a cumulative total of 40,000. In 2012, 8,460 new vulnerabilities were discovered, with a cumulative total of 50,000. In 2013, 8,661 new vulnerabilities were discovered, with a cumulative total of 60,000. In 2014, 9,666 new vulnerabilities were discovered, with a cumulative total of 70,000. In 2015, 9,875 new vulnerabilities were discovered, with a cumulative total of 80,000. In 2016, 11,212 new vulnerabilities were discovered, with a cumulative total of 100,000. In 2017, 16,621 new vulnerabilities were discovered, with a cumulative total of 120,000. In 2018, 17,859 new vulnerabilities were discovered, with a cumulative total of 140,000. In 2019, 17,997 new vulnerabilities were discovered, with a cumulative total of 160,000. In 2020, 19,137 new vulnerabilities were discovered, with a cumulative total of 180,000. In 2021, 19,649 new vulnerabilities were discovered, with a cumulative total of 200,000.*

**Figure 11**
Vulnerabilities discovered by year, 2011-2021
New vulnerabilities identified each year, 2011-2021, and cumulative number  
of vulnerabilities (Source: IBM Security X-Force)

#### Top 10 vulnerabilities of 2021
While any vulnerability carries risk and should be assessed, the following list includes the top 
vulnerabilities that X-Force IR observed threat actors exploit or attempt to exploit during the course 
of operations in 2021. X-Force recommends prioritizing patching of these vulnerabilities if your 
organization has not done so already.
1.  CVE-2021-34523 – Microsoft Exchange server flaw 
    enabling malicious actors to bypass authentication 
    and impersonate an administrator. Known generically 
    as ProxyLogon.
2.  CVE-2021-44228 – Vulnerability in