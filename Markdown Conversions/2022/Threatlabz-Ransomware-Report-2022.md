# 2022 ThreatLabz State of Ransomware Report

## Contents
[Introduction](#introduction)
[Key findings](#key-findings)
[The evolution of ransomware](#the-evolution-of-ransomware)
[Ransomware attack sequence](#ransomware-attack-sequence)
[2021–2022 ransomware attack statistics](#20212022-ransomware-attack-statistics)
[Industry verticals affected by ransomware](#industry-verticals-affected-by-ransomware)
[Top ransomware families](#top-ransomware-families)
[2022-23 predictions](#2022-23-predictions)
[Prevention guidance](#prevention-guidance)
[Key ransomware trends](#key-ransomware-trends)
[Supply chain attacks](#supply-chain-attacks)
[Log4j ransomware](#log4j-ransomware)
[Ransomware-as-a-service](#ransomware-as-a-service)
[Geopolitical attacks](#geopolitical-attacks)
[Law enforcement takedowns](#law-enforcement-takedowns)
[Ransomware rebranding](#ransomware-rebranding)
[Major vulnerabilities used in ransomware attacks](#major-vulnerabilities-used-in-ransomware-attacks)
[Top 11 prevalent ransomware families](#top-11-prevalent-ransomware-families)
[Conti](#conti)
[LockBit](#lockbit)
[PYSA/Mespinoza](#pysamespinoza)
[REvil/Sodinokibi](#revilsodinokibi)
[Avaddon](#avaddon)
[Clop](#clop)
[Grief](#grief)
[Hive](#hive)
[BlackByte](#blackbyte)
[AvosLocker](#avoslocker)
[BlackCat/ALPHV](#blackcatalphv)
[About ThreatLabz](#about-threatlabz)
[About Zscaler](#about-zscaler)

© 2022 Zscaler, Inc. All rights reserved.

## Introduction
If it feels like ransomware is always in the news, it isn’t just media bias: the Zscaler ThreatLabz research team has found that ransomware attacks increased by yet another 80% between February 2021 and March 2022 compared to the previous year, setting new records for both the volume of attacks and the cost of damages.

These tactics add up to be very damaging. Industry experts predict that ransomware will be the top tactic used in third-party breaches and supply chain attacks in 2022, and that the global cost of ransomware damages will grow to $42 billion by 2024.

These trends have pushed ransomware even further up the list of cybersecurity priorities for organizations across industries. Aimpoint’s “The CISOs Report,” 2022 found that ransomware is the single highest threat that CISOs around the world are most concerned about.

How can you identify and defend against the latest ransomware variants? This report should help.

ThreatLabz analyzes data from more than 200 billion daily transactions and 150 million daily blocked attacks across the Zscaler Zero Trust Exchange along with Zscaler ThreatLabz threat intelligence to track prevalent threat families, identify emerging trends, and improve protections for Zscaler customers. In this report, ThreatLabz looked at ransomware data from February 1, 2021, through March 31, 2022, to identify the most prolific ransomware families and their tactics. We will share our findings, predictions, and best practices guidance to help inform your ransomware defense strategies.

Ransomware is more and more attractive to attackers, who are able to wage increasingly profitable campaigns based on three major trends:

*   **Supply chain attacks** that exploit trusted vendor relationships to breach organizations and multiply the damage of attacks by enabling threat actors to hit multiple (sometimes hundreds or thousands) of victims at the same time.
*   **Ransomware as a service** that uses affiliate networks to distribute ransomware on a wide scale, allowing hackers who are experts in breaching networks to share profits with the most advanced ransomware groups.
*   **Multiple-extortion attacks** that utilize data theft, distributed denial of service (DDoS) attacks, customer communications, and more as layered extortion tactics to increase ransom payouts.

© 2022 Zscaler, Inc. All rights reserved.

## Key findings
*   Ransomware attacks increased by 80% year over year, accounting for all ransomware payloads observed in the Zscaler cloud.
*   Double extortion ransomware increased by 117%, indicating that more and more attacks include data theft in their strategies. Some industries saw particularly high growth of double extortion attacks, including healthcare (643%), food service (460%), mining (229%), education (225%), media (200%), and manufacturing (190%).
*   Manufacturing was the most targeted industry for the second straight year, making up almost 20% of double extortion ransomware attacks.
*   Supply chain ransomware attacks are on the rise, as are supply chain attacks in general. Exploiting trusted suppliers lets attackers breach a large number of organizations all at once, including organizations that otherwise have strong protections against external attacks. Supply chain ransomware attacks of the past year include damaging campaigns against Kaseya and Quanta as well as a number of attacks exploiting the Log4j vulnerability.
*   Ransomware as a service is driving more attacks. Ransomware groups continue to recruit affiliates through underground criminal forums. These affiliates compromise large organizations and deploy the group’s ransomware, typically in exchange for about 80% of the ransom payments received from victims. Most (8 out of 11) of the top ransomware families of the past year have commonly proliferated via ransomware-as-a-service models.
*   Law enforcement is cracking down. A number of last year’s top ransomware families—particularly those targeting critical services—attracted attention from law enforcement agencies around the world. REvil (responsible for famous attacks on Kaseya and JSB), DarkSide (responsible for the attack on Colonial Pipeline), and Egregor (a rebranding of Maze, last year’s top ransomware family) all had assets seized by law enforcement in 2021.
*   Ransomware families aren’t going away—they’re just rebranding. Feeling increased heat from law enforcement, many ransomware groups have disbanded and reformed under new banners, where they use the same (or very similar) tactics. DarkSide rebranded as BlackMatter, DoppelPaymer rebranded as Grief, and Avaddon rebranded as Haron and Midas. Evil Corp, sanctioned by the US government, has consistently rebranded their ransomware operations.
*   The Russia-Ukraine conflict has the world on high alert. There have been several attacks associated with the Russia-Ukraine conflict, including multiple wipers including HermeticWiper and PartyTicket ransomware. So far, most of this activity has targeted Ukraine. However, government agencies have warned organizations to be prepared for more widespread attacks as the conflict persists.
*   Zero trust remains the best defense. To minimize the chance of a breach and the damage a successful attack can cause, your organization must use defense-in-depth strategies that include reducing your attack surface, enforcing least privileged access control, and continuously monitoring and inspecting data across your environment.

© 2022 Zscaler, Inc. All rights reserved.

## The evolution of ransomware
Ransomware is a type of malware cybercriminals use to disrupt a victim’s organization. Ransomware encrypts an organization’s important files into an unreadable form and demands a ransom payment to decrypt them. Ransom demands are often proportional to the number of systems infected and the value of the encrypted data: the higher the stakes, the higher the payment.

In late 2019, attackers evolved their ransomware tactics to include data exfiltration, commonly referred to as a “double extortion” ransomware attack. In these attacks, if victims choose not to pay the ransom to decrypt the data and, instead, attempt to restore the data from a backup, the attackers threaten to leak the stolen data. In late 2020, some ransomware attackers added another attack layer with DDoS tactics that bombard the victim’s website or network, creating even more business disruption, thus pressuring the victim to negotiate.

In 2021 and going into 2022, the most damaging ransomware trend involves supply chain attacks, in which a breach of a vendor (typically a software or other technology provider) opens the door for second-stage attacks on organizations that rely on their products. Supply chain attacks are estimated to have jumped 51% in the back half of 2021. Threat actors have made headlines through exploits of popular software products such as SolarWinds, Kaseya, and Log4j, and we expect this trend to escalate in the coming years.

© 2022 Zscaler, Inc. All rights reserved.

## Ransomware attack sequence
Today’s ransomware attacks typically have the following stages:

*   **Initial compromise:** Attackers use a variety of intrusion vectors to gain access to systems, including phishing emails, exploiting vulnerabilities in remote administrator or virtual private network (VPN) tools, and using brute force or stolen credentials to access Remote desktop protocol (RDP) connections. Supply chain attacks are yet another method to infiltrate an organization.
*   **Lateral movement:** After gaining initial access, threat actors proceed to gather victims’ infrastructure information and move laterally across network systems, escalating privileges and establishing persistence mechanisms as needed, cataloging key data to steal or encrypt, and depositing ransomware payloads for later execution.
*   **Data exfiltration:** In the case of a double extortion attack, attackers will next steal sensitive data to use as a secondary extortion tactic so they can demand higher ransom payments. This reduces the victims’ leverage: even if they can recover the encrypted data from backups, they still must face the threat of the cybercriminals leaking the stolen data.
*   **Ransomware execution:** Next, attackers deploy and execute the ransomware, encrypting targeted files on systems connected to the network. Ransomware typically terminates processes related to security software and databases to maximize the number of files it can encrypt. Shadow copy backups are also usually deleted from the system to hinder file recovery. Some ransomware families will also reboot the compromised system in Windows Safe Mode to bypass security endpoint software prior to file encryption. After file encryption, victims are provided with a ransom note that provides instructions for paying the ransom and decrypting their files.
*   **DDoS:** If the victim does not negotiate, some hacking groups will wage a DDoS attack against the victim’s network or website, disrupting their business operations to gain additional leverage.

**Figure 1:** *Infection chain of a ransomware attack. The image shows a flow chart with the following steps: Initial access (spam email, brute force or stolen credentials to RDP, exploiting a vulnerability) -> Network reconnaissance & lateral movement -> Data exfiltration -> Ransomware deployment, execution, & data encryption -> DDOS attack on victim website or network until negotiation. If ransom is not paid: Publish data to leak site (credentials, sensitive data, other information)*

© 2022 Zscaler, Inc. All rights reserved.

## 2021–2022 ransomware attack statistics
The high volume of transaction data on the Zero Trust Exchange provides a unique look into the tactics and victims of cybercriminals. From February 2021 through March 2022, ThreatLabz observed an 80% increase in ransomware payloads compared to the previous year. Further, we saw a 117% increase in double extortion ransomware victims based on data published on threat actors’ data leak sites.

## Industry verticals affected by ransomware
Manufacturing was already the most targeted vertical in 2020, making up 12.7% of double extortion ransomware attacks between November 2019 and January 2021. This year, the percentage of attacks on manufacturing organizations rose even further to 19.5%, followed by services (9.7%), construction (8.1%), retail and wholesale (7.5%), and high tech (6.7%).

**Figure 2:** *Ransomware infections by industry. The image is a bar graph showing the number of ransomware infections by industry. Manufacturing has the highest number of infections at 339, followed by Services at 169, Construction at 141, Retail & Wholesale at 130, High Tech at 117, Other at 111, Financial Services at 85, Transportation Services at 81, Education at 78, Food, Beverage & Tobacco at 68, Healthcare at 52, Real Estate at 52, Government at 48, Basic Materials and Chemicals at 36, Insurance at 33, Oil & Gas at 31, Restaurants, Bars & Food Services at 28, Mining at 23, Nonproft Institutions at 22, Telecommunications at 22, Consumer Services at 18, Advertising at 15, Media at 15, Aerospace & Defense at 10, Utilities at 6, Arts, Entertainment & Recreation at 3, Energy at 3, Household & Personal Products at 2.*

Growth in double extortion ransomware attacks varied widely by industry. In last year’s report, we noted a particularly low number of attacks against healthcare organizations, driven by increased scrutiny from law enforcement as well as pledges from several prevalent ransomware families that they would not target healthcare during the COVID-19 pandemic.

This year’s data tells a different story. Double extortion ransomware attacks against healthcare grew by 643% in 2021, though it started with a very low baseline of attacks in 2020. Several other verticals with higher starting points also saw triple-digit growth in attacks, including education (225%), manufacturing (190%), construction (161%), financial services (130%), and services (109%).

**Figure 3:** *Percentage change in double extortion attacks by industry. The image is a bar graph showing the percentage change in double extortion attacks by industry from 2020 to 2021. Healthcare has the highest percentage change at 643%, followed by Restaurants, Bars & Food Services at 460%, Mining at 229%, Education at 225%, Media at 200%, Manufacturing at 190%, Basic Materials and Chemicals at 177%, Construction at 161%, Financial Services at 130%, Services at 109%, Food, Beverage & Tobacco at 100%, Insurance at 94%, Real Estate at 93%, Retail & Wholesale at 71%, Telecommunications at 69%, Oil & Gas at 63%, High Tech at 58%, Government at 37%, Other at 28%, Nonproft Organizations at 16%, Advertising at 7%, Transportation at 0%, Consumer Services at -5%, Utilities at -25%, Aerospace & Defense at -33%, Energy at -50%, Arts, Entertainment & Recreation at -70%, Household & Personal Products at -83%.*

© 2022 Zscaler, Inc. All rights reserved.

## Top ransomware families
Conti and LockBit were the most prevalent double extortion ransomware families in 2021, joined by a range of new entrants that emerged over the course of the year.

**Figure 4:** *Timeline of ransomware families publishing on data leak sites or hacking forums. The image is a timeline showing the emergence of various ransomware families from November 2019 to November 2021. The timeline includes Maze, CUBA, Clop, PYSA/Mespinoza, BlackCat/ALPHV, MountLocker, NEFILIM, LockBit, Netwalker, RansomExx, Pay2Key, AKO, LV, Vice Society, AvosLocker, BlackByte, Hive, Avaddon, Conti, Egregor, Ranzy, DarkSide, Sekhmet, REvil/Sodinokibi, RagnarLocker, DopplePaymer, Lorenz, Spook, and Grief.*

Many of the active ransomware families in 2021–2022 are ransomware-as-a-service (RaaS) models, increasing their distribution through affiliate networks. In 2021, we also saw the rebranding of several popular ransomware families, such as DoppelPaymer rebranding as Grief, DarkSide rebranding as BlackMatter, and Avaddon rebranding as Haron followed by Midas (the latter two using the Thanos ransomware builder).

Conti has been the most active ransomware group of the last two years and the costliest of all time: The FBI estimates that as of January 2022, there were more than 1,000 victims of attacks associated with Conti ransomware, with total victim payouts exceeding US$150 million (not including related damages or remediation costs). Conti victims have included a range of critical services organizations from financial services, IT, energy, and government sectors, including Ireland’s public healthcare services and the government of Costa Rica. In May 2022, the US Department of State offered a $10 million reward for information on leaders of the group.

LockBit, formerly known as ABCD ransomware, tends to attack small- to medium-size businesses, thus mostly avoiding the headlines, with the exception of their attack on Accenture in August 2021. LockBit is a widely used RaaS that is attractive to attackers due to its speed and performance.

**Figure 5:** *Ransomware attacks by family, February 2021-March 2022. The image is a bar graph showing the number of ransomware attacks by family. Conti has the highest number of attacks, followed by LockBit, Pysa, REvil/Sodinokibi, Avaddon, Clop, Grief, Hive, BlackByte, AvosLocker, LV, AlphaV/BlackCat, CUBA, Spook, Vice Society, Midas, and RansomExx.*

© 2022 Zscaler, Inc. All rights reserved.

## 2022–23 predictions
*   **Ransomware as a service will continue to increase** RaaS has proven to be valuable for all parties involved. New ransomware developers and affiliates will increase their use of this model to wage rapidly changing attacks on vulnerable organizations.
*   **Changing ransomware models will lead to changing targets** With ransomware builders and organizational intel available for sale on the dark web, attackers have the advantage of filtering through company profiles to narrow down the ideal targets for specific vulnerabilities, profits, and types of ransomware. As a result, you should expect to see a shift toward easier targets, including small to medium enterprises with fewer security controls and organizations with internet-visible applications that have known vulnerabilities along with previously phished credentials.
*   **Dwell time will continue to decrease** Now that threat actors have easy and cheap access to company profiles and compromised credentials for sale on the dark web, the days of attackers sitting on targets for months or even years and then taking extra time to look around before launching an attack are coming to an end. With more public reports of ransomware attackers reducing dwell times to just days, the criminals are savvy to increased detection techniques, realizing time is of the essence for a successful attack. As a result, security teams need to close the gap and speed up detection—to days, hours, or just minutes—to prevent worst-case scenario breaches in 2022 and beyond.
*   **Supply chain attacks will increase as adversaries compromise partner and supplier ecosystems** The world’s top organizations often have the best security in place—but the same may not be true for their suppliers and partners, with third-party access to supporting networks, systems, and information. We saw this in the recent compromise of Okta by the rogue hacker group Lapsus$, and in REvil threatening Apple via Quanta Computer, a top manufacturer of Apple products. These groups and many others used supply chain attacks to access sensitive upstream information using supplier access without ever having to breach the hardened security measures of their final targets.
*   **Ransomware may be used as, or in conjunction with, a wiper to destroy data** In early 2022, publicized attacks on Ukraine featured multiple types of wiper attacks, including HermeticWiper alongside a decoy ransomware known as PartyTicket. This is not the first time ransomware has been used in geopolitical attacks, with NotPetya and Bad Rabbit being deployed in 2017 to attack Ukrainian organizations. Geopolitical tensions bring with them the threat of masked ransomware, wipers, and other tactics that afford threat actors an elevated degree of anonymity and plausible deniability.
*   **Old (and new) vulnerabilities will continue to cause damage** There have been some major vulnerabilities discovered in the past year (e.g., Log4j, PrintNightmare, ProxyShell/ProxyLogon) that organizations will be dealing with for years to come. Attackers will continue to search for and exploit unpatched and out-of-date software and servers to bypass security controls.
*   **Ransomware families will continue rebranding** We saw this cycle throughout 2021: a ransomware group pulls off a major attack, earns attention and sanctions from law enforcement, and then disappears and reforms later under a new name. With ransomware very much on the radar of law enforcement, this cycle will continue throughout 2022 and beyond.
*   **Organizations will need to beef up security beyond endpoint protection** Ransomware groups will increase use of tactics to bypass antivirus and other endpoint security controls. Organizations will have an even greater need for defense-in-depth rather than relying solely on endpoint security to prevent and detect intrusions.
*   **Ransomware developers will add more malware obfuscation** Malware authors implement malware obfuscation techniques to hinder reverse engineering and bypass static signature detection. The malware obfuscation complexity will continue to increase with advanced techniques, including control flow flattening, polymorphic string obfuscation, and the use of virtual machine-based packers.
*   **Leaked ransomware source code will lead to forks** There have been several source code leaks for ransomware in the past year, including two versions of Conti and Babuk. Zscaler ThreatLabz has already observed both ransomware families’ source code being forked by third parties and used in attacks. The release of source code will undoubtedly lead to abuse by other criminal groups that do not have the expertise to design and build their own ransomware from scratch.

© 2022 Zscaler, Inc. All rights reserved.

## Prevention guidance
Whether a simple ransomware attack, a double- or triple-extortion attack, a self-contained threat family, or a RaaS attack executed by an affiliate network, the defense strategy is the same: employ the principles of zero trust to limit vulnerabilities, prevent and detect attacks, and limit the blast radius of successful breaches. Here are some best practices recommendations to safeguard your organization against ransomware.

1.  **Get your applications off of the internet.** Ransomware actors start their attacks by performing reconnaissance on your environment, looking for vulnerabilities to exploit, and calibrating their approach. The more applications you have published to the internet, the easier you are to attack. Use a zero trust architecture to secure internal applications, making them invisible to attackers.
2.  **Enforce a consistent security policy to prevent initial compromise.** With a distributed workforce, it is important to implement a security service edge (SSE) architecture that can enforce consistent security policy no matter where your users are working (in office or remotely).
3.  **Use sandboxing to detect unknown payloads.** Signature-based detection is not enough in the face of rapidly changing ransomware variants and payloads. Protect against unknown and evasive attacks with an inline, AI-powered sandbox that analyzes the behavior rather than the packaging of a file.
4.  **Implement a zero trust network access (ZTNA) architecture.** Implement granular user-to-application and application-to-application segmentation, brokering access using dynamic least-privileged access controls to eliminate lateral movement. This allows you to minimize the data that can be encrypted or stolen, reducing the blast radius of an attack.
5.  **Deploy inline data loss prevention.** Prevent exfiltration of sensitive information with trust-based data loss prevention tools and policies to thwart double extortion techniques.
6.  **Keep software and training up to date.** Apply software security patches and conduct regular security awareness employee training to reduce vulnerabilities that can be exploited by cybercriminals.
7.  **Have a response plan.** Prepare for the worst with cyber insurance, a data backup plan, and a response plan as part of your overall business continuity and disaster recovery program.

To maximize your chances of defending against ransomware, you must embrace layered defenses that can disrupt the attack at each stage—from reconnaissance to initial compromise, lateral movement, data theft, and ransomware execution.

**Stopping ransomware with zero trust**

*The image is a diagram showing how zero trust can stop ransomware. It has the following layers: Minimize attack surface (Make apps invisible), Prevent initial compromise (Inspect all traffic, Safely render email links, Cloud browser isolation, In-line inspection of all traffic, SWG, IPS, Sandbox), Eliminate lateral movement (User-to-app segmentation, App-to-app segmentation, Deception), Stop data loss & malware delivery (Cloud DLP, Cloud CASB, Cloud firewall, Workload protection). Below the layers are the attack stages: Gain initial entry (Vulnerable VPN), Install malware (G Drive), Deliver malware dropper (G Drive), Establish foothold with phishing (Gmail), Steal credentials & compromise additional systems (Domain controller), Install ransomware & demand payment, Steal data.*

© 2022 Zscaler, Inc. All rights reserved.

## Key ransomware trends

### Supply chain attacks
**What is a Supply Chain Attack?**

Supply chain attacks—sometimes called value chain or third-party attacks—are attacks against the suppliers of an organization as a means for gaining access. Most large organizations have sophisticated security controls that make infiltration difficult, so attackers have found a way in through the suppliers to these organizations.

Supply chain attacks exploit the trust between legitimate organizations that exists in normal business operations. Attackers plant a backdoor into a product that they know their target uses, which allows the attacker to infiltrate the target’s network without detection—typically gaining entry via automated patches or software updates, called “trojanized” updates. Once inside, the attackers can spy, steal data, implant other malware, and disrupt operations.

Such attacks involve a high degree of planning and sophistication, and they can have a devastating impact on organizations within the blast radius of the original compromise.

**Figure 6:** *Supply chain attack. The image is a diagram showing the steps of a supply chain attack. Attacker breaches software product and installs malicious code. Malicious code is distributed to customers during software update.*

#### Kaseya supply chain ransomware
On July 2, 2021, IT management software firm Kaseya disclosed a security incident impacting their on-premises version of Kaseya VSA software, a platform that allows managed service providers (MSPs) to perform patch management, backups, and client monitoring for their customers. Roughly 70 MSPs are believed to have been breached in this attack, with downstream impacts to as many as 1,500 small and medium businesses.

The threat actor behind this attack identified and exploited a zero day vulnerability in the Kaseya VSA server that allowed them to send a malicious script to all clients that were managed by that server. The script was used to deliver REvil/Sodinokibi ransomware that encrypted files on the affected systems.

#### Quanta computer supply chain
In April 2021, REvil attacked Quanta Computer, the world’s largest laptop manufacturer and a top manufacturer of Apple products. Quanta refused to pay a $50 million ransom demand, leading to REvil targeting Apple and other Quanta customers for the ransom instead. REvil leaked 21 screenshots of MacBook schematics and threatened to publish more data from Apple and other companies until Apple or Quanta paid the ransom demand.

### Log4j ransomware
In December 2021, the Apache Software Foundation released a security advisory regarding a remote code execution vulnerability (CVE-2021-44228) in their popular Log4j logging library. This vulnerability allows an attacker to download and execute a malicious payload by submitting a specially crafted request to the vulnerable system. The attacker can then control log messages or log message parameters to execute arbitrary code loaded from LDAP servers when message lookup substitution is enabled.

Log4j is incorporated into many popular websites, applications, and frameworks, making the impact widespread. Several ransomware attacks have emerged exploiting this vulnerability:

*   **NightSky ransomware** On January 4, 2021, attackers exploited the Log4j vulnerability in an internet-facing system running VMware Horizon, dropping the NightSky ransomware.
*   **Khonsari** Multiple attacks have been observed using Log4j exploits on Windows systems to deploy Khonsari ransomware.
*   **Conti** The Conti group has also leveraged the Log4j vulnerability to execute ransomware attacks. AdvIntel discovered the group scanning and targeting vulnerable Log4j VMware vCenter versions, moving laterally from existing Cobalt Strike sessions to US and European victim networks.
*   **TellYouThePass** Attackers have exploited the Log4j vulnerability to deploy and execute the TellYouThePass ransomware in Windows and Linux systems.

### Ransomware-as-a-service
The dark web has become a very popular place for threat groups to sell their wares to would-be criminals. We’ve detailed the impact of these marketplaces for other attack types, such as the growth of phishing as a service in the 2022 ThreatLabz State of Phishing report.

RaaS has become incredibly popular, and it now drives the bulk of modern ransomware attacks. In fact, 8 of the top 11 ransomware families from the past year utilize RaaS ecosystems.

The RaaS model requires two parties: operators and affiliates. Operators are the threat groups that develop the ransomware. Affiliates target their victims, execute the ransomware, and set demands.

Operators recruit affiliates and provide them with the ransomware and tools required to execute it, access to a data leak site, negotiation assistance, and other support, in exchange for approximately 70–80% of the profit from the attacks.

This model is beneficial to both parties. Affiliates get everything that they need to execute highly effective ransomware attacks without needing to develop any of it themselves. This is attractive both to skilled criminals who save development time and resources as well as low-skilled criminals who otherwise would not be able to execute such an attack. Ransomware operators can dramatically increase the scale of their operations and, consequently, their profits.

RaaS has increased both the volume and damage of attacks:

*   Increase in volume of ransomware attacks: More affiliates begin executing ransomware as it now requires less time and skill to develop.
*   Increase in ransom amounts due to double extortion: RaaS includes a double extortion component in which threat actors steal data and threaten to publish it on a data leak site if the ransom is not paid. This increases the ransom amount and the rate of successful payment.

### Geopolitical attacks
Security leaders around the world are on guard for an increase in ransomware attacks as a result of the Russia-Ukraine conflict.

In March 2022, US President Joe Biden issued a statement warning of the potential for malicious cyber conduct against the United States as a response to economic sanctions against Russia. His statement urged immediate action to harden cyber defenses among both public and private sector organizations.

As of the writing of this report, there have been several ransomware attacks against Ukraine and/or associated with this conflict:

1.  **PartyTicket ransomware:** This Go-based ransomware has been used in conjunction with the HermeticWiper malware to target organizations in Ukraine. PartyTicket is unsophisticated and contains flawed encryption that can be decrypted and reversed, leading us to suspect that it was developed as a decoy to distract from HermeticWiper.
2.  **Conti ransomware:** The Cybersecurity and Infrastructure Security Agency (CISA), the Federal Bureau of Investigation (FBI), the National Security Agency (NSA), and the United States Secret Service have rereleased an advisory on Conti, a Russia-linked ransomware group. Their advisory warns that “Conti cyber threat actors remain active and reported Conti ransomware attacks against U.S. and international organizations have risen to more than 1,000.” In late February, Conti posted two statements on their leak site, pledging support to the Russian government in response to “Western warmongering and American threats to use cyber warfare against the citizens of Russian Federation.”

### Law enforcement takedowns
Law enforcement agencies around the world are paying increased attention to ransomware families, particularly those causing widespread damages. There have been several successful takedowns of high-impact ransomware families through 2021 and early 2022.

#### REvil takedown
REvil is one of the most infamous ransomware families of the last two years, in the news after major attacks against Kaseya and JSB. Following the Kaseya attack, the FBI planned a takedown of the REvil servers. However, they never got their chance: shortly after this critical attack in July 2021, REvil shut down its operations and the hackers disappeared. This turned out to be brief, as Kaseya’s operations restarted in September 2021.

In January 2022, the Russian government apparently dismantled the REvil hacking group, arresting members at the request of the United States. The Russian Federal Security Service (FSB) searched 25 addresses, detaining 14 group members of REvil as well as seizing 426 million rubles, US$600,000, 500,000 euros, 20 luxury cars, and computer equipment. However, REvil reemerged in April 2022, attacking organizations with an updated ransomware version.

#### DarkSide takedown
On May 6, 2021, the DarkSide ransomware group executed a high-profile ransomware attack on Colonial Pipeline, the largest oil pipeline in the United States. Federal agencies took action, and within two weeks of the attack, a threat actor known as UNKN announced that DarkSide had been shut down, as they had lost access to servers and their cryptocurrency had been transferred to an unknown account. The Department of Justice announced that they had seized 63.7 bitcoins valued around US$2.3 million.

#### Egregor takedown
The Egregor ransomware group—formerly known as Maze—was taken down by cooperative law enforcement efforts on February 9, 2021. Agencies from Ukraine, France, and the United States shut down the Egregor leak website, arrested group members, and seized computers that were linked to ransomware attacks. Egregor had extorted approximately US$80 million from more than 150 victim companies.

### Ransomware rebranding
Ransomware operators have been rebranding their ransomware at a high rate in the past year. Rebranding is commonly due to unwanted attention from law enforcement and the media, as well as due to sanctions that limit the groups’ abilities to collect ransom payments.

#### DoppelPaymer rebranded as Grief
In early May 2021, DoppelPaymer ransomware activity dropped significantly. Although the DoppelPaymer leak site still remains online, there has not been a new victim post since May 6, 2021. In addition, no victim posts have been updated since the end of June. This lull is likely a reaction to the Colonial Pipeline ransomware attack that occurred on May 7, 2021. However, the apparent break is due to the threat group behind DoppelPaymer rebranding the ransomware under the name Grief. Both ransomware variants share malware code, and the leak sites are very similar. The Grief ransom portal has some differences from the DoppelPaymer portal. In particular, the ransom demand payment method is made in Monero (XMR) instead of bitcoin (BTC). This switch in cryptocurrencies may be in response to the FBI recovering part of the Colonial Pipeline ransom payment.

#### Darkside rebranded as BlackMatter
After DarkSide’s shutdown in May 2021, a new ransomware family named BlackMatter emerged in late July. The encryption routine used in the ransomware and text in the data leak site indicated that BlackMatter was a rebranding of DarkSide.

BlackMatter ceased its operations in November 2021. The group posted a shut down operation message on its RaaS portal that said, “Due to certain unsolvable circumstances associated with pressure from the authorities (part of the team is no longer available, after the latest news) — the project is closed.”

#### Thanos based ransomware rebranding
Advertised on the dark web as RaaS, Thanos ransomware was first identified in February 2020. The Thanos builder was leaked, and in the following two years, a series of new variants have been developed. The Prometheus ransomware variant emerged in February 2021. In September, Prometheus was rebranded as Spook. Both have similar ransom notes and data leak sites and contain Thanos’s signature Key Identifier.

In July 2021, another Thanos derived ransomware called Haron was discovered. Haron ransomware has striking similarities with Avaddon ransomware. Haron and Avaddon share commonalities in their ransom notes, negotiation sites, and data leak sites. In October 2021, another variant called Midas was discovered that is a rebranded version of Haron ransomware.

#### Evil Corp rebranding
The Evil Corp gang, also known as Indrik Spider, is known for a range of malicious activity. They created banking trojans such as Dridex, the latter of which was used to distribute their BitPaymer ransomware.

The Office of Foreign Assets Control (OFAC) of the US Treasury Department sanctioned members of Evil Corp for damages caused by their Dridex malware, claiming that they inflicted more than $100 million in damages across banks and financial institutions in more than 40 countries. Following these sanctions, ransomware negotiation firms refused to facilitate ransom payments for Evil Corp for fear of fines or legal action from the US Treasury Department. To bypass sanctions, Evil Corp discovered a simple loophole through rebranding their ransomware.

Evil Corp distributed WastedLocker ransomware in June 2020, Hades ransomware in December 2020, and Phoenix ransomware in March 2021. In May 2021, they continued to rebrand their