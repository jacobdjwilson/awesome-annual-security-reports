2022 ThreatLabz
State of Ransomware
Report 2022 Zscaler, Inc. All rights reserved.ContentsIntroductionKey findingsThe evolution of ransomwareRansomware attack sequence20212022 ransomware attack statisticsIndustry verticals affected by ransomwareTop ransomware families2022\-23 predictionsPrevention guidanceKey ransomware trendsSupply chain attacksLog4j ransomwareRansomware\-as\-a\-serviceGeopolitical attacksLaw enforcement takedownsRansomware rebrandingMajor vulnerabilities used in ransomware attacksTop 11 prevalent ransomware familiesContiLockBitPYSAMespinozaREvilSodinokibiAvaddonClopGriefHiveBlackByteAvosLockerBlackCatALPHVAbout ThreatLabzAbout Zscaler356788101214161617181819202123232528303336384043454850512 2022 Zscaler, Inc. All rights reserved.ThreatLabz ReportIntroductionIf it feels like ransomware is always in the news, 
it isnt just media bias: the Zscaler ThreatLabz 
research team has found that ransomware 
attacks increased by yet another 80% between 
February 2021 and March 2022 compared to the 
previous year, setting new records for both the 
volume of attacks and the cost of damages.3 2022 Zscaler, Inc. All rights reserved.ThreatLabz ReportRansomware is more and more attractive to attackers, who are able to wage increasingly profitablecampaigns based on three major trends:Supply chain
attacks
that exploit trusted vendorRansomware as 
a service
that uses affiliate networks toMultiple\-extortion 
attacks
that utilize data theft, distributedrelationships to breach organizationsdistribute ransomware on a widedenial of service (DDoS) attacks,and multiply the damage of attacksscale, allowing hackers who arecustomer communications, andby enabling threat actors to hitexperts in breaching networks tomore as layered extortion tactics tomultiple (sometimes hundreds orshare profits with the most advancedincrease ransom payouts.thousands) of victims at theransomware groups.same time.These tactics add up to be very damaging.ThreatLabz analyzes data from more thanIndustry experts predict that ransomware will be200 billion daily transactions and 150 millionthe top tactic used in third\-party breaches anddaily blocked attacks across the Zscaler Zerosupply chain attacks in 2022, and that the globalTrust Exchange along with Zscaler ThreatLabzcost of ransomware damages will grow to $42threat intelligence to track prevalent threatbillion by 2024\.These trends have pushed ransomware evenfurther up the list of cybersecurity priorities fororganizations across industries. Aimpoints TheCISOs Report, 2022 found that ransomware isthe single highest threat that CISOs around theworld are most concerned about.How can you identify and defend against thelatest ransomware variants? This reportshould help.families, identify emerging trends, and improveprotections for Zscaler customers. In this report,ThreatLabz looked at ransomware data fromFebruary 1, 2021, through March 31, 2022, toidentify the most prolific ransomware familiesand their tactics. We will share our findings,predictions, and best practices guidance to helpinform your ransomware defense strategies.4 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportKey findingsRansomware attacks increased by 80% year over year, accounting for all 
ransomware payloads observed in the Zscaler cloud.Double extortion ransomware increased by 117%, indicating that more and 
more attacks include data theft in their strategies. Some industries saw particularly high growth of doubleextortion attacks, including healthcare (643%), food service (460%), mining (229%), education (225%),media (200%), and manufacturing (190%).Manufacturing was the most targeted industry for the second 
straight year, making up almost 20% of double extortion ransomware attacks.Supply chain ransomware attacks are on the rise, as are supply chain attacks 
in general. Exploiting trusted suppliers lets attackers breach a large number of organizations all at once,including organizations that otherwise have strong protections against external attacks. Supply chainransomware attacks of the past year include damaging campaigns against Kaseya and Quanta as well as anumber of attacks exploiting the Log4j vulnerability.Ransomware as a service is driving more attacks. Ransomware groups continue 
to recruit affiliates through underground criminal forums. These affiliates compromise large organizationsand deploy the groups ransomware, typically in exchange for about 80% of the ransom paymentsreceived from victims. Most (8 out of 11\) of the top ransomware families of the past year have commonlyproliferated via ransomware\-as\-a\-service models.Law enforcement is cracking down. A number of last years top ransomware 
familiesparticularly those targeting critical servicesattracted attention from law enforcementagencies around the world. REvil (responsible for famous attacks on Kaseya and JSB), DarkSide(responsible for the attack on Colonial Pipeline), and Egregor (a rebranding of Maze, last years topransomware family) all had assets seized by law enforcement in 2021\.Ransomware families arent going awaytheyre just rebranding. 
Feeling increased heat from law enforcement, many ransomware groups have disbanded and reformedunder new banners, where they use the same (or very similar) tactics. DarkSide rebranded as BlackMatter,DoppelPaymer rebranded as Grief, and Avaddon rebranded as Haron and Midas. Evil Corp, sanctioned bythe US government, has consistently rebranded their ransomware operations.The Russia\-Ukraine conflict has the world on high alert. There have 
been several attacks associated with the Russia\-Ukraine conflict, including multiple wipers includingHermeticWiper and PartyTicket ransomware. So far, most of this activity has targeted Ukraine. However,government agencies have warned organizations to be prepared for more widespread attacks as theconflict persists.Zero trust remains the best defense. To minimize the chance of a breach and 
the damage a successful attack can cause, your organization must use defense\-in\-depth strategiesthat include reducing your attack surface, enforcing least privileged access control, and continuouslymonitoring and inspecting data across your environment.5 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportThe 
evolution of 
ransomwareRansomware is a type ofattackers added anothermalware cybercriminals use toattack layer with DDoSdisrupt a victims organization.tactics that bombard theRansomware encrypts anvictims website or network,organizations important filescreating even more businessinto an unreadable formdisruption, thus pressuringand demands a ransomthe victim to negotiate.payment to decrypt them.Ransom demands are oftenproportional to the numberof systems infected and thevalue of the encrypted data:the higher the stakes, thehigher the payment.In 2021 and going into2022, the most damagingransomware trend involvessupply chain attacks, inwhich a breach of a vendor(typically a software or othertechnology provider) opensIn late 2019, attackers evolvedthe door for second\-stagetheir ransomware tacticsattacks on organizations thatto include data exfiltration,rely on their products. Supplycommonly referred tochain attacks are estimated toas a double extortionhave jumped 51% in the backransomware attack. In thesehalf of 2021\. Threat actorsattacks, if victims choose nothave made headlines throughto pay the ransom to decryptexploits of popular softwarethe data and, instead, attemptproducts such as SolarWinds,to restore the data from aKaseya, and Log4j, and webackup, the attackers threatenexpect this trend to escalate into leak the stolen data. In latethe coming years.2020, some ransomware6 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportRansomware attack sequenceTodays ransomware attacks typically have the following stages:12345Initial compromise: Attackers use a variety of intrusion vectors to gain access to systems, includingphishing emails, exploiting vulnerabilities in remote administrator or virtual private network(VPN) tools, and using brute force or stolen credentials to access Remote desktop protocol (RDP)connections. Supply chain attacks are yet another method to infiltrate an organization.Lateral movement: After gaining initial access, threat actors proceed to gather victimsinfrastructure information and move laterally across network systems, escalating privileges andestablishing persistence mechanisms as needed, cataloging key data to steal or encrypt, anddepositing ransomware payloads for later execution.Data exfiltration: In the case of a double extortion attack, attackers will next steal sensitive data touse as a secondary extortion tactic so they can demand higher ransom payments. This reduces thevictims leverage: even if they can recover the encrypted data from backups, they still must face thethreat of the cybercriminals leaking the stolen data.Ransomware execution: Next, attackers deploy and execute the ransomware, encrypting targetedfiles on systems connected to the network. Ransomware typically terminates processes relatedto security software and databases to maximize the number of files it can encrypt. Shadow copybackups are also usually deleted from the system to hinder file recovery. Some ransomware familieswill also reboot the compromised system in Windows Safe Mode to bypass security endpointsoftware prior to file encryption. After file encryption, victims are provided with a ransom note thatprovides instructions for paying the ransom and decrypting their files.DDoS: If the victim does not negotiate, some hacking groups will wage a DDoS attack against thevictims network or website, disrupting their business operations to gain additional leverage.Figure 1 displays the typical attack chain of a multi\-extortion ransomware attack.Initial access
 Spam email
 Brute force or stolen 
credentials to RDP
 Exploiting a 
vulnerabilityNetwork 
reconnaissance \& 
lateral movementData
exfiltrationRansomware
deployment,
execution, \&
data encryptionDDOS attack on
victim website or
network until
negotiationFigure 1: Infection chain of a ransomware attackExtortion
tactic \#1Extortion
tactic \#2Extortion
tactic \#3If ransom is not paid:Publish data to leak site
 Credentials
 Sensitive data 
 Other information7 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware Report2021\-2022 ransomware 
