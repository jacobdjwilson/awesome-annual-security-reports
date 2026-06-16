# THE STATE OF SECRETS SPRAWL 2023

Organization: GitGuardian  
Year: 2023

## Table of Contents
- [Foreword](#foreword)
- [A look back at 2022 major incidents](#a-look-back-at-2022-major-incidents)
- [How leaky was 2022?](#how-leaky-was-2022)
- [How does secrets sprawl threaten software supply chain security?](#how-does-secrets-sprawl-threaten-software-supply-chain-security)
- [From code to cloud: Infrastructure as code](#from-code-to-cloud-infrastructure-as-code)
- [Measuring time-to-hacked: our experiment with honeytokens](#measuring-time-to-hacked-our-experiment-with-honeytokens)
- [Fun facts](#fun-facts)
- [Insight from DarkOwl: The hidden economy of credentials on the darknet](#insight-from-darkowl-the-hidden-economy-of-credentials-on-the-darknet)
- [Taming Secrets Sprawl in the SDLC](#taming-secrets-sprawl-in-the-sdlc)
- [What’s a good strategy for mitigating hard-coded secrets?](#whats-a-good-strategy-for-mitigating-hard-coded-secrets)
- [Conclusion](#conclusion)
- [About GitGuardian](#about-gitguardian)
- [Appendix](#appendix)

---

## Foreword

Hard-coded secrets have never been a more significant threat to the security of people, enterprises, and even countries worldwide. IT systems, open-source, and entire software supply chains are vulnerable to exploiting keys left by mistake in source code.

As the world digital footprint grows, millions of such keys accumulate every year, not only in public spaces such as code-sharing platforms but especially in closed spaces such as private repositories or corporate IT assets. In other words, secrets sprawl on GitHub is only the tip of the iceberg.

This wouldn’t be so concerning if credentials theft weren’t the most common cause of data breaches. The 2022 editions of Verizon’s DBIR and the IBM Cost of a data breach reports highlighted that this attack vector had remains the top concern since 2021:

> Use of stolen or compromised credentials remains the most common cause of a data breach. Stolen or compromised credentials were the primary attack vector in 19% of breaches in the 2022 study and also the top attack vector in the 2021 study, having caused 20% of breaches. Breaches caused by stolen or compromised credentials had an average cost of USD 4.50 million.[^1]

Secrets are not just any kind of credentials; they are the keys to obtaining privileged access to secure systems. Because of the leverage they provide, they are hackers’ most sought-after information. However, many infosec incidents that occurred in 2022 pointed to how inadequate their protection is.

[^1]: From the IBM Cost of a data breach 2022

---

## A look back at 2022 major incidents

Secrets are found in one way or another in most of the security incidents that happened in 2022. We can classify them into three categories:

### Secrets exploited in an attack
- **Uber**: An attacker breached Uber and used hard-coded admin credentials to log into Thycotic, the firm’s Privileged Access Management platform. They pulled a full account takeover on several internal tools and productivity applications. (Sep. 15)
- **CircleCI**: An attacker leveraged malware deployed to a CircleCI engineer’s laptop to steal a valid, 2FA-backed SSO session. They could then exfiltrate customer data, including customer environment variables, tokens, and keys. (Dec. 29)

### Stolen source code repositories
- **NVIDIA**: NVIDIA source code is leaked by the “Lapsus$” group. (Feb. 25)
- **Samsung**: 200GB of Samsung source code is leaked, revealing 6,695 hard-coded secrets. (Mar. 7)
- **Microsoft**: 250 Microsoft projects are leaked, revealing 376 hard-coded secrets. (Mar. 22)
- **LastPass**: LastPass source code is stolen, leaking credentials and keys used months later to access and decrypt storage volumes. (Aug.-Dec.)
- **Okta**: Okta admitted a breach of its GitHub repositories resulting in source code theft. (Dec. 21)
- **Slack**: Slack employee tokens are stolen and misused to download private code. (Dec. 7)

### Secrets exposed publicly
- **Android Apps**: Research reveals 18,000+ Android apps leak hard-coded secrets. (Sep. 1)
- **Toyota**: Toyota disclosed a contractor exposed a credential giving access to user data on GitHub for five years. (Oct. 7)
- **Infosys**: Tom Forbes disclosed Infosys leaked FullAdminAccess AWS keys on PyPi for over a year (and then 57 other AWS keys on PyPi). (Nov. 16)
- **Dropbox**: Dropbox disclosed that 130 stolen code repositories contained API keys. (Nov. 1)

---

## How leaky was 2022?

![Infographic showing 10 million new secrets detected in public GitHub commits in 2022, a 67% increase from 2021.]

- **1.027B** commits scanned by GitGuardian (+20% compared to 2021).
- **85.7M+** new repositories on GitHub in 2022 (+20%).
- **94M** developers (+27%).
- **HCL (Hashicorp Configuration Language)** is the fastest-growing language on GitHub.

### Key Statistics
- **1 in 10** authors exposed a secret in 2022.
- **10M** secret occurrences detected in 2022 (3M unique secrets).
- **5.5** commits out of 1,000 exposed at least one secret (+50%).
- **3.7%** of repositories active during 2022 leaked a secret.

![Chart showing the growth of secrets sprawl from 2020 to 2022.]

### Debunking a myth: hard-coding secrets is a junior developer mistake.
It is a common myth that hard-coded secrets are committed mainly by junior developers. The reality is that this can happen to any level of developer. Hard-coding secrets is often a result of convenience. Senior developers, who might be simply testing a database connection or an endpoint, are under tremendous pressure to deliver quickly.

---

## How does secrets sprawl threaten software supply chain security?

When weighing the risk posed by secrets sprawl, it’s essential to consider the ensemble of hard-coded plaintext secrets rather than individual secrets taken separately.

An excellent example of this principle was demonstrated in research by Ronen Shustin and Shir Tamari from Wiz, a cloud security vendor. They use the image of a keychain to illustrate the concept: the collection of one or more scattered secrets the attacker finds throughout the target environment.

They discovered a vulnerability, dubbed **“Hell’s Keychain,”** that combined three exposed secrets and a network misconfiguration in IBM Cloud Databases for PostgreSQL. This would have allowed them to compromise IBM Cloud’s internal image-building process to finally read and modify the data stored in every instance of IBM Cloud Databases for PostgreSQL databases.

---

## From code to cloud: Infrastructure as code

Infrastructure as code (IaC) is the abstraction layer used to declare the final/desired state of IT infrastructure with code.

- **28%** increase in IaC-related contributions on GitHub in 2022.
- **Distribution of IaC filetypes**: Dockerfile (32.5%), Cloudformation (31.9%), Azure Resource Manager (18.9%), Ansible (9%), Docker compose (6.2%).

### Shifting left: Infrastructure as code security
We found that Terraform files had an average of 5.57 occurrences of secrets per 1,000 patches.

**The most common IaC vulnerabilities are:**
1. **Networking misconfigurations**: Unrestricted egress or ingress traffic.
2. **Data exposure misconfigurations**: S3 buckets without encryption.
3. **Secrets**: Exposing a sensitive environment variable.
4. **Permission misconfigurations**: Using the default service account.

---

## Measuring time-to-hacked: our experiment with honeytokens

GitGuardian conducted an experiment by leaking two types of honeytokens (canary tokens) on GitHub: a set of AWS IAM credentials and PostgreSQL credentials.

- The first attempt occurred **2 seconds** after publicly exposing the credentials.
- In total, 24 IPs requested AWS IAM information using the credentials in the first 9 hours after the leak.

---

## Fun facts

![Chart showing the correlation between the buzz around OpenAI/ChatGPT and the number of OpenAI API keys detected.]

---

## Insight from DarkOwl: The hidden economy of credentials on the darknet

The darknet facilitates a complex ecosystem of cybercrime. “Secret” data, including tokens and keys found on open repositories such as GitHub, are easily re-sold on the darknet and deep web.

- **BreachForums**: Leaked data is offered for download via vendor-specific currency or by sharing other breached data.
- **DarkOwl Data (Jan 2023)**: Identified 11,246 unique exposed API keys for AWS alone.
- **Total records**: Over 9.3 billion emails and 5 billion plaintext passwords tracked in their database.

---

## Taming Secrets Sprawl in the SDLC

Organizations serious about taming secrets sprawl must work on three fronts:
1. **People**: Ensure Dev, Sec, and Ops are trained on secure coding best practices.
2. **Processes**: Establish a secure software development lifecycle (S-SDLC).
3. **Tools**: Use technologies such as detection, encryption, tokenization, and dynamic key rotation.

---

## What’s a good strategy for mitigating hard-coded secrets?

1. **Monitor**: Scan commits and merge/pull requests in real-time.
2. **Harden**: Enable pre-receive checks to stop the bleeding.
3. **Educate**: Use pre-commit scanning as a seatbelt for individuals.
4. **Plan**: Develop a strategy for historical analysis.
5. **Champion**: Implement a secrets’ security champion program.

---

## Conclusion

Secrets sprawl continues accelerating. With 10 million secrets discovered in public GitHub commits, this is one of the biggest threats to the security of the digital world. Companies must bring security and development closer and advance towards an application shared responsibility.

---

## About GitGuardian

GitGuardian is a code security platform that provides solutions for DevOps generation. It is the #1 security application on the GitHub Marketplace, trusted by companies including Instacart, Snowflake, Orange, and DataDog.

---

## Appendix

### Definitions
- **Secret**: Digital authentication credentials that grant access to services, systems, and data (e.g., API keys, passwords).
- **Occurrence**: A single instance of a hard-coded secret detected in a file or repository.
- **Secret incident**: A uniquely identified security event that necessitates remediation.
- **Supply chain security**: Securing each link in the logistical pathway from source code to production.
- **Infrastructure as code security**: Bridging the gap between Security, Operations, and Development to prevent misconfigurations.

### Methodology
- **Octoverse 2022**: Data period 01/01/2021 to 09/30/2022.
- **GitGuardian Data**: Period 01/01/2021 to 12/31/2022.
- **IaC Vulnerabilities**: Study dataset comprised 6,311 git repositories hosting Terraform files.

### About DarkOwl
DarkOwl is a Denver-based information security company specializing in darknet OSINT tools. For more information, visit [www.darkowl.com](http://www.darkowl.com).