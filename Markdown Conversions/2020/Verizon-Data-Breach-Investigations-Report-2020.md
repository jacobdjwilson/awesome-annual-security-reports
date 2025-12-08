# 2020 Data Breach Investigations Report

The official report URL is: https://www.verizon.com/business/resources/reports/2020-data-breach-investigations-report.pdf

## Table of Contents
- [DBIR Cheat sheet](#dbir-cheat-sheet)
- [Introduction](#introduction)
- [Summary of findings](#summary-of-findings)
- [Results and analysis](#results-and-analysis)
- [Industry analysis](#industry-analysis)
- [Does size matter? A deep dive into SMB breaches](#does-size-matter-a-deep-dive-into-smb-breaches)
- [Regional analysis](#regional-analysis)
- [Wrap-up](#wrap-up)
- [Appendices](#appendices)

---

## DBIR Cheat sheet

Hello, and welcome to the 2020 Data Breach Investigations Report (DBIR)! We have been doing this report for a while now, and we appreciate that all the verbiage we use can be a bit obtuse at times. We use very deliberate naming conventions, terms and definitions and spend a lot of time making sure we are consistent throughout the report. Hopefully, this section will help make all of those more familiar.

### VERIS resources

The terms “threat actions,” “threat actors” and “varieties” will be referenced a lot. These are part of the Vocabulary for Event Recording and Incident Sharing (VERIS), a framework designed to allow for a consistent, unequivocal collection of security incident details. Here is how they should be interpreted:

*   **Threat actor**: Who is behind the event? This could be the external “bad guy” that launches a phishing campaign or an employee who leaves sensitive documents in their seat-back pocket.
*   **Threat action**: What tactics (actions) were used to affect an asset? VERIS uses seven primary categories of threat actions: Malware, Hacking, Social, Misuse, Physical, Error and Environmental. Examples at a high level are hacking a server, installing malware and influencing human behavior through a social attack.
*   **Variety**: More specific enumerations of higher-level categories, e.g., classifying the external “bad guy” as an organized criminal group or recording a hacking action as SQL injection or brute force.

Learn more here:

*   github.com/vz-risk/dbir/tree/gh-pages/2020 includes DBIR facts, figures and figure data.
*   veriscommunity.net features information on the framework with examples and enumeration listings.
*   github.com/vz-risk/veris features the full VERIS schema.
*   github.com/vz-risk/vcdb provides access to our database on publicly disclosed breaches, the VERIS Community Database.
*   http://veriscommunity.net/veris_webapp_min.html allows you to record your own incidents and breaches. Don’t fret, it saves any data locally and you only share what you want.

### Incident vs breach

We talk a lot about incidents and breaches and we use the following definitions:

*   **Incident**: A security event that compromises the integrity, confidentiality or availability of an information asset.
*   **Breach**: An incident that results in the confirmed disclosure—not just potential exposure—of data to an unauthorized party.

### Industry labels

We align with the North American Industry Classification System (NAICS) standard to categorize the victim organizations in our corpus. The standard uses two- to six-digit codes to classify businesses and organizations. Our analysis is typically done at the two-digit level. We will specify NAICS codes along with an industry label. For example, a chart with a label of Financial (52) is not indicative of 52 as a value. “52” is the NAICS code for the Finance and Insurance sector. The overall label of “Financial” is used for brevity within the figures. Detailed information on the codes and classification system is available here:

https://www.census.gov/cgi-bin/sssd/naics/naicsrch?chart=2012

### Dotting the charts and crossing the confidence

Last year, we introduced our now (in)famous slanted bar charts to show the uncertainty due to sampling bias.[^1] One tweak we added this year was to roll up an “Other” aggregation of all the items that do not make the cut on our “Top (whatever)” charts. This will give you a better sense of the things we left out.

Not to be outdone this year, our incredible team of data scientists decided to try dot plots[^2] to provide a better way to show how values are distributed.

The trick to understanding this chart is that the dots represent organizations. So if there are 100 dots (like in each chart in Figure 1), each dot represents 1% of organizations.

In Figure 1, we have three different charts, each representing common distributions you may find in this report. For convenience, we have colored the first half and the second half differently so it’s easier to locate the median.

In the first chart (High), you see that a lot of companies had a very large value[^3] associated with them. The opposite is true for the second one (Low), where a large number of the companies had zero or a low value. On the third chart (Medium), we got stuck in the middle of the road and all we can say is that most companies have that middle value. Using the Medium chart, we could probably report an average or a median value. For the High and Low ones, an average is statistically undefined and the median would be a bit misleading. We wouldn’t want to do you like that.

Questions? Comments? Still mad because VERIS uses the term “Hacking”? Let us know! Drop us a line at dbir@verizon.com, find us on LinkedIn, tweet @VerizonBusiness with the #dbir. Got a data question? Tweet @VZDBIR!

[^1]: Check “New chart, who dis?” in the “A couple of tidbits” section on the inside cover of the 2019 DBIR if you need a refresher on the slanted bar charts.
[^2]: To find out more about dot plots, check out Matthew Kay’s paper: http://www.mjskay.com/papers/chi2018-uncertain-bus-decisions.pdf
[^3]: Don’t worry about what the value is here. We made it up to make the charts pretty. And don’t worry later either, we’ll use a real value for the rest of the dot plots.

---

## Introduction

Experience is merely the name men gave to their mistakes.
—Oscar Wilde, The Picture of Dorian Gray

Here we are at another edition of the DBIR. This is an exciting time for us as our little bundle of data turns 13 this year. That means that the report is going through a lot of big changes right now, just as we all did at that age. While some may harbor deeply rooted concerns regarding the number 13 and its purported associations with mishap, misadventure and misfortune, we here on the team continue to do our best to shine the light of data science into the dark corners of security superstition and dispel unfounded beliefs.

With that in mind, we are excited to ask you to join us for the report’s coming-of-age party. If you look closely, you may notice that it has sprouted a few more industries here and there, and has started to grow a greater interest in other areas of the world. This year, we analyzed a record total of 157,525 incidents. Of those, 32,002 met our quality standards and 3,950 were confirmed data breaches. The resultant findings are spread throughout this report.

This year, we have added substantially more industry breakouts for a total of 16 verticals (the most to date) in which we examine the most common attacks, actors and actions for each. We are also proud to announce that, for the first time ever, we have been able to look at cybercrime from a regional viewpoint—thanks to a combination of improvements in our statistical processes and protocols, and, most of all, by data provided by new contributors—making this report arguably the most comprehensive analysis of global data breaches in existence.

We continue to use the VERIS framework to classify and analyze both incidents and breaches, and we have put additional focus on this process in order to improve how VERIS connects and interacts with other existing standards. We also aligned with the Center for Internet Security (CIS)[^4] Critical Security Controls and the MITRE ATT&CK®[^5] framework to improve the types of data we can collect for this report, and to map them to appropriate controls.

A huge “thank you” is in order to each and every one of our 81 contributors representing 81 countries, both those who participated for the first time in this year’s report, and those tried-and-true friends who have walked this path with us for many years. This document, and the data and analysis it contains, would not be possible without you, and you have our most sincere thanks and heartfelt gratitude. And while we are on that topic, the way to continue to grow and improve is to have more quality organizations like yours join us in this fight against the unknown and the uncertain. Therefore, we urge you to consider becoming a data contributor and help us to continue to shed light into dark places.

Finally, thank you, our readers, for sticking with us these many years and for sharing your expertise, advice, encouragement and suggestions so that we can continue to make this report better each year.

Sincerely,
The DBIR Team

(in alphabetical order)

Gabriel Bassett
C. David Hylender
Philippe Langlois
Alexandre Pinto
Suzanne Widup

[^4]: https://www.cisecurity.org/
[^5]: https://attack.mitre.org/

---

## Summary of findings

![Figure 2. What tactics are utilized? (Actions)](https://i.imgur.com/example.png)
*45% of breaches featured Hacking*
*Errors were causal events in 22% of breaches*
*22% included Social attacks*
*17% involved Malware*
*4% of breaches had four or more attacker actions*
*8% of breaches were Misuse by authorized users*
*1% involved Partner actors*
*Physical actions were present in 4% of breaches*

![Figure 3. Who’s behind the breaches?](https://i.imgur.com/example.png)
*70% perpetrated by External actors*
*30% involved internal actors*

![Figure 4. Who are the victims?](https://i.imgur.com/example.png)
*72% of breaches involved large business victims*
*28% of breaches involved small business victims*

![Figure 5. What are the other commonalities?](https://i.imgur.com/example.png)
*81% of breaches were contained in days or less*
*86% of breaches were financially motivated*
*Web applications were involved in 43% of breaches*
*58% of victims had Personal data compromised*
*37% of breaches stole or used credentials*
*27% of Malware incidents were Ransomware*
*22% of breaches involved Phishing*

---

## Results and analysis

The results found in this and subsequent sections within the report are based on a dataset collected from a variety of sources, including cases provided by the Verizon Threat Research Advisory Center (VTRAC) investigators, cases provided by our external collaborators and publicly disclosed security incidents. The year-to-year data will have new incident and breach sources as we continue to strive to locate and engage with additional organizations that are willing to share information to improve the diversity and coverage of real-world events. This is a sample of convenience,[^6] and changes in contributors—both additions and those who were not able to contribute this year—will influence the dataset. Moreover, potential changes in contributors’ areas of focus can shift bias in the sample over time. Still other potential factors, such as how we filter and subset the data, can affect these results. All of this means that we are not always researching and analyzing the same population. However, they are all taken into consideration and acknowledged where necessary within the text to provide appropriate context to the reader. Having said that, the consistency and clarity we see in our data year-to-year gives us confidence that while the details may change, the major trends are sound.

Now that we have covered the relevant caveats, we can begin to examine some of the main trends you will see while reading through this report. When looking at Figure 6 below, let’s focus for a moment on the Trojan[^7] line. When many people think of how hacking attacks play out, they may well envision the attacker dropping a Trojan on a system and then utilizing it as a beachhead in the network from which to launch other attacks, or to expand the current one. However, our data shows that this type of malware peaked at just under 50% of all breaches in 2016, and has since dropped to only a sixth of what it was at that time (6.5%). Likewise, the trend of falling RAM-scraper malware that we first noticed last year continues. We will discuss that in more detail in the “Retail” section. As this type of malware decreases, we see a corresponding increase in other types of threats. As time goes on, it appears that attackers become increasingly efficient and lean more toward attacks such as phishing and credential theft. But more on those in the “Social” and “Hacking” subsections respectively. Other big players this year, such as Misconfiguration and Misdelivery, will be examined in the “Error” subsection.

![Figure 6. Select action varieties in breaches over time](https://i.imgur.com/example.png)

[^6]: Convenience sampling is a type of nonrandom sampling that involves the sample being drawn from that part of the population that is close to hand or available. More details can be found in our “Methodology” section.
[^7]: This year, we added a Trojan category to Malware. This is a combination of Malware RAT, Malware C2 and Backdoor, Hacking Use of backdoor or C2, and Malware Spyware/Keylogger.

### Actors

Let us begin by disabusing our readers of a couple of widely held, but (according to our data) inaccurate beliefs. As Figure 7 illustrates, in spite of what you may have heard through the grapevine, external attackers are considerably more common in our data than are internal attackers, and always have been. This is actually an intuitive finding, as regardless of how many people there may be in a given organization, there are always more people outside it. Nevertheless, it is a widely held opinion that insiders are the biggest threat to an organization’s security, but one that we believe to be erroneous. Admittedly, there is a distinct rise in internal actors in the dataset these past few years, but that is more likely to be an artifact of increased reporting of internal errors rather than evidence of actual malice from internal actors. Additionally, in Figure 8, you’ll see that Financially motivated breaches are more common than Espionage by a wide margin, which itself is more common than all other motives (including Fun, Ideology and Grudge, the traditional “go to” motives for movie hackers). There is little doubt that Cyber-Espionage is more interesting and intriguing to read about or watch on TV. However, our dataset indicates that it is involved in less than a fifth of breaches. But don’t let that keep you away from the cinema, just make sure to save us some popcorn.

In regard to incidents, Figure 9 illustrates that Financial is still the primary motive, but it must be acknowledged that the Secondary motivation is not far behind. As a refresher (or fresher for our new readers), the compromised infrastructure in Secondary incidents is not the main target, but a means to an end as part of another attack. In fact, if we had included the Secondary Web application breaches (we removed this subset as mentioned in the “Incident classification patterns and subsets” section), the Secondary motive category would actually be higher than Financial.

When we look at criminal forums and underground data, 5% refer to a “service.” That service could be any number of things including hacking, ransomware, Distributed Denial of Service (DDoS), spam, proxy, credit card crime-related or other illicit activities. Worse still, that “service” may just be hosted on your hardware. The simple fact is this: If you leave your internet-facing assets so unsecured that taking them over can be automated, the attackers will transform your infrastructure into a multi-tenant environment.

![Figure 7. Actors over time in breaches](https://i.imgur.com/example.png)

![Figure 8. Actor motives over time in breaches](https://i.imgur.com/example.png)

![Figure 9. Top Actor motives in incidents (n = 3,828)](https://i.imgur.com/example.png)

![Figure 10. Top Actor varieties in breaches (n = 977)](https://i.imgur.com/example.png)

A good follow-up question might be “where are these unwanted occupants coming from?” Figure 10 shows that Organized crime[^8] is the top variety of actor for the DBIR. After that, we see a roundup of the usual suspects: State-aligned actors who are up to no good, internal End users and System admins making errors as though they were paid to do it, and, at the very bottom, the Unaffiliated. Although they may sound like the title of a book series for young adults, they are actually an interesting group. These are people from areas unknown and their motivation is not always readily apparent. One potential origin for these actors might be gleaned from looking at the criminal forum and marketplace data we referenced above. About 3% of the forum threads related to breach and incident cybercrime[^9] were associated with training and education.[^10]

These are would-be hackers who are still serving out their apprenticeship, for lack of a better term. In fact, as noted by the United Kingdom’s National Crime Agency, “Offenders begin to participate in gaming cheat websites and ‘modding’ (game modification) forums and progress to criminal hacking forums without considering the consequences.”[11] In other words, this is a group of individuals with a certain skill set but no clear sense of direction, who could perhaps, given the right amount of persuasion and incentive, be kept from the dark side and thereby added to the talent pool for our industry. Giving them a career and a future rather than a jail sentence is, in the long run, better for all concerned. Although it is handy to know a game cheat every now and again.

Another thing you might be wondering is where the attackers are coming from. Based off of computer data breach and business email compromise complaints to the FBI Internet Crime Complaint Center (IC3), 85% of victims and subjects were in the same country, 56% were in the same state and 35% were even in the same city. In part, this is driven by many of the complaints coming from high-population areas such as Los Angeles, CA, and New York City, NY. So, the proverbial call is almost coming from inside the building.

[^8]: When we say “Organized crime,” we mean “a criminal with a process,” not “the mafia.”
[^9]: Cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber, cyber.
[^10]: Matched a search for guide, tutorial, learn or train in the title or body.
[^11]: Pathways into Cyber Crime, NCA, 2017 (https://www.nationalcrimeagency.gov.uk/who-we-are/publications/6-pathways-into-cyber-crime-1/file).

### Actions

When we analyzed the high-level actions on Figure 11, we found that it mirrors Figure 6. The only action type that is consistently increasing year-to-year in frequency is Error. That isn’t really a comforting thought, is it? Nevertheless, there is no getting away from the fact that people can, and frequently do, make mistakes and many of them probably work for you.

Physical breaches have stayed relatively level and infrequent, but Misuse, Hacking, Malware and Social have all decreased since last year’s report. While Hacking and Social are down as a percent, they have remained close to the levels we have seen for the past few years. On the other hand, Malware has been on a consistent and steady decline as a percentage of breaches over the last five years.

Why is this? Has malware just gone out of fashion like poofy hair and common courtesy? No, we think that other attack types such as hacking and social breaches benefit from the theft of credentials, which makes it no longer necessary to add malware in order to maintain persistence. So, while we definitely cannot assert that malware has gone the way of the eight-track tape, it is a tool that sits idle in the attacker’s toolbox in simpler attack scenarios.

It is important to keep in mind that the points made above are in reference to breaches and not incidents. The incidents tell us a somewhat different story. Ransomware—which in our dataset rarely results in a confirmed breach[^12] unless paired with credential use—is on the rise. Still, as malware tools continue to evolve and improve, there appears to be a sense that malware prevalence is decreasing somewhat, as this causes fewer instances that rise to the status of “incident” for our data contributors. This seems to have the effect on our dataset of a polarization: malware being either part of advanced attacks or the simpler (yet still effective) smash-and-grab compromises.

![Figure 11. Actions over time in breaches](https://i.imgur.com/example.png)

[^12]: We are aware of reports of ransomware families that are now capturing data before encrypting so the actors can threaten to also expose the data if the ransom is not paid. However, the cases logged were documented after October 31, 2019, the close date of the data scope for this issue.

### Threat action varieties

Taking a peek at threat action varieties allows us to dig a bit deeper into the bad guy’s toolbox. Figure 12 provides an idea of what action varieties drive incident numbers and, shocker, Denial of Service (DoS) plays a large part. We also see a good bit of phishing, but since data disclosure could not be confirmed, they remain incidents and do not graduate to breach status (but maybe they can if they take a couple of summer classes). In sixth overall, we see ransomware popping up like a poor relation demanding money—which, in many cases, they get.

When we again switch back to looking at the top Action varieties for breaches in Figure 13, we see our old foes, Phishing, Use of stolen credentials and Misconfiguration in the top five. Misdelivery is making an impressive showing (mostly documents and email that ended up with the wrong recipients) this year. While we don’t have data to prove it, we lean toward the belief that this is an artifact of breach disclosure becoming more normalized (and increasingly required by privacy laws around the world), especially for errors.

Finally, you’ll notice “Other” in the mix. As we mentioned in the “DBIR Cheat sheet” section at the very beginning of this report, “Other” represents any enumeration not represented by one of the categories in the figure. It turns out there are a lot of breaches (675 to be specific) that didn’t contain any of the top varieties. Breaches (like people and problems) come in many shapes and sizes and are never too far away from your front door.

![Figure 12. Top threat Action varieties in incidents (n = 23,619)](https://i.imgur.com/example.png)

![Figure 13. Top threat Action varieties in breaches (n = 2,907)](https://i.imgur.com/example.png)

### Error

Errors definitely win the award for best supporting action this year. They are now equally as common as Social breaches and more common than Malware, and are truly ubiquitous across all industries. Only Hacking remains higher, and that is due to credential theft and use, which we have already touched upon. In Figure 14 you can see that since 2017, Misconfiguration errors have been increasing. This can be, in large part, associated with internet-exposed storage discovered by security researchers and unrelated third parties. While Publishing errors appear to be decreasing, we wouldn’t be surprised if this simply means that errors formerly attributed to publishing a private document on an organization’s infrastructure accidentally now get labeled Misconfiguration because the system admin set the storage to public in the first place.

Finally, it is also worth noting what isn’t making the list. Loss is down among the single digits this year. Disposal errors are also not really moving the needle. Errors have always been present in high-ish numbers in the DBIR in industries with mandatory reporting requirements, such as Public Administration and Healthcare. The fact that we now see Error becoming more apparent in other industries could mean we are getting better at admitting our mistakes rather than trying to simply sweep them under the rug.

Of course, it could also mean that since so many of them are caught by security researchers and third parties, the victims have no choice but to utter “mea culpa.” Security researcher has become the most likely Discovery method for an Error action breach by a significant amount (Figure 15), being over six times more likely than it was last year. However, we here on the DBIR team are of an optimistic nature, so we will go with the former conclusion.

![Figure 14. Top Error varieties over time in breaches](https://i.imgur.com/example.png)

![Figure 15. Top discovery methods in Error breaches (n = 95)](https://i.imgur.com/example.png)

### Malware

Our Malware findings further reinforce the trends of phishing and obtaining credentials with regard to breaches. As Figure 16 illustrates, Password dumper (used to get those sweet, sweet creds) has taken the top spot among breach Malware varieties. Email (usually associated with Phishing) and Direct install (an avenue generally—but not always—requiring credentials) are the top vectors.

Ransomware is the third most common Malware breach variety and the second most common Malware incident variety. Downloaders follow closely behind Ransomware, and they are clearly doing their jobs, not only moving Ransomware, but also Trojans.[^13] It is perhaps worth noting that Cryptocurrency mining doesn’t even make the top 10 list, which we know is sure to disappoint all our HODL readers.

However, it is important to acknowledge that the relative percentage of Malware that we see present in breaches and incidents may not correspond to your experiences fighting, cleaning and quarantining malware throughout your own organization. With that in mind, we would like to spend some time talking about bias, more precisely survivorship bias regarding those varieties.

![Figure 16. Top Malware varieties in breaches (n = 506)](https://i.imgur.com/example.png)

![Figure 17. Top Malware vectors in breaches (n = 360)](https://i.imgur.com/example.png)

[^13]: A combination of multiple malware varieties: RAT, Trojan, C2, Backdoor and Spyware/keylogger

#### Survivorship bias

We talk about survivorship bias (or more formally selection bias) in the “Methodology” section, but this is a good place for a call out. You, us, everyone looks at a lot of malware data. Our incident corpus suffers from the opposite of survivorship bias. Breaches and incidents are records of when the victim didn’t survive. On the other hand, malware being blocked by your protective controls is an example of survivorship bias where the potential victim didn’t get the malware. Since we have both types of data at our disposal in the DBIR, it can highlight four possible situations:

1.  **Large numbers in both blocks and incidents**: This is something big. It’s being blocked but also happening a lot
2.  **Large numbers in incidents but not blocks**: This is potentially happening more than it’s being caught
3.  **Large numbers in blocks but not incidents**: We’re doing well at this. It’s getting caught more than it’s getting through
4.  **Small numbers in both blocks and incidents**: This just ain’t happening much

#### Ransomware

Traditionally, Ransomware is categorized as an incident in the DBIR and not as a breach, even though it is considered a breach in certain industries for reporting purposes (such as Healthcare) due to regulatory guidance. The reason we consider it only an incident is because the encryption of data does not necessarily result in a confidentiality disclosure. This year, however, ransomware figures more prominently in breaches due in large part to the confirmed compromise of credentials during ransomware attacks. In still other cases, the “breach” designation was due to the fact that personal information was known to have been accessed in addition to the installation of the malware.

Ransomware accounted for 3.5% of unique malware samples submitted for analysis, not such a big number overall. At least one piece of ransomware was blocked by 18% of organizations through the year,[^14] even though it presented a fairly good detection rate of 82% in simulated incident data.

However, it shows up heavily in actual incidents and breaches, as discussed previously. This indicates that it falls into category #2 in the survivorship bias callout. It’s a big problem that is getting bigger, and the data indicates a lack of protection from this type of malware in organizations, but that can be stopped. Part of its continued growth can be explained by the ease with which attackers can kick off a ransomware attack. In 7% of the ransomware threads found in criminal forums and market places, “service” was mentioned, suggesting that attackers don’t even need to be able to do the work themselves. They can simply rent the service, kick back, watch cat videos and wait for the loot to roll in.

It’s a big problem that’s continuing to get bigger.

#### Droppers and Trojans

As we pointed out earlier, Trojans, although still in the top five malware varieties, have been decreasing over time. However, their backdoor and remote-control capabilities are still a key functionality for more advanced attackers to operate and achieve their objectives in more intricate campaigns. Downloaders are a common way to get that type of malware on the network, and they made up 19% of malware samples. Nineteen percent were classified as backdoors and 12% were keyloggers.

Droppers and Trojans seem to fall into category #3 in the survivorship bias callout. We see them quite frequently in malware, but they do not necessarily appear in a large number of incidents and breaches. One possible explanation for this is that we might be simply getting better at blocking the cruder and more commoditized versions of this type of malware, thereby pushing unsophisticated attackers increasingly to smash-and-grab tactics. Additionally, the shift to web interfaces for most of our services may simply mean Trojans have a smaller attack surface to exploit.

[^14]: Please bear in mind that incidents that would result in a Ransomware attack can also be stopped before the malware even manifests itself, so this is maybe an underestimation.

#### Malware with vulnerability exploits

If Droppers and Trojans are examples of category #3, then Malware that exploits vulnerabilities falls under category #4. It ranks at the bottom of malware varieties in Figure 16. Figure 25 (ahead in the “Hacking” section) shows that exploiting vulnerabilities in Malware is even more rare than in Hacking (where it’s already relatively scarce). While successful exploitation of vulnerabilities does still occur (particularly for low-hanging fruit as in Figure 22—also in the “Hacking” section), if your organization has a reasonable patch process in place, and you do not have a state-aligned adversary targeting you, then your time might be better spent attending to other threat varieties.

#### Cryptocurrency mining

The cryptocurrency mining malware variety falls squarely into category #4. It accounted for a mere 2.5% of malware among breaches and only 1.5% of malware for incidents. Around 10% of organizations received (and blocked) Cryptocurrency mining malware at some point throughout the course of the year.[^15]

The breach simulation data clues us in on what might be happening, as it indicates that the median block rate for cryptocurrency mining malware was very high. Another valid theory is that cryptomining occurrences rarely rise to the level of “reported incident” unless we are talking about instances running on stolen cloud infrastructure. These cost your organization a lot of money while generating less loose change than the threat actor could have found in their couch cushions.

![Figure 18. Top malware filetypes and delivery methods](https://i.imgur.com/example.png)

[^15]: The potential underestimation from incidents being stopped before the malware manifests itself is also valid here.

### Malware delivery

Finally, this year we’ve dug a bit deeper into the malware delivery methods. Office documents and Windows® apps still tend to be the malware filetype of choice; however, the “Other” category has also grown relatively large. Most malware is still delivered by email, with a smaller amount arriving via web services, and almost none by other services (at least when detected).

One takeaway from Figure 18 is that the “average” really doesn’t represent a great many companies. For example, approximately 22% of organizations got almost none of their malware via email, while about 46% got almost all of theirs that way. If you look at the Office documents part of the malware filetypes chart, other than a spike of organizations near 0%, all the other dot piles are almost the same—meaning that type of delivery is almost uniformly distributed. When attempting to determine what percentage of malware your organization would receive as an Office document, you would be as likely to be correct by throwing a dart at that figure[^16] as by basing it on data. This is not to indicate that it is low, just that it is simply all over the map.

Speaking of maps, Figure 19 provides a glimpse at the other filetypes of malware organizations typically see. It lacks the detail of Figure 18, but still serves as an adequate visual reminder that malware comes in a variety of types, most of which apparently look like lengths of hardwood flooring. Thankfully, as we stated previously, malware is not showing up as frequently in incidents and breaches. So, if you obtain a good tool to block it where possible you can focus your attention on more pressing matters.[^17]

[^16]: Other than zero obviously. And please exercise caution with sharp objects around coworkers, family members and pets if you attempt this.
[^17]: Credential theft and use, Phishing and Errors.

### Hacking

At a high level, Hacking can be viewed as falling into three distinct groups: 1) those utilizing stolen or brute-forced credentials; 2) those exploiting vulnerabilities; and 3) attacks using backdoors and Command and Control (C2) functionality.

However, it must be said that Hacking and even breaches in general (at least in our dataset) are driven by credential theft. Over 80% of breaches within Hacking involve Brute force or the Use of lost or stolen credentials. These Hacking varieties (Figure 20 below), along with exploitation of a vulnerability (of which SQLi is a part), are associated in a major way with web applications as illustrated in Figure 21. We have spent some time on this over the last year, and it is important to reassert that this trend of having web applications as the vector of these attacks is not going away. This is associated with the shift of valuable data to the cloud, including email accounts and business-related processes.

Use of backdoor or C2 (checking in at third place) are both associated with more advanced threats, since, for more intricate campaigns and data exfiltration missions, there is nothing quite like the human touch. For better or worse, the promise of fully autonomous Artificial Hacking Intelligence (AHI) is still at least 15 years away,[^18] along with flying cars.

![Figure 20. Top Hacking varieties in breaches (n = 868)](https://i.imgur.com/example.png)

![Figure 21. Top Hacking vectors in breaches (n = 1,361)](https://i.imgur.com/example.png)

[^18]: [citation needed] I read this in some vendor marketing copy somewhere, I’m sure. OK, I didn’t, but doesn’t it sound like something I would?

![Figure 22. Connection attempts by port over time in honeypot data (n = 2.55 billion)](https://i.imgur.com/example.png)

#### Using and abusing credentials

Criminals are clearly in love with credentials, and why not since they make their jobs much easier? If you refer back to Figure 6 at the very beginning of the Results and Analysis section, it is apparent that use of credentials has been on a meteoric rise. Figure 22 represents connection attempts by port over time based on contributor honeypot data, and provides another take on the topic. As it depicts, SSH (port 22) and Telnet (port 23) connection attempts are two orders of magnitude[^19] above the next cluster of services. Let’s explore credential stuffing and then move on to exploiting vulnerabilities.

Additional contributor data sheds light onto the credential stuffing attacks criminals are attempting. Figure 23[^20] shows the number of attempts orgs who had any credential stuffing attempts typically received.