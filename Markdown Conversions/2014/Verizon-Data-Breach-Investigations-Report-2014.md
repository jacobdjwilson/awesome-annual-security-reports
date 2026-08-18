# 2014 Data Breach Investigations Report

## Table of Contents
- [Introduction](#introduction)
- [2013 Year in Review](#2013-year-in-review)
- [Victim Demographics](#victim-demographics)
- [A Decade of DBIR Data](#a-decade-of-dbir-data)
- [Results and Analysis](#results-and-analysis)
- [Point-of-Sale (POS) Intrusions](#point-of-sale-pos-intrusions)

---

## INTRODUCTION

Welcome to the 2014 Data Breach Investigations Report (DBIR).[^1] Whether you’re a veteran reader who’s been with us since our initial publication back in 2008 or a newbie to our annual data party, we’re sincerely glad you’re here. We hope that this year’s submission will improve awareness and practice in the field of information security and support critical decisions and operations from the trenches to the boardroom.

For DBIR veterans, a cursory look at the table of contents will reveal some significant changes to the report structure you’ve gotten used to in years past. Rather than our signature approach organized around actors, actions, assets, timelines, etc., we’ve created sections around common incident patterns derived directly from the data itself (more on that later). Within each of those patterns, we cover the actors who cause them, the actions they use, assets they target, timelines in which all this took place, and give specific recommendations to thwart them. The drive for change is three-fold: first, we realized that the vast majority of incidents could be placed into one of nine patterns; second, we can (and did) draw a correlation between these incident patterns and industries; and third, we wanted to challenge ourselves to look at the data with a fresh perspective. The ultimate goal is to provide actionable information presented in a way that enables you to hash out the findings and recommendations most relevant to your organization.

We all know that data doesn’t grow on trees, and we must express our gratitude to the 50 organizations that contributed to this report, representing public and private entities from around the globe. We’re proud to work with these organizations and feel that what you’re now reading is proof of the benefits of coordinated incident data sharing. For the full list of 2014 DBIR contributors, check out Appendix C.

The dataset that underpins the DBIR is comprised of over 63,000 confirmed security incidents — yep, over Sixty-Three Thousand. That rather intimidating number is a by-product of another shift in philosophy with this year’s report; we are no longer restricting our analysis only to confirmed data breaches. This evolution of the DBIR reflects the experience of many security practitioners and executives who know that an incident needn’t result in data exfiltration for it to have a significant impact on the targeted business.

So prepare to digest what we hope will be some very delicious data prepared for you this year. The Methodology section, normally found near the beginning of the report, is now in Appendix A. We’ll begin instead with a review of 2013 from the headlines, then provide a few sample demographics to get you oriented with the dataset. The following section — a summary of our 10 years’ of incident data — might just be our favorite (but please don’t tell the other sections that). We’ll then provide analysis of the aforementioned incident classification patterns and end with some conclusions and a pattern-based security control mapping exercise. So let’s get started!

---

## 2013 YEAR IN REVIEW

The year 2013 may be tagged as the “year of the retailer breach,” but a more comprehensive assessment of the infoSec risk environment shows it was a year of transition from geopolitical attacks to large-scale attacks on payment card systems.

> This section is a compilation of the weekly INTSUM lead paragraphs posted to our blog and is 100% based on open source intelligence (OSINT). We maintain a very strong policy against identifying investigative clients, and mentions of organizations in this section in no way imply that we conducted an investigation involving them or that they are among the victims in our dataset.

### JANUARY
January saw a series of reports of targeted attacks by what were probably state-sponsored actors. The Red October cyber-espionage campaign was exposed and responsible for targeting government agencies and research institutions globally, but in Russian-speaking countries in particular. A different series of attacks beginning with a “watering hole” attack on the Council on Foreign Relations web site (`cfr.org`) that began on Boxing Day 2012 was linked to actors using the Elderwood Framework. Meanwhile, the Izz ad-Din al-Qassam Cyber Fighters (QCF) were almost a month into Phase II of Operation Ababil Distributed Denial of Service (DDoS) attacks on U.S. financial services companies.

### FEBRUARY
The segue into February was provided by _The New York Times_ and _The Wall Street Journal_, with new reports of targeted cyber-espionage. And Sophos reported a new Citadel-based Trojan crafted to attack Point-of-Sale (POS) systems using a Canadian payment card processor. We would soon learn that `www.iphonedevsdk.com` became a watering hole, using a surprise attack on Java late in the month. Most infoSec professionals well remember February as the month Mandiant (now FireEye) released its superb APT1 report. February was also the start of reports of data breaches from large enterprises, courtesy of the aforementioned iPhoneDevSDK: Facebook, Twitter, Apple, and Microsoft were all victims. Noteworthy retailer POS data breaches were reported by Bashas’ and Sprouts, two discrete grocery chains in the U.S. Southwest. Bit9 reported a data breach that began in July 2012, attacking its code-signing infrastructure.

### MARCH
Fifty million Evernote users remember that March was the month they were forced to change their passwords. On March 20, the Republic of Korea suffered a large-scale cyber-attack that included disk corruption. We remain skeptical that the Cyberbunker-CloudFlare-Spamhaus DoS attack almost broke the internet at the end of March. Group-IB reported “Dump Memory Grabber” (a.k.a. BlackPOS), a new POS Trojan that would go on to make headlines when news broke of Target Stores’ breach in December.

### APRIL
In April, another U.S. grocery retailer, Schnucks, reported a POS data breach. The Syrian Electronic Army (SEA) did some damage when it hijacked the Associated Press’ Twitter account, sending a tweet reporting an explosion at the White House and causing a spasm on Wall Street. Operation Ababil continued, but OSINT cannot support attributing DoS attacks on several European banks to the QCF.

### MAY
Cyber-espionage continued in May, with reports from QinetiQ and the U.S. Army Corps of Engineers. The SEA hijacked the Twitter accounts of both _The Guardian_ and _The Financial Times_. A watering hole attack targeted nuclear weapons researchers in the U.S. for cyber-espionage, probably from China. More cyber-espionage campaigns reported in May included Operation Hangover, targeting Pakistan; Safe, targeting Mongolia; and operations by the Sunshop actors against Tibetan activists. The U.S. Department of Justice shut down Liberty Reserve, the go-to bank for cyber-criminals.

### JUNE
Early in June, Raley’s, yet another U.S. grocer with stores in California and Nevada, reported its payment card systems were breached. NetTraveller, a global cyber-espionage campaign targeting diplomats in countries with interests not aligned with China occurred. A day later, _The Guardian_ published the first intelligence leaked by Edward Snowden… and then infoSec intelligence became the “All-Snowden-All-the-Time” channel.

### JULY
July’s largest retailer data breach was reported by Harbor Freight, a U.S. tool vendor with 445 stores – nearly 200 million customers and we still don’t know how many records were compromised. The QCF initiated Phase IV of Operation Ababil. The SEA breached Viber, Tango, and the Daily Dot. The U.S. Department of Justice indicted four Russians and one Ukrainian for high-profile data breaches, including Heartland and Global Payments.

### AUGUST
In August, the SEA hijacked the Twitter accounts of CNN, _The Washington Post_, Time Magazine, SocialFlow, and both _The New York Times_ and _New York Post_. Attendees of the G8 Summit in St. Petersburg, Russia, were targeted for cyber-espionage by the Calc Team actors.

### SEPTEMBER
In September, Vodafone notified two million customers their personal and financial information had been breached. Espionage reported in September involved the EvilGrab Trojan and separately, the Hidden Lynx actors who seem to engage in both espionage and cybercrime. New intelligence linked the Bit9 attack from February with Operation Deputy Dog, Hidden Lynx, and watering hole attacks on Japanese financial institutions. At the end of the month Brian Krebs began his reports on intelligence extracted from `ssndob[dot]ms`. The site was home to data stolen from some of America’s largest data brokers: Lexis-Nexis, Kroll, and Dun & Bradstreet. Cryptolocker made its first appearance in September, extorting money from victims that were willing to pay to decrypt their essential files.

### OCTOBER
On October 3, Adobe announced its systems had been breached; eventually 38 million accounts were identified as affected. Intelligence connected this to the `ssndob[dot]ms` actors. Nordstrom, the luxury U.S. department store, discovered skimmers on some of its cash registers. Two of 2013’s big wins also occurred in October: Dmitry “Paunch” Fedotov, the actor responsible for the Blackhole exploit kit, was arrested in Russia, and Silk Road, an online fraud bazaar, was taken down.

### NOVEMBER
The proverbial calm before the storm, November was fairly quiet. Banking malware evolved with reports of Neverquest and another version of IceIX. BIPS, a major European bitcoin payment processor, was the victim of one of the largest bitcoin heists recorded up to that point in time.

### DECEMBER
The last significant entry under cyber-espionage for 2013 was the targeting of foreign ministries in European countries by Operation Ke3chang. _The Washington Post_ reported its second breach of the year. And then infoSec intelligence became the “All-Target-All-the-Time” channel. Although the breach of this major U.S. retailer was a little more than half the size of Heartland and three-fourths the size of TJX, it’s vying to become the event for which 2013 will always be remembered.

---

## VICTIM DEMOGRAPHICS

Readers of the DBIR frequently approach us with two important questions. How generally representative are the findings of this report? Are these findings relevant to my organization? To help get you oriented with this year’s report, let’s see what the data has to show us.

The 2013 DBIR featured breaches affecting organizations in 27 countries. This year’s report ups that tally by 350%, to 95 distinct countries (Figure 1). All major world regions are represented, and we have more national Computer Security Incident Response Teams (CSIRTs) than ever before. Our ability to compare global trends has never been higher.

But it’s not quite that simple. The charter, focus, methods, and data differ so much between CSIRTs that it’s difficult to attribute differences to true variations in the threat environment.[^2] However, regional blind spots are getting smaller thanks to our growing list of contributors (see Appendix C), and we’re very happy with that.

![Figure 1. Countries represented in combined caseload map/list]

**Countries represented in combined caseload (in alphabetical order):** Afghanistan, Albania, Algeria, Argentina, Armenia, Australia, Austria, Azerbaijan, Bahrain, Belarus, Belgium, Bosnia and Herzegovina, Botswana, Brazil, Brunei Darussalam, Bulgaria, Cambodia, Canada, Chile, China, Colombia, Congo, Croatia, Cyprus, Czech Republic, Denmark, Egypt, Ethiopia, Finland, France, Georgia, Germany, Greece, Hong Kong, Hungary, India, Indonesia, Iran, Islamic Republic of, Iraq, Ireland, Israel, Italy, Japan, Jordan, Kazakhstan, Kenya, Korea, Republic of, Kuwait, Kyrgyzstan, Latvia, Lebanon, Lithuania, Luxembourg, Macedonia, the former Yugoslav Republic of, Malaysia, Mali, Mauritania, Mexico, Moldova, Republic of, Montenegro, Morocco, Mozambique, Nepal, Netherlands, New Zealand, Oman, Pakistan, Palestinian Territory, Occupied, Peru, Philippines, Poland, Portugal, Qatar, Romania, Russian Federation, Saudi Arabia, Singapore, Slovakia, Slovenia, South Africa, Spain, Switzerland, Taiwan, Province of China, Tanzania, United Republic of, Thailand, Turkey, Turkmenistan, Uganda, Ukraine, United Arab Emirates, United Kingdom, United States, Uzbekistan, Vietnam, Virgin Islands.

### Figure 2. Number of security incidents by victim industry and organization size, 2013 dataset
| Industry | Total | Small | Large | Unknown |
| --- | --- | --- | --- | --- |
| Accommodation [72] | 212 | 115 | 34 | 63 |
| Administrative [56] | 16 | 8 | 7 | 1 |
| Agriculture [11] | 4 | 0 | 3 | 1 |
| Construction [23] | 4 | 2 | 0 | 2 |
| Education [61] | 33 | 2 | 10 | 21 |
| Entertainment [71] | 20 | 8 | 1 | 11 |
| Finance [52] | 856 | 43 | 189 | 624 |
| Healthcare [62] | 26 | 6 | 1 | 19 |
| Information [51] | 1,132 | 16 | 27 | 1,089 |
| Management [55] | 10 | 1 | 3 | 6 |
| Manufacturing [31,32,33] | 251 | 7 | 33 | 211 |
| Mining [21] | 11 | 0 | 8 | 3 |
| Professional [54] | 360 | 26 | 10 | 324 |
| Public [92] | 47,479 | 26 | 47,074 | 379 |
| Real Estate [53] | 8 | 4 | 0 | 4 |
| Retail [44,45] | 467 | 36 | 11 | 420 |
| Trade [42] | 4 | 3 | 0 | 1 |
| Transportation [48,49] | 27 | 3 | 7 | 17 |
| Utilities [22] | 166 | 2 | 3 | 161 |
| Other [81] | 27 | 13 | 0 | 14 |
| Unknown | 12,324 | 5,498 | 4 | 6,822 |
| Total | 63,437 | 5,819 | 47,425 | 10,193 |

### Figure 3. Number of security incidents with confirmed data loss by victim industry and organization size, 2013 dataset
| Industry | Total | Small | Large | Unknown |
| --- | --- | --- | --- | --- |
| Accommodation [72] | 137 | 113 | 21 | 3 |
| Administrative [56] | 7 | 3 | 3 | 1 |
| Construction [23] | 2 | 1 | 0 | 1 |
| Education [61] | 15 | 1 | 9 | 5 |
| Entertainment [71] | 4 | 3 | 1 | 0 |
| Finance [52] | 465 | 24 | 36 | 405 |
| Healthcare [62] | 7 | 4 | 0 | 3 |
| Information [51] | 31 | 7 | 6 | 18 |
| Management [55] | 1 | 1 | 0 | 0 |
| Manufacturing [31,32,33] | 59 | 6 | 12 | 41 |
| Mining [21] | 10 | 0 | 7 | 3 |
| Professional [54] | 75 | 13 | 5 | 57 |
| Public [92] | 175 | 16 | 26 | 133 |
| Real Estate [53] | 4 | 2 | 0 | 2 |
| Retail [44,45] | 148 | 35 | 11 | 102 |
| Trade [42] | 3 | 2 | 0 | 1 |
| Transportation [48,49] | 10 | 2 | 4 | 4 |
| Utilities [22] | 8;0* | 2 | 0 | 78 |
| Other [81] | 8 | 6 | 0 | 2 |
| Unknown | 126 | 2 | 3 | 121 |
| Total | 1,367 | 243 | 144 | 980 |

*Small = organizations with less than 1,000 employees, Large = organization with 1,000+ employees*  
*For more information on the NAICS codes [shown above] visit: [https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012](https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012)*

We saw some increases where we added new industry-specific contributors, so pieces of the puzzle are filling in. Certain sectors will always skew higher in the victim count given their attractiveness to financially motivated actors — i.e., those that store payment card or other financial data. But even discounting that, we don’t see any industries flying completely under the radar. And that’s the real takeaway here — everyone is vulnerable to some type of event. Even if you think your organization is at low risk for external attacks, there remains the possibility of insider misuse and errors that harm systems and expose data.

Next, let’s review the different industries and sizes of victim organizations in this year’s dataset (Figure 2). The Public sector’s astronomical count is primarily a result of U.S. agency reporting requirements, which supply a few of our contributors with a vast amount of minor incidents (more on that later), rather than a sign of higher targeting or weak defenses. Figure 3 filters out the minutiae by narrowing the dataset to only those incidents involving confirmed data compromise. Moving beyond the Public sector outlier, both Figure 2 and Figure 3 show demographics relatively similar to prior years.

So, we can’t claim to have unbiased coverage of every type and size of organization on the planet (fingers crossed for next year, though!). But we dare say that the majority of readers will be able to see themselves or something that looks enough like them in this sample.

---

## A DECADE OF DBIR DATA

Long-time readers of this report will know that we’re not very good at maintaining the status quo. The sources of data grow and diversify every year. The focus of our analysis shifts. The way we visualize data and organize results evolves over time. And with the 2014 DBIR, we’re really gonna shake things up.

> This section attempts to create an “as-comparable-as-possible” set of findings to previous DBIRs. It “only” includes breaches from 2004-2012, plus the 1,367 incidents for which data compromise was confirmed in 2013.

While this does make it hard to meaningfully compare trends across time, it has the positive effect of shining light into new and shadowy areas each year. The truth of the matter is that we’re more interested in exploring and learning than churning out the same ‘ol stuff each time just to measure deltas. 

That said, measuring deltas has value and we know readers appreciate some level of continuity between reports. Thus, this section attempts to create an “as-comparable-as-possible” set of findings to previous DBIRs. It “only” includes breaches from 2004-2012, plus the 1,367 incidents for which data compromise was confirmed in 2013. It’s worth noting that this represents the high mark in ten years of data breaches, and is the first time we’ve crossed 1,000. (Give a round of applause to all those contributors who keep adding fuel to the bonfire.)

We began writing a lot of commentary for this section, but changed our minds. Instead, we’ll churn out some eye candy for you to chew on as long as you like, with only a few general observations from us.

### A BRIEF PRIMER ON VERIS AND VCDB

The Vocabulary for Event Recording and Incident Sharing (VERIS) is designed to provide a common language for describing security incidents in a structured and repeatable manner. It takes the narrative of “who did what to what (or whom) with what result,” and translates it into the kind of data you see in this report. Because we hope to facilitate the tracking and sharing of security incidents, we released VERIS for free public use. Get additional information on the VERIS community site; the full schema is available on GitHub.

Launched in 2013, the VERIS Community Database (VCDB) project enlists the cooperation of volunteers in the security community in an attempt to record all publicly disclosed security incidents in a free and open dataset.

We leverage VCDB for a few sections in this report, which are clearly marked. Learn more about VCDB by visiting the website below.

[www.veriscommunity.com](www.veriscommunity.com) | [github.com/vz-risk/veris](github.com/vz-risk/veris) | [vcdb.org](vcdb.org)

Both are good companion references to this report for understanding terminology and context.

![Figure 4. Number of breaches per threat actor category over time]  
![Figure 5. Percent of breaches per threat actor category over time]

Figure 4 depicts the raw count of breaches attributed to external, internal, and partner actors over the 10-year history of our breach data. Figure 5 shows this as a proportion of all breaches and rearranges the categories to highlight exclusivity and overlap among them. It uses a third-degree polynomial trend line to make it nice and smooth, so we can see the basic behavior over time. Together they help answer our primary questions of interest — which actors perpetrate the most breaches and what’s the relative change over time?

> **BREACHES VS INCIDENTS?**  
> This report uses the following definitions:  
> - **Incident:** A security event that compromises the integrity, confidentiality, or availability of an information asset.  
> - **Breach:** An incident that results in the disclosure or potential exposure of data.  
> - **Data disclosure:** A breach for which it was confirmed that data was actually disclosed (not just exposed) to an unauthorized party.

Since we’re letting the visualizations do most of the talking here, we’ll only make a few observations and leave the rest for homework.
- Ten years offers some nice min/max/most likely estimates for you modelers out there. Barring 2006-2008, the overall ratio is relatively stable, especially when you consider the dramatic changes in total breaches and sources in scope each year.
- 2007 is the only year showing an insider majority in Figure 4. This is primarily the result of an unusually small Verizon caseload for confirmed breaches and an influx of U.S. Secret Service data from 2006-2008. We essentially crashed two equally sized – but very different – samples together.
- That giant dip for external actors in 2012 seen in Figure 4 coincides with an overall drop in breach count that year, mainly due to fewer large, multi-victim POS intrusion sprees targeting SMBs in the dataset.
- Thanks to several new partners who focus on insider crimes, the proportional trend line for internal swings up over the last couple years while external turns downward. If we removed the polynomial curving, however, you’d see a positive regression for outsiders and a slightly negative one for insiders.

![Figure 6. Percent of breaches per threat actor motive over time]  
![Figure 7. Number of breaches per threat actor motive over time]

Two different views indicating how the motives of threat actors have changed over the last five years appear in Figure 6 and 7. The line chart (Figure 6) gives the relative percentage of the top three motives in our dataset, while Figure 7 uses an area plot of total incident counts.
- We knew espionage had been rising over the last few years, but the trend line chart surprised us by the degree of convergence with financial motives. Will that continue?
- Is this finding merely the result of adding contributors to the DBIR who specialize in espionage, or is money truly diminishing as the prime driver of crime on the internet? We have an easier time believing the former than the latter, but it certainly makes us want to continue widening our collection of breach data in the future.
- The area plot reminds us that money-motivated breaches still outnumber others by a good margin. To borrow from Pink Floyd, most actors still want to “grab that cash with both hands and make a stash.”

![Figure 8. Number of breaches per threat action category over time]

- This chart does a superb job underscoring the value of data sharing. You can see the number of breaches and diversity of threats grow as the DBIR transitions from single sample to a meta study.
- But it’s not all because of changes in the sample set. Notice how the hacking and malware categories explode upward in 2009 and social tactics begin to climb in 2010. These have parallel stories in the real world (e.g., better automated attack tools and DIY malware kits), and it’s fascinating to see them reflected in the data.

![Figure 9. Top 20 varieties of threat actions over time]

Figure 9 dives deeper into the specific varieties of threat actions observed over the last five years. The overall top twenty across the five-year span is listed in successive columns, and the lines connecting columns highlight how each action changes over time. To be honest, concise commentary on this visualization may be impossible. Yes, it’s incredibly busy, but it’s also incredibly information-dense. Let your eyes adjust and then explore whatever strikes your fancy. As an example, follow RAM scrapers through the years. They start at #5 in 2009, drop way down over the next few years and then shoot up the charts to the #4 spot in 2013. We talk about that resurgence in the POS intrusions section of this report. Literally every item in Figure 9 has a story if you care to look for it. Enjoy.

![Figure 10. Percent of breaches per asset category over time]  
![Figure 11. Number of breaches per asset category over time]

Figures 10 and 11 show how the mix of compromised assets has changed over time. It’s useful because it reveals the “footprint” of attackers as they travel through the victim’s environment in search of data. As defenders, it gives us a sense of what may need extra attention or protection.
- Servers have typically been on top, probably because attackers know that’s where the data is stored.
- User devices have been growing over time, probably because they offer an easy foot in the door.
- Media is the only asset category trending down, probably because of an unusually high concentration of (partially-related) cases in 2009 that involved numerous thefts of documents and digital media.
- Many ask why the Network category is so low, given that most of these breaches take place over the network. In view here are specific network devices like routers, switches, etc. Malicious traffic definitely passes through those, but they’re not typically compromised during a breach.

![Figure 12. Breach count by data variety over time]

It would be hard to give proper treatment to a decade of data theft without covering the varieties of data stolen over that time period. Thankfully, Figure 12’s got us covered in that department.
- If you compare these trends with those of actor motives from Figure 6 and 7, you’ll see some parallels. Financially-motivated criminals will naturally seek out data that is easily converted to cash, such as bank information and payment cards, while espionage groups target internal corporate data and trade secrets.
- The trend for payment card theft is quite fascinating; it rises quickly to a peak in 2010, and then exhibits a negative slope. There’s an uptick in 2013, but it was still the first year in the history of this report where the majority of data breaches did not involve payment cards.
- Authentication credentials are useful in both the criminal underground and the shadowy world of the clandestine, and that demand is reflected here.

![Figure 13. Percent of breaches where time to compromise (red)/time to discovery (blue) was days or less]  
![Figure 14. Breach discovery methods over time]

Take a deep, calming breath before diving into this last one; it may result in mental or even bodily harm. In Figure 13, we’re contrasting how long it takes the attacker to compromise an asset with how long it takes the defender to discover this. We chose to peg this on “days” to keep things simple and stark (one might also add “sad” to that alliteration).
- Ignore the behavior of the lines for a minute and focus on the wide gap between percentages for the two phases. It smacks us with the fact that the bad guys seldom need days to get their job done, while the good guys rarely manage to get theirs done in a month of Sundays.
- The trend lines follow that initial smack with a roundhouse kick to the head. They plainly show that attackers are getting better/faster at what they do at a higher rate than defenders are improving their trade. This doesn’t scale well, people.
- We thought about superimposing “total spending on network monitoring,” “number of security products on the market,” and “number of Certified Information Systems Security Professionals (CISSPs) in the workplace,” but we were concerned it would result in much self-inflicted harm within the security community. And we’d much rather you guys and gals stick around and help us fix this.

Having dealt that last blow regarding timelines, readers familiar with the traditional flow of the DBIR may expectantly hear that Mortal Kombat imperative of “Finish Him!” in their heads as we head into discussion of breach discovery methods. But there will be no triumphant “Fatality!” announcement here; we’re going to show mercy instead and end on a positive note.
- We’re thrilled to see that internal discoveries outnumber external fraud detection for the first time in DBIR history!
- It’s great that law enforcement is steadily getting better and better at detecting breaches and notifying victims!
- Unrelated third parties, like CSIRTs and threat researchers, are quickly rising as an important and prominent way that victims — especially espionage victims — come to learn about breaches. Keep up the good work, folks; we’re making a dent!

We hope you enjoyed this little ten-year trip down memory lane as much as we did. This small band of geeks is grateful to Verizon for allowing us to spend so much time in our playground of breach information. We’re also grateful to the many organizations that have participated in making it possible; without your contributions the data would have gotten stale years ago. And finally, thanks to all you readers out there who download this document and consider these trends as you fight the good fight of protecting information and customers. May the next ten years find us all on the winning side of that battle.

---

## RESULTS AND ANALYSIS

The seeds of our approach to the 2014 DBIR began to grow during the final phase of drafting the 2013 report. When trying to present statistics around threat actions in a simple and meaningful way, we noticed certain combinations of actors, actions, and assets frequently occurring together within an incident scenario. We gave names to three of these and included some “scratch paper” calculations showing they collectively described 68% of the entire dataset (Figure 15). Production deadlines prevented further exploration into that phenomenon, so we left readers with this thought: “We may be able to reduce the majority of attacks by focusing on a handful of attack patterns.” But as soon as the 2013 DBIR was put to bed, we returned to the notion of incident patterns and began studying our dataset from a very new perspective with a new set of techniques.

![Figure 15. Scratch paper calculations from the 2013 DBIR for commonly-observed incident patterns]

Now, fast forward to the 2014 DBIR. We have more incidents, more sources, and more variation than ever before – and trying to approach tens of thousands of incidents using the same techniques simply won’t cut it. Not only would the dominant incident characteristics drown out the subtleties of the less frequent varieties, but we cannot continue to study those characteristics as though they occur in isolation. A list of the top 20 actions is helpful, but even more helpful is an accounting of the actors that perform them, other actions used in combination with them, and the assets they tend to target. To reel in that prize, we’re going to need a bigger boat. Full throttle, Mr. Hooper!

And that brings us back to recurring combinations of actors, actions, assets, and attributes, or more formally, incident classification patterns. In order to expose these latent patterns in the data, we applied a statistical clustering technique (the bigger boat) by creating a matrix aggregating incidents within each of the common VERIS enumerations and calculating the numeric “distance” between them. This enabled us to find clusters, or patterns, of strongly related VERiS enumerations within the incident dataset. “Strongly related” here essentially means they often occur together in the same incidents and are distinct in some way from other combinations.

The first time through, we tossed everything in and looked at the clustering (of the hierarchical type if you’re into that) of VERIS enumerations. Some clusters were obvious, like the social action of phishing with the social vector of email. However, we were looking for clusters that describe comprehensive incident classifications rather than just frequent pairings. For example, incidents involving physical tampering of ATMs by organized criminal groups to steal payment cards stood out like a Wookie among Ewoks. So we labeled that pattern “skimmers,” removed the matching incidents, and reran the cluster analysis on the remaining incidents to look for the next pattern.

In the end, we identified nine patterns that together describe 94% of the confirmed data breaches we collected in 2013.

> **Nine out of ten of all breaches can be described by nine basic patterns.**

But (using our best infomercial voice) that’s not all! When we apply the same method to the last three years of breaches, 95% can be described by those same nine patterns.

But wait — there’s more! Act now, and we’ll throw in all security incidents — not just breaches — from all partners and the VERiS Community Database (VCDB) over the last ten years — for free! Yes, all for the same price of nine patterns, you can describe 92% of 100K+ security incidents!

Remember that promise from last year — “We may be able to reduce the majority of attacks by focusing on a handful of attack patterns?” Consider it fulfilled. To us, this approach shows extreme promise as a way to drastically simplify the seemingly endless array of threats we must deal with to protect information assets.

![Figure 16. Frequency of incident classification patterns]  
![Figure 17. Number of selected incident classification patterns over time]  
![Figure 18. Percent of selected incident classification patterns over time]

We dig into each incident pattern in the following sections, but you can see from Figure 16 that POS intrusions, web app attacks, cyber-espionage, and card skimmers are among the top concerns when we focus on data disclosure. However, it’s not enough to just identify and count the patterns as a whole.

Obviously not every organization needs to focus on point of sale attacks. To make the analysis actionable, we pulled all incidents within each industry and then applied the patterns to create the work of art that is Figure 19. It shows the proportion of incidents within each industry represented by the nine patterns over the last three years.

In order to use Figure 19, identify your industry in the left hand column. Refer to the NAICS website if you’re unsure where your organization fits. The percentages are relative to each industry. For example, 10% of all Retail incidents fall within the “web app attack”. The coloring should help you quickly identify “hot spots” for your industry and/or discern differing threat profiles across multiple industries.

Before continuing on to the detailed discussion of each pattern (which appear in order according to Figure 18), you may want to study Figure 19. Look up the industry (or industries) that matter to you, identify which patterns are most relevant, and pay special attention to those sections in the report (you’ll still want to read the whole thing, of course). For those curious about how these incident patterns trend over time, we’ve retrofitted them to pre-2013 data to produce Figures 17 and 18.

We’ve heard the (constructive) criticism from some of you noting that it’s difficult to pick out exactly which findings from the DBIR apply to your organization, and we spent a lot of time figuring out how to address that. We hope you’ll agree this is a step in the right direction, not only for this report, but also for threat analysis and decision support in general.

### Figure 19. Frequency of incident classification patterns per victim industry
| Industry | POS Intrusion | Web App Attack | Insider Misuse | Theft/Loss | Misc. Error | Crimeware | Payment Card Skimmer | Denial of Service | Cyber-espionage | Everything Else |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Accommodation [72] | 75% | 1% | 8% | 1% | 1% | 1% | <1% | 10% | — | 4% |
| Administrative [56] | — | 8% | 27% | 12% | 43% | 1% | — | 1% | 1% | 7% |
| Construction [23] | 7% | — | 13% | 13% | 7% | 33% | — | — | 13% | 13% |
| Education [61] | <1% | 19% | 8% | 15% | 20% | 6% | <1% | 6% | 2% | 22% |
| Entertainment [71] | 7% | 22% | 10% | 7% | 12% | 2% | 2% | 32% | — | 5% |
| Finance [52] | <1% | 27% | 7% | 3% | 5% | 4% | 22% | 26% | <1% | 6% |
| Healthcare [62] | 9% | 3% | 15% | 46% | 12% | 3% | <1% | 2% | <1% | 10% |
| Information [51] | <1% | 41% | 1% | 1% | 1% | 31% | <1% | 9% | 1% | 16% |
| Management [55] | — | 11% | 6% | 6% | 6% | — | 11% | 44% | 11% | 6% |
| Manufacturing [31,32,33] | — | 14% | 8% | 4% | 2% | 9% | — | 24% | 30% | 9% |
| Mining [21] | — | — | 25% | 10% | 5% | 5% | 5% | 5% | 40% | 5% |
| Professional [54] | <1% | 9% | 6% | 4% | 3% | 3% | — | 37% | 29% | 8% |
| Public [92] | — | <1% | 24% | 19% | 34% | 21% | — | <1% | <1% | 2% |
| Real Estate [53] | — | 10% | 37% | 13% | 20% | 7% | — | — | 3% | 10% |
| Retail [44,45] | 31% | 10% | 4% | 2% | 2% | 2% | 6% | 33% | <1% | 10% |
| Trade [42] | 6% | 30% | 6% | 6% | 9% | 9% | 3% | 3% | — | 27% |
| Transportation [48,49] | — | 15% | 16% | 7% | 6% | 15% | 5% | 3% | 24% | 8% |
| Utilities [22] | — | 38% | 3% | 1% | 2% | 31% | — | 14% | 7% | 3% |
| Other [81] | 1% | 29% | 13% | 13% | 10% | 3% | — | 9% | 6% | 17% |

*For more information on the NAICS codes [shown above] visit: [https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012](https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012)*

---

## POINT-OF-SALE (POS) INTRUSIONS

**AT A GLANCE**  
- **Description:** Remote attacks against the environments where retail transactions are conducted, specifically where card-present purchases are made. Crimes involving tampering with or swapping out devices are covered in the Skimming pattern.  
- **Top industries:** Accommodation and Food Services, Retail  
- **Frequency:** 198 total incidents | 198 with confirmed data disclosure  
- **Key findings:** Given recent headlines, some may be surprised to find that POS intrusions are trending down over the last several years. That’s mainly because we’ve seen comparatively fewer attack sprees involving numerous small franchises. Brute forcing remote access connections to POS still leads as the primary intrusion vector. A resurgence of RAM scraping malware is the most prominent tactical development in 2013.  

![Figure 20. Comparison of POS Intrusions and Web App Attacks patterns, 2011-2013]

We know many of you will come to this section hoping to find all the particulars and dirty laundry of a certain breach involving a major U.S. retailer in late 2013. Prepare to be disappointed; we don’t name victims in this report nor do we divulge client-specific information on any breaches handled by any of the DBIR contributors. If you want up-to-the-minute news on particular breaches, you’d best look elsewhere. As a consolation prize, however, we hope you’ll accept our overall analysis of two hundred POS intrusions that occurred in 2013, along with recommendations on how you can avoid increasing that number in 2014.

The industries most commonly affected by POS intrusions are of no surprise: restaurants, hotels, grocery stores, and other brick-and-mortar retailers are all potential targets. Recent highly publicized breaches of several large retailers have brought POS compromises to the forefront. But at the risk of getting all security-hipster on you — we’ve been talking about this for years. In fact, this is the main cause of the large dip in 2012 seen in many of the “over time” charts in this report. We were writing about RAM scrapers before anyone heard of them and we’re quite frankly not all that into them anymore because they’ve sold out and gone mainstream.

Jokes aside, while POS hacks are getting more press recently, they really have been going on for years and we really have talked quite a bit about them in previous DBIRs. The media frenzy makes quite a splash, but from a frequency standpoint, this largely remains a small-and-medium business issue. Focusing too much on outliers and headlines can reflect cognitive bias. For instance, some may be surprised that the number of POS attacks in 2012 and 2013 is substantially lower than in 2011 (Figure 20). 

From an attack pattern standpoint, the most simplistic narrative is as follows: compromise the POS device, install malware to collect magnetic stripe data in process, retrieve data, and cash in. All of these attacks share financial gain as a motive, and most can be conclusively attributed (and the rest most likely as well) to organized criminal groups operating out of Eastern Europe.[^3] Such groups are very efficient at what they do; they eat POSs like yours for breakfast, then wash ‘em down with a shot of vodka.

While the majority of these cases look very much alike, the steps taken to compromise the point-of-sale environment offer some interesting variations.

[^1]: 2014 Data Breach Investigations Report (DBIR).
[^2]: Differences in reporting requirements, legal mandates, and definitions of what constitutes a security incident or breach across different Computer Security Incident Response Teams (CSIRTs).
[^3]: Attribution based on analysis of actor signatures, command-and-control infrastructure, and victim telemetry within the dataset.

---

lower than the number
recorded in 2010 and 2011 (despite having ten times more
contributors in the latter years). Figure 20 reminds us that our
understanding of risk should always come back to the data, not
what makes good headlines and marketing fodder.
ELAS-FO-TNiOP
SNOiSURTNi
16 VERIZON ENTERPRISE SOLUTIONS

Let’s start with the most frequent scenario, which affects small  was that the same password was used for all organizations
POiNT-OF-SALE  POiNT-OF-SALE
businesses that may or may not realize just how lucrative a  managed by the vendor. Once it was stolen, it essentially became  iNTRUSiONS iNTRUSiONS
target they are. This event chain begins with the compromise of  a default password and the attackers also gained knowledge of
the POS device with little to no legwork; the devices are open to  the customer base. Armed with this information, the familiar
the entire internet and, to make matters worse, protected with  modus operandi of installing malicious code that captured and
weak or default passwords (and sometimes no passwords). transmitted the desired data began.
| Figure 21.  |     |     | Figure 22.  |     |     |     |
| ----------- | --- | --- | ----------- | --- | --- | --- |
Top 10 threat action varieties within POS Intrusions (n=196) Hacking variety within POS Intrusions (n=187) ATTACKS WEB APP
| RAM scraper [mal] |     | 85% |             |     |     |     |
| ----------------- | --- | --- | ----------- | --- | --- | --- |
|                   |     |     | Brute force |     | 53% |     |
Export data [mal] 79%
|                   |     |     | Use of stolen creds |     | 38% |                  |
| ----------------- | --- | --- | ------------------- | --- | --- | ---------------- |
| Brute force [hac] |     | 50% |                     | 9%  |     | PRiViLEGE MiSUSE |
Offline cracking
iNSiDER AND
| Use of stolen creds [hac] | 37% |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- |
Unknown 9%
| Offline cracking [hac] | 8%  |     | Use of backdoor or C2 | 2%  |     |     |
| ---------------------- | --- | --- | --------------------- | --- | --- | --- |
Use of backdoor
2%
| or C2 [hac]             |     |     | SQLi | <1% |     |     |
| ----------------------- | --- | --- | ---- | --- | --- | --- |
| Spyware/Keylogger [mal] | 2%  |     |      |     |     |     |
PHYSiCAL THEFT
| Backdoor [mal] | 1%  |     |     |     |     | AND LOSS |
| -------------- | --- | --- | --- | --- | --- | -------- |
Figure 23.
Misconfiguration [err] <1% Hacking vector within POS Intrusions (n=187)
| Phishing [soc] | <1% |     |                   |     |     |                |
| -------------- | --- | --- | ----------------- | --- | --- | -------------- |
|                |     |     | 3rd party desktop |     | 55% |                |
|                |     |     | Desktop sharing   |     | 35% | MiSCELLANEOUS  |
The top three threat actions tell the story rather well (Figure 21).
The perpetrators scan the internet for open remote-access ports  Physical access 9% ERRORS
and if the script identifies a device as a point of sale, it issues
|     |     |     | Backdoor or C2 | 1%  |     |     |
| --- | --- | --- | -------------- | --- | --- | --- |
likely credentials (Brute force) to access the device. They then
install malware (RAM scraper) to collect and exfiltrate (Export  Command hell 1%
| data) payment card information. |     |     |     | <1% |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- |
VNP
One finding that intrigued us is the renaissance of RAM scraping  CRiMEWARE
|     |     |     | Web application | <1% |     |     |
| --- | --- | --- | --------------- | --- | --- | --- |
malware as the primary tool used to capture data. RAM scrapers
allow payment card data to be grabbed while processed in
While not as common as the simpler POS intrusions, our dataset
memory (where it is unencrypted) rather than when stored on
does include several incidents from the first quarter of 2013
disk or in transit across the network (where it is (ostensibly)
that feature a compromise at a corporate location, leading to
encrypted).
|     |     |     | widespread compromise of individual locations and malicious  |     |     | PAYMENT CARD  |
| --- | --- | --- | ------------------------------------------------------------ | --- | --- | ------------- |
SKiMMERS
it’s interesting, but not necessarily surprising, that RAM  code installations across a multitude of stores. Some cases have
scraping has usurped keyloggers as the most common malware  begun with a store compromise that led to penetration of the
functionality associated with POS compromises. One could  corporate network, but the hub-and-spoke architecture allowed
theorize that keyloggers (most of which were common varieties  for efficient traversal of the network and the impact of the
such as Perfect Keylogger and Artemis) are more easily spotted  compromise was magnified regardless of where “device 0” was
| than the memory-scraping code we witnessed in this data set. Or  |     |     | located. |     |     |     |
| ---------------------------------------------------------------- | --- | --- | -------- | --- | --- | --- |
ESPiONAGE
perhaps the RAM scrapers, which hook into specific processes of
CYBER-
the POS software, simply do the job better and more efficiently.
in years past, we analyzed attack sprees that spanned multiple
victims with no association with each other beyond the use
of truly awful passwords. This report features almost 200
incidents, but in prior years we saw over 200 victims for one
ATTACKS
criminal group. The two biggest sprees in our 2013 dataset,  DOS
one involving several franchisees of the same company, and the
other affecting multiple corporations, are a bit different, and
lead us to our second common scenario: the use of stolen vendor
credentials. in one case the credentials stolen belonged to a
EVERYTHiNG
point-of-sale vendor and were compromised via Zeus malware
infecting the vendor’s systems. The big problem among these  ELSE
| VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT |     |     |     |     |     | 17  |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- |

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
The timelines in Figure 25 reinforce both the compromise
vectors and the discovery methods. Entry is often extremely
quick, as one would expect when exploiting stolen or weak
passwords. Most often it takes weeks to discover, and that’s
based entirely on when the criminals want to start cashing in on
their bounty.
Figure 25.
Timespan of events within POS Intrusions
Regardless of how large the victim organization was or which
methods were used to steal payment card information, there
is another commonality shared in 99% of the cases: someone
else told the victim they had suffered a breach. This is no
different than in years past, and we continue to see notification
by law enforcement and fraud detection as the most common
discovery methods. in many cases, investigations into breaches
will uncover other victims, which explains why law enforcement
is the top method of discovery and the top contributor of POS
intrusions in our dataset. Long story short, we’re still discovering
payment card breaches only after the criminals begin using their
ill-gotten gains for fraud and other illicit purposes.
961=n
esimorpmoC
961=n
noitartlfixE
871=n
yrevocsiD
sdnoceS setuniM sruoH syaD skeeW shtnoM sraeY reveN
Figure 24.
Top 5 discovery methods for POS Intrusions (n=197)
All External 99%
All Internal 1%
Ext - law
75%
enforcement
Ext - fraud detection 14%
Ext - customer 11%
Int - NIDS <1%
51%
Int - reported by user <1%
36%
21%
11% 1% 5% 1% 0%
88%
11%
1% 1% 1% 0% 0% 0%
85%
13%
BOTNET MITIGATION: AN INCENTIVE PROBLEM 0% 0% 0% 1% 1% 0%
According to the NHTCU, the impact of botnets — the Swiss
Army knife of cybercriminals — remained high in 2013.
Furthermore, they note an apparent incentive problem when
it comes to mitigating these crafty menaces. Since the
impact of a botnet is often spread around the globe, federal
authorities aren’t always able to amass resources to fight it
on a national level. While the total damage of such a botnet
might be large, specific countries only deal with a small
part of these damages. The initial costs for fighting such a
botnet don’t seem to outweigh the benefits of its takedown.
Nevertheless, the NHTCU continue to fight botnets. in
February of 2013, public broadcaster NOS presented
findings on part of a dropzone of the so-called Pobelka
botnet. After an online checking tool was made available,
500,000 people checked to see if their machines had (at
some time) been infected; of that group, 23,000 self-
identified as victims.
By then, the dropzone had been examined for correlations
with a 2012 malware outbreak that had prompted a
criminal investigation. Sixteen organizations within the
vital infrastructure were informed of being infected, and
relevant infected iP addresses had been communicated to
the respective iSPs.
ELAS-FO-TNiOP
SNOiSURTNi
18 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
RECOMMENDED CONTROLS
REFLECTIONS AFTER THE EC3’S FIRST YEAR IN
FOR ALL COMPANIES OPERATION
The shared vector for the major scenarios is third-party remote- Last year’s DBiR featured an appendix from Troels Oerting,
access software (e.g., pcAnywhere, LogMein). The security of Assistant Director of the European Cybercrime Centre
these products is not the issue here. it just happens that we (EC3), discussing the plans and priorities of the newly
often find them implemented in a very insecure manner. established division of Europol. Law enforcement agencies
play a critical role in this report, and it’s not often we get
Restrict remote access to see them in their formative stages. Thus, we thought it
would be interesting to include some reflections on EC3’s
Limit any remote access into POS systems by your third-party first year of operations.
management vendor, and have serious business discussions
The job of the EC3 isn’t a small one: it serves 28 European
regarding how and when they will perform their duties.
Union (EU) member states and dozens of countries, and
coordinates protection for 500 million citizens, almost
Enforce password policies
three-quarters of whom have internet access. in terms
of operations, the EC3 prioritizes four areas: cyber
Make absolutely sure all passwords used for remote access
intelligence, intrusion, online fraud, and child sexual abuse.
to POS systems are not factory defaults, the name of the POS
As with any new venture, much of the first year focused
vendor, dictionary words, or otherwise weak. if a third party
on building infrastructure and capabilities to fulfill these
handles this, require (and verify) that this is done, and that they
priorities. Secure network connections to EU and non-EU
do not use the same password for other customers.
partners were rolled out, as well as centralized forensic
analysis environments and tools.
“S” is for “Sale,” not “Social.”
The EC3 trained more than 100 law enforcement experts
Do not browse the web, email, use social media, play games, or do all over the EU in cyber investigation, tools, and obtaining
anything other than POS-related activities on POS systems. forensic evidence. it built a new central forensic laboratory
to assist member state colleagues in obtaining evidence.
Deploy AV
it distributed alerts, intelligence notifications, and
threat assessments to stakeholders. Memorandums
install and maintain anti-virus software on POS systems.
of understanding (MoUs) were signed with key private
Bottom line: Make it difficult for miscreants to log into a stakeholders, and a new Advisory Group consisting of
device that accepts the most targeted piece of information for experts outside the law enforcement community was
financially motived criminals. established (Verizon is happy to be among them).
Trends observed by the EC3 across member states in
FOR LARGE/MULTI-STORE COMPANIES
2013 include substantial increases in intrusions, malware,
Larger, multi-store companies and franchises should consider a
phishing, grooming, DDoS, espionage, and botnet activity.
couple of additional recommendations to limit the impact of a
it also reports a boom in criminal infrastructure on the
single-location breach and prevent a mass compromise.
darknet, growth in malware affecting mobile devices,
and wider distribution of malware from cloud services. in
Debunk the flat network theory
combating these trends, the EC3 has prioritized identifying
criminal network operations and cases, with the potential
Review the interconnectivity between stores and central for major and lasting impact.
locations and treat them as semi-trusted connections. Segment
the POS environment from the corporate network.
Look for suspicious network activity
Monitor network traffic to and from the POS network. There
should be a normalized traffic pattern, and while easier said than
done, anomalous traffic must be identified and investigated.
Use two-factor authentication
Stronger passwords would cut out a huge chunk of the problem,
but larger organizations should also consider multiple factors to
authenticate third-party and internal users.
iNTRUSiONS
POiNT-OF-SALE
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 19

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
WEB APP ATTACKS
AT A GLANCE
Description Any incident in which a web application was the vector of attack. This includes exploits of code-
level vulnerabilities in the application as well as thwarting authentication mechanisms.
Top industries
information, Utilities, Manufacturing, Retail
Frequency
3,937 total incidents
490 with confirmed data disclosure
Key findings Web applications remain the proverbial punching bag of the internet. They’re beaten in one of
two ways: by exploiting a weakness in the application (typically inadequate input validation), or
by using stolen credentials to impersonate a valid user. Many of the attacks in our 2013 dataset
targeted off-the-shelf content management systems (e.g., Joomla!, Wordpress, or Drupal) to gain
control of servers for use in DDoS campaigns.
There’s no question about it – the variety and combination FINANCIALLY MOTIVATED ATTACKS
of techniques available to attackers make defending web
Financially motivated attackers are hyper-focused on gaining
applications a complex task. Regrettably, our discussion of this
access to the money, so it follows that their two primary target
complexity is hampered by the level of detail provided on these industries are the financial and retail industries (where data
incidents. Unless a forensics investigation was performed (a
that easily converts to money is abundant and, all too often,
small subset of the overall dataset), the specific techniques
accessible). Within the financial industry, they focus on gaining
utilized went largely unreported or were recorded with broad
access to the user interface of the web (banking) application
categorizations. While we have enough material to discuss web
more so than exploiting the web application itself, because the
application data breaches at a high level, our ability to draw
application grants logical access to the money. This means they
conclusions drops as we dig further into the details (which often
target user credentials and simply use the web applications
aren’t there).
protected with a single factor (password) as the conduit to their
Greed takes a back seat to ideology when it comes to web app goal. These could have been included in the section on crimeware
attacks in the 2013 dataset. Just under two out of every three (and some did slip through cracks in the algorithm to land there),
web app attacks were attributable to activist groups driven by but the use of web applications as a vector of attack causes
ideology and lulz; just under one out of three came by the hand them to show up here. The tactics used by attackers are all the
of financially motivated actors; with the small remainder linked usual suspects: a) phishing techniques to either trick the user
to espionage. After some slicing and dicing we found some very into supplying credentials or installing malware onto the client
distinct sub-patterns divided along these motives. The financial system, b) the old stand-by of brute force password guessing,
and ideological attacks deserve unique discussion since the and c) rarer cases of targeting the application through SQL
treatment for each may be slightly different. While attacks injection or other application-level attacks as a means to retrieve
perpetrated by those motivated by espionage are certainly credentials, bypass the authentication, or otherwise target
relevant, discussion of these is taken up in the Espionage the user-management system. When attribution is possible,
section. the majority of external attackers utilizing stolen credentials
somewhere along the attack chain hail from Eastern
Figure 26. Europe.
External actor motives within Web App Attacks (n=1,126)
Within the retail industry, we see a slightly different focus. The
primary aim is payment card information (targeted in 95% of
Ideology/Fun 65%
the incidents), which is often accessible simply by exploiting the
Financial 33% web application. Social actions (such as phishing) are mostly non-
existent, most likely because exploiting vulnerabilities inherent
Espionage 2%
in web applications works plenty well enough. SQL injection was
leveraged in 27 of the 34 (80%) attacks against web applications
in the retail industry, followed by techniques to install and use
web shells (remote file inclusion, etc.) in five of the 34.
PPA
BEW
SKCATTA
20 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
IDEOLOGICALLY MOTIVATED ATTACKS: Figure 27.
ideology represents the largest identified portion of motives Top 10 discovery methods for financially motivated incidents
for web application attacks, and the actors also tend to be within Web App Attacks (n=122)
the most geographically diverse. 74% focus on tried and true
Total External 88%
exploits targeting, above all else, unvalidated inputs in executed
code. Nowhere is this exploited on a larger scale than Content Total Internal 12%
Management Systems (CMS) such as Joomla!, Drupal, and
WordPress, and even then, more in the added plugins than the Ext - customer 74%
core CMS code itself. Ext - fraud detection 6%
ideological actors (whether their motivation is social, political, or Int - IT audit 4%
just for plain fun) are less concerned about getting at the crown
Ext - unrelated party 3%
jewels than they are about getting a platform (in all senses of the
word) to stand on. With that in mind, it’s not surprising that we Ext - law enforcement 2%
see two types of results from ideological attackers going after
Int - fraud detection 2%
a web server: defacements to send a message or hijacking the
server to attack (including by DDoS) other victims. Int - reported by user 2%
This focus on opportunistically owning just the web server Ext - actor disclosure 2%
becomes plain when looking at the assets compromised in the Ext - audit 1%
attack. The web server was the only asset recorded in nearly all
Ext - monitor service 1%
incidents attributable to ideological motives. The actors didn’t
appear to be interested in pushing deeper and wider into the
Discovery method looks a little bleaker for activists. 99%
network. This result may be the product of simply not reporting
of the notifications were external parties (primarily CSiRTs)
those secondary components of the incident — so don’t take this
contacting victims to let them know their hosts were involved in
as advice to only focus on the web server — but it is logical and a
other attacks. This is heavily influenced by ideological attackers
point of contrast to other types of attacks in our dataset.
quietly using the platform to attack others rather than, for
DISCOVERY METHODS AND TIMELINE instance, simple defacements (which are rare in the dataset).
When the actor is financially motivated and the discovery Even though the timeline data is a little sparse, it paints the
method is recorded, we see a leading notification method that we picture of quick entry with 60% of the initial compromises
don’t see anywhere else: customers. Perhaps customers notice occurring within minutes or less. This reflects the highly
the fraudulent activity before anyone else, but something is repetitive CMS exploits in this pattern; if it works, it works
definitely tipping them off before any internal mechanism. With quickly. Just over 85% of the incidents are discovered in days
all internal discovery methods combined, only 9% of victims or more, with about 50% taking months or longer to discover.
discovered data breaches of their own accord. Once discovered though, we see fairly good reaction time, with
about half of the organizations taking days or less to respond
and contain the incident. This is far better than the norm, which is
typically weeks or longer.
COMPARING ATTACKS TO PATCH TIMEFRAMES
Wouldn’t it be great to know that (quickly) patching web What we found is a non-finding and the only valid conclusion
application vulnerabilities helps? This year we partnered to draw from this is that more work is needed to understand
with WhiteHat Security in order to combine and compare the relationship between web application vulnerabilities and
the incident data we’ve collected against the vulnerability security incidents. With a non-finding, we can only speculate
assessment data they collect from tens of thousands on why we are seeing these results. Perhaps this is telling us
of websites across hundreds of the most well-known that no industry is doing enough. We know three out of four
organizations. After some back and forth, we decided first to web-based compromises occur in hours or less of first contact,
break out the data by industries (because patterns emerge and maybe fixing vulnerabilities in 10 days versus 70 days
across industries), then we decided to compare two data doesn’t help all that much. Plus, the attacker only exploits one
points on web vulnerabilities to the incident data: the average (maybe two) vulnerabilities. But a different explanation could
(mean) vulnerabilities per site and median days to patch. be that our lens was focused too wide, and we could learn
We assumed that industries with fewer vulnerabilities and more by matching the high-quality WhiteHat data with specific
quicker patch time would be less represented in the breach incident data within the same sample. Whatever the causes,
data (i.e., have fewer incidents) and so we applied some good we do know that web application attacks occur often enough
old-fashioned statistics and were admittedly let down when to repeat what is said in the WhiteHat Website Security
we didn’t see the relationship4 we were expecting. Statistics Report,5 “What’s needed is more secure software,
NOT more security software.”
ATTACKS WEB
APP
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 21

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
RECOMMENDED CONTROLS
Single-password fail
The writing’s on the wall for single-factor, password-based
authentication on anything internet-facing. Even though it may
draw you out of a known comfort zone, if you’re defending a
web application seek out alternatives to this method of identity
verification. if you’re a vendor in the web application space, also
consider mandating alternative authentication mechanism for
your customers.
Rethink CMS
And we mean “rethink” in every way. if you’re committed to an
Figure 29.
active platform (Joomla!, Drupal, WordPress, etc.), then set up
Timespan of events within Web App Attacks
an automated patch process. if an automated patch process
isn’t viable, then develop a manual process and stick to it. This
is especially true for the third-party plugins. Another way to
rethink CMS is to consider a static CMS framework. instead of
executing code for every request and generating the content,
static CMS will pre-generate those same pages, removing the
need to execute code on the server for every request.
Validate inputs
Even though we’ve been tilting at this windmill for years,
the advice still holds true. The best way to be sure your web
application won’t be exploited is to seek out and fix the
vulnerabilities before the attackers do (and they will). if you don’t
have access to the source code and/or the developers, be sure
to have something in place (e.g., a contract) to fix the problems
when they’re found.
Enforce lockout policies
Brute force attacks aren’t the leading method in this section,
but they’re still worthy of mention. By instituting counter-
measures, such as a slowing down the rate of repeated attempts
or temporarily locking accounts with multiple failed attempts,
the rate of successful brute force attempts will more than likely
dissipate and disappear (although you may still be dealing with
that pesky bot poking at your accounts every now and then).
Monitor outbound connections
While many web-based attacks rely heavily on the existing
firewall bypass protocol (HTTP), many others change the victim’s
web server into a client. Critical points in the attack chain are
pulling additional malware to continue the attack, exfiltrating
compromised data, or attacking others on command. So unless
your server has a legitimate reason to send your data to Eastern
Europe or DoS’ing others is part of the business plan, try to lock
down your web server’s ability to do so.
07=n
yrevocsiD
14=n
tnemniatnoC
41%
17% 16%
11% 11%
3%
0% 0%
42%
29%
22%
5% 0% 2%
34=n
esimorpmoC
33=n
noitaretlfixE
42%
23%
19%
12%
5%
0% 0% 0%
27%
21% 21%
18%
9%
3%
0% 0%
0% 0%
sdnoceS setuniM sruoH syaD skeeW shtnoM sraeY reveN
Figure 28.
Top 5 discovery methods for ideologically motivated incidents
within Web App Attacks (n=775)
Total External 98%
Total Internal 2%
Ext - unrelated party 93%
Ext - fraud detection 4%
Ext - law enforcement 1%
Int - reported by user <1%
Ext - actor disclosure <1%
Ext - customer <1%
Int - unknown <1%
Int - antivirus <1%
Int - fraud detection <1%
Other <1%
PPA
BEW
SKCATTA
22 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
INSIDER AND PRIVILEGE MISUSE
AT A GLANCE
Description All incidents tagged with the action category of Misuse — any unapproved or malicious use of
organizational resources — fall within this pattern. This is mainly insider misuse, but outsiders
(due to collusion) and partners (because they are granted privileges) show up as well.
Top industries
Public, Real Estate, Administrative, Transportation, Manufacturing, Mining
Frequency
11,698 total incidents
112 with confirmed data disclosure
Key findings Most crimes by trusted parties are perpetrated for financial or personal gain. The most
noticeable shifts in the 2013 dataset, however, were an increase in insider espionage targeting
internal data and trade secrets, and a broader range of tactics. We say “2013 dataset” because we
do not believe the actual rate of such crimes increased significantly; we’re seeing the benefit of
increased visibility from insider-focused partners.
An organization’s intellectual property is among its most Figure 30 lists the top threat actions observed across incidents
valuable assets, frequently driving its ability to compete in the fitting the misuse pattern. Note that not all are within the
market. in many cases, organizations also have custody of vast misuse category [mis]; stay tuned for more on that later. Not
amounts of data about the customers they serve, the employees unexpectedly, privilege abuse — taking advantage of the
who serve them, and the relationships they rely upon to do system access privileges granted by an employer and using
business. This data has value to the organization, but also to them to commit nefarious acts — tops the list. We realize that
those who would seek it for their own personal benefit or myriad encompasses a very broad range of activities, but the overall
other reasons. For the misuse pattern, we focus on those who theme and lesson differ little: most insider misuse occurs within
already have a trusted place inside the organization. Arguably, the boundaries of trust necessary to perform normal duties.
the most prominent case of internal misuse in the headlines this That’s what makes it so difficult to prevent.
past year has been that of U.S. government contractor Edward
Remember that action varieties in VERiS are not mutually
Snowden. While this is an extreme example of the damage that
exclusive, and it’s common to see more than one in a single
determined insiders can inflict, it illustrates the risk that exists
incident. Unapproved hardware and email misuse/data
when an organization must place trust in individuals.
mishandling (tied) round out the top three actions in the
Figure 30. misuse category, but they’re more a function of how the data is
Top 10 threat action varieties within Insider Misuse (n=153) exfiltrated rather than how it’s acquired. Unapproved hardware
refers to employees using devices like USB drives that are
Privilege abuse [mis] 88% either forbidden altogether or allowed but subject to various
Unapproved restrictions. An employee sending intellectual property out to his
18%
hardware [mis]
or her personal address is an example of email misuse. We also
Bribery [soc] 16% reviewed cases where system administrators abused the email
Email misuse [mis] 11% system, posing as another user and sending messages under that
identity, with the goal of getting them fired. Data mishandling
Data mishanding [mis] 11%
takes place when someone uses data in a manner counter to
Use of stolen creds [hac] 7% the organization’s policies. For example, a call center employee
Unapproved who writes customer credit card numbers down on paper, or an
5%
workaround [mis] engineer who skirts policy by taking restricted documents home
Theft [phy] 4% to examine on a personal computer.
Unapproved
4%
software [mis]
Embezzlement [mis] 4%
PRiViLEGE
MiSUSE
iNSiDER
AND
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 23

With more incidents than ever before involving trusted  Let’s take a look at the people committing these crimes. While
 ELAS-FO-TNiOP
SNOiSURTNi parties, we could more easily see how they go about acquiring  payment chain personnel and end-users were still prominent,
the data when their own access is insufficient. in addition  managers (including those in the C-suite) came in higher than in
to abusing entrusted privileges and resources, we observed  prior years. You know the type; one of those straight shooters
hacking techniques to elevate privileges (often by stealing  with upper management written all over him. They often have
others’ credentials) and circumvent controls, various forms of  access to trade secrets and other data of interest to the
social engineering, and the use of malware like keyloggers and  competition and, tragically, are also more likely to be exempted
backdoors. These cads have even resorted to physical theft,  from following security policies because of their privileged
 PPA BEW SKCATTA
taking documents such as blueprints and other intellectual  status in the company.6 One of those “white-collar resort
property, often denying availability to the original organization  prisons” won’t do for their ilk.
by taking the only copy.
Figure 33.
Figure 31.  Variety of external actors within Insider Misuse (n=25)
ESUSiM EGELiViRP ESUSiM EGELiViRP
Vector for threat actions within Insider Misuse (n=123)
 DNA REDiSNi  DNA REDiSNi
Organized crime
36%
|     | LAN access |     | 71% |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- |
Former employee 24%
|     | Physical access | 28% |     |     |     |     |
| --- | --------------- | --- | --- | --- | --- | --- |
Unaffiliated 24%
|     | Remote access | 21% |     |            |     |     |
| --- | ------------- | --- | --- | ---------- | --- | --- |
|     |               |     |     | Competitor |     | 16% |
 TFEHT LACiSYHP
|          | Other 2%         |     |     |              |     |     |
| -------- | ---------------- | --- | --- | ------------ | --- | --- |
| SSOL DNA |                  |     |     | Acquaintance |     | 8%  |
|          | Non-corporate 1% |     |     |              |     |     |
As mentioned in the beginning of this section, insiders aren’t the
it’s also worth noting that the corporate LAN was the vector in
only ones who misuse entrusted privileges and resources. Figure
71% of these incidents, and 28% took advantage of physical
33 gives an account of external and partner actors who directly
 SUOENALLECSiM
access within the corporate facility. This means the majority of
or indirectly participated in incidents of misuse. Organized
| SRORRE employees perpetrated their acts while in the office right under  |     |     |     |     |     |     |
| ------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- |
criminals bribe insiders to steal data for fraud schemes. Former
the noses of coworkers, rather than hopping through proxies
employees exploit still active accounts or other holes known
from the relative safety of their house. if someone wants to use
only to them. Competitors solicit intellectual property to gain
these statistics to loosen up work-at-home policies and tear
business advantages. To mount a proper defense, organizations
down cube farms in favor of more open floor plans — you have
must take into account that such players are on the field.
our blessing.
ERAWEMiRC
Nearly all misuse incidents prior to 2013 centered on obtaining
Figure 32.
information to use for fraud. As Figure 34 shows, we saw more
Top 10 varieties of internal actors within Insider Misuse (n=99) insider espionage targeting internal organizational data and
trade secrets than ever before.
|               | Cashier  |     | 23% |                                             |     |     |
| ------------- | -------- | --- | --- | ------------------------------------------- | --- | --- |
|  DRAC TNEMYAP | End-user |     | 17% | Figure 34.                                  |     |     |
| SREMMiKS      |          |     |     | Actor motives within Insider Misuse (n=125) |     |     |
|               | Finance  | 13% |     |                                             |     |     |
Financial 72%
|     | Manager     | 13% |     |           |     |     |
| --- | ----------- | --- | --- | --------- | --- | --- |
|     | Call center |     |     | Espionage |     | 18% |
9%
Grudge 10%
|     | Executive | 7%  |     |     |     |     |
| --- | --------- | --- | --- | --- | --- | --- |
EGANOiPSE
|  -REBYC | Other | 7%  |     | Convenience | 4%  |     |
| ------- | ----- | --- | --- | ----------- | --- | --- |
Fun 3%
|     | Developer    | 6%  |     |     |        |     |
| --- | ------------ | --- | --- | --- | ------ | --- |
|     | System admin | 6%  |     |     | N/A 2% |     |
Auditor 1% According to The Recover Report,7 published by one of our DBiR
contributors, Mishcon de Reya, the two most common scenarios
SKCATTA
|  SOD |     |     |     | involve perpetrators taking the data to: |     |     |
| ---- | --- | --- | --- | ---------------------------------------- | --- | --- |
•  Start their own competing company (30%).
•  Help secure employment with a rival (65%).
This kind of thing is certainly not new — it’s largely due to the
  GNiHTYREVE addition of more contributors who have a view into this type of
activity than ever before. So, whether it’s fraud-ready data sold
ESLE
on the quick to criminals or internal secrets eventually sold to a
competitor, insider crime is still “all about the Benjamins, baby.”
| 24  |     |     |     |     |     | VERIZON ENTERPRISE SOLUTIONS |
| --- | --- | --- | --- | --- | --- | ---------------------------- |

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
Figure 35. Discovery methods for the majority of breaches have
Variety of at-risk data within Insider Misuse (n=108) traditionally been dominated by external signals. For insider
misuse, however, internal methods (55%) are responsible for
Personal 34% detecting more incidents than external methods (45%). The most
common way organizations detected insider crimes was when
Payment 29%
employees reported them. Discoveries triggered by financial
Internal 27% and iT audits were also very common. Reviewing the books on
Secrets 18% Monday morning is an example of the former, and a promising
example of the latter is a regular process to review access for
Bank 14%
exiting employees.
Credentials 9%
The CERT insider Threat Center (another partner of ours)
Medical 3% focuses research on insider breaches, and it determined that
in more than 70% of the iP theft cases, insiders stole the
Other 3%
information within 30 days of announcing their resignation.8
Unknown 2% On quite a few occasions, a review of the activity of outgoing
employees with access to sensitive information allowed
Classified 1%
impacted organizations to detect the incident and act quickly to
Desktops are the most frequently compromised asset in this retrieve the information (hopefully before irreparable damage
pattern, which makes sense because desktop computers are had been done).
an employee’s primary interface to the rest of the network
Figure 37.
(Figure 36). Typically, this is where the data is stored, uploaded,
Top 10 discovery methods within Insider Misuse (n=122)
or emailed out of the organization, or copied onto removable
media. Databases and file servers, both repositories of so much Total External 45%
valuable information, are also targeted regularly. Payment
Total Internal 55%
cards doesn’t refer to the variety of data, but rather actual
cards that were run through handheld skimming devices (or Ext - customer 16%
otherwise copied) in the classic “evil waiter” scenario. As far
Int - reported by user 13%
as asset ownership, we see insiders abusing corporate-owned
rather than employee-owned (“BYOD”) assets allowed for Int - unknown 11%
corporate use. However, we do see evidence they often leverage
Int - financial audit 10%
unapproved personal devices to help them get the data out of the
organization (which shows up as use of unapproved hardware). Int - IT audit 9%
Figure 36. Ext - fraud detection 8%
Top 10 assets affected within Insider Misuse (n=142) Ext - unknown 6%
Ext - law
Desktop 26% enforcement 6%
(user dev)
Database 25% Int - fraud detection 6%
(server)
Other 22% Ext - audit 3%
(server)
Payment card 12%
(media)
Cashier
10%
(people)
File 9%
(people)
Other 8%
(people)
Web application 8%
(server)
Unknown 6%
Laptop 5%
(user dev)
PRiViLEGE
MiSUSE
iNSiDER
AND
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 25

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
Note the discovery timeline for misuse in Figure 38 — it looks RECOMMENDED CONTROLS
very different from the overall timeline we see for other types
The root cause of data theft and other illicit acts by trusted
of incidents. The majority of the misuse incidents were detected
parties is, rather obviously, an employee breaking bad. No, not
within days (which is great), but there’s also a not insignificant
in a Walter White sense; more like a white collar crime sense
number of incidents (70 to be exact) that took years to discover
(though Walter did ***SPOiLER ALERT*** murder his boss
(which ain’t so great).
and execute a forced takeover of the business, so it is rather
Figure 38. apropos). While it’s impossible to stop all rogue employees, there
Discovery timeline within Insider Misuse (n=1,017) are some steps that can reduce the likelihood of an incident
occurring, or at least increase your chances of catching it quickly.
Seconds 32%
Know your data and who has access to it
Minutes 7%
Hours 28% The first step in protecting your data is in knowing where it is,
and who has access to it. From this, build controls to protect it
Days 22%
and detect misuse. it won’t prevent determined insiders (because
Weeks 8%
they have access to it already), but there are many other benefits
Months 4% that warrant doing it.
Years <1%
Review user accounts
Having identified the positions with access to sensitive data,
implement a process to review account activity when those
employees give notice or have been released. Disable user
accounts as soon as an employee leaves the company (and, if
warranted, before that). This has proven successful in either
preventing the data from leaving the organization, or in
retrieving it quickly to contain the incident.
Watch for data exfiltration
in the top misuse varieties, we see actions that facilitate the
data transfer out of the organization — these are excellent
places to set up controls to detect this type of activity. Many
data loss prevention products cover the most common actions
taken to steal sensitive information, and these are certainly
worth exploring.
Publish audit results
From an awareness perspective, regularly publish anonymized
results of audits of access. Let employees know that there are
consequences and that the policies are being enforced. This can
act as a powerful deterrent to bad behavior.
DNA
REDiSNi
ESUSiM
EGELiViRP
26 VERIZON ENTERPRISE SOLUTIONS

PHYSICAL THEFT AND LOSS
POiNT-OF-SALE
iNTRUSiONS
AT A GLANCE
Description Pretty much what it sounds like — any incident where an information asset went missing, whether
|     | through misplacement or malice. |     |     | ATTACKS WEB APP  |
| --- | ------------------------------- | --- | --- | ---------------- |
Top industries
Healthcare, Public, Mining
| Frequency | total incidents9 |     |     |     |
| --------- | ---------------- | --- | --- | --- |
9,704
PRiViLEGE MiSUSE
116 with confirmed data disclosure
iNSiDER AND
Key findings Loss is reported more often than theft. in a surprising finding, we discovered that assets are
stolen from corporate offices more often than personal vehicles or residences. And while
personal and medical information is commonly exposed, most losses/thefts are reported
because of mandatory disclosure regulations rather than because of fraud.
PHYSiCAL THEFT  PHYSiCAL THEFT
AND LOSS AND LOSS
To be honest, we debated whether or not to include a section on  noteworthy that this is the only incident pattern that applies
lost and stolen assets in this report. We decided, however, that  across the board. Even farmers have problems with people that
we simply couldn’t ignore the blatant fact that such incidents  come and try to snatch their crops laptops.
— while not sexy or “cyber-y” — are among the most common
Speaking of laptops, they’re the most common variety of asset
MiSCELLANEOUS
causes of data loss/exposure reported by organizations. This
reported with this pattern. incident reports — especially to
is especially apparent in industries like Healthcare, where the  ERRORS
CSiRTs — often don’t specify the asset lost or stolen. Thus,
disclosure of all incidents that potentially expose sensitive data
“some kind of user device” is all we can infer and explains why
is mandatory. And if there’s anything we know to be true about
“Other (user dev)” is so frequent. Beyond that, it’s what you’d
human nature, it’s that losing things and stealing things seem to
expect: computers, documents, and drives.
be inherent predispositions.
The next thing to note is the ratio of loss to theft; losing
Studying the findings yielded a few interesting observations  CRiMEWARE
information assets happens way more than theft, by a 15-to-one
that may help inform practice, and that’s where we’ll focus our
difference. And that’s important because it suggests the vast
attention in this section. As we begin, keep in mind that we’re
majority of incidents in this pattern are not due to malicious
specifically talking about information assets;10 whatever was
or intentional actions. Thus, the primary challenge is to a) keep
lost or stolen had to store, process, or transmit information in
employees from losing things (not gonna happen) or b) minimize
order to get our attention.
|     |     | the impact when they do. The smart money is on option b, though  |     | PAYMENT CARD  |
| --- | --- | ---------------------------------------------------------------- | --- | ------------- |
SKiMMERS
Observation #1 relates to demographics; we have evidence  bio-implanted computing devices do hold some future promise
that every type and size of organization loses stuff and/or has  for option a. That’s about all we’re going to say about loss, but
stuff stolen. That may not be much of a shock, but it’s at least  theft still has a few more lessons for us.
| Figure 39.  |     | Figure 40.  |     |     |
| ----------- | --- | ----------- | --- | --- |
Top 10 action varieties of Theft/Loss (n=9,678) Top 10 locations for theft within Theft/Loss (n=332)
ESPiONAGE
| Other |     |     |     | CYBER-  |
| ----- | --- | --- | --- | ------- |
892 Victim work area 43%
(user dev)
Laptop 308
Personal vehicle 23%
(user dev)
Documents
|     | 140 | Personal residence | 10% |     |
| --- | --- | ------------------ | --- | --- |
(media)
| Desktop     | 108 |                    |     |         |
| ----------- | --- | ------------------ | --- | ------- |
| (user dev)  |     | Victim secure area | 5%  |         |
| Flash drive |     |                    |     | ATTACKS |
|             | 102 | Partner facility   | 4%  | DOS     |
(media)
| Disk drive | 37  | Partner vehicle | 4%  |     |
| ---------- | --- | --------------- | --- | --- |
(media)
Tapes
|     | 36  | Public facility | 3%  |     |
| --- | --- | --------------- | --- | --- |
(media)
Other
|          | 27  | Victim grounds | 2%  |              |
| -------- | --- | -------------- | --- | ------------ |
| (server) |     |                |     | EVERYTHiNG   |
| Other    | 12  |                |     |              |
|          |     | Public vehicle | 2%  | ELSE         |
(media)
Database
|     | 11  | Victim public area | 2%  |     |
| --- | --- | ------------------ | --- | --- |
(server)
| VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT |     |     |     | 27  |
| ---------------------------------------------- | --- | --- | --- | --- |

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
We find it quite surprising that the highest proportion of thefts RECOMMENDED CONTROLS
occur in the victim’s work area, which basically refers to the
The primary root cause of incidents in this pattern is
main office space or cube farm (Figure 40). That suggests
carelessness of one degree or another. Accidents happen. People
simply having sensitive information “behind locked doors” isn’t
lose stuff. People steal stuff. And that’s never going to change.
enough; there are still a lot of people inside those locked doors.11
But there are a few things you can do to mitigate that risk.
Notice that thefts in internal high security areas are much less
common, but still post higher than public facilities. That last bit
is counterintuitive to the point of irrationality; we can’t help but Encrypt devices
suspect that people whose laptops are stolen when they take a
potty break at the coffee shop simply report them as “lost” to Considering the high frequency of lost assets, encryption is
save face. as close to a no-brainer solution as it gets for this incident
pattern. Sure, the asset is still missing, but at least it will save
Personal residences and personal/partner/public vehicles serve
a lot of worry, embarrassment, and potential lawsuits by simply
as the venue for nearly 40% of thefts and remind us that devices
being able to say the information within it was protected. Also,
on the go are prone to go missing.
periodically checking to ensure encryption is still active is
Figure 41. right up there too. This will come in handy when the auditor or
Vector of physical access within Theft/Loss (n=158) regulator asks that dreaded question: “How do you know for sure
it was encrypted?”
Disabled controls 60%
Keep it with you
Bypassed controls 26%
Privileged access 11% Encourage employees to keep sensitive devices in their
Uncontrolled location 3% possession and in sight at all times. Yes, this applies to fancy
client dinners and visits to the restroom. it’s not a bad principle
to apply to mobile devices in a corporate setting either. it may
While it’s usually not known/reported exactly how actors gained
be awkward, but it’s safer than leaving it in the car or unattended
physical access to these locations, over 80% of thefts where we
in a room full of strangers. if it absolutely must be left in the car,
do have that info involved disabling or bypassing controls. The
lock it in the trunk before you leave the office and don’t leave it
remainder had access already, either because they were granted
there overnight.
privileges or because it was a publicly accessible location.
Back it up
Figure 42.
Variety of at-risk data within Theft/Loss (n=3,824)
Regular (and preferably automatic) backups serve a threefold
purpose. They salvage weeks/months/years’ worth of
Personal 3,393
irrecoverable work, get you productive again on a new device
Medical 508 with minimal down time, and help establish what data was on the
Payment 23 device to determine if disclosure is necessary.
Internal 21
Lock it down
Bank 20
Classified 5 in light of the evidence that so many thefts occur in the office,
cabling or otherwise securing equipment to immovable fixtures
Credentials 5
should at least be considered. The big caveat, however, is that
Unknown 4 the majority of such thefts were documents taken from the filing
Secrets 3 cabinet and mobile devices (including laptops). A more effective
strategy would be to move highly sensitive or valuable assets to
Other 1
a separate, secure area and make sure they stay there.
The final set of observations covers the variety of data that
was compromised or, more often, potentially exposed when BONUS - Use unappealing tech
assets were lost or stolen. it’s worth pointing out that the
primary reason most of these incidents are included is because Yes, it’s unorthodox as far as recommendations go, but it might
they tripped some kind of mandatory reporting/disclosure actually be an effective theft deterrent (though it will probably
requirement. The asset went missing, was determined to increase loss frequency). That shiny new MacBook Air on the
contain regulated information that is now exposed to potential passenger seat may be too tempting for anyone to resist, but
unauthorized access, and therefore had to be reported. This only those truly dedicated crooks will risk incarceration for a 4”
explains the predominance of regulated data like personal or thick mid-90’s lap brick. Or, if being the fastest hunk of junk in
identifying information and medical records in Figure 42. the galaxy is a must, perhaps there’s a lucrative aftermarket for
clunky laptop covers. She may not look like much, but she’s got it
where it counts, kid.
TFEHT
LACiSYHP
SSOL
DNA
28 VERIZON ENTERPRISE SOLUTIONS

MISCELLANEOUS ERRORS
POiNT-OF-SALE
iNTRUSiONS
AT A GLANCE
Description incidents where unintentional actions directly compromised a security attribute of an
information asset. This does not include lost devices, which is grouped with theft instead. ATTACKS WEB APP
Top industries
Public, Administrative, Healthcare
|     | Frequency |     |     | total incidents12 |     |     |
| --- | --------- | --- | --- | ----------------- | --- | --- |
16,554
PRiViLEGE MiSUSE
412 with confirmed data disclosure
iNSiDER AND
Key findings After scrutinizing 16K incidents, we’ve made a startling discovery — people screw up sometimes.
(Nobel Prize, here we come!) The data seems to suggest that highly repetitive and mundane
business processes involving sensitive info are particularly error prone. it’s also noteworthy that
this pattern contains more incidents caused by business partners than any other.
PHYSiCAL THEFT
AND LOSS
Nearly every incident involves some element of human error.
Misdelivery (sending paper documents or
For example, failing to apply a WordPress patch certainly leaves
the application vulnerable to attack, but it doesn’t directly  emails to the wrong recipient) is the most
compromise the system. Some other threat actor/action is
|     |     |     | frequently seen error resulting in data  |     |     | MiSCELLANEOUS  MiSCELLANEOUS  |
| --- | --- | --- | ---------------------------------------- | --- | --- | ----------------------------- |
required to do that. Without drawing that distinction, this
|     |     |     | disclosure. |     |     | ERRORS ERRORS |
| --- | --- | --- | ----------- | --- | --- | ------------- |
category would be so bloated with “incidents” that it would be
difficult to extract useful information.
There are only two difficult problems in computer science: cache
it’s also worth noting that this pattern doesn’t include every
invalidation, naming things, and off-by-one errors. Misdelivery
incident in the Error category. Loss is a type of error, but we
(sending paper documents or emails to the wrong recipient)
grouped it with theft (under Physical) in a different pattern
|     |     |     | is the most frequently seen error resulting in data disclosure.  |     |     | CRiMEWARE |
| --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --------- |
because they share certain similarities (you no longer possess
One of the more common examples is a mass mailing where
the device) and because it’s often difficult to determine loss vs.
the documents and envelopes are out of sync (off-by-one)
theft. Please keep this in mind as you view the top actions and
and sensitive documents are sent to the wrong recipient. A
assets in this section.
mundane blunder, yes, but one that very often exposes data to
unauthorized parties.
PAYMENT CARD
SKiMMERS
| Figure 43.  |     |     | Figure 44.  |     |     |     |
| ----------- | --- | --- | ----------- | --- | --- | --- |
Top 10 threat action varieties within Miscellaneous Errors  Top 10 assets affected within Miscellaneous Errors (n=546)
(n=558)
Documents
49%
(media)
Misdelivery 44%
|     |     |     |     | Web application | 14% |     |
| --- | --- | --- | --- | --------------- | --- | --- |
(server)
ESPiONAGE
| Publishing error |     |     | 22% | Desktop |     |         |
| ---------------- | --- | --- | --- | ------- | --- | ------- |
|                  |     |     |     |         | 9%  | CYBER-  |
(user dev)
| Disposal error |     |     | 20% | File |     |     |
| -------------- | --- | --- | --- | ---- | --- | --- |
7%
(server)
| Misconfiguration |     | 6%  |     | Database | 5%  |     |
| ---------------- | --- | --- | --- | -------- | --- | --- |
(server)
| Malfunction |     | 3%  |     | Other |     |     |
| ----------- | --- | --- | --- | ----- | --- | --- |
5%
(server)
|                   |     | 3%  |     | Mail     |     |         |
| ----------------- | --- | --- | --- | -------- | --- | ------- |
| Programming error |     |     |     |          | 4%  |         |
|                   |     |     |     | (server) |     | ATTACKS |
DOS
|     | Gaffe | 1%  |     | Disk media | 3%  |     |
| --- | ----- | --- | --- | ---------- | --- | --- |
(media)
|     | Omission | 1%  |     | Disk drive |     |     |
| --- | -------- | --- | --- | ---------- | --- | --- |
1%
(media)
|     | Other | 1%  |     | Other | 1%  |     |
| --- | ----- | --- | --- | ----- | --- | --- |
(media)
| Maintenance error |     | <1% |     |     |     | EVERYTHiNG   |
| ----------------- | --- | --- | --- | --- | --- | ------------ |
ELSE
| VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT |     |     |     |     | 29  |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- |

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
Figure 45.
GOVERNMENT MISDELIVERY
Discovery and containment timeline within Miscellaneous
According to our sample, government organizations Errors
frequently deliver non-public information to the wrong Discovery n=127 Containment n=55
recipient; so much so, in fact, that we had to remove it from
Seconds 3% 6%
Figure 43 so that you could see the other error varieties.
Why is that number so large? The United States federal Minutes 9% 4%
government is the largest employer in that country, and Hours 10% 38%
maintains a massive volume of data on both its employees
Days 17% 27% and constituents, so one can expect a high number of
misdelivery incidents. Public data laws and mandatory Weeks 6% 13%
reporting of security incidents also cover government
Months 47% 6%
agencies. Since we have more visibility into government
mistakes, it creates the impression that government Years 8% 2%
mistakes happen more frequently than everyone else’s,
Never 0% 6%
which may not be the case. This is not unlike the way we
see higher numbers of overall breaches in U.S. states that
have had disclosure laws on the books the longest. Case
Organizations only discover their own mistakes about one-third
in point: even with government misdelivery removed from
of the time. Otherwise, an external entity makes them aware
the results, misdelivery still dominates the list of errors
of the incident, and most frequently it’s the organization’s own
resulting in exposed data.
customers. You could try the “inconceivable!” tactic when a
customer calls to say they found their unprotected personal data
on your website — but if you keep using that word, they’ll figure
Oxford Dictionaries declared that “selfie” was 2013’s word of
out it doesn’t mean what you think it means.
the year,13 but did you know that posting content to the web and
later regretting it was a meme in the corporate world too? That’s Figure 46.
right, the second most frequent error variety is publishing errors, Top 10 discovery methods for Miscellaneous Error incidents
which often involve accidentally posting non-public information (n=148)
to a public resource, such as the company web server. That’s
why web application takes the number two spot on the affected Total External 68%
assets chart (Figure 44). Rounding out the top three in this
Total Internal 32%
category is disposal error, where the affected asset is thrown
away without being shredded or, in the case of digital media,
Ext-customer 30%
properly cleared of sensitive data.
Ext-unrelated party 25%
Who’s making all these mistakes? Well, it’s Int-reported by user 18%
almost entirely insiders, of course. End-users, Other 12%
sysadmins, and developers lead the pack when
Int-unknown 5%
it comes to mucking things up, though pretty
Int-IT audit 3%
much all of us are guilty.
Ext-law enforcement 2%
Ext-actor disclosure 2%
Who’s making all these mistakes? Well, it’s almost entirely
insiders, of course. End-users, sysadmins, and developers lead Ext-audit 1%
the pack when it comes to mucking things up, though pretty much
Int-log review 1%
all of us are guilty. But the interesting thing is that there’s quite a
large number of incidents (70) caused by partner errors — more
than any other pattern.
SUOENALLECSiM
SRORRE
30 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
RECOMMENDED CONTROLS
IMPRISONED RESPONSE: THE FUTURE OF IR?
Bob Ross, everyone’s favorite painter of fluffy little clouds, once
An example from the VCDB shows how bad things can get
said, “We don’t make mistakes, we just have happy accidents.”
when document disposal goes wrong. A medical center
Even still, organizations can take steps to decrease the
arranged to have a vendor pick up documents and shred
frequency of all manner of accidents by reducing their exposure
them prior to disposal. Apparently, an actual “pickup” truck
to the common error patterns that result in data disclosure.
was used, because the files ended up all over the roadside
instead. “it looked like a blizzard of white paper had struck
Keep it on the DLP the area,” according to one witness. These were old medical
records with all manner of protected information. When
Consider implementing Data Loss Prevention (DLP) software people found them and called law enforcement, an inmate
to reduce instances of sensitive documents sent by email. DLP crew doing regular trash pickup in the area was sent to
can identify information that follows a common format, such as retrieve these sensitive documents. And that’s the sound of
credit card numbers, social security numbers, or medical billing the men working on the “cha-ching” gang.
codes.
Check out the pub
Decrease the frequency of publishing errors by tightening up
processes around posting documents to internal and external
sites. For example, have a second reviewer approve anything
getting posted to company servers, develop processes to
regularly scan public web pages for non-public data, and
implement a blanket prohibition against storing un-redacted
documents on a file server that also has a web server running. it’s
amazing how easy it is for a spreadsheet to migrate over to the
htmldocs folder. Make sure there’s a process to test the security
controls after a change — we’ve often seen a failure to put
controls back in place result in a publishing breach.
Nail the snail mail fail whale
Say that three times really fast. When sending large postal
mailings (also prone to error at higher speed and repetition),
spot-check a sample to ensure that the information in the
document matches the name on the envelope. Watch out for
window envelopes too – sometimes that window might be too
big or your content might not be centered properly, allowing
sensitive information to show through. A lot of these incidents
could have been prevented if someone had popped a few
envelopes off the stack and inspected them before they went in
the mail.
IT don’t make trash
iT burns it. Any disposal or sale of information assets should
be coordinated by the iT department. Educate users to think of
disposing of a computer the same way they think of disposing
of hazardous materials. “You can’t just throw that in the trash
(or sell it on eBay)! Send it to iT for proper handling.” Test the
disposal process by sampling devices to verify they’ve been
sanitized properly. if a third-party handles this, ensure that
contracts stipulate how to transfer, store, and dispose of data,
along with roles, responsibilities, verification, and penalties for
non-compliance.
ERRORS
MiSCELLANEOUS
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 31

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
CRIMEWARE
AT A GLANCE
Description Any malware incident that did not fit other patterns like espionage or point-of-sale attacks. We
labeled this pattern “crimeware” because the moniker accurately describes a common theme
among such incidents. in reality, the pattern covers a broad swath of incidents involving malware
of varied types and purposes.
Top industries
Public, information, Utilities, Manufacturing
Frequency 12,535 total incidents
50 with confirmed data disclosure
Key findings The primary goal is to gain control of systems as a platform for illicit uses like stealing
credentials, DDoS attacks, spamming, etc. Web downloads and drive-bys are the most common
infection vectors.
Many incidents in this section come from our CSiRT partners, This one primarily targets Android and Blackberry mobile
reflecting a roll-up across many victim organizations. The devices for similar purposes. While Zeus serves as an example
level of detail tends to be lower because there was no forensic of crimeware families reported all around the world, others had
investigation or similar in-depth analysis (or the report wasn’t a more localized presence. Nitol, for instance, was quite common
provided to the CSiRT), leaving VERiS metrics a bit sparse. among incidents reported to MyCERT of Cybersecurity Malaysia,
But the high number of incidents still offers some insight into but we have no instances of it infecting systems outside Asia.
day-to-day malware infections where the victim’s anti-virus (AV) Nitol allows backdoor access and frequently causes infected
and intrusion prevention system (iPS) shields could not repel systems to participate in DDoS attacks.
firepower of that magnitude.
Expanding online markets, where specialists offer cybercrime-
As expected, this incident pattern consists mainly of as-a-service, became a growing trend in 2013. A good example
opportunistic infections tied to organized criminals with some in the Netherlands was the wave of DDoS attacks on banks
kind of direct or indirect financial motive (hence the title and specific institutions since March, 2013. So-called “booter
“crimeware”). Once malicious code has acquired a level of access websites” have made this type of attack available to literally
and control of a device, the myriad possibilities to make a buck anyone who wants to attack a company or institution. Naturally,
are opened up for the attacker. a host of other malware families made appearances last year, but
these two stood out to us as worthy of a brief mention.
in not-so-shocking news, Zeus continues to be a favorite way
to make a buck with crimeware in 2013 (see sidebar for more Figure 47.
detail). Zeus and its offspring, Citadel, primarily focus on Top 10 threat action varieties within Crimeware (n=2,274)
stealing money via bank account takeovers, though they can also
be used for other functions. Zitmo (“Zeus in the Mobile”) also
C2 86%
shows up in the data.14
Unknown 24%
Spyware/keylogger 13%
ZEUS
Downloader 10%
Zeus (sometimes called “Zbot”) is sort of the cockroach of
malware. it has managed to survive and even thrive despite Spam 9%
many attempts to eradicate it. international arrests and the
Client-side attack 6%
supposed retirement of the original author have not slowed
Backdoor 4%
it down, and once the source code behind it was published,
other programmers could modify and extend Zeus for their DoS 4%
own purposes, including evading antivirus software. in fact,
Adware 2%
Citadel started off as a variant of Zeus but has evolved
substantially. Zeus can be used to install other malware Export data 1%
but often grabs login and banking credentials from within
browsers. Despite the efforts of many, it has continued to
elude the good guys that are trying to shut it down.
ERAWEMiRC
32 VERIZON ENTERPRISE SOLUTIONS

Victims don’t always report malware functionality, but when they  Figure 50.
POiNT-OF-SALE
do, they prefer C2 (according to the most interesting CSiRTs  Top 10 assets affected within Crimeware (n=1,557) iNTRUSiONS
in the world, at least). This makes perfect sense, as the goal is
Other 43%
to achieve and maintain control of a device to command it to
(server)
| do your bidding. Whether the little compromised minions are  |     | Other |     |     |
| ------------------------------------------------------------ | --- | ----- | --- | --- |
19%
(user dev)
participating in a spam botnet, stealing banking credentials, or
|                                                                  | Web application |          | 14% |     |
| ---------------------------------------------------------------- | --------------- | -------- | --- | --- |
| hijacking a browser to artificially boost ad revenue, there are  |                 | (server) |     |     |
Mail
| numerous ways to leverage compromised workstations that  |     |          | 13% |                  |
| -------------------------------------------------------- | --- | -------- | --- | ---------------- |
|                                                          |     | (server) |     | ATTACKS WEB APP  |
don’t entail deeper penetration into a network.
|     |     | Other | 10% |     |
| --- | --- | ----- | --- | --- |
(people)
| Figure 48.  |     | Desktop |     |     |
| ----------- | --- | ------- | --- | --- |
7%
| Top 10 vectors for malware actions within Crimeware (n=337) |     | (user dev) |     |                  |
| ----------------------------------------------------------- | --- | ---------- | --- | ---------------- |
|                                                             |     | Unknown 3% |     |                  |
| Web drive-by                                                | 43% |            |     | PRiViLEGE MiSUSE |
|                                                             |     | Laptop <1% |     |                  |
iNSiDER AND
(user dev)
| Web download | 38% | End-user |     |     |
| ------------ | --- | -------- | --- | --- |
<1%
(people)
Network propagation 6%
|     |     | Mobile phone <1% |     |     |
| --- | --- | ---------------- | --- | --- |
(user dev)
Email attachment 5%
Like us, your first reaction might be “why not technologies like
Email link 4%
iDS and AV?” This reflects the role of CSiRTs as the primary  PHYSiCAL THEFT
AND LOSS
Download by malware 2% provider of crimeware incidents in this dataset. The discovery
method wasn’t known for 99% of incidents; it’s not usually within
Other 2%
their visibility or responsibility. For all we know, CSiRTs only saw
Remote injection 1% the 1% not discovered by AV or iDS. The discovery timeline in
Figure 52 hints that this might, in fact, be the case. Notice the
Unknown 1%
MiSCELLANEOUS
difference in N between Figure 51 and Figure 52 and how many
Removable media  1%
infections are discovered within seconds — only automated  ERRORS
The majority of crimeware incidents start via web activity —  detection methods would be so quick.
downloads or drive-by infections from exploit kits and the like
Figure 51.
— rather than links or attachments in email.15 Adware still shows
External vs. internal discovery methods within Crimeware
up, though Bonzi Buddy thankfully remains extinct. For malware
(n=183)
with a social engineering component, both scams and phishing
CRiMEWARE CRiMEWARE
play important roles.16 infected assets usually weren’t identified,
but interestingly, those that were reported more servers than  External discovery 84%
user devices. Wow. So vectors. Much families. Many incident.
|     | Internal discovery | 16% |     |     |
| --- | ------------------ | --- | --- | --- |
Figure 49.
Variety of at-risk data within Crimeware (n=73) PAYMENT CARD
Figure 52.
SKiMMERS
Credentials 82% Discovery timeline within Crimeware (n=1,017)
| Bank | 71% |         |     |     |
| ---- | --- | ------- | --- | --- |
|      |     | Seconds | 32% |     |
Payment 14%
|     |     | Minutes 7% |     |     |
| --- | --- | ---------- | --- | --- |
4%
Personal
|            |     | Hours | 28% | ESPiONAGE |
| ---------- | --- | ----- | --- | --------- |
| Unknown 4% |     |       |     | CYBER-    |
|            |     | Days  | 22% |           |
Internal 3%
|     |     | Weeks 8% |     |     |
| --- | --- | -------- | --- | --- |
Secrets 1%
|     |     | Months 4% |     |     |
| --- | --- | --------- | --- | --- |
Crimeware incidents are light on timeline and discovery details  Years <0.1%
ATTACKS
because the response is often to just wipe the system and  DOS
get it back to work (remember, this pattern comprises a lot of
one-off infections that don’t fit other patterns). When known,
notification by unrelated third parties (namely CSiRTs) were by
far the most common way victims learned of the incident.
EVERYTHiNG
ELSE
| VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT |     |     |     | 33  |
| ---------------------------------------------- | --- | --- | --- | --- |

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
RECOMMENDED CONTROLS
A YEAR IN THE LIFE OF THE POLISH CERT
These results led us to develop some specific recommendations
to help keep incidents of crimeware down. The natural question By the CERT Polska/NASK
to ask is “what happened to antivirus?” AV technologies
The internet threat landscape in Poland is largely defined by
play an important role in catching many types of commodity
banking Trojans — crimeware aimed at stealing users’ online
malware and preventing compromise in the first place. So this
banking credentials. These use a combination of social
pattern reflects a reverse sort of “survivorship bias” in which
engineering and software vulnerabilities to gain access to
we look primarily at the sorts of things AV does not do as well
a user’s computer, and subsequently to their bank account.
— or organizations that don’t do AV particularly well. Nitol, in
Whenever new financial malware or attack methods surface,
particular, infected many systems at the factory before shipping
Polish users are often among the first hit. 2013 also saw
and likely before users or administrators had deployed any
numerous financial malware botnets using Polish internet
sort of AV. The Zeus and Citadel family has a well-deserved
properties for C2 purposes (including .pl ccTLD domain
reputation for evolving quickly to evade signature-based
names). Over 20 such botnets were taken over or disrupted
detection of the sort used by many AV products.
by CERT Polska.
The attacker’s tool of choice is a variety of web-inject
Keep browsers up to date
malware (with Zeus/Citadel being the most popular
malware family), which infects a user’s machine, and then
Zeus frequently uses a technique called “man in the browser”
injects code into the browser whenever that user visits a
that involves using browser vulnerabilities and add-on functions.
banking site deemed of interest (a “Man-in-the-Browser”
Keeping browsers and plugins secure will go a long way toward
attack). A common theme is the use of social engineering
reducing the impact of this sort of incident. Apply browser techniques to obtain credentials. For example, attempts
patches as quickly as software producers make them available.
are made to install one-time password stealers to intercept
mobile transaction authentication numbers (mTANs) used
Disable Java in the browser
by banks to authenticate transactions. in such cases, a
user is prompted to provide his mobile number, supposedly
Legacy apps may complicate this, but if possible, avoid using
to install a new security certificate designed by the bank
Java browser plugins, given the difficulty in sandboxing content
on his smartphone – but what, in reality, is malware used
and the history of vulnerabilities here.
to intercept and redirect text messages to the attacker.
Cruder methods to subvert two-factor authentication
Use two-factor authentication
are also employed: fictitious bank messages are injected,
notifying the recipient of an erroneous bank transfer and
Our results link crimeware to stolen credentials more often than
asking for the money to be returned - to an attacker’s
any other type of data. This points to the key role of crimeware
account. Real world events are often exploited: a recent
when the attack objective is to gain access to user accounts.
brand merger involving the largest Polish online bank
Two-factor authentication won’t prevent the theft of credentials,
resulted in attacks forcing users to redefine lists of
but it will go a long way toward preventing the fraudulent re-use
permanent transfers – redirecting them to an attacker’s
of those credentials.
bank numbers – under the auspices of changes resulting
from the merger.
Change is good…except when it isn’t
However, it’s not just web-inject malware at work: other
Consider how best to deploy system configuration change tricks observed in 2013 include malware that switches
monitoring. Unlike iocane powder, many of the vectors and bank account numbers to those of the attacker during a
persistence methods used by crimeware can be easily detected copy/paste operation in Microsoft Windows. it’s not always
by watching key indicators on systems. This goes to the general about malware either: late 2013 saw large scale attacks
theme of improving detection and response rather than solely against home routers, which had their DNS server settings
focusing on prevention. subsequently reconfigured to point at rogue DNS servers.
These were then used to perform Man-in-the-Middle
Leverage threat feeds attacks through a series of proxies, subverting SSL and
two-factor authentication mechanisms by using social
Given the high incidence of C2 communications, using feeds of
engineering methods similar to those described above.
threat data that identify iP addresses and domain names used to
control botnets, then matching this data against firewall or proxy
logs can help accelerate detection and thus containment. We
generally don’t recommend using these lists for outright blocking
due to possible operational issues. But malware researchers do
a fine job of implementing sinkholes and reverse-engineering
malware quickly to identify infrastructure used by the bad guys.
ERAWEMiRC
34 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
PAYMENT CARD SKIMMERS
AT A GLANCE
Description All incidents in which a skimming device was physically implanted (tampering) on an asset that
reads magnetic stripe data from a payment card (e.g., ATMs, gas pumps, POS terminals, etc.).
Top industries
Finance, Retail
Frequency
130 total incidents17
130 with confirmed data disclosure
Key findings There’s not a ton of variation in this pattern at the VERiS level: criminal groups install skimmers
on ATMs (most common) and other card swipe devices. On a more qualitative level, the skimmers
are getting more realistic in appearance and more efficient at exporting data through the use of
Bluetooth, cellular transmission, etc.
Figure 54.
For a wide array of criminals ranging from highly organized crime
Assets affected within Card Skimmers (n=537)
rings to garden variety ne’er-do-wells who are turning out no
good just like their mama warned them they would, skimming
ATM 87%
continues to flourish as a relatively easy way to “get rich quick.” (terminal)
Gas terminal While most incidents are linked to Eastern European actors, 9%
(terminal)
nearly all victims of payment card skimmers in this report are Access reader 2%
U.S. organizations (the U.S. Secret Service and public disclosures (network)
being the primary sources for this data). While some don’t think PED pad 2%
(terminal)
we should include this type of attack in the DBiR, we can’t justify POS terminal 2%
excluding a tried-and-true method used by criminals to steal (user dev)
Backup 1%
payment card information. (server)
Database 1%
Figure 53. (server)
Origin of external actors within Card Skimmers (n=40) Mail 1%
(server)
Mainframe 1%
Bulgaria 38% (server)
Proxy 1%
Armenia 18% (server)
in 2013, most skimming occurred on ATMs (87%) and gas pumps
Romania 18%
(9%) due to the relative ease with which they can be approached
Brazil 8% and tampered with. Gas pump skimmers are often installed by
a small group of people acting in concert. One scenario involves
United States 8%
one or more conspirators going into the station to make a
Bosnia and
2%
Herzegovina purchase and distract the cashier’s attention, while a partner in
Cuba 2% crime plants the device inside the machine using a universal key.
Iran, Islamic
2% ATM skimmers, on the other hand, are installed on the outside
Republic of
of the machine. While some ATM skimming devices are clunky
Mexico 2%
homemade affairs that might afford an opportunity for
Nigeria 2% observant customers to spot them, the design of many skimmers
(both those created by the criminal and those purchased “off the
shelf”) can be so realistic in appearance that they are virtually
invisible to the end user. in most cases they can be snapped in
place in a matter of seconds and can be produced in sufficient
quantities to make the attacks scalable and highly organized.
This, however, has been the norm for some time and warrants
only a cursory mention in this report. What has changed over
time, however, are the methods by which the data is retrieved by
the criminals.
SKiMMERS
PAYMENT
CARD
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 35

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
in the past it was necessary for the criminal to return to the
scene and physically remove the device in order to collect the EVOLUTION OF SKIMMING
stolen data. While we continue to see this, it’s normally indicative Like any technology, the tendency is to develop from bulky
of the less organized and more small time crooks out to “make and slow toward streamlined and efficient. Skimming
some sweet moolah with Uncle Rico.” They’re often apprehended devices are no different. Many people still think of the
when retrieving the skimmed card data. in keeping with what traditional skimmer as the classic wedge – the small hand-
we find with network-based attacks, the successful criminal is held skimmer typically used by waitstaff to illicitly obtain
the one who can maintain a safe distance between themselves mag stripe data while they had the card away from the
and the target. Therefore, the more highly skilled criminals now customer. Because they were so easy to use, they became
collect data via Bluetooth or SiM cards with remote caching and the stock-in-trade for most criminals for a long time.
tampering alerts. Some devices actually send an SMS alert to the
On the flip side, it was often relatively easy for the good
criminal each time the ATM is used.
guys to pinpoint the culprit after the fraud had transpired.
Figure 55. Common Point of Purchase (CPP) algorithms could be used
Discovery methods within Card Skimmers (n=42) to determine the restaurant responsible for the fraudulent
charges. When law enforcement arrived at the restaurant
Total External 76% they could obtain access to the receipts, and with relative
ease determine that the same waiter/waitress served all
Total Internal 24%
the victims. The individual would then be interviewed and…
Ext - fraud detection 26% well, you know the rest.
Ext - law enforcement 21% Fast-forward to the year 2000, when the first gas pump
skimmer was found at a gas station in California. The
Ext - customer 17%
skimmer was placed inside the pump, and (since it only
Int - reported by user 17% captured track information) the criminals set up a wireless
video camera 300 yards away in a weatherproof case. in
Ext - unrelated party 12%
this particular instance, the camera was discovered and
Int - fraud detection 7% unplugged by an investigator. Within minutes, the bad guys
showed up at the gas station to see what went wrong, and
With subterfuge and fraud being the objectives behind skimming,
were promptly taken into custody.
it’s not surprising that it’s most commonly detected by a third
party. Most of the time that third party is a payment card Eventually the risk of discovery during retrieval became too
company or a customer who has noticed fraudulent activity. great, so more criminals started manufacturing skimmers
Other times it’s a phone call from a law enforcement agency after and selling them online. This new wave of devices was
they’ve arrested a gang with a trunk full of skimming devices Bluetooth equipped, which allowed someone to download
and white plastic cards. Hanging close to that pack of external the track and PiN data from the safety of the parking lot.
discovery methods are internal users who spot tampering and
it’s now possible to buy online skimming devices with
report it to management. Way to go, folks. As skimmers become
built-in SiM cards that allow for remote configuration,
more difficult to detect visually, however, we can’t help but
remote uploading of data, and tampering alerts that, if
wonder if this latter scenario will become increasingly rare.
triggered, will cache the data and send it out immediately,
greatly reducing risk.
DRAC
TNEMYAP
SREMMiKS
36 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
RECOMMENDED CONTROLS
Though some might argue, we find no obvious mistake or
oversight on the part of organizations that allows skimming to
succeed when it otherwise wouldn’t. But there are some things
that can be done to make it harder for the criminal and shorten
the window of exposure.
FOR BUSINESSES
Design (or buy) tamper-resistant
terminals
As the merchant, this probably isn’t something you can do
yourself, but be aware that certain designs are more susceptible
to skimming devices than others. Many modern ATMs are
designed with this in mind; choose those if possible.
Use tamper-evident controls
Do things that make it obvious (or send an alert) when tampering
occurs. This may be as simple as a sticker over the door of a
gas pump or more sophisticated tactics like visual anomaly
monitoring on ATMs.
Watch for tampering
Regularly check terminals for signs of unauthorized tampering.
Also train employees to spot skimmers and recognize suspicious
behavior from individuals trying to install them. if a criminal is
able to place a skimmer on one of your devices, these regular
inspections will help curb the damage.
FOR CONSUMERS
Protect the PIN
When entering your PiN, cover your hand to block tiny cameras
that may be recording it. You wouldn’t want a ne’er-do-well
getting ahold of your PiN now, would you?
Trust your gut
if something looks out of the ordinary at your ATM or gas pump,
something fishy may be afoot. While criminals are increasingly
sly at designing difficult-to-detect skimmers, you still might be
able to notice something amiss, especially if the terminal looks
different than others around it. if one of these things is not like
the others, don’t swipe your card!
See something, say something
if something seems out of place to you at a payment terminal,
don’t keep it to yourself. Be sure to tell the merchant or bank
that you may have found a skimmer. Not only will you be helping
them, you’ll also be helping your fellow consumers.
SKiMMERS
PAYMENT
CARD
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 37

CYBER-ESPIONAGE
 ELAS-FO-TNiOP
SNOiSURTNi
AT A GLANCE
Description incidents in this pattern include unauthorized network or system access linked to state-affiliated
 PPA BEW SKCATTA actors and/or exhibiting the motive of espionage.
Top industries
Professional, Transportation, Manufacturing, Mining, Public18
Frequency
511 total incidents
ESUSiM EGELiViRP
306 with confirmed data disclosure
 DNA REDiSNi
Key findings Most surprising to us is the consistent, significant growth of incidents in the dataset. We knew
it was pervasive, but it’s a little disconcerting when it triples last year’s already much-increased
number. Espionage exhibits a wider variety of threat actions than any other pattern. The most
evident changes from our last report include the rise of strategic web compromises and the
 TFEHT LACiSYHP broader geographic regions represented by both victims and actors.
SSOL DNA
Figure 56.
Comprehensive information about “cyber”19 espionage is really
Number of incidents by victim industry and size within
hard to come by. Organizations typically aren’t required to
Cyber-espionage
 SUOENALLECSiM
|        | publicly disclose breaches of internal information and trade      |     |     |     |
| ------ | ----------------------------------------------------------------- | --- | --- | --- |
| SRORRE | secrets, as they are with regulated consumer data. Additionally,  |     |     |     |
there’s no fraud algorithm to alert victims about illicit use of  Industry Total Small Large Unknown
such data, leaving many cases of espionage undiscovered. Most  Administrative [56] 2 1 1 0
of what we know publicly about this genre of threat comes
|     |     | Construction [23] | 1 0 | 0 1 |
| --- | --- | ----------------- | --- | --- |
from incident responders, intelligence analysts, and malware
|     |     | Education [61] | 2 1 | 1 0 |
| --- | --- | -------------- | --- | --- |
researchers who compile and share their knowledge with the
ERAWEMiRC
community. Thus, we’re excited to have quite a few contributors  Finance [52] 3 0 2 1
from these circles, whose information has more than tripled the  Healthcare [62] 2 1 0 1
number of espionage incidents in this year’s dataset, to 511.
|     |     | information [51] | 11 2 | 2 7 |
| --- | --- | ---------------- | ---- | --- |
Before someone concludes we’re asserting a vast increase in  Management [55] 2 1 1 0
espionage in 2013, we’re quite sure countless organizations
|  DRAC TNEMYAP |                                                              | Manufacturing [31,32,33] | 81 5 | 17 59 |
| ------------- | ------------------------------------------------------------ | ------------------------ | ---- | ----- |
| SREMMiKS      | have been consistently targeted for several years. instead,  |                          |      |       |
|               |                                                              | Mining [21]              | 5 0  | 2 3   |
we attribute this increase primarily to our ever-expanding set
of contributors conducting research in this area, along with  Professional [54] 114 11 5 98
more community information sharing that improves discovery  Public [92] 133 20 19 94
capabilities. Like a streetlight illuminating cars parked along
|     |     | Real Estate [53] | 1 1 | 0 0 |
| --- | --- | ---------------- | --- | --- |
the street, more contributors allow us to see more cars.
|                     |                                                             | Retail [44,45] | 1 0 | 1 0 |
| ------------------- | ----------------------------------------------------------- | -------------- | --- | --- |
| EGANOiPSE EGANOiPSE | Unfortunately, we can also see that those cars have broken  |                |     |     |
 -REBYC  -REBYC
|     | windows and stolen stereos. | Transportation [48,49] | 5 1    | 3 1    |
| --- | --------------------------- | ---------------------- | ------ | ------ |
|     |                             | Utilities [22]         | 8 0    | 1 7    |
|     |                             | Other [81]             | 5 5    | 0 0    |
|     |                             | Unknown                | 135 0  | 3 132  |
|     |                             | Total                  | 511 49 | 58 404 |
SKCATTA
 SOD For more information on the NAiCS codes [shown above] visit:
https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012
  GNiHTYREVE
ESLE
| 38  |     |     | VERIZON ENTERPRISE SOLUTIONS |     |
| --- | --- | --- | ---------------------------- | --- |

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
To set the tone, we need to understand the victims represented Attribution is also probabilistic in nature. Be wary of threat
within the data. We don’t claim to cover all espionage activity in intelligence vendors claiming to be 100% sure an attack is X
2013 — quite far from it, actually. As is evident in Figure 57, the actor group from Y country with Z motives; they are “likely”
sample is still largely (over half) U.S. based, but not as exclusively incorrect. There are many methods for determining attribution
as in previous years. We expect this to continue as more global — sometimes it’s following the breadcrumbs left by the actors.
organizations join the cause. We can’t help but wonder why we Other times it’s ruling out the alternatives using something like
have no examples of italian victims of espionage in our dataset. analysis of competing hypothesis.20 None of these methods
Our best hypothesis is that sophisticated actors remember the are perfect. it’s important to carefully evaluate information
classic blunder of “go[ing] in against a Sicilian when death is on to make sure one isn’t suffering from some type of cognitive
the line” when selecting targets (the most famous blunder, of bias.21 it would be more helpful if probabilistic language like
course, is getting involved in a land war in Asia). Sherman Kent’s “Words of Estimative Probabilities”22 was used
when describing attribution to particular countries, regions, and
Figure 57.
threat actors. With that in mind, the following would fall between
Victim country within Cyber-espionage (n=470)
“Probable” and “Almost Certain.”
United States 54% Figure 58.
South Korea 6% Variety of external actors within Cyber-espionage (n=437)
Japan 4% State-affiliated 87%
Russian Federation 3% Organized crime 11%
Colombia 2% Competitor 1%
Ukraine 2% Former employee 1%
Vietnam 1% Unknown <1%
Belarus 1%
As expected, most incidents in this category are attributed
Kazakhstan 1%
to state-affiliated actors. But the data also reminds us that
Philippines 1% organized criminal groups, competitors, and current23 and
former employees join in the game too. We also see that the
in addition to geographic broadening, we see a wide distribution longer game of espionage is not always the sole motive; it often
of both sizes and types of victim organizations. Unfortunately, exhibits a nearer-term, more direct financial element as well.
victim size is often not tracked, so there are a lot of unknowns An example would be a mercenary-style theft of source code or
here. insofar as we can determine from the data before us, digital certificates contracted by a rival organization or other
however, size doesn’t seem to be a significant targeting factor. interested party.
industry, on the other hand, does: the Public, Professional, and
Manufacturing sectors are more targeted by espionage than Figure 59.
the rest of the field (which still runs a fairly wide gamut). There Region of external actors within Cyber-espionage (n=230)
is little doubt that figures for the Public sector, which spans
embassies, economic programs, military, and other support Eastern Asia 49%
organizations, are boosted by our government contributors.
Unattributed 25%
There is also little doubt that they are a prime target for
espionage. Victims within the Professional, Scientific, and Eastern Europe 21%
Technical Services category typically deal with custom computer Western Asia 4%
programming services, research and development, engineering
Northern America <1%
and design, and legal practices. Many of these organizations
are targeted because of the contracts and relationships they Europe <1%
have with other organizations. For some, they can serve as
Southern Asia <1%
both a valuable aggregation point for victim data and a trusted
exfiltration point across several target organizations. Lastly, and
not unexpected, Manufacturing industries are also targeted for
their intellectual property, technology, and business processes.
ESPiONAGE
CYBER-
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 39

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
With respect to actor origin, the percentage of incidents it’s interesting that, while the array of tools is diverse, the basic
attributed to East Asia is much less predominant in this year’s methods of gaining access to a victim’s environment are not. The
dataset. Two countries in particular, the People’s Republic of most prolific is the old faithful: spear phishing. We (and others)
China and the Democratic People’s Republic of Korea, represent have covered this ad nauseam in prior reports, but for both of
that region. This underscores the point we made in our last report you who have somehow missed it, here goes: A well-crafted and
– that, despite our China-exclusive results, China definitely was personally/professionally-relevant email is sent to a targeted
not the only country conducting espionage. user(s), prompting them to open an attachment or click a link
within the message. inevitably, they take the bait, at which
The 2013 dataset shows much more activity attributed to
point malware installs on the system, a backdoor or command
Eastern European actors, Russian-speaking ones in particular.
channel opens, and the attacker begins a chain of actions moving
As before, we don’t propose these are the only active regions/
toward their objective. The proportion of espionage incidents
countries engaged in espionage. More comprehensive research
incorporating phishing is lower than our last report (it was 95%),
into different actor groups is continually driving better detection
but not because of a drop in actual frequency. This is primarily
and attribution, and we hope future versions of this report will
due to a big increase in the use of strategic web compromises
show the fruits of those efforts. At a high level, there doesn’t
(SWCs) as a method of gaining initial access.
seem to be much difference in the industries targeted by East
Asian and Eastern European groups. Chinese actors appeared to Figure 61.
target a greater breadth of industries, but that’s because there Vector for malware actions within Cyber-espionage (n=329)
were more campaigns attributed to them.
Email attachment 78%
One aspect of this pattern that sets it apart from others is the
wide variety of threat actions. Many of the other patterns have Web drive-by 20%
simpler stories with relatively few VERiS actions. Espionage
Direct install 4%
breaks that mold in a big way, though the specific actions
Downloaded by
involved won’t be a surprise to many readers. State-affiliated malware 3%
groups often deploy a wide range of tools (or tools that have
Email link 2%
wide range of capabilities), which is evident in Figure 60.
Email autoexecute <1%
Figure 60.
Network propagation <1%
Top threat action varieties within Cyber-espionage (n=426)
Remote injection <1%
Use of backdoor or C2 [hac] 70% Unknown <1%
C2 [mal] 68%
Phishing [soc] 67% instead of email bait, SWCs set a trap within (mostly) legitimate
Backdoor [mal] 65% websites likely to be visited by the target demographic. When
they visit the page, the trap is sprung, the system infected, and
Downloader [mal] 60%
the rest is the same as described above. Even if detected quickly,
Capture stored data [mal] 57% SWCs can provide a very high reward for attackers. Furthermore,
Export data [mal] 43% the industry has observed some maturation of the SWC
technique, which assists the actors in focusing their targets and
Spyware/keylogger [mal] 38%
avoiding detection (see sidebar on next page for more on SWCs).
Exploit vuln [mal] 37%
Scan network [mal] 37%
Use of stolen creds [hac] 30% CAMPAIGN RESEARCH PUBLISHED IN 2013
Disable controls [mal] 28% The DBiR focuses on overall trends and stats related
to espionage campaigns. Several of our contributors
Rootkit [mal] 24%
have published in-depth research on specific actors and
Brute force [mal] 24% campaigns, some examples are listed below:
Brute force [hac] 24% • Deputy Dog (FireEye), August-September 2013
• Ephemeral Hydra (FireEye), November 2013
Password dumper [mal] 19%
• MiniDuke (Kaspersky), February 2013
Packet sniffer [mal] 16%
• Red October (Kaspersky), May 2007-January 2013
Ram scraper [mal] 14% • Sunshop (FireEye), September 2011-October 2013 (But
likely ongoing)
Other [mal] 14%
• Troy (McAfee, part of intel Security), January–March
Client-side attack [mal] 13% 2013
• Multi-campaign (U.S. Defense Security Service),
“Targeting U.S. Technologies”
-REBYC
EGANOiPSE
40 VERIZON ENTERPRISE SOLUTIONS

Figure 62. Figure 64.
POiNT-OF-SALE
 Variety of at-risk data within Cyber-espionage (n=355) Discovery timeline within Cyber-espionage (n=101) iNTRUSiONS
Seconds 0%
| Internal |     | 85%         |     |     |
| -------- | --- | ----------- | --- | --- |
| Secrets  |     | 83% Minutes | 0%  |     |
Hours 9%
| System |     | 80% |     |     |
| ------ | --- | --- | --- | --- |
Days 8%
Credentials 39%
ATTACKS WEB APP
Weeks 16%
Classified 31%
Months 62%
| Unknown | 19% |     |     |     |
| ------- | --- | --- | --- | --- |
Years 5%
| Personal | 2%  |     |     |     |
| -------- | --- | --- | --- | --- |
PRiViLEGE MiSUSE
Payment 1% The most common method of discovery is ad hoc notification  iNSiDER AND
Copyrighted <1% from threat intelligence and research organizations that
observe, for instance, the victim communicating with C2
| Other | <1% |     |     |     |
| ----- | --- | --- | --- | --- |
infrastructure of a known threat group. While this isn’t good news
per se, it does suggest intelligence operations are an important
Once the phishing email or SWC has done its work, and an  tool for combating espionage.
PHYSiCAL THEFT
internal system is infected, the name of the game is moving
AND LOSS
determinedly through the network to obtain the prize. This may
happen quickly, but it also may last for years. Common methods
involving loading backdoors on systems to maintain access,
dropping spyware/keyloggers and password dumpers to steal  TOOLS OF THE TRADE: STRATEGIC WEBSITE COMPROMISE
user credentials, and then using those credentials to elevate
|     |     | Strategic website compromises (SWCs) have proven to be  |     | MiSCELLANEOUS  |
| --- | --- | ------------------------------------------------------- | --- | -------------- |
privileges and expand control. an effective tactic of state-affiliated threats to infiltrate
ERRORS
the networks of target organizations. in 2012, SWCs made
Figure 63.
their debut with the “VOHO Affair”24 and continued in 2013
Top 10 discovery methods within Cyber-espionage (n=302)
with attacks focused against the Public, Manufacturing,
| Total External |     | 85% Professional, and Technical sectors.  |     |     |
| -------------- | --- | ----------------------------------------- | --- | --- |
SWCs leverage websites that are of critical or
| Total Internal | 15% |     |     | CRiMEWARE |
| -------------- | --- | --- | --- | --------- |
complementary value to an industry’s line of business to
Ext - unrelated party 67% distribute malware traditionally contained in spear phishing
Ext - law enforcement 16% emails. Visitors are hit with a drive-by download, granting
attackers access/ownership of the system. State-affiliated
| Int - antivirus | 8%  |     |     |     |
| --------------- | --- | --- | --- | --- |
SWCs in 2013 exhibited three new browser-based zero-day
PAYMENT CARD
Int - NIDS 2% vulnerabilities (constituting over 75% of publicly disclosed
SKiMMERS
SWCs), which upped the rate of compromise per event.
| Int - reported by user | 2%  |     |     |     |
| ---------------------- | --- | --- | --- | --- |
So, why has the use of SWCs in espionage campaigns
| Int - log review | 1%  |     |     |     |
| ---------------- | --- | --- | --- | --- |
increased? Well, there’s no doubt that attackers have
| Int - unknown | 1%  |     |     |     |
| ------------- | --- | --- | --- | --- |
realized this tactic scales well and provides reasonable
assurances of ambiguity. By opting out of direct attacks
| Other          | 1%  |                                                         |     |                     |
| -------------- | --- | ------------------------------------------------------- | --- | ------------------- |
|                |     | like phishing, attackers effectively remove themselves  |     | ESPiONAGE ESPiONAGE |
| Ext - customer | 1%  |                                                         |     | CYBER-  CYBER-      |
from the tribulations of poor grammar, scanners, and astute
<1% users. And by leveraging zero-day exploits, they achieve
Ext - audit
higher success rate that no longer rely on carefully coerced
actions.
Examining discovery timelines and methods for espionage
incidents reveals ample room for improvement. While this
in 2014, we’d like to predict SWCs will fade, but that
information is often not known or provided (for various reasons,
|     |     | seems unlikely. While there are downsides to SWCs for the  |     | ATTACKS |
| --- | --- | ---------------------------------------------------------- | --- | ------- |
DOS
including the visibility and focus of our contributors), there’s  attackers (high visibility and high cost to weaponize and
enough to discern the general state of affairs. it typically takes
burn a zero day), the benefits of a low-cost way to support
victims months or more to learn they’ve been breached and it’s  long-term operations generally outweigh the risks.
usually an outside party notifying them.
EVERYTHiNG
ELSE
| VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT |     |     |     | 41  |
| ---------------------------------------------- | --- | --- | --- | --- |

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
RECOMMENDED CONTROLS
isolating the root cause of an espionage-related breach is a bit of Beyond the basics, there are some specific practices that
a snipe hunt. Sure, victims make mistakes (minor and otherwise) organizations concerned with state-affiliated and other
that are exploited in the process, but the real root issue is a determined adversaries should consider. These roughly follow
determined, skillful, patient, and well-resourced adversary who critical points in the path of attack, where victims have the best
will keep poking until he finds (or makes) a hole. With that in chance to recognize and respond.
mind, let’s take a closer look at the holes and other thin spots
these adversaries often take advantage of. Break the delivery-exploitation-
installation25 chain First, we’ll start with a few blocking and tackling fundamentals
that you really ought to be doing regardless of whether or not
you’re worried about espionage. if you don’t do these, all those Users will be phished, and they will eventually click; we’ve got
super-advanced cybertastic APT kryptonite solutions may well the data to prove it. Focus on implementing a solution that more
be moot. completely defends against phishing, such as not relying solely
on spam detection and blocklists, but also doing header analysis,
Patch ALL THE THINGS! pattern matching based on past detected samples, and sandbox
analysis of attachments or links included.
Exploiting browser, OS, and other third-party software (e.g., For more mature organizations, check out the growing collection
Flash and Java) vulnerabilities to infect end-user systems is a of Data Execution Prevention (DEP) and Endpoint Threat
common initial step for attackers. Keeping everything up to date Detection and Response (ETDR) solutions. We don’t promote
will make that step a lot harder to take. specific products in this report, but you’ll find some good
options in this space by starting your search with some of our
Use and update anti-virus (AV)
contributors.
While many proclaim AV is dead, not having it is akin to living Spot C2 and data exfiltration
without an immune system. it might not protect you from the
dreaded zero day, but let’s be honest — many espionage victims Collect and/or buy threat indicator feeds. in and of themselves,
still fall to one-zero-zero days (or higher). An up to date AV (in-line they aren’t intelligence, but they’re certainly useful within
and on the endpoint) can go a long way to detect anomalies in intelligence and monitoring operations.
applications and find pesky shells and other malware.
Monitor and filter outbound traffic for suspicious connections
Train users and potential exfiltration of data to remote hosts. in order to
recognize “abnormal,” you’ll need to establish a good baseline of
Some will consider this a lost cause, but we counter with a what “normal” looks like. Those indicators you collected/bought
reminder that, over the years we’ve done this research, users will come in handy here.
have discovered more breaches than any other internal process
Monitor your DNS connection, among the single best sources
or technology. it’s not all about prevention; arm them with the
of data within your organization. Compare these to your threat
knowledge and skills they need to recognize and report potential intelligence, and mine this data often.
incidents quickly.
Stop lateral movement inside
Segment your network
the network
Good network and role segmentation will do wonders for After gaining access, attackers will begin compromising systems
containing an incident, especially where actors intend to leverage across your network. ETDR, mentioned above, can help here too.
access to one desktop as a stepping-stone to the entire network.
Two-factor authentication will help contain the widespread and
unchallenged re-use of user accounts.
Keep good logs
We mentioned network segmentation in the basics, but since
Log system, network, and application activity. This will not only
doing it well is challenging, we’ll mention it here again. Don’t make
lay a necessary foundation for incident response, but many
it a straight shot from patient zero to a full-fledged plague.
proactive countermeasures will benefit from it as well.
Watch for user behavior anomalies stemming from compromised
accounts.
-REBYC
EGANOiPSE
42 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
DENIAL OF SERVICE ATTACKS
Hold on a second? DoS attacks? in a data breach report? when you visit during the holidays. Obviously, such systems,
reserved largely for normal home internet users, have relatively
Knowing that these attacks are top of mind for many
small bandwidth from DSL or cable modems. The attackers then,
organizations — especially in light of late 2012/2013 events
harnessing their botnet of DoS drones, could send commands to
— we decided to expand the scope of the DBiR to include them.
direct attacks at a specific target. Flash forward to September
We collected quite a bit of data on the topic from multiple
2012 and you see a different scenario altogether, along with a
sources, including teams at Akamai and Verizon that spent a lot
different method for building a better botnet. in this situation,
of time in the trenches fighting DDoS attacks in 2013. We could
attackers scanned for and exploited vulnerable websites and
have renamed it Verizon’s Security incident Report (VSiR), but
CMSs. Then they placed specific DOS attacks scripts onto these
Microsoft has already laid claim to the “SiR”26 title.
sites. The primary script used by these attackers is a customized
A new trend started developing in September of 2012. in the version of a Russian kit known as Brobot or itsoknoproblembro.
past, DOS attacks were primarily generated from compromised So what’s different? Well, for starters these botnet drones aren’t
home computers or by willing participants. Think “your parents’ sitting on the internet pipes of home broadband users.
desktop” system – you know, the one you’re always cleaning up
.3 .2
.1 .3
.2 .1
.3 .2
.1 104 106 108 1010 104 106 108
ytisneD
ytisneD
ytisneD
AT A GLANCE
Description Any attack intended to compromise the availability of networks and systems. includes both
network and application layer attacks.
Top industries
Finance, Retail, Professional, information, Public
Frequency
1,187 total incidents
0 with confirmed data disclosure
Key findings The headliner for DDoS in our 2013 dataset was the QCF campaign against the financial industry,
which compromised vulnerable CMSs to create high-bandwidth attacks from hosting centers.
DNS reflection attacks also became “big” but sightings of the DoS equivalent of Bigfoot (DDoS
distractors covering up other nefarious activities) remain rare.
Figure 65.
Denial of Service attack bandwidth and packet count levels 2011-2013
2011 mean = 4.7Gbps 2011
bits per second packets per second
mean = 0.4Mpps
2012 mean = 7.0Gbps 2012
bits per second packets per second
mean = 2.6Mpps
2013 mean = 10.0Gbps 2013
bits per second packets per second
mean = 7.8Mpps
ATTACKS
DOS
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 43

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
They’re in hosted/cloud/private cloud/etc. data centers with Speaking of DoS attacks that don’t require a vast botnet to be
high bandwidth pipes. The servers are also optimized for heavy devastating, we’ve observed another trend stealing the limelight
traffic. Put these two together and you have the makings of what recently: DNS reflection attacks. Not as clumsy or random as
gamers might call a DoS BFG. Or, if music is your game — “these a botnet; these are an elegant weapon for a more civilized age.
go to 11.” High packet, high bandwidth attacks. in some of the Remember the biggest DoS attack in history?27 if not, allow us to
Brobot attacks in the last year we saw upwards of 97 Gbps/100 refresh your memory. in March 2013, the anti-spam organization
Mpps attacks. These were some of the largest attacks we (and Spamhaus was the target of a massive and sustained DoS target
likely anyone else) have ever seen. that some security vendors claim spiked at nearly 300 Gbps
of traffic. The key word here is spiked (and we can’t emphasize
So who exactly was behind this new wave of DoS attacks? The
that enough); the average amount of traffic hitting Spamhaus
simple answer is the izz ad-Din al-Qassam Cyber Fighters (or
during the attack ranged anywhere from 85-120 Gbps, which
QCF for short). The group first popped up in September 2012
still represents a sizable bombardment. The method behind
with the stated goal of using DoS attacks to wreak havoc on U.S.
generating an attack this large is DNS reflection.
financial institutions – part of a campaign they dubbed Operation
Ababil. And they did just that; for several weeks near the end So how does it work? Typically, an attacker sends a bunch of
of 2012 and well into the first half of 2013, the QCF launched DNS queries to open DNS resolvers. The attacker forges the
wave after wave of DoS attacks against U.S. banks using their source address on his requests to make it look as though they
powerful Brobot ion cannons (think Hoth). originated from his desired target. The open resolvers then send
their typically larger responses to the targeted address, which
All of this begs the question: Why was the QCF so determined
is quickly swamped with seemingly legitimate traffic. Hence,
to wage a campaign against prominent U.S. financials? if you
“reflection.” Much like the low and slow attacks described above,
believe the propaganda the group regularly posted to Pastebin
DNS reflection doesn’t require significant computing resources
during their attacks, then the answer to the question of what
on the part of the attacker to produce devastating results.
motivated them is simple: ideology. Like a broken record, the
QCF repeatedly stated they would attack U.S. banks until all
forms of a highly controversial and disparaging video named
“innocence of Muslims” was removed from YouTube. They even
DOS’ING THE MATH
created a mathematical formula to convert the number of “likes”
the video had to how long the campaign would continue. if there’s one thing we’ve learned from the attack on
Spamhaus and others like it, it’s the importance of
While this was the show the QCF put on for public consumption,
understanding the numbers behind DoS attacks. Let’s look
there were theories circulating in the security community that
at an example. Say there was a 200 Gbps attack at 25 Mpps,
Operation Ababil was nothing more than a front for state- 200 Gbps = 2.14 x 1011 or so bps, divide that by 25,000,000
affiliated attackers based in iran. Those theories created a
and that is about 8,500 bits per packet or just over 1k bytes
VERiS dilemma about how to classify the QCF’s actor variety.
per packet on average. This indicates many of the packets
Are they truly hacktivists looking to get YouTube videos taken
are pushing towards the maximum packet size most iSPs
down or are they state-affiliated threat actors probing for
will route. We’ve seen attacks with a higher packet rate, but
weaknesses in the U.S. financial infrastructure at the bidding of
never anything close to that in bandwidth. Both attackers
the iranian government? Unfortunately, the multilayer command
and defenders tend to sensationalize attacks like this. Both
and control infrastructure utilized in botnet creation makes
have motives for inflating them. Attackers want to call
it incredibly difficult to say with certainty from open sources
attention to their attacks and defenders will say, “Look,
that iran is indeed the wizard behind the green curtain, so we
it was so large there was no way we could keep that site
ultimately decided to go with the publicly stated purpose of the
up and running.” Or if it’s a vendor, “Look how powerful our
actors and chalk it up to hacktivism.
service is. We can stop all the attacks!”
While it’s true that exactly what motivated the QCF isn’t entirely That being said, data compiled by our DoS defense team
certain, the tactics used to carry out the group’s attacks are well
shows an increase in the average size of attacks over the
known. Not only did the group use more traditional attacks such
past three years — as shown in figure 65. in 2011, the
as UDP and SYN floods to clog up a target website’s bandwidth
average attack involved 4.7 Gbps of bandwidth with a
and tie up server resources, it also carried out application-layer
411 Kpps packet rate. Move forward to 2012 and those
DoS attacks. in these low and slow attacks the QCF would send
averages jumped to 6.7 Gbps at 2.5 Mpps. it shouldn’t
multiple HTTPS GET requests for PDF files on the target site.
surprise you to learn that in 2013 the average DoS attack
These types of attacks are especially frustrating: they don’t clocked in at 10.1 Gbps at close to 8.1 Mpps. While the QCF
require significant resources, they can be difficult to defend
and its powerful arsenal likely shoulder some of the blame
against, and they can be incredibly effective. The use of HTTPS is
for this year-over-year increase, the increasing popularity
particularly problematic for mitigation because the packets are
of reflection attacks and the power they generate are the
encrypted, which makes it difficult for defenders to determine
primary culprits.
junk traffic from legitimate traffic.
SOD
SKCATTA
44 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
Aside from the rise in DNS reflection attacks and converting RECOMMENDED CONTROLS
webservers into high-powered DoS bots, not much has changed
Now that we’ve talked about the problem at length it’s a good
over the past few years. Sure, there are always new DoS toolkits
time to discuss what can be done to lessen or even prevent DoS
making their way into the underground and new waves of attacks
attacks against your organization.
taking place, but the general principles remain the same, as do
the targets. We saw many attacks directed at the financial, retail,
Let’s start with the basics
professional services, and public sectors. What better way to
inflict pain on a bank or retailer than to go after its website –
Servers/services should always be turned off when not in use,
something critical to customer service? And though carrying out
patched when in use, and available only to the people who need
a DoS attack isn’t as difficult as it seems, results may vary. For
them, especially in the case of reflection attacks.
the financially challenged attacker it’s possible to download open
source tools such as Low Orbit ion Cannon (LOiC), but he’ll need A
Isolate key assets
LOT of friends to do the same if the attack has a chance of being
successful. On the other hand, if he’s got some cash to burn, the
Segregate key iP/servers from non-essential iP space. Any iP
attacker can rent out a DirtJumper or Athena botnet and pummel
space not in active use for key servers should be announced
the target of his choice for less than $10 an hour. The more
out of a separate circuit, perhaps even purchase a small backup
enterprising (and development-minded) individual might even
circuit and announce iP space. That way if it’s attacked, the
go so far as to write his or her own DoS script and herd a botnet
attack won’t compromise your primary facilities/servers.
together. And trust us, these three scenarios play out every day
in the cybercriminal underground.
Get comfortable
We’ve heard many clients and colleagues express concern
about attackers using DoS attacks as a “smokescreen” to Don’t be shy about using your provider’s anti-DDoS service. You
hide fraudulent automated clearing house (ACH) transfers should be able to test it quarterly without charge. Make sure that
and other illicit activity. Although there are scattered reports your key operations teams will react in a timely manner if there
of this happening, hard evidence we’ve managed to collect is an actual attack. Even if your provider offers “auto-mitigation,”
doesn’t indicate the rate or impact justifies the level of angst. this shouldn’t be an install-and-forget kind of service.
We sometimes jokingly refer to this as the “DoS Bigfoot,” not
because we don’t think it’s real, but because we’re intrigued and Have a plan in place
want to capture it on film. Data collection for the 2015 DBiR is
already underway, and we invite any with shaky night vision film What are you going to do? Who will you call if your primary
clips of this thing to set the record straight. anti-DDoS doesn’t work? You know what you’d do if one of your
circuits or servers went down – why should this be any different?
Do the math
Know that most attacks are about the FUD numbers cited by the
news media. They’re above your SSL server capacity, or perhaps
a few times your ingress circuit line rate. But attackers don’t
have infinite resources either – the biggest attack will be just
over what you can manage.
Ask about capacity
Understand that all iSPs will have to, at some point, protect their
general network over your company’s specific traffic. Ask your
anti-DDoS provider about its upstream peering capacity – if
they can’t get the (good and bad) traffic in no matter how much
mitigation capacity they have, your good traffic will be dropped
at the outside edge of their iSP’s network and your call queues
will light up with unhappy customers.
ATTACKS
DOS
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 45

ELAS-FO-TNiOP
PPA
BEW
DNA
REDiSNi
TFEHT
LACiSYHP
SUOENALLECSiM
DRAC
TNEMYAP
-REBYC
SOD
GNiHTYREVE
ERAWEMiRC
SNOiSURTNi
SKCATTA
ESUSiM
EGELiViRP
SSOL
DNA
SRORRE
SREMMiKS
EGANOiPSE
SKCATTA
ESLE
EVERYTHING ELSE
AT A GLANCE
Description This last “pattern” isn’t really a pattern at all. instead, it covers all incidents that don’t fit within
the orderly confines of the other patterns. Given that, one might assume you’d never find a more
wretched hive of scum and villainy than this random assortment of outcasts. But what we actually
find looks nothing like the riffraff of a Mos Eisley cantina; it’s almost entirely dominated by two
related species of incidents.
“Why not make two more patterns, then?” you might well ask. “Then why do you say they’re related species?” you might counter.
Great question; allow us to explain. A little digging into the data uncovers the fact that these
incidents actually represent mass attacks reported to a CSiRT. in
First, let’s describe what we see here among these 7,269
one, thousands of servers in hosting facilities were compromised
incidents. Actors are 99.9% external. Generic “hacking” (variety
and used to host phishing sites. The other involved hundreds of
unknown), phishing, and browser-busting malware lead known
servers hijacked to host malware for drive-by exploits. Nothing
threat actions, with everything else below the 1% line. Three-
else was reported about the method of compromise or the
quarters of all incidents involved compromised web servers; the
phishing/malware campaigns themselves.
rest were unknown.
Figure 66.
Hierarchical clustering of VERIS enumerations for confirmed data disclosures falling outside the main incident patterns
20 10 0
actor.external.variety.Unaffiliated (7)
attribute.confidentiality.data.variety.Personal (7)
asset.assets.variety.P − Finance (5)
attribute.integrity.variety.Fraudulent transaction (5)
attribute.confidentiality.data.variety.Payment (11)
actor.external.motive.Financial (23)
actor.external.variety.Organized crime (9)
action.social.variety.Pretexting (12)
attribute.integrity.variety.Alter behavior (18)
attribute.confidentiality.data.variety.Bank (9)
action.social.vector.Phone (11)
asset.assets.variety.P − Call center (9)
attribute.confidentiality.data.variety.Secrets (12)
asset.assets.variety.S − Database (9)
asset.assets.variety.S − Web application (10)
asset.assets.variety.S − File (7)
attribute.integrity.variety.Software installation (5)
attribute.integrity.variety.Misappropriation (6)
action.hacking.variety.Brute force (5)
action.hacking.variety.Use of stolen creds (18)
attribute.confidentiality.data.variety.Credentials (22)
GNiHTYREVE
ESLE
46 VERIZON ENTERPRISE SOLUTIONS

iNTRUSiONS
ATTACKS
PRiViLEGE
MiSUSE
AND
LOSS
ERRORS
SKiMMERS
ESPiONAGE
ATTACKS
ELSE
CRiMEWARE
POiNT-OF-SALE
WEB
APP
iNSiDER
AND
PHYSiCAL
THEFT
MiSCELLANEOUS
PAYMENT
CARD
CYBER-
DOS
EVERYTHiNG
All in all, not very informative — and therein lies the issue. it this pairing is sometimes seen in conjunction with brute-force
quickly becomes apparent that these incidents aren’t something attacks, unauthorized software (malware) installation, and
utterly different, but rather simply lack sufficient detail to misappropriation (illegitimate use/hijacking) of file servers.
better classify them. That’s not exclusive, mind you, but it’s a pattern recognized by the
algorithm.
A slightly more interesting view is found by narrowing in on the
subset (81 incidents) that involved confirmed data disclosure.28 To the left of that, we see a strongly related cluster linking
We’ll use the Figure 66 dendrogram to go hunting for patterns. phone-based social engineering of call center employees.
We realize that dendrograms aren’t the most inherently intuitive including nearby clusters within that whole middle segment adds
visualizations,29 but their basic premise is pretty straightforward additional context around that: financially motivated, organized
and they serve this purpose well. criminals using pretexting to steal payment information from
bank call centers, and conducting fraudulent transactions.
The words in the dendrogram are VERiS enumerations.
Enumerations are organized into clusters. Clusters are The theft of trade secrets kind of sticks out like the extra digit
connected — directly or indirectly — by branches of varying on a six-fingered man (yes; the one who killed your father and
levels. Multiple enumerations on the same cluster or low-level must prepare to die); probably because the source knew what
branch signify a close and distinguishing relationship (i.e., they was taken, but not how it was taken or who took it.
commonly appear together within incidents). Enumerations and
The leftmost clusters appear to be generic intrusions into web
clusters separated by higher branches signify weak or infrequent
servers and databases to steal personal information.
relationships.
We could go deeper into this rabbit hole, but this at least gives
When applied to Figure 66, this results in a cluster to the far
some sense of what didn’t make the cut for the other patterns.
right encompassing stolen credentials and the use of those
You’re probably dendrogrammed out by now anyway.
credentials to gain unauthorized access. Higher level (weaker/
less frequent) clusters in that same rightmost branch hint that
YOU AND ME GO PHISHING IN THE DARK
Figure 67.
in last year’s report we examined data from ThreatSim and
Success rates of phishing exercises
came to the earth-shattering conclusion that phishing is an
effective way to gain access to an organization. Okay, maybe
Drive-by 18%
that isn’t news, but the revelation that a phishing campaign of
only ten messages has a better-than 90% chance of getting a Form/Data-entry 9%
click was surprising to many of us.
Click attachment 9%
This year we took a look at ThreatSim’s data again and
immediately reconfirmed the findings from last year; that even Figure 68.
a campaign consisting of a small number of email messages
Phishing success rates
has a high probability of success. However, this year we found
that the overall success rate of a phishing message was 100%
slightly lower at 18%. The reason could be more awareness of Overall
phishing, or just natural variation in the samples. 90% (2013) Drive-by
Infections
We also looked at the success rate of different tactics in 5800%% (2014)
phishing. Are users more likely to visit a link than run an
attachment? Are they more likely to click an attachment than 70%
User Action
enter their passwords in a web form? in general, it appears
(2014)
that about 8% of users will click an attachment and about 8% 60%
will fill in a web form. And while most users are skeptical about
50%
clicking an attachment (though not skeptical enough) they
are less fearful of visiting a link in an email. 18% of users will
40%
visit a link in a phishing email. Users unfamiliar with drive-by
malware might think that simply visiting a link won’t result in a
30%
compromise.
20%
10%
0 10 20 30 40
ELSE
EVERYTHiNG
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 47

CONCLUSION AND SUMMARY
RECOMMENDATIONS
it’s fascinating to study what goes wrong. But the real purpose of So for example, in the column for the Public sector, you’ll see CSC
this research is to help you reduce the risk that these bad things 17 stands out as a priority. Sure, someone could have said before,
will happen to you. At the end of the day, we do this work to support “intuitively, data loss prevention should probably be important for
evidence-based risk management. We think the perspective of the Public sector.” But now this report puts some hard data behind
studying clustered incident patterns enables more tailored strategies that. Misuse, theft/loss, and error constitute a strong majority of the
to reduce risk, and toward that end, we did two specific things this attack patterns the public sector faces, and data loss prevention helps
year. First, we mapped industries to attack patterns to help answer address all of them. The other 19 CSCs are great (and we certainly
the question, “For my industry, which threats am i most likely to aren’t saying anyone should ignore them), but this perspective is a
face?” Second, for each pattern we made specific recommendations, strong argument for making sure the industry gives CSC 17 the focus
including priority controls from the Critical Security Controls (CSCs) and resources it deserves; specifically the sub-controls that cover full
based on our collaboration with the Council on Cybersecurity. This disk encryption (17.3) and detecting mis-published information (17.6).
included mapping patterns to controls. View this as evidence that can help answer the question “Based on
where my industry is now (which reflects the controls already in place
To wrap up, let’s connect the dots in one more way. Since we’ve
and the threats they often face), what should we focus on next?”
used the data to map industries to incident patterns and patterns
to controls, we figured we also have a decent foundation to map Granted, one element of this is subjective in that we and the Council’s
industries directly to recommendations for controls. Figure 69 on experts decided which controls would best address each threat
the next page shows which controls we think are key to the threat pattern. But we based those decisions on event chains observed in our
patterns each industry faces. And it weights each control by how data set. And the weighting we did is based firmly on the frequency
often we see the patterns the control addresses in that industry. data we have for patterns and industries. So while small differences
Essentially, we just did a whole bunch of multiplication to save you the in these numbers probably aren’t too meaningful, we do think there’s a
trouble. strong argument for taking a hard look at the controls that come out
on top.
As always, we hope you find this year’s report valuable, and we look
forward to hearing your feedback. May the Force be with you, and
THE COUNCIL ON CYBERSECURITY have fun storming the castle!
The Council on CyberSecurity was established in 2013 as an
independent, expert, not-for-profit organization with a global
scope committed to the security of an open internet. The Council
is committed to the ongoing development, support, and adoption
of the Critical Security Controls; to elevating the competencies Questions? Comments? Brilliant ideas?
of the cybersecurity workforce; and to the development of
We want to hear them. Drop us a line at
policies that lead to measurable improvements in our ability to
dbir@verizon.com, find us on LinkedIn, or tweet @
operate safely, securely and reliably in cyberspace. For additional
VZdbir with the hashtag #dbir.
information, visit the Council’s website.
www.counciloncybersecurity.org
48 VERIZON ENTERPRISE SOLUTIONS

Figure 69.
Critical security controls mapped to incident patterns. Based on recommendations given in this report.
|                              |     |  snoisurtni |          |                  | ssoL/tfehT |        |           |  sremmikS |  eganoipse |          |
| ---------------------------- | --- | ----------- | -------- | ---------------- | ---------- | ------ | --------- | --------- | ---------- | -------- |
|                              |     |             |  ppA beW |                  |  lacisyhP  |        | erawemirC |           |            |  skcattA |
|                              |     |             | skcattA  |  redisni  esusiM |            | srorrE |           |  draC     |  -rebyC    |          |
| Critical Security Controls   |     |  SOP        |          |                  |            | csiM   |           |           |            |  SoD     |
(SANS Institute)
| Software inventory | 2.4  |     |     |     |     |     | ∑   |     | ∑   |     |
| ------------------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                    | 3.1  |     |     |     |     |     | ∑   |     |     |     |
| Standard Configs   | 3.2  |     | ∑   |     |     |     | ∑   |     | ∑   |     |
|                    | 3.8  |     |     |     |     |     | ∑   |     |     |     |
|                    | 5.1  | ∑   |     |     |     |     | ∑   |     | ∑   |     |
| Malware Defenses   | 5.2  | ∑   |     |     |     |     | ∑   |     | ∑   |     |
|                    | 5.6  |     |     |     |     |     | ∑   |     | ∑   |     |
|                    | 6.4  |     | ∑   |     |     |     |     |     |     |     |
| Secure Development | 6.7  |     | ∑   |     |     |     |     |     |     |     |
|                    | 6.11 |     | ∑   |     |     |     |     |     |     |     |
| Backups            | 8.1  |     |     |     | ∑   |     |     |     |     |     |
|                    | 9.3  |     |     |     | ∑   |     |     |     |     |     |
Skilled Staff
|                   | 9.4  |     |     |     |     |     |     |     | ∑   |     |
| ----------------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                   | 11.2 | ∑   |     |     |     |     |     |     |     |     |
| Restricted Access | 11.5 | ∑   |     |     |     |     |     |     |     |     |
|                   | 11.6 | ∑   |     |     |     |     |     |     |     |     |
|                   | 12.1 | ∑   |     | ∑   |     |     |     |     |     |     |
|                   | 12.2 |     |     | ∑   |     |     |     |     |     |     |
| Limited Admin     | 12.3 | ∑   |     |     |     |     |     |     |     |     |
|                   | 12.4 | ∑   |     |     |     |     |     |     |     |     |
|                   | 12.5 | ∑   |     |     |     |     |     |     |     |     |
|                   | 13.1 |     |     |     |     |     | ∑   |     | ∑   |     |
|                   | 13.7 | ∑   | ∑   |     |     |     | ∑   |     | ∑   |     |
Boundary defense
|                      | 13.10 | ∑   |     |     |     |     |     |     |     |     |
| -------------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                      | 13.14 | ∑   |     |     |     |     |     |     |     |     |
| Audit Logging        | 14.5  | ∑   |     | ∑   |     |     |     |     |     |     |
|                      | 16.1  |     |     | ∑   |     |     |     |     |     |     |
| identity Management  | 16.12 |     |     | ∑   |     |     |     |     |     |     |
|                      | 16.13 |     |     | ∑   |     |     |     |     |     |     |
|                      | 17.1  |     |     |     | ∑   |     |     |     |     |     |
| Data Loss Prevention | 17.6  |     |     | ∑   |     | ∑   |     |     |     |     |
|                      | 17.9  |     |     | ∑   |     | ∑   |     |     |     |     |
|                      | 18.1  |     |     |     |     |     |     |     |     | ∑   |
| incident Response    | 18.2  |     |     |     |     |     |     |     |     | ∑   |
|                      | 18.3  |     |     |     |     |     |     |     |     | ∑   |
| Network Segmentation | 19.4  |     |     |     |     |     |     |     | ∑   | ∑   |
To find out more about the SANS institute’s Critical Security Controls, visit: http://www.sans.org/critical-security-controls/
| VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT |     |     |     |     |     |     |     |     |     | 49  |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Figure 70.
Prioritization of critical security controls by industry. Based on frequency of incident patterns within each industry and recommendations
for each pattern given in this report. The shading is relative to each industry.
Critical Security Controls (SANS Institute)
]27[
noitadommoccA
]65[
evitartsinimdA ]32[ noitcurtsnoC ]16[ noitacudE
]17[
tnemniatretnE ]25[
ecnaniF
]26[ erachtlaeH ]15[ noitamrofni ]55[ tnemeganaM
]33,23,13[
gnirutcafunaM ]12[
gniniM
]18[
rehtO
]45[ lanoisseforP ]29[
cilbuP
]35[ etatsE
laeR
]54,44[
liateR
]24[
edarT
]94,84[
noitatropsnarT ]22[
seitilitU
Software inventory 2.4
3.1
Standard Configs 3.2
3.8
5.1
Malware Defenses 5.2
5.6
6.4
Secure Development 6.7
6.11
Backups 8.1
9.3
Skilled Staff
9.4
11.2
Restricted Access 11.5
11.6
12.1
12.2
Limited Admin 12.3
12.4
12.5
13.1
13.7
Boundary defense
13.10
13.14
Audit Logging 14.5
16.1
identity Management 16.12
16.13
17.1
Data Loss Prevention 17.6
17.9
18.1
incident Response 18.2
18.3
Network Segmentation 19.4
For more information on the NAiCS codes [shown above] visit: https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012
To find out more about the SANS institute’s Critical Security Controls, visit: http://www.sans.org/critical-security-controls/
50 VERIZON ENTERPRISE SOLUTIONS

APPENDIX A:
METHODOLOGY
Based on feedback, one of the things readers value most about this 1. VERIZON’S DATA COLLECTION METHODOLOGY
report is the level of rigor and integrity we employ when collecting, The underlying methodology we used is unchanged from previous
analyzing, and presenting data. Knowing our readership cares about years. All results are based on first-hand evidence collected during
such things and consumes this information with a keen eye helps keep paid external forensic investigations and related intelligence
us honest. Detailing our methods is an important part of that honesty. operations we conducted from 2004 through 2013. The 2013
caseload is the primary analytical focus of the report, but the entire
Our overall methodology remains intact and largely unchanged from
range of data is referenced throughout. Once an investigation is
previous years. With 50 organizations contributing data this year,
completed, our analysts use case evidence, reports, and interviews to
there is no single means used to collect and record the data. instead
create a VERiS record of the incident(s). The record is then reviewed
we employed different methods to gather and aggregate the data
and validated by other members of the team to ensure reliable and
produced by a range of approaches by our contributors.
consistent data.
Once collected, all incidents included in this report were individually
2. METHODOLOGY FOR CONTRIBUTORS USING VERIS
reviewed and converted (if necessary) into the VERiS framework to
Contributors using this method provided incident data to our team in
create a common, anonymous aggregate dataset. But the collection
VERiS format. For instance, agents of the U.S. Secret Service (USSS)
method and conversion techniques differed between contributors.
used an internal VERiS-based application to record pertinent case
in general, three basic methods (expounded below) were used to
details. Several other organizations recorded incidents directly into
accomplish this:
an application we created specifically for this purpose.30 For a few
1) direct recording by Verizon using VERiS contributors, we captured the necessary data points via interviews
and requested follow-up information as necessary. Whatever the
2) direct recording by contributors using VERiS
exact process of recording data, these contributors used investigative
3) re-coding using VERiS from a contributor’s existing schema notes, reports provided by the victim or other forensic firms, and their
own experience gained in handling the incident.
All contributors received instruction to omit any information that
might identify organizations or individuals involved, since such details 3. METHODOLOGY FOR CONTRIBUTORS NOT USING VERIS
are not necessary to create the DBiR. Some contributors already collect and store incident data using
their own framework. A good example of this is the CERT insider
Threat Database31 compiled by the CERT insider Threat Center at the
Sharing and publishing incident information isn’t
Carnegie Mellon University Software Engineering institute. For this
easy, and we applaud the willingness and work
and other similar data sources, we created a translation between the
of all these contributors to make this report original schema and VERiS32 and then re-coded incidents into valid
possible. We sincerely appreciate it. VERiS records for import into the aggregate dataset. We worked with
contributors to resolve any ambiguities or other challenges to data
quality during this translation and validation process.
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 51

