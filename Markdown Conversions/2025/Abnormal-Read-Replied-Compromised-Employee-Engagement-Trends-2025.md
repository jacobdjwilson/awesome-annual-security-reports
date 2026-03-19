# THREAT REPORT: Read, Replied, Compromised: Data Reveals 44% Engagement Rate with VEC Attacks

## Table of Contents
- [Executive Summary](#executive-summary)
- [Inside the Threat: Why VEC Works](#inside-the-threat-why-vec-works)
- [VEC Risks Increase with Organization Size](#vec-risks-increase-with-organization-size)
- [Sector by Sector: Where VEC Drives the Highest Engagement](#sector-by-sector-where-vec-drives-the-highest-engagement)
- [Role-Related Risk: Job Functions and VEC Engagement](#role-related-risk-job-functions-and-vec-engagement)
- [Across Borders: VEC and BEC Trends by Region](#across-borders-vec-and-bec-trends-by-region)
- [The Reporting Deficit in Email Security](#the-reporting-deficit-in-email-security)
- [Thread Hijacked: Inside a Vendor Impersonation Attack](#thread-hijacked-inside-a-vendor-impersonation-attack)
- [Why Behavioral AI Is the Best Defense Against Human-Centric Threats](#why-behavioral-ai-is-the-best-defense-against-human-centric-threats)
- [About Abnormal AI](#about-abnormal-ai)

---

## Executive Summary

Your workforce is your greatest asset, and your vendors are integral to the success of the enterprise. It’s no surprise, then, that cybercriminals are targeting both, exploiting the trust in these partnerships to deceive, defraud, and divert funds.

Much like traditional business email compromise (BEC), vendor email compromise (VEC) involves the misuse of a familiar identity. In these attacks, however, the person being impersonated is an external third party rather than an internal employee. Posing as trusted partners, threat actors attempt to trick targets into paying fake invoices, initiating fraudulent wire transfers, or updating banking details to reroute funds into attacker-controlled accounts.

![Infographic showing 44.2% overall employee engagement rate, $300M in attempted vendor fraud, and 98.5% of text-based advanced attacks failing to be reported.]

### Behavioral Data Reveals Alarming VEC Engagement Rates

From March 2024 to March 2025, we monitored the email environments of more than 1,400 organizations of various sizes across multiple industries. These companies had implemented Abnormal in passive, read-only mode, which means the platform was integrated with the organization’s mail client but not actively blocking attacks.

This allowed us to observe unfiltered employee behavior and analyze engagement with text-based advanced email attacks—e.g., business email compromise, vendor email compromise, reconnaissance, and extortion. To enable cross-organizational comparison, we standardized the data by using only attacks that were read, eliminating volume as a variable and allowing conclusions to be drawn based on user behavior rather than incident frequency.

Our findings were eye-opening. The data revealed that employees frequently struggle to differentiate between legitimate messages and attacks, especially when those emails appear to come from a known vendor. VEC attacks consistently drove either the highest or second-highest rates of replies and forwards, irrespective of organization size, industry, or geographic location. Over the course of the observation period, attackers also attempted to steal more than $300 million through VEC, emphasizing the significant financial risk these threats pose.

This report exposes the behavioral blind spots attackers are exploiting and underscores the urgency of reducing exposure to malicious content.

---

## Inside the Threat: Why VEC Works

All text-based advanced email attacks are insidious and deceptive, but there are a few aspects of vendor email compromise that make it especially difficult to detect. First is the inherent financial nature of the vendor-customer dynamic and the fact that billing and payments are routinely discussed via email. Consequently, malicious messages seemingly from vendors requesting changes to banking information or large fund transfers may not be immediately flagged as suspicious.

Further, the scale of some supply chains makes it nearly impossible for employees to be well-versed in every vendor’s operations. Therefore, they simply don’t have the context to recognize when a request is out of the ordinary. Even when the target is knowledgeable about the standard processes and which parties are usually involved, there is no guarantee that they will discern that something is amiss.

Cybercriminals who engage in VEC will monitor ongoing correspondence, learn typical patterns and behaviors, and patiently wait until the ideal time to strike. Often, they will download older invoices or statements and alter only the bank account information, leaving the modified documents essentially indistinguishable from the originals.

Threat actors will also use spoofed sender addresses or look-alike domains to increase the appearance of authenticity. Some even leverage actual compromised vendor accounts, frequently hijacking existing email threads to carry out the attack. The emails, originating from a legitimate account with no history of suspicious behavior, bypass signature-based security tools and land in the inboxes of employees who have no reason to believe the message is malicious.

### The Role of AI in Amplifying Vendor Email Compromise

VEC occurs at a lower rate than other threats, like phishing, for several reasons. Chief among them is that attackers tend to choose the path of least resistance, and vendor email compromise, though lucrative, is a high-effort attack type. That being said, with the added capabilities of weaponized AI, even low-skill cybercriminals are increasingly able to execute these sophisticated, socially engineered attacks.

With AI-powered tools, attackers can generate remarkably believable messages that mirror real vendor communications, complete with realistic language, formatting, and urgency cues. In a tight job market, with economic uncertainty and persistent layoff concerns, employees may rush to resolve an apparent oversight—like a missing payment—without verifying the request.

AI further amplifies this risk by helping bad actors make fraudulent invoices and follow-up messages more persuasive, increasing the likelihood of success.

---

## VEC Risks Increase with Organization Size

Employees in the largest organizations—i.e., those with a workforce of 50,000 or more—had the highest rate of second-step engagement[^1] with vendor email compromise. After reading a VEC message, they took additional action 72.3% of the time.

![Chart showing VEC engagement by organization size, with engagement rates rising as the number of mailboxes increases.]

Another way to think about these percentages is this: if employees at a company read 10 VEC attacks, at least two and up to seven of those messages will be replied to or forwarded.

The natural, and understandable, assumption here is to make a connection between VEC volume and engagement rate. While the probability of receiving a VEC attack does typically increase with the number of mailboxes, the baseline attack rate is a non-issue here.

In order to facilitate an accurate comparison, our analysis focuses only on the percentage of vendor email compromise attacks that are read, making gross volume irrelevant. The true variables are instead the number of employees and the number of vendors. Every partner represents another entity that can be impersonated or an account that can be compromised, and every member of the workforce represents a potential target—a human that is far from infallible.

Interestingly, enterprises with more than 50,000 employees actually had the lowest read rate of any organization size band, showing that the threat doesn’t stem from volume alone, but from how employees behave after opening the email.

Across the board, VEC engagement rates are already worrisomely high. But what makes the issue even worse is the fact that 7.3% of these instances of second-step engagement were initiated by individuals who had previously replied to and/or forwarded a different VEC attack.

While it is impossible to know why this is, there are a few reasons why an employee might become a “repeat engager.” Perhaps they didn’t receive sufficient training after the first incident. Employers should not assume that once an employee has experienced the negative consequences of falling victim to an attack, no additional coaching is needed to avoid repeating the error. There’s also the possibility that after being deceived once, an employee may adopt the attitude that “lightning never strikes the same place twice.” Rather than becoming more vigilant, they erroneously believe they won’t be targeted again.

[^1]: Second-step engagement refers to an action taken after reading a message—e.g., replying, forwarding, or both. Forwards do not include messages sent to phishing mailboxes.

---

## Sector by Sector: Where VEC Drives the Highest Engagement

Industry type emerged as a critical factor in VEC susceptibility, with engagement rates varying dramatically based on operational characteristics.

![Chart showing VEC engagement by industry, with Telecommunications at 71.30% and Media & Entertainment at 28.23%.]

At 71.3%, the second-step engagement rate for the telecommunications industry is by far the highest of any vertical, dwarfing the 56% observed in energy/utilities providers, which ranked second.

Telecommunications organizations depend on complex networks of vendors, resellers, infrastructure providers, and technology partners to deliver services. They also have large, geographically distributed teams, including field technicians, regional offices, and 24/7 operations centers. This creates an environment where email serves as a critical coordination channel between internal teams and external partners.

In an industry where disruptions and delays can have wide-ranging impacts, employees may feel compelled to act quickly when a message appears related to service interruptions or contract issues. The pressure to maintain uptime—reinforced by SLAs and internal expectations regarding responsiveness—can result in employees bypassing verification processes in favor of speed.

Energy/utilities and hospitality round out the top three industries for second-step engagement. Though the services they provide differ significantly, organizations in these verticals do share certain characteristics that prime employees to act on messages seemingly from external vendors with minimal scrutiny.

Both operate in high-pressure, service-driven environments with dispersed, often round-the-clock workforces that rely extensively on email for communication. Further, energy and utilities employees face intense pressure to protect critical infrastructure, while hospitality staff are trained to prioritize rapid responses to maintain positive guest experiences.

---

## Role-Related Risk: Job Functions and VEC Engagement

One notable trend was the clear correlation between an employee’s organizational role and their likelihood of engaging with vendor email compromise attacks.

![Chart showing VEC engagement by job category, with Sales (Entry-Level) at 85.71% and HR (Entry- & Mid-Level) at 0%.]

Sales-focused roles are heavily represented among the job categories with the highest second-step engagement rates, holding three of the top four spots. These positions rely primarily on email correspondence, are typically among the most public-facing in an organization, and often involve interacting with various departments. Additionally, these roles are traditionally commission-based, meaning employees are financially incentivized to be helpful, respond to inquiries quickly, and resolve issues promptly.

Though not sales-oriented, Project Management’s second-place position is unsurprising. While “Project Manager” and similar titles can encompass a wide variety of responsibilities depending on industry and department, the fundamental goal remains the same: ensure projects are completed on time. Thus, if they receive an email seemingly related to a matter that could impact the progress of a project, they would be highly motivated to take steps to address the issue as quickly as possible.

These results, while not unexpected, remain concerning. The figures underscore how important it is to provide proactive and ongoing security awareness training to employees in these positions since, by the nature of their roles themselves or the personalities of those who fill them, they are at a greater risk of engaging with VEC.

---

## Across Borders: VEC and BEC Trends by Region

Because the 1,400 organizations in this analysis span North America, EMEA, and APAC, the data offers a unique opportunity to examine how employee behavior varies by geographic location. While engagement patterns differed across regions, one trend remained consistent: second-step interaction rates with both BEC and VEC were alarmingly high.

![Chart comparing BEC and VEC engagement rates across North America, EMEA, and APAC.]

### EMEA: External Impersonation Is a Blind Spot

For organizations in EMEA, the second-step engagement rate with VEC eclipsed that of BEC, exceeding it by 90%. Additionally, the repeat engagement rate for VEC was over twice as high for BEC and the highest of any geographic region. Interestingly, EMEA employees had the lowest reporting rate for vendor email compromise attacks—a shockingly low 0.27%—but the highest reporting rate for BEC attacks: 4.22%. They also had the lowest rate of second-step engagement with BEC (24.7%).

**The Bottom Line:** EMEA employees appear to be highly susceptible to continued interaction with VEC attacks but resistant to engaging with BEC, indicating vulnerability to external impersonations and suggesting stronger skepticism toward imitation of internal identities.

### APAC: Cultural and Compliance Factors Shape Risk

For APAC organizations, the data trended in the opposite direction of EMEA enterprises, with BEC engagement surpassing VEC. Though the variation is not as dramatic—BEC second-step engagement is just 10% higher—the rate itself (44.4%) remains concerning. Additionally, APAC employees had the highest BEC repeat engagement rate of any region (5.65%). However, while APAC employees engage with BEC attacks more than VEC, they at least report those attacks at a substantially higher rate, albeit still at a significantly lower than desired frequency (1.92%). Notably, APAC had the lowest vendor email compromise second-step engagement rate across all regions (40.24%), but even that remains far above acceptable levels.

**The Bottom Line:** In contrast to other regions, BEC poses the greater risk for APAC employees, with higher engagement and repeat interaction rates, but their comparatively higher reporting rate for BEC signals better recognition of internal threats.

### North America: Equal Opportunity for Exploitation

Employees at organizations in North America demonstrated equal vulnerability to BEC and VEC attacks, with a negligible difference between the second-step engagement rates for both attack types. However, similar to EMEA, the repeat engagement rate for VEC attacks was considerably higher than for BEC attacks—7.42% vs. 2.69%. This indicates employees may not recognize they’ve been manipulated, increasing the risk of repeated engagement without targeted intervention or improved training. Like their counterparts in EMEA and APAC, North American organizations reported BEC attacks more often than VEC, though reporting remained low overall.

**The Bottom Line:** North American employees engage with VEC and BEC attacks at nearly equal rates but are more likely to fall for vendor email compromise attacks repeatedly, suggesting greater challenges in recognizing vendor-based deception.

---

## The Reporting Deficit in Email Security

If your organization relies on employee reporting to understand the full extent of attack frequency, we have bad news: only 1.46% of text-based advanced email attacks that are read are reported.

To put that in perspective, the average monthly text-based advanced attacks received by a mid-market enterprise with 1,500-3,000 employees between March 2024 and March 2025 was approximately 560 per 1,000 mailboxes. That means, every month, there are an estimated 840-1,680 attacks not being reported to the security team. For larger organizations, the number can be much, much higher.

### Why Aren’t Employees Reporting Malicious Emails?

- **The Bystander Effect**: In this context, an employee may believe they aren’t the only target of an attack, and thus they don’t report the message because they assume a colleague already has.
- **No Harm, No Foul**: Some employees may believe that as long as they don’t engage with the attacker, they’ve fulfilled their obligation to the organization.
- **Fear of Being Wrong**: In some cases, an employee may feel uncertain about their ability to distinguish safe emails from attacks. Rather than risk flagging benign messages, they stay silent, either out of fear of looking foolish or creating unnecessary work for the security team.

---

## Thread Hijacked: Inside a Vendor Impersonation Attack

*Note: This attack was observed during a risk assessment in which Abnormal was operating in read-only mode, which is why it was not proactively blocked.*

In the example below, the attacker poses as an employee at a construction equipment rental company, hijacks an existing thread with a partner, and attempts to divert future invoice payments.

The first email in a thread was a legitimate message from “T.B.,” a project manager at the equipment rental organization, to “L.W.,” an employee at a contracting services company, regarding an invoice for services rendered.

Three weeks after this email was sent, the bad actor hijacked the thread using a lookalike domain. Posing as “J.B.,” an accounts receivable specialist, the perpetrator contacted L.W. regarding an update to the organization’s payment processes.

![Text of the fraudulent email claiming an account reconciliation audit and a transition to electronic payments.]

The fabricated message claimed that due to an ongoing account reconciliation audit, the company’s operating account had become inactive, and they were transitioning to electronic payments. The cybercriminal requested acknowledgment of the message so they could send new banking details.

The email contained no malicious links or attachments and had only minor grammar and punctuation issues. The attacker also used the impersonated employee’s real email signature. Simply put, to most employees, the email would raise zero red flags, which is likely why L.W. replied to the threat actor and even added two colleagues to the thread to assist with the request.

Shortly after the target replied, the cybercriminal emailed again, this time posing as the project manager, T.B. To manufacture a sense of urgency, the bad actor claimed that the contracting services company had multiple outstanding invoices that were more than two months overdue. L.W. once more responded and confirmed that as soon as the updated bank account information was provided, payment would be initiated.

At this point, Abnormal stepped in to prevent the attack from moving forward, despite being in passive-only mode.

---

## Why Behavioral AI Is the Best Defense Against Human-Centric Threats

Every time an employee has to decide whether an email is legitimate, the risk of human error enters the equation. And if they’re wrong, cybercriminals won’t hesitate to capitalize and cause financial consequences that ripple across the enterprise.

The challenge is that organizations have limited control over their vendors’ security postures and can only take steps to ensure their vendors’ vulnerabilities can’t be used against them. While security awareness training helps reduce the likelihood of employees engaging with threat actors, it’s not enough on its own. Humans can’t be your last line of defense.

The only effective strategy is to remove the burden of detection from employees entirely. That requires an innovative security solution—one that leverages AI to analyze identity, context, and content and builds behavioral baselines for every employee and vendor in your cloud environment. By understanding an organization’s unique communication patterns, an AI-native email security platform can detect subtle behavioral anomalies that traditional tools miss, enabling it to flag suspicious communications and automatically remediate threats before they reach employee inboxes.

---

## About Abnormal AI

Abnormal AI is the leading AI-native human behavior security platform, leveraging machine learning to stop sophisticated inbound attacks and detect compromised accounts across email and connected applications.

The anomaly detection engine leverages identity and context to understand human behavior and analyze the risk of every cloud email event—detecting and stopping sophisticated, socially-engineered attacks that target the human vulnerability.

You can deploy Abnormal in minutes with an API integration for Microsoft 365 or Google Workspace and experience the full value of the platform instantly. Additional protection is available for Slack, Workday, ServiceNow, Zoom, and multiple other cloud applications. Abnormal is currently trusted by more than 3,200 organizations, including over 20% of the Fortune 500, as it continues to redefine how cybersecurity works in the age of AI.