# DBIR: 2022 Data Breach Investigations Report

## Table of Contents
- [About the 2022 cover](#about-the-2022-cover)
- [Original Table of Contents](#original-table-of-contents)
- [01 DBIR Master’s Guide](#01-dbir-masters-guide)
  - [Incident vs. breach](#incident-vs-breach)
  - [VERIS resources](#veris-resources)
  - [Industry labels](#industry-labels)
  - [Being confident of our data](#being-confident-of-our-data)
- [Introduction](#introduction)
- [Summary of findings](#summary-of-findings)
- [Results and Analysis](#results-and-analysis)
  - [Results and Analysis: Introduction](#results-and-analysis-introduction)
  - [Actor – Friends in low places](#actor--friends-in-low-places)
  - [Actions](#actions)
  - [Assets](#assets)
  - [Attribute](#attribute)
  - [Timeline](#timeline)
  - [Value Chain](#value-chain)
- [Incident Classification Patterns](#incident-classification-patterns)
  - [Incident Classification Patterns: Introduction](#incident-classification-patterns-introduction)
  - [System Intrusion](#system-intrusion)
  - [Scratching the surface](#scratching-the-surface)
  - [Social Engineering](#social-engineering)

---

## About the 2022 cover

Our long-time readers may recall that the cover for our inaugural report back in 2008 depicted an empty chair in a server room. It was intended to convey the fact that many organizations are not properly minding their assets and data. The 2022 cover is a throwback to that report both for purposes of nostalgia and to convey that many organizations continue to struggle with keeping an eye on their people and their systems. The overlay of the timeline with the dot plot illustrates the number of global contributors that have joined us over the 15-year history of the report (broken out by year).

---

## Original Table of Contents

| Section / Chapter | Page | Section / Chapter | Page | Section / Chapter | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1 DBIR Master’s Guide** | 4 | **4 Industries** | 49 | **6 Wrap-up** | 87 |
| Introduction | 6 | Introduction | 50 | Year in review | 89 |
| Summary of findings | 7 | Accommodation and Food Services | 53 | | |
| | | Arts, Entertainment and Recreation | 55 | **7 Appendices** | 92 |
| **2 Results and Analysis** | 9 | Educational Services | 57 | Appendix A: Methodology | 93 |
| Introduction | 10 | Financial and Insurance | 59 | Appendix B: VERIS and Standards | 96 |
| Actor | 11 | Healthcare | 61 | Appendix C: Changing Behavior | 98 |
| Actions | 14 | Information | 63 | Appendix D: U.S. Secret Service | 100 |
| Assets | 17 | Manufacturing | 65 | Appendix E: Ransomware Pays | 102 |
| Attribute | 18 | Mining, Quarrying, and Oil & Gas Extraction + Utilities | 67 | Appendix F: Contributing Organizations | 104 |
| Timeline | 20 | Professional, Scientific and Technical Services | 69 | | |
| | | Public Administration | 71 | | |
| **3 Incident Classification Patterns** | 22 | Retail | 73 | | |
| Introduction | 23 | Very Small Business | 75 | | |
| System Intrusion | 25 | | | | |
| Scratching the Surface | 31 | **5 Regions** | 77 | | |
| Social Engineering | 33 | Introduction | 78 | | |
| Basic Web Application Attacks | 36 | Asia Pacific (APAC) | 80 | | |
| Miscellaneous Errors | 39 | Europe, Middle East and Africa (EMEA) | 81 | | |
| Denial of Service | 41 | Northern America (NA) | 83 | | |
| Lost and Stolen Assets | 43 | Latin America and the Caribbean | 85 | | |
| Organic Free-Range Data | 45 | | | | |

---

## 01 DBIR Master’s Guide

Hello, and welcome first-time readers! Before you get started on the 2022 Data Breach Investigations Report (DBIR), it might be a good idea to take a look at this section first. (For those of you who are familiar with the report, please feel free to jump over to the introduction). We have been doing this report for a while now, and we appreciate that the verbiage we use can be a bit obtuse at times. We use very deliberate naming conventions, terms and definitions and spend a lot of time making sure we are consistent throughout the report. Hopefully this section will help make all of those more familiar.

### Incident vs. breach

We talk a lot about incidents and breaches and we use the following definitions:

> **Incident:** A security event that compromises the integrity, confidentiality or availability of an information asset.
> 
> **Breach:** An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party.

### VERIS resources

The terms “threat actions,” “threat actors” and “varieties” will be referenced often. These are part of the Vocabulary for Event Recording and Incident Sharing (VERIS), a framework designed to allow for a consistent, unequivocal collection of security incident details. Here is how they should be interpreted:

- **Threat actor:** Who is behind the event? This could be the external “bad guy” that launches a phishing campaign or an employee who leaves sensitive documents in their seat back pocket.
- **Threat action:** What tactics (actions) were used to affect an asset? VERIS uses seven primary categories of threat actions: Malware, Hacking, Social, Misuse, Physical, Error and Environmental. Examples at a high level are hacking a server, installing malware, or influencing human behavior through a social attack.
- **Variety:** More specific enumerations of higher-level categories—e.g., classifying the external “bad guy” as an organized criminal group or recording a hacking action as SQL injection or brute force.

**Learn more here:**
- [github.com/vz-risk/dbir/tree/gh-pages/2022](https://github.com/vz-risk/dbir/tree/gh-pages/2022) – DBIR facts, figures and figure data.
- [veriscommunity.net](http://veriscommunity.net) features information on the framework with examples and enumeration listings.
- [github.com/vz-risk/veris](https://github.com/vz-risk/veris) features information on the framework with examples and enumeration listings.

### Industry labels

We align with the North American Industry Classification System (NAICS) standard to categorize the victim organizations in our corpus. The standard uses two- to six-digit codes to classify businesses and organizations. Our analysis is typically done at the two-digit level and we will specify NAICS codes along with an industry label. For example, a chart with a label of Financial (52) is not indicative of 52 as a value. “52” is the NAICS code for the Finance and Insurance sector. The overall label of “Financial” is used for brevity within the figures. Detailed information on the codes and the classification system are available here: [https://www.census.gov/naics/?58967?yearbck=2012](https://www.census.gov/naics/?58967?yearbck=2012)

### Being confident of our data

Starting in 2019 with slanted bar charts, the DBIR has tried to make the point that the only certain thing about information security is that nothing is certain. Even with all the data we have, we’ll never know anything with absolute certainty. However, instead of throwing our hands up and complaining that it is impossible to measure anything in a data-poor environment, or worse yet, just plain making stuff up, we get to work. This year, you’ll continue to see the team representing uncertainty throughout the report figures.

The examples shown in Figures 1, 2, 3 and 4 all convey the range of realities that could credibly be true. Whether it be the slant of the bar chart, the threads of the spaghetti chart, the dots of the dot plot or the color of the pictogram plot, all convey the uncertainty of our industry in their own special way.

The slanted bar chart will be familiar to returning readers. The slant on the bar chart represents the uncertainty of that data point to a 95% confidence level (which is standard for statistical testing). In layman’s terms, if the slanted areas of two (or more) bars overlap, you can’t really say one is bigger than the other without angering the math gods.

The dot plot is another returning champion, and the trick to understanding this chart is to remember that the dots represent organizations. If, for instance, there are 200 dots (like in Figure 3), each dot represents 0.5% of organizations. This is a much better way of understanding how something is distributed among organizations, and provides considerably more information than an average or a median. We added more colors and callouts to those in an attempt to make them even more informative.

The Pictogram plot, our relative newcomer, attempts to capture uncertainty in a similar way to slanted bar charts but are more suited for a single proportion.

We hope they make your journey through this complex dataset even smoother than previous years.

![Figure 1: Example slanted bar chart (n=205)]

![Figure 2: Example spaghetti chart]

![Figure 3: Example dot plot (n=672). Each dot represents 0.5% of organizations. Orange: lower half of 80%. Yellow: upper half of 80%. Green: 80%-95%. Blue: Outliers. 95% of orgs: 148 - 1,594,648. 80%: 1,274 - 438,499. Median: 29,774 (log scale).]

![Figure 4: Example pictogram plot (n=4,110). Each glyph represents 40 breaches.]

> **PLEASE NOTE:** While we have always listed the following facts in our Methodology section (because that is where this type of information belongs) we decided to also mention it here for the benefit of those who don’t make it that far into the report. Each year, the DBIR timeline for in-scope incidents is from Nov. 01 of one calendar year until Oct. 31, of the next calendar year. Thus, the incidents described in this report took place between Nov. 01, 2020 to Oct. 31, 2021. The 2021 caseload is the primary analytical focus of the 2022 report, but the entire range of data is referenced throughout, notably in trending graphs. The time between the latter date and the date of publication for this report is spent in acquiring the data from the 80 odd global contributors, anonymizing and aggregating that data, analyzing the dataset and, finally, creating the graphics and writing the report. Rome wasn’t built in a day, and neither is the DBIR.

#### Questions? Comments?
Let us know! Drop us a line at `dbir@verizon.com`, find us on LinkedIn, tweet `@VerizonBusiness` with `#dbir`. Got a data question? Tweet `@VZDBIR`!

---

## Introduction

Welcome to the 15th annual Verizon Data Breach Investigations Report! It is truly hard to believe that it has been 15 years since our inaugural installment of this document. Were we to indulge our imaginations with anthropomorphic comparisons, we might find this report having its braces removed, finally being able to get a driver’s permit, overusing sarcasm, perhaps becoming a bit goth and generally being unappreciative. But we won’t bother with all that. We will simply say THANK YOU!

Thank you to our contributors for your continued willingness to share your data, insight and vast experience in a selfless effort to improve this industry. A huge thank you to our readers for sticking with us through this long and epic journey, for being the reason we work so hard to produce this report, and most of all, for keeping us from having to get real jobs.

The past few years have been overwhelming for all of us. Just when we think we have reached the uttermost limit of our ability to be surprised, the world throws us yet another curve ball. Honestly, at this point, we here on the team would not so much as blink if Sasquatch were elected Governor, if Area 51 opened a bed and breakfast, or if ransomware increased yet again. Spoiler alert – one of those things did, in fact, happen. (Congrats, Squatch! You deserve it.)

The past year has been extraordinary in a number of ways, but it was certainly memorable with regard to the murky world of cybercrime. From very well publicized critical infrastructure attacks to massive supply chain breaches, the financially motivated criminals and nefarious nation-state actors have rarely, if ever, come out swinging the way they did over the last 12 months. As always, we will examine what our data has to tell us about these and the other common action types used against enterprises. Also, in honor of the 15th edition of the DBIR, we will occasionally refer back to comments, charts and figures from previous editions of this report to see how far we, as an industry, have come, and how the threat landscape and the techniques threat actors utilize have changed. This year the DBIR team analyzed 23,896 security incidents, of which, 5,212 were confirmed data breaches.

With that in mind, let’s revisit the Introduction to the 2018 DBIR:

> “The DBIR was created to provide a place for security practitioners to look for data-driven, real-world views on what commonly befalls companies with regard to cybercrime. That need to know what is happening and what we can do to protect ourselves is why the DBIR remains relevant over a decade later. We hope that as in years past, you will be able to use this report and the information it contains to increase your awareness of what tactics attackers are likely to use against organizations in your industry, as a tool to encourage executives to support much-needed security initiatives, and as a way to illustrate to employees the importance of security and how they can help.”

From that perspective, we are proud to say that nothing has changed, and we hope you both enjoy the report and find the information it contains useful. Thanks again, for everything.

**The DBIR Team**  
Gabriel Bassett, C. David Hylender, Philippe Langlois, Alex Pinto, Suzanne Widup

_Special thanks to Dave Kennedy of the Verizon Threat Research Advisory Center (VTRAC) for his continued support and yearly contribution to this report, and to the Verizon Sheriff Team for their invaluable assistance._

---

## Summary of findings

There are four key paths leading to your estate: Credentials, Phishing, Exploiting vulnerabilities and Botnets. These four pervade all areas of the DBIR, and no organization is safe without a plan to handle them all.

![Figure 5: Select enumerations in non-Error, non-Misuse breaches (n=4,250)]

This year, Ransomware has continued its upward trend with an almost 13% increase–a rise as big as the last five years combined (for a total of 25% this year). It’s important to remember, Ransomware by itself is really just a model of monetizing an organization’s access. Blocking the four key paths mentioned above helps to block the most common routes Ransomware uses to invade your network.

![Figure 6: Ransomware over time in breaches]

2021 illustrated how one key supply chain breach can lead to wide ranging consequences. Supply chain was responsible for 62% of System Intrusion incidents this year. Unlike a Financially motivated actor, Nation-state threat actors may skip the breach and keep the access.

![Figure 7: Partner vector in System Intrusion incidents (n=3,403). Each glyph represents 25 incidents.]

Error continues to be a dominant trend and is responsible for 13% of breaches. This finding is heavily influenced by misconfigured cloud storage. While this is the second year in a row that we have seen a slight leveling out for this pattern, the fallibility of employees should not be discounted.

![Figure 8: Misconfiguration over time in breaches]

The human element continues to drive breaches. This year 82% of breaches involved the human element. Whether it is the Use of stolen credentials, Phishing, Misuse, or simply an Error, people continue to play a very large role in incidents and breaches alike.

![Figure 9: The human element in breaches (n=4,110). Each glyph represents 25 breaches.]

---

## Results and Analysis

### Results and Analysis: Introduction

Welcome to the DBIR 15-year reunion! Please grab a name tag, find some familiar faces, and reminisce about the good ole days back in 2008. Now, let’s catch everyone up on how we’ve changed over the years.

A picture may tell a thousand words, but so will a good figure. The charts we use in our report are the result of numerous iterative attempts to convey both the main story of the data, as well as the main constraints, which is a tricky[^1] proposition. Our dataset comes to us in a variety of formats and represents many different contributors—each of which come complete with their own particular nuances and biases. We realize that our data is not a ‘pure sample’ of the world of breaches and incidents (because such a thing does not exist). Nevertheless, we can still extract meaningful analysis.

You may already be familiar with the charts such as Figure 10 we used in the original DBIR, and while these bar charts are an excellent means of allowing for easy comparisons between a small set of things, they can also sometimes hide important information in their percentages. Therefore, in an effort to be more transparent with our readers regarding the level of ambiguity or uncertainty in our data, over time we have transitioned to slanted bar charts such as Figure 11, which captures both the comparison between the “things” and the range of values for those based on the confidence we have in the data. We’ve also applied the same notion to our line charts, instead of representing trends as singular lines based on the average, we plot a collection of lines within our confidence interval. The good news is that you can still convey the core message of “things change” but also provide an honest illustration of “these are the possible representations of those changes.”

After 15 years of this data breach journey, we find ourselves reminiscing about all the deadlines, failed cover ideas, and heated arguments that we encountered along the way. However, maybe the real treasure of our journey wasn’t all the fame, mega yachts, book deals and data breach analysis, but the friends we made over the years. Initially this report was based solely on Verizon data, but since then we have been joined by 87 partners and collaborators from across the globe who make this report possible. Due in large part to them, we have collected and analyzed in total over 914,547 incidents, 234,638 breaches and 8.9 TBs of cybersecurity data, to bring our readers the best possible analysis and results. Truly, we stand on the shoulders of giants. Without further ado, let’s take a dive into the analysis.

[^1]: It’s not just rhymes that are tricky to rock.

---

### Actor – Friends in low places

![Figure 10: Sources of Data Breaches (2008 DBIR Figure 3)]
![Figure 11: Actors in breaches (n=5,146)]

> Our findings indicate that data compromises are considerably more likely to result from external attacks than from any other source. Nearly three out of four cases yielded evidence pointing outside the victim organization. In keeping with other studies revealing risks inherent to the extended enterprise, business partners were involved in 39 percent of the data breaches handled by our investigators. Internal sources accounted for the fewest number of incidents (18 percent), trailing those of external origin by a ratio of four to one.
>
> The relative infrequency of data breaches attributed to insiders may be surprising to some. It is widely believed and commonly reported that insider incidents outnumber those caused by other sources. While certainly true for the broad range of security incidents, our caseload showed otherwise for incidents resulting in data compromise. This finding, of course, should be considered in light of the fact that insiders are adept at keeping their activities secret. (2008 DBIR)

Some things haven’t changed since we first began publishing this report back in 2008 (For those of you who need context, the original iPhone had been released only one year prior). The 2008 cyber[^2] security world, with limited access to handheld wonder machines, held the belief that insider incidents outnumbered external ones, or at least felt it was “certainly true for the broad range of security incidents.” As we look back now, with the benefit (?) of 15 years of time-wasting apps, considerably more gray hair and a few chips off the collective Infosec shoulders, we can confidently state that External actors are consistently more common than Internal, with 80% of breaches being caused by those external to the organization, as seen in Figure 11.

[^2]: Can you find all 145 “cyber” references in the DBIR this year? I bet you can’t…

> The median size (as measured in the number of compromised records) for an insider breach exceeded that of an outsider by more than 10 to one. Likewise, incidents involving partners tend to be substantially larger than those caused by external sources. This supports the principle that privileged parties are able to do more damage to the organization than outsiders. (2008 DBIR)

In the 2008 report, the number of records breached was the metric of choice. Now that we are a bit further into the 21st century, the currency of impact is the metric du jour. Though records are still of interest, they are typically not viewed with the same level of importance as in past years. However, in 2008 the median internal breach nabbed 375,000 records; as you can see in Figure 13, this year it’s only 80,000. While it appears the number of records is decreasing, it is important to keep in mind that a number of changes have taken place both in this report and within the industry at large. Therefore, the change in record count could be reflective of the fact that there are now more ways for attackers to monetize data.

![Figure 12: Median Number of Records Compromised (2008 DBIR Figure 5)]
![Figure 13: Records by Actor in breaches (n=54)]

![Figure 14: Motive in external agents by percent of breaches within external (2012 DBIR Figure 15)]

> Bottom line: most data thieves are professional criminals deliberately trying to steal information they can turn into cash. Like we said—same ol’ story. It’s not the whole story, however, nor is it the most important one. The most significant change we saw in 2011 was the rise of “hacktivism” against larger organizations worldwide. The frequency and regularity of cases tied to activist groups that came through our doors in 2011 exceeded the number worked in all previous years combined (2015 DBIR).

Motive, for the most part, was not an initial topic of analysis for the DBIR (although in 2008 we did consider it in the context of targeted vs opportunistic breaches). In 2010, we stated “Today’s cybercriminals are not hobbyists seeking knowledge or thrills; they are motivated by the illicit profits possible in online crime.” While that may seem obvious to today’s readers, it is important to remember that at that time the stereotypical “let me hack this site from my mom’s basement to impress my bros” type of activity was believed by many to account for a certain proportion of breaches. Regardless, the motive of the threat actor is important to understand in order to attempt to quantify how many of our troubles are caused by the illicit economy, personal vendettas or by accidental blunders.

Financial has been the top motive since we began to track it in 2015. However, that same year the rise of hacktivism (particularly leaks) accounted for many attacks. Espionage-related attacks were not even on the radar, but seven years later the world is a very different place. Espionage has taken the 2nd place spot for years, and hacktivism is, for the most part, simply an afterthought. Before we move on, however, it should be noted that while espionage has almost certainly increased over the last few years, the fact that it did not appear at all in 2015 was quite likely due to our contributors and general case load at the time.

![Figure 15: Motives in External actors by org size]

---

### Actions

The Actions section tells the story of how the security incident or breach plays out. It’s a bit like a Hollywood action movie, only with a modest budget and there are no explosions or car chases. Nevertheless, in spite of the dearth of pyrotechnics, the actions that lead up to these breaches have a definite impact on their victims.

Actions are discussed in the DBIR by variety (the type of action) and vector (through what means the action took place). Figure 16 through Figure 19 illustrate the varieties and vectors associated with incidents and breaches.

#### Action Categories

- **Hacking:** attempts to intentionally access or harm information assets without (or exceeding) authorization by circumventing or thwarting logical security mechanisms.
- **Malware:** any malicious software, script, or code run on a device that alters its state or function without the owner’s informed consent.
- **Error:** anything done (or left undone) incorrectly or inadvertently.
- **Social:** employ deception, manipulation, intimidation, etc., to exploit the human element, or users, of information assets.
- **Misuse:** use of entrusted organizational resources or privileges for any purpose or manner contrary to that which was intended.
- **Physical:** deliberate threats that involve proximity, possession, or force.
- **Environmental:** not only includes natural events such as earthquakes and floods, but also hazards associated with the immediate environment or infrastructure in which assets are located.

> **PLEASE NOTE:** That Backdoors provide a direct access point for human operators while C2s are indirect connections used by malware. “Backdoor or C2” contains both Backdoors and C2 provided only by malware, while “Backdoor” covers both backdoors provided by malware and backdoors provided by hacking. Because neither is a subset of the other, we keep them both. As a reader, your takeaway should be that remote access established by the attacker is important and that there are a slew of ways of creating that persistent access.

![Figure 16: Top Action vectors in incidents (n=18,419)]
![Figure 17: Top Action varieties in incidents (n=18,511)]

The Denial of Service (DoS) action is the clear leader, representing 46% of total incidents, followed by the malware types of Backdoor or C2 at 17%. However, a much more interesting finding is the inclusion of Partner and Software update among the top vectors this year. This is a first for Software update, and is something we will discuss in greater detail in a subsequent section. Web application is the number one vector, and, not surprisingly, is connected to the high number of DoS attacks. This pairing, along with the Use of stolen credentials (commonly targeting some form of Web application), is consistent with what we’ve seen for the past few years.

Turning to breaches, the top varieties are a bit more dynamic, with Use of stolen credentials, Ransomware and Phishing all in the top five. The category of “Other” has stealthily crept into one of the top three spots this year as well. This is largely due to the dataset being long “tailed” and diverse. In other words, there are a lot of different things that aren’t in the top 10, but are still noteworthy. We can also flip that on its head and state that 73% of breach varieties are found in the top 10 varieties. Not too shabby considering the fact that we have more than 180 different action varieties. How’s that for the Pareto principle?[^4]

In terms of vectors, these align well with the notion that the main ways in which your business is exposed to the internet are the main ways that your business is exposed to the bad guys. Web application and Email are the top two vectors for breaches. This is followed by Carelessness, which is associated with Errors such as Misdelivery and Misconfiguration. Next we have Desktop Sharing Software, which captures things like Remote Desktop Protocol (RDP) and third-party software that allows users to remotely access another computer via the Internet. Unfortunately, if you can access the asset directly over the internet simply by entering the credentials, so can the criminals.

[^4]: Not to be confused with the Peter Principle, which is something else entirely.

![Figure 18: Top Action vectors in breaches (n=3,279)]
![Figure 19: Top Action varieties in breaches (n=3,875)]

#### ’08 Throwback

While the DBIR has grown and evolved dramatically since its inception, we find it incredibly interesting how many of the core stats remain the same. In Figure 20 from 2008, you’ll find that the numbers are eerily similar to what we see today. Hacking continues to be the main action, followed by Malcode (Malware). In the 2008 report, Error was recorded in two ways: Errors that directly caused the breach (the dark bar) and Errors that contributed to the breach (light colored bar). We no longer use this breakdown (for a few reasons, one of which is that it can be argued that errors play at least a small part in almost all breaches), but Error accounts for 14% of breaches overall. From there, however, things begin to deviate slightly. This is particularly true with regard to Social and Error, but please keep in mind that our data has grown both in size and diversity of source over the years, expanding from 500 breaches that first year to over 5,000 breaches this year.

![Figure 20: Threat Categories (2008 DBIR Figure 9) Dark = Caused, Light = Contributed]
![Figure 21: Actions in breaches (n=5,212)]

---

### Assets

> #### Looking back
> Although how we classified assets in the 2008 DBIR (all those years ago) was different from how we do it today, the findings are relatively similar. Most incidents impact Servers (online data) with a sprinkling of user and networking devices. It seems that servers in data breaches, like JNCO jeans and spiked tipped hair in haute couture, are timeless.

![Figure 23: Compromised Assets (2008 DBIR Figure 18)]

![Figure 22: Assets in breaches (n=4,384)]

For those not “in the know” about VERIS, (but if you are, that’s awesome!) Assets are the THING that the Action happens to. So, this is where you find WHAT was hacked via an exploit (probably a server), WHO was socially engineered by an attacker or WHAT was lost or stolen.[^5] For the staunch defenders, this should help you understand what is being targeted and also be a useful tool to start prioritizing what type of coverage your infrastructure needs.

Figure 22 illustrates that the top varieties of Assets impacted in breaches are Servers, People and their devices. When we start to zoom into the specific types of servers (Figure 24) we find Web application (56%) and Mail (28%) servers accounting for the top two varieties, which is rather intuitive when one considers that email servers and web applications are the Assets that are most likely to be internet-facing. As such, they provide a useful venue for attackers to slip through the organization’s “perimeter” by using clever tricks like (spoiler alert) stolen credentials.

Dropping down the list a bit farther to the folks that are socially engineered. These are commonly the individuals who deal with company money and have the ability to do things with it (like update where it is deposited).

While we are on the topic of assets, it is important to remember that not only are Information Technology (IT) assets important, but so are OT (Operational Technology). The topic of OT is on many people’s minds (and in the news) these days due to the current political climate. These are the computer systems that run our national infrastructure, and while we do have a smattering of cases, they only account for approximately 3% of our overall incident data. Technically, this is an increase from last year (about 1%). Please consider this a gentle reminder to protect those systems that are quietly chugging away in the background keeping our infrastructure up and running. It isn’t called critical infrastructure for nothing.

![Figure 24: Top Asset varieties in breaches (n=2,796)]

[^5]: We feel a Schoolhouse Rock song coming on.

---

### Attribute

If security incidents did not have associated attributes, the life of an InfoSec professional would be a good deal easier. Unfortunately, they do: Confidentiality, Integrity and Availability (commonly referred to as the CIA triad), and they can greatly impact numerous aspects of an incident (who needs to be notified, what actions need to be taken and what explanations need to be given to senior management to name a few). Figure 25 shows the CIA triad over time in our dataset (with regard to security incidents).

![Figure 25: Attributes over time in incidents]

The DBIR defines a data breach as a compromise of the Confidentiality attribute, and anytime Confidentiality is compromised, it begs the question what type of data was involved? Fifteen years ago (Figure 20 from the 2008 DBIR), Payment card data led the pack by a large margin. However, it has slowly declined over the past few years. No doubt this decline is to some degree reflective of the additional security controls that have been added in recent years to protect this type of data. Regardless, Figure 27 shows the top two data types are now Credentials and Personal data. We’ve long held that Credentials are the favorite data type of criminal actors because they are so useful for masquerading as legitimate users on the system. Much like the proverbial wolf in sheep’s clothing, their actions appear innocuous until they attack. With regard to breaches, attackers are frequently exfiltrating Personal data, including email addresses, since it is useful for financial fraud. There is also a large market for their resale, which means they are truly the “gift” that keeps on giving. Unfortunately, what it gives is mostly trouble to the data subjects (whom the data is about).

![Figure 26: Compromised Data Types (2008 DBIR Figure 20)]

![Figure 27: Top Confidentiality data varieties over time in breaches]

Once attackers are inside the victim’s network they often install malware, which violates the Integrity of a system (as does any other illicit change). The Integrity of a person can also be compromised when they alter their behavior due to the actions of the adversary. Examples include responding to a phishing email or falling victim to a pretexting scenario. These are the two main types of Integrity violations we see in our data, and while they have both been present in all reports, they were not necessarily referred to in the same terminology. In the early days of the DBIR, social actions such as Phishing were not as prevalent as they are now. However, the installation of malware was already quite common back in the day, and our data shows that this year is no exception, with over 30% of breach cases involving some type of malware, and approximately 20% of cases involving a Social action.

Ransomware’s heyday continues, and is present in almost 70% of malware breaches this year. Ransomware is an attack that straddles the first two of the CIA Triad (38% of ransomware cases have some Confidentiality compromise), bringing us to the third leg: Availability. When ransomware is triggered, the organization experiences an Availability loss since they can no longer access their data. The particular variety is Obscuration in our dataset, as shown in Figure 28.

Another common form of availability impact is Interruption which often arises from Distributed Denial of Service (DDoS) attacks. These attacks make up a large number of incidents, but are relatively non-existent in our breach caseload. But if DoS is something you are particularly concerned about, we have an entire pattern devoted to it.

![Figure 28: Top Availability varieties in breaches (n=1,109)]

---

### Timeline

Discovery time is a good place to begin when viewing timelines. While Figure 29 might seem like good news (that we are more likely to detect breaches within days than months), it gets to be a little less comforting once you start looking at some of the drivers. The top Discovery Method for breaches (more than 50%) is now “Actor Disclosure” (normally either on the asset in the form of a ransomware note or on a criminal forum to sell the data or announce the breach). Neither of which is desirable. “Ignorance is bliss” doesn’t readily apply to breaches.

![Figure 29: Detection in non-actor-disclosed breaches]

#### Event Chains

Rather than simply analyze how long an attack took in time, we can also analyze how long it took with regard to Actions in Figure 30. We can view this timeline of Actions in our Event Chain data. Event Chains capture the path an attack followed.[^6] Figure 30 shows that the vast majority of breaches include only a handful of steps. Three Actions (Phishing, Downloader, and Ransomware) are the most common, while very few breaches utilize five or more Actions. Our job as defenders is to lengthen that attack path. Attackers tend to avoid longer attack chains because every additional step is a chance for the defender to prevent, detect, respond to and recover from the breach.

![Figure 30: Number of steps per breach in non-Error breaches (n=258)]

[^6]: Event Chains are kinda like Attack Flow in Appendix B: VERIS and Standards, but more basic.

---

### Value Chain

#### “It takes money to make money”

Over the past two years the DBIR team has been collecting value chain information, defined as the capabilities and investments an attacker must acquire prior to the actions on the target, either by purchase or investment in its creation. Traditionally, defenders are largely focused on the events that occur within their boundaries, which makes sense since those are the things they control. However, an attacker ecosystem exists both before and after the breach, and it plays into and feeds off of the incident. The value chain asks the question “Where did that email address come from?” Or “Where do those stolen credentials go?” It often seems that breaches beget more breaches, creating a Circle of Breach[^7] so to speak. By understanding the transactions associated with this ecosystem, we can understand the key steps involved in attacks and work collaboratively to make those transactions more difficult, expensive or unsustainable for the attackers.

There are several things attackers must invest in for a breach:

- **Development:** software or content that must be developed to accomplish the actions on the target.
- **Targeting:** work that identifies exploitable opportunities. These overlap heavily with the data varieties that are compromised.
- **Distribution:** services used to distribute actor content including email, compromised servers and websites.
- **Non-Distribution Services:** services provided and used by threat actors other than those used for distribution of actor content.
- **Cash-out:** methods for converting something (likely the attribute compromised) into currency.

![Figure 31: Top value chain variety by value chain category in breaches]

Figure 31 provides the top variety for each part of the value chain. Email is the most common method. While we can easily infer email in the value chain, things such as malware in development or credentials in targeting are harder to infer, and so may be underrepresented. Malware can be freely available and credentials may be stolen. The takeaway is not to think of breaches only in terms of starting or ending. Instead, think of them like you might think of a sports team: they are either on the field or preparing to be.

[^7]: Like the Circle of Life, but for threat actors.

---

## Incident Classification Patterns

### Incident Classification Patterns: Introduction

The DBIR dataset is very large and, at times, extremely complex. It captures many different types of data points, and it grows larger each year. In order to create an easier way to analyze the ever-growing mountain of data and, even more importantly, to assist us in communicating our findings to our readers, we began using “Patterns” in our 2014 report.

![Figure 32: Patterns over time in incidents]

The patterns are essentially clusters of “like” incidents. Starting in 2014, and for several subsequent years, there were nine patterns. Last year we found that due to changes in attack type and the threat landscape, the data was leading us toward revamping, combining and generally overhauling those patterns. Therefore, starting with the 2021 report, we moved from the original nine patterns down to the eight you see in this report. The eight patterns, and how they are defined, can be found in Table 1. Please be sure to peruse the way we define the different patterns, as we will refer to them throughout the report.

| Pattern | Description |
| :--- | :--- |
| **Basic Web Application Attacks** | These attacks are against a Web application, and after initial compromise, they do not have a large number of additional Actions. It is the “get in, get the data and get out” pattern. |
| **Denial of Service** | Attacks intended to compromise the availability of networks and systems. This includes both network and application layer attacks. |
| **Lost and Stolen Assets** | Incidents where an information asset went missing, whether through misplacement or malice. |
| **Miscellaneous Errors** | Incidents where unintentional actions directly compromised a security attribute of an information asset. This does not include lost devices, which are grouped with theft instead. |
| **Privilege Misuse** | Incidents predominantly driven by unapproved or malicious use of legitimate privileges. |
| **Social Engineering** | A psychological compromise of a person that alters their behavior into taking an action or breaching confidentiality. |
| **System Intrusion** | Complex attacks that leverage malware and/or hacking to achieve their objectives including deploying Ransomware. |
| **Everything Else** | This “pattern” isn’t really a pattern at all. Instead, it covers all incidents that don’t fit within the orderly confines of the other patterns. Like that container where you keep all the cables for electronics you don’t own anymore: Just in case. |

_Table 1. Incident Classification Patterns_

![Figure 33: Patterns over time in breaches]

---

### System Intrusion

![Figure 34: System Intrusion incident paths (n=228)]

#### Summary

| Metric | Details |
| :--- | :--- |
| **Frequency** | 7,013 incidents, 1,999 with confirmed data disclosure |
| **Threat Actors** | External (98%), Internal (2%) (breaches) |
| **Actor Motives** | Financial (93%), Espionage (6%) (breaches) |
| **Data Compromised** | Credentials (42%), Personal (37%), Other (35%), Internal (16%) (breaches) |

#### It’s complicated

This pattern consists of more complex breaches and attacks that leverage a combination of several different actions such as Social, Malware and Hacking and is where we find Supply Chain breaches and Ransomware, both of which increased dramatically this year.

Although we have defined the System Intrusion pattern earlier in the report, a good example may be called for. When you think of Advanced Persistent Threat (APT) or some other form of capable actor moving across the environment popping shells, dropping malware, dumping creds and doing all the fun stuff you would expect from an unexpected Red Team exercise, that’s System Intrusion.

#### What is the same?

This pattern continues to see the Use of stolen credentials and malware, such as Ransomware, as the top concerns.

From a look at our data this year, it would appear that defenders have faced many challenges, particularly with rises in Ransomware and threats originating from partners (including vendors).

To better understand this pattern, let’s take a look into the action varieties and vectors that make up the incidents. Figure 35 shows the top Action varieties with Backdoor (provided by the malware) and Ransomware competing for the top spot, followed by Use of stolen credentials. With regard to vectors, in Figure 36, we see Partner and Software update (shocker!) as the leading vectors for incidents. This is primarily attributed to one very large and very public security incident that happened last year. We’ll give you a hint, it rhymes with “PolarShins.” Please see “Partners, Supply Chains and 3rd parties, oh my” for more information. However, if we look past the Partner and Software update varieties, we find that 14% of incidents involved Desktop sharing software as one of the main vectors, followed by Email at 9%.

![Figure 35: Top Action varieties in System Intrusion incidents (n=5,212)]
![Figure 36: Top Action vectors in System Intrusion incidents (n=3,403)]

![Figure 37: Malware delivery method proportion per organization]

Figure 37 captures the distribution of file types along with the distribution of the delivery methods. It seems that the common route of office docs and emails[^8] are still the tried-and-true method for delivering those initial payloads, which can then be used for further naughty deeds such as Ransomware deployment.

[^8]: With the median organization receiving over 75% of its malware via email.

#### Rampant Rampaging Ransomware

This section is the perfect sequel to last year’s finding of Ransomware dramatically increasing (unlike my Unamused Baboons NFT’s value). That trend has continued with an almost 13% increase this year (an increase as large as the last five years combined).

![Figure 38: Ransomware over time in breaches]

Keeping in mind that while insidious, Ransomware alone is simply a model of monetization of a compromised organization’s access that has become quite popular. Ransomware operators have no need to look for data of specific value, e.g., credit cards or banking information. They only need to interrupt the organizations’ critical functions by encrypting their data.

#### Ransomware routes

While Ransomware comes in a variety of different flavors with catchy and not so catchy names, the way that Ransomware makes its way onto a system isn’t quite as diverse. In Figure 39 you can see the pairings of the Actions to their respective vectors which are used to deploy Ransomware. There are a couple of key points to consider: 40% of Ransomware incidents involve the use of Desktop sharing software and 35% involved the use of Email. There are a variety of different tools the threat actor can use once they are inside your network, but locking down your external-facing infrastructure, especially RDP and Emails, can go a long way toward protecting your organization against Ransomware.

When we examine the types of malware blocked, we find that Droppers are typically the second most common. This aligns well with Email being such a prevalent entry point. If attackers have credentialed remote access, they can leverage that directly. Otherwise they must make their own remote access by emailing either malicious links or attachments.

> #### Looking Back: Ransomware
> Even though the first Ransomware case occurred when at least one of the current authors was still in diapers (1989), it took quite a while for it to become a mainstay in the DBIR. The first case of Ransomware showed up in our data in 2008 and it wasn’t until 2013 that we had sufficient data to write something about it. And we quote:
>
> “When targeting companies, typically SMBs, the criminals access victim networks via Microsoft’s Remote Desktop Protocol (RDP) either via unpatched vulnerabilities or weak passwords. Once they’ve gained initial access they then proceed to alter the company’s backup so that they continue to run each night but no longer actually backup any data.” (2013 DBIR page 31)
>
> Had we known that what was true nine years ago would still be true today, we could have saved some time by just copying and pasting some text. Oh well, maybe in another nine years things will change for the better.

![Figure 39: Select action varieties within vectors in System Intrusion Ransomware incidents (n=1,032)]

#### Partners, Supply Chains and 3rd parties, oh my

For anyone who deals with supply chains, third parties and partners, this has been a year to remember. For those who need a quick recap, 2020 ended[^9] (sadly, soon after the data collection window for the 2021 report) with a bit of a bang as a massive espionage campaign was discovered by our intrepid friends in the cybersecurity community. This event kicked off a complex, grueling and herculean effort to identify the potential victims impacted by the supply chain breach. While we typically don’t examine individual events, but restrict our attention to the larger trends, this one incident alone had a tremendous effect in the industry and impacted our dataset in some surprising ways. One only need glance at Figure 36 to see just how severe an influence this one incident had on our System Intrusion pattern: skyrocketing Software updates moved Partner from its previous position as somewhat of a novelty (formerly showing up in less than 1% in our data) to an astounding 60% of incidents. However, while this incident might seem like an anomalous one-off, it may actually be representative of larger trends that we’ve been seeing in the industry, in terms of the interconnected risks that exist between the vendors, partners and third parties we work with on a daily basis.[^10]

To understand the big picture of these breaches, we need to define Third-party and Supply chain breaches and that can be a bit complex. First of all, we should caveat that we code our incidents based off of the victim. Therefore, it is typically (though not always, of course) one victim, one incident. However, that fails to capture the interconnected nature of real-world environments when discussing Supply Chain and Third-party breaches. Over time we added fields that would assist to capture breaches with “secondary victims” that were impacted by the initial breach.

We define Third-party breaches as a single breach that compromised a Third-party. In our data, this is when the data owner is different from the breached victim. An example would be a datacenter that suffered a ransomware incident which encrypted their customer’s data. While their customer’s internal infrastructure was never directly breached, they were certainly impacted.

In our 2022 dataset we found that Third-party breaches represent a small percentage (1%) of our breach data. Nevertheless, we can still find some interesting data points. For example, within these Third-party breaches, we found the Use of stolen credentials along with Ransomware as two of the top five action varieties.

![Figure 40: Top Action varieties in third-party incidents (n=73)]

The next type of incident vector is the Supply Chain. We define Supply Chain breaches as a sequence of one or more breaches chained together. In our data this may be a breach where there are secondary victims (when seen from the primary victim’s breach) or where a partner was the vector (when seen from the secondary victim’s breach). Another common example would be when a compromised software vendor is used to push a malicious update to an organization resulting in a breach, or a generic partner breach where a partner is compromised and either a set of credentials or some trusted connection is used to gain access.

After the major events of last year, these types of incidents account for 9% of our total incident corpus and 0.6% of our breaches this year. Due to the major event in 2021 in which a large network administration tool was compromised and used to push a backdoor to compromised servers, we see an extremely high rate of Backdoor[^11] in the action varieties. However, there are still other noteworthy items within those remaining percentages such as Ransomware, Use of stolen credentials and other forms of malware with the capabilities you might expect to see. We have encountered cases of Supply Chain attacks in previous reports, reminding us that even if it’s not a frequently used tactic each year, there is an established precedent for these attacks.

![Figure 41: Top varieties in Supply Chain incidents (n=2,103)]

[^9]: I mean, we’re told it ended. We can neither confirm nor deny, as we are still in our bunkers awaiting the imminent arrival of Ragnarök.
[^10]: The timeline section talks about value chains and event chains, which are both part of the attacker Circle of Breach.
[^11]: And because “Backdoor or C2” contains backdoor, we see a large amount of it as well.

#### Ending remarks

When large-scale events like those we experienced in 2021 happen, they can shake our confidence in our abilities to protect ourselves. However, it is important to keep in mind that the close collaboration between federal security organizations and the cybersecurity community resulted in the detection and remediation of this event within a few months rather than years. While we do not have sufficient information to know whether or not the perpetrators considered it a successful operation, we can say that as an industry and as a community, we were ultimately successful in sharing resources and protecting each other from a complex threat. Thank you to everyone that stepped up and assisted in this effort. You deserve a drink of your choice and the DBIR team would be happy to raise a glass with you.

---

### Scratching the surface

We discuss many things related to the human element in the DBIR: Phishing, Credentials, Errors, etc. However, this section is about the entry point into your organization that does not directly involve a human asset: Vulnerabilities.

The action variety of Exploit vulnerability is up to 7% of breaches this year, doubling from last year. While it’s not on par with the massive numbers we see in Credentials and Phishing, it’s worth some thought. The first question one might reasonably ask is “How are attackers finding these vulnerabilities?” As we pointed out last year, attackers have a sort of opportunistic attack sales funnel as seen in Figure 43. They start with scanning for IPs and open ports. Then they move to crawling for specific services. They then move on to testing for specific Common Vulnerabilities and Exposures (CVE). Finally, they try Remote Code Execution (RCE) to gain access to the system.

If attackers have this process for targeting organizations, what do they find? In Figure 42 we found sets of organizations in four different categories with about 100 organizations in each: Secure (or at least actively trying to be secure), Ransomware (organization with a disclosed ransomware incident), Random (organizations chosen purely at random) and Breached (organizations that had suffered a breach). We looked at how many vulnerabilities they had per host on average.[^12]

What we found is the median company in all categories had almost no vulnerabilities (with random organizations being just a bit higher). This can happen because so many breaches aren’t tied to vulnerabilities. However, the tails of the distribution tell a different story. While security-concerned organizations run a pretty tight ship, the other three have organizations out in the tail with far more vulnerabilities per internet-facing host. And if you wonder who the threat actors from Figure 43 are looking for, it’s the organizations in that tail. Remember that for many attackers it’s simply a numbers game—they just want some amount of access—and those tails still provide enough of an incentive for them to continue to try the exploits until they get lucky.

![Figure 42: Vulnerabilities per host by organization type (only organizations with internet presence represented)]
![Figure 43: Threat actor opportunistic sales funnel]

[^12]: And by average, we mean median because statistics isn’t hard enough already. Mode.

The good news is we are getting better. Figure 44 shows vulnerability remediation speed and completeness over the past six years. Higher is better in this figure and, in general, things are looking up. We’re patching more and we’re patching faster.

![Figure 44: Time to remediate findings]

Another bright spot is that last year we talked about Gini coefficients, (basically a measure of if a few things happened a lot and a lot of things happened only a few times). We apply that in Figure 46 to the different levels of the Pyramid of Pain. For the non-threat intelligence expert, the Pyramid of Pain[^13] is a model used by threat intelligence analysts to categorize the value of different indicators to the defender. The base of the pyramid is trivial for the attacker to modify (like the hash of a file) and therefore less useful to the defender. The tip of the pyramid is extremely difficult to modify by the attacker (like the attacker’s established process also known as Tactics, Techniques and Procedures [TTPs]).

| Pyramid Layer | Level of Difficulty |
| :--- | :--- |
| **TTPs** | Tough! |
| **Tools** | Challenging |
| **Network / Host Artifacts** | Annoying |
| **Domain Names** | Simple |
| **IP Addresses** | Easy |
| **Hash Values** | Trivial |

![Figure 45: Pyramid of Pain]
![Figure 46: Cumulative sum of indicators]

[^13]: “The Pyramid of Pain,” Bianco, David J., [https://bit.ly/PyramidOfPain](https://bit.ly/PyramidOfPain), January 2014.

What we found was that other than hashes, most indicators in the Pyramid of Pain have pretty high Gini coefficients. That means that if you block the first few percent of that indicator, you stop most of the malice. Frankly we expected that the Gini coefficient would go up as we went up the pyramid, but from IP addresses on up, they are all about the same. We see something similar with IPs back in Figure 43. Only 0.4% of the IPs that attempted RCEs weren’t seen in one of the prior phases showing what SecOps probably already know: Block bad IPs!

You may notice we didn’t get the TTPs at the top of the pyramid. The reality is the DBIR team just doesn’t have this data. But check out Appendix B: VERIS & Standards for Attack Flow: a solution to this data collection problem!

---

### Social Engineering

![Figure 47: Social Engineering incident paths (n=75)]

#### How is this my fault?

| Summary | Details |
| :--- | :--- |
| **Frequency** | 2,249 incidents, 1,063 with confirmed data disclosure |
| **Threat Actors** | External (100%), Internal (breaches) |

The human element continues to be a key driver of 82% of breaches and this pattern captures a large percentage of...

---

----------------- | ------------- | ----------------- |
This year, 82% of breaches in the
| those breaches. Additionally, malware  |     | (breaches) |
| -------------------------------------- | --- | ---------- |
DBIR14 involved the human element.
and stolen credentials provide a great
This puts the person square in the
|     | Actor Motives | Financial (89%),  |
| --- | ------------- | ----------------- |
center of the security estate with the  second step after a social attack gets
Espionage (11%),
Social Engineering pattern capturing  the actor in the door, which emphasizes
| the importance of having a strong  |     | (breaches) |
| ---------------------------------- | --- | ---------- |
many of those human-centric events.
security awareness program.
|     | Data  | Credentials (63%),  |
| --- | ----- | ------------------- |
Compromised
Internal (32%),
| What is the same? |     | Personal (24%),  |
| ----------------- | --- | ---------------- |
Other (21%)
These attacks continue to be split
(breaches)
between Phishing attacks and the more
convincing Pretexting attacks, which
are commonly associated with
Business Email Compromises.
14 Not just the Social Engineering pattern.
2022 DBIR  Incident Classification Patterns 33

As you can see in Figure 49, the Social BEC
Engineering pattern is dominated by
In Figure 49, we see that Pretexting is
Phishing. And we know what you’re
27% of Social Engineering breaches,
going to say: “I’m so surprised! Fetch
almost all of which are BECs. While we
my fainting couch!”
call these attacks BECs, they tend to
But in a way the chart highlights the be a bit more complex than just some
numerous paths a social engineering bad actor impersonating someone
breach can take. We see where the through a compromised email account.
phish steals credentials to then be Only 41% of BECs involved Phishing. Of
used in “Use of stolen creds.” We see the remaining 59%, 43%17 involved Use
Business Email Compromises (BECs) of stolen credentials against the victim
(with the E for email being directly organization. The percentage remaining
tied to the phish) in “Pretexting.” were most likely BECs using an email
We see malware being dropped in from a partner, or utilizing a free email
“Downloader” and “Ransomware” account of some type requiring no “C”18
(which, by the way, goes up to 17% at all. BECs come in many forms: your
of Social Engineering when we are organization may be targeted due to
discussing incidents rather than a breach in a partner, your partners
breaches), hacking in “Scan network” may be targeted due to a breach of
and “Profile host,” and persistence in your emails, you may be breached and
“Backdoor or C2.” All in all, it highlights then targeted using your own breach,
the fact that phishing is one of the four or as pointed out earlier, there may be
main entry points into an organization.15 no breach at all, just an attacker with a
convincing story about why they need
your money.
Phishing
Sutton’s law tells us “When diagnosing,
first consider the obvious.” Thus, if
you wonder why criminals phish, it is
because email is where their targets
are reachable. And while only 2.9%
of employees may actually click on
phishing emails, a finding that has
been relatively steady over time, that
is still more than enough for criminals
to continue to use it. For example, in
our breach data alone, there were
1,154,259,736 personal16 records
breached. If we assume those are
mostly email accounts, 2.9% would
be 33,473,532 accounts phished,
(akin to successfully phishing every
person in Peru). Figure 48. Phishing email report rate by Figure 49. Action varieties in Social
click status (n=295,825,679) Engineering breaches (n=1,063)
The good news is we are getting
better at reporting phishing. Figure 48
shows a steady climb with an increase
of roughly 10% in phishing test emails
reported in the last half decade. The
question is “Can your organization
both act on the 12.5% that reported
and find the 2.9% that clicked?”
15 Along with Credentials, Vulnerabilities and pre-existing Bots.
16 “Personal” doesn’t have to be email. It could be addresses and names and such, but it normally includes email. And this doesn’t even count credentials
where the username is often an email.
17 Ok, so 59% times 43%, carry the 1, convert to roman numerals ... that’s like 25% of all BECs!
18 Compromise.
2022 DBIR Incident Classification Patterns 34

Figure 50 gives an idea of how much the door, Figure 52 shows that the improve security behaviors, in both day-
of that money the criminals feel they Backdoor, C2 and Downloader hold it to-day (such as Don’t Click … Stuff, and
need. It appears they saw inflation on open for all the rest of the actions to using a password keeper) as well as in
the horizon and granted themselves a make their way in. It is noteworthy that design (such as secure coding, lifecycle
raise this year. Regardless, you, being while Ransomware shows up about management, etc.). Unfortunately, while
the erudite reader of the DBIR that you halfway down the list in breaches, getting training is easy, proving it’s
are, can do something about it. File a the same analysis for incidents has working is a bit harder. If you want some
complaint at ic3.gov and get in touch Downloader and Ransomware moving pointers on how to do it, have a look at
with the FBI IC3 Recovery Asset Team into the top two spots with 74% and Appendix C: Changing Behavior.
(RAT). In cases where the RAT acts on 64% of malware incidents respectively.
BECs, and works with the destination This definitively proves that we can’t
bank, half of all U.S.-based BECs had write a single section of the DBIR this
93% of the money either recovered or year without mentioning Ransomware
frozen, whereas only 14% had nothing at least once.
at all recovered.
Training
Clearly the Human Element leaves
a lot to be desired when it comes
to information security. Even when
a breach is not directly caused by
a person, the information systems
were still built by people.19 Frankly,
we’d rather have people solving the
problems since asking the AI to do it
sounds much trickier.
Unfortunately, nothing is perfect. Not
people, not processes, not tools, not
systems.20 But, we can get better,
Figure 50. Median transaction size
both at what we do and what we build.
for BECs (n=50,342). Based on FBI
To that end, training is a big part of
IC3 complaints where a transaction
improving. Figure 51 gives an idea of
occurred.
the amount of phishing training folks
are taking per year. Most training takes
twice as long to complete than was
Malware expected, with 10% taking three times
as long. Training can potentially help
“Malware? I already read about it in
the Action section. Why do I have to
hear about malware again?!” Because
there’s lots of it! Although, we admit
there is a degree of bleed-over in the
sections. This year we saw more things
that fell into two patterns than we did
last year. With System Intrusion and
Social Engineering being chief
among them.
As Figure 37 in the System Intrusion
section points out, email is the most
common malware delivery method,
at least initially. Figure 52 shows that,
in breaches, providing a Backdoor or
Command and Control (C2), followed
by delivering a Downloader are the top
two things actors are looking to do Figure 51 . Minutes per year spent Figure 52. Top Malware varieties in
once their successful phish lands their on training per person (n=45,372, Social Engineering breaches (n=235)
malware. If the phish busts through log scale)
19 Unless that whole bigfoot thing is true. We sent Dave to a conference to find out but haven’t heard back.
20 Not DBIR authors (this is debatable. We asked the Oracle, rolled some bones, and signs pointed to “probably perfect”).
2022 DBIR Incident Classification Patterns 35

Basic Web
Application Attacks
Figure 53. Basic Web Application Attacks incident paths (n=92)
Does this
|          | Summary                                | Frequency | 4,751 incidents, 1,273  |
| -------- | -------------------------------------- | --------- | ----------------------- |
| make my  |                                        |           | with confirmed data     |
|          | Attacks within this pattern are split  |           | disclosure              |
between two areas. The means of
infrastructure
|           | accessing the server, such as using  | Threat Actors | External (100%)   |
| --------- | ------------------------------------ | ------------- | ----------------- |
|           | stolen credentials, exploiting       |               | (breaches)        |
| look big? | vulnerabilities and brute forcing    |               |                   |
|           |                                      | Actor Motives | Financial (65%),  |
passwords constitutes the first.
Espionage (31%),
The second represents the specific
In Basic Web Application Attacks
|     | payload, such as backdoors, which   |     | Grudge (2%),  |
| --- | ----------------------------------- | --- | ------------- |
(BWAA), we are largely focusing
|     | are used to maintain persistence or  |     | Ideology (1%)  |
| --- | ------------------------------------ | --- | -------------- |
on attacks that directly target
|     | monetize access. |     | (breaches) |
| --- | ---------------- | --- | ---------- |
an organization’s most exposed
| infrastructure, such as Web servers.  |     | Data  | Personal (69%),  |
| ------------------------------------- | --- | ----- | ---------------- |
These incidents leverage one or the  What is the same? Compromised Credentials (67%),
| other of two entry points, the Use of  |     |     | Other (29%), Medical  |
| -------------------------------------- | --- | --- | --------------------- |
stolen credentials or Exploiting   This pattern continues to largely be  (15%) (breaches)
| a vulnerability. | dominated by the Use of stolen  |     |     |
| ---------------- | ------------------------------- | --- | --- |
credentials to access an organization’s
internet-facing infrastructure, like web
servers and email servers.
2022 DBIR  Incident Classification Patterns 36

Hopefully, Figure 54 demonstrates
the importance of proper password
protection since over 80% of the
breaches in this pattern can be
attributed to stolen credentials. Figure
55 reveals the larger trends in terms of
using stolen credentials vs exploiting
vulnerabilities. There’s been an almost
30% increase in stolen credentials
since 2017, cementing it as one of the
most tried-and-true methods to gain
access to an organization for the past
four years.
Figure 55 clearly displays how the vast
majority of incidents involving Web
application are using stolen credentials.
There is a sprinkling of other vectors
in Figure 56, such as Backdoor (useful
after you have a foothold), Remote
injection (how malware gets on the
system after an exploited vulnerability)
and, of course, Desktop sharing
software.
Figure 54. Top Action varieties in Basic Figure 55. Exploit vuln vs Stolen creds Figure 56. Top Action vectors in Basic
Web Application Attacks breaches over time in Basic Web Application Web Application Attacks breaches
(n=962) Attacks breaches (n=972)
2022 DBIR Incident Classification Patterns 37

Mail servers under attack Basic != not useful
With regard to what is being targeted, One might be forgiven for assuming
Figure 59 captures the high prevalence that these types of attacks would
of Web application (which seems largely be the work of enterprising
obvious based on the title of the criminals spraying the internet looking
section) but also of Mail servers, which for weak credentials. However, it seems
represented less than 20% of the that Nation-state actors have also
total breaches in this pattern. Of those been leveraging this low-cost, high-
Mail servers, 80% were compromised pay-off strategy with over 20% of our
with stolen credentials and 30% were BWAA breaches being attributed to
compromised using some form of Espionage. If the front door has a weak
exploit. While this 30% may not seem lock there is no reason to develop a
like an extremely high number, the complicated polymorphic backdoor
targeting of mail servers using exploits with a fast flux network of C2 servers.
has increased dramatically since last
year, when it accounted for only 3% of
the breaches.
Looking back:
Santayana tells us that “those who do not learn from history are doomed
to repeat it.” That seems to be the case, as we have continued to see poor
Figure 58. Top Motives in Basic Web
password practices as one of the leading causes of data breaches dating Application Attacks breaches (n=251)
back to 2009.
“From the chart, it is evident that many intrusions exploit the basic
(mis)management of identity. Unauthorized access via default,
shared, or stolen credentials constituted more than a third of the
entire Hacking category and over half of all compromised records.
It is particularly disconcerting that so many large breaches stem
from the use of default and/or shared credentials, given the relative
ease with which these attacks could be prevented.”
(2009 DBIR page 17)
Figure 59. Top Asset varieties in Basic
Web Application Attacks breaches
(n=1,001)
Figure 57. Types of Hacking by number of breaches (black) and percent of records
(red) (2009 DBIR Figure 15)
2022 DBIR Incident Classification Patterns 38

Miscellaneous
Errors
Figure 60. Miscellaneous Errors incident paths (n=32)
Misconfiguring
| Summary | Frequency | 715 incidents, 708   |
| ------- | --------- | -------------------- |
the situation  with confirmed data
| While this pattern is by definition   |     | disclosure |
| ------------------------------------- | --- | ---------- |
made up of either Internal or Partner
| actors, this year’s data shows it is all  | Threat Actors | Internal (100%)  |
| ----------------------------------------- | ------------- | ---------------- |
While most patterns have changed
| about your employees. Misdelivery   |     | (breaches) |
| ----------------------------------- | --- | ---------- |
over the years, one constant has been
people making mistakes. In 2015,  and Misconfiguration are the top two
|     | Data  | Personal (81%), Other  |
| --- | ----- | ---------------------- |
most mistakes were the Misdelivery  varieties. Misconfiguration is frequently
|     | Compromised | (23%), Medical (18%),  |
| --- | ----------- | ---------------------- |
of Media assets (Documents) while  paired with the Discovery Method of
| “Security Researcher.” |     | Bank (8%) (breaches) |
| ---------------------- | --- | -------------------- |
Misconfiguration accounted for
less than 10% of breaches. This
What is the same?
year, however, Misconfiguration and
Misdelivery have converged. People are still fallible, and that fallibility
can cause data breaches.
2022 DBIR  Incident Classification Patterns 39

The rise of the Misconfiguration error The data types involved in these
began in 2018 and was largely driven breaches are still overwhelmingly
by cloud data store implementations of the Personal variety. Medical and
that were stood up without Banking information are occasionally
appropriate access controls. Many involved, but they are not the norm.
security researchers made a name for The data tends to be from customers,
themselves by finding these exposed and it is also the customers who are
databases on the internet. Despite the notifying the breached organizations
efforts of the major cloud providers to in a high number of cases. However,
make the default configurations more Security researchers are still the stars
secure (which we applaud), these of this Discovery show (although their
errors persist. percentage is down from last year).
These days Misdelivery data breaches
are frequently electronic in nature
and consist of email going to the
wrong recipients, although physical
Documents do remain a problem to
some degree. Figure 62. Top Asset varieties in
Miscellaneous Errors breaches (n=513)
Figure 61. Top Action varieties over time in Miscellaneous Errors breaches
2022 DBIR Incident Classification Patterns 40

Denial of
Service
Figure 63. Denial of Service incident paths (n=3)
Heavy
Summary Frequency 8,456 incidents,
traffic ahead 4 with confirmed
While these attacks are a nuisance data disclosure
impacting a large range of organizations,
Welcome to the Denial of Service some organizations face these attacks Threat Actors External (100%)
pattern—one that is perhaps all too on a regular basis which may potentially (incidents)
familiar to many of you, as it continues impact their business function.
to be the top type of incident in our
dataset. This pattern consists of those
What is the same?
annoying attacks where botnets or
compromised servers are leveraged Denial of Service continues to be one
in order to send junk data to target of the most common types of
computers with the hopes of denying cybersecurity incidents.
that service by creating a “traffic jam in
the pipes.”
2022 DBIR Incident Classification Patterns 41

These types of irksome incidents aren’t are perpetually bombarded with DoS
isolated to any one industry. As Figure attacks. We found that the median
64 demonstrates there are a wide Denial of Service attack lasted less
range of companies from Information than four hours (Figure 65) and that
Services, Professional Services, the vast majority of organizations
Manufacturing and Government that are monitored for these attacks
(which happens to cover many of the experience less than 10 attacks a year.
industries we write about). If, on the other hand, you’re one of
those unlucky 1% of companies that
However, while they may be ubiquitous experience more than 1,000 DDoS
within industries, it does not mean attacks a year, you’re already aware of
that organizations in these industries this and most likely have a service to
help you manage the traffic.
My, how big your DDoS
have gotten
We first became acquainted with
DDoS in the 2013 DBIR and it has
since become a regular topic of
discussion. It is interesting to look
back and see how things have
changed over the years. For 2013 era
DDoS, the median attack was clocking
in around 422 Mbps, with a very small
number hitting the 100Gbps mark. By
2016, the median value was 1.1 Gbps
(doubling from three years prior) and
today the median is around 1.3 Gbps.
We can also see how DDoS has
become narrowly centered. From
2013, through 2016, and on to 2021,
DDoS has become tightly clustered
around the median. We speculate21
that back in 2013, DDoS attacks
were ad hoc, whereas today’s DDoS
infrastructure is far more formalized
and repeatable.
Figure 64. Top industries in Denial of Figure 65. DDoS attack duration Figure 66. DDoS BPS over time
Service incidents (n=8,330) (n=15,059 log scale) (log scale)
21 Read “guess.”
2022 DBIR Incident Classification Patterns 42

Lost and
Stolen Assets
Figure 67.  Lost and Stolen Assets incident paths
Losing it
| Summary | Frequency | 885 incidents,   |
| ------- | --------- | ---------------- |
81 with confirmed
In last year’s report, we mentioned that  Most of the cases in this pattern are  data disclosure
for security incidents (not confirmed  classified as “incidents” rather than
| “breaches, because the nature of the  | Threat Actors | Internal (94%),  |
| ------------------------------------- | ------------- | ---------------- |
breaches), assets were far more likely
| devices stolen makes it difficult to  |     | External (6%)   |
| ------------------------------------- | --- | --------------- |
to be lost by employees than stolen by
| confirm data access. The prevalence  |     | (incidents) |
| ------------------------------------ | --- | ----------- |
someone who does not work for the
organization. However, when looking at  of theft in this pattern is driven by the
|     | Actor Motives | Financial (98%),  |
| --- | ------------- | ----------------- |
breaches, we see the opposite is true. Financial motive—we believe many of
Ideology (2%)
the perpetrators of theft are
(incidents)
committing the crime with the
intention of an immediate payoff
|     | Data  | Personal (77%),  |
| --- | ----- | ---------------- |
by selling the stolen asset.
|     | Compromised | Medical (43%), Other  |
| --- | ----------- | --------------------- |
(15%), Bank (9%)
(incidents)
What is the same?
The type of data affected by these
incidents is the same (almost exactly)
as last year. External actors typically
perpetrate the thefts, while employees
are responsible for losing track of
their assets.
2022 DBIR  Incident Classification Patterns 43

Stolen assets are more likely to be Figure 69 shows the devices most
the causes of cases where we can often lost or stolen. User devices
confirm that data compromise occurred. (including desktops, laptops and
Still, this is a pattern where most mobile phones) are most frequently
(approximately 90%) of the cases are the type of item that is either lost
classified as “security incidents” rather or stolen. However, Documents still
than “breaches,” because confirming account for a good percentage of these
that the data was compromised is breaches. This occurs most often in the
difficult based on the assets stolen. Public Administration and Healthcare
industries, which goes some way
We found it interesting that, despite the toward explaining the prevalence
pandemic and the resulting lessening of Medical data compromised in
of travel, the Lost and Stolen Assets these incidents. The government (of
remained a common pattern in our almost any country) administers large
dataset. It shows that if you entrust programs that manage health-related Figure 69. Top Asset varieties in Lost
portable devices to employees, a certain data, as of course do the members of and Stolen Assets breaches (n=76)
percentage of them will either misplace the Healthcare industry. Industries that
their devices or leave them somewhere handle Protected Health Information
that they are vulnerable to theft. Leaving (PHI) tend to have higher regulatory
items in personal vehicles is a recurring requirements for reporting breaches,
theme in the data. People may just do it and therefore we have better visibility
closer to home than before. into these events as well.
Figure 68. Top Action varieties over time in Lost and Stolen Assets breaches
2022 DBIR Incident Classification Patterns 44

Organic free-
range data
Mobile data is something that appears only sparingly in our data,
which seems ironic considering who we are.
Unfortunately (or fortunately), mobile idea about the content of those calls.
phones hover around 1% or less in our About a third of them have little to no
breach dataset with the associated audio or are silent, which sounds to us22
causes being somewhat random. This like vishing (voice phishing) for
is likely due to bias in the data; when a live numbers.
phone is used to phish creds, it’s likely
the email server that gets reported, Another 29% are known scams (with
not the device used to access it. When 7% of the 29% known to be targeting
we see breaches involving malware businesses specifically) and the rest
on mobile phones, it is not uncommon being other stuff or simply unknown.
for the malware to be there to collect
Thankfully it’s not as if the targeting
data. And if that’s your goal, it helps to
of mobile devices is a big surprise to
be quiet and not get caught, especially
the security community. Sandboxed
considering the difficulty it takes to get
OSes and high prices for vulnerabilities
on the devices in the first place.
suggest mobile security inherited a lot
However, when we look at non-incident of hard-fought lessons learned from
data, we get a clearer view of the personal computers (PCs23) and so
role mobile plays in the security security has been incorporated into
ecosystem. Figure 70 gives an idea of mobile devices from the get-go.
the threats that mobile phones see.
We point out in the Social Engineering
Only 42% of devices avoided blocking pattern that 82% of breaches involve
access to any URL while 84% of the human element—something the
devices avoided an unwanted app. silicon isn’t going to be mitigating.
However that means the other 58% Eighteen percent of clicked phishing
of devices had at least one malicious emails come from a mobile device.
URL clicked and 16% of devices had Admittedly, we can’t say if more folks
at least one malware or riskware app click on mobile vs PC since no one’s
installed. While that may not sound phone is narc’ing on them. Still, since
like a lot, a quick look at your Mobile almost a fifth of phishing successes
Device Management console (or a came from mobile devices, that should
company headcount) will tell you those be good enough confirmation that it
numbers can add up rapidly. needs to be within your security estate.
And it’s not just texts tempting the Part of the problem is trying to get
telephonic users. Phone honeypot users to improve their security behavior.
data reveals that 5% of honeypots get One such approach is providing access
at least one call a day, and we’re about to key security information knowledge
90% sure the honeypots don’t need to quizzes within reach of their thumbs in
refinance their student loans or even the form of a mobile app. For one such
own a car with an extended warranty security dashboard app, 66% of users Figure 70. Events detected on mobile
(they prefer leasing). Figure 71 gives an who accepted the terms and conditions devices by type (log scale)
22 Well, not sounds sounds. Well … you get the picture.
23 Yes, we spelled out “PC.” Look, we both know what a PC is, but the kids these days, with their mobile phones and metaverses. Who knows?!
2022 DBIR Incident Classification Patterns 45

never interacted with the dashboard. behavior. The next is helping the user
Of those that did, 99% interacted envision the impact of those risks on
more than once, but as you can see in themselves. Finally, you need to give
Figure 72, the median interaction time users the means to improve, which is
was 15 seconds. Still, about half of folks where training comes in.24 It may feel
came back after minutes, hours, or like throwing spaghetti at the wall to
even months. see what sticks, but sometimes that’s
what is required to make it better.
Making information available to the user
about their specific security risks is
the first step in the journey to changing
Figure 71. Phone honeypot calls by type Figure 72. Length of interaction with a mobile security dashboard
(n > 10,000) (n=22,086, log scale)
24 And if you’re wondering about how, check out the “Changing Behavior” Appendix!
2022 DBIR Incident Classification Patterns 46

Privilege
Misuse
Figure 73. Privilege Misuse incident paths (n=33)
The best
|                 | Summary                                   | Frequency | 275 incidents,       |
| --------------- | ----------------------------------------- | --------- | -------------------- |
| laid plans of   |                                           |           | 216 with confirmed   |
|                 | This pattern is almost entirely insiders  |           | data disclosure      |
using their access maliciously to
Mice and Men
|     | cause breaches. While Financial is    | Threat Actors | Internal (100%),  |
| --- | ------------------------------------- | ------------- | ----------------- |
|     | still the leading motive, Espionage,  |               | External (4%),    |
|     | Convenience and just plain Grudges    |               | Multiple (4%)     |
We get it. You’ve honed your hiring
|     | are still represented. Personal data  |     | (breaches)  |
| --- | ------------------------------------- | --- | ----------- |
processes to a fine edge. You’re well
remains the most common data type
prepared to ensure that you onboard  Actor Motives Financial (78%),
for these breaches, but Medical data
only the most qualified people to join
|     | continues to be sought. |     | Grudge (9%),  |
| --- | ----------------------- | --- | ------------- |
your organization. And yet, things
Espionage (8%),
somehow go wrong despite your best
Convenience (6%)
efforts. Privilege Misuse is the pattern
|     | What is the same? |     | (breaches) |
| --- | ----------------- | --- | ---------- |
where people use the legitimate
Most of the incidents in this pattern
| access granted to them as employees  |     | Data  | Personal (70%),   |
| ------------------------------------ | --- | ----- | ----------------- |
to steal data. Often, they act alone,  result in successful data breaches.  Compromised Other (28%), Medical
but they sometimes act in concert  These actors are still motivated by  (22%), Internal (12%)
with others. Either way, you have a  greed (financial gain), and are stealing  (breaches)
| data breach and must deal with   | Personal data because it is easy   |     |     |
| -------------------------------- | ---------------------------------- | --- | --- |
| the fallout.                     | to monetize.                       |     |     |
2022 DBIR  Incident Classification Patterns 47

It’s not that easy In this pattern the threat actor already
has access to perform their day-to-
Far and away the most common
day duties, therefore, we do not see
action in this pattern is Privilege abuse.
Credentials as the data type affected.
However, Data mishandling also shows
Instead, Personal data (whether of
up, albeit to a much lesser degree, and
customers, employees, or even partners)
is typically associated with the motive
is of the highest interest to those looking
of Convenience. Sometimes people do
to capitalize on their access.
unsafe things to get around a security
control designed to protect the data Medical data is still taken in 22% of
from exposure. While some controls breaches in this pattern. When you
may make it harder for people to get realize that the most common industry
their jobs done, it is important to pair represented in this pattern is Healthcare,
these controls with education to at least that makes sense. In fact, Healthcare
let people know the “why” behind the has had an ongoing problem with
process. Regardless, offering a less Internal actors accessing their data
laborious process that remains secure without a valid reason for a long time.
would be something to consider if your And while it is no longer in the top tier of
organization repeatedly suffers this kind the patterns in Healthcare, it should not
of event. be discounted as a solved problem.
Figure 74. Top Action varieties in Privilege Misuse breaches (n=176)
2022 DBIR Incident Classification Patterns 48

2008 2022
2014
4
Industries

Introduction
If you are a long-time reader this  manages their systems for them. The  number might be, given a large enough
introduction may be redundant, but for  infrastructure, and conversely the  sample. For example, instead of stating
new readers it is worth perusing. This  attack surface, largely drives the risk. “In the Accommodation industry, 92% of
year we looked at 23,896 incidents,  attacks were financially motivated,” we
which boiled down to 5,212 confirmed  Therefore, we caution our readers not  might state that “financially motivated
data breaches. As always, we break  to make inferences about the security  attacks ranged between 86% and 100%.”
these incidents and breaches into their  posture (or lack thereof) of a particular  Check out our riveting Methodology
sector based on how many breaches or
respective industries to illustrate that all  section for far more information about the
incidents their industry reports. These
industries are not created equal. At least  statistical confidence background used
not when it comes to attack surfaces  numbers are heavily influenced by  throughout this report.
and threats. The type of attacks suffered  several factors, including data breach
by a particular industry will have a great  reporting laws and partner visibility.  If you are reading this only for a glimpse
deal to do with what infrastructure they  Because of this, some of the industries  of your industry, our recommendation
have very low numbers, and as with any  is to verify what the top patterns are on
rely upon, what data they handle and
small sample, we must caution readers  the summary table accompanying each
how people (customers, employees and
everyone else) interact with them.       that our confidence in any statistics  industry and also spend some time with
derived from a small number must also  those pattern sections. In addition, we
A large organization whose business  be less.      provide a description of what Center for
model focuses entirely on mobile  Internet Security (CIS) Critical Security
devices where their customers use an  When examining industries with a small  Controls) to prioritize in each industry
app on their phone will have different  sample, we will provide ranges where the  section for ease of reading if you want
actual value may reside. This allows us
risks than a small Mom and Pop  to get straight to strategizing your
to maintain our confidence interval while
| shop with no internet presence, but  |     |     |     |     | security moves. |     |     |
| ------------------------------------ | --- | --- | --- | --- | --------------- | --- | --- |
giving you an idea of what the actual
who use a point-of-sale vendor that
|     | Incidents |     |     | Breaches |     |     |     |
| --- | --------- | --- | --- | -------- | --- | --- | --- |
Industry Total Small (1-1,000) Large (1,000+) Unknown Total Small (1-1,000) Large (1,000+) Unknown
| Total                      | 23,896 | 2,065 | 636 21,195 | 5,212 | 715 | 255 | 4,242 |
| -------------------------- | ------ | ----- | ---------- | ----- | --- | --- | ----- |
| Accommodation (72)         | 156    | 2     | 1 153      | 69    | 1   | 1   | 67    |
| Administrative (56)        | 39     | 5     | 7 27       | 19    | 3   | 5   | 11    |
| Agriculture (11)           | 243    | 1     | 1 241      | 39    | 1   | 0   | 38    |
| Construction (23)          | 127    | 21    | 7 99       | 57    | 8   | 5   | 44    |
| Education (61)             | 1,241  | 112   | 48 1,081   | 282   | 57  | 15  | 210   |
| Entertainment (71)         | 215    | 12    | 5 198      | 96    | 6   | 3   | 87    |
| Finance (52)               | 2,527  | 103   | 50 2,374   | 690   | 56  | 32  | 602   |
| Healthcare (62)            | 849    | 36    | 14 799     | 571   | 14  | 10  | 547   |
| Information (51)           | 2,561  | 59    | 25 2,477   | 378   | 27  | 10  | 341   |
| Management (55)            | 8      | 1     | 2 5        | 2     | 0   | 0   | 2     |
| Manufacturing (31-33)      | 2,337  | 168   | 74 2,095   | 338   | 54  | 22  | 262   |
| Mining (21)                | 231    | 0     | 0 231      | 132   | 0   | 0   | 132   |
| Other Services (81)        | 180    | 16    | 1 163      | 101   | 8   | 1   | 92    |
| Professional (54)          | 3,566  | 1,095 | 144 2,327  | 681   | 263 | 52  | 366   |
| Public Administration (92) | 2,792  | 110   | 88 2,594   | 537   | 74  | 25  | 438   |
| Real Estate (53)           | 118    | 31    | 5 82       | 76    | 19  | 2   | 55    |
| Retail (44-45)             | 629    | 157   | 68 404     | 241   | 54  | 35  | 152   |
| Transportation (48-49)     | 305    | 26    | 38 241     | 137   | 17  | 23  | 97    |
| Utilities (22)             | 172    | 20    | 14 138     | 47    | 14  | 3   | 30    |
| Wholesale Trade (42)       | 166    | 79    | 33 54      | 68    | 38  | 8   | 22    |
| Unknown                    | 5,434  | 11    | 11 5,412   | 651   | 1   | 3   | 647   |
| Total                      | 23,896 | 2,065 | 636 21,195 | 5,212 | 715 | 255 | 4,242 |
Table 2. Number of security incidents and breaches by victim industry and organization size
2022 DBIR  Industries 50

Breaches
Figure 75. Breaches by industry
2022 DBIR Industries 51
nrettaP
noitcA
tessA

Incidents
Figure 76. Incidents by industry
2022 DBIR Industries 52
nrettaP
noitcA
tessA

Accommodation and
Food Services
 SCIAN
27
Summary
| Frequency | 156 incidents, 69 with  |     |     |     |     |
| --------- | ----------------------- | --- | --- | --- | --- |
confirmed data
disclosure
Accommodation and Food Services, while having seen a decrease of System Intrusion
Top patterns System Intrusion,  since 2016, is still victimized by Malware via email and the Use of stolen credentials
|     | Social Engineering  | used against Web application. |     |     |     |
| --- | ------------------- | ----------------------------- | --- | --- | --- |
and Basic Web
Application Attacks
represent
|               |                  |                   | 5-year     | 3-year     | Difference   |
| ------------- | ---------------- | ----------------- | ---------- | ---------- | ------------ |
|               | 90% of breaches  | Patterns in years |            |            |              |
|               |                  |                   | difference | difference | with peers   |
| Threat actors | External (90%),  |                   |            |            |              |
|               | Internal (10%)   | System Intrusion  | Less       | Less       | No change    |
(breaches)
Actor motives Financial (91%),  Social Engineering Greater No change No change
Espionage (9%)
(breaches)
Basic Web
|             |                     |                     | Greater | Greater | No change |
| ----------- | ------------------- | ------------------- | ------- | ------- | --------- |
| Data        | Credentials (45%),  | Application Attacks |         |         |           |
| compromised | Personal (45%),     |                     |         |         |           |
Payment (41%), Other
(18%) (breaches)
The Accommodation and Food Services industry is one of the few industries that
| Top IG1  | Security Awareness  |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- |
saw a drop in terms of System Intrusion. However, it shows similar trends to other
protective
and Skills Training  industries in regard to Basic Web Application Attacks and Social Engineering. They
Controls
(CSC 14), Access
have been on the increase over the last 5 years, and are now a bit closer to the
Control Management
same baseline for the types of attacks that the other industries are experiencing.
(CSC 6), Secure
Configuration of
Enterprise Assets
and Software (CSC 4)
| What is the  | This industry  |     |     |     |     |
| ------------ | -------------- | --- | --- | --- | --- |
same?
continues to be
targeted by financially
motivated criminals
going after Payment
and Personal data.
Figure 77. Top patterns over time in Accommodation and Food Services breaches
2022 DBIR  Industries 53

Figure 78 captures the top Action
varieties found in this industry. This Looking back
is one of the few industries that is In the 2012 DBIR, Accommodation and Food Services represented over
extremely long tailed, with over 80% 54% of our cases and has since dropped to less than 2% of our incidents.
of the breaches including Actions not This represents both a total drop in cases but also a rather dramatic drop in
captured in the top five varieties. While incidents and may be representative of a larger shift in the criminal ecosystem
that might seem imposing, keep in to target and victimize not only the organizations with credit card data but
mind that the vectors are still the usual any organization.
suspects found in the other industries:
Email, Web apps and Desktop
sharing software.
Figure 79. Industry groups represented by percent of breaches (2012 DBIR Figure 3)
Figure 78. Top Action varieties in
Accommodation and Food Services
breaches (n=58)
Figure 80. Top Action vectors in Accommodation and Food Services breaches (n=47)
2022 DBIR Industries 54

Arts, Entertainment
and Recreation
Summary
The System Intrusion and Basic Web Application Attacks patterns exchanged
positions, but the Miscellaneous Errors pattern held on to 3rd place on the podium.
For incidents, Denial of Service attacks remain a problem in the sector, particularly
for the Gambling industry.
This industry mainly covers live performances, and whether dance, theater or
sporting events, the common thread is that none are pre-recorded for later
broadcast. It also includes the gambling industry. One can only imagine the different
attack surfaces that are present for the myriad organization types belonging to this
NAICS code. Something many of them have in common, however, is that at least
a portion of their infrastructure relies on the internet to perform critical functions,
whether that is ticket sales or taking orders (or bets as the case may be). In any
event, when a Denial of Service attack comes calling, it is a very unwelcome guest.
Nevertheless, it is a frequent guest in this sector (particularly in the Gaming
organizations in the APAC region), and represents over 20% of incidents.
With regard to breaches, the three patterns listed in the At-a-Glance table show the
vulnerability of the infrastructure beyond disruption of services. Once the attackers
get in, they can wreak havoc in earnest. These attackers are largely External actors,
with a Financial motive, although there are a small amount of Grudge-motivated
attacks in this sector as well.
The inclusion of the Basic Web Application Attacks is concerning, given the less
complex nature of these attacks. Conversely, the attackers have to try much harder
to gain their prize in the System Intrusion attacks, where ransomware is always a
favored tool. As we have seen in the past, every attacker loves credentials, and will
use them to masquerade as a legitimate employee to evade capture for as long as it
takes to get what they are after.
55
SCIAN
17
Frequency 215 incidents, 96 with
confirmed data
disclosure
Top patterns Basic Web
Application Attacks,
System Intrusion and
Miscellaneous Errors
represent 80% of
breaches
Patterns in years 5-year 3-year Difference
Threat actors External (74%), difference difference with peers
Internal (26%)
(breaches) Basic Web
No change No change No change
Application Attacks
Actor motives Financial (97%),
Grudge (3%)
System Intrusion No change No change Less
(breaches)
Data Personal (66%),
compromised Credentials (49%), Miscellaneous Errors No change No change Greater
Other (23%), Medical
(15%) (breaches)
Top IG1 Security Awareness
protective and Skills Training
Controls
(CSC 14), Secure
Configuration of
Enterprise Assets
and Software (CSC
4), Access Control
Management (CSC 6)
What is the The patterns are the
same? same, but the order is
not. Medical data
continues to be
compromised in
this industry.
2022 DBIR Industries

Figure 81. Patterns over time in Arts and Entertainment breaches
The most commonly taken data is
Personal information (although it is
down from a high last year of 83%) and
Credentials. Oddly enough, Medical
data is still being snarfed up (technical
term) in 15% of the breaches in this
sector. This was similar to last year (at
26%), but it remains a puzzling data Figure 82. Misdelivery vs Misconfiguration in Arts and Entertainment industry Error
breaches (n=16)
type to find in a sector that has no
medical affiliation. It may be that the
data taken is from companies that are
self-insured for their employee medical
needs, and so have a need to store Miscellaneous Errors remain in the
that kind of data, or it could possibly top three patterns again this year
be from some form for Workers (25%). The Misconfiguration error
Compensation data (on the job injuries). was the most common, representing
Additionally, this NAICS code includes approximately 15% of the breaches.
sports teams which could account for It appears this sector simply traded
a certain number of stolen medical one problem for another as Misdelivery
records. Regardless, it is a rather errors (the most common last year)
counterintuitive finding. have dropped considerably.
2022 DBIR Industries 56

Educational Services
Summary
Frequency 1,241 incidents, 282
with confirmed data
disclosure
Educational Services follows an eerily similar trend to the majority of the other industries;
it is experiencing a dramatic increase in Ransomware attacks (over 30% of breaches). In
Top patterns System Intrusion,
addition, this industry needs to protect itself against stolen credentials and phishing
Basic Web
attacks potentially exposing the personal information of its employees and students.
Application Attacks
and Miscellaneous
Errors represent
80% of breaches
Threat actors External (75%),
Internal (25%)
(breaches)
Actor motives Financial (95%),
Espionage (5%)
(breaches)
Data Personal (63%),
compromised Credentials (41%),
Other (23%), Internal
(10%) (breaches)
Top IG1 Security Awareness
Alright, class is back in session, put away your NSYNC Trapper Keeper and get
protective and Skills Training
Controls out a number two pencil, cause you’re about to get schooled on the breaches and
(CSC 14), Access
incidents impacting the Educational Services industries. System Intrusion, Social
Control Management
Engineering and DoS are the leading causes of incidents and System Intrusion,
(CSC 6), Secure
BWAA and Errors lead the way with regard to breaches. Falling along the peak of
Configuration of
the grading curve, this industry also has Use of stolen creds and Ransomware as
Enterprise Assets
the top two action varieties, which is a very dangerous combination. The rumor
and Software
is stolen creds and ransomware quit school due to recess, because they don’t
(CSC 4)
play around.
What is the This industry
same? continues to be
impacted by attacks
targeting their
external infrastructure
and are largely
targeted by External
actors with Financial
motives. However,
Educational Services
also faces errors as
one of the top causes
of breaches.
2022 DBIR Industries 57
SCIAN
16
Patterns in years 5-year 3-year Difference
difference difference with peers
Basic Web
No change Greater Less
Application Attacks
System Intrusion Greater Greater Greater
Miscellaneous Errors No change Less Greater
Figure 83. Top patterns over time in Education breaches

While an erroneous number in a
calculation might result in a few points
2017 Yearbook
off of your homework, the erroneous There’s nothing quite like the feeling of nostalgia that hits you when you’re
end user might result in a data breach. looking over your old yearbook. Signatures and notes from friends long ago,
Thirty four percent of the errors found ahh, the good old days. We get that same feeling when looking back at the 2017
in this industry were from an email sent DBIR and see Cyber-Espionage as the top breach pattern for this industry. No
to the wrong people, or with the wrong worries though, Espionage has not graduated and moved away yet. It shows
attachment. up in 34% of incidents this year. Figure 85 captures the shifts in data and
the somewhat dramatic rise of Espionage that is still all too present today.
While errors may have decreased Unfortunately, unlike your opinionated high school friends on social media, you
over the past three years, they’re still can’t just block espionage from cluttering up your feed.
a relatively normal occurrence that
should be taken seriously, especially
considering the various troves of
data schools handle, we would hate
to have our poor little Bobby Tables’
data leaked.25
Figure 84. Top Action varieties in
Educational Services breaches (n=218)
Figure 85. Percent of breach classification patterns over time within the Education
industry (DBIR 2017 Figure 17)
25 https://xkcd.com/327, a classic.
2022 DBIR Industries 58

Financial and
Insurance
Summary
Frequency 2,527 incidents, 690
with confirmed data
disclosure
The Financial sector continues to be victimized by financially motivated organized crime,
often via the actions of Social (Phishing), Hacking (Use of stolen credentials) and Malware
Top patterns Basic Web
(Ransomware). Finally, Miscellaneous Errors, often in the form of Misdelivery, is still very
Application Attacks,
common as it has been for the past three years in a row.
System Intrusion and
Miscellaneous Error
represent 79%
of breaches.
Threat actors External (73%),
Internal (27%)
(breaches)
Actor motives Financial (95%),
Espionage (5%)
(breaches)
Data Personal (71%),
compromised Credentials (40%),
Other (27%), Bank
(22%) (breaches)
Top IG1 Security Awareness
In 2016 servers were involved in 50% of Financial breaches, as opposed to
protective and Skills Training
90% currently. However, the specific variety of “Server—Web application” has
Controls
(CSC 14), Secure
increased from 12% to 51% over that same timeframe, thus accounting for Basic
Configuration of
Web application Attacks’ position in the top three patterns. A key component of
Enterprise Assets
these attacks is that they usually involve the Use of stolen credentials, which is the
and Software (CSC
number one Action variety in this vertical. These creds may have been obtained in
4), Data Protection
any number of ways, but brute force hacking and credential stuffing are the most
(CSC 3)
likely culprits. One thing is certain, stolen creds and web apps go together like
peanut butter and chocolate.
What is the Basic Web
same? Application Attacks
and Miscellaneous
Errors continue to
play a large part in
breaches for this
vertical as they did
last year.
59
SCIAN
25
Patterns in years 5-year 3-year Difference
difference difference with peers
Basic Web
Greater Greater Less
Application Attacks
System Intrusion Greater Greater Greater
Miscellaneous Errors Greater Greater Greater
2022 DBIR Industries

Figure 86. Patterns over time in Financial and Insurance industry breaches
“I’ll show you “Through the Finally, we would be remiss if we did
not mention that DoS attacks continue
mine if you years…” to be a huge problem and account
for 58% of security incidents in this
show me yours” vertical. That is approximately twice as
System Intrusion has doubled from 14% much as we see in the other industries.
in 2016 to 30% this year. Organized
crime was responsible for only 49% of
The Error variety of “Misdelivery” (16%)
breaches in 2018 vs the 79% we see in
is the second most common action
this report. Availability was affected in
variety in this vertical. Misdelivery is
only 6% of breaches back in 2016, vs
exactly what it sounds like, delivering
14% today, and the discovery method
PII or other sensitive information to the
of Actor disclosure was 5% (in 2016)
wrong recipient. One might expect to
as opposed to the 58% in this year’s
see that variety more often in Public
report. We need hardly say that this is
Sector or Healthcare because, by their
mainly due to ransomware attacks, but
very nature, they send a great deal of
to be on the safe side, we will say
mail. Instead, our data indicates that
it anyway:
Misdelivery is approximately three
times higher in Financial than in the
This is mainly due to ransomware
other industries. We here on the DBIR
attacks. As long as ransomware
team were taken aback by this finding,
continues to be a high profit, low risk
as it would be embarrassing if any
attack, criminals will continue to
unauthorized person were to view
utilize it.
our checks and learn that we make
countless millions for writing this
report each year.26
26 If only.
2022 DBIR Industries 60

Healthcare
 SCIAN
26
Summary
| Frequency | 849 incidents, 571   |     |     |     |     |
| --------- | -------------------- | --- | --- | --- | --- |
with confirmed data
disclosure
The Basic Web Application Attacks have overtaken the Miscellaneous Errors in causing
breaches in this sector.  Errors are still a significant problem.
| Top patterns | Basic Web  |     |     |     |     |
| ------------ | ---------- | --- | --- | --- | --- |
Application Attacks,
Miscellaneous Errors
|     | and System Intrusion  |     |     |     |     |
| --- | --------------------- | --- | --- | --- | --- |
represent 76% of  Patterns in years 5-year  3-year  Difference
|     |     |     | difference | difference | with peers |
| --- | --- | --- | ---------- | ---------- | ---------- |
breaches
| Threat actors | External (61%),  | Basic Web  |         |         |         |
| ------------- | ---------------- | ---------- | ------- | ------- | ------- |
|               |                  |            | Greater | Greater | Greater |
Application Attacks
Internal (39%)
(breaches)
|               |                   | System Intrusion | Greater | Greater | Less |
| ------------- | ----------------- | ---------------- | ------- | ------- | ---- |
| Actor motives | Financial (95%),  |                  |         |         |      |
Espionage (4%),
|     | Convenience (1%),  | Miscellaneous Errors |      |      |         |
| --- | ------------------ | -------------------- | ---- | ---- | ------- |
|     |                    |                      | Less | Less | Greater |
Grudge (1%)
(breaches)
| Data        | Personal (58%),  |                           |     |     |     |
| ----------- | ---------------- | ------------------------- | --- | --- | --- |
| compromised | Medical (46%),   | Insiders? What Insiders?  |     |     |     |
Credentials (29%),
Other (29%)
(breaches) Healthcare is the industry where the internal actor has figured prominently in
breaches since we first began collecting and reporting data. While the make-up of
Top IG1  Security Awareness  the insider breach has moved from being largely malicious Misuse incidents to the
protective
and Skills Training  more benign (but no less reportable) Miscellaneous Errors, we have always been
Controls
(CSC 14), Secure  able to rely on this industry to tell the insider threat story. With the rise of the Basic
Configuration   Web Application Attacks pattern in this vertical, those inside actors no longer hold
of Enterprise Assets
sway. Move over Insiders, the big dogs are here.
and Software (CSC
4), Access Control  Make no mistake (no pun intended) your employees are still causing breaches, but
Management (CSC 6)  they are more than 2.5 times more likely to make an error than to maliciously misuse
their access. Misdelivery and Loss are the most common errors (and they are so
What is the  The top three  close, we’d need a photo finish to determine a winner).
same?
patterns are the
same, but the order is
not. The threat actors
were exactly the
same as last year
(down to the
percentage point).
2022 DBIR  Industries 61

Figure 87. Patterns over time in Healthcare industry breaches
Figure 87 illustrates the change over For the second year, Personal data is
time in patterns for Healthcare. Back compromised more often than Medical.
in 2015, the top pattern was Privilege Do we consider this the norm now
Misuse, followed by Miscellaneous for the one industry with a plethora
Errors. It wasn’t until 2019 that we of medical data? Is this because the
started to see the rise of Basic Web actors are just getting in and getting
Application Attacks, and they have their encryption game on without
clearly become a serious problem regard to the type of records they are
for everyone, not just this industry. rendering inaccessible? Only those in
Healthcare has increasingly become a the industry know for certain if they
target of run-of-the-mill hacking attacks have increased their controls around
and the more impactful ransomware their Medical data but left Personal
campaigns (both from the System data in the waiting room.
Intrusion pattern, which came in third).
With the increase in ransomware,
comes the associated increase of the
discovery method of Actor Disclosure.
It is a bad day when that ransom note
pops up after the encryption has
been triggered, providing convenient
methods of payment for these
customer service-focused threat
groups. (And really, who doesn’t want
to make it easy for their “customers”
to pay them?)
2022 DBIR Industries 62

Information
Summary
Frequency 2,561 incidents, 378
with confirmed data
disclosure System Intrusion moves ahead of Errors and Basic Web Application Attacks to claim the
top spot this year in breaches, meanwhile DDoS maintains its top position in incidents.
Top patterns System Intrusion,
Malware has seen a noticeable rise over the past two years, while Errors appear to be on
Basic Web
the down swing since their rise five years ago.
Application Attacks
and Miscellaneous
Errors represent 81%
of breaches
Threat actors External (76%),
Internal (24%)
(breaches)
Actor motives Financial (78%),
Espionage (20%),
Ideology (1%), Grudge
(1%) (breaches)
Data Personal (66%),
compromised Other (35%),
Credentials (27%),
Internal (17%)
(breaches) Last year, not unlike your boss at your last performance review, we highlighted
the Errors in the Information industry. However, as we can see in Figure 88, there
Top IG1 Security Awareness has been clear progress that we can put on the mid-year review. Errors have
protective and Skills Training experienced a decline since their upswing half a decade ago in 2017.
Controls
(CSC 14), Secure
Configuration of
Enterprise Assets
and Software (CSC
4), Access Control
Management (CSC 6)
What is the Surprisingly, over the
same? last five years Social
breaches have
remained roughly the
same. This may be
because Social
breaches are
targeting customers
resulting in Hacking
breaches (which have
also stayed pretty
level) to the company
due to stolen
credentials.
63
SCIAN
15
Patterns in years 5-year 3-year Difference
difference difference with peers
Basic Web
No change No change Greater
Application Attacks
Miscellaneous Errors Greater Less Greater
System Intrusion Greater Greater Greater
Figure 88. Actions over time in Information industry breaches
2022 DBIR Industries

To maintain the balance however, Misconfiguration, Backdoor or C2, and Finally, Figure 91 provides a look into
Malware has seen a measurable Export Data appearing in more than 4% something else that’s easy to forget:
increase over the past two years. of breaches. In fact, Information is tied botnets. The information industry takes
That is reflected in Figure 89. System for 2nd place in industries by number of the top spot in botnets for the second
Intrusion has jumped to the top in this varieties above 4% at 17 different year running. Botnet breaches are
vertical, even rising above Basic Web Action varieties. often masked at the victim organization
Application Attacks. because they only see the malicious
Figure 90 illustrates the top incidents, login, and not that the bot also stole the
One interesting effect of having System dominated by DDoS attacks and credentials.
Intrusion in the number one position is System Intrusions (which are driven by
that the Information industry contains Ransomware). Please be sure not to
a smorgasbord of Action varieties. Use forget about DDoS–while it is relatively
of stolen creds is the most common, easy to mitigate, it has certainly not
but after that, a legion of varieties gone away.
are present, with Ransomware,
Figure 90. Top patterns in Information
industry incidents (n=2,561)
Figure 89. Patterns in Information Figure 91. Evil Corp botnet breaches by
industry breaches (n=378) industry (n=7,072)
2022 DBIR Industries 64

Manufacturing
 SCIAN
33-13
Summary
| Frequency | 2,337 incidents, 338  |     |     |     |     |
| --------- | --------------------- | --- | --- | --- | --- |
with confirmed data
disclosure
Manufacturing continues to be a lucrative target for espionage, but is also
increasingly being targeted by other criminals via the use of Denial of Service
| Top patterns | System Intrusion,  |     |     |     |     |
| ------------ | ------------------ | --- | --- | --- | --- |
attacks, credential attacks and Ransomware.
Basic Web
Application Attacks
and Social
|     | Engineering  |                   |         |         |              |
| --- | ------------ | ----------------- | ------- | ------- | ------------ |
|     |              | Patterns in years | 5-year  | 3-year  | Difference   |
represent 88% of
|     |     |     | difference | difference | with peers |
| --- | --- | --- | ---------- | ---------- | ---------- |
breaches
Basic Web
| Threat actors | External (88%),  |     | Greater | Greater | Greater |
| ------------- | ---------------- | --- | ------- | ------- | ------- |
Application Attacks
Internal (12%),
Partner (1%)
(breaches)
|               |                   | Social Engineering | Less | Less | Less |
| ------------- | ----------------- | ------------------ | ---- | ---- | ---- |
| Actor motives | Financial (88%),  |                    |      |      |      |
Espionage (11%),
|     |     | System Intrusion | Greater | Greater | Greater |
| --- | --- | ---------------- | ------- | ------- | ------- |
Grudge (1%),
Secondary (1%)
(breaches)
| Data  | Personal (58%),  |     |     |     |     |
| ----- | ---------------- | --- | --- | --- | --- |
Manufacturing, with its hum of machinery churning out the key components that
compromised
Credentials (40%),  make our modern life possible, continues to be a valued target for espionage
Other (36%), Internal  (mostly due to recent indiscriminate supply chain attacks covered in a previous
(14%) (breaches) section). However, it has also become a lucrative target for financially motivated
criminals looking to make a quick dollar.
| Top IG1     | Security Awareness   |     |     |     |     |
| ----------- | -------------------- | --- | --- | --- | --- |
| protective  | and Skills Training  |     |     |     |     |
Controls
(CSC 14), Access
Control Management
(CSC 6), Secure
Configuration of
Enterprise Assets
and Software (CSC 4)
| What is the  | System intrusion   |     |     |     |     |
| ------------ | ------------------ | --- | --- | --- | --- |
| same?        | and Basic Web      |     |     |     |     |
Application Attacks
continue to be among
the main patterns this
industry faces.
Figure 92. Top patterns over time in Manufacturing breaches
2022 DBIR  Industries 65

In previous reports, Manufacturing
was largely targeted for their juicy
schematics and secrets. For example,
in 2016 over 55% of the incidents in
this vertical involved Espionage (Figure
93), but that has been lower over the
last few years. Or, conversely, the spies
have upped their game to the point that
they are no longer exposed.
DoSing against
the machine
Figure 93. Motives over time in Manufacturing industry incidents
For an industry where availability equals
productivity, it’s interesting to see the
yo-yo pattern that has been taking
place with DoS attacks over the years.
While DoS attacks initially reached its
former peak in the 2018 report (over
40% of incidents), it’s been increasing
since 2019 and now accounts for
approximately 70% of incidents, which
puts it more in line with what we see in
other industries. This rise of DoS, while
unlikely to prevent those key assets
from actually running the manufacturing
process, is still worth keeping in mind
as integration increases between the
OT side of the house and the IT side.
With regard to the breaches impacting
this sector, one can find the usual
suspects, such as stolen credentials
(39%), Ransomware (24%) and Figure 94. Patterns over time in Manufacturing industry incidents
Phishing (11%) demonstrated in Figure
95. These types of breaches appear
to be impacting everyone regardless
of industry. Implementing safeguards,
such as the ones listed in the At-a-
Glance table, should be a priority for
this vertical. Otherwise, you might find
your organization unexpectedly seizing
up due to a certain someone with an
anime girl avatar.
Figure 95. Top Action varieties for Manufacturing industry breaches (n=259)
2022 DBIR Industries 66

Mining, Quarrying,
and Oil & Gas
Extraction + Utilities
Frequency 403 incidents, 179
with confirmed data
disclosure
Top patterns Social Engineering,
System Intrusion
and Basic Web
Application Attacks
represent 95% of
breaches
Threat actors External (96%),
Internal (4%)
(breaches)
Actor motives Financial (78%),
Espionage (22%)
(breaches)
Data Credentials (73%),
compromised Personal (22%),
Internal (9%)
(breaches)
Top IG1 Security Awareness
protective and Skills Training
controls
(CSC 14), Access
Control Management
(CSC 6), Account
Management (CSC 5)
What is the This industry
same? continues to be
targeted by financially
motivated actors
as well as actors
committing
espionage.
67
SCIAN 22+12
Summary
The Mining and Utilities industry faces similar types of attacks as other industries
such as those targeting credentials and leveraging Ransomware, but in addition has
a high rate of social engineering attacks like Phishing.
Patterns in years 5-year 3-year Difference
difference difference with peers
Basic Web
No change No change Less
Application Attacks
Social Engineering No change No change No change
System Intrusion No change No change Less
Mining, Quarrying, and Oil & Gas Extraction + Utilities (or MQOGEU as we like to
say) simply rolls off the tongue. It is an interesting “combined” industry has had a
higher number of engineers. This is perhaps fitting as it seems to be under barrage
from the other form of “engineers”—the Social Engineers. This industry has had a
higher rate of Social Engineering breaches than their peers.
Figure 96. Top patterns over time in MQOGEU breaches
2022 DBIR Industries

And it shows, as more than 60% of all
breaches are Phishing (Figure 97),
followed by stolen credentials
(potentially gathered by Phishing) and
Ransomware (potentially tangential to
Phishing). Given the key importance of
this industry to our everyday well-being,
we certainly hope that those credentials
aren’t the only thing keeping our utilities
and mining operations safe, especially
since that’s one of the most commonly
breached data types.
Considering the high prevalence of
Phishing and credential attacks, it’s not
too surprising to have Email servers
as this industry’s most commonly
breached asset, followed by Web
application and Desktop. Even though
the infrastructure that runs these
complex systems isn’t traditional IT
infrastructure, the company can still be
exposed to the very same threats as
any other organization. Figure 97. Top Action varieties in Figure 98. Top Asset varieties in
MQOGEU breaches (n=153) MQOGEU breaches (n=130)
2022 DBIR Industries 68

Professional, Scientific
and Technical Services
Summary
Frequency 3,566 incidents, 681
with confirmed data
disclosure
Denial of Service attacks are a serious problem in this industry, and while they rarely
result in a data breach, they can still have a significant impact. The System Intrusion
Top patterns System Intrusion,
attack pattern is in the first position again this year, while Social attacks are less
Basic Web
prominent, but still in the top three.
Application Attacks
and Social
Engineering
represent 89% of
breaches
Threat actors External (84%),
Internal (17%),
Multiple (1%)
(breaches)
Actor motives Financial (90%),
Espionage (10%)
(breaches)
Data Credentials (56%),
compromised Personal (48%),
Other (26%), Internal
(14%) (breaches) Services denied
Top IG1 Security Awareness
protective and Skills Training
As a NAICS code with the name of Professional, Scientific and Technical Services
controls
(CSC 14), Access
might imply, this sector relies on their internet presence to provide their highly
Control Management
skilled offerings to their customers. This means that when they are hit with a DoS
(CSC 6), Secure
attack, particularly the higher volume distributed varieties, they definitely feel the
Configuration of
impact. This past year has been a hard one for this sector, with the DoS attacks
Enterprise Assets
accounting for almost half of the incidents recorded. And even though this type of
and Software
attack rarely leads to a reportable data breach, it can still do significant damage to
(CSC 4)
the victim.
What is the The top three attack
same? patterns remain
System Intrusion, The devil you know
Basic Web
Application Attacks
and Social Moving to breaches, the System Intrusion pattern remained at the top of our
Engineering, but they pyramid, while Basic Web Application Attacks and Social Engineering switched
have changed order places. So, the same players remain on the field, they are simply playing
compared to last different positions.
year’s report.
2022 DBIR Industries 69
SCIAN
45
Patterns in years 5-year 3-year Difference
difference difference with peers
Basic Web
No change No change No change
Application Attacks
Social Engineering Less Less No change
System Intrusion Greater Greater No change

Figure 99. Patterns over time in Professional, Scientific and Technical Services breaches
The perpetrators of these top three Days gone by
attack patterns tend to be External.
The Internal actor breaches were down
this year by comparison to last year’s Looking back over the years in this
report. Surprisingly we saw a small sector, the Miscellaneous Errors
uptick in the multiple actor breaches in pattern was in the top three. However,
this sector this year. These are when as Figure 99 shows, in 2019, the
an external actor recruits an internal or System Intrusion pattern began its
partner actor to help them out with the meteoric rise to the top, eventually
breach activities. Sometimes they are far surpassing Errors. This sector
paid for their troubles, and sometimes mirrors the overall dataset in terms of
it is a more subtle form of influence by the top attack patterns. The top three
an acquaintance or significant other here are the top three patterns in the
exerting pressure on the person with full dataset, so clearly, these patterns
the access to data. Either way, the are holding sway in a number of
result is a breach that can be more business categories.
difficult to detect, since it is someone
on the inside facilitating the access
under the guise of conducting their
regular duties.
2022 DBIR Industries 70

Public
Administration
Summary
The System Intrusion pattern is the newest big dog to arrive on the scene in this
sector. Employees continue to be a cause of breaches in this vertical, although
Internal actors are seven times more likely to make a mistake than to commit a
malicious act that causes a breach.
Here and now
The System Intrusion pattern has drop-kicked the Social Engineering pattern right out
of the “top three” club. This was quite the coup, considering the Social Engineering
pattern was in the top spot last year. In part, this may be attributed to some prominent
and far-reaching supply chain breaches that came to light last year.
As the Social Engineering pattern fell, the Basic Web Application Attacks stepped in
to fill the vacuum. Miscellaneous Errors remained in the middle spot, with the trio of
Misconfiguration, Misdelivery and Loss nearly tied for what caused the most error-
based breaches in this sector.
The occurrence of errors in this industry accounts for the prevalence of breaches
caused by the Internal actor. While there was a smattering of Misuse breaches in
this sector, Internal actors are about seven times more likely to make a mistake that
causes a breach than they are to do something malicious.
We have said before how popular Credentials are as a data type to be raided.
However, this year’s data showed a drop from 2021’s report, when it was 80% in
this industry. Personal was only 18% last year, but has now catapulted into the
top spot.
71
SCIAN
29
Frequency 2,792 incidents, 537
with confirmed data
disclosure
Top patterns System Intrusion,
Miscellaneous Errors
and Basic Web
Application Attacks
represent 81% of
breaches
Patterns in years 5-year 3-year Difference
Threat actors External (78%), difference difference with peers
Internal (22%)
(breaches) Basic Web
No change Greater Less
Application Attacks
Actor motives Financial (80%),
Espionage (18%),
Miscellaneous Errors No change Less Less
Ideology (1%), Grudge
(1%) (breaches)
System Intrusion Greater Greater Greater
Data Personal (46%),
compromised Credentials (34%),
Other (28%), Internal
(28%) (breaches)
Top IG1 Security Awareness
protective and Skills Training
controls
(CSC 14), Access
Control Management
(CSC 6), Account
Management (CSC 5)
What is the Miscellaneous Errors
same? remain in the top
three patterns in the
same place as last
year.
2022 DBIR Industries

Figure 100. Patterns over time in Public Administration breaches
Step into
Figure 101 illustrates the change in the
Espionage-motivated actors in this
my raggedy industry since 2017. As you can see,
when the Espionage motive fell, the
DeLorean Financial-motivated attacks rose. It
appears that the Public Administration
sector has joined the rest of us in being
In honor of our 15-year anniversary, targeted by criminals looking to make a
we wanted to take a look back in time buck. Welcome to the party, pal!27
at what has changed in this sector.
Just three years ago, the top motive
was Espionage, at 66% of breaches.
Five years ago, it was 64%, which
illustrates that it has been a persistent
challenge for Government entities. This
makes sense, when you consider that
regardless of which Government entity
we are talking about, someone wants
to know what they’re up to. Speaking of
malicious—we found that the Espionage
motive is up from 4% from last year to
18% this year. Internal breaches also
increased from last year, and we have
the motive of Grudge popping up in our
list for a change.
Figure 101. Actor motives over time in Public Administration breaches
27 Admit it, you read this in John McClane’s voice.
2022 DBIR Industries 72

Retail
 SCIAN 54-44
Summary
| Frequency | 629 incidents, 241  |     |     |     |     |
| --------- | ------------------- | --- | --- | --- | --- |
with confirmed data
disclosure
The Retail industry is experiencing the same types of attacks they suffered last year:
Use of stolen credentials, Phishing and Ransomware.
| Top patterns | System Intrusion,  |     |     |     |     |
| ------------ | ------------------ | --- | --- | --- | --- |
Social Engineering
and Basic Web
|     | Application Attacks  |     |     |     |     |
| --- | -------------------- | --- | --- | --- | --- |
represent 84% of  Patterns in years 5-year  3-year  Difference
|     |     |     | difference | difference | with peers |
| --- | --- | --- | ---------- | ---------- | ---------- |
breaches
| Threat actors | External (87%),  | Basic Web  |           |      |      |
| ------------- | ---------------- | ---------- | --------- | ---- | ---- |
|               |                  |            | No change | Less | Less |
Application Attacks
Internal (13%)
(breaches)
|               |                   | Social Engineering | No change | Greater | Greater |
| ------------- | ----------------- | ------------------ | --------- | ------- | ------- |
| Actor motives | Financial (98%),  |                    |           |         |         |
Espionage (2%)
(breaches)
|             |                     | System Intrusion | Greater | No change | Greater |
| ----------- | ------------------- | ---------------- | ------- | --------- | ------- |
| Data        | Credentials (45%),  |                  |         |           |         |
| compromised | Personal (27%),     |                  |         |           |         |
Other (25%), Payment
(24%) (breaches)
Our society, indeed the entire globe, has seen an astounding amount of change over
the last couple of years. The Retail industry, on the other hand, has not, at least when
| Top IG1  | Security Awareness  |     |     |     |     |
| -------- | ------------------- | --- | --- | --- | --- |
it comes to breaches. As tempting as it was to simply cut and paste our findings for
| protective  | and Skills Training  |     |     |     |     |
| ----------- | -------------------- | --- | --- | --- | --- |
this industry from last year’s report, we bravely refrained from doing so. Nevertheless,
| controls | (CSC 14), Access  |     |     |     |     |
| -------- | ----------------- | --- | --- | --- | --- |
while the needle has not moved very much from when we last looked at it, there are a
Control Management
few noteworthy findings.
(CSC 6), Secure
Configuration of
Social attacks, roughly split between Phishing (53%) and Pretexting (47%), have
Enterprise Assets and
been on the rise over the last few years in the Retail industry: 7% in 2016, 13%
Software (CSC 4)
in 2018, 29% this year. This accounts for Social Engineering’s position in the top
three patterns. Therefore, as one might expect, Credentials are the top data type
| What is the  | These organizations  |     |     |     |     |
| ------------ | -------------------- | --- | --- | --- | --- |
compromised in this vertical. In many cases those Credentials are later utilized to
| same? | continue to be  |     |     |     |     |
| ----- | --------------- | --- | --- | --- | --- |
hack into servers and load ransomware (47%). Then the criminals sit back and
impacted by a variety
wait for a big payday.
of threat actors that
leverage a range of  One interesting finding this year is that the Malware enumeration of “Capture app
tactics such as
data” in the Retail industry is 7 times higher than the other industries. This goes
deploying malware to
some way to explain why the System Intrusion pattern is ranked at first place in
capture credit cards
this industry. The “Capture app data” functionality is one that we commonly see in
being processed by
Magecart-type attacks, in which the attacker will typically exploit a vulnerability, use
webforms and more  stolen credentials to gain access to an e-commerce server and then just chill there
common tactics like  and take a little sumpin’ sumpin’ for themselves, almost always payment card data.
phishing.
2022 DBIR  Industries 73

Figure 102. Patterns over time in Retail industry breaches
Finally, when a company in the Retail
industry learns that they have become
a victim, it’s via fraud detection
mechanisms (e.g., Common Point
of Purchase [CPP] or law enforcement)
more than any other industry. This is
perhaps a rather intuitive finding given
the fact that Retail is responsible
for so many transactions, but it is
noteworthy nonetheless.
Figure 103. Actions in Retail industry
breaches (n=241)
2022 DBIR Industries 74

Very Small Business
Cybercrime
Protection Sheet
If you own or manage a very small You may have heard the term “Business
Frequency 832 incidents, 130
business, we offer the following Email Compromise” in news articles.
with confirmed data
recommendations or best practices. We They typically involve Phishing and/or
disclosure
suggest you print out or tear out this Pretexting, and can be quite convincing,
Top patterns System Intrusion, section and refer to it when a concern (such as an invoice that looks like it
Social Engineering appears. comes from a known supplier but has a
different payment account, or an email
and Privilege Misuse
from a business partner saying they’re
represent 98% of
in a pinch and need a quick payment
breaches
What are the made on their behalf). While most come
Threat actors External (69%), in through email, criminals have also
Internal (34%), most common employed the telephone to convince
Multiple (3%) their target that this is a legitimate
(breaches) threats facing request. The criminal element often run
their enterprise just like a legitimate
Actor motives Financial (100%) my business? business and may even take advantage
(breaches) of criminal call centers (yes, these exist)
to help lend credence to their ploy.
Data Credentials (93%), The number one action type in our
compromised Internal (4%), Bank dataset for very small businesses are Phishing is a type of social attack
(2%), Personal (2%) ransomware attacks. Ransomware
(breaches) is a type of malicious software that
encrypts your data so that you
When cybercrime makes the news, it is
cannot view or utilize it, and once
typically because a large organization
the ransomware is triggered the
has fallen victim to an attack. However,
threat actor demands a (frequently
contrary to what many may think,
large) payment to unencrypt it.
very small organizations are just as
This is where having those offline28
enticing to criminals as large ones,
backups come in handy.
and, in certain ways, maybe even more
so. Threat actors have the “we’ll take The second most common is the
anything we can get” philosophy when Use of stolen credentials. Attackers
it comes to cybercrime. These incidents can get your credentials (username
can and have put small companies and password) via many different
out of business. Therefore, it is crucial methods. Brute force attacks (where
that even very small businesses attackers use automation to try
(10 employees or less) should take numerous combinations of letters,
precautions to avoid becoming a symbols and numbers to guess your
target. Large organizations have large credentials), various types of malware
resources, which means they can afford (thus the value of having an up-to-date
Information Security professionals and Antivirus), reused passwords from
cutting-edge technology to defend another site that has been hacked
themselves. Very small businesses and last but not least, social attacks
on the other hand have very limited such as Phishing and Pretexting.29
resources and cannot rely on a trained
Figure 104. Action varieties in 1 to 10
staff. That is why we wrote this section.
employee organization breaches (n=61)
28 If you’re unsure what “offline” means here, see “What to do to avoid becoming a target” below.
29 If you’re not familiar with “phishing” or “pretexting,” it’s okay. Keep reading for the definitions.
2022 DBIR SMB 75

(usually via email) in which the attacker
tries to fool you into doing something
What to do to avoid becoming a target
you should not, such as providing them
with your user name and password or 1. Use two-factor authentication30
clicking on a malicious link. Examples
2. Do not reuse or share passwords31
include “click here to reset your
password” or download an invoice, 3. Use a password keeper/generator app
view the pdf attachment, verify your
4. Be sure to change the default credentials of the Point of Sale (PoS)
bank account number, etc. These
controller or other hardware/software
attacks can be extremely realistic and
are often very hard to identify. 5. Ensure that you install software updates promptly so that vulnerabilities
can be patched
Pretexting is the human equivalent of
6. Work with your vendors to be sure that you are as secure as you can be,
Phishing. Typically, the threat actor
and that they are following these same basic guidelines
attempts to create a dialog with the
victim by impersonating a business 7. Keep a consistent schedule with regard to backups and be sure to
partner, a bank employee, or a superior maintain offline backups—meaning that they are not on a device connected
in your own organization in order to to a computer
gain access to login information. 8. Ensure that the built-in firewall is switched on for user devices such as
The end game for Pretexting is usually laptops and desktops (“on” may not be the default)
the automated transfer of funds from
9. Use antivirus software, for all your devices. Smart phones, tablets and
your organization to the criminal’s
credit card swipers are just as important as laptops and computers. It
bank account.
won’t catch everything, but it will help
10. Do not click on anything in an unsolicited email or text message
11. Set up an out of band method for verifying unusual requests for data
How do I know
or payments
I have become 12. Make sure the computer used for financial transactions is not used for
other purposes such as social media or email
a victim? 13. Use email services that incorporate phishing and pretexting defenses and
use a web browser that warns you when a website may be spoofed
Watch for anything strange or out of
the ordinary. For example, you might
see unexpected charges on your bank
Who do I Familiarize yourself with these
statement or phone bill. Keep an eye
resources, and draw up a plan for
out for transactions on your credit
card that you don’t recognize. You may contact if I learn what steps you will take if you find
your organization has become a victim.
receive comments from friends about
emailed requests for them to buy a I have been a Plan this ahead of time instead of
waiting until your company’s “hair” is
gift card. You may receive phone calls
asking for your password or credit victim of on fire. Even if it is just a document that
contains the contact information for all
card number, or a request to change
of your vendors and your bank’s fraud
the account number or how you pay cybercrime?
department, it is a place to start. Print
a regular vendor or client. All of these
it off and post it somewhere you can
things are warning signs that something
access it easily. Don’t just keep it on
malicious might be happening. Think of • A large range of resources for
your computer—it might be unavailable
your computer like a car–if it suddenly many different situations is available
as part of the attack.
won’t start, runs slower or makes a through https://fightcybercrime.org/.
weird noise, it’s time to have an expert This website provides information
Some planning on your part, along with
take a look. Finally, with threats such on where to go and what to do in the
a bit of educating the people most likely
as ransomware the threat actor will event of a cyber incident
to encounter these kinds of attacks,
actually alert you that your data has
• Scam Spotter provides simple, easy- can go a long way in helping to make
been encrypted.
to-understand information about your small company safer.
how to recognize common scams:
https://scamspotter.org/
• If you are in the United States, your
state’s Attorney General’s office
website may have resources for you
as well
30 This adds an additional layer to just the username and password combination. It may be a code that is texted to your registered cell phone, the use of
an authenticator app like Google or Microsoft Authenticator, or the use of a little device that you plug into a USB drive when prompted. If your vendors
do not offer two-factor authentication (also called multi-factor authentication or MFA), start lobbying for them to accommodate it.
31 Not between people and not between applications or websites. A password keeper makes this easier.
2022 DBIR SMB 76

5
Regions
2008 2022
2018

Introduction
to Regions
This edition of the DBIR marks the third year that we have analyzed incidents and
presented them from a macro-region perspective. It is our hope that our readers
find this more global view of cybercrime helpful and informative. As we have
mentioned in the past, we have greater or lesser visibility into a given region
based on numerous factors such as contributor presence, regional disclosure
regulations, our own caseload and so on.
If you reside and work in a part of the world that is not mentioned in the following
pages, please contact us about becoming a data contributor and encourage other
organizations in your area to do the same, so that we may continue to expand and
refine our coverage each year. It is important to keep in mind that if you do not
see your region represented here it does not necessarily mean that we have no
visibility at all into the region, but simply that we do not have enough incidents in
that geographic location to be statistically relevant for a stand-alone section.
We define the regions of the world in accordance with the United Nations M49
standards, which combines the super-region and sub-region of a country together.
By so doing, the regions we will examine are as follows:
APAC: Asia and the Pacific, including Southern Asia (034), South-eastern Asia
(035), Central Asia (143), Eastern Asia (030) and Oceania (009)
EMEA: Europe, Middle East and Africa, including North Africa (002), Europe and
Northern Asia (150) and Western Asia (145)
NA: Northern America (021), which primarily consists of breaches in the United
States and Canada
LAC: Latin America and Caribbean, which consists of breaches in South America
(005), Central America (013) and Caribbean (029)
2022 DBIR Regions 78

Figure 105. Incidents and breaches by region
2022 DBIR Regions 79
nrettaP
noitcA
tessA

Asia Pacific
(APAC)
Regions with records
Frequency 4,114 incidents, 283
Regions without records
with confirmed data
disclosure
Top patterns Social Engineering,
Basic Web Application
Attacks and System
Intrusion represent
98% of breaches
Threat actors External (98%),
Internal (2%)
(breaches)
Actor motives Financial (54%),
Espionage (46%),
Secondary (1%)
(breaches)
This year in APAC we see the well- incidents. This is interesting in that our
Data Credentials (72%),
known trifecta of Hacking (58%), data does not reflect a high number
compromised Internal (26%),
Social (48%) and Malware (36%) of defacements in other areas of the
Secrets (18%), Other
taking center stage. The majority of world. And while a nuisance, they
(11%) (breaches)
incidents were perpetrated by usually have a lesser impact than a
What is Basic Web Application attackers with Financial (81%) motives. ransomware case for example.
the same? Attacks and Social However, State-affiliated (19%) and
Engineering continue Nation-state (1%) actors with the motive
to be persistent of Espionage (19%) were rather
threats for this region. common in APAC as well.
The predominant Hacking action was
Summary ‘Use of stolen credentials’ (83%) being
mostly used to compromise a web
application (60%). The social attacks in
APAC experiences a high
this region accounted for approximately
number of Social and Hacking
twice the number we saw in other
related attacks, but has a much
lower number of Ransomware regions, and consisted almost
cases than other areas. exclusively of Phishing (99%). Similar to
last year, we saw a comparatively low
number of ransomware cases in APAC.
Ransomware was involved in 10% of
breaches in APAC as opposed to the
overall dataset average of 25%.
There were a substantial number of
defacement attacks in this region this
year (over 2,800), which pushed the
Figure 106. Top patterns in Asia Pacific
attribute of “Integrity” up to 75% of
breaches (n=283)
2022 DBIR Regions 80

Europe, Middle East
and Africa (EMEA)
Frequency 1,093 incidents, 307
with confirmed data
disclosure
Top patterns Social Engineering,
System Intrusion and
Basic Web
Application Attacks
represent
97% of breaches
Threat actors External (97%),
Internal (3%)
(breaches) Regions with records
Actor motives Financial (79%), Regions without records
Espionage (21%)
(breaches)
Data Credentials (67%),
compromised Internal (67%),
Secrets (20%), Other
(18%) (breaches)
What is The patterns are the
the same? same top three, but
they have rearranged
themselves in order.
External actors
continue to
perpetrate the vast
The EMEA region, covering Europe, the Middle East and Africa, has seen a sharp
majority of breaches
increase in the Social Engineering pattern in the past year (to almost 60% of
in this region.
breaches). While the same three patterns continue to afflict the region, Social
Engineering was in third place in last year’s data. At the same time, we saw Basic
Web Application Attacks plummet (Figure 108 on the next page). In last year’s
Summary report, they accounted for over 50% of the breaches in this region, but have now
dropped to the 15% range. The more complex System Intrusion pattern, however,
continues to thrive and still holds second place at 30%.
The rise of the Social Engineering
pattern in this region illustrates
Credential theft remains a problem in this region, and regardless of how threat
the need for controls to detect
actors obtain those credentials (the rise of Social Engineering provides a likely
this type of attack quickly.
answer), once they are acquired they use them against your infrastructure. With the
Credential theft remains a large
problem as well, as illustrated in foothold this provides, attackers are then able to leverage their access to obtain
the continued persistence of the more Credentials via Phishing, or utilize details gained from company emails to craft
Basic Web Application Attacks realistic pretexts as part of BEC attacks.
pattern in EMEA.
2022 DBIR Regions 81

Figure 108. Patterns over time in Europe, Middle East and Africa breaches
Threat actors are most commonly
attacking Web application servers
as a means to gaining access (since
it is the most easily reached via the
internet) along with Email servers. Email
servers provide both an opportunity
to mine the account’s contents for
interesting internal company data
for espionage, and a venue to gain
more access via phishing other
employees. In terms of the people
being targeted, unsurprisingly, phishers
like to compromise people in Finance
since they have convenient access
to the organization’s money transfer
capabilities. If they can convince
one of those targets to send them Figure 107. Top Action varieties in
currency under the guise of a legitimate Europe, Middle East and Africa
transaction, they don’t need to worry breaches (n=283)
about monetizing data.
2022 DBIR Regions 82

Northern America
(NA)
Frequency 4,504 incidents,
1,638 with confirmed
data disclosure
Top patterns System Intrusion,
Social Engineering
and Basic Web
Application Attacks
represent 90% of
breaches
Threat actors External (90%),
Internal (10%),
Regions with records
Multiple (1%)
(breaches)
Actor motives Financial (96%),
Espionage (3%),
Grudge (1%)
(breaches)
Data Credentials (66%),
compromised Internal (21%),
Personal (20%),
Other (20%)
(breaches)
Since our dataset shows a strong Northern American (NA) bias, we find that as this
What is The top three
the same? patterns remain the region goes, so goes the dataset. This is nowhere more evident than when looking
same, only their at the top three patterns for Northern America. These three mirror the top patterns
order has changed. for the full dataset. The bias is due to a combination of things. First of all, the breach
External actors disclosure laws in NA are quite robust, and they continue to evolve. Determining
continue to hold all the places you must report a breach to in Northern America almost requires
sway in breaches in a decoder ring and Magic 8 Ball. In addition to this, most of our data sharing
this region. contributors have excellent visibility into the NA region, in both private and public
sectors. And, frankly, our English is excellent, our French and Portuguese passable,
but beyond that our linguistic facilities falter. All of this means we have very good
data on this region–more so than any other.
Summary
The System Intrusion pattern
has become the dominant
pattern in this region. Social
Engineering gave way as System
Intrusion increased, but there
remains a large problem with
social actions such as Phishing
in Northern America. Basic Web
Application Attacks continue to
beset organizations here as well.
2022 DBIR Regions 83

Figure 109. Patterns over time in Northern America breaches
We can see in Figure 109, that while With our Social Engineering pattern
the Social Engineering pattern has comes Social actions, of course. The
held sway for some time as the top most common is a straight-up Phish,
pattern in breaches, last year showed a with Pretexting coming in second
change. The top pattern is now System (Figure 111).
Intrusion, which is also where most
of the Ransomware cases reside. It is
surely no secret that Ransomware has
been rising for several years and has
become quite prominent in our data.
In fact, for cases where malware is
present, Ransomware is by far the
most common variety (Figure 110).
Increasingly over the past several
Figure 112. Top Confidentiality data
years, this attack has the one-two variety in Northern America breaches
punch of causing both a loss of access (n=944)
to the data, and the need to report a
data breach as the actors have also
taken a copy of the organization’s data.
In attacks that result in confirmed data
breaches, the data type most frequently
Figure 111. Top Social varieties in
stolen is, unsurprisingly, Credentials.
Northern America breaches (n=264)
They are stolen more often than the
next two most common varieties
combined. Perhaps Credentials are like
Pretexting takes more work, so it
popcorn, you cannot steal just one.
may be employed against higher-
value targets. We see this in cases
where a Business Email Compromise
attack offers up a fake invoice or
something similar to attempt to get
either money or banking info from the
target. As expected, people in the
Finance function of the organization
are likely to be the target of more
advanced attacks.
Figure 110. Top Malware varieties in
Northern America breaches (n=647)
2022 DBIR Regions 84

Latin America and
the Caribbean (LAC)
Frequency 92 incidents, 24 with
confirmed data
disclosure
Top patterns System Intrusion
Denial of Service and
Social Engineering
represent 88% of
incidents
Threat actors External (95%),
Internal (7%), Multiple
(1%) (incidents)
Regions with records
Actor motives Financial (92%), Regions without records
Convenience (3%),
Espionage (2%),
Grudge (2%), Other
(2%) (incidents)
Data System (51%),
compromised Credentials (40%),
Internal (21%), Other
(12%) (incidents)
What is Financially motivated
the same? actors continue to be
the main threat actors
in this region.
Water might spin in the opposite direction in the Southern Hemisphere, but
Summary breaches and incidents seem to go down just as they do elsewhere. Unfortunately,
our data collection for this section of the world is still very sparse, and we continue
to be in need of partners to help us round out our understanding of what’s going
Much like the rest of the world,
on with our friends in the South. If your organization operates in this region please
Latin American businesses face
reach out and join us.
attacks targeting the functioning
of their businesses, such as
Ransomware and Denial of
Service attacks. These attacks
account for 37% and 27% of
incidents respectively.
2022 DBIR Regions 85

Figure 113 provides a breakdown of
what industries have been breached
in Latin America. While we don’t
necessarily have a large number
of breaches, we certainly have a
diverse collection of compromised
organizations, with approximately
20% of victims not from the top seven.
Just like their Northern America
counterparts, Latin America
industries face the looming threat
of Ransomware. This attack type
accounts for more than 30% of their
incidents. This is followed by the
ever-present DoS attack. This region
of the world also experiences its fair
share of Phishing attacks and Stolen
credentials, which we realize may be
beginning to sound like a broken
record. Or, erg … would a buffering
looping advert be the modern
equivalent? At this point we’re
beginning to get the feeling that
some of these attacks are universal
to anyone who has some form of
Figure 113. Top industries in Latin Figure 114. Top Action varieties in Latin
internet presence.
America and the Caribbean incidents America and the Caribbean incidents
(n=92) (n=89)
2022 DBIR Regions 86

2008 2022
2020
DIRne avp tea os Btrit rg eaatciohn s
6
IWncridaepn-tu p
Classification
Patterns
87
0202

This concludes
another installment
of the Data Breach
Investigations Report.
As always, it is our hope that you have brighter tomorrow! We hope to see you
found the information herein to be all again next year. We will close with a
informative, actionable and enjoyable line from a former report that we feel is
to read. While we do our best to bring particularly apropos:
the occasional smile to our readers,
we assure you that we take cybercrime
“Be well, be prosperous, and be
seriously indeed. The five of us on the
DBIR team feel truly fortunate to be prepared for anything.”
in this fight alongside each and every
one of you. We will do our best to keep
providing you with whatever insight we
can from our data, and we wish all of
you the greatest success. Here is to a
2022 DBIR Wrap-up 88

Year in review
Year in review
January As the New Year began, the Verizon Threat Research Advisory Center (VTRAC) was still tracking the
SolarWinds-related campaigns. Tools emerged for security teams to use in Azure/Microsoft O365
environments. January’s patch Tuesday included one remote code execution vulnerability in Windows
Defender that was already being exploited in the wild (zero-day). SonicWall was investigating an attack
exploiting “probable zero-day vulnerabilities” in certain secure remote access products. Researchers
reported a fourth malware used in the SolarWinds operation. “Raindrop” is a digital cousin to the
Teardrop malware. Raindrop was installed only on select targets and delivered Cobalt Strike. After
zero-day attacks, Apple released security updates for three vulnerabilities in iOS/iPadOS. The best
news in January came when Europol closed down Emotet’s infrastructure redirecting 1.6 million victim
systems to servers controlled by law enforcement.
February Google kicked off February with Chrome browser updates to mitigate one zero-day. SonicWall, Cisco,
Fortinet and Palo Alto Networks all released patches and updates to VPN and remote access products.
SonicWall’s CVE-2021-20016 was already being exploited. Two more zero-day vulnerabilities were
patched on patch Tuesday, one each by Microsoft and Adobe. CERT-FR reported a supply-chain
compromise of Centrion by the Russian Sandworm threat actor that exhibited commonalities with the
2020’s SolarWinds Orion and Accellion attacks. Two days before the Super Bowl, the fresh water plant
for a small city in Florida was briefly breached. One processing chemical was manipulated but quickly
detected and corrected. IT security at the plant did almost everything wrong: the attacker entered via
TeamViewer with a shared static password on a Windows 7 computer.
March March roared in with out-of-cycle updates for four zero-day vulnerabilities in Microsoft Exchange that
had been initially exploited in January. At least 30,000 Exchange servers were reported to be victims of
Hafnium, a newly-labeled APT-grade threat actor aligned with the national security interests of China.
The flaws were dubbed, “ProxyLogon.” Scanning and exploitation quickly surged. Other APTs and other
threat actors breached unpatched Exchange servers. Microsoft patched 89 vulnerabilities including CVE-
2021-26411, a zero-day in Internet Explorer exploited by a North Korean threat actor targeting security
researchers. The month closed with Apple releasing patches for a zero-day vulnerability in Apple iOS/
iPadOS/WatchOS.
April In early April, the VTRAC collected reports of attacks by APTs from China and Russia targeting
Japanese manufacturing and the German Bundestag respectively. The most significant shift in risk
was due to zero-day exploitation of an authentication bypass vulnerability in Ivanti Pulse Secure
SSL VPN appliances. Microsoft patched 114 vulnerabilities, one of which was exploited before patch
Tuesday. The US government formally attributed the SolarWinds Orion operation to the Russian SVR
intelligence service and their APT29 or Nobelium threat actor. SITA, a communications and IT vendor
for almost all of the world’s airlines, was the victim of a data breach that compromised data for millions
of passengers. It was among the largest data breaches of the year.
2022 DBIR Year in review 89

May May began with one of 2021’s milestone breaches: Colonial Pipeline was compelled to shut down
operations of their pipeline to contain a DarkSide ransomware attack. Several states suffered from fuel
shortages. Even after paying the 75 Bitcoin (~US$5 million) ransom, the closure lasted six days. On the
same day Colonial resumed operations, DarkSide announced they were ceasing operations, releasing
decryptors to their affiliates and claiming that a portion of the group’s infrastructure was disrupted by an
unspecified law enforcement agency. A month later, the FBI seized 63.7 Bitcoin (~US$2.3 million due to
declining Bitcoin valuation). May’s zero-day vulnerabilities were one vulnerability in MacOS, one in Adobe
Reader and four vulnerabilities in Android. A threat actor self-identifying as “Fancy Lazarus,” a tongue-
in-cheek combination derived from names of a Russian and a North Korean APT, began an extortion
DDoS campaign. Japanese conglomerate, FujiFilm and the world’s largest meat packer, JBS Foods, both
suffered business interruptions caused by REvil ransomware.
June North Korean APT Kimsuky breached the network of the South Korean Atomic Energy Research
Institute in June. Threat actors stole source code from Electronic Arts by first infiltrating the
company’s support channel on Slack to bypass the company’s multi-factor authentication. Microsoft
reported APT29 targeted IT, think tanks and government organizations using credential harvesting
attacks. Six zero-day vulnerabilities were among 50 patched on Microsoft Tuesday. Apple patched
two zero-days in iPadOS and iOS and Google patched one in Chrome browser.
July Hours before the USA’s Independence Day holiday, REvil ransomware abused Kaseya Virtual Systems
Administrator (VSA) to attack Managed Security Service Providers that controlled the infrastructure of
thousands of companies. No one knows how many of the millions of end point systems were encrypted.
A few days later, the REvil threat actors closed their darknet website and ceased infecting new victims.
Before the end of the month, the BlackMatter ransomware debuted announcing: “The project has
incorporated in itself the best features of DarkSide, REvil, and LockBit.” Attacks exploiting a total of 15
zero-day vulnerabilities in five product families were reported in July. Cloudflare mitigated a 17.2 million
request per second DDoS attack on a financial industry customer. The attack was a 30 second burst
launched from 20,000 bots. Microsoft discovered a Chinese threat actor targeting SolarWinds Serv-U
software with a Zero-day exploit.
August August 5th at Black Hat, a “researcher” revealed how he chained two April and one May vulnerabilities
in Windows to create the “ProxyShell” attack. Mass scanning for vulnerable Exchange servers ensued.
Cybereason reported on “DeadRinger,” a campaign targeting Asian telecom providers. Cybereason
found links to no less than five Chinese threat actor groups. Microsoft patched 51 vulnerabilities including
“exploitation detected” for one zero-day. Italian energy company ERG and Accenture were the victims of
LockBit 2.0 ransomware. T-Mobile reported a breach of PII from about 40 million former or prospective
customers. The Poly Network, a “DeFi” or decentralized finance platform that works across blockchains,
said that an attacker stole about $600 million in cryptocurrencies.
2022 DBIR Year in review 90

September Just in time to ruin the Labor Day holiday in the United States, threat actors began exploiting a one-week
old vulnerability in Atlassian Confluence servers. Most threat actors installed cryptominers but before
the end of the month, VTRAC collected intelligence for payloads including webshells akin to the TTPs
of APT actors. On Labor Day, Microsoft released an out-of-cycle advisory for zero-day exploitation of a
vulnerability in the Windows browser rendering engine. Microsoft advised: “Keep antimalware products
up to date,” but did not release patches until a week later, on the eve of Patch Tuesday. Iowa farm services
provider NEW Cooperative was hit with BlackMatter ransomware and a $5.9 million ransom demand.
CISA and the FBI urged organizations to patch a vulnerability in Zoho ManageEngine ADSelfService Plus
that APTs had been using as a zero-day exploit to target defense contractors, academic institutions, and
other entities. Google patched five vulnerabilities being exploited in zero-day attacks on Chrome browser.
Zero-day attacks drove Apple to patch three vulnerabilities in iOS/iPadOS and MacOS.
October The month began with accelerated patching to mitigate zero-day attacks on a vulnerability in Apache
HTTPD, the internet’s #2 (after Nginx) web server. After the fix in Apache 2.4.50 was found to be
“insufficient,” and that it introduced a new vulnerability that was, in turn, exploited almost immediately.
Apache released version 2.4.51. Zero-day attacks also struck Microsoft, Apple and the Chrome browser.
The REvil ransomware operation shut down again after an unknown person hijacked their Tor payment
portal and data leak blog. CrowdStrike published an analysis of the threat actor known as “LightBasin”
which had been targeting companies in the telecommunications sector since 2016. CrowdStrike did not
attribute LightBasin to a nation-state. A “cyber event” shuttered Schreiber Foods, a multibillion-dollar
dairy company for three days. This would affect the availability of cream cheese in the United States for
the holiday season. CISA/FBI/NSA issued a joint alert detailing the TTP of BlackMatter ransomware. The
ransomware had been targeting multiple US critical infrastructure organizations since July 2021. Eighteen
days later BlackMatter closed down after transferring its current victims to LockBit 2.0.
November Robinhood Markets said a hacker tried to extort the financial services company following a breach of
data for 7 million customers. The actor targeted 10 customers to collect “extensive account details.”
Emotet returned, using TrickBot for distribution and launched a worldwide email spam campaign
delivering malicious documents. Researchers believe that the Conti ransomware gang was behind the
botnet’s return. Google’s monthly Android update addressed a local privilege escalation vulnerability
under “limited targeted exploitation.” Microsoft released advisories for 55 vulnerabilities including two
that were already being exploited. Ukraine’s security service, the SSU, identified five Russian FSB
officers as operators behind the Gamaredon threat actor.
December The Apache Foundation patched a critical remote code execution vulnerability in the widely employed
Log4j library. Within days, security researchers discovered indications of exploitation that began nine
days before the patch announcement. The VTRAC collected intel about attacks exploiting two previously
unknown vulnerabilities in Zoho ManageEngine. Zero-day attacks impacted one Windows and one
Chrome browser vulnerability respectively. The APT29 (Nobelium) actor maintained the high operational
tempo it reached for the SolarWinds compromise one year earlier. Reports detailed several cyber-
espionage campaigns tied to the APT. “In most instances, post compromise activity included theft of
data relevant to Russian interests.”
2022 DBIR Year in review 91

2008 2022
2021
7
Appendices
Appendices

Appendix A:
Methodology
One of the things readers value Non-committal 1 Direct recording of paid external
most about this report is the forensic investigations and
level of rigor and integrity we disclaimer related intelligence operations
conducted by Verizon using
employ when collecting,
the VERIS Webapp
analyzing and presenting data.
We would like to reiterate that we make
no claim that the findings of this report 2 Direct recording by partners
Knowing our readership cares about
are representative of all data breaches using VERIS
such things and consumes this
in all organizations at all times. Even
information with a keen eye helps keep
3 Converting partners’ existing
though we believe the combined
us honest. Detailing our methods is an
schema into VERIS
records from all our contributors
important part of that honesty.
more closely reflect reality than any
First, we make mistakes. A column of them in isolation, it is still a sample. All contributors received instruction to
transposed here; a number not updated And although we believe many of the omit any information that might identify
there. We’re likely to discover a few findings presented in this report to be organizations or individuals involved.
things to fix. When we do, we’ll list appropriate for generalization (and our
Some source spreadsheets are
them on our corrections page: https:// conviction in this grows as we gather
converted to our standard spreadsheet
www.verizon.com/business/resources/ more data and compare it to that of
formatted through automated mapping
reports/dbir/2022/corrections/ others), bias exists.
to ensure consistent conversion.
Second, we check our work. The same Reviewed spreadsheets and VERIS
way the data behind the DBIR figures The DBIR Webapp JavaScript Object Notation
can be found in our GitHub repository,32 (JSON) are ingested by an automated
as with last year, we’re publishing process workflow that converts the incidents
our fact check report there as well. and breaches within into the VERIS
It’s highly technical, but for those JSON format as necessary, adds
interested, we’ve attempted to test Our overall process remains intact missing enumerations, and then
every fact in the report. and largely unchanged from previous validates the record against business
years.33 All incidents included in this logic and the VERIS schema. The
Third, science comes in two flavors: report were reviewed and converted (if automated workflow subsets the data
creative exploration and causal necessary) into the VERIS framework and analyzes the results. Based on the
hypothesis testing. The DBIR is to create a common, anonymous results of this exploratory analysis, the
squarely in the former. While we may aggregate data set. If you are unfamiliar validation logs from the workflow, and
not be perfect, we believe we provide with the VERIS framework, it is short discussions with the partners providing
the best obtainable version of the for Vocabulary for Event Recording the data, the data is cleaned and re-
truth, (to a given level of confidence and Incident Sharing, it is free to use, analyzed. This process runs nightly for
and under the influence of biases and links to VERIS resources are at the roughly two months as data is collected
acknowledged below). However, beginning of this report. and analyzed.
proving causality is best left to
randomized control trials. The best The collection method and conversion
we can do is correlation. And while techniques differed between
correlation is not causation, they are contributors. In general, three basic
often related to some extent, and methods (expounded below) were
often useful. used to accomplish this:
32 https://github.com/vz-risk/dbir/tree/gh-pages
33 As does this sentence.
2022 DBIR Appendix A 93

Incident data 1 Samples sizes smaller than five exclude incidents and breaches
are too small to analyze affecting individuals that cannot be tied
to an organizational attribute loss. If
Our data is non-exclusively multinomial, 2 We won’t talk about count or your friend’s laptop was hit with Emotet
meaning a single feature, such as percentage for small samples. it would not be included in this report.
“Action,” can have multiple values (i.e., This goes for figures too and is
“social,” “malware” and “hacking”). why some figures lack the dot for Lastly, for something to be eligible
This means that percentages do the median frequency for inclusion into the DBIR, we have
not necessarily add up to 100%. For to know about it, which brings us to
example, if there are 5 botnet breaches, 3 For small samples we may talk several potential biases we will
the sample size is 5. However, since about the value being in some discuss next.
each botnet used phishing, installed range, or values being greater/less
keyloggers and used stolen credentials, than each other. These all follow
there would be 5 social actions, 5 the confidence interval approaches Acknowledge-
hacking actions and 5 malware actions, listed above
adding up to 300%. This is normal, ment and
expected and handled correctly in our
Incident
analysis and tooling. analysis of bias
Another important point is that when eligibility
looking at the findings, “Unknown” is Many breaches go unreported (though
equivalent to “Unmeasured.” Which is our sample does contain many of
to say that if a record (or collection of For a potential entry to be eligible for those). Many more are as yet unknown
records) contains elements that have the incident/breach corpus, a couple of by the victim (and thereby unknown to
been marked as “Unknown” (whether it requirements must be met. The entry us). Therefore, until we (or someone)
is something as basic as the number of must be a confirmed security incident can conduct an exhaustive census of
records involved in the incident, or as defined as a loss of Confidentiality, every breach that happens in the entire
complex as what specific capabilities a Integrity, or Availability. In addition world each year (our study population),
piece of malware contained), it means to meeting the baseline definition we must use sampling. Unfortunately,
that we cannot make statements about of “security incident” the entry is this process introduces bias.
that particular element as it stands assessed for quality. We create a
in the record—we cannot measure subset of incidents (more on subsets The first type of bias is random
where we have too little information. later) that pass our quality filter. The bias introduced by sampling. This
Because they are “unmeasured,” details of what makes a “quality” year, our maximum confidence is
they are not counted in sample sizes. incident are: +/- 0.7% for incidents and +/- 1.4%
The enumeration “Other,” however, is for breaches, which is related to our
counted, as it means the value was • The incident must have at least sample size. Any subset with a smaller
known but not part of VERIS. Finally, seven enumerations (e.g., threat sample size is going to have a wider
“Not Applicable” (normally “NA”) may actor variety, threat action category, confidence margin. We’ve expressed
be counted or not counted depending variety of integrity loss, et al.) across this confidence in the complementary
on the claim being analyzed. 34 fields OR be a DDoS attack. cumulative density (slanted) bar
Exceptions are given to confirmed charts, hypothetical outcome plot
This year we have again made liberal data breaches with less than seven (spaghetti) line charts, quantile dot
use of confidence intervals to allow enumerations plots and pictograms.
us to analyze smaller sample sizes. • The incident must have at least one
We have adopted a few rules to help known VERIS threat action category The second source of bias is sampling
minimize bias in reading such data. (hacking, malware, etc.) bias. We strive for “the best obtainable
Here we define ‘small sample’ as less version of the truth” by collecting
than 30 samples. In addition to having the level of details breaches from a wide variety of
necessary to pass the quality filter, the contributors. Still, it is clear that we
incident must be within the timeframe conduct biased sampling. For instance,
of analysis, (November 1, 2020, to some breaches, such as those publicly
October 31, 2021, for this report). The disclosed, are more likely to enter our
2021 caseload is the primary analytical corpus, while others, such as classified
focus of the report, but the entire breaches, are less likely.
range of data is referenced throughout,
notably in trending graphs. We also
2022 DBIR Appendix A 94

Breaches Breaches Data subsets
We already mentioned the subset
of incidents that passed our quality
requirements, but as part of our
analysis there are other instances
where we define subsets of data. These
subsets consist of legitimate incidents
that would eclipse smaller trends if left
in. These are removed and analyzed
separately, though they may not be
written about if no relevant findings
were, well, found. This year we have
two subsets of legitimate incidents
that are not analyzed as part of the
overall corpus:
Figure 115. Individual contributions Figure 116. Individual contributions
per action per actor 1 We separately analyzed a subset
of web servers that were identified
as secondary targets (such as
Breaches Breaches taking over a website to spread
malware)
2 We separately analyzed botnet-
related incidents
Both subsets were separated out the
last five years as well.
Finally, we create some subsets to
help further our analysis. In particular,
a single subset is used for all analysis
within the DBIR unless otherwise
stated. It includes only quality incidents
as described above and excludes the
two aforementioned subsets.
Figure 117. Individual contributions Figure 118. Individual contributions per
per asset attribute Non-incident
data
The above four figures are an attempt aggregating several other sources, so
to visualize potential sampling bias. not actual single contributions. It also
Each radial axis is a VERIS enumeration occurs along most axes, limiting the Since the 2015 issue, the DBIR includes
and we have stacked bar charts bias introduced by that grouping of data that requires analysis that did
representing our data contributors. indirect contributors. not fit into our usual categories of
Ideally, we want the distribution of “incident” or “breach.” Examples of
sources to be roughly equal on the The third source of bias is confirmation non-incident data include malware,
stacked bar charts along all axes. Axes bias. Because we use our entire dataset patching, phishing, DDoS and other
represented by only a single source for exploratory analysis, we cannot test types of data. The sample sizes for
are more likely to be biased. However, specific hypotheses. Until we develop non-incident data tend to be much
contributions are inherently thick tailed, a collection method for data breaches larger than the incident data, but from
with a few contributors providing a beyond a sample of convenience this is fewer sources. We make every effort
lot of data and a lot of contributors probably the best that can be done. to normalize the data, (for example
providing a few records within a certain weighting records by the number
area. Still, we mostly see that most axes As stated above, we attempt to mitigate contributed from the organization so all
have multiple large contributors with these biases by collecting data from organizations are represented equally).
small contributors adding appreciably diverse contributors. We follow a We also attempt to combine multiple
to the total incidents along that axis. consistent multiple-review process and partners with similar data to conduct
when we hear hooves, we think horse, the analysis wherever possible. Once
You’ll notice a rather large contribution not zebra.34 We also try to review analysis is complete, we try to discuss
on many of the axes. While we’d findings with subject matter experts in our findings with the relevant partner
generally be concerned about this, the specific areas ahead of release. or partners so as to validate it against
they represent contributions their knowledge of the data.
34 A unique finding is more likely to be something mundane such as a data collection issue than an unexpected result.
2022 DBIR Appendix A 95

Appendix B: VERIS
and Standards
to them with the Safeguards that can creating repeatable pen tests or control
protect them from the attacks within validations, or communicating to
While the DBIR is celebrating its 15th
those patterns. Within each industry leadership, attack paths and graphs are
birthday, VERIS (the data standard
section, organizations can find the difficult to create, share and analyze.
underlying the DBIR) is creeping up
Implementation Group 1 set of controls
to the ripe old age of 12. The standard
that they can use as a starting point to The DBIR team, with MITRE CTID and
was born out of necessity as a means
improve their defenses based on the its participants, hope to change that
of cataloging in a repeatable manner
top patterns for that industry. with the Attack Flow project. Attack
the key components of an incident. This
Flow is a data schema for capturing
enables analysis of what happened,
MITRE ATT&CK both the causal path of an attack as
who was impacted and how it occurred.
MITRE’s ATT&CK has become one well as the contextual data around it
Since then it has grown and matured
of the defining ways of capturing as it “flows.” Because breaches fan
into a standard that can be adopted by
technical tactical information in terms out and then come back together, go
many different types of stakeholders.
of what attackers do as part of their down a path and come back to a server,
VERIS is tailored to be a standard that
attack process. This rich dataset not Attack Flow supports arbitrary graphs
provides not only ease of communication,
only includes the specific techniques, of actions and assets interacting.
but also a connection point to other
but also the software, groups and Because we all need to know different
industry standards and best practices,
mitigations associated with each things about the attack, it uses a
such as the Center for Internet Security
technique, and as of earlier this year, knowledge graph structure to capture
(CIS) Critical Security Controls and
the associated VERIS components. To the context of the flow. And because
MITRE Adversary Tactics, Techniques
assist organizations with translating we all organize differently, it supports
& Common Knowledge (ATT&CK). We
the technical tactical information multiple namespaces. So, for example,
realize that there isn’t going to be one
into strategic insights, Verizon you could use VERIS Actions, MITRE
universal framework (or language or well,
collaborated with partners at the ATT&CK actions, organization specific
anything) to rule them all, but we certainly
Center for Threat Informed Defense actions, or even a combination of all
believe in the importance of peaceful
(CTID) and created the official VERIS of the above as part of your attack
co-existence between all the frameworks
to ATT&CK36 mapping, available free path analysis.
that have enabled the growth of this
of charge to anyone with an internet
community. Below are some of the great
connection. The mapping data is With Attack Flow, we now have a
projects and connection points that exist
represented in Structured Threat format we can use to share non-atomic
with VERIS and it is our hope that the
Information eXpression (STIX) STIX data. Digital Forensics and Incident
standard will bring more players to
format, includes tools and scripts to Response (DFIR) folks could document
the cybersecurity table.
update the mapping and also has a an incident as a flow. Detection vendors
visualization layer that can be imported could use it to create a signature.
CIS Critical Security Controls into ATT&CK37 Navigator. By providing Control validation tools can use it to
The CIS Critical Security Controls35 (CIS this mapping, we hope that the various simulate the incident. The Security
CSC) are a community-built, prioritized stakeholders of the organization can Engineering team can use it to build
list of cybersecurity best practices that communicate and share their needs in attack surface graphs and plan
help organizations of different maturity a consistent fashion. mitigations. And they all can use the
levels protect themselves against threats. structure to create communications to
The CIS CSC aligns well with VERIS, as Attack Flow leadership, and all be able to share the
the DBIR is built to help organizations One thing you may notice in the DBIR same underlying data with each other
catalogue and assess cybersecurity is that outside of a few small areas in a standardized but flexible structure.
incidents. This mapping connects the such as the Timeline section, we do not If that sounds like something you could
dots between the bad things that are discuss the path the attack takes. This get behind, check out the MITRE
happening and things that can help is because non-atomic data (like paths project at https://github.com/center-
protect the organizations. Since 2019 and graphs of actions) is really hard, for-threat-informed-defense/attack-
we’ve published a mapping document for us and the rest of the information flow and the DBIR team’s graph based
that can help organizations crosswalk security ecosystem. Whether it’s tools for working with it at https://
the patterns that are most concerning describing breaches, writing signatures, github.com/vz-risk/flow.
35 https://www.cisecurity.org/controls
36 https://github.com/center-for-threat-informed-defense/attack_to_veris/
37 https://oasis-open.github.io/cti-documentation/stix/intro
2022 DBIR Appendix B 96

Figure 119. CIS to pattern mapping
2022 DBIR Appendix B 97
lortnoC
Pattern

Appendix C:
Changing Behavior
In 2021 we reported that the human • A population of people you are phishing,” “Read a comic book and
element impacted 85% of breaches, interested in. (If the test was run took a nap,” etc.)
which decreased slightly to 82% this only in a healthcare company or in
• Random assignment. (“200
year. Unfortunately, strong asset a specific division, the population
employees were picked to participate
management and a stellar vulnerability should be “Employees of healthcare
in the study. 100 were randomly
scanner aren’t going to solve this one. companies” not “Anyone.”)
assigned the control and 100 were
• A measurable outcome that can be randomly assigned the intervention.”)
Instead, you’re going to need to change
proven or disproven. (Such as “More
the behavior of humans, and that is • The conditions of the test should
correct answers on a questionnaire
quite an undertaking. Regardless of also be shared. (“Participants were
about phishing delivered 1 day after
how you plan on doing it (be it giving sent the control or intervention via
training,” or “Fewer people clicked
them a reason to change, providing the company training tool as annual
the phishing email,” etc.)
training or a combination of the two), mandatory training.”)
you will need a way to tell if it worked, • An intervention to test to see if it
and that normally means running a test. changes the outcome. (“Watch a This test may be something run
Here’s a cheat-sheet of things that your 15-minute video on not clicking specifically for you or a test the trainer
internal department or vendor who is phishing.”) already ran. As long as the population,
responsible for conducting the training outcome, etc. are close to yours, it
• A control that provides a baseline for
should provide to you so you can doesn’t matter.
the outcome. (“Received no training,”
determine if it is paying off:
“Read a paragraph of text about
Intervention
Population
Population is split into 2 groups Outcomes for both
by random assignment groups are measured
Control
= Same behavior = Changed behavior
Figure 120. Randomized control test
2022 DBIR Appendix C 98

The manner in which the results are • What if some folks just refused • There should also be qualitative
reported is just as important as how the to take the training? That’s called questions. Sometimes you don’t
testing was conducted. Here are a few dropout and is important to the know what you don’t know.38 In that
things you should expect in the results: results. The results should show case, there should be an open-ended
who dropped out (preferably by full question about the training in addition
• A result with a confidence interval. name so they can be shamed in front to the more objective outcomes. It
(If 10 folks in the control clicked of their peers – okay, not really). also gives a chance to ask questions
the phishing email and only 1 in the (“Twenty percent of technically like “Do you have formal education
intervention, 10-1 = 9 people we savvy employees didn’t take the or a job in a computer-related field?”
thought would click, but didn’t. That’s intervention training, while only 2% And you can see the importance
a 9/10 or 90% effectiveness.) But didn’t take the control training.”) of this in the dropout bullet above.
that one number doesn’t tell the Dropout can occur for any of the Asking “Is there anything else you’d
whole story. What if some of those other characteristics recorded like us to know?” might reveal that
were flukes? The result should come (industry, world region, department, while the training was effective, many
with a range (such as 70% to 100% age, etc.) and if major differences folks found it highly offensive.
effective at 95% confidence) similar are found, the results should be
to the DBIR ranges. (Btw, if the range broken out by those characteristics Unfortunately, there’s no way to
includes 0%, there’s a chance the as well. (“People changed 98% in guarantee something works. But, if
training didn’t actually do anything.) tech savvy folks, but only 70% in you’re getting the information above
If the outcome question was yes/ non-tech savvy.”) (Population, Outcome, Intervention,
no, then just a confidence level will Control, Random, Conditions) and
do. (“People changed due to the (Results, When, Dropout, Qualitative)
intervention with 98% confidence.”) you can be reasonably confident you’re
getting something for your effort.
• Since results can vary over time, you
So, remember those easy acronyms:
should know when the result was
POICRC and RWDQ!
measured. “The result was 30 days
after the intervention.”
38 Often referred to as the Rumsfeld paradox.
2022 DBIR Appendix C 99

Appendix D:
U.S. Secret Service
Evolution of Investigative
David Smith
Assistant Director Methodology to Thwart an
U.S. Secret Service
Everchanging Cybercriminal
Jason D. Kane Landscape
Special Agent in Charge
Criminal Investigative Division
U.S. Secret Service
The ways in which we live, work and interact with each other has changed
dramatically the last few years. The increased use of Internet platforms during the
COVID-19 pandemic clearly demonstrates our growing economic dependence on
information technology, and with that increased risk of cybercrime. Transnational
cyber criminals continue to expand their capabilities, and their ability to cause
harm—regardless of if they are financially or politically motivated.
In terms of criminal activity, 2021 experienced a growth in crimes involving
cryptocurrencies. This includes digital extortion schemes (including ransomware),
theft of credentials or private keys that control substantial value in digital assets,
manipulation of decentralized finance (DeFi) systems, and new money laundering
methods that enable a wide variety of illicit activity. Transnational criminals are
increasingly using cryptocurrency and other digital assets, rather than traditional
physical assets or the intermediated financial system. Cryptocurrencies even found
their way into Superbowl advertisements. What was once a niche market is now a
growing part of modern life – investing, trading, and for illicit activity as well.
Since its creation in 1865, the U.S. Secret Service has continuously evolved its
investigative strategies and methods to protect our nation’s financial system. We are
no longer chasing counterfeiters on horseback but are now focused on preventing
cyber fraud by identifying and arresting cybercriminals worldwide. In 2010, when
the Secret Service first joined in developing the DBIR, the foremost risk we were
seeing was the theft of payment card and PII data for use in fraud. As this year’s
report shows that risk is still present, but we are seeing development of new
schemes by those who illicitly exploit the Internet.
To keep pace with evolving criminal activity, the U.S. Secret Service focuses on
partnering to enable businesses and law enforcement to take effective actions to
mitigate risk. The DBIR is a key part of this—providing recommendations derived
from analysis of aggregated incident reports. We also aid our partners and prevent
cyber incidents through the work of our Cyber Fraud Task Forces, and the over
3,000 state, local tribal and territorial (SLTT) law enforcement personnel we trained
at the National Computer Forensics Institute (NCFI) in FY 2021. We coordinate
these activities globally through a dedicated group of investigators in our Global
Investigative Operations Center (GIOC) focused on achieving the most effective
outcomes—from recovering and returning stolen assets to victims to apprehending
those responsible.
2022 DBIR Appendix D 100

This past year clearly demonstrated criminals defrauded relief programs.
The U.S. Secret Service, while the increasing impact ransomware In response, the U.S. Secret Service
focused on thwarting criminal is having on businesses, critical named a National Pandemic Fraud
activity today, has already infrastructure and national security. Recovery Coordinator to focus on
The most prolific ransomware partnering with financial institutions
started to train and prepare for
networks are Russian-speaking, to prevent and recover fraudulent
the cybercrimes of the future.
though this crime is not limited to one payments. These efforts resulted in
country or region. According to one the U.S. Secret Service recovering
industry estimate, 74% of ransomware more than $1.2 billion, the return of
payments were Russian affiliated. We more than $2.3 billion of fraudulently
have also seen the use of destructive obtained funds, and over 100 arrests.
malware, which is functionally similar
to ransomware, but lacks a means for As the world becomes more digitized,
payment. This dynamic, coupled with in addition to being connected to each
the limited cooperation of some states other through technology, we are
in countering ransomware, illustrates connected to a wide array of devices,
a growing risk which blurs distinctions such as the internet of things (IoT).
politically and financially motivated Other emerging technologies that may
cybercrimes. This risk reinforces why soon be the targets of cybercriminals
partnership is essential in improving include quantum cryptography, 5G
cybersecurity by both improving the wireless technology and Artificial
resilience of computer systems and Intelligence (AI). These technologies
apprehending the threat actors. have the potential to improve lives and
open new lines of communication.
Despite transnational cybercrime being Conversely, cybercriminals will seek
a daunting challenge, the U.S. Secret ways to use these technologies for
Service relentlessly pursues these malicious gains. The U.S. Secret
cases. In 2021, the Secret Service Service, while focused on thwarting
led or participated in numerous multi- criminal activity today, has already
national operations to counter cyber started to train and prepare for the
criminal networks. For example, we cybercrimes of the future.
conducted a multinational operation
with Dutch Police and Europol to arrest Preventing cybercrime requires a
multiple individuals responsible for multi-pronged strategy including
ransomware attacks affecting over increasing cybersecurity resilience
1,800 victims in 71 countries. In total, and pursuing criminals and seizing
Secret Service responded to over 700 illicit gains to deter and prevent
network intrusions and prevented over future crimes. Both of these efforts
$2.3 billion in cyber financial losses last are strengthened by the analysis of
fiscal year. aggregated incident reports, and
evidence-based recommendations
Identity theft and fraud continues the DBIR provides. In 2022, the U.S.
to be a core activity of transnational Secret Service looks forward to further
cyber criminals—it provides a strengthening our partnerships, to
means to convert stolen personally stay ahead of our changing use of
identifiable information into profit. technology, the efforts of criminals to
The COVID-19 pandemic created new exploit it, and ensure there is no safe
opportunities for this sort of fraud, as place for cyber criminals to hide.
2022 DBIR Appendix D 101

Appendix E:
Ransomware Pays
In past reports, we have talked at length about the cost of
ransomware and other breaches to victims. However, we have
never examined what the economics look like for the threat actor.
This alternate point of view might provide some useful insights.
To that end, we have combined the value
chain targeting and distribution data,
phishing test success rate data, criminal
forum data, and ransomware payment
data to estimate what the business looks
like from the criminal’s side.
First, let’s examine the cost of access.
Figure 121 illustrates the cost of hiring
(criminal) professional services to do
the actor’s dirty work. These (and larger
criminal organizations with internal staff
for access) are likely going for riskier,
bigger-payout attacks.
The small-time criminal is less of a
techie and more of a manager. They
are trying to minimize costs so will not
invest in professional services. Instead,
they buy access products outright in the
Figure 121. Cost of skilled intrusion services (log scale).
form of credentials, emails for phishing,
Based on 3,000 simulations of criminal forum data.
vulnerabilities, or botnet access. Figure
122 gives an idea of the costs. Instead
of $100,000, the majority of access
doesn’t even cost a dollar. This is
because most access is email which is
incredibly cheap, even when the median
click rate is only 2.9%. While purchasing
access directly in the form of access to
a bot, login credentials, or knowledge
of a vulnerability are also included, it’s
email that steers the ship.
Figure 122. Simulated cost of access (log 100 scale)
(Phishing, Credentials, Vulnerabilities and Botnets)
2022 DBIR Appendix E 102

Contrast Figure 122 with the profits in
Figure 123. Sixty percent of ransomware
incidents had no profit and aren’t shown
in the figure. A large portion had a profit
near one dollar. However, the median is
just over $100. Figure 124 shows what
those same profits look like over time.
After 300 simulated ransoms the actor
has over $600,000 in income.39
To see if this was an anomaly, we
simulated 500 ransomware actors and
1.4% of them showed a loss.40 However,
the median profit after 300 incidents
was $178,465, with the top simulated
earner making $3,572,211.
The takeaway is that ransomware is
more of a lottery41 than a business. You
gamble on access, win the lottery 40%
Figure 123. Simulated profit from ransomware incidents (log scale)
of the time, and get a payout from a few
bucks to thousands of dollars. But for
something more actionable, focus on
the access. If an actor has to pay for
services to break in rather than just an
access product, you’ve made yourself
much less of a target. Use antivirus
to remove bots; implement patching,
filtering and asset management to
prevent exposed vulnerabilities; and
standardize two-factor authentication
and password managers to minimize
credential exposure. Lastly, with email
being the largest vector, you can’t ignore
the human element. Start with email and
web filtering followed by training. (See
the Changing Behavior Appendix for a
recommendation on how to tell if your
training is working.)
Figure 124. Profit for a simulated ransomware actor over time
39 We assume tax-free.
40 I suppose not everyone can be good at business. Even criminals.
41 As Erick Galinkin also suggests in “Winning the Ransomware Lottery: A Game-Theoretic Model for Mitigating Ransomware Attacks,”
https://doi.org/10.48550/ arXiv.2107.14578
2022 DBIR Appendix E 103

Appendix F:
Contributing
Organizations
| A   | D   | J   |
| --- | --- | --- |
Akamai Technologies Defense Counterintelligence Security  Jamf
Agency (DCSA)
| Ankura |     | JPCERT/CC  |
| ------ | --- | ---------- |
Dell
Anomali
Digital Shadows
| Apura Cybersecurity Intelligence |     | K   |
| -------------------------------- | --- | --- |
DomainTools (formerly
| AttackIQ |                    | K-12SIX—(K-12 Security   |
| -------- | ------------------ | ------------------------ |
|          | Farsight Security) | Information Exchange)    |
Atos
|     | Dragos, Inc. | Kaspersky |
| --- | ------------ | --------- |
Knowbe4
| B   | E   |     |
| --- | --- | --- |
Kordamentha
Bad Packets
EASE (Energy Analytic
| bit-x-bit | Security Exchange) |     |
| --------- | ------------------ | --- |
L
| Bitsight | Edgescan |     |
| -------- | -------- | --- |
Lares Consulting
| Blackberry Cylance | Elevate Security |     |
| ------------------ | ---------------- | --- |
Legal Services—ISAO
Emergence Insurance
LMG Security
| C   | EUROCONTROL |     |
| --- | ----------- | --- |
Lookout
Center for Internet Security
F
CERT European Union
M
DomainTools (formerly
CERT Division of Carnegie
|     | Farsight Security)  | Malicious Streams |
| --- | ------------------- | ----------------- |
Mellon University’s Software
Engineering Institute
Financial Services ISAC (FS-ISAC) Maritime Transportation System ISAC
| Checkpoint Software Technologies Ltd. |     | (MTS-ISAC) |
| ------------------------------------- | --- | ---------- |
Federal Bureau of Investigation—Inter
| Chubb     | Crime Complaint Center (FBI IC3)  | Micro Focus |
| --------- | --------------------------------- | ----------- |
| Coalition | Fortinet                          | mnemonic    |
Computer Incident Response Center
| Luxembourg (CIRCL) | G   |     |
| ------------------ | --- | --- |
N
| Coveware     | Global Resilience Federation | NetDiligence®          |
| ------------ | ---------------------------- | ---------------------- |
| Crowdstrike  | Grey Noise                   | NETSCOUT               |
| Cybersixgill |                              | NINJIO Cybersecurity   |
Awareness Training
| Cybercrime Support Network        | H         |     |
| --------------------------------- | --------- | --- |
| Cybersecurity and Infrastructure  | HackedEDU |     |
| Security Agency (CISA)            |           | P   |
Hasso-Plattner Institut
CyberSecurity Malaysia, an agency
Palo Alto Networks
under the Ministry of Communications
| and Multimedia (KKMM) | I                                | Paraflare Pty Ltd |
| --------------------- | -------------------------------- | ----------------- |
|                       | Irish Reporting and Information  | Proofpoint        |
Security Service (IRISS-CERT)
PSafe
2022 DBIR  Appendix F 104

Q
Qualys
R
Ransomwhe.re
Recorded Future
S
S21sec
SecurityTrails
Shadowserver Foundation
Shodan
SISAP - Sistemas Aplicativos
Swisscom
U
U.S. Secret Service
V
VERIS Community Database
Verizon Cyber Risk Programs
Verizon DDoS Shield
Verizon Mobile Security Dashboard
Verizon Network Operations
and Engineering
Verizon Professional Services
Verizon Sheriff Team
Verizon Threat Intelligence Platform
Vestige Digital Investigations
Verizon Threat Research Advisory
Center (VTRAC)
W
WatchGuard Technologies
Z
Zscaler
2022 DBIR Appendix F 105

2022 DBIR Appendix F 106

2022 DBIR Appendix F 107

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-10-17", "model": "gemini-3.8-flash"} -->