SECURITY INCIDENTS VERSUS DATA DISCLOSURE Finally, in 1959, Jerome Cornfield and several other researchers took
The DBiR has traditionally focused exclusively on security events a step back to conduct a meta-analysis,35 which is analysis done by
resulting in confirmed data disclosure33 rather than the broader looking at the combination of several other studies (an approach Nate
spectrum of all security incidents.34 in the 2013 DBiR, we deviated Silver would apply to the 2012 U.S. presidential elections with great
from that tradition slightly by collecting and referencing a large success). They showed how the aggregate results of all the other
number of confirmed security incidents. The 2014 DBiR breaks form studies provided overwhelming evidence that linked smoking with
altogether to gain a broader view. We chose to include these incidents lung cancer. Even though each study was flawed in some way, they
to capture events such as denial of service attacks, compromises of were flawed in different ways and the aggregate had a consistency
systems without data loss, and a very large bucket of incidents where that was enough to dispel any uncertainty. it would take years for this
data loss was just simply unknown. While we think this change is for to permeate into the culture, but Cornfield’s meta-analysis was the
the better (and we hope you do too), it does mean our report on data tipping point in acknowledging the health hazards of smoking.
breaches will include more than data breaches.
While we believe many of the findings presented in this report to
A WORD ABOUT SAMPLE BIAS be appropriate for generalization, bias and methodological flaws
For years, science and statisticians debated the relationship between undoubtedly exist. However, with 50 contributing organizations this
smoking and lung cancer. Through the 1940s and 1950s cases of year, we’re aggregating across the different collection methods,
epidermoid carcinoma of the lung were on the rise and medical priorities and goals of our partners. We hope this aggregation will help
experts sought to understand why. individual studies starting in minimize the influence of any individual shortcomings in each of the
the 1950s would establish a correlation between smoking and lung samples and the whole of this research will be greater than the sum of
cancer, but each of them had statistical flaws in their methodologies. its parts.
These flaws were not errors or mistakes in any way; the flaws were
present because the real world presented imperfect data and the
researchers did the best they could to compensate for the imperfect
data. R. A. Fisher (a well-respected and famous statistician, who was
often shown smoking his pipe) was an outspoken opponent of those
studies and would put considerable effort into dissecting and refuting
the techniques and conclusions found therein. His personal beliefs
were being expressed through his expertise in statistics to such a
point that he even accused researchers of manipulating their data.
52 VERIZON ENTERPRISE SOLUTIONS

