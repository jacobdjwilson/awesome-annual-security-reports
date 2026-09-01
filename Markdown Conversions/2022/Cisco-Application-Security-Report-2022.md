2022
Application
Security Report

INTRODUCTION
Business applications are increasingly under attack from advanced threats and malicious actors
that are looking to exploit software vulnerabilities. Organizations are trying to counter these threats
by utilizing various controls for securing applications, such as vulnerability scanning, anti-malware
software, penetration testing, and identity and access controls. To gain deeper insights into the state
of application security, Cybersecurity Insiders conducted an in-depth study in partnership with Cisco
in July 2022. The resulting report reveals the latest application security trends, how organizations
protect critical applications, and the tools and best practices cybersecurity professionals prioritize.
Key findings include:
• Cybersecurity professionals most frequently mention protection of data (44%) as their key
application security concern. This is followed by the challenge of keeping up with the rising
number of vulnerabilities (42%), threat and breach detection (38%), and securing cloud
apps (37%).
• Customer-facing web applications tops the list of applications introducing the highest
security risks (42%), followed by legacy apps (40%). Less frequently mentioned are mobile
apps (30%), desktop applications (28%), and internal-facing web apps (26%).
• About a third (36%) of cybersecurity professionals confirm encrypted traffic is a security
risk to their environment due to the inability to inspect all traffic and detect threats quickly
before they can cause damage. Specifically, cyber professionals are most concerned
about hidden malware (63%), lack of visibility (58%), and data loss through exfiltration
(37%) as the main problems caused by encrypted traffic.
We would like to thank Cisco for supporting this important research.
We hope you enjoy this report.
Thank you,
Holger Schulze
Holger Schulze
CEO and Founder
Cybersecurity Insiders
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 2

SECURITY BARRIERS
Various barriers inhibit organizations from adequately defending against cyber threats and an
effective security posture. At the top of the list are two “people issues”: the perennial lack of skilled
personnel (39%) followed by low security awareness among employees (35%). Organizational
issues are also a contributing factor.
Which of the following barriers inhibit your organization from adequately defending
against cyberthreats?
|                        |     | 39%             |          | 35%                    |          | 35% |                    |     |
| ---------------------- | --- | --------------- | -------- | ---------------------- | -------- | --- | ------------------ | --- |
|                        |     | Lack of skilled |          | Low security awareness |          |     | Lack of            |     |
|                        |     | personnel       |          | among employees        |          |     | budget             |     |
|                        | 29% |                 | 26%      |                        | 22%      |     |                    | 21% |
| Lack of collaboration  |     |                 | Lack of  |                        | Too much |     | Poor integration/  |     |
between separate  management  data to analyze interoperability
|     | departments |     | support/  |     |     |     | between security  |           |
| --- | ----------- | --- | --------- | --- | --- | --- | ----------------- | --------- |
|     |             |     | awareness |     |     |     |                   | solutions |
Lack of investment in effective solutions 20%  |  Inability to prioritize vulnerabilities based on risk 20%  | Lack of contextual information from
security tools 13%  | Inability to justify additional investment 13%  | None 7%  | Not sure/other 10%
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved.     |   3

APPLICATION SECURITY CONCERNS
When asked about their biggest application security concerns, cybersecurity professionals most
frequently mentioned protecting data (44%) as their key concern. This is followed by the challenge
of keeping up with the rising number of vulnerabilities (42%), threat and breach detection (38%), and
securing cloud apps (37%).
What are your biggest application security concerns?
44% Protecting
data
42% Keeping up with the rising
number of vulnerabilities
38% Threat detection/
breach detection
37% Securing
cloud apps
37% Securing applications
we develop
Effective threat modeling 27% | Effectively prioritizing and remediating vulnerabilities that pose the most risk 26% | Meeting regulatory/
compliance requirements 26% | Securing mobile apps 26% | Securing business apps (ERP, etc.) 23% | Meeting customers’ security needs
and requirements 21% | Securing open source software 20% | Securing embedded/IoT hardware 17% | Securing commercial off-the-shelf
software 16% | Securing Blockchain 6% | Don’t know/other 6%
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 4

RISKIEST APPLICATIONS
So, which types of applications present the highest security risks? Customer-facing web applications
tops the list (42%), followed by legacy applications (40%). Less frequently mentioned are mobile
applications (30%), desktop applications (28%), and internal-facing web applications (26%).
Which types of applications present the highest security risk to your business?
Customer-facing
42%
web applications
Legacy applications 40%
30%
Mobile applications
Desktop (client) 28%
applications
Internal-facing 26%
web applications
Business applications
26%
(ERP, SCM, MES, HR SRM, etc.)
Embedded/IoT
17%
software and firmware
Embedded/IoT software and firmware 17% | Securing Blockchain applications 7% | Don’t know/unsure/other 12%
Securing blockchain 7%
applications
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 5