attack statisticsThe high volume of transaction data on the Zero TrustExchange provides a unique look into the tactics andvictims of cybercriminals. From February 2021 throughMarch 2022, ThreatLabz observed an 80% increase inransomware payloads compared to the previous year.Further, we saw a 117% increase in double extortionransomware victims based on data published onthreat actors data leak sites.Industry verticals affected by ransomwareManufacturing was already the most targeted vertical in 2020, making up 12\.7% of double extortionransomware attacks between November 2019 and January 2021\. This year, the percentage of attacks onmanufacturing organizations rose even further to 19\.5%, followed by services (9\.7%), construction (8\.1%),retail and wholesale (7\.5%), and high tech (6\.7%).Ransomware infections by industry169141130117111339Manufacturing
Services
Construction
Retail \& Wholesale
High Tech
Other
Financial Services
Transportation Services
Education
Food, Beverage \& Tobacco
Healthcare
Real Estate
Government
Basic Materials and Chemicals
Insurance
Oil \& Gas
Restaurants, Bars \& Food Services
Mining
Nonprofit Institutions
Telecommunications
Consumer Services
Advertising
Media
Aerospace \& Defense
Utilities
Arts, Entertainment \& Recreation
Energy
Household \& Personal Products8581
786852
52
4836
33
31
2823
22
2218
15
15106
3
3
2Figure 2: Ransomware infections by industry01002003004008 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportGrowth in double extortion ransomware attacks varied widely by industry. In last years report, we noteda particularly low number of attacks against healthcare organizations, driven by increased scrutiny fromlaw enforcement as well as pledges from several prevalent ransomware families that they would not targethealthcare during the COVID\-19 pandemic.This years data tells a different story. Double extortion ransomware attacks against healthcare grew by643% in 2021, though it started with a very low baseline of attacks in 2020\. Several other verticals withhigher starting points also saw triple\-digit growth in attacks, including education (225%), manufacturing(190%), construction (161%), financial services (130%), and services (109%).Percent change in double extortion attacks: 2021 vs 2020460%643%Healthcare
Restaurants, Bars \& Food Services
Mining
Education
Media
Manufacturing
Basic Materials and Chemicals
Construction
Financial Services
Services
Food, Beverage \& Tobacco
Insurance
Real Estate
Retail \& Wholesale
Telecommunications
Oil \& Gas
High Tech
Government
Other
Nonprofit Organizations
Advertising
Transportation
Consumer Services
Utilities
Aerospace \& Defense
Energy
Arts, Entertainment \& Recreation
Household \& Personal Products229%
225%200%190%177%161%130%109%
100%
94%
93%71%
69%
63%
58%37%
28%16%
7%
0%
\-5%
\-25%
\-33%
\-50%
\-70%
\-83%Figure 3: Percentage change in double extortion attacks by industry9 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportTop ransomware familiesConti and LockBit were the most prevalent double extortion ransomware families in 2021, joined by a rangeof new entrants that emerged over the course of the year.Figure 4 shows when each of the most active ransomware families of the past several years first emergedand began publishing data on leak sites or hacking forums.SekhmetNEFILIMAKOPYSAMespinozaNetwalkerMountLockerPay2KeyClopLockBitDarkSideRansomExxREvilSodinokibiRagnarLockerContiEgregorMazeDopplePaymerAvaddonRanzyCUBANOV
2019DEC
2019JAN
2020FEB
2020MAR
2020APR
2020MAY
2020JUNE
2020JULY
2020AUG
2020SEPT
2020OCT
2020NOV
2020DEC
2020HiveVice SocietyLVBlackCatALPHVLorenzGriefBlackByteAvosLockerGriefSpookJAN
2021FEB
2021MAR
2021APR
2021MAY
2021JUNE
2021JULY
2021AUG
2021SEPT
2021OCT
2021NOV
2021Figure 4: Timeline of ransomware families publishing on data leak sites or hacking forums10 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportMany of the active ransomware families inservices organizations from financial services,20212022 are ransomware\-as\-a\-serviceIT, energy, and government sectors, including(RaaS) models, increasing their distributionIrelands public healthcare services and thethrough affiliate networks. In 2021, we also sawgovernment of Costa Rica. In May 2022, the USthe rebranding of several popular ransomwareDepartment of State offered a $10 million rewardfamilies, such as DoppelPaymer rebranding asfor information on leaders of the group.Grief, DarkSide rebranding as BlackMatter, andAvaddon rebranding as Haron followed by Midas(the latter two using the Thanos ransomwarebuilder).LockBit, formerly known as ABCD ransomware,tends to attack small\- to medium\-sizebusinesses, thus mostly avoiding the headlines,with the exception of their attack on AccentureConti has been the most active ransomwarein August 2021\. LockBit is a widely used RaaSgroup of the last two years and the costliest of allthat is attractive to attackers due to its speed andtime: The FBI estimates that as of January 2022,performance.there were more than 1,000 victims of attacksassociated with Conti ransomware, with totalvictim payouts exceeding US$150 million (notincluding related damages or remediation costs).Conti victims have included a range of criticalFigure 5 shows the ransomware families thataffected the highest number of organizations withdouble\-extortion attacks between February 2021and March 2022, based on information from dataleak sites.Ransomware attacks by family6004002000i
t
n
o
Ct
i
B
k
c
o
La
s
y
Piib
k
o
n
d
o
S
il
ip
o
Clf
e
i
rGe
v
Hin
o
d
d
a
v
AV
Le
t
y
B
k
c
a
Blr
e
k
c
o
L
s
o
v
Av
E
RFigure 5: Ransomware attacks by family, February 2021\-March 2022lt
a
C
k
c
a
BV
a
h
p
AlA
BU
Ck
o
o
p
Siy
t
e
c
o
Se
c
Vis
a
d
Mix
x
E
m
o
s
n
a
R11 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware Report 
202223 predictionsRansomware as a service will continue to increase
RaaS has proven to be valuable for all parties involved. New ransomware developers and affiliates will increasetheir use of this model to wage rapidly changing attacks on vulnerable organizations.Changing ransomware models will lead to changing targets
With ransomware builders and organizational intel available for sale on the dark web, attackers have theadvantage of filtering through company profiles to narrow down the ideal targets for specific vulnerabilities,profits, and types of ransomware. As a result, you should expect to see a shift toward easier targets, includingsmall to medium enterprises with fewer security controls and organizations with internet\-visible applicationsthat have known vulnerabilities along with previously phished credentials.Dwell time will continue to decrease
Now that threat actors have easy and cheap access to company profiles and compromised credentials for saleon the dark web, the days of attackers sitting on targets for months or even years and then taking extra time tolook around before launching an attack are coming to an end. With more public reports of ransomware attackersreducing dwell times to just days, the criminals are savvy to increased detection techniques, realizing time is ofthe essence for a successful attack. As a result, security teams need to close the gap and speed up detectionto days, hours, or just minutesto prevent worst\-case scenario breaches in 2022 and beyond.Supply chain attacks will increase as adversaries
compromise partner and supplier ecosystems
The worlds top organizations often have the best security in placebut the same may not be true for theirsuppliers and partners, with third\-party access to supporting networks, systems, and information. We saw thisin the recent compromise of Okta by the rogue hacker group Lapsus$, and in REvil threatening Apple via QuantaComputer, a top manufacturer of Apple products. These groups and many others used supply chain attacks toaccess sensitive upstream information using supplier access without ever having to breach the hardened securitymeasures of their final targets.Ransomware may be used as, or in conjunction with,
a wiper to destroy data
In early 2022, publicized attacks on Ukraine featured multiple types of wiper attacks, including HermeticWiperalongside a decoy ransomware known as PartyTicket. This is not the first time ransomware has been used ingeopolitical attacks, with NotPetya and Bad Rabbit being deployed in 2017 to attack Ukrainian organizations.Geopolitical tensions bring with them the threat of masked ransomware, wipers, and other tactics that affordthreat actors an elevated degree of anonymity and plausible deniability.12 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportOld (and new) vulnerabilities will continue to cause damage
There have been some major vulnerabilities discovered in the past year (e.g Log4j, PrintNightmare, ProxyShellProxyLogon) that organizations will be dealing with for years to come. Attackers will continue to search for andexploit unpatched and out\-of\-date software and servers to bypass security controls.Ransomware families will continue rebranding
We saw this cycle throughout 2021: a ransomware group pulls off a major attack, earns attention and sanctionsfrom law enforcement, and then disappears and reforms later under a new name. With ransomware very muchon the radar of law enforcement, this cycle will continue throughout 2022 and beyond.Organizations will need to beef up security beyond endpoint protection 
Ransomware groups will increase use of tactics to bypass antivirus and other endpoint security controls.Organizations will have an even greater need for defense\-in\-depth rather than relying solely on endpointsecurity to prevent and detect intrusions.Ransomware developers will add more malware obfuscation
Malware authors implement malware obfuscation techniques to hinder reverse engineering and bypass staticsignature detection. The malware obfuscation complexity will continue to increase with advanced techniques,including control flow flattening, polymorphic string obfuscation, and the use of virtual machine\-based packers.Leaked ransomware source code will lead to forks
There have been several source code leaks for ransomware in the past year, including two versions of Conti andBabuk. Zscaler ThreatLabz has already observed both ransomware families source code being forked by thirdparties and used in attacks. The release of source code will undoubtedly lead to abuse by other criminal groupsthat do not have the expertise to design and build their own ransomware from scratch.13 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportPrevention guidanceWhether a simple ransomware attack, a double\- or triple\-extortion attack, a self\-contained threat family, or a RaaSattack executed by an affiliate network, the defense strategyis the same: employ the principles of zero trust to limitvulnerabilities, prevent and detect attacks, and limit theblast radius of successful breaches. Here are some bestpractices recommendations to safeguard yourorganization against ransomware.1Get your applications off
of the internet.
Ransomware actors start their attacks by performing4Implement a zero trust network 
access (ZTNA) architecture. 
Implement granular user\-to\-application andreconnaissance on your environment, lookingapplication\-to\-application segmentation, brokeringfor vulnerabilities to exploit, and calibrating theiraccess using dynamic least\-privileged accessapproach. The more applications you have publishedcontrols to eliminate lateral movement. This allowsto the internet, the easier you are to attack. Use ayou to minimize the data that can be encrypted orzero trust architecture to secure internal applications,stolen, reducing the blast radius of an attack.making them invisible to attackers.2Enforce a consistent security 
policy to prevent initial 
compromise. 
With a distributed workforce, it is important toimplement a security service edge (SSE) architecturethat can enforce consistent security policy no matterwhere your users are working (in office or remotely).3Use sandboxing to detect 
unknown payloads. 
Signature\-based detection is not enough in theface of rapidly changing ransomware variants andpayloads. Protect against unknown and evasiveattacks with an inline, AI\-powered sandbox thatanalyzes the behavior rather than the packagingof a file.56Deploy inline data loss prevention.
Prevent exfiltration of sensitive information withtrust\-based data loss prevention tools and policies tothwart double extortion techniques.Keep software and training
up to date.
Apply software security patches and conductregular security awareness employee training toreduce vulnerabilities that can be exploited bycybercriminals.7Have a response plan.
Prepare for the worst with cyber insurance, a databackup plan, and a response plan as part of youroverall business continuity and disaster recoveryprogram.14 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportTo maximize your chances of defending against ransomware, you must embrace layered defenses thatcan disrupt the attack at each stagefrom reconnaissance to initial compromise, lateral movement, datatheft, and ransomware execution.Stopping ransomware with zero trustMinimize 
attack surfacePrevent initial 
compromiseEliminate 
lateral movementStop data loss 
\& malware deliveryGain initial entry
Vulnerable 
VPNEstablish 
foothold 
with 
phishing
GmailDeliver 
malware 
dropper
G DriveInstall
malware
G DriveSteal credentials 
\& compromise 
additional systems
Domain controllerSteal dataInstall 
ransomware 
\& demand 
paymentMake apps invisible
Inspect all trafficSafely render email links \| 
Cloud browser isolationIn\-line inspection of all traffic \| SWG \| 
IPS \| SandboxCloud DLP \| Cloud CASB \| 
Cloud firewall \| 
Workload protectionUser\-to\-app 
segmentationApp\-to\-app 
segmentationDeception15 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportKey ransomware trendsSupply chain attacksWhat is a Supply Chain Attack?Supply chain attackssometimes called value chain or third\-party attacksare attacks against thesuppliers of an organization as a means for gaining access. Most large organizations have sophisticatedsecurity controls that make infiltration difficult, so attackers have found a way in through the suppliers tothese organizations.Supply chain attacks exploit the trust between legitimate organizations that exists in normal businessoperations. Attackers plant a backdoor into a product that they know their target uses, which allows theattacker to infiltrate the targets network without detectiontypically gaining entry via automated patchesor software updates, called trojanized updates. Once inside, the attackers can spy, steal data, implantother malware, and disrupt operations.Such attacks involve a high degree of planning and sophistication, and they can have a devastating impacton organizations within the blast radius of the original compromise.Attacker breaches
software product and
installs malicious codeMalicious code is
distributed to 
customers during
software updateFigure 6: Supply chain attack16 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportKaseya supply chain ransomwarelibrary. This vulnerability allows an attacker toOn July 2, 2021, IT management software firmdownload and execute a malicious payload byKaseya disclosed a security incident impactingsubmitting a specially crafted request to thetheir on\-premises version of Kaseya VSAvulnerable system. The attacker can then controlsoftware, a platform that allows managed servicelog messages or log message parameters toproviders (MSPs) to perform patch management,execute arbitrary code loaded from LDAP serversbackups, and client monitoring for theirwhen message lookup substitution is enabled.customers. Roughly 70 MSPs are believed to haveLog4j is incorporated into many popular websites,been breached in this attack, with downstreamapplications, and frameworks, making the impactimpacts to as many as 1,500 small and mediumwidespread. Several ransomware attacks havebusinesses.emerged exploiting this vulnerability:The threat actor behind this attack identified andNightSky ransomwareexploited a zero day vulnerability in the KaseyaOn January 4, 2021, attackers exploitedVSA server that allowed them to send a maliciousthe Log4j vulnerability in an internet\-facingscript to all clients that were managed by thatsystem running VMware Horizon, droppingserver. The script was used to deliver REvilthe NightSky ransomware.Sodinokibi ransomware that encrypted files onthe affected systems.KhonsariMultiple attacks have been observed usingQuanta computer supply chainLog4j exploits on Windows systems to deployIn April 2021, REvil attacked Quanta Computer,Khonsari ransomware.the worlds largest laptop manufacturer and atop manufacturer of Apple products. Quantarefused to pay a $50 million ransom demand,leading to REvil targeting Apple and other Quantacustomers for the ransom instead. REvil leaked21 screenshots of MacBook schematics andthreatened to publish more data from Apple andother companies until Apple or Quanta paid theransom demand.Log4j ransomwareIn December 2021, the Apache SoftwareFoundation released a security advisory regardinga remote code execution vulnerability (CVE\-2021\-44228\) in their popular Log4j loggingContiThe Conti group has also leveraged the Log4jvulnerability to execute ransomware attacks.AdvIntel discovered the group scanning andtargeting vulnerable Log4j VMware vCenterversions, moving laterally from existing CobaltStrike sessions to US and European victimnetworks.TellYouThePassAttackers have exploited the Log4jvulnerability to deploy and execute theTellYouThePass ransomware in Windows andLinux systems.17 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportRansomware as a serviceRaaS has increased both the volume and damageThe dark web has become a very popular placefor threat groups to sell their wares to would\-becriminals. Weve detailed the impact of thesemarketplaces for other attack types, such asof attacks:Increase in volume of ransomware attacks:More affiliates begin executing ransomware asit now requires less time and skill to develop.the growth of phishing as a service in the 2022Increase in ransom amounts due to doubleThreatLabz State of Phishing report.RaaS has become incredibly popular, and it nowdrives the bulk of modern ransomware attacks. Infact, 8 of the top 11 ransomware families from thepast year utilize RaaS ecosystems.extortion: RaaS includes a double extortioncomponent in which threat actors steal data andthreaten to publish it on a data leak site if theransom is not paid. This increases the ransomamount and the rate of successful payment.The RaaS model requires two parties: operatorsGeopolitical attacksand affiliates. Operators are the threat groupsthat develop the ransomware. Affiliates targettheir victims, execute the ransomware, and setdemands.Operators recruit affiliates and provide them withthe ransomware and tools required to execute it,access to a data leak site, negotiation assistance,and other support, in exchange for approximately7080% of the profit from the attacks.Security leaders around the world are on guardfor an increase in ransomware attacks as a resultof the Russia\-Ukraine conflict.In March 2022, US President Joe Biden issued astatement warning of the potential for maliciouscyber conduct against the United States as aresponse to economic sanctions against Russia.His statement urged immediate action to hardencyber defenses among both public and privateThis model is beneficial to both parties. Affiliatessector organizations.get everything that they need to execute highlyeffective ransomware attacks without needingto develop any of it themselves. This is attractiveboth to skilled criminals who save developmenttime and resources as well as low\-skilledcriminals who otherwise would not be able toexecute such an attack. Ransomware operatorscan dramatically increase the scale of theiroperations and, consequently, their profits.8 of the top 11 
ransomware 
families of 2021 
utilize RaaS 
ecosystems.18 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportAs of the writing of this report, there have beenmajor attacks against Kaseya and JSB. Followingseveral ransomware attacks against Ukraine andthe Kaseya attack, the FBI planned a takedownor associated with this conflict:of the REvil servers. However, they never got1PartyTicket ransomware: This Go\-basedransomware has been used in conjunctionwith the HermeticWiper malware to targetorganizations in Ukraine. PartyTicket isunsophisticated and contains flawed encryptionthat can be decrypted and reversed, leading usto suspect that it was developed as a decoy todistract from HermeticWiper.their chance: shortly after this critical attack inJuly 2021, REvil shut down its operations and thehackers disappeared. This turned out to be brief,as Kaseyas operations restarted in September2021\.In January 2022, the Russian governmentapparently dismantled the REvil hacking group,arresting members at the request of the United2 Conti ransomware: The Cybersecurity andStates. The Russian Federal Security ServiceInfrastructure Security Agency (CISA), the(FSB) searched 25 addresses, detaining 14 groupFederal Bureau of Investigation (FBI), themembers of REvil as well as seizing 426 millionNational Security Agency (NSA), and therubles, US$600,000, 500,000 euros, 20United States Secret Service have rereleased anluxury cars, and computer equipment. However,advisory on Conti, a Russia\-linked ransomwareREvil reemerged in April 2022, attackinggroup. Their advisory warns that Conti cyberorganizations with an updated ransomwarethreat actors remain active and reportedversion.Conti ransomware attacks against U.S. andinternational organizations have risen to morethan 1,000\. In late February, Conti posted twostatements on their leak site, pledging supportto the Russian government in response toWestern warmongering and American threatsto use cyber warfare against the citizens ofRussian Federation.Law enforcement takedownsLaw enforcement agencies around the worldare paying increased attention to ransomwarefamilies, particularly those causing widespreaddamages. There have been several successfultakedowns of high\-impact ransomware familiesthrough 2021 and early 2022\.REvil takedownREvil is one of the most infamous ransomwarefamilies of the last two years, in the news afterDarkSide takedownOn May 6, 2021, the DarkSide ransomwaregroup executed a high\-profile ransomwareattack on Colonial Pipeline, the largest oil pipelinein the United States. Federal agencies tookaction, and within two weeks of the attack, athreat actor known as UNKN announced thatDarkSide had been shut down, as they had lostaccess to servers and their cryptocurrency hadbeen transferred to an unknown account. TheDepartment of Justice announced that they hadseized 63\.7 bitcoins valued around US$2\.3 million.Egregor takedownThe Egregor ransomware groupformerlyknown as Mazewas taken down by cooperativelaw enforcement efforts on February 9, 2021\.Agencies from Ukraine, France, and the UnitedStates shut down the Egregor leak website,arrested group members, and seized computers19 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware Reportthat were linked to ransomware attacks. Egregorbitcoin (BTC). This switch in cryptocurrencies mayhad extorted approximately US$80 million frombe in response to the FBI recovering part of themore than 150 victim companies.Colonial Pipeline ransom payment.Ransomware rebrandingRansomware operators have been rebrandingtheir ransomware at a high rate in the pastDarkside rebranded as BlackMatterAfter DarkSides shutdown in May 2021, a newransomware family named BlackMatter emergedin late July. The encryption routine used inyear. Rebranding is commonly due to unwantedthe ransomware and text in the data leak siteattention from law enforcement and the media,indicated that BlackMatter was a rebranding ofas well as due to sanctions that limit the groupsDarkSide.abilities to collect ransom payments.DoppelPaymer rebranded as GriefBlackMatter ceased its operations in November2021\. The group posted a shut down operationIn early May 2021, DoppelPaymer ransomwaremessage on its RaaS portal that said, Due toactivity dropped significantly. Although theDoppelPaymer leak site still remains online,there has not been a new victim post sincecertain unsolvable circumstances associated withpressure from the authorities (part of the team isno longer available, after the latest news) theMay 6, 2021\. In addition, no victim posts haveproject is closed.been updated since the end of June. Thislull is likely a reaction to the Colonial Pipelineransomware attack that occurred on May 7,2021\. However, the apparent break is due to thethreat group behind DoppelPaymer rebrandingthe ransomware under the name Grief. Bothransomware variants share malware code, and theleak sites are very similar. The Grief ransom portalhas some differences from the DoppelPaymerportal. In particular, the ransom demand paymentmethod is made in Monero (XMR) instead ofRansomware 
groups rebrand to 
bypass sanctions 
and reduce 
attention from 
law enforcement.Thanos based ransomware rebrandingAdvertised on the dark web as RaaS, Thanosransomware was first identified in February2020\. The Thanos builder was leaked, and in thefollowing two years, a series of new variants havebeen developed. The Prometheus ransomwarevariant emerged in February 2021\. In September,Prometheus was rebranded as Spook. Both havesimilar ransom notes and data leak sites andcontain Thanoss signature Key Identifier.In July 2021, another Thanos derivedransomware called Haron was discovered.Haron ransomware has striking similarities withAvaddon ransomware. Haron and Avaddon sharecommonalities in their ransom notes, negotiationsites, and data leak sites. In October 2021,another variant called Midas was discovered thatis a rebranded version of Haron ransomware.20 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportEvil Corp rebrandingThe Evil Corp gang, also known as Indrik Spider,is known for a range of malicious activity. Theycreated banking trojans such as Dridex, the latterof which was used to distribute their BitPaymerransomware.The Office of Foreign Assets Control (OFAC)of the US Treasury Department sanctionedMajor vulnerabilities used in 
ransomware attacksProxyLogon vulnerabilitiesBlackKingdom and DearCry ransomwares havecombined four different ProxyLogon vulnerabilityexploits to gain entry and encrypt their victimsnetworks. This tactic has been used to accessthe Microsoft Exchange servers, steal email,members of Evil Corp for damages caused byand deploy other backdoors. The ProxyLogontheir Dridex malware, claiming that they inflictedvulnerabilities include CVE\-2021\-26855more than $100 million in damages across(server\-side request forgery \[SSRF] vulnerabilitybanks and financial institutions in more than 40in Exchange), CVE\-2021\-26857 (insecurecountries. Following these sanctions, ransomwaredeserialization vulnerability in the Unifiednegotiation firms refused to facilitate ransomMessaging service), CVE\-2021\-26858 (post\-payments for Evil Corp for fear of fines or legalauthentication arbitrary file write vulnerabilityaction from the US Treasury Department. Toin Exchange), and CVE\-2021\-27065 (post\-bypass sanctions, Evil Corp discovered a simpleauthentication arbitrary file write vulnerabilityloophole through rebranding their ransomware.in Exchange). Microsoft patched theseEvil Corp distributed WastedLocker ransomwarevulnerabilities in March 2021\.in June 2020, Hades ransomware in DecemberA typical attack chain that allows an attacker to2020, and Phoenix ransomware in March 2021\.execute remote code over exposed port 443:In May 2021, they continued to rebrand theirAttackers use the CVE\-2021\-26855 vulnerabilityransomware as PayloadBin, impersonatingto bypass Microsoft Exchange authenticationanother threat actor who was not subject to theand impersonate a user. The attacker sendssame sanctions.Rook rebrandingRook ransomware was spotted in November2021, based on leaked source code from Babukransomware. In December 2021, a variant of Rookwas rebranded as Night Sky, which has beenused by the China\-based threat actor groupDEV\-0401 to target corporate networks indouble extortion ransomware attacks leveraginga modified POST request for any file in thedirectory that is readable without authentication,where the file in the directory is not required. Theattacker authenticates into the Exchange controlpanel (ECP) and overwrites any file in the targetedsystem using CVE\-2021\-26858 or CVE\-2021\-27065 vulnerabilities. After these exploits, anattacker can execute remote code using web shellon the Exchange server.the Log4Shell vulnerability. In January 2022, bothProxyShell exchange vulnerabilityRook and Night Sky shut down, and PandoraConti ransomware exploits Microsoft Exchangeransomware emerged. Based on code similarities,Servers vulnerability to enter into the victimsPandora is also a rebranded version of Rook.21 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware Reportnetwork. ProxyShell exchange vulnerabilitiesSonicWall SMA 100are a combination of CVE\-2021\-34473In January 2021, SonicWall confirmed a SQL(Microsoft Exchange Server remote codeinjection vulnerability in their Secure Mobileexecution vulnerability), CVE\-2021\-34523Access SMA 100 Series product that allowed(Microsoft Exchange Server elevation ofattackers to access login credentials and sessionsprivilege vulnerability), and CVE\-2021\-31207and breach vulnerable appliances by using(Microsoft Exchange Server security featureunauthenticated, specially crafted queries. It wasbypass vulnerability) vulnerabilities. Microsoftpatched by SonicWall in February 2021\.has patched these vulnerabilities between Apriland May 2021, but Conti continues to targetunpatched servers to execute remote code.The infection chain for this ransomware canbe seen in this report, in the breakdowns ofBlackByte, AvosLocker, and Hive ransomwaregangs. LockFile ransomware also targets thesevulnerabilities to deploy the ransomware.PrintNightmareThis was discovered after the UNC2447 threatgroup used this flaw to attack a targeted networkand deploy FIVEHANDS double extortionransomware into victims systems. The threatactor used the zero\-day vulnerability to gainentry and drop the SOMBRAT backdoor alongwith additional tools to gain a foothold, performreconnaissance, and exfiltrate data, includingCobalt Strike beacons, Adfind, BloodHound,Ransomware actors exploit the PrintNightmareMimikatz, PC Hunter, and Rclone. At the endvulnerabilities to target Windows systems.of attack, UNC2447 dropped and executedPrintNightmare vulnerabilities are a combinationFIVEHANDS ransomware to encrypt the dataof CVE\-2021\-34527 and CVE\-2021\-34481,of the targeted system, and then attempted toremote code execution vulnerabilities in theextort money under threat of publishing the dataWindows print spooler service that improperlyon hacker forums.performs privileged file operations and allowsattackers to execute remote code with SYSTEMprivileges.QNAP NAS deviceA new variant of eCh0raix ransomware targetedQuality Network Appliance Provider (QNAP)The vulnerability exists in the point\-and\-network\-attached storage (NAS) devices andprint capability on Windows systems, andSynology NAS devices. In the attack chain, theallows nonprivileged users to update or installattacker exploited the vulnerability CVE\-2021\-remote printers. Microsoft released updates28799 in QNAP NAS devices. The improperfor PrintNightmare in July and August 2021authorization vulnerability has been reported inaddressing the vulnerabilities.QNAP NAS running HBS 3 (hybrid backup sync)In one attack, a ransomware group exploitedPrintNightmare vulnerabilities and droppedVice Society ransomware. In another campaign,attackers exploited PrintNightmare and droppedMagniber ransomware.devices and allows the attacker to log in to adevice remotely.22 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportTop 11 prevalent 
ransomware familiesWhat follows is an overview of 11 different ransomware families and their attack sequences. Theseransomware families claimed the most victims in 2021 and into 2022, and best represent the current stateof ransomware that your organization must defend against. For each family, well provide a bit of history,a summary of their tactics (including MITRE ATT\&CK mappings), and some statistics on their targetindustries.ContiConti ransomware was first spotted in February 2020\. Conti is sometimes classified as RaaS, but theiraffiliates are essentially employees, rather than affiliates who sign up, use a portal to manage the page, andreceive a cut of the profits. Conti and Ryuk share similar code, indicating that Conti is likely the successorof Ryuk ransomware. Conti has been the most prevalent ransomware in 2021\.Infection chain:Conti has used a range of initial access mechanisms across various campaigns:1It has been distributed through spam emails containing malicious attachments or links that furtherdownload TrickBot, IcedID, BazarLoader or Cobalt Strike to get a foothold into the system.2 Initial access is also done by exploiting known vulnerabilities such as Log4j, ProxyShell, or using weakRDP (Remote desktop protocol) credentials.After compromise, Conti uses Cobalt Strike, Mimikatz, and other post\-exploitation tools to stealcredentials and establish a foothold on the network. Conti threat actors are known to use Metasploit,Netscan, and other red team tools to obtain network and domain controller information. After acquiringthe necessary information, the threat actors may use AnyDesk, PsExec, or other remote utilities for lateralmovement. Conti threat actors exfiltrate data using Rclone or other tools, and finally deploy and executeConti ransomware to encrypt data as shown below in Figure 7\.Spam email campaignExploiting Log4j
vulnerabilitiesExploiting ProxyShell
vulnerabilitiesDeploy and execute
Conti ransomware and 
encrypt dataTrickBotBazarLoaderIceIDWebshellCobalt StrikeCobalt Strike, Mimikatz, and
other post exploitation tools
to steal credentials and get
foothold into the systemData exfiltration using
Rclone or other toolsAnyDesk, PsExec or
other remote utility used
for lateral movementMetasploit, Netscan, or other 
network discovery tool to
get network informationFigure 7: Anatomy of a Conti ransomware attack23 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportThe first version of Conti used RSA and AES algorithms in the encryption process. However, AES was laterreplaced with ChaCha encryption.In late January 2022, ThreatLabz identified an updated version of Conti ransomware as part of our globalransomware tracking efforts. This update was released prior to a massive leak of Conti source code andchat logs on February 27, 2022, which was published by a Ukrainian researcher after the invasion ofUkraine. The new version of Conti added new command line arguments that allow Conti to reboot thesystem in Windows Safe Mode with networking enabled, and then start encryption. By booting in SafeMode, Conti can maximize the number of files that are encrypted, because business applications such asdatabases are likely not running. Conti also updated the encrypted file extensions to include uppercase andlowercase characters and numbers. It also sets the victims desktop wallpaper after file encryption.Figure 8 displays the industry verticals targeted by double extortion attacks using Conti.11%9%8%7%6%24%Conti infections by industryManufacturing
Services
Construction
Retail \& Wholesale
High Tech
Other
Food, Beverage \& Tobacco
Transportation Services
Healthcare
Government
Real Estate
Education
Legal
Mining
Basic Materials and Chemicals
Insurance
Telecommunications
Restaurants, Bars \& Food Services
Nonprofit Institutions
Oil \& Gas
Utilities
Media
Advertising
Agriculture \& Forestry4%
4%3%3%2%
2%
2%
2%1%
1%
1%
1%1%
1%
1%
1%
1%
1%Figure 8: Conti infections by industryConti created its own data leak site in August 2020\. If a ransom demand is not paid by an organization,Conti will publish its stolen data.Figure 9: Conti data leak site24 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportConti: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionSpear
phishing linkCommand\- 
line interfaceBoot or logon 
autostart 
executionAccess token 
manipulationDeobfuscate
Decode files 
or informationExploitation 
for privilege 
escalationImpair
defensesProcess 
injectionSpear 
phishing 
attachmentExecution 
through 
module loadExploit 
public\-facing 
applicationValid accountsShared
modulesUser
executionSupply chain 
compromiseLockBitLateral 
MovementCollectionExfiltrationImpactLateral tool 
transferArchive
collected dataAutomated 
exfiltrationRemote 
servicesData from 
local systemExfiltration 
over web 
serviceData
encrypted for 
impactInhibit system 
recoverySystem
shutdown
rebootDefacementDiscoverySystem 
network 
configuration 
discoveryRemote
system 
discoveryFile and 
directory 
discoverySecurity 
software 
discoveryQuery registryLockBit ransomware first emerged in September 2019 as ABCD ransomware, named after its extension.abcd. A new version emerged at the start of 2020 that appends the extension .lockbit to encryptedfiles. In 2020, LockBit joined the Maze cartel and began publishing victims data on Mazes data leak site.In September 2020 when Maze shut down their operations, LockBit started their own data leak site asshown in figure 10\.Figure 10: LockBit data leak site25 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportIn June 2021, LockBit released a new version called LockBit 2\.0\. In July 2021, LockBit 2\.0 startedpublishing victim companies data on their data leak site. It uses the RaaS model. LockBit has solicitedaffiliates who were employed by their target organizations and had legitimate network access. LockBit hasbeen distributed through spam email campaigns that contain malicious attachments or links.LockBit has also been seen to gain access by brute forcing RDP or VPN credentials, via compromised RDPaccounts, and exploiting Fortinet VPNs CVE\-2018\-13379 vulnerability.Infection chain:In the first observed LockBit 2\.0 attack, the attacker used a hacked RDP account to access the targetedsystem. They then used a network scanner to recover network information and locate domain controllers.The threat actor used StealBit to exfiltrate the data, Process Hacker and PC Hunter to terminate processesand services related to the database, and other tools. A batch file was used to uninstall security productsand disable Windows event logs and Windows Defender features. Finally, LockBit used Windows grouppolicies to distribute and execute the LockBit 2\.0 ransomware.Hacked remote desktop
protocol (RDP) accountNetwork scanner to 
get network information and 
find domain controllerStealBit used to
exfiltrate the dataProcess hacker and PC Hunter 
used to terminate processes 
and services related to data 
based and other toolsBatch file used to uninstall 
security products, disable
Windows event logs and 
Windows Defender featureFigure 11: Anatomy of a LockBit ransomware attackUses group policy to
distribute and execute the 
LockBit 2\.0 ransomwarePart of what makes LockBit so popular is its efficiency: LockBit has the fastest encryption method as it usesa multi\-threaded encryption approach and encrypts only 4 KB of data for each file. It uses a combinationof RSA and AES algorithms to encrypt files. LockBit released a Linux and VMware ESXi variant in October2021\. This uses a combination of Advanced Encryption Standard (AES) and elliptic\-curve cryptography(ECC) algorithms for data encryption.26 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportFigure 12 displays the industry verticals targeted by double extortion attacks using LockBit.Lockbit infections by industryManufacturing
Services
Construction
Retail \& Wholesale
High Tech
Financial Services
Other
Legal
Real Estate
Education
Transportation Services
Food, Beverage \& Tobacco
Government
Restaurants, Bars \& Food Services
Basic Material and Chemicals
Insurance
Media
Nonprofit Institutions
Consumer Services
Telecommunications
Healthcare
Advertising
Oil \& Gas
Mining2%
2%2%
2%2%
2%1%
1%1%1%
1%1%6%6%5%4%4%
4%3%Figure 12: LockBit infections by industryLockBit: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionSpear
phishing linkCommand\- 
line interfaceBoot or logon 
autostart 
executionDeobfuscate
Decode files 
or informationAbuse
elevation 
control
mechanism: 
Bypass user 
account 
control10%8%8%7%18%DiscoverySystem 
network 
configuration 
discoveryLateral 
MovementCollectionExfiltrationImpactLateral tool 
transferArchive
collected dataExfiltration 
over web 
serviceData
encrypted for 
impactSpear 
phishing 
attachmentValid accountsExploit 
public\-facing 
applicationSupply chain 
compromiseRemote 
servicesData from 
local systemInhibit system 
recoveryDefacementImpair
defenses:
disable or 
modify toolsIndicator
removal on 
host: Clear 
windows 
event logsRemote
system
discoveryFile and 
directory 
discoveryDomain policy 
modification: 
group policy 
modificationSecurity 
software 
discovery27 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportPYSAMespinozaPYSA ransomware, also known as Mespinoza, was first spotted in October 2019\. They attack a wide rangeof industries around the world, but are known in particular for attacks on soft targets such as educationand hospitals.Infection chainPYSA achieves initial compromise through spam email or compromised RDP credentials. Next, the threatactors collect network information through scanning tools such as Port Scanner and the Advanced IPScanner developed by Famatech Corp. The attackers use post exploitation tools like Mimikatz, PowerShellEmpire, Koadic, and PsExec to steal credentials and move laterally. The WinSCP tool has been used toexfiltrate the data from victims systems. A PowerShell script disables security software and deletesshadow copies and system restore points, preventing victims from restoring their data. Finally, the attackerdeploys and executes the PYSA ransomware and encrypts the victims data.Spam email or 
compromised RDP 
serverDeploy and execute
PYSA ransomwareGet network information of 
running services in the system 
using Port Scanner and the
Advanced IP Scanner toolsMimikatz, PowerShell 
Empire, Koadic, and PsExec 
for credential stealing and 
lateral movementPowerShell script to disable 
security software and delete
shadow copies and system 
restore pointWinScp tool has been
used to exfiltrate the data
from victims' systemsFigure 13: Anatomy of a PYSA ransomware attack18% of PYSA attacks targeted 
educational institutions.28 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportPYSA uses a combination of RSA and AES\-CBC algorithms to encrypt files.Figure 14 displays the industry verticals targeted by double extortion attacks using PYSAMespinoza.PYSAMespinoza infections by industry10%
10%18%7%
7%6%
6%4%
4%
4%4%
4%3%
3%2%Education
Healthcare
Manufacturing
Services
Transportation Services
High Tech
Other
Construction
Government
Retail \& Wholesale
Oil \& Gas
Real Estate
Food, Beverage \& Tobacco
Nonprofit Institutions
Legal
Basic Materials and Chemicals
Financial Services
Insurance
Mining
Advertising
Aerospace \& Defense
Consumer Services
Media
Pharmaceutical
Telecommunication
Utilities1%
1%
1%
1%1%
1%
1%
1%
1%
1%
1%Figure 14: PYSAMespinoza attacks by industryPYSA will publish stolen data on their leak site (shown in figure 15\) if a victim does not pay a ransom.Figure 15: PYSAMespinoza data leak site29 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportPYSAMespinoza: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionSpear
phishing linkCommand\- 
line interfaceBoot or logon 
autostart 
executionAccess token 
manipulationDeobfuscate
Decode files 
or informationSpear 
phishing 
attachmentExecution 
through 
module loadScheduled 
taskjobValid accountsUser
executionImpair
defensesDomain policy 
modification: 
group policy 
modificationDiscoverySystem 
network 
configuration 
discoveryRemote
system
discoveryFile and 
directory 
discoverySecurity 
software 
discoveryQuery registryLateral 
MovementCollectionExfiltrationImpactLateral tool 
transferArchive
collected dataData from 
local systemExfiltration 
over
alternative 
protocolExfiltration 
over web 
serviceData
encrypted for 
impactInhibit system 
recoveryREvilSodinokibiREvil ransomware (a.k.a. Sodinokibi) was first spotted in April 2019 and has been one of the most activethreat groups over the last several years. REvil also uses a RaaS ecosystem. REvil started double extortion inJanuary 2020, first publishing data on a hacking forum. In February 2020, Sodinokibi attackers launchedtheir own data leak site as shown in Figure 16\.Figure 16: REvilSodinokibi data leak site30 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportThey also experimented with auctioning stolen data on their leak site until that proved unsuccessful.The REvil threat group famously exploited a zero day vulnerability in the Kaseya VSA server in July 2021\.The compromised Kaseya VSA server was used to send a malicious script to all clients that were managedby that VSA server.As noted previously, members of REvil were apparently arrested by Russian law enforcement in January2022\. However, the ransomware was updated and the infrastructure came back online in April 2022, atwhich point REvil attacks resumed.Infection chainREvil affiliates have used a variety of initial access mechanisms, including spam emails, exploit kits,compromised RDP accounts, and vulnerability exploits. An example campaign starts with a spam emailwith a malicious attachment. Once opened, the malicious attachment downloads a trojan such as IcedID,which serves as a pivot point for lateral movement. As shown in figure 17, REvil affiliates use a varietyof different tools like Cobalt Strike, SharpSploit, Mimikatz, and other post\-exploitation tools to stealcredentials. Further, affiliates collect network information using Netscan, BloodHound, AdFind, and othernetwork discovery tools. The attackers move laterally using PsExec or RDP access. Data exfiltration hasbeen performed using FileZilla, Rclone, MEGAsync, or FreeFileSync. Before deploying ransomware, REvilaffiliates are known to use PC Hunter, Process Hacker, KillAV, andor other scripts to terminate processesand services related to security software. Finally, the threat actor deploys the REvil ransomware andencrypts data.Spam email campaignCompromised RDP
accountsExploit kitsExploiting
vulnerabilitiesIcedIDCobalt Strike to steal
credentials and get a 
foothold into the systemPowerShell, macro, 
or other scriptSharpSploit, Mimikatz
or other post exploitation tools
to steal the credentialsNetscan, Bloodhound,
Adfind network discovery
tool to get network
informationDeploy and execute
REvil ransomware
and encrypt dataPC Hunter, Process Hacker,
KillAV, or other script used 
to terminate processes 
and services related to 
security softwareFigure 17: REvilSodinokibi attack chainData exfiltration using 
FileZIlla, Rclone,
MEGAsync, or FreeFileSyncPsExec or RDP access
used for lateral movement31 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportREvil uses asymmetric elliptic\-curve cryptography, using Curve25519 in combination with Salsa20, toencrypt files.Figure 18 displays the industry verticals targeted by double extortion attacks using REvil.16%9%8%8%
8%
8%7%5%
5%5%4%
4%3%REvilSodinokibi infections by industryManufacturing
Financial Services
Legal
Construction
Food, Beverage \& Tobacco
Other
Retail \& Wholesale
Real Estate
Services
High Tech
Basic Materials and Chemicals
Insurance
Transportation Services
Healthcare
Mining
Oil \& Gas
Restaurants, Bars \& Food Services
Telecommunications
Advertising
Agriculture \& Forestry
Consumer Services
Education
Government2%
2%
2%
2%
2%1%
1%
1%
1%
1%Figure 18: REvilSodinokibi infections by industryREvilSodinokibi: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionSpear
phishing linkCommand\- 
line interfaceBoot or logon 
autostart 
executionAccess token 
manipulationDeobfuscate
Decode files 
or informationImpair
defensesHijack
execution 
flowExploitation 
for privilege 
escalationSpear 
phishing 
attachmentExecution 
through 
module loadHijack
execution 
flowExploit 
public\-facing 
applicationShared
modulesDrive\-by 
compromiseUser
executionValid accountsSupply chain 
compromiseDiscoverySystem 
network 
configuration 
discoveryRemote
system
discoveryFile and 
directory 
discoverySecurity 
software 
discoveryQuery registryLateral 
MovementCollectionExfiltrationImpactLateral tool 
transferArchive
collected dataAutomated 
exfiltrationRemote 
servicesData from 
local systemExfiltration 
over web 
serviceData
encrypted for 
impactInhibit system 
recoverySystem
shutdown
rebootDefacement32 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportAvaddonAvaddon ransomware was first spotted in June 2020, and was very active at that time. Avaddon was yetanother ransomware family that used the RaaS ecosystem. In January 2021, Avaddon added DDoS intoits operation as a triple extortion tactic. Avaddon waged DDoS attacks on either the victims website ornetwork to encourage the victim to negotiate with its operators, forcing higher ransom amounts.Infection chainAvaddon gained access through different affiliates who utilized a range of vectors for the initialcompromise. Avaddon was most widely distributed in spam campaigns and exploit kits, but some affiliatesused brute force attacks or compromised RDP and VPN credentials to gain access to networks.In an example attack chain, Avaddon gained access to an initial broker that was initially infected throughcompromised credentials and used custom malware, such as BlackCrow and DarkRaven web shells, togain a foothold on the targeted system. Avaddon used SystemBC to get access to compromised hosts,then Mimikatz and SharpDump to steal credentials. The threat actor performed network scanning post\-exploitation using SoftPerfect Network Scanner, PowerSploit, and Empire. For lateral movement, Avaddonaffiliates used RDP, and Windows Scheduled Tasks for persistence. Before dropping the main ransomwarepayload, the threat actors exfiltrated data using MEGAsync and terminated processes and services relatedto security software. Finally, the threat actor dropped and executed the Avaddon payload and encryptedthe targeted systems.Compromised 
credentialsBlackCrow, DarkRaven,
and SystemBC to maintain
foothold and interact
with infected serversNetscan, BloodHound, 
Adfind network 
discovery tool to get 
network informationMimiKatz,
SharpDump to 
steal credentialsLateral movement using
Remote Desktop
Protocol (RDP) accessDeploy and execute 
Avaddon ransomware
and encrypt dataGMER, PowerTool, and 
TDSSKiller to terminate 
processes and services
related to security softwareMEGASync for data
exfiltrationFigure 19\. Anatomy of an Avaddon ransomware attack33 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportAvaddon used a combination of RSA and AES algorithms to encrypt files. In February, a researcherreleased a free decrypter after discovering a flaw, which Avaddon then fixed. In June 2021, Avaddon shutdown their operations and released victims decryption keys, allowing Emsisoft to build a decrypter forAvaddon ransomware.Similar to the other ransomware families discussed earlier, Avaddon followed the trend of creating dataleak websites, launching its own in August 2020, as shown in figure 20\.Figure 20: Avaddon data leak siteAfter Avaddon shut down in June 2021, the threat group relaunched attacks using the Thanos ransomwarebuilder. The threat group rebranded Avaddon as Haron and, in October 2021, rebranded the ransomwareagain under the name Midas.34 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportFigure 21 displays the industry verticals targeted by double extortion attacks using Avaddon.10%8%19%6%6%
6%5%
5%4%
4%
4%Avaddon infections by industryManufacturing
High Tech
Financial Services
Services
Government
Other
Construction
Transportation Services
Basic Material and Chemicals
Legal
Retail \& Wholesale
Consumer Service
Food, Beverage \& Tobacco
Healthcare
Insurance
Oil \& Gas
Aerospace \& Defense
Education
Mining
Telecommunications
Advertising
Agriculture \& Forestry
Nonprofit Institutions
Real Estate
Restaurants, Bars \& Food Services2%
2%
2%
2%
2%2%
2%
2%
2%1%
1%
1%
1%
1%Figure 21: Avaddon infections by industryAvaddon: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionSpear
phishing linkCommand\- 
line interfaceBoot or logon 
autostart 
executionValid
accountsDeobfuscate
Decode files 
or informationSpear 
phishing 
attachmentScheduled 
taskjobValid
accountsUser
executionExploit 
public\-facing 
applicationDrive\-by 
compromiseValid accountsImpair
defensesProcess 
injectionIndicator 
removal on 
hostIndicator 
removal on 
hostDiscoverySystem 
network 
configuration 
discoveryRemote
system
discoveryFile and 
directory 
discoverySecurity 
software 
discoverySecurity 
software 
discoveryLateral 
MovementCollectionExfiltrationImpactLateral tool 
transferArchive
collected dataData from 
local systemRemote
services:
remote
desktop 
protocolExfiltration 
over
alternative 
protocolData
encrypted for 
impactInhibit system 
recovery35 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportClopClop ransomware was first spotted in February 2019\. In March 2020, Clop started using double extortion,leaking stolen data of compromised organizations that did not pay ransoms to their data leak sites, asshown in figure 22\.Figure 22: Clop data leak siteThe Clop group focuses effort mostly on large organizations. ThreatLabz has observed the Clopransomware group demand eight\-figure ransom demands and even turn down multimillion\-dollar ransompayment offers.Clop ransomware was initially deployed by the TA505 and FIN11 threat groups. Clop has been widelydistributed in spam campaigns carried out by threat actor TA505\. ThreatLabz has observed severalClop attacks exploiting the SolarWinds Serv\-U CVE\-2021\-35211 vulnerability, which enables remotecode execution with elevated privileges, for initial access. The FIN11 threat group has exploited multiplevulnerabilities in the Accellion File Transfer Appliance (FTA) tracked as CVE\-2021\-27101, CVE\-2021\-27102, CVE\-2021\-27103, and CVE\-2021\-27104\. FIN11 then drops the DEWMODE web shell, whichexfiltrates data before dropping and executing Clop ransomware.Clop wages high\-profile 
attacks, causing an estimated 
$500M in damage as of 
November 2021\.36 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportInfection chainAn example attack by TA505 achieved compromise through a spam email containing an HTMLattachment. The attachment redirected to an XLS document file that further dropped the Get2 loader.The loader downloaded further payloads like SdBot, FlawedAmmy, FlawedGrace, and Cobalt Strike.After getting a foothold in the network and stealing and exfiltrating data, the threat group deployed andexecuted Clop ransomware, as illustrated in figure 23\.Spam emailHTML redirects to
XLS documentXLS downloads 
loader Get2FlawedAmmyy RATSdBotDownloads and executes
Clop ransomwareTinyMetCobalt Strike used to
steal credentialsFigure 23: Anatomy of a Clop ransomware attackClop uses a combination of RSA and AES algorithms to encrypt files.Figure 24 displays the industry verticals targeted by double extortion attacks using Clop.14%13%
13%11%9%8%
8%5%
5%Clop infections by industryManufacturing
Legal
Services
High Tech
Education
Other
Transportation Services
Construction
Healthcare
Agriculture \& Forestry
Government
Insurance
Pharmaceutical
Retail \& Wholesale
Advertising
Consumer Services
Food, Beverage \& TobaccoFigure 24: Clop infections by industry3%
3%
3%
3%
3%1%
1%
1%37 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportClop: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionDiscoveryLateral 
MovementExfiltrationImpactValid accountsCommand\- 
line interfaceBoot or logon 
autostart
executionAccess token 
manipulationMasquerading: 
invalid code 
signatureSystem network 
configuration 
discoveryLateral tool 
transferAutomated 
exfiltrationData
encrypted for 
impactRemote servicesExfiltration over 
web serviceInhibit system 
recoveryCreate or 
modify
system process: 
Windows 
serviceBypass user 
account controlImpair
defenses:
disable or
modify toolsRemote
system
discoveryExploitation 
for privilege 
escalationDeobfuscate
Decode files or 
informationFile and
directory
discoveryProcess 
injection: DLL 
injectionIndirect
command 
executionQuery registrySecurity
software
discoverySpear phishing 
attachmentUser
executionNative APIExploit 
public\-facing 
applicationSupply chain 
compromiseGriefGrief ransomware is a rebranding of DoppelPaymer, whose activity dropped significantly in May 2021following the Colonial Pipeline attack. Grief ransomware has lots of similarities with DoppelPaymer,including shared ransomware code and data leak websites. An example screenshot of the Grief leak site isshown in figure 25\.Figure 25: Grief data leak site38 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportThe Grief ransom portal has some differences from the DoppelPaymer portal. In particular, the ransomdemand payment method is made in Monero instead of bitcoin. This switch in cryptocurrencies may be inresponse to the FBI recovering part of the Colonial Pipeline ransom payment, which was made in bitcoin.Infection chainGrief ransomware has been deployed on systems that were previously infected with Dridex, which theattacker uses before using Cobalt Strike and deploying and executing the Grief ransomware payload. Griefuses a combination of 2048\-bit RSA and 256\-bit AES algorithms to encrypt files.DridexCobalt Strike to get
foothold and steals
the passwordsUse other post
exploitation to move
laterally into the
systemExecute Grief
ransomware that
deletes shadow copy and 
disable Windows Defender 
and encrypt filesFigure 26: Anatomy of a Grief ransomware attackFigure 27 displays the industry verticals targeted by double extortion attacks using Grief.17%9%8%7%7%
7%5%5%Grief infections by industryManufacturing
Retail \& Wholesale
Food, Beverage \& Tobacco
Education
Other
Transportation Services
Government
Services
Construction
Real Estate
Restaurants, Bars \& Food Services
Agriculture \& Forestry
Basic Materials and Chemicals
Healthcare
High Tech
Mining
Nonprofit Institutions
Consumer Services
Financial Services
Household \& Personal Product
Media
TelecommunicationsFigure 27: Grief infections by industry4%4%
4%3%3%
3%3%3%3%1%1%
1%1%1%39 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportGrief: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionValid accountsCommand\- 
line interfaceProcess
injectionBoot or logon 
autostart
execution:
registry run keys 
 startup folderHijack execution 
