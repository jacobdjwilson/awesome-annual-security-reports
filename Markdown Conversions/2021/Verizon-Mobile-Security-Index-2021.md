# Mobile Security Index 2021

## Table of Contents
- [Foreword](#foreword)
- [Mobile Security Index cheatsheet](#mobile-security-index-cheatsheet)
- [The state of mobile security](#the-state-of-mobile-security)
  - [Compromises may be down, but the threats are growing.](#compromises-may-be-down-but-the-threats-are-growing)
- [Let’s start just calling it “work.”](#lets-start-just-calling-it-work)
  - [Out of office](#out-of-office)
  - [Working personas](#working-personas)
  - [Bring your own.](#bring-your-own)
  - [Securing BYOD/BYOPC programs](#securing-byodbyopc-programs)
  - [Small, but mighty](#small-but-mighty)
  - [5G and multi-access edge computing](#5g-and-multi-access-edge-computing)
- [The threats are real.](#the-threats-are-real)
  - [The number compromised was down.](#the-number-compromised-was-down)
  - [It’s more than data that’s at risk.](#its-more-than-data-thats-at-risk)
  - [The pressure to sacrifice security](#the-pressure-to-sacrifice-security)
  - [What do companies sacrifice security for?](#what-do-companies-sacrifice-security-for)
  - [Shadow IT](#shadow-it)
- [The mobile threat landscape](#the-mobile-threat-landscape)
  - [04.1 People and behaviors](#041-people-and-behaviors)
    - [VAPs not VIPs](#vaps-not-vips)
    - [Phishing](#phishing)
    - [The COVID-19 effect](#the-covid-19-effect)
    - [QRiosity can be dangerous.](#qriosity-can-be-dangerous)
    - [Attack case study: Clorox](#attack-case-study-clorox)
    - [Business email compromise](#business-email-compromise)
    - [Securing against phishing](#securing-against-phishing)
    - [Credential theft](#credential-theft)
    - [Inappropriate use](#inappropriate-use)
    - [Acceptable use and remote workers](#acceptable-use-and-remote-workers)
  - [04.2 Apps](#042-apps)
    - [Trends in app use](#trends-in-app-use)
    - [App permissions](#app-permissions)
    - [Password snooping](#password-snooping)
    - [Leaky apps](#leaky-apps)
    - [Malware](#malware)
    - [Ransomware](#ransomware)
    - [Attack case study: Lucy ransomware](#attack-case-study-lucy-ransomware)
    - [Securing against malware](#securing-against-malware)
  - [04.3 Devices and things](#043-devices-and-things)
    - [Out-of-date operating systems](#out-of-date-operating-systems)
    - [Lost or stolen devices](#lost-or-stolen-devices)
    - [IoT devices](#iot-devices)
    - [Securing IoT devices](#securing-iot-devices)
  - [04.4 Networks and cloud](#044-networks-and-cloud)
    - [Risky networks](#risky-networks)
    - [Public Wi-Fi](#public-wi-fi)
    - [Home Wi-Fi](#home-wi-fi)
    - [VPNs](#vpns)
    - [Cloud](#cloud)
    - [Securing against network threats](#securing-against-network-threats)
- [Looking ahead](#looking-ahead)
  - [Drivers of change](#drivers-of-change)
  - [The future](#the-future)
- [About this report](#about-this-report)
  - [Terminology](#terminology)
  - [Survey methodology](#survey-methodology)
- [Contributors](#contributors)
  - [Security companies](#security-companies)
  - [Law enforcement](#law-enforcement)
- [Further reading](#further-reading)
  - [Verizon thought leadership](#verizon-thought-leadership)
  - [Other Verizon security reports](#other-verizon-security-reports)
  - [Additional resources from government and law enforcement agencies](#additional-resources-from-government-and-law-enforcement-agencies)

---

# Foreword

Cybersecurity is not a new issue, but the stakes are getting higher. The scale of regulatory penalties is growing, and customers—consumers, businesses and public-sector organizations alike—are becoming more sensitive to the issue. In the past, many consumers saw little difference between the security postures of the companies—such as banks and retailers—pursuing their business, and so it didn’t sway their loyalty. That’s changing, and consequently lots of companies are responding by making security and data privacy central to their value proposition.

78%
More than three-quarters of companies think that data privacy will be a key brand differentiator in the future.

For more than a decade, Verizon has published some of the preeminent reports on cybersecurity, including the Data Breach Investigations Report (DBIR). This is the fourth edition of the Mobile Security Index. As the name suggests, it focuses on the threats to mobile devices; what defenses companies have in place to thwart these attacks; and how often those fail, leading to a mobile-related compromise.

One of the key themes of the 2020 Mobile Security Index was mal-innovation. We talked about how cybercriminals were constantly finding new and often imaginative ways to carry out attacks. In another life, where their motives weren’t nefarious and the outcomes not so damaging to so many, the creativity and ingenuity shown by some of the attackers would merit fame and accolades.

Sadly, mal-innovation continues apace, and we saw many new examples in 2020. COVID-19—you didn’t think that we’d not mention it, did you?—provided cybercriminals with new opportunities. Criminals were able to craft tailored phishing attacks very quickly. But that’s no longer a surprise. It doesn’t take a pandemic for phishing gangs to identify new ways to exploit human weaknesses to further their attacks.

Another of the key themes of our 2020 report was how mobile devices are not just being used more, but used for more. In large part driven by apps and data in the cloud, mobile devices have evolved from being a handy companion into an essential business tool. Today, you can buy a watch that has much of the functionality smartphones had just a couple of years ago. Smartphones, tablets and other mobile devices can now be used to access core systems, edit spreadsheets and perform other mission-critical tasks.

When we asked respondents to our latest survey to rate how crucial mobile is to their business on a 10-point scale, 71% answered 8 or higher. But with the increased reliance on mobile devices, the risk has grown too. Mobile devices are subject to all the same risks as non-mobile user devices, plus some of their own:

### Amplified risks
Mobile devices can be subject to attacks that could happen on any device, but sometimes the mobile device makes them more likely to be successful.

An example is a phishing attack. Several of the ways users spot a malicious email or website are less obvious on a small screen, meaning users may be more likely to fall for an attack.

### Specific risks
Mobile devices are significantly more prone to loss and theft. This can lead to the exposure of data, but often the biggest impact is on productivity.

Because they are often used in public places—like trains and coffee shops—mobile devices are susceptible to eavesdropping, both physical and electronic.

### Gateway risks
Attackers can exploit mobile devices to acquire data from the cloud and other systems that they connect to.

They can also be attacked to capture credentials, which can then be used to gain access to data in other systems.

We couldn’t really write this report without discussing the impact the COVID-19 pandemic has had on the nature of how we work. The number of remote workers has been growing for years, but in many companies—including Verizon—working from home went from being the exception to being the rule virtually overnight. Unsurprisingly, this led some to cut corners, including on security. Nearly a quarter (24%) of respondents to our survey said that their organization had sacrificed the security of mobile devices to facilitate their response to restrictions put in place due to the pandemic.

Read on to learn more about the mobile security environment and understand its risks. We hope that this insight will help you to strengthen your mobile security as your digital transformation journey—and evolution to the new world of work—unfolds.

The findings of this report are based on a survey of 856 professionals responsible for the procurement, management or security of mobile devices. Unless stated otherwise, quoted statistics are from this survey. Other findings are based on data supplied by our contributors: Asavie, Check Point, BlackBerry Cylance, IBM, Lookout, MobileIron, NetMotion, Netskope, Proofpoint, Qualcomm, Thales, VMware and Wandera.
For full details of the methodology, please see page 86.

MSI 2021  Foreword

4

# Mobile Security Index cheatsheet

The threats are rising.

Two-fifths of respondents said that they think that mobile devices are the company’s biggest IT security threat. Of the rest, 85% said that mobile devices are at least as vulnerable as other IT systems.

40%
Forty percent said that mobile devices are the company’s biggest security risk.

78%
Seventy-eight percent expected home working to remain higher even when COVID-19 is no longer an issue.

Driven by increased home working
A large majority (79%) had seen remote working increase as a result of COVID-19. Most (70%) expected remote working to fall again, but over three-quarters said that it would remain higher than before lockdown.

And expanded use of cloud
Respondents said that nearly half (46%) of their IT workloads were run in the cloud. Three-quarters said their reliance on cloud-based apps is growing.

75%
Seventy-five percent said that their business’s reliance on cloud-based apps is growing.

76%
Seventy-six percent said that they’d come under pressure to sacrifice the security of mobile devices for expediency.

Putting pressure on IT
Growing threats and never-ending pressure from the organization are putting IT in a difficult position. Over three-quarters had come under pressure to sacrifice mobile device security to help meet deadlines and other business goals. And 75% of those succumbed.

And increasing concerns
The vast majority (82%) of respondents that expressed an opinion said that within five years their company will rely on networks it doesn’t own, like home broadband and cellular, more than ones it does. More than half (58%) said they struggle to reconcile differing mobile demands from across the business.

83%
Eighty-three percent said that they are concerned about the growth of “shadow IT.”1

23%
Twenty-three percent were aware that their company had experienced a mobile device-related security compromise.2

Reported compromises are down.
Fewer respondents in our latest survey were aware of their company having suffered a mobile-related security compromise.

But the severity remains high.
Over half of those that had suffered a compromise said that the consequences were major. Just 12%, less than one in eight, said that the consequences were minor.

53%
Fifty-three percent said that the consequences of a breach they suffered were major.

1 Users or departments making their own IT decisions and purchasing without oversight.
2 All 856 respondents.

MSI 2021  Mobile Security Index cheatsheet

6

# The state of mobile security

01

Each edition of this report has seen the number of companies suffering mobile security compromises rise. Until now. While this is good news, there are many reasons to believe that the picture isn’t as rosy as this finding might suggest. More than one in five surveyed companies had experienced a compromise involving a mobile device in the preceding 12 months. And further, the severity of the consequences remained high.

## Compromises may be down, but the threats are growing.

Fewer companies were aware of successful mobile-related attacks.

By way of comparison, a recent report by Thales noted that 26% of global respondents had experienced a data breach of any kind in the previous 12 months.5

This is the fourth year that Verizon has published this report. And this time the percentage of companies that admitted to having suffered a mobile-related security compromise is the lowest we’ve seen—just 23%.3 But hold the Champagne. Nearly one in four companies suffering a mobile device attack is not cause for celebration.

One factor affecting these results is that the pressure on companies to sacrifice security was higher due to the measures needed to cope with COVID-19. This is highly likely to have inflated the sacrifice figures.

Companies were also likely to have been distracted. This could mean that they haven’t spotted compromises, or if they did spot them, they have not thoroughly traced them back to identify all involved sources.

It’s also likely that cybercriminals were still modifying their methods when we did our survey. While attacks like phishing could continue as normal—and, in fact, COVID-19 gave hackers new opportunities—these attacks are less likely to be traced back to a device type.

The share of companies sacrificing security went up, but fewer suffered a compromise.

| Report | Sacrificed security | Experienced compromise | Multiplier* |
|---|---|---|---|
| 2018 | 32% | 27% | 2.4x |
| 2019 | 48% | 33% | 1.9x |
| 2020 | 43% | 39% | 2.0x |
| 20214 | 45% | 23% | 1.5x |

Figure 1. Has your organization experienced a security compromise involving mobile/IoT devices during the past year? Has your organization ever sacrificed the security of mobile devices (including IoT devices) to “get the job done” (e.g., meet a deadline or productivity targets)? [n=601, 671, 876, 856]

*Increased likelihood that an organization that sacrificed security suffered a mobile-related security compromise. For example: Companies that sacrificed security in 2021 were 1.5 times as likely to suffer a mobile-related security compromise.

3 Ibid.
4 Ibid.
5 Thales Data, Threat Report Global Edition, 2020. Based on research carried out by IDC in November 2019.

MSI 2021  The state of mobile security

9

Half thought that mobile device risks were growing faster than others.

50%
Figure 4. Which of the following statements regarding the security of mobile devices do you agree with? Mobile device threats are growing more quickly than other threats. [n=598]

The risks remain high.
Companies see themselves as at risk.
Despite the drop in known compromises, more than one in five companies experienced the loss of data or significant disruption to operations, or both.
More than two-thirds of respondents said that the risks associated with mobile devices had increased in the past year. And half (50%) said that mobile device risks are growing faster than others.

Few thought that there was no risk associated with mobile devices.

| Risk Level | Percentage |
|---|---|
| High risk | 25% |
| Significant risk | 50% |
| Moderate risk | 25% |
| Little or no risk | 0% |

Figure 2. How would you assess your organization’s risk from mobile device threats? Consider any security risk stemming from the use of smartphones, tablets or laptops using mobile data. [n=590]

Most thought that the risk associated with mobile devices grew in the past year.

| Change in Risk | Percentage |
|---|---|
| Increased significantly | 25% |
| Increased | 50% |
| Not changed | 25% |
| Decreased | 0% |
| Decreased significantly | 0% |

Figure 3. How do you think the security risks associated with mobile devices have changed in the past year? [n=591]

MSI 2021   The state of mobile security

10

Companies are still failing on the basics.

Since the first edition of this report, back in 2018, we have tracked how many companies have had four basic protections in place. These precautions were chosen based on some of the recurring problems identified in our sister publication, the Verizon Payment Security Report.

Over the years, the share of companies in compliance with these protections hasn’t changed much. Until now. In previous reports, the share of companies in compliance with all four hovered around 12%, give or take 1 percentage point (pp). In our latest review, just 9% had all of them in place.

Despite not even having some of the most basic precautions in place, most respondents thought that any security or misuse issues would be spotted quickly. This mirrors our findings in previous years.

### The four basic protections
Which of the following statements match your organization’s security policies?
1. We change all default/vendor-supplied passwords
2. We always encrypt sensitive data when sent across open, public networks
3. We restrict access to data on a “need-to-know” basis
4. We regularly test our security systems and processes

Find out more.
Learn more about compliance with the Payment Card Industry Data Security Standard (PCI DSS) in the Verizon 2020 Payment Security Report (the ninth edition).
verizon.com/paymentsecurityreport

Companies with all four basic protections in place
Few had four basic security measures in place.

| Year | Percentage |
|---|---|
| 2018 | 12% |
| 2019 | 12% |
| 2020 | 13% |
| 2021 | 9% |

Figure 5. Which of the following statements match your organization’s security policies? [n=601, 671, 856, 598]

| Protection | Percentage |
|---|---|
| We restrict access to data on a need-to-know basis. | 39% |
| We always encrypt sensitive data when sent across open, public networks. | 40% |
| We change all default/vendor-supplied passwords. | 39% |
| We regularly test our security systems and processes. | 49% |
| None | 15% |

Figure 6. Which of the following statements match your organization’s security policies? [n=598]

MSI 2021   The state of mobile security

11

Companies remain confident in their defenses.

Despite the risks and numerous indications throughout our survey that companies have insufficient defenses in place—both in terms of security solutions and processes—companies were confident that they would spot compromises and misuse quickly.

This isn’t new; we’ve seen similar confidence in our previous surveys. Nor is the fact that despite this, companies realize that they have more to do. In our latest survey, 81% of respondents agreed that organizations need to take the security of mobile devices more seriously.

Most thought they’d spot a compromised device quickly.

| Confidence Level | Percentage |
|---|---|
| Very confident | 25% |
| Quite confident | 50% |
| Not very confident | 25% |
| Not at all confident | 0% |

Figure 7. If a mobile device was compromised, would you spot it quickly? [n=591]

Most thought that the risk associated with mobile devices grew in the past year.

| Confidence Level | Percentage |
|---|---|
| Very confident | 25% |
| Quite confident | 50% |
| Not very confident | 25% |
| Not at all confident | 0% |

Figure 8. If one of your employees misused a company device, would you spot it quickly? [n=592]

MSI 2021   The state of mobile security

12

# Let’s start just calling it “work.”

02

In the past, working from home was thought of as a special case. That attitude had been changing, slowly. Then COVID-19 hit and companies were forced to reevaluate virtually overnight. The shift may not have been through choice, but now even some leaders with the most entrenched objections to home working have changed their minds. It seems that necessity is also the mother of evolution. The “new normal” remains uncertain, but it’s a safe bet that more flexible working arrangements are going to be part of it.

## Out of office

You don’t need a research report to tell you that there was a massive increase in the number of people working from home in 2020. Remote working has become commonplace and things are unlikely to ever go back to the way they were. Numerous companies have announced long-term—or even permanent—work-from-home policies and plans to reduce their property footprint.

Netskope has called this phenomenon “inversion.” Its research found that the ratio of remote workers to others went from one in four at the start of 2020 to two out of three by the summer. And that pattern continued throughout the rest of the year.

“We anticipate never going back to five days a week in the office, that seems very old-fashioned now.”
—Alan Jope, Unilever CEO6

Almost two-thirds (66%) of respondents said that they expect the term “remote working” will have disappeared within five years.

The ratio of remote workers to others has “inverted.”

| Period | Remote Workers | Non-Remote Workers |
|---|---|---|
| Jan 2 | 25% | 75% |
| Jan 15 | 25% | 75% |
| Jan 30 | 25% | 75% |
| Feb 13 | 25% | 75% |
| Feb 27 | 25% | 75% |
| Mar 12 | 25% | 75% |
| Mar 26 | 50% | 50% |
| April 9 | 75% | 25% |
| April 23 | 75% | 25% |
| May 7 | 75% | 25% |
| May 21 | 75% | 25% |
| June 4 | 75% | 25% |
| June 18 | 75% | 25% |
| July 2 | 75% | 25% |
| July 16 | 75% | 25% |
| July 30 | 75% | 25% |
| Aug 3 | 75% | 25% |
| Aug 27 | 75% | 25% |
| Sept 10 | 75% | 25% |
| Sept 24 | 75% | 25% |
| Oct 8 | 75% | 25% |
| Oct 22 | 75% | 25% |
| Nov 5 | 75% | 25% |
| Nov 19 | 75% | 25% |
| Dec 3 | 75% | 25% |
| Dec 17 | 75% | 25% |
| Dec 31 | 75% | 25% |

Figure 9. Split of workers, remote versus non-remote. Data from Netskope.7

6 Reuters, Reuters Next conference, January 2021.
7 Netskope, January 2021. Research was performed on anonymized usage data collected from a subset of Netskope Security Cloud platform customers (primarily North American) that had given permission for this use.

MSI 2021  Let’s start just calling it “work.”

14

Our survey respondents reported similar numbers. Nearly four-fifths (79%) of organizations saw remote working increase. Overall, the share of remote workers grew from around a third (32%) of the average workforce before lockdowns began to nearly twice as many (62%) during lockdown.

We also asked respondents what they expected this proportion to be once COVID-19 is just a memory. A large majority (70%) of those that had seen remote working grow following the introduction of restrictions expected it to fall again afterward. However, 78% said that it would still remain higher than before lockdown. Overall, our respondents said that they expected the number of remote workers to settle at around half (49%).

Interestingly, the difference between small and medium-sized businesses (SMBs) and enterprises was quite small, just a few percentage points. The biggest difference was how much more capable larger companies were of adjusting operations to switch employees to working from home. SMBs increased home working by 22 pp, enterprises by 32 pp.

“Mobile devices were critical to maintaining business continuity during lockdown by enabling employees to stay productive from home. That explains the 26% increase in their use we saw in the first 100 days.
— Aaron Cockerill, Chief Strategy Officer, Lookout

Remote working peaked at nearly double, expected to settle at more than 50% up.

| Period | Pre-lockdown | During lockdown | Post-lockdown (anticipated) |
|---|---|---|---|
| Mean | 32% | 62% | 49% |
| 95% Confidence Interval | 29.9% - 34.0% | 59.9% - 64.2% | 47.0% - 51.3% |

Figure 10. What proportion of your organization’s staff work remotely, including from home? Include anybody that works outside the office more than 25 days per year. Lockdown refers to restrictions put in place in response to COVID-19. Dotted lines show 95% confidence intervals. [n=598]

This chart isn’t meant as an homage to Joy Division—or the cover of the 2015 DBIR for you fans of our sister publication. Those of you with a knowledge of statistics will recognize these as confidence plots. The horizontal center of each curve shows the mean—32% in the pre-lockdown results. As our respondents are just a sample of all businesses, the actual average may be different; this is called sampling error. Statistically, we can say that the true number is within the two dotted lines with 95% confidence. In this analysis, the potential error is small, around just ±2 percentage points (pp).

89%
Eighty-nine percent of remote workers have encountered connectivity or poor user experience issues during the lockdown.8

Views on productivity when working from home vary by region.

U.K.
U.S.
Australia

The productivity question
Historically, there have been many reasons why companies have been reluctant to let employees work from home. The main reason our respondents cited for not enabling more staff to work from home was the nature of their roles—either there was no demand for the role (for example, the store, restaurant or other site was closed) or the role couldn’t be done remotely (for example, production line jobs and care workers).

Another reason has been that some leaders felt that staff couldn’t—or wouldn’t—be as productive working remotely. But attitudes are changing. Three-fifths (60%) of respondents to our survey said that the productivity of remote workers was at least as high as those onsite. And one in five (20%) said that it was significantly higher—and that was at a time of mass disruption, with many people using makeshift workstations and a large number of parents having to cope with challenges like remote schooling.

Enterprises (61%) were more likely to say that the productivity of remote workers was at least as good, compared to SMBs (54%). There was more variation by region. It’s tempting to try to explain these numbers—and with U.S. and U.K. contributors, we had some interesting conversations—but we don’t have the data to confirm any hypothesis.

These variances remind us about the dangers of averages. Working from home is much easier for some workers than others. For instance, the technology to create virtual call centers is well established, and companies with adaptable infrastructures were able to transition workers quickly. It’s also worth noting that some companies were able to successfully empower staff to work from home, but not in their normal role. For instance, when its U.S. retail stores were forced to close, Verizon was able to retask staff to provide online support—which was seeing a huge growth in demand.

Not all roles are as easy to shift. Some industries, like manufacturing, tend to have more of these sorts of roles and so faced greater challenges.

Most companies think their workforce is at least as productive when working remotely.

| Productivity Level | Percentage |
|---|---|
| Much less productive | 0% |
| Somewhat less productive | 0% |
| A little less productive | 0% |
| About the same | 60% |
| A little more productive | 20% |
| Somewhat more productive | 10% |
| Much more productive | 10% |

Figure 11. Is your workforce as productive working from home as when in the office? [n=598]

Figure 12. Is your workforce as productive working from home as when in the office? [n=598]

8 NetMotion, SDP report, June 2020. A survey of over 600 network and IT professionals across the U.S., the U.K. and Australia.

MSI 2021  Let’s start just calling it “work.”

16

Lockdowns adversely affected security.

| Agreement Level | Percentage |
|---|---|
| Strongly disagree | 0% |
| Disagree | 0% |
| No opinion | 3% |
| Agree | 50% |
| Strongly agree | 47% |

Figure 13. Changes to remote working practices made during lockdown adversely affected our security. [n=566]

Security and compliance issues prevented more people from working from home.

| Percentage |
|---|
| Some employees prevented | 33% |
| No employees prevented | 67% |

Figure 14. Why weren’t more of your employees able to work from home during lockdown? Security/compliance issues.

Sales of MDM boomed.

| Period | New license sales |
|---|---|
| Nov 2019–Jan 2020 | Low |
| Feb 2020–April 2020 | High |
| May 2020–July 2020 | Very High |
| Aug 2020–Oct 2020 | Very High |

Figure 15. Volume of new license sales for Verizon MDM.

The security question
Nearly all (97%) security leaders consider remote workers to be exposed to more risk than office workers.9 And almost half (49%) said that changes during lockdown conditions affected mobile security for the worse.

In fact, one in three (33%) respondents said that it wasn’t possible to enable all the employees to work from home that they wanted to due to security or compliance issues.

One of the most obvious reactions to dealing with the security challenges of the increase in home workers was the increase in demand for mobile device management (MDM). Contributors to this report, like IBM, MobileIron and Wandera, all reported seeing an increase in new license sales, and Verizon saw an order-of-magnitude increase in purchases of its MDM solution.

“The number of requests for proposal (RFPs) for large enterprise mobile threat defense projects more than doubled from 2019 to 2020.”
—Michael Covington, VP Product Strategy, Wandera10

According to NetMotion, 43% of companies experienced cybersecurity issues with remote workers in 2020.11

9 NetMotion, SDP report, June 2020. A survey of over 600 network and IT professionals across the U.S., the U.K. and Australia.
10 Michael Covington, statement, January 2021.
11 NetMotion, Experience Monitoring Report, November 2020. A survey of 500 IT professionals and 500 office workers now working remotely.

MSI 2021  Let’s start just calling it “work.”

17

## Working personas

Clearly, when it comes to where and how we work, the landscape has changed. In the past, people have used terms like “remote working,” “home working” and “flexible working” interchangeably. This fails to clearly describe the nature of the modern workforce and the nuances in behaviors and the threats they face.

We’ve identified seven types of employees. These fall into four categories based on the type of work they do and where the work is done. We’ve used these terms throughout this report for precision and clarity.

### Non-remote workers
Employees that work inside a company-controlled environment, the perimeter, like an office, store or plant

#### Back office
##### Office bound:
This includes a wide range of workers, from call center staff to lawyers. They might be required to work from the office, or chose to do so—not everybody likes or has the right conditions to work from home. These workers typically rely on a local area network (LAN) or wireless LAN (WLAN)—within the perimeter. They might work from home a few times a month.
##### Floor workers:
This category includes many roles in retail, hospitality, manufacturing, etc. These workers aren’t fixed to a desk, but their location doesn’t change much. They are more likely to use a specialized device. They will rarely use a network not controlled by the company.

#### Front of house
##### Commuters:
##### Corridor warriors:
Employees that are never at their desks, but their roaming is mainly limited to one of the company’s sites. They primarily use the company’s WLAN.
##### Tethered:

### Remote workers
Employees that operate outside the perimeter, whether on the road or at home

#### Back office
##### Home workers:
People based at home or who work from home a lot. This label can apply to a wide variety of roles. They typically use home Wi-Fi, perhaps with a virtual private network (VPN).
##### Flexible workers:
Employees that work from home a few days a week—there are all kinds of reasons why. They commonly use home Wi-Fi, perhaps with a VPN.

#### Front of house
##### Nomads
##### Road warriors:
These are the classic “remote workers”: sales people, consultants, CxOs of big companies, etc. They need to be able to work from multiple locations and work on the move. They have complex requirements and use multiple types of networks. They are likely to need to use third-party Wi-Fi and cellular connectivity.
##### Field workers:
Another well-established category. It includes roles like service engineers. People in this group often need to use custom apps and work on the move—so cellular connectivity is key. Their primary device may be a customized or ruggedized device.

Figure 16. Classification of types of workers.

MSI 2021  Let’s start just calling it “work.”
MSI 2021

18

## Bring your own.

Bring your own device (BYOD) was a very hot topic a few years ago. While vendors had introduced a number of variants (see below) prior to COVID-19, interest among organizations seemed to have waned. However, when restrictions were put in place to combat the pandemic, many companies relied heavily on employees using their own devices to maintain operations. More than one in three (36%) organizations opened up access to corporate resources and systems to employees using personal devices—that’s on top of those that already allowed it.

Another factor driving increased interest in BYOD is the rise of the “gig economy.” This isn’t limited to delivery riders; roles like telesales and support can fit this model very well. Companies are increasingly using this approach to enable them to scale more quickly as demand ebbs and flows. Verizon’s 2020 The Future of Work report found that about half (49%) of respondents thought that the pandemic had increased the importance