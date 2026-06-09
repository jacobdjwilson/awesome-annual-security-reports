# State of Code Security Report 2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [2024: Year in Review](#2024-year-in-review)
- [Current Landscape](#current-landscape)
- [Methodology](#methodology)
- [Overall Usage: Key Findings](#overall-usage-key-findings)
- [VCS Trends: GitHub dominates, multi-platform strategies are on the rise](#vcs-trends-github-dominates-multi-platform-strategies-are-on-the-rise)
- [The ratio of public repos in GitHub is 3 times higher than in other VCS platforms](#the-ratio-of-public-repos-in-github-is-3-times-higher-than-in-other-vcs-platforms)
- [Repositories: Key findings](#repositories-key-findings)
- [Secrets in public repositories are only the tip of the iceberg](#secrets-in-public-repositories-are-only-the-tip-of-the-iceberg)
- [Cloud keys represent a big part of exposed secrets](#cloud-keys-represent-a-big-part-of-exposed-secrets)
- [Scripting languages are more popular than programming languages](#scripting-languages-are-more-popular-than-programming-languages)
- [CI/CD security: The story of insecure defaults](#cicd-security-the-story-of-insecure-defaults)
- [One in every 10 organizations has GitHub Actions enabled](#one-in-every-10-organizations-has-github-actions-enabled)
- [Around 80% of workflow permissions in repositories are insecure](#around-80-of-workflow-permissions-in-repositories-are-insecure)
- [Branch protection is weak, false sense of security exists in public repos](#branch-protection-is-weak-false-sense-of-security-exists-in-public-repos)
- [Self-hosted runners in cloud present a serious risk to 35% of enterprises](#self-hosted-runners-in-cloud-present-a-serious-risk-to-35-of-enterprises)
- [GitHub Actions – no limits](#github-actions--no-limits)
- [Dangerous permission scopes are prevalent in GitHub Apps](#dangerous-permission-scopes-are-prevalent-in-github-apps)
- [How Wiz Can Help](#how-wiz-can-help)
- [Conclusion](#conclusion)

## Executive Summary

For this report, Wiz researchers examined the ratio of public versus private repositories, occurrence of secrets in code, GitHub Apps security, workflow security settings, and more. In the following pages we will present our findings and draw some conclusions. Here is a preview of the most impactful takeaways stemming from this effort:

- Even “best case scenario” numbers show a worrisome habit of keeping cloud secrets in code repositories. Alarmingly, 61% of organizations have secrets exposed in public repositories. A threat actor scanning public repos could stumble across these secrets – which might include SaaS API keys, access tokens, or cloud credentials – and exploit them to wreak havoc. For instance, with a leaked AWS access key an attacker could extract sensitive data from cloud storage, incurring significant financial loss and reputational damage.
- Version Control Systems (VCS) and CI/CD security posture practices are lacking, with workflows and actions boasting high privileges. This is extremely concerning because it is an important part of the software development lifecycle and involves direct access to the production environment.
- Not all VCS are created equal – at least not when it comes to security. GitHub is not only the leader by number of repositories, but also by percentage of public repositories (over 30%). That creates an appealing target for malicious actors, and the potential for catastrophe.

Throughout the process of collection and analysis, it became clear that the broader connection between code repositories and cloud environments provides essential context for interpreting the statistics. Some examples:

- Weak security practices around self-hosted runners, which require particular attention. Runners serve as the middle ground between code and cloud, and can allow attackers to pivot in either direction.
- Code repositories with cloud and SaaS secrets leading to cloud environments.
- Vulnerabilities in code repositories manifesting themselves post-deployment, in cloud.

As such, the report illustrates the reality that code and cloud are two deeply connected domains in today’s agile, cloud-native world.

## 2024: Year in Review

The past 12 months have been noteworthy for both the number and impact of supply chain attacks. Arguably, the most prominent one was an attack on XZ Utils that exposed the security community to the lengths which malicious actors are willing to go to plant a well-hidden backdoor in a widely used software package.

![Figure 1: xz-utils attack flow]

This incident made headlines worldwide because it illustrated the dangers of an inside actor. A somewhat overlooked angle of this attack is the “disgruntled employee” scenario. We believe the answer lies in multi-layered VCS defenses – for example, branch protection and PR reviews in addition to the default authentication – and behavioral monitoring of users.

Unlike the XZ Utils incident, exposed secrets are a well-known and well-researched attack vector. This does not prevent attackers from continuing to abuse leaked secrets for their leverage. These are great examples of the visibility problem – security scanners must have visibility into all repositories and must know how to validate secrets and estimate the secret impact.

Other supply chain attacks this year targeted the NPM and PyPI ecosystems. A rarer attack made waves this summer: a Chinese company named Funnull acquired the Polyfill domain and GitHub repo, and inserted malware into polyfill.js that redirected users to gambling websites.

Finally, the CI/CD security research community benefitted from some great findings presented at industry conferences, such as “Self-Hosted GitHub CI/CD Runners: Continuous Integration, Continuous Destruction” and “H-MY-DC: Abusing OIDC all the way to your cloud”.

## Current Landscape

### Methodology
This report includes insights from Wiz Research based on data collected throughout 2024. Over this period of time, hundreds of thousands of code repositories were analyzed. We gained these insights in large part from the release of Wiz Code, which granted us a unique opportunity to connect cloud deployments with their source code.

### Overall Usage: Key Findings

#### GitHub leads the pack with 80% of total repos
![Repositories by platform]

#### VCS Trends: GitHub dominates, multi-platform strategies are on the rise
- Only about 5% of the organizations use more than one platform.
- Of those, only a few organizations in our sample set have all three platforms installed, the rest have two platforms.
- Of those with more than one platform, all but a few have GitHub as one of the platforms.

#### The ratio of public repos in GitHub is 3 times higher than in other VCS platforms
The percentage of public repositories is about 35% in GitHub and less than 10% in other platforms. 

![Public vs. private repo ratios]
![Public vs. private repo ratios - filtered]
![Organizations without any public repo]

### Repositories: Key findings

#### Secrets in public repositories are only the tip of the iceberg
While it is heartening to see the number of secrets drop between private and public repos (from 7% to 2%), even private repos are not a good place to store secrets.

![Secrets in repositories]

#### Cloud keys represent a big part of exposed secrets
The numbers confirm our suspicions that cloud keys, albeit in a smaller amount, can still be found in private and public repositories.

![Secrets in Private Repositories]
![Secrets in Public Repositories]
![Sensitive Data in Repositories]

#### Scripting languages are more popular than programming languages
Numbers point to the relative popularity of scripts and markup languages, whereas Java, the most popular compiled language, comes in at only seventh.

![Languages in private vs. public repositories]

### CI/CD security: The story of insecure defaults

#### One in every 10 organizations has GitHub Actions enabled
![GitHub organizations and CICD workflows]

#### Around 80% of workflow permissions in repositories are insecure
The vast majority of repository workflows in GitHub have the worst default combination of permissions – allowed approval of pull requests (PRs) AND the ability to write content into the repo.

![Workflow permissions in repositories]

#### Branch protection is weak, false sense of security exists in public repos
![Percentage of repositories with branch protection enabled]

#### Self-hosted runners in cloud present a serious risk to 35% of enterprises
We find that over 35% of enterprises use at least one self-hosted runner. VMs with runners installed have on average more High and Critical vulnerabilities than all other VMs.

![Vulnerabilities numbers in VMs with self-hosted runners]

#### GitHub Actions – no limits
The most common configuration is: enable all (external and internal) actions in all the repositories in the organization.

![GitHub actions - degrees of freedom]

#### Dangerous permission scopes are prevalent in GitHub Apps
We observe the most popular scopes among the apps are metadata, pull requests and contents.

![Permission scopes presence in apps]
![Permission scope access type]

## How Wiz Can Help

Wiz connects code and cloud to protect secrets and prevent incidents. The platform approach ensures secrets in code are not just detected but contextualized and secured. Our Wiz Code offering identifies exposed secrets in repositories, while Wiz Cloud correlates them to sensitive configurations.

![Platform approach: Protect secrets in code and prevent impact in cloud]

## Conclusion

The mission of the Wiz Research team is to view the cloud from the vantage point of an attacker and leverage our observations to help the security community better combat critical risk. We should not look at VCS and CI/CD security in isolation. Attackers seek to exploit toxic combinations of risk in an effort to move laterally across interconnected systems. To stay ahead, security must ensure that issues are addressed from the codebase through to the cloud environment.

**Visit CloudVulnDB**: In February 2025 the CloudVulnDB project expanded its scope to include GitHub and GitLab, in addition to traditional cloud service providers such as AWS, GCP, and Azure.