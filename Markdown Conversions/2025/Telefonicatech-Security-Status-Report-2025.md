# Security Status Report 2025 H1

## Table of Contents
- [Executive Overview](#executive-overview)
- [Highlights of the First Half of 2025](#highlights-of-the-first-half-of-2025)
- [Mobiles](#mobiles)
  - [Apple iOS](#apple-ios)
  - [Apple Transparency Report](#apple-transparency-report)
  - [Android](#android)
- [Significant Vulnerabilities](#significant-vulnerabilities)
  - [Vulnerabilities in figures](#vulnerabilities-in-figures)
- [APT Operations, Organised Groups, and Associated Malware](#apt-operations-organised-groups-and-associated-malware)
- [OT Threat Analysis](#ot-threat-analysis)
- [Threat Study by Indicator](#threat-study-by-indicator)
- [Useful Links](#useful-links)

---

2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Página 1 de 43

---

Security Status Report 2025 H1

Índex

EXECUTIVE OVERVIEW ................................................................................................................................ 3

HIGHLIGHTS OF THE FIRST HALF OF 2025 ................................................................................................ 5

MOBILES ......................................................................................................................................................... 9

Apple iOS ..................................................................................................................................................................................................................... 9

Apple Transparency Report ............................................................................................................................................................... 11

Android ........................................................................................................................................................................................................ 15

SIGNIFICANT VULNERABILITIES ............................................................................................................... 20

Vulnerabilities in figures ....................................................................................................................................................................... 21

APT OPERATIONS, ORGANISED GROUPS, AND ASSOCIATED MALWARE ........................................ 24

OT THREAT ANALYSIS ................................................................................................................................ 26

THREAT STUDY BY INDICATOR ................................................................................................................. 31

USEFUL LINKS ............................................................................................................................................. 38

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 2 de 37

---

Security Status Report 2025 H1

# EXECUTIVE OVERVIEW

The purpose of this report is to synthesize the cyber security information of the last few months (from mobile security to the most relevant news and the most common vulnerabilities), adopting a point of view that covers most aspects of this discipline, in order to help the reader understand the risks of the current landscape.

This semester, two news items stand out. Although apparently unrelated, we believe they have a common denominator.

The U.S. government announced in April 2025 that it would stop funding MITRE to operate and maintain the Common Vulnerabilities and Exposures (CVE) system. This system has been managed by MITRE since 1999 with funding from the Department of Homeland Security (DHS) and the Cybersecurity and Infrastructure Security Agency (CISA). Yosry Barsoum, vice president of MITRE, warned that the contract would expire on April 16, 2025, and that, if not renewed, there would be serious consequences. The main reason pointed to be a budget cut driven by the Trump administration, although CISA and other sources did not publicly detail the exact reasons.

The potential service disruption generated alarm in the cyber security community. Fortunately, hours before the expiration, CISA stepped in and temporarily renewed MITRE's contract, avoiding an immediate disruption of CVE services. This solution was yet considered temporary and highlighted the fragility of relying on a single government funder for such a critical resource. In response, the creation of the CVE Foundation, an independent entity driven by members of the CVE board itself, was announced. The entity will ensure the long-term sustainability and neutrality of the system.

as Google, Apple, Facebook, GitHub, Telegram... and even government portals. The investigation was led by the Cybernews team, which detected at least 30 databases of different sizes, some with more than 3.5 billion records each. It did not look like an attack on a single company, but a massive collection of thefts. It was eventually learned that the alleged “leak” of 16 billion passwords was not a new leak or a recent attack, but a compilation of credentials previously stolen over the years through infostealer-type malware, previous breaches and credential stuffing attacks. The affected sites were not recently compromised to obtain these credentials.

What happened (as other times) is that a massive database was compiled and exposed, composed of records already circulating in underground forums and marketplaces. There is no evidence that it contains unpublished data (or at least, not a relevant amount) or extracted from new breaches. The first news went unnoticed by the mainstream media. While the cyber security industry was biting its nails for 24 hours for fear of losing the CVE system, the world went on. The second news, in contrast, opened generic news in all countries, with front pages and reports. Everyone knew about the leak. In this case, the world was on edge while the industry suspected (by pure logic) that it was a compilation of old thefts of no great significance. The numbers were not so much in technical reality as in a headline.

On the other hand, in June, what appeared to be one of the biggest cyber security incidents in history was revealed: the leak of 16 billion passwords and login credentials for services such

When the continuity of CVE was compromised, the alarm was immediate: experts, companies, and security managers realized that losing this infrastructure meant flying blind in the face of

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 3 de 37

---

Security Status Report 2025 H1

vulnerabilities, a chaos that would affect incident response, infrastructure protection and global coordination. However, the password leak, despite its enormous media coverage, did not generate the same professional concern because, in essence, it did not alter the threat landscape or introduce new risks: it was, above all, noise and recycling of already exposed data.
This phenomenon highlights a persistent gap between what really matters in the industry for digital resilience and what the headlines capture.
The media tends to amplify the most spectacular or easily understood incidents, even if their real impact is limited, while structural issues - such as critical infrastructure financing and governance - are relegated or overlooked.

This not only distorts the user's perception, who often ends up believing any amplified alarm without context, but also reflects a certain immaturity in news coverage: the right experts are

rarely consulted and the underlying technical consequences are rarely explained. The industry, for its part, reveals that what is really important is not always what is most visible, and that security depends more on the solidity of its foundations - such as CVE - than on the sensational nature of the incidents that make the front pages. Are we still, perhaps, too far removed from the user?

Whether you are an amateur or a professional, it is important to be able to keep up with relevant cyber security news: what is the most relevant thing going on? What is the current landscape?
Through this report, the reader will have a tool to understand the state of security from different perspectives and will be able to learn about its current state and project possible short-term trends. The information gathered is based in large part on the compilation and synthesis of internal data, contrasted with public information from sources we consider to be of quality. Let's go!

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 4 de 37

---

Security Status Report 2025 H1

# HIGHLIGHTS OF THE FIRST HALF OF 2025

The following are the news items that have had the greatest impact during the first half of 2025.

## JANUARY

*   A flaw that allows hibernate images to be retrieved in clear text is identified, potentially exposing passwords and sensitive data if an attacker has physical access to the BitLocker-encrypted hard drive (CVE-2025-21210). This won't be the only problem with this technology this year.

*   Two serious vulnerabilities are discovered in SAP: CVE-2025-0070, Improper Authentication in SAP NetWeaver AS for ABAP and ABAP Platform, which allows an authenticated attacker to gain illegitimate access to the system by exploiting improper authentication checks. In addition to CVE-2025-0066, an information disclosure in SAP NetWeaver AS for ABAP and ABAP Platform (Internet Communication Framework).

*   A so-called “Belsen Group” leaks configuration files, IP addresses, and VPN credentials of more than 15,000 FortiGate devices from around the world, both public and private sector, for free on the dark web. The 1.6 GB dump includes sensitive information such as clear text passwords, private keys and firewall rules, and has been collected after exploiting vulnerability CVE-2022-40684 in 2022.
*   Moxa, a provider of industrial communications and networks, issues an urgent advisory on January 3 about two high-impact breaches. There are no mitigation measures available for some of the affected devices at the time. One of these vulnerabilities allows control of affected devices and systems to be taken over remotely.

*   Xlab publishes research on a Mirai-based botnet that is exploiting 0-day vulnerabilities in industrial and home routers. The botnet handles about 15,000 bots daily and most of them are located in the USA, China, Russia, Iran, and Turkey. The most common activity of this botnet is DDoS attacks.
*   Although it occurred in October, it becomes known in January. Cloudflare mitigates the largest DDoS attack ever recorded, which peaks at 5.6 terabits per second. The attack is launched by a Mirai-based botnet with 13,000 compromised devices, it targets an Internet service provider in East Asia and lasts only 80 seconds.

## FEBRUARY

*   A 0-day vulnerability in 7-Zip (CVE-2025-0411) was detected in September 2024 that allowed Russian attackers to bypass “Mark of the Web” (MoTW) protection in Windows using double-nested compressed files. This flaw is exploited during February in phishing campaigns targeting Ukrainian government agencies and companies, allowing the execution of malware such as SmokeLoader without displaying security warnings to the user.

*   At least 28 apps on Google Play and Apple's App Store included malware, known as SparkCat or SparkKitty, designed to steal cryptocurrency wallet recovery phrases using optical character recognition (OCR) techniques. This malware, hidden in legitimate apps and downloaded more than 242,000 times, accesses the device's image gallery and searches for screenshots with keywords associated with cryptocurrencies, allowing attackers to empty victims' wallets. This is the first time such a stealer has managed to infiltrate the App Store.

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 5 de 37

---

Security Status Report 2025 H1

*   The FBI blames North Korea, through the APT Group “Lazarus”, for the theft of 1.5 billion dollars from the cryptoasset exchange Bybit. In this operation, which the FBI called “TraderTraitor” and is listed as the largest cryptoasset theft in history, the criminals manages to breach one of the cold wallets, considered secure, accessing the funds and splitting them into multiple wallets to make them harder to trace.

*   Lee Enterprises, one of the largest newspaper groups in the United States, says a cyberattack affecting its systems caused a disruption in February and impacted its operations. These operations include worker access to the system, making it impossible to deliver articles, print, and deliver dozens of newspapers.
This company, which publishes 77 daily newspapers with a daily circulation of 1.2 million, 350 weeklies and digital editions with more than 44 million unique visitors, was already attacked in 2020 by Iranian cybercriminals during the presidential election campaign.

*   According to chainAnalysis, in 2024, ransomware payments fell by 35% compared to the previous year, totaling $813.55 million compared to $1.25 billion in 2023, despite record attack volumes. Only 30% of victims who negotiated with cybercriminals eventually paid up.

*   Two critical vulnerabilities are discovered in OpenSSH: one, identified as CVE-2025-26465, allows (MitM) type attacks against OpenSSH customers when the VerifyHostKeyDNS option ware enabled. This flaw has existed since 2014 and particularly affected FreeBSD systems where the option was enabled by default. The second one, CVE-2025-26466, introduced in 2023, allows denial-of-service (DoS) attacks before authentication.

## MARCH

*   The GreyNoise research group detects a backdoor campaign affecting thousands of ASUS routers. According to the researchers, this movement would be focused on the establishment of a future botnet.

*   Proofpoint researchers identify a highly targeted email campaign aimed at fewer than five Proofpoint customers in the United Arab Emirates related to aviation and satellite communications, as well as critical transportation infrastructure. This campaign exposes a backdoor called Sosano and the use of polyglots to obfuscate the payload content. These files are specially designed so that different applications interpret them as different file types.

*   Truffle Security researchers discover nearly 12,000 API keys and valid passwords (including AWS, MailChimp and WalkScore credentials) within the Common Crawl dataset, widely used to train artificial intelligence models from companies such as OpenAI, Google and Meta, many of them hardcoded in HTML and JavaScript.

*   YouTube warns of a sophisticated phishing campaign in which cybercriminals use an AI-generated video simulating the platform's CEO, Neal Mohan, announcing fake changes to the monetization policy. The attackers send this deepfake as a private video to content creators, along with emails that include links to a fake YouTube Partner Program verification page. Attempting to “confirm” the new terms, victims hand over their credentials.

*   Researchers identify a massive malware campaign called “Steam”, in which 331 malicious apps on Google Play, disguised as utilities such as health trackers, battery optimizers or QR scanners, achieves more than 60 million downloads. These initially legitimate apps to bypass

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 6 de 37

---

Security Status Report 2025 H1

Google's controls, download malicious code after installation to display intrusive ads, steal credentials and card data through phishing, and make them difficult to remove by hiding their icon and activity.

*   Researchers warn about the massive exploitation of the critical vulnerability CVE-2024-4577 in PHP for Windows, which allows remote code execution on servers using PHP in CGI mode. Although the flaw was patched in June 2024, attackers quickly exploited the exploit, especially in Japan, and then globally, with more than 1,000 unique IPs attempting to exploit the vulnerability in January alone.

## APRIL

*   The FBI, through the Internet Crime and Complaint Center (IC3), states that the U.S. lost more than $16.6 billion in 2024. As a reference, in 2023 the reported losses were $12.5 billion. It should be cautioned that, although the figure is very striking, it only reflects activity detected by the IC3 or reported by victims, so it represents only a portion of the final amount.

*   Renal dialysis company DaVita discloses that it suffered a ransomware attack that encrypted parts of its network and impacted some of its operations. Days later, the cybercriminal group Interlock claims credit for the attack and announced that it had 20 terabytes of the company's confidential information. According to the same group, negotiations with the company were unsuccessful, so they put the information up for sale. DaVita has annual revenues in excess of $12.8 billion.

*   GitHub detects more than 39 million leaked secrets in repositories, including API keys and credentials, exposing users and organizations to serious security risks. Despite measures such as push protection enabled by default on public repositories.

*   A critical remote code execution (RCE) vulnerability has been discovered in Apache Parquet, a data storage format widely used in big data and analytics environments, especially on platforms such as Hadoop, AWS, Google Cloud and Azure. It is identified as CVE-2025-30065 and has a maximum CVSS score of 10.0.

*   A massive campaign is discovered in April in which at least ten malicious extensions for Visual Studio Code, published on Microsoft's official marketplace, infected thousands of Windows users with the XMRig cryptominer for Monero.These extensions, which pretended to be legitimate development tools such as “Prettier”, “Discord Rich Presence” or “Solidity Compiler”, accumulates hundreds of thousands of downloads, many of them artificially inflated to appear popular.

*   Google Chrome 136 fixes a vulnerability that had been allowing websites to identify users' browsing history by analyzing the color of links visited with the CSS :visited selector for more than 20 years. This flaw allows malicious sites to track, profile and even launch phishing attacks by detecting which links a user has visited on other sites.

## MAY

*   A joint police operation carried out by Dutch and US authorities dismantles a botnet consisting of some 7,000 Internet of Things (IoT) devices and others in an End of Life (EoL) state. The

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 7 de 37

---

Security Status Report 2025 H1

network was rented to provide anonymity to the attackers. Attackers paid between $9.95 and $110 per month, generating revenues of more than $46 million.

*   Arla Foods, the Danish food industry giant, confirms that it was the target of a cyberattack that disrupts its production operations at a dairy plant in Germany. This attack forced the company to inform its customers of delays in their orders.

*   A supply chain attack targeting Linux servers is detected, where three malicious Go modules published on GitHub contained obfuscated code that downloaded and executed a Bash script capable of completely overwriting the main disk (/dev/sda) with zeros. This action causes total and irreversible data loss and renders the systems unusable. The modules, which imitated legitimate projects, are quickly removed.

*   The LockBit criminal organization suffers an internal breach when its administration and affiliate panels on the dark web were attacked and replaced with a warning message along with a link to download a copy of its MySQL database. The dump exposes key operational details: more than 59,000 bitcoin addresses, attack configurations, affiliate credentials and, especially, more than 4,400 records of negotiations between victims and extortionists since December 2024.
*   Researchers uncover a massive campaign that introduced more than 100 malicious extensions to the Chrome Web Store, masquerading as legitimate tools such as VPNs, AI assistants and utilities from well-known brands such as Fortinet and YouTube. These extensions, promote through fake websites and malvertising, offer some of the promised functionality, but in reality, they steal cookies, credentials and browsing data, can execute remote scripts, modify traffic and turn the browser into a proxy for the attackers.

## JUNE

*   WestJet, Canada's second largest airline, confirms a cyberattack that disrupted access to some internal systems. The attack also prevents users from logging into the website and mobile app, services that were restored by now.

*

*   A new attack named ‘SmartAttack’ uses smartwatches as covert ultrasonic signal receivers to extract data from physically isolated systems through the “Airgap” technique, used in many industrial environments. This technique can also interfere with the performance of RAM, displays, SATA cables... etc. Even if the reception of these signals can be done through Smartwatch, still someone must have compromised the Airgap isolated device.
In June 2025, CVE-2025-49113, a critical remote code execution (RCE) vulnerability in Roundcube Webmail affecting all versions from 1.1.0 to 1.6.10, is disclosed. The flaw, caused by a lack of validation on the _from parameter in the upload.php script, allows an authenticated attacker to execute malicious code on the server, compromising the security of the platform. More than 84,000 Roundcube instances remain vulnerable.
In June 2025, two critical local privilege escalation vulnerabilities are discovered in Linux, CVE-2025-6018 and CVE-2025-6019, which allow any user with access to a session (even via SSH) to gain root permissions on most modern distributions. The first flaw, in SUSE's PAM configuration, grants “allow_active” privileges to remote users; the second, in libblockdev and the udisks daemon (present by default in almost all Linux systems), allows these users to elevate themselves to root with very little effort.

*

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 8 de 37

---

Security Status Report 2025 H1

*

It is reported that more than 46,000 instances of Grafana exposed to the Internet remain vulnerable to the critical flaw CVE-2025-4123, an open redirect and XSS issue that allows attackers to execute malicious plugins and hijack user accounts via a simple link. The exploit, which does not require elevated privileges and can run even with anonymous access enabled, allows session hijacking, credential switching and, in some cases, SSRF attacks against internal systems.

# MOBILES

## Apple iOS

The new iOS 18 security improvements

We will have to wait until after the summer to know the security improvements of the new version of iOS.

What we do know, so far, is that it will not be called iOS 19 but iOS 26. We are moving from linear numbering to naming the operating systems in a unified way according to the year; but even though it will be released in 2025, the name will be brought forward to the next one.

In the following report we will reveal the new security features that iOS 26 will bring us.

Vulnerabilities and versions released in the first half of 2025

We closed out 2024 with iOS 18.2. 2025 didn’t take long to bring a new update, although in this case, it didn’t include any security fixes. On January 6, iOS 18.2.1 was released.

It wasn’t until January 27 that the first patches arrived. That day, Apple released iOS 18.3, which addressed 38 CVEs — some of them affecting the kernel, with the potential for arbitrary code execution or privilege escalation. Notably, CVE-2025-24085, a vulnerability in CoreMedia, was being actively exploited by attackers to escalate privileges on iOS versions prior to 17.2.

On February 10, Apple issued an emergency update: iOS 18.3.1. This patch addressed a very specific vulnerability, known to have been exploited in a targeted attack against a high-profile individual. Specifically, the update fixed an issue allowing access to a locked iPhone (CVE-2025-24200).

The alarms didn’t stop there. On March 11, Apple released iOS 18.3.2 to patch another vulnerability that had been used in highly targeted attacks. This time, it was a WebKit buffer overflow (out-of-bounds write), registered as CVE-2025-24201.

Given the severity of these two vulnerabilities, Apple also decided to release updates for older devices. On March 31, versions 15.8.4 and 16.7.11 were published to address the same issues on legacy systems.

That same day, iOS 18.4 was released, patching a staggering 75 unique vulnerabilities. Despite the high number, only one of them — CVE-2025-24243, involving the Audio component — could be exploited to execute arbitrary code.

On April 16, Apple released another critical update: iOS 18.4.1. It patched two zero-day vulnerabilities that had been actively exploited in targeted operations — similar to previous cases. One was in the CoreAudio component, and the other in RPAC (Reconfigurable Preprocessing Architecture Core).

From that point until May 12 — the release date of iOS 18.5 — no further incidents were reported. This update addressed 33 vulnerabilities, including two that could allow arbitrary code execution.

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 9 de 37

---

Security Status Report 2025 H1

Evolution of vulnerabilities in iOS during the first half of 2025

This number is similar to that of the first half of 2025, which is slightly higher with 153 patches.

The second half of 2024 closed with 149 patched vulnerabilities, four considered high-risk, with the possibility of executing arbitrary code.

VULNERABILITTIES IN IOS 2025-H1
Evolution of vulnerabilities by year

Total vulnerabilities found

Category within "arbitrary code
execution"

387

387

112

69

211

122

96

50

51

163

222

125

156

187

78

63

261

267 260

163

153

13

37 48

66

21

28

22

1
0

9
2

27

6

32

14

37

10

2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025

Fragmentation of versions during the first half of 2025

Fragmentation has never been traditionally an issue for iOS developers. The advantage of having a homogeneous platform is undisputed and continues to yield near-identical figures every time we review iPhone user adoption of a new version of the operating system.

And no wonder. The first four share positions are occupied by iOS 18 and its different versions.

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 10 de 37

---

Security Status Report 2025 H1

FRAGMENTACIÓN EN APPLE iOS 2025-H1

Others

21,86%

3,34%

5,72%

5,97%

16.7

18.2

17.6

18.5

18.4

18.1

18.3

9,09%

10,85%

16,12%

27,05%

0,00%

5,00%

10,00%

15,00%

20,00%

25,00%

30,00%

That said, we have a 21.86% share that does not specify version, so it is a bag of versions that we cannot identify and could be supported or not.

The latest version supported by Apple is iOS 15, released in September 2021.

## Apple Transparency Report

Governments sometimes need to rely on large corporations to do their job. When a threat involves knowing the identity or having access to the data of a potential attacker or a victim in danger, the digital information stored by these companies can prove vital to the investigation and avert a catastrophe. Apple publishes a comprehensive report every six months on what data governments request from it, which data and to what extent the requests are fulfilled. We update here some data we have extracted from information published by Apple for the second half of 2023 and first half of 2024 (the latest published by Apple as of the first half of 2025) on government activities and requests to the company.

### Device-based requests

It represents requests from government agencies requesting Apple device information, such as serial number or IMEI number. When law enforcement acts on behalf of customers who, for example, have had their device stolen or lost. It also receives requests related to fraud investigations: they typically request details of Apple customers associated with Apple devices or connections to Apple services.

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 11 de 37

---

Security Status Report 2025 H1

Country

Requests
2023-H2

Accepted
2023-H2

Requests
2024-H1

Accepted
2024-H1

Addition

% Accepted

United States

6.410

5.233

12.043

10.377

18.543

Germany

8.866

4.463

9.778

4.713

18.644

China
mainland

905

853

1.212

1.146

2.117

Brazil

5.858

4.765

8.776

6.808

14.634

United
Kingdom

1.633

1.337

2.925

2.278

4.558

85%

49%

94%

79%

79%

Spain

620

290

540

186

1.160

41%

As usual, Germany leads the way in requests for device information, although in 2024 the United States made a strong comeback. Brazil is also a major player here. In Spain, there is a curious detail: the acceptance rate is quite low.

### Requests based on financial data

These requests happen when law enforcement acts on behalf of customers who require assistance related to fraudulent credit card or gift card activity that has been used to purchase Apple products.

Country

Requests
2023-H2

Data Prov.
2023-H2

Requests
2024-H1

Data Prov.
2024-H1

Addition

% Accepted

Taiwan

Japan

China
mainland

United States

South Korea

4.415

4.345

4.968

4.819

9.383

477

327

1.018

154

300

278

744

131

1.345

1.142

1.822

465

361

792

1.341

199

930

2.359

111

353

98%

79%

81%

71%

69%

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 12 de 37

---

Security Status Report 2025 H1

Spain

593

197

640

224

1.233

34%

Taiwan again surpasses the United States in requests for fraud information during the second half of 2023 and first half of 2024. Spain occupies a prominent position, also, as in the previous case, with a very low acceptance rate.

### Account-based requests

Requests are made from governments to Apple related to accounts that may have been used in violation of the law and Apple's terms of use. These are iCloud or iTunes accounts and their name, address and even content in the cloud (backup, photos, contacts…).

Country

Requests 2023-
H2

Requests 2024-
H1

Addition

% Accepted
23H2

% Accepted
24H1

United States

10.827

12.812

23.639

Germany

Brazil

United Kingdom

Japan

Spain

1.925

3.327

1.414

259

101

2.655

3.664

2.550

841

156

90%

63%

62%

81%

55%

34%

90%

65%

71%

82%

77%

36%

The United States again leads by a comfortable margin in account information requests sent to Apple during late 2023 and early 2024.

### Requests Related to Account Preservation

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 13 de 37

---

Security Status Report 2025 H1

Under the context of the U.S. Electronic Communications Privacy Act (ECPA), Apple may be requested to “freeze” an account's data and hold it for 90 to 180 days. This is a preliminary step to requesting access to the account, pending legal permission to request data and to prevent the account from being deleted by the respondent.

Country

Requests 2023-H2

Preserved 2023-H2

Requests 2024-H1

Preserved 2024-H1

United States

Brazil

United Kingdom

Germany

France

Spain

6.610

242

47

53

2

1

16.682

466

54

61

6

1

8.170

264

64

52

41

0

20.513

407

99

50

85

0

The United States is by far the country with the most requests, followed by Brazil. In this respect, Spain hardly ever makes this type of request.

### Emergency requests

Also under the U.S. Electronic Communications Privacy Act (ECPA), it is possible to request Apple to provide private account data if in emergency situations it is believed that this could avert a danger of death or serious harm to individuals.

Country

Requests
2023-H2

Data Prov.
2023-H2

Requests
2024-H1

Data Prov.
2024-H1

Add. Data Prov.

United Kingdom

United States

Japan

Canada

Germany

Spain

655

636

259

147

99

5

597

451

215

125

73

3

726

793

288

169

99

1

658

601

239

141

74

1

1.255

1.052

454

266

147

4

 2025 © Telefónica Cybersecurity & Cloud Tech, S.L.U. All Rights Reserved.

Page 14 de 37

---

Security Status Report 2025 H1

The United Kingdom continues to be the country with the highest number of such requests to Apple, with most of them being fulfilled.

### Requests related to the removal of apps from the market

This data is no longer provided in Apple's report. We will update the following with more information and new developments in Apple's transparency report.

To clarify: In this exercise we have graphed the tables published by Apple itself. It is important to specify that requests are made in batches that may include more than one account or device. Apple, for example, counts the number of requests for device information, and in turn each request can contain an undetermined number of devices in them. Same with account requests and the number of accounts in each request. When Apple talks about the percentage of fulfilled requests, it is talking about requests, but not about specific accounts. For example: Apple receives 10 requests, with 100 devices among all the requests and then says it has satisfied 90% of the requests, we don