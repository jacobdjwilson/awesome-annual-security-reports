proofpoint.comAn In\-Depth Exploration of User Awareness,Vulnerability and Resilience2022 State of the PhishREPORT2021: THE YEAR OF THE NEW NORMAL?A NOTE ON TERMINOLOGYPhishing can mean different things to 
different people. We use the term in a broad 
sense to encompass all socially engineered 
email attacks, regardless of the specific 
malicious intent (such as directing users to 
dangerous websites, distributing malware, 
collecting credentials and so on).Here are a few of the other terms we use 
throughout this report and how we define 
them:Bulk phishing: indiscriminate,commodity attacks in which the same 
email is sent to many people within an 
organization.Spear phishing: Targeted attacks sent to 
selected people within an organization.Whaling: Attacks against high\-valuetargets, such as top executives.Smishing: Attacks that use mobile textmessaging (SMS) as the main 
communication vector.Vishing: Attacks that use phone calls orvoice messages to lure targets.Last year, we titled our introduction A Year Like No Other. We could easily have 
repeated that heading to describe 2021\. The year has left many organizations 
contemplating what normal will mean for their workforces going forward.Along with hybrid and remote work options, organizations are mulling the best 
ways to keep employees connected and collaborative. Studies show the ongoing 
pandemic has had a major impact on workers mental health. Employees are 
feeling burned out, emotionally drained and distracted.1 Meanwhile, cyber 
attackers are as adept as ever. And they continue to use tactics and lures that 
resonate with employees and consumers alike.In this, our eighth annual State of the Phish report, we explore user vulnerabilities 
from multiple angles. We look at issues driven by poor cyber hygiene and those 
that could result from a lack of knowledge and clear communication. We discuss 
ways organizations can become more attuned to their risks. And we outline 
opportunities to build and sustain engaging security awareness training initiatives 
in this challenging climate.This years report includes analysis of data from the following sources:A commissioned survey ofA commissioned survey of3,500600working adults across 
seven countries (Australia, France, 
Germany, Japan, Spain, the United 
Kingdom and the United States)information and 
IT security professionals across the 
same seven countriesAlmostMore than100 million15 millionsimulated phishing attacks sent by our 
customers over a 12\-month periodemails reported by our customers end 
users over that same time period21Society for Human Resource Management. Ongoing Pandemic Takes Toll on Workers Mental Health.August 2021\.2022 STATE OF THE PHISHREPORTTable of Contents1The 2021 Threat Landscape:
a High\-Level View. . . . . . . . . . . . . . . . . . . . . . . . 44Benchmarking: Failure Rates andComparison Data . . . . . . . . . . . . . . . . . . . . . . . . 23Cashing in on COVID. . . . . . . . . . . . . . . . . . . . . . . . 5Failure rates by template type . . . . . . . . . . . . . . . . . 23Dialing to defraud. . . . . . . . . . . . . . . . . . . . . . . . . . 5Industry failure rates. . . . . . . . . . . . . . . . . . . . . . . . 25Making it personal . . . . . . . . . . . . . . . . . . . . . . . . . . 5Department failure rates . . . . . . . . . . . . . . . . . . . . . 262By the Numbers: Targeted Attacks,Ransomware, and Ramifications . . . . . . . . . . . . . 65Email Reporting and Resilience:Measurements and Goals. . . . . . . . . . . . . . . . . . 29Phishing attacks on the rise . . . . . . . . . . . . . . . . . . . 6Calculating resilience . . . . . . . . . . . . . . . . . . . . . . . 29Other social engineering attacks also up . . . . . . . . . . 7Benchmarking: industry resilience factors. . . . . . . . 31Attackers were more successful in 2021 
than in 2020\. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8Successful attacks had wide\-ranging impacts. . . . . . 9Ransomware: nearly 60% of infected
orgs paid upmany more than once . . . . . . . . . . . 103Working Adults: Cybersecurity Habitsand Knowledge Gaps . . . . . . . . . . . . . . . . . . . . . 12Overview: more devices, more issues. . . . . . . . . . . 12Survey says: communicate clearly
to train effectively. . . . . . . . . . . . . . . . . . . . . . . . . . 13Misconceptions about email . . . . . . . . . . . . . . . . . . 15Getting personal with employer\-issued
devices. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16Real\-world phishing and reporting accuracy . . . . . . 326Security Awareness Training:Insights and Opportunities . . . . . . . . . . . . . . . . . 34Training tools and frequency of use. . . . . . . . . . . . 35Orgs ignore too many important topics when
training users . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 377Making It Personal: IdentifyingVulnerabilities, Gauging Success . . . . . . . . . . . . 418Appendix . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45A. Infosec and IT security survey:
country\-by\-country breakdown. . . . . . . . . . . . . . . 45Employee\-driven risk: the (even)
bigger picture. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18B. Working adult survey:
country\-by\-country breakdown. . . . . . . . . . . . . . . 53Parting thoughts: risky business in 2021\. . . . . . . . 20C. Industry failure rates by
simulated phishing template style . . . . . . . . . . . . . . 5932022 STATE OF THE PHISHREPORTSection 1The 2021 Threat Landscape:
a High\-Level ViewFor many, 2021 felt like a year\-long case of dj vu. Pandemic\-related concerns 
remained top\-of\-mind for employees and organizationsand for many cyber 
attackers. Human resources and operations teams suddenly had to support 
remote and hybrid work models. Meanwhile, information security and IT teams 
had to secure it all.The first three quarters of the year were busy ones for cyber attackers: we 
identified nearly 5,500 campaigns2 that used one or more recognizable tactics. 
Our researchers also identified nearly 15 million phishing messages with malware 
payloads that have been directly linked to later\-stage ransomware. Of these 
malware families, Dridex, The Trick, Emotet, Qbot, and Bazaloader were the most 
common.MALWAREThe TrickBazaLoaderSocGholishIcedIDQbotRANSOMWAREWastedLockerRyukEgregorMazeSodinokibiProLockFigure 1: Observed links between first\-stage malware families and later\-stage malware.2We define a campaign as a group of related threats and activities. Phishing messages within 
a campaign share common attributes, like the same or similar subject lines, the same sending 
infrastructure, and the same eventual payload. Further research related to a campaign often reveals 
further commonalities, such as the threat actor behind it, the type of malware being used, and targeted 
geographies or industries.42022 STATE OF THE PHISHREPORTABUSING THE BRAND: HOW 
ATTACKERS PIGGYBACKED
BIG TECH NAMESMicrosoft, Google, Zoom and Amazon 
were among the most abused brands 
in attack campaigns seen in the first 
three quarters of 2021\. More than 1,100 
campaigns abused the Microsoft brand, 
using a Microsoft\-themed lure or product 
to steal credentials or deliver malware.Amazon campaigns tended to be high 
volume: fewer than 100 campaigns 
accounted for more than 68 million 
total messages. Much of this volume 
was attributable to sizeable Japanese\-
language campaigns, which continued 
into 2021 after surfacing in 2020\. In 
comparison, about the same number of 
COVID\-themed campaigns totaled around 
1\.3 million messages.Cashing in on COVIDNot surprisingly, COVID\-themed campaigns continued, mimicking the 
opportunistic attacks that piggybacked pandemic developments throughout 
1\. As public concerns ebbed and flowed, so did COVID\-themed phishing 
attacks. We saw a lull through the spring and early summer of 2021\. But as the 
delta variant took center stage, pandemic\-themed attacks surged. Beginning 
in June 2021, we saw an uptick in campaigns that latched onto timely, relevant 
COVID\-related topics, such as vaccine mandates and organizational policies.3Dialing to defraudAnother trend involved telephone\-oriented attack delivery (TOAD). These 
schemes are nothing newwe detect and block tens of thousands of TOAD\-
related emails every day.4 But we saw an uptick in 2021, many of them part of 
a robust and complex attack chain. Multi\-faceted TOAD efforts use a variety of 
tools, such as: Fraudulent emails Call centers Well\-designed websites and mobile apps Remote access software Malware, including downloaders linked to later\-stage ransomware deliveryMost TOAD threats require the victims active participation. While this approach 
may seem counter\-intuitive from a security standpoint, it works. Perhaps the level 
of detail and familiar approach work in the attackers favor. For many people, 
calling a support line for help may seem a safe option. And many feel more 
comfortable when an authority figure talks them through account updates and 
refund processes. In addition, many organizations use the same remote access 
software that attackers exploit in TOAD schemes and other attacks. These 
activities could bypass security protections designed to block malicious remote 
access attempts.Making it personalTOAD threats and other attacks in 2021 targeted both personal and organizational 
email addresses. Amid the shift to remote work, targeting personal addresses 
can have a bigger impact on organizations than in years past. As we note later 
in the report, many people (and their family members!) are accessing personal 
information and accounts on employer\-issued devices.In general, the 2021 threat landscape reinforced one key point: successful threat 
protection requires people\-centric defense in depth. Your users must be a key 
part of the security stack. The more informed and equipped they are, the more 
resilient your organization will be.3Selena Larson (Proofpoint). As Delta Variant Spreads, COVID\-19 Themes Make Resurgence in EmailThreats. August 2021\.4Selena Larson, Sam Scholten and Timothy Kromphardt (Proofpoint). Caught Beneath the Landline:A 411 on Telephone Oriented Attack Delivery. November 2021\.52022 STATE OF THE PHISHREPORTA LOOK BACK AT 202077%of organizations saw bulk
phishing attacks66%of organizations dealt with
spear phishing attacks.65%of organizations faced
BEC attacks.COUNTRY SPOTLIGHT91%of UK survey respondents said their 
organization faced bulk phishing attacks
in 2021\.90%or more of Australian respondents said their 
organization faced spear phishing, BEC and 
email\-based ransomware attacks in 2021\.Section 2By the Numbers: Targeted Attacks, 
Ransomware, and RamificationsThis years State of the Phish again presents the results of a Proofpoint\-designed 
study of the threat landscape, as seen through the eyes of information security and 
IT security professionals. Our quantitative surveys, conducted by an outside polling 
firm, asked 600 participants across Australia, France, German, Japan, Spain, the 
United Kingdom and the United States about their organizations experiences in 2021\.Phishing attacks on the riseAccording to respondents, the 2021 threat landscape was more active than 
2020s. Reports of phishing attacks were up across the board. Indiscriminate 
bulk phishing attacks rose 12% year over year. And increases in targeted 
attacks were even higher: reports of spear phishingwhaling and business email 
compromise (BEC)which includes payroll redirect and supplier invoicing 
fraudwere up 20% and 18%, respectively.5 Note: the figures represented in 
Figure 2 include both successful and unsuccessful attacks.Volume of Bulk Phishing AttacksVolume of BEC Attacks2%14%15%86%
of organizations 
faced bulk 
phishing attacks
in 202136%33%Volume of Spear Phishing
and Whaling Attacks2%13%21%79%
of organizations 
saw attacks 
targeting specific 
users in 202137%27%35%2%13%23%77%
of organizations 
faced BEC attacks 
in 202135%27%Volume of Email\-Based
Ransomware Attacks61%14%22%78%
of organizations 
saw email\-based 
ransomware 
attacks in 202128%No attacks1\-1011\-5050\+Total unknownFigure 25Unless otherwise indicated, survey results represent global averages. You can find country\-by\-countrybreakdowns of survey questions and findings in the Appendix.6New figures for this years report. Note that survey respondents were specifically asked to identify attacksin which a ransomware payload was delivered or intended to be delivered via email.62022 STATE OF THE PHISHREPORTA LOOK BACK AT 202061%saw smishing attacks.61%dealt with social media attacks.54%faced vishing attacks.54%reported USB\-based attacks.Other social engineering attacks also upEmail remains the top attack vector for cyber criminals. But its not the only way 
bad actors are trying to compromise people and the organizations they work 
for. Reports of SMStext phishing (smishing), voice phishing (vishing), and social 
media\-based attacks all increased by more than 20%. And reports of USB drops 
were up more than 15%.Volume of Smishing AttacksVolume of Social Media Attacks1%2%16%26%74%
of organizations 
faced smishing 
attacks in 202123%34%17%26%74%
of organizations 
saw social attacks 
in 202134%21%COUNTRY SPOTLIGHTUK and Spanish respondents had very 
different experiences with non\-email\-based 
social engineering attacks in 2021:Spanish Organizations Were
Least Likely to Face Attacks\<60%faced smishing and social media attacks.\<50%faced vishing attacks and malicious
USB drops vs UK Organizations Were Most
Likely to Face High Volumes\>20%faced 50\+ smishing, social media, and 
vishing attacks.18%faced 50\+ malicious USB drops.Volume of VishingVolume of Malicious USB Drops1%13%31%69%
of organizations 
faced vishing 
attacks in 202133%22%1%12%36%64%
of organizations 
saw USB\-based 
attacks in 202132%19%No attacks1\-1011\-5050\+Total unknownFigure 372022 STATE OF THE PHISHREPORTKEY FINDINGS83%of survey respondents said their 
organization experienced a successful 
email\-based phishing attack in 2021,
up from 57% in 2020\.54%said their organization dealt with more
than three successful attacks.11%experienced 10 or more successful attacks.COUNTRY SPOTLIGHT92%of Australian organizations dealt with 
successful attacks, the highest of any 
region surveyed (and a 53% year\-over\- 
year increase).66%of Japanese organizations experienced a 
successful phishing attack in 2021, the 
lowest of any region surveyed (though
18% higher than 2020\).Attackers were more successful in 2021 
than in 2020Not every attempted attack succeeds. Millions of malicious emails are blocked 
by email gateways every day. Advanced email analysis and detection tools are 
getting better at identifying and stopping impostor emails and the many flavors of 
email fraud, including BEC. So in some ways, a successful phishing attack is like 
the proverbial needle in a haystack.But those successful attacks do real damage. And 2021 was especially painful for 
the infosec and IT security workers we interviewed.More than 80% of our survey respondents said their organization suffered a 
successful email\-based phishing attack in 2021\. Thats a 46% jump from 2020\. 
Several factors may be at play in the increase, including those in the following 
sections.Pandemic fatigueThe World Health Organization (WHO) defines pandemic fatigue, in part, as 
demotivation to follow recommended protective behaviors, emerging gradually 
over time.7 WHOs behavioral focus centers around restrictions and suggestions 
related to containing infections. But many researchers have cautioned that COVID 
exhaustion is hurting people in other waysincluding job performance.8Attention spans are short. Many feel displaced and disconnected. Others struggle 
to remain engaged in work environments that revolve around virtual conferencing 
and an overload of screen time. The bottom line? People are not at their best. And 
thats likely leading to more mistakes in the inbox.Exploiting legitimate servicesCloud collaboration is now a normal part of business. And where people and 
organizations go, attackers follow.In the first half of 2021, we saw a marked increase in the abuse of Microsoft 
and Google infrastructures, which were used to host and send threats across 
Microsoft 365 (including Office apps, OneDrive, and SharePoint), Microsoft Azure, 
Google Workspace, and Firebase storage. Because these messages mimic 
standard business processes, it can be hard for employees to tell the difference 
between malicious messages and safe ones apart.This is especially true for employees who are unaware that attackers operate 
this way. And plenty are uninformed: more than 30% of working adults think that 
emails with familiar logos are safe, and 35% believe that all files stored in a cloud 
service like Google Drive are safe. (See more from our survey of working adults in 
Section 3\.)7World Health Organization, Regional Office for Europe. Pandemic fatigue: Reinvigorating the public toprevent COVID\-19\. October 2020\.8Healthline. COVID Fatigue: How to Cope with Pandemic Burnout. October 2021\.82022 STATE OF THE PHISHREPORTKEY FINDINGSThe impacts of successful phishing attacks 
varied widely in 2021\. While Australia and 
Japan are both part of the Asia\-Pacific 
region, respondents in the two countries 
reported wildly different experiences.Australian organizations reported adverse 
outcomes of successful attacks at rates 
higher than global averages in all cases but 
one: just 20% of respondents said their 
organization experienced a widespread 
network outage following a phishing attack 
(vs. 22% globally).At the other end of the spectrum, many of 
the differences were significant. For 
example, 30% reported direct financial loss, 
nearly twice the global average. And 61% 
said their organization experienced 
ransomware as an email payload, 33% 
higher than the global average.In contrast, Japanese respondents reported 
lower\-than\-average effects in all cases but 
one: they matched the 27% global average 
for reports of malware other than 
ransomware. And their lows were markedly 
lower in multiple cases: just 3% said their 
organization experienced direct financial 
loss (vs. the 17% global average) or 
financial penalties (vs. the 11% global 
average). And no Japanese respondents 
said their organization faced an advanced 
persistent threat (APT) following a 
successful attack in 2021\.Use of trending contentAttackers have taken advantage of trending topics and events for years. But 
exploiting of trends seems to have become, well, a trend in itself. And its gotten 
more intense since the onset of the pandemic. Weve seen attackers lures 
morphing to coincide with current public concerns and discourse with greater 
speed and strategy than ever.9Beyond evolving COVID lures in 2021, we saw attackers use lures associated with 
popular trends. Here are just a few examples of attack lures: Streaming shows, such as Squid Game Pop\-culture events, such as a Justin Bieber world tour Economic issues, such as U.S. unemployment programsWe even saw a sophisticated, multi\-faceted campaign that included a fake 
streaming service, luring victims looking to cancel nonexistent subscriptions. 
(The campaign coincided with a wave of people cancelling their pandemic\-fueled 
streaming video subscriptions.)Attackers are skilled and savvy. They know the appeal of relevant content. And 
when content is more appealing, people are more likely to engage with it.Successful attacks had wide\-ranging impactsSuccessful attacks dont happen in a vacuum. Phishing emails can affect 
organizations in many ways. While some effects are immediate, others arent 
known about or felt until later.We expanded our view of impacts this year (see Figure 4\), so we cant make year\-
over\-year comparisons in some cases. But we did see an 8% drop in reports of 
credential compromise, a 6% drop in direct financial loss and a 2% drop in email\-
driven ransomware infections vs. 2020\.Still, these marginal improvements are little consolation, especially when 
considering the real\-world consequences of each statistic. With the rise in 
crippling ransomware infections, critical infrastructure attacks and supply chain 
fraud, cybersecurity threats are more serious than ever.9ThreatPost. Phishers Capitalize on Headlines with Breakneck Speed. October 2020\.92022 STATE OF THE PHISHREPORTResults of Successful Phishing Attacks (Global Average)54%48%46%44%Breach of customer or client dataCredentialaccount compromiseRansomware infection (payload delivered via email)Loss of dataintellectual propertyMalware other than ransomwareReputational damage27%24%Widespread network outagedowntime22%Advanced persistent threat18%Financial losswire transfer or invoice fraudZero\-day exploit17%15%Financial penaltyregulatory fine
11%0102030405060Figure 4Ransomware: nearly 60% of infected orgs paid up
many more than onceRansomware made headlines throughout 2021, with government and critical 
infrastructure sectors particularly hard hit. Security agencies around the 
globe cautioned organizations of all sizes to strengthen their defenses against 
ransomware, and with good reason.Our researchers have been tracking threat actors who have become initial access 
brokers and, likely, ransomware affiliates, selling the access theyve gained 
through first\-stage malware to other operators. This scale and the availability 
of ransomware\-as\-a\-service offerings have both fueled the rise in successful 
attacks.10As shown in Figure 5, nearly 70% of organizations dealt with at least one 
ransomware infection 2021 (a slight increase over 2020\). Of those, nearly two\-
thirds experienced more than three separate infections. And nearly 15% dealt with 
more than 10 separate infections.11KEY FINDING68%of organizations experienced at least
one ransomware infection in 2021
(up from 66% in 2020\).10Proofpoint. Tips for Developing Your Ransomware Defense Strategy. November 2021\.
11 This includes infections from all sources, including initial payloads and later\-stage delivery. The number ofseparate infections may have resulted from a single intrusion or separate incidents.102022 STATE OF THE PHISHREPORTOnce infected, nearly 60% opted to negotiate with attackers (with mixed results), 
despite cybersecurity and government agencies warning against the practice. As 
always, payment does not guarantee restoration of data (as some of our survey 
respondents found out firsthand). In addition, ransomware payments are likely 
to fuel the fire, rewarding attackers for their activities and encouraging repeat 
behavior.Ransomware by the Numbers1%14%34%16%68%
of organizations 
were infected
by ransomware
in 2021Ransomware Infections:
What Happened After Payment4%10%58%
of infected 
organizations 
agreed to pay 
ransom in 202132%54%35%1\-3 separate infections4\-6 separate infections7\-9 separate infections10 or more separate infectionsUnsure of totalRegained access to datasystems 
after first paymentPaid additional ransom demand(s) 
and eventually regained accessRefused to pay additional ransom demand(s) 
and walked away without dataNever got access to datasystems, 
even after paying ransom(s)Figure 5COUNTRY SPOTLIGHT81%of French organizations experienced a 
ransomware infection last year, the highest 
of any country surveyed. (At 50%, Japanese 
organizations were least likely to experience 
an infection.)30%of Australian organizations that experienced 
ransomware said they dealt with 10 or more 
separate infections.82%of UK organizations that were infected opted 
to pay the ransom, the highest of any region 
surveyed (and 41% higher than the global 
average).42%of Spanish organizations admitted to paying 
more than one ransom to regain access to 
data, the highest of any region surveyed. 
But at 21%, they were also the most likely 
to refuse to pay a follow\-up ransom after 
making an initial payment.112022 STATE OF THE PHISHREPORTSection 3Working Adults: Cybersecurity Habits 
and Knowledge GapsAs in the past, this years State of the Phish dedicates significant real estate 
to exploring the greatest source of organizational security risk: people. Our 
quantitative surveys, conducted by a third party, asked 3,500 working adults 
across seven countries (Australia, France, German, Japan, Spain, the United 
Kingdom and the United States) about their cybersecurity perceptions, habits and 
experiences in 2021\.All survey participants identified as being 18 years or older and employed. 
Different roles and responsibilities are represented in this group of 
respondentsa blend that reflects the workforces in many organizations.We didnt isolate on deskbound workers or those in computer\-dominated 
positionsand that was intentional. We wanted the survey group to represent the 
makeup of all the people who can influence an organizations security posture. 
And make no mistake: every person who works within an organization can have a 
positive or negative impact on security, no matter what their role is.Overview: more devices, more issuesAll survey respondents said they use one or more electronic devices (phone
smartphone, laptop computer, desktop computer or tablet) for their job. Among 
these: 73% said they have access to at least one employer\-issued device 74% said they use one or more of their own devices for work\-related purposes 54% use a personal phonesmartphone and 22% use a personal tablet for work 44% said they are in a new remote working environment (either full time or parttime) due to the pandemic12 83% said they received at least one suspicious communication (either via email,text message, social media, or phone call) in 2021 42% said they took a dangerous action (clicked a malicious link, downloadedmalware, or exposed their personal data or login credentials) in 2021We highlight these statistics to illustrate a point that must be considered 
throughout this section: workers personal choices often lead to
organizational risk.1312To add more context, we also asked our infosec and IT professionals about the impact the pandemichas had on remote work. Some 81% said at least half of their organizations employees are now working 
remotely, either full time or part time. Another 14% said employees had worked remotely due to COVID, 
but were no longer doing so (while just 6% of our working adults said the same).13Unless otherwise indicated, survey results represent global averages. You can find country\-by\-countrybreakdowns of survey questions and findings in the Appendix.COUNTRY SPOTLIGHT80%of U.S. workers use one or more of their 
own mobile devices for work. 64% said they 
use personal phonessmartphones, and 
30% use personal tablets. These results 
were the highest of any region surveyed.32%of Japanese workers said they do not have 
access to an employer\-issued electronic 
device (but 100% use one or more 
electronic devices for work purposes).33%of U.S. workers and 30% of Australian 
workers said they are now working remotely 
full time due to the pandemic, well more 
than the 20% global average.30%of UK workers now have a hybrid approach 
to working (part\-time on site, part time 
remote).47%of French workers and 45% of German 
workers said the pandemic did not impact 
their work location, the highest among the 
regions surveyed.122022 STATE OF THE PHISHREPORTOur what is survey questions offered 
three multiple choice answers and an 
Im not sure option. In reviewing 
results, consider that users who dont 
know an answer may pose as much risk 
as those who answer incorrectly.Survey says: communicate clearly to train 
effectivelyWeve been assessing working adults recognition of common cybersecurity 
terminology for several years. And while we saw some decent progress last year, 
this years results have rolled that back. One considerable drop was with the 
term phishing: correct answers were down more than 15%, and Im not sure 
responses were up more than 30%.Ransomware responses provided the one bright spot, with recognition up about 
10% and unsure responses holding steady. With the rise in ransomware attacks 
around the globe, this improvement comes at a good time.The overall decline in awareness is another area where pandemic fatigueand 
its impact on workers engagement and attention spanscould be a factor. It 
could also reflect a decreased prioritization of cybersecurity awareness and 
training initiatives during 2021\. The pandemic has put many different pressures on 
organizations, and some may have been forced (due to lack of time, resources or 
other factors) to deprioritize employee education programs.Another possibility: perhaps workers are overloaded by the sheer amount of 
terminology they hear or news stories detailing cyber attacks and warning of dire 
consequences. People may simply be feeling overwhelmed and confused.Whatever the case, this years results make it clear: it is never safe to assume 
workers recognize security lingo, no matter how often these terms make 
headlines. This is especially true if your formal security awareness training 
sessionsapart from phishing simulationshappen infrequently. Reminders and 
reinforcement are critical to knowledge and skill development. Employees need 
to understand the language you speak to fully absorb what youre saying and, 
eventually, learn from it.132022 STATE OF THE PHISHREPORTTerm limits: what users (dont) knowWhat isPHISHING?Correct53%IncorrectI Dont Know27%20%Correct answers were down from last years 63% mark, a 
16% year\-over\-year decrease.UK workers were again most likely to answer correctlybut 
this years 62% fell short of last years 69%.What isRANSOMWARE?Correct36%IncorrectI Dont Know33%31%This is the only term that saw an increase in recognition, 
with correct answers rising from 33% and incorrect 
responses falling from 36%. (Unsure responses held steady 
at 31%.)At 49% correct, Australian workers performed well above 
the global average. French and German workers were least 
likely to answer correctly (at 27% and 26%, respectively).What isMALWARE?Correct63%IncorrectI Dont Know20%17%Like last year, Spanish workers led their global counterparts 
in recognition of this term. But this years 73% was lower 
than last years 75% (and well off the 80% high mark from 
two years ago).At 52%, Japanese workers were least likely to answer this 
correctly, and another 38% were unsure of how to answer.What isSMISHING?Correct23%IncorrectI Dont Know32%45%Global recognition of this term was down from 31% last 
year, a 26% year\-over\-year drop.Japanese workers again struggled with this term. Just 17% 
answered correctly (down from 19% last year), and 56% 
were unsure of how to answer (the same as last year).What isVISHING?30% of global respondents answered this question correctly 
last year, representing a 20% year\-over\-year decrease in 
recognition.Correct24%IncorrectI Dont Know31%45%French workers went from first to worst in recognition of 
this term. Last year, they led all regions at 54% correct. 
This year, just 17% answered correctly (a decrease of 
nearly 70%).142022 STATE OF THE PHISHREPORTMisconceptions about emailDefining cybersecurity threats isnt always a key to defending against them. So, 
we wanted to know what workers believe to be true about email and email\-based 
attack methods.We saw plenty of bright spots. For example, 86% of respondents recognize that 
they should be cautious of any unsolicited message. And this response level was 
mostly steady across all regions surveyed. At 81%, French workers were the only 
group to dip below the 85% mark.But theres always room for improvement. We see some areas where quick 
and clear communication is called for. Employees need immediate clarity on 
key points like internal email, cloud documents, and the need to take personal 
responsibility for email security. More than two\-thirds of respondents showed 
a lack of understanding about the capabilities of technical email safeguards 
on work accounts. That lack of knowledge is a clear and present danger to 
organizations around the globe.Email Survey Results1481%77%52%38%know that email 
attachments can be 
maliciousknow that an email can 
appear to come from 
someone other than the 
true senderknow that familiar logos 
and contact information 
arent an automatic 
indication of safetyknow that their personal 
email provider cannot 
block all dangerous email37%37%36%30%know that files stored 
in the cloud can be 
maliciousknow that unsafe 
contacts may email them 
multiple timesknow that even internal 
emails could be 
dangerousknow that their 
organizations security 
tools cannot block all 
dangerous emailFigure 6COUNTRY SPOTLIGHTTop Performers85%of German workers know that email 
attachments can be dangerous.82%of UK workers know that an emails sender 
details can be disguised.63%of Japanese workers know that familiar 
logos in emails dont equate to safety.49%of Japanese workers know that unsafe 
contacts may email them multiple times vs Bottom Performers59%of Spanish workers think that all internal 
emails are safe57%of Spanish workers think their organization 
will automatically block all malicious email 
(and 49% believe their personal email 
provider will do the same)46%of U.S. workers think that all files stored in 
the cloud are safe42%of U.S. workers believe all emails with 
familiar logos are safe14We asked similar questions in last years survey, but in a different format. We believe this years format 
offered more clarity and more accurate findings. Full details and results for these questions are in the 
Appendix.152022 STATE OF THE PHISHREPORTKEY FINDING56%of workers who have an employer\-issued 
device grant access to friends andor family 
members (up from 52% last year).Getting personal with employer\-issued devicesWith 44% of global workers saying they are working remotely either part\-time 
or full\-time due to the pandemic, the line between personal life and work life 
is murkier than ever. But heres something that is clear: employees personal 
choices can pose a major risk to your data, devices and systems.As noted earlier in this section, 73% of our survey participants said they have 
access to at least one employer\-issued electronic device. Of those, 77% admitted 
to using those devices for personal purposes. This is a drop from last years 81%, 
and as shown in Figure 7, we saw a decline in several specific activities.For example, the number of workers who said they check personal email on 
employer devices decreased more than 25%. Social media use also decreased, 
down 15% year over year. But online shopping was upand the number of 
people who said they play games on employer devices jumped more than 75%.Personal Activities Performed on Work\-Issued DevicesCheckrespond to personal email 42%57%79%Read news stories 40%
 40%
 41%Research (new products, travel destinations etc.)2021
