2023
CYBER SECURITY
REPORT

# CHAPTER 1: INTRODUCTION TO THE 2023 CYBERSECURITY REPORT
BY MAYA HOROWITZ

# CHAPTER 2: TIMELINE OF KEY 2022'S CYBER EVENTS

# CHAPTER 3: 2022'S CYBER SECURITY TRENDS

## 20 Russo-Ukrainian conflict
## 22 The year of wiper disruption
## 26 Hacktivism graduates to major player on geopolitical stage
## 30 Weaponization of Legitimate Tools
## 34 Ransomware Extortion—Shifting focus from encryption to data extortion
## 38 Mobile Malware Landscape—The Risk of Trusting the Familiar
## 41 Cloud: Third Party Threat

# CHAPTER 4: GLOBAL ANALYSIS

# CHAPTER 5: HIGH PROFILE GLOBAL VULNERABILITIES

# CHAPTER 6: INCIDENT RESPONSE PERSPECTIVE

# CHAPTER 7: 2023 INSIGHTS FOR CISOS: DISRUPTION AND DESTRUCTION

# CHAPTER 8: PREVENTION IS AT REACH

# CHAPTER 9: MALWARE FAMILY DESCRIPTIONS

# CHAPTER 10: CONCLUSION

# CHAPTER 1: INTRODUCTION TO THE CHECK POINT 2023 SECURITY REPORT

## MAYA HOROWITZ
VP Research, Check Point

In 1976, Queen Elizabeth II sent the first royal email. It was sent over ARPANET, 7 years before the internet was invented, and a long 13 years before the first recorded internet hack.

Almost 50 years later, email has evolved into a popular communication method, and the most popular vehicle for threat actors to initiate their attacks. In fact, the Check Point Research (cp<r>) annual Security Report shows that in 2022, the proportion of email-delivered-attacks has increased, reaching a staggering record of 86% of all file-based attacks in-the-wild.

In our Security Report, we discuss a few more trends observed by cp<r> throughout the year. The Russia-Ukraine war demonstrated how the traditional, kinetic, war can be augmented by a cybernetic war. It has also influenced the broader threat landscape in the rapid changes of hacktivism and how independent threat actors choose to work for state-affiliated missions. The war has also seen enhanced usage of wiper malware, and this trend has been adopted by several actors, reaching a point where 2022 has seen more wiper attacks globally, than in the previous decade altogether. Traditional cybercrime has also changed—in 2022, threat actors started using more legitimate tools in their operations, including native operating system files, IT software and penetration testing tools, all helping them in their efforts to stay under the radar. In their ransomware attacks, threat actors are starting to skip the encryption process, realizing that the financial rewards comes mostly from data breaches and the threat to publish victim data.

In attacks on mobile devices, attackers make a habit out of mimicking legitimate applications, and in the cloud threat landscape—companies’ data is at risk mostly when hosted by third parties, and susceptible to attacks due to misconfigurations, over-permissive roles and permissions, and access keys stored publicly.

In the last days of 2022, we witnessed a dramatic advancement in the field of generative artificial intelligence, now widely available to the public, and which is able to generate highly professional text (code included) on demand in seconds. As we step into 2023, we should keep in mind that this technology may quickly be adopted by threat actors, to craft even more malicious emails, in even better quality than those typically authored by threat actors, and with endless variations of malware and malicious code in general. This comes to prove, yet again, the importance of zero day prevention of attacks, across the entire IT infrastructure, including email, endpoint, network, cloud, and everything in between.

Check Point Software is committed to ensuring our customers are provided the best and prevention-first security across all these vectors. At Check Point Research, we are happy to provide this annual Security Report to help in raising awareness and vigilance, so that we can all join hands in preventing the next cyberattack.

Maya Horowitz

VP Research at Check Point Software Technologies

# CHAPTER 2: TIMELINE OF 2022'S KEY CYBER EVENTS

## JANUARY

### UKRAINE
Ukraine has been hit by a large scale cyber-attack that took down several of its government and ministries websites. Threat actors defaced the Foreign Affairs website with threatening message reading “Ukrainians!… All information about you has become public, be afraid and expect worse.” Researchers additionally found evidence of a significant ongoing operation targeting multiple organizations in Ukraine, leveraging a malware disguised as ransomware that could render a system inoperable.

