Table of Contents

Executive Summary ..................................................................................................... 3

Extortion Is on the Rise ................................................................................................. 5

Why Having Backups Is No Longer Enough ......................................................................... 7

Common Extortion Tactics ............................................................................................ 9

Who Is Being Attacked? ............................................................................................... 14

Insights From Dark Web Leak Sites ................................................................................. 15

Industries Most Heavily Impacted .................................................................................. 18

Regions Most Heavily Impacted ..................................................................................... 21

What Are Extortion Threat Groups After? ........................................................................ 22

What You Can Expect From an Attack: An Example Ransomware Incident ................................ 25

When APTs Use Ransomware ....................................................................................... 29

Conclusion: What to Expect From Extortion Groups in 2023 ................................................. 32

Reach Out to Experts.................................................................................................. 38

Methodology ............................................................................................................39

Unit 42 Incident Response Methodology ..........................................................................40

About Palo Alto Networks and Unit 42 ........................................................................ 41

Ransomware and Extortion Report 2023 \| 2

Executive Summary

Threat actors are increasingly employing 

Organizations, in turn, need to evolve defenses 

extortion techniques to gain leverage over 

to address the various methods threat actors use 

targeted organizations and accomplish their 

to apply pressure. Incident response plans today 

goals. While much attention has been paid to 

need to involve not only technical considerations 

ransomware in recent years, modern threat actors 

but also safeguards for an organization’s 

increasingly use additional extortion techniques 

reputation and considerations for how to protect 

to coerce targets into paying—or dispense with 

employees or customers who may become 

ransomware altogether and practice extortion on 

targets for some of extortionists’ more 

its own. 

aggressive tactics. 

While in many cases the motivation is financial, 

In our review of incident response cases, as well 

Unit 42 also sees indications that extortion can 

as our threat intelligence analysts’ assessment of 

happen in service of a group’s larger goals—

the larger threat landscape, we noted some 

sometimes simply to fund other activities, but 

key points: 

other times to distract from them. 

Multi\-extortion tactics continue to rise.

Harassment is another extortion tactic we 

In Unit 42 ransomware cases, as of late 2022, 

see being used in more ransomware cases. 

threat actors engaged in data theft in about 70% 

Ransomware threat actor groups will target 

of cases on average. Compare this to mid\-2021, 

specific individuals in the organization, often 

and we saw data theft in only about 40% of cases 

in the C\-suite, with threats and unwanted 

on average. Threat actors often threaten to leak 

communications. By late 2022, harassment was 

stolen data on dark web leak sites, which are 

a factor in about 20% of ransomware cases. 

increasingly a key component of their efforts to 

Compare this to mid\-2021, when harassment was 

extort organizations. 

a factor in less than 1% of Unit 42 

ransomware cases.

Victims pay to 

regain access

Attackers threaten to 

DDoS attacks shut 

Customers, business 

release stolen data

down public websites

partners, and 

media contacted

Encryption

Data Theft

DDoS

Harassment

Ransomware and Extortion Report 2023 \| 3

MExtortion gangs are opportunistic, but there are 

out\-of\-date software that isn’t regularly or 

some patterns in the organizations they attack. 

easily updated or patched—not to mention 

Based on our analysis of dark web leak sites, 

the industry’s low tolerance for downtime. 

manufacturing was one of the most targeted 

industries in 2022, with 447 compromised 

Organizations based in the United States were 

organizations publicly exposed on leak sites. 

most severely affected, according to leak site 

Unit 42 believes this is due to the prevalence 

data, accounting for 42% of the observed 

of systems used by this industry running on 

leaks in 2022\.

Large, multinational organizations can 

organizations on the Forbes Global 2000 list 

be lucrative targets for threat actors.

were publicly impacted by extortion attempts. 

Attacks on the world’s largest organizations 

Since 2019, at least 96 of these organizations 

represent a small but notable percentage 

have had confidential files publicly exposed to 

of public extortion incidents. In 2022, 30 

some degree as part of attempted extortion.

Advanced threat groups may use extortion 

Other threat groups, including some from Iran or 

and ransomware to fund other activities — 

China, seem to have a different objective when 

or hide them. Threat groups from countries 

using ransomware. Threat actors can gain more 

under economic embargoes or sanctions have 

than money from deploying ransomware —it also 

been observed using ransomware and extortion 

has potential for both destruction and espionage.

to fund their operations. 

Predictions for what to expect from extortion 

• A rise in extortion related to 

in the coming year. Unit 42 experts have put 

insider threats. 

together predictions for what we expect to 

see from extortion groups in the coming year. 

Our predictions include:

• 2023 will be the year we see a large 

cloud ransomware compromise. 

• A rise in politically motivated 

extortion attempts. 

• The use of ransomware and extortion 

to distract from attacks aimed to infect 

the supply chain or source code.

Ransomware and Extortion Report 2023 \| 4

ELAPExtortion Is on the Rise

The number one goal for many criminal threat 

• Distributed Denial of Service (DDoS): 

actors is getting paid, and they’ll do whatever 

Websites or other resources are targeted via a 

they can to improve the chances of that 

DDoS attack to disrupt operations and to get 

happening. As such, we are seeing threat actors 

an organization’s attention.

increasingly focus on extortion techniques—often 

layering them on top of each other. 

• Harassment: 

Ransomware actors, for example, often use a 

variety of extortion techniques (called multi\-

extortion) to pressure organizations into making 

the difficult decision to pay ransom. 

Unit 42 has observed the following extortion 

tactics employed and threatened by ransomware 

threat actors:

• Encryption: 

Threat actors may call, email, or 

otherwise contact an organization’s 

employees or customers. They may also 

post on social media about the incident or 

contact journalists. 

In a selected set of Unit 42 incidents 

involving ransomware, we have seen significant 

increases in threat actors’ use of data theft 

and harassment.

An organization’s data and files are encrypted, 

Threat actors also simply use extortion. 

and the threat actor demands payment in 

About 10% of the extortion incidents Unit 42 

order to restore access to them. This has 

responded to in the period covered did not 

long been the primary extortion tactic of 

involve encryption.

ransomware.

• Data Theft: 

Threat actors acquire an organization’s data 

and threaten to disseminate it unless they are 

paid. This often involves dark web leak sites. 

Threat actors increasingly target information 

that may be particularly sensitive, such as files 

containing personally identifiable information 

(PII), customer financial data, protected health 

information (PHI), etc.

Ransomware and Extortion Report 2023 \| 5

Threat actor’s 
use of additional 
extortion tactics

Ransomware and Extortion Report 2023 \| 6

Why Having Backups 
Is No Longer Enough

