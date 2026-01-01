# 2022 State of the Phish Report

The official report URL is: https://go.proofpoint.com/en-2022-state-of-the-phish.html

proofpoint.com

An In-Depth Exploration of User Awareness, Vulnerability and Resilience
2022 State of the Phish REPORT

## 2021: THE YEAR OF THE NEW NORMAL?

### A NOTE ON TERMINOLOGY

“Phishing” can mean different things to different people. We use the term in a broad sense to encompass all socially engineered email attacks, regardless of the specific malicious intent (such as directing users to dangerous websites, distributing malware, collecting credentials and so on).

Here are a few of the other terms we use throughout this report and how we define them:

*   **Bulk phishing**: indiscriminate, “commodity” attacks in which the same email is sent to many people within an organization.
*   **Spear phishing**: Targeted attacks sent to selected people within an organization.
*   **Whaling**: Attacks against high-value targets, such as top executives.
*   **Smishing**: Attacks that use mobile text messaging (SMS) as the main communication vector.
*   **Vishing**: Attacks that use phone calls or voice messages to lure targets.

Last year, we titled our introduction “A Year Like No Other.” We could easily have repeated that heading to describe 2021. The year has left many organizations contemplating what “normal” will mean for their workforces going forward.

Along with hybrid and remote work options, organizations are mulling the best ways to keep employees connected and collaborative. Studies show the ongoing pandemic has had a major impact on workers’ mental health. Employees are feeling burned out, emotionally drained and distracted.[^1] Meanwhile, cyber attackers are as adept as ever. And they continue to use tactics and lures that resonate with employees and consumers alike.

In this, our eighth annual State of the Phish report, we explore user vulnerabilities from multiple angles. We look at issues driven by poor cyber hygiene and those that could result from a lack of knowledge and clear communication. We discuss ways organizations can become more attuned to their risks. And we outline opportunities to build and sustain engaging security awareness training initiatives in this challenging climate.

This year’s report includes analysis of data from the following sources:

*   A commissioned survey of **3,500** working adults across seven countries (Australia, France, Germany, Japan, Spain, the United Kingdom and the United States)
*   A commissioned survey of **600** information and IT security professionals across the same seven countries
*   Almost **100 million** simulated phishing attacks sent by our customers over a 12-month period
*   More than **15 million** emails reported by our customers’ end users over that same time period

[^1]: Society for Human Resource Management. “Ongoing Pandemic Takes Toll on Workers’ Mental Health.” August 2021.

## Table of Contents

1.  The 2021 Threat Landscape: a High-Level View . . . . . . . . . . . . . . . . . . . . . . . . 4
    *   Cashing in on COVID . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
    *   Dialing to defraud . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
    *   Making it personal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.  By the Numbers: Targeted Attacks, Ransomware, and Ramifications . . . . . . . . . . . . . 6
    *   Phishing attacks on the rise . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
    *   Other social engineering attacks also up . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
    *   Attackers were more successful in 2021 than in 2020 . . . . . . . . . . . . . . . . . . . . . 8
    *   Successful attacks had wide-ranging impacts. . . . . . . . . . . . . . . . . . . . . . . . . 9
    *   Ransomware: nearly 60% of infected orgs paid up—many more than once . . . . . . . . . . . 10
3.  Working Adults: Cybersecurity Habits and Knowledge Gaps . . . . . . . . . . . . . . . . . . 12
    *   Overview: more devices, more issues. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
    *   Survey says: communicate clearly to train effectively. . . . . . . . . . . . . . . . . . . . . . . . 13
    *   Misconceptions about email . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
    *   Getting personal with employer-issued devices . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
    *   Employee-driven risk: the (even) bigger picture. . . . . . . . . . . . . . . . . . . . . . . . . . . 18
    *   Parting thoughts: risky business in 2021 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
4.  Benchmarking: Failure Rates and Comparison Data . . . . . . . . . . . . . . . . . . . . . . . 23
    *   Failure rates by template type . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23
    *   Industry failure rates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
    *   Department failure rates. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.  Email Reporting and Resilience: Measurements and Goals. . . . . . . . . . . . . . . . . . 29
    *   Calculating resilience . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
    *   Benchmarking: industry resilience factors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
    *   Real-world phishing and reporting accuracy . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
