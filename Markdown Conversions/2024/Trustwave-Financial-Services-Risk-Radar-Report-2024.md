# Trustwave Risk Radar Report 2024: Financial Services Sector

## Contents
[Financial Services’ Unique Threat Landscape](#financial-services-unique-threat-landscape)
[Notable & Prominent Trends in Financial Services](#notable-prominent-trends-in-financial-services)
[Growing Risk of Insider Threats](#growing-risk-of-insider-threats)
[Phishing-as-a-Service Goes Mainstream](#phishing-as-a-service-goes-mainstream)
[Ransomware Groups Continue to Target Financial Services](#ransomware-groups-continue-to-target-financial-services)
[Evolution of Emerging Technology: Cryptocurrency and Deepfakes](#evolution-of-emerging-technology-cryptocurrency-and-deepfakes)
[Threat Actor Techniques by Attack Stage](#threat-actor-techniques-by-attack-stage)
[Conclusion & Key Takeaways](#conclusion-key-takeaways)

In 2023, Trustwave released its Financial Services Threat Intelligence Briefing that analyzed the attack flow specific to the financial services sector, offering insight on specific threat actors, actionable intelligence, and recommended mitigations for each stage.

In our 2024 report, the Trustwave SpiderLabs team highlights the unique factors at play in financial services, the significant trends currently affecting the industry, and an overview of the threat actor techniques by attack stage. Additionally, Trustwave SpiderLabs created two complementary deep-dive writeups containing extensive research and analysis on two looming threats: phishing-as-a-service and insider threats.

Recent research by the Ponemon Institute identifies malicious insiders as the costliest type of data breach, with phishing as the second most expensive and the most prevalent. Our in-depth analysis explores why these threats are particularly pervasive in the financial services sector.

5

Key Report Findings for the Financial Services Sector

*   24% of ransomware attacks were ALPHV
*   65% of ransomware attacks were in the US
*   49% of attacks originated from phishing
*   37% of phishing emails contain HTML attachments
*   20% of ransomware attacks were against banking institutions
*   73% of credentials access techniques were brute-force attempts

Figure 1: Cost and frequency of a data breach by initial attack vector; measured in USD millions; percentage of all breaches. Source: Ponemon Institute. The image is a bar chart showing the cost and frequency of data breaches by initial attack vector. The y-axis represents the cost in USD millions, ranging from 3.8 to 5.2. The x-axis represents the percentage of all breaches, ranging from 4% to 18%. The bars are labeled with different attack vectors: Malicious insider, Stolen or compromised credentials, Social engineering, Business email compromise, Unknown zero-day vulnerability, Known unpatched vulnerability, Accidental data loss and lost or stolen device, Physical security compromise, Phishing, Clouds misconfiguration, and System error.

Financial services organizations are a goldmine for cybercriminals. With their abundance of sensitive financial data and large sums of money, these institutions are highly attractive to attackers. Cyberattacks on this sector have surged, as threat actors exploit vulnerabilities to extort, steal, and defraud financial institutions and their customers. The potential for substantial financial gain drives a relentless pursuit of these lucrative targets. According to Ponemon research, the cost of a breach in the financial services sector is $6.08 million, making it the second most expensive sector, just behind healthcare.

## Financial Services’ Unique Threat Landscape

7

### Expanded Regulatory Requirements

*   The European Union’s Digital Operational Resilience Act (DORA) represents a significant shift in how financial institutions are expected to manage and respond to cyber threats. This regulation mandates that organizations must not only implement robust cybersecurity measures but also continuously test their resilience to cyber incidents.
*   DORA, along with other regulations like the GDPR and PCI-DSS, requires financial institutions to maintain comprehensive cybersecurity frameworks, conduct regular audits, and demonstrate their preparedness for potential cyberattacks. Compliance with these regulations ensures that financial institutions maintain high standards of security and operational resilience, directly influencing their cybersecurity strategies.
*   The regulatory landscape extends beyond Europe. Jurisdictions like the United States and Australia have also introduced stringent cybersecurity requirements for financial institutions. In the US, regulations such as the Gramm-Leach-Bliley Act (GLBA) and the Cybersecurity Framework (CSF) impose specific obligations on financial firms. Similarly, Australia’s Privacy Act and the Security of Critical Infrastructure Act (SOCI) mandate robust cybersecurity practices.
*   Complying with multiple overlapping regulations, often with varying requirements and enforcement mechanisms, is extraordinarily intricate in nature.

### Cryptocurrency Evolution

*   As cryptocurrencies gain legitimacy and integration into traditional banking systems increases, the financial services industry faces new cybersecurity challenges. The rise of digital wallets and crypto transactions introduces potential targets for cybercriminals, such as infostealers that focus on capturing private keys and wallet credentials.
*   Financial institutions must adapt by developing robust protection mechanisms for digital assets and ensuring the security of their customers’ cryptocurrency holdings. This includes implementing advanced security protocols for wallet protection, monitoring for suspicious activities, and educating consumers about best practices in managing their digital assets.

> Jersey Financial Regulator Leaks Private Documents in Second Data Breach of 2024
>
> July 2024, Financial Times

### Consumer Protection Considerations

*   The financial services industry is a prime target for various forms of cyber threats aimed at stealing sensitive consumer information. Banking trojans, for instance, can capture login credentials and facilitate unauthorized transfers of funds. Phishing attacks continue to evolve, targeting individuals with sophisticated schemes designed to extract personal and financial information. Additionally, Magecart attacks, which involve injecting malicious code into e-commerce sites to capture credit card data, pose a significant risk.
*   Financial institutions must implement advanced threat detection and response systems, educate their customers on recognizing and avoiding scams, and ensure robust mechanisms are in place to protect consumer data.

### Heightened Risk Aversion

*   Financial institutions operate under a high level of risk aversion due to the potential impact of security breaches on their operations, reputation, and regulatory compliance. This heightened risk sensitivity drives a proactive approach to cybersecurity, with organizations investing in advanced technologies and dedicated teams to preemptively address vulnerabilities.
*   The financial sector’s emphasis on minimizing risks results in stringent security protocols, frequent updates to security measures, and a focus on incident response and recovery planning.

9

### Franchise Model

*   The franchise model in the financial services industry introduces variability in cybersecurity practices across different branches and entities. With different franchisers and franchisees adopting diverse business models, there can be significant disparities in the consistency and effectiveness of cybersecurity policies and their implementation.
*   This fragmentation can lead to uneven protection levels and potential vulnerabilities. Standardizing cybersecurity practices across franchises and ensuring uniform adherence to industry best practices are crucial for maintaining a cohesive and resilient security posture throughout the organization.
*   Ensuring compliance with regulatory requirements across a franchise network can be complex, especially when dealing with different jurisdictions and varying local regulations. This requires a coordinated approach to maintain consistent security and compliance.

With more than 250 security researchers across the globe, the Trustwave SpiderLabs team puts its resources to task in looking into what leads to these breaches. We are uniquely positioned to do so, as we perform over 200,000 hours of penetration tests and uncover tens of thousands of vulnerabilities annually. We also have a dedicated email security team analyzing millions of phishing URLs validated daily, including 10k per day that are uniquely identified by Trustwave SpiderLabs. Our diverse coverage of infosec disciplines, including Advanced Continuous Threat Hunting, Digital Forensics and Incident Response, Malware Reversal, and Database Security, give us insight into identifying how these breaches occur as well as mitigations and controls that your organization can put in place to prevent these compromises.

This report examines the myriads of threats facing the financial services industry. In addition to supplemental reports focused on insider threats and phishing-as-a-service, Trustwave SpiderLabs will offer recommendations to help financial institutions mitigate risks and safeguard their customers and data.

## Notable & Prominent Trends in Financial Services

## Growing Risk of Insider Threats

### The Threat

We explore insider threats in-depth in our accompanying report. At a high level, here are some key points to consider:

Insider threats are often overlooked in an organization’s overall security posture. While news outlets frequently highlight ransomware attacks and data breaches, they often neglect the potential dangers posed by employees.

Unlike external attackers, insiders already have access to critical systems, making it easier for them to bypass traditional security measures. Insider motives can vary widely, including financial gain, personal grievances, or coercion by external threat actors.

Insider threats generally fall into two main categories: unintentional and intentional.

#### Unintentional Insider Threats:

*   Unintentional insider threats can result from negligence or accidents. Negligent threats occur when employees are careless, such as by ignoring updates or security patches.
*   Accidental threats arise from genuine mistakes, such as sending sensitive information to the wrong email address or inadvertently opening a phishing email.

#### Intentional Insider Threats:

*   Intentional insider threats are categorized as malicious or collusive. Malicious insiders actively seek to harm the organization, often for personal benefit or out of grievance.
*   For instance, they might delete critical databases to create operational issues if they feel wronged. Collusive insider threats involve individuals who collaborate with external threat actors or groups to compromise the organization.

11

### What Trustwave Is Seeing

The Trustwave SpiderLabs team conducted a threat hunt to identify behaviors indicative of insider threats. They discovered that 48% of the risky findings were related to T1219 Remote Access Software and T1572 Protocol Tunneling.

Another notable threat vector observed during this campaign was T1052 Exfiltration over Physical Medium, specifically the sub-technique Exfiltration over USB.

Then, the Trustwave SpiderLabs team took to the Dark Web to analyze the demand for malicious insiders, why insiders become malicious, and how threat actors are recruiting.

Several factors drive individuals to become malicious insiders. Financial gain is a primary motivator, as insiders may sell sensitive information or facilitate breaches for profit. Personal grievances, such as dissatisfaction with their employer, can also lead insiders to engage in malicious activities.

Figure 2: Threat actor offers a high salary for PayPal’s insider services. The image is a screenshot of a forum post. The post is from a user offering a high salary to a PayPal employee. The user's nickname, status, and rate are highlighted in gold. The user has a high reputation score of 217, 139 likes, and 89 posts.

The above threat actor offering additional payment to the PayPal employee is both serious and knowledgeable, as evidenced by their salary offer. This individual is a respected forum user with a high reputation score of 217, 139 likes, and 89 posts. The golden highlights on their nickname, status, and rate suggest that they are a high-level, possibly paid account with an escrow deposit, indicating their trustworthiness and influence within the forum.

13

### Mitigations to Reduce Risk

*   **Access and Usage Controls:** Reduce RMM (Remote Monitoring and Management) usage to one tool, enforcing restrictions on authorized accounts and their locations.
*   **Continuous Monitoring:** Implement continuous monitoring of employee activities to detect unusual behavior or access patterns.
*   **Access Controls:** Enforce strict access controls and the principle of least privilege to limit access to sensitive information.
*   **Enhanced Vetting Processes:** Strengthen background checks during the hiring process to identify potential risks.
*   **Anonymity and Reporting:** Create anonymous reporting mechanisms for employees to report suspicious activities without fear of retribution.

> More Than 450K hit by JPMorgan Breach
>
> May 2024, SC Media

## Phishing-as-a-Service Goes Mainstream

### The Threat

We cover phishing-as-a-service in-depth in our accompanying report. At a high level, here are some key points to consider:

Phishing-as-a-Service (PaaS) has emerged as a major cybersecurity threat to the financial sector. This “Cybercrime-as-a-Service” model offers sophisticated phishing tools and services that can be accessed through underground forums and Telegram marketplaces.

Today, many phishing emails targeting corporate networks are part of campaigns driven by PaaS platforms.

### What Trustwave Is Seeing

The accompanying report provides an in-depth analysis of how PaaS operates, its features, and various platforms, including a detailed case study of Tycoon PaaS.

Attackers have increasingly adopted HTML and PDF attachments to transport, hide, and obfuscate phishing URLs. These attachment types are common and often bypass email scanning gateways.

*   HTML attachments can serve as self-contained phishing pages, redirectors to phishing sites, or use HTML smuggling techniques to deploy malware.
*   PDF attachments may include links that redirect to phishing pages or malware downloads, or they might contain QR codes leading to malicious content.

15

### Malicious Email Attachments

Figure 3: Malicious email attachment types; June 2024. The image is a bar chart showing the distribution of malicious email attachment types. The y-axis represents the percentage of each attachment type. The x-axis lists the attachment types: HTML, EXE, PDF, RTF, XLSX, DOCX, PDFCRYPT, VBS, XLSCRYPT, Other. The percentages are: HTML (37%), EXE (29%), PDF (16%), RTF (4%), XLSX (3%), DOCX (3%), PDFCRYPT (3%), VBS (2%), XLSCRYPT (2%), Other (1%).

### Mitigations to Reduce Risk

*   **Advanced Training and Awareness Programs:** Continuously update training to educate employees on the latest phishing tactics and prevention methods.
*   **Layered Email Security:** Tools like Trustwave MailMarshal provide layered protection against email-based threats, capturing all forms of threats to protect an environment and reduce the burden on security teams.
*   **Email Filtering and Analysis:** Use advanced email filters with machine learning to detect anomalies, analyze headers, and assess sender reputation.
*   **Regular Audits and Simulations:** Perform regular security audits and phishing simulations to evaluate and improve organizational readiness against phishing attacks.
*   **Collaboration and Intelligence Sharing:** Engage in industry collaborations to stay updated on emerging phishing trends and share critical security insights.
*   **Hardware-based Authentication:** Implement FIDO2 authentication with cryptographic keys stored on hardware devices to prevent MFA bypass attacks and ensure secure authentication.

## Ransomware Groups Continue to Target Financial Services

### Threat

Ransomware poses a significant and escalating threat to financial institutions and the broader financial services sector. As these organizations handle vast amounts of sensitive data and financial transactions, they are prime targets for cybercriminals seeking to disrupt operations and extract large ransoms. The impact of a ransomware attack on a financial institution can be catastrophic, leading to operational paralysis, substantial financial losses, and severe reputational damage. Attackers often deploy sophisticated encryption methods to lock access to critical systems and data, demanding hefty ransoms in cryptocurrency, which further complicates recovery efforts and legal responses.

The financial services sector is particularly vulnerable due to its interconnected nature and the reliance on complex IT infrastructures. Institutions such as banks, investment firms, and insurance companies manage intricate networks of information systems that, if compromised, can have ripple effects across the entire economy. The downtime caused by ransomware attacks can disrupt not only daily operations but also critical financial transactions, affecting everything from individual bank accounts to international market stability. Moreover, the regulatory environment around financial institutions requires them to adhere to stringent data protection and reporting standards, adding layers of complexity to their response and recovery strategies.

In addition to the direct financial costs and operational disruptions, ransomware attacks on financial institutions can lead to a loss of customer trust and regulatory scrutiny. Customers expect high levels of security and reliability from their financial service providers, and any breach can erode confidence and drive customers to seek more secure alternatives. Regulatory bodies may impose hefty fines and mandate enhanced security measures, further straining the resources of affected institutions.

17

### What Trustwave Is Seeing

Trustwave SpiderLabs analyzed ransomware incidents targeting the financial services sector and identified AlphV and LockBit as the predominant groups operating in this space. Last year, AlphV accounted for 10% of attacks, but this year their share has increased to 24%. Similarly, LockBit’s share was 24% last year, compared to 23% this year.

Figure 4: Top ransomware groups targeting financial services. The image is a bar chart showing the top ransomware groups targeting financial services. The y-axis represents the percentage of attacks. The x-axis lists the ransomware groups: AlphV, LockBit3, Ransomhub, Play, Medusa, Akira, Inc Ransomware, Qilin, Everst, Dispossessor. The percentages are: AlphV (24%), LockBit3 (23%), Ransomhub (13%), Play (9%), Medusa (7%), Akira (6%), Inc Ransomware (5%), Qilin (5%), Everst (4%), Dispossessor (4%).

Though threat actors target companies worldwide, the majority of reported breaches involve organizations from the US, with Brazil and Canada coming in second and third, respectively. The proportion of breaches affecting US companies has increased from 51% last year to 65% this year.

Figure 5: Financial services organizations affected by ransomware by country. The image is a bar chart showing the countries most affected by ransomware attacks in the financial services sector. The y-axis represents the percentage of attacks. The x-axis lists the countries: USA, Brazil, Canada, UK, India, Australia, Indonesia, Italy, France, El Salvador. The percentages are: USA (65%), Brazil (6%), Canada (6%), UK (5%), India (4%), Australia (4%), Indonesia (3%), Italy (3%), France (3%), El Salvador (2%).

Perhaps unsurprisingly, banking is the top target for ransomware attacks, accounting for 20% of incidents, followed closely by the insurance sector at 18%. It’s important to note that no subsector is immune from these attacks. Credit unions are targeted 8% of the time, while loan and legal services, as well as wealth management firms, each face a 6% attack rate. This distribution underscores the need for robust cybersecurity measures across all financial services sectors.

Figure 6: Ransomware attacks by financial services type. The image is a bar chart showing the distribution of ransomware attacks by financial services type. The y-axis represents the percentage of attacks. The x-axis lists the financial services types: Banking, Insurance, Financial Management, Accounting, Credit Union, Investment Management, Credit and Loan Services, Financial Legal Services, Wealth Management, Payment Solutions. The percentages are: Banking (20%), Insurance (18%), Financial Management (13%), Accounting (11%), Credit Union (8%), Investment Management (8%), Credit and Loan Services (6%), Financial Legal Services (6%), Wealth Management (6%), Payment Solutions (4%).

> Data Breach Affects 57,000 Bank of America Accounts
>
> February 2024, American Banker

19

### Mitigations to Reduce Risk

*   **Use Host-Based Anti-Malware Tools:** Deploy anti-malware tools on individual hosts to identify and quarantine specific malware. Be aware that these tools have limitations and may be circumvented by custom malware packages.
*   **Enable and Audit System Logs:** Activate logging on valuable systems and workstations. Implement network logging through flows, Network Monitoring Solutions, or IDS devices on ingress and egress channels. These logs are crucial for identifying potential compromises.
*   **Active Monitoring of Logs:** Regularly monitor logs to detect abnormal behavior or traffic. Establish a baseline of normal activity to make deviations more noticeable, as merely enabling logs without active monitoring diminishes their effectiveness.
*   **Establish a Formal Incident Response Process:** Develop and routinely practice a formal incident response plan to ensure a swift and coordinated reaction to ransomware attacks.
*   **Ongoing Underground and Dark Web Monitoring:** Continuously monitor the underground and dark web for information leakage that might have been overlooked. This can provide early warnings about potential threats or data exposure.

> Prudential Financial Data Breach Impacts 2.5 Million
>
> February 2024, SecurityWeek

## Evolution of Emerging Technology: Cryptocurrency and Deepfakes

### Threat

As emerging technologies advance rapidly, they bring both transformative opportunities and new challenges, particularly in cybersecurity. For the financial services sector, the evolution of cryptocurrencies and the rise of deepfake technology represents a double-edged sword. While these innovations offer enhanced efficiency and new avenues for growth, they also introduce significant security risks that require proactive and sophisticated responses.

Cryptocurrency, once a niche financial product, has become a mainstream asset class, increasingly integrated into traditional financial systems. This integration opens up new attack vectors, including the theft of digital assets and hacking of cryptocurrency exchanges. The EU’s Markets in Crypto-Assets Regulation (MiCA) aims to mitigate these risks by establishing a comprehensive regulatory framework for the crypto-asset market.

Deepfake technology, meanwhile, presents an emerging threat in the form of highly convincing but fabricated digital content. These synthetic media can be used to deceive individuals and organizations, undermining trust and facilitating fraud.

Earlier this year, a finance worker at a multinational firm was tricked into paying out $25 million to fraudsters using deepfake technology to pose as the company’s chief financial officer in a video conference call.

21

### What Trustwave Is Seeing

#### Cryptocurrency Risks:

The surge in cryptocurrency adoption has created several new security challenges:

*   **Wallet Theft:** Digital wallets, essential for storing cryptocurrencies, are prime targets for cybercriminals. Successful attacks can result in the irreversible loss of funds.
*   **Exchange Hacks:** Cryptocurrency exchanges, where users trade digital assets, are increasingly targeted by hackers seeking to exploit vulnerabilities and steal assets on a large scale.
*   **Cryptojacking:** Malicious actors may use infected systems to mine cryptocurrencies without the user’s consent, leading to significant operational disruptions and financial losses.

In February 2024, Trustwave SpiderLabs discovered Ov3r\_Stealer, a malware designed to steal credentials and crypto wallets through Facebook job advertisements.

The observed Ov3r\_Stealer malware is designed to collect and exfiltrate the following data:

Figure 7: Types of cryptowallets the Ov3r\_Stealer malware is designed to exfiltrate. The image is a table showing the types of cryptowallets the Ov3r_Stealer malware is designed to exfiltrate. The table has two columns: Data Type and Location. The rows list the locations of various crypto wallets.

| Data Type       | Location                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  