THE STATE OF
CLOUD SECURITY 2020
The results of an independent study 
of 3,521 IT managers hosting data 
and workloads in the public cloudA Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Introduction
Thanks to growing demand for remote working and public cloud services, on\-premises 
infrastructure is shifting from asset to liability. But moving to the cloud comes at a cost: 
increasing every organizations attack surface. The numerous and well\-publicized breaches 
of data storage services have raised cloud security awareness, but cybercriminals work 
diligently to stay one step ahead.To understand the reality behind the headlines, Sophos commissioned an independent 
survey of 3,251 IT managers across 26 countries who are using the public cloud. The 
findings provide brand new insights into the concerns for security teams that host data and 
workloads in the public cloud; how attackers are changing the rules to find new ways into 
environments; and how to find the visibility you need and perhaps the security gaps you 
never knew you had.About the survey
Sophos commissioned research specialist Vanson Bourne to survey 3,521 IT managers 
currently hosting data and workloads in the public cloud about their experiences with 
cloud security. By public cloud we mean organizations using at least one of the following 
providers: Azure, Oracle Cloud, AWS, VMWare Cloud on AWS, and Alibaba Cloud. In addition, 
they may also have used Google Cloud and IBM Cloud. Sophos had no role in the selection 
of respondents and all responses were provided anonymously. The survey was conducted 
during January and February 2020\.48% of survey respondents using the public cloud were from small organizations (100\-
1000 employees), and 52% were from larger organizations (1001\-5000 employees).Respondents came from 26 countries across six continents:COUNTRY\# RESPONDENTSCOUNTRY\# RESPONDENTSCOUNTRY\# RESPONDENTSAustraliaBelgiumBrazilCanadaChinaColombiaCzech RepublicFranceGermany1486613613116212063203194IndiaItalyJapanMalaysiaMexicoNetherlandsNigeriaPhilippinesPoland22712812679140150656253SingaporeSouth AfricaSpainSwedenTurkeyUAEUKUS158158139727265191413Respondents came from a range of sectors, both public and private.SECTOR\# RESPONDENTS% RESPONDENTSIT, technology and telecomsManufacturing and productionRetail, distribution and transportFinancial servicesBusiness and professional servicesPublic sectorConstruction and propertyEnergy, oilgas and utilitiesMedia, leisure and entertainmentOther73546644940935730817712512037521%13%13%12%10%9%5%4%3%11%1A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Executive summary
The survey provides fresh new insights into the experiences of organizations hit by 
cybercriminals in the public cloud, including: Almost three\-quarters of organizations hosting data or workloads in the public cloudexperienced a security incident in the last year. Seventy percent of organizations 
reported they were hit by malware, ransomware, data theft, account compromise 
attempts, or cryptojacking in the last year. Data lossleakage is the number one concern for organizations. Data loss and leakage 
topped our list as the biggest security concern, with 44% of organizations seeing data 
loss as one of their top threefocus areas. Ninety\-six percent of organizations are concerned about their current level of cloudsecurity. Data loss, detection and response, and multi\-cloud management top the list of 
the biggest concerns among organizations. Multi\-cloud organizations reported more security incidents in the last 12 months. 
Seventy\-three percent of the organizations surveyed were using two or more public 
cloud providers and reported more security incidents as those using a single platform. European organizations may have the General Data Protection Regulation (GDPR)to thank for the lowest attack rates of all regions. The GDPR guidelines focus on data 
protection, and well\-publicized ransomware attacks have likely led to these lucrative 
targets becoming harder for cybercriminals to compromise in Europe. Only one in four organizations see lack of staff expertise as a top concern despite the 
number of cyberattacks reported in the survey. When it comes to hardening security 
postures in the cloud, the skills needed to create good designs, develop clear use cases, 
and leverage third\-party services for platform tools are crucial but underappreciated. Two\-thirds of organizations leave back doors open to attackers. Accidental exposurethrough misconfigurations continues to plague organizations. Security gaps in 
misconfigurations were exploited in 66% of attacks (either through attackers exploiting 
a flaw in the web application firewall to access account credentials or attackers taking 
advantage of a misconfigured resource), while 33% of attacks used stolen credentials to 
get into cloud provider accounts.Use of data and charts in this report
We encourage the re\-use of data, charts, and text published in this report. You are free to share 
and make commercial use of this work as long as you attribute the Sophos State of Cloud 
Security 2020\.2A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Part 1: The prevalence of cloud attacks
Seven in 10 organizations have been hit by a cyberattack
Seventy percent of respondents said they had suffered a public cloud security breach in the 
last year. This is extremely worrisome for organizations, with 96% of the 3,521 respondents 
expressing concern about their current level of security across the six major public cloud 
platforms listed, including Amazon Web Services, Microsoft Azure, and Google Cloud Platform.70%of organizations suffered 
a public cloud security 
breach in the last year96%of organizations are 
concerned about their 
current level of 
cloud securityAs you move, so does the target
Among organizations suffering a cyberattack in the cloud, the breakdown of attack types 
reads like the usual suspects: 50% of organizations were hit by malware of some form, 
including ransomware (respondents could select multiple options).Organizations suffering security incidents in the last yearMalwareExposed DataRansomwareAccount
CompromiseCryptojacking17%34%29%28%25%20%
Has your organization suffered a public cloud security incident in the last 12 months? Base 3,521 respondents40%0%60%80%100%3A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Attack levels vary across the globe
Looking at the number of public cloud attacks across the globe reveals interesting 
variations. This is likely due to criminals focusing their efforts where they see the greatest 
opportunity for return. Country\-level analysis also showed differing levels of protection and 
visibility of cloud environments, and awareness of cloud security responsibilities and best 
practices.Organizations suffering public cloud security incidents in the last yearIndiaNigeriaPhilippinesSwedenBrazilTurkeyColombiaUAEFranceAustraliaMexicoMalaysiaNetherlandsSingaporeChinaBelgiumUSCzech RepublicCanadaGermanySouth AfricaUKJapanSpainPolandItaly93%86%82%82%79%79%76%75%75%74%74%73%71%71%70%68%68%67%65%61%61%61%59%57%47%45%0%20%40%60%Global Average80%100%Has your organization suffered a public cloud security incident in the last 12 months? Combination of Yes answers (Yes Malware, 
Yes, Exposed Data, Yes, Ransomware, Yes, Account Compromise, and Yes, Cryptojacking. Base 3,521 respondents India (227 respondents) tops the list with 93% of organizations reporting being hit by a 
cyberattack in the last year, despite 92% of organizations reporting they had complete 
visibility of all cloud assets. This indicates a lack of complete cyber hygiene, creating 
weaknesses in cloud security configurations which make organizations vulnerable to 
attack. This trend of the highest proportion of attacks echoes throughout the Asia\-Pacific 
(APAC) region, with the highest regional rates of exposed data (35%), ransomware 
attacks (37%), and account compromise (33%) among the survey respondents. Europe (1259 respondents) may have GDPR to thank for its low attack rate, withEuropean respondents suffering the lowest percentage of security incident rates of all 
respondents in the last year. This includes Italy (45%), Poland (47%), Spain (57%), UK 
(61%) and Germany (61%).4A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020The focus on protection of data and well\-publicized ransomware attacks have likely 
led to these lucrative targets being better protected than other regions. As a result, 
Europe shows the lowest rates of malware infections (29%), exposed data (24%), and 
ransomware attacks (22%) among the survey respondents. This also explains the higher 
comparative levels of account compromise incidents (21%) and cryptojacking (15%), as 
attackers move to exploit resource misconfigurations and over\-privileged IAM roles to 
compromise cloud environments. Middle East and Africa (360 respondents) has some of the lowest attack ratesoutside of Europe, the result of geo\-targeted attacks that go after the most lucrative 
opportunities. However, value is in the eye of the beholder. Here we see cryptojacking at 
its highest among all regions (22%) as criminals spin up hundreds of virtual servers to 
run illegal cryptomining and escape before being discovered. United States (413 respondents) reported surprisingly few incidents despite being the 
largest group of survey respondents. It was in the bottom 35% of countries suffering 
security incidents in the last year. As an advanced, Western country, it could be 
considered a lucrative target, yet only 30% of respondents report being hit by malware, 
31% by ransomware, 28% suffering a data breach, and 21% having account credentials 
compromised. Contributing factors here point to clear ownership of security, with 
90% of organizations understanding their responsibility for cloud security. With 85% of 
organizations being aware of all their cloud assets, the U.S. is a full 17 percentage points 
higher than the global awareness average.Organizations hit by malware in the public cloud in the last yearTurkeyPhilippinesUAEIndiaNigeriaChinaCanadaSingaporeColombiaBrazilAustraliaMexicoBelgiumCzech RepublicSwedenGermanyFranceNetherlandsUSSouth AfricaSpainUKItalyJapanMalaysiaPoland63%58%54%49%43%41%40%37%35%35%34%34%33%33%33%32%31%31%30%28%27%27%23%23%23%17%0%20%40%60%80%100%Has your organization suffered a public cloud security incident in the last 12 months? Yes, Malware. Base 3,521 respondents5A Sophos whitepaper July 2020Organizations hit by ransomware in the public cloud in the last yearTHE STATE OF CLOUD SECURITY 202054%53%39%35%34%33%33%31%MalaysiaIndiaAustraliaBrazilNigeriaBelgiumChinaUSSingaporeUAECzech RepublicFranceMexicoSwedenSouth AfricaColombiaGermanyNetherlandsItalyPhilippinesCanadaJapanUKSpainPolandTurkey28%28%27%26%25%25%25%24%24%23%20%19%19%19%18%17%9%7%0%20%40%60%80%100%Has your organization suffered a public cloud security incident in the last 12 months? Yes, Ransomware. Base 3,521 respondentsOrganizations with public cloud data exposed in the last yearNigeriaIndiaPhilippinesMalaysiaSwedenChinaColombiaCanadaAustraliaSingaporeCzech RepublicNetherlandsBrazilSouth AfricaUSMexicoFranceUKPolandJapanBelgiumGermanySpainUAEItalyTurkey57%49%40%35%33%33%33%31%30%30%30%30%29%28%28%28%28%24%23%21%21%20%18%15%15%13%0%20%40%60%80%100%Has your organization suffered a public cloud security incident in the last 12 months? Yes, Exposed Data. Base 3,521 respondents6A Sophos whitepaper July 2020Organizations with cloud account credentials stolen in the last yearTHE STATE OF CLOUD SECURITY 2020IndiaNigeriaMalaysiaPhilippinesNetherlandsCzech RepublicJapanChinaAustraliaSouth AfricaSwedenTurkeyCanadaFranceBelgiumBrazilUSGermanyColombiaSpainMexicoSingaporeUAEPolandItalyUK48%46%42%40%32%32%29%28%28%27%26%24%23%22%21%21%21%20%20%19%19%19%17%15%15%12%0%20%40%60%80%100%Has your organization suffered a public cloud security incident in the last 12 months? Yes, Stolen Credentials. Base 3,521 respondentsOrganizations suffering a cryptojacking cyberattack in the public cloud in the last year36%26%26%26%25%25%25%24%22%IndiaNigeriaSouth AfricaBelgiumBrazilSwedenAustraliaNetherlandsMalaysiaJapanColombiaCzech RepublicUAEPhilippinesTurkeyGermanyFranceSingaporeUSUKCanadaMexicoSpainItalyChinaPoland6%4%4%18%18%17%17%16%15%15%14%13%13%12%11%10%8%0%20%40%60%80%100%Has your organization suffered a public cloud security incident in the last 12 months? Yes, Cryptojacking. Base 3,521 respondents7A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Part 2: How criminals are getting in
Two\-thirds of organizations leave back doors open to criminals
When it comes to the cloud, its best to think of a network like a building with multiple 
windows and multiple openings they all add up to multiple potential access points for 
someone, or something, to get in and out.For example, a misconfigured route table on an organizations firewall leaves the window 
open. Virtual machines running private server workloads or hosting sensitive data suddenly 
become accessible from the internet.Accidental exposure continues to plague organizations, and this is reflected in our survey 
responses. Security gaps in misconfigurations were exploited in 66% of attacks, while 33% 
of attacks used stolen credentials to get into cloud provider accounts.As organizations start to introduce new cloud services in order to provide shared storage, 
containers, database services, and serverless functions, the potential for misconfiguration 
only increases, which in turn expands an organizations attack surface.66%Breached through 
a security 
misconfiguration33%Had cloud account 
credentials stolen22%Cloud resource 
misconfiguration44%Misconfigured web 
application firewall 
(WAF)How did the attacker get into your organizations environment? Base 3,521 respondents8A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Entry methods vary across the globe
Every organization represents value to a cybercriminal. That value might be in the data that 
can be sold or held onto for ransom. It could also be the organizations wallet thats used to 
pay for cryptomining virtual machines. And while in the real world, targeting based on Gross 
Domestic Product (GDP) or industry sectors may be the norm, isnt as clear cut in the cloud.An organizations security posture is often the deciding factor when it comes to choosing 
entry methods and weak points (misconfiguration 66%, or credentials 33%). But its 
important to realize that though misconfigurations can still give cybercriminals access to 
cloud accounts, such access may last for less time: up to six hours or so when temporary 
credentials are obtained thanks to a resource misconfiguration, for instance.Our survey also highlights the role that visibility of cloud assets plays when it comes to how 
an organization is targeted: South Africa and Japan showed the highest number of stolen cloud provider account 
credentials in our survey. These organizations also have amongst the highest levels of 
asset visibility across cloud environments, which suggests a stronger security posture 
overall with less chance of misconfigurations. Turkey and Poland show the reverse: with the lowest levels of visibility, these 
organizations were most likely to be attacked via misconfigured cloud assets.How organizations were compromisedSouth AfricaJapanIndiaSwedenBelgiumUKSingaporeNigeriaGermanyNetherlandsCzech RepublicFranceAustraliaBrazilSpainPhilippinesCanadaMalaysiaColombiaUSUAEChinaItalyMexicoPolandTurkey39%39%44%49%58%59%63%64%64%64%67%67%69%69%70%71%72%74%75%75%76%0%20%40%60%MisconfigurationStolen CredentialsOtherDon't KnowHow did the attacker get into your organizations environment? Base 2,456 respondents. Due to rounding, occasionally the totals do 
not add up to 100%59%59%55%49%40%38%2%1%0%2%2%3%37%0%36%0%35%35%1%1%33%0%31%29%29%29%27%25%2%2%2%1%2%4%26%0%25%0%23%20%17%1%6%1%2%18%0%16%0%16%0%100%18%979%81%82%84%84%80%A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Identity security represents a huge challenge
A review of cloud accounts by the Sophos Cloud Optix cloud security posture management 
service discovered worrying trends in organizations security posture as it relates to cloud 
account access.Thirty\-three percent of organizations reported that cybercriminals gained access by 
stealing cloud provider account credentials. Once inside, however, all attacks utilized 
Identity and Access Management (IAM) roles and permissions to navigate the compromised 
cloud accounts. Managing access to cloud accounts is an enormous challenge and yet only 
quarter of organizations in our survey saw it as a top area for concern.The scale and interwoven nature of individual and group access to services means that 
organizations often simply cant accurately see how their services can be accessed, and 
this lack of visibility is exploited by attackers.91%Had overprivileged 
Identity and Access 
Management roles98%Had MFA disabled on 
their cloud provider 
accountsWhy it Matters
Granting extensive access permissions to IAM 
users, groups and cloud services is a risky 
practice. If those credentials are compromised, 
the cybercriminals will have access to any 
services and data those permissions grant.Why it Matters
All user accounts should have MFA enabled 
to ensure protection against password 
compromises. MFA adds an extra layer of 
protection on top of a username and password.10A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Part 3: Organizations are not focusing on root causes
The most worrying outcome for organizations is data loss
Data security topped the list as the most likely concern, cited by 44% of respondents. 
The rapid growth of cloud usage has resulted in fractured distribution of data, with 73% 
of organizations now utilizing at least two public clouds platforms. This multi\-platform 
approach compounds the visibility challenge for security teams, who often must switch 
between multiple platforms for a complete picture of cloud assets.Top cloud security concerns among organizationsData lossleakageIdentifying and responding 
to security incidentsManaging multiple 
public cloud providersIdentifying sudden 
increases in cloud spendStaying compliant with 
relevant regulationsManaging user roles 
and permissionsConvincing senior 
management of the need to 
invest in cloud securityLack of staff expertiseLack of visibility of 
our infrastructureSecurity cant keep up with 
the pace of our developersMy organization does not have any 
public cloud security concerns3%Don't know1%44%41%28%27%26%26%25%25%24%24%0%20%40%60%80%100%Combination of responses ranked first, second and third for the question What are your organization's biggest public cloud security 
concerns? Base 3,521 respondentsA significant root cause is a lack of cloud expertise
To properly secure a cloud environment, good design and clear use cases are necessary 
in order to leverage platform tools effectively and extend them with third\-party services. 
This requires skilled experts, either employed directly by organizations or available through 
partners. Unfortunately, while 70% of organizations in our survey suffered a security breach 
in the last year, only a quarter see lack of staff expertise as a top concern.11A Sophos whitepaper July 2020The impact of configurations on data security
A review of cloud accounts by the Sophos Public Cloud Security team discovered that 
accidental data exposure through misconfigured storage services continues to plague 
organizations, with 60% leaving information unencrypted. Organizations are making it easy 
for attackers to search for and identify new targets.THE STATE OF CLOUD SECURITY 2020Organizations had 
storage services without 
encryption turned onOrganizations had 
databases without 
encryption turned onOrganizations had databases 
open to the Internet13%Organizations had storage 
services with public readlist 
permission enabled18%65%85%0%20%40%60%80%100%Why it matters
Encryption is critical in stopping cybercriminals from seeing and reading stored information, 
and is a requirement for many compliance and security best\-practice standards. While 
public mode, a setting that can be applied to databases, shared storage and other cloud 
provider services is a major course of data breaches. Misconfiguring cloud services in 
public mode allows cybercriminals to automate their searches for these weak points in 
security. Guardrails should be in place to prevent such misconfigurations.Most successful ransomware attacks now hit the public cloud
In parallel to this cloud security survey, Sophos recently released a survey of 5,000, IT 
managers that explored their experiences with ransomware. Among those organizations, 
59% of attacks where the data was encrypted involved data in the public cloud. While its 
likely that respondents took a broad interpretation of public cloud including cloud\-based 
services such as Google Drive and Dropbox, and cloud backup such as Veeam its clear 
that cybercriminals are targeting data wherever its stored.59%Includes data in 
the public cloud41%On premises
private cloud 
data35%Data in the public 
cloud24%Data in the public 
cloud and on 
premisesprivate 
cloud dataDid the cybercriminals succeed in encrypting your organizations data in the most significant ransomware attack? Responses from 
respondents whose organizations data had been encrypted in the most recent ransomware attack. Base: 1,849 respondents.12A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Multi\-cloud creates multiple challenges
Security risks inevitably multiply as organizations expand their number of cloud 
environments. Seventy\-three percent of the organizations surveyed were using two or more 
public cloud providers and reported up to twice as many security incidents as those using 
one cloud platform.Single and multi\-cloud organizations hit by cyberattacks in the last yearMalwareExposed DataRansomwareAccount 
compromiseCryptojacking7%1%2%0%0%Don't knowYes, otherNot suffered a 
cloud security 
incident0%14%17%12%21%21%22%20%39%34%32%30%50%40%60%80%100%Two or more public cloudsOne public cloudMulti\-cloud organizations include those respondents selecting one or more cloud providers for the question Which of the following 
public clouds does your organization host data or workloads in? Base 3,521 respondentsThe secret to effective cybersecurity across dispersed environments in Amazon Web 
Services, Microsoft Azure, and Google Cloud Platform is to improve overall security posture 
and address the most important security aspects. Ensure architecture is secure and 
configured correctly, gain complete architecture visibility, regularly review who has access 
to cloud accounts and services (including permissions levels), and, importantly, ensure 
consistent security management across multiple cloud environments.24%13A Sophos whitepaper July 2020THE STATE OF CLOUD SECURITY 2020Recommendations
Moving from traditional to cloud\-based workloads offers huge opportunities for 
organizations of all sizes, yet this survey has confirmed that securing the public cloud is 
imperative. It also provides insight into how to minimize the risk of a security incident:1\. Start with the assumption that attackers will find cloud assets. Cybercriminals areautomating their searches for vulnerable cloud services. Whether an organization has 
used the cloud to host data and workloads for some time or has recently accelerated 
the use of public cloud provider services, accurate visibility of cloud services in use is 
the only guaranteed route to ensure they are configured securely and protected against 
threats.2\. Invest in cloud workload protection with anti\-malware technology. Seventy percentof survey respondents suffered a security incident in the last year. Among that majority, 
34% were hit by malware, 28% hit by ransomware (an advanced form of malware), and 
17% were hit by cryptojacking (which can be malware). These results highlight that 
malware is the number one threat to organizations and the sensitive data they hold.3\. Protect data wherever its held. Data protection is the highest concern for globalorganizations. Almost 60% of ransomware attacks in the last year that successfully 
encrypted data included data in the public cloud. Cloud strategies should include 
protecting data in the public cloud, private cloud, and on premises.4\. Continually monitor cloud resource configurations. Two\-thirds of survey respondentswere compromised through misconfigured cloud resources, allowing attackers to 
exploit these weaknesses to carry out malicious activity. Proactive monitoring of 
configurations by a security team can significantly reduce the likelihood of breaches.5\. Proactively manage cloud access. On average, IAM roles were compromised in 33% of 
cyberattacks reported by the survey respondents, rising to 59% in specific countries. 
Effective management of individual and group user permissions is key to ensuring over\-
privileged roles are not compromised.6\. Provide secure remote access for workers. Ensure the same level of protection is inplace for virtual desktops as it is for other critical server workloads. Virtual desktops run 
on virtual machines, which are susceptible to the same threats. Likewise, as remote 
workers access private applications and sensitive data, they should be equipped with 
VPN access to ensure secure connections.7\. Deploy a layered defense. Cybercriminals use a wide range of techniques to get around 
defenses. When one is blocked, they move on to the next one until they find something 
a weakness that can be exploited. Make sure to defend against all possible vectors of 
attack.8\. Learn responsibilities for securing public cloud provider services. Public cloud 
providers offer a great deal of flexibility. And while theyre responsible for physical 
protection at the datacenter and virtual separation of customer data and environments, 
whatever organizations store or run in the cloud is their responsibility to secure. Almost 
half of survey respondents didnt fully understand their responsibilities. To find out more, 
visit the Amazon Web Services or Microsoft Azure websites.14A Sophos whitepaper July 2020Secure the cloud with Sophos
Protection from the latest generation of public cloud cyberattacks requires a new level of 
visibility and security automation. Sophos gives you the advanced protection technologies 
you need to disrupt the entire attack chain.THE STATE OF CLOUD SECURITY 2020Cloud Storage and DatabasesVirtual MachinesContainers and ServerlessstreamFor Server with EDRSecurity AnalysisIdentity SecurityWorkload ProtectionNetwork Firewalling Sophos Cloud Optix extends detection and response in the public cloud. Continuallymonitor cloud infrastructure configurations to detect insecure deployments, suspicious 
access events, over\-privileged IAM roles, unusual network traffic, and sudden spikes in 
cloud spend, with guided remediation to shrink incident response times. Guardrails lock 
down configurations to stop accidental or malicious changes that could impact security 
posture. Sophos Intercept X for Server with EDR secures cloud, on\-premises, or hybrid workloadenvironments. It protects Windows and Linux virtual machines and virtual desktops 
from the latest threats, including ransomware, file\-less attacks, and server\-specific 
malware. Automate detection and response with unparalleled visibility to hunt down 
evasive threats, see and control exactly which apps are running, and automatically 
respond to incidents. Sophos XG Firewall protects the network edge with the ultimate all\-in\-one firewall 
solution. Get deep packet inspection with VPN for remote workers, IPS, ATP, URL 
filtering, bidirectional antivirus for WAF with authentication offloading, path\-based 
routing, and country\-level blocking. Synchronized communication with cloud workloads 
automates isolation and malware clean\-up.Start an instant demo at
www.sophos.comdemoUnited Kingdom and Worldwide Sales
Tel: \+44 (0\)8447 671131
Email: sales@sophos.comNorth American Sales
Toll Free: 1\-866\-866\-2802
Email: nasales@sophos.comAustralia and New Zealand Sales
Tel: \+61 2 9409 9100
Email: sales@sophos.com.auAsia Sales
Tel: \+65 62244168
Email: salesasia@sophos.com Copyright 2020\. Sophos Ltd. All rights reserved.
Registered in England and Wales No. 2096520, The Pentagon, Abingdon Science Park, Abingdon, OX14 3YP, UK
Sophos is the registered trademark of Sophos Ltd. All other product and company names mentioned are 
trademarks or registered trademarks of their respective owners.20\-06\-18 WPEN (DD)