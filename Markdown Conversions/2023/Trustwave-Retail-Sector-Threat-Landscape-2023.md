# 2023 Retail Threat Landscape

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
- [Artificial Intelligence and Generative AI](#artificial-intelligence-and-generative-ai)
- [Automated Bot Attacks in Retail](#automated-bot-attacks-in-retail)
- [Third-Party Risk and Exposure](#third-party-risk-and-exposure)
- [Dissecting the Attack Flow for Retail](#dissecting-the-attack-flow-for-retail)
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
- [Consumer Attacks in Retail](#consumer-attacks-in-retail)
- [Bot Attacks in Retail](#bot-attacks-in-retail)
- [Dark Web Fraud and Scams in Retail](#dark-web-fraud-and-scams-in-retail)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)
- [Appendix/Reference](#appendixreference)
- [Threat Groups](#threat-groups)
- [8BASE](#8base)
- [Bian Lian](#bian-lian)
- [BlackCat/ALPHV](#blackcatalphv)
- [Clop](#clop)
- [LockBit](#lockbit)
- [Play](#play)
- [RansomedVC](#ransomedvc)
- [Royal](#royal)

NOVEMBER 2023

## Executive Summary
In the fiercely competitive realm of retail, companies invest significant resources to earn a coveted spot in consumers' minds as household names. The allure of brand recognition is undeniable, but it also presents a stark reality in the realm of cybersecurity: the bigger the brand, the larger the target.

Adding to the complexity, the online retail, or e-commerce, market surpassed a staggering $1.09 trillion in 2022, marking a 209% increase from the levels of 2019, according to Comscore.

Retailers today are facing a barrage of mounting cybersecurity challenges. Unlike security incidents affecting businesses in less-publicized sectors, a breach involving a major retailer is almost guaranteed to become a headline-grabbing affair. While the average cost of a breach in the retail sector ($2.9 million) is lower than the industry average ($4.4 million), the extensive public awareness of these retail giants, coupled with the loyal customer base they command, can amplify the reputational consequences of any breach.

During January 2023, malicious actors successfully obtained the personal information of 10 million customers from the records of a UK-based sports retailer. This security breach raised significant concerns regarding data management practices, given that the compromised database held millions of transaction records dating back up to four years.

In September 2021, a high-end retailer alerted 4.6 million customers to a security incident in which a hacker had breached online accounts in May 2020. This unauthorized access resulted in the compromise of sensitive personal information, including usernames, passwords, customer names, contact details, credit card numbers, as well as their expiration dates and virtual card numbers.

There are a number of factors that make retailers especially vulnerable to cyberattacks, including:

- **Rise of E-commerce:** The shift to e-commerce has made retailers more vulnerable to cyberattacks in a number of ways. First, e-commerce retailers store a large amount of sensitive customer data, such as credit card numbers and shipping addresses. Second, e-commerce retailers often rely on third-party vendors, which we’ll detail later, for services such as web hosting and payment processing. These third-party vendors can be a security risk if they are not properly vetted and monitored. Additionally, e-commerce opens the risk of automated bot attacks and digital skimming, among other threats.

- **Seasonality:** Retail businesses experience significant fluctuations in traffic and sales throughout the year. This seasonality can make it difficult to maintain security and compliance standards. For example, during the holiday season, retailers may hire temporary employees and increase their online sales. This influx of new activity can create opportunities for cybercriminals to exploit vulnerabilities in the retailer's systems and networks.

$2.9M vs $4.4M AVERAGE COST OF A DATA BREACH IN THE RETAIL SECTOR COMPARED TO ALL OTHER INDUSTRIES

- **Omnichannel:** Retailers today typically operate across multiple channels, including physical stores, e-commerce websites, and mobile apps. This omnichannel approach provides convenience for customers, but it also complicates security. Retailers need to ensure that their systems are integrated and secure across all channels. If there is a vulnerability in one channel, it could be exploited to gain access to data in other channels.

- **Prevalence of Gift Cards:** While gift cards have increasingly become the go-to present during the holiday season, they have also become the tool of choice for threat actors. Threat actors utilize gift cards to maintain anonymity in their transactions and, more alarmingly, to launder funds sourced from compromised credit cards and other payment platforms. The approach often involves acquiring high-value gift cards using stolen financial credentials, which are later used or sold for a profit.

- **Franchise Model:** Franchises pose a unique set of security challenges for retailers. Franchisees are independent businesses, but they are also part of a larger brand. This means that a security breach at one franchise could damage the reputation of the entire brand. Additionally, franchisees may not have the same level of security resources as the parent company, making them more vulnerable to cyberattacks.

With more than 250 security researchers across the globe, the Trustwave SpiderLabs team puts its resources to task to investigate what leads to these breaches. We are uniquely positioned to do so, as we perform over 100,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 4,000 to 10,000 per day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Continuous Threat Hunting, Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur as well as mitigations and controls that your organization can put in place to prevent these compromises.

This report will examine the multitude of threats that pose challenges to the retail industry. It will also provide recommendations for how the retail sector can mitigate these risks and protect their customers and data.

We will begin by highlighting the significant trends currently affecting the industry: Generative AI, automated bots, and third-party risk. Subsequently, we will analyze the attack flow specific to the retail sector, offering insight on specific threat actors, actionable intelligence, and recommended mitigations for each stage to illustrate how organizations can proactively identify and prevent attacks to avoid lasting impact.

In this report, we will examine many of the most prevalent threat tactics and threat actors operating across retail and throughout the attack chain, including:

THREAT ACTORS
- Royal
- Bian Lian
- LockBit
- Clop
- BlackCat/ALPHV
- Play
- 8BASE
- RansomedVC

THREAT TACTICS
- Email-Borne Malware
- Phishing
- BEC
- Vulnerability Exploitation
- Credential Access
- Access for Sale
- Malware
- Consumer-Based Attacks
- Bot Attacks
- Gift Card Fraud and Scams

For additional information about the most prevalent threat actors, please go to the Appendix.

## Emerging and Prominent Trends

## Artificial Intelligence and Generative AI
The Threat

Generative AI has taken the world by storm. While AI isn’t new, the advances made in Generative AI and Large Language Models (LLMs) are setting new benchmarks for what’s possible for retail organizations and for adversaries and defenders as well.

The retail industry is in the business of knowing its customers and their preferences. As a result, tailored and personalized marketing is a core component to stay competitive. As more business intelligence and customer analytics platforms integrate generative AI into their tools, the retail sector must vet and audit the security protections within those systems.

Additionally, social engineering attacks can become more sophisticated as LLMs have the capability to create highly personalized and targeted messages.

While the potential benefits of these tools could be substantial, the security of these systems has not yet been proven. Therefore, it is essential to adopt a risk-benefit approach and carefully consider the implications with the CISO leading the way.

Similar to other industries, using this technology also raises concerns about data privacy and security. Retail businesses need to carefully consider the risks and benefits of using generative AI before deploying it.

What Trustwave SpiderLabs Is Seeing

Trustwave SpiderLabs consistently finds that phishing is among the most effective methods attackers use to gain an initial foothold in retail organizations. However, this method is highly dependent on the quality of the lure, the writing style, and the contextual and grammatical clues given in the phishing email. These issues have often been the weakness of phishing attacks, particularly as security awareness training has continually taught personnel what to look for.

But now comes the advent of Generative AI and LLMs. The quick maturity and expanded use of LLM technology makes crafting phishing emails even easier, more compelling, highly personalized, and harder to detect. Our team regularly encounters and analyzes phishing emails with malicious attachments or links against our retail clients. We see that as LLM technology progresses, creating these compelling phishing emails will likely be made easier and effective as an attack vector. We’re also seeing an increase in deepfakes as a result of more sophisticated technology.

Lately, we have seen the emergence of LLMs like WormGPT and FraudGPT on underground forums, highlighting the potential cybersecurity risks posed by their criminal use. WormGPT and FraudGPT can craft convincing phishing emails without many of the red flags that we teach users to identify phishing emails by including items like picking out misspellings, grammar mistakes, and general clumsiness of writing that may indicate that the author is not a native speaker.

ARTIFICIAL INTELLIGENCE AND GENERATIVE AI
Unique implications and risks due to the sensitive nature of the data potentially being shared with these tools, as well as advances in phishing.

Trustwave continually monitors the progress and attacker implementation of Generative AI and LLMs. Based on observations to date, Trustwave sees the primary areas of concern as the increased speed and quality that phishing emails can be drafted and exploit code can be enhanced. These advancements will require security vendors to adjust their detection and response capabilities accordingly.

Mitigations to Reduce Risk

- Evaluate your security solutions with Generative AI and LLMs in mind. Choose security tools or partners that can detect AI-generated threats like advanced phishing.

- Create robust internal policies and employee training for proper data usage and data sharing to help minimize the risk of data breaches.

- The reality of the current landscape is that Generative AI is here to stay. While the tools still have inherent risks, retail organizations, like all entities, will need to determine how to govern the tools versus instituting broad-based bans.

- Consider instituting an internal AI Infosec working group across relevant teams (like Legal, Privacy, IT, etc.) to deal with governance and data sharing guidelines

## Automated Bot Attacks in Retail
The Threat

The rise of automated bots in the online retail landscape has ushered in new types of threats, especially during critical periods like the holiday shopping season.

These bots, often malicious in nature, pose a substantial risk to online retailers and consumers alike. Automated bots encompass a diverse range of malicious activities, including scalping, and freebie exploitation.

What Trustwave SpiderLabs Is Seeing

Our team has observed a significant increase in malicious bot traffic during the holiday shopping season which poses a threat to online retailers. These bots engage in various automated threats, including credential stuffing, account takeover, gift card cracking, web scraping, API scraping, fake account creation, and inventory scalping.

Bot attacks can potentially slow down or even disrupt online operations of retailers by simulating consumer actions, leading to an overwhelming increase in website traffic. These bots extract pricing information, exploit promotions, and carry out fraudulent transactions, impacting online retail significantly. This increased bot activity may raise operational costs, affecting website resources, marketing, technical support, and even cause financial losses through fraud.

Two specific types of malicious bots are noteworthy: Grinchbots and Freebie Bots.

GRINCHBOTS

Grinchbots are scalping bots targeting hard-to-find holiday items, causing frustration among consumers by purchasing limited stock, also called inventory hoarding. For example, in September and October 2020, there was a massive increase in malicious bot activity on retail websites worldwide. This surge of malicious bot activity occurred at the same time as the launch of new gaming consoles and the holiday shopping season. Consequently, consumers faced difficulties in buying consoles, GPUs, and CPUs because these bots had already bought up all available stock, leading to significant frustration among consumers.

FREEBIEBOTS

Freebie Bots, on the other hand, exploit errors on retail websites during the holiday season. These automated scripts allow users to purchase incorrectly priced or inaccurately described items and resell them for profit. In a study by Kasada, it was observed that in a well-known community where people share freebies, members utilized Freebie Bots to buy nearly 100,000 products within a single month. These products had a combined value of $3.4 million. Surprisingly, Freebie Bot users only spent 882 USD to acquire these goods, resulting in some individuals making monthly profits of over $100,000.

Also, during the November 2022 Black Friday and Cyber Monday weekend, Freebie Bots successfully acquired products worth $500,000 from a single retailer, with a total expenditure of $85.36 across 610 users.

In line with this, it should be noted that these Freebie Bot attacks are dependent on mispriced items. Items can become mispriced on online retail platforms due to a variety of reasons. Some common reasons are:

- **Data Entry Error** A human operator might enter incorrect data while updating the price of an item or a unit price is incorrectly calculated or entered (e.g. pricing per kilogram instead of per pound)

- **Supplier Errors** A supplier provides incorrect pricing data.

- **Promotional or Discount Errors** Discounts or promotional prices might be incorrectly applied to products.

- **Algorithmic Pricing** Some retailers use automated pricing algorithms to adjust prices. Malfunctions or poor design can lead to mispriced items.

- **Technical Glitches** Glitches could occur due to software bugs, integration errors or database errors.

- **Currency Conversion Errors** Incorrect or outdated exchange rates can result in mispriced items particularly in international sales.

- **Timing Issues** Delays in updating prices on the platform when there are changes in cost, discounts, or other pricing factors.

![Example of Freebiebots at work]

Mitigations to Reduce Risk

- Invest in DDOS and advanced filtering tools to block malicious traffic and differentiate between legitimate and malicious requests.

- Ensure you have sufficient bandwidth and autoscaling resources to handle unexpected traffic spikes, reducing the risk of a DDoS attack overwhelming your site.

- Regularly audit and update your payment processing systems to detect and fix vulnerabilities.

- Employ end-to-end encryption for all payment transactions to ensure data security.

- Avoid storing sensitive customer data like full credit card numbers; if necessary, use strong encryption and follow PCI DSS standards.

- Implement a multi-stage filtering process to differentiate between beneficial and malicious bots.

- Move beyond traditional CAPTCHA; adopt advanced rate limiting that can detect IP rotation and other evasion techniques.

- Implement cart session time limits to prevent bots from indefinitely holding merchandise.

- Use browser environment verification and mobile API hardening to differentiate between genuine shoppers and bots.

- Implement robust data entry procedures and conduct regular audits and price monitoring. Also automate with caution particularly in terms of product pricing.

- Utilize pricing management software and utilize error detection technologies when possible. Maintain protocols for corrective action to minimize harm.

## Third-Party Risk and Exposure
The Threat

The retail industry is increasingly reliant on third-party vendors for a variety of services, such as point-of-sale systems, payment processing, supply chain management, and customer relationship management.

Point of Sale (POS) systems are a prime target for cybercriminals, as they contain sensitive customer data such as credit card numbers. If a POS system is compromised, criminals could steal this data and use it to commit fraud.

Payment processors are also a target for cybercriminals, as they handle large volumes of financial transactions. If a payment processor is compromised, criminals could steal money from retail businesses or their customers.

This creates a multitude of third-party risks, as these vendors may have access to sensitive data or systems, such as customer names, addresses, credit card information, and product inventory. Retail businesses need to carefully vet their third-party vendors and implement strong security measures to mitigate this risk.

It is crucial for organizations to prioritize ensuring their suppliers adhere to stringent security measures to mitigate potential risks. It’s also important to remember that an organization is often reliant on these types of suppliers to patch and update systems, which could open them up to risk of vulnerabilities.

What Trustwave SpiderLabs Is Seeing

At its core, the retail industry is reliant on a stable and secure supply chain and third-party infrastructure to be able to maintain inventory, manage deliveries, support geographic expansion, and maintain e-commerce operations.

Cybercriminals commonly prefer to attack these third parties in a sort of flanking maneuver—if the attack succeeds, they gain access to the targeted company’s data. Perhaps more importantly, these aforementioned third parties pose a grave risk to retail organizations because of the large dependency of these organizations on third-party software and vendors for day-to-day operations. Recent supply chain headlines, like SolarWinds and 3CX, underscore the exposure third-party vendors can create for retail organizations.

To put this in perspective, Clop, currently one of the most active ransomware gangs, was heavily associated with a recent massive campaign targeting an SQLi zero-day vulnerability in a popular third party file transfer software called MOVEit. Retail organizations use MOVEit to transfer sensitive information such as payment information, inventory reports, and other sensitive and logistical data across multiple stores and offices. Notable retail organizations such as retail giants TJX and Estee Lauder have publicly reported being affected by issues concerning this third-party software.

Mitigations to Reduce Risk

- Retail organizations must ensure their own systems and those belonging to third-party partners are secure and protected by the latest security measures. This can be achieved through regular penetration tests and vulnerability scans.

- Maintain an inventory management system for all hardware and software, including vendor-developed software components, operating systems, version and model numbers.

- Implement a routine vulnerability scan before installing any new devices or technology onto the operating IT network.

## Dissecting the Attack Flow for Retail

## Attack Flow Overview
While the specifics and details of every breach and compromise may vary, there is typically a specific attack flow that occurs from the initial security bypass to escalation, compromise, followed by persistent home on your network and exfiltration and/or destruction of valuable data. The following analysis presents an overview of the attack flow specific to the retail sector, incorporating insights from the Trustwave SpiderLabs team and offering actionable mitigations for organizations to implement.

At each stage of the attack flow, the recommended mitigations provide proactive guidance to minimize the potential risks of financial, reputational, regulatory, or physical impacts to a retail organization. The typical sequence of events unfolds as follows:

## Attack Flow Steps
Initial Foothold
This is the step where the attacker successfully triggers a security bypass that will give them the ability to expand their access to suit their motives and goals. This initial foothold can take various forms, ranging from successful phishing attacks to vulnerability exploitation or even logging into public-facing systems using previously acquired credentials.

In this section, we will explore the most common methods through which attackers gain this initial foothold in the retail sector, like phishing, abuse of valid accounts and exploitation of vulnerabilities.

Initial Payload
Once the attackers have established a foothold on the network, they will proceed to download more sophisticated tools and malware.

In this section, we will specifically concentrate on real-world examples of the types of payloads that frequently target retail organizations.

Initial Foothold
Initial Payload
Expansion / Pivoting
Malware
Exfiltration / Post Compromise

Expansion / Pivoting
The initial foothold typically involves a low-value workstation, such as a phishing victim's laptop, or a network appliance like a VPN endpoint.

In this section, we will showcase how once armed with the necessary tools, attackers can target higher-value accounts and systems, such as Domain Admins, root accounts, Active Directory Systems, and Database servers.

Malware
There are a variety of malware types with a myriad of uses. We’re talking about Remote Access Toolkits (RATs), infostealers, ransomware, and many others.

In this section, we will focus on the types of malware that are prevalent in retail.

Exfiltration / Post Compromise
In most cases, the primary motive behind compromises is data theft.

In this section, we will explore the types of data that are targeted and exfiltrated in retail-related compromises. Additionally, we will present real-world examples of retail sector data breaches to provide concrete illustrations.

## Initial Foothold: Phishing and Business Email Compromise (BEC)
The Threat

Phishing and email-borne malware stand out as the most commonly exploited method for gaining an initial foothold in an organization. Instead of attempting to exploit the software or systems on the network, attackers direct their focus towards targeting the individuals operating the keyboard.

Using a persuasive and time-sensitive email, the attacker successfully convinces their victim to take specific actions, such as opening an attachment, clicking on an embedded URL, or following instructions to transfer funds to a purported "stranded CEO."

Typical phishing goals:

- **Credential theft:** Invoice from a customer includes a link. When the link is clicked it prompts the user for their password before “access is granted to the document”

- **Malware insertion:** Via PowerShell scripts, JavaScript, Macros

- **Triggering action:** Wire transfer for “stranded CEO” (BEC)

Trustwave SpiderLabs Insights

The Trustwave SpiderLabs team is dedicated to monitoring email-based threats including opportunistic phishing, targeted/spear-phishing, and BEC. Over the last year, the team has observed interesting developments in the techniques and delivery methods of email-based attacks in retail. We believe that these developments have contributed to the continuing relevance and effectiveness of these types of attacks.

Based on the data from our retail client base, we observed that over 70% of the malicious emails contain malicious HTML attachments with 30% of these being obfuscated. Our team has noted that most of these attachments include local, standalone phishing pages, redirectors, and malware. Aside from HTML, other file types included are executables, Microsoft Office documents, PDFs, and One Note files. Common malware that we found piggybacking off these attachments were Agent Tesla, Emotet, and Qakbot.

![The top malicious attachment filetypes]

Of particular note is the recent decline in the activity of Emotet and Qakbot botnets. These two botnets have previously been the predominant method used by spammers to distribute malware. Qakbot’s decline was particularly evident after a recent FBI takedown campaign against its infrastructure.

But after the Qakbot takedown, the SpiderLabs team observed campaigns using similar email structures as ones delivering Qakbot. By searching the Indicators of Compromise (IOCs) found on various malicious attachments, our team identified that similar email campaigns are now leveraging the DarkGate malware.

DarkGate is a loader that gained popularity in June 2023 when the tool was advertised in a Dark Web forum. Spam campaigns leading to this threat utilized highjacked email threads. Typically, a shortcut file (LNK) attachment or a download link to the LNK file are often the initial vector of this threat. The LNK downloader retrieves a VBS downloader which will then lead to the DarkGate malware.

![Hijacked email spam with LNK attachment leading to DarkGate malware]

Aside from email-borne malware, traditional credential phishing attacks remain a substantial threat for retailers and their employees. A common trend we have observed is that 70% of phishing links contain embedded victims’ email addresses. This is a prevalent technique used by phishers to make fraudulent websites more personal and appear more convincing. When the user clicks on the link, they are redirected to a fraudulent login page often impersonating Microsoft Outlook, where the email address field is already pre-populated on the login form.

![Phishing email about mailbox storage limit which contains a phishing link that embeds the email address of the recipient]

In phishing attacks directed towards retailers and their employees, the most prevalent impersonated brands are Microsoft and DHL.

Related to this, a particularly interesting trend is the increase of cyber-squatting or typo-squatting on the “onmicrosoft.com” domain. Note that when a company signs up for an Office 365 for Business subscription, Microsoft will create a new subdomain with this onmicrosoft.com domain for the institution. For example, “my-company.onmicrosoft.com.”

In the past year, our team has seen an uptick of new domains that were made to look like they are sent using “onmicrosoft.com.” As Microsoft is a reputable and well-known brand, threat actors use their brand name as senders to make their phishing and BEC emails appear legitimate.

![Sample email header of a malicious email leveraging typo-squatting techniques focusing on the onmicrosoft.cm domain]

In terms of phishing and BEC lures, “Payroll Diversion” is the most prevalent lure in this sector. This method sees fraudsters impersonate employees to redirect the paycheck of the impersonated employee to a fraudulent bank account. “Request for Contact” comes in second, where victims are asked for their mobile contact information. In this method, threat actors attempt to collect the victim’s phone number and then move the conversation to mobile, either via SMS or mobile chat applications, where they can directly communicate with the victim and evade the detection of security gateways.

![Breakdown of the top phishing and BEC lures]

The two most prevalent systems abused in phishing links in the retail sector are InterPlanetary File System (IPFS) and Google Services. IPFS is currently the most abused system accounting for over 30% of all identified phishing links. Phishers exploit the decentralized and resilient nature of IPFS to host malicious contents. Various Google services on the other hand, rank second most abused in over 15% of all email phishing link attempts. Services like Google Translate and Google Search are used to create links that conceal deceptive sites or malicious content, making the links appear more legitimate.

Additionally, Trustwave SpiderLabs has been monitoring the effect of AI and LLMs like ChatGPT on phishing attacks. Many of the red flags that we teach users to identify phishing emails, such as misspellings, grammar mistakes, and general clumsiness of writing, may indicate that the author is not a native speaker.

The quick maturity and expanded use of LLM technology makes crafting these emails easier, more compelling, highly personalized, and harder to detect. Trustwave SpiderLabs has uncovered multiple spearphishing attacks with malicious attachments or links being used against retailers. Creating these targeted, compelling spearphishing emails will likely be easier for attackers with LLM technology.

Lately, we have noted the emergence of LLMs like WormGPT and FraudGPT on underground forums, highlighting the potential cybersecurity risks posed by their criminal use. WormGPT's and FraudGPTs capabilities include not only crafting convincing phishing emails, but even assisting in creating undetectable malware, writing malicious code, and finding vulnerabilities. More details can be found in the recent Trustwave SpiderLabs blog here.

Mitigations to Reduce Risk

- Consistently conduct mock phishing tests to assess the effectiveness of anti-phishing training and retrain repeat offenders.

- Implement robust anti-spoofing measures, including deploying technologies on email gateways.

- Deploy layered email scanning with a solution like Trustwave MailMarshal to provide better detection and protection.

- Utilize techniques to detect domain misspellings, enabling the identification of phishing and BEC attacks.

When layered, captures up to 90% of malicious emails missed by other email security vendors.

## Initial Foothold: Logging in
The Threat

Sometimes attackers gain access to your network simply by logging in. This can occur if the default credentials for a device have not been changed, if weak passwords are used and vulnerable to brute-forcing, or if credentials have been purchased from an underground forum. Beyond simple credentials, attackers can purchase access to a webshell or active sessions already in place in a target organization.

Trustwave SpiderLabs Insights

The Trustwave SpiderLabs team performs proactive threat hunts in our client’s environment to identify breaches or compromises that have yet to be identified. In the course of these engagements, the team regularly finds the following issues that directly contribute to this threat.

CREDENTIAL ACCESS

Credential Access accounts for 30% of all tactics for reported incidents in our retail client base. Generic brute-force attacks make up the majority of the observations. This tactic has threat actors leveraging valid accounts to compromise systems by simply logging in using weak passwords that are vulnerable to password guessing.

![Credential Access techniques used by attackers]

In our threat hunts, we commonly find exposed passwords from custom batch files and scripts used for report automation in our retail client base. We also discover instances of potential credential exposure with the usage of SFTP with many of the applications used for this activity exposing passwords in command lines.

INITIAL ACCESS BROKERS

Initial access brokers are individuals or groups with expertise and resources in providing initial entry points to an organization. These brokers employ a range of techniques to get that initial access from phishing, exploits, or various forms of social engineering. Once they have successfully gained and persisted in this access, they typically sell these access other malicious actors, who can then carry out more advanced stages of an attack.

Through our Dark Web research and monitoring, our team has found a multitude of initial access entry points for various retailers around the world being sold by these brokers. Here are some of the notable types of access these groups are selling:

- Remote Desktop Protocol (RDP) Accounts are the most prevalent types of initial access being sold targeting retail organizations. They comprise 34% of the type of access being sold in underground marketplaces. These accounts sell for as cheap as $150 to as high as $5,000 based on the organization and the level of privileges. For example, in one of the postings, RDP credentials with proof of access to a Spain-based grocery retailer with a $5.7M annual revenue was being auctioned for a starting bid of just $500.

- Citrix accounts are another notable mechanism of initial access being sold by Initial Access Brokers. These account for 11% of all access being sold in underground marketplaces. One notable driver of this type of access is the exploitation of the previous zero-day vulnerability, CVE-2023-3519. In line with this, in July 2023, threat actors advertised access to various compromised Citrix credentials in various cybercrime forums, with starting bid prices of $3,000. For example, one of the posts asserted that the threat actor had successfully gained unauthorized access to a German retailer's system through a compromised Citrix instance, offering a screenshot taken from the compromised system as evidence of their claim.

- Microsoft Remote Desktop Web (RDWeb) accounts make up 7% of the types of access being sold in underground marketplaces. For example, last August 2023, a threat actor advertised the sale of unauthorized access, complete with domain administrator privileges to the network, of a lighting store located in the United Kingdom, using compromised Microsoft RDWeb credentials.

- Other types of access being sold in underground marketplaces were Microsoft Office 365, VPN, and SSH accounts. Organizations with these types of access can range from car dealerships in Slovakia to a large Saudi Arabia-based conglomerate of companies.

![RDP access with local admin privileges of a electronics and computer retailer being sold in underground forums]

Mitigations to Reduce Risk

- Regularly rotate passwords (e.g., every quarter) to mitigate issues related to valid accounts.

- Implement password complexity requirements to enhance security.

- Enable multi-factor authentication (MFA) to provide an additional layer of protection for accounts.

- Securely store credentials in programs in Password Managers to prevent credential abuse.

- Encrypt credentials when used in scripts to safeguard sensitive information.

- Audit local administrative accounts regularly and obfuscate admin accounts by not using admin in the name.

- Use LAPS on Windows systems to manage local accounts.

- Implement Privileged Access Management (PAM) and Privileged Identity Management (PIM) solutions to deepen defense in depth strategy.

## Initial Foothold: Vulnerability Exploitation
The Threat

Exploiting vulnerabilities is often the first thing people think of when it comes to information security. This topic encompasses discussions on zero days, patch agility, proof-of-concept exploits, and vulnerability disclosure.

Simply put, a vulnerability refers to a bug in software that introduces security risks. Attackers develop specialized software or scripts to exploit the vulnerability and circumvent security controls, such as authorization, authentication, and audit controls. Once the vulnerability is exploited, the attacker can bypass a security control and introduce a payload, which can manifest as various types of malware, as we will explore later.

A software patch provided by the vendor resolves the bug responsible for the vulnerability and prevents exploitation.

Trustwave SpiderLabs Insights

Through active monitoring, Trustwave SpiderLabs identified the most common exploits targeting our clients in the retail industry.

The exploits used in the attack attempts were mostly ZeroLogon (CVE-2020-1472) and Apache Log4J (CVE-2021-44228), but we also observed unspecified remote code execution attempts, MOVEit Transfer RCE (CVE-2023-34362), Exchange Server RCE (CVE-2022-41040, CVE-2022-41082), and Cross Site Scripting.

![Exploit procedures used by attackers]

Through our Dark Web research, we have observed threat actors that are auctioning information on SQL injection vulnerabilities affecting various global retailers and have reportedly successfully exfiltrated data from various retail databases. For example, in these auctions, threat actors claim they have successfully leveraged SQL injection vulnerabilities to exfiltrate data from a US-based sleep innovation company, a Sweden-based home appliances company, and an Italy-based eyewear conglomerate.

Additionally, a recent Trustwave SpiderLabs search of Shodan, which scans all public IP addresses on the Internet, turned up over 39,500 open ports, service banners and/or application fingerprinting in the top 50 global retailers of 2023.

![Number of open services of the top 50 global retailers of 2023]

The port and services profile of the retail sector does not differ much compared to the overall profile of our client base. Most of the ports open on the hosts were very common; TCP ports like 443 (https) and 80 (http) were the two most common. The HTTPS services were mainly for online shopping websites, payment processing/point of sale (POS) systems, inventory management, and customer support. Our team also noted other common ports and services were 161 (SNMP), 5985 (WinRM), 21 (FTP), 3306 (MySQL), 22(SSH), 8888 (HTTP), and 179 (BGP).

![Types of services exposed to the internet in retail organizations]

Across the retail organizations that had exposed services, there were numerous Apache HTTP Servers, Microsoft IIS Servers, and MySQL Servers that were outdated and vulnerable to known attacks. In line with this activity, we also discovered a popular UK-based retail chain had an unusually large port and service exposure (in the thousands), which is highly unusual and potentially dangerous.

Aside from outdated software, there are a multitude of misconfigured software and services in retail organizations exposed on the Internet. Among the interesting and notable ones are:

Multiple instances of alarm system interfaces exposed to the internet. If configured with weak or default passwords, an attacker could easily turn off security measures of any of the given retail stores leading to theft

Instances of Grafana (an open-source analytics tool) that is vulnerable to CVE-2023-3128 which lets an attacker take over the account and bypass authentication. This could potentially put consumer data at risk.

Instances of building automation systems without any password protection, which could potentially allow threat actors to take control of basic retail facility operations such as lights and air conditioning

Mitigations to Reduce Risk

- assessments and penetration testing to identify vulnerable servers. Pay close attention to consumer facing applications and mobile apps.

- Databases that store sensitive consumer data should be a priority for system and software patching. Database auditing tools like Trustwave’s DbProtect that can flag misconfiguration and user rights can also help eliminate risk.

- Place all servers behind the firewall and practice proper network segmentation for enhanced access control.

- Disable Internet access for servers that do not require it.

- Strengthen access controls to minimum necessary levels for authorized users.

- Promptly patch critical vulnerable systems.

## Initial Foothold: Supply Chain
The Threat

Supply chain attacks are increasingly prevalent. Instead of directly targeting multiple large entities, attackers concentrate their efforts on trusted third-party partners frequently utilized by these entities. This strategy is sometimes referred to as "the Domino Risk," as the attackers aim to to