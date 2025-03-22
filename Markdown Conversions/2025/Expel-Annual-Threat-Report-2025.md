# Annual Threat Report 2025

## Letter from the CEO

Expel's customer base runs the gamut, spanning organizations across almost every industry. This diversity grants our operators unique access to a wealth of data, which is crucial for staying ahead of threat actors and driving innovation.

This access also comes with serious responsibility. Namely, in protecting and maintaining the trust of our customers, but also in how we use our access and insights to share our learnings to continue fighting cybercriminals together as defenders.

As we delve into trends from 2024—ranging from cloud to phishing and everything in between—we'll share what the data told us, how to detect (and protect yourself) against similar threats, and what that might look like in the coming year. Additionally, we'll share thoughts and predictions for 2025 from our Expel experts, based on both their personal experiences and what they're seeing throughout the industry.

Regardless of your org's security maturity, there's something here for everyone. Whether you're strengthening your cloud environment, working to identify specific threats, or just exploring the data, we hope this report helps you start 2025 more informed and better equipped as we face the looming challenges ahead together.

Dave Merkel

CEO, Expel

> “ Regardless of your org's security maturity, there's something here for everyone.”

![Image description: Annual Threat Report 2025 i]

## Letter from the CSO

In an industry that's oversaturated with digital content, I want to thank you for carving out some time from your likely overbooked schedule to review our Expel Annual Threat Report. Cybersecurity isn't a slow industry, and, again, we know your spare time is limited. Your day-to-day consists of nothing but complex, nonstop problem-solving, so hopefully this report makes your day job a little bit easier.

While the data presented here is based on technology, it's colored by the experiences, challenges, and successes our analysts saw throughout 2024. This team of experts works 24x7, every day of the year to keep us and our customers safe. In this report, you'll see the threats they encountered and how they overcame them, so we can all learn together as we work towards a more secure future.

Cybersecurity is a team sport, and it's a game of inches—not yards. Slow, continuous progress is the key to creating a sustainable security strategy that scales with your business. Our goal is to translate our data into strategic guidelines you can use to better protect your business, while, in the process, sharing information and contributing to the betterment of our cybersecurity community.

Greg Notch

CSO, Expel

> “ Cybersecurity is a team sport, and it's a game of inches—not yards. Slow, continuous progress is the key to creating a sustainable security strategy that scales with your business.”

![Image description: Annual Threat Report 2025 ii]

## Table of Contents