flow: DLL 
search order 
hijackingDiscoverySystem network 
configuration 
discoverySpear phishing 
attachmentUser
executionScheduled task
jobShared modulesDeobfuscate
Decode files or 
informationRemote
system
discoveryImpair
defenses:
disable or
modify toolsMasquerading: 
match
legitimate 
name or
locationFile and
directory
discoverySecurity
software
discoveryLateral 
MovementExfiltrationImpactLateral tool 
transferScheduled 
transferData
encrypted for 
impactInhibit system 
recoverySystem
shutdown
rebootHiveHive ransomware was first spotted in June 2021, using a RaaS model. It uses multiple mechanisms toachieve initial access, including malicious spam emails, leaked VPN credentials, and vulnerability exploitsin external\-facing assets. The initial infection starts with exploiting the ProxyShell vulnerabilities presentin Microsoft Exchange Server. ProxyShell exchange vulnerabilities are a combination of CVE\-2021\-34473(Microsoft Exchange Server remote code execution vulnerability), CVE\-2021\-34523 (Microsoft ExchangeServer elevation of privilege vulnerability), and CVE\-2021\-31207 (Microsoft Exchange Server securityfeature bypass vulnerability) vulnerabilities.Infection chainThe attacker creates a draft email item within a mailbox, with an attachment that contains the encodedweb shell. Then, the attacker exports the entire mailbox (malicious draft email included) to PST file formatwith an ASPX extension. This allows attackers to drop web shells on vulnerable servers. The web shelldownloads the PowerShell script that contains the encoded Cobalt Strike payload. It further downloadsadditional stagers and establishes a foothold in the victims system. It then uses Mimikatz to steal NTLMhashes and leverages a pass\-the\-hash tactic to access the domain control account. Hive performs furtherlateral movement over RDP using stolen credentials. It scans the network and gets additional informationusing the SoftPerfect Network scanner. At the end, it deploys and executes the Hive ransomware andencrypts the data.40 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportExploiting ProxyShellDownloadvulnerabilities to drop webshell in Exchange serverCobalt Strike beaconCobalt Strike establishedfoothold and downloadadditional stagerMimikatz used to stealcredentials and take controlof domain admin accountDeploy and executeHive ransomwareScan and fetch detailsRDP access using stolenof domain assetsusing SoftPerfectNetwork scannercredentials for lateralmovement and findcritical serversFigure 28: Hive attack chainEarlier versions of Hive ransomware payload were written in the Go programming language and used acombination of RSA and AES algorithms to encrypt files. More recent versions of Hive are written in theRust programming language and use Curve25519 and ChaCha20 for file encryption.Hive affiliates also exfiltrate data from victims prior to file encryption. A screenshot of the Hive data leaksite is shown in figure 29\.Figure 29: Hive data leak site41 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportFigure 30 displays the industry verticals targeted by double extortion attacks using Hive.Hive infections by industryConstructionRetail \& WholesaleServicesFinancial ServicesHealthcareHigh TechManufacturingOtherAerospace \& DefenseAgriculture \& ForestryLegalTransportation ServicesEducation4%4%4%
4%2%2%11%11%11%9%9%
9%7%Figure 30: Hive infections by industryNonprofit InstitutionsMediaRestaurants, Bars \& Food Services
Hive: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistenceExternal Remote 
servicesCommand\- 
line interfaceValid
accounts: 
Domain
accountsPrivilege 
EscalationDefense 
EvasionValid accountsClear windows 
event logsDiscoverySystem network 
configuration 
discoverySpear phishing 
attachmentUser
executionCreate account: 
domain
accountDomain
accountsImpair
defenses:
disable or
modify toolsRemote
system
discoveryRemote servicesExploit 
public\-facing 
applicationExploitation 
for privilege 
escalationDeobfuscate
Decode files or 
informationFile and
directory
discoveryQuery registrySecurity
software
discoveryLateral 
MovementExfiltrationImpactRemote desktop 
protocolScheduled 
transferData
encrypted for 
impactInhibit system 
recovery42 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportBlackByteBlackByte is another RaaS group that appeared prominently in July 2021\. It was originally written in C\# andlater redeveloped in the Go programming language around September 2021\. The Go\-based version sharesmany similarities with the C\# version, including the commands executed to perform lateral propagation,privilege escalation, and file encryption.BlackByte campaigns start with exploiting the ProxyShell vulnerabilities present in MicrosoftExchange Server.Infection chainThe attacker creates a draft email item within a mailbox. The email has an attachment that contains theencoded web shell. Then, the attacker exports the entire mailbox (malicious draft email included) to PSTfile format with an ASPX extension. This allows attackers to drop web shells on vulnerable servers.Next, the web shell is used to drop a Cobalt Strike beacon on the targeted Exchange server. Cobalt Strikeand other post\-exploitation tools are used to steal credentials and gain access to service accounts to get afoothold into the system. Furthermore, BlackByte installs the AnyDesk RDP tool. AnyDesk is used for lateralmovement and to drop Cobalt Strike in the infected domain controller. Finally, Cobalt Strike deploys andexecutes the BlackByte ransomware.Exploiting ProxyShell
vulnerabilities to drop
web shell in
Exchange serverCobalt Strike beaconCobalt Strike and post\-
exploitation tools 
used to steal credentials 
and gain access to 
service accountsCobalt Strike deploys
and executes BlackByte
ransomwareInstalls Cobalt Strike
beacon on
compromised domain
controllerAnyDesk used for
lateral movementFigure 31: Anatomy of a BlackByte ransomware attackInitial access by exploiting ProxyShell vulnerabilities to drop a web shell on the Exchange server. The webshell downloads the Cobalt Strike beacon. Cobalt Strike then steals credentials and installs the AnyDeskRDP tool. AnyDesk is used for lateral movement and drops Cobalt Strike in the infected domain controller.Cobalt Strike is then used to deploy and execute the BlackByte ransomware.43 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportBlackByte uses a combination of RSA and AES algorithms to encrypt files. The most recent BlackByteversions use Curve25519 ECC for asymmetric encryption and ChaCha20 for symmetric file encryption.The BlackByte threat actors also exfiltrate data from victims prior to file encryption. A screenshot of theBlackByte data leak site is shown in figure 32\.Figure 32: BlackByte data leak siteFigure 33 displays the industry verticals targeted by double extortion attacks using BlackByte.11%17%9%
9%
9%9%6%
6%
6%4%4%BlackByte infections by industryManufacturing
Other
Construction
Real Estate
Retail \& Wholesale
Food, Beverage \& Tobacco
Oil \& Gas
Services
Restaurant, Bars \& Food Services
Transportation Services
Aerospace \& Defense
Education
Energy
Financial Services
Government
Healthcare
High Tech
Mining
Nonprofit Institutions2%
2%
2%
2%
2%
2%
2%
2%
2%Figure 33: BlackBye infections by industry44 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportBlackByte: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionSpear phishing 
attachmentCommand 
and scripting 
interpreterDomain
accountsCreate or 
modify system 
process:
windows 
serviceImpair
defenses:
disable or
modify toolsDiscoverySystem network 
configuration 
discoveryExploit 
public\-facing 
applicationNative APIExploitation 
for privilege 
escalationDeobfuscate
Decode files or 
informationRemote
system
discoveryLateral 
MovementExfiltrationImpactLateral tool 
transferScheduled 
transferData
encrypted for 
impactInhibit system 
recoveryUser executionModify registryFile and
directory
discoveryQuery registrySecurity
software
discoveryAvosLockerAvosLocker ransomware is a RaaS group that appeared prominently in July 2021\. Like Hive and BlackByte,the initial infection starts with exploiting ProxyShell vulnerabilities CVE\-2021\-34473, CVE\-2021\-34523,and CVE\-2021\-31207 present in the Microsoft Exchange server.Infection chainThe attacker creates a draft email item within a mailbox. The email has an attachment that contains theencoded web shell. Then, the attacker exports the entire mailbox (malicious draft email included) to PSTfile format with an ASPX extension. This allows attackers to drop web shells on vulnerable servers.Next, the web shells are used to drop Cobalt Strike on the infected exchange server. Cobalt Strike andRclone are used to steal credentials and exfiltrate data to remote servers.The attack installs AnyDesk RDP to access multiple systems, moving laterally. It drops several batch scriptsto modify and delete registry keys related to security software. It also disables Windows Update andWindows Defender.Exploiting ProxyShell
vulnerabilities to drop
a web shell in
Exchange serverDownloadCobalt Strike beaconBatch script sets Registry 
Run Once key to 
execute the
AvosLocker ransomwareBatch script to 
modify or delete 
registry key related 
to security softwareFigure 34: Anatomy of an AvosLocker ransomware attackCobalt Strike and
Rclone used to steal
and exfiltrate dataDropsAnyDesk used for
remote access and
lateral movement45 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware Report 
At the end, AvosLocker reboots the system in Windows Safe Mode, and then the ransomware starts fileencryption. By booting in Safe Mode, AvosLocker can maximize the number of files that are encrypted,because business applications such as databases are likely not running. Therefore, those applicationswill not have open file handles that could prevent file encryption. In addition, many security softwareapplications (e.g antivirus programs) will not be loaded by default when the system is running in SafeMode. The ability to encrypt files in Windows Safe Mode is a feature that has been observed in otherransomware families including Conti, REvil, and BlackMatter.AvosLocker uses a combination of RSA and AES algorithms to encrypt files. AvosLocker created aLinux version of their ransomware that targets VMware ESXi.After the attack, the attacker threatens to publish the victims data to a data leak site and, in some cases,threatens and executes a DDoS attack on the victim network during negotiation. A screenshot of theAvosLocker data leak site is shown in figure 35\.Figure 35: AvosLocker data leak site46 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportFigure 36 displays the industry verticals targeted by double extortion attacks using AvosLocker.16%11%
11%9%7%
7%
7%5%
5%AvosLocker infections by industryManufacturing
Construction
Services
Retail \& Wholesale
Financial Services
Legal
Real Estate
Other
Transportation Services
Arts, Entertainment \& Recreation
Basic Materials and Chemicals
Consumer Services
Government
Healthcare
High Tech
Insurance
Mining
Oil \& Gas
Restaurant, Bars \& Food Services2%
2%
2%
2%
2%
2%
2%
2%
2%
2%Figure 36: AvosLocker infections by industryAvosLocker: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessExecutionPersistencePrivilege 
EscalationDefense 
EvasionSpear phishing 
attachmentCommand\- 
line interfaceDomain
accountsBoot or logon 
autostart
execution:
registry run keys 
 startup folderImpair
