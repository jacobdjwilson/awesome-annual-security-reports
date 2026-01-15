# DBIR

## 2023 Data Breach Investigations Report

---

## About the cover

The magnifier on the cover is intended to visually convey the effort the team made to refocus our energy and resources more on our core breach dataset. The graph that is magnified is simply a cumulative count of the number of breaches in our dataset as the years have gone by since our first report. Long-time readers may notice the Vocabulary for Event Recording and Incident Sharing (VERIS) Framework trademark honeycombs, which are meant to convey the 4As (Actor, Action, Asset, Attribute) and their various enumerations.

![Graph showing cumulative number of breaches over the years, with a magnifier focusing on a section. The magnifier also shows VERIS framework honeycombs.](Image description)

---

## Table of contents

*   [Helpful definitions and chart guidance](#helpful-definitions-and-chart-guidance)
*   [Introduction](#introduction)
*   [Summary of findings](#summary-of-findings)
*   [Results and analysis](#results-and-analysis)
    *   [Introduction](#introduction-1)
    *   [Actors](#actors)
    *   [Actions](#actions)
    *   [Assets](#assets)
    *   [Attributes](#attributes)
*   [Incident Classification Patterns](#incident-classification-patterns)
    *   [Introduction](#introduction-2)
    *   [System Intrusion](#system-intrusion)
    *   [Social Engineering](#social-engineering)
    *   [Basic Web Application Attacks](#basic-web-application-attacks)
    *   [Miscellaneous Errors](#miscellaneous-errors)
    *   [Denial of Service](#denial-of-service)
    *   [Lost and Stolen Assets](#lost-and-stolen-assets)
    *   [Privilege Misuse](#privilege-misuse)
*   [Industries](#industries)
    *   [Introduction](#introduction-3)
    *   [Accommodation and Food Services](#accommodation-and-food-services)
    *   [Educational Services](#educational-services)
    *   [Financial and Insurance](#financial-and-insurance)
    *   [Healthcare](#healthcare)
    *   [Information](#information)
    *   [Manufacturing](#manufacturing)
    *   [Mining, Quarrying, and Oil & Gas Extraction + Utilities](#mining-quarrying-and-oil--gas-extraction--utilities)
    *   [Professional, Scientific and Technical Services](#professional-scientific-and-technical-services)
    *   [Public Administration](#public-administration)
    *   [Retail](#retail)
    *   [Small and medium business](#small-and-medium-business)
*   [Regions](#regions)
    *   [Introduction](#introduction-4)
*   [Wrap-up](#wrap-up)
*   [Year in review](#year-in-review)
*   [Appendices](#appendices)
    *   [Appendix A: Methodology](#appendix-a-methodology)
    *   [Appendix B: VERIS mappings to MITRE ATT&CK®](#appendix-b-veris-mappings-to-mitre-attack)
    *   [Appendix C: VTRAC 20-year retrospective](#appendix-c-vtrac-20-year-retrospective)
    *   [Appendix D: Contributing organizations](#appendix-d-contributing-organizations)

---

## Helpful definitions and chart guidance

Hello, and welcome first-time readers! Before you get started on the 2023 Data Breach Investigations Report (DBIR), it might be a good idea to take a look at this section first. (For those of you who are familiar with the report, please feel free to jump over to the introduction.) We have been doing this report for a while now, and we appreciate that the verbiage we use can be a bit obtuse at times. We use very deliberate naming conventions, terms and definitions and spend a lot of time making sure we are consistent throughout the report. Hopefully this section will help make all of those more familiar.

### VERIS Framework resources

The terms “threat actions,” “threat actors” and “varieties” will be referenced often. These are part of the Vocabulary for Event Recording and Incident Sharing (VERIS), a framework designed to allow for a consistent, unequivocal collection of security incident details. Here is how they should be interpreted:

*   **Threat actor**: Who is behind the event? This could be the external “bad guy” that launches a phishing campaign or an employee who leaves sensitive documents in their seat back pocket.
*   **Threat action**: What tactics (actions) were used to affect an asset? VERIS uses seven primary categories of threat actions: Malware, Hacking, Social, Misuse, Physical, Error and Environmental. Examples at a high level include hacking a server, installing malware or influencing human behavior through a social attack.
*   **Variety**: More specific enumerations of higher-level categories—e.g., classifying the external “bad guy” as an organized criminal group¹ or recording a hacking action as SQL injection or brute force.

Learn more here:

*   [https://github.com/vz-risk/dbir/tree/gh-pages/2023](https://github.com/vz-risk/dbir/tree/gh-pages/2023)—includes DBIR facts, figures and figure data
*   [https://verisframework.org](https://verisframework.org)—features information on the framework with examples and enumeration listings
*   [https://github.com/vz-risk/veris](https://github.com/vz-risk/veris)—features information on the framework with examples and enumeration listings

### Incident vs. breach

We talk a lot about incidents and breaches and we use the following definitions:

*   **Incident**: A security event that compromises the integrity, confidentiality or availability of an information asset.
*   **Breach**: An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party. A Distributed Denial of Service (DDoS) attack, for instance, is most often an incident rather than a breach, since no data is exfiltrated. That doesn’t make it any less serious.

### Industry labels

We align with the North American Industry Classification System (NAICS) standard to categorize the victim organizations in our corpus. The standard uses two- to six-digit codes to classify businesses and organizations. Our analysis is typically done at the two-digit level, and we will specify NAICS codes along with an industry label. For example, a chart with a label of Financial (52) is not indicative of 52 as a value. “52” is the NAICS code for the Financial and Insurance sector. The overall label of “Financial” is used for brevity within the figures. Detailed information on the codes and the classification system is available here:

[https://www.census.gov/naics/?58967?yearbck=2012](https://www.census.gov/naics/?58967?yearbck=2012)

¹ By organized criminal group, we mean a group that does this for a living and has a set process they use repeatedly, not Tony Soprano and his band of merry men.

---

### I’m sorry, this all happened when?

While we have always listed the following facts in our Methodology section (because that is where this type of information belongs), we decided to also mention it here for the benefit of those who don’t make it that far into the report. Each year, the DBIR timeline for in-scope incidents is from November 1 of one calendar year through October 31 of the next calendar year. Thus, the incidents described in this report took place between November 1, 2021, and October 31, 2022. The 2022 caseload is the primary analytical focus of the 2023 report, but the entire range of data is referenced throughout, notably in trending graphs. The time between the latter date and the date of publication for this report is spent in acquiring the data from our global contributors, anonymizing and aggregating that data, analyzing the dataset and, finally, creating the graphics and writing the report. Rome wasn’t built in a day, and neither is the DBIR.

### Being confident of our data

Starting in 2019 with slanted bar charts, the DBIR has tried to make the point that the only certain thing about information security is that nothing is certain. Even with all the data we have, we’ll never know anything with absolute certainty. However, instead of throwing our hands up and complaining that it is impossible to measure anything in a data-poor environment or, worse yet, just plain making stuff up, we get to work. This year, you’ll continue to see the team representing uncertainty throughout the report figures.

The examples shown in Figures 1, 2, 3 and 4 all convey the range of realities that could credibly be true. Whether it be the slant of the bar chart, the threads of the spaghetti chart, the dots of the dot plot or the color of the pictogram plot, all convey the uncertainty of our industry in their own special way.

Much like the slanted bar chart, the spaghetti chart represents the same concept: the possible values that exist within the confidence interval; however, it’s slightly more involved because we have the added element of time. The individual threads represent a sample of all possible connections between the points that exists within each observation’s confidence interval. As you can see, some of the threads are looser than others, indicating a wider confidence internal and a smaller sample size.

![Example slanted bar chart showing uncertainty with slanted areas.](Image description)
Figure 1. Example slanted bar chart (n=205)

The slanted bar chart will be familiar to returning readers. The slant on the bar chart represents the uncertainty of that data point to a 95% confidence level (which is standard for statistical testing).

In layman’s terms, if the slanted areas of two (or more) bars overlap, you can’t really say one is bigger than the other without angering the math gods.

![Example spaghetti chart showing multiple threads representing possible connections over time.](Image description)
Figure 2. Example spaghetti chart

The dot plot is another returning champion, and the trick to understanding this chart is to remember that the dots represent organizations. If, for instance, there are 200 dots (like in Figure 3), each dot represents 0.5% of organizations. This is a much better way of understanding how something is distributed among organizations and provides considerably more information than an average or a median. We added more colors and callouts to those in an attempt to make them even more informative.

The pictogram plot, our relative newcomer, attempts to capture uncertainty in a similar way to slanted bar charts but is more suited for a single proportion.

We hope they make your journey through this complex dataset even smoother than previous years.

![Example dot plot with dots representing organizations and color-coded confidence intervals.](Image description)
Figure 3. Example dot plot (n=672). Each dot represents 0.5% of organizations. Orange: lower half of 80%. Yellow: upper half of 80%. Green: 80%–95%. Blue: Outliers. 95% of orgs: 148–1,594,648. 80%: 1,274–438,499. Median: 29,774 (log scale).

![Example pictogram plot where each glyph represents a number of breaches.](Image description)
Figure 4. Example pictogram plot (n=4,110). Each glyph represents 40 breaches.

### Credit where credit is due

Turns out folks enjoy citing the report, and we often get asked how they should go about doing it.

You are permitted to include statistics, figures and other information from the report, provided that (a) you cite the source as “Verizon 2023 Data Breach Investigations Report” and (b) content is not modified in any way. Exact quotes are permitted, but paraphrasing requires review. If you would like to provide people a copy of the report, we ask that you provide them a link to verizon.com/dbir rather than a copy of the PDF.

### Questions? Comments? Organizing a bank run?

Let us know! Drop us a line at dbir@verizon.com, find us on LinkedIn, tweet @VerizonBusiness with #dbir. Got a data question? Tweet @VZDBIR!

If you are interested in becoming a contributor to the annual Verizon DBIR (and we hope you are), the process is very easy and straightforward. Please email us at dbircontributor@verizon.com.

---

## Introduction

“Success is stumbling from failure to failure with no loss of enthusiasm.”
—attributed to Sir Winston Churchill

Hello and welcome old friends and new readers to the 2023 Verizon Data Breach Investigations Report! We are happy to have you join us once again as we take a look at the sordid underbelly of cybercrime and see what lessons we may collectively learn from doing so. It often seems that with every new defense strategy, appliance or Please-Save-Us-As-A-Service we create, buy or borrow, our adversaries are just as quick to adapt and find a new vantage point from which to attack. While this state of affairs is already unfortunate enough, it becomes worse still when we do not even require them to evolve their tactics because the old ones still work just fine.

Regardless of where we fall on the crazy-secure to not-so-secure spectrum, the quote above is a good road map to cybersecurity (and life in general). This report aims to take a look at the times when things did not work as intended—not to point fingers but to help us all learn and improve. In a time where almost everyone, corporations and individuals alike, is looking at ways to do more with less, we believe a close analysis of when our defenses failed can be very beneficial. While times of great change are always challenging, they often also prompt us to take stock of our situation and, if necessary, refocus both our viewpoint and our energies. Such is the case with the DBIR this year. As a team, we decided to take a step back toward the fundamental things that got us where we are, an intense focus on actual data breaches analyzed using our own VERIS Framework. And speaking of VERIS, one of the new goodies this refocusing brings is an even better mapping between VERIS and MITRE ATT&CK through a collaboration with MITRE Engenuity and the Center for Threat Informed Defense (CTID).² It also helps that our parent organization, the Verizon Threat Research Advisory Center (VTRAC)³, shared the most breaches ever for us to analyze. Did you know it is VTRAC’s 20th anniversary this year? Save us a slice of that cake, boss!

As long-time readers will know, over the past few years, we have increasingly utilized non-incident data to add depth and dimension to our breach findings via various forms of research and analysis. While that remains a big part of what we do, as mentioned above, we did take purposeful steps toward a more direct focus on the breach side of the house this year. In short, the result of this was to make the report more concise and succinct and less unwieldy. This year we analyzed 16,312 security incidents, of which 5,199 were confirmed data breaches. As always, we hope you find this information informative, useful, easy to understand and actionable.

Finally, we thank our global data contributors most sincerely, as this report would quite literally not be possible without them. Of course, the same can be said of our readers, so please accept our deep gratitude for your continued support.

Sincerely,

The Verizon DBIR Team
C. David Hylender, Philippe Langlois, Alex Pinto, Suzanne Widup

Very special thanks to:
*   Dave Kennedy and Erika Gifford from VTRAC.
*   Kate Kutchko, Marziyeh Khanouki and Yoni Fridman from the Verizon Business Product Data Science Team.
*   Gabriel Bassett for all the statistical tooling, charts and terrible jokes over the years. Good luck on your next adventure!

² [https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/](https://mitre-engenuity.org/cybersecurity/center-for-threat-informed-defense/)
³ [https://www.verizon.com/business/resources/reports/verizon-threat-research-advisory-center/](https://www.verizon.com/business/resources/reports/verizon-threat-research-advisory-center/)

---

## Summary of findings

![Graph showing pretexting incidents over time, with a clear upward trend.](Image description)
Figure 5. Pretexting incidents over time

Social Engineering attacks are often very effective and extremely lucrative for cybercriminals. Perhaps this is why Business Email Compromise (BEC) attacks (which are in essence pretexting attacks) have almost doubled across our entire incident dataset, as can be seen in Figure 5, and now represent more than 50% of incidents within the Social Engineering pattern.

74% of all breaches include the human element, with people being involved either via Error, Privilege Misuse, Use of stolen credentials or Social Engineering.

83% of breaches involved External actors, and the primary motivation for attacks continues to be overwhelmingly financially driven, at 95% of breaches.

The three primary ways in which attackers access an organization are stolen credentials, phishing and exploitation of vulnerabilities.

![Bar chart showing select key enumerations with percentages.](Image description)
Figure 6. Select key enumerations

![Bar chart showing select enumerations in non-Error, non-Misuse breaches.](Image description)
Figure 7. Select enumerations in non-Error, non-Misuse breaches (n=4,291)

![Line graph showing ransomware action variety over time, indicating a steady presence.](Image description)
Figure 8. Ransomware action variety over time

![Bar chart showing the percentage of Log4j scanning for 2022, with a significant spike early in the year.](Image description)
Figure 9. Percentage of Log4j scanning for 2022

Ransomware continues its reign as one of the top Action types present in breaches, and while it did not actually grow, it did hold statistically steady at 24%. Ransomware is ubiquitous among organizations of all sizes and in all industries.

More than 32% of all Log4j scanning activity over the course of the year happened within 30 days of its release (with the biggest spike of activity occurring within 17 days).

Log4j was so top-of-mind in our data contributors’ incident response that 90% of incidents with Exploit vuln as an action had “Log4j,” or “CVE-2021-44228” in the comments section. However, only 20.6% of the incidents had comments.

![Bar chart showing the percentage of identified Exploit vuln that was Log4j, with each glyph representing an incident.](Image description)
Figure 10. Percentage of identified Exploit vuln that was Log4j (n=81). Each glyph represents an incident.

---

## 2 Results and analysis

---

### Results and analysis: Introduction

Hello friends, and welcome to the “Results and analysis” section. This is where we cover the highlights we found in the data this year. This dataset is collected from a variety of sources, including our own VTRAC investigators, reports provided by our data contributors and publicly disclosed security incidents.

Since data contributors come and go, one of our priorities is to make sure we can get broad representation on different types of security incidents and the countries where they occur. This ebb and flow of contributors obviously influences our dataset, and we will do our best to provide context on those potential biases where applicable.

As some of you may have noticed⁴ over the years, the incident data collection we do is based on the VERIS Framework. It has been the bedrock upon which our multiyear dataset has been built and is what allows us to be able to speak with confidence when trends in the attack landscape surface. Our dataset currently contains 953,894 incidents, of which 254,968 are confirmed breaches, and we can’t wait to celebrate⁵ with you when we reach 1 million⁶ incidents!

In VERIS, the core categories we use to describe an incident are called the 4As: Actor (who), Action (how), Asset (where) and Attribute (what). An incident needs all these four to be “complete,” even if at the end of the day some of those are unknown to the parties investigating the incident. Keep an eye out for our instructive callouts in each of those sub-sections giving more context on our VERIS categories.

Let’s go over the results for each one of these.

⁴ We certainly won’t shut up about it.
⁵ Not sure if we should be celebrating security incidents, but everyone loves a round number.
⁶ Here’s hoping being a millionaire doesn’t get to our dataset’s head, and they decide to join the “Great Resignation” and retire in some tropical tax haven.

---

### Actors

Life can be scary and unpredictable, which is why we like to start our results discussion with the cozy and familiar Actor analysis. It really is true, as they say, that the only certainties in life are death, taxes and External actors.⁷

As Figure 11 demonstrates, External actors were responsible for 83% of breaches, while Internal ones account for 19%. It is worth reminding our readers that Internal actors are not only responsible for intentional harm in these cases, but they are also just as likely⁸ to be responsible for Error actions. Regardless, the clear frequency of External actors as instigators of breaches is a datapoint that has held steady ever since we started this gig.

![Pie chart showing threat actors in breaches, with External actors dominating.](Image description)
Figure 11. Threat actors in breaches (n=5,177)

#### Actor categories⁹

*   **External**: External threats originate from sources outside of the organization and its network of partners. Examples include criminal groups, lone hackers, former employees and government entities. This category also includes God (as in “acts of”), “Mother Nature” and random chance. Typically, no trust or privilege is implied for external entities.
*   **Internal**: Internal threats are those originating from within the organization. This encompasses company full-time employees, independent contractors, interns and other staff. Insiders are trusted and privileged (some more than others).
*   **Partner**: Partners include any third party sharing a business relationship with the organization. This includes suppliers, vendors, hosting providers and outsourced IT support. Some level of trust and privilege is usually implied between business partners. Note that an attacker could use a partner as a vector, but that does not make the partner the Actor in this case. The partner has to initiate the incident.

⁷ That’s what they say, right?
⁸ OK, actually twice as likely.
⁹ [https://verisframework.org/actors.html](https://verisframework.org/actors.html)

Long-time readers of the report will be similarly shocked to learn that Financial motives still drive the vast majority of breaches (Figure 12), showing growth in relation to last year with a whopping 94.6% representation in breaches. If we look inside to see which external actors are the hardest working, the top performer is Organized crime (Figure 13).

What is most interesting in Figure 13, however, is realizing that the internal variety of End-user shows up more often than the external variety State-sponsored attackers.¹⁰ Those organization employees are mostly involved in Misuse (read, internal malicious activity) and Errors (accidents), which suggests where we should be paying more attention on our day-to-day security management.

This is relevant because we were expecting some increased activity in State-sponsored attacks, be it Espionage-related or not, due to the ongoing conflict in Ukraine. Even with anecdotal evidence of increased ideology or hacktivism-related attacks stemming from the geopolitical discussion, it really isn’t making a dent in larger statistical terms. It is also worth noting that this kind of activity would also be unlikely to disrupt our average reader’s organization.¹¹

![Pie chart showing threat actor Motives in breaches.](Image description)
Figure 12. Threat actor Motives in breaches (n=2,328)

![Bar chart showing threat actor Varieties in breaches.](Image description)
Figure 13. Threat actor Varieties in breaches (n=2,489)

¹⁰ Huge win for anarchists and other state-abolishing ideologies, if you ask us.
¹¹ No, Mr. Bond, MI6 does not represent our average reader.

---

### Actions

Action, as the name would imply, is what brings dynamism to our report. What dastardly deeds have the threat actors been up to? If you replied “ransomware,” we’d say you have no imagination, but you would also be right. This pesky Malware variety has been holding our talking points hostage for years now, and we can’t scrounge up enough cryptocurrency to pay the ransom!

Figures 14, 15, 16 and 17 describe the top Action varieties (what happened in more detail) and vectors (how those actions came to pass).

#### Action categories¹²

*   **Hacking (hak)**: attempts to intentionally access or harm information assets without (or exceeding) authorization by circumventing or thwarting logical security mechanisms.
*   **Malware (mal)**: any malicious software, script or code run on a device that alters its state or function without the owner’s informed consent.
*   **Error (err)**: anything done (or left undone) incorrectly or inadvertently.
*   **Social (soc)**: employ deception, manipulation, intimidation, etc., to exploit the human element, or users, of information assets.
*   **Misuse (mis)**: use of entrusted organizational resources or privileges for any purpose or manner contrary to that which was intended.
*   **Physical (phy)**: deliberate threats that involve proximity, possession or force.
*   **Environmental (env)**: not only includes natural events such as earthquakes and floods but also hazards associated with the immediate environment or infrastructure in which assets are located.

![Bar chart showing top Action varieties in breaches.](Image description)
Figure 14. Top Action varieties in breaches (n=4,354)

![Bar chart showing top Action varieties in incidents.](Image description)
Figure 15. Top Action varieties in incidents (n=14,829)

![Bar chart showing top Action vectors in breaches.](Image description)
Figure 16. Top Action vectors in breaches (n=3,194)

![Bar chart showing top Action vectors in incidents.](Image description)
Figure 17. Top Action vectors in incidents (n=10,502)

¹² [https://verisframework.org/actions.html](https://verisframework.org/actions.html)

As expected, the charts are led by either first-stage or single-stage attacks, namely Use of stolen creds for breaches and Denial of Service for incidents. This is consistent with previous years. What is concerning, if unsurprising, is having Ransomware take over the second spot in incidents, now being present in 15.5% of all incidents. Meanwhile, the share of Ransomware did not grow in breaches and held steady (statistically, at least) at 24%. You can see the evolution of both in Figure 18.

That almost a quarter of breaches involve a Ransomware step continues to be a staggering result. However, we had been anticipating that Ransomware would soon be hitting its theoretical ceiling, by which we mean that all the incidents that could have Ransomware, would have. Ransomware is present today in more than 62% of all incidents committed by Organized crime actors and in 59% of all incidents with a Financial motivation, so sadly there is still some room for growth.

Eagle-eyed readers will notice the absence of Partner and Software update as action vectors for incidents this year, in contrast to last year’s “software supply chainpocalypse.”¹³ Instead, our collective Christmas was ruined by another Ghost of Technical Debt Past: the Log4j vulnerability popularly known as CVE-2021-44228.¹⁴

We will be spending some time digging into the Log4j vulnerability in the “System Intrusion” section, but it is worth noting that the presence of the Exploit vuln action has kept stable in incidents and is actually less prominent in breaches, dropping from 7% to 5%. So, did the collective security industry sacrifice its holidays for nothing?

![Line graph showing ransomware action variety over time.](Image description)
Figure 18. Ransomware action variety over time

Not quite. This is one of those cases where the alternatives are just more popular. Use of stolen creds, our current champion, increased its share from 41.6% to 44.7%, which more than accounts for the drop in Exploit vuln.

More importantly, there was swift action from the community to spread awareness and patch all the different systems that had Log4j as a component. That surely helped avert a bigger disaster, so our success makes it look like it wasn’t a big deal after all.¹⁵ In fact, Log4j was so top-of-mind in our data contributors’ incident response that 90% of incidents with Exploit vuln as an action had “Log4j,” or “CVE-2021-44228” in the comments section. Granted, only 20.6% of the incidents had comments at all,¹⁶ so even if it can’t fully represent the whole dataset, it certainly speaks to how significant the vulnerability was in late 2021 and early 2022 for the incident response teams.

Finally, before I lose your attention, we should touch base on Loss.¹⁷ This action variety describes losing a physical device or media by accident and is often paired with the Carelessness action vector. It did show up fairly high in incidents. This is often because the data could not be confirmed as having been accessed and was therefore considered at risk rather than a breach. It is worth pointing out though that those were mostly concentrated in the data from some of our public sector contributors, where this sort of event is more tightly reported. Regardless, we know everyone was super excited about leaving the house again as the pandemic waned, but please keep an eye on your stuff when you go work from the coffee shop.

¹³ Wouldn’t you know, the moment we mention anything has not had relevance in our dataset, something new happens to remind us that change is the only constant. Best of luck for the teams responding to the 3CX supply-chain breach in late March 2023 as we close out this section. Make sure to keep copious notes so we can talk about it in a future edition of the report.
¹⁴ Just rolls off the tongue, doesn’t it?
¹⁵ Who here was working on the Y2K bug? Don’t forget to schedule your shingles vaccine!
¹⁶ In everyone’s defense, most of the data sharing happening here is machine-to-machine. Long gone are the days of artisanal, bespoke, VERIS-coded incidents for most of our contributors.
¹⁷ For the extremely online folks, we apologize for the psychic damage.

---

### Assets

In case you just wandered out of an Accounting 101 class, our Assets are more than the numbers that you list on the left side of your balance sheet.¹⁸ They encompass the entities that can be affected in an incident or breach and end up being manipulated by the threat actors for their nefarious goals. The callout box describes some of the most common top-level Assets in VERIS and some of the most common attack patterns that target them.

Figure 19 has the breakdown of varieties of Assets affected in breaches, and the results are pretty much what would be expected given the focus of System Intrusion, Basic Web Application Attacks and Social Engineering as the top attack patterns this year.

We can see a small fluctuation on the top three, as slightly less Servers were affected and slightly more User devices, but this order has held true for at least a couple of years, ever since Person overtook the second spot. Don’t forget that in VERIS, people are assets too,¹⁹ and they are the “where” that is affected by social threat actions.

![Bar chart showing Assets in breaches.](Image description)
Figure 19. Assets in breaches (n=4,433)

#### Asset categories²⁰

*   **Server (srv)**: a device that performs functions of some sort supporting the organization, commonly without end-user interaction. Where all the web applications, mail services, file servers and all that magical layer of information is generated. If someone has ever told you “the system is down,” rest assured that some Servers had their Availability impacted. Servers are common targets in almost all of the attack patterns, but especially in our System Intrusion, Basic Web Application Attacks, Miscellaneous Errors and Denial of Service patterns.
*   **Person (per)**: the folks (hopefully) doing the work at the organization. No AI chat allowed. Different types of Person will be members of different departments and will have associated permissions and access in the organization stemming from this role. At the very least they will have access to their very own User device and their own hopes and dreams for the future. Person is a common target in the Social Engineering pattern.
*   **User device (usr)**: the devices used by Persons to perform their work duties in the organizations. Usually manifested in the form of laptops, desktops, mobile phones and tablets. Common target in the System Intrusion pattern but also in the Lost and Stolen Asset pattern. People do like to take their little computers everywhere.
*   **Network (net)**: not the concept, but the actual network computing devices that make the bits go around the world, such as routers, telephone and broadband equipment, and some of the traditional in-line network security devices, such as firewalls and intrusion detection systems. Hey, Verizon is a Telecommunications company, OK?
*   **Media (med)**: precious diluted data in its most pure and crystalline form. Just kidding, mostly thumb drives and actual printed documents. You will see the odd full disk drive and actual physical payment cards from time to time, but those are more rare. Common in the Lost and Stolen Assets pattern.

¹⁸ However, not caring for them properly could cause liabilities that would go on the right side.
¹⁹ Just ask your organization’s HR department.
²⁰ [https://verisframework.org/assets.html](https://verisframework.org/assets.html)

For those keeping track, we had a 3.4% showing of OT assets in breaches that declared their impact. In summary—keep your attention level high, given the potential impact when those systems are affected, but either those numbers are very low overall, or they just don’t make it to our contributors’ dataset due to national²² security concerns.

Breaking the Asset varieties down further in Figure 20 showcases Web application and Mail servers on top, as would be expected, but it is interesting to see Person - Finance trending up from last year as we see a related growth in Pretexting social actions. We will be discussing those, and more specifically BECs, in the “Social Engineering” section of this report.

As a parting note, we continue to see very small numbers of incidents involving Operational Technology (OT), where the computers interface with heavy machinery and critical infrastructure, as contrasted with incidents involving Information Technology (IT), where we keep our cat pictures and internet memes. Industries like Manufacturing and Mining, Quarrying and Oil & Gas Extraction + Utilities²¹ continue to be relatively well-represented in our dataset, but reports of actual impact on OT devices are still too few for us to meaningfully write about in this report.

![Bar chart showing top Asset varieties in breaches.](Image description)
Figure 20. Top Asset varieties in breaches (n=3,207)

²¹ We know, it’s a mouthful.
²² From any country really.

---

### Attributes

The next time you meet an incident responder in the wild, know that all that goes through their mind is, “Did the asset or a copy of the data get out the door” (Confidentiality), “was it changed from a known and trusted state” (Integrity) and “do we still have access to it ourselves?” (Availability). Please offer them a word of kindness and a beverage, because it is a very tortured existence. If you are feeling cold, they are cold too.

One of the most interesting Attribute varieties we track year over year is the Confidentiality data varieties (Figure 21), or what kinds of data got out in a breach. Personal data represents Personally Identifiable Information (PII) from your customers, partners or employees, and it is the one that usually gets companies the most in trouble with regulators, as more and more privacy-related laws are passed around the world (although Medical data is a whole other ball of earwax).

#### Virtual money, real problems

When VERIS describes Attributes, it is directly referencing the CIA triad in information security (InfoSec): Confidentiality, Integrity and Availability. It’s a tried-and-true method of understanding the potential impact of an incident by describing what properties of the asset were potentially affected.

#### Attribute categories²³

*   **Confidentiality (cp)**: refers to limited