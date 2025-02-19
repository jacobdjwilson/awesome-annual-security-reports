# CYBER THREAT REPORT 2023/2024

## Table of Contents
- [Foreword](#foreword)
- [By the numbers](#by-the-numbers)
- [Aotearoa New Zealand threat landscape](#aotearoa-new-zealand-threat-landscape)
- [Incidents usually affecting individuals or small to medium businesses](#incidents-usually-affecting-individuals-or-small-to-medium-businesses)
- [Incidents of potential national significance](#incidents-of-potential-national-significance)
- [The impact of ransomware](#the-impact-of-ransomware)
- [Analysing trends in tactics and techniques](#analysing-trends-in-tactics-and-techniques)
- [High-impact techniques and mitigations](#high-impact-techniques-and-mitigations)
- [Loss and harm](#loss-and-harm)
- [International threat landscape](#international-threat-landscape)
- [Conclusion](#conclusion)
- [Getting in touch with the NCSC](#getting-in-touch-with-the-ncsc)
- [Glossary](#glossary)

The National Cyber Security Centre is part of the Government Communications Security Bureau

---

## Foreword
Whakapuakitanga

The National Cyber Security Centre (NCSC), a part of the Government Communications Security Bureau (GCSB), is Aotearoa New Zealand’s lead operational cyber security agency. An important organisational milestone was reached in the past financial year, when New Zealand’s Computer Emergency Response Team was transferred from the Ministry of Business, Innovation and Employment (MBIE) to the NCSC. This integration process, when completed, will result in an agency that provides cyber security services to all New Zealanders – from individuals and small to medium enterprises, through to nationally significant organisations.

This Cyber Threat Report outlines the NCSC’s view of the domestic threat landscape for the year from 01 July 2023 to 30 June 2024. The report provides insight into the scope and nature of cyber threats targeting the information and systems of New Zealand organisations and individuals. The report identifies and analyses some of the common, recurring techniques that malicious cyber actors have used in cyber incidents.

The information in this report is primarily intended to support the work of cyber security practitioners and researchers, as well as cyber security decision makers. However, anyone with an interest in cyber security may find the report informative, and I encourage all New Zealanders to build their understanding of cyber security.

This is the first reporting year in which the NCSC has compiled a whole-of-economy overview of cyber threats. While still drawn from separate data sets, in this report readers can begin to see the extent to which our country’s entire economy is being impacted by malicious cyber activity.

This year’s report illustrates how malicious cyber activity affects every part of New Zealand society. Good cyber security awareness and practices help to protect against the harm this malicious activity can cause. This report encourages familiarity with the cyber landscape and better understanding of the techniques and tactics used by malicious cyber actors, and recommends steps to mitigate them. Through good decisions and action, New Zealand can become a place where good cyber security happens everywhere, all the time, by everyone.

Lisa Fong (she/her)
Deputy Director-General Cyber Security.

---

## By the numbers
Mā ngā tau

The NCSC in 2023/24

The NCSC receives and handles incident reports through two distinct triage processes. Most incident reports are handled through the NCSC’s general triage process because they do not require specialist technical attention. Often these incidents affect either individual New Zealanders or small to medium businesses. The NCSC acknowledges that while these incidents did not require specialist attention, they remain highly impactful for the people or organisations they affect.

A much smaller proportion of incidents are triaged for more specialist technical support because of the nature of the victim, or the nature of the incident. These incidents could cause high impact at the national level and are referred to as incidents of potential national significance. These are incidents affecting organisations such as operators of critical infrastructure, and those that have the potential to impact large groups of New Zealanders. This report examines both categories of incident and provides analysis of key statistics and trends within them.

DISRUPTIONS AND INDICATORS

**10.3m**

In 2023/2024, the NCSC disrupted over 10.3 million malicious cyber events via Malware Free Networks® (compared to 250,000 in 2022/2023).

This exponential growth has continued since the reporting period closed.

**28,804**

Indicators of malicious activity published in 2023/24 via Malware Free Networks.

**11,386**

Phishing indicators published in 2023/24 via the Phishing Disruption Service.

**7122**

Total incident reports recorded by the NCSC

![Image description: Infographic showing the numbers of incidents and disruptions recorded by the NCSC in 2023/2024.]

**110**

or 32% of 343 incidents of potential national significance indicated links to suspected state-sponsored actors

Compared to 28% in 2022/2023

**6779**

Incidents handled through the NCSC’s general triage process, often affecting individual New Zealanders or small to medium businesses

Compared to 7744 in 2022/2023, a decrease of 12.5%

**65**

out of 343 incidents of potential national significance, or 19%, were likely criminal or financially motivated

Compared to 28% in 2022/2023

**343**

Incidents triaged for specialist technical support because of potential national significance

Compared to 316 incidents in 2022/2023 - an increase of 8.5%

IN THE 2023/2024 YEAR THE NCSC AND GCSB:

- Received 143 notifications of network change proposals under the Telecommunications (Interception Capability and Security) Act 2013 (TICSA).
- Conducted 21 assessments of regulated space activities under the Outer Space and High-altitude Activities Act 2017 (OSHAA).
- Conducted 74 assessments of regulated radio spectrum activities under the Radiocommunications Act 1989.
- Provided advice on 39 assessments under the Overseas Investment Amendment Act 2021 (OIAA).

THE NCSC INCREASED AOTEAROA NEW ZEALAND’S COLLECTIVE CYBER RESILIENCE:

- Delivered 82 incident reports to customers.
- Published 19 advisories for customers, including 16 co-authored with domestic and international partners.
- Published 30 critical vulnerability alerts.
- Co-chaired 24 sector-based Security Information Exchanges.

THE NCSC IN A TYPICAL MONTH THIS YEAR:

- Detected 7 cyber incidents affecting one or more nationally significant organisations through the NCSC’s cyber defence capabilities.
- Received 22 new incident reports or requests for assistance for incidents of potential national significance. Of the new incident reports received each month, 15 came from international or domestic partners while 7 came from self-reporting by victim organisations.
- Recorded 565 incidents handled through the NCSC’s general triage process, often affecting individual New Zealanders and small to medium businesses and organisations.

HARM REDUCTION AND FINANCIAL LOSS

**$38.8m**

$38.8 million worth of harm prevented in 2023/2024. Since June 2016, the NCSC has prevented an estimated $421.2 million worth of harm to Aotearoa New Zealand’s nationally significant organisations.

**$21.6m**

Total financial loss reported to the NCSC in incidents handled through the NCSC’s general triage process

Compared to $22.4 million in 2022/2023

Since 2017, the estimated total financial loss reported through the CERT function is $121 million.

---

## Aotearoa New Zealand threat landscape
Te āhuatanga o ngā tuma i Aotearoa

The cyber threat landscape is constantly changing, so it is vital to understand key cyber security threats in order to inform responses to the challenges. Malicious cyber activity is likely to continue to impact a larger range of systems and victims as New Zealand’s dependence on technology grows in size and complexity.

Aotearoa New Zealand’s growing connectivity of devices and networks, alongside the adoption of emerging technologies (such as artificial intelligence and machine learning), has made our domestic cyber landscape more complex, and our nation continues to experience cyber threats from an increasing number of sources. A rising dependence on digital technology within New Zealand’s economy and day-to-day life is also providing more opportunities for malicious cyber activity to affect more victims.

### State-sponsored malicious cyber activity and hacktivism

State-sponsored malicious cyber activity endures and primarily poses an espionage threat to New Zealand organisations. This year, the NCSC has observed a wider range of state-sponsored malicious cyber activity and some heightened activity from traditional adversaries.

While the number of incidents that can be linked to state-sponsored actors (110 incidents, or 32% of incidents of national significance) is up 8.5% on the previous year, it is broadly consistent with the proportion of recorded state-sponsored incidents over the previous five years. These have ranged from 33% in 2019/20, 28% in 2020/21, and 34% in 2021/22. An exception was a decrease to 23% in 2022/23.

New Zealand’s international relations, involvement in global organisations, technological innovations, and research, means our nation holds information that is likely of high intelligence value, and state-sponsored cyber actors continue to demonstrate the intent and capability to target us for its acquisition.

The tense geopolitical environment − including the rise of hacktivism, fallout from the Russia-Ukraine conflict, and acceleration of disruptive cyber capabilities − has almost certainly increased the cyber threat to New Zealand organisations. The NCSC has seen this reflected in cyber incidents in a number of ways, including an increase in Russian state-linked malicious cyber activity and pro-Russian hacktivists targeting multiple New Zealand government organisations.

> Hacktivism refers to the act of using digital techniques to gain unauthorised access to computer files or networks for politically or socially motivated purposes.

As more cyber threat actors enter this environment, it is becoming increasingly difficult to disassociate or attribute state and criminal cyber activity. A proportion of unattributed cyber incidents this year was likely also state-sponsored activity that could not be linked. Additionally, there is the potential that some criminal groups are being directed by states, or at least have tacit approval to conduct malicious cyber activity that aligns with state interests.

### Cyber-dependent and cyber-enabled crime

New Zealand is increasingly experiencing incidents in which sophisticated cyber criminals are using their capabilities and wider resources to scale their operations.

Ransomware has remained a persistent threat to New Zealand’s nationally significant organisations, smaller businesses and even schools. Disruption efforts, such as arresting actors and taking down infrastructure, have resulted in a decrease in financially motivated cyber incidents this year. However, it is expected that this will only be temporary as groups diversify and rebuild. Ransomware actors continue to take advantage of exfiltrated data to extort payment from their victims, increasing the potential for reputational and economic harm, and impact to critical services. Dominant ransomware players continue to successfully target high-profile victims. Extortion activity in New Zealand was not only limited to ransomware; victims also experienced disruptive distributed denial-of-service (DDoS) activity in lieu of encryption or data leaks.

The scale and impact of online scams and cyber-enabled fraud is rising in New Zealand, enabled through the growing use of social media and cryptocurrency. The compromise of business or corporate email accounts is of growing concern and is becoming increasingly profitable for criminals. This is because it enables cyber criminals to pretend to be trusted organisations, making it more likely for people to provide personal information. Victims are experiencing significant personal, reputational and financial harm as a consequence of this activity.

### Tradecraft and technology

The proliferation of cyber capabilities has lowered the barrier of entry for malicious cyber actors, providing access to more sophisticated skills and techniques. Offensive cyber tools and services (including spyware), once only available to well-resourced countries who could develop them internally, are now widely accessible to both states and cyber criminals. This growing availability of effective malicious cyber tools, compromised credentials, and vulnerabilities in public-facing infrastructure, has made it easier for malicious cyber actors to work at scale and with the ability to cause national-level harm in New Zealand.

Advancements in and adoption of these technologies is enabling the propagation of scams and other forms of cybercrime. In particular, the scale and sophistication of this enabling activity is likely to test the resilience of financial and identity systems as malicious cyber actors improve their ability to bypass security controls. Whilst controls such as multi-factor authentication (MFA) can mitigate against some of this activity, malicious cyber actors continue to develop tactics, techniques and procedures (TTP) that challenge these cyber security defences.

The use of large-scale data and credential breaches to enable malicious cyber activity is an ongoing trend. This year, the NCSC saw significant data breaches occur worldwide, some of which included New Zealanders’ personal information. An example this year was a publicly reported incident in which a finance company experienced a breach of customers’ personal identity and contact information. These breaches can subsequently allow actors to identify targets for phishing activity, or to directly compromise accounts: two of the most prolific and impactful forms of malicious activity experienced by New Zealanders.

Cyber threat actors’ success from social engineering use is increasing. This year social engineering was used across the sophistication spectrum: from scams against individual victims, to state-sponsored cyber actors using it to gain accesses for cyber espionage. What makes social engineering effective is its reliance on the human element, rather than technical vulnerabilities in software and systems. A wide range of malicious cyber and scam actors rely on social engineering and behavioural manipulation to convince a victim to act against their interests.

Cyber threat actors will likely continue to experiment with new tradecraft and technologies, but success does not necessarily rely on these. The threat to victims from simpler, long-standing methods − such phishing to deploy malware or vulnerability exploitation − is still prevalent across New Zealand’s domestic cyber threat landscape, from individuals to our nationally significant organisations.

The next section of this report illustrates how this cyber threat landscape translates into incidents recorded by the NCSC. First, the report outlines the key trends related to the 6779 incidents handled through the NCSC’s general triage process and the most common incident types. Then the report focuses on the 343 incidents of potential national significance and provides insight into the types of measures that could prevent these incidents from occurring.

---

## Incidents usually affecting individuals or small to medium businesses
Ngā whakaeke ā-ipurangi ka pā ki te tangata, ki ngā pakihi iti ki te waenga rānei

The majority of the incidents recorded by the NCSC affect individuals and small to medium businesses and organisations. Cyber criminals continue to prey on people’s increasing reliance on technology in their daily lives, as well as an absence of fundamental cyber security protections. Scams and fraud, phishing and credential harvesting, and unauthorised access were the most common types of incidents this year.

In total, NCSC recorded 7122 incidents in 2023/2024. The majority of these incidents, 6779, were handled through the NCSC’s general incident triage process because they did not require specialist technical attention. Often, these incidents impacted individual New Zealanders or small to medium businesses. While these incidents did not require specialist or intensive technical attention, they may be highly impactful for the people or organisations they affected.

The 6779 incidents handled through the NCSC’s general triage process was 12.5% lower than the previous year. For these incidents, scams and fraud, and phishing and credential-harvesting were the most common types of incident in this year. Both incident types generally rely on a person inadvertently taking actions that are part of malicious cyber activity. Most categories of incident experienced an overall decline from 2022/2023 figures, except website compromise and denial-of-service.

**565**

Average incidents per month.

**6779**

Incidents handled through the NCSC’s general triage process.

![Image description: Bar graph showing the number of incidents handled through the NCSC's general triage process in 2023/2024, broken down by category.]

2023/2024 incidents handled through general triage process affecting individuals, by category

- Scams and fraud 1894
- Phishing and credential harvesting 1498
- Unauthorised access 601
- Other 145
- Malware 66
- Website compromise 38
- Ransomware 10
- Denial of service 5
- Suspicious network traffic 3
- Command and control hosting 1

![Image description: Pie chart showing the percentage of all 2023/2024 incidents handled through the general triage process, broken down by category.]

All 2023/2024 incidents handled through general triage process, by category

- Phishing and credential harvesting 3455
- Scams and fraud 2045
- Unauthorised access 681
- Other 312
- Malware 131
- Website compromise 89
- Ransomware 37
- Denial of service 12
- Suspicious network traffic 9
- Botnet traffic 4
- Command and control server hosting 3
- Attack on a system 1

### Scams and fraud incidents

Of the 6779 incidents handled through NCSC’s general triage process in 2023/2024, 30% related to scams and fraud. Scams and fraud incidents rely on deceiving a legitimate user into doing something, rather than gaining unauthorised access to an account or system. Although the scams and fraud incidents included here are cyber-enabled, they can often only be prevented through the individual identifying them as illegitimate, as opposed to other cyber incidents which are cyber-dependent and can be prevented through cyber security controls. Incidents of scams and fraud includes fake investment ‘opportunities’ that are propagated over email, or online deals that are too good to be true.

> Cyber-enabled crimes are assisted, facilitated or escalated in scale by the use of technology.
>
> Cyber-dependent crimes can only happen on a computer, where the computer or the system is the target.

This incident type consistently features in the top three incident types reported. During 2023/2024, investment scams saw a 176% increase from the previous financial year (34 to 94 incidents). Extortion/blackmail scams increased from 119 to 136, although the reported financial loss decreased.

#### Case study: education sector incident

In August 2023, the NCSC became aware of reports of phishing coming from an organisation in the education sector. The NCSC let the organisation know they likely had a compromised email account. The organisation was then able to remove the malicious access to the compromised account. The NCSC also used the Phishing Disruption Service (PDS) to help organisations block the malicious website domain.

![Image description: Bar graph showing the number of incidents handled through the general triage process affecting organisations, primarily small to medium, by category.]

2023/2024 incidents handled through general triage process affecting organisations, primarily small to medium, by category

- Phishing and credential harvesting 190
- Scams and fraud 67
- Unauthorised access 57
- Other 32
- Website compromise 29
- Ransomware 21
- Malware 12
- Suspicious network traffic 5
- Command and control server hosting 2
- Denial of service 5
- Botnet traffic 2

Cyber security incidents targeting individuals remain a concern, despite lower numbers of reported incidents. With technology use pervasive within day-to-day life, whether people are buying and selling goods or pursuing career opportunities, threat actors are willing to identify and exploit opportunities to prey on people’s trust.

The NCSC provides general technical advice regarding scam and fraud incidents. Incidents that have potential financial or legal consequences, or where further action is required, are referred to New Zealand Police or other relevant agencies, with consent from the individual or organisation reporting.

### Phishing and credential-harvesting incidents

Phishing and credential-harvesting continue to be the most common incidents reported by organisations, despite a 31% decrease from the previous year. This category was the second-most common incident reported by individuals (after scams and fraud) despite decreasing by 19%. The prevalence of this incident type is largely due to its use ranging from unauthorised money transfer to ransomware.

The most common phishing impersonation theme was mail or package delivery, making up the vast majority of phishing emails and links. Other impersonation themes include government services, banks, and online shopping.

### Unauthorised access incidents

In 2023/2024, the NCSC handled 681 reports of unauthorised access through its general triage process. 601 reports impacted individual New Zealanders, and 57 reports impacted organisations – a 23% and 27% decrease from the previous year, respectively. A further 23 incident reports did not specify who they impacted.

A significant portion of these reports involve cyber threat actors gaining unauthorised access to social media accounts. For individuals, this frequently results in malicious messages being sent to their friends and family, spreading malware and furthering the distribution of scams. For organisations, this may include messaging customers as well as purchasing fraudulent ads to spread the same malware and scam messaging. The best ways to prevent unauthorised access include using long, strong and unique passwords, along with multi-factor authentication (MFA) to improve cyber security and reduce opportunities for malicious cyber actors to bypass security controls.

![Image description: Bar graph showing the breakdown of incidents in the scams and fraud category.]

Breakdown of incidents in the scams and fraud category

- Buying, selling or donating goods 1063
- A new job or business opportunity 199
- Investment scams 94
- Extortion or blackmail 136
- Dating and romance 160
- Unauthorised money transfer 114
- Ask to pay money upfront 40
- Cryptocurrency investment 61
- Fake government services scam 14
- Tech scam phone calls 75
- Buying, selling or donating services 31
- Scam phone calls 50
- Fake lottery, prize or grant scam 6
- Inheritance scam 2

---

## Incidents of potential national significance
Ngā mōreareatanga ka tūpono whaipānga ki te motu

A subset of incidents the NCSC responds to are triaged for more intensive technical support based on the nature of victim or incident. These incidents could cause high impact at the national level, and are referred to as incidents of potential national significance. This year there was an increase in the number of state-sponsored incidents. This increase is consistent with global experience of an increasingly adversarial cyber threat landscape.

An incident of potential national significance can include those that affect the systems and data of organisations in key sectors such as government, key economic generators, niche exporters, research institutions, or institutions that are important for New Zealand’s health and safety, economic wellbeing, international reputation, and democracy. Whether an incident is potentially nationally significant can also be determined by the NCSC’s understanding of the nature of the malicious actor responsible for the incident.

In 2023/2024, NCSC recorded 343 incidents of potential national significance.

While this figure is 8.5% higher than the previous year’s incidents, it is close to the yearly average of 353 recorded by the NCSC in the past five years. The proportion of incidents attributed to suspected state-sponsored actors and criminal or financially motivated actors has also remained relatively consistent over this five-year period.

**110**

of the 343 incidents that indicated links to suspected state-sponsored actors (32%).

**861,204**

Average MFN disruptions per month.

**65**

of the 343 incidents were likely criminal or financially motivated (19%).

**29**

Average incidents of potential national significance per month.

![Image description: Line graph showing incidents of potential national significance for the financial years 2019/20 to 2023/24.]

In 2023/2024, multiple organisations experienced similar malicious cyber activity around the same time. These incidents significantly increased the volume of total incident figures and were considered likely to be part of the same malicious cyber campaign. The groups of incidents were typically phishing campaigns or mass-exploitation of the same vulnerability. For example, in June 2024 the NCSC recorded six incidents of advanced, multi-stage adversary-in-the-middle (AiTM) phishing attacks targeting the health, education and government sectors. One of these incidents resulted in a breach where malicious actors were able to send 450 further phishing emails to contacts of the breached account. Sending phishing emails from a known individual or organisation can make it more likely for users to trust the email.

This financial year there was also an increase in the number of suspected state-sponsored incidents. An increase in state-sponsored malicious cyber activity is consistent with global experience of an increasingly adversarial cyber threat landscape and escalation in targeting of critical infrastructure. The NCSC assesses it is possible that a proportion of the 49% of unattributed cyber incidents may also have been conducted by state-sponsored actors but owing to technical or other constraints cannot be linked. This proportion is approximately consistent with previous years.

### The technical attribution process

The NCSC undertakes a technical attribution process to identify the actors responsible for malicious cyber activity, and the intent behind their actions. This process can inform and direct the NCSC’s own incident response and network defence efforts, as well as the advice the NCSC provides to affected organisations.

Technical attribution can also inform decision and policy makers, enabling them to understand the malicious cyber activity affecting New Zealand, including those responsible for the impacts. This technical attribution process can subsequently enable further response actions, including in the most significant cases using the attribution to contribute to the Government’s decision to publicly ‘call out’ the activity. The NCSC’s contribution to this process ensures that New Zealand has an independent, sovereign technical assessment that supports confidence in calling out malicious activity.

Incidents of potential national significance for the financial years 2019/20 to 2023/24

|                    | 2019/2020 | 2020/2021 | 2021/2022 | 2022/2023 | 2023/2024 | Average over 5 years |
| :----------------- | :-------- | :-------- | :-------- | :-------- | :-------- | :------------------- |
| Total incidents    | 352       | 404       | 350       | 316       | 343       | 353                  |
| Unknown            | 186       | 181       | 151       | 153       | 168       | 167.8                |
| State-sponsored    | 116       | 113       | 181       | 73        | 110       | 106                  |
| Criminal           | 50        | 110       | 81        | 90        | 65        | 79.2                 |

The NCSC categorises organisations into sectors following the Australian and New Zealand Standard Industrial Classification (ANZSIC) divisions from the Australian Bureau of Statistics. The public administration and safety division includes central government agencies, local councils, public order and safety services, and Defence.

Of the 343 incidents of potential national significance that the NCSC responded to, the 10 sectors affected by malicious cyber activity in 2023/2024 remained consistent with the previous fiscal year. The sector with the highest percentage of recorded cyber security incidents was again public administration and safety. Aotearoa New Zealand government organisations are commonly targeted for their access to sensitive information and data, which is reflected in this year’s increase in suspected state-sponsored cyber incidents, alongside the increasing global threat of the targeting of democratic institutions. Government sectors and regulated critical infrastructure also have reporting obligations, which means there is a higher rate of incidents reported for these sectors compared to others.

Incidents arising from the actions of financially motivated malicious cyber actors predominately involved organisations in the health care, information media and telecommunications sectors. The health care sector is a common target in financially motivated cyber activity, as disruption to critical services is more likely to increase the possibility of a ransom payment. Growing global connectivity and software supply chains also make it more likely that financially motivated ransomware incidents overseas could have indirect downstream effects for New Zealand organisations or critical services.

![Image description: Pie chart showing the top 10 sectors affected by incidents of potential national significance.]

Top 10 sectors affected by incidents of potential national significance

- Public Administration and Safety 39%
- Information Media and Telecommunications 12%
- Health Care and Social Assistance 9%
- Professional, Scientific and Technical Services 7%
- Education and Training 6%
- Financial and Insurance Services 4%
- Transport, Postal and Warehousing 3%
- Manufacturing 3%
- Electricity, Gas, Water and Waste Services 3%
- Administrative and Support Services 3%

To help understand the impact of any one incident, NCSC triages incidents affecting nationally significant organisations into categories, which consider the severity of the compromise and the size of the organisation impacted.

This year’s most severe cyber incidents were categorised C3. These C3 incidents were predominately associated with disruptive ransomware or other extortion activity. Other incident types within this category included the exploitation of public-facing applications and compromised networks or infrastructure. Organisations affected by these C3 incidents were in the education, government, media and telecommunications, transport, and energy sectors.

Another C3 incident included the targeting of a central government organisation by a sophisticated state-sponsored malicious cyber actor. Analysis revealed that a vulnerable perimeter device was exploited to gain initial access to the network. The NCSC assisted the victim organisation and its managed service provider to understand the scope of the intrusion, remove the intruder, and prevent further attempts to compromise the network. Prompt response efforts and work to identify the full path of the intrusion contained the compromise and reduced its impact.

Moderate (C4) and routine incidents (C5) increased in volume this year, consistent with the overall downward trend in the severity of impact experienced in New Zealand’s cyber incidents of potential national significance. Moreover, several incidents relating to the same vulnerability being exploited could be grouped as the same activity. For instance, in April 2024, the NCSC responded to a series of 10 incidents connected to a then zero-day vulnerability that could allow malicious cyber actors root access to systems using Palo Alto’s PAN-OS software. The NCSC observed attempted use of this vulnerability early and supported organisations’ remediation.

![Image description: Pie chart showing the impact of incidents of potential national significance.]

Impact of incidents of potential national significance

- C1 National Cyber Emergency 0
- C2 Highly significant incident 0
- C3 Significant incident 8
- C4 Moderate incident 90
- C5 Routine incident 169
- C6 Minor incident 76

#### Case study: networks compromised

In August 2021, the NCSC provided support to the compromise of computer networks associated with New Zealand’s Parliamentary Counsel Office and the Parliamentary Service by malicious cyber actors attributed to the People’s Republic of China (PRC), known as APT40. During the last three years, the PRC has demonstrated ongoing targeting of democratic institutions globally, and the targeting of critical infrastructure networks in the United States.

Following the March 2024 public announcement of the APT40 activity against Parliament, in July 2024 the NCSC joined partners to highlight evolving tactics, techniques and procedures of APT40. The actors had been observed using compromised small-office/home-office (SOHO) devices as operational infrastructure, and exploiting newly public vulnerabilities in applications and devices such as Microsoft Exchange, Atlassian Confluence, and Apache Log4j. Many of these SOHO devices, including in New Zealand, are unpatched or end-of-life devices left vulnerable to exploitation. Once compromised, SOHO devices can be used for attacks whilst blending in with legitimate traffic, subsequently presenting challenges for network defenders. APT40 continues to make use of compromised infrastructure and use available exploits within hours or days of public release.

This joint advisory served to raise awareness of and resilience to the tactics associated with a significant cyber threat to New Zealand and likeminded nations.

---

## The impact of ransomware
Te pānga o ngā pūmanawa tono utu

This year, Aotearoa New Zealand’s reported ransomware incidents declined significantly, despite global trends of ransomware being a pervasive and damaging cyber security threat. Even with a smaller number of incidents, it was still disruptive to those impacted, with ransomware actors incorporating a range of techniques intended to extort ransoms from victims including individuals, organisations, and government agencies.

### A year in ransomware incidents

Of the 7122 total incidents recorded during the 2023/2024 financial year, the NCSC responded to 46 ransomware incidents, approximately half the number of incidents compared to 2022/2023. Overall, the total number of ransomware incidents in 2023/2024 dropped considerably from previous years.

While the number of ransomware incidents has declined, the severity of impact from ransomware this year was still proportionally more than other cyber security incidents. In 2023/2024, 5 out of the 8 C3 incidents of potential national significance involved ransomware, or extortion/exfiltration which is often associated with ransomware events.

37 of the 46 ransomware incidents (80%) were not likely to cause nationally significant harm as they impacted smaller organisations or individuals. Ransomware actors likely select smaller enterprises and individuals alongside ‘big game’ targets, since these victims likely have less-mature cyber security capabilities. Emerging players enabled by ransomware-as-a-service are also capitalising on smaller organisations’ vulnerabilities to test their capabilities.

In many ransomware incidents where impact was less severe, this was mainly due to effective cyber security measures, including robust backups, automated cyber threat detection, and timely incident response. This is reflected in the following case studies about four ransomware incidents experienced by Aotearoa New Zealand organisations this year:

- In September 2023, the NCSC was made aware of a ransomware event affecting a New Zealand transport organisation’s card service for public transport services. The ransomware affected the system responsible for reconciling account balances with credit card data that facilitates users’ ability to top up their accounts. The NCSC provided the transport organisation with support and guidance to assist with the containment of this incident.
- In November 2023, the NCSC was made aware of malicious cyber activity that indicated ransomware on the network of a New Zealand organisation in the media and telecommunications sector. Subsequent investigation supported by the NCSC indicated the intrusion occurred via a vulnerable remote services tool with weak administration credentials. Due to robust backups (which were not affected) the organisation had the ability to restore the impacted file systems and data.
- In March 2024, the NCSC was notified of possible ransomware activity on the network of an organisation in the manufacturing sector. Access was likely via the exploitation of a known vulnerability in a remote service tool. After gaining access to the network, the actor was observed making attempts to copy sensitive credential databases. Early identification of the activity by a cyber threat detection tool on the network allowed the organisation to remediate the server before the ransomware was deployed.

> The NCSC recommends never paying cyber ransoms
>
> Governments worldwide are increasingly concerned about appropriate protection of sensitive data, including personal information, and are discouraging the payment of a ransom.
>
> In 2021, the New Zealand Government agreed that government agencies should not pay cyber ransoms. Paying ransoms encourages illegal activity and may fund other illicit activities. Payment of a ransom could also be in violation of the Russia Sanctions Act 2022 or the United Nations Act 1946.
>
> Payment of ransom does not guarantee that an organisation gets their data or systems back, and can result in the same organisation being targeted again, due to their willingness to pay.
>
> The New Zealand Government encourages all victims to report any cyber ransom incidents to the relevant agencies, regardless of whether a ransom is paid. The Privacy Act 2020 requires reporting of privacy breaches that have caused serious harm or are likely to do so.
>
> For more information see: ncsc.govt.nz/news/ransomware-advice

---

## Analysing trends in tactics and techniques
Te tātari i ngā ia rauhanga, tikanga hoki

Mapping recorded incidents to the MITRE ATT&CK® framework provides insight into common or emerging trends and can help defenders focus their security efforts. This section provides an overview of the three most used techniques in the 343 incidents of