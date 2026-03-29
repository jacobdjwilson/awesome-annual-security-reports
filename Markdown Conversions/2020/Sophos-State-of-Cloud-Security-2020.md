# THE STATE OF CLOUD SECURITY 2020

A Sophos whitepaper July 2020

## Table of Contents
- [Introduction](#introduction)
- [About the survey](#about-the-survey)
- [Executive summary](#executive-summary)
- [Part 1: The prevalence of cloud attacks](#part-1-the-prevalence-of-cloud-attacks)
- [Part 2: How criminals are getting in](#part-2-how-criminals-are-getting-in)
- [Part 3: Organizations are not focusing on root causes](#part-3-organizations-are-not-focusing-on-root-causes)
- [Recommendations](#recommendations)
- [Secure the cloud with Sophos](#secure-the-cloud-with-sophos)

---

## Introduction
Thanks to growing demand for remote working and public cloud services, on-premises infrastructure is shifting from asset to liability. But moving to the cloud comes at a cost: increasing every organization’s attack surface. The numerous and well-publicized breaches of data storage services have raised cloud security awareness, but cybercriminals work diligently to stay one step ahead.

To understand the reality behind the headlines, Sophos commissioned an independent survey of 3,251 IT managers across 26 countries who are using the public cloud. The findings provide brand new insights into the concerns for security teams that host data and workloads in the public cloud; how attackers are changing the rules to find new ways into environments; and how to find the visibility you need – and perhaps the security gaps you never knew you had.

## About the survey
Sophos commissioned research specialist Vanson Bourne to survey 3,521 IT managers currently hosting data and workloads in the public cloud about their experiences with cloud security. By public cloud we mean organizations using at least one of the following providers: Azure, Oracle Cloud, AWS, VMWare Cloud on AWS, and Alibaba Cloud. In addition, they may also have used Google Cloud and IBM Cloud. Sophos had no role in the selection of respondents and all responses were provided anonymously. The survey was conducted during January and February 2020.

48% of survey respondents using the public cloud were from small organizations (100-1000 employees), and 52% were from larger organizations (1001-5000 employees).

![Table of respondents by country]
![Table of respondents by sector]

## Executive summary
The survey provides fresh new insights into the experiences of organizations hit by cybercriminals in the public cloud, including:

- **Almost three-quarters of organizations hosting data or workloads in the public cloud experienced a security incident in the last year.** Seventy percent of organizations reported they were hit by malware, ransomware, data theft, account compromise attempts, or cryptojacking in the last year.
- **Data loss/leakage is the number one concern for organizations.** Data loss and leakage topped our list as the biggest security concern, with 44% of organizations seeing data loss as one of their top three focus areas.
- **Ninety-six percent of organizations are concerned about their current level of cloud security.** Data loss, detection and response, and multi-cloud management top the list of the biggest concerns among organizations.
- **Multi-cloud organizations reported more security incidents in the last 12 months.** Seventy-three percent of the organizations surveyed were using two or more public cloud providers and reported more security incidents as those using a single platform.
- **European organizations may have the General Data Protection Regulation (GDPR) to thank for the lowest attack rates of all regions.** The GDPR guidelines’ focus on data protection, and well-publicized ransomware attacks have likely led to these lucrative targets becoming harder for cybercriminals to compromise in Europe.
- **Only one in four organizations see lack of staff expertise as a top concern despite the number of cyberattacks reported in the survey.** When it comes to hardening security postures in the cloud, the skills needed to create good designs, develop clear use cases, and leverage third-party services for platform tools are crucial but underappreciated.
- **Two-thirds of organizations leave back doors open to attackers.** Accidental exposure through misconfigurations continues to plague organizations. Security gaps in misconfigurations were exploited in 66% of attacks (either through attackers exploiting a flaw in the web application firewall to access account credentials or attackers taking advantage of a misconfigured resource), while 33% of attacks used stolen credentials to get into cloud provider accounts.

## Part 1: The prevalence of cloud attacks
### Seven in 10 organizations have been hit by a cyberattack
Seventy percent of respondents said they had suffered a public cloud security breach in the last year. This is extremely worrisome for organizations, with 96% of the 3,521 respondents expressing concern about their current level of security across the six major public cloud platforms listed, including Amazon Web Services, Microsoft Azure, and Google Cloud Platform.

![Chart: 70% of organizations suffered a public cloud security breach in the last year; 96% of organizations are concerned about their current level of cloud security]

### As you move, so does the target
Among organizations suffering a cyberattack in the cloud, the breakdown of attack types reads like the usual suspects: 50% of organizations were hit by malware of some form, including ransomware (respondents could select multiple options).

![Chart: Organizations suffering security incidents in the last year (Malware, Exposed Data, Ransomware, Account Compromise, Cryptojacking)]

### Attack levels vary across the globe
Looking at the number of public cloud attacks across the globe reveals interesting variations. This is likely due to criminals focusing their efforts where they see the greatest opportunity for return.

![Chart: Organizations suffering public cloud security incidents in the last year by country]

- **India (227 respondents)** tops the list with 93% of organizations reporting being hit by a cyberattack in the last year.
- **APAC region** shows the highest regional rates of exposed data (35%), ransomware attacks (37%), and account compromise (33%).
- **Europe (1259 respondents)** suffered the lowest percentage of security incident rates of all respondents in the last year.
- **Middle East and Africa (360 respondents)** shows cryptojacking at its highest among all regions (22%).
- **United States (413 respondents)** was in the bottom 35% of countries suffering security incidents in the last year.

![Charts: Organizations hit by malware, ransomware, exposed data, stolen credentials, and cryptojacking by country]

## Part 2: How criminals are getting in
### Two-thirds of organizations leave back doors open to criminals
When it comes to the cloud, it’s best to think of a network like a building with multiple windows and multiple openings – they all add up to multiple potential access points for someone, or something, to get in and out.

![Chart: How did the attacker get into your organization’s environment? (Breached through security misconfiguration, Stolen credentials, Misconfigured WAF)]

### Entry methods vary across the globe
An organization’s security posture is often the deciding factor when it comes to choosing entry methods and weak points.

![Chart: How organizations were compromised by country]

### Identity security represents a huge challenge
A review of cloud accounts by the Sophos Cloud Optix cloud security posture management service discovered worrying trends in organizations’ security posture as it relates to cloud account access.

- **91%** had overprivileged Identity and Access Management roles.
- **98%** had MFA disabled on their cloud provider accounts.

## Part 3: Organizations are not focusing on root causes
### The most worrying outcome for organizations is data loss
Data security topped the list as the most likely concern, cited by 44% of respondents.

![Chart: Top cloud security concerns among organizations]

### A significant root cause is a lack of cloud expertise
While 70% of organizations in our survey suffered a security breach in the last year, only a quarter see lack of staff expertise as a top concern.

### The impact of configurations on data security
A review of cloud accounts by the Sophos Public Cloud Security team discovered that accidental data exposure through misconfigured storage services continues to plague organizations.

![Chart: Percentage of organizations with unencrypted storage/databases and public access enabled]

### Most successful ransomware attacks now hit the public cloud
In parallel to this cloud security survey, Sophos recently released a survey of 5,000 IT managers that explored their experiences with ransomware. Among those organizations, 59% of attacks where the data was encrypted involved data in the public cloud.

![Chart: Did the cybercriminals succeed in encrypting your organization’s data in the most significant ransomware attack?]

### Multi-cloud creates multiple challenges
Seventy-three percent of the organizations surveyed were using two or more public cloud providers and reported up to twice as many security incidents as those using one cloud platform.

![Chart: Single and multi-cloud organizations hit by cyberattacks in the last year]

## Recommendations
1. **Start with the assumption that attackers will find cloud assets.**
2. **Invest in cloud workload protection with anti-malware technology.**
3. **Protect data wherever it’s held.**
4. **Continually monitor cloud resource configurations.**
5. **Proactively manage cloud access.**
6. **Provide secure remote access for workers.**
7. **Deploy a layered defense.**
8. **Learn responsibilities for securing public cloud provider services.**

## Secure the cloud with Sophos
Protection from the latest generation of public cloud cyberattacks requires a new level of visibility and security automation. Sophos gives you the advanced protection technologies you need to disrupt the entire attack chain.

![Diagram: Sophos Cloud Security ecosystem components]

- **Sophos Cloud Optix**: Extends detection and response in the public cloud.
- **Sophos Intercept X for Server with EDR**: Secures cloud, on-premises, or hybrid workload environments.
- **Sophos XG Firewall**: Protects the network edge with the ultimate all-in-one firewall solution.

Start an instant demo at [www.sophos.com/demo](http://www.sophos.com/demo)

---
© Copyright 2020. Sophos Ltd. All rights reserved.
Registered in England and Wales No. 2096520, The Pentagon, Abingdon Science Park, Abingdon, OX14 3YP, UK