LAST BREACH
Forty-four percent of surveyed organizations have experienced application breaches or compromises
in the past, and of those, 20% have been attacked just within the last year. The alarming news is
that nearly one third of survey participants (32%) are not sure if they have experienced a security
attack against applications. If you can’t see it then you can’t protect against it.
When was the last time that one of your company’s applications was breached/
compromised?
Within the last 5 years 18%
44%
Within the last year 15%
of organizations
confirmed they
More than 5 years ago 6% experienced application
breaches or compromises
in the past
Within the last month 5%
24%
Never
32%
Don’t know/unsure
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 6

ATTACKS AGAINST APPS
Recent years have seen rapid growth in volume and sophistication of attacks, and the survey
answers reflect this trend. Not surprisingly, malware remains the most common attack vector
against applications (31%), followed by distributed denial-of-service attacks (23%) and application
misconfiguration (21%). Other common types of attacks include stolen credentials (20%), exploits
of software vulnerabilities (18%), and brute force attacks (17%).
Which of the following security attacks against applications has your organization
experienced over the past 12 months?
21% 20%
Application Stolen
misconfiguration credentials
18%
23%
Software
DDoS vulnerability
exploit
17%
31%
Brute force
Malware
Cross-site scripting 16% | Unpatched library 15% | Information leakage 15% | Web fraud 14% | SQL injection 13% | Content spoofing
10% | Clickjacking 7% | Cross-site registry 7% | MitM/MitB 4% | Other 6%
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 7

WHERE THE APPS ARE
Despite rapid adoption of cloud computing in the last years, most business applications are still
hosted on-premises (51%), followed by hybrid cloud environments (19%), private clouds (16%) and
public clouds (13%).
Where are the majority of your applications hosted?
51%
On-premises/
datacenter
19%
Hybrid
cloud
16%
Private
cloud
13%
Public cloud
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 8

APPLICATION MONITORING
How are organizations monitoring their apps for security issues? About half of organizations (49%)
are actively monitoring applications in production to collect and respond to threat intelligence.
They’re using a variety of methods to monitor security issues, with Web Application Firewalls (WAF)
being one of the primary solutions (45%).
How are you currently monitoring applications for security issues?
We actively monitor
applications running in 49%
production to collect and
respond to threat intelligence
We use firewalls to
45%
protect our applications
We have a feedback loop to share
incidents and identified vulnerability
29%
information back to our
development and design teams
We use code signing in the
23%
deployment of our applications
None of the above 10% | We use endpoint security to protect our applications 5% | We use the embedded security provided by our cloud
provider 3% | We use a workload security product to protect our applications 1% | Don’t know/unsure/other 17%
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 9

ENCRYPTED TRAFFIC RISKS
About a third (36%) of cybersecurity professionals confirm encrypted traffic is a security risk to
their environment due to the inability to inspect all traffic and detect threats quickly before they
can cause damage. Specifically, cyber professionals are most concerned about hidden malware
(63%), lack of visibility (58%), and data loss through exfiltration (37%) as the main risks amplified
by encrypted traffic.
Do you view encrypted traffic as a security risk in your environment?
36% 52%
36% 52%
Yes No
Yes No
1122%%
UnUsnusruere
If yes, what problems does encrypted traffic cause?
Hidden malware 63%
Hidden malware 63%
Lack of visibility 58%
Lack of visibility 58%
37%
Data loss through exfiltration
37%
Data loss through exfiltration 32%
Cannot apply security controls
32%
Cannot apply security controls
Other 5%
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 10

HANDLING ENCRYPTED TRAFFIC
How do organizations handle the challenges created by encrypted network traffic? A third of
organizations (34%) don’t have a good solution for encrypted traffic while 21% selectively decrypt
some traffic.
How do you deal with encrypted traffic in your environment?
21%
34%
Selectively decrypt
some traffic We don't have a good
solution for this
Cannot decrypt
due to compliance 8%
mandates 8% Decrypt
everything
Unsure 25% | Other 4%
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 11

APPLICATION VULNERABILITIES
Only half of organizations (50%) agree they have sufficient resources to detect and remediate
vulnerabilities in a timely manner. That leaves the other half without the necessary funds and staff
to address application security issues quickly.
My organization has ample resources to detect and remediate vulnerabilities in
applications in a timely manner
50%
organizations are lacking
sufficient resources to
detect and remediate application
vulnerabilities quickly
26% 40%
20%
10%
4%
Strongly disagree Strongly agree
Strongly disagree Disagree Neutral/not sure Agree Strongly agree
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 12

