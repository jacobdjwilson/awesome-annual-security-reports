# The State of Secrets Sprawl 2024

**Organization**: GitGuardian  
**Year**: 2024

## Table of Contents
- [Foreword](#foreword)
- [2023 Map of Leaks](#2023-map-of-leaks)
- [Industry Leaks](#industry-leaks)
- [Secrets Detectors](#secrets-detectors)
- [Focus: GenAI Secrets Leaks](#focus-genai-secrets-leaks)
- [Ranking File Extensions by Their Leakiness](#ranking-file-extensions-by-their-leakiness)
- [What Happens After a Secret Leaks?](#what-happens-after-a-secret-leaks)
- [Remediation Efforts](#remediation-efforts)
- [Revoked secrets](#revoked-secrets)
- [Zombie Leaks: a Hidden Threat](#zombie-leaks-a-hidden-threat)
- [DMCA Takedown Notices: a Last Resort to Stop Leaks?](#dmca-takedown-notices-a-last-resort-to-stop-leaks)
- [AI for Secrets Detection](#ai-for-secrets-detection)
- [How Good Can LLMs Be at Detecting Secrets?](#how-good-can-llms-be-at-detecting-secrets)
- [Powering Secrets Detection with AI: GitGuardian’s Approach](#powering-secrets-detection-with-ai-gitguardians-approach)
- [Are You Sure to Know Where Your Secrets Are?](#are-you-sure-to-know-where-your-secrets-are)
- [Unveiling Secret Exposures with HasMySecretLeaked](#unveiling-secret-exposures-with-hasmysecretleaked)
- [Solving Secrets Sprawl](#solving-secrets-sprawl)
- [Awareness & Training](#awareness--training)
- [Combining Secrets Detection & Management](#combining-secrets-detection--management)
- [Preventing Leaks & Breaches](#preventing-leaks--breaches)
- [About GitGuardian](#about-gitguardian)
- [Appendix](#appendix)
  - [Definitions](#definitions)
  - [Methodology](#methodology)

---

## Foreword

It is not a secret. Hard-coded credentials have long been a primary cause of security incidents in the software world. Yet, with the growing complexity of digital supply chains, secrets sprawl is the Achilles’ heel for organizations of all sizes and security postures.

GitGuardian has been at the forefront of identifying and reporting hard-coded secrets for the past four years. Remarkably, the incidence of publicly exposed secrets has quadrupled in this time, with a staggering 12.8 million occurrences detected on GitHub.com in the last year alone—a 28% increase from 2022.

> “[In 2023] for the first time, compromised credentials took the top spot in root causes [of attacks]. In the first six months, compromised credentials accounted for 50% of root causes, whereas exploiting a vulnerability came in at 23%.”
> — Verizon’s 2023 Data Breach Investigations Report

> “49% of breaches by external actors involved Use of stolen credentials, while Phishing made up 12% of external attacks. Attackers used the Exploit vulnerability technique in 5% of breaches.”
> — Sophos’ 2023 Active Adversary Report

The proliferation of 50 million new code repositories on GitHub, a 22% increase from last year, amplifies the risk of both accidental exposures and deliberate malicious acts. This reality underscores the vital need for companies to track and manage the exposure of their sensitive information. Too many remain vulnerable to breaches without awareness or means to mitigate them.

Our research sheds light on a concerning trend: 90% of exposed valid secrets remain active for at least five days after the author is notified.

This finding emphasizes a crucial lesson in code security: while detecting vulnerabilities is critical, the real challenge lies in remediation. Security, we believe, must be a shared responsibility across all stages of the Software Development Life Cycle (SDLC), not just the domain of specialized teams. Raising awareness about these seemingly minor lapses is essential for mitigating supply chain risks.

When 507 IT decision-makers were asked, “Have you ever been impacted by, or heard of secrets (API keys, username and passwords, encryption keys, etc.) leaking within your organization?” the responses highlighted widespread concern:
- 75% of respondents reported experiencing a secret leak.
- 60% reported leaks impacting the company or its employees.
- 47% identified “Hard-coded secrets” as key risk points in their software supply chain.

As our world becomes increasingly digital, and as secrets continue to underpin the trustworthiness of digital systems, closing the remediation loop is imperative for securing a safer digital future.

### How Leaky Was 2023?

All the metrics featured in this report have been meticulously filtered to ensure they precisely depict the current state of secrets sprawl. For a comprehensive understanding of our methodology, please refer to the appendix.

- **4.6% of active repositories leaked a secret in 2023**: On 67,243,678 active repositories, 3,066,304 leaked a secret.
- **More than 1 in 10 commit authors leaked a secret**: Out of the 14,978,367 distinct authors who contributed, 1,749,398 (11.7%) leaked a secret.
- **1.8M pro-bono alert emails (+23.5%)**: GitGuardian sent 1,854,834 pro-bono alert emails following the detection of an exposed secret for the first time. Out of these, only 33,242 secrets were revoked within 5 days. GitGuardian stops tracking the status of secrets after these 5 days.

## 2023 Map of Leaks

![Map of global secret leaks]

## Industry Leaks

Leveraging its advanced proprietary algorithm, GitGuardian has successfully traced many secret occurrences back to their respective companies. This capability extends to incidents where secrets were leaked outside the company-owned repositories. Through this sophisticated mapping process, GitGuardian provides insightful data on the prevalence of leaks across different industries:

Unsurprisingly, the IT sector, which includes software vendors, accounts for 65.9% of all detected leaks. Following IT, the education sector is responsible for 20% of the leaks, reflecting the growing digitization and reliance on technology within academic institutions. The remaining 14% of leaks are evenly divided between the Science & Technology fields and other industries.

## Secrets Detectors

GitGuardian differentiates specific secrets from generic ones (see the definitions in the appendix). In 2023, specific occurrences were up 16.7%, while generic occurrences were up 37%.

### Generic Detectors
For the purposes of this report, we intentionally omitted a certain percentage of generic secrets. Consequently, the ratio of specific to generic detectors does not precisely represent the prevalence of generic secrets in our overall detection results.

Indeed, as Pierre Lalanne, Engineering Manager at GitGuardian, notes:
> “Overall, generic detectors account for 45.4% of all the secrets we detect.”

💡 Leveraging a promising machine learning algorithm, the GitGuardian AI/ML team was able to categorize Generic High Entropy and Generic Password secrets.

### Specific Detectors
Looking specifically at specific detectors, we found over 1M valid Google API secrets (occurrences), 250K Google Cloud, and 140K AWS IAM.

🦉 **Fun Fact**: Ironically, GitHub became its own cautionary tale when it inadvertently leaked its RSA SSH host key for GitHub.com right on GitHub.com! GitHub caught it quickly and replaced the key to ensure operations remained secure. It just goes to show, nobody’s immune to the occasional slip-up, not even the experts!

## Focus: GenAI Secrets Leaks

OpenAI, the powerhouse behind the widely recognized ChatGPT, DALL-E, and the newer Sora generative AI tools, has seen its services soar in popularity well beyond the tech world. It’s hardly surprising that API keys for programmatically accessing these tools have proliferated across GitHub, becoming a common sight.

In 2023, GitGuardian observed a 1212x increase in the number of OpenAI API key leaks from previous year, unsurprisingly making them the highest-growth detector.

OpenAI remains the most utilized AI service, evidenced by the alarming average of 46,441 API key occurrences leaked each month in 2023. This figure significantly surpasses the leakage rates of other AI services we monitored throughout the year, such as Cohere, Claude, Clarifai, Google Bard, Pinecone, and Replicate.

## Ranking File Extensions by Their Leakiness

To better understand which file types are most likely to leak secrets, we adopted a risk-based approach. The core of this method involves calculating the likelihood that a file with a specific extension will expose a secret.

![Chart showing file extension probability to expose a secret]

For example, this score indicates that whenever GitGuardian scans an “.env” file, there’s a 54% chance that it will result in the detection of a secret.

## What Happens After a Secret Leaks?

When someone exposes a secret on public GitHub, they should consider it compromised. The author must revoke the secret quickly to reduce the impact of the incident.

### Remediation Efforts
In 2023, GitGuardian monitored how well authors fixed leaks. The tracking started when the first valid occurrence of a secret was detected and ended five days later. The common trend is troubling: **More than 90% of the secrets remained valid 5 days after being leaked.**

GitGuardian found that after 5 days, 91.6% of the secrets remained valid. Also, just 2.6% of the secrets were revoked within 1 hour of notification via email.

### Revoked secrets
This analysis reveals that leaked WeChat App and Algolia keys are the most likely to remain exposed for over 5 days. Conversely, developers are more concerned about the risks of leaking Stripe or Cloudflare API keys.

A noteworthy finding is that 58.5% of OpenAI API keys are still valid 5 days after being leaked. Likewise, only 33.4% of valid AWS IAM keys are revoked within the initial five days.

### Zombie Leaks: a Hidden Threat
A zombie leak occurs when a secret is exposed but not revoked, remaining a potential attack vector. The commit author may believe that deleting the commit or repository is sufficient, overlooking the crucial revocation step.

## DMCA Takedown Notices: a Last Resort to Stop Leaks?

In 2023, GitHub received 2,085 DMCA takedown notices, and 2,050 of the repositories mentioned in these notices were taken down: of these, 255 (12.4%) exposed at least one secret. Between 2021 and 2023, the percentage of takedown requests that involved a repository with an exposed secret increased by 37.8%.

## AI for Secrets Detection

Could foundational models effectively replace human-developed engines for tackling secrets sprawl? This chapter explores whether LLMs models could serve as an alternative to traditional secret detection tools.

### How Good Can LLMs Be at Detecting Secrets?
- **Operating Scale**: GitGuardian scans ~10M public documents per day. This volume challenges the rate limits set by OpenAI for their foundational models.
- **Performance**: We conducted a test with 1,000 known valid secrets. ChatGPT failed to recognize 15.2% of the secrets, demonstrating less-than-ideal recall. Furthermore, ChatGPT’s precision was significantly low, flagging an excessive number of files as false positives.

## Powering Secrets Detection with AI: GitGuardian’s Approach

Make no mistake: AI represents a revolutionary shift in the field of secrets detection. However, our conviction lies in the power of combining AI with our specialized secrets detection engine to unlock true value.

- **Categorize Generic Secrets**: GitGuardian is leveraging AI to classify generic secrets. For instance, we found that 66.7% of exposed passwords are related to database storage.
- **Improving Precision and Recall**: GitGuardian’s ML team is developing a model to accurately score the likelihood of a genuine generic secret versus a false positive.

## Are You Sure to Know Where Your Secrets Are?

### Unveiling Secret Exposures with HasMySecretLeaked
HasMySecretLeaked is a pioneering free service designed to allow security practitioners to proactively check if their secrets have been exposed on GitHub.com. It leverages GitGuardian’s comprehensive database, which includes over 20 million records of leaked secrets found across GitHub since 2017.

The result of our study: **3.11% of the secrets leaked in private repositories were also exposed in public repositories.**

## Solving Secrets Sprawl

### Awareness & Training
Cultivating secure coding practices is an ongoing process. Informal “lunch and learns” are highly effective. These sessions can raise awareness and foster a shared understanding of security issues without creating overwhelming pressure.

### Combining Secrets Detection & Management
Secrets management tools are essential for maintaining good credential hygiene, providing a secure, central location for storing, distributing, and rotating secrets. However, these tools cannot guarantee their use and may be bypassed.

## Preventing Leaks & Breaches

A multi-layered detection strategy is crucial for preventing hard-coded secrets and ensuring robust security.

- **GGshield**: The GitGuardian command-line interface (CLI) was designed to detect hard-coded secrets in pre-commit hooks. In 2023, ggshield prevented 417K policy breaks per month.
- **Honeytokens**: Honeytokens are decoy credentials acting as tripwires, revealing attacker information without granting access to real customer resources.

## About GitGuardian

GitGuardian is the security platform for the DevOps generation. GitGuardian enables security teams to define and enforce secure coding practices consistently and globally at every step of the software development process.

## Appendix

### Definitions
- **Secret**: Any sensitive data we want to keep private (API keys, username/password combos, private keys).
- **Occurrence**: A specific instance of a secret found in a file or repository.
- **Detector**: A set of rules that filter documents for secrets.
- **Specific detector**: Designed to detect secrets for a specific provider (e.g., AWS).
- **Generic detector**: Designed to catch a broad variety of secrets that cannot be tied to a specific service.

### Methodology
All GitHub metrics are extracted from the State of the Octoverse 2023. The study perimeter was filtered to eliminate generic false positives. For file extension risk scores, we utilized a probabilistic risk score based on Bayes theorem. Password strength was calculated using entropy in bits.

---
*© 2024 GitGuardian. All Rights Reserved.*