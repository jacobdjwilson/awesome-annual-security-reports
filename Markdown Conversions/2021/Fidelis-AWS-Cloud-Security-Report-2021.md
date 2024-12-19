# AWS CLOUD SECURITY REPORT 2021

## Table of Contents
  * [INTRODUCTION](#introduction)
  * [PUBLIC CLOUD SECURITY CONCERNS](#public-cloud-security-concerns)
  * [CLOUD SECURITY CONCERNS](#cloud-security-concerns)
  * [BIGGEST CLOUD SECURITY THREATS](#biggest-cloud-security-threats)
  * [RESPONSIBLE FOR CHANGES](#responsible-for-changes)
  * [REMEDIATION METHODS](#remediation-methods)
  * [CADENCE FOR MANAGING REMEDIATION](#cadence-for-managing-remediation)
  * [CLOUD DEPLOYMENT STRATEGIES](#cloud-deployment-strategies)
  * [CHALLENGES SECURING MULTI-CLOUD](#challenges-securing-multi-cloud)
  * [SECURITY DASHBOARDS](#security-dashboards)
  * [SINGLE CLOUD SECURITY PLATFORM](#single-cloud-security-platform)
  * [CLOUD-NATIVE SECURITY DRIVERS](#cloud-native-security-drivers)
  * [CLOUD SECURITY SOLUTIONS](#cloud-security-solutions)
  * [CLOUD SECURITY BUDGET](#cloud-security-budget)
  * [METHODOLOGY & DEMOGRAPHICS](#methodology--demographics)

## INTRODUCTION
Holger Schulze
CEO and Founder
Cybersecurity Insiders

Cloud security concerns remain high as the adoption of public cloud computing continues to surge in the wake of the COVID crisis and the resulting massive shift to remote work environments.

The 2021 AWS Cloud Security Report is based on a comprehensive survey of 316 cybersecurity professionals to uncover how AWS user organizations are responding to new security threats in the cloud, and what tools and best practices cybersecurity leaders are prioritizing in their move to the cloud.

This year’s survey saw some significant changes in how organizations manage remediation of security and compliance issues with system owners. The reported remediation cadences of real-time, ad-hoc, and before-audit fire drills all declined between 10 and 13 percentage points since 2020. While the numbers for quarterly and weekly remediation cadences stayed the same, these declines indicate positive process improvements.

Key survey findings include:
* More than nine out of ten cybersecurity professionals (95%) confirm they are extremely to moderately concerned about public cloud security.
* Misconfiguration of the cloud platform remains the top concern (71%). Exfiltration of sensitive data came in second (59%), followed by insecure APIs (54%).
* Periodic vulnerability and compliance reports are still the primary method for organizations (58%) to communicate with system owners about security and compliance issues needing remediation. This is followed by automatically opened tickets (47%) using tools such as Jira, ServiceNow, etc.
* Organizations increasingly embrace hybrid cloud (44%) and multi-cloud deployments (43%) for planned redundancy because of commitments to legacy applications in traditional data centers. Single cloud deployments (11%) continue to diminish in importance. Ninety percent of organizations use more than two cloud providers.
* When selecting a cloud security provider, organizations prioritize cost-effectiveness (66%), scalability (52%), ease of deployment (51%), and tools that can be deployed with automation (48%) as the top four criteria.

We would like to thank CloudPassage for supporting this important industry research project. We hope you find this report informative and helpful as you continue your efforts in securing your journey into the cloud.

Thank you,
Holger Schulze

## PUBLIC CLOUD SECURITY CONCERNS
**How concerned are you about the security of public clouds?**

*A pie chart visually represents the following data:*
*   **24%** Extremely concerned
*   **42%** Very concerned
*   **29%** Moderately concerned
*   **5%** Slightly concerned
*   **0%** Not at all concerned

**95%** of organizations are concerned about cloud security.

Cloud security concerns are improving somewhat but remain high as the adoption of public cloud computing continues to surge in the wake of the COVID crisis and the resulting shift to remote work environments. Ninety-five percent of cybersecurity professionals confirm they are extremely to moderately concerned about public cloud security.

## CLOUD SECURITY CONCERNS
Despite the increasing security measures already offered by cloud providers, such as Amazon Web Services, cloud users are ultimately responsible for securing their own workloads in the cloud. When asked about their biggest cloud security challenges, cybersecurity professionals in our survey are highlighting the risk of data loss and leakage (67%), threats to data privacy (61%), and accidental exposure of credentials (49%) as the top three security concerns.

**What are your biggest cloud security concerns?**

*A bar chart visually represents the following data:*

*   **67%** Data loss/leakage
*   **61%** Data privacy/confidentiality
*   **49%** Accidental exposure of credentials
*   **46%** Legal and regulatory compliance
*   **43%** Visibility and transparency
*   **41%** Data sovereignty/control
*   **36%** Incident response
*   **26%** Lack of forensic data
*   **24%** Business continuity
*   **23%** Liability
*   **22%** Availability of services, systems, and data
*   **21%** Having to adopt new security tools
*   **20%** Disaster recovery
*   **18%** Performance
*   **17%** Fraud (i.e., theft of SSN records)
*   **4%** Not sure/other

## BIGGEST CLOUD SECURITY THREATS
This year, we are observing some shifts in what security professionals see as the biggest cloud security threats. While misconfiguration of the cloud platform/wrong set-up remains the top concern (71% from 49% in 2020), exfiltration of sensitive data rose to second place (59%). This is followed by insecure APIs (54%, up from 47%), moving from the second highest concern to third place. Unauthorized access dropped from third to fourth place (53%) while external sharing of data remained in fifth place (44%).

**What do you see as the biggest security threats in public clouds?**

*A bar chart visually represents the following data, comparing 2020 and 2021 responses:*

*   **71%** Misconfiguration of the cloud platform/wrong set-up (2021) - *An increase of 22% from last year*
*   **49%** Misconfiguration of the cloud platform/wrong set-up (2020)
*   **59%** Exfiltration of sensitive data (2021)
*   **54%** Insecure interfaces/APIs (2021)
*   **47%** Insecure interfaces/APIs (2020)
*   **53%** Unauthorized access (2021)
*   **44%** External sharing of data (2021)
*   **42%** External sharing of data (2020)
*   **40%** Malicious insiders
*   **38%** Hijacking of accounts, services, or traffic
*   **36%** Foreign state-sponsored cyber attacks
*   **34%** Malware/ransomware
*   **27%** Denial of service attacks
*   **18%** Cloud cryptojacking
*   **13%** Theft of service
*   **9%** Lost mobile devices
*   **6%** Don’t know/other

## RESPONSIBLE FOR CHANGES
We asked cybersecurity pros who in their organization are accountable for technical changes to systems required to remediate security or compliance problems. The responsibility is spread fairly evenly among system engineers, security engineers, and DevOps engineers. This suggests that there is no single “best practice” yet regarding who should be making changes for security and compliance. While the majority of those responsible for changes are still in a centralized IT, InfoSec, or DevOps organization, 24% have moved to a model with distributed DevOps teams reporting to business units (up 2 points from 22% in 2020).

**Who is accountable for actual technical changes to systems that are required to remediate security or compliance problems?**

*A bar chart visually represents the following data:*

*   **55%** System engineers within a central IT operations/hosting ops organization
*   **51%** Security engineers within a central information security organization
*   **27%** DevOps engineers within a central DevOps organization (central DevOps)
*   **24%** DevOps engineers within individual business units (distributed DevOps)
*   **4%** Other

## REMEDIATION METHODS
Periodic vulnerability and compliance reports (58%) are still the primary method for organizations to communicate with system owners about security and compliance issues needing remediation. This is followed by automated trouble tickets (47%) that are opened using tools such as Jira, ServiceNow, etc., and scheduled in-person meetings (42%, up from 31% in 2020). It is a positive sign that ad-hoc emails as a remediation method declined to 33% from 40% in 2020.

**What is the primary method for managing remediation of security and compliance issues with system owners?**

*A bar chart visually represents the following data:*

*   **58%** Periodic vulnerability and compliance reports
*   **47%** Tickets automatically opened in operational tools (e.g., Jira, Service Now, etc.)
*   **42%** Scheduled meetings
*   **33%** Ad-hoc emails
*   **32%** System owners have access to tools operated by information security
*   **21%** Integrations consume issues directly from security tools and auto-remediate
*   **19%** System owners operate their own security and compliance tools
*   **4%** Other

## CADENCE FOR MANAGING REMEDIATION
This year’s survey saw some significant changes in how organizations manage remediation of security and compliance issues with system owners. The reported remediation cadences of real-time, ad-hoc, and before-audit fire drills all declined between 10 and 13 percentage points in 2021 from 2020. However, the numbers for quarterly and weekly remediation cadences stayed the same, indicating positive process improvements. Of some concern is that monthly remediation cadence increased significantly from 37% to 52% year-over-year.

**Outside of critical vulnerabilities, what is the cadence for managing remediation of security and compliance issues with system owners?**

*A bar chart visually represents the following data, comparing 2020 and 2021 responses:*

*   **14%** Before audits (2020)
*   **2%** Before audits (2021)
*   **27%** Ad-hoc (2020)
*   **15%** Ad-hoc (2021)
*   **24%** Real-time (2020)
*   **10%** Real-time (2021)
*   **26%** Daily (2020)
*   **27%** Daily (2021)
*   **33%** Weekly (2020)
*   **37%** Weekly (2021)
*   **37%** Monthly (2020)
*   **52%** Monthly (2021)
*   **43%** Quarterly (2020)
*   **43%** Quarterly (2021)

*10-13 percentage points decline from 2020*

## CLOUD DEPLOYMENT STRATEGIES
The survey results show that organizations are increasingly embracing hybrid cloud (44%) and multi-cloud deployments (43%) for planned redundancy because of commitments to legacy applications in traditional data centers. Single cloud deployments (11%) continue to diminish in importance. Ninety percent of organizations use two or more cloud providers.

**What is your primary cloud deployment strategy?**

*A pie chart visually represents the following data:*

*   **11%** SINGLE CLOUD
*   **44%** HYBRID (e.g., integration between multiple providers, managed as a single cloud)
*   **43%** MULTI-CLOUD (e.g., multiple providers without integration)

**90%** use two or more cloud providers

**How many cloud providers does your organization currently use?**

*A bar chart visually represents the following data:*

*   **8%** One
*   **41%** Two
*   **25%** Three
*   **24%** More than 3
*   **2%** None

## CHALLENGES SECURING MULTI-CLOUD
We asked the survey participants what multi-cloud security challenges they are experiencing. Ensuring data protection and privacy for each environment leads the list with 58%. This is followed by the perennial challenge of procuring the right skillset in-house to deploy and manage security solutions across cloud environments (57%) and understanding how different solutions fit together (52%). These results suggest that organizations could reduce complexity and achieve productivity improvements with cloud security and compliance solutions that worked consistently across cloud service vendors.

**What are your biggest challenges securing multi-cloud environments?**

*A bar chart visually represents the following data:*

*   **58%** Ensuring data protection and privacy for each environment
*   **57%** Having the right skills to deploy and manage a complete solution across all cloud environments
*   **52%** Understanding how different solutions fit together
*   **46%** Loss of visibility and control
*   **44%** Keeping up with the rate of change
*   **42%** Understanding service integration options
*   **35%** Selecting the right set of services
*   **28%** Providing seamless access to users based on their credentials
*   **28%** Managing the costs of different solutions
*   **3%** Other

## SECURITY DASHBOARDS
More than half of organizations use between three to six different dashboards to configure cloud security policies (66%). This requirement significantly increases the cost and complexity of managing security across multi-cloud environments and negatively impacts security posture. These results do not take into account the multiple dashboards that security professionals may have to access to secure assets hosted in-house, highlighting the need for vendors to offer comprehensive security solutions for multi-and hybrid cloud deployments.

**How many dashboards for separate security solutions do your users have to access to configure the policies that secure your enterprise’s entire cloud footprint?**

*A bar chart visually represents the following data:*

*   **4%** 1-2
*   **38%** 3-4
*   **28%** 5-6
*   **17%** 7-8
*   **6%** 9-10
*   **7%** +10

**66%** need to access between three to six dashboards to configure cloud security policies

## SINGLE CLOUD SECURITY PLATFORM
Eight of ten cybersecurity professionals prefer using a single cloud security platform with a single dashboard; they would consider this very to extremely helpful (79%) to comprehensively protect data across cloud environments.

**How helpful would it be to have a single cloud security platform with a single dashboard where you could configure all of the policies needed to protect data consistently and comprehensively across your cloud footprint?**

*A bar chart visually represents the following data:*

*   **2%** Not at all helpful
*   **4%** Slightly helpful
*   **15%** Moderately helpful
*   **37%** Very helpful
*   **42%** Extremely helpful

**79%** of professionals would consider it very to extremely helpful to have a single cloud security dashboard

## CLOUD-NATIVE SECURITY DRIVERS
Organizations recognize the advantages of deploying cloud-native security solutions. New this year, the top-reported driver is better scalability (55%). This is closely followed by faster time to deployment (54%) and reduced efforts for patching and upgrading software, which jumped from fifth place in 2020 (33%) to tie for third with cost savings (42%).

**What are the main drivers for considering cloud-based security solutions?**

*A bar chart visually represents the following data:*

*   **55%** Better scalability
*   **54%** Faster time to deployment
*   **42%** Reduced effort around patches and upgrades of software
*   **42%** Cost savings
*   **39%** Our data/workloads reside in the cloud (or are moving to the cloud)
*   **37%** Better performance
*   **34%** Better visibility into user activity and system behavior
*   **33%** Meet cloud compliance expectations
*   **31%** Need for secure app access from any location
*   **31%** Better uptime
*   **28%** Easier policy management
*   **24%** Reduction of appliance footprint in branch offices
*   **1%** Other

## CLOUD SECURITY SOLUTIONS
We asked security professionals what they look for in a cloud security provider. When selecting a cloud security provider, organizations prioritize cost effectiveness (66%), scalability (52%), ease of deployment (51%), and tools that can be deployed with automation (48%).

**What do you look for in your cloud security provider?**

*A bar chart visually represents the following data:*

*   **66%** Cost effectiveness
*   **52%** Scalable solution
*   **51%** Ease of deployment
*   **48%** Tools can be deployed with automation
*   **47%** Multi-cloud support
*   **44%** Security tools are cloud-native
*   **44%** Interoperable with on-premises solutions
*   **43%** Easily manageable platform
*   **42%** Policy customization
*   **41%** Integrates seamlessly with cloud platforms
*   **35%** Extends on-premises policies to the cloud
*   **32%** Security uptime
*   **28%** Demonstrate cloud knowledge
*   **28%** All capabilities under one platform

## CLOUD SECURITY BUDGET
Cloud customers are recognizing the growing significance of addressing cloud security threats and are investing in cloud security accordingly. Looking ahead in 2021, 55% expect cloud security budgets to increase by a little less than one third, down from 65% in 2020. Forty percent expect their cloud security budgets to remain flat, up from 30% in 2020. Those anticipating their cloud security funding to shrink held steady at only five percent.

**How is your cloud security budget changing in the next 12 months?**

*A pie chart visually represents the following data:*

*   **5%** Budget will decline
*   **40%** Budget will stay flat
*   **55%** Budget will increase

*will increase by a little less than one-third, down from 65% in 2020*

## METHODOLOGY & DEMOGRAPHICS
This AWS Cloud Security Report is based on the results of a comprehensive online survey of 316 cybersecurity professionals, conducted in April 2021, to gain deep insight into the latest trends, key challenges, and solutions for cloud protection. The respondents range from technical executives to managers and IT security practitioners, representing a balanced cross-section of organizations of varying sizes across multiple industries.

*A series of bar charts visually represent the following data:*

**COMPANY SIZE**

*   **19%** Fewer than 10
*   **18%** 10-99
*   **17%** 100-499
*   **15%** 500-999
*   **14%** 1,000-4,999
*   **3%** 5,000-10,000
*   **14%** Over 10,000

**CAREER LEVEL**

*   **54%** Specialist
*   **15%** Director
*   **8%** Consultant
*   **5%** Manager/Supervisor
*   **4%** CTO, CIO, CISO, CMO, CFO, COO
*   **2%** Vice President
*   **2%** Other

**DEPARTMENT**

*   **23%** IT Security
*   **22%** IT Operations
*   **11%** Engineering
*   **7%** Operations
*   **6%** Compliance
*   **5%** Product Management
*   **5%** DevOps
*   **3%** SecOps
*   **14%** Other

**INDUSTRY**

*   **13%** Financial Services
*   **10%** Technology, Software & Internet
*   **18%** Government
*   **10%** Professional Services
*   **33%** Manufacturing
*   **11%** Education & Research
*   **23%** Telecommunications
*   **22%** Transportation & Logistics
*   **11%** Healthcare, Pharmaceuticals & Biotech
*   **7%** Other

CloudPassage®, a Fidelis Cybersecurity® company, safeguards cloud infrastructure for the world’s best-recognized brands in finance, e-commerce, gaming, B2B SaaS, healthcare, biotech, and digital media. Fidelis Cybersecurity combats the full spectrum of cyber-crime, data theft and espionage.

As the leading innovator of Active XDR solutions, Fidelis helps organizations detect, respond and neutralize threats earlier and deploy deception technologies to stop adversaries before they advance across the IT environment. The CloudPassage Halo® platform unifies security and compliance across servers, containers, and IaaS resources across any mix of public, private, hybrid, and multi-cloud environments including Amazon Web Services, Microsoft Azure, and Google Cloud Platform. Fidelis Cybersecurity is trusted by Global 1000s and Governments as their last line of defense. Fidelis Cybersecurity is a portfolio company of Skyview Capital.

www.cloudpassage.com | www.fidelissecurity.com