APPENDIX B:
DATA BREACHES AND IDENTITY
THEFT, A CONVOLUTED ISSUE
BY THE IDENTITY THEFT RESOURCE CENTER (ITRC)
We focus primarily on the corporate side of data breaches in this LESS-SENSITIVE PII – IMPORTANCE AND VALUE
report, but there is clearly an overlap into the consumer world. Over time, consumers have been made increasingly aware of breaches
Because that world is very much front-and-center for iTRC, we exposing passwords, usernames, and emails. These pieces of less-
thought it would be appropriate to have them contribute a perspective sensitive Pii might, on the surface, appear to have no importance
on an important aspect of breaches: consumer identity theft. and/or value, and therefore represent relatively low risk of harm.
Consumers use these pieces of information day-in and day-out, most
So you received a data breach notification letter. Does this mean you
likely without thinking about their value, or the measures in place to
are now a victim of identity theft? Not necessarily (yet).
keep them secure and private. For businesses, exposure of this data
The relationship between data breaches and identity theft is trickier does not typically even trigger the need for breach notification.
than you think. it’s more convoluted than just these two issues being
is there risk of identity of theft? This depends on the ingenuity and
related or even correlated. There are studies touting the relationship
level of motivation of the data thief. While it is true that thieves can
between receiving a data breach notification and identity theft
use this non-Pii to “socially engineer” other information about you, it
victimization, but the iTRC believes this oversimplifies the issue.
does require some degree of effort.
TYPES OF INFORMATION
SENSITIVE PII – IMPORTANCE AND VALUE
Data breaches are becoming more commonplace and understood
Most consumers readily identify credit/debit cards, and financial
by the general public, due in part to publicity surrounding the many
account information as important. When it comes to these pieces of
high profile incidents that occurred over the past year. As a result,
financial information, they understand the need to protect it — there
consumers are faced with the fact that their personal identifying
are associated risks with it being compromised. One major concern
information (Pii) is being left unsecured by those entrusted to
is who is responsible for any financial loss or expenses incurred as
protect it. Passwords, usernames, emails, credit/debit card and
a result of this occurrence. Many consumers fear exposure of this
financial account information, and Social Security Numbers are being
information may result in identity theft; not realizing additional
compromised at a staggering rate, endangering the identities of
information (see Social Security number below) is necessary to take
consumers nationwide.
it to that level. Typically, the use of financial information is limited to
The perceived significance of Pii falls along a continuum of various forms of financial fraud or existing account fraud.
importance and value – as well as risk. This issue of “perception”
The value of financial account information may be high, but it is
applies to all the players in a data breach scenario – the consumer, the
usually short-lived if the consumer takes action and closes accounts
business entity, and of course, the “data thief.” i hesitate to call the
quickly. This is facilitated by businesses making prompt breach
criminal an “identity thief” for we know not yet their underlying motive
notifications and alerting the consumer that they need to take
for stealing the Pii.
proactive measures.
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 53

