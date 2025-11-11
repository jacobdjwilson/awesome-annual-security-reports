# The State of Identity and Access Management (IAM) Maturity

Sponsored by GuidePoint Security
Independently conducted by Ponemon Institute LLC

Publication Date: May 2025

Ponemon Institute© Research Report

## Table of Contents
- [Part 1. Executive Summary](#part-1-executive-summary)
- [Part 2. Introduction: Including a Peek at High Performer Trends](#part-2-introduction-including-a-peek-at-high-performer-trends)
- [Part 3. Key findings](#part-3-key-findings)
  - [Risks to identity security](#risks-to-identity-security)
  - [Managing user access & IT privileges in the IAM platform](#managing-user-access--it-privileges-in-the-iam-platform)
  - [Current and future trends in identity security technologies](#current-and-future-trends-in-identity-security-technologies)
  - [Best practices in achieving a strong identity security posture](#best-practices-in-achieving-a-strong-identity-security-posture)
- [Part 4. Methodology](#part-4-methodology)
- [Part 5. Caveats to this study](#part-5-caveats-to-this-study)
- [Part 6. Appendix with the detailed audited findings](#part-6-appendix-with-the-detailed-audited-findings)
  - [Part 1: Screening questions](#part-1-screening-questions)
  - [Part 2: Organization's IAM coverage and investment](#part-2-organizations-iam-coverage-and-investment)
  - [Part 3: Potential IAM security risks and exposures](#part-3-potential-iam-security-risks-and-exposures)
  - [Part 4: Understanding IAM and strategies](#part-4-understanding-iam-and-strategies)
  - [Part 5: Demographics](#part-5-demographics)

## Part 1. Executive Summary

Identity and Access Management (IAM) Maturity refers to the extent to which an organization effectively manages user identities and access across its systems and applications. It’s a measure of how well an organization is implementing and managing Identity and Access Management (IAM) practices. A mature IAM program ensures that only authorized users have access to the resources they need, enhancing security, reducing risks and improving overall efficiency.

Most organizations remain in the early to mid-stages of IAM maturity, leaving them vulnerable to identity-based threats. This new study of 626 IT professionals by the Ponemon Institute, sponsored by GuidePoint Security, highlights that despite growing awareness of insider threats and identity breaches, IAM is under-prioritized compared to other IT security investments. All participants in this research are involved in their organizations’ IAM programs.

Key Insights:

- IAM is underfunded and underdeveloped.

Only 50 percent of organizations rate their IAM tools as very or highly effective, and even fewer (44 percent) express high confidence in their ability to prevent identity-based incidents. According to 47 percent of organizations, investments in IAM technologies trail behind other security investment priorities.

- Manual processes are stalling progress.

Many organizations still rely on spreadsheets, scripts and other manual efforts for tasks like access reviews, deprovisioning and privileged access management—introducing risk and inefficiencies.

- High performers show the way forward.

High performers in this research are those organizations that self-report their IAM technologies and investments are highly effective (23 percent). As a result, they report fewer security incidents and stronger identity controls. These organizations also lead other organizations represented in this research in adopting biometric authentication, authentication, identity threat detection and integrated governance platforms.

- Technology and expertise gaps persist.

A lack of tools, skilled personnel and resources is preventing broader progress. Many IAM implementations are driven by user experience goals rather than security or compliance needs.

Bottom Line:

Achieving IAM maturity requires a strategic shift—moving from reactive, manual processes to integrated, automated identity security. Organizations that treat IAM as foundational to cybersecurity, not just IT operations, are best positioned to reduce risk, streamline access and build trust in a dynamic threat landscape.

## Part 2. Introduction: Including a Peek at High Performer Trends

The purpose of an Identity and Access Management (IAM) program is to manage user identities and access across systems and applications. A mature IAM program ensures that only authorized users have access to the resources they need to enhance security, reduce risks and improve overall efficiency.

This survey, sponsored by GuidePoint Security, was designed to understand how effective organizations are in achieving IAM maturity and which tools and practices are critical components of their identity and access management programs. A key takeaway from the research is that organizations’ continued dependency on manual processes as part of their IAM programs is a barrier to achieving maturity and reducing insider threats. Such a lack of maturity can lead to data breaches and security incidents caused by negligent or malicious insiders.

Recent examples of such events include former Tesla employees in 2023 who leaked sensitive data about 75,000 current and former employees to a foreign media outlet[^1]. In August 2022, Microsoft experienced an insider data breach where employees inadvertently shared login credentials for GitHub infrastructure, potentially exposing Azure servers and other internal systems to attackers.

According to the research, investments in IT security technologies are prioritized over IAM technologies. Without the necessary investments in IAM, organizations lack confidence in their ability to prevent identity-based security incidents. Respondents were asked to rate effectiveness in their organizations’ tools and investments in combating modern identity threats on a scale from 1 = not effective to 10 = highly effective, their confidence in the ability to prevent identity-based security incidents from 1 = not confident to 10 = highly confident and the priority of investing in IAM technologies compared to other security technologies from 1 = not a priority to 10 = high priority.

Figure 1 shows the very effective/very confident/high priority responses (7+ on the 10-point scale). As shown, only half (50 percent of respondents) believe their tools and investments are very effective and only 44 percent of respondents are very or highly confident in their ability to prevent identity-based security incidents. Less than half of the organizations (47 percent of respondents) say investing in IAM technologies compared to other IT security technologies is a high priority.

![Bar chart showing Effectiveness of tools and investments in combating modern identity threats at 50%, The priority of investing in IAM technologies compared to other IT security technologies at 47%, and Confidence in the ability to prevent identity-based security incidents at 44%. All percentages represent 7+ responses on a 10-point scale.]

[^1]: Tesla: Insiders Responsible for Major Data Breaches, Infosecurity Magazine, August 2023.

Best practices in achieving a strong identity security posture

To identify best practices in achieving a strong identity security posture, we analyzed the responses of the 23 percent of IT professionals who rated the effectiveness of their tools and investments in combating modern identity threats as highly effective (9+ on a scale from 1 = low effectiveness to 10 = high effectiveness). We refer to these respondents and their organizations as high performers. Seventy-seven percent of respondents rated their effectiveness on a scale from 1 to 8. We refer to this group as “other” in the report.

Organizations that have more effective tools and investments to combat modern identity threats are less likely to experience an identity-based security incident. Only 39 percent of high performers had an identity-based security incident.

High performers are outpacing other organizations in the adoption of automation and advanced identity security technologies.

- Sixty-four percent of high performers vs. 37 percent of other respondents have adopted biometric authentication.
- Fifty-nine percent of high performers vs. 34 percent of other respondents use automated mechanisms that check for compromised passwords.
- Fifty-six percent of high performers vs. 23 percent of other respondents have a dedicated PAM platform.
- Fifty-three percent of high performers vs. 31 percent of other respondents use IAM platforms and/or processes used to manage machine, service and other non-human accounts or identities.

High performers are significantly more likely to assign privileged access to a primary account (55 percent vs. 30 percent). Only 25 percent of high performers vs. 33 percent of other respondents use manual or scripted processes to temporarily assign privileged accounts.

High performers are leading in the adoption of ITDR, ISPM and IGA platforms.

- Thirty-seven percent of high performers vs. 12 percent of other respondents have adopted IDTR.
- Thirty-five percent of high performers vs. 15 percent of other respondents have adopted ISPM.
- Thirty-one percent of high performers vs. 9 percent of other respondents have adopted IGA platforms.

Barriers and challenges to achieving IAM maturity

Following are highlights from organizations represented in this research

Identity verification solutions are systems that confirm the authenticity of a person’s identity, typically in digital contexts, such as online transactions or applications. These solutions use various methods to verify a person’s identity and ensures only authorized users have access to the resources they need.

Few organizations use identity verification solutions and services to confirm a person’s claimed identity. Only 39 percent of respondents say their organizations use identity verification solutions and services. If they do use identity verification solutions and services, they are mainly for employee and contractor onboarding (37 percent of respondents). Thirty-three percent of respondents say it is part of customer registration and vetting, and 30 percent of respondents say it is used for both employee/contractor and customer.

Reliance on manual processes stalls organizations’ ability to achieve maturity. Less than half of organizations (47 percent) have an automated mechanism that checks for compromised passwords. If they do automate checks for compromised passwords, 37 percent of respondents say it is for both customer and workforce accounts, 34 percent only automate checks for customer accounts, and 29 percent only automate checks for workforce accounts.

To close the identity security gap, organizations need technologies, in-house expertise and resources. However, as discussed previously, more resources are allocated to investments in IT security. Fifty-four percent of respondents say there is a lack of technologies. Fifty-two percent say there is a lack of in-house expertise, and 45 percent say it is a lack of resources.

Security is not a priority when making IAM investment decisions. Despite many high-profile examples of insider security breaches, 45 percent of respondents say the number one priority for investing in IAM is to improve user experience. Only 34 percent of respondents say investments are prioritized based on the increase in number of regulations or industry mandates or the constant turnover of employees, contractors, consultants and partners (31 percent of respondents).

To achieve greater maturity, organizations need to improve the ability of IAM platforms to authenticate and authorize user identities and access rights. Respondents were asked to rate the effectiveness of their IAM platform in user access provisioning lifecycle from onboarding through termination, and its effectiveness authenticating and authorizing on a scale of 1 = not effective to 10 = highly effective. Only 46 percent of respondents say their IAM platform is very or highly effective for authentication and authorization. Fifty percent of respondents rate the effectiveness of their IAM platforms’ user access provisioning lifecycle from onboarding through termination as very or highly effective.

Policies and processes are rarely integrated with IAM platforms in the management of machine, service and other non-human accounts or identities. Forty-four percent of respondents say their IAM platform and/or processes are used to manage machine, service and other non-human accounts or identities. Thirty-nine percent of respondents say their organizations are in the adoption stage of using their IAM platform and/or processes to manage machine, service and other non-human accounts. Of these 83 percent of respondents (44 percent + 39 percent), 39 percent say the use of the IAM platform to manage machine, service and other non-human accounts or identities is ad hoc. Only 28 percent of these respondents say management is governed with policy and/or processes and integrated with the IAM platform.

IAM platforms and/or processes are used to perform periodic access review, attestation, certification of user accounts and entitlements but mostly it is manual. While most organizations conduct periodic access review, attestation and certification of user accounts and entitlements, 34 percent of respondents say it is manual with spreadsheets, and 36 percent say their organizations use custom in-house built workflows. Only 17 percent of respondents say it is executed through the IAM identity governance platform. Only 41 percent of respondents use internal applications and resources based on their roles and needs, to streamline onboarding, offboarding and access management. An average of 38 percent of internal applications are managed by their organizations’ IAM platforms.

Deprovisioning non-human identities, also known as non-human identity management (NHIM), focuses on removing or disabling access for digital entities like service accounts, APIs, and IoT devices when they are no longer needed. This process is crucial for security, as it helps prevent the misuse of credentials by automated systems that could lead to data breaches or system compromises.

Deprovisioning user access is mostly manual. Forty-one percent of respondents say their organizations include non-human identities in deprovisioning user access. Of those respondents, 40 percent say NHI deprovisioning is mostly a manual process. Twenty-seven percent of respondents say the process is automated with a custom script and 26 percent say it is automated with a SaaS tool or third-party solution.

Few organizations are integrating privileged access with other IAM systems and if they do the integration is not effective. Forty-two percent of respondents say PAM is running a dedicated platform. Twenty-seven percent say privileged access is integrated with other IAM systems, and 31 percent of respondents say privileged access is managed manually. Of these 27 percent of respondents, only 45 percent rate the effectiveness of their organizations’ IAM platforms for PAM as very or highly effective.

## Part 3. Key findings

In this section of the report, we present an analysis of the findings. The complete findings are presented in the Appendix. We have organized the report according to the following topics.

- Risks to identity security
- Managing user access & IT privileges in the IAM platform
- Current and future trends in identity security technologies
- Best practices in achieving a strong identity security posture

### Risks to identity security

Leaked, compromised or stolen credentials were most likely to cause an identity-based security incident. In the past 12 months, 50 percent of organizations represented in this research had an identity-based security incident. According to Figure 2, the number one cause was leaked, compromised or stolen credentials (34 percent of respondents). Other primary causes were identity theft (25 percent of respondents) and phishing (23 percent of respondents).

![Bar chart showing causes of identity-based security incidents. Leaked, compromised or stolen credentials at 34%, Identity theft at 25%, Phishing at 23%, Malware or ransomware at 21%, Social engineering at 21%, Identity misconfiguration at 17%, and Other at 7%. More than one response permitted.]

In addition to the possibility of fines and other financial consequences, identity-based security incidents cause declines in workforce and employee productivity. Respondents were asked how the incident affected their organizations. As shown in Figure 3, organizations experienced such serious consequences as the loss of workforce productivity because employees couldn’t access systems (38 percent of respondents) and diminishment of employee productivity (27 percent of respondents). Reputation of the organization also declined (27 percent of respondents).

![Bar chart showing the impact of identity-based security incidents. Loss of workforce productivity (e.g. production lines shut down, employees can’t access systems) at 38%, Decline in reputation at 27%, Diminished employee productivity at 27%, Loss of sales or customer access at 19%, Decline in trustworthiness at 17%, Cost of consultants and attorneys at 16%, Data exfiltration and extortion at 16%, and Regulatory fines at 12%. More than one response permitted.]

Few organizations use identity verification solutions and services to confirm a person’s claimed identity. Identity verification solutions are systems that confirm the authenticity of a person's identity, typically in digital contexts, such as online transactions or applications. These solutions use various methods to verify a person's identity, ensuring they are who they claim to be.

Only 39 percent of respondents say their organizations use identity verification solutions and services. As shown in Figure 4, if they do use identity verification solutions and services, it is mainly for employee and contractor onboarding (37 percent of respondents). Thirty-three percent of respondents say it is part of customer registration and vetting, and 30 percent of respondents say it is used for both employee/contractor and customer.

![Bar chart showing how identity verification solutions and services are used. Part of employee and contractor onboarding at 37%, Part of customer registration and vetting at 33%, and Used for both employee/contractor and customer at 30%.]

Less than half of organizations (47 percent) have an automated mechanism that checks for compromised passwords. According to Figure 5, if they automate checks for compromised passwords, 37 percent of respondents say it is for both customer and workforce accounts. Thirty-four percent only automate checks for customer accounts, and 29 percent only automate checks for workforce accounts.

![Bar chart showing how automated mechanisms for compromised passwords are used. For both customer and workforce accounts at 37%, For customer accounts at 34%, and For workforce accounts at 29%.]

To close the identity security gap, organizations need technologies, in-house expertise and resources. As shown in Figure 6, the top three gaps in identity security are the lack of technologies (54 percent of respondents), lack of in-house expertise (52 percent of respondents), and lack of resources (45 percent of respondents).

![Bar chart showing the biggest challenges to effectively implementing an identity-based security strategy. Lack of technologies at 54%, Lack of in-house expertise at 52%, Lack of resources at 45%, Lack of executive-level support at 37%, and Not a priority at 12%. Two responses permitted.]

Security is not the highest priority when making IAM investment decisions. Despite the many high-profile examples of insider security breaches, 45 percent of respondents say the number one priority for investing in IAM is to improve user experience, according to Figure 7. Similarly, investments are not prioritized to address weaknesses caused by the increase in number of regulations or industry mandates (34 percent of respondents), or the constant turnover of employees, contractors, consultants and partners (31 percent of respondents).

![Bar chart showing the most important drivers for investing in IAM security. Improved user experience at 45%, The increase in the number of regulations or industry mandates at 34%, To reduce costs at 33%, The constant turnover of employees, contractors, consultants, and partners at 31%, The constant changes to the organization due to corporate reorganizations, downsizing, and financial distress at 29%, Changes to the organization because of mergers and acquisitions at 23%, and Other at 5%. Two responses permitted.]

### Managing user access & IT privileges in the IAM platform

IAM platforms utilize various data sources to manage user identities and access rights. These include directory services, user accounts, and application and resource information. They also integrate with external systems like HR databases and IT systems for comprehensive identity management. An average of 86 data sources are integrated in the IAM platform.

To achieve greater maturity, organizations need to improve the ability of IAM platforms to authenticate and authorize user identities and access rights. Respondents were asked to rate the effectiveness of their IAM platform in user access provisioning lifecycle from onboarding through termination, and its effectiveness authenticating and authorizing on a scale of 1 = not effective to 10 = highly effective.

According to Figure 8, only 46 percent of respondents say their IAM platform is very or highly effective for authentication and authorization. Fifty percent of respondents rate the effectiveness of their IAM platforms’ user access provisioning lifecycle from onboarding through termination as very or highly effective.

![Bar chart showing the effectiveness of an IAM platform’s user access provisioning. Effectiveness of the IAM platform’s user access provisioning lifecycle from onboarding through termination at 50%, and Effectiveness of the IAM platform for authentication and authorization at 46%. Both represent 7+ responses on a 10-point scale.]

Policies and processes are rarely integrated with IAM platforms to manage machine, service and other non-human accounts or identities. Forty-four percent of respondents say their IAM platform and/or processes are used to manage machine, service and other non-human accounts or identities. Thirty-nine percent of respondents say their organizations are at the adoption stage of using their IAM platform and/or processes to manage machine, service and other non-human accounts.

As shown in Figure 9, of these 83 percent of respondents (44 percent + 39 percent), 39 percent say the use of the IAM platform to manage machine, service and other non-human accounts or identities is ad hoc. Only 28 percent of these respondents say management is governed with policy and process integrated with the IAM platform.

![Bar chart showing how organizations use their IAM platform and/or processes to manage machine, service and other non-human accounts or identities. Ad hoc approach at 39%, Policy and process driven, not integrated with IAM platform at 33%, and Governed with policy and process and integrated with IAM platform at 28%.]

Periodic access to review/attestation/certification of user accounts and entitlements is mostly manual. Eighty-seven percent of respondents say their organization performs access review/attestation/certification. According to Figure 10, 36 percent of respondents say their organizations use custom in-house built workflows, 34 percent of respondents say it is manual with spreadsheets, and 17 percent of respondents say it is executed through the IAM identity governance platform.

![Bar chart showing the most important processes to perform periodic access review/attestation/certification of user accounts and entitlements. Custom in-house built workflows at 36%, Manual with spreadsheets at 34%, Executed through IAM identity governance platform at 17%, and No access review/attestation/certification performed at 13%.]

According to Figure 11, only 41 percent of respondents use internal applications and resources based on their roles and needs to streamline onboarding, offboarding and access management. An average of 38 percent of internal applications are managed by their organizations’ IAM platforms.

![Bar chart showing responses to "Does your organization use internal application provisions to grant users access to internal applications and resources based on their roles and needs, streamlining onboarding, offboarding and access management?". Yes at 41%, No at 50%, and Unsure at 9%.]

More organizations will complete a refresh to a cloud-or SaaS-delivered IAM platform for user access provisioning, lifecycle from onboarding to termination. Currently, 39 percent of respondents have completed a refresh.

As shown in Figure 12, 86 percent of respondents say their organizations will complete a refresh in less than 1 year (27 percent), 1 to 2 years (22 percent), 3 to 4 years (21 percent) or 4+ years (16 percent).

![Bar chart showing plans to complete a refresh to a cloud-or SaaS-delivered IAM platform. In less than 1 year at 27%, 1 to 2 years at 22%, 3 to 4 years at 21%, 4+ years at 16%, and No plans to complete a refresh at 14%.]

Deprovisioning non-human identities, also known as non-human identity management (NHIM), focuses on removing or disabling access for digital entities like service accounts, APIs, and IoT devices when they are no longer needed. This process is crucial for security, as it helps prevent the misuse of credentials by automated systems that could lead to data breaches or system compromises.

Deprovisioning user access is mostly manual. Forty-one percent of respondents say their organizations include non-human identities when deprovisioning user access. According to Figure 13, this is mostly a manual process (40 percent of respondents). Twenty-seven percent of respondents say the process is automated with a custom script, and 26 percent say it is automated with a SaaS tool or third-party solution.

![Bar chart showing how organizations deprovision user access. Manual at 40%, Automation, custom script at 27%, Automation, SaaS tool or third-party solution at 26%, and Other at 7%.]

A PAM (Privileged Access Management) platform is a cybersecurity technology that secures, manages and monitors privileged accounts across an IT environment. It focuses on accounts with elevated permissions, like administrator accounts, and uses techniques like credential vaulting, session monitoring, and access controls to protect sensitive resources. PAM ensures only authorized users can access critical systems and data, minimizing the risk of breaches and operational disruptions.

Few organizations are integrating privileged access with other IAM systems, and if they do, the integration is not effective. According to Figure 14, 42 percent of respondents say PAM is running on a dedicated platform. Twenty-seven percent say privileged access is integrated with other IAM systems, and 31 percent of respondents say privileged access is managed manually. Of these 27 percent of respondents, only 45 percent rate the effectiveness of their organizations’ IAM platforms for PAM as very or highly effective.

![Bar chart showing responses to "Does your organization have a dedicated PAM platform?". Yes, PAM is running a dedicated platform at 42%, No, privileged access is managed manually at 31%, and No, privileged access is integrated with other IAM systems at 27%.]

Privileged access refers to the ability of individuals or entities to access resources and systems with higher-than-standard permissions, often including administrative or superuser-level access. This access allows them to perform sensitive operations and manage critical aspects of the organization's infrastructure.

As shown in Figure 15, 43 percent of respondents say privileged access is permanently assigned to a primary account, 30 percent of respondents say a manual or script exists to temporarily assign a privileged account, and 27 percent of respondents say privileged access is permanently assigned through a secondary account.

![Bar chart showing how organizations assign privileged access. Privileged access is permanently assigned to primary account at 43%, Manual or scripted process exists to temporarily assign privileged account at 30%, and Privileged access is permanently assigned through a secondary account at 27%. Only one choice permitted.]

As shown in Figure 16, 40 percent of respondents say the management of privileged access passwords, including privileged access assigned to service accounts, is managed by the account owner. Thirty-four percent of respondents say passwords are static, and 26 percent of respondents say passwords are regularly rotated by a process or system.

![Bar chart showing how organizations manage privileged access passwords. Passwords are assigned and managed by the account owner at 40%, Passwords are static at 34%, and Passwords are regularly rotated by a process or system at 26%.]

### Current and future trends in identity security technologies

Passwordless authentication is a means to verify a user’s identity without using a password. Instead passwordless uses more secure alternatives like possession factors, one-time passwords (OTP), registered smartphones or biometrics.

The adoption of passwordless authentication is in its early stages. Fifty-five percent of respondents say their organizations have adopted or plan to adopt passwordless authentication. However, only 21 percent of these respondents say it is fully implemented in their organizations, as shown in Figure 17.

![Bar chart showing the adoption or plan to adopt passwordless authentication. Fully implemented at 21%, Testing passwordless capabilities at 19%, Evaluating passwordless solutions at 12%, Adopt within 1 year at 25%, Adopt between 1 to 2 years at 10%, and Adopt in more than 2 years at 13%.]

Cost and complexity deter the adoption of passwordless authentication. Of the 45 percent of respondents who say their organizations have no plans to adopt passwordless authentication, 34 percent say it is the cost, and 25 percent say it is the complexity of managing passwordless authentication, as shown in Figure 18.

![Bar chart showing reasons why organizations would not adopt passwordless authentication. Cost at 34%, Complexity of managing passwordless authentication at 25%, Security risks at 20%, Complexity for end users at 12%, and Service desk issues at 9%.]

Seventy-two percent of organizations have implemented multifactor authentication MFA. According to Figure 19, 27 percent of respondents say MFA is applied to customer accounts only, 24 percent of respondents say MFA is applied to both customer and workforce accounts, and 21 percent of respondents say MFA is applied to workforce accounts only.

![Bar