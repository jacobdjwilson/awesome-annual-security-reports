# Ransomware-Defense-Report 2023

## Table of Contents
- [Introduction](#introduction)
- [Why We Do This Survey](#why-we-do-this-survey)
- [Key Findings](#key-findings)
- [The Shifting Ransomware Trends](#the-shifting-ransomware-trends)
- [On the Positive Side, We Saw Fewer Organizations Affected...](#on-the-positive-side-we-saw-fewer-organizations-affected)
- [...But the Impact Remains Immense for Entire Organizations](#but-the-impact-remains-immense-for-entire-organizations)
- [The Cost Is Climbing, Too](#the-cost-is-climbing-too)
- [A False Sense of Confidence](#a-false-sense-of-confidence)
- [Ransomware Is More than a SecOps Problem](#ransomware-is-more-than-a-secops-problem)
- [Where SecOps and BizOps Collide](#where-secops-and-bizops-collide)
- [Battling Ransomware on Multiple Fronts](#battling-ransomware-on-multiple-fronts)
- [Countermeasures Misaligned with New Ransomware Tactics](#countermeasures-misaligned-with-new-ransomware-tactics)
- [Future Defense Priorities Show Some Disconnect](#future-defense-priorities-show-some-disconnect)
- [All Eyes on Prevention and Automation](#all-eyes-on-prevention-and-automation)
- [Adapting Ransomware Defenses for Stealthier Attacks](#adapting-ransomware-defenses-for-stealthier-attacks)
- [Final Thoughts](#final-thoughts)
- [About SpyCloud](#about-spycloud)

---

## Introduction

For the last several years, we’ve watched our workplaces digitally transform, making the convenience of working and collaborating from anywhere the rule rather than an exception. Many organizations have welcomed this new reality, but they’ve struggled to keep their security defenses in step with the fast pace of digital growth and an expanding attack surface.

Cybercriminals, however, haven’t had any problem staying current with a digital-first, cloud-first environment. As they quickly pivot to next-generation tactics for exfiltrating data and access, security operations (SecOps) teams are falling farther behind – while exposure to cyberattacks like ransomware is at an all-time high.

### Some Background Before You Dig In

After the release of our last Ransomware Defense Report in September 2022, ransomware attacks showed some promising signs of slowing down. Criminals tested other tactics and government agencies cracked down, with the number of attacks leveling off by the end of year. But that glimmer of hope fizzled quickly, with attackers picking up the pace so fast in 2023 that we’re headed toward the second-most costly year for ransomware in history.

Even through that ebb-and-flow, the sophistication and impact of ransomware attacks has grown. At least one new ransomware group with double-extortion abilities surfaced every month last year, while the average cost of a ransomware attack escalated to $5.13 million – surpassing the average cost of a data breach.

And one thing hasn’t changed: ransomware is one of the toughest cybersecurity challenges organizations of all sizes and industries continue to face. In SpyCloud’s 2023 Malware and Readiness Defense Report, security leaders and practitioners ranked ransomware as the top threat to their organization’s security.

## Why We Do This Survey

As we note in our findings, ransomware defenses are not keeping pace with cybercriminals. We do this survey to shine a light on one of the contributing causes: an emerging threat that could be an early warning sign of a ransomware event – information-stealing malware, or infostealers.

Criminals are using infostealers to siphon authentication data – including logs with information that enable access to enterprise networks and applications – and selling the data to ransomware operators. And through a deep analysis of recaptured infostealer logs, we’ve uncovered that the presence of infostealer malware is related to the likelihood that a company will experience a ransomware event in the near future.

### The Infostealer-Ransomware Connection, Broken Down

SpyCloud researchers conducted a detailed analysis using ransomware event data from ecrime.ch and our own database of recaptured records from the criminal underground. Of 2,613 North American and European companies victimized by ransomware in 2023, 30% had at least one infostealer infection prior to being attacked.

Our analysis also showed that the presence of specific infostealer infections – Raccoon, Vidar, and Redline – increases the probability that a company will experience a ransomware event.

![Chart showing the most prevalent infostealer families associated with ransomware victim companies: Raccoon (76%), Vidar (8%), Redline (8%), Metastealer (2%), LummaC2 (2%), Rhadamanthys (2%), Stealc (1%), Aurora (1%)]

Many organizations fail to fully remediate infostealer and other malware infections, focusing primarily on protecting the infected device and skipping critical remediation of exposed credentials and active session data, leaving them exposed to follow-on attacks. In addition to presenting survey results in this report, we offer insights about how comprehensive Post-Infection Remediation can help prevent ransomware attacks – and ultimately enable security teams to get ahead of attackers.

## Key Findings

1. **Despite some positive developments, the impact of ransomware attacks remains high.**
   The good news? We found a drop in the number of organizations affected by ransomware and in the number paying ransom compared to the previous year. This likely reflects the temporary slowdown of ransomware activity in the later part of 2022 before things ramped up again in the first half of 2023. Overall, however, impact from ransomware remains high, with 81% of surveyed organizations affected at least once in the past 12 months, and 48% of those that were impacted paying a ransom.

2. **Security teams are changing how they defend their riskiest entry points – but will need to keep pivoting to combat new attack vectors.**
   Survey participants ranked phishing and social engineering as the riskiest entry points for ransomware attacks again this year. With human behavior an ongoing issue, security teams are changing their approach – shifting from user awareness and training to technology-driven countermeasures to mitigate the inevitable human-driven risks.

3. **Infostealer malware is a precursor for a ransomware event, but teams aren't worried about it – and they aren’t prioritizing malware remediation.**
   Organizations are optimistic about their ransomware prevention capabilities, with 79% of surveyed security professionals expressing general confidence in their ability to prevent a full-blown ransomware incident. But their optimism may be misplaced, since only 19% of organizations are prioritizing improved visibility and remediation of exposed credentials and malware-exfiltrated data.

## The Shifting Ransomware Trends

As we noted, ransomware took a roller-coaster ride in the past 12 months. SpyCloud’s survey reflects these shifting trends. Although some of our indicators moved in a positive direction, upon digging in, we found a bleaker picture than appears on the surface.

### On the Positive Side, We Saw Fewer Organizations Affected...

First, the positive news. We found a slight decline in the number of organizations affected at least once by ransomware in the past 12 months: 81% in this year’s survey vs. 90% last year.

![Chart showing the past frequency of ransomware incidents year-over-year]

Contributing to some good news for organizations on the financial front is a decline in the number of organizations paying a ransom (48% in the past 12 months compared to 65% the previous year) and a slight uptick in the number of those that recovered data at least partially if not fully.

### ...But the Impact Remains Immense for Entire Organizations

Despite some positive trends, ransomware remains a huge problem for organizations of any size. While the prevailing assumption is that larger organizations are in a better position to defend themselves given budgets and resources, our data shows that large enterprises with 10,000 or more employees were affected just as much as mid-sized organizations.

![Chart showing percentage of organizations affected by ransomware at least once by organization size]

### The Cost Is Climbing, Too

Last year, security researchers found an increase in average ransom demands across many sectors. Even when victims choose not to pay, they still see financial losses that go far beyond the ransom. Fewer than 12% of our surveyed organizations that were hit described their costs as negligible. For 39%, the price tag was over $1 million.

## A False Sense of Confidence

The positive developments we noted perhaps explain why 79% of surveyed security professionals feel fairly or highly confident about their capabilities to prevent a full-blown ransomware attack in the next 12 months.

![Chart showing confidence levels about preventing a ransomware attack]

Measuring confidence based on the past or the current state breeds complacency – which is especially dangerous since attackers are constantly innovating. Security practitioners understand this better than security leaders: executives expressed much higher general confidence than practitioners in preventing an attack.

## Ransomware Is More than a SecOps Problem

Although some organizations may not see big, immediate financial impact from ransomware attacks, they recognize that the exposure due to data loss creates just as much risk, if not more. Participants ranked exposure of proprietary and sensitive data as the greatest potential impact of ransomware, followed by disruption to business operations and disruption to IT and SecOps.

## Where SecOps and BizOps Collide

As we’ve discussed, ransomware is not just a SecOps problem. It affects business operations by hoarding resources across the organization, often involving a minimum of seven internal departments. IBM’s annual Cost of a Data Breach Report shows a painful price tag for an organization due to a ransomware attack: $5.13 million on average, not including the ransom itself.

## Battling Ransomware on Multiple Fronts

Phishing and social engineering, along with unpatched vulnerabilities, once again ranked as the riskiest entry points for ransomware.

![Chart showing perceived risk of entry points for ransomware]

We were surprised, however, to see stolen cookies/tokens rated as the least risky entry point, suggesting that understanding of this new threat is just beginning. This entry point is an especially high risk in passwordless environments, which many view as the future of authentication.

## Countermeasures Misaligned with New Ransomware Tactics

Year over year, data backup has remained the most important countermeasure for organizations. We highlight this as concerning because it shows that defenses are not adjusting to the shift in ransomware tactics. Backup was effective years ago when data encryption was the biggest problem, but it doesn’t mitigate the risks of modern ransomware – which relies heavily on malware-exfiltrated authentication data.

## Future Defense Priorities Show Some Disconnect

Lack of visibility, the inefficiency of manual tasks, and cumbersome or false alerts are recognized problems in cybersecurity. Survey participants overwhelmingly agree that better visibility of malware-exfiltrated data, along with automated remediation workflows, would improve their ability to combat ransomware and improve overall security posture.

## All Eyes on Prevention and Automation

Proactive prevention is just as important as strengthening defenses and response capabilities, and our respondents agreed when asked to pick their top three defense priorities. Improving ransomware prevention capabilities is the top priority for organizations in the next 12 months, followed by improving ransomware detection capabilities and automating security processes and workflows.

## Adapting Ransomware Defenses for Stealthier Attacks

We found that ransomware prevention is consistently at the top of the priority list for organizations. Ransomware is a malware problem at its core, which means that preventing ransomware attacks must start with proper and robust malware remediation.

### Malware Response Must Include Post-Infection Remediation

Today’s attack surface includes users and applications, not just devices. And Post-Infection Remediation is a paradigm shift from the current machine-centric response to a more comprehensive identity-centric response. While traditional machine-centric remediation simply clears a device, Post-Infection Remediation takes additional measures to reset stolen credentials and invalidate active web sessions of exposed applications.

## Final Thoughts

Our biggest takeaway from this year’s survey is that SecOps teams have not yet embraced a key piece of the ransomware defense puzzle – remediating malware-exfiltrated authentication data – which means that many organizations may be more vulnerable than they realize. With an infostealer infection as a precursor to nearly one-third of ransomware events in 2023, teams can no longer ignore this rising threat.

## About SpyCloud

SpyCloud transforms recaptured darknet data to protect businesses from cyberattacks. Its products operationalize Cybercrime Analytics (C2A) to produce actionable insights that allow enterprises to proactively prevent ransomware and account takeover, protect their business from consumer fraud losses, and investigate cybercrime incidents. Headquartered in Austin, TX, SpyCloud is home to nearly 200 cybersecurity experts whose mission is to make the internet a safer place.

To learn more and see insights on your company’s exposed data, visit [spycloud.com](http://spycloud.com).