With ransomware incidents grabbing attention 

Often, the threat of disclosure of sensitive data 

of late—both in the news and within security 

is what coerces organizations to pay the ransom. 

teams—many organizations have absorbed the 

Such leaks can cause reputational damage, loss 

basic concepts of how to defend against them. 

of confidence from consumers and partners, and 

Ransomware actors typically encrypt files to 

potential fines and sanctions from regulators and 

render them unusable and then demand ransom 

authorities—none of which can be prevented 

in exchange for a decryptor to recover encrypted 

by backups. 

data. The traditional advice for getting ahead of 

this type of attack is therefore to keep up\-to\-date 

We’ve also seen incidents in which organizations 

backups, stored offline, and test them often, 

decided not to pay ransom because they had 

so that your data is never fully at the mercy of a 

strong backups, but the threat actors followed up 

threat actor. 

with harassment campaigns so intense that the 

resulting costs exceeded the ransom demanded.

This is still a vital safeguard. Unfortunately, many 

of today’s threat actors have introduced such 

effective extortion techniques that they can 

coerce the victim to pay even if they’ve already 

backed up and protected their data and can 

minimize operational disruption from 

such attacks. 

Ransomware and Extortion Report 2023 \| 7

N
O

I

T
A
D
N
E
M
M
O
C
E
R

UNIT 42 EXECUTIVE 

RECOMMENDATION:

Prepare a Playbook 
for Multi\-Extortion

During an active extortion incident, rapid 

support from your incident response partner 

and outside legal counsel is critical. From a 

mitigation perspective, having a comprehensive 

incident response plan with corresponding crisis 

communication protocols will greatly reduce 

uncertainty. It’s important to know which 

stakeholders should be involved and the process 

to make decisions promptly (e.g., whether or not 

to pay, or who is authorized to approve payments).

The crisis communication plan should also 

cover what to do (or avoid doing) in the event 

that employees or clients are being harassed. 

Ransomware harassment awareness training 

should be delivered to an organization’s staff to 

equip them with tools and processes to follow 

during an active harassment incident.

Organizations should conduct a post\-mortem 

compromise assessment to validate that any 

remnant backdoors or other indicators of 

compromise (IoCs) (e.g. scheduled tasks or jobs) 

have been removed. This ensures that the threat 

actor cannot easily conduct a follow\-up attack 

after an initial breach.

Read Mitigating Cyber Risks with MITRE 

ATT\&CK for an in\-depth set of recommendations 

by Unit 42 incident responders. 

Ransomware and Extortion Report 2023 \| 8

Common Extortion Tactics

Encryption

Encryption is a tactic commonly favored by 

warns against attempting to circumvent 

ransomware threat actors. Criminal groups often 

the attack.

tout the facility and speed of their encryption 

software as a means to recruit “affiliates.” The 

However, threat actors are moving away from 

typical approach, following an initial breach, is to 

relying on encryption alone to extort payment. 

deploy malware that encrypts files and delivers a 

The majority of Unit 42’s ransomware incidents 

ransom note. This note promises the delivery of 

involving negotiation also included at least one 

a decryptor upon payment, provides instructions 

additional extortion tactic.

for how to contact the threat actor—and often 

\>\> What happened?

Important files on your network was ENCRYPTED and now they have “\[REDACTED]” extension.
In order to recover your files you need to follow instructions below.

\>\> Sensitive Data

Sensitive data on your network was DOWNLOADED.
If you DON’T WANT your sensitive data to be PUBLISHED you have to act quickly.

Data includes:
\- Employees personal data, CVs, DL, SSN.
\- Complete network map including credentials for local and remote services.
\- Private financial information including:citizens data, courts data, bills, 
budgets, annual reports, bank statements, etc
Samples are available on your personal web page linked below.

\>\> CAUTION

DO NOT MODIFY ENCRYPTED FILES YOURSELF.
DO NOT USE THIRD PARTY SOFTWARE TO RESTORE YOUR DATA.
YOU MAY DAMAGE YOUR FILES, IT WILL RESULT IN PERMANENT DATA LOSS.

\>\> What should I do next?

1\) Download and install Tor Browser from: https://torproject.org/
2\) Navigate to: \[REDACTED]

Figure 2\. An example of a BlackCat ransom note dropped on a compromised system

Ransomware and Extortion Report 2023 \| 9

Data Theft and Multi\-Extortion

Ransomware groups have threatened to leak data 

many threat actors target regulated data sets or 

stolen from victims in about 53% of ransomware 

highly commercially sensitive information for 

incidents involving negotiation between mid\-2021 

maximum leverage.

and late 2022\. Due to the efficacy of this tactic, 

There are many journalists asking questions about us and our attacks.
If you are a journalist and want to ask some questions you should write:

1\. Who are you?
2\. Where are you from?
3\. Where will you publish our answers?

We are trying to answer everyone in 24 hours.

\#Frequently Asked Questions:
Why did you choose GTA as branding?
\-Some old articles about us used GTA logo, so we decided to use it too.

How long have you beenn in operation?
\-From January 2021\.

Are you recruiting partners or are you closed?
\-We have been closed from the beginning and we don’t have affiliates.

How did you decide to team up and start a dedicated ransomware group? How was ViceSociety born?
\-Group of friends that were interested in pentest. We decided to try.

What do you do if the law says that someone can’t pay you? Does that matter? What happens if the customer doesn’t respond?
\-We don’t care about laws. If someone doesn’t pay or doesn’t contact us, we will publish their documents.

Has Vice Society published all the data it took from “company name” or does Vice Society have additional data that still has not been published?
\-We always publish everything.

Can you explain your decision to publish “company name” data?
\-They didn’t pay.

We DON’T answer questions like:
What country or region of the world are you from?
How old are you?
What vulns/eve do you use?

©2021 Copyright Vice Society. All rights reserved. Emails: V.society.official@onionmail.org. Vice Society@onionmail.org

Figure 3\. A page “for journalists” from Vice Society’s leak site

Ransomware and Extortion Report 2023 \| 10

Often known as multi\-extortion, this tactic 

effective at coercing payment than data theft 

typically involves publicly posting information 

and harassment. 

about breached organizations to a website 

maintained by the threat actors on the dark web. 

Harassment

These dark web leak sites sometimes threaten 

to sell data to third parties after the deadline 

for paying a ransom has passed. In other cases, 

threat actors simply threaten to post the 

data publicly. 

The leak sites often include some version of a 

blog, or what appears to be a customer service 

portal, providing ways for affected organizations 

to view the status of their ransom demand and 

communicate with the threat actors. Some leak 

sites even have a section aimed at journalists 

seeking information about the ransomware group, 