- [Executive summary](#executive-summary)
- [2024 by the numbers](#2024-by-the-numbers)
- [Identity threats](#identity-threats)
- [Cloud platform threats](#cloud-platform-threats)
- [Computer-based threats](#computer-based-threats)
- [Phishing threats](#phishing-threats)
- [Annual spotlight](#annual-spotlight)
- [Looking ahead to 2025](#looking-ahead-to-2025)
- [2024 at Expel](#2024-at-expel)
- [Reference highlights](#reference-highlights)

![Image description: Annual Threat Report 2025 1]

## Executive summary

### Key insights and takeaways

For the last four years, we've published this report detailing the attack trends our security operations center (SOC) analysts protect against every day. This is an analysis of the incidents, email submissions, vulnerability tracking, and threat hunting leads that our team investigated from January 1 to December 31, 2024.

We break down the trends into four essential threat categories: identity, cloud infrastructure, computer-based, and phishing. We do this to keep the report easy to digest and take action on, but keep in mind these threats are often tightly related. For example, attackers using endpoint phishing to deploy malware can lead to compromised user identities, impacting an organization's cloud assets. We'll highlight this interconnectivity throughout the report. But first, let's review what we saw as the top trends in each threat category.

**OUR TOP TAKEAWAYS:**

**Identity trends continue to dominate incident investigations**

Identity-based incidents made up 68% of all incidents among Expel customers, up four percentage points from 2023. While attempting to access email accounts is the most classic form of account abuse, successful identity attacks can be used to modify payroll settings, access cloud environments, or connect new (and malicious) devices to a network. Identity-based threats are highly lucrative for attackers, and should continue to be a high priority for defense.

**Leaked and stolen credentials cause most cloud incidents**

Attackers abusing leaked or stolen secrets caused the most cloud incidents this year, continuing previous years' trends. It's easy for users to expose keys inadvertently, and these keys typically provide high levels of access to attackers, making them attractive targets.

![Image description: Annual Threat Report 2025 2]

**New malware scams drive most endpoint threats**

Infostealing malware—which is malware that targets user credentials—made up the highest number of endpoint incidents. Stolen information often ends up on the dark market, where adversaries can buy and leverage it for new attacks. If credentials don't change or accounts aren't disabled, attackers can abuse them years after the original malware execution.

A popular means to deploy malware is a tactic tricking users into executing malicious scripts on their own machines (like presenting the user with a fake CAPTCHA). This tactic has become the most frequent means of installing malware onto a device because it bypasses the need for a user to download and run a program.

**Vulnerability trends**

The newest and most severe vulnerabilities in 2024 were in firewall and VPN appliances. Firewall and VPN appliances normally gate access to an environment, but can provide a springboard for attackers when compromised. However, despite these new and powerful vulnerabilities, we also observed attackers frequently leveraging vulnerabilities from years past. Older vulnerabilities still being leveraged include Log4j (CVE-2021-44228), Oracle WebLogic remote code execution (CVE-2020-14882), and Microsoft Office Outlook privilege escalation (CVE-2023-23397).

**Credential harvesting has become the most prominent form of phishing**

Of the phishing trends our SOC saw in 2024, about 41% of malicious phishing submissions were attempts to deploy credential harvesters, and about 34% of submissions were other forms of social engineering. These rates were consistent across industries.

In addition to hearty amounts of credential harvesters and social engineering attempts, we also saw extortion attempts across several industries. This tactic typically involves a phishing email sent to a user's corporate email account, which includes pieces of personal information in an attempt to scare the targeted user into completing a desired action for the attacker. The activity appears to be a steady campaign with no signs of diminishing any time soon.

**Spotlight: Microsoft Teams setting allows malicious external messages**

A default setting in Microsoft Teams allows users to receive messages from external organizations, and attackers abused this tactic throughout 2024 to gain unauthorized network access. These attacks abuse a built-in remote access tool—Quick Assist—and leverage other commercial remote access tools to gain and keep access to target systems.

![Image description: Annual Threat Report 2025 3]

## 2024 by the numbers

### Incident types detected by Expel's SOC

This year's incident data compared to last year

-   **Identity-based incidents dominated again this year, making up 68% of all incidents in 2024—four percentage points higher than in 2023.**
    -   In the context of this report, we define identity-based attacks as attempts by cybercriminals to gain access to a user's identity to perpetuate fraud.
-   **Endpoint-based incidents accounted for 22% of threats, likely only decreasing from 2023 due to the increase in identity threats.**
    -   The highest subcategory was malware, driven up by a tactic called ClickFix, which we'll discuss in depth on page 16.
-    **Attacks specifically targeting cloud infrastructure accounted for approximately 2% of threats, which was identical to 2023. While a few actors are specializing in targeting these assets, this category doesn't have the volume of incidents that other categories have.**
    -   The highest volume of cloud infrastructure incidents are the result of leaked or stolen cloud secrets.
-   **Targeted threats account for 1% of incidents. These attacks involve a bad actor who has their eyes set on a very specific organization or goal.**

**Why measure a category that's only 1% of incidents?**

Even though targeted attacks make up a small percentage of incidents, these attacks deserve special attention in detection and response. Most incidents are opportunistic, and cast a wide net to identify any vulnerable target. With targeted attacks, they're incredibly persistent because attackers have their sights set on a specific target, and this persistence makes them a bit more dangerous.

Targeted attacks are tailored to a specific organization and may rely on open source intelligence collected about employees. Attackers are likely to make several attempts if one fails, using any learnings from failed attacks to adapt and improve. Although they make up a small number of incidents, this determination to succeed means analysts should be extra vigilant when a targeted attack is spotted.

![Image description: Annual Threat Report 2025 4]

**Chart 1: Breakdown of incidents detected by the Expel SOC in 2023 and 2024**

| Incident type        | 2023 | 2024 |
| -------------------- | ---- | ---- |
| Identity             |      |      |
| Endpoint             |      |      |
| Red team/Pentest     |      |      |
| Cloud infrastructure |      |      |
| Targeted             |      |      |
| *Percentage*          | *0*   | *20* | *40* | *60* | *80* |

### Incidents across industries

Identity compromise, most often the result of phishing, is a threat seen across all industries. While some sectors face higher volumes, no industry is immune. This is a major reason that identity incidents feature prominently in this report.

The following graph depicts the volume of incidents across the top ten industries that our customers represent. Within our customer base, we tracked the highest number of identity incidents for non-profits, retail, and legal services. But it's important to note these industries lead all others only by a small margin, as identity threats continue to dominate the threat landscape, regardless of industry, size, or security maturity.

**Chart 2: Incidents across top 10 industries**

| Industry             | Targeted | Cloud infrastructure | Red team/Pentest | Endpoint | Identity |
| -------------------- | -------- | -------------------- | ---------------- | -------- | -------- |
| Entertainment        |          |                      |                  |          |          |
| Financial services   |          |                      |                  |          |          |
| Healthcare           |          |                      |                  |          |          |
| Hospitality          |          |                      |                  |          |          |
| Legal services       |          |                      |                  |          |          |
| Manufacturing        |          |                      |                  |          |          |
| Non-profit           |          |                      |                  |          |          |
| Retail               |          |                      |                  |          |          |
| Technology           |          |                      |                  |          |          |
| Travel               |          |                      |                  |          |          |
|                      |          |                      |                  |          |          |
| *Percentage*         | *0*      | *25*                 | *50*             | *75*     | *100*    |

![Image description: Annual Threat Report 2025 5]

### Initial alert sources in 2023 and 2024

Cloud resources managing identity, data, and infrastructure provided the highest number of leads to identify malicious activity, with identity being the foremost. This is consistent with identity being the most common entry point for cyber attacks, and it trended the same in both 2023 and 2024.

Endpoint detection and response (EDR) systems continued to be the primary source of monitoring and means of finding threats within networks in 2024. EDR systems identified 25% of all incidents, while SIEM and network monitoring systems provided alert leads for 3% and 1%, respectively.

**Chart 3: Initial alert sources identifying incidents**

| Incident type          | 2023 | 2024 |
| --------------------- | ---- | ---- |
| Cloud                 |      |      |
| EDR                   |      |      |
| Phishing submissions  |      |      |
| SIEM                  |      |      |
| Network               |      |      |
| *Percentage*          | *0*   | *25* | *50* | *75* |

![Image description: Annual Threat Report 2025 6]

## Identity threats

### Stealing and abusing credentials

Year-over-year, identity-based attacks continue to be the most common attack type we see across our customer base, with increasing volume. Barring major changes in cybercrime, we expect this trend to continue into 2025. Threat actors will continue to innovate, finding new ways to iterate on tried-and-true methods to steal and abuse credentials.

**How are credentials stolen?**

This year, we observed three primary contributors to the theft and abuse of credentials: phishing-as-a-service (PhaaS) platforms, traditional phishing, and infostealing malware. PhaaS platforms are a fairly recent innovation to phishing that arose out of attackers' needs to bypass multi-factor authentication (MFA). Unlike traditional phishing, PhaaS platforms create attachments and emails, and maintain infrastructure on behalf of attackers. Despite this convenience, PhaaS platforms haven't fully replaced traditional phishing—yet.

Unlike credential harvesters, which target one type of login, infostealing malware targets a wide array of sensitive data on a computer, whether it's stored by the browser or in files. Infostealing malware has been around for decades, but has become a much more common threat in the last few years. The computer-based threats section of this report delves into infostealing malware, but for now, let's focus on the rising popularity of PhaaS platforms as an identity threat.

**PhaaS platforms**

PhaaS platforms provide an aspiring criminal with an easy introduction into cybercrime. Just like platform-as-a-service (PaaS) software products used by legitimate businesses, PhaaS offers access to a service without requiring the buyer to set up their own infrastructure. These platforms offer many of the necessary components for running a phishing campaign, such as templates, infrastructure, and victim tracking. The buyer is only responsible for providing a target list and then acting on any stolen credentials.

PhaaS platforms work by creating a webpage that can proxy information to and from the legitimate login domain. This type of proxying is classified as an adversary-in-the-middle (AiTM) tactic, since it allows an attacker to intercept traffic.

Since the webpage is proxying traffic, it's often configured to load the same graphics as the legitimate login page. If the target organization has a specific background or logo, the malicious page will also use this information to make it look legitimate. The fake page then submits any information supplied by the user and returns any results provided by the real login

![Image description: Annual Threat Report 2025 7]

page. So if the real login page requests an MFA token or a one-time pass (OTP), the fake one will request this information too. The proxying page intercepts session cookies, which can then be used by an attacker to access the account and bypass MFA. We most frequently see this attempt to access the account occur from a hosting provider.

Over 2024, we've continued to see a growth in the use of PhaaS platforms by observing login attempts from hosting providers. This trend in authentication sources is detailed in the graph below.

Attackers can change user agents for malicious logins easily, but they often don't. Identifying and triggering alerts with suspicious user agents is a valuable way to identify many malicious logins.

Based on our tracking and analysis of the data, logins from hosting providers were consistently the result of users interacting with phishing distributed from a PhaaS platform. The logins often exhibit signs of automation, such as user agents that are part of automation systems. Examples include axios and node-fetch. This combination of automation and hosting infrastructure is a high-confidence indicator of malicious activity.

**Understanding the data**

As an authentication source, hosting is defined as infrastructure offered from a data center. This may consist of physical or virtual private servers consumers can spin up.

The VPN category tracks malicious logins identified from sources associated with consumer VPN providers and logins using The Onion Router (TOR).

Geolocation tracks instances where a login was flagged as a suspicious location—either from miles away, or on the other side of the planet.

The anomaly category is used for tracking malicious logins that were eerily close to the user's expected geolocation. These logins may have been identified as malicious for reasons other than geolocation, but the login source often suggests an attacker is using a proxy.

**Chart 4: Authentication sources over time**

|               | Q1-2024 | Q2-2024 | Q3-2024 | Q4-2024 |
| ------------- | ------- | ------- | ------- | ------- |
| Other         |         |         |         |         |
| Hosting       |         |         |         |         |
| VPN           |         |         |         |         |
| Geolocation   |         |         |         |         |
| Anomaly       |         |         |         |         |
| *Percentage* | *0*     | *20*    | *40*    | *60*    |

*Calendar quarter*

![Image description: Annual Threat Report 2025 8]

**How are stolen credentials leveraged?**

For credentials to be leveraged, they first must be stolen. The graph below represents incidents where credentials have been successfully compromised. In most identity incidents we observed this year (56%), the bad actor was blocked from accessing the account via customer security controls after the credentials were compromised. The other 44% of the time, attackers most often used stolen credentials to access email accounts and single-sign-on (SSO) applications.

It's important to note that even though credentials were compromised 56% of the time but not leveraged for additional actions like identity portal compromise (IdP) or business email compromise (BEC), that doesn't mean it isn't a security concern. Credentials should always be updated when compromised, regardless of whether an attacker's first attempt to apply them was successful or not, because they will try again.

**Understanding the data**

At Expel, we track three main types of identity incidents:

BEC: This is an unauthorized party authenticated to an active email account. When this happens, abuse of the account is a matter of when—not if—and requires action from automation or security teams to kill sessions and investigate activity.

IdP compromise: This is when an unauthorized party authenticates to an identity portal, where they can then access SSO applications.

Credential compromise: This occurs when an unauthorized party attempts account access and is denied. This indicates an attacker successfully intercepted a user's credentials, but access was restricted (likely due to access policies). In future attempts, this could be circumvented with retries using VPNs or proxies. Credential compromise introduces additional risk because one blocked login attempt doesn't mean the attacker won't try to access other services with the same password.

**Chart 5: Type of identity compromise tracked in 2024**

|                            |      |
| -------------------------- | ---- |
| Credential compromise      |      |
| BEC                        |      |
| IdP compromise             |      |
| *Percentage of incidents* |      |

![Image description: Annual Threat Report 2025 9]

**Protecting your organization from PhaaS platforms**

PhaaS platforms make session token theft easier for adversaries, so it's important organizations reset passwords and terminate sessions for compromised users immediately after a successful attack. Otherwise, the attacker can (and will) continue to access the account for as long as the session is valid.

For any accounts accessed by an attacker, it's important for security teams to investigate and identify any newly added MFA devices. In many situations, attackers will attempt to add MFA devices to maintain an account connection even after the session has ended.

It's also important to create detections for each stage of an attack to ensure an attack is detected even if another control fails. Examples include:

-   **Triggering alerts for newly added MFA devices**
    -   Give special attention to MFA devices added after passwords resets, and MFA devices added while connected to a proxy or VPN.
-   **Triggering alerts for the creation of new inbox rules**
    -   Attackers commonly use simple names for inbox rules. Many attacker-created rules can be caught by looking for rules consisting of two to three characters or only containing a single repeating character.
    -   Monitor for rules created containing keywords like "payroll", "malware", or "virus". Rules with these keywords often indicate malicious activity.
-   **Advising employees to know their payroll information and report any abnormal or suspicious activity to the security team. Changes resulting in unexplained variances in paychecks are evidence of an identity compromise.**
    -   Some HR management systems allow administrators to require approval for sensitive information updates (such as direct deposit details). Consider implementing this type of control for your own organization.

**Creative uses of credentials**

In last year's Annual Threat Report, we reported the highest volume of targeted attacks among our customers were the result of the hacking group known as The Com, a group including actors such as Scattered Spider. This year, that trend continued. During 2024, some individual arrests were made within the group, but we anticipate these tactics will continue into 2025.

Actors within this group share a primary tactic. Specializing in SMS message abuse, they perform SIM swaps, assigning a victim's phone number to a device they control to target a user's identity. This allows attackers to receive SMS messages intended for the recipient. In this case, these are SMS messages allowing the user to complete authentication for an account. The attacker uses credential harvesting or self-service password resets to bypass their need for the user's password.

A subgroup known as Atlas Lion (and as Storm-0539) conducted one of the incidents we observed this year. In an attempt to gain access to a target network, the threat actor created a virtual machine within Azure. During the installation of Windows 10, the threat actor used stolen credentials to register the device to the target domain. This registration behaved as a newly enrolled device, and connected with the AzureID to install designated software for corporate devices. Expel's SOC detected this activity because the automation downloaded the corporate EDR agent and triggered an alert due to the user's abnormal location.

![Image description: Annual Threat Report 2025 10]

**Service credentials**

A high-profile news story in 2024 also highlighted a creative use of credentials. A large number of Snowflake data stores were compromised, and during the investigation, analysts discovered the attacker purposefully purchased credentials specific to Snowflake data lake instances. Additionally, the attacker developed a custom tool targeting this specific platform.

The main reason this incident was possible was because Snowflake didn't require MFA for accounts at the time. As a result, accounts that weren't secured with MFA were easy targets for the attacker, who specifically sought out the Snowflake data lake credentials.

The credentials purchased had been stolen by infostealing malware and were sold on the dark market. As we've discussed on our blog, the purchase of credentials to steal data isn't limited to any particular platform (like Snowflake). When exposed credentials are sold to attackers, this type of incident can happen on other platforms, too.

**Ransomware gangs love stolen credentials**

We noted this trend in 2023, have seen it continue through 2024, and expect it to continue in 2025. Ransomware gangs are also keen on using stolen credentials to gain network access, and will often collaborate with other criminals who sell credentials or access to infected computers.

In tracking tactics from multiple ransomware gangs, we've observed several gangs buy credentials and leverage them against corporate VPN accounts. If they're not protected with MFA, these purchased credentials give an attacker easy access to corporate systems.

![Image description: Annual Threat Report 2025 11]

## Cloud platform threats

### Increased cloud adoption leads to increased cloud threats

**Cloud infrastructure incidents in 2024**

Cloud infrastructure attacks target assets hosted on cloud platforms such as Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Kubernetes. The techniques and frequency of these attacks continue to evolve, reflecting the growing adoption of cloud environments and the expanding attack surface that comes with them.

Expel defines cloud infrastructure activity as an incident where an attacker can gain access to the control plane or data plane of a cloud platform. In 2024, 86% of our cloud infrastructure incidents impacted assets in AWS, while only 9% impacted assets in Google Cloud and Azure.

Just like previous years, credential compromise continued to be the top cause of cloud infrastructure incidents in 2024. Stolen or leaked cloud credentials (also known as secrets) provide attackers with access to the cloud control plane through an attack framework or a command line utility. These secrets can be exposed through accidental uploads to repositories, vulnerability exploitation, or infostealing malware.

**Chart 6: Cloud infrastructure incident types in 2024**

| Incident type          |      |
| ---------------------- | ---- |
| Credential compromise  |      |
| Server-side exploitation |      |
| SSRF                   |      |
| Misconfiguration      |      |
| Other                  |      |
| *Percentage*           | *0*  | *10* | *20* | *30* | *40* | *50* |

![Image description: Annual Threat Report 2025 12]

The second leading cause of cloud incidents in 2024 was server-side exploitation. In these incidents, an attacker identified and exploited a vulnerability in a web application to deploy a web shell or malware. While we couldn't identify a leading cause for these types of incidents (due to a lack of successful compromise), we do know the most common payload deployed was cryptomining malware.

The third-highest cause of incidents were server-side request forgeries (SSRF), where an attacker tricks a public-facing web application into exposing sensitive information. Specifically, it tricks an Amazon Elastic Compute Cloud (Amazon EC2) instance into exposing secrets by requesting information from the instance's own metadata. To protect against this type of attack, it's important to review the security of the application in the instance you're using. Ensure the instance is using AWS's Instance Metadata Service version 2 (IMDSv2). AWS originally released IMDSv1 to mitigate the issue, but version 2 should be used instead to best protect sensitive information.

**From identity to infrastructure: Scattered Spider targets compromised AWS accounts**

Scattered Spider has adapted its tactics to include data theft from cloud storage objects. Some individuals in the group have also shifted their primary goal to exfiltration-based extortion.

During a 2024 phishing/smishing campaign, Expel confirmed Scattered Spider actors accessed multiple applications via compromised user accounts while using Okta SSO. One compromised account was then used to authenticate access to the organization's AWS console and assume an engineering role. The attacker attempted AWS discovery before being locked out of the account.

A key portion of Scattered Spider's campaigns involve gathering intelligence and data. Had the attackers been more successful in their attempts to understand the organization's environment configuration for the next stages of their attack, they may have been able to successfully iterate through AWS resources to locate the most valuable data for their attack or extortion.

**Protecting your organization from cloud infrastructure threats**

Just like with other technologies, it's important to ensure your cloud infrastructure is monitored with a defense-in-depth strategy. That is, build your detections to spot suspicious activity at multiple stages of the attack lifecycle.

Secrets are most often exposed accidentally. We recommend using secret scanning to prevent key exposure. This process can identify accidentally exposed access keys in code repositories during development, or after publishing. Secret scanning can also be performed through paid services, or can be configured with open source tools. These can identify hundreds of secret types from a wide range of sources to keep you secure.

For AWS specifically, you can create detections around long-term and short-term access keys (beginning with AKIA and ASIA, respectively) to detect early stages of unauthorized access to your environment.

![Image description: Annual Threat Report 2025 13]

## Computer-based threats

### Trending malware and popular vulnerabilities

In the neverending game of cat-and-mouse, both attackers and defenders study each other to understand what tactics might outwit their opponent. Just like defenders, successful cybercriminals learn from one another and adopt effective techniques. Throughout the year, we monitor those trending techniques to improve our detection capabilities. We're sharing our observations here to alert others to trends in malware and vulnerabilities.

**Malware trends**

Malware is any software that's used to harm networks, computers, or users. This includes custom and off-the-shelf software repurposed for cyberattacks. As defenders, we're responsible for defending against both types of malware.

At Expel, we break malware into two major categories based on risk: high-risk malware and latent-risk malware. High-risk malware can take off fast and cause a lot of damage. This category includes remote access tools (RATs), initial access tools (IATs), and USB initial access tools. Latent-risk malware is all about the long game: the cybercriminals deploying malware aren't acting immediately on their objectives. This category includes infostealers, cryptocurrency miners, and banking trojans.

**Commonly observed malware types**

- IATs: Also called loaders or droppers, IATs attempt to circumvent defenses to get onto a system, so they can download or load additional malware.
- RATs: Aptly named, RATs enable remote access to computers. RATs can include abuse of legitimate commercial tools like remote management and monitoring (RMM) tools or custom attacker-built tools.
- USB initial access tools: This is malware that runs from infected USB drives. When the infected drive is plugged into a computer, the malware attempts to connect to pull down additional tools to give bad actors access to the device.
- Infostealers: Infostealers are malware that access sensitive data on a device and then send it to an attacker. They most frequently target passwords stored in the browser, cryptocurrency wallets, or files stored in common places.
- Cryptocurrency miner: This is malware that uses the resources of a computer or server to generate cryptocurrency on behalf of the attacker.
- Banking trojan: This type of malware steals or intercepts financial information as the victim is using this information.

![Image description: Annual Threat Report 2025 14]

The following graph compares the prevalence of these subcategories in 2024 and compares them to our data from the prior year. The biggest difference between the years was a shift in prevalence from IATs to infostealers.

**Chart 7: Malware type prevalence 2024 vs. 2023**

| Malware type             | 2023 | 2024 |
| ------------------------ | ---- | ---- |
| Infostealer              |      |      |
| RAT                      |      |      |
| IAT                      |      |      |
| Cryptocurrency miner     |      |      |
| USB initial access tool  |      |      |
| Banking trojan           |      |      |
| *Percentage*             | *0*  | *10* | *20* | *30* | *40* | *50* |

The following graph depicts the change in malware types over the last two years.

**Chart 8: 2023 and 2024 malware types**

|                   | Q1-2023 | Q2-2023 | Q3-2023 | Q4-2023 | Q1-2024 | Q2-2024 | Q3-2024 | Q4-2024 |
| ----------------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- | ------- |
| Banking trojan    |         |         |         |         |         |         |         |         |
| Infostealer       |         |         |         |         |         |         |         |         |
| IAT               |         |         |         |         |         |         |         |         |
| Cryptocurrency    |         |         |         |         |         |         |         |         |
| RAT               |         |         |         |         |         |         |         |         |
| USB initial       |         |         |         |         |         |         |         |         |
| *Percentage*      | *0*     | *25*    | *50*    | *75*    | *100*   |         |         |         |

*Calendar quarter*

As depicted in the graph above, the largest volume of malware in the first quarter of 2023 were IATs. These were largely attributed to the Qakbot botnet and Gootloader malware. Qakbot was virtually eliminated as a threat after the 2023 takedown of the botnet[^1]. Additionally, Gootloader's activity also significantly decreased in the second half of 2023, and declined even further in the second half of 2024. This decline largely seems to be the result of threat actors changing tactics from SEO poisoning to using PDF-to-doc converter websites[^2]. These changes resulted in RATs and infostealers taking a larger share of observed malware activity in 2024.

**Understanding the data**

Of all the malware incidents we investigated in 2023 and 2024, Chart 8 highlights the frequency of each malware type throughout the year.

The graph is always at 100%, representing all the malware types we saw in each quarter from 2023–2024, with the quarters as follows:

-   Q1: January–March
-   Q2: April–June
-   Q3: July–September
-   Q4: October–December

Q1 of 2023, for example, would be read as about 50% of malware occurring during that time were IATs. About 20% were infostealers, and no banking trojan malware was encountered. However, by Q4 of 2024, IATs were only about 10% of the malware encountered, and infostealer malware was over 50% of the malware encountered by our SOC.

It's important to note that percentages on the y axis represent the portion of 100%, and not all start at zero. It requires a little bit of mental math to determine exact percentages, but provides a helpful visual guide to malware trends.

![Image description: Annual Threat Report 2025 15]

**PDF-to-doc converter websites**

It's critical to make sure your employees have the tools they need to do their job, including authorized PDF editing tools. With Gootloader, a victim uploads (sometimes sensitive) documents to convert the files from PDFs to Microsoft documents (.doc), but instead installs malware that can lead to ransomware if unmitigated.

Our SOC also observed a massive increase in infostealers beginning in the third quarter of 2024. This was driven by the decrease in the Qakbot and Gootloader malware, and the rise of the ClickFix tactic.

**Development and growth of the ClickFix tactic**

With the decline of Qakbot and Gootloader malware, the most consistent IAT threat is SocGholish malware. The criminal group maintaining the malware consistently relies on infected websites to deliver it, and many other aspiring cybercrime groups are looking to follow in their digital footsteps.

In this approach, the infected website displays a message instructing the user to download and run malware disguised as a browser update. If the user attempts to download the fake update, they'll receive a JavaScript file which, when executed, loads malware onto their system. The actor running this malware often hands off infected computers to ransomware gangs.

![Image description: Example of SocGholish phishing designed to execute JavaScript and deploy IAT malware]

![Image description: Annual Threat Report 2025 16]

In 2023, multiple threat actors hopped on the "fake update pop-up" bandwagon to trick users into downloading malicious files.