Social Security numbers — the gold standard of all sensitive Pii — UNDERSTANDING TYPES OF PII AND NEED FOR FOLLOW UP ACTION
are that extra piece of information that unlocks so many doors. With Depending on the type of personal data compromised (sensitive
this data in hand, thieves can now gain access to new credit and other or less-sensitive) in any given data breach incident, many of the
benefits in the victim’s name — lines of credit, government benefits, associated risks to the consumer will be contingent upon on how
tax refunds, employment, utilities, mortgages, and even medical quickly they respond to a breach notification. This is why the
resources. The data thief is the one who truly appreciates the value of timeliness of the notification to the consumers is of significant
this information. importance. Laws aside, forewarned is forearmed. An aware
customer/client/employee/student is one who can take proactive
U.S. businesses recognize the importance of protecting these pieces
measures to minimize the risk of any potential harm.
of sensitive information because they know exposure of this data will
trigger breach notification laws around the country in 46 states. There
is a definite value to the business to implement best practices and Many of the associated risks to the consumer will
protocols to ensure the security of this information, otherwise they be contingent upon on how quickly they respond to
will face the subsequent costs of mitigating a breach.
a breach notification.
VICTIM IMPACT — PERSONAL COST (NON-FINANCIAL COSTS)
And while not all consumers who receive a data breach notification With that said, it is extremely important for consumers to understand
will become victims of identity theft, many will face the need to the steps they can take to keep their information as private as
contact credit reporting agencies, creditors, financial institutions, possible.
health care providers, and possibly law enforcement agencies, to
report that their Pii has been compromised. Placing Fraud Alerts or RECOMMENDATIONS FOR CONSUMERS
• First and foremost, never carry your Social Security card with you.
Credit Freezes, closing credit cards and financial accounts, changing
• Develop strong passwords – Don’t be like the millions of others who
passwords and PiNs, and closing or changing email accounts are just
use “12345678” or “password.” Even when hashed, these passwords
some of the possible steps one might need to take to minimize future
can easily be deciphered by data thieves.36
risk of identity theft. That said, pity those who do not receive a breach
• Don’t be too social on social media. Providing too much information
notification letter for they do not yet know their information has been
on these very public venues provides data thieves plenty of
compromised.
information to go phishing at your expense. Even if you’re not the
hottest celebrity in town, you might be more popular than the next
Placing Fraud Alerts or Credit Freezes, closing
guy on the thief’s list.
credit cards and financial accounts, changing • Shred sensitive documents – what you don’t shred, lock up in a
passwords and PINs, and closing or changing secure location.
• Monitor financial statements and be on the look for any fraudulent
email accounts are just some of the possible steps
transactions.
one might need to take to minimize future risk of
• Make every possible effort to guard your Protected Health
identity theft. information (PHi). Minimize the number of times you provide it the
doctor’s office. Ask questions such as who can access it, will it be
Many of these steps take a personal toll on consumers who encrypted, and do they take measures to store it securely. Be your
oftentimes have no idea what steps to take – even when they are own PHi watchdog.
spelled out in a breach notification letter or on a company website. All
they know is they are feeling angry, frustrated and confused. They are
frequently in an emotional and anxious state of mind. They are trying
to grasp the meaning of who is responsible for any financial losses.
How much time is it going to take to make necessary calls? Who do
they call? What’s the number? Why is the line always busy? Can you
make the call for me? Will a request for a credit report effect my
credit score? How could the business let something like this happen?
54 VERIZON ENTERPRISE SOLUTIONS

