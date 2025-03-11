# The State of Secrets Sprawl on GitHub

## Table of Contents
- [Summary](#summary)
- [Secrets Sprawl](#secrets-sprawl)
- [Findings](#findings)
- [Where leaks come from](#where-leaks-come-from)
- [Why](#why)
- [What type of secrets do we find](#what-type-of-secrets-do-we-find)
- [File extensions that cause data breaches](#file-extensions-that-cause-data-breaches)
- [Pro bono alerting](#pro-bono-alerting)
- [What happens after a leak](#what-happens-after-a-leak)
- [Recommendations](#recommendations)
- [To conclude](#to-conclude)
- [About GG Detection Engine, Data Gathering & Methodology](#about-gg-detection-engine-data-gathering--methodology)

## Summary

GitHub has become the central hub for developers, fostering innovation, collaboration, and networking. With over 50 million developers and billions of contributions annually, the platform inevitably faces challenges such as leaked secrets, intellectual property, and personally identifiable information (PII).

Many organizations may overlook the risks associated with public GitHub, assuming their private repositories are secure. However, their developers often have open-source repositories where secrets can be inadvertently exposed.

## Secrets Sprawl

Secrets sprawl is a significant issue as organizations adopt cloud architectures, SaaS platforms, and microservices. Developers handle increasing amounts of sensitive information, including API keys, database connection strings, private keys, and certificates. The complexity of enforcing security practices grows with the organization's size, the number of repositories, and the geographical spread of developer teams.

![Image description: Secrets Sprawl Graphic]

As a result, secrets spread across organizations, often hardcoded into source code, shared via email or messaging systems, saved in config files, or stored in internal wikis. This sprawl increases the risk of attackers moving laterally through infrastructure and makes it difficult to track where secrets end up.

## Findings

GitGuardian has been monitoring every commit pushed to public GitHub since July 2017. In 2020 alone, they uncovered millions of secrets and sent nearly 1 million pro bono alerts to developers.

- **2.5M** public commits scanned/day
- **35%** more repositories created last year
- **25%** more contributions to open-source projects
- Almost **1B** public commits scanned/year

## Where leaks come from

- **85%** of leaks on GitHub occur within public repositories owned by organizations.
- **15%** of leaks occur on developers' personal repositories.

Corporate secrets are often exposed publicly through current or former developers' personal repositories.

**Top 10 Countries Where Leaks Originate:**

1.  United States
2.  India
3.  Brazil
4.  Nigeria
5.  France
6.  Russia
7.  UK
8.  Canada
9.  Bangladesh
10. Indonesia

## Why

Leaks are usually unintentional, resulting from:

-   Developers using a single GitHub account for both personal and professional purposes.
-   Misconfigured git pushing wrong data.
-   Forgetting that the entire git history remains publicly visible even after sensitive data is deleted.

## What type of secrets do we find

Secrets are digital authentication credentials granting access to services, systems, and data. The volume and diversity of these credentials are growing rapidly.

**Types of Secrets Found:**

-   Google keys: **27.6%**
-   Cloud provider (AWS, Azure, Google, etc.): **15.9%**
-   Data storage (MySQL, Mongo, Postgres, etc.): **15.4%**
-   Development tools (Django, RapidAPI, Okta): **11.1%**
-   Private keys: **8.4%**
-   Messaging systems (Discord, Sendgrid, Slack, etc.): **6.7%**
-   Version Control Platform (GitHub, GitLab): **1.9%**
-   Collaboration tools (Asana, Atlassian, Jira, etc.): **0.8%**
-   Social network: **0.4%**
-   Other (CRM, cryptos, identity providers, etc.): **12%**

## File extensions that cause data breaches

-   Top 10 file extensions account for 81% of all results.
-   Top 3 account for over 56%.

**File Extension Categories:**

-   Programming languages: Python, JavaScript, PHP, TypeScript
-   Data serialization files: JSON, XML, YAML, .properties
-   Forbidden or sensitive files: .env, .pem

**Top 10 File Extensions:**

1.  Python: **27.9%**
2.  All others: **19.1%**
3.  JavaScript: **18.8%**
4.  Environment: **9.7%**
5.  JSON: **7.5%**
6.  Properties: **4%**
7.  PEM: **3.6%**
8.  PHP: **3.2%**
9.  XML: **2.2%**
10. YAML: **2.1%**
11. TypeScript: **2%**

## Pro bono alerting

In 2020, GitGuardian sent:

-   **937,539** alerts pro bono.
-   Alerted **558,085** developers pro bono.
-   Found secrets in **860,000** unique commits.
-   Found secrets in **700,000** unique repositories.

## What happens after a leak

-   GitGuardian's algorithm reaction time (Mean Time To Detect): **4 seconds**.
-   Alerts are sent immediately to developers and security teams.
-   Median Time To React: **25 minutes**.

## Recommendations

Companies cannot entirely avoid the risk of secrets exposure, even with centralized secrets management systems. Best practices include:

-   Never store unencrypted secrets in .git repositories.
-   Don't share secrets unencrypted in messaging systems.
-   Store secrets safely.
-   Restrict API access and permissions.

Automated secrets detection is crucial. When choosing a solution, consider:

-   Monitoring developers' personal repositories.
-   Secrets detection performance (accuracy, precision, recall).
-   Real-time alerting.
-   Integration with remediation workflows.
-   Easy collaboration between teams.

## To conclude

Millions of commits occur daily on public GitHub. Organizations need automated detection and efficient remediation tools to focus on relevant information and prevent secrets from ending up in developers' personal repositories.

## About GG Detection Engine, Data Gathering & Methodology
GitGuardian’s secrets detection engine has analyzed billions of commits from GitHub since 2017. The engine is:

- High precision: Minimizes false positives.
- High recall: Minimizes missed secrets.
- Fast: Scans common git repository history in under a minute.
- Community and customer-driven: Constantly trained and improved by feedback.

GitGuardian detects more than 200 different types of secrets[^1].

[^1]: You can find the exhaustive list here: [www.gitguardian.com](http://www.gitguardian.com)
