REPORT
2022 State of the Phish
An In-Depth Exploration of User Awareness,
Vulnerability and Resilience
proofpoint.com

## Table of Contents
- [The 2021 Threat Landscape: a High-Level View](#the-2021-threat-landscape-a-high-level-view)
- [By the Numbers: Targeted Attacks, Ransomware, and Ramifications](#by-the-numbers-targeted-attacks-ransomware-and-ramifications)
- [Working Adults: Cybersecurity Habits and Knowledge Gaps](#working-adults-cybersecurity-habits-and-knowledge-gaps)
- [Benchmarking: Failure Rates and Comparison Data](#benchmarking-failure-rates-and-comparison-data)
- [Email Reporting and Resilience: Measurements and Goals](#email-reporting-and-resilience-measurements-and-goals)
- [Security Awareness Training: Insights and Opportunities](#security-awareness-training-insights-and-opportunities)
- [Making It Personal: Identifying Vulnerabilities, Gauging Success](#making-it-personal-identifying-vulnerabilities-gauging-success)
- [Appendix](#appendix)

2021: THE YEAR OF THE NEW NORMAL?
Last year, we titled our introduction “A Year Like No Other.” We could easily have
repeated that heading to describe 2021. The year has left many organizations
contemplating what “normal” will mean for their workforces going forward.

A NOTE ON TERMINOLOGY
“Phishing” can mean different things to
different people. We use the term in a broad
sense to encompass all socially engineered
email attacks, regardless of the specific
malicious intent (such as directing users to
dangerous websites, distributing malware,
collecting credentials and so on).

Here are a few of the other terms we use
throughout this report and how we define
them:
• Bulk phishing: indiscriminate,
“commodity” attacks in which the same
email is sent to many people within an
organization.
• Spear phishing: Targeted attacks sent to
selected people within an organization.
• Whaling: Attacks against high-value
targets, such as top executives.
• Smishing: Attacks that use mobile text
messaging (SMS) as the main
communication vector.
• Vishing: Attacks that use phone calls or
voice messages to lure targets.

Along with hybrid and remote work options, organizations are mulling the best
ways to keep employees connected and collaborative. Studies show the ongoing
pandemic has had a major impact on workers’ mental health. Employees are
feeling burned out, emotionally drained and distracted.[^1] Meanwhile, cyber
attackers are as adept as ever. And they continue to use tactics and lures that
resonate with employees and consumers alike.

In this, our eighth annual State of the Phish report, we explore user vulnerabilities
from multiple angles. We look at issues driven by poor cyber hygiene and those
that could result from a lack of knowledge and clear communication. We discuss
ways organizations can become more attuned to their risks. And we outline
opportunities to build and sustain engaging security awareness training initiatives
in this challenging climate.

This year’s report includes analysis of data from the following sources:

A commissioned survey of
**3,500** working adults across
seven countries (Australia, France,
Germany, Japan, Spain, the United
Kingdom and the United States)

A commissioned survey of
**600** information and
IT security professionals across the
same seven countries

Almost
**100 million** simulated phishing
attacks sent by our
customers over a 12-month period

More than
**15 million** emails reported by
our customers’ end
users over that same time period

[^1] Society for Human Resource Management. “Ongoing Pandemic Takes Toll on Workers’ Mental Health.” August 2021.

---

## The 2021 Threat Landscape: a High-Level View

For many, 2021 felt like a year-long case of déjà vu. Pandemic-related concerns
remained top-of-mind for employees and organizations—and for many cyber
attackers. Human resources and operations teams suddenly had to support
remote and hybrid work models. Meanwhile, information security and IT teams
had to secure it all.

The first three quarters of the year were busy ones for cyber attackers: we
identified nearly 5,500 campaigns[^2] that used one or more recognizable tactics.
Our researchers also identified nearly 15 million phishing messages with malware
payloads that have been directly linked to later-stage ransomware. Of these
malware families, Dridex, The Trick, Emotet, Qbot, and Bazaloader were the most
common.

| MALWARE | RANSOMWARE |
| :--- | :--- |
| The Trick | WastedLocker |
| Ryuk | BazaLoader |
| Egregor | SocGholish |
| Maze | IcedID |
| Sodinokibi | Qbot |
| ProLock | |

_Figure 1: Observed links between first-stage malware families and later-stage malware._

[^2] We define a “campaign” as a group of related threats and activities. Phishing messages within a campaign share common attributes, like the same or similar subject lines, the same sending infrastructure, and the same eventual payload. Further research related to a campaign often reveals further commonalities, such as the threat actor behind it, the type of malware being used, and targeted geographies or industries.

### Cashing in on COVID

Not surprisingly, COVID-themed campaigns continued, mimicking the
opportunistic attacks that piggybacked pandemic developments throughout
2020. As public concerns ebbed and flowed, so did COVID-themed phishing
attacks. We saw a lull through the spring and early summer of 2021. But as the
delta variant took center stage, pandemic-themed attacks surged. Beginning
in June 2021, we saw an uptick in campaigns that latched onto timely, relevant
COVID-related topics, such as vaccine mandates and organizational policies.[^3]

### ABUSING THE BRAND: HOW ATTACKERS PIGGYBACKED BIG TECH NAMES

Microsoft, Google, Zoom and Amazon were among the most abused brands in attack campaigns seen in the first three quarters of 2021. More than 1,100 campaigns abused the Microsoft brand, using a Microsoft-themed lure or product to steal credentials or deliver malware.

Amazon campaigns tended to be high volume: fewer than 100 campaigns accounted for more than 68 million total messages. Much of this volume was attributable to sizeable Japanese-language campaigns, which continued into 2021 after surfacing in 2020. In comparison, about the same number of COVID-themed campaigns totaled around 1.3 million messages.

### Dialing to defraud

Another trend involved telephone-oriented attack delivery (TOAD). These
schemes are nothing new—we detect and block tens of thousands of TOAD-
related emails every day.[^4] But we saw an uptick in 2021, many of them part of
a robust and complex attack chain. Multi-faceted TOAD efforts use a variety of
tools, such as:

• Fraudulent emails  
• Call centers  
• Well-designed websites and mobile apps  
• Remote access software  
• Malware, including downloaders linked to later-stage ransomware delivery  

Most TOAD threats require the victim’s active participation. While this approach
may seem counter-intuitive from a security standpoint, it works. Perhaps the level
of detail and familiar approach work in the attacker’s favor. For many people,
calling a support line for help may seem a “safe” option. And many feel more
comfortable when an “authority figure” talks them through account updates and
refund processes. In addition, many organizations use the same remote access
software that attackers exploit in TOAD schemes and other attacks. These
activities could bypass security protections designed to block malicious remote
access attempts.

### Making it personal

TOAD threats and other attacks in 2021 targeted both personal and organizational
email addresses. Amid the shift to remote work, targeting personal addresses
can have a bigger impact on organizations than in years past. As we note later
in the report, many people (and their family members!) are accessing personal
information and accounts on employer-issued devices.

In general, the 2021 threat landscape reinforced one key point: successful threat
protection requires people-centric defense in depth. Your users must be a key
part of the security stack. The more informed and equipped they are, the more
resilient your organization will be.

[^3] Selena Larson (Proofpoint). “As Delta Variant Spreads, COVID-19 Themes Make Resurgence in Email Threats.” August 2021.
[^4] Selena Larson, Sam Scholten and Timothy Kromphardt (Proofpoint). “Caught Beneath the Landline: A 411 on Telephone Oriented Attack Delivery.” November 2021.

---

## By the Numbers: Targeted Attacks, Ransomware, and Ramifications

This year’s State of the Phish again presents the results of a Proofpoint-designed
study of the threat landscape, as seen through the eyes of information security and
IT security professionals. Our quantitative surveys, conducted by an outside polling
firm, asked 600 participants across Australia, France, German, Japan, Spain, the
United Kingdom and the United States about their organizations’ experiences in 2021.

### A LOOK BACK AT 2020
- **77%** of organizations saw bulk phishing attacks
- **66%** of organizations dealt with spear phishing attacks.
- **65%** of organizations faced BEC attacks.

### Phishing attacks on the rise

According to respondents, the 2021 threat landscape was more active than
2020’s. Reports of phishing attacks were up across the board. Indiscriminate
“bulk” phishing attacks rose 12% year over year. And increases in targeted
attacks were even higher: reports of spear phishing/whaling and business email
compromise (BEC)—which includes payroll redirect and supplier invoicing
fraud—were up 20% and 18%, respectively.[^5] Note: the figures represented in
Figure 2 include both successful and unsuccessful attacks.

![Volume of Bulk Phishing, BEC, Spear Phishing, and Ransomware Attacks charts]

### COUNTRY SPOTLIGHT
- **91%** of UK survey respondents said their organization faced bulk phishing attacks in 2021.
- **90%** or more of Australian respondents said their organization faced spear phishing, BEC and email-based ransomware attacks in 2021.

_Figure 2_

[^5] Unless otherwise indicated, survey results represent global averages. You can find country-by-country breakdowns of survey questions and findings in the Appendix.
[^6] New figures for this year’s report. Note that survey respondents were specifically asked to identify attacks in which a ransomware payload was delivered or intended to be delivered via email.

### Other social engineering attacks also up

Email remains the top attack vector for cyber criminals. But it’s not the only way
bad actors are trying to compromise people and the organizations they work
for. Reports of SMS/text phishing (smishing), voice phishing (vishing), and social
media-based attacks all increased by more than 20%. And reports of USB drops
were up more than 15%.

### A LOOK BACK AT 2020
- **61%** saw smishing attacks.
- **61%** dealt with social media attacks.
- **54%** faced vishing attacks.
- **54%** reported USB-based attacks.

### COUNTRY SPOTLIGHT
UK and Spanish respondents had very different experiences with non-email-based social engineering attacks in 2021:

**Spanish Organizations Were Least Likely to Face Attacks**
- **<60%** faced smishing and social media attacks.
- **<50%** faced vishing attacks and malicious USB drops.

vs

**UK Organizations Were Most Likely to Face High Volumes**
- **>20%** faced 50+ smishing, social media, and vishing attacks.
- **18%** faced 50+ malicious USB drops.

![Volume of Smishing, Social Media, Vishing, and Malicious USB Drops charts]

_Figure 3_

### Attackers were more successful in 2021 than in 2020

Not every attempted attack succeeds. Millions of malicious emails are blocked
by email gateways every day. Advanced email analysis and detection tools are
getting better at identifying and stopping impostor emails and the many flavors of
email fraud, including BEC. So in some ways, a successful phishing attack is like
the proverbial needle in a haystack.

But those successful attacks do real damage. And 2021 was especially painful for
the infosec and IT security workers we interviewed.

More than 80% of our survey respondents said their organization suffered a
successful email-based phishing attack in 2021. That’s a 46% jump from 2020.
Several factors may be at play in the increase, including those in the following
sections.

### KEY FINDINGS
- **83%** of survey respondents said their organization experienced a successful email-based phishing attack in 2021, up from 57% in 2020.
- **54%** said their organization dealt with more than three successful attacks.
- **11%** experienced 10 or more successful attacks.

#### Pandemic fatigue

The World Health Organization (WHO) defines pandemic fatigue, in part, as
“demotivation to follow recommended protective behaviors, emerging gradually
over time.”[^7] WHO’s behavioral focus centers around restrictions and suggestions
related to containing infections. But many researchers have cautioned that COVID
exhaustion is hurting people in other ways—including job performance.[^8]

Attention spans are short. Many feel displaced and disconnected. Others struggle
to remain engaged in work environments that revolve around virtual conferencing
and an overload of screen time. The bottom line? People are not at their best. And
that’s likely leading to more mistakes in the inbox.

#### Exploiting legitimate services

Cloud collaboration is now a normal part of business. And where people and
organizations go, attackers follow.

In the first half of 2021, we saw a marked increase in the abuse of Microsoft
and Google infrastructures, which were used to host and send threats across
Microsoft 365 (including Office apps, OneDrive, and SharePoint), Microsoft Azure,
Google Workspace, and Firebase storage. Because these messages mimic
standard business processes, it can be hard for employees to tell the difference
between malicious messages and safe ones apart.

This is especially true for employees who are unaware that attackers operate
this way. And plenty are uninformed: more than 30% of working adults think that
emails with familiar logos are safe, and 35% believe that all files stored in a cloud
service like Google Drive are safe. (See more from our survey of working adults in
Section 3.)

[^7] World Health Organization, Regional Office for Europe. “Pandemic fatigue: Reinvigorating the public to prevent COVID-19.” October 2020.
[^8] Healthline. “COVID Fatigue: How to Cope with Pandemic Burnout.” October 2021.

#### Use of trending content

Attackers have taken advantage of trending topics and events for years. But
exploiting of trends seems to have become, well, a trend in itself. And it’s gotten
more intense since the onset of the pandemic. We’ve seen attackers’ lures
morphing to coincide with current public concerns and discourse with greater
speed and strategy than ever.[^9]

Beyond evolving COVID lures in 2021, we saw attackers use lures associated with
popular trends. Here are just a few examples of attack lures:

• Streaming shows, such as “Squid Game”  
• Pop-culture events, such as a Justin Bieber world tour  
• Economic issues, such as U.S. unemployment programs  

We even saw a sophisticated, multi-faceted campaign that included a fake
streaming service, luring victims looking to cancel nonexistent subscriptions.
(The campaign coincided with a wave of people cancelling their pandemic-fueled
streaming video subscriptions.)

Attackers are skilled and savvy. They know the appeal of relevant content. And
when content is more appealing, people are more likely to engage with it.

### COUNTRY SPOTLIGHT
- **92%** of Australian organizations dealt with successful attacks, the highest of any region surveyed (and a 53% year-over-year increase).
- **66%** of Japanese organizations experienced a successful phishing attack in 2021, the lowest of any region surveyed (though 18% higher than 2020).

### KEY FINDINGS
The impacts of successful phishing attacks varied widely in 2021. While Australia and Japan are both part of the Asia-Pacific region, respondents in the two countries reported wildly different experiences.

Australian organizations reported adverse outcomes of successful attacks at rates higher than global averages in all cases but one: just 20% of respondents said their organization experienced a widespread network outage following a phishing attack (vs. 22% globally).

At the other end of the spectrum, many of the differences were significant. For example, 30% reported direct financial loss, nearly twice the global average. And 61% said their organization experienced ransomware as an email payload, 33% higher than the global average.

In contrast, Japanese respondents reported lower-than-average effects in all cases but one: they matched the 27% global average for reports of malware other than ransomware. And their lows were markedly lower in multiple cases: just 3% said their organization experienced direct financial loss (vs. the 17% global average) or financial penalties (vs. the 11% global average). And no Japanese respondents said their organization faced an advanced persistent threat (APT) following a successful attack in 2021.

### Successful attacks had wide-ranging impacts

Successful attacks don’t happen in a vacuum. Phishing emails can affect
organizations in many ways. While some effects are immediate, others aren’t
known about or felt until later.

We expanded our view of impacts this year (see Figure 4), so we can’t make year-
over-year comparisons in some cases. But we did see an 8% drop in reports of
credential compromise, a 6% drop in direct financial loss and a 2% drop in email-
driven ransomware infections vs. 2020.

Still, these marginal improvements are little consolation, especially when
considering the real-world consequences of each statistic. With the rise in
crippling ransomware infections, critical infrastructure attacks and supply chain
fraud, cybersecurity threats are more serious than ever.

[^9] ThreatPost. “Phishers Capitalize on Headlines with Breakneck Speed.” October 2020.

**Results of Successful Phishing Attacks (Global Average)**
- Breach of customer or client data: 54%
- Credential/account compromise: 48%
- Ransomware infection (payload delivered via email): 46%
- Loss of data/intellectual property: 44%
- Malware other than ransomware: 27%
- Reputational damage: 24%
- Widespread network outage/downtime: 22%
- Advanced persistent threat: 18%
- Financial loss/wire transfer or invoice fraud: 17%
- Zero-day exploit: 15%
- Financial penalty/regulatory fine: 11%

_Figure 4_

### Ransomware: nearly 60% of infected orgs paid up—many more than once

Ransomware made headlines throughout 2021, with government and critical
infrastructure sectors particularly hard hit. Security agencies around the
globe cautioned organizations of all sizes to strengthen their defenses against
ransomware, and with good reason.

Our researchers have been tracking threat actors who have become initial access
brokers and, likely, ransomware affiliates, selling the access they’ve gained
through first-stage malware to other operators. This scale and the availability
of ransomware-as-a-service offerings have both fueled the rise in successful
attacks.[^10]

As shown in Figure 5, nearly 70% of organizations dealt with at least one
ransomware infection 2021 (a slight increase over 2020). Of those, nearly two-
thirds experienced more than three separate infections. And nearly 15% dealt with
more than 10 separate infections.[^11]

Once infected, nearly 60% opted to negotiate with attackers (with mixed results),
despite cybersecurity and government agencies warning against the practice. As
always, payment does not guarantee restoration of data (as some of our survey
respondents found out firsthand). In addition, ransomware payments are likely
to fuel the fire, rewarding attackers for their activities and encouraging repeat
behavior.

### KEY FINDING
- **68%** of organizations experienced at least one ransomware infection in 2021 (up from 66% in 2020).

### COUNTRY SPOTLIGHT
- **81%** of French organizations experienced a ransomware infection last year, the highest of any country surveyed. (At 50%, Japanese organizations were least likely to experience an infection.)
- **30%** of Australian organizations that experienced ransomware said they dealt with 10 or more separate infections.
- **82%** of UK organizations that were infected opted to pay the ransom, the highest of any region surveyed (and 41% higher than the global average).
- **42%** of Spanish organizations admitted to paying more than one ransom to regain access to data, the highest of any region surveyed. But at 21%, they were also the most likely to refuse to pay a follow-up ransom after making an initial payment.

![Ransomware by the Numbers and Ransomware Infections: What Happened After Payment charts]

_Figure 5_

[^10] Proofpoint. “Tips for Developing Your Ransomware Defense Strategy.” November 2021.
[^11] This includes infections from all sources, including initial payloads and later-stage delivery. The number of separate infections may have resulted from a single intrusion or separate incidents.

---

## Working Adults: Cybersecurity Habits and Knowledge Gaps

As in the past, this year’s State of the Phish dedicates significant real estate
to exploring the greatest source of organizational security risk: people. Our
quantitative surveys, conducted by a third party, asked 3,500 working adults
across seven countries (Australia, France, German, Japan, Spain, the United
Kingdom and the United States) about their cybersecurity perceptions, habits and
experiences in 2021.

All survey participants identified as being 18 years or older and employed.
Different roles and responsibilities are represented in this group of
respondents—a blend that reflects the workforces in many organizations.

We didn’t isolate on “deskbound” workers or those in computer-dominated
positions—and that was intentional. We wanted the survey group to represent the
makeup of all the people who can influence an organization’s security posture.
And make no mistake: every person who works within an organization can have a
positive or negative impact on security, no matter what their role is.

### Overview: more devices, more issues

All survey respondents said they use one or more electronic devices (phone/
smartphone, laptop computer, desktop computer or tablet) for their job. Among
these:

• **73%** said they have access to at least one employer-issued device  
• **74%** said they use one or more of their own devices for work-related purposes  
• **54%** use a personal phone/smartphone and **22%** use a personal tablet for work  
• **44%** said they are in a new remote working environment (either full time or part time) due to the pandemic[^12]  
• **83%** said they received at least one suspicious communication (either via email, text message, social media, or phone call) in 2021  
• **42%** said they took a dangerous action (clicked a malicious link, downloaded malware, or exposed their personal data or login credentials) in 2021  

We highlight these statistics to illustrate a point that must be considered
throughout this section: workers’ personal choices often lead to
organizational risk.[^13]

### COUNTRY SPOTLIGHT
- **80%** of U.S. workers use one or more of their own mobile devices for work. **64%** said they use personal phones/smartphones, and **30%** use personal tablets. These results were the highest of any region surveyed.
- **32%** of Japanese workers said they do not have access to an employer-issued electronic device (but 100% use one or more electronic devices for work purposes).
- **33%** of U.S. workers and **30%** of Australian workers said they are now working remotely full time due to the pandemic, well more than the 20% global average.
- **30%** of UK workers now have a hybrid approach to working (part-time on site, part time remote).
- **47%** of French workers and **45%** of German workers said the pandemic did not impact their work location, the highest among the regions surveyed.

[^12] To add more context, we also asked our infosec and IT professionals about the impact the pandemic has had on remote work. Some 81% said at least half of their organization’s employees are now working remotely, either full time or part time. Another 14% said employees had worked remotely due to COVID, but were no longer doing so (while just 6% of our working adults said the same).
[^13] Unless otherwise indicated, survey results represent global averages. You can find country-by-country breakdowns of survey questions and findings in the Appendix.

### Survey says: communicate clearly to train effectively

We’ve been assessing working adults’ recognition of common cybersecurity
terminology for several years. And while we saw some decent progress last year,
this year’s results have rolled that back. One considerable drop was with the
term “phishing”: correct answers were down more than 15%, and “I’m not sure”
responses were up more than 30%.

Ransomware responses provided the one bright spot, with recognition up about
10% and unsure responses holding steady. With the rise in ransomware attacks
around the globe, this improvement comes at a good time.

The overall decline in awareness is another area where pandemic fatigue—and
its impact on workers’ engagement and attention spans—could be a factor. It
could also reflect a decreased prioritization of cybersecurity awareness and
training initiatives during 2021. The pandemic has put many different pressures on
organizations, and some may have been forced (due to lack of time, resources or
other factors) to deprioritize employee education programs.

Another possibility: perhaps workers are overloaded by the sheer amount of
terminology they hear or news stories detailing cyber attacks and warning of dire
consequences. People may simply be feeling overwhelmed and confused.

Whatever the case, this year’s results make it clear: it is never safe to assume
workers recognize security lingo, no matter how often these terms make
headlines. This is especially true if your formal security awareness training
sessions—apart from phishing simulations—happen infrequently. Reminders and
reinforcement are critical to knowledge and skill development. Employees need
to understand the language you speak to fully absorb what you’re saying and,
eventually, learn from it.

Our “what is” survey questions offered three multiple choice answers and an “I’m not sure” option. In reviewing results, consider that users who don’t know an answer may pose as much risk as those who answer incorrectly.

### Term limits: what users (don’t) know

- **What is PHISHING?**  
  Correct: 53% | Incorrect: 27% | I Don’t Know: 20%  
  _Correct answers were down from last year’s 63% mark, a 16% year-over-year decrease. UK workers were again most likely to answer correctly—but this year’s 62% fell short of last year’s 69%._

- **What is RANSOMWARE?**  
  Correct: 36% | Incorrect: 33% | I Don’t Know: 31%  
  _This is the only term that saw an increase in recognition, with correct answers rising from 33% and incorrect responses falling from 36%. (Unsure responses held steady at 31%.) At 49% correct, Australian workers performed well above the global average. French and German workers were least likely to answer correctly (at 27% and 26%, respectively)._

- **What is MALWARE?**  
  Correct: 63% | Incorrect: 20% | I Don’t Know: 17%  
  _Like last year, Spanish workers led their global counterparts in recognition of this term. But this year’s 73% was lower than last year’s 75% (and well off the 80% high mark from two years ago). At 52%, Japanese workers were least likely to answer this correctly, and another 38% were unsure of how to answer._

- **What is SMISHING?**  
  Correct: 23% | Incorrect: 32% | I Don’t Know: 45%  
  _Global recognition of this term was down from 31% last year, a 26% year-over-year drop. Japanese workers again struggled with this term. Just 17% answered correctly (down from 19% last year), and 56% were unsure of how to answer (the same as last year)._

- **What is VISHING?**  
  Correct: 24% | Incorrect: 31% | I Don’t Know: 45%  
  _30% of global respondents answered this question correctly last year, representing a 20% year-over-year decrease in recognition. French workers went from first to worst in recognition of this term. Last year, they led all regions at 54% correct. This year, just 17% answered correctly (a decrease of nearly 70%)._

### Misconceptions about email

Defining cybersecurity threats isn’t always a key to defending against them. So,
we wanted to know what workers believe to be true about email and email-based
attack methods.

We saw plenty of bright spots. For example, 86% of respondents recognize that
they should be cautious of any unsolicited message. And this response level was
mostly steady across all regions surveyed. At 81%, French workers were the only
group to dip below the 85% mark.

But there’s always room for improvement. We see some areas where quick
and clear communication is called for. Employees need immediate clarity on
key points like internal email, cloud documents, and the need to take personal
responsibility for email security. More than two-thirds of respondents showed
a lack of understanding about the capabilities of technical email safeguards
on work accounts. That lack of knowledge is a clear and present danger to
organizations around the globe.

### COUNTRY SPOTLIGHT
**Top Performers**
- **85%** of German workers know that email attachments can be dangerous.
- **82%** of UK workers know that an email’s sender details can be disguised.
- **63%** of Japanese workers know that familiar logos in emails don’t equate to safety.
- **49%** of Japanese workers know that unsafe contacts may email them multiple times.

**Bottom Performers**
- **59%** of Spanish workers think that all internal emails are safe.
- **57%** of Spanish workers think their organization will automatically block all malicious email (and 49% believe their personal email provider will do the same).
- **46%** of U.S. workers think that all files stored in the cloud are safe.
- **42%** of U.S. workers believe all emails with familiar logos are safe.

**Email Survey Results[^14]**
- **81%** know that email attachments can be malicious.
- **77%** know that an email can appear to come from someone other than the true sender.
- **52%** know that familiar logos and contact information aren’t an automatic indication of safety.
- **38%** know that their personal email provider cannot block all dangerous email.
- **37%** know that files stored in the cloud can be malicious.
- **37%** know that unsafe contacts may email them multiple times.
- **36%** know that even internal emails could be dangerous.
- **30%** know that their organization’s security tools cannot block all dangerous email.

_Figure 6_

[^14] We asked similar questions in last year’s survey, but in a different format. We believe this year’s format offered more clarity and more accurate findings. Full details and results for these questions are in the Appendix.

### Getting personal with employer-issued devices

With 44% of global workers saying they are working remotely either part-time
or full-time due to the pandemic, the line between personal life and work life
is murkier than ever. But here’s something that is clear: employees’ personal
choices can pose a major risk to your data, devices and systems.

As noted earlier in this section, 73% of our survey participants said they have
access to at least one employer-issued electronic device. Of those, 77% admitted
to using those devices for personal purposes. This is a drop from last year’s 81%,
and as shown in Figure 7, we saw a decline in several specific activities.

For example, the number of workers who said they check personal email on
employer devices decreased more than 25%. Social media use also decreased,
down 15% year over year. But online shopping was up—and the number of
people who said they play games on employer devices jumped more than 75%.

### KEY FINDING
- **56%** of workers who have an employer-issued device grant access to friends and/or family members (up from 52% last year).

### COUNTRY SPOTLIGHT
- **69%** of Spanish workers allow friends or family members to access their employer-issued devices. This is nearly 25% more than the global average and a marked increase from last year (45%).
- **48%** of Australian workers grant others access to their employer-issued devices, the least of any region surveyed.

![Personal Activities Performed on Work-Issued Devices chart]

_Figure 7_

![Friends and Family Activities Performed on Work-Issued Devices chart]

_Figure 8_

### Employee-driven risk: the (even) bigger picture

Cybersecurity extends beyond the inbox. It even transcends the professional and
personal activities that employees do on their devices. From a risk perspective,
how people do things is often more important than what they do.

Think of it in terms of driving a car: there’s some element of risk involved every
time. But if someone drives recklessly (or doesn’t know how to drive at all), the risk
is much greater to that driver and to others on the road.

Password management is one of these “hows”—and it’s an ongoing struggle.
Much of the issue comes down to a balance of convenience and security.
Generally, convenience wins. The question is: how are working adults opting for
convenience?

We asked survey participants about password management habits for personal
and work accounts—and saw strikingly similar answers. This reinforces a point we
often stress: cybersecurity skills are life skills, not work skills. They are portable.

This cuts both ways. Skills and behaviors learned at work can be applied at
home—but conversely, personal habits and shortcuts are likely to be a factor at
work. It’s one reason that ongoing training is so important. It gives people the
confidence to recognize and value opportunities to make safer decisions for
themselves at work and at home.

### COUNTRY SPOTLIGHT
- **33%** of U.S. workers save their login information in their web browser.
- **27%** of UK workers use a password manager.
- **30%** of German workers manually enter a unique password for each account.
- **16%** of Japanese and Spanish users rotate between one and four passwords for their accounts.

![Password Management Habits at Work and at Home chart]

_Figure 9_

External Wi-Fi networks are another ongoing struggle for security teams. And with
the significant increase in full-time and part-time remote workers, home Wi-Fi is
the elephant in the room.

Nearly all survey respondents said they have a home Wi-Fi network. But most are
not taking key security precautions. That means many workers’ home networks
are as susceptible as open-access public Wi-Fi.

### KEY FINDING
Among those with home Wi-Fi networks, **85%** did not complete all the security measures we asked them about (11% said they don’t do any of them). Of the 85%, 62% said they haven’t taken some or all of the precautions because they aren’t concerned about the security of their home Wi-Fi network. Another 34% said they haven’t adjusted their security settings because they don’t know how to.

Of the 4% who offered another (write-in) reason, we saw some common sentiments:

• Unnecessary/don’t need to  
• Default settings/passwords are already complex/secure  
• Another person (spouse/partner, landlord) handles it  
• Too inconvenient/don’t want to reconnect devices  
• Never thought about it  

**Wi-Fi Security Measures on Home Networks**
- **97%** said they have a home Wi-Fi network
- **60%** password-protect their home Wi-Fi network
- **26%** changed the default name of their network
- **26%** changed their network’s default Wi-Fi password (network security key)
- **22%** changed their router’s default password
- **18%** checked for updates to router software
- **11%** took none of these security measures

_Figure 10_

Wi-Fi-based attacks assume proximity—which can be difficult to achieve in
targeted attacks. Still, it’s clear that many users don’t have a strong grasp of
fundamental Wi-Fi practices. And with the increase in remote workers, home
networks factor into organizational security more than ever. Small changes can
minimize risk. So, if you haven’t advised your workforce on how to close security
gaps in home Wi-Fi, we suggest making the effort in 2022.

### Parting thoughts: risky business in 2021

Like successful phishing attacks, users’ beliefs and behaviors don’t exist
in a vacuum. So we asked workers about cybersecurity-related events they
experienced in 2021.

We’ve highlighted some key findings here, with more data (including country-by-
country breakdowns) in the Appendix. (Note: these are self-identified by survey
participants, so actual numbers could be much higher.)

### COUNTRY SPOTLIGHT
- **91%** of Spanish workers received at least one suspicious communication in 2021. 49% saw a suspicious email attachment, and 20% got a suspicious message in a work-related messaging app.
- **83%** of U.S. workers admitted to taking a risky action in 2021. 26% clicked an email link that led to a suspicious website, and 17% accidentally compromised their credentials.
- **52%** of U.S. workers experienced a cyberattack or fraud. 19% were victims of identity theft, and 17% paid a ransom to regain access to a personal device or data.

**Cyber Events and Impacts: Key Findings**
- **55%** received at least one suspicious communication in 2021
  - **39%** received an email that contained a suspicious attachment
  - **38%** received a suspicious text message
  - **37%** received a suspicious phone call/voicemail
  - **16%** received a suspicious message in a work-related messaging app
  - **15%** received an email impersonating their organization
- **42%** took a risky action
  - **19%** clicked an email link that led to a suspicious website
  - **14%** clicked a link in a direct message that downloaded malware
  - **13%** accidentally downloaded malware from a malicious email or website
  - **12%** gave personal information to a scam artist/impostor
  - **11%** accidentally compromised account credentials
- **37%** experienced a cyberattack or fraud
  - **14%** said one or more of their social media accounts was compromised
  - **12%** said someone duplicated their social media account and attempted to impersonate them
  - **12%** lost money because of a fraud committed against them
  - **11%** were victims of identity theft
  - **10%** paid a ransom to regain access to a personal device or data

_Figure 11_

### Spotlight: Security Culture

There’s a lot of talk about security culture in the workplace today. And that’s
a great thing. A strong security culture pays dividends. But getting there
isn’t easy.

The reality is that “culture”—like “maturity”—is nebulous. Many things factor
into it, and each organization is likely to interpret the term differently. And
measuring gains (or losses) in cultural “strength” can be difficult.

Still, some key dimensions to culture can (and should) be assessed on an
ongoing basis. In particular, you should gauge employee perception of:

• Your organization’s commitment to cybersecurity  
• The role they should play in protecting your organization  
• Their confidence level in identifying, reporting or acknowledging security incidents  

Assessing these factors can reveal obstacles to achieving a strong security
culture. In part, it can show where disconnects between perceptions of
security teams, executive teams and employees exist. This is something we
saw in asking similar questions to our two different survey audiences.

### KEY FINDINGS
- **85%** of infosec and IT survey respondents said they had a positive perception of their organization’s security culture. 14% indicated a neutral stance, and just 1% had a negative perception.
- **52%** of working adults are confident or extremely confident that, should they have a cybersecurity-related issue with one of their work devices, their IT team could identify and address the issue without their involvement.

### COUNTRY SPOTLIGHT
- **<45%** of Japanese infosec and IT professionals said cybersecurity is a high priority for their organization.
- **>50%** of Spanish and German working adults said cybersecurity is a high priority for themselves and their organization.

**Level of Cybersecurity Priority Within the Organization[^15]**
- **High priority**: 65% (Infosec/IT) vs. 42% (Working adults)
- **Priority**: 28% (Infosec/IT) vs. 23% (Working adults)
- **Somewhat a priority**: 5% (Infosec/IT) vs. 18% (Working adults)
- **Low priority**: 2% (Infosec/IT) vs. 7% (Working adults)
- **Not a priority**: 0% (Infosec/IT) vs. 3% (Working adults)

_Figure 12_

[^15] Some 7% of working adults said they were unsure of how their organization prioritizes cybersecurity.

**Level of Cybersecurity Priority for Employees[^16]**
- **High priority**: 50% (Infosec/IT) vs. 40% (Working adults)
- **Priority**: 39% (Infosec/IT) vs. 29% (Working adults)
- **Somewhat a priority**: 8% (Infosec/IT) vs. 19% (Working adults)
- **Low priority**: 2% (Infosec/IT) vs. 6% (Working adults)
- **Not a priority**: <1% (Infosec/IT) vs. 2% (Working adults)

_Figure 13_

[^16] For this question, infosec and IT professionals were asked their perception of cybersecurity priority for the average employee. Working adults were asked about the priority they personally place on cybersecurity. Note that 4% of working adults were not sure how to classify their personal commitment to cybersecurity.

That 35% of infosec and IT professionals said cybersecurity is not a high
priority for their organization is borderline alarming. But we see other key
disconnects:

• Infosec and IT professionals have a more positive view of employees’
commitment to cybersecurity than employees themselves do (89% priority/
high priority vs. 69%)  
• Working adults are more likely to say cybersecurity is a priority or a
high priority for themselves than they are to say the same about their
organization (69% vs. 65%)  
• 10% of working adults believe cybersecurity is a low priority or not a priority
for their organization  

And among workers who indicated that cybersecurity is not a priority or is a
low priority for them, we see key misconceptions:

• 32% said that since they’ve never experienced any issues, they don’t need
to prioritize cybersecurity  
• 27% believe their job is not high-level enough to be a target of cyber
attackers, so they don’t need to worry about cybersecurity  
• 22% feel they don’t interact with devices often enough to be worried  
• 19% believe their organization or IT team will take care of any security
needs they have or mistakes they make  

These survey results cover many organizations, industries and regions. But
they illustrate the value of understanding where the disconnects may be
within your organization. Once you identify issues, you can begin to address
them through clearer communication and targeted education.

---

## Benchmarking: Failure Rates and Comparison Data

Our customers actively tested their end users’ response to phishing emails over
the course of our 12-month measurement period. They sent nearly 100 million
simulated attacks, an increase of more than 50% over 2020. And they saw positive
results: the average failure rate held steady at 11%, even with the increase in
activity.[^17]

But as we’ve cautioned before, average failure rates don’t provide the level of
detail needed to fully assess risk. Nor do they allow organizations to adequately
benchmark themselves against others who are running these types of tests.

We dig into our data to provide you with better benchmarking—and to help you
identify areas for improvement.

### KEY FINDINGS
- **11%** average failure rate on phishing tests.
- **33%** average view rate of simulated attacks.

### FUN FACT
Over the past 10 years, our customers have sent nearly 275M simulated phishing emails to their users.

[^17] We calculate average failure rates at the organizational level rather than the user level, giving equal weight to each organization’s average failure rate rather than equally weighting each user’s failure rate. This approach helps to eliminate the sway of large organizations and high-volume programs, providing a more balanced view of failure data.

### Failure rates by template type

Within our phishing simulation tool, customers can select from a variety of themes
and lures among three primary template types: link-based, data entry-based and
attachment-based.

This year, we saw a slight drop in the use of link-based templates (65% vs. 68%)
and an increase in the use of data entry-based templates (26% vs. 23%). Use of
attachment-based templates remained the same year over year, with fewer than
10% of tests falling into this category.

This breakdown isn’t necessarily misguided; more attacks use malicious links
and lures designed to harvest credentials. But we saw plenty of attacks that used
Microsoft Office and PDF attachments, among other file types, to deliver malware
in 2021. So the combination of low usage and high failure rates on attachment-
based tests is noteworthy. (See the full comparison in Figure 14.)

**Phishing Template Types: Frequency of Use**
- Link: 65%
- Data Entry: 26%
- Attachment: 9%

**Phishing Template Types: Average Failure Rates**
- Link: 11%
- Data Entry: 4%
- Attachment: 20%

_“Failed” data-entry tests refer to cases in which users submitted data after clicking a link in the simulated attack. Overall, the average click rate in data entry-based tests was 12% and the average failure rate was 4%._

_Figure 14_

You should assess your organization’s approach to phishing simulations with
this insight in mind. Also critical: understanding the types of attacks your
organization and your users are facing, as well as how your employees work. If
your organization sees a high number of emails with attachments (malicious or
not), test and train users about this attack method. If your users widely assume
that attachments are safe to interact with, attackers—especially those who use
ransomware—could easily exploit that.

In general, simulated phishing programs should include a variety of templates
across a variety of themes. We know attackers are adept and adaptive. Your
security awareness training efforts should prepare your users to follow suit.

### Industry failure rates

The industries that ran the most phishing tests in 2021 were healthcare, financial
services, energy/utilities, manufacturing and technology.

Overall, we saw some great year-over-year improvements on both ends of the
spectrum. Last year, the lowest average failure rate was 9%; this year, it’s 8%.
And this year’s high mark of 14% bests last year’s 16%.

### KEY FINDINGS
Many organizations like to compare themselves to others in their industry. This year, we’ve expanded our reporting on industry performance to 25 industries (compared to 20 last year). Our data set per industry also increased over last year (see sidebar). This provides the most robust industry benchmarking we’ve offered to date.

**Average Failure Rate by Industry[^18]**
- Automotive: 8%
- Electronics: 8%
- Engineering: 8%
- Entertainment/Media: 9%
- Financial Services: 9%
- Education: 10%
- Energy/Utilities: 10%
- Healthcare: 10%
- Hospitality/Leisure: 10%
- Manufacturing: 10%
- Food & Beverage: 11%
- Government: 11%
- Insurance: 11%
- Legal: 11%
- Retail: 11%
- Transportation: 11%
- Agriculture: 12%
- Construction: 12%
- Mining: 12%
- Real Estate: 12%
- Technology: 12%
- Telecommunications: 12%
- Aerospace: 12%
- Business Services: 12%
- Consulting: 14%

_Each industry represented in our failure rate comparison includes data from at least 20 organizations and at least 300,000 simulated phishing attacks (vs. 15 orgs and 150,000 phishing tests last year)._

_Figure 15_

[^18] Look for industry failure rates by template type in the Appendix.

### Department failure rates

People in key roles are targeted for different reasons—and a high position on
an org chart is often not a factor. Distribution lists and aliases are also popular
targets. These email addresses are frequently published publicly, and they carry
the bonus of potentially reaching multiple people with a single send.

Department-level failure rates can help organizations pinpoint teams that are
struggling with identifying and avoiding phishing—and begin to address those
vulnerabilities.

With 25 departments[^19] now represented (vs. 20 last year), this year’s report
provides even more opportunities for benchmarking. And like our industry
comparisons, the department data set is more robust than ever.

### KEY FINDINGS
- **Facilities** was last year’s worst-performing department, tallying a 17% average failure rate. This year, they sit at a 9% average failure rate, a nearly 50% year-over-year improvement.
- Even two of this year’s worst-performing departments—**quality** and **maintenance**, each at 12%—are ahead of their average failure rates from last year (14% and 15%, respectively).
- There is one notable bit of bad news: **purchasing**, last year’s best performer with a 7% average failure rate, dropped to join the lowest performers at 12%.

We saw some exciting improvements in the annual comparison. This year’s lowest
average failure (6%) beats last year’s 7% mark. But the best news comes with the
highest failure rate: 12% vs. last year’s 17%.

**Average Failure Rate by Department**
- Audit: 6%
- Information Technology: 6%
- Customer Service: 8%
- Logistics: 8%
- Security: 8%
- Administrative Services: 9%
- Communications: 9%
- Facilities: 9%
- Finance: 9%
- Legal: 9%
- Accounting: 10%
- Human Resources: 10%
- Management: 10%
- Marketing: 10%
- Research and Development: 10%
- Sales: 10%
- Supply Chain: 10%
- Warehouse: 10%
- Engineering: 11%
- Operations: 11%
- Production: 11%
- Project Management: 11%
- Maintenance: 12%
- Purchasing: 12%
- Quality: 12%

_Department designations represented in our failure rate comparison were used by at least 85 organizations and include data on a minimum of 2,500 users (vs. 40 orgs and 1,500 users last year)._

_Figure 16_

[^19] Note that our customers self-select department designations. As such, similar designations could mean different things across multiple organizations. For example, “facilities” and “maintenance” might overlap in one organization but have fully separate duties in another.

### Spotlight: Template Themes

As we noted earlier, our customers have access to a frequently updated
template library. They can test their users on a wide variety of themes,
topics, and tactics, including some of the latest threats our researchers
spot in the wild.

On average, our customers sent out nine phishing campaigns over the
course of our 12-month measurement period. That’s an increase from
the eight-campaign average we saw last year. This is a positive trend; we
recommend testing users at least every four to six weeks (and, ideally, at
least once a month).

In 2021, organizations heavily favored “corporate”-themed phishing tests;
more than 50% of templates used featured this theme. The emphasis was not
misplaced. Many attackers used process and policy lures in their campaigns.
We also saw a surge in attacks that abused cloud services that many
organizations rely on for communication and collaboration.

Here are the top 10 most-used templates last year and 10 well-used templates
that proved trickiest for recipients (resulting in users taking the bait). This
year, we’ve also included the average failure rate for each of the templates.

The most-used templates highlighted were sent to between 73,000 and 1.5M users. The most “successful” templates highlighted were sent to a minimum of 10,000 users (and as many as 52,000 users).

Some templates used in smaller-scale campaigns (sent to fewer than 1,000 users) had significantly higher failure rates. This includes a Tax Refund Notification template and a New Company Policy template, each of which topped a 70% failure rate.

| Most-Used Templates | | Trickiest Templates | |
| :--- | :--- | :--- | :--- |
| 1. Voicemail from unknown caller | 18% | 1. Dress code update | 30% |
| 2. Parcel arrival notice | 15% | 2. Local holiday giveaways and samples | 28% |
| 3. Email password change: Urgent attention | 10% | 3. Bonus review | 26% |
| 4. Deactivation of old OneDrive account | 8% | 4. Denny’s food order | 26% |
| 5. Important social media policy change | 7% | 5. Missed Zoom meeting | 24% |
| 6. Urgent Microsoft 2FA activation | 7% | 6. Updated EMR policy (healthcare) | 24% |
| 7. Microsoft Teams invitation | 6% | 7. Updated vacation policy | 24% |
| 8. O365 password expiration notice | 6% | 8. Urgent message re: dress code | 23% |
| 9. Important information about queued email | 4% | 9. Code of conduct: reported incident | 23% |
| 10. Unusual account sign-in activity | 3% | 10. Updated payroll timetable | 22% |

_Table 1_ | _Table 2_

A majority of the most-used templates revolve around internal accounts and tools—and many of those have very low failure rates. This is why it pays to mix things up when testing users. Though most of the trickiest templates also mimicked internal communications, they used topics that are likely to draw an immediate and emotional response from recipients (like the two separate dress code templates).

On average, our customers used two different templates within each

---

That emotional impact is reflected in the failure rates. The lowest among the
simulated phishing campaign in
most “successful” templates is still 20% higher than the highest failure rate
2021. Using more than one template
among the most-used templates (and more than seven times higher than the
in a single campaign can help
lowest failure rate).
organizations avoid the so-called
“prairie dog effect,” which happens Granted, these types of “triggering” tests can be a hard sell with reviewers
when one employee spots a test (or and approvers. And they may not be a good fit for every organization’s
fails a test) and warns others about culture. Regardless, the fact remains: attackers are not at all concerned about
the email. offending, frightening or tricking your employees. At the very least, users
must be made aware that threat actors are freely using these types of lures
and tactics, even if you don’t use them in simulated phishing emails.
28

2022 STATE OF THE PHISH \ REPORT
Section 5
Email Reporting and Resilience:
AMONG ORGANIZATIONS THAT
USE OUR PHISHALARM EMAIL
REPORTING TOOL Measurements and Goals
15%
overall average reporting rate
Email reporting: a critical part of your cyber defenses
(up from 13% last year).
10% Reporting tools are a relative newcomer to the security arsenal. Many organizations have
not implemented an easy-to-use, in-client reporting tool like PhishAlarm®.
overall average failure rate If we could shout it from the rooftops, we would: email reporting is critical to both
(down from 11% last year). defending against cyber attackers and evaluating effectiveness of your security
awareness training efforts.
1.5
We encourage all of our customers to implement our PhishAlarm in-client reporting
overall average resilience factor button, because it:
(up from 1.2 last year).
• Allows users to actively participate in email defenses
• Alerts security teams to suspicious, malicious and nuisance emails that evade filters
• Promotes a collaborative relationship between users and security teams
• Enables you to correlate failure rates and reporting rates to gauge resilience
• Enables you to integrate of reporting and remediation functions, simplifying and
accelerating identification and removal of active email-borne threats
Calculating resilience
AVERAGE REPORTING RATE BY
TEMPLATE TYPE
Among customers who use our PhishAlarm button, the average overall reporting
18 rate on simulated attacks in 2021 was 15%, up from 13% last year. The overall
%
average failure rate among these organizations was 10%, down from 11% last
year. Both of these are positive signs in general, especially in terms of resilience.
for attachment campaigns.
Last year, we introduced the concept of a resilience factor. An organization’s
17
% resilience factor is a measurement of simulated phishing reporting rates in
comparison to failure rates. The first goal is to achieve a resilience factor greater
for data entry campaigns.
than 1, which means more people are reporting than failing. Last year, our
PhishAlarm customers’ overall resilience factor was 1.2. This year, we saw a
16
% 25% improvement:
for link-based campaigns.
15 10 1.5
% %
average reporting rate ÷ average failure rate = resilience factor
29

2022 STATE OF THE PHISH \ REPORT
A resilience factor of 1.5 is clearly not ideal. But the year-over-year improvement is
a step in the right direction.
The ultimate goal is to increase resilience over time, which happens through
improvements in users’ responses to phishing tests. Higher reporting rates are a
sign that users are paying more attention to the emails they’re receiving and are
taking intentional action to help protect your organization.
While lower failure rates can also be a positive sign, not clicking a simulated
TIP phishing email is not the same thing as actively rejecting it. Phishing tests might
be ignored or avoided for any number of reasons, not just because users believe
If your organization’s failure
them to be suspicious.
rate is higher than your
reporting rate, calculate your We reiterate our advice from the past couple of years: work toward the stretch
resilience factor by inverting goals of an overall reporting rate of 70% and an overall failure rate of 5%—an
the equation and adding a overall resilience factor of 14. This would put you in the very positive position
negative sign to the result.
of having a user base that’s 14 times more likely to report a phishing test than
engage with one. That attention to detail will pay off when real-world phishing
attacks evade your perimeter defenses.
It bears repeating that we consider a 70/5 ratio to be a stretch goal. It’s not
something that will happen overnight.
Still, we regularly see customers’ campaigns meeting or surpassing these marks.
So, it’s achievable. Yes, it’s more easily achieved on individual campaigns. But
we see organizations sustaining even higher resilience factors across multiple
campaigns. So it’s also repeatable.
As with all security awareness training initiatives, you’ll need to be patient
and allow for improvements to come. To make gains, email reporting must
carry weight within your organization—from both a training and measurement
perspective.
Consider these key actions:
• Coach users about reporting. It’s not enough to simply give them access to a
reporting tool. They need to know how to find it and how to use it.
• Communicate about the positive impact user-reported emails can make
within your organization. A reporting tool empowers users to help stop cyber
attacks. That is compelling.
• Train users about when to report. And allow time to grow their confidence in
their ability to identify and take action on suspicious messages.
• If necessary, shift organizational focus away from failure rates as the
ultimate indicator of phishing awareness. Become an internal advocate for
reporting and emphasize reporting rates in metrics that are socialized internally.
• Share successes with users, too. Highlight real-world phishing attempts
reported by employees. These stories both reinforce the positive impacts of
reporting and remind employees that they can make a difference when they
apply what they learn in your security awareness training program.
30

2022 STATE OF THE PHISH  \  REPORT
Benchmarking: industry resilience factors
As noted earlier, we know organizations are eager to level-set their performance
KEY FINDINGS against more granular measurements than overall failure and reporting rates. Our
industry-based reporting and resilience analysis supports those efforts. As with
Last year’s single highest reporting
our earlier set of industry comparisons, we’ve expanded our coverage to include
rate—20%, achieved by the financial
25 industries this year.
services industry—was matched or
beaten by nine industries this year
In Table 3, we present each industry’s average reporting rate, failure rate, and
(including financial services, which   resilience factor. You’ll note that the failure rates in this section may vary slightly
reached a 23% reporting rate).
from those in Figure 15. The average failure rates seen here are based on
customers who use both our phishing simulations and our PhishAlarm button, a
Last year, six industries had a negative
smaller subset of the data used earlier.
resilience factor (more users failed than
reported phishing tests). This year, just
Industries are ranked in order of reporting rate, highest to lowest.
one—education—was in negative territory.
But even that industry saw an improvement
over 2020 (-1.3 vs. -2.0). Industry Reporting, Failure and Resilience Data
Just four industries had a reporting rate     Reporting   Failure   Resilience
| Industry | Rate | Rate | Factor |
| -------- | ---- | ---- | ------ |
of 10% or lower this year, compared to
| Aerospace | 26% | 6%  | 4.3 |
| --------- | --- | --- | --- |
nine in 2020.
| Electronics         | 26% | 8%  | 3.3  |
| ------------------- | --- | --- | ---- |
| Energy/Utilities    | 24% | 7%  | 3.4  |
| Financial Services  | 23% | 6%  | 3.8  |
| Legal               | 23% | 6%  | 3.8  |
| Agriculture         | 22% | 7%  | 3.1  |
| Insurance           | 21% | 8%  | 2.6  |
| Consulting          | 20% | 10% | 2.0  |
| Engineering         | 20% | 7%  | 2.9  |
| Construction        | 18% | 8%  | 2.2  |
| Real Estate         | 17% | 11% | 1.5  |
| Automotive          | 16% | 10% | 1.6  |
| Manufacturing       | 16% | 7%  | 2.3  |
| Government          | 13% | 7%  | 1.9  |
| Mining              | 13% | 6%  | 2.2  |
| Business Services   | 12% | 12% | 1.0  |
| Entertainment/Media | 12% | 5%  | 2.4  |
| Retail              | 12% | 8%  | 1.5  |
| Telecommunications  | 12% | 9%  | 1.3  |
| Healthcare          | 11% | 7%  | 1.6  |
| Technology          | 11% | 7%  | 1.6  |
| Food & Beverage     | 10% | 8%  | 1.3  |
| Transportation      | 8%  | 6%  | 1.3  |
| Education           | 6%  | 8%  | -1.3 |
| Hospitality/Leisure | 5%  | 4%  | 1.3  |
Table 3
31

2022 STATE OF THE PHISH \ REPORT
Real-world phishing and reporting accuracy
Worried that user-reported emails will
overwhelm your remediation team?
Over our one-year measurement period, we saw the immense value in allowing
Solutions like our Closed-Loop Email
users to actively participate in email defenses. Our customers’ employees spotted
Analysis and Response (CLEAR) can
and reported many active threats, including emails that contained malware
Wheolprr isetdre tahmatl inues emr-arenpaogretmede netm oafi lasb wusilel
affiliated with nation-state and financial APTs. They alerted infosec teams to:
omvaeirlbwohxeelms, uyosiunrg r eamuteodmiaattiioonn taenadm a?d vanced
Semolauitli osnesc ulirkiety o fuera tCulroesse tdo- Lcouot po pEemraatiilo nal • More than 350,000 credential phishing emails
Aovnearlyhseiasd a. nd Response (CLEAR) can
• Nearly 40,000 emails with malware payloads like Trojans, downloaders,
help streamline management of abuse
stealers, keyloggers and ransomware
mailboxes, using automation and
advanced email security features to cut • More than 20,000 malicious spam emails
operational overhead. • More than 8,500 emails associated with botnets or spambots
• More than 8,000 attacks using remote access or banking Trojans
• More than 6,000 attacks containing downloaders
This year, we’ve also analyzed reporting accuracy data. This is calculated for
PhishAlarm customers who also use PhishAlarm Analyzer. Email reporting is even
more effective when paired with real-time analysis. Tools like PhishAlarm Analyzer
use advanced machine learning, behavioral insights and sandboxing to quickly
analyze reported messages.
In this process, we can definitely auto-classify between 60% and 80% of user-
reported messages as malicious/spam or bulk/benign. Using a tool like CLEAR
(see sidebar), those classifications can be tied to an automated action such as
removing the message and similar threats, resetting user credentials or closing
the case (if the email is benign).
The accuracy rates shown in Table 4 reflect the percentage of messages sent
to Analyzer that were classified as malicious, suspicious or spam. (Messages
classified as bulk, low risk or unknown are not factored into accuracy rates.)20
Even the “lower” accuracy rates we see here have value: at least 2 of every 10
messages reported had evaded perimeter defenses. Naturally, a higher accuracy
rate is more favorable—and it’s a great metric to evaluate over time because it
reflects users’ ability to distinguish problem emails from safe ones.
We suggest targeting an accuracy rate of 50% or higher, which would indicate that
most of the messages your users are reporting are spam or potentially malicious,
rather than innocuous. But like resilience, it’s a metric that requires time and
patience—and a focused effort to assess your users’ weaknesses and provide
the right training. If you have a tool like CLEAR, your remediation teams won’t be
overtaxed as reporting accuracy is given space to improve.
20 Note that simulated phishing attacks, when reported, are not forwarded to PhishAlarm Analyzer. So, by
default, simulated phishing reports are not factored into accuracy ratings.
32

2022 STATE OF THE PHISH \ REPORT
Reporting Accuracy Rates by Industry
Industry Accuracy Rate
Legal 45%
Engineering 42%
Education 41%
Government 36%
Agriculture 35%
Real Estate 35%
Business Services 34%
Entertainment/Media 34%
Insurance 34%
Manufacturing 34%
Construction 33%
Electronics 32%
Financial Services 32%
Hospitality/Leisure 32%
Telecommunications 32%
Energy/Utilities 30%
Technology 30%
Transportation 30%
Aerospace 29%
Food & Beverages 29%
Consulting 29%
Healthcare 28%
Retail 27%
Automotive 26%
Mining 22%
Table 4
33

2022 STATE OF THE PHISH \ REPORT
Section 6
Security Awareness Training:
99
%
Insights and Opportunities
of organizations have a security
awareness training program
___________ BUT ___________
Understanding of industry trends, employee knowledge gaps and benchmark
57 data won’t do much for you if you don’t act on what you learn. Security awareness
%
training is a must for organizations across the globe. And security frameworks and
Only
compliance requirements shouldn’t be the only things driving you to make it part
provide organization-wide training of your defense-in-depth strategy.
___________ AND ___________
The good news is that nearly everyone is doing something to educate employees:
85 99% of the infosec and IT professionals we surveyed said their organization has
%
Only a security awareness training program. The bad news? How programs are being
implemented leaves much room for improvement. (And as we noted earlier:
educate employees who fall for real or
from a risk perspective, how people do things is often more important, than what
simulated phishing attacks.
they do.)
Here are some areas of concern revealed in our global survey:
• Fewer than 60% of organizations deliver organization-wide training. Nearly 30%
focus their efforts strictly on specific departments and roles, and another 15%
are only concerned about specific individuals.
• Fewer than 50% of organizations formally cover email-based phishing in their
training programs, and just 43% cover ransomware. In comparison, more than
80% of organizations experienced at least one successful phishing attack in
2021, and nearly 70% dealt with at least one ransomware infection. (See more
on topics later in this section.)
COUNTRY SPOTLIGHT • 81% of organizations said that more than half of their employees are working
remotely (either part time or full time) due to the pandemic. But just 37%
68
% educate workers about best practices for remote working.
• Only 34% educate employees about best practices for email reporting.
of French organizations deliver
• Nearly 15% of organizations do not educate workers who interact with real or
organization-wide training, the highest
simulated phishing emails. (And just to be clear: we consider this to be too large
of any region surveyed.
a number.)
45
%
of Japanese organizations train only
specific departments and roles
(60% higher than the global average).
23
%
of Spanish organizations train only
specific individuals, followed closely
by Australian organizations (22%).
34

2022 STATE OF THE PHISH \ REPORT
Training tools and frequency of use
73
%
Security awareness training programs should use several different tools—variety
of organizations deliver is your friend when it comes to educating users. A mix of tools will not only help
formal security awareness to keep employees engaged, it will also help you learn different things about the
training to their employees people you rely on to protect your organization’s data, devices and systems.
(via computer-based,
in-person or instructor-led Variety also helps apply key learning principles to your program: reinforcement
virtual training). and repetition. Reaching users in multiple ways and keeping cybersecurity a
relevant and palatable conversation are critical.
Don’t focus just on teaching and testing. Friendly reminders, notes about trending
threats, and even program performance news—like big saves when employees
report real-world phish—offer opportunities to show how important cybersecurity
is to your organization and plant the seeds for a strong security culture.
Nearly 75% of organizations said they assign what we consider to be “formal”
training to their users (note that more than one answer was permitted):
COUNTRY SPOTLIGHT
• 43% deliver computer-based training
37
% • 38% provide in-person training
• 35% offer virtual, instructor-led training
of Australian organizations use simulated
phishing attacks, the least of any region Formal education sessions were, by far, the most used component of security
surveyed. But they are by far the most awareness training programs in 2021, according to survey participants. Other
active in using them: 61% said their tools, and their percentage of use, include:
organization sends phishing simulations
daily. • Simulated phishing emails (41%)
• Newsletters or informative emails (39%)
37
%
• Awareness posters or videos (35%)
of UK organizations simulate malicious USB • Smishing and/or vishing simulations (33%)
drops, the most of any region surveyed. But
• Internal cybersecurity chat channel (32%)
this represents fewer than half of UK orgs
• Cybersecurity-based contests and prizes (30%)
that faced USB-based attacks in 2021.
• Simulated USB drops (28%)
<25
%
• Internal cybersecurity wiki (26%)
of Spanish and German organizations use Just 14% of organizations that use formal training said they train users only once
gamification techniques like contents and or twice a year. Ideally, this number would be 0%. Still, the trend toward more
prizes, the least among all regions surveyed. frequent training is a positive one.
We saw some indications that organizations could be using formal training and
phishing simulations too frequently (more on that to follow). But on the other end
of the spectrum, we also saw 38% organizations saying they allocated an hour or
less to formal training in 2021 (vs. 28% in 2020).
35

2022 STATE OF THE PHISH \ REPORT
1%
5% 4%
9% 14% 21%
16%
15% Frequency of Frequency of
Formal Phishing
Training Simulations
34% 27%
31%
23%
Daily Weekly Monthly Quarterly Twice a year Once a year
Figure 17 Figure 18
13% 9%
30 minutes or less
Time
12%
Allocated to 31 to 59 minutes
Formal 29% 1 to 2 hours
Training
Sessions in 2 to 3 hours
a Year More than 3 hours
37%
Figure 19
The key is balance. Yes, we believe cybersecurity must be talked about frequently.
And security awareness and training initiatives should be an ongoing pursuit that
allows skills to develop consistently over time. But an overabundance of anything
“extra” is not likely to be well-received by users. Training fatigue is a legitimate
concern.
We recommend a blend of formal, computer-based training assignments (done
at least quarterly) and monthly phishing simulations. These should be paired with
regular use of supporting materials and activities like posters, flyers, newsletters
and lunch-and-learn sessions.
Ultimately, it might take some time to comfortably identify the appetite for training
among your user base. For example, you may find that microlearning modules
(those that offer about 1-3 minutes of “bite-sized” training) are better received
by your users than longer, more intense training. And that may pave the way to a
monthly training schedule vs. a quarterly one.
One thing to always keep in mind: attackers are putting in time and effort to
identify and compromise your employees. Organizations that don’t allocate time
and effort to security awareness training in a way that’s most likely to resonate
with their people will be at a disadvantage.
36

2022 STATE OF THE PHISH \ REPORT
Orgs ignore too many important topics when
training users
Of the 99% who said their organization has a security awareness training
COUNTRY SPOTLIGHT program, all but one Japanese survey respondent said their program covers
at least one of the topics we surveyed about. But both globally and regionally,
Australian organizations lagged behind their
there’s not nearly the breadth or depth of coverage needed to prepare users to
global counterparts (and global averages)
defend against more sophisticated threat actors, who frequently use multiple
on coverage of several key security
techniques and tactics in a single attack campaign.
awareness training topics:
37
% Topics Covered in Security Awareness Training Programs
Email-based phishing
cover email-based phishing. 49%
Malware
35
% 47%
Wi-Fi security
cover mobile device security. 44%
Ransomware
35
% 43%
Mobile device security
cover ransomware. 43%
Password best practices
29
% 42%
Best practices for internet safety
cover BEC. 40%
BEC/invoice fraud
29
% 40%
Cloud-based threats
cover cloud-based threats. 39%
Best practices for remote working
29
% 37%
Physical security measures
cover internet safety. 36%
Best practices for email reporting
27
% 34%
Compliance-related topics (GDPR, PCI, etc.)
cover malware. 33%
Insider threats
33%
Multi-factor authentication
32%
Social engineering
27%
Smishing
26%
Role-based training
25%
Vishing
23%
0% 10% 20% 30% 40% 50%
Figure 20
37

2022 STATE OF THE PHISH \ REPORT
Consequence models: could they cost you?
KEY FINDINGS
55 Here are some stats we don’t love:
%
• More than half of the infosec and IT professionals we surveyed said their
of organizations take disciplinary action
organization disciplines or punishes employees who interact with real or
against employees who fall for real or
simulated phishing emails.
simulated phishing attacks, the same
percentage as last year. • Another 4% said the launch of a consequence model is imminent within their
organization, and an additional 14% said they’re considering the approach.
24
% • Among those using a consequence model, more than 95% said that both real
and simulated attacks trigger consequences within their organization.
of organizations said a consequence model
is not the right fit for their organization’s Nearly three-quarters (73%) of survey respondents seem comfortable with the
culture (a new response choice this year). idea of punishing/disciplining (two words we used in our survey) employees for
their mistakes in handling email. That’s concerning enough. It’s even more vexing
70
% when you consider these points:
• Just 49% of survey respondents said their organization covers email-based
of those who employ a consequence model
phishing in their security awareness training program
said it has increased employee awareness
of phishing, a 15% year-over-year drop. • Only 25% said their organization allocates two or more hours to formal
25% said awareness is about the same, and employee training each year.
4% feel awareness has decreased since the
• Sometimes one mistake by a user is all it takes to trigger a consequence, even
introduction of consequences.
when the mistake is made in handling a hypothetical threat to the organization.
As we did last year, we excluded training from the list of “punishments” within
consequence models. That’s because training should never be presented to users
as a punishment. Training is an opportunity to learn and improve. And it should
always be positioned as a positive experience, not a negative one.
FOR YOUR CONSIDERATION
Technical safeguards that are purpose-built to identify and block phishing threats
aren’t perfect 100% of the time. Is it fair to ask employees who are not cybersecurity
experts to be perfect or be punished?
38

2022 STATE OF THE PHISH \ REPORT
Figure 21 shows the disciplinary actions that are used within our survey
GLOBAL “LEADERS’ respondents’ organizations, and Figure 22 breaks down the thresholds that
trigger the first consequence.
>75
%
of Australian and UK organizations use a
Consequences for Interacting with Real or Simulated Phishing Attacks
consequence model
One-on-one discussion with manager
73
% 60%
of U.S. organizations ask managers to One-on-one discussion with a member of the infosec team
counsel employees 59%
56 Impact to employees’ yearly performance reviews
%
52%
of Australian organizations ask their HR
HR-enforced disciplinary actions
teams to enforce certain disciplinary actions
45%
42
%
Removal of access to systems
of UK organizations impose a monetary 35%
penalty (62% higher than the global
Monetary penalty
average)
26%
39
% Termination
18%
of Spanish organizations said a
consequence model isn’t a cultural fit, 0% 10% 20% 30% 40% 50% 60%
followed closely by German organizations
Figure 21
(37%)
25
%
Figure 22 illustrates that it’s not just “repeat offenders” who are being punished
or more of UK, U.S., and Spanish for their email actions. And Figure 23 shows that many organizations are just as
organizations include termination in their eager to introduce consequences as they are to launch a security awareness
consequence models (vs. ~10% of training program.
German and Japanese organizations)
The First Action That Triggers a Consequence21
40%
35%
35% 33%
Simulated Phishing
Real-world Phishing
30%
COUNTRY SPOTLIGHT
24%
25% 23% 23%
26
%
20%
of German organizations have a 16%
consequence for users who fail a single 15%
phishing simulation. 11%
10% 8%
38 6%
% 5%
4% 4%
5%
2% 2%
of U.S. organizations punish users who fall
0%
for one real-world phishing attack. 1 failure 2 failures 3 failure 4 failures 5 failures More than 5 failures Unsure
Figure 22
21 Just 3% of respondents said that phishing test failures do not result in a consequence. Only 1% said that
falling for a real-world phishing attack doesn’t trigger a consequence.
39

2022 STATE OF THE PHISH \ REPORT
Correlation of Consequence Model Launch to
Launch of Security Awareness Training Program
Launched at the same time as security awareness training
45%
Launched within 6 to 12 months of security awareness training launch
35%
Launched within 1 to 2 years of security awareness training launch
14%
Launched more than 2 years after security awareness training
5%
Launched a consequence model without offering security awareness training
<1%
0% 10% 20% 30% 40% 50%
Figure 23
Some organizations feel they must punish users for their email mistakes. And if
handled with careful consideration and clear communication, a consequence
model may prove beneficial in some cases.
But it’s a slippery slope. Many organizations have found there are limited options
for delivering consequences in a fair, consistent and legally sound way.
And as found in our survey, many employees are not receptive to consequence
models. This sentiment can hurt an organization’s overall culture, leaving
employees less engaged, less responsive and less likely to want to participate in
cybersecurity initiatives.
Users’ Response to Consequence Model
KEY FINDING
1%
At 62%, Spanish organizations were most
likely to say that employees understand and
21%
accept the use of a consequence model. But Widespread acceptance
they’re also most likely to say that, in spite 37%
Mixed response
of many complaints, the organization is firm
Many complaints
in their belief that consequences are the
(organization working to address)
right approach to take (28%). 20%
Many complaints
(organization firm in maintaining approach)
21%
Unsure of users’ response
Figure 24
40

2022 STATE OF THE PHISH \ REPORT
Section 7
Making It Personal: Identifying
72
%
Vulnerabilities, Gauging Success
of infosec and IT
professionals surveyed said
their organization’s current We’ve analyzed a lot of information for this year’s report and provided more
security awareness training (and more robust) benchmarking data than ever. But we get that it can be
program has lowered phishing overwhelming—much like running a security awareness training program itself.
failure rates.
Just over 70% of the infosec and IT professionals we surveyed said they’ve seen
a reduction in phishing failure rates since launching their organization’s security
awareness training program. (Another 24% said phishing susceptibility has stayed
about the same, 3% said failure rates are higher, and 1% weren’t sure how training
has impacted failure rates.) The good news: based on our findings, there is a lot of
opportunity to run these programs more effectively.
Here are three key steps you can take to that end:
1. Prioritize the things that are important within
COUNTRY SPOTLIGHT
your organization
84
%
Here’s a key belief of ours: Everyone who can influence your organization’s
of U.S. organizations said security
cybersecurity posture should be trained in cybersecurity best practices.
awareness training has reduced phishing
Everyone should have a foundational understanding of common
failure rates, the highest of any region
surveyed. cybersecurity threats and practical defense measures. Everyone who touches
your network and data, everyone who handles your equipment, everyone who
6 manages or controls access to organizational assets. Everyone.
%
Just 57% of the infosec and IT professionals we surveyed said they take this
of Japanese organizations say phishing approach (and that number hovers around 50% for Japanese, Spanish and
failure rates have increased since the Australian organizations). Too many people who contribute to cybersecurity
implementation of their current security risk are being left out of training.
awareness training program, twice the
Still, that doesn’t mean you can’t be deliberate and strategic about how
global average.
you assess and train your people. And it doesn’t mean that everyone has
to receive the exact same training at the exact same time. And it certainly
doesn’t mean that your program should replicate that of an organization in
another industry (or even that of direct competitor).
Your program should prioritize topics you know are relevant to your industry
and your organization—and the people who work within it. The following
information can help you determine what to cover and with whom:
• Knowledge levels across your user base, including those who struggle to
understand basic concepts vs. those who exhibit more advanced skills
• Known, wider-spread issues within your organization (for example,
credential compromise, problems with lost devices, BYOD concerns or
improper use of cloud accounts)
• Compliance, regulatory or contractual training requirements
41

2022 STATE OF THE PHISH \ REPORT
• Specific job functions that are a threat to your organization if handled
incorrectly (for example, paying invoices/executing wire transfers, managing
confidential customer or employee data, accessing high-risk websites)
• High-visibility roles within your organization (for example, executives,
spokespeople and influencers)
• Department-level failure rates on phishing simulations
• Benchmark data and insights from others in your industry
2. Use threat intelligence to your advantage
Threat intelligence can help you determine a key piece of information: when
to deliver specific training to specific people.
93%
High-level threat intelligence shared publicly or privately is invaluable. This
may include the information we deliver on the Proofpoint Threat Insight blog,
of organizations factor threat
our Threat Hub or in our customer-facing Threat Alerts and Attack Spotlights.
intelligence into their security
awareness training plans (up But it’s just as critical to understand the people and departments within your
from 90% last year). organization that are being attacked and targeted at any given time, and the
ways attackers are trying to compromise your organization.
More than 90% of infosec and IT survey respondents said their organization’s
threat intelligence influences security awareness training decisions. But how
that happens could use some work.
We were glad to see gains in all three of the areas we surveyed (see Figure
25). But ideally, many more organizations would be taking advantage of
knowledge about their specific threat landscape and using that to inform their
training approach.
COUNTRY SPOTLIGHT
Use of Threat Intelligence
71
%
of Spanish organizations train about topics
60% 53% 43%
that relate to attacks they know their
organization is facing.
67
%
of U.S. organizations use phishing tests that train users about topics use phishing simulations deliver specific training to
mimic trending threats. that relate to known that mimic trending people who are being
attacks on their threats targeted by certain types
organization of attacks
53
%
Figure 25
of UK organizations train individuals they
know are being targeted by specific types of
attacks.
14
%
of Japanese organizations do not adjust
training based on threat intelligence, and
another 4% say they do not have access to
threat data.
42

2022 STATE OF THE PHISH \ REPORT
In 2021, we added a CISO Dashboard to our Security Education Platform. A key feature of that dashboard is the User Vulnerability
Summary, which identifies key indicators of vulnerability among an organization’s employees. Customers can view users with low
participation rates and low performance rates. Those who leverage Proofpoint Targeted Attack Protection (TAP) can also identify their
organization’s Very Attacked People (VAPs) and Top Clickers.
To improve the effectiveness of your security awareness training program, we
suggest identifying the following:
• The individual and group inboxes that are being sent the largest
number of suspicious and malicious messages. We refer to these
individuals and inboxes as Very Attacked People™ (or VAPs). These users
are sometimes VIPs—but often, they’re not. And your organization’s VAPs
can change a lot over time.
• Trending attack characteristics. Attack intensity and methodology can
change over time, just as VAPs can. Examining the how behind the what
can reveal vital information. For example, suppose threat intelligence shows
an increase in credential harvesting attempts targeting specific people and
groups. With the right intel, you can quickly communicate that insight and
deliver training tailored to reduce specific risks.
• Vulnerable users. Being able to identify specific people who have fallen
for real or simulated phishing attacks and the lures they fell for can be
incredibly valuable.
• The intersection of vulnerability, attacks and privilege. This is what we
like to call the “perfect storm”: privileged users within your organization
who are vulnerable to attack and are being actively targeted. These are the
risks to know about—and address. (The User Vulnerability Summary in our
CISO Dashboard helps our customers do this. See the callout on this page
for more.)
43

2022 STATE OF THE PHISH \ REPORT
3. Evaluate key security awareness training metrics
Security Program Effectiveness:
Ranking by industry
to gauge success
1. Engineering
You should not hinge your view of success on a single measurement (like
2. Financial Services
phishing test failure rates). And benchmark data should neither induce panic
3. Aerospace within your organization nor give you a false sense of security.
As with a security awareness training program itself, “success” measurement
4. Energy/Utilities
should include multiple components and take individual organizational factors
into account.
5. Manufacturing
To help organizations better gauge how effective their programs are, we
6. Legal introduced a new feature in our Security Education Platform in 2021: the CISO
Dashboard. In addition to at-a-glance views of user vulnerability (see callout
7. Telecommunications
on page 43), this dashboard displays and aggregates key performance and
participation indicators that help drive decision-making.
8. Consulting
Our overall Security Program Score provides a holistic review of an
9. Construction organization’s security awareness program and its results. The overall score
factors in the following:
10. Insurance
1. Phishing simulation failures
11. Electronics
2. Phishing simulation reporting
12. Mining 3. Knowledge assessments
4. Reported email accuracy
13. Entertainment/Media
5. Training participation
14. Automotive
This type of high-level view helps organizations gauge the relative health of
15. Food & Beverages their security awareness training program and improvements over time. It
also helps with decision-making, course corrections and program planning.
16. Hospitality/Leisure
After all, a security awareness training program should be an ongoing
initiative. Where you are today isn’t where you’ll be in a year. As threats,
17. Technology
knowledge levels and key metrics evolve, your program should adapt
18. Transportation with them.
With that in mind, we leave you with a final ranking: overall program
19. Agriculture
effectiveness by industry. This ranking, shown in Table 5, is based on
participation and performance across all five aspects of security awareness
20. Education
training listed above.
21. Real Estate
22. Business Services
23. Government
24. Healthcare
25. Retail
Table 5
44

2022 STATE OF THE PHISH  \  REPORT
Section 8
Appendix
A.  Infosec and IT security survey: country-by-country breakdown
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
How many of these cyberattacks—successful and unsuccessful—did your organization experience in 2021?
Bulk phishing attack (same email sent to multiple people)
| 0               | 10% | 12% | 15% 22% | 11% 9%  | 17% 14% |
| --------------- | --- | --- | ------- | ------- | ------- |
| 1-10            | 46% | 41% | 20% 30% | 49% 33% | 36% 36% |
| 11-25           | 18% | 20% | 26% 14% | 17% 13% | 18% 18% |
| 26-50           | 10% | 14% | 18% 16% | 15% 23% | 11% 15% |
| 51-100          | 8%  | 8%  | 11% 6%  | 2% 12%  | 8% 8%   |
| 100+            | 6%  | 5%  | 6% 8%   | 6% 9%   | 9% 7%   |
| Unsure of total | 2%  | 0%  | 4% 4%   | 0% 1%   | 1% 2%   |
Spear phishing/whaling (targeted email attack)
| 0               | 8%  | 14% | 16% 40% | 26% 18% | 23% 21% |
| --------------- | --- | --- | ------- | ------- | ------- |
| 1-10            | 18% | 39% | 26% 28% | 32% 29% | 20% 27% |
| 11-25           | 48% | 16% | 24% 14% | 22% 25% | 29% 25% |
| 26-50           | 12% | 15% | 12% 8%  | 5% 18%  | 15% 12% |
| 51-100          | 8%  | 13% | 16% 8%  | 9% 3%   | 5% 9%   |
| 100+            | 4%  | 2%  | 2% 0%   | 5% 7%   | 7% 4%   |
| Unsure of total | 2%  | 1%  | 4% 2%   | 1% 0%   | 1% 2%   |
Business email compromise (for example, wire transfer fraud or invoice fraud)
| 0               | 10% | 25% | 25% 36% | 23% 19% | 21% 23% |
| --------------- | --- | --- | ------- | ------- | ------- |
| 1-10            | 30% | 29% | 22% 24% | 33% 25% | 26% 27% |
| 11-25           | 24% | 22% | 14% 10% | 19% 20% | 24% 19% |
| 26-50           | 26% | 17% | 21% 6%  | 14% 19% | 11% 16% |
| 51-100          | 4%  | 6%  | 10% 12% | 4% 9%   | 9% 8%   |
| 100+            | 4%  | 1%  | 5% 8%   | 7% 7%   | 7% 5%   |
| Unsure of total | 2%  | 0%  | 3% 4%   | 0% 1%   | 2% 2%   |
45

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. | Average  |
| --- | --------- | ------ | ------------- | -------- | ---- | -------- |
Email-based ransomware attack (ransomware payload delivered via email)
| 0               | 10% | 20% | 20% 32% | 32% 16% | 22% | 22% |
| --------------- | --- | --- | ------- | ------- | --- | --- |
| 1-10            | 14% | 31% | 32% 26% | 37% 28% | 25% | 28% |
| 11-25           | 36% | 24% | 13% 22% | 8% 21%  | 21% | 21% |
| 26-50           | 24% | 10% | 16% 8%  | 8% 18%  | 17% | 14% |
| 51-100          | 8%  | 13% | 13% 8%  | 9% 9%   | 9%  | 10% |
| 100+            | 8%  | 2%  | 3% 2%   | 5% 7%   | 5%  | 4%  |
| Unsure of total | 0%  | 0%  | 3% 2%   | 1% 1%   | 1%  | 1%  |
Smishing (SMS/text message phishing)
| 0               | 8%  | 29% | 27% 26% | 43% 20% | 25% | 26% |
| --------------- | --- | --- | ------- | ------- | --- | --- |
| 1-10            | 24% | 23% | 19% 38% | 21% 16% | 16% | 23% |
| 11-25           | 26% | 14% | 16% 6%  | 21% 20% | 24% | 18% |
| 26-50           | 22% | 26% | 18% 10% | 5% 19%  | 13% | 16% |
| 51-100          | 12% | 5%  | 9% 14%  | 6% 13%  | 11% | 10% |
| 100+            | 8%  | 3%  | 7% 2%   | 4% 11%  | 10% | 6%  |
| Unsure of total | 0%  | 0%  | 4% 4%   | 0% 1%   | 1%  | 1%  |
Vishing (voice phishing via phone calls)
| 0               | 8%  | 31% | 34% 44% | 51% 22% | 28% | 31% |
| --------------- | --- | --- | ------- | ------- | --- | --- |
| 1-10            | 22% | 26% | 20% 24% | 22% 20% | 19% | 22% |
| 11-25           | 30% | 20% | 15% 10% | 15% 21% | 27% | 20% |
| 26-50           | 30% | 11% | 12% 8%  | 6% 16%  | 10% | 13% |
| 51-100          | 8%  | 10% | 11% 8%  | 2% 15%  | 7%  | 9%  |
| 100+            | 2%  | 2%  | 4% 2%   | 4% 6%   | 9%  | 4%  |
| Unsure of total | 0%  | 0%  | 4% 4%   | 0% 0%   | 0%  | 1%  |
USB drops (thumb drives weaponized with malicious software or code)
| 0               | 10% | 38% | 36% 48% | 59% 22% | 37% | 36% |
| --------------- | --- | --- | ------- | ------- | --- | --- |
| 1-10            | 18% | 22% | 19% 24% | 15% 20% | 19% | 19% |
| 11-25           | 30% | 15% | 13% 14% | 15% 19% | 19% | 18% |
| 26-50           | 24% | 17% | 14% 6%  | 7% 21%  | 9%  | 14% |
| 51-100          | 8%  | 6%  | 9% 6%   | 3% 10%  | 11% | 8%  |
| 100+            | 10% | 2%  | 5% 0%   | 1% 8%   | 5%  | 4%  |
| Unsure of total | 0%  | 0%  | 4% 2%   | 0% 0%   | 0%  | 1%  |
Social media attacks (for example, pretexting or account takeover)
| 0               | 8%  | 23% | 26% 42% | 45% 15% | 25% | 26% |
| --------------- | --- | --- | ------- | ------- | --- | --- |
| 1-10            | 22% | 26% | 17% 18% | 22% 24% | 22% | 21% |
| 11-25           | 36% | 19% | 18% 18% | 12% 15% | 19% | 20% |
| 26-50           | 14% | 15% | 16% 4%  | 10% 24% | 15% | 14% |
| 51-100          | 10% | 13% | 11% 10% | 8% 9%   | 10% | 10% |
| 100+            | 10% | 4%  | 8% 2%   | 3% 13%  | 7%  | 7%  |
| Unsure of total | 0%  | 0%  | 4% 6%   | 0% 0%   | 2%  | 2%  |
46

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
How many SUCCESSFUL phishing attacks did your organization experience in 2021?
| 0               | 8%  | 12% | 20%  34% | 18% 9%  | 21% 17% |
| --------------- | --- | --- | -------- | ------- | ------- |
| 1-3             | 14% | 30% | 28% 26%  | 36% 26% | 20% 26% |
| 4-6             | 38% | 32% | 21% 22%  | 26% 27% | 25% 27% |
| 7-9             | 16% | 17% | 12% 12%  | 11% 24% | 23% 16% |
| 10 or more      | 20% | 8%  | 15% 6%   | 8% 13%  | 9% 11%  |
| Unsure of total | 4%  | 1%  | 4% 0%    | 1% 1%   | 2% 2%   |
What impact(s) did successful phishing attacks have on your organization in 2021?
Loss of data/intellectual property 52% 51% 50% 24% 25% 57% 52% 44%
Breach of customer/client data 64% 49% 57% 48% 42% 57% 60% 54%
Credential/account compromise 57% 52% 46% 42% 38% 58% 43% 48%
Ransomware infection (email payload) 61% 40% 49% 45% 33% 50% 40% 46%
| Other malware infection(s) | 36% | 25% | 28% 27% | 15% 30% | 28% 27% |
| -------------------------- | --- | --- | ------- | ------- | ------- |
Financial loss/wire transfer fraud 30% 20% 14% 3% 9% 29% 18% 17%
| Advanced persistent threat | 30% | 16% | 17% 9%  | 14% 24% | 19% 18% |
| -------------------------- | --- | --- | ------- | ------- | ------- |
| Zero-day exploit           | 18% | 13% | 14% 0%  | 14% 29% | 17% 15% |
| Widespread outage/downtime | 20% | 22% | 22% 12% | 19% 28% | 34% 22% |
| Reputational damage        | 27% | 21% | 22% 15% | 17% 33% | 29% 24% |
Financial penalty (e.g., regulatory fine) 14% 7% 8% 3% 5% 24% 18% 11%
| I’m not sure | 2%  | 1%  | 0% 6% | 2% 1% | 1% 2% |
| ------------ | --- | --- | ----- | ----- | ----- |
Did your organization experience any ransomware infections (due to email, later-stage malware delivery, etc.) in 2021?
| Yes          | 80% | 81% | 54% 50% | 62% 78% | 72% 68% |
| ------------ | --- | --- | ------- | ------- | ------- |
| No           | 20% | 17% | 42% 48% | 33% 21% | 25% 29% |
| I’m not sure | 0%  | 2%  | 4% 2%   | 5% 1%   | 3% 3%   |
How many SEPARATE ransomware infections did your organization experience?
| 1-3             | 18% | 35% | 35% 48% | 48% 25% | 31% 34% |
| --------------- | --- | --- | ------- | ------- | ------- |
| 4-6             | 47% | 39% | 35% 24% | 32% 32% | 35% 35% |
| 7-9             | 5%  | 19% | 9% 20%  | 15% 24% | 22% 16% |
| 10 or more      | 30% | 7%  | 21% 4%  | 5% 18%  | 12% 14% |
| Unsure of total | 0%  | 0%  | 0% 4%   | 0% 1%   | 0% 1%   |
Did your organization pay any ransoms to resolve a ransomware infection/attack in 2021?
| Yes          | 80% | 56% | 65% 20% | 39% 82% | 64% 58% |
| ------------ | --- | --- | ------- | ------- | ------- |
| No           | 20% | 43% | 33% 80% | 61% 18% | 36% 42% |
| I’m not sure | 0%  | 1%  | 2% 0%   | 0% 0%   | 0% <1%  |
47

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain | UK U.S. | Average  |
| --- | --------- | ------ | ------------- | ----- | ------- | -------- |
Thinking of the most recent payment made, what happened?
Paid one ransom and regained access  53% 69% 54% 40% 37% 69% 54% 54%
to data/systems
Paid an initial ransom and follow-up  41% 20% 37% 20% 42% 28% 39% 32%
ransom(s) and got access to data/
systems
Paid an initial ransom, refused to pay  3% 4% 9% 20% 21% 3% 7% 10%
more, and did not get access to data
Never got access to data, even after  0% 7% 0% 20% 0% 0% 0% 4%
paying
| I’m not sure | 3%  | 0%  | 0% 0% | 0%  | 0% 0% | <1% |
| ------------ | --- | --- | ----- | --- | ----- | --- |
Does your organization run a security awareness training program?
| Yes | 98% | 100% | 97% 98% | 100% | 98% 100% | 99% |
| --- | --- | ---- | ------- | ---- | -------- | --- |
| No  | 2%  | 0%   | 3% 2%   | 0%   | 2% 0%    | 1%  |
Which of the following topics are covered in your security awareness training program?
| Email-based phishing    | 37% | 54% | 42% 57% | 58% | 40% 57% | 49% |
| ----------------------- | --- | --- | ------- | --- | ------- | --- |
| Malware                 | 27% | 48% | 48% 61% | 61% | 35% 48% | 47% |
| Wi-Fi security          | 39% | 37% | 43% 35% | 58% | 46% 49% | 44% |
| Ransomware              | 35% | 44% | 47% 37% | 58% | 40% 43% | 43% |
| Mobile device security  | 35% | 40% | 44% 47% | 49% | 36% 51% | 43% |
| Password best practices | 37% | 37% | 47% 45% | 47% | 32% 46% | 42% |
Best practices for internet safety 29% 42% 36% 45% 59% 35% 38% 40%
BEC (e.g., wire transfer/invoice fraud) 29% 35% 38% 57% 53% 31% 38% 40%
| Cloud-based threats | 29% | 36% | 41% 45% | 51% | 35% 37% | 39% |
| ------------------- | --- | --- | ------- | --- | ------- | --- |
Best practices for remote working 35% 30% 25% 43% 48% 35% 43% 37%
| Physical security measures  | 33% | 32% | 35% 45% | 31% | 38% 41% | 36% |
| --------------------------- | --- | --- | ------- | --- | ------- | --- |
Best practices for email reporting 33% 30% 32% 27% 43% 30% 43% 34%
| Insider threats | 27% | 34% | 31% 39% | 34% | 32% 38% | 33% |
| --------------- | --- | --- | ------- | --- | ------- | --- |
Compliance topics (e.g., GDPR and  31% 31% 34% 29% 36% 28% 40% 33%
PCI)
| Multi-factor authentication | 33% | 26% | 34% 35% | 34% | 28% 37% | 32% |
| --------------------------- | --- | --- | ------- | --- | ------- | --- |
| Social engineering          | 39% | 17% | 25% 22% | 21% | 33% 31% | 27% |
| Smishing                    | 22% | 27% | 19% 24% | 33% | 30% 30% | 26% |
| Role-based training         | 31% | 25% | 23% 14% | 25% | 27% 28% | 25% |
| Vishing                     | 14% | 22% | 25% 22% | 33% | 19% 26% | 23% |
| None of these               | 0%  | 0%  | 0% 2%   | 0%  | 0% 0%   | <1% |
48

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
Who does your organization assign security awareness training to?
| Everyone in the organization | 51% | 68% | 56% 49% | 50% 59% | 64% 57% |
| ---------------------------- | --- | --- | ------- | ------- | ------- |
| Select departments/roles     | 25% | 23% | 33% 45% | 26% 25% | 22% 28% |
| Select individuals           | 22% | 9%  | 11% 6%  | 23% 16% | 14% 15% |
| I’m not sure                 | 2%  | 0%  | 0% 0%   | 1% 0%   | 0% <1%  |
Which of the following tools are used in your security awareness training program?
| In-person training sessions | 22% | 35% | 35% 37% | 52% 41% | 47% 38% |
| --------------------------- | --- | --- | ------- | ------- | ------- |
Virtual, instructor-led training 29% 38% 38% 27% 46% 31% 34% 35%
| Computer-based training      | 31% | 41% | 48% 35% | 44% 51% | 50% 43% |
| ---------------------------- | --- | --- | ------- | ------- | ------- |
| Simulated phishing attacks   | 37% | 38% | 44% 47% | 39% 38% | 41% 41% |
| Awareness posters and videos | 39% | 41% | 30% 37% | 19% 41% | 38% 35% |
| Newsletters and emails       | 39% | 40% | 37% 43% | 40% 35% | 42% 39% |
Cybersecurity-based contests/prizes 31% 29% 23% 29% 22% 39% 35% 30%
Smishing and/or vishing simulations 37% 29% 31% 35% 31% 30% 37% 33%
| Simulated USB drops | 35% | 28% | 21% 24% | 23% 37% | 29% 28% |
| ------------------- | --- | --- | ------- | ------- | ------- |
Internal cybersecurity chat channel 33% 28% 35% 33% 33% 26% 36% 32%
| Internal wiki | 31% | 22% | 31% 24% | 24% 29% | 22% 26% |
| ------------- | --- | --- | ------- | ------- | ------- |
How often does your organization send phishing simulations to employees?
| Daily        | 61% | 5%  | 26% 0%  | 5% 38%  | 15% 21% |
| ------------ | --- | --- | ------- | ------- | ------- |
| Weekly       | 28% | 39% | 26% 39% | 28% 22% | 37% 31% |
| Monthly      | 6%  | 34% | 28% 35% | 39% 21% | 27% 27% |
| Quarterly    | 5%  | 11% | 16% 17% | 23% 19% | 19% 16% |
| Twice a year | 0%  | 8%  | 2% 9%   | 5% 0%   | 2% 4%   |
| Once a year  | 0%  | 3%  | 2% 0%   | 0% 0%   | 0% 1%   |
Does your organization offer educational training to employees who fall for simulated or real-world phishing emails?
| Yes          | 88% | 86% | 83% 82% | 89% 84% | 83% 85% |
| ------------ | --- | --- | ------- | ------- | ------- |
| No           | 10% | 12% | 15% 18% | 10% 13% | 16% 13% |
| I’m not sure | 2%  | 2%  | 2% 0%   | 1% 3%   | 1% 2%   |
How often does your organization assign formal training (in-person, instructor-led, or computer-based)?
| Daily        | 23% | 8%  | 10% 3%  | 5% 32%  | 20% 14% |
| ------------ | --- | --- | ------- | ------- | ------- |
| Weekly       | 47% | 37% | 22% 37% | 25% 34% | 36% 34% |
| Monthly      | 24% | 24% | 23% 23% | 27% 23% | 19% 23% |
| Quarterly    | 3%  | 15% | 17% 23% | 25% 6%  | 16% 15% |
| Twice a year | 3%  | 12% | 14% 11% | 11% 5%  | 2% 9%   |
| Once a year  | 0%  | 4%  | 14% 3%  | 7% 0%   | 7% 5%   |
49

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. | Average  |
| --- | --------- | ------ | ------------- | -------- | ---- | -------- |
In a year, how much time does your organization allocate to formal training (in-person, instructor-led, or computer-based)?
| 30 minutes or less | 29% | 5%  | 3% 6%   | 4% 4%   | 12% | 9%  |
| ------------------ | --- | --- | ------- | ------- | --- | --- |
| 31-59 minutes      | 29% | 37% | 29% 29% | 21% 32% | 25% | 29% |
| 1-2 hours          | 24% | 31% | 38% 53% | 35% 38% | 37% | 37% |
| 2-3 hours          | 6%  | 14% | 17% 10% | 19% 10% | 12% | 12% |
| More than 3 hours  | 12% | 13% | 13% 2%  | 21% 16% | 14% | 13% |
Since implementing your current security awareness training program, has your organization experienced lower phishing failure
rates?
| Yes                 | 78% | 74% | 69% 55% | 72% 68% | 84% | 72% |
| ------------------- | --- | --- | ------- | ------- | --- | --- |
| About the same      | 18% | 20% | 30% 35% | 26% 26% | 13% | 24% |
| No, they are higher | 4%  | 4%  | 0% 6%   | 2% 5%   | 1%  | 3%  |
| I’m not sure        | 0%  | 2%  | 1% 4%   | 0% 1%   | 2%  | 1%  |
Does your organization’s threat intelligence influence your security awareness training decisions? (Multiple responses allowed.)
Yes, we use phishing tests that mimic  56% 61% 43% 48% 45% 51% 67% 53%
trending threats
Yes, we train on specific topics that  68% 64% 55% 50% 71% 58% 56% 60%
relate to attacks we are facing
Yes, we train specific individuals we  40% 39% 44% 40% 45% 53% 43% 43%
know are being targeted
| No, we do not adjust our training  | 2%  | 5%  | 8% 14% | 4% 6% | 5%  | 6%  |
| ---------------------------------- | --- | --- | ------ | ----- | --- | --- |
according to threat intelligence
| N/A (I don't have access to my  | 0%  | 0%  | 2% 4% | 0% 1% | 0%  | 1%  |
| ------------------------------- | --- | --- | ----- | ----- | --- | --- |
organization’s threat intelligence)
As a product of the pandemic, are more than 50% of your organization’s employees working remotely?
| Yes, full-time remote | 50% | 26% | 23% 16% | 24% 49% | 47% | 34% |
| --------------------- | --- | --- | ------- | ------- | --- | --- |
Yes, part-time remote, part-time on site 38% 49% 57% 62% 56% 32% 35% 47%
They were but aren’t any longer 10% 17% 13% 14% 16% 15% 16% 14%
| No, our employees were not impacted  | 0%  | 5%  | 5% 6% | 3% 2% | 1%  | 3%  |
| ------------------------------------ | --- | --- | ----- | ----- | --- | --- |
this way by the pandemic
| More than 50% of our employees  | 2%  | 3%  | 2% 2% | 1% 2% | 1%  | 2%  |
| ------------------------------- | --- | --- | ----- | ----- | --- | --- |
always work remotely
Excluding educational training, do employees in your organization face discipline/punishment (i.e., a consequence model) for
interacting with real or simulated phishing attacks?
| Yes | 78% | 53% | 42% 44% | 29% 77% | 60% | 55% |
| --- | --- | --- | ------- | ------- | --- | --- |
No, it’s not a fit for our culture 14% 28% 37% 24% 39% 5% 21% 24%
No, but we’re considering this approach 4% 12% 15% 18% 22% 11% 15% 14%
| No, but we will implement this soon | 2%  | 4%  | 4% 6% | 9% 4% | 2%  | 4%  |
| ----------------------------------- | --- | --- | ----- | ----- | --- | --- |
| No, I don’t know what this is       | 0%  | 0%  | 2% 8% | 0% 1% | 2%  | 2%  |
| I’m not sure                        | 2%  | 3%  | 0% 0% | 1% 2% | 0%  | 1%  |
50

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
Excluding educational training, what are the consequences employees face? (Multiple answers allowed.)
| Counseling from manager | 56% | 57% | 55% 59% | 48% 73% | 73% 60% |
| ----------------------- | --- | --- | ------- | ------- | ------- |
Counseling from the infosec team 59% 66% 64% 68% 52% 51% 50% 59%
Impact to yearly performance reviews 67% 47% 45% 45% 34% 65% 63% 52%
Disciplinary actions (like a written  56% 53% 50% 41% 28% 48% 42% 45%
warning) enforced by HR
| Removal of access to systems | 46% | 30% | 31% 27% | 34% 53% | 25% 35% |
| ---------------------------- | --- | --- | ------- | ------- | ------- |
| Monetary penalty             | 31% | 30% | 21% 5%  | 31% 42% | 25% 26% |
| Termination                  | 15% | 11% | 10% 9%  | 28% 29% | 25% 18% |
| I’m not sure                 | 3%  | 0%  | 2% 0%   | 0% 0%   | 2% 1%   |
For simulated phishing attacks: What is the FIRST action that determines whether an employee faces a consequence?
| Failing 1 phishing test            | 8%  | 6%  | 26% 23% | 17% 13% | 20% 16% |
| ---------------------------------- | --- | --- | ------- | ------- | ------- |
| Failing 2 phishing tests           | 28% | 49% | 26% 32% | 45% 23% | 28% 33% |
| Failing 3 phishing tests           | 31% | 19% | 29% 27% | 17% 26% | 20% 24% |
| Failing 4 phishing tests           | 13% | 21% | 5% 14%  | 4% 12%  | 10% 11% |
| Failing 5 phishing tests           | 8%  | 2%  | 2% 0%   | 4% 12%  | 8% 5%   |
| Failing more than 5 phishing tests | 8%  | 2%  | 5% 0%   | 10% 10% | 7% 6%   |
Failing phishing tests does not result in  0% 0% 5% 4% 0% 3% 5% 3%
a consequence
| I’m not sure | 4%  | 1%  | 2% 0% | 3% 1% | 2% 2% |
| ------------ | --- | --- | ----- | ----- | ----- |
For real-world phishing attacks: What is the FIRST action that determines whether an employee faces a consequence?
Falling for 1 real-world phishing attack 10% 2% 31% 32% 28% 17% 38% 23%
Falling for 2 real-world phishing attacks 36% 56% 34% 41% 35% 21% 27% 35%
Falling for 3 real-world phishing attacks 31% 23% 24% 18% 24% 31% 8% 23%
Falling for 4 real-world phishing attacks 10% 11% 2% 0% 0% 19% 13% 8%
Falling for 5 real-world phishing attacks 8% 6% 5% 0% 3% 5% 5% 4%
Falling for more than 5 phishing attacks 0% 0% 0% 4% 10% 7% 5% 4%
Falling for real-world phishing attacks  0% 0% 2% 5% 0% 0% 2% 1%
does not result in a consequence
| I’m not sure | 5%  | 2%  | 2% 0% | 0% 0% | 2% 2% |
| ------------ | --- | --- | ----- | ----- | ----- |
How did the implementation of a consequence module correlate to the launch of your security awareness training program?
Launched at the same time as security  57% 41% 33% 27% 45% 57% 57% 45%
awareness training
Launched 6 to 12 months after security  31% 40% 38% 46% 41% 24% 27% 35%
awareness training
Launched 1 to 2 years after security  5% 11% 22% 18% 10% 17% 13% 14%
awareness training
| Launched more than 2 years after  | 8%  | 8%  | 5% 9% | 4% 1% | 3% 5% |
| --------------------------------- | --- | --- | ----- | ----- | ----- |
security awareness training
| Launched a consequence model  | 0%  | 0%  | 0% 0% | 0% 1% | 0% <1% |
| ----------------------------- | --- | --- | ----- | ----- | ------ |
without having a training program
| I’m not sure | 0%  | 0%  | 2% 0% | 0% 0% | 0% <1% |
| ------------ | --- | --- | ----- | ----- | ------ |
51

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
How has the use of a consequence model impacted employee awareness of phishing?
| Awareness has increased     | 61% | 68% | 64% 91% | 65% 71% | 70% 70% |
| --------------------------- | --- | --- | ------- | ------- | ------- |
| Awareness is about the same | 31% | 28% | 31% 9%  | 28% 25% | 27% 25% |
| Awareness has decreased     | 8%  | 4%  | 2% 0%   | 7% 4%   | 3% 4%   |
| I’m not sure                | 0%  | 0%  | 3% 0%   | 0% 0%   | 0% <1%  |
What best describes how employees have responded to these consequences overall?
For the most part, people seem to  33% 40% 22% 32% 62% 40% 30% 37%
understand and accept the approach
| The response has been mixed | 23% | 17% | 24% 32% | 0% 29% | 25% 21% |
| --------------------------- | --- | --- | ------- | ------ | ------- |
There have been many complaints, but  21% 26% 38% 9% 10% 10% 22% 20%
we’re working to resolve concerns
There have been many complaints, but  21% 17% 14% 27% 28% 21% 22% 21%
we firmly believe it’s the right approach
| I’m not sure | 2%  | 0%  | 2% 0% | 0% 0% | 1% 1% |
| ------------ | --- | --- | ----- | ----- | ----- |
Cybersecurity for your organization is:
| High priority       | 70% | 65% | 65% 44% | 74% 67% | 69% 65% |
| ------------------- | --- | --- | ------- | ------- | ------- |
| Priority            | 24% | 32% | 25% 46% | 20% 22% | 30% 28% |
| Somewhat a priority | 4%  | 3%  | 7% 6%   | 5% 9%   | 1% 5%   |
| Low priority        | 2%  | 0%  | 3% 4%   | 1% 2%   | 0% 2%   |
| Not a priority      | 0%  | 0%  | 0% 0%   | 0% 0%   | 0% 0%   |
In your organization, cybersecurity for the average employee is:
| High priority       | 66% | 44% | 48% 32% | 53% 56% | 53% 50% |
| ------------------- | --- | --- | ------- | ------- | ------- |
| Priority            | 26% | 43% | 43% 46% | 41% 34% | 39% 39% |
| Somewhat a priority | 4%  | 13% | 7% 16%  | 6% 7%   | 5% 8%   |
| Low priority        | 4%  | 0%  | 1% 6%   | 0% 2%   | 3% 2%   |
| Not a priority      | 0%  | 0%  | 1% 0%   | 0% 1%   | 0% <1%  |
Organizations often talk about building a culture of security. How do you feel about the security culture at your organization?
| Positive | 90% | 88% | 80% 76% | 89% 84% | 86% 85% |
| -------- | --- | --- | ------- | ------- | ------- |
| Neutral  | 8%  | 12% | 18% 24% | 11% 15% | 13% 14% |
| Negative | 2%  | 0%  | 2% 0%   | 0% 1%   | 1% 1%   |
52

2022 STATE OF THE PHISH  \  REPORT
B.  Working adult survey: country-by-country breakdown
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
What is phishing?
| Correct answer   | 59% | 47% | 54% 52% | 52% 62% | 49% 53% |
| ---------------- | --- | --- | ------- | ------- | ------- |
| Incorrect answer | 21% | 29% | 29% 23% | 29% 28% | 32% 27% |
| I don’t know     | 20% | 24% | 17% 25% | 19% 10% | 19% 20% |
What is ransomware?
| Correct answer   | 49% | 27% | 26% 31% | 36% 47% | 38% 36% |
| ---------------- | --- | --- | ------- | ------- | ------- |
| Incorrect answer | 30% | 32% | 34% 28% | 21% 37% | 39% 33% |
| I don’t know     | 21% | 41% | 40% 41% | 33% 16% | 23% 31% |
What is malware?
| Correct answer   | 69% | 63% | 56% 52% | 73% 71% | 61% 63% |
| ---------------- | --- | --- | ------- | ------- | ------- |
| Incorrect answer | 17% | 21% | 26% 10% | 17% 21% | 26% 20% |
| I don’t know     | 14% | 16% | 18% 38% | 10% 8%  | 13% 17% |
What is smishing?
| Correct answer   | 23% | 24% | 25% 17% | 27% 24% | 24% 23% |
| ---------------- | --- | --- | ------- | ------- | ------- |
| Incorrect answer | 26% | 27% | 34% 27% | 30% 41% | 37% 32% |
| I don’t know     | 51% | 49% | 41% 56% | 43% 35% | 39% 45% |
What is vishing?
| Correct answer   | 26% | 17% | 24% 22% | 26% 27% | 25% 24% |
| ---------------- | --- | --- | ------- | ------- | ------- |
| Incorrect answer | 23% | 29% | 39% 22% | 31% 35% | 38% 31% |
| I don’t know     | 51% | 54% | 37% 56% | 43% 38% | 37% 45% |
53

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
Understanding of email
An email can appear to come from someone other than the person or company who sent it.
| True         | 79% | 71% | 81% 68% | 76% 82% | 81% 77% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 11% | 14% | 9% 13%  | 14% 11% | 11% 12% |
| I’m not sure | 10% | 15% | 10% 19% | 10% 7%  | 8% 11%  |
If an email includes logos and contact information from a familiar brand, I know it’s safe.
| True         | 32% | 28% | 32% 19% | 34% 28% | 42% 31% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 52% | 53% | 49% 63% | 48% 59% | 42% 52% |
| I’m not sure | 16% | 19% | 19% 18% | 18% 13% | 16% 17% |
Email attachments can be infected with software that can damage my computer.
| True         | 84% | 78% | 85% 78% | 83% 83% | 79% 81% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 9%  | 11% | 7% 10%  | 10% 10% | 12% 10% |
| I’m not sure | 7%  | 11% | 8% 12%  | 7% 7%   | 9% 9%   |
All internal emails (like those I exchange with coworkers) are safe.
| True         | 48% | 52% | 54% 21% | 59% 48% | 50% 47% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 36% | 29% | 29% 59% | 28% 39% | 34% 36% |
| I’m not sure | 16% | 19% | 17% 20% | 13% 13% | 16% 16% |
If a link in an email takes me to a file that’s stored in a reputable cloud service (like Office 365, Google Drive, or Dropbox), I know that file is
safe.
| True         | 28% | 35% | 32% 27% | 44% 29% | 46% 35% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 42% | 34% | 35% 42% | 30% 46% | 32% 37% |
| I’m not sure | 30% | 31% | 33% 31% | 26% 25% | 22% 28% |
If I have exchanged multiple emails with someone, I know that is a safe contact.
| True         | 45% | 52% | 49% 28% | 57% 46% | 50% 47% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 40% | 33% | 31% 49% | 31% 42% | 34% 37% |
| I’m not sure | 15% | 15% | 20% 23% | 12% 12% | 16% 16% |
I should be cautious of any unexpected emails.
| True         | 88% | 81% | 85% 89% | 90% 88% | 85% 86% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 5%  | 13% | 7% 6%   | 5% 8%   | 9% 8%   |
| I’m not sure | 7%  | 6%  | 8% 5%   | 5% 4%   | 6% 6%   |
My organization’s security tools will automatically block all suspicious/dangerous emails.
| True         | 49% | 46% | 55% 43% | 57% 45% | 49% 49% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 35% | 32% | 23% 28% | 23% 38% | 32% 30% |
| I’m not sure | 16% | 22% | 22% 29% | 20% 17% | 18% 21% |
My personal email provider will automatically block all suspicious dangerous emails.
| True         | 38% | 37% | 49% 43% | 49% 36% | 45% 43% |
| ------------ | --- | --- | ------- | ------- | ------- |
| False        | 47% | 39% | 35% 31% | 31% 49% | 38% 38% |
| I’m not sure | 15% | 24% | 16% 26% | 20% 15% | 17% 19% |
54

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
Has the pandemic impacted where you currently work?
Yes, now work remotely full time 30% 11% 12% 10% 16% 26% 33% 20%
Yes, now work remotely part time and  27% 21% 25% 23% 27% 30% 16% 24%
on site part time
Yes, now work on site full time 10% 13% 14% 24% 10% 14% 15% 14%
I was working remotely, but I don’t  3% 8% 4% 6% 12% 4% 7% 6%
anymore
My work location hasn’t changed 30% 47% 45% 37% 35% 26% 29% 36%
Which of the following applies to your home Wi-Fi network? (Multiple responses allowed.)
I have changed the default name of my  23% 22% 37% 16% 28% 21% 34% 26%
wireless network
My wireless network is password  61% 50% 69% 44% 69% 68% 61% 60%
protected
I have changed my wireless network’s  22% 21% 34% 22% 28% 19% 32% 26%
default password
I have changed my wireless router’s  23% 10% 32% 19% 22% 20% 24% 22%
default password
I have checked for software updates to  18% 10% 23% 19% 14% 16% 24% 18%
my wireless router
I currently haven’t done anything like  8% 15% 6% 25% 8% 8% 7% 11%
this for my Wi-Fi network
| I don’t have a home W-Fi network | 4%  | 3%  | 2% 6% | 1% 1% | 3% 3% |
| -------------------------------- | --- | --- | ----- | ----- | ----- |
| I’m not sure                     | 9%  | 11% | 3% 9% | 1% 5% | 5% 6% |
You have not taken some/all of the Wi-Fi security actions noted. Why?
I am not worried about my home Wi-Fi  65% 64% 65% 57% 54% 62% 68% 62%
network
I don’t know how to change these  30% 34% 31% 38% 41% 36% 29% 34%
settings
Other, please specify (see the body of  5% 2% 4% 5% 5% 2% 3% 4%
the report for common write-in reasons)
Which of these PERSONAL devices do you use for work-related purposes? (Multiple responses allowed.)
| Phone/smartphone | 56% | 43% | 50% 54% | 59% 50% | 64% 54% |
| ---------------- | --- | --- | ------- | ------- | ------- |
| Laptop computer  | 39% | 31% | 34% 37% | 42% 33% | 41% 37% |
| Desktop computer | 25% | 21% | 26% 20% | 27% 20% | 27% 24% |
| Tablet           | 20% | 17% | 24% 17% | 26% 21% | 30% 22% |
| None of these    | 23% | 32% | 29% 31% | 20% 29% | 19% 26% |
Which of these EMPLOYER-ISSUED devices to you use for work? (Multiple responses allowed.)
| Phone/smartphone | 31% | 38% | 40% 36% | 46% 36% | 45% 39% |
| ---------------- | --- | --- | ------- | ------- | ------- |
| Laptop computer  | 45% | 36% | 40% 42% | 41% 51% | 43% 43% |
| Desktop computer | 29% | 27% | 33% 25% | 31% 29% | 34% 30% |
| Tablet           | 18% | 15% | 22% 14% | 22% 22% | 29% 20% |
| None of these    | 28% | 29% | 27% 32% | 26% 20% | 24% 27% |
55

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain UK | U.S. Average  |
| --- | --------- | ------ | ------------- | -------- | ------------- |
Which of these personal activities you do on your employer-issued device? (Multiple responses allowed.)
Check/respond to personal email 50% 39% 32% 37% 51% 40% 47% 42%
| View/post to social media    | 26% | 23% | 22% 29% | 35% 26% | 39% 29% |
| ---------------------------- | --- | --- | ------- | ------- | ------- |
| Stream media (music, videos) | 26% | 24% | 24% 20% | 35% 25% | 42% 28% |
| Shop online                  | 35% | 30% | 33% 20% | 39% 31% | 40% 32% |
| Read news stories            | 44% | 34% | 36% 44% | 48% 38% | 36% 40% |
Research (new products, travel) 41% 30% 31% 42% 41% 34% 38% 37%
| Play games    | 19% | 27% | 27% 11% | 25% 22% | 34% 23% |
| ------------- | --- | --- | ------- | ------- | ------- |
| None of these | 21% | 22% | 28% 25% | 20% 24% | 17% 23% |
Which of these activities do you allow friends/family to do on your employer-issued device? (Multiple responses allowed.)
| Check/respond to email          | 19% | 18% | 22% 20% | 34% 20% | 30% 23% |
| ------------------------------- | --- | --- | ------- | ------- | ------- |
| View/post to social media       | 13% | 14% | 17% 18% | 29% 16% | 26% 19% |
| Stream media (music, videos)    | 19% | 14% | 18% 13% | 28% 16% | 28% 20% |
| Shop online                     | 22% | 19% | 27% 13% | 36% 20% | 34% 24% |
| Read news stories               | 20% | 18% | 20% 25% | 38% 19% | 24% 23% |
| Research/complete homework      | 19% | 19% | 15% 24% | 26% 18% | 23% 21% |
| Play games                      | 14% | 19% | 20% 10% | 22% 19% | 26% 19% |
| Not sure how they use my device | 4%  | 5%  | 6% 3%   | 4% 4%   | 3% 4%   |
| None of these                   | 52% | 44% | 44% 51% | 31% 49% | 39% 44% |
How do you currently manage your passwords for your PERSONAL online accounts?
| Logins saved in a browser | 25% | 22% | 19% 31% | 23% 21% | 36% 25% |
| ------------------------- | --- | --- | ------- | ------- | ------- |
| Use password manager      | 20% | 15% | 20% 17% | 21% 26% | 23% 20% |
Manually enter a unique password for  27% 32% 34% 16% 30% 29% 22% 27%
every account
Manually enter and rotate 1 to 4  14% 13% 14% 16% 14% 14% 10% 14%
passwords across accounts
| Manually enter and rotate 5 to 10  | 8%  | 8%  | 7% 8% | 7% 5% | 4% 7% |
| ---------------------------------- | --- | --- | ----- | ----- | ----- |
passwords across accounts
Manually enter and rotate more than 10  6% 10% 6% 12% 5% 5% 5% 7%
passwords
How do you currently manage your passwords for your WORK-RELATED online accounts?
| Logins saved in a browser | 20% | 22% | 16% 27% | 26% 16% | 33% 23% |
| ------------------------- | --- | --- | ------- | ------- | ------- |
| Use password manager      | 20% | 18% | 20% 19% | 22% 27% | 21% 21% |
Manually enter a unique password for  32% 32% 38% 19% 28% 33% 27% 30%
every account
Manually enter and rotate 1 to 4  14% 14% 14% 16% 16% 13% 8% 14%
passwords across accounts
| Manually enter and rotate 5 to 10  | 5%  | 7%  | 7% 7% | 5% 6% | 6% 6% |
| ---------------------------------- | --- | --- | ----- | ----- | ----- |
passwords across accounts
Manually enter and rotate more than 10  9% 7% 5% 12% 3% 5% 5% 6%
passwords
56

2022 STATE OF THE PHISH \ REPORT
Global
Australia France Germany Japan Spain UK U.S. Average
In 2021, did you receive any of the following? (Multiple responses allowed.)
An email from a sender who 17% 20% 20% 13% 19% 17% 22% 18%
impersonated someone I know
An email from a sender who 33% 31% 25% 27% 32% 29% 26% 29%
impersonated another person/
organization
An email that impersonated your 16% 12% 18% 12% 14% 15% 18% 15%
current organization
An email that contained an 44% 32% 40% 33% 49% 35% 39% 39%
untrustworthy attachment
Suspicious text messages on your 51% 36% 33% 24% 39% 42% 41% 38%
phone/smartphone
Suspicious messages on social media 24% 24% 24% 22% 34% 24% 33% 27%
Suspicious messages in a work-related 12% 17% 14% 17% 20% 14% 19% 16%
messaging app
Suspicious phone calls or voicemails 53% 29% 32% 23% 39% 34% 46% 37%
No, I didn’t receive any of these 13% 18% 17% 29% 9% 15% 15% 17%
In 2021, did you do any of the following? (Multiple responses allowed.)
Clicked a link in an email that led to a 16% 18% 16% 10% 23% 20% 26% 19%
fake website
Accidentally compromised an account 5% 10% 10% 7% 14% 12% 17% 11%
password
Accidentally downloaded malware from 9% 14% 14% 7% 18% 11% 19% 13%
a dangerous email or website
Clicked a link in a direct message that 9% 14% 16% 10% 17% 12% 22% 14%
downloaded malware
Gave personal information to a 11% 13% 13% 6% 11% 12% 18% 12%
scammer or impostor
No, I did not do any of these 69% 54% 56% 75% 50% 58% 45% 58%
In 2021, did you experience any of the following? (Multiple responses allowed.)
Some hacked into one or more of your 8% 13% 17% 7% 13% 14% 22% 14%
social media accounts
Someone duplicated one or more 8% 13% 13% 9% 14% 10% 18% 12%
social media profiles and tried to
impersonate you
Identity theft 7% 8% 13% 8% 10% 10% 19% 11%
A ransomware infection that led to 8% 9% 10% 6% 11% 11% 17% 10%
paying money to regain access to
personal files/device
Financial loss due to a fraud committed 11% 15% 10% 6% 12% 12% 18% 12%
against you
No, I did not experience any of these 73% 61% 59% 76% 62% 64% 48% 63%
57

2022 STATE OF THE PHISH  \  REPORT
Global
|     | Australia | France | Germany Japan | Spain | UK U.S. | Average  |
| --- | --------- | ------ | ------------- | ----- | ------- | -------- |
Cybersecurity for my organization is:
| Not a priority      | 2%  | 4%  | 4% 5%   | 2%  | 2% 5%   | 3%  |
| ------------------- | --- | --- | ------- | --- | ------- | --- |
| Low priority        | 5%  | 9%  | 5% 10%  | 4%  | 8% 7%   | 7%  |
| Somewhat a priority | 18% | 18% | 14% 21% | 18% | 19% 14% | 18% |
| Priority            | 25% | 30% | 19% 25% | 21% | 21% 21% | 23% |
| High priority       | 44% | 31% | 53% 21% | 53% | 46% 45% | 42% |
| I’m not sure        | 6%  | 8%  | 5% 18%  | 2%  | 4% 8%   | 7%  |
Cybersecurity for me is:
| Not a priority      | 1%  | 3%  | 3% 3%   | <1% | 1% 4%   | 2%  |
| ------------------- | --- | --- | ------- | --- | ------- | --- |
| Low priority        | 5%  | 7%  | 3% 9%   | 3%  | 7% 7%   | 6%  |
| Somewhat a priority | 21% | 19% | 14% 24% | 17% | 21% 17% | 19% |
| Priority            | 30% | 38% | 26% 28% | 26% | 31% 27% | 29% |
| High priority       | 40% | 30% | 52% 22% | 53% | 39% 42% | 40% |
| I’m not sure        | 3%  | 3%  | 2% 14%  | <1% | 1% 3%   | 4%  |
You mentioned cybersecurity is a low priority or not a priority for you. Why?
My organization/IT team will take care  10% 14% 33% 17% 12% 18% 27% 19%
of any security needs or mistakes I
make
I don’t interact with devices often  28% 27% 17% 24% 12% 21% 24% 22%
enough to be worried
| I’ve never experienced any  | 31% | 24% | 33% 31% | 44% | 32% 27% | 32% |
| --------------------------- | --- | --- | ------- | --- | ------- | --- |
cybersecurity issues, so I don’t need to
prioritize it
My job isn’t high-level enough for me to  31% 35% 17% 25% 32% 29% 22% 27%
be a target for cyberattackers
| Other | 0%  | 0%  | 0% 3% | 0%  | 0% 0% | <1% |
| ----- | --- | --- | ----- | --- | ----- | --- |
If you have a cybersecurity issue with a work device, how confident are you that your IT team can identify and address that issue
without your involvement?
| Not at all confident | 3%  | 11% | 4% 11%  | 4%  | 3% 4%   | 6%  |
| -------------------- | --- | --- | ------- | --- | ------- | --- |
| Not confident        | 6%  | 17% | 10% 17% | 17% | 11% 7%  | 12% |
| Neutral              | 24% | 32% | 36% 44% | 23% | 21% 26% | 30% |
| Confident            | 45% | 26% | 36% 23% | 47% | 47% 37% | 37% |
| Extremely confident  | 22% | 14% | 14% 5%  | 9%  | 18% 26% | 15% |
58

2022 STATE OF THE PHISH  \  REPORT
C.  Industry failure rates by simulated phishing template style
As was the case last year, users across all industries struggled to identify and avoid attachment-based phishing tests in 2021.
But even the highest average failure rates—including mining’s 36%—didn’t have much influence on overall industry failure
rates. It’s further proof of something discussed in Section 4: that attachment-based tests are not frequently used in many
organizations.
As we cautioned in the main report, an overall average failure rate is a general view; it cannot reveal more specific areas of
risk. Susceptibility to attachment-based phishing attacks could be a hidden issue for many organizations. Regular testing
and training about these types of threats could prove beneficial.
Average Failure Rate
|                     | Link-Based   | Attachment-Based   | Data Entry-Based   |         |
| ------------------- | ------------ | ------------------ | ------------------ | ------- |
| Industry            | Tests        | Tests              | Tests              | Overall |
| Aerospace           | 11%          | 18%                | 4%                 | 12%     |
| Agriculture         | 13%          | 18%                | 7%                 | 12%     |
| Automotive          | 9%           | 15%                | 3%                 | 8%      |
| Business Services   | 12%          | 29%                | 4%                 | 12%     |
| Construction        | 12%          | 21%                | 5%                 | 12%     |
| Consulting          | 14%          | 25%                | 6%                 | 14%     |
| Education           | 11%          | 17%                | 4%                 | 10%     |
| Electronics         | 9%           | 17%                | 3%                 | 8%      |
| Energy/Utilities    | 10%          | 20%                | 4%                 | 10%     |
| Engineering         | 8%           | 18%                | 4%                 | 8%      |
| Entertainment/Media | 10%          | 19%                | 5%                 | 9%      |
| Financial Services  | 10%          | 17%                | 3%                 | 9%      |
| Food & Beverages    | 13%          | 17%                | 3%                 | 11%     |
| Government          | 12%          | 14%                | 4%                 | 11%     |
| Healthcare          | 10%          | 26%                | 4%                 | 10%     |
| Hospitality/Leisure | 9%           | 29%                | 4%                 | 10%     |
| Insurance           | 13%          | 20%                | 4%                 | 11%     |
| Legal               | 12%          | 18%                | 6%                 | 11%     |
| Manufacturing       | 11%          | 20%                | 4%                 | 10%     |
| Mining              | 11%          | 36%                | 5%                 | 12%     |
| Real Estate         | 11%          | 23%                | 6%                 | 12%     |
| Retail              | 12%          | 23%                | 5%                 | 11%     |
| Technology          | 14%          | 25%                | 4%                 | 12%     |
| Telecommunications  | 13%          | 21%                | 7%                 | 12%     |
| Transportation      | 14%          | 15%                | 5%                 | 11%     |
59

2022 STATE OF THE PHISH \ REPORT
LEARN MORE
Test your current security awareness program with our free People Risk Assessment.
You’ll get visibility into your users’ cybersecurity knowledge and vulnerability. It covers critical cybersecurity topics such as
phishing, visit passwords, data protection and more. proofpoint.com/us/people-risk-assessment
ABOUT PROOFPOINT
Proofpoint, Inc. is a leading cybersecurity and compliance company that protects organizations’ greatest assets and biggest risks: their people. With an integrated suite of cloud-based solutions,
Proofpoint helps companies around the world stop targeted threats, safeguard their data and make their users more resilient against cyber attacks. Leading organizations of all sizes, including more than
half of the Fortune 1000, rely on Proofpoint for people-centric security and compliance solutions that mitigate their most critical risks across email, the cloud, social media and the web. More information is
available at www.proofpoint.com.
©Proofpoint, Inc. Proofpoint is a trademark of Proofpoint, Inc. in the United States and other countries. All other trademarks contained herein are property of their respective owners. Proofpoint.com
0400-007-01-01 01/22

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-14", "model": "gemini-3.5-flash-lite"} -->
