# Arctic Wolf 2025 Cybersecurity Predictions Threat Report

## Table of Contents
- [Foreword](#foreword)
- [Key Takeaways](#key-takeaways)
- [Introduction](#introduction)
  - [Data sourcing and methodology](#data-sourcing-and-methodology)
- [Part 01: Ransomware & Data Extortion](#part-01-ransomware--data-extortion)
  - [Lower barriers to entry have led to a crowded landscape](#lower-barriers-to-entry-have-led-to-a-crowded-landscape)
  - [Ransomware actors continue to target organizations with no tolerance for downtime](#ransomware-actors-continue-to-target-organizations-with-no-tolerance-for-downtime)
  - [Ransoms: demands, negotiations, and potential payment](#ransoms-demands-negotiations-and-potential-payment)
  - [Unsecured RDP is the root cause of the largest portion of ransomware cases](#unsecured-rdp-is-the-root-cause-of-the-largest-portion-of-ransomware-cases)
  - [Spotlight: The usual suspects](#spotlight-the-usual-suspects)
- [Part 02: Business Email Compromise](#part-02-business-email-compromise)
  - [Financial services organizations are the prime targets](#financial-services-organizations-are-the-prime-targets)
  - [Social engineering (phishing in particular) drives BEC cases](#social-engineering-phishing-in-particular-drives-bec-cases)
- [Part 03: Intrusions](#part-03-intrusions)
  - [Intrusions, the first step towards greater threats](#intrusions-the-first-step-towards-greater-threats)
  - [Intruders disproportionately leverage a small number of vulnerabilities](#intruders-disproportionately-leverage-a-small-number-of-vulnerabilities)
  - [Vulnerabilities keep increasing](#vulnerabilities-keep-increasing)
  - [External exposure is the root cause of the vast majority of intrusions](#external-exposure-is-the-root-cause-of-the-vast-majority-of-intrusions)
- [Part 04: Managing & Mitigating Threats](#part-04-managing--mitigating-threats)
  - [Ensure you have broad visibility (monitoring) into your environment and assets, and create a baseline of normal behavior](#ensure-you-have-broad-visibility-monitoring-into-your-environment-and-assets-and-create-a-baseline-of-normal-behavior)
  - [Enforce strong identity controls](#enforce-strong-identity-controls)
  - [Establish and continually foster a culture of security](#establish-and-continually-foster-a-culture-of-security)
  - [Consider an IR retainer with an organization that staffs ransomware negotiators](#consider-an-ir-retainer-with-an-organization-that-staffs-ransomware-negotiators)
- [Conclusion](#conclusion)
- [How Arctic Wolf can help](#how-arctic-wolf-can-help)
- [About Arctic Wolf](#about-arctic-wolf)

---

A R C T I C   W O L F

THREAT REPORT

2025

## Foreword

This Arctic Wolf® Threat Report draws upon the first-hand experience of Arctic Wolf’s security experts, augmented by Arctic Wolf Labs research into the cybercrime ecosystem and additional credited sources.

By deliberately focusing on cyber attacks that escalated to a level of requiring an incident response (IR) investigation by Arctic Wolf, we aim to:

*   Highlight which attack types are responsible for severe incidents
*   Uncover the tactics, techniques, and procedures (TTPs) that allow threat actors to evade detection long enough to pursue actions on objective (e.g., deploying ransomware, tricking organizations into transferring funds, conducting intrusions, etc.)
*   Raise awareness of the cybersecurity practices needed to prevent, detect, and recover from such incidents

Very broadly, we see evidence that threat actors are adapting to target stronger cybersecurity postures by looking for novel methods of attack or embracing low-tech — but effective — means of bypassing high-tech safeguards. At the same time, competition within their own ranks and better resilience on the part of their victims has ransomware operators engaging in more aggressive tactics and taking a firmer stance on ransom payments. Business email compromise (BEC) continues to be a menace, especially for organizations that routinely transfer funds and use email to coordinate these activities. And although many intrusions we investigated appear to be failed ransomware attacks, others are more likely to be incidents of stealthy cyber espionage.

How do organizations protect themselves in the continuing cybersecurity arms race? By focusing on the fundamentals, including:

*   An adaptable security posture
*   Detection and response spanning the full attack surface
*   An IR process and partner that enables fast and effective recovery

Our hope is that reading this report will equip you with insights and actions to bolster all three of these elements.

K E R R I   S H A F E R - PA G E ,
Vice President, Incident Response

---

## Key Takeaways

### Three Cyber Incident Types Account for 95% of All IR Cases

Organizations typically reserve third-party IR engagements for only the most disruptive and damaging incidents, so it’s telling that our cases are dominated by ransomware (44% of cases), business email compromise (27%), and intrusions (24%). While their combined contribution is quite consistent year over year, an increase in the intrusion proportion is largely offset by a decrease in ransomware’s share. Detailed analysis hints that this is no mere coincidence, with signs that many ransomware attacks were stopped prior to detonation — indicating that organizations are improving their detection capabilities.

### 96% of Ransomware Cases Included Data Theft, as Threat Actors Adapt to Stronger Backup and Restoration Capabilities

As potential victims implemented more reliable backup and restoration processes, ransomware operators introduced data exfiltration as a means to apply additional pressure and protect their revenue streams. Today, this double extortion is undeniably the norm, as 96% of ransomware incidents we investigated included this element. Nevertheless, preparedness on the part of organizations remains important: our case analysis shows that in 68% of ransomware incidents, backups aided in the recovery process.

### The Ransomware Landscape is a Modern-Day Hydra

The well-established ransomware-as-a-service (RaaS) model has democratized access to ransomware software, intrusion tools, and — via initial access brokers — IT environments. One result is a very long tail of threat actors all vying for a piece of the cybercrime pie; as such, we observed more than 50 unique ransomware threat actors in victim environments. Like the Hydra of Greek mythology, when a ransomware operation ceases to exist — whether due to law-enforcement operations, infighting, politics, retirement, etc. — other groups (new and old) fill the void.

### Professional Incident Response (IR) Pays Off

In the not-too-distant past, most ransomware actors showed at least some willingness to negotiate with the victim to arrive at a workable solution. Nowadays, though, harassment and a stated refusal to negotiate are commonplace. Expert incident responders have encountered all these tactics before. Despite attackers’ persistent threats and aggressive tactics, our IR professionals were able to reduce aggregate ransom demands by 64%. Perhaps more importantly, our IR expertise was a major reason why 70% of our clients who used our negotiation services did not pay their ransoms. The Arctic Wolf Incident Response team includes a Threat Negotiation team and does not leverage the use of a partner or vendor to complete these activities.

### When It Comes to Business Email Compromise (BEC), Fraudsters Follow the Money

The finance and insurance industry accounted for 26.5% of BEC IR cases, roughly double the second-place industry (legal and government, at 13.3%). In fact, BEC accounted for 53% of IR cases pertaining to finance and insurance — the only industry for which BEC outnumbered ransomware. Clearly, organizations that regularly exchange money and process payment details over email are in the crosshairs of BEC attacks.

### Attackers Embrace Low-Tech Ways to Bypass High-Tech Defenses

Why kick down the door when you already have the key, or can find someone to open it on your behalf, or — best of all — you find it unlocked to begin with? Unsecured Remote Desktop Protocol (RDP) and compromised VPN credentials are the leading root causes of ransomware and intrusions, while phishing and previously compromised credentials are behind the vast majority of all BEC cases. Access controls and safeguards including strong, phishing-resistant multi-factor authentication (MFA) can not only help to stop attackers from gaining initial access, but are also effective means of thwarting intrusion actions, including reconnaissance.

### Prioritized Patching Can Prevent Intrusions

In 76% of intrusion cases, threat actors employed at least one of 10 specific vulnerabilities, none of which were zero-days and seven of which were associated with remote access tools or other externally facing services. Vulnerability management can seem like a never-ending game of high-stakes Whac-A-Mole — but a little prioritization can take away attackers’ favorite means of infiltration. To inform that prioritization, organizations must understand the complexities of their network, the need to patch critical infrastructure (especially VPN services, firewalls, and other edge devices) based on CVE severity (if known), and the answers to the questions, “Where is our data?” and “Where is our customers’ data?”

### Threat Actors Save Their Zero-Day Exploits for Stealthy Intrusions

While zero-day exploits almost never appeared in ransomware (0.4% of cases) or BEC (0%) incidents, they represented the fifth-leading root cause in intrusions — accounting for 6% of such cases. This stark contrast suggests threat actors are selective, reserving such actions for the most sensitive and targeted activities with the highest probability of success.

---

## Introduction

The insights and data presented are drawn from hundreds of global digital forensics and incident response (DFIR) engagements conducted by the Arctic Wolf Incident Response team from October 1, 2023, through September 30, 2024.

The IR case data is augmented with telemetry from the Arctic Wolf Aurora Platform and research from our threat intelligence team, digital forensics experts, incident responders, and professional ransomware negotiators.

The top three incident types collectively accounted for 95% of all IR cases.

Accordingly, we will examine these three types in detail to provide an overview of the threat, and:

*   Reveal which industries are most impacted
*   Understand root causes
*   Dive into related topics

### Data sourcing and methodology

To enable the holistic analysis within this report, all data is aggregated without any identifying characteristics or attributes.

The vast majority of these IR engagements were initiated as part of cyber insurance policies, through our partnerships with insurance providers and privacy law practitioners. Consequently, these incidents typify cyber attacks that were so severe (i.e., damaging, disruptive) that they led to insurance claims — making them ideal study subjects in our aim to better understand the most dangerous threats.

However, many cyber incidents include multiple elements, as threat actors rarely execute a single action. For instance, an attacker may employ social engineering to obtain credentials which are then used to access the environment via a VPN service, followed by lateral movement and reconnaissance, all as precursors to exfiltrating data and ultimately deploying a malicious payload to encrypt files. If this attack progressed through all those steps, we would classify the incident as a ransomware/data extortion case; however, if the lateral movement was detected and contained, it would be classified as an intrusion.

While cyber insurance is a valuable risk transfer option for any organization, it’s important to recognize that certain industries are more likely to have coverage than others, and that our sample cases will reflect this distribution. Rephrased, the sample represents our real-world experience delivering incident response services and is not intended to represent all cyber attacks across all markets and segments.

### Case classification

We classify cases by the focal point of the incident, or the best answer to the question, “What is the most impactful aspect of the attack?”

*   **Ransomware / Data Extortion**: 44%
*   **Business Email Compromise (BEC)**: 27%
*   **Intrusions**: 24%
*   **Other (e.g., Insider Threat, DDoS)**: 1%
*   **Malware Infections**: 2%
*   **Data Incidents**: 2%

---

# PART 01: RANSOMWARE & DATA EXTORTION

### Highlights

*   **RANSOMWARE REMAINS THE BIGGEST DRIVER OF IR CASES**: 44% of IR cases during the reporting period pertained to ransomware, indicating just how prevalent such incidents are to victimized organizations.
*   **AS BACKUP AND RESTORATION CAPABILITIES IMPROVE, DOUBLE EXTORTION IS NOW THE NORM**: In 96% of ransomware IR cases, the attacker also exfiltrated data to apply pressure and extort payment.
*   **EXPERT NEGOTIATION IS WORTHWHILE**: Although every case is unique to some degree, Arctic Wolf’s experienced ransomware negotiators were able to secure a 64% reduction in aggregate ransom demands.
*   **MANY VICTIMS PAY UNNECESSARILY**: While prior surveys suggest that upwards of 80% of victims ultimately chose to pay a ransom, our data shows only 30% of Arctic Wolf IR cases resulted in a ransom payment — and in the majority of those incidents, the victim paid to expedite recovery, rather than out of necessity.
*   **ATTACKERS ARE LETTING THEMSELVES IN**: Unsecured Remote Desktop Protocol (RDP) and compromised virtual private network (VPN) credentials are the leading root causes of ransomware IR cases — with RDP alone being the culprit in 38% of such incidents.

For the 12-month period covered by this report, Ransomware / Data Extortion cases accounted for 44% of our IR incidents.

This proportion represents a slight decline from last year’s report (48.6%)¹, but nevertheless underscores ransomware’s dominance as an attack-of-choice for many threat actors.

Unfortunately, all signs indicate that ransomware and data extortion will remain everyday threats for the foreseeable future. In particular, the risk versus reward calculation provides strong incentives for attackers to go this route. Consider that:

*   Despite some high-profile law enforcement takedowns, the chances of perpetrators facing legal consequences remains low (especially when they enjoy the protection of their governments or security agencies)
*   Ransom payments, on average, remain high (more on this, in a moment)
*   There’s always the possibility of a massive payout — for context, 2024 saw the largest ransom payment on record ($75 million USD from a Fortune 50 company, paid to the Dark Angels group)

¹As we’ll see later, there’s evidence this decline is the result of effective defenses stopping attacks at the intrusion stage (i.e., before ransomware deployment)

### Lower barriers to entry have led to a crowded landscape

During this reporting period, we observed more than 50 unique threat actor groups operating in victim environments.

This expansive collection is what happens when financial incentives intersect with the democratization of ransomware, the latter of which is the result of the evolving cybercrime ecosystem.

In the early history of ransomware, threat groups managed the entire attack lifecycle in-house. This meant they needed the skills to develop ransomware software, identify potential victims, successfully infiltrate targets, perform intrusion actions leading to ransomware deployment and detonation, and negotiate payment.

Today, ransomware-as-a-service (RaaS) is a well-established model in which:

*   Ransomware developers (individuals and organizations) write their own software, then lease it to other individuals and groups (usually as a percentage of the ransoms paid)
*   Initial access brokers (IABs), who specialize in gaining access and establishing persistence, sell access into IT environments around the globe
*   Individuals and criminal organizations, operating as affiliates to the ransomware groups, conduct the actual attacks and negotiations

Now, any aspiring cybercriminal can simply purchase access into an organization from an IAB and then deploy the ransomware. As part of their affiliate relationship with the ransomware authors, the actual attacker may receive general guidance (or even strict rules) about how to conduct the negotiations; they will also be able to leverage the author’s reputation, as needed.

Plus, the individuals or groups launching attacks are rarely tied to a single variety of ransomware. Exclusivity agreements are rare (and difficult to enforce), so attackers can pick and choose whichever strain they prefer — whether for some technical reason, or perhaps because they stand to earn a bigger cut of the payday.

Although it’s certainly possible to have file encryption or data extortion, rather than both, 96% of the ransomware cases to which we responded included both elements.

The first known “double extortion” incident occurred in 2019, when the Maze ransomware operation attacked security staffing firm Allied Universal. In addition to encrypting files, Maze exfiltrated sensitive data and threatened to publish it unless Allied Universal paid the ransom.

The model quickly caught on and is now the norm due to the pressure it exerts — including against victims with reliable backup and recovery processes.

Notably, threat actors continue to add new extortion layers, including contacting business partners of victims and family members of executives — anything to compel a quick and large payment.

Learn more in our blog, The Dangers of Double and Triple Extortion in Ransomware

### Ransomware actors continue to target organizations with no tolerance for downtime

To extract a payment, ransomware operators apply pressure, typically by taking operations offline or threatening to release sensitive data.

And when we look at the data, we see that five industries that are highly susceptible to both these tactics account for just over two-thirds of ransomware IR cases.

**Ransomware & Data Extortion IR Cases by Industry**

*   Manufacturing: 18.6%
*   Healthcare: 13.1%
*   Construction: 12.0%
*   Legal & Government: 11.7%
*   Education & Nonprofit: 11.7%
*   Retail: 7.7%
*   Business Services: 6.2%
*   Finance & Insurance: 5.8%
*   Energy & Natural Resources: 5.5%
*   Technology: 3.3%
*   Shipping & Logistics: 2.9%
*   Other: 1.5%

Manufacturers are historically a favored target of threat actors, as any operational disruption threatens to derail production, risk contractual penalties, create backlogs, and damage the manufacturer’s reputation. Plus, manufacturers often hold valuable information about industrial processes and customers, making them similarly susceptible to the data extortion aspect of modern ransomware.

Given this context, it’s unsurprising to see the manufacturing industry accounts for the largest share of ransomware IR cases, at 18.6%.

Healthcare has the second-largest share, at 13.1%, followed by construction with 12%. The top five are rounded out by legal and government, and education and nonprofit, each at 11.7%.

Like in manufacturing, service or production outages for organizations in any of these industries become immediately evident and have significant consequences; similarly, many such organizations will also be sitting on troves of sensitive and proprietary data.

### Ransoms: demands, negotiations, and potential payment

From an outside perspective, ransomware incidents can seem like fairly simple transactions: an attacker severely disrupts an organization and threatens to release data, the attacker states a ransom amount, the organization pays to expedite recovery or refuses to pay.

Behind the scenes, though, things are considerably more complicated.

**The Median Aggregate Ransom Demand Remains at $600,000 (USD)**

It’s generally understood that cybercriminals base their initial ransom demand on a multitude of factors, including:

*   The victim organization’s size and financial position, which threat actors use to estimate the organization’s ability to pay
*   The victim organization’s industry, which influences their sensitivity to disruption and negative press, and which could provide relevant history on frequency of payouts
*   The scope of the attack, which typically influences the victim’s ability to recover and the impact to their operations
*   The victim’s insurance coverage, as some ransomware groups actively seek out cyber insurance policies in a victim’s environment to better inform their ransom demands
*   The ego, mood, and reputation of the attacker

Perhaps the ‘ransomware industry’ as a whole is reaching something of a steady state, now that victims are better prepared to recover, and now that the cyber insurance market is maturing.

With so many variables at play, there can be considerable variation from year-over-year within each industry. Indeed, comparing the figure below to the one in last year’s report reveals only a few strong consistencies:

*   Retail and the energy and natural resources sector once again faced the highest median ransom demands
*   Healthcare continued to receive the second lowest ransom demands
*   Manufacturing and technology were again in the bottom half

The remainder of the list is heavily reordered, compared to last year’s report, with the most notable changes being:

*   Construction, which was third-lowest last year, has jumped to third highest
*   Finance and insurance, which was fourth-highest last year, has dropped to last

Although it’s tempting to posit explanations for both the consistencies and changes, probably the wisest approach is simply to observe that there is tremendous variation across and within industries, and that specific ransom amounts remain largely unpredictable.

In the aggregate (i.e., across all industries), the myriad of variables largely control for themselves, leading to less fluctuation and stronger predictive value. In fact, despite all the shuffling, the aggregate median initial ransom demand is unchanged: $600,000 (USD).

**Median Initial Ransom Demand by Industry (USD)**

*   Retail: $800K
*   Energy & Natural Resources: $775K
*   Construction: $775K
*   Business Services: $699K
*   All Industries: $600K
*   Shipping & Logistics: $600K
*   Legal & Government: $600K
*   Education & Nonprofit: $600K
*   Manufacturing: $550K
*   Other: $488K
*   Healthcare: $450K
*   Technology: $400K
*   Finance & Insurance: $325K

### Expert negotiation pays off

Many victims— especially those who choose to respond to an attack on their own without professional support — may not be aware that the ransom demand can be negotiated down.

It’s worth bearing in mind that the worst outcome for the attacker is that they don’t get paid. A ransom demand that’s too high or an outright refusal to negotiate can both increase the odds of this result, so ransomware actors have strong motivations to come to the negotiating table, so to speak.

Although negotiating with criminals is at best unsavory, the harsh business reality is that doing so can pay off in a significant way. Individual cases vary, of course, but our IR case data reveals that, in aggregate – Arctic Wolf ransomware negotiators were able to reduce the ransom demand by 64%.

But negotiating with a ransomware actor is best left to the experts, who generally have much, much more experience with doing so than any in-house personnel. A professional ransomware negotiator will work on the victim’s behalf to communicate with the threat actor, to better understand the situation, and to try to reduce the amount demanded.

Plus, we’ve observed that attackers are becoming more aggressive with their extortion tactics and adopting tougher stances. In the not-too-distant past, most ransomware actors showed at least some willingness to negotiate with the victim to arrive at a workable solution². Nowadays, though, harassment has become much more common, and some attackers even reach out to the victim organization’s business partners and the families of the victim organization’s executives — all while refusing to reduce their demands.

²Note: We’re not at all giving them credit for this behavior — our intention is merely to contrast this slightly less deplorable behavior with the more aggressive behavior of the recent past.

Expert incident responders have encountered all these tactics before.

Still, there’s a bigger question: whether or not a threat actor reduces their demand, do victimized organizations even need to pay the ransom?

### Ransom payments are often a business decision rather than a recovery necessity

At Arctic Wolf, our position aligns with the general recommendations of the FBI, other law enforcement agencies, and governments: If possible, ransom demands should not be paid, as starving the perpetrators is the only way we can collectively hope to eliminate these attacks.

Nevertheless, the decision on whether to pay is one that must be made by stakeholders within the victim organization once presented with all possible information and options.

As context, Arctic Wolf’s The State of Cybersecurity: 2024 Trends Report revealed that, within that report’s 12-month research window, 83% of ransomware victims paid a ransom³. In contrast, in the ransomware IR cases used in the report you’re reading now, only 30% of victims elected to pay — meaning 70% chose not to, nearly the inverse of the survey-sourced number.

What’s behind this stark difference?

Lacking visibility into the incidents reflected in the survey, we can’t say for sure. However, we believe it’s fair to say that an organization acting on their own almost certainly lacks the experience to understand all the options available and may succumb to pressure from the perpetrators to act quickly — but calling in a professional IR team can unlock more options.

Employing the services of a professional IR organization can have many benefits, including:

*   Preventing further problems: In some circumstances, the threat actor demanding a payment could be a sanctioned entity or have ties to a terrorist organization. In these cases, any payment to such a group constitutes a crime on behalf of the payee.
*   Insight into the situation and explanation of what options are available: This can include if a payment is even necessary (sometimes decryption keys are already known) and the reputation of the threat actor. Professional negotiators can sometimes get information from the threat actors (e.g., what data was stolen) that can lead to better-informed decisions.
*   Smaller payments: While every ransomware affiliate and group is different, professionals know who is more likely to lower their demands, and by how much.

³That is, 83% of organizations hit by ransomware paid either some or all of the initial ransom demand. Note, however, that this figure comes from a survey of 1,000 IT and security decision makers and was not limited to incidents that pulled in IR professionals or, more specifically, Arctic Wolf’s IR professionals. Nevertheless, it indicates that the large majority of ransomware victims pay, overall.

Detailed examination of our IR case data suggests that paying a ransom was the victim’s only viable recovery option in a mere 12% of cases — meaning that some organizations chose to pay when they didn’t (strictly speaking) have to.

The main motivations for doing so were to:

*   Prevent publication of stolen data
*   Speed up the recovery process

Let’s first confront the reality that the majority of ransomware attacks include data theft. In theory, paying up is the only way to prevent publication and, supposedly, to ensure deletion (although, per the callout below, “buyer beware” applies). However, an IR team may provide compelling evidence that paying the ransom, while perhaps preventing publication, won’t guarantee deletion. This fact alone might cause an organization to reconsider. Or maybe the IR team helps the organization better understand the regulatory ramifications or can uncover information suggesting the exfiltrated data isn’t as sensitive or damaging as first feared. Maybe the presence of the IR team simply buys time, and — no longer feeling rushed to act — the organization reconsiders and ultimately decides not to pay. This list is not intended to be exhaustive, but rather to highlight some possibilities.

The second major aspect is recovery-centric ransoms — that is, paying to receive a decryption key. In this case, the IR team might know of a flaw in the encryption algorithm that renders decryption without a key possible. Or maybe the decryption keys are already known from prior incidents or law enforcement actions. In working with the IR team, perhaps the victim organization finds that their backup and recovery processes are sufficient to negate most of the harm, changing the math that determines the ‘value’ of making the payment. So, while every situation is different, aggregate case analysis indicates that bringing in a professional IR team is worthwhile.

### “Can we trust a ransomware group to be true to their word?”

This is one of the most common questions ransomware victims ask our IR professionals when considering whether or not to pay the ransom/extortion demand.

Our best, most-informed answer is roughly, “Generally, yes, but…”

“Generally, yes...”
Most ransomware groups and affiliates model themselves after legitimate businesses; accordingly, they recognize that their success depends in large part upon their reputation. If a threat actor’s actions lead to a reputation of not delivering on their promises — by failing to deliver a decryption key or releasing data after a ransom is paid — then that undermines the entire extortion business model.

“But…”
However, although these groups may model themselves as businesses, never forget that they are criminals. We have handled multiple cases in which our analysts, or agencies with whom we have collaborated, have offensively “hacked back” against the threat actor and discovered data that victims had been assured was deleted — violating the terms of the ransom agreement. While the threat actor may not have released this data, they still kept it. What’s to prevent them from coming back later and demanding additional payment if they find themselves in a situation where they need more money? Plus, if the ransomware actor enjoys the patronage or protection of a government intelligence agency, it’s reasonable to presume that exfiltrated information is immediately passed ‘up the chain.’

In general, payment may be regarded as a path to faster recovery and a means to prevent publication of data but should not be considered as a guarantee that information won’t be distributed privately or even that these criminals will stay true to their word.

### Unsecured RDP is the root cause of the largest portion of ransomware cases

External exposure is the root cause of 93% of our ransomware and data extortion IR cases, with two varieties — external remote access (59.4%) and external exploits (33.2%) — accounting for practically all such incidents.

**Root Causes of Ransomware & Data Extortion IR Cases**

*   External Remote Access (e.g., RDP, VPN, RMM, etc.): 59.4%
*   External Exploit: 33.2%
*   Zero-Day Exploit: 0.4%
*   Malicious Software Download: 4.4%
*   Previously Compromised Account / Credentials: 0.9%
*   Social Engineering (e.g., Tech Support Scam, Account Creation, etc.): 0.9%
*   Phishing: 0.4%
*   Third Party and Supply Chain: 0.4%

**Categories**

*   External Exposure: 93.0%
*   Human Risk: 6.6%
*   Trusted Relationship: 0.4%

Digging deeper, attackers leveraged unsecured Remote Desktop Protocol (RDP) and compromised virtual private network (VPN) credentials as their primary methods, with RDP alone being the culprit in 38% of cases.

To put this in perspective, it means attackers abused the very tools organizations have implemented to enable and secure their remote offices and workforces — often by simply logging in to unprotected services.

With many organizations having offices distributed geographically, and with remote — and hybrid- work models here to stay, remote access tools — including RDP, VPN, and remote monitoring and management (RMM) utilities — are workhorses of modern IT infrastructure. And, unlike many other elements within the tech stack, these tools generally have to be externally accessible.

Unfortunately, absent an added layer of protection such as strong, phishing-resistant multi-factor authentication (MFA), these services also provide a convenient way for threat actors to largely bypass an organization’s defenses. All an attacker needs to do so is obtain a set of active credentials, which can be sourced via phishing, purchased within a cybercrime marketplace, or ‘discovered’ via an identity-based attack like credential stuffing or password spraying. The use of a valid account makes it more difficult for organizations to detect the activity as being malicious, which gives an attacker time to pursue their objectives.

During this report period, we observed malicious usage of 32 different RMM tools. There’s also a distinct upward trend, with RMM tools being used in 36% of IR cases within the last quarter.

What if a target doesn’t have an RMM tool already in place? We observed several instances where the threat actor would send a phishing email with an unauthorized charge/purchase pretext. The recipients would be directed to a phishing site, the goal of which is to have them download and install ConnectWise ScreenConnect. In some cases, the victim would even call a support phone number (provided by the attacker) and actually be guided through the download and installation process. The Black Basta ransomware group is known to employ a similar approach. After following up an email bombing attack by impersonating IT personnel, the group would use Windows Quick Assist to obtain initial access and then turn to a combination of RMM tools to maintain persistence.

Unfortunately, as explained in the Arctic Wolf Labs 2025 Predictions Report, we expect threat actors to continue to target perimeter defenses using these same tactics.

To help withstand perimeter-focused attacks, organizations should scan their environments for unsecured RDP and should pay particular attention to credential management (in addition to implementing and enforcing phishing-resistant MFA).

### Backing up to bounce back

One of the most effective ways an organization can increase resilience against ransomware attacks is to maintain proper backup practices. While backups don’t address the issues around data exfiltration, being able to restore business operations can buy your organization time and limit the ripple effects of the attack. Our case analysis shows that in 68% of ransomware incidents, reliable backups aided in the recovery process — in many cases removing the need for a payout by providing an alternate path to sufficient recovery.

Following the 3-2-1 principle of backup: The 3-2-1 principle says that an organization should have:

*   3 copies of data (1 primary and 2 backup)
*   2 different types of media
*   1 off-site copy (ideally in a secure private cloud)

Regular recovery testing: A real-world incident is not the time to uncover problems with processes, prioritization, or the backups themselves — be sure to regularly (and perhaps randomly) test your ability to recover.

Understanding and accounting for the shared responsibility model of cloud services: The cloud/SaaS provider and the SaaS customer (i.e., you) each assume ownership of particular responsibilities with respect to data security. Be sure to understand the terms of each of your contracts, but in general:

*   The SaaS provider is only responsible for the underlying application, operating system, virtualization, hardware, and network — including hardware failures, software failures, natural disasters, power outages, and physical intrusion into the data centers
*   The customer is responsible for users, data, administration, human errors, programmatic errors, malicious insiders, ransomware attacks, and other malware — in other words, a security incident originating from within your organization that destroys or disrupts your cloud data is your responsibility

Looking beyond ransomware, restoring from reliable backups was also the number one recovery method for intrusions. When an attacker has gained unauthorized access to an environment, there’s a high likelihood that they have established multiple persistence mechanisms that would allow them to regain access should they be expelled. Therefore, it’s often recommended to restore every system accessed by the attacker and start over, rather than assuming all persistence mechanisms were found and removed — as even a single missed backdoor can prove disastrous.

Outlined below and in the right column of this page are some backup best practices that might make a meaningful difference on a dark day.

### Spotlight: The usual suspects

We observed 50 unique ransomware threat actors in victim environments. The ransomware-as-a-service reality makes positive attribution of an incident considerably more difficult than in years past.

However, such attributions can be informed by a combination of:

*   Malware samples
*   Infrastructure overlap or reuse
*   Post-encryption file extensions
*   Ransom messages and leak site postings
*   Negotiation script patterns

As such, our team of researchers have identified the five major ransomware groups that were behind 42% of the cases we investigated in the last 12 months.

---

#### THREAT ACTOR: AKIRA

**DARK WEB DATA:**

*   **AW IR DATA | 10.23–10.24:**
    *   Percentage of Our Cases: 15%
    *   Median Starting Demand: $325,000 USD
    *   File Ext. of Encrypted Files: .akira or .powerranges (Megazord variant) or .arika when their ransomware misfires / file corruption on hosts
*   **First Observed:** March 2023
*   **Potential Lineage:** Ryuk > Conti --> Akira
*   **NUMBER OF VICTIMS:** 215 (Listed on their leak site*)
*   **NUMBER OF POSTS:** 19 (Average postings each month on their data leak site**)
*   **TOP 3 INDUSTRIES***: 01. Manufacturing ~23%, 02. Construction ~11%, 03. Technology ~7%
*   **TOP 5 COUNTRIES***: 01. United States ~51%, 02. Canada ~7%, 03. United Kingdom ~5%, 04. Brazil ~4%,