6.  Security Awareness Training: Insights and Opportunities . . . . . . . . . . . . . . . . . . 34
    *   Training tools and frequency of use . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
    *   Orgs ignore too many important topics when training users . . . . . . . . . . . . . . . . . . . 37
7.  Making It Personal: Identifying Vulnerabilities, Gauging Success . . . . . . . . . . . . . . 41
8.  Appendix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
    *   A. Infosec and IT security survey: country-by-country breakdown . . . . . . . . . . . . . . . 45
    *   B. Working adult survey: country-by-country breakdown . . . . . . . . . . . . . . . . . . . . . 53
    *   C. Industry failure rates by simulated phishing template style . . . . . . . . . . . . . . . . . . . . 59

## Section 1

### The 2021 Threat Landscape: a High-Level View

For many, 2021 felt like a year-long case of déjà vu. Pandemic-related concerns remained top-of-mind for employees and organizations—and for many cyber attackers. Human resources and operations teams suddenly had to support remote and hybrid work models. Meanwhile, information security and IT teams had to secure it all.

The first three quarters of the year were busy ones for cyber attackers: we identified nearly 5,500 campaigns[^2] that used one or more recognizable tactics. Our researchers also identified nearly 15 million phishing messages with malware payloads that have been directly linked to later-stage ransomware. Of these malware families, Dridex, The Trick, Emotet, Qbot, and Bazaloader were the most common.

**MALWARE**
*   The Trick
*   BazaLoader
*   SocGholish
*   IcedID
*   Qbot

**RANSOMWARE**
*   WastedLocker
*   Ryuk
*   Egregor
*   Maze
*   Sodinokibi
*   ProLock

![Figure 1: Observed links between first-stage malware families and later-stage malware.](Image description)

[^2]: We define a “campaign” as a group of related threats and activities. Phishing messages within a campaign share common attributes, like the same or similar subject lines, the same sending infrastructure, and the same eventual payload. Further research related to a campaign often reveals further commonalities, such as the threat actor behind it, the type of malware being used, and targeted geographies or industries.

### ABUSING THE BRAND: HOW ATTACKERS PIGGYBACKED BIG TECH NAMES

Microsoft, Google, Zoom and Amazon were among the most abused brands in attack campaigns seen in the first three quarters of 2021. More than 1,100 campaigns abused the Microsoft brand, using a Microsoft-themed lure or product to steal credentials or deliver malware.

Amazon campaigns tended to be high volume: fewer than 100 campaigns accounted for more than 68 million total messages. Much of this volume was attributable to sizeable Japanese-language campaigns, which continued into 2021 after surfacing in 2020. In comparison, about the same number of COVID-themed campaigns totaled around 1.3 million messages.

#### Cashing in on COVID

Not surprisingly, COVID-themed campaigns continued, mimicking the opportunistic attacks that piggybacked pandemic developments throughout 2020. As public concerns ebbed and flowed, so did COVID-themed phishing attacks. We saw a lull through the spring and early summer of 2021. But as the delta variant took center stage, pandemic-themed attacks surged. Beginning in June 2021, we saw an uptick in campaigns that latched onto timely, relevant COVID-related topics, such as vaccine mandates and organizational policies.[^3]

#### Dialing to defraud

Another trend involved telephone-oriented attack delivery (TOAD). These schemes are nothing new—we detect and block tens of thousands of TOAD-related emails every day.[^4] But we saw an uptick in 2021, many of them part of a robust and complex attack chain. Multi-faceted TOAD efforts use a variety of tools, such as:

*   Fraudulent emails
*   Call centers
*   Well-designed websites and mobile apps
*   Remote access software
*   Malware, including downloaders linked to later-stage ransomware delivery