defenses:
disable or
modify toolsDiscoverySystem network 
configuration 
discoveryExploit 
public\-facing 
applicationUser
executionScheduled task
jobExploitation 
for privilege 
escalationDeobfuscate
Decode files or 
informationRemote
system
discoveryFile and
directory
discoverySecurity
software
discoveryLateral 
MovementExfiltrationImpactLateral tool 
transferScheduled 
transferData
encrypted for 
impactInhibit system 
recoverySystem shut\-
downreboot47 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportBlackCatALPHVBlackCat, a.k.a. ALPHV, is a RaaS operation that was first spotted around November 2021\. BlackCat hasused the RUST programming language, which helps to improve performance and reliable concurrentprocessing.Infection chainInitial infection starts with the use of compromised credentials to gain access to victims network systems.Initially it uses Cobalt Strike, PowerShell scripts, and batch script to get a foothold into the victimsnetwork. Once it gets access, it compromises admin accounts in Active Directory. Further, it uses maliciousGroup Policy Objects (GPOs) to deliver and execute ransomware. It also uses Microsoft Sysinternals andother administrative tools in the attack.Initial access through
compromised user
credentialsCompromised Active
Directory and 
admin account using
different toolsCobalt Strike to 
get footholdPowerShell script to
disable antivirusExecute ransomware
by using BAT script
through GPOFigure 37: Anatomy of a BlackCatALPHV ransomware attackBlackCat added DDoS tactics into its operation. BlackCat wages DDoS attacks on either the victims websiteor network to encourage the victim to negotiate with its operators and force higher ransom amounts. Anexample screenshot of the BlackCat data leak site is shown in figure 38\.Figure 38: BlackCatALPHV data leak site48 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportFigure 39 displays the industry verticals targeted by double extortion attacks using BlackCatALPHV.BlackCatALPHV infections by industry21%8%
8%
8%Manufacturing
Legal
Retail \& Wholesale
Transportation Services
Construction
Financial Services
Food, Beverage \& Tobacco
High Tech
Services
Advertising
Agriculture \& Forestry
Basic Materials \& Chemicals
Consumer Services
Education
Government
Mining
Oil \& Gas
Other
Real Estate
Restaurants, Bars \& Food Services5%
5%
5%
5%
5%3%
3%
3%
3%
3%
3%
3%
3%
3%
3%
3%Figure 39: BlackCatALPHV infections by industryBlackCat: MITRE ATT\&CK Tactics \& TechniquesInitial
AccessValid accountsExecutionPersistencePrivilege 
EscalationDefense 
EvasionCommand 
and scripting 
interpreterDomain
accountsBoot or logon 
autostart
execution:
registry run keys 
 startup folderImpair