a clear attempt by the cybercriminals to boost 

their notoriety in the cyber landscape.

During an 18\-month span between May 2021 

through October 2022, data theft leveraged as 

an extortion tactic grew by 30 percentage points. 

Unit 42 expects this upward trend of data theft 

and multi\-extortion to continue.

Distributed Denial of Service (DDoS)

Unit 42 has observed threat actors leveraging 

harassment as an extortion tactic in at least 9% 

of our ransomware incidents involving negotiation 

overall. As with DDoS, threat actors generally 

employ this extortion tactic when trying to get 

an organization’s attention. However, unlike with 

DDoS, threat actors seem to be turning to this 

extortion tactic more often.

Threat actors call and leave voicemails 

for corporate executive leaders and other 

employees, send emails to personnel, or 

disclose victims’ identities on a leak site or 

social media. The purpose of these activities is 

to make it uncomfortable for an organization to 

avoid responding to the threat actors and their 

demands. Not only is the organization faced 

with responding to a ransomware incident, but 

now they also have a personnel public relations 

situation to deal with.

During an 18\-month span between May 2021 

through October 2022, harassment as an 

extortion tactic grew from an average of \<1% 

While DDoS remains an extortion tactic, Unit 

of Unit 42’s monthly ransomware cases to a 

42 has only observed this in less than 2% of 

monthly average of approximately 20%. While 

ransomware cases. In these cases, threat 

the available data and case information reflect an 

actors have used DDoS to get an organization’s 

upward trend, the information available is limited 

attention if the victim chose to ignore them rather 

and contains significant outliers. As such, while 

than communicate about payment of a ransom. 

we believe this extortion tactic will continue to be 

While we continue to observe the tactic in use 

used by threat actors, it is difficult to predict how 

occasionally, we believe that it has not grown in 

frequently it will occur in the future. Unit 42 will 

popularity among threat actors because it is less 

be closely monitoring this trend.

Ransomware and Extortion Report 2023 \| 11

 
Extortion Without Encryption

About 10% of Unit 42’s incident response 

We’ve also investigated several incidents 

matters involving extortion do not involve 

related to the Luna Moth/Silent Ransom Group. 

encryption. Often, these extortion attempts 

These threat actors are known for an extortion 

rely on data theft. 

campaign targeting businesses in multiple 

sectors, including legal and retail. Rather than 

However, in a small number of cases, threat 

encryption, the campaign relies on social 

actors have deleted organizations’ data 

engineering to convince targets to provide 

altogether. This is particularly prevalent in 

remote access to systems. They then use that 

matters involving databases that were vulnerable 

access to exfiltrate data and follow up with 

and directly exposed to the internet. There 

extortion attempts. 

are several automated threats that delete the 

database contents, claim to have exfiltrated 

them, and leave behind an extortion message in a 

new database table for the victims to find.

Using data theft as an extortion tactic without 

encryption was most frequently seen in Unit 42 

cases involving the Karakurt ransomware group. 

Ransomware and Extortion Report 2023 \| 12

N
O

I

T
A
D
N
E
M
M
O
C
E
R

UNIT 42 EXECUTIVE 

RECOMMENDATION:

Ensure Complete Visibility via 
Extended Detection and Response 
(XDR) Technology

When it comes to protecting your organization 

from threats, you must be able to see them. One 

of the greatest ways to protect your organization 

is to increase visibility of activity in your 

environments. Cortex XDR technology allows 

defenders to see activity on endpoints in near real 

time and respond to attacks quickly. 

By empowering your defenders to isolate 

computers as malicious activity is detected, 

you can help reduce the likelihood of attackers 

spreading to other endpoints. This in turn reduces 

the impact of ransomware encryption. To 

increase protection, mature organizations move 

toward automating this isolation via Security 

Orchestration, Automation, and Response 

(Cortex XSOAR) technology. This can be 

important as attackers may operate when your 

team is not working.

Read Mitigating Cyber Risks with MITRE 

ATT\&CK for an in\-depth set of recommendations 

by Unit 42 incident resonders. 

Ransomware and Extortion Report 2023 \| 13

Who Is Being Attacked?

Threat actors interested in extortion are 

Cybercriminals out to make a name for 

frequently opportunistic, targeting whichever 

themselves may also seek to leak data from well\-

organizations they believe will pay. Because some 

known organizations. 

criminals provide services to other threat actors, 

it can be difficult to discern the behavior of 

In some cases, threat actors display political 

particular gangs. In part because of this, extortion 

motivations or regional preferences. For example, 

can affect organizations large and small across 

some samples of ransomware have been 

various industries and regions. 

observed to check systems for Cyrillic characters, 

typical of Eastern European languages, and avoid 

However, many groups focus on profitable 

encrypting files when they are found. 

organizations—a practice sometimes known 

as “big\-game hunting.” Large, multinational 

At times, extortionists do seem to favor 

organizations often have the means to pay larger 

targets in particular industries. For example, 

sums of money and have the motivation to pay to 

Vice Society has a reputation for targeting 

avoid disruption of business operations. Although 

educational institutions. 

these organizations may be better prepared to 

withstand cyberattacks on a daily basis, they can 

Combining our observations from incident 

still be vulnerable to extortion. 

response cases and our ongoing monitoring of 

For example, less\-protected subsidiaries, satellite 

view of who criminal groups are attacking.

activity on dark web leak sites, we can provide a 

offices, or remote workers could be impacted by 

ransomware in an attempt to move laterally to 

access an organization’s crown jewels. We have 

observed ransomware groups focusing efforts on 

regional offices—a practice that could impact the 

larger organization. 

Ransomware and Extortion Report 2023 \| 14

Insights From Dark Web Leak Sites

Every day, our threat researchers see information 

It’s also worth mentioning that when we track 

about seven new victims posted to dark web 

organizations whose information was posted 

leak sites—averaging out to about one publicly 

on a leak site, we are typically looking at those 

posted new extortion target every four hours. In 

who chose not to pay the criminal group’s 

2022, names and proof of compromise for 2,679 

original demand. Therefore, the actual global 

victims were posted on leak sites, about 4% 

impact of gangs who maintain leak sites is higher 

higher than the number observed in 2021\. 

than what we can observe there—presumably, 

In 2022, the extortion group LockBit 

posted information about 801 breached 

organizations on their leak site, the highest 

victim count we have observed in the last 

two years from any one group. LockBit 

posted 409 victims in 2021, meaning that 

in 2022, we saw a 95% increase in victim 

count compared to last year’s entries. 

By comparison, Conti posted 511 victims 

in 2021\.

Attacks on the world’s largest organizations 

represent a small but notable percentage of 