2020
2019Shop online 37% 35%37% 32% 30%27%Viewpost to social media29% 34%
34%Stream media (music, videos etc.)28%
29%25%23%Play games13%11%0%10%20%30%40%50%60%70%80%90%100%Figure 7162022 STATE OF THE PHISHREPORTWhile workers personal use of employer devices decreased overall, their 
willingness to grant access to friends and family increased. More than 55% of 
those with employer devices allow others to use them. About 5% admitted that 
use is unsupervised, meaning they do not monitor or restrict activities on the 
devices. (A seemingly small number, but a mighty risk.)Some friends and family activities increased while others decreased. As with 
workers themselves, playing games showed the largest gain (up nearly 75% over 
last year). And as shown in Figure 8, several of the activities are up sharply since 
our 2019 survey.Friends and Family Activities Performed on Work\-Issued DevicesCheckrespond to personal email 23%33%38%Read news stories23% 20%15%Research (new products, travel destinations, homework topics etc.)2021
2020
2019 21%18%12%Shop online 24%22%15%Viewpost to social media19%26%23%Stream media (music, videos etc.)
20%22%18%19%Play games11%8%0%10%20%30%40%50%60%70%80%90%100%Figure 8COUNTRY SPOTLIGHT69%of Spanish workers allow friends or family 
members to access their employer\-issued 
devices. This is nearly 25% more than the 
global average and a marked increase from 
last year (45%).48%of Australian workers grant others access to 
their employer\-issued devices, the least of 
any region surveyed.172022 STATE OF THE PHISHREPORTEmployee\-driven risk: the (even) bigger pictureCybersecurity extends beyond the inbox. It even transcends the professional and 
personal activities that employees do on their devices. From a risk perspective, 
how people do things is often more important than what they do.Think of it in terms of driving a car: theres some element of risk involved every 
time. But if someone drives recklessly (or doesnt know how to drive at all), the risk 
is much greater to that driver and to others on the road.Password management is one of these howsand its an ongoing struggle. 
Much of the issue comes down to a balance of convenience and security. 
Generally, convenience wins. The question is: how are working adults opting for 
convenience?We asked survey participants about password management habits for personal 
and work accountsand saw strikingly similar answers. This reinforces a point we 
often stress: cybersecurity skills are life skills, not work skills. They are portable.This cuts both ways. Skills and behaviors learned at work can be applied at 
homebut conversely, personal habits and shortcuts are likely to be a factor at 
work. Its one reason that ongoing training is so important. It gives people the 
confidence to recognize and value opportunities to make safer decisions for 
themselves at work and at home.Password Management Habits at Work and at HomeCOUNTRY SPOTLIGHTWork\-Related Password
Management Habits33%of U.S. workers save their login information 
in their web browser.27%of UK workers use a password manager.Use a unique password for each account38%of German workers manually enter a unique 
password for each account.16%of Japanese and Spanish users rotate 
between one and four passwords for their 
accounts. 30% 27%Save login information within a web browser 23% 25%Use a password manager 21% 20%Rotate 1\-4 passwords across accounts14%
14%Rotate 5\-10 passwords across accounts6%
7%Rotate more than 10 passwords across accounts6%
7%Work
Personal0%10%20%30%40%50%60%70%80%90%100%Figure 9182022 STATE OF THE PHISHREPORTExternal Wi\-Fi networks are another ongoing struggle for security teams. And with 
the significant increase in full\-time and part\-time remote workers, home Wi\-Fi is 
the elephant in the room.Nearly all survey respondents said they have a home Wi\-Fi network. But most are 
not taking key security precautions. That means many workers home networks 
are as susceptible as open\-access public Wi\-Fi.Wi\-Fi Security Measures on Home Networks60%26%26%password\-protect their 
home Wi\-Fi networkchanged the default name 
of their networkchanged their networks 
default Wi\-Fi password 
(network security key)22%18%11%changed their routers 
default passwordchecked for updates to 
router softwaretook none of these 
security measuresFigure 10Wi\-Fi\-based attacks assume proximitywhich can be difficult to achieve in 
targeted attacks. Still, its clear that many users dont have a strong grasp of 
fundamental Wi\-Fi practices. And with the increase in remote workers, home 
networks factor into organizational security more than ever. Small changes can 
minimize risk. So, if you havent advised your workforce on how to close security 
gaps in home Wi\-Fi, we suggest making the effort in 2022\.97%%of survey respondents said 
they have a home Wi\-Fi 
networkBUTOnly 60% said their network is 
password\-protected. KEY FINDINGAmong those with home Wi\-Fi networks, 
85% did not complete all the security 
measures we asked them about (11% said 
they dont do any of them). Of the 85%, 
62% said they havent taken some or all
of the precautions because they arent 
concerned about the security of their home 
Wi\-Fi network. Another 34% said they 
havent adjusted their security settings 
because they dont know how to.Of the 4% who offered another (write\-in) 
reason, we saw some common sentiments:Unnecessarydont need toDefault settingspasswords are alreadycomplexsecureAnother person (spousepartner,landlord) handles itToo inconvenientdont want toreconnect devicesNever thought about it192022 STATE OF THE PHISHREPORTCOUNTRY SPOTLIGHT91%of Spanish workers received at least
one suspicious communication in 2021\. 
49% saw a suspicious email attachment, 
and 20% got a suspicious message in
a work\-related messaging app.55%of U.S. workers admitted to taking a risky 
action in 2021\. 26% clicked an email link 
that led to a suspicious website,
and 17% accidentally compromised their 
credentials.Parting thoughts: risky business in 2021Like successful phishing attacks, users beliefs and behaviors dont exist 
in a vacuum. So we asked workers about cybersecurity\-related events they 
experienced in 2021\.Weve highlighted some key findings here, with more data (including country\-by\-
country breakdowns) in the Appendix. (Note: these are self\-identified by survey 
participants, so actual numbers could be much higher.)Cyber Events and Impacts: Key Findings83%received at least
one suspicious 
communication
in 202139% received an email that contained a suspicious attachment38% received a suspicious text message37% received a suspicious phone callvoicemail16% received a suspicious message in a work\-relatedmessaging app15% received an email impersonating their organization52%of U.S. workers experienced a cyberattack 
or fraud. 19% were victims of identity theft, 
and 17% paid a ransom to regain access to 
a personal device or data.42%19% clicked an email link that led to a suspicious website14% clicked a link in a direct message that downloaded malware13% accidentally downloaded malware from a maliciousemail or website12% gave personal information to a scam artistimpostortook a risky action11% accidentally compromised account credentials37%experienced a 
cyberattack or 
fraud14% said one or more of their social media accounts wascompromised12% said someone duplicated their social media account andattempted to impersonate them12% lost money because of a fraud committed against them11% were victims of identity theft10% paid a ransom to regain access to a personal device or dataFigure 11202022 STATE OF THE PHISHREPORT 
Spotlight: Security CultureTheres a lot of talk about security culture in the workplace today. And thats
a great thing. A strong security culture pays dividends. But getting there
isnt easy.The reality is that culturelike maturityis nebulous. Many things factor 
into it, and each organization is likely to interpret the term differently. And 
measuring gains (or losses) in cultural strength can be difficult.Still, some key dimensions to culture can (and should) be assessed on an 
ongoing basis. In particular, you should gauge employee perception of: Your organizations commitment to cybersecurity The role they should play in protecting your organization Their confidence level in identifying, reporting or acknowledging securityincidentsAssessing these factors can reveal obstacles to achieving a strong security 
culture. In part, it can show where disconnects between perceptions of 
security teams, executive teams and employees exist. This is something we 
saw in asking similar questions to our two different survey audiences.Level of Cybersecurity Priority Within the Organization15 42%65%Infosec and IT professionals
Working adultsHigh priorityPriority 28% 23%Somewhat a priority
 5% 18%Low priority2%
