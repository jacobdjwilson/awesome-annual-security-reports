2026
State of
AppSec Report
When Development Velocity
Exceeds Security Maturity
©2026 ORCA SECURITY. ALL RIGHTS RESERVED.

Application security has fundamentally changed, but many programs still operate
as if it hasn’t. Software is built on open-source dependencies, automated pipelines,
and infrastructure as code, while AI is increasing both scale and risk. Yet security
teams are expected to manage this complexity with outdated approaches.
Across real production environments, risk is visible but rarely actionable without
context. AI is accelerating development and expanding the attack surface, from
generated code to model dependencies, making prioritization essential. This
report helps organizations understand where traditional approaches fall short
and how to focus on the changes that materially reduce risk.”
GIL GERON,
CEO AND CO-FOUNDER OF ORCA SECURITY

2026 STATE OF APPLICATION SECURITY REPORT
Inside This Report
| Foreword | 01  | 5. CI/CD Pipeline Security  | 18  |
| -------- | --- | --------------------------- | --- |
|          |     | 5.1 CI/CD Platform Adoption | 20  |
About the Orca Research Pod 02 5.2 GitHub Actions Security 21
| Executive summary                   | 03  | 6. Infrastructure as Code Security  | 22  |
| ----------------------------------- | --- | ----------------------------------- | --- |
|                                     |     | 6.1 IaC Platform Adoption           | 24  |
| Key findings                        | 04  |                                     |     |
|                                     |     | 6.2 Storage and Data Protection     | 25  |
|                                     |     | 6.3 Identity and Access Management  | 26  |
| 1. The Rise of Supply Chain Attacks | 05  |                                     |     |
|                                     |     | 6.4 Network Security                | 27  |
1.1 Major Supply Chain Attacks 07 6.5 Container Security in IaC 28
2. Vulnerabilities in AI Packages  08 7. Repository and SCM Security 29
| 2.1 Critical Remote Code Execution Vulnerabilities | 10  |                                   |     |
| -------------------------------------------------- | --- | --------------------------------- | --- |
|                                                    |     | 7.1 Code Review and Approval Gaps | 31  |
2.2 Malicious Packages: Still Lurking in Production 11 7.2 Branch Protection Weakness 32
|                                                   |     | 7.3 Access Control and Hygiene    | 33  |
| ------------------------------------------------- | --- | --------------------------------- | --- |
| 3. Container Vulnerability Landscape              | 12  |                                   |     |
|                                                   |     | 8. Key Recommendations            | 34  |
| 3.1 High/Critical Vulnerability Patching Velocity | 14  |                                   |     |
|                                                   |     | 8.1 Immediate Actions (0-30 Days) | 35  |
4. Secrets Management 15 8.2 Short-term Initiatives (30-90 D a  y s ) 36

|                              |     | 8.3 Strategic Improvements (90+ Days) | 37  |
| ---------------------------- | --- | ------------------------------------- | --- |
| 4.1 The AI/ML Secrets Crisis | 17  |                                       |     |

|     |     | 9. Conclusion | 38  |
| --- | --- | ------------- | --- |

2026 STATE OF APPLICATION SECURITY REPORT
Foreword
As organizations accelerate software delivery through cloud-native architectures, open-source
dependencies, and automated pipelines, application attack surfaces are expanding faster than security
practices can keep up. AI-assisted development is further increasing this velocity, generating code,
dependencies, and configurations at a pace that traditional security processes were not designed to
govern.
Modern applications are built from thousands of third-party components and deployed at machine speed.
This velocity enables scale and innovation, but it also makes it impossible to fix everything once code
reaches production. Vulnerable dependencies, exposed secrets, and insecure configurations are no longer
edge cases; they are structural realities of how software is built today. At the same time, AI systems
introduce new risks and enable the rapid propagation of insecure code patterns and model dependencies
across environments.
These challenges are compounded by the rise of software supply chain attacks, which have proven to be
one of the most effective paths to large-scale compromise. A single poisoned dependency or workflow can
cascade across thousands of organizations, turning application security failures into operational risk.
This State of Application Security Report is designed to help teams understand where these risks are
introduced and how to address them effectively. Grounded in real-world findings from the Orca Research
Pod, it provides a clear view into the current Application Security landscape and practical guidance for
securing modern applications at the speed today’s businesses demand.
Gil Geron
CEO and Co-Founder of Orca Security
2026 STATE OF APPSEC REPORT | 01

2026 STATE OF APPLICATION SECURITY REPORT
About the Orca Research Pod
The Orca Research Pod is a group of security researchers that discover and analyze security
risks and vulnerabilities to strengthen the Orca Security Platform and promote CNAPP security
best practices.
Research Methodology
This report is based on aggregated, anonymized security telemetry from more than 1,000 production
organizations leveraging Orca Security’s cloud security platform.
All metrics presented represent the percentage of organizations exhibiting each finding, calculated as a
weighted average across the organizations. Data was collected between Q3 2025 and Q1 2026, focusing
exclusively on production environments to ensure findings reflect real-world security postures rather than
test or development configurations.
Security findings span multiple domains: CI/CD pipeline security, secrets management, repository
configuration, software composition analysis (SCA), static application security testing (SAST), infrastructure
as code (IaC), and container security.
Report Data Set:
● Cloud workload and configuration data
● Billions of real-world production cloud assets
● Data referenced in this report was collected from Q3 2025 to Q1 2026
● AWS, Azure, Google Cloud, Oracle Cloud, and Alibaba Cloud environments
2026 STATE OF APPSEC REPORT | 02

