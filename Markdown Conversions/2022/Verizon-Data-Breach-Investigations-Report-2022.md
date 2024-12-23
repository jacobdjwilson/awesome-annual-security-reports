# DBIR
Data Breach Investigations Report
2008
2022
## About the 2022 cover
Our long-time readers may recall that the cover for our inaugural report back in 2008 depicted an empty chair in a server room. It was intended to convey the fact that many organizations are not properly minding their assets and data. The 2022 cover is a throwback to that report both for purposes of nostalgia and to convey that many organizations continue to struggle with keeping an eye on their people and their systems. The overlay of the timeline with the dot plot illustrates the number of global contributors that have joined us over the 15-year history of the report (broken out by year).
3
## Table of Contents
- [DBIR Master’s Guide](#dbir-masters-guide)
- [Introduction](#introduction)
- [Summary of findings](#summary-of-findings)
- [Results and Analysis](#results-and-analysis)
  - [Introduction](#results-and-analysis-introduction)
  - [Actor](#actor)
  - [Actions](#actions)
  - [Assets](#assets)
  - [Attribute](#attribute)
  - [Timeline](#timeline)
- [Incident Classification Patterns](#incident-classification-patterns)
  - [Introduction](#incident-classification-patterns-introduction)
  - [System Intrusion](#system-intrusion)
  - [Scratching the Surface](#scratching-the-surface)
  - [Social Engineering](#social-engineering)
  - [Basic Web Application Attacks](#basic-web-application-attacks)
  - [Miscellaneous Errors](#miscellaneous-errors)
  - [Denial of Service](#denial-of-service)
  - [Lost and Stolen Assets](#lost-and-stolen-assets)
  - [Organic Free-Range Data](#organic-free-range-data)
- [Industries](#industries)
  - [Introduction](#industries-introduction)
  - [Accommodation and Food Services](#accommodation-and-food-services)
  - [Arts, Entertainment and Recreation](#arts-entertainment-and-recreation)
  - [Educational Services](#educational-services)
  - [Financial and Insurance](#financial-and-insurance)
  - [Healthcare](#healthcare)
  - [Information](#information)
  - [Manufacturing](#manufacturing)
  - [Mining, Quarrying, and Oil & Gas Extraction + Utilities](#mining-quarrying-and-oil-gas-extraction--utilities)
  - [Professional, Scientific and Technical Services](#professional-scientific-and-technical-services)
  - [Public Administration](#public-administration)
  - [Retail](#retail)
  - [Very Small Business](#very-small-business)
- [Regions](#regions)
  - [Introduction](#introduction-to-regions)
  - [Asia Pacific (APAC)](#asia-pacific-apac)
  - [Europe, Middle East and Africa (EMEA)](#europe-middle-east-and-africa-emea)
  - [Northern America (NA)](#northern-america-na)
  - [Latin America and the Caribbean](#latin-america-and-the-caribbean)
- [Wrap-up](#wrap-up)
  - [Year in review](#year-in-review)
- [Appendices](#appendices)
  - [Appendix A: Methodology](#appendix-a-methodology)
  - [Appendix B: VERIS and Standards](#appendix-b-veris-and-standards)
  - [Appendix C: Changing Behavior](#appendix-c-changing-behavior)
  - [Appendix D: U.S. Secret Service](#appendix-d-us-secret-service)
  - [Appendix E: Ransomware Pays](#appendix-e-ransomware-pays)
  - [Appendix F: Contributing Organizations](#appendix-f-contributing-organizations)

Table of contents
1
2022 DBIR  Table of contents
01
4
# DBIR Master’s Guide
Hello, and welcome first-time readers! Before you get started on the 2022 Data Breach Investigations Report (DBIR), it might be a good idea to take a look at this section first. (For those of you who are familiar with the report, please feel free to jump over to the introduction). We have been doing this report for a while now, and we appreciate that the verbiage we use can be a bit obtuse at times. We use very deliberate naming conventions, terms and definitions and spend a lot of time making sure we are consistent throughout the report. Hopefully this section will help make all of those more familiar.
## VERIS resources
The terms “threat actions,” “threat actors” and “varieties” will be referenced often. These are part of the Vocabulary for Event Recording and Incident Sharing (VERIS), a framework designed to allow for a consistent, unequivocal collection of security incident details. Here is how they should be interpreted:
**Threat actor**: Who is behind the event? This could be the external “bad guy” that launches a phishing campaign or an employee who leaves sensitive documents in their seat back pocket.
**Threat action**: What tactics (actions) were used to affect an asset? VERIS uses seven primary categories of threat actions: Malware, Hacking, Social, Misuse, Physical, Error and Environmental. Examples at a high level are hacking a server, installing malware, or influencing human behavior through a social attack.
**Variety**: More specific enumerations of higher-level categories—e.g., classifying the external “bad guy” as an organized criminal group or recording a hacking action as SQL injection or brute force.
Learn more here:
- github.com/vz-risk/dbir/tree/gh-pages/2022 – DBIR facts, figures and figure data.
- veriscommunity.net features information on the framework with examples and enumeration listings.
- github.com/vz-risk/veris features information on the framework with examples and enumeration listings
## Incident vs. breach
We talk a lot about incidents and breaches and we use the following definitions:
**Incident**: A security event that compromises the integrity, confidentiality or availability of an information asset.
**Breach**: An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party.
## Industry labels
We align with the North American Industry Classification System (NAICS) standard to categorize the victim organizations in our corpus. The standard uses two- to six-digit codes to classify businesses and organizations. Our analysis is typically done at the two-digit level and we will specify NAICS codes along with an industry label. For example, a chart with a label of Financial (52) is not indicative of 52 as a value. “52” is the NAICS code for the Finance and Insurance sector. The overall label of “Financial” is used for brevity within the figures. Detailed information on the codes and the classification system are available here: https://www.census.gov/naics/?58967?yearbck=2012
2022 DBIR  Master’s Guide
5
## Questions? Comments?
Let us know! Drop us a line at dbir@verizon.com, find us on LinkedIn, tweet @VerizonBusiness with #dbir. Got a data question? Tweet @VZDBIR!
In layman’s terms, if the slanted areas of two (or more) bars overlap, you can’t really say one is bigger than the other without angering the math gods.
The dot plot is another returning champion, and the trick to understanding this chart is to remember that the dots represent organizations. If, for instance, there are 200 dots (like in Figure 3), each dot represents 0.5% of organizations. This is a much better way of understanding how something is distributed among organizations, and provides considerably more information than an average or a median. We added more colors and callouts to those in an attempt to make them even more informative.
2022 DBIR  Master’s Guide
![Example slanted bar chart (n=205)](Figure 1. Example slanted bar chart (n=205))
Figure 1. Example slanted bar chart (n=205)
![Example spaghetti chart](Figure 2. Example spaghetti chart)
Figure 2. Example spaghetti chart
![Example dot plot (n=672). Each dot represents 0.5% of organizations. Orange: lower half of 80%. Yellow: upper half of 80%. Green: 80%-95%. Blue: Outliers. 95% of orgs: 148 - 1,594,648. 80%: 1,274 - 438,499. Median: 29,774 (log scale).](Figure 3. Example dot plot (n=672). Each dot represents 0.5% of organizations. Orange: lower half of 80%. Yellow: upper half of 80%. Green: 80%-95%. Blue: Outliers. 95% of orgs: 148 - 1,594,648. 80%: 1,274 - 438,499. Median: 29,774 (log scale).)
Figure 3. Example dot plot (n=672). Each dot represents 0.5% of organizations. Orange: lower half of 80%. Yellow: upper half of 80%. Green: 80%-95%. Blue: Outliers. 95% of orgs: 148 - 1,594,648. 80%: 1,274 - 438,499. Median: 29,774 (log scale).
![Example pictogram plot (n=4,110). Each glyph represents 40 breaches.](Figure 4. Example pictogram plot (n=4,110). Each glyph represents 40 breaches.)
Figure 4. Example pictogram plot (n=4,110). Each glyph represents 40 breaches.
Each glyph represents 40 breaches.
The Pictogram plot, our relative newcomer, attempts to capture uncertainty in a similar way to slanted bar charts but are more suited for a single proportion.
We hope they make your journey through this complex dataset even smoother than previous years.
PLEASE NOTE: While we have always listed the following facts in our Methodology section (because that is where this type of information belongs) we decided to also mention it here for the benefit of those who don’t make it that far into the report. Each year, the DBIR timeline for in-scope incidents is from Nov. 01 of one calendar year until Oct. 31, of the next calendar year. Thus, the incidents described in this report took place between Nov. 01, 2020 to Oct. 31, 2021. The 2021 caseload is the primary analytical focus of the 2022 report, but the entire range of data is referenced throughout, notably in trending graphs. The time between the latter date and the date of publication for this report is spent in acquiring the data from the 80 odd global contributors, anonymizing and aggregating that data, analyzing the dataset and, finally, creating the graphics and writing the report. Rome wasn’t built in a day, and neither is the DBIR.
## Being confident of our data
Starting in 2019 with slanted bar charts, the DBIR has tried to make the point that the only certain thing about information security is that nothing is certain. Even with all the data we have, we’ll never know anything with absolute certainty. However, instead of throwing our hands up and complaining that it is impossible to measure anything in a data-poor environment, or worse yet, just plain making stuff up, we get to work. This year, you’ll continue to see the team representing uncertainty throughout the report figures.
The examples shown in Figures 1, 2, 3 and 4 all convey the range of realities that could credibly be true. Whether it be the slant of the bar chart, the threads of the spaghetti chart, the dots of the dot plot or the color of the pictogram plot, all convey the uncertainty of our industry in their own special way.
The slanted bar chart will be familiar to returning readers. The slant on the bar chart represents the uncertainty of that data point to a 95% confidence level (which is standard for statistical testing).
6
# Introduction
Welcome to the 15th annual Verizon Data Breach Investigations Report! It is truly hard to believe that it has been 15 years since our inaugural installment of this document. Were we to indulge our imaginations with anthropomorphic comparisons, we might find this report having its braces removed, finally being able to get a driver’s permit, overusing sarcasm, perhaps becoming a bit goth and generally being unappreciative. But we won’t bother with all that. We will simply say THANK YOU! Thank you to our contributors for your continued willingness to share your data, insight and vast experience in a selfless effort to improve this industry. A huge thank you to our readers for sticking with us through this long and epic journey, for being the reason we work so hard to produce this report, and most of all, for keeping us from having to get real jobs.
The past few years have been overwhelming for all of us. Just when we think we have reached the uttermost limit of our ability to be surprised, the world throws us yet another curve ball. Honestly, at this point, we here on the team would not so much as blink if Sasquatch were elected Governor, if Area 51 opened a bed and breakfast, or if ransomware increased yet again. Spoiler alert – one of those things did, in fact, happen. (Congrats, Squatch! You deserve it.)
The past year has been extraordinary in a number of ways, but it was certainly memorable with regard to the murky world of cybercrime. From very well publicized critical infrastructure attacks to massive supply chain breaches, the financially motivated criminals and nefarious nation-state actors have rarely, if ever, come out swinging the way they did over the last 12 months. As always, we will examine what our data has to tell us about these and the other common action types used against enterprises. Also, in honor of the 15th edition of the DBIR, we will occasionally refer back to comments, charts and figures from previous editions of this report to see how far we, as an industry, have come, and how the threat landscape and the techniques threat actors utilize have changed. This year the DBIR team analyzed 23,896 security incidents, of which, 5,212 were confirmed data breaches.
With that in mind, let’s revisit the Introduction to the 2018 DBIR:
“The DBIR was created to provide a place for security practitioners to look for data-driven, real-world views on what commonly befalls companies with regard to cybercrime. That need to know what is happening and what we can do to protect ourselves is why the DBIR remains relevant over a decade later. We hope that as in years past, you will be able to use this report and the information it contains to increase your awareness of what tactics attackers are likely to use against organizations in your industry, as a tool to encourage executives to support much-needed security initiatives, and as a way to illustrate to employees the importance of security and how they can help.”
From that perspective, we are proud to say that nothing has changed, and we hope you both enjoy the report and find the information it contains useful. Thanks again, for everything.

The DBIR Team
Gabriel Bassett, C. David Hylender, Philippe Langlois, Alex Pinto, Suzanne Widup
Special thanks to Dave Kennedy of the Verizon Threat Research Advisory Center (VTRAC) for his continued support and yearly contribution to this report, and to the Verizon Sheriff Team for their invaluable assistance.
2022 DBIR  Introduction
7
![Partner vector in System Intrusion incidents (n=3,403) Each glyph represents 25 incidents.](Figure 7. Partner vector in System Intrusion incidents (n=3,403) Each glyph represents 25 incidents.)
Figure 7. Partner vector in System Intrusion incidents (n=3,403) Each glyph represents 25 incidents.
# Summary of findings
![Select enumerations in non-Error, non-Misuse breaches (n=4,250)](Figure 5. Select enumerations in non-Error, non-Misuse breaches (n=4,250))
Figure 5. Select enumerations in non-Error, non-Misuse breaches (n=4,250)
![Ransomware over time in breaches](Figure 6. Ransomware over time in breaches)
Figure 6. Ransomware over time in breaches
There are four key paths leading to your estate: Credentials, Phishing, Exploiting vulnerabilities and Botnets. These four pervade all areas of the DBIR, and no organization is safe without a plan to handle them all.
This year, Ransomware has continued its upward trend with an almost 13% increase–a rise as big as the last five years combined (for a total of 25% this year). It’s important to remember, Ransomware by itself is really just a model of monetizing an organization’s access. Blocking the four key paths mentioned above helps to block the most common routes Ransomware uses to invade your network.
2021 illustrated how one key supply chain breach can lead to wide ranging consequences. Supply chain was responsible for 62% of System Intrusion incidents this year. Unlike a Financially motivated actor, Nation-state threat actors may skip the breach and keep the access.
2022 DBIR  Summary of findings
8
![The human element in breaches (n=4,110) Each glyph represents 25 breaches.](Figure 9. The human element in breaches (n=4,110) Each glyph represents 25 breaches.)
Figure 9. The human element in breaches (n=4,110) Each glyph represents 25 breaches.
![Misconfiguration over time in breaches](Figure 8. Misconfiguration over time in breaches)
Figure 8. Misconfiguration over time in breaches
Error continues to be a dominant trend and is responsible for 13% of breaches. This finding is heavily influenced by misconfigured cloud storage. While this is the second year in a row that we have seen a slight leveling out for this pattern, the fallibility of employees should not be discounted.
The human element continues to drive breaches. This year 82% of breaches involved the human element. Whether it is the Use of stolen credentials, Phishing, Misuse, or simply an Error, people continue to play a very large role in incidents and breaches alike.
2022 DBIR  Summary of findings
# Results and Analysis
Results 
and Analysis
2
2008
2008
2022
10
# Results and Analysis: Introduction
Welcome to the DBIR 15-year reunion! Please grab a name tag, find some familiar faces, and reminisce about the good ole days back in 2008. Now, let’s catch everyone up on how we’ve changed over the years.
A picture may tell a thousand words, but so will a good figure. The charts we use in our report are the result of numerous iterative attempts to convey both the main story of the data, as well as the main constraints, which is a tricky[^1] proposition. Our dataset comes to us in a variety of formats and represents many different contributors—each of which come complete with their own particular nuances and biases. We realize that our data is not a ‘pure sample’ of the world of breaches and incidents (because such a thing does not exist). Nevertheless, we can still extract meaningful analysis.
You may already be familiar with the charts such as Figure 10 we used in the original DBIR, and while these bar charts are an excellent means of allowing for easy comparisons between a small set of things, they can also sometimes hide important information in their percentages. Therefore, in an effort to be more transparent with our readers regarding the level of ambiguity or uncertainty in our data, over time we have transitioned to slanted bar charts such as Figure 11, which captures both the comparison between the “things” and the range of values for those based on the confidence we have in the data. We’ve also applied the same notion to our line charts, instead of representing trends as singular lines based on the average, we plot a collection of lines within our confidence interval. The good news is that you can still convey the core message of “things change” but also provide an honest illustration of “these are the possible representations of those changes.”
After 15 years of this data breach journey, we find ourselves reminiscing about all the deadlines, failed cover ideas, and heated arguments that we encountered along the way. However, maybe the real treasure of our journey wasn’t all the fame, mega yachts, book deals and data breach analysis, but the friends we made over the years. Initially this report was based solely on Verizon data, but since then we have been joined by 87 partners and collaborators from across the globe who make this report possible. Due in large part to them, we have collected and analyzed in total over 914,547 incidents, 234,638 breaches and 8.9 TBs of cybersecurity data, to bring our readers the best possible analysis and results. Truly, we stand on the shoulders of giants. Without further ado, let’s take a dive into the analysis.
[^1]: It’s not just rhymes that are tricky to rock.
2022 DBIR  Results and Analysis
11
# Actor – Friends in low places
![Sources of Data Breaches (2008 DBIR Figure 3)](Figure 10. Sources of Data Breaches (2008 DBIR Figure 3))
Figure 10. Sources of Data Breaches (2008 DBIR Figure 3)
![Actors in breaches (n=5,146)](Figure 11. Actors in breaches (n=5,146))
Figure 11. Actors in breaches (n=5,146)
Some things haven’t changed since we first began publishing this report back in 2008 (For those of you who need context, the original iPhone had been released only one year prior). The 2008 cyber[^2] security world, with limited access to handheld wonder machines, held the belief that insider incidents outnumbered external ones, or at least felt it was “certainly true for the broad range of security incidents.” As we look back now, with the benefit (?) of 15 years of time-wasting apps, considerably more gray hair and a few chips off the collective Infosec shoulders, we can confidently state that External actors are consistently more common than Internal, with 80% of breaches being caused by those external to the organization, as seen in Figure 11.
> Our findings indicate that data compromises are considerably more likely to result from external attacks than from any other source. Nearly three out of four cases yielded evidence pointing outside the victim organization. In keeping with other studies revealing risks inherent to the extended enterprise, business partners were involved in 39 percent of the data breaches handled by our investigators. Internal sources accounted for the fewest number of incidents (18 percent), trailing those of external origin by a ratio of four to one.
>
> The relative infrequency of data breaches attributed to insiders may be surprising to some. It is widely believed and commonly reported that insider incidents outnumber those caused by other sources. While certainly true for the broad range of security incidents, our caseload showed otherwise for incidents resulting in data compromise. This finding, of course, should be considered in light of the fact that insiders are adept at keeping their activities secret. (2008 DBIR)
[^2]: Can you find all 145 “cyber” references in the DBIR this year? I bet you can’t…
2022 DBIR  Results and Analysis
12
In the 2008 report, the number of records breached was the metric of choice. Now that we are a bit further into the 21st century, the currency of impact is the metric du jour. Though records are still of interest, they are typically not viewed with the same level of importance as in past years. However, in 2008 the median internal breach nabbed 375,000 records; as you can see in Figure 13, this year it’s only 80,00. While it appears the number of records is decreasing, it is important to keep in mind that a number of changes have taken place both in this report and within the industry at large. Therefore, the change in record count could be reflective of the fact that there are now more ways for attackers to monetize data.
![Median Number of Records Compromised (2008 DBIR Figure 5)](Figure 12. Median Number of Records Compromised (2008 DBIR Figure 5))
Figure 12. Median Number of Records Compromised (2008 DBIR Figure 5)
![Records by Actor in breaches (n=54)](Figure 13. Records by Actor in breaches (n=54))
Figure 13. Records by Actor in breaches (n=54)
> The median size (as measured in the number of compromised records) for an insider breach exceeded that of an outsider by more than 10 to one. Likewise, incidents involving partners tend to be substantially larger than those caused by external sources. This supports the principle that privileged parties are able to do more damage to the organization than outsiders. (2008 DBIR)
2022 DBIR  Results and Analysis
13
![Motives in External actors by org size](Figure 15. Motives in External actors by org size)
Figure 15. Motives in External actors by org size
Motive, for the most part, was not an initial topic of analysis for the DBIR (although in 2008 we did consider it in the context of targeted vs opportunistic breaches). In 2010, we stated “Today’s cybercriminals are not hobbyists seeking knowledge or thrills; they are motivated by the illicit profits possible in online crime.” While that may seem obvious to today’s readers, it is important to remember that at that time the stereotypical “let me hack this site from my mom’s basement to impress my bros” type of activity was believed by many to account for a certain proportion of breaches. Regardless, the motive of the threat actor is important to understand in order to attempt to quantify how many of our troubles are caused by the illicit economy, personal vendettas or by accidental blunders.
Financial has been the top motive since we began to track it in 2015. However, that same year the rise of hacktivism (particularly leaks) accounted for many attacks. Espionage-related attacks were not even on the radar, but seven years later the world is a very different place. Espionage has taken the 2nd place spot for years, and hacktivism is, for the most part, simply an afterthought. Before we move on, however, it should be noted that while espionage has almost certainly increased over the last few years, the fact that it did not appear at all in 2015 was quite likely due to our contributors and general case load at the time.
![Motive in external agents by percent of breaches within external (2012 DBIR Figure 15)](Figure 14. Motive in external agents by percent of breaches within external (2012 DBIR Figure 15))
Figure 14. Motive in external agents by percent of breaches within external (2012 DBIR Figure 15)
> Bottom line: most data thieves are professional criminals deliberately trying to steal information they can turn into cash. Like we said—same ol’ story.
>
> It’s not the whole story, however, nor is it the most important one. The most significant change we saw in 2011 was the rise of “hacktivism” against larger organizations worldwide. The frequency and regularity of cases tied to activist groups that came through our doors in 2011 exceeded the number worked in all previous years combined (2015 DBIR).
2022 DBIR  Results and Analysis
14
# Actions
The Actions section tells the story of how the security incident or breach plays out. It’s a bit like a Hollywood action movie, only with a modest budget and there are no explosions or car chases. Nevertheless, in spite of the dearth of pyrotechnics, the actions that lead up to these breaches have a definite impact on their victims. Actions are discussed in the DBIR by variety (the type of action) and vector (through what means the action took place). Figure 16 through Figure 19 illustrate the varieties and vectors associated with incidents and breaches.
## Action Categories
**Hacking**: attempts to intentionally access or harm information assets without (or exceeding) authorization by circumventing or thwarting logical security mechanisms.
**Malware**: any malicious software, script, or code run on a device that alters its state or function without the owner’s informed consent.
**Error**: anything done (or left undone) incorrectly or inadvertently
**Social**: employ deception, manipulation, intimidation, etc., to exploit the human element, or users, of information assets.
**Misuse**: use of entrusted organizational resources or privileges for any purpose or manner contrary to that which was intended.
**Physical**: deliberate threats that involve proximity, possession, or force.
**Environmental**: not only includes natural events such as earthquakes and floods, but also hazards associated with the immediate environment or infrastructure in which assets are located.
![Top Action vectors in incidents (n=18,419)](Figure 16. Top Action vectors in incidents (n=18,419))
Figure 16. Top Action vectors in incidents (n=18,419)
![Top Action varieties in incidents (n=18,511)](Figure 17. Top Action varieties in incidents (n=18,511))
Figure 17. Top Action varieties in incidents (n=18,511)
2022 DBIR  Results and Analysis
PLEASE NOTE: That Backdoors provide a direct access point for human operators while C2s are indirect connections used by malware. “Backdoor or C2” contains both Backdoors and C2 provided only by malware, while “Backdoor” covers both backdoors provided by malware and backdoors provided by hacking. Because neither is a subset of the other, we keep them both. As a reader, your takeaway should be that remote access established by the attacker is important and that there are a slew of ways of creating that persistent access.
15
The Denial of Service (DoS) action is the clear leader, representing 46% of total incidents, followed by the malware types of Backdoor or C2 at 17%. However, a much more interesting finding is the inclusion of Partner and Software update among the top vectors this year. This is a first for Software update, and is something we will discuss in greater detail in a subsequent section. Web application is the number one vector, and, not surprisingly, is connected to the high number of DoS attacks. This pairing, along with the Use of stolen credentials (commonly targeting some form of Web application), is consistent with what we’ve seen for the past few years.
Turning to breaches, the top varieties are a bit more dynamic, with Use of stolen credentials, Ransomware and Phishing all in the top five. The category of “Other” has stealthily crept into one of the top three spots this year as well. This is largely due to the dataset being long “tailed” and diverse. In other words, there are a lot of different things that aren’t in the top 10, but are still noteworthy. We can also flip that on its head and state that 73% of breach varieties are found in the top 10 varieties. Not too shabby considering the fact that we have more than 180 different action varieties. How’s that for the Pareto principle?[^3]
In terms of vectors, these align well with the notion that the main ways in which your business is exposed to the internet are the main ways that your business is exposed to the bad guys. Web application and Email are the top two vectors for breaches.
This is followed by Carelessness, which is associated with Errors such as Misdelivery and Misconfiguration. Next we have Desktop Sharing Software, which captures things like Remote Desktop Protocol (RDP) and third-party software that allows users to remotely access another computer via the Internet. Unfortunately, if you can access the asset directly over the internet simply by entering the credentials, so can the criminals.
[^3]: Not to be confused with the Peter Principle, which is something else entirely.
![Top Action vectors in breaches (n=3,279)](Figure 18. Top Action vectors in breaches (n=3,279))
Figure 18. Top Action vectors in breaches (n=3,279)
![Top Action varieties in breaches (n=3,875)](Figure 19. Top Action varieties in breaches (n=3,875))
Figure 19. Top Action varieties in breaches (n=3,875)
2022 DBIR  Results and Analysis
16
![Threat Categories (2008 DBIR Figure 9) Dark = Caused, Light = Contributed](Figure 20. Threat Categories (2008 DBIR Figure 9) Dark = Caused, Light = Contributed)
Figure 20. Threat Categories (2008 DBIR Figure 9)
Dark = Caused, Light = Contributed
![Actions in breaches (n=5,212)](Figure 21. Actions in breaches (n=5,212))
Figure 21. Actions in breaches (n=5,212)
## ’08 Throwback
While the DBIR has grown and evolved dramatically since its inception, we find it incredibly interesting how many of the core stats remain the same. In Figure 20 from 2008, you’ll find that the numbers are eerily similar to what we see today. Hacking continues to be the main action, followed by Malcode (Malware). In the 2008 report, Error was recorded in two ways: Errors that directly caused the breach (the dark bar) and Errors that contributed to the breach (light colored bar). We no longer use this breakdown (for a few reasons, one of which is that it can be argued that errors play at least a small part in almost all breaches), but Error accounts for 14% of breaches overall. From there, however, things begin to deviate slightly. This is particularly true with regard to Social and Error, but please keep in mind that our data has grown both in size and diversity of source over the years, expanding from 500 breaches that first year to over 5,000 breaches this year.
2022 DBIR  Results and Analysis
17
# Assets
For those not “in the know” about VERIS, (but if you are, that’s awesome!) Assets are the THING that the Action happens to. So, this is where you find WHAT was hacked via an exploit (probably a server), WHO was socially engineered by an attacker or WHAT was lost or stolen.[^4] For the staunch defenders, this should help you understand what is being targeted and also be a useful tool to start prioritizing what type of coverage your infrastructure needs.
Figure 22 illustrates that the top varieties of Assets impacted in breaches are Servers, People and their devices. When we start to zoom into the specific types of servers (Figure 24) we find Web application (56%) and Mail (28%) servers accounting for the top two varieties, which is rather intuitive when one considers that email servers and web applications are the Assets that are most likely to be internet-facing. As such, they provide a useful venue for attackers
[^4]: We feel a Schoolhouse Rock song coming on.
![Assets in breaches (n=4,384)](Figure 22. Assets in breaches (n=4,384))
Figure 22. Assets in breaches (n=4,384)
![Top Asset varieties in breaches (n=2,796)](Figure 24. Top Asset varieties in breaches (n=2,796))
Figure 24. Top Asset varieties in breaches (n=2,796)
![Compromised Assets (2008 DBIR Figure 18)](Figure 23. Compromised Assets (2008 DBIR Figure 18))
Figure 23. Compromised Assets (2008 DBIR Figure 18)
## Looking back
Although how we classified assets in the 2008 DBIR (all those years ago) was different from how we do it today, the findings are relatively similar. Most incidents impact Servers (online data) with a sprinkling of user and networking devices. It seems that servers in data breaches, like JNCO jeans and spiked tipped hair in haute couture, are timeless.
to slip through the organization’s “perimeter” by using clever tricks like (spoiler alert) stolen credentials. Dropping down the list a bit farther to the