APPSEC BUDGETS ON THE RISE
For most organizations (51%), budgets dedicated to application security are increasing over the
next 12 months. Only 15% expect a decline.
How is the budget for securing your applications changing over the next 12 months?
34% 51%
Stay 3the4 sa%me 51Inc%rease
Stay the same Increase
15%
15%
Decrease
Decrease
If the budget for securing your application will increase, indicate by how much.
15% 41% 20% 9% 15%
15% 41% 20% 9% 15%
1-51%-5% 66--1100%% 11-1115-%15% 16-2160-%20% >20%>20%
2022 APPLICATION SECURITY REPORT Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. | 13

|     |     | 25% |     |     | 17% |     | 8%  | 6%  | 5%5% |     | 34% |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
Technology, Software & Internet           Financial Services          Healthcare, Pharmaceuticals & Biotech
Computers & Electronics              Government           Professional Services             Other
DEMOGRAPHICS
The 2022 Application Security Report is based on the results of a comprehensive online global
survey of 386 cybersecurity professionals, conducted in July 2022, to gain deep insight into the
|     |     |     | Consultant |     |     |     |     | 20% |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
latest trends, key challenges, and solutions for application security. T1he6 %respondents range from
|     | Manager/Supervisor |     |     |     |     |     |     | 19% |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IT Operations
technical executives to managers and IT security practitioners, representing a balanced cross-
|     |     |     | Specialist |     |     |     |     | 18% |     |     |     |     |     |     |
| --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
section of organizations of varying sizes across multiple industries.
8%
| CTO, CIO, CISO, CMO, CFO, COO |     |     |     |     |     |     | 14% |     |     | Engineering |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
48%
|     | What is yDoiurerc toorrganization’1s 0in%dustry?  |     |     |     |     |     |     |     |     |     | 5%  |     |     |     |
| --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IT Security
Product Management
4%
Vice President
4%
|     |     |                    |     |     | 3%  |     |     |     |       | Co mpliance |     |     |     |     |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | ----- | ----------- | --- | --- | --- | --- |
|     |     | Project2 M5an%ager |     |     |     | 17% |     |     | 8% 6% | 5%5 %       |     |     | 34% |     |
4%
|     | Owner/CEO/President |     |     |     | 3%  |     |     |     |     |     |     |     |     |     |
| --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Operations
15%
Technology ,  S o ftware & Intern9e%t           Financial Services          Healthcare, PharmaceuticOatlhse &r Biotech
|     |     |     | O   | t he r |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Computers & Electronics              Government           Professional Services             Other
What is your company size?
|     |           |     | Consultant |     |        |         |     |                   | 20% |           |     |     |     |     |
| --- | --------- | --- | ---------- | --- | ------ | ------- | --- | ----------------- | --- | --------- | --- | --- | --- | --- |
|     | 10%2255%% |     |            | 20% | 1177%% | 16%88%% |     | 686%%%55%%515%5%% |     | 8% 3344%% |     | 23% |     |     |
16%
|     |     | Manager/Supervisor |     |     |     |     |     |     | 19% |     |     |     |     |     |
| --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
IT Operations
Fewer than 10         10–99          100–499         500-999          1,000–4,999         5,000–10,000         Over 10,000
TTeecchhnnoolologgy,y ,S Sooftfwtwaarere & & I nInteternrneet t                    F Fininaanncciaial lS Seervrviciceess                   H Heeaaltlhthccaarere, ,P Phhaarmrmaacceeuutitcicaalsls & & B Bioiotetecchh
CCoommppuutetersrs & & SE Elpelecectrctorionanicliicsss t                          G Goovveernrnmmeennt t                    P Prorofefessssioi1onna8al lS Se%ervrviciceess                         O Oththeerr
8%
| CTO, CIO, CISO, CMO, CFO, COO |     |     |     |     |     |     |     | 14% |     |     |     | Engineering |     |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
What department do you work in? What organizational level best  48%
|     |     |     |     | Director |     |     | 10% |     |     |     |     |     | 5%  |     |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
describes your current position?  IT Security
Product Management
|     |     |     | Vice President       |     |     | 4%  |     |        |     |     |     |     |     |     |
| --- | --- | --- | -------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
|     |     |     | CCoonnssuultlatanntt |     |     |     |     | 2200%% |     |     |     |     | 4%  |     |
1166%%
MMaannaPagrgeoer/jreS/Sucuptp eMervravisinsoorarger 3% Compliance
|     |     |     |     |     |     |     |     | 1199%% |     | ITIT O Oppeeraratitoionnss |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | -------------------------- | --- | --- | --- | --- |
4%
|     | Owner/CEO |     | SSp /pP eec | rci e aial s isliist dtent |     | 3%  | 1188%% |     |     |     |     |     |     |     |
| --- | --------- | --- | ----------- | -------------------------- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Operations
|     |     |     |     |     |     |     |     |     |     | 88%% |     |     |     | 15% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
CCTTOO, ,C CIOIO, ,C CISISOO, ,C CMMOO, ,C CFFOO, ,C COO OO 114 9 4%% % EEnngginineeeerirningg
|     |     |     |                  | O ther |     |        |     |     |     |      |     |     |     | Other  |
| --- | --- | --- | ---------------- | ------ | --- | ------ | --- | --- | --- | ---- | --- | --- | --- | ------ |
|     |     |     |                  |        |     | 1100%% |     |     |     |      |     |     |     | 4488%% |
|     |     |     | DDirierecctotorr |        |     |        |     |     |     | 55%% |     |     |     |        |
ITIT S Seeccuurirtiyty
PProrodduucct tM Maannaaggeemmeenntt
44%%
VVicicee P Preressidideenntt
44%%
|     |     |     |     |     | 33%% |     |     |     |     | CCoommpplialiannccee |     |     |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
PProrojejecct tM Maannaaggeerr
44%%
33%%
|     | OOwwnneer/rC/CEEOO/P/Preressidideenntt |     |     |     |     |     |     |     |     | OOppeeraratitoionnss |     |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
1155%%
|     |     |     |     |     |     | 99%% |     |     |     |     |     | OOththeerr |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | ---------- | --- | --- |
OOththeerr
|     |     | 1 0 | %   | 2   | 0 % |     |     | 16% | 8 % | 1 5 % |     | 8 % |     | 2 3 % |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | ----- |
2022 APPLIC A TI ON SECURITY  RE PO RT Copyri gh t © 2022  C yb ersecurity  Ins iders. All Rights R es er ved.     |   14
Fewer than 10         10–99          100–499         500-999          1,000–4,999         5,000–10,000         Over 10,000
|     |     | 1100%% |     | 2200%% |     | 1166%% |     | 88%% | 1155%% | 88%% | 2233%% |     |     |     |
| --- | --- | ------ | --- | ------ | --- | ------ | --- | ---- | ------ | ---- | ------ | --- | --- | --- |
FFeewweer rt hthaann 1 100                 1 100–9–999                   1 10000–4–49999                 5 50000--999999                   1 1,0,00000–4–4,9,99999                 5 5,0,00000–1–100,0,00000                 O Ovveer r1 100,0,00000

