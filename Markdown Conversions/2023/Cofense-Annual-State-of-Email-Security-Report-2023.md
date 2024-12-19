# 2023 ANNUAL STATE of EMAIL SECURITY REPORT
ISSUED MARCH 2023

2023 Cofense Annual State of Email Security Report  •  1

## CONTENTS
[TOC]

2023 Cofense Annual State of Email Security Report  •  1

Letter from the CISO. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  2

### SECTION 1 Executive Summary.
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  3
	
Top Attack Vector in 2022: Credential Phishing. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  5
	
Emotet & Qakbot Remain the Top Malware Families to Watch. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  5
	
BEC Continues to be One of the Top Cybercrimes for the 8th Year in a Row Related to Financial Losses. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  7
 
Successfully Bypassing Two-Factor Authorization (2FA) to Gain Access to Accounts
	
Payroll Diversion Attacks Still Flying Under the Radar
	
Law Enforcement’s Takedown of Cybercrime
	
Scamming the Scammers
 
Attackers Still Request Gift Cards in 2022
	
Web3 Technologies Used in Phishing Campaigns Increased 341%. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  9
	
Telegram Bots as Exfiltration Destinations Increased 800%. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  9
### SECTION 2 Phish Swimming in Murky Waters. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  10
	
Downstream Impacts, Ransomware. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  10
Big Breaches. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  10
World Events. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  11
Blockchain, Cryptocurrency and NFT Phishing. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  11
Energy Sector (Critical Infrastructure) on High Alert.
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  13
Malicious HTML Attachments.
 .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  13
Adobe is the Top .com Domain Abused to Deliver Phishing Emails . .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  14
Top Malicious Attachment Types Reaching Inboxes . .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  15
 
Emotet Phishing Emails Exploit 2022 Tax Season, Spoofing IRS
	
Return of Emotet Phishing Emails
	
Malware Foothold: QakBot
	
Noteworthy Mentions. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  17
 
Phishing Attacks Supported by Illicit Marketplaces – “Phishing as a Service (PaaS)”
 
Conti Leaks Demonstrated Importance of Phishing in Ransomware Operations
	
Whaling in Bulk
	
Industry Overview. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  19
### SECTION 3 So Now What?. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  21 
	
How to Enhance Your Email Security . .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  21
	
Checklist: Protect Your Organization from Top Threats. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 23
	
BEC/Vendor Email Compromise
	
Credential Phishing
	
Attachments
	
Malware	
23
CONCLUSION. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  . 24
APPENDIX . .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  25
	
List of Figures. .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  .  25

2023 Cofense Annual State of Email Security Report  •  2

## LETTER FROM THE CISO

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

> It’s more critical than ever to ensure your intelligence feeds are actionable intelligence allowing you to reduce noise and provide context to those alerts.

Tonia Dudley
VP, CISO at Cofense

## SECTION 1
2023 Cofense Annual State of Email Security Report  •  3

### SECTION 1
### EXECUTIVE SUMMARY

I
n 2022, cybersecurity threats increased exponentially and it’s no surprise 
the vast majority involved phishing. As threats increase in frequency, 
intensity, and sophistication, the need for rapid and actionable intelligence 
has never been greater. As a result of this increased frequency, Cofense 
Intelligence saw 569% more malicious phishing emails, had a 478% increase 
in the number of credential phishing related Active Threat Reports published 
and identified a 44% increase in malware. Based on this data, we conclude 
that credential phishing was the cyber threat of choice in 2022.

**FIGURE 1: TOP THEMES IN ACTIVE THREAT REPORTS**

*A pie chart showing the distribution of themes in active threat reports. The largest slice, at 37%, is "Finance", followed by "Notification/Other" at 36%. The remaining slices are "Account/Password Alert" at 8%, "Document" at 6%, "Shipping" at 3%, "Voicemail" at 2%, "Order" at 2%, "Response" at 1%, "Benefits" at 1%, and "Fax" at 5%.*

Due to this increase in threat activity, we were able to detect, auto-quarantine, and remove a record-
setting number of malicious emails and phishing campaigns that were missed by Secure Email 
Gateways (SEGs) as seen in Figure 2. 

**FIGURE 2: COFENSE AUTO-QUARANTINE SUMMARY**

*A line graph showing the number of malicious emails detected using Cofense Intelligence over time. The x-axis represents the quarters of 2021 and 2022, and the y-axis represents the number of emails. The graph shows a steady increase in detected malicious emails, with a significant jump in Q1 and Q2 of 2022. The text below the graph indicates that 255,863 unique campaigns were identified and 480,754 total malicious emails were identified.*

> Cofense Intelligence saw 569% more malicious phishing emails, had a 478% increase in the number of credential phishing related Active Threat Reports published and identified a 44% increase in malware.

> Thanks to the power of Cofense Intelligence, we saw a 626% YoY increase in emails detected and auto-quarantined from customer inboxes worldwide.

SECTION 1
2023 Cofense Annual State of Email Security Report  •  4

*   Credential Phishing is the top attack vector with a 478% increase in malicious emails identified
*   Emotet & QakBot remain the top malware families to watch
*   BEC continues to be one of the top cybercrimes for 8th year in a row
*   Web3 technologies used in phishing campaigns increased 341%
*   Telegram bots as exfiltration destinations increased 800%

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

**FIGURE 3: PERCENTAGE OF MALICIOUS EMAILS MISSED BY SEG IN 2022**

*A stacked bar chart comparing the percentage of malicious emails missed by various Secure Email Gateways (SEGs) in 2022. The chart shows that a significant portion of malicious emails are missed by each SEG. The SEGs listed include CISCO, FORTINET, GOOGLE, MIMECAST, MICROSOFT, PROOFPOINT, and SYMANTEC. The chart also shows the distribution of threat types, with "Credential Phishing" being the most common, followed by "Malware", "BEC", and "Threat Unavailable".*

