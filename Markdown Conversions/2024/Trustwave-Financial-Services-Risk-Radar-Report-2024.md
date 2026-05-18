# 2024 Trustwave Risk Radar Report: Financial Services Sector

## Table of Contents
- [Financial Services’ Unique Threat Landscape](#financial-services-unique-threat-landscape)
- [Notable & Prominent Trends in Financial Services](#notable--prominent-trends-in-financial-services)
- [Growing Risk of Insider Threats](#growing-risk-of-insider-threats)
- [Phishing-as-a-Service Goes Mainstream](#phishing-as-a-service-goes-mainstream)
- [Ransomware Groups Continue to Target Financial Services](#ransomware-groups-continue-to-target-financial-services)
- [Evolution of Emerging Technology: Cryptocurrency and Deepfakes](#evolution-of-emerging-technology-cryptocurrency-and-deepfakes)
- [Threat Actor Techniques by Attack Stage](#threat-actor-techniques-by-attack-stage)
- [Conclusion & Key Takeaways](#conclusion--key-takeaways)

In 2023, Trustwave released its Financial Services Threat Intelligence Briefing that analyzed the attack flow specific to the financial services sector, offering insight on specific threat actors, actionable intelligence, and recommended mitigations for each stage.

In our 2024 report, the Trustwave SpiderLabs team highlights the unique factors at play in financial services, the significant trends currently affecting the industry, and an overview of the threat actor techniques by attack stage. Additionally, Trustwave SpiderLabs created two complementary deep-dive writeups containing extensive research and analysis on two looming threats: phishing-as-a-service and insider threats.

Recent research by the Ponemon Institute identifies malicious insiders as the costliest type of data breach, with phishing as the second most expensive and the most prevalent. Our in-depth analysis explores why these threats are particularly pervasive in the financial services sector.

![Chart showing cost and frequency of a data breach by initial attack vector]

Financial services organizations are a goldmine for cybercriminals. With their abundance of sensitive financial data and large sums of money, these institutions are highly attractive to attackers. Cyberattacks on this sector have surged, as threat actors exploit vulnerabilities to extort, steal, and defraud financial institutions and their customers. The potential for substantial financial gain drives a relentless pursuit of these lucrative targets. According to Ponemon research, the cost of a breach in the financial services sector is $6.08 million, making it the second most expensive sector, just behind healthcare.

### Key Report Findings for the Financial Services Sector
- **24%** of ransomware attacks were ALPHV
- **49%** of attacks originated from phishing
- **20%** of ransomware attacks were against banking institutions
- **65%** of ransomware attacks were in the US
- **37%** of phishing emails contain HTML attachments
- **73%** of credentials access techniques were brute-force attempts

---

## Financial Services’ Unique Threat Landscape

### Expanded Regulatory Requirements
- The European Union’s Digital Operational Resilience Act (DORA) represents a significant shift in how financial institutions are expected to manage and respond to cyber threats. This regulation mandates that organizations must not only implement robust cybersecurity measures but also continuously test their resilience to cyber incidents.
- DORA, along with other regulations like the GDPR and PCI-DSS, requires financial institutions to maintain comprehensive cybersecurity frameworks, conduct regular audits, and demonstrate their preparedness for potential cyberattacks.
- The regulatory landscape extends beyond Europe. Jurisdictions like the United States and Australia have also introduced stringent cybersecurity requirements for financial institutions.
- Complying with multiple overlapping regulations, often with varying requirements and enforcement mechanisms, is extraordinarily intricate in nature.

> **Jersey Financial Regulator Leaks Private Documents in Second Data Breach of 2024**
> *July 2024, Financial Times*

### Cryptocurrency Evolution
- As cryptocurrencies gain legitimacy and integration into traditional banking systems increases, the financial services industry faces new cybersecurity challenges. The rise of digital wallets and crypto transactions introduces potential targets for cybercriminals, such as infostealers that focus on capturing private keys and wallet credentials.
- Financial institutions must adapt by developing robust protection mechanisms for digital assets and ensuring the security of their customers’ cryptocurrency holdings.

### Consumer Protection Considerations
- The financial services industry is a prime target for various forms of cyber threats aimed at stealing sensitive consumer information. Banking trojans, for instance, can capture login credentials and facilitate unauthorized transfers of funds. Phishing attacks continue to evolve, targeting individuals with sophisticated schemes. Additionally, Magecart attacks pose a significant risk.

### Heightened Risk Aversion
- Financial institutions operate under a high level of risk aversion due to the potential impact of security breaches on their operations, reputation, and regulatory compliance. This heightened risk sensitivity drives a proactive approach to cybersecurity.

### Franchise Model
- The franchise model in the financial services industry introduces variability in cybersecurity practices across different branches and entities. This fragmentation can lead to uneven protection levels and potential vulnerabilities.

---

## Notable & Prominent Trends in Financial Services

## Growing Risk of Insider Threats

### The Threat
Insider threats are often overlooked in an organization’s overall security posture. Unlike external attackers, insiders already have access to critical systems, making it easier for them to bypass traditional security measures.

**Unintentional Insider Threats:**
- Can result from negligence or accidents. Negligent threats occur when employees are careless, such as by ignoring updates. Accidental threats arise from genuine mistakes.

**Intentional Insider Threats:**
- Categorized as malicious or collusive. Malicious insiders actively seek to harm the organization. Collusive insider threats involve individuals who collaborate with external threat actors.

### What Trustwave Is Seeing
The Trustwave SpiderLabs team conducted a threat hunt to identify behaviors indicative of insider threats. They discovered that 48% of the risky findings were related to T1219 Remote Access Software and T1572 Protocol Tunneling. Another notable threat vector observed was T1052 Exfiltration over Physical Medium.

![Image of a threat actor offering a high salary for PayPal’s insider services]

### Mitigations to Reduce Risk
- **Access and Usage Controls**: Reduce RMM usage to one tool.
- **Continuous Monitoring**: Detect unusual behavior or access patterns.
- **Access Controls**: Enforce the principle of least privilege.
- **Enhanced Vetting Processes**: Strengthen background checks.
- **Anonymity and Reporting**: Create anonymous reporting mechanisms.

> **More Than 450K hit by JPMorgan Breach**
> *May 2024, SC Media*

---

## Phishing-as-a-Service Goes Mainstream

### The Threat
Phishing-as-a-Service (PaaS) has emerged as a major cybersecurity threat. This “Cybercrime-as-a-Service” model offers sophisticated phishing tools and services that can be accessed through underground forums and Telegram marketplaces.

### What Trustwave Is Seeing
Attackers have increasingly adopted HTML and PDF attachments to transport, hide, and obfuscate phishing URLs.

![Chart of malicious email attachment types; June 2024]

### Mitigations to Reduce Risk
- **Advanced Training and Awareness Programs**
- **Layered Email Security**: Tools like Trustwave MailMarshal.
- **Email Filtering and Analysis**: Use machine learning to detect anomalies.
- **Regular Audits and Simulations**
- **Collaboration and Intelligence Sharing**
- **Hardware-based Authentication**: Implement FIDO2.

---

## Ransomware Groups Continue to Target Financial Services

### Threat
Ransomware poses a significant and escalating threat to financial institutions. The impact can be catastrophic, leading to operational paralysis, substantial financial losses, and severe reputational damage.

### What Trustwave Is Seeing
Trustwave SpiderLabs identified AlphV and LockBit as the predominant groups. AlphV accounted for 24% of attacks.

![Chart of top ransomware groups targeting financial services]
![Chart of financial services organizations affected by ransomware by country]
![Chart of ransomware attacks by financial services type]

> **Data Breach Affects 57,000 Bank of America Accounts**
> *February 2024, American Banker*

### Mitigations to Reduce Risk
- **Use Host-Based Anti-Malware Tools**
- **Enable and Audit System Logs**
- **Active Monitoring of Logs**
- **Establish a Formal Incident Response Process**
- **Ongoing Underground and Dark Web Monitoring**

> **Prudential Financial Data Breach Impacts 2.5 Million**
> *February 2024, SecurityWeek*

---

## Evolution of Emerging Technology: Cryptocurrency and Deepfakes

### Threat
The evolution of cryptocurrencies and the rise of deepfake technology represent a double-edged sword. While these innovations offer enhanced efficiency, they also introduce significant security risks.

### What Trustwave Is Seeing
**Cryptocurrency Risks:** Wallet theft, exchange hacks, and cryptojacking.
**Deepfake Threats:** Identity fraud, phishing scams, and reputation damage.

![Table of types of cryptowallets the Ov3r_Stealer malware is designed to exfiltrate]

### Mitigations to Reduce Risk
- **Enhanced Wallet Security**
- **Secure Exchanges**
- **User Education**
- **Advanced Detection Technologies**
- **Employee Training**
- **Incident Response Planning**
- **Industry Collaboration**
- **Regulatory Compliance**
- **Verify Identities**

> **Data Breach Confirmed by Toyota Financial Services**
> *December 2023, SC Media*

> **China’s ICBC, the World’s Biggest Bank, Hit by Ransomware Attack that Reportedly Disrupted Treasury Markets**
> *November 2023, CNBC*

---

## Threat Actor Techniques by Attack Stage

Trustwave SpiderLabs analyzed data from Fusion to understand the path that threat actors take within financial services.

### Initial Access Techniques
- Phishing (T1566): 49%
- Exploit Public-Facing Application (T1190): 31%
- Valid Accounts (T1078): 20%

### Execution Techniques
- Command and Scripting Interpreter (T1059): 54%
- User Execution (T1204): 44%
- Windows Management (T1047): 2%

### Credential Access Techniques
- Brute Force (T110): 73%
- OS Credential Dumping (T1003): 16%
- Multi-Factor Authentication Request Generation (T1556): 7%

### Lateral Movement Techniques
- Remote Services (T1021): 97%
- Use Alternate Authentication Material (T1550): 3%

### Persistence Techniques
- Account Manipulation (T1098): 59%
- Account Creation (T1136): 37%
- Boot or Logon Autostart Execution (T1547): 4%

> **Fidelity National Financial Subsidiary Says 1.3M Affected by November Cyberattack**
> *November 2023, Cybersecurity Dive*

---

## Conclusion & Key Takeaways

The 2024 Trustwave Risk Radar Report underscores the escalating cyber threats faced by the financial services sector. As the industry continues to be a prime target for cybercriminals, the need for comprehensive and proactive security measures has never been greater.

### Key Takeaways
1. **Heightened Threat Landscape**: Financial services are increasingly targeted by sophisticated cyberattacks.
2. **Costly Insider Threats**: Malicious insiders pose a significant risk, being the most expensive type of data breach.
3. **Regulatory Pressures**: Compliance with evolving regulations like the EU’s DORA is crucial.
4. **Emerging Technology Risks**: The rise of cryptocurrencies and deepfake technology introduces new security challenges.
5. **Phishing-as-a-Service**: The proliferation of PaaS platforms has made phishing attacks more accessible.
6. **Proactive Measures**: Continuous monitoring, strict access controls, and background checks are critical.
7. **Ransomware Resilience**: Regular data backups, securing remote desktop services, and updating security patches are key defenses.