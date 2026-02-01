# 2023 Retail Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
  - [Artificial Intelligence and Generative AI](#artificial-intelligence-and-generative-ai)
  - [Automated Bot Attacks in Retail](#automated-bot-attacks-in-retail)
  - [Third-Party Risk and Exposure](#third-party-risk-and-exposure)
- [Dissecting the Attack Flow for Retail](#dissecting-the-attack-flow-for-retail)
  - [Attack Flow Overview](#attack-flow-overview)
  - [Attack Flow Steps](#attack-flow-steps)
    - [Initial Foothold](#initial-foothold)
      - [Initial Foothold: Phishing and Business Email Compromise (BEC)](#initial-foothold-phishing-and-business-email-compromise-bec)
      - [Initial Foothold: Logging in](#initial-foothold-logging-in)
      - [Initial Foothold: Vulnerability Exploitation](#initial-foothold-vulnerability-exploitation)
      - [Initial Foothold: Supply Chain](#initial-foothold-supply-chain)
    - [Initial Payload](#initial-payload)
    - [Expansion / Pivoting](#expansion--pivoting)
    - [Malware](#malware)
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

---

# Executive Summary

The fiercely competitive realm of retail demands significant investment to establish brand recognition. However, this prominence also makes larger brands larger targets in cybersecurity. The online retail market surpassed $1.09 trillion in 2022, a 209% increase from 2019. Retailers face mounting cybersecurity challenges, with breaches of major retailers guaranteed to attract headlines. While the average cost of a breach in retail ($2.9 million) is lower than the industry average ($4.4 million), the public awareness and customer loyalty can amplify reputational damage.

Examples include a January 2023 breach of a UK-based sports retailer, compromising personal information of 10 million customers, and a September 2021 incident affecting a high-end retailer, exposing sensitive personal information of 4.6 million customers.

Factors making retailers vulnerable include:

*   **Rise of E-commerce**: Retailers store vast amounts of sensitive customer data and often rely on third-party vendors, increasing vulnerability to bot attacks and digital skimming.
*   **Seasonality**: Fluctuations in traffic and sales, especially during holiday seasons with temporary staff, create opportunities for cybercriminals.
*   **Omnichannel**: The complexity of securing physical stores, e-commerce websites, and mobile apps across multiple channels creates security challenges.
*   **Prevalence of Gift Cards**: Gift cards are used for anonymity and laundering funds from compromised payment platforms.
*   **Franchise Model**: Independent franchisees may lack the security resources of the parent company, creating brand-wide risks.

Trustwave SpiderLabs, with over 250 security researchers, investigates breaches through penetration tests, vulnerability discoveries, and analysis of millions of phishing URLs. Their expertise in threat hunting, forensics, incident response, malware reversal, and database security provides insights into breach causes and mitigation strategies.

This report examines the threats facing the retail industry and provides recommendations for mitigation. It highlights key trends: Generative AI, automated bots, and third-party risk. It then analyzes the retail-specific attack flow, detailing threat actors, intelligence, and mitigations for each stage.

The report covers prevalent threat tactics and actors, including:

**THREAT ACTORS**:
*   Royal
*   Bian Lian
*   LockBit
*   Clop
*   BlackCat/ALPHV
*   Play
*   8BASE
*   RansomedVC

**THREAT TACTICS**:
*   Email-Borne Malware
*   Access for Sale
*   Phishing
*   BEC
*   Malware
*   Consumer-Based Attacks
*   Vulnerability Exploitation
*   Bot Attacks
*   Credential Access
*   Gift Card Fraud and Scams

---

# Emerging and Prominent Trends

## Artificial Intelligence and Generative AI

**The Threat**
Generative AI and Large Language Models (LLMs) are advancing rapidly, setting new benchmarks for both retail organizations and adversaries. The retail industry's reliance on customer knowledge and personalized marketing makes it susceptible to AI integration in business intelligence and customer analytics platforms. Security protections within these systems must be rigorously vetted. Social engineering attacks are becoming more sophisticated due to LLMs' ability to craft highly personalized and targeted messages. The security of these AI systems is still unproven, necessitating a risk-benefit approach led by CISOs. Data privacy and security concerns are paramount.

**What Trustwave SpiderLabs Is Seeing**
Phishing remains a primary method for initial foothold, but its effectiveness relies on lure quality, writing style, and contextual clues. Generative AI and LLMs are making phishing emails easier to craft, more compelling, highly personalized, and harder to detect. Trustwave SpiderLabs analyzes phishing emails with malicious attachments or links targeting retail clients and observes that LLM advancements will likely enhance phishing effectiveness. Deepfakes are also increasing due to sophisticated technology.

LLMs like WormGPT and FraudGPT are appearing on underground forums, highlighting cybersecurity risks. These tools can craft convincing phishing emails without common red flags like misspellings or grammatical errors, making them harder for users to identify.

Trustwave monitors the implementation of Generative AI and LLMs, identifying increased speed and quality in phishing email drafting and exploit code enhancement. This requires security vendors to adapt their detection and response capabilities.

**Mitigations to Reduce Risk**
*   Evaluate security solutions with Generative AI and LLMs in mind, choosing tools that can detect AI-generated threats.
*   Create robust internal policies and employee training for proper data usage and sharing to minimize data breach risks.
*   Retail organizations must determine how to govern AI tools rather than instituting broad bans.
*   Consider establishing an internal AI Infosec working group across relevant teams (Legal, Privacy, IT, etc.) for governance and data sharing guidelines.

## Automated Bot Attacks in Retail

**The Threat**
The rise of automated bots in online retail introduces new threats, particularly during peak shopping seasons. These malicious bots pose significant risks to retailers and consumers, engaging in activities like scalping and freebie exploitation.

**What Trustwave SpiderLabs Is Seeing**
Trustwave SpiderLabs has observed a significant increase in malicious bot traffic during the holiday shopping season. These bots engage in credential stuffing, account takeover, gift card cracking, web scraping, API scraping, fake account creation, and inventory scalping. Bot attacks can disrupt online operations by simulating consumer actions, overwhelming websites, extracting pricing information, exploiting promotions, and conducting fraudulent transactions. This increases operational costs and can lead to financial losses.

Two specific types of malicious bots are noteworthy:

*   **GRINCHBOTS**: These scalping bots target hard-to-find holiday items, purchasing limited stock (inventory hoarding) and causing consumer frustration. For example, during the launch of new gaming consoles and the holiday season in 2020, Grinchbots made it difficult for consumers to purchase consoles, GPUs, and CPUs.
*   **FREEBIEBOTS**: These bots exploit errors on retail websites, allowing users to purchase incorrectly priced or inaccurately described items for resale. A study by Kasada found that members of a freebie community used Freebie Bots to acquire nearly 100,000 products valued at $3.4 million in a single month, spending only $882. During Black Friday and Cyber Monday 2022, Freebie Bots acquired products worth $500,000 from a single retailer for $85.36 across 610 users.

Freebie Bot attacks depend on mispriced items, which can occur due to:
*   Data Entry Error
*   Supplier Errors
*   Promotional or Discount Errors
*   Algorithmic Pricing malfunctions
*   Technical Glitches
*   Currency Conversion Errors
*   Timing Issues

**Mitigations to Reduce Risk**
*   Invest in DDoS and advanced filtering tools to block malicious traffic.
*   Ensure sufficient bandwidth and autoscaling resources to handle traffic spikes.
*   Regularly audit and update payment processing systems.
*   Employ end-to-end encryption for payment transactions.
*   Avoid storing sensitive customer data like full credit card numbers; use strong encryption and PCI DSS standards if necessary.
*   Implement multi-stage filtering to differentiate beneficial and malicious bots.
*   Adopt advanced rate limiting beyond traditional CAPTCHA to detect evasion techniques.
*   Implement cart session time limits.
*   Use browser environment verification and mobile API hardening.
*   Implement robust data entry procedures and regular price monitoring.
*   Utilize pricing management software and error detection technologies.

## Third-Party Risk and Exposure

**The Threat**
The retail industry's reliance on third-party vendors for services like point-of-sale (POS) systems, payment processing, supply chain management, and customer relationship management creates significant third-party risks. These vendors may have access to sensitive data or systems. Retail businesses must carefully vet vendors and implement strong security measures. Ensuring suppliers adhere to stringent security measures is crucial, as their systems may be reliant on vendor patches and updates, potentially opening them to vulnerabilities.

**What Trustwave SpiderLabs Is Seeing**
The retail industry depends on a stable and secure supply chain and third-party infrastructure for inventory, deliveries, expansion, and e-commerce operations. Cybercriminals often attack third parties as a flanking maneuver to gain access to targeted companies' data. The dependency on third-party software and vendors poses a grave risk. Recent supply chain incidents like SolarWinds and 3CX highlight this exposure.

Clop, a prevalent ransomware gang, was heavily associated with a campaign targeting a zero-day SQLi vulnerability in the MOVEit file transfer software. Retail organizations use MOVEit for transferring sensitive information. Notable retailers like TJX and Estee Lauder reported being affected.

**Mitigations to Reduce Risk**
*   Ensure retail organizations' systems and those of third-party partners are secure and protected by the latest security measures through regular penetration tests and vulnerability scans.
*   Maintain an inventory of all hardware and software, including vendor-developed components, operating systems, and version numbers.
*   Implement routine vulnerability scans before installing new devices or technology onto the IT network.

---

# Dissecting the Attack Flow for Retail

## Attack Flow Overview

While breach specifics vary, a typical attack flow exists from initial security bypass to escalation, compromise, persistence, and exfiltration/destruction of data. This analysis presents an overview of the attack flow specific to the retail sector, incorporating Trustwave SpiderLabs insights and offering actionable mitigations. Mitigations at each stage aim to minimize financial, reputational, regulatory, or physical impacts.

The typical sequence of events:

1.  **Initial Foothold**: Attacker bypasses security to gain initial access.
2.  **Initial Payload**: Attacker downloads more sophisticated tools and malware.
3.  **Expansion / Pivoting**: Attacker targets higher-value accounts and systems.
4.  **Malware**: Various malware types are deployed.
5.  **Exfiltration / Post Compromise**: Attacker steals or destroys data.

## Attack Flow Steps

### Initial Foothold

This is where the attacker successfully bypasses security to expand their access. It can range from phishing attacks to vulnerability exploitation or using acquired credentials.

#### Initial Foothold: Phishing and Business Email Compromise (BEC)

**The Threat**
Phishing and email-borne malware are the most common methods for initial foothold. Attackers target individuals, using persuasive emails to trick victims into opening attachments, clicking URLs, or transferring funds (e.g., "stranded CEO" scenario).

Typical phishing goals:
*   **Credential theft**: Links in invoices prompt users for passwords.
*   **Malware insertion**: Via PowerShell scripts, JavaScript, Macros.
*   **Triggering action**: Wire transfer for "stranded CEO" (BEC).

**Trustwave SpiderLabs Insights**
Trustwave SpiderLabs monitors email-based threats, observing developments in retail attack techniques. Over 70% of malicious emails contain malicious HTML attachments, with 30% obfuscated. These attachments often include phishing pages, redirectors, and malware (Agent Tesla, Emotet, Qakbot).

The decline of Emotet and Qakbot botnets has been noted, with campaigns now leveraging DarkGate malware, often distributed via hijacked email threads with LNK attachments. DarkGate is a loader advertised on Dark Web forums, using LNK attachments leading to VBS downloaders and then the DarkGate malware.

Traditional credential phishing remains a substantial threat. 70% of phishing links embed the victim's email address, making fraudulent websites appear more personal. Impersonated brands are often Microsoft and DHL. Cyber-squatting on the "onmicrosoft.com" domain is increasing.

"Payroll Diversion" is the most prevalent lure, impersonating employees to redirect paychecks. "Request for Contact" is second, aiming to collect mobile numbers for communication via SMS or chat apps to evade security gateways.

The most prevalent systems abused in phishing links are InterPlanetary File System (IPFS) and Google Services. IPFS is used to host malicious content due to its decentralized nature. Google services like Translate and Search are used to conceal deceptive or malicious links.

AI and LLMs like ChatGPT are impacting phishing. Misspellings and grammatical errors, once red flags, are becoming less common. LLMs make crafting compelling, personalized, and harder-to-detect phishing emails easier. WormGPT and FraudGPT on underground forums can craft convincing phishing emails, create undetectable malware, write malicious code, and find vulnerabilities.

**Mitigations to Reduce Risk**
*   Consistently conduct mock phishing tests and retrain repeat offenders.
*   Implement robust anti-spoofing measures on email gateways.
*   Deploy layered email scanning solutions.
*   Utilize techniques to detect domain misspellings.

#### Initial Foothold: Logging in

**The Threat**
Attackers gain network access by logging in, often through unchanged default credentials, weak passwords vulnerable to brute-forcing, or purchased credentials from underground forums. They can also buy access to webshells or active sessions.

**Trustwave SpiderLabs Insights**
Credential Access accounts for 30% of reported incidents in retail clients, with generic brute-force attacks being the majority. Attackers leverage valid accounts with weak passwords. Exposed passwords are found in custom batch files and scripts, and SFTP usage can expose passwords in command lines.

**Initial Access Brokers (IABs)** provide initial entry points, selling access gained through phishing, exploits, or social engineering. Notable types of access sold include:
*   **Remote Desktop Protocol (RDP) Accounts**: Most prevalent (34%), selling for $150-$5,000.
*   **Citrix Accounts**: 11% of access sold, driven by vulnerabilities like CVE-2023-3519.
*   **Microsoft Remote Desktop Web (RDWeb) Accounts**: 7% of access sold.
*   Other types include Microsoft Office 365, VPN, and SSH accounts.

**Mitigations to Reduce Risk**
*   Regularly rotate passwords.
*   Implement password complexity requirements.
*   Enable multi-factor authentication (MFA).
*   Securely store credentials in Password Managers.
*   Encrypt credentials when used in scripts.
*   Audit local administrative accounts regularly and obfuscate admin account names.
*   Use LAPS on Windows systems.
*   Implement Privileged Access Management (PAM) and Privileged Identity Management (PIM) solutions.

#### Initial Foothold: Vulnerability Exploitation

**The Threat**
Exploiting vulnerabilities (bugs in software) is a common initial access method. Attackers use specialized software to exploit these bugs, bypassing security controls like authorization and authentication. Software patches resolve these vulnerabilities.

**Trustwave SpiderLabs Insights**
Common exploits targeting retail clients include ZeroLogon (CVE-2020-1472) and Apache Log4J (CVE-2021-44228), along with unspecified remote code execution attempts, MOVEit Transfer RCE (CVE-2023-34362), Exchange Server RCE (CVE-2022-41040, CVE-2022-41082), and Cross-Site Scripting.

Threat actors auction information on SQL injection vulnerabilities affecting global retailers, claiming successful data exfiltration. Shodan scans reveal over 39,500 open ports and services in top global retailers, with common ports like 443 (HTTPS) and 80 (HTTP) for websites, payment processing, and inventory management. Other common ports include 161 (SNMP), 5985 (WinRM), 21 (FTP), 3306 (MySQL), 22 (SSH), 8888 (HTTP), and 179 (BGP).

Outdated and vulnerable Apache HTTP Servers, Microsoft IIS Servers, and MySQL Servers are common. Misconfigured software and services are also exposed, including alarm system interfaces, Grafana instances vulnerable to CVE-2023-3128, and building automation systems without password protection.

**Mitigations to Reduce Risk**
*   Conduct assessments and penetration testing to identify vulnerable servers, prioritizing consumer-facing applications.
*   Prioritize patching for databases storing sensitive consumer data. Use database auditing tools.
*   Place all servers behind firewalls and practice proper network segmentation.
*   Disable internet access for servers that do not require it.
*   Strengthen access controls to minimum necessary levels.
*   Promptly patch critical vulnerable systems.

#### Initial Foothold: Supply Chain

**The Threat**
Supply chain attacks target trusted third-party partners to gain access to multiple large entities. This "Domino Risk" strategy offers substantial ROI.

**Trustwave SpiderLabs Insights**
The retail industry relies heavily on third-party vendors for inventory, deliveries, expansion, and e-commerce. Cybercriminals attack these third parties as an "end-around maneuver" to access targeted companies' data. Dependency on third-party software and vendors poses a grave risk, as highlighted by SolarWinds and 3CX.

Clop ransomware was associated with a campaign targeting a MOVEit file transfer software vulnerability, affecting retailers like TJX and Estee Lauder. Analysis of Clop's Dark Web leaks shows multiple retailers falling victim, suggesting third-party software exploitation as a potential initial vector. Supply Chain Management companies have also been affected by ransomware attacks, potentially disrupting retail operations.

**Mitigations to Reduce Risk**
*   Prioritize the security and protection of your systems and those of third-party partners.
*   Implement the latest security measures.
*   Recognize that ecosystem security depends on the strength of its weakest link.

### Initial Payload

Once a foothold is established, attackers download more sophisticated tools and malware or leverage existing tools like PowerShell or LOLBins.

**Trustwave SpiderLabs Insights**
PowerShell is frequently used to execute commands and scripts, download, and run malicious payloads, often bypassing traditional security measures. PowerShell can download executables from the internet, running them directly from storage or in memory without disk interaction.

An example involved an unauthorized PowerShell command downloading a decoy PDF and a .bat executable, which turned out to be the Ducktail malware, designed to steal sensitive information, browser cookies, and session data, and hijack social media accounts via Telegram.

Social engineering to get users to open files leading to code execution is another popular technique.

**Mitigations to Reduce Risk**
*   Conduct regular audits of all applications operating within the environment.
*   Implement highly granular whitelisting of applications on specific hosts.
*   Prevent malicious actors from deploying applications that masquerade as known apps.
*   Monitor commands being run to identify malicious actions.
*   Apply additional privilege restrictions to prevent unprivileged sources from running different shells.

### Expansion / Pivoting

Since the initial foothold is often on a low-value system, attackers target higher-value accounts and systems like Domain Admins, Root Accounts, Active Directory Systems, and Database servers.

**Trustwave SpiderLabs Insights**
The goal is privilege escalation and expansion, often referred to as "pivoting" or "lateral movement." The most common lateral movement techniques in retail are Remote Desktop Protocol (RDP), "Pass the Ticket," and movement through SMB and Windows Admin Shares. These are exploited by ransomware gangs.

Attackers establish persistence using External Remote Services, Account Creation, Account Manipulation, and Valid Accounts.

*   **External Remote Services**: Threat actors leverage external-facing services like RDP, VPNs, and Citrix for initial access and persistence. Legacy and test systems running these services can be forgotten and exploited.
*   **Account Creation**: Threat actors create new or modify existing user accounts (backdoor accounts, fake service accounts) to maintain access.
*   **Account Manipulation**: Exploiting vulnerabilities or weaknesses in user accounts, credentials, and permissions (privilege escalation, pass the hash, kerberoasting).
*   **Use of Valid Accounts**: Exploiting mechanisms that initiate actions in response to events (user logons, application execution) to repeatedly execute malicious code. These accounts are often obtained through IABs, credential phishing, and infostealers.

**Mitigations to Reduce Risk**
*   Perform routine assessments of all applications to counter custom applications that might introduce vulnerabilities.
*   Establish a detailed whitelist of applications on specified hosts.
*   Enforce privilege constraints to block unauthorized execution of different shells.
*   Conduct regular user and service account reviews.

### Malware

#### Malware: Infostealers

**The Threat**
Infostealers are specialized malware designed to steal information, targeting data at rest and in transit. They steal contacts, cached passwords, cryptocurrency wallets, system details, and can manipulate browser connections to steal account information or perform unauthorized actions.

**Trustwave SpiderLabs Insights**
Notable infostealers observed in the retail sector include:

*   **LUMMA STEALER**: Emerged in 2022, gathering login credentials from web browsers, cryptocurrency wallets, browser extensions, and 2FA systems. It can be used to download other malware.
*   **DUCKTAIL**: Originated in 2021, a .NET malware stealing sensitive system information, browser cookies, and session data, and hijacking social media accounts via Telegram. Often initiated through unauthorized PowerShell commands.
*   **PRILEX POS**: Advanced malware discovered in 2022, capturing transaction data, forcing protocol downgrades, and running credit card fraud. It can target NFC-enabled cards and block contactless transactions to force PIN pad entry for data capture.

**Mitigations to Reduce Risk**
*   Use host-based anti-malware tools, understanding their limitations.
*   Enable system and network logs for valuable systems and workstations.
*   Implement active monitoring of logs to establish baselines and detect abnormal behavior.
*   Establish and regularly practice a formal Incident Response process.
*   Perform ongoing Underground and Dark Web monitoring for information leakage.

#### Malware: RATs

**The Threat**
Remote Access Trojans (RATs) provide administrative backdoor access, allowing attackers to download files, capture sensitive data, take screenshots, execute binaries, upload malware, activate webcams/microphones, and sniff network traffic.

**Trustwave SpiderLabs Insights**
RATs observed in the retail sector include:

*   **DARKGATE**: A loader distributed through infected email attachments, malicious ads, software cracks, and social engineering. It supports VNC access, cryptocurrency mining, reverse shells, keylogging, and information stealing. It has been observed supplanting Qakbot campaigns.
*   **AMADEY BOT**: A Trojan used for stealing sensitive information and loading other malware. It can collect data from web browsers, target crypto wallets, terminate wallet processes, intercept cryptocurrency transactions, and monitor the clipboard. It spreads through phishing sites and spam emails.
*   **SECTOPRAT**: A .NET RAT with stealth functions, victim system profiling, and information stealing capabilities. It can create hidden secondary desktops and has anti-VM/anti-emulator features. It has been seen working with Amadey Bot and Lumma Stealer in multi-malware packages.

**Mitigations to Reduce Risk**
*   Use host-based anti-malware tools.
*   Enable system and network logs for valuable systems and workstations.
*   Implement active monitoring of logs.
*   Establish and regularly practice a formal Incident Response process.
*   Perform ongoing Underground and Dark Web monitoring.

#### Malware: Ransomware

**The Threat**
Ransomware encrypts or locks data, demanding a ransom for access. Modern campaigns remove access to backups and delete Volume Shadow Copies. Double extortion involves exfiltrating data before deployment and threatening public posting. Triple extortion includes DDoS attacks.

**Trustwave SpiderLabs Insights**
Prevalent ransomware groups in retail include Lockbit, Alphv/BlackCat, and Black Basta. Clop, Royal, Play, Akira, 8BASE, and RansomedVC also operate in this sector.

*   **LOCKBIT**: Evolved from ABCD ransomware, with versions like LockBit 2.0, 3.0, and Green. It infiltrates via RDP, phishing, and vulnerability exploits. It displays ransom notes, changes computer appearance, and sends encrypted info to C2 servers. A major Canadian bookstore chain was a victim.
*   **ALPHV/BLACKCAT**: Gains access through compromised credentials and MS Exchange server vulnerabilities. They disable security tools, unregister antivirus, and run ransomware in safe mode. They conduct extensive discovery and exfiltrate data using alternative protocols. A US-based technology company providing retail solutions was targeted.
*   **BLACK BASTA**: Allegedly connected to Conti, REvil, and Fin7. It uses private recruitment, QakBot, Cobalt Strike, and network access brokers. Attacks have occurred in Canada, Belgium, Germany, and the US.
*   **CLOP**: Believed to be Russian-speaking, affiliated with FIN11 and TA505. Uses spearphishing, Cobalt Strike, and lateral movement. Exploited a zero-day vulnerability in Fortra GoAnywhere MFT, targeting approximately 130 organizations, including a US multinational health and hygiene corporation and a luxury department store chain.
*   **ROYAL**: Demands $1M-$11M in Bitcoin. Uses phishing emails (66.7%), malicious PDF documents, malvertising, RDP compromise, and public-facing application exploits. Has a significant focus on Venezuela.
*   **PLAY**: Concentrates attacks on Latin America, particularly Brazil. Leverages exploits in FortiOS SSL VPN, ProxyNotShell, OWASSRF, and MS Exchange Server. The UK arm of a large Japanese retailer and a US-based health food retailer were victims.
*   **8BASE**: Operational since March 2022, intensifying in June 2023. Targets small and medium-sized businesses (SMBs), with a preference for business services, finance, manufacturing, and IT. Claimed responsibility for breaches affecting a US printing superstore and a US car dealership group.
*   **RANSOMEDVC**: Emerged in August 2023, targeting corporations, government bodies, and educational institutions. Exploits GDPR laws for extortion. Has put its entire toolkit up for sale, including a ransomware builder, affiliate access, and VPN access to companies with significant revenue.

**Mitigations to Reduce Risk**
*   Use host-based anti-malware tools.
*   Enable system and network logs.
*   Implement active monitoring of logs.
*   Establish and regularly practice a formal Incident Response process.
*   Perform ongoing Underground and Dark Web monitoring.

### Exfiltration / Post Compromise

Once attackers are within a network, they execute their final plan, which can be a "smash and grab" for data, meticulous targeting of specific systems, or widespread destruction.

**Trustwave SpiderLabs Insights**
There is an overwhelming tendency towards data encryption related to unspecified ransomware activity. Retailers are targeted due to financial transactions and customer data (payment information, personal details), making them appealing for extortion or black market sales. Disruptions during peak shopping seasons increase the urgency to pay ransoms. Retailers' reliance on intricate supply chains and operational necessity to meet ransom demands make them prime targets.

Most ransomware gangs use double-extortion tactics (encrypting and threatening to expose data). The increasing sophistication and monetary incentive make defense difficult.

**Mitigations to Reduce Risk**
*   Monitor the Dark Web regularly for potential compromises.
*   Conduct regular penetration tests to identify vulnerabilities.
*   Decrease the time to remediation.
*   Run continuous Threat Hunting for undetected compromises.
*   Formalize and regularly test your Incident Response Policy.

---

# Consumer Attacks in Retail

## Bot Attacks in Retail

**The Threat**
Automated bots in online retail pose new threats, especially during peak shopping seasons. These malicious bots engage in scalping and freebie exploitation, risking online retailers and consumers.

**Trustwave SpiderLabs Insights**
Trustwave SpiderLabs has observed a significant increase in malicious bot traffic during the holiday shopping season, including credential stuffing, account takeover, gift card cracking, web scraping, API scraping, fake account creation, and inventory scalping. Bot attacks can disrupt operations by simulating consumer actions, overwhelming websites, extracting pricing information, exploiting promotions, and conducting fraudulent transactions, increasing operational costs and leading to financial losses.

Two specific types of malicious bots are noteworthy:

*   **GRINCHBOTS**: Scalping bots targeting hard-to-find holiday items, causing consumer frustration by purchasing limited stock (inventory hoarding).
*   **FREEBIEBOTS**: Exploit errors on retail websites, allowing users to purchase incorrectly priced or inaccurately described items for resale. A study found members of a freebie community used Freebie Bots to acquire nearly 100,000 products valued at $3.4 million in a single month, spending only $882. During Black Friday and Cyber Monday 2022, Freebie Bots acquired products worth $500,000 from a single retailer for $85.36 across 610 users.

Freebie Bot attacks depend on mispriced items, which can occur due to:
*   Data Entry Error
*   Supplier Errors
*   Promotional or Discount Errors
*   Algorithmic Pricing malfunctions
*   Technical Glitches
*   Currency Conversion Errors
*   Timing Issues

**Mitigations to Reduce Risk**
*   Invest in DDoS and advanced filtering tools.
*   Ensure sufficient bandwidth and autoscaling resources.
*   Regularly audit and update payment processing systems.
*   Employ end-to-end encryption for payment transactions.
*   Avoid storing sensitive customer data like full credit card numbers; use strong encryption and PCI DSS standards if necessary.
*   Implement multi-stage filtering to differentiate beneficial and malicious bots.
*   Adopt advanced rate limiting beyond traditional CAPTCHA.
*   Implement cart session time limits.
*   Use browser environment verification and mobile API hardening.
*   Implement robust data entry procedures and regular price monitoring.
*   Utilize pricing management software and error detection technologies.

## Dark Web Fraud and Scams in Retail

**The Threat**
Dark Web scams and fraud, particularly gift card fraud and refund schemes, are pervasive threats in the retail industry. Understanding and combating these forms of fraud are critical for retailers to safeguard operations and maintain customer trust.

**Trustwave SpiderLabs Insights**

**GIFT CARD FRAUD**
Gift cards are used by threat actors for anonymity and to launder funds from compromised credit cards. They acquire high-value gift cards using stolen credentials, which are then used or sold for profit. Tactics include:
*   Purchasing cards using stolen credit card details.
*   Extracting gift card numbers from databases.
*   Social engineering tricks.
*   Physical tampering of gift cards.
*   Manipulating gift card refund policies.

Online services provide guides for credit card fraud and illicit cash withdrawal schemes targeting retailers like Apple, Best Buy, and Walmart. Gift cards are used in BEC schemes to hide the origins of ill-gotten gains, often converted into cryptocurrencies. Scattered Canary used Paxful to conceal gift card proceeds. Loyalty programs and rewards from retailers like Macy's, Nordstrom, and Target are also stolen, counterfeited, and sold.

**REFUND SCHEME**
The "refund scheme" involves obtaining cash refunds without returning purchased items, often facilitated by "reputable refund gangs" who claim high success rates and anonymity. Fraudulent returns constitute a substantial portion of all industry returns ($85 billion in 2022), with online fraudulent returns making up roughly $22.8 billion. Dark Web gangs play a significant role in this fraud.

**Mitigations to Reduce Risk**
*   Require strong authentication for consumer accounts (encryption, CAPTCHA, two-factor authentication).
*   Educate customers on account safety best practices.
*   Monitor for suspicious bulk purchases and limit accounts or IP addresses.
*   Enforce stricter gift card activation rules and check for tampering.
*   Limit gift card purchases per customer or transaction.
*   Avoid gift card payments on guest checkouts; require account creation.
*   Enforce well-defined return policies (receipts, original packaging, timeframes, identity verification).
*   Regularly review refund and return data to identify suspicious patterns.

---

# Key Takeaways and Recommendations

The retail sector is an attractive target due to its high volume of financial transactions and extensive customer data (payment details, personal contact information), which is valuable for identity theft, financial fraud, and targeted cyberattacks. Intricate supply chains also present vulnerable entry points.

The rise of e-commerce has brought new challenges. Threat actors exploit vulnerabilities in retailers and consumers, especially during peak shopping times when security measures are stretched. Underground forums facilitate the monetization of acquired data.

The retail industry faces threats from multiple fronts:

*   **Valuable Data**: Retail databases are prime targets. Phishing, spearphishing, and BEC attacks are increasingly sophisticated.
*   **Supply Chain Vulnerabilities**: The complex web of suppliers and partners introduces multiple points of vulnerability.
*   **Financial Transactions**: The sheer volume of transactions makes retail businesses targets for payment card theft or personal identification data theft, which can be sold on the Dark Web or used for fraud.
*   **Ransomware Attacks**: The sector faces a rise in ransomware attacks, causing significant financial and reputational damage.
*   **E-commerce Threats**: Bot attacks and digital skimming pose unique challenges, particularly during peak business times.

Attackers often use multiple vectors for persistent targeting. While technical aspects evolve, underlying methods like phishing, email-borne malware, exploiting vulnerabilities, and compromising third-party vendors remain significant threats. Threat actors continuously refine techniques, incorporating new exploits, malware, and technologies like Generative AI for social engineering. Attacks targeting retail organizations are unlikely to subside.

**ACTIONABLE MITIGATION RECOMMENDATIONS:**

**Initial Foothold**
*   Consistently conduct mock phishing tests and retrain repeat offenders.
*   Utilize techniques to detect domain misspellings for identifying phishing and BEC attacks.
*   Regularly rotate passwords, implement password complexity requirements, enable multi-factor authentication (MFA), and securely store or encrypt credentials.
*   Implement vulnerability assessments and penetration testing, promptly patch critical systems, and keep all software up to date.

**Initial Payload & Expansion / Pivoting**
*   Regularly audit all applications to prevent vulnerabilities from custom applications.
*   Implement a detailed whitelist of applications and externally accessible remote services to minimize exposure and prevent malicious actors from gaining access or introducing disguised harmful applications.
*   Impose additional restrictions on privileges to prevent unauthorized execution of different shells from unprivileged sources.

**Malware**
*   Use host-based anti-malware tools.
*   If prevention is not possible, audit controls become crucial indicators of potential compromise. Enable system logs on valuable systems and workstations, and implement network logging.
*   Implement active monitoring of logs to establish baselines and detect abnormal behavior.

**Exfiltration / Post Compromise**
*   Monitor the Dark Web regularly for potential compromises.
*   Run continuous Threat Hunting for undetected compromises.
*   Formalize and regularly test your Incident Response Policy.

---

# Appendix/Reference

## Threat Groups

### 8BASE
*   8BASE is a ransomware group operating under a Ransomware-as-a-Service (RaaS) model since April 2022. They use a private ransomware strain named 8BASE aka RADAR 8BASE, which encrypts data on NAS, VMware ESXi hypervisors, and Unix/Windows operating systems.
*   The ransomware resembles customized versions of Babuk and Phobos, suggesting crossover between groups. 8BASE targets small to medium-sized entities opportunistically.

### Bian Lian
*   Active since June 2022, BianLian is involved in ransomware development, deployment, and data extortion. They target crucial US infrastructure, Australian infrastructure, professional services, and property development. Entry often involves exploiting valid RDP credentials and using open-source tools for data discovery.
*   After accessing victim systems, BianLian extracts data using FTP, Rclone, or Mega and threatens publication unless a ransom is paid. They shifted