Most TOAD threats require the victim’s active participation. While this approach may seem counter-intuitive from a security standpoint, it works. Perhaps the level of detail and familiar approach work in the attacker’s favor. For many people, calling a support line for help may seem a “safe” option. And many feel more comfortable when an “authority figure” talks them through account updates and refund processes. In addition, many organizations use the same remote access software that attackers exploit in TOAD schemes and other attacks. These activities could bypass security protections designed to block malicious remote access attempts.

#### Making it personal

TOAD threats and other attacks in 2021 targeted both personal and organizational email addresses. Amid the shift to remote work, targeting personal addresses can have a bigger impact on organizations than in years past. As we note later in the report, many people (and their family members!) are accessing personal information and accounts on employer-issued devices.

In general, the 2021 threat landscape reinforced one key point: successful threat protection requires people-centric defense in depth. Your users must be a key part of the security stack. The more informed and equipped they are, the more resilient your organization will be.

[^3]: Selena Larson (Proofpoint). “As Delta Variant Spreads, COVID-19 Themes Make Resurgence in Email Threats.” August 2021.
[^4]: Selena Larson, Sam Scholten and Timothy Kromphardt (Proofpoint). “Caught Beneath the Landline: A 411 on Telephone Oriented Attack Delivery.” November 2021.

## Section 2

### By the Numbers: Targeted Attacks, Ransomware, and Ramifications

This year’s State of the Phish again presents the results of a Proofpoint-designed study of the threat landscape, as seen through the eyes of information security and IT security professionals. Our quantitative surveys, conducted by an outside polling firm, asked 600 participants across Australia, France, German, Japan, Spain, the United Kingdom and the United States about their organizations’ experiences in 2021.

#### Phishing attacks on the rise

According to respondents, the 2021 threat landscape was more active than 2020’s. Reports of phishing attacks were up across the board. Indiscriminate “bulk” phishing attacks rose 12% year over year. And increases in targeted attacks were even higher: reports of spear phishing/whaling and business email compromise (BEC)—which includes payroll redirect and supplier invoicing fraud—were up 20% and 18%, respectively.[^5] Note: the figures represented in Figure 2 include both successful and unsuccessful attacks.

![Figure 2: Volume of Bulk Phishing Attacks, Volume of BEC Attacks, Volume of Spear Phishing and Whaling Attacks, Volume of Email-Based Ransomware Attacks.](Image description)

[^5]: Unless otherwise indicated, survey results represent global averages. You can find country-by-country breakdowns of survey questions and findings in the Appendix.
[^6]: New figures for this year’s report. Note that survey respondents were specifically asked to identify attacks in which a ransomware payload was delivered or intended to be delivered via email.

#### Other social engineering attacks also up

Email remains the top attack vector for cyber criminals. But it’s not the only way bad actors are trying to compromise people and the organizations they work for. Reports of SMS/text phishing (smishing), voice phishing (vishing), and social media-based attacks all increased by more than 20%. And reports of USB drops were up more than 15%.

![Figure 3: Volume of Smishing Attacks, Volume of Social Media Attacks, Volume of Vishing, Volume of Malicious USB Drops.](Image description)

#### Attackers were more successful in 2021 than in 2020

Not every attempted attack succeeds. Millions of malicious emails are blocked by email gateways every day. Advanced email analysis and detection tools are getting better at identifying and stopping impostor emails and the many flavors of email fraud, including BEC. So in some ways, a successful phishing attack is like the proverbial needle in a haystack.

But those successful attacks do real damage. And 2021 was especially painful for the infosec and IT security workers we interviewed.

More than 80% of our survey respondents said their organization suffered a successful email-based phishing attack in 2021. That’s a 46% jump from 2020. Several factors may be at play in the increase, including those in the following sections.

##### Pandemic fatigue

The World Health Organization (WHO) defines pandemic fatigue, in part, as “demotivation to follow recommended protective behaviors, emerging gradually over time.”[^7] WHO’s behavioral focus centers around restrictions and suggestions related to containing infections. But many researchers have cautioned that COVID exhaustion is hurting people in other ways—including job performance.[^8]