2026 STATE OF APPLICATION SECURITY REPORT
Executive Summary
Leveraging real-world telemetry from more than 1,000 production organizations, this report examines the current state of application security across the modern software
delivery lifecycle. The findings reveal a growing disconnect between how applications are built today and how application security is practiced, resulting in persistent risk, stalled
remediation, and widening exposure across production environments. Our main findings summary includes:
🔺 Application risk is widespread and routinely reaches production 🔺 CI/CD Pipelines and Infrastructure-as-Code are scaling risk by default
More than 78% of organizations have applications running with critical With 74% of organizations deploying infrastructure through code,
vulnerabilities. Even years after disclosure, high-impact issues like Log4Shell misconfigurations are no longer isolated mistakes, they are repeatable
continue to affect nearly half of production environments, highlighting how production risks. Over 80% of IaC environments lack proper logging and
traditional AppSec approaches struggle to keep pace with dependency sprawl. monitoring, and 84% deploy unencrypted storage, embedding security gaps
directly into delivery pipelines.
🔺 Secrets exposure remains pervasive, and AI adoption is amplifying impact
Nearly one-third of organizations expose valid, active secrets in code, while 🔺 Supply chain attacks are now a routine production risk
over 41% have leaked AI/ML credentials. These exposures grant direct access More than 11% of organizations have well known malicious packages in
to proprietary models, sensitive data, and usage-based services, increasing production, including dependencies publicly disclosed and removed years ago.
both security and financial risk. Self-replicating attacks like the 2025 Shai-Hulud worm demonstrate how a
single compromised dependency can cascade across thousands of
🔺 Detection is not translating into remediation downstream environments.
While vulnerabilities are identified, they are rarely resolved. Over 77% of
organizations still carry high or critical container vulnerabilities after 90 days,
revealing that when teams can’t effectively prioritize risk, vulnerabilities
aren’t remediated.
2026 STATE OF APPSEC REPORT | 03

2026 STATE OF APPLICATION SECURITY REPORT
Key Findings
| 31% | 43% | 78% | 80% |
| --- | --- | --- | --- |
of organizations expose  of organizations have  of organizations run  of organizations lack logging  or
|                          | exposed AI or machine  |                             | monitoring in Infrastructure  |
| ------------------------ | ---------------------- | --------------------------- | ----------------------------- |
| valid secrets in source  |                        | applications with critical  |                               |
|                          | learning credentials.  |                             | deployed as code              |
| code repositories.       |                        | vulnerabilities             |                               |
Hardcoded credentials provide attackers with  As AI adoption accelerates, leaked model and  High-severity issues still reach production,  When infrastructure is defined programmatically
direct access to systems and data, turning  API credentials introduce new risks, including  showing that CVSS scores alone, without  without visibility, misconfigurations and
simple code exposure into immediate,  unauthorized access, data leakage, and  exploitability context, no longer drive
compromises can persist undetected across
potentially large scale, security incidents. unexpected financial impact. effective prioritization or remediation. multiple environments.
| 77% | 50% | 11% | 75% |
| --- | --- | --- | --- |
of organizations have high  of organizations remain  of organizations have well  of organizations
or critical container vulnerabilities  vulnerable to Log4Shell-affected  known malicious packages  manage infrastructure
unpatched after 90 days. dependencies in production. running in production. through code.
While vulnerabilities are detected early,  The persistence of widely publicized,  Software supply chain attacks are no longer  When infrastructure is defined and deployed
remediation stalls when teams lack the  high-impact vulnerabilities years after  edge cases, with malicious dependencies  programmatically, misconfigurations such as
context needed to determine which findings  disclosure shows how deeply embedded and  continuing to propagate long after they are  unencrypted storage and missing logging are
pose real production risk. hard to remediate transitive dependencies are. publicly disclosed and removed from registries. repeatedly pushed into production at scale.
2026 STATE OF APPSEC REPORT   |   04

01
The Rise of
Supply Chain Attacks

