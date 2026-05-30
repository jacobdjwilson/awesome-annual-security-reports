# The state of Secrets Sprawl on GitHub: HOW LEAKY CAN IT GIT

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

---

## Summary

GitHub is more than ever “The Place to Be” for developers when it comes to innovating, collaborating and networking.

This amazing “octoverse” gathers more than 50 million developers working on their personal and/or professional projects. So when 60 million repositories are created in a year and nearly 2 billion contributions* are added, some mistakes can happen, such as leaked secrets, Intellectual Property or PII.

Some companies may think: I don’t really care about public GitHub, we are not open sourcing our code, everything is stored on our private repositories. But what about the developers of these companies… they most likely have open source repositories and can leak secrets.

*\*State of the octoverse 2020*

---

## Secrets Sprawl

Let’s now focus on secrets. You would say that secrets stored in internal Version Control Systems is a very bad practice but in fact it is much more frequent than you would think. But why is that?

At GitGuardian, we’ve been monitoring every single commit pushed to public GitHub since July 2017. Three and a half years later… we’ve uncovered millions of secrets and sent nearly 1 million pro bono alerts to developers in 2020 alone.

API keys, database connection strings, private keys, certificates, usernames and passwords… As organizations move to cloud architectures, SaaS platforms and microservices, developers handle increasing amounts of sensitive information, more than ever before.

To add to that, companies are pushing for shorter release cycles, developers have many technologies to master, and the complexity of enforcing good security practices increases with the size of the organization, the number of repositories, the number of developer teams and their geographical spread.

As a result, secrets are spreading across organizations, particularly within the source code. This pain is so huge that it even has a name: Let us introduce you to the concept of “secrets sprawl” and how this can lead to public exposure of some of your most sensitive assets.

### SECRETS
A secret can be any sensitive data that we want to keep private. When discussing secrets in the context of software development, secrets generally refer to digital authentication credentials that grant access to services, systems and data. These are most commonly API keys, usernames and passwords, or security certificates.

Secrets are what tie together different building blocks of a single application by creating a secure connection between each component. Secrets grant access to the most sensitive systems.

Keeping secrets encrypted and tightly wrapped makes it harder for developers to both access and distribute them. This can lead developers to choose the path of least resistance when handling them which may include hardcoding them into source code, distributing them through email or messaging systems like Slack, saving them directly into config files and storing them inside internal wikis. Once secrets start to enter different systems:

- Attackers can move laterally through infrastructure
- You lose visibility over where secrets end up.

### Commit
A commit is an incremental change that has been made to an individual or set of files.
When making a commit, the difference (or diff) between the current version of files and the previous version is saved, including data that was removed.

---

## Findings

![Chart showing 2.5M public commits scanned/day, 1B public commits scanned/year, 35% more repositories created last year, and 25% more contributions to open source projects]

### WHAT DO WE FIND
- More than 5K secrets detected/day
- Over 2M secrets detected in 2020
- +20% compared to previous year

Secrets present in all these repositories can be either personal or corporate and this is where the risk lies for organizations as some of their corporate secrets are exposed publicly through their current or former developers’ personal repositories.

- 85% of the leaks occur on developers’ personal repositories.
- 15% of leaks on GitHub occur within public repositories owned by organizations.

> "We launched this audit, and several leaked secrets were brought to our attention. What was very interesting and what we didn’t anticipate was that most of the alerts came from the personal code repositories of our developers." — Anne Hardy, CISO

---

## Where leaks come from

**TOP 10**
1. India
2. Brazil
3. United States
4. Nigeria
5. France
6. Russia
7. UK
8. Canada
9. Bangladesh
10. Indonesia

---

## Why

Usually these leaks are unintentional, not malevolent. They happen because:

- Developers typically have one GitHub account that they use both for personal and professional purposes, sometimes mixing the repositories.
- It is easy to misconfigure git and push wrong data.
- It is easy to forget that the entire git history is still publicly visible even if sensitive data has since been deleted from the actual version of source code.

> "Human error exists, but the key is to be alerted and be able to take appropriate action when a leak is found." — Anne Hardy, CISO

> "Human error is nothing you can avoid and prevent, especially if it is not an error but just laziness, or even provoked, implement a risk based approach and simply add many layers to prevent it in your whole lifecycle." — David Dos Neves - Munich Re

---

## What type of secrets do we find

Secrets are digital authentication credentials that grant access to services, systems and data. The volume and diversity of these digital authentication credentials is growing fast as architectures move to the cloud but also rely on more and more components and apps.

- 27.6% Google keys
- 15.9% Development tools (Django, RapidAPI, Okta)
- 15.4% Data storage (MySQL, Mongo, Postgres…)
- 12% Other (including CRM, cryptos, identity providers, payments systems, monitoring)
- 11.1% Messaging systems (Discord, Sendgrid, Mailgun, Slack, Telegram, Twilio…)
- 8.4% Cloud provider (AWS, Azure, Google, Tencent, Alibaba…)
- 6.7% Private keys
- 1.9% Social network
- 0.8% Version Control Platform (GitHub, GitLab)
- 0.4% Collaboration tools (Asana, Atlassian, Jira, Trello, Zendesk…)

---

## File extensions that cause data breaches

**TOP 10**
- 27.9% Python
- 19.1% All others
- 18.8% JavaScript
- 9.7% Environment
- 7.5% JSON
- 4% Properties
- 3.6% PEM
- 3.2% PHP
- 2.2% XML
- 2.1% YAML
- 2% TypeScript

---

## Pro bono alerting

Such knowledge of leaked credentials comes with a great responsibility. We alert developers in a pro bono manner.

- 937,539 ALERTS WERE SENT PRO BONO
- 700,000 UNIQUE REPOSITORIES
- 860,000 UNIQUE COMMITS
- 558,085 DEVELOPERS WERE ALERTED PRO BONO

---

## What happens after a leak

- GitGuardian’s algorithm reaction to a leak is 4 seconds (Mean Time To Detect). The alert is sent right away.
- 25 minutes Median Time To React. The developer is on the front line of the issue, which allows to nullify most of the potential damage very quickly, if the developer takes immediate action after the alert.

When a secrets detection solution is in place, security teams also receive dual alerts to make sure they can follow up, remediate and report easily on security incidents.

> "If you leave your keys to your house in the lock and you notice they are gone then you change the locks." — Allan Alford

---

## Recommendations

Companies can’t avoid the risk of secrets exposure even if they put in place centralized secrets management systems. These systems are typically not deployed on the whole perimeter and are not coercitive as they do not prevent developers from hardcoding credentials stored in the vault.

**Companies need to scan not only public repositories but also private repositories to prevent lateral movements of malicious actors.**

Some best practices can be followed to limit the risk of secrets exposure or the impact of a leaked credential:
- Never store unencrypted secrets in .git repositories
- Don’t share your secrets unencrypted in messaging systems like Slack
- Store secrets safely
- Restrict API access and permissions.

Following best practices is not sufficient and companies need to secure the SDLC with automated secrets detection.

---

## To conclude

There are millions of commits per day on public GitHub, how can organizations look through the noise and focus exclusively on the information that is of direct interest to them? How can they make sure their secrets are not ending on their developers’ personal repositories on GitHub? They can’t avoid that developers have personal repositories, they need automated detection and efficient remediation tools.

In this state of secrets sprawl on GitHub analysis we focused on secrets although this is not the only sensitive information that can end up being publicly exposed: Intellectual Property, personal and medical data are also at risk. But this is for another State of Report!