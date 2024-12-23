# A YEAR IN REVIEW
8TH EDITION, OCTOBER 2024

## Table of Contents
- [Letter From Our Vice President, Threat Research](#letter-from-our-vice-president-threat-research)
- [Executive Summary and Key Findings](#executive-summary-and-key-findings)
- [Chapter 1: Despite Law Enforcement Gains, Cybercrime Continues to Flourish](#chapter-1-despite-law-enforcement-gains-cybercrime-continues-to-flourish)
- [Chapter 2: Notable Trends in Tactics, Techniques, and Procedures](#chapter-2-notable-trends-in-tactics-techniques-and-procedures)
- [Chapter 3: Hacktivism Flourishes](#chapter-3-hacktivism-flourishes)
- [Chapter 4: State-Sponsored Threat Activity](#chapter-4-state-sponsored-threat-activity)
- [Chapter 5: Conclusion](#chapter-5-conclusion)
- [Appendix](#appendix)

2
State of the Threat: A Year in Review | 8th Edition
TABLE OF 
CONTENTS
Letter From Our Vice President, Threat Research
Executive Summary and Key Findings
Chapter 1: Despite Law Enforcement Gains, Cybercrime Continues to Flourish 
Chapter 2: Notable Trends in Tactics, Techniques, and Procedures 
Chapter 3: Hacktivism Flourishes
Chapter 4: State-Sponsored Threat Activity
Chapter 5: Conclusion
Appendix
03
04
06
36
46
54
89
90

3
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix
The human and business impact of cybercrime in the last year  
has been stark. 
In June 2024, urgent and lifesaving operations were cancelled in 
the UK when National Health Service provider Synnovis fell victim 
to a ransomware attack. In April, AT&T revealed that 109 million U.S. 
customer account details, including calls and texts, had been illegally 
accessed by cybercriminals. Clorox laid bare the business cost of a 
cyberattack in its Q1 FY24 earnings when it attributed a 20% decline 
worth $356 million in net sales to a ransomware attack.
In the face of a criminal ecosystem seemingly running rampant, law 
enforcement fought back. Operations to disrupt QakBot, ALPHV, 
LockBit, and many more sent shockwaves through the cybercriminal 
landscape, upending hierarchies and sparking new affiliations. 
Disruption counts. It shows cybercriminals that they cannot hide 
under the veil of anonymity. They can be reached.
But cybercriminal ecosystems are akin to living organisms. They adapt 
and mutate in the face of disruption, reacting with speed to maintain 
the tempo of their attacks. The names and affiliations may be 
different, but the impact is the same, with attacks causing maximum 
business disruption, downtime, and remediation costs.
State actors have augmented strategic priorities with tactical 
campaigns related to ongoing and heightened geopolitical tensions. In 
parallel, Western governments have shown that their tolerance for cyber 
espionage is low with notable moves by the U.S., UK, and allies against 
both Russia and China. 2024 is the year of elections and the world’s 
democratic governments are on high alert for disinformation and other 
attempts to influence or call into question the election process.
New regulations that promote greater transparency and knowledge 
sharing are key to our collective defense—so is the ongoing effort 
by law enforcement to shine a light into the darkest recesses of 
the cybercriminal underground. The collective actions of the cyber 
defense community to spread understanding of the state of the 
threat continue to make an essential difference. This annual State of 
the Threat report plays a key role in maintaining that understanding 
and awareness, adding further depth and context to the threat 
intelligence publications that Secureworks produces throughout  
the year.
Cordially,
A LETTER FROM OUR VICE 
PRESIDENT, THREAT RESEARCH
Don Smith
Vice President, Threat Research
Secureworks®

4
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix
Cyber risk levels remain high for all organizations. A flourishing cybercriminal ecosystem 
continues to present numerous threats, and geopolitical issues are bringing additional 
pressures. This annual report explains why, using the collected findings of the Secureworks® 
Counter Threat Unit™ (CTU)™ research team for the period July 2023 to the end of June 2024.
Cybercrime is still the number one threat facing Secureworks customers. Most cybercrime 
is opportunistic, seeking out easy victims with cash or assets worth stealing. Ransomware 
continues to be the most pressing cybercrime concern. Despite law enforcement agencies 
getting some significant wins in the past year, the ransomware ecosystem keeps bouncing 
back, showing it can roll with the punches, adjust, and persist. Many individual threat actors 
have adapted, shedding loyalties in favor of financial gain. Some have switched group 
affiliation, while others work with multiple groups.
Geopolitical events are again driving state-sponsored and hacktivist cyber activity. Conflicts 
in Ukraine, the Middle East and the South China Sea are directing the agendas of big 
players like China, Russia, and Iran and encouraging grassroots activism. Some hacktivists 
are deliberately blurring their origins, raising suspicions of tasking or involvement by state-
sponsored threat actors. The result is very different threat levels in different geographies. 
Chapter 1 of this report explores this year’s ups and downs of ransomware, the takedowns and 
the new actors, as well as key enablers of the ecosystem such as infostealers and botnets. 
It also covers Business Email Compromise (BEC)—another ever-present threat. Chapter 
2 examines some of the tactics we see cybercriminal and state-sponsored groups using, 
including exploiting internet-facing vulnerabilities, Living off the Land, and the emergence of AI. 
Chapters 3 and 4 discuss the hacktivism and state-sponsored cyber landscapes respectively.
EXECUTIVE SUMMARY 
AND KEY FINDINGS

5
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix
Hacktivists continue to conduct denial of 
service or web site defacement campaigns 
against organizations linked to conflict zones.
The basics of cybersecurity defense remain as 
essential as ever—phishing-resistant MFA, timely 
patching, and comprehensive XDR implementation 
with threat-led detections. One or more of these 
defenses were absent in over 50% of the incidents 
worked by Secureworks incident responders last year.
In contrast to hacktivist activity, stealth remains an 
essential element in state-sponsored attacks. Threat 
actors favor the use of obfuscation networks, living-
off-the-land (LOTL) techniques, and commodity 
tooling in many attacks, making detection and 
attribution difficult. These techniques and tools are 
also increasingly used by ransomware groups.
Unpatched vulnerabilities remain the top Initial Access 
Vector (IAV) in ransomware attacks, accounting for 
nearly 50% of known IAVs. Vulnerable perimeter 
devices in particular draw the attention of both state-
sponsored and cybercriminal threat actors.
Adversary in The Middle phishing kits have emerged 
as a key weapon in the adversaries’ arsenal to bypass 
established multi-factor authentication (MFA) 
defenses, making choosing phishing-proof MFA 
solutions essential. 
Ransomware dwell times—the period of time from 
initial compromise to ransomware deployment—
remain low. The shortest ransomware dwell time 
observed by Secureworks incident responders was 
just under seven hours. 
The overall number of attacks is still high. 
Ransomware remains a major threat to all types of 
organization. March 2024 saw the highest number 
of name-and-shame ransomware schemes listing 
victims on leak sites.
For network defenders,  
our key findings this year are:

6
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix
Ransomware—A Year in Review
In some respects, the past year has seemed like business as normal 
for the ransomware ecosystem. Victim listings on ransomware 
leak sites have remained high. With 730 victims listed, March 2024 
represents the busiest month on record, although this figure was 
inflated by Dispossessor listing 330 victims on their site, most of 
which had previously been listed by other ransomware groups.
C H A P T E R  1
DESPITE LAW 
ENFORCEMENT GAINS, 
CYBERCRIME CONTINUES 
TO FLOURISH
![Figure 1. Totals by month for ransomware leak site listings. (Source: Secureworks)]

7
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix
On the other hand, recent law enforcement activity seems to have 
had a fragmenting effect on the ransomware ecosystem. High-
profile law enforcement operations have led, indirectly or otherwise, 
to the apparent demise of one of the two most active ransomware 
operators. GOLD BLAZER[^1] pulled an exit scam by failing to pay one 
of its affiliate $22 million USD owed in commission when it shut 
down its ALPHV/BlackCat operation, shortly after a law enforcement 
takedown that initially seemed of limited impact. Affiliates are threat 
actors who conduct ransomware attacks on behalf of operators in 
return for a share of the ransom.
GOLD MYSTIC[^2] persists, despite appearing to have taken the LockBit 
operation offline (at least for a short while) after a multi-stage law 
enforcement operation. This revealed the identity of ‘LockBitSupp’, 
the LockBit admin, and appeared designed to frighten off affiliates. 
The operation undoubtedly had an impact on LockBit, and monthly 
victim numbers dropped, but the group has not yet disappeared. The 
differing ways in which ransomware groups have responded to law 
enforcement pressure will be discussed later in this chapter.
![Figure 2. Name and shame group leak site lists July 23 – June 24. (Source: Secureworks)] 
Tracking Changes in Tactics, 
Techniques, and Procedures 
(TTPs)
Direct observation from Secureworks ransomware incident response 
engagements suggests that dwell times overall remain low, although 
they varied greatly over the year. More than half the incidents 
observed involved a dwell time of under 28 hours and the median 
dwell time was just over two and a half days. However, the median 
figure only tells part of the story. 
There were clusters with shorter dwell times, and clusters with much, 
much longer ones. A third of intrusions saw ransomware deployed 
in less than a day. In fact, the shortest dwell time observed was just 
under seven hours. In another third, operators took longer than a day 
but less than a week to deploy their ransomware. The remaining third 
took longer than ten days. In one case, ransomware was deployed 
over 135 days after initial access was obtained. This variance may 
reflect a more chaotic affiliate landscape; as ransomware schemes 
expand and take on more affiliates, it is likely that newer affiliates will 
be less adept at intrusions and will take longer to deploy ransomware. 
 
A Quiet Year for Some
GOLD TAHOE[^3] had a quiet year after extorting 
thousands of organizations in last year’s ultra high-
profile data-theft-only attacks exploiting zero-days 
in managed file transfer (MFT) services such as Fortra 
GoAnywhere and MOVEit Transfer.
Although the group allegedly exploited a zero-day 
vulnerability in SysAid IT support software in late 2023, 
there was no significant corresponding increase in 
victim naming on the leak site. Targeting a tool like 
SysAid represents a departure from GOLD TAHOE’s 
usual zero-day exploitation activity, as any data 
exfiltration would require lateral movement from the 
point of entry. It is possible that such access was used 
instead in the deployment of ransomware rather than 
during data theft-only intrusions, given the group’s 
background operating cadence over the year of listing 
approximately five victims a month.
State of the Threat: A Year in Review | 8th Edition
8
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix

9
State of the Threat: A Year in Review | 8th Edition
For researchers, tracking individual ransomware threat actors is 
challenging because many ransomware schemes offer playbooks 
to affiliates. We saw this with release of material related to the 
Conti operation in August 2021. Affiliates share tools, sometimes 
even down to the exact same binaries with the same hashes. Many 
ransomware groups also do not rely on custom malware for access, 
instead using living-off-the-land binaries (LOLBins) or off the shelf 
tools to conduct operations. For example, remote management tools 
like ScreenConnect, AnyDesk, Atera and Splashtop have become 
increasingly popular. Tying the use of the tools to a specific individual 
or even group can be difficult.
Ransomware attackers continue to look for the easiest means 
of initial access—the top IAVs used were either scan and exploit 
of vulnerable devices or stolen credentials (where multi-factor 
authentication (MFA) was absent.)
Ransomware groups have been quick to exploit high profile 
vulnerabilities. In October 2023, shortly after the Citrix Bleed 
vulnerability (CVE-2023-4966) was revealed and exploit code 
was published, CTU™ researchers observed multiple exploitation 
attempts that were likely the precursor to LockBit ransomware 
deployment. 
In one compromise that Secureworks incident responders 
investigated, exploitation of CVE-2023-4966 led to data theft and 
the naming of the victim on the LockBit leak site. In this case, no 
attempt was made to deploy ransomware. This is the first time CTU 
researchers have observed a LockBit affiliate attempt extortion 
without deploying ransomware, but there is nothing surprising 
about this. Ransomware groups are opportunistic and look for ways 
to monetize access. The need for decryption keys to get business 
operations back online might be the biggest incentive for victims to 
pay, but data theft-only attacks can still result in ransom payment. 
The nature of that particular compromise suggested that it was 
conducted by a LockBit affiliate with limited technical aptitude. The 
Citrix Bleed vulnerability is easy to exploit with publicly available 
exploit code, the legitimate tools used for post-compromise activity 
in the incident are straightforward to use, and the batch script to 
propagate the ransom note was not complex.
Over the same period, initial access brokers also took advantage of 
new vulnerabilities to gain access. These are the threat actors who 
gain initial access to networks and then auction or otherwise sell the 
access to other threat actors. In one incident, exploitation activity 
on a Citrix NetScaler gateway server began in August 2023. This was 
shortly after the critical remote code execution vulnerability CVE-
2023-3519 was disclosed, a patch was released, and exploit code was 
made publicly available. The threat actor exploited the vulnerability 
to drop a web shell on a Citrix NetScaler device for persistence. 
This web shell is a variant of TinyShell, which is based on China 
Chopper. It includes basic functionality that allowed the execution of 
commands on the device. After deploying TinyShell, the attacker ran 
another basic web shell to harvest Citrix credentials and write them 
to a file. The file contents indicated that credentials were obtained 
in mid-September, suggesting that the web shell was first executed 
around that time.
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix

10
Then, in late November, an unknown affiliate of the Black Basta 
ransomware-as-a-service (RaaS) scheme operated by the GOLD 
REBELLION[^4] threat group entered the victim’s network via the 
access gained through the organization's compromised NetScaler 
gateway server. In the following weeks, the attacker conducted 
post-compromise activity from this initial host. This activity 
included running obfuscated PowerShell commands, conducting 
Active Directory reconnaissance via the legitimate Windows Active 
Directory Explorer tool, and accessing multiple ZIP and temporary 
files. The threat actor also downloaded and executed a malicious 
variant of the NetSupport Manager remote management tool. The 
same activity was observed during a separate compromise, including 
the use of exactly the same TinyShell web shell with the same file 
hash and same embedded password. The delay between initial 
access and subsequent exploitation attempts suggested the same 
initial access broker (IAB) may have been responsible for access in 
each intrusion.
Nor was it just new vulnerabilities that IABs exploited for access. 
CTU researchers observed GOLD MELODY[^5] continue to use tried-
and-tested methods to gain access to networks. In October 2023, a 
threat actor exploited a Java deserialization vulnerability (CVE-2022-
21445) to compromise and execute commands on an organization's 
internet-facing Oracle WebLogic server. CTU researchers attributed 
the activity to the group because of GOLD MELODY’s previous 
targeting of Oracle WebLogic servers, and use of the same attacker-
controlled infrastructure and execution of the Wget command to 
download a Perl script named bc.pl. 
In a separate intrusion, CTU researchers assessed that the 
compromise of an internet-facing Oracle WebLogic server for 
access, and the use of the AUDITUNNEL tunnelling tool and a 
JSP web shell, were also consistent with GOLD MELODY activity. 
Subsequent efforts to compress and exfiltrate data appeared to have 
been carried out by a different attacker, reinforcing the  
notion that GOLD MELODY operates as an IAB, selling on access  
to other attackers.
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix

11
State of the Threat: A Year in Review | 8th Edition
All Change in the  
Ransomware Ecosystem?
With LockBit and ALPHV no longer dominant, affiliates have been 
forced to look for alternative operators to work with. Beneficiaries 
of this trend appear to include Qilin, BlackSuit, Play, and others. As a 
result, there has been a more even spread of victims against a larger 
number of ransomware schemes. In the three months before the 
May 2024 part of the LockBit takedown, there were 45 name-and-
shame ransomware groups active. In the three months following, 
there were 55 groups active. May also saw the highest ever number 
of name-and-shame ransomware schemes listing victims on 
dedicated leak sites.
![Figure 3. Number of ransomware schemes listing victims on leak sites  
per month. (Source: Secureworks)]
Month (2024)
January
February
March
April
May
June
32
36
35
39
40
39
No. of Schemes
Why Leak Site Numbers  
Give a Partial View
Victims named on leak sites will almost invariably 
represent failed extortion attempts, so the numbers 
cannot be taken as representing an accurate overall 
picture of ransomware activity. There is a lot that leak 
sites don’t tell us.
For example, if more victims refuse to pay, we might 
expect to see an increase in victim numbers on leak 
sites. However, this would not indicate that ransomware 
was becoming more prolific. We would not have sight of 
all the data needed to make that judgement. 
Nor do leak site numbers reflect attacks by ransomware 
groups that do not engage in naming and shaming 
victims on a dedicated leak site. For example, Phobos 
ransomware is quite prolific, but its operators do not 
steal data or name their victims.
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix

12
State of the Threat: A Year in Review | 8th Edition
There was also a significant uplift in new groups entering the 
ecosystem and attempting to profit from the uncertainty after the 
ALPHV/LockBit disruptions.
One scheme, called Dispossessor (since disrupted[^6] by law 
enforcement), created a leak site with strong design similarities to 
LockBit’s site and posted details of multiple victims in March 2024.  
However, most victims had already been listed as victims on sites 
belonging to other groups, predominantly LockBit but also CL0P, 
8BASE and Egregor. It is likely that the group behind the site has 
used data stolen and published by other groups to re-extort victims. 
Attempts were made to establish another leak site called Rabbit  
Hole in March 2024. Rabbit Hole was designed to allow smaller 
groups operating without their own leak site to publish victim  
names to an independent site. Despite its promotion on underground 
forums, it appears that Rabbit Hole did not gain traction and was 
quickly shuttered.
![Figure 4. Number of new ransomware schemes vs. total number of schemes. (Source: Secureworks)]
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix

13
State of the Threat: A Year in Review | 8th Edition
Reorganize, Regroup, Rebrand
There was a lot of affiliate movement in the ransomware ecosystem 
over this reporting period. Affiliates continue to engage with 
multiple schemes at the same time or use schemes to relist victims 
when a service collapses. For example, when NoEscape and then 
ALPHV/BlackCat perpetrated exit scams, leaving their affiliates 
high and dry, LockBit offered to list victims in return for a share of 
ransom payments. Following the first stage of the law enforcement 
disruption activity against LockBit, the group did list at least six 
victims on the leak site that had briefly appeared on the ALPHV site 
prior to its takedown.  
CTU researchers observed a number of ransomware attacks where 
the victims were listed on more than one leak site. For example, 
in late 2023, Secureworks incident responders attended an 
engagement that involved the deployment of the ALPHV/BlackCat 
ransomware before the victim was named on the INC ransom leak 
site. The timing of the data theft in this engagement aligned with 
law enforcement action that rendered GOLD BLAZER's Tor-based 
infrastructure unreachable. It is therefore likely in this case that the 
affiliate was unable to list the victim’s name on the ALPHV/BlackCat 
site so sought an alternative, settling on INC Ransom instead.
Qilin Benefits from  
New Affiliates
One group that may have benefited from law 
enforcement takedowns to attract new affiliates 
is GOLD FEATHER’s[^7] Qilin (also known as Agenda) 
ransomware operation. GOLD FEATHER is likely Russian, 
as the threat actors advertise Qilin on Russian-language 
forums and apply a special vetting procedure to English-
speaking affiliates before agreeing to work with them.
The number of victims named on the Qilin leak site 
increased over the first half of 2024. The group first 
listed victims in October 2022 but before early 2024 
had never exceeded nine victim listings per month. 
From February 2024 onwards it consistently listed ten or 
more, reaching a peak of 19 in May.
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix

14
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix
![Figure 5. Growth in Qilin listings mapped against ransomware landscape developments. (Source: Secureworks)]
Qilin’s expanded operations have facilitated high-profile attacks. A 
June 3 ransomware attack[^8] on Synnovis, which supplies pathology 
services to the UK National Health Service (NHS), impacted services 
such as blood testing at several London hospitals and resulted 
in the NHS issuing[^9] an urgent call for blood donors, highlighting 
the potential life threatening impact cyberattacks can have on 
healthcare.
Qilin uses ransomware written in Rust that could target both 
Windows and VMware ESXi devices. CTU researchers have observed 
the group using Remote Desktop Protocol (RDP) in one attack, 
as well as tools including PCHunter (PCHunter64.exe) tool and 
PowerTool (PowerTool64.exe), both of which can disable antivirus 
services. The attacker also used SessionGopher (SessionGopher.
ps1), a PowerShell tool that can remotely extract private key 
information and passwords from saved sessions of PuTTY, WinSCP, 
SuperPuTTY, FileZilla, and RDP. However, because Qilin uses 
affiliates to conduct attacks, these TTPs may not be a reliable 
indicator of TTPs in future attacks. Indeed, the more affiliates a 
group attracts, the more diverse the tooling used can become. 
Some groups operate playbooks for affiliates, leading to more 
consistent TTPs being used but it is not known whether that is true 
for Qilin.

15
State of the Threat: A Year in Review | 8th Edition
![Figure 6. How Darkside became ALPHV/BlackCat. (Source: Secureworks).]
Ransomware affiliates are financially motivated and may operate 
in their own best interest rather than remaining loyal to a particular 
threat group or ransomware family. For example, CTU researchers 
observed a warning on Donut Leaks' leak site about an affiliate who 
had allegedly stolen data from them and posted it on other leak sites 
with modified contact information to collect the ransom. The post 
specifically mentions INC ransomware, although the connection 
is unclear. Some affiliates have reportedly deployed up to seven 
different ransomware families. The dynamic relationship between 
affiliates and operators could be another explanation for the cross 
posting of the stolen data on other leak sites. However, the principal 
reason for a rebrand is to avoid the effect of law enforcement 
activity, most notably sanctions, which can impact ransom 
payments.
The threshold for rebranding isn’t always that high, though. Groups 
may rebrand just to avoid law enforcement interest. We saw this 
with GOLD WATERFALL’s[^10] Darkside ransomware attack on Colonial 
Pipeline. It had such a devastating impact on critical infrastructure 
in the U.S. that the group immediately found themselves in the 
crosshairs of the Federal Bureau of Investigation (FBI) and other 
agencies. So, they shuttered the Darkside operation and rebranded 
as BlackMatter. BlackMatter then rebranded to ALPHV/BlackCat, 
possibly because a BlackMatter decryption key was made available 
by Emsisoft[^11]. It is possible that this historical link with Darkside was 
part of the reason for the FBI’s takedown attempt against ALPHV/
BlackCat in December 2023. We have not yet (as of July 2024) 
seen ALPHV/BlackCat re-emerge under a new scheme since GOLD 
BLAZER perpetrated its alleged exit scam[^12], by apparently failing to 
pay an affiliate known as Notchy[^13] a commission of $22 million for an 
attack. Notchy then attempted to re-extort the victim of that attack 
via another ransomware group, RansomHub.
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix
Given the group’s history of rebranding, they will probably attempt 
to do so again at some point. However, they might find this 
challenging because of the damage their exit scam has likely done 
to their reputation among potential future partners.
Over the course of the reporting period, we have seen several 
scheme rebrands: GOLD VICTOR’s[^14] Vice Society rebranded to 
Rhysida and GOLD SOUVENIR’s[^15] Royal Ransomware rebranded to 
Black Suit. CTU researcher analysis in the latter case confirms that 
the ransomware binary has code in common with Royal ransomware, 
but the Black Suit ransom note is new. In these two cases, the 
specific motivations for rebranding are unclear.
Overall, rebranding is a good method of throwing researchers and 
law enforcement off the scent. It is not foolproof, but it can cause 
enough confusion to delay investigations and make them more 
challenging, particularly if findings need to be developed to an 
evidential standard. Also, on occasion, affiliates who break away 
from groups take ransomware source code with them to effectively 
rebrand. For example, we believe that the REvil ransomware 
operators (GOLD SOUTHFIELD[^16]) were former affiliates of the 
Gandcrab ransomware operation.
Is Lockbit Finally Locked Down?
GOLD MYSTIC continued to name LockBit ransomware 
victims at a fairly steady rate after the first law 
enforcement infrastructure takedown and then after the 
indictment of Dimitry Yuryevich Khoroshev as LockBitSupp, 
the LockBit scheme administrator. However, in June 2024, 
just 12 victims were named on the LockBit leak site, which 
represents by far its lowest monthly total since the launch 
of LockBit 2.0 in July 2021. The leak site also appears to 
be struggling to stay up, with significant downtime as of 
publication. One of the victims named in June was the U.S. 
Federal Reserve, alongside claims that 33TB of U.S. citizens’ 
data had been stolen. However, it became apparent 
that this claim was bogus, and any data was related to a 
different organization. 
It is hard to see how LockBit can continue to operate 
under that name now that financial sanctions[^17] are in 
place against Khoroshev. These sanctions effectively 
make it illegal for UK or U.S. organizations to pay ransoms 
following a LockBit ransomware attack, which rules out 
a significant source of potential victims. Affiliates are 
unlikely to continue working with LockBit if they know their 
chances of securing payment are significantly reduced. The 
significant drop-off in activity might well be an indication 
that the operation is about to be shuttered.

16
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix

17
State of the Threat: A Year in Review | 8th Edition
# Letter From Our VP
# Executive Summary 
and Key Findings
# Chapter 1: Despite Law  
Enforcement Gains, Cybercrime 
Continues to Flourish
# Chapter 2: Notable Trends  
in Tactics, Techniques,  
and Procedures
# Chapter 3: Hacktivism Flourishes
# Chapter 4: State-Sponsored  
Threat Activity
# Chapter 5: Conclusion
# Appendix
When TTPs Evolve,  
Process Tightening Can Help
Secureworks incident responders attended two engagements in 
quick succession in early 2024 that involved the social engineering 
tactics normally associated with