Attention spans are short. Many feel displaced and disconnected. Others struggle to remain engaged in work environments that revolve around virtual conferencing and an overload of screen time. The bottom line? People are not at their best. And that’s likely leading to more mistakes in the inbox.

##### Exploiting legitimate services

Cloud collaboration is now a normal part of business. And where people and organizations go, attackers follow.

In the first half of 2021, we saw a marked increase in the abuse of Microsoft and Google infrastructures, which were used to host and send threats across Microsoft 365 (including Office apps, OneDrive, and SharePoint), Microsoft Azure, Google Workspace, and Firebase storage. Because these messages mimic standard business processes, it can be hard for employees to tell the difference between malicious messages and safe ones apart.

This is especially true for employees who are unaware that attackers operate this way. And plenty are uninformed: more than 30% of working adults think that emails with familiar logos are safe, and 35% believe that all files stored in a cloud service like Google Drive are safe. (See more from our survey of working adults in Section 3.)

[^7]: World Health Organization, Regional Office for Europe. “Pandemic fatigue: Reinvigorating the public to prevent COVID-19.” October 2020.
[^8]: Healthline. “COVID Fatigue: How to Cope with Pandemic Burnout.” October 2021.

#### Successful attacks had wide-ranging impacts

Successful attacks don’t happen in a vacuum. Phishing emails can affect organizations in many ways. While some effects are immediate, others aren’t known about or felt until later.

We expanded our view of impacts this year (see Figure 4), so we can’t make year-over-year comparisons in some cases. But we did see an 8% drop in reports of credential compromise, a 6% drop in direct financial loss and a 2% drop in email-driven ransomware infections vs. 2020.

Still, these marginal improvements are little consolation, especially when considering the real-world consequences of each statistic. With the rise in crippling ransomware infections, critical infrastructure attacks and supply chain fraud, cybersecurity threats are more serious than ever.

![Figure 4: Results of Successful Phishing Attacks (Global Average).](Image description)

#### Ransomware: nearly 60% of infected orgs paid up—many more than once

Ransomware made headlines throughout 2021, with government and critical infrastructure sectors particularly hard hit. Security agencies around the globe cautioned organizations of all sizes to strengthen their defenses against ransomware, and with good reason.

Our researchers have been tracking threat actors who have become initial access brokers and, likely, ransomware affiliates, selling the access they’ve gained through first-stage malware to other operators. This scale and the availability of ransomware-as-a-service offerings have both fueled the rise in successful attacks.[^10]

As shown in Figure 5, nearly 70% of organizations dealt with at least one ransomware infection 2021 (a slight increase over 2020). Of those, nearly two-thirds experienced more than three separate infections. And nearly 15% dealt with more than 10 separate infections.[^11]

![Figure 5: Ransomware by the Numbers, Ransomware Infections: What Happened After Payment.](Image description)

[^10]: Proofpoint. “Tips for Developing Your Ransomware Defense Strategy.” November 2021.
[^11]: This includes infections from all sources, including initial payloads and later-stage delivery. The number of separate infections may have resulted from a single intrusion or separate incidents.

## Section 3

### Working Adults: Cybersecurity Habits and Knowledge Gaps

As in the past, this year’s State of the Phish dedicates significant real estate to exploring the greatest source of organizational security risk: people. Our quantitative surveys, conducted by a third party, asked 3,500 working adults across seven countries (Australia, France, German, Japan, Spain, the United Kingdom and the United States) about their cybersecurity perceptions, habits and experiences in 2021.

All survey participants identified as being 18 years or older and employed. Different roles and responsibilities are represented in this group of respondents—a blend that reflects the workforces in many organizations.

We didn’t isolate on “deskbound” workers or those in computer-dominated positions—and that was intentional. We wanted the survey group to represent the makeup of all the people who can influence an organization’s security posture. And make no mistake: every person who works within an organization can have a positive or negative impact on security, no matter what their role is.

#### Overview: more devices, more issues

All survey respondents said they use one or more electronic devices (phone/ smartphone, laptop computer, desktop computer or tablet) for their job. Among these:

