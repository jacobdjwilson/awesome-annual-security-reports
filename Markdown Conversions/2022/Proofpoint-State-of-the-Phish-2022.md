# An In-Depth Exploration of User Awareness, Vulnerability and Resilience
## 2022 State of the Phish
proofpoint.com
REPORT

Last year, we titled our introduction “A Year Like No Other.” We could easily have repeated that heading to describe 2021. The year has left many organizations contemplating what “normal” will mean for their workforces going forward. Along with hybrid and remote work options, organizations are mulling the best ways to keep employees connected and collaborative. Studies show the ongoing pandemic has had a major impact on workers’ mental health. Employees are feeling burned out, emotionally drained and distracted.[^1] Meanwhile, cyber attackers are as adept as ever. And they continue to use tactics and lures that resonate with employees and consumers alike.

In this, our eighth annual State of the Phish report, we explore user vulnerabilities from multiple angles. We look at issues driven by poor cyber hygiene and those that could result from a lack of knowledge and clear communication. We discuss ways organizations can become more attuned to their risks. And we outline opportunities to build and sustain engaging security awareness training initiatives in this challenging climate.

This year’s report includes analysis of data from the following sources:

### 2021: THE YEAR OF THE NEW NORMAL?
* A commissioned survey of **3,500** working adults across seven countries (Australia, France, Germany, Japan, Spain, the United Kingdom and the United States)
* A commissioned survey of **600** information and IT security professionals across the same seven countries
* Almost **100 million** simulated phishing attacks sent by our customers over a 12-month period
* More than **15 million** emails reported by our customers’ end users over that same time period

[^1]: Society for Human Resource Management. “Ongoing Pandemic Takes Toll on Workers’ Mental Health.” August 2021.

### A NOTE ON TERMINOLOGY
“Phishing” can mean different things to different people. We use the term in a broad sense to encompass all socially engineered email attacks, regardless of the specific malicious intent (such as directing users to dangerous websites, distributing malware, collecting credentials and so on).

Here are a few of the other terms we use throughout this report and how we define them:
* **Bulk phishing:** indiscriminate, “commodity” attacks in which the same email is sent to many people within an organization.
* **Spear phishing:** Targeted attacks sent to selected people within an organization.
* **Whaling:** Attacks against high-value targets, such as top executives.
* **Smishing:** Attacks that use mobile text messaging (SMS) as the main communication vector.
* **Vishing:** Attacks that use phone calls or voice messages to lure targets.