these incidents. In 2022, 30 organizations on the 

Forbes Global 2000 list were publicly impacted 

by extortion attempts from groups including 

LockBit, Conti, BlackCat, Hive, and Black Basta. 

Since 2019, at least 96 of these organizations 

have had confidential files publicly exposed to 

some degree as part of attempted extortion. 

some organizations choose to pay to keep their 

information off the dark web. 

A few frequent practitioners of the multi\-

extortion strategy, such as Conti and REvil, 

dissolved in 2022\. However, we expect other 

criminals to continue making heavy use of 

this approach to extortion. As noted above, 

cybercriminals threatened to leak stolen data 

in about 70% of ransomware cases involving 

negotiation in late 2022\. The cybersecurity 

industry has also observed signs that individuals 

from the Conti and REvil groups continue to have 

an influence on the cybercriminal community, as 

former members of those gangs start new illicit 

endeavors and bring many of their tactics 

with them.

While they represent a body of evidence of the 

damage extortionists do to organizations, leak 

sites also provide visibility into these groups’ 

resources, capabilities, and typical approaches. 

Unit 42 keeps tabs on them as part of our ongoing 

monitoring of the global threat landscape.

Ransomware and Extortion Report 2023 \| 15

Data Extortionist Groups and the 
Global 2000

Karakurt, named the “Extortion Branch of Conti,” 

Other groups try to make a name for themselves 

was responsible for various notorious incidents 

by attacking the world’s most recognizable 

in 2022\. For example, they attacked one of the 

organizations. For example, Lapsus$, a 

largest Chinese investment holding companies, 

cybercrime group that emerged in mid\-2021, was 

allegedly stealing 320 GB of corporate data.

responsible for compromising organizations such 

as NVIDIA, Samsung, Microsoft, and LG. 

This group gains access to corporate networks 

either through their own expertise or by paying 

To accomplish this, Lapsus$ mostly used 

initial access brokers (who sell access to 

social engineering (including phishing and SIM 

breached networks). Karakurt forgoes encryption 

swapping) for initial access. This group also tried 

in favor of other methods of extortion, such 

to entice disgruntled employees to provide them 

as contacting victims’ employees, business 

with inside information in exchange for payment. 

partners, and clients with harassing emails and 

Even well\-defended organizations can struggle to 

phone calls to pressure the victims to cooperate. 

prevent attacks targeted at insiders in 

They often exacerbate the situation by using the 

this manner. 

organization’s own data against them. 

While the group extorted some victims, they 

sometimes appeared more interested in the 

notoriety of compromising high\-profile targets. 

Ransomware and Extortion Report 2023 \| 16

N
O

I

T
A
D
N
E
M
M
O
C
E
R

UNIT 42 EXECUTIVE 

RECOMMENDATION:

Implement a Threat 
Intelligence Program

Organizations can learn about the tactics, 

techniques, and procedures (TTPs) that 

threat actors use to successfully compromise 

their industry peers and conduct attacks. 

Organizations must have a chartered, funded, and 

staffed threat intelligence program in place. 

The program will provide the blue team (their 

defenders) with net new, specific indicators 

sourced from the threat intelligence team. These 

can be used to monitor for the latest TTPs, 

enabling rapid detection and mitigation of a full\-

scale ransomware attack. 

Unit 42 consultants can help with designing 

a modern, threat\-informed security program 

or enhance the effectiveness of your existing 

program based on lessons learned from our 

incident response investigations. 

Read Mitigating Cyber Risks with MITRE 

ATT\&CK for an in\-depth set of recommendations 

by Unit 42 incident responders. 

Ransomware and Extortion Report 2023 \| 17

Industries Most Heavily Impacted

Based on both Unit 42’s data and dark web leak 

This gives the threat actors a rapidly expanding 

site data, the manufacturing industry was one 

attack surface through which they can deploy 

of the most impacted by extortion attacks in 

their attacks. The bigger the scale, the bigger 

2022, with 447 victims listed on various sites. 

the payout.

Following this sector was the professional and 

legal services industry, with 343 victims.

Criminals often seek targets in industries where 

it’s critical for business operations to be able to 

Industries in which organizations often run 

provide certain products or services in a timely 

on systems with out\-of\-date software can be 

manner. The groups aim to take advantage of the 

more heavily impacted. When it’s difficult for 

pressure these organizations are under to meet 

organizations to regularly update or patch, threat 

deadlines and produce deliverables, hoping this 

actors gain an opportunity to take advantage of 

will lead them to pay quickly and in full. Lost 

old vulnerabilities to initiate their exploits.

revenue streams from operational downtime 

can also push organizations to concede to threat 

actors’ demands.

Figure 4\. Industries most heavily impacted by extortion attacks (leak site data, 2022\)

Ransomware and Extortion Report 2023 \| 18

N
O

I

T
A
D
N
E
M
M
O
C
E
R

UNIT 42 EXECUTIVE 

RECOMMENDATION:

Proactively Manage and Reduce 
Your Attack Surface Inventory

A staggering number (at least 75%) of 

ransomware attacks and breaches fielded by 

Unit 42’s Incident Response team result from 

a common culprit: attack surface exposures. 

Organizations must continuously monitor the 

health, inventory, and accuracy of their external 

attack surface. 

When using our Active Attack Surface 

Management (ASM) solution Cortex Xpanse 

with our clients in their environments, Xpanse 

continuously monitors all internet\-connected 

assets and discovers unknown exposures. 

Once we receive the contextualized results 

from Xpanse, we can prioritize findings to align 

the security concerns with the organization’s 

critical assets.

To illustrate, the analysis report from Xpanse 

shows all systems running Remote Desktop 

Protocol (RDP) that are directly accessible from 

the internet. Clients can then decide if Xpanse 

should automatically fix these exposures or not. 

RDP is the most common capabilities used by 

threat actors for initial access. Furthermore, 

RDP is the most impactful tool for lateral 

movement once attackers have a foothold 

inside targeted networks.

Ransomware and Extortion Report 2023 \| 19

We also commonly see cybercriminals taking 

advantage of expired certificates, deprecated 

server operating system versions, and end\-of\-life 

email platforms, all items that are automatically 

discovered by Xpanse. All of these things were 

directly exposed to the internet, giving threat 

actors a path of least resistance.

It is strongly advised that you perform an 

Attack Surface Assessment if your organization 

does not have an accurate inventory of your 

external attack surface, including your cloud 

assets, or does not actively monitor changes 

to your external asset estate.

Read Mitigating Cyber Risks with MITRE 

ATT\&CK for an in\-depth set of recommendations 

by Unit 42 incident responders. 