defenses:
disable or
modify toolsDiscoverySystem network 
configuration 
discoveryUser
executionScheduled task
jobExploitation 
for privilege 
escalationDeobfuscate
Decode files or 
informationRemote
system
discoveryLateral 
MovementExfiltrationImpactLateral tool 
transferScheduled 
transferData
encrypted for 
impactInhibit system 
recoveryDomain policy 
modification: 
group policy 
modificationFile and
directory
discoverySecurity
software
discovery49 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportAbout ThreatLabzThreatLabz is the security research arm of Zscaler. This world\-class team is responsible for hunting newthreats and ensuring that the thousands of organizations using the global Zscaler platform are alwaysprotected. In addition to malware research and behavioral analysis, team members are involved in theresearch and development of new prototype modules for advanced threat protection on the Zscalerplatform, and regularly conduct internal security audits to ensure that Zscaler products and infrastructuremeet security compliance standards. ThreatLabz regularly publishes in\-depth analyses of new andemerging threats on its portal, research.zscaler.com.Stay updated on ThreatLabz research by subscribing to our Trust Issues newsletter today.The Zscaler Zero Trust Exchange has been named by Gartner as a leading security service edge (SSE)platform, delivering ransomware protection across every stage of the attack chain to dramatically reduceyour chance of being attacked and mitigate potential damages.Zscaler natively integrates industry\-leading capabilities to:Minimize the 
attack surfaceZscalers cloud nativeproxy\-based architecturereduces the attacksurface by makinginternal apps invisibleto the internet, thuseliminating potentialPrevent 
compromiseZscaler deliversfull inspection andauthentication ofall traffic, includingencrypted traffic, toEliminate lateral 
movementStop
data lossZscaler safely connectsZscaler inspects allusers and entities directlytraffic outbound to cloudto applicationsnotapplications to preventnetworksto eliminatedata theft, and usesthe possibility ofcloud access securitykeep malicious actorslateral movement, andbroker (CASB) capabilitiesout, leveraging toolssurrounds your crownto identify and remediateattack vectors.such as browser isolationjewel applications withvulnerabilities in dataand inline sandboxingto protect users fromunknown andevasive threats.realistic decoys forgood measure.at rest.To learn more, visit our Zscaler Ransomware Protection page.50 2022 Zscaler, Inc. All rights reserved.ThreatLabz 2022 Ransomware ReportAbout Zscaler 
Zscaler (NASDAQ: ZS) accelerates digital transformation so that customers can be more agile, efficient, resilient, 
and secure. The Zscaler Zero Trust Exchange protects thousands of customers from cyberattacks and data loss 
by securely connecting users, devices, and applications in any location. Distributed across more than 150 data 
centers globally, the SASE\-based Zero Trust Exchange is the worlds largest inline cloud security platform.
Learn more at zscaler.com or follow us on Twitter @zscaler. 2022 Zscaler, Inc. All rights reserved. Zscaler, 
Zero Trust Exchange, Zscaler Internet Access, 
ZIA, Zscaler Private Access, ZPA and 
other trademarks listed at zscaler.comlegal
trademarks are either (i) registered trademarks or 
service marks or (ii) trademarks or service marks 
of Zscaler, Inc. in the United States andor other 
countries. Any other trademarks are the properties 
of their respective owners.zscaler.com\+1 408\.533\.0288Zscaler, Inc. (HQ)120 Holger WaySan Jose, CA 95134