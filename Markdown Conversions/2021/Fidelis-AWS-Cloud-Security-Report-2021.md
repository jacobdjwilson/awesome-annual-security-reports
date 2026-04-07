# AWS Cloud Security Report 2021

## Table of Contents
- [Introduction](#introduction)
- [Public Cloud Security Concerns](#public-cloud-security-concerns)
- [Cloud Security Concerns](#cloud-security-concerns)
- [Biggest Cloud Security Threats](#biggest-cloud-security-threats)
- [Responsible for Changes](#responsible-for-changes)
- [Remediation Methods](#remediation-methods)
- [Cadence for Managing Remediation](#cadence-for-managing-remediation)
- [Cloud Deployment Strategies](#cloud-deployment-strategies)
- [Challenges Securing Multi-Cloud](#challenges-securing-multi-cloud)
- [Security Dashboards](#security-dashboards)
- [Single Cloud Security Platform](#single-cloud-security-platform)
- [Cloud-Native Security Drivers](#cloud-native-security-drivers)
- [Cloud Security Solutions](#cloud-security-solutions)
- [Cloud Security Budget](#cloud-security-budget)
- [Methodology & Demographics](#methodology--demographics)

---

## Introduction

Cloud security concerns remain high as the adoption of public cloud computing continues to surge in the wake of the COVID crisis and the resulting massive shift to remote work environments.

The 2021 AWS Cloud Security Report is based on a comprehensive survey of 316 cybersecurity professionals to uncover how AWS user organizations are responding to new security threats in the cloud, and what tools and best practices cybersecurity leaders are prioritizing in their move to the cloud.

This year’s survey saw some significant changes in how organizations manage remediation of security and compliance issues with system owners. The reported remediation cadences of real-time, ad-hoc, and before-audit fire drills all declined between 10 and 13 percentage points since 2020. While the numbers for quarterly and weekly remediation cadences stayed the same, these declines indicate positive process improvements.

Key survey findings include:

- More than nine out of ten cybersecurity professionals (95%) confirm they are extremely to moderately concerned about public cloud security.
- Misconfiguration of the cloud platform remains the top concern (71%). Exfiltration of sensitive data came in second (59%), followed by insecure APIs (54%).
- Periodic vulnerability and compliance reports are still the primary method for organizations (58%) to communicate with system owners about security and compliance issues needing remediation. This is followed by automatically opened tickets (47%) using tools such as Jira, ServiceNow, etc.
- Organizations increasingly embrace hybrid cloud (44%) and multi-cloud deployments (43%) for planned redundancy because of commitments to legacy applications in traditional data centers. Single cloud deployments (11%) continue to diminish in importance. Ninety percent of organizations use more than two cloud providers.
- When selecting a cloud security provider, organizations prioritize cost-effectiveness (66%), scalability (52%), ease of deployment (51%), and tools that can be deployed with automation (48%) as the top four criteria.

We would like to thank CloudPassage for supporting this important industry research project.

We hope you find this report informative and helpful as you continue your efforts in securing your journey into the cloud.

Thank you,

Holger Schulze
CEO and Founder
Cybersecurity Insiders

---

## Public Cloud Security Concerns

Cloud security concerns are improving somewhat but remain high as the adoption of public cloud computing continues to surge in the wake of the COVID crisis and the resulting shift to remote work environments. Ninety-five percent of cybersecurity professionals confirm they are extremely to moderately concerned about public cloud security.

![Chart showing 95% of organizations are concerned about cloud security, with breakdown of concern levels: 42% extremely concerned, 29% very concerned, 24% moderately concerned, 5% slightly concerned/not at all concerned.]

---

## Cloud Security Concerns

Despite the increasing security measures already offered by cloud providers, such as Amazon Web Services, cloud users are ultimately responsible for securing their own workloads in the cloud. When asked about their biggest cloud security challenges, cybersecurity professionals in our survey are highlighting the risk of data loss and leakage (67%), threats to data privacy (61%), and accidental exposure of credentials (49%) as the top three security concerns.

![Chart showing top cloud security concerns: Data loss/leakage (67%), Data privacy/confidentiality (61%), Accidental exposure of credentials (49%), Legal and regulatory compliance (46%), Visibility and transparency (43%), Incident response (41%), Data sovereignty/control (36%). Additional factors listed: Lack of forensic data (26%), Business continuity (24%), Liability (23%), Availability of services, systems, and data (22%), Having to adopt new security tools (21%), Disaster recovery (20%), Performance (18%), Fraud (17%), Not sure/other (4%).]

---

## Biggest Cloud Security Threats

This year, we are observing some shifts in what security professionals see as the biggest cloud security threats. While misconfiguration of the cloud platform/wrong set-up remains the top concern (71% from 49% in 2020), exfiltration of sensitive data rose to second place (59%). This is followed by insecure interfaces/APIs (54%, up from 47%), moving from the second highest concern to third place. Unauthorized access dropped from third to fourth place (53%) while external sharing of data remained in fifth place (44%).

![Chart comparing 2020 vs 2021 security threats: Misconfiguration (71%), Exfiltration of sensitive data (59%), Insecure interfaces/APIs (54%), Unauthorized access (53%), External sharing of data (44%). Additional threats: Malicious insiders (40%), Hijacking of accounts (38%), Foreign state-sponsored attacks (36%), Malware/ransomware (34%), Denial of service (27%), Cloud cryptojacking (18%), Theft of service (13%), Lost mobile devices (9%), Other (6%).]

---

## Responsible for Changes

We asked cybersecurity pros who in their organization are accountable for technical changes to systems required to remediate security or compliance problems. The responsibility is spread fairly evenly among system engineers, security engineers, and DevOps engineers. This suggests that there is no single “best practice” yet regarding who should be making changes for security and compliance. While the majority of those responsible for changes are still in a centralized IT, InfoSec, or DevOps organization, 24% have moved to a model with distributed DevOps teams reporting to business units (up 2 points from 22% in 2020).

![Chart showing accountability for technical changes: System engineers (55%), Security engineers (51%), DevOps engineers central (27%), DevOps engineers distributed (24%), Other (4%).]

---

## Remediation Methods

Periodic vulnerability and compliance reports (58%) are still the primary method for organizations to communicate with system owners about security and compliance issues needing remediation. This is followed by automated trouble tickets (47%) that are opened using tools such as Jira, ServiceNow, etc., and scheduled in-person meetings (42%, up from 31% in 2020). It is a positive sign that ad-hoc emails as a remediation method declined to 33% from 40% in 2020.

![Chart showing remediation methods: Periodic reports (58%), Automated tickets (47%), Scheduled meetings (42%), Ad-hoc emails (33%), System owners have access to security tools (32%), System owners operate their own tools (21%), Integrations consume issues directly (19%), Other (4%).]

---

## Cadence for Managing Remediation

This year’s survey saw some significant changes in how organizations manage remediation of security and compliance issues with system owners. The reported remediation cadences of real-time, ad-hoc, and before-audit fire drills all declined between 10 and 13 percentage points in 2021 from 2020. However, the numbers for quarterly and weekly remediation cadences stayed the same, indicating positive process improvements. Of some concern is that monthly remediation cadence increased significantly from 37% to 52% year-over-year.

![Chart comparing 2020 vs 2021 remediation cadences: Before audits (2%), Ad-hoc (33%), Real-time (14%), Daily (10%), Weekly (27%), Monthly (52%), Quarterly (24%).]

---

## Cloud Deployment Strategies

The survey results show that organizations are increasingly embracing hybrid cloud (44%) and multi-cloud deployments (43%) for planned redundancy because of commitments to legacy applications in traditional data centers. Single cloud deployments (11%) continue to diminish in importance. Ninety percent of organizations use two or more cloud providers.

![Chart showing primary cloud deployment strategy: Hybrid (44%), Multi-cloud (43%), Single cloud (11%), Other (2%). Also shows number of cloud providers: One (8%), Two (41%), Three (24%), More than 3 (25%), None (2%).]

---

## Challenges Securing Multi-Cloud

We asked the survey participants what multi-cloud security challenges they are experiencing. Ensuring data protection and privacy for each environment leads the list with 58%. This is followed by the perennial challenge of procuring the right skillset in-house to deploy and manage security solutions across cloud environments (57%) and understanding how different solutions fit together (52%). These results suggest that organizations could reduce complexity and achieve productivity improvements with cloud security and compliance solutions that worked consistently across cloud service vendors.

![Chart showing multi-cloud challenges: Data protection/privacy (58%), Right skills (57%), Understanding solution integration (52%), Loss of visibility/control (46%), Keeping up with change (44%), Understanding service integration options (42%), Selecting right services (35%), Seamless access (28%), Managing costs (28%), Other (3%).]

---

## Security Dashboards

More than half of organizations use between three to six different dashboards to configure cloud security policies (66%). This requirement significantly increases the cost and complexity of managing security across multi-cloud environments and negatively impacts security posture. These results do not take into account the multiple dashboards that security professionals may have to access to secure assets hosted in-house, highlighting the need for vendors to offer comprehensive security solutions for multi-and hybrid cloud deployments.

![Chart showing number of dashboards used: 1-2 (17%), 3-4 (38%), 5-6 (28%), 7-8 (6%), 9-10 (4%), +10 (7%).]

---

## Single Cloud Security Platform

Eight of ten cybersecurity professionals prefer using a single cloud security platform with a single dashboard; they would consider this very to extremely helpful (79%) to comprehensively protect data across cloud environments.

![Chart showing helpfulness of a single dashboard: Extremely helpful (42%), Very helpful (37%), Moderately helpful (15%), Slightly helpful (4%), Not at all helpful (2%).]

---

## Cloud-Native Security Drivers

Organizations recognize the advantages of deploying cloud-native security solutions. New this year, the top-reported driver is better scalability (55%). This is closely followed by faster time to deployment (54%) and reduced efforts for patching and upgrading software, which jumped from fifth place in 2020 (33%) to tie for third with cost savings (42%).

![Chart showing drivers for cloud-based security: Better scalability (55%), Faster deployment (54%), Reduced patching/upgrading (42%), Cost savings (42%), Better performance (39%), Better visibility (37%), Meet compliance (34%), Workloads reside in cloud (33%), Secure app access (31%), Better uptime (31%), Easier policy management (28%), Reduction of appliance footprint (24%), Other (1%).]

---

## Cloud Security Solutions

We asked security professionals what they look for in a cloud security provider. When selecting a cloud security provider, organizations prioritize cost effectiveness (66%), scalability (52%), ease of deployment (51%), and tools that can be deployed with automation (48%).

![Chart showing criteria for cloud security providers: Cost effectiveness (66%), Scalability (52%), Ease of deployment (51%), Automation (48%), Multi-cloud support (47%), Cloud-native tools (44%), Interoperable with on-premises (44%), Manageable platform (43%), Policy customization (42%), Integrates with cloud platforms (41%), Extends on-premises policies (35%), Security uptime (32%), Cloud knowledge (28%), All capabilities under one platform (28%).]

---

## Cloud Security Budget

Cloud customers are recognizing the growing significance of addressing cloud security threats and are investing in cloud security accordingly. Looking ahead in 2021, 55% expect cloud security budgets to increase by a little less than one third, down from 65% in 2020. Forty percent expect their cloud security budgets to remain flat, up from 30% in 2020. Those anticipating their cloud security funding to shrink held steady at only five percent.

![Chart showing budget changes: Increase (55%), Flat (40%), Decline (5%).]

---

## Methodology & Demographics

This AWS Cloud Security Report is based on the results of a comprehensive online survey of 316 cybersecurity professionals, conducted in April 2021, to gain deep insight into the latest trends, key challenges, and solutions for cloud protection. The respondents range from technical executives to managers and IT security practitioners, representing a balanced cross-section of organizations of varying sizes across multiple industries.

![Charts showing demographics: Career Level (Specialist 19%, Director 18%, Consultant 17%, Manager/Supervisor 15%, CTO/CIO/CISO/etc 14%, VP 3%, Other 14%), Department (IT Security 54%, IT Operations 15%, Engineering 8%, Operations 5%, Compliance 4%, Product Management 2%, DevOps 2%, SecOps 2%, Other 8%), Company Size (Fewer than 10 5%, 10-99 13%, 100-499 10%, 500-999 11%, 1,000-4,999 18%, 5,000-10,000 10%, Over 10,000 33%), Industry (Financial Services 23%, Technology 22%, Government 11%, Professional Services 7%, Manufacturing 6%, Education 5%, Telecommunications 5%, Transportation 4%, Healthcare 3%, Other 14%).]

---

CloudPassage®, a Fidelis Cybersecurity® company, safeguards cloud infrastructure for the world’s best-recognized brands in finance, e-commerce, gaming, B2B SaaS, healthcare, biotech, and digital media. Fidelis Cybersecurity combats the full spectrum of cyber-crime, data theft and espionage.

As the leading innovator of Active XDR solutions, Fidelis helps organizations detect, respond and neutralize threats earlier and deploy deception technologies to stop adversaries before they advance across the IT environment. The CloudPassage Halo® platform unifies security and compliance across servers, containers, and IaaS resources across any mix of public, private, hybrid, and multi-cloud environments including Amazon Web Services, Microsoft Azure, and Google Cloud Platform. Fidelis Cybersecurity is trusted by Global 1000s and Governments as their last line of defense. Fidelis Cybersecurity is a portfolio company of Skyview Capital.

www.cloudpassage.com | www.fidelissecurity.com