Ransomware and Extortion Report 2023 \| 20

Regions Most Heavily Impacted

Leak site data indicates the 

 Americas region 

Germany and the U.K., accounting for 

was hit the hardest by extortion attempts in 

nearly 5% each. 

2022, followed by 

 Europe, the Middle East, 

and Africa (EMEA), and the 

 Asia Pacific 

Threat actors, due to their financial goals, 

region (JAPAC).

often focus on profitable organizations based 

When looking at organizations posted on leak 

concentration of attacks in the U.S., criminal 

sites by country, the United States is still the 

gangs have a global presence and have been 

most severely impacted, accounting for 42% of 

observed impacting organizations in 107 

the observed leaks in 2022\. This is followed by 

countries in 2022\.

in the United States. However, despite the 

Figure 5\. Top countries impacted by extortion attempts (leak site data, 2022\)

Ransomware and Extortion Report 2023 \| 21

What Are Extortion 
Threat Groups After?

While the obvious answer is “money,” it can be 

We often see evidence of threat actors searching 

helpful to take a look at what in your organization 

systems for personal information such as 

translates to financial gainfrom the perspective of 

identification numbers, passwords, and other 

a cybercriminal.

credentials. They may seek documents such as 

passports and tax forms.

First and foremost, threat actors want you to 

feel pressured. The more you feel this way, the 

Threat actors know that many organizations 

more likely you will pay what they demand. When 

are legally (and ethically) obligated to protect 

cybercriminals use tactics such as harassment and 

information of this type. Multinational 

urgency in addition to encryption, they’re trying to 

organizations are bound by cyber regulation and 

make you feel out of control and under pressure 

data protection laws from various parts of the 

so you’ll do what they want.

world—and failing to meet these requirements 

can result in fines, sanctions, the loss of 

Another way threat actors seek to amp up the 

operating licenses, and even the imprisonment of 

pressure is to search your systems for information 

individuals. Threat actors can take advantage of 

about any insurance policies or financial assets. 

these types of consequences to exert leverage on 

Our incident responders have encountered threat 

their targets. 

actors who quote from these internal sources 

during negotiations and use this information to 

Information that can be used in identity theft can 

form an opinion about how high a ransom an 

often be sold to other criminals. And when threat 

organization can pay.

actors search for passwords, they may be looking 

to sell initial access to a compromised network to 

Today’s threat actors, however, are also looking 

other criminals—or they may be looking for ways 

for ways to multiply their payday. This means 

to further the compromise and get deeper into an 

they’re not only looking for ways to halt the 

organization’s systems. 

targeted organization’s business operations—but 

they’re also in pursuit of information that could be 

These activities underscore the need to protect 

valuable to third parties.

your systems beyond having backups. It’s vital to 

be aware of what information is most sensitive 

This creates a win\-win situation for the threat 

and valuable to your organization and to be 

actor. If the targeted organization chooses to pay 

conscious of how that information is stored and 

what is demanded, the threat actor makes a profit. 

who can access it. A Zero Trust approach can help 

If the organization chooses not to pay, the threat 

minimize the damage a threat actor can do after 

actor is still in possession of exfiltrated data they 

an initial compromise.

can sell. In some cases, cybercriminals may even 

try to double dip and make money both ways.

Ransomware and Extortion Report 2023 \| 22

N
O

I

T
A
D
N
E
M
M
O
C
E
R

UNIT 42 EXECUTIVE 

RECOMMENDATION:

Implement Enterprise\-Wide 
Zero Trust Architecture

Organizations that have the capabilities to rapidly 

contain the extent of their attack surface will 

reduce the impact that threat actors will have 

if they successfully circumvent other controls. 

Having an effective Zero Trust architecture 

mitigates the risk of a threat actor conducting 

lateral movement, which is a key indicator in 

advance of many types of attacks.

A huge part of winning the battle against 

cyberattacks is successfully making an attacker’s 

job harder. Implementing Zero Trust Network 

Architecture (or ZTNA) is not an overnight 

journey, but is one of the more effective 

frameworks—specifically ZTNA 2\.0, which is a 

refined version of ZTNA. This framework helps 

create the layers of security that slow down and 

prevent an attacker from successfully moving 

laterally around the network.

Ransomware and Extortion Report 2023 \| 23

This framework helps force an attacker to make 

more noise to move around or through controls, 

while also slowing them down. Both of these 

things can provide more time for detection and 

response, giving you a better chance to properly 

contain and remediate the threat. 

Taking it one step further, you can implement a 

Secure Access Service Edge (SASE) framework 

with Prisma SASE. Prisma SASE builds on 

the principals of ZTNA, but adds guidance on 

additional layers of control across web traffic and 

cloud platforms, in addition to other principles.

Read Mitigating Cyber Risks with MITRE 

ATT\&CK for an in\-depth set of recommendations 

by Unit 42 incident responders. 

Ransomware and Extortion Report 2023 \| 24

What You Can Expect From 
an Attack: An Example 
Ransomware Incident

Attacks aren’t a single malicious action. 

Breaching your network is only one step of a fairly 

complex process. The good news is that every 

Financial Impact of Ransomware

time threat actors take an action in your network 

In 2022 Unit 42 observed:

to further their criminal goals, it presents an 

opportunity for you to detect their presence or 

prevent them from having an impact. 

Below, we tell the story of an example 

• Ransom demands as low as 

$3,000 and as high as $50 million. 

• Ransom payments as low as 

$3,000 and as high as $7 million.

ransomware incident, which has been mapped 

• The median demand was $650,000, 

to MITRE ATT\&CK tactics and techniques. This 

while the median ransom payment was 

provides a sample of how extortion groups may 

conduct themselves for maximum profit. When 

planning your organization’s defense, it may be a 

useful exercise to assess how you might respond 

to a threat actor using these TTPs.

$350,000, a 46% decrease from the 

original median ransom demand.

Ransomware and Extortion Report 2023 \| 25

N
O

I

T
A
D
N
E
M
M
O
C
E
R

UNIT 42 EXECUTIVE 

RECOMMENDATION:

Pressure Test Your 
IR Plans and Program

Organizations that continuously review, update, 

and test their incident response plans are much 

more likely to effectively respond and contain 

an active attack. Organizations that conduct 

tabletop exercises, purple teaming tests, 

breach simulations (automated and manual), 

and partner with Unit 42 consultants strengthen 

their velocity and preparedness when responding 

to an active attack. 

These exercises build the internal and external 

communication cadence, establish stakeholder 

relationships and foster environmental 

knowledge sharing in advance of an attack. 

This significantly increases the likelihood of 

early support and containment. Furthermore, 

these exercises will likely find opportunities or 

