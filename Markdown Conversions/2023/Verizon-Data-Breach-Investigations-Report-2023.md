# DBIR 2023 Data Breach Investigations Report

## Table of Contents
- [About the Cover](#about-the-cover)
- [Original Report Table of Contents](#original-report-table-of-contents)
- [Helpful Definitions and Chart Guidance](#helpful-definitions-and-chart-guidance)
  - [Incident vs. Breach](#incident-vs-breach)
  - [VERIS Framework Resources](#veris-framework-resources)
  - [Industry Labels](#industry-labels)
  - [I’m Sorry, This All Happened When?](#im-sorry-this-all-happened-when)
  - [Being Confident of Our Data](#being-confident-of-our-data)
  - [Credit Where Credit Is Due](#credit-where-credit-is-due)
  - [Questions? Comments? Organizing a Bank Run?](#questions-comments-organizing-a-bank-run)
- [Introduction](#introduction)
- [Summary of Findings](#summary-of-findings)
- [2 Results and Analysis](#2-results-and-analysis)
  - [Results and Analysis: Introduction](#results-and-analysis-introduction)
  - [Actors](#actors)
    - [Actor Categories](#actor-categories)
  - [Actions](#actions)
    - [Action Categories](#action-categories)
  - [Assets](#assets)
    - [Asset Categories](#asset-categories)
  - [Attributes](#attributes)
    - [Attribute Categories](#attribute-categories)
    - [Virtual Money, Real Problems](#virtual-money-real-problems)
- [3 Incident Classification Patterns](#3-incident-classification-patterns)
  - [Incident Classification Patterns: Introduction](#incident-classification-patterns-introduction)
  - [System Intrusion](#system-intrusion)
    - [Summary](#summary)
    - [This Is Mine, and This Is Mine …](#this-is-mine-and-this-is-mine-)
    - [Jiggling Locks](#jiggling-locks)
    - [Well, That Escalated Quickly.](#well-that-escalated-quickly)
    - [Results](#results)
    - [Ransomware … Seriously, We’re Still Doing This Section?](#ransomware--seriously-were-still-doing-this-section)
    - [Splitting the Log4j](#splitting-the-log4j)
    - [CIS Controls for Consideration](#cis-controls-for-consideration)
    - [Just One More (Ransomware) Note](#just-one-more-ransomware-note)

---

## About the Cover

The magnifier on the cover is intended to visually convey the effort the team made to refocus our energy and resources more on our core breach dataset. The graph that is magnified is simply a cumulative count of the number of breaches in our dataset as the years have gone by since our first report. Long-time readers may notice the Vocabulary for Event Recording and Incident Sharing (VERIS) Framework trademark honeycombs, which are meant to convey the 4As (Actor, Action, Asset, Attribute) and their various enumerations.

`30K`  
`20K`  
`10K`  
`2005 2010 2015 2020`

---

## Original Report Table of Contents

| Section | Page | Section | Page |
| :--- | :--- | :--- | :--- |
| **1 Helpful definitions and chart guidance** | **4** | **4 Industries** | **49** |
| Introduction | 7 | Introduction | 49 |
| Summary of findings | 8 | Accommodation and Food Services | 53 |
| | | Educational Services | 54 |
| **2 Results and analysis** | **11** | Financial and Insurance | 55 |
| Introduction | 11 | Healthcare | 56 |
| Actors | 12 | Information | 57 |
| Actions | 14 | Manufacturing | 58 |
| Assets | 17 | Mining, Quarrying, and Oil & Gas Extraction + Utilities | 59 |
| Attributes | 19 | Professional, Scientific and Technical Services | 61 |
| | | Public Administration | 62 |
| **3 Incident Classification Patterns** | **22** | Retail | 63 |
| Introduction | 22 | Small and medium business | 65 |
| System Intrusion | 24 | | |
| Social Engineering | 31 | **5 Regions** | **70** |
| Basic Web Application Attacks | 35 | Introduction | 70 |
| Miscellaneous Errors | 40 | | |
| Denial of Service | 42 | **6 Wrap-up** | **74** |
| Lost and Stolen Assets | 44 | Year in review | 74 |
| Privilege Misuse | 46 | | |
| | | **Appendices** | **79** |
| | | Appendix A: Methodology | 79 |
| | | Appendix B: VERIS mappings to MITRE ATT&CK® | 83 |
| | | Appendix C: VTRAC 20-year retrospective | 84 |
| | | Appendix D: Contributing organizations | 85 |

---

## Helpful Definitions and Chart Guidance

Hello, and welcome first-time readers! Before you get started on the 2023 Data Breach Investigations Report (DBIR), it might be a good idea to take a look at this section first. (For those of you who are familiar with the report, please feel free to jump over to the introduction.)

We have been doing this report for a while now, and we appreciate that the verbiage we use can be a bit obtuse at times. We use very deliberate naming conventions, terms and definitions and spend a lot of time making sure we are consistent throughout the report. Hopefully this section will help make all of those more familiar.

### Incident vs. Breach

We talk a lot about incidents and breaches and we use the following definitions:

- **Incident:** A security event that compromises the integrity, confidentiality or availability of an information asset.
- **Breach:** An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party. A Distributed Denial of Service (DDoS) attack, for instance, is most often an incident rather than a breach, since no data is exfiltrated. That doesn’t make it any less serious.

### VERIS Framework Resources

The terms “threat actions,” “threat actors” and “varieties” will be referenced often. These are part of the Vocabulary for Event Recording and Incident Sharing (VERIS), a framework designed to allow for a consistent, unequivocal collection of security incident details. Here is how they should be interpreted:

- **Threat actor:** Who is behind the event? This could be the external “bad guy” that launches a phishing campaign or an employee who leaves sensitive documents in their seat back pocket.
- **Threat action:** What tactics (actions) were used to affect an asset? VERIS uses seven primary categories of threat actions: Malware, Hacking, Social, Misuse, Physical, Error and Environmental. Examples at a high level include hacking a server, installing malware or influencing human behavior through a social attack.
- **Variety:** More specific enumerations of higher-level categories—e.g., classifying the external “bad guy” as an organized criminal group[^1] or recording a hacking action as SQL injection or brute force.

**Learn more here:**
- [https://github.com/vz-risk/dbir/tree/gh-pages/2023](https://github.com/vz-risk/dbir/tree/gh-pages/2023)—includes DBIR facts, figures and figure data
- [https://verisframework.org](https://verisframework.org)—features information on the framework with examples and enumeration listings
- [https://github.com/vz-risk/veris](https://github.com/vz-risk/veris)—features information on the framework with examples and enumeration listings

### Industry Labels

We align with the North American Industry Classification System (NAICS) standard to categorize the victim organizations in our corpus. The standard uses two- to six-digit codes to classify businesses and organizations. Our analysis is typically done at the two-digit level, and we will specify NAICS codes along with an industry label. For example, a chart with a label of Financial (52) is not indicative of 52 as a value. “52” is the NAICS code for the Financial and Insurance sector. The overall label of “Financial” is used for brevity within the figures. Detailed information on the codes and the classification system is available here:  
[https://www.census.gov/naics/?58967?yearbck=2012](https://www.census.gov/naics/?58967?yearbck=2012)

### I’m Sorry, This All Happened When?

While we have always listed the following facts in our Methodology section (because that is where this type of information belongs), we decided to also mention it here for the benefit of those who don’t make it that far into the report. Each year, the DBIR timeline for in-scope incidents is from November 1 of one calendar year through October 31 of the next calendar year. Thus, the incidents described in this report took place between November 1, 2021, and October 31, 2022. The 2022 caseload is the primary analytical focus of the 2023 report, but the entire range of data is referenced throughout, notably in trending graphs. The time between the latter date and the date of publication for this report is spent in acquiring the data from our global contributors, anonymizing and aggregating that data, analyzing the dataset and, finally, creating the graphics and writing the report. Rome wasn’t built in a day, and neither is the DBIR.

### Being Confident of Our Data

Starting in 2019 with slanted bar charts, the DBIR has tried to make the point that the only certain thing about information security is that nothing is certain. Even with all the data we have, we’ll never know anything with absolute certainty. However, instead of throwing our hands up and complaining that it is impossible to measure anything in a data-poor environment or, worse yet, just plain making stuff up, we get to work. This year, you’ll continue to see the team representing uncertainty throughout the report figures.

The examples shown in Figures 1, 2, 3 and 4 all convey the range of realities that could credibly be true. Whether it be the slant of the bar chart, the threads of the spaghetti chart, the dots of the dot plot or the color of the pictogram plot, all convey the uncertainty of our industry in their own special way.

![Figure 1. Example slanted bar chart (n=205)]

The slanted bar chart will be familiar to returning readers. The slant on the bar chart represents the uncertainty of that data point to a 95% confidence level (which is standard for statistical testing).

In layman’s terms, if the slanted areas of two (or more) bars overlap, you can’t really say one is bigger than the other without angering the math gods.

Much like the slanted bar chart, the spaghetti chart represents the same concept: the possible values that exist within the confidence interval; however, it’s slightly more involved because we have the added element of time. The individual threads represent a sample of all possible connections between the points that exists within each observation’s confidence interval. As you can see, some of the threads are looser than others, indicating a wider confidence interval and a smaller sample size.

![Figure 2. Example spaghetti chart]

The dot plot is another returning champion, and the trick to understanding this chart is to remember that the dots represent organizations. If, for instance, there are 200 dots (like in Figure 3), each dot represents 0.5% of organizations. This is a much better way of understanding how something is distributed among organizations and provides considerably more information than an average or a median. We added more colors and callouts to those in an attempt to make them even more informative.

![Figure 3. Example dot plot (n=672). Each dot represents 0.5% of organizations. Orange: lower half of 80%. Yellow: upper half of 80%. Green: 80%–95%. Blue: Outliers. 95% of orgs: 148–1,594,648. 80%: 1,274–438,499. Median: 29,774 (log scale).]

The pictogram plot, our relative newcomer, attempts to capture uncertainty in a similar way to slanted bar charts but is more suited for a single proportion.

We hope they make your journey through this complex dataset even smoother than previous years.

![Figure 4. Example pictogram plot (n=4,110). Each glyph represents 40 breaches.]

### Credit Where Credit Is Due

Turns out folks enjoy citing the report, and we often get asked how they should go about doing it.

You are permitted to include statistics, figures and other information from the report, provided that (a) you cite the source as “Verizon 2023 Data Breach Investigations Report” and (b) content is not modified in any way. Exact quotes are permitted, but paraphrasing requires review. If you would like to provide people a copy of the report, we ask that you provide them a link to [verizon.com/dbir](https://www.verizon.com/dbir) rather than a copy of the PDF.

### Questions? Comments? Organizing a Bank Run?

Let us know! Drop us a line at dbir@verizon.com, find us on LinkedIn, tweet @VerizonBusiness with #dbir. Got a data question? Tweet @VZDBIR!

If you are interested in becoming a contributor to the annual Verizon DBIR (and we hope you are), the process is very easy and straightforward. Please email us at dbircontributor@verizon.com.

---

## Introduction

> “Success is stumbling from failure to failure with no loss of enthusiasm.”  
> —attributed to Sir Winston Churchill

Hello and welcome old friends and new readers to the 2023 Verizon Data Breach Investigations Report! We are happy to have you join us once again as we take a look at the sordid underbelly of cybercrime and see what lessons we may collectively learn from doing so. It often seems that with every new defense strategy, appliance or Please-Save-Us-As-A-Service we create, buy or borrow, our adversaries are just as quick to adapt and find a new vantage point from which to attack. While this state of affairs is already unfortunate enough, it becomes worse still when we do not even require them to evolve their tactics because the old ones still work just fine.

Regardless of where we fall on the crazy-secure to not-so-secure spectrum, the quote above is a good road map to cybersecurity (and life in general). This report aims to take a look at the times when things did not work as intended—not to point fingers but to help us all learn and improve. In a time where almost everyone, corporations and individuals alike, is looking at ways to do more with less, we believe a close analysis of when our defenses failed can be very beneficial. While times of great change are always challenging, they often also prompt us to take stock of our situation and, if necessary, refocus both our viewpoint and our energies. Such is the case with the DBIR this year. As a team, we decided to take a step back toward the fundamental things that got us where we are, an intense focus on actual data breaches analyzed using our own VERIS Framework. And speaking of VERIS, one of the new goodies this refocusing brings is an even better mapping between VERIS and MITRE ATT&CK through a collaboration with MITRE Engenuity and the Center for Threat Informed Defense (CTID).[^2] It also helps that our parent organization, the Verizon Threat Research Advisory Center (VTRAC),[^3] shared the most breaches ever for us to analyze. Did you know it is VTRAC’s 20th anniversary this year? Save us a slice of that cake, boss!

As long-time readers will know, over the past few years, we have increasingly utilized non-incident data to add depth and dimension to our breach findings via various forms of research and analysis. While that remains a big part of what we do, as mentioned above, we did take purposeful steps toward a more direct focus on the breach side of the house this year. In short, the result of this was to make the report more concise and succinct and less unwieldy. This year we analyzed 16,312 security incidents, of which 5,199 were confirmed data breaches. As always, we hope you find this information informative, useful, easy to understand and actionable.

Finally, we thank our global data contributors most sincerely, as this report would quite literally not be possible without them. Of course, the same can be said of our readers, so please accept our deep gratitude for your continued support.

Sincerely,  
**The Verizon DBIR Team**  
C. David Hylender, Philippe Langlois, Alex Pinto, Suzanne Widup

**Very special thanks to:**
- Dave Kennedy and Erika Gifford from VTRAC.
- Kate Kutchko, Marziyeh Khanouki and Yoni Fridman from the Verizon Business Product Data Science Team.
- Gabriel Bassett for all the statistical tooling, charts and terrible jokes over the years. Good luck on your next adventure!

---

## Summary of Findings

Social Engineering attacks are often very effective and extremely lucrative for cybercriminals. Perhaps this is why Business Email Compromise (BEC) attacks (which are in essence pretexting attacks) have almost doubled across our entire incident dataset, as can be seen in Figure 5, and now represent more than 50% of incidents within the Social Engineering pattern.

![Figure 5. Pretexting incidents over time]

- **74%** of all breaches include the human element, with people being involved either via Error, Privilege Misuse, Use of stolen credentials or Social Engineering.
- **83%** of breaches involved External actors, and the primary motivation for attacks continues to be overwhelmingly financially driven, at **95%** of breaches.
- The three primary ways in which attackers access an organization are stolen credentials, phishing and exploitation of vulnerabilities.

![Figure 6. Select key enumerations]  
![Figure 7. Select enumerations in non-Error, non-Misuse breaches (n=4,291)]

- **Ransomware** continues its reign as one of the top Action types present in breaches, and while it did not actually grow, it did hold statistically steady at **24%**. Ransomware is ubiquitous among organizations of all sizes and in all industries.

![Figure 8. Ransomware action variety over time]

- More than **32%** of all Log4j scanning activity over the course of the year happened within 30 days of its release (with the biggest spike of activity occurring within 17 days).

![Figure 9. Percentage of Log4j scanning for 2022]

- Log4j was so top-of-mind in our data contributors’ incident response that **90%** of incidents with Exploit vuln as an action had “Log4j,” or “CVE-2021-44228” in the comments section. However, only **20.6%** of the incidents had comments.

![Figure 10. Percentage of identified Exploit vuln that was Log4j (n=81). Each glyph represents an incident.]

---

# 2 Results and Analysis

## Results and Analysis: Introduction

Hello friends, and welcome to the “Results and analysis” section. This is where we cover the highlights we found in the data this year. This dataset is collected from a variety of sources, including our own VTRAC investigators, reports provided by our data contributors and publicly disclosed security incidents.

Since data contributors come and go, one of our priorities is to make sure we can get broad representation on different types of security incidents and the countries where they occur. This ebb and flow of contributors obviously influences our dataset, and we will do our best to provide context on those potential biases where applicable.

As some of you may have noticed[^4] over the years, the incident data collection we do is based on the VERIS Framework. It has been the bedrock upon which our multiyear dataset has been built and is what allows us to be able to speak with confidence when trends in the attack landscape surface. Our dataset currently contains 953,894 incidents, of which 254,968 are confirmed breaches, and we can’t wait to celebrate[^5] with you when we reach 1 million[^6] incidents!

In VERIS, the core categories we use to describe an incident are called the 4As: Actor (who), Action (how), Asset (where) and Attribute (what). An incident needs all these four to be “complete,” even if at the end of the day some of those are unknown to the parties investigating the incident. Keep an eye out for our instructive callouts in each of those sub-sections giving more context on our VERIS categories.

Let’s go over the results for each one of these.

---

## Actors

Life can be scary and unpredictable, which is why we like to start our results discussion with the cozy and familiar Actor analysis. It really is true, as they say, that the only certainties in life are death, taxes and External actors.[^7]

As Figure 11 demonstrates, External actors were responsible for 83% of breaches, while Internal ones account for 19%. It is worth reminding our readers that Internal actors are not only responsible for intentional harm in these cases, but they are also just as likely[^8] to be responsible for Error actions. Regardless, the clear frequency of External actors as instigators of breaches is a datapoint that has held steady ever since we started this gig.

![Figure 11. Threat actors in breaches (n=5,177)]

### Actor Categories[^9]

- **External:** External threats originate from sources outside of the organization and its network of partners. Examples include criminal groups, lone hackers, former employees and government entities. This category also includes God (as in “acts of”), “Mother Nature” and random chance. Typically, no trust or privilege is implied for external entities.
- **Internal:** Internal threats are those originating from within the organization. This encompasses company full-time employees, independent contractors, interns and other staff. Insiders are trusted and privileged (some more than others).
- **Partner:** Partners include any third party sharing a business relationship with the organization. This includes suppliers, vendors, hosting providers and outsourced IT support. Some level of trust and privilege is usually implied between business partners. Note that an attacker could use a partner as a vector, but that does not make the partner the Actor in this case. The partner has to initiate the incident.

---

Long-time readers of the report will be similarly shocked to learn that Financial motives still drive the vast majority of breaches (Figure 12), showing growth in relation to last year with a whopping 94.6% representation in breaches. If we look inside to see which external actors are the hardest working, the top performer is Organized crime (Figure 13).

What is most interesting in Figure 13, however, is realizing that the internal variety of End-user shows up more often than the external variety State-sponsored attackers.[^10] Those organization employees are mostly involved in Misuse (read, internal malicious activity) and Errors (accidents), which suggests where we should be paying more attention on our day-to-day security management.

This is relevant because we were expecting some increased activity in State-sponsored attacks, be it Espionage-related or not, due to the ongoing conflict in Ukraine. Even with anecdotal evidence of increased ideology or hacktivism-related attacks stemming from the geopolitical discussion, it really isn’t making a dent in larger statistical terms. It is also worth noting that this kind of activity would also be unlikely to disrupt our average reader’s organization.[^11]

![Figure 12. Threat actor Motives in breaches (n=2,328)]  
![Figure 13. Threat actor Varieties in breaches (n=2,489)]

---

## Actions

Action, as the name would imply, is what brings dynamism to our report. What dastardly deeds have the threat actors been up to? If you replied “ransomware,” we’d say you have no imagination, but you would also be right. This pesky Malware variety has been holding our talking points hostage for years now, and we can’t scrounge up enough cryptocurrency to pay the ransom!

Figures 14, 15, 16 and 17 describe the top Action varieties (what happened in more detail) and vectors (how those actions came to pass).

### Action Categories[^12]

- **Hacking (hak):** attempts to intentionally access or harm information assets without (or exceeding) authorization by circumventing or thwarting logical security mechanisms.
- **Malware (mal):** any malicious software, script or code run on a device that alters its state or function without the owner’s informed consent.
- **Error (err):** anything done (or left undone) incorrectly or inadvertently.
- **Social (soc):** employ deception, manipulation, intimidation, etc., to exploit the human element, or users, of information assets.
- **Misuse (mis):** use of entrusted organizational resources or privileges for any purpose or manner contrary to that which was intended.
- **Physical (phy):** deliberate threats that involve proximity, possession or force.
- **Environmental (env):** not only includes natural events such as earthquakes and floods but also hazards associated with the immediate environment or infrastructure in which assets are located.

![Figure 14. Top Action varieties in breaches (n=4,354)]  
![Figure 15. Top Action varieties in incidents (n=14,829)]  
![Figure 16. Top Action vectors in breaches (n=3,194)]  
![Figure 17. Top Action vectors in incidents (n=10,502)]

---

As expected, the charts are led by either first-stage or single-stage attacks, namely Use of stolen creds for breaches and Denial of Service for incidents. This is consistent with previous years. What is concerning, if unsurprising, is having Ransomware take over the second spot in incidents, now being present in 15.5% of all incidents. Meanwhile, the share of Ransomware did not grow in breaches and held steady (statistically, at least) at 24%. You can see the evolution of both in Figure 18.

![Figure 18. Ransomware action variety over time]

That almost a quarter of breaches involve a Ransomware step continues to be a staggering result. However, we had been anticipating that Ransomware would soon be hitting its theoretical ceiling, by which we mean that all the incidents that could have Ransomware, would have. Ransomware is present today in more than 62% of all incidents committed by Organized crime actors and in 59% of all incidents with a Financial motivation, so sadly there is still some room for growth.

Eagle-eyed readers will notice the absence of Partner and Software update as action vectors for incidents this year, in contrast to last year’s “software supply chainpocalypse.”[^13] Instead, our collective Christmas was ruined by another Ghost of Technical Debt Past: the Log4j vulnerability popularly known as CVE-2021-44228.[^14]

We will be spending some time digging into the Log4j vulnerability in the “System Intrusion” section, but it is worth noting that the presence of the Exploit vuln action has kept stable in incidents and is actually less prominent in breaches, dropping from 7% to 5%. So, did the collective security industry sacrifice its holidays for nothing?

Not quite. This is one of those cases where the alternatives are just more popular. Use of stolen creds, our current champion, increased its share from 41.6% to 44.7%, which more than accounts for the drop in Exploit vuln.

More importantly, there was swift action from the community to spread awareness and patch all the different systems that had Log4j as a component. That surely helped avert a bigger disaster, so our success makes it look like it wasn’t a big deal after all.[^15] In fact, Log4j was so top-of-mind in our data contributors’ incident response that 90% of incidents with Exploit vuln as an action had “Log4j,” or “CVE-2021-44228” in the comments section. Granted, only 20.6% of the incidents had comments at all,[^16] so even if it can’t fully represent the whole dataset, it certainly speaks to how significant the vulnerability was in late 2021 and early 2022 for the incident response teams.

Finally, before I lose your attention, we should touch base on Loss.[^17] This action variety describes losing a physical device or media by accident and is often paired with the Carelessness action vector. It did show up fairly high in incidents. This is often because the data could not be confirmed as having been accessed and was therefore considered at risk rather than a breach. It is worth pointing out though that those were mostly concentrated in the data from some of our public sector contributors, where this sort of event is more tightly reported. Regardless, we know everyone was super excited about leaving the house again as the pandemic waned, but please keep an eye on your stuff when you go work from the coffee shop.

---

## Assets

In case you just wandered out of an Accounting 101 class, our Assets are more than the numbers that you list on the left side of your balance sheet.[^18] They encompass the entities that can be affected in an incident or breach and end up being manipulated by the threat actors for their nefarious goals. The callout box describes some of the most common top-level Assets in VERIS and some of the most common attack patterns that target them.

Figure 19 has the breakdown of varieties of Assets affected in breaches, and the results are pretty much what would be expected given the focus of System Intrusion, Basic Web Application Attacks and Social Engineering as the top attack patterns this year.

We can see a small fluctuation on the top three, as slightly less Servers were affected and slightly more User devices, but this order has held true for at least a couple of years, ever since Person overtook the second spot. Don’t forget that in VERIS, people are assets too,[^19] and they are the “where” that is affected by social threat actions.

![Figure 19. Assets in breaches (n=4,433)]

### Asset Categories[^20]

- **Server (srv):** a device that performs functions of some sort supporting the organization, commonly without end-user interaction. Where all the web applications, mail services, file servers and all that magical layer of information is generated. If someone has ever told you “the system is down,” rest assured that some Servers had their Availability impacted. Servers are common targets in almost all of the attack patterns, but especially in our System Intrusion, Basic Web Application Attacks, Miscellaneous Errors and Denial of Service patterns.
- **Person (per):** the folks (hopefully) doing the work at the organization. No AI chat allowed. Different types of Person will be members of different departments and will have associated permissions and access in the organization stemming from this role. At the very least they will have access to their very own User device and their own hopes and dreams for the future. Person is a common target in the Social Engineering pattern.
- **User device (usr):** the devices used by Persons to perform their work duties in the organizations. Usually manifested in the form of laptops, desktops, mobile phones and tablets. Common target in the System Intrusion pattern but also in the Lost and Stolen Asset pattern. People do like to take their little computers everywhere.
- **Network (net):** not the concept, but the actual network computing devices that make the bits go around the world, such as routers, telephone and broadband equipment, and some of the traditional in-line network security devices, such as firewalls and intrusion detection systems. Hey, Verizon is a Telecommunications company, OK?
- **Media (med):** precious diluted data in its most pure and crystalline form. Just kidding, mostly thumb drives and actual printed documents. You will see the odd full disk drive and actual physical payment cards from time to time, but those are more rare. Common in the Lost and Stolen Assets pattern.

---

Breaking the Asset varieties down further in Figure 20 showcases Web application and Mail servers on top, as would be expected, but it is interesting to see Person - Finance trending up from last year as we see a related growth in Pretexting social actions. We will be discussing those, and more specifically BECs, in the “Social Engineering” section of this report.

As a parting note, we continue to see very small numbers of incidents involving Operational Technology (OT), where the computers interface with heavy machinery and critical infrastructure, as contrasted with incidents involving Information Technology (IT), where we keep our cat pictures and internet memes. Industries like Manufacturing and Mining, Quarrying and Oil & Gas Extraction + Utilities[^21] continue to be relatively well-represented in our dataset, but reports of actual impact on OT devices are still too few for us to meaningfully write about in this report.

For those keeping track, we had a 3.4% showing of OT assets in breaches that declared their impact. In summary—keep your attention level high, given the potential impact when those systems are affected, but either those numbers are very low overall, or they just don’t make it to our contributors’ dataset due to national[^22] security concerns.

![Figure 20. Top Asset varieties in breaches (n=3,207)]

---

## Attributes

When VERIS describes Attributes, it is directly referencing the CIA triad in information security (InfoSec): Confidentiality, Integrity and Availability. It’s a tried-and-true method of understanding the potential impact of an incident by describing what properties of the asset were potentially affected.

The next time you meet an incident responder in the wild, know that all that goes through their mind is, “Did the asset or a copy of the data get out the door” (Confidentiality), “was it changed from a known and trusted state” (Integrity) and “do we still have access to it ourselves?” (Availability). Please offer them a word of kindness and a beverage, because it is a very tortured existence. If you are feeling cold, they are cold too.

### Attribute Categories[^23]

- **Confidentiality (cp):** refers to limited observation and disclosure of an asset (or data). A loss of confidentiality implies that data were actually observed or disclosed to an unauthorized actor rather than endangered, at-risk or potentially exposed (the latter fall under the attribute of Possession and Control). Short definition: limited access, observation and disclosure.
- **Integrity (ia):** refers to an asset (or data) being complete and unchanged from the original or authorized state, content and function. Losses to integrity include unauthorized insertion, modification and manipulation. Short definition: complete and unchanged from original.
- **Availability (au):** refers to an asset (or data) being present, accessible and ready for use when needed. Losses to availability include destruction, deletion, movement, performance impact (delay or acceleration) and interruption. Short definition: accessible and ready for use when needed.

---

One of the most interesting Attribute varieties we track year over year is the Confidentiality data varieties (Figure 21), or what kinds of data got out in a breach. Personal data represents Personally Identifiable Information (PII) from your customers, partners or employees, and it is the one that usually gets companies the most in trouble with regulators, as more and more privacy-related laws are passed around the world (although Medical data is a whole other ball of earwax).

![Figure 21. Top Confidentiality data varieties in breaches (n=5,010)]

### Virtual Money, Real Problems

One data variety really caught the DBIR team’s attention this year: Virtual currency. We saw a fourfold increase this year in the number of breaches involving cryptocurrency from last year. That is a far cry from the days of innocence in 2020 and earlier, when we got one or two cases maximum each year. If our cartoon animal NFTs had these kinds of returns, we can assure you we would be living large and writing this report from our Lambos, not from our parents’ basements.[^24]

Figures 23 and 24 show the top action varieties and vectors in breaches involving virtual currency, and it is a fierce competition between Exploit vulnerabilities, Use of stolen creds and Phishing. These types of breaches fall between the actual coin networks or exchanges being breached via their applications and application programming interfaces (APIs), or phishing and pretexting activity on chat platforms (like Discord) of the coin communities, where after a simple click on a link, suddenly your wallet is not yours anymore.

Having assets in virtual currency is a risky endeavor at best, even when there are no bad actors involved in rug-pulling.[^26] The added focus of threat actors on these types of assets doesn’t make the landscape any easier. Our parting message is that unless security is taken seriously in those cases, we, in fact, are not going to make it.

![Figure 23. Top Action varieties in breaches where virtual currency was involved (n=30)]  
![Figure 24. Top Action vectors in breaches where virtual currency was involved (n=48)]

Internal data and System data are usually byproducts of an extensive breach with multiple steps, as information from emails and documents are vacuumed up by threat actors. Credentials have really gained ground over the past five years, as the Use of stolen credentials became the most popular entry point for breaches.

Of course, we still get specific data being beset, such as Medical, Bank account information and Payment card data. Those could be specific, targeted events or just be a part of the data that is acquired during a ransomware attack with data exfiltration. And just in case you are not tired of us moaning about ransomware,[^25] please enjoy Figure 22, where we can see another impact of the ransomware growth as the Obscuration of data became the most common availability impact variety, handily overcoming plain old Loss of data.

![Figure 22. Availability variety over time]

---

# 3 Incident Classification Patterns

## Incident Classification Patterns: Introduction

One of the greatest gifts that evolution has granted the human race is a pattern-seeking brain. Was that just some swaying foliage in the jungle, or is a striped tiger sneaking around to pounce on us? The fact that humans are still around tells us we got that question right more often than we didn’t. Thankfully, we can also use our pattern-seeking superpowers to try to organize and make sense of all the different ways in which computers remind us they were a mistake.[^27]

Our incident patterns are, in a nutshell, a way to cluster similar incidents into an easy-to-remember shorthand. As we mentioned before, incidents are characterized by the 4As of VERIS, and we can avoid a long descriptive paragraph every time by classifying our incidents in this way.[^28] Our eight patterns, and how they are defined, can be found in Table 1.

![Figure 25. Patterns over time in incidents]

This year, we are showcasing a detailed breakdown of ATT&CK Techniques[^29] and Center for Internet Security (CIS) Critical Security Controls[^30] related to certain patterns, as those are the places that make sense so we don’t repeat ourselves throughout this report. We are proud of the ATT&CK mappings release, as they represent the culmination of a multiyear collaboration with MITRE CTID in creating and maintaining a working relationship between its standard and VERIS. You can read more about this in our Appendix B.

So, enjoy the cognitive load we just removed from your (pattern-seeking) grey matter as we deep dive into specific results and detailed analysis for each pattern.

As we have in prior years, here we present our Incident Classification Patterns (patterns) and show how they fared year over year. Figure 25 shows the patterns over time for incidents, and you can see that Denial of Service is top of the heap, as it has been for several years.

When you contrast this graphic with Figure 26, you can see how different the environment looks when we are focused on those incidents where there was confirmed data loss.

The System Intrusion pattern—with its more complex attacks—has been an overachiever and includes multistep attacks that feature ransomware. But we’re getting ahead of ourselves. Let’s move into the detailed pattern sections for the full story.

| Pattern | Description |
| :--- | :--- |
| **Basic Web Application Attacks** | These attacks are against a Web application, and after the initial compromise, they do not have a large number of additional Actions. It is the “get in, get the data and get out” pattern. |
| **Denial of Service** | These attacks are intended to compromise the availability of networks and systems. This includes both network and application layer attacks. |
| **Lost and Stolen Assets** | Incidents where an information asset went missing, whether through misplacement or malice, are grouped into this pattern. |
| **Miscellaneous Errors** | Incidents where unintentional actions directly compromised a security attribute of an information asset fall into this pattern. This does not include lost devices, which are grouped with theft instead. |
| **Privilege Misuse** | These incidents are predominantly driven by unapproved or malicious use of legitimate privileges. |
| **Social Engineering** | This attack involves the psychological compromise of a person that alters their behavior into taking an action or breaching confidentiality. |
| **System Intrusion** | These are complex attacks that leverage malware and/or hacking to achieve their objectives, including deploying Ransomware. |
| **Everything Else** | This “pattern” isn’t really a pattern at all. Instead, it covers all incidents that don’t fit within the orderly confines of the other patterns. Like that container where you keep all the cables for electronics you don’t own anymore: Just in case. |

*Table 1. Incident Classification Patterns*

![Figure 26. Patterns over time in breaches]

---

## System Intrusion

### Summary

This pattern largely pertains to attacks perpetrated by more dedicated criminals who utilize their expertise in hacking and ready access to malware to breach and/or impact organizations of different sizes, frequently leveraging Ransomware as their means of getting a payday.

#### What Is the Same?

Ransomware continues to dominate this pattern as attackers leverage a bevy of different techniques to compromise an organization.

#### Pattern Overview

- **Frequency:** 3,966 incidents, 1,944 with confirmed data disclosure
- **Threat actors:** External (96%), Internal (4%), Multiple (2%), Partner (1%) (breaches)
- **Actor motives:** Financial (97%), Espionage (3%) (breaches)
- **Data compromised:** Other (42%), Personal (34%), System (31%), Internal (24%) (breaches)

#### Relevant ATT&CK Techniques

- **Exploit vuln (VERIS):**
  - Exploitation for Privilege Escalation: T1068
  - Exploit Public-Facing Application: T1190
  - Exploitation for Defense Evasion: T1211
  - Exploitation for Credential Access: T1212
  - Exploitation of Remote Services: T1210
  - External Remote Services: T1133
  - Vulnerability Scanning: T1595.002
- **Use of stolen creds (VERIS):**
  - Compromise Accounts: T1586
    - Social Media Accounts: T1586.001
    - Email Accounts: T1586.002
  - External Remote Services: T1133
  - Remote Services: T1021
    - Remote Desktop Protocol: T1021.001
  - Use Alternate Authentication Material: T1550
    - Web Session Cookie: T1550.004
  - Valid Accounts: T1078
    - Default Accounts: T1078.001
    - Domain Accounts: T1078.002
    - Local Accounts: T1078.003
    - Cloud Accounts: T1078.004
- **Tactics:**
  - Execution: TA0002
  - Persistence: TA0003
  - Privilege Escalation: TA0004
  - Defense Evasion: TA0005
  - Credential Access: TA0006

---

### This Is Mine, and This Is Mine …

Imagine strolling into your office one morning only to discover an alarming desktop image from some criminal group with a cringeworthy name requesting Bitcoin (BTC) in exchange for the return of all your data. Hopefully, being the avid DBIR reader you are, you would have recent and well-tested backups to restore from. However, what if these criminals do not stop at only encrypting your data but also threaten to leak portions of your more sensitive information unless paid? Oftentimes it appears that no matter how fast our defenses and practices evolve, attackers adapt theirs just as quickly.

This creates a perpetual arms race, and nowhere is it better represented than in the System Intrusion pattern. We frequently think of the threat actors in this pattern as the “hands on keyboard” type of attackers. While they might leverage automation to gain a foothold, once they are inside the organization, they utilize finely honed skills to bypass controls and achieve their goals. As Figure 28 illustrates, this commonly includes Ransomware. They use a variety of tools to traverse your environment and then pivot, including using phishing and stolen credentials to obtain access and adding backdoors to maintain that access and leverage vulnerabilities to move laterally. We can see these attacks more clearly when we break them into three smaller, more consumable portions.循环 Namely, the initial access phase, the breach escalation and the results. Figure 27 has a breakdown of the Action-Asset combinations that we see during different steps of the attack.

![Figure 27. Steps in System Intrusion breaches]  
![Figure 28. Action varieties in System Intrusion incidents (n=2,700)]  
![Figure 29. Action vectors in System Intrusion incidents (n=787)]

### Jiggling Locks

When looking at Figure 27, we see the clear leaders for the initial access—a great deal of hacking servers and an almost equal amount of unknown actions. In terms of hacking, 9% of incidents involve Exploiting vulnerabilities and 8% involve the Use of stolen credentials. When we examine only our incidents that contain the exploitation of vulnerabilities, we find those vulnerabilities are largely exploited via Web applications (Figure 29).

In addition, we see some User devices being directly targeted, and we also observe Phishing in roughly 6% of cases. Phishing provides just another means of ingress, either to get a set of usable credentials or to deploy a payload on a user system. Malware is largely distributed via email and often comes in the form of Microsoft Office documents (see Figure 30). This makes sense when you consider that most of these documents now have the ability to run code on the client system, which is extremely useful if you’re an attacker.

![Figure 30. Malware delivery method proportion per organization]

Admittedly, there are many cases in which we do not know the exact means of entry the attacker used. However, these pathways of Exploiting vulnerabilities, Using stolen credentials and Phishing are very similar to previous years’ findings, and let’s face it, they are straight out of InfoSec 101. This again demonstrates the importance of the fundamentals.

### Well, That Escalated Quickly.

Once attackers have access to your environment, they will typically look for ways to escalate privileges, maintain persistence and locate paths to move across the organization to achieve their ultimate goal, whatever that may be. For those ATT&CK aficionados out there, you may be thinking this sounds like we’re talking about a big chunk of that matrix. Well, we are. While we have a higher view of the incidents, we do not always have the telemetry required to find out exactly what techniques were used. However, below we discuss some of the additional hacking techniques and malware capabilities that we can track.

Malware that maintains command and control (C2) access to the system was witnessed in about 5% of incidents. Also present are the more typical types of malware that profile hosts, scan networks and (a local favorite) dump passwords. Lastly, just in case you thought the 2010s were behind us, we even found a handful of crypto miners in this dataset. There were not enough for us to confirm that they are back en vogue, but definitely enough to confirm that certain parties still consider compromised servers as free real-estate from which to mine.

### Results

With such a high reliance upon the installation of malware across this pattern (either in the form of Ransomware, backdoors or payment card skimming malware) we shouldn’t be too surprised when we find servers that have illicit software installed as the most common combination of Attribute and Asset. The second most common is the exfiltration of data, and rounding out the trio is the loss of availability, aka rendering your data unreadable. These top three describe the final steps associated with many of these attacks quite well—attackers find a way to install their payload across the organization, steal data and then encrypt the systems on their way out.

### Ransomware … Seriously, We’re Still Doing This Section?

Ransomware continues to be a major threat for organizations of all sizes and industries and is present in 24% of breaches. Of those cases, 94% fall within System Intrusion. While Ransomware has increased only slightly this year, it is so ubiquitous that it may simply be a threat that we will always have to protect against—91% of our industries have Ransomware as one of their top three actions.

![Figure 31. Action vectors for Ransomware (n=690)]

To understand how these attacks occur, it is often useful to look at the top Vectors for the actions. In this case, the most common ways in are Email, Desktop sharing software and Web applications (Figure 31). Email as a vector isn’t going away any time soon. The convenience of sending your malware and having the user run it for you makes this technique timeless. The next most common vector, Desktop sharing software, makes sense, since these breaches and incidents frequently leverage some means of accessing a system. What better way to do that than by using a built-in tool such as RDP or a third-party version to provide the criminal mastermind a nice GUI?

### Splitting the Log4j

As we DBIR authors groggily awoke from our hyperbolic slumber to start collecting and writing about all the major happenings in the cybersecurity world, we saw yet another major cybersecurity event had slowly played out after the cutoff of our data collection. This occurred first in 2020, with SolarWinds,[^31] and history has repeated itself in 2021 with Log4j,[^32] opening what seems to be a Pandora’s box of vulnerabilities. However, there is one advantage to waiting—we get to watch as the dust settles and provide an objective analysis as to what actually occurred. There was a great deal of uncertainty and complexity surrounding the incidents involving the Log4j vulnerability. One of which was the fact that no one really understood the full scope of the breach as it was not simply in one software product but was actually in a library used by numerous applications and programs (both purchased and open sourced.)

A quick recap of the event is perhaps warranted to refresh everyone’s memory. The vulnerability was disclosed in late November 2021, and within a few days the first exploitations began to appear. The vulnerability, given the designation of CVE-2021-44228, was given a whopping criticality score of 10.[^33] By the end of December, 0.003% of the scanning activity captured by honeypots were actively poking and prodding for this specific vulnerability. While that number might seem small, the velocity was rather striking, with more than 32% of all Log4j scanning activity over the course of the year happening within 30 days of its release (the biggest spike of activity occurred within 17 days, as Figure 32 shows). This velocity is an interesting comparison versus organizations’ median time to patch, which is currently 49 days for critical vulnerabilities, a number that has stayed relatively consistent over the years.

![Figure 32. Percentage of Log4j scanning for 2022]

However, it may not have been as big of a disaster as many predicted. When examining the DBIR incident dataset, we actually saw a decrease of vulnerability exploitation leading to incidents and breaches, with Log4j being mentioned in 0.4% of our incidents (just under a hundred cases). However, when examining these cases, we found that Log4j was used by a variety of actors to achieve an assortment of different objectives, with 73% of our cases involving Espionage and 26% involving Organized crime. Given the nature of the vulnerability, allowing remote code execution, we predictably saw a lot of malware activity associated with it, such as Backdoors and Downloaders to pull in additional hosts. Finally, in about 26% of the cases, we saw the exploit of Log4j being leveraged as part of Ransomware attacks, which only goes to show that attackers will leverage whatever beachhead they can get.

Based on some of the vulnerability scanning data we analyzed (as in the good folks scanning for vulnerabilities, not the bad ones) we found that vulnerable Log4j showed up in 8% of organizations. And in other somewhat surprising news, we also found that there was a greater percentage of Log4j installations that were end of life (EOL) with 14% of organizations, even if they weren’t actually vulnerable to Log4j explicitly. Lastly, 22% of organizations had multiple (i.e., more than one) instances of the Log4j vulnerability in their systems.

This underlying vulnerability in a dependency has brought back the discussion around having a software bill of materials (SBOM). You may think that SBOM is a term kids are throwing around in between their “no caps” and “bussin,” but its goal is to help organizations understand all the ingredients (software packages and libraries) that go into making the software their organization relies upon. Having a mature SBOM process across their ecosystem enables organizations to quickly identify vulnerabilities within the underlying libraries and help with future remediation processes for something like Log4j.

### CIS Controls for Consideration

Bearing in mind the breadth of activity found within this pattern and how actors leverage a wide collection of techniques and tactics, there are a lot of safeguards that organizations should consider implementing. A small subset—including the CIS Control Number—is below, which should serve as a starting point for building out your own risk assessments to determine what controls are appropriate to your organization’s risk profile.

#### Protecting Devices
- **Secure Configuration of Enterprise Assets and Software [4]**
  - Establish and Maintain a Secure Configuration Process [4.1]
  - Establish and Maintain a Secure Configuration Process for Network Infrastructure [4.2]
  - Implement and Manage a Firewall on Servers [4.4]
  - Implement and Manage a Firewall on End-User Devices [4.5]
- **Email and Web Browser Protection [9]**
  - Use DNS Filtering Services [9.2]
- **Malware Defenses [10]**
  - Deploy and Maintain Anti-Malware Software [10.1]
  - Configure Automatic Anti-Malware Signature Updates [10.2]
- **Continuous Vulnerability Management [7]**
  - Establish and Maintain a Vulnerability Management Process [7.1]
  - Establish and Maintain a Remediation Process [7.2]
- **Data Recovery [11]**
  - Establish and Maintain a Data Recovery Process [11.1]
  - Perform Automated Backups [11.2]
  - Protect Recovery Data [11.3]
  - Establish and Maintain an Isolated Instance of Recovery Data [11.4]

#### Protecting Accounts
- **Account Management [5]**
  - Establish and Maintain an Inventory of Accounts [5.1]
  - Disable Dormant Accounts [5.3]
- **Access Control Management [6]**
  - Establish an Access Granting/Revoking Protocol [6.1]
  - Require MFA for Externally-Exposed Applications [6.3]
  - Require MFA for Remote Network Access [6.4]

#### Security Awareness Programs
- **Security Awareness and Skills Training [14]**

---

### Just One More (Ransomware) Note

![Figure 33. 95% and 80% confidence intervals of Ransomware incident cost per complaint (n=2,575)]

Since we are hot on the subject of ransomware, we thought it would be interesting to revisit the breach impact data provided by our partner, the FBI Internet Crime Complaint Center (IC3).[^34]

When we last reviewed this data in the 2021 DBIR, we found that 90% of the incidents reported to the IC3 had no financial loss result, but for the remaining 10%, the median amount lost was $11,500, and the range of losses in 95% of the cases were between $70 and $1.2 million.

In reviewing Figure 33, of the incidents with loss, the calculated median more than doubled to $26,000, and the 95% range of losses expanded to sit between $1 and $2.25 million, putting that upper bound in scarier territory if you are a small business. The FBI did find that only 7% of the incidents had losses in this case, so it’s not all bad news.

Now, before any one of you makes a snarky quip about inflation and the base rate of the economy, here is the unusual part: When combining the paid-out transactions to the threat actors on the same time period, we get a much smaller median—$10,000 (Figure 34), and this median is actually less than the two previous years when the DBIR team has had access to this dataset.

![Figure 34. Median transaction size for Ransomware based on FBI IC3 complaints]

What this suggests is that the overall costs of recovering from a ransomware incident are increasing[^35] even as the ransom amounts are lower. This fact could be suggesting that the overall company size of ransomware victims is trending down. Even though the amounts requested by the threat actors would be smaller for those smaller companies—they want to get any money they can—the added costs of recovering their IT infrastructure under a backdrop of likely technical debt would spike their overall losses. This is conjecture, as we don’t have the company size data and not all complaints have the associated transaction value data in this specific dataset. Even so, this is a result we have been expecting to see due to the increase of automation and efficiency of ransomware operators. Regardless, it’s fair to say that an ounce of prevention is worth a pound of cure,[^36] so we cannot emphasize enough the need of having a plan and/or incident response resources at the ready ahead of your next unscheduled encryption event.

---

[^1]: By organized criminal group, we mean a group that does this for a living and has a set process they use repeatedly, not Tony Soprano and his band of merry men.
[^2]: [https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/](https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/)
[^3]: [https://www.verizon.com/business/resources/reports/verizon-threat-research-advisory-center/](https://www.verizon.com/business/resources/reports/verizon-threat-research-advisory-center/)
[^4]: We certainly won’t shut up about it.
[^5]: Not sure if we should be celebrating security incidents, but everyone loves a round number.
[^6]: Here’s hoping being a millionaire doesn’t get to our dataset’s head, and they decide to join the “Great Resignation” and retire in some tropical tax haven.
[^7]: That’s what they say, right?
[^8]: OK, actually twice as likely.
[^9]: [https://verisframework.org/actors.html](https://verisframework.org/actors.html)
[^10]: Huge win for anarchists and other state-abolishing ideologies, if you ask us.
[^11]: No, Mr. Bond, MI6 does not represent our average reader.
[^12]: [https://verisframework.org/actions.html](https://verisframework.org/actions.html)
[^13]: Wouldn’t you know, the moment we mention anything has not had relevance in our dataset, something new happens to remind us that change is the only constant. Best of luck for the teams responding to the 3CX supply-chain breach in late March 2023 as we close out this section. Make sure to keep copious notes so we can talk about it in a future edition of the report.
[^14]: Just rolls off the tongue, doesn’t it?
[^15]: Who here was working on the Y2K bug? Don’t forget to schedule your shingles vaccine!
[^16]: In everyone’s defense, most of the data sharing happening here is machine-to-machine. Long gone are the days of artisanal, bespoke, VERIS-coded incidents for most of our contributors.
[^17]: For the extremely online folks, we apologize for the psychic damage.
[^18]: However, not caring for them properly could cause liabilities that would go on the right side.
[^19]: Just ask your organization’s HR department.
[^20]: [https://verisframework.org/assets.html](https://verisframework.org/assets.html)
[^21]: We know, it’s a mouthful.
[^22]: From any country really.
[^23]: [https://verisframework.org/attributes.html](https://verisframework.org/attributes.html)
[^24]: Our Lambos might be parked in our parent’s garage, though.
[^25]: We’re not bitter; you’re bitter.
[^26]: That rug really tied the room together, man!
[^27]: As opposed to ChatGPT and other AI platforms, which insist that humans may be the mistake.
[^28]: It’s like they say, a pattern is worth about four A’s.
[^29]: [https://attack.mitre.org/](https://attack.mitre.org/)
[^30]: [https://www.cisecurity.org/controls](https://www.cisecurity.org/controls)
[^31]: [https://www.cisa.gov/news-events/news/cisa-issues-emergency-directive-mitigate-compromise-solarwinds-orion-network](https://www.cisa.gov/news-events/news/cisa-issues-emergency-directive-mitigate-compromise-solarwinds-orion-network)
[^32]: [https://www.cisa.gov/news-events/news/cisa-issues-emergency-directive-requiring-federal-agencies-mitigate-apache-log4j](https://www.cisa.gov/news-events/news/cisa-issues-emergency-directive-requiring-federal-agencies-mitigate-apache-log4j)
[^33]: Though insiders have indicated that it could have gone up to 11.
[^34]: [https://www.ic3.gov](https://www.ic3.gov)
[^35]: Feel free to make that inflation joke now.
[^36]: This sentence was famously said by a man who flew a kite with a key in a thund

---

erstorm. Makes you think.
2023 DBIR Incident Classification Patterns 30

Social
Engineering
Summary
|     | Frequency | 1,700 incidents,    |                  |
| --- | --------- | ------------------- | ---------------- |
|     |           | 928 with confirmed  | Relevant ATT&CK  |
Social Engineering incidents have
|     |     | data disclosure | techniques |
| --- | --- | --------------- | ---------- |
increased from the previous year
| largely due to the use of Pretexting,  | Threat actors | External (100%),  |     |
| -------------------------------------- | ------------- | ----------------- | --- |
which is commonly used in BEC, almost  Multiple (2%),   Compromise Accounts: T1586
doubling since last year. Compounding  Internal (1%),     – Email Accounts: T1586.002
| the frequency of these attacks, the  |     | Partner (1%)  |     |
| ------------------------------------ | --- | ------------- | --- |
| median amount stolen from these      |     | (breaches)    |     |
Establish Accounts: T1585
attacks has also increased over the
  – Email Accounts: T1585.002
|     | Actor motives | Financial (89%),  |     |
| --- | ------------- | ----------------- | --- |
last couple of years to $50,000.
|     |     | Espionage (11%)  | External Remote Services: T1133 |
| --- | --- | ---------------- | ------------------------------- |
(breaches)
| What is the same? |       |                     | Internal Spearphishing: T1534 |
| ----------------- | ----- | ------------------- | ----------------------------- |
|                   | Data  | Credentials (76%),  |                               |
Phishing and Pretexting continue
|     | compromised | Internal (28%),   | Phishing: T1566  |
| --- | ----------- | ----------------- | ---------------- |
to dominate this pattern, thus  Other (27%),    –  Spearphishing Attachment:
| ensuring that email remains one  |     | Personal (26%)  | T1566.001 |
| -------------------------------- | --- | --------------- | --------- |
of the most common means  (breaches)   –  Spearphishing Link:
| of influencing individuals. |     |     | T1566.002 |
| --------------------------- | --- | --- | --------- |
  –  Spearphishing via Service:
T1566.003
Phishing for Information: T1598
| Professional  | However, this section is about another,  |     |                              |
| ------------- | ---------------------------------------- | --- | ---------------------------- |
|               | not-so-useful-to-society, form of        |     |   –  Spearphishing Service:  |
| engineers?    | engineer—the social engineer. This       |     | T1598.001                    |
pattern focuses on tactics used
Use Alternate Authentication
by threat actors that leverage our
Material: T1550
| Engineering is a beautiful combination  | innate helpful nature to manipulate  |     |     |
| --------------------------------------- | ------------------------------------ | --- | --- |
  –  Application Access Token:
| of math and physics applied to a  | and victimize us. These attackers  |     |     |
| --------------------------------- | ---------------------------------- | --- | --- |
T1550.001
| practical and meaningful end—or      | use a combination of strategies to    |     |     |
| ------------------------------------ | ------------------------------------- | --- | --- |
| so we’re told. However, much to our  | accomplish this: by creating a false  |     |     |
Valid Accounts: T1078
parents’ disappointment, most of  sense of urgency for us to provide a
  –  Domain Accounts:
us are not engineers, but only an  reply or to perform an action, a fake
T1078.002
infinite collection of monkeys tied to  petition from authority, or even hijacking
| typewriters. (Legend has it we will  | existing communication threads to  |     |     |
| ------------------------------------ | ---------------------------------- | --- | --- |
compose “Hamlet” by pure chance any  convince us to disclose sensitive data
| day now. Watch your back, GPT-4.)  | or take some other action on their  |     |     |
| ---------------------------------- | ----------------------------------- | --- | --- |
behalf. Social engineering has come
a long way from your basic Nigerian
Prince scam to tactics that are much
more difficult to detect. This increased
sophistication explains why Social
Engineering continues to rise and
currently resides in our top three
patterns (accounting for 17% of our
Breaches and 10% of Incidents).
2023 DBIR Incident Classification Patterns 31

Please use this actors prior to the attack. For example,
they might have spun up a look-alike
bank account domain that closely resembles that
of the requesting party and possibly
number going even updated the signature block to
include their number instead of the
forward. vendor they’re pretending to represent.
These are just two of the numerous
subtle changes that attackers can
There is a common misconception make in order to trick their marks—
when it comes to distinguishing especially those who are constantly
phishing from the more complex forms bombarded with similar legitimate
of social engineering. Raise your hand requests. Perhaps this is one of the
if you haven’t received an email with reasons BEC attacks have almost
a dubious attachment or a malicious doubled across our entire incident
link requesting that you update your dataset, as can be seen in Figure 36,
password. Nobody? Yeah, that’s what and now represent more than 50%
we thought. This is phishing, and it of incidents within this pattern.
makes up 44% of Social Engineering
Attack type doesn’t appear to have
incidents. Now, who has received an
much of an effect on click/open rate.
email or a direct message on social
The median fail rates for attachment
media from a friend or family member
and link campaigns are 4% and 4.7%
who desperately needs money?
respectively, and the median click
Probably fewer of you. This is social Figure 35. Action varieties in Social
rate for data entry campaigns is 5.8%
engineering (pretexting specifically) and Engineering incidents (n=1,696)
(though the data entry rate is 1.6%).
it takes more skill. The most convincing
social engineers can get into your head
and convince you that someone you
love is in danger. They use information
they have learned about you and your
loved ones to trick you into believing
the message is truly from someone
you know, and they use this invented
scenario to play on your emotions and
create a sense of urgency. Figure 35
shows that Pretexting is now more
prevalent than Phishing in Social
Engineering incidents. However,
when we look at confirmed breaches,
Phishing is still on top.
One of the more complex social
attacks is the BEC. In these pretexting
attacks, actors leverage existing email
threads and context to request that the
recipient conduct a relatively routine
task, such as updating a vendor’s bank
account. However, the devil is in the
details, and the new bank account
belongs to the attacker, so all payments
the victim makes to that account will
make zero dents in what they owe
that vendor. These types of attacks
are often much harder to detect due
Figure 36. Pretexting incidents over time
to the groundwork laid by the threat
2023 DBIR Incident Classification Patterns 32

Inconspicuous Two paths the attackers are able to spin a
credible story (albeit fictitious) to
beginnings diverged, convince someone to do their bidding.
Persuading someone to change the
etc., etc. bank account for the claimed recipient,
Because this pattern is largely based for example, is found in 56% of
on human-targeted attacks, it makes incidents. Of course, a combination of
sense that the very first action in this What happens after that initial email tactics can also be used. The attackers
pattern will be some form of phishing is where things often diverge. There may leverage their acquired access to
or pretexting email (Figure 37). In fact, are two major routes that the attacks a user’s inbox to look for an email chain
email alone makes up 98% of the vector typically take. Most commonly, if the they can hijack or search the victim’s
for these incidents, with the occasional attackers are soliciting credentials and address book to find people who can
sprinkling of other communication obtain them, then they will leverage be targeted further. It’s not uncommon
methods, such as phone, social media those credentials to access the user’s for attackers to add forwarding rules
or some internal messaging app that inbox (found in 32% of incidents). to make sure their activities stay
some folks might be Slacking off on The road less traveled is where—by undetected as long as possible, which
(cough, cough). simply using email communication— is why …
Figure 37. Steps in Social Engineering breaches
2023 DBIR Incident Classification Patterns 33

Time is of CIS Protect accounts
the essence. Controls for Account Management [5]
– Establish and Maintain an
consideration Inventory of Accounts [5.1]
When responding to social engineering – Disable Dormant Accounts [5.3]
attacks (and the same could be said
of most attacks), rapid detection and There are a fair number of controls to Access Control Management [6]
response is key. The importance of consider when confronting this complex – Establish an Access Granting
timely detection is highlighted by the threat, and all of them have pros and Process [6.1]
increasing median cost of BECs, as cons. Due to the strong human element – Establish an Access Revoking
shown in Figure 38, which has risen associated with this pattern, many of Process [6.2]
steadily from 2018 and now hovers the controls pertain to helping users – Require MFA for Externally-
around the $50,000 mark. However, detect and report attacks as well as Exposed Applications [6.3]
unlike the times we live in, this section protecting their user accounts in the – Require MFA for Remote Network
isn’t all doom and gloom. Fortunately event that they fall victim to a phishing Access [6.4]
for the victims, law enforcement has lure. Lastly, due to the importance of
developed a process by which they the role played by law enforcement in Security awareness
collaborate with banks to help recover responding to BECs, it is key to have programs
money stolen from attacks such plans and contacts already in place.
as BEC. More than 50% of victims Security Awareness and Skills
were able to recover at least 82% of Training [14]
their stolen money. This illustrates
the importance of ensuring that Why do BECs work? Although not part of the CIS Controls,
their employees feel comfortable a special focus should be placed on
reporting potential incidents to BEC and processes associated with
Much like Ransomware,
security, since their willingness to do updating bank accounts.
which is the monetization of
so greatly improves the organization’s
access to an organization’s
ability to respond. With this in mind, Managing incident response
network, BECs are just one
we encourage companies to step
of the many means criminals
away from the “phishing exercises Incident Response Management [17]
have of monetizing access to
will continue until click rates – Designate Personnel to Manage
a user’s inbox and contacts.
improve” stance and adopt a more Incident Handling [17.1]
collaborative approach to security. • BECs can be targeted – Establish and Maintain Contact
Information for Reporting Security
internally, meaning that
Incidents [17.2]
the attacker will leverage a
– Establish and Maintain an
compromised employee’s
Enterprise Process for Reporting
email account to target
Incidents [17.3]
their own organization by
impersonating the user. We
commonly see actors trying
to redirect payroll deposits
into an account they control.
• Alternatively, actors can target
partners by using access to
an employee’s email account,
so they can impersonate that
user and request updates to
payments in order to include
their own bank account.
Figure 38. Median transaction size for
BECs (n=73,420). Based on FBI IC3
complaints where a transaction
occurred.
2023 DBIR Incident Classification Patterns 34

Basic Web
Application Attacks
Summary
Frequency 1,404 incidents,
1,315 with confirmed Relevant ATT&CK
While representing approximately one-
data disclosure
fourth of our dataset, these breaches techniques
and incidents tend to be largely Threat actors External (100%),
driven by attacks against credentials, Internal (1%), Brute Force: T1110
with the attackers then leveraging Multiple (1%) – Credential Stuffing:
those stolen credentials to access (breaches) T1110.004
a variety of different resources.
– Password Cracking:
Actor motives Financial (95%),
T1110.002
Espionage (4%),
– Password Guessing:
What is the same? Fun (1%) (breaches)
T1110.001
Poorly picked and protected passwords – Password Spraying:
Data Credentials (86%),
continue to be one of the major sources T1110.003
compromised Personal (72%),
of breaches within this pattern.
Internal (41%),
Compromise Accounts: T1586
Other (19%)
– Email Accounts: T1586.002
(breaches)
Exploit Public-Facing Application:
T1190
Who dunnit? This pattern, which accounts for 25%
of our breaches, consists largely External Remote Services: T1133
of leveraging stolen credentials
While it may liven up our humdrum and vulnerabilities to get access to Valid Accounts: T1078
existence to imagine the threat actors an organizations’ assets. With this – Default Accounts:
behind breaches as characters from a beachhead, the attackers can then do T1078.001
game of Clue (the cyber version),37 it a variety of things, such as stealing – Domain Accounts:
is more likely to have been an average key information hiding in emails or T1078.002
Jane Doe using stolen credentials or taking code from repositories. While
some well-known vulnerability. these attacks aren’t complicated, Use Alternate Authentication
they certainly are effective and have Material: T1550
remained a relatively stable part of our – Application Access Token:
dataset, which prompts us to discuss T1550.001
once again (drum roll, please), the
importance of multifactor authentication Active Scanning: T1595
(MFA) and patch management!38 – Vulnerability Scanning:
T1595.002
37 Was the breach caused by the mysterious Spiderlady via a complicated zero day on an internet-facing
server? Or was it perpetrated by the Sophisticated Panda using drones inside a Kubernetes cluster?
38 Yes, it is the “Groundhog Day” of InfoSec topics. I bet you can find it in our past reports!
2023 DBIR Incident Classification Patterns 35

Initial access Breach
escalation
86% of the breaches, as you can
see in Figure 39, involve the Use of
stolen credentials. And where better Even though we refer to these attacks
to use those credentials than against as “basic,” they’re not simply “one and
the various web servers that contain done” incidents where credentials are
our sensitive information? The other leveraged against a web application and
major part of the puzzle within this the attacker then goes on their merry
pattern is the use of exploits. This way. There is often some sort of middle
is where attackers have an exploit step (Figure 40). For instance, malware
and the victims just happen to have a is frequently one of the primary means
vulnerability (handy for the criminal). of maintaining persistence (look at
This typically occurs in only about us, using them fancy ATT&CK terms),
10% of the dataset, and while that with Backdoor or C2 in about 2%
may sound like an insignificant of the incidents. In other cases, the
number of breaches, unpatched attackers will leverage their current
vulnerabilities are still the bread and access to conduct additional attacks.
butter for many attackers, with 50%
of organizations experiencing over 39
Web application attacks this year.39
Figure 39. Top Action varieties for
Basic Web Application Attacks
breaches (n=1,287)
39 One of the advantages to running these types of attacks is that the server never tires, never sleeps,
it just throws exploits at everyone continually, night and day—unlike your humble cybersecurity
analyst who needs at least four coffees a day and nine hours of sleep.
2023 DBIR Incident Classification Patterns 36

Impacts
With regard to impact, we commonly
see that after Web applications, Mail
servers are one of the preferred
targets for attackers. This makes
sense, because hidden away in our
inboxes among the hundreds of unread
emails40 there are often key internal
documents (41% of breaches involve
mail servers) or, sadly, credentials to
some other system. The findings for
this pattern show that attackers can
access Internal data (41%), Medical
data (6%) and even Banking data
(6%) using simple inbox mining tactics
(again, reminding us of the importance
of good email and server hygiene).
Figure 40. Steps in Basic Web Application Attacks
40 Sorry, Grandma.
2023 DBIR Incident Classification Patterns 37

You can’t eat place. We might have a good idea in this year demonstrated some of those
terms of the different ways that one shortcomings. In some cases, criminals
just one. would be capable of getting credentials, used social engineering to convince
such as buying them from password users to accept the authentication
stealers who are nabbing them through attempts. In other instances, they
One thing you probably don’t hear social engineering or even spraying stole the session cookie and used it
often is someone saying, “If I only them in a brute force attack. What we to masquerade as the user. Of course,
had more usernames and passwords don’t have is the exact breakdown some MFA bypasses weren’t really
to remember.” Credentials are as of how many of our breaches and bypassing MFA because some of the
ubiquitous as sand in the desert and incidents are caused by each. As the services weren’t properly configured to
almost as hard to hold onto. Threat old adage goes “What we know is a ONLY use MFA. As mentioned above,
actors seem to have a plentiful supply drop; what we don’t know is an ocean.” what we can’t really tell you at this time
as well. However, what is missing in our is how much there were of each, as
data, and we try to be explicit when it It’s not all bad news, however. Even we need to both update our standard
comes to biases and limitations, is that though there are many ways to steal VERIS and collect the data. While this
we don’t necessarily know where all credentials, we have many ways to would be an awesome opportunity
these credentials are coming from. But protect them as well. One of the for us to finally settle the score and
we here on the DBIR team love a good best ways (stop me if you have heard discuss which MFA is better and which
mystery. Did the butler do it? Are aliens this one before) is the use of MFA. bypasses are leveraged the most, we
real? What about the Yeti? Ghosts? Before you recline in your chair and will have to keep this placeholder for
People with strong work ethics? Alas, “Well, ACKtually …” us, we do realize another year.
we will probably never know. We may there are limitations to some MFA
also never know where the criminals implementations. As you’re undoubtably
obtained the credentials in the first aware, some very high profile breaches
Quote from As the Nation’s Cyber Defense Agency, we’ve called on our industry partners
the Cybersecurity and Infrastructure to provide radical transparency to allow
Jen Easterly Security Agency (CISA) sees how our our defenders to better see, understand
nation’s adversaries operate and what and ultimately protect our citizens,
tools they use. While some of these customers and companies. In particular,
Director adversaries use advanced tools and it’s critical that “high-value targets” like
techniques, most take advantage of system administrators and Software
U.S. Cybersecurity and
unpatched vulnerabilities, poor cyber as a Service (SaaS) staff use phishing-
Infrastructure Security hygiene or the failure of organizations resistant MFA.
Agency to implement critical technologies like
MFA. Sadly, too few organizations But more and better information is
learn how valuable MFA is until they just the beginning.
experience a breach.
Working collaboratively, I look
Since joining CISA, I’ve made it a forward to seeing what we can
priority to raise MFA awareness across do to together to make our nation
all sectors to better protect our nation’s more resilient, more secure, and
critical infrastructure. Importantly, to show measurable progress …
we need more and better data to including in next year’s Verizon Data
understand the scope of, and solutions Breach Investigations Report.
to, the threats we face in cyber, and
2023 DBIR Incident Classification Patterns 38

CIS
If you happen to be interested
Controls for in how we updated VERIS to
capture attacks that bypass
consideration MFA, look no further than the
list below:
1. A dded a new Action to indicate
Mitigating against stolen
the take-over of a secondary
credentials by protecting authentication mechanism
accounts (hijack)
Account Management [5] 2. A dded a new data variety—
– Establish and Maintain an Multifactor credential—to
Inventory of Accounts [5.1] indicate whether the other
– Disable Dormant Accounts [5.3] factors, aside from credentials,
were captured
Access Control Management [6]
3. Added the social variety
– Establish an Access Granting
of Prompt Bombing41
Process [6.1]
for those attacks that
– Establish an Access Revoking
target sending annoying
Process [6.2]
levels of authentication
– Require MFA for Externally-
requests to users
Exposed Applications [6.3]
– Require MFA for Remote Network
Hopefully, the combination of
Access [6.4]
our existing enumerations, along
with these new ones, will capture
Mitigating against
the majority of the cases we
vulnerability exploitation encounter. If not, we will re-
examine our enumerations with
C ontinuous Vulnerability the next version of VERIS.
Management [7]
– Establish and Maintain a
Vulnerability Management Process
[7.1]
– Establish and Maintain a
Remediation Process [7.2]
– Perform Automated Operating
System Patch Management [7.3]
– Perform Automated Application
Patch Management [7.4]
41 This sounds like what you would call someone who photobombs people in a timely manner, doesn’t it?
2023 DBIR Incident Classification Patterns 39

Miscellaneous
Errors
You can’t find
Summary Frequency 602 incidents,
512 with confirmed
Misdelivery, Misconfiguration and data disclosure good help
Publishing errors continue to be the
headliners, and the errors that lead to Threat actors Internal (99%), these days.
breaches are most often committed by Partner (2%),
System admins and Developers. Multiple (1%),
External (1%) The great English poet and essayist,
(breaches) Alexander Pope once quipped, “It is
What is the same? hard to hire people who don’t screw
Data Personal (89%), things up.” Well, it was something
Employees continue to make compromised Medical (19%), more or less along those lines—just
mistakes, and sometimes they Other (10%), take our word for it. Regardless of
result in considerable damage Bank (10%) who said (or did not say) what, the
to their organizations. (breaches) Miscellaneous Errors pattern continues
to comprise a decent chunk of our
breach data. If you are a “glass half full”
kind of reader, you may take comfort
in the fact that this year, error-related
breaches are down to 9% as opposed
to 13% last year. If you are a “glass
half empty” reader, you may simply
attribute it to reporting since last
year we had 715 error incidents and
708 with confirmed data disclosure
as opposed to 602 incidents, with
512 confirmed breaches this year.
It’s my favorite
mistake.
Perhaps “favorite” is too strong a word.
Misdelivery (sending something to the
wrong recipient) accounts for 43% of
breach-related errors in our dataset
(Figure 41). Publishing errors (showing
something to the wrong audience)
is in second place at 23%. Finally,
Misconfiguration, the much-loved
Figure 41. Action varieties over time in Miscellaneous Errors breaches action type of the lazy person, comes
in third and accounts for 21% of error-
related breaches. This might tempt us
to think that people are unreliable—
perish the thought. However, you can
rely on them to at least keep things
interesting by switching up their
mistakes to help keep you on your toes.
2023 DBIR Incident Classification Patterns 40

In fact, as Figure 41 illustrates, If we drill down a little deeper (Figure CIS
Misconfiguration and Misdelivery 42), it’s easy to see that these
have ebbed and flowed over the three Error types have won the Controls for
last few years as if they were part popularity contest by a wide margin.
of the choreographed dance of However, the team is saddened to consideration
celestial bodies. In last year’s report, see that Gaffe is always at or near
Misdelivery and Misconfiguration the bottom (considering how many
converged, but this year Misdelivery of those we make ourselves).
Control data
is in the ascendancy,42 whereas our
old faithful dog, the Publishing error, is As illustrated in Figure 43, the majority
Data Protection [3]
once again meeting Misconfiguration of errors that lead to breaches are
— Establish and Maintain a Data
on its downward slope. committed by Developers and System
Management Process [3.1]
admins, along with a sprinkling of End-
— Establish and Maintain a Data
users. Given the Error action types that
Inventory [3.2]
are most often found in breaches, it is
— Configure Data Access Control
hardly surprising that those who have
Lists [3.3]
more responsibility for maintaining the
— Enforce Data Retention [3.4]
data and the upkeep of the environment
— Securely Dispose of Data [3.5]
are also those who are most frequently
— Segment Data Processing and
responsible. Speaking of responsibility,
Storage Based on Sensitivity [3.12]
the error vector of Carelessness
— Deploy a Data Loss Prevention
appeared in 98% of cases. Yikes!
Solution [3.13]
Maybe Pope was on to something.
Secure infrastructure
Continuous Vulnerability
Management [7]
— Perform Automated Vulnerability
Scans of Externally-Exposed
Enterprise Assets [7.6]
Application Software Security [16]
— U se Standard Hardening
Configuration Templates for
Application Infrastructure [16.7]
— Apply Secure Design Principles in
Application Architectures [16.10]
Train employees
Security Awareness and Skills
Training [14]
— Train Workforce on Data Handling
Best Practices [14.4]
— Train Workforce Members on
Figure 42. Top action varieties in Figure 43. Top actor varieties in
Causes of Unintentional Data
Miscellaneous Errors breaches (n=450) Miscellaneous Errors breaches (n=89)
Exposure [14.5]
Application Software Security [16]
— Train Developers in Application
Security Concepts and Secure
Coding [16.9]
42 If you were born under the sign of Misdelivery you should expect good news soon. 3, 9, 13 and 33
are your lucky numbers.
2023 DBIR Incident Classification Patterns 41

Denial of
Service
We will not
Summary Frequency 6,248 incidents,
4 with confirmed data
As Denial of Service continues to disclosure be denied.
dominate our incidents, so do the
capabilities of mitigation services. Threat actors External (100%)
However, there has been a resurgence (incidents) As the name would imply, the Denial
of low volume attacks that still cause of Service pattern covers all of
issues to corporations. those attacks that try to keep you
from streaming your next episode
of “Below Deck,” watching your next
TikTok movie or loading your timeline
What is the same?
on Twitter.43 Sadly, all of this can
Denial of Service attacks continue to be obviously add up to the nuisance of
ubiquitous and have remained in the top having to acknowledge the real world
spot of incidents for several years now. and the people around us. We can all
agree that would be terrible indeed.
However, as some of our readers may
know, organizations still actually need
the internet to be up and running in
order to conduct business. Every year,
DoS shows up as a huge volume of
Incidents in our datasets, stemming
from several different mitigation service
partners, including Verizon’s own.
They are all doing an excellent job in
preventing those Incidents from having
any significant impact on organizations.
In that light, even though the Denial of
Service pattern has consistently taken
the top spot in Incidents for the last
several years (Figure 44), there is really
not a lot of nuance to be discussed
here, apart from our usual suggestion
to invest in some sort of mitigation
service if you care about the continued
availability of your network presence on
Figure 44. Patterns over time in incidents
43 Not sure if we can blame our usual threat actors for this one.
2023 DBIR Incident Classification Patterns 42

the internet. This is not due to a lack of We are going as costs of bandwidth and CPU
nuance in the DDoS dataset overall but processing become more accessible
more a reflection of a lack of the typical to need a and available and suggests a trend
details that we traditionally analyze that is hard to break on escalating
such as Actors, Assets and Attributes. bigger pipe. competition between the attackers
and mitigating services. Just make
Even so, it didn’t feel right to deny our sure your contracted service can clear
readers a Denial of Service section, One important point we should touch that bar, and most of the impact will
as there are still important trends on is the growth of median and above likely be absorbed. Let the machines
and information that are necessary median percentiles in bits per second fight it out Transformers-style and
to be reviewed. It’s important to of DDoS attacks (see Figure 45).44 The crack open a cold beverage while
realize they’re still there, even if you median grew a whopping 57%45 from you worry about all the other attack
can easily solve them. Also, it is a 1.4 gigabytes per second (Gbps) last patterns afflicting your corporation.
respite to not have to write about year to 2.2 Gbps now, and the 97.5
Ransomware for a couple of pages. percentile grew 25% from 99 Gbps Even as the volume of garbage in our
to 124 Gbps. This is to be expected networks grows, some attacks have a
more subtle touch. A point of attention
that some of our partners brought
to us was the growth of distributed
DNS Water Torture46 attacks in, you
guessed it, shared DNS infrastructure.
It is basically a resource exhaustion
attack done by querying random name
prefixes on the DNS cache server so
it always misses and forwards it to the
authoritative server. It is quite silly when
you think of it, but it can be a heavy
burden with some simple coordination
by the threat actors’-controlled
devices. Make sure to check on your
DNS infrastructure resiliency and
check for options with your mitigation
service as well to make sure you are
protected against these attacks too.
Figure 45. Bits per second in DDoS incidents (n=10,622)
44 Be sure to discuss this at parties. You’ll be wildly popular.
45 I bet you thought our inflation numbers in the U.S. were bad, huh?
46 This is NOT a subtle name!
2023 DBIR Incident Classification Patterns 43

Lost and
Stolen Assets
Where go
Summary Frequency 2,091 incidents,
159 with confirmed
This pattern continues to be a problem data disclosure my laptop?
for organizations because these
small (and not so small) devices are Threat actors External (92%),
just so portable. We’ve seen their Internal (68%), The headline in this pattern is “Your
capacity to store large amounts Multiple (60%), stuff is gone,” which isn’t really a news
of data increase over time, while Partner (1%) flash. Whether the missing item(s)
employees’ ability to misplace them (breaches) had “help” in the form of someone
(or External actors to steal them) stealing a laptop, or was accidental,
remains predictably common. Actor motives Financial (100%) as in classified printed documents
(breaches) being mislaid in high-level government
officials’ residences, the more portable
What is the same? Data Personal (87%), an asset is, the more it needs protection
compromised Medical (30%), against loss and theft.
Devices and media are still more likely Other (21%),
to be lost by Internal actors than stolen Bank (13%) This is a pattern where we see a high
by External ones. (breaches) percentage of incidents not resulting
in confirmed data breaches—largely
because the status of confidentiality
disclosure remains “at-risk” rather
than “confirmed” due to the loss of
custody of the asset in question. The
exception is printed material, since no
controls exist to shield documents from
view once printed. Similar to last year,
we again have less than 10% of the
incidents as confirmed data breaches.
While stolen devices certainly represent
a risk to organizations, employees are
much more likely to cause a breach
accidentally through loss. This fact
has held true year over year on a
consistent basis, as shown in Figure 46.
What is going missing, you may ask?
Unsurprisingly, it’s the portable user
devices, such as laptops, and mobile
phones. In fact, phones have become
quite the commodity (Figure 47).
Considering the fact that no one
ever seems to put them down, it’s
hard to believe so many are lost.
Figure 46. Top Action varieties in Lost and Stolen Assets incidents
2023 DBIR Incident Classification Patterns 44

CIS
Controls for
consideration
Protect data at rest
Data Protection [3]
– Encrypt Data on End-User
Devices [3.6]
– Encrypt Data on Removable
Media [3.9]
Secure Configuration of Enterprise
Assets and Software [4]
– Enforce Automatic Device
Lockout on Portable End-User
Devices [4.10]
– Enforce Remote Wipe Capability on
Portable End-User Devices [4.11]
Figure 47. Top Assets in Lost and Stolen Assets incidents
2023 DBIR Incident Classification Patterns 45

Privilege
Misuse
Summary My employees
Frequency 406 incidents,
288 with confirmed
Your employees continue to use data disclosure love me!
their access to commit breaches
and, in some cases, initiate
Threat actors Internal (99%),
fraudulent transactions. We saw Multiple (7%), People may think they are somehow
more collusion between multiple External (6%), immune to a data breach. They
types of actors this year. Partner (2%) may put their trust in their security
(breaches) controls, thinking they have amazing,
impenetrable defenses. They may put
What is the same? Actor motives Financial (89%), their trust in “flying under the radar”
Grudge (13%), or believe they are too small to have a
This pattern continues to be
Espionage (5%), breach. But this kind of thinking largely
dominated by the Internal actor, by
Convenience (3%), assumes breaches come from the
definition. Most are motivated by
Fun (3%), outside, from the “bad actors” that are
financial gain, and Personal data
Ideology (2%) external to the organization. What they
continues to be a favorite target.
(breaches) fail to take into account is the risk of
an insider breach. “Surely, MY people
Data Personal (73%),
wouldn’t do that!” they say. But of
compromised Medical (34%),
course, they would—and don’t call
Other (18%),
me Shirley.
Bank (12%),
Payment (12%) The hard fact to face is that some of our
(incidents) employees also cause data breaches
for malicious reasons. The most
common nonaccidental Internal actor
breach is Privilege abuse. This is just
what it sounds like—employees abusing
the access they have been given to
do their jobs to steal data instead.
They are significantly more likely to
do this for their own financial gain
(Figure 48). We know, it’s a shocker.
Figure 48. Internal actor motives in
Privilege Misuse breaches (n=59)
2023 DBIR Incident Classification Patterns 46

We’ll just help We are increasingly seeing Privilege
Misuse breaches paired with Fraudulent
ourselves. transactions, more so this year than in
the past several, as shown in Figure 49.
Fraudulent transactions are an Integrity
We’ve talked about your employees violation that is frequently the end game
committing these acts—but our At- of the BEC and is typically a money
a-Glance table shows that we see transfer to a threat actor-controlled
other kinds of threat actors in this bank account. However, since Internal
pattern. Interestingly, we see multiple actors already have access to the
threat actors (Internal, External, systems where bank accounts and
Partner—some combination of these routing information are stored in these
three) in 7% of the breaches. This cases, they’re probably just making
is collusion—evidence of multiple that banking update themselves.
kinds of Actors working together Seeing Internal actors increasingly just
to bring about a data breach. redirect funds is especially concerning,
considering it may be someone
Indeed, we have seen instances where in a position to siphon significant
organized fraud gangs have sent in resources away from the organization.
people with the objective of being
hired by businesses for the purpose of
facilitating large-scale scams. We have
seen this in multiple industries, and it
has continued to plague organizations
for years. These people can be
difficult to spot—they may present and
interview convincingly. This practice by
financially motivated criminal groups
makes it even more important to have
your detective controls in place to
catch the inappropriate access that
these people are enabling. One of
the difficulties in responding to an
incident like this is that no company’s
onboarding process is perfect, and
most onboarding involves getting the
new hire added to various groups and
systems that aren’t always directly
controlled by IT. Those investigations
often reveal process-related
weaknesses in the IT infrastructure.
Figure 49. Fraudulent transactions in Privilege Misuse breaches
2023 DBIR Incident Classification Patterns 47

4
Industries

Industries:
Introduction
If you are a new reader, you may find this introduction of some use. If, on the other
hand, you are a long-time reader, then just move along; this will all be familiar territory.
The 2023 DBIR examined 16,312 incidents, of which 5,199 were confirmed data
breaches. We take a look at both from the point of view of their respective industries
in the upcoming sections. Attacks that consistently prey on one industry may not
affect another industry at all. Attack surfaces, the interest of specific threat actors and
the infrastructure a given industry relies upon all play a big role in how they experience
security incidents. The types and quantity of data the industry handles, how people
(customers, employees, etc.) interact with them, and a host of other factors too
numerous to mention will also dictate the kinds of attacks each industry encounters.
A large organization whose business model focuses entirely on mobile devices and
the apps it includes will naturally have a different set of risks than a very, very small
business with no internet presence but that uses a point-of-sale (PoS) vendor to
manage their systems for them. The infrastructure, and conversely the attack surface,
largely drives the risk.
Therefore, we caution our readers not to make inferences about the security posture
(or lack thereof) of a particular sector47 based on how many breaches or incidents
an industry reports. These numbers are heavily influenced by several factors,
including data breach reporting laws and partner visibility. Because of this, some of
the industries have very low numbers, and as with any small sample, we must advise
readers that our confidence in any statistics derived from a small number must also
be less.
If you are reading this only for a glimpse of your industry, our recommendation is to
verify what the top patterns are on the summary table accompanying each industry
and also spend some time with those pattern sections.
47 Legal made us say that; of course, you should totally ridicule your [fren]emies in other industries.
2023 DBIR Industries 49

| Incidents |     |     |     | Breaches |     |     |     |     |
| --------- | --- | --- | --- | -------- | --- | --- | --- | --- |
Industry Total Small (1–1,000) Large (1,000+) Unknown Total Small (1–1,000) Large (1,000+) Unknown
|     | 16,312 | 694 | 489 | 15,129 | 5,199 | 376 | 223 | 4,600 |
| --- | ------ | --- | --- | ------ | ----- | --- | --- | ----- |
Total
| Accommodation (72)         | 254   | 4   | 2   | 248   | 68  | 4   | 1   | 63  |
| -------------------------- | ----- | --- | --- | ----- | --- | --- | --- | --- |
| Administrative (56)        | 38    | 8   | 14  | 16    | 32  | 8   | 11  | 13  |
| Agriculture (11)           | 66    | 1   | 5   | 60    | 33  | 0   | 3   | 30  |
| Construction (23)          | 87    | 7   | 1   | 79    | 66  | 4   | 1   | 61  |
| Education (61)             | 496   | 63  | 15  | 418   | 238 | 28  | 8   | 202 |
| Entertainment (71)         | 432   | 13  | 3   | 416   | 93  | 10  | 1   | 82  |
| Finance (52)               | 1,829 | 70  | 30  | 1,729 | 477 | 38  | 18  | 421 |
| Healthcare (62)            | 522   | 28  | 15  | 479   | 433 | 23  | 15  | 395 |
| Information (51)           | 2,105 | 45  | 110 | 1,950 | 380 | 23  | 19  | 338 |
| Management (55)            | 9     | 1   | 0   | 8     | 9   | 1   | 0   | 8   |
| Manufacturing (31–33)      | 1,814 | 37  | 24  | 1,753 | 259 | 18  | 15  | 226 |
| Mining (21)                | 25    | 2   | 0   | 23    | 13  | 2   | 0   | 11  |
| Other Services (81)        | 143   | 7   | 2   | 134   | 100 | 6   | 1   | 93  |
| Professional (54)          | 1,396 | 176 | 54  | 1,166 | 421 | 85  | 32  | 304 |
| Public Administration (92) | 3,270 | 87  | 110 | 3,073 | 582 | 48  | 39  | 495 |
| Real Estate (53)           | 83    | 15  | 5   | 63    | 59  | 10  | 2   | 47  |
| Retail (44–45)             | 404   | 62  | 44  | 298   | 191 | 33  | 28  | 130 |
| Transportation (48–49)     | 349   | 13  | 25  | 311   | 106 | 8   | 13  | 85  |
| Utilities (22)             | 117   | 12  | 6   | 99    | 33  | 3   | 3   | 27  |
Wholesale Trade (42)
|         | 96     | 42  | 22  | 32     | 53    | 23  | 11  | 19    |
| ------- | ------ | --- | --- | ------ | ----- | --- | --- | ----- |
| Unknown | 2,777  | 1   | 2   | 2,774  | 1,553 | 1   | 2   | 1,550 |
| Total   | 16,312 | 694 | 489 | 15,129 | 5,199 | 376 | 223 | 4,600 |
Table 2. Number of security incidents and breaches by victim industry and organization size
| 2023 DBIR Industries |     |     |     |     |     |     |     | 50  |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | --- |

Incidents
51
nrettaP
noitcA
tessA
Figure 50. Incidents by industry
2023 DBIR Industries

Breaches
52
nrettaP
noitcA
tessA
Figure 51. Breaches by industry
2023 DBIR Industries

Accommodation and
Food Services
I’ll just scrape
Frequency 254 incidents,
68 with confirmed
that off.
data disclosure
Top patterns System Intrusion,
Basic Web System Intrusion is the top pattern in
Application Attacks this sector for the second year running.
and Social Included in this pattern, among other
Engineering things, is a collection of various types
represent 90% of of malware. Approximately one-third of
breaches cases involved the use of Ransomware,
and much of the remainder consisted
Threat actors External (93%), of RAM scrapers. In fact, RAM scrapers
Internal (9%), targeting the PoS is the favorite combo
Multiple (1%) in this sector, which likely comes as no
(breaches) surprise to those trying to maintain
their defenses.
Actor motives Financial (100%)
(breaches) Payment card data was targeted
41% of the time, which is the same
Data Payment (41%), percentage we saw last year, but since
compromised Credentials (38%), Credentials and Personal data fell as
Personal (34%), a proportion of the whole, they have
Other (26%) taken a back seat to credit cards.
(breaches) Along with the increased focus on the
data type of Payment cards comes the
What is the We are seeing the
motivation of Financial. Last year, we
same? same three attack
saw the Espionage motive in 9% of the
patterns hitting this
breaches, but this year, it is all Financial
sector as we did last
all the time.48
year—but the order
has changed. External
actors continue to
target this industry
because of the
lucrative data the
members hold.
Summary
Payment card data continues to be the
top target for Data types in this sector,
unsurprisingly. The use of RAM
scrapers continues to be a favorite tool
of the Financially motivated attackers
that regularly plague this sector.
53
SCIAN
27
Give a person
a phish and you
feed them for
a day!
Social continues to have a considerable
presence in this sector. While Phishing
and Pretexting (the main difference
between them is how hard the adversary
must work to make it happen) are the
main social engineering concerns in
Accommodation, they are too close
to call for the top spot. Most of these
social attacks are coming in via email, so
make sure it is easy for your employees
to report any questionable attempt
quickly. There is nothing like having your
employees be your first line of defense—
they are certainly already on the front line
of targets.
48 Honestly, what isn’t though?
2023 DBIR Industries

Educational
Services
Who saw Frequency 497 incidents,
238 with confirmed
data disclosure that coming?
Top patterns System Intrusion,
Miscellaneous Errors In a move that shocked faculty, staff and
and Social students alike, last year’s much lauded
Engineering salutatorian, Basic Web Application
represent 76% of Attacks, has dropped out (of the top
breaches three patterns). Miscellaneous Errors
is still present (isn’t it always?) and has
Threat actors External (72%), increased slightly from last year. As you
Internal (29%), may have guessed, these errors are the
Multiple (1%), usual suspects: Misdelivery, Publishing
Partner (1%) errors and Misconfiguration.
(breaches)
Social Engineering clawed its way to
Actor motives Financial (92%), the number three position, increasing
Espionage (8%), from 14% last year to 21% in 2023
Convenience (1%), (Figure 52). This rise is primarily
Fun (1%) (breaches) represented by Phishing attacks,
which showed up in 18% of breaches,
Data Personal (56%),
and Pretexting scenarios (4%).
compromised Credentials (40%),
Other (25%),
Internal (20%)
(breaches)
What is the System Intrusion and
same? Miscellaneous Errors
are yet again two of
the top three patterns
for this industry. The
ratio of External and
Internal actors is
nearly the same as
last year.
Summary
Basic Web Application Attacks dropped
out of the top three to be replaced
by Social Engineering. Ransomware
continues to play a large role in
breaches in this vertical.
54
SCIAN
16
Hacking was present in 40% of
breaches, with the Use of stolen
credentials appearing in 31% of
them. Not to be outdone, Malware
also showed up in 40% of breaches,
with Ransomware present in 30%
of those breaches. Let’s review that
finding for the exam: Ransomware was
responsible for almost one-third of all
breaches in the Educational Services
vertical. In spite of this impressive
showing from both Hacking and
Malware, the System Intrusion pattern,
while maintaining its number one spot,
decreased slightly from last year.
Figure 52. Patterns in Education breaches
2023 DBIR Industries

Financial and
Insurance
 SCIAN
25
|           |                    | These attacks  | Make them  |
| --------- | ------------------ | -------------- | ---------- |
| Frequency | 1,832 incidents,   |                |            |
480 with confirmed
|              | data disclosure | are so basic. | work for it. |
| ------------ | --------------- | ------------- | ------------ |
| Top patterns | Basic Web       |               |              |
Application Attacks,  “We were compromised by a highly  Rounding out the top three is the pattern
Miscellaneous Errors  sophisticated cyberattack.” So reads   that requires adversaries to actually put
and System Intrusion  a large percentage of data breach  forth a bit of effort, System Intrusion.
represent 77% of  notification letters. But really, just how  While it dropped from 27% to 14% this
breaches sophisticated is a brute-forced password?  year (allowing Miscellaneous Errors to
|     |     | Or better still, credential stuffing where  | dominate), it remains a serious issue.   |
| --- | --- | ------------------------------------------- | ---------------------------------------- |
Threat actors External (66%),  you don’t even have to guess the  This illustrates that at least some of
Internal (34%),  password—you’ve acquired it from  the time, adversaries had to trot out
Multiple (1%)  another breach! The Basic Web  their more sophisticated techniques in
(breaches) Application Attacks pattern is the most  order to get the job done. Interestingly,
prevalent in this sector, which means  Ransomware is decreasing as a favorite
| Actor motives | Financial (97%),  |     |     |
| ------------- | ----------------- | --- | --- |
those not-so-complex attacks are  tactic in this pattern for this sector. We
Espionage (3%),
succeeding splendidly for the adversaries.  discuss it more in depth in the “Incident
Convenience (1%),
Why put forth a great deal of effort when  Classification Patterns” section in case if
Ideology (1%)
just a little will do? you skipped that part. We know, some of
(breaches)
you just read the DBIR for the pictures.
| Data  | Personal (74%),  |     |     |
| ----- | ---------------- | --- | --- |
Wait—did I give
| compromised | Credentials (38%),  |     |     |
| ----------- | ------------------- | --- | --- |
Other (30%),
you that?
Bank (21%)
(breaches)
| What is the  | The top three           | Another prominent attack involves        |     |
| ------------ | ----------------------- | ---------------------------------------- | --- |
| same?        | patterns remain the     | Internal actors making mistakes.         |     |
|              | same, but their order   | Misdelivery—where protected data is      |     |
|              | of ascendancy has       | sent to the wrong recipient—is the most  |     |
|              | rearranged. Personal    | common. Sometimes it is a matter of      |     |
|              | data, very useful for   | paper documents going to the wrong       |     |
|              | fraud, continues to be  | people, and other times it is just the   |     |
|              | the most desired data   | electronic version that goes astray.     |     |
|              | type stolen.            | Either way, extra care needs to be       |     |
given to catching these kinds of Errors
| Summary |     | before they cause a data breach. |     |
| ------- | --- | -------------------------------- | --- |
With Basic Web Application Attacks as
the top pattern, we know that the
adversaries are successfully gaining
access without too much effort. This,
combined with the Misdelivery error,
indicates there is room for good
controls to cover a decent percentage
of attacks in this sector.
2023 DBIR Industries 55

Healthcare
A sector
under siege
The Healthcare vertical is highly
targeted by ransomware gangs, which
results in both the loss of use of
their systems—potentially with life-
threatening consequences—as well as
data breaches. While the number of
ransomware incidents peaked in this
industry in 2021, the last three years
have seen a jump in data breaches
(where the data is confirmed to have
been stolen as well as the encryption
triggered) caused by ransomware. This
combination of attacks by adversaries
is resulting in more data being
compromised in addition to the usual
chaos of staff being forced to do their
jobs without the systems they rely upon.
Mitigating these attacks takes time—if
the organization even has reliable,
tested backups of the systems
compromised—and resources. If
both are scarce in your organization,
prevention and early detection are your
best friends. Don’t ignore the threat this
type of attack represents when you are
planning your controls.
Sorry ’bout
that
The Miscellaneous Errors pattern
remains prevalent in healthcare. The
action variety of Misdelivery is a
consistent people problem. This is the
mistake that happens when data that
is supposed to go to a certain person
(or group) actually ends up going to
someone entirely different. Sometimes
it is in the form of that spreadsheet with
56
SCIAN
26
sensitive employee health information
Frequency 525 incidents,
accidentally being sent to a much wider
436 with confirmed
distribution than planned (those email
data disclosure
groups can be so similar—thanks a lot,
Top patterns System Intrusion, autocomplete). In other cases, it is a
Basic Web mailing error with paper documents
Application Attacks that are placed in such a way that
and Miscellaneous too much information is visible in the
Errors represent 68% envelope’s clear window. Who wants
of breaches their letter carriers to know about their
embarrassing condition? Customers
Threat actors External (66%), (patients) are understandably upset.
Internal (35%),
Multiple (2%)
(breaches) Where’s my
Actor motives Financial (98%), gruntle?
Espionage (2%),
Fun (1%),
Ideology (1%) Ah, the disgruntled employee—so often
(breaches) the perpetrator of malicious actions
and wreaking the kind of havoc only an
Data Personal (67%),
insider can achieve. While the Privilege
compromised Medical (54%),
Misuse pattern is no longer in the top
Credentials (36%),
three for this industry, it remains a
Other (17%)
consistent problem. Snooping from
(breaches)
curiosity—more the bored employee
What is the The top three than the actively hostile—is common
same? patterns remain the in Healthcare as well. But this is also
same, although the a sector in which we see evidence
order has changed. of collusion, multiple actors working
Internal actors together to make their breach dreams
making mistakes a reality. If only this diligence could
continue to trouble be put toward their legitimate work
this sector. tasks, these employees could be top
performers. The industry’s only defense
Summary for when someone loses their gruntle is
fast detection of unusual data access
Ransomware actors continue targeting
patterns. This remains a challenge for
this sector and are increasingly causing any industry where internal actors are
confirmed data breaches in the process. motivated to cause trouble.
Errors (particularly Misdelivery) are
prevalent as well. Finally, don’t discount
the insider threat in this industry.
2023 DBIR Industries

Information
Frequency 2,110 incidents,
384 with confirmed
data disclosure
Top patterns System Intrusion,
Basic Web
Application Attacks
and Social
Engineering
represent 77% of
breaches
Threat actors External (81%),
Internal (20%),
Multiple (2%),
Partner (1%)
(breaches)
Actor motives Financial (92%),
Espionage (8%)
(breaches)
Data Personal (51%),
compromised Credentials (37%),
Other (35%),
Internal (19%)
(breaches)
What is the System Intrusion
same? remains the top
pattern in this vertical,
and it is still
dominated by
Financially motivated
external actors.
Summary
Miscellaneous Errors continues the
downward trend it has exhibited for the
last several years and loses its position
in the top three to Social Engineering.
Denial of Service attacks account for
70% of incidents in NAICS 51.
57
SCIAN
15
Make no
mistake,
information
is power.
Over the last few years, errors have
played a diminishing role in breaches
within the Information vertical. That
downward trend continues this
year, so much so that it has fallen to
number four and accounts for only
13% of breaches (Figure 53). Good
on ya, Information folks! Securing
your assets from the bad guys is
hard enough without unwittingly
exposing assets yourself.
Social Engineering, on the other hand,
has slowly crept up and captured the
number three position with 20% of Figure 53. Patterns in Information
breaches. In some industries, we see sector breaches (n=384)
a much higher degree of Phishing than
we do of its more complicated cousin,
Pretexting. In the Information vertical, those are not big numbers, but it is of
however, the two social actions are interest to see them reappearing in this
not far apart, with Phishing at 15% industry for the first time in a couple
and Pretexting at 11%. As mentioned of years. As one would expect, the
elsewhere in this report, Pretexting is vast majority of attacks, regardless
definitely on the rise. of who was committing them, were
Financially motivated. The motive of
Espionage was still present at 8% of
Please listen breaches but is significantly lower than
last year’s 20%. The most likely reason
closely as our for the change is the move away from
web apps and servers and toward spy
options have balloons and remote viewing.
NOT changed.
As always, external actors (the vast
majority of which are Organized crime)
are behind most attacks in this vertical.
In fact, last year, we showed only
External and Internal actors. This year
we did see an increase (albeit very
small) in the categories of Partner and
multiple actors at 1% each. Granted,
2023 DBIR Industries

Manufacturing
In our postmodern world, we rely on
Frequency 1,817 incidents,
gadgets and gizmos galore to make it
262 with confirmed
through our day—certainly more so than
data disclosure
at any other time period in history.49
Top patterns System Intrusion, The importance of Manufacturing
Social Engineering truly cannot be understated as it
and Basic Web relates to how we exist and interact
Application Attacks with each other on a daily basis. The
represent 83% of Manufacturing industry is aware of this
breaches and consequently is continually looking
for the next big thing that we all think
Threat actors External (90%), we can’t live without. Cybercriminals
Internal (11%), know it as well and are constantly
Multiple (2%), maneuvering in an effort to cash in.
Partner (1%)
(breaches) This year we can see in Figure 54 the
same top three patterns that we saw
Actor motives Financial (96%), in last year’s report, albeit in a slightly
Espionage (4%), different order. Social Engineering
Convenience (1%) (23%) and Basic Web Application
(breaches) Attacks (17%) changed places in the
lineup, while System Intrusion remains
Data Personal (60%),
in first place at 42%.
compromised Credentials (38%),
Other (37%),
Internal (18%)
(breaches)
What is the The top three attack
same? patterns remain the
same, but their order
has changed slightly.
Financially motivated
external actors
continue to wreak
havoc in this industry.
Summary
Hacking and Malware actions are
pacing each other in the race for the
top two spots. While Social Engineering
attacks are still alive and well, they
are a distant third. For incidents, do
not discount Denial of Service attacks
against this industry’s infrastructure to
disrupt the ability to meet deadlines.
58
SCIAN 33–13
As Figure 56 illustrates, when we drill
down into what attack actions most
often occur in the Manufacturing
vertical, we see that Hacking and
Malware attacks are occurring at
almost exactly the same rate and
that Social attacks continue to make
a strong showing. Ransomware,
which accounts for a large part of
the breaches in the System Intrusion
pattern, continues to slowly trend
upward in this vertical for the third year
in a row (Figure 55).
Figure 56. Select Actions over time in
Manufacturing breaches
From an incident perspective, it is still
mainly about Denial of Service attacks.
DoS attacks account for approximately
67% of incidents in this vertical. This
has been a rising trend over the past
few years, so if your organization
resides in this industry, it is definitely
Figure 54. Patterns over time in
something to keep an eye on. Manufacturing incidents
Figure 55. Action varieties over time in
Manufacturing breaches
49 And believe me, we have lived through several of them.
2023 DBIR Industries

Mining, Quarrying,
and Oil & Gas
Extraction + Utilities
 SCIAN
22+12
Dig around and
| Frequency | 143 incidents,   |     |
| --------- | ---------------- | --- |
47 with confirmed
find out.
data disclosure
| Top patterns | System Intrusion,    |                                         |
| ------------ | -------------------- | --------------------------------------- |
|              | Basic Web            | Due to the smaller number of incidents  |
|              | Application Attacks  | and breaches reported to us from        |
NAICS 21 and 22, we have to dig deep
and Miscellaneous
(pun intended) at times to have a
Errors represent 81%
|     | of breaches | statistically relevant population. Even  |
| --- | ----------- | ---------------------------------------- |
so, because of the smaller sample
| Threat actors | External (80%),  | size, we are sometimes still forced  |
| ------------- | ---------------- | ------------------------------------ |
|               | Internal (20%)   | to use ranges rather than definite   |
|               | (breaches)       | percentages. However, as both these  |
sections are considered critical
Actor motives Financial (63%–93%),  infrastructure and are not too dissimilar,
Espionage (4%–32%),
we do our best to find useful and
Grudge (1%–21%),
interesting nuggets where we can. Are
Ideology (0%–15%),
you a member of these industries? If
|     | Convenience/Fear/ | so, please consider becoming a DBIR  |
| --- | ----------------- | ------------------------------------ |
|     | Fun/Other/        | contributor to help us provide more  |
|     | Secondary (0%–7%  | useful analysis.                     |
each) (breaches)
The number one pattern this year is
Figure 57. Mining and Utilities top
| Data  | Personal (50%),  |     |
| ----- | ---------------- | --- |
System Intrusion. If you have been  Actions in breaches (n=37)
| compromised | Internal (33%),   |     |
| ----------- | ----------------- | --- |
reading the other sections, you will
Other (26%),
know that this in no way makes those
Credentials (24%)
in this vertical the Lone Ranger. As
|     | (breaches) | stated in the patterns section, the  |
| --- | ---------- | ------------------------------------ |
System Intrusion pattern is made up
| What is the  | System Intrusion   |     |
| ------------ | ------------------ | --- |
of more complex, multistep attacks as
| same? | and Basic Web  |     |
| ----- | -------------- | --- |
opposed to the “get in, grab the loot
Application Attacks
and scram” type of attacks. Specifically,
remain significant
most ransomware attacks fall into
causes for concern
System Intrusion, and approximately
in this industry.
one out of three breaches (32%) in
this industry were ransomware attacks
Summary
(Figure 57). Given the high rate of
Ransomware is responsible for  success of ransomware (along with
approximately one out of three   the fact that attackers often take data
breaches in this vertical. Social  before they encrypt it, and they do love
Engineering, in spite of its overall   to post it on their leak sites), seeing
rise, has decreased in this industry. so much of it in critical infrastructure
verticals is a matter for concern.
2023 DBIR Industries 59

Last year we commented on the high
number of breaches in this vertical that
fell into the Social Engineering pattern.
This year it has dropped out of the
top three completely with Basic Web
Application Attacks and Miscellaneous
Errors coming in at numbers two
and three. In fact, Social Engineering
dropped out of the top five. This is
mildly surprising due to the uptick we
are seeing in phishing and pretexting in
other industries. Maybe the criminals
don’t want to have to actually interact
with others to steal money? We
can certainly understand that.
When it comes to what the threat actors
are taking, personal data accounts
for half, and there was a substantial
rise in Internal data (33% this year as
opposed to 9% last year, as shown in
in Figure 58). This may be tied to the
name and shame ransomware attacks
mentioned on the previous page.
Figure 58. Top Data type stolen in
Mining and Utilities (n=46)
2023 DBIR Industries 60

Professional, Scientific
and Technical Services
 SCIAN
45
This sector could perhaps be
| Frequency | 1,398 incidents,   |     |
| --------- | ------------------ | --- |
considered the lubricant that keeps all
423 with confirmed
industries running smoothly. It consists
data disclosure
of many disparate professions,
| Top patterns | System Intrusion,    | including our lawyer friends [joke          |
| ------------ | -------------------- | ------------------------------------------- |
|              | Basic Web            | redacted by legal], accounting and          |
|              | Application Attacks  | various other business services. Much       |
|              | and Social           | like the other sectors they serve, this     |
|              | Engineering          | industry is also affected by the big three  |
patterns of System Intrusion (47%),
represent 90% of
Basic Web Application Attacks (25%)
breaches
and Social Engineering (18%).
| Threat actors | External (92%),  |     |
| ------------- | ---------------- | --- |
Internal (9%),
With regard to action varieties, while we
Multiple (3%),
see DoS and Use of stolen creds
Partner (2%)
among the top actions in Figure 59, we
(breaches)
also see a good deal of Ransomware.
This year, Ransomware accounted for
| Actor motives | Financial (96%),  |     |
| ------------- | ----------------- | --- |
approximately 23% of the incidents in
Espionage (4%),
this sector, which is a notable increase
Convenience (1%)
from last year’s 14%.
(breaches)
If you are wondering how these
| Data  | Personal (57%),  |     |
| ----- | ---------------- | --- |
Figure 59. Actions in Professional
| compromised | Credentials (53%),  | breaches occur, you need look  |
| ----------- | ------------------- | ------------------------------ |
Services incidents (n=1,351)
|     | Other (25%),    | no further than Web applications     |
| --- | --------------- | ------------------------------------ |
|     | Internal (16%)  | (55%), Email (25%) and Desktop       |
|     | (breaches)      | sharing software (17%). Considering  |
the frequent usage of stolen
| What is the  | System Intrusion,  | credentials and email, it might be  |
| ------------ | ------------------ | ----------------------------------- |
| same?        | Basic Web          |                                     |
a good time to remind folks to
Application Attacks
implement strong authentication
and Social
practices and to encourage your
|     | Engineering continue    | team members to keep in mind the  |
| --- | ----------------------- | --------------------------------- |
|     | to be the main threats  | importance of staying diligent.   |
to organizations in
this sector.
Summary
Even though the top patterns haven’t
changed for this industry, this sector
has experienced an increase in
Ransomware over the year, with
incidents following the same core
vectors as the previous year.
2023 DBIR Industries 61

Public
Administration
62
SCIAN
29
That’s no What’s worse
Frequency 3,273 incidents,
584 with confirmed
moon! than quiet
data disclosure
Top patterns System Intrusion, quitting?
Lost and Stolen Whether data is stolen by stealthy
Assets, and Social “weather research” balloons (death
Engineering stars) floating overhead or by more This brings us to the point that internal
represent 76% of conventional methods such as phishing, actor Misuse continues to be a
breaches external threat actors are diligently consistent problem in this sector. While
gaining access to data in the public prevalent, it is not increasing, so that
Threat actors External (85%), sector. Mind you, when we created is at least some good news. In fact,
Internal (30%), VERIS to allow us to categorize Misuse peaked in 2019 (of the past five
Multiple (16%) breaches, we didn’t expect to see it years) and has decreased somewhat
(breaches) applied to UFOs being shot out of the since then. However, the pairing of the
sky. But, until it becomes a trend, we unhappy employee with a motivated
Actor motives Financial (68%), will simply tag it as Physical - Other and external adversary shows the continued
Espionage (30%), call it a day for now. need for detective controls. If you
Ideology (2%)
can catch this kind of Internal actor-
(breaches) The System Intrusion pattern remains facilitated attack in its early stages, you
high in this sector. Some intrusions are can mitigate the damage significantly.
Data Personal (38%),
stuff that movies are made of—complex
compromised Other (35%), attacks against a challenging target,
Credentials (33%),
where the stakes are high for entire
Internal (32%)
economic systems.50 We did see an
(breaches) increase in the Espionage-motivated We see evidence of collusion
actors in this pattern this year. In fact, (multiple actors working in
What is the This sector continues
this sector is one where the Espionage- concert) in 16% of Public
same? to be targeted by motivated actor is consistently among Administration breaches this
Financially motivated
the highest. year. That is significant, given
external threat
that we didn’t see multiple Actor
actors as well as
Within the System Intrusion pattern, we breaches the past two years in
spying Nation-states
saw a slight decrease in Ransomware this sector, and in 2020’s report,
that are interested
as a tactic. This doesn’t mean you it was only at 2%.
in what their rivals
should ignore it, however, as it remains
are doing. Personal
a favored method of disrupting
data remains the
government workings while generating
most often stolen
income for the adversaries.
data type.
While it is possible to reach their goals
Summary
by themselves, these actors are not
This sector continues to make top opposed to recruiting help from within
scores in Espionage-motivated the organization. We see evidence of
breaches. It is also rich in multiple actor collusion (multiple actors working in
breaches. External and Partner or concert) in 16% of Public Administration
Internal actors working together to breaches this year. That is significant,
steal data is not the kind of international given that we didn’t see multiple Actor
cooperation we want to see fostered. breaches the past two years in this
sector, and in 2020’s report, it was
only at 2%.
50 There are explosions and car chases in there too, we’re sure of it.
2023 DBIR Industries

Retail
63
SCIAN 54–44
Can you breach If you are in the Retail world and you
Frequency 406 incidents,
operate an e-commerce platform,
193 with confirmed
me now? then this section is especially worth
data disclosure
paying attention to. Within Retail,
Top patterns System Intrusion, we often find the “Magecart”51-type
Social Engineering Some people turn to the Retail sector actors. These criminals find ways of
and Basic Web as a form of therapy—and we on embedding their malicious code within
Application Attacks the DBIR team probably have more your site’s credit card processing page.
represent 88% of dragons, guitars and cuckoo clocks This allows them to quietly and subtly
breaches (don’t ask) than we really need. Sadly, abscond with your customers’ payment
criminals have been enjoying their data without actually affecting the
Threat actors External (94%), own “retail therapy” by targeting this functionality of your website. Currently,
Internal (7%), sector for many years. They continue these attacks represent about 18%
Multiple (2%), to do so by capitalizing on this of Retail breaches. While we freely
Partner (2%) industry’s heavy use of payment data. admit that we don’t always know how
(breaches) these Actors were able to access the
web application and upload their bad
Actor motives Financial (100%),
Top actions/ JavaScript, we have seen them use
Espionage (1%)
several different tricks (Figure 61).
(breaches)
top vectors
Data Payment (37%),
compromised Credentials (35%),
When it comes down to how these
Other (32%),
breaches and incidents occur, it is a
Personal (23%)
roundup of the usual suspects, with
(breaches)
both Ransomware and Use of stolen
What is the Retail organizations credentials among the top, along with
same? continue to be Email and Web applications for vector.
lucrative targets for However, there is a relatively unique
cybercriminals addition to some of these actions—the
looking to collect “Export data” and “Capture app data.”
Payment card data. This is also one of the few industries
where we see “Other” creep up as
Summary one of the top actions (Figure 60), and
that’s largely because there’s a variety
While the same three patterns dominate
of secondary actions that actors are
this industry as many others, Retail
using to either deploy their ransomware
has the added bonus of being targeted
or find a way to collect payment cards.
for its Payment card data in addition
to common threats like Ransomware
and Basic Web Application Attacks.
Figure 60. Top Action varieties for
Retail breaches (n=182)
51 In layman’s terms, it is when wizards race each other in go-carts.
2023 DBIR Industries

Stolen Considering the function of this This begs the question: Where is this
industry, it is hardly surprising to see data being stolen from? Because it’s
credentials: Payment card data as one of the difficult to protect something if you
most common data types breached, don’t know what you are protecting.
$5. Domain accounting for 37% of breaches this Luckily, we have some data that may
year. If you look at Figure 62, you can help. In our analysis of just payment
hosting: $12. readily observe that Payment card data card breaches in Retail, we found that
has been trending downward since its 70% of breaches originated from Web
high-water mark in 2018. However, we applications, 17% from Gas terminals
Malicious
are seeing a relatively large increase in and 8% from PoS servers. This once
Payment card data stolen as compared again illustrates how e-commerce has
JavaScript:
to last year. Although stealing card made it way too easy to get what you
data is a tried-and-true method of want, including stolen credit cards.
$50. Snagging
monetizing data, sometimes the threat If you are looking for some added
actor simply wants a quicker payday. incentive, it’s worth mentioning that by
all the fullz:
Ransomware has definitely skewed the time our 2024 DBIR is published,
some of the data in this sector, but it you should all already be compliant
priceless. seems as if Payment card data is still with Payment Card Industry (PCI)
extremely valuable and will continue to Data Security Standard (DSS) 4.0.52
remain a popular target.
Figure 61. Top Action vectors in Retail Figure 62. Payment card over time in Retail breaches
breaches (n=130)
52 https://www.pcisecuritystandards.org/resources-overview/
2023 DBIR Industries 64

Small and
medium business
“ Let’s do In past reports we have discussed the Large businesses (more than
research we conduct with regard to 1,000 employees)
some word controls—in particular, the work we
have done with MITRE to map VERIS
Frequency 496 incidents,
problems!” to ATT&CK. This year, we would like 227 with confirmed
to take this research a bit more into
data disclosure
the real world and apply it to how you
— said no one ever (except would use these mappings with the Top patterns System Intrusion,
math teachers) appropriate CIS Implementation Group Social Engineering
protective controls. and Basic Web
In certain prior reports, we have
Application Attacks
compared and contrasted small
represent 85% of
and medium businesses (SMBs) Small businesses (less than breaches
against large organizations to 1,000 employees)
determine whether the attack surface Threat actors External (89%),
differed significantly between them. Frequency 699 incidents, Internal (13%),
Increasingly, both SMBs and large 381 with confirmed Multiple (2%),
companies are using similar services data disclosure Partner (2%)
and infrastructure, and that means (breaches)
that their attack surfaces share more Top patterns System Intrusion,
in common than ever before. This Social Engineering Actor motives Financial (97%),
has led to a convergence of attack and Basic Web Espionage (3%),
profiles regardless of the size of the Application Attacks Ideology (2%),
organization. However, what is very represent 92% of Convenience (1%),
different is the ability of organizations to breaches Fun (1%) (breaches)
respond to threats due to the number of
resources they can deploy in the event Threat actors External (94%), Data Internal (41%),
that they are attacked. Internal (7%), compromised Credentials (37%),
Multiple (2%), Other (30%),
The tables on the right illustrate the fact Partner (1%) System (22%)
that SMBs and large organizations have (breaches) (breaches)
increasingly become similar to each
other. This phenomenon began several Actor motives Financial (98%),
Table 4. At a glance for large
years ago, and by now there is so little Espionage (1%), organizations
difference based on organizational Convenience (1%),
size that we were hard-pressed to Grudge (1%)
make any distinctions whatsoever. (breaches)
Therefore, this year we decided to
Data Credentials (54%),
look at these a bit differently53 by
compromised Internal (37%),
looking at the implementation of
Other (22%),
security controls for various size
System (11%)
SMBs (smaller, midsize and larger)
(breaches)
and how they may overlap or differ.
Table 3. At a glance for SMB
53 Again, there is that refocusing thing we keep talking about.
2023 DBIR Small and medium business 65

It’s not easy an organization may want to comply When you drill further into the Sub-
with as their adopted standard. You Controls, more granularity should guide
being small. will see that they are broken into three you in your quest for maturing your
Implementation Groups, and each one organization’s security posture. Each
is geared to the organization’s maturity organization will need to customize
Let’s assume you’re a startup—a tiny level. Since we’re at the beginning here, and prioritize according to its own risk
company in its infancy. You have very, we will start with Implementation Group profile and tolerance, but it is at least
very limited resources for implementing 1 (IG1). While these are all good controls a place to begin. Once the most likely
security controls of any kind. Your IT and should be on the road map, let’s suspects are accounted for, move onto
person is also your security person is take a more threat-centric approach in the next mostly likely attack pattern
also your Jack- (or Jill-) of-all-trades our scenario. you may be facing and determine
who wears many hats and never sleeps. how to handle that. Using data-driven
You can see in Tables 3 and 4 that information on your most probable risk
The first step is to see which controls regardless of an organization’s size, areas is a defensible strategy toward
are recommended for your level of they are most commonly going to prioritizing controls with few resources.
security maturity and resources. But face the System Intrusion pattern. Hopefully after some progress is made,
where to begin? We like the CIS Critical In last year’s report, we mapped your Jack-/Jill-of-all-trades can go back
Security Controls Navigator as a good the Controls to the pattern and to sleeping at night.
starting point.54 It breaks down each showed which were most commonly
of the CIS Controls into small, easy- going to help you in an attack.55
to-consume chunks and then maps The result in IG1 shows Controls 14
them to various security standards that (89%), 11 (80%) and then 5 (67%).
Control Description
14 Security Awareness and Skills Training
Establish and maintain a security awareness program to
influence behavior among the workforce to be security
conscious and properly skilled to reduce cybersecurity
risks to the enterprise.
11 Data Recovery
Establish and maintain data recovery practices sufficient to
restore in-scope enterprise assets to a preincident and
trusted state.
5 Access Control Management
Use processes and tools to create, assign, manage
and revoke access credentials and privileges for user,
administrator and service accounts for enterprise assets
and software.
Table 5. CIS Implementation Group 1 Controls for Incident Classification Patterns
most commonly encountered by SMBs
54 https://www.cisecurity.org/controls/cis-controls-navigator/
55 2022 DBIR, Appendix B: VERIS and Standards, p. 96
2023 DBIR Small and medium business 66

Midsize is “ You get a These Controls mature along with
your organization. Therefore, let us
the right size. resource! examine the IG3 Controls with regard
to the third most common pattern
You get a for SMB: Basic Web Application
You’ve been at this a while. You’re Attacks. The first, Control 17 (100%),
not tiny, but you’re not quite at the resource! we talked about in the previous
enterprise level just yet. You have been section, but Controls 16 (100%) and
working diligently at maturing your 18 (100%) we have not yet discussed.
Everybody
processes in both IT operations and
in information security. You have put • Control 16 – Application
gets a
in place the Controls in IG1 and are Software Security
now eyeing IG2 to take your company Manage the security life cycle
resource!”
to the next level of protection. of in-house developed, hosted
or acquired software to prevent,
With that in mind, let’s take a look at detect and remediate security
the IG2 controls that cover the Social Now let’s pivot to look at the larger weaknesses before they can
Engineering pattern, which is the organizations in the SMB area. To impact the enterprise.
second largest threat for SMBs. The clarify, we are still writing with regard
first two controls are the same main to SMBs, we simply mean the larger • Control 18 – Penetration Testing
categories as they were for System companies that still fall into that Test the effectiveness and
Intrusion, Control 5 (100%) and category (<1,000 employees). When resiliency of enterprise assets
Control 14 (100%). However, the third your company reaches this point, there through identifying and exploiting
control is different for this pattern: are more resources available to throw weaknesses in controls (people,
at problems, whether in the form of processes and technology), and
• Control 17 – Incident Response more people, more technology options simulating the objectives and
Management or just plain more cash,56 and bringing actions of an attacker.
Establish a program to develop those resources to bear can yield
and maintain an incident response substantial benefits. At this, level you Control 16 is certainly timely,
capability (e.g., policies, plans, may have tackled IG1 and IG2 and are considering the SolarWinds case from
procedures, defined roles, training and ready for IG3 Controls. last year’s report and the Log4j impact
communications) to prepare, detect discussed in this year’s report, so we
and quickly respond to an attack. should have no problem seeing the
relevance of this Control. Sub-Controls
An Incident Response Management 16.2: Establish and Maintain a Process
plan is key to all areas of security but to Accept and Address Software
perhaps especially so when it comes Vulnerabilities, 16.4: Establish and
to Social Engineering attacks for a few Manage an Inventory of Third-Party
reasons. Many of these attacks, such Software Components, and 16.5: Use
as pretexting, tend to escalate quickly Up-to-Date and Trusted Third-Party
and can have a high impact. Perhaps Software Components would have
just as importantly, employees need to gone a long way to defending against
feel secure in the knowledge that they both of those cases.
have a place they can report these
incidents to when they occur because
the sooner they report them, the more
quickly you can address them.
56 And this never really hurts, does it?
2023 DBIR Small and medium business 67

Once an entity has reached the larger
end of the SMB scale, Control 18
From the Center for Internet Security:
also comes into play. Establishing
penetration testing capabilities and
Report after report, and study of this enterprise is to keep the
incorporating their findings into the
after study, shows that many business operational, as they have
security processes can only improve
attacks are successful because a limited tolerance for downtime.
the information security posture of a
network owners did not know their The sensitivity of the data that they
larger SMB. This is basically real-world
enterprise assets, the software are trying to protect is low and
testing of your controls to make sure
they had running and where their principally surrounds employee and
they are performing how you expect
critical data was. Knowing your financial information.
them to. Like backups, only controls
environment is foundational to
that have been tested and verified any cybersecurity program, so Safeguards selected for IG1 should
should be trusted. they encompass the first three be implementable with limited
controls of the CIS Critical cybersecurity expertise and aimed
Now that you’ve already looked at the
Security Controls (Controls). to thwart general, non-targeted
Controls and prioritized them, you
After all, you can’t protect what attacks. These Safeguards will
know what you’re most likely to be
you don’t know you have. also typically be designed to work
hit with and you’re working your way
in conjunction with small or home
through to the end—your ducks are
After understanding your office commercial off-the-shelf
almost all in a row. You have balanced
environment, you can prioritize (COTS) hardware and software.
preventive and detective capabilities
where to apply and which
and are on your way to being able to not controls to implement across your But no matter the size or
only detect when something bad has enterprise. At CIS we know that complexity of your business, we
happened but also respond quickly and this will take time and resources, recommend that all organizations
appropriately. You have moved from the which is why we have prioritized begin with IG1. We also refer to
basics of putting your plan together to the Controls and supporting IG1 as Essential Cyber Hygiene
implementing a road map. Safeguards to help you plan your because it provides the actions
security improvement program. necessary for an organization
A few final things to consider at this
We do this through Implementation to defend itself against the
point: Are you looking at aligning with
Groups (IGs). There are three IGs major attack types being used
a particular compliance framework?
and are based on the risk profile by cybercriminals. IG1 is not just
Do you track metrics around security
and resources an enterprise has another list of good things to
in your environment? Do your efforts
available to them to implement do; it’s an essential set of steps
result in ongoing improvements to
controls. Each IG builds upon the that helps all enterprises defend
your security posture, or do they just
previous one. So IG2 builds upon against real-world threats. And it
provide a point-in-time snapshot that
IG1 and IG3 comprises all the provides a strong foundation for
says, “I was good at this moment,
Controls and Safeguards. your cyber maturity growth, or as
but then things changed”? There
your security needs change. This
is quite a bit you can do when you
We describe a typical IG1 is a strong claim, but we back it up
use good information about what
enterprise as small to medium- with our use of the best-available
is happening in your organization
sized with limited IT and summaries of attacks (like the
to steer your security strategy.
cybersecurity expertise to dedicate Verizon DBIR), and an open, shared
toward protecting IT assets and methodology (the CIS Community
personnel. The principal concern Defense Model v2.057).
57 https://www.cisecurity.org/insights/white-papers/cis-community-defense-model-2-0
2023 DBIR Small and medium business 68

5
Regions

Regions:
Introduction
This edition of the DBIR marks the fourth year we have examined cybercrime LAC: Latin America and the Caribbean,
incidents from a macro-regional point of view. We hope our readers find this including South America (005), Central
broader look at cybercrime useful and instructive. As previously mentioned, America (013) and Caribbean (029)
our visibility into a certain region is determined by many variables, including
contributors, regional disclosure laws and our own data. If your part of the world NA: Northern America (021), including
is not featured in the following pages, please contact us about becoming a data the United States and Canada
contributor and motivate other organizations in your area to do the same so that
As in previous years, we have sliced and
we can keep growing and improving our coverage each year. Even if your region is
diced our data in many ways, and this
not represented here, this does not mean we have no visibility into the region but
time we are presenting the data for the
rather that we don’t have enough incidents in that geography to have a statistically
various regions a little differently. Long-
significant section.
time readers will recognize the At-
We define the regions of the world in accordance with the United Nations M4958 a-Glance tables that we put in each
standards, which combines the super-region and sub-region of a country together. major section, only in this case, we’ve
By so doing, the regions we will examine are as follows: combined them to give you an easy way
to see just how similar (and different)
APAC: Asia Pacific, including Southern Asia (034), South-eastern Asia (035), each of the regions are with regard to
Central Asia (143), Eastern Asia (030) and Oceania (009) the frequency, top patterns, etc.
EMEA: Europe, Middle East and Africa, including Northern Africa (015), Europe
(150) and Eastern Europe (151), and Western Asia (145)
Region Frequency Top patterns Threat actors Actor motives Data compromised
APAC 699 incidents, Social Engineering, External (92%), Financial (61%), Internal (56%),
164 with confirmed System Intrusion and Internal (9%), Espionage (39%), Secrets (42%),
data disclosure Basic Web Application Partner (2%), Convenience (2%), Other (33%),
Attacks represent 93% Multiple (2%) Grudge (2%), Credentials (29%)
of breaches (breaches) Secondary (1%) (breaches)
(breaches)
EMEA 2,557 incidents, System Intrusion, Social External (98%), Financial (91%), Credentials (53%),
637 with confirmed Engineering and Basic Internal (2%), Espionage (8%), Internal (37%),
data disclosure Web Application Attacks Multiple (1%) Ideology (1%), System (35%),
represent 97% of (breaches) Fun (1%) (breaches) Other (15%)
breaches (breaches)
LAC 535 incidents, System Intrusion, Social External (95%), Financial (93%), System (55%),
65 with confirmed Engineering and Basic Internal (5%), Espionage (11%), Internal (32%),
data disclosure Web Application Attacks Partner (2%), Ideology (2%) Classified (23%),
represent 94% of Multiple (2%) (breaches) Credentials (23%),
breaches (breaches) Other (19%)
(breaches)
NA 9,036 incidents, System Intrusion, Basic External (94%), Financial (99%), Credentials (67%),
1,924 with Web Application Attacks Internal (12%), Espionage (1%), Internal (50%),
confirmed data and Social Engineering Multiple (9%), Grudge (1%) Personal (38%),
disclosure represent 85% of Partner (2%) (breaches) Other (24%)
breaches (breaches) (breaches)
Table 6. At a glance for regions
58 https://unstats.un.org/unsd/methodology/m49/
2023 DBIR Regions 70

It is readily apparent that the System
Intrusion pattern is top of the heap for
all regions except APAC, where it is still
a large problem, just not as pressing
as Social Engineering. It is also quite
clear that the who and why behind
cybercrime is the Financially motivated
external actor. We see more variation in
the data types favored by these actors
in the different regions, and while our
data frequently shows us the “what,” it
rarely tells us the “why.” It may be that
certain data types are better protected
by regulatory requirements in certain
regions versus others. It may be some
other factor we haven’t thought of; it’s
hard to say. But clearly, Credentials are
still figuring prominently and need to
be made less valuable when breached
(hint: we’re looking at you, MFA).
Just feast your eyes on these lovely
heatmaps in Figure 63. This is our
favorite way to illustrate how different
(or similar) these attacks are based on
geography. When broken out by pattern
and region, you can clearly see that
although there are definitely differences
(many of which are no doubt based on
industry and their resulting common
infrastructure partners), there are
some concentrations for each
region as well as across regions.
Hopefully this is illustrative of what
your region—and, when combined with
other data in this report, industries
and organization size—is most prone
to in terms of attacks so that you can
better direct your defensive strategy.
Figure 63. Incidents and breaches by region
If you’re still unsure where to start and
you skipped over the SMB section, it is
a good reference for how to apply the
information in this report.
2023 DBIR Regions 71

6
Wrap-up

This wraps up another year of
delving deep into data breaches
to mine for useful nuggets
of information and analysis.
It is, as always, our hope that you found As always, be well, be
it instructive, actionable and maybe
prosperous and be
even fun to read.59 All of us here on
prepared for anything.60
the team feel extremely fortunate to
be where we are and doing what we
do. We would also like to extend our
most sincere gratitude once again
to our faithful readers. The feedback
and stories you have provided to us
throughout the years drives us to work
diligently to continually evolve and
improve this report.
59 OK, that might be a stretch. How about “not the all-around cure for insomnia”?
60 Unofficial DBIR team motto, by the way
2023 DBIR Wrap-up 73

Year in review
January The VTRAC Intelligence Analysts experienced déjà vu as we began 2022 tracking attacks exploiting
Log4j in much the same way SolarWinds campaigns kicked off 2021. During the first week of December
2021, the Log4j vulnerability became the biggest blip on the InfoSec risk radar. About a week later,
VMware observed Log4Shell attacks, and “the majority of the attacks target Linux systems.” Log4j,
and especially attacks on VMware, remained a persistent risk issue through 2022. Before the end of
the month, Prophet Spider, a notorious initial access broker, was selling VMware Horizons systems
breached using Log4j. The Russian Ember Bear threat actor (TA) launched attacks on Ukraine using
WhisperGate wiper malware. Microsoft patched a zero-day vulnerability in the Win32k.sys driver. Apple
patched a zero-day vulnerability impacting iPhones and iPads.
February Collection and analysis of intelligence covering cyberattacks supporting Russia’s February 2022 invasion
of Ukraine was the most significant activity for VTRAC in February. On and before February 24, the
Russian Main Intelligence Directorate (GRU)61 launched AcidRain wiper malware attacks on the Viasat
satellite communications terminals in Ukraine, but significant collateral damage was also done to terminals
scattered across Europe. Ukraine was targeted with at least six new wiper malwares by Russian TAs.
On February 25, the notorious cybercrime-as-a-service TA, “Conti” announced support for Russia. Two
days later, Twitter user “@ContiLeaks” released 400 internal Conti files including 60,000 chat messages.
“Ordinary” cyber intelligence in February included zero-day vulnerabilities in Zimbra, Chrome, Apple OS
and Adobe Commerce/Magento. Cybercriminals controlling Emotet leveraged the Russia-Ukraine conflict
in bait themes in their malspam.
March Zero-day exploitation of vulnerabilities in Chrome, Firefox, Trend Micro Apex Central and Mitel business
telephony components kept enterprise security and patch management teams busy in March. Increased
vigilance looking for evidence of Russian-Ukraine cyber-attacks yielded intelligence on APT actors from
China, Iran and North Korea. Chinese APT actor Mustang Panda used the Russia-Ukraine conflict in
attacks on diplomatic missions, think tanks and ISPs in Mongolia, Vietnam, Myanmar and Russia. New
intelligence detailing the exploitation of a vulnerable web application led to lateral exploitation of networks
in several US state governments by APT41 (Winnti), another Chinese APT actor. Iranian APT MuddyWater
targeted the Arabian Peninsula, Turkey and Pakistan. The largest cryptocurrency theft to date occurred
when North Korea’s Lazarus Group stole more than US$620 million from the Ronin Network. North
Korean APT Kimsuky targeted a nuclear-related think tank with their signature “BabyShark” malware. The
Lapsus$ TA shifted tactics, techniques and procedures (TTP) from ransomware to data theft extortion,
claiming compromises at Microsoft, Okta, Nvidia and Samsung.
61 Now known as the Main Directorate of the General Staff of the Armed Forces of the Russian
Federation—how’s that for a mouthful?
2023 DBIR Wrap-up 74

April Patch management teams were especially harried in April mitigating zero-day vulnerabilities under
attack in the Windows CLFS, Apple OS, Trend Micro security products, Chrome browser and VMware.
Sophos firewalls came under attack hours after release of a security advisory and patches. SonicWall,
Zyxel and FortiGuard also released security advisories and updates for their firewalls. The VTRAC
began collecting more than the usual volume of intelligence on APT-grade actors yielding TTP updates
usable by both other TAs and Verizon Cyber Security Consulting clients. A campaign by the Chinese
APT-grade actor Deep Panda had been exploiting the ill-famed Log4Shell vulnerability in VMware
Horizon servers missing December’s patches. We also collected intelligence on Russian state actors
attacking Ukraine, including details on the attack on Viasat in February, and four operations by North
Korea’s Lazarus Group. Attacks by cybercrime TAs including LockBit, FIN7, ALPHV, Hive, CL0P and
Conti continued unabated.
May Vulnerabilities in infrastructure components began to emerge as a recurring theme in 2022. In the
wild exploitation commenced within one week of the release of security advisories and patches in
vulnerabilities in F5 BIG-IP appliances (CVE-2022-1388) and Zyxel firewalls (CVE-2022-30525).
Microsoft patched 74 vulnerabilities in May’s Patch Tuesday, including a zero-day Windows LSA Spoofing
Vulnerability (CVE-2022-26925). CISA initially added it to their Known Exploited Vulnerabilities Catalog
but quickly removed it to avoid outages caused by authentication failures resulting from precipitous
domain controller patching. Two infamous malware families, Emotet and REvil, thought to have shut down,
each made a resurgence in May, but the controversial ransomware group Conti disbanded. As May ended,
intelligence emerged that a Chinese APT actor was exploiting another Windows zero-day vulnerability
(CVE-2022-30190) to attack targets in Russia and Belarus. The “Folina” vulnerability was a remote code
execution vulnerability in the Microsoft Support Diagnostic Tool (MSDT).
June Days after the discovery of Folina, Atlassian announced patches for a zero-day remote code
execution vulnerability (CVE-2022-26134) in Confluence Data Center and Server. Over the Memorial
Day weekend in the United States, Volexity’s incident responders had detected suspicious activity
on two internet-facing Atlassian Confluence Servers with Behinder web shells installed, probably by
Chinese threat actors. Volexity also reported that a zero-day vulnerability in Sophos Firewall (CVE-
2022-1040) was being exploited by a Chinese APT actor they labeled, “DriftingCloud.” Intelligence
indicated that widespread attacks, by the infamous Chinese APT actor Deep Panda, were continuing
to successfully exploit Log4j in unpatched VMware Horizon servers.
2023 DBIR Wrap-up 75

July The release of cyber intelligence reports usually precedes the Black Hat USA and DEF CON conferences.
The quality, quantity and breadth of those reports in 2022 represented the most significant intelligence
for the month of July. Tracking successful TTPs has been an intelligence requirement because our
adversaries are adept at learning from open source intelligence (OSINT), making agility in tuning security
architecture an imperative. Exploitation of zero-day vulnerabilities in Google’s Chrome browser and
Windows CSRSS kept patch management teams busy, as did three unexploited critical vulnerabilities
in multiple Atlassian products. Intelligence emerged that a ransomware and crypto mining TA had been
successfully exploiting one, CVE-2022-26138, since June.
August In addition to “Folina” a second zero-day remote code vulnerability in the Microsoft Windows Support
Diagnostic Tool was discovered, exploited and patched in August. Apple, macOS, iOS and iPadOS
plus Google Chrome all had their own zero-day vulnerabilities reported and patched. In early August,
current and former employees of Twilio received smishing messages purporting to be from Twilio’s IT
department calling for a password change. That breach led to the compromise of 9,931 accounts in
130+ organizations, most of which used Okta identity and access management solutions. The threat
actor compromised 93 users of Twilio’s Authy multifactor authentication solutions. Intelligence emerged
attributing these and multiple identity attacks at least as far back as March to the “Scatter Swine” or
Oktapus TA.
September September was the zero-day-palooza month for 2022. Two days into the new month, Google Chrome
and Microsoft Edge were patching a zero-day vulnerability in their browsers. Trend Micro mitigated
their second zero-day vulnerability of the year following successful in-the-wild attacks on their Apex
One security products. And Sophos firewall customers had to patch their second zero-day of the
year. The most significant zero-days were attributed to a Chinese APT actor that chained a pair of
Windows vulnerabilities quickly nicknamed “ProxyNotShell.” VMware servers were also targeted by
a Chinese cyberespionage actor employing malicious vSphere installation bundles for ESXi, Linux
and Windows servers.
2023 DBIR Wrap-up 76

October Microsoft did not patch “ProxyNotShell” in October’s Patch Tuesday release, but they did release a patch
for CVE-2022-41033, an elevation of privilege zero-day. Fortinet patched a zero-day authentication
bypass vulnerability in multiple products. More than 1,600 servers were breached by exploiting a zero-day
in Zimbra Collaboration Suite, CVE-2022-41352, and tardy patching of three earlier Zimbra vulnerabilities.
“Text4Shell” entered the InfoSec lexicon after a new Apache Commons Text library vulnerability, even
though no attacks were reported. Two notorious malwares repurposed to expand their target sets:
URSNIF and Emotet each exhibited significant TTP shifts, the former from banking Trojan to initial access
downloader and the latter awoke from a four-month siesta as the tool of a full-service malware-as-a-
service operator. Other zero-day attacks, vulnerabilities and patches were reported in Chrome browser
and, separately, iOS and iPadOS.
November Several strains of malware highlighted InfoSec risk intelligence in November. Forty days after the initial
reports of ProxyNotShell attacks on Exchange, Microsoft patched those two vulnerabilities. Microsoft
also patched four other zero-days in its products on Patch Tuesday. Chrome browser also mitigated a
zero-day vulnerability. Updated intelligence on three malware families were prominent in the VTRAC
collections. SocGholish is a JavaScript framework and malware-as-a-service used by cybercriminals
to implement drive-by-downloads. Bumblebee, a new malicious loader, first appeared in May and in
November began delivering Meterpreter and Cobalt Strike payloads. Cybercriminals controlling the
Raspberry Robin worm evolved into initial access brokers for deploying other payloads.
December Breaking the string of end-of-year InfoSec milestones set in 2020 with SolarWinds Orion and in 2021
by Log4j, December 2022 was comparatively boring. Intelligence indicated several threat actors were
abusing Microsoft developer accounts to get malicious drivers signed through their profiles to be used
in cyberattacks, including ransomware incidents and SIM swapping operations. The streak of months
with attacks exploiting zero-day vulnerabilities was extended with reports of successful attacks on
Microsoft, Apple, Fortinet and Citrix products. OWASSRF is a new attack chain exploiting on-premises
Exchange Servers using the URL rewrite mitigations provided by Microsoft responding to September’s
ProxyNotShell attack chain. The Play ransomware threat actors had exploited OWASSRF to attack at
least eight victims. Among the best intelligence collections was a virtual order of battle of TA subordinate
to Bureau 121 in the Reconnaissance General Bureau (RGB), North Korea’s military intelligence agency.
Special thanks to Dave Kennedy of the Verizon Threat Research Advisory Center (VTRAC) for his
continued support and yearly contribution to this report.
2023 DBIR Wrap-up 77

7
Appendices

Appendix A:
Methodology
One of the things readers value most Non-committal The collection method and conversion
about this report is the level of rigor and techniques differed between
integrity we employ when collecting, disclaimer contributors. In general, three basic
analyzing and presenting data. Knowing methods (expounded below) were used
our readership cares about such to accomplish this:
things and consumes this information We must reiterate that we make no
with a keen eye helps keep us honest. claim that the findings of this report are 1. D irect recording of paid external
Detailing our methods is an important representative of all data breaches in all forensic investigations and related
part of that honesty. organizations at all times. Even though intelligence operations conducted by
we believe the combined records from Verizon using the VERIS Webapp
First, we make mistakes. A column all our contributors more closely reflect
transposed here; a number not updated reality than any of them in isolation, 2. D irect recording by partners
there. We’re likely to discover a few it is still a sample. And although we using VERIS
things to fix. When we do, we’ll list them believe many of the findings presented
3. Converting partners’ existing schema
on our corrections page: verizon.com/ in this report to be appropriate for
into VERIS
business/resources/reports/dbir/2023/ generalization (and our conviction in
corrections/. this grows as we gather more data and
All contributors received instruction to
compare it to that of others), bias exists.
omit any information that might identify
Second, we check our work. The same
organizations or individuals involved.
way the data behind the DBIR figures
can be found in our GitHub repository,62
The DBIR Some source spreadsheets are
as with last year, we’re also publishing
converted to our standard spreadsheet
our fact check report there as well.
process formatted through automated mapping
It’s highly technical, but for those
to ensure consistent conversion.
interested, we’ve attempted to test
Reviewed spreadsheets and VERIS
every fact in the report.
Our overall process remains intact Webapp JavaScript Object Notation
and largely unchanged from previous (JSON) are ingested by an automated
Third, science comes in two flavors:
years.63 All incidents included in this workflow that converts the incidents
creative exploration and causal
report were reviewed and converted, if and breaches within into the VERIS
hypothesis testing. The DBIR is
necessary, into the VERIS framework JSON format as necessary, adds
squarely in the former. While not
to create a common, anonymous missing enumerations and then
perfect, we believe we provide the
aggregate dataset. If you are unfamiliar validates the record against business
best obtainable version of the truth (to
with the VERIS framework, it is short logic and the VERIS schema. The
a given level of confidence and under
for Vocabulary for Event Recording automated workflow subsets the data
the influence of biases acknowledged
and Incident Sharing. It is free to use, and analyzes the results. Based on
below). However, proving causality is
and links to VERIS resources are at the the results of this exploratory analysis,
best left to randomized control trials.
beginning of this report. the validation logs from the workflow
The best we can do is correlation. And
and discussions with the partners
while correlation is not causation, they
providing the data, the data is cleaned
are often related to some extent and
and reanalyzed. This process runs
often useful.
nightly for roughly two months as data
is collected and analyzed.
62 https://github.com/vz-risk/dbir/tree/gh-pages
63 As does this sentence
2023 DBIR Appendices 79

Incident data Finally, “Not Applicable,” (normally incident,” the entry is assessed
“NA”), may be counted or not counted for quality. We create a subset of
depending on the claim being analyzed. incidents (more on subsets later) that
Our data is non-exclusively multinomial pass our quality filter. The details
meaning a single feature, such as This year we have made liberal use of what is a “quality” incident are:
“Action,” can have multiple values (i.e., of confidence intervals to allow us to
“Social,” “Malware” and “Hacking”). analyze smaller sample sizes. We have • The incident must have at least seven
This means that percentages do adopted a few rules to help minimize enumerations (e.g., threat actor
not necessarily add up to 100%. bias in reading such data. Here we variety, threat action category, variety
For example, if there are five botnet define “small sample” as less than of integrity loss, et al.) across 34 fields
breaches, the sample size is five. 30 samples. OR be a DDoS attack. Exceptions are
However, since each botnet used given to confirmed data breaches with
phishing, installed keyloggers and 1. S ample sizes smaller than five are too less than seven enumerations.
used stolen credentials, there would small to analyze.
be five Social actions, five Hacking • The incident must have at least one
actions and five Malware actions, 2. W e won’t talk about count or known VERIS threat action category
adding up to 300%. This is normal, percentage for small samples. (hacking, malware, etc.).
This goes for figures, too, and is
expected and handled correctly
why some figures lack the dot In addition to having the level of details
in our analysis and tooling.
for the median frequency. necessary to pass the quality filter, the
Another important point is that when incident must be within the timeframe of
looking at the findings, “unknown” is 3. For small samples we may talk about analysis, (November 1, 2021, to October
equivalent to “unmeasured.” Which is the value being in some range or 31, 2022, for this report). The 2022
to say that if a record (or collection of values being greater/less than each caseload is the primary analytical focus
records) contains elements that have other. These all follow the confidence of the report, but the entire range of
been marked as “unknown” (whether it interval approaches listed above. data is referenced throughout, notably
is something as basic as the number of in trending graphs. We also exclude
records involved in the incident, or as incidents and breaches affecting
complex as what specific capabilities a Incident individuals that cannot be tied to an
piece of malware contained), it means organizational attribute loss. If your
that we cannot make statements about eligibility friend’s laptop was hit with Trickbot, it
that particular element as it stands would not be included in this report.
in the record—we cannot measure
where we have too little information. For a potential entry to be eligible Lastly, for something to be eligible
Because they are “unmeasured,” for the incident/breach corpus, a for inclusion into the DBIR, we have
they are not counted in sample sizes. couple of requirements must be to know about it, which brings us
The enumeration “Other,” however, met. The entry must be a confirmed to several potential biases we will
is counted as it means the value was security incident defined as a discuss below.
known but not part of VERIS (or not one loss of confidentiality, integrity or
of the other bars if found in a bar chart). availability. In addition to meeting
the baseline definition of “security
2023 DBIR Appendices 80

Acknowledgement and The first type of bias is random
bias introduced by sampling. This
analysis of bias year, our maximum confidence is
+/- 0.7% for incidents and +/- 1.4%
for breaches, which is related to our
Many breaches go unreported (though can conduct an exhaustive census of sample size. Any subset with a smaller
our sample does contain many of every breach that happens in the entire sample size is going to have a wider
those). Many more are as yet unknown world each year (our study population), confidence margin. We’ve expressed
by the victim (and thereby unknown to we must use sampling. Unfortunately, this confidence in the complementary
us). Therefore, until we (or someone) this process introduces bias. cumulative density (slanted) bar charts,
hypothetical outcome plot (spaghetti)
line charts and quantile dot plots.
Breaches Breaches
The second source of bias is sampling
bias. We strive for “the best obtainable
version of the truth” by collecting
breaches from a wide variety of
contributors. Still, it is clear that we
conduct biased sampling. For instance,
some breaches, such as those publicly
disclosed, are more likely to enter our
corpus, while others, such as classified
breaches, are less likely.
The four figures on the left are an
attempt to visualize potential sampling
bias. Each radial axis is a VERIS
enumeration, and we have stacked
Figure 64. Individual contributors Figure 65. Individual contributors bar charts representing our data
per Action per Actor contributors. Ideally, we want the
distribution of sources to be roughly
equal on the stacked bar charts along
all axes. Axes only represented by
Breaches Breaches
a single source are more likely to be
biased. However, contributions are
inherently thick tailed, with a few
contributors providing a lot of data
and a lot of contributors providing a
few records within a certain area. Still,
we mostly see that most axes have
multiple large contributors with small
contributors adding appreciably to the
total incidents along those axes.
Figure 66. Individual contributors Figure 67. Individual contributors
per Asset per Attribute
2023 DBIR Appendices 81

You’ll notice rather large contributions Data subsets Non-incident
on many of the axes. While we’d
generally be concerned about this, they data
represent contributions aggregating We already mentioned the subset
several other sources, not actual single of incidents that passed our quality
contributions. It also occurs along most requirements, but as part of our Since the 2015 issue, the DBIR includes
axes, limiting the bias introduced by analysis there are other instances data that requires the analysis that
that grouping of indirect contributors. where we define subsets of data. These did not fit into our usual categories of
subsets consist of legitimate incidents “incident” or “breach.” Examples of
The third source of bias is confirmation that would eclipse smaller trends if left non-incident data include malware,
bias. Because we use our entire dataset in. These are removed and analyzed patching, phishing and DDoS. The
for exploratory analysis, we cannot test separately, though may not be written sample sizes for non-incident data tend
specific hypotheses. Until we develop about if no relevant findings were, well, to be much larger than the incident
a collection method for data breaches found. This year we have two subsets data but from fewer sources. We
beyond a sample of convenience, this is of legitimate incidents that are not make every effort to normalize the
probably the best that can be done. analyzed as part of the overall corpus: data (for example, weighting records
by the number contributed from the
As stated above, we attempt to mitigate 1. W e separately analyzed a subset of
organization so all organizations are
these biases by collecting data from web servers that were identified as
represented equally). We also attempt
diverse contributors. We follow a secondary targets (such as taking
to combine multiple partners with
consistent multiple-review process, and over a website to spread malware).
similar data to conduct the analysis
when we hear hooves, we think horses,
wherever possible. Once analysis is
not zebras.64 We also try to review 2. W e separately analyzed botnet-
complete, we try to discuss our findings
findings with subject matter experts in related incidents.
with the relevant partner or partners so
the specific areas ahead of release.
Both subsets were separated the last as to validate it against their knowledge
six years as well. of the data.
Finally, we create some subsets to
help further our analysis. In particular,
a single subset is used for all analysis
within the DBIR unless otherwise
stated. It includes only quality incidents
as described above and excludes the
aforementioned two subsets.
64 A unique finding is more likely to be something mundane, such as a data collection issue,
than an unexpected result.
2023 DBIR Appendices 82

Appendix B:
VERIS mappings to
MITRE ATT&CK®
When it comes to sailing the stormy The results of that work are remarkable: The second version of this mapping
seas of the cybersecurity world, a map ATT&CK provides excellent tactical has just been released as of April 6,
comes in handy to help you chart your and technical details into the specific 2023, and we are very excited about
direction. We consider the DBIR to be techniques the threat actors leverage, it. In addition to VERIS Actions, a lot of
one of those maps, helping organizations while VERIS provides a strategic view of thought was put into mapping Attributes.
navigate the complicated and ever- the landscape, covering a wider range To make it better, Actors were mapped
changing conditions of the cybersecurity of possible mishaps. Errors, for instance, to ATT&CK Groups.68 There are also new
landscape. To make sure this map is the are present in 9% percent of breaches mappings to ATT&CK for Mobile and
most accurate possible, we have created this year but are out of scope in ATT&CK. ATT&CK for ICS.
the VERIS Framework,65 which captures When VERIS and ATT&CK are combined,
most of the important components of they provide you with a clearer view If this interests you at all, please hop over
data breaches in order to facilitate risk- of what type of assets were impacted to https://center-for-threat-informed-
oriented decision making for our weary and what type of victims those assets defense.github.io/attack_to_veris/
cyber mariners. belonged to while still preserving the for all the details of the work. Even if
specifics of the attack techniques that it doesn’t,69 you are already reaping
Over the years, new guiding frameworks were leveraged. the benefits of the work thanks to the
have been created that provide different ATT&CK Technique mappings we
levels of detail, MITRE ATT&CK® being This combination of forces is timely due have added to some select Incident
by far the most popular. We have worked to the increased regulatory pressure of Patterns to help you in your epic
with MITRE Engenuity and the Center for reporting data breaches to governments, journey to “full control coverage.”
Threat Informed Defense66 to capture the although there is no commonly accepted
relationships between VERIS to ATT&CK format in how this reporting should be Our team puts a lot of thought and
so that organizations can leverage the done. We, of course, cannot opine on energy into trying to make the VERIS
benefits of both in their navigation. the need for such regulations,67 but we Framework more accessible and helpful
would like to do our part to make sure for all. If you are curious about the
that organizations have the right tooling framework or have tried it in the past and
to reduce their burden as new laws come want to check what’s new, get in touch
to fruition. with the DBIR team at dbir@verizon.com.
65 https://verisframework.org/
66 https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/
67 Who are we kidding? We would love to have more data to analyze!
68 https://attack.mitre.org/groups/
69 How dare you?
2023 DBIR Appendices 83

Appendix C:
VTRAC 20-year
retrospective
I can still remember some of the first organizations across more than 100
By Chris Novak, data breaches I ever investigated. Old countries. We not only have several
Managing Director timers will appreciate the days when physical lab locations around the world
we showed up onsite with our “medical but also cloud-based and client on-
Cyber Security Consulting
bag” —typically a bag that had a binder premises lab locations to care for nearly
Verizon of bootable floppy disks, a collection of every conceivable data privacy and
assorted cables, and a variety of hard sovereignty concern.
drives and enclosures. As mentioned
above, hardly anyone knew what Of course, I cannot forget to mention the
It’s hard to believe that the Verizon
cybersecurity was back then, and the incredible work of the DBIR team that
Threat Research Advisory Center
average person had no idea of the makes this very publication possible.
(VTRAC) is 20 years old! I’ve had
purpose of the equipment in that medical Many have heard me say that the DBIR
the unique pleasure of being part of
bag. In a world just following 9/11, going is my third child. It was born 16 years
the team since the very beginning—
through airport security with that bag ago as part of an early incarnation of
or should I say the “zero-day”?
of odd-looking electronics and cables VTRAC (back then we were called the
Over those 20 years, we’ve had a few guaranteed that I was frequently the RISK Team) with a vision of sharing our
different names but always the same lucky winner of “random” extra screening. data breach insights with the world.
passionate team behind the scenes. If only that luck carried over into a few of Metaphorically, I heard it say its first
Back then, I was part of a small gaggle the trips to Vegas … words and watched it take its first
steps alongside the other co-creators.
of geeks in New York City, always
Today, we rarely need to travel. We Thankfully, I don’t have to save for the
having a suitcase packed and ready
have enterprise tools that can facilitate DBIR’s college tuition.70
to hop a flight to anywhere to take on
remote forensic evidence collection
the next big data breach investigation.
from anywhere in the world. Taking I couldn’t be prouder of what the past and
Our forensic lab at the time was a
advantage of our telecommunications present members of the VTRAC have
collection of systems that didn’t even
backbone and advances in cellular built and accomplished over the past 20
fill a single full-height server rack.
connectivity, we’re even able to provide years. It is the passion and dedication
It bears reminding that, 20 years ago, immediate emergency and out-of-band of each and every team member that
“cybersecurity” was not a commonly communications via 5G, allowing us to contributes to our long client tenure,
used or understood word. If you asked collect forensic data at speeds in excess never having missed a contractual
the average person what “cyber” was, of 1 Gbps, even if the victim organization service level agreement, world-class
you would probably get back responses has its own network, systems or thought leadership and consistent
that sounded like something from a infrastructure outages. rating as a leader by industry analysts.
science fiction movie. There was no such
The then and now comparisons over I look forward to the adventures,
thing as a cybersecurity college degree—
the last 20 years are staggering to innovation and excitement to come
the closest thing that existed at the time
consider. Today, we have exponentially in our next 20 years!
was a computer science or engineering
more people on our team, with incredible
degree. Today, there are hundreds of
Happy 20th birthday, VTRAC!
diversity of backgrounds and geographic
universities around the world that not only
locations. The VTRAC supports
offer cybersecurity bachelor’s degrees, —Chris Novak
but also master’s degrees and Ph.D.s.
70 Editor’s note: We hope the DBIR is actually helping you pay for tuition for your human children.
2023 DBIR Appendices 84

Appendix D:
Contributing
organizations
| A   | CrowdStrike | F   |
| --- | ----------- | --- |
Akamai Technologies Cybersecurity and Infrastructure  Federal Bureau of Investigation –
Internet Crime Complaint Center
Security Agency (CISA)
Ankura
(FBI IC3)
CyberSecurity Malaysia, an agency
Apura Cyber Intelligence
|     | under the Ministry of Communications  | Fortinet |
| --- | ------------------------------------- | -------- |
and Multimedia (KKMM)
B
|     | Cybersixgill | G   |
| --- | ------------ | --- |
Bit-x-bit
|     | CYBIR | Global Resilience Federation |
| --- | ----- | ---------------------------- |
BitSight
GreyNoise
BlackBerry
D
|     | Dell  | H   |
| --- | ----- | --- |
C
|                              | Department of Government Services,    | HackEDU                                   |
| ---------------------------- | ------------------------------------- | ----------------------------------------- |
| Censys, Inc.                 | Victorian State Government, Australia |                                           |
| Center for Internet Security | DomainTools                           | I                                         |
| Cequence Security            |                                       | Irish Reporting and Information Security  |
|                              | E                                     | Service (IRISS-CERT)                      |
CERT Division of Carnegie Mellon
University’s Software Engineering  Energy Analytic Security Exchange  Ivanti
| Institute              | (EASE)              |            |
| ---------------------- | ------------------- | ---------- |
| CERT – European Union  | Edgescan            | J          |
| CERT Polska            | Elevate Security    | JPCERT/CC  |
| Check Point Software   | Emergence Insurance |            |
| Technologies Ltd.      |                     | K          |
EUROCONTROL
| Chubb |     | K-12 Security Information Exchange  |
| ----- | --- | ----------------------------------- |
Eviden
(K-12 SIX)
Coalition
Kaspersky
Computer Incident Response Center
| Luxembourg (CIRCL) |     | KordaMentha |
| ------------------ | --- | ----------- |
Coveware
2023 DBIR Appendices 85

L S
Legal Services Information Sharing and S21sec
Analysis Organization (LS-ISAO)
SecurityTrails, a Recorded
Future Company
M
Shadowserver Foundation
Malicious Streams
SISAP – Sistemas Aplicativos
Maritime Transportation System ISAC
Shodan
(MTS-ISAC)
Swisscom
mnemonic
U
N
U.S. Secret Service
NetDiligence®
NETSCOUT
V
VERIS Community Database
O
Verizon Cyber Risk Programs
Okta
Verizon Cyber Security Consulting
OpenText Cybersecurity
Verizon DDoS Defense
P Verizon Network Operations
and Engineering
Palo Alto Networks
Verizon Threat Research Advisory
Proofpoint
Center (VTRAC)
Vestige Digital Investigations
W
WatchGuard Technologies, Inc.
2023 DBIR Appendices 86

2023 DBIR Appendices 87

| Verizon Cyber  | Verizon Network  | Verizon Threat  |
| -------------- | ---------------- | --------------- |
Verizon Cyber  Verizon DDoS
| Security  | Operations and   | Research Advisory  |
| --------- | ---------------- | ------------------ |
Risk Programs Defense
| Consulting | Engineering | Center (VTRAC) |
| ---------- | ----------- | -------------- |
2023 DBIR Appendices 88

© 2023 Verizon. OGWP1950623

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-11-14", "model": "gemini-3.8-flash"} -->