*   73% said they have access to at least one employer-issued device
*   74% said they use one or more of their own devices for work-related purposes
*   54% use a personal phone/smartphone and 22% use a personal tablet for work
*   44% said they are in a new remote working environment (either full time or part time) due to the pandemic[^12]
*   83% said they received at least one suspicious communication (either via email, text message, social media, or phone call) in 2021
*   42% said they took a dangerous action (clicked a malicious link, downloaded malware, or exposed their personal data or login credentials) in 2021

We highlight these statistics to illustrate a point that must be considered throughout this section: workers’ personal choices often lead to organizational risk.[^13]

[^12]: To add more context, we also asked our infosec and IT professionals about the impact the pandemic has had on remote work. Some 81% said at least half of their organization’s employees are now working remotely, either full time or part time. Another 14% said employees had worked remotely due to COVID, but were no longer doing so (while just 6% of our working adults said the same).
[^13]: Unless otherwise indicated, survey results represent global averages. You can find country-by-country breakdowns of survey questions and findings in the Appendix.

#### Survey says: communicate clearly to train effectively.

We’ve been assessing working adults’ recognition of common cybersecurity terminology for several years. And while we saw some decent progress last year, this year’s results have rolled that back. One considerable drop was with the term “phishing”: correct answers were down more than 15%, and “I’m not sure” responses were up more than 30%.

Ransomware responses provided the one bright spot, with recognition up about 10% and unsure responses holding steady. With the rise in ransomware attacks around the globe, this improvement comes at a good time.

The overall decline in awareness is another area where pandemic fatigue—and its impact on workers’ engagement and attention spans—could be a factor. It could also reflect a decreased prioritization of cybersecurity awareness and training initiatives during 2021. The pandemic has put many different pressures on organizations, and some may have been forced (due to lack of time, resources or other factors) to deprioritize employee education programs.

Another possibility: perhaps workers are overloaded by the sheer amount of terminology they hear or news stories detailing cyber attacks and warning of dire consequences. People may simply be feeling overwhelmed and confused.

Whatever the case, this year’s results make it clear: it is never safe to assume workers recognize security lingo, no matter how often these terms make headlines. This is especially true if your formal security awareness training sessions—apart from phishing simulations—happen infrequently. Reminders and reinforcement are critical to knowledge and skill development. Employees need to understand the language you speak to fully absorb what you’re saying and, eventually, learn from it.

![Term limits: what users (don’t) know](Image description)

#### Misconceptions about email

Defining cybersecurity threats isn’t always a key to defending against them. So, we wanted to know what workers believe to be true about email and email-based attack methods.

We saw plenty of bright spots. For example, 86% of respondents recognize that they should be cautious of any unsolicited message. And this response level was mostly steady across all regions surveyed. At 81%, French workers were the only group to dip below the 85% mark.

But there’s always room for improvement. We see some areas where quick and clear communication is called for. Employees need immediate clarity on key points like internal email, cloud documents, and the need to take personal responsibility for email security. More than two-thirds of respondents showed a lack of understanding about the capabilities of technical email safeguards on work accounts. That lack of knowledge is a clear and present danger to organizations around the globe.

![Email Survey Results](Image description)

#### Getting personal with employer-issued devices

With 44% of global workers saying they are working remotely either part-time or full-time due to the pandemic, the line between personal life and work life is murkier than ever. But here’s something that is clear: employees’ personal choices can pose a major risk to your data, devices and systems.

As noted earlier in this section, 73% of our survey participants said they have access to at least one employer-issued electronic device. Of those, 77% admitted to using those devices for personal purposes. This is a drop from last year’s 81%, and as shown in Figure 7, we saw a decline in several specific activities.

For example, the number of workers who said they check personal email on employer devices decreased more than 25%. Social media use also decreased, down 15% year over year. But online shopping was up—and the number of people who said they play games on employer devices jumped more than 75%.

![Figure 7: Personal Activities Performed on Work-Issued Devices](Image description)