## Table of Contents
1.  [The 2021 Threat Landscape: a High-Level View](#the-2021-threat-landscape-a-high-level-view) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
    *   [Cashing in on COVID](#cashing-in-on-covid) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
    *   [Dialing to defraud](#dialing-to-defraud) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
    *   [Making it personal](#making-it-personal) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.  [By the Numbers: Targeted Attacks, Ransomware, and Ramifications](#by-the-numbers-targeted-attacks-ransomware-and-ramifications) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
    *   [Phishing attacks on the rise](#phishing-attacks-on-the-rise) . . . . . . . . . . . . . . . . . . . . . . . . 6
    *   [Other social engineering attacks also up](#other-social-engineering-attacks-also-up) . . . . . . . . . . . . . . 7
    *   [Attackers were more successful in 2021 than in 2020](#attackers-were-more-successful-in-2021-than-in-2020) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
    *   [Successful attacks had wide-ranging impacts](#successful-attacks-had-wide-ranging-impacts) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
    *   [Ransomware: nearly 60% of infected orgs paid up—many more than once](#ransomware-nearly-60-of-infected-orgs-paid-up-many-more-than-once) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.  [Working Adults: Cybersecurity Habits and Knowledge Gaps](#working-adults-cybersecurity-habits-and-knowledge-gaps) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
    *   [Overview: more devices, more issues](#overview-more-devices-more-issues) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
    *   [Survey says: communicate clearly to train effectively](#survey-says-communicate-clearly-to-train-effectively) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
    *   [Misconceptions about email](#misconceptions-about-email) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
    *   [Getting personal with employer-issued devices](#getting-personal-with-employer-issued-devices) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
    *   [Employee-driven risk: the (even) bigger picture](#employee-driven-risk-the-even-bigger-picture) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
    *   [Parting thoughts: risky business in 2021](#parting-thoughts-risky-business-in-2021) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.  [Benchmarking: Failure Rates and Comparison Data](#benchmarking-failure-rates-and-comparison-data) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
    *   [Failure rates by template type](#failure-rates-by-template-type) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
    *   [Industry failure rates](#industry-failure-rates) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
    *   [Department failure rates](#department-failure-rates) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.  [Email Reporting and Resilience: Measurements and Goals](#email-reporting-and-resilience-measurements-and-goals) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
    *   [Calculating resilience](#calculating-resilience) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
    *   [Benchmarking: industry resilience factors](#benchmarking-industry-resilience-factors) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
    *   [Real-world phishing and reporting accuracy](#real-world-phishing-and-reporting-accuracy) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
6.  [Security Awareness Training: Insights and Opportunities](#security-awareness-training-insights-and-opportunities) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
    *   [Training tools and frequency of use](#training-tools-and-frequency-of-use) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
    *   [Orgs ignore too many important topics when training users](#orgs-ignore-too-many-important-topics-when-training-users) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37
7.  [Making It Personal: Identifying Vulnerabilities, Gauging Success](#making-it-personal-identifying-vulnerabilities-gauging-success) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
8.  [Appendix](#appendix) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
    *   [A. Infosec and IT security survey: country-by-country breakdown](#a-infosec-and-it-security-survey-country-by-country-breakdown) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
    *   [B. Working adult survey: country-by-country breakdown](#b-working-adult-survey-country-by-country-breakdown) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
    *   [C. Industry failure rates by simulated phishing template style](#c-industry-failure-rates-by-simulated-phishing-template-style) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

---

<a name="the-2021-threat-landscape-a-high-level-view"></a>
## Section 1
## The 2021 Threat Landscape: a High-Level View
For many, 2021 felt like a year-long case of déjà vu. Pandemic-related concerns remained top-of-mind for employees and organizations—and for many cyber attackers. Human resources and operations teams suddenly had to support remote and hybrid work models. Meanwhile, information security and IT teams had to secure it all.

The first three quarters of the year were busy ones for cyber attackers: we identified nearly 5,500 campaigns[^2] that used one or more recognizable tactics. Our researchers also identified nearly 15 million phishing messages with malware payloads that have been directly linked to later-stage ransomware. Of these malware families, Dridex, The Trick, Emotet, Qbot, and Bazaloader were the most common.

**MALWARE** | **RANSOMWARE**
:---|:---
The Trick | WastedLocker
BazaLoader | Ryuk
SocGholish | Egregor
IcedID | Maze
Qbot | Sodinokibi
 | ProLock

Figure 1: Observed links between first-stage malware families and later-stage malware.

[^2]: We define a “campaign” as a group of related threats and activities. Phishing messages within a campaign share common attributes, like the same or similar subject lines, the same sending infrastructure, and the same eventual payload. Further research related to a campaign often reveals further commonalities, such as the threat actor behind it, the type of malware being used, and targeted geographies or industries.

<a name="cashing-in-on-covid"></a>
### Cashing in on COVID
Not surprisingly, COVID-themed campaigns continued, mimicking the opportunistic attacks that piggybacked pandemic developments throughout 2020. As public concerns ebbed and flowed, so did COVID-themed phishing attacks. We saw a lull through the spring and early summer of 2021. But as the delta variant took center stage, pandemic-themed attacks surged. Beginning in June 2021, we saw an uptick in campaigns that latched onto timely, relevant COVID-related topics, such as vaccine mandates and organizational policies.[^3]

<a name="dialing-to-defraud"></a>
### Dialing to defraud
Another trend involved telephone-oriented attack delivery (TOAD). These schemes are nothing new—we detect and block tens of thousands of TOAD-related emails every day.[^4] But we saw an uptick in 2021, many of them part of a robust and complex attack chain. Multi-faceted TOAD efforts use a variety of tools, such as:
*   Fraudulent emails
*   Call centers
*   Well-designed websites and mobile apps
*   Remote access software
*   Malware, including downloaders linked to later-stage ransomware delivery

Most TOAD threats require the victim’s active participation. While this approach may seem counter-intuitive from a security standpoint, it works. Perhaps the level of detail and familiar approach work in the attacker’s favor. For many people, calling a support line for help may seem a “safe” option. And many feel more comfortable when an “authority figure” talks them through account updates and refund processes. In addition, many organizations use the same remote access software that attackers exploit in TOAD schemes and other attacks. These activities could bypass security protections designed to block malicious remote access attempts.

<a name="making-it-personal"></a>
### Making it personal
TOAD threats and other attacks in 2021 targeted both personal and organizational email addresses. Amid the shift to remote work, targeting personal addresses can have a bigger impact on organizations than in years past. As we note later in the report, many people (and their family members!) are accessing personal information and accounts on employer-issued devices.

In general, the 2021 threat landscape reinforced one key point: successful threat protection requires people-centric defense in depth. Your users must be a key part of the security stack. The more informed and equipped they are, the more resilient your organization will be.

[^3]: Selena Larson (Proofpoint). “As Delta Variant Spreads, COVID-19 Themes Make Resurgence in Email Threats.” August 2021.
[^4]: Selena Larson, Sam Scholten and Timothy Kromphardt (Proofpoint). “Caught Beneath the Landline: A 411 on Telephone Oriented Attack Delivery.” November 2021.

> **ABUSING THE BRAND: HOW ATTACKERS PIGGYBACKED BIG TECH NAMES**
>
> Microsoft, Google, Zoom and Amazon were among the most abused brands in attack campaigns seen in the first three quarters of 2021. More than 1,100 campaigns abused the Microsoft brand, using a Microsoft-themed lure or product to steal credentials or deliver malware.
>
> Amazon campaigns tended to be high volume: fewer than 100 campaigns accounted for more than 68 million total messages. Much of this volume was attributable to sizeable Japanese-language campaigns, which continued into 2021 after surfacing in 2020. In comparison, about the same number of COVID-themed campaigns totaled around 1.3 million messages.

---
<a name="by-the-numbers-targeted-attacks-ransomware-and-ramifications"></a>
## Section 2
## By the Numbers: Targeted Attacks, Ransomware, and Ramifications
This year’s State of the Phish again presents the results of a Proofpoint-designed study of the threat landscape, as seen through the eyes of information security and IT security professionals. Our quantitative surveys, conducted by an outside polling firm, asked 600 participants across Australia, France, German, Japan, Spain, the United Kingdom and the United States about their organizations’ experiences in 2021.

<a name="phishing-attacks-on-the-rise"></a>
### Phishing attacks on the rise
According to respondents, the 2021 threat landscape was more active than 2020’s. Reports of phishing attacks were up across the board. Indiscriminate “bulk” phishing attacks rose 12% year over year. And increases in targeted attacks were even higher: reports of spear phishing/whaling and business email compromise (BEC)—which includes payroll redirect and supplier invoicing fraud—were up 20% and 18%, respectively.[^5] Note: the figures represented in Figure 2 include both successful and unsuccessful attacks.

[^5]: Unless otherwise indicated, survey results represent global averages. You can find country-by-country breakdowns of survey questions and findings in the Appendix.

<a name="image-figure-2"></a>
**Figure 2**
*A bar chart showing the volume of different types of attacks experienced by organizations in 2021. The chart is divided into four sections, each representing a different type of attack: Bulk Phishing Attacks, Spear Phishing and Whaling Attacks, BEC Attacks, and Email-Based Ransomware Attacks. Each section shows the percentage of organizations that experienced 1-10, 11-50, 50+ attacks, or an unknown number of attacks, or no attacks. Below each section is a summary of the percentage of organizations that faced that type of attack in 2021, with a comparison to 2020. There are also country spotlights highlighting specific regions.*

| Attack Type | 1-10 | 11-50 | 50+ | Total Unknown | No Attacks |
|---|---|---|---|---|---|
| Volume of Bulk Phishing Attacks | 14% | 36% | 33% | 15% | 2% |
| Volume of Spear Phishing and Whaling Attacks | 21% | 27% | 37% | 13% | 2% |
| Volume of BEC Attacks | 22% | 28% | 35% | 14% | 1% |
| Volume of Email-Based Ransomware Attacks | 23% | 27% | 35% | 13% | 2% |

*   **86%** of organizations faced bulk phishing attacks in 2021
*   **79%** of organizations saw attacks targeting specific users in 2021
*   **77%** of organizations faced BEC attacks in 2021
*   **78%** of organizations saw email-based ransomware attacks in 2021

<a name="image-a-look-back-at-2020"></a>
**A LOOK BACK AT 2020**
*   **77%** of organizations saw bulk phishing attacks
*   **66%** of organizations dealt with spear phishing attacks.
*   **65%** of organizations faced BEC attacks.

<a name="image-country-spotlight"></a>
**COUNTRY SPOTLIGHT**
*   **91%** of UK survey respondents said their organization faced bulk phishing attacks in 2021.
*   **90%** or more of Australian respondents said their organization faced spear phishing, BEC and email-based ransomware attacks in 2021.

[^6]: New figures for this year’s report. Note that survey respondents were specifically asked to identify attacks in which a ransomware payload was delivered or intended to be delivered via email.

<a name="other-social-engineering-attacks-also-up"></a>
### Other social engineering attacks also up
Email remains the top attack vector for cyber criminals. But it’s not the only way bad actors are trying to compromise people and the organizations they work for. Reports of SMS/text phishing (smishing), voice phishing (vishing), and social media-based attacks all increased by more than 20%. And reports of USB drops were up more than 15%.

<a name="image-figure-3"></a>
**Figure 3**
*A bar chart showing the volume of different types of social engineering attacks experienced by organizations in 2021. The chart is divided into four sections, each representing a different type of attack: Smishing Attacks, Vishing Attacks, Social Media Attacks, and Malicious USB Drops. Each section shows the percentage of organizations that experienced 1-10, 11-50, 50+ attacks, or an unknown number of attacks, or no attacks. Below each section is a summary of the percentage of organizations that faced that type of attack in 2021, with a comparison to 2020. There are also country spotlights highlighting specific regions.*

| Attack Type | 1-10 | 11-50 | 50+ | Total Unknown | No Attacks |
|---|---|---|---|---|---|
| Volume of Smishing Attacks | 26% | 23% | 34% | 16% | 1% |
| Volume of Vishing | 31% | 22% | 33% | 13% | 1% |
| Volume of Social Media Attacks | 26% | 21% | 34% | 17% | 2% |
| Volume of Malicious USB Drops | 36% | 19% | 32% | 12% | 1% |

*   **74%** of organizations faced smishing attacks in 2021
*   **69%** of organizations faced vishing attacks in 2021
*   **74%** of organizations saw social attacks in 2021
*   **64%** of organizations saw USB-based attacks in 2021

<a name="image-a-look-back-at-2020-2"></a>
**A LOOK BACK AT 2020**
*   **61%** saw smishing attacks.
*   **61%** dealt with social media attacks.
*   **54%** faced vishing attacks.
*   **54%** reported USB-based attacks.

<a name="image-country-spotlight-2"></a>
**COUNTRY SPOTLIGHT**
UK and Spanish respondents had very different experiences with non-email-based social engineering attacks in 2021:

**Spanish Organizations Were Least Likely to Face Attacks**
*   <60% faced smishing and social media attacks.
*   <50% faced vishing attacks and malicious USB drops.

**vs**

**UK Organizations Were Most Likely to Face High Volumes**
*   >20% faced 50+ smishing, social media, and vishing attacks.
*   18% faced 50+ malicious USB drops.

<a name="attackers-were-more-successful-in-2021-than-in-2020"></a>
### Attackers were more successful in 2021 than in 2020
Not every attempted attack succeeds. Millions of malicious emails are blocked by email gateways every day. Advanced email analysis and detection tools are getting better at identifying and stopping impostor emails and the many flavors of email fraud, including BEC. So in some ways, a successful phishing attack is like the proverbial needle in a haystack.

But those successful attacks do real damage. And 2021 was especially painful for the infosec and IT security workers we interviewed.

More than 80% of our survey respondents said their organization suffered a successful email-based phishing attack in 2021. That’s a 46% jump from 2020. Several factors may be at play in the increase, including those in the following sections.

#### Pandemic fatigue
The World Health Organization (WHO) defines pandemic fatigue, in part, as “demotivation to follow recommended protective behaviors, emerging gradually over time.”[^7] WHO’s behavioral focus centers around restrictions and suggestions related to containing infections. But many researchers have cautioned that COVID exhaustion is hurting people in other ways—including job performance.[^8] Attention spans are short. Many feel displaced and disconnected. Others struggle to remain engaged in work environments that revolve around virtual conferencing and an overload of screen time. The bottom line? People are not at their best. And that’s likely leading to more mistakes in the inbox.

#### Exploiting legitimate services
Cloud collaboration is now a normal part of business. And where people and organizations go, attackers follow.

In the first half of 2021, we saw a marked increase in the abuse of Microsoft and Google infrastructures, which were used to host and send threats across Microsoft 365 (including Office apps, OneDrive, and SharePoint), Microsoft Azure, Google Workspace, and Firebase storage. Because these messages mimic standard business processes, it can be hard for employees to tell the difference between malicious messages and safe ones apart.

This is especially true for employees who are unaware that attackers operate this way. And plenty are uninformed: more than 30% of working adults think that emails with familiar logos are safe, and 35% believe that all files stored in a cloud service like Google Drive are safe. (See more from our survey of working adults in Section 3.)

#### Use of trending content
Attackers have taken advantage of trending topics and events for years. But exploiting of trends seems to have become, well, a trend in itself. And it’s gotten more intense since the onset of the pandemic. We’ve seen attackers’ lures morphing to coincide with current public concerns and discourse with greater speed and strategy than ever.[^9]

Beyond evolving COVID lures in 2021, we saw attackers use lures associated with popular trends. Here are just a few examples of attack lures:
*   Streaming shows, such as “Squid Game”
*   Pop-culture events, such as a Justin Bieber world tour
*   Economic issues, such as U.S. unemployment programs

We even saw a sophisticated, multi-faceted campaign that included a fake streaming service, luring victims looking to cancel nonexistent subscriptions. (The campaign coincided with a wave of people cancelling their pandemic-fueled streaming video subscriptions.)

Attackers are skilled and savvy. They know the appeal of relevant content. And when content is more appealing, people are more likely to engage with it.

<a name="image-key-findings"></a>
**KEY FINDINGS**
*   **83%** of survey respondents said their organization experienced a successful email-based phishing attack in 2021, up from 57% in 2020.
*   **54%** said their organization dealt with more than three successful attacks.
*   **11%** experienced 10 or more successful attacks.

[^7]: World Health Organization, Regional Office for Europe. “Pandemic fatigue: Reinvigorating the public to prevent COVID-19.” October 2020.
[^8]: Healthline. “COVID Fatigue: How to Cope with Pandemic Burnout.” October 2021.

<a name="image-country-spotlight-3"></a>
**COUNTRY SPOTLIGHT**
*   **92%** of Australian organizations dealt with successful attacks, the highest of any region surveyed (and a 53% year-over-year increase).
*   **66%** of Japanese organizations experienced a successful phishing attack in 2021, the lowest of any region surveyed (though 18% higher than 2020).

[^9]: ThreatPost. “Phishers Capitalize on Headlines with Breakneck Speed.” October 2020.

<a name="successful-attacks-had-wide-ranging-impacts"></a>
### Successful attacks had wide-ranging impacts
Successful attacks don’t happen in a vacuum. Phishing emails can affect organizations in many ways. While some effects are immediate, others aren’t known about or felt until later.

We expanded our view of impacts this year (see Figure 4), so we can’t make year-over-year comparisons in some cases. But we did see an 8% drop in reports of credential compromise, a 6% drop in direct financial loss and a 2% drop in email-driven ransomware infections vs. 2020.

Still, these marginal improvements are little consolation, especially when considering the real-world consequences of each statistic. With the rise in crippling ransomware infections, critical infrastructure attacks and supply chain fraud, cybersecurity threats are more serious than ever.

<a name="image-key-findings-2"></a>
**KEY FINDINGS**
The impacts of successful phishing attacks varied widely in 2021. While Australia and Japan are both part of the Asia-Pacific region, respondents in the two countries reported wildly different experiences.

Australian organizations reported adverse outcomes of successful attacks at rates higher than global averages in all cases but one: just 20% of respondents said their organization experienced a widespread network outage following a phishing attack (vs. 22% globally).

At the other end of the spectrum, many of the differences were significant. For example, 30% reported direct financial loss, nearly twice the global average. And 61% said their organization experienced ransomware as an email payload, 33% higher than the global average.

In contrast, Japanese respondents reported lower-than-average effects in all cases but one: they matched the 27% global average for reports of malware other than ransomware. And their lows were markedly lower in multiple cases: just 3% said their organization experienced direct financial loss (vs. the 17% global average) or financial penalties (vs. the 11% global average). And no Japanese respondents said their organization faced an advanced persistent threat (APT) following a successful attack in 2021.

<a name="image-figure-4"></a>
**Figure 4**
*A bar chart showing the results of successful phishing attacks in 2021. The chart displays the percentage of organizations that experienced various impacts, such as breach of customer data, credential compromise, ransomware infection, and financial loss. The percentages are based on global averages.*

| Impact | Percentage |
|---|---|
| Breach of customer or client data | 54% |
| Credential/account compromise | 48% |
| Ransomware infection (payload delivered via email) | 46% |
| Loss of data/intellectual property | 44% |
| Malware other than ransomware | 27% |
| Reputational damage | 24% |
| Widespread network outage/downtime | 22% |
| Advanced persistent threat | 18% |
| Financial loss/wire transfer or invoice fraud | 17% |
| Zero-day exploit | 15% |
| Financial penalty/regulatory fine | 11% |

<a name="ransomware-nearly-60-of-infected-orgs-paid-up-many-more-than-once"></a>
### Ransomware: nearly 60% of infected orgs paid up—many more than once
Ransomware made headlines throughout 2021, with government and critical infrastructure sectors particularly hard hit. Security agencies around the globe cautioned organizations of all sizes to strengthen their defenses against ransomware, and with good reason.

Our researchers have been tracking threat actors who have become initial access brokers and, likely, ransomware affiliates, selling the access they’ve gained through first-stage malware to other operators. This scale and the availability of ransomware-as-a-service offerings have both fueled the rise in successful attacks.[^10]

As shown in Figure 5, nearly 70% of organizations dealt with at least one ransomware infection 2021 (a slight increase over 2020). Of those, nearly two-thirds experienced more than three separate infections. And nearly 15% dealt with more than 10 separate infections.[^11]

Once infected, nearly 60% opted to negotiate with attackers (with mixed results), despite cybersecurity and government agencies warning against the practice. As always, payment does not guarantee restoration of data (as some of our survey respondents found out firsthand). In addition, ransomware payments are likely to fuel the fire, rewarding attackers for their activities and encouraging repeat behavior.

<a name="image-key-finding-3"></a>
**KEY FINDING**
*   **68%** of organizations experienced at least one ransomware infection in 2021 (up from 66% in 2020).

[^10]: Proofpoint. “Tips for Developing Your Ransomware Defense Strategy.” November 2021.
[^11]: This includes infections from all sources, including initial payloads and later-stage delivery. The number of separate infections may have resulted from a single intrusion or separate incidents.

<a name="image-figure-5"></a>
**Figure 5**
*A set of pie charts and a bar chart showing the impact of ransomware attacks in 2021. The pie chart on the left shows what happened after payment, with the majority of organizations regaining access to data after the first payment. The pie chart on the right shows the number of separate ransomware infections experienced by organizations. The bar chart below shows the percentage of organizations that experienced 1-3, 4-6, 7-9, or 10 or more separate infections, or were unsure of the total.*

**Ransomware Infections: What Happened After Payment**
*   Regained access to data/systems after first payment: 54%
*   Paid additional ransom demand(s) and eventually regained access: 32%
*   Refused to pay additional ransom demand(s) and walked away without data: 10%
*   Never got access to data/systems, even after paying ransom(s): 4%

*   **58%** of infected organizations agreed to pay ransom in 2021

**Ransomware by the Numbers**
*   1-3 separate infections: 34%
*   4-6 separate infections: 35%
*   7-9 separate infections: 16%
*   10 or more separate infections: 14%
*   Unsure of total: 1%

*   **68%** of organizations were infected by ransomware in 2021

<a name="image-country-spotlight-4"></a>
**COUNTRY SPOTLIGHT**
*   **81%** of French organizations experienced a ransomware infection last year, the highest of any country surveyed. (At 50%, Japanese organizations were least likely to experience an infection.)
*   **30%** of Australian organizations that experienced ransomware said they dealt with 10 or more separate infections.
*   **82%** of UK organizations that were infected opted to pay the ransom, the highest of any region surveyed (and 41% higher than the global average).
*   **42%** of Spanish organizations admitted to paying more than one ransom to regain access to data, the highest of any region surveyed. But at 21%, they were also the most likely to refuse to pay a follow-up ransom after making an initial payment.

---
<a name="working-adults-cybersecurity-habits-and-knowledge-gaps"></a>
## Section 3
## Working Adults: Cybersecurity Habits and Knowledge Gaps
As in the past, this year’s State of the Phish dedicates significant real estate to exploring the greatest source of organizational security