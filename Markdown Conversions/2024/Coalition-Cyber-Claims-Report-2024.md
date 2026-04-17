# 2024 Cyber Claims Report

## Table of Contents
- [Executive Summary](#executive-summary)
- [Cybercrime Put All Businesses at Risk](#cybercrime-put-all-businesses-at-risk)
- [Boundary Devices Targeted by Threat Actors](#boundary-devices-targeted-by-threat-actors)
- [Funds Transfer Fraud Counteracted by Clawbacks](#funds-transfer-fraud-counteracted-by-clawbacks)
- [Ransomware Severity Increased Amid Volatile Year](#ransomware-severity-increased-amid-volatile-year)
- [Business Email Compromise Remained Stable](#business-email-compromise-remained-stable)
- [MOVEit Persisted as Third-Party Risk](#moveit-persisted-as-third-party-risk)
- [Mitigating Cyber Risk with an Active Partner](#mitigating-cyber-risk-with-an-active-partner)
- [Methodology](#methodology)

---

## Executive Summary

Technology has become ingrained in modern business and so has cyber risk. Cyber risk is now the most significant concern for business leaders globally.[^1] As a result, businesses of all sizes and industries must take steps to safeguard their critical information from opportunistic threat actors.

For the better part of a decade, cyber insurance providers have been promoting good cyber hygiene and advocating for better risk management decisions — and policyholders are listening. Despite critical vulnerabilities reaching an all-time high and global ransom payments surpassing $1 billion in 2023,[^2] businesses that reinforced their security controls and embraced partnership with cyber insurance providers were generally more secure.

Claims activity in 2023 has validated a belief long-held by Coalition: Volatility across the cyber threat landscape persists (and likely always will), but an active approach to cyber risk management can help reduce claims for businesses and insurance providers. The findings in this report highlight the value and impact of Active Insurance experienced by Coalition policyholders.

### Key takeaways of 2023

- **Cyber claims increased year over year (YoY).** Overall frequency continued to trend upward. Although overall severity decreased in the latter half of the year, it was not enough to offset the first-half spike primarily driven by increased ransomware claims.
- **Cyber claims originated in the inbox.** More than half of all claims were business email compromise (BEC) or funds transfer fraud (FTF), highlighting the importance of email security as a key aspect of cyber risk management.
- **As ransomware payments hit $1 billion globally, Coalition ransomware severity dropped 54%.** Ransomware frequency, severity, and demands dropped in the second half of the year after a surge in the first half, though severity is still up year over year.
- **Businesses using select boundary devices were at greater risk.** Firewalls, virtual private networks, and other devices can help reduce cyber risk. However, boundary devices with known vulnerabilities increased the likelihood of a business experiencing a cyber claim.

Coalition’s 2024 Cyber Claims Report features data and case studies from organizations across the United States. Cyber risk is global, and we believe this report’s trends and risk mitigation strategies are applicable regardless of location. As an active partner in protecting organizations from digital risk, we’re proud to share these insights to help policyholders, brokers, and others in our industry stay informed about the ever-changing threat landscape.

---

## Cybercrime Put All Businesses at Risk

![Chart showing Overall Claims Frequency from 2021-2023]
![Chart showing Overall Claims Severity from 2021-2023]

Cybercrime is a thriving business that adversely impacts the global economy. In 2023, the Federal Bureau of Investigation (FBI) received more than 880,000 complaints of cybercrime with reported losses of $12.5 billion.[^3]

Overall claims frequency increased 13% YoY but remained below the historic high of 2021. Overall claims severity increased 10% YoY to an average loss amount of $100,000, primarily due to a surge of ransomware claims in the first half of the year. However, 52% of all reported matters were handled without any out-of-pocket payments by the policyholder.

![Chart showing Gross Reported Claims by Event Type: FTF 28%, BEC 28%, Ransomware 19%, Other 25%]

Ransomware accounted for just 19% of reported claims, although historically it is the largest source of claims severity. Funds transfer fraud (FTF) and “Other” events increased YoY by 2% and 7%, respectively, while claims related to business email compromise (BEC) decreased by 8% YoY.

Claims frequency increased across businesses of all revenue amounts. Businesses between $25 million and $100 million in revenue saw the sharpest spike, with a 32% increase YoY. Businesses with more than $100 million in revenue saw a 14% increase in frequency, while businesses with less than $25 million in revenue experienced an 8% increase.

![Chart showing Claims Frequency by Revenue]
![Chart showing Claims Severity by Revenue]

Claims severity stabilized in the latter half of the year after a volatile start. After spiking to an average loss amount of more than $236,000 in 1H 2023, businesses with more than $100 million in revenue saw severity nearly cut in half — though still a 21% increase YoY. The significant changes in severity among this cohort are attributable to spikes in ransomware severity in the first half of the year. Severity among businesses with under $25 million in revenue increased 10% YoY, while businesses between $25 million and $100 million saw severity increase by 9%.

The uptick in overall claims frequency and severity among Coalition policyholders[^4] is indicative of industry-wide trends, though far less volatile than the pandemic-era ransomware boom in 2021.

---

## Boundary Devices Targeted by Threat Actors

The technologies critical to business operations are often prime targets for threat actors. This is especially true of boundary devices, such as routers, firewalls, and virtual private networks (VPNs), that sit between a business and the public internet.

However, boundary devices are also critical tools in reducing a business’ attack surface and protecting other types of risky technology. This is the case with Remote Desktop Protocol (RDP), a protocol used for hosts to communicate. When a boundary device does not secure remote access, it can increase the risk of a business experiencing a cyber attack.

![Chart showing Cisco ASA Relative Claims Frequency]

### Cisco Adaptive Security Appliance
Cisco Adaptive Security Appliance (ASA) devices facilitate remote access and protect networks through a combination of firewall, antivirus, intrusion prevention, and VPN capabilities. Due to the risk associated with these devices, Coalition routinely scans policyholders for exposed Cisco ASA web panels. The relative claims frequency for policyholders using Cisco ASA surged in 2023. Businesses with internet-exposed Cisco ASA devices were nearly five times more likely to experience a claim in 2023.

> **CASE STUDY: Coalition Helps Firm Locate Vulnerable Boundary Device Exploited in Ransomware Attack**
> A financial firm using a Cisco ASA device called Coalition to report a ransomware event. Coalition Incident Response[^5] (CIR) investigated the matter but was unable to determine the root cause because the firm did not have good logging in place. Around the same time, Coalition learned the Akira ransomware gang was using an old vulnerability to compromise Cisco ASA devices, so we began rapidly scanning the internet for vulnerable businesses. Coalition Security Labs used proprietary scanning technology to successfully locate the SSL VPN login for the financial firm’s vulnerable boundary device. This device was determined to be the likely source of compromise, which led to the ransomware attack.

![Chart showing Fortinet Relative Claims Frequency]
![Chart showing RDP Relative Claims Frequency]

### Fortinet
Fortinet offers a variety of boundary devices that are often targeted and exploited by threat actors due to the level of privileged access that can be gained by compromising them. Businesses with internet-exposed Fortinet devices were twice as likely to experience a claim in 2023.

### Remote Desktop Protocol
RDP is a remote access solution built into Windows. Given its ubiquity, RDP is frequently targeted by threat actors who scan the internet looking for exposed instances to exploit. After a decrease in 2022, the risk associated with RDP surged in 2023. Policyholders using internet-exposed RDP were 2.5 times more likely to experience a claim in 2023.

---

## Funds Transfer Fraud Counteracted by Clawbacks

FTF is a low-effort, high-reward way to monetize cybercrime. According to the Federal Trade Commission (FTC), $10 billion was lost to fraud in 2023, with reports of imposter fraud soaring: “Consumers reported losing more money to bank transfers and cryptocurrency than all other methods combined.”[^6]

![Chart showing FTF Frequency]
![Chart showing FTF Initial Severity]

FTF frequency increased 15% YoY. Despite the increase, FTF frequency remains relatively flat over time. FTF initial severity increased 24% YoY to an average loss of more than $278,000.

### Life Cycle of a Coalition Clawback
1. Business unintentionally transfers money to a fraudster.
2. Business quickly reports the incident to Coalition.
3. Coalition leverages existing relationships to track down funds.
4. Government officials and banks freeze the stolen funds.
5. Coalition helps ensure the stolen funds are returned to the business.

Coalition successfully clawed back more than $38 million in fraudulent transfers in 2023. In instances where recovery was successful, we recovered an average amount of $470,000 per FTF claim in 2023.

> **CASE STUDY: Coalition Claws Back $4.9M From Overseas Transfer**
> A real estate firm contacted Coalition after paying a fraudulent invoice. The firm’s vendor had been compromised by a threat actor who emailed instructions to wire a $4.9 million payment to a bank account they controlled in Hong Kong. Within days of the initial transfer, Coalition helped the firm file a report with the FBI, and law enforcement agencies froze the funds before the threat actor could transfer the money to another account. Coalition successfully clawed back all $4.9 million of the stolen money.

---

## Ransomware Severity Increased Amid Volatile Year

Ransomware remains a pain point for businesses and governments alike. In 2023, ransomware payments hit historic highs. Ransomware frequency increased by 15% YoY, largely due to a sharp uptick in frequency in the first half of the year.

![Chart showing Ransomware Frequency]
![Chart showing Ransomware Severity]

Ransomware severity increased 28% YoY for an average loss of more than $263,000. Following historic lows in 2022, ransomware severity spiked in 1H 2023 to more than $369,000. However, Coalition’s ransomware severity dropped 54% in the latter half of the year to an average of nearly $170,000.

![Chart showing Ransom Demands]

The average ransom demand increased 36% YoY to an average of nearly $1.4 million. Among policyholders that experienced a ransomware incident, 40% opted to pay a ransom. Among ransomware claims that resulted in a payment, Coalition successfully negotiated the amount down by an average of 64% of the original demand.[^7]

![Chart showing Ransomware Variants]

> **CASE STUDY: Business Merger Leads to Costly Ransomware Attack**
> A construction business fell victim to a ransomware attack despite having endpoint detection and response (EDR) to alert on anomalous activity in its network. The business had recently acquired a subsidiary and failed to perform sufficient due diligence on the subsidiary’s security controls during the merger. A salesperson clicked on a phishing link that enabled a threat actor to breach the subsidiary and move laterally to compromise the construction business. The threat actor demanded a ransom of nearly $1 million, for which CIR helped negotiate a reduced payment.

---

## Business Email Compromise Remained Stable

BEC frequency has been relatively stable over time and is likely to remain as such, despite a 5% YoY increase. BEC severity decreased 15% YoY to an average loss of more than $26,000.

![Chart showing BEC Frequency]
![Chart showing BEC Severity]

---

## MOVEit Persisted as Third-Party Risk

Claims frequency for "Other" events increased by 21% YoY. Claims severity for Other events increased by 28% to an average loss of more than $53,000.

![Chart showing 'Other' Frequency]
![Chart showing 'Other' Severity]

The most notable third-party compromise event pertains to MOVEit. Progress Software disclosed a critical vulnerability in the file transfer program in May 2023. The Cl0p ransomware gang likely exploited the vulnerability prior to disclosure and used it to compromise hundreds of organizations.

![Chart showing MOVEit Incidents in 2023]

---

## Mitigating Cyber Risk with an Active Partner

The volatility of the cyber threat landscape is inevitable. The frequency and severity of cyber claims continued to trend upward in 2023, yet Coalition found success in minimizing the impact through data-driven risk selection and active engagement with policyholders.

Coalition sits at the intersection of security and insurance. Our robust data on cyber threats and claims allow us to create a comprehensive picture of real-time risk.

### Active Insurance
- **ASSESS**: Real-time, external view of cyber risk with customized recommendations.
- **PROTECT**: Identify and prevent new threats with tailored remediation guidance and support.
- **COVER**: Comprehensive coverage to give peace of mind following an attack.
- **RESPOND**: Immediate expert support to minimize impact and speed up recovery.

---

## Methodology

The 2024 Cyber Claims Report is based on reported claims data from January 1 to December 31, 2023. A claim is defined as an adverse cyber event reported by a Coalition policyholder that incurred a gross loss. Our team of data scientists and actuaries used our own internal claims data to complete the analysis.

Coalition uses the reported experience as of six months of age rather than ultimate loss projections. By comparing reported experience evaluated at the same age, we assume the same ultimate development between all periods, allowing for a direct comparison without the bias of future trends skewing the ultimate projections.

---

[^1]: Allianz, Allianz Risk Barometer 2024
[^2]: Chainalysis, Ransomware Payments Exceed $1 Billion in 2023, Hitting Record High After 2022 Decline
[^3]: Federal Bureau of Investigation, Internet Crime Report 2023
[^4]: Insurance products in the United States are offered through Coalition Insurance Solutions, Inc., a licensed insurance producer with its principal place of business in San Francisco, CA (Cal. license #0L76155), acting on behalf of a number of insurance companies and an affiliate of Coalition, Inc.
[^5]: Coalition Incident Response services provided through Coalition’s affiliate are offered to policyholders as an option via our incident response firm panel.
[^6]: Federal Trade Commission, As Nationwide Fraud Losses Top $10 Billion in 2023, FTC Steps Up Efforts to Protect the Public
[^7]: Decrease in ransom amount paid only includes negotiations handled by Coalition Incident Response, an affiliate firm made available to all policyholders via panel selection.