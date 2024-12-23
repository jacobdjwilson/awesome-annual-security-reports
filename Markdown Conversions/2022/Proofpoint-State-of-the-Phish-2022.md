# An In-Depth Exploration of User Awareness, Vulnerability and Resilience
## 2022 State of the Phish
proofpoint.com
REPORT

Last year, we titled our introduction “A Year Like No Other.” We could easily have repeated that heading to describe 2021. The year has left many organizations contemplating what “normal” will mean for their workforces going forward. Along with hybrid and remote work options, organizations are mulling the best ways to keep employees connected and collaborative. Studies show the ongoing pandemic has had a major impact on workers’ mental health. Employees are feeling burned out, emotionally drained and distracted.[^1] Meanwhile, cyber attackers are as adept as ever. And they continue to use tactics and lures that resonate with employees and consumers alike.

In this, our eighth annual State of the Phish report, we explore user vulnerabilities from multiple angles. We look at issues driven by poor cyber hygiene and those that could result from a lack of knowledge and clear communication. We discuss ways organizations can become more attuned to their risks. And we outline opportunities to build and sustain engaging security awareness training initiatives in this challenging climate.

This year’s report includes analysis of data from the following sources:

2021: THE YEAR OF THE NEW NORMAL?
- A commissioned survey of 3,500 working adults across seven countries (Australia, France, Germany, Japan, Spain, the United Kingdom and the United States)
- A commissioned survey of 600 information and IT security professionals across the same seven countries
- Almost 100 million simulated phishing attacks sent by our customers over a 12-month period
- More than 15 million emails reported by our customers’ end users over that same time period

[^1]: Society for Human Resource Management. “Ongoing Pandemic Takes Toll on Workers’ Mental Health.” August 2021.

A NOTE ON TERMINOLOGY
“Phishing” can mean different things to different people. We use the term in a broad sense to encompass all socially engineered email attacks, regardless of the specific malicious intent (such as directing users to dangerous websites, distributing malware, collecting credentials and so on).

Here are a few of the other terms we use throughout this report and how we define them:
- Bulk phishing: indiscriminate, “commodity” attacks in which the same email is sent to many people within an organization.
- Spear phishing: Targeted attacks sent to selected people within an organization.
- Whaling: Attacks against high-value targets, such as top executives.
- Smishing: Attacks that use mobile text messaging (SMS) as the main communication vector.
- Vishing: Attacks that use phone calls or voice messages to lure targets.