> How did your SEG stack up? These are real threats detected by our Phishing Defense Center (PDC) that are bypassing your current email controls.

> BASED ON OUR INTELLIGENCE, THE TOP FIVE HIGHLIGHTS OF THE EMAIL SECURITY LANDSCAPE ARE:

SECTION 1
2023 Cofense Annual State of Email Security Report  •  5

### TOP FIVE Top Attack Vector in 2022: Credential Phishing

It was no surprise to see credential phish still rank as the leading threats seen by our Phishing Defense Center (PDC) customers. 
As one of the several collection inputs to Cofense Intelligence, it’s also no surprise to see an increase of 478% of credential phishing-
related Active Threat Reports published. This threat category still plays a significant role in the ransomware attack chain, as well as 
BEC. Wait, BEC? How does that connect? When a user falls susceptible to a credential phish, while the password may have been 
reset, the threat actor remains persistent in the inbox by adding auto-forwarding rules for keywords related to financial transactions 
(i.e. invoice, purchase order, quote). These emails are then, in turn, used to target downstream organizations with BEC/Vendor 
Email Compromise threats.

**FIGURE 4: MALICIOUS THREATS OBSERVED BY PDC**

*A bar chart comparing the percentage of malicious threats observed by the Phishing Defense Center (PDC) in 2021 and 2022. The chart shows that "Credential Phishing" was the most common threat in both years, followed by "Malware", "BEC", and "Threat Unavailable". The percentage of "Credential Phishing" decreased from 61% in 2021 to 67% in 2022, while the percentage of "Malware" increased from 26% to 23%.*

> As one of the several collection inputs to Cofense Intelligence, it’s also no surprise to see an increase of 478% of credential phishing-related Active Threat Reports published.

### TOP FIVE Emotet & QakBot Remain the Top Malware Families to Watch

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

SECTION 1
2023 Cofense Annual State of Email Security Report  •  6

**FIGURE 5: TOP 5 MALWARE FAMILIES IN 2022**

*A line graph showing the number of malware threats identified for the top 5 malware families in 2022. The x-axis represents the months of 2022, and the y-axis represents the number of threats. The graph shows that Emotet was the most prevalent malware family throughout the year, followed by FormBook, Agent Tesla, Snake, and QakBot.*

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

**FIGURE 6: MALWARE CHARACTERISTICS**

*A table summarizing the characteristics of the top 5 malware families in 2022. The table lists each malware family and indicates whether it has information stealing capabilities, keylogging capabilities, remote access capabilities, loader capabilities, and backdoor controls.*

> Want more detailed insights on Emotet and QakBot? Make sure you read the strategic analysis starting on page 15!

Figure 6 shows the most common characteristics 
of each malware family and the capabilities that 
we observed in phishing campaigns of malicious 
emails that would have reached inboxes.

SECTION 1
2023 Cofense Annual State of Email Security Report  •  7

### TOP FIVE BEC Continues to be One of the Top Cybercrimes for the 
8th Year in a Row Related to Financial Losses

In 2022, Business Email Compromise (BEC) continued to be one of the leading cybercrimes related to financial losses for the 8th year 
in a row. With BEC responsible for billions in global losses with victims in 90% of the world, it’s no wonder scammers outside of Nigeria 
have started taking notice of the successes of BEC. While SEGs have evolved from spam filters to now being used to detect and potentially 
block malware, malicious links, and ransomware attacks, many fail at detecting conversational-based phishing attacks such as this. 

Over the last year, BEC actors attacked with many different techniques, including requesting checks, wire transfers, payroll 
diversions, and gift cards. While many of these techniques are nothing new, we have observed a continued blending of tactics to 
make detection and mitigation even more difficult for organizations. By using and blending these attacks, threat actors continue to 
bypass SEGs to manipulate users into sending billions of dollars year after year. 

#### Successfully Bypassing Two-Factor Authentication (2FA) to Gain Access to Accounts 

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

#### Payroll Diversion Attacks Still Flying Under the Radar 

> “Are you in the office? I need to update my direct deposit. Can I provide a voided check?”

is still a technique used by BEC actors 
today. Dubbed payroll diversion scams, threat actors target Human Resources departments that have financial authority to change 
the financial records of employees. While attackers made a shift in mid 2014 to target enterprises and corporations, these attacks 
largely go unreported due to the same stigmas and lower losses as gift card scams. We continued to track wave after wave of 
payroll diversion attacks through our Cofense Reporter™ submissions from customers, meaning these attacks are still successfully 
bypassing email gateways. 

> Are you in the office? I need to update my direct deposit. Can I provide a voided check?

> BEC THREAT TECHNIQUE

SECTION 1
2023 Cofense Annual State of Email Security Report  •  8

**FIGURE 7: BEC DOMAINS**

*A pie chart showing the distribution of BEC domains. The largest slice, at 81%, is "Free", followed by "ISP" at 14%, "Mobile" at 3%, and "Spoof" at 2%.*

#### Law Enforcement’s Takedown of Cybercrime

Although BEC, ransomware, and other cybercrime operations carried on through 2022, our research indicated that threat actors 
felt pressure from the arrests as law enforcement agencies worldwide made significant strides combating cyber threat actors. 
Authorities arrested individuals suspected of involvement in the LockBit ransomware and JabberZeus banking trojan operations. 
The FBI infiltrated the Hive ransomware group starting in July, ultimately leading to the takedown of the entire operation in January 
2023. Authorities in several countries arrested dozens of suspected BEC perpetrators,