APPENDIX C:
LIST OF CONTRIBUTORS
CSIRTS INFOSEC PRODUCT AND SERVICE PROVIDERS
• CERT insider Threat Center • Akamai
• CERT Polska/NASK • Centripetal Networks, inc.
• CERT-EU European Union • FireEye
• CERT.PT • Kaspersky Lab
• Computer Emergency Response team of Ukraine (CERT-UA) • Malicious Streams
• Computer incident Response Center Luxembourg (CiRCL), National • McAfee, part of intel Security
CERT, Luxembourg • ThreatGRiD, inc.
• CyberSecurity Malaysia, an agency under the Ministry of Science, • ThreatSim
Technology and innovation (MOSTi) • Verizon DoS Defense
• industrial Control Systems Cyber Emergency Response Team • WhiteHat Security
(iCS-CERT)
ISACS
• irish Reporting and information Security Service (iRiSS-CERT)
• Center for internet Security (MS-iSAC)
• OpenCERT Canada
• Electricity Sector information Sharing and Analysis Center
• US Computer Emergency Readiness Team (US-CERT)
(ES-iSAC)
CYBER CENTERS • Financial Services iSAC (FS-iSAC)
• Centre for Cyber Security, Denmark • Public Transit iSAC (PT-iSAC)
• Council on CyberSecurity • Real Estate iSAC (RE-iSAC)
• Defense Security Service (DSS) • Research & Education iSAC (REN-iSAC)
• European Cyber Crime Center (EC3)
LAW ENFORCEMENT AGENCIES
• National Cybersecurity and integration Center (NCCiC)
• Australian Federal Police (AFP)
• Netherlands National Cyber Security Centre (NCSC-NL)
• Cybercrime Central Unit of the Guardia Civil (Spain)
FORENSIC PROVIDERS • Danish National Police, NiTES (National iT investigation Section)
• Deloitte and Touche LLP • Dutch Police: National High Tech Crime Unit (NHTCU)
• G-C Partners, LLC • Policía Metropolitana (Argentina)
• Guidance Software • Policía Nacional de Colombia
• S21sec • US Secret Service
• Verizon RiSK Team
OTHER
• Anonymous contributor
• Commonwealth of Massachusetts
• identity Theft Resource Center
• Mishcon de Reya
• VERiS Community Database (VCDB)
• Winston & Strawn
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 55

