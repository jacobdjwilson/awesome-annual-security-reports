# Instinct-Cyber-Threat-Landscape-Report 2022

## Table of Contents
- [Executive Summary](#executive-summary)
- [Foreword](#foreword)
- [Top Takeaways](#top-takeaways)
- [The Top Malware Trends of 2021](#the-top-malware-trends-of-2021)
- [The Top 5: Malware Families](#the-top-5-malware-families)
- [The Top 5: Ransomware Families](#the-top-5-ransomware-families)
- [The Top 5: Linux Malware Families](#the-top-5-linux-malware-families)
- [The Top 5: Financial Malware Families](#the-top-5-financial-malware-families)
- [The Top 10: MITRE techniques and capabilities](#the-top-10-mitre-techniques-and-capabilities)
- [High profile vulnerabilities in 2021](#high-profile-vulnerabilities-in-2021)
- [Interesting trends and campaigns in 2021](#interesting-trends-and-campaigns-in-2021)
- [Malware Trends by Campaign](#malware-trends-by-campaign)
- [Deep Instinct discoveries in 2021](#deep-instinct-discoveries-in-2021)
- [The New Normal: Post COVID-19 and the hybrid workplace](#the-new-normal-post-covid-19-and-the-hybrid-workplace)
- [Cyber Insights: A Look Back at Our 2021 Predictions](#cyber-insights-a-look-back-at-our-2021-predictions)

---

## Executive Summary

Welcome to our annual review of the most significant cyber threats and trends from 2021. While there were continuations of trend lines that have been mainstays of the threat landscape for the past few years, there were also some unexpected developments that warrant mention. The increase in the highest profile threat (ransomware) has not continued at the same pace seen during the height of the COVID-19 outbreak in spring 2020, although it still recorded double digit (15.8%) growth. Specific attack vectors have grown substantially, such as the use of Office droppers (up 170%), along with an overall uptick of 125% in all threat types combined. Overall, the volume of all malware types is still substantially higher than during the pre-pandemic period.

The attacks themselves are also changing as we are now witnessing some groups opting to inflict the maximum impact over a shorter time span. In these shorter-duration attacks, the goal is to damage data (its confidentiality and availability), destabilize a business, and impair business continuity. High profile breaches within critical infrastructures — such as the one experienced by Colonial Pipeline — can have huge consequences for millions of consumers. The energy sector is experiencing more of these attacks because the instant pain inflicted can speed the payment of ransom — the ultimate goal of any ransomware attack. While attacks that rely on dwell time and stealth are certainly a major hazard for cyber professionals, shorter duration attacks are gaining favor.

The ongoing transition of many organizations to a work-from-anywhere or hybrid work model has broadened and multiplied attack surfaces, in the process rendering defenses less active. Additionally, the continued move to cloud applications has reduced costs, but also surfaced several inherent dangers to business leaders.

Modular campaigns have been a feature of 2021, highlighted by spyware/ransomware combinations and multi/cross-OS attacks. We have seen a clear relationship between Emotet and TrickBot operators, with infected TrickBot machines being used to download the new Emotet binary. More thought is going into certain attack methods with a rise in multi-stage custom-built packers and encryptors evident. As a result, adopting a multi-layered protection mindset becomes even more critical.

Supply-chain attacks have been an ongoing topic as well. In July 2021, in one of the year’s greatest supply-chain attacks, REvil infected Kaseya VSA and then infiltrated the company’s VSA clients’ environments. REvil took advantage of a then-unpatched zero-day vulnerability in the Kaseya VSA product. More than 1,500 companies using Kaseya’s services were ultimately infected with REvil.

The HAFNIUM group, which targeted Exchange servers shortly after Microsoft revealed multiple zero-day vulnerabilities, was behind the single biggest threat of the year. This attack underscored why major vulnerabilities are being exploited and used within hours of disclosing the vulnerability. The race between patching vulnerable systems versus an attacker’s ability to create a single-day exploit will continue to be a significant trend in 2022.

Overall, while 2021 was not marked with exponential increases in attack volumes, attacks became increasingly advanced. Attackers turned to more sophisticated evasion techniques that worked by fooling or bypassing detection tools. Defense evasion and privilege escalation are becoming more prevalent, and we expect to see a continuation of EPP/EDR evasion techniques in 2022. Bad actors are clearly investing in anti-AI and adversarial attack techniques and integrating these methods into their larger evasion strategy.

This report represents Deep Instinct’s current view of the threat landscape, showcasing trends seen throughout the course of the past year and providing concrete, actionable data to verify the credibility of these developments. The information was sourced from our data repositories, which are routinely analysed as part of protecting our customers from ceaseless attacks. We hope this report will provide you with a better understanding of the present threat landscape and its future trajectory.

Best regards,

Shimon N. Oren
VP of Research and Deep Learning

---

## Foreword

Deep Instinct is pleased to release its 2021 Threat Landscape Report. The information presented in this report is based on D-cloud, Deep Instinct’s proprietary file reputation database. The database receives data from multiple feeds including well-known threat intelligence providers, curated sources maintained by Deep Instinct’s research group, and production data from Deep Instinct’s customer base. This wide cumulation of datasets is reflective of hundreds of millions of events that occurred in 2021.

The proprietary database provides real-time information on threats for the purpose of supporting Deep Instinct’s research efforts and to help ensure optimal security of our customers. The analysis in this research study considers hundreds of millions of attempted attacks that occurred every day throughout 2021 within our customer environments. This information was gathered by Deep Instinct’s team of researchers who have decades of combined experience and are veterans of various cyber intelligence units in the Israel Defense Forces. They extrapolated these findings to predict the future of cybersecurity so that we can stay ahead of attackers and prepare for the security threats of tomorrow. We also give a keen eye to what motivates attackers, how their threat tactics and strategies are evolving, and most importantly, what steps we can take now to learn from this information and develop more fortified defenses against future attacks.

---

## Top Takeaways

### 01 The rise of supply chain attacks
While supply chain attacks are certainly not new, they were leveraged with greater regularity in 2021. A variety of large service offering companies became targets with threat actors intending to not only gain access to their environments, but the environments of their customers by proxy. — hit in early July 2021 by the REvil ransomware using a then-unpatched zero-day vulnerability in the Kaseya VSA product. As a result, more than 1,500 companies were infected with REvil. Given the success of these attacks and the efficiency of one attack opening thousands more for compromise, we’re likely to see many similar attacks moving ahead.

### 02 The shift to impact and high-profile attacks vs. stealth and long dwell-time attacks
We have traditionally seen attackers gaining initial access and persistence over a victim network with the goal of dwelling for extended periods, stealing information, and avoiding detection from security solutions for as long as possible. Their foothold remains stealthy, and they are harvesting data or abusing servers for cryptomining as long as they can. In 2021, we saw a transition to high-profile attacks with a massive impact. We have begun seeing more high-impact attacks on critical infrastructures across all sectors in recent years, but nothing seems to compare to the Colonial Pipeline breach in terms of scope. This attack, which caused Colonial Pipeline to halt their operations for six days, caused major disruptions across the U.S., a shortage of fuel, and a subsequent increase in gas prices. Not only did this incident demonstrate the significant and cascading impact of a well-executed malware attack, but it also emphasized the importance of having sufficient cybersecurity defense mechanisms to protect critical infrastructure.

### 03 Public and private sector collaborations become more common
As we have predicted, there was greater partnership among international task forces this past year to identify and bring to justice key threat actors around the world. High-profile targets, including Emotet and REvil, were taken down by joint teams of law enforcement agencies. Other high-profile threat actors such as Glupteba became the target of private companies that joined forces to interrupt their activity as much as possible. We hope this growing spirit of collaboration is here to stay and leads to the dismantling of more high-profile threat groups.

### 04 The quick trickling down on zero-day
Zero-day threats have always been a major concern when it comes to cyber security. But severe vulnerabilities are not discovered daily. When it comes to zero-day threats, there is a long period from the time between when the vulnerability is disclosed and patched to the time an organization can patch all its relevant components. In 2021, we saw major vulnerabilities being exploited and used within a single day of disclosing the vulnerability. One of the examples is the HAFNIUM group which surfaced shortly after Microsoft revealed multiple zero-day vulnerabilities. The race between patching vulnerable systems versus attacker’s ability to create a zero-day exploit will continue in 2022.

### 05 Cloud as a gateway for attackers
The transition to work-from-anywhere has sped digital transformation efforts for many organizations, inducing them to move most of their services to the cloud rather than on premises. And attackers are not remaining indifferent to these changes. For many organizations, the transition to the cloud brings a plethora of business opportunities, but it also comes with many cyber security challenges and risks. For organizations that are not experienced working with cloud services there is the risk that misconfigurations or vulnerable, out-of-date components with external API access can be exploited.

During 2021 we saw many high-profile vulnerabilities every few months, with publicly available exploit POCs. Securing the entire on-premises network is not enough anymore, as a single outdated cloud component can create a gateway for attackers to breach an entire organization.

---

## The Top Malware Trends of 2021

![Graph showing the number of new samples each month since January 2020, grouped by malware type (Backdoor, Ransomware, Dropper, Spyware, Virus, Worm, Miner) in arbitrary units.]

As seen in the graph below, the trend that started in 2020 continued throughout 2021 with a spike in all malware types. In spite of a decrease in spyware caused by the Emotet takedown in early 2021, the rates of all malware types are still substantially higher than those of the pre-COVID era.

---

## The Top 5: Malware Families

![Chart showing the top 5 malware families: Dridex (58%), Emotet (10%), AgentTesla (13%), IcedID (10%), TrickBot (9%)]

### 01 Dridex
is a highly active banking trojan family, observed in the wild since 2011 (for context, in 2011 it appeared as its predecessor, Cridex). The first version of the current iteration of Dridex was spotted in mid-2014 and has become an extremely high-profile financial malware family.

### 02 Emotet
initially functioned as a banking trojan when it emerged in 2014. It was spread via spam campaigns, imitating financial statements, transfers, and payment invoices. Emotet is propagated mostly via Office email attachments containing a macro. If enabled, it downloads a malicious PE file (Emotet) which is then executed. Once executed, it can intercept and log network traffic, inject into browsers, and access banking sites in order to exfiltrate and store financial data.

### 03 Agent Tesla
is a spyware that has been sold online since 2014. It is advertised as a legitimate monitoring software not intended for malicious purposes. However, its password extraction functionality and features that are aimed at avoiding detection allow Agent Tesla’s operators to use it for malicious purposes.

### 04 TrickBot
is a sophisticated banking malware that targets individuals, SMBs, and enterprise environments focusing specifically on gaining access to bank account credentials, financial data, and personal information in order to carry out financial fraud and identity theft.

### 05 IcedID
is a modular banking trojan active in the past few years, mainly targeting businesses in the U.S. and the UK. It primarily targets the financial industry, aiming to attack banks, credit card companies, and e-commerce properties.

---

## The Top 5: Ransomware Families

![Chart showing the top 5 ransomware families: STOP, REvil, Cerber, Conti, DarkSide]

### 01 STOP
is a ransomware family discovered in December 2018. It encrypts files on a victim’s machine using the AES-256 encryption algorithm.

### 02 REvil
also known as Sodinokibi, is a ransomware which first appeared in the wild in April 2019. This malware has since been utilized in several high-profile targeted attacks against private companies and government organizations.

### 03 Cerber
was one of the most widespread and publicized ransomware families in 2016 and 2017. At its peak in early 2017, Cerber accounted for more than 25% of all ransomware infections.

### 04 Conti
ransomware, first seen in May 2020, is a highly proliferating ransomware and one of most common malware variants we see today.

### 05 DarkSide
which first appeared in August 2020, is a ransomware that mostly targets organizations in English-speaking countries.

---

## The Top 5: Linux Malware Families

![Chart showing the top 5 Linux malware families: XorDDoS, Mirai, Gafgyt, Hajime, Tsunami]

### 01 XorDDos
was first seen in 2014 and has been building its army of botnets for the last eight years. The malware spreads by brute forcing its way into Linux and Docker servers.

### 02 Mirai
is an infamous botnet that has been operating since 2016. It was responsible for some of the most disruptive DDoS attacks in the world.

### 03 Gafgyt
(aka BASHLITE, Lizkebab, and Torlus) is a modular botnet malware with dropper, backdoor, and spyware capabilities.

### 04 Hajime
was discovered in October 2016 while researching Mirai. It utilizes a peer-to-peer decentralized network for its communication purposes.

### 05 Tsunami
(aka Mushtik, Amnesia, and Radiation) botnet has been active since as early as 2013.

---

## The Top 5: Financial Malware Families

![Chart showing the top 5 financial malware families: Dridex, TrickBot, QakBot, Zloader, IcedID]

*(Content details for these families are provided in the report, mirroring the descriptions found in the Malware Families section.)*

---

## The Top 10: MITRE techniques and capabilities

1. **Execution**: Command and Scripting Interpreter [TA0002.T1059]
2. **Persistence**: Boot or Logon AutoStart Execution [TA0004.T1574]
3. **Privilege Escalation**: Hijack Execution Flow [TA0003.T1547]
4. **Defense Evasion**: Obfuscated Files or Information: Software Packing [TA0005.T1027.002]
5. **Credential Access**: OS Credential Dumping [TA0006.T1003]
6. **Discovery**: Virtualization/Sandbox Evasion [TA0007.T1497]
7. **Lateral Movement**: Remote Services [TA0008.T1021]
8. **Collection**: Input Capture [TA0009.T1056]
9. **Exfiltration**: Exfiltration Over Web Service [Ta0010.T1567]
10. **Impact**: Data Encrypted for Impact [TA0040.T1486]

---

## High profile vulnerabilities in 2021

- **Log4Shell**: A severe vulnerability in Apache’s logging framework, Log4j2, with a CVSS score of 10.0.
- **ProxyShell**: A combination of three Microsoft Exchange vulnerabilities disclosed in August 2021.
- **PrintNightmare**: An ongoing issue in the Windows print Spooler service, first seen during the early summer of 2021.

---

## Interesting trends and campaigns in 2021

- **Python and Go Malware**: Threat actors have made a discernable shift away from older programming languages, such as C and C++, in favor of newer languages.
- **RedLine Stealer**: An information stealer that added new tools to its utility belt in 2021, making it considerably more dangerous.
- **Cloud Service Providers**: GuLoader and other droppers are increasingly abusing legitimate cloud service providers (Google Drive, OneDrive) to store malware.

---

## Malware Trends by Campaign

- **Excel 4.0 Macros**: A legacy scripting language supported in Microsoft Office since 1992, now being used for sophisticated malware delivery.
- **JavaScript**: Script-based attacks now account for 40% or more of all global cyberattacks.
- **Attacks on Microsoft Exchange Servers**: High-profile, high-severity vulnerabilities (HAFNIUM, ProxyShell) dominated the landscape.

---

## Deep Instinct discoveries in 2021

- **LSAAS memory dumps**: A new technique of credential dumping relying on the "Silent Process Exit" mechanism.
- **Identifying Excel 4.0 Macros**: Researchers presented methods at DefCon on how to identify Excel 4.0 macros using anomaly detection.
- **Emotet re-emerges**: Development of the "DeMotet" tool to automate the analysis of Emotet samples on a large scale.

---

## The New Normal: Post COVID-19 and the hybrid workplace

Work-from-anywhere jobs have become the new normal. Perimeter solutions that relied on physical access are now less effective compared to endpoint protection solutions. Security professionals must prioritize changing security footprints to ensure full coverage.

---

## Cyber Insights: A Look Back at Our 2021 Predictions

- **COVID-19 aftereffects**: Cybersecurity incidents increased significantly as predicted.
- **Proliferation of botnets**: Botnets continued to be a growing threat.
- **Organized cybersecurity cooperation**: While some government cooperation occurred, open collaboration between governments and private researchers was less frequent than hoped.
- **Adversarial machine learning**: Has yet to become a serious threat, though it remains a concern.
- **Ransomware targeting mission-critical organizations**: This prediction was correct, as seen in the Colonial Pipeline attack.

---

he attack, by the DarkSide
gang, forced the company to stop its operations, resulting
in fuel shortages that were partly caused by panic buying
of fuel. It also forced airlines to temporarily change routes
and flight schedules.

Additionally, the BlackMatter group attacked JBS, which is
the world’s largest meat processing company, demanding
$11M USD in ransom.

Another case of ransomware trying to hit critical
infrastructure was an attack on two Brazilian
electric utility companies: Eletrobras and Copel.
Although no disruptions in electricity supply were
reported, such an attack could have left a large
number of citizens without power or caused
damage to the nuclear power plants responsible
for its production.

An additional ransomware attack on the Italian
vaccination registration system prevented residents
of the Lazio region from getting vaccinated,
endangering their lives during a pandemic.

We also witnessed several attacks on hospitals
and health centers in the U.S. (UF Health Central
Florida, Scripps Health, and Crisp Regional Health
Services) and France (Oloron-Sainte-Marie and
Dax-Côte d’Argent Hospital Center) as well as other
hospitals in Canada, Australia, and Ireland.

Although high profile attacks have the biggest
payoff, they also have their price – massive publicity
and scrutiny. These attacks are the ones that
motivated the multinational efforts to arrest and
prosecute operators of these ransomware crews.

CYBER THREAT LANDSCAPE REPORT 2022

28

VPN as a breach vector

As the COVID-19 pandemic continues to
impact people and organizations in significant
ways, giants of industry are again delaying
their “return to office” plans with many
operationalizing a longer strategic plan for
hybrid and full remote work models.

A new normal has emerged where remote
work and access are the de facto reality and
organizations are now exposing more attack
surfaces to potential adversaries. Defenders
must be prepared to deal with devices in their
networks which they can’t physically access
and may not even be able to access at all in
a BYOD scenario, exposing more of their
organizational assets to the outside world.
We expect these new work conditions and
their connected devices to become a more
significant part of the active threat landscape.

Prepare for more supply
chain attacks

Supply chain attacks are on the rise, presenting
an extreme challenge for cyber defenders.

Considering the newly established and
commonplace reality of remote access and
remote work, we expect companies that
develop remote-access software and other
companies enabling remote work to become
much more enticing targets for supply chain
attack actors. These are likely to result in
high repercussion incidents like SolarWinds
becoming more numerous and impactful to a
larger number of connected organizations.

The ongoing rise of
Malware-As-a-Service

With a growing number of malware strains
opting to operate under a Malware-as-a-
Service model, developing new malware
has become big business – especially in the
Ransomware landscape.

Threat actors either lacking the ability to
develop their own malware or seeking to
disguise themselves among a horde of other
malware users are gravitating towards these
“services,” and we expect this ongoing trend
to continue and intensify.

CYBER THREAT LANDSCAPE REPORT 2022

29

Cyber Insights: 2022 PredictionsDefense evasion
becoming a greater
focus

As more and more security vendors make use
of machine learning and artificial intelligence
in their products and take actions to improve
their already-existing defense mechanisms,
increasing their efficacy, malicious actors will
also continue to hone and improve efforts
to evade and fool both traditional and AI-
based defense mechanisms. We expect to see
malware becoming generally more evasive,
with more innovative attempts to evade both
traditional defenses and machine classifiers by
various means, including adversarial AI attacks.

Health sector
increasingly targeted

As the pandemic rages on, the global
healthcare sector and its supply chains will
continue to pose a significant and enticing
target for adversaries. Considering this sector’s
global importance with COVID-19 still a major
issue, coupled with its everyday operational
sensitivity, we expect to see an increase in the
number of attacks against it by adversaries,
possibly including attacks against COVID-19
vaccine supply chains.

CYBER THREAT LANDSCAPE REPORT 2022

30

This report was authored by members of
the Deep Instinct Threat Research team:

Deep Instinct takes a prevention-first approach to stopping ransomware and other malware using the world’s first
and only purpose built, deep learning cybersecurity framework. We predict and prevent known, unknown, and
zero-day threats in <20 milliseconds, 750X faster than the fastest ransomware can encrypt.

Moshe Hayun
Ido Kringel
Bar Block
Roei Amit
Shaul Vilkomir-Preisman

© Deep Instinct Ltd.

Deep Instinct has >99% zero-day accuracy and promises a <0.1% false positive rate. The Deep Instinct Prevention
Platform is an essential addition to every security stack — providing complete, multi-layered protection against
threats across hybrid environments.

www.deepinstinct.com  |  info@deepinstinct.com