## Table of Contents
- [The 2021 Threat Landscape: a High-Level View](#the-2021-threat-landscape-a-high-level-view)
- [By the Numbers: Targeted Attacks, Ransomware, and Ramifications](#by-the-numbers-targeted-attacks-ransomware-and-ramifications)
- [Working Adults: Cybersecurity Habits and Knowledge Gaps](#working-adults-cybersecurity-habits-and-knowledge-gaps)
- [Benchmarking: Failure Rates and Comparison Data](#benchmarking-failure-rates-and-comparison-data)
- [Email Reporting and Resilience: Measurements and Goals](#email-reporting-and-resilience-measurements-and-goals)
- [Security Awareness Training: Insights and Opportunities](#security-awareness-training-insights-and-opportunities)
- [Making It Personal: Identifying Vulnerabilities, Gauging Success](#making-it-personal-identifying-vulnerabilities-gauging-success)
- [Appendix](#appendix)
    - [Infosec and IT security survey: country-by-country breakdown](#infosec-and-it-security-survey-country-by-country-breakdown)
    - [Working adult survey: country-by-country breakdown](#working-adult-survey-country-by-country-breakdown)
    - [Industry failure rates by simulated phishing template style](#industry-failure-rates-by-simulated-phishing-template-style)

# Section 1
## The 2021 Threat Landscape: a High-Level View
For many, 2021 felt like a year-long case of déjà vu. Pandemic-related concerns remained top-of-mind for employees and organizations—and for many cyber attackers. Human resources and operations teams suddenly had to support remote and hybrid work models. Meanwhile, information security and IT teams had to secure it all.

The first three quarters of the year were busy ones for cyber attackers: we identified nearly 5,500 campaigns[^2] that used one or more recognizable tactics. Our researchers also identified nearly 15 million phishing messages with malware payloads that have been directly linked to later-stage ransomware. Of these malware families, Dridex, The Trick, Emotet, Qbot, and Bazaloader were the most common.

MALWARE
RANSOMWARE
The Trick
WastedLocker
BazaLoader
Ryuk
SocGholish
Egregor
IcedID
Maze
Qbot
Sodinokibi
ProLock

![Observed links between first-stage malware families and later-stage malware]

[^2]: We define a “campaign” as a group of related threats and activities. Phishing messages within a campaign share common attributes, like the same or similar subject lines, the same sending infrastructure, and the same eventual payload. Further research related to a campaign often reveals further commonalities, such as the threat actor behind it, the type of malware being used, and targeted geographies or industries.

## Cashing in on COVID
Not surprisingly, COVID-themed campaigns continued, mimicking the opportunistic attacks that piggybacked pandemic developments throughout 2020. As public concerns ebbed and flowed, so did COVID-themed phishing attacks. We saw a lull through the spring and early summer of 2021. But as the delta variant took center stage, pandemic-themed attacks surged. Beginning in June 2021, we saw an uptick in campaigns that latched onto timely, relevant COVID-related topics, such as vaccine mandates and organizational policies.[^3]

## Dialing to defraud
Another trend involved telephone-oriented attack delivery (TOAD). These schemes are nothing new—we detect and block tens of thousands of TOAD-related emails every day.[^4] But we saw an uptick in 2021, many of them part of a robust and complex attack chain. Multi-faceted TOAD efforts use a variety of tools, such as:
- Fraudulent emails
- Call centers
- Well-designed websites and mobile apps
- Remote access software
- Malware, including downloaders linked to later-stage ransomware delivery

Most TOAD threats require the victim’s active participation. While this approach may seem counter-intuitive from a security standpoint, it works. Perhaps the level of detail and familiar approach work in the attacker’s favor. For many people, calling a support line for help may seem a “safe” option. And many feel more comfortable when an “authority figure” talks them through account updates and refund processes. In addition, many organizations use the same remote access software that attackers exploit in TOAD schemes and other attacks. These activities could bypass security protections designed to block malicious remote access attempts.

## Making it personal
TOAD threats and other attacks in 2021 targeted both personal and organizational email addresses. Amid the shift to remote work, targeting personal addresses can have a bigger impact on organizations than in years past. As we note later in the report, many people (and their family members!) are accessing personal information and accounts on employer-issued devices.

In general, the 2021 threat landscape reinforced one key point: successful threat protection requires people-centric defense in depth. Your users must be a key part of the security stack. The more informed and equipped they are, the more resilient your organization will be.

[^3]: Selena Larson (Proofpoint). “As Delta Variant Spreads, COVID-19 Themes Make Resurgence in Email Threats.” August 2021.
[^4]: Selena Larson, Sam Scholten and Timothy Kromphardt (Proofpoint). “Caught Beneath the Landline: A 411 on Telephone Oriented Attack Delivery.” November 2021.

ABUSING THE BRAND: HOW ATTACKERS PIGGYBACKED BIG TECH NAMES
Microsoft, Google, Zoom and Amazon were among the most abused brands in attack campaigns seen in the first three quarters of 2021. More than 1,100 campaigns abused the Microsoft brand, using a Microsoft-themed lure or product to steal credentials or deliver malware.

Amazon campaigns tended to be high volume: fewer than 100 campaigns accounted for more than 68 million total messages. Much of this volume was attributable to sizeable Japanese-language campaigns, which continued into 2021 after surfacing in 2020. In comparison, about the same number of COVID-themed campaigns totaled around 1.3 million messages.

# Section 2
## By the Numbers: Targeted Attacks, Ransomware, and Ramifications
This year’s State of the Phish again presents the results of a Proofpoint-designed study of the threat landscape, as seen through the eyes of information security and IT security professionals. Our quantitative surveys, conducted by an outside polling firm, asked 600 participants across Australia, France, German, Japan, Spain, the United Kingdom and the United States about their organizations’ experiences in 2021.

## Phishing attacks on the rise
According to respondents, the 2021 threat landscape was more active than 2020’s. Reports of phishing attacks were up across the board. Indiscriminate “bulk” phishing attacks rose 12% year over year. And increases in targeted attacks were even higher: reports of spear phishing/whaling and business email compromise (BEC)—which includes payroll redirect and supplier invoicing fraud—were up 20% and 18%, respectively.[^5] Note: the figures represented in Figure 2 include both successful and unsuccessful attacks.

[^5]: Unless otherwise indicated, survey results represent global averages. You can find country-by-country breakdowns of survey questions and findings in the Appendix.

[^6]: New figures for this year’s report. Note that survey respondents were specifically asked to identify attacks in which a ransomware payload was delivered or intended to be delivered via email.

![Volume of Bulk Phishing Attacks 1-10:14%, 11-50:36%, 50+:33%, Total unknown:15%, No attacks:2%
Volume of Spear Phishing and Whaling Attacks 1-10:21%, 11-50:27%, 50+:37%, Total unknown:13%, No attacks:2%
Volume of BEC Attacks 1-10:23%, 11-50:27%, 50+:35%, Total unknown:13%, No attacks:2%
Volume of Email-Based Ransomware Attacks 1-10:22%, 11-50:28%, 50+:35%, Total unknown:14%, No attacks:1%]

- 86% of organizations faced bulk phishing attacks in 2021
- 79% of organizations saw attacks targeting specific users in 2021
- 77% of organizations faced BEC attacks in 2021
- 78% of organizations saw email-based ransomware attacks in 2021

A LOOK BACK AT 2020
- 77% of organizations saw bulk phishing attacks
- 66% of organizations dealt with spear phishing attacks.
- 65% of organizations faced BEC attacks.

COUNTRY SPOTLIGHT
- 91% of UK survey respondents said their organization faced bulk phishing attacks in 2021.
- 90% or more of Australian respondents said their organization faced spear phishing, BEC and email-based ransomware attacks in 2021.

## Other social engineering attacks also up
Email remains the top attack vector for cyber criminals. But it’s not the only way bad actors are trying to compromise people and the organizations they work for. Reports of SMS/text phishing (smishing), voice phishing (vishing), and social media-based attacks all increased by more than 20%. And reports of USB drops were up more than 15%.

![Volume of Smishing Attacks 1-10:26%, 11-50:23%, 50+:34%, Total unknown:16%, No attacks:1%
Volume of Vishing 1-10:31%, 11-50:22%, 50+:33%, Total unknown:13%, No attacks:1%
Volume of Social Media Attacks 1-10:26%, 11-50:21%, 50+:34%, Total unknown:17%, No attacks:2%
Volume of Malicious USB Drops 1-10:36%, 11-50:19%, 50+:32%, Total unknown:12%, No attacks:2%]

- 74% of organizations faced smishing attacks in 2021
- 69% of organizations faced vishing attacks in 2021
- 74% of organizations saw social attacks in 2021
- 64% of organizations saw USB-based attacks in 2021

COUNTRY SPOTLIGHT
UK and Spanish respondents had very different experiences with non-email-based social engineering attacks in 2021:

Spanish Organizations Were Least Likely to Face Attacks
- <60% faced smishing and social media attacks.
- <50% faced vishing attacks and malicious USB drops.

vs

UK Organizations Were Most Likely to Face High Volumes
- >20% faced 50+ smishing, social media, and vishing attacks.
- 18% faced 50+ malicious USB drops.

A LOOK BACK AT 2020
- 61% saw smishing attacks.
- 61% dealt with social media attacks.
- 54% faced vishing attacks.
- 54% reported USB-based attacks.

## Attackers were more successful in 2021 than in 2020
Not every attempted attack succeeds. Millions of malicious emails are blocked by email gateways every day. Advanced email analysis and detection tools are getting better at identifying and stopping impostor emails and the many flavors of email fraud, including BEC. So in some ways, a successful phishing attack is like the proverbial needle in a haystack.

But those successful attacks do real damage. And 2021 was especially painful for the infosec and IT security workers we interviewed.

More than 80% of our survey respondents said their organization suffered a successful email-based phishing attack in 2021. That’s a 46% jump from 2020. Several factors may be at play in the increase, including those in the following sections.

### Pandemic fatigue
The World Health Organization (WHO) defines pandemic fatigue, in part, as “demotivation to follow recommended protective behaviors, emerging gradually over time.”[^7] WHO’s behavioral focus centers around restrictions and suggestions related to containing infections. But many researchers have cautioned that COVID exhaustion is hurting people in other ways—including job performance.[^8]

Attention spans are short. Many feel displaced and disconnected. Others struggle to remain engaged in work environments that revolve around virtual conferencing and an overload of screen time. The bottom line? People are not at their best. And that’s likely leading to more mistakes in the inbox.

### Exploiting legitimate services
Cloud collaboration is now a normal part of business. And where people and organizations go, attackers follow.

In the first half of 2021, we saw a marked increase in the abuse of Microsoft and Google infrastructures, which were used to host and send threats across Microsoft 365 (including Office apps, OneDrive, and SharePoint), Microsoft Azure, Google Workspace, and Firebase storage. Because these messages mimic standard business processes, it can be hard for employees to tell the difference between malicious messages and safe ones apart.

This is especially true for employees who are unaware that attackers operate this way. And plenty are uninformed: more than 30% of working adults think that emails with familiar logos are safe, and 35% believe that all files stored in a cloud service like Google Drive are safe. (See more from our survey of working adults in Section 3.)

KEY FINDINGS
- 83% of survey respondents said their organization experienced a successful email-based phishing attack in 2021, up from 57% in 2020.
- 54% said their organization dealt with more than three successful attacks.
- 11% experienced 10 or more successful attacks.

[^7]: World Health Organization, Regional Office for Europe. “Pandemic fatigue: Reinvigorating the public to prevent COVID-19.” October 2020.
[^8]: Healthline. “COVID Fatigue: How to Cope with Pandemic Burnout.” October 2021.

COUNTRY SPOTLIGHT
- 92% of Australian organizations dealt with successful attacks, the highest of any region surveyed (and a 53% year-over-year increase).
- 66% of Japanese organizations experienced a successful phishing attack in 2021, the lowest of any region surveyed (though 18% higher than 2020).

### Use of trending content
Attackers have taken advantage of trending topics and events for years. But exploiting of trends seems to have become, well, a trend in itself. And it’s gotten more intense since the onset of the pandemic. We’ve seen attackers’ lures morphing to coincide with current public concerns and discourse with greater speed and strategy than ever.[^9]

Beyond evolving COVID lures in 2021, we saw attackers use lures associated with popular trends. Here are just a few examples of attack lures:
- Streaming shows, such as “Squid Game”
- Pop-culture events, such as a Justin Bieber world tour
- Economic issues, such as U.S. unemployment programs

We even saw a sophisticated, multi-faceted campaign that included a fake streaming service, luring victims looking to cancel nonexistent subscriptions. (The campaign coincided with a wave of people cancelling their pandemic-fueled streaming video subscriptions.)

Attackers are skilled and savvy. They know the appeal of relevant content. And when content is more appealing, people are more likely to engage with it.

## Successful attacks had wide-ranging impacts
Successful attacks don’t happen in a vacuum. Phishing emails can affect organizations in many ways. While some effects are immediate, others aren’t known about or felt until later.

We expanded our view of impacts this year (see Figure 4), so we can’t make year-over-year comparisons in some cases. But we did see an 8% drop in reports of credential compromise, a 6% drop in direct financial loss and a 2% drop in email-driven ransomware infections vs. 2020.

Still, these marginal improvements are little consolation, especially when considering the real-world consequences of each statistic. With the rise in crippling ransomware infections, critical infrastructure attacks and supply chain fraud, cybersecurity threats are more serious than ever.

[^9]: ThreatPost. “Phishers Capitalize on Headlines with Breakneck Speed.” October 2020.

KEY FINDINGS
The impacts of successful phishing attacks varied widely in 2021. While Australia and Japan are both part of the Asia-Pacific region, respondents in the two countries reported wildly different experiences.

Australian organizations reported adverse outcomes of successful attacks at rates higher than global averages in all cases but one: just 20% of respondents said their organization experienced a widespread network outage following a phishing attack (vs. 22% globally).

At the other end of the spectrum, many of the differences were significant. For example, 30% reported direct financial loss, nearly twice the global average. And 61% said their organization experienced ransomware as an email payload, 33% higher than the global average.

In contrast, Japanese respondents reported lower-than-average effects in all cases but one: they matched the 27% global average for reports of malware other than ransomware. And their lows were markedly lower in multiple cases: just 3% said their organization experienced direct financial loss (vs. the 17% global average) or financial penalties (vs. the 11% global average). And no Japanese respondents said their organization faced an advanced persistent threat (APT) following a successful attack in 2021.

![Breach of customer or client data:54%, Credential/account compromise:48%, Ransomware infection (payload delivered via email):46%, Loss of data/intellectual property:44%, Malware other than ransomware:27%, Reputational damage:24%, Widespread network outage/downtime:22%, Advanced persistent threat:18%, Financial loss/wire transfer or invoice fraud:17%, Zero-day exploit:15%, Financial penalty/regulatory fine:11%]

## Ransomware: nearly 60% of infected orgs paid up—many more than once
Ransomware made headlines throughout 2021, with government and critical infrastructure sectors particularly hard hit. Security agencies around the globe cautioned organizations of all sizes to strengthen their defenses against ransomware, and with good reason.

Our researchers have been tracking threat actors who have become initial access brokers and, likely, ransomware affiliates, selling the access they’ve gained through first-stage malware to other operators. This scale and the availability of ransomware-as-a-service offerings have both fueled the rise in successful attacks.[^10]

As shown in Figure 5, nearly 70% of organizations dealt with at least one ransomware infection 2021 (a slight increase over 2020). Of those, nearly two-thirds experienced more than three separate infections. And nearly 15% dealt with more than 10 separate infections.[^11]

[^10]: Proofpoint. “Tips for Developing Your Ransomware Defense Strategy.” November 2021.
[^11]: This includes infections from all sources, including initial payloads and later-stage delivery. The number of separate infections may have resulted from a single intrusion or separate incidents.

KEY FINDING
- 68% of organizations experienced at least one ransomware infection in 2021 (up from 66% in 2020).

Once infected, nearly 60% opted to negotiate with attackers (with mixed results), despite cybersecurity and government agencies warning against the practice. As always, payment does not guarantee restoration of data (as some of our survey respondents found out firsthand). In addition, ransomware payments are likely to fuel the fire, rewarding attackers for their activities and encouraging repeat behavior.

![Ransomware Infections: What Happened After Payment Regained access to data/systems after first payment:54%, Paid additional ransom demand(s) and eventually regained access:32%, Refused to pay additional ransom demand(s) and walked away without data:10%, Never got access to data/systems, even after paying ransom(s):4%
Ransomware by the Numbers 1-3 separate infections:34%, 4-6 separate infections:35%, 7-9 separate infections:16%, 10 or more separate infections:14%, Unsure of total:1%]

- 58% of infected organizations agreed to pay ransom in 2021
- 68% of organizations were infected by ransomware in 2021

COUNTRY SPOTLIGHT
- 81% of French organizations experienced a ransomware infection last year, the highest of any country surveyed. (At 50%, Japanese organizations were least likely to experience an infection.)
- 30% of Australian organizations that experienced ransomware said they dealt with 10 or more separate infections.
- 82% of UK organizations that were infected opted to pay the ransom, the highest of any region surveyed (and 41% higher than the global average).
- 42% of Spanish organizations admitted to paying more than one ransom to regain access to data, the highest of any region surveyed. But at 21%, they were also the most likely to refuse to pay a follow-up ransom after making an initial payment.

# Section 3
## Working Adults: Cybersecurity Habits and Knowledge Gaps
As in the past, this year’s State of the Phish dedicates significant real estate to exploring the greatest source of organizational security risk: people. Our quantitative surveys, conducted by a third party, asked 3,500 working adults across seven countries (Australia, France, German, Japan, Spain, the United Kingdom and the United States) about their cybersecurity perceptions, habits and experiences in 2021.

All survey participants identified as being 18 years or older and employed. Different roles and responsibilities are represented in this group of respondents—a blend that reflects the workforces in many organizations. We didn’t isolate on “deskbound” workers or those in computer-dominated positions—and that was intentional. We wanted the survey group to represent the makeup of all the people who can influence an organization’s security posture. And make no mistake: every person who works within an organization can have a positive or negative impact on security, no matter what their role is.

## Overview: more devices, more issues
All survey respondents said they use one or more electronic devices (phone/smartphone, laptop computer, desktop computer or tablet) for their job. Among these:
- 73% said they have access to at least one employer-issued device
- 74% said they use one or more of their own devices for work-related purposes
- 54% use a personal phone/smartphone and 22% use a personal tablet for work
- 44% said they are in a new remote working environment (either full time or part time) due to the pandemic[^12]
- 83% said they received at least one suspicious communication (either via email, text message, social media, or phone call) in 2021
- 42% said they took a dangerous action (clicked a malicious link, downloaded malware, or exposed their personal data or login credentials) in 2021

We highlight these statistics to illustrate a point that must be considered throughout this section: workers’ personal choices often lead to organizational risk.[^13]

[^12]: To add more context, we also asked our infosec and IT professionals about the impact the pandemic has had on remote work. Some 81% said at least half of their organization’s employees are now working remotely, either full time or part time. Another 14% said employees had worked remotely due to COVID, but were no longer doing so (while just 6% of our working adults said the same).
[^13]: Unless otherwise indicated, survey results represent global averages. You can find country-by-country breakdowns of survey questions and findings in the Appendix.

COUNTRY SPOTLIGHT
- 80% of U.S. workers use one or more of their own mobile devices for work. 64% said they use personal phones/smartphones, and 30% use personal tablets. These results were the highest of any region surveyed.
- 32% of Japanese workers said they do not have access to an employer-issued electronic device (but 100% use one or more electronic devices for work purposes).
- 33% of U.S. workers and 30% of Australian workers said they are now working remotely full time due to the pandemic, well more than the 20% global average.
- 30% of UK workers now have a hybrid approach to working (part-time on site, part time remote).
- 47% of French workers and 45% of German workers said the pandemic did not impact their work location, the highest among the regions surveyed.

## Survey says: communicate clearly to train effectively
We’ve been assessing working adults’ recognition of common cybersecurity terminology for several years. And while we saw some decent progress last year, this year’s results have rolled that back. One considerable drop was with the term “phishing”: correct answers were down more than 15%, and “I’m not sure” responses were up more than 30%.

Ransomware responses provided the one bright spot, with recognition up about 10% and unsure responses holding steady. With the rise in ransomware attacks around the globe, this improvement comes at a good time.

The overall decline in awareness is another area where pandemic fatigue—and its impact on workers’ engagement and attention spans—could be a factor. It could also reflect a decreased prioritization of cybersecurity awareness and training initiatives during 2021. The pandemic has put many different pressures on organizations, and some may have been forced (due to lack of time, resources or other factors) to deprioritize employee education programs.

Another possibility: perhaps workers are overloaded by the sheer amount of terminology they hear or news stories detailing cyber attacks and warning of dire consequences. People may simply be feeling overwhelmed and confused.

Whatever the case, this year’s results make it clear: it is never safe to assume workers recognize security lingo, no matter how often these terms make headlines. This is especially true if your formal security awareness training sessions—apart from phishing simulations—happen infrequently. Reminders and reinforcement are critical to knowledge and skill development. Employees need to understand the language you speak to fully absorb what you’re saying and, eventually, learn from it.

Our “what is” survey questions offered three multiple choice answers and an “I’m not sure” option. In reviewing results, consider that users who don’t know an answer may pose as much risk as those who answer incorrectly.

### Term limits: what users (don’t) know
- **What is PHISHING?** Correct answers were down from last year’s 63% mark, a 16% year-over-year decrease. UK workers were again most likely to answer correctly—but this year’s 62% fell short of last year’s 69%.

![Correct:53%, Incorrect:27%, I Don't Know:20%]

- **What is RANSOMWARE?** This is the only term that saw an increase in recognition, with correct answers rising from 33% and incorrect responses falling from 36%. (Unsure responses held steady at 31%.) At 49% correct, Australian workers performed well above the global average. French and German workers were least likely to answer correctly (at 27% and 26%, respectively).

![Correct:36%, Incorrect:33%, I Don't Know:31%]

- **What is MALWARE?** Like last year, Spanish workers led their global counterparts in recognition of this term. But this year’s 73% was lower than last year’s 75% (and well off the 80% high mark from two years ago). At 52%, Japanese workers were least likely to answer this correctly, and another 38% were unsure of how to answer.

![Correct:63%, Incorrect:20%, I Don't Know:17%]

- **What is SMISHING?** Global recognition of this term was down from 31% last year, a 26% year-over-year drop. Japanese workers again struggled with this term. Just 17% answered correctly (down from 19% last year), and 56% were unsure of how to answer (the same as last year).

![Correct:23%, Incorrect:32%, I Don't Know:45%]

- **What is VISHING?** 30% of global respondents answered this question correctly last year, representing a 20% year-over-year decrease in recognition. French workers went from first to worst in recognition of this term. Last year, they led all regions at 54% correct. This year, just 17% answered correctly (a decrease of nearly 70%).

![Correct:24%, Incorrect:31%, I Don't Know:45%]

## Misconceptions about email
Defining cybersecurity threats isn’t always a key to defending against them. So, we wanted to know what workers believe to be true about email and email-based attack methods.

We saw plenty of bright spots. For example, 86% of respondents recognize that they should be cautious of any unsolicited message. And this response level was mostly steady across all regions surveyed. At 81%, French workers were the only group to dip below the 85% mark.

But there’s always room for improvement. We see some areas where quick and clear communication is called for. Employees need immediate clarity on key points like internal email, cloud documents, and the need to take personal responsibility for email security. More than two-thirds of respondents showed a lack of understanding about the capabilities of technical email safeguards on work accounts. That lack of knowledge is a clear and present danger to organizations around the globe.

![know that email attachments can be malicious:81%, know that an email can appear to come from someone other than the true sender:77%, know that familiar logos and contact information aren’t an automatic indication of safety:52%, know that their personal email provider cannot block all dangerous email:38%, know that files stored in the cloud can be malicious:37%, know that unsafe contacts may email them multiple times:37%, know that even internal emails could be dangerous:36%, know that their organization’s security tools cannot block all dangerous email:30%]

[^14]: We asked similar questions in last year’s survey, but in a different format. We believe this year’s format offered more clarity and more accurate findings. Full details and results for these questions are in the Appendix.

COUNTRY SPOTLIGHT
Top Performers
- 85% of German workers know that email attachments can be dangerous.
- 82% of UK workers know that an email’s sender details can be disguised.
- 63% of Japanese workers know that familiar logos in emails don’t equate to safety.
- 49% of Japanese workers know that unsafe contacts may email them multiple times.

vs

Bottom Performers
- 59% of Spanish workers think that all internal emails are safe
- 57% of Spanish workers think their organization will automatically block all malicious email (and 49% believe their personal email provider will do the same)
- 46% of U.S. workers think that all files stored in the cloud are safe
- 42% of U.S. workers believe all emails with familiar logos are safe

## Getting personal with employer-issued devices
With 44% of global workers saying they are working remotely either part-time or full-time due to the pandemic, the line between personal life and work life is murkier than ever. But here’s something that is clear: employees’ personal choices can pose a major risk to your data, devices and systems.

As noted earlier in this section, 73% of our survey participants said they have access to at least one employer-issued electronic device. Of those, 77% admitted to using those devices for personal purposes. This is a drop from last year’s 81%, and as shown in Figure 7, we saw a decline in several specific activities.

For example, the number of workers who said they check personal email on employer devices decreased more than 25%. Social media use also decreased, down 15% year over year. But online shopping was up—and the number of people who said they play games on employer devices jumped more than 75%.

KEY FINDING
- 56% of workers who have an employer-issued device grant access to friends and/or family members (up from 52% last year).

![Personal Activities Performed on Work-Issued Devices Check/respond to personal email:2019:79%, 2020:57%, 2021:42%, Read news stories:2019:40%, 2020:41%, 2021:40%, Research (new products, travel destinations etc.):2019:37%, 2020:34%, 2021:37%, Shop online:2019:35%, 2020:34%, 2021:37%, View/post to social media:2019:40%, 2020:29%, 2021:28%, Stream media (music, videos etc.):2019:27%, 2020:25%, 2021:23%, Play games:2019:11%, 2020:13%, 2021:23%]

While workers’ personal use of employer devices decreased overall, their willingness to grant access to friends and family increased. More than 55% of those with employer devices allow others to use them. About 5% admitted that use is unsupervised, meaning they do not monitor or restrict activities on the devices. (A seemingly small number, but a mighty risk.)

Some friends and family activities increased while others decreased. As with workers themselves, playing games showed the largest gain (up nearly 75% over last year). And as shown in Figure 8, several of the activities are up sharply since our 2019 survey.

![Friends and Family Activities Performed on Work-Issued Devices