ENDNOTES
1. Yes, we’ll continue to call it the Data Breach investigations Report, even though it analyzes incidents that aren’t exclusively breaches or
derived through forensic investigations. Hey! Maybe we should just call it the “Data Report” because those two words are still dead-on.
2. Stay tuned, though. We may dig deeper into this topic once we’re free from the pressures of publishing the main report.
3. To be fair, the biggest sprees in this year’s dataset originated in both Romania and Germany
4. For the initiated, we could not reject the null-hypothesis with a p-value of 0.21 and R2 of 0.134.
5. https://www.whitehatsec.com/resource/stats.html
6. Silowash, G., Cappelli, D., Moore, A., Trzeciak, R., Shimeall, T., & Flynn, L. (2012). Common Sense Guide to Mitigating insider Threats. in
S.E. institute (Ed.), (4th ed., pp. 17): Carnegie Mellon University. http://www.sei.cmu.edu/library/abstracts/reports/12tr012.cfm
7. http://www.mishcon.com/assets/managed/docs/downloads/doc_2714/Mishcon_Recover_Report.pdf
8. Silowash, G., Cappelli, D., Moore, A., Trzeciak, R., Shimeall, T., & Flynn, L. (2012). Common Sense Guide to Mitigating insider Threats. in
S.E. institute (Ed.), (4th ed., pp. 17): Carnegie Mellon University. http://www.sei.cmu.edu/library/abstracts/reports/12tr012.cfm
9. We supplemented this pattern with data from VCDB because it is a rich source of related incidents.
10. http://veriscommunity.net/doku.php?id=enumerations#assetvariety
11. Note to self: stop leaving laptop in conference room when walking down to the cafeteria.
12. We supplemented this pattern with data from VCDB because it is a rich source of related incidents.
13. http://blog.oxforddictionaries.com/2013/11/word-of-the-year-2013-winner/
14. A major NHTCU investigation into groups using mobile malware showed that in less than a year’s time, five variations of mobile
malware for one specific bank could be detected. Modest estimates suggest that criminals gained around €50,000 per week using this
specific form of mobile malware, harvesting over 4,000 user credentials from 8,500 infected bank customers in just a few months.
Mobile malware does not move the needle in our stats as we focus on organizational security incidents as opposed to consumer device
compromises.
15. The two email vectors are almost certainly underrepresented based on the number of phishing actions in this data set. Not enough
info was provided to discern whether those phishing incidents utilized email attachments or embedded links, and so they were marked
“unknown.” Therefore, the actual number of both email vectors is surely higher than shown here, but still not be enough to overtake the
web vectors.
16. You can get more data on this by sending us a small fee to cover transfer costs. Just give us your bank account number and we will email
you the information. Bitcoins welcome.
17. We supplemented this pattern with data from VCDB because it is a good source of related incidents.
18. Espionage is not one of the more common patterns in the Public sector, but if you look solely at data breaches, it becomes quite
prominent.
19. in all honesty, some of us aren’t crazy about the “cyber” thing. Be that as it may, it is increasingly THE collectively used and understood
modifier for the type of attacks we discuss here. By “cyber,” we’re referring to computer networks, systems, and devices. We promise
not to go all cyber-cyber-cyber!!! on you; we’ll just use it as a way to reference this pattern.
56 VERIZON ENTERPRISE SOLUTIONS

