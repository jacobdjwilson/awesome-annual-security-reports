# 2023 State of the Threat: A Year in Review

## Table of Contents
- [Letter From Our Vice President, Threat Research](#letter-from-our-vice-president-threat-research)
- [Executive Summary and Key Findings](#executive-summary-and-key-findings)
- [The Business of Cybercrime—Is Boomtime Back?](#the-business-of-cybercrimeis-boomtime-back)
- [Innovations in TTPs Occur When Infection Chains Are Forced to Evolve](#innovations-in-ttps-occur-when-infection-chains-are-forced-to-evolve)
- [State-Sponsored Threat Activity](#state-sponsored-threat-activity)
- [Threat Actor Use of Artificial Intelligence](#threat-actor-use-of-artificial-intelligence)
- [Conclusion](#conclusion)
- [Appendix](#appendix)

A  Y E A R  I N  R E V I E W
State of the Threat
7 T H  E D I T I O N
2
2023 State of the Threat: A Year in Review

The war in Ukraine continues to dominate the headlines, both in 
terms of kinetic military action and of hostile pro-Russia cyber 
activity. It is not surprising that Russian state-sponsored threat 
groups persist in conducting attacks against targets in Ukraine and in 
countries that have vocally supported Ukraine in the conflict.
For the first few months after Russia's invasion of Ukraine on 
February 24, 2022, it looked as if an unexpected but welcome victim 
of the war might be the cybercrime ecosystem, as the number of 
successful ransomware attacks dropped. 
Eighteen months on, that optimism appears short lived. 
Ransomware attack numbers have rapidly returned to and then 
exceeded normal levels over the period of this report. Some well-
known ransomware operator names remain highly active, and 
new groups are joining the fray too. Other threat actors have 
also continued to concern our customers, from business email 
compromise attackers to Chinese cyberespionage groups, to North 
Korean attackers focused on cryptocurrency theft.
The Secureworks® Counter Threat Unit™ (CTU) gathers the data 
obtained from the trillions of events processed by our Taegis™ XDR 
platform. We combine it with insights from engagements carried 
out by the Secureworks Incident Response team, dynamic threat 
actor emulation activities, extensive monitoring of the Dark Web 
and underground forums, coupled with proactive research into 
cyberattacks to create a unique view of the threat landscape. All 
these data points then feed back into Taegis, creating a virtuous 
circle that further combines with the wealth of human expertise we 
offer to help keep our customers safe.
This report distills our findings to share with you, drawing and 
building on the specialist threat intelligence we have published to our 
customers over the period this report covers. It specifically focuses 
on how threat actor behavior has evolved over the past twelve 
months, both in terms of tooling and tactics. 
We hope the information presented here proves both an interesting 
and useful part of your security journey.
Sincerely,
3
2023 State of the Threat: A Year in Review

# Letter From Our Vice President, Threat Research
Don Smith
Vice President, Threat Research
Secureworks
4
2023 State of the Threat: A Year in Review

# Executive Summary and Key Findings
Over the past year, both cybercriminal and state-sponsored threat 
actors have maintained high levels of activity, meaning that the 
threat level to businesses remains as elevated as ever. The range of 
threats remains broad, from the temporary nuisance of hacktivist 
denial of service attacks to wiper attacks or IP theft and other 
types of cyberespionage, from business email compromise to data 
exfiltration attacks or business-threatening ransomware attacks. 
Precursor cyber activity continues at scale, delivering the malware 
that makes many of these cyberattacks, particularly ransomware 
attacks, easier and faster to carry out.
Amidst all this, Secureworks® Counter Threat Unit™ (CTU) 
researchers continue to track these threats and use their knowledge 
and expertise to develop insights into this activity. These insights 
feed into published threat intelligence and provide the indicators 
and technical content that allows us to create countermeasures that 
provide protection for Secureworks' customers. 
This report synthesizes and presents our findings for the period July 
2022 to June 2023.
5
2023 State of the Threat: A Year in Review
Ransomware continues to be the primary threat 
facing organizations, because of the scope of 
disruption it can cause and its prevalence. Attack 
numbers returned to and then exceeded historical 
norms, after last year's brief slowdown following the 
invasion of Ukraine. Average dwell times between 
initial access and ransomware payload delivery have 
dropped significantly to a median figure of just 
24 hours. 2023 may be the most prolific year for 
ransomware attacks to date.
1.  Drive-by downloads are becoming increasingly 
popular as a malware delivery method and over 
the past year have surged in use as an initial 
access vector for ransomware. Two major strains 
of malware delivered this way are Gootloader and 
SocGholish, often via compromised websites.
2.  Supply chain attacks on and through suppliers 
provide threat actors with maximum impact for 
effort expended. Threat actors as diverse as North 
Korean state-sponsored groups and ransomware 
operators have conducted notable supply chain 
attacks over the past year, leveraging initial victims 
to gain access to their customers.
3.  Infostealer activity has also increased, associated in 
large part with use by ransomware affiliates. Stolen 
credentials now vie with scan-and-exploit as some of 
the most significant precursors of ransomware attacks. 
On a single day on one underground marketplace, as 
many as seven million infostealer logs were available 
for sale, well over twice as many as on the same 
day last year. The case for organizations to monitor 
underground forums for stolen data is clear.
6
2023 State of the Threat: A Year in Review
Microsoft's disabling by default of macros 
in documents from the internet has forced 
threat actors to innovate in how they deliver 
malware. Use of malicious Microsoft OneNote 
files and container file types such as ISO grew to 
compensate during the year.
4.  Artificial intelligence (AI) is a supporting tool to 
existing threat actors, rather than a new class of threat. 
To date, phishing lures and Telegram bots remain the 
major tangible evidence of use of AI by threat actors. 
However, the level of interest that threat actors are 
showing suggests that they may soon develop more 
complex and dangerous applications.
5.  Regular and timely patching remains as essential 
as ever in preventing threat actors from 
compromising networks. Both state-sponsored 
threat groups and cybercriminals make wide use 
of scan-and-exploit to commence their attacks, 
making exploited vulnerabilities one of the most 
frequently observed initial access vectors.
6.  State-sponsored threat activity remains driven 
by political imperatives. Russia's primary focus is 
the war in Ukraine, North Korea's is currency theft, 
Iran's is suppression of opposition, and China's is 
cyberespionage. However, regional focuses are, in 
some cases, starting to shift, particularly on the part 
of China, which is closely monitoring the impact of 
the war on Ukraine on other European nations.
7
2023 State of the Threat: A Year in Review

# The Business of Cybercrime—Is Boomtime Back?
Over the past year, the number of victims named on ransomware 
leak sites returned to normal levels (after the brief dip in early 2022[^1]) 
and then continued to grow to reach unprecedented heights.  
The last four months have proved the most fertile in terms of victim 
numbers since name-and-shame emerged. 
![Ransomware name-and-shame leak site victim listings—2020 to 2023](Figure 1. Ransomware name-and-shame leak site victim listings—2020 to 2023. (Source: Secureworks))
8
2023 State of the Threat: A Year in Review
It is tempting to conclude that business is booming, although leak sites only list victims who have not 
paid the ransom, so an entirely accurate picture is not possible. However, we should not forget that 
spikes of anomalous activity on the part of a few highly impactful groups may to an extent be skewing 
the figures, as shown in figure 2.
![Victim count by scheme per month](Figure 2. Victim count by scheme per month. (Source: Secureworks))
9
2023 State of the Threat: A Year in Review
Name-and-Shame Sites Reveal 
the Most Active Ransomware 
Groups 
At current rates of victim naming, 2023 is on course to be the most 
prolific year since name-and-shame attacks began in 2019. It is likely 
that the 10,000th victim name will be posted to leak sites by late 
summer 2023.*
However, one-off mass exploitations of specific vulnerabilities 
explain why March (Fortra GoAnywhere, exploited by Clop operator 
GOLD TAHOE[^2]), May (Zimbra mail server, exploited by MalasLocker) 
and June 2023 (MOVEit Transfer, exploited by GOLD TAHOE) saw 
the highest ever monthly number of victims named.
The same threat groups continued to dominate in 2023—GOLD 
MYSTIC's LockBit again remains the head of the pack but GOLD 
BLAZER's BlackCat/ALPHV, Clop, GOLD SOUVENIR's Royal, 
BianLian, PLAY and GOLD REBELLION's Black Basta all feature in the 
ten most active groups. 
LockBit operator GOLD MYSTIC and its broad and loosely managed 
pool of affiliates continue to deploy LockBit ransomware prolifically. 
Once again in 2022/23, it tops the ratings for most active group, this 
time with nearly three times the number of victims of the next most 
active group, ALPHV(BlackCat), operated by GOLD BLAZER.
![Name-and-shame victims listed per year July-June](Figure 3. Name-and-shame victims listed per year July-June. (Source: 
Secureworks))
* The 10,000th name-and-shame ransomware victim name 
was posted to the BlackCat/ALPHV leak site in mid-August.
10
2023 State of the Threat: A Year in Review
However, new schemes have also posted numerous victims: 
MalasLocker, 8BASE and Akira all emerged only in May 2023. 8BASE 
listed nearly 40 victims on its leak site during June 2023, only 
slightly fewer than LockBit. Analysis indicates it posted a dump 
of victims going as far back as mid-2022 all at the same time. 
MalasLocker attacks, targeting Zimbra servers from the end of 
March 2023[^3] and listed on their leak site in May, accounted for at 
least 171 victims. This provides just one illustration of how valuable 
scan-and-exploit (where threat actors use search engines to identify 
vulnerable systems) can be as a tactic for ransomware groups.
![The 20 most active name-and-shame ransomware groups by victims listed between July 2022 and June 2023](Figure 4. The 20 most active name-and-shame ransomware groups by victims listed between July 2022 and June 2023. (Source: Secureworks))
11
2023 State of the Threat: A Year in Review
Assessing the Size of the  
Ransomware Problem
Accurately assessing the scale of the ransomware problem is 
challenging. Leak sites only touch on a fraction of the problem and 
not all ransomware groups operate leak sites. New ransomware 
variants launch regularly. Without a leak site, it is very difficult to 
judge how active they are.
The primary purpose of leak sites is to encourage currently 
recalcitrant victims to pay. Therefore, they only show the names 
of victims who are yet to pay a ransom. As such, they cannot be 
considered an accurate record of any specific group's activity.  
Nor are they an indication of the overall impact of ransomware.
Historic data from ransomware group takedowns or collapses 
indicate that leak sites only reveal a small percentage of overall 
attacks. For example, Hive's leak site listed 150 organizations, likely 
accounting for around 10 percent of their overall victim count of 
1,500. Avaddon listed just 180 victims, a small fraction of the nearly 
3,000 decryption keys the group released when it shuttered the 
operation. It is difficult to assess how representative these  
examples are.
To extrapolate, we would need to know how successful each group's 
leak site is and what the likelihood of payment by a victim once they 
have been named is. It may not be outlandish to assume that the 
vast majority of “successful” ransomware operations occur without 
the victim's name ever reaching the leak site—that is where the 
incentive to pay lies, with the victim motivated to prevent public 
disclosure.
Leak sites generally do not reveal whether ransomware was deployed. 
And we can't draw conclusions about how effective or impactful 
a ransomware deployment was, and whether the victim did not 
pay because the impact was low, or because the data stolen was 
inconsequential.
Name-and-shame statistics are useful for some things. They show 
how particular variants emerge onto the scene and how they 
grow and shrink in usage. But how reliable are they as indicators of 
impact? Without knowing how many victims pay the ransom, we 
can't determine how successful any particularly variant is in terms of 
payment to victim ratio. Leak site data should therefore be used with 
caution. In aggregate though it is clear from the continued activity 
that ransomware and data-theft extortion remain a viable criminal 
business model and a substantial threat to businesses.
12
2023 State of the Threat: A Year in Review
Dwell Times Are Dropping for 
Ransomware Attacks
Despite the increasing threat posed by ransomware attacks, in 
many cases early detection and response thwarts attackers from 
progressing to ransomware deployment. Because of this, our incident 
responders frequently discover ransomware precursor activity 
without evidence of damaging system encryption events. 
However, there have been some interesting trends over the past 
year in those attacks where ransomware is deployed. Most notably, 
the dwell time—the time between gaining access to a network and 
executing the ransomware—has significantly reduced compared to 
previous years.
- In just over ten percent of cases, we saw ransomware 
deployed within five hours of initial access.
- Nearly two-thirds of attacks were carried out inside one 
single day, nearly four fifths within one week.
- In around a fifth of attacks, the threat actor sat on 
the network for longer than a week before deploying 
ransomware.
- Of those, three-quarters continued to sit on the network 
for over a month.
Notably, the median dwell time in ransomware engagements 
dropped to just under 24 hours from 4.5 days in the previous year 
and 5.5 days in the year before that. 
Importantly, the incident response engagements that provided 
the data used to make this calculation featured a broad range of 
18 different ransomware variants. This means that the data was 
not skewed by a prevalence of variants that are known typically to 
be deployed very quickly, such as Phobos ransomware. The dwell 
times in engagements where exfiltration of data was observed 
were generally longer, but this is not universally true; in some 
engagements involving Black Basta, Hive, and AvosLocker—all 
double extortion ransomware schemes—we observed data 
exfiltration and ransomware deployment taking place more quickly 
than the median dwell time of 24 hours.
Average (median) dwell 
time for ransomware actors
24 hours
13
2023 State of the Threat: A Year in Review
So why are threat actors executing their ransomware attacks 
so much more quickly? CTU researchers have observed that 
ransomware intrusions have become less complex. Threat actors 
are not conducting the same operations more quickly. Instead, they 
are conducting simpler operations. Devastating enterprise-wide 
encryption events, which are more difficult to execute and take 
longer to carry out, are now rarer than in previous years. 
One driver for this is likely the need to reduce dwell time to lower 
the chance of detection. The cybersecurity industry is undoubtedly 
getting better at detecting the activity that has historically preceded 
ransomware, such as the use of offensive security toolkits like Cobalt 
Strike. This may be a factor in forcing ransomware operators to work 
more quickly. 
However, it is also likely that the threat actors now deploying 
ransomware are just lower skilled than previous operators. The 
introduction of the RaaS model lowered the bar to entry, introducing 
playbooks for affiliates to use, and allowed it to scale significantly as 
a result. 
Arguably, this represents a commodification of the ransomware 
landscape, with scheme operators reducing the cost of operations 
in order to increase volume. This can be seen in the sheer number 
of victims named on name-and-shame leak sites. But it is also 
reflected in the “quality” of ransomware operations. This might 
provide one reason why fewer victims are reported[^4] to be paying 
ransoms (although such reports may not give a full picture, given 
the fracturing of the ransomware landscape and the increasing 
difficulties in reliably identifying cryptocurrency wallets). 
This absolutely does not imply that ransomware can now be ignored 
as a threat. Even a limited distribution on a victim's network can be 
highly damaging. Hitting a single server in a production environment, 
for example, might be enough to take business operations offline for 
enough time to cause significant financial impact. And ransomware 
operators and their affiliates are aware of this. The increased take-up 
of virtualized environments, now often crucial to many companies' 
IT infrastructures, makes them a viable target. More and more 
ransomware schemes now have Linux-compatible variants, created 
to target VMware ESXi hosts. Threat actors have an incentive to 
spend minimal time on a likely-monitored Windows system before 
moving to encrypt hundreds of virtual disks on a single VMware ESXi 
host.
Dwell times can vary considerably case by case. In July 2022, in an 
incident involving the financially motivated GOLD TOMAHAWK 
threat group (also known as Karakurt), Secureworks incident 
responders identified 29 hosts and 10 user accounts compromised 
by the threat actor. Over 300GB of compressed data was exfiltrated 
from two of these hosts. The attacker had remained on the network 
for as long as six weeks before incident responders were engaged, 
navigating across multiple hosts in different countries possibly to 
locate data to steal. The unusually long dwell time included a three-
week hiatus from malicious activity.
In contrast, in April 2023, Secureworks incident responders 
investigated an incident where an organization that did not use 
Secureworks managed services experienced an intrusion where, 
within a single 24-hour period, two different ransomware variants, 
Buhti and AvosLocker, were deployed. 
14
2023 State of the Threat: A Year in Review
The Top Initial Access Vectors  
for Ransomware
Scan-and-exploit and stolen credentials were the two largest initial 
access vectors used by threat actors in the ransomware attacks 
Secureworks investigated, each accounting for approximately 32 
percent of intrusions. These figures are consistent with the top 
IAVs for all incident response engagements over the same period 
but represent a change relative to ransomware engagements in the 
previous twelve months. This is the period covered in last year's State 
of the Threat report, when scan-and-exploit at 52 percent accounted 
for many more ransomware intrusions than the next nearest IAV, 
stolen credentials, at 39 percent. 
Secureworks incident responders also investigated several intrusions 
where threat actors used the Qakbot malware to deliver Cobalt 
Strike, which then led to Black Basta ransomware deployment. These 
incidents were notable due to the speed of the operations: again, 
data exfiltration and ransomware deployment occurred within 24 
hours of initial access.
Ransomware Initial Access 
Vectors
The three largest initial access vectors (IAVs) observed 
during ransomware engagements where customers 
engaged Secureworks incident responders were:
- Scan-and-exploit—32 percent
- Stolen credentials—32 percent
- Commodity malware delivered via 
phishing emails—14 percent
Each of these IAVs can either be prevented or detected 
at an early stage before ransomware is deployed, using 
a combination of prompt and regular patching, multi-
factor authentication, and comprehensive implementing 
of monitoring solutions.
15
2023 State of the Threat: A Year in Review
The most likely enabler of the rise in the use of stolen credentials 
as an IAV is the explosion in infostealer activity. Infostealers are 
a type of malware that can pilfer sensitive information such as 
login credentials, session cookies and tokens, financial details, and 
personal data from compromised computers and networks. Once 
installed via methods such as phishing attacks, infected websites, 
and malicious software downloads, they can execute and exit very 
quickly, sometimes in less than a minute of total runtime. The data 
is then packaged and sold as “logs.” Each log contains data taken by 
the infostealer from a compromised user machine.
Threat actors use these stolen credentials to gain unauthorized 
access to enterprise networks via remote access services such as 
virtual private networks (VPNs) and Microsoft Office Web Access 
(OWA). This unauthorized access can form an early stage in the 
exfiltration of sensitive data or the deployment of ransomware. As 
a result, infostealers are a significant type of intrusion precursor 
malware and a contributory factor to attacks that often happens 
outside protective corporate controls.
![What's in a log?](Figure 5. What's in a log? (Source: Secureworks))
16
2023 State of the Threat: A Year in Review
![Threat actor Telegram channel listing logs prices and deals](Figure 6. Threat actor Telegram channel listing logs prices and deals.  
(Source: Secureworks))
Opening the Valves on the 
Infostealer Data to Threat  
Actor Pipeline
Initial access using stolen credentials accounted for up to 32 percent 
of the ransomware incident response engagements we handled in 
the last year. Credentials can be obtained via a variety of means, 
including phishing emails that lead victims to credential harvesting 
websites, or through previous breaches. 
However, in the past year, there has been a significant increase in 
the use of infostealers to obtain credentials. A thriving market clearly 
exists, and new infostealers are regularly developed and put up for 
sale to meet this demand. 
Russian Market remains by far the most prolific marketplace[^5] for 
infostealer logs. On a single day in June 2022, there were 2.9 million 
logs advertised for sale. A year later, that figure has ballooned to 
over 7 million, over 2.4 times as many, and a notable increase on the 
five million that were available on a single day in late February 2023. 
Other markets include 2easy and Genesis Market, and there is also a 
significant level of trade via certain Telegram channels.
17
2023 State of the Threat: A Year in Review
Buyers on these marketplaces are likely discerning, seeking out 
logs containing credentials to particularly high-value organizations 
before making a purchase. However, CTU researchers have observed 
that the bulk of logs available for purchase contain credentials for 
systems like social media platforms and common webmail services. 
These are not likely to be of great value to ransomware operators 
specifically looking to extort organizations. This means that the 
majority of available stock likely consists of a large number of older 
logs deemed of limited value to users. 
However, sometimes there are rich pickings to be had. In October 
2022, we observed a vendor on an underground forum auctioning 
access to a home PC belonging to an employee of a global brand in 
the food and drink industry. According to the seller, virtual network 
computing (VNC) credentials and cookies harvested from the 
employee's personal computer facilitated access to a corporate 
dashboard and the user's Outlook inbox. This could allow a threat 
actor to conduct reconnaissance, pivot deeper into the network, 
conduct phishing attacks, or deploy ransomware. 
![Underground forum post advertising access to corporate resources via a personal computer](Figure 7. Underground forum post advertising access to corporate resources via a personal computer. (Source: Secureworks))
18
2023 State of the Threat: A Year in Review
Home devices have provided fertile ground for infostealers over 
the past year. Based on posts observed by CTU researchers, most 
devices infected with an infostealer were running Windows 7 Home 
or Windows 10 Home operating systems. Typically, home computers 
also have weaker security controls than corporate-managed 
devices. CTU researchers expect to see an increase in the volume of 
corporate credentials stolen from compromised personal devices for 
abuse as an initial access vector for ransomware and other malicious 
activity. Limiting how employees access company resources from 
personally owned devices can greatly reduce the enterprise's risk 
from infostealers.
Over the past year, Russian Market also added a pre-order function 
to its website, enabling buyers to request logs by domain or type. It is 
not clear whether this functionality has been widely taken up, but the 
development implies that buyers can effectively pay sellers to target 
specific organizations or services.
The development of new infostealer malware advertised for sale 
on underground forums also occurs at speed. In 30 days through 
May and June 2023, we saw 12 new infostealers made available for 
purchase or rent on underground forums. Once advertised, they are 
tested and reviewed by forum users. Their developers rely on positive 
feedback for success and not all will become widely used.
Although the use of these tools to harvest credentials is clearly 
widespread, firm evidence connecting specific stealers to specific 
compromises is scant. This is likely to be down to two key factors: 
one, if credentials are used in a compromise, their origin is rarely 
made clear and two, the time delay between them being collected 
by an infostealer and used in an intrusion is likely to be significant, 
and certainly well beyond the scope of most incident response 
engagements. 
Credentials go for a premium on underground forums and 
marketplaces because it is highly likely they are used to facilitate 
cybercrime-related intrusions, including ransomware. The time lapse 
between theft and use further shows the value for organizations of 
monitoring forums for stolen data.
![Extract from an advertisement for the Meduza Stealer](Figure 8. Extract from an advertisement for the Meduza Stealer.  
(Source: Secureworks))
Scan-and-Exploit—Why  
Patching Pays 
Scan-and-exploit, where threat actors use search engines like 
Shodan to identify vulnerable systems, can lead to spikes in attack 
activity by specific groups, and even anomalistic peaks in name-
and-shame ransomware activity. MalasLocker ransomware listed 
171 victims on their leaksite by exploiting Zimbra servers vulnerable 
to CVE-2022-27924, a cross-site scripting (XSS) flaw impacting 
Zimbra Collaboration Suite 8.8.15. Clop operator GOLD TAHOE 
specializes in acquiring and exploiting specific vulnerabilities in file 
transfer solutions (see the section later in the report) to impact 
maximum numbers of victims.
Initial access broker GOLD MELODY has also favored scanning 
internet-facing servers to identify and exploit vulnerabilities 
to opportunistically compromise networks. In August 2022, 
Secureworks incident responders worked on an engagement  
where the group likely exploited a Log4j vulnerability (CVE-2021-
4104) to compromise an organization's internet-facing Flexera 
FlexNet server. 
Chinese ransomware group[^6] BRONZE STARLIGHT also uses scan-
and-exploit attacks to target unpatched internet-facing servers. 
For example, in August 2022, CTU researchers observed BRONZE 
STARLIGHT compromising an organization's vulnerable internet-
facing ManageEngine server. Other state-sponsored groups depend 
on scan-and-exploit too, for example China's BRONZE ATLAS and 
Iran's COBALT MIRAGE. 
The easy availability of information about vulnerable servers can 
even see multiple threat actors compromising a network using the 
same vulnerability, at the same time or in quick succession.
The annual listing of top routinely exploited vulnerabilities published 
by CISA and partner agencies lists top vulnerabilities that threat 
actors scan for. Frequently, this list contains older vulnerabilities. 
Of the top 12 vulnerabilities exploited during 2022 listed in the 
roundup[^7] for the year, seven have CVE dates of earlier than 2022. 
One, CVE-2018-13379, a path traversal vulnerability in Fortinet 
FortiOS and FortiProxy, also made the top 15 routinely exploited list 
in 2021 and in 2020.
While organizations should always prioritize their patching schedule 
according to their individual risk profile, the vulnerabilities listed in 
these reports likely remain at high risk of exploitation.
19
2023 State of the Threat: A Year in Review
20
2023 State of the Threat: A Year in Review
Data Leak-Only Attacks—What's 
the Impact?
Despite initial questions about whether threat actors would find 
data leak-only extortion a lucrative endeavor, threat groups that 
specialize in this type of attack continue their activities. Karakurt, 
thought to be a spin-off of the now defunct Conti ransomware 
operation, persists in regularly naming victims on its leak site at an 
average of seven a month. And arguably the biggest ransomware 
event of the last year—the exploitation of a zero-day vulnerability 
in the MOVEit Transfer file management software—did not involve 
actual ransomware at all. GOLD TAHOE continue a long-term trend 
of targeting such utilities to steal data and hold it to ransom, naming 
many hundreds of alleged victims on its Clop leak site.
21
2023 State of the Threat: A Year in Review
![Services exploited by GOLD TAHOE in attacks on file transfer solutions](Figure 9. Services exploited by GOLD TAHOE in attacks on file transfer solutions. (Source: Secureworks))
GOLD TAHOE Has Two Strings  
to Its Bow 
The GOLD TAHOE threat group, operator of Clop ransomware 
and the Clop Leaks site, has been around for over a decade. Its 
members have worked with GOLD DRAKE (EvilCorp, Dridex), GOLD 
BLACKBURN (TrickBot), GOLD NIAGARA (FIN7), and other well-
known threat groups. Perhaps because of these connections, GOLD 
TAHOE does not openly communicate on any criminal forums. And 
while the group does not operate its ransomware as a RaaS, it does 
appear to rely on another group, GOLD NIAGARA, to deliver its 
ransomware in a private arrangement.
But the Clop ransomware itself tells only half of the story. While the 
leak site the group has operated since August 2020 lists victims 
of its ransomware operations, it also carries the names of those 
targeted in its attempts at data theft-only extortion. There are 
many more names of the latter type than there are of the former; 
Clop ransomware deployments account for around a quarter of 
listed victims, while the data theft-only operation features the 
remainder. And the bulk of those are from two campaigns from 
2023. By exploiting zero-day vulnerabilities in two file management 
services—Fortra's GoAnywhere MFT in March and Progress 
Software's MOVEit Transfer application in May—the group claims 
to have successfully stolen data from over three hundred victims 
and possibly as many as six hundred. It is not possible to gauge 
exactly how many were affected given that the victims named on 
leak sites constitute those who have not paid the ransom.
Such activity for a ransomware group is unusual, but it forms the 
most recent chapter in its exploitation of vulnerabilities to steal 
and ransom victim data. Since late 2020, the group has sought to 
exploit both zero-day and N-day vulnerabilities in file management 
applications to extort the users of such services. Their use of zero-
day vulnerabilities is notable, and shows how well-resourced the 
group is—zero-days are expensive to develop or procure, and were 
historically the domain of state-sponsored actors.
22
2023 State of the Threat: A Year in Review
Exploiting these services gives the group access to shared files, 
some of which may come from third parties, as for example in 
the Zellis payroll compromise[^8] which formed part of the MOVEit 
Transfer attacks. And while there is little an organization can do to 
prevent a breach of a trusted third-party, especially through the 
abuse of a zero-day vulnerability in the vendor's platform, there are 
some steps organizations can take to detect and mitigate the threat 
posed by GOLD TAHOE.
- Enforce a retention policy on shared files to ensure data 
is available for only as long as it is needed. 
- Protect highly sensitive data (like PII) with file level 
encryption that requires a key that is not stored on the 
file sharing service. If a platform does not support such 
a facility, it may not be the best method of sharing this 
type of data. 
- Encrypt data in transit and at rest.
- Enable alerting that indicates when files are being 
accessed and monitor for anomalies.
- Implement auditing so that if a breach occurs it can 
be quickly determined what files were present during 
relevant time period(s).
- For on-premises solutions, implement network flow 
monitoring to detect and alert on large data transfers.
23
2023 State of the Threat: A Year in Review
The Conti Implosion—The Hydra 
is Dead but Its Limbs Survive
The most obvious impact of the conflict in Ukraine on the 
cybercrime ecosystem was the implosion in the first half of 2022 of 
GOLD ULRICK, the group behind Conti ransomware. The revelations 
in the Conti Leaks—a large disclosure of information about the 
group's activity, likely by a Ukrainian affiliate angered at the group's 
almost immediate declaration of support for Russia's invasion—
preceded the disappearance of Conti ransomware by a few months. 
While the full reasons for its dissolution remain unclear, it is likely 
that affiliates were concerned about damage to the Conti name that 
might make it harder for victims to pay. GOLD ULRICK may also have 
been disconcerted by the U.S. Department of State announcing[^9] 
in May 2022 a $10 million reward for information leading to the 
identification or location of key leaders behind the Conti ransomware 
operation. Such unwanted scrutiny may have also been a cause for 
the group's disappearance.
However,