# 2020-2021 Cyber-Espionage Report

## Table of Contents
[01 | Compass points and decoder keys](#01--compass-points-and-decoder-keys)
[02 | State of Cyber-Espionage](#02--state-of-cyber-espionage)
  [Patterns](#patterns)
  [Timelines](#timelines)
[03 | Targeted victims](#03--targeted-victims)
  [NIST CSF Identify](#nist-csf-identify)
  [Regions](#regions)
  [Industries](#industries)
[04 | Essential Elements of Friendly Information](#04--essential-elements-of-friendly-information)
  [NIST CSF Protect](#nist-csf-protect)
  [Attributes](#attributes)
  [Assets](#assets)
  [Data](#data)
[05 | Threat actors](#05--threat-actors)
  [NIST CSF Detect](#nist-csf-detect)
  [Actors](#actors)
  [Motives](#motives)
[06 | Tradecraft](#06--tradecraft)
  [NIST CSF Respond](#nist-csf-respond)
  [Actions](#actions)
  [Misuse](#misuse)
  [Social](#social)
  [Hacking](#hacking)
  [Malware](#malware)
  [Deeper dive—Action varieties](#deeper-diveaction-varieties)
  [Deeper dive—Action vectors](#deeper-diveaction-vectors)
[07 | The way forward](#07--the-way-forward)
  [NIST CSF Recover](#nist-csf-recover)
  [Takeaways](#takeaways)
  [Mappings](#mappings)
[08 | Appendix A: Guides](#08--appendix-a-guides)
  [VERIS framework](#veris-framework)
  [VIPR process](#vipr-process)
  [NIST Cybersecurity Framework](#nist-cybersecurity-framework)
  [CIS Critical Security Controls](#cis-critical-security-controls)
[09 | Appendix B: Industry dossiers](#09--appendix-b-industry-dossiers)
  [Educational Services](#educational-services)
  [Financial and Insurance](#financial-and-insurance)
  [Information](#information)
  [Manufacturing](#manufacturing)
  [Mining, Quarrying, Oil & Gas Extraction + Utilities](#mining-quarrying-oil--gas-extraction--utilities)
  [Professional, Scientific, and Technical Services](#professional-scientific-and-technical-services)
  [Public Administration](#public-administration)
  [Final notes](#final-notes)

## 01 | Compass points and decoder keys
2
2020-2021 Cyber-Espionage Report
Welcome to the Cyber-Espionage Report (CER), 
our first-ever data-driven publication on 
advanced cyberattacks. The CER is one of the 
most comprehensive overviews of the Cyber-
Espionage landscape, offering a deep dive into 
attackers, their motives, their methods and the 
victims who they target. The report serves as a 
tool for better understanding these threat actors 
and what organizations can do to hunt, detect 
and respond to Cyber-Espionage attacks.

This data-driven report draws from seven years 
of Data Breach Investigations Report (DBIR) 
content as well as more than 14 years of Verizon 
Threat Research Advisory Center (VTRAC) 
Cyber-Espionage data breach response 
expertise. The CER serves as a guide for 
cybersecurity professionals looking to bolster 
their organization’s cyberdefense posture and 
incident response (IR) capabilities against 
Cyber-Espionage attacks.

More specifically, the CER is an elaboration of 
the “Cyber-Espionage” Incident Classification 
Pattern as reflected in the 2020 DBIR. And as 
with the DBIR, we use the same naming 
conventions, terms and definitions. Content in 
this section and in “Appendix A: Frameworks” 
will help serve as your compass points and 
decoder keys for the rest of the report. Download 
a copy of the CER at verizon.com/business/
resources/reports/cyber-espionage-report/

### Using this report
Throughout the CER, we present and compare findings 
from a seven-year perspective (content from the 2014 DBIR 
through the 2020 DBIR): Cyber-Espionage breaches vs. all 
breaches. At times, we also address findings from a one-year 
(2020 DBIR) perspective: Cyber-Espionage breaches vs. all 
breaches. All references to years in this report are in DBIR 
years. For example, “2020 DBIR timeframe” refers to DBIR 
year 2020, which in turn correlates with the DBIR dataset 
timeframe of October 2018 to October 2019.

### Data Breach Investigations Report
The 2020 DBIR is our 13th edition, covering global 
cybercrime trends. The DBIR combines real data from scores 
of sources and provides actionable insight into tackling 
cybercrime. Download the 2020 DBIR here:
[enterprise.verizon.com/resources/reports/dbir/](enterprise.verizon.com/resources/reports/dbir/)

### VERIS framework
The Vocabulary for Event Recording and Incident Sharing 
(VERIS) framework is a set of metrics designed to provide 
a common language for describing security incidents in 
a structured and repeatable manner. See “Appendix A: 
Frameworks” for more information and read more about 
VERIS at the link below:
[veriscommunity.net/](veriscommunity.net/)

### Incident Classification Patterns
Way back in 2014, to help us better understand and 
communicate the DBIR dataset, we grouped “like” incidents 
together and called them “Incident Classification Patterns.” 
Nine patterns comprised the majority of data breaches back 
then and still do so today. These patterns are Crimeware, 
Cyber-Espionage, Denial of Service, Lost and Stolen Assets, 
Miscellaneous Errors, Payment Card Skimmers, Point of 
Sale, Privilege Misuse, Web Applications and the catchall 
Everything Else. For definitions and summaries, see pages 36 
to 37 of the 2020 DBIR.

### Cyber-Espionage pattern
The DBIR Cyber-Espionage pattern consists of espionage 
enabled via unauthorized network or system access. Nation-
state or state-affiliated threat actors looking for those oh-so-
juicy secrets primarily fall within this pattern.

3
2020-2021 Cyber-Espionage Report

### Industry labels
We align the CER with the North American Industry 
Classification System (NAICS), a standard for categorizing 
victim organizations. NAICS uses two- to six-digit codes to 
classify organizations. For the CER, we use the two-digit 
classification level. We provide detailed analyses for seven 
NAICS-coded industries in “Appendix B: Industry dossiers.” 
Detailed information on the codes is available here:
[naics.com/search-naics-codes-by-industry/](naics.com/search-naics-codes-by-industry/)

### NIST Cybersecurity Framework
We use the National Institute of Standards and Technology 
(NIST) Cybersecurity Framework (CSF) in this report. 
Specifically, we use the five functional areas of Identify, 
Protect, Detect, Respond and Recover. See “Appendix A: 
Frameworks” and here for more information:
[nist.gov/cyberframework](nist.gov/cyberframework)

### CIS Critical Security Controls
We also use the 20 Center for Internet Security (CIS) Critical 
Security Controls (CSCs) in this report. See “Appendix A: 
Frameworks” and here for more information:
[cisecurity.org/controls/cis-controls-list/](cisecurity.org/controls/cis-controls-list/)

### Contact us.
Questions? Comments? Feedback? Drop the 
VTRAC team a line at vtrac@verizon.com or 
find us on LinkedIn at #cyberespionagereport 
and #vtrac

## 02 | State of Cyber-Espionage
4
2020-2021 Cyber-Espionage Report
### Overview
We’ve conducted all sorts of investigations into cybersecurity 
incidents and data breaches over the years. None have been 
more challenging or perplexing than Cyber-Espionage attacks.

Indeed, Cyber-Espionage threat actors pose a unique 
challenge to cyberdefenders and incident responders. 
Through advanced techniques and a specific focus, these 
determined threat actors seek to swiftly and stealthily gain 
access to heavily defended environments. Depending on 
their goals, they move laterally through the network, obtain 
targeted access and data, and exit without being detected. 
Or, they stay back and maintain covert persistence.

Often, threat actors leave little to no indication of their 
actions, let alone objectives, to avoid detection and thwart 
response efforts. Many choose not to move immediately 
toward their objectives, opting to embed themselves in the 
environment where they persist quietly until their next move.

Threat actors conducting espionage can range from nation-
states (or state-affiliated entities) to business competitors, 
and in some cases, organized criminal groups. Their targets 
are both the public sector (governments) and private sector 
(corporations). Their reasons? National security, political 
positioning and economic competitive advantage. They seek 
national secrets, intellectual property and sensitive information.

The Cyber-Espionage threat actor modus operandi includes 
gaining unauthorized access, maintaining a low (or no) profile 
and compromising sensitive assets and data. Technology 
makes espionage actors fast, efficient, evasive and difficult to 
attribute. In a nutshell, for the threat actor, Cyber-Espionage 
is an opportunity with relatively low risk (of being discovered), 
low cost (in terms of resources) and high potential (for payoff).

In seeking to accomplish their objectives, Cyber-Espionage 
threat actors leverage three primary actions:
*   Social engineering by targeting employees through 
activities such as phishing
*   Hacking systems and networks by using backdoors and 
command and control (C2) functions to establish and 
maintain access
*   Deploying malicious software, such as Trojan downloaders, 
to extend their capabilities

Within the DBIR dataset, we identified the industries most 
impacted over the past seven years (2014-2020 DBIR 
timeframe) by Cyber-Espionage breaches: Education, Financial, 
Information, Manufacturing, Mining + Utilities, Professional and 
Public. We focused on these industries because they were the 
most often targeted by these threat actors.

Now, if your industry isn’t featured within this report, you’re 
not off the hook. Cyber-Espionage threat actors may still 
be targeting your assets and data—we may just not have 
visibility into those attacks. If you’ve got sensitive, classified, 
proprietary or internal secrets that you’d like to keep from 
getting into the wrong hands, turn the page and read on.

### The ever-evolving 
threat landscape
To stay ahead of cyberdefenders and incident responders, 
Cyber-Espionage threat actors adjust their tactics, techniques, 
and procedures (TTPs) to embrace new technology, while 
keeping their tried-and-true TTPs operational. Here we map 
those TTPs to the VERIS Action varieties to give you an idea of 
what is in and what is out.

For example, Phishing (Social) and Backdoor (Malware) have 
served as go-to Action varieties. Downloader (Malware), 
Capture stored data (Malware) and Spyware/Keylogger 
(Malware) have all steadily declined from the 2014 DBIR to 
the 2020 DBIR, with Scan network (Malware) completely 
falling off the top 10 list by the time we get to the 2020 DBIR. 
Password dumper (Malware), Trojan (Malware) and Remote 
Access Trojan (RAT) (Malware) are new to the 2020 DBIR 
top 10 list. And, while we see that since the 2014 DBIR, 
Backdoor (Malware), Use of backdoor or C2 (Malware) and 
C2 (Malware) have declined percentagewise over the years, 
these Action varieties consistently remain within the top five 
Action varieties for the entire timeframe.

*Figure #1: Top Action varieties within Cyber-Espionage breaches (2014 DBIR; n=282)*
A bar chart showing the top action varieties in cyber-espionage breaches in 2014. The x-axis shows percentages from 0% to 100% in increments of 20%. The y-axis shows the following action varieties: Backdoor, Phishing, Downloader, Use of backdoor or C2, Capture stored data, C2, Export data, Scan network, Exploit vuln, Spyware/Keylogger. The corresponding percentages are: 91%, 90%, 89%, 89%, 87%, 76%, 66%, 55%, 54%, 53%.

*Figure #2: Top Action varieties within Cyber-Espionage breaches (2014-2020 DBIR; n=1,465)*
A bar chart showing the top action varieties in cyber-espionage breaches from 2014-2020. The x-axis shows percentages from 0% to 100% in increments of 20%. The y-axis shows the following action varieties: Phishing, Use of backdoor or C2, Backdoor, C2, Downloader, Capture stored data, Spyware/Keylogger, Export data, Use of stolen creds, Exploit vuln. The corresponding percentages are: 79%, 60%, 53%, 53%, 27%, 27%, 23%, 22%, 21%, 20%.

*Figure #3: Top Action varieties within Cyber-Espionage breaches (2020 DBIR; n=114)*
A bar chart showing the top action varieties in cyber-espionage breaches in 2020. The x-axis shows percentages from 0% to 100% in increments of 20%. The y-axis shows the following action varieties: Phishing, Password dumper, Backdoor, C2, Use of backdoor or C2, Export data, Trojan, Exploit vuln, RAT, Downloader. The corresponding percentages are: 81%, 59%, 51%, 49%, 44%, 39%, 39%, 38%, 36%, 32%.

5
2020-2021 Cyber-Espionage Report

### Patterns
6
2020-2021 Cyber-Espionage Report
#### Breach patterns
When it comes to overall breaches by 
Incident Classification Pattern for the 
2014-2020 DBIR timeframe, we see that 
Cyber-Espionage ranks sixth (10%)—
albeit within close striking distance of 
fourth: Privilege Misuse (ranked fourth 
at 11%) and the sagging Point of Sale 
intrusions (ranked fifth at 11%).

It is important to note that these 
Incident Classification Patterns 
are just those known, reported and 
collected. Because Cyber-Espionage 
attacks are difficult to detect, and 
the breaches within this pattern are 
under-reported, the number may be 
much higher. The kinds of data stolen 
in Cyber-Espionage breaches (e.g., 
Secrets, Internal or Classified) may not 
fall under the data types that trigger 
reporting requirements under many 
laws or regulations. Cyber-Espionage 
threat actors are not typically targeting 
customer data, or even employee data, 
but rather the intellectual property (or 
secret sauce if you will) that would give 
them a leg up in industrial espionage.

*Figure #4: Breaches by pattern (2014-2020 DBIR; n=16,090)*
A bar chart showing breaches by pattern from 2014-2020. The x-axis shows percentages from 0% to 50% in increments of 10%. The y-axis shows the following incident classification patterns: Web Applications, Miscellaneous Errors, Everything Else, Privilege Misuse, Point of Sale, Cyber-Espionage, Crimeware, Lost and Stolen Assets, Payment Card Skimmers, Denial of Service. The corresponding percentages are: 27%, 14%, 14%, 11%, 11%, 10%, 7%, 4%, 3%, 0%.

*Figure #5: Breaches by pattern (2020 DBIR; n=3,950)*
A bar chart showing breaches by pattern in 2020. The x-axis shows percentages from 0% to 50% in increments of 10%. The y-axis shows the following incident classification patterns: Web Applications, Everything Else, Miscellaneous Errors, Crimeware, Privilege Misuse, Lost and Stolen Assets, Cyber-Espionage, Point of Sale, Payment Card Skimmers, Denial of Service. The corresponding percentages are: 31%, 22%, 21%, 10%, 8%, 4%, 3%, 1%, 1%, 0%.

### Timelines
7
2020-2021 Cyber-Espionage Report
#### Attacker timelines
One of the most effective ways to 
convey the current state of data 
breaches and their impact to victim 
organizations is through temporal 
analysis or timelining.

When we look at the DBIR dataset, four 
timelines manifest most clearly. Two 
are from the threat actor standpoint— 
Time to Compromise and Time to 
Exfiltration—and two are from the 
cyberdefender and incident responder 
standpoint—Time to Discovery and 
Time to Containment.

Traditionally, for all breaches, the DBIR 
has shown that successful threat actors 
have taken a short amount of time 
(seconds to minutes) to compromise, 
and a relatively short amount of time 
(minutes to days) to exfiltrate data.

Victim organizations have taken 
considerably longer (days to months) 
to discover breaches, and an 
uncomfortably long time (hours to 
weeks) to contain breaches.

While the timelines for all breaches 
may seem bleak, the same timelines 
for Cyber-Espionage breaches appear 
even more dire.

In the 2014-2020 DBIR timeframe, for 
Cyber-Espionage threat actors, the 
Time to Compromise ranges from mere 
seconds to days (91%, the sum of 23%, 
19%, 23% and 26%), while the Time 
to Exfiltration ranges from minutes to 
weeks (88%).

*Figure #6: Time to Compromise within Cyber-Espionage breaches (2014-2020 DBIR; n=47)*
A bar chart showing time to compromise within cyber-espionage breaches from 2014-2020. The x-axis shows percentages from 0% to 80% in increments of 20%. The y-axis shows the following timeframes: Seconds, Minutes, Hours, Days, Weeks, Months, Years. The corresponding percentages are: 23%, 19%, 23%, 26%, 4%, 4%, 0%.

*Figure #7: Time to Compromise within all breaches (2014-2020 DBIR; n=2,658)*
A bar chart showing time to compromise within all breaches from 2014-2020. The x-axis shows percentages from 0% to 80% in increments of 20%. The y-axis shows the following timeframes: Seconds, Minutes, Hours, Days, Weeks, Months, Years. The corresponding percentages are: 15%, 70%, 6%, 4%, 2%, 1%, 0%.

*Figure #8: Time to Exfiltration within Cyber-Espionage breaches (2014-2020 DBIR; n=43)*
A bar chart showing time to exfiltration within cyber-espionage breaches from 2014-2020. The x-axis shows percentages from 0% to 80% in increments of 20%. The y-axis shows the following timeframes: Seconds, Minutes, Hours, Days, Weeks, Months, Years. The corresponding percentages are: 0%, 30%, 14%, 21%, 23%, 12%, 0%.

*Figure #9: Time to Exfiltration within all breaches (2014-2020 DBIR; n=1,098)*
A bar chart showing time to exfiltration within all breaches from 2014-2020. The x-axis shows percentages from 0% to 80% in increments of 20%. The y-axis shows the following timeframes: Seconds, Minutes, Hours, Days, Weeks, Months, Years. The corresponding percentages are: 6%, 3%, 0%, 5%, 38%, 9%, 37%.

8
2020-2021 Cyber-Espionage Report
#### Defender timelines
When we look closer, for 
cyberdefenders, we see the Time to 
Discovery within Cyber-Espionage 
breaches is months to years (69%, the 
sum of 30% and 39%) and the Time 
to Containment ranges from hours to 
weeks (64%, the sum of 10%, 25% 
and 29%).

The slow, methodical and lengthy 
process employed by threat actors 
versus the correspondingly plodding 
response from cyberdefenders 
speaks to the patience and 
complexity often accompanying 
Cyber-Espionage attacks.

Moreover, this is indicative of the 
threat actor’s due diligence to not only 
understand their target’s environment 
and cybersecurity posture, but also to 
leverage that knowledge to accomplish 
their objectives without detection.

#### Top controls
*   CSC-6: Maintenance, 
Monitoring and Analysis of 
Audit Logs
*   CSC-12: Boundary Defense 
*   CSC-16: Account Monitoring 
and Control
*   CSC-19: Incident Response 
and Management
*   CSC-20: Penetration Tests 
and Red Team Exercises

*Figure #10: Time to Discovery within Cyber-Espionage breaches (2014-2020 DBIR; n=125)*
A bar chart showing time to discovery within cyber-espionage breaches from 2014-2020. The x-axis shows percentages from 0% to 80% in increments of 20%. The y-axis shows the following timeframes: Seconds, Minutes, Hours, Days, Weeks, Months, Years. The corresponding percentages are: 0%, 1%, 3%, 13%, 14%, 30%, 39%.

*Figure #11: Time to Discovery within all breaches (2014-2020 DBIR; n=2,918)*
A bar chart showing time to discovery within all breaches from 2014-2020. The x-axis shows percentages from 0% to 80% in increments of 20%. The y-axis shows the following timeframes: Seconds, Minutes, Hours, Days, Weeks, Months, Years. The corresponding percentages are: 9%, 1%, 3%, 14%, 23%, 38%, 12%.

*Figure #12: Time to Containment within Cyber-Espionage breaches (2014-2020 DBIR; n=51)*
A bar chart showing time to containment within cyber-espionage breaches from 2014-2020. The x-axis shows percentages from 0% to 80% in increments of 20%. The y-axis shows the following timeframes: Seconds, Minutes, Hours, Days, Weeks, Months, Years. The corresponding percentages are: 0%, 2%, 10%, 25%, 29%, 25%, 2%.

*Figure #13: Time to Containment within all breaches (2014-2020 DBIR; n=789)*
A bar chart showing time to containment within all breaches from 2014-2020. The x-axis shows percentages from 0% to 80% in increments of 20%. The y-axis shows the following timeframes: Seconds, Minutes, Hours, Days, Weeks, Months, Years. The corresponding percentages are: 2%, 7%, 21%, 37%, 18%, 13%, 1%.

## 03 | Targeted victims
9
2020-2021 Cyber-Espionage Report
### NIST CSF Identify
Develop an organizational understanding 
to manage cybersecurity risk to systems, 
people, assets, data and capabilities. 
A fundamental requirement for a solid 
information security posture is identifying 
assets before the adversary does. It’s 
only when the unknowns become known 
that assets and data can be protected. 
After all, you don’t know—and cannot 
protect—what you don’t know.

Asset identification is a foundational 
part of the risk management process, 
which aims to define and prioritize risks 
for an organization. Risk managers often 
build matrices listing threats in order 
of severity. They also classify assets 
in terms of confidentiality, integrity and 
availability (referred to as the “CIA Triad”); 
consider the impact of security breaches 
on the organization; and estimate the 
likelihood of certain incidents.

Risk management also requires an 
organization to identify asset owners 
and asset access controls. Asset 
identification and risk management 
should align with the organization’s 
business objectives to add value to 
the business and help gain buy-in 
from decision makers. For example, 
a business-driven risk management 
strategy could include:
*   Defining objectives
*   Identifying assets and threats
*   Selecting and prioritizing targets
*   Monitoring and detecting threats
*   Responding and improving response 
capabilities

While it can be an overwhelming task 
to start from scratch, it’s possible to 
develop a risk management process 
with smaller objectives by incorporating 
cyber threat intelligence and building 
and refining from there.

An organization that leverages cyber 
threat intelligence to prioritize Cyber-
Espionage attacks as part of its 
risk management process can start 
by asking questions relevant to the 
organization, such as:
*   How prevalent are Cyber-Espionage 
attacks compared to other 
cybersecurity attack patterns?
*   Which Cyber-Espionage threat 
actors have been targeting other 
similar organizations? Based on this, 
how likely is the organization to be 
targeted?
*   What assets and data are Cyber-
Espionage threat actors targeting?
*   What are the common TTPs of 
Cyber-Espionage threat actors?

If the answers to these questions 
point to lower risk, does it mean that in 
some industries, such as Healthcare 
or Accommodation, organizations 
should not be concerned with Cyber-
Espionage? Not at all. This data 
shouldn’t be analyzed without context. 
For example, while the number of Cyber-
Espionage breaches may be lower in 
some industries, the impact of sensitive 
or proprietary data exposure on an 
organization in one of those lesser-
targeted industries could be substantial.

Long story short: Just because your 
organization’s industry has not been 
a typical target for Cyber-Espionage 
threat actors doesn’t mean it won’t be, 
can’t be or hasn’t been.

To contextualize information for an 
organization, it’s not uncommon 
to deploy an internal cyber threat 
intelligence team or to wholly or partly 
outsource this capability.

VERIS and the Center for Internet 
Security (CIS) Critical Security 
Controls (CSCs), as well as the 
VERIS Common Attack Framework 
(VCAF)—a VERIS-to-MITRE ATT&CK® 
Framework introduced in the 2020 
DBIR—are publicly available resources 
for formalizing incident and threat 
data. VERIS helps categorize security 
incidents, while CIS CSCs help focus 
on cybersecurity controls.

Risk analysis, asset identification and 
incident classification can inform the 
appropriate measures for preventing, 
mitigating, detecting and responding 
to threat actors while also maintaining 
the ability to meet organizational 
business objectives.

#### Identification tips
*   Identify assets, asset owners 
and asset access controls 
as part of an effective 
and comprehensive risk 
management strategy
*   Align risk management with 
the organization’s business 
objectives to add business 
value and gain buy-in from 
decision makers
*   Leverage cyber threat 
intelligence to help prioritize 
Cyber-Espionage attacks as 
part of the risk management 
process
*   Avoid complacency. 
Cyber-Espionage attacks 
can potentially impact all 
organizations—even those in 
lesser-targeted industries

### Regions
10
2020-2021 Cyber-Espionage Report
For the 2014-2020 DBIR timeframe, we see Cyber-Espionage breaches occurring 
most often in the Asia-Pacific (APAC) region (42%), followed by the Europe, Middle 
East and Africa (EMEA) region (34%), and North America (NA) (23%) region. 
This contrasts sharply with all breaches for this same timeframe, as NA (65%) 
dominates, followed by APAC (17%) and EMEA (16%).

*Figure #14: Cyber-Espionage breaches by region (2014-2020 DBIR; n=597)*
A bar chart showing cyber-espionage breaches by region from 2014-2020. The x-axis shows percentages from 0% to 100% in increments of 20%. The y-axis shows the following regions: APAC, EMEA, NA. The corresponding percentages are: 42%, 34%, 23%.

*Figure #15: All breaches by region (2014-2020 DBIR; n=6,780)*
A bar chart showing all breaches by region from 2014-2020. The x-axis shows percentages from 0% to 100% in increments of 20%. The y-axis shows the following regions: NA, APAC, EMEA. The corresponding percentages are: 65%, 17%, 16%.

### Industries
11
2020-2021 Cyber-Espionage Report
#### Overall Cyber-Espionage breaches within 
select industries
One way to identify industries impacted by Cyber-
Espionage attacks is by examining overall Cyber-Espionage 
breach numbers.

When we look at how the industries that were featured 
in the 2020 DBIR fared when it comes to Cyber-
Espionage breaches, we can see that some were more 
strongly impacted than others. In particular, Public (31%), 
Manufacturing (22%) and Professional (11%) topped the list 
for Cyber-Espionage breaches.

This is a good time to point out that the DBIR dataset can 
only tell us what the DBIR dataset knows. The DBIR dataset 
consists of successful, reported and known data breaches 
(and cybersecurity incidents). It doesn’t cover undiscovered, 
unreported or uncollected data (i.e., data originating outside 
of the 81 contributors to the 2020 DBIR).

While we have included more detailed, industry-specific 
Cyber-Espionage profiles in “Appendix B: Industry dossiers,” 
here we provide insight into seven industries. These sectors 
are the most impacted by Cyber-Espionage breaches over 
the 2014-2020 DBIR timeframe and have sufficient content 
for analysis Industry (NAICS #): Education (61), Financial (52), 
Information (51), Manufacturing (31-33), Mining + Utilities 
(21+22), Professional (54) and Public (92).

#### Cyber-Espionage breaches within all breaches 
of select industries 
Another way to look at industries impacted by Cyber-
Espionage attacks is the number of Cyber-Espionage 
breaches within all breaches. For the 2014-2020 DBIR 
timeframe, we see Manufacturing (35%), Mining + Utilities 
(23%), Public (23%), Professional (17%), Education (8%), 
Information (7%) and Financial (2%) for percentage of Cyber-
Espionage breaches within all breaches by industry.

We include more detailed, industry-specific Cyber-
Espionage profiles in “Appendix B: Industry dossiers.” 
Here we provide insight into Breaches by pattern, Cyber-
Espionage within all breaches, Actors within Cyber-
Espionage, Actions within Cyber-Espionage, Assets within 
Cyber-Espionage and compromised data within Cyber-
Espionage for these seven industries.

Note: In Figure #16 and Figure #17, numbers in parentheses 
after each industry correspond to the 2-digit NAICS #.

*Figure #16: Cyber-Espionage breaches within select industries (2014-2020 DBIR; n=1,580)*
A bar chart showing cyber-espionage breaches within select industries from 2014-2020. The x-axis shows percentages from 0% to 50% in increments of 10%. The y-axis shows the following industries: Public (92), Manufacturing (31-33), Professional (54), Information (51), Mining + Utilities (21+22), Education (61), Other Services (81), Financial (52), Healthcare (62), Transportation (48-49), Retail (44-45). The corresponding percentages are: 31%, 22%, 11%, 5%, 3%, 3%, 3%, 1%, 1%, 1%, 1%.

*Figure #17: Cyber-Espionage breaches within all breaches of select industries (2014-2020 DBIR)*
A combined bar and line chart showing cyber-espionage breaches within all breaches of select industries from 2014-2020. The x-axis shows the following industries: Manufacturing (31-33), Mining + Utilities (21+22), Public (92), Professional (54), Education (61), Information (51), Financial (52). The left y-axis shows cyber-espionage breaches from 0 to 500 in increments of 500. The right y-axis shows all breaches from 0 to 3000 in increments of 500. The corresponding cyber-espionage breaches are: 344, 54, 485, 166, 47, 72, 42. The corresponding all breaches are: 985, 230, 2,152, 980, 607, 1,043, 2,797. The corresponding percentages are: 35%, 23%, 23%, 17%, 8%, 7%, 2%.

## 04 | Essential Elements of Friendly Information
12
2