# STATE OF CLOUD SECURITY 2025

Organizations embracing cloud-native architectures face attackers who are using an ever-expanding set of techniques to exploit services, tools, and environments. Complacency is costly, and understanding risk across every layer of the cloud stack is essential to defending growing attack surfaces against threats that are evolving just as quickly.

For the 2025 edition of our State of Cloud Security study, we analyzed security posture data from a sample of thousands of organizations that use AWS, Azure, or Google Cloud. Our findings suggest that, while progress continues to be made in removing long-lived credentials, enforcing secure-by-default mechanisms, and eliminating overprivileged IAM roles, many organizations continue to leave key resources vulnerable to known exploits and potential attacks. Newer strategies, such as data perimeters and centrally managed multi-account environments, are growing in popularity and offer powerful restrictions but often aren’t enabled by default or introduce additional attack vectors if not configured properly.

## Table of Contents
- [Fact 1: Multi-account environments allow organizational guardrails in AWS](#fact-1)
- [Fact 2: As organizations adopt data perimeters, most lack centralized control](#fact-2)
- [Fact 3: Long-lived cloud credentials remain pervasive and risky](#fact-3)
- [Fact 4: One in two EC2 instances enforces IMDSv2, but older instances lag behind](#fact-4)
- [Fact 5: Adoption of public access blocks in cloud storage services is plateauing](#fact-5)
- [Fact 6: Overprivileged and misconfigured IAM roles for third-party integrations remain risks for AWS accounts](#fact-6)
- [Fact 7: Insecure default configurations leave managed Kubernetes clusters at risk](#fact-7)
- [Fact 8: Organizations continue to run risky workloads](#fact-8)
- [Methodology](#methodology)

---

<a id="fact-1"></a>
## FACT 1: Multi-account environments allow organizational guardrails in AWS

Enforcing minimal privileges in a single AWS account is challenging. Similarly, running workloads from the different stages (dev, prod) in the same AWS account can be difficult due to quota, IAM, network, and performance issues. This is why a common best practice, both from a security and operational perspective, is to have multiple AWS accounts centrally managed through AWS Organizations, a governance service offered by AWS. Note that an “AWS organization” refers to one grouping of AWS accounts within this service and is not the same as an “organization.”

We found that at least 84% of organizations use more than one AWS account, while 86% of organizations have AWS accounts using AWS Organizations. AWS Organizations has become a popular way to centrally manage multi-account environments, with over two in three organizations (70%) having all their AWS accounts part of an AWS organization and three in four AWS accounts (74%) part of an AWS organization. A meaningful minority of organizations (14%) do not use AWS Organizations at all for any of their AWS accounts.

When using multi-account environments managed through AWS Organizations, it’s possible to enforce security invariants across all AWS accounts with organization-level guardrails. We found that among organizations using AWS Organizations, two in five (40%) take advantage of service control policies (SCPs), and 6% use resource control policies (RCPs)—a recently introduced type of organizational policy that applies at the resource level.

By analyzing the IAM condition keys in use in the explicit deny statements of these policies, we saw that SCPs are most commonly used to protect shared infrastructure and “landing zones” deployed in member accounts, as well as security mechanisms like CloudTrail and GuardDuty. When RCPs are defined, they are most commonly used to enforce encryption across all S3 buckets in an organization and ensure that all buckets in an AWS organization can only be accessed by principals from the same AWS organization.

However, using AWS Organizations comes with a few things to watch out for. By design, authorized principals in the organization management account can access all child accounts, creating an extremely powerful lateral movement vector. To protect against this, AWS recommends that the management account should not run any workloads, as doing so reduces the risk of it getting compromised. Still, we identified that 9% of organizations run EC2 instances in their AWS organization management account, up from 6% in 2024. In these configurations, an attacker who’s able to compromise a single EC2 instance may be able to escalate their privileges and access all child AWS accounts.

<a id="fact-2"></a>
## FACT 2: As organizations adopt data perimeters, most lack centralized control

In the cloud, identity is the new perimeter. There is little concept of an internal network, since cloud APIs are exposed to the internet by design. This means that an attacker stealing cloud credentials can call cloud APIs from anywhere in the world without the need to be in an internal network. With credential theft being a major attack vector, the concept of data perimeters has emerged in recent years. Data perimeters enable teams to restrict certain cloud API calls so they only succeed if coming from approved networks or trusted cloud accounts.

However, data perimeters are not implemented by default. They require enacting a set of various policies such as SCPs, RCPs, or resource-based policies—for example, at the S3 bucket or VPC endpoint level. Using a data perimeter requires using advanced IAM policy condition keys such as `aws:SourceAccount` or `aws:PrincipalOrgID`.

We determined that almost two in five (40%) organizations use data perimeters through either SCPs, RCPs, VPC endpoints, or S3 bucket policies.

Overall, the most popular ways to implement data perimeters are through:

- **S3 bucket policies** (32% of organizations), mostly through the `aws:SourceAccount` condition key. This ensures that nobody outside of a specific AWS account can access the bucket, even if its ACLs or individual files are mistakenly made public.
- **VPC endpoint policies** (13% of organizations), mostly through the `aws:PrincipalAccount` condition key. This ensures that an attacker cannot exfiltrate data to an attacker-owned AWS account.
- **SCPs** (0.6% of organizations), mostly through the `aws:PrincipalAccount` condition key.
- **RCPs** (0.1% of organizations), mostly through the `aws:PrincipalOrgID`, `aws:SourceOrgID`, and `aws:SourceAccount` condition keys. These allow defenders to make sure that a specific type of resource can’t be accessed by anyone outside the organization, even if it’s misconfigured.

Although data perimeters are considered an advanced practice, over a third of organizations already use them. This reflects growing concern over credential theft and a willingness to adopt provider-supported safeguards for cloud data. But our analysis also reveals that most data perimeters are still applied per resource. Many organizations beginning to use data perimeters should shift toward modern controls like RCPs, which enforce guardrails at the organizational level, eliminating gaps in coverage.

<a id="fact-3"></a>
## FACT 3: Long-lived cloud credentials remain pervasive and risky

Long-lived cloud credentials continue to pose a major security risk, with previous installments of this report having shown that they are the most common cause of publicly documented cloud security breaches. For this year’s findings, we followed up on how organizations are using legacy versus modern authentication methods to authenticate humans and applications across AWS, Azure, and Google Cloud.

We found that most organizations (79%) continue to use federated authentication for human users to access the AWS console, such as through AWS IAM Identity Center or Okta. This represents a small increase in comparison to 2024, up from 76%, indicating that some organizations have transitioned fully to only federated authentication. However, almost two in five (39%) organizations still use IAM users in some capacity, and one in five organizations relies exclusively on IAM users. This shows that although organizations are increasingly adopting central human identities to access their cloud environments, they are struggling to get rid of their legacy IAM practices, such as humans using IAM users.

Similar to last year, we found that long-lived cloud credentials are often old and even unused:

- **In AWS**, 59% of IAM users have an active access key older than one year. Over half of these users have credentials that have been unused for over 90 days.
- **Google Cloud service accounts**: 55% of Google Cloud service accounts have active service account keys older than a year, down from 62% a year ago.
- **Microsoft Entra ID**: 40% of Microsoft Entra ID applications have credentials older than one year, down from 46% a year ago.

Analyzing access key age over time also shows that organizations using long-lived credentials are struggling to rotate them. The percentage of access keys older than three years has mostly increased across all clouds.

> “From an incident response perspective, exposed access keys belonging to IAM users remain the primary initial access vector in AWS. Previously, we observed access key exposure more in scripts that were accidentally exposed through various code sharing platforms. In more recent incidents, the keys were exposed through improperly protected CI/CD pipelines and shared developer workstations.”
> — **Korstiaan Stam**, Founder and CEO, Invictus Incident Response

<a id="fact-4"></a>
## FACT 4: One in two EC2 instances enforces IMDSv2, but older instances lag behind

Adoption of IMDSv2—an AWS security mechanism that blocks credential theft in EC2 instances—continues to grow. On average, organizations now enforce IMDSv2 on 66% of their instances, up from 47% a year ago. Overall, 49% of EC2 instances have IMDSv2 enforced.

While this reinforces an ongoing trend, we also found that not all EC2 instances are created equal. Although over half of instances created in the two weeks preceding the collection of the data for this report enforce IMDSv2, only 14% of instances created over two years ago enforce it.

We also identified that more organizations are taking IMDSv2 seriously. Over one in three organizations (37%) enforces IMDSv2 on 100% of their EC2 instances, up from less than one in four in 2024.

> “While IMDSv2 adoption has been increasing year over year, enforcement still lags despite AWS introducing configurable defaults. Organizations should enable these security defaults and enforce IMDSv2 through SCPs across their environments. IMDSv2 is a simple, effective control that significantly reduces the impact of SSRF vulnerabilities.”
> — **Adam Pietrzycki**, Senior Infrastructure Security Engineer, Zapier

<a id="fact-5"></a>
## FACT 5: Adoption of public access blocks in cloud storage services is plateauing

In this year’s report, we found that adoption of public access blocks continues to increase but at a slower pace than previous years. One percent of S3 buckets are effectively public, down from 1.5% in 2024. Over four in five (83%) S3 buckets are covered by an account-wide or bucket-specific S3 Block Public Access.

On the Azure side, 1.3% of Azure Blob Storage containers are effectively public, down from 2.6% a year ago. Relatedly, almost three in five (58%) Azure Blob Storage containers are in a storage account that proactively blocks public access, up from 42% a year ago.

<a id="fact-6"></a>
## FACT 6: Overprivileged and misconfigured IAM roles for third-party integrations remain risks for AWS accounts

We found that on average, an organization deploys 13 third-party integration roles (up from 10.2 in 2024), linked to an average of 2.5 distinct vendors.

We found that 12.2% of third-party integrations are dangerously overprivileged, allowing the vendor to access all data in the account or to take over the whole AWS account. This is slightly up from 10% in 2024. We also identified that 2.25% of third-party integration roles don’t enforce the use of an external ID.

<a id="fact-7"></a>
## FACT 7: Insecure default configurations leave managed Kubernetes clusters at risk

Two in five (39%) EKS clusters and one in three (34%) AKS clusters are exposed to the internet. This number is much higher for GKE clusters, reaching over one in two (54%).

We also analyzed the IAM roles attached to these managed Kubernetes clusters. For EKS, we determined that 13% of clusters have a dangerous node role that has full administrator access, allows for privilege escalation, has overly permissive data access, or allows for lateral movement. In Google Cloud, 10% of GKE clusters have a privileged service account.

<a id="fact-8"></a>
## FACT 8: Organizations continue to run risky workloads

In AWS, while fewer than 0.4% of EC2 instances have administrator privileges, almost one in five (19.4%) is overprivileged. Among these:
- 3.8% have risky permissions that allow lateral movement.
- 2.4% allow an attacker to gain full administrative access.
- 17.9% have excessive data access.

In Google Cloud, we found that 17% of VMs have full administrator “editor” permissions on the project they run in through the use of the Compute Engine default service account. In total, nearly one in four Google Cloud VMs (23%) has overly permissive access to a project.

<a id="methodology"></a>
## Methodology

Findings are based on data collected in September 2025 from customers of Datadog Infrastructure Monitoring, Datadog Logs, and Datadog Cloud Security.

### Data Perimeter Analysis
We considered that organizations were using an AWS data perimeter when they contained any of the following AWS IAM condition keys in any of the statements:
- `aws:PrincipalAccount`
- `aws:PrincipalOrgID`
- `aws:PrincipalOrgPaths`
- `aws:ResourceAccount`
- `aws:ResourceOrgID`
- `aws:ResourceOrgPaths`
- `aws:SourceAccount`
- `aws:SourceIp`
- `aws:SourceOrgID`
- `aws:SourceOrgPath`
- `aws:SourceVpc`
- `aws:SourceVpce`

### Licensing
Report: CC BY-ND 4.0
Images: CC BY-ND 4.0