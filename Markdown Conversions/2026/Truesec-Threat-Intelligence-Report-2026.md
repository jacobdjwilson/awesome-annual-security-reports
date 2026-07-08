# Threat Intelligence Report 2026

## Table of Contents
- [About The Report](#about-the-report)
- [Acknowledgements](#acknowledgements)
- [Executive Summary](#executive-summary)
- [The Threat Landscape](#the-threat-landscape)
- [The End Of Rules-Based Order](#the-end-of-rules-based-order)
- [Conflicts In Cyberspace](#conflicts-in-cyberspace)
- [Blurred Boundaries](#blurred-boundaries)
- [The Globalization Of Cybercrime](#the-globalization-of-cybercrime)
- [The Fight Against Cybercrime](#the-fight-against-cybercrime)
- [Cybercrime & Other Crime](#cybercrime--other-crime)
- [Threat Actors & Their Motivators](#threat-actors--their-motivators)
- [Observations From Truesec](#observations-from-truesec)
- [Focus Areas](#focus-areas)
- [The Constant Evolution Of Social Engineering](#the-constant-evolution-of-social-engineering)
- [Threats From Within](#threats-from-within)
- [When The Threat Doesn’t Go Away](#when-the-threat-doesn’t-go-away)
- [The Complexity Of Large And Multinational Organizations](#the-complexity-of-large-and-multinational-organizations)
- [Password Attacks Are Still Relevant](#password-attacks-are-still-relevant)
- [Malicious Packages Pose Software Supply Chain Risk](#malicious-packages-pose-software-supply-chain-risk)
- [Deep Dive: The Malicious PDF Editor](#deep-dive-the-malicious-pdf-editor)
- [The Use Of AI In Cyberattacks](#the-use-of-ai-in-cyberattacks)
- [The Challenge Of Knowing When "The Regular" Becomes A Threat](#the-challenge-of-knowing-when-the-regular-becomes-a-threat)
- [Not Taking The Regular For Granted](#not-taking-the-regular-for-granted)
- [Hybrid Warfare](#hybrid-warfare)
- [Outlook 2026](#outlook-2026)

---

## About The Report
Welcome to the seventh release of our annual Threat Intelligence Report. This report aims to contextualize cybersecurity trends and support defenders in their work to secure networks, prevent breaches, and minimize impact in a seemingly unpredictable world.

The first part of the report examines the current threat landscape, threat actors, and relevant cybercrime statistics derived from Truesec’s engagements throughout 2025. The report then highlights a series of current cybersecurity challenges, supported by real-world examples observed by our SOC and CSIRT teams, and recommends solutions. We conclude the report with our view of what we see on the horizon for 2026 and present our predictions in the Outlook section.

While examples are drawn from real-world experience, the case studies in this report are anonymized and sometimes an amalgamation of several incidents to protect client confidentiality. Our research encompasses a broad range of activities that generate data for our analysis. In addition to our own sources and accumulated knowledge from actual breaches and vulnerabilities, we also utilize information from private industry and law enforcement partnerships.

We are only as good as the work we deliver, and we appreciate any feedback you may have regarding this report. Please contact Truesec if you have any questions or comments.

## Acknowledgements
This report is the result of the relentless and dedicated work of the Truesec Threat Intelligence team. Their deep understanding of the cyber threat landscape and threat actors, combined with extensive experience in intelligence collection, processing, analysis, and dissemination, has been essential to its development.

As much of their work necessarily takes place behind the scenes, we would like to take this opportunity to formally recognize and express our sincere appreciation for their expertise, professionalism, and continued commitment.

## Executive Summary
Cybercrime is still the most prevalent cyber threat to most organizations, but it is not all about ransomware. Technology evolution, spearheaded by agentic AI, will change the game for both attackers and defenders.

Cyberspace is a mirror of the geopolitical landscape. Cyber defenders need to prepare for a future in which Europe will increasingly have to find its own way, including in the cyber domain.

It appears that more organizations now have greater visibility into their environments and can acquire assistance to avert serious cyberattacks earlier in the kill chain. This has reduced the impact of many breaches. According to Truesec data, the total number of ransomware incidents in the Nordics in which a threat actor successfully encrypted victims decreased in 2025 compared with previous years. Instead, we have observed a corresponding increase in the number of incidents in which the threat actor was kicked out of the environment before reaching their final objective.

Initial attack vectors in breaches remain largely the same, even as the number of supply chain attacks has increased. At the same time, methods for establishing persistence within an environment have evolved. A majority of threat actors, both cybercriminals and cyber espionage groups, are no longer deploying hacking tools such as remote access trojans (RATs) or Cobalt Strike on victims’ networks. Instead, they use commercially available remote management and monitoring (RMM) tools to ensure persistence. Various types of sideloading, hijacking, and the use of vulnerable drivers remain prevalent mechanisms across a wide range of attacks and steps within the kill chain.

Modern IT is full of integration and dependencies. Today, some of an organization’s most sensitive data may reside outside the typical network boundary. Threat actors are aware of this, and there are an increasing number of methods and attacks targeting web cookies and credentials stored in browsers used to access various software-as-a-service (SaaS) portals.

In 2026, Truesec expects more threat actors to incorporate large language models (LLMs) and other AI-based solutions into their attack chains. Skilled threat actors will use AI to automate tasks, making them cheaper and quicker to perform. This will not fundamentally change the challenge facing defenders, but it will likely necessitate faster responses. It can potentially also lead to a new wave of mass extortion attacks against smaller enterprises deemed unworthy of more targeted attacks.

The widespread adoption of AI will also make AI itself an attack surface. LLMs and other AI systems exposed to the internet will be targeted with prompt-injection attacks. In 2026, Truesec assesses that threat actors will start experimenting with using company LLMs to assist them in mapping their victims’ environments, once they have gained a foothold. In 2026, your company’s LLM could become the ultimate insider threat.

A key trend in the current threat landscape is the weakening of the international rules-based order. Since the end of World War II, the Western alliance has promoted a legal framework to manage global conflicts. Today, many of these established rules are being challenged, and their validity questioned. In this context, a robust and united European approach to cybersecurity is more crucial than ever. A key takeaway is that asymmetric conflicts shape the contemporary threat landscape. The armed invasion of Ukraine is met with financial sanctions from the West, which in turn triggers retaliation in the form of sabotage and disinformation. Regardless of the points of conflict between Europe and our adversaries, they will seek out our weakest spot. If cybersecurity is lacking, they will focus their efforts there.

## The Threat Landscape
### The End Of Rules-Based Order
A general theme for this threat landscape is the erosion of the international rules-based order. Since World War II, the Western alliance, led by the U.S., has advocated a rules-based order as a legal framework for managing international conflicts. Many of these rules are now being ignored with no consequences.

U.S. leadership of the Western alliance is eroding amid shifts in U.S. politics under the current administration. Rather than viewing the U.S.’s role as an unchallenged leader of the Western bloc and custodian of international regimes as a vital privilege to protect, the administration appears to see it as a power to be leveraged.

The effects of the U.S. administration’s “America First” policies have influenced both national security and cybersecurity in Europe. Just as Europe has been forced to initiate a program of rearmament amid doubts about Trump’s commitment to NATO, there are now also doubts about Europe’s dependence on U.S. information technology.

Another problem with the U.S. administration’s unpredictable leadership is that it undermines collective cybersecurity efforts. The U.S. Cybersecurity and Infrastructure Security Agency’s (CISA) efforts to track Russian influence operations have reportedly been curtailed, and laws that promote collaboration between the U.S. government and private industry on cyber incidents have lapsed. Today, European nations are increasingly pressured by both the U.S. and China to align with these countries’ respective positions on global conflicts, or face consequences.

As the international rules-based order crumbles, and there is a risk that international efforts against cyberattacks begin to fracture, adversaries like Russia, Iran, North Korea, and China appear to collaborate closer than ever, while the U.S. is increasingly acting on its own.

### Conflicts In Cyberspace
The political and military alliance between Russia, Iran, and North Korea is also replicated in cybercrime. As North Korean soldiers fight under Russian command in Ukraine, and Iran supplies Russia with drone technology, North Korean and Iranian cybercriminals also collaborate with Russian ransomware groups.

The primary driver is the war in Ukraine. Russian society is under increasing pressure due to the costs of the war in Ukraine. Ukraine’s campaign to target Russia’s oil and gas industry is hurting Russia both financially and logistically.

One of Russia’s main objectives is to isolate Ukraine by undermining the support from the West. The Russian strategy to achieve this is a combination of threats, sabotage, and disinformation. Russia invests significant sums in supporting extremist parties in Europe, both on the left and the right, to incentivize them to create strife and be openly critical of Ukraine. Russia also maintains a campaign of sabotage and other forms of pressure on Western allies to dissuade further support for Ukraine.

The geopolitical situation will determine the risk of cyber sabotage against Europe and its critical infrastructure. Today, international conflicts are often asymmetrical. The destruction of cables in the Baltic Sea, GPS jamming, drone disruptions, and DDoS attacks are all highly likely part of Russia’s attempt to force Europe to end its support for Ukraine. At the same time, the West uses economic sanctions against Russia to force an end to its aggressive war.

Russia may raise the stakes and conduct more destructive attacks on critical infrastructure in Europe. In our chapter on Hybrid Warfare, we explore how this affects cybersecurity.

### Blurred Boundaries
Another example of the erosion of the rules-based order is the blurring of the boundaries between state-sponsored cyber actors, private actors, and cybercriminals. Under pressure from the faltering war in Ukraine, the Russian government is increasingly leaning on criminal structures to support its efforts. Russian organized crime is enlisted to smuggle sanctioned items to Russia, while Russian cybercriminals breach networks or steal credentials and then sell the access to Russian intelligence agencies.

The collaboration between security services and criminals is almost always transactional, but the government doesn’t always pay in money; it may also extort criminals by offering “protection” from being drafted into its cyber-espionage units or even being sent to the front. This suggests that Russian authorities, such as the Russian Federal Security Service (FSB), tolerate, guide, and potentially profit from ransomware actors.

While Russia’s war in Ukraine dominates Europe’s security threats, China is also a significant factor in Europe’s cybersecurity. The commercial nature of much of China’s cyber espionage also means that some private companies involved, engage in cybercrime. There are examples of Chinese threat actors linked to private companies that conduct cyber espionage for profit, and sometimes also engage in ransomware operations.

As boundaries blur and the rules-based order erodes, today’s conflicts are increasingly asymmetric. An armed invasion is met with financial sanctions, which in turn trigger retaliation in the form of sabotage and disinformation. Regardless of the points of conflict between states and their adversaries, they will target their enemy’s weakest spot. If our cybersecurity is lacking, then that is where our adversaries will strike.

### The Globalization Of Cybercrime
While organized cybercrime is a global problem, cybercrime has traditionally been divided into distinct regional ecosystems. Russia is home to much of the infrastructure used in ransomware. Western Africa is the center for an ecosystem of cyberfraud and business email compromise (BEC)[^1]. Southeast Asia is the hub for so-called “pig slaughtering”, fraud based on romance scams, and human trafficking.

As cybercrime matures, these ecosystems are increasingly merging, and cybercriminals from different parts of the world are collaborating more. Cybercriminals from Pakistan can sell phishing kits to Chinese cybercriminals in Africa or access brokers in Russia.

Geopolitical alliances are also duplicated in the cybercriminal world. North Korea’s “Lazarus” group, a part of North Korea’s military intelligence service, now collaborates with Russian ransomware groups to finance North Korea’s program for weapons of mass destruction. At the same time, Iranian cyber espionage actors sell access to Russian cybercriminals for profit.

In recent years, Western cybercriminals, mainly from the U.S. and the UK, but also from France, Canada, and Brazil, have emerged who conduct cyber extortion, sometimes in collaboration with Russian RaaS groups. These hackers are often technically proficient and excel at various forms of social engineering, but they are often less professional in their business dealings than their Russian counterparts. Some of them also collaborate with Russian criminals and deliver ransomware from Russian ransomware syndicates in exchange for a share of the profits.

They belong to a loosely organized online collective known as “The Com,” comprising young hackers driven by a toxic mixture of contempt for society and a desire for quick wealth and fame. They meet and radicalize one another in online spaces such as 4chan and Discord. They even recruit new members among young teenagers in game chat rooms such as Roblox and Minecraft.

As organized crime infiltrates society worldwide, cybercriminals are increasingly organizing on a global scale. While the ransomware ecosystem remains centered in Russia, it now includes cybercriminals from around the world.

[^1]: Read more about BEC in the Truesec Threat Intelligence Report 2025.

### The Fight Against Cybercrime
Both Truesec data and independent sources indicate that the number of severe ransomware attacks has declined since the 2023 peak, in both the Nordics and Northern Europe. The number of significant ransomware incidents has decreased by more than a third compared with earlier periods.

Even if we at Truesec see a decrease in ransomware attacks, independent sources show that ransomware attacks are still on the rise. One possible explanation is that many attacks that could have been classified as ransomware go undetected. Smaller and mid-sized companies are also more frequently targeted than large enterprises, adding to the number of unreported attacks.

Several factors may explain the decline in ransomware attacks observed in our data, with enhanced cybersecurity measures likely playing a significant role. As our statistics show, more ransomware incidents are now discovered in time, before damage is done. A less savory possibility is that, as cybercriminals pivot toward easier targets with fewer defensive capabilities, they tend to attack smaller organizations, which may be more likely to “pay and move on,” and thus are not represented in industry statistics.

Another reason may be that, despite political differences between the U.S. and the EU, there has been a successful international collaboration to capitalize on the fact that even if cybercriminals are often located outside the West, their IT infrastructure is often located in Europe or the U.S. By analyzing the criminals’ activities and identifying their servers, police can seize and disrupt the criminal infrastructure. Maintaining this collaboration is vital in combating cybercrime.

This year, several large ransomware-as-a-service (RaaS) groups and cybercriminal forums had their infrastructure seized by law enforcement. The continuation of this positive trend has disrupted activities by groups such as LockBit, Black Cat, and RansomHub, thereby fragmenting parts of the ransomware ecosystem.

Truesec has seen more ransomware incidents that appear to have been conducted by small independent actors, either lone individuals or small teams, not connected to any of the large ransomware syndicates. Overall, this is still positive, as cybercriminals are almost always more effective when they organize and collaborate. At the same time, the cyber extortion ecosystem is resilient. Cybercriminals continue to trade information and services on various dark web forums. Newer RaaS brands, such as Qilin and DragonForce, have replaced older ones.

To truly impact cybercrime, cybercriminals must be arrested and sentenced, yet most still operate from countries that do not attempt to stop them. The conflict between Europe and Russia leaves little leverage for European nations to pressure Russia to act against cybercriminals, as the diplomatic arsenal is already almost exhausted.

Europe’s diminishing influence in Africa could also lead to fewer opportunities for collaboration with local police. In 2024, over 1,000 cybercriminals and fraudsters were arrested in a joint INTERPOL and AFRIPOL operation. None of them came from a country where Russia supports the regime with mercenaries. If Europe’s influence in Africa further deteriorates, there will likely be less collaboration to apprehend cybercriminals in the future. In our chapter, "The Complexity of Large Multinational Organizations," we look at how cybersecurity is affected by global threats.

The geopolitical situation always limits what can be achieved through international law enforcement. If European law enforcement is too successful in denying criminals access to inexpensive server capacity in Europe, they will likely relocate to other parts of the world, even if it is more expensive.

### Cybercrime & Other Crime
Another trend is the fading of the boundaries between cyberspace and the physical world. Russian and Chinese intelligence agencies combine human intelligence gathering with cyber espionage. In Latin America, organized cybercrime is directly affiliated with drug cartels. Cybercriminals from Mexico steal personal information on government officials, hoping to find extortion material that can be used to protect the cartels.

An example of how physical threats and extortion have been used in conjunction with cyberattacks is a U.S. case in which an unknown cybercriminal hacked an individual’s email account and identified their cryptocurrency assets. The threat actor then collaborated with a gang of criminals to stage a home invasion and, at gunpoint, forced the victim to transfer their cryptocurrency assets to an account under the cybercriminal’s control.

In Sweden, Truesec has seen what we assess to be nation-state intelligence services using local criminals to target senior executives to get them to give up their organizations’ support to Ukraine. It is possible that prior surveillance and intelligence gathering on these individuals was done through cyber-enabled means. Criminals for such actions are recruited through online forums and encrypted apps. A tactic that is also used by non-state aligned criminals to recruit children and young adults to carry out violence on behalf of organized crime, highlighting the link to cyberspace and the disintegration of national borders. Actions in the cyber domain enable crime and terrorism in the physical domain.

Even if it’s still relatively uncommon that cyberattacks are seen in combination with physical violence, communities like the online collective known as “The Com” have members that conduct cybercrime, but also members that offer swatting-as-a-service[^2] and violence-as-a-service. However, the overwhelming majority of the violence-as-a-service offerings found on the darknet today are likely still fraudsters. While this is the case, we do see an increase in the solicitation of criminals through online forums and encrypted apps to carry out violence on behalf of malicious organizations.

[^2]: Threat actors coordinate fake emergency calls by spoofing phone numbers and using compromised smart devices to make the fake emergency seem to come from the victim's home, enhancing credibility with 911 dispatchers. The goal is to draw heavy police response (SWAT teams) to the location, creating chaos, and to distract law enforcement while committing other crimes, like crypto theft.

### Threat Actors & Their Motivations
In the cybersecurity landscape, the term threat actor encompasses a diverse array of individuals and groups. These range from nation-state operatives and organized cybercriminals to hacktivists and insider threats. These actors don’t operate in neat, isolated categories; instead, their techniques, tactics, and procedures frequently overlap, creating a complex and often confusing environment for defenders. The boundaries between different threat actor types are increasingly blurred as tools and methods are shared, sold, or copied across the underground ecosystem. This makes clear-cut attribution challenging. What matters most today is understanding how threat actors operate, what motivates them and how current events shape their actions, but most importantly, how these actions impact organizations. By focusing on behaviors and intent, defenders can better anticipate and respond to the evolving threat landscape, regardless of who is behind the keyboard.

### Observations From Truesec
Most of the incidents Truesec has handled have been carried out by cybercriminals motivated by financial gain. Cybercriminals use extortion or fraud to obtain money from victims or to gain access to sell it to other criminals.

By measuring the number of intrusion attempts averted in Truesec SOC each month and normalizing it to the total number of endpoints protected, a rough estimate of the cyber threats can be obtained. This data shows that the number of attempted cyberattacks is increasing steadily.

There are just as many serious cyberattacks as last year, but with better detection, fewer have escalated to the worst outcomes. In our last Annual Report, we noted a decline in the number of serious ransomware incidents targeting large enterprises in the Nordics, as cybercriminals shifted their focus to smaller organizations. In our Truesec data, we see that this trend in ransomware continued in 2025. The total number of ransomware incidents in which a threat actor successfully encrypted and extorted victims has decreased. In contrast, we observed a corresponding increase in incidents in which the threat actor was kicked out of the environment before reaching their final objective.

It appears that more organizations now have better visibility into their environments and can request assistance earlier in the kill chain to avert serious cyberattacks, such as ransomware, reducing their impact. This highlights the importance of proper detection and response capabilities.

### Focus Areas
![Image description]

### The Constant Evolution Of Social Engineering
In 2025, Truesec assisted a company that experienced a serious cyber-extortion incident that began not with a phishing email but with hundreds of seemingly pointless spam emails. Social engineering takes many forms, and threat actors continually devise new tactics to exploit the human mind to achieve their objectives.

This time, the access method was a relatively new technique known as “BazarCall,” also referred to as “callback phishing.” It’s particularly challenging as it requires no breach or system access to initiate; the only thing the attackers need is your email address.

The threat actor known as “Silent Ransom” began by identifying valid email addresses of several employees at their chosen targets. We don’t know exactly how, but finding valid corporate email addresses is easily done using open source intelligence (OSINT) techniques, which sometimes is as simple as checking the company's website or social media. Their next step was to register email addresses for numerous subscriptions to various newsletters, websites, and other services eager to expand their mailing lists. This resulted in hundreds of emails flooding the victims’ inboxes, causing them significant stress as they were caught completely off guard.

What was once a manageable stream of messages became an overwhelming deluge, turning routine communication into chaos. This tactic not only disrupts productivity but also significantly increases the difficulty of locating legitimate, important, and time-sensitive emails. This creates a twofold effect: first, it reduces the likelihood that the user will notice legitimate assistance from IT or security teams, while simultaneously generating a sense of urgency to resolve the issue. At this point, the threat actor stepped in, positioning themselves as the solution to the problem they had created.

### Threats From Within
Truesec was called in to assist with a serious IT incident. The victim, a medium-sized enterprise, had received no warning when parts of its IT environment suddenly stopped responding. No encrypted files, ransom note, or any other clue as to what had happened or who was behind it.

Initially, Truesec treated this as a potential active external threat. It was apparent someone had purposefully disabled functions and deleted critical data. However, as the investigation progressed, forensic analysis revealed facts that seemed inconsistent with this assumption. The available logs indicated that the threat actor’s activity originated from an IP address identified as a Tor (The Onion Router) exit node. There was, however, no indication of which account was used at the time. The threat actor also appeared to possess detailed knowledge of both the infrastructure and its security controls. Leveraging this insight, they disabled key security features within the cloud infrastructure platform.

With defenses neutralized, they carried out destructive actions, including the complete deletion of critical resources and systems, causing severe operational disruption. After disabling security features and deleting resources, systems, and data, the threat actor proceeded to target backups, snapshots, and other copies of the systems. These were also erased, significantly limiting recovery options and maximizing impact.

Given the context, it may not be surprising to learn that the threat actor was in fact a disgruntled employee, just days away from leaving the company. This individual attempted to conceal the sabotage by using anonymization services, shared accounts, and various other obfuscation methods. Fortunately, these efforts were not enough to erase all traces. Forensic analysis ultimately revealed the perpetrator’s identity, allowing intervention to halt further damage.

### When The Threat Doesn’t Go Away
![Image description]

### The Complexity Of Large And Multinational Organizations
![Image description]

### Password Attacks Are Still Relevant
![Image description]

### Malicious Packages Pose Software Supply Chain Risk
![Image description]

### Deep Dive: The Malicious PDF Editor
![Image description]

### The Use Of AI In Cyberattacks
![Image description]

### The Challenge Of Knowing When "The Regular" Becomes A Threat
![Image description]

### Not Taking The Regular For Granted
![Image description]

### Hybrid Warfare
![Image description]

### Outlook 2026
![Image description]

---

ed. Employees who
attempt to elevate privileges or
access resources or data beyond
their assigned role should raise
concerns. Clear incident response
procedures should be in place for
suspected insider threats, where
collaboration across departments
is planned and trained to identify
and respond quickly and efficiently.
Threat Intelligence Report 2026 37

When the Threat Doesn’t Go Away
The Eternal Victim
In 2025, Truesec responded to The question was referred to
a severe ransomware attack. the victim organization, which
reluctantly reported that this
One of the first steps was to was the fifth time it had been
conduct a forensic investigation encrypted this year alone, and that
to determine whether any data each time, its service provider had
could be recovered, identify how responded by simply restoring the
the threat actor gained access, environment from backups to a
and determine an appropriate state before encryption.
course of action for recovery and
restoration. The service provider had not
considered that their restoration
The forensic analysis indicated would not fix the vulnerability
that the threat actor likely had that had let the first ransomware
gained access through com- actor in, which was presumably
promised VPN credentials. still open to new threat actors.
However, additional anomalies Each successive ransomware
were detected. The investigation attack also meant that a new data
identified artifacts from what dump from the network had been
appeared to be older incidents. stolen, likely containing additional
Eventually, it reached a point at information that could be used to
which files were found that had compromise them again.
been encrypted by a different
encryptor, belonging to a comp- Further analysis revealed that
letely different ransomware actor. some of these attacks may have
been carried out by the same
As the forensic analysis continued, threat actor, who used different
the traces continued to point brands in separate attacks,
further and further back in time, possibly a RaaS affiliate using
seemingly to no end. Eventually, it different brands in multiple
reached a point at which files were attacks. Other artifacts clearly
found that had been encrypted belonged to different groups
by a third encryptor, and by a altogether, using different methods
completely different ransomware to take over the environment.
actor than in the previous two
cases. At this stage, the question Once attackers know how to
had to be asked: What had really breach your environment, they can
happened here? Why do traces of exploit that weakness repeatedly
at least three different encryptors, unless you take proactive steps
each linked to separate ransom- to ensure you understand how to
ware groups, appear within a few prevent future incidents.
months of each other?
438 Threat Intelligence Report 2026

Threat Intelligence Report 2026 39

The Challenging Cycle These are sometimes overlooked
of Re-Victimization when applying enterprise
policies such as multi-factor
A cyberattack rarely ends with the authentication (MFA). Once
ransom note or the restoration of exfiltrated, attackers can crack
encrypted files. While the victim them offline using readily
organization scrambles to contain available tools, chain them
the damage, communicate with other stolen data, and
with stakeholders, and meet impersonate legitimate users
immediate regulatory deadlines, months later, long after the initial
the cybercriminal is already busy incident has faded from the
trying to monetize the breach headlines.
further.
This data-hoarding behavior
Regardless of whether the victim represents a strategic evolution
pays the ransom, cyber extortion in cybercrime. Stolen data from
groups will attempt to remonetize a breach can be remonetized
the stolen data; every log file, by leveraging it in new extortion
configuration setting, temporary schemes, breaches, or cyber
cache, browser history, saved fraud. Data lost in a single breach
credential, session cookie, autofill can fuel future cyberattacks.
entry, and even browser extension
data. This is not opportunistic During the reconnaissance
theft; it is deliberate information phase of an intrusion, attackers
gathering. methodically build a living map
of the victim’s digital and, more
Consider a single user’s browser commonly, human ecosystem.
profile. Browsers such as Chrome, They catalog the IT environment,
Edge, or Firefox store far more including Active Directory
than browsing history. They retain structures, firewall rules, VPN
saved passwords (often weakly configurations, and cloud tenancy
encrypted with OS-level keys), details. They trace network archi-
autofill data (names, addresses, tecture, documenting internal
payment details), session IP ranges, subnet layouts, jump
cookies (allowing instant re- hosts, and lateral movement
authentication to cloud services), pathways.
and OAuth tokens (granting
persistent access to SaaS plat- Information gathered during
forms). A mid-level manager’s reconnaissance may also
local profile might contain 50+ persist after a failed cyberattack.
credentials: internal VPN portals, Scavenger criminals will harvest
AWS consoles, Slack workspaces, data from failed extortion
GitHub repositories, and even attempts and repost them as
personal accounts used for work- new attacks, further damaging
related tasks. the victim’s brand.
440 Threat Intelligence Report 2026

Log sellers are a relatively new
type of cybercriminal that often
represent the final stage in the life
cycle of a data breach. Log sellers
hoard stolen data from hundreds
of successful and failed data
extortion attempts. They structure
and enrich data in databases,
then profit by selling access
to criminals who can exploit
it for purposes ranging from
launching ransomware attacks
to committing fraud and scams.
Even state-sponsored actors
purchase intelligence from these
log sellers.
Attackers may also view victims
who have been successfully
attacked before as easy targets
for future attacks, since they may
not have had time or resources
to fully recover or update their
security.
Stolen data from previous attacks,
obtained from log sellers, can give
attackers a significant advantage.
They can gain intimate knowledge
of the target environment. A
forgotten service account found
in a stolen config file can easily
become the next entry vector.
Phishing emails now reference
real internal project codenames,
upcoming board meetings,
or personal details lifted from
browser history. A stolen session
cookie can grant temporary
admin access before MFA
reasserts. Even a single dormant
credential, such as a VPN account
with SMS-based MFA that rotates
infrequently, can be reactivated.
Threat Intelligence Report 2026 41

From Victim to Resilient Target
How do you protect yourself Many of these suggested
from someone who has stolen solutions can be challenging to
your data and is now using it to implement because they often
ransom you, attack you again, or affect the entire organization.
sell it to the highest bidder? There However, it is possible to do this
is no perfect solution, but there in steps: start with the simpler
are many things you can do. variants, protect the most
sensitive data, and then expand
At its core, data is what threat from there.
actors primarily seek, regardless
of its form. That means you can But what can you do when the
work with various data-handling unfortunate happens? When
methods. Avoid collecting and data has been stolen or has
storing data that you do not need. inadvertently ended up in the
Archive or delete anything that wrong hands. Here is where it gets
has lost its value, necessity, or difficult, as there is no perfect
importance to you; it may still be solution.
highly sensitive and valuable to
someone else.
There is ample evidence that
paying criminals’ ransom
Understanding where your data
demands does not guarantee
resides, what is sensitive, who and
your troubles are over or that
what can access it, and how you
your data is safe. Criminals
know when unauthorized access
will always find new ways to
has occurred, also remains
monetize your stolen data.
crucial. Furthermore, modern
However, there are some steps
data classification tools strike a
you can take to limit the impact.
good balance between security
and usability, making them
highly viable options for further
Evaluate your monitoring
protection of your data.
capabilities of the dark web as
well as public sources. If your
Ideally, you want to design your
data is out there, accessible or
infrastructure with data sensitivity
readable, you at the very least
in mind, so that the most sensitive
want to know where and what.
data is protected not just by a
This allows you to better assess
single software application, but by
the damage, risk, or potential
layered security features across
threats its exposure may pose.
multiple levels.
42 Threat Intelligence Report 2026

From Victim to Resilient Target
When data resides in a location or
platform of relevant legitimacy or
reputability, a takedown request
may be possible. Some platforms
offer removal or other measures
when stolen data is published or
shared through their solutions.
Reporting to authorities can
sometimes lead to actions being
taken that may better protect your
organization.
Assume Breach is not a new
strategy, and the goal today is not
to prevent every single breach,
because that is virtually impossible.
Instead, ensure that even when the
attacker holds the blueprint, your
house remains unlivable for them.
By assuming compromise,
eliminating trust, and building
intelligence-aware defenses,
organizations have a better
chance of breaking the cycle
of re-victimization.
Threat Intelligence Report 2026 43

The Complexity of
Large and Multinational
Organizations
The Chain Is Never Stronger
Than the Weakest Link
Throughout the year, Truesec
has handled several incidents in
which threat actors have followed
patterns like those described in
this section; however, the following
example is an amalgamation of
several actual incidents.
A ransomware attack hit a
European enterprise with an inter-
national presence. The corporate
IT was fully encrypted, the business
was at a standstill, and money was
bleeding out.
During the forensic investigation of
the incident, Truesec discovered
that the threat actor established
a foothold via a firewall serving
a subsidiary in Asia. The local IT
admins reported that MFA was
too slow in the remote area, so
they enabled local accounts
on the firewall without MFA to
circumvent the problem. As these
accounts were intended only for
short-term troubleshooting, they
had generic names and default
passwords. This enabled the threat
actor to immediately guess the
valid credentials, which were the
default credentials for the specific
firewall, and in turn, access the
environment.
This gave the threat actor an
initial foothold in the environment,
enabling them to execute tools
from their own machines via the
VPN solution and target systems
44 Threat Intelligence Report 2026

within the IT environment. They on their own machine through the
began scanning the environment VPN connection.
to understand what was present,
using a combination of network This second server was part of
scans and Domain Name a Microsoft Hyper-V cluster that
System (DNS) requests. The DNS hosted virtual machines serving
requests were used to identify the the entire global business. In
Microsoft Active Directory domain quick succession, the threat actor
controllers. The network scans copied malware files from the VPN
revealed which systems had a to the Hyper-V server. From there,
remote management port and, they copied the same file to all the
in some cases, were accepting virtual machines in the cluster and
credentials obtained by the threat executed it on them. This malware
actor. file was the encryptor that
rendered the data on all virtual
After this initial discovery and machines completely unreadable,
reconnaissance, the threat actor bringing the entire IT environment
transferred a vulnerable driver to a grinding halt. This was also
to one machine that they could the first time the threat actor had
access. This driver exhibited introduced malware onto the
behavior that could enable the compromised environment, aside
remote extraction of Microsoft from the initial failed attempt with
Windows registry files. However, the vulnerable driver.
when the threat actor attempted
to execute it, the installed EDR
agent detected and blocked the
activity. Upon realizing that their
initial attempts had failed, the
threat actor disconnected the VPN
session to avoid further detection.
Around 24 hours later, the threat
actor reconnected by starting a
new VPN session. They conducted
lateral movement from the VPN
to a server via Remote Desktop
Protocol (RDP). The threat
actor then obtained additional
credentials from other users who
had visited the servers. Shortly
after, the threat actor moved to
another server, again using RDP.
Throughout the period leading up
to that point, the threat actor did
not download any hacking tools on
the victim’s machine. Instead, the
threat actor ran the hacking tools
Threat Intelligence Report 2026 45

The Challenge That Comes
With a Global Presence
In our modern globalized world, you’re in a back office in Asia,
companies have offices and working for minimum wage, not
teams working across the globe, really knowing the board, the
all connected through their brand, or the company history, in a
corporate network. VPN solutions country you’ve never visited.
and interactive log on capabilities,
such as RDP, help employees feel Maintaining cybersecurity and
like they can access everything protecting valuable intellectual
seamlessly, no matter where they property in a global enterprise
are in the world. requires careful network
segmentation, with roles and
In a typical open corporate privileges assigned as securely
network, adversaries need as possible so that a breach at a
only to find one vulnerability, weak point doesn’t compromise
one misconfigured server, one the entire environment.
careless employee, or one
unpatched system in one single
office anywhere in the sprawling
global network. At the same time,
defenders must maintain flawless
protection everywhere, at all
times, across every culture, every
jurisdiction, and every time zone.
It’s not necessarily fair, but
the reality of cybersecurity in
the multinational enterprise is
complex. The attack surface
expands when the network spans
the world. Vital IT operations may
be outsourced to regions chosen
for low labor costs rather than
good security practices. Global
supply chains may require a
presence in high-risk countries
where government surveillance is
endemic.
Company culture is one thing
when you are in the same office
as the CEO in Europe, but it is
something entirely different when
46 Threat Intelligence Report 2026

Using Technical Controls
To Prevent Global Attacks
When large multinational Proper network segmentation
organizations have their enforces access based on
entire global environment necessity. Karen from Accounting
compromised, the primary needs access to her finance and
reason the threat actor can move business applications, not to the
throughout the network is a lack management ports of the servers
of proper network segmentation: themselves. Similarly, John from
once connected, the threat reception at the Sweden office
actor has access to the entire only needs access to the local
internal network. More often access control system, not to the
than not, organizations provide RDP port on the file server in the
network access when a lower U.S. office.
level of access would suffice.
For example, information/data If segregation is not in place, a
access or application access. This threat actor can move from a
can be achieved without granting server to an infrastructure server.
the person network access by The infrastructure servers, core
using solutions such as cloud networks, and storage networks
storage (e.g., Microsoft OneDrive constitute the “fabric” on which the
or application gateways). whole organization’s IT systems
are built and operate. As such, this
It is neither necessary nor is the most critical component of
advisable to allow access to all the organization’s technologies.
assets once a user is logged in. If a threat actor gains access
Users need access only to the to this fabric, the potential for
systems relevant to their tasks, catastrophic damage is high.
usually only a handful of the
hundreds of systems available Truesec recommends using
to the organization. Connecting tiering4 to enforce proper
to a server via RDP from a VPN or segregation, and the most logical
from any user workstation is often place to start is the fabric. From a
unnecessary. Instead, a user’s network standpoint, this means
daily access typically requires refusing all connections to any
only a few services, such as management port of the fabric
Kerberos or SMB. systems except for dedicated
privileged access workstations
(PAW)5.
4. Read more: www.truesec.com/security/active-directory-tiering
5. A Privileged Access Workstation (PAW) is a hardened,
dedicated computer, physical or virtual, used exclusively for
performing administrative tasks on critical systems. It's a key
security control designed to protect high-value accounts and
systems from compromise.
Threat Intelligence Report 2026 47

Password Attacks
Are Still Relevant
More than a third of the
ransomware incidents handled
by Truesec in 2025 began with
attackers using valid usernames
and passwords to access
exposed VPN gateways or
terminal servers.
The Challenge of
Preventing Attackers from The passwords in these dumps
Logging In may be either in plain text or
hashed. In the former case, they
Almost 14 percent of valid are available in clear text and can
credentials used in ransomware be immediately exploited. Even
attacks handled by Truesec CSIRT when passwords are stored in
in 2025 were obtained through a hashed form, they can still be
password spraying. For the rest, cracked, leaving attackers with the
it’s largely unknown how the actual credentials to log in.
credentials were compromised.
While phishing remains a well- Truesec has observed several
known method for stealing different methods used to gain
credentials, it is far from the only valid credentials.
one. There is a great deal of
information-stealing malware One type of attack exploits
available for purchase on password reuse across multiple
criminal dark websites. Previous platforms. With the explosion of
data breaches can also lead to online services mentioned above,
credential leaks. The explosion of this is highly relevant. Imagine
online services that use credentials an employee who uses the
for login, combined with frequent same password for both a cloud
data breaches, has provided service and the company’s VPN.
threat actors with vast lists, called If the cloud service suffers a data
dumps, of potential usernames breach and user credentials are
and, sometimes, passwords to leaked, a threat actor can obtain
leverage against organizations. that data, identify the employee’s
email and password, and simply
Often, the usernames in these try those same credentials on the
dumps are email addresses linked corporate VPN. If they work, the
to specific companies, making the attacker gains access, and voilà,
potential victims easy to target. classic credential stuffing in action.
448 Threat Intelligence Report 2026

A step beyond password reuse is
when threat actors do not have the
exact password for an account but
instead possess lists of potential
usernames and passwords. This
enables the notorious password-
spraying attack, in which
attackers systematically test these
combinations against exposed
systems, in the hope of finding a
match. This is especially effective
against organizations that set a
default password at either account
creation or when a password reset
is requested.
Large botnets available for hire on
the darknet are commonly used
for DDoS attacks but also for large,
distributed password-spraying
attacks. By distributing password-
spraying attempts against
hundreds of accounts among tens
of thousands of bots, it’s easier to
avoid triggering warnings.
If a password-spraying attempt
fails or no password list is available,
threat actors will generate their
own list of password candidates.
This list can be quite extensive,
often containing the name of the
company and variations, and
the list of the top 10 most used
passwords in 20256 and even the
list of the top 500 worst passwords7.
Truesec responded to an incident in
2025 in which the threat actor tried
more than 10,000 combinations of
usernames and passwords before
finding a valid pair.
6. Read More: www.passwordmanager.com/most-common-
passwords-latest-statistics
7. Read More: weakpass.com/wordlists/500_worst_passwords.txt
Threat Intelligence Report 2026 459

A Multi-Pronged Approach of
Prevention, Detection, & Response
When it comes to defending against When it comes to resilience, MFA
password attacks, MFA remains the methods that use separate hardware
most effective countermeasure. The storage are much more resistant to
concept of MFA is straightforward. In attacks. Also, MFA techniques based
addition to a password, the account on public key infrastructure (PKI)
has one or more additional forms or FIDO2 are very robust against
of verification. These factors are sophisticated phishing attacks due to
what you have, what you know, and their cryptographic binding8.
what you are. It can include a client
certificate, a token generating one- MFA protects against password
time passwords, or an application attacks, but threat actors are creative
that requires manual approval, to and have found ways to bypass MFA.
name a few. Often, authentication Two standard techniques used are
relies on a password and one MFA fatigue and the Adversary-in-
additional factor, so-called two-factor the-Middle (AiTM) technique. MFA
authentication (2FA), but nothing fatigue leverages push notifications.
prevents the use of more than two The threat actor, knowing the correct
factors. password for an account, submits
hundreds of requests to the system,
In an MFA scenario, a threat actor with which results in an equal number of
a valid username and password is approval requests sent to the user.
hindered by the remaining additional The attack succeeds because the
factor. Note that our use of “hinder” victim usually gets tired of the flood of
and not “prevent” is intentional. MFA is incoming requests and accepts it just
not bulletproof, and it comes with its to end the annoyance. In AiTM, the
own challenges. threat actor is intercepting the user’s
login session by using a proxy server
To begin with, deploying MFA to position themselves between the
organization-wide is difficult because user and the legitimate login page,
MFA solutions that cover all network stealing the credentials and the one-
assets are rare. In addition, it is time MFA code.
unfortunately common to use less
effective MFA methods. For example, Threat actors may also call the help
SMS-based MFA is considered one desk and use social engineering
of the least secure options due to its to request a password reset while
vulnerability to various attacks that deactivating MFA. They then usually
may expose the one-time code to call the help desk, posing as an
threat actors. employee with a lost or stolen
phone, who lacks MFA access and
8. Microsoft Word - IAM Group 2 MFA SSO Challenges FINAL
450 Threat Intelligence Report 2026

A Multi-Pronged Approach of
Prevention, Detection, & Response
needs help regaining control of their and when it comes to security, “just
account. Threat actors who conduct one time” can be enough to sink a
these types of social engineering company.10 It is thus paramount to
attacks are usually highly skilled, have detect the signs of a potential attack,
done their homework on the target whether successful or not, early
company and its employees, and are enough, and with as many details as
therefore highly convincing, making possible to enable a timely, adequate
them extremely difficult to detect for response. Monitoring login failures,
untrained individuals.9 This is not a their sources, and subsequent
technical attack; it falls under social successful authentications often
engineering, which we cover in our yields valuable insights into
chapter, "The Constant Evolution of adversaries attempting to gain
Social Engineering." network access.
Knowing what the threat actors know There, it pays to be discerning in
helps you act on what matters. In the observations. Authentication
the age of infostealers and ongoing attempts against well-known or
data breaches, it is essential to generic account names are now
identify leaked credentials quickly. almost inevitable and often just
An effective way to do this is to background noise11. However, as soon
use a service that scans the dark as the attempted authentication
web for leaked credentials. Such matches a valid username in the
services can provide alerts whenever organization, an alert must be
leaked credentials matching their triggered.
domains are discovered, which
enables preventive actions such as As the adage goes, “detection without
resetting passwords, implementing response is meaningless”. Readiness
additional monitoring, or imposing and response playbooks make a
restrictions, for example, Conditional huge difference. Whether it is the help
Access, on affected accounts. desk, IT, or the SOC, teams must be
Quick interventions are vital in these equipped to reset multiple passwords
scenarios, as a threat actor who has swiftly, block compromised users
logged in with valid credentials can from authenticating externally, and
be extremely difficult to detect. revoke access to cloud platforms
instantly. Preparing and rehearsing
While prevention and proactivity go these measures will make all the
a long way, there will always be that difference when every second counts.
one time when, despite all measures
taken, the threat actor can get in,
9. Scattered Spider | CISA
Threat Intelligence Report 2026 10. Ransomware: from incident to bankruptcy - PONT Data&Privacy 51
11. This is also a good reason to not to leave default accounts on exposed systems.

Malicious Packages Pose incorporated self-propagating
Software Supply Chain Risk mechanisms that enabled
automated spread across the
Throughout the year, we have seen ecosystem.
a range of breaches targeting the
development chain or parts thereof. While we have seen these types
In late August 2025, reports emerged of breaches for several years, they
of malicious versions of several Nx have transitioned from a specific
packages being published to npm, type of focus, commonly crypto
the world’s largest software registry. wallets, to a broader and more
This campaign, dubbed S1ingularity, impactful approach. Threat actors
involved code designed to exfiltrate now commonly deploy various
sensitive data such as credentials types of information stealers and
and crypto wallets and upload similar malicious code, which can
it to attacker-controlled GitHub significantly impact both individuals
repositories. and the organizations they belong to.
Shortly thereafter, a second major The fundamental risk in these attacks
incident, referred to as “Shai-Hulud”, stems from the profile of impacted
compromised more than 500 npm users and devices. Those most likely
packages. The malicious code once to download and integrate third-
again focused on several types of party packages are typically highly
credential theft but also included privileged users, such as developers
worm-like behavior, spreading or system administrators, often
rapidly by injecting malicious code possessing broad access across
into additional packages and organizational environments. These
publishing compromised versions to accounts typically operate with
registries. elevated permissions and store
sensitive assets, including API keys,
In October, we saw a different, albeit SSH credentials, and access tokens,
similar type of supply chain attack. on their local systems.
The Open VSX registry, which serves
extensions for Visual Studio Code, When such accounts are
was targeted by Glassworm, a self- compromised, the supply chain
propagating VSCode extension effect intensifies, as stolen
worm. Several Open VSX extensions credentials can enable lateral
were compromised to include code movement into critical infrastructure
that aimed to steal credentials, drain components, such as deployment
cryptocurrency wallets, and even pipelines, CI/CD servers, and source
establish command-and-control code repositories. This creates
(C2) channels. Later, malicious a cascading impact, allowing
extensions in the official Visual attackers to infiltrate multiple layers
Studio Code repository were found. of the ecosystem and potentially
Like “Shai-Hulud”, this campaign compromise entire development
environments. Notably, malicious
452 Threat Intelligence Report 2026

packages may reach CI/CD servers exceed what an in-house team
directly if, for example, they are used for a closed-source project might
in the build process. If that happens, achieve. However, this advantage is
other types of credentials that may inconsistent and depends heavily
not be present on developer devices on contributor engagement and
could be compromised if used as expertise.
part of the build process.
Closed-source software is not
immune to these issues, but
organizations typically enforce
structured review processes,
including procurement checks,
security assessments (often
rudimentary and secondary
priorities), and testing phases before
deployment. In contrast, open source
components are often downloaded
and executed within minutes of
discovery, significantly increasing
the risk of introducing unverified
code into production environments.
The boundaries between open and
closed-source software can also
be blurred, as many closed-source
projects depend on open source
components.
Both open source and closed-
source software face similar security The widespread lack of maturity
challenges, but the underlying in secure development practices
dynamics differ. Open source remains a critical issue. When this
projects often lack dedicated is combined with the absence of
security budgets and resources, structured processes for managing
leaving critical packages and widely third-party software and the use
used repositories without formal of highly privileged devices, the
requirements or rigorous security risk profile escalates dramatically.
vetting. This raises questions about Conditions like this create an
how vulnerabilities are addressed environment where vulnerabilities,
and security measures implemented malware, or generally insecure
when funding and focus are limited. components can propagate
unchecked, and compromise can
Conversely, open source code lead to deep, systemic breaches
benefits from community-driven across development and production
scrutiny, which can sometimes ecosystems.
Threat Intelligence Report 2026 53

Revisiting Core Security Concepts
in a World of Rapid Development
Software developers are now a development lifecycle, regularly
significant target for threat actors. reviewing which packages are
There is no single, simple solution used, and removing those that
to reduce these threats. It is essential are no longer needed is crucial
to revisit foundational security for maintaining a clear inventory
principles such as least privilege and of dependencies across your
administrative isolation. codebase.
The combination of You need to continuously
local administrative privileges and identify risks, monitor for vulnera-
access to various build solutions, git bilities, find deprecated packages,
repositories, cloud environments, and notice unauthorized changes
CI/CD pipelines, APIs, and even across your codebase. In most cases,
infrastructure directly in a DevOps effective tooling or processes to
environment creates a broad attack support this are also needed.
surface.
Despite our best efforts, malicious
Ideally, the area where developers code can still be introduced.
build and test new software solutions Some vulnerabilities only
should be separated from the become apparent after exploitation.
production environment, so that Protecting your software pipelines,
only safe, vetted code is introduced much like defending against zero-day
into a production environment with vulnerabilities, is challenging at best.
separation at the AD level. Reality, of
course, is far more complex, and this Having comprehensive asset
concept would only address some of management that can identify not
the issues. only the affected package but also the
exact version, download timestamp,
Even with careful separation between and whether it was executed will also
development, test, and production significantly reduce the time it takes to
builds, each build typically contains identify and respond if some part of the
code packages that, in turn, include code has been compromised.
many dependencies, often patched
at varying frequencies. Each patch One key factor in minimizing the risk
may introduce malicious updates of introducing malicious code into
or inadvertent vulnerabilities in the projects is to delay immediate adoption
carefully vetted production build. of newly released packages. While this
approach may seem counterintuitive,
This is where asset management given the common practice of rapid
comes into place. Expanding updates to patch security flaws, it can
this to the software be prudent in environments where new
releases have not undergone stringent
security vetting.
454 Threat Intelligence Report 2026

Revisiting Core Security Concepts
in a World of Rapid Development
Allowing a short delay gives the community
or vendors time to identify and remediate
potential vulnerabilities before deployment,
reducing the likelihood of introducing
compromised code into production.
There are, of course, exceptions when a
particularly severe known vulnerability is
actively exploited by attackers, even if the
patch is intended to address it.
Minimizing the impact of supply chain
breaches requires a layered approach that
addresses vulnerabilities before they are
exploited and ensures rapid containment
when incidents occur. General advice
on securing your environment, including
detection and response capabilities, applies
here in particular. An EDR agent generally
will not detect flaws in a malicious code
package unless it is already known to be
bad, but it can react during execution if it
introduces a backdoor or conducts other
malicious activity.
For more detailed help in securing your
software supply chain, please visit the
Truesec blog post by scanning the QR code.
Npm Supply chain
Attacks: How to
Reduce Risk
55

56 Threat Intelligence Report 2026

Deep Dive:
The Malicious PDF Editor
Threat Intelligence Report 2026 57

In June 2025, a series of Google It then makes an HTTP GET request
Ads campaigns began promoting to indicate that the installation
the PDF Editor by AppSuite. Truesec process has been started. This
has identified at least five distinct is sent to the URL: hxxp[://]inst[.]
Google campaign IDs, suggesting productivity-tools[.]ai/status/Install
a widespread campaign primarily Start?v=1[.]0[.]28[.]0&p=PDFEditor&c
targeting Europe. The ads pointed ode=EN-US
to several websites that appeared
to be AI-generated and hosted The next step is that an executable
the PDF editor. The PDF Editor file file is downloaded from: hxxp[://]
was heavily obfuscated, and many vault[.]appsuites[.]ai/AppSuites-
independent researchers agreed PDF-1[.]0[.]28[.]exe. This is a binary
that the malicious code appeared that turns into the actual malware.
to be generated by AI/LLMs. The
file installed, PDF Editor.exe had the After successful installation, it
following properties: makes two additional GET
requests to confirm that all is set.
Filename: PDF Editor.exe
hxxp[://]inst[.]productivity-
MD5: 6fd6c053f8fcf345efaa04f16a- tools[.]ai/status/Download%20
c0bffe Complete?v=1[.]0[.]28[.]0&p-
=PDFEditor&code=
SHA1: 2ecd25269173890e04fe00ea-
23a585e4f0a206ad hxxp[://]inst[.]productivity-
tools[.]ai/status/
SHA256: cb15e1ec1a472631c53378d- InstallDownloadComplete?v=1-
54f2043ba57586e3a28329c9dbf40c [.]0[.]28[.]0&p=PDFEditor&code
b69d7c10d2c
When the user executes
the installation file, a
EULA is first prompted:
58 Threat Intelligence Report 2026

During the setup process, a The –cm have the following
registry key is also added for different arguments.
persistence, which is executed
on startup. It contains a --cm --install
argument that gives executable
instructions on how to behave. --enableupdate
Internet records suggest that --disableupdate
this campaign began on June
26, 2025, when many of the --fullupdate
sites linked to it were either first
registered or first known to have --partialupdate
promoted the AppSuite PDF
Editor. However, the PDF editor
--backupupdate
was first submitted to Virustotal
on May 15.
--check
--ping
--reboot
Threat Intelligence Report 2026 59

When initialized, Tamperedchef starts to query the web
browser’s database using DPAPI.
Upon startup, it begins querying Data traffic to sites that distribute
the system for different security the AppSuite PDF Editor includes
products. Then it terminates referrers from Google Ads
different browsers, likely to access campaign codes, suggesting
data within them, which is locked if
running.
60 Threat Intelligence Report 2026

that the threat actor behind These new companies, in turn, also
this campaign used Google had code signing certificates that
advertising to promote this PDF pointed to other malicious apps.
editor. The duration from the start So, the threat actor behind the
of the campaign to the malicious malicious PDF editor appears to
update was also 56 days, close have a plethora of malicious apps
to the 60-day length of a typical created with the aid of an LLM,
Google advertising campaign, along with an infrastructure of fake
suggesting the threat actor let shell companies and websites to
the ad campaign run its course, distribute them.
maximizing downloads, before
activating the malicious features. An interesting fact is that the
traces of this threat actor go back
The threat actor has used multiple several years to an old malicious
versions of the AppSuite PDF Editor browser extension released under
app, each signed with certificates the name “Blaze Media”. The
issued by at least four different threat actor had expanded their
companies. The companies are: operations considerably over the
last year, from a malicious browser
■ ECHO Infini SDN BHD to a range of apps, likely due to
■ GLINT By J SDN. BHD the adoption of AI and LLMs to
■ SUMMIT NEXUS Holdings LLC, BHD accelerate operations.
■ Byte Media Sdn. Bhd.
Read more at: Malicious Appsuite
PDF Editor Spreads Tamperedchef
The web pages of these Malware by scanning the following
companies all appear highly QR code:
generic and likely AI generated.
The companies appear to
be nothing more than shell
companies established to obtain
signing certificates in their names.
An investigation into these
companies revealed additional
shell companies registered at
the same addresses, with similar,
generic-looking websites of
companies purporting to be in
“digital transformation”.
Threat Intelligence Report 2026 61

The Use of AI in Cyberattacks
Velocity, Scale, and an We are seeing a similar
Expanded Attack Surface development among
cybercriminals and espionage
In 2025, AI has revolutionized groups. Using LLMs can make their
software development. New production considerably faster, but
and powerful large LLMs are the result is seldom better than
increasingly being used in the what an experienced and skilled
industry. It is only natural that human can produce.
cyber threat actors follow the
same path, for the same reasons. Some things that become
considerably faster and
Correctly used, AI and LLMs can cheaper to produce using LLMs
be powerful tools in software include writing phishing email
development, but they also have texts, building fake web sites,
limitations. “Vibe Coding” lowers obfuscating code, and generating
the bar for software development, updated versions of malicious
and speeds up the process, but code when the original is detected
such code is often full of errors and by antivirus solutions.
the time gained in writing the code
is sometimes lost in bug-fixing. Using LLMs to generate texts can
give a threat actor the ability to
Alternatively, apps are released full craft convincing spear phishing
of security holes, as LLMs are still emails in multiple languages, but
notoriously bad at securing its own the reality here is that these emails
code. often contain all the typical AI
hallucinations and mistakes that
LLMs have.
62 Threat Intelligence Report 2026

An AI-generated text will almost The sheer volume of email and
always have a lower success rate code an LLM can produce for the
than one crafted by a human same cost as a skilled human
operator with an understanding operator can also still lead to
of language and local culture, but more successful breaches. The
not all threat actors have access important lesson here is that
to such individuals. One reason threat actors use AI for the same
why LLM-assisted phishing emails reason as industry does, because
are often more successful than it does the job more effectively,
many written by humans is likely not because it’s better than skilled
that many cybercriminals have humans. Correctly used, AI can
only a cursory understanding of enhance the productivity of skilled
the business texts they attempt to human operators, but not yet
mimic. replace them.
Some threat actors are now The AI technology is still in its
experimenting with malware that early stages and it’s too soon to
use calls with prompts to LLM to predict how it will advance in a
generate malicious commands, few years’ time. For now, however,
so they won’t have to include it appears that the greatest
them in the code, where they can threat to cybersecurity isn’t
be detected. Such novelties are highly sophisticated AI-powered
unlikely to have a lasting effect, as cyberattacks, but a deluge of
the prompts themselves can also “AI slop”: relatively simple and
be detected. It will nonetheless stereotypical attacks that are fast
have an impact on the security and easy to replicate..
tooling out there, demanding
a higher sophistication level, Core security features that
and updating to be capable of focus on specific signatures
identifying malicious prompts, for or patterns, can be crippled
adequate protection. by polymorphic malware, but
behavioral-based detection
remains effective. Detection based
on known strings and file hashes
can also become overwhelmed
by the sheer numbers of new
LLM-created projects. The race
between offensive and defensive
AI in cybersecurity is currently less
about sophistication and more
about speed and volume.
Threat Intelligence Report 2026 63

AI Is Your Friend,
If You Use It Safely
The widespread adoption of AI Vibe-coded apps are great for
and LLM brings two separate, but testing ideas, but seldom safe for
linked problems. How to secure your production.
networks from malicious use of LLM
and AI, and how to secure your own Incorporating an LLM into your
use of LLM and AI. organization’s environment also
introduces its own security risks. It
Vibe Coding is opening up new is vital to carefully weigh the risks
possibilities for software developers of allowing an LLM to ingest your
to quickly realize ideas into proof- data, even if it is not exposed to
of-concept apps that can be tested the outside. Limiting what data an
and developed into new features LLM can access is also required to
faster than before. comply with the EU member states’
local implementations of the NIS2
This doesn’t eliminate the need for directive.
DevOps, DevSecOps and indeed,
human developers. A successful POC The use of LLM by cybercriminals also
still needs to go through the regular means that it is now easier than ever
development cycle before it can be to produce legitimate looking apps
implemented safely in production. that are actually malicious. Many
threat actors have learned how to
circumvent trust-based security, by
registering shell companies for the
express purpose of obtaining code
signing certificates to sign their
binaries.
The fact that we are now flooded
with various vibe-coded apps, both
malicious and non-malicious, also
means that organization’s need
to put more thought into what
apps users are allowed to use on
machines that have access to their
network. Ideally, only approved apps
available from a company portal
should be allowed, and AppLocker,
64 Threat Intelligence Report 2026

AI Is Your Friend,
If You Use It Safely
or a similar solution, can then be
used to enforce this. This is also true
of phones. Enrolling phones in your
EDR solution is highly recommended.
You should also consider limiting
what apps are allowed on such
phones.
The use of AI and LLMs by cyber-
criminals also has implications for
your SOC. Signature based detection
is going to be less effective going
forward. The use of LLM prompts to
import malicious scripts or make
code polymorphic is just one more
reason. It’s easy for threat actors to
hide and obfuscate strings used in
static detection. Detection should be
based on malicious behavior, not just
signatures.
Response time will likely also need
to be much faster in the future. While
agentic AI use by threat actors is
unlikely to make cyberattacks more
sophisticated, they can potentially
speed up attacks considerably.
Response time until a threat actor
is actively evicted from the system
may have to be measured in
minutes in the future. An alert in a
ticket system that no one responds
to, will do nothing but help the
forensic investigation after the
incident.
Threat Intelligence Report 2026 65

Securing Your Data in
The U.S. America First policy, coupled with
an Insecure World
its readiness to use threats to impose its
will on long-standing allies, exemplified
The Challenge of Knowing When
by open challenges to Greenland’s
“The Regular” Becomes a Threat
sovereignty, is eroding Europe’s trust in
the U.S. This has raised questions about
The vision of an open digital world,
Europe’s dependency on U.S. tech. Two
where information flows in a global
events have added momentum to the
cloud without interference or borders,
effort to reduce European dependence
appears to be coming to an end.
on U.S. technology.
China is using its massive production
capability to flood European markets
with cheap, effective tech that often
contains software with security flaws
or hidden backdoors that China can
abuse. Recently, Norway found hidden
5G SIM cards in buses bought from
China, which could be dialed in from
outside to impact the service.
Commercial Chinese-built network
The first event is that the new U.S.
devices have been known to route
administration fired several members
information back to China for years.
of the U.S. Privacy and Civil Liberties
It’s now increasingly the same across
Oversight Board (PCLOB), leaving the
the world. The Indian government
board unable to issue rulings. Efficient
has enacted laws requiring hosting
oversight by the PCLOB was a key factor
providers to retain network traffic
in the EU Commission’s decision to issue
for up to 6 months for potential
the latest adequacy decision and sign
government inspection. Everywhere,
the Data Protection Framework with the
governments are asserting control
U.S., enabling personal data transfers
over digital information physically
and processing in the U.S. without
stored within the country or passing
requiring additional safeguards from
through it and attempting to leverage
data controllers. This raises concerns
it for their benefit. There is a similar
over the adequacy decisions and the
suggestion in Sweden, where a number
data privacy framework’s longevity and,
of independent inter-communication
in consequence, to what extent that
service providers can, according to
personal data can be lawfully processed
the suggestion, become subject to
by U.S. cloud providers in the future.
mandatory judgments by a secret
court to retain communication in end-
The second event is the U.S. sanctions
to-end encrypted communication
on key personnel in the International
services if the communication is
Criminal Court (ICC) over the ICC’s
deemed to contain information
refusal to drop the war crimes charges
valuable for fighting organized crime.
against Israel officials.
66 Threat Intelligence Report 2026

Another significant consequence is actors. For example, the malicious
that U.S. sanctions on Russia prevent backdoor found in XZ Utils was the
the issuance of new licenses for cloud culmination of a three-year-long effort
products in the Russian market. While to infiltrate and compromise this open
such measures against Russia may be source project.
in line with Europe’s interests, similar
restrictions could be imposed on Another threat to an independent
other nations at the U.S. government’s European software industry is that U.S.
discretion. tech giants have the financial muscle
to buy promising European startups
Today, there are very few reliable that could pose a threat to them. Even if
alternatives to U.S. IT technologies. these European initiatives are successful
The massive U.S.-based hyperscalers and can eventually be scaled up, they
are inexpensive and effective. They will likely not be able to break European
also have the resources to continually dependence on key U.S. IT technologies
identify and patch vulnerabilities in their for at least 5-10 years.
systems. U.S. tech giants themselves
have shown no interest in being drawn
into any conflict that would force them
to act against the interests of their
European customers. However, as they
have testified, they can be forced to
obey the U.S. government.
There are several promising projects
today with a stronger focus on
Europe and the EU. The Digital Europe
Programme (DIGITAL) is an EU funding
program that supports the deployment
of digital technologies to businesses, The adoption of AI in enterprises
citizens, and public administrations introduces new risks to data integrity.
across the EU, with a focus on European LLMs create an additional attack vector
solutions. Most of these projects are in that can lead to data compromise if
the research or evaluation phase and access controls and usage policies are
are not ready to be scaled up or to not strictly enforced. Virtually all LLMs
compete with U.S. services. Today, the available now are owned by either U.S. or
road to an independent European tech Chinese companies.
industry that can rival the U.S. is still
very long.
Many of the European startups
referenced are open source
programs. A problem with open
source alternatives is that they can
be vulnerable to infiltration by threat
Threat Intelligence Report 2026 67

Not Taking the Regular for Granted
Using hosting providers and Microsoft is reportedly exploring a
technology from countries such as new model that would allow several
India and China entails an obligation European hosting providers to run
to conduct ongoing risk assessments Azure independently on a licensing
for enterprises seeking to capitalize model.
on the lower operational costs.
Enterprises need to understand This could potentially put European
the trade-offs associated with out- customers’ data outside U.S.
sourcing critical IT functions, including legislation. If implemented correctly,
increased risk, a larger attack surface, this could alleviate some current
and susceptibility to threats that may risks, but the outcome of these
not exist in lower-risk countries with negotiations will still determine the
higher operational costs. final result.
The fact that the U.S. government The most significant potential
has shown itself willing to use its impact of an open conflict between
power over U.S. tech giants to cut off the U.S. and Europe is that the U.S.
individuals within organizations like government can, and has already
the ICC from American IT services demonstrated a willingness to,
is a cause for concern. Until now, impose sanctions on both individuals,
the widespread adoption of a as in the case of the ICC, and on
technological ecosystem built on U.S. entire nations, as with Russia. Given
tech giants has been, in part, based the widespread adoption and
on trust, and broken trust is not easily extensive capabilities of U.S. cloud
repaired. services, sanctions that cut off
individuals or nations from these
Organizations should weigh risks services could force organizations
against one another. U.S. cloud and governments to implement
services offer effective, affordable alternative solutions on extremely
solutions, but can place your data short notice.
under U.S. government control, which
should, regardless of what origin The risk that something like that
a piece of technology has, always would happen in Northern Europe
be considered and, depending on is hard to quantify, but imposing
context, classified and managed as a sanctions on entire European nations
potential risk. Enterprises with a global would be a “nuclear option” strongly
footprint often need to connect their resisted by the U.S. tech industry, as
networks to high-risk nations to do it would likely devastate its future
business, but doing so safely requires sales in Europe. Truesec assesses
careful planning. that the risk of this occurring is small
in the current climate, but that,
given the unpredictability of the U.S.
administration, this assessment can
change in the future.
68 Threat Intelligence Report 2026

Not Taking the Regular for Granted
Outside of preparations for the extreme
scenario of a complete cutoff of U.S.
services, organizations can take steps
to secure their data from compromise
by foreign governments when using U.S.
tech or storing data outside Europe. Data
governance is key to protecting sensitive
data, regardless of whether the threat is
from a physical site in a high-risk country,
training an LLM on your data, or software
or hardware products from potentially
hostile countries.
On-prem solutions offer greater control
over your data than cloud solutions.
This can also be extended to EDR and
log handling. Network segmentation,
permissions, and identity management
based on clearly defined roles can help
secure environments against data loss
from cyber espionage and LLM leakage.
Organizations must evaluate risks, assess
their threat profile, and understand
business needs. Cloud or on-prem, U.S.
or Europe, all the options come with
their own pros and cons, whereas each
organization weighs them differently.
Despite the risks, continuing to use current
U.S. solutions, whether cloud or on-prem,
remains the safest and most efficient
option for most organizations in Europe
today.
Geopolitical risks are now affecting
cybersecurity, so staying on top of
international political events and
interpreting their implications is also vital
for cybersecurity. Threat intelligence is
more important than ever.
Threat Intelligence Report 2026 69

Hybrid Warfare
At the “Folk och Försvar” conference on Hybrid warfare refers to conflicts that
January 25, 2025, the Swedish Prime blend conventional military force with
Minister stated: “Sweden is not at war. But non-military tools, such as cyber-
neither are we at peace.” This sentiment attacks, disinformation campaigns, and
reflects a reality where conventional war economic pressure. Unlike conventional
is absent, yet hybrid conflict is pervasive. warfare, which primarily relies on military
While NATO is not engaged in open power, hybrid warfare leverages the
conventional warfare with Russia, the entire spectrum of political, military,
relationship is adversarial. economic, social, informational, and
infrastructural domains to achieve
strategic objectives.
70 Threat Intelligence Report 2026

The attempt to achieve long-term Shaped by Russia’s long-standing use
objectives through the synchronized use of cyber operations and information
of three or more instruments of such warfare, which began well before the
powers while deliberately remaining full-scale invasion of Ukraine in 2022,
below the threshold of declared war or the cyber domain is a main front in this
casus belli is “hybrid war”. conflict. In fact, Russia has employed
these tactics since at least 2008, as seen
According to this definition, a single in Estonia. And Sweden has experienced
cyberattack does not qualify as hybrid pressure from Vladimir Putin’s strategic
war; only their orchestrated fusion into a aspirations before joining NATO.
unified campaign across several domains
does. Being in a state of hybrid war The Nordic region is a case study of
introduces new cybersecurity challenges, this development, and recent events
as the cyber domain becomes a focal have demonstrated Russia’s willingness
point for foreign influence and disruption. to employ tactics such as disruptive
It is therefore paramount that we cyberattacks and information domain
incorporate what we understand about warfare. Denmark and Sweden will hold
hybrid war and its manifestations in national elections in 2026, creating
cyberspace when we consider our future opportunities for information operations,
defensive requirements. disruptions, and cyber sabotage that
could undermine trust in democratic
Malign use of cyberspace has existed for processes. The DDoS attacks during
decades, particularly within economic Denmark’s municipal elections in
crimes. What hybrid warfare adds is a November 2025 foreshadow what may
political dimension: adversaries exploit come. Simultaneously, Nordic countries
vulnerabilities to create fear, confusion, are becoming key hubs for defense
and mistrust. Confrontations in hybrid production supporting Ukraine, making
conflicts are often asymmetrical, striking them prime targets for espionage and
where the opponent is weak. For example, sabotage.
the West enforces economic sanctions,
while Russia exploits open and free As tension rises, the risk of escalation
societies to spread propaganda and grows. Political leaders warn that
fear. If cybersecurity of key government open war between NATO and Russia
institutions and civic functions is lacking, is not inconceivable within a few
adversaries will target it, not necessarily years. Ukraine’s experience shows that
for direct military gain, but to erode once this threshold is crossed, cyber
confidence and to cultivate FUD in defense extends beyond cyberspace:
sovereign populations. This FUD can, protecting against destructive malware
in turn, be leveraged in disinformation and even kinetic strikes against
campaigns to erode the democratic critical infrastructure such as server
foundation of individual countries and the farms might become a reality for
unity of allies. cybersecurity. Preparing these scenarios
is essential. Robust cybersecurity and
resilience can deter adversaries and
reduce the likelihood of escalation.
Threat Intelligence Report 2026 71

Outlook 2026
72 Threat Intelligence Report 2026

AI Will Not Change the Game, but
It Will Change the Pace
Two factors will shape cybersecurity mass ransomware attacks targeting
and cyber threats in the coming year smaller enterprises than those
more than anything else: geopolitical typically targeted today. Cost-effective
challenges and the continued cybersecurity solutions for smaller
adoption of artificial intelligence. organizations will likely become more
necessary in 2026.
It is easy to be misled by the venture-
capital-driven hype around various The widespread adoption of AI will also
AI initiatives, but beneath the make it an attack surface. LLMs and
hype, fundamental changes in IT other AI solutions exposed to the internet
technology, driven by AI, will continue will be targeted by prompt-injection
regardless of whether the financial attacks. The use of online LLMs accessed
growth expectations surrounding AI through web browsers will be exploited
are sustainable. by owners harvesting the user’s data,
but even offline LLMs can become a tool
In 2026, Truesec expects more threat for an attacker.
actors to incorporate the use of LLMs
and AI-based solutions into their For years, the cybersecurity industry has
attack chains. We do not expect preached network segmentation and
anything like true agentic AI to tighter identity management as key to
replace human operators in complex improving cybersecurity. Now, some
intrusions; instead, we expect skilled organizations are undoing this work by
threat actors to use AI to automate allowing all their company data to be
tasks, making them cheaper and ingested into a company LLM.
faster to perform.
In 2026, Truesec assesses that threat
This will not fundamentally change actors will begin experimenting with
the challenge facing defenders, but using a company’s AI to map their
it will likely require faster response victims’ environments once they have
times. A ransomware operator that gained a foothold. Once a threat actor
uses AI to automate parts of the has gained access to a patient zero and
attack chain may reduce the time stolen their identity, they can contact
from initial breach to full encryption the company AI. What better assistant in
from days to hours, or even less determining where the most vital data
than an hour. Response times for is stored and how it’s secured than the
defenders need to match this speed. victim’s own AI? How do we ensure our
AI does not become a single point of
Using AI to automate attacks can also failure or even the ultimate insider?
reduce the time and money required
to breach an organization. This, in
turn, will enable a cybercriminal
business models focused more on
Threat Intelligence Report 2026 73

Globalized Cybercrime
Ransomware has, for all intents and
young people now believe that achieving
purposes, been a problem originating
the same standard of living as their
in Russia. But now cybercriminals
parents is not within reach, there has
from around the world collaborate on
been a rise in cybercriminals who are
sophisticated ransomware attacks.
often young and cynical. This is also
an area where foreign adversaries’
Ultimately, organized cybercrime, like all
information operations can affect
crime, is tied to the societies it springs
cybercrime. Divisive and demoralizing
from. When ambitious people with the
state-sponsored propaganda
right skills see no legal way to achieve
is designed to give rise to more
their ambitions, they often turn to crime.
disillusioned youth who sometimes turn
The most corrupt societies are often also
to cybercrime.
the most crime-ridden. The financial
markets and the ways leaders of the
Geopolitical developments will shape not
world can instill hope in their citizens’
just hybrid threats and cyber sabotage
economic future will also determine the
but also organized cybercrime. The
growth of organized cybercrime.
current trend is worrying. While the
international community’s united action
Many developing countries, while
against organized cybercrime is under
often plagued by corruption, have
strain, organized cybercrime is becoming
now attained a level of wealth that
more globalized than ever.
makes owning a computer within
reach. This means more technically
Predicting the future of the geopolitical
proficient computer users, and as a
landscape is beyond the scope of a
result, potentially more hackers. As we
cyber threat landscape report, but wars,
know, cybercrime, unlike other forms
conflicts, and trade wars will likely trigger
of organized crime, has a global reach
a global financial downturn unless they
and requires no physical foothold in the
can be contained. If this comes to fruition,
victim’s country.
it will likely fuel more cybercrime.
Even in the Western world, where many
74 Threat Intelligence Report 2026

War and Innovation
Large wars can trigger significant
innovation. The logic of war reveals what
military and technological concepts
have become obsolete, and which are
the new paradigms. The war in Ukraine
has revealed that missile and drone
technology is more critical than either
side believed before the war.
On all sides, nations and entrepreneurs
now scramble to learn from the
experience of those involved in the war
and to invent their own concepts. Drones
and drone defenses are evolving rapidly.
Cyber espionage is already an
essential part of this new arms race,
and cybersecurity must try to keep up.
This is especially important, as many
of the organizations at the forefront of
this new technology are small startups
with significant innovations but fewer
resources to invest in cybersecurity.
The Nordic countries are now among
the most critical hubs in the European
defense sector. Ensuring that startups
engaged in cutting-edge defense-
sector technology have the proper
cybersecurity focus will be a critical
concern for our own security in 2026.
Threat Intelligence Report 2026 75

Software Development Is
Becoming the Weakest Link
For years, most cybersecurity efforts As a result, large parts of the code
have focused on those with the least used in most software products
information: users. The average are maintained with less security
user in a corporate environment than warranted, given how many
today has a fairly locked-down users can be affected if the code
machine with few options that could is compromised. Some projects
compromise cybersecurity. are arguably better from a security
standpoint than others, but the vast
Software developers, sometimes with majority place nearly zero emphasis
included IT administrative tasks, are on security.
trusted to be more knowledgeable
and therefore have far greater Until the ungoverned open source
permissions to conduct actions community finds a solution to this
that could potentially compromise problem, Truesec assesses that
security. They also require elevated the rise in cyberattacks targeting
permissions to do their jobs, but software developers in general
in many cases, they have higher and open source projects in
permissions than needed, often particular will continue and may
based on trust, which can make a even accelerate. Some forms of
single mistake fatal. gatekeeping and improved security
for such hubs may eventually
These permissions and access to be required, even if that means
software pipelines have now put introducing fees to finance them.
them in the crosshairs of a growing This is very difficult to do, however,
number of threat actors. A wide as there is no structure or governing
variety of attacks, from sophisticated entity. The entire concept of open
social engineering to mass source is based on freedom and
supply chain exploitation, aim to creativity.
compromise software developers.
Just as streaming services reduced
The epicenter of this is the the problem of pirated media, which
ungoverned part of the open source was often riddled with malware,
software community. Large parts something similar may be required
of software development today to address the massive scale of
are heavily dependent on open targeting of open source code-
source code projects. Most such sharing hubs, which are increasingly
projects, in turn, contain numerous vulnerable to a growing number of
dependencies. threat actors.
76 Threat Intelligence Report 2026

Threat Intelligence Report 2026 77

Security Will Be
Everyone’s Concern
As the boundaries between
cyberspace and the real world lowering our guard and granting
blur, so do the boundaries them access, it will be vital to
between cybersecurity and make cybersecurity everyone’s
physical security. With improved business in 2026.
technical cybersecurity, more
threat actors will try to “hack the If we don’t invest in the human
human” instead of the machine. layer of cybersecurity, it won’t
matter if the technical controls are
Social engineering is one of the best-in-class. First-line defenders,
oldest tricks in the book, but such as help desks and IT support,
it’s also constantly evolving. AI are a vital part of cybersecurity, as
technologies, such as deepfake they control network access and
images, will likely further enhance should be treated as part of the
the success of social engineering cybersecurity team. That means
attacks in the coming year. investing in their knowledge and
empowering them to be vigilant.
As our lives become increasingly
digitized and publicly shared Not everyone needs to be a
on social media, it becomes security expert, but raising
easier to find information about awareness and fostering a
individuals and to use it to gain security-aware culture will be key
their trust. To meet the challenge to improved cybersecurity in the
posed by threat actors using coming year.
social engineering to trick us into
78 Threat Intelligence Report 2026

Prevent Breach & Minimize Impact
For more information visit: truesec.com
Threat Intelligence Report 2026 79

For more information
visit: truesec.com