While workers’ personal use of employer devices decreased overall, their willingness to grant access to friends and family increased. More than 55% of those with employer devices allow others to use them. About 5% admitted that use is unsupervised, meaning they do not monitor or restrict activities on the devices. (A seemingly small number, but a mighty risk.)

Some friends and family activities increased while others decreased. As with workers themselves, playing games showed the largest gain (up nearly 75% over last year). And as shown in Figure 8, several of the activities are up sharply since our 2019 survey.

![Figure 8: Friends and Family Activities Performed on Work-Issued Devices](Image description)

#### Employee-driven risk: the (even) bigger picture

Cybersecurity extends beyond the inbox. It even transcends the professional and personal activities that employees do on their devices. From a risk perspective, how people do things is often more important than what they do.

Think of it in terms of driving a car: there’s some element of risk involved every time. But if someone drives recklessly (or doesn’t know how to drive at all), the risk is much greater to that driver and to others on the road.

Password management is one of these “hows”—and it’s an ongoing struggle. Much of the issue comes down to a balance of convenience and security. Generally, convenience wins. The question is: how are working adults opting for convenience?

We asked survey participants about password management habits for personal and work accounts—and saw strikingly similar answers. This reinforces a point we often stress: cybersecurity skills are life skills, not work skills. They are portable.

This cuts both ways. Skills and behaviors learned at work can be applied at home—but conversely, personal habits and shortcuts are likely to be a factor at work. It’s one reason that ongoing training is so important. It gives people the confidence to recognize and value opportunities to make safer decisions for themselves at work and at home.

![Figure 9: Password Management Habits at Work and at Home](Image description)

External Wi-Fi networks are another ongoing struggle for security teams. And with the significant increase in full-time and part-time remote workers, home Wi-Fi is the elephant in the room.

Nearly all survey respondents said they have a home Wi-Fi network. But most are not taking key security precautions. That means many workers’ home networks are as susceptible as open-access public Wi-Fi.

![Figure 10: Wi-Fi Security Measures on Home Networks](Image description)

Wi-Fi-based attacks assume proximity—which can be difficult to achieve in targeted attacks. Still, it’s clear that many users don’t have a strong grasp of fundamental Wi-Fi practices. And with the increase in remote workers, home networks factor into organizational security more than ever. Small changes can minimize risk. So, if you haven’t advised your workforce on how to close security gaps in home Wi-Fi, we suggest making the effort in 2022.

#### Parting thoughts: risky business in 2021

Like successful phishing attacks, users’ beliefs and behaviors don’t exist in a vacuum. So we asked workers about cybersecurity-related events they experienced in 2021.

We’ve highlighted some key findings here, with more data (including country-by-country breakdowns) in the Appendix. (Note: these are self-identified by survey participants, so actual numbers could be much higher.)

![Figure 11: Cyber Events and Impacts: Key Findings](Image description)

## Section 4

### Benchmarking: Failure Rates and Comparison Data

Our customers actively tested their end users’ response to phishing emails over the course of our 12-month measurement period. They sent nearly 100 million simulated attacks, an increase of more than 50% over 2020. And they saw positive results: the average failure rate held steady at 11%, even with the increase in activity.[^17]

But as we’ve cautioned before, average failure rates don’t provide the level of detail needed to fully assess risk. Nor do they allow organizations to adequately benchmark themselves against others who are running these types of tests.

We dig into our data to provide you with better benchmarking—and to help you identify areas for improvement.

#### Failure rates by template type

Within our phishing simulation tool, customers can select from a variety of themes and lures among three primary template types: link-based, data entry-based and attachment-based.

This year, we saw a slight drop in the use of link-based templates (65% vs. 68%) and an increase in the use of data entry-based templates (26% vs. 23%). Use of attachment-based templates remained the same year over year, with fewer than 10% of tests falling into this category.

This breakdown isn’t necessarily misguided; more attacks use malicious links and lures designed to harvest credentials. But we saw plenty of attacks that used Microsoft Office and PDF attachments, among other file types, to deliver malware in 2021. So the combination of low usage and high failure rates on attachment-based tests is noteworthy. (See the full comparison in Figure 14.)