18,000+
The Rise of Supply Chain Attacks
Software supply chain attacks have shifted from edge-case threats to one of the
most reliable paths to large-scale compromise. By targeting shared dependencies,
DOWNSTREAM ORGANIZATIONS
build systems, and automation workflows, attackers can achieve exponential
impact from a single intrusion.
The SolarWinds breach in 2020 marked a turning point, demonstrating how
compromising one build pipeline could grant access to 18,000+ downstream
organizations, including Fortune 500 companies and government agencies. Since
then, attackers have increasingly focused on package registries, CI/CD platforms,
and maintainer credentials, where trust is implicit and validation is often limited.
This evolution accelerated in 2025 with the emergence of self-replicating supply
chain malware. The Shai-Hulud campaigns introduced a new class of attack that
spreads autonomously by harvesting npm tokens and GitHub credentials from
infected environments. Shai-Hulud 2.0 alone compromised over 796 npm packages
with more than 20 million weekly downloads, exposing 14,000 secrets across 487
organizations.
These attacks underscore a new reality, that modern software is only as secure as
the weakest dependency, maintainer account, or automation workflow it relies on.
2026 STATE OF APPSEC REPORT | 06

THE RISE OF SUPPLY CHAIN ATTACKS
| ATTACK / CAMPAIGN |     | TYPE | IMPACT |
| ----------------- | --- | ---- | ------ |
Major Supply Chain Attacks
| 2025 | Shai-Hulud 2.0 | npm Self- | 796+ npm packages,  |
| ---- | -------------- | --------- | ------------------- |
Software supply chain attacks have evolved from isolated incidents
|     |     | Replicating Worm | 20M+ weekly downloads |
| --- | --- | ---------------- | --------------------- |
into one of the most effective paths to large-scale compromise. Over
the past five years, their sophistication and impact have increased
sharply, as attackers exploit the force-multiplier effect of compromising  2025 React shell  RCE Vulnerability CVSS 10.0, 55.8M+
|     | (CVE-2025-55182) |     | weekly downloads  |
| --- | ---------------- | --- | ----------------- |
shared dependencies, build systems, and automation workflows.
| 2025 | tj-actions/changed-files | GitHub Actions  | 23,000+  |
| ---- | ------------------------ | --------------- | -------- |
The 2020 SolarWinds breach marked a turning point, demonstrating
|     |     | Compromise  | repositories |
| --- | --- | ----------- | ------------ |
how a single compromised build pipeline could grant access to more
than 18,000 downstream organizations, including government
| 2024 | XZ Utils Backdoor  | Maintainer Social  | CVSS 10.0,  |
| ---- | ------------------ | ------------------ | ----------- |
agencies and Fortune 500 companies. Since then, attackers have
|     |     | Engineering  | multi-year operation  |
| --- | --- | ------------ | --------------------- |
increasingly targeted package registries, CI/CD platforms, and
maintainer credentials, as these are areas where trust is implicit and
| 2024 | 3CX /  | Double Supply  | 242,519+ |
| ---- | ------ | -------------- | -------- |
security controls are often weakest. SmoothOperator  Chain Attack  IPs compromised
This escalation accelerated in 2025 with the emergence of  2023 MOVEit Zero-Day  600+
self-replicating supply chain malware. Campaigns like Shai-Hulud  Exploitation  organizations
introduced attacks capable of spreading autonomously by harvesting
npm tokens and GitHub credentials from infected environments.  2021 Log4Shell (Log4j)  Critical Library  CVSS 10.0,
Shai-Hulud 2.0 alone compromised over 796 npm packages with more  Vulnerability  billions of devices
than 20 million weekly downloads, exposing 14,000 secrets across
487 organizations. This signals a shift toward persistent, scalable  2020 SolarWinds /  Build System  18,000+
|     | SUNBURST  | Compromise  | customers |
| --- | --------- | ----------- | --------- |
operations that weaponize trust across the software ecosystem.
22002266  SSTTAATTEE  OOFF  AAPPPPSSEECC  RREEPPOORRTT      ||      0077

02
Dependency
& Vulnerability Management

Dependency and
Dependency Security Findings
Vulnerability Management
Packages with known vulnerabilities of any severity
Modern applications are built on layers of third-party code, with much of it shipping
82%
with known risk. Open-source dependencies accelerate development, but they also
introduce vulnerabilities that are difficult to track, prioritize, and remediate across
Packages with critical vulnerabilities
complex dependency trees. Our research shows that vulnerable packages are not
78%
isolated findings, but pervasive across production environments.
Using deprecated packages
More than 78% of organizations have applications running with critical
17%
vulnerabilities. As dependency sprawl grows, traditional AppSec approaches that
rely on severity-based alerting struggle to distinguish between theoretical risk and
Malicious packages detected
issues that pose real exposure in production.
11%
The result is a growing backlog of vulnerabilities that teams are aware of but lack
the context to confidently and efficiently address.
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 09