7%Not a priority
0%3%0%10%20%30%40%50%60%70%80%90%100%Figure 12KEY FINDING85%of infosec and IT survey respondents
said they had a positive perception of 
their organizations security culture.
14% indicated a neutral stance, and
just 1% had a negative perception.52%of working adults are confident or 
extremely confident that, should they 
have a cybersecurity\-related issue
with one of their work devices, their IT 
team could identify and address the
issue without their involvement.COUNTRY SPOTLIGHT\<45%of Japanese infosec and IT professionals 
said cybersecurity is a high priority for 
their organization.\>50%of Spanish and German working adults 
said cybersecurity is a high priority for 
themselves and their organization.15Some 7% of working adults said they were unsure of how their organization prioritizes cybersecurity.212022 STATE OF THE PHISHREPORTLevel of Cybersecurity Priority for Employees1650% 40%39% 29%Infosec and IT professionals
Working adultsHigh priorityPrioritySomewhat a priority8% 19%Low priority
2%
6%Not a priority
\<1%
2%0%10%20%30%40%50%60%70%80%90%100%Figure 13That 35% of infosec and IT professionals said cybersecurity is not a high 
priority for their organization is borderline alarming. But we see other key 
disconnects: Infosec and IT professionals have a more positive view of employeescommitment to cybersecurity than employees themselves do (89% priority
high priority vs. 69%) Working adults are more likely to say cybersecurity is a priority or ahigh priority for themselves than they are to say the same about their 
organization (69% vs. 65%) 10% of working adults believe cybersecurity is a low priority or not a priorityfor their organizationAnd among workers who indicated that cybersecurity is not a priority or is a 
low priority for them, we see key misconceptions: 32% said that since theyve never experienced any issues, they dont needto prioritize cybersecurity 27% believe their job is not high\-level enough to be a target of cyberattackers, so they dont need to worry about cybersecurity 22% feel they dont interact with devices often enough to be worried 19% believe their organization or IT team will take care of any securityneeds they have or mistakes they makeThese survey results cover many organizations, industries and regions. But 
they illustrate the value of understanding where the disconnects may be 
within your organization. Once you identify issues, you can begin to address 
them through clearer communication and targeted education.16For this question, infosec and IT professionals were asked their perception of cybersecurity priority 
for the average employee. Working adults were asked about the priority they personally place on 
cybersecurity. Note that 4% of working adults were not sure how to classify their personal commitment 
to cybersecurity.222022 STATE OF THE PHISHREPORTKEY FINDINGS11%average failure rate on phishing tests.33%average view rate of simulated attacks.FUN FACTOver the past 10 years, our 
customers have sent nearly 
275M simulated phishing 
emails to their users.Section 4Benchmarking: Failure Rates and 
Comparison DataOur customers actively tested their end users response to phishing emails over 
the course of our 12\-month measurement period. They sent nearly 100 million 
simulated attacks, an increase of more than 50% over 2020\. And they saw positive 
results: the average failure rate held steady at 11%, even with the increase in 
activity.17But as weve cautioned before, average failure rates dont provide the level of 
detail needed to fully assess risk. Nor do they allow organizations to adequately 
benchmark themselves against others who are running these types of tests.We dig into our data to provide you with better benchmarkingand to help you 
identify areas for improvement.Failure rates by template typeWithin our phishing simulation tool, customers can select from a variety of themes 
and lures among three primary template types: link\-based, data entry\-based and 
attachment\-based.This year, we saw a slight drop in the use of link\-based templates (65% vs. 68%) 
and an increase in the use of data entry\-based templates (26% vs. 23%). Use of 
attachment\-based templates remained the same year over year, with fewer than 
10% of tests falling into this category.This breakdown isnt necessarily misguided; more attacks use malicious links 
and lures designed to harvest credentials. But we saw plenty of attacks that used 
Microsoft Office and PDF attachments, among other file types, to deliver malware 
in 2021\. So the combination of low usage and high failure rates on attachment\-
based tests is noteworthy. (See the full comparison in Figure 14\.)17We calculate average failure rates at the organizational level rather than the user level, giving equal weightto each organizations average failure rate rather than equally weighting each users failure rate. This 
approach helps to eliminate the sway of large organizations and high\-volume programs, providing a more 
balanced view of failure data.232022 STATE OF THE PHISHREPORTFailed data\-entry tests refer to cases 
in which users submitted data after 
clicking a link in the simulated attack. 
Overall, the average click rate in data 
entry\-based tests was 12% and the 
average failure rate was 4%.Phishing Template Types: Frequency of Use65%26%9%LinkData EntryAttachmentPhishing Template Types: Average Failure Rates11%4%20%LinkData EntryAttachmentFigure 14You should assess your organizations approach to phishing simulations with 
this insight in mind. Also critical: understanding the types of attacks your 
organization and your users are facing, as well as how your employees work. If 
your organization sees a high number of emails with attachments (malicious or 
not), test and train users about this attack method. If your users widely assume 
that attachments are safe to interact with, attackersespecially those who use 
ransomwarecould easily exploit that.In general, simulated phishing programs should include a variety of templates 
across a variety of themes. We know attackers are adept and adaptive. Your 
security awareness training efforts should prepare your users to follow suit.242022 STATE OF THE PHISHREPORTKEY FINDINGSThe industries that ran the most phishing 
tests in 2021 were healthcare, financial 
services, energyutilities, manufacturing
and technology.Industry failure ratesMany organizations like to compare themselves to others in their industry. This 
year, weve expanded our reporting on industry performance to 25 industries 
(compared to 20 last year). Our data set per industry also increased over last year 
(see sidebar). This provides the most robust industry benchmarking weve offered 
to date.Overall, we saw some great year\-over\-year improvements on both ends of the 
spectrum. Last year, the lowest average failure rate was 9%; this year, its 8%.
And this years high mark of 14% bests last years 16%.Average Failure Rate by Industry1811% overall average 
failure rateEach industry represented in our 
failure rate comparison includes 
data from at least 20 organizations 
and at least 300,000 simulated 
phishing attacks (vs. 15 orgs and 
150,000 phishing tests last year).Automotive: 8%Electronics: 8%Engineering: 8%EntertainmentMedia: 9%Financial Services: 9%Education: 10%EnergyUtilities: 10%Healthcare: 10%HospitalityLeisure: 10%Manufacturing: 10%Food \& Beverage: 11%Government: 11%Insurance: 11%Legal: 11%Retail: 11%Transportation: 11%Agriculture: 12%Construction: 12%Mining: 12%Real Estate: 12%Technology: 12%Telecommunications: 12%Aerospace: 12%Business Services: 12%Consulting: 14%0%3%6%9%12%15%Figure 1518Look for industry failure rates by template type in the Appendix.252022 STATE OF THE PHISHREPORTKEY FINDINGSFacilities was last years worst\-performing 
department, tallying a 17% average failure 
rate. This year, they sit at a 9% average 
failure rate, a nearly 50% year\-over\-year 
improvement.Even two of this years worst\-performing 
departmentsquality and maintenance, 
each at 12%are ahead of their average 
failure rates from last year (14% and 15%, 
respectively).There is one notable bit of bad news: 
purchasing, last years best performer with 
a 7% average failure rate, dropped to join 
the lowest performers at 12%.Department designations 
represented in our failure rate 
comparison were used by at least 
85 organizations and include data 
on a minimum of 2,500 users (vs. 
40 orgs and 1,500 users last year).Department failure ratesPeople in key roles are targeted for different reasonsand a high position on 
an org chart is often not a factor. Distribution lists and aliases are also popular 
targets. These email addresses are frequently published publicly, and they carry 
the bonus of potentially reaching multiple people with a single send.Department\-level failure rates can help organizations pinpoint teams that are 
struggling with identifying and avoiding phishingand begin to address those 
vulnerabilities.With 25 departments19 now represented (vs. 20 last year), this years report 
provides even more opportunities for benchmarking. And like our industry 
comparisons, the department data set is more robust than ever.We saw some exciting improvements in the annual comparison. This years lowest 
average failure (6%) beats last years 7% mark. But the best news comes with the 
highest failure rate: 12% vs. last years 17%.Average Failure Rate by Department11% overall average 
failure rateAudit: 6%Information Technology: 6%Customer Service: 8%Logistics: 8%Security: 8%Administrative Services: 9%Communications: 9%Facilities: 9%Finance: 9%Legal: 9%Accounting: 10%Human Resources: 10%Management: 10%Marketing: 10%Research and Development: 10%Sales: 10%Supply Chain: 10%Warehouse: 10%Engineering: 11%Operations: 11%Production: 11%Project Management: 11%Maintenance: 12%Purchasing: 12%Quality: 12%0%2%4%6%8%10%12%Figure 16\.19Note that our customers self\-select department designations. As such, similar designations could mean 
different things across multiple organizations. For example, facilities and maintenance might overlap 
in one organization but have fully separate duties in another.262022 STATE OF THE PHISHREPORTSpotlight: Template ThemesAs we noted earlier, our customers have access to a frequently updated 
template library. They can test their users on a wide variety of themes,
topics, and tactics, including some of the latest threats our researchers
spot in the wild.On average, our customers sent out nine phishing campaigns over the
course of our 12\-month measurement period. Thats an increase from 
the eight\-campaign average we saw last year. This is a positive trend; we 
recommend testing users at least every four to six weeks (and, ideally, at
least once a month).In 2021, organizations heavily favored corporate\-themed phishing tests; 
more than 50% of templates used featured this theme. The emphasis was not 
misplaced. Many attackers used process and policy lures in their campaigns. 
We also saw a surge in attacks that abused cloud services that many 
organizations rely on for communication and collaboration.Here are the top 10 most\-used templates last year and 10 well\-used templates 
that proved trickiest for recipients (resulting in users taking the bait). This 
year, weve also included the average failure rate for each of the templates.The most\-used templates highlighted 
were sent to between 73,000 and
1\.5M users.The most successful templates 
highlighted were sent to a minimum 
of 10,000 users (and as many as
52,000 users).Some templates used in smaller\-scale 
campaigns (sent to fewer than 1,000 
users) had significantly higher failure 
rates. This includes a Tax Refund 
Notification template and a New 
Company Policy template, each of 
which topped a 70% failure rate.Most\-Used TemplatesTrickiest Templates1\.Voicemail from unknowncaller18%1\.Dress code update2\.Parcel arrival notice15%2\.Local holiday giveawaysand samples10%3\.Bonus review3\.Email password change:Urgent attention4\.Deactivation of oldOneDrive account5\.Missed Zoom meeting6\.Urgent Microsoft
2FA activation7\.Microsoft Teamsinvitation8\.O365 password 
expiration notice9\.Important information 
about queued email10\.Unusual account
sign\-in activity8%7%7%6%6%4%3%30%28%26%26%24%24%4\.Dennys food order5\.Important social media 
policy change6\.Updated EMR policy(healthcare)7\.Updated vacation policy24%8\.Urgent message re:dress code9\.Code of conduct: 
reported incident10\.Updated payrolltimetable23%23%22%Table 1Table 2272022 STATE OF THE PHISHREPORTOn average, our customers used 
two different templates within each 
simulated phishing campaign in 
1\. Using more than one template 
in a single campaign can help 
organizations avoid the so\-called 
prairie dog effect, which happens 
when one employee spots a test (or 
fails a test) and warns others about 
the email.A majority of the most\-used templates revolve around internal accounts and 
toolsand many of those have very low failure rates. This is why it pays to 
mix things up when testing users. Though most of the trickiest templates also 
mimicked internal communications, they used topics that are likely to draw 
an immediate and emotional response from recipients (like the two separate 
dress code templates).That emotional impact is reflected in the failure rates. The lowest among the 
most successful templates is still 20% higher than the highest failure rate 
among the most\-used templates (and more than seven times higher than the 
lowest failure rate).Granted, these types of triggering tests can be a hard sell with reviewers 
and approvers. And they may not be a good fit for every organizations 
culture. Regardless, the fact remains: attackers are not at all concerned about 
offending, frightening or tricking your employees. At the very least, users 
must be made aware that threat actors are freely using these types of lures 
and tactics, even if you dont use them in simulated phishing emails.282022 STATE OF THE PHISHREPORTAMONG ORGANIZATIONS THAT
USE OUR PHISHALARM EMAIL 
REPORTING TOOL15%overall average reporting rate
(up from 13% last year).10%overall average failure rate
(down from 11% last year).1\.5overall average resilience factor
(up from 1\.2 last year).AVERAGE REPORTING RATE BY 
TEMPLATE TYPE18%for attachment campaigns.17%for data entry campaigns.16%for link\-based campaigns.Section 5Email Reporting and Resilience: 
Measurements and GoalsEmail reporting: a critical part of your cyber defensesReporting tools are a relative newcomer to the security arsenal. Many organizations have 
not implemented an easy\-to\-use, in\-client reporting tool like PhishAlarm.If we could shout it from the rooftops, we would: email reporting is critical to both 
defending against cyber attackers and evaluating effectiveness of your security 
awareness training efforts.We encourage all of our customers to implement our PhishAlarm in\-client reporting 
button, because it:Allows users to actively participate in email defensesAlerts security teams to suspicious, malicious and nuisance emails that evade filtersPromotes a collaborative relationship between users and security teamsEnables you to correlate failure rates and reporting rates to gauge resilienceEnables you to integrate of reporting and remediation functions, simplifying andaccelerating identification and removal of active email\-borne threatsCalculating resilienceAmong customers who use our PhishAlarm button, the average overall reporting 
rate on simulated attacks in 2021 was 15%, up from 13% last year. The overall 
average failure rate among these organizations was 10%, down from 11% last 
year. Both of these are positive signs in general, especially in terms of resilience.Last year, we introduced the concept of a resilience factor. An organizations 
resilience factor is a measurement of simulated phishing reporting rates in 
comparison to failure rates. The first goal is to achieve a resilience factor greater 
than 1, which means more people are reporting than failing. Last year, our 
PhishAlarm customers overall resilience factor was 1\.2\. This year, we saw a
25% improvement:15% average reporting rate 10% average failure rate\= 1\.5 resilience factor292022 STATE OF THE PHISHREPORTTIPIf your organizations failure 
rate is higher than your 
reporting rate, calculate your 
resilience factor by inverting 
the equation and adding a 
negative sign to the result.A resilience factor of 1\.5 is clearly not ideal. But the year\-over\-year improvement is 
a step in the right direction.The ultimate goal is to increase resilience over time, which happens through 
improvements in users responses to phishing tests. Higher reporting rates are a 
sign that users are paying more attention to the emails theyre receiving and are 
taking intentional action to help protect your organization.While lower failure rates can also be a positive sign, not clicking a simulated 
phishing email is not the same thing as actively rejecting it. Phishing tests might 
be ignored or avoided for any number of reasons, not just because users believe 
them to be suspicious.We reiterate our advice from the past couple of years: work toward the stretch 
goals of an overall reporting rate of 70% and an overall failure rate of 5%an 
overall resilience factor of 14\. This would put you in the very positive position 
of having a user base thats 14 times more likely to report a phishing test than 
engage with one. That attention to detail will pay off when real\-world phishing 
attacks evade your perimeter defenses.It bears repeating that we consider a 705 ratio to be a stretch goal. Its not 
something that will happen overnight.Still, we regularly see customers campaigns meeting or surpassing these marks. 
So, its achievable. Yes, its more easily achieved on individual campaigns. But 
we see organizations sustaining even higher resilience factors across multiple 
campaigns. So its also repeatable.As with all security awareness training initiatives, youll need to be patient 
and allow for improvements to come. To make gains, email reporting must 
carry weight within your organizationfrom both a training and measurement 
perspective.Consider these key actions: Coach users about reporting. Its not enough to simply give them access to areporting tool. They need to know how to find it and how to use it. Communicate about the positive impact user\-reported emails can makewithin your organization. A reporting tool empowers users to help stop cyber 
attacks. That is compelling. Train users about when to report. And allow time to grow their confidence intheir ability to identify and take action on suspicious messages. If necessary, shift organizational focus away from failure rates as theultimate indicator of phishing awareness. Become an internal advocate for 
reporting and emphasize reporting rates in metrics that are socialized internally. Share successes with users, too. Highlight real\-world phishing attemptsreported by employees. These stories both reinforce the positive impacts of 
reporting and remind employees that they can make a difference when they 
apply what they learn in your security awareness training program.302022 STATE OF THE PHISHREPORTKEY FINDINGSLast years single highest reporting 
rate20%, achieved by the financial 
services industrywas matched or
beaten by nine industries this year 
(including financial services, which
reached a 23% reporting rate).Last year, six industries had a negative 
resilience factor (more users failed than 
reported phishing tests). This year, just 
oneeducationwas in negative territory. 
But even that industry saw an improvement 
over 2020 (\-1\.3 vs. \-2\.0\).Just four industries had a reporting rate
of 10% or lower this year, compared to
nine in 2020\.Benchmarking: industry resilience factorsAs noted earlier, we know organizations are eager to level\-set their performance 
against more granular measurements than overall failure and reporting rates. Our 
industry\-based reporting and resilience analysis supports those efforts. As with 
our earlier set of industry comparisons, weve expanded our coverage to include 
25 industries this year.In Table 3, we present each industrys average reporting rate, failure rate, and 
resilience factor. Youll note that the failure rates in this section may vary slightly 
from those in Figure 15\. The average failure rates seen here are based on 
customers who use both our phishing simulations and our PhishAlarm button, a 
smaller subset of the data used earlier.Industries are ranked in order of reporting rate, highest to lowest.Industry Reporting, Failure and Resilience DataIndustryAerospaceElectronicsEnergyUtilitiesFinancial ServicesLegalAgricultureInsuranceConsultingEngineeringConstructionReal EstateAutomotiveManufacturingGovernmentMiningBusiness ServicesEntertainmentMediaRetailTelecommunicationsHealthcareTechnologyFood \& BeverageTransportationEducationHospitalityLeisureReporting
RateFailure
RateResilience
Factor26%26%24%23%23%22%21%20%20%18%17%16%16%13%13%12%12%12%12%11%11%10%8%6%5%Table 36%8%7%6%6%7%8%10%7%8%11%10%7%7%6%12%5%8%9%7%7%8%6%8%4%4\.33\.33\.43\.83\.83\.12\.62\.02\.92\.21\.51\.62\.31\.92\.21\.02\.41\.51\.31\.61\.61\.31\.3\-1\.31\.3312022 STATE OF THE PHISHREPORT 
Worried that user\-reported emails will 
overwhelm your remediation team? 
Solutions like our Closed\-Loop Email 
Analysis and Response (CLEAR) can 
Worried that user\-reported emails will 
help streamline management of abuse 
overwhelm your remediation team? 
mailboxes, using automation and advanced 
Solutions like our Closed\-Loop Email 
email security features to cut operational 
Analysis and Response (CLEAR) can 
overhead. 
help streamline management of abuse 
mailboxes, using automation and 
advanced email security features to cut 
operational overhead.Real\-world phishing and reporting accuracyOver our one\-year measurement period, we saw the immense value in allowing 
users to actively participate in email defenses. Our customers employees spotted 
and reported many active threats, including emails that contained malware 
affiliated with nation\-state and financial APTs. They alerted infosec teams to: More than 350,000 credential phishing emails Nearly 40,000 emails with malware payloads like Trojans, downloaders,stealers, keyloggers and ransomware More than 20,000 malicious spam emails More than 8,500 emails associated with botnets or spambots More than 8,000 attacks using remote access or banking Trojans More than 6,000 attacks containing downloadersThis year, weve also analyzed reporting accuracy data. This is calculated for 
PhishAlarm customers who also use PhishAlarm Analyzer. Email reporting is even 
more effective when paired with real\-time analysis. Tools like PhishAlarm Analyzer 
use advanced machine learning, behavioral insights and sandboxing to quickly 
analyze reported messages.In this process, we can definitely auto\-classify between 60% and 80% of user\-
reported messages as maliciousspam or bulkbenign. Using a tool like CLEAR 
(see sidebar), those classifications can be tied to an automated action such as 
removing the message and similar threats, resetting user credentials or closing 
the case (if the email is benign).The accuracy rates shown in Table 4 reflect the percentage of messages sent 
to Analyzer that were classified as malicious, suspicious or spam. (Messages 
classified as bulk, low risk or unknown are not factored into accuracy rates.)20Even the lower accuracy rates we see here have value: at least 2 of every 10 
messages reported had evaded perimeter defenses. Naturally, a higher accuracy 
rate is more favorableand its a great metric to evaluate over time because it 
reflects users ability to distinguish problem emails from safe ones.We suggest targeting an accuracy rate of 50% or higher, which would indicate that 
most of the messages your users are reporting are spam or potentially malicious, 
rather than innocuous. But like resilience, its a metric that requires time and 
patienceand a focused effort to assess your users weaknesses and provide 
the right training. If you have a tool like CLEAR, your remediation teams wont be 
overtaxed as reporting accuracy is given space to improve.3220Note that simulated phishing attacks, when reported, are not forwarded to PhishAlarm Analyzer. So, bydefault, simulated phishing reports are not factored into accuracy ratings.2022 STATE OF THE PHISHREPORTIndustryLegalEngineeringEducationGovernmentAgricultureReal EstateBusiness ServicesEntertainmentMediaInsuranceManufacturingConstructionElectronicsFinancial ServicesHospitalityLeisureTelecommunicationsEnergyUtilitiesTechnologyTransportationAerospaceFood \& BeveragesConsultingHealthcareRetailAutomotiveMiningReporting Accuracy Rates by IndustryAccuracy Rate45%42%41%36%35%35%34%34%34%34%33%32%32%32%32%30%30%30%29%29%29%28%27%26%22%33Table 42022 STATE OF THE PHISHREPORT99%of organizations have a security 
awareness training programBUT
Only 57%provide organization\-wide trainingAND
Only 85%educate employees who fall for real or 
simulated phishing attacks.Section 6Security Awareness Training:
Insights and OpportunitiesUnderstanding of industry trends, employee knowledge gaps and benchmark 
data wont do much for you if you dont act on what you learn. Security awareness 
training is a must for organizations across the globe. And security frameworks and 
compliance requirements shouldnt be the only things driving you to make it part 
of your defense\-in\-depth strategy.The good news is that nearly everyone is doing something to educate employees: 
99% of the infosec and IT professionals we surveyed said their organization has 
a security awareness training program. The bad news? How programs are being 
implemented leaves much room for improvement. (And as we noted earlier:
from a risk perspective, how people do things is often more important, than what 
they do.)Here are some areas of concern revealed in our global survey: Fewer than 60% of organizations deliver organization\-wide training. Nearly 30% 
focus their efforts strictly on specific departments and roles, and another 15% 
are only concerned about specific individuals. Fewer than 50% of organizations formally cover email\-based phishing in their 
training programs, and just 43% cover ransomware. In comparison, more than 
80% of organizations experienced at least one successful phishing attack in 
2021, and nearly 70% dealt with at least one ransomware infection. (See more 
on topics later in this section.)COUNTRY SPOTLIGHT 81% of organizations said that more than half of their employees are workingremotely (either part time or full time) due to the pandemic. But just 37% 
educate workers about best practices for remote working. Only 34% educate employees about best practices for email reporting. Nearly 15% of organizations do not educate workers who interact with real orsimulated phishing emails. (And just to be clear: we consider this to be too large 
a number.)68%of French organizations deliver
organization\-wide training, the highest
of any region surveyed.45%of Japanese organizations train only
specific departments and roles
(60% higher than the global average).23%of Spanish organizations train only
specific individuals, followed closely
by Australian organizations (22%).342022 STATE OF THE PHISHREPORT73%of organizations deliver 
formal security awareness 
training to their employees 
(via computer\-based, 
in\-person or instructor\-led 
virtual training).COUNTRY SPOTLIGHT37%of Australian organizations use simulated 
phishing attacks, the least of any region 
surveyed. But they are by far the most 
active in using them: 61% said their 
organization sends phishing simulations 
daily.37%of UK organizations simulate malicious USB 
drops, the most of any region surveyed. But 
this represents fewer than half of UK orgs 
that faced USB\-based attacks in 2021\.\<25%Training tools and frequency of useSecurity awareness training programs should use several different toolsvariety 
is your friend when it comes to educating users. A mix of tools will not only help 
to keep employees engaged, it will also help you learn different things about the 
people you rely on to protect your organizations data, devices and systems.Variety also helps apply key learning principles to your program: reinforcement 
and repetition. Reaching users in multiple ways and keeping cybersecurity a 
relevant and palatable conversation are critical.Dont focus just on teaching and testing. Friendly reminders, notes about trending 
threats, and even program performance newslike big saves when employees 
report real\-world phishoffer opportunities to show how important cybersecurity 
is to your organization and plant the seeds for a strong security culture.Nearly 75% of organizations said they assign what we consider to be formal 
training to their users (note that more than one answer was permitted): 43% deliver computer\-based training 38% provide in\-person training 35% offer virtual, instructor\-led trainingFormal education sessions were, by far, the most used component of security 
awareness training programs in 2021, according to survey participants. Other 
tools, and their percentage of use, include: Simulated phishing emails (41%) Newsletters or informative emails (39%) Awareness posters or videos (35%) Smishing andor vishing simulations (33%) Internal cybersecurity chat channel (32%) Cybersecurity\-based contests and prizes (30%) Simulated USB drops (28%) Internal cybersecurity wiki (26%)of Spanish and German organizations use 
gamification techniques like contents and 
prizes, the least among all regions surveyed.Just 14% of organizations that use formal training said they train users only once 
or twice a year. Ideally, this number would be 0%. Still, the trend toward more 
frequent training is a positive one.We saw some indications that organizations could be using formal training and 
phishing simulations too frequently (more on that to follow). But on the other end 
of the spectrum, we also saw 38% organizations saying they allocated an hour or 
less to formal training in 2021 (vs. 28% in 2020\).352022 STATE OF THE PHISHREPORT5%9%14%15%Frequency of 
Formal
Training23%1%4%16%21%Frequency of 
Phishing
Simulations34%27%31%DailyWeeklyMonthlyQuarterlyTwice a yearOnce a yearFigure 17Figure 1812%13%9%Time
Allocated to 
Formal 
Training 
Sessions in
a Year37%29%Figure 1930 minutes or less31 to 59 minutes1 to 2 hours2 to 3 hoursMore than 3 hoursThe key is balance. Yes, we believe cybersecurity must be talked about frequently. 
And security awareness and training initiatives should be an ongoing pursuit that 
allows skills to develop consistently over time. But an overabundance of anything 
extra is not likely to be well\-received by users. Training fatigue is a legitimate 
concern.We recommend a blend of formal, computer\-based training assignments (done 
at least quarterly) and monthly phishing simulations. These should be paired with 
regular use of supporting materials and activities like posters, flyers, newsletters 
and lunch\-and\-learn sessions.Ultimately, it might take some time to comfortably identify the appetite for training 
among your user base. For example, you may find that microlearning modules 
(those that offer about 1\-3 minutes of bite\-sized training) are better received 
by your users than longer, more intense training. And that may pave the way to a 
monthly training schedule vs. a quarterly one.One thing to always keep in mind: attackers are putting in time and effort to 
identify and compromise your employees. Organizations that dont allocate time 
and effort to security awareness training in a way thats most likely to resonate 
with their people will be at a disadvantage.362022 STATE OF THE PHISHREPORTCOUNTRY SPOTLIGHTAustralian organizations lagged behind their 
global counterparts (and global averages) 
on coverage of several key security 
awareness training topics:37%cover email\-based phishing.35%cover mobile device security.35%cover ransomware.29%cover BEC.29%cover cloud\-based threats.29%cover internet safety.27%cover malware.Orgs ignore too many important topics when
training usersOf the 99% who said their organization has a security awareness training 
program, all but one Japanese survey respondent said their program covers 
at least one of the topics we surveyed about. But both globally and regionally, 
theres not nearly the breadth or depth of coverage needed to prepare users to 
defend against more sophisticated threat actors, who frequently use multiple 
techniques and tactics in a single attack campaign.Topics Covered in Security Awareness Training Programs49%47%44%43%43%42%40%40%39%37%36%34%33%33%32%Email\-based phishingMalwareWi\-Fi securityRansomwareMobile device securityPassword best practicesBest practices for internet safetyBECinvoice fraudCloud\-based threatsBest practices for remote workingPhysical security measuresBest practices for email reportingCompliance\-related topics (GDPR, PCI, etc.)Insider threatsMulti\-factor authenticationSocial engineeringSmishingRole\-based trainingVishing27%26%25%23%0%10%20%30%40%50%Figure 20372022 STATE OF THE PHISHREPORTKEY FINDINGS55%of organizations take disciplinary action 
against employees who fall for real or 
simulated phishing attacks, the same 
percentage as last year.24%of organizations said a consequence model 
is not the right fit for their organizations 
culture (a new response choice this year).70%of those who employ a consequence model 
said it has increased employee awareness 
of phishing, a 15% year\-over\-year drop. 
25% said awareness is about the same, and 
4% feel awareness has decreased since the 
introduction of consequences.Consequence models: could they cost you?Here are some stats we dont love: More than half of the infosec and IT professionals we surveyed said their 
organization disciplines or punishes employees who interact with real or 
simulated phishing emails. Another 4% said the launch of a consequence model is imminent within their 
organization, and an additional 14% said theyre considering the approach. Among those using a consequence model, more than 95% said that both realand simulated attacks trigger consequences within their organization.Nearly three\-quarters (73%) of survey respondents seem comfortable with the 
idea of punishingdisciplining (two words we used in our survey) employees for 
their mistakes in handling email. Thats concerning enough. Its even more vexing 
when you consider these points: Just 49% of survey respondents said their organization covers email\-basedphishing in their security awareness training program Only 25% said their organization allocates two or more hours to formalemployee training each year. Sometimes one mistake by a user is all it takes to trigger a consequence, even 
when the mistake is made in handling a hypothetical threat to the organization.As we did last year, we excluded training from the list of punishments within 
consequence models. Thats because training should never be presented to users 
as a punishment. Training is an opportunity to learn and improve. And it should 
always be positioned as a positive experience, not a negative one.FOR YOUR CONSIDERATIONTechnical safeguards that are purpose\-built to identify and block phishing threats 
arent perfect 100% of the time. Is it fair to ask employees who are not cybersecurity 
experts to be perfect or be punished?382022 STATE OF THE PHISHREPORTGLOBAL LEADERS\>75%of Australian and UK organizations use a 
consequence model73%of U.S. organizations ask managers to 
counsel employees56%of Australian organizations ask their HR 
teams to enforce certain disciplinary actions42%of UK organizations impose a monetary 
penalty (62% higher than the global 
average)39%of Spanish organizations said a 
consequence model isnt a cultural fit, 
followed closely by German organizations 
(37%)25%or more of UK, U.S and Spanish 
organizations include termination in their 
consequence models (vs. \~10% of
German and Japanese organizations)COUNTRY SPOTLIGHT26%of German organizations have a 
consequence for users who fail a single 
phishing simulation.38%of U.S. organizations punish users who fall 
for one real\-world phishing attack.Figure 21 shows the disciplinary actions that are used within our survey 
respondents organizations, and Figure 22 breaks down the thresholds that 
trigger the first consequence.Consequences for Interacting with Real or Simulated Phishing AttacksOne\-on\-one discussion with manager60%59%52%45%One\-on\-one discussion with a member of the infosec teamImpact to employees yearly performance reviewsHR\-enforced disciplinary actionsRemoval of access to systemsMonetary penaltyTermination26%18%35%0%10%20%30%40%50%60%Figure 21Figure 22 illustrates that its not just repeat offenders who are being punished 
for their email actions. And Figure 23 shows that many organizations are just as 
eager to introduce consequences as they are to launch a security awareness 
training program.The First Action That Triggers a Consequence2140%35%30%25%20%15%10%5%0%16%35%33%23%24%23%Simulated PhishingReal\-world Phishing11%8%5%4%6%4%2% 2%1 failure2 failures3 failure4 failures5 failuresMore than 5 failuresUnsureFigure 2221Just 3% of respondents said that phishing test failures do not result in a consequence. Only 1% said thatfalling for a real\-world phishing attack doesnt trigger a consequence.392022 STATE OF THE PHISHREPORTCorrelation of Consequence Model Launch to
Launch of Security Awareness Training ProgramLaunched at the same time as security awareness training45%Launched within 6 to 12 months of security awareness training launch35%Launched within 1 to 2 years of security awareness training launch14%Launched more than 2 years after security awareness training5%Launched a consequence model without offering security awareness training
\<1%0%10%20%30%40%50%Figure 23Some organizations feel they must punish users for their email mistakes. And if 
handled with careful consideration and clear communication, a consequence 
model may prove beneficial in some cases.But its a slippery slope. Many organizations have found there are limited options 
for delivering consequences in a fair, consistent and legally sound way.And as found in our survey, many employees are not receptive to consequence 
models. This sentiment can hurt an organizations overall culture, leaving 
employees less engaged, less responsive and less likely to want to participate in 
cybersecurity initiatives.Users Response to Consequence ModelKEY FINDINGAt 62%, Spanish organizations were most 
likely to say that employees understand and 
accept the use of a consequence model. But 
theyre also most likely to say that, in spite 
of many complaints, the organization is firm 
in their belief that consequences are the 
right approach to take (28%).1%37%21%20%Widespread acceptanceMixed responseMany complaints 
(organization working to address)Many complaints 
(organization firm in maintaining approach)21%Unsure of users responseFigure 24402022 STATE OF THE PHISHREPORT72%of infosec and IT 
professionals surveyed said 
their organizations current 
security awareness training 
program has lowered phishing 
failure rates.COUNTRY SPOTLIGHT84%of U.S. organizations said security 
awareness training has reduced phishing 
failure rates, the highest of any region 
surveyed.6%of Japanese organizations say phishing 
failure rates have increased since the 
implementation of their current security 
awareness training program, twice the 
global average.Section 7Making It Personal: Identifying 
Vulnerabilities, Gauging SuccessWeve analyzed a lot of information for this years report and provided more 
(and more robust) benchmarking data than ever. But we get that it can be 
overwhelmingmuch like running a security awareness training program itself.Just over 70% of the infosec and IT professionals we surveyed said theyve seen 
a reduction in phishing failure rates since launching their organizations security 
awareness training program. (Another 24% said phishing susceptibility has stayed 
about the same, 3% said failure rates are higher, and 1% werent sure how training 
has impacted failure rates.) The good news: based on our findings, there is a lot of 
opportunity to run these programs more effectively.Here are three key steps you can take to that end:1\.Prioritize the things that are important withinyour organizationHeres a key belief of ours: Everyone who can influence your organizations 
cybersecurity posture should be trained in cybersecurity best practices. 
Everyone should have a foundational understanding of common 
cybersecurity threats and practical defense measures. Everyone who touches 
your network and data, everyone who handles your equipment, everyone who 
manages or controls access to organizational assets. Everyone.Just 57% of the infosec and IT professionals we surveyed said they take this 
approach (and that number hovers around 50% for Japanese, Spanish and 
Australian organizations). Too many people who contribute to cybersecurity 
risk are being left out of training.Still, that doesnt mean you cant be deliberate and strategic about how 
you assess and train your people. And it doesnt mean that everyone has 
to receive the exact same training at the exact same time. And it certainly 
doesnt mean that your program should replicate that of an organization in 
another industry (or even that of direct competitor).Your program should prioritize topics you know are relevant to your industry 
and your organizationand the people who work within it. The following 
information can help you determine what to cover and with whom: Knowledge levels across your user base, including those who struggle to 
understand basic concepts vs. those who exhibit more advanced skills Known, wider\-spread issues within your organization (for example,credential compromise, problems with lost devices, BYOD concerns or 
improper use of cloud accounts) Compliance, regulatory or contractual training requirements412022 STATE OF THE PHISHREPORT Specific job functions that are a threat to your organization if handledincorrectly (for example, paying invoicesexecuting wire transfers, managing 
confidential customer or employee data, accessing high\-risk websites) High\-visibility roles within your organization (for example, executives,spokespeople and influencers) Department\-level failure rates on phishing simulations Benchmark data and insights from others in your industry2\.Use threat intelligence to your advantageThreat intelligence can help you determine a key piece of information: when 
to deliver specific training to specific people.High\-level threat intelligence shared publicly or privately is invaluable. This 
may include the information we deliver on the Proofpoint Threat Insight blog, 
our Threat Hub or in our customer\-facing Threat Alerts and Attack Spotlights.But its just as critical to understand the people and departments within your 
organization that are being attacked and targeted at any given time, and the 
ways attackers are trying to compromise your organization.More than 90% of infosec and IT survey respondents said their organizations 
threat intelligence influences security awareness training decisions. But how 
that happens could use some work.We were glad to see gains in all three of the areas we surveyed (see Figure 
25\). But ideally, many more organizations would be taking advantage of 
knowledge about their specific threat landscape and using that to inform their 
training approach.Use of Threat Intelligence93%of organizations factor threat 
intelligence into their security 
awareness training plans (up 
from 90% last year).COUNTRY SPOTLIGHT71%of Spanish organizations train about topics 
that relate to attacks they know their 
organization is facing.60%53%43%train users about topics 
that relate to known 
attacks on their 
organizationuse phishing simulations 
that mimic trending 
threatsFigure 25deliver specific training to 
people who are being 
targeted by certain types 
of attacks67%of U.S. organizations use phishing tests that 
mimic trending threats.53%of UK organizations train individuals they 
know are being targeted by specific types of 
attacks.14%of Japanese organizations do not adjust 
training based on threat intelligence, and 
another 4% say they do not have access to 
threat data.422022 STATE OF THE PHISHREPORTIn 2021, we added a CISO Dashboard to our Security Education Platform. A key feature of that dashboard is the User Vulnerability 
Summary, which identifies key indicators of vulnerability among an organizations employees. Customers can view users with low 
participation rates and low performance rates. Those who leverage Proofpoint Targeted Attack Protection (TAP) can also identify their 
organizations Very Attacked People (VAPs) and Top Clickers.To improve the effectiveness of your security awareness training program, we 
suggest identifying the following: The individual and group inboxes that are being sent the largest 
number of suspicious and malicious messages. We refer to these 
individuals and inboxes as Very Attacked People (or VAPs). These users 
are sometimes VIPsbut often, theyre not. And your organizations VAPs 
can change a lot over time. Trending attack characteristics. Attack intensity and methodology can 
change over time, just as VAPs can. Examining the how behind the what 
can reveal vital information. For example, suppose threat intelligence shows 
an increase in credential harvesting attempts targeting specific people and 
groups. With the right intel, you can quickly communicate that insight and 
deliver training tailored to reduce specific risks. Vulnerable users. Being able to identify specific people who have fallen 
for real or simulated phishing attacks and the lures they fell for can be 
incredibly valuable. The intersection of vulnerability, attacks and privilege. This is what we 
like to call the perfect storm: privileged users within your organization
who are vulnerable to attack and are being actively targeted. These are the 
risks to know aboutand address. (The User Vulnerability Summary in our 
CISO Dashboard helps our customers do this. See the callout on this page 
for more.)432022 STATE OF THE PHISHREPORTSecurity Program Effectiveness: 
Ranking by industry3\.Evaluate key security awareness training metricsto gauge successYou should not hinge your view of success on a single measurement (like 
phishing test failure rates). And benchmark data should neither induce panic 
within your organization nor give you a false sense of security.As with a security awareness training program itself, success measurement 
should include multiple components and take individual organizational factors 
into account.To help organizations better gauge how effective their programs are, we 
introduced a new feature in our Security Education Platform in 2021: the CISO 
Dashboard. In addition to at\-a\-glance views of user vulnerability (see callout 
on page 43\), this dashboard displays and aggregates key performance and 
participation indicators that help drive decision\-making.Our overall Security Program Score provides a holistic review of an 
organizations security awareness program and its results. The overall score 
factors in the following:1\. Phishing simulation failures2\. Phishing simulation reporting3\. Knowledge assessments4\. Reported email accuracy5\. Training participationThis type of high\-level view helps organizations gauge the relative health of 
their security awareness training program and improvements over time. It
also helps with decision\-making, course corrections and program planning.After all, a security awareness training program should be an ongoing 
initiative. Where you are today isnt where youll be in a year. As threats, 
knowledge levels and key metrics evolve, your program should adapt
with them.With that in mind, we leave you with a final ranking: overall program 
effectiveness by industry. This ranking, shown in Table 5, is based on 
participation and performance across all five aspects of security awareness 
training listed above.1\.Engineering2\.Financial Services3\.Aerospace4\.EnergyUtilities5\.Manufacturing6\.Legal7\.Telecommunications8\.Consulting9\.Construction10\. Insurance11\.Electronics12\. Mining13\. EntertainmentMedia14\. Automotive15\. Food \& Beverages16\. HospitalityLeisure17\.Technology18\. Transportation19\. Agriculture20\. Education21\. Real Estate22\. Business Services23\. Government24\.Healthcare25\. RetailTable 5442022 STATE OF THE PHISHREPORTSection 8AppendixA.Infosec and IT security survey: country\-by\-country breakdownAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageHow many of these cyberattackssuccessful and unsuccessfuldid your organization experience in 2021?Bulk phishing attack (same email sent to multiple people)01\-1011\-2526\-5051\-100100\+Unsure of total10%46%18%10%8%6%2%Spear phishingwhaling (targeted email attack)01\-1011\-2526\-5051\-100100\+Unsure of total8%18%48%12%8%4%2%12%41%20%14%8%5%0%14%39%16%15%13%2%1%15%20%26%18%11%6%4%16%26%24%12%16%2%4%Business email compromise (for example, wire transfer fraud or invoice fraud)01\-1011\-2526\-5051\-100100\+Unsure of total10%30%24%26%4%4%2%25%29%22%17%6%1%0%25%22%14%21%10%5%3%22%30%14%16%6%8%4%40%28%14%8%8%0%2%36%24%10%6%12%8%4%11%49%17%15%2%6%0%26%32%22%5%9%5%1%23%33%19%14%4%7%0%9%33%13%23%12%9%1%18%29%25%18%3%7%0%19%25%20%19%9%7%1%17%36%18%11%8%9%1%23%20%29%15%5%7%1%21%26%24%11%9%7%2%14%36%18%15%8%7%2%21%27%25%12%9%4%2%23%27%19%16%8%5%2%452022 STATE OF THE PHISHREPORTEmail\-based ransomware attack (ransomware payload delivered via email)AustraliaFranceGermanyJapanSpainUKU.S.Global 
Average01\-1011\-2526\-5051\-100100\+Unsure of totalSmishing (SMStext message phishing)01\-1011\-2526\-5051\-100100\+Unsure of totalVishing (voice phishing via phone calls)01\-1011\-2526\-5051\-100100\+Unsure of total10%14%36%24%8%8%0%8%24%26%22%12%8%0%8%22%30%30%8%2%0%20%31%24%10%13%2%0%29%23%14%26%5%3%0%31%26%20%11%10%2%0%20%32%13%16%13%3%3%27%19%16%18%9%7%4%34%20%15%12%11%4%4%USB drops (thumb drives weaponized with malicious software or code)01\-1011\-2526\-5051\-100100\+Unsure of total10%18%30%24%8%10%0%38%22%15%17%6%2%0%Social media attacks (for example, pretexting or account takeover)01\-1011\-2526\-5051\-100100\+Unsure of total468%22%36%14%10%10%0%23%26%19%15%13%4%0%36%19%13%14%9%5%4%26%17%18%16%11%8%4%32%26%22%8%8%2%2%26%38%6%10%14%2%4%44%24%10%8%8%2%4%48%24%14%6%6%0%2%42%18%18%4%10%2%6%32%37%8%8%9%5%1%43%21%21%5%6%4%0%51%22%15%6%2%4%0%59%15%15%7%3%1%0%45%22%12%10%8%3%0%16%28%21%18%9%7%1%20%16%20%19%13%11%1%22%20%21%16%15%6%0%22%20%19%21%10%8%0%15%24%15%24%9%13%0%22%25%21%17%9%5%1%25%16%24%13%11%10%1%28%19%27%10%7%9%0%37%19%19%9%11%5%0%25%22%19%15%10%7%2%22%28%21%14%10%4%1%26%23%18%16%10%6%1%31%22%20%13%9%4%1%36%19%18%14%8%4%1%26%21%20%14%10%7%2%2022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageHow many SUCCESSFUL phishing attacks did your organization experience in 2021?01\-34\-67\-910 or moreUnsure of total8%14%38%16%20%4%12%30%32%17%8%1%20%28%21%12%15%4%34%26%22%12%6%0%What impact(s) did successful phishing attacks have on your organization in 2021?Loss of dataintellectual propertyBreach of customerclient dataCredentialaccount compromiseRansomware infection (email payload)Other malware infection(s)Financial losswire transfer fraudAdvanced persistent threatZero\-day exploitWidespread outagedowntimeReputational damageFinancial penalty (e.g regulatory fine)Im not sure52%64%57%61%36%30%30%18%20%27%14%2%51%49%52%40%25%20%16%13%22%21%7%1%50%57%46%49%28%14%17%14%22%22%8%0%24%48%42%45%27%3%9%0%12%15%3%6%18%36%26%11%8%1%25%42%38%33%15%9%14%14%19%17%5%2%9%26%27%24%13%1%57%57%58%50%30%29%24%29%28%33%24%1%21%20%25%23%9%2%52%60%43%40%28%18%19%17%34%29%18%1%Did your organization experience any ransomware infections (due to email, later\-stage malware delivery, etc.) in 2021?YesNoIm not sure80%20%0%81%17%2%54%42%4%50%48%2%How many SEPARATE ransomware infections did your organization experience?1\-34\-67\-910 or moreUnsure of total18%47%5%30%0%35%39%19%7%0%35%35%9%21%0%48%24%20%4%4%Did your organization pay any ransoms to resolve a ransomware infectionattack in 2021?YesNoIm not sure80%20%0%56%43%1%65%33%2%20%80%0%62%33%5%48%32%15%5%0%39%61%0%78%21%1%25%32%24%18%1%82%18%0%72%25%3%31%35%22%12%0%64%36%0%17%26%27%16%11%2%44%54%48%46%27%17%18%15%22%24%11%2%68%29%3%34%35%16%14%1%58%42%\<1%472022 STATE OF THE PHISHREPORTThinking of the most recent payment made, what happened?AustraliaFranceGermanyJapanSpainUKU.S.Global 
Average53%69%54%40%37%69%54%54%41%20%37%20%42%28%39%32%Paid one ransom and regained access 
to datasystemsPaid an initial ransom and follow\-up 
ransom(s) and got access to data
systemsPaid an initial ransom, refused to pay 
more, and did not get access to dataNever got access to data, even after 
payingIm not sure3%0%3%4%7%0%9%0%0%20%21%20%0%98%2%Does your organization run a security awareness training program?YesNo98%2%100%0%97%3%Which of the following topics are covered in your security awareness training program?Email\-based phishingMalwareWi\-Fi securityRansomwareMobile device securityPassword best practicesBest practices for internet safetyBEC (e.g wire transferinvoice fraud)Cloud\-based threatsBest practices for remote workingPhysical security measuresBest practices for email reportingInsider threatsCompliance topics (e.g GDPR and 
PCI)Multi\-factor authenticationSocial engineeringSmishingRole\-based trainingVishingNone of these37%27%39%35%35%37%29%29%29%35%33%33%27%31%33%39%22%31%14%0%54%48%37%44%40%37%42%35%36%30%32%30%34%31%26%17%27%25%22%0%42%48%43%47%44%47%36%38%41%25%35%32%31%34%34%25%19%23%25%0%57%61%35%37%47%45%45%57%45%43%45%27%39%29%35%22%24%14%22%2%483%0%0%98%2%40%35%46%40%36%32%35%31%35%35%38%30%32%28%28%33%30%27%19%0%7%0%0%100%0%57%48%49%43%51%46%38%38%37%43%41%43%38%40%37%31%30%28%26%0%10%4%\<1%99%1%49%47%44%43%43%42%40%40%39%37%36%34%33%33%32%27%26%25%23%\<1%0%0%100%0%58%61%58%58%49%47%59%53%51%48%31%43%34%36%34%21%33%25%33%0%2022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageWho does your organization assign security awareness training to?Everyone in the organizationSelect departmentsrolesSelect individualsIm not sure51%25%22%2%68%23%9%0%56%33%11%0%49%45%6%0%Which of the following tools are used in your security awareness training program?In\-person training sessionsVirtual, instructor\-led trainingComputer\-based trainingSimulated phishing attacksAwareness posters and videosNewsletters and emailsCybersecurity\-based contestsprizesSmishing andor vishing simulationsSimulated USB dropsInternal cybersecurity chat channelInternal wiki22%29%31%37%39%39%31%37%35%33%31%35%38%41%38%41%40%29%29%28%28%22%35%38%48%44%30%37%23%31%21%35%31%How often does your organization send phishing simulations to employees?DailyWeeklyMonthlyQuarterlyTwice a yearOnce a year61%28%6%5%0%0%5%39%34%11%8%3%26%26%28%16%2%2%37%27%35%47%37%43%29%35%24%33%24%0%39%35%17%9%0%50%26%23%1%52%46%44%39%19%40%22%31%23%33%24%5%28%39%23%5%0%59%25%16%0%41%31%51%38%41%35%39%30%37%26%29%38%22%21%19%0%0%64%22%14%0%47%34%50%41%38%42%35%37%29%36%22%15%37%27%19%2%0%Does your organization offer educational training to employees who fall for simulated or real\-world phishing emails?YesNoIm not sure88%10%2%86%12%2%83%15%2%82%18%0%89%10%1%84%13%3%How often does your organization assign formal training (in\-person, instructor\-led, or computer\-based)?DailyWeeklyMonthlyQuarterlyTwice a yearOnce a year23%47%24%3%3%0%8%37%24%15%12%4%10%22%23%17%14%14%3%37%23%23%11%3%5%25%27%25%11%7%32%34%23%6%5%0%83%16%1%20%36%19%16%2%7%57%28%15%\<1%38%35%43%41%35%39%30%33%28%32%26%21%31%27%16%4%1%85%13%2%14%34%23%15%9%5%492022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageIn a year, how much time does your organization allocate to formal training (in\-person, instructor\-led, or computer\-based)?30 minutes or less31\-59 minutes1\-2 hours2\-3 hoursMore than 3 hours29%29%24%6%12%5%37%31%14%13%3%29%38%17%13%6%29%53%10%2%4%21%35%19%21%4%32%38%10%16%12%25%37%12%14%9%29%37%12%13%Since implementing your current security awareness training program, has your organization experienced lower phishing failure 
rates?YesAbout the sameNo, they are higherIm not sure78%18%4%0%74%20%4%2%69%30%0%1%55%35%6%4%72%26%2%0%68%26%5%1%84%13%1%2%72%24%3%1%Does your organizations threat intelligence influence your security awareness training decisions? (Multiple responses allowed.)Yes, we use phishing tests that mimic 
trending threatsYes, we train on specific topics that 
relate to attacks we are facingYes, we train specific individuals we 
know are being targetedNo, we do not adjust our training 
according to threat intelligenceNA (I don't have access to my 
organizations threat intelligence)Yes, full\-time remoteYes, part\-time remote, part\-time on siteThey were but arent any longerNo, our employees were not impacted 
this way by the pandemicMore than 50% of our employees 
always work remotely56%61%43%48%45%51%67%53%68%64%55%50%71%58%56%60%40%39%44%40%45%53%43%43%2%0%5%0%8%2%14%4%4%0%6%1%50%38%10%0%26%49%17%5%23%57%13%5%16%62%14%6%24%56%16%3%49%32%15%2%2%3%2%2%1%2%1%2%5%0%47%35%16%1%6%1%34%47%14%3%As a product of the pandemic, are more than 50% of your organizations employees working remotely?Excluding educational training, do employees in your organization face disciplinepunishment (i.e a consequence model) for 
interacting with real or simulated phishing attacks?YesNo, its not a fit for our cultureNo, but were considering this approachNo, but we will implement this soonNo, I dont know what this isIm not sure78%14%4%2%0%2%53%28%12%4%0%3%42%37%15%4%2%0%44%24%18%6%8%0%29%39%22%9%0%1%77%5%11%4%1%2%60%21%15%2%2%0%55%24%14%4%2%1%502022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageExcluding educational training, what are the consequences employees face? (Multiple answers allowed.)Counseling from managerCounseling from the infosec teamImpact to yearly performance reviewsDisciplinary actions (like a written 
warning) enforced by HRRemoval of access to systemsMonetary penaltyTerminationIm not sure56%59%67%56%46%31%15%3%57%66%47%53%30%30%11%0%55%64%45%50%31%21%10%2%59%68%45%41%27%5%9%0%48%52%34%28%34%31%28%0%73%51%65%48%53%42%29%0%73%50%63%42%25%25%25%2%For simulated phishing attacks: What is the FIRST action that determines whether an employee faces a consequence?Failing 1 phishing testFailing 2 phishing testsFailing 3 phishing testsFailing 4 phishing testsFailing 5 phishing testsFailing more than 5 phishing testsFailing phishing tests does not result in 
a consequenceIm not sure8%28%31%13%8%8%0%4%6%49%19%21%2%2%0%1%26%26%29%5%2%5%5%2%23%32%27%14%0%0%4%0%17%45%17%4%4%10%0%13%23%26%12%12%10%3%3%1%20%28%20%10%8%7%5%2%For real\-world phishing attacks: What is the FIRST action that determines whether an employee faces a consequence?Falling for 1 real\-world phishing attackFalling for 2 real\-world phishing attacksFalling for 3 real\-world phishing attacksFalling for 4 real\-world phishing attacksFalling for 5 real\-world phishing attacksFalling for more than 5 phishing attacksFalling for real\-world phishing attacks 
does not result in a consequenceIm not sure10%36%31%10%8%0%0%5%2%56%23%11%6%0%0%2%31%34%24%2%5%0%2%2%32%41%18%0%0%4%5%0%28%35%24%0%3%10%0%0%17%21%31%19%5%7%0%0%38%27%8%13%5%5%2%2%60%59%52%45%35%26%18%1%16%33%24%11%5%6%3%2%23%35%23%8%4%4%1%2%How did the implementation of a consequence module correlate to the launch of your security awareness training program?Launched at the same time as security 
awareness trainingLaunched 6 to 12 months after security 
awareness trainingLaunched 1 to 2 years after security 
awareness trainingLaunched more than 2 years after 
security awareness trainingLaunched a consequence model 
without having a training programIm not sure57%41%33%27%45%57%57%45%31%40%38%46%41%24%27%35%5%8%0%0%11%22%18%10%17%13%14%8%0%0%5%0%2%9%0%0%4%0%0%1%1%0%3%0%0%5%\<1%\<1%512022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageHow has the use of a consequence model impacted employee awareness of phishing?Awareness has increasedAwareness is about the sameAwareness has decreasedIm not sure61%31%8%0%68%28%4%0%64%31%2%3%91%9%0%0%65%28%7%0%71%25%4%0%70%27%3%0%70%25%4%\<1%What best describes how employees have responded to these consequences overall?For the most part, people seem to 
understand and accept the approachThe response has been mixedThere have been many complaints, but 
were working to resolve concernsThere have been many complaints, but 
we firmly believe its the right approach33%40%22%32%62%40%30%37%23%21%17%26%24%38%32%9%0%10%29%10%25%22%21%20%21%17%14%27%28%21%22%21%Im not sure2%0%2%0%0%0%1%1%Cybersecurity for your organization is:High priorityPrioritySomewhat a priorityLow priorityNot a priority70%24%4%2%0%65%32%3%0%0%In your organization, cybersecurity for the average employee is:High priorityPrioritySomewhat a priorityLow priorityNot a priority66%26%4%4%0%44%43%13%0%0%65%25%7%3%0%48%43%7%1%1%44%46%6%4%0%32%46%16%6%0%74%20%5%1%0%53%41%6%0%0%67%22%9%2%0%56%34%7%2%1%69%30%1%0%0%53%39%5%3%0%Organizations often talk about building a culture of security. How do you feel about the security culture at your organization?PositiveNeutralNegative90%8%2%88%12%0%80%18%2%76%24%0%89%11%0%84%15%1%86%13%1%65%28%5%2%0%50%39%8%2%\<1%85%14%1%522022 STATE OF THE PHISHREPORTB.Working adult survey: country\-by\-country breakdownAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageWhat is phishing?Correct answerIncorrect answerI dont knowWhat is ransomware?Correct answerIncorrect answerI dont knowWhat is malware?Correct answerIncorrect answerI dont knowWhat is smishing?Correct answerIncorrect answerI dont knowWhat is vishing?Correct answerIncorrect answerI dont know59%21%20%49%30%21%69%17%14%23%26%51%26%23%51%47%29%24%27%32%41%63%21%16%24%27%49%17%29%54%54%29%17%26%34%40%56%26%18%25%34%41%24%39%37%52%23%25%31%28%41%52%10%38%17%27%56%22%22%56%52%29%19%36%21%33%73%17%10%27%30%43%26%31%43%62%28%10%47%37%16%71%21%8%24%41%35%27%35%38%49%32%19%38%39%23%61%26%13%24%37%39%25%38%37%53%27%20%36%33%31%63%20%17%23%32%45%24%31%45%532022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageUnderstanding of emailAn email can appear to come from someone other than the person or company who sent it.TrueFalseIm not sure79%11%10%71%14%15%81%9%10%68%13%19%If an email includes logos and contact information from a familiar brand, I know its safe.TrueFalseIm not sure32%52%16%28%53%19%32%49%19%Email attachments can be infected with software that can damage my computer.TrueFalseIm not sure84%9%7%78%11%11%All internal emails (like those I exchange with coworkers) are safe.TrueFalseIm not sure48%36%16%52%29%19%85%7%8%54%29%17%19%63%18%78%10%12%21%59%20%76%14%10%34%48%18%83%10%7%59%28%13%82%11%7%28%59%13%83%10%7%48%39%13%81%11%8%42%42%16%79%12%9%50%34%16%77%12%11%31%52%17%81%10%9%47%36%16%If a link in an email takes me to a file thats stored in a reputable cloud service (like Office 365, Google Drive, or Dropbox), I know that file is 
safe.TrueFalseIm not sure28%42%30%35%34%31%32%35%33%If I have exchanged multiple emails with someone, I know that is a safe contact.TrueFalseIm not sure45%40%15%I should be cautious of any unexpected emails.TrueFalseIm not sure88%5%7%52%33%15%81%13%6%49%31%20%85%7%8%27%42%31%28%49%23%89%6%5%My organizations security tools will automatically block all suspiciousdangerous emails.TrueFalseIm not sure49%35%16%46%32%22%55%23%22%43%28%29%My personal email provider will automatically block all suspicious dangerous emails.38%47%15%37%39%24%49%35%16%43%31%26%TrueFalseIm not sure5444%30%26%57%31%12%90%5%5%57%23%20%49%31%20%29%46%25%46%42%12%88%8%4%45%38%17%36%49%15%46%32%22%50%34%16%85%9%6%49%32%18%45%38%17%35%37%28%47%37%16%86%8%6%49%30%21%43%38%19%2022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageHas the pandemic impacted where you currently work?Yes, now work remotely full timeYes, now work remotely part time and 
on site part timeYes, now work on site full timeI was working remotely, but I dont 
anymore30%27%10%3%11%21%13%8%12%25%14%4%10%23%24%6%16%27%10%12%26%30%14%4%33%16%15%7%20%24%14%6%My work location hasnt changed30%47%45%37%35%26%29%36%Which of the following applies to your home Wi\-Fi network? (Multiple responses allowed.)I have changed the default name of my 
wireless networkMy wireless network is password 
protectedI have changed my wireless networks 
default passwordI have changed my wireless routers 
default passwordI have checked for software updates to 
my wireless routerI currently havent done anything like 
this for my Wi\-Fi networkI dont have a home W\-Fi networkIm not sure23%22%37%16%28%21%34%26%61%50%69%44%69%68%61%60%22%21%34%22%28%19%32%26%23%10%32%19%22%20%24%22%18%10%23%19%14%16%24%18%8%4%9%15%3%11%6%2%3%25%6%9%8%1%1%8%1%5%7%3%5%11%3%6%You have not taken someall of the Wi\-Fi security actions noted. Why?I am not worried about my home Wi\-Fi 
networkI dont know how to change these 
settingsOther, please specify (see the body of 
the report for common write\-in reasons)65%64%65%57%54%62%68%62%30%34%31%38%41%36%29%34%5%2%4%5%5%2%3%4%Which of these PERSONAL devices do you use for work\-related purposes? (Multiple responses allowed.)PhonesmartphoneLaptop computerDesktop computerTabletNone of these56%39%25%20%23%43%31%21%17%32%50%34%26%24%29%54%37%20%17%31%59%42%27%26%20%Which of these EMPLOYER\-ISSUED devices to you use for work? (Multiple responses allowed.)PhonesmartphoneLaptop computerDesktop computerTabletNone of these31%45%29%18%28%38%36%27%15%29%40%40%33%22%27%36%42%25%14%32%46%41%31%22%26%50%33%20%21%29%36%51%29%22%20%64%41%27%30%19%45%43%34%29%24%54%37%24%22%26%39%43%30%20%27%552022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageWhich of these personal activities you do on your employer\-issued device? (Multiple responses allowed.)Checkrespond to personal emailViewpost to social mediaStream media (music, videos)Shop onlineRead news storiesResearch (new products, travel)Play gamesNone of these50%26%26%35%44%41%19%21%39%23%24%30%34%30%27%22%32%22%24%33%36%31%27%28%37%29%20%20%44%42%11%25%51%35%35%39%48%41%25%20%40%26%25%31%38%34%22%24%47%39%42%40%36%38%34%17%Which of these activities do you allow friendsfamily to do on your employer\-issued device? (Multiple responses allowed.)Checkrespond to emailViewpost to social mediaStream media (music, videos)Shop onlineRead news storiesResearchcomplete homeworkPlay gamesNot sure how they use my deviceNone of these19%13%19%22%20%19%14%4%52%18%14%14%19%18%19%19%5%44%22%17%18%27%20%15%20%6%44%20%18%13%13%25%24%10%3%51%How do you currently manage your passwords for your PERSONAL online accounts?34%29%28%36%38%26%22%4%31%23%21%30%20%16%16%20%19%18%19%4%49%21%26%29%30%26%28%34%24%23%26%3%39%36%23%22%42%29%28%32%40%37%23%23%23%19%20%24%23%21%19%4%44%25%20%27%Logins saved in a browserUse password managerManually enter a unique password for 
every accountManually enter and rotate 1 to 4 
passwords across accountsManually enter and rotate 5 to 10 
passwords across accountsManually enter and rotate more than 10 
passwordsLogins saved in a browserUse password managerManually enter a unique password for 
every accountManually enter and rotate 1 to 4 
passwords across accountsManually enter and rotate 5 to 10 
passwords across accountsManually enter and rotate more than 10 
passwords5625%20%27%22%15%32%19%20%34%31%17%16%8%6%8%10%7%6%8%12%7%5%14%13%14%16%14%14%10%14%20%20%32%22%18%32%16%20%38%27%19%19%26%22%28%14%14%14%16%16%13%5%9%7%7%7%5%7%12%5%3%6%5%5%5%16%27%33%4%5%33%21%27%8%6%5%7%7%23%21%30%14%6%6%How do you currently manage your passwords for your WORK\-RELATED online accounts?2022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageIn 2021, did you receive any of the following? (Multiple responses allowed.)An email from a sender who 
impersonated someone I knowAn email from a sender who 
impersonated another person
organizationAn email that impersonated your 
current organizationAn email that contained an 
untrustworthy attachmentSuspicious text messages on your 
phonesmartphone17%20%20%13%19%17%22%18%33%31%25%27%32%29%26%29%16%12%18%12%14%15%18%15%44%32%40%33%49%35%39%39%51%36%33%24%39%42%41%38%Suspicious messages on social mediaSuspicious messages in a work\-related 
messaging appSuspicious phone calls or voicemailsNo, I didnt receive any of these24%12%53%13%24%17%29%18%24%14%32%17%22%17%23%29%34%20%39%9%24%14%34%15%33%19%46%15%27%16%37%17%In 2021, did you do any of the following? (Multiple responses allowed.)Clicked a link in an email that led to a 
fake websiteAccidentally compromised an account 
passwordAccidentally downloaded malware from 
a dangerous email or websiteClicked a link in a direct message that 
downloaded malwareGave personal information to a 
scammer or impostor16%18%16%10%23%20%26%19%5%9%9%10%10%14%14%7%7%14%12%17%11%18%11%19%13%14%16%10%17%12%22%14%11%13%13%6%11%12%18%12%No, I did not do any of these69%54%56%75%50%58%45%58%In 2021, did you experience any of the following? (Multiple responses allowed.)Some hacked into one or more of your 
social media accountsSomeone duplicated one or more 
social media profiles and tried to 
impersonate youIdentity theftA ransomware infection that led to 
paying money to regain access to 
personal filesdeviceFinancial loss due to a fraud committed 
against you8%8%7%8%13%17%13%13%8%9%13%10%7%9%8%6%13%14%22%14%14%10%18%12%10%11%10%11%19%17%11%10%11%15%10%6%12%12%18%12%No, I did not experience any of these73%61%59%76%62%64%48%63%572022 STATE OF THE PHISHREPORTAustraliaFranceGermanyJapanSpainUKU.S.Global 
AverageCybersecurity for my organization is:Not a priorityLow prioritySomewhat a priorityPriorityHigh priorityIm not sureCybersecurity for me is:Not a priorityLow prioritySomewhat a priorityPriorityHigh priorityIm not sure2%5%18%25%44%6%1%5%21%30%40%3%4%9%18%30%31%8%3%7%19%38%30%3%4%5%14%19%53%5%3%3%14%26%52%2%5%10%21%25%21%18%3%9%24%28%22%14%2%4%18%21%53%2%\<1%3%17%26%53%\<1%2%8%19%21%46%4%1%7%21%31%39%1%5%7%14%21%45%8%4%7%17%27%42%3%3%7%18%23%42%7%2%6%19%29%40%4%You mentioned cybersecurity is a low priority or not a priority for you. Why?My organizationIT team will take care 
of any security needs or mistakes I 
makeI dont interact with devices often 
enough to be worriedIve never experienced any 
cybersecurity issues, so I dont need to 
prioritize itMy job isnt high\-level enough for me to 
be a target for cyberattackers10%14%33%17%12%18%27%19%28%27%17%24%12%21%24%22%31%24%33%31%44%32%27%32%31%35%17%25%32%29%22%27%Other0%0%0%3%0%0%0%\<1%If you have a cybersecurity issue with a work device, how confident are you that your IT team can identify and address that issue 
without your involvement?Not at all confidentNot confidentNeutralConfidentExtremely confident3%6%24%45%22%11%17%32%26%14%4%10%36%36%14%11%17%44%23%5%4%17%23%47%9%3%11%21%47%18%4%7%26%37%26%6%12%30%37%15%582022 STATE OF THE PHISHREPORTC.Industry failure rates by simulated phishing template styleAs was the case last year, users across all industries struggled to identify and avoid attachment\-based phishing tests in 2021\. 
But even the highest average failure ratesincluding minings 36%didnt have much influence on overall industry failure 
rates. Its further proof of something discussed in Section 4: that attachment\-based tests are not frequently used in many 
organizations.As we cautioned in the main report, an overall average failure rate is a general view; it cannot reveal more specific areas of 
risk. Susceptibility to attachment\-based phishing attacks could be a hidden issue for many organizations. Regular testing 
and training about these types of threats could prove beneficial.IndustryAerospaceAgricultureAutomotiveBusiness ServicesConstructionConsultingEducationElectronicsEnergyUtilitiesEngineeringEntertainmentMediaFinancial ServicesFood \& BeveragesGovernmentHealthcareHospitalityLeisureInsuranceLegalManufacturingMiningReal EstateRetailTechnologyTelecommunicationsTransportationAverage Failure RateLink\-Based
TestsAttachment\-Based
TestsData Entry\-Based
TestsOverall11%13%9%12%12%14%11%9%10%8%10%10%13%12%10%9%13%12%11%11%11%12%14%13%14%18%18%15%29%21%25%17%17%20%18%19%17%17%14%26%29%20%18%20%36%23%23%25%21%15%4%7%3%4%5%6%4%3%4%4%5%3%3%4%4%4%4%6%4%5%6%5%4%7%5%12%12%8%12%12%14%10%8%10%8%9%9%11%11%10%10%11%11%10%12%12%11%12%12%11%592022 STATE OF THE PHISHREPORTLEARN MORE
Test your current security awareness program with our free People Risk Assessment. 
Youll get visibility into your users cybersecurity knowledge and vulnerability. It covers critical cybersecurity topics such as 
phishing, visit passwords, data protection and more. proofpoint.comuspeople\-risk\-assessmentABOUT PROOFPOINTProofpoint, Inc. is a leading cybersecurity and compliance company that protects organizations greatest assets and biggest risks: their people. With an integrated suite of cloud\-based solutions, 
Proofpoint helps companies around the world stop targeted threats, safeguard their data and make their users more resilient against cyber attacks. Leading organizations of all sizes, including more than 
half of the Fortune 1000, rely on Proofpoint for people\-centric security and compliance solutions that mitigate their most critical risks across email, the cloud, social media and the web. More information is 
available at www.proofpoint.com.Proofpoint, Inc. Proofpoint is a trademark of Proofpoint, Inc. in the United States and other countries. All other trademarks contained herein are property of their respective owners. Proofpoint.com2022 STATE OF THE PHISHREPORT0400\-007\-01\-010122