![Figure 14: Phishing Template Types: Frequency of Use, Phishing Template Types: Average Failure Rates](Image description)

You should assess your organization’s approach to phishing simulations with this insight in mind. Also critical: understanding the types of attacks your organization and your users are facing, as well as how your employees work. If your organization sees a high number of emails with attachments (malicious or not), test and train users about this attack method. If your users widely assume that attachments are safe to interact with, attackers—especially those who use ransomware—could easily exploit that.

In general, simulated phishing programs should include a variety of templates across a variety of themes. We know attackers are adept and adaptive. Your security awareness training efforts should prepare your users to follow suit.

#### Industry failure rates

Many organizations like to compare themselves to others in their industry. This year, we’ve expanded our reporting on industry performance to 25 industries (compared to 20 last year). Our data set per industry also increased over last year (see sidebar). This provides the most robust industry benchmarking we’ve offered to date.

Overall, we saw some great year-over-year improvements on both ends of the spectrum. Last year, the lowest average failure rate was 9%; this year, it’s 8%. And this year’s high mark of 14% bests last year’s 16%.

![Figure 15: Average Failure Rate by Industry](Image description)

#### Department failure rates

People in key roles are targeted for different reasons—and a high position on an org chart is often not a factor. Distribution lists and aliases are also popular targets. These email addresses are frequently published publicly, and they carry the bonus of potentially reaching multiple people with a single send.

Department-level failure rates can help organizations pinpoint teams that are struggling with identifying and avoiding phishing—and begin to address those vulnerabilities.

With 25 departments[^19] now represented (vs. 20 last year), this year’s report provides even more opportunities for benchmarking. And like our industry comparisons, the department data set is more robust than ever.

We saw some exciting improvements in the annual comparison. This year’s lowest average failure (6%) beats last year’s 7% mark. But the best news comes with the highest failure rate: 12% vs. last year’s 17%.

![Figure 16. Average Failure Rate by Department](Image description)

[^19]: Note that our customers self-select department designations. As such, similar designations could mean different things across multiple organizations. For example, “facilities” and “maintenance” might overlap in one organization but have fully separate duties in another.

## Section 5

### Email Reporting and Resilience: Measurements and Goals

#### Email reporting: a critical part of your cyber defenses

Reporting tools are a relative newcomer to the security arsenal. Many organizations have not implemented an easy-to-use, in-client reporting tool like PhishAlarm®.

If we could shout it from the rooftops, we would: email reporting is critical to both defending against cyber attackers and evaluating effectiveness of your security awareness training efforts.

We encourage all of our customers to implement our PhishAlarm in-client reporting button, because it:

*   Allows users to actively participate in email defenses
*   Alerts security teams to suspicious, malicious and nuisance emails that evade filters
*   Promotes a collaborative relationship between users and security teams
*   Enables you to correlate failure rates and reporting rates to gauge resilience
*   Enables you to integrate of reporting and remediation functions, simplifying and accelerating identification and removal of active email-borne threats

#### Calculating resilience

Among customers who use our PhishAlarm button, the average overall reporting rate on simulated attacks in 2021 was 15%, up from 13% last year. The overall average failure rate among these organizations was 10%, down from 11% last year. Both of these are positive signs in general, especially in terms of resilience.

Last year, we introduced the concept of a resilience factor. An organization’s resilience factor is a measurement of simulated phishing reporting rates in comparison to failure rates. The first goal is to achieve a resilience factor greater than 1, which means more people are reporting than failing. Last year, our PhishAlarm customers’ overall resilience factor was 1.2. This year, we saw a 25% improvement:

15% average reporting rate ÷ 10% average failure rate = 1.5 resilience factor

A resilience factor of 1.5 is clearly not ideal. But the year-over-year improvement is a step in the right direction.

The ultimate goal is to increase resilience over time, which happens through improvements in users’ responses to phishing tests. Higher reporting rates are a sign that users are paying more attention to the emails they’re receiving and are taking intentional action to help protect your organization.

While lower failure rates can also be a positive sign,