20. http://en.wikipedia.org/wiki/Analysis_of_competing_hypotheses
21. https://www.cia.gov/library/center-for-the-study-of-intelligence/csi-publications/books-and-monographs/psychology-of-
intelligence-analysis/
22. https://www.cia.gov/library/center-for-the-study-of-intelligence/csi-publications/books-and-monographs/sherman-kent-and-the-
board-of-national-estimates-collected-essays/6words.html
23. See the Misuse section for analysis of insider espionage.
24. http://blogs.rsa.com/wp-content/uploads/VOHO_WP_FiNAL_READY-FOR-Publication-09242012_AC.pdf
25. See Hutchins, E. M., Cloppert, M. J., & Amin, R. M. (2010). intelligence-Driven Computer Network Defense informed by Analysis of
Adversary Campaigns and intrusion Kill Chains.
26. http://www.microsoft.com/security/sir/default.aspx
27. ...at least until February 2014, when NTP reflection became bigger-est in history – but too late for us to edit this report beyond adding
a footnote.
28. it’s funny to consider that this remnant of the rejects is about equal to the total number of breaches in the 2009 DBiR.
29. For a primer on dendrograms and hierarchical clustering techniques (our method for identifying patterns in this report), see http://
en.wikipedia.org/wiki/Hierarchical_clustering
30. See an example here: https://incident.veriscommunity.net/s3/example
31. http://www.cert.org/blogs/insider_threat/2011/08/the_cert_insider_threat_database.html
32. For instance, CERT has an attribute named “Motives and expectations” that maps very well to actor.internal.motive in VERiS.
33. VERiS defines data disclosure as any event resulting in confirmed compromise (unauthorized viewing or accessing) of any non-public
information. Potential disclosures and other “data-at-risk” events do NOT meet this criterion, and have thus not traditionally been part
of the sample set for this report.
34. VERiS defines an incident as any event that compromises a security attribute (confidentiality, integrity, availability) of an information
asset.
35. Cornfield, Jerome, et al. “Smoking and Lung Cancer: Recent Evidence and a Discussion of Some Questions.” Journal of the National
Cancer institute 22.1 (1959): 173-203.
36. Don’t believe us? Just Google 286755fad04869ca523320acce0dc6a4
VERIZON 2014 DATA BREACH INVESTIGATIONS REPORT 57

