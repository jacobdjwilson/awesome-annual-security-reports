# State of Secrets Sprawl 2022

## Table of Contents
- [Summary](#summary)
- [Definitions](#definitions)
- [Public Monitoring](#public-monitoring)
  - [How leaky was 2021?](#how-leaky-was-2021)
  - [Leaks correlate to popularity](#leaks-correlate-to-popularity)
  - [Scanning Docker Hub](#scanning-docker-hub)
  - [Fun facts](#fun-facts)
  - [Where leaks come from](#where-leaks-come-from)
  - [2021 breaches involving secrets leaks](#2021-breaches-involving-secrets-leaks)
- [Internal Monitoring](#internal-monitoring)
  - [Security teams are overwhelmed](#security-teams-are-overwhelmed)
  - [A false sense of secrecy](#a-false-sense-of-secrecy)
  - [Recommendations](#recommendations)
  - [Developer in the Loop](#developer-in-the-loop)
  - [Solving the problem of secrets sprawl](#solving-the-problem-of-secrets-sprawl)
- [Let’s conclude](#lets-conclude)
- [About GitGuardian](#about-gitguardian)
- [Methodology](#methodology)
- [Appendix](#appendix)

---

## Summary
The growing problem of secrets sprawling in corporate repositories can only be solved by enabling collaboration between AppSec and Developers.

It’s safe to say that 2021 will go down in history for cybersecurity experts. Ransomware and other large-scale cyberattacks (SolarWinds, Colonial Pipelines) or vulnerabilities (Log4Shell) have made headlines around the world. Software supply chain attacks have seen their number explode, and this comes as no surprise considering the plethora of vulnerabilities and misconfigurations found across software development environments.

Unsurprisingly, a lot of attacks start with the compromise of a leaked secret. Credentials are a nightmare for security engineers because they can end up in so many places: build, monitoring, or runtime logs, stack traces, and … git history. Our data show the extent of publicly exposed secrets on GitHub has more than doubled since 2020. The problem is not bound to this particular platform, as revealed by our Docker Hub analysis.

In 2020, GitGuardian started monitoring private repositories as well, which granted us a unique insight into what really happens behind the scenes. The data reveals that on average, in 2021, a typical company with 400 developers would discover 1,050 unique secrets leaked upon scanning its repositories and commits. With each secret detected in 13 different places on average, the amount of work required for remediation far exceeds current AppSec capabilities: with a security-to-developers ratio of 1:100[^1], 1 AppSec engineer needs to handle 3,413 secrets occurrences on average.

[^1]: From TAG Cyber, see Methodology.

---

## Definitions
- **Secret**: A secret can be any sensitive data that we want to keep private. When discussing secrets in the context of software development, we refer to digital authentication credentials that grant access to services, systems, and data. These are most commonly API keys, usernames and passwords, or security certificates.
- **Secret incident**: A secret incident is a uniquely identified security event that has been determined to have an impact on the organization and necessitates remediation. An incident often has multiple occurrences across files or repositories.
- **Secret occurrences**: A single incident generally encompasses multiple occurrences, which are the various locations across files or repositories where the secret was identified. Occurrences map to the magnitude of the sprawl, and are therefore correlated to the amount of work needed to redistribute the secret after it has been rotated. Occurrences can be assimilated to technical debt.
- **Secrets sprawl**: Unlike traditional credentials, secrets are meant to be distributed to developers, applications, and infrastructure systems. Adding more of these factors will inevitably make the number of secrets used in a development cycle increase, leading to a natural sprawling phenomenon: secrets start to appear hardcoded in source code. From an organization’s point of view, visibility and control over their distribution start to degrade. This is what secrets sprawl is all about.

> "Source code is a huge wealth of knowledge. It also happens to exist on pretty much every developer’s workstation, which they probably take home with them. You probably don’t want your secrets being all over the country." — Don, Security engineer

---

## Public Monitoring
![Statistics on GitHub: 56M users, +25% repositories created, +23% commits scanned]

### How leaky was 2021?
![Chart showing secrets by category: Other, Storage, Data, Cloud provider, Private key, Development tool, Messaging system, Version control]

- **6M+ secrets** detected in 2021.
- **2x increase** compared to 2020.
- On average, 3 commits out of 1,000 exposed at least one secret, +50% compared to 2020.

### Leaks correlate to popularity
It should come as no surprise that leaks are proportional to user adoption, and this is especially true for newcomers rapidly gaining in popularity. Supabase and PlanetScale are cited as examples of rapid growth correlating with increased secret detection.

### Scanning Docker Hub
Docker Hub has become a favorite for developers. The layers making up Docker images are additional attack surfaces.
- 4.62% of images expose at least one secret.
- 10K images scanned, 1.2K secrets, 6100 unique layers.

### Fun facts
- Leaks mostly happen on weekends.
- If we exclude weekends, most leaks happen on holidays.
- We found more than 500 commit messages containing GitHub personal access tokens!

### Where leaks come from
1. India
2. USA
3. Germany
4. France
5. Indonesia
6. Russia
7. Nigeria
8. Bangladesh
9. Brazil
10. UK

### 2021 breaches involving secrets leaks
- **Codecov**: Attackers extracted a static GCP service account credential from a Docker image layer.
- **Twitch**: Nearly 7,000 secrets were uncovered in the leaked codebase, including AWS, Google, Stripe, and GitHub keys.
- **Indian government**: 35 separate instances of exposed credential pairs were found inside public-facing .git directories.

---

## Internal Monitoring
In 2020, GitGuardian launched Internal Repositories Monitoring for Enterprise. Monitoring thousands of repositories in real-time, we gained a realistic view of the state of application security in the DevOps era.

> "Secrets detection is a very essential part of security. It’s one of the basics that you need to cover all the time. Otherwise, you’re going to expose your endpoints online and you’re going to suffer endless attacks." — Abbas Haidar, Head of InfoSec

### Security teams are overwhelmed
On average, in 2021, a typical company with 400 developers and 4 AppSec engineers would discover 1,050 unique secrets leaked. 1 AppSec engineer needs to handle 3,413 secrets occurrences on average.

### A false sense of secrecy
Private repositories are 4x more likely to reveal at least one incident compared to public ones.
![Chart comparing incidents on public vs private repositories for Azure, AWS, Salesforce, and Okta]

### Recommendations
To prevent codebases from becoming hackers’ playgrounds, the focus needs to shift to collaborative prevention. With enough discipline and education, coupled with the right tools, it is possible to drastically improve the situation.

### Developer in the Loop
"Developer in the Loop" allows security engineers to share an incident with the developer who committed the secret.
- Involving the developer results in an incident closing rate 72% higher.
- Median Time to Remediate is divided by 2.

### Solving the problem of secrets sprawl
1. Monitor commits and merge/pull requests in real-time.
2. Enable pre-receive checks to "stop the bleeding."
3. Educate about using pre-commit scanning.
4. Plan a long-term strategy for historical git scans.
5. Implement a Secrets Security Champion program.

---

## Let’s conclude
Secrets sprawl is a growing phenomenon. Version control systems are becoming a top target for hackers. There is an urgency to remove secrets from source code by sharing the application security responsibility between developers, security, and ops.

---

## About GitGuardian
Founded in 2017 by Jérémy Thomas and Eric Fourrier, GitGuardian is the leader in secrets detection. It is the #1 security application on the GitHub Marketplace with more than 150K installs.

---

## Methodology
- **Secrets detection engine**: GitGuardian detected over 6M secrets on public GitHub in 2021. The engine is language-agnostic and uses over 350 specific detectors.
- **AppSec to Developers ratio**: Based on TAG Cyber research, an average ratio of 1:200 was used.
- **Docker Hub**: Scanned 10K random Docker images.
- **Internal Monitoring**: Based on historical scans of enterprise accounts.

---

## Appendix
List of common secrets detected:
- Alibaba Cloud Keys, Artifactory Token, Auth0 Keys, AWS Keys, Bitbucket Keys, Cloudflare API Credentials, Confluent Keys, Datadog API Credentials, DB2 Credentials, DigitalOcean (OAuth, Spaces, Token), Dropbox App Credentials, Facebook (Access Token, App Keys), GitHub (Access Token, App Keys, OAuth App Keys), GitLab (Enterprise Token, Token), Google Cloud Keys, HubSpot API Key, Intercom Access Token, Jira Basic Auth, Kubernetes Cluster Credentials, LDAP Credentials, MariaDB Credentials, Microsoft Azure Storage Account Key, Microsoft Teams webhook, MongoDB Credentials, MSSQL Credentials, MySQL Credentials, npm Token, NuGet API Key, ODBC Connection String, Okta (Keys, Token), Oracle Credentials, PayPal OAuth2 Keys, PostgreSQL Credentials, Python Package Index Key, Redis Credentials, Salesforce (Oauth2 Keys, Refresh Tokens), SendGrid Key, Slack (App Token, Application Credentials, Bot Token, Signing Secret, User Token, Webhook URL), SMTP credentials, Snowflake Credentials, Splunk Authentication Token, Tencent Cloud Keys, Terraform Cloud Token, Twilio (Keys, Master Credentials), VISA Basic Auth, Zendesk Token.