### IRAN
Television channels and a radio station run by Iran’s state broadcaster were hacked in a complex attack by an exiled opposition group. Hacktivist group Edalat-e Ali (Ali's Justice) hacked the television website and broadcasted a video with a strong opposition message. The video started with footage of people in Tehran’s Azadi stadium shouting “death to dictator” referring to Supreme Leader Ali Kamenei, then it cut into a close up of a masked man similar to the protagonist of the movie V for Vendetta, who said “Khamenei is scared, the regime’s foundation is rattling”. Check Point Research provided in-depth technical analysis of one of the attacks. CPR was able to discover part of the tools that were utilized in this operation, including the evidence of the usage of a destructive wiper malware.

## FEBRUARY

### BELGIUM, GERMANY, NETHERLANDS
A significant Ransomware attack has disrupted operations of oil port terminals in Belgium, Germany and in the Netherlands, affecting at least 17 ports and resulting in difficulties loading and unloading refined product cargoes. The BlackCat cybercrime group is suspected to be the group behind the attack.

### UKRAINE
Ukraine has been at the center of a series of targeted DDoS attacks on its armed forces, defense ministry, public radio and national banks websites. The US Government has officially attributed the attacks to Russia’s Main Directorate of the General Staff of the Armed Forces.

State-sponsored Attack Groups Capitalise on Russia-Ukraine War for Cyber Espionage
CPR has observed advanced persistent threat (APT) groups around the world launching new campaigns, or quickly adapting ongoing ones to target victims with spear-phishing emails using the war as a lure.
[https://research.checkpoint.com/2022/state-sponsored-attack-groups-capitalise-on-russia-ukraine-war-for-cyber-espionage/](https://research.checkpoint.com/2022/state-sponsored-attack-groups-capitalise-on-russia-ukraine-war-for-cyber-espionage/)

Check Point Research has released data on cyberattacks observed around the Russia/ Ukraine conflict. Cyberattacks on Ukraine’s government and military sector surged by 196% in the first three days of combat. Cyberattacks on Russian organizations increased by 4%. Phishing emails in the East Slavic languages increased 7-fold.

## MARCH

### UKRAINE
Ukraine “IT army” consisting of cyber-operatives and volunteers worldwide has claimed attacks taking down multiple Russian and Belarusian key websites, including the Kremlin’s official site.

### RUSSIA
One of Russia’s largest meat producers Miratorg Agribusiness Holding has suffered a major cyberattack. Threat actors used Windows BitLocker to encrypt the victim’s IT systems in full volumes and demanded a ransom. The attack resulted in distribution disruptions for several days.

### GLOBAL
Following an announcement by OpenSea about a contract migration they are planning, Check Point Research observed that hackers took advantage of the upgrade process and scammed NFT users, leading to theft of millions of dollars.

### GLOBAL
As part of the NVIDIA leak by the Lapsus$ ransomware gang were 2 stolen code signing certificates used by to sign their drivers and executables. Attackers have already started using these certificates to sign malware, hoping to evade security solutions. Ransomware gang Lapsus$, which took responsibility for the breach on the giant chip firm NVIDIA, claims it also managed to breach the Korean manufacturer Samsung, and published 190GB of sensitive data online.

## APRIL

### GLOBAL
Check Point Research (CPR) revealed a large spike in attacks committed by advanced persistent threat groups (APTs) around the world, using lures utilizing the war between Russia and Ukraine. Most of the attacks started with spear-phishing emails that contained documents with malicious macros dropping malware such as Loki.Rat backdoor.

### SINGAPORE
The new Spring4shell vulnerability (CVE-2022-22965) has been actively exploited by threat actors since the beginning of April, leveraging the Mirai botnet. The Singapore region has been one of the most impacted geographic areas. Check Point Research shows that 16% of the organizations worldwide were impacted with Spring4Shell during the first 4 days after the vulnerability outbreak. VMware has released security updates to address this critical remote code execution flaw within its products.

### GLOBAL
Check Point Research identified “ALHACK”, a set of vulnerabilities in the ALAC audio format that could have been used for remote code execution on two-thirds of the world’s mobile devices. The vulnerabilities affected Android smartphones powered by chips from MediaTek and Qualcomm, the two largest mobile chipset manufacturers.

Check Point Research identified a vulnerability in the Everscale blockchain wallet. If exploited, the vulnerability would have given an attacker full control over a victim’s wallet and subsequent funds. The vulnerability was discovered in the web version of Everscale’s wallet, known as Ever Surf. Available on Google Play Store and Apple’s App Store, Ever Surf is a cross-platform messenger, blockchain browser, and crypto wallet for the Everscale blockchain network.

Blockchain Security 101
Every year, ordinary people lose money in blockchain hacks. Could it be that this technology is simply insecure by nature? Or is there something we’re all missing—something that can save this industry, and the millions of people who’ve invested their hard-earned money into it, from squandering billions of dollars every year?

Tune in to CP<RADIO> our Podcast channel for this insightful podcast
[https://research.checkpoint.com/2022/blockchain-security-101/](https://research.checkpoint.com/2022/blockchain-security-101/)

## MAY

### COSTA RICA
Costa Rica has declared a State of Emergency following a devastating ransomware attack by the Conti gang. The attack affected many governmental organizations, including The Finance Ministry, The Costa Rican Social Security Fund, and The Ministry of Science, Innovation, Technology, and Telecommunications. An estimated $200 million was lost due to disruptions related to the tax and customs platforms. The Conti Ransomware gang has allegedly taken its infrastructure offline after its leaders announced they were reorganizing their operation. The news comes a few days after Conti extorted Costa Rica. Conti members are believed to be currently migrating and rebranding into smaller ransomware operations.

### UNITED STATES
Lincoln College, a 157-year-old institution in Illinois, has announced it will indefinitely close after a significant ransomware attack that occurred in December 2021 took a toll on the school operations.

### RUSSIA
Sberbank, a Russian banking services organization, has been the target of continuous attacks in the past month by Pro-Ukraine hackers. The bank recently suffered the largest distributed denial-of-service (DDoS) attack ever recorded, measured at 450GB/sec.

### GLOBAL
Russian state-sponsored hacking group, Turla, has been launching a reconnaissance campaign against the Austrian Economic Chamber, a NATO platform, and the Baltic Defense College.

How the Evolution of Ransomware Changed the Threat Landscape From WannaCry to Conti: A 5 Year Perspective
[https://www.checkpoint.com/ransomware-hub/](https://www.checkpoint.com/ransomware-hub/)

## JUNE

### UKRAINE
CERT Ukraine has issued a warning concerning Russian hackers, possibly the state-sponsored APT group Sandworm, launching attacks exploiting the Follina critical vulnerability (CVE-2022-30190) in Microsoft Windows Support Diagnostic Tool. The campaign leverages malicious emails with DOCX attachments targeting media and news outlets in Ukraine.

### GLOBAL
The largest ever-recorded HTTPS DDoS attack has recently been mitigated, with 26 million request per second. The attack targeted a Cloudflare customer and originated from cloud service providers rather than residential internet service providers, indicating the use of hacked virtual machines.

### GLOBAL
Microsoft has issued a fix to address the critical Follina vulnerability (tracked CVE-2022-30190) which has been exploited in the wild, recommending users to urgently update and patch.

### GLOBAL
Russian intelligence services have reportedly increased attacks against governments and NGOs supporting Ukraine in 42 different countries, with the goal to obtain sensitive information from NATO countries’ agencies.

Check Point customers among the first to be protected from Follina Vulnerability
Check Point customers were protected on the same day Follina was discovered (May 30th). Utilizing Harmony Endpoint and Threat Emulation behavioral protections
[https://blog.checkpoint.com/2022/05/31/follina-zero-day-vulnerability-in-microsoft-office-check-point-customers-remain-protected/](https://blog.checkpoint.com/2022/05/31/follina-zero-day-vulnerability-in-microsoft-office-check-point-customers-remain-protected/)

## JULY

### NORWAY, LITHUANIA
Both Norway and Lithuania were victims of large-scale DDoS. The attacks are assumed to have been carried out by separate pro-Russian hacker groups, with the goal of discouraging the nations’ support of Ukraine.

### GLOBAL
Twitter has suffered a data breach after threat actors used a vulnerability to build a database of phone numbers and email addresses belonging to 5.4 million accounts, with the data now up for sale on a hacker forum for $30,000. It has been reported on a stolen data market that the database contains info about various accounts, including celebrities, companies, and random users.

Data Breaches. Is your Business Protected?
Download our guide to learn more about data breaches and the best practices you must follow to prevent them.
[https://pages.checkpoint.com/prevent-cyber-attack-data-breach.html](https://pages.checkpoint.com/prevent-cyber-attack-data-breach.html)

The New Era of Hacktivism—State-Mobilized Hacktivism Proliferates to the West and Beyond
In the past year, things have changed. As one of the multiple fallouts of conflicts in Eastern Europe and the Middle East, some hacktivism groups stepped up their activities in form and focus to a new era; Hacktivism is no longer just about social groups with fluid agendas.
[https://research.checkpoint.com/2022/the-new-era-of-hacktivism/](https://research.checkpoint.com/2022/the-new-era-of-hacktivism/)

## AUGUST

### GLOBAL
Atlassian Confluence critical vulnerability tracked CVE-2022-26138 has been exploited in the wild. Unauthenticated actors could leverage the flaw remotely to gain unrestricted access to all pages in confluence. In addition, CISA issued a warning and ordered US federal agencies to address the vulnerability.

### GLOBAL
Cisco confirms it has been breached by the Yanluowang ransomware group. The initial access was gained after the threat actor gained an employee’s Google account credentials, saved in their browser, and after getting an MFA push accepted by the user. The company says that while there have also been signs of pre-ransomware activity, no ransomware has been deployed on Cisco’s systems.

### UNITED STATES
The pro-Russian hacker group Killnet publicly targeted Lockheed Martin, calling other hacker groups to join in on attacks. At this point Killnet claims to be responsible for a recent DDoS attack on the company, and tells they have obtained personal data of the company’s employees; claims were denied by the American corporation.

### UNITED KINGDOM
South Staffordshire Water, UK’s largest water company supplying 330M liters of drinking water to 1.6M consumers daily, has been a victim of ransomware attack launched by Cl0p, a Russian-speaking ransomware gang. The group caused disruption of the company’s IT systems, allowing them access to more than 5TB of data including passports, screenshots from water treatment SCADA systems, driver’s licenses, and more.

### GLOBAL
Apple has issued an urgent patch for two zero-day flaws actively exploited by attackers to hack iPhones, iPads, or Macs. Among them is CVE-2022-32893, an out-of-bounds write vulnerability in WebKit that would allow an attacker to perform arbitrary code execution, and CVE-2022-32894, an out-of-bounds write vulnerability in the operating system’s kernel that would allow an attacker to execute code with kernel privileges.

### GLOBAL
Check Point Research has discovered an active cryptocurrency mining campaign imitating “Google Translate Desktop” and other free software to infect PCs. Created by a Turkish speaking entity called Nitrokod, the campaign counts 111,000 downloads in 11 countries since 2019.

## SEPTEMBER

### RUSSIA
A traffic jam was generated in Moscow in a kind of physical DDoS attack, as attackers hacked Russian taxi service Yandex, and ordered dozens of cars to a specific location. The Anonymous collective claims to be behind this attack.

### ALBANIA
Multiple cyberattacks linked to Iran have been disrupting Albania’s government systems since July, forcing them to shut down some online services. In response, Albania’s government halted its diplomatic ties with Iran, ordering staff to leave within 24 hours. The latest attack which occurred over the weekend, allegedly by the same actor, targeted the Albanian Police’s computer system, forcing officials to take its TIMS system, used for immigration data tracking, offline.

### GLOBAL
Uber has suffered a data breach, allegedly by an 18-year-old hacker who managed to gain access using social engineering tactics on an employee. The hacker claims to have access to Uber’s internal IT systems and to the company’s HackerOne bug bounty account, which contains vulnerabilities in Uber’s systems and apps, disclosed privately by security researchers. Uber claims that the users’ private information was not compromised.

### GLOBAL
A new record-breaking DDoS attack in has been recorded this week, peaking at 704.8 Mpps, about 7% higher than the previous attack recorded on the same European organization last July.

## OCTOBER

### IRAN
Hacktivist groups around the world have taken aim at the Iranian regime, as protests throughout the country continue. The groups have been leaking information relating to Iranian government officials, and offering support to the protesters in sharing information and evading censorship.

### AUSTRALIA
Personal information of 10 million Australians has been stolen in a breach of telecom company Optus. The data includes sensitive information, such as passport and healthcare details. While the hackers initially demanded a 1M USD ransom, they later retracted their demand due to the high attention drawn to the hack and the law enforcement operation initiated to identify the attackers.

### GLOBAL
Check Point Research published a report studying the rising trend of state-mobilized Hacktivism. While in the past Hacktivist groups tended not to affiliate themselves with national interests, groups nowadays take part in state-directed efforts, driven by geopolitical conflicts.

### UNITED STATES
Russian-speaking threat group Killnet claims responsibility for attacks taking down different US state government websites, including those of Colorado, Kentucky, Mississippi and others.

### AUSTRALIA
Online shopping company Woolworths has reported a data breach impacting over two million Australian users of its MyDeal subsidiary. The company said the breach was due to a compromised user credential that was used to gain unauthorized access to MyDeal’s customer relationship management system. Several Australian companies have been breached during October—The country’s largest health insurance firm, Medibank, froze trading on the Australian stock exchange after confirming a 200GB data breach; In a breach of wine retailer Vinomofo’s network data of over 500,000 customers was leaked; an attack on energy company EnergyAustralia exposed payment data of hundreds of the company’s customers.

Pulling the Curtains on Azov Ransomware: Not a Skidsware but Polymorphic Wiper
CPR provides under-the-hood details of its analysis of the infamous Azov Ransomware
[https://research.checkpoint.com/2022/pulling-the-curtains-on-azov-ransomware-not-a-skidsware-but-polymorphic-wiper/](https://research.checkpoint.com/2022/pulling-the-curtains-on-azov-ransomware-not-a-skidsware-but-polymorphic-wiper/)

## NOVEMBER

### BULGARIA
Russian-affiliated hacktivist group ‘Killnet’ has launched a DDoS attack against government websites in Bulgaria, causing them to become inaccessible. Killnet said that Bulgaria was targeted due to its “betrayal to Russia” and the supply of weapons to Ukraine.

### GLOBAL
The Largest copper manufacturer in Europe—Aurubis—has been the victim of a cyberattack that targeted its IT systems and forced the company to shut down many of its sites’ systems.

### GLOBAL
OpenSSL, used widely for secure communications, gave heads-up for a critical vulnerability in versions 3.0 and above that will be published on Tuesday, November 1st. eventually the vulnerabilities published were downgraded to ‘high’ severity

### GLOBAL
Check Point Research found that global attacks increased by 28% in the third quarter of 2022, with education/research as the most attacked industry overall, and the healthcare sector the most targeted industry in ransomware attacks.

## DECEMBER

### RUSSIA
IT Army of Ukraine claim to have gained access to Russia’s Central Bank. They published 27K of the leaked files, containing personal, legal, and financial data.

### GLOBAL
Check Point Research identified a new and unique malicious package on PyPI, the leading package index used by developers for the Python programming language. The package was designed to hide code in images and infect through open-source projects on Github.

### GLOBAL
The Azov ransomware is being distributed worldwide to encrypt victim files, while in fact an analysis by Check Point Research proves that Azov ransomware is a data wiper aimed at destroying data with no way to recover the files.

### UNITED STATES
Meta has fired dozens of employees, after the employees had received thousands of dollars in bribes by outside hackers in return for granting access to users’ Facebook or Instagram profiles. The employees used the company’s internal support tool, which allows full access to any user account.

### EUROPE
The European Parliament website has been attacked following a vote declaring Russia a state sponsor of terrorism. The pro-Russian hacktivist groups Anonymous Russia and Killnet, have claimed responsibility for the attack, causing an ongoing DDoS (Distributed Denial of Service).

### GLOBAL
Black Basta ransomware group is running a campaign targeting organizations in the United States, Canada, United Kingdom, Australia, and New Zealand. The group uses QakBot (AKA QBot, Pinkslipbot) banking Trojan to infect an environment and install a backdoor allowing it to drop the ransomware.

### AUSTRALIA
Cyber criminals who breached Australian Medibank’s systems have released another batch of data onto the dark web, claiming that the files contain all data harvested in the former heist that impacted 9.7 million customers in October 2022. Medibank has confirmed the data breach.

### GLOBAL
Researchers found that over 300,000 users across 71 countries were effected by an Android campaign meant to steal Facebook credentials. This is by using Schoolyard Bully Mobile Trojan, deployed in legitimate education-themed applications, which were available in the official Google Play Store.

### GLOBAL
Check Point Research has analyzed the activity of cyber-espionage group Cloud Atlas. Since its discovery in 2014, the group has launched multiple, highly targeted attacks on critical infrastructure across geographical zones and political conflicts, however its scope has narrowed significantly in the last year, with a clear focus on Russia, Belarus and conflicted areas in Ukraine and Moldova.

### GLOBAL
As artificial intelligence (AI) models grow more and more popular, Check Point Research discusses the risks and upsides of the technology. CPR demonstrates how AI technologies, like ChatGPT and Codex, can easily be used to create a full infection flow, from spear-phishing to running a reverse shell, and provides examples of the positive impact of AI on the defenders’ side.

# CHAPTER 3: 2022'S CYBER SECURITY TRENDS

## RUSSO-UKRAINIAN CONFLICT

The ongoing Russian-Ukrainian war has had a profound effect on cyberspace and caused a significant increase in cyber-attacks in 2022. Hacktivism has been transformed, and the use of destructive malware by state-sponsored groups and independent entities has become more prevalent globally.

The role of cyberwarfare has been well documented in this first full-blown hybrid conflict, where battles are fought online as well as on physical ground. The Russians revealed new cyber tools and achieved tactical objectives that affected military and civil communications, including blocking public media transmissions. While cyber activity cannot win the war on its own, it does play a significant part in tactical operations and has an indisputable psychological and economic effect. For cyber-operations to be effective, is not just a matter of employing malware. Much like conventional warfare, cyberwarfare also requires meticulous and thorough preparations. Reconnaissance, intelligence gathering and assessment, target-bank compilation and prioritization, dedicated-payload development and network infiltration are all prerequisites for a successful campaign.

As was the case on the physical battleground, the Russians apparently did not prepare for a long cyber campaign. Their cyber operations, which in the early stages included carefully planned precise attacks, have all but ceased. Multiple new tools and wipers, that were characteristic of the initial stages, have been replaced with a different operational mode. Current offensive cyberattacks are mostly rapid exploitations of opportunities as they arise and use already known attack tools. These are not intended to assist tactical combat efforts but rather create a psychological effect by damaging the Ukrainian civil infrastructure.

The recruitment of cyber professionals, criminals, and other civilians to the military cyber effort—on both sides of the conflict—has further blurred the distinction between nation-state actors, cyber criminals, and hacktivists. The Ukrainian government has established an army of hacktivists whose management is very different from anything we have seen before. Previously characterized by loose cooperation between individuals in an ad hoc fashion, new-hacktivist organizations conduct recruitment, training, intelligence-gathering and allocation of targets and battlefield status compilation in a military manner. Attacks on Russian entities, which were once considered off-limits by many cybercrime entities, have now increased and Russia is struggling under an unprecedented hacking wave that combines state-sponsored activity, political cyber warriors and criminal action. On the other side, multiple Russian-affiliated hacktivist groups were established that target not only Ukraine but also Europe, North America and Japan. For more details, see our section on Hacktivism.

The extensive use of destructive malware has already resulted in an increase in similar activities in other regions and by other geopolitical groups. Can cyberattacks be considered a hostile act? What type of proof, and how extensive must the damage be to be considered a casus belli? Are modifications to existing treaties required? We address these questions in another chapter of the report entitled “Wipers”.

Eight years of continuous cyber hostility between Russia and Ukraine have served as a training period for both sides. Ukraine’s cyber defense organizations are praised as “the most effective defensive cyber activity in history”. Knowing adversaries tools and modus operandi has an increased importance in cyber warfare. The impact of a first-time deployment of a particular wiper may be devastating, but the impact of the second one is often much smaller. For example, the effect of the Industroyer2 attack on the energy sector in Ukraine in March 2022 was limited in comparison to Industroyer’s first deployment in 2016.

The full scope of changes brought on by this conflict is yet to be seen, but we have already learned some valuable lessons.

SERGEY SHYKEVICH
Threat Intelligence Group Manager, Check Point Software Technologies

> The role of cyberwarfare has been well documented in this first full-blown hybrid conflict, where battles are fought online as well as on physical ground. The Russians revealed new cyber tools and achieved tactical objectives that affected military and civil communications, including blocking public media transmissions. While cyber activity cannot win the war on its own, it does play a significant part in tactical operations and has an indisputable psychological and economic effect.

## THE YEAR OF UNRESTRAINED WIPER DISRUPTION

Wipers and other types of destructive malware are carefully designed to cause irreversible damage, and if tightly woven into cyberwarfare, the effect can be catastrophic. This is probably why we have only seen limited use of wipers over the years, and they were usually associated with nation states. Until recently, countries primarily used cyberattacks for the purpose of espionage and intelligence gathering, and only rarely resorted to destructive cyber tools. In 2022 we have seen a change in the appearance of multiple new wiper families that are used to destroy thousands of machines.

Wipers are destructive malware, designed to inflict damage with limited potential for financial gain for attackers. Early use of wipers to showcase attackers’ capabilities was thus limited and short-lived. But in all the cases, the main purpose of the wipers is to interrupt operations or to irreversibly destruct data. While the process of data destruction has several technological implementations.

Stuxnet, arguably the most famous destructive malware, was used in 2010 to sabotage the centrifuges in the Iranian nuclear project. At the time, Stuxnet was unique in many respects but mostly because its immediate impact was the physical destruction of mechanical hardware. In 2012, Shamoon was deployed to disrupt oil companies in the Middle East, targeting Saudi and Qatari facilities. In 2013, DarkSeoul, attributed to North Korea, was used to destroy more than 30,000 computers related to the banking and broadcasting sectors in South Korea. This attack took place during a period of heightened tensions between the two countries following nuclear testing by the North.

In the ensuing years we witnessed the Black Energy attack in 2015 on the Ukrainian energy infrastructure (KillDisk) and another attack on Saudi targets by dubbed Shamoon2 in 2016. NotPetya was distributed against Ukrainian targets in 2017 in a supply chain attack which caused significant collateral damage globally.

In 2018 Olympic Destroyer, purportedly produced by North Korea, was used by the Russian-affiliated Sandworm to disrupt the opening ceremonies of the Winter Olympic Games. In 2019 Dustman and ZeroCleare were used in Iranian attacks on targets in the Middle East related to oil production. On average, there was one attack by a wiper family per year.

During 2022, there has been a noticeable shift in the tactics of destructive malware deployment. Cyberespionage continued, as it was previously, but this activity has been supplemented by destructive cyber operations, instigated by nations whose goal appears to be to inflict as much damage as possible. The start of the Russian-Ukrainian war in February saw a massive uptick in disruptive cyberattacks carried out by Russia against Ukraine. Russia has a long history of cyber assaults against its neighbor. In January 2022, WhisperGate was used to attack government and financial organizations in Ukraine, overwriting systems’ MBR (Master Boot Record) to prevent system reboot and file recovery. Attackers left a ransom note but did not offer a recovery mechanism, leading to speculation that the demand for payment was only intended to mislead victims. The files were further corrupted using a second stage payload that was hosted on a Discord channel.

On the eve of the ground invasion in February, three additional wipers were deployed: Hermetic wiper, HermeticWizard and HermeticRansom. The tools were named after their certificate which was issued to ‘Hermetica Digital Ltd’. Additional wipers were reported later that month. Another attack was directed at the Ukrainian power grid in April, using a new version of Industroyer, the malware that was used in a similar attack in 2016.

ELI SMADJA
Security Research Group Manager, Check Point Software Technologies

> Wipers and other types of destructive malware are carefully designed to cause irreversible damage, and if tightly woven into cyberwarfare, the effect can be catastrophic. This is probably why we have only seen limited use of wipers over the years, and they were usually associated with nation states. Until recently, countries primarily used cyberattacks for the purpose of espionage and intelligence gathering, and only rarely resorted to destructive cyber tools. In 2022 we have seen a change in the appearance of multiple new wiper families that are used to destroy thousands of machines.

In total, there were at least nine different wipers deployed in Ukraine in less than a year. Many of them were most likely separately developed by different Russian intelligence services and employed different wiping and evasion mechanisms.

One of the attacks, enacted hours before the ground invasion of Ukraine, was intended to interfere with Viasat, satellite communications company that provided services to Ukraine. The attack used a wiper called AcidRain that was designed to wipe modems and routers and cut off internet access for tens of thousands of systems. There was also significant collateral damage, including thousands of wind turbines in Germany.

The attacks were clearly the result of detailed planning. Some of the tools were designed specifically to fit their intended targets, with attackers breaching security measures and gaining access months earlier and then using GPOs (Group Policy Objects) to deploy their wipers at the time of the actual attack.

Cyber destructive activity was not restricted to Russia-Ukraine. In the Middle East, Iran has suffered a series of destructive attacks since the middle of 2021. In July 2021, a hacktivist group identifying itself as Predatory Sparrow attacked Iran’s railway system, causing delays and general panic. An investigation by Check Point Research (cp<r>) revealed that older versions of the wipers were used in attacks against multiple targets in Syria.

In January 2022, the Iranian state broadcasting service IRIB was attacked