{
"action": {
"hacking": {
"variety": [
"Abuse of functionality",
"SQLi",
"Use of backdoor or C2”
ABOUT THE COVER "Brute force"
"notes": “Numerous attacks methods
were used in the remote attack of the
The “universe” of colored dots on the cover represents 4,596 Apache web server running 2.0.65 and utilizing
a password of tomcat for the admin page. The
incidents from the DBiR dataset, including all confirmed data main page was replaced with a GOCI logo of a
scary dragon, and a skull, and other evil and
menacing symbols. Not what the victim wanted
breaches over the past three years and a sample of 400 Denial of to see on their page no doubt. Default password
was used first, and the attackers moved laterally
Service attacks from last year. We calculated the distance between via SQL injection and installed a Bifrose variant
backdoor on 3 servers.”
dots using a multi-dimensional scaling technique (with the Manhattan ] " , vector": [
"Web application"
distance algorithm) with 65 VERiS fields for each incident. This ]
}
required over 6 million comparisons, and the resulting distances were },
"actor": {
"external": {
projected on a two-dimensional plane. The closer the dots, the more "country": [
"Unknown"
similar the incidents, meaning they share many VERiS characteristics ],
"motive": [
like threat actors, actions, assets, etc. The colors represent the ] , "Espionage"
“variety”: [
nine incident classification patterns discussed throughout this "Organized crime"
“notes”: “The organized group is very
report (see the Table of Contents for a section detailing how these heinous and patient when attacking their
available victims. Ruthless in nature and
selectively contracted, they can hail from
patterns were derived). Patterns in close proximity (e.g., Misuse Helsinki, or Istanbul, or Perth. They were
thought to be the main group responsible for
and Error) share many VERiS characteristics, while those that are heading up the 2006 web compromise of the
ecommerce environment (Apache 2.0.65) of a BSD
far apart (e.g., Espionage and POS intrusions) have little in common. w h e e b l p f a o n r g f a o n r i u z m e t a h a f t r a w u a d s u l t e h n e t n c a o p n p t r e o s p t r i t a h t a e t d c t a o us ed
over thirteen thousand dollars in losses. Funds
The tightness or looseness of dots within each pattern shows the laundered to another division created an
electronic-hacking division based in Bucharest
amount of variation among incidents in that pattern. The sub-pattern Romania enabling this group to branch out,
executing in a decentralized manner. Since 2009
primarily using IRC and other channels for
clusters (overlayed points and lines) were created using 10 years obfuscated communication, the group targets
regulatory agencies as well as some private
of incident data (over 100,000 incidents). We generated a force- targets. The Oslo faction has become more
fanatical; called The Guild of Calamitous
directed network graph from the frequency of VERiS fields and the I r n i t g e h n t t - , w i t n h g e , g l r e o f u t p - w h i a n s g , k n a o n w d n b a u s f s f o a c l i o a - t w i i o n n g s g w r i o t u h ps .
Sophisticated hacking techniques like the
relationships between them for each individual cluster. TARNHT (Truly Awesome Really New Hacking Thing)
can be attributed to the exploit innovation
laboratory. The FBI, CIA, NHL, NTSB, ISIS,
Underdog, and Zach Attack all have special
electro-cyber-hero divisions on the case. “
}
},
"asset": {
"accessibility": "External",
"assets": [
{
"variety": "S – Web application"
}
],
"hosting": "Internal",
"management": "Internal",
"ownership": "Victim"
},
"attribute": {
"availability": {
"variety": [
"Interruption"
]
},
"confidentiality": {
"data": [
{
"variety": "Secrets"
},
{
"variety": "Personal"
}
],
"data_disclosure": "Confirmed",
"state": [
"Unknown"
]
}
},
"discovery_method": "Int - reported by user",
"impact": {
"overall_rating": "Unknown"
},
"incident_id": "069A2112-080D-1235-813F-3DB3CEDDEDA",
"plus": {
"analysis_status": "First pass",
"analyst": "Czumak",
},
"created": "2014-03-20T20:24:00Z",
"github": "00110110.11101011.01000000.01110000",
"master_id": "069A2112-080D-1235-813F-3DB3CEDDEDA",
"modified": "2014-03-20T15:21:58Z",
"timeline": {
"notification": {
"year": 2014
}
}
},
"reference": "http://beesbeesbees.com",
"schema_version": "1.2.1",
"security_incident": "Confirmed",
"source_id": "vcdb",
"summary": "Welcome folks. Enjoy this years report.
Wow. So vectors. Much families. Many incident.",
"timeline": {
"compromise": {
"unit": "NA"
},
"exfiltration": {
"unit": "NA"
},
"incident": {
"year": 2007
}
},
"victim": {
"country": "US",
"employee_count": "101 to 1000",
"industry": "541711",
"state": "OR",
"victim_id": "Mittelos Bioscience"
}
}
verizonenterprise.com
© 2014 Verizon. All Rights Reserved. The Verizon name and logo and all other names, logos, and slogans identifying Verizon’s products and services are trademarks and service marks or registered trademarks and service marks of Verizon
Trademark Services LLC or its affiliates in the United States and/or other countries. All other trademarks and service marks are the property of their respective owners. MC15912 04/14

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-07-25", "model": "gemini-3.5-flash-lite"} -->