CVSS Critical/High Vulnerabilities DEPENDENCY & VULNERABILITY MANAGEMENT 1 2
Apache Tomcat RCE (CVE-2025-24813)
50%
2.1 Critical Remote
Log4j Additional RCE (CVE-2021-45046)
Code Execution Vulnerabilities
47%
Certain vulnerabilities demand immediate attention due to severity
Log4Shell (CVE-2021-44228)
and ease of exploitation, however many evade remediation.
46%
Apache Commons Text RCE (CVE-2022-42889) The persistence of Log4Shell nearly four years after disclosure, still
44% affecting 46% of organizations, underscores a broader challenge in
modern AppSec that even when vulnerabilities are widely publicized
Spring4Shell (CVE-2022-22965)
and patches are available, remediation can still stall. At the same
44% time, new RCE vulnerabilities like React2Shell (CVE-2025-55182),
which affects 29% of organizations and applies to all React 19 and
React/Next.js RCE (CVE-2025-55182)
2 9 %
Next.js 15/16 applications using React Server Components by
default, are rapidly expanding the attack surface of modern
Apache Struts RCE (CVE-2024-53677) application frameworks.
1 7 %
Together, these findings show that severity alone is not enough to
n8n Workflow RCE (CVE-2025-68613)
9 %
drive effective remediation. Without validation, prioritization, and
production context, even the most critical vulnerabilities remain open
Erlang/OTP RCE (CVE-2025-32433)
because teams struggle to gather the insight needed to determine
6 % which risks are truly exploitable and demand immediate action.
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 10

DEPENDENCY & VULNERABILITY MANAGEMENT
1 2
|                           | PACKAGE | VERSION(S) | ECOSYSTEM | ATTACK TYPE | % Of ORGS |
| ------------------------- | ------- | ---------- | --------- | ----------- | --------- |
|                           |         |            | npm       | Maintainer  |           |
| 2.2  Malicious Packages:  | Faker   | 6.6.6      |           |             | 7%        |
Sabotage
Still Lurking in Production
|     | Event-stream | 3.3.6 | npm | Account Takeover /  | 4%  |
| --- | ------------ | ----- | --- | ------------------- | --- |
Despite public disclosure and removal from package
Bitcoin Stealer
registries, confirmed malicious packages continue to persist
in production, in some cases dating back to 2018. A single
|     | flatmap-stream | 0.1.1 | npm | Malicious  | 3%  |
| --- | -------------- | ----- | --- | ---------- | --- |
malicious package in production can enable credential theft,
Dependency
data exfiltration, or full system compromise. This makes
Injection
even limited exposure a significant organizational risk. Our
analysis shows that organizations are still running known
|     | colors | 1.4.1, 1.4.2,  | npm | Maintainer  | 2%  |
| --- | ------ | -------------- | --- | ----------- | --- |
supply chain threats, exposing persistent gaps in
|     |     | 1.4.44-liberty-2 |     | Storage |     |
| --- | --- | ---------------- | --- | ------- | --- |
dependency governance and remediation practices.
|     | CTX | 0.1.2, 0.2.2,  | PyPl | AWS Takeover /  | 1%  |
| --- | --- | -------------- | ---- | --------------- | --- |
Notably, the most prevalent threats identified originated
from the same trusted maintainer, reinforcing that modern  0.2.6+ AWS Credential
Stealer
supply chain attacks do not always come from unknown
external actors. In many cases, the threat is introduced
larpexodus
through trusted dependencies already embedded within the  0.1 PyPl Typosquatting /  <1%
| application ecosystem. |     |     |     | Infostealer |     |
| ---------------------- | --- | --- | --- | ----------- | --- |
2026 STATE OF APPSEC REPORT   |   11

03
Container
x
Vulnerability Landscape

Container Vulnerable Container Packages
Vulnerability Landscape tar-1.34+dfsg (critical vulnerabilities)
61%
Containers are a foundational component of modern application delivery, but many glibc-2.28 (critical vulnerabilities)
production images are built on outdated and vulnerable base layers. Our research 55%
shows that critical vulnerabilities are deeply embedded in commonly used container
libxml2-2.9.13 (critical vulnerabilities)
packages.
54%
Over 60% of organizations run containers with critical vulnerabilities in core expat-2.1.0 (critical vulnerabilities)
system packages such as tar (61%) and glibc (55%). These components sit at the 52%
foundation of container images and are inherited across applications, meaning a
curl-7.58.0 (critical vulnerabilities)
single vulnerable base image can propagate risk across entire environments.
46%
43% of organizations still run containers with OpenSSL 1.0.1f, a version affected krb5-1.13.2 (critical vulnerabilities)
by Heartbleed and other high-impact vulnerabilities, reflecting the widespread use 44%
of base images that are not regularly updated. This allows well-known, openssl-1.0.1f (critical vulnerabilities)
high-severity vulnerabilities to persist in production workloads.
43%
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 13

CONTAINER VULNERABILITY LANDSCAPE
High/Critical Vulnerability Patching Velocity
Time Unpatched
While container vulnerabilities are widely detected, remediation remains slow and
inconsistent. Our research found that 77% of organizations still have high or 30+ Days
critical container vulnerabilities unpatched after 90 days, revealing a significant
86%
gap between detection and action.
The data shows that delays begin early and compound over time. 86% of 60+ Days
organizations retain high or critical vulnerabilities for more than 30 days, and 81%
81%
continue to carry them beyond 60 days. Organizations that don’t patch
vulnerabilities quickly are unlikely to patch at all.
90+ Days
With the vast majority of organizations (70%) tolerating critical and high-risk
vulnerabilities for months, container vulnerability management has become less 77%
about remediation and more about risk acceptance. Closing this gap requires not
just identifying vulnerabilities, but enabling teams to prioritize and act on the risks
that truly demand immediate attention.
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 14