Cisco has long established itself as the worldwide leader in technology that powers the
internet, while building an open, integrated portfolio of cybersecurity solutions along the
way. We believe that security solutions should be designed to act as a team. They should
learn from each other. They should listen and respond as a coordinated unit. When that
happens, security becomes more systematic and effective. Our customers have trusted us
for years as both the world’s largest provider of IT infrastructure and networking services
and the world’s largest enterprise cybersecurity business.
Cisco Secure is built on the principle of better security, not more. It delivers a streamlined,
customer-centric approach to security that ensures it’s easy to deploy, manage, and use –
and that it all works together. We’re driven by the fact that people and our customers are at the
heart of what we do. We understand that customers want to cut through the complexity and
noise and feel confident in their security, focusing on outcomes. This requires simplification
without being simplistic. Our cloud-native platform is a giant leap forward in that.
We empower the security community with the reliability and confidence that they’re safe
from threats now and in the future with the Cisco SecureX platform. We help 100 percent
of the Fortune 100 companies secure work – wherever it happens – with the broadest, most
integrated platform. Learn more about how we simplify experiences, accelerate success,
and protect futures at cisco.com/go/secure.
Learn more about Cisco Secure

Cybersecurity Insiders is a 500,000+ member online community for
information security professionals, bringing together the best minds
dedicated to advancing cybersecurity and protecting organizations across
all industries, company sizes, and security roles.
We provide cybersecurity marketers with unique marketing opportunities to
reach this qualified audience and deliver fact-based, third-party validation
thought leadership content, demand-generation programs, and brand
visibility in the cybersecurity market.
For more information please visit
www.cybersecurity-insiders.com
Copyright © 2022 Cybersecurity Insiders. All Rights Reserved. Data can be reproduced
or referenced as long as it is sourced and linked to www.cybersecurity-insiders.com.

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-09-01", "model": "gemini-3.5-flash-lite"} -->
