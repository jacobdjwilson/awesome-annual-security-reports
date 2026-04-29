# Threat Monitor Annual Report 2023

**Organization:** NCCGroup  
**Year:** 2023  
**Website:** [nccgroup.com](https://nccgroup.com)

## Table of Contents
- [Foreword](#foreword)
- [SECTION 1 - Critical Events Timeline](#section-1---critical-events-timeline)
- [SECTION 2 - Incidents of Note](#section-2---incidents-of-note)
- [SECTION 3 - Law Enforcement Interventions](#section-3---law-enforcement-interventions)
- [SECTION 4 - Incident Response Findings](#section-4---incident-response-findings)
- [SECTION 5 - SOC Findings](#section-5---soc-findings)
- [SECTION 6 - Ransomware Threat Landscape](#section-6---ransomware-threat-landscape)
- [SECTION 7 - Threat Actors](#section-7---threat-actors)
- [SECTION 8 - Regions](#section-8---regions)
- [SECTION 9 - Vulnerability Landscape](#section-9---vulnerability-landscape)
- [SECTION 10 - Global Conflicts](#section-10---global-conflicts)
- [SECTION 11 - Threat Spotlight](#section-11---threat-spotlight)

---

## Foreword

In this year’s Annual Cyber Threat Monitor Report, we take a look back at the key events that shaped the cyber threat landscape in 2023, as well as looking ahead at the year to come, sharing insights from our Cyber Threat Intelligence team here at NCC Group.

2023 appeared to show signs that the international community is beginning to take the threats from cyber adversaries more seriously. We saw several examples of coordinated law enforcement action against criminal groups including key ransomware operators and individuals believed to be acting on behalf of foreign intelligence services. There was also consensus on the issue of ransomware, in that governments around the world have showed a united front against ransom payments and intelligence sharing through The International Counter Ransomware Initiative, which introduced several measures that offer a real opportunity to fight back against the pervasive threat from ransomware operators.

However, despite this, we saw the highest volume of ransomware victims NCC Group has ever recorded with an 84% increase in 2023 alone. The sheer volume of attacks and different types of victims proves that no organisation is safe. Notably, ransomware operators employed new and innovative techniques to maximize their profits, targeting big software creators and managed service providers. So, even if an organisation does not perceive a direct threat from ransomware, it should consider the potential impact on its supply chain.

The ongoing threat to critical national infrastructure across the globe by hacktivists and Foreign Intelligence Services continued in 2023, following on from multiple geo-political conflicts in the Middle East, Eastern Europe, and Asia. National Cyber Security Centres in multiple countries have highlighted this threat and it is something we are monitoring as a priority moving in to 2024.

With those few things in mind, here we give further insight into what was a challenging 2023, and what organisations should be focusing on in the year ahead.

**Matt Hull**  
Global Head of Threat Intelligence

---

## SECTION 1 - Critical Events Timeline

![Timeline of critical cyber events throughout 2023]

- **10th Jan - Ransomware: Royal Mail attack**: Royal Mail suffered 6 weeks of disruption to international postal services, affecting 11,500 Post Office branches. This was due to a LockBit affiliate driven ransomware attack, with Royal Mail refusing to pay the ransom.
- **30th Jan - Hacktivism: Killnet targets NATO countries**: Pro-Russian Hacktivist group, Killnet, launched DDoS attacks against US healthcare organisations and public healthcare sectors.
- **2nd Feb - Ransomware: GoAnywhere MFT Zero-Day exploited by CL0P**: Remote Code Injection flaw, CVE-2023-0669, on exposed administrative consoles of GoAnywhere secure web file transfer solution was shared by Fortra.
- **14th Mar - Surveillance: Russian state-sponsored TA targets EU diplomatic entities**: Nobelium, aka APT29 and Cozy Bear, targeted European diplomatic missions and systems sharing sensitive political information.
- **29th Mar - Supply Chain Attack: 3CX VOIP desktop client compromised**: North Korean threat actors compromised 3CX customers' critical infrastructure organisations within the energy sector using a trojanised version of the legitimate software.
- **14th Apr - Papercut: Ransomware Zero-Day**: Print Management Software maker, Papercut, announced RCE vulnerabilities in Papercut NG and Papercut MF, exploited by groups such as LockBit.
- **23rd May - Barracuda Zero Day Vulnerability**: Barracuda announced a zero-day vulnerability in their Email Security Gateway, CVE-2023-2868, leveraged by Chinese state-affiliated UNC4841 for espionage.
- **31st May - Ransomware: Move-IT Managed File Transfer vulnerability**: Progress released a security advisory regarding a Zero-Day vulnerability, CVE-2023-34362, used by CL0P to exfiltrate data.
- **11th Jul - Breach: Microsoft China Storm-0558**: Microsoft revealed that customer email accounts were accessed using Outlook Web Access (OWA) Exchange Online via forged authentication tokens.
- **8th Aug - Police Force Data Leak**: An FOI request to the Police Service of Northern Ireland led to a spreadsheet detailing the locations and names of serving employees being mistakenly made public.
- **31st Aug - Malware: Infamous Chisel**: NCSC and Five Eyes partners issued a report associating Infamous Chisel Malware targeting Ukrainian military Android devices with the threat actor, Sandworm.
- **20th Sept - FBI & CISA Advisory: Snatch Ransomware**: Advisory warning that Snatch threat actor group were targeting a wide range of Critical National Infrastructure (CNI) sectors.
- **27th Sept - Law Enforcement: Dual Ransomware Advisory**: FBI shared a Private Industry alert warning of an increasing trend of dual ransomware attacks.
- **27th Sept - Law Enforcement: US and Japanese warn of Chinese exploitation of Cisco Router Firmware**: BlackTech targeted government, industrial, and technology organisations by leveraging flaws in Cisco routers.
- **7th Oct - Ransomware: Caesars Casino**: Hackers exfiltrated data from the hotel and casino giant; they paid $US 15,000,000. Suspected actor: Scattered Spider (UNC3944).
- **7th Oct - Geopolitics: Hamas attack on Israel**: Palestinian group Hamas launched an armed assault against Israel, leading to significant regional conflict.
- **10th Oct - 23andMe Data Breach**: A credential stuffing attack allowed a threat actor to access 14,000 customer records, eventually scraping data from 6.9 million customers.
- **12th Oct - Ransomware: MGM Casino**: MGM suffered a ransomware attack including theft of customer data, costing the business approximately $US 100,000,000. BlackCat took responsibility.
- **12th Dec - Hack: Kyivstar Telco**: Russian threat actor, Sandstorm, disrupted Ukraine’s largest mobile network operator, leaving half the population without services for days.

---

## SECTION 2 - Incidents of Note

### Hybrid Warfare: Gaza conflict
The cyber threat landscape mirrored the Russia-Ukraine conflict with hacktivism at the forefront. Adversaries targeted Israeli infrastructure, primarily impacting the Availability vector of the CIA triad through Denial of Service (DoS) attacks, with a keen interest in Industrial Control Systems (ICS) and SCADA.

### Supply chains continue to be breached
- **Capita Breach**: In March 2023, Capita suffered a data breach impacting 90 organisations. The company suffered direct cyber incident costs of around £25m.
- **File sharing platforms**: Throughout 2023, platforms like Fortra’s GoAnywhere MFT and MOVEit were exploited, leading to the biggest data theft of 2023, impacting 62 million individuals.

### Data compromise: KidSecurity app
In September 2023, the KidSecurity app (1,000,000+ downloads) left user activity logs publicly available due to misconfigured Elasticsearch and Logstash collections, exposing 300 million records.

### Ransomware re-encryption: Henry Schein
In October 2023, healthcare giant Henry Schein suffered re-encryption of files after negotiations with Alphv stalled, causing two weeks of operational disruption and impacting 35,000,000 records.

### Royal Mail hit by LockBit
In January, Royal Mail halted international shipping due to a LockBit attack. They refused to pay the £66 million ransom, leading to the leak of 44GB of internal data.

---

## SECTION 3 - Law Enforcement Interventions

- **TrickBot**: Joint sanctions were levied against 11 individuals. Latvian national Alla Witte and Russian national Vladimir Dunaev faced charges for their involvement in the banking trojan.
- **Sanctions against North Korea**: The US Treasury sanctioned entities and individuals involved in sending IT workers abroad to generate revenue for the DPRK regime.
- **BreachForums and Pompompurin**: US authorities arrested Conor Brian Fitzpatrick, the owner of BreachForums, who pled guilty to conspiracy to commit access device fraud.
- **Ukrainian phishing ring**: Authorities apprehended members of a phishing ring responsible for stealing over £3 million from over one thousand victims across Europe.
- **LockBit affiliate arrested**: Ruslan Astamirov was arrested and charged in June for his role as an affiliate of the LockBit RaaS group.
- **EncroChat**: Following the 2020 compromise, over 6,500 arrests have been made, and nearly a billion euros in assets seized.

---

## SECTION 4 - Incident Response Findings

In 2023, the Financials sector observed the greatest percentage of incidents (15%), followed by Industrials (14%) and Government (14%). 

![Figure 1: Percentage of CIRT Cases by Sectors Impacted]

Analysis of attack categories found that most incidents concerned:
1. **Unauthorised Access** (36%)
2. **Phishing** (16%)
3. **Malicious Code** (15%)

---

## SECTION 5 - SOC Findings

NCC Group’s Global Security Operations Centre (SOC) reported 3,493 true positive incidents in 2023, a 36% increase from 2022.

- **Peak Activity**: July recorded the highest number of tickets (356).
- **Sector Targeting**: Academic & Educational Services were the most susceptible to incidents (810 recorded).
- **Escalation**: 82% of incidents did not require escalation, while 17% (588 cases) were escalated to the client.

---

## SECTION 6 - Ransomware Threat Landscape

2023 saw an 84% increase in ransomware cases compared to 2022 (4,667 vs 2,531). The mean number of attacks per month rose to 389.

- **Industrials**: The most targeted sector (32% of total).
- **Consumer Cyclicals**: 15% of total.
- **Technology**: 11% of total.

![Figure 8: Most Targeted Sectors 2022 vs 2023]

---

## SECTION 7 - Threat Actors

2023 saw a rise in the number of active threat groups from 55 to 64.

- **LockBit 3.0**: Remained the most prominent group, responsible for 1,039 attacks (nearly 32% of total ransomware activity).
- **BlackCat**: Saw a 200% increase in activity.
- **CL0P**: Rose to the 3rd most active group with 404 attacks.

![Figure 15: Top 10 Most Active Threat Actors in 2023]

---

## SECTION 8 - Regions
*(Content omitted in source text)*

---

## SECTION 9 - Vulnerability Landscape
*(Content omitted in source text)*

---

## SECTION 10 - Global Conflicts

### Russian Invasion of Ukraine
The conflict has seen increased attacks, though often with reduced impact due to improved defensive postures. Tactics include influence operations, hacktivism, and destructive operations.

### Israeli-Palestinian Conflict
The conflict has triggered a surge in hacktivist activity, primarily targeting Israeli infrastructure with DDoS attacks.

---

## SECTION 11 - Threat Spotlight
*(Content omitted in source text)*

[^1]: All financial figures are in the currency specified in the original report.

---

g received

a total of 68 attacks: just under 7% of the group’s

annual total.

44

 45
 45

Blackcat

Figure 20: Total BlackCat Attacks Month-on-Month 2022 vs 2023

Following on from their activity levels in 2022,

BlackCat displayed a consistently high activity level

BlackCat/ALPHV remains the second most active

throughout 2023, only missing being in the top three

ransomware threat group of 2023 (when considering

most active threat groups in four months of the year,

LockBit 2.0 and LockBit 3.0 as one evolved entity

though in those four months they were the fourth

instead of two separate ones).

most active threat group.

Their activity spiked over 100% from their activity

Though not as dominant, and with attack volumes

levels last year, rising from 215 attacks in 2022 to

still less than half of, LockBit BlackCat have shown

433 attacks in 2023.

a consistent level of activity throughout the year until

experiencing a dip in activity in December.

This more than doubling of attacks in real terms also

represents an increase in BlackCat’s proportional

This can likely be attributed to the temporary

share in the total ransomware attack volume, though

disruption which BlackCat/ALPHV’s leak site

only minorly from 8.5% share of the total in 2022 to

experienced in early December.

just over 9% of the total in 2023.

Sectors Targeted
BlackCat’s 2023 distribution of focus amongst

business sectors is only slightly different to what was

seen in 2022. Industrials remain the most targeted

sector with 142 attacks representing 33% of the

group’s total activity.

The second most targeted sector is, once again,

Consumer Cyclicals with 64 attacks representing

15% of the group’s 2023 activity. The third most

targeted sector in 2023, taking the place of 2022’s

Technology sector, is the Healthcare sector which

received 53 attacks, or 12% of their total activity for

the year.

Industries Targeted
The specifics of targeted industries within overall

sectors have also undergone a shift since 2022.

The most targeted industry remains Professional &

Commercial Services with 77 attacks, 18% of the

group’s yearly total.

The second most targeted industry is Healthcare

Providers & Services with 34 attacks, less than

half the total of those levied against Professional &

Commercial Services, representing 8% of the group’s

total. The third most targeted industry for BlackCat in

2023 was Software & IT Services, the industry which

was in joint-second position in 2022.

There has been much speculation about what

caused the 5-day disruption with some speculating

that it is the result of law enforcement interventions,

whilst the operators at BlackCat maintain it was

simply a hardware issue which is in the process of

being solved.

Members of BlackCat have had a turbulent career in

cybercrime: affiliates of the DarkSide group formed

BlackMatter upon DarkSide’s disbandment; affiliates

of BlackMatter helped to form BlackCat/ALPHV

in early 2022; and now LockBit 3.0 has started

to poach some affiliates of BlackCat and even

displaying some of BlackCat’s victims on their leak

This industry was attacked by BlackCat 31 times in

site (see LockBit section above).

2023, 7% of their total activity for the year.

46

 47

CL0P

CL0P favours identifying a weak spot in

organisational supply chains (preferably facilitating

file transfer / storage), developing an exploit, and

subsequently performing mass-exploitation over the

following month/s, and the numbers show that this is

indeed highly effective.

Going forward, we can expect this activity to persist

as it has evidently proven to be profitable for the

ransomware group, particularly in June and July with

the collective victim count of 261 likely enabling them

to have their subsequent four-month break.

Therefore, it is prudent for organisations of any

sector to consider their third-party security posture

and the exploitability of their supply chain, to avoid

becoming a victim of CL0P’s likely future excursion

into the supply chain.

Figure 21: Total CL0P Attacks Month-on-Month 2022 vs 2023

For a long time CL0P has been present in the

threat landscape, but their activity was particularly

notable in 2023 where being the third most active

threat actor over the course of the year and, in some

instances, the most prominent actor of the month.

With a huge 609% increase from just 57 attacks in

2022, which was 2% of the year’s total, to a much

more impactful 404 cases in 2023, which is 9%

of the total; CL0P have evidently stepped up their

game.

Despite being completely inactive for 33% of the

year (0 attacks), and conducting just 5 attacks or

less per month for another 42%, they have still

managed to come in third relying on their campaigns

carried out in March, June, and July (and also the

months in which the group was in first position).

Interestingly, as the readers of our Monthly Threat

Pulse will be aware, these seemingly random

spikes that can be observed in Figure 21 are in fact

representative of CL0P’s bespoke modus operandi

(MO) which distinguishes them from the majority

of other threat actors in the ransomware threat

landscape.

Between the GoAnywhere MFT vulnerability

(CVE-2023-0669), exploited by them on the 3rd

of February, and which significantly boosted their

March figures, and the MOVEit Transfer vulnerability

(CVE-2023-34362) exploited on the 31st of May,

affecting their June and July figures, we can begin to

outline their MO.

Sectors Targeted
In 2023, CL0P’s most targeted sectors were

In this case, Industrials will certainly be the most

targeted due to the sheer quantity of varying

Industrials with 108 attacks (27% of their total for the

industries that reside within, meaning a greater

year), followed by Technology with 80 (20% of the

percentage of organisations using these devices will

total), and finally Financials in third with 67 (17% of

exist within the Industrials sector.

the total).

Note that, unlike other threat actors in the

Industries Targeted
In terms of CL0Ps most targeted industries, in first is

ransomware threat landscape, CL0P’s targeted

Professional & Commercial Services with 67 cases

sectors are likely more circumstantial than those

(16% of their total for the year), followed by Software

of other groups, as their victims will be those

organisations that use the device that they are

& IT Services in second with 61 (15% of the total),

and finally Banking Services with 33 (8% of the total).

targeting.

48

 49

SECTION 08

REGIONS

Key

North America

Europe

Asia

South America

Undisclosed

Oceania

Africa

There are no deviations from the norm with regard

to the most targeted regions in 2023, with North

America, Europe and Asia occupying more than

80% of the pie chart, with the rest being fairly

evenly split between South America, Undisclosed,

Figure 22: Total Victims by Region in 2023

Oceania and Africa.

As can be seen in Figure 22, North America was the

As for the remaining regions; South America

most targeted region in 2023, accounting for 2330

experienced 214 cases (15%), Undisclosed had

attacks (or 50%), followed by Europe with 1300 (28%),

151 cases (3%) which accounts for those hacked

and in third we have Asia with 475 attacks (or 10%).

organisations whose names were not disclosed by the

As can be seen in Figure 22,
North America was the most
targeted region in 2023.

threat actors and therefore the regions unidentifiable.

Oceania suffered 108 attacks (2%), and finally Africa

saw 89 (2%).

Contrasting the situation with the top three, these

regions have stayed largely consistent with 2022,

Threat actors likely perceive these regions as wealthier

proportionately speaking, where South America

which thereby increases their targeting, consistently

contributed 5%, Oceania 3%, Africa 2%, and finally

making these three regions the most targeted.

just 9 undisclosed attacks (0%) as this was a new

technique at the time.

Notably, in 2022 the distribution of attacks between

North America and Europe was less disparate with

Something to extrapolate from this data is that the

them contributing 44% and 35% respectively, showing

extortive methodology of keeping victim names

that interest in the former has seemingly increased in

redacted does not seem to have been a passing fancy

2023.

and must be proving effective in pressuring victims, as

it now accounts for 3% of the year’s total.

In fact, relatively speaking, North America’s targeting

increased by 6%, even with the sizeable 84% increase

We expect this extortion technique to persist in 2024

in overall ransomware attacks in 2023.

and, if other threat actors begin to adopt it, we could

even see it increasing by 2024’s close.

As a result, Europe’s targeting decreased by 7% and

Asia’s decreased by 1%.

50

 51

SECTION 09

VULNERABILITY
LANDSCAPE

Exploiting vulnerabilities are a proven point of entry for threat actors. In this section we highlight

critical vulnerabilities that have been published during 2023 and enable readers to gain insights

into the dynamics of the vulnerability landscape.

According to NIST, 2023 saw a total of 29,065

exploited vulnerabilities with CVE-2023-0669, CVE-

vulnerabilities disclosed across the year compared to

2023-34362 and CVE-2023-27350 respectively.

25,083 in 2022 an increase of 3,982 in a year.

As the corporate world settles into a hybrid and

2023 were all from the year apart from CVE-2022-

remote working environment, the top three MITRE

41328 which is a Fortinet FortiOS vulnerability from

techniques exploited are exploitation of remote

a previous year still heavily exploited in the wild

services, exploitation of public facing applications

sitting at number 3 in the list.

Furthermore, the top ten exploited vulnerabilities of

and the exploitation for privilege escalation.

In addition, SentinelOne continue to see Fortinet

Additionally, of the disclosed vulnerabilities, less

FortiOS & FortiProxy (CVE-2018-13379), Microsoft

than 1% of them were continually exploited in the

Exchange Server (CVE-2021-34473, CVE-2021-

wild according to Qualys. With the increase in

31207, CVE-2021-34523) and Atlassian Confluence

remote work and AI seen this year, 3 in 4 security

Server & Data Centre (CVE-2021-26084, CVE-2022-

professionals also believe that the cyber risk of

26134) among other historic vulnerabilities being

organizations has increased.

routinely abused throughout 2023.

Furthermore, the reliance on supply chain security

This shows that organisations are not implementing

is also high on the agenda for organisations with 8

sufficient mitigation or remediation efforts to secure

in 10 saying there is an ever-increasing dependency

their digital estate from historic vulnerabilities

on good security postures of those in their supply

and shows the importance of an effective patch

chains according to SoSafe.

management programme to mitigate this threat.

Managed File Transfer platforms are a way for

2023 saw the rise of Artificial Intelligence (AI) and

organisations to securely share files and data with

Machine Learning (ML) with OpenAI’s ChatGPT

other parties.

becoming widely adopted in the mainstream. This

presents a variety of opportunities and challenges

They are usually more secure than other methods

for both malicious actors and defenders of digital

including the File Transfer Protocol (FTP) and email.

estates. The UK’s National Cyber Security Centre

Additionally, they are usually hosted in the cloud so

(NCSC) believes it has great potential but needs to

are scalable and efficient. These platforms are used

be built on secure foundations.

by organisations to share a variety of documentation

including contracts for new hires and for suppliers

The fast rise of the technology has created a new

and clients.

vulnerability in adversarial attacks. NCSC say there

are several methods for this attack including data

Therefore, these platforms have a vast array of

poisoning. Additionally, AI presents an opportunity to

data traversing them and could be seen as valuable

get ahead of the vulnerability before they are found

to malicious actors. In 2023, the vulnerabilities

because AI can spot insecure coding practices.

disclosed showed exactly this with data sharing

enabling platforms including MFT platforms such as

However, AI can be used maliciously to develop

GoAnywhere and MOVEit and print management

better phishing and malware capabilities.

solution PaperCut NG featuring in the Qualys top

52

 53

In 2019, 80% of cyber security decision-makers

expected AI to increase the scale and speed of

attacks and 66% expected attacks to evolve to

“conduct attacks that no human could conceive of”.

In 2023, security experts say this is already

happening with AI-enabled cyberattacks being an

issue that organisations are unable to cope with.

Those that leverage generative AI models such

as ChatGPT need to be aware of the trustworthy

nature of the coding packages it outputs as it can

be leveraged to spread malicious packages into

developer’s environments through data poisoning.

The stable trend of vulnerability disclosures in

Additionally, the known exploited vulnerabilities have

previous years seems to have come to an end.

stayed level with the previous years (2020-2023)

With the innovative security measure of BugBounty

during the COVID-19 pandemic (see Figure 24) and

programmes being adopted by organisations to find

prime opportunity to target the less secure home

excluding the spike during the remote working shift

vulnerabilities in their software and hardware before

worker.

adversaries, it encourages the ethical disclosure

of security vulnerabilities by security researchers

However, it would be reasonable to assume that

to vendors giving them chance to patch before

malicious actors will not disclose the vulnerabilities

exploitation occurs by malicious actors, enhancing

they are utilising to enable greater success on their

their security posture.

objectives.

Figure 23: Vulnerability Disclosures per Quarter 2019-2023

Figure 24: Known Exploited Vulnerabilities

Figure 23 demonstrates that NCC Groups 2022

This average is heavily weighted towards a high

Looking forward into 2024, it is highly likely the

Historic vulnerabilities will also continue to be

prediction that there would be an increase in

number of vulnerabilities during Q2 of 2023 (7150

number of vulnerability disclosures will continue

abused by adversaries as it is common knowledge

vulnerability disclosures was correct.

vulnerabilities) and the lowest number of critical

its upwards trajectory year over year given the

that not all organisations have an efficient patch

vulnerabilities being disclosed at 1132.

increase in BugBounty initiatives, and with global

management programme in place to successfully

2023 saw a substantial increase in vulnerability

governments understanding that increased

mitigate the threats these historic vulnerabilities

disclosures and was a record year compared to

If the anomaly of Q2 is excluded, then critical

disclosure could see increased exploitation attempts,

pose. Therefore, organisations should enforce an

2022 where the number of vulnerabilities disclosed

vulnerabilities as a percentage of disclosed

given greater awareness.

per quarter increased substantially up 38.5% on

vulnerabilities remains in a decline at 9% compared

actionable and appropriate patch management

programme to mitigate the risks posed by disclosed

average, beginning a continuous upwards trajectory

to 2022. It is noteworthy, that given the substantial

Additionally, generative AI will keep evolving and

vulnerabilities and ensure they are consuming and

seen in 2022.

increase in vulnerability disclosures, the number

help organisations improve their security posture

actioning relevant threat intelligence from mature

However, on average, per quarter the number of

at record levels with an average of 1295 critical

enhance their capabilities.

providers, to allow for a proactive approach to their

critical vulnerabilities disclosed was down 12%.

disclosures per quarter, up 21% year on year.

security posture.

of critical vulnerabilities being disclosed were still

whilst also being leveraged by malicious actors to

intelligence functions, be that internal or third-party

54

 55

SECTION 10

GLOBAL
CONFLICTS

In 2023, two key global conflicts saw cyber capabilities

work alongside kinetic warfare. Notably, Russia’s ongoing

invasion of Ukraine and the Israeli-Palestinian conflict.

Russian Invasion of Ukraine

Increased Attacks, Reduced Impact

In 2023, cyber-attacks against Ukrainian

Although cyber-attacks have not been the leading

attack method in this war, and have not met previous

conceptions of Russia’s reputation as a prolific cyber

infrastructure continued to be high; however, their

actor, they have certainly become part of the broader

sophistication and overall impact reduced.

military strategy on both sides.

In H1 2023, Ukraine’s State Service of Special

Communications and Information Protection of

As the war continues to unfold, it is likely that we will

continue to observe the exploitation of cyber powers

Ukraine (SSSCIP) identified a 123% increase in

alongside kinetic warfare against both Ukrainian and

registered incidents from H2 2022, however, the

Russian infrastructure.

growth of critical incidents had severely decreased

(-81%), and the ratio of high-level critical incidents

improved.

During this period, attackers appeared to place

greater emphasis on the likes of spray and pray

and phishing approaches versus sophisticated

techniques.

Influence and Information Operations

Particular emphasis was placed on Russian

influence and information operations against

Ukraine. Notably, espionage, surveillance and

intelligence gathering targeted the Ukrainian civic

sector with law enforcement a key interest.

With reduced innovation with respect to the

The likely suspected objective here being to

technology used and the methods employed, as well

ascertain information gathered by Ukraine, which

as an increasingly opportunistic rather than strategic

could be used to identify Russian war crimes.

approach, Ukraine’s defence has grown stronger.

Furthermore, Ukraine’s ability to bolster its security

Such evidence could assist in criminal proceedings

against Russian individuals and companies engaged

defences should not be understated.

in the war.

Prior hostilities between Ukraine and Russia, as well

as international and domestic support, have allowed

Ukraine to anticipate and build resilience against

Russian capabilities, contributing to their success in

2023.

Advanced Persistent Threat groups (APTs),

notably the Russian Federal Security Service

(FSB), the Main Directorate of the General Staff

of the Armed Forces of the Russian Federation

(GRU), and the Foreign Intelligence Service of the

Russian Federation (SVR), were identified as likely

Ongoing cooperation with international bodies such

responsible.

as the NATO Cooperative Cyber Defence Centre or

Excellence (CCDCOE), as well as private companies

The threat actors would often revisit previously

such as Microsoft, Google, Amazon, and ESET,

targeted victims, leveraging information accessed to

continue to fortify their defence.

conduct further operations.

56

 57

In addition, the SSCIP and CERT-UA found Russian

In the opposing corner, the IT Army of Ukraine

Global Impact

information operations also heavily consisted of

disrupted Russian Internet providers in territories

disinformation campaigns, identifying the Media

occupied by Russia, “Miranda-media”, “Krimtelekom”

sector as a key target, where targeting resources

and “MirTelekom”.

and or accounts.

Disinformation campaigns support Russia to

the increasing prevalence of non-traditional actors

Over the last two years, hacktivism has underscored

Whilst much of the events were concentrated in

Ukraine and Russia, the international nature of the

war has led to spill over effects also reflected by

cyber activity. Countries seen to support Ukraine

have continued to feel the wrath of Russian threat

undermine the truth, sow discord, and limit access to

participating in cyberwarfare, and war more

actors.

That said, Ukraine’s defence efforts remain strong,

and with continued collaboration with international

partners, the public and private sectors, the country

will continue to reinforce its cyber security strategy.

Going forward, an understanding of the key APTs

and hacktivist groups should support their defence

measures.

In addition to the above, destructive attacks were

also observed in 2023, predominantly conducted by

Overall, the international impact will likely see the

the Russian APT group Sandworm. These attacks

continued targeting of Ukrainian supporters, NATO

notably given the latter.

seek to eradicate targeted infrastructure to ensure

countries, and the spread of disinformation to boost

maximum chaos and destabilisation.

Russian backing.

timely and accurate information. By influencing public

generally.

opinion, Russia continues its attempts to undermine

confidence in Ukrainian policies and government,

Whilst this has taken the shape of both state-backed

and to destabilise international support for Ukraine.

and non-state-backed hacktivism, the latter has been

This is of course not new, as we have historically

observed Russia engage in widespread

Concerns regarding whether these groups may

disinformation campaigns, and we are likely to

have a greater appetite for attacks than known state

observe this as the war continues into 2024.

groups continue to be raised.

notably evident in both sides of the war.

Disruption and Hacktivism

Destructive Operations

Distributed Denial of Service (DDoS) attacks were

prevalent throughout 2023. From January to March

alone, DDoS accounted for 87.5% of all cyberattacks

recorded by the CyberPeace Institute.

From January to March alone,
DDoS accounted for 87.5% of
all cyberattacks recorded by the
CyberPeace Institute.

Whilst differing cyber threat actors are engaged in

DDoS, hacktivists on both sides, such as Russia’s

Killnet and Ukraine’s IT Army have remained active.

Notable events include KillNets’ DDoS attacks

against US hospitals in response to Western support

for Ukraine,  as well as their reported targeting of

NATO websites. Likewise, in collaboration with

groups such as Anonymous Sudan, believed to be

part of Killnet, Killnet threatened to target critical

banking infrastructure SWIFT, in response to

increased Western aid to Ukraine.

In December 2023, Ukraine’s largest

telecommunications provider Kyivstar was targeted,

destroying the core of the telecoms operator. The

Solnstsepek group, who are believed to be linked to

Sandworm, subsequently claimed the events.

This concerned one of the most destructive cyber-

attacks conducted by Russia against Ukraine since

the onset of the war, which as a result, left an

estimated 25 million subscribers without internet

connection.

The threat actors are reported to have been on the

network since May 2023, demonstrating how APTs

can often remain in systems undiscovered until the

moment of attack.

The events are being emphasised as a warning to

the West that no one is untouchable, and thus of

potential threats to come.

For example, Microsoft observed Cadet Blizzard

targeting Latin American and European companies,

Israeli-Palestinian Conflict

particularly NATO countries, providing military

support to Ukraine.

In addition, Russia’s disinformation campaigns

seek to garner support for the state beyond its

borders where spreading a pro-Russian narrative at

international scale. This has included narratives of

Western Russophobia, Ukrainian Nazi ideology and

the negative impact of Ukrainian refugees in Europe

spread via fake social media accounts.

The ongoing war between Israel and Palestine has

predominantly shed light on hacktivist activities,

although debate as to whether nation states are

already involved has been raised.

Certainly, there is the possibility that APTs may adopt

a more proactive role in cyber activity the longer

the war unfolds. Groups such as Cyber Avengers,

Cyber Toufan and Killnet have been prominent where

targeting Israeli infrastructure, demonstrating the

international element of the hacktivist community,

Equally, pro-Israeli hacktivists have also been

observed targeting Palestinian infrastructure, such

as Predatory Sparrow.

Summary

Overall, in 2023, cyber-attacks have remained an

Similar to Russia-Ukraine, we are observing

important tool alongside kinetic warfare for both

increasingly non-traditional actors adopt their

Ukraine and Russia.

position in war and provides food for thought where

considering the types of threat actors we may

As part of the broader military strategy, they support

increasingly see in future conflicts.

operations in the physical world where enhancing

disruptive and destructive capabilities, as well as

driving key information and influence operations.

Russia’s cyberattacks remained persistent, and

although their overall impact often not critical, nor

their levels of sophistication high, nonetheless the

attacks on Kyivstar served as a stark reminder that

detrimental attacks remain a possibility.

58

 59

SECTION 11

THREAT SPOTLIGHT
Ducks & Loaders: Life after Qakbot?

Law enforcement operations can have a severe

This annual Spotlight would like to take you for a fly-

and abrupt impact on the threat landscape, putting

by through our investigation of the loader landscape

pressure on threat actors to expand and adapt their

step by step, starting with getting cozy with our new

toolsets to minimize business interruption. Operation

malware friend Pikabot, continuing to the tall grass

Duck Hunt in 2023 that knocked an extremely prolific

hunt for more specimen like it, and the woes of

loader malware family, Qakbot, off its throne is one

collecting malware data from the Wild Wide Web.

of such changes.

Pikabot overview

This shift in landscape tends to attract the attention

of certain threat intelligence analysts; and so, due

Before embarking on looking for traces of Qakbot’s

to Qakbot’s popularity and its subsequent downfall,

competitor activity, we had to get up close and

these certain threat intelligence analysts at NCC

friendly with our potential targets in order to

Group became interested in proactively monitoring

understand how they tick and how to go about

potential increases in the usage of similar loaders.

looking for more.

Should Qakbot’s departure from the playing field

Pikabot is a new loader type malware that emerged

have left a vacuum, which competitor would rise up

in early 2023. In its early stages, the loader’s

to the challenge now that the tool’s infrastructure has

purpose was fetching additional malware. Like

been seized? And so, while law enforcement silently

Qakbot, the loader consists of three main modular

toiled to disrupt, we silently turned to digging.

components. The loader component is used to

drop secondary payloads on infected systems and

Loader malware is a pivotal, expensive, and powerful

downloads the malicious DLL.

entry vector that secures its place in the victim’s

systems. Loaders serve a wide range of other

The code injector is used to decrypt and inject the

malware operators (including other loaders), making

core module. Finally, the core module is responsible

sure that initial stages of crime run smoothly, making

for communicating with the C2 servers; retrieving

them high priority investigation targets.

and injecting malicious payloads from the C2;

After all, from the defending perspective, one would

In recent campaigns Cobalt Strike has been used

much rather close off the entry points for malicious

to facilitate the further compromise of the infected

activity as early as possible instead of dealing with

system and network.

executing remote commands and code injection.

the fallout within the core systems.

Our research preemptively started with a close

the distribution methods, campaigns, and malware

investigation of the Pikabot loader, a trojan that

behavior. E-mail thread hijacking is used to attempt

emerged in May 2023 that was deemed a likely

to lure the target to interact with a password

match for Qakbot.

protected ZIP file.

Pikabot shares similarities with Qakbot including

The new addition to the loader market exhibited

When this happens, curl is used to download

multiple resemblances to Qakbot from the beginning

Pikabot, which collects some basic level information

of its career. The eerily similar way both loaders

like the current user and system network details.

were spreading during their respective campaigns

by what is thought to be one specific affiliate by the

security research community.

60

 61

Anti-analysis analysis and main components

The loader

One of the fascinating and frustrating things about

Pikabot’s two-step infection chain would usually

new malware is keeping up with its changelog.

start with a ZIP attachment to an e-mail, that in most

Pikabot has been undergoing many frequent and

would execute the second stage upon interaction.

cases holds a JavaScript file (the loader itself) that

rapid changes in the past year, from improving

obfuscation techniques being used to the actual

The type of loader differs and can be presented as

processes executed, improving the anti-analysis and

HTA, IMG, PDF or LNK files, which slightly changes

detection evasion of the malware.

The frequency of changes could be attributed both

the upcoming steps, but the main goal remains the

same: getting a malicious DLL and executing it.

to the craftiness of the threat actors always on the

In most cases, the loader downloads the malicious

lookout for the best methods of avoiding detection,

DLL from an external server using the curl command.

but also to the fact that Pikabot is a relatively new

Next, the loader executes the resulting DLL using

malware.

rundll32.exe, usually by calling one of its export

functions. The name of the export function changes

Regardless of the driver, the steady output of

and might be Crash, Enter, vips, Excpt, or something

changes complicates tracking any malware, boosting

else entirely.

Pikabot’s evasion portfolio.

Figure 25: 1 Pikabot Infection Chain

The core module injector

The main functionalities are decrypting, injecting,

and executing the core module. Later versions

The core module usually contains anti-analysis code,

of the malware spawn a legitimate looking

specifically anti-debug and some virtual machine

SearchProtocolHost.exe process to inject the core

or sandbox checks, as well as flags for checking

module.

the user’s language to avoid infecting victims

The core module

whoami.exe /all

Unsurprisingly, the core module holds the very

  ipconfig.exe /all

center of the malware chocolate egg: the main

malicious functions of the loader.

  netstat.exe -aon

After another round of anti-analysis checks has

The gathered data is encrypted and subsequently

verified that it is safe to begin operations, the core

sent to a C2 server. The core module, safely nested

module will start gathering victim information.

in the victim system, can then start receiving target

specific commands from the threat actor and, for

Each victim gets assigned its own ID after which an

example, begin dropping other malware.

array of specifications on the user and computer are

queried in order to adjust the next steps.

Earlier infections show Pikabot successfully ferrying

penetration testing frameworks and other big

In newer versions of the malware, the following

malware into the victim systems like Cobalt Strike,

processes are spawned to collect more information:

IcedID, and DarkGate.

The Hunt
After having gotten up close and familiar with

The downside of multi-source hunting for entire

entities like full active malware does, however, come

Pikabot, we added it to our malware portfolio and

at a potential cost of loss of accuracy. Whatever

turned our sights to the next stage: collecting data

visibility we might gain could be compromised by

on the various loaders’ activities in the timeframe

noise or improperly set searches. To circumvent this

between Qakbot’s downfall and present time.

Our targets of choice, in addition to Pikabot,

were Danabot and DarkGate; solid and popular

and retain control over the process, NCC Group

analysts created multiple additional YARA rules to

hunt for Pikabot as a starting point.

competitors that had their own breakthroughs and an

If set up correctly, hunt progression would show

eventful 2023.

the following: a decrease in Qakbot’s activity, an

increase in the usage of Pikabot, and subsequent

In order to build a reliable landscape picture, we

increases in other loader popularity.

could not rely on internal data only.No analyst team

is an island, and cybersecurity’s strength lies in its

We focused on the most tangible indicators of a

collective community. The array of sources plugged

malware’s activity: capture samples themselves (the

into the sample collection stage included:

•  Desk research and previous publications.

most coveted clue), and command & control IOCs

that could be attributed to a specific malware family.

•  Crowdsourcing YARA rules for the malware

Packed samples (malware obfuscated by means of

  families within scope.

being compressed by other software) did not make it

•  Developing additional YARA rules for Pikabot

into our analysis due to having to hunt for the various

  specifically.

packers used, and out of concern for introducing

in Commonwealth of Independent States (CIS)

In even newer samples, SearchFilterHost.exe is

countries, depending on the operator.

used instead.

•  Performing retrohunts using the outputs above.

data duplications.

•  Verifying all Pikabot samples manually.

62

 63

Tally-ho!

The hunt culminated in 3 graphs for us to dissect: one focusing solely on
the sample sightings, and two outlining the C&C numbers.

Finding one: confirmation

The unsurprising but not unwelcome first find among

May, though it is also unknown how long Operation

the collected numbers: the Qakbot’s takedown is not

Duck Hunt was active for, and what kind of effects

shy about showing itself through a glaring lack of

covert interference might have on these results.

This may account for the odd dip in IOCs following

samples and Qakbot related infrastructure IOCs in

the collected findings.

Qakbot was observed decreasing activity and

working on their internal infrastructure during the

summer months.

Figures 26 and 27 show Qakbot’s dominance and

subsequent downfall during Operation Duck Hunt.

Figure 26: Retrohunt Results for 2023

Figure 27: Command & Control Servers for 2023

Finding two: coronation
As for the alleged competitors, Pikabot emerges

For ‘commercial’ malware (i.e. advertised and

distributed through underground forums and chatter

as the current market leader according to our data.

as opposed to kept in smaller teams), this is further

Congratulations, Pikabot!

intensified since more operators could potentially

make use of the updated malware versions, resulting

in higher detection (sharper rise) on the graphs

simply due to higher numbers involved in the attacks

Finding three: peaks and valleys

that will then get detected.

Sudden ebbs and rises in the data graphs may

Correlations between the developments we currently

seem jagged at a glance, but most tend to have a

know of within the presented malware families and

logical explanation: we simply do not expect smooth

their detection numbers indicate a change-detection

progression from malware tracking due to the nature

lag of ca 3 weeks.

of collecting samples and indicators.

As new versions of malware are pushed by the

May and November correlate neatly with Pikabot’s

threat actors, detection on the defending side

technical evolution steps and new features added.

needs time to improve and develop, a process not

Danabot upgraded to version 3 in July, moving the

represented by a smooth and gradual line.

detection ticks upwards the next month.

For the collected samples (Figure 26), the peaks in

64

 65

Some sharp increases and decreases may

Several threat intelligence providers have observed

The danger of statistics

have other internal explanations requiring us to

and reported on small-scale campaigns involving

corroborate sources. DarkGate related IOCs taper

Qakbot in December, indicating the project may be

off quite aggressively after their October peak,

severely hamstrung but perhaps not down for the

As much as we would love our findings to be

irrefutable, there is always a risk with using

•  Public YARA rules used to hunt for samples

  were selected from the sets with proven

  accuracy and a low false positive rate.

though there are no conclusive reasons for this.

count.

increasingly large datasets collected from third party

•  C&C selection was based on a confidence

sources to make trend explanations and predictions.

  threshold with a high score (75 to 100) assigned

One hypothesis is the noted difficulty in crypting

As no arrests were made it is possible that the

  by the submitters.

DarkGate – obfuscating the malware so that it may

development team behind Qakbot were able to set

Ultimately, confidence scores assigned to C&C

be delivered to target systems undetected – on

up their infrastructure and resume operations.

related IOCs or reliability of YARA rules developed

Unfortunately, even imposing constraints and

underground forums.

by someone else will always decrease reliability of

reducing scope does not entirely remove the risk

If this were the case, it would account for the

findings – in addition to the fact that investigated

of duplicates if the same infection was captured

This issue came to light in December 2023, which

November and December uptick in samples and

targets are criminal tools developed in a notoriously

using different methods that could potentially result

resulted in the DarkGate’s developer offering to

IOCs seen in figures 26 and 28.

non-transparent setting. In order to keep the results

in multiple entries describing the same event from

crypt the malware for customers at the cost of USD

5000 and recommending a crypting service costing

upwards of an impressive USD 10000.

These additional costs to an otherwise very

expensive malware (a monthly license easily costs

USD 15000) may have influenced the ongoing

operations and sourcing of additional customers.

Figure 28: Command & Control Servers for H2 2023

as tightly controlled as possible, we have set the

different angles.

following hard criteria to minimize noise:

Wrap-up

catalysts for the developer teams behind DarkGate,

Danabot, and Pikabot to push their products to the

2023 has been a turbulent and exciting year in the

public, the result is the same: it would seem we have

loader microcosm. Like avid birdwatchers, threat

traded Qakbot for at least three worthy challengers

analysts have keenly observed new families rise and

that have taken the last two quarters of the 2023 by

develop, taking their place among the names in our

storm.

monitoring.

For the recipients of the report, unfortunately, this

threat actors to pick the instruments for the job with

means that new threats have grown and settled into

more ease.And so, we go excitedly into 2024 armed

the landscape within an impressive timeline.

with the knowledge that the hunt has just begun.

Diversity in the choice of tooling allows multiple

Despite Qakbot’s dramatic downfall, it would seem

Further research into the activity relating to other

there is not one specific competitor that has shown

loaders may further illuminate the dynamics of the

alarming levels of activity to fill the vacuum of its

current landscape..

absence. On the contrary, several strong players

ended up developing new toolsets and capabilities,

providing a steady increase in the loader market.

Regardless of the internal drivers that acted as

66

 67

About us

NCC Group is a global cyber and software
resilience business, operating across multiple
sectors, geographies and technologies.

As society’s dependence on the connected
environment and associated technologies
increases, we use our global expertise to enable
organisations to assess, develop and manage
their cyber resilience posture to confidently take
advantage of the opportunities that sustain their
business growth.

With circa 2,400 colleagues, we have a
significant market presence in the UK, Europe
and North America, and a growing footprint in
Asia Pacific with offices in Australia, Japan and
Singapore.

+44 (0)161 209 5200
response@nccgroup.com
www.nccgroup.com

68