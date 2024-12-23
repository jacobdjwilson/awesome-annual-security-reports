# Annual Threat Report 2024
## Table of Contents
- [Letter from the CEO](#letter-from-the-ceo)
- [Letter from the VP, Security Operations](#letter-from-the-vp-security-operations)
- [Contents](#contents)
- [Executive summary](#executive-summary)
- [2023 by the numbers](#2023-by-the-numbers)
- [Identity threats](#identity-threats)
- [Cloud platform threats](#cloud-platform-threats)
- [Computer-based threats](#computer-based-threats)
- [Phishing threats](#phishing-threats)
- [Annual spotlight](#annual-spotlight)
- [Looking ahead to 2024…](#looking-ahead-to-2024)
- [2023 at Expel](#2023-at-expel)
- [Reference highlights](#reference-highlights)

Annual
Threat Report 
2024
Cybersecurity insights, 
resilience recommendations, 
and predictions
i 
Annual Threat Report 2024
Expel’s operators do a massive amount of 
analysis, triage, and complicated problem- 
solving—stopping intricate attacks every  
single day. 
It’s our responsibility to take lessons learned from 
our varied customer base and share those insights 
with others in our community in the interest of 
banding together against our common adversaries.
For each of the top trends we explore, we’ll tell 
you what we saw, how to detect these threats 
and protect your organization, and what to watch 
for in 2024. We cap it off with some thoughts and 
predictions for cybersecurity this year, courtesy of 
our leadership team and some of the smartest folks 
in the industry (who also happen to be Expletives). 
We delve into the data to identify trends and patterns 
in the security events we’re seeing and translate 
them into strategic guidelines your organization 
can put into play right away. Whether it’s hardening 
your environment against specific known threats or 
improving measures to detect bad actors who find their 
way past the first lines of defense, we’re in this together 
and strong, collaborative information sharing is key.

## Letter from the CEO
Dave Merkel
CEO, Expel
“
We’re in this 
together 
and strong, 
collaborative 
information 
sharing  
is key.”
i  
Annual Threat Report 2024
ii  
Annual Threat Report 2024
ii 
Annual Threat Report 2024
Thanks for taking the time to review our  
Annual Threat Report. I know firsthand that the 
day of a cyber operator is a busy one and it’s 
not easy to find time to read and digest such an 
extensive report.
The challenges you face every day are complex, fast-moving and 
constantly evolving, so it’s our goal to provide a resource packed 
with intel that is both valuable and actionable for protecting 
your organization.
Much of the information included in this report originates from our 
technology stack, but it’s the experience and the expertise that 
our analysts bring to the fight which enables our SOC team to go 
beyond the technology and protect our customers. These people 
are the best in the business, and they work behind the scenes to 
keep our customers (and Expel) safe.
People are at the core of the work we do, and although a modern 
security strategy and the right technology are critical, without a 
high-performing SOC, security teams will lose more often than 
they win. Effective, modern SOC operations enable and empower 
analysts to make effective real-time decisions that protect the 
enterprises entrusted to them. We believe this passionately and it’s 
for this reason that we’re sharing this information and intelligence 
with you, the cybersecurity community.

## Letter from the VP, Security Operations
Daniel Clayton
VP, Security Operations
“
Effective, modern 
SOC operations 
enable and  
empower analysts 
to make effective 
real-time decisions 
that protect the 
enterprises  
entrusted to them.”
## Contents
Executive summary.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2023 by the numbers	�������������������������������������������������������6
Identity threats. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
Cloud platform threats.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
Computer-based threats	������������������������������������������������19
Phishing threats.
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .27
Annual spotlight	�������������������������������������������������������������30
Looking ahead to 2024…	�����������������������������������������������31
2023 at Expel	�����������������������������������������������������������������33
Reference highlights	������������������������������������������������������34
1  
Annual Threat Report 2024

## Executive summary
Key insights and takeaways
Now in its third installment, the trends, predictions, 
and recommendations discussed in this report 
are based primarily on incidents our security 
operations center (SOC) identified through 
investigations into alerts, email submissions, 
vulnerability disclosures, and threat-hunting leads 
spanning January 1 to December 31, 2023. We 
relied on a combination of time-series analyses, 
statistics, customer input, and analyst expertise to 
generate these insights.
To make it easy to follow along, we’ve broken 
this report into four different threat types: 
identity, cloud, computer-based, and phishing. 
Keep in mind, though, that these threats are 
tightly related. Compromise of user identities 
can occur through phishing and can impact an 
organization’s cloud assets and endpoints, or 
malicious activity on an endpoint may be indicative 
of an exploited vulnerability. We’ll highlight that 
interconnectivity throughout.
O U R  T O P  TA K E A W AY S :
Identity-based incidents dominate 
three years in a row
Identity threats accounted for 64% of all incidents our 
SOC investigated and increased in volume by 144% from 
2022. Of those incidents, 60% were unauthorized email 
logins and 40% were authentications to identity platforms, 
like Microsoft Entra ID (formerly Azure Active Directory), 
Okta, Ping, and Duo.
Of the organizations targeted with an identity attack:
 
 35% experienced more than one incident (up from 24% 
in 2022)
 
 Organizations saw an average of eight identity-based 
incidents over the year
 
 One nonprofit organization was targeted 255 times 
(up from 104 times in 2022 at the same organization)
Identity threats accounted for 64% of all 
incidents our SOC investigated and increased 
in volume by 144% from 2022.
Sixty-nine percent of identity-based incidents involved 
malicious logins from suspicious infrastructure, which are 
hosting providers or proxies that aren’t expected for a user or 
organization. We’ve noted in past years a shift toward using 
more proxies, VPNs, and hosting providers to bypass network 
zone and conditional access policies, and we expect we’ll 
continue to see this trend until organizations consistently 
put effective roadblocks in place—such as phish-resistant 
multifactor authentication (MFA) and policies to block 
suspicious logins.
Phishing-as-a-service (PhaaS) drives 
identity-based incidents
The increased volume of identity incidents noted above 
is a direct result of more phishing platforms becoming 
available on the dark market. Several of these harvesters 
can both pre-fill the intended victim’s email address and 
load the appropriate branding and background for the 
target organization’s login page, making these pages look 
convincingly like the expected login page.
It’s not surprising to see another branch of cybercrime-as-a-
service (CaaS) gain traction—it’s accessible, convenient, and 
available with a low barrier to entry. Unfortunately, that means 
it’s not going away anytime soon and we’re only likely to see 
this attack vector grow in 2024.
2  
Annual Threat Report 2024
The rise of QR code phishing
The recent uptick in QR code phishing—or qishing—is 
cause for concern because it takes the activity off endpoints 
and puts it on mobile devices, which may not be managed 
with tight security controls—allowing the attacker to 
bypass endpoint security. We found that Microsoft’s threat 
intelligence can reliably identify phishing pages created 
with PhaaS platforms. However, Microsoft’s effectiveness in 
identifying these pages may have inadvertently contributed 
to an increase in threat actors’ use of QR codes for phishing.
Personal devices typically lack the same level 
of protection as endpoint devices, meaning 
threat actors may be able to bypass the usual 
security barriers more easily.
Personal devices typically lack the same level of protection 
as endpoint devices, meaning threat actors may be able to 
bypass the usual security barriers more easily. It’s pivotal 
users become as wary of unexpected QR codes as they are 
URLs (or at least, as they should be).
Threat groups favor social engineering 
tactics to mimic employees and 
target organizations
“The Com,” a hacking group including the actors tracked as 
“Scattered Spider,” was responsible for the largest number 
of targeted identity attacks our SOC investigated this year. 
These attackers primarily targeted Okta and Microsoft 
accounts, attempting to abuse password reset mechanisms 
and MFA push fatigue to gain access.
We observed two main attack tactics:
 
 Calling into an organization’s helpdesk
 
 Abusing self-service password reset mechanisms
When calling into the helpdesk, the actors impersonate 
staff and request that their passwords be reset. If either the 
helpdesk or self-service password request attempts are 
successful, the threat actor sends MFA pushes to the real 
user. If the user accepts the MFA push, the attacker gains 
access to the account.
Attackers spend a stunning amount of time conducting 
thorough research on possible victims to mimic their speech 
patterns. Of note, “The Com” primarily targeted customers in 
the financial services industry in the second half of the year. 
We expect this attack style to continue into 2024, especially 
as generative AI has the potential to make this kind of 
impersonation even easier.
Cloud infrastructure incidents trend up, 
with stolen or leaked cloud credentials 
(aka secret) exposure as the biggest 
and most frequent risk
This year, we noted a 72% increase in cloud infrastructure 
incidents, roughly consistent with what we saw in 2022 and 
continuing the upward trend since we began supporting 
Amazon Web Services (AWS), Google Cloud Platform (GCP), 
Microsoft Azure, and Kubernetes. Exposed credentials (or 
secrets) were the leading root cause of cloud infrastructure 
incidents (42%). Publicly exposed or stolen credentials 
allow attackers to maintain persistent access to the cloud 
environment with the permissions tied to that identity or role.
Common misconfiguration of Amazon 
Cognito (aka AWS Cognito) allows 
attackers to gain direct access to AWS 
control plane
Amazon Cognito (also known as AWS Cognito) enables 
user sign-up and authentication to apps, but administrators 
frequently misconfigure the service. In these cases, an 
attacker can do things like create new accounts with 
excessive permissions or even access AWS credentials 
associated with the Cognito Identity Pool.
This year, security researchers released a few Amazon 
Cognito auditing tools. While these help operators identify 
misconfiguration, threat actors can also take advantage: 
we’re seeing more of these AWS Cognito focused 
attacks seemingly enabled by the auditing tools. But the 
misconfigurations that lead to these attacks are common—
and thus, effective—for a reason. We wrote more about what 
to know and understand about Amazon Cognito in this recent 
blog post.
3  
Annual Threat Report 2024
More than half of all malware 
incidents presented an immediate, 
significant risk
We separate malware into categories based on its 
functionality. In more than half the malware incidents, 
the malware deployed presented an immediate and 
significant risk to the environment (what we would classify 
as “high-risk”)—including risks of pre-ransomware activity 
or exfiltration. Pre-ransomware accounted for 57% of the 
malware incidents our SOC investigated.
In more than half the malware incidents, the 
malware deployed presented an immediate 
and significant risk to the environment.
The most frequent malware cases we classified as 
pre-ransomware included:
 
 Gootloader—17% of high-risk malware incidents
 
 Qakbot—12%
 
 SocGholish—11%
It’s worth noting that these were also the top pre-ransomware 
threats we reported in both 2021 and 2022. The skilled actors 
behind these threats have been active for a while; they’ll likely 
continue to be active for the foreseeable future.
Attackers trick users with sneaky 
infostealers downloaded from 
malicious ads with cloned versions of 
legitimate websites
Infostealers—malware that accesses sensitive data, like 
passwords, cryptocurrency wallets, and other information 
stored in the user’s browsers or on their devices—provide a 
wide range of options for an attacker.
While infostealing malware can be targeted, threat actors 
most frequently deployed it opportunistically. Adversaries 
often take advantage of a user looking to download software. 
“Cracked” software, or software that generally requires a 
license but attackers have modified to circumnavigate that 
requirement, represents the highest risk. In these situations, 
users are more likely to act against their better judgment in 
downloading software from a sketchy website to avoid buying 
a paid version.
This year, we saw a lot of infostealers downloaded from 
malicious ads (also known as malvertising). These ads appear 
at the top of search results and often imitate productivity or IT 
software. Clicking the ad directs the user to a cloned version 
of the legitimate software’s website. When the software 
downloads and runs, the malware executes the malicious 
payload—sometimes even installing the legitimate software 
to avoid suspicion.
Shadow IT represents a growing 
concern for security teams
We frequently saw attackers leveraging both search engine 
ads and SEO poisoning to guide users to download malicious 
payloads. These attacks target both Windows and MacOS 
systems, and the main types of malware used in these attacks 
are remote access tools (RATs) and infostealers.
Common “lures” include:
 
 Software used by IT teams (such as Advanced IP Scanner, 
Nmap, WinSCP)
 
 Productivity software (such as Notion, Notepad++, and PDF 
manipulation tools)
Shadow IT attacks became a fad for threat actors in 2023. 
Google and Microsoft actively work to combat the tactic, but 
we expect malvertising to remain popular into 2024 (and, 
ultimately, for as long as it works).
Zero-days emphasize importance of 
defense-in-depth and strong layers 
of control
Here are the top vulnerabilities our SOC identified based on 
incident frequency:
 
 Progress’ MOVEit Transfer (CVE-2023-34362)
 
 Adobe ColdFusion (CVE-2023-26360)
 
 Citrix NetScaler ADC, also known as 
CitrixBleed (CVE-2023-4966)
Properly configured and implemented security controls—
or the lack thereof—directly affect the impact of these 
vulnerabilities on an organization. All of these vulnerabilities 
were zero-days, but there’s good news: security teams 
can identify zero-day exploitation when it happens thanks 
to defense-in-depth and by understanding common 
attacker tactics.
4  
Annual Threat Report 2024
Bad actors trended toward script-
based files for pre-ransomware 
initial access
JavaScript made up the highest volume of files at 39%, but 
we also saw lots of other scripting types, including executable 
(EXE—20%),  LNK (12%), and VBS (7%) files.
JS and VBS are text files that receive less scrutiny from 
automated analysis mechanisms than EXE files. Unlike EXE, 
attackers can hide their functionality among benign content 
or by command obfuscation. By default, the native Windows 
program, wscript.exe, will execute these scripts when a user 
double-clicks the files. Attackers use this setting to their 
advantage, so we highly recommend changing this default 
setting, which can be done using a group policy object (GPO).
Witness the power of secure-by-default 
to fully stop threat vectors
At the very end of 2022, we saw the beginning of a new trend 
toward leveraging OneNote files in attacks. In January 2023, 
Microsoft pushed a patch to slow down the exploitation, and 
ultimately implemented much stronger controls in March, 
virtually killing the technique.
This not only illustrates how Microsoft can eliminate a threat 
vector, but it also proves that if organizations adopt tight 
controls, they also have the power to fully stop a threat vector.
Hospitality, travel, tech, and financial 
services stand out as heavily 
targeted industries
Hospitality held onto the top spot for industries targeted by 
phishing attacks for the second year in a row with the highest 
volume at 55%. It’s followed—but not closely—by travel (12%), 
technology (9%), financial services, and healthcare (5% each).
Hospitality held onto the top spot for 
industries targeted by phishing attacks for the 
second year in a row with the highest volume 
of targeted attacks at 55%.
Hospitality, technology, and financial services also made 
the list of top industries where we identified the most high-
risk malware and identity incidents. We recommend that 
organizations in heavily targeted industries take extra security 
measures, including phishing training, strong endpoint 
defenses, and regular reviews of the environment based on 
user-identified malicious emails.
Infostealer campaign targeting 
hospitality customers since 2022
Since 2022, our SOC has observed an infostealing campaign 
targeting our hospitality customers with the goal of 
gaining administrative access to sites like Booking.com to 
commit fraud.
The campaign has developed over time, but it generally 
looks like this: an attacker uses a Gmail account to request 
information about a booking, ask for help, or to lodge a 
complaint. Instead of an attachment, the email contains a 
link to a file storage service such as Dropbox, Google Drive, 
and Mega.nz.
In most situations, the files in the storage service are a file 
archive (ZIP, RAR, etc.), which is password-protected to 
prevent the storage provider from scanning its contents. 
When the user opens the file, the archive typically contains an 
inflated EXE file which is an infostealer.
Though this campaign targets hospitality companies, 
understanding it is extremely valuable for organizations in 
other industries, too. As a common threat vector, infostealing 
malware can affect any organization.
5  
Annual Threat Report 2024

## 2023 by the numbers
Incident types detected by the Expel SOC
Incident types in 2023 vs. 2022 (Chart 1):
 
 Identity continues to reign supreme, with a 14% increase 
out of overall incidents from the previous year. Our 
analysts work multiple identity-based incidents a day and 
we expect this trend to continue upward.
 
 Of note: while malware as a percentage of overall incidents 
decreased by 25% in 2023, the potential impact of both 
high-risk and latent-risk malware should not be discounted.
 
 Phishing incidents tripled from 2% in 2022 to 6% in 2023.
 
 The percentage of authorized penetration tests and red 
teams we investigated decreased 43%. While we can only 
speculate, this could indicate that customers are dealing 
with tighter budgets and not performing these exercises 
as often.
![Chart 1: Breakdown of incidents detected by the Expel SOC in 2022 and 2023]
Initial alert sources in 2023 and 2022 (Chart 2):
 
 Year over year, we see attackers targeting cloud 
infrastructure, as cloud incidents increased by 12% in 2023. 
Remember that monitoring your cloud is like planting a 
tree; the best time to start was five years ago. The second 
best time is right now.
 
 Similar to malware in the chart above, endpoint incidents 
fell as a percentage of overall incidents in 2023.
 
 We observed a slight decrease in initial alerts coming from 
network and SIEM as a percentage in 2023.
![Chart 2: Initial alert source]
6  
Annual Threat Report 2024

## Identity threats
Targeting email and identity platforms
Identity-based incidents were the most common 
attacks we saw across our customer base in 2023, 
accounting for 64% of all incidents handled by our 
SOC. The total of identity-based incidents rose 
144% compared to 2022.
Chart 3 shows that within these identity incidents, 60% 
were unauthorized email logins (pre-BEC), and 40% were 
authentications to identity platforms (BAC), like Microsoft 
Entra ID (formerly Azure Active Directory), Okta, Ping, and 
Duo. While email remains the top target for attackers, we 
urge security teams to consider attackers that target identity 
platforms a serious threat, too.
2023’s top threat
Over the course of 2023, the Expel SOC saw an overall 
increase in the number of identity incidents as the year 
progressed, until we saw a dip in frequency at the end of 
the year (perhaps due to normal seasonality). Take a look at 
Chart 4 on page 8 to see the peaks and valleys, as well as the 
overall increasing trend.
![Chart 3: BEC (email compromise) vs. BAC (application compromise) in 2023]
7  
Annual Threat Report 2024
W H AT  W E  S A W  I N  O U R 
P R E V I O U S  A N N U A L  R E P O R T
 
 Representing 50% of all incidents, BEC attempts 
were the top threat to our customers in 2022.
 
 60% of attempts to compromise cloud identity 
provider credentials (aka BAC activity) happened 
in Okta; 17% of the remainder were in Box and 6% 
were in Ping and OneLogin.
 
 Nonprofit, retail, and entertainment were the 
industries most targeted by BEC attacks.
 
 Of the organizations targeted by BEC 
threat actors:
 
—
—
	 53% experienced at least one BEC attempt.
 
—
—
	 24% experienced at least three BEC attempts.
 
—
—
	 One organization was targeted 104 times 
in 2022.
 
 BEC attackers moved away from authenticating 
via legacy protocols to bypass MFA in Microsoft 
365. Instead, they increasingly adopted the use 
of frameworks such as Evilginx2 to steal login 
credentials and session cookies.
 
 The number of BEC threat actors who 
successfully gained access to M365 accounts 
trended up. A main culprit was adversary-in-the-
middle (AiTM) phishing to steal session cookies.
![Chart 4: The increase in identity incidents throughout 2023]
The increased volume of identity incidents is a direct result 
of more phishing platforms becoming available on the dark 
market. “Phishing-as-a-service (PhaaS)” platforms allow 
a buyer to easily deploy convincing credential harvesters 
for a phishing campaign. Several of these harvesters can 
both pre-fill the intended victim’s email address and load 
the appropriate branding and background for the target 
organization’s login page, making them look convincingly like 
the expected login page.
“Phishing-as-a-service (PhaaS)” platforms 
allow a buyer to easily deploy convincing 
credential harvesters for a phishing campaign.
Risks of identity compromise
It goes without saying that identity compromise is serious. 
According to the Federal Bureau of Investigation’s (FBI’s) 
most recent Internet Crime Complaint Center (IC3) statistics, 
Americans reported a combined loss of $2.7 billion over 
2022 due to BEC attacks that weren’t stopped in their early 
stages. BAC was the attack type behind the much-publicized 
compromises at Uber, Nvidia, and Rockstar Games; in those 
incidents, attackers compromised user identities to gain 
access to sensitive data, sell it, and use it for extortion.
At Expel, mitigating identity threats is a priority. We 
understand many of these attacks attempt to leverage 
access as soon as possible, and we pride ourselves on our 
ability to detect and respond quickly to secure an account. 
Our goal is to respond to the compromise in real time as 
much as possible to prevent the attack from playing out. 
However, by taking action and stopping an attack, it becomes 
impossible to understand the full intent of that attack. In 
most situations, we classify the attack based on the type of 
account compromised.
As such, we classify evidence of a compromised user 
password as an identity incident. In some instances, MFA or 
conditional access blocks logins; however, we treat these 
with the same seriousness as an incident due to the high 
risk that would exist were the incident to play out. Many 
authentication blocking methods are but a small speed bump 
for attackers and require our analysts to take further action 
to prevent potentially successful attempts. In fact, we’ve 
seen many instances when an attacker tried to login, was 
blocked by conditional access based on geolocation or MFA, 
and immediately switched to a bypass method, like a VPN or 
legacy protocol, resulting in successful login.
Furthermore, compromise of credentials is evidence of 
another compromise: users may have entered credentials 
into a credential harvester, had their credentials stolen by an 
infostealer (more on these later), or been exposed due to a 
weak password or a previous data leak. Organizations should 
thoroughly investigate any situation where users could have 
unknowingly compromised their passwords.
8  
Annual Threat Report 2024
![Chart 5: Identity incidents by vertical industry]
Identity incidents by industry verticals
Throughout 2023, threat actors targeted non-profit 
organizations most, followed by technology companies and 
financial services.
Chart 5 shows the percentage of identity incidents our 
SOC saw, broken down by industry. Like in past years, this 
breakdown shows that threat actors don’t discriminate—while 
some industries are targeted more often than others, none 
are immune.
Identity targeting frequency
Identity incidents affected 58% of our customers (up from 
53% in 2022). But if we dig into the data and look at the 
frequency our customers are targeted, we get a clearer 
picture of the pervasiveness of these attacks.
Of the organizations targeted with an identity attack:
 
 35% experienced more than one incident (up from 24% 
in 2022).
 
 Organizations saw an average of eight identity-based 
incidents over the year.
 
 One non-profit organization was targeted 255 times (up 
from 104 times in 2022).
One non-profit organization was targeted 255 
times (up from 104 times in 2022).
This data illustrates that some organizations are targeted 
more than others, and those with a lower public profile and 
more compensating controls are less likely to experience 
identity attacks.
Identity incidents by source technology
We identified 88% of incidents based on signal from Microsoft 
products. This high targeting rate is due to Microsoft’s large 
business email and identity market share, which makes the 
company’s identity products an attractive target—similar to 
the way Windows operating systems are highly targeted by 
malware because of Microsoft’s prominent place in end-user 
operating systems.
Okta was a distant second place to Microsoft, being the 
source of 9% of identity incidents. Google Workspace 
(recently rebranded from G Suite), Duo, OneLogin, Ping, and a 
few others make up the remaining technologies.
9  
Annual Threat Report 2024
Malicious login sources
Sixty-nine percent of incidents in 2023 involved malicious logins 
from suspicious infrastructure, which are hosting providers or proxies 
that aren’t expected for a user or organization. These logins may not 
be geographically suspicious but are abnormal for the specific user. 
When we analyze abnormal logins, we’re looking at the details of the 
IP address associated with the login against the user’s or account’s 
baseline behavior.
Just over 10% of malicious logins came from VPNs, and the rest (about 
21%) were identified through geolocation alerts. See Chart 6 for 
the breakdown.
This is consistent with a trend we noted in 2022—namely, that attackers 
were shifting to using more proxies, VPNs, and hosting providers to 
bypass network zone and conditional access policies. The takeaway? 
Organizations need to take any abnormal logins seriously.
Let’s look at an example: here’s a user logging in from the IP 
address 196.247.229.187, associated with Packet Exchange, 
which differs from the expected baseline.
We compare this information with the user’s baseline and 
often we’re able to identify clearly if the origin is normal or 
abnormal for the user.
![Image 1: Expel Workbench™ IP lookup results for an anomalous login]
![Image 2: Results from automated review of user behavior]
![Chart 6: Breakdown of malicious login sources]
10  
Annual Threat Report 2024
QR code attacks
We found that Microsoft’s threat intelligence can reliably 
identify phishing pages created with PhaaS platforms. 
Customers using Microsoft’s Defender for Endpoint product 
regularly received alerts for users accessing credential 
harvesters. However, Microsoft’s effectiveness in identifying 
these pages may have inadvertently contributed to an 
increase in threat actors’ use of QR codes.
 
Qishing attacks take the activity off endpoints—which 
Microsoft defenses have visibility into—and put it on mobile 
devices, which may not be managed with tight security 
controls. This allows the attacker to bypass endpoint controls.
How to protect your organization from malicious login sources
 
 Deploy phish-resistant MFA.
 
 If FIDO-only factors for MFA are unrealistic, opt for 
push notifications.
 
―
̭
	
If feasible for your environment, configure 
identity provider policies to restrict access to 
managed devices.
Pay close attention to detections related 
to suspicious logins.
 
 Pay close attention to detections related to suspicious 
logins. Most technologies will monitor for user behavior 
that differs from the baseline but these alerts do no 
good unless they’re reviewed and analyzed by security 
or IT teams.
 
―
̭
	
Use vendor technologies that identify or block 
authentication attempts with previously unseen 
authentication characteristics, such as impossible 
travel, unusual locations for the environment, or a 
new device for the account.
 
 Use policies to block access from suspicious logins 
based on IP address(es), autonomous system numbers 
(ASN), IP types, or geolocation, and configure 
pre-auth policies.
 
 Of note: when analyzing these alerts, remember that 
malicious logins don’t only occur from suspicious 
locations or VPNs—a lot also come from hosting 
providers and proxies.
 
 Use password managers to create, store, and share 
passwords. These allow users to create unique, 
complex passwords and store them in a way that keeps 
them safe from attackers and infostealer malware.
How to protect your organization from QR code attacks
Microsoft only recently released new features to 
address qishing, so we have yet to see the full impact 
of its response. We believe that to make a real impact, 
Microsoft needs to block QR codes by default. If Microsoft 
makes the settings configurable, we recommend 
organizations opt for the strictest QR code settings.
For organizations that aren’t using Microsoft products, 
it’s still important to understand these tactics and ensure 
users are wary of QR codes just as they might be wary 
of a URL. And, if an organization uses QR codes for any 
reason, it should make end users (customers, partners, 
employees, vendors, etc.) aware of when and how it 
uses them.
11  
Annual Threat Report 2024
Targeted attacks
“The Com,” a hacking group including the actors tracked as 
“Scattered Spider,” was responsible for the largest number of 
targeted identity attacks this year. These attackers primarily 
targeted Okta and Microsoft accounts, attempting to abuse 
password reset mechanisms and MFA push fatigue to 
gain access.
We observed two main attack tactics: (1) calling into an 
organization’s helpdesk, and (2) abusing self-service 
password reset mechanisms.
When calling into the helpdesk the actors impersonated staff 
and requested that their passwords be reset. If either the 
helpdesk or self-service request attempts were successful, 
the threat actor sent MFA pushes to the real user. If the 
user accepted the MFA push, the attacker gained access to 
the account.
Attacks from these actors are high-volume, too. In one 
environment, an attacker submitted password reset attempts 
for more than 100 accounts. In multiple attacks, organizations 
blocked the attempts thanks to controls that required 
authentications from a compliant device. Of note, in the 
second half of the year, the threat actor primarily targeted 
customers in the financial services industry. We expect this 
style of attack to continue in 2024.
According to Microsoft, these actors perform thorough 