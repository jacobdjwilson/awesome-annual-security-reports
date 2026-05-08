# 2023 Annual Cybersecurity Report: Calibrating Expansion

## Table of Contents
- [APT Campaigns](#apt-campaigns)
- [Ransomware Threats](#ransomware-threats)
- [Cloud and Enterprise Threats](#cloud-and-enterprise-threats)
- [MITRE ATT&CK Detections](#mitre-attck-detections)
- [Threat Landscape](#threat-landscape)

---

## APT Campaigns

The 2023 landscape saw a variety of Advanced Persistent Threat (APT) campaigns targeting government, defense, and technology sectors globally.

### APT28
*   **NTLMv2 hash relay attacks (April 2022 – August 2023):** Targeted organizations in foreign affairs, energy, defense, and transportation. Exploited CVE-2023-23397.
*   **Credential phishing (November – December 2023):** Targeted European government organizations using similar technical indicators to the hash relay campaign.

### Other Notable Campaigns
*   **Gamaredon (Jan–Nov 2023):** Targeted Ukrainian government organizations using Remote Template Injection.
*   **Earth Lusca (Jan–June 2023):** Targeted government and tech sectors in the Philippines, Taiwan, Malaysia, South Africa, Germany, and the USA.
*   **Earth Estries (Jan 2023–present):** Targeted government departments in Southeast Asia, Central Asia, and the Balkans. Deployed the "SprySOCKS" Linux backdoor.
*   **Kimsuky (April 2022, April–May 2023):** Targeted individuals related to the DPRK and diplomatic/military organizations.
*   **Void Rabisu (June–August 2023):** Targeted European military and political leaders using the zero-day CVE-2023-36884.
*   **Turla (July 2023):** Targeted Ukrainian diplomatic and military organizations using Capibar and Kazuar malware.
*   **APT34 (August 2023):** Targeted organizations in Saudi Arabia with new espionage-focused malware.
*   **Mustang Panda (August 2023–present):** Targeted Philippine government organizations using DLL sideloading.
*   **APT38 (May–September 2023):** Targeted cryptocurrency and investment firms.
*   **Konni Group (November 2023):** Targeted companies in the Republic of Korea.
*   **APT29 (November 2023):** Targeted European embassies using the WinRAR vulnerability CVE-2023-38831.

---

## Ransomware Threats

### Tactics to Watch
*   **Remote Encryption:** Mapping drives to encrypt endpoints without lateral movement.
*   **Intermittent Encryption:** Encrypting chunks of data to speed up the process and complicate decryption.
*   **EDR Bypass:** Using unmonitored virtual machines (VMs) to navigate and encrypt files.
*   **Multi-ransomware Attacks:** Initial access brokers selling access to multiple ransomware groups.

### Statistics
*   ![Chart showing total ransomware detections from 2019 to 2023, showing a peak in 2021 and a decline through 2023.]
*   **Operating Systems:** Windows remains the primary target, though Linux-targeted attacks saw a significant surge in 2022 before stabilizing in 2023.
*   **Top Countries:** Thailand, United States, Turkey, Taiwan, and India.
*   **Top Industries:** Banking, Government, Technology, and Retail.
*   **Top Families:** StopCrypt and LockBit remain the most prolific.

---

## Cloud and Enterprise Threats

### Home Network Security
*   ![Chart showing top home network security events, led by Brute-Force Login attempts.]
*   **Affected Devices:** Desktops and laptops recorded the highest number of inbound attack detections, followed by smartphones and tablets.
*   **Vulnerability by Vendor:** Adobe, Microsoft, and D-Link were the top vendors associated with detected vulnerabilities.

---

## MITRE ATT&CK Detections

### Top 5 Tactics (Overall)
1.  **Defense Evasion (TA0005)**
2.  **Command and Control (TA0011)**
3.  **Initial Access (TA0001)**
4.  **Persistence (TA0003)**
5.  **Impact (TA0040)**

### Living-Off-The-Land (LotL)
Threat actors continue to favor well-known tools like **Mimikatz** and **Cobalt Strike** for their reliability in harvesting data and maintaining control while evading detection.

---

## Threat Landscape

### Malware Detection
*   **Top Countries:** Japan, United States, India, Italy, and Brazil.
*   **Top Targeted Industries:** Government, Healthcare, Manufacturing, Education, and Banking.
*   **Top Malware Families:** CoinMiner (cryptocurrency mining) surpassed Webshells in 2023.

### Email Threats
*   ![Chart showing email threat statistics, noting a decrease in malicious URLs but an increase in Business Email Compromise (BEC) and malware detections.]
*   **Spam Attachments:** PDF files were the most common spam attachment type in 2023.

### Threats Blocked
*   Total threats blocked reached **161 billion** in 2023, a 10% increase from 2022.
*   While network and email-based detections (WRS/ERS) have decreased, file-based detections (FRS) have consistently increased, suggesting a shift toward more targeted, high-quality attacks.

### Vulnerabilities
*   **Zero-Day Advisories:** 1,913 published ZDI advisories in 2023.
*   **Riskiest CVEs:** CVE-2023-24880, CVE-2023-21823, and CVE-2023-23376.

### Risk Events
*   **Top Events:** Risky Cloud App Access (82.9 billion) and Risky Website Access (18.8 billion).
*   **Top Countries:** United States, India, Brazil, Great Britain, and Germany.

---

## Recommendations for Lowering Risk
1.  Apply the latest patches and upgrade software versions.
2.  Implement prevention rules to protect against known vulnerabilities.
3.  Optimize security settings within the current environment.
4.  Restrict access to risky applications and websites.
5.  Enforce strong password policies and enable Account Lockout policies.
6.  Restrict user account privileges on at-risk devices.

[^1]: Industry data counts are limited to customers who have elected to provide details pertaining to their business sectors.