gaps that result in improved incident response 

posture once the gaps are mitigated.

Read Mitigating Cyber Risks with MITRE 

ATT\&CK for an in\-depth set of recommendations 

by Unit 42 incident responders.

Ransomware and Extortion Report 2023 \| 26

From First Campaign to Final Impact: 
A MITRE ATT\&CK Flowchart

Note: Certain actions in the narrative below are associated with multiple tactics 

and techniques, but only one has been listed for each row for the sake of brevity.

Ransomware and Extortion Report 2023 \| 27

Ransomware and Extortion Report 2023 \| 28

Too Big—Nothing To See Here!

Unit 42 continues to see threat actors 

artificially increase the size of malicious 

scripts and utilities to evade automated 

scanning tools, which often have 

file size limitations for performance 

reasons (T1027\.001: Obfuscated Files or 

Information: Binary Padding). By adding 

“junk data” to malicious utilities, these 

malicious files may evade detection by 

some antivirus and other security software 

solutions, depending on their configuration.

When APTs 
Use Ransomware

Security leaders at large organizations with 

While it makes sense to be concerned about 

mature security programs sometimes assign a 

determined and highly skilled threat groups—

lower risk level to ransomware incidents. These 

the sorts of threat actors who can circumvent 

organizations generally have sufficient security 

even a mature organization’s security controls—

tools, robust cyber liability insurance, and 

dismissing the threat of ransomware can overlook 

strong data recovery programs or operational 

the infrequent but impactful ransomware attacks 

redundancy. Instead of ransomware, these 

that are now run by APT groups.

organizations are often more concerned about 

defending against nation\-state attackers and 

advanced persistent threat (APT) groups. 

Ransomware and Extortion Report 2023 \| 29

Some APT groups use ransomware to raise 

Ransomware payments could (in some 

money, either for individuals or for their 

cases) help fund these countries’ domestic 

organization. In other cases, threat actors use 

programs, which has led the U.S. Cybersecurity 

ransomware as a distraction from a larger and 

Infrastructure and Security Agency (CISA) to 

more impactful compromise.

warn that paying ransomware operators could 

APT Financial Motivation

organizations take proactive steps to prevent 

pose sanctions risks. They also noted that when 

Threat groups from countries that have been 

observed using ransomware in their attacks 

(including North Korea and Iran) are also among 

those currently under economic embargoes or 

sanctions by the United States government. This 

perhaps gives them extra motivation to seek 

financial benefit—and carries legal consequences 

that may eliminate an organization’s ability to pay 

a ransom demand.

ransomware attacks, the U.S. Treasury’s Office 

of Foreign Assets Control (OFAC) would be more 

likely to resolve apparent sanctions violations 

with a nonpublic enforcement response.

The British Office of Financial Sanctions 

Implementation (OFSI) issued sanctions in 

February against a number of individuals 

associated with ransomware groups. Guidance 

from the OFSI indicates that the purpose is to 

“disrupt and reduce the profitability 

Threat groups from North Korea seem particularly 

of ransomware.”

interested in financial gain, as other tactics 

observed in their attacks (such as cryptocurrency 

theft and ATM cash\-outs) also fit this pattern.

Paying ransoms will likely be even more heavily 

scrutinized by governments worldwide, especially 

as nations continue to sanction Russia, with 

which a number of well known ransomware 

groups are associated.

Ransomware and Extortion Report 2023 \| 30

APT Smoke Screens and Red Herrings

Other threat groups, including some from Iran or 

Defending Against APTs and 
Cybercrime Groups

China, seem to have a different objective when 

The TTPs used to deploy ransomware for either 

using ransomware. Threat actors can gain more 

APT or cybercrime groups are often identical. 

than money from deploying ransomware—it also 

Both groups exploit vulnerabilities to gain access 

has potential for both destruction and espionage.

to a target system, then compromise credentials 

Some malware authors have taken steps to 

and move laterally.

blur the lines between ransomware and wipers. 

These common areas are where organizations 

Iranian attackers have specifically used wipers 

must focus their defenses and visibility. 

for destructive effect. Wipers could be very 

Unfortunately, paying a ransom is not always 

useful for getting rid of evidence of a threat 

the end of the story. With APT groups in the mix 

groups’ activities, while creating the appearance 

and ransomware groups using multi\-extortion 

of a ransomware attack. If this approach is 

in the majority of the cases we see, apparent 

successful, organizations may not realize the true 

ransomware attacks are often related to data 

purpose of a threat group’s intrusion.

exfiltration. This can be especially concerning 

in light of a trend of cyber insurance providers 

Similarly, ransomware has been used as a 

stating that acts of war won’t be covered. In 

way of disguising intellectual property theft or 

some cases, a ransomware attack attributable to 

cyberespionage as something more banal. APT 

APT actors could be defined as such.

groups steal data from environments and attempt 

to pass it off as a multi\-extortion scheme, 

promising to destroy the data if a ransom 

payment is made. In reality, the stolen data is 

not destroyed and is likely used to the threat 

actor’s advantage.

Ransomware and Extortion Report 2023 \| 31

CONCLUSION

What to Expect From 
Extortion Groups in 2023

The most important information about the 

in cloud environments that they’ll need to 

threat landscape is not where we have been, but 

work through. 

where we are going. When we ask our incident 

responders and threat intelligence analysts 

However, it’s always been clear that 

what’s coming for extortion, they make a few 

ransomware actors will shift their focus to 

key predictions.

cloud environments and engage in attacks 

that require more skill but could have a larger 

Prediction \#1: Government involvement will 

payoff due to the potential operational impact 

be key to disrupting the operations of extortion 

to organizations. In recent years, Unit 42 has 

groups.

tracked cloud threat actors—individuals or 

Bans on payments to certain groups and 

groups posing a threat to organizations through 

countries have changed the landscape of the 

directed and sustained access to cloud platform 

ransomware and extortion business. In some 

resources, services or embedded metadata. 

cases, concerns about sanctions may have 

These threat actors have evolved their TTPs 

influenced more organizations to refuse to pay 

specifically to target cloud workloads.

threat groups, lowering revenue and causing 

affiliates to abandon known groups to work with 

While the shared responsibility model reduces 

unsanctioned groups instead.

users’ burden in securing infrastructure, platform, 

and software in the cloud, we’ve also seen 

Prediction \#2: This will be the year we see a 

organizations—particularly the world’s largest—

large cloud ransomware compromise.

transfer increasing amounts of valuable data and 

Most of our cloud incident response cases thus 

workloads to the public cloud. 2023 will be the 

far have shown threat actors reaching for low\-

year that this tempts threat actors to make the 

