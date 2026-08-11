# Report Title: Cyber-Espionage-Report
Organization: Verizon
Year: 2020

## Table of Contents
- [01 | Compass points and decoder keys](#01--compass-points-and-decoder-keys)
- [02 | State of Cyber-Espionage](#02--state-of-cyber-espionage)
- [03 | Targeted victims](#03--targeted-victims)
- [04 | Essential Elements of Friendly Information](#04--essential-elements-of-friendly-information)
- [05 | Threat actors](#05--threat-actors)

## 01 | Compass points and decoder keys

Welcome to the Cyber-Espionage Report (CER), our first-ever data-driven publication on advanced cyberattacks. The CER is one of the most comprehensive overviews of the Cyber-Espionage landscape, offering a deep dive into attackers, their motives, their methods and the victims who they target. The report serves as a tool for better understanding these threat actors and what organizations can do to hunt, detect and respond to Cyber-Espionage attacks.

This data-driven report draws from seven years of Data Breach Investigations Report (DBIR) content as well as more than 14 years of Verizon Threat Research Advisory Center (VTRAC) Cyber-Espionage data breach response expertise. The CER serves as a guide for cybersecurity professionals looking to bolster their organization’s cyberdefense posture and incident response (IR) capabilities against Cyber-Espionage attacks.

More specifically, the CER is an elaboration of the “Cyber-Espionage” Incident Classification Pattern as reflected in the 2020 DBIR. And as with the DBIR, we use the same naming conventions, terms and definitions. Content in this section and in “Appendix A: Frameworks” will help serve as your compass points and decoder keys for the rest of the report. Download a copy of the CER at [verizon.com/business/resources/reports/cyber-espionage-report/](verizon.com/business/resources/reports/cyber-espionage-report/)

### Using this report

Throughout the CER, we present and compare findings from a seven-year perspective (content from the 2014 DBIR through the 2020 DBIR): Cyber-Espionage breaches vs. all breaches. At times, we also address findings from a one-year (2020 DBIR) perspective: Cyber-Espionage breaches vs. all breaches. All references to years in this report are in DBIR years. For example, “2020 DBIR timeframe” refers to DBIR year 2020, which in turn correlates with the DBIR dataset timeframe of October 2018 to October 2019.

### Data Breach Investigations Report

The 2020 DBIR is our 13th edition, covering global cybercrime trends. The DBIR combines real data from scores of sources and provides actionable insight into tackling cybercrime. Download the 2020 DBIR here: [enterprise.verizon.com/resources/reports/dbir/](enterprise.verizon.com/resources/reports/dbir/)

### VERIS framework

The Vocabulary for Event Recording and Incident Sharing (VERIS) framework is a set of metrics designed to provide a common language for describing security incidents in a structured and repeatable manner. See “Appendix A: Frameworks” for more information and read more about VERIS at the link below:

[veriscommunity.net/](veriscommunity.net/)

### Incident Classification Patterns

Way back in 2014, to help us better understand and communicate the DBIR dataset, we grouped “like” incidents together and called them “Incident Classification Patterns.” Nine patterns comprised the majority of data breaches back then and still do so today. These patterns are Crimeware, Cyber-Espionage, Denial of Service, Lost and Stolen Assets, Miscellaneous Errors, Payment Card Skimmers, Point of Sale, Privilege Misuse, Web Applications and the catchall Everything Else. For definitions and summaries, see pages 36 to 37 of the 2020 DBIR.

### Cyber-Espionage pattern

The DBIR Cyber-Espionage pattern consists of espionage enabled via unauthorized network or system access. Nation-state or state-affiliated threat actors looking for those oh-so-juicy secrets primarily fall within this pattern.

### Industry labels

We align the CER with the North American Industry Classification System (NAICS), a standard for categorizing victim organizations. NAICS uses two- to six-digit codes to classify organizations. For the CER, we use the two-digit classification level. We provide detailed analyses for seven NAICS-coded industries in “Appendix B: Industry dossiers.” Detailed information on the codes is available here: [naics.com/search-naics-codes-by-industry/](naics.com/search-naics-codes-by-industry/)

### NIST Cybersecurity Framework

We use the National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF) in this report. Specifically, we use the five functional areas of Identify, Protect, Detect, Respond and Recover. See “Appendix A: Frameworks” and here for more information: [nist.gov/cyberframework](nist.gov/cyberframework)

### CIS Critical Security Controls

We also use the 20 Center for Internet Security (CIS) Critical Security Controls (CSCs) in this report. See “Appendix A: Frameworks” and here for more information: [cisecurity.org/controls/cis-controls-list/](cisecurity.org/controls/cis-controls-list/)

### Contact us.

Questions? Comments? Feedback? Drop the VTRAC team a line at vtrac@verizon.com or find us on LinkedIn at #cyberespionagereport and #vtrac

---

## 02 | State of Cyber-Espionage

### Overview

We’ve conducted all sorts of investigations into cybersecurity incidents and data breaches over the years. None have been more challenging or perplexing than Cyber-Espionage attacks.

Indeed, Cyber-Espionage threat actors pose a unique challenge to cyberdefenders and incident responders. Through advanced techniques and a specific focus, these determined threat actors seek to swiftly and stealthily gain access to heavily defended environments. Depending on their goals, they move laterally through the network, obtain targeted access and data, and exit without being detected. Or, they stay back and maintain covert persistence.

Often, threat actors leave little to no indication of their activities, let alone objectives, to avoid detection and thwart response efforts. Many choose not to move immediately toward their objectives, opting to embed themselves in the environment where they persist quietly until their next move.

Threat actors conducting espionage can range from nation-states (or state-affiliated entities) to business competitors, and in some cases, organized criminal groups. Their targets are both the public sector (governments) and private sector (corporations). Their reasons? National security, political positioning and economic competitive advantage. They seek national secrets, intellectual property and sensitive information.

The Cyber-Espionage threat actor modus operandi includes gaining unauthorized access, maintaining a low (or no) profile and compromising sensitive assets and data. Technology makes espionage actors fast, efficient, evasive and difficult to attribute. In a nutshell, for the threat actor, Cyber-Espionage is an opportunity with relatively low risk (of being discovered), low cost (in terms of resources) and high potential (for payoff).

> "The internet has made us richer, freer, connected and informed in ways its founders could not have dreamt of. It has also become a vector of attack, espionage, crime and harm."
> 
> George Osborne, British Politician and Newspaper Editor[^1]

In seeking to accomplish their objectives, Cyber-Espionage threat actors leverage three primary actions:

- Social engineering by targeting employees through activities such as phishing
- Hacking systems and networks by using backdoors and command and control (C2) functions to establish and maintain access
- Deploying malicious software, such as Trojan downloaders, to extend their capabilities

Within the DBIR dataset, we identified the industries most impacted over the past seven years (2014-2020 DBIR timeframe) by Cyber-Espionage breaches: Education, Financial, Information, Manufacturing, Mining + Utilities, Professional and Public. We focused on these industries because they were the most often targeted by these threat actors.

Now, if your industry isn’t featured within this report, you’re not off the hook. Cyber-Espionage threat actors may still be targeting your assets and data—we may just not have visibility into those attacks. If you’ve got sensitive, classified, proprietary or internal secrets that you’d like to keep from getting into the wrong hands, turn the page and read on.

### The ever-evolving threat landscape

To stay ahead of cyberdefenders and incident responders, Cyber-Espionage threat actors adjust their tactics, techniques, and procedures (TTPs) to embrace new technology, while keeping their tried-and-true TTPs operational. Here we map those TTPs to the VERIS Action varieties to give you an idea of what is in and what is out.

For example, Phishing (Social) and Backdoor (Malware) have served as go-to Action varieties. Downloader (Malware), Capture stored data (Malware) and Spyware/Keylogger (Malware) have all steadily declined from the 2014 DBIR to the 2020 DBIR, with Scan network (Malware) completely falling off the top 10 list by the time we get to the 2020 DBIR. Password dumper (Malware), Trojan (Malware) and Remote Access Trojan (RAT) (Malware) are new to the 2020 DBIR top 10 list. And, while we see that since the 2014 DBIR, Backdoor (Malware), Use of backdoor or C2 (Malware) and C2 (Malware) have declined percentagewise over the years, these Action varieties consistently remain within the top five Action varieties for the entire timeframe.

![Figure #1: Top Action varieties within Cyber-Espionage breaches (2014 DBIR; n=282)](fig1_placeholder)
![Figure #2: Top Action varieties within Cyber-Espionage breaches (2014-2020 DBIR; n=1,465)](fig2_placeholder)
![Figure #3: Top Action varieties within Cyber-Espionage breaches (2020 DBIR; n=114)](fig3_placeholder)

### Patterns

> **Breach patterns**
> Breach patterns are just those known, reported and collected. Because Cyber-Espionage attacks are difficult to detect, and the breaches within this pattern are under-reported, the number may be much higher. The kinds of data stolen in Cyber-Espionage breaches (e.g., Secrets, Internal or Classified) may not trigger reporting requirements under many laws or regulations. Cyber-Espionage threat actors are not typically targeting customer data, or even employee data, but rather the intellectual property (or secret sauce if you will) that would give them a leg up in industrial espionage.

When it comes to overall breaches by Incident Classification Pattern for the 2014-2020 DBIR timeframe, we see that Cyber-Espionage ranks sixth (10%)—albeit within close striking distance of fourth: Privilege Misuse (ranked fourth at 11%) and the sagging Point of Sale intrusions (ranked fifth at 11%).

![Figure #4: Breaches by pattern (2014-2020 DBIR; n=16,090)](fig4_placeholder)
![Figure #5: Breaches by pattern (2020 DBIR; n=3,950)](fig5_placeholder)

### Timelines

> **Attacker timelines**
> One of the most effective ways to convey the current state of data breaches and their impact to victim organizations is through temporal analysis or timelining.
> 
> When we look at the DBIR dataset, four timelines manifest most clearly. Two are from the threat actor standpoint—Time to Compromise and Time to Exfiltration—and two are from the cyberdefender and incident responder standpoint—Time to Discovery and Time to Containment.

Traditionally, for all breaches, the DBIR has shown that successful threat actors have taken a short amount of time (seconds to minutes) to compromise, and a relatively short amount of time (minutes to days) to exfiltrate data.

Victim organizations have taken considerably longer (days to months) to discover breaches, and an uncomfortably long time (hours to weeks) to contain breaches.

While the timelines for all breaches may seem bleak, the same timelines for Cyber-Espionage breaches appear even more dire.

In the 2014-2020 DBIR timeframe, for Cyber-Espionage threat actors, the Time to Compromise ranges from mere seconds to days (91%, the sum of 23%, 19%, 23% and 26%), while the Time to Exfiltration ranges from minutes to weeks (88%).

![Figure #6: Time to Compromise within Cyber-Espionage breaches (2014-2020 DBIR; n=47)](fig6_placeholder)
![Figure #7: Time to Compromise within all breaches (2014-2020 DBIR; n=2,658)](fig7_placeholder)
![Figure #8: Time to Exfiltration within Cyber-Espionage breaches (2014-2020 DBIR; n=43)](fig8_placeholder)
![Figure #9: Time to Exfiltration within all breaches (2014-2020 DBIR; n=1,098)](fig9_placeholder)

> **Defender timelines**
> When we look closer, for cyberdefenders, we see the Time to Discovery within Cyber-Espionage breaches is months to years (69%, the sum of 30% and 39%) and the Time to Containment ranges from hours to weeks (64%, the sum of 10%, 25% and 29%).
> 
> The slow, methodical and lengthy process employed by threat actors versus the correspondingly plodding response from cyberdefenders speaks to the patience and complexity often accompanying Cyber-Espionage attacks.

Moreover, this is indicative of the threat actor’s due diligence to not only understand their target’s environment and cybersecurity posture, but also to leverage that knowledge to accomplish their objectives without detection.

> **Top controls**
> - CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
> - CSC-12: Boundary Defense
> - CSC-16: Account Monitoring and Control
> - CSC-19: Incident Response and Management
> - CSC-20: Penetration Tests and Red Team Exercises

![Figure #10: Time to Discovery within Cyber-Espionage breaches (2014-2020 DBIR; n=125)](fig10_placeholder)
![Figure #11: Time to Discovery within all breaches (2014-2020 DBIR; n=2,918)](fig11_placeholder)
![Figure #12: Time to Containment within Cyber-Espionage breaches (2014-2020 DBIR; n=51)](fig12_placeholder)
![Figure #13: Time to Containment within all breaches (2014-2020 DBIR; n=789)](fig13_placeholder)

---

## 03 | Targeted victims

### NIST CSF Identify
Develop an organizational understanding to manage cybersecurity risk to systems, people, assets, data and capabilities.

#### Identification tips
- Identify assets, asset owners and asset access controls as part of an effective and comprehensive risk management strategy
- Align risk management with the organization’s business objectives to add business value and gain buy-in from decision makers
- Leverage cyber threat intelligence to help prioritize Cyber-Espionage attacks as part of the risk management process
- Avoid complacency. Cyber-Espionage attacks can potentially impact all organizations—even those in lesser-targeted industries

An organization that leverages cyber threat intelligence to prioritize Cyber-Espionage attacks as part of its risk management process can start by asking questions relevant to the organization, such as:

- How prevalent are Cyber-Espionage attacks compared to other cybersecurity attack patterns?
- Which Cyber-Espionage threat actors have been targeting other similar organizations? Based on this, how likely is the organization to be targeted?
- What assets and data are Cyber-Espionage threat actors targeting?
- What are the common TTPs of Cyber-Espionage threat actors?

If the answers to these questions point to lower risk, does it mean that in some industries, such as Healthcare or Accommodation, organizations should not be concerned with Cyber-Espionage? Not at all. This data shouldn’t be analyzed without context. For example, while the number of Cyber-Espionage breaches may be lower in some industries, the impact of sensitive or proprietary data exposure on an organization in one of those lesser-targeted industries could be substantial.

Long story short: Just because your organization’s industry has not been a typical target for Cyber-Espionage threat actors doesn’t mean it won’t be, can’t be or hasn’t been.

A fundamental requirement for a solid information security posture is identifying assets before the adversary does. It’s only when the unknowns become known that assets and data can be protected. After all, you don’t know—and cannot protect—what you don’t know.

Asset identification is a foundational part of the risk management process, which aims to define and prioritize risks for an organization. Risk managers often build matrices listing threats in order of severity. They also classify assets in terms of confidentiality, integrity and availability (referred to as the “CIA Triad”); consider the impact of security breaches on the organization; and estimate the likelihood of certain incidents.

Risk management also requires an organization to identify asset owners and asset access controls. Asset identification and risk management should align with the organization’s business objectives to add value to the business and help gain buy-in from decision makers. For example, a business-driven risk management strategy could include:

- Defining objectives
- Identifying assets and threats
- Selecting and prioritizing targets
- Monitoring and detecting threats
- Responding and improving response capabilities

While it can be an overwhelming task to start from scratch, it’s possible to develop a risk management process with smaller objectives by incorporating cyber threat intelligence and building and refining from there.

VERIS and the Center for Internet Security (CIS) Critical Security Controls (CSCs), as well as the VERIS Common Attack Framework (VCAF)—a VERIS-to-MITRE ATT&CK® Framework introduced in the 2020 DBIR—are publicly available resources for formalizing incident and threat data. VERIS helps categorize security incidents, while CIS CSCs help focus on cybersecurity controls.

Risk analysis, asset identification and incident classification can inform the appropriate measures for preventing, mitigating, detecting and responding to threat actors while also maintaining the ability to meet organizational business objectives.

### Regions

For the 2014-2020 DBIR timeframe, we see Cyber-Espionage breaches occurring most often in the Asia-Pacific (APAC) region (42%), followed by the Europe, Middle East and Africa (EMEA) region (34%), and North America (NA) (23%) region. This contrasts sharply with all breaches for this same timeframe, as NA (65%) dominates, followed by APAC (17%) and EMEA (16%).

![Figure #14: Cyber-Espionage breaches by region (2014-2020 DBIR; n=597)](fig14_placeholder)
![Figure #15: All breaches by region (2014-2020 DBIR; n=6,780)](fig15_placeholder)

### Industries

#### Overall Cyber-Espionage breaches within select industries

One way to identify industries impacted by Cyber-Espionage attacks is by examining overall Cyber-Espionage breach numbers.

When we look at how the industries that were featured in the 2020 DBIR fared when it comes to Cyber-Espionage breaches, we can see that some were more strongly impacted than others. In particular, Public (31%), Manufacturing (22%) and Professional (11%) topped the list for Cyber-Espionage breaches.

This is a good time to point out that the DBIR dataset can only tell us what the DBIR dataset knows. The DBIR dataset consists of successful, reported and known data breaches (and cybersecurity incidents). It doesn’t cover undiscovered, unreported or uncollected data (i.e., data originating outside of the 81 contributors to the 2020 DBIR).

While we have included more detailed, industry-specific Cyber-Espionage profiles in “Appendix B: Industry dossiers,” here we provide insight into seven industries. These sectors are the most impacted by Cyber-Espionage breaches over the 2014-2020 DBIR timeframe and have sufficient content for analysis. Industry (NAICS #): Education (61), Financial (52), Information (51), Manufacturing (31-33), Mining + Utilities (21+22), Professional (54) and Public (92).

![Figure #16: Cyber-Espionage breaches within select industries (2014-2020 DBIR; n=1,580)](fig16_placeholder)

#### Cyber-Espionage breaches within all breaches of select industries

Another way to look at industries impacted by Cyber-Espionage attacks is the number of Cyber-Espionage breaches within all breaches. For the 2014-2020 DBIR timeframe, we see Manufacturing (35%), Mining + Utilities (23%), Public (23%), Professional (17%), Education (8%), Information (7%) and Financial (2%) for percentage of Cyber-Espionage breaches within all breaches by industry.

We include more detailed, industry-specific Cyber-Espionage profiles in “Appendix B: Industry dossiers.” Here we provide insight into Breaches by pattern, Cyber-Espionage within all breaches, Actors within Cyber-Espionage, Actions within Cyber-Espionage, Assets within Cyber-Espionage and compromised data within Cyber-Espionage for these seven industries.

Note: In Figure #16 and Figure #17, numbers in parentheses after each industry correspond to the 2-digit NAICS #.

![Figure #17: Cyber-Espionage breaches within all breaches of select industries (2014-2020 DBIR)](fig17_placeholder)

---

## 04 | Essential Elements of Friendly Information

### NIST CSF Protect
Develop and implement appropriate safeguards to ensure delivery of critical services.

Sophisticated threat actors often use stealthy methods to perpetrate Cyber-Espionage attacks. These methods can include utilizing compromised administrative credentials or leveraging dual-use tools that blend in with the environment.

These threat actors also deploy custom zero-day malware, which antivirus or other alerting software cannot detect. From our experience, Cyber-Espionage attacks—using sophisticated techniques; taking steps to avoid detection; and having specific, targeted objectives—tend to be considerably more difficult to detect and investigate than other breaches. Nevertheless, there are ways to protect against them even without specific knowledge of their custom/zero-day nature.

### Access control

With administrative permissions and a flat (i.e., unsegmented) network, a threat actor has the freedom to roam. Even in segmented networks, a threat actor can find their way to the coveted data utilizing mapping and other dual-use tools. Network segmentation, strict access controls, layered security (the more access controls the better), a least-privilege practice and multifactor authentication for lateral movement into critical data areas can all help safeguard against Cyber-Espionage attacks.

### Awareness and training

As seen in the 2020 DBIR, Cyber-Espionage attacks rely heavily on Social and Malware combined vectors, using Phishing in 81% of the incidents and some form of Malware in 92%. Training end users to recognize and report social attacks, such as phishing or pretexting, can help reduce poor outcomes related to Cyber-Espionage attacks.

### Data security

Secure the data that is most valuable and sought after by cyber threat actors. Compile a critical data inventory and implement access controls and monitoring to ensure that data is safe.

### Processes and procedures

Appropriately crafted corporate processes and procedures can help protect sensitive data. These should cover everything from ensuring that user devices are protected with encryption and strong passwords to restricting the use of public Wi-Fi and determining how sensitive data should be securely transmitted. Security practices should ensure safe and closely controlled access to potentially vulnerable data.

### Maintenance

Cyber-Espionage risk mitigation is far from a set-it-and-forget-it strategy. Regular maintenance should be performed to ensure that employees follow proper cybersecurity measures and procedures so that data is protected.

### Protective technology

Some Cyber-Espionage protective measures can be automated. Data Leakage Prevention (DLP) solutions send alerts when data leaves the network. These solutions also offer a large variety of features, such as detecting or blocking data copied to external locations, sent by email, or shared using file-sharing apps and sites; preventing protected data from being printed; and more. DLP solutions can even help identify unencrypted data destinations.

#### Protection tips
- Safeguard against Cyber-Espionage attacks with network segmentation, strict access controls, layered security, a least-privilege practice and multifactor authentication for lateral movement into critical data areas
- Train end users to recognize and report social attacks, such as phishing or pretexting
- Compile a critical data inventory and implement access controls and monitoring to ensure that data is safe
- Implement DLP solutions to detect and prevent sensitive data from being exported, shared or copied

### Attributes

#### Compromised Attributes

In the 2014-2020 DBIR timeframe, for both Cyber-Espionage breaches and all breaches, the top compromised Attribute is Confidentiality (100%). This is by definition. For an incident to meet the VERIS requirement for breach classification, it has to exhibit a confirmed data compromise, which equates with Confidentiality. Thus, all Cyber-Espionage breaches impact the Confidentiality attribute.

Integrity (95%) and Availability (1%) follow Confidentiality for Cyber-Espionage breaches. Integrity, because Social actions impact the person targeted (Alter behavior), and Malware actions impact the asset where it was installed (Software installation). These two are among the favorite TTPs of the Cyber-Espionage threat actor. In contrast, most of these attacks do not affect the availability of the asset—as that would likely lead to faster discovery of the threat actor.

> **CIA Triad**
> For VERIS, compromised asset security attributes are based on the expanded CIA Triad, which includes confidentiality/possession, integrity/authenticity and availability/utility. Multiple attributes can be affected for any one asset, and each attribute contains different metrics.

![Figure #18: Compromised Attributes within Cyber-Espionage breaches (2014-2020 DBIR; n=1,580)](fig18_placeholder)
![Figure #19: Compromised Attributes within all breaches (2014-2020 DBIR; 16,090)](fig19_placeholder)

#### Compromised Attribute varieties

When we look at Cyber-Espionage breaches and the top compromised Attribute varieties for the 2014-2020 DBIR timeframe, we see Software installation (Integrity) (91%), Alter behavior (Integrity) (84%) and Secrets (Confidentiality) (73%) as top compromised Attribute varieties.

In comparing all breaches to Cyber-Espionage breaches during the 2014-2020 DBIR timeframe, we see Software installation (Integrity) (43%) and Alter behavior (Integrity) (32%) as first and second for all breaches, which parallels Cyber-Espionage breaches, albeit at a much lower percentage. For all breaches, the next two compromised Attribute varieties are Credentials (Confidentiality) (29%) and Personal (Confidentiality) (28%), whereas for Cyber-Espionage breaches, the third and fourth most compromised Attribute varieties are Secrets (Confidentiality) (73%) and Internal (Confidentiality) (29%).

Secrets and Internal compromised Attribute varieties ranking so high within Cyber-Espionage breaches comes as no surprise, as these are the top compromised Data varieties (see “Data” section of this report).

> **Top controls**
> - CSC-4: Controlled Use of Administrative Privileges
> - CSC-5: Secure Configuration for Hardware and Software
> - CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
> - CSC-8: Malware Defenses
> - CSC-13: Data Protection
> - CSC-16: Account Monitoring and Control

![Figure #20: Top compromised Attribute varieties within Cyber-Espionage breaches (2014-2020 DBIR; n=1,571)](fig20_placeholder)
![Figure #21: Top compromised Attribute varieties within all breaches (2014-2020 DBIR; n=14,736)](fig21_placeholder)

### Assets

#### Compromised Asset varieties—Short term

At a high level, top compromised Assets (n=115) for the 2020 DBIR timeframe are User Device (87%), Person (82%) and Server (26%). Interestingly, if we look closer at compromised Asset varieties for this timeframe, we see contemporary assets being affected more so than over the 2014-2020 DBIR timeframe.

The top compromised asset varieties for the 2020 DBIR timeframe in Cyber-Espionage breaches were Desktop or laptop (88%), Mobile phone (14%) and Web application (10%). For all breaches, these are Web application (43%), Desktop or laptop (31%) and Mail (21%). The Desktop or laptop, Mobile phone and Mail compromised Assets are likely due to Cyber-Espionage attacks starting with Social action.

![Figure #22: Top compromised Asset varieties within Cyber-Espionage breaches (2020 DBIR; n=113)](fig22_placeholder)
![Figure #23: Top compromised Asset varieties within all breaches (2020 DBIR; n=2,667)](fig23_placeholder)

#### Compromised Asset varieties—long term

Also, at a high-level, for the 2014-2020 DBIR timeframe, top compromised Assets (n=1,492) are Person (88%), User Device (83%) and Server (34%). When we look at compromised Asset varieties impacted by Cyber-Espionage breaches for this timeframe, we see Desktop or laptop (89%) and Desktop (80%) leading the pack, with Mobile phones (9%) a very distant third followed by Router or switch (8%).

For top compromised Asset varieties within all breaches, Desktop or laptop (32%), Web application (30%) and Desktop (24%) are listed as the top three, with Point of Sale (POS) controller (13%), POS terminal (12%) and Database (12%) vying for fourth place.

Web application, POS controller and POS terminal speak to the wide variety of Assets that threat actors target in the all breaches category. The Desktop or laptop, Desktop and Mobile phone varieties speak to social engineering—a popular threat action for threat actors associated with Cyber-Espionage breaches as well as breaches in general.

> **Top controls**
> - CSC-5: Secure Configuration for Hardware and Software
> - CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
> - CSC-17: Implement a Security Awareness and Training Program
> - CSC-18: Application Software Security
> - CSC-20: Penetration Tests and Red Team Exercises

![Figure #24: Top compromised Asset varieties within Cyber-Espionage breaches (2014-2020 DBIR; n=1,297)](fig24_placeholder)
![Figure #25: Top compromised Asset varieties within all breaches (2014-2020 DBIR; n=13,217)](fig25_placeholder)

### Assets and vulnerabilities

#### Critical assets

Significant research and analysis have focused on developing models aimed at helping organizations identify, measure and monitor the criticality of their assets. These models, such as the NIST IR 8179 (Criticality Analysis Process Model), are aimed at helping organizations better identify, understand and protect their assets. This approach focuses on not only the asset’s criticality to business operations but also the potential damage/impact of the loss of the asset. However, many such analytical models tend to view assets through a single lens and don’t necessarily assess them through the prism of Cyber-Espionage.

This nuance is particularly important when two factors are considered. First, while the overall significance of Cyber-Espionage as a whole is relatively low and appears to be decreasing (as indicated in the 2020 DBIR), a by-industry breakdown reveals a more nuanced picture.

Reported instances of Cyber-Espionage breaches have been concentrated in certain industries (such as Manufacturing, Mining + Utilities and Public), while other industries (Construction, Real Estate) reported none at all (note that this doesn’t necessarily mean none occurred or that there is no risk for those particular industries, just that none were reported where we had visibility). This implies that any organization’s critical asset/sensitive data management strategy may need to adjust to the Cyber-Espionage risk associated with their particular vertical.

It’s reasonable to assume that the overall Cyber-Espionage rate suffers from chronic underreporting. Other motivations (i.e., Financial) lend themselves toward having a more clearly identifiable end state. Cyber-Espionage, on the other hand, can potentially be associated with longer attack timelines and potentially unending exploitation.

In self-assessing critical assets and sensitive data, organizations need to ensure that their assessment criteria account for the possibility of Cyber-Espionage. Specifically, their model should address:

1. Overall Cyber-Espionage risk
2. Assets/data susceptible to Cyber-Espionage
3. Safeguards and monitoring to alert on Cyber-Espionage attacks
4. Preventative measures for Cyber-Espionage, such as:
   - a. Continuous critical asset/sensitive data identification, protection and monitoring
   - b. Cyber threat intelligence/dark web research/threat hunting
   - c. Insider Threat Program
   - d. Competitive landscape awareness (i.e., unexpected loss of competitive advantage)

#### Targeted vulnerabilities

Vulnerabilities occupy a huge amount of mindshare in information security. Security researchers, independent hackers, nation-state actors, organized criminal groups, customers and even employees discover thousands of vulnerabilities every year ([https://www.cvedetails.com/browse-by-date.php](https://www.cvedetails.com/browse-by-date.php)).

Some discovered vulnerabilities are reported responsibly and some (including their exploit code) are stashed away for a multitude of reasons (most of which are nefarious in nature). Most application software and firmware vendors have established formal programs to release patches on a periodic basis, or on an emergency basis depending on the severity of the vulnerability.

Periodically, organizations discover scores of known vulnerabilities within their infrastructure using typical vulnerability scanning tools and patch them based on risk assessment. However, threat actors leverage a relatively small percentage of these vulnerabilities in breaches, as you can see in the diagram below from the 2020 DBIR.

![Figure #26: Vulnerability exploitation over time in breaches](fig26_placeholder)

Zero-day vulnerability exploits—those security weaknesses not disclosed to vendors or developers—make tackling vulnerabilities even harder for impacted organizations. More often than not, the exploitation of such vulnerabilities doesn’t leave credible evidence on the system (although there may be some circumstantial evidence left somewhere else).

There were times when zero-day vulnerabilities were for sale on the dark web. Due to recent enforcement actions by some marketplace operators, the not-so-good researchers have become less active and have possibly moved to other avenues for financial gain and other motives. We’ve seen—and continue to see—organized crime syndicates or nation-state and state-affiliated actors use zero-day vulnerabilities to exploit systems for nefarious purposes.

It is important to realize that vulnerabilities are here to stay, and the typical patch-cycle mentality cannot solve this problem. A multilayered approach consisting of several controls, such as robust risk management, use of strict least-privilege principle, application whitelisting, threat hunting and deception-based detection techniques, can help protect against the invisible monster.

### Data

#### Cyber-Espionage breaches—Short term

The top compromised Data varieties for Cyber-Espionage breaches for the 2020 DBIR timeframe are data types that fall outside regulatory reporting requirements: Credentials (56%), Secrets (49%), Internal (12%) and Classified (7%), with Bank (6%), Source code (6%) and Digital certificate (6%) all statistically tied for fifth. In addition, much like the 2014-2020 DBIR timeframe, this makes sense for Cyber-Espionage breaches, as threat actors would seek these Data varieties for competitive gain.

![Figure #27: Top compromised Data varieties within Cyber-Espionage breaches (2020 DBIR; n=110)](fig27_placeholder)

#### All breaches—Short term

When we look at compromised Data varieties for the 2020 DBIR timeframe, a different story emerges for all breaches. We find Personal (58%), Credentials (41%), Internal (17%) and Medical (16%) as the top compromised Data varieties for all breaches, with Payment (12%) and Bank (11%) bringing up the rear. With the exception of Credentials, these Data varieties align with regulatory reporting for data breaches in general.

![Figure #28: Top compromised Data varieties within all breaches (2020 DBIR; n=3,373)](fig28_placeholder)

#### Cyber-Espionage breaches—Long term

For compromised Data varieties in the 2014-2020 DBIR timeframe, we find that Cyber-Espionage threat actors seek these data types most frequently: Secrets (75%), Internal (30%), Credentials (22%), System (19%) and Classified (9%). This makes sense for Cyber-Espionage breaches, as these data types are ostensibly sought after by threat actors targeting sensitive/propriety/classified information.

![Figure #29: Top compromised Data varieties within Cyber-Espionage breaches (2014-2020 DBIR; n=1,526)](fig29_placeholder)

#### All breaches—Long term

For all breaches, we see Credentials (31%), Personal (31%), Payment (23%), Medical (13%) and Internal (13%) as more valuable targets for compromised Data varieties. Moreover, this is understandable because, with the exception of Credentials and Internal, these Data varieties fall within the realm of mandatory regulatory reporting requirements for breaches in general.

> **Top controls**
> - CSC-4: Controlled Use of Administrative Privileges
> - CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
> - CSC-13: Data Protection
> - CSC-14: Controlled Access Based on the Need to Know
> - CSC-16: Account Monitoring and Control
> - CSC-17: Implement a Security Awareness and Training Program

![Figure #30: Top compromised Data varieties within all breaches (2014-2020 DBIR; n=13,657)](fig30_placeholder)

---

## 05 | Threat actors

### NIST CSF Detect
Develop and implement appropriate activities to identify the occurrence of a cybersecurity event.

The 2016 DBIR reported that, in general, victim organizations seldom detect data breaches. Rather, external sources are more likely to make the discovery. This trend remains the same even years later in the 2020 DBIR and is especially true for Cyber-Espionage breaches in the 2014-2020 DBIR timeframe. These breaches tend to allow the adversary to siphon as much information as possible from their victim for as long as possible while remaining undetected.

The questions for organizations in 2016 were how could an organization improve its Time to Discovery trend? How can it avoid relying mostly on external sources that lie beyond its control? How can it detect intrusions as they occur if not before they occur? These questions led to innovation in the detection-technology space, which we cover later in the report.

However, despite some organizations adopting these new technologies, the problem remains. A possible explanation is that these new techniques often rely on the organization having first covered the basics, such as determining network activity baselines, defining cybersecurity incidents and specifying alert thresholds, which isn’t always the case.

Before investing in new technology, an organization should verify that its cybersecurity foundations are solid. Security strategists can accomplish this by adopting the Capability Maturity Model (CMM) strategy, originally developed to improve software development processes. The CMM relies on measuring, controlling and regularly updating documentation and processes to limit the unknowns.

During VTRAC data breach investigations, crucial data is often unavailable. Gaps come in the form of missing log files, undocumented systems, poor data accessibility, network traffic flows, operational practices, and underestimated or under-documented data-sensitivity issues.

This lack of information not only hinders a data breach investigation and subsequent incident response efforts, but it also creates golden opportunities for the adversary to easily find and access potentially sensitive information.

It’s also important to remember that having the best technology in your arsenal doesn’t help unless you have equally mature processes as well as suitably skilled and trained personnel to manage it effectively.

The last few years have seen the development and enhancement of both network and host detection and prevention systems. These have been re-envisioned as Endpoint Detection and Response (EDR) and Network Detection and Response (NDR) solutions. Event and telemetry data from these systems typically roll up into Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) solutions to trigger response and containment, eradication, remediation and recovery actions.

These technologies have moved beyond outdated signature-based detection toward behavior-pattern detection enhanced with cyber threat intelligence, automation, and machine learning or artificial intelligence (i.e., statistical analysis and anomaly detection). Solutions also facilitate proactive analysis, often referred to as “security health checks.”

One way to address the gap between compromise and detection speed in breaches involving adversaries using evasion tactics is to enhance detection capabilities while keeping up with new evasion techniques. Organizations should develop defensive capabilities, such as counterespionage deception techniques, specifically to reflect these emerging evasion TTPs.

#### Detection tips
- Verify that the organization’s cybersecurity foundations are solid by adopting the CMM strategy
- Ensure the availability of crucial data by reducing the incidence of missing log files, undocumented systems, poor data accessibility, network traffic flows, operational practices, and underestimated or under-documented data-sensitivity issues
- Develop counterespionage detection techniques that evolve to reflect emerging evasion TTPs
- Move toward behavior-pattern detection enhanced with cyber threat intelligence, automation, and solutions based on machine learning or artificial intelligence
- Leverage experienced security professionals to manage advanced technology

[^1]: ‘Chancellor’s speech to GCHQ on cybersecurity’: public-sector.co.uk/article/ff8fa006cdcd35f4cf9ef4e030e08ff1

---

1 Cyber-Espionage Report

0% 10% 20% 30% 40% 50%
Discovery methods
Suspicious traffic 48%
In terms of top Discovery methods for Cyber-Espionage Antivirus 23%
Emergency response team 7%
breaches in the 2014-2020 DBIR timeframe, we see the
Reported by employee 5%
top two methods as Suspicious traffic (48%) and Antivirus Law enforcement 4%
(23%), with Emergency response team a distant third (7%). NIDS 3%
This contrasts sharply with the top Discovery methods for Log review 2%
all breaches for the same timeframe, in which we see Law
enforcement (28%), Fraud detection (19%) and Customer
Figure #31: Top Discovery methods for Cyber-Espionage breaches
(15%), respectively, at the top. (2014-2020 DBIR; n=408)
When we put on the threat actor “motive filter,” this makes
sense. Data breaches overall are dominated by the Financial
motive, whereas Cyber-Espionage breaches align with the 0% 10% 20% 30% 40% 50%
Espionage motive, which is much more targeted in its approach. Law enforcement 28%
Fraud detection 19%
A factor at play here is that the Financial motive threat Customer 15%
actor has to contend with the Payment Card Industry (PCI) Reported by employee 8%
Common Point of Purchase (CPP) fraud detection system. Monitoring service 6%
Actor disclosure 6%
There is no corresponding detection service looking for theft
Suspicious traffic 4%
of trade secrets, which contributes to longer discovery times.
Figure #32: Top Discovery methods for all breaches
(2014-2020 DBIR; n=7,025)
Top controls
• CSC-6: Maintenance, Monitoring and Analysis of
Audit Logs
• CSC-8: Malware Defenses
• CSC-12: Boundary Defense
• CSC-19: Incident Response and Management
21 2020-2021 Cyber-Espionage Report

Actors
100%
Actors over time
80%
For the 2014-2020 DBIR timeframe, External actors have  External
dominated Actor types, ranging from 69% to 88% over this
| timeframe, with Internal actors a distant second, ranging from  | 60% |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
12% to 34% over the same timeframe.
40%
When we look at Cyber-Espionage breaches for the 2014- Internal
2020 DBIR timeframe, External actors (State-affiliated,
Nation-state, Organized crime, Former employee and  20% Multiple
Partner
Competitor combined) are at 100%. This makes sense, as
0%
within VERIS, Cyber-Espionage threat actors are coded as
|     | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 2020 |
| --- | ---- | ---- | ---- | ---- | ---- | --------- |
External actors in all breaches.
|     | (n=1,477) | (n=1,792) | (n=2,600) | (n=1,990) | (n=2,231) | (n=1,979) (n=3,904) |
| --- | --------- | --------- | --------- | --------- | --------- | ------------------- |
Figure #33: Actors over time for all breaches (2014-2020 DBIR)
Actor varieties
Attempting to identify Actor varieties is an immense
challenge in cyberspace. Threat actors go to great lengths  0% 20% 40% 60% 80% 100%
to maintain anonymity, obfuscate their activities and
|     | State-affiliated |     |     |     |     | 85% |
| --- | ---------------- | --- | --- | --- | --- | --- |
impede identification using bogus IP addresses (even
|     | Nation-state |     | 8%  |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- |
MAC addresses can be spoofed), domain names, email  Organized crime 4%
|     | Former employee | 2%  |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- |
addresses, file names and malware tools, among other
|     | Competitor | 1%  |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- |
indicators of compromise (IoCs).
|     | Unaffiliated | 0%  |     |     |     |     |
| --- | ------------ | --- | --- | --- | --- | --- |
|     | End-user     | 0%  |     |     |     |     |
The top Actor varieties in Cyber-Espionage breaches for the
|     | Activist | 0%  |     |     |     |     |
| --- | -------- | --- | --- | --- | --- | --- |
2014-2020 DBIR timeframe are State-affiliated (85%), Nation-
|     | Developer | 0%  |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
state (8%), Organized crime (4%) and Former employee (2%).
This should be no surprise, as State-affiliated and Nation-state
Figure #34: Actor varieties within  Cyber-Espionage breaches
threat actors align more with the Espionage motive.
(2014-2020 DBIR; n=1,435)
For all breaches during this same timeframe, we see a bit of
a different picture, with Organized crime (59%) dominating
the list of Actor varieties, followed by State-affiliated (13%),
|     |     | 0%  | 20% | 40% | 60% | 80% 100% |
| --- | --- | --- | --- | --- | --- | -------- |
Unaffiliated (7%), and then End-user (6%) and System admin
(4%). Organized crime has been identified mainly with the  Organized crime 59%
Financial motive, one that continues to dominate our DBIR  State-affiliated 13%
| dataset for all breaches over the years. | Unaffiliated    | 7%  |     |     |     |     |
| ---------------------------------------- | --------------- | --- | --- | --- | --- | --- |
|                                          | End-user        | 6%  |     |     |     |     |
|                                          | System admin    | 4%  |     |     |     |     |
|                                          | Nation-state    | 1%  |     |     |     |     |
|                                          | Developer       | 1%  |     |     |     |     |
|                                          | Former employee | 1%  |     |     |     |     |
Threat actors defined
|     | Executive | 1%  |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
Threat actors are entities that cause or contribute
to a data breach or cybersecurity incident. External  Figure #35: Actor varieties within all breaches
actors originate from outside the organization  (2014-2020 DBIR; n=9,077)
and its network of partners and typically have no
trust or privilege granted to them. Internal actors
originate from within the organization and enjoy
some level of trust and privilege. Partner actors
include any third party that shares a business
relationship with the organization and thus enjoys
some level of trust and privilege.
| 22  |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | -------------------------------- | --- |

The labyrinth:
How attribution could be wrong
Digital forensic investigations should On top of that, Tor (The Onion
ideally answer the five Ws (who, what, Router) networks, the dark web,
where, when and why) and one H (How) business infrastructures that lack
questions. However, challenges related security, and privacy legislations in
to the availability and granularity of certain countries further complicate
detail in evidentiary data can leave attribution. Using cryptocurrencies
many questions unanswered. (especially altcoins, such as Monero,
offering anonymity) or services, such
Cyberattack attribution in particular as coin mixers, makes tracing the
is meant to address the “Who” and origin of attacks more difficult.
“Why” questions. Investigators focus
on threat actor TTPs, consult cyber Another very important obstacle is the
threat intelligence reports and review extreme difficulty of prosecuting cross-
IoCs to root out perpetrators and border cybercriminals, which nation-
mount a defense. state actors inherently protect. The lack
of local legal statutes, regulations or
However, IoCs such as IP addresses, reliable evidence lessens deterrence
domain names, file names, malware and may even motivate threat actors.
behavior and binary code sections
can be misleading. Consequently, Finally, it should be noted that
investigators shouldn’t rely only on attribution is a multidimensional
these to make a cyberattack attribution. challenge. Attribution—aside from
forensic evidence—depends on
The current geopolitical climate, various types of intelligence, including
recent pandemic and heightened forensics evidence; Technical
trade tensions provide a conducive Intelligence (TECHINT); Human
environment for cyberattack Intelligence (HUMINT); Signals
misattribution. This is especially true for Intelligence (SIGINT); Open Source
Cyber-Espionage attacks that typically Intelligence (OSINT); and adversarial
involve tactics such as leveraging tradecraft (i.e., TTPs), infrastructure
covert TTPs and “false flags.” Threat and intent. All dimensions must align
actors associated with these attacks for sound and reliable attribution.
are attempting to thwart detection and
response efforts, as well as conceal
attack attribution for political and
national security purposes.
2233 22002200--22002211 CCyybbeerr--EEssppiioonnaaggee RReeppoorrtt

Motives
| Motives over time |     |     |     | Motives |     |     |     |
| ----------------- | --- | --- | --- | ------- | --- | --- | --- |
For the 2014-2020 DBIR timeframe, annually, we see  Within the dataset that shows all breaches, for both the
Financial motive underlying breaches between 67% and 86%  2020 DBIR and 2014-2020 DBIR timeframes, we see
of the time and Espionage motive as the driver between 10%  Financial motive as the overwhelming Actor motive (86%
and 26% of the time. and 76%, respectively), with Espionage the second highest
motive (10% and 18% respectively).
Given their nature (e.g., stealthy tactics, specific targeting),
Espionage attacks can be difficult to detect and identify as  Actor motives consolidated in “The Rest” (6%) for the
an actual Espionage-related attack (given scant IoCs and  2014-2020 DBIR timeframe include Fun (3%), Grudge (1%),
| other details). |     |     |     | Convenience (1%) and Ideology (1%). |     |     |     |
| --------------- | --- | --- | --- | ----------------------------------- | --- | --- | --- |
Whereas Financial attacks—if not detected while occurring or
soon thereafter—eventually become apparent when money
goes missing. At that point, the Financial motive, if not already
ascertained, can be determined.
100%
Financial
80%
60%
40%
Espionage
20%
0%
|     | 2014 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 |
| --- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
(n=1,141) (n=1,208) (n=1,419) (n=1,552) (n=2,089) (n=1,320) (n=1,134)
Figure #36: Actor motives over time within all breaches (2014-2020 DBIR)
| 0% 20%      | 40% | 60% | 80% 100% | 0%          | 20% 40% | 60% | 80% 100% |
| ----------- | --- | --- | -------- | ----------- | ------- | --- | -------- |
| Financial   |     |     |          | Financial   |         |     |          |
|             |     |     | 86%      |             |         |     | 76%      |
| Espionage   |     |     |          | Espionage   |         |     |          |
| 10%         |     |     |          |             | 18%     |     |          |
| Grudge      |     |     |          | Fun         |         |     |          |
| 2%          |     |     |          | 3%          |         |     |          |
| Fun         |     |     |          | Grudge      |         |     |          |
| 1%          |     |     |          | 1%          |         |     |          |
| Convenience |     |     |          | Convenience |         |     |          |
| 1%          |     |     |          | 1%          |         |     |          |
| Ideology    |     |     |          | Ideology    |         |     |          |
| 1%          |     |     |          | 1%          |         |     |          |
Figure #37: Actor motives within all breaches   Figure #38: Actor motives within all breaches
| (2020 DBIR; n=1,141) |     |     |     | (2014-2020 DBIR; n=9,863) |     |                                  |     |
| -------------------- | --- | --- | --- | ------------------------- | --- | -------------------------------- | --- |
| 24                   |     |     |     |                           |     | 2020-2021 Cyber-Espionage Report |     |

Proactive defense:
The best defense is a great offense.
Threat hunting | Additional actions
Behavioral analysis
Consider taking these additional
Advanced threat actors attempt protective measures:
to blend in to evade automated
cyberdefense measures. With the rise • Assign all users separate, unique
of zero-day and fileless attacks, it’s accounts. Don’t use generic or
harder than ever to protect endpoints shared accounts or passwords
with confidence. In addition, preventing • Block outbound, unrestricted internet
and detecting these attacks can be a access from server infrastructure.
huge drain on organizational resources. This is intended to prevent
adversaries from exfiltrating data to
Compromise happens within minutes
known or unknown IP addresses and
to hours, as we have seen consistently
using services, protocols or ports in
over the years in the DBIR. This is mainly
an unauthorized manner
attributable to the use of email and
web-based threat vectors coupled with • Create adequate network
heavily automated attacks (nowadays segmentation to separate virtual local
also powered by machine learning). area networks (VLANs) from internet-
facing infrastructure, server farms,
Visibility and detection speed internal networks and administrator
techniques play a very important role networks. Appropriate segmentation
in this never-ending battle against makes it difficult for an adversary to
cyberattacks. It is imperative that move laterally within the network
detection measures be a combination
• Restrict PowerShell and other native
of signature- and behavior-based
scripting to only individuals with an
techniques. One cannot manage or
acknowledged legitimate use and track
defend against unknown threats using
the assignment of such privileges
traditional means. Effective, efficient
and multilayered threat hunting can • Prohibit interactive log-ons using
help give you a significant advantage in service accounts or “break-the-glass”
detecting these unknowns. accounts. Implement a rule in the
SIEM to trigger an alert to the security
Threat hunting consists of: operations team whenever an attempt
is made to log on to any system
1. Making hypothesis-driven exercises interactively using service accounts
2. Proactively and reactively searching • Require two-factor authentication
for threat actor activities for all administrative access to
infrastructure components. This
3. Effectively eliminating, or at least
implementation will mitigate the
reducing, false negatives (indicators
impersonation risk and prohibit access
that signature-based detection
using unauthorized credentials
approaches can overlook)
4. Assuming that threat actors are
already present in the infrastructure
5. Placing a strong focus on indicators
of attack (IoAs) combined with IoCs
6. Prioritizing overall threat types and
looking for the most dangerous
ones first
2255 22002200--22002211 CCyybbeerr--EEssppiioonnaaggee RReeppoorrtt

Tradecraft
06
NIST CSF Respond
One key objective for a Cyber- Sometimes, the cyber threat
Develop and implement appropriate
Espionage investigation is to identify intelligence team encounters stolen
activities to take action regarding a
“patient zero” and determine how data and credentials being traded by
detected cybersecurity incident.
the adversary gained access to the cybercriminals, and this data is all the
infrastructure. Common methods of adversary needs for further attacks on
entry include exploiting an internet- an organization.
Investigating Cyber-Espionage
facing application, applying brute force
breaches differs from researching
to an account, using phishing email to One key challenge faced during
cybersecurity incidents. Thus, incident
gain an initial foothold or compromising Cyber-Espionage investigations is the
responders and forensic investigators
the human factor—trust. identification of compromised systems.
may not initially realize that an
Many Cyber-Espionage attacks are
attack is targeted and the motive is
During Cyber-Espionage investigations, associated with advanced persistent
intellectual property theft. It’s only as
it is common to find phishing (or attacks—multistaged attacks that
the investigation progresses and the
targeted phishing) emails as the initial involve lateral movement.
complexity of the attack becomes
vector. These emails usually are well
apparent that investigators take a
crafted (industry specific) to lure the Identifying compromised assets or
slightly different approach.
recipients either to click a URL hosting assets posing as intermediaries can
a malicious or lookalike website, or be a challenge. Cyber-Espionage
Before the investigation, investigators
to open an attachment that executes attacks employ specifically created
collect technical information such
malicious software. In some cases, malware that causes multiple layers
as network topology. Investigators
obtaining user credentials is the goal for of obfuscation and malware variants,
also interview network and system
follow-on use in the initial penetration. making IoC-based detection within the
administrators to scope out the incident
enterprise environment difficult.
and identify possible intrusion channels.
Based on the information received
In addition, investigators collect in-
from the impacted organization and A further challenge is that Cyber-
scope volatile data and system images
the results of the initial analysis, the Espionage attacks often leverage
plus all associated logs from various
threat-intelligence team endeavors legitimate credentials and legitimate
sources, such as system (including
to identify an associated threat actor. dual-use tools, such as network
PowerShell or System Monitor), SIEM
By identifying its goals, capabilities mapping or remote access software
and proxy logs.
and methods, the team can develop already being used in the environment.
attack models—based on the most This makes it extremely difficult to
Understanding how the incident was
common and most lethal cybersecurity differentiate between malicious actions
detected helps an investigator triage
incidents—to prepare for and better and legitimate administrative tasks.
and scope, as Cyber-Espionage attacks
respond to cybersecurity attacks.
generally involve multiple systems
To circumvent challenges, EDR
and other infrastructure components.
When combined with organization and NDR solutions help identify
In-scope data sources require periodic
profiling, unique risk identification is abnormalities and build the IoCs
review and re-scoping throughout the
possible and can provide valuable necessary to locate affected systems
IR lifecycle.
assistance to the investigation to find and infrastructure components.
in-scope compromised or affected
infrastructure components.
Response tips
• Learn how the incident was detected to help • Search for common vectors, such as phishing (or
investigators triage the incident and scope targeted phishing) emails that lure recipients to execute
the response malicious software
• Identify “patient zero” and determine how the • Deploy EDR and NDR solutions to aid
adversary gained access to the organization’s incident response
network infrastructure
26 2020-2021 Cyber-Espionage Report

The sweetener:
Honeypots, honeytokens, honeynets
A honeypot is a system, or several Once the maturity requirements are You can extend the simple document
networked systems, that waits for fulfilled, the next step is to start small and honeytoken approach to a system
unsolicited requests. More specifically, and scale up gradually. Similar to honeypot, such as a file server hosting
honeypots observe unsolicited building an SIEM infrastructure, it is the document. This allows security
activity, attract possible threat best to deploy deception solutions administrators to detect an intrusion
actors and document their methods. based on use cases. Start with a high- before the adversary reaches the
Honeypots are effective for discovering risk scenario you want to address and honeytoken document. Again, the
opportunistic attacks, large-scale build from there. system must pose as a standard file
probes or computer worms, brute server to lure the adversary.
force authentication, misconfiguration, The scenario can be based on either risk
vulnerability exploits and web analysis or real incidents. When using If we extend this concept, we reach the
application attacks. real incident scenarios, it is important to honeynet level, a network of honeypots.
leverage cyber threat intelligence.
Information security researchers
use honeypot technologies for Start with your top identified Cyber-
counterespionage attacks because Espionage risk. Determine how
they can mimic the organization’s the sensitive data is stored (digital
production environment but with fake documents, database), where it is
believable data as bait. stored (file server, database server, web
application) and what the data looks like.
The purpose of honeypot technology
isn’t only to detect a threat actor, but If sensitive data is stored in documents,
to also: for instance, create realistic documents
with fake data. Then consider using a
• Slow down the threat actor honeytoken with a canary value that, if
used, will trigger a security alert.
• Lure threat actors away from
sensitive data
A honeytoken can be as simple as
• Collect information on the threat an unused official email address, a
actor link to an unused server, specific
keywords or records. If a honeytoken
• Gain visibility into gaps in
is used, it should trigger an alert in
perimeter defenses
the security-monitoring infrastructure.
Honeypot technology requires the Honeytokens can also be extended
organization to have fundamental to other components such as specific
information security controls already database records or invalid or unused
in place. To reach this higher maturity user accounts.
level, organizations should:
Some organizations have gone further
• Identify crown jewels that the threat by intentionally using administrative
actor would potentially seek account names such as “administrator”
or “adm-yinzer” as honeytokens. These
• Enable monitoring, logging,
honeytokens can be made to appear
alerting and response processes in
even more enticing by associating
associated infrastructure
them with critical servers such as
• Integrate information security domain controllers using “DC” in the
infrastructure components system name.
• Train employees on
incident response
• Segment the network and be able to
redirect traffic easily, if needed
2277 22002200--22002211 CCyybbeerr--EEssppiioonnaaggee RReeppoorrtt

Actions
however, the order in which they appear differs. For Cyber-
Threat actions
Espionage breaches, the top Actions are Malware (90%),
Social (83%) and Hacking (80%). For all breaches, the top
Actions are measures that threat actors take to cause or
Actions are Hacking (56%), Malware (39%) and Social (29%).
contribute to an incident. They answer the question,
“What tactics (actions) were used to affect an asset?”
This implies more of a reliance on Malware and Social Actions
for Cyber-Espionage threat actors than for all breach Actions.
For the 2014-2020 DBIR timeframe, the top three Actions
align for Cyber-Espionage breaches and all breaches;
| 0% 20%  | 40% | 60% | 80% 100% | 0% 20%  | 40% | 60% | 80% 100% |
| ------- | --- | --- | -------- | ------- | --- | --- | -------- |
| Malware |     |     |          | Hacking |     |     |          |
|         |     |     | 90%      |         |     | 56% |          |
| Social  |     |     |          | Malware |     |     |          |
|         |     |     | 83%      |         | 39% |     |          |
| Hacking |     |     |          | Social  |     |     |          |
|         |     |     | 80%      |         | 29% |     |          |
| Misuse  |     |     |          | Error   |     |     |          |
2% 16%
| Physical      |     |     |     | Misuse        |     |     |     |
| ------------- | --- | --- | --- | ------------- | --- | --- | --- |
| 0%            |     |     |     | 11%           |     |     |     |
| Error         |     |     |     | Physical      |     |     |     |
| 0%            |     |     |     | 6%            |     |     |     |
| Environmental |     |     |     | Environmental |     |     |     |
| 0%            |     |     |     | 0%            |     |     |     |
Figure #39: Actions within Cyber-Espionage breaches   Figure #40: Actions within all breaches
| (2014-2020 DBIR; n=1,580) |     |     |     | (2014-2020 DBIR; n=16,090) |     |                                  |     |
| ------------------------- | --- | --- | --- | -------------------------- | --- | -------------------------------- | --- |
| 28                        |     |     |     |                            |     | 2020-2021 Cyber-Espionage Report |     |

Misuse
Top Misuse action varieties for all breaches during this
Misuse action varieties
same timeframe are somewhat similar to Cyber-Espionage
breaches. Privilege abuse (74%) and Data mishandling (21%)
Misuse action varieties use entrusted organizational resources
also top this category; however, Possession abuse (11%),
or privileges granted for any purpose or in any manner—
Unapproved hardware (7%) and Knowledge abuse (6%)
malicious or not—contrary to their original intentions.
occupy the next three positions for all breaches.
Within the limited data for Cyber-Espionage breaches for
the 2014-2020 DBIR timeframe, we find for Misuse action
varieties that Privilege abuse (59%) and Data mishandling
(32%) are far ahead of the three-way tie between Email
misuse (14%), Unapproved hardware (14%) and Unapproved
workaround (14%).
| 0% 20%           | 40% | 60% | 80% 100% | 0% 20%           | 40% | 60% | 80% 100% |
| ---------------- | --- | --- | -------- | ---------------- | --- | --- | -------- |
| Privilege abuse  |     |     |          | Privilege abuse  |     |     |          |
|                  |     | 59% |          |                  |     |     | 74%      |
| Data mishandling |     |     |          | Data mishandling |     |     |          |
|                  | 32% |     |          | 21%              |     |     |          |
| Email misuse     |     |     |          | Possession abuse |     |     |          |
14% 11%
| Unapproved hardware |     |     |     | Unapproved hardware |     |     |     |
| ------------------- | --- | --- | --- | ------------------- | --- | --- | --- |
14% 7%
| Unapproved workaround  |     |     |     | Knowledge abuse |     |     |     |
| ---------------------- | --- | --- | --- | --------------- | --- | --- | --- |
14% 6%
| Knowledge abuse |     |     |     | Unapproved workaround |     |     |     |
| --------------- | --- | --- | --- | --------------------- | --- | --- | --- |
| 11%             |     |     |     | 5%                    |     |     |     |
Figure #41: Top Misuse action varieties within   Figure #42: Top Misuse action varieties within all breaches
Cyber-Espionage breaches (2014-2020 DBIR; n=37) (2014-2020 DBIR; n=1,769)
| 29  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Social
Social action varieties
Top controls
Social action varieties employ tactics, such as deception, manipulation and
intimidation, to exploit the human users of information assets. • CSC-17: Implement a
Security Awareness and
For Cyber-Espionage breaches during the 2014-2020 DBIR timeframe, the top Training Program
Social action variety by far is Phishing (97%), with Pretexting (2%) and Bribery (1%)
• CSC-19: Incident Response
as a distant second and third, respectively.
and Management
For all breaches during this same timeframe, the top Social action varieties mirror • CSC-20: Penetration Tests
Cyber-Espionage breaches, with a slightly lower percentage for Phishing (87%) and and Red Team Exercises
slightly higher percentages for Pretexting (9%) and Bribery (3%).
0% 20% 40% 60% 80% 100%
Phishing
97%
Pretexting
2%
Bribery
1%
Figure #43: Top Social action varieties within Cyber-Espionage breaches
(2014-2020 DBIR; n=1,191)
0% 20% 40% 60% 80% 100%
Phishing
87%
Pretexting
9%
Bribery
3%
Figure #44: Top Social action varieties within all breaches (2014-2020 DBIR; n=4,529)
30 2020-2021 Cyber-Espionage Report

Hacking
Hacking action varieties
Top controls
Hacking action varieties are all attempts to intentionally access or harm information
assets without (or exceeding) authorization by circumventing or thwarting logical • CSC-4: Controlled Use of
security mechanisms. Administrative Privileges
• CSC-6: Maintenance,
During the 2014-2020 DBIR timeframe, the top Hacking action varieties for Cyber-
Monitoring and Analysis of
Espionage breaches are Use of backdoor or C2 (86%), Use of stolen creds (30%),
Audit Logs
Brute force (12%) and Exploit vuln (9%).
• CSC-12: Boundary Defense
During this same timeframe, for all breaches, the top four Hacking action varieties
• CSC-16: Account Monitoring
align with the Cyber-Espionage breaches, albeit in a different order of primacy:
and Control
Use of stolen creds (63%), Use of backdoor or C2 (39%), Brute force (18%) and
Exploit vuln (9%). • CSC-19: Incident Response
and Management
Of the four top Hacking action varieties, Cyber-Espionage breaches rely more
• CSC-20: Penetration Tests
heavily on the sneakier Use of backdoor or C2, whereas all breaches rely
and Red Team Exercises
extensively on the matter-of-fact Use of stolen creds.
0% 20% 40% 60% 80% 100%
Use of backdoor or C2
86%
Use of stolen creds
30%
Brute force
12%
Exploit vuln
9%
Footprinting
5%
Figure #45: Top Hacking action varieties within Cyber-Espionage breaches
(2014-2020 DBIR; n=1,032)
0% 20% 40% 60% 80% 100%
Use of stolen creds
63%
Use of backdoor or C2
39%
Brute force
18%
Exploit vuln
9%
SQLi
5%
Figure #46: Top Hacking action varieties within all breaches (2014-2020 DBIR; n=6,581)
31 2020-2021 Cyber-Espionage Report

Malware
During the same timeframe, the top Malware action varieties
Malware action varieties
for all breaches group together more closely: C2 (48%),
Export data (42%), Spyware/Keylogger (40%), RAM scraper
Malware actions are any malicious software, script or code
(35%) and Backdoor (25%).
that runs on a device to alter its state or function without the
owner’s informed consent.
For top Malware action varieties, Cyber-Espionage threat
actors place significant value in Backdoor and C2, while all
For Cyber-Espionage breaches during the 2014-2020 DBIR
breach threat actors similarly place value in C2, but tend to
timeframe, we see Cyber-Espionage threat actors place
also favor Export data, Spyware/Keylogger and RAM scraper.
significantly more value on the top two Malware action
varieties, Backdoor (78%) and C2 (77%), than the next four
Malware action varieties: Downloader (40%), Capture stored
data (40%), Spyware/Keylogger (33%) and Export data (32%).
| 0% 20%   | 40% | 60% | 80% 100% | 0% 20%      | 40% | 60% | 80% 100% |
| -------- | --- | --- | -------- | ----------- | --- | --- | -------- |
| Backdoor |     |     |          | C2          |     |     |          |
|          |     |     | 78%      |             | 48% |     |          |
| C2       |     |     |          | Export data |     |     |          |
77%
42%
| Downloader |     |     |     | Spyware/Keylogger |     |     |     |
| ---------- | --- | --- | --- | ----------------- | --- | --- | --- |
|            | 40% |     |     |                   | 40% |     |     |
Capture stored data
RAM scraper
|                   | 40% |     |     |                     | 35% |     |     |
| ----------------- | --- | --- | --- | ------------------- | --- | --- | --- |
| Spyware/Keylogger |     |     |     | Backdoor            |     |     |     |
|                   | 33% |     |     | 25%                 |     |     |     |
| Export data       |     |     |     | Downloader          |     |     |     |
|                   | 32% |     |     | 10%                 |     |     |     |
| Password dumper   |     |     |     | Password dumper     |     |     |     |
| 22%               |     |     |     | 10%                 |     |     |     |
| Exploit vuln      |     |     |     | Capture stored data |     |     |     |
| 21%               |     |     |     | 9%                  |     |     |     |
| Adminware         |     |     |     | Adminware           |     |     |     |
| 21%               |     |     |     | 7%                  |     |     |     |
| Scan network      |     |     |     | Capture app data    |     |     |     |
18% 6%
| Disable controls |     |     |     | Scan network     |     |     |     |
| ---------------- | --- | --- | --- | ---------------- | --- | --- | --- |
| 13%              |     |     |     | 6%               |     |     |     |
| Rootkit          |     |     |     | Exploit vuln     |     |     |     |
| 11%              |     |     |     | 4%               |     |     |     |
| Brute force      |     |     |     | Ransomware       |     |     |     |
| 10%              |     |     |     | 3%               |     |     |     |
| Packet sniffer   |     |     |     | Disable controls |     |     |     |
| 7%               |     |     |     | 3%               |     |     |     |
Rootkit
RAM scraper
| 6%  |     |     |     | 3%  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
Figure #47: Top Malware action varieties within   Figure #48: Top Malware action varieties within all breaches
Cyber-Espionage breaches (2014-2020 DBIR; n=1,005) (2014-2020 DBIR; n=5,298)
Top controls
•  CSC-6: Maintenance, Monitoring and Analysis   •  CSC-13: Data Protection
of Audit Logs
•  CSC-19: Incident Response and Management
•  CSC-8: Malware Defenses
•  CSC-20: Penetration Tests and Red Team Exercises
•  CSC-12: Boundary Defense
| 32  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

In both Cyber-Espionage breaches and all breaches, threat
Malware vector varieties actors rely on Email attachments and Email links for malware
delivery. However, Web drive-by and Download by malware are
For Cyber-Espionage breaches during the 2014-2020
next on the list for Cyber-Espionage breaches, while Direct
DBIR timeframe, the top Malware vector varieties are Email
install is next for all breaches. For Download by malware and
attachment (67%), Email link (17%), Web drive-by (11%) and
Direct install, this implies that threat actors have already gained
Download by malware (11%).
access to the asset or environment.
For all breaches during the same timeframe, the top Malware
vector varieties are Email attachment (43%), Direct install
(39%) and Email link (9%).
| 0% 20%           | 40% | 60% | 80% 100% | 0% 20%           | 40% | 60% | 80% 100% |
| ---------------- | --- | --- | -------- | ---------------- | --- | --- | -------- |
| Email attachment |     |     |          | Email attachment |     |     |          |
|                  |     |     | 67%      |                  | 43% |     |          |
| Email link       |     |     |          | Direct install   |     |     |          |
17% 39%
| Web drive-by        |     |     |     | Email link          |     |     |     |
| ------------------- | --- | --- | --- | ------------------- | --- | --- | --- |
| 11%                 |     |     |     | 9%                  |     |     |     |
| Download by malware |     |     |     | Download by malware |     |     |     |
| 11%                 |     |     |     | 5%                  |     |     |     |
| Direct install      |     |     |     | Web drive-by        |     |     |     |
| 6%                  |     |     |     | 4%                  |     |     |     |
| Web download        |     |     |     | Remote injection    |     |     |     |
| 2%                  |     |     |     | 3%                  |     |     |     |
Figure #49: Top Malware vector varieties within   Figure #50: Top Malware vector varieties within all breaches
Cyber-Espionage breaches (2014-2020 DBIR; n=1,212) (2014-2020 DBIR; n=5,252)
Top controls
•  CSC-4: Controlled Use of Administrative Privileges •  CSC-17: Implement a Security Awareness and Training
Program
•  CSC-6: Maintenance, Monitoring and Analysis
| of Audit Logs |     |     |     | •  CSC-19: Incident Response and Management |     |     |     |
| ------------- | --- | --- | --- | ------------------------------------------- | --- | --- | --- |
•  CSC-8: Malware Defenses •  CSC-20: Penetration Tests and Red Team Exercises
•  CSC-12: Boundary Defense
| 33  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Deeper dive—Action varieties
For this deeper dive into Action varieties, we filtered the DBIR For this same timeframe, the Use of stolen creds (47%)
dataset for External actors and for Espionage and Financial topped the list of Action varieties by External actor with
motives within breaches. Financial motive. The next six Action varieties are closely
grouped: Phishing (33%), Export data (30%), C2 (28%),
During the 2014-2020 DBIR timeframe, the top four Action RAM scraper (28%), Spyware/Keylogger (27%) and Use
varieties by External actor with Espionage motive within of backdoor or C2 (26%).
breaches are Phishing (81%), Use of backdoor or C2 (60%),
Backdoor (54%) and C2 (53%). Capture stored data (27%) This close grouping of Action varieties implies that threat
and Downloader (27%) are tied for a distant fifth. actors with Financial motive use a greater variety of options
than those with Espionage motive to attain their objectives.
This high percentage across four Action varieties (which can
be simplified further into Phishing, Backdoor and C2) implies
that these are the primary go-to choices for threat actors with
Espionage motive.
0% 20% 40% 60% 80% 100%
Phishing 81%
Use of backdoor or C2 60%
Backdoor 54%
C2 53%
Capture stored data 27%
Downloader 27%
Spyware/Keylogger 23%
Export data 21%
Use of stolen creds 21%
Exploit vuln 19%
Password dumper 14%
Adminware 14%
Scan network 12%
Disable controls 9%
Brute force 8%
Figure #51: Top Action varieties by External actor and Espionage motive within breaches (2014-2020 DBIR; n=1,422)
0% 20% 40% 60% 80% 100%
Use of stolen creds 47%
Phishing 33%
Export Data 30%
C2 28%
RAM scraper 28%
Spyware/Keylogger 27%
Use of backdor or C2 26%
Brute force 16%
Backdoor 7%
Skimmer 6%
Pretexting 6%
Theft 5%
Capture app data 4%
Exploit vuln 4%
Password dumper 3%
Figure #52: Top Action varieties by External actor and Financial motive within breaches (2014-2020 DBIR; n=6,436)
34 2020-2021 Cyber-Espionage Report

Deeper dive—Action vectors
For a look into Action vectors, we filtered the dataset for For threat actors with Financial motive during this same
External actors and for Espionage and Financial motives timeframe, the top Action vectors are Web application (44%),
within breaches. Email (41%), Direct install (31%), Backdoor or C2 (28%) and
Email attachment (24%).
The top three Action vectors by External actor and Espionage
motive during the 2014-2020 DBIR timeframe are Email Compared to threat actors with Espionage motive, these
(84%), Email attachment (60%) and Backdoor or C2 (60%). Action vectors are much more varied, implying that threat
actors with Financial motive prefer to use a larger selection
Much like the Action varieties above, this high percentage of Action vectors to accomplish their objectives.
over three Action vectors implies that they are the primary
go-to choices for threat actors with Espionage motive.
0% 20% 40% 60% 80% 100%
Email 84%
Email attachment 60%
Backdoor or C2 60%
Email link 15%
Web drive-by 9%
Download by malware 9%
Direct install 4%
Desktop sharing 3%
Website 3%
Web application 3%
Figure #53: Top Action vectors by External actor and Espionage motive within breaches (2014-2020 DBIR; n=1,348)
0% 20% 40% 60% 80% 100%
Web application 44%
Email 41%
Direct install 31%
Backdoor or C2 28%
Email attachment 24%
Desktop sharing software 19%
3rd party desktop 13%
Partner 9%
Desktop sharing 5%
Victim grounds 3%
Figure #54: Top Action vectors by External actor and Financial motive within breaches (2014-2020 DBIR; n=5,969)
35 2020-2021 Cyber-Espionage Report

MITRE ATT&CK®
framework aspects
MITRE ATT&CK® is a globally accessible • How did the adversary escalate
knowledge base of adversary tactics privileges? (e.g., account bypass,
and techniques based on real-world Dynamic Link Library hijacking,
observations. In the 2020 DBIR, we vulnerability exploitation,
mapped VERIS (threat actions) to process injection)
MITRE ATT&CK.® If your organization
• Were there any indications of lateral
uses MITRE ATT&CK,® here are some
movement? (e.g., remote service
questions to ask:
exploitation, local admin account
log-ons, pass the hash vs. pass the
• How was “initial access” gained? (e.g.,
ticket, network sniffing)
known vulnerability exploitation, drive-
by download, phishing attack vector, • How did C2 servers access the
compromised credential access) environment? (e.g., unknown or
unexpected traffic or http, https, ftp,
• How was “persistence” achieved?
etc.; data encoding or obfuscation;
(e.g., new accounts, hooking, startup
domain fronting; uncommon ports)
item, registry run keys, batch jobs,
scheduled tasks)
EDR and NDR technologies
Using an EDR solution during a NDR deployments give investigators
Cyber-Espionage investigation can access to large amounts of data, which
significantly increase the effectiveness they can index for rapid searches to
of the investigation. This technology identify anomalies. This can lead to the
can provide much needed visibility discovery of other unidentified, infected
into understanding adversary infrastructure components and help
TTPs, monitoring lateral movement, build up the IoCs needed to find more
identifying persistence mechanisms impacted and compromised systems.
and expediting the return to normal
business operations. EDR and NDR solutions can be efficient
toolsets for organizations to leverage
EDR technology can accelerate the during an incident and hasten the return
speed of the investigation by utilizing to normal business operation.
behavioral detection tactics combined
with IoC-based searches (in near real
time) within the infrastructure, leading
to further identification of compromised
or affected system components.
Network traffic can provide keen insight
into threat actors’ breach defenses and
impact assets and data. Utilizing NDR
solutions gives organizations in-depth
visibility into the network, which helps
network forensics investigators gain
insights into packet-level activities.
Such insight helps investigators identify
new IoCs using behavioral analysis and
heuristics techniques.
3366 22002200--22002211 CCyybbeerr--EEssppiioonnaaggee RReeppoorrtt

The way forward
07
NIST CSF Recover
Assemble feedback and countermeasure solutions in an action
Develop and implement appropriate activities to maintain
plan to update the IR Plan, determine additional IR resource
plans for resilience and to restore any capabilities or services
requirements and identify internal IR stakeholder and tactical
that were impaired due to a cybersecurity incident.
responder training needs. Ensure that an organization’s IR
lifecycle includes an explicit provision directing continual
maturation via the after action-review process.
After-action reviews (a.k.a. postmortem sessions) should
be completed as part of any IR effort. This is particularly
important for the closeout of more advanced IR efforts, such
as those focused on Cyber-Espionage attacks.
Recovery tips
Complete the review by conducting a lessons-learned
• Complete a postmortem review of any IR actions
discussion, noting participant feedback (e.g., what went well,
what went not so well and what can be improved upon in the • Develop a post-incident action plan to incorporate
next session). lessons learned
• Ensure that the after action-review process becomes
part of the organization’s maturation process
37 2020-2021 Cyber-Espionage Report

Takeaways
Victim impact Actor activities
Timelines. For Cyber-Espionage breaches, Time to Discovery. Top Discovery methods for Cyber-Espionage
Compromise was seconds to days (91%), Time to Exfiltration breaches were Suspicious traffic (48%), Antivirus (23%) and
was minutes to weeks (88%), Time to Discovery was months Emergency response team (7%).
to years (69%) and Time to Containment was days to
months (79%). For all breaches, top Discovery methods were Law enforcement
(28%), Fraud detection (19%) and Customer (15%).
For all breaches, Time to Compromise was seconds to minutes
(85%), Time to Exfiltration was seconds to days (89%), Time to Actors. For Cyber-Espionage breaches, top Actor varieties
Discovery was days to months (75%) and Time to Containment were State-affiliated (85%), Nation-state (8%) and Organized
was hours to weeks (76%). crime (4%).
Patterns. Among the nine DBIR Incident Classification For all breaches, top Actor varieties were Organized crime
Patterns, Cyber-Espionage ranked sixth (10%). (59%), State-affiliated (13%) and Unaffiliated (7%).
Industries. For Cyber-Espionage breaches, Public (31%), Motives. Within all breaches, Actor motives were Financial
Manufacturing (22%) and Professional (11%) were most (76%), Espionage (18%) and “The Rest” (6%).
common. Manufacturing (35%), Mining + Utilities (23%) and
Actions. Top Actions for Cyber-Espionage breaches were
Public (23%) were most common by percent within breaches.
Malware (90%), Social (83%) and Hacking (80%).
Attribute varieties. For Cyber-Espionage breaches, top
For all breaches, top Actions were Hacking (56%), Malware
Attribute varieties, Software installation (Integrity) (91%), Alter
(39%) and Social (29%).
behavior (Integrity) (84%), Secrets (Confidentiality) (73%),
Internal (Confidentiality) (29%), Credentials (Confidentiality)
Action varieties. Phishing (81%), Use of Backdoor | C2 (53%
(21%) and System (Confidentiality) (19%) were most impacted.
| 60%), Capture stored data (27%) and Downloader (27%)
were top Action varieties for External actors with Espionage
For all breaches, top Attribute varieties were Software
motive within breaches.
installation (Integrity) (43%), Alter behavior (Integrity) (32%),
Credentials (Confidentiality) (29%), Personal (Confidentiality)
For External actors with Financial motive, Use of stolen
(28%) and Payment (Confidentiality) (22%).
creds (47%), Phishing (33%) and Export data (30%) were top
Action varieties.
Asset varieties. For Cyber-Espionage breaches, top
compromised Asset varieties (2020 DBIR) were Desktop or
Action vectors. Email (84%), Email attachment (60%) and
laptop (88%), Mobile phone (14%) and Web application (10%).
Backdoor or C2 (60%) were top Action vector varieties for
External actors with Espionage motive within all breaches.
For all breaches (2020 DBIR), top compromised Asset
varieties were Web application (43%), Desktop or laptop (31%)
For External actors with Financial motive within all breaches,
and Mail (21%).
Use of stolen creds (47%), Phishing (33%) and Export data
(30%) were top Action vector varieties.
Data varieties. Top compromised Data varieties for Cyber-
Espionage breaches (2020 DBIR) were Credentials (56%),
Secrets (49%), Internal (12%) and Classified (7%).
Key Cyber-Espionage CIS Critical Security Controls
Personal (58%), Credentials (41%), Internal (17%) and Medical
CSC-4: Controlled Use of Administrative Privileges
(16%) topped compromised Data varieties for all breaches.
CSC-5: Secure Configuration for Hardware and Software
CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
CSC-8: Malware Defenses
CSC-12: Boundary Defense
CSC-13: Data Protection
CSC-14: Controlled Access Based on the Need to Know
CSC-16: Account Monitoring and Control
CSC-17: Implement a Security Awareness and Training Program
CSC-18: Application Software Security
CSC-19: Incident Response and Management
CSC-20: Penetration Tests and Red Team Exercises
38 2020-2021 Cyber-Espionage Report

Mappings
VERIS category CER key takeaways Top CIS Critical Security Controls
Timelines Time to Compromise was seconds to days (91%), CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
Time to Exfiltration was minutes to weeks (88%), CSC-12: Boundary Defense
Time to Discovery was months to years (69%), CSC-16: Account Monitoring and Control
Time to Containment was days to months (79%) CSC-19: Incident Response and Management
CSC-20: Penetration Tests and Red Team Exercises
Discovery Suspicious traffic (48%), CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
Antivirus (23%), CSC-8: Malware Defenses
Emergency response team (7%) CSC-12: Boundary Defense
CSC-19: Incident Response and Management
Attribute varieties Software installation (Integrity) (91%), CSC-4: Controlled Use of Administrative Privileges
Alter behavior (Integrity) (84%), CSC-5: Secure Configuration for Hardware and Software
Secrets (Confidentiality) (73%), CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
Internal (Confidentiality) (29%), CSC-8: Malware Defenses
Credentials (Confidentiality) (21%), CSC-13: Data Protection
System (Confidentiality) (19%) CSC-16: Account Monitoring and Control
Asset varieties Desktop or laptop (User Device) (88%), CSC-5: Secure Configuration for Hardware and Software
(2020 DBIR) Mobile phone (User Device) (14%), CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
Web application (Server) (10%) CSC-17: Implement a Security Awareness and Training Program
CSC-18: Application Software Security
CSC-20: Penetration Tests and Red Team Exercises
Data varieties Credentials (56%), CSC-4: Controlled Use of Administrative Privileges
(2020 DBIR Secrets (49%), CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
Internal (12%) CSC-13: Data Protection
CSC-14: Controlled Access Based on the Need to Know
CSC-16: Account Monitoring and Control
CSC-17: Implement a Security Awareness and Training Program
Social varieties Phishing (97%), CSC-17: Implement a Security Awareness and Training Program
Pretexting (2%), CSC-19: Incident Response and Management
Bribery (1%) CSC-20: Penetration Tests and Red Team Exercises
Hacking varieties Use of backdoor or C2 (86%), CSC-4: Controlled Use of Administrative Privileges
Use of stolen creds (30%), CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
Brute force (12%) CSC-12: Boundary Defense
CSC-16: Account Monitoring and Control
CSC-19: Incident Response and Management
CSC-20: Penetration Tests and Red Team Exercises
Malware varieties Backdoor (78%), CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
C2 (77%), CSC-8: Malware Defenses
Downloader (40%), CSC-12: Boundary Defense
Capture stored data (40%) CSC-13: Data Protection
CSC-19: Incident Response and Management
CSC-20: Penetration Tests and Red Team Exercises
Malware vectors Email attachment (67%), CSC-4: Controlled Use of Administrative Privileges
Email link (17%), CSC-6: Maintenance, Monitoring and Analysis of Audit Logs
Web drive-by (11%), CSC-8: Malware Defenses
Download by malware (11%) CSC-17: Implement a Security Awareness and Training Program
CSC-19: Incident Response and Management
CSC-20: Penetration Tests and Red Team Exercises
Figure #55: Mapping VERIS categories to CER key takeaways to CIS top Critical Security Controls
39 2020-2021 Cyber-Espionage Report

Appendix A: Guides
08
VERIS framework
Hacking: Attempting to intentionally
Overview Threat actors access or harm information assets,
without (or exceeding) authorization,
Vocabulary for Event Recording Entities causing or contributing to an
by circumventing or thwarting logical
and Incident Sharing (VERIS) is a incident are referred to as threat actors.
security mechanisms
set of metrics designed to provide
a common language for describing External actors: External threats
Malware: Any malicious software, script
security incidents in a structured and originate from sources outside of
or code that runs on a device to alter
repeatable manner. the organization and its network of
its state or function without the owner’s
partners. Typically, no trust or privilege
informed consent
VERIS was crafted as a response to is implied for external entities.
one of the most critical and persistent
challenges in the security industry—a Internal actors: Internal threats
lack of quality information. originate from within the organization. Assets and attributes
Insiders are trusted and privileged
VERIS targets this problem by helping (some more than others). A compromised asset is one that
organizations to collect useful incident- suffers from any loss of confidentiality/
related information and to share Partner actors: Partners include any possession, integrity/authenticity or
it—anonymously and responsibly— third party that shares a business availability/utility (primary security
with others. The overall goal is to relationship with the organization. Some attributes of the expanded CIA Triad). An
lay a foundation from which we can level of trust and privilege is usually incident can involve multiple assets and
constructively and cooperatively learn implied between business partners and affect multiple attributes (each of which
from our experiences to better measure the organizations. contains different metrics) of those assets.
and manage risk.
Threat actions Additional resources
A4 threat model
Threat actors conduct threat actions Further information on VERIS can be
VERIS employs the A4 threat model, to cause or contribute to an incident. obtained from these resources:
which was developed originally by the VERIS uses seven primary categories
Verizon RISK Team (now known as for threat actions: Malware, Hacking, • DBIR facts, figures and data: github.
VTRAC). In the A4 threat model, an Social, Misuse, Physical, Error and com/vz-risk/dbir/tree/gh-pages/2020
incident is viewed as a series of events Environmental. For this report, we • VERIS framework: veriscommunity.net
that adversely affect the information focus on four: Misuse, Social, Hacking
assets of an organization. The A4 and Malware. • VERIS schema:
github.com/vz-risk/veris
threat model elements are:
Misuse: Using entrusted organizational
• VERIS Community Database (VCDB):
• Actors: Whose actions affected resources or privileges for any github.com/vz-risk/vcdb
the asset? purpose or manner contrary to that
which was intended
• Actions: What actions affected
the asset? Social: Employing tactics such as
• Assets: Which assets were affected? deception, manipulation and intimidation
to exploit the human element, or users,
• Attributes: How were assets affected?
of information assets
40 2020-2021 Cyber-Espionage Report

VIPR process
1
Planning
and
Overview
Preparation
|     |     | 6   | 2   |
| --- | --- | --- | --- |
Based in our previous proactive IR
|     |     | Assessment  | Detection  |
| --- | --- | ----------- | ---------- |
engagements, we’ve formulated a
|                                      |     | and        | and        |
| ------------------------------------ | --- | ---------- | ---------- |
| six-phase approach to investigative  |     | Adjustment | Validation |
response and IR readiness: the
Verizon Incident Preparedness and
Response (VIPR) process. VIPR
consists of six phases: (1) Planning
and Preparation, (2) Detection and
| Validation, (3) Containment and  |     | 5           | 3            |
| -------------------------------- | --- | ----------- | ------------ |
|                                  |     | Remedation  | Containment  |
Eradication, (4) Collection and Analysis,
|     |     | and  | and  |
| --- | --- | ---- | ---- |
(5) Remediation and Recovery, and (6)
|     |     | Recovery | Eradication |
| --- | --- | -------- | ----------- |
Assessment and Adjustment.
4
Collection
Further insight into these IR phases and  and
their corresponding sub-components  Analysis
can be found in the VIPR report:
enterprise.verizon.com/resources/
Figure #56: VIPR phases
reports/vipr/
| VIPR report key takeaways | Phase             | Key takeaway                               |     |
| ------------------------- | ----------------- | ------------------------------------------ | --- |
|                           | 1 – Planning and  | 1.  Construct a logical, efficient IR Plan |     |
Having an efficient and effective IR
Preparation
Plan is the key to successful incident  2.  Create IR playbooks for specific incidents
response. Capturing this efficiency and
3.  Periodically review, test and update the IR Plan
effectiveness is the ultimate purpose of
4.  Cite external and internal cybersecurity and incident response
our VIPR report.
governance and standards
The VIPR report is a data- and  5.  Define internal IR stakeholder roles and responsibilities
scenario-driven approach to incident
6.  Require internal IR stakeholders to periodically discuss the
preparedness and response. It’s
cybersecurity threat landscape
based on three years (2016-2018) of
our IR Plan assessment engagement  7.  Train and maintain skilled tactical responders
observations and recommendations,
8.  Periodically review third-party cybersecurity services and contact
as well as our data breach simulation
procedures
recommendations. Findings presented
|     | 2 – Detection and  | 9.  Define cybersecurity events (along with incidents) |     |
| --- | ------------------ | ------------------------------------------------------ | --- |
in the VIPR report culminated in 20
Validation
key takeaways. 10. Classify incidents by type and severity level
11.  Describe technical and non-technical incident detection sources
12. Specify incident and event-tracking mechanisms
13. Specify escalation and notification procedures
|     | 3 – Containment  | 14. Provide containment and eradication measures |     |
| --- | ---------------- | ------------------------------------------------ | --- |
and Eradication
4 – Collection and  15. Specify evidence collection and data analysis tools and procedures
Analysis
16. Specify evidence handling and submission procedures
|     | 5 – Remediation  | 17.  Provide remediation and recovery measures |     |
| --- | ---------------- | ---------------------------------------------- | --- |
and Recovery
|     | 6 – Assessment  | 18. Feed lessons-learned results back into the IR Plan |     |
| --- | --------------- | ------------------------------------------------------ | --- |
and Adjustment
19. Establish a data and document retention policy
20. Track incident and incident response metrics
Figure #57: VIPR report key takeaways
| 41  |     |     | 2020-2021 Cyber-Espionage Report |
| --- | --- | --- | -------------------------------- |

NIST Cybersecurity Framework
Overview Five functions
The NIST Cybersecurity Framework (CSF) is voluntary The five functions of the NIST CSF are as follows:
guidance based on existing standards, guidelines and
practices to help organizations better manage and reduce Identify. Develop an organizational understanding to
cybersecurity risk. In addition to helping organizations manage cybersecurity risk to systems, people, assets, data
manage and reduce risks, it was designed to foster risk and and capabilities.
cybersecurity management communications among both
Examples of outcome categories include Asset Management,
internal and external organizational stakeholders.
Business Environment, Governance, Risk Assessment and
nist.gov/cyberframework Risk Management Strategy.
Protect. Develop and implement appropriate safeguards to
ensure delivery of critical services.
er Id
v e
o n Examples of outcome categories include Identity Management
c t
e if and Access Control, Awareness and Training, Data
R y
Security, Information Protection Processes and Procedures,
Maintenance, and Protective Technology.
Framework Detect. Develop and implement appropriate activities to
R Version 1.2 t identify the occurrence of a cybersecurity event.
e c
s e
p o t Examples of outcome categories include Anomalies and Events,
o r
n P Security, Continuous Monitoring, and Detection Processes.
d
Respond. Develop and implement appropriate activities to
take action regarding a detected cybersecurity incident.
Detect
Examples of outcome categories include Response Planning,
Communications, Analysis, Mitigation and Improvements.
Figure #58: NIST Cybersecurity Framework Recover. Develop and implement appropriate activities to
maintain plans for resilience and to restore any capabilities or
services that were impaired due to a cybersecurity incident.
The NIST CSF provides a common language for understanding,
Examples of outcome categories include Recovery Planning,
managing and expressing cybersecurity risk to internal and
Improvements and Communications.
external stakeholders. It can be used to help identify and
prioritize actions for reducing cybersecurity risk, and it is a tool
for aligning policy, business and technological approaches to
managing that risk. It can be used to manage cybersecurity risk
across entire organizations or it can be focused on the delivery
of critical services within an organization:
nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf
42 2020-2021 Cyber-Espionage Report

CIS Critical Security Controls
Overview Critical Security Controls
The Center for Internet Security (CIS) Critical Security
Controls (CSCs) are internationally recognized cybersecurity
best practices for defense against common threats. They are Type # Description
a consensus-developed resource that brings together expert Basic CSC-1 Inventory and Control of Hardware
insight on cyber threats, business technology and security. Assets
CSC-2 Inventory and Control of Software
Organizations with varying resources and risk exposure use
Assets
the CIS CSCs to build an effective cyber-defense program:
CSC-3 Continuous Vulnerability Management
cisecurity.org/controls/cis-controls-list/
CSC-4 Controlled Use of Administrative
Privileges
CSC-5 Secure Configuration for Hardware
DBIR Implementation and Software on Mobile Devices,
Laptops, Workstations and Servers
The 2020 DBIR best describes the implementation of
CSC-6 Maintenance, Monitoring and
CIS CSCs:
Analysis of Audit Logs
For those who are unacquainted with the CIS CSCs, they Foundational CSC-7 Email and Web Browser Protections
are a community-built, attacker-informed prioritized set
CSC-8 Malware Defenses
of cybersecurity guidelines that consist of 171 safeguards
organized into 20 higher-level controls. CSC-9 Limitation and Control of Network
Ports, Protocols and Services
One of the unique elements of the CIS CSCs is their focus on
CSC-10 Data Recovery Capabilities
helping organizations understand where to start their security
program. This prioritization is represented in two ways: CSC-11 Secure Configuration for Network
Devices, such as Firewalls, Routers
and Switches
• Through the ordering of the CSCs so that they allow a loose
prioritization (CSC-1: Inventory of Hardware is probably a CSC-12 Boundary Defense
better place to start than CSC-20: Penetration Testing)
CSC-13 Data Protection
• Introduced in version 7.150 is the concept of Implementation
CSC-14 Controlled Access Based on
Groups, in which the 171 safeguards are grouped, based on
the Need to Know
the resources and risks the organizations are facing. This
means that a smaller organization with fewer resources CSC-15 Wireless Access Control
(Implementation Group 1) shouldn’t be expected to CSC-16 Account Monitoring and Control
implement resource and process-intensive controls such as
Passive Asset Discovery even if it’s within CSC-1, while an
Organizational CSC-17 Implement a Security Awareness and
organization with more resources and/or a higher risk level
Training Program
may want to consider that control
CSC-18 Application Software Security
CSC-19 Incident Response and Management
CSC-20 Penetration Tests and Red Team
Exercises
Figure #59: CIS Critical Security Controls
43 2020-2021 Cyber-Espionage Report

Appendix B:
09
Industry dossiers
Educational Services
| NAICS   | 61 – Educational Services                        | Summary |     |     |     |
| ------- | ------------------------------------------------ | ------- | --- | --- | --- |
| Remarks | Unless otherwise stated, information covers the  |         |     |     |     |
Since 2014, confirmed data breaches with Espionage
2014-2020 DBIR timeframe. Also, note the change
motive made up about 8% of the breaches reported in the
in scale among figures.
Educational Services industry. In 2019, the percentage
All breaches was only 1%. While the percentage is low, this percentage
is somewhat driven down due to the very high rate of
| Frequency | 607 (2014-2020) | 228 (2020) |     |     |     |     |
| --------- | ---------------------------- | --- | --- | --- | --- |
Ransomware (80%) financially motivated breaches that
| Actors | External (69%), Internal (32%), Partner (2%),  |     |     |     |     |
| ------ | ---------------------------------------------- | --- | --- | --- | --- |
target this industry.
Multiple (2%)
Motives Financial (92%), Fun (5%), Convenience (3%),  Another consideration when looking at the numbers for the
Espionage (3%) Educational Industry is that Cyber-Espionage threat actors
are known to use ransomware to cover up data theft, and in
Cyber-Espionage breaches
many cases the threat actor succeeds in preventing analysts
Frequency 47 (8%) (2014-2020) from determining what if any data was exfiltrated from the
Actors External (100%) network. This is particularly true when the organization
doesn’t have sufficient logging in place to properly investigate.
| Actions | Social (91%), Hacking (91%), Malware (94%) |                      |        |     |     |
| ------- | ------------------------------------------ | -------------------- | ------ | --- | --- |
| Assets  | Person (96%), User Dev (73%), Server (7%)  |                      |        |     |     |
|         |                                            |                      | 0% 20% | 40% | 60% |
| Data    | Secrets (94%), Credentials (9%)            |                      |        |     |     |
|         |                                            | Everything Else      | 25%    |     |     |
|         |                                            | Miscellaneous Errors | 24%    |     |     |
Web Applications
23%
Crimeware 9%
|                                |                | Cyber-Espionage        | 8%  |     |     |
| ------------------------------ | -------------- | ---------------------- | --- | --- | --- |
|                                |                | Privilege Misuse       | 6%  |     |     |
| Cyber-Espionage breach dossier |                | Lost and Stolen Assets | 5%  |     |     |
|                                |                | Point of Sale          | 0%  |     |     |
| NAICS                          | All industries | Denial of Service      |     |     |     |
0%
|     |     | Payment Card Skimmers | 0%  |     |     |
| --- | --- | --------------------- | --- | --- | --- |
All breaches (2014-2020)
| Frequency  | 16,090 (2014-2020) | 3,950 (2020) |     |     |     |     |
| ---------- | --------------------------------- | --- | --- | --- | --- |
Figure #60: Breaches by pattern for Education
(2014-2020 DBIR; n=607)
| Actors | External (75%), Internal (26%), Multiple (2%),  |     |     |     |     |
| ------ | ----------------------------------------------- | --- | --- | --- | --- |
Partner (1%)
500
| Motives | Financial (76%), Espionage (18%), Fun (3%) |     |     |     |     |
| ------- | ------------------------------------------ | --- | --- | --- | --- |
400
Cyber-Espionage breaches (2014-2020)
300
| Frequency | 1,580 (2014-2020) |     |     |     |     |
| --------- | ----------------- | --- | --- | --- | --- |
200
| Actions | Malware (90%), Social (83%), Hacking (80%)         |           |           |      |      |
| ------- | -------------------------------------------------- | --------- | --------- | ---- | ---- |
| Assets  | Person (88%), User Dev (83%), Server (34%)         | 100       |           |      |      |
| Data    | Secrets (75%), Internal (20%), Credentials (22%),  | 0         |           |      |      |
|         | System (19%)                                       | 2015 2016 | 2017 2018 | 2019 | 2020 |
Cyber-Espionage breaches All breaches
Figure #61: Cyber-Espionage breaches within all breaches annually
for Education (2015-2020 DBIR)
| 44  |     |     | 2020-2021 Cyber-Espionage Report |     |     |
| --- | --- | --- | -------------------------------- | --- | --- |

| 0% 20%   | 40% 60% | 80% | 100% 0%  | 20% | 40% 60% | 80% | 100% |
| -------- | ------- | --- | -------- | --- | ------- | --- | ---- |
| External |         |     | External |     |         |     |      |
100%
69%
| Internal |     |     | Internal |     |     |     |     |
| -------- | --- | --- | -------- | --- | --- | --- | --- |
| 0%       |     |     |          |     | 32% |     |     |
| Partner  |     |     | Partner  |     |     |     |     |
| 0%       |     |     | 2%       |     |     |     |     |
| Multiple |     |     | Multiple |     |     |     |     |
| 0%       |     |     | 2%       |     |     |     |     |
Figure #62: Actors within Cyber-Espionage breaches for Education  Figure #63: Actors within all breaches for Education
| (2014-2020 DBIR; n=47) |         |         | (2014-2020 DBIR; n=598) |        |         |         |        |
| ---------------------- | ------- | ------- | ----------------------- | ------ | ------- | ------- | ------ |
| 100%                   |         |         | 100%                    |        |         |         |        |
| 50%                    |         |         | 50%                     |        |         |         |        |
| 0%                     |         |         |                         | 0%     |         |         |        |
| Social                 | Hacking | Malware | Misuse                  | Social | Hacking | Malware | Misuse |
Figure #64: Actions within Cyber-Espionage breaches for  Figure #65: Actions within all breaches for Education
| Education (2014-2020 DBIR; n=47) |     |     | (2014-2020 DBIR; n=592) |     |     |     |     |
| -------------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- |
| 100%                             |     |     | 100%                    |     |     |     |     |
| 50%                              |     |     | 50%                     |     |     |     |     |
| 0%                               |     |     | 0%                      |     |     |     |     |
Person User Dev Server Media Network Person User Dev Server Media Network
Figure #66: Assets within Cyber-Espionage breaches for Education  Figure #67: Assets within all breaches for Education
| (2014-2020 DBIR; n=45) |     |     | (2014-2020 DBIR; n=552) |     |     |     |     |
| ---------------------- | --- | --- | ----------------------- | --- | --- | --- | --- |
| 100%                   |     |     | 100%                    |     |     |     |     |
| 50%                    |     |     | 50%                     |     |     |     |     |
| 0%                     |     |     | 0%                      |     |     |     |     |
Credentials Internal Secrets Personal m Bank ment Medical Credentials Internal Secrets Personal m Bank ment Medical
|     |     | Syste |     |     |     | Syste |     |
| --- | --- | ----- | --- | --- | --- | ----- | --- |
|     |     | Pay   |     |     |     | Pay   |     |
Figure #68: Compromised Data varieties within Cyber-Espionage  Figure #69: Compromised Data varieties within all breaches
breaches for Education (2014-2020 DBIR; n=47) for Education (2014-2020 DBIR; n=507)
| 45  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Financial and Insurance
|         |                                                  |                  | 0% 10% 20% | 30% 40% | 50% 60% |
| ------- | ------------------------------------------------ | ---------------- | ---------- | ------- | ------- |
| NAICS   | 52 – Financial and Insurance                     |                  |            |         |         |
|         |                                                  | Web Applications |            |         | 58%     |
| Remarks | Unless otherwise stated, information covers the  |                  |            |         |         |
2014-2020 DBIR timeframe. Also, note the change  Payment Card Skimmers 12%
in scale among figures.
| All breaches |                                                | Miscellaneous Errors | 8%  |     |     |
| ------------ | ---------------------------------------------- | -------------------- | --- | --- | --- |
| Frequency    | 2,797 (2014-2020) | 448 (2020)                 | Privilege Misuse     | 8%  |     |     |
| Actors       | External (87%), Internal (14%), Partner (1%),  |                      | 7%  |     |     |
Everything Else
Multiple (2%)
|         |                                              | Crimeware       | 5%  |     |     |
| ------- | -------------------------------------------- | --------------- | --- | --- | --- |
| Motives | Financial (91%), Espionage (3%), Grudge (3%) |                 |     |     |     |
|         |                                              | Cyber-Espionage | 2%  |     |     |
Cyber-Espionage breaches
| Frequency | 42 (2%) (2014-2020) | Lost and Stolen Assets | 1%  |     |     |
| --------- | ------------------- | ---------------------- | --- | --- | --- |
Actors External (100%), Internal (2%), Partner (2%),  Point of Sale 0%
Multiple (5%)
|         |                                            | Denial of Service | 0%  |     |     |
| ------- | ------------------------------------------ | ----------------- | --- | --- | --- |
| Actions | Social (56%), Hacking (90%), Malware (85%) |                   |     |     |     |
| Assets  | Person (58%), User Dev (70%), Server (58%) |                   |     |     |     |
Figure #70: Breaches by pattern for Financial
Data Secrets (38%), Payment (31%), Internal (15%),  (2014-2020 DBIR; n=2,797)
Credentials (15%)
1000
Summary
800
The DBIR dataset pertaining to Cyber-Espionage in the
Financial and Insurance industry has seen some significant
changes in percentages. For the past seven years
600
(2014-2020 DBIR timeframe), Financial on average was
approximately 3%; however in the last three years, it made up
400
6.3% of Cyber-Espionage breaches. In 2018, there was
a significant increase where it reached 10.3%.
200
Remember, these numbers represent only reported breaches.
When the compromised data doesn’t fall within reporting
criteria, a private organization may choose not to disclose
0
a breach. This makes Cyber-Espionage breaches, which  2014 2015 2016 2017 2018 2019 2020
are already challenging to detect, even less likely to be
discovered and by extension, reported. There is no way to
|     |     | Cyber-Espionage breaches | All breaches  |     |     |
| --- | --- | ------------------------ | ------------- | --- | --- |
truly gauge the magnitude of Cyber-Espionage attacks,
especially in any of the private industries.
Figure #71: Cyber-Espionage breaches within all breaches annually
for Financial (2014-2020 DBIR)
| 46  |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | -------------------------------- | --- |

| 0% 20%   | 40% 60% | 80% | 100% 0%  | 20% | 40% 60% | 80% | 100% |
| -------- | ------- | --- | -------- | --- | ------- | --- | ---- |
| External |         |     | External |     |         |     |      |
|          |         |     | 100%     |     |         |     | 87%  |
| Internal |         |     | Internal |     |         |     |      |
| 2%       |         |     |          | 14% |         |     |      |
Partner
Partner
| 2%       |     |     | 1%       |     |     |     |     |
| -------- | --- | --- | -------- | --- | --- | --- | --- |
| Multiple |     |     | Multiple |     |     |     |     |
| 5%       |     |     |          | 2%  |     |     |     |
Figure #72: Actors within Cyber-Espionage breaches for Financial  Figure #73: Actors within all breaches for Financial
| (2014-2020 DBIR; n=42) |         |         | (2014-2020 DBIR; n=2,787) |        |         |         |        |
| ---------------------- | ------- | ------- | ------------------------- | ------ | ------- | ------- | ------ |
| 100%                   |         |         | 100%                      |        |         |         |        |
| 50%                    |         |         | 50%                       |        |         |         |        |
| 0%                     |         |         |                           | 0%     |         |         |        |
| Social                 | Hacking | Malware | Misuse                    | Social | Hacking | Malware | Misuse |
Figure #74: Actions within Cyber-Espionage breaches for Financial  Figure #75: Actions within all breaches for Financial
| (2014-2020 DBIR; n=41) |     |     | (2014-2020 DBIR; n=2,331) |     |     |     |     |
| ---------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
| 100%                   |     |     | 100%                      |     |     |     |     |
| 50%                    |     |     | 50%                       |     |     |     |     |
| 0%                     |     |     |                           | 0%  |     |     |     |
Person User Dev Server Media Network Person User Dev Server Media Network
Figure #76: Assets within Cyber-Espionage breaches for Financial  Figure #77: Assets within all breaches for Financial
| (2014-2020 DBIR; n=40) |     |     | (2014-2020 DBIR; n=2,238) |     |     |     |     |
| ---------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
| 100%                   |     |     | 100%                      |     |     |     |     |
| 50%                    |     |     | 50%                       |     |     |     |     |
| 0%                     |     |     | 0%                        |     |     |     |     |
Credentials Internal Secrets Personal m Bank ment Medical Credentials Internal Secrets Personal m Bank ment Medical
|     |     | Syste |     |     |     | Syste |     |
| --- | --- | ----- | --- | --- | --- | ----- | --- |
|     |     | Pay   |     |     |     | Pay   |     |
Figure #78: Compromised Data varieties within Cyber-Espionage  Figure #79: Compromised Data varieties within all breaches
breaches for Financial (2014-2020 DBIR; n=39) for Financial (2014-2020 DBIR; n=2,205)
| 47  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Information
|         |                                                  |                  | 0% 10% 20% | 30% 40% | 50% 60% |
| ------- | ------------------------------------------------ | ---------------- | ---------- | ------- | ------- |
| NAICS   | 51 – Information                                 |                  |            |         |         |
|         |                                                  | Web Applications |            |         | 42%     |
| Remarks | Unless otherwise stated, information covers the  |                  |            |         |         |
2014-2020 DBIR timeframe. Also, note the change  Miscellaneous Errors 26%
in scale among figures.
| All breaches |                                | Everything Else | 15% |     |     |
| ------------ | ------------------------------ | --------------- | --- | --- | --- |
| Frequency    | 1,043 (2014-2020) | 360 (2020) | Cyber-Espionage | 7%  |     |     |
Actors External (70%), Internal (30%), Partner (2%),  Privilege Misuse 6%
Multiple (2%)
|         |                                              | Crimeware              | 4%  |     |     |
| ------- | -------------------------------------------- | ---------------------- | --- | --- | --- |
| Motives | Financial (88%), Espionage (7%), Fun (2%),   |                        |     |     |     |
|         | Grudge (2%)                                  | Lost and Stolen Assets | 1%  |     |     |
Cyber-Espionage breaches
|           |                                               | Point of Sale         | 0%  |     |     |
| --------- | --------------------------------------------- | --------------------- | --- | --- | --- |
| Frequency | 72 (7%) (2014-2020)                           |                       |     |     |     |
|           |                                               | Denial of Service     | 0%  |     |     |
| Actors    | External (100%), Internal (4%), Multiple (4%) |                       |     |     |     |
|           |                                               | Payment Card Skimmers | 0%  |     |     |
| Actions   | Social (59%), Hacking (78%), Malware (67%)    |                       |     |     |     |
| Assets    | Person (61%), User Dev (61%), Server (48%)    |                       |     |     |     |
Figure #80: Breaches by pattern for Information
Data Secrets (70%), Credentials (30%), Internal (13%) (2014-2020 DBIR; n=1,043)
500
Summary
The Information industry reported the fourth-highest amount
400
of Cyber-Espionage-motivated data breaches during the
2014-2020 DBIR timeframe. Information is a vast industry,
which encompasses all organizations involved in the creation,
300
storage or transmission of information.
| The bread-and-butter motivation for Information industry  |     | 200 |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- |
data breaches is Financial; however, we have still seen 7% of
breaches with a Cyber-Espionage motive.
100
An important factor for breaches in the Information industry
is that since 2019, there has been a significant increase in
0
web applications attacks, which are leveraging both stolen  2014 2015 2016 2017 2018 2019 2020
credentials and vulnerability exploitation. Misconfiguration
errors were a main contributing factor to breaches in the
|     |     | Cyber-Espionage breaches | All breaches  |     |     |
| --- | --- | ------------------------ | ------------- | --- | --- |
Information industry.
Figure #81: Cyber-Espionage breaches within all breaches annually
for Information (2014-2020 DBIR)
| 48  |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | -------------------------------- | --- |

| 0% 20%   | 40% 60% | 80% | 100% 0%  | 20% | 40% 60% | 80% | 100% |
| -------- | ------- | --- | -------- | --- | ------- | --- | ---- |
| External |         |     | External |     |         |     |      |
|          |         |     | 100%     |     |         | 70% |      |
| Internal |         |     | Internal |     |         |     |      |
| 4%       |         |     |          |     | 30%     |     |      |
| Partner  |         |     | Partner  |     |         |     |      |
| 0%       |         |     |          | 2%  |         |     |      |
| Multiple |         |     | Multiple |     |         |     |      |
| 4%       |         |     |          | 2%  |         |     |      |
Figure #82: Actors within Cyber-Espionage breaches for  Figure #83: Actors within all breaches for Information
| Information (2014-2020 DBIR; n=72) |         |         | (2014-2020 DBIR; n=1,036) |        |         |         |        |
| ---------------------------------- | ------- | ------- | ------------------------- | ------ | ------- | ------- | ------ |
| 100%                               |         |         | 100%                      |        |         |         |        |
| 50%                                |         |         | 50%                       |        |         |         |        |
| 0%                                 |         |         |                           | 0%     |         |         |        |
| Social                             | Hacking | Malware | Misuse                    | Social | Hacking | Malware | Misuse |
Figure #84: Actions within Cyber-Espionage breaches   Figure #85: Actions within all breaches for Information
for Information (2014-2020 DBIR; n=63) (2014-2020 DBIR; n=1,013)
| 100% |     |     | 100% |     |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
| 50%  |     |     | 50%  |     |     |     |     |
| 0%   |     |     |      | 0%  |     |     |     |
Person User Dev Server Media Network Person User Dev Server Media Network
Figure #86: Assets within Cyber-Espionage breaches for  Figure #87: Assets within all breaches for Information
| Information (2014-2020 DBIR; n=61) |     |     | (2014-2020 DBIR; n=937) |     |     |     |     |
| ---------------------------------- | --- | --- | ----------------------- | --- | --- | --- | --- |
| 100%                               |     |     | 100%                    |     |     |     |     |
| 50%                                |     |     | 50%                     |     |     |     |     |
| 0%                                 |     |     | 0%                      |     |     |     |     |
Credentials Internal Secrets Personal m Bank ment Medical Credentials Internal Secrets Personal m Bank ment Medical
|     |     | Syste |     |     |     | Syste |     |
| --- | --- | ----- | --- | --- | --- | ----- | --- |
|     |     | Pay   |     |     |     | Pay   |     |
Figure #88: Compromised Data varieties within Cyber-Espionage  Figure #89: Compromised Data varieties within all breaches
breaches for Information (2014-2020 DBIR; n=61) for Information (2014-2020 DBIR; n=806)
| 49  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Manufacturing
|         |                                                  |                 | 0% 10% 20% | 30% 40% | 50% 60% |
| ------- | ------------------------------------------------ | --------------- | ---------- | ------- | ------- |
| NAICS   | 31-33 – Manufacturing                            |                 |            |         |         |
|         |                                                  | Cyber-Espionage |            | 35%     |         |
| Remarks | Unless otherwise stated, information covers the  |                 |            |         |         |
2014-2020 DBIR timeframe. Also, note the change  Crimeware 20%
in scale among figures.
| All breaches |                              | Web Applications | 16% |     |     |
| ------------ | ---------------------------- | ---------------- | --- | --- | --- |
| Frequency    | 985 (2014-2020) | 381 (2020) | Privilege Misuse | 11% |     |     |
Actors External (84%), Internal (17%), Partner (1%),  Everything Else 9%
Multiple (1%)
|         |                                  | Miscellaneous Errors   | 7%  |     |     |
| ------- | -------------------------------- | ---------------------- | --- | --- | --- |
| Motives | Financial (73%), Espionage (27%) |                        |     |     |     |
|         |                                  | Lost and Stolen Assets | 3%  |     |     |
Cyber-Espionage breaches
| Frequency | 344 (35%) (2014-2020) | Point of Sale | 0%  |     |     |
| --------- | --------------------- | ------------- | --- | --- | --- |
Actors External (100%), Internal (1%), Multiple (1%) Payment Card Skimmers  0%
Actions Social (85%), Hacking (58%), Malware (84%) Denial of Service 0%
| Assets | Person (86%), User Dev (73%), Server (13%) |     |     |     |     |
| ------ | ------------------------------------------ | --- | --- | --- | --- |
Data Secrets (85%), Credentials (21%), Internal (2%) Figure #90: Breaches by pattern for Manufacturing
(2014-2020 DBIR; n=985)
Summary
500
In 2019, the Manufacturing industry had the largest number
of Cyber-Espionage-motivated breaches compared to other
400
industries. Overall between 2014 and 2020, it’s ranked as
the second-highest-hit industry at nearly 22% of all reported
Cyber-Espionage breaches.
300
In 2018, we noted a significant drop in reported Cyber-
| Espionage breaches in the Manufacturing industry. However,  | 200 |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- |
we believe this was due in part to a change that year in DBIR
contributors who typically provide specific metrics around
| Cyber-Espionage breaches in Manufacturing. | 100 |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- |
Cyber-Espionage threat actors primarily target Secrets and—
0
like all other industries—Credentials as a means to acquire  2014 2015 2016 2017 2018 2019 2020
these Secrets.
|     |     | Cyber-Espionage breaches | All breaches  |     |     |
| --- | --- | ------------------------ | ------------- | --- | --- |
Figure #91: Cyber-Espionage breaches within all breaches annually
for Manufacturing (2014-2020 DBIR)
| 50  |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | -------------------------------- | --- |

| 0% 20%   | 40% 60% | 80% | 100% 0%  | 20% | 40% 60% | 80% | 100% |
| -------- | ------- | --- | -------- | --- | ------- | --- | ---- |
| External |         |     | External |     |         |     |      |
|          |         |     | 100%     |     |         | 84% |      |
| Internal |         |     | Internal |     |         |     |      |
| 1%       |         |     |          | 17% |         |     |      |
| Partner  |         |     | Partner  |     |         |     |      |
| 0%       |         |     |          | 1%  |         |     |      |
| Multiple |         |     | Multiple |     |         |     |      |
| 1%       |         |     |          | 1%  |         |     |      |
Figure #92: Actors within Cyber-Espionage breaches   Figure #93: Actors within all breaches for Manufacturing
for Manufacturing (2014-2020 DBIR; n=344) (2014-2020 DBIR; n=977)
| 100%   |         |         | 100%   |        |         |         |        |
| ------ | ------- | ------- | ------ | ------ | ------- | ------- | ------ |
| 50%    |         |         | 50%    |        |         |         |        |
| 0%     |         |         |        | 0%     |         |         |        |
| Social | Hacking | Malware | Misuse | Social | Hacking | Malware | Misuse |
Figure #94: Actions within Cyber-Espionage breaches   Figure #95: Actions within all breaches for Manufacturing
for Manufacturing (2014-2020 DBIR; n=320) (2014-2020 DBIR; n=937)
| 100% |     |     | 100% |     |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
| 50%  |     |     | 50%  |     |     |     |     |
| 0%   |     |     |      | 0%  |     |     |     |
Person User Dev Server Media Network Person User Dev Server Media Network
Figure #96: Assets within Cyber-Espionage breaches   Figure #97: Assets within all breaches for Manufacturing
for Manufacturing (2014-2020 DBIR; n=316) (2014-2020 DBIR; n=874)
| 100% |     |     | 100% |     |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
| 50%  |     |     | 50%  |     |     |     |     |
| 0%   |     |     | 0%   |     |     |     |     |
Credentials Internal Secrets Personal m Bank ment Medical Credentials Internal Secrets Personal m Bank ment Medical
|     |     | Syste |     |     |     | Syste |     |
| --- | --- | ----- | --- | --- | --- | ----- | --- |
|     |     | Pay   |     |     |     | Pay   |     |
Figure #98: Compromised Data varieties within Cyber-Espionage  Figure #99: Compromised Data varieties within all breaches
breaches for Manufacturing (2014-2020 DBIR; n=312) for Manufacturing (2014-2020 DBIR; n=767)
| 51  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Mining, Quarrying, Oil &
Gas Extraction + Utilities
0% 10% 20% 30% 40% 50% 60%
NAICS 21+22 – Mining, Quarrying, Oil & Gas Extraction +
Utilities Web Applications 37%
Remarks Unless otherwise stated, information covers the
Cyber-Espionage 23%
2014-2020 DBIR timeframe. Also, note the change
in scale among figures. Privilege Misuse 18%
All breaches
Everything Else 13%
Frequency 230 (2014-2020) | 43 (2020)
Miscellaneous Errors 6%
Actors External (80%), Internal (24%), Multiple (4%)
Crimeware 4%
Motives Financial (63%-95%), Espionage (8%-43%)
Lost and Stolen Assets 2%
Cyber-Espionage breaches
Payment Card Skimmers 1%
Frequency 54 (23%) (2014-2020)
Actors External (100%), Internal (13%), Multiple (13%) Point of Sale 0%
Actions Social (88%), Hacking (79%), Malware (79%) Denial of Service 0%
Assets Person (90%), User Dev (80%), Server (27%)
Data Secrets (62%), Internal (27%), Credentials (14%) Figure #100: Breaches by pattern for Mining + Utilities
(2014-2020 DBIR; n=230)
Summary
In 2019, less than half of breaches in the Mining, Quarrying,
Oil & Gas Extraction + Utilities industries had confirmed
motives, resulting in significant ranges for Financial and
Espionage motive percentages.
For this industry combination, we observed a range of
8%-43% in Espionage motives, making the degree of this
threat uncertain. The range also highlights the challenges in
identifying Espionage-motivated attacks and determining just
how prevalent the threat is in this industry.
We see the dominant action for Cyber-Espionage breaches
in this industry as Social followed closely by Malware
and Hacking.
52 2020-2021 Cyber-Espionage Report

| 0% 20%   | 40% 60% | 80% | 100% 0%  | 20% | 40% 60% | 80% | 100% |
| -------- | ------- | --- | -------- | --- | ------- | --- | ---- |
| External |         |     | External |     |         |     |      |
|          |         |     | 100%     |     |         | 80% |      |
| Internal |         |     | Internal |     |         |     |      |
| 13%      |         |     |          | 24% |         |     |      |
| Partner  |         |     | Partner  |     |         |     |      |
| 0%       |         |     | 0%       |     |         |     |      |
| Multiple |         |     | Multiple |     |         |     |      |
| 13%      |         |     |          | 4%  |         |     |      |
Figure #101: Actors within Cyber-Espionage breaches   Figure #102: Actors within all breaches for Mining + Utilities
for Mining + Utilities (2014-2020 DBIR; n=54) (2014-2020 DBIR; n=227)
| 100%   |         |         | 100%   |        |         |         |        |
| ------ | ------- | ------- | ------ | ------ | ------- | ------- | ------ |
| 50%    |         |         | 50%    |        |         |         |        |
| 0%     |         |         |        | 0%     |         |         |        |
| Social | Hacking | Malware | Misuse | Social | Hacking | Malware | Misuse |
Figure #103: Actions within Cyber-Espionage breaches   Figure #104: Actions within all breaches for Mining + Utilities
for Mining + Utilities (2014-2020 DBIR; n=42) (2014-2020 DBIR; n=140)
| 100% |     |     | 100% |     |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
| 50%  |     |     | 50%  |     |     |     |     |
| 0%   |     |     |      | 0%  |     |     |     |
Person User Dev Server Media Network Person User Dev Server Media Network
Figure #105: Assets within Cyber-Espionage breaches   Figure #106: Assets within all breaches for Mining + Utilities
for Mining + Utilities (2014-2020 DBIR; n=41) (2014-2020 DBIR; n=131)
| 100% |     |     | 100% |     |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
| 50%  |     |     | 50%  |     |     |     |     |
| 0%   |     |     | 0%   |     |     |     |     |
Credentials Internal Secrets Personal m Bank ment Medical Credentials Internal Secrets Personal m Bank ment Medical
|     |     | Syste |     |     |     | Syste |     |
| --- | --- | ----- | --- | --- | --- | ----- | --- |
|     |     | Pay   |     |     |     | Pay   |     |
Figure #107: Compromised Data varieties within Cyber-Espionage  Figure #108: Compromised Data varieties within all breaches
breaches for Mining + Utilities (2014-2020 DBIR; n=37) for Mining + Utilities (2014-2020 DBIR; n=113)
| 53  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Professional, Scientific,
and Technical Services
|       |                                      |     | 0% 10% 20% | 30% 40% | 50% 60% |
| ----- | ------------------------------------ | --- | ---------- | ------- | ------- |
| NAICS | 54 – Professional, Scientific, and   |     |            |         |         |
Technical Services
|         |                                                  | Web Applications |     | 26% |     |
| ------- | ------------------------------------------------ | ---------------- | --- | --- | --- |
| Remarks | Unless otherwise stated, information covers the  |                  |     |     |     |
|         |                                                  | Everything Else  |     | 21% |     |
2014-2020 DBIR timeframe. Also, note the change
|     | in scale among figures. | Cyber-Espionage | 17% |     |     |
| --- | ----------------------- | --------------- | --- | --- | --- |
All breaches
|           |                                                | Miscellaneous Errors | 16% |     |     |
| --------- | ---------------------------------------------- | -------------------- | --- | --- | --- |
| Frequency | 980 (2014-2020) | 326 (2020)                   |                      |     |     |     |
|           |                                                | Privilege Misuse     | 9%  |     |     |
| Actors    | External (77%), Internal (23%), Partner (3%),  |                      |     |     |     |
|           |                                                | Crimeware            | 8%  |     |     |
Multiple (2%)
Motives Financial (93%), Espionage (8%), Ideology (1%) Lost and Stolen Assets 4%
| Cyber-Espionage breaches |                                               | Point of Sale      | 1%  |     |     |
| ------------------------ | --------------------------------------------- | ------------------ | --- | --- | --- |
| Frequency                | 166 (17%) (2014-2020)                         |                    |     |     |     |
|                          |                                               | Denial of Service  | 0%  |     |     |
| Actors                   | External (100%), Internal (2%), Multiple (2%) |                    |     |     |     |
|                          | Payment Card Skimmers                         |                    | 0%  |     |     |
| Actions                  | Social (74%), Hacking (58%), Malware (84%)    |                    |     |     |     |
| Assets                   | Person (79%), User Dev (77%), Server (20%)    |                    |     |     |     |
Figure #109: Breaches by pattern for Professional
(2014-2020 DBIR; n=980)
| Data    | Secrets (80%), Credentials (14%), Internal (8%) |     |     |     |     |
| ------- | ----------------------------------------------- | --- | --- | --- | --- |
| Summary | 500                                             |     |     |     |     |
The Professional, Scientific, and Technical Services industry
400
has seen approximately 11% of the Cyber-Espionage
breaches between 2014 and 2019. Like other private
| industries, not all Cyber-Espionage breaches are reported. | 300 |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --- | --- | --- |
Since 2015, we have seen a definite decline in reported
| Espionage-motivated attacks in the Professional industry.   | 200 |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- |
We cannot account for the number of unreported breaches.
| From the reported breaches, however, we can see that  | 100 |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- |
assets Person and User Dev were the top compromised
assets and that 80% of compromised data was classified
0
as Secrets.
|     |     | 2014 2015                | 2016 2017     | 2018 | 2019 2020 |
| --- | --- | ------------------------ | ------------- | ---- | --------- |
|     |     | Cyber-Espionage breaches | All breaches  |      |           |
Figure #110: Cyber-Espionage breaches within all breaches
annually for Professional (2014-2020 DBIR)
| 54  |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | -------------------------------- | --- |

| 0% 20%   | 40% 60% | 80% | 100% 0%  | 20% | 40% 60% | 80% | 100% |
| -------- | ------- | --- | -------- | --- | ------- | --- | ---- |
| External |         |     | External |     |         |     |      |
|          |         |     | 100%     |     |         | 77% |      |
| Internal |         |     | Internal |     |         |     |      |
| 2%       |         |     |          | 23% |         |     |      |
| Partner  |         |     | Partner  |     |         |     |      |
| 0%       |         |     |          | 3%  |         |     |      |
| Multiple |         |     | Multiple |     |         |     |      |
| 2%       |         |     | 2%       |     |         |     |      |
Figure #111: Actors within Cyber-Espionage breaches   Figure #112: Actors within all breaches for Professional
for Professional (2014-2020 DBIR; n=166) (2014-2020 DBIR; n=976)
| 100%   |         |         | 100%   |        |         |         |        |
| ------ | ------- | ------- | ------ | ------ | ------- | ------- | ------ |
| 50%    |         |         | 50%    |        |         |         |        |
| 0%     |         |         |        | 0%     |         |         |        |
| Social | Hacking | Malware | Misuse | Social | Hacking | Malware | Misuse |
Figure #113: Actions within Cyber-Espionage breaches  Figure #114: Actions within all breaches for Professional
for Professional (2014-2020 DBIR; n=125) (2014-2020 DBIR; n=923)
| 100% |     |     | 100% |     |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
| 50%  |     |     | 50%  |     |     |     |     |
| 0%   |     |     |      | 0%  |     |     |     |
Person User Dev Server Media Network Person User Dev Server Media Network
Figure #115: Assets within Cyber-Espionage breaches   Figure #116: Assets within all breaches for Professional
for Professional (2014-2020 DBIR; n=117) (2014-2020 DBIR; n=859)
| 100% |     |     | 100% |     |     |     |     |
| ---- | --- | --- | ---- | --- | --- | --- | --- |
| 50%  |     |     | 50%  |     |     |     |     |
| 0%   |     |     | 0%   |     |     |     |     |
Credentials Internal Secrets Personal m Bank ment Medical Credentials Internal Secrets Personal m Bank ment Medical
|     |     | Syste |     |     |     | Syste |     |
| --- | --- | ----- | --- | --- | --- | ----- | --- |
|     |     | Pay   |     |     |     | Pay   |     |
Figure #117: Compromised Data varieties within Cyber-Espionage  Figure #118: Compromised Data varieties within all breaches
breaches for Professional (2014-2020 DBIR; n=124) for Professional (2014-2020 DBIR; n=816)
| 55  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Public Administration
|         |                                                  |                      | 0% 10% 20% | 30% 40% | 50% 60% |
| ------- | ------------------------------------------------ | -------------------- | ---------- | ------- | ------- |
| NAICS   | 92 – Public Administration                       |                      |            |         |         |
|         |                                                  | Miscellaneous Errors |            | 23%     |         |
| Remarks | Unless otherwise stated, information covers the  |                      |            |         |         |
2014-2020 DBIR timeframe. Also, note the change  Cyber-Espionage 23%
in scale among figures.
| All breaches |     | Everything Else | 17% |     |     |
| ------------ | --- | --------------- | --- | --- | --- |
Frequency 2,152 (2014-2020) | 338 (2020) Privilege Misuse 14%
| Actors | External (61%), Internal (40%), Multiple (3%),  |                  |     |     |     |
| ------ | ----------------------------------------------- | ---------------- | --- | --- | --- |
|        |                                                 | Web Applications | 10% |     |     |
Partner (1%)
Crimeware 8%
| Motives | Financial (75%), Espionage (19%), Fun (3%) |                        |     |     |     |
| ------- | ------------------------------------------ | ---------------------- | --- | --- | --- |
|         |                                            | Lost and Stolen Assets | 6%  |     |     |
Cyber-Espionage breaches
| Frequency | 485 (23%) (2014-2020) | Payment Card Skimmers | 0%  |     |     |
| --------- | --------------------- | --------------------- | --- | --- | --- |
| Actors    | External (100%)       | Denial of Service     | 0%  |     |     |
Actions Social (94%), Hacking (93%), Malware (97%) Point of Sale 0%
| Assets | Person (96%), User Dev (95%), Server (25%) |     |     |     |     |
| ------ | ------------------------------------------ | --- | --- | --- | --- |
Data Secrets (55%), Internal (42%), Credentials (12%) Figure #119: Breaches by pattern for Public
(2014-2020 DBIR; n=2,152)
Summary
500
The Public Administration industry has ranked in the past
several years as one of the top industries reporting confirmed
400
data breaches with a Cyber-Espionage motive. In fact, in the
past three years, nearly half of Cyber-Espionage breaches
were reported in the public sector. And, since 2014, nearly a
300
quarter of the Cyber-Espionage breaches were reported in
this industry.
200
There are a few factors to consider when looking at these
numbers. We know that government data is one of the top
| data types of interest to Nation-state and State-affiliated  |     | 100 |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- |
actors, so these numbers don’t surprise us. However, it is
important to point out that the public industry has more
0
stringent reporting requirements than the private sector,  2014 2015 2016 2017 2018 2019 2020
which will inevitably result in more breaches being reported.
|     |     | Cyber-Espionage breaches | All breaches  |     |     |
| --- | --- | ------------------------ | ------------- | --- | --- |
Figure #120: Cyber-Espionage breaches within all breaches
annually for Public (2014-2020 DBIR)
| 56  |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | -------------------------------- | --- |

| 0% 20%   | 40% 60% | 80% | 100% 0%  | 20% | 40% 60% | 80% | 100% |
| -------- | ------- | --- | -------- | --- | ------- | --- | ---- |
| External |         |     | External |     |         |     |      |
|          |         |     | 100%     |     |         | 61% |      |
| Internal |         |     | Internal |     |         |     |      |
| 0%       |         |     |          |     | 40%     |     |      |
| Partner  |         |     | Partner  |     |         |     |      |
| 0%       |         |     | 1%       |     |         |     |      |
| Multiple |         |     | Multiple |     |         |     |      |
| 0%       |         |     |          | 3%  |         |     |      |
Figure #121: Actors within Cyber-Espionage breaches for Public   Figure #122: Actors within all breaches for Public
| (2014-2020 DBIR; n=485) |         |         | (2014-2020 DBIR; n=2,138) |        |         |         |        |
| ----------------------- | ------- | ------- | ------------------------- | ------ | ------- | ------- | ------ |
| 100%                    |         |         | 100%                      |        |         |         |        |
| 50%                     |         |         | 50%                       |        |         |         |        |
| 0%                      |         |         |                           | 0%     |         |         |        |
| Social                  | Hacking | Malware | Misuse                    | Social | Hacking | Malware | Misuse |
Figure #123: Actions within Cyber-Espionage breaches for Public  Figure #124: Actions within all breaches for Public
| (2014-2020 DBIR; n=380) |     |     | (2014-2020 DBIR; n=1,826) |     |     |     |     |
| ----------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
| 100%                    |     |     | 100%                      |     |     |     |     |
| 50%                     |     |     | 50%                       |     |     |     |     |
| 0%                      |     |     |                           | 0%  |     |     |     |
Person User Dev Server Media Network Person User Dev Server Media Network
Figure #125: Assets within Cyber-Espionage breaches for Public   Figure #126: Assets within all breaches for Public
| (2014-2020 DBIR; n=374) |     |     | (2014-2020 DBIR; n=1,367) |     |     |     |     |
| ----------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
| 100%                    |     |     | 100%                      |     |     |     |     |
| 50%                     |     |     | 50%                       |     |     |     |     |
| 0%                      |     |     | 0%                        |     |     |     |     |
Credentials Internal Secrets Personal m Bank ment Medical Credentials Internal Secrets Personal m Bank ment Medical
|     |     | Syste |     |     |     | Syste |     |
| --- | --- | ----- | --- | --- | --- | ----- | --- |
|     |     | Pay   |     |     |     | Pay   |     |
Figure #127: Compromised Data varieties within Cyber-Espionage  Figure #128: Compromised Data varieties within all breaches
breaches for Public (2014-2020 DBIR; n=370) for Public (2014-2020 DBIR; n=1,268)
| 57  |     |     |     |     |     | 2020-2021 Cyber-Espionage Report |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- |

Final notes
Cyber-Espionage Report Team Verizon thought leadership
The Cyber-Espionage Report (CER) Team is a subset of
VTRAC combined with elements of the DBIR Team. We’ve Data Breach Investigations Report (DBIR)
spent years investigating advanced threat actor data breaches,
assessing cybersecurity postures and advising on IR measures • Data Breaches/Cybersecurity Incidents
in our current roles and previous lives.
• 9 x Incident Classification Patterns |
Managing Director Contributors 9 x CIS CSCs
Chris Novak David Kennedy, Alex Pinto, • enterprise.verizon.com/resources/reports/
Phillipe Langlois, Suzanne dbir/
Authors
Widup
John Grim, Ashish Thapar,
Mobile Security Index (MSI)
Amy Ayers, Anshuman
Sharma, Nicolas Villatte,
• Mobile Devices/IoT/Wi-Fi Security Insight
Damian John Werts, Domingo
Jesus Alvarez-Fernandez • 5 x Fortify Levels
• enterprise.verizon.com/resources/reports/
mobile-security-index/
About VTRAC
Insider Threat Report (ITR)
The Verizon Threat Research Advisory Center (VTRAC) Insider
Threat
Report
has been assisting customers globally with maturing and Osohu uot t ou o fldf m s ni i g neh dvetr be • Insider Threat Breaches/Cybersecurity
improving their IR readiness for more than 14 years. In
Incidents
conducting its engagements, VTRAC uses industry best
practices—such as the NIST Cybersecurity Framework—and • 5 x Breach Scenarios |
our VIPR phases, as well as our expertise from the more than 11 x Countermeasures
500 incidents we investigate globally each year. We cover all business ready • enterprise.verizon.com/resources/reports/
five functional areas of the NIST Cybersecurity Framework.
insider-threat-report/
Our capabilities include endpoint forensics, network forensics,
malware reverse engineering, threat intelligence, threat hunting, Verizon Insider Preparedness and
Incident
dark web research, mobile device forensics and complex data P a R n r e e d p p o R a r e r t e sp d o n n e s s e s Response (VIPR) Report
recovery, as well as breach simulations, cyber threat landscape Tdb a rae mtaa i cbn heg .a tshte
briefings, IR capability assessments, first responder training, • IR Plan review and breach simulation
and IR Plan and playbook development. exercise insight
• 5 x Breach Scenarios | 6 x VIPR Phases |
VTRAC has written the book—literally—on data breaches,
from starting the DBIR phenomenon and contributing annually A publication written by practitioners for practitioners. 20 x Key Takeaways
to the Payment Security Report to creating the Data Breach • enterprise.verizon.com/resources/reports/
Digests, Insider Threat Report, Incident Preparedness and vipr/
Response Report and now the CER.
With the CER now under our proverbial belts, the only Payment Security Report (PSR)
question left unanswered is: • PCI Assessment/PFI Investigation Insight
What will VTRAC set its sights on next? Stay tuned to find • 12 x PCI DSS Requirements
out...
• verizon.com/business/resources/reports/
payment-security-report/
About the cover
Cyber-Espionage breaches occur when external attackers,
such as State-affiliated or Nation-state threat actors,
penetrate victim organization cyberdefenses to steal sensitive
data or proprietary information. The cover image for our first-
ever Cyber-Espionage Report depicts a Cyber-Espionage
breach at the moment the attacker pierces the veil of security
en route to plundering their targeted victim’s critical assets
and most sensitive information.
58 2020-2021 Cyber-Espionage Report
0202
Mobile
Security
Index
2020 Report
PSaeycmureitnyt R eport

verizon.com/business/resources/reports/cyber-espionage-report/
REP11431120