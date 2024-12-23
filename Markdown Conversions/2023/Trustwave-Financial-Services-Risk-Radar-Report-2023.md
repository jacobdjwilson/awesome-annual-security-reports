# 2023 Financial Services Sector Threat Landscape
## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Artificial Intelligence and Generative AI](#artificial-intelligence-and-generative-ai)
- [Ransomware Groups Targeting Financial Services](#ransomware-groups-targeting-financial-services)
- [Supplier and Third-Party Risk](#supplier-and-third-party-risk)
- [Dissecting the Attack Flow for Financial Services](#dissecting-the-attack-flow-for-financial-services)
- [Attack Flow Overview](#attack-flow-overview)
- [Attack Flow Steps](#attack-flow-steps)
- [Initial Foothold: Phishing and Business Email Compromise (BEC)](#initial-foothold-phishing-and-business-email-compromise-bec)
- [Initial Foothold: Logging in](#initial-foothold-logging-in)
- [Initial Foothold: Vulnerability Exploitation](#initial-foothold-vulnerability-exploitation)
- [Initial Foothold: Supply Chain](#initial-foothold-supply-chain)
- [Initial Payload](#initial-payload)
- [Expansion / Pivoting](#expansion--pivoting)
- [Malware: Infostealers](#malware-infostealers)
- [Malware: RATs](#malware-rats)
- [Malware: Ransomware](#malware-ransomware)
- [Exfiltration / Post Compromise](#exfiltration--post-compromise)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)
- [Appendix/Reference](#appendixreference)
- [Threat Groups](#threat-groups)
- [8BASE](#8base)
- [BlackCat/ALPHV](#blackcatalphv)
- [Black Basta](#black-basta)
- [Clop](#clop)
- [Medusa](#medusa)
- [LockBit](#lockbit)
- [Play](#play)
- [Royal](#royal)

T R U S T W A V E  T H R E A T  I N T E L L I G E N C E 
B R I E F I N G  A N D  M I T I G A T I O N  S T R A T E G I E S 

2023 Financial Services Sector Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies

OCTOBER 2023

## Executive Summary
When questioned about why he robbed banks, Willie 
Sutton famously responded, "Because that's where the 
money is." Some things never change, and threat actors 
are similarly drawn to the financial services sector for 
the substantial financial rewards they offer.

Financial services organizations are attractive targets because of the 
elevated potential for monetary gain. Serving as repositories of wealth, this 
sector is rich with lucrative opportunities for cybercriminals, who exploit them 
for financial gains through extortion, theft, and fraud.

In addition to the money itself, the financial services sector stores large 
volumes of sensitive data, including customer information, financial records, 
and intellectual property. 

Trailing only behind the healthcare industry, the financial services sector 
ranks second in terms of the cost of a data breach. In 2023, the average cost 
of a data breach in the financial services sector amounted to $5.9 million, 
compared to the industry average of $4.4 million, according to data from the 
Ponemon Institute.

In March 2023, Melbourne-based Latitude Financial had more than 
14 million records compromised when a threat actor stole an employee’s login 
credentials. In June 2022, one of the largest financial providers in the U.S., 
Flagstar Bank, suffered a massive data breach, leaking the Social Security 
numbers of almost 1.5 million customers – their second cybersecurity incident 
in two years.

$5.9M
vs
$4.4M 
AVERAGE COST OF 
A DATA BREACH IN 
FINANCIAL SERVICES 
COMPARED TO ALL 
OTHER INDUSTRIES

There are a number of factors that make the financial services industry 
especially vulnerable to cyberattacks, including:
	
- **Sensitive Data**: The financial services industry holds a vast amount of 
sensitive customer data, including names, addresses, Social Security 
numbers, bank account numbers, and credit card numbers, making the 
sector a high-value target. Organizations must be vigilant and inventory 
where this data resides. It’s impossible to protect something without 
knowing where it is.  
	
- **Heavily Regulated**: Heightened regulation is a double-edged sword. While 
it incentivizes increased protections, it can also make it complex and 
expensive for financial institutions to implement and maintain effective 
cybersecurity programs. 
	
- **Trust as Currency**: Consumers anchor their financial decisions on trust. If 
trust is eroded by the compromise of personal data or account information, 
customers can and will take their money elsewhere. This means they are 
a prime target for cyber criminals who will try to exploit this dependency 
on trust.
	
- **Partnership Complexity**: As a byproduct of strict regulations, it can be 
difficult for financial institutions to partner with vendors or incorporate 
tools that could improve their security posture. There are unique 
barriers and requirements for partners, adding complexity to an already 
complicated landscape. 
	
- **Interconnectedness**: In addition to business partners, the financial 
services industry is heavily interconnected with other service vendors and 
financial entities, such as merchants and payment processors, opening it 
up to supply chain and third-party risk. 

With more than 250 security researchers across the globe, the Trustwave 
SpiderLabs team puts its resources to task in looking into what leads to these 
breaches. We are uniquely positioned to do so, as we perform over 100,000 
hours of penetration tests and uncover tens of thousands of vulnerabilities 
annually. We also have a dedicated email security team analyzing millions 
of phishing URLs validated daily, including 4,000 to 8,000 per day that are 
uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec 
disciplines, including Continuous Threat Hunting, Forensics and Incident 
Response, Malware Reversal, and Database Security, give us insight into 
identifying how these breaches occur as well as mitigations and controls that 
your organization can put in place to prevent these compromises.

This report will examine the multitude of threats that pose challenges to 
the financial services industry. It will also provide recommendations for how 
financial institutions can mitigate these risks and protect their customers 
and data.

We will begin by highlighting the significant trends currently affecting the 
industry: Generative AI, ransomware, and third-party risk. Subsequently, we 
will analyze the attack flow specific to the financial services sector, offering 
insight on specific threat actors, actionable intelligence, and recommended 
mitigations for each stage to illustrate how organizations can proactively 
identify and prevent attacks to avoid lasting impact.

In this report, we will examine many of the most prevalent threat tactics and 
threat actors operating across financial services and throughout the attack 
chain, including:

THREAT ACTORS 
	
- Clop
	
- LockBit
	
- Alphv / BlackCat
	
- Black Basta
	
- 8BASE
	
- Royal
	
- Play
	
- Medusa 

THREAT TACTICS 
	
- Email-Borne Malicious 
Attachments (Downloaders, 
HTML Smuggling) 
	
- Phishing (IPFS, Google/Cloudflare 
Services, RPMSG)
	
- BEC (Payroll Diversion, 
Contact Request)
	
- Vulnerability Exploitation
	
- Credential Access (Brute Forcing, 
Abuse of Valid Accounts)
	
- Malware 
(Infostealers, Ransomware) 

For additional information about the most prevalent threat actors, please go 
to the Appendix. 

On top of everything financial services organizations must do to keep 
their perimeters and infrastructure safe, consumer protection is also 
a key component of their threat model. But with that said, it is not 
uncommon for our researchers to encounter consumer account logins 
and information being sold in underground marketplaces. This could 
lead to significant financial loss for the consumer and reputational 
impact to the financial services organization.

![Sample of stolen bank account logins being sold in underground marketplaces]

Security leaders are responsible for implementing safeguards to 
ensure customer safety. Some of the key recommendations and 
mitigations are:
	
- **Consumer Security Education**: Inform customers about the 
dangers associated with phishing and malware threats including 
education on recognizing phishing attempts and safe online 
practices.
	
- **Implementing Security Controls**: Implement robust security 
measures to safeguard customer accounts such as encryption, 
multi-factor authentication (MFA), human identification, 
penetration testing for consumer facing apps, and intrusion 
detection systems.
	
- **Customer Support and Incident Response**: Provide a support 
mechanism to customers when a security incident occurs 
including assisting customers in changing passwords, securing 
compromised accounts, and providing guidance on reinforcing 
their personal security practices. 

## Emerging and Prominent Trends

## Artificial Intelligence and Generative AI
The Threat
Generative AI and Large Language Models (LLMs) have taken the world by 
storm. While AI isn’t new, the advances made in Generative AI and LLMs 
are setting new benchmarks for what’s possible for financial services 
organizations, adversaries, and defenders. 

For financial services, the nature of the data, from credit card information to 
Social Security numbers, heightens the risks of data potentially being leaked 
to these tools.

Moreover, financial organizations face an increased risk of exposure due to 
their reliance on third-party vendors who may incorporate Generative AI or 
LLMs into their products, raising concerns about the potential loss of control 
over customer data used for training these models.

While the potential benefits of these tools could be substantial, the security 
of these systems has yet to be proven. Therefore, it is essential to adopt a 
risk-benefit approach and carefully consider the implications with the CISO 
leading the way.

What Trustwave SpiderLabs Is Seeing
Trustwave SpiderLabs consistently finds that phishing is one of the most 
effective methods attackers use to gain an initial foothold in financial services 
organizations. However, this method is highly dependent on the quality of 
the lure, the writing style, and the contextual and grammatical clues given in 
the phishing email. These issues have often been the weakness of phishing 
attacks, particularly as security awareness training has continually taught 
personnel what to look for. 

But now comes the advent of Generative AI and LLMs. The quick maturity 
and expanded use of LLM technology makes the crafting of phishing emails 
even easier, more compelling, highly personalized, and harder to detect. 
Our team regularly encounters and analyzes phishing emails with malicious 
attachments or links against our financial services clients. We see that as 
LLM technology progresses, creating these compelling phishing emails will 
likely be made easier and effective as an attack vector. We’re also seeing an 
increase in deepfakes as a result of more sophisticated technology.

Lately, we have seen the emergence of LLMs like WormGPT and FraudGPT 
on underground forums, highlighting the potential cybersecurity risks posed 
by their criminal use. WormGPT and FraudGPT can craft convincing phishing 
emails without many of the red flags that we teach users to identify phishing 
emails by including items like picking out misspellings, grammar mistakes, 
and general clumsiness of writing that may indicate that the author is not a 
native speaker.

Trustwave continually monitors the progress and attacker implementation 
of Generative AI and LLMs. Based on observations to date, Trustwave 
sees the primary areas of concern as the increased speed and quality that 
phishing emails can be drafted and exploit code can be enhanced. These 
advancements will require security vendors to adjust their detection and 
response capabilities accordingly.

ARTIFICIAL 
INTELLIGENCE AND 
GENERATIVE AI
Unique implications and risks 
due to the sensitive nature of 
the data potentially being shared 
with these tools, as well as 
advances in phishing.

Mitigations to Reduce Risk
	
- Evaluate your security solutions with Generative AI and LLMs 
in mind. Choose security tools or partners that can detect AI-
generated threats like advanced phishing.
	
- Create robust internal policies and employee training for proper 
data usage and data sharing to help minimize the risk of data 
breaches. 
	
- The reality of the current landscape is that Generative AI is here 
to stay. While the tools still have inherent risks, financial services 
organizations, like all entities, will need to determine how to govern 
the tools versus instituting broad-based bans.  
	
- Consider instituting an internal AI Infosec working group 
across relevant teams (like Legal, Privacy, IT, etc.) to deal with 
governance and data sharing guidelines.

## Ransomware Groups Targeting Financial Services
The Threat
According to U.S. Commodity Futures Trading Commission (CFTC) 
commissioner Christy Goldsmith Romero, “A 2022 survey of 130 global 
financial institutions found that 74% experienced at least one ransomware 
attack over the past year.”

The rising frequency of ransomware attacks within the financial services 
sector underscores the significant enhancement in adversaries' ability to 
conduct large-scale attacks. The ransomware-as-a-service model allows 
attackers to scale their operations and cause widespread impact.

Clop has been the most active ransomware group targeting banks and 
financial services, with the GoAnywhere attack in February 2023 impacting 
banks and over 10 financial institutions being named among the victims of 
the MOVEit attack, including Deutsche Bank, ING Bank, Charles Schwab, 
TD Ameritrade, among others. 

What Trustwave SpiderLabs Is Seeing
Trustwave SpiderLabs has seen a continuing rise in ransomware incidents 
directly targeting the financial services sector. Clop, LockBit, and Alphv/
BlackCat remain the predominant groups operating in this sector.

Just in the previous quarter, notable banks such as Latitude Financial, 
1st Source Corp, Pacific Premier Bancorp, M&T Bank, MidFirst Bank, and 
European Investment Bank were hit with various types of cyberattacks, 
potentially exposing millions of customer records. 

![Screenshot of the Lockbit Leak site claiming to have data from a breach of Banco De Venezuela]

74% 
OF 130 GLOBAL 
FINANCIAL INSTITUTIONS 
EXPERIENCED AT 
LEAST ONE 
RANSOMWARE ATTACK 
OVER THE PAST YEAR

Trustwave SpiderLabs' review of the Dark Web leaks sites of these 
ransomware gangs shows a multitude of financial services organizations 
already falling victim to various threat groups. In many cases, the data 
stolen has already been posted and made available publicly for other threat 
actors to leverage and exploit. The victims can also become prey for double-
extortion tactics, when ransomware groups not only encrypt a victim's data, 
but also threaten to expose it publicly unless a ransom is paid.

The increasing sophistication of ransomware attacks and the monetary 
incentive they present to threat actors make it more difficult for financial 
services providers to defend against such attacks. But the Trustwave 
SpiderLabs teams see a steady maturation of security controls in this sector 
to help address ransomware. Even so, there are many challenges that the 
financial services sector still faces, such as maintaining proper asset and 
data inventories, enforcing basic security hygiene, managing the risk of 
insider threats, and ensuring that personnel remain cognizant of phishing and 
social engineering attacks. 

Mitigations to Reduce Risk
	
- Remember, the best defense is a good offense. The subsequent 
sections will dive into each of these further but regularly train and 
test employees, ensure policies and patches are up to date, and 
deploy layered email security to help detect and cleanse malicious 
emails.
	
- Regularly backing up your data can help ensure the ability to 
recover from a ransomware attack or other types of data loss. Be 
sure to store backups offsite and verify that they can be restored.  
	
- Ransomware and other malware gangs target Remote Desktop 
Protocol (RDP), the Microsoft protocol that allows users to execute 
remote operations on other computers. Secure exposed RDP 
services, patch known vulnerabilities, and/or disable them if not 
necessary.

Trustwave's database 
security DbProtect delivers 
7x more database-specific 
security and compliance 
checks vs. vulnerability 
assessment tools.

## Supplier and Third-Party Risk
The Threat
The financial services industry is heavily interconnected with other 
businesses and with other financial entities, such as merchants and payment 
processors, opening it up to supply chain and third-party risk.

Unfortunately, cybercriminals often target these third parties as a strategic 
maneuver – if they successfully breach a third-party vendor, they can gain 
access to the targeted company's data. This poses a significant threat to 
financial services organizations since many of these vendors lack robust 
cybersecurity measures and data breach protection. 

Additionally, financial services organizations are subject to a wide range of 
regulations. If a third-party fails to comply with these regulations, it could put 
the financial services organization at risk of fines, penalties, or even criminal 
prosecution.

What Trustwave SpiderLabs Is Seeing
Trustwave SpiderLabs has seen a sharp rise in successful attacks due to 
third-party software and services, including high-profile, supplier-based 
attack vectors like SolarWinds, 3CX, and just recently, MOVEit. These attacks 
can be considered a flanking maneuver because they target the “weak side” 
of an organization. Through this approach, attackers can access the targeted 
company’s data and infrastructure even though the company itself may have 
a relatively high security maturity.

The financial services sector is not immune to this threat, and it may exhibit 
a higher exposure to this issue due to the interconnected nature of its 
business. The industry’s infrastructure also depends on third-party code, 
APIs, vendors, support providers, and other managed services.

To put this in perspective, Clop, currently one of the most prevalent 
ransomware groups, has been heavily associated with a recent massive 
campaign targeting an SQLi zero-day vulnerability in MOVEit, the widely used 
third-party file transfer software. We have seen hundreds of organizations 
impacted by this vulnerability, leading to successful breaches. Notable 
financial services organizations have already publicly reported being 
affected, including large, well-funded institutions like Deutsche Bank, 
ING Bank, Charles Schwab, TD Ameritrade, among others.

While this isn’t a unique threat to financial services alone, since almost 
everything is connected in one way or another, the issue is exacerbated. 
The ability to purchase a trinket from a small shop in Southeast Asia using 
a mobile app or move millions of dollars across countries highlights how 
broadly connected and complex the sector is. One weak link in the chain can 
lead to grave consequences for the organization.

Mitigations to Reduce Risk
	
- Financial services organizations must ensure their own systems 
and those belonging to third-party partners are secure and 
protected by the latest security measures. This can be achieved 
through regular penetration tests and vulnerability scans.
	
- Maintain an inventory management system for all software, 
including vendor-developed software components, operating 
systems, version and model numbers.
	
- Implement a routine vulnerability scan before installing any new 
applications, devices, or technology onto the IT environment.

## Dissecting the Attack Flow for Financial Services

## Attack Flow Overview
While the details of every breach and compromise may vary, there is a 
specific attack flow that typically occurs from the initial security bypass 
to escalation, compromise, followed by persistent home on your network 
and exfiltration and/or destruction of valuable data. The following analysis 
presents an overview of the attack flow specific to the financial services 
sector, incorporating insights from the Trustwave SpiderLabs team and 
offering actionable mitigations for organizations to implement. 

At each stage of the attack flow, the recommended mitigations provide 
proactive guidance to minimize the potential risks of financial, reputational, 
regulatory, or physical impacts to a financial services organization. The 
typical sequence of events unfolds as follows:

## Attack Flow Steps
### Initial Foothold
This step is when the attacker successfully triggers a security bypass that 
gives them the ability to expand their access to suit their motives and goals. 
This initial foothold can take various forms, ranging from successful phishing 
attacks to vulnerability exploitation or even logging into public-facing 
systems using previously acquired credentials.

In this section, we will explore the most common methods attackers use 
to gain an initial foothold in financial services, like phishing, abuse of 
valid accounts, and exploitation of vulnerabilities.

### Initial Payload
Once the attackers have established a foothold on the network, they will 
proceed to download more sophisticated tools and malware.

In this section, we will specifically concentrate on real-world 
examples of the types of payloads that frequently target financial 
services organizations. 

Initial Foothold
Initial Payload
Expansion
/ Pivoting
Malware
Exfiltration /
Post Compromise

### Expansion / Pivoting
The initial foothold typically involves a low-value workstation, such as a 
phishing victim's laptop, or a network appliance like a VPN endpoint. 
In this section, we will showcase how once armed with the 
necessary tools, attackers can target higher-value accounts and 
systems, such as Domain Admins, root accounts, Active Directory 
Systems, and Database servers.

### Malware
There are a wide variety of malware types with a myriad of uses. We’re 
talking about remote access toolkits (RATs), infostealers, ransomware, and 
many others. 
In this section, we will focus on the types of malware that are 
prevalent in financial services.

### Exfiltration / Post Compromise
In most cases, the primary motive behind compromises is data theft. 
In this section, we will explore the types of data that are targeted 
and exfiltrated in financial services-related compromises. 
Additionally, we will present real-world examples of financial services 
data breaches to provide concrete illustrations.

## Initial Foothold: Phishing and Business Email Compromise (BEC)
The Threat
Phishing and email-borne malware stand out as the most commonly 
exploited methods for gaining an initial foothold in an organization. Instead 
of attempting to exploit the software or systems on the network, attackers 
direct their focus towards targeting the individuals operating the keyboard.

Using a persuasive and time-sensitive email, the attacker successfully 
convinces their victim to take specific actions, such as opening an 
attachment, clicking on an embedded URL, or following instructions to 
transfer funds to a purported "stranded CEO."

TYPICAL PHISHING GOALS: 
	
- **Credential theft example**: Invoice from a customer includes a link. When 
the link is clicked, it prompts the user for their password before “access is 
granted to the document”
	
- **Malware insertion**: Via PowerShell scripts, Javascript, Macros
	
- **Triggering action example**: Wire transfer for “stranded CEO” (BEC)

Trustwave SpiderLabs Insights
The Trustwave SpiderLabs team is dedicated to monitoring email-based threats 
including opportunistic phishing, targeted/spear-phishing, and BEC. Over the last 
year, our team has observed interesting developments in the delivery methods, 
techniques, themes, and even targeted brands of email-based attacks in 
financial services. We believe that these developments have contributed to the 
continuing relevance and effectiveness of these types of attacks.

Based on the data from our financial services client base, we observed 
that HTML attachments are the most common malicious attachments in 
emails. These HTML attachments make up 78% of all malicious attachments 
seen, and are mainly used for credential phishing, redirectors, and 
HTML smuggling. It is also notable that 33% of these HTML files employ 
obfuscation as a means of defense evasion. 

HTML smuggling is a technique used to sneak in malicious files onto the target’s 
system. The malicious file is encrypted and embedded into the HTML attachment. 
Once the HTML is opened with a browser, the blob will be automatically decoded and 
dropped on the system 

![Spam email with HTML attachment]
![User Action Required]
![Password-protected archive]
![Opens]
![HTML containing an encrypted blob]
![Archive]
![LNK]
![Shortcut file]
![Clicks]
![Opens]
![Contains]
![Qakbot DLL]
![Launches]

Prevalence of email malware attachments
Aside from HTML, our team has observed executables as the next most 
prevalent type of malicious attachment. Commonly spotted attachments are 
mostly information stealing malware such as Gootloader, XLoader, Lokibot, 
Formbook, and Snake Keylogger. We have also seen Agent Tesla (RAT) in our 
current data set. We will discuss these individually in the malware section of 
this report. 

To a lesser degree, attackers use PDFs, Excel, and Word documents. PDFs 
typically serve as redirectors and a mechanism to download malware such as 
Qabot. Similarly, attackers use Word and Excel documents in the same way 
but with noticeable use of MS Office exploits like CVE-2017-1182 and CVE-
2017-0199. It is worth noting that the prevalence of Qabot has decreased 
dramatically due to the recent takedown by the U.S. Justice Department.

Our team noted the most common themes of the emails containing these 
malicious attachments are related to voicemail notifications, payment 
receipts, purchase orders, remittances, bank deposits, and quotation 
requests. 

![Word cloud based on the subject lines for emails with malicious attachments]

HTML
Executable
PDF
Excel
Word Document
Other (Shortcut,
OneNote)
78%
14%
3%
2%
1%
2%

remittance
remittance
advice
confirmation
action
direct
deposit
statement
receipt
approved
benefits
enrollment
completed
information
missed
purchase
listen
review
shipment
processed
shared
advice
notice

We have also observed that 24% of the emails with malicious attachments 
attempted to spoof American Express. DHL is next at 21% and Microsoft in 
third with 15%. 

![Top spoofed brands in emails with malicious attachments]

From a purely phishing standpoint (those without malicious attachments), 
the most prevalent phishing themes are “Urgent Action” themes, mailbox-
related alerts, document sharing, e-signing, account-related alerts, 
missed communications, meeting-related notifications, and 
payment/invoice-related alerts.

![Wordcloud based on the subject lines for phishing emails (no malicious attachments)]

American Express
DHL
Microsoft
DocuSign
RingCentral
USAA
DropBox
FedEx
Chase
Wells Fargo
HSBC
Others
24%
21%
15%
11%
8%
5%
4%
3%
2%
2%
1%
4%

action
required
email
password
incoming
messages
received
new
password
expired
pending
messages
incoming
emails
new
document
message
email
email
received
new
message
new
message
messages
pending
voice
message
document
shared
password
expiration
password
email
email
account
mails
blocked
new
voice
mail
box

The brands most spoofed in phishing attacks are Microsoft at 52%, DocuSign 
at 10%, and American Express at 8%. 

![Top impersonated brands in phishing emails]

Though phishing as an attack vector remains the same, techniques have 
continually evolved in order to stay ahead of email defenses. During the past 
year, we have discovered and have subsequently conducted analysis on new 
techniques in phishing that attackers actively use in the financial services 
sector:
	
- IPFS-based Phishing
	
- Cloudflare Pages.dev and Workers.dev Phishing
	
- RPMSG Campaigns

For more information, we have linked each of these techniques to their 
individual in-depth studies on the Trustwave SpiderLabs blogs. 

Finally, on the BEC front, we have observed that “Payroll Diversion” at 48% is 
still the most used lure with “Request for Contact” and “Task” at 23% and 13% 
respectively. 

![Lures used in BEC messages]

Microsoft
DocuSign
American Express
WeTransfer
DHL
Wells Fargo
Chase
Others
52%
10%
8%
7%
5%
4%
2%
12%

13% Task
43% Payroll Diversion
2% Gift Purchase
23% Request for Contact
10% Availability
2% Wire Transfer
2% Invoice Transaction

Additionally, Trustwave SpiderLabs has been monitoring the effect of AI and 
LLMs like ChatGPT on phishing attacks. Many of the red flags that we teach 
users to identify phishing emails, such as misspellings, grammar mistakes, 
and general clumsiness of writing, may indicate that the author is not a 
native speaker. 

The quick maturity and expanded use of LLM technology makes crafting 
these emails easier, more compelling, highly personalized, and harder to 
detect. Trustwave SpiderLabs has uncovered multiple spearphishing attacks 
with malicious attachments or links being used against financial services 
entities. Creating these targeted, compelling spearphishing emails will likely 
be easier for attackers with LLM technology.

Lately, we have noted the emergence of LLMs like WormGPT and FraudGPT 
on underground forums, highlighting the potential cybersecurity risks posed 
by their criminal use. WormGPT's and FraudGPTs capabilities include not 
only crafting convincing phishing emails, but even assisting in creating 
undetectable malware, writing malicious code, and finding vulnerabilities. 
More details can be found in the recent Trustwave SpiderLabs blog here.
 
Mitigations to Reduce Risk
	
- Consistently conduct mock phishing tests to assess the 
effectiveness of anti-phishing training and retrain repeat offenders.
	
- Implement robust anti-spoofing measures, including deploying 
technologies on email gateways.
	
- Deploy layered email scanning with a solution like MailMarshal to 
provide better detection and protection.
	
- Utilize techniques to detect domain misspellings, enabling the 
identification of phishing and BEC attacks.

When layered, captures up 
to 90% of malicious emails 
missed by other email 
security vendors.

## Initial Foothold: Logging in
The Threat
Sometimes, attackers can gain access to a network by simply logging in. 
This access can occur if the default credentials for a device have not been 
changed, weak passwords are used making them vulnerable to brute-forcing, 
or if credentials have been purchased from an underground forum. Beyond 
simple credentials, attackers can purchase access to a webshell or active 
sessions already in place in a target organization.

Trustwave SpiderLabs Insights
The Trustwave SpiderLabs team performs proactive threat hunts and analysis 
in our client’s environment to identify breaches or compromises that have yet 
to be identified. In the course of these engagements, the team regularly finds 
the following issues that directly contribute to this threat.

ABUSE OF VALID ACCOUNTS
The use of valid accounts continues to be one of the easiest and most 
efficient ways for a threat actor to get an initial foothold into a financial 
services organization. Various types of phishing attacks and poor 
cybersecurity hygiene are largely responsible for these successes. In fact, 
as discussed in the previous section, phishing is often the first stage for 
obtaining valid credentials or is used as a redirector to install infostealers. 
This malware then steals valid credentials from the target. Poor cybersecurity 
hygiene, on the other hand, refers to poor credential and password 
management that we will further discuss in the next item.

CREDENTIAL ACCESS 
Attackers use credential access about 20% of the time for all reported 
incidents in our client base. Brute-force attacks, in particular, make up the 
majority of the observations. This tactic has threat actors leveraging valid 
accounts to compromise systems by simply logging in using weak passwords 
that are vulnerable to password guessing. 

When our teams carry out penetration testing in financial services, one 
of the common areas of vulnerability identification is weaknesses related 
to password hygiene. The Trustwave SpiderLabs offensive security team 
will often find unchanged default credentials in use within an environment 
including administrative and high privileged accounts with passwords older 
than one year. We also noted issues stemming from shared passwords across 
administrative and non-administrative accounts. While not exclusive to 
financial services, these types of findings are also being used by actors and 
malware to further access. 

Another issue often encountered by Trustwave SpiderLabs are unsecured 
files containing credentials, as well as scripts or custom applications passing 
credentials in cleartext in environments. If a malicious actor can gain access 
to these unsecured files or sniff the password from these applications, they 
will have gained the foothold they are looking for. 

Initial Foothold
Expansion
/ Pivoting
Malware
Exfiltration /
Post Compromise
Initial Payload
Threat Actor
VPN Acess Point

In our threat hunts, typical unsecured credentials were often found in 
plaintext documents with easily identifiable and obvious names such as 
“Username and Passwords,” “Bank Keys Passwords,” and “SFTP Passwords,” 
among others. We also observed that passwords were stored and sent in 
clear text through various applications and configuration files such as custom 
PowerShell Scripts. 

INFOSTEALERS
As the name suggests, infostealers focus on that exact activity as its primary 
function. The stolen information is then typically offered up for sale. 
Our data indicates that most executables attached in email-based attacks 
in this sector are infostealers. Notable infostealers that we have observed 
are XLoader, Lokibot Formbook, and Snake Keylogger. Each of these will be 
further discussed in subsequent sections. 

It is worth noting that the prevalent use of infostealers has helped create 
an online supply of ready to use login credentials that can be purchased via 
underground forums and the Dark Web.

Top tactics not detected by security technologies
In our Threat Hunts, we uncover things that aren’t alerted by security 
technologies. These are the top tactics in financial services compared to 
other industries.

![Top tactics not detected by security technologies]

0%
10%
20%
30%
40%
Initial Access
Credential Access
Execution
Command & Control
Discovery
37%
23%
17%
6%
5%
45%
19%
12%
7%
6%
Cross Industry
Financial Services

Mitigations to Reduce Risk
	
- Regularly rotate passwords (e.g., every quarter) to mitigate issues 
related to valid accounts.
	
- Implement password complexity requirements to enhance security.
	
- Enable multi-factor authentication (MFA) to provide an additional 
layer of protection for accounts.
	
- Securely store credentials in programs in Password Vaults or 
Password Management Systems to prevent credential abuse.
	
- Encrypt credentials when used in scripts to safeguard sensitive 
information.
	
- Audit local administrative accounts regularly and obfuscate admin 
accounts by not using admin in the name.
	
- Use LAPS on Windows systems to manage local accounts.
	
- Implement Privileged Access Management (PAM) and Privileged 
Identity Management (PIM) solutions to deepen defense in depth 
strategy.

## Initial Foothold: Vulnerability Exploitation
The Threat
Exploiting vulnerabilities is often the first thing people think of when it comes 
to information security.  This topic encompasses discussions on zero days, 
patch agility, proof-of-concept exploits, and vulnerability disclosure.

Simply put, a vulnerability refers to a bug in software that introduces 
security risks. Attackers develop specialized software or scripts to exploit 
the vulnerability and circumvent security controls, such as authorization, 
authentication,