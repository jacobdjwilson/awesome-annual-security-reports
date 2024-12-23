# Annual Cyber Threat Report 2023–2024

## Table of Contents
- [Imprint](#imprint)
- [Foreword](#foreword)
- [Contents](#contents)
- [About ASD’s ACSC](#about-asds-acsc)
- [About the contributors](#about-the-contributors)
- [Executive summary](#executive-summary)
- [Year in review](#year-in-review)
- [State actors](#state-actors)
- [Critical infrastructure](#critical-infrastructure)
- [Cybercrime](#cybercrime)
- [Hacktivism](#hacktivism)
- [Resilience](#resilience)
- [ASD programs](#asd-programs)
- [Notes](#notes)
- [Sources](#sources)
- [Glossary](#glossary)

## Imprint
Website 
www.cyber.gov.au 
Contact us
ASD welcomes feedback to improve the services it provides to Australians. 
Feedback can be provided by emailing asd.assist@defence.gov.au. Alternatively, 
a feedback form can be found at: https://www.cyber.gov.au/about-us/about-acsc/contact-us.
Copyright
© Commonwealth of Australia 2024
With the exception of the Coat of Arms, the entity’s logo, third party content and where otherwise 
stated, all material presented in this publication is provided under a Creative Commons Attribution 
3.0 Australian Licence. To the extent that copyright subsists in a third party, permission will be 
required by a third party to reuse the material.
Creative Commons Attribution 3.0 Australia Licence is a standard form licence agreement that allows 
you to copy, distribute, transmit and adapt this publication provided that you attribute the work.
The details of the relevant licence conditions are available on the Creative Commons website, as is 
the full Creative Commons legal code.
The Commonwealth’s preference is that you attribute this publication (and any material sourced 
from it) using the following wording: © Commonwealth of Australia 2024, Australian Signals 
Directorate, 2023–24 Annual Cyber Threat Report.
Use of the Coat of Arms
The terms under which the Coat of Arms can be used are detailed at:
www.pmc.gov.au/government/commonwealth-coat-arms
Acknowledgement of Country
We acknowledge the Traditional Owners and Custodians of Country throughout Australia and their 
continuing connections to land, sea and communities. We pay our respects to them, their cultures 
and their Elders, past and present. We also recognise Australia’s First Peoples’ enduring contribution 
to Australia’s national security.
Annual Cyber Threat Report
2023–2024
v

## Foreword
I am pleased to present the 2023–24 Annual Cyber Threat Report.
This year’s report comes amid a continued deterioration in Australia’s strategic environment. The 
Indo‑Pacific continues to face entrenched strategic competition, Russia’s invasion of Ukraine has entered its 
third year and conflict continues to unfold in the Middle East.  
As the 2024 National Defence Strategy outlined, these challenges are being compounded by rapid 
technological advancements. Malign actors – both state and non-state – are improving their cyber 
capabilities, increasing the risk of disruptions to Australia’s critical systems, infrastructure and networks. 
Grey-zone activities have also expanded in the Indo-Pacific, with malicious cyber actors continuing to 
conduct espionage and spread disinformation.
This year’s report outlines the cyber threat posed to Australian governments, critical infrastructure, 
businesses and households. It shows how malicious state actors and cybercriminals are continuing to 
adapt their tradecraft in an attempt to compromise Australian networks. 
These circumstances underline the significant role that cyber capabilities play in safeguarding our national 
security and the critical role ASD continues to play in protecting Australians. That is why the Albanese 
Government has committed $15–$20 billion to 2033–34 to enhance our cyber domain capabilities as part of 
the 2024 Integrated Investment Program. 
This significant investment will provide greater visibility of threats to critical infrastructure, increase the 
resilience of our infrastructure to cyber attacks, provide new intelligence functions and enable offensive 
cyber operations. The Government has also prioritised REDSPICE funding to enhance ASD’s signals 
intelligence and cyber capabilities.
This report highlights the importance of strong partnerships between the public and private sectors in 
defending Australians from cyber threats and making our country a harder target. It also reflects the 
concrete steps we are taking to deter cybercriminals and hold them to account, with the Government 
having used for the first time Australia’s autonomous cyber sanctions framework to impose cyber sanctions 
on Russian cybercriminals.  
Informed by ASD’s intelligence insights and partnerships, this report reinforces the importance of enhancing 
our nation’s cyber defences and the need for all Australians to play their part in protecting our collective 
cyber security. Reporting cybercrime, incidents and vulnerabilities remains a critical part of building a 
national threat picture and enabling us to effectively counter malicious cyber actors.
This report is a key part of the Government’s efforts to raise the profile of Australia’s cyber threats to ensure 
we can respond effectively to keep Australians safe. 
The Hon Richard Marles MP
Deputy Prime Minister and Minister for Defence
vi
Australian Signals Directorate
Annual Cyber Threat Report 2023–24
vii

## Contents
About ASD’s ACSC.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii
About the contributors.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . viii
Executive summary.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
Year in review.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
State actors. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
Critical infrastructure.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
Cybercrime. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
Hacktivism. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
Resilience. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
ASD programs.. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59

## About ASD’s ACSC
The Australian Signals Directorate’s Australian Cyber Security Centre (ASD’s ACSC) is the Australian 
Government’s technical authority on cyber security. Through the ACSC, ASD brings together capabilities to 
improve Australia’s national cyber resilience. Its services include:
	
- providing the Australian Cyber Security Hotline, which is contactable 24 hours a day, 7 days a week, 
via 1300 CYBER1 (1300 292 371)
	
- providing technical advice and publishing alerts, advisories and notifications on significant cyber 
security threats
	
- monitoring cyber threats and sharing intelligence with partners, including through the Cyber Threat 
Intelligence Sharing platform (CTIS)
	
- helping Australian organisations respond to cyber security incidents
	
- providing exercises and uplift activities designed to enhance the cyber security resilience of 
Australian organisations
	
- supporting collaboration between over 119,300 Australian organisations and individuals on cyber 
security issues through ASD’s Cyber Security Partnership Program.
Collaboration and partnerships are key to effective cyber security. ASD thanks all of the organisations that 
contributed to this report, including federal, state and territory government agencies, industry partners, and 
all who reported cyber security matters to ASD.

## About the contributors
Australian Federal Police
The Australian Federal Police (AFP) is 
responsible for enforcing Commonwealth 
criminal law; contributing to combatting 
complex transnational, serious, and organised 
crime that impacts Australia’s national 
security; and protecting Commonwealth 
interests from criminal activity in Australia 
and overseas. Operation Aquila leverages 
the complementary powers, capabilities 
and intelligence of ASD and the AFP to 
disrupt the most serious cybercrime threats 
facing Australia. The AFP-led Joint Policing 
Cybercrime Coordination Centre (JPC3) brings 
together Australian law enforcement and key 
industry and international partners to fight 
high-volume, high-harm cybercrime and 
prevent harm and financial loss to the 
Australian community. 
Australian Institute 
of Criminology
The Australian Institute of Criminology 
(AIC) is Australia’s national research and 
knowledge centre on crime and justice. The 
AIC informs crime and justice policy and 
practice in Australia by undertaking, funding 
and disseminating policy-relevant research of 
national significance.
Australian Security 
Intelligence Organisation
The Australian Security Intelligence 
Organisation (ASIO) is Australia’s security 
intelligence service. It protects Australia and 
Australians from threats to their security, 
including terrorism, espionage, sabotage, and 
interference in Australia’s affairs by foreign 
governments. ASIO’s cyber program is focused 
on investigating and assessing the threat to 
Australia from malicious state-sponsored 
cyber activity. ASIO’s contribution to ASD 
includes intelligence collection, investigations 
and intelligence-led outreach to business and 
government partners.
ix

Department of Foreign 
Affairs and Trade
The Department of Foreign Affairs and Trade 
(DFAT) promotes and protects Australia’s 
international interests to support our security 
and prosperity. DFAT leads Australia’s 
international engagement on cyber and 
critical technology across the Australian 
government. This work is coordinated by 
Australia’s Ambassador for Cyber Affairs and 
Critical Technology. DFAT is leading on the 
international elements of the 2023-2030 Cyber 
Security Strategy, the development of which 
is being coordinated by the Department of 
Home Affairs.
Department of Home 
Affairs
The Department of Home Affairs is responsible 
for central coordination, strategy and policy 
leadership of cyber and critical infrastructure 
resilience and security, immigration, border 
security, national security and resilience, 
counter-terrorism, and citizenship. The 
Department of Home Affairs leads the 
development of cyber security policy, 
including the implementation of the 
2023–2030 Australian Cyber Security Strategy.
National Cyber Security 
Coordinator
The National Cyber Security Coordinator, 
supported by the National Office of Cyber 
Security (NOCS), leads the coordination of 
national cyber security policy, responses to 
major cyber incidents, whole-of-government 
cyber incident preparedness efforts and 
the strengthening of Commonwealth cyber 
security capability. The Coordinator also 
oversees the implementation of the 2023–2030 
Australian Cyber Security Strategy. 
Australian Competition 
and Consumer 
Commission
The National Anti-Scam Centre, run by 
the ACCC, brings together experts from 
government, law enforcement and the 
private sector to disrupt scams before they 
reach consumers. The National AntiScam 
Centre is collectively committed to making 
Australia a harder target for scammers 
and reducing the financial and emotional 
harm caused by scams. The Centre does 
this through collaboration (technology and 
intelligence sharing), disruption, awareness 
and protection.
Defence Intelligence 
Organisation 
The Defence Intelligence Organisation 
co-leads the Cyber Threat Assessment 
team in partnership with ASD to provide 
the Australian Government with an 
all-source strategic, cyber threat intelligence 
assessment capability.
Office of the 
Australian Information 
Commissioner
The Office of the Australian Information 
Commissioner (OAIC) regulates the 
compliance of Australian government 
agencies, organisations with an annual 
turnover of more than $3 million and the 
compliance of some other organisations 
with the Privacy Act 1988 and other laws when 
handling personal information. 
Reserve Bank of Australia
The Reserve Bank of Australia is Australia’s 
central bank. Its duty is to serve the Australian 
people and contribute to their economic 
prosperity and welfare through sustainment 
of full employment and maintenance of price 
stability. It issues the nation’s banknotes and 
operates the core of the payments system.

## Executive summary
Australia faces the most complex and challenging strategic environment since the Second World War. These 
strategic challenges extend to the cyber threat landscape. While advancements in critical and emerging 
technologies offer significant social and economic benefits, they also improve the capabilities of malicious 
cyber actors who continue to target Australia’s networks.
In FY2023–24, ASD received over 36,700 calls to its Australian Cyber Security Hotline, an increase of 12% 
from the previous financial year. ASD also responded to over 1,100 cyber security incidents, highlighting the 
continued exploitation of Australian systems and ongoing threat to our critical networks.
State-sponsored cyber actors persistently target Australian governments, critical infrastructure and 
businesses using evolving tradecraft. These actors conduct cyber operations in pursuit of state goals, 
including for espionage, in exerting malign influence, interference and coercion, and in seeking to pre-position 
on networks for disruptive cyber attacks.
Over the past year, ASD co-sealed several joint advisories with international partners to highlight the 
evolving operations of state-sponsored cyber actors. In February 2024, ASD joined the US and other 
international partners in releasing an advisory that assessed the People’s Republic of China (PRC) is 
leveraging living off the land techniques that abuse native tools and processes on systems. The PRC’s choice 
of targets and pattern of behaviour is consistent with pre-positioning for disruptive effects rather than 
traditional cyber espionage operations.
Russia is also adapting its techniques, including for the exploitation of cloud platforms. The evolution of 
this tradecraft means that network defenders must prioritise and invest in cyber security skills, resources 
and teams.
Critical infrastructure networks are an attractive target due to the sensitive data they hold and the 
widespread disruption that a cyber security incident can cause on those networks. In FY2023–24, over 11% of 
cyber security incidents ASD responded to related to critical infrastructure. Compromise could lead to the 
disruption of critical services, affecting the economy and lives of everyday Australians.
Cybercrime is a persistent and disruptive threat. Cybercriminals are adapting to capitalise on new 
opportunities, such as artificial intelligence, which reduces the level of sophistication needed for cybercriminals 
to operate. In FY2023–24, business email compromise and fraud were among the top self-reported 
cybercrimes for businesses and individuals in Australia. Ransomware and data theft extortion also remained a 
pervasive and costly threat.
In response to this threat, ASD has worked across government, with industry and international partners 
to successfully pursue cybercriminals targeting Australia. During FY2023–24, the Australian Government 
for the first time used Australia’s autonomous cyber sanctions framework to sanction two Russian 
citizens for their roles in cybercrime activities. These sanctions are a key tool in deterring cybercrime and 
protecting Australians.   
2

Strong partnerships are critical to building cyber resilience and making Australia a harder target. ASD 
continues to monitor and adapt to the threat environment, and collaborates on a national scale to protect 
Australians. An increasing number of industry and government partners are choosing to participate in 
ASD programs, which provide a platform to share threat intelligence and expertise. This includes the ASD-
Microsoft initiative to connect ASD’s Cyber Threat Intelligence Sharing platform with Microsoft’s Sentinel 
platform. These types of collaborations are improving the speed and scale of information-sharing between 
and among government agencies and industry partners. 
In FY2023–24, ASD notified entities more than 930 times of potential malicious activity on their networks. A 
robust partnership between government and industry underpins our ability to effectively defend the nation 
against malicious cyber activity.
Cyber security is not set-and-forget. Organisations should consider replacing unsupported information and 
communications technology (ICT) systems with secure-by-design products, consider cyber security when 
implementing new technologies and follow ASD’s best-practice cyber security advice, such as the Essential 
Eight. Regularly updating and applying ICT best practice builds resilience now and into the future.
Be ready to respond. Critical infrastructure organisations should adopt a stance of ‘when’ not ‘if’ a cyber 
security incident will occur. All organisations should have a cyber security incident response plan and test it 
regularly to ensure an effective response and fast recovery. To develop and implement a response plan, an 
organisation needs to know its systems and where its most valuable data is stored.
ASD encourages every organisation and individual who observes suspicious cyber activity, incidents and 
vulnerabilities to report to ReportCyber at cyber.gov.au, and to the Australian Cyber Security Hotline 1300 
CYBER1 (1300 292 371). ASD provides free technical incident response advice and assistance, 24 hours a day, 
7 days a week.

## Year in review
YEAR IN REVIEW
What ASD saw
Answered over 36,700 calls to the Australian Cyber Security 
Hotline, up 12%
	
- on average, 100 calls per day, an increase from 
90 calls per day
Average self-reported cost of cybercrime per report 
for individuals, up 17% ($30,700) 
Average self-reported cost of cybercrime per report for 
businesses, down 8% overall
	
- small business: $49,600 (up 8%)
	
- medium business: $62,800 (down 35%)
	
- large business: $63,600 (down 11%)
Received over 87,400 cybercrime reports, 
down 7%
	
- on average a report every 6 minutes,
 consistent with last year
Top 3 self-reported cybercrime types for individuals
	
- identity fraud (26%)
	
- online shopping fraud (15%)
	
- online banking fraud (12%)
Top 3 self-reported cybercrime types for business
	
- email compromise (20%)
	
- online banking fraud (13%)
	
- business email compromise fraud (13%)
Publicly reported common vulnerabilities and exposures 
increased 31%
11% of all incidents 
responded to included ransomware, 
a 3% increase from last year
YEAR IN REVIEW
What ASD did
Responded to over 
1,100 cyber security incidents, 
similar to last year
Australian Protective Domain Name System 
blocked customer access to 82 million malicious domains, 
up 21%
Domain Takedown Service 
has requested the removal of over 189,000 
malicious domains targeting Australian servers,
up 49%
Notified entities 930 times of 
potential malicious cyber activity
Cyber Threat Intelligence Sharing partners 
grew by 66% to over 400 partners
	
- shared over 1,372,400 indicators of compromise
Cyber Hygiene Improvement Program
	
- performed 365 high-priority operational taskings, 
up 250%
	
- distributed around 6,400 reports 
to approximately 2,000 organisations,
up 32% and 48% respectively
Cyber Uplift Remediation Program 
	
- 24 active engagements
	
- 17 engagements commenced
Cyber Maturity Measurement Program 
	
- 16 active engagements
YEAR IN REVIEW
What ASD did
Critical Infrastructure Uplift Program
	
- 10 uplifts completed covering 15 CI assets 
	
- 5 uplifts in progress 
	
- 17 uplift information packs sent
	
- 42 uplift workshops held
Notified critical infrastructure organisations 
over 90 times of potential malicious cyber activity
Published or updated 29 PROTECT publications, 
updated the Information Security Manual 
quarterly, and updated the Essential Eight 
Maturity Model
Published 19 joint advisories and publications 
with international partners to cyber.gov.au 
Published 118 alerts, advisories, 
incident and insight reports 
on cyber.gov.au and the Partnership Portal
ASD’s Cyber Security Partnership Program 
grew to around 119,300 partners
Led 16 cyber security exercises 
involving over 130 organisations 
to strengthen Australia’s cyber resilience
Briefed board members 
and company directors covering 
37% of the ASX200
YEAR IN REVIEW
Sustained disruption of essential 
systems and associated services
C6
C5
C4
C3
C1
C1
Extensive compromise
C6
6
C5
20
C4
15
C3
1
C2
C1
Isolated compromise
1
C6
57
C5
93
C5
75
C3
46
C3
C2
Coordinated low-level 

malicious attack
C6
1
C6
6
C5
6
C4
7
C3
3
C3
Low-level malicious attack
1
C6
81
C6
53
C5
60
C4
95
C4
11
C3
Unsuccessful low-level 

malicious attack
C6
13
C6
20
C6
70
C6
360
C6
28
C6
Member(s) of 
the public
Small 
organisation(s)
Sole traders
Medium-sized 
organisation(s)
Schools
Local 
government
State 
government
Academia/R&D
Large 
organisation(s)
Supply chain
Federal 
government
Government 
shared services
Regulated 
critical 
infrastructure
National security
Systems of 
National 
Significance
![Figure 1: Cyber security incidents by severity category for FY2023–24 (total 1,129)]
ASD categorises each cyber security incident it responds to on a scale of Category 1 (C1), the most severe, 
to Category 6 (C6), the least severe. Cyber security incidents are categorised on severity of impact and 
significance of the organisation’s impact to Australia.
In FY2023–24, there was a slight decrease in the number of extensive compromises, while the number of 
unsuccessful low-level malicious attacks increased by 10% compared with FY2022–23. There was also a 39% 
increase in isolated compromises this financial year.  
Coordinated low-level malicious cyber attacks fell by 77%, however this largely reflects a spike in incidents 
in FY2022–23 following a specific hacktivist campaign. It does not necessarily imply that the threat of 
coordinated low-level malicious cyber activity has diminished. 
Incidents categorised as C3 or above involve organisations such as federal and state governments, 
large organisations, academia, and supply chains. The frequency of C3 or above incidents in FY2023–24 
was consistent with FY2022–23, with 14% of all incidents being categorised C3 or above. While ASD 
only responded to one C2 incident, down from 5 in FY2022–23, the nature of the incident highlights the 
importance of ensuring systems are updated – the C2 was through the exploitation of a known vulnerability 
targeting a legacy, unpatched test server. 
Over a quarter (26%) of all C3 incidents were discovered as a result of a tipper, where ASD proactively 
notified the affected organisation of suspicious activity. The most common malicious activity leading to 30% 
of C3 incidents was the exploitation of public facing applications.
C3 incidents commonly involved compromised accounts or credentials (23%), malware infection other 
than ransomware (19%) and compromised assets, networks or infrastructure (18%). This contrasts with C3 
incidents in FY2022–23, where assets, networks or infrastructure were more frequently compromised than 
accounts or credentials. This suggests that malicious actors will adapt their methods to gain access.
10

ASD responded to over 1,100 cyber security incidents, around the 
same as in the last financial year.
100
76
90
111
106
70
109
105
104
88
85
85
June
May
April
March
February
January
December
November
October
September
August
July
![Figure 2: Cyber security incidents by month]
The top 5 reporting 
sectors are consistent 
with FY2022–23.
ASD categorises sectors following 
the Australian and New Zealand 
Standard Industrial Classification 
Divisions from the Australian 
Bureau of Statistics. The public 
safety and administration 
division encompasses several 
sectors, including federal, state, 
territory and local governments, 
public order and safety services, 
and defence.
37%
12%
6%
5%
5%
5%
5%
4%
4%
3%
Retail trade
Transport, postal 
and warehousing
Financial and
insurance services
Information media and 
telecommunications
Electricity, gas, water and 
waste water services
Professional, scientiﬁc, 
and technical services
Educational 
and Training
Healthcare and 
social assistance
State and local 
government
Federal government 
![Figure 3: Top 10 reporting sectors]
Compared to FY2022–23, healthcare and social assistance rose to be the most frequently reported 
non-government sector.
Government sectors and regulated critical infrastructure have additional reporting obligations, which may 
explain the relatively high reporting rate for these sectors compared with others.
	
- The number of extortion-related cyber security incidents responded to by ASD increased by 9% 
compared to the last financial year.
	
- Around 71% of these incidents involved ransomware.
	
- In FY2023–24, ASD responded to 53 incidents involving Denial of Service (DoS) or Distributed Denial of 
Service (DDoS) attacks, a decrease of 15% on the last financial year.
11
Australian Signals Directorate
Annual Cyber Threat Report 2023–24
Reported top 3
Cyber security  
incident types
Mitigations
Top 3 reported 
cyber security 
incident types 
for critical 
infrastructure




Compromised 
account or 
credentials
32%
	
- Use phishing-resistant multi-factor authentication (MFA) 
where possible
	
- Analyse event logs from workstations in a timely manner 
to detect cyber security events
	
- Find and remove inactive user and service accounts
	
- Enforce the principle of least privilege
Malware infection 
(other than 
ransomware)
17%
	
- Use antivirus software and endpoint detection and 
response software
	
- Keep your devices up to date
	
- Implement application control
	
- Maintain backups of critical data applications and 
settings. Regularly test that you can restore from backups 
in a timely manner
Compromised 
asset, network or 
infrastructure
12%
	
- Use network segmentation and segregation
	
- Apply ASD’s industrial control systems remote access protocol
	
- Define a process for introducing software and patches 
into the industrial control system
	
- Ensure sufficient logging is enabled and monitor for 
key indicators
	
- Ensure logs are stored securely
Cyber security  
incident types
Mitigations
Top 3 reported 
cyber security 
incident types 
for government 
(federal, state and 
local) 



Compromised 
account or 
credentials
30%
	
- Use phishing-resistant MFA where possible
	
- Use a password management solution to store 
passwords securely
	
- Ensure event logs from authentication services and 
workstations are analysed within a timely manner to 
detect cyber security events
Malware infection 
(other than 
ransomware)
20%
	
- Mitigate known vulnerabilities (e.g. applying patches in a 
timely manner)
	
- Implement access control and application control
	
- Use antivirus software and endpoint detection and 
response software
	
- Maintain backups of critical data applications and 
settings. Regularly test that you can restore from backups 
in a timely manner
Compromised 
asset, network or 
infrastructure
20%
	
- Use system and application hardening
	
- Adopt a Secure-by-Design approach
	
- Apply network access controls
	
- Ensure logging is enabled and monitor for key indicators
12

Self-reported 
cybercrime types
Mitigations
Top 3 self-reported 
cybercrime 
threats for 
business (S,M,L)



Email compromise 
resulting in no 
financial loss
20%
	
- Train staff to recognise phishing which is commonly used 
to compromise accounts
	
- Require MFA and strong, unique passwords for business 
email accounts
	
- Use email content filtering
Online banking 
fraud
13%
	
- Be aware of suspicious changes to banking details or 
payment requests
	
- Be aware of changes to email addresses – such as if the 
domain name does not match the supplier’s company 
name or differs from previous correspondence
	
- Be aware of unsolicited SMS messages from financial 
providers – including messages that ask for a password, 
an MFA code, or to click on a link
Business email 
compromise (BEC) 
fraud resulting in 
financial loss
13%
	
- Increase cyber security awareness training for staff
	
- Use MFA for identity confirmation
	
- Protect domain names – renew domain names on 
schedule and register additional domain names
Self-reported 
cybercrime types
Mitigations
Top 3 self-reported 
cybercrime threats 
for individuals




Identity fraud
26%
	
- Use MFA and secure passphrases
	
- Keep your devices up to date and use antivirus software
	
- Limit the personally identifiable information you 
share online
Online shopping 
fraud 
15%
	
- Use MFA and secure passphrases
	
- Keep your devices up to date and use antivirus software
	
- Limit the personally identifiable information you 
share online
Online banking 
fraud
12%
	
- Use MFA through your financial providers
	
- Be aware of suspicious changes to banking details or 
payment requests
	
- Be aware of changes to email addresses – such as if the 
domain name does not match the supplier’s company 
name or differs from previous correspondence
	
- Be aware of unsolicited SMS messages from financial 
providers – including messages that ask for a password, 
an MFA code, or to click on a link
![Figure 4: Most common reported threats and key steps to improving cyber security]
Note: Incidents can have multiple incident types. 
For best-practice cyber security mitigation advice, including ASD’s Essential Eight, visit cyber.gov.au.

## State actors
	
- The threat of state-sponsored cyber operations is persistent and will likely grow as strategic 
competition in the Indo-Pacific increases.
	
- State-sponsored cyber actors will continue targeting Australian governments, critical infrastructure, 
and businesses, as well as connected systems and their supply chains, for espionage and 
information-gathering purposes. These actors will continue to adapt their techniques, using both 
publicly available and bespoke tools to achieve their objectives.
	
- In February 2024, ASD joined other Five Eyes partners in a US-led advisory, which assessed that the 
People’s Republic of China state-sponsored cyber actors are seeking to pre-position themselves 
on information and communications technology networks for disruptive cyber attacks against 
US critical infrastructure in the event of a major crisis or conflict. Australian critical infrastructure 
networks could be vulnerable to similar state-sponsored malicious cyber activity as seen in the US. 
	
- ASD’s Cyber Security Partnership Program and the Cyber Threat Intelligence Sharing platform 
support Australian organisations to combat state-based cyber threats.
14
State actors    // 
 
Global state-sponsored cyber activity 
increases as tensions rise
Australia continues to face a complex set of strategic circumstances. Multiple