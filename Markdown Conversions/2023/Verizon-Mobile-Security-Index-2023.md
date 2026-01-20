# 2023 Mobile Security Index

The official report URL is: https://www.verizon.com/business/resources/reports/mobile-security-index/

## Table of Contents
- [Who should read this white paper?](#who-should-read-this-white-paper)
- [Definitions](#definitions)
- [Introduction](#introduction)
- [What’s at risk?](#whats-at-risk)
- [Plenty of stones left unturned](#plenty-of-stones-left-unturned)
- [Users and behaviors](#users-and-behaviors)
- [The complacency problem](#the-complacency-problem)
- [The danger of security fatigue](#the-danger-of-security-fatigue)
- [Is working from home here to stay?](#is-working-from-home-here-to-stay)
- [Taking work home or bringing risks to work?](#taking-work-home-or-bringing-risks-to-work)
- [Users not as savvy as they think](#users-not-as-savvy-as-they-think)
- [Phishing is still a popular pastime.](#phishing-is-still-a-popular-pastime)
- [Everything is going hybrid.](#everything-is-going-hybrid)
- [Big exec compromise?](#big-exec-compromise)
- [Balancing security and user experience](#balancing-security-and-user-experience)
- [Applications](#applications)
- [Malware](#malware)
- [Ransomware](#ransomware)
- [Balancing security and freedom](#balancing-security-and-freedom)
- [Devices and things](#devices-and-things)
- [BYOD](#byod)
- [Device loss/theft](#device-loss/theft)
- [SIM theft](#sim-theft)
- [Internet of Insecure Things?](#internet-of-insecure-things)
- [Balancing security and privacy](#balancing-security-and-privacy)
- [Networks and clouds](#networks-and-clouds)
- [Home Wi-Fi](#home-wi-fi)
- [Public Wi-Fi](#public-wi-fi)
- [Clouds](#clouds)
- [5G](#5g)
- [Balancing security and cost](#balancing-security-and-cost)
- [Connected laptops](#connected-laptops)
- [Fixed wireless access (FWA)](#fixed-wireless-access-fwa)
- [Conclusion](#conclusion)
- [Contributors](#contributors)
- [About the cover](#about-the-cover)

---

# 2023 Mobile Security Index white paper

## Who should read this white paper?

We produced this Verizon Mobile Security Index white paper to help security professionals, such as chief information security officers (CISOs), assess their organization’s mobile security environment and calibrate their defenses. This report is also relevant to anyone involved in the specification, procurement or management of IT devices and services.

## Definitions

Security terms like “attack” and “breach” are often used interchangeably. For clarity and precision, we’ve used the following definitions throughout this report:

*   **Attack**: A general term covering any deliberate unauthorized action toward a system or data. This may be as simple as attempting to access it without permission.
*   **Compromise**: A successful attack that results in a system’s defenses being rendered ineffective. This could involve data loss, downtime, other systems being affected or no detrimental effects at all. It could be malicious or accidental.
*   **Data breach**: An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party.
*   **Exploit**: A definition, often in the form of a script or code, of a method to successfully leverage one or more vulnerabilities to access a system without proper authorization.
*   **Incident**: Any form of security event, malicious or not, successful or not. This could be anything from a failed authentication attempt to a successful compromise and data breach. It includes non-malicious events, such as the loss of a device.
*   **Risk**: A measure of the likelihood of a threat, an organization’s vulnerability to said event and the scale of the potential damage.
*   **Threat**: Any danger that could impact the security of systems or privacy of data. This can apply to a technique, such as phishing, or an actor, such as an organized criminal group.
*   **Vulnerability**: A weakness that could be exploited. It may be known or unknown—to the manufacturer, developer, owner or the world.

## Introduction

The statistics are sobering: 61% of CISOs (and 53% of CEOs) think that their organization is unprepared to cope with a targeted cyberattack in the next 12 months.¹ With mobile devices now making up a large part—even the majority—of the device estate, mobile security is more important than ever.

Those managing security must protect a growing number and diversity of endpoints. Increasingly, those endpoints are mobile or using mobile connectivity. Bring-your-own-device (BYOD) policies, hybrid working and the proliferation of Internet of Things (IoT) have multiplied the scale and complexity of protecting endpoints. This ultimately affects the business, its employees, shareholders and customers.

In this report, we’ll look at some of the biggest threats to mobile devices—from the phone in your pocket to the predictive maintenance sensors on a 5-ton steel press.

In the 2022 edition of the Mobile Security Index, we reported that nearly two-thirds (66%) of respondents said that they’d come under pressure to sacrifice mobile device security “to get the job done.” Of those, 79% (or 52% of all respondents) had succumbed to that pressure. In this white paper, we look at the challenges of balancing security with user experience, privacy, freedom and cost. We offer some guidance on how to strike this balance.

According to Forrester, IoT devices, employee-owned mobile devices followed by company-owned mobile devices were the three most common targets in external attacks.

> Forrester²

¹ Proofpoint, Cybersecurity: The 2023 Board Perspective, 2023
² Forrester, The State Of IoT Security, 2023

## What’s at risk?

One of the reasons why mobile devices likely don’t get the attention that they deserve is that people focus on what’s on the device. But it’s not just what’s on the device that businesses have to worry about. As of 2022, 60% of all corporate data was stored in the cloud.³

Mobile phones make an attractive target in a similar way to a wallet. Pocketing the cash might be nice, and maybe all an attacker is after. But it’s the cards that offer access to much greater rewards for attackers that know what they’re doing. The content stored on a phone may be of some interest, but the greatest potential value of compromising the device is the entry point it could offer to the company’s “crown jewels”—its customer data, intellectual property and other secrets. And many of the characteristics of mobile devices make them more vulnerable than other assets, namely:

### 4 cons of mobile device security

*   **Convenience**: The portability of mobile devices—obviously not the aforementioned steel press—can make them easier to steal.
*   **Connections**: Mobile devices typically connect to more networks—often insecure public ones. This can expose them to more risk.
*   **Control**: Organizations often have less visibility of mobile devices and they’re often less well-protected than endpoints like servers.
*   **Content**: Users often blur the lines between work and personal tasks when using mobile devices—and what apps and data they store on them.

> Various studies estimate that as many as 90% of successful cyberattacks and as many as 70% of successful data breaches originate at endpoint devices.⁴
>
> 91% of CEOs/CFOs put the responsibility for cybersecurity squarely with IT.
>
> Accenture⁵

So why aren’t mobile device breaches constantly in the news? While cybersecurity is much bigger news than it was a few years ago, companies are often reticent to share the details of attacks they’ve suffered. Even when details are discussed, it’s rare that the specific device type involved in the initial compromise is mentioned.

It’s a lot like when a company wins a big deal. Very few companies are able to trace back all the points of contact or all the little things that encouraged the customers to place the order—such as the marketing emails, TV ads, events, etc. Likewise, a breach may be attributed to a phishing attack, but maybe that only worked because the message came from a legitimate address. So, an earlier credential-stuffing attack was actually a critical step in the attack.

³ Lookout, The State of Remote Work Security, 2023
⁴ IBM, What is Endpoint Security?, 2023
⁵ Accenture, Elevating the Cybersecurity Discussion, 2022

## Plenty of stones left unturned

Unsurprisingly, headlines about security breaches tend to focus on the impact—the number of customers affected, the disruption to services, the cost of remediation and the fines levied. Many security reports focus on the techniques employed to gain access to systems and data. What isn’t discussed very often is what happens between when a company’s systems are first compromised and when the attackers’ presence is detected. Over the years, the authoritative source of cybersecurity breach information, the Verizon Data Breach Investigations Report (DBIR), has tracked how long it takes companies to discover a breach.

### Detection in non-actor-disclosed breaches errors

![Figure 1: Time to detect intrusion (non-actor disclosed breaches).](https://www.verizon.com/business/resources/reports/mobile-security-index/assets/images/figure1.png)
*Figure 1: Time to detect intrusion (non-actor disclosed breaches).⁶*

Around 50% of intrusions are disclosed by the perpetrators—who either send a ransomware demand, brag about their success on a forum or put the loot up for sale. Around one-fifth goes undiscovered for months or more.⁷

It wasn’t until the 1970s that the Allies admitted that they’d broken the German Enigma machine in 1941. If they’d let the Nazis know they could read their messages before the end of World War II, they’d have stopped using the machine and an incredibly valuable source of information would have dried up. Likewise, cyberattackers often lurk in the shadows gathering useful intelligence and nosing around.

It’s an effective tactic. According to IBM, nearly 40% of the data breaches that it studied involved the loss of data from across multiple environments—including public cloud, private cloud and on-premises. This shows that attackers were able to move laterally and compromise multiple environments before being detected.⁸

### 4 ways attackers can exploit access

*   **Persistence**: Lying low and staying alert can yield results. Eavesdropping for an hour may prove pretty boring. Eavesdropping for a couple of months is much more likely to reveal something valuable or useful in an attack.
*   **Lateral movement**: Like a burglar moving from room to room, cybercriminals will often use the access they’ve gained to move from system to system until they find something valuable.
*   **Impersonation**: Today, many staff are wise to the dangers of social engineering. But even technologically savvy employees may fall for an email or instant message “from a colleague.” Attackers can exploit this to access other systems, change payment details and more.
*   **Credential elevation**: Similar to lateral movement, attackers can use a set of compromised credentials to compromise other credentials—perhaps using impersonation—with greater access.

⁶ Verizon, Data Breach Investigations Report (DBIR) 2022
⁷ ibid.
⁸ IBM, Cost of a Data Breach Report 2023, 2023

## Users and behaviors

A lack of understanding of the potential consequences combined with the blurring of boundaries between home and work make a dangerous combination.

> 81% of organizations faced malware, phishing, and password attacks last year which were mainly targeted at users. This underscores that employees can be an organization’s weakest point.
>
> Fortinet¹¹

The enormous increase in the functionality of mobile devices has fundamentally altered how we think about work. It’s changed the way we think about where we work from, as well as how we separate work and personal—both activities and responsibilities.

In the 2022 Mobile Security Index, we discussed how the world has moved from “work from anywhere” to an “everywhere, all the time” mindset. While this shift may have improved productivity—although there is some debate—it has also created additional challenges for IT and security teams.

The first challenge is that the separation between work and personal device use has all but evaporated. Who doesn’t occasionally check messages or do some shopping on a work device? Most users don’t even consider that something “harmless,” like using personal social media or connecting to an unknown Wi-Fi network while traveling, could impact their entire organization.

The majority of data breaches involve a human weakness, often people falling for social engineering techniques.

### The complacency problem

Despite improvements in cybersecurity training over the years, many users are not well-informed about the risks associated with mobile devices. Nearly half (49%) of users think that clicking on a malicious link or opening a malicious attachment can only affect their device.⁹

That helps explain why over a third (34%) of users have fallen for one of the five following basic security errors.

#### 5 basic security errors

*   Clicked phishing link: 18%
*   Downloaded malware: 13%
*   Downloaded malware from smish: 11%
*   Gave personal info to a scammer: 9%
*   Gave password to untrustworthy actor: 8%
*   Took any type of risk action: 34%

![Figure 2: Risky behaviors exhibited by users.](https://www.verizon.com/business/reports/mobile-security-index/assets/images/figure2.png)
*Figure 2: Risky behaviors exhibited by users. Proofpoint¹⁰*

⁹ Proofpoint, State of the Phish 2023, 2023
¹⁰ ibid.
¹¹ Fortinet, 2023 Security Awareness and Training Global Research Brief, 2023

### The danger of security fatigue

Fatigue is a serious concern. Let’s face it, having to remember and enter passwords is boring. Having to be constantly vigilant is tiring. People have a lot to think about.

The risks of security fatigue are demonstrated by the increase in cyber-insurance claims connected with multifactor authentication (MFA) spamming attacks. According to cyber-insurance group Coalition, these have been steadily growing since September 2022.¹²

#### A false sense of security

MFA is supposed to help improve security. But as we’ve discussed in previous reports, it’s not a panacea. In fact, the false sense of security that having MFA in place can generate is a risk in itself.

Increasingly SMS- and authenticator-app-based types of MFA are being supplanted. Many applications now use a form of MFA where users are asked to respond—typically accept or reject—to an alert on their mobile device. In an MFA spamming attack, the perpetrator bombards the user with prompts in the hope that the person will click “accept” to make the annoyance go away. Some do.

In 2022, Uber suffered a high-profile—although, it said, fairly harmless—breach due to MFA fatigue.¹³ The attacker used a contractor’s compromised VPN credentials to repeatedly attempt to log in. When this didn’t succeed, the attacker contacted the victim on WhatsApp and, pretending to be Uber IT support, encouraged the employee to accept the request. They did. The attacker was able to exploit access to the VPN to move laterally to breach critical systems such as the company’s email, cloud storage and code repository.

Uber was not the only target. In response to these attacks, Microsoft issued an update that requires users responding to MFA push notifications to input a number that appears on the screen of the device that is trying to log in. The update also adds additional context to requests, including application name, device location and IP address. Okta and Duo have followed suit with similar updates.

> 74% of all breaches include the human element.
>
> Verizon 2023 DBIR¹⁴
>
> Even as organizations spend billions every year to shore up their infrastructure, they may be neglecting the people-based security risks that matter most. People are the easiest and most lucrative entry point into your environment.
>
> Proofpoint¹⁵

¹² Coalition, MFA spamming attacks increase cyber claims, 2023
¹³ Lookout, Social Engineering and VPN Access: The Making of a Modern Breach, 2022
¹⁴ Verizon, Data Breach Investigations Report (DBIR) 2023, 2023
¹⁵ Proofpoint, The Definitive Email Cybersecurity Strategy Guide, 2022

### Is working from home here to stay?

Not long ago it seemed like working from home could become the norm. Immediately after lockdowns were lifted, users were reluctant to return to the office. But now, lots of companies—even some of those that benefited most from the increase in remote working—are now encouraging—in some cases forcing—workers back to the office.

According to research by Ivanti, nearly half of knowledge workers are now back in the office. Interestingly, it found that the C-suite was most likely to be following a hybrid model—60% of respondents.

#### Current working model

| Role      | Office worker | IT worker | C-suite |
| :-------- | :------------ | :-------- | :------ |
| In office full-time | 47%           | 10%       | 29%     |
| Hybrid (employer controlled) | 14%           | 22%       | 10%     |
| Hybrid (employee controlled) | 49%           | 19%       | 30%     |
| At home full-time | 53%           | 10%       | 7%      |

![Figure 3: Ivanti.](https://www.verizon.com/business/reports/mobile-security-index/assets/images/figure3.png)
*Figure 3: Ivanti¹⁶*

Hybrid working is certainly popular with users. One in five (20%) said they’d be prepared to take a pay cut to continue working from home at least part of the time—and a not insignificant one, the average was 8%.¹⁷

Almost half (49%) of workers currently working in the office would prefer to follow another model. Almost three-quarters (73%) of them would like a hybrid model.¹⁸

#### Current vs preferred working model

| Arrangement | Current | Preferred |
| :---------- | :------ | :-------- |
| Office full-time | 42% | 24% |
| Hybrid (employer) | 10% | 3% |
| Hybrid (employee) | 34% | 47% |
| WFH or anywhere | 14% | 26% |

![Figure 4: What best describes your current/preferred working arrangement? Ivanti.](https://www.verizon.com/business/reports/mobile-security-index/assets/images/figure4.png)
*Figure 4: What best describes your current/preferred working arrangement? Ivanti¹⁹*

> We believe that a structured hybrid approach—meaning employees that live near an office need to be on site two days a week to interact with their teams—is most effective for Zoom. As a company, we are in a better position to use our own technologies, continue to innovate, and support our global customers.
>
> A Zoom company spokesperson reported in the New York Times²⁰

¹⁶ Ivanti, Elevating the Future of Everywhere Work, 2023
¹⁷ ibid.
¹⁸ ibid.
¹⁹ ibid.
²⁰ New York Times, Even Zoom Is Making People Return to the Office, 2023

### Taking work home or bringing risks to work?

The increase in remote working is not without its downsides. A survey by Fortinet found that 62% of companies had experienced a security compromise that was at least partly attributable to remote working in the past three years.²¹

> 62% of companies suffered a security breach connected to remote working.
>
> An HBR study of remote workers found that, 67% of the participants reported failing to fully adhere to cybersecurity policies at least once, with an average failure-to-comply rate of once out of every 20 job tasks.
>
> Harvard Business Review²³

See section on home Wi-Fi security on page 22.

![Figure 5: Did you experience a security breach during the past two to three years that could be at least partially attributed to an employee working remotely? Fortinet.](https://www.verizon.com/business/reports/mobile-security-index/assets/images/figure5.png)
*Figure 5: Did you experience a security breach during the past two to three years that could be at least partially attributed to an employee working remotely? Fortinet²²*

The inability to extend corporate security to a non-owned environment means that working from home presents several potential additional risks, including:

*   Poorly secured home networks—including unpatched devices, weak encryption and lax password management
*   Multiple unknown users and devices—family, friends, housemates, smart home devices, etc.
*   Increased use of work devices for personal tasks—including by family members
*   Lower policy adherence—users may be less rigorous about following security policies in a non-corporate environment

Ideally, organizations would be able to establish consistent policies across all devices and all locations. Fortinet found that companies are evenly split: 42% use the same vendors across endpoint device types and 42% use different vendors.

²¹ Fortinet, 2023 Work-from-Anywhere Global Study, 2023
²² ibid.
²³ Harvard Business Review, Research: Why Employees Violate Cybersecurity Policies, 2022

## Users not as savvy as they think

Proofpoint has been tracking the awareness of cybersecurity among users and has generally seen an upward trend. Users say all the right things: When asked in surveys, they say that they know to be suspicious of unsolicited emails and to be wary of attachments.

*   89% know to be cautious of unexpected emails
*   84% know email attachments can have damaging software
*   79% know an email can appear to come from someone other than the sender
*   37% know an email link might not match the website it goes to

![Figure 6: Awareness of threats among users.](https://www.verizon.com/business/reports/mobile-security-index/assets/images/figure6.png)
*Figure 6: Awareness of threats among users. Proofpoint²⁴*

> Most employees want to be able to work anywhere—in the office when meetings require it, at home (or away) when it benefits them. But delivering on Everywhere Work requires a change of mindset, culture and technology. And securing it will be among the top priorities—and accomplishments—of 2023.
>
> Ivanti²⁶

Yet, the evidence shows otherwise. IBM’s X-Force Threat Intelligence Index found that 53.2% of victims clicked on the link in a simulated targeted phishing attack.²⁵ As we’ve said before, attackers continue to rely on phishing because it works.

²⁴ Proofpoint, State of the Phish 2023, 2023
²⁵ IBM, 2022 X-Force Threat Intelligence Index, 2022
²⁶ Ivanti, Elevating the Future of Everywhere Work, 2023

## Phishing is still a popular pastime.

The 2023 DBIR reported a doubling of “Social Engineering” incidents, largely due to the use of pretexting—a tactic commonly used in business email compromise (BEC) attacks. Compounding the problem, the median amount stolen in these has increased over the past couple of years, reaching $50,000.²⁷

Data from Lookout on the number of unique URLs accessed by users on both consumer and enterprise devices (see Figure 7) shows that the number interacting with more than six malicious links is increasing each year. This is probably due to the increasing sophistication of phishing campaigns and the blurring of the lines between personal and work use on mobile devices.

> The mobile device presents a fundamentally different environment from a laptop or desktop. These devices can give a significant leg up to attackers who use the smaller screens, simplified interfaces and hidden URLs to their advantage. This, coupled with our natural tendency to immediately tap on anything that comes up on our smartphone or tablet screen, gives phishing attacks a higher chance of success.
>
> Aaron Cockerill, Executive VP of Products, Lookout

| Number of devices on which a phishing link was clicked | Enterprise devices | Personal devices |
| :----------------------------------------------------- | :----------------- | :--------------- |
| 2020                                                   | 8.2%               | 20.4%            |
| 2021                                                   | 27.5%              | 38.0%            |
| 2022                                                   | 54.2%              | 48.2%            |

| Link Count | Enterprise devices | Personal devices |
| :--------- | :----------------- | :--------------- |
| 1 link     | 20.4%              | 27.5%            |
| 3–5 links  | 38.0%              | 54.2%            |
| 6+ links   | 48.2%              | 20.4%            |

![Figure 7: Analysis of users clicking on dangerous links.](https://www.verizon.com/business/reports/mobile-security-index/assets/images/figure7.png)
*Figure 7: Analysis of users clicking on dangerous links. Lookout²⁸*

> 84% of organizations experienced at least one successful phishing attack between September 2021 and August 2022.
>
> Proofpoint³⁰
>
> 80% of phishing sites target mobile devices specifically or are designed to function both on desktop and mobile. Meanwhile, the average user is 6–10 times more likely to fall for SMS phishing attacks than email-based attacks.
>
> Zimperium³¹

Despite this, nearly two-thirds (65%) of companies still don’t perform phishing simulations.²⁹ And, we’d venture to say, even those that do rarely scope non-email-based variants (such smishing, using SMS messages) into their campaigns.

²⁷ Verizon, Data Breach Investigations Report, 2023
²⁸ Lookout, The Global State of Mobile Phishing, 2023
²⁹ Proofpoint, State of the Phish 2023, 2023
³⁰ ibid.
³¹ Zimperium, 2023 Global Mobile Threat Report, 2023

### Everything is going hybrid.

Hybrid phishing combines multiple techniques to increase the effectiveness of attacks. This often includes a combination of large-scale, automated tactics and more targeted methods. For example, pairing an email phishing attack with a voice-phishing (vishing) attack.

Telephone-oriented attack delivery (TOAD) is a form of hybrid phishing that emerged in 2021. Since then, the number of instances of this type of attack has been steadily rising. Proofpoint said that it sees up to 600,000 TOAD messages per day.³² That’s a tiny number compared to the total number of phishing messages sent—many individual phishing campaigns send millions of messages. But the higher degree of effectiveness makes this type of attack something to take very seriously.

Adding a vishing element to a click-targeted phishing campaign tripled its effectiveness, eliciting a click from 53.2% of recipients, according to IBM’s 2022 X-Force Threat Intelligence Index.³³

A typical TOAD attack consists of sending a message containing one of the common phishing messages or payloads—such as a fake invoice, an update on an invented delivery or a warning about an account being compromised and the password needing to be reset. What sets it apart from a standard phishing attack is the inclusion of a customer service (or should that be victim service?) number for recipients with questions.

This lends credibility to the attack. It shouldn’t.

### Big exec compromise?

Business email compromise (BEC) attacks, which we covered in detail in the 2022 Mobile Security Index, continue to be one of the most lucrative types of attack for cybercriminals. The Federal Bureau of Investigations (FBI) IC3 unit has reported that Investment and BEC attacks made up over half of the US $10.3 billion in losses reported to it in 2022. The reported losses associated with BEC attacks averaged US $125,611.67 each.³⁴

*   Investment fraud: $3,311,742,206 (~37 Boeing 737-700s (sticker price))
*   Business email compromise: $2,742,354,049 (~31 Boeing 737-700s (sticker price))

> Don’t believe your eyes or ears.
>
> The recent growth of generative artificial intelligence (GAI) has shown that we can no longer believe our eyes. Anybody with internet access can create a deep fake image or video. Attackers are exploiting this technology to make phishing attacks even more effective.
>
> Researchers have found that seven words can be enough of a sample to create a believable impersonation of an individual’s voice. That YouTube interview with the CEO could very easily be turned into a convincing voicemail instructing an employee to change the payment details of a large supplier or reset credentials to an important system.

![Figure 8: Reported losses in 2022. Top two categories.](https://www.verizon.com/business/reports/mobile-security-index/assets/images/figure8.png)
*Figure 8: Reported losses in 2022. Top two categories. FBI³⁵*

³² Proofpoint, State of the Phish 2023, 2023
³³ IBM, 2022 X-Force Threat Intelligence Index, 2022
³⁴ FBI, Internet Crime Report 2022, 2022
³⁵ ibid.

The COVID-19 crisis forced many companies to adapt quickly. They generally did a pretty good job of adjusting to the new reality, including enabling remote work. But now they’re thinking about the future, how to secure the business, and how to support users in a sustainable and flexible way.

As remote working increases and workloads shift to the cloud, many are turning to approaches based on zero trust and secure access service edge (SASE). These approaches are designed for the hybrid-working, cloud-first, mobile-first and perimeter-less world of today—and tomorrow.

The traditional way to secure remote workers was to use a virtual private network (VPN). Once established, a VPN connection is trusted implicitly. With this model, potentially thousands of devices, applications and users could have wide-ranging access to the organization’s network and sensitive data. It was also not a very user-friendly experience.

If employees can’t easily access the applications and systems they need to do their work, they may not be as productive. It’s a delicate balance, but you can deliver a frictionless remote work experience while also helping to keep the organization secure.

A zero-trust approach can help strengthen a company’s security policy and make it more resilient. It can also improve the user’s experience. For example, intelligent, analytics-driven identity access management solutions can automate the process of determining when to grant a specific user access to certain applications. AI-driven threat detection solutions can also help the organization detect anomalies, suspicious user behavior and network activity, and isolate these threats before a breach occurs.

With this approach, employees:

*   Don’t have to deal with onerous authentication requirements
*   Aren’t unintentionally blocked from systems they need to do their jobs
*   Aren’t given unauthorized access to sensitive data

A zero-trust model can also help give employees the flexibility they want. With an approach focused on verification rather than implicit trust, companies can deliver a better employee experience and remain agile in the increasingly complex threat environment.

Zero trust is one of the foundational components of the SASE framework.

> While the promise of digital transformation remains a priority, the reality for most enterprise technology teams is that managing and securing an increasingly complex IT environment poses major challenges. This paper explores how SASE can help secure and optimize your unique network environment.
>
> Read more〉

## Balancing security and user experience

## Applications

### Malware

Before you skip ahead, thinking you’ve got this one in hand, pause for a minute to consider that nearly 1 in 10 (9%) organizations were hit by mobile malware in 2022.³⁶

Check Point identified a “vast increase in the number of malicious applications infiltrating Google and Apple stores.” One approach is to create a simple app—like an “improved flashlight” or a puzzle to make that long journey less boring—with malware baked in. Apps like this raise few red flags in people’s minds—“It’s only a flashlight, what harm can it cause?” But many attackers now hide their malicious code in modified versions of legitimate apps.

These malicious variants (MVs) can appeal to users for several reasons. Who hasn’t searched for an app to perform a one-off task, then edited the search to include the word “free?” Attackers often tempt users with a free trial or extended functionality not available in the legitimate free version. This isn’t just about games with extra lives or other frivolous things. Attackers have released modified versions of apps like OpenVPN and SoftVPN.

App updates that take away popular features—as some social platforms have done recently—are a boon for attackers. Users can be tempted with the promise to revert to a version with the functionality they miss. The modified app doesn’t even have to deliver, just get the user to try it.

One of the weaknesses with apps is that it’s quite difficult to tell what data they are sending and how securely. Awareness of threats has grown over the years. For example, many users know to look out for the padlock when visiting a website. They may not know exactly what it means, but they know it’s important. However, when using an app, there’s no reliable visible indicator that data is encrypted in transit.

> +30% Mobile app threats increased by over 30% between the first half of 2022 and the first half of 2023.
>
> Lookout³⁷
>
> 40% Malware showed up in 40% of breaches.
>
> Verizon 2023 DBIR³⁸

³⁶ Check Point, 2023 Cyber Security Report, 2023
³⁷ Lookout, Lookout Security Graph, 2023
³⁸ Verizon, 2023 Data breach Investigations Report, 2023

### Ransomware

Over the past few years, ransomware has risen faster than a K-pop band. It can take many forms: crypto ransomware, lockers, scareware and doxware. As awareness has grown, so has preparedness. But the attacks keep happening, and many companies are affected.

Some may be under the illusion larger enterprises are a more attractive target as they present a higher potential payoff, but an Akamai analysis of victims by revenue paints a different picture.³⁹ More than 60% of victims have annual revenue under $50 million per year—but obviously, there are more organizations of this size. Organizations with revenue of over $1 billion make up only 0.03% of the total population, but over 8% of the victims.

![Figure 9: Number of companies falling victim to a ransomware attack by company size.](https://www.verizon.com/business/reports/mobile-security-index/assets/images/figure9.png)
*Figure 9: Number of companies falling victim to a ransomware attack by company size. Data from October 1, 2021 to May 31, 2023. Akamai⁴⁰*

> Ransomware continues to be a major threat for organizations of all sizes and industries and is present in 24% of breaches.
>
> Verizon 2023 DBIR⁴²

IBM’s 2023 Cost of a Data Breach report found that despite ongoing efforts by law enforcement to collaborate with ransomware victims, 37% of respondents opted not to bring them in. Nearly half (47%) of studied victims paid the ransom.⁴¹

³⁹ Akamai, Ransomware on the Move, 2023
⁴⁰ ibid
⁴¹ IBM, Cost of a Data Breach Report 2023, 2023
⁴² Verizon, 2023 Data