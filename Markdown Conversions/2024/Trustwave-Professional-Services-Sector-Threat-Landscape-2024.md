# 2024 Professional Services Threat Landscape: Trustwave Threat Intelligence Briefing and Mitigation Strategies

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
  - [Supply Chain Exposure](#supply-chain-exposure)
  - [Rise of Ransomware](#rise-of-ransomware)
  - [Double-Edged Sword of Technology](#double-edged-sword-of-technology)
- [Dissecting the Attack Flow for Professional Services](#dissecting-the-attack-flow-for-professional-services)
  - [Attack Flow Overview](#attack-flow-overview)
  - [Attack Flow Steps](#attack-flow-steps)
    - [Initial Foothold](#initial-foothold)
      - [Phishing, Spam & Scams](#phishing-spam--scams)
      - [Logging in](#logging-in)
      - [Vulnerability Exploitation](#vulnerability-exploitation)
      - [Supply Chain](#supply-chain)
    - [Initial Payload](#initial-payload)
    - [Expansion / Pivoting](#expansion--pivoting)
    - [Malware](#malware)
      - [Loaders, Infostealers and RATs](#loaders-infostealers-and-rats)
      - [Ransomware](#ransomware)
    - [Exfiltration / Post Compromise/Impact](#exfiltration--post-compromiseimpact)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)

---

## Executive Summary

Professional services firms, including legal service entities, are prime targets for cyberattacks due to the wealth of sensitive data they hold. This treasure trove includes intellectual property, financial information, legal documents, and personal client details. Such data is a goldmine for cybercriminals seeking financial gain, identity theft, or a competitive edge. A cyberattack can severely damage a professional services firm's reputation, as clients entrust them with keeping their data confidential and secure.

The consequences of a cybersecurity breach in this sector can be catastrophic. Financial losses from recovery efforts, legal fees, and potential fines are compounded by the severe reputational damage that erodes client trust and future business. Operational disruptions, employee stress, and increased regulatory scrutiny further exacerbate these challenges. As a result, robust cybersecurity is a critical priority for these information-rich firms.

To ensure comprehensive coverage, this report examines cybersecurity challenges facing professional service firms, including legal services, consulting services, and accounting services. While a broad coverage area, the sector encompasses businesses that sell expertise and intellectual capital rather than tangible products.

Australian law giant HWL Ebsworth was hit by ransomware in April 2023. The attackers (ALPHV/Blackcat) claimed to steal 4TB of data, including client info and financial reports, before the firm publicly disclosed the breach. In May 2020, Entertainment law firm Grubman Shire Meiselas & Sacks fell victim to a ransomware attack by REvil. The hackers leaked client data, including Lady Gaga's, and threatened to expose more celebrities' information to pressure the firm.

Cybersecurity within professional services is a complex landscape with a number of unique factors, including:

- **High Value of Data**: Law firms and other professional services firms deal with a wealth of sensitive information - intellectual property, legal documents, financial records, and personal client data. This data is highly attractive to cybercriminals seeking financial gain, a competitive edge, or for identity theft purposes.
- **Complex Vendor Ecosystem**: These firms often rely on a network of third-party vendors and suppliers for various services. Each vendor introduces a potential security risk, as a weakness in a vendor's system can be exploited to gain access to the professional services firm's network.
- **Regulatory Burden**: The professional services industry, especially law firms, faces strict regulations regarding data protection, privacy, and security. Compliance with these regulations can be complex, requiring significant resources and ongoing vigilance.
- **Reputation is Paramount**: A cyberattack can have a devastating impact on a professional services firm's reputation. Clients trust these firms to keep their data confidential and secure. A data breach can erode client trust and damage future business prospects.

Leveraging the expertise of hundreds of security researchers, Trustwave SpiderLabs is uniquely positioned to analyze the evolving threat landscape. Our team identifies tens of thousands of vulnerabilities each year, performs thousands of penetration tests and analyzes millions of phishing URLs daily. This comprehensive coverage across information security disciplines – including continuous threat hunting, forensics, incident response, malware analysis, and database security – empowers us to not only understand how breaches occur, but also recommend effective mitigations and controls for organizations.

This report delves into the critical trends impacting the professional services sector, including supply chain exposure, the rise of ransomware, and the double-edged sword of emerging technology. We will then dissect the attack flow specific to professional services entities, providing actionable intelligence, and tailored mitigation strategies at each stage. We will examine many of the most prevalent threat tactics and threat actors, including:

**THREAT ACTORS**
- Lockbit
- Blackcat/ALPHV
- REvil

**THREAT TACTICS**
- Phishing and Business Email Compromise (BEC)
- Supply Chain/Third-Party Risk
- Data Brokers and Access Brokers
- Malware and Ransomware
- Vulnerability Exploitation
- Powershell-Driven Execution
- Social Engineering and User Driven Execution

---

## Emerging and Prominent Trends

### Supply Chain Exposure

**The Threat**
Cybercriminals are increasingly targeting trusted third-party vendors used by professional services and legal firms. This approach allows them to gain a backdoor into the target companies' data through a less secure vendor.

These firms often act as third parties themselves and rely heavily on various external software, consultants, and contractors. This complex supply chain creates numerous potential entry points for attackers.

**What Trustwave SpiderLabs Is Seeing**
Research shows third-party software, particularly file transfer services like MOVEit, is a common cause of supply chain breaches in professional services. Later in the report, we’ll highlight several examples where MOVEit vulnerabilities were exploited to access sensitive data at firms like Ernst & Young, Deloitte, PwC, and Kirkland & Ellis.

The report also details breaches caused by vulnerabilities in third-party cloud storage platforms and electronic discovery vendors used by professional services firms like Proskauer Rose, Quinn Emanuel, and Goodwin Procter.

**Mitigations to Reduce Risk**
- **Vet Third-Party Vendors**: Conduct security assessments and include strict cybersecurity clauses in contracts, requiring regular audits and breach notifications.
- **Review & Patch**: Regularly review vendor security practices, conduct vulnerability assessments, and implement penetration testing.
- **Tighten Internal Controls**: Enforce access controls, change control, and audit trails to monitor unauthorized activity.
- **Data Security**: Encrypt sensitive data at rest and in transit, restrict access based on need, and monitor access logs for suspicious behavior.
- **Compliance**: Ensure vendors comply with relevant data protection regulations.
- **Employee Training**: Train employees on cybersecurity hygiene to identify and prevent phishing and social engineering attacks.

### Rise of Ransomware

**The Threat**
Professional services firms are in the crosshairs of a rapidly evolving ransomware crisis.

Ransomware attackers often target not just firms’ data but also client data such as intellectual property, trade secrets, and internal operational data where the theft or exposure of which can severely compromise a company's competitive advantage and market position. Exposure of confidential data will affect the firm and the multitude of clients they cater to.

**What Trustwave SpiderLabs Is Seeing**
Professional services and legal entities have experienced a significant surge in ransomware attacks, with at least 142 firms falling victim over the past year.

Despite recent law enforcement seizures of prominent ransomware groups like LockBit and ALPHV/BlackCat, their impact within the current year continues to be significant. These groups remain the top two most active ransomware operators (Fig 1), with only slight differences in the frequency of reported incidents. The third position is now occupied by the 8Base group.

![Figure 1: Professional services sector victims' distribution according to claims of ransomware gangs](Image description: A pie chart showing the distribution of ransomware victims in the professional services sector by ransomware gang. Lockbit3 accounts for 19%, 8base for 19%, Alphv for 20%, Biantian for 18%, Play for 6%, Blackbasta for 4%, Medusa for 4%, Akira for 3%, and Other for 20%.)

**Mitigations to Reduce Risk**
- **Anti-Malware**: Use host-based anti-malware tools but be aware of their limitations against custom malware.
- **Email Security**: Strengthen email controls to block ransomware sent via email. Train employees to identify suspicious emails and attachments.
- **Incident Response Plan**: Develop and practice a formal incident response plan, including data backups for recovery.
- **Enable System Logging**: Enable system and network logging across critical systems to monitor activity.
- **Active Monitoring**: Continuously monitor logs to detect abnormal behavior or suspicious traffic.
- **Dark Web Monitoring**: Monitor the dark web for potential information leaks.
- **Least Privilege**: Enforce the principle of least privilege to limit access to data.
- **Defense in Depth**: Implement layered security with multiple anti-malware scanners from different vendors.

### Double-Edged Sword of Technology

**The Threat**
The embrace of emerging technologies by professional services firms to better serve clients is a double-edged sword.

While these technologies offer exciting new solutions and a competitive edge, they also introduce significant cybersecurity risks. Unfamiliar attack surfaces in new technologies and the complexities of integrating them with existing systems create vulnerabilities for cybercriminals to exploit.

Additionally, reliance on third-party vendors for these technologies introduces another layer of risk. To mitigate these threats, firms need to prioritize employee training on security protocols for the new technologies, implement robust data security measures, and stay updated on evolving compliance regulations.

**What Trustwave SpiderLabs Is Seeing**
Data breaches involving emerging technologies are a growing concern. Emerging technologies often lack a mature security track record, meaning vulnerabilities may not be fully understood or patched. This creates a larger attack surface for cybercriminals to exploit.

For example, several professional services firms have experienced data breaches or leaks after migrating to cloud platforms. These incidents can occur due to misconfigured cloud storage settings, inadequate access controls, or a lack of employee training on cloud security best practices. These examples showcase the importance of careful planning and implementation when integrating new technologies like cloud computing.

**Mitigations to Reduce Risk**
- **Employee Training**: Professional services firms must prioritize employee training on security protocols for new technologies. This ensures employees understand the specific risks associated with these technologies and how to handle data securely.
- **Robust Data Security**: Implementing robust data security measures is crucial. This includes data encryption, access controls, data loss prevention strategies, and proper data disposal practices.
- **Compliance Awareness**: Staying updated on evolving compliance regulations surrounding data privacy and security is essential. Firms need to ensure their use of emerging technologies adheres to these regulations.
- **Vendor Risk Management**: Since reliance on third-party vendors for emerging technologies introduces risk, firms need to conduct thorough vendor assessments and ensure their security posture is strong.

---

## Dissecting the Attack Flow for Professional Services

### Attack Flow Overview

Data breaches and compromises come in many forms but often follow a similar pattern. Attackers gain access, escalate privileges, establish a foothold, steal or destroy data, and then vanish. This analysis focuses on this attack flow within professional services, drawing on insights from Trustwave SpiderLabs. It also provides actionable steps organizations can take to mitigate these risks.

These recommendations aim to proactively minimize financial losses, reputational damage, regulatory issues, and even physical harm that professional services organizations might face during an attack. The typical sequence of events unfolds as follows:

- Initial Foothold
- Initial Payload
- Expansion / Pivoting
- Malware
- Exfiltration / Post Compromise

### Attack Flow Steps

#### Initial Foothold

This is the step where the attacker successfully triggers a security bypass, giving them the ability to expand their access to suit their motives and goals. This initial foothold can take various forms, ranging from successful phishing attacks to vulnerability exploitation or even logging into public-facing systems using previously acquired credentials.

In this section, we will explore the most common methods by which attackers gain this initial foothold in a professional services firm, like phishing, third-party suppliers, and exploitable vulnerabilities.

##### Phishing, Spam & Scams

**The Threat**
Professional services firms, just like many others, are particularly vulnerable to phishing attacks. Unlike exploiting software flaws, attackers target the human element. They craft emails designed to manipulate employees, contractors, or anyone with access to critical systems like financial or customer databases. These emails aim to trick the recipient into taking a specific action, such as opening an attachment, clicking a malicious link, or even following instructions that compromise security.

Typical phishing goals:
- **Credential Theft**: An example of this would be an email that appears to be from the company's admin, containing a link. When the recipient clicks this link, they are prompted to enter their login details under the pretense of accessing important information or job opportunity details.
- **Malware Insertion**: This is often executed by embedding PowerShell scripts, JavaScript, or enabling Macros in a document.
- **Triggering Specific Actions**: This could involve convincing the recipient to provide confidential information or perform other actions under the guise of a necessary step for a certain request.

**Trustwave SpiderLabs Insights**
The Trustwave SpiderLabs team keeps a close eye on email threats targeting professional services. This scrutiny includes opportunistic (broad) phishing, spear-phishing (targeted) attacks, malware-laden spam, and scams. Notably, we've observed a concerning trend: attackers constantly refine their tactics and delivery methods, keeping these email-based attacks relevant and impactful.

In the professional services sector, Trustwave SpiderLabs observed that HTML attachments were the predominant method of delivering malicious payloads, with over 60% serving as credential phishing pages and approximately 8% acting as redirectors. These HTML attachments are often heavily obfuscated to conceal the malicious content from security scanners.

PDF files were the second most abused type at 13% with more than half of these files containing links to phishing sites or malicious files. Notably, 8% of PDFs involve 'Quishing' (using QR codes to hide malicious URLs) and 2% use HTML smuggling.

![Figure 2: Top malicious attachment filetypes for professional services](Image description: A bar chart showing the top malicious attachment filetypes for professional services. HTML accounts for 65%, DOC/DOCX for 14%, XLS/XLSX for 12%, PDF for 11%, RTF for 3%, EXE/W32 for 2%, VBS for 2%, and Other for 2%.)

RTF, Word, and Excel documents were also observed being commonly used as downloaders exploiting old CVEs to download further malware, and some contain phishing links or scams. Our researchers also noted interesting observations that were relatively common across industries:
- The InterPlanetary File System (IPFS) is a significant vector in email phishing, representing 35% of phishing links and exploiting its decentralized nature to evade detection.
- Google domains and Cloudflare services are exploited for their reputability to deliver phishing content.
- WordPress sites are manipulated to set up fake login pages.
- In Business Email Compromise (BEC) attacks, 'Payroll Diversion' and 'Request for Contact' are common tactics like other industries.

In a review of our professional services sector dataset, Trustwave researchers observed several notable phishing campaign themes targeting the organizations themselves and the stakeholders who use the organization’s various services. Our researchers also noted that most of the phishing campaigns are focused on legal services.

**ATTORNEY IMPERSONATION – BEC SCAM**
A common campaign in the professional services sector that Trustwave SpiderLabs researchers have been monitoring are attorney impersonation scams. Attorney impersonation involves pretending to be a legal representative of a vendor company or law firm to deceive victims with fake invoices, directing payments to attackers' bank accounts. In one campaign (Fig 3) that our researchers have observed, known as “Multi-Persona Invoice Transaction BEC,” attackers impersonate both a company executive and a lawyer from a global law firm, creating a fabricated email thread. Initially, the thread shows the "executive" reminding the victim about an outstanding invoice for attorney services with the "lawyer" cc'd, though this exchange never actually occurred.

Subsequently, the "lawyer" directly contacts the victim to follow up on the invoice. The impersonating attorney uses a domain with a minor alteration—inserting an "l" into the legitimate domain name (e.g., "hogansllovel.com")—a practice called typo-squatting. This technique, featuring multiple fake personas and specific details like invoice numbers and payment deadlines, increases the attack's realism and urgency, differing from the typically brief content of traditional BEC messages.

![Figure 3: Sample from an Attorney Impersonation BEC campaign](Image description: A sample email from an attorney impersonation BEC campaign. The email appears to be a continuation of a conversation between an executive and a lawyer regarding an invoice. The lawyer's email address uses a typo-squatted domain.)

**DEBT RECOVERY OFFICER IMPERSONATION**
Another campaign that our researchers observed deals with impersonation of debt recovery officers. Debt recovery officers, or debt collectors, are individuals that help financial companies recover owed money by tracking accounts, identifying outstanding debts, planning recovery strategies, and negotiating payments with debtors.

In the campaign below (Fig 4), a purported debt collector, acting for an unspecified client contacts a target. The email message includes detailed elements like an invoice number and is professionally crafted to enhance its perceived legitimacy. However, as observed here, a significant red flag in the scam is the use of newborn domains in both the 'From' and 'Reply to' fields of the email's header, indicating a potential fraud. This message primarily aims to act as an initial vector for the scammer to gather information about the victim.

![Figure 4: Sample from a debt recovery officer Impersonation phishing campaign](Image description: A sample email from a debt recovery officer impersonation phishing campaign. The email claims to be from a debt collector and includes an invoice number. The sender and reply-to domains are newly registered.)

**LAW FIRM IMPERSONATION IN ADVANCE-FEE FRAUD**
Like the two previous campaigns, our team have observed that scammers frequently impersonate professionals due to the trust and authority associated with these roles contributing to schemes like ‘Advance Fee Fraud.’ This type of scam tricks individuals into paying upfront fees under the guise of receiving a large future sum.

The campaign below (Fig 5) shows a message claiming to be from a legitimate law firm named 'Ravenscroft & Schmierer.' The message states that a distant relative has left a valuable estate and prompts the victim to contact an email address for more details. This email is controlled by the scammer who, upon contact, will request money disguised as legal fees and may also ask for sensitive information.

![Figure 5: Sample from an “Advance-fee Fraud” BEC campaign](Image description: A sample email from an "Advance-fee Fraud" BEC campaign. The email claims to be from a law firm and states that a distant relative has left an estate, prompting the recipient to contact a provided email address for more details.)

**SPECIAL POWER OF ATTORNEY**
Our researchers noted that legal documents such as the “Special Power of Attorney” (SPOA) document, are a particularly common type of “lure” used in many campaigns. A special power of attorney (SPOA) is a legal document that grants one person (the agent) authority to act on behalf of another (the principal) in specific situations, such as making financial or medical decisions.

In a phishing scam campaign that Trustwave SpiderLabs researchers have observed (Fig 6), threat actors used an SPOA document as bait within an email. The email, written in Portuguese, claims that all parties involved have signed the document and appears to be sent by CredPago, a Brazilian property rental analytics platform. It prompts the recipient to view the document via an embedded URL that leads to a phishing site, utilizing a newborn domain unaffiliated with CredPago.

![Figure 6: Sample phishing campaign using a “Special Power of Attorney” document](Image description: A sample phishing campaign using a "Special Power of Attorney" document as bait. The email claims to be from CredPago and prompts the recipient to view a document via an embedded URL, which leads to a phishing site.)

**DOCUSIGN - SUBPOENA**
Esignature platforms like DocuSign and Adobe Sign are integral to many organizations, including law firms, for managing electronic agreements and document signings. Threat actors are actively exploiting the trust in these well-known brands to send phishing emails that mimic these services.

In the malicious email campaign observed below (Fig 7), an email masquerading as a DocuSign notification from 'Gibson, Dunn & Crutcher LLP'—a prominent international law firm known for litigation—falsely informs the recipient that a subpoena has been filed against their company which requires review. However, the 'VIEW COMPLETED DOCUMENT' button, ostensibly providing a link to DocuSign for accessing the document, directs users to a credential harvesting site hosted via an IPFS link.

![Figure 7: Sample phishing campaign leveraging fake eSignature platforms for subpoena notice](Image description: A sample phishing campaign leveraging fake eSignature platforms for a subpoena notice. The email appears to be from DocuSign and a law firm, informing the recipient of a subpoena and providing a link to view the document.)

**TRADEMARK SCAM**
The trademark scam targets businesses either holding registered trademarks or those new to the trademark application process, using professionally styled emails purportedly from law firms or trademark experts.

Trustwave SpiderLabs researchers have observed scams featuring a message (Fig 8) allegedly from an intellectual property lawyer, alerting the recipient of a conflicting trademark application with a third party. To instill urgency, the sender demands a response within 24 hours, warning of potential loss of the trademark if not complied with. The message incorrectly cites the Trademark Act of 1946 to underscore its seriousness, although the United States Patent and Trademark Office (USPTO) clarifies that registering a mark is not mandatory. The provided contract number is controlled by the scammer and notably differs from another contract number listed in the signature, which contains legitimate details including a real lawyer's name and a law firm's contact information specializing in trademarks.

![Figure 8: Sample of a trademark email scam](Image description: A sample of a trademark email scam. The email is from an alleged intellectual property lawyer and warns of a conflicting trademark application, demanding a response within 24 hours.)

**LAW FIRM IMPERSONATED IN ‘FINANCIAL SCAM RECOVERY’ FRAUD**
In a somewhat ironic twist, our researchers have identified a scam that targets individuals who have fallen victim to scams, with threat actors claiming they can retrieve the lost funds. These threat actors typically demand an upfront payment or sensitive information before disappearing, exacerbating the victim's financial losses without recovering any funds.

The example below (Fig 9) is an email that poses as 'Lexington Law Firm.' However, the sender's domain does not align with the legitimate domain which should already be a red flag. Such scams often impersonate law firms, government agencies, and other reputable organizations to seem credible.

![Figure 9: Sample of a “Financial Scam Recovery” scam](Image description: A sample of a "Financial Scam Recovery" scam email. The email poses as 'Lexington Law Firm' and claims to offer recovery of lost funds.)

Another red flag in the scam email is its use of a newly registered look-alike domain in the reply-to field, designed to mimic the legitimate domain of the firm closely. The content of the email boasts an affiliation with the largest scam recovery service and offers a free consultation, tactics aimed at attracting more victims. It includes a button which, when clicked, composes an email to the scam-controlled address in the reply-to field.

![Figure 10: Newly registered fake domains involved in the scam](Image description: An image showing newly registered fake domains used in a scam, designed to mimic legitimate domains.)

Additionally, the message lists various types of frauds they purportedly handle, such as wire, investment, cryptocurrency, mining, romance, ICO, loan, and advanced fee scams, further attempting to legitimize the false service offering.

![Figure 11: Sample of the fake services in an attempt to make the message look legitimate](Image description: A sample of fake services listed in a scam email to make the message appear legitimate.)

**IMPERSONATION OF LEGAL SERVICES – SETTLEMENT AND COURT ORDER**
Another phishing campaign that our researchers observed involves a message impersonating legal authorities, claiming that the recipient needs to review a settlement and court order document. The email includes a PDF attachment that mimics a legitimate legal document, with its filename echoing the email's subject. However, when opened, the PDF masquerades as a secured OneDrive document. A 'VIEW DOCUMENT' button within the PDF misleadingly directs users to a phishing website designed to harvest their credentials, further illustrating the deceptive nature of the scam.

![Figure 12: Sample of another fake legal services claiming a settlement offer](Image description: A sample of a fake legal services email claiming a settlement offer. The email includes a PDF attachment that leads to a phishing website.)

Trustwave SpiderLabs have observed many more phishing campaigns and our researchers have been actively monitoring the evolution of phishing techniques as they have become more complex. Our researchers have published many relevant articles to keep track of this threat such as: AI-based Phishing attacks, HTML Smuggling, RPMSG phishing delivery, QR code phishing techniques, Cloudflare R2 public buckets phishing delivery, and new techniques in malicious PDF delivery.

**Mitigations to Reduce Risk**
- **Conduct security awareness sessions**: Educate employees about the latest phishing tactics and techniques. These lessons should include all the basic red flags, and also cover newer techniques such as "Quishing" and AI-generated phishing emails.
- **Consistently conduct mock phishing tests**: Assess the effectiveness of anti-phishing training and retrain repeat offenders.
- **Implement robust anti-spoofing measures**: Deploy technologies on email gateways. Deploy layered email scanning with a solution like MailMarshal to provide better detection and protection.
- **Leverage web filtering and categorization technologies**: Block access to malicious websites that could potentially be used to download phishing pages and malware.
- **Perform routine security audits**: Audit IT applications and infrastructure to identify and rectify vulnerabilities that attackers could exploit in phishing campaigns.
- **Enable multi-factor authentication (MFA)**: Provide an additional layer of protection for accounts.
- **Restrict access**: Limit the access of assets and sensitive data with the principle of least privilege.

##### Logging in

**The Threat**
While brute-forcing weak passwords or exploiting unchanged default credentials can gain an attacker access, they more commonly use stealthier tactics. These include phishing emails designed to trick employees into giving up login details, drive-by downloads that infect machines through compromised websites, exploiting software vulnerabilities, or even buying pre-existing access to the network from underground marketplaces.

**Trustwave SpiderLabs Insights**
As discussed in the previous section (Initial Foothold: Phishing, Spam & Scams), phishing is the most widespread tactic to gain initial access. Here attackers focus not on software or system vulnerabilities, but on manipulating individuals. This is supported by our client dataset (Fig 13) where initial access vectors used in the attacks mostly relied on Phishing with Exploitation of Public-Facing Applications following next.

![Figure 13: Initial access techniques observed by Trustwave in our professional services client base](Image description: A bar chart showing initial access techniques observed by Trustwave in their professional services client base. T1566 Phishing accounts for 93%, and T1190 Exploit Public-Facing Application accounts for 7%.)

This section will explore some additional phishing approaches as well as other common techniques threat actors use are leveraging valid accounts such as through access brokers and exploiting vulnerabilities.

**PHISHING-AS-A-SERVICE IN PROFESSIONAL SERVICES**
Phishing-as-a-Service (PaaS) is a model where threat actors offer phishing campaigns as a service which ironically is similar to the business approach of some professional services organizations.

The rise of phishing-as-a-Service models like Tycoon Group has made sophisticated phishing attacks accessible to even unskilled wannabe threat actors. The ease of use of these platforms is evident in the increased frequency of phishing attacks utilizing such services. Tycoon Group's PaaS, marketed on Telegram, offers features that claims to be capable of bypassing Microsoft two-factor authentication. The group utilizes trusted domains and cloud-based services to mask the true URLs of their phishing landing pages.

![Figure 14: Tycoon Group Phishing-as-a-Service marketed on Telegram](Image description: A screenshot of a Telegram post marketing the Tycoon Group Phishing-as-a-Service.)

The Tycoon PaaS Group which has been active since August 2023, has been implicated in multiple phishing attacks in the professional services sector including a major global law firm. In this campaign, a Tycoon “affiliate” employed paperless.io (a contract management software company) to disseminate a phishing link disguised as a document copy (Fig 15) and audit trail.

![Figure 15: The phishing email leading to Tycoon Group Phishing-as-a-Service landing page.](Image description: A phishing email that leads to a Tycoon Group Phishing-as-a-Service landing page. The email is disguised as a document copy and audit trail.)

The attack chain (Fig 16) typically begins with a phishing campaign using trusted domains and cloud-based services to obscure the true destination URL of the main phishing landing page.

![Figure 16: Phishing attack chain using the Tycoon Group PaaS](Image description: A flowchart illustrating the phishing attack chain using the Tycoon Group PaaS. It shows the steps from phishing email to the victim entering credentials on a fake login page.)

Upon clicking the link, users are redirected to a web domain controlled by the Tycoon affiliates, where a JavaScript checks for human interaction via Cloudflare. After confirming a user is not a bot, the JavaScript unveils a fake sign-in page, tailored to the phishing theme chosen by the subscriber, such as mimicking a Microsoft 365 login page.

Tycoon Group's phishing pages also feature WebSocket technology for efficient data transmission, highlighting the sophistication and accessibility of phishing-as-a-service models that enable even unskilled criminals to launch advanced phishing campaigns. The examples below show a Tycoon PaaS admin page (Fig 17) as well as the campaign settings (Fig 18) of an affiliate.

![Figure 17: Tycoon Group Phishing-as-a-Service admin page](Image description: A screenshot of a Tycoon Group Phishing-as-a-Service admin page.)

![Figure 18: Tycoon Group phishing campaign settings](Image description: A screenshot of Tycoon Group phishing campaign settings.)

In another example, an Investment Management Services client was targeted by a phishing attack facilitated by the Greatness PaaS platform. The phishing email was crafted to convincingly mimic a legitimate DocuSign notification, using an image overlay that included the phrase "Non-Disclosure Agreement" to instill urgency and prompt immediate action from recipients.

![Figure 19: Phishing email crafted to mimic a DocuSign notification](Image description: A phishing email crafted to mimic a DocuSign notification, with an overlay of "Non-Disclosure Agreement".)

Clicking the email's URL led to a phishing landing page hosted by the Greatness platform, which has been operational since mid-2022 and was developed by a threat actor known as "fisherstell." This service is marketed at $120 per month, payable in Bitcoin, and provides a comprehensive infrastructure for conducting phishing campaigns. Below is an example of a Greatness PaaS admin login page (Fig 20).

![Figure 20: Greatness PaaS admin login page](Image description: A screenshot of a Greatness PaaS admin login page.)

**VALID ACCOUNTS AND ACCESS BROKERS**
Trustwave researchers found many offerings in valid accounts and access credentials pertaining to infrastructure, networks, and systems related to professional services organizations on the Dark Web. Initial Access Brokers, currently very active in underground marketplaces and forums, were seen offering data that could potentially lead to unauthorized access to various target organizations. Here are some notable examples that our research team have found:

**Big 4 Access Logs for Sale in Underground Marketplaces**
Russian Market, a well-known online marketplace, has become a hub for access brokers, especially those targeting the accounting and consulting sectors. In the past year, nearly 10,000 items related to the "Big Four" accounting firms have been listed, primarily logs (Fig 21) containing sensitive infrastructure details, individual user credentials and personal information.

![Figure 21: Distribution of “Big 4” logs offered on the Russian Market](Image description: A pie chart showing the distribution of "Big 4" logs offered on the Russian Market. Deloitte accounts for 73%, PwC for 14%, KPMG for 9%, and EY for 4%.)

These offerings represent a significant threat as they could be used to access sensitive corporate data, proprietary information, and internal systems. Threat actors use these data to execute attacks like credential stuffing, and business email compromise (BEC).

Based on our review of the marketplace data, our researchers have identified that threat actors are purportedly offering pilfered credentials associated with the following domains:
- auth.dpass.us.deloitte.com
- account.deloitte.com
- usijobs.deloitte.com
- kiapplicationform.kpmg.in
- kcheckcp.kpmg.in
- stage-gstpilot.in.kpmg.com
- login.pwc.com
- pwc365.pwc.com
- deg.fedsvc.pwcinternal.com
- globalaccess.ey.com
- globalone.ey.com
- payroll-ktp.ey.com

![Figure 22: Domains found in the logs being sold](Image description: A list of domains found in the logs being sold on underground marketplaces.)

Another concerning log that our researchers identified pertains to PwC, with the victim hailing from Saudi Arabia. Based on the visited domains, it appears the victim is associated with governmental or legal/audit operations.

![Figure 23: Associated domains with credentials offered on the Russian Market](Image description: A list of associated domains with credentials offered on the Russian Market, including PwC, governmental domains, and other services.)

**EXPLOITING PUBLIC-FACING APPLICATIONS**
Professional services firms are exposed to public-facing exploits due to the nature of the services these organizations provide. By its nature, this sector typically acts as third parties service providers to many organizations worldwide and in order to provide these services more efficiently, many have moved their infrastructure online.

In a recent Shodan review, our researchers noted over 55,000 exposed devices (Fig 24) that can be considered as part of the professional services sector. Though this is lower compared to other industries that we have reviewed, there is still significant exposure to assets that could lead to potential compromise.

![Figure 24: Publicly accessible devices in the professional services sector](Image description: A bar chart showing the number of publicly accessible devices in the professional services sector, as identified by Shodan.)

In the next section, we will explore the implications of this exposure and how threat actors might use this attack surface to gain initial access through vulnerabilities and exploits.

**Mitigations to Reduce Risk**
- **Ensure proper security controls around account management**: Enforce strong password policies, enable MFA for all users, and perform regular user access reviews.
- **Regularly monitor external access points**: Review logs for unusual activities and conduct periodic audits of network infrastructure.
- **Educate system users**: Implement a training program on the risks of phishing, spam, and scams. Utilize simulated phishing exercises.
- **Regularly monitor Dark Web sites**: Put procedures in place to respond to possible breaches, such as changing affected credentials.
- **Restrict access**: Enforce the principle of least privilege.
- **Enforce proper password hygiene**: Ensure consistent password complexity requirements and securely store credentials.
- **Encrypt credentials**: Encrypt credentials when used in scripts.
- **Disable default guest accounts and local administrator accounts**: Limit administrative privileges.
- **Use LAPS on Windows systems**: Implement Privileged Access Management (PAM) and Privileged Identity Management (PIM) solutions.

##### Vulnerability Exploitation

**The Threat**
Vulnerability exploitation is a critical concept in information security. It describes how attackers leverage software bugs (vulnerabilities) to bypass security controls and gain unauthorized access to systems or data. These vulnerabilities can encompass various types, such as SQL injection or cross-site scripting (XSS).

Attackers develop specialized software (exploits) to take advantage of vulnerabilities. Once exploited, attackers can introduce malicious payloads like malware. Fortunately, software vendors release patches to fix vulnerabilities and prevent exploitation. However, timely patching by organizations is crucial to maintaining a strong security posture.

It's important to note that not all hacking is malicious. Ethical hackers (penetration testers) identify vulnerabilities with permission to help organizations improve their security.

**Trustwave SpiderLabs Insights**
By actively monitoring our professional services clients, Trustwave SpiderLabs identified the most common exploits targeting our clients. Based on our dataset, the exploit procedures observed were Cloud Instance Metadata Service (IMDS) Abuse and SQL Injection. This is expected as web applications and online cloud environments are used extensively in the professional services sector.

![Figure 25: Most common exploits detected through Trustwave active monitoring](Image description: A bar chart showing the most common exploits detected through Trustwave active monitoring. Cloud Instance Metadata Service Abuse accounts for 88%, and SQL Injection accounts for 12%.)

Additionally, Trustwave SpiderLabs also encounters and analyzes various attacks through our specialized incident response, OSINT, and Dark Web research. Our review of Shodan, which scans all public IP addresses on the Internet, revealed over 55,000 devices associated with the professional services sector. The majority of the services running on these devices (Fig 26) were web services (HTTPS/HTTP). Others include