hanging fruit. Organizations often neglect basic 

adaptations needed to deploy ransomware in 

security controls and don’t take advantage of 

cloud environments. 

security features offered by the major cloud 

service providers or additional enhanced cloud 

When this happens, it will raise new questions 

security tools. While threat actors know about 

about the shared responsibility model—especially 

these gaps, they’ve mostly chosen to not exploit 

if ransomware deployed on a cloud service 

these security issues for ransomware and 

provider’s platform manages to affect 

extortion since there are still some complexities 

multiple clients.

Ransomware and Extortion Report 2023 \| 32

N
O

I

T
A
D
N
E
M
M
O
C
E
R

UNIT 42 EXECUTIVE 

RECOMMENDATION:

Protect Your Cloud Architectures

Threat actors will continue to weaponize 

and build attack payloads to compromise 

cloud workloads. As such, it is integral that a 

comprehensive cloud security program (from a 

governance perspective) and a cloud security 

platform (from a technical controls perspective) 

are both in place at the organization. The cloud 

security platform should be able to detect and 

prevent attacks to cloud workloads, network 

security, code (including infrastructure as code 

and source code), containers, identities and keys, 

and data.

Prisma Cloud is one example of a platform that 

offers comprehensive cloud native security.

Read Mitigating Cyber Risks with MITRE 

ATT\&CK for an in\-depth set of recommendations 

by Unit 42 incident responders.

Ransomware and Extortion Report 2023 \| 33

Prediction \#3: Threat actors will identify 

novel means of initial access.

Our incident responders are seeing threat 

What is SEO Poisoning?

actors turning to different methods of initial 

Threat actors leverage search engine 

access, including SEO poisoning (especially 

optimization (SEO) to infect potential 

augmented by malvertising), callback phishing, 

victims. Unit 42 has often seen this take the 

and fake software installs and/or updates. This 

form of (fake) software downloads, browser 

is because of the effectiveness of introducing 

updates, or malicious document templates. 

social engineering elements, as well as the need 

For example, a threat actor compromises 

to move away from other methods that are 

legitimate websites and shares supposed 

commonly detected.

Prediction \#4: Threat actors will 

ramp up additional extortion methods. 

templates for common business document 

types, such as certain accounting or human 

resources forms, and these files contain 

malware. When a victim is searching for 

Our data already shows an increase of data theft 

some kind of template (e.g., an invoice 

and harassment in conjunction with encryption. 

template), they find the malicious file via 

We expect this trend to continue as threat actors 

search results and upon downloading and 

respond to lower success rates by attempting to 

opening it, are infected with malware. This 

increase the pressure to pay. This leads to our 

malware gives the threat actor a foothold 

next prediction.

into the victim’s environment. Unit 42 has 

repeatedly seen GootLoader and SocGholish 

Prediction \#5: Extortion without 

in association with this technique.

encryption will rise. 

As threat actors have found success by adding 

extortion methods to ransomware, some groups 

have drawn the conclusion that extortion can 

be effective on its own. Forgoing the encryption 

step allows threat actors to reduce the technical 

complexity of an attack. We expect more groups 

to explore this approach.

Ransomware and Extortion Report 2023 \| 34

Prediction \#6: Politically\-motivated 

Prediction \#8: Attackers will infect 

ransomware incidents will rise.

supply chains and source code of victims 

Ransomware and extortion are most obviously 

before using ransomware to distract from 

carried out for financial gain. However, in 

the supply chain infection.

some cases, these activities can be connected 

As more organizations learn how to deal 

to political motivations. Groups may use 

with ransomware, they may begin to treat 

ransomware to fund other politically\-motivated 

a ransomware infection as routine. Threat 

activities. They may also use ransomware 

actors will take advantage of this by deploying 

and extortion to disrupt the political process, 

ransomware to distract from the true purposes 

destabilize critical infrastructure, create fear and 

of their attacks. Taken to an extreme, this could 

anger at governments, and sow discord.

allow threat actors to remain under the radar 

Prediction \#7: Insider threats will 

large numbers of organizations worldwide. 

while orchestrating attacks that could affect 

lead to extortion attempts.

In 2023 alone, there have been more than 

Organizations should review incident response 

100,000 layoffs from more than 300 tech 

plans for ransomware and extortion with a 

companies. Some of the people affected will 

view to the future landscape. We expect highly 

hold a grudge—and have the skills to take 

motivated threat actors to continue to seek 

revenge. Insider threats can be particularly 

additional layers of leverage to get what they 

dangerous because employees are more likely to 

want from their targets. We anticipate other 

know where the crown jewels are kept. In today’s 

types of threat groups taking advantage of 

environment, an insider threat can cover their 

known cybercrime techniques. Responsible 

identity by selling access and other information to 

security leaders should consider that dealing 

cybercriminal groups, making the act potentially 

with today’s extortion techniques goes beyond 

more tempting. 

safeguarding data—as vital as that is. It is also a 

key responsibility to protect your organization’s 

reputation, and the safety of employees, 

partners, and customers.

Ransomware and Extortion Report 2023 \| 35

N
O

I

T
A
D
N
E
M
M
O
C
E
R

UNIT 42 EXECUTIVE 

RECOMMENDATION:

Talk to Your Board About 
Ransomware and Extortion

When it comes to ransomware, boards are 

most concerned with risk management and 

how effectively the organization is managing 

ransomware threats to the business. Boards 

frequently ask, after seeing in the news that one 

of their peers was significantly hit by ransomware 

or extortion, “Would we be able to prevent that 

type of attack?” 

When the CISO is asked this type of question, 

they need to have defensible, objective data to 

respond with that maps directly to the risks that 

boards are most concerned with. These risks are 

often regarding the following categories: 

• Strategic risk

• Reputational risks

• Compliance or regulatory concerns

• Operational issues

• Financial risks

The CISO’s reponse should be able to link 

their ransomware and extortion readiness and 

prevention capabilities to those that would 

mitigate the risk areas that the board is 

focused on.

Ransomware and Extortion Report 2023 \| 36

Organizations that are well prepared to engage in 

these discussions focus on proactively improving 

their security posture against known attacker 

tactics and techniques. Unit 42 consultants 

leverage the experience of responding to 

thousands of attacks into services that discover 

weaknesses for clients. Our consultants work 

with clients to build roadmaps and proactively 

secure gaps. 

These trusted security advisors use Palo Alto 

Networks technology to accomplish 

• Attack Surface Assessments

• Ransomware Readiness Assessments

• 

Incident Response Playbook 

Design and Review

• 

Incident Simulation Exercises

• SOC Transformations

Unit 42 consultants also partner with clients to 

