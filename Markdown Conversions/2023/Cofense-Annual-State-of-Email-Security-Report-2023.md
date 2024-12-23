# 2023 ANNUAL STATE of EMAIL SECURITY REPORT
ISSUED MARCH 2023

## Table of Contents
- [Letter from the CISO](#letter-from-the-ciso)
- [Executive Summary](#executive-summary)
- [Top Attack Vector in 2022: Credential Phishing](#top-attack-vector-in-2022-credential-phishing)
- [Emotet & Qakbot Remain the Top Malware Families to Watch](#emotet--qakbot-remain-the-top-malware-families-to-watch)
- [BEC Continues to be One of the Top Cybercrimes for the 8th Year in a Row Related to Financial Losses](#bec-continues-to-be-one-of-the-top-cybercrimes-for-the-8th-year-in-a-row-related-to-financial-losses)
- [Successfully Bypassing Two-Factor Authorization (2FA) to Gain Access to Accounts](#successfully-bypassing-two-factor-authorization-2fa-to-gain-access-to-accounts)
- [Payroll Diversion Attacks Still Flying Under the Radar](#payroll-diversion-attacks-still-flying-under-the-radar)
- [Law Enforcement’s Takedown of Cybercrime](#law-enforcements-takedown-of-cybercrime)
- [Scamming the Scammers](#scamming-the-scammers)
- [Attackers Still Request Gift Cards in 2022](#attackers-still-request-gift-cards-in-2022)
- [Web3 Technologies Used in Phishing Campaigns Increased 341%](#web3-technologies-used-in-phishing-campaigns-increased-341)
- [Telegram Bots as Exfiltration Destinations Increased 800%](#telegram-bots-as-exfiltration-destinations-increased-800)
- [Phish Swimming in Murky Waters](#phish-swimming-in-murky-waters)
- [Downstream Impacts, Ransomware](#downstream-impacts-ransomware)
- [Big Breaches](#big-breaches)
- [World Events](#world-events)
- [Blockchain, Cryptocurrency and NFT Phishing](#blockchain-cryptocurrency-and-nft-phishing)
- [Energy Sector (Critical Infrastructure) on High Alert](#energy-sector-critical-infrastructure-on-high-alert)
- [Malicious HTML Attachments](#malicious-html-attachments)
- [Adobe is the Top .com Domain Abused to Deliver Phishing Emails](#adobe-is-the-top-com-domain-abused-to-deliver-phishing-emails)
- [Top Malicious Attachment Types Reaching Inboxes](#top-malicious-attachment-types-reaching-inboxes)
- [Emotet Phishing Emails Exploit 2022 Tax Season, Spoofing IRS](#emotet-phishing-emails-exploit-2022-tax-season-spoofing-irs)
- [Return of Emotet Phishing Emails](#return-of-emotet-phishing-emails)
- [Malware Foothold: QakBot](#malware-foothold-qakbot)
- [Noteworthy Mentions](#noteworthy-mentions)
- [Phishing Attacks Supported by Illicit Marketplaces – “Phishing as a Service (PaaS)”](#phishing-attacks-supported-by-illicit-marketplaces--phishing-as-a-service-paas)
- [Conti Leaks Demonstrated Importance of Phishing in Ransomware Operations](#conti-leaks-demonstrated-importance-of-phishing-in-ransomware-operations)
- [Whaling in Bulk](#whaling-in-bulk)
- [Industry Overview](#industry-overview)
- [So Now What?](#so-now-what)
- [How to Enhance Your Email Security](#how-to-enhance-your-email-security)
- [Checklist: Protect Your Organization from Top Threats](#checklist-protect-your-organization-from-top-threats)
- [BEC/Vendor Email Compromise](#becvendor-email-compromise)
- [Credential Phishing](#credential-phishing)
- [Attachments](#attachments)
- [Malware](#malware)
- [Conclusion](#conclusion)
- [Appendix](#appendix)
- [List of Figures](#list-of-figures)

2023 Cofense Annual State of Email Security Report  •  1

# Letter from the CISO
A
s I transition from behind the scenes of this report, I wanted to take 
a moment to share some of my thoughts on what we’ve seen over 
the past year. Taking on the role of CISO has added some additional 
insight as I stepped back into the role of practitioner again. Now 
that I review our cyber insurance and 3rd party questionnaires, it has given 
me perspective into why organizations have started asking more questions 
about simulation metrics. 
Something that hasn’t changed over the last year, your SOC still needs HELP! As teams continue 
to deal with workforce shortages, remote work and burnout, optimizing processes and automation 
are even more critical to defend the perimeter. As I’ve spent time with incident responders and 
attended conferences to hear from practitioners, it’s clear the community demands products 
and solutions to integrate together rather than stand-alone products. It’s this reason that we’ve 
continued to enhance our APIs, while also expanding our integration partnerships, allowing you to 
quickly identify threats hitting the inbox and moving those IOCs to your other controls to defend 
against the adversary quickly.  
Have you followed the trend of adding a Cyber Threat Intelligence (CTI) team? We continue to hear 
from customers that are building out teams to become more proactive in defending against the 
threat landscape. But adding more threat feeds isn’t productive – or helping your SOC automation. 
This is why we have stood firm on our “human-vetted” intelligence, to ensure you can depend on 
adding IOCs to your automation. It’s more critical than ever to ensure your intelligence feeds are 
actionable intelligence allowing you to reduce noise and provide context to those alerts.  
As I think about the conversations I’ve had with SOC teams, it’s become clear they have a love-
hate relationship with the reporting of suspicious emails versus employees just deleting them. 
Our intelligence is enriched because users report suspicious emails. The SOC can benefit from 
those suspicious messages being reported by extracting the IOCs and taking action to mitigate a 
threat. However, the button that is often used is the “delete” button by the user who is just flat-out 
annoyed with “spam” and wants it to stop. As I scanned through the simulation campaigns sent 
over the year, it suddenly occurred to me why users struggle with whether or not to report an email. 
It’s because you’re sending the wrong types of simulations, coupled with punitive programs putting 
additional pressure on the user to just report the email.  Simulate the threats making it to the inbox 
– NOT the topics already blocked by your spam filters, aka your Secure Email Gateway. I’m looking 
at you “eCard/Valentines” campaign fans. 
As you read this report, you’ll find it difficult to identify the simulation section as we’ve reported 
in years past. That was intentional. For years we’ve pushed our security awareness teams to align 
their programs to “real phish.” For the past few years, we’ve only added templates based on real 
phish we’ve observed. That too is intentional. But what you find are some highlights of what we 
observed over the year and how you can adjust your Security Awareness and Incident Response 
programs to better defend against the phishing threats making it to your users’ inboxes. It has been 
an exciting year talking to customers who have experienced the impact of the network effect. 
Tonia Dudley 
VP, CISO at Cofense 
2023 Cofense Annual State of Email Security Report  •  2

> It’s more 
critical than 
ever to 
ensure your 
intelligence 
feeds are 
actionable 
intelligence 
allowing you 
to reduce noise 
and provide 
context to 
those alerts.

Tonia Dudley
VP, CISO at Cofense

# SECTION 1
2023 Cofense Annual State of Email Security Report  •  3
# SECTION 1
# EXECUTIVE SUMMARY
I
n 2022, cybersecurity threats increased exponentially and it’s no surprise 
the vast majority involved phishing. As threats increase in frequency, 
intensity, and sophistication, the need for rapid and actionable intelligence 
has never been greater. As a result of this increased frequency, Cofense 
Intelligence saw 569% more malicious phishing emails, had a 478% increase 
in the number of credential phishing related Active Threat Reports published 
and identified a 44% increase in malware. Based on this data, we conclude 
that credential phishing was the cyber threat of choice in 2022.

![Figure 1: Top Themes in Active Threat Reports]

Due to this increase in threat activity, we were able to detect, auto-quarantine, and remove a record-
setting number of malicious emails and phishing campaigns that were missed by Secure Email 
Gateways (SEGs) as seen in Figure 2. 

![Figure 2: COFENSE AUTO-QUARANTINE SUMMARY]

> Cofense 
Intelligence saw 
569% 
more malicious 
phishing 
emails, had a 
478% 
increase in 
the number 
of credential 
phishing related 
Active Threat 
Reports published 
and identified a
44% 
increase 
in malware.

> Thanks to the power 
of Cofense Intelligence, 
we saw a 
626% 
YoY increase in emails 
detected and auto-
quarantined from 
customer inboxes 
worldwide.

# SECTION 1
2023 Cofense Annual State of Email Security Report  •  4
- Credential Phishing is the top attack vector with a 478% increase in malicious emails identified
- Emotet & QakBot remain the top malware families to watch
- BEC continues to be one of the top cybercrimes for 8th year in a row
- Web3 technologies used in phishing campaigns increased 341%
- Telegram bots as exfiltration destinations increased 800%

The cybersecurity landscape is always evolving, so it is imperative to stay on top of the latest trends and tactics. 
To learn more about what our intelligence trends revealed, here’s a more in-depth look at what we discovered last year.
Phishing is a major threat because it is so simple. Often, we hear of large, destructive attacks that sound extremely advanced, beyond 
the comprehension of security-minded individuals. It is important to remember the initial access is often acquired well before the 
incident occurs and may come from simple phishing campaigns that have no apparent connection to any advanced persistent threat 
group. In the aftermath, as these sophisticated attacks make the news, organizations should not become so consumed with searching 
for specific indicators of compromise (IOCs) or malware that they ignore the emerging phishing threats. As threats increase in frequency 
and intensity, it is not only critical, but a fundamental necessity to protect and defend against daily emerging phishing attacks.
Over the past decade, we have built an unrivaled standard of phishing expertise. Our goal is to contribute the phishing expertise 
necessary to turn humans around the world into the strongest link in the security chain, and to translate the resulting human efforts 
into machine learning, phishing threat intelligence, and automated action(s). 
With our global network of 35+ million human reporters, we crowdsource millions of suspicious enterprise emails that are processed, 
enriched, and analyzed by our unique intelligence insights. At times, even removing threats within seconds before users have the 
chance to interact with them.

![Figure 3: PERCENTAGE OF MALICIOUS EMAILS MISSED BY SEG IN 2022]

> How did your SEG stack 
up? These are real 
threats detected by 
our Phishing Defense 
Center (PDC) that are 
bypassing your current 
email controls.

**BASED ON OUR INTELLIGENCE, THE TOP FIVE HIGHLIGHTS OF THE EMAIL SECURITY LANDSCAPE ARE:**

# SECTION 1
2023 Cofense Annual State of Email Security Report  •  5
# TOP FIVE  Top Attack Vector in 2022: Credential Phishing
It was no surprise to see credential phish still rank as the leading threats seen by our Phishing Defense Center (PDC) customers. 
As one of the several collection inputs to Cofense Intelligence, it’s also no surprise to see an increase of 478% of credential phishing-
related Active Threat Reports published. This threat category still plays a significant role in the ransomware attack chain, as well as 
BEC. Wait, BEC? How does that connect? When a user falls susceptible to a credential phish, while the password may have been 
reset, the threat actor remains persistent in the inbox by adding auto-forwarding rules for keywords related to financial transactions 
(i.e. invoice, purchase order, quote). These emails are then, in turn, used to target downstream organizations with BEC/Vendor 
Email Compromise threats.

![Figure 4: MALICIOUS THREATS OBSERVED BY PDC]

# TOP FIVE  Emotet & QakBot Remain the Top Malware Families to Watch
Throughout 2022, we analyzed and assessed top 
malware families seen in Figure 5. However, in this 
report, we wanted to provide a quick reference 
guide for understanding the malware families 
that made up the highest volume of phishing 
campaigns disseminated in 2022.
There are several characteristics that 
can make a malware family more 
appealing to threat actors, such as 
the malware features, cost, and 
complexity. In combination, 
these properties determine 
how well malware aligns to 
a threat actor’s agenda 
for a phishing campaign. 
Figure 5 shows the top 
5 malware families 
in 2022. 

> As one of the several 
collection inputs to 
Cofense Intelligence, 
it’s also no surprise to 
see an increase of 
478% 
of credential 
phishing-related 
Active Threat 
Reports published.

# SECTION 1
2023 Cofense Annual State of Email Security Report  •  6

![Figure 5: TOP 5 MALWARE FAMILIES IN 2022]

The continued position of Emotet (and consequently malware loaders, which are often the first 
stage of a compromise) at the top of the list is a testament to its outscaling of all other malware-
delivery campaigns. There was an overall increase in volume for keyloggers and Remote 
Access Trojans (RATs). Information stealers saw the largest increase with malware families like 
FormBook being high commodities in the phishing threat landscape. We continued to watch 
Snake Keylogger in 2022, which is a staple in the phishing threat landscape as it is a keylogger 
written in .NET. It can monitor a user’s keystrokes, scan applications to steal saved credentials, 
and exfiltrate this data through a variety of protocols. Although it is not as popular as other malware families such as FormBook or 
Agent Tesla, it did maintain a significant presence throughout 2022, and 
its usage continues to increase. This banking trojan malware type passed 
RATs due to a high volume of QakBot phishing emails. Despite not having 
as high of volume as others in the Top 5, Qakbot remains at the top of our 
list of families to watch since it has been far more successful at bypassing 
SEGs and reaching inboxes. 

![Figure 6: MALWARE CHARACTERISTICS]

> Want more detailed insights 
on Emotet and QakBot? 
Make sure you read the 
strategic analysis starting 
on page 15!

Figure 6 shows the most common characteristics 
of each malware family and the capabilities that 
we observed in phishing campaigns of malicious 
emails that would have reached inboxes.

# SECTION 1
2023 Cofense Annual State of Email Security Report  •  7
# TOP FIVE  BEC Continues to be One of the Top Cybercrimes for the 
8th Year in a Row Related to Financial Losses
In 2022, Business Email Compromise (BEC) continued to be one of the leading cybercrimes related to financial losses for the 8th year 
in a row. With BEC responsible for billions in global losses with victims in 90% of the world, it’s no wonder scammers outside of Nigeria 
have started taking notice of the successes of BEC. While SEGs have evolved from spam filters to now being used to detect and potentially 
block malware, malicious links, and ransomware attacks, many fail at detecting conversational-based phishing attacks such as this. 
Over the last year, BEC actors attacked with many different techniques, including requesting checks, wire transfers, payroll 
diversions, and gift cards. While many of these techniques are nothing new, we have observed a continued blending of tactics to 
make detection and mitigation even more difficult for organizations. By using and blending these attacks, threat actors continue to 
bypass SEGs to manipulate users into sending billions of dollars year after year. 
**Successfully Bypassing Two-Factor Authentication (2FA) to Gain Access to Accounts** 
By putting the “compromise” in BEC, threat actors continued to use credential phishing attacks to gain access to organization inboxes 
to perform man-in-the-mailbox (MiTMbox) attacks. Once an attacker gains access to an organization’s email account, they will 
routinely create email forward rules to monitor all traffic coming in and out of the account. In some cases, they will create rules that 
include the words “purchase order,” “invoice,” or other financially based transactions between clients. 
Once the threat actors identify an invoice or opportunity to re-route the transaction, the threat actors pounce, replying to the known 
and trusted email thread with new information. In some cases, this will come from a look-alike domain, and in other cases this 
will come from the compromised infrastructure itself. By modifying and forging invoices with new banking and account numbers, 
scammers are able to re-route business transactions and invoices to accounts under their control. Unfortunately, many of these 
attacks are caught too late for a successful financial reversal. 
One of the best ways to mitigate against these attacks is to use two-factor authentication (2FA), as the requirement for a second 
piece of information makes it virtually impossible to log into an account without the second piece of information. However, in 
2022, Microsoft published a technique used by scammers called adversary-in-the-middle (AiTM) that successfully bypasses 2FA 
authentication. Through hijacking the session cookie, BEC attackers are able to gain access to the user’s account. 
**Payroll Diversion Attacks Still Flying Under the Radar** 
“Are you in the office? I need to update my direct deposit. Can I provide a voided check?” is still a technique used by BEC actors 
today. Dubbed payroll diversion scams, threat actors target Human Resources departments that have financial authority to change 
the financial records of employees. While attackers made a shift in mid 2014 to target enterprises and corporations, these attacks 
largely go unreported due to the same stigmas and lower losses as gift card scams. We continued to track wave after wave of 
payroll diversion attacks through our Cofense Reporter™ submissions from customers, meaning these attacks are still successfully 
bypassing email gateways. 

> Are you in 
the office? I 
need to update 
my direct deposit. 
Can I provide a voided 
check?

> BEC THREAT TECHNIQUE

# SECTION 1
2023 Cofense Annual State of Email Security Report  •  8

![Figure 7: BEC DOMAINS]

**Law Enforcement’s Takedown of Cybercrime**
Although BEC, ransomware, and other cybercrime operations carried on through 2022, our research indicated that threat actors 
felt pressure from the arrests as law enforcement agencies worldwide made significant strides combating cyber threat actors. 
Authorities arrested individuals suspected of involvement in the LockBit ransomware and JabberZeus banking trojan operations. 
The FBI infiltrated the Hive ransomware group starting in July, ultimately leading to the takedown of the entire operation in January 
2023. Authorities in several countries arrested dozens of suspected BEC perpetrators, as well. Ransomware attacks and payouts both 
trended downward compared to 2021. If authorities continue to make high-impact arrests, we expect to see more downward pressure 
on phishing threats, as actors will be forced to adapt, harden their operations against intelligence efforts and/or decentralize. 
**SCAMMING THE SCAMMERS**
To dig deeper into this conversational tactic, we spent some time interacting with real emails reported by users. In phases one 
and two of a multi-part study into the criminal ecosystem of gift card attacks, we responded to BEC phishing attacks to gauge 
the level of interaction from the scammers. During this phase of the research, we wanted to see how many responses it took to 
identify the cash out method for BEC attacks. 
In phase one where we simply analyzed the delivery email, 6% of the analyzed emails presented themes of gift cards in the initial 
phish. In phase two, we responded to the scammers to try and identify the phishing theme. In 22% of these cases, we were able 
to identify gift card requests from the scammers. The significant jump signifies that for most gift card BEC attacks, scammers 
are looking for a response prior to asking for gift cards. 
**Attackers Still Request Gift Cards in 2022** 
In part three of our gift card study, we launched a successful counter-operation against BEC actors to better understand the 
gift card ecosystem plaguing organizations and small businesses. Just like many types of BEC attacks, scammers pretend to 
be someone in the organization with authority, asking for a quick or urgent task to be done. Once the user confirms, they’re 
instructed to go to a retail store to purchase gift cards in different denominations. In some cases, attackers request the users’ 
phone numbers to move the conversation outside of an organization’s security structure and detection. 
But what happens when scammers ask for gift cards? And more importantly, what happens when they receive gift cards? We 
took $500 dollars of gift cards and gave them to the scammers. We wanted to see what the conversations looked like, how 
quickly they were cashed out, and what insights we could gather from the research. Here is what we learned. 
For the research, we used $25 worth of gift cards in each phish. While scammers typically asked for $500 or $1,000 dollars in 
gift cards, our researchers’ true intent was to get cards in larger denominations, such as $100. It was surprisingly difficult to get 
the scammers to accept a $25 gift card as it broke their script and thought process for what was normally received, causing 
them to question the legitimacy of the funds soon to be stolen. Secondly, once the cards were sent the entire workflow was 
24 hours or less for the card to be stolen, sold, then re-laundered into purchasing other goods online. We identified toy stores, 
greeting card stores, Amazon, and several other strange purchases once the cards were sold. 

> What do you get when 
you analyze 10,000 
email accounts used 
to send over 25,000 
emails? You get visibility 
into which type of email 
accounts used by threat 
actors go undetected. 
Also noteworthy, we 
saw that nine different 
customers received 
an email from the 
same email address, 
which is clearly a 
spoofed domain.

# SECTION 1
2023 Cofense Annual State of Email Security Report  •  9
# TOP FIVE  Web3 Technologies Used in Phishing Campaigns 
Increased 341%
It’s important for threat actors to carefully craft links or carefully select hosts for links in order to bypass SEGs. The malicious use of 
Web3 technologies as a link-crafting tool for phishing campaigns exploded in 2022. “Web3” refers to a set of technologies intended 
to decentralize common internet and computing activity. Users of Web3 protocols host content collaboratively, which removes the 
need for traditional hosting servers and makes censorship much more difficult. A fast-growing number of phishing campaigns used 
Web3 platforms to host malicious content throughout 2022, as evidenced by our strategic analysis, “Abuse of Web3 Technology 
for Evasive Phishing Grows Massively in 2022”. Overall, in 2022 there was a 341% increase in Web3 Technologies used in phishing 
campaigns. Most browsers still require a “gateway” server to interact with Web3-hosted content, which gives organizations a chance 
to detect and block it. However, the technology will likely remain a useful weapon in threat actors’ arsenals for the foreseeable future.
# TOP FIVE  Telegram Bots as Exfiltration Destinations Increased 800%
Among phishing emails reaching inboxes over the course 
of 2022, the utilization of Telegram bots as exfiltration 
destinations for phished information increased gradually 
but significantly, resulting in a year-over-year increase of 
more than 800% between 2021 and 2022. The increase 
is largely associated with the now popular tactic of using 
HTML attachments as delivery mechanisms in credential 
phishing. While Telegram bots being used by threat actors to 
exfiltrate information is not new, it has not been commonly 
known for its use in credential phishing. Telegram bots have 
become a popular choice for threat actors, since they are a 
low-cost/free, single-pane-of-glass solution. Threat actors 
appreciate the ease of setting up bots in a private or group 
chat, the bots’ compatibility with a wide range of programming 
languages, and ease of integrations into malicious mediums 
such as malware or credential phishing kits. Coupling the 
ease of Telegram bot setup and use with the popular and 
successful tactic of attaching an HTML credential phishing 
file to an email, a threat actor can quickly and efficiently reach 
inboxes while exfiltrating credentials to a single point, using 
an often-trusted service.

> Among phishing emails reaching inboxes 
over the course of 2022, the utilization of 
Telegram bots as exfiltration destinations 
for phished information increased 
gradually but significantly, resulting in 
a year-over-year increase of more than 
800%

> Overall, in 2022 there was a
341% 
INCREASE 
in Web3 Technologies 
used in phishing 
campaigns.

> between 2021 
and 2022.

2023 Cofense Annual State of Email Security Report  •  10
# SECTION 2
**Downstream Impacts, Ransomware**
The FBI’s 2022 ICS report states that phishing email is the top crime for ransomware that targets 
organizations around the world. Ransomware is a primary downstream impact from email-based 
threats. In one common scenario, other malware families are delivered initially to gain a foothold, then 
followed by installation of ransomware anywhere from hours to weeks later. In another scenario, a 
credential phishing email campaign gives the threat actor credentials they can use to access systems 
to deploy ransomware directly. In both cases, it is important to look upstream at the chain of events 
that led to the ransomware and determine the payloads delivered within the email. 
In 2021, there were well-known instances of BazarBackdoor being used to deliver ransomware. 
However, in 2022 there was a combination of phishing threats and we cannot point to one 
single major malware used to deliver ransomware. Rather than focusing on the outcome such as 
ransomware, readers should focus on credential phishing, delivery mechanisms, and the malware 
type known as “loaders” which can be used to deliver ransomware. It is preferred to use tools to 
help prevent the delivery of malicious-based emails. Operators of malware families like Emotet and 
Qakbot that offer the services of installing other malware on already-compromised computers (called 
“malware-installation as a service”) are prime options for ransomware operators to gain initial entry. 
These services become partner or “affiliates” in a ransomware operation. In November of 2022, 
Qakbot was identified as the primary malware foothold used by the Black Basta ransomware gang. 
While it is critical to monitor for ransomware at the endpoint, security teams may reduce the 
frequency and impact of endpoint events by focusing on credential phishing and an early-stage 
malware from malicious email campaigns that can in turn be used to deliver ransomware. We 
analyze these threats at great lengths and provide unique human-vetted expertise and analysis with 
actionable insights. We treat each malware infection as a potential vector for future ransomware 
attacks, reverse engineer the payloads and trace the steps that led to the infection to enable our 
customers to determine the flaws in their defenses and prevent phishing attacks. Using solutions 
such as Cofense Intelligence to help detect and prevent infections, while training employees to 
recognize and avoid interacting with malicious content can provide an intuitive line of protection that 
machines are not capable of. Phishing tactics are always evolving and becoming more complex. 
**Big Breaches** 
Data breaches in 2022 seemed to come fast and furious, impacting several high-profile brands in the security sector including Cisco, 
Okta and LastPass. Large data breaches like this can be part of a cyclical pattern that involves phishing, since data breaches can 
begin with a phishing attack or contribute to future phishing activity. 
- In May 2022, Cisco experienced a cyberattack where the attacker had to go to extreme lengths to hack into an employee’s 
personal Google account that contained passwords synced from their web browser. Besides the credential theft, there was an 
additional element of phishing called vishing (voice phishing) and multi-factor authentication (MFA) fatigue where the threat actor 
prompt bombs the user with a flood of user authentications in hopes they will enable the attacker to gain unauthorized access. 
Once the threat actor has a foothold, they build their own backdoor accounts for access. 
- In August 2022, the Okta event occurred where threat actors obtained credentials and unauthorized access to Workforce Identity 
Cloud (WIC) repositories hosted in GitHub and copied source code. Days after the Okta event, LastPass had an incident where 
credentials were obtained to extract information from a backup stored in a cloud-based storage service. The adversary copied 
customer vault data which was stored in a “proprietary binary format” that contained unencrypted data, website URLs, usernames 
and passwords, secure notes, and form-filled data. 
- In August 2022, LastPass’ incident opened the door to an even larger data breach in December which included user account 
information, billing, email addresses, telephone numbers and IP addresses. LastPass’ big data breach affected users across their 
product suite, eventually disclosing loss of source code.

> In 2022, threat 
actors used a 
combination 
of phishing 
threats and we 
cannot point 
to one single 
major malware 
used to deliver 
ransomware.

# SECTION 2
# PHISH SWIMMING IN MURKY WATERS
2023 Cofense Annual State of Email Security Report  •  11
# SECTION 2
When large data breaches occur, it often results in the exposure 
of sensitive documents, personal information of employees or 
customers, and system, network, and application credentials. 
Compromised credentials may provide the threat actors 
responsible for the breach with temporary illicit access, but 
after the breach is discovered and/or publicized, it is much less 
likely that the credentials for those specific accounts will be 
useable. Instead, other sensitive and proprietary information 
(especially if published by the threat actors) can be employed 
in future phishing campaigns. Email addresses may be added 
to phishing target lists, and business process information 
may be used to craft targeted spear-phishing emails. Threat 
actors can also use information obtained from data breaches to 
conduct future credential phishing attacks. Credential stuffing 
attacks use stolen credentials from one website or system to 
gain access to other websites/systems where the user has the 
same credentials. Threat actors then continue the train of impacts by once again using any discovered sensitive information such as 
contact lists, new credentials, and business processes to boost future phishing activity and attacks.
**World Events** 
Many major events happened across the globe over the course of 2022. Threat actors use these events on the world stage to design 
phishing campaigns. The Russia-Ukraine War captured the attention of many over the course of 2022. Cofense Intelligence observed a 
variety of phishing campaigns using the Russia/Ukraine conflict. Threat actors are weaponizing the conflict for financial gain by creating 
well-crafted credential phishing campaigns and donation scams. Threat actors using current 
events as themes within their email campaigns is quite common, and users should be universally 
vigilant against these threats. We have also seen a combination of lure tactics with a 
variety of emails using the Russia/Ukraine war as a lure reported to the Cofense Phishing 
Defense Center directly from enterprise users’ inboxes. Other major world events used in 
campaigns include the death of Queen Elizabeth II and the Beijing Winter Olympics. 
We observed that it is significantly more likely a tried-and-true phishing themes 
will be used rather than a stand-alone current event theme (as actors use 
a combination of methods and tactics). There will always be attempts to 
convince the receiver their mailbox is full and their password needs to be 
updated. Attached invoices of all sorts will make it to people’s inboxes, 
along with shipping receipts, deposit receipts and voicemails. These sorts 
of lures were in the background throughout the year. Threat actors will 
be opportunistic with world events, but there is typically no reason to 
change from the more traditional (and dependable) lures, especially 
as those methods have proven to work. We continue to monitor 
phishing threats related to world events and will continue to 
identify malicious campaigns that are using the current events 
as a lure to target end users.
**Blockchain, Cryptocurrency and NFT Phishing**
Blockchain technology and cryptocurrencies are a popular topic for the general media, and consequently, a target for threat actors 
seeking financial gain. The blockchain is a public ledger used to store virtual currency secured by cryptography, or cryptocurrency. 
This type of digital currency differs greatly from legacy currency, such that banking controls for legacy currency make it difficult, if 
not impossible, for attackers to move currency out of an account. In contrast, a crypto wallet can be emptied almost immediately and 
the funds are unrecoverable. 
Throughout 2022, we observed crypto-themed emails and phishing campaigns seeking to obtain digital wallets that contain tokens, 
but these are not the only malicious purposes for the digital assets. Due to the less-than-secure account controls, cryptocurrency is 
commonly used as payment methods for ransomware and sextortion campaigns, as well as within advance-fee and romance scams. 
Certain malware families also seek to steal cryptocurrency wallet keys stored on infected machines, while others are designed to use 
an infected machine to mine cryptocurrencies.

> Threat actors use sensitive information 
such as contact lists, new credentials, and 
business processes to boost future phishing 
activity and attacks.

2023 Cofense Annual State of Email Security Report  •  12
# SECTION 2

![Figure 8: The Blockchain and Cryptocurrencies in Phishing]

We analyzed an uptick in crypto phishing emails, including one observation where threat actors used a convergence of crypto and the 
Russia/Ukraine war. The phishing email used the current Russia/Ukraine war as a lure