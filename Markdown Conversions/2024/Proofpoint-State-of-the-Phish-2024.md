# 2024 State of the Phish Report

## Table of Contents
- [Introduction](#introduction)
- [Key Findings](#key-findings)
- [Security Behaviors and Attitudes](#security-behaviors-and-attitudes)
- [Security Awareness Trends](#security-awareness-trends)
- [The Threat Landscape](#the-threat-landscape)
- [Organizational Benchmarks](#organizational-benchmarks)
- [Conclusion](#conclusion)

## Introduction
Imagine a successful cyberattack against your organization. What does it look like? Maybe it involves a fiendishly clever piece of social engineering—a convincing lure that catches the recipient off guard. Or maybe it would take a smart technical exploit to get past your defenses. But in reality, threat actors don’t always have to try that hard.

Often, the easiest way to breach security is to exploit the human factor. People are a key part of any good defense, but they can also be the most vulnerable. They may make mistakes, fall for scams or simply ignore security best practices. According to this year’s State of the Phish survey, 71% of working adults admitted to taking a risky action, such as reusing or sharing a password, clicking on links from unknown senders, or giving credentials to an untrustworthy source. And 96% of them did so knowing that they were taking a risk.

When obliged to choose between convenience and security, users pick the former almost every time. So, what can organizations do to change this? In this report we’ll take a closer look at how attitudes towards security manifest in real-world behavior, and how threat actors are finding new ways to take advantage of our preference for speed and expedience. We’ll also examine the current state of security awareness initiatives, as well as benchmarking the resilience of people and organizations against attack.

The foundation of this report is a survey of 7,500 end users and 1,050 security professionals, conducted across 15 countries. It also includes Proofpoint data derived from our products and threat research, as well as findings from 183 million simulated phishing messages sent by our customers over a 12-month period and more than 24 million emails reported by our customers’ end users over the same period.

## Key Findings
- 69% of organizations were infected by ransomware.
- Over 1 million attacks are launched with MFA-bypass framework EvilProxy every month, but 89% of security professionals still believe MFA provides complete protection against account takeover.
- 71% of users took a risky action and 96% of them knew they were doing something risky.
- Over 1 million BEC attacks were detected and blocked on average per month by Proofpoint.
- 58% of users who took risky actions engaged in behavior that would have made them vulnerable to common social engineering tactics.
- 85% of security professionals said that most employees know they are responsible for security, but 59% of users either weren’t sure or claimed that they’re not responsible at all.
- 10 million TOAD messages are sent every month.
- Microsoft continues to be the most abused brand, with 68 million malicious messages associated with the brand or its products.

## Security Behaviors and Attitudes
Even the best technical defenses can be undermined if users don’t do the basics, such as avoiding suspicious links, verifying the sender’s identity and setting a strong password and keeping it to themselves. However, many users fail to follow these simple rules, putting themselves and their organizations at risk.

### End-user behavior and attitudes
According to our survey, 71% of users said they took a risky action and almost all of them—96%—did so knowingly. Among that group, 73% said they’d taken two or more risky actions. And more than a third of the risks they took were rated by those users as either “extremely risky” or “very risky.”

![Risky Actions Taken]

- 29% Use work device for personal activities
- 26% Reuse or share password
- 26% Connect without using VPN at a public place
- 24% Respond to a message (email or SMS text) from someone I don’t know
- 20% Access inappropriate website
- 19% Click on links or download attachments from someone I don’t know
- 16% Share work device with friends or family
- 13% Call an unfamiliar phone number in an urgent email
- 11% Tailgating: allow others to enter the office without badging in
- 10% Upload sensitive data to unproven third-party cloud
- 9% Give credentials to untrustworthy source
- 29% Have never taken a risky action

Users took risky actions for a variety of reasons: convenience, time saving and urgency being the most common answers. But a small cohort of 2.5% took risky actions purely out of curiosity. Either way, the message is clear: people aren’t taking risky actions because they lack security awareness. Often, users know what they are doing when they take risks and are quite willing to gamble with organizational security.

Nobody knows this better than the world’s cybercriminals. They understand that people can be exploited, either through negligence, obliviousness or—in rare instances—malice. Social engineering is a part of almost every email threat analyzed by our researchers. And 58% of users who took a risky action said they engaged in behavior that would put them at risk of basic social engineering tactics, such as clicking on unknown links, responding to unfamiliar senders and sharing credentials with untrustworthy sources. These actions can lead to ransomware infection, malware, data breach or financial loss.

![Why Risky Action is Taken]
- 44% It is convenient
- 39% To save time
- 24% To meet an urgent deadline
- 19% To meet other performance objectives
- 11% To save money
- 10% Other, please specify
- 5% To achieve a revenue target

One of the reasons users take these risks is a lack of consensus about accountability and responsibility. Only 41% of users said they know that they bear responsibility for cybersecurity at their workplace. About 7% claimed that they aren’t responsible at all, while the majority (52%) weren’t sure.

### The professional view
Security professionals understandably have a different perspective on security risks to end users. They are more aware of the threat landscape and the consequences of a breach. And they have a more nuanced understanding of the challenges that go into securing complex and dynamic environments. They also have the unenviable task of finding ways to balance the need for security with the need for unhindered productivity and efficiency.

According to our survey of security professionals, they rate users with access to business-critical data as the biggest security risk (63%)—a group that is inevitably hard to manage, as much of that access is necessary. But click-happy users and those who don’t complete security awareness training are close behind in joint second place (56% each). These categories of user were all considered significantly more risky than executives/VIPs (34%), despite the latter group often having broad access to valuable data.

This contrasts with the view among security professionals, 85% of whom say that most employees know they are responsible for security. This gap between perception and reality suggests that there is a need for clearer communication about shared responsibility, rather than just more training on security best practices and policies.

![Perception on Security Responsibility]
- Security Professionals: 85% Yes – Employees think they are responsible for security, 13% No – Employees believe security is not their responsibility, 2% Not sure
- Employees: 41% Yes – Employees think they are responsible for security, 7% No – Employees believe security is not their responsibility, 52% Not sure

63% of security professionals rated users with access to critical business data as the top cybersecurity risk

![Users Who Represent Risk]
- 63% Users who have business privilege and access to critical data
- 56% Users who are click happy
- 56% Users who consistently fail to complete training assignment
- 49% Suppliers or business partners
- 42% People who are leaving
- 34% VIPs, executives

Unfortunately, our survey reveals significant overlap between the riskiest behaviors identified by security professionals and the most common risky actions taken by end users. Reusing passwords, using work devices for personal activities and accessing inappropriate websites are among behaviors considered the most unsafe; all of them appeared in the top actions taken by users.

This overlap suggests that users may be taking some of these actions because they are unaware of just how risky they are considered by security teams.

![Top Risks Considered by Infosec vs. Top Risky Actions Taken by Users]
**Top Risks Considered by Infosec**
1. Click on links or download attachments from someone I don’t know
2. Connect without using VPN at a public place
3. Respond to a message (email or SMS text) from someone I don’t know
4. Upload sensitive data to unproven third-party cloud
5. Reuse or share password

**Top Risky Actions Taken by Users**
1. Reuse or share password
2. Access inappropriate website
3. Use work device for personal activities

## Security Awareness Trends
While training alone isn’t enough to change unsafe behavior, teams that lack basic security awareness tools and knowledge are still much more likely to fall prey to cybercriminals. But as new social engineering lures and techniques appear on the threat landscape, awareness programs must be agile and broad-based to remain relevant.

### Current state of security awareness
First some positive news: 99% of respondents said they have a security awareness program of some sort up and running. But while the basics may already be in place, many are struggling to drive real behavioral change. A possible reason for this is that only 53% say they train everyone in the organization (down from 56% last year). This means that some users may be left out of the loop or may receive inadequate or outdated training.

Another challenge is the coverage and relevance of training topics. Security professionals agree that remote work, password hygiene and internet safety are critical, but less than a third of security awareness programs cover all these topics. The top training topics cited by respondents were malware, Wi-Fi security, ransomware and email phishing, which are all important, but not sufficient to address the full spectrum of risks. And as we’ll see later when we examine the latest cybercriminal tactics and techniques, emerging threats can quickly become commonplace, taking unprepared users by surprise.

![Security Awareness Activities Assignment]
- 2022: 56% Everyone in the organization, 28% Only specific departments and roles, 15% Only specific individuals, 1% Not sure
- 2023: 53% Everyone in the organization, 41% Only specific departments and roles, 6% Only specific individuals, 1% Not sure

On the positive side, the survey shows some signs of improvement and innovation in security awareness tactics. Year over year, training of specific roles and departments has risen significantly (41% from 28%), indicating a more tailored and targeted approach. Time allocated to user education has also increased year over year, with more respondents dedicating over three hours per year to awareness training. Overall, the average amount of time dedicated to awareness training has increased for the first time in three years.

![Time Allocated for Security Awareness Activities]
- 6% 30 minutes or less
- 17% 31–59 minutes
- 15% 1–2 hours
- 25% 3–4 hours
- 37% More than 4 hours

The types of tactics being used are evolving, too, with a 23% increase in the use of contests and prizes to gamify and incentivize attention. This change can help increase user engagement and motivation, while also creating a positive and fun learning environment. Computer-based training remains the most common format (45%), but other methods such as simulated USB drops, videos, posters and newsletters are also being used.

![Security Awareness Tactics]
- 45% Computer-based training
- 38% Awareness posters and videos
- 37% In-person training sessions
- 34% Simulated phishing attacks
- 34% Internal cybersecurity chat channel
- 33% Cybersecurity-based contests and prizes
- 31% Internal wiki
- 30% Smishing and vishing simulations
- 23% Simulated USB drops
- 23% Newsletters and emails
- 1% My company does not have a security awareness program
- 41% from 28% The percentage of organizations that trained specific roles jumped year over year

However, only 34% of respondents say they perform simulated phishing attacks, despite the high volume of malicious email seen in the threat landscape. This suggests that there is still room for improvement in the composition of most security awareness training syllabuses.

### Areas for improvement
Security is not only a technical issue, but also a cultural and organizational one. It requires the collaboration and commitment of all stakeholders, from security professionals to end users. However, there is often a gap between what security professionals think is effective and what end users say would motivate them to prioritize security

According to our survey, security professionals believe that more training, tighter controls, closer business alignment, better rewards and stronger championing of security initiatives would all be effective in improving security. However, fewer than a third of organizations reward positive user behaviors or champion security initiatives. These are important ways to recognize and reinforce good security practices, and to ensure that all employees are invested in creating a security-aware culture.

In contrast, users overwhelmingly say that they want security to be made easier. They want processes to be more user-friendly, convenient and transparent, and they want to have more communication and feedback from security experts. Users overwhelmingly agree (94%) that improving ease of use would motivate them to be more attentive to security. These disparities between security team actions and user motivations clearly demonstrate the need for open communication between security teams and end users.

![Actions Taken by Security Pros vs. User Motivation]
**Actions Taken by Security Pros**
1. Provide more training
2. Implement more security controls or restrictions
3. Align security initiatives with business priorities

**User Motivation**
1. Making security easier for me
2. Using rewards and recognition
3. Increased engagement from leadership or security team

- 83% of surveyed security professionals implement more training to drive behavior change
- 81% implement more controls or restrictions

![What Policies Motivate Users to Prioritize Cybersecurity]
- 94% Making security easier for me
- 89% Using rewards or recognition
- 87% Increased engagement from leadership or security team
- 85% More training or different styles of training
- 71% Punishment, such as reduction in pay, bonus removal, job termination
- 6% Not Motivating
- 11% Not Motivating
- 13% Not Motivating
- 15% Not Motivating
- 29% Not Motivating

In keeping with trends we’ve observed over the past few years, punishing unwanted behavior was considered the least effective approach by security professionals. Fortunately, it was also the least implemented. Punishment can have negative effects, such as creating fear, resentment and distrust, and reducing motivation and morale. It can also discourage users from reporting incidents or seeking help, which can seriously increase the risk of security breaches. Punishment was also the least motivating response among end users, though 71% still agreed that this would be an incentive for them. This suggests that some users may be willing to comply with security rules to avoid negative consequences, though it is unlikely that compelled participation will lead to enduring behavior change.

## The Threat Landscape
Cybersecurity is a constantly evolving field as cybercriminals devise new and sophisticated ways to attack people and breach organizations. Users who take risks, such as clicking on suspicious links, opening unknown attachments or using weak passwords, face an increasing variety of real-world threats from attackers.

### Threat prevalence
Some of the most common forms of attack reported by survey participants were phishing, business email compromise (BEC) and ransomware. While each of these techniques is distinct, security teams will often encounter them as individual components of an extended attack chain, with phishing leading to ransomware, or a supply chain attack leading to BEC.

![Prevalence of Attacks]
- 2022: 72% Bulk Phishing, 74% Spear Phishing, 73% BEC, 77% Ransomware, 67% Smishing, 66% Vishing, 66% TOAD (Callback Phishing), 64% Data Loss via Insider, 68% Data Loss via External Attacker, 67% Supply Chain Risk, 74% Social Media, 76% USB Drop
- 2023: 76% Bulk Phishing, 74% Spear Phishing, 75% BEC, 76% Ransomware, 71% Smishing, 69% Vishing, 69% TOAD (Callback Phishing), 66% Data Loss via Insider, 71% Data Loss via External Attacker, 74% Supply Chain Risk, 65% Social Media, 60% USB Drop

However, these aren’t the only threats that users and organizations need to be aware of. According to our own data, many novel attack types are becoming increasingly prominent.

### Growing threats: TOAD, MFA-Bypass, QR codes and generative AI
In telephone-oriented attack delivery (TOAD), the malicious message often appears to be completely benign, containing nothing more than a phone number and some erroneous information. It isn’t until the unsuspecting victim calls the listed number for help that the attack chain is activated. Cybercriminal call centers are operating around the world, guiding victims into granting remote access, revealing sensitive information and credentials, or even infecting themselves with malware. Our data reveals that an average of 10 million TOAD messages are sent every month.

Another increasingly popular attack method involves using advanced techniques to bypass multifactor authentication (MFA), which is now a standard part of corporate cybersecurity. These attacks typically use proxy servers to intercept MFA tokens, allowing attackers to circumvent the additional layer of security provided by one-time codes and biometrics. Several off-the-shelf phish kits now include MFA bypass functionality, allowing even relatively unsophisticated attackers to benefit. We see around 1 million phishing threats using the popular EvilProxy framework every month. This is of particular concern, as 89% of security professionals still consider MFA to be a silver bullet for protection against account takeover, with 84% of respondents saying their organizations use MFA to prevent account takeover.

- 13 million Proofpoint saw over 13M TOAD attacks at peak in August 2023
- 89% of security pros believe that MFA can protect against account compromise completely

![Does MFA Provide Complete Protection Against Account Takeover?]
- 47% Completely agree
- 42% Somewhat agree
- 9% Neither agree or disagree
- 1% Somewhat disagree
- 2% Completely disagree

And within the paradigm of traditional phishing, attackers are finding new ways to embed malicious content. In recent months we’ve seen an increase in the use of QR codes as an alternative to links or attachments. This technique is particularly dangerous, as it both attempts to evade automated detection while presenting users with a familiar format in a context they may not have seen before. It is also impossible to tell just by looking if a QR code leads to a phishing site or malware download. Unfamiliar users scanning a QR code may not even be aware that they’ve engaged with a piece of malicious content until it’s too late.

It’s also worth noting that even the least common type of attack—USB drop—was still reported by 60% of respondents. This shows that cybercriminals are willing to try any tactic, old or new, if they think it will give them a chance to exploit an unsuspecting victim.

Despite the growing prominence and sophistication of these threats, many organizations are not adequately prepared or trained to deal with them. Only 23% of organizations train their users on how to recognize and prevent TOAD attacks, and only 23% educate their users on generative AI safety.

Generative AI is a technology that can create realistic and convincing content—such as images, videos or text—based on a given prompt or data input. This technology promises to enhance social engineering for all messaging-based attacks, as attackers can use it to improve the quality of their lure, particularly when targeting other languages. Moreover, generative AI also poses a risk of data loss, as there is currently little transparency over what happens to data that is uploaded to services such as ChatGPT and Google Bard.

### BEC attacks benefit from AI
BEC attacks also continue to pose a serious threat, especially in non-English-speaking countries. Fewer organizations reported BEC attempts globally, but attacks continue to grow in prevalence among countries such as Japan (35% year-over-year increase), Korea (31% jump), and UAE (29% jump). These countries may have previously seen fewer BEC attacks due to language barriers, cultural differences or lack of visibility. But there is now a likely link between BEC and generative AI, as attackers can use the latter to create more convincing and personalized emails in multiple languages. Our own data shows an average of 66 million targeted BEC attacks every month.

### Microsoft remains most-abused brand
Brand abuse is a favorite tactic for phishing and malware delivery, as attackers exploit the trust and familiarity that users have with certain brands. More than 68 million messages were associated with Microsoft products and brand in 2023, making it the most abused brand by cybercriminals. Adobe and DHL rounded out the top three, but at fewer than 10 million messages each.

- 68 million malicious messages included references to Microsoft and/or Microsoft products in 2023, making the software giant the world’s most abused brand

![Brand Abuse Threats (Millions)]
- 68 Microsoft
- 9.4 Adobe
- 8.8 DHL
- 6.1 Google
- 4.4 AOL
- 3.5 DocuSign
- 3.1 Amazon

- 20 million Office 365 was the most abused Microsoft product in malicious email, with over 20 million email threats using the brand

### Ransomware still a major concern
The percentage of organizations that faced a ransomware attack rose 5 percentage points to 69%. Almost 60% of organizations reported four or more separate ransomware incidents in a year, indicating that ransomware is still a persistent and lucrative form of attack.

![Ransomware by the Numbers]
- 39% 1–3 separate incidents
- 38% 4–6 separate incidents
- 15% 7–9 separate incidents
- 5% 10 or more separate incidents
- 3% Unsure

One of the ways that organizations try to mitigate the risk and impact of cyberattacks is by purchasing cyber insurance, which covers the costs and damages associated with a cybersecurity incident. Among those that had experienced a ransomware incident, 96% now have cyber insurance. Most insurers (91%) helped with ransom payments, up from 82% the year before. However, globally, the rate of payment to ransomware attackers has declined from 64% to 54%.

![Infected Organizations That Agreed to Pay Ransom]
- 2021: 58%
- 2022: 64%
- 2023: 54%

- 15% of organizations refused to pay more than one ransom after their first payment didn’t get their data back, up from just 6% in 2022

The number of respondents who regained access to their data after paying also declined, with the number who regained access after a single payment seeing the largest decline. This may be one explanation for the drop in payments. Another possible reason is that organizations are becoming more aware of the drawbacks and risks of paying ransoms, such as encouraging more attacks, funding criminal activities or receiving corrupted or incomplete data.

![Ransomware Infections: What Happens After Payment]
- 2022: 52% Regained access to data after first payment, 41% Paid additional ransom demand(s) and eventually, 6% Refused to pay addtional ransom demand(s) and walked, 1% Never got access to data even after paying ransoms
- 2023: 41% Regained access to data after first payment, 43% Paid additional ransom demand(s) and eventually, 15% Refused to pay addtional ransom demand(s) and walked, 1% Never got access to data even after paying ransoms

### Attack consequences
The impact of phishing attacks on organizations can be devastating, both financially and reputationally. 71% of organizations experienced at least one successful phishing attack in 2023, down from 84% in 2022. However, while the incidence of successful phishing attacks has declined, some of the negative consequences have soared. Year on year, we saw a 144% increase in reports of financial penalties, such as regulatory fines, and a 50% increase in reports of reputational damage due to phishing incidents.

![Results of Successful Phishing Attacks]
- 2022: 32% Loss of data / intellectual property, 29% Ransomware infection *, 27% Breach of customer / client data, 27% Credential / account compromise, 25% Reputational damage, 22% Widespread network outage / downtime, 20% Advanced persistent threat, 21% Direct financial loss **, 9% Financial penalty ***, 22% Other malware infection(s), 22% Zero-day exploit, 28% I’m not sure
- 2023: 33% Loss of data / intellectual property, 44% Ransomware infection *, 76% Breach of customer / client data, 18% Credential / account compromise, 44% Reputational damage, 26% Widespread network outage / downtime, 36% Advanced persistent threat, 30% Direct financial loss **, 67% Financial penalty ***, 20% Other malware infection(s), 2% Zero-day exploit, 71% I’m not sure
* malware was delivered via email
** wire transfer or invoice fraud
*** regulatory fine

- 73% of organizations reported a BEC attack, but only 29% teach users about BEC attacks

The threat landscape is constantly evolving, as cybercriminals employ new tactics and techniques in their quest to gain an advantage. This is why it’s key to equip people with the knowledge they need to identify and resist attacks; after all, as sophisticated as these techniques are becoming, people remain their primary target. Most organizations say they use real-world threat intelligence to shape their security awareness program, however there are some major disparities. For example, 73% of organizations experienced a BEC attack, but only 29% train users specifically on BEC threats. Similarly, only 23% of organizations provide training on TOAD attacks, despite their ubiquity. The threat landscape moves pretty fast; if you don’t stop and update your program once in a while you could miss something.

## Organizational Benchmarks
One of the ways that organizations can measure and improve their cybersecurity awareness and resilience is by conducting phishing simulations. Proofpoint phishing simulations mimic real-world phishing scenarios and assess how users respond to them. Our customers conducted 183 million phishing simulations over a 12-month period. Of these, link-based tests were the most common, accounting for 59% of all simulations, followed by data-entry tests (30%) and attachment-based tests (10%). However, attachment-based tests had the highest failure rate overall, at 17%. Failure rates for all types of simulations were within 1 percentage point of last year’s results.

![Simulation Type and Failure Rate]
- Link-based: 2022 failure rate 12%, 2023 failure rate 11%, 2022 frequency of use 66%, 2023 frequency of use 59%
- Data Entry: 2022 failure rate 4%, 2023 failure rate 3%, 2022 frequency of use 27%, 2023 frequency of use 30%
- Attachment: 2022 failure rate 16%, 2023 failure rate 17%, 2022 frequency of use 8%, 2023 frequency of use 10%

We also analyzed failure rates by industry and found some interesting patterns. The finance industry saw the most improvement, with failure rates decreasing by 7 percentage points, from 16% in 2022 to 9% in 2023. On the other hand, the agriculture and construction industries both saw their failure rates increase by 3 percentage points from last year. Although this increase is relatively small, it may point to an underlying issue with security approaches in these industries.

### Current Industry Failure Rate
![Current Industry Failure Rate]
- Marketing/Advertising: 2022 7%, 2023 6%, Change -1%
- Retail: 2022 8%, 2023 7%, Change -1%
- Aerospace: 2022 10%, 2023 7%, Change -3%
- Hospitality/Leisure: 2022 11%, 2023 8%, Change -3%
- Legal: 2022 9%, 2023 8%, Change -1%
- Insurance: 2022 10%, 2023 9%, Change -1%
- Financial Services: 2022 16%, 2023 9%, Change -7%
- Engineering: 2022 10%, 2023 9%, Change -1%
- Agriculture: 2022 8%, 2023 11%, Change 3%
- Real Estate: 2022 11%, 2023 11%, Change 0%
- Energy/Utilities: 2022 12%, 2023 10%, Change -2%
- Non-profit: 2022 11%, 2023 11%, Change 0%
- Entertainment/Media: 2022 12%, 2023 11%, Change -1%
- Technology: 2022 10%, 2023 12%, Change 2%
- Automotive: 2022 11%, 2023 11%, Change 0%
- Consulting: 2022 12%, 2023 10%, Change -2%
- Electronics: 2022 10%, 2023 11%, Change 1%
- Healthcare: 2022 13%, 2023 11%, Change -2%
- Manufacturing: 2022 11%, 2023 12%, Change 1%
- Finance: 2022 16%, 2023 9%, Change -7%
- Government: 2022 10%, 2023 10%, Change 0%
- Education: 2022 11%, 2023 10%, Change -1%
- Mining: 2022 13%, 2023 12%, Change -1%
- Telecommunications: 2022 11%, 2023 12%, Change 1%
- Environmental: 2022 10%, 2023 11%, Change 1%
- Transportation: 2022 12%, 2023 12%, Change 0%
- Business Services: 2022 11%, 2023 11%, Change 0%
- Other: 2022 11%, 2023 10%, Change -1%
- Food and Beverage: 2022 11%, 2023 12%, Change 1%
- Construction: 2022 10%, 2023 13%, Change 3%
- Best Improvement: Finance
- Worst Increase (tie): Agriculture, Construction

Another factor influencing the success or failure of phishing simulations is the content and design of the test phishing emails. Templates are designed to mimic real-world threats; accordingly, our customers featured Microsoft in 7 of the top 10 phishing simulation templates, matching the data about abuse of its brand and products shared in the previous section. The highest failure rate among these templates was for a OneDrive deactivation email, which had a failure rate of 10%. This email claimed that the user’s OneDrive account would be deactivated unless they clicked on a link and verified their identity. A lure like this is designed to trigger feelings of loss aversion and urgency—provoking the strong emotional response that is often at the core of effective social engineering.

![Top Phishing Simulation Templates]
1.  Microsoft: Microsoft deactivation of old OneDrive account - 10%
2.  Microsoft: Microsoft password expiration - 8%
3.  Microsoft: Microsoft voicemail - 7%
4.  Microsoft: Teams reply (phish hook enabled) - 6%
5.  Microsoft: O365 re-authentication - 5%
6.  IT: system update - 5%
7.  Social media: LinkedIn search appearance - 4%
8.  IT: password expiration - 4%
9.  Email account alert: email password change - 4%
10. Microsoft: your storage capacity is full - 2%

Overall, the reporting rates for simulated phishing increased slightly to 18.3%, from 17% in 2022. This means that slightly more users reported the phishing emails they received to their IT or security team, rather than ignoring or deleting them. Reporting rates are an important indicator of user awareness and engagement, as they show that users can recognize and flag suspicious messages.

- 18.3% of simulated phishing emails were properly reported by users in 2023, a slight increase from 2022

![Industry Reporting, Failure and Resilience Factor]
- Aerospace: Reporting Rate 23%, Failure Rate 7%, Resilience Ratio 3.2
- Healthcare: Reporting Rate 14%, Failure Rate 8%, Resilience Ratio 1.7
- Financial Services: Reporting Rate 22%, Failure Rate 8%, Resilience Ratio 2.7
- Not for Profit: Reporting Rate 17%, Failure Rate 11%, Resilience Ratio 1.6
- Legal: Reporting Rate 29%, Failure Rate 9%, Resilience Ratio 3.1
- Other: Reporting Rate 18%, Failure Rate 11%, Resilience Ratio 1.6
- Energy/Utilities: Reporting Rate 26%, Failure Rate 10%, Resilience Ratio 2.7
- Business Services: Reporting Rate 18%, Failure Rate 12%, Resilience Ratio 1.5
- Insurance: Reporting Rate 23%, Failure Rate 9%, Resilience Ratio 2.5
- Construction: Reporting Rate 18%, Failure Rate 12%, Resilience Ratio 1.5
- Marketing/Advertising: Reporting Rate 13%, Failure Rate 6%, Resilience Ratio 2.1
- Agriculture: Reporting Rate 15%, Failure Rate 11%, Resilience Ratio 1.4
- Technology: Reporting Rate 15%, Failure Rate 8%, Resilience Ratio 2.1
- Mining: Reporting Rate 15%, Failure Rate 11%, Resilience Ratio 1.4
- Electronics: Reporting Rate 18%, Failure Rate 10%, Resilience Ratio 1.9
- Transportation: Reporting Rate 15%, Failure Rate 11%, Resilience Ratio 1.3
- Consulting: Reporting Rate 17%, Failure Rate 9%, Resilience Ratio 1.9
- Food and Beverage: Reporting Rate 15%, Failure Rate 12%, Resilience Ratio 1.3
- Engineering: Reporting Rate 17%, Failure Rate 9%, Resilience Ratio 1.8
- Automotive: Reporting Rate 15%, Failure Rate 11%, Resilience Ratio 1.3
- Environmental: Reporting Rate 18%, Failure Rate 10%, Resilience Ratio 1.8
- Entertainment/Media: Reporting Rate 14%, Failure Rate 11%, Resilience Ratio 1.3
- Manufacturing: Reporting Rate 21%, Failure Rate 12%, Resilience Ratio 1.7
- Telecommunications: Reporting Rate 14%, Failure Rate 11%, Resilience Ratio 1.2
- Retail: Reporting Rate 18%, Failure Rate 10%, Resilience Ratio 1.7
- Education: Reporting Rate 13%, Failure Rate 12%, Resilience Ratio 1.1
- Government: Reporting Rate 12%, Failure Rate 7%, Resilience Ratio 1.7
- Real Estate: Reporting Rate 9%, Failure Rate 10%,