discover and improve their capabilities to respond 

with a host of readiness and testing offerings 

aligned with the goals of the CISO and the needs 

of the board.

Read Mitigating Cyber Risks with MITRE 

ATT\&CK for an in\-depth set of recommendations 

by Unit 42 incident responders.

Ransomware and Extortion Report 2023 \| 37

S
T
R
E
P
X
E

O
T

T
U
O

H
C
A
E
R

Need help with a ransomware or 

extortion incident? Call in the experts.

If your files and applications are inaccessible 

due to a ransomware attack, please contact 

us. The Unit 42 Incident Response team is 

available 24/7, year\-round, and can swiftly help 

investigate, contain, and eradicate the threat, so 

you can restore operations quickly. And while we 

hope you never need it, we can help negotiate 

ransom demands on your behalf.

Additionally, with a Unit 42 Retainer in place, 

you can make our incident response experts an 

extension of your team—on speed dial. You can 

also choose to allocate your retainer credits for 

proactive Unit 42 cyber risk management services, 

such as a Ransomware Readiness Assessment.

Ransomware and Extortion Report 2023 \| 38

 
 
 
 
Methodology

In creating this report, we reviewed the findings 

We also gathered information from our ongoing 

from a selection of approximately 1,000 incident 

monitoring of dark web leak sites, as well as 

response cases Unit 42 completed between 

our threat intelligence analysts’ work tracking 

May 2021 and October 2022\. We reviewed a 

cybercrime groups and APTs. 

smaller subset (about 100 cases) for insights 

into ransomware and extortion negotiations. 

Finally, we supplemented our case data by 

While the majority of cases were located in the 

conducting in\-depth interviews with experienced 

U.S., the threat actors conducting attacks were 

security consultants to gather recommendations 

located worldwide while targeting businesses, 

and predictions based on their work with clients 

organizations, and IT infrastructure worldwide. 

in specific areas of expertise. 

Ransomware and Extortion Report 2023 \| 39

Unit 42 Incident Response Methodology

Every minute that an attack remains unresolved 

costs your organization money and can damage 

Investigate

its reputation. With Unit 42 Incident Response 

We work to fully understand the incident as 

team experts by your side, you will jump\-start 

we investigate what happened, leveraging the 

your investigation and take advantage of our 

available data and working alongside your team.

experience responding to thousands of incidents 

similar to yours. With our threat\-informed 

Secure

approach to incident response and advanced 

As the incident is contained and the threat 

tools across endpoint, network, and cloud, we 

actor and their tools are eradicated from your 

provide fast containment to minimize the impact 

environment, we concurrently assist your 

on your business.

organization with rapidly restoring operations.

Unit 42’s average response time—how long it 

Support and Report

takes us to make initial contact after receiving a 

Unit 42 will also assist you in understanding 

request for assistance—is well under 15 minutes. 

the root cause and potential impact of the 

Once called in, we work quickly to understand 

incident, including any unauthorized access or 

the full scope of the intrusion, which systems 

acquisition of sensitive information that may 

are impacted, and what security actions have 

trigger legal obligations.

already been taken so we can quickly contain the 

incident. We do this quickly, and remotely, to help 

Transform

you respond to an incident with speed. We follow 

We believe a key step in incident response is 

the proven methodology outlined below.

helping ensure an improved security posture 

We follow a proven methodology:

specific improvements and build out incident 

Scope

response plans that will help protect against 

For an accurate understanding of the incident, 

future and similar attacks.

going forward. We work with you to apply 

it’s critical to get the scoping phase right. This 

allows us to align the right resources and skill sets 

to get your organization back running as quickly 

as possible and accurately estimate the level of 

effort needed to assist you.

Learn more about Unit 42 
Incident Response services

SCOPE

INVESTIGATE

SECURE

SUPPORT \& 
REPORT

TRANSFORM

Define engagement 

Fully understand the 

Contain and eradicate

Findings and response 

Improve your security 

scope 

incident

Assess the breadth, 
severity, and nature of 
the security incident.

Our experts use 
advanced tools for 
evidence collection, 
detection and analysis 
to flag IoCs, TTPs and 
other clues.

We remove the 

threat with custom 

eradication strategies 

and provide 24/7 

monitoring against new 

malicious activity.

Threat Intelligence

assistance 

posture 

Get a detailed 
investigation report 
as well as guidance 
in implementing 
additional security 
controls while you get 
back on your feet.

Use lessons learned 
and apply specific 
improvements to your 
security approach to 
protect against future 
and similar attacks.

Ransomware and Extortion Report 2023 \| 40

 
 
About Palo Alto Networks 

Palo Alto Networks is the world’s cybersecurity leader. We innovate to outpace cyberthreats, 

so organizations can embrace technology with confidence. We provide next\-gen cybersecurity to 

thousands of customers globally, across all sectors. Our best\-in\-class cybersecurity platforms and 

services are backed by industry\-leading threat intelligence and strengthened by state\-of\-the\-art 

automation. Whether deploying our products to enable the Zero Trust Enterprise, responding 

to a security incident, or partnering to deliver better security outcomes through a world\-class 

partner ecosystem, we’re committed to helping ensure each day is safer than the one before. 

It’s what makes us the cybersecurity partner of choice. 

At Palo Alto Networks, we’re committed to bringing together the very best people in service 

of our mission, so we’re also proud to be the cybersecurity workplace of choice, recognized 

among Newsweek’s Most Loved Workplaces (2021\), Comparably’s Best Companies for 

Diversity (2021\), and HRC’s Best Places for LGBTQ Equality (2022\). For more information, 

visit www.paloaltonetworks.com.

About Unit 42

Palo Alto Networks Unit 42 brings together world\-renowned threat researchers, elite incident 

responders and expert security consultants to create an intelligence\-driven, response\-ready 

organization that’s passionate about helping you proactively manage cyber risk. Together, 

our team serves as your trusted advisor to help assess and test your security controls against 

the right threats, transform your security strategy with a threat\-informed approach, and respond 

to incidents in record time so that you get back to business faster.Visit paloaltonetworks.com/unit42\.

3000 Tannery Way 

Santa Clara, CA 95054

Main \+1\.408\.753\.4000 

Sales \+1\.866\.320\.4788 

Support \+1\.866\.898\.9087

© 2023 Palo Alto Networks, Inc. Palo Alto Networks is a registered 

trademark of Palo Alto Networks. A list of our trademarks can be 

found at www.paloaltonetworks.com/company/trademarks.html. 

All other marks mentioned herein may be trademarks of their 

respective companies. 2023 Unit 42 Ransomware and Extortion 

www.paloaltonetworks.com

Report 03/2023\.