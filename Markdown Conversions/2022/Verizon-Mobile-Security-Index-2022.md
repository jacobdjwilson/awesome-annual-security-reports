# Verizon Mobile Security Index 2022

## Table of Contents
- [About This Report](#about-this-report)
  - [Who Should Read This Report?](#who-should-read-this-report)
- [Original Report Table of Contents](#original-report-table-of-contents)
- [Executive Summary / Foreword](#executive-summary--foreword)
  - [Attacks Are Up—Losses Too](#attacks-are-up-losses-too)
  - [Changing Working Practices Are a Challenge](#changing-working-practices-are-a-challenge)
  - [Companies Are More Reliant on Mobile Devices](#companies-are-more-reliant-on-mobile-devices)
  - [Security Spend Is Rising in Response](#security-spend-is-rising-in-response)
- [1. Introduction](#1-introduction)
  - [Mobile Is Now Critical](#mobile-is-now-critical)
  - [Everywhere, All the Time](#everywhere-all-the-time)
  - [Success Brings Unwanted Attention](#success-brings-unwanted-attention)
  - [The Severity of Attacks Has Grown](#the-severity-of-attacks-has-grown)
  - [Security Spend](#security-spend)
- [2. Bring Your Own Dangers](#2-bring-your-own-dangers)
  - [Bring Your Own Office](#bring-your-own-office)
  - [Bring Your Own Device (BYOD)](#bring-your-own-device-byod)
  - [Bring Your Own Applications](#bring-your-own-applications)
  - [How to Secure BYOD Devices](#how-to-secure-byod-devices)
  - [Work Profiles](#work-profiles)
  - [Training and Acceptable Use Policies](#training-and-acceptable-use-policies)
  - [How to Work from Home, Securely](#how-to-work-from-home-securely)
- [3. Threats and Defenses](#3-threats-and-defenses)
  - [3.1 Users and Behaviors](#31-users-and-behaviors)
    - [Passwords](#passwords)
    - [Phishing](#phishing)
    - [Types of Phishing](#types-of-phishing)
    - [A Little Learning Can Be a Dangerous Thing](#a-little-learning-can-be-a-dangerous-thing)
    - [Complacency Can Be Dangerous](#complacency-can-be-dangerous)
    - [Phishing and Mobile Devices](#phishing-and-mobile-devices)
    - [Inappropriate Content](#inappropriate-content)
    - [The Great Exfiltration](#the-great-exfiltration)
    - [How to Secure Against Phishing](#how-to-secure-against-phishing)
    - [How to Create an Effective Incident Reporting Process](#how-to-create-an-effective-incident-reporting-process)

---

## About This Report

In April 2022, we commissioned an independent market research company to survey more than 600 people responsible for security strategy, policy and management. We also surveyed security practitioners and interviewed nine C-level experts in the field. And again this year we worked with several leaders in mobile device security: Absolute, Check Point, IBM, Ivanti, Jamf, Lookout, Netskope, Proofpoint and Thales. These contributors provided additional information, including incident and usage data.

We’d like to thank all our contributors for helping us to present a more complete picture of the threats that affect mobile devices and what is being done to mitigate them. This report wouldn’t be possible without them.

For more information on our methodology, see page 61.

### Who Should Read This Report?

We produced this fifth annual Verizon Mobile Security Index to help security professionals, like chief information security officers (CISOs), assess their organization’s mobile security environment and calibrate their defenses. While the report is packed with detail, there’s also lots of information that would be interesting—and extremely relevant—to anybody involved in the specification, procurement or management of IT devices and services.

---

## Original Report Table of Contents

| Foreword | 3 | 3. Threats and defenses | 24 | 4. Zero Trust | 55 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Attacks are up—losses too. | 4 | 3.1 Users and behaviors | 25 | Zero Trust network access | 56 |
| Changing working practices is a challenge. | 5 | Passwords | 26 | A continuous Zero Trust mindset | 57 |
| Companies are more reliant on mobile devices. | 6 | Phishing | 28 | Conclusion | 58 |
| Security spend is rising in response. | 7 | Inappropriate content | 33 | | |
| | | The great exfiltrations | 34 | 5. Appendices | 59 |
| 1. Introduction | 8 | How to secure against phishing | 35 | Terminology used in this report | 60 |
| Mobile is now critical. | 9 | How to create an effective incident reporting process | 36 | Survey methodology | 61 |
| Everywhere, all the time | 9 | 3.2 Apps | 37 | Contributors | 62 |
| Success brings unwanted attention. | 13 | App permissions | 38 | | |
| The severity of attacks has grown. | 13 | Malware | 39 | | |
| Security spend | 14 | Ransomware | 40 | | |
| | | Mobile ransomware | 43 | | |
| 2. Bring your own dangers | 16 | How to secure apps | 44 | | |
| Bring your own office | 17 | 3.3 Devices and things | 45 | | |
| Bring your own device (BYOD) | 19 | Lost or stolen devices | 46 | | |
| Bring your own applications | 19 | Device management | 46 | | |
| How to secure BYOD devices | 19 | Check Point: The case for UEM | 47 | | |
| Training and acceptable use policies | 21 | The dangers of things | 48 | | |
| How to work from home, securely | 23 | How to secure IoT devices | 49 | | |
| | | 3.4 Networks and clouds | 50 | | |
| | | Public Wi-Fi | 51 | | |
| | | Home Wi-Fi | 52 | | |

---

## Executive Summary / Foreword

In 2021, America experienced an unprecedented increase in cyberattacks and malicious cyber activity. Normally, the legal team would never let us say something as bold as that; they’d want evidence for such a dramatic statement. But those words are verbatim from the opening of the FBI’s 2021 Internet Crime Report.[^1]

And our research found that compromises that were known to involve a mobile device followed this trend—in fact, the growth in the number of companies affected was higher.

### Attacks Are Up—Losses Too

> **45%**  
> Close to half of the companies that we surveyed said they had suffered a compromise involving a mobile device in the past 12 months. Companies with a global presence were even more likely to have been affected. More than three in five (61%) had been hit, compared to 43% of organizations with only a local presence.

![Figure 1: Percentage of respondents that admitted their company suffered a compromise which involved a mobile device and led to the loss of data or downtime from 2018 to 2022, showing a 14% CAGR reaching 45% in 2022. [n=601, 671, 876, 856, 632]]

In 2021, the FBI’s Internet Crime Complaint Center (IC3) team received a record 847,376 complaints—a 7% increase from 2020. The estimated potential losses were over $6.9 billion.[^1] Unsurprisingly, ransomware, business email compromise (BEC) and the criminal use of cryptocurrency were among the most commonly reported types of incident.

### Changing Working Practices Are a Challenge

According to a survey by Proofpoint, 64% of people have changed where they work. Changes driven by the pandemic have stuck. Sixty-eight percent of those surveyed have started working from home either full time or some of the time.[^2]

IT organizations did a stellar job enabling millions of people to work from home on short notice. New security approaches and tools mean that employees working from home can be just as secure as those working from the office. And managing a mix of remote, home, hybrid and office-based employees doesn’t need to be any more difficult either.

But companies are still struggling. Almost four-fifths of respondents agreed that recent changes to working practices had adversely affected their organization’s cybersecurity.

> **79%**  
> Almost four-fifths of respondents agreed that recent changes to working practices had adversely affected their organization’s cybersecurity.

> **22%**  
> Over a fifth (22%) of IT leaders in an Absolute study said that their primary reason for wanting employees to work from the office is to maintain a better corporate security posture.[^3]

Almost two in three CISOs across all regions agree that remote working makes their organization more vulnerable to cyberattack.

### Companies Are More Reliant on Mobile Devices

Companies are increasingly reliant on mobile devices. This is partly driven by the shift toward more hybrid working, but there are several other factors too. For many, mobile devices are no longer a secondary device.

- **58%**: We have more users using mobile devices than 12 months ago.
- **59%**: Mobile users are doing more with the devices than 12 months ago.
- **53%**: Mobile devices have access to more sensitive data than a year ago.

Many employees now have access to much of the same data—customer lists, banking details, employees’ personal data, billing information, etc.—and systems—messaging, enterprise resource planning (ERP), etc.—via their mobile devices as they would sitting at a desktop in the office. This means that the compromise of a mobile device can now pose a significant risk to customer data, intellectual property and core systems.

> **13%**  
> Only one in eight respondents said they had few (less than 10% of their workforce) people working from home or following a hybrid working model.

### Security Spend Is Rising in Response

Over three-quarters (77%) of respondents said that their security spend had increased in the preceding year. More than a fifth said that it had increased significantly.

![Figure 2: Year-over-year change in security spend showing proportions for Increased significantly, Increased, Not changed, Decreased, and Decreased significantly. [n=632]]

![Figure 3: Factors that respondents said drove the increase in security spend that they have seen in the preceding 12 months, including More devices, Greater awareness of threats, Increased remote working/working from home, More users, More apps/doing more things, and Increased threats. [n=626]]

---

## 1. Introduction

Whereas traditionally technology got a foothold in the enterprise and then trickled down to consumers, it was consumers that drove the growth of what we then called smartphones. Fifteen years ago, around when the first edition of the Verizon Data Breach Investigations Report (DBIR) was being written, most home computers were large boxes with separate monitors and keyboards. These devices were pretty rudimentary compared with what we’re used to today, but at the time they were game changing. Now you could have a device in your pocket that enables you to access the web, send and receive emails, and more.

### Mobile Is Now Critical

It’s worth remembering that one of the early successes in the mobile device field was BlackBerry, and specifically BlackBerry Enterprise Server. The first thing that springs to mind when most people think of BlackBerry is the physical keyboard. But looking back, what’s really interesting about BlackBerry is that security was central to how it was designed.

However, Blackberry’s dominance, driven by enterprise users, was quickly overwhelmed by consumer-friendly devices from the likes of Apple. And that’s when people started having better technology at home than at work. Executives around the world started putting pressure on IT teams to give them devices for work that were as user friendly as their personal devices. And it wasn’t just hardware, it was apps too.

Today, few people even use the phrase “mobile phone”—unless you’re well over 40, anyway—and laptops have become the norm. And it’s not just the hardware that’s changed, what we do with it has exploded.

Mobile devices are now critical to how we work. With increased capabilities and expansive connectivity, we now have access to far more information and tools than we ever did in the days of desktops and personal digital assistants (PDAs). Partly driven by the growth in cloud-based applications, a smaller screen no longer means less powerful.

> **85%**  
> The vast majority of respondents said that flexibility in where they work and what devices they can use will be important to attracting the best new talent.

![Figure 4: Responses to the question "How critical are mobile devices to the smooth running of your organization?" on a 10-point scale. [n=632]]

When asked how critical, on a ten-point scale, mobile devices were to the smooth running of their organization, 91% of respondents in our survey answered seven or above—and 78% answered eight or higher. The picture was very similar regardless of company operations (local, regional or global) and company size (small, medium or enterprise size). The difference was no more than two percentage points up or down.

![Figure 5: What proportion of your organization’s staff work from each of these locations most (80% or more) of the time? Showing breakdowns for: On the road (including at a customer site), A company-owned/managed site (office, store, etc.), Home, and Hybrid. [n=632]]

### Everywhere, All the Time

Fifteen years ago when we wrote about mobility, we often talked about the new ability to work from anywhere at any time. Marketers came up with all kinds of clever phrases, like “Make work an activity, not a location.”

Obviously, the COVID-19 pandemic had a dramatic impact on working practices. But it didn’t create the trend toward more flexible working, it just accelerated it. On average, about two-fifths (40%) of employees work from the office most of the time (80% or more). About the same percentage (41%) work from home or “on the road” most of the time.

There is a downside. For many people, “any time, anywhere” has evolved into “everywhere, all the time.” Sometimes, it’s employers putting expectations on employees to be contactable outside, often way outside, working hours. In some cases, it’s employees themselves slipping into the habit of checking messages, and more, at all hours of the day. It’s easy to find ways to justify it to yourself: “This project is important,” “I’d rather know now than worry about it all night,” and countless more.

Prior to 2016, employers in France were able to dismiss employees for failing to respond to out-of-hours messages—and some did. Then the French government passed a law giving workers the right to disconnect.[^5] Since then, Ireland, Italy and Spain have enacted similar legislation. The province of Ontario is considering enacting a similar law.

> **Assembly of Ontario: Schedule 2 Employment Standards Act 2000**  
> The Schedule amends the *Employment Standards Act, 2000*. The new Part VII.01 of the Act imposes a requirement on employers that employ 25 or more employees to have a written policy with respect to disconnecting from work. The term “disconnecting from work” is defined to mean not engaging in work-related communications, including emails, telephone calls or the sending or reviewing of other messages, so as to be free from the performance of work.[^6]  
> _— Figure 7. Extract from Working for Workers Act, 2021 in the Legislative Assembly of Ontario._

![Figure 6: Reasons why employees feel unable to “disconnect” from work, including: Too much to do during usual hours, Manager contacts me, Coworkers contact me, I’m required to be on call, I’m self-employed, and Other. Data from LifeWorks. [^4]]

Working excessive hours can affect mental health. LifeWorks found that the 21% of workers who disagreed with the statement “I am typically able to disconnect from work after usual work hours” had a Mental Health Index score 4.8 points lower than those that were able to switch off.[^7]

![Figure 8: Global Mental Health Index score by month over time from April 2020 to March 2022. Data from LifeWorks. [^8]]

This is more than an interesting aside; there is a direct connection with cybersecurity. In previous editions, we’ve discussed why mobile phones can make it harder to spot an attack like a phishing email. Tired or distracted employees are also more likely to tap on something that they shouldn’t.

Imagine two scenarios:

| Scenario 1 | Scenario 2 |
| :--- | :--- |
| It’s mid-morning and you’re sitting at your desk in the office. An email drops into your inbox. You double-click it and start reading.<br><br>You’ve just taken a training course about phishing, so you’re a bit suspicious. But the email includes some personal information, looks professional and has no obvious giveaways like bad grammar.<br><br>**What do you do?**<br>• Hover over the button and check the actual URL in the status bar<br>• Expand the message header and check the sender’s address<br>• Close the email and decide to review later<br>• Flag the email as spam/suspicious<br>• Click the button | It’s late. You’ve been out for the evening and had a couple of beers. You’re in a cab on your way home when your phone buzzes in your pocket. You tap on the notification and the email opens up.<br><br>You’ve just taken a training course about phishing, so you’re a bit suspicious. But the email includes some personal information, looks professional and has no obvious giveaways like bad grammar.<br><br>**What do you do?**<br>• Close the email and decide to review later<br>• Flag the email as spam/suspicious<br>• Click the button |

> **62%**  
> Nearly two-thirds of cyberattacks attributed to insiders were assessed to be due to negligence rather than malicious intent.[^9]

### Success Brings Unwanted Attention

Now that mobile is so critical to business operations, it’s getting more attention from bad actors too. From coordinated state-sponsored campaigns to unfocused, opportunistic criminal exploits, the volume of attacks is going up. Whether the attacker is a well-trained and well-resourced professional or an amateur taking advantage of the many commercially available exploits, mobile devices are an attractive target.

![Figure 9: Reported incidents and losses, based on FBI data from 2017 to 2021, displaying Losses ($B) and Complaints (thousands). [^10]]

Despite this, we still get respondents saying that mobile devices are of less interest to cybercriminals than other IT assets—36% in our latest survey, up from 30% in our 2021 report.

### The Severity of Attacks Has Grown

As mentioned earlier, 45% of respondents said that their organization had been subject to a security incident involving a mobile device that led to data loss, downtime or other negative outcome.

Of those respondents, 73% described the impact of the attack as major, and over two-fifths (42%) said that it had lasting repercussions. That’s up from our previous report, where less than half of incidents were described as major, and just 28% were said to have had lasting repercussions.

> **46%**  
> Nearly half of SMBs that had suffered a mobile-related compromise said that the impact was major and that it had lasting repercussions.

However, the 2021 data was a bit of an anomaly—wonder why? This year’s severity figures show a return to the level we’ve seen since we started producing the Mobile Security Index, just a little higher. Of course, with a lot more respondents saying that their company had experienced a mobile-related compromise, this means a lot more companies are facing major, and lasting, consequences.

![Figure 10: Prevalence and severity of mobile-related compromises from 2018 to 2022 showing percentages for Compromised, Major, and Lasting repercussions. [n=601, 671, 876, 856, 632]]

> **73%**  
> Nearly three-quarters of respondents from small and medium-sized businesses said that they perceived the risk as significant or high—compared to “just” 60% of those from larger organizations.

### Security Spend

These factors help explain why 77% of respondents said that their cybersecurity budget had increased in the previous 12 months—that’s up from 65% in the previous edition of this report—and close to a third (29%) of those said it had increased significantly.

> **77%**  
> Over three-quarters of respondents said that their cybersecurity budget had increased in the previous 12 months.

And respondents expect their budgets to grow again. Over three-quarters said that they expected their budget to grow in the following 12 months; 25% said they expected it to increase significantly. Just 1% expected their budget to decrease.

> **77%**  
> Over three-quarters of respondents said that they expect their cybersecurity budget to increase in the coming 12 months.

> **67%**  
> Over two-thirds said that spend had increased in the previous 12 months and they expected it to rise again in the next 12 months.

Of course, growing budgets sounds like good news for CISOs, but what really matters is whether that budget is sufficient to meet needs—especially when needs are growing as we’ve discussed.

Four out of five (80%) of our respondents said that they expected their budget to be adequate to do the job.

The most common objective for security spend was increasing the security of existing user activities. That’s not as obvious a statement as it might seem at first glance. With so many new hybrid workers and the continuous stream of new applications and capabilities, you might expect that the focus would be on securing new things, but apparently a lot of companies know that they have much to do to secure existing activities.

In the past, companies focused their spend on Protect activities, as defined by the National Institute of Standards and Technology (NIST) Cybersecurity Framework. But our research found that companies are now spending more evenly across the five NIST categories. This is a very encouraging sign.

![Figure 11: Objectives for cybersecurity spend, showing share of companies prioritizing: Increasing security of existing user activities, Integrating management of phones, tablets and laptops, Enabling new services to remote workers, Reducing burden on the IT team (e.g., automating tasks), and Reducing inconvenience to users and increasing productivity. [n=632]]

![Figure 12: Respondents' estimated breakdown of security spend by NIST category: Identify (18%), Protect (23%), Detect (16%), Respond (18%), Recover (17%), and Other (7%). [n=632]]

- **40%**: According to a report by Thales, two-fifths of organizations are not confident that their current security systems could effectively secure remote work.[^11]
- **67%**: Over two-thirds of respondents agreed that companies only take cybersecurity seriously enough after they have been compromised.
- **85%**: The vast majority of companies said that they have a defined budget for mobile security.

---

## 2. Bring Your Own Dangers

Working patterns were changing long before we all learned what a coronavirus is. But the COVID-19 crisis catalyzed dramatic changes in expectations, for both employers and employees. These new behaviors have brought new challenges and threats with them.

### Bring Your Own Office

How many times have you seen a “look what I just received” post on LinkedIn? Somebody has just started a new job and received a new laptop, monitor and bunch of logo’d swag—typically including a water bottle and a mousepad. That’s what onboarding has looked like for a lot of people over the last couple of years.

As working from home has become more commonplace, people have invested in building a more comfortable place to work. There’s been a boom in loft and garage conversions, or if you’re really lucky maybe you splashed out on a “shed quarters” at the bottom of the garden.

> Over half of CISOs across all regions agree that targeted attacks on their organizations have increased since adopting mass hybrid working. Small organizations seem more affected, with 59% of companies with 500 or fewer employees saying their workforce has been targeted more since they implemented hybrid working. At the other end of the scale, only 48% of enterprises (5,000 employees and above) agree.[^12]

Many of you reading this report will be seasoned remote workers. But recent events have created millions of new home and hybrid workers. Despite this, many companies haven’t provided employees with clear guidance on what’s expected.

![Figure 13: Biggest challenges to managing risk and compliance under “work from anywhere” policy: Right tools and technologies (54%), Right processes and policies (28%), Right people and culture (18%). Data from Absolute. [^13]]

> **79%**  
> According to Thales, nearly four in five organizations are still “somewhat” or “very concerned” about the security risks and threats that a greatly increased remote workforce poses.[^14]

### Bring Your Own Device (BYOD)

The number of companies that said that they allow employees to use their own devices dropped since the previous edition of this report. But in that report, over half of the 70% of companies with a BYOD policy said that they’d adopted it during lockdown. It seems likely that some will have done so only as a temporary measure and rescinded it because it didn’t suit their company culture, caused security problems or proved to be unpopular.

Securing BYOD devices can be considerably more difficult than securing company-owned ones with a mobile device management (MDM) solution in place. Rigorous policies and thorough enforcement will be required. See our discussion of Zero Trust approaches on page 56.

One challenge of securing BYOD devices is getting users to follow company policy on a device that they see as their property. Employees that receive a stipend may be more willing to countenance their employer setting rules about how they use devices and intrusions to their privacy. Over two-thirds (68%) of the respondents to our survey whose company had a BYOD program said that this included such a payment.

![Figure 14: BYOD policies, current and under consideration. Allow employees to access email on their own phones/tablets: 60% (31% considering). Allow employees to use their own phones/tablets to access corporate systems and data (BYOD): 41% (41% considering). Allow employees to use their own laptops for work-related tasks (BYOPC): 50% (35% considering). [n=623]]

### Bring Your Own Applications

It’s not just devices that people bring into the business. News reports have brought to light incidents of officials—both in the U.S. and the U.K.—using encrypted messaging apps like WhatsApp and Telegram to carry out government business. And it’s not just in the public sector. It’s been reported that major organizations have let people go for using unauthorized messaging apps. In 2021, one of these, a major bank, was fined $200 million for insufficient monitoring and record keeping associated with employees using unapproved messaging apps.

No matter what security measures you put in place, you can’t stop an employee using an app like this on a personal device to conduct business conversations. And if they do, it’s a lot harder, even impossible, to spot phishing attacks and sensitive data being sent outside the company. It could also have serious compliance implications.

This underlines the importance of making sure that security measures aren’t too intrusive and that users understand why they are in place. The more draconian and arbitrary security measures seem, the more likely users are to try and find ways around them.

### How to Secure BYOD Devices

These recommendations are structured around the five functions in the NIST Cybersecurity Framework. To find out more, visit [nist.gov/cyberframework](https://www.nist.gov/cyberframework).

![NIST Cybersecurity Framework Cycle: Identify, Protect, Detect, Respond, Recover]

#### Identify
- Develop a detailed BYOD policy that clearly lists responsibilities in plain language—this may involve translating it into local languages.

#### Protect
- Educate users on the importance of managing the permissions granted to apps—users often aren’t aware of how some permissions can be exploited for nefarious purposes.
- Implement an MDM solution to help remotely secure, manage and support personally owned devices.
- Consider restricting what resources devices not controlled by the company can access.
- Ensure that users understand the importance of keeping the operating system (OS) and apps up to date.
- Educate users on the dangers of malware and how to reduce the risks—malware can obviate protections like containerization.
- Consider implementing a Zero Trust approach; this can reduce the reliance on end users making informed and security-conscious decisions—see page 56 for more details.

#### Detect
- Consider introducing endpoint detection and response (EDR); this uses behavioral-based analysis to provide threat protection and can provide valuable insight.
- Consider implementing data loss prevention (DLP) to detect and block the exfiltration of information.
- Give users an authorized—and easy-to-use—means to share files outside the company.

#### Respond
- Make sure that your team has the training—or the third-party support—to handle greater device variety.
- Make sure that staff know what to do if a device is lost or stolen, or they spot something suspicious—this should be part of your general security policy, but it’s worth reiterating here.
- Make reporting concerns easy—it shouldn’t be something people have to look up—and remember, the employee might not be able to access company systems when reporting an issue.

#### Recover
- Use mobile threat defense (MTD) combined with unified endpoint management (UEM) to help bring devices that are out of compliance back into line through self-remediation.
- Develop a clear policy, in consultation with your legal team, that covers the tricky issues around performing digital forensics on an employee-owned device.

---

### Work Profiles

#### Non-remote workers
*Employees that work inside a company-controlled environment, the perimeter, like an office, store or plant.*

##### Back office
- **Commuters / Office-bound:**  
  This includes a wide range of workers, from call center staff to lawyers. They might be required to work from the office or choose to do so—not everybody likes or has the right conditions to work from home. These workers typically rely on a local area network (LAN) or wireless LAN (WLAN) within the perimeter. They might work from home a few times a month.

##### Front of house / Tethered
- **Floor workers:**  
  This category includes many roles in retail, hospitality, manufacturing, etc. These workers aren’t fixed to a desk, but their location doesn’t change much. They are more likely to use a specialized device. They will rarely use a network not controlled by the company.
- **Corridor warriors:**  
  Employees that are never at their desks, but their roaming is mainly limited to one of the company’s sites. They primarily use the company’s WLAN.

#### Remote workers
*Employees that operate outside the perimeter, whether on the road or at home.*

##### Omniworkers
- **Home workers:**  
  People based at home or who work from home a lot. This label can apply to a wide variety of roles. They typically use home Wi-Fi, perhaps with a virtual private network (VPN).
- **Flexible workers:**  
  Employees that work from home a few days a week—there are all kinds of reasons why. They commonly use home Wi-Fi, perhaps with a VPN.

##### Nomads
- **Road warriors:**  
  These are the classic “remote workers:” sales people, consultants, CxOs of big companies, etc. They need to be able to work from multiple locations and work on the move. They have complex requirements and use multiple types of networks. They are likely to need to use third-party Wi-Fi and cellular connectivity.
- **Field workers:**  
  Another well-established category. It includes roles like service engineers. People in this group often need to use custom apps and work on the move—so cellular connectivity is key. Their primary device may be a customized or ruggedized device.

---

### Training and Acceptable Use Policies

#### Lack of Clarity on Expectations
Some behavior is clearly unacceptable, such as accessing adult, extreme or illegal content on company devices. This could not only damage your organization’s reputation, this type of behavior could put your company at risk. But there are many gray areas in defining appropriate use, especially when it comes to mobile devices. What if employees want to use their work devices to check personal emails, stream music or scroll through social media? Many people think this is a reasonable allowance in a flexible, modern workplace.

> **79%**  
> Nearly four-fifths (79%) of people admitted to using a work device for a personal task, such as checking personal email, shopping or streaming.[^16]

> **48%**  
> Nearly half of respondents said their organization didn’t have an acceptable use policy in place.

![Figure 15: Personal tasks carried out on work devices, by device "owner" and user's friends/family (Personal email, Online shopping, Social media, Gaming). Data from Proofpoint. [^15]]

Part of the problem is that many companies struggle to develop an effective acceptable use policy (AUP)—48% didn’t have one at all, an improvement from 57% in our last report. Defining what counts as misuse of a work device can be tricky, especially if your employees need to access social media and other content to do their jobs, but creating clear guidance, including rules for mobile-specific content, is crucial for helping prevent misuse.

Plus, with many employees now working from home, the lines are blurred even further.

#### Lack of Training
Many companies set high expectations on their employees but don’t give them sufficient training to meet those standards.

- **44%**: Don’t give employees security training on a regular basis.
- **51%**: Don’t give employees security training when their working arrangements change (e.g., start working from home).

#### Lack of Remote Working Guidance
We’ve seen a massive shift in working practices—even if only temporary for some people—yet less than half of companies said that they have given employees training on how that affects cybersecurity.

- **64%**: We have guidelines on what are suitable locations for remote working (e.g., home is okay, coffee shop isn’t).
- **47%**: We issue guidance on maintaining privacy when working remotely (e.g., when working in a shared apartment).

It’s not our place to say how companies should manage abuse, but we advocate creating a positive security culture. Creating a blame-free environment is likely to encourage employees to report suspicious activity and mistakes that they may make—enabling the organization to mitigate the damage.

---

### How to Work from Home, Securely
#### A Guide for Users

#### Reduce Risky Behavior
- Read and understand your company’s policies. Ask for further guidance on anything you’re unsure about.
- Try to keep your private and work life separate.
- Consider where you keep work devices and any sensitive data—are these stored safely when not in use?
- Make sure that you’ve set a password or PIN—or enabled Touch ID where applicable—for access.
- Configure your devices to lock automatically after a few minutes of inactivity.
- Create a unique strong password for each account, including email and web applications.
- Turn on two-factor authentication wherever possible.
- Think about who can see or hear what you are saying or typing on your screen.
- Sign up to newsletters from trusted organizations to improve your cybersecurity skills and knowledge.

#### Manage Your Apps
- Be careful what apps you install on your devices, especially when those devices have access to corporate resources.
- Make sure you understand your company’s AUP and any other restrictions that may be in place.
- Install updates promptly—it can be a bother, but failing to do so could put your device, and the company, at risk.
- Be frugal with which permissions you give apps. Consult company policies on what to limit on which apps.

#### Secure Your Devices
- Don’t share devices—you may be allowed to perform personal tasks, but that doesn’t apply to your friends and family.
- As with apps, install OS updates when asked to do so.
- If you lose a device, or it gets stolen—these things happen—report it immediately.

#### Be Smart About Networks
- Change the default password on your home router—and any smart home devices connected to it.
- Set up separate Wi-Fi networks for smart home devices, visitors and work use—many wireless access points include this functionality in the admin console.
- If your company provides a VPN, use it.
- Be wary of public Wi-Fi networks—even ones associated with brands you know and trust.

---

## 3. Threats and Defenses

### 3.1 Users and Behaviors

Whether they’re deliberately breaking policy or inadvertently opening up vulnerabilities, users are a threat. Social engineering remains one of the most powerful tools in the cybercriminal’s arsenal. And attackers are finding increasingly innovative ways to exploit and manipulate users.

The human element continues to drive breaches. Over four-fifths (82%) of breaches analyzed for the 2022 DBIR involved the human element. Whether it is the use of stolen credentials, phishing, misuse or simply an error, people continue to play a very large role in incidents and breaches alike.[^17]

> **44%**  
> Over two-fifths (44%) of those that had suffered a mobile-related security breach said that user behavior was a contributing factor. Those in the manufacturing sector were most likely to list this as a factor, 57%.

#### Passwords

Yup, passwords again. Despite the thousands of articles about the importance of passwords, the sad fact is that many attackers don’t hack into systems. They log in. And users make it easy for them.

> *The sad fact is that many attackers don’t hack into systems. They log in.*

Long, complex passwords can be a pain on a device with a keyboard, even more so on a small screen with a virtual keyboard—and don’t get us started on trying to enter a strong password on a smart TV! But it’s critically important as attackers have many tools and techniques at their disposal.

Attackers exploit a range of social and technical vulnerabilities to steal or crack credentials:
- **They guess:** Publicly available information such as name, date of birth and relatives’ names provide a head start.
- **They trick people into revealing them:** Social engineering, including phishing and old-fashioned scamming, can be very effective.
- **They “credential stuff:”** This involves using usernames and passwords leaked from data breaches on other sites; this exploits people’s tendency to reuse passwords.
- **They “password spray:”** This involves simply trying some of the most commonly used passwords across a huge number of sites.
- **They use “brute force:”** This is automated guessing, but the easy availability of large amounts of computing power and techniques honed over many years make it a more powerful technique than you might think.
- **They “shoulder surf:”** Which is exactly what it sounds like—it might also include reading the sticky notes stuck around a monitor.
- **They exploit network vulnerabilities:** This can enable them to intercept passwords when users log in.
- **They use a keylogger:** This enables them to capture a record of every keypress a user makes.

These and other techniques are widely documented on the web—you can even download tools to help.

For years, vendors have foretold the imminent demise of passwords, but each year it seems like we need more passwords rather than fewer. Password managers and alternatives like fingerprint scanning can help, but for the foreseeable future it’s important to make sure that employees understand what makes a strong password.

Remember that poor password practices at home can be a threat to the business. If a user uses the same password across multiple accounts, this could increase the risk of a successful credential stuffing attack.

Authentication is a fundamental component of a Zero Trust approach to mobile device security; see page 56.

> ##### What makes a password strong? LUCID.
> We, security professionals that is, often talk about password strength, but how many users actually know what that means?
> 
> - **Long:** With passwords, it’s all about entropy, and length is one of the key components. A simple (mix of upper- and lowercase letters) 8-character password would take about 22 minutes to crack; a 12-character one, 300 years.
> - **Unique:** Don’t reuse passwords. We can’t stress this enough. Password stuffing is popular with hackers because it works.
> - **Complex:** Complexity is the other component of entropy. Throw a “special character” into that 12-character password and the time to crack leaps to 400,000 years.
> - **Impersonal:** Brute-force attacks can be smarter than they sound. Hackers can use social engineering to make more educated guesses. That’s why it’s a bad idea to include any personal information in a password. A password with the same entropy as “Cassie%12032005” would take 5,000,000,000 years to crack, but it would be a lot easier for a hacker that read about your daughter Cassandra’s birthday on Facebook.
> - **Different:** Yes, that’s the same as unique, but it’s that important a point.

---

#### Phishing

Another old “favorite.” We’ve been writing this report for five years and phishing has been a major topic every year. Our colleagues who create the Verizon DBIR have been covering the rise of phishing attacks for 15 years.

Despite the prevalence of phishing attacks over many years, a large number of employees are unable to correctly define the term. As we’ve discussed in previous editions of this report, email is not the only place where we see phishing attacks, and attackers continue to innovate, so let’s start by getting our definitions straight.

![Figure 16: Share of working adults able to correctly define “phishing”: Correct (53%), Incorrect (27%), Don't know (20%). [^18]]

> **83%**  
> In 2021, five out of six organizations experienced a successful email-based phishing attack in which a user was tricked into risky action, such as clicking a bad link, downloading malware, providing credentials or executing a wire transfer. That’s a huge increase from 2020, when the number was “just” 46%.[^19]

---

#### Types of Phishing

| Name | Description | Means | Scale | Common intent |
| :--- | :--- | :--- | :--- | :--- |
| **Bulk phishing** | The most familiar type of phishing, commonly used in both business and consumer environments. Research from Proofpoint shows that many major brands are seen in bulk phishing attacks. | Email, in-game chat, etc. | Big, unfocused. It’s all about the numbers. Success rates are low, but send out enough messages and somebody will click or tap. | Get the target to click on a link, either to capture credentials or get additional biographical information or payment details. |
| **Smishing** | Similar to bulk phishing, but using text messages. A common recent example is the “You have a parcel” message. | SMS | Big, unfocused. | Get the target to click on a link or respond with sensitive details. |
| **Vishing** | Many, though not all, users have learned to be suspicious of emails. But a phone call must be legit, right? It’s still relatively rare, but deepfake technology has been used to go a step further and actually impersonate key individuals. As artificial intelligence/machine learning (AI/ML) becomes more accessible, this may increase. | Phone calls or voice messages | Small, targeted—for now. The nature of these attacks is often like bulk phishing, but they are labor-intensive, so they are often focused on high-value targets, making them more like whaling attacks. | Get the target to visit a website through which malware is then deployed, give information over the phone or allow the attacker to take over control of the device—the “support scam” is a common version of this. |
| **Spear phishing** | Spear phishing is to organically fed, free-range chicken as bulk phishing is to factory farming. Instead of going for the widest audience possible, attackers focus on a specific company and tailor the approach to increase the chances of success. | Email | Small, targeted. | Sometimes part of a concerted information-gathering campaign to help gain access to accounts, often a direct attack with the goal of financial enrichment. |
| **Whaling** | Also called business email compromise (BEC), whaling targets high-level employees. The difference between whaling and spear phishing is that whaling exclusively targets those in the highest echelons of the organization. | Email | Small, targeted. | Financial theft, wire transfer fraud, credential extraction. |

> **$2.4 B**  
> According to the FBI, BEC schemes in the U.S. resulted in 19,954 complaints in 2021, with losses estimated at nearly $2.4 billion. The amount of money lost through BEC scams continues to grow, with identified global exposed losses increasing 65% between July 2019 and December 2021.[^20]

---

#### A Little Learning Can Be a Dangerous Thing

We often talk about the need for users to be more alert, wise to “obvious” signs of attacks. This is probably most common when it comes to phishing. Surely users can spot a phishing email—they are all full of typos, have bad grammar and fit into a standard pattern, like “Your account has been compromised” or “You’ve been chosen to receive millions.”

But what about the opposite hypothesis? In the U.K., there was a series of campaigns aimed at teaching children about the dangers of strangers. There were TV ads, lessons in school and more. Some years later, it was discovered that all this effort had an unintended consequence. It had made kids confident that they could spot a dangerous stranger: They looked like the one in the ads—a man in a gray trench coat with a bag of sweets. The problem with that was it left many thinking that anybody not meeting that specific model wasn’t a threat—surely a woman wasn’t dangerous?

Is the same happening with phishing awareness? Are users falling into a false sense of security? Phishing attacks come in many forms; attackers are constantly adapting their technique. And, as we discussed in the previous edition of this report, perpetrators are very quick to respond to current events, like COVID-19.

It’s important to teach users that not only do attacks come via different channels, they can take many different forms. A reasonably informed user would be suspicious of a message from a Nigerian prince, regardless of whether it came by email, SMS or Facebook. But what about a message about a parcel held up waiting additional address information—especially if they were waiting for a parcel or it was around their birthday or other gift-giving occasion? And what about a “fun” quiz that involves answering questions about your childhood and favorite things?

> **I wish more people did these. It's fun to learn odd little things:**  
> First job - **Stop**  
> Current job - **Sending**  
> Dream job - **Your**  
> Favorite food - **Potential**  
> Favorite dog - **Passwords**  
> Favorite footwear - **Or**  
> Favorite chocolate bar - **Memorable**  
> Favorite ice cream - **Data**  
> Your vehicle color - **To**  
> Favorite holiday - **People**  
> Night owl or earlybird - **Who**  
> Favorite day of the week - **Collect**  
> Tattoos - **This**  
> Favorite color - **For**  
> Do you like vegetables - **Social**  
> Do you wear glasses - **Engineering**  

Going back to our opening discussion, mobile phones have broken down the barriers. We don’t separate work and leisure the way that we used to. What if instead of your regular social media site, it was a business-related message, and it asked about the city where you went to school, what your first job was, etc.? And what if it arrived after a long day, maybe as you were enjoying a beer and watching TV?

> **18%**  
> of clicked phishing emails come from a mobile device.[^21]

---

#### Complacency Can Be Dangerous

Right now you might be thinking “what idiots,” but not everybody is a cybersecurity specialist and most of us like to think that most people are pretty decent. A lot also think that the people who do understand security are so far ahead of them that they must be able to outwit the bad guys. Nearly half of respondents in a Proofpoint study said that they thought their organization’s safety measures would prevent any dangerous emails getting as far as their inbox.

- **49%**: Nearly half of global users thought that their organization’s safety measures would prevent any dangerous emails from getting through to their inbox.[^22]
- **43%**: More than two-fifths thought that their personal email provider would stop any dangerous emails getting through to their account.[^23]
- **53%**: More than half of people encountered an unsafe link while using a mobile device during the third quarter of 2021.[^24]

---

#### Phishing and Mobile Devices

Attackers will take advantage of any opportunity to make their phishing attacks more successful. The design of apps on mobile devices can, unintentionally, make phishing harder to detect, helping attackers to get past people’s normal defenses.

Cybercriminals have become adept at designing campaigns to take advantage of the nature of mobile devices and users facing numerous distractions.

##### Why phishing campaigns are harder to spot on mobile devices:
- The smaller screen and aspects of user-interface design make it harder to evaluate the legitimacy of an email or website:
  - The URL is truncated and hard to read
  - The URL disappears on scrolling to make room for more content
  - You can’t hover over a link to check the destination before tapping
- Users are more likely to check email on a mobile device when on the move, surrounded by distractions

> *“Attackers continue to produce ever more convincing phishing sites and increasingly target mobile users. Our research shows that as many as one in ten mobile users click on the links in phishing emails.”*  
> — **Michael Covington, Ph.D.**, VP Portfolio Strategy, Jamf

Zimperium conducted an analysis of more than 500,000 phishing websites over a two-and-a-half-year period. It found that the share of sites that specifically targeted mobile devices and delivered content tailored for the mobile format rose from just under half in the first quarter of 2019 to over three-quarters during the last quarter of 2021.[^25]

![Figure 17: Share of phishing sites specifically designed for mobile from Q1 2019 to Q4 2021, rising from under 50% to over 75%. [^26]]

Why does phishing remain so prevalent? Because it works. Despite the proliferation of attacks and increased awareness, research suggests that the success rate of phishing campaigns is going up.

![Figure 18: Change in success of phishing attacks over a 12-month period from June 2021 to May 2022. Data provided by Jamf. [^27]]

---

#### Inappropriate Content

It might seem hard to believe that anybody would watch porn during the working day, but it happens. We know because there have been highly publicized cases, including a well-known journalist and a member of the U.K. Parliament. In the latter case, at least one incident was in a shared space. A couple of anecdotes don’t mean much, but the data shows that it’s not an uncommon problem.

Increased working from home could actually be responsible for accessing inappropriate content becoming a bigger problem. Devoid of the constant presence of others, employees may visit websites that they wouldn’t when in the office. Maybe not adult content, but what about gaming or gambling sites? Or other non-work-related sites, such as social media or online shopping?

##### Are adult websites more dangerous?
It might be awkward to talk about, but porn exists. And it’s popular. There are two adult websites in the top 10 by visitor count. They get billions of visitors each month—far more than sites like netflix.com. But surely that’s all outside of office hours? Wrong, Pornhub reports a peak in traffic around 4 PM each day.[^28]

We were unable to find any evidence that adult sites were any more likely to be infected or exploited to spread malware, but there are a couple of factors that could make these sites more of a risk.

Firstly, users may be more willing to hand over personal information—perhaps for age verification—than they would on, say, a news site. This could be exploited for social engineering. But, far more worryingly, it’s reasonable to assume that users would be much less likely to report that their device is suffering adverse effects after visiting adult sites.

![Figure 19: Most popular websites by number of visits during April 2022 (in billions): youtube.com, google.com, facebook.com, wikipedia.org, pornhub.com, xvideos.com, twitter.com, reddit.com, amazon.com, instagram.com. Data from Semrush. [^29]]

---

#### The Great Exfiltration

Much has been written about the “great resignation.”[^30] There’s much debate about whether it’s a real phenomenon, and which age groups and industries are affected. While it may not be the global exodus that some have suggested, some companies have definitely seen a spike in exits.

What’s that got to do with mobile security? Well, according to research by Lookout, when leaving a job, about one in six employees uses a personal instance of a cloud storage app to take company data with them.[^31]

Netskope studied departing employees and found that between 2020 and 2021, 29% of them downloaded more files from managed corporate app instances and 15% of users uploaded more files to personal app instances in their final 30 days than usual. Of the users who uploaded more files, half uploaded more than 5x the normal volume, 8% uploaded 100x more and 1% uploaded 1,000x more.[^32]

Mobile devices, working from home and cloud-based apps can all make this easier. This underscores the importance of having good reporting and monitoring tools. A data-loss prevention tool could also help to prevent this.

> **16%**  
> When leaving a job, about one in six employees uses a personal instance of a cloud storage app to take company data with them.[^33]

![Figure 20: Increase in volume of data uploaded to a personal cloud service in the 30 days prior to leaving the company (showing jumps from >5x, 10x, 100x, up to 1,000x). Data provided by Netskope. [^34]]

---

#### How to Secure Against Phishing

These recommendations are structured around the five functions in the NIST Cybersecurity Framework. To find out more, visit [nist.gov/cyberframework](https://www.nist.gov/cyberframework).

![NIST Cybersecurity Framework Cycle: Identify, Protect, Detect, Respond, Recover]

##### Identify
- Identify the very attacked people (VAPs) in your organization—these aren’t always the VIPs—and provide them with additional awareness training.
- Carry out “real world” attack simulations that mimic the sort of interactions employees have regularly.

##### Protect
- Carry out regular employee training and attack simulations so that employees, especially VAPs, know the signs and how to avoid becoming the weakest point.
- Make sure that your phishing training and simulations aren’t limited to email.
- Implement controls to verify requests for changes in account information—this could be as simple as sending a confirmation message before changes come into force.
- Use a web isolation solution to restrict suspicious and unverified URLs to a protected container, like a sandbox—consider using this to isolate personal activity, like shopping and checking personal email, too.

##### Detect
- Implement a solution that blocks inbound email threats before they reach employees’ inboxes.
- Use an MTD solution to help detect and block phishing attempts however they are instigated.
- Set devices to allow full email addresses and URLs to be viewed.
- Configure your mail system to flag emails from outside your domain—many companies add a prefix, like [E], to the subject line.

##### Respond
- Create an incident response (IR) plan—44% of respondents to our survey, down from 51% in 2021, said their organization didn’t have one.
- Take a copy of the email (complete with headers) and ensure that all logs are retained.
- Search email logs to identify everybody that may have received the message and notify them.
- Where necessary, terminate live sessions, lock accounts and force password changes.
- Update your email filters to block similar messages in the future.

##### Recover
- Show employees examples of actual attacks the company has faced to show that the danger is real.
- Remind employees about their obligation to read and follow the company’s acceptable use policy.
- Use MTD and UEM to help bring non-compliant devices back into line through self-remediation.

---

#### How to Create an Effective Incident Reporting Process

Penalizing employees for security mistakes is now quite common. For example, according to a Proofpoint study, more than half (55%) of organizations “discipline or punish” employees that fall for phishing emails—including ones sent by the company as part of a simulation. A further 18% were considering implementing such a policy. That number was even higher in the U.K. (77% + 15%) and Australia (78% + 15%).

![Figure: Penalties for security mistakes - statistics and breakdown]

1. **Keep it simple:** It’s important to capture enough details to enable the infosec team to take action, but keep it simple for the user. Avoid jargon and complex terminology.
2. **Define multiple workflows:** Different types of incidents will need different responses. An incident reporting system should allow multiple escalation paths and then route incident reports to the correct path.

---

## References

[^1]: FBI, *2021 Internet Crime Report*, 2021.
[^2]: Proofpoint, *2022 State of the Phish*, 2022.
[^3]: Absolute, *The Future of Work*, 2022.
[^4]: LifeWorks, *The Mental Health Index by LifeWorks*, 2022.
[^5]: Légifrance, *Partie législative (Articles L1 à L8331-1)*, 2017.
[^6]: Legislative Assembly of Ontario, *Bill 27, Working for Workers Act, 2021*, 2021.
[^7]: LifeWorks, *The Mental Health Index by LifeWorks*, 2022.
[^8]: LifeWorks, *The Mental Health Index by LifeWorks*, 2022.
[^9]: Ponemon, *2020 Ponemon Cost of Insider Threats Global Report*, 2020.
[^10]: FBI, *2021 Internet Crime Report*, 2021.
[^11]: Thales, *2022 Thales Data Threat Report*, 2022.
[^12]: Proofpoint, *2022 Voice of the CISO*, 2022.
[^13]: Absolute, *The Future of Work*, 2022.
[^14]: Thales, *2022 Thales Data Threat Report*, 2022.
[^15]: Proofpoint, *2022 State of the Phish*, 2022.
[^16]: Proofpoint, *2022 State of the Phish*, 2022.
[^17]: Verizon, *Data Breach Investigations Report*, 2022.
[^18]: Proofpoint, *2022 State of the Phish*, 2022.
[^19]: Proofpoint, *2022 State of the Phish*, 2022.
[^20]: FBI, *2021 Internet Crime Report*, 2021.
[^21]: Verizon, *2022 Data Breach Investigations Report*, [verizon.com/dbir](https://www.verizon.com/dbir).
[^22]: Proofpoint, *2022 State of the Phish*, 2022.
[^23]: Proofpoint, *2022 State of the Phish*, 2022.
[^24]: Lookout, *Predictions 2022: Five Threats That Will Impact Your Personal Data and Privacy*, 2022.
[^25]: Zimperium, *2022 Global Mobile Threat Report*, 2022.
[^26]: Zimperium, *2022 Global Mobile Threat Report*, 2022.
[^27]: Jamf, data provided, May 2022.
[^28]: Pornhub, *2021 Year in Review*, 2021.
[^29]: Semrush, *Most Visited Websites by Traffic in the world for all categories, April 2022*, 2022.
[^30]: Bloomberg, *How to Quit Your Job in the Great Post-Pandemic Resignation Boom*, 2021.
[^31]: Lookout, data supplied, May 2022.
[^32]: Netskope, *Cloud and Threat Report - January 2022 Edition*, 2022.
[^33]: Netskope, *Cloud and Threat Report - January 2022 Edition*, 2022.
[^34]: Netskope, *Cloud and Threat Report - January 2022 Edition*, 2022.

---

h based
6%).35 on type, severity, location and other Meeting with manager or
relevant factors. infosec team
Consequences ranged from mandatory
training or a meeting with the infosec Ideally, these paths should be easy to
team all the way up to termination. configure so that administrators can 52%
keep them up to date as new threats
Users should not be worried about emerge and organizational
reporting potential security issues. changes happen.
By creating an easy, blame-free way
to report incidents, you can make 3. Leverage automation.
Negative mark on
employees become part of your early Automated systems that send alerts performance review
warning system against cyberattacks. to the right people can help speed
response and mitigate the damage
This can help:
caused by an incident. This doesn’t have 45%
to be a big and complex project. You
• Foster a companywide commitment
could do it using a Google Form.
to tackling cybercrime and fraud
4. Create an audit trail.
• Limit the severity of compromises—
the sooner an attack is spotted, the Obviously, the primary purpose of an Disciplinary action, such as a
more you can do to mitigate it incident reporting process is to enable written warning
employees to report incidents and
• Maintain regulatory compliance— action those reports. But the information
timeliness is increasingly part of gathered as part of this process can 31%
security frameworks and regulations be invaluable to later forensic analysis.
such as ISO27001, DPA 2018 It’s important to record everything that
and GDPR you can: What was reported, when
and by whom. Consider using existing
Follow these four steps to create an tools to record the progress of a report.
Monetary penalty
effective incident reporting process. Though not specifically designed for
the purpose, applications like Jira and
1. Make it easy.
Slack are easy to use, record a journal
15%
To be effective, an incident reporting of activity and enable you to set up
system should be easy to use. That automated notifications.
means making it easy to access—
remember the employee may not have
access to their email account, intranet,
etc., that might be part of what they Termination
need to report.
Figure 21. Penalties for falling for a phishing
email, real or simulated, reported by
respondents. Data from Proofpoint.36
35, 36 Proofpoint, 2022 State of the Phish, 2022
MMSSII 22002212 FTohrreewaotsr dand defenses 3366

3.2 Apps
The number of apps, especially web-based apps, continues to
grow apace. Malware remains a major problem, but even non-
malicious apps, including those downloaded from official stores,
can be a threat.
Nearly half of those that had
suffered a mobile-related
46%
security breach said that app
threats were a contributing
factor. Those in the energy and
utilities sector were most likely
to list this as a factor, 55%.
MSI 2022 Threats and defenses 37

App permissions
Hands up, who has ever read the terms and conditions when making a purchase
or installing an app on a mobile device? We’re guessing that there aren’t many
hands up right now.
As we’ve discussed in previous editions of this report, giving applications access
to the camera, microphone, photos, location data and other data and device
functions can be a significant security risk.
It’s very easy to just click accept, but users should be careful about applications
requesting permissions that they don’t really need. For example, according
to Jamf research, 53% of finance applications request permission to access
location data. Only 62% of navigation apps ask for the same access!
Percentage of apps per category requesting specific iOS permissions
Photos 66% 78% 69% 63% 65% 79% 71% 49% 68% 53% 50% 62% 96% 75% 87% 84% 67% 52% 65%
Camera 60% 75% 54% 54% 58% 74% 56% 44% 68% 39% 48% 43% 90% 70% 83% 83% 54% 52% 61%
Location 58% 63% 42% 57% 53% 81% 61% 43% 66% 46% 62% 61% 68% 47% 81% 72% 64% 60% 55%
Microphone 34% 44% 40% 40% 24% 32% 15% 19% 36% 41% 21% 41% 64% 44% 33% 69% 21% 20% 38%
Calendar 29% 28% 22% 38% 18% 31% 56% 23% 31% 36% 27% 31% 18% 23% 26% 35% 41% 33% 25%
Contacts 27% 37% 19% 20% 36% 46% 9% 15% 31% 13% 22% 21% 44% 37% 37% 59% 20% 27% 26%
Bluetooth 25% 26% 21% 39% 17% 42% 18% 23% 29% 35% 22% 25% 31% 22% 25% 26% 31% 20% 26%
Voice
processing 9% 14% 15% 3% 9% 10% 2% 7% 8% 7% 6% 3% 8% 12% 13% 18% 5% 7% 9%
Health 2% 1% 1% 1% 1% 3% 2% 23% 3% 1% 1% 1% 0% 1% 1% 1% 4% 1% 1%
Local
network 1% 1% 1% 1% 0% 0% 0% 0% 1% 0% 0% 0% 1% 1% 0% 2% 0% 0% 1%
All Business Educatio
E
n ntertain ment Financ
F
e
ood
and drink G
H
a
e
m
a
e
lt
s
h
and fitness Lifestyle Music Navigation N
P
e
h
w
o
s
to
and video Productivity Sho
S
p
o
p
c
in
ia
g
l
net working Sports Travel Utilities
Figure 22. Permissions requested by Apple iOS apps. Data from Jamf.37
37 Jamf, An Analysis of iOS App Permissions, 2021
MSI 2022 Threats and defenses 38

Malware
Lorem ipsum
The 2022 Verizon Data Breach Check Point Research recently tracked
Investigations Report found that over the development of a new form of
30% of breach cases involved some malware. “Rogue” is a form of mobile
form of malware.38 And according to remote access Trojan (MRAT) that can
Jamf, the percentage of organizations gain control over the host device and
that experienced the installation of exfiltrate data such as photos, location,
malware on a remote device doubled contacts and messages; modify the
70%
in 2021, going from 3% to 6%.38 files on the device; and download other
malicious payloads.
Over the years, one of the problems
we’ve faced when writing this report is a Rogue is particularly adept at digging in
lack of mobile-specific stats on threats and avoiding removal:
and compromises. In fact, that’s why
we started producing this report. Often, • It adopts the services of the Firebase
people will talk about the actions that platform to disguise and masquerade
attackers use, such as phishing, and the as a legitimate Google service
asset that was the eventual target, say a • Once it gets all the required
server, but not the device that provided permissions, it hides its icon to make
the opening for the attack in the it harder for the user to get rid of it Ransomware was present
first place. in almost 70% of malware
• It registers itself as a device
breaches analyzed for
As we’ve shown, attackers do design administrator; if the user tries to
the 2022 Data Breach
phishing campaigns specifically revoke this permission, they are
targeting mobile devices, and they presented with an “Are you sure to Investigations Report.39
build malware specifically for mobile wipe all the data?” dialog
devices too.
The built-in security features on some Malware comes in many forms, but in
phones and the degree of control recent years ransomware has become
associated with using official app stores, the most common.
such as Google Play, do offer some
protection. But attackers manage.
38 Jamf, Security 360 Annual Trends Report, 2022
39 Verizon, Data Breach Investigations Report, 2022
MSI 2022 Threats and defenses 39

Ransomware
You must have been hiding under a rock for the last few years if you haven’t heard 75%
about ransomware. It’s been behind some of the most high-profile compromises in
the past decade. But just in case you have been busy, here’s a quick definition.
Three-quarters of
ransomware attacks start
Ransomware is a form of malware that denies a user or
with email phishing.44
organization access to files on their computers. Files are
encrypted and a ransom demanded for the decryption key.
Ransomware is no longer limited to individual machines and
many attackers target servers or cloud services. Some
variants have added additional functionality—such as data
theft or exposure—to further incentivize victims to pay up.40
Percentage change in
In previous editions of this report, we have discussed some of the variants of renewal premiums
+28%
ransomware, including doxware. We won’t go over those again here, but we
saw a new angle during 2021.
25%
Several companies reported employees receiving emails soliciting them to become
20%
accomplices in a ransomware attack. The emails targeted users with access to
company servers and offered a substantial return if the attack was successful.
15%
10%
Think you’re covered? Think again.
5%
According to the U.S. Government Accountability Office (GAO), the percentage of
0%
companies with cyber coverage increased from 26% in 2016 to 47% in 2020.41 But
’20/Q1 ’20/Q3 ’21/Q1 ’21/Q3
insurance is no panacea. As payouts have increased,42 insurers have tightened up
policies, reduced coverage and increased premiums.43 Between 20Q1 and 21Q3, Figure 23. Increase in cyber insurance
renewal premiums increased more than 2.5-fold. Not only are premiums increasing, renewal premiums.45
the rate at which they have increased has grown.
40 Proofpoint, Stopping Ransomware Hub, 2022
41 U.S. Government Accountability Office, Cyber Insurance: Insurers and Policyholders Face Challenges in an Evolving Market, 2021
42 Fitch, Sharply Rising Cyber Insurance Claims Signal Further Risk Challenges, 2021
43 ACA Group, Cyber Insurance: Top Five Trends for 2022, 2022
44 Check Point, What is Ransomware?, 2022.
45 The Council, Commercial Property Casualty Market Index: Q3/2021, 2021
MSI 2022 Threats and defenses 40

64%
To pay or not to pay?
There are several reasons why companies choose to pay the ransom:
Nearly two-thirds of
respondents in a Proofpoint
Reduce downtime
study said that their
Downtime is costly, so paying the ransom and avoiding lengthy disruption
can look like an attractive option. organization had paid a
ransom to try and resolve a
Protect reputation ransomware incident.48
Some people may think that paying up quickly could help keep the
compromise quiet, even obviate the need to publicly admit “we’ve been
hacked” and damage customer and investor confidence.
Avoid recovery costs
The ransoms stated in some of the stories that hit the headlines can be tens
of millions, but they are usually a lot lower—21% of ransoms paid were under
$10,000.46 If the costs of bringing in the experts, replacing hardware,
rebuilding devices and servers, etc., are higher, doesn’t paying up make
business sense?
Protect privacy
Companies don’t want their dirty linen, or their data, exposed. For some,
the ransom is a more palatable loss.
But there is widespread agreement among experts that paying the ransom is a
bad idea:
• The attacker won’t send the unlock code at all—this happens quite often
• The unlock code may not work—according to a Sophos study, only 4%
that pay up get all their data back; the average was 61%47
• There are technical issues with decrypting files—this has been reported by
many users
• The attacker may demand a further payment or payments—sometimes
this is linked to not publishing the files, an attack known as doxware
Those are the selfish reasons for not paying. There’s also a social reason.
Paying up incentivizes attackers to carry out more attacks. Unfortunately,
it’s a bit like when we’re faced with a traffic jam; we wish that everybody
else would turn around and give us a clear road ahead.
There might soon be another reason not to pay up; it might be against
the law.
46, 47 Sophos, The State of Ransomware 2022, 2022.
48 Verizon, Data Breach Investigations Report, 2022
MSI 2022 Threats and defenses 41

Paying up may be illegal.
“The FBI does not advocate
paying a ransom, in part
The U.S. government has already communicated that paying up could be contrary to
existing laws intended to block the funding of groups involved in crime or terrorism. because it does not
guarantee an organization
Bills to specifically outlaw the payment of ransoms have been discussed in several will regain access to its
countries, including the U.S. On March 15, 2022, U.S. President Biden signed the
data. In some cases,
Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA) into law. It places
victims who paid a ransom
mandatory reporting obligations in connection with cybersecurity incidents on a
were never provided
broad range of private and public-sector entities operating in “critical infrastructure”
with decryption keys. In
sectors. Companies covered by the act must report “substantial” cyber incidents to
the Cybersecurity and Infrastructure Security Agency (CISA) within 72 hours. And if addition, due to flaws in the
they pay a ransom, they must report doing so within 24 hours. Similar laws are being encryption algorithms of
considered in several other countries. certain malware variants,
victims may not be able to
recover some or all of their
data even with a valid
“Companies that facilitate ransomware payments to cyber decryption key.
actors on behalf of victims, including financial institutions,
cyber insurance firms, and companies involved in digital Paying ransoms
forensics and incident response, not only encourage future emboldens criminals to
ransomware payment demands but also may risk violating target other organizations
OFAC [Office of Foreign Assets Control] regulations.”49 and provides an alluring
and lucrative enterprise to
other criminals. However,
the FBI understands that
when businesses are faced
with an inability to function,
executives will evaluate all
options to protect their
shareholders, employees,
and customers.”
—FBI50
49 U.S. Department of the Treasury, Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments, 2021
50 FBI, 2021 Internet Crime Report, 2021.
MSI 2022 Threats and defenses 42

Mobile ransomware
Ransomware has been a thorn in the side of cybersecurity teams for the past
several years. It’s not just big companies that should be concerned about
ransomware; companies of all sizes in all industries have been attacked.
And mobile devices are a common component of attacks.
The remote environment is primed for ransomware.
As organizations continue to support remote or hybrid work, they no longer have the
visibility and control they once had inside their perimeter. Attackers are exploiting this
weakness and profiting. Here are three reasons they’re able to do so:
• Most organizations now have employees working from anywhere
• These employees expect seamless access to all resources from unmanaged and
personal devices on networks outside the traditional perimeter
Hank Schless • This greatly reduces the visibility and control that security teams have and can
Senior Manager, Security Solutions make it difficult to understand risks posed by users and the devices they’re
Lookout working from
Mobile devices make it easier for attackers to phish credentials.
Attackers are always looking for ways into your infrastructure. Compromising
an employee’s credentials enables them to gain legitimate access and remain
undetected. Their primary tactic for stealing credentials is to phish employees on
mobile devices. Because phones, tablets, etc., are used for both work and personal
tasks, employees can be targeted through multiple apps such as SMS, social media
platforms and third-party messaging apps. The simplified user interfaces of a phone
or tablet hide signs of phishing and make them ripe targets for socially engineered
phishing campaigns.
VPNs enable lateral movement.
Organizations rely on VPNs to give their employees remote access to resources,
but this approach has a number of security shortcomings. First, a VPN may grant
individuals the capability to traverse to any app across your network from a single
point of entry. Second, VPNs don’t evaluate the context under which users or devices
connect. Context is necessary to detect activity that’s indicative of a compromised
account or device.
Ransomware groups now operate like businesses. There is more evidence of
organized groups carrying out scalable campaigns that increase their success rate
and enable them to reinvest in new tools and procedures. Regardless of where or how
we work, these groups continue to take advantage of vulnerable architecture to extort
money from victims. Many organizations have taken steps to protect themselves from
ransomware attacks, but attackers continue to evolve their tactics, and companies
must respond.
MMSSII 22002212 FTohrreewaotsr dand defenses 4433

How to
Recover Identify
secure apps NIST
dnopseR Framework
tcetor
P
tceteD
These recommendations are structured Identify Detect
around the five functions in the NIST
Cybersecurity Framework.
Audit company systems and processes Implement an MTD solution to quickly
To find out more, visit for vulnerabilities to malware. identify potential threats.
nist.gov/cyberframework
Subscribe to a threat intelligence Educate users on how to identify and
service to stay abreast of the latest report unexpected system behavior—
malware threats. something a user may just see as an
annoyance, like a device constantly
Conduct regular network penetration needing charging, could be an indicator
tests to identify possible vulnerabilities— of malware infection.
and act on the findings.
Monitor devices for unusual behavior—
Protect including excessive data transfer and
out-of-hours use.
Deploy anti-malware functionality to Respond
all devices.
Add content filtering to all external Identify all infected devices and
gateways to make it more difficult for physically disconnect them from
attackers to deliver malicious content the network.
to users via their web browser
and email. Suspend the login credentials of
any accounts that may have been
Where possible, prevent the use compromised.
of removable media such as USB
drives—at the very least, disable Notify all users of the compromised
auto-run functions and set up devices app and what action to take—deleting
to automatically scan removable media the app may not always be the best
for malicious content. course of action, as this could destroy
important forensic data.
Ensure that your backup policies
are effective—backups should not Recover
be connected to the computers and
networks they are backing up; for
Reset all credentials, especially those
example, store them offline.
with administrator privileges, that may
have been compromised.
Verify your backups often—an
emergency is a bad time to find
Wipe all infected devices and reinstall
out that there’s a problem.
from the OS up.
Use deny listing on external
Conduct a postmortem exercise
gateways to block access to known
to determine how the malware
malicious websites.
managed to get through and where
controls, processes and technology
fell short, and then distribute an
“after action” report.
MMSSII 22002212 FTohrreewaotsr dand defenses 4444

3.3 Devices
and things
With the volume of devices a modern enterprise relies on, keeping
them all up to date can seem like a Sisyphean task. With more and
more devices, the danger of lost or missing devices grows. But
it’s not just the quantity of devices that’s growing, the variety is
growing too. Today there are smartphones, laptops, tablets,
hybrids (like Microsoft Surface), Chromebooks, wearables and
a seemingly endless range of connected devices.
Over a third of those that had
suffered a mobile-related
46% security breach said that
device-based threats were a
contributing factor. Those in
the healthcare sector were
most likely to list this as a
factor, 47%.
MSI 2022 Threats and defenses 45

Lost or
stolen devices
People leave phones, tablets and laptops in taxis, on trains, at restaurants—the list
goes on and on. Some of these will end up in a lost-and-found box, and others will
find a new owner—or rather a new owner will find them.
One of the reasons so few organizations are worried is because loss/theft is one
of the types of attack that’s easiest to mitigate. Protections like device encryption
and remote wipe are now standard with most types of user devices and MDM.
But that doesn’t mean that companies, or their employees, are using them.
Whole-disk encryption and PIN security codes should be activated as a standard
precaution on all devices. With these simple precautions in place, even if a device
is stolen, the data it holds will be—for all intents and purposes—worthless to
the attacker.
Mobile device
management
MDM is not mobile security. MDM Encounter rate of phishing attacks on devices with/without MDM
solutions were never designed
MDM No MDM 3-month rolling average 3-month rolling average
to protect against sophisticated
cyberattacks. The purpose of 20%
these solutions have always been
management—the clue is in the name.
The security capabilities of these
15%
solutions have always been quite
limited. They can be useful in ensuring
applications are kept up to date and
some other policies are being followed.
10%
But devices are prone to threats like
phishing even with MDM in place, as
this data from Lookout shows. This
shows that the difference in encounter 5%
rate is small, and on occasion devices
with MDM even faced more attacks.
0%
20Q1 20Q2 20Q3 20Q4 21Q1 21Q2 21Q3 21Q4 22Q1
Figure 24. Incidence of phishing attacks on devices with/without MDM in place.
Data from Lookout.51
51 Lookout, data supplied, June 2022
MSI 2022 Threats and defenses 46

The case for MTD
Unified endpoint management (UEM) solutions—or their predecessors, mobile
device management (MDM) solutions—were designed to help mobilize businesses
by streamlining processes, managing device life cycles and creating a managed
workspace on smartphones and tablets. Today, UEM solutions have evolved into
consolidated solutions that work with other endpoints beyond mobile devices,
including PCs.
UEM enforces some device-level policies—such as device encryption and remote
wipe—to maintain a basic hygiene and some have a basic jailbreak/root detection
function too. But these basic features don’t provide the protection needed to
withstand even the most basic mobile malware attack. UEMs do not scan for mobile-
related threats like malicious apps, vulnerable operating systems or network-based
attacks, nor do they protect users against phishing and other social engineering
attacks. Even with a UEM solution in place, organizations remain exposed to
credential theft, data leakage or device takeover.
A mobile threat defense (MTD) solution is essential to keep corporate data on
Pete Nicoletti
mobile devices secure, protected from all attack vectors.
Field CISO
Check Point
To find out more, read the Check Point white paper, Mobile Management Solutions
Are Not Security.52
|                        | Features                      | MDM/UEM | MTD |
| ---------------------- | ----------------------------- | ------- | --- |
| UEMs do not scan for   | Device life-cycle management  | •       |     |
mobile-related threats like
|     | App management and containerization  | •   |     |
| --- | ------------------------------------ | --- | --- |
malicious apps, vulnerable
| operating systems or network- |     | •   |     |
| ----------------------------- | --- | --- | --- |
Remote access
based attacks, or protect
| users against phishing and  |     | •   | •   |
| --------------------------- | --- | --- | --- |
Conditional access
other social engineering
attacks. As a result, users and  Jailbreak/root detection  Partial •
organizations remain exposed
|     | Malicious app detection  |     | •   |
| --- | ------------------------ | --- | --- |
to credential theft, data leakage
or device takeover.
|     | Download prevention                      |     | •   |
| --- | ---------------------------------------- | --- | --- |
|     | Anti-phishing (known and unknown sites)  |     | •   |
|     | Anti-bot (blocking C&C communications)   |     | •   |
|     | Man-in-the-middle attack prevention      |     | •   |
|     | URL filtering                            |     | •   |
|     | Real-time threat intelligence            |     | •   |
52  Check Point, Mobile Management Solutions Are Not Security, 2021
| MMSSII  22002212  FTohrreewaotsr dand defenses |     |     | 4477 |
| ---------------------------------------------- | --- | --- | ---- |

The dangers
of things
One of the challenges of securing IoT projects is the lack of centralized 42%
coordination of projects. In many organizations, IoT projects are led by the lines
of business and don’t even have to follow standard security requirements.
Remember, an IoT device can be an attack vector (a weak point that can be
exploited to mount an attack), a vehicle for attacks (like a part of a botnet used
Lines of business/business
to carry out a distributed denial-of-service (DDoS) attack) or a target in its
units initiate their own
own right.
IoT projects.
59% 48% 53%
IT has oversight of all There is central coordination We have defined IoT security
IoT projects. of all IoT projects. standards that apply to
all projects.
The nature of IoT devices themselves also presents distinct challenges compared to
securing other mobile devices. These fall into three broad areas:
Variety Distance Longevity
The sheer volume and Many IoT devices are out in the In the survey for the previous
diversity of IoT devices can field. This can make them edition of this report, we found
present enormous logistical vulnerable to physical tampering that over half (54%) said that
obstacles to effective device or network attack and harder to some of their IoT devices had an
security. It doesn’t help that update or replace. Isolation can anticipated lifetime of five years
many IoT products have been also make devices vulnerable to or more—up from 36% in our
found to have extremely weak SIM theft, one of the simplest previous report. This would be
cybersecurity—including security types of attack to carry out— very old for a smartphone or
devices such as smart locks, often all that’s required is a laptop. Combined with the
doorbells and, ironically, screwdriver. All the hacker has to difficulty of updating devices,
security cameras. do is break open the connected this can make it hard to keep IoT
device, such as a smart lamppost, protected against constantly
and remove the SIM. This can evolving threats.
then be put into another device,
giving the user free calls and data
at the organization’s expense.
MSI 2022 Threats and defenses 48

How to secure
Recover Identify
IoT devices NIST
dnopseR Framework
tcetor
P
tceteD
These recommendations are structured Identify
Ensure that users developing or
around the five functions in the NIST
purchasing IoT programs work with
Cybersecurity Framework.
Thoroughly review the security before the information security team to factor
To find out more, visit you purchase anything. in the cost and resources required to
secure devices and applications.
nist.gov/cyberframework
Ask potential vendors to supply details of
Detect
their security measures, and review them
for robustness.
Use network intrusion detection tools
Protect
to monitor all traffic, incoming and
outgoing, for unusual activity and put in
place a process to handle any
Harden all devices, including
alerts promptly.
ensuring they are tamper-resistant
and tamper-evident.
Subscribe to a threat intelligence
service to get early warning of
Change all default or vendor-
emerging threats.
supplied passwords.
Analyze logs for signs of suspicious
Change all default or vendor-supplied
behavior.
passwords, really.
Integrate MTD with EDR or security
Shut down anything you don’t
incident event management (SIEM) to
need—if you’re not using a port or
help simplify monitoring and, should it
protocol, block it.
be necessary, forensic analysis
Keep devices patched—use over-the-
Respond
air (OTA) updates to help keep devices
secure, especially those in remote or
difficult-to-access locations. Put controls in place to contain the
spread of infection and prevent the
Bind SIMs to devices, limiting the attacker from gaining any additional
potential damage of SIM theft. access or access to sensitive data.
Use private, non-routable IP addresses Implement network blocks to limit an
to make it harder for attackers to attack from infecting more devices
access IoT devices. or the attacker from accessing more
critical systems.
Consider using a private cellular
network to keep devices off the Recover
public internet.
Conduct a postmortem to determine
Encrypt data in transit and at rest.
how the attack managed to get
through and where controls, processes
Create an IoT security assurance and technology fell short, and then
process that regularly analyzes IoT risk distribute an “after action” report.
data in your organization.
MMSSII 22002212 FTohrreewaotsr dand defenses 4499

3.4 Networks
and clouds
Insecure networks remain a serious threat to mobile device
security. Attackers can intercept traffic through man-in-the-
middle (MitM) attacks or lure employees into using rogue Wi-Fi
hotspots or access points. Cloud-based services are now used
for many mission-critical tasks. They are also one of the reasons
that mobile devices have become more critical to business.
52%
That brings a whole new range of problems.
“ There is a distinct imbalance between protecting a
network and attacking it, and this imbalance continues to
grow as more effective hacking resources become available
at a significantly lower cost. But without continuous
investment and commitment to cyber resilience,
organizations will be more vulnerable to cyberattacks Over half of those that had
and thus more likely to endure reputational, financial, suffered a mobile-related
operational and safety impacts.” security breach said that
network threats were a
—World Economic Forum, 202253 contributing factor. Those
in the financial services
sector were most likely to
list this as a factor, 61%.
53 World Economic Forum, Global Cybersecurity Outlook 2022, 2022.
MSI 2022 Threats and defenses 50

Public Wi-Fi
Another familiar topic. With traveling off the agenda, public Wi-Fi may not have Ah, you might say, but it’s okay as long
been on your list of most pressing issues last year, but it remains a critical issue. as you use a virtual private network.
Reports suggest that corporate travel is at less than 50% of pre-pandemic norms VPNs do offer a degree of protection,
and experts suggest that it will take years to recover—if it ever does. But the but many companies still rely on an
dangers of public Wi-Fi aren’t limited to executives jetting around the world, “honor approach.” Even among the
or even employees traveling by plane, train or automobile. informed audience that made up our
survey respondents, 8% admitted to
There’s a lot of disagreement about working models, how they have changed and not using a VPN when using public
how they may change in the future. But it’s safe to say that fewer people are now Wi-Fi. It’s quite likely that this is an
following the traditional model of commuting to the office five days a week. For a underestimate—many people will
lot of people, that means working from home a couple of days a week or more. forgive themselves the odd slipup. It’s
Maybe that includes the odd afternoon in a coffee shop for a change of scenery. highly likely that this number is much
Or whether you work from home or not, who hasn’t checked their email when higher among employees that don’t
at the mall or in a restaurant or other public place. With reliable, high-speed mobile work in cybersecurity.
internet now widely available, you might do this on a cellular connection. But
whether for performance or to avoid data caps, people still use public Wi-Fi, with
all its attendant dangers. x2
Less than a third of organizations (32%) ban the use of public Wi-Fi, and only about
half (52%) of those actually do anything to enforce that policy.
In fact, 43% of respondents working for companies that banned the use of public
In 2021, the number of devices
Wi-Fi admitted breaking the rule themselves.
connecting to a risky hotspot
per week doubled from 0.5%
Public Wi-Fi policy to 1%.54
Banned No policy Allowed
46%
0% 25% 50% 75% 100%
Nearly half of VPN clients
Blocking of public Wi-Fi
are misconfigured or
Blocked Not blocked
out of date.55
See our discussion of Zero Trust
approaches on page 56.
0% 25% 50% 75% 100%
Figure 25. Public Wi-Fi policy. [n=632]
54 Absolute, The Future of Work, 2022
55 Jamf, Security 360 Annual Trends Report, 2022.
MSI 2022 Threats and defenses 51

Home Wi-Fi
With fewer people working in the office five days a week, it’s inevitable that more
business is being done over home Wi-Fi and home broadband connections.
It’s unsurprising then that nearly four-fifths of businesses allow employees to
use their home networks.
Home Wi-Fi policy
Banned No policy Allowed
0% 25% 50% 75% 100%
Figure 26. Use of home Wi-Fi. [n=632]
While likely to be less risky than public Wi-Fi (see our 2019 report), home Wi-Fi is
still a concern. Ask yourself how many employees have:
Changed the default password on their home router?
Shared their router password with dozens of friends and family members—maybe
even neighbors?
Updated their router firmware since receiving it?
Looked at router logs for signs of intrusion?
MSI 2022 Threats and defenses 52

Proofpoint surveyed 3,500 working  Of those who hadn’t taken steps to
adults across Australia, France,  secure their home Wi-Fi, 62% said that
Germany, Japan, Spain, the U.K. and  was because they weren’t concerned
the U.S. It found that most hadn’t taken  about the security of their home
basic security measures to protect   network. Close to 90% of the rest said
it was because they didn’t know how to.
their home Wi-Fi network.56
| 82%               | 80%                  | 74%             |
| ----------------- | -------------------- | --------------- |
| never updated     | had never changed    | hadn’t changed  |
| router software/  | their router         | their Wi-Fi     |
| firmware.         | password.            | password.       |
| 74%               | 40%                  | 11%             |
| hadn’t changed    | didn’t password-     | didn’t do any   |
| their Wi-Fi       | protect their Wi-Fi. | of the above.   |
network name.
Figure 27. What measures working adults took to protect their home Wi-Fi network.
56   Proofpoint, 2022 State of the Phish, 2022
MSI 2022 Threats and defenses 53

How to secure
Recover Identify
networks NIST
dnopseR Framework
tcetor
P
tceteD
These recommendations are structured Identify Detect
around the five functions in the NIST
Cybersecurity Framework.
Remember that mobile devices could Use network intrusion detection tools
To find out more, visit provide an entry point for a wide range to monitor all traffic, incoming and
nist.gov/cyberframework of attacks; consider ways that attackers outgoing, for unusual activity and put
could disrupt operations as well as in place a process to handle any
expose data. alerts promptly.
Protect Subscribe to a threat intelligence
service to get early warning of
emerging threats.
Re-architect your network into smaller
segments, isolating the hosts and
Analyze logs for signs of suspicious
services that hold sensitive data.
behavior.
Implement a “least privilege” access
Integrate MTD with EDR or SIEM to
policy—if people don’t absolutely need
help simplify monitoring and, should it
access, they shouldn’t have it, and
be necessary, forensic analysis.
access should be revoked when no
longer required.
Respond
Secure all wireless access points;
allow only known devices to connect to Create an IR plan that covers how
corporate Wi-Fi services. to qualify and categorize incidents,
what should be done and who the
Educate users on the dangers of Wi-Fi, responsible parties are.
including rogue access points.
Recover
Consider providing users with a
fixed wireless access (FWA) device—
Conduct a postmortem to determine
sometimes called mobile broadband—
where controls, processes and
exclusively for use when working
technology fell short and then distribute
from home.
an “after action” report.
Confirm that employees chose a
Consider updating policies; at the very
home broadband solution that includes
least, remind users about your AUP
regular firmware updates to patch any
and their responsibilities.
new vulnerabilities.
Consider putting systems like MDM or
endpoint protection in place to block
the use of public Wi-Fi entirely.
Implement MTD to monitor and mitigate
the risk of MitM attack.
Consider using a cloud access security
broker (CASB) or secure web gateway
(SWG) to help secure all connections to
cloud-based systems.
MMSSII 22002212 FTohrreewaotsr dand defenses 5544

Zero Trust 4
Zero Trust network access (ZTNA) is an approach
to network security that assumes every device,
application or system that connects to your
network potentially could be compromised.
It involves granting authorized users access only
to the applications they need to perform their
jobs. It also isolates specific applications, devices
and systems to certain parts of the network and
doesn’t make the internal network visible to the
internet, which could otherwise make it easier for
hackers to infiltrate.

Zero Trust network
access
ZTNA can be an effective alternative to the traditional approach to network security,
which typically involves using a VPN to connect workers from remote locations and
implicitly trusting these connections.
A Zero Trust security approach can bolster endpoint, network and remote
work security by minimizing the company’s exposure. With this model, dozens
or potentially hundreds of devices, applications and users would not have
wide-ranging access to the company’s network or sensitive data—they could 82%
only access the systems and information to which they are authorized.
Though ZTNA can strengthen a company’s security policy and make it more
resilient, it’s also important to balance this approach with delivering a user-friendly
digital experience that helps remote employees remain productive. If employees
can’t easily access the applications and systems they need to do their work, they
may not be as productive.
It’s a delicate balance, but you can deliver a frictionless remote work experience
while also helping to keep the organization secure. For example, intelligent,
analytics-driven identity access management solutions can automate the process
A large majority of respondents
of determining when to grant a specific user access to certain applications. AI-
said that they had adopted or
driven threat detection solutions can also help your organization detect anomalies
were actively considering
or suspicious user behavior and network activity and isolate these threats before a
adopting a Zero Trust
breach occurs. This way, employees don’t have to deal with onerous authentication
requirements; they aren’t unintentionally blocked from accessing the systems they approach to security.
need to do their jobs and also aren’t given unauthorized access to sensitive data.
As companies embrace remote and hybrid work, a ZTNA model can help combat
security threats while giving employees the flexibility to work from anywhere and
on any device they choose—whether it’s their desktop, tablet or phone. With an
approach focused on verification rather than implicit trust, companies can establish
a strong security perimeter, deliver a better employee experience and remain agile
in the increasingly complex threat environment as they adapt to the future of work.
MSI 2022 Zero Trust 56

A continuous
Zero Trust mindset
The White House’s executive order (EO) highlights many specific areas of interest
for not only federal government security, but how we should be thinking about
security and network architecture everywhere.57
As the EO notes: “To keep pace with today’s dynamic and increasingly sophisticated
cyber threat environment, the Federal Government must take decisive steps to
modernize its approach to cybersecurity, including by increasing the Federal
Government’s visibility into threats, while protecting privacy and civil liberties.”
According to the EO, agency heads are required to update existing agency plans,
develop a plan to implement Zero Trust Architecture based on current NIST migration
steps, and report on progress—within 60 days of the order. This is powerful, not
least because it helps bring Zero Trust back down to earth from how over-marketed
the term has become in recent years. It helpfully frames Zero Trust in architecture
terms—something Netskope has also underscored and that we’re seeing as common
to the success of our many customers worldwide.
In a modern architecture, Zero Trust principles should be judiciously applied, adaptively
Sanjay Beri and continuously. But today, many organizations don’t have much more than isolated
Founder and CEO “Zero Trust projects” focused on networks, users, devices or isolating servers. The
Netskope main miss on most of these projects is that they are focused on application-level
access and other pieces, but not focused on the data. Architecturally, we must go
beyond access control and isolation to provide continuous Zero Trust: real-time
access and policy controls that adapt on an ongoing basis based on users, devices,
apps, threats and data context.
This data-centric approach is the only effective way to dynamically manage risk
47% across a mix of third-party applications and a remote-first workforce that needs
always-on access to cloud apps and data to stay productive. As the EO calls out in
Section 10, item K:
“Zero Trust Architecture embeds comprehensive security monitoring; granular
risk-based access controls; and system security automation in a coordinated manner
Nearly half of respondents
throughout all aspects of the infrastructure in order to focus on protecting data in
that experienced a mobile-
real-time within a dynamic threat environment. This data-centric security model
related compromise said that
allows the concept of least-privileged access to be applied for every access decision,
cloud-based systems/apps
where the answers to the questions of who, what, when, where, and how are critical
were compromised as
for appropriately allowing or denying access to resources…”
a consequence.
Proper application of Zero Trust principles is also a critical step toward Secure
Access Service Edge (SASE) architecture. SASE isn’t specifically mentioned in the
EO, but as the order explains, applying Zero Trust at an architectural level means
“a set of system design principles, and a coordinated cybersecurity and system
management strategy based on an acknowledgment that threats exist both inside
and outside traditional network boundaries.” In other words—and crucial to SASE—
yesterday’s security and network technologies and designs won’t even start to
address the prevalence of cloud-delivered threats or attacker abuse of cloud
apps, or the increasingly acute need for security and networking teams to more
effectively converge and collaborate.
57 The White House, Executive Order on Improving the Nation’s Cybersecurity, 2021
MMSSII 22002212 FZoerreow Torrudst 5577

Conclusion
While preparing this report, at the end of each interview, we asked the same 64%
question: Are you optimistic or pessimistic about the future of mobile device
security? Without exception, every one of the experts said that they were optimistic.
When we asked them why, they had a variety of reasons. Some cited the growing
awareness of the issue among business leaders; others talked about the advances
in technology, including the introduction of AI; some talked about improved Nearly two-thirds of
regulation and industry standards.
respondents said that public
awareness of cybersecurity
It’s been said that sunlight is the best disinfectant.58 As cybersecurity becomes
more high-profile, it is receiving more attention from consumers, business leaders risks will increase in the future.
and legislators. This increased attention is driving companies to take the issue
more seriously and legislators to improve guidance for organizations. In the past,
66%
many cybersecurity regulations were criticized for being too “outcome-based” and
offering little clear guidance. Our panel of experts said that they see that changing.
But having rules and tools in place is only part of the story. Our experts weren’t
surprised to hear that over half of respondents had said that they’d sacrificed
mobile device security. And when we asked them for a single piece of advice for Nearly two-thirds of
our readers, the majority of them said that they wished more companies used respondents said that they’d
all the tools that they were paying for.
come under pressure to
sacrifice mobile-device
Based on our experts’ advice, we have strived to pack this report with lots
security “to get the job done.”
of practical advice. We hope that you find it useful and that it helps you to
educate your employees, inform your leadership and get more out of your And 79% of those (52% of all
cybersecurity investments. respondents) had succumbed
to that pressure.
We too are optimistic about the future of cybersecurity, because people like
you got through a whole 58 pages.
You didn’t cheat and skip to the last page did you?
58 Louis Brandeis, Other People’s Money, 1914
MSI 2022 Appendices 58

Appendices 5
In compiling this report, we interviewed a number of leading
security experts among our contributors. Talking with these highly
experienced security professionals was fascinating and really
helped us to shape this report. We are really grateful to them for
their time.

Terminology used
in this report
Organization
descriptions
Security terms
Throughout this report, when we
refer to companies, businesses or Security terms like “attack” and “breach” are often used interchangeably.
organizations, we include both public- For clarity and precision, we have used the following definitions
and private-sector entities of all sizes. throughout this report:
We use the term “enterprise” to refer
to organizations with 500 or more
employees, and “small and medium-
sized businesses (SMBs)” for those Attack
with fewer. A general term covering any deliberate action toward a system or
data that is unauthorized. This may be as simple as attempting to
access it without permission.
Compromise
A successful attack that results in a system’s defenses being
rendered ineffective. This could involve data loss, downtime, other
systems being affected or no detrimental effects at all. It could be
malicious or accidental.
Data breach
An incident that results in the confirmed disclosure—not just
potential exposure—of data to an unauthorized party.
Exploit
A definition, often in the form of a script or code, of a method
to successfully leverage one or more vulnerabilities to access a
system without proper authorization.
Incident
This covers any form of security event, malicious or not, successful
or not. This could be anything from a failed authentication attempt
to a successful compromise and data breach. It includes non-
malicious events, such as the loss of a device.
Risk
A measure of the likelihood of a threat, an organization’s
vulnerability to said event and the scale of the potential damage.
Threat
Any danger that could impact the security of systems or privacy of
data. This can apply to a technique, such as phishing, or an actor,
such as an organized criminal group.
Vulnerability
A weakness that could be exploited. It may be known or unknown—
to the manufacturer, developer, owner or the world.
MSI 2022 Appendices 60

Survey
methodology
We contracted an independent research company to survey senior professionals
responsible for the procurement, management and security of mobile devices.
In total, 632 professionals responsible for the buying, managing and security of
these devices responded. The charts below break down the demographics of these
respondents. Our sample included both small companies and large enterprises.
Company size was not a strong indicator for most of our questions. Unless stated
otherwise, all data in this report is from this survey.
Unless stated otherwise, stats quoted in this report are from this survey.
Respondents by country Respondents by company size Respondents by company operations
Global (operations across
multiple countries across
Australia 10,000 or more multiple continents)
5,000 — 9,999
U.K.
6% 5% 17%
10%
14%
11% 34%
Regional
2,500 – 4,999 47%
25%
80%
27%
24%
Local
U.S. 500 – 2,499 50 – 499 Multinational
(operations in at least
one other country)
Data from contributions
Details of the source of data and statistics supplied by our contributors are given in
the next section.
MSI 2022 Appendices 61

Contributors
Absolute
Maintain secure remote access, without sacrificing on experience. Kick off or
continue your journey to SASE with a cloud-first security platform that improves
the remote working experience. NetMotion by Absolute provides optimized
remote access with a Zero Trust security posture alongside context-aware policy
enforcement for all endpoints on any network. It also enables complete visibility
of remote devices and the employee experience.
absolute.com
Check Point
Check Point is a leading provider of cybersecurity solutions to governments and
corporate enterprises globally. Its solutions protect customers from fifth-generation
cyberattacks with a leading catch rate of malware, ransomware and other types
of attacks. Check Point offers multilevel security architecture, “Infinity” Total
Protection with Gen-V advanced threat prevention, which defends enterprises’ cloud-,
network- and mobile device-held information. Check Point provides one of the most
comprehensive and intuitive “one point of control” security management systems.
Check Point protects over 100,000 organizations of all sizes.
checkpoint.com
IBM
IBM Security MaaS360 with Watson transforms how IT is securing smartphones,
tablets, laptops, desktops, wearables and IoT without sacrificing a great user
experience. AI and predictive analytics keep you alerted to potential endpoint threats
and provide remediation to avoid security breaches and disruptions. MaaS360
protects apps, content and data so organizations can rapidly scale their remote
workforce and BYOD initiatives.
The MaaS360 Mobile Metrics feature offers cloud-sourced benchmarking data and
best practices to enhance productivity and improve security. Benchmarking data is
generated by leveraging multiple data values from MaaS360 client implementations
to build aggregated metrics.
ibm.com/security/mobile/maas360
MSI 2022 Appendices 62

Ivanti
Ivanti makes the Everywhere Workplace possible. In the Everywhere Workplace,
employees use myriad devices to access IT applications and data over various
networks to stay productive as they work from anywhere. The Ivanti Neurons
automation platform connects the company’s unified endpoint management, Zero
Trust security and enterprise service management solutions, providing a unified IT
platform that enables devices to self-heal and self-secure and also empowers users
to self-service. Over 40,000 customers, including 96 of the Fortune 100, have
chosen Ivanti to discover, manage, secure and service their IT assets from cloud
to edge, and deliver excellent end-user experiences for employees, wherever and
however they work.
ivanti.com
Jamf
Jamf’s purpose is to simplify work by helping organizations manage and secure
an Apple experience that end users love and organizations trust. Jamf is one of
the only companies in the world that provides complete management and security
solutions for an Apple-first environment that is enterprise secure, consumer simple
and protects personal privacy. Today, more than 62,000 customers rely on Jamf to
manage and secure more than 27 million devices worldwide.
jamf.com
Lookout
Lookout is a leading provider of endpoint and cloud security solutions. Our
mission is to secure and empower our digital future in a privacy-focused world
where mobility and cloud are essential to all we do for work and play. We enable
consumers and employees to protect their data, and to securely stay connected
without violating their privacy and trust. Lookout is trusted by millions of consumers,
the largest enterprises and government agencies, and various partners across
telecommunications and technology.
Powered by one of the largest data sets of mobile code in existence, the Lookout
Security Graph provides visibility into the entire spectrum of mobile risk. The
installed base of Lookout’s personal and enterprise mobile endpoint products is
over 205 million mobile devices worldwide. This acts as a global sensor network
that provides visibility into the threat landscape, including over 170 million apps—
and that’s growing by up to 90,000 apps a day
lookout.com
MSI 2022 Appendices 63

Netskope
Netskope safely and quickly connects users directly to the internet, any application,
and their infrastructure from any device, on or off the network. With CASB, SWG,
and ZTNA built natively in a single platform, the Netskope Security Cloud provides
the most granular context, via patented technology, to enable conditional access
and user awareness while enforcing Zero Trust principles across data protection
and threat prevention everywhere. Netskope’s global security private cloud provides
full compute capabilities at the edge.
Netskope’s Security Cloud protects 25% of Fortune 100 companies, including:
• Three of the world’s six largest airlines
• Three of the world’s four largest banks
• Five of the world’s seven largest healthcare providers
• Two of the world’s largest telecommunications companies
Netskope is fast everywhere, data-centric and cloud-smart, all while enabling good
digital citizenship and providing a lower total cost of ownership.
netskope.com
Proofpoint
Proofpoint, Inc., is a leading cybersecurity company that protects organizations’
greatest assets and biggest risks: their people. With an integrated suite of cloud-
based solutions, Proofpoint helps companies around the world stop targeted
threats, safeguard their data and make their users more resilient against
cyberattacks. Leading organizations of all sizes, including more than half of the
Fortune 1000, rely on Proofpoint for people-centric security and compliance
solutions that mitigate their most critical risks across email, the cloud, social
media and the web.
proofpoint.com
Thales
Thales is a global high-technology leader investing in digital and “deep tech”
innovations—connectivity, big data, artificial intelligence, cybersecurity and quantum
technology—to build a future we can all trust, which is vital to the development of
our societies. The company provides solutions, services and products that help
its customers—businesses, organizations and states—in the defense, aeronautics,
space, transportation, and digital identity and security markets to fulfill their critical
missions, by placing humans at the heart of the decision-making process.
thalesgroup.com
MSI 2022 Appendices 64

65

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-17", "model": "gemini-3.8-flash"} -->
