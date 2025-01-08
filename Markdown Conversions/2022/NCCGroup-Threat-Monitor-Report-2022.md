# NCC Group Annual Threat Monitor 2022

## Table of Contents
- [Foreword by Matt Hull, Global Head of Threat Intelligence](#foreword-by-matt-hull-global-head-of-threat-intelligence)
- [Critical Events Timeline](#critical-events-timeline)
- [Incidents of Note](#incidents-of-note)
  - [Russia’s FSB arrest REvil gang members & seize assets](#russias-fsb-arrest-revil-gang-members--seize-assets)
  - [Russia Invades Ukraine](#russia-invades-ukraine)
  - [Predatory Sparrow attack on Iran Steel Plant](#predatory-sparrow-attack-on-iran-steel-plant)
  - [Clop targets UK water supplier](#clop-targets-uk-water-supplier)
  - [Optus of Australia PII data breached](#optus-of-australia-pii-data-breached)
- [Law Enforcement Interventions](#law-enforcement-interventions)
  - [Lapsus$ arrest](#lapsus-arrest)
  - [US authorities shut down RaidForums](#us-authorities-shut-down-raidforums)
  - [US Government offer Reward for Conti Information](#us-government-offer-reward-for-conti-information)
  - [Spanish National Police arrest 55 members of the Black Panthers sim swap gang](#spanish-national-police-arrest-55-members-of-the-black-panthers-sim-swap-gang)
  - [FBI warn that search engine advertisement services are being used to distribute malware](#fbi-warn-that-search-engine-advertisement-services-are-being-used-to-distribute-malware)
- [Incident Response Findings](#incident-response-findings)
  - [Sectors](#sectors)
  - [Attack Vectors](#attack-vectors)
  - [Impact Stages](#impact-stages)
- [SOC Findings](#soc-findings)
- [Ransomware Threat Landscape](#ransomware-threat-landscape)
  - [Sectors](#sectors-1)
    - [Industrials](#industrials)
    - [Consumer Cyclicals](#consumer-cyclicals)
    - [Industries](#industries)
    - [Technology](#technology)
    - [Industries](#industries-1)
  - [Threat Actors](#threat-actors)
    - [Lockbit](#lockbit)
    - [BlackCat](#blackcat)
    - [Conti](#conti)
    - [BlackBasta](#blackbasta)
  - [Regions](#regions)
- [DDoS Threat Landscape](#ddos-threat-landscape)
  - [Geography](#geography)
  - [Attack Durations](#attack-durations)
  - [Exploited Protocols](#exploited-protocols)
  - [Conclusion](#conclusion)
- [Vulnerability Landscape](#vulnerability-landscape)
- [Ukraine-Russia War](#ukraine-russia-war)
- [Threat Spotlight: Hydra Malware](#threat-spotlight-hydra-malware)
  - [Introduction](#introduction)
  - [Credential-stealing Features](#credential-stealing-features)
  - [New features Stealing Cookies](#new-features-stealing-cookies)
  - [Hydra Variants](#hydra-variants)
  - [C2 Server Analysis](#c2-server-analysis)
  - [Conclusion](#conclusion-1)
- [Threat Spotlight: SEO Poisoning](#threat-spotlight-seo-poisoning)
  - [Recent cases of SEO Poisoning](#recent-cases-of-seo-poisoning)
  - [BATLOADER](#batloader)
  - [Conclusion](#conclusion-2)

---
# NCC Group
Annual Threat Monitor 2022
nccgroup.com

## Foreword by Matt Hull, Global Head of Threat Intelligence

In what is only our second Annual Threat Monitor Report, we are pleased to share some of the insights and knowledge of our ever-growing Global Threat Intelligence team here at NCC Group. Working closely with teams across the organisation from our incident response, security operations, public affairs, risk management and security testing teams, we provide an overview of the events across 2022 that profoundly impacted the Cyber Threat Landscape.

We also look ahead to the year to come. This knowledge will of course enable us to inform the decisions that allow organisations of all sizes to prepare, prevent, detect and respond to the ever-evolving cyber threat.

In 2022, the threat landscape was heavily influenced by the conflict between Russia and Ukraine. We saw the whole arsenal of offensive cyber capabilities being deployed not only by these two countries, but around the world. Criminals, hacktivists, and even other nations made use of techniques in support of either of the countries. From the disruptive use of disinformation, defacement, and Distributed Denial of Service attacks to the deployment of destructive malware, which crippled critical national infrastructure in Ukraine and beyond.

The criminal ecosystem was also partly influenced by the conflict as it caused global economic uncertainty. The threat from ransomware persisted, and no organisation was safe, be it a university, large health insurer, telecommunications company, or even National Governments. All fell victim to a host of well-established ransomware operators and the access brokers that support their business.

The successes of criminal groups were also met by the ever-strengthening response to cyber threats by global governments and law enforcement agencies. Several coordinated operations resulted in the arrests of key members of prolific cyber-criminal groups and intelligence operatives. The second ‘Counter Ransomware Initiative’ also took place, showing that countries around the world were willing to support an International Counter Ransomware Task Force. Some countries have even sought to take a hard-line approach, preventing the payment of ransoms.

Looking forward to 2023, it is highly likely that the threat from ransomware will persist. Some ransomware operators have shown repeatedly that they are effective innovators and will find any opportunity to extort money from their victims. However, organisations are able to reduce the risk of ransomware by ensuring that they are well prepared for an incident, with robust back-up processes and incident response plans. A lot is known about the common Tactics Techniques and Procedures used by these criminal groups, so using timely threat intelligence can help organisations tailor their security controls.

For the second year running, we saw that the industrials sector was the most targeted by criminal gangs, especially ransomware operators. We also saw Nation States flex their muscles, targeting operational technology (OT) environments. As such, there are growing concerns around organisations that operate as part of a country’s Critical National Infrastructure. It is likely that organisations in this sector, particularly those with large OT or IoT estates will come under continued targeting.

So, there we have it. A short look back at the last year, and a glimpse in to 2023. But of course, you will find much more detail in the rest of our Annual Threat Monitor Report. We hope you find it useful.
In the blink of an eye, 2022 was over… and was yet again, another year that kept us on our toes.
2022 NCC Group Annual Threat Monitor
4

## Critical Events Timeline
The timeline highlights major incidents that shaped the global threat landscape during 2022

### 14 January
Ransomware
**Russia’s FSB arrest REvil gang members & seize assets**
In a rare move, Russian authorities publicly announced the arrest of alleged members of the REvil cyber crime group. Interestingly this occurred in the midst of growing tensions between Russia and Ukraine and calls from the international community to de-escalate.

### 27 February
Ransomware
**Conti Ransomware member leaks details about the group**
Following the invasion of Ukraine by Russia, the Conti group pledged support for the invasion. However, a Ukrainian member of the cybercrime group called out against this and ultimately revealed the inner workings of the group’s infrastructure and business model.

### January
Data Leak
**Leading identity and access management provider, Okta, breached**
The LAPSUS$ data extortion group broke into the company’s internal systems in January 2022 after obtaining remote access to a workstation belonging to a support engineer.

### 24 February
Geopolitics
**Russia Invades Ukraine**
Following escalations in both the physical and digital space, Russian ground forces invaded Ukraine on the 24th February. The invasion was preceded by the deployment of wiper malware against key Ukrainian public services, government and Critical National Infrastructure.

### February
Nation State
**Satellite provider impacted by wiper malware**
Although announced later, in an effort to hamper Ukraine’s capabilities in the early part of the invasion, Russian operatives successfully targeted the American satellite company Viasat using the destructive wiper called AcidRain.
2022 NCC Group Annual Threat Monitor
6

### 24 March
Law Enforcement
**Lapsus arrest**
Police in the UK arrest seven people between the ages of 16 and 21 with suspected connections to Lapsus$. The arrests came shortly after security researchers revealed that the mastermind behind the group was a 16-year-old living with his mother in Oxford, UK.

### 18 March
Nation State
**Lapsus vs Nvidia**
In its second big news story of 2022, the data extortion group Lapsus$ announced that it had gained access to and stolen up to 1Tb of Nvidia proprietary data.

### 29 March
Nation State
**Eastern European satellite navigation and communication systems jammed**
Following an alert from the FBI and CISA regarding the possible threat to satellite communications, the European Union Aviation Safety Agency (EASA) warned of satellite jamming and spoofing attacks across a broad swath of Eastern Europe that could affect air navigation systems.

### April
Nation State
**Ronin Network sees $540 million in crypto assets stolen by Lazarus Group**
In an apparent social engineering attack, the Lazarus Group, which in recent years has focused its attention towards DeFi services, was able to steal and launder approximately $540 million.
2022 NCC Group Annual Threat Monitor
7

### April
Ransomware
**Conti attack against Costa Rica Government**
The Costa Rica Government was forced to declare a ‘state of emergency’ following a successful series of ransomware attacks by Conti which crippled many of the country’s essential services.

### May
Ransomware
**Conti disbands**
Following a period of turmoil for the renowned ransomware group it became clear that the gang was disbanding from their known guise of Conti. Reports and research surfaced soon thereafter, indicating that splinter-cells had begun to operate using similar TTP’s.

### 01 April
Vulnerability
**Spring4Shell (CVE-2022-22965)**
Disclosed by VMWare, Spring4Shell is a critical vulnerability (CVSSv3 9.8) targeting Java’s most popular framework, Spring. The Spring4Shell vulnerability allows attackers to execute arbitrary code on the application server where a number of pre-requisites are met.

### 12 April
Law Enforcement
**US authorities shut down RaidForums**
A multi-agency operation orchestrated by Europol saw the administrator and supporting members of the RaidForums site arrested and the site’s infrastructure shut down.

### 19 May
Nation State
**Chinese APT targets Russian-owned defence institutes**
In an interesting twist, researchers identified several campaigns by Chinese APT groups conducting espionage against their Russian allies that were believed to have been ongoing since the summer of 2021.
2022 NCC Group Annual Threat Monitor
8

### 03 June
Vulnerability
**Confluence (CVE-2022-26134)**
Atlassian warned of a critical unpatched remote code execution vulnerability which impacted Confluence Server and Data Center products. This vulnerability was quickly weaponised and was seen to be actively exploited in the wild.

### 27 June
Nation State
**Predatory Sparrow attack on Iran steel plant**
The terrifying potential of an attack against an OT environment was realised in June this year. The threat actor ‘Predatory Sparrow’ was able to demonstrate the true impact of a cyber-kinetic attack, which resulted in a large fire in an Iranian steel plant.

### 06 June
Ransomware
**BlackBasta group uses QBot malware for initial access and persistence**
In an interesting evolution of TTPs, NCC Group researchers identified the use of the long-standing information stealer, Qakbot, being deployed for lateral movement by the BlackBasta ransomware group.

### July
Cyber Crime
**Verified Twitter account takeovers**
In a series of social engineering campaigns, malicious actors were able to take control of ‘verified’ Twitter accounts. Account takeovers, or cloning, has been a successful tactic in Business Email Compromise campaigns over the last couple of years.
2022 NCC Group Annual Threat Monitor
9

### August
Law Enforcement
**Conti doxed by US**
Lawmakers in the US revealed personal details and pictures of key Conti members, as well as releasing ‘wanted’ posters in an effort to track down and bring the group’s members to justice.

### 22 September
Data Breach
**Optus of Australia had PII belonging to millions of customers breached**
Australian Telecom’s giant Optus revealed that the personal information of approximately 10 million customers had been exposed in a data breach. The data which was reportedly accessed through an exposed API, had been posted on a data breach forum and was later removed by the attacker along with an apology.

### September
Nation State
**China accused NSA of numerous cyberattacks**
In a series of back-and-forth reports, China announced (via a report published by China’s National Computer Virus Emergency Response Centre), that the US National Security Agency has accessed the personal data and the

### 02 September
Ransomware
**BlackCat/ALPHV target Italian energy company**
A further example of the targeting of critical national infrastructure by criminal groups in 2022. BlackCat/Alphv also had a number of successes impacting energy and gas suppliers in Germany and Luxembourg.

### October
Data Leak
**Medibank**
The personal data of over 9.7 individuals was exposed following a Ransomware attack against Australia’s largest health insurance provider. The attack has led to renewed collaborative action against ransomware operators by world leaders and law enforcement.

### August
Ransomware
**Clop targets UK water supplier**
CloP publicised their successful targeting of South Staffordshire Water (initially believing the organisation to be Thames Water, before correcting their error). Although there was no indication that Cl0p had affected the water supply itself, the water company did confirm that the data of customers who pay their bills via direct debit had been compromised and subsequently shared on the dark web.
2022 NCC Group Annual Threat Monitor
10

### October
Law Enforcement
**Raccoon Stealer operator arrested**
A 26-year-old Ukrainian national was arrested in the Netherlands for the part he played in developing and selling the popular Racoon Stealer information stealing trojan, which was distributed under the Malware-as-a-Service model.

### 02 December
Law Enforcement
**Spanish National Police arrest 55 members of the Black Panthers sim swap gang**
The ultimate goal of the gang was to perform SIM swapping attacks, which is to port a target's phone number to the attacker's device. By porting the number, the attackers gained access to the victim's text messages and used these to bypass 2FA protection on their bank accounts. This resulted in loses to customers in the region of quarter of a million pounds.

### 03 November
Cyber Crime
**Crimson Kingsnake targets law firms**
Business Email Compromise (BEC) is a fraudulent cyber crime relying on spoofed emails and websites and broader social engineering. The aim, to divert funds into the criminal’s accounts, usually by sending false invoices or posing as a senior member of staff in the organisation. Crimson Kingsnake were one of the more prolific groups of 2022, a year where some reports suggested BEC attacks increased by 85% on the previous year.

### 11 November
Vulnerability
**Citrix Gateway and Citrix ADC authentication bypass**
Several vulnerabilities affecting Citrix platforms, allowing remote, unauthenticated attackers to take control of a vulnerable system.

### 21 December
Law Enforcement
**FBI warn that search engine advertisement services are being used to distribute malware**
In a series of attacks aimed at deploying ransomware and stealing user credentials, some criminal gangs were seen to be purchasing advertisements that appear within internet search results using a domain that is similar to an actual business or service. These advertisements appear at the very top of search results with minimum distinction between an advertisement and an actual search result.
2022 NCC Group Annual Threat Monitor
11

## Incidents of Note

### Russia’s FSB arrest REvil gang members & seize assets

In early January, Russia’s FSB (Federal Security Service) responded to US Government requests for the arrest and extradition of REvil gang members. Footage of the arrests was shared by the FSB, which showed a montage of short clips of the raids taking place. This included imagery of large quantities of cash, various laptops, and Bitcoin assets, all allegedly controlled by the group.

The REvil gang became well known following a number of significant attacks in 2021, such as the Kaseya supply-chain ransomware attack affecting the computers of thousands of organisations, and the world’s largest meat packing company, JBS SA of Brazil.

Although subsequent imagery of alleged REvil members being held in custody was shared online, none were known to have been extradited to the USA.

The timing of the arrests made by Russian authorities came at a point in time when Russia was preparing for war. Some argued that the arrests were to garner favour with Western countries in the run up to the invasion of Ukraine. Interestingly, REvil resumed operations in October 2022. It is yet to be determined whether those arrested in January are back in action, or whether the arrests were a ruse.

### Russia Invades Ukraine

One of the most notable events of 2022 was the invasion of Ukraine by Russian forces. Analysts in the public space had alluded to an impending act by Russia in the weeks and months leading up to the invasion, using OSINT and IMINT of military hardware being moved towards Ukrainian borders. Moreover, cyber-attacks such as wiper malware had also been deployed against Ukrainian infrastructure.

You can find further commentary on the Russian invasion of Ukraine later in this report.
> One of the most notable events of 2022 was the invasion of Ukraine by Russian forces.
13
2022 NCC Group Annual Threat Monitor

![Image description] Iranian Steel Company Cyber-kinetic Attack

### Predatory Sparrow attack on Iran Steel Plant

The group known as Predatory Sparrow, aka Gonjeshke Darande, poked their head above the social media parapet in October of 2021, describing themselves as a hacktivist organisation from within Iran. Interestingly, the group also took responsibility for the cyber-attack against the Islamic Republic of Iran Railway organisation.

Similar attacks affecting Iranian infrastructure continued into 2022, with the most notable being the attacks on Khouzestan Steel Company, Mobarakeh Steel Company and the Hormozgan Steel Company. Predatory Sparrow claimed that the acts were conducted against these organisations due to their affiliations with the Islamic Revolutionary Guard Corps (IRGC) and the Basij (Iranian volunteer paramilitary militia). Both military organisations had previously been added to the terrorist watch lists of the US, Saudi Arabia, and Bahrain. CCTV footage from inside one of the plants was also released by the group, showing the impact of their cyber-kinetic attack as it took place.

Research indicates that the group may be a front for an Israeli actor, given their targeting and capability; however, this has not been corroborated.

The conflict between Iran and Israel is extensive and long running. Improvements in the development of Iranian nuclear capabilities continues to raise alarms within the intelligence and security agencies of Israel, but also amongst allies such as the USA and Saudi Arabia.

> We expect that OT environments will continue to be a priority target for a plethora of threat groups over the coming years, and as such, the security of which should be an area of investment.
14
2022 NCC Group Annual Threat Monitor

### Clop targets UK water supplier

In August 2022, the Clop crime group publicised their successful targeting of South Staffordshire Water (initially believing the organisation to be Thames Water, before correcting their error).

Although there was no indication that Clop had affected the water supply or the industrial control systems used by South Staffordshire Water, the water company did confirm that the data of customers who pay their bills via direct debit had been compromised and subsequently shared on the dark web.

The precise number of effected customers is not clear; however, the data obtained by the criminal group is thought to exceed 5TB.

Security researchers investigating the incident indicated that within the data leak were spreadsheets containing internal system IP addresses and passwords. Many of these passwords were reportedly re-used across multiple services in use within Staffordshire Water. Fortunately for Staffordshire Water, there has been no evidence that these credentials have been used for further attacks.

Password re-use and the sharing of passwords internally in this manner has proven to be a quick win for various network access brokers. Passwords of employees, service accounts and so forth are more readily available to attackers than most organisations realise. These passwords can be used to log in to remote services, allowing attackers almost direct access to critical systems and data.
> The Australian telecoms company Optus publicly acknowledged a data breach of its systems affecting 10 million customers in September 2022.

### Optus of Australia PII data breached

The Australian telecoms’ company Optus publicly acknowledged a data breach of its systems affecting 10 million customers in September 2022. This vast trove of data included names, birthdates, home addresses, phone and email contacts, and passport and driving licence numbers.

Chief executive of Optus, Kelly Bayer, stated that the breach was a ‘sophisticated attack’. Conversely, the Australian Minister for Cyber Security stated that Optus had ‘left the window open’, and that ‘quite a basic hack’ had been undertaken. The method used for gaining access to Optus’ data is not totally clear, although many cyber security news outlets indicate that a publicly exposed API was used to obtain the data.

Shortly after the breach, an unknown actor posted within a forum a ransom demand of A$1m to be paid in cryptocurrency. The actor released a sample of 10,000 customer records to verify the breach and reiterate the ransom deadline. In an interesting turn of events, the same actor subsequently deleted the post and refused sale of the data to third parties, and even apologized for the inconvenience.
15
2022 NCC Group Annual Threat Monitor

## Law Enforcement Interventions
> Here we sum up the most prominent law enforcement and legislative action impacting cyberspace over the last year. Most significant are those operations that have had an immediate effect on active threat actors and the infrastructure, malware, and the monetisation channels they leverage.

### Lapsus$ arrest

From late 2021 and well into 2022, the Lapsus$ hacking group came storming into news headlines for allegedly breaching the defences of multiple well-known organisations, such as Nvidia, Vodafone, Uber, Okta, Ubisoft, among others.

By March of 2022, UK police had arrested 7 members of the gang, one of which was believed to be a 16 year old from Oxford, UK, known as ‘White’ or ‘BreachBase’ within the criminal group. This individual is thought to have had amassed a substantial fortune from their operations. Activity by the group appeared to tail off in the latter part of 2022, suggesting that the law enforcement actions may have successfully hampered the group’s activities.

### US authorities shut down RaidForums

Europol Operation TOURNIQUET saw the multi-agency coordination and arrest of three RaidForums personnel in early 2022, later announced publicly by the agency on 12 April 2022.

Launched in 2015, RaidForums was considered one of the world’s biggest hacking forums with a community of over half a million users. Diogo Santos Coelho, a Portuguese national known by the monikers of Omnipotent, Downloading, Shiza, and Kevin Maradona, was the founder and administrator of the site.

According to the US Department of Justice, “The RaidForums website offered four tiers of membership options, including in order of cost: (1) free membership; (2) VP membership; (3) MVP membership; and (4) God membership. The more expensive the membership. The more access a user could get to the RaidForums website. The God membership, for example, offered almost unlimited access to-the RaidForums website and features.”

The site provided dedicated forum areas covering cracking, leaks, and a marketplace enabling users to buy/sell/trade various illicit items within these sectors. The data breach of T-Mobile was just one of many databases offered for sale on the site.

The takedown of this site was a significant blow for a whole host of script kiddies, criminal groups, hacktivists and loan wolves, who relied on the site for new tools, breach data and buying access to potential targets.
17
2022 NCC Group Annual Threat Monitor

### US Government offer Reward for Conti Information

In August, the US Government announced a $10m reward for information leading to the arrest of 5 Conti group members, announced on the @RFJ_USA (Rewards for Justice) twitter account which included a TOR based onion link with which to share the information.
![Image description] Rewards for Justice Conti Reward
The information requested by the RFJ include Conti members Target, Tramp, Dandis, Professor, and Reshaev. The department also requested any additional information relating to malware or ransomware used in the targeting of US critical infrastructure.

### Spanish National Police arrest 55 members of the Black Panthers sim swap gang

Sim swapping is where an attacker takes over the mobile phone number of the real subscriber by asking the mobile telecom provider to link that number to a SIM card under the attacker’s control. In December 2022, the Spanish National Police arrested 55 members of the Black Panther’s cybercrime group in Barcelona who had been operating a sim swapping criminal enterprise. The gang was organised into four specialist action cells dedicated to social engineering, vishing (voice phishing), phishing, and carding. According to the Spanish National Police, “This gave them access to the database of the telephone operators themselves and allowed them to obtain the personal data of the victims, making duplicate SIM cards themselves.”

### FBI warn that search engine advertisement services are being used to distribute malware

Often termed as ‘Malvertising’, the distribution of malware via web pages promoted within sponsored search engine results, typically impersonating brands or services, began to see an increase in 2022. On December 21st, the FBI made a public service announcement regarding the uptick in malvertising and described the issue as:

“When a user searches for that business or service, these advertisements appear at the very top of search results with minimum distinction between an advertisement and an actual search result. These advertisements link to a webpage that looks identical to the impersonated business’s official webpage.

In instances where a user is searching for a program to download, the fraudulent webpage has a link to download software that is actually malware. The download page looks legitimate and the download itself is named after the program the user intended to download.”

One recent example of this attack type was the impersonation of the GIMP image editing platform, where the threat actors had generated a Google advertisement for a fake GIMP site used to host malware. We dive further into this attack methodology within the ‘Threat Spotlight: SEO Poisoning’ section of this report.
18
2022 NCC Group Annual Threat Monitor

## Incident Response Findings
> Analysis of our Cyber Incident Response Team’s (CIRT) activities this year have uncovered both interesting and expected findings alike, from the most targeted sectors to the most common attack vectors. In this section we will delve into some of the details of these cases.

### Sectors
Whilst these statistics are based on our clients and not necessarily reflective of global distribution, the most targeted sector in 2022 was ‘Government Activity’ with 18% of the total. This was followed by Financials and Industrials with 13%, and finally Technology joint with Consumer Cyclicals with 11% of the incidents each.

This year’s incident response activity slightly differs from 2021, where Industrials was the most prevalent sector with 19% of the total cases (6% proportional difference) and Government Activity was third with 13%.

Technology also only has a 1% proportional difference from 2021 to 2022 showing consistent and unwavering interest. Consumer Cyclicals however, which was the second-most targeted sector in 2021 with 16% of attacks, accounted for only 11% in 2022, exhibiting a 5% proportional difference.

Although there are some slight differences between 2021-2022, the general distribution of cases by sector is similar between the two years and there is no reason to expect any different in 2023, providing NCC Group’s client base doesn’t undergo any drastic changes.
![Image description] CIRT Cases by Sector
20
2022 NCC Group Annual Threat Monitor

### Attack Vectors
In terms of initial access techniques used to gain a foothold on the victim’s systems in 2022’s CIRT cases, the most used was spearphishing (varying between malicious link and attachment), followed by the exploitation of vulnerable public-facing applications, and finally the abuse of unsecure external remote services (RDP or VPN’s etc.) This does not go against our expectations as these three are oftentimes considered the most utilised attack vectors by threat actors: gaining initial access through remote services, remotely executing code on popular hardware and software through the leveraging of vulnerabilities and exploiting accidental insider threats through phishing.

We expect this trend to continue into 2023, as these methods are the most immediately accessible and effective ways of gaining initial access to a victim’s network. For example, valid account credentials can simply be purchased on marketplaces, phishing emails can be mass delivered or convincingly tailored to exploit the untrained employee, and new critical vulnerabilities for popular hardware and software are discovered almost daily.
![Image description] CIRT Cases by Initial Access Technique (2022)
21
2022 NCC Group Annual Threat Monitor

### Impact Stages
With reference to the threat groups perpetrating the attacks seen by our CIRT team, the majority (81%) were conducted by Organised Crime Groups (OCGs). Of the attacks conducted by OCG’s 56% were ransomware attacks and 24% were Business Email Compromise (BEC) attacks.

Other research has shown that BEC attacks increased dramatically in volume in 2022 compared to the previous year. Despite this, the conversation around BEC, and the risk it poses, is often side-lined by other topics.

Just 13% of the total attacks were Nation-State or State-Affiliated attacks, and the remaining were either insiders or opportunists.
The most common impact among our CIRT Cases was, as is to be expected, ransomware with 40% of the total attacks. This is followed by BEC with 33% of the total cases and finally coin mining with 13%. Successful ransomware attacks (where data encryption was actually achieved and not just the prior phases) are only slightly more common than BEC attacks, with a 7% difference, again implying that the reports of their rise in 2022 are valid. With reference to this data, NCC Group suggest that there will be a further increase of BEC cases in 2023 and they may reach an equilibrium with ransomware cases towards the end of the year, providing there are no dramatic increases in the latter.
![Image description] CIRT Cases by Initial Access Technique
![Image description] CIRT Cases by Impact Techniques (2022)
22
2022 NCC Group Annual Threat Monitor

## SOC Findings
> Data collated from our Global Security and Operations Centre (SOC) reported 2559 true positive incidents across the European and APAC SOCs. 2022 saw a 116% increase from the 1183 true positive cases observed in 2021, reflecting a growth in the number of tickets raised across NCC Group’s client base. This may also be in line with a growth in NCC's clientele, amounting to a greater number of incidents overall and not necessarily a growth in global security incidents. Regardless, in this section we will dive into the dataset to better understand the course of events throughout the year.

September observed the greatest number of tickets raised, with 350 recorded. This is in strong contrast to the figures for 2021 (See Figure 7) in which January-May saw the greatest number of incidents, albeit declining, and before observing a general drop until the end of the year. It is, however, difficult to pinpoint a root cause for the spike in September’s activity as a number of variables may be at play, from client security practices to a growth in cybercrime activity. September does however present as an anomaly, given the lower numbers immediately both before and after. In this respect, we are more likely to observe sub-300 figures as we move into 2023, closer to the low to mid 100s, if similar to early 2022.
![Image description] Month-by-Month Count of Incidents Raised in the SOC (2022)
24
2022 NCC Group Annual Threat Monitor

Overall, 1122 incidents were mitigated (44%), and 990 (39%) required no action; hence, the vast majority (83%) did not need to be escalated, with no further action needed. 386 cases were escalated to the client (15%).
Where analysing incidents by sector, NCC Group clients within the Academic and Educational Services were most susceptible with 657 incidents. Again, this is likely to be influenced by NCC's client base. With that in mind, it is worth noting that Academic and Education Services also ranked as most targeted in 2021 with 255 incidents. This is a notable growth of 157%, although only a proportional increase of 4%.
![Image description] Month-by-Month Count of Incidents Raised in the SOC (2021)
![Image description] Number of Cases by True Positive Category
25
2022 NCC Group Annual Threat Monitor

A number of confounding variables again are likely at play, from internal security issues, rise in cyberattacks, or new clients working with NCC. That said, reports in 2022 noted an increase in targeting against the sector, which alongside a 31% year on year rise for academia identified in our ransomware database, suggests a potential increase in targeting. Additionally, leading the attack numbers for SOC data in both 2021 and 2022 does suggest the possibility for a high number of tickets to be raised in the sector in 2023 and should encourage clients within to ensure best practice.
![Image description] SOC Tickets’ Raised according to Sector 2022
26
2022 NCC Group Annual Threat Monitor

## Ransomware Threat Landscape
> With 2022 concluded, the following provides an analysis of the ransomware threat landscape with year-on-year comparisons and trend predictions for 2023 to support organisations in implementing security measures for the year ahead.

> In this section of the report, we will discuss the trends that have emerged throughout the year and their implications, how these differ from what we have found in previous annual reports, and what we expect going forward based on existing data.

Firstly, there was a moderate decrease in cases of 5% from 2021 – 2022, from 2667 - 2531, differing from the increase that we saw from 2020 – 2021. As seen in Figure 1, there has been a varied distribution of cases in 2022 when compared with 2021. This is somewhat surprising as 2020 and 2021 were similar to one another in terms of fluctuations, but not when considering absolute figures.
Based on the data, the first half of 2021 was less sporadic and ranged from 127 – 229 attacks, whereas 2022 had a more pronounced curve, ranging from 120 – 289 attacks. Conversely, the latter half of 2021 saw some pronounced fluctuations, ranging from 155 – 324, whereas 2022 had a more gradual inclining trend with consistent highs and lows, ranging from 159 – 269 attacks.
![Image description] Total Hack & Leak Cases Year on Year
28
2022 NCC Group Annual Threat Monitor

2022’s initial rise in attacks until April can, with confidence, be attributed to LockBit’s (2.0 then) rampant activity at the time, with their total victims reaching highs of 103 in April, and not dipping below 78 in February, excluding January when threat actors are usually less active following the holidays. In June, there was a huge drop in activity, which can be attributed to Conti’s dissolution since March, as well as LockBit’s rebranding into 3.0 (which likely required an adjustment period, as their attacks were down 45%). These events likely also contributed to the 5% decrease from 2021 – 2022. Following