04
Secrets Management

Secrets Exposure Findings
Valid, active secrets in repositories
31%
Secrets Management
Secrets in git history only (removed but recoverable)
Modern applications rely on secrets, such as API keys, tokens, passwords, and 30%
certificates, to connect services, access data, and automate workflows. As
development velocity increases, secrets management remains a fragile and AWS Secret Access Keys exposed
immature area of AppSec. 14%
Our research shows that secrets are frequently hardcoded, committed to Slack Webhooks exposed
repositories, and retained long after they should be revoked. These exposures 11%
are routinely found in active production code, which creates a direct path
Secrets in CI/CD workflow files
to compromise.
9%
More than 31% of organizations expose valid secrets in source code
GitHub Personal Access Tokens exposed
repositories, while 30% retain secrets in git history, leaving credentials recoverable
9%
by anyone with repository access even after they appear to have been removed.
Once exposed, these secrets often remain active, granting attackers persistent
Secrets echoed to logs
access to internal systems, cloud services, and sensitive data.
4%
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 16

SECRETS MANAGEMENT
| The AI/ML Secrets Crisis  |     |     |     |
| ------------------------- | --- | --- | --- |
The rapid adoption of AI and machine learning has introduced a new  enable intellectual property theft, model poisoning, or the unauthorized
category of secrets exposure. Our analysis found that 43% of production  consumption of expensive GPU resources.
organizations have exposed AI/ML credentials, reflecting how quickly
teams are integrating AI services without establishing proper  Unlike traditional API keys, AI/ML secrets introduce compounding risk.
secrets hygiene. Usage-based billing models can lead to massive, unexpected costs. Access
to proprietary   models represents direct intellectual property theft. And
The risk is amplified by the nature of these services. Hugging Face tokens,  compromised inference endpoints can be abused to generate malicious or
for example, can grant access to private models, internal datasets, and  harmful content attributed to the victim organization.
inference endpoints. A single compromised token can
AI/ML Secrets Exposure by Service
Hugging Face (model hosting, inference APIs)  Anthropic (Claude API)  AWS Bedrock (foundation models)  AWS SageMaker
| 29% | 10% | 4%  | 2%  |
| --- | --- | --- | --- |
OpenAI (GPT, DALL-E, embeddings)  Replicate (model deployment)  Google AI / Vertex AI  Mistral AI
| 18% | 6%  | 4%  | 2%  |
| --- | --- | --- | --- |
Databricks (MLOps, model serving) Modal (serverless ML infrastructure  MLflow (experiment tracking)  Cohere
| 12% | 6%  | 3%  | 1%  |
| --- | --- | --- | --- |
 % OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT   |   17

05
CI/CD Pipeline Security

CI/CD Pipeline Security
CI/CD pipelines sit at the center of modern software delivery,
automating the build, test, and deployment of applications at
speed. As organizations push more logic and credentials into
these pipelines, CI/CD systems have become high-value targets
for attackers, yet security controls have not kept pace with their
growing privilege and reach.
Our research shows that CI/CD pipelines frequently operate with
excessive permissions, limited oversight, and minimal validation
of third-party actions. When compromised, these systems
provide attackers with a powerful launch point into source code,
production infrastructure, and sensitive credentials.
2026 STATE OF APPSEC REPORT | 19

CI/CD PIPELINE SECURITY 1 2
CI/CD Platform Usage
Jenkins
37%
GitHub Actions
31%
5.1 CI/CD Platform Adoption Bitbucket Pipelines
28%
Our research shows broad adoption of CI/CD platforms across production
AWS CodeBuild
organizations, reinforcing the importance of securing these systems as critical
infrastructure. As pipelines become more interconnected with cloud environments, 27%
identity systems, and deployment tooling, misconfigurations in CI/CD platforms
GitLab CI
increasingly translate into production risk.
24%
Without consistent security controls, visibility, and governance, CI/CD platforms AWS CodeDeploy
can unintentionally amplify application risk rather than reduce it. 11%
Bamboo
5%
TeamCity
5%
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 20

CI/CD PIPELINE SECURITY 1 2
GitHub Actions Security
Repositories created before Feb 2023
5.2 GitHub Actions Security
(legacy GITHUB_TOKEN permissions)
GitHub Actions has become a foundational component of modern CI/CD pipelines, 25%
enabling teams to automate workflows through reusable actions and third-party
integrations. However, this flexibility introduces new security challenges when Overly permissive default token permissions
workflows are built on overly permissive permissions and unvalidated components. 22%
Our research found that 25% of repositories still rely on legacy or overly
Actions not limited to verified/trusted sources
permissive GitHub token permissions, increasing the risk of credential abuse and
18%
unauthorized workflow execution. When combined with third-party actions and
automated deployment privileges, these permissions can allow attackers to move
Vulnerable pull_request_target + checkout patterns
from code changes to production access with minimal resistance.
1%
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 21

06
Infrastructure
as Code Security

Infrastructure as Code Security
Infrastructure as Code (IaC) has fundamentally transformed how
organizations deploy and manage cloud resources. As IaC adoption
continues to accelerate, however, security controls have not evolved at
the same pace.
Our research shows that 75% of organizations manage
infrastructure through code. IaC includes cloud-native templates,
Kubernetes manifests, and configuration-driven container deployment.
These misconfigurations introduced through IaC are repeatable,
% automated, and often deployed across multiple
75
environments simultaneously.
Without strong validation and governance, IaC can turn small
configuration gaps into large-scale production risk.
ORGANIZATIONS MANAGE INFRASTRUCTURE
THROUGH CODE
2026 STATE OF APPSEC REPORT | 23

IINNFFRRAASSTTRRUUCCTTUURREE AASS CCOODDEE SSEECCUURRIITTYY 1 2 3 4 5
Infrastructure as Code Platform Usage
CloudFormation
67%
Kubernetes Manifests
6.1 IaC Platform Adoption 58%
Helm Charts
IaC platforms are widely adopted across production organizations, reflecting the
shift toward automated, cloud-native infrastructure management. 75% of 46%
organizations use Infrastructure as Code to deploy cloud resources, reflecting
Terraform
the industry-wide shift toward automated infrastructure management.
41%
This standardization accelerates deployment, but also concentrates risk when IaC Ansible
templates are copied, shared, and reused across environments. In complex 40%
environments, teams may not fully understand the security implications of
Dockerfile
infrastructure changes until after deployment.
23%
Securing IaC platforms is therefore critical to preventing systemic risk across
Docker Compose
cloud environments.
7%
Pulumi
4%
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 24

IINNFFRRAASSTTRRUUCCTTUURREE AASS CCOODDEE SSEECCUURRIITTYY 1 2 3 4 5
Storage and Data Protection Issues
Storage without encryption at rest
84%
Object versioning disabled
6.2 Storage and Data Protection 71%
Secrets stored in plain environment variables
Storage misconfigurations remain one of the most common and impactful risks
introduced through IaC, with potential for data breaches and compliance 68%
violations. Our research found that 84% of organizations deploy unencrypted
Public S3 / Blob / GCS buckets
storage resources through infrastructure code, embedding data exposure directly
63%
into production environments.
No secret rotation configured
In addition, 80% of organizations lack sufficient logging and monitoring 63%
controls for IaC-managed storage. Without encryption and visibility, sensitive
Backup disabled for critical storage
data can be exposed or accessed without detection for extended periods of time.
51%
When insecure storage configurations are codified, data protection failures scale
Publicly exposed database (RDS / Cloud SQL)
as efficiently as infrastructure itself.
39%
Hardcoded secrets in Terraform
8%
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 25

IINNFFRRAASSTTRRUUCCTTUURREE AASS CCOODDEE SSEECCUURRIITTYY 1 2 3 4 5
IAM Configuration Issues
6.3 Identity and Access Management
Cross-account trust without conditions
Identity and access misconfigurations in IaC templates continue to be a leading
61%
source of cloud risk, granting excessive permissions that persist across
deployments. Our research shows that overly permissive IAM roles and wildcard IAM policy allows *:* (full admin)
permissions are frequently deployed via infrastructure templates, increasing the 60%
blast radius of credential compromise.
IAM users without MFA
58%
Once deployed, these permissions are automatically propagated across
environments, allowing attackers to escalate privileges and move laterally at Service account with admin role
speed. In IaC-driven environments, a single misconfigured role can grant
37%
excessive access across large portions of the cloud estate.
IAM role assumable by anyone
Embedding least-privilege IAM controls into infrastructure definitions is essential 7%
to reducing large-scale compromise risk.
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 26

INFRASTRUCTURE AS CODE SECURITY 1 2 3 4 5
Network Security Issues
6.4 Network Security
No logging / monitoring enabled
Network controls such as security groups, firewall rules, and routing policies are 80%
increasingly managed through IaC. While this enables consistency and efficiency,
Open firewall rules (0.0.0.0/0)
it also increases the risk of deploying overly permissive network access at scale.
62%
Our research found that open ingress rules and unrestricted management ports
Security group allows 0.0.0.0/0 on admin ports (22, 3389)
are commonly introduced through IaC. 80% of organizations have no logging or
60%
monitoring enabled, and 62% have open firewall rules, expanding the external
attack surface of cloud environments. EC2 / VM metadata service v1 enabled (SSRF risk)
37%
Without validation and segmentation, network misconfigurations defined in code
can expose entire environments to compromise. Ingress without TLS
20%
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 27

IINNFFRRAASSTTRRUUCCTTUURREE AASS CCOODDEE SSEECCUURRIITTYY 1 2 3 4 5
Container Security in IaC
Containers running as root
6.5 Container Security in IaC
46%
Containers are frequently deployed and managed through IaC, which connects allowPrivilegeEscalation: true
container security to infrastructure definitions. Our research shows that 77% of
43%
organizations retain high or critical container vulnerabilities for more than 90
days, indicating persistent gaps in remediation and runtime security. Containers without read-only filesystem
43%
In addition, insecure container configurations are often embedded directly into IaC
Privileged containers
templates. Once defined, these insecure patterns propagate to every deployment
30%
across clusters and environments.
No resource limits defined
28%
The Shift-Left Gap
Using untagged or 'latest' base images
Despite widespread IaC adoption (75%), security has not kept pace. With
21%
84% of organizations deploying unencrypted storage and 80% lacking
logging, misconfigurations are being codified and replicated at scale. Every HostPath mounted (node filesystem access)
terraform apply or kubectl apply propagates these vulnerabilities
3%
across environments.
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 28

07
Repository
x
and SCM Security

Repository and SCM Security
Source code repositories and source control management (SCM)
platforms form the foundation of modern application development.
They store proprietary code, infrastructure definitions, and credentials
and automation logic that directly impact production environments.
Our research shows that security controls across SCM platforms often
lag behind their critical role in the software supply chain, creating
opportunities for unauthorized code changes, bypassing code review
requirements, or credential theft.
Without consistent governance, validation, and access hygiene,
weaknesses in repositories can propagate rapidly across CI/CD
pipelines and into production systems.
2026 STATE OF APPSEC REPORT | 30

REPOSITORY AND SCM SECURITY 1 2 3
Code Review Configuration Issues
7.1 Code Review and Approval Gaps
Insufficient code review requirements (fewer than 2 reviewers)
Code review and approval processes are the final line of defense against 31%
malicious or accidental changes entering production. However, our research
Code review not limited to code owners
indicates that many repositories lack sufficient enforcement of review
requirements, with over 1 in 4 organizations requiring no code reviews at all. 30%
This allows risky changes to be merged with limited to no oversight.
Re-approval not required after new changes
28%
When pull requests are merged without consistent review, attackers can introduce
backdoors, malicious dependencies, or credential leaks directly into trusted Unrestricted review dismissal (anyone can dismiss approvals)
codebases. In fast-moving development environments, these gaps are often 28%
exploited through compromised accounts or social engineering rather than
No code review required at all
sophisticated exploits.
26%
Without mandatory, enforceable review controls, organizations rely heavily on
GitHub Actions can auto-approve PRs
trust and developer vigilance, which does not scale with modern
13%
development velocity.
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 31

REPOSITORY AND SCM SECURITY 1 2 3
Branch Protection Findings
Signed commits not required
31%
7.2 Branch Protection Weakness
CI/CD checks not required before merge
Branch protection rules are critical to prevent unauthorized or unsafe changes to 26%
critical branches. Despite their importance, our research shows that branch
Branch protection not enabled
protection is frequently incomplete or inconsistently applied across repositories. In
25%
fact, 25% of organizations studied do not have branch protection enabled.
Unrestricted push access to default branch
Weak or missing branch protection allows changes to bypass testing, review, and
24%
policy checks, increasing the likelihood that vulnerable or malicious code reaches
production. In organizations with large repository footprints, inconsistent Force push allowed on default branch
enforcement creates uneven security posture and blind spots attackers can 11%
exploit.
Branch deletion not protected
4%
% OF ORGANIZATIONS
2026 STATE OF APPSEC REPORT | 32

REPOSITORY AND SCM SECURITY 1 2 3
7.3 Access Control and Hygiene
Access to source code repositories is often broader than necessary, with users,
service accounts, and integrations retaining permissions long after they are needed, Access Control and Hygiene Issues
resulting in an expanded attack surface. Our research highlights persistent gaps in
access hygiene, including excessive privileges and stale accounts.
Missing .gitignore file (risk of committing sensitive files)
Over-privileged access increases the blast radius of account compromise, while
24%
unused or unmanaged accounts create silent entry points into the software supply
chain. When combined with limited monitoring and infrequent access reviews, these
conditions make it difficult to detect or respond to unauthorized activity. Too many repository administrators (3 or more)
23%
This is not a novel idea, however it is important to emphasize that maintaining strong
access hygiene, such as least-privilege permissions, regular audits, and timely
offboarding is critical to reducing SCM risk and protecting application code integrity. MFA not enforced for maintainers
11%
The XZ Utils Wake-Up Call
The 2024 XZ Utils backdoor demonstrated how weak repository controls enable % OF ORGANIZATIONS
supply chain attacks. The attacker spent two years building trust before introducing
malicious code. With 31% of organizations not requiring signed commits and 26%
requiring no code review at all, many repositories remain vulnerable to similar patient,
sophisticated attacks.
2026 STATE OF APPSEC REPORT | 33

08
Key
Recommendations

2026 STATE OF APPLICATION SECURITY REPORT
Key Recommendations
This research highlights a growing gap between risk visibility and effective remediation. The recommendations below provide a prioritized roadmap for closing that
gap, focusing on the actions that will most immediately reduce exposure and strengthen long-term application security.
8.1 Immediate Actions (0-30 Days)
Secrets Remediation Critical Vulnerability Patching CI/CD Token Permissions
Identify and rotate all valid secrets across Prioritize remediation of actively exploitable Audit CI/CD authentication tokens and
code repositories, commit history, and CI/CD CVSS 10.0 vulnerabilities, including restrict permissions to the minimum required
environments. Deploy automated secret React2Shell (CVE-2025-55182), Log4Shell, access. Reduce GITHUB_TOKEN scopes,
scanning with blocking controls to prevent and Spring4Shell. Focus first on remove legacy default permissions, and limit
new credentials from being committed or vulnerabilities reachable from production workflows to verified and trusted actions.
exposed. workloads.
2026 STATE OF APPSEC REPORT | 35

2026 STATE OF APPLICATION SECURITY REPORT
Key Recommendations
8.2 Short-term Initiatives (30-90 Days)
Supply Chain Security Controls Repository Hardening IaC Security Gates
Implement dependency scanning with Enforce branch protection on critical Integrate Infrastructure as Code scanning
enforcement for known malicious packages. repositories, require signed commits, and into CI/CD pipelines with blocking policies for
Audit CI/CD workflows for unpinned actions mandate MFA for all maintainers. Implement high-risk misconfigurations, including public
and transitive dependencies. Require lock files CODEOWNERS to ensure sensitive paths storage, open firewall rules, unencrypted
and integrity verification for third- require explicit approval from resources, and overly permissive IAM roles.
party packages. trusted reviewers.
2026 STATE OF APPSEC REPORT | 36

2026 STATE OF APPLICATION SECURITY REPORT
Key Recommendations
8.3 Strategic Improvements (90+ Days)
Container Image Hygiene Zero Trust for CI/CD Pipelines Continue Risk Monitoring
Establish standards for approved base Adopt ephemeral credentials, integrate Deploy runtime security monitoring across
images and enforce regular rebuilds and secrets managers, and eliminate long-lived applications and infrastructure. Establish
updates. Implement automated container tokens from pipelines. Enable full audit baseline behavior, enable comprehensive
vulnerability scanning in registries and logging for all CI/CD actions and logging, and configure alerting to detect
continuously monitor runtime workloads for credential usage. anomalous activity and emerging threats in
high and critical risks. real time.
2026 STATE OF APPSEC REPORT | 37

09
x
Conclusion

2026 STATE OF APPLICATION SECURITY REPORT
Conclusion
The state of application security in 2025–2026 reflects an industry in transition. trust at scale. The 11% malicious package detection rate demonstrates that
Organizations have embraced modern development practices such as even mature organizations remain vulnerable. Incidents like the
cloud-native architectures, infrastructure as code, and automated pipelines, but tj-actions/changed-files compromise further highlight how trusted automation
security maturity has not kept pace with the velocity of change. can turn into an attack vector overnight.
The numbers are sobering. 78% of organizations ship applications with critical The good news is that the most impactful defenses are also the most practical.
vulnerable dependencies, 31% expose valid secrets in code, and 80% lack Enforcing MFA, scanning and rotating secrets, updating dependencies,
adequate logging across their infrastructure. These are not edge cases, they restricting permissions, pinning GitHub Actions to commit SHAs, and
represent the norm across more than a thousand production environments. monitoring continuously can dramatically reduce exposure across the software
supply chain.
Container security paints an equally stark picture. With 77% of organizations
carrying unpatched high or critical container vulnerabilities after 90 days, the The threat landscape will continue to evolve. Attacks will grow more
data reveals a hard truth: organizations that don’t patch quickly often don’t sophisticated, new vulnerability classes will emerge, and attackers will continue
patch at all. These vulnerabilities are being tolerated instead of remediated. to abuse trust relationships embedded in modern development workflows.
At the same time, software supply chain attacks have emerged as the defining Organizations that thrive will be those that build application security into the
threat of this era. The progression from the SolarWinds compromise to DNA of their development process, not as an afterthought, but as a core
self-replicating attacks like Shai-Hulud shows how attackers are exploiting competency.
2026 STATE OF APPSEC REPORT | 39

About Orca Security
Orca enables organizations to make cloud security a strategic
advantage. With the most comprehensive coverage and visibility
across multi-cloud environments, the agentless-first Orca Platform
unites teams to eliminate complexities, vulnerabilities and risks.
____
Backed by Temasek, CapitalG, ICONIQ Capital, Redpoint Ventures
and others, Orca is trusted by hundreds of organizations, including
SAP, Gannett, Autodesk, Unity, Lemonade and Digital Turbine.
To find out more, schedule a
personalized demo of the Orca platform
2026 STATE OF APPSEC REPORT | 40

The path forward requires treating application security
not as a checkbox, but as a fundamental component of
software quality. Every commit, dependency, and
configuration change shapes risk and must be evaluated
through a security lens, with clear context, prioritization,
and accountability across the software lifecycle.”
YOAV ALON
CTO OF ORCA SECURITY

©2026 ORCA SECURITY. ALL RIGHTS RESERVED.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-23", "model": "gemini-3.5-flash-lite"} -->
