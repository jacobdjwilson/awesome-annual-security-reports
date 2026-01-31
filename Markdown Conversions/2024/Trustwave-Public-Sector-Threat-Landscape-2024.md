# 2024 Public Sector Threat Landscape

The official report URL is: https://www.trustwave.com/en-us/services/threat-intelligence-as-a-service/

## Table of Contents
- [Executive Summary](#executive-summary)
- [Emerging and Prominent Trends](#emerging-and-prominent-trends)
  - [Double-Edged Sword of Emerging Technologies](#double-edged-sword-of-emerging-technologies)
  - [Convergence of IT and OT in Critical Infrastructure](#convergence-of-it-and-ot-in-critical-infrastructure)
  - [Access and Data Brokers and the Dark Web](#access-and-data-brokers-and-the-dark-web)
- [Dissecting the Attack Flow for the Public Sector](#dissecting-the-attack-flow-for-the-public-sector)
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
    - [Exfiltration / Post Compromise/ Impact](#exfiltration--post-compromise-impact)
- [Key Takeaways and Recommendations](#key-takeaways-and-recommendations)

# Executive Summary

Societies depend on government institutions to deliver stability, continuity, and security. However, cyberattacks can disrupt these vital functions. Robust cybersecurity is the cornerstone of public trust. It ensures the vast amount of sensitive data governments hold, which underpins the smooth operation of society, remains safe.

The effects of public sector cyberattacks can differ starkly from those targeting private corporations. Breaches can disrupt essential services that citizens rely on daily, from healthcare and social security to law enforcement and national defense. This can upset the very fabric of society and erode public confidence in government institutions, potentially hindering cooperation and creating a climate of fear and uncertainty. The risk to individuals is compounded by the need for us all to provide large quantities of our personal information to the government.

Furthermore, successful cyberattacks on critical infrastructure, such as power grids or transportation systems, can have a ripple effect, causing widespread economic disruption, jeopardizing public safety, and even endangering lives.

In March 2024, the White House stated that critical infrastructure, specifically water and wastewater systems, are major targets for state-sponsored threat actors. In May 2023, the Five Eyes intelligence alliance (US, UK, Canada, Australia, New Zealand) and Microsoft said a state-sponsored Chinese hacking group was spying on US critical infrastructure organizations. In October 2023, a ransomware attack by Rhysida Group forced the UK's national library to close and will cost it 40% of their financial reserves to recover after they refused to pay the ransom.

Public sector cybersecurity is a complex landscape with a number of unique factors, including:

*   **Legacy and Diverse Systems**: Public sector agencies often rely on outdated legacy systems that were built without modern cybersecurity threats in mind. These systems can be difficult and expensive to patch or upgrade, and many are managed by private entities, with very little standardization, making them prime targets for exploitation.
*   **Focus on Public Service**: In pursuit of public service, government agencies may prioritize accessibility and user convenience over stringent security measures. This pursuit can leave them vulnerable to phishing attacks or social engineering tactics that prey on unsuspecting employees.
*   **Fragmented IT Infrastructure**: Public sector organizations can have complex and sprawling IT infrastructures with multiple departments and agencies using different systems. This fragmentation can create blind spots and make it difficult to implement consistent security policies across the board.
*   **Data Trove**: Public sector agencies hold a massive amount of sensitive data on citizens, including Social Security numbers, financial information, and medical records. This data is highly valuable to cybercriminals who can use it for identity theft, financial fraud, or further cyberattacks.
*   **Siloed Information Stores**: Public sector agencies have traditionally been the keepers of their own data, with a growing requirement to link and pool data, there is a risk of hidden connections being inadvertently exposed.
*   **Limited Budgetary Resources**: Budgetary constraints often restrict the ability of public sector organizations to invest in the latest cybersecurity technologies and skilled personnel. These financial issues leave them vulnerable to attacks that exploit known weaknesses.
*   **Regulatory Compliance**: Public sector agencies are subject to a complex web of regulations governing data privacy and security. Balancing compliance with effective cybersecurity practices can be a challenge.
*   **International Focus**: Public sector networks can be targeted by foreign governments or state-sponsored actors engaged in espionage or cyberwarfare. This adds another layer of complexity to the cybersecurity landscape.

To ensure comprehensive coverage, this report examines cybersecurity challenges facing the public sector globally, which encompasses government institutions (ranging from libraries to national defense) and essential public services (ranging from law enforcement to infrastructure).

Leveraging the expertise of hundreds of security researchers, Trustwave SpiderLabs is uniquely positioned to analyze the evolving threat landscape. Our team identifies tens of thousands of vulnerabilities each year, performs thousands of penetration tests, and analyzes millions of phishing URLs daily.

This comprehensive coverage across information security disciplines – including continuous threat hunting, forensics, incident response, malware analysis, and database security – empowers us to not only understand how breaches occur, but also recommend effective mitigations and controls for organizations.

This report delves into the critical trends impacting the public sector, including the rise of emerging technologies, risks to critical infrastructure, and the increased sale of public sector assets on the Dark Web. We'll then dissect the attack flow specific to public sector entities, providing actionable intelligence, and tailored mitigation strategies at each stage. We will examine many of the most prevalent threat tactics and threat actors, including:

**THREAT ACTORS**
*   LockBit 3.0
*   Medusa
*   Play
*   ALPHV/BlackCat
*   CLOP/Cl0p

**THREAT TACTICS**
*   Phoenix Cyber Group
*   GhostSec Hacking Group / KillNet
*   Anonymous Sudan
*   NoName057(16)
*   RomCom
*   Phishing and Business Email Compromise (BEC)
*   Supply Chain/Third-Party Risk
*   Data Brokers and Access Brokers
*   Powershell-Driven Execution
*   Malware and Ransomware
*   Vulnerability Exploitation
*   Information Warfare and Espionage
*   Social Engineering and User Driven Execution

# Emerging and Prominent Trends

## Double-Edged Sword of Emerging Technologies

**The Threat**
Emerging technologies like generative AI and quantum computing present a double-edged sword for public-sector cybersecurity. While they offer promising possibilities for efficiency and innovation, they also raise significant security concerns should the public sector be slow to adopt them and subsequently left behind.

**What Trustwave SpiderLabs Is Seeing**
AI-powered threats like hyper-realistic misinformation and social engineering attacks could manipulate public opinion and steal sensitive data. Although still in its early stages, Quantum computing could crack current encryption, jeopardizing government communications and citizen data.

However, the public sector can leverage these technologies for good. AI can be used for advanced threat detection, analyzing vast amounts of data to predict and prevent cyberattacks. Automation powered by AI can free up human resources for more complex tasks.

Moreover, the public sector also bears the added burden of adapting regulations and guidance to this evolving landscape. It's crucial to understand that traditional approaches may not be sufficient for the rapid pace of innovation. Here's what the public sector might consider:

*   **Focus on security by design**: Implementing regulations that require developers to prioritize secure coding practices from the outset.
*   **Standardization for post-quantum cryptography**: Encouraging research and collaboration to develop and adopt new, quantum-resistant encryption standards.
*   **Transparency and accountability**: Developing frameworks that hold tech companies accountable for potential security risks associated with their products and services.
*   **International collaboration**: Cyber threats transcend borders. Establishing international cooperation and information sharing is crucial for a unified approach to regulating emerging technologies.

The public sector must navigate this new frontier by fostering innovation while safeguarding its systems and citizens' data. Proactive planning, robust security practices, agile response to threats, and collaboration across sectors will be key to securing the digital future of the public sector.

**Mitigations to Reduce Risk**
*   Leverage AI for advanced threat detection and automation.
*   Regulate for secure-by-design in emerging technologies.
*   Increase transparency across development and hold tech companies accountable for offerings.
*   Foster international collaboration on cyber threats and regulations.
*   Train public sector staff and citizens on AI threats.
*   Implement robust cybersecurity frameworks (zero-trust, MFA, data security).
*   Repeatedly test incident response and business continuity plans to ensure they will work as expected when needed.

## Convergence of IT and OT in Critical Infrastructure

**The Threat**
Critical infrastructure faces a complex web of security threats. The vast number of entities involved in ownership and management, from small local utilities to federal agencies, can contribute to vulnerabilities. Many critical infrastructure systems are decades old and haven't been updated due to cost concerns, making them more susceptible to attack. Additionally, cybersecurity hasn't always been a high priority for infrastructure owners.

These systems are also interdependent, meaning a disruption in one sector like energy can have cascading effects on others. Furthermore, certain critical points within a system are highly vulnerable, and if compromised, can cause widespread outages.

The rise of cyber threats poses a significant danger. The lack of standardized equipment from different vendors can create issues with configuration management and contribute to security gaps. Additionally, the merging of IT and OT systems increases the attack surfaces for criminals. These systems are often inadequately segmented, allowing attackers to move freely within a network. Even reliance on third-party vendors for services and support introduces security risks, as they can be used as a potential pathway into critical infrastructure systems.

Finally, the increasing use of machine-to-machine communication within critical infrastructure creates new physical security concerns, as attackers can potentially exploit these automated systems. The convergence of IT and OT systems further exacerbates these risks, as these systems were not originally designed with security in mind.

**What Trustwave SpiderLabs Is Seeing**
The convergence of IT and OT systems has created new security challenges. Many organizations mistakenly believed their OT systems were isolated from cyber threats because they were air gapped. This led to a relaxed approach to patching and updating legacy systems. This lack of awareness often extends beyond a single entity, creating a widespread issue.

**LIMITED ASSET MANAGEMENT:**
*   Organizations often lack a comprehensive understanding of their OT environment. They may not have a complete inventory of all systems and their configurations, making it difficult to identify vulnerabilities and implement proper safeguards.
*   The diverse nature of OT systems further complicates matters. Different systems may operate on varying protocols and require unique security measures.

**PATCHING CHALLENGES:**
*   Legacy OT systems often present unique patching difficulties. These systems may be one-of-a-kind and critical to operations, making downtime for patching risky.
*   Additionally, the lack of proper testing environments makes it difficult to predict how a patch might impact system functionality.
*   Vendor support can also be unreliable. While vendors may offer patches, their effectiveness can depend heavily on the specific configuration of the system within a given environment.

**RESILIENCE AND RESPONSE:**
*   Building redundancy into critical infrastructure systems is crucial for maintaining resilience in the face of cyberattacks. Having multiple systems allows for continued operation if one system is compromised.
*   If redundancy is not feasible, organizations must have a robust backup and recovery plan in place. This plan should ensure the ability to quickly restore functionality in the event of an attack.

**EVOLVING THREATS AND LIMITED AWARENESS:**
*   The sophistication of cyberattacks varies greatly. While nation-states may launch highly targeted attacks, less skilled attackers may rely on opportunistic tactics. Regardless of the attacker, the vulnerability of critical infrastructure remains the same.
*   Traditionally, OT personnel haven't faced the same level of cyber threats as their IT counterparts. This lack of awareness is slowly changing, but there's still a gap in understanding and preparedness.

**THE ROLE OF GOVERNMENT:**
*   Governments can play a crucial role in assisting critical infrastructure owners and operators. Instead of solely issuing regulations, they can provide resources for technical testing and help entities build resilience and security capabilities.
*   Sharing information collected by the government is also critical. However, this process can be cumbersome, hindering a collaborative approach to cybersecurity.
*   Governments also play a key role in information sharing across industries and organizations, providing a forum to discuss and interchange learnings.

**Mitigations to Reduce Risk**
*   Prioritize a complete understanding of critical infrastructure environment, including OT systems, assets, configurations, and connections.
*   Evaluate and understand the connections and functionalities of all third-party vendors involved in critical infrastructure operations.
*   Acknowledge resource limitations and prioritize protection of the most critical systems and functionalities.
*   Implement continuous monitoring of critical infrastructure systems to identify suspicious activity and potential vulnerabilities.
*   Develop and test comprehensive backup and incident response plans to ensure a swift recovery from cyberattacks.
*   Provide training programs to educate personnel on social engineering tactics and how to identify and prevent them.
*   Conduct penetration or offensive testing to identify weaknesses so they can be mitigated before they are exploited.

## Access and Data Brokers and the Dark Web

**The Threat**
A disturbing trend has emerged on the Dark Web: a significant increase in the sale of public sector assets.

This includes highly sensitive data such as citizen information, law enforcement databases, election data, and more. This proliferation of stolen data poses a serious threat to national security, public safety, and citizen privacy.

**What Trustwave SpiderLabs Is Seeing**
Trustwave researchers found significant volumes of trade in valid accounts and access credentials pertaining to infrastructure, networks, and systems related to public sector organizations on the Dark Web.

Access and Data Brokers, currently very active in underground marketplaces and forums, were seen offering unauthorized access to various infrastructure and applications public sector organizations worldwide.

The types of public sector data offered on the Dark Web range from highly sensitive to seemingly mundane. Here are some of the concerning categories:

*   **Citizen Information**: Social Security numbers, addresses, financial records, medical data – all valuable for identity theft, financial fraud, and targeted attacks.
*   **Law Enforcement Data**: Criminal records, ongoing investigations, witness testimonies – a goldmine for criminals seeking to evade capture or manipulate ongoing cases.
*   **Election Data**: Voter registration rolls, election results, internal communications – could be used to disrupt elections, undermine trust in democratic processes, or target specific voters.
*   **Government Documents**: Classified information, policy blueprints, internal communications – could expose national security secrets, disrupt critical operations, and give adversaries an advantage.

![Threat actor offering Argentinian Municipal Electoral Registry from 2023](Image description)

**Mitigations to Reduce Risk**
*   Databases that store sensitive data should be prioritized for robust security controls. Database security tools like Trustwave’s DbProtect that can flag misconfiguration and user rights can also help reduce risk.
*   Ensure the appropriate level of protection is applied based on the criticality of information. Implement data protection controls such as data encryption in assets that need to be protected.
*   Ensure appropriate segmentation, segregation, and apply Zero Trust principles are in place. Review if the database needs to be accessible to the whole network, or if it can be hidden behind certain applications.
*   Ensure that up-to-date backups are available as a contingency to recover from a worst-case scenario.
*   Monitor the Dark Web regularly for potential compromises and have a robust incident response process to contain and manage incidents.

# Dissecting the Attack Flow for the Public Sector

## Attack Flow Overview

Data breaches and compromises come in many forms, but they often follow a similar pattern. Attackers gain access, escalate privileges, establish a foothold, steal, or destroy data, and then vanish. This analysis focuses on this attack flow within the public sector, drawing on insights from Trustwave SpiderLabs. It also provides actionable steps organizations can take to mitigate these risks.

These recommendations aim to proactively minimize financial losses, reputational damage, regulatory issues, and even physical harm that public sector organizations might face during an attack. The typical sequence of events unfolds as follows:

![Attack Flow Diagram: Initial Foothold -> Initial Payload -> Expansion / Pivoting -> Malware -> Exfiltration / Post Compromise](Image description)

## Attack Flow Steps

### Initial Foothold

This is the step where the attacker successfully triggers a security bypass that will give them the ability to expand their access to suit their motives and goals. This initial foothold can take various forms, ranging from successful phishing attacks to vulnerability exploitation or even logging into public-facing systems using previously acquired credentials.

In this section, we will explore the most common methods through which attackers gain this initial foothold into a public sector organization, like phishing, third-party suppliers, and exploitable vulnerabilities.

#### Phishing, Spam & Scams

**The Threat**
Public sector organizations, just like many others, are particularly vulnerable to phishing attacks. Unlike exploiting software flaws, attackers target the human element. They craft emails designed to manipulate employees, contractors, or anyone with access to critical systems like financial or customer databases. These emails aim to trick the recipient into taking a specific action, such as opening an attachment, clicking a malicious link, or even following instructions that compromise security.

Typical phishing goals:
*   **Credential Theft**: An example of this would be an email that appears to be from the company's admin, containing a link. When the recipient clicks this link, they are prompted to enter their login details under the pretense of accessing important information or job opportunity details.
*   **Malware Insertion**: This is often executed through embedding PowerShell scripts, JavaScript, or enabling Macros in a document.
*   **Triggering Specific Actions**: This could involve convincing the recipient to provide confidential information or perform other actions under the guise of a necessary step for a certain request.

**Trustwave SpiderLabs Insights**
The Trustwave SpiderLabs team keeps a close eye on email threats targeting the public sector. This includes opportunistic (broad) phishing, spear-phishing (targeted) attacks, malware-laden spam, and scams. Notably, we've observed a concerning trend: attackers are constantly refining their tactics and delivery methods, keeping these email-based attacks relevant and impactful.

In the public sector, the top three email attachment file types (Fig 2) commonly received by clients are HTML, Executables, and PDFs, like other sectors. HTML attachments comprised 78% of observed malicious attachments. More than half (45%) of these HTML attachments were found to be credential phishing pages, while the rest were malware droppers, downloaders, or redirectors. PDFs were the second most weaponized file type and lead mostly to malware downloads, or phishing including QR codes with embedded malicious URLs as highlighted in a recent SpiderLabs research article.

![Top malicious attachment filetypes for the public sector: HTML 78%, PDF 11%, EXEW32 8%, Other 2%, JS 1%](Image description)

In a review of our public sector dataset, Trustwave researchers observed several notable phishing campaign themes targeting both the organizations themselves and the public who uses the organizations various services:

**MALICIOUS CAMPAIGNS TARGETING LOCAL GOVERNMENT FINANCE DEPARTMENTS**
Trustwave SpiderLabs researchers noted BEC and phishing campaigns targeting public sector organizations leveraging fake financial documents typically attempting to impersonate CFOs and account officers as lures.

In one example, our researchers discovered BEC emails impersonating Chief Financial Officers (CFOs) for local government units. In the example shown below (Fig 3), threat actors are requesting copies of “AR aging reports,” which are schedules of accounts receivable. These AR aging reports contain unpaid invoices along with the customer details and are used to keep track of customers who haven’t paid for the goods or services. Threat actors leverage these reports to conduct something called Invoice Transaction Fraud. They use this list obtained from the organization to contact indebted customers and arrange for the payment to be transferred to the threat actor account.

![Sample of a CFO impersonation BEC email targeting local government units](Image description)

**MALICIOUS CAMPAIGNS LEVERAGING TAX GOVERNMENT OFFICES**
Trustwave SpiderLabs often see a spike in malicious email campaigns during various tax seasons around the world. For example, we noted a recent spike in tax related phishing emails in Australia. Below is a supposed tax lodgment receipt (Fig 4) from the Australian Taxation Office. Although the headers and message body appear legitimate, this is a phishing email with a malicious HTML attachment.

![Sample of a malicious email mimicking a tax office advisory in Australia](Image description)

Once the user opens the HTML attachment, a fake Office 365 login page is displayed (Fig 5). To appear legitimate, all related Microsoft backgrounds and logos are fetched from an external source. The email and password supplied by the user will be sent to a site prepared by the threat actor for future harvesting.

![Microsoft 365 fake login page used in credential harvesting for the Australia Tax Office phishing campaigns](Image description)

Another tax-related phishing campaign that Trustwave SpiderLabs researchers identified is related to the Inland Revenue public service department of New Zealand. The Inland Revenue Department (IRD) is responsible for collecting tax, providing the government with policy advice, and administering social support services. It has an online portal called “myIR,” where residents can check if they have tax that needs to be settled, tax refunds, or file a tax return, among others. Typically, email notifications are sent to the account holder if there is any communication sent by the department. Below is an example of a phishing email posing as an official IRD communication.

![Phishing disguised as an official communication from New Zealand Inland Revenue Department](Image description)

The phishing email uses a tax refund as a lure to bait the victim into divulging their “myIR” account credentials. The subject and text of the message body do appear very similar to legitimate IRD notifications however, the falseness of the email is obvious as the “From” field does not even bear the name of the department and the embedded link points to an IP address that does not belong to the Inland Revenue Department.

Our researchers also noted another campaign, this time leveraging the Receita Federal do Brasil (Special Department of Federal Revenue of Brazil). This department is the revenue service agency responsible for tax collection, customs inspections and audits, and assistance in the prosecution of various crimes in Brazil.

In another phishing campaign, the threat actors disguised themselves as Receita Federal and used a “CPF” irregularity as a lure to steal the victim’s information. The CPF number or “Cadastro de Pessoas Físicas” is the individual taxpayer registry number in Brazil.

**FAKE GOVERNMENT BIDDING SCAMS**
Trustwave SpiderLabs researchers have also been continually observing fake government bidding scam campaigns. This scams leverages “Request for Quotation” or “Invitation to Bid”-themed phishing scam emails to lure government suppliers and vendors.

A campaign example attempts to leverage what appears to be the Department of Corrections (DCS) of South Africa for RFQ-themed content (Fig 7). As with most RFQ-related scams, the targets are instructed to respond with quotes where sensitive information can potentially be harvested by the threat actors.

![RFQ-themed scam campaign targeting the Department of Corrections (DCS) of South Africa](Image description)

Another bidding scam campaign that our researchers have been monitoring is related to the US Department of Agriculture (USDA). This campaign impersonates the USDA, asking the target to download an attached PDF tender file (Fig 8) that contains bidding instructions.

![Invitation for Bid themed email campaign impersonating an official USDA advisory](Image description)

The threat actors then attempt to trick the user to click the button inside the PDF to start the bidding process. When clicked, the “Bid Now” button and the QR code contained (Fig 9) within the PDF attachment, leads to a fake USDA “procurement website” asking for sensitive data such as email account credentials.

![The PDF attachment from the fake USDA advisory contains a button and a QR code leading for a fake USDA portal](Image description)

**GOVERNMENT REFUND PHISHING**
Our researchers noted a phishing scam campaign leveraging the Australian “MyGov” portal. MyGov is the Australian government's online service that acts as the single point of access to government services and information. Based on our current data set, this is one of the most impersonated “brands” in the public sector.

![Sample of a phishing campaign targeting MyGov users](Image description)

**DISASTER AID-THEMED PHISHING**
Another notable phishing campaign that our researchers have been observing leverages an offer of a fake relief fund for natural disasters as a lure for potential targets.

The phishing message (Fig 11) urges the target to click on the link to verify their benefits claim status, however, this will direct the target to a phishing site that impersonates the “Benefits.gov” website, an official benefits website of the US government. The landing page attempts to harvest personal information such as Social Security Numbers (SSN) and bank account details.

![Phishing campaign impersonating benefits.gov that leverages natural disaster relief fund as a lure](Image description)

**NOTABLE PHISHING TECHNIQUES TARGETING THE PUBLIC SECTOR**
Trustwave SpiderLabs researchers have been monitoring the continued increase in the use of the InterPlanetary File System (IPFS) by threat actors to host and distribute phishing landing pages. The decentralized and low-cost nature of IPFS makes it an attractive option for orchestrating credential phishing. Our researchers have seen campaigns targeting public sector organizations with links to compromised IPFS domains such as dweb.link, ipfs.io, and cloudflare-ipfs.com.

Another prevalent method leveraging IPFS involves phishing emails impersonating reputable entities like Microsoft that uses simple text files (Fig 12) with IPFS links as bait for downloading malicious eFaxes or documents.

![Fake eFax notification email where the IPFS phishing link is contained in the attachment](Image description)

Our researchers have also witnessed numerous campaigns leveraging PDF files embedded with malicious content. Prevalent ones like fake order scams notify recipients of supposed purchases or renewals while directing them to fraudulent customer support scam services. These scams predominantly originate from Gmail accounts and use real-looking sender names like "Your E-Receipt" or "Your Validated E-Invoice."

![Sample of a fake order scam campaign](Image description)

Trustwave has also seen the emergence of 'quishing' or phishing via QR codes. Our researchers have observed QR codes being embedded in PDFs to redirect targets to phishing sites upon scanning. These PDFs often leverage legitimate government communications (Fig 14) as a lure.

![QR code embedded in a PDF attachment](Image description)

Understanding the exposure of the public sector organizations and the public which they cater to is important as phishing attacks have increasingly become complex. Trustwave SpiderLabs researchers have been actively monitoring the evolution of phishing techniques and has published many relevant articles to keep track of this threat such as: AI-based Phishing attacks, HTML Smuggling, RPMSG phishing delivery, QR code phishing techniques, Cloudlare R2 public buckets phishing delivery, and new techniques in malicious PDF delivery.

**Mitigations to Reduce Risk**
*   Conduct security awareness sessions to educate employees about the latest phishing tactics and techniques. This should include all the basic red flags, and cover newer techniques such as "Quishing" and AI-generated phishing emails.
*   Consistently conduct mock phishing tests to assess the effectiveness of anti-phishing training and retrain repeat offenders.
*   Implement robust anti-spoofing measures, including deploying technologies on email gateways. Deploy layered email scanning with a solution like MailMarshal to provide better detection and protection.
*   Leverage web filtering and categorization technologies to block access to malicious websites that could potentially be used to download phishing pages and malware.
*   Perform routine security audits of IT applications and infrastructure to identify and rectify vulnerabilities that could be exploited in phishing campaigns.
*   Enable multi-factor authentication (MFA) to provide an additional layer of protection for accounts.
*   Restrict the access of assets and sensitive data with the principle of least privilege in mind.

#### Logging in

**The Threat**
While brute-forcing weak passwords or exploiting unchanged default credentials can work, attackers more commonly use stealthier tactics. These include phishing emails designed to trick employees into giving up login details, drive-by downloads that infect machines through compromised websites, exploiting software vulnerabilities, or even buying pre-existing access to the network from underground marketplaces.

**Trustwave SpiderLabs Insights**
As discussed in the previous section (Initial Foothold: Phishing, Spam & Scams), phishing is the most widespread tactic to gain initial access to organizations, with attackers focusing not on software or system vulnerabilities, but rather on manipulating the individuals. Other common techniques used by threat actors are leveraging valid accounts, such as through access brokers and exploiting vulnerabilities (Fig 15).

![Initial access techniques observed by Trustwave in our public sector client base: Phishing 80%, Exploit Public-Facing Application 20%](Image description)

**VALID ACCOUNTS AND ACCESS BROKERS**
Trustwave researchers found many trades in valid accounts and access credentials pertaining to infrastructure, networks, and systems related to public sector organizations on the Dark Web. Initial Access Brokers, currently very active in underground marketplaces and forums, were seen offering unauthorized access to various infrastructure and applications public sector organizations worldwide. Here are some notable examples that our research team have found:

**ELECTION SYSTEMS**
In the example below (Fig 16), our researchers identified a threat actor claiming to have access to the Libyan Election system and selling the access for 150K USD. More information about threats and impact on electoral systems is provided later in the “Post-Compromise/Impact” section.

![Threat actor claiming access to the Libyan Election system](Image description)

**GOVERNMENT INFRASTRUCTURE AND WEBSITES**
Our researchers found multiple instances of claims of compromised infrastructure such as web hosting and intranet of various public sector organizations. There were some examples discovered in various underground forums that offered web server hosting access for the Brazilian government containing 100+ websites (Fig 17) and website admin access for the Ministry of Justice of Buenos Aires, Argentina (Fig 18), that even claims to have the ability to modify criminal trial data.

![Threat actor selling access to 100+ governmental websites in Brazil](Image description)

![Administrative access to the website of the Ministry of Justice of Buenos Aires, Argentina](Image description)

**LAW ENFORCEMENT PORTALS**
Trustwave SpiderLabs researchers noted a number of law enforcement access-related offerings in various underground forums. One example claims that the access they are selling allows the buyer access to lookup license plates, firearms, and criminal records (Fig 19) through the Brazil Federal Police infrastructure.

![Threat actor selling “access to” the Federal Police of Brazil](Image description)

In another example, a threat actor is apparently selling a “Paypal Law Enforcement Portal” (Fig 20) which means they are selling a Paypal account used by law enforcement. It is also worth noting that the seller appears to be related to the GhostSec hacking group, a well-known hacktivist group associated with activities against extremist groups.

![The actor selling access to a police portal that could be used to extract and operate PayPal accounts data](Image description)

**EMAIL ACCOUNTS AND ACCESS**
Another notable observation from our researchers is the large demand and offerings for emails and email access for public sector organizations. There were many requests to buy webmail access to intelligence and law enforcement agencies offering “high prices,” (Fig 21) particularly for US and EU organizations.

![The actor is looking for specific law enforcement webmail access](Image description)

Our team has also seen sellers of government and law enforcement email addresses. For example, the offer below (Fig 22) expounds that access to these types of emails can facilitate EDR (Electronic Discovery Requests) and subpoenas, and claims that the emails they are selling are fully functional and able to send and receive messages.

![Then actor sells governmental emails in many countries, offering law enforcement accounts as well](Image description)

Based on Trustwave threat hunting engagements for public sector organizations, researchers observed that threat actors are often able to obtain valid accounts due to a company's inadequate management of user accounts, particularly poorly managed local administrative accounts.

It should be noted that all the above examples were found in various Dark web forums and underground marketplaces. As such, these should be considered as only unverified claims and offers.

**EXPLOITING PUBLIC-FACING APPLICATIONS**
Public sector organizations are exposed to public-facing exploits due to the sheer number and broad scope of public sector organizations worldwide. This sector is huge and includes everything from tiny municipalities to some of the largest organizations in the world. By its nature, the public sector is “public-facing” and many of the services that it provides are now digitized and moving online.

In a recent Shodan review, our researchers noted over 825,000 exposed devices (Fig 23) that can be considered as public sector. In the next section, we will explore the implications of this exposure and how threat actors might use this attack surface to gain initial access through vulnerabilities and exploits.

![Publicly accessible devices in the public sector](Image description)

**Mitigations to Reduce Risk**
*   Ensure that proper security controls are in place around account management. This includes enforcing strong password policies like enabling MFA for all users. Additionally, perform regular user access reviews to identify any unauthorized access.
*   Regularly monitor external access points to the organization (VPN, SSH, RDP, etc.) and review logs for unusual activities. Organizations should also conduct periodic audits of their network infrastructure to identify and address vulnerabilities.
*   Educate system users and implement a training program on the risks of phishing, spam, and scams. Utilize simulated phishing exercises to test user security awareness and phishing readiness.
*   Regularly monitor Dark Web sites and underground marketplaces for possible breaches. Put procedures in place to respond to possible breaches such as changing affected credentials and investigating the scope of the breach.
*   Restrict access to assets and sensitive data based on the principle of least privilege. Ensure that users only have access necessary to perform their job functions.
*   Enforce proper password hygiene and ensure systems follow a consistent password complexity requirement/standard across the organization. Additionally, securely store credentials in password managers or leverage vaults to prevent credential abuse.
*   Encrypt credentials when used in scripts to safeguard sensitive information.
*   Disable default guest accounts and local administrator accounts where possible. Limit the number of users and service accounts with administrative privileges to reduce the risk of account misuse.
*   Use LAPS on Windows systems to manage local accounts. Implement Privileged Access Management (PAM) and Privileged Identity Management (PIM) solutions to deepen defense-in-depth strategy.

#### Vulnerability Exploitation

**The Threat**
Vulnerability exploitation is a critical concept in information security. It describes how attackers leverage software bugs (vulnerabilities) to bypass security controls and gain unauthorized access to systems or data. These vulnerabilities can encompass various types, such as SQL injection or cross-site scripting (XSS).

Attackers develop specialized software (exploits) to take advantage of vulnerabilities. Once exploited, attackers can introduce malicious payloads like malware. Fortunately, software vendors release patches to fix vulnerabilities and prevent exploitation. However, timely patching by organizations is crucial to maintain a strong security posture.

It's important to note that not all hacking is malicious. Ethical hackers (penetration testers) identify vulnerabilities with permission to help organizations improve their security.

**Trustwave SpiderLabs Insights**
Through active monitoring of our public sector clients, Trustwave SpiderLabs identified the most common exploits targeting our clients.

Apache Log4j and MOVEit Transfer continue to be the most common exploit attempts (Fig 24) against public sector organizations based on our active monitoring. Apache Log4j, a notable logging library vulnerability across multiple industries, remains a threat in the public sector with its extensive ecosystem of web-based services and online devices that are publicly accessible.

MOVEit Transfer is notorious for being leveraged by ransomware gangs to exploit multiple organizations across all sectors.

![Most common exploits detected through Trustwave active monitoring: Apache Log4J CVE-2021-44228 80%, MOVEit Transfer Vulnerability CVE-2023-34362 20%](Image description)

In one of the cases that our researchers investigated, we identified an attempt by a threat actor targeting a public sector organization client using the MOVEit transfer vulnerability. The threat actor attempted to drop a web shell (Fig 25) by exploiting a vulnerable host with the MOVEit Transfer software. The exploitation attempt was blocked, and further Open-Source Intelligence (OSINT) investigation revealed that the artifacts collected were known to be used in the Cl0P MOVEit campaigns.

![Trustwave has monitored and responded to MOVEit exploit attempts attempting to drop web shells: 1. Exploit CVE-2023-34362 to drop human2.aspx WebShell, 2. Leverage WebShell to execute commands to target, 3. Exfiltrate data from target to C2 server](Image description)

Trustwave SpiderLabs also encounters and analyzes various attacks through our specialized incident response, OSINT, and Dark Web research. Our review of Shodan, which scans all public IP addresses on the Internet, revealed over 825,000 devices associated with the public sector. The majority of the services running on these devices (Fig 26) were web services (HTTPS/HTTP). Others include SSH, SMTP, and other network management protocols.

![Most common services running in publicly accessible devices in public sector organizations in Shodan: 443, 80, 22, 8443, 25, 2083, 8081, 4443, 2087, 1044