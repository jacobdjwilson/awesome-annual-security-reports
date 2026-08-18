Security Navigator
2024
Research-driven insights
to build a safer digital society

## Table of Contents
- [Security Navigator 2024 Foreword](#security-navigator-2024-foreword)
- [Introduction: What you need to know](#introduction-what-you-need-to-know)
- [Summary: This is what happened](#summary-this-is-what-happened)

## Security Navigator 2024 Foreword
Hugues Foulon
Executive Director at Orange and
CEO Orange Cyberdefense

We are very pleased to provide to the cyber security community the next edition of the Security Navigator. Our position as part of one of the largest telecom operators in the world, and as a leader in cyber security services and research, gives us profound insights. It has become our custom to share this unique view of the cyber security landscape.

There is no denying that this has been a year of fundamental changes for most of us.

Geopolitical disorder has hit countries and society at probably the worst possible time and will severely decelerate recovery after COVID for years. The digital world is becoming a virtual battleground for state-backed APT groups and political hacktivists. Not only businesses, but whole economies find themselves being targeted for political reasons, or at risk of becoming collateral damage. Shifting the focus from monetary gain to mere destruction of "the enemy" has left the threat landscape in turmoil.

But aside from all the crisis we are also on the brink of yet another technological revolution. With incredible speed Generative Artificial Intelligence has started to impact and shift the way we think about and interact with computer technology. The transformative power this has on shaping our economy, security and our everyday life is yet to be determined.

Being aware of one’s vulnerabilities is key to avoid becoming the weak link. We all must join our efforts to build up resilience and protect the digital space. Not only for ourselves, but for our customers, suppliers, employees and the community. Hence our mission is to build a safer digital society. CISOs do that every day.

This is not an easy job. Cyber security is complex. Keeping track of technological evolution means to constantly re-learn, re-evaluate and re-educate yourself and your peers. At Orange Cyberdefense we are tirelessly working to offer you the best guidance and support along this way.

With that goal in mind, our multi-disciplinary experts have digested all this unique information and synthesized our key findings in this report, to the benefit of our clients and of the broader cyber security community. These insights are also crucial for us to keep being relevant as a company.

Trends got confirmed, others are emerging. Cyberextortion emerges as the most prominent form of attack with a strong increase in the past year and a geographical shift towards EMEA and Asia Pacific. Small and medium companies are gaining ground as favourite vulnerable targets. Insightful observations like that should help us navigate the threat landscape – as a closely-knit community. We are proud and humbled every day to be trusted with the security of our clients’ most important assets, and we are deploying the best expertise and technology in all domains to protect their business.

Thank you for your trust and we hope you enjoy reading this edition of the Security Navigator!

Hugues Foulon

---

## Introduction: What you need to know
Olivier Bonnet De Paillerets
EVP Marketing & Technology
Orange Cyberdefense

> "In our shared technological adventure, people and safety must be our primary concern."

Our very singular ability to gather data from very different sources both within Orange and externally, cross-referencing and analyzing them assures the relevance of this report.

Data from the Security Navigator 2024 highlights a few trends, including:
- A dynamic cybercrime ecosystem, that expands its operational mode by directly targeting company personnel in order to better penetrate their systems.
- Cyber criminals accelerating the geographical lateralization of their attacks, targeting not only Anglo-Saxon countries or Europe which nevertheless are still strongly impacted.
- An increase in cyberattacks that should be seen on mobile devices, where our personal and business data are increasingly concentrated.
- Continued targeting of Scientific and Technical IP, the financial sector, and particularly of Industrial and Manufacturing infrastructure.
- An explosion of Cyber hacktivism over the past two years to support political or social demands.

Today, the Security Navigator is one of the central elements of Orange Cyberdefense’s threat analysis, insights of which must go beyond Chief Information Security Officers (CISOs) and security experts. It is complemented by the ‘Executive Security Navigator’, a dedicated report intended to support them in raising awareness and driving actions with their organization’s leadership, anchored on the reality of the risks induced by this cyber threat.

This document is also intended to become the cornerstone of the partnership of trust that we wish to build with you. It must enrich our debates within a community that is still too isolated. For example, we invite you to take advantage of all our analytical capabilities through articles reflecting on the importance of the human factor in an attack, and stories from our response teams, in order to continue to acculturate your environment on cyber security.

Above all, it emphasizes the extent to which in our common technological adventure, people and security must be our primary concern.

I hope you enjoy reading!

---

## Summary: This is what happened
Charl van der Walt
Head of Security Research
Orange Cyberdefense

We’ve never used the word ‘unprecedented’ in a Security Navigator before, and we won’t do it this year either. But there’s no denying that the 12 months of cybersecurity captured in this report have been extraordinary.

The tempo, the severity, the complexity, and the consequences of developments in our domain have accelerated to dizzying levels.

Our World Watch service published 491 advisories for the period October 2022 through September 2023, averaging over 40 advisories per month. No advisories with Urgency Critical were issued for the period. This is somewhat astonishing given the almost overwhelming scale and frequency of security ‘drama’ that occupied our minds. Yet the CISOs we speak to universally wear a kind of ‘thousand yard’ stare and report being nearly overwhelmed by the ferocity of the security news cycle.

No single effort could hope to capture, comprehend, and convey all the security industry has seen and learned since we last published this report. Instead, we aim to share what we at Orange Cyberdefense have observed or considered first-hand. We cross-reference and analyze the data we collect from our diverse operations and own research. We describe the pictures we see in that data and share our efforts to answer the questions it raises for us. With this somewhat lopsided effort we hope to illuminate in some small way those parts of the landscape we can shine a light on, and present insights and observations we hope will enable security practitioners to make better-informed decisions that deliver the positive security outcomes our digital world desperately needs.

We begin with a summary of key events, themes and observations.

### Incidents & Attacks

#### Cl0p, Cl0p, Cl0pping on heaven’s door
The security incident that 2023 will probably be remembered for was the series of attacks with cascading impacts by the Cl0p Cy-X group. Cl0p was credited with exploiting vulnerabilities in the public facing managed file transfer (MFT) solution of MOVEit Transfer by vendor Progress Software. This was the third MFT solution Cl0p exploited in almost three years. In early February 2023 news reports of victims associated with another MFT called GoAnywhere emerged[^1]. This time a 0-day was targeted in Internet-facing GoAnywhere services and was a repeat of the playbook that CL0p was starting to perfect.

We’ve been tracking Cl0p for 41 months now. While they’ve historically been a relatively low-profile actor, their recent successes against prominent enterprise platforms completely changed their profile.

Cl0p has claimed 514 victims in 43 different countries, but the effectiveness of their unique modus operandi in 2023 is clear to see.

Cl0p impacted so many 2nd and 3rd level victims that it completely distorted our Cyber Extortion (Cy-X) victim data, which we explore extensively in this report. Cl0p accounts for 373 victims in 2023, significantly inflating the 2563 victims recorded for this period from other actors.

The ‘Finance and Insurance’ sector in particular recorded a 106% increase in Cy-X victims, largely at the hands of Cl0p.

The Cl0p incidents illustrated just how much damage a single security blow can do. It spawns passionate arguments about software supply chain security and raises concerns about the resilience of the cloud and SaaS offerings so many businesses rely on. But it also reminds us of the issue of ‘interdependence’, which is a fundamental characteristic of cyberspace and cybersecurity.

#### Microsoft faces the STORM (-0558)
In 2023, Microsoft announced that an attacker, identified as STORM-0558, gained unauthorized access to Exchange Online data hosted in Azure by abusing Outlook Web Access (OWA)[^2]. The attackers had targeted a subset of accounts belonging to specific organizations. At the time, Microsoft conceded that they couldn’t explain how the attackers had obtained the private key of the MSA certificate used in the attack and was still investigating the matter. This inactive MSA key enabled attackers to fool the process that checks authentication token signatures, as the forged authentication token was signed by the trusted certificate. In a follow-up post by Microsoft, the firm speculated that the attacker obtained the private MSA key material from an unredacted crash dump of a host that had the key material in its memory. The crash dump was allegedly obtained from a compromised Microsoft engineer’s debug workstation, to which the dump file had been copied[^3].

#### Jump(Cloud) the higher we fall
JumpCloud was the victim of a cyberattack in mid-2023 that prompted them to force a rotation of privileged API keys. Shortly after this Mandiant published a report in which they described how attackers gained access to a victim's network and deployed malicious scripts using JumpCloud Agents. Mandiant reported that the activity matched adversaries with strong links to the Democratic People’s Republic of North Korea (DPRK).

Incidents like the STORM-0558 attack against Microsoft, the JumpCloud compromise, and more attacks impacting Okta and in turn impacting 1Password, BeyondTrust, and Cloudflare show us how we have collectively been shifting our attack surface from the Internet perimeter to the desktop, to the cloud[^4][^5][^6][^7]. The homogeneous Microsoft desktop environment has historically enabled massive ROI for threat actors, but the same homogeneity is characteristic of successful enterprise-oriented cloud offerings and similarly presents attackers with a compelling ROI.

#### (In)Security impacts governments
In July 2023 the Norwegian government announced that 12 government departments were impacted by a cyberattack[^8]. The attackers leveraged a previously unknown critical vulnerability in the Ivanti Endpoint Manager Mobile (EPMM)[^9] that allowed the attackers to access users’ Personally Identifiable Information (PII). A second vulnerability was also reported a few days later that could, if combined with the first, result in a fully functioning backdoor[^10]. A Proof-Of-Concept (POC) was published shortly thereafter, putting the exploit in the hands of anyone wanting to test it[^11]. Ivanti then announced a third vulnerability[^12]. The publicly available POC means that these older versions are at great risk of being exploited.

#### A Volt of lightning
In May 2023, Microsoft reported[^13] on the activities of a Chinese threat actor named ‘Volt Typhoon’, that is considered responsible for targeting critical infrastructure providers and other sectors in Guam and elsewhere in the United States. According to Microsoft, Volt Typhoon has been breaching critical infrastructure in the USA since 2021[^14]. Volt Typhoon was compromising vulnerable ‘internet-facing Fortinet FortiGuard devices’ and then moved further through the victim’s infrastructure using features and capabilities available on the network in a technique known as Living-Off-the-Land. Microsoft’s report states that Volt Typhoon also used compromised routers and Small Office Home Office (SOHO) network equipment to act as a proxy, making the attacker’s network traffic look mundane.

Microsoft claims that Volt Typhoon is allegedly affiliated with the Peoples Republic of China (PRC). Notable about the incident is Microsoft’s assessment that Volt Typhoon is ‘pursuing development of capabilities that could disrupt critical communications infrastructure between the United States and Asia region during future crises’.

The case is an important first glimpse at an inevitable and anticipated next evolution of conflict in cyberspace, in which one of the crucial weaknesses of offensive cyber capabilities is addressed: the outcome of cyber operations is not a linear certainty. Unlike a missile that can be deployed, loaded, and fired with predictable results at a moment’s notice, a cyber operation is more like the deployment of ground troops or an aircraft carrier - complex, nuanced, unpredictable. Cyber operations can take an indeterminate amount of time to have an effect.

#### When governments play (smaller countries lose)
The war against Ukraine has of course continued to fuel ongoing cyber activities. Mandiant detailed the strategic cyberattack playbook used by Russian attackers against Ukrainian targets[^15]. Pre-invasion actions involved reconnaissance, followed by destructive attacks just before the Russian invasion of Ukraine in February 2022. Pressure was sustained against targets throughout 2022. The report also mentions the introduction of new personas in the form of hacktivists such as the CyberArmyofRussia_Reborn, to amplify and propagate falsehoods about Russia’s progress in the war.

There have been countless other examples of government hacking campaigns against multiple targets – too many to mention in this report – so we highlight just a few here:
- The United Kingdom’s Electoral Commission announced in August 2023 that ‘hostile actors’ had breached it and accessed Personal Identifiable Information (PII) of registered voter’s data[^16]. At the time of writing, the Electoral Commission had not provided details besides the fact that PII was stolen[^17]. Some speculated that a vulnerable Microsoft Exchange Server could be linked to the incident, but that has not been explicitly confirmed[^18].
- In August 2023, the China National Computer Virus Emergency Response Center (CVERC), along with a cyber security company, announced that they had discovered the compromise of a data collection station at the Wuhan Earthquake Monitoring Center[^19]. The CVERC attributed the attack to intelligence agencies of the United States of America. CVERC claim that the goal of the implant was to allow the attackers to steal monitoring data as part of reconnaissance and intelligence gathering procedures.
- A threat actor with ties to the Chinese government, tracked as UNC4841 by Mandiant, have allegedly exploited an unknown weakness (0-day) in the Barracuda Email Security Gateway (ESG) since October 2022[^20][^21]. Attacks spread across 16 countries and were so persistent, it prompted Barracuda to instruct their clients to completely replace the hardware appliance rather than rely on the software fix to close the backdoor.

The Belfer Center’s National Cyber Power Index[^22] ranks countries that have some degree of “cyber power”. In 2022 the ten “most powerful cyber nations” were considered to be the U.S.A, China, Russia, the United Kingdom, Australia, the Netherlands, Republic of Korea, Vietnam, France and Iran. But the index tracks 30 such countries, there are doubtless others, and the list is growing.

With practice, cyber operations have become an effective tool, and at a relatively low price point they are becoming increasingly popular.

Smaller and developing nations also become victims of compromise by other nations, either as direct targets or as well-placed staging positions for operations with other objectives.

Losing control over technology implies losing control over autonomy. Every government is an ‘e’ Government. And every human is a citizen of cyberspace. This is a digital world and digital security is an essential part of the core infrastructure on which this world is built. National security therefore demands robust and consistent national cybersecurity but achieving that is far from trivial. The larger and more complex technology and systems become, the more difficult it is to defend, to the point where a tenable defense tends toward a practical impossibility.

### 0h (days) my goodness
July 2023 was a particularly busy time for 0-days, with news breaking of a vulnerability in Citrix ADC (CVE-2023-3519) that was potentially being exploited in the wild. There were several others.

By their very nature, it’s hard to keep track of the number of 0-days. In September this year Ars Technica asserted[^23] that with 70 zero-days uncovered so far this year, 2023 is on track to beat the previous record of 81 set in 2021.

Our own internal ‘Vulnerability Watch’ Exploit Database (EDB) records 109 CVEs tagged with "Exploited in the Wild", but of course those are not necessarily 0-day.

The practice of vulnerability management, prioritization and patching is still far from mature, and is becoming ever more urgent.

### Hacktivism

#### Distributing DDoS
Hacktivism can be understood as a form of cyberattack that is conducted to further the goals of political or social activism. It aims to draw public attention to an issue or cause the hacktivist believes in[^24].

Hacking, crime, espionage, politics, and ideology have long been difficult to tease apart, and hacktivism has always been a central, if somewhat benign, element of this complex mix.

But the past 2 years we have seen an apparent increase of activity in the hacktivism space.

With the war against Ukraine, we observed a significant surge in hacktivist activity supporting both sides of the conflict.

Examples included the hacker collective Anonymous declaring ‘war’ on Russia[^25] and the Ukrainian Minister of Digital Transformation Mykhailo Fedorov calling on individual hackers on the internet for help[^26][^27], thus creating the first IT Army of Ukraine[^28].

While the geopolitical rhetoric escalated, so too did the force and impact of the Denial-of-Service attacks recently favored by hacktivists.

Indeed, hacktivism and mis/disinformation have emerged as two sides of the same coin and have increasingly come to characterize the use of cyber within geopolitical conflicts.

Two hacktivist groups that we have been tracking are Anonymous Sudan and Noname057(16). Both are directly or indirectly engaged with the ongoing war against Ukraine.

We are seeing a continuous evolution towards ‘cognitive’ activity. The impact has less to do with the disruptive effect of the attack or the value of the data or systems that are affected but with the impact that these attacks will have on societal perception.

A pro-Ukraine hacktivist group called ‘Ukrainian Cyber Alliance’ apparently took down the Trigona ransomware leak site and its servers[^36].

The Trigona take down was not an action against cybercrime, however, but part of a politically driven effort to disrupt any Russian cyber operation.

#### Crossing over
Current geopolitical events have also politicized some Cy-X actors[^29], some of whom have become more politically driven. Conti, CoomingProject, and Stormous all proclaimed their full support for Russia in the war against Ukraine[^30]. Ransomedvc suggested an intent to attack Iran and Palestine after the Hamas-Israel war broke out[^31]. And Cuba group members have reportedly run espionage operations targeting government and military officials in Ukraine[^32][^33].

‘Crossovers’ have gone in the other direction also. The hacktivist group Anonymous Sudan, for example, at one point was demanding ransoms to stop their ongoing DDoS attacks[^34]. The hacktivist group GhostSec also turned to ransomware and launched their own RaaS offering and released its own ransomware strain[^35].

Most of the hacktivist attacks we’ve recorded also use Distributed-Denial-of-Service (DDoS) attacks, and some have developed sophisticated DDoS capabilities, which are also becoming more available as services.

In June 2023 Microsoft detailed[^37] ongoing DDoS activity by the threat actor they track as STORM-1359. They assessed that the attacks relied on access to multiple virtual private servers (VPS), in conjunction with rented cloud infrastructure, open proxies, and DDoS tools. More interestingly, the DDoS activity targeted Layer 7 (L7) rather than the OSI Layer 3 or 4, as is most often the case.

We reported at the time that these types of attacks require a different approach. A cleverly designed L7 attack is more difficult to execute, but can demand even more processing by the server, creating a kind of asymmetry and quickly depleting server resources.

DDoS has sometimes been thought of as a mere nuisance in the past, but it’s been becoming more effective and available to actors of all kinds. In the current convergence between politically motivated attacks and Cyber Extortion – both of which involve a form of psychological coercion – DDoS is assuming a more important role.

Since the emotional impact of a DoS attack is powered by the attacker’s message, the actor can choose to make a political statement out of any apparently successful attack. Targeting can be highly opportunistic, which greatly exacerbates the technical asymmetry already faced by defenders in cyberspace.

### Vulnerabilities and Exploits

In 2023, we tracked renewed interest in Vulnerability Intelligence and prioritization. As defenders are increasingly overwhelmed by waves of new vulnerabilities and exploits, the challenge of patching and mitigation remains as intractable as ever, and attackers have rediscovered the art (and benefit) of exploiting vulnerable systems over the internet.

#### Vulnerability is getting old
This year we revisit the menacing vulnerability theme with an eye on the ever present and lingering tail of unresolved system weaknesses. We assess over 2.5m vulnerability findings that we reported to our clients, and over 1,500 reports from our professional ethical hackers, to understand the current state of security vulnerabilities and consider their role and effectiveness as a tool for prioritization.

The bulk of unique Findings reported by our scanning teams - 79% - are classified as ‘High’ or ‘Medium’, and 18% of all serious findings are 150-days or older. Though these are generally dealt with more swiftly than others, some residual still accumulates over time. While the number of findings we identify are resolved rapidly after 90 days, 35% of all findings we report persist for 120 days and longer. Too many are never addressed at all.

While our scanning results illuminate the persistent problem of unpatched vulnerabilities, our Ethical Hacking teams more frequently encounter newer applications and systems built on contemporary platforms, frameworks and languages.

17.67% of findings our Ethical Hackers reported were rated as ‘Serious’, but the hackers must work harder today to discover them then they had to in the past.

#### Hacking getting harder
The Ethical Hacking dataset we examine for this report includes clients from over 10 different countries.

From this data we assess that our hacking teams had to work 13% harder in 2023 than in 2018 to match the level of findings reported per project day.

The average time spent per project to report a serious finding is 10.5 days.

#### Hacking Intelligently and patching intelligently
Only an estimated 4.1% to 5.5% of all vulnerabilities in 2020 were considered exploitable, and this reality hasn’t changed[^38][^39].

The Exploit Prediction Scoring System (EPSS) by FIRST is a relatively new statistically-derived metric designed to help the vulnerability management process by illuminating vulnerabilities that are more likely to be exploited[^40]. EPSS could help focus security teams on vulnerabilities that should be patched first.

In this report we explore the notion that Ethical Hacking, as a form of vulnerability identification and prioritization, also acts as a source of highly contextual vulnerability intelligence.

By scaling EPSS scores so that they can easily be compared with the scores assigned by Ethical Hackers, we note that EPSS and Ethical Hacking scores correlate quite closely, but vary across different target types.

Most importantly, however, a total of 177 (85.92%) CVEs were reported by our testers that have a lower EPSS score. In other words, a skilled attacker matching our Ethical Hacking team’s skill would have found 177 potentially serious vulnerabilities that would probably not have been prioritized using EPSS.

Using our own in-house Exploit Database as a reference, we are unable to reproduce the very encouraging conclusions of previous research that used more ‘theoretical’ frames of reference. This year we thus continue to explore more efficient ways to employ Vulnerability Intelligence in the ‘real world’.

---

[^1]: [Image description of GoAnywhere MFT 0-day news reference]
[^2]: [Image description of Microsoft STORM-0558 advisory]
[^3]: [Image description of Microsoft debug workstation crash dump explanation]
[^4]: [Image description of Okta security impact diagram]
[^5]: [Image description of 1Password incident report]
[^6]: [Image description of BeyondTrust advisory]
[^7]: [Image description of Cloudflare impact report]
[^8]: [Image description of Norway government cyberattack report]
[^9]: [Image description of Ivanti EPMM vulnerability advisory]
[^10]: [Image description of Ivanti EPMM backdoor analysis]
[^11]: [Image description of Proof-Of-Concept exploit release]
[^12]: [Image description of Ivanti third vulnerability notice]
[^13]: [Image description of Microsoft Volt Typhoon advisory]
[^14]: [Image description of Volt Typhoon critical infrastructure timeline]
[^15]: [Image description of Mandiant Russian cyberattack playbook report]
[^16]: [Image description of UK Electoral Commission breach announcement]
[^17]: [Image description of PII stolen details report]
[^18]: [Image description of Microsoft Exchange Server link speculation]
[^19]: [Image description of Wuhan Earthquake Monitoring Center compromise report]
[^20]: [Image description of Mandiant UNC4841 Barracuda ESG report]
[^21]: [Image description of Barracuda hardware replacement advisory]
[^22]: [Image description of Belfer Center National Cyber Power Index ranking]
[^23]: [Image description of Ars Technica zero-day tracking article]
[^24]: [Image description of Hacktivism definition reference]
[^25]: [Image description of Anonymous declaration of war on Russia]
[^26]: [Image description of Mykhailo Fedorov call to action]
[^27]: [Image description of Internet hackers appeal]
[^28]: [Image description of IT Army of Ukraine formation]
[^29]: [Image description of Politicized Cy-X actors overview]
[^30]: [Image description of Conti, CoomingProject, and Stormous statements]
[^31]: [Image description of Ransomedvc intent declaration]
[^32]: [Image description of Cuba group espionage operations report]
[^33]: [Image description of Ukraine military officials targeting report]
[^34]: [Image description of Anonymous Sudan ransom demand report]
[^35]: [Image description of GhostSec RaaS offering release]
[^36]: [Image description of Ukrainian Cyber Alliance Trigona take down report]
[^37]: [Image description of Microsoft STORM-1359 DDoS activity report]
[^38]: [Image description of Exploitable vulnerabilities statistics 2020]
[^39]: [Image description of Vulnerability exploitability trend analysis]
[^40]: [Image description of FIRST Exploit Prediction Scoring System overview]

---

ice: Sweden 17
The power of GRC Governance: Risk Management: Compliance:
The Strategic Compass The Agile Watchdog The Steadfast Lighthouse
Governance is the strategic compass for Risk management is like a vigilant Compliance, like a dependable lighthouse,
How governance, risk and compliance (GRC) can an organization's cybersecurity, aligning cybersecurity watchdog. It entails ensures organizations navigate the
the strategy with the given objectives. It proactively identifying, assessing and complexities of the cyber domain while
shape the backbone of your security strategy sets clear goals, policies, and proactive mitigating risks. Anticipating and enabling upholding legal and ethical standards.
strategies. For example, in safeguarding preventive measures to minimize their It encompasses adherence to laws,
customer data, governance establishes impact is also essential. Risk management regulations, and standards, verified
policies like encryption, access controls, can entail threat modeling and developing through regular audits. When new
While many organizations may work with these three elements individually, the true power
and incident response plans, aligning countermeasures, effectively bolstering regulations arise, compliance involves
of GRC principles lies in their ability to synergize with each other and, at the same time,
cybersecurity with broader business incident response capabilities. reviewing processes, updating policies,
harmoniously align with business objectives and strategic goals.
strategies to protect the organization and conducting audits to maintain legality,
Together, the GRC principles form a holistic, strategic, and protective ”umbrella” that against emerging threats. ethics, and enhance incident response as
safeguards critical areas, including OT Security and Mobile Device Security, against a per regulatory expectations.
broad spectrum of cyber threats.
Margarita Sallinen, Information Security Consultant, Orange Cyberdefense To summarize: governance sets the direction; risk management identifies potential
obstacles; and compliance ensures cybersecurity practices remains lawful and ethical.
Adapting to complex cyber threats A strong commitment to cybersecurity initiatives drives Five practical GRC implementation tips
substantial change and fosters a resilient cybersecurity culture,
Cyber threats range from well-established approaches like seamlessly integrating cybersecurity with strategic planning While understanding the individual GRC principles is important, practical implementation blending all
phishing attacks to emerging ones like Cyber Extortion, rather than treating it as an afterthought. three is where organizations can be most effective.
hacktivism and AI-driven attacks by cybercriminals. In addition
C-suite executives must champion GRC principles in
to providing comprehensive defense, GRC principles offer a
cybersecurity, and send a clear message throughout the
strategic framework for mitigating financial and reputational
organization that cybersecurity is not merely a technical 1. Define Clear Governance Policies
risks while preserving an organization's brand. Achieved
concern but a critical aspect of risk management and corporate
through governance, robust risk management, and stringent Establish comprehensive governance policies that clearly define roles, responsibilities, and decision-making processes
governance. This mindset should permeate every department,
compliance measures, this approach enables organizations to related to cybersecurity. Ensure alignment with your organization's strategic objectives. Engage key stakeholders,
from the boardroom to employees handling sensitive
navigate the complex domain of cyber threats with resilience including leadership, IT teams, and legal departments, in policy development.
information, ultimately creating a culture of cyber resilience.
and confidence.
When the boardroom treats cybersecurity as a strategic
2. Conduct a Cybersecurity Risk Assessment
It's not 'just a tech problem' business imperative it sets the expected behavior for
the rest of the organization. Start by identifying your organization's unique cybersecurity risks. Understand the threats you face, the vulnerabilities
Cybersecurity is usually associated with tech, code, firewalls, in your systems, and the potential impact of security incidents. This assessment serves as the foundation for tailored
and encryption algorithms. But equating security with governance, risk management, and compliance strategies.
technology is a misconception; and implementing solutions
Redefining the
alone can lead to a false sense of protection. Of course 3. Stay Compliant
deploying the right tools and having the appropriate expertise Cybersecurity Strategy
Continuously monitor and maintain compliance with relevant laws, regulations, and industry standards. This includes
to respond and recover from cyber security incidents is
conducting regular audits and assessments to ensure adherence to cybersecurity best practices. Keep abreast of
To effectively adapt to and navigate the shifting threat
essential. However, as risks have grown more intricate, and
regulatory changes that may impact your organization.
landscape, organizations must transcend the boundaries
threats more pervasive, technology alone is not sufficient to
of traditional IT-focused cybersecurity strategies. Instead of
ensure cyber resilience. 4. Foster a Cybersecurity Culture
relying solely on reactive measures and asking, "Why would
As cyber threats evolve, they introduce new challenges, it happen to us?" organizations should embrace a holistic Promote a culture of cybersecurity awareness and responsibility throughout the organization. Train employees to
spanning from Operational Technology (”OT”) risks, approach grounded in resilience and proactive measures. They recognize and respond to threats effectively. Encourage reporting of security incidents and near misses.
encompassing critical infrastructure, to vulnerabilities should recognize the profound importance of Governance,
associated with Mobile Device Security, which impact nearly Risk Management, and Compliance (”GRC”) principles as a 5. Continuously Evaluate and Improve
every employee. Within this evolving threat landscape, foundational framework for cybersecurity.
Cybersecurity is an ongoing journey. Regularly assess the effectiveness of your GRC principles and make adjustments
organizations now face consequences such as breaches,
as needed. Conduct post-incident reviews to identify areas for improvement.
financial losses, and reputational damage, prompting them to
carefully consider where to direct their cybersecurity efforts. Understanding GRC Principles
Therefore, it has become imperative to zoom out and adopt a
For an organization's cybersecurity strategy to excel, GRC
broader, and more comprehensive perspective.
should rightfully claim the spotlight. To gain a comprehensive Key takeaways
The Critical role of the C-suite understanding of this framework and unlock its benefits, it's
essential to delve into the individual GRC principles first.
Leadership, including the Board and C-suite executives, The Power of GRC in cybersecurity is realized when Governance, Risk Management, and Compliance
plays a pivotal role in adopting the GRC framework into the (GRC) principles synergize, while aligning with business objectives. This holistic approach yields
organization's cybersecurity strategy. Cybersecurity resilience multiple benefits, including the minimization of operational inefficiencies, improved communication,
should start in the boardroom. and enhanced risk mitigation. GRC principles play a pivotal role in this context, offering a
comprehensive framework that bridges technology with strategic goals.
GRC principles not only protect critical areas but also mitigate financial and reputational risks.
Leadership's commitment, especially in the boardroom, is crucial to fostering a culture of cyber
resilience.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

18 Security Navigator 2024 Key data of the year 19
Basic Data analysis
Key data
of the year
We collect and analyze two fundamental forms of data for the
Security Navigator: data produced by our internal operations –
Threat Detection, Security Intelligence, Vulnerability Scanning and
Ethical Hacking – and data we collect specifically for research
purposes, namely Cyber Extortion victims, (limited) Hacktivism
attacks.
In this chapter we present an analysis of each of these data sources
individually, then also apply this data elsewhere in the report to
answer specific research questions.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

20 Security Navigator 2024 Key data of the year: Threat Detection 21
Threat Detection Types of incidents Physical
Physical actions encompass deliberate threats that involve
We announced in our previous report that we were in the
proximity, possession, or force. Includes theft, tampering,
process of adopting the industry standard VERIS (Vocabulary
snooping, sabotage, local device access, assault, etc.
for Event Recording and Incident Sharing) framework for
About the data
incident classification across our SOCs. This has now been
Error
▪ Total of incidents: 129,395 (up from 99,506 in 2022) rolled out to the majority of our CyberSOCs, meaning most of
the data in scope for this report now uses this classification Error broadly encompasses anything done (or left
▪ Out of these incidents, 25,076 could be confirmed as True Positive Incidents (19%)
framework, allowing us to provide analysis based solely on undone) incorrectly or inadvertently. Includes omissions,
▪ Period analyzed: October 2022 to September 2023 VERIS. misconfigurations, programming errors, trips and spills,
malfunctions, etc.
▪ Data sources: firewalls, directory services, proxy, endpoint, EDR, IPS, DNS, DHCP, 4A
SIEM and our managed threat detection platform Environmental
Environmental not only includes natural events such as
earthquakes and floods, but also hazards associated with
THREAT ACTORS are entities that cause the immediate environment or infrastructure in which assets
Actor
Funnel: 129,395 25,076 or contribute to an incident. are located. The latter encompasses power failures, electrical
interference, pipe leaks, and atmospheric conditions.
THREAT ACTION describe what the
Action threat actor(s) did to cause or contribute
Alert to incident Potential incidents Confirmed Incidents to the incident. A global view
ASSET describes the information assets As always, we strive to provide a global overview of what we
Asset that were compromised during the are seeing in our incident data with the aim being to highlight
incident. trends that can also be applied to the global threat landscape.
To facilitate this, a broad data set is collected from across all of
Attribute Which security ATTRIBUTES were
Hacking 30% the operational teams within Orange Cyberdefense including
(CIA) compromised during the incident?
our 14 CyberSOCs responsible for supporting customers
End user
around the globe.
device
28% Following in the same vein as recent Security Navigator reports,
Threat Actions we again have the luxury of utilizing a whole years’ worth of
Managed Threat Detection Services data, 1st October 2022 to
External The Threat Action categories used in the VERIS framework 30th September 2023. This year’s report however will be the
Misuse 16%
44% Server consist of the following 7 primary categories: first time we have had a full year’s worth of data based on using
the VERIS framework to better categorize our incidents.
27%
Malware
Malware is any malicious software, script, or code run on a Events, Incidents,
Malware 13%
device that alters its state or function without the owner’s
Confirmed Incidents
Other/Unknown informed consent. Examples include viruses, worms, spyware,
keyloggers, backdoors, etc.
Internal Assets A note on terminology: we log an event that has met certain
Other Action 7%
37% 22% Hacking conditions and is thus considered an Indicator of Compromise,
Attack or Vulnerability. An Incident is when this logged Event, or
Hacking is defined within VERIS as all attempts to intentionally several Events, are correlated or flagged for investigation by a
Social 7% Account 7% access or harm information assets without (or exceeding) human – our security analysts.
authorization by circumventing or thwarting logical security
Other 1% An Incident is considered ‘Confirmed’ when, with help of the
mechanisms. This includes brute force, SQL injection,
customer or at the discretion of the analyst, we can determine
Partner 1% Error 7% Network 6% cryptanalysis, denial of service attacks, etc. that security was indeed compromised. We refer to these
‘Confirmed’ incidents in this report as ‘True Positives’.
Social
Unknown
Cloud 1% True Legitimate incidents are those that were raised but, after
Actor 18% Social tactics employ deception, manipulation, intimidation, etc
consultation with the customer, proved to be legitimate activity.
to exploit the human element, or users, of information assets.
Incidents are categorized as 'False Positive' when a false alarm
Includes pretexting, phishing, blackmail, threats, scams, etc.
was raised.
Misuse
Because individual SOCs or clients may have slightly different
Actors Action Asset Misuse is defined as the use of entrusted organizational approaches to defining Incident status, we simplify these
Entities causing What the threat The asset that resources or privileges for any purpose or manner contrary categories to ‘Confirmed’ and ‘Other’ in parts of this report.
an incident actor(s) did was affected to that which was intended. Includes administrative abuse,
use policy violations, use of non-approved assets, etc. These
actions can be malicious or non-malicious in nature. Misuse
is exclusive to parties that enjoy a degree of trust from the
organization, such as insiders and partners.
* Overview flow with major categories, for details see following pages
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

22 Security Navigator 2024 Key data of the year: Threat Detection 23
Totals It’s important to remember though that Misuse does not Threat Action in detail
necessarily equate to malicious activity with intent to cause
In total 129,395 incidents were recorded, all of which were harm or loss, it could equally be an unintentional breach of Top 20 Threat Action and Threat Action Level 2 combined
investigated by human security analysts in one of our a policy. With this being the first time we present full year of
CyberSOCs. These investigations resulted in 25,076 ‘True VERIS data, we reserve speculation on shifts until we have Web Attack (Hacking)
Positive’ confirmed security incidents being raised with our another full year for comparison. Unapproved hardware/software/
customers - 19% of all the incidents we investigated. The other script/workaround (Misuse)
Just as we saw last year, Hacking remains in the top spot,
incidents comprised of 10% ‘True Legitimates’ and 58% ‘False Port scan (Hacking)
however this year it accounts for almost a third of confirmed
Positives’ with the remaining 13% having inconclusive status. Phishing/Spear-Phishing (Social)
incidents with 30.32%, which is a relatively significant increase
We are happy to say that our client base has grown from last on the 25% previously seen. Incidents categorized as Error None (Physical)
year with data from 44.5% more clients being included in this (7.33%) again take fourth place and Social (7.15%) completes Brute force (Hacking)
report. This relatively large growth in dataset however actually the top 5.
Malfunction (Error)
resulted in only 25,076 confirmed incidents, a decrease of 14%
Whilst ‘Error’ does not always imply a security incident it can
in the confirmed incidents from last year’s report. Other (Malware)
easily be a precursor to one, especially with the rapid migration
Phishing (Social)
This translated into an average number of 23.6 confirmed to cloud environments and the complexities involved with their
incidents per month/customer over the past 12 months. configurations for example, whereby a simple misconfiguration Adware (Malware)
This is a significant decrease from the figure of 42.7 we could easily leave private data exposed. Net misuse (Misuse)
recorded for the same period last year, primarily due to
The Social category covers any attempt to deceive, manipulate None (Environmental)
the configuration of clients in this dataset, and internal
or otherwise abuse employees. The obvious tactic here is
operational efficiencies. Web Access misuse (Misuse)
any form of phishing or Business Email Compromise (BEC).
Carelessness (Error)
Historically we have always seen Malware to be one of the two Social attacks of this kind are difficult to identify in detection
highest detected true positive incident types, this year though data – where we observe the effect rather than the cause of Misconfiguration (Error)
it has slipped to third with just 13%, dropping from 16.5% of an activity. This threat vector is therefore probably under- Privilege abuse (Misuse)
VERIS classified incidents seen last year which saw it joint represented in this datasource. Spam (Social)
second with Misuse. The Misuse category was again second
Worm (Malware)
with 17.28%, almost exactly in line with last year’s report.
Downloader/Dropper (Malware)
Backdoor (Malware)
0% 5% 10% 15% 20%
If we add a second level of detail to the top level VERIS Threat It’s worth remembering that this combination would also
category, we can see a more granular view of the underlying cover so-called shadow IT. This is where employees deploy
Incidents by Threat Action cause of the incidents our analysts have investigated. The or use hardware (or software) that has not been approved or
top three combined incident types, Web Attack (Hacking), provisioned by the organization. The motivation is usually to
Distribution of True Positive incidents by threat action Unapproved hardware/software/script/workaround (Misuse) bypass certain restrictions, hence this is done without the
and Port Scan (Hacking), in the above chart make up over involvement of the IT department who would ensure correct
45% of all categorized Incidents. All three of these combined and secure configuration.
incident types remain in the same places as in the previous
External Port Scans are a very common activity and are
3.15% Navigator report, however all three did increase their
used by “legitimate” services such as Shodan or Censys for
percentage share of incidents quite considerably.
6.60% example.
Web Attacks are where an attacker will try and abuse
30.32% Hacking However, they are also a common technique used by threat
a weakness or vulnerability in a website or web-based
actors in the reconnaissance phase of an attack.
7.15% 30.32% 16.61% Misuse application. These will commonly include SQL injection and
Cross-Site Scripting (XSS), as well as Cross-Site Request
14.27% N/A Forgery (CSRF) attacks. Incident sources and targets
12.98% Malware The sub-action of “Unapproved hardware/software/script/ As the flow chart at the start of this chapter illustrates, we see
7.33% workaround”, which is a form of Misuse, again features in the an almost equal proportion of incidents being attributed to
7.33% Error top 3 combined incident types we detected, with 14%. In our Internal and External Actors. This is a notable shift away from
data we saw Misuse incidents which covered activities such as: last year, when Internal 'actors' featured more prominently. This
7.15% Social
▪ Suspicious PowerShell/CMD command line detected is a trend worth noting.
6.60% Other Action ▪ Honeytoken activity End user devices are (predictably) the most common assets
▪ Hacking tool detected impacted. These endpoints remain the cold-face for most
12.98% 3.15% Physical
▪ Proxy Bypass: TOR, anonymization or other contemporary attacks. But Servers also feature prominently,
and there is a general sense that attackers are reviving the 'lost'
1.60% Environmental ▪ High volume of data transferred to removable storage
art of exploiting services over the internet.
▪ Malware detected on USB devices
16.61%
▪ Connection toward a known suspicious domain/IP
address
14.27%
▪ Network reconnaissance or host scan detected
▪ Potential phishing link clicked
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

24 Security Navigator 2024 Key data of the year: Threat Detection 25
Incident sources Other & Unconfirmed Incidents
4W
Distribution of incidents by Threat Actor In addition to classifying Confirmed Incidents, our
analysts also document Unconfirmed Incidents using
the “4W” framework to the right.
Why? Why did we get an unexpected result?
We investigate questions regarding the volume of False
Positive alerts our CyberSOCs deal with later in the
17.64% report in chapter "Fake News and False Positives"
Where is the root cause of the
Where?
unexpected result located?
43.60% External
Who was the actor or entity that caused
Who?
or contributed to this unexpected result?
37.45% Internal
43.60%
17.64% Unknown Actor Which mission of the security incident
What?
management chain was impacted?
0.81% Other
How? How was the improvement handled?
0.50% Partner
37.45%
Incident targets False Positive types
Distribution of incidents by impacted asset Distribution of incidents that raised an alert but turned out to be harmless
3.42%
27.70% End user device
6.34%
5.14%
27.34% Server 78.79% Legitimate activity / application
27.70%
5.76% 18.77% Unknown Asset 9.64% 9.64% Unknown
6.78% Account 6.34% Incorrect data / Misconfiguration
6.78% 3.42% Infrastructure
5.76% Network
1.61% Error in correlation rule
5.14% Multiple
0.10% Service
2.84% Other
0.08% Other
2.65% People
18.77%
0.01% N/A
1.56% Media
78.79%
27.34%
1.46% Cloud
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

26 Security Navigator 2024 Key data of the year: Threat Detection 27
Incidents by industry Incidents by industry
Breakdown of incidents analyzed by customer industry  Incidents by industry, normalized using the Coverage Score  Confirmed Incidents (TP adjusted) Other (adjusted) Coverage Score
|     | 32.43% Manufacturing | 50% |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
21.73% Retail Trade
|     | 9.84%  Professional, Scientific, and  | 45% |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        Technical Services
3.80%
8.55% Finance and Insurance
4.17% 40%
6.52% Accommodation and Food Services
5.83% 5.83% Public Administration
35%
32.43%
4.17%  Transportation and Warehousing
6.52% 3.80% Health Care and Social Assistance
30%
3.63% Real Estate and Rental and Leasing
|     | 1.08%  Information | 25% |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.74%  Construction
8.55% 0.45%  Other Services (except Public
20%
        Administration)
0.41%  Mining, Quarrying, and Oil and
        Gas Extraction
15%
0.33% Educational Services
0.23% Utilities
9.84% 10%
0.09% Wholesale Trade
0.08% Management of Companies
| 21.73% |         and Enterprises | egarevoc |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------ | ----------------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
5%
0.05%  Administrative and Support and Waste
        Management and Remediation Services
|     | 0.04%  Agriculture, Forestry, Fishing and Hunting |      | 0 %     |             |             |           |           |       |         |         |         |          |        |           |            |          |            |
| --- | ------------------------------------------------- | ---- | ------- | ----------- | ----------- | --------- | --------- | ----- | ------- | ------- | ------- | -------- | ------ | --------- | ---------- | -------- | ---------- |
|     |                                                   |      | g       | e           | c ,         | n e       | e         | g     | s       | g n     | n       | n n      | ) s    | e         | s          | e g      | n Services |
|     |                                                   |      | ctur in | a d         | t ifi e s t | i o n c   | n c s     | i n c | e s i n | t i o   | t i o   | t io i o | ti e   | s t       | s s e      | a d t in | ti o       |
|     |                                                   |      |         | T r         | e n i c r a | r a       | ta u      | r v i | a       | m a     | u c a   | c a t    | t i li | W a c e   | rp r i T r | u n      | e a        |
|     |                                                   |      | fa      | a i l   c i | r v s t     | s u       | s i s h o | Se    |  L e    | r       | t r t r | s t r    | U      | d   v i   | e l e      | H        | c r        |
|     |                                                   | Manu | e       | t   S       | S e i n i   | I n A s   | r e       | d     | d       | f o n s | E x     | n i      |        | n e r     | n t s a    | d        | R e l      |
|     |                                                   |      | R       | a l , a     | l   m       | n d   l   | W a       | o o   |  a n    | I n C o | s       | m i      | t   a  | n   S   E | l e        | a n d    |   n a      |
Incidents by Industry We perform a simple modification on the Incident volumes  o n i c A d a c i a d   F a l G a A d o r o n d h o g   n t io
|     |     |     |     | s i h n | c   c e   | o   | n n d   | n t |     |     | d   c   |     | p p a t | i   a | W h | i n ,  a | c a |
| --- | --- | --- | --- | ------- | --------- | --- | ------- | --- | --- | --- | ------- | --- | ------- | ----- | --- | -------- | --- |
to factor in the relative level of coverage: Divide the incident  e s e c b l i n d   S n   a a R e a n b l i u d i e s i s en t u
|     |     |     | o f |   T P u | n a | n io | o n   | d   |     | il   | u   | d   |   S m e | a n i |   F | m   | E d |
| --- | --- | --- | --- | ------- | --- | ---- | ----- | --- | --- | ---- | --- | --- | ------- | ----- | --- | --- | --- |
Another key factor we take into consideration is which vertical  P r n d F i e   a a t t i a n   O t   P n e p r y , in
count by the assessed coverage score and multiply it by the  a a r o r t d a e   n d e p e   a   R m e s t t a
our customers are operating in. As can be seen above, the  C p m o a t ,  a x c ti v n d C o o r e r
maximum possible score. Put simply, the lower a client’s  h   n s m E st g e a   a o f   F n t
|     |     |     |     |     | a l t | r a o | l   |     |     | y i n es   | (   | s t r n t | t   |     | e ,   ,   E |     |     |
| --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | ---------- | --- | --------- | --- | --- | ----------- | --- | --- |
Manufacturing sector is by far the largest contributor in terms  assessed coverage score is, the more this adjustment will  H e T c c e a r r c n i m e e n u r ts
|     |     |     |     |     |     | A   | R   |     | u a | r v i | m   | i e m |     | u l t | A r |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- |
of Confirmed Incidents our analysts handled, following the  ‘boost’ the number of incidents in this comparison. For a client  Q S e A d a g g e ic
|     |     |     |     |     |     |     |     |     | g ,  | r   |     | a n n a |     | g r |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | ------- | --- | --- | --- | --- | --- |
same trend as recent years. With Retail Trade & Professional,  with the maximum possible level of coverage, we will simply  n in h e M M a A
M i O t
Scientific and Technological Services completing the top 3, we
reflect the actual number of incidents we observed.
can easily see that just 3 Industries are responsible for almost
Using this simple calculation, we can now consider how
two thirds of the Confirmed Incidents we responded to.
businesses and industries compare with their relative levels of
Where available, the Assessed Coverage Score can be used to  coverage taken into account.
review our comparison of Incident levels across Industries and
Business Size.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

28 Security Navigator 2024 Key data of the year: Threat Detection 29
Incidents
by business size
|     |     |     |     |     | Business Size |     | Employee Count |     |     |
| --- | --- | --- | --- | --- | ------------- | --- | -------------- | --- | --- |
We correlate certain demographics of our customers with the
| incidents we investigate. One of the key demographics we take  |     |     |     |     | Small |     | 1-49 |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | ----- | --- | ---- | --- | --- |
into account is the Business Size.
|     |     |     |     |     | Medium |     | 50-249 |     |     |
| --- | --- | --- | --- | --- | ------ | --- | ------ | --- | --- |
We map our detected incidents not only through classifications
but also by connecting certain ‘demographics’ of the customer
| profile to them - one of these is organization size. Based on the  |     |     |     |     | Large |     | 250-10,000+ |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | ----- | --- | ----------- | --- | --- |
OECD business size scale we differentiate between business
sizes as in the table to the right.
Incidents by business size
|       |       | Hacking | Misuse | Malware | Other Action | Error | Social | Physical Environmental | Unknown |
| ----- | ----- | ------- | ------ | ------- | ------------ | ----- | ------ | ---------------------- | ------- |
| 0.91% | 0.60% |         | 3.49%  | 1.94%   | 0.97%        |       |        | 2.73%                  | 0.71%   |
3.79%
5.48%
| 7.90% |     |     |     | 5.45% |     |     |     |     |     |
| ----- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
23.53%
7.36%
6.53%
8.44%
9.11%
|     |     |     | 9.11% |     |     | 45.81% |     |     |     |
| --- | --- | --- | ----- | --- | --- | ------ | --- | --- | --- |
48.47%
11.65%
|     | Small |     |     | Medium |     |     | 11.05% | Large |     |
| --- | ----- | --- | --- | ------ | --- | --- | ------ | ----- | --- |
10.38%
21.06%
17.17%
|                                       |     |     |                                      | 16.32% |     |     |                                            | 18.95% |     |
| ------------------------------------- | --- | --- | ------------------------------------ | ------ | --- | --- | ------------------------------------------ | ------ | --- |
| For our clients who are categorized   |     |     | Hacking is again the highest cause   |        |     |     | With our large customers the pattern       |        |     |
| as Small, slightly under 50% of the   |     |     | of Confirmed Incidents for our       |        |     |     | remains similar in terms of the threat     |        |     |
| Confirmed Incidents were as a result  |     |     | Medium sized customers, albeit with  |        |     |     | actions making up the top 3. However       |        |     |
| of Hacking activity.                  |     |     | a slightly reduced proportion. When  |        |     |     | there has been a fairly significant shift  |        |     |
|                                       |     |     | combined, the Misuse & Malware       |        |     |     | in the proportions. The threat actions     |        |     |
|                                       |     |     | threat actions were responsible for  |        |     |     | of Misuse (21.06%) and Malware             |        |     |
|                                       |     |     | just over 25% of incidents for this  |        |     |     | (18.95%) now make up over 40% of           |        |     |
|                                       |     |     | category of organization, which is   |        |     |     | confirmed incidents between them,          |        |     |
|                                       |     |     | still considerably lower than those  |        |     |     | whereas Hacking has now dropped to         |        |     |
|                                       |     |     | categorized as Hacking.              |        |     |     | 23.53%.                                    |        |     |
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

30 Security Navigator 2024 Key data of the year: Vulnerbility Scanning 31
| Vulnerability Scanning                                        |     |     |                                                             |     |     | Age of findings                                                 |     |     |      |             |             |
| ------------------------------------------------------------- | --- | --- | ----------------------------------------------------------- | --- | --- | --------------------------------------------------------------- | --- | --- | ---- | ----------- | ----------- |
|                                                               |     |     |                                                             |     |     | Average and maximum age of the vulnerabilities found (in days)  |     |     |      | Average age | Maximum age |
| To be effective at vulnerability management one must be able  |     |     | Penetration Testing is generally considered a component of  |     |     |                                                                 |     |     |      |             |             |
|                                                               |     |     |                                                             |     |     | 1600                                                            |     |     | 1486 | 1486        |             |
1441 1441
| to address those items that may have the biggest impact    |     |     | Vulnerability Management, but could also be seen as a form of   |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| on the business in a meaningful way. This requires timely  |     |     | Threat Intelligence that businesses should leverage as part of  |     |     |     |     |     |     |     |     |
1400
| threat intelligence that is accurate and concise, combined  |     |     | their proactive defense strategy.  |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
with efficient vulnerability scanning results in a capability that
A capable Ethical Hacker demonstrates value through clear
| empowers teams responsible for managing exposure and  |     |     |     |     |     | 1200 |     |     |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
communication with actionable feedback that empowers the
associated risks.
client and instills trust.
1000
The Orange Cyberdefense Vulnerability Operations Center
(VOC) monitors our customers' exposure to current threats and
Vulnerability Scanning
| how open their environment is to potential risks.  |     |     |     |     |     | 800 |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Findings by Severity
This year we revisit the menacing vulnerability theme with an
600
| eye on the ever present and lingering tail of unresolved system  |     |     | The chart on the bottom of the next page shows the long  |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
weaknesses. The waves of newly discovered serious issues
tail of unresolved real findings. Examining the severity rating
| joust for our attention with existing unresolved issues, seeming  |     |     |     |     |     | 400 |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
share per unique Finding we see that the bulk of unique
like a hydra that keeps on growing new snaking heads as soon  Findings, 79%, are classified as ‘High’ or ‘Medium’. However,  208
185
| as you dispatch others.  |     |     | it is also worth noting that half, 50.4%, of unique Findings are  |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
|                          |     |     |                                                                   |     |     | 200 | 88  | 82  |     |     |     |
considered ‘Critical’ or ‘High’.
Assessing whether a system is adequately protected is a
challenge that requires skill and expertise and can take a lot
|     |     |     | The average number of ‘Critical’ or ‘High’ Findings has  |     |     | 0   |     |     |     |     |     |
| --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
of time. But we want to learn of any weaknesses beforehand  Critical High Medium Low
decreased by 52.17% and 43.83% respectively compared to
| rather than having to deal with the fallout of an unplanned “free  |     |     | our previous published results. An improvement can also be      |     |     |                                                                |     |                                                           |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --------------------------------------------------------------- | --- | --- | -------------------------------------------------------------- | --- | --------------------------------------------------------- | --- | --- | --- |
|                                                                    |     |     |                                                                 |     |     | The majority, 78%, of Findings rated ‘Critical’ or ‘High’ are  |     | But should this be a concern when only 0.71% of critical  |     |     |     |
| pentest” by a random Cy-X group.                                   |     |     | observed for Findings with severity ratings ‘Medium’ and ‘Low’  |     |     |                                                                |     |                                                           |     |     |     |
|                                                                    |     |     |                                                                 |     |     | 30 days or younger (when looking at a 120-day window).         |     | findings are 660 days or older?                           |     |     |     |
being down 29.92% and 28.76%. As this report uses a slightly
The role of the Ethical Hacker is to conduct Penetration  Conversely, 18% of all findings rated ‘Critical’ or ‘High’ are 150-
Tests – to emulate a malicious attacker and assess a system,  different sample of clients to last year, a YoY comparison has  Overall, Critical findings constitute only 0.37% of all real
days or older. From prioritization perspective ‘Critical’ or ‘High’
|     |     |     | limited value, but we believe clients are responding to the  |     |     |     |     | findings. |     |     |     |
| --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --------- | --- | --- | --- |
application, device, or even people for vulnerabilities that could  real findings seem to be dealt with swiftly, but some residual
findings we report.
be used to gain access or deny access to IT resources.  still accumulates over time.
We see therefore that unresolved Findings continue to grow
older. Indeed, ~35% of all unique CVEs are from findings 120
days old, and older.
| Severity of findings |     |     |     |     |     | Age vs. Severity of findings |     |     |     |     |     |
| -------------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
Average findings per unique asset and total severity distribution  Proportions of severity along the age axis (in days)
|     |     |     |     | Critical High | Medium Low |     |     |     |     | Critical High | Medium Low |
| --- | --- | --- | --- | ------------- | ---------- | --- | --- | --- | --- | ------------- | ---------- |
25
400000
21.93
11.2% 9.4%
350000
20
300000
250000
15
12.95
200000
| 10  |     |     |     |     | 41.0% | 150000 |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- | --- |
38.4%
7.05
100000
4.34
5
50000
0
0 0 06 021 081 042 003 063 024 084 045 006 066 027 087 048 009 069 0201 0801 0411 0021 0621 0231 0831 0441
| Critical                        | High | Medium | Low |     |     |     |     |     |                            |     |     |
| ------------------------------- | ---- | ------ | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
| © Orange Cyberdefense 2023/2024 |      |        |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |

32 Security Navigator 2024 Key data of the year: Vulnerbility Scanning 33
Findings by Asset Exposure Finding Severity by target exposure Industry perspective Our clients in the Construction industry appear to be
performing exceptionally well compared to clients in other
We can also examine the average severity rating of Findings per  Critical High Medium Low The high average numbers of ‘Critical’ and ‘High’ findings are
industries, with an average of 12.12 Findings per Asset. At the
unique Asset which are classified as External or Internal to an  60 largely influenced by assets running Microsoft Windows or
opposite end of the spectrum, we have the Mining, Quarrying,
organization. Both Internal and External assets have a similar  Microsoft Windows Server operating systems. Assets running  and Oil and Gas industry, where we report an average of 76.25
number of Medium findings at approximate 31%. Internal  operating systems other than Microsoft such as Linux based  unique findings per asset. Clients in Public Administration
50
Assets have on average 23.38 Findings rated 'High', and 15.6  OS are present, but these are reported proportionally far less.  surprised us by outperforming Finance and Insurance with
findings rated Medium. Although External assets only have 3.77
|                                                                     |     |     |     |     | We should note, however, that the ‘Critical’ or ‘High’ findings  |     |     |     |     |     | an average of 35.3 Findings per Asset, compared with 43.27,  |     |     |     |     |     |
| ------------------------------------------------------------------- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- |
| Unique Findings rated 'Critical', it is proportionally much higher  | 40  |     |     |     |                                                                  |     |     |     |     |     |                                                              |     |     |     |     |     |
despite the larger number of Assets. Of course, these values
associated with assets running Windows are not necessarily
than the 'High' severity for External Assets (18.7%). Internal  derived from the set of clients present in our sample, and may
vulnerabilities in the operating system but can also be related to
assets have 7.18 average Findings for unique assets rated  30 not represent the universal reality.
applications running on the asset.
'Critical', this is very close to the overall average.
By comparing the ratio of Total CVSS3 Base Score per Asset
It is perhaps understandable that unsupported Microsoft
20
|     |     |     |     |     | Windows and Windows Server versions are prominent here, but  |     |     |     |     |     | to the total number of Assets for a given Industry, we observe  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- |
that our clients in the Construction Industry are performing
it is surprising to find more recent versions of these operating
10 the best. In second place is Public Administration, followed by
systems with severities rated as ‘Critical’ or ‘High’.
Manufacturing that just pipped third place from Finance and
|     |     |     |     |     | The results here only consider Findings based on scans of  |     |     |     |     |     | Insurance. Mining and Quarrying and Oil and Gas along with  |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- |
0
hosts rather than services such as web applications. The
External Internal Accommodation and Food Services have ratios of between 6
|     |     |     |     |     | average unique real finding per unique asset is 31.74 for all  |     |     |     |     |     | to 7 times higher than Manufacturing. Industries with Unique  |     |     |     |     |     |
| --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- |
Findings by Asset Type Finding Severity by target type organizations, denoted by the dashed horizontal line in the  Assets below 500 may not yield meaningful results.
chart below.
| Another approach is to consider the scanning engine used to    |     |     | Critical High | Medium Low |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | ------------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| distinguish between assets classes. We can create two groups,  | 50  |     |               |            |     |     |     |     |     |     |     |     |     |     |     |     |
namely ‘Web’ and ‘Infrastructure’. The group classified as
45
Infrastructure yield average scores per severity rating nearly
| identical to the overall average. Assets classified as Web have  | 40  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
proportionally, much lower severity rating of ‘High’ on average.
35
Findings per asset by industry
Assets classified as External and Web do seem to have fewer
30
impactful Findings on average compared with assets falling in  Average Unique Findings per Unique Asset by Industry
|     | 25  |     |     |     |     |     |     |     |     |     |     |     | Avg. CVSS score | Avg. Findings per asset |     | Unique assets |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------- | ----------------------- | --- | ------------- |
the Internal and Infrastructure groups, especially for Findings
with a Severity rating of 'High'. This would suggest that External  20 5,921
and Web assets are enjoying priority when getting Findings  6,000 600
|     | 15  |     |     |     |     |     | 5,564 |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
resolved.
10
5
|     |     |     |     |     | 5,000 |     |     |     |     |     |     |     |     |     |     | 500 |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0
Infrastructure Web
|     |     |     |     |     | 4,000 |     |     |     |     |     |     |     |     |     |     | 400 |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Criticality of findings by Operating System
3,216
3,048
| Critical & High Findings by Target Operating System  |       |      |       | Critical High |       |     |     |     |     |     |     |     |     |     |     |     |
| ---------------------------------------------------- | ----- | ---- | ----- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                      |       |      |       |               | 3,000 |     |     |     |     |     |     |     |     |     |     | 300 |
| 62.3%                                                | 13.7% | 8.8% | 52.1% |               |       |     |     |     |     |     |     |     |     |     |     |     |
|                                                      |       |      |       |               | 2,000 |     |     |     |     |     |     |     |     |     |     | 200 |
1,295
|     |     |     | 2R 2102 revreS swodniW |     |       |                 |     |                |               |     |         |           | 950            |     |            |     |
| --- | --- | --- | ---------------------- | --- | ----- | --------------- | --- | -------------- | ------------- | --- | ------- | --------- | -------------- | --- | ---------- | --- |
|     |     |     |                        |     | 1,000 |                 |     | 641            |               |     |         |           |                |     |            | 100 |
|     |     |     |                        |     |       |                 |     |                |               |     |         | 100       |                |     |            | 179 |
|     |     |     |                        |     |       |                 |     |                |               |     | 1       |           |                |     | 9          |     |
|     |     |     |                        |     | 0     |                 |     |                |               |     |         |           |                |     |            | 0   |
|     |     |     | Windows 10             |     |       |                 | e   |   ministration | Manufacturing |     |         |           |   Construction |     | n Services |     |
|     |     |     |                        |     |       | n g   d Insuran | c   | n d            |               |     | n d     | p t       | ifi c ,        |     | io         |     |
|     |     |     |                        |     |       | y i n d n       |     |  a e s         |               |     |   a c e | c e o n ) | n t es         |     | mat        |     |
Windows Server 2008 R2 a r r   a o o n v i c r e a n  (e x t i ie v ic Infor
|     |                     |                               | 24.1%                  |                |          | Q u O i l c ti |     | a ti e r  |     | C     | a is t   | s t r a     | S c e r |     | ucational  |     |
| --- | ------------------- | ----------------------------- | ---------------------- | -------------- | -------- | -------------- | --- | --------- | --- | ----- | -------- | ----------- | ------- | --- | ---------- | --- |
|     |                     |                               |                        |                | Mining,  | d   r a        | mo  | d S       |     | h     | s s      | ic e in is  | l,   S  |     |            |     |
|     |                     |                               |                        |                |          | a n E x t an   |     | o d   A d |     | a lt  | A v      | m n a       | a l     |     |            |     |
|     | 4.9% 4.2%           | 8.9%                          |                        |                |          | s   e          | m   | o ic      |     | He a  | l  S e r | d i o       | n ic    |     |            |     |
|     |                     |                               |                        |                |          | G a n c        | co  | F b l     |     | o c i | r        |   A s s c   | h       |     |            |     |
|     |                     |                               |                        |                |          | n a            | c   | P u       |     | S     | h e l ic | f e e       |         |     | E d        |     |
|     |                     |                               |                        |                |          | F i            | A   |           |     |       | O t u b  | P r o d   T |         |     |            |     |
|     |                     |                               | Windows Server 2008 R2 |                |          |                |     |           |     |       | P        | n           |         |     |            |     |
|     | 9102 revreS swodniW | 6102 revreS swodniW Windows 7 |                        |                |          |                |     |           |     |       |          | a           |         |     |            |     |
|     |                     |                               | 8.9%                   | 4 .6    % 2.8% |          |                |     |           |     |       |          |             |         |     |            |     |
|     |                     | 1.4% 1.1%                     |                        | W i n dows     |          |                |     |           |     |       |          |             |         |     |            |     |
|     |                     | Win Srv.                      |                        | Win 7          |          |                |     |           |     |       |          |             |         |     |            |     |
Server
|                                 |     |  swodniW 2008 | swodniW   | 2016         |     |     |     |     |     |     |     |     |     |                            |     |     |
| ------------------------------- | --- | ------------- | --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
|                                 |     |  revreS       |   2R 2102 | Win Srv.     |     |     |     |     |     |     |     |     |     |                            |     |     |
|                                 |     |   2202 0.7%   |    revreS | 3.8 %        |     |     |     |     |     |     |     |     |     |                            |     |     |
|                                 |     |               |           | 2008         |     |     |     |     |     |     |     |     |     |                            |     |     |
| Windows 10                      |     |               |           | Win Srv. ... |     |     |     |     |     |     |     |     |     |                            |     |     |
|                                 |     | Linux         |           | 2019         |     |     |     |     |     |     |     |     |     |                            |     |     |
| © Orange Cyberdefense 2023/2024 |     |               |           |              |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |

34 Security Navigator 2024 Key data of the year: Vulnerbility Scanning 35
?
Age of findings by industry
Research Question:
Average and max. age of Unique Findings for different verticals (ordered by average)
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Average age |     | Maximum age |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------- | --- | --- | --- | --- |
1,600
Can we reproduce the findings of other
researchers on the effectiveness of EPSS, but on
1,400
the vulnerabilities reported to our own clients?
1,200
1,000 We are unable to reproduce the findings of other researchers using our own vulnerability and
EPSS datasets, which shows how context-sensitive vulnerability intelligence is. However, EPSS
has been shown to be a more effective alternative to CVSS when making remediation decisions,
800
especially in terms of Coverage
600
369.22
EPSSolutely Vulnerable Included in this group are 34 CVEs that have an CVSS score of
| 400 |     |     |     | 267.18 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
244.05 8, and some with scores as high as 9.8. In other words, a skilled
|     |     |     |     |     |     |     | 198.77 |     | 195.29 | 183.82 |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
150.18 147.59 An estimated 4.1 to 5.5% of all vulnerabilities in 2020 were  attacker matching our Penetration Testing team’s skill would
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | 123.99 |     | 122.1 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ----- | --- | --- | --- | --- | --- |
200 found to be exploitable[41][42]. Given that fewer than 10% of
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 54.3 | have found 177 potentially serious vulnerabilities that would  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | -------------------------------------------------------------- | --- | --- | --- |
reported vulnerabilities are likely to ever be exploited by an
probably not have been prioritized using EPSS.
0 attacker in the wild, and given that most enterprises are never
|     |     | n   | d   |     | d   |     | ,   | t   | ministration | Manufacturing |     | Services |     | g   |     | n d Insurance |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | --- | -------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
matio n es n e fi c s e p n) in   Construct io a b l e   t o   p a t c h   m o r e   t h a n   ~ 1 5 % [ 4 3 ]   o f   t h e   v u l n e r a b i l i t i e s   o n  t h e ir
|     |     |     | n  a ic |     | e  a c | n t i | ic e | x c o |     |     |     |     |     | r y n d |     |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | ------ | ----- | ---- | ----- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
Infor o rv a r a n ie v  (e a t i a r l  a ion n e t w o r k s ,   d e t e r m i n i n g   w h a t   v u l n e r a b i l i t i e s   to   p r io r i t i z e   b e c o m e s  C V S S   v s   E P S S   o f   C V E   F i n d i n g s
|     |     |     | a ti e | C   | i s t | S c e | r   | e s is t r |     |     | Educational  |     |     | Q u O i c | t   |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | ----- | ----- | --- | ---------- | --- | --- | ------------ | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
mo d   S lt h   s s l,   l  S ic in d Mining,  d   r a ance an a n   e s s e n t i a l  f a c e t   o f   V u l n e r a b i l i t y   M a n a g e m e n t .
o d a l  A n a ic a r v m A a n x t in  pe ne tr a t io n  te s ts
m F o He i a s i o n S e A d lic    E A v era ge  C VS S Average EPSS
|     |     | cco |     | o c | s   | c h | r  ic   | u   | b   |     |     |     |     | a s |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A S o f e T e th e b l P G in T h e   E x p l o i t   P r e d i c t i o n   S c o r i n g   S y s t e m   ( E P S S ) [ 4 4 ]   w a s   p r e s e n t e d
|     |     |     |     |     | P r d   | O   | u   |     |     |     |     |     |     |     |     | F   |     |     | Ap p lic a ti | on  Se cu ri ty |     |
| --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --------------- | --- |
a n P b y   t h e   F I R S T   o r g a n i z a t i o n   a t   t h e   B l a c k H a t   c o n f e r e n c e   i n
2019[45], and seeks to provide clear, accurate predictions
| When comparing the average severity per unique asset per  |     |     |     |     |     |     |     |     |     | Similarly, Finance and Insurance with Accommodation and  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
on whether vulnerabilities are likely to be exploited. EPSS
| I n | d u st ry   | w e  s e e |  a  m ix e | d  p i c tu | re . W e  c | a n  i g n | o r e  H e | a l th   Care  |     | F o o d  S | e r vi c e | s   a ls o  o v | e r s h o t |   t h e   o v e | r a l l  a v e r | a g e   b y  | 1 0 .2  a n d  |     |     |     |     |
| --- | ----------- | ---------- | ---------- | ----------- | ----------- | ---------- | ---------- | -------------- | --- | ---------- | ---------- | --------------- | ----------- | --------------- | ---------------- | ------------ | -------------- | --- | --- | --- | --- |
promises to become an invaluable source of intelligence that  10.00
| a n | d  S o c | i al  A s s is | ta nc e |  a n d   In | fo rm at io | n ,  w i th |   a   re la ti | v e ly   |     | 3. 4  fi n d | in g s   p | e r  u n iq u | e   a s s e t |   r e s p e c | t i v e l y .  T | h e   s a m | e   th re e   |     |     |     |     |
| --- | -------- | -------------- | ------- | ----------- | ----------- | ----------- | -------------- | -------- | --- | ------------ | ---------- | ------------- | ------------- | ------------- | ---------------- | ----------- | ------------- | --- | --- | --- | --- |
can inform defenders' decisions, by illuminating vulnerabilities  8.00
| small unique asset count, that results in averages that are  |     |     |     |     |     |     |     |     |     | Industries exceeded the overall average for findings rated  |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that are more likely to be exploited within 30 days of a given  6.00
| disproportionate in relation to other Industries.  |     |     |     |     |     |     |     |     |     | Critical, with Accommodation and Food Servers doing so by  |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
date[46].
|     |     |     |     |     |     |     |     |     |     | almost a factor of 3.  |     |     |     |     |     |     |     | WebApp | 4.00 |     | External |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | ------ | ---- | --- | -------- |
Our overall Industry average for Severity rating High is 21.93
EPSS scores are calculated by a complex algorithm using  2.00
and by that number Mining, Quarrying and Oil and Gas
real-time intelligence from multiple sources to help defenders
0.00
Extraction has more than double that average.
strike the optimal balance between coverage and efficiency.
A judicious application of the EPSS predictions should result in
Criticality of findings by industry
no exploitable vulnerabilities getting missed, while avoiding the
‘wasted effort’ of patching or mitigating issues that aren’t ever
Average Severity per Unique Asset per Industry (ordered by most critical)  exploited.
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | Critical |     | High Medium | Low |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | ----------- | --- | --- | --- | --- | --- |
90
Predicting Hacking
Mobile Internal
80
EPSS provides a metric that can be used to inform prioritization
strategies. Each of the 212,443 available CVE is assigned an
70 This serves as a reminder that EPSS is a general model with
EPSS score from between 0 and 1 daily, based on fresh data
certain limitations in terms of context. Penetration Tests, on the
and intelligence. For example, only 6,838 CVS have an EPSS
60 other hand, can look deeper into an environment to produce
score greater than or equal to 0.4, which is approximately 3.2%  findings that may not be considered in the algorithm that
50 of all CVE. Choosing an EPSS score threshold can determine
produces EPSS scores.
which CVEs are mitigated or left, depending on the use case.
| 40  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Leveraging additional capabilities such EPSS can assist  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
Ethical Hacking, as a form of vulnerability identification and
vulnerability management teams to focus on what is likely to
prioritization, can also be thought of as a source of highly  be exploited. An effective vulnerability management process
30
contextual vulnerability intelligence. So how do these two
should also use the intelligence produced by Penetration
sources of intelligence compare?
| 20  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Testing to augment other vulnerability management data.  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
The chart to the right shows a mix of project types with 29
10 CVEs reported that have an EPSS score of 0.4 or higher,
grouped by project type. The CVSS scores vary from as low as
0
3 to a max of 10.
|     | io n |     | d      | g     |               | c e | io   | n   | c ,   Manufacturing |     |            | o n | e s | p t |     | an d | d       |     |     |     |     |
| --- | ---- | --- | ------ | ----- | ------------- | --- | ---- | --- | ------------------- | --- | ---------- | --- | --- | --- | --- | ---- | ------- | --- | --- | --- | --- |
|     | mat  |     |  a n s | y i n | d   d Insuran |     | ra t |     | ifi es              |     | Constructi |     | vic | c e | n ) |   g  |  a n ce |     |     |     |     |
n ic e r r a n n minist ie n t ic Ser  (e x i o o n sin e n P e r h a p s   m o s t  i m p o r t a n tly ,   a   t o t a l   o f   1 7 7   (8 5 .9 2 % )  C V E s   w e re
|     | Infor | ti o | rv  | u a i l  | io  |     |     | c   | r v |     |     |     |     | r at | ta ti | o u | C a r ta |     |     |     |     |
| --- | ----- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ----- | --- | -------- | --- | --- | --- | --- |
d a S e ning,  Q O c t   S S e ucational  e s is t por h h   s is r e p o r t e d   b y   o u r  t e s t e r s  b u t   h a v e   a n   E P S S  s c o r e o f  le s s   t ha n
|     |     | mo d  |     | n d   t | r a n |         | d   | a l,   | a l  |     |     |     |     | v ic in | a r e | lt  | A s  |     |     |     |     |
| --- | --- | ----- | --- | ------- | ----- | ------- | --- | ------ | ---- | --- | --- | --- | --- | ------- | ----- | --- | ---- | --- | --- | --- | --- |
|     |     | m o o |     | a E x   | e  a  | blic  A |     | o n ic |      |     |     |     | e r | d m     | n s W | e a | a l  |     |     |     |     |
co F M i s   c s i h n r  S A ra H c i 0 . 4 ,  a n d   s o  a r e   n o t   p r e s e n t   in   t h i s   c h a rt .
|     | c   |     |     | G a a | n   | u   | e     | s e c |     |     |     | d   | e ic   |     | T   | S o |     |     |     |     |     |
| --- | --- | --- | --- | ----- | --- | --- | ----- | ----- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
|     | A   |     |     | F i n |     | P   | r o f |   T   |     |     |     | E   | th b l |     |     |     |     |     |     |     |     |
|     |     |     |     |       |     |     | P     | n d   |     |     |     |     | O P u  |     |     |     |     |     |     |     |     |
a
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |

36 Security Navigator 2024 Key data of the year: Vulnerbility Scanning 37
Science comes to Target exploit group is the collection of vulnerabilities that is The chart below illustrates the outcomes of our efforts to These two thresholds were selected by aiming for an Effort of
believed to be exploited and must therefore be patched. This replicate the Jacobs et al. analysis, using the more ‘local’ approximately 15%, which other research shows is a pragmatic
Vulnerability Management
is a subset of the total vulnerability population. We derive this perspective provided by our own data. Their data and paper level for most organizations.
subset by matching our client’s vulnerabilities with either: serve as the benchmark against which our replicated tests can
In a seminal paper titled ‘Enhancing Vulnerability Prioritization: Notice that for the same level of Effort, the First EPSS strategy
Data-Driven Exploit Predictions with Community-Driven ▪ our own internal ‘VulnWatch’ Exploit Database be compared. These are labelled ‘First CVSS’ and ‘First EPSS’ achieves Coverage of 90% and Efficiency of 24.1%, far better
Insights’[47], Jacobs et al. consider how EPSS can be used (EDB) (n = 439) respectively. than the CVSS strategy, which only achieves 33.5% and 6.1%
to derive and evaluate patching strategies by using Effort, ▪ A list of CVE reported by our Ethihical Hackers on clients' The First CVSS and the First EPSS Analysis assess the Effort, respectively.
Coverage, and Efficiency as metrics[48]. estates (n = 482), or Coverage, and Effort for strategies involving vulnerabilities with
How much time (Effort) must be invested to get all relevant ▪ The CISA Known Exploited Vulnerabilities list a CVSS score of 9.1 or higher (First CVSS), and an EPSS score
vulnerabilities patched (Coverage) while ensuring that we do (KEV) (n = 465). of 0.022 or higher (First EPSS).
not waste resources on patching less impactful vulnerabilities Remediation group is the collection of vulnerabilities that
(Efficiency)? must be patched according to the selected strategy. This is a
subset of the vulnerability population and can overlap with the Strategy Analysis
The paper by Jacobs et al. is a rare example of the application
target exploit group.
of real science and data to a problem in our industry. The depth
and breadth of the work exceeds anything we could hope to EPSS score is the temporal score calculated by the EPSSv3 Comparing Vulnerability Prioritization Strategies in our Client context Efficiency Coverage Effort
present here, but it outlines some concepts and conclusions Machine Learning model that predicts the likelihood of the
that are incredibly far-reaching and offer a base from which we vulnerability being exploited within the next 30 days.
can endeavor to build further. Strategy is how we select the vulnerabilities to be included in FIRST CVSS
the remediation group. In our case this will be done by using
In a section titled ‘Simple Remediation Strategies’ the paper’s
authors endeavor to ‘compare the amount of effort required the Common Vulnerability Scoring System (CVSS) version 3 FIRST EPSS
score or the EPSS score.
(as measured by the number of vulnerabilities needing to be
remediated) for differing remediation strategies… [and highlight] Coverage is the percentage of remediated vulnerabilities
the performance of 6 simple (but practical) vulnerability that were that is also present in the target exploit group. For EPPS (0.085) KEV EDB
prioritization strategies based on [their] test data’. example, if 15 vulnerabilities are present in the target exploit
group and the strategy led to 5 being remediated, then
They posit that patching only vulnerabilities with an EPSS score EPSS (0.085) VulnWatch EDB
Coverage is 33.3%.
of 0.022 (2.2% probability) or above, would require only 15.3%
Efficiency is the number of remediated vulnerabilities from the
of all vulnerabilities to be patched (aligning with the pragmatic
target exploit group as a proportion of the total remediation EPPS (0.085) Pentest EDB
real-world observation mentioned above) and result in 90.4% of
group. If we patch 100 vulnerabilities in total but only 5 are
exploitable vulnerabilities being mitigated, at an efficiency level
considered exploitable, then our efficiency is 5%.
of 24.1%. KEV EDB CVSS
Effort is expressed as the number of vulnerabilities in the
This intelligent and encouraging finding required the
remediation group that will be patched as a percentage of the
researchers to define some concepts and parameters: vulnerability population. If the total number of vulnerabilities in KEV EDB EPSS
▪ First, they needed a ‘population’ of existing vulnerabilities consideration is the entire CVE pool of 212,443 and our strategy
that represents the combination of everything that could requires us to patch 21,245 vulnerabilities, then the Effort is VulnWatch EDB CVSS
and should be patched. Jacobs et al. used the entire CVE 10%.
set at the time of writing as their population.
The EPSS paper provides quantitative examples of evaluating
▪ Next, they need a ‘target’ exploit group, which reflects all Efficiency, Coverage, and Effort for a strategy based on either VulnWatch EDB EPSS
the vulnerabilities that are known to be exploited in the CVSS or EPSS scores. In their experiment they use the entire
wild. There is no single definitive list like this at any given CVE pool as their vulnerability population. The target exploit Pentest EDB CVSS
time, however, and the Jacobs team don’t disclose what group in their paper is a set of vulnerabilities they collected
list they use in their evaluation. from various sources.
Pentest EDB EPSS
▪ Finally, they define the concepts ‘Coverage’, ‘Efficiency’ We emulate this experiment with our own vulnerability datasets.
and ‘Effort’ as the metrics that need to be balanced to Our vulnerability population is comprised of CVE identified on
evaluate the quality of a given patching strategy. client networks by our VOC scanning service. We chose three 0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%
separate target exploit groups: two are based on proprietary
Standing on the shoulders of giants vulnerability intelligence sources, namely our own ‘Vulnerability
Watch’ Exploit Database (EDB) and a Pentest EDB that is a
In an effort to apply the concepts presented by Jacobs et al. collection of CVE identified by our ethical hacking teams on
in the context of our own clients, and with our own intelligence client assignments. The third target exploit group is the CISA
about what’s being exploited, we derive the following Known Exploited Vulnerability list (KEV), which we label the
definitions: KEV EDB.
All three target exploit groups are trimmed down to intersect
Vulnerability population (n = 24,177) is the collection of all
with our vulnerability population, as some of the ‘exploited’
vulnerabilities that require consideration. Jacobs et al. used
vulnerabilities do not occur in our client environments and
the entire CVE datataset. For our purposes we use all the CVEs
would thus be of no interest to us.
present in the dataset of unpatched client vulnerability findings
we reported on in this Security Navigator.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

38 Security Navigator 2024 Key data of the year: Vulnerbility Scanning 39
|                          |     |     |     |                         |     |     |     |
| ------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- |
| FIRST example strategies |     |     |     | Patch all EPSS >= 0.022 |     |     |     |
Population Remediation group Target exploit group All CVEs CVEs above threshold Exploited
| Strategy:   | CVSS v3.x |     |     |     |     |     |     |
| ----------- | --------- | --- | --- | --- | --- | --- | --- |
24,177
| Threshold:   | 9.1+ CVSS score |     | Population |     |     |     |     |
| ------------ | --------------- | --- | ---------- | --- | --- | --- | --- |
Effort:     15.1% of CVEs  Population: All CVE in VOC results (24,177)
Known Exploited: All CVE from KEV EDB
| Coverage:   | 33.5%  |     |     |     |     |     | 5,765 |
| ----------- | ------ | --- | --- | --- | --- | --- | ----- |
Efficiency:   6.1% Remediation Threshold: 0.022+ EPSSv3 score 1
2 7
|               |                   |     |       | Effort:     | 23.84% of reported CVEs           |      | 9 0 |
| ------------- | ----------------- | --- | ----- | ----------- | --------------------------------- | ---- | --- |
|               |                   |     | group |             |                                   |      | 5   |
| Strategy:     | EPSS v3           |     |       |             |                                   |      |     |
|               |                   |     |       | Coverage:   | 63.44% of ‘exploited’ CVEs        |      |     |
| Threshold:    | 0.022+ EPSS score |     |       |             |                                   |      |     |
|               |                   |     |       | Efficiency: | 5.11% of vulnerabilities patched  |      |     |
| Effort:       | 15.3% of CVEs     |     |       |             |                                   |      |     |
|               |                   |     |       |             |   were e  xploitable              |      |     |
| Coverage:     | 90.4%             |     |       |             |                                   |      |     |
|               |                   |     |       |             |                                   |      |     |
| Efficiency:   | 24.1%             |     |       |             |                                   |      |     |
|               |                   |     |       |             |                                   |      |     |
Strategy: Patch all CVSS >= 9.1 Effort 15% with EPSS >= 0.085
All CVEs CVEs above threshold Exploited All CVEs CVEs above threshold Exploited
|     |     |     | 24,177 |     |     |     | 24,177 |
| --- | --- | --- | ------ | --- | --- | --- | ------ |
Population: All CVE in VOC results (24,177) Population: All CVE in VOC results (24,177)
Known Exploited: All CVE from VulnWatch EDB Finding Known Exploited: All CVE from Pentest EDB
4,167
Threshold: 9.1+ CVSS score 3 Threshold: 0.085+ EPSSv3 score 3,631 3
1 0 1 5
Effort: 17.24% of reported CVEs  3 1 Effort: 15.02% of reported CVEs  3 1
8 1
Coverage: 31.44% of ‘exploited’ CVEs  Coverage: 27.18% of ‘exploited’ CVEs
Efficiency: 3.31%  of vulnerabilities patched  Efficiency: 3.61% of vulnerabilities patched
|                         |   were e x ploitable |      |     |                               |   were e  xploitable |      |     |
| ----------------------- | -------------------- | ---- | --- | ----------------------------- | -------------------- | ---- | --- |
|                         |                      |      |     |                               |                      |      |     |
|                         |                      |      |     |                               |                      |      |     |
| Patch all EPSS >= 0.022 |                      |      |     | Effort 15% with EPSS >= 0.085 |                      |      |     |
All CVEs CVEs above threshold Exploited All CVEs CVEs above threshold Exploited
|     |     |     | 24,177 |     |     |     | 24,177 |
| --- | --- | --- | ------ | --- | --- | --- | ------ |
Population: All CVE in VOC results (24,177) Population: All CVE in VOC results (24,177)
Known Exploited: All CVE from VulnWatch EDB Finding 5,765 Known Exploited: All CVE from VulnWatch EDB
Threshold: 0.022+ EPSSv3 score 1 Threshold: 0.085+ EPSSv3 score 3,631 1
2 6 2 8
Effort: 23.84% of reported CVEs  7 0 Effort: 15.02% of reported CVEs  5 6
9 3
Coverage: 63.55% of ‘exploited’ CVEs  Coverage: 57.63% of ‘exploited’ CVEs
Efficiency: 4,83% of vulnerabilities patched  Efficiency: 6.97% of vulnerabilities patched
|                       |   were e  xploitable |      |     |                               |   were e  xploitable |      |     |
| --------------------- | -------------------- | ---- | --- | ----------------------------- | -------------------- | ---- | --- |
|                       |                      |      |     |                               |                      |      |     |
|                       |                      |      |     |                               |                      |      |     |
| Patch all CVSS >= 9.1 |                      |      |     | Effort 15% with EPSS >= 0.085 |                      |      |     |
All CVEs CVEs above threshold Exploited All CVEs CVEs above threshold Exploited
|     |     |     | 24,177 |     |     |     | 24,177 |
| --- | --- | --- | ------ | --- | --- | --- | ------ |
Population: All CVE in VOC results (24,177) Population: All CVE in VOC results (24,177)
Known Exploited: All CVE from KEV EDB Known Exploited: All CVE from KEV EDB 5,631
4,167
Threshold: 9.1+ CVSS score 3 Threshold: 0.085+ EPSSv3 score 1
1 2 2 9
4 1 6 8
Effort: 17.24% of reported CVEs  4 Effort: 15.02% of reported CVEs  7
Coverage: 30.97% of ‘exploited’ CVEs  Coverage: 57.42% of ‘exploited’ CVEs
Efficiency: 3.46% of vulnerabilities patched  Efficiency: 7.35% of vulnerabilities patched
|                                 |   were e  xploitable |      |     |     |   were e  xploitable |      |                            |
| ------------------------------- | -------------------- | ---- | --- | --- | -------------------- | ---- | -------------------------- |
|                                 |                      |      |     |     |                      |      |                            |
| © Orange Cyberdefense 2023/2024 |                      |      |     |     |                      |      | www.orangecyberdefense.com |

40 Security Navigator 2024 Key data of the year: Vulnerbility Scanning 41
VOC Scanning Research Notes
1.  Most notable in these experiments is that we do not report Coverage above 57.63% for any strategy, or
Efficiency of above 5.1%, against any of our EDB.
2.  Back-to-back for any dataset, EPSS out-performs CVSS in terms of Coverage, but of course Effort and  About the data Clients and Assets sampled
| Efficiency then tend to vary accordingly. |     |     |     |     |     | Industry | %   |
| ----------------------------------------- | --- | --- | --- | --- | --- | -------- | --- |
▪  2,555,515 unique findings
▪
3.  The FIRST EPSS Strategy of patching EPSS >= 0.022 requires an Effort of > 23% on our client vulnerability  0.02% of unique findings classified as False Positives
population, which is far higher than the 15.2% established by Jacobs et al.  ▪  Finance and Insurance 31.20%
23,690 unique assets
▪  Average number of unique findings per unique asset is
4.  Using the KEV EDB and the VulnWatch EDB tend to yield similar results for both strategies.
|     |     |     |     |     |     | Public Administration | 25.18% |
| --- | --- | --- | --- | --- | --- | --------------------- | ------ |
31.74 for all organizations
5.  A CVSS strategy fairs particularly poorly against the Pentest EDB, achieving 50% lower Coverage compared to  ▪  Oldest findings are 1,486 days
the EPSS strategy while requiring 7 percentage points more Effort.  Manufacturing 13.71%
▪  Average finding age is 125.81 days
▪
6.  In repeating the experiments from the Jacobs paper, we overshot the target Effort level of 15%. Our EPSS  0.37% of all unique findings are rated 'Critical’
|     |     |     |     |     |     | Construction | 12.87% |
| --- | --- | --- | --- | --- | --- | ------------ | ------ |
strategy generally required more Effort than the CVSS strategy, but of course with correspondingly better
The dataset is representative of a subset of clients that
results.
subscribe to our vulnerability scanning services. Assets
|     |     |     |     |     |     | Professional, Scientific, and Technical Services | 5.63% |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | ----- |
7.  To align with the Effort level in line with the 15% target Jacobs et al. set, we derive an EPSS strategy with a  scanned include those reachable across the Internet, as well as
score of 0.085 as a threshold. Once again, the KEV EDB and VulnWatch EDB Coverage were remarkably  those present on internal networks. The data include findings
|     |     |     |     |     |     | Mining, Quarrying and Oil and Gas Extraction | 5.47% |
| --- | --- | --- | --- | --- | --- | -------------------------------------------- | ----- |
similar, but none of the scenarios achieved more than 57.63% coverage or 7.35% Efficiency. for network equipment, desktops, web servers, database
servers, and even the odd document printer or scanning
8.  Another point to note is that these two EDBs do not intersect fully and represent different vulnerabilities. Aiming  device. Accommodation and Food Services 2.71%
for a 15% Efficiency when dealing with the Pentest EDB yielded a much lower Coverage and Efficiency score.
The number of organizations in this dataset is smaller (3 less)
|     |     |     |     |     |     | Other Services (except Public Administration) | 1.78% |
| --- | --- | --- | --- | --- | --- | --------------------------------------------- | ----- |
than the previous dataset used in Security Navigator 2023 and
Summary some organizations were replaced by new additions. With the
|     |     |     |     |     | change of organizations comes a different mix of assets which  | Educational Services | 0.76% |
| --- | --- | --- | --- | --- | -------------------------------------------------------------- | -------------------- | ----- |
The difference in the size and nature of datasets represent different perspectives of what the ‘threat’ (the
leaves comparing the previous results in the Security Navigator
list of exploitable vulnerabilities) is. This needs to be decided, then weighed up against the ‘challenge’ (the  2023 akin to comparing apples to oranges (we might be
|     |     |     |     |     |     | Transportation and Warehousing | 0.57% |
| --- | --- | --- | --- | --- | --- | ------------------------------ | ----- |
total population of vulnerabilities), and the available budget and skill, before a strategy can be selected.  biased), but it still worth noting similar patterns where possible.
EPSS provides an invaluable input into this decision-making process, but its usefulness at any given  The term unique finding is used to describe an identifier that
|     |     |     |     |     |     | Information | 0.11% |
| --- | --- | --- | --- | --- | --- | ----------- | ----- |
threshold can only be determined once the respective factors are selected.
is specific to an asset linked to a to an organization. A unique
EPSS has been shown to be a more Effective alternative to CVSS when making remediation decisions,  finding is a composition of the following attributes:
|     |     |     |     |     |     | Health Care and Social Assistance | 0.02% |
| --- | --- | --- | --- | --- | --- | --------------------------------- | ----- |
▪  Client Identifier
especially in terms of Coverage. But our Pentest EDB dataset still poses a challenge for both the CVSS and
| EPSS strategies.  |     |     |     |     | ▪  Asset Name |     |     |
| ----------------- | --- | --- | --- | --- | ------------- | --- | --- |
▪
Ethical Hacking can be thought of as a source of vulnerability intelligence that is unique in that it can  IP Address
|                                                         |     |     |     |     |     | Business size | %   |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | ------------- | --- |
| provide much better context to a specific environment.  |     |     |     |     | ▪   |               |     |
Host Type
▪
|     |     |     |     |     | Finding Name | 1-100 | 15.91% |
| --- | --- | --- | --- | --- | ------------ | ----- | ------ |
This dataset contains 2,555,515 unique findings, which is a
22.9% increase in size compared with the number of unique
| Objective | Risk Reduction |     | Threat Mitigation |     |     | 101-500 | 9.31% |
| --------- | -------------- | --- | ----------------- | --- | --- | ------- | ----- |
findings in the previous Security Navigator, even though we
have fewer client organization present this year. It is important
▪  Reduce attack surface ▪  Respond to Vulnerability Intelligence 501-1000 5.15%
to note that the total unique findings mentioned here includes
| Strategies | ▪  Deal with vulnerability classes |     | ▪  Respond to Threat Intelligence |     |     |     |     |
| ---------- | ---------------------------------- | --- | --------------------------------- | --- | --- | --- | --- |
False Positives. This year we reported a drop in the number
|     | ▪  Deal with asset classes |     | ▪  Respond to attacks |     |                                                                |           |       |
| --- | -------------------------- | --- | --------------------- | --- | -------------------------------------------------------------- | --------- | ----- |
|     |                            |     |                       |     | of False Positives to approximately 0.02% of unique findings,  | 1001-5000 | 9.75% |
compared with 1% unique findings in Security Navigator 2023.
Asset Intelligence
|              |     |                     |     |     |     | 5001-10000 | 16.14% |
| ------------ | --- | ------------------- | --- | --- | --- | ---------- | ------ |
| Intelligence |     | Attack Intelligence |     |     |     |            |        |
Terminology
|     |     | Vulnerability Intelligence |     |     |                                                             | 10001-50000 | 39.45% |
| --- | --- | -------------------------- | --- | --- | ----------------------------------------------------------- | ----------- | ------ |
|     |     | Threat Intelligence        |     |     | Findings are assigned a severity rating that can be either  |             |        |
‘Informational’, ‘Low’, ‘Medium’, ‘High’, or ‘Critical’. The
|     |     |     |     |     |     | 100001-200000 | 4.30% |
| --- | --- | --- | --- | --- | --- | ------------- | ----- |
Metrics Risk Metrics Threat Metrics ‘Informational’ severity rating can be relevant in some cases,
but this is excluded from our analysis due to its volume in
|     | E.g.                   |     |     | E.g.                            | relation to other severity rating types.  |     |     |
| --- | ---------------------- | --- | --- | ------------------------------- | ----------------------------------------- | --- | --- |
|     | ▪  Deprecate unneeded  |     |     | ▪  Patch or mitigate vulnerable |                                           |     |     |
Real findings are those findings that exclude duplicates and
|     |   systems | Upgrade entire hosts |     |   systems |     |     |     |
| --- | --------- | -------------------- | --- | --------- | --- | --- | --- |
false positives, while having a severity rating of either ‘Critical’,
|         | ▪  Deprecate unneeded  |     |     | ▪  Suspend vulnerable  |                           |     |     |
| ------- | ---------------------- | --- | --- | ---------------------- | ------------------------- | --- | --- |
| Tactics |                        |     |     |                        | ‘High’, ‘Medium’ or ‘Low. |     |     |
|         |   software             |     |     |   systems              |                           |     |     |
Adjust software/
|     | ▪  Upgrade application |                 |     | ▪  Block threat           |     |     |     |
| --- | ---------------------- | --------------- | --- | ------------------------- | --- | --- | --- |
|     |   systems or BU        | vendor strategy |     | ▪  Full Incident Response |     |     |     |
▪  Improve patch automation
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

42 Security Navigator 2024 Key data of the year: Pentesting Statistics 43
Penetration Testing
Finding Severity by Project Type
How critical were the Findings for specific test categories?
Max CVSS Avg CVSS Median CVSS Min CVSS
A Penetration Test is a contracted exercise in which a team The ‘findings’ of a Penetration Test report are therefore only a
9.80
of skilled and highly-trained ‘Ethical Hackers’ is tasked with small element of the overall output, but they contain elements
6.66
WebApp
emulating the activities of a real attacker in order to assess similar to the findings of a vulnerability scan and can be 6.10
the security of a system, identify vulnerabilities, and derive analyzed in a similar way, and even compared to some extent. 4.30
opportunities to improve its security posture. 9.30
As reports are a boutique product – hand-written by the tester
7.13
Mobile
Like Vulnerability Scanning, this exercise involves finding and and customized to meet the client’s specific requirement - they 6.80
reporting Vulnerabilities in the target systems, and has a similar do not lend themselves readily to quantitative analysis. 4.30
goal. But the process is very different. The tester will also seek
10.00
to identify known vulnerabilities (often those with CVE numbers 7.13
Internal
assigned to them) but will then also attempt to leverage those This year’s Penetration Testing dataset was expanded from 5.30 6.75
vulnerabilities to gain access to a target system, identify last year to include reports from two teams, one being a new
valuable resources that could be compromised or pivot from addition. We reviewed 296 anonymized Penetration Testing 9.80
6.83
there to attack other systems in range. reports for the period October 2022 through September 2023. External 6.10
Assessments are typically focused on specific customer 2.60
Penetration Testing is usually very targeted, performed within
requirements and scopes within the bounds of certain
a set of constraints agreed with the client that will include the 9.80
targets in scope, the time available, the location and privileges project types such as Internal, External, Web Application, Application Security 7.67
Mobile Application Security, Red Teaming, API assessment, 7.90
of the attacker, and sometimes specific goals or ‘objectives’ 5.90
Configuration Review, and more. These can vary in complexity
the tester should seek to achieve. Each test is performed by
one or more specific Ethical Hackers who then also writes up a and time allocation and may require multiple Ethical Hackers to 0 2 4 6 8 10 12
perform. For the most part the Client determines the scope and
report by hand explaining what was done, what was achieved,
extent of testing required.
what that implies and what could be done to improve security
In last year’s Navigator we reported that our Penetration Testing average length of a project in which we report a serious finding,
posture.
teams had to work 10% harder in the year 2022 than in 2018, is 10.5 days.
requiring 8 hours and 47 minutes to achieve a comparable
We’ve thus speculated previously that Penetration Tests have
outcome. Here we see the same pattern emerging. The testing
been revealing fewer serious security flaws over time, requiring
teams had to work 13% harder in 2023 than in 2018 to match
our Penetration Testing teams to work harder to uncover
the same total CVSS score per project day – needing to work
weaknesses that may impact a business. The good news for
9h 3m per project day. Our testers would have to work 9h 3m to
our clients is that this still holds true for our 2023 data, and no
achieve the same results they would have managed in 8 hours
significant regression has been observed. However, issues
at the start of 2018, which is 16 minutes more than for 2022.
are still regularly discovered that could negatively impact a
The average number of project days required to report a business if left unattended.
Serious (Critical or High) finding has increased by 2.5% to 7.9,
up from 7.7 previously reported in 2022. Comparatively the
Finding Severity over time
Finding Severity as Sum of CVSS per Project Day
30
2018 2019 2020 2021 2022 2023
25
20
15
10
5
0
Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

44 Security Navigator 2024 Key data of the year: Pentesting Statistics 45
| Finding Severity by industry                    |     |     |     |     |     |     |     |     |     |     |                      |     |                            |     |       | Research Notes |     |     |     |     |                                                                  |     |     |     |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | -------------------------- | --- | ----- | -------------- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| Finding Severity as Sum of CVSS per Project Day |     |     |     |     |     |     |     |     |     |     | CVSS per project day |     | Total project testing days |     |       |                |     |     |     |     |                                                                  |     |     |     |     |     |     |
|                                                 |     |     |     |     |     |     |     |     |     |     |                      |     |                            |     |       | About the data |     |     |     |     | Having said that, we can assert that our clients in the Finance  |     |     |     |     |     |     |
| 1.4                                             |     |     |     |     |     |     |     |     |     |     |                      |     |                            |     | 4,500 |                |     |     |     |     |                                                                  |     |     |     |     |     |     |
and Insurance and Public Administration industries rank
▪  296 new Penetration Tests reports in scope
4,230 high in both Penetration Testing and VOC Industry datasets,
▪
1.19 4,000 Period reviewed October 2022 to September 2023,   suggesting that these businesses are investing in improving
1.2
1.1 making a total dataset of 1,799 reports cyber security postures.
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 3,500 | ▪   |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Average CVSS score for CVEs report is 6.93
| 1.  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Types of tests |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
▪
|     |     |     | 0.87 |      |      |      |      |      |     |     |     |     |     |     | 3,000 | Average number of findings per project 7.71 |     |     |     |     |              |     |     |     |     |     |     |
| --- | --- | --- | ---- | ---- | ---- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | ----- | ------------------------------------------- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
|     |     |     |      | 0.82 | 0.81 |      |      |      |     |     |     |     |     |     |       | ▪  17.67% of findings are rated ‘Serious’   |     |     |     |     |              |     |     |     |     |     |     |
|     |     |     |      |      |      | 0.78 | 0.77 |      |     |     |     |     |     |     |       |                                             |     |     |     |     | Project type |     |     | %   |     |     |     |
| 0.8 |     |     |      |      |      |      |      | 0.73 |     |     |     |     |     |     | 2,500 |                                             |     |     |     |     |              |     |     |     |     |     |     |
This dataset includes Clients from over 10 different countries.
|     |     |     |     |     |     |     |     |     | 0.62 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Application Security  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
The selection of project types in this chart above is a subset
| 0.6 |     |     |     |     |     |     |     |     |     |     |     |     |     |     | 2,000 |     |     |     |     |     |     |     |     |     | involves evaluating discrete  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |
of project types compromised of WebApp, Internal, External,
|     |     |     |     |     |     |     |     |     |     | 0.48 | 0.48 | 0.47  |      |     |       |                                                             |     |     |     |     | Application Security |     |     | 6.5% |                        |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ----- | ---- | --- | ----- | ----------------------------------------------------------- | --- | --- | --- | --- | -------------------- | --- | --- | ---- | ---------------------- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |      |      |       |      |     |       | Mobile, and Application Security. The type of projects our  |     |     |     |     |                      |     |     |      | application that runs  |     |     |
|     |     |     |     |     |     |     |     |     |     |      |      | 1,475 |      |     | 1,500 |                                                             |     |     |     |     |                      |     |     |      |                        |     |     |
|     |     |     |     |     |     |     |     |     |     |      |      |       | 0.37 |     |       |                                                             |     |     |     |     |                      |     |     |      | natively on an OS      |     |     |
0.4 penetration testers engage in are for the most part determined
982 0.25 1,000 by our Clients. Our clients in this dataset have contracted us  A simulated attack from
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | for over 930 hours of WebApp testing from Q4 2022 through  |     |     |     |     |          |     |     |        | outside the test scope.  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | ------ | ------------------------ | --- | --- |
| 0.2 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |                                                            |     |     |     |     | External |     |     | 21.12% |                          |     |     |
555 465500 Q3 2023. This is the same amount of time allocated to External,  Typically, from across the
487
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Internal, Mobile and Application Security projects combined.  |     |     |     |     |     |     |     |     | Internet. |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- |
|     |     | 246 | 212 |     | 180 |     |     |     | 217 |     |     |     |     | 198 |     |                                                               |     |     |     |     |     |     |     |     |           |     |     |
|     | 5 4 |     |     | 7 2 |     |     |     |     |     |     |     |     | 4 5 |     |     |                                                               |     |     |     |     |     |     |     |     |           |     |     |
0 .       n     n   g e ministration g   de 0 S i m u l a t i n g   a   b r e a c h e d
|     | ts , | tio n |  o f | o   | p t | c , | matio | n d | in  | c   | Manufacturin |     | o n |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---- | ----- | ---- | --- | --- | --- | ----- | --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
A r n t ,   a n g n t e s   c t i c e o n ) ti fi es   a ce i n ra n a ti es Retail Tra n e t w o r k   a n d   a t t a c k i n g
e o n r t u s i m e n i es tr u e x a t i e n v i c re a n M d Insu d v ic C l i e n t s   s a m p l e d
n m a t i p o o e p a r is ons s  ( t r S c i e r Infor C a st m o e r Internal 10.78%
ta i r e n s e h a g m r p c e n i s l,     S th   s s i m   S a s s e t s   o n   t h e   p r i v a t e
| e r | e c r a a r | a n C o | t e C | v i m i | n a | a l | ea l | A   | e an | A d |     |     | o o d |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ----------- | ------- | ----- | ------- | --- | --- | ---- | --- | ---- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n t R T W M E n e r d o n ic H ia l  lic   c c o A   s u b s e t   o f   o u r   C l i e n ts   w a s   c l a s s ifi e d  p e r   I n d u s tr y   a n d   n e t w o r k   o f   a   c l i e n t .
| E n d   | n d   | d   |     |   S   A | s s i c h |     | o c |     | n c | b   |     | A d |  F  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------- | ----- | --- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a a a n h e r li c f e T e S in a P u n b u s in e s s   b a s e d   o n   e m p l o y e e   c o u n t.   W h e r e   c o m p a r i s o ns  a r e
|     |     |     | O   | t u b ro | d   |     |     |     | F   |     |     | a   |     |     |     |     |     |     |     |     |     |     |     |     | A   | n   a s s e s | s m e n t   o f   a n   |
| --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----------------------- |
P P a n m a d e   b a s e d  o n   I n d u s tr y   a n d   e m p lo y e e   c o u n t ,  b e a r   i n  m in d   th at
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |                                                                     |     |     |     |     |        |     |     |        | ap  | p li c a t i | o n   r u n n i n g   o n   a  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | ------ | --- | ------------ | ------------------------------ |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | the data set is smaller. The distribution of projects per Industry  |     |     |     |     | Mobile |     |     | 11.63% |     |              |                                |
mobile OS like Apple iOS
varies and only provides a metric that is useful when combined
or Android.
with observations such as the Vulnerability Operations Center
Attacking an application
(VOC) scan results.
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | WebApp |     |     | 50% | that is typically accessed  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --------------------------- | --- | --- |
via a web browser.
Key metrics by industry
Average Time per Project type
| Key metrics for the over-all vulnerability of different verticals  |     |     |     |     |     |     |     |     | VOC Findings/Asset |     | VOC Time to Patch |     | CVSS/Day | Overall ranking |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------------- | --- | -------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
14
Z
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | A   |       |     |     |     |     |            | A   |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | ---------- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       | In  |     | p   |     | Z          |     |     |     |
| 12  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       |     |     | p   |     |            |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       | te  |     | A   |     |            |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       | r   |     | b   |     |            |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | B   |     |       | n   |     | e   |     |            | U S |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | E   |       | a   |     | W   |     | n          |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       | l   |     |     |     | o          |     |     |     |
| 1 0 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       |     |     |     |     | ti         |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       |     |     |     |     | c a rit  y |     | A   |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | M   |       |     |     |     |     | pli        |     | Z   |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | o     |     |     |     | p   | c u        |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | b ile |     |     |     | A   | e          |     |     |     |
| 8   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       |     |     |     |     | S          |     | GB  |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |       |     |     |     | Q 3 | Mobile     |     |     |     |
3-
2 0
| 6   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |        |     | 2    |     | 0 2 |     |          |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | --- | ---- | --- | --- | --- | -------- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |        |     | 2 -Q |     | 2   |     |          |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |        |     | 4    |     |     |     | External |     |     |     |
| 4   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | WebApp |     |      |     |     |     |          |     |     | US  |
Internal
2
| 0   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | i o n |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
n e s n   l   t   ,   n d   n   mation Manufacturing e ,   f   p li c a t
ti o n c Servic e o s O i n e p n ) fi c s ministratio n e tio ng a d n t n  o   Ap y WebApp BE
u c r a a t i ic e d   i o x c io n ti c e re   a n c a si Tr m e i o e n t e s es e c u r i t 2023-Q
tr d Insu o d v a n a c t  ( e a t i e v i a st a o r t u Infor Retail  in e a t m a n i is S
n s tional  m S e r g   t r s s t r S c S e r C s i p h o ta cr g e p p r
Co an m d   yin E x c e n i l,   l   d th   s n s r e te r R e na o m e r 1 2
c o o r r s   r v i m i n a ic a A ea l l  A T r a W a En d   a C n t Q
c e   c a A c  F o u a G a S e A d i o n ic   H c ia d   ,  n M   E nal - US
| n    | d u |     | d     |   Q d   r |   c     | s s c h   | b l | o   | n   |     |     |     | r ts a | n d |     |     |     | e r |     | 3   |     |     |     |     |     |     |     |
| ---- | --- | --- | ----- | --------- | ------- | --------- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| in a | E   |     | a n g | , a n h e | b l i o | f e T e P | u   | S   | a   |     |     |     | A      | a   |     |     |     | x t |     | 0 2 |     |     |     |     |     |     |     |
| F    |     |     | n in  | O t P     | u P r   | d         |     |     |     |     |     |     |        |     |     |     |     | E   |     | 2   |     |     |     | M   |     |     |     |
|      |     |     | M i   |           |         | a n       |     |     |     |     |     |     |        |     |     |     |     |     |     |     |     |     |     | o   |     |     |     |
b
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | e   |     |     |     | E   | ile |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | E   |     | bil |     |     |     | x   |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | D   |     | o   |     |     |     | te  |     |     | Z A |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | M   |     |     |     |     | rn  |     |     |     |
p
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | p   | In  |     |     | a   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | A   |     | A   |     |     |     | l   |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Z   |     |     |     | te  |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | b   |     | r   |     |     |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | e   |     | n   |     | Z   |     |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | W   |     | a   |     |     | A   |     |     |
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | E   |     |     |     | l   |     |     |     |     |     |
B
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- |

46 Security Navigator 2024 Key data of the year: Pentesting Statistics 47
Pentesting
Dataset demographics
| Industry | %   | The distribution of projects assessed per business size shows  |
| -------- | --- | -------------------------------------------------------------- |
us that Small to Large businesses are engaging in penetration
| Finance and Insurance | 35.68% | testing services.  |
| --------------------- | ------ | ------------------ |
| Information           | 14.05% | Dataset caveat     |
For operational reasons, not all clients can be categorized by
| Public Administration | 13.51% |     |
| --------------------- | ------ | --- |
Size and Industry, so the data included here is not a complete
representation.
| Professional, Scientific, and Technical Services | 11.35% |     |
| ------------------------------------------------ | ------ | --- |
| Management of Companies and Enterprises          | 5.41%  |     |
| Transportation and Warehousing                   | 4.86%  |     |
| Health Care and Social Assistance                | 4.32%  |     |
| Other Services (except Public Administration)    | 3.78%  |     |
| Mining                                           | 3.24%  |     |
| Accommodation and Food Services                  | 1.08%  |     |
| Retail Trade                                     | 1.08%  |     |
| Arts, Entertainment, and Recreation              | 0.54%  |     |
| Construction                                     | 0.54%  |     |
| Manufacturing                                    | 0.54%  |     |
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

48 Security Navigator 2024 Key data of the year: World Watch 49
| World Watch |     |     |     |     |     | Urgency |     |     |     |     |     |     |
| ----------- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
Security Advisory types by Urgency
| Our World Watch service published 491 advisories for the  |     |     | World Watch advisory types |     |     |     |     |               |                      |     |             |                 |
| --------------------------------------------------------- | --- | --- | -------------------------- | --- | --- | --- | --- | ------------- | -------------------- | --- | ----------- | --------------- |
|                                                           |     |     |                            |     |     |     |     | Mobile Threat | Ransom Vulnerability |     | High Medium | Low Information |
100%
period October 2022 through September 2023 averaging
|     |     |     |     | Mobile Threat | Ransom Vulnerability |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------- | -------------------- | --- | --- | --- | --- | --- | --- | --- |
over 40 advisories per month – a combination of new and
90%
updates on previously covered topics. At a high-level World
12%
| Watch covers vulnerabilities and threats. We have split out two  |     |     |     | 3%  |     | 80% |     |     |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
other categories, Mobile and Ransom, to monitor. Rather than  24%
|     |     |     | 16% |     |     | 70% |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
being the only themes that emerge in our advisories, these are
| specific contexts we have chosen to monitor from a research  |     |     |     |     |     | 60% |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
perspective.
50%
The advisories are also classified according to one of five
40%
33%
urgency levels - Informational, Low, Medium, High, and Critical.
| Fortunately, we did not see the need to use the Critical urgency,  |     |     |     |     | 58% | 30% |     |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
23%
which is reserved for exceptionally bad situations. The bulk of
|     |     |     |     |     |     | 20% |     |     |     |     | 31% |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
our advisories this year were assigned an urgency of Medium
| or Low. |     |     |     |     |     | 10% |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0%
|     |     |     |     |     |     | High | Information | Low | Medium |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ----------- | --- | ------ | --- | --- | --- |
About the data:
▪  Number of advisories: 491
▪
Average number of advisories per month: Over 40
▪
Period analyzed: October 2022 to September 2023 Urgency of advisory types
▪  Themes: Threat, Vulnerability, Ransom, Mobile
▪  Distribution of advisories per theme: 58% Threat, 23%  High Medium Low Information
Vulnerability, 16% Ransom, 3% Mobile
▪  Distribution of Urgency: 33% Medium, 31% Low, 24%
9% 5%
| Information, 12% High |     |     |     |     |     |     |     |     |     | 12% | 16% | 12% |
| --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
24%
23%
▪  No Advisories with Urgency Critical was issued for the  31%
| period.                                             |     |     |     |     |     |     |     | 29% |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                                                     |     |     |     |     |     |     |     |     | 44% |     | 44% |     |
| ▪  202 distinct CVEs were mentioned in World Watch  |     |     |     |     |     |     | 30% |     |     |     |     |     |
20%
Advisories
|     |     |     |     |     |     |     |     |     |     | 38% |     | 38% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
41%
37%
|     |     |     |     |     |     |        |            | 35% | 6%              |     |                 | 6%  |
| --- | --- | --- | --- | --- | --- | ------ | ---------- | --- | --------------- | --- | --------------- | --- |
|     |     |     |     |     |     | Threat | Ransomware |     | Mobile Security |     | Vulnerabilities |     |
Advisory types over time
| Advisory types as they were issued in Q4 2022 to Q3 2023 |      |     |     | Mobile Threat | Ransom Vulnerability |                                                                  |     |     |                                                           |     |     |     |
| -------------------------------------------------------- | ---- | --- | --- | ------------- | -------------------- | ---------------------------------------------------------------- | --- | --- | --------------------------------------------------------- | --- | --- | --- |
| 60                                                       |      |     |     |               |                      | Urgency                                                          |     |     | Threats                                                   |     |     |     |
| 2022                                                     | 2023 |     |     |               |                      |                                                                  |     |     |                                                           |     |     |     |
|                                                          |      |     |     |               |                      | No advisories with urgency Critical were issued for the period.  |     |     | The World Watch team published 285 advisories describing  |     |     |     |
50
|     |     |     |     |     |     | This is somewhat astonishing given the almost overwhelming  |     |     | Threats, this constitutes 58% of all advisories published for the  |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- |
|     |     |     |     |     |     | scale and frequency of security ‘drama’ that occupied our   |     |     | period – made up from a combination of 111 new advisories          |     |     |     |
40 minds over the past 12 months. The fact that we didn’t have to  and 174 updates on existing advisories.
raise any of these incidents to a Critical level is a tribute to the
The high proportion of Advisory updates illustrates just how
resilience of our security systems and the level-headedness
30 important it is for defenders to have a way to track threats as
of our CERT team. Yet the CISOs we speak to universally
they develop. This is a somewhat under-examined challenge:
wear a kind of “thousand yard” stare and report being nearly
20 Threats and Vulnerabilities are not one-time events. Rather they
overwhelmed by the verocity of the security news cycle.
evolve and our understanding of them develops. Our response
needs also needs to adapt as the threat evolves or new insights
10
emerge.
0
| Oct Nov                         | Dec Jan | Feb Mar | Apr May | Jun Jul | Aug Sep |     |     |     |     |                            |     |     |
| ------------------------------- | ------- | ------- | ------- | ------- | ------- | --- | --- | --- | --- | -------------------------- | --- | --- |
| © Orange Cyberdefense 2023/2024 |         |         |         |         |         |     |     |     |     | www.orangecyberdefense.com |     |     |

50 Security Navigator 2024 Key data of the year: World Watch 51
Threats & Technologies Ransomware We have yet to see this threat emerging in any significant way.
However, the issue of mobile phone security has continued to
Technlogies or Vendors mentioned in World Watch Advisories relating to threats The cybercrime ecosystem is not shrinking, and as our Cy-X
High Medium Low Information grow and has featured prominently in our security advisories
research has shown, ransomware and its associated extortion
this year. For example:
activities have regained momentum off the back of a slow 2022.
MSI Several groups are active, some more than others, and the ▪ By July 2023, Apple had already issued patches to
Realtek better resourced groups are evolving their wares. address 11 0-day vulnerabilities in several of Apple’s
Dell operating systems, including iOS. By September 2023
In November 2022, Orange Cyberdefense published analysis
HP the tally rose to 16 0-days for the year. Once again, the
on new features present in the Play ransomware. These
3CX Israeli surveillance firm NSO Group and its Pegasus mobile
features are aimed at hiding the nature of the malware and to
malware made headlines through research published by
Atlassian
make it difficult for others to learn how it functions. The analysis
the non-profit research group CitizenLab.
AT&T we did proved useful when our Computer Security Incident
SonicWall Response Team (CSIRT) were called in the following month to ▪ We reported on examples of mobile surveillance by
actors other than NSO Group. Google Threat Analysis
Okta deal with an incident involving Play.
Group (TAG), with assistance from Amnesty International,
AutoIt
In February 2023, alarm bells rang as a wave of cyberattacks published findings on another surveillance activity
Netgear
were observed hitting VMware ESXi server. Malware possibly related to a surveillance vendor called Cytrox.
Mitel dubbed ESXiArgs ransomware was used by attackers that Shortly thereafter, we highlighted work by CitizenLab and
IrfanView compromised ESXi Servers by exploiting a vulnerability in Microsoft that pointed to possible surveillance malware
TP-Link OpenSLP. The panic was somewhat misplaced, as most of the called ‘Reign’, attributed to the Israeli vendor QuaDream.
Amazon victims were out of date self-hosted ESXi servers on popular
In last year’s report, we examined the relative pros and cons of
Roundcube cloud hosting service providers. The attackers had also evolved
the Apple and Android environments. This year we see these
SonarQube the malware to improve the encryption speed, and it was later
attributes continuing to shape the threat landscape in different
discovered that encrypted data could be recovered due to the
Zingdoor
ways.
partial encryption approach used to improve speed.
F5
Apple iOS features frequently in reports as the targeted device,
Linux These events seemed serious in isolation, but nothing could
but surveillance vendors such as Cytrox have a complete
LastPass compare with the sheer scale of what Cl0p did to Fortra’s
solution for Android devices also. For attackers and malware
DrayTek GoAnywhere MFT and Progress’ MOVEit Managed File
writers, iOS platforms have the benefit of being homogenous.
Barracuda Transfer (MFT) solutions. Using a 0-day vulnerability, Cl0p and
In other words, the code base is stable across many versions of
other groups exploited hundreds if not thousands of internet-
Oracle
the operating systems and runs on many hardware platforms.
facing systems, downloading large volumes of data and later
IBM This allows one 0-day to work on many Apple handsets running
using Cyber Extortion techniques to put pressure on victims.
McAfee a range of iOS version in a predictable manner.
This involved not only businesses who ran the vulnerable
GoTo
software, but also business partners and other 3rd parties Android has one inadvertent advantage in the numerous device
SolarWinds
whose data was being processed on them. In July 2023, the vendors and flavours of the operating system, so attackers
Zoom situation reached such a level that the U.S. State Department cannot rely on just one exploit chain to exploit a wide range of
Zyxel offered a reward of up to $10 million for information linking Cl0p devices or operating systems. This, however, can also make
Ivanti to attacks targeting U.S. critical infrastructure. asset and vulnerability management more challenging.
Mozilla
Apple has managed to develop a "privacy halo" that shines on
Adobe Mobile
their mobile products, giving it an aura of trustworthiness, so
QNAP
people valuing privacy may tend to gravitate towards Apple.
Huawei Orange Cyberdefense is part of Orange, a major
Thus Apple may be more commonly used by the very people
Apache telecommunications player. As such, we find the threat of surveillance operations are targeting.
attacks against mobile devices warrants special attention. This
Citrix
is why we track it as a separate theme from the general topics
Apple
of Threats and Vulnerabilities. We believe that attacks against
Intel
mobile devices will become more important as adoption
Opera
continues to grow and this technology becomes more essential
VMware
to personal, businesses and cybersecurity technology.
Cisco
For example, the threat of espionage gives governments
Fortinet
sleepless nights, and the threat of surveillance by some
0 2 4 6 8 10 12 governments on ordinary people is equally scary. But these
types of threats require a level of sophistication that is not yet
Note: In the chart above we omit Google and Microsoft because these two vendors skew the chart generally accessible.
considerably.
In last year’s report we raised concerns about the challenges
of managing vulnerabilities in enterprise mobile phone estates,
There are some familiar names in the remaining list of vendors mentioned in our Threat Advisories
and postulated that, as mobile phones assume a critical role in
that remain. It is also notable that we continue to encounter major security vendors in this list.
the enterprise security stack, criminals would begin to adopt
more sophisticated hacking techniques to exploit phones and
We also note the emergence of LastPass and Okta – two names that as we write are rapidly and
thus bypass controls like Multi Factor Authentication.
dramatically earning a place in our Advisories, our data, and next year’s report.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

52 Security Navigator 2024 Key data of the year: World Watch 53
Another reason why we appear to observe more sophisticated Vulnerabilities & Technologies
attacks against iOS then against Android is that Android
presents attackers with simpler options. Technlogies or Vendors mentioned in World Watch Advisories relating to vulnerabilities
High Medium Low Information
A feature of Android that iOS lacks is the ability to sideload
Microsoft
applications. Sideloading allows users to install mobile
applications without having to use the official Google Play Store. VMware
Anyone can install a compatible Android application on their
Cisco
handset. This is particularly useful for malware known as trojans.
Fortinet
For example, malware with traces of code linked to the Bahamut
Adobe
campaign was reported on toward the end of 2022. The Android
trojan masquerades as the “SecureVPN” mobile application that Citrix
then proceeds to steal information from the phone itself, as well Apache
as installed applications.
Google
This technique is quite common. Another Android application
IBM
with a strong Chinese user base, Pinduoduo, was found to
contain three exploits that target 2 Samsung vulnerabilities and Veeam
1 Android vulnerability. Pinduoduo is supposedly a legitimate Apple
ecommerce application for mobiles, and the software vendor
Amazon
denies the presence of any exploits. The question of how the
exploits ended up in the mobile application remains unanswered Barracuda
and raises the suspicion of either a supply chain compromise or Debian
coercion by an outside authority.
ConnectWise
Newer versions of Android spyware called WyrmSpy and
Accellion
DragonEgg were reported on in July 2023 by Lookout Threat
Intelligence. The Android spyware has been linked to APT41, a Sophos
Chinese state-backed hacking group. According to Lookout, the Symantec
spyware is not in common circulation, and victims are likely be
SolarWinds
compromised using social engineering techniques.
Gigabyte
A trojan can thus be a cheap trick to get surveillance software on
Samsung
a victim’s phone in the absence of more sophisticated exploits.
Although currently only a real option on Android, cyber criminals Intel
will probably start to adopt this approach for iOS also when
Oracle
Apple starts to allow sideloading of applications to comply with
requirements from the European Union. Sideloading of iOS Dell
application, which will possibly be a feature only available to Opera
users in the EU from iOS 17, is earmarked for 2024.
Ivanti
Although the issue of mobile phone security has not yet reached
Openfire
its zenith, and the story is still being written. We continue to
GNU
caution our clients that the challenge of mobile vulnerability
management is emerging and must be considered in medium- MOVEit
term security strategy considerations.
Fujitsu
McAfee
AMD
Juniper
JetBrains
Hitachi
0 5 10 15 20 25 30 35
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

54 Security Navigator 2024 Key data of the year: World Watch 55
|                    |     |     |     |     | ?   |     |     |                    |     |     |     |     |     |     | ?   |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
| Research Question: |     |     |     |     |     |     |     | Research Question: |     |     |     |     |     |     |     |     |
How much does our vulnerability
Is EPSS a possible way to
intelligence overlap with other
prioritize Security Intelligence?
common sources?
EPSS predicts the likelihood that a given vulnerability will be exploited. We note with interest that  We find that the overlap across popular vulnerability intelligence is small, but the vulnerabilities
prioritizing Advisories that contain CVE with high EPSS scores surfaces an entirely different view  that do overlap are absolutely worth paying attention to.
on what intelligence to prioritize.
The common bad
Choosing between left and right
The Exploit Prediction Scoring System (EPSS) is an initiative by  Which Intelligence Advisories   Overlap between World Watch and other popular Vulnerability Intelligence sources
| the Forum of Incident Response and Security Teams (FIRST)[49].  |     | would be prioritized if we focused on   |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
EPSS provides a score, ranging from 0 to 1, for each registered
the top 5% of CVE according to EPSS?
vulnerability that has an assigned CVE code. The EPSS score
One way to explore the potential value of EPSS as a source
indicates the likelihood of possible exploitation of a vulnerability
of Vulnerability Intelligence is to apply it retrospectively. We
within the next 30 days. The EPSS score can be used as
could look back at past intelligence reports that reference a
part of a triage process when deciding whether and when to
CVE. Some of our World Watch advisories meet this criterion.
patch a given vulnerability. EPSS has been shown to be an
We can create two groupings named ‘Prioritize’ and the other
accurate predictor and is rapidly becoming a valuable tool for
‘Evaluate’. The former, Prioritize, represents the World Watch
vulnerability managers.
Advisories we might need to examine closely and reassess.
| Along with each EPSS score is another value called the             |     | The Evaluate group should not be discarded but should be  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------------ | --- | --------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ‘percentile’ that provides a relative rank for the score assigned  |     | revisited at a later stage.                               |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
to a CVE. At the end of September 2023, there were 203,161
Of course, this distinction is made for the purpose of this
(94.73%) CVEs below the 95th EPSS percentile. Leaving 10,694
experiment only. Advisories with a high level of urgency should
(5.26%) CVEs in the top 5% of vulnerabilities most likely to be
always be read carefully to determine if this impacts the
exploited. If we were only concerned with CVEs, then we could
business.
focus our attention on CVEs in this pool.
The chart to the left illustrates how one would view our World
World Watch Advisories split on
Watch Advisories if we apply a simple heuristic using EPSS.
This is a simple experiment on using EPSS, but it demonstrates
CVEs at the 95th percentile of EPSS
the potential value of the EPSS metric in triage.
If we prioritize advisories with CVEs in 95th EPSS percentile, we
|     | T   | reduce the overall intelligence load to 27% of the total. As the  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
h
|     | re  | chart shows, this grouping is surprisingly diverse, though most  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
V a
|     | u ln t | Advisories would still address Threats and Vulnerabilities. |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------ | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Vul n
|      | In   | T h e   d i ve | r s i t y  o f  p ri o ri | t y  l e v e l s  is  m o | re  s u rp ri s in g | ,  w it h  4 5%   o f   |     |     |     |     |     |     |     |     |     |     |
| ---- | ---- | -------------- | ------------------------- | ------------------------- | -------------------- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Vuln | H fo |                |                           |                           |                      |                         |     |     |     |     |     |     |     |     |     |     |
ig
|         | M h   | th e s e   p ri | o r i t iz e d  A d v i | s o r ie s   b e in g  ca | te g o riz e d  a | s   ‘L o w  P rio r it y ’  |     |     |     |     |     |     |     |     |     |     |
| ------- | ----- | --------------- | ----------------------- | ------------------------- | ----------------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R       | edium |                 |                         |                           |                   |                             |     |     |     |     |     |     |     |     |     |     |
| a n som |       | b y   o u r   C | E R T .                 |                           |                   |                             |     |     |     |     |     |     |     |     |     |     |
V Mediu m O v e r l a p p i n g   V u l n e r a b i l i t y I t  i s  s tr i k in g  h o w   s m a l l   t h e   o v e rl a p   is   b e t w e e n   th e   fo u r  C V E
| u l n | Prioritize | T h e   P r i o | r i t y   c l a s s i fi c a | t io n   a s s ig n e d |   t o   A d v i s o r i e | s  i s   a         |              |                          |                           |                          |                       |                   |                          |                            |                             |                 |
| ----- | ---------- | --------------- | ---------------------------- | ----------------------- | ------------------------- | ------------------ | ------------ | ------------------------ | ------------------------- | ------------------------ | --------------------- | ----------------- | ------------------------ | -------------------------- | --------------------------- | --------------- |
|       |            |                 |                              |                         |                           |                    |              |                          |                           |                          |                       | g r o u p s .   T | h e   e x c e p t i o n  |   i s  t h e   Q u a l y s |   lis t ,  fr o m   w h i c | h  9 0 %   o f  |
|       |            | c o m p l e x   |   a n d   c o n t e x t-     | a w a re   p r o c e    | s s ,   a n d   s h o u   | ld   n o t   b e   |              |                          |                           |                          |                       |                   |                          |                            |                             |                 |
|       |            |                 |                              |                         |                           |                    | T h e  n u m | b e r   o f  C V E s   p | u b l i s h e d   i n   2 | 0 2 2   w a s  2 4 . 4 % |   h ig h e r  t h a n |   C V E   a l s o |   a p p e a r e d   in   | W o r ld   W a t c h .     |                             |                 |
Low
Thr e a ig n o r e d  b y  d e fe n d e r s .   E P S S   p r e d ic t s   t h e  l i k e li h o o d   t h a t  a   in  2 0 2 1 .  T h e   n u m b e r   C V E s  p u b l i s h e d   i n   th e  fi r s t  t hr e e  q u a r t e rs
t
given vulnerability will be exploited. We note with interest  of 2023 was 12% higher than the same period in 2022. If this  Given the low level of commonality between these lists,
Threat that prioritizing Advisories that contain CVE with high EPSS  identifying the most serious and important vulnerabilities from
projection is linear then we can predict that in 2023 we will
scores surfaces an entirely different view on what intelligence  across all of them is somewhat tricky. Ranked Top X-lists are
record over 28,000 new CVEs.
Threat Evaluate t o  p r i o ri t iz e .  B y   h ig h li g h t i n g   s p e c i fic   C V E ,  t h is  p e r s p e c t iv e   g o o d   a t  h i g h l ig h ti n g   t h e   t ip   o f  th e  ic eb e r g  w h e n  it   c o m e s  t o
Info
|     |     |                |                         |                           |                          |                     | World Watch highlighted 202 distinct CVEs across all  |                                                           |     |     |     | ex p l o i te d |   v u l n e ra b i li t ie | s ,   b u t  t h es e  m | ig h t  n o t  e ve n |   b e  a p p l ic able  |
| --- | --- | -------------- | ----------------------- | ------------------------- | ------------------------ | ------------------- | ----------------------------------------------------- | --------------------------------------------------------- | --- | --- | --- | --------------- | -------------------------- | ------------------------ | --------------------- | ----------------------- |
|     |     | a ls o   h a s |   th e   a d v a n ta g | e   t h a t   it  i d e n | ti fi e s  s p e c ifi c |  t e c h n i c a l  |                                                       |                                                           |     |     |     |                 |                            |                          |                       |                         |
|     |     |                |                         |                           |                          |                     | t h e m e s  a                                        | n d  a   121 distinct CVEs were raised in the context of  |     |     |     |                 |                            |                          |                       |                         |
Vuln vulnerabilities that can be searched for and addressed! to your environment.
|     |     |     |     |     |     |     | V u ln e ra b | i lit ie s . |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
L
o w
g h T o   g e t  a   s e n s e   o f   t h e   o v e r l a p   b e t w e e n   v u l n e r a b il i ty   in te l l i g e n c e
| Threat | Hi Vuln |     |     |     |     |     |                 |                          |                        |                               |                        |     |     |     |     |     |
| ------ | ------- | --- | --- | --- | --- | --- | --------------- | ------------------------ | ---------------------- | ----------------------------- | ---------------------- | --- | --- | --- | --- | --- |
|        |         |     |     |     |     |     | s o u r c e s , |  w e   e v a l u a t e d |   t h e s e   W o r ld |   W a tc h  C V E s           | a g a i n s t   th e   |     |     |     |     |     |
|        |         |     |     |     |     |     | C IS A   2 0 2  | 2   T o p   R o u t i n  | e l y  E x p lo it e d |   V u l n e r a b i li ti e s | ,   Q u a l y s  2 0 2 | 3   |     |     |     |     |
M
o T o p  1 0 ,  a n d  t h e  jo in t l y   p u b lis h e d   S e c u r i n ,  C S W ,  I v a n ti ,  a n d
ul n T h b
V re ile
a C y w a re   R a n s o m w a r e   R e p o rt  f o r   20 2 3 .   T h e   W or l d   W a t c h  C VE
t
pool is as much as 20x larger than the other lists.
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |

56 Security Navigator 2024 Key data of the year: World Watch 57
Overlap in Vulnerabilities
CVE CVSS Description
Vendors in the CISA KEV CVE that overlapped with CVE highlighted in World Watch this year
CVE-2018-13379 9.8 Fortinet FortiOS SSL VPN Path Traversal Vulnerability
ZK Framework
XStream
CVE-2020-1472 10 Microsoft Netlogon Privilege Escalation Vulnerability
Webmin
VMware
CVE-2021-45046 9 Apache Log4j2 Deserialization of Untrusted Data Vulnerability
Sitecore
Red Hat
CVE-2022-1388 9.8 F5 BIG-IP Missing Authentication Vulnerability Realtek
Netwrix
VMware Workspace ONE Access and Identity Manager Server-Side Template Injection
CVE-2022-22954 9.8 Mozilla
Vulnerability*
Intel
CVE-2022-26134 9.8 Atlassian Confluence Server and Data Center Remote Code Execution Vulnerability IBM
GitLab
ForgeRock
CVE-2023-0669 7.2 Fortra GoAnywhere MFT Remote Code Execution Vulnerability
FatPipe
F5
CVE-2023-20887 9.8 Vmware Aria Operations for Networks Command Injection Vulnerability
DrayTek
Dell
CVE-2023-23397 9.8 Microsoft Office Outlook Privilege Escalation Vulnerability CWP
Cacti
CVE-2023-24880 4.4 Microsoft Windows SmartScreen Security Feature Bypass Vulnerability Barracuda Networks
Artifex
CVE-2023-27350 9.8 PaperCut MF/NG Improper Access Control Vulnerability Zoho
Zimbra
Veeam
CVE-2023-28252 7.8 Microsoft Windows Common Log File System (CLFS) Driver Privilege Escalation Vulnerability
RARLAB
Oracle
CVE-2023-2868 9.8 Barracuda Networks ESG Appliance Improper Input Validation Vulnerability
Ivanti
Atlassian
CVE-2023-29059 7.8 3CX DesktopApp Arm
Veritas
CVE-2023-34362 9.8 Progress MOVEit Transfer SQL Injection Vulnerability Google
Citrix
Cisco
Apple
Fortinet
Apache
Microsoft
0 5 10 15 20 25 30
The vulnerabilities in the table above mostly have satisfyingly high CVSS scores, but that there are
some exceptions: the “Microsoft Windows SmartScreen Security Feature Bypass Vulnerability”, has
CVSS score of only 4.4 and yet appears in all these lists.
It’s also somewhat sobering to note (again) the prominence of security vendor products in this
consensus list about which vulnerabilities really matter.
The CISA Known Exploited Vulnerabilities (KEV) list is another intelligence source worth tracking. It
may be very U.S. Government specific, but it is still a valuable source, given that many of the CVEs it
lists impact popular vendors.
Placing the two lists side by side, we note that almost 10% of the 1,014 CVEs in the KEV
correspond to 48% of the World Watch CVEs mentioned in advisories.
Even bearing in mind that World Watch is an Advisory service, not a ‘top-x’ list, we are surprised to
find how little overlap there is between these intelligence sources. Where there is overlap, however, it
is clearly a powerful signal that vulnerabilities need to be focused on!
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

58 Security Navigator 2024 Key data of the year: Cyber Extortion 59
Cyber Extortion
Cl0p in Cy-X victims
| Since January 2020, we recorded 8,948 victims of Cyber  |     |     |     | Secondly, it shows us that roughly the same number of actors  |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Extortion that have been publicly listed on a ‘leak site’ on the  can cause much more damage than they did 2 years ago (we  Victims of Cl0p vs. other actors over time
Victims of Cl0p Not Cl0p
| dark web. Cyber Extortion, or ‘Cy-X’ is a form of computer  |     |     |     | don’t believe this year’s actors are the same actors as 2021). |     |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
1200
crime in which the security of a corporate digital asset
(Confidentiality, Integrity or Availability) is compromised and  2020 2021 2022 2023 177
The Cl0p-Effect
exploited in a threat of some form to extort a payment. 91
1000
One important factor influencing the record numbers in 2023 is
While this number of almost 9,000 victims seems high, we
the Threat Actor Cl0p. Cl0p is one of the oldest Cyber Extortion
know that this is just a partial view on the whole problem of  105
Cyber Extortion. This is obviously true because we note that  operations we monitor. In 2023, they displayed advanced  800 27
| the victims have been exposed on leak sites. This means they  |     |     |     | capabilities by exploiting 0-day vulnerabilities (in GoAnywhere  |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
8
and MOVEit), which resulted in several hundreds of victims
have already reached the end of the Cyber Extortion attack
|     |     |     |     | being exposed on their leak site.  |     |     |     |     | 13  | 12 11 | 4   |
| --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | --- | ----- | --- |
chain and threat actors have determined there is some value in  600
|     |     |     |     |     |     |     |     | 10  | 13  |     | 3   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
making the purported compromise public. We are very aware
Even without the Cl0p victims, our overall observations still
that there is a high dark number of victims that we simply don’t  34
hold true, as we can see in the chart on the next page. We have
know of.  400
never seen as many victims in any year as we have collected
in 2023. Cl0p accounts for 373 victims in 2023, leaving a victim
5
count excluding them of 2563 for the first three quarters alone.
Overall trends in victimology
200
In the past 12 months, since our last Security Navigator,  smitciV 1
The year 2023 has seen the highest count of victims we have
we documented 3,502 victim of Cyber Extortion. This is an  342 015 746 783 415 775 137 665 555 394 955 127 339 909
ever recorded, with the amount of Threat Actors participating
increase of 46% on the year before.  0
in this criminal ecosystem and maintaining a leak site also
returning to the (previous high) levels we saw in 2021. There  But who are the victims?  Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3
are two concerning observations to be made here. First of all,
the victim count for 2023 only includes the first three quarters.
Cy-X over time
Victims and actors count observed on double-extortion leak sites over time
|      |     |      |     |      |     | Victims count | No. of actors |     |     |     |     |
| ---- | --- | ---- | --- | ---- | --- | ------------- | ------------- | --- | --- | --- | --- |
| 1200 |     |      |     |      |     |               | 60            |     |     |     |     |
| 2020 |     | 2021 |     | 2022 |     | 2023          |               |     |     |     |     |
| 1000 |     |      |     |      |     |               | 50            |     |     |     |     |
39
| 800 |     |     |     |     |     | 38  | 40  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
34
33
29
| 600 |     |     |     |     |       |     | 30  |     |     |     |     |
| --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
|     |     | 26  |     | 25  |       |     |     |     |     |     |     |
|     | 24  |     |     |     | 23 24 |     |     |     |     |     |     |
23
21
| 400 |     | 18  |     |     |     |     | 20  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
13
12
| 200 |     |     |     |     |     |     | 10  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
smitciV
|           |           |           |           |           |           | 5201      | 6801 srotcA |     |     |     |     |
| --------- | --------- | --------- | --------- | --------- | --------- | --------- | ----------- | --- | --- | --- | --- |
| 09 842    | 915 556   | 024 725   | 095 957   | 875 665   | 394 665   | 528       |             |     |     |     |     |
| 0         |           |           |           |           |           |           | 0           |     |     |     |     |
| Qtr1 Qtr2 | Qtr3 Qtr4 | Qtr1 Qtr2 | Qtr3 Qtr4 | Qtr1 Qtr2 | Qtr3 Qtr4 | Qtr1 Qtr2 | Qtr3        |     |     |     |     |
In the past 12 months, since our last Security Navigator Report, we documented 3,502
organizations that fell victim to Cyber Extortion.
This is an increase of 46% on the year before.
But who are the victims?
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- |

60 Security Navigator 2024 Key data of the year: Cyber Extortion 61
Regional shift in victim count The South Arises Industry distribution
|                                              |     |     |     |     |                |                 |         | Latin America continues to feature prominently when we      |     |     |     | In the past years, we have seen a rather equal distribution  |     |     |     |
| -------------------------------------------- | --- | --- | --- | --- | -------------- | --------------- | ------- | ----------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- |
| Comparison between the last and prior year   |     |     |     |     | Last 12 months | Prior 12 months | Delta % |                                                             |     |     |     |                                                              |     |     |     |
|                                              |     |     |     |     |                |                 |         | track changes in victimology over time. Here we mostly see  |     |     |     | across several industry groups in our victim data. This is   |     |     |     |
1800 120% Brazil (8th) and Mexico (12th). Victims in this region have  especially true when looking at the top 3 impacted industries.
1683
97% been consistently increasing more quickly than elsewhere  As can be seen below, Manufacturing has remained the most
| 1600 |     |     |     |     |     |     | 100% |                                                              |     |     |     |                                                                |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | ------------------------------------------------------------ | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- |
|      |     |     |     |     |     |     |      | over time. We see almost every country in South and Central  |     |     |     | impacted sector over the 3.5 years we’ve been collecting this  |     |     |     |
1400 73% 70% 80% America impacted at least once by Cyber Extortion and clearly  data. We have investigated the question of why Manufacturing
67%
66% remember the attack by Conti against Costa Rica in 2022,  features so prominently in our victim data, in last year’s
|     | 52% 56% | 54% |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
1200 60% “affecting the backbone of the functioning of the state”[53],  Navigator and elsewhere, and remain perplexed by the topic.
1014
|      |     |     |     |     |     |     |     | which led the country to declare a state of national emergency.  |     |     |     | To date we have been unable to find an explanation that  |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | -------------------------------------------------------- | --- | --- | --- |
| 1000 |     |     |     |     |     |     | 40% |                                                                  |     |     |     |                                                          |     |     |     |
41% 21% contradicts our consistent hypothesis: The primary factor
14%
800 8% 20% influencing victim demographics is the size of the target
|     |     |     |     | 22% 23% |     |     |     | The South East Asian Tigers |     |     |     |              |     |     |     |
| --- | --- | --- | --- | ------- | --- | --- | --- | --------------------------- | --- | --- | --- | ------------ | --- | --- | --- |
| 609 |     |     |     |         |     |     |     |                             |     |     |     | population.  |     |     |     |
566
| 600 |     |     |     |     |     |     | 0%  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
As we’ve noted already in June 2023, in our CyXplorer report,
Bigger economies and bigger industries will in general tend to
|     |     |     |     |     |     | -34% |     | we observe above-average victim growth in South East Asia  |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
400 -20% be impacted more. Where we see deviations from this general
208 205 also, where LockBit is responsible for many of the cases. This
137 131 162 pattern, as in the case of Manufacturing, these emerge primarily
| 200 |     | 105 110 | 66 95 79 | 65 74 60 68 | 61  |     | -40% |     |     |     |     |     |     |     |     |
| --- | --- | ------- | -------- | ----------- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
55 40 31 55 39 47 39 21 32 8 7 is interesting if we believe that culture and language may have  from attributes of the victims rather than deliberate choices
|     |     |     |     |     |     |     |      | previously acted as a barrier to Cyber Extortionists. It looks  |     |     |     | made by the Threat Actor. In the case of Manufacturing, we  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---- | --------------------------------------------------------------- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- |
| 0   |     |     |     |     |     |     | -60% |                                                                 |     |     |     |                                                             |     |     |     |
S pe B merica A A a N East Africa dia er dics a n like Threat Actors are overcoming the barrier of language and
U o G C S E n i C h i n gi o currently still believe that vulnerability is the primary factor that
ur ea Asia  ex  d  I n Ot or C h e culture and increasingly impacting organizations in regions
E A Oc Mi N n r determines which businesses get compromised and extorted.
n  bea where they previously might have had issues understanding,
ati As our analysis of Industry patterns elsewhere in this report
|     | L   |     | s t  |     |     | b   |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
E a a r i communicating and negotiating. In the South East Asia region  suggests, business in the Manufacturing sector may have less
C
|     |     |     |     |     |     |     |     | we see Thailand, Malaysia and Singapore impacted the most.  |     |     |     | mature security postures and therefore find themselves more  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- |
vulnerable to opportunistic attacks.

| Country distribution / Geography  |     |     |     | Given rapid economic growth in the country, this could be  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
expected. According to the World Bank[51], India is one of the
| We observe that North America is the most impacted  |     |     |     | world’s fastest-growing economies.  |     |     |     |     |     |     |     |     |     |     |     |
| --------------------------------------------------- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
region. In fact, 53% of all victims for the past 12 months
On the other hand, India’s victim count is growing from a
were headquartered in the United States (ranked 1st). This
|                                                              |     |     |     | relatively low base, which we believe may be due to the barriers  |     |     |     | Victims by Industry |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- |
| is followed by other English-speaking countries such as the  |     |     |     | imposed by language and business culture. Cyber Extortion is      |     |     |     |                     |     |     |     |     |     |     |     |
| United Kingdom (2nd, 6%) and Canada (3rd, 5%). We offer      |     |     |     | a form of bullying in which victims must be coerced into paying   |     |     |     |                     |     |     |     |     |     |     |     |
Distribution shift among verticals we saw affected by Extortion in different years
| two potential explanations for this. First, as noted in previous  |     |     |     | for something that was already theirs. Depending on values,  |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
reports, we believe that the size of the economy plays a role in
culture, and other contextual factors, businesses in different
why victim countries are impacted by Threat Actors. In our first
countries are likely to be more or less approachable to the actor  0202 %31 %32
|                                                                  |     |     |     |                                                                |     |     |     | % % % % % %1 %0 | %2 %2 %4 %3 | %4 %5 %5 | %4 %7 | %5 %6 | %9  |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --------------- | ----------- | -------- | ----- | ----- | --- | --- | --- |
| annual Cy-X report, published in June 2023[50], we considered    |     |     |     | and responsive to the coercion. Like China and Japan, India    |     |     |     | 1 1 1 1 2       |             |          |       |       |     |     |     |
| whether the number of businesses registered in a country         |     |     |     | may be unfamiliar territory for most Cy-X threat actors. And,  |     |     |     |                 |             |          |       |       |     |     |     |
| could explain the geographical distribution in Cy-X victims. In  |     |     |     | at the risk of grossly generalizing, we suspect that business  |     |     |     |                 |             |          |       |       |     |     |     |
that analysis, we noticed that the top 7 victim countries were
culture in India may not respond well to the form of ransom
| also the countries with the most registered businesses. A    |     |     |     |                                       |     |     |     | 1202           |             |          |          |       |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | ------------------------------------- | --- | --- | --- | -------------- | ----------- | -------- | -------- | ----- | --- | --- | --- |
|                                                              |     |     |     | negotiation that makes Cy-X function. |     |     |     |                |             |          |          |       |     | %81 | %32 |
|                                                              |     |     |     |                                       |     |     |     | % % % % % % %0 | %3 %2 %4 %4 | %4 %3 %4 | %3 %5 %5 | %8 %7 |     |     |     |
| large economy and number of businesses serve to predict the  |     |     |     |                                       |     |     |     | 1 1 1 1 1 2    |             |          |          |       |     |     |     |
These two barriers appear to have been slowly eroding over the
number of suitable victims.
past 12 months, causing victim counts to move closer to where
the size of the economy predicts. Despite this subtle change,
India developing
|     |     |     |     | the Indian numbers remain low in comparison with other  |     |     |     | 2202         |             |          |          |       |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | ------------ | ----------- | -------- | -------- | ----- | --- | --- | --- |
|     |     |     |     |                                                         |     |     |     | % % % % % %2 | %4 %2 %3 %3 | %3 %4 %3 | %5 %6 %5 | %6 %6 | %7  | %61 | %02 |
similarly-sized economies.
| There are other factors that play an important role in shaping  |     |     |     |     |     |     |     | 1 1 1 1 1 |     |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
the observed victimology, namely language and culture.
Europe still in the cross hairs
Obviously, the email and website lures often used to achieve
initial access require an actor to be fluent in the victim’s
Other countries that have been more heavily impacted over  3202 %81 %02
language and have insight into their culture and business  % % % % % %2 %2 %3 %3 %4 %3 %5 %5 %6 %5 %8 %5 %4
|     |     |     |     | the past 12 months are the European countries. Here we  |     |     |     | 1 1 1 1 2 |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
practices. Moreover, if stolen data is used to pressure and
| extort victim organizations, Threat Actors need to understand  |     |     |     | see, Germany (4th), France (5th), Italy (6th) and Spain (10th)  |     |     |     |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
accounting for the most victims.  0% 10% 20% 30% 40% 50% 60% 70% 80% 90% 100%
what they have compromised and what it’s worth to the victim.
|     |     |     |     |     |     |     |     | Manufacturing |     |     | Health Care and Social Assistance |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --------------------------------- | --- | --- | --- | --- |
We believe that regional language and culture might act as  Unknown
Oceania takes the lead
a ‘barrier to entry’ to actors outside those regions, and thus  Professional, Scientific, and Technical Information Accommodation and Food Services
| served to help shape the victimology. But for a variety of  |     |     |     |     |     |     |     | Services |     |     |     |     |     |     |     |
| ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
Australia (7th) and Oceania overall has seen an increase of  Administrative and Support and Waste Utilities
reasons, this has recently started changing. Although English-
|     |     |     |     | 73%. This is interesting since Australia is the leader of the  |     |     |     | Retail Trade |     |     | Management and Remediation Services |     |     |     |     |
| --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | ------------ | --- | --- | ----------------------------------- | --- | --- | --- | --- |
Arts, Entertainment, and Recreation
speaking countries this year continue to account for the highest
|     |     |     |     | international taskforce to fight ransomware[52], but this effort  |     |     |     | Wholesale Trade |     |     | Transportation and Warehousing |     |     |     |     |
| --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --------------- | --- | --- | ------------------------------ | --- | --- | --- | --- |
numbers of victims, we are seeing a shift to other regions. Mining, Quarrying, and Oil and Gas
does not seem to have had a deterrent effect on actors
|                                                              |     |     |     |                                                                 |     |     |     | Finance and Insurance |     |     | Public Administration |     |     | Extraction |     |
| ------------------------------------------------------------ | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --------------------- | --- | --- | --------------------- | --- | --- | ---------- | --- |
| For example, India has seen the biggest increase in victims  |     |     |     | targeting the country. Instead, Oceania is the region with the  |     |     |     |                       |     |     |                       |     |     |            |     |
Management of Companies and
over the past 12 months.  second-largest relative growth over the last 12 months. Construction Other Services (except Public
|     |     |     |     |     |     |     |     |                      |     |     | Administration) |     |     | Enterprises                                |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --------------- | --- | --- | ------------------------------------------ | --- |
|     |     |     |     |     |     |     |     | Educational Services |     |     |                 |     |     | Agriculture, Forestry, Fishing and Hunting |     |
Real Estate and Rental and Leasing
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- |

62 Security Navigator 2024 Key data of the year: Cyber Extortion 63
Big Business The sector was particularly impacted between March and  Shift in victims by industry
August 2023, where we saw an average of 9. Threat Actors
The second most impacted sector, namely Professional  per month extorting victims. We have not previously witnessed
|     | Industry breakdown: comparison between the last and prior year   |     |     |     |     | Last 12 months | Prior 12 months |
| --- | ---------------------------------------------------------------- | --- | --- | --- | --- | -------------- | --------------- |
Services is very diverse and includes the sub-industries
this kind of high level of monthly Threat Actor activity for the
Engineering, Accounting, Research, Business Services, and
Information sector. By comparison, February and August 22  Manufacturing +42%
Legal Services. It is therefore also a very large industry. The  we saw an average of 4 Threat Actors in action per month. In
Retail sector has remained somewhere within the top 3 or 4  2021, the average was 5. In the past 12 months, Cl0p, LockBit3,  Professional, Scientific, and Technical Services +52%
impacted, except in 2023; where it has moved a few positions  ALPHV (BlackCat), Play and BianLian impacted this sector the
|     |     | Finance and Insurance |     |     | +106% |     |     |
| --- | --- | --------------------- | --- | --- | ----- | --- | --- |
down to position 9.
most.
|     |     |     | Educational Services |     | +115% |     |     |
| --- | --- | --- | -------------------- | --- | ----- | --- | --- |
Financing Cl0p
| Extorting Transportation |     |                                   | Wholesale Trade |     | +66% |     |     |
| ------------------------ | --- | --------------------------------- | --------------- | --- | ---- | --- | --- |
|                          |     | Health Care and Social Assistance |                 |     | +61% |     |     |
The Finance sector has seen an increase in 2023. This is largely  Transportation and Warehousing also caught our attention. In
due to a spike in June 2023, where the Threat Actor Cl0p  the past 12 months, we noted a significant increase in victims
|     |     |     | Construction |     | +33% |     |     |
| --- | --- | --- | ------------ | --- | ---- | --- | --- |
exploited the MOVEit vulnerability and uploaded hundreds  from this sector, making it the 5th fastest growing industry. This
of victims to their leak site. Amongst the victims were many  sector has sub-classifications that include essential services  Information +129%
businesses from the Financial sector.
| in society, which makes it particularly interesting to us. For  |     |     | Retail Trade |     | -20% |     |     |
| --------------------------------------------------------------- | --- | --- | ------------ | --- | ---- | --- | --- |
example, 13% of the victims were in Water Transportation, 11%
| in Air Transportation, 11% in Transit and Ground Passenger  |     | Transportation and Warehousing |     | +67% |     |     |     |
| ----------------------------------------------------------- | --- | ------------------------------ | --- | ---- | --- | --- | --- |
Extorting Education
Transportation, 2% in Rail Transportation and 2% in Pipeline
|                  | Administrative and Support and Waste  |     |     | +26% |     |     |     |
| ---------------- | ------------------------------------- | --- | --- | ---- | --- | --- | --- |
| Transportation.  | Management and Remediation Services   |     |     |      |     |     |     |
Another observation we are making is that over the last two
years the Educational Sector has started featuring significantly  Public Administration +22%
Pipeline transportation covers for transportation of oils or
in our victim dataset. In fact, from 2022 to 2023 we saw a 115%
| natural gases for example. The biggest sub-industry within this  | Other Services (except Public Administration) |     |     | +57% |     |     |     |
| ---------------------------------------------------------------- | --------------------------------------------- | --- | --- | ---- | --- | --- | --- |
increase in victims from this sector. Here we see universities,
sector was Support Activities for Transportation. Those would
colleges, elementary and secondary schools, as can be seen in  Real Estate and Rental and Leasing +33%
the cover activities such as Air Traffic Control, Air Operations,
our Sub-Industry breakdown.
| Freight Transportation support[54].  |                                               | Accommodation and Food Services |     | +33%  |     |     |     |
| ------------------------------------ | --------------------------------------------- | ------------------------------- | --- | ----- | --- | --- | --- |
|                                      | Mining, Quarrying, and Oil and Gas Extraction |                                 |     | +110% |     |     |     |
Extorting Information
|     |     | Arts, Entertainment, and Recreation |     | +34% |     |     |     |
| --- | --- | ----------------------------------- | --- | ---- | --- | --- | --- |
Over the past two years, we note that the Information Sector
has seen a significant increase of 129% in victims. We see  Utilities +3%
Computing Infrastructure Providers, Data Processing, Web
|     | Management of Companies and Enterprises |     |     | +4% |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
Hosting and Related Services, Telecommunications, Publishing
Industry (including Software providers) and Broadcasting  Agriculture, Forestry, Fishing and Hunting 0%
and Content Providers (such as radio, television, and media
streaming services as well as social networks), to mention a few  0 100 200 300 400 500 600 700 800
examples.
Business sizes
Cy-X victims by business size
We’ve already established that organizations from different
sectors around the world are being impacted by this form
|     | of cybercrime. Businesses of every size are also impacted.  |     |     |     |     | Large Medium | Small Unknown |
| --- | ----------------------------------------------------------- | --- | --- | --- | --- | ------------ | ------------- |
We observe Large Enterprises being impacted the most in
real numbers. They are followed by Small organizations,
which make up a quarter of all the victims and Medium- 12%
sized businesses, with a share of 23%. This is similar to the
distribution we reported in our CyXplorer report in June 2023.
Noteworthy is that we see Large organizations being impacted
more over the past 12 months, especially in August, when we
40%
saw victims with employee count of 1,000 to 9,999 peaking.
This seems to be a collective contribution – including victims
25%
from LockBit, 8Base, ALPHV (BlackCat), NoEscape, Akira, and
others – and thus not connected to a single event or single
1 - 49 Small
Threat Actor.
50 - 249 Medium
|     | Victims with 10,000+ employees have seen a steady increase  |     |     |     | 250+ Large |     |     |
| --- | ----------------------------------------------------------- | --- | --- | --- | ---------- | --- | --- |
in 2023, most notably with peaks in March, June and July. This
can be largely attributed to a single threat actor, namely Cl0p.
They exploited two major vulnerabilities in 2023 and uploaded
23%
data from hundreds of victims during those months, many from
the Large business category.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

64 Security Navigator 2024 Key data of the year: Cyber Extortion 65
Manufacturing: sub-industries
Victim count
Threat Actors
Machinery Manufacturing
Fabricated Metal Product Manufacturing Extortion groups observed in the past 12 months
| Chemical Manufacturing |     |     |     |     |     |     |     |     |     |              | 1% or less: |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----------- |
|                        |     |     |     |     |     |     |     |     |     | 26% LockBit3 | cloak       |
Computer and Electronic Product Manufacturing
|     |     |     |     |     |     |     |     |     |     | 11% Clop | AvosLocker |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | ---------- |
Food Manufacturing
|     |     |     |     |     |     |     |     |     |     | 10% ALPHV (BlackCat) | Abyss  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | ------ |
|     |     |     |     |     |     |     |     |     |     | 5%   Play            | Mallox |
Transportation Equipment Manufacturing
|     |     |     |     |     |     |     |     |     |     | 5%   Royal | Cuba |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---- |
26%
| Electrical Equipment, Appliance,  |     |     |     |     |     |     |     |     |     | 5%   8Base | RA Group |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- |
and Component Manufacturing
1%
|     |     |     |     |     |     |     |     |     |     | 4%   BianLian | MONTI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ----- |
Plastics and Rubber Products Manufacturing 2%
|     |     |     |     |     |     |     |     | 2%  |     | 4%   Black Basta | LV  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- |
Printing and Related Support Activities 2% 3%   Akira Everest
|                             |     |     |     |     |     |     |     | 2%  |     | 3%   Medusa      | metaencryptor |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | ------------- |
| Miscellaneous Manufacturing |     |     |     |     |     |     |     |     |     | 2%   ViceSociety | incransom     |
3%
Nonmetallic Mineral Product Manufacturing 2%   BlackByte knight (cyclops)
3%
|     |     |     |     |     |     |     |     |     |     | 2%   Snatch | Lorenz |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------ |
Furniture and Related Product Manufacturing 11% 2%   noescape Dunghill Leak
4%
|     |     |     |     |     |     |     |     |     |     | 1%   losttrust | Ransomhouse |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------- | ----------- |
Primary Metal Manufacturing
|     |     |     |     |     |     |     |     |     |     | 1%   Karakurt | ransomedvc |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | ---------- |
4%
Beverage and Tobacco Product Manufacturing 1%   Rhysida Darkrace
5%
|     |     |     |     |     |     |     |     |     | 10% | 1%   cactus | ciphbit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | ------- |
Paper Manufacturing 5%
|     |     |     |     |     |     |     |     |     | 5%  | 1%   Qilin        | Money Message |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | ------------- |
|     | 0   | 20  | 40  | 60  |     | 80  | 100 |     |     | 1%   RagnarLocker | Trigona       |
|     |     |     |     |     |     |     |     |     |     | 1%   HiveLeaks    | threeam       |
Finance and Insurance: sub-industries
Victim count
|     |     |     |     |     |     |     |     | Threat Actors & the Cy-X ecosystem  | There are indications that NoEscape might actually be the  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | ---------------------------------------------------------- | --- | --- |
Credit Intermediation and Related Activities first re-brand we have seen of Avaddon since they closed
|     |     |     |     |     |     |     |     | The Cyber Extortion ecosystem has been highly active over  | operations in June 2021, the main clue being that NoEscape’s  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | ------------------------------------------------------------- | --- | --- |
Insurance Carriers and Related Activities the past 12 months but even more so since February 2023.  and Avaddon’s encryptors are almost identical[55].
Securities, Commodity Contracts, and Other
This is an interesting observation, given the fact this also marks
Financial Investments and Related Activities
one year since Russias war against Ukraine broke out and we
The major players
Funds, Trusts, and Other Financial Vehicles reported notable disruptions in Cyber Extortion operations.
So, what has changed in the ecosystem to cause such an
Monetary Authorities-Central Bank increase? To shed light on this, we explore which Actors are  Who were the major Threat Actor groups over the past 12
months? In total, we recorded 54 Cyber Extortion operations
|     | 0   | 20  | 40  | 60  |     | 80  | 100 | responsible for the compromises we are seeing. |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- |
with leak sites on the dark web. This is an increase in Threat
Actors of 12.5% over 2022. As previously mentioned, the
Professional Services: sub-industries
|     |     |     |     |     |     |              |     | Multiple personalities                                            | number of victims increased 46% over the same period.         |     |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ----------------------------------------------------------------- | ------------------------------------------------------------- | --- | --- |
|     |     |     |     |     |     | Victim count |     |                                                                   | This disproportionality suggests how effective this criminal  |     |     |
|     |     |     |     |     |     |              |     | If we’re to believe the self-portrayals of Threat Actors, we are  | ecosystem has become.                                         |     |     |
Computer Systems Design and Related Services
dealing with “honest and simple pentesters” that call their
Architectural, Engineering, and Related Services victims “customers” and offer “loyal” conditions in pursuit  Threat Actors observed during this report period are shown
|     |     |     |     |     |     |     |     | of the return their hostages – namely the stolen data – to the  | below. LockBit3 has remained the most prolific actor site since  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | ---------------------------------------------------------------- | --- | --- |
Offices of Lawyers
approx. 1.5 years ago when Conti was still active and claimed
Accounting, Tax Preparation, Bookkeeping, victims after payment has been received.
and Payroll Services the top position. In line with the general trend, we saw a steady
Management, Scientific, and In reality, we are dealing with individuals or groups of  increase in LockBit3’s activity during the past 12 months. In
Technical Consulting Services
|     |     |     |     |     |     |     |     | individuals that conduct criminal activities by extorting  | June 2023, the German BSI and the US CISA agency published  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | ----------------------------------------------------------- | --- | --- |
Other Services organizations to receive a ransom payment.  a warning regarding LockBit, calling them the most dangerous
ransomware group[56][57]. However, other Threat Actors have
Legal Services
also been busy, and proportionally, we’ve actually been seeing
| Unknown |     |     |     |     |     |     |     | Evolving tactics |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- |
less LockBit3. Another group that sticks out is Cl0p, who we
Advertising, Public Relations, and Related have mentioned on several occasions already. Cl0p is closely
Threat actors continue evolving their tactics, especially their
followed by Play, who is responsible for 10% of all victims over
Scientific Research and Development Services extortion techniques. As previously observed, attacks no  the past 12 months.
longer just involve encryption. But, especially in 2023, we have
Specialized Design Services
seen a larger proportion of attacks extorting money only based
The frequent changes in and between Threat Actor groups
Engineering Services on stolen data, which we record as Data Extortion. Besides
can make the ecosystem seem bigger than it really is. Our
Data Extortion and the classic ransomware, we also observed
Real Estate analysis shows a growth of ‘only’ 12.5% in active groups but
|     |     |     |     |     |     |     |     | a small amount of DDoS threats made by the Threat Actor  | the victim count is growing more rapidly. We examine Threat  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | ------------------------------------------------------------ | --- | --- |
Computing Infrastructure Providers, Data
Processing, Web Hosting, and Related Services group NoEscape. This is interesting since we last saw threats to  Actor movements in a dedicated analysis later in this report that
DDoS from a long-gone group called Avaddon.
Management of Companies and Enterprises might shed some more light to this.
|     | 0   | 20  | 40  | 60  | 80  | 100 | 120 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

66 Security Navigator 2024 Key data of the year: Cyber Threat Intelligence 67
We collect a variety of IoC types, as depicted by the chart to Datalake IoC collected by Type
Cyber Threat Intelligence the right.
IP Domain URL File AS Other
The majority of the IoC we collect are IPs and Domains, which
together constitute over 50% of the data we collect.
Accurate and timely Cyber Threat Intelligence (CTI) can help As we collect IoC we remove duplicates. About 53% of the 2% 4%
defenders better identify and mitigate vulnerabilities and Indicators are unique. We also use a proprietary algorithm to
The datalake continuously ingests
attacks. CTI can also measure the credibility of possible assign each indicator a ‘Risk Score’ between 0 and 100. This 13%
attacks to reduce the number of security alerts IT teams face, security data from nearly 500 distinct scores serves as an indicator of how trustworthy we believe 31%
so that they are freed to mitigate genuine attacks. an indicator to be. The Risk Scores can be manually adjusted
sources. From these sources, we
by our Threat Analysts as they investigate Incidents, but are
The Orange Cyberdefense Datalake was developed to deliver
processed over 500 million distinct also algorithmically adjusted using variables like Sightings,
an integrated “Threat Intelligence Platform” (TIP) that allows
the fundamental trust we assign to the source and how many
allows our analysts and customer organizations to see what inputs during this reporting period.
unique sources report the same indicator.
is being detected by threat intelligence sources around the
world. It presents relevant information in a format that eases
25%
the analysis of Indicators of Compromise (IoC), providing risk
scores given by our security experts to facilitate decision About the data
making.
▪ Period: 01 October 2022 – 30 September 2023
The datalake collects, normalizes, enriches and offers up ▪ Number of Data Sources: 473 25%
standard CTI Indicators of Compromise (IoC) like domains,
▪ Ingested Events: 526,582,280
FQDN, IP and URLs, but also other types of data such as
emails, pasties, hash files, malware signature, registry keys, ▪ Unique Indicators: 246,113,573
data related to finance, such as IBAN numbers, and so forth. ▪ Data sample: 2,245,430 Unique IP indicators
The original threat data (called “Events”) include Orange's tier-1 ▪ Sampled between: 01 April 2023 & 30 September 2023
telco operator Internet backbone feeds, Orange Cyberdefense
feeds, open-source threat intelligence feeds, customers and
partners. Uniqueness
Threat data is being generated at an astronomical rate.
The chart below illustrates just how much data the Our CERT team has conducted internal research into the relative “uniqueness” of the intelligence we produce. With
datalake ingested this year. CTI, a key question is always “how much do we need”, and “how much value does additional intelligence add”? To
assess this question, the team investigates how much of the intelligence we can offer that isn’t already available in
other data sources.
Processed IoC data Every CTI product must have unique properties to be competitive in the market, and for us one differentiating
feature is the internal intelligence we collect, from Orange as a mobile operator, and from our own in-house
Datalake Indicators ingested over time capabilities. Some examples of these bespoke sources can be found below.
90,000,000
2022 2023 Orange Cyberdefense uniqueness rate
80,000,000
70,000,000
48% 38% 42% 42%
60,000,000
50,000,000
Mean > 48% exclusive intelligence Mean > 38% exclusive intelligence Mean > 42% exclusive intelligence Mean > 44% exclusive intelligence
40,000,000
30,000,000
C2 Monitoring Phishing Initiative Detect DNS P2A Sandbox
20,000,000 ▪Active C2 tracker, with ~0% ▪https://phishing-initiative.eu/ ▪Based in DNS Telemetry to ▪Proprietary in-house sand-
false-positives, tracking 43 ▪Backed by identify phishing and malici- box developed by Orange
10,000,000 malware families, including Orange Cyberdefense ous domains Cyberdefense
Cobalt Strike, Sliver, CERT experts ▪Backed by CERT Threat In- ▪Automatic malware identifi-
PoshC2, Quakbot, Bumble- ▪All intelligence is a result of telligence experts cation and configuration ex-
0
bee and more. manual analysis traction
Oct Nov Dec Jan Feb Mar Apr May Jun Jul Aug Sep
▪Over 10,000 active C2 tra-
ckers in database.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

There are other internal sources also, e.g. IoC noted in incidents All forms of intelligence-led security suffer from the same Malicious IPs
and registered by our CyberSOC and CSIRT teams, but for tension between three factors – False Positives, Limited
confidentiality reasons they are not reflected in the chart on the Resources & the infamous Unknown Unknowns. IP IoC collected for this sample over time
previous page.
At what levels do these come into balance and, given that we 30,000
As some of our intelligence is boutique and sourced internally, will never know the Unknown Unknowns, is there any real logic
that begs the question how “unique” our data is compared with in pursuing them?
25,000
other sources available to defenders.
Would our limited resources not be better spent in proactively
Given that there will also be data in those other sources that engineering robust systems? 20,000
are not present in our datalake, it is clear that our clients enjoy
This dilemma holds not only for Threat Intelligence, but also
increased visibility when additional intelligence is added. 15,000
for Threat Detection, Bug Hunting, Vulnerability Scanning and
Whether the additional intelligence warrants the additional cost,
other domains.
and what that tipping point is, remains open for debate. 10,000
We hope to bring some data and transparency to this debate
through reports like this one, and we hope other vendors will
The great intelligence dilemma 5,000
join us in providing objective insights that defenders can apply
The effectiveness of any kind of security intelligence lies on an to do the difficult decisions they have to make.
0
asymptotic curve – no matter how good it is, it will always be
missing something. And since we can’t know how much there
is to know, we can never know how much we’re missing.
That begs the question of whether improving the effectiveness
of any security intelligence makes any sense at all. No matter
how much we know, there will always be unknowns.
Data sample What we see
For the purpose of this first public exploration of our IoC data, Although limited, the sample dataset provides insights into the
we extracted a sample of all the unique IP address indicators volumes, effectiveness and diversity of the IoC we produce.
recorded in the Datalake between 01 April and 30 September
2023. This sample represents just under 2.5 million datapoints,
The source of all wisdom
which is a paltry sample of the full dataset. While this is
therefore just a humble introduction to this remarkable dataset, We ingest nearly 500 CTI sources, including internal,
we believe that there are interesting questions to be raised, and commercial and open source offerings. So how much value do
anticipate expanding on this research with bigger samples in we get from each source?
future research.
3202
,1
lirpA
3202
,8
lirpA
3202
,51
lirpA
3202
,22
lirpA
3202
,92
lirpA
3202
,6
yaM
3202
,31
yaM
3202
,02
yaM
3202
,72
yaM
3202
,3
enuJ
3202
,01
enuJ
3202
,71
enuJ
3202
,42
enuJ
3202
,1
yluJ
3202
,8
yluJ
3202
,51
yluJ
3202
,22
yluJ
3202
,92
yluJ
3202
,5
tsuguA
3202
,21
tsuguA
3202
,91
tsuguA
3202
,62
tsuguA
3202
,2
rebmetpeS
3202
,9
rebmetpeS
3202
,61
rebmetpeS
3202
,32
rebmetpeS
3202
,03
rebmetpeS
68 Security Navigator 2024 Key data of the year: Cyber Threat Intelligence 69
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

70 Security Navigator 2024 Key data of the year: Cyber Threat Intelligence 71
We note that 50% of all IoC are contributed by just 5 CTI data sources. The most prolific source alone contributes  A Risky Business
16%. The ‘long tail’ of ROI starts at the 20th data source. From here on each data source contributes less than 1%
of all the IoC. Each IoC is assigned a risk score, initially derived from the  The shape of this distribution is intriguing: 33% of all IoC have a
|     |     |     |     |     |     |     |     |     | value of the source, but adjusted manually over time by  |     |     | risk score of 20, and 98% have a risk score of 20 or less. 0.12%  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------------------------------- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- |
On average, each unique IoC is contributed by 2.2 sources. But once again, the distribution is highly skewed:
|     |     |     |     |     |     |     |     |     | intervention, correlation, sightings, etc.                 |     |     | of IoC have a Risk Score of 100.                       |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | The Risk Score gives defenders a means of focusing on IoC  |     |     | This characteristic is more easily understood when we  |     |     |     |
Sources across IoCs that are likely to be better predictors of malicious activity,  consider that each IoC is assigned a risk score between
|     |     |     |     |     |     |     |     |     | because they come from a reliable source, have been reported  |     |     | 0 and 20 in any of nine categories: Hack, Scan, DDoS,  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | ------------------------------------------------------ | --- | --- | --- |
Distribution of the number of distinct Sources across IoC   by multiple sources or have been associated with Incidents  Malware, Spam, Phishing, Fraud, Leak and Scam.
somewhere in our operations.
60%
50%
40%
The average Score (on a scale of 0-100)
30%
assigned for each of these Risk types is as follows:
20%
Risk Score per type
10%
Average Risk Score by Risk Type
0%
| 1 2 3 4 | 5 6 7 8 9 | 10 11 12 13 14 | 15 16 17 18 19 | 20 21 22 23 24 | 25 26 27 28 29 | 30 31 32 33 34 | 35 36 37 3840 | 41 45 47 57 | 20  |     |     |     |     |     |     |
| ------- | --------- | -------------- | -------------- | -------------- | -------------- | -------------- | ------------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
18
As the chart above illustrates, 53% of IoC are contributed by just one Source, while a further 26% are contributed
by two different Sources. And although some IoC are reported by more than 50 sources, more than 98% of all IoC
16
are reported by 10 sources or less.
14
Correlation
| Every time an IoC is submitted to the datalake we update an event counter. So analyzing the Events Count can give  |     |     |     |     |     |     |     |     | 12  |     |     |     |     |     |     |
| ------------------------------------------------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
us a sense of how many times a given IoC has been submitted and re-submitted by all our diverse sources.
| The Average Event count is 15.5.  |     |     |     |     |     |     |     |     | 10  |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Confirmed IoCs
8
Distribution of IoC confirmations - 10 or less
6
70%
| 60% |     |     |     |     |     |     |     |     | 4   |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
50%
2
40%
0
|     |     |     |     |     |     |     |     |     | Hack | Scan | DDoS Malware | Spam Phishing | Fraud | Leak | Scam |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ------------ | ------------- | ----- | ---- | ---- |
30%
20%
10%
0%
| 1 01 91 | 82 73 64 55 | 56 47 88 | 99 211 621 641 | 361 781 122 842 | 372 403 543 | 004 964 345 466 | 938 3211 7651 | 2742 1825 54581 539399 |     |     |     |     |     |     |     |
| ------- | ----------- | -------- | -------------- | --------------- | ----------- | --------------- | ------------- | ---------------------- | --- | --- | --- | --- | --- | --- | --- |
Just under 68% of all IoC are only submitted once and 96% are submitted 10 or fewer times.
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |

72 Security Navigator 2024 Key data of the year: Cyber Threat Intelligence 73
| Risk Score per type |     |     |     |     |     |     |     |     |     | Update Lag |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
Average Risk Score by Risk Type  Distribution across Update Lag Time in days
| 100% |     |     |     |     |     |     |     |     | 0-9 | 35% |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
90%
10-19
30%
80%
20-29
| 70% |     |     |     |     |     |     |     |     |     | 25% |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
30-39
60%
|     |     |     |     |     |     |     |     |     | 40-49 | 20% |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
50%
50-59
sgnithgiS fo egatnecreP 15%
40%
60-69
10%
30%
70-79
| 20% |     |     |     |     |     |     |     |     |     | 5%  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
80-89
10%
|     |     |     |     |     |     |     |     |     | 90-99 | 0%     |             |             |             |               |                 |                 |                 |                     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ----- | ------ | ----------- | ----------- | ----------- | ------------- | --------------- | --------------- | --------------- | ------------------- |
|     |     |     |     |     |     |     |     |     |       | 0 6 21 | 81 42 03 63 | 24 84 45 06 | 66 27 87 48 | 09 69 201 801 | 411 021 621 231 | 831 441 051 651 | 261 861 471 081 | 681 291 891 402 012 |
0%
|     | DDoS Fraud | Hack | Leak | Malware | Phishing | Scam | Scan | Spam |     |     |     |     |     |     |     |     |     |     |
| --- | ---------- | ---- | ---- | ------- | -------- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Update lag in days
|                                                                      |     |     |     |                                                                |     |     |     |     |     | The chart above visualizes how the maximum update ‘lag’ is      |     |     |     | Nevertheless, for our own Cyber Security Services we do have      |     |     |     |     |
| -------------------------------------------------------------------- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- |
| The distribution of Trust Scores across the different Threat         |     |     |     | One in three of all IoC are updated a day or more after being  |     |     |     |     |     |                                                                 |     |     |     |                                                                   |     |     |     |     |
|                                                                      |     |     |     |                                                                |     |     |     |     |     | distributed across all the IoC in this dataset. Almost a third  |     |     |     | feedback mechanisms in place that records when and where          |     |     |     |     |
| Types is quite diverse. It’s clear to see that vast majority of IoC  |     |     |     | ingested into the platform.                                    |     |     |     |     |     |                                                                 |     |     |     |                                                                   |     |     |     |     |
|                                                                      |     |     |     |                                                                |     |     |     |     |     | (33%) are updated on the same day, while 84% aren’t updated     |     |     |     | IoC are discovered by our operations in the wild. We call this a  |     |     |     |     |
have a Risk Score below 20 across all Threat Types.
Perhaps unsurprisingly given our observations above, most IoC  again after 30 days. Only 5% of IoC in the dataset are updated  ‘Positive Sighting’.
|     |     |     |     | that are updated end up with a Risk Score under 20. The only  |     |     |     |     |     | after 90 days. |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Less than 1% of the IoC in this dataset were updated with
| Some Tender Loving Care |     |     |     | other Risk Score common with updated IoC is between 50 and  |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
a confirmed ‘Positive Sighting’. However, whether or not
60. ~3% of IoC that were updated ended up with a Risk Score
|                                                                 |     |     |     |                |     |     |     |     |     | In the world of the blind |     |     |     | that information is fed back to our Datalake, and how much  |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ----------------------------------------------------------- | --- | --- | --- | --- |
| After being ingested, an IoC needs to be enriched and its Risk  |     |     |     | in this range. |     |     |     |     |     |                           |     |     |     |                                                             |     |     |     |     |
additional information accompanies that feedback, is an
Score needs to be updated as more sources submit it, its seen
|     |     |     |     |     |     |     |     |     |     | The truly meaningful question to ask about CTI is of course  |     |     |     | operational question. So we can’t glean much insight into the  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- |
in the wild, or an analyst manually reviews it.
whether it ever produces any results. Are the IoC we collect and
effectiveness of the CTI itself. We focus therefore on the 1% of
|     |     |     |     | The average lag between an IoC first being seen, and last  |     |     |     |     |     | distribute from the Datalake ever actually observed in ‘action’  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
How often does this happen? IoC that were positively identified in the wild and reported to
|     |     |     |     | being updated, is 17 days. |     |     |     |     |     | by our clients or security operations? Like good advice, good  |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
the Datalake.
To answer this question we consider the ‘Last Updated’ field of
CTI is not necessarily heeded. Since we don’t always know if,
an IoC. If this is more than a day later than the ‘First Seen’ date  First we examine how the ‘lag’ between the IoC being recorded
when, or how the CTI we distribute is put to use, this can be a
on which the IoC was first catalogued in the Datalake, then we
|     |     |     |     |     |     |     |     |     |     | very difficult question to answer objectively. |     |     |     | in the Datalake and being observed in the wild. This distribution  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | ------------------------------------------------------------------ | --- | --- | --- | --- |
consider the IoC to have been ‘Updated’ in some way.  is illustrated below:
| IoC Updates and Risk Score |     |     |     |     |     |     |     |     |     | Sightings Lag |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Proportion of IoC updated Risk Score Updated Not updated Positive Sightings Time Lag - distribution in days
| 100% |     |     |     |     |     |     |     |     |     | 70% |     |     |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
90%
60%
80%
70%
50%
60%
40%
50%
40%
sgnithgiS fo egatnecreP 30%
30%
20%
20%
10%
10%
|     | 31.42% 5.50% | 60.97% | 0.04% | 0.27% | 2.99% | 0.00% | 0.00% | 0.00% | 0.25% |     |     |     |     |     |     |     |     |     |
| --- | ------------ | ------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0%
|     | 0-9 10-19 | 20-29 | 30-39 | 40-49 | 50-59 | 60-69 | 70-79 | 80-89 | 90-100 |     |     |     |     |     |     |     |     |     |
| --- | --------- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0%
|     |     |     |     |     |     |     |     |     |     | 0 2 | 4 6 10 | 12 15 17 | 25 31 33 | 36 41 | 46 50 52 | 55 59 66 | 71 78 87 | 95 117 142 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ | -------- | -------- | ----- | -------- | -------- | -------- | ---------- |
Sightings lag in days
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |

74 Security Navigator 2024 Key data of the year: Cyber Threat Intelligence 75
Sightings Flow
Confirmed Sightings for two Orange Cyberdefense internal data sources
| We note that 51% of all the confirmed Positive Sightings are  |     | We therefore see some evidence that a higher Risk Score           |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| not recorded in the wild after the 1st day. The average time  |     | correlates with a higher probably of Sighting in the wild, but a  |     |     |     |     |     |     |     |     |     |     |     |     |
| between recording the IoC in the Datalake and a confirmed     |     | more extensive analysis would be required to confirm this.        |     |     |     |     |     |     |     |     |     |     |     |     |
Positive Sighting in the wild is ~ 20 days. Two thirds (67%) of all
IoC are not reported in the wild after ~10 days.
|     |     | Risk Scores for   |     |     |     |     |     |     |     | Hack |     |     |     |     |
| --- | --- | ----------------- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- |
If we consider Sightings that were reported but not ‘confirmed’
IoC Sighted in Operations
as Positive (we call these ‘Neutral Sightings’), the sample
‘grows’ to 2.15% of this dataset. The ‘oldest’ Sighting also
|                                                               |     |     |       |          |      | gnikcarT revreS CnC |     |     |     |     |     |     |     | Medium |
| ------------------------------------------------------------- | --- | --- | ----- | -------- | ---- | ------------------- | --- | --- | --- | --- | --- | --- | --- | ------ |
| increases slightly from 155 to 202 days, the average time to  |     |     | Min   | Average  | Max  | Median              |     |     |     |     |     |     |     |        |
Sighting
| sight an IoC grows to 31 days, and we note that 67% of IoC are  |     |     | Score | Score | Score | Score |     |     |     |     |     |     |     |     |
| --------------------------------------------------------------- | --- | --- | ----- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
sighted within the first 10 days before ‘disappearing’.
|     |     | None | 0   | 14,51 | 100 |     |     |     |     |     |     |     |     |     |
| --- | --- | ---- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The Mean Risk score across all types is 14 for IoC with
Malware
confirmed Positive Sightings, compared to just 5 for ‘Neutral’
|     |     | Neutral | 0   | 9,47 | 100 | 5   |     |     |     |     |     |     |     |     |
| --- | --- | ------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sightings. 40% of Positive Sightings have a Risk Score
between 20 and 30. Interestingly, there is a small spike in IoC
| with a ‘perfect’ Risk Score of 100 within the Positive Sightings –  |     | Positive | 0   | 15,95 | 100 | 14  |     |     |     |     |     |     |     |     |
| ------------------------------------------------------------------- | --- | -------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
almost 2% - compared to 0.6% for Neutral Sightings.
Phishing
gnirotinom topyenoH
Low
Risk scores of Sightings
| Distribution of Risk Scores for Positive and Neutral Sightings |     |     |     |     | Neutral | Positive |     |     |     |     |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Spam
60%
50%
Scan
40%
The relationship between Sources and Risk Scores for confirmed positive Sightings is shown above, limited to two
internal IoC data sources that were sighted. The flow visualizes the data source, the Threat Type and Risk Score for
30% that Threat Type for each IoC in a confirmed Positive Sighting:
Sightings lag and Risk Score
sgnithgiS fo egatnecreP 20%
|     |     |     |     |     |     | IoC Sightings lag vs Average Risk Score |     |     |     |     |     |     | Neutral | Positive |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- | --- | ------- | -------- |
250
10%
200
0%
| 0-9 10-19 | 20-29 30-39 | 40-49 50-59 | 60-69 | 70-79 | 80-89 | 90-100 |     |     |     |     |     |     |     |     |
| --------- | ----------- | ----------- | ----- | ----- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
IoC Risk Score
150
100
syaD ni gnithgiS tsaL
50
0
|     |     |     |     |     |     |     | 1 2 3 | 4 5 6 | 7 8 | 9 10 11 12 | 13 14 15 | 16 17 18 | 20 25 26 | 29 31 |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | --- | ---------- | -------- | -------- | -------- | ----- |
Average Risk Score
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |

76 Security Navigator 2024 Key data of the year: Cyber Threat Intelligence 77
The average Risk Score assigned across all IoC is 14.39. above that the charts can be hard to tell apart!
Although this dataset is arguably too small to draw definitive This kind of distribution beautifully captures the ‘intelligence
conclusions from, we note with interest that as the Risk Score dilemma’ we discuss above, which is classic ‘Pareto
increases (shown on the X-axis from 1 to 31), the Sightings lag Principle’[58]: The majority of the apparent value we get from
(shown in days on the Y-axis) appears to decrease. Bearing CTI is highly concentrated in a few sources, with an average
in mind that this refers to the last sighting, it would seem to Risk Score and will persist for around 2 days. At the same
suggest that the more highly rated the IoC (the ones we have time, however, there is a lot of value distributed across other
more confidence in) persist in the wild for a shorter time. This sources, with diverse Risk Scores. Ignoring those indicators
may in turn suggest that this high-confidence is indeed more means taking the risk of missing crucial intelligence, though
accurate, but that the attacker infrastructure being identified is the probabilities become even lower. We need both ‘depth’ and
being recycled quickly. ‘breadth’ in the CTI we consider. At the same time, even that is
not *all* the intelligence there is, so one is inclined to add even
IoC with a Risk Score above 20 were never Sighted after more
more data. But IoC are duplicated across multiple sources, so
than ~100 days had lapsed.
the relative ROI decreases even more, although the security
value is still there.
A tale of curvy distributions
A few key elements ensure positive security outcomes
This humble analysis of our CTI data surfaces several from CTI:
inconclusive findings: The volume of data in play is
1. The correct balance between quality and quantity of data;
overwhelming, and that’s just from a researcher’s perspective.
Defenders have to deal with a plethora of data sets that differ
2. Data context to facilitate effective triage;
but also overlap significantly.
A dynamic Risk Score provides clients with a means to 3. Minimum ‘friction’ to reduce the cost of applying and
prioritize indicators, but on a scale of 1-100, the average Risk acting on CTI;
Score assigned is only 14.39. Furthermore, 98% of IoC have a
4. Feedback loops that allows one to assess the relative value
risk score of 20 or less and only 0.12% of IoC have a Risk Score
of sources and indicators;
of 100.
It’s very hard to select the best CTI ‘Sources’ also: 50% of all 5. Data transparency that facilitates informed decision
IoC in our Datalake are contributed by just 5 CTI data sources. making by security buyers.
The most prolific source alone contributes 16%. But there’s a
‘long tail’ of contributors that starts at the 20th data source. We hope that the data provided in this report sheds some light
From here on each data source contributes less than 1% of all on the intelligence dilemma and contributes in some small
the IoC. How many data sources are enough? way to the effective procurement and application of CTI by
defenders.
Like so many things in security, the ‘effectiveness’ of IoC is also
a large blind spot: Since CTI tends to flow in one direction, it’s
hard to know what CTI is effective, and how long it remains
effective.
From the limited insight we have, we assess that the average
time between recording the IoC in the Datalake and a
confirmed Positive Sighting in the wild is ~ 20 days. However,
the majority of IoC that we do observe are not seen again after
5 days, and really 2 days seems to be the expiry time for most
CTI. So any process that consumes CTI needs to be highly
agile.
The challenge for defenders is therefore to determine how
much CTI they need, and what CTI matters.
Wherever we examine any attribute that might help inform that
question, we see the same dramatic ‘reverse L’ distribution
emerging. The bulk of IoC tend to share the same attributes
(source, Risk Score, Updates, etc), but that is always followed
by a ‘long tail’ of IoC that have diverse attributes. This pattern is
so consistent across the distributions we visualize in the study
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

78 Security Navigator 2024 79
Region Scorecard
Region Scorecard
Europe Region
Nordics Region
Cy-X region ranking Cy-X victim delta
Europe, including UK, had the second In this region we saw an increase in the Cy-X region ranking Cy-X victim delta
highest number of Cy-X victims number of victim organizations of
Proportionally the Nordics rank The Number of victims increased from last
year. We saw a rise of
23% in our + 16%
10th in our
+ 21%
victim data
victim data
Most affected country Most affected country
On its own UK was in second place when it came to victim numbers, with Sweden was targeted most heavily with 25 victims recorded:
206 organizations having entries posted on leak sites, around
53% of all Nordic victims.
6% of all victims and a 52% increase
from last year. Hacktivism Ranking
▪ Sweden was the third most impacted country with 338 attacks, which was
followed by Denmark with rank 11, translating into 127 attacks.
▪ Most of the Nordic countries were impacted by the two groups, namely
Hacktivism Ranking "NoName057(16)" and "Anonymous Sudan".
▪ As a region Europe, including the Nordics, dominates the chart for number of
Hacktivism incidents, with 3,404 out of a total of 4,016 recorded attacks.
▪ The top 5 victim countries are all European, and not surprisingly Ukraine takes pole
position by some way with 639 documented attacks.
▪ The remainder of the top 5 consists of Poland(433), Sweden(338), Lithuania(220) &
Germany(219).
▪ Over 60% of the attacks against Ukraine were by a group known as
"CyberArmyRussia". The remaining top 5 countries were primarily targeted by the
group "NoName057(16)", with the exception of Sweden who attracted the attention
of "Anonymous Sudan".
CyberSOC Ranking
▪ The top 5 countries when it came to confirmed incidents in our CyberSOCs are all European. Incidents
from clients in Sweden(36%) & France(35%) made up the vast majority of true positives, whilst the UK
made up the top 3 with 9%.
▪ The picture changes slightly when we consider false positive incidents instead. Sweden is still top of the
pile with 29%, however the UK is now second with 28% and Germany completes the top 3 with 15%.
▪ When we consider how countries compare with their relative levels of coverage taken into account, we
see that the top 5 for confirmed incidents are again all countries in Europe, this time however there has
been a significant shift.
▪ If we now look at false positive incidents the top 2 countries remain the same, however the proportions
are slightly closer with France having 60% and Sweden now with 13% of recorded false positives. The
UK is now not too far behind Sweden representing 12%, Belgium & Denmark make up the rest of the
top 5 again, this time with 6% & 5% respectively.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

80 Security Navigator 2024 81
| Region Scorecard            |     | Region Scorecard |     |
| --------------------------- | --- | ---------------- | --- |
| Africa & Middle East Region |     | South-East Asia  |     |
Cy-X region ranking  Cy-X victim delta  Cy-X region ranking  Cy-X victim delta
A total of 142 victims in this region put it in  On what we reported in last year’s Navigator  A total of 110 victims in this region put it in 5th  From the perspective of a percentage increase
4th place. we saw an increase of  place. on last year, South-East Asia was 4th highest
with an increase in victim numbers of
| 142 victims | + 42%  | 142 victims |     |
| ----------- | ------ | ----------- | --- |
+ 67%
| Most affected country  |     | Most affected country  |     |
| ---------------------- | --- | ---------------------- | --- |
The most victims in this region were from South Africa where we saw 23  Thailand has the dubious honor of top spot in this region with 36 victims,
organizations, which represents  around 1% of all victims globally or almost
0.67% of all victims, listed on leak sites. 33% of the total for this region.
Hacktivism Ranking
▪  Israel was the primary focus of attacks in the Africa and Middle East region.
They were the target for
102 attacks all initiated by "Anonymous Sudan".
OT Ranking
▪  Israel, Iran & South Africa were joint tenth in the list with each having
2.5% of reported global OT attacks.  Region Scorecard
East Asia Region
| Region Scorecard |     | Cy-X region ranking                      | Cy-X victim delta                              |
| ---------------- | --- | ---------------------------------------- | ---------------------------------------------- |
|                  |     | This region comes in at 6th place with   | Whilst all other regions were hit with double  |
South Asia Region
|     |     | 100 victims this year. | digit percentage increases, East Asia only  |
| --- | --- | ---------------------- | ------------------------------------------- |
experienced a increase of
100 victims
+ 3%
| Cy-X region ranking                                 | Cy-X victim delta                             |     |     |
| --------------------------------------------------- | --------------------------------------------- | --- | --- |
| A total of 71 victims in this region put it in 8th  | Despite the low number of victims South Asia  |     |     |
| place.                                              | witnessed an increase of                      |     |     |
Most affected country
| 71 victims | + 115%  |     |     |
| ---------- | ------- | --- | --- |
The cause of the low increase in the region is explained by China,
which actually saw a drop from 32 last year to 21, which is a
decrease in recorded victims by -34%
Most affected country
CyberSOC Ranking
India is the primary reason for the overall increase in South Asian victims.
Indian organizations went from 31 being targeted to 61, a  This year we saw slightly under 3% of our confirmed incidents
originate from clients in China.
97% year on year increase.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

82 Security Navigator 2024 83
Region Scorecard
North America Region (US & CA)
Cy-X region ranking Cy-X victim delta
Highest number of recorded Cy-X victims Since last year’s Security Navigator we saw
with 1,845 reported in the past 12 months. the number of victims grow at
53.5% of the + 65%
victims
Most affected country
The US was by far the most targeted, both in their region and globally,
with 1,683 victims listed
53% of all victims were headquartered in
the United States. Region Scorecard
Latin America Region
Hacktivism Ranking
▪ Considering the proportion of Cy-X attacks seen in North
Cy-X region ranking Cy-X victim delta
America the number of recorded Hacktivism incidents is
relatively low. Latin America had the third highest victim This region saw a fairly significant increase in
count with 205, almost 6% of the total comparison to what we saw last year
▪ "Anonymous Sudan" & "KillNet" were the primary perpetrators
number of victims.
when it came to the US, whereas Canada only saw attacks
+ 56%
originating from "NoName057(16)".
205 victims
There were 201 targeting the US whilst
Canada saw 96.
Most affected country
OT Ranking
▪ North American companies made up almost a third of all Brazil accounted for most of the Latin American victims with 74, putting it
in 8th place of all victims globally.
reported attacks on OT.
▪ With just short of a quarter of the reported attacks on OT it is Brazil accounted for 36% of
no surprise that the US tops the rankings of targeted countries Latin American victims
globally.
▪ Canada, while not as prominent as the US, also featured in the
top 5 list of targeted countries with almost 8% of all attacks.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

84 Security Navigator 2024 85
Industry Scorecard
Industry Scorecard
Manufacturing
Professional, Scientific, and
Technical Services
Cy-X industry ranking Cy-X victim delta
Manufacturing was again on the top spot in  Compared to last year, Manufacturing had
terms of targeted industries with  200+ more victims, a year-on-year increase of
|     | Cy-X industry ranking | Cy-X victim delta |
| --- | --------------------- | ----------------- |
20% of all
+ 42%
|     | Professional, Scientific, and Technical  | Professional, Scientific, and Technical      |
| --- | ---------------------------------------- | -------------------------------------------- |
|     | Services were second overall by a        | Services remained in second place this year  |
known attacks
|     | considerable margin, with  | but saw an increase in victims of  |
| --- | -------------------------- | ---------------------------------- |
|     | 17% of victims             | + 52%                              |
and over 17% more than the second placed
industry Professional, Scientific, and
| Technical Services. | falling under this banner. |     |
| ------------------- | -------------------------- | --- |
Most affected sub industry
Most affected sub industry
As a sub-industry, Machinery Manufacturing had the highest proportion of attacks
with 15%  This sector is a very diverse one, while we see Computer System Design related organizations (17%) being impacted
the most, followed by Architecture and Engineering (17%); we find it interesting that we see Offices of Lawyers with 14%
(highlight in big and orange) and at the 10% f the victims stem from the overall Legal Services sub-sector. Highlighting
In joint second Chemical & Fabricated Metal Product Manufacturing   that the Legal Service industry has been mostly impacted.
both had a 12% share of attacks.
CyberSOC Industry Ranking
|     | CyberSOC Industry Ranking | Pentesting Industry Ranking |
| --- | ------------------------- | --------------------------- |
▪  No surprise to once again see Manufacturing top the table for most total incidents. Almost
|     | ▪  The fourth highest volume of total incidents came  | ▪  Professional, Scientific, and Technical Services has  |
| --- | ----------------------------------------------------- | -------------------------------------------------------- |
38,000 incidents came from customers in this sector, with over 8,100 confirmed
|     | from the Professional, Scientific, and Technical  | an average of 5.11 findings per pentest.  |
| --- | ------------------------------------------------- | ----------------------------------------- |
as True Positive incidents.
|     | Services industry, with 16,425 incidents being  | ▪  We see 34% fewer findings than the average.  |
| --- | ----------------------------------------------- | ----------------------------------------------- |
▪  Between them the Hacking & Misuse threat actions made up over 50% of True Positive incidents
|     | recorded. Almost 2,500 of these incidents required  | ▪   |
| --- | --------------------------------------------------- | --- |
The average CVSS score per finding is 4.73.
for our Manufacturing industry clients. investigating by our analysts as True Positive
▪
▪  Internal threat actors accounted for more than half of the Manufacturing True Positive incidents.   incidents. Pentesting reports 2 risks rated Critical on average.
|     | ▪   | ▪  On average 1.4 risks were rated High. |
| --- | --- | ---------------------------------------- |
This ties in with the high proportion of incidents categorized as Misuse. Hacking (35%) & Malware (17%) made up more
|                      | than half of Professional, Scientific, and Technical  | ▪  2.44 risks were rated Low on average.  |
| -------------------- | ----------------------------------------------------- | ----------------------------------------- |
| VOC Industry Ranking | Services incidents.                                   | ▪                                         |
4 risks were rated Medium on average.
▪
Manufacturing placed third in terms of lowest average vulnerability score. ▪  When it came to threat actor, both External (45%) and
▪  On average we saw 15.13 findings per asset.  Internal (43%) actors were very close proportionally.
▪  That is 53% less findings per asset than the industry average.
▪
The average vulnerability in Manufacturing lives for approximately 3 months on average.
VOC Industry Ranking
▪
Manufacturing has vulnerabilities as old as 4 years or 1457 days.
▪  We saw 7.06 findings per asset on average
▪  The average age per finding for Manufacturing is 1.19 times higher than the industry average.
▪
Professional, Scientific, and Technical Services
▪  This industry has a vulnerability score that is 19% lower than the average.
has 78% less findings per asset than the industry
▪
Manufacturing averages 4 Critical rated findings per asset, 25.3 rated High, rated 6.6 Medium and  average.
| 1.9 rated Low. | ▪   |     |
| -------------- | --- | --- |
The average vulnerability lives for 7 months.
▪
Pentesting Industry Ranking Some vulnerabilities are older than 3.5 years.
▪
The average age per finding is 1.58 times higher than
NOTE we do not have enough data for a meaningful analysis.
the industry average.
▪  our testers saw an average of 5 findings per assessment.
▪
Professional, Scientific, and Technical Services
▪  Manufacturing sees 35% fewer findings than the average for a pentest.
has a vulnerability score that is 68% lower than the
▪
| The average CVSS score per finding was 4.22. | average. |     |
| -------------------------------------------- | -------- | --- |
| ▪                                            | ▪        |     |
Manufacturing pentest projects report 3 risks rated Low on average. On average we see 3 Critical rated findings per asset,
▪  Manufacturing pentest projects report 2 risks rated Medium on average. 7.5 were rated High, 5.2 Medium and 3.6 rated Low.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

86 Security Navigator 2024 87
Industry Scorecard
Health Care and
Social Assistance
Cy-X Industry ranking Cy-X victim delta
Health Care and Social Assistance is in 6th Compared to last year, resulting in the move up
place this year with from 7th place to 6th, we see an increase in
5% of all victims + 61%
Most affected sub industry
Unfortunately Hospitals made up most of all victims in the Health Care and
Industry Scorecard
Social Assistance industry with
Educational Services
20% of all victims.
CyberSOC Industry Ranking Pentesting Industry Ranking
Cy-X Industry ranking Cy-X victim delta
▪ With 6,000 total incidents, Health Care and Social ▪ Health Care has an average of 4.86 findings per
Assistance were 5th highest, 16 % of those incidents pentest. The fourth highest attacked industry is This industry climbed from 8th to 4th most
were identified as being True Positive. ▪ We see 38% fewer findings than the average pentest Educational Services, representing affected, representing a growth of
▪ Hacking was by far the biggest threat action reported, ▪ The average CVSS score per finding is 4.64. 6% of victims + 115%
with 65% of all True Positive incidents.
▪ Pentest projects on average report 1 risks rated
▪ Three quarters of the threat actors for Health Care and Critical on average, 2 risks rated High, 2.33 risks rated
Social Care incidents were classified as External. Medium and 2.83 risks rated Low.
VOC Industry Ranking Most affected sub industry
NOTE: we do not have enough data for Three quarters of all Educational Services victims are made up of
a meaningful analysis. institutions from
▪ Health Care averages 19 findings per asset. Colleges, Universities and Professional
▪ We see the lowest maximum finding age of
Schools combined with Elementary and
less than 1 year.
▪ Health Care beats the industry vulnerability score Secondary Schools.
average by 47%.
▪ We note the third highest average finding age of
244.04 days, that is 2.12 times higher than the average. VOC Industry Ranking
▪ We recorded zero findings per asset rated Critical. NOTE: we do not have enough data for
▪ 1 finding per asset was rated High, 14.5 findings per a meaningful analysis
asset were rated Medium and 30.2 Low. ▪ Educational Services averages 1.94 findings per asset.
▪ The maximum finding age is more than 2.5 years.
▪ We see an average finding age of almost 5 months.
▪ The finding age is 1.2 times higher than average.
▪ 3 findings per asset were rated Critical, 2.2 were rated High, 1.2
were rated Medium and 1.1 were rated Low.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

88 Security Navigator 2024 89
Industry Scorecard
Industry Scorecard
Finance and Insurance
Public Administration
Cy-X industry ranking Cy-X victim delta
At around 64% less than top placed Compared to last year Finance has moved up
Cy-X industry ranking Cy-X victim delta
Manufacturing we find this industry with to the third place in with an increase of
7% of all Public Administration featured in 12th place As a proportion, Public Administration
+ 106%
of Cy-X victims we recorded with just victims dropped from 10th to 12th place this
year, despite seeing 18 victims more, an
known victims 3% of the total
increase of
+ 22%
Most affected sub industry
Most affected sub industry
Within Finance & Insurance, 3 subsectors dominated.
Victims in the Executive, Legislative and Other General Government Support sector are top of the pile
Credit Intermediation made up 38%, interestingly Insurance Carriers
in the Public Administration with 58% of victims part of this sector. Perhaps worryingly,
had 32% with Securities, Commodity Contracts and Other Financial almost 8% of victims aligned with the National Security and
Investments completing the top 3 with 24%. International Affairs subsector.
CyberSOC Industry Ranking
CyberSOC Industry Ranking
▪ Finance and Insurance ranked second for total number of incidents, although the total was less than half that ▪ We recorded less than 5,000 incidents for clients in the Public Administration space, with less than
of Manufacturing, and only around 12% of those incidents were confirmed as True Positive.
a third of these being confirmed as True Positive.
▪ The Hacking (49%) Threat Action made up the majority of the True Positive incidents. A fairly distant second ▪ Hacking, Malware & Misuse were all quite close as threat actions for the True Positive incidents,
came Malware with 22%.
with 19%, 16% & 16% respectively.
▪ External threat actors were identified for 65% of the True Positive incidents. ▪ In line with the threat actions, threat actors were also equally dispersed, showing External with
39% and Internal 37%.
VOC Industry Ranking
▪ Finance and Insurance averages 43.3 findings per asset. VOC Industry Ranking
▪ That is 1.36 times more findings per asset than the industry average. ▪ This industry averages 35.3 findings per asset.
▪ We see the youngest average age of 54.3 days per finding. ▪ Public Administration beats industry vulnerability score average by 14%.
▪ The oldest findings as old as 4 years. ▪ We see an average age per finding of almost 6 months.
▪ The average age per finding is 2.31 times lower than industry average. ▪ The average finding age is 1.46 times higher than the average.
▪ The vulnerability score is 1.4 time higher than the average. ▪ The max unique finding age peaks at 1420 days.
▪ 9.5 findings per asset were rated Critical, 31 were rated High, 15.2 Mediumand 5 .2 rated Low. ▪ We see 5.2 findings per asset rated Critical, 15.2 findings rated High, 17.4 findings rated Medium
and 3.8 rated Low.
Pentesting Industry Ranking
▪ Finance and Insurance has an average of 6.44 findings per pentest. Pentesting Industry Ranking
▪ We see 16% fewer findings than in the average pentest. ▪ Public Administration has an average of 5.56 findings per pentest.
▪ The average CVSS score per finding was 5.13. ▪ We see 28% fewer findings than in the average pentest.
▪ 1.38 risks were rated Critical on average, 2.25 risks rated High on average, 3.92 risks were rated Medium and ▪ The average CVSS score per finding is 5.10.
2.55 were rated Low. ▪ Public Administration pentest projects report 2.5 risks rated Critical on average, 2.33 rated High,
3.42 rated Medium and 1.9 risks rated Low.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

90 Security Navigator 2024 91
Industry Scorecard
Construction
Cy-X industry ranking Cy-X victim delta
This year Construction came in at 7th As a proportion of all victims construction fell
place with from 4th place to 7th, but still had a growth in
victims of
5% of the
+ 33%
victims
VOC Industry Ranking
▪ Construction averages 12.12 findings per asset.
▪ This industry beats the vulnerability score average by more than 70%.
▪ The average vulnerability age for Construction is almost 4 months. Industry Scorecard
▪ The average finding age for Construction is 3% lower than the average.
Retail
▪ Construction has unpatched vulnerabilities as old as 1.5 years.
▪ We see 3 Critical findings, 7.5 High findings, 5.2 Medium findings and 3.6 Low findings per asset.
Pentesting Industry Ranking
NOTE: we do not have enough data for a meaningful analysis. Cy-X industry ranking Cy-X victim delta
▪ Construction has an average of 9 findings per pentest. The Retail vertical saw significantly fewer Interstingly this is the only vertical in which we
▪ The report lists 1.16 times more findings than the average pentest report. victims than our top 2 industries, so we see observed a drop in the number of victims by
▪ The test revealed an average CVSS score per finding of 4.6. them in the 9th place. It represents 139, which is
▪ 4 risks were rated High and 5 risks were rated Medium.
4% of the - 20%
victims
CyberSOC Industry Ranking
▪ With over 17,000 total incidents recorded, the Retail sector was third highest. However looking at confirmed
True Positive incidents they came in second behind Manufacturing with 5,376.
▪ Hacking and Misuse threat actions combined made up almost a third of True Positive incidents.
Pentesting Industry Ranking
NOTE: we do not have enough data for a meaningful analysis.
▪ We saw an average of 10 findings in the pentests.
▪ The reports list 1.29 times more findings than the industry average.
▪ Retail has an average CVSS score per finding of 5.79.
▪ We see on average 2.5 risks rated High on average, 12 risks rated Medium and 3 risks rated Low.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

92 Security Navigator 2024 Expert voice: South Africa 93
Hacking the Human Mind
Formula for attack
To describe the modus operandi for attackers targeting humans, we can formulate simple formulas.
A standard attacker formula will be as follows:
Exploiting Vulnerabilities in the
(Target) + (Vulnerability) + (Exploit) = Compromise
‘First Line of Cyber Defense’
But when applied to the human it could be as follows:
Humans are a complex beings with consciousness, emotions, and the capacity to act based Intended Objective
on thoughts. In the ever-evolving realm of cybersecurity, humans consistently remain primary (Human Mind) + (Emotional + En ( g S in o e c e ia r l ing = through
targets for attackers. Over the years, these attackers have developed their expertise in exploiting Trigger/Trait) Resultant Reaction
Technique)
various human qualities, sharpening their skills to manipulate biases and emotional triggers with
the objective of influencing human behaviour to compromise security whether it be personal and
organizational security.
Ulrich Swart, Training Manager & Technical Team Leader, Orange Cyberdefense
The attack chain is apparent by looking at how these formulas relate
to triggers and techniques in combination with vulnerabilities.
More than just a 'human factor' I think, therefore I can be manipulated
Cognitive Emotional Exploitation
Understanding what defines our humanity, recognizing Attackers exploit this safety net (emotions and fundamental Example
Influence Triggers Techniques
how our qualities can be perceived as vulnerabilities, and traits) when targeting humans, as it can be manipulated to fulfil
comprehending how our minds can be targeted provide the their objectives. This safety net weakens even more when we Link to download a donation form to help
Trust, Empathy & Using goodwill or
foundation for identifying and responding when we inevitably venture into the "online" realm, as certain safeguards fail due Reciprocation humanitarian aid or asking for money back
Guilt asking for help
become the target. to a lack of insight. The abstraction of communication through after a fake payment was made in excess.
a name on screen often misleads our minds in interpreting Email made to look as if it is from Microsoft indi-
The human mind is a complex landscape that evolved over Using legitimate context or
situations in a way that our emotions cannot accurately Authority Trust & Urgency cating your account is compromised and you
years of exposure to the natural environment, interactions form of power
navigate. should act.
with others, and lessons drawn from past experiences.
In the realm of manipulation, various models and methods have Using an Limited offer to win a house if you pay £50 now
As humans, our minds set us apart, marked by a multitude Scarcity Greed & Urgency
been employed over centuries to influence human behaviour. irresistible offer or clicking a link.
of traits and emotions, often too complicated to articulate
In today's context, attackers exploit these models to identify Call about wanting to improve asking for informa-
precisely. Commitment & Using an improvement
human vulnerabilities, characterised as weaknesses within the Vulnerability & Ego tion about work and personal life which can be
Human behaviour is complex system that can be exploited. Consistency or advantage sensitive.
In addition to directly manipulating fundamental traits through Trust & Using causes Impersonating a friend to ask you to open a file or
Some of our fundamental traits can be outlined as follows: Liking
carefully targeted attacks, attackers tend to target humans Vulnerability or loved ones do something you’ll only do for close connections.
▪ Trust – Humans place their trust in others, assuming
through forms of influence and persuasion. These can be
Threatens to expose something about you or offer
inherent goodness. summarised as follows, and humans tend to operate mentally Social Proof Ego & Guilt Using status or threats
to get you mentioned somewhere important.
▪ Empathy – Humans exhibit care for others in these realms:
and their feelings. ▪ Reciprocation – Humans feel compelled to reciprocate Exploitation techniques, often seen in digital channels like email, phone calls, or text messages, are frequently used for
▪ Ego – Humans harbour a competitive spirit, aspiring what they have received. phishing. These tactics manipulate established interactions to achieve various objectives, such as deceiving individuals into
to outshine their peers. ▪ Authority – Humans are inclined to comply with parting with funds, opening malicious files, submitting credentials, or revealing sensitive data. The consequences of these
▪ Guilt – Humans experience remorse for their actions, authoritative/known figures. attacks can vary from individual losses to organizational breaches.
especially when they harm others. ▪ Scarcity – Humans desire items that are less attainable.
▪ Greed – Humans desire possessions and may ▪ Commitment & Consistency – Humans favor routine and
succumb to impulsivity.
structure.
▪ Urgency – Humans respond promptly to situations ▪ Liking – Humans form emotional connections. Defending ourselves
demanding immediate attention.
▪ Social Proof – Humans seek validation and fame.
▪ Vulnerability – Humans often grapple with fear To safeguard against these attacks against our minds, we should align our
and are candid about their emotions. These aspects can be viewed as potential vulnerabilities in the cognitive standards with emotional triggers by asking questions like; what is
human mind when combined with emotions and fundamental the purpose, expectation, and legitimacy of the interaction. These questions
While this list is not exhaustive, it summarises common and traits. Attackers leverage these aspects to gain direct control could prevent impulsive reactions and allow introspection.
understandable aspects that drive human behaviour. Human over our actions, an occurrence now recognised as social
interactions hold essential value, instilling life with significance engineering. Establishing a "stop and assess" mentality acts as a mental firewall,
and advancing cultural norms. However, for attackers seeking strengthened by vigilance, to enhance personal and organizational
Social engineering encompasses various techniques and
to exploit us, the social construct of human-to-human security. By considering potential attacks, we heighten our awareness
tactics, yet at its core, it exploits one or more of the areas
interactions provides a pathway for manipulation. of vulnerabilities and work on resilience. This awareness, coupled with
mentioned above through accurately crafted interactions.
Our naturally social nature forces us to revert to these traits. a proactive approach, helps mitigate threats to our minds and humanity,
Emotions serve as a safety net for communication, problem- promoting collaboration to disarm attackers and weaken their operations.
solving, and connections in our everyday life and we have come
Stay vigilant, stay informed, and continue to question everything.
to trust our emotional responses to further guide and protect us
in a variety of situations.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

94 Security Navigator 2024 Why aren’t we more effective in defending against Cyber Extortion? 95
Diana Selck-Paulsson
Lead Security Researcher
Orange Cyberdefense
Data analysis:
Why aren’t we
more effective in
defending against
Cyber Extortion?
An alarming surge in Cyber Extortion in Q1 2023 led us to believe
that there was reason enough to dedicate a paper to this problem
– looking beyond the typical, technical aspect of "Ransomware”,
to understand the true nature of this crime – so we produced our
detailed Cy-Xplorer report.
Now, half a year has passed. So what has happened since then?
Let's once again take a look at the crime scenes, victims and
round up the usual suspects.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

Cyber Extortion has surged to unseen levels, despite efforts In the last two and a half years we’ve seen a steady increase
made to disrupt this form of cybercrime. The question arises: in LE activity. We recorded 102 actions that we have
what do current efforts to disrupt this ecosystem look like? been connecting to counter cybercrime in some way. We
We will focus mostly on actions taken by government and documented the type of crime, which the action was taken
law enforcement agencies, however it should also be noted against (e.g. Fraud, Crypto, Cy-X) and what actions the LE
that other entities are also responding to the current threat. operation took to achieve its goal (arrest, takedown, an
Therefore, we’ll explore all of the responses we have seen in the individual was extradited, etc.). As can be seen below, LE
past 12 months and investigate whether or not they have been activity increased noticeably by Q4 2022 and there has been a
successful or have the potential to disrupt the ecosystem in the steady increase in efforts to combat cybercrime ever since.
near future.
We see Cyber Extortion as the number one crime type being
fought against with 15% of all LE actions in our humble dataset.
Law enforcement efforts Cy-X is closely followed by Hacking and Crypto which each
claimed a share of 12%, and Fraud with 11%; and 9% of all
We’ve been tracking Law Enforcement (LE) activities for a LE activity we recorded had to do with dark web or clear web
while now to determine whether the actions they’ve taken sites or marketplaces. In 2023, we specifically noted increased
have any disruptive impact on the cybercrime ecosystem. We efforts to take down or disrupt the infrastructure and hosting
see increased activity by governments, local authorities, and services Threat Actors (mis-)used.
international collaborations with the goal of fighting some of the
types of cybercrime we have been witnessing in the past two A more telling metric is perhaps what actions were taken
and a half years. Our observations are based on news articles against those forms of crime we mentioned above. Here, we
reporting on the counter measures taken against various forms recorded that almost 60% of LE activities were announcements
of cybercrime and criminal actors. We are not aware of any of arrests and the sentencing of individuals or groups. This is
comprehensive and open access list of activities, so we started a positive observation because prosecution potentially has a
our own dataset this year by looking at two and a half years of deterrent effect on other Threat Actors, especially very young
news coverage on LE activities and government collaborations. (potential) offenders.
Focus of Law Enforcement
Types of cyber crime Law Enforcement activities targeted in recent years
12
10
8
6
4
2
0
naJ beF guA peS tkO beF raM rpA yaM nuJ luJ guA peS tkO voN ceD naJ beF raM rpA yaM nuJ luJ guA peS
96 Security Navigator 2024 97
Types of defense activities
Proportion of different types of Law Enforcement activities observed
39.22% Arrest
3%
3%
20.59% Sentenced
5%
14.71% Takedown
5%
6.86% Other
39%
4.90% Law enforcement disrupts
7%
4.90% Extradited
2.94% Lawsuit
2.94% Sanctions 15%
0.98% Cryptocrime fighting activity
0.98% Wanted
20% 0.98% Seizure
The third most common LE action in our dataset is takedowns First of all, others tried to jump onto the ‘brand’ and its
(15%). These actions targeted dark web marketplaces and reputation and began copying the appearance of Hive’s leak
sites, Cryptocurrency tumblers, and botnets such as Qakbot[59], site (RansomHouse). Secondly, a re-brand of Hive surfaced
which was dismantled in 2023. The Qakbot takedown was a in October 2023, 10 months after Hive was disrupted. The
significant milestone in the potential of LE agencies’ evolving re-brand is called Hunters International[62][63] and so far has
capabilities. victimized two organizations, one in Europe and one in the
U.S. Their malware code matches 94% of that used previously
Besides ‘traditional’ LE activity, we also observed increased
by Hive[64], but according to Hunters International themselves,
government activities focusing on disruption. This became
they bought the code from Hive, fixed it and are otherwise
especially evident after the takedown of the threat actor group
not connected to the Hive operation or their members. In a
‘Hive’ in January 2023, which was a result of a collaborative
2021 2022 2023 statement from the 24th of October, they say:
effort by EUROPOL, the German, Dutch and U.S. authorities[60]
and others. Hive was something different, here we saw
authorities, namely the FBI, infiltrating Hive’s network and
“We started to see that someone falsely decided that we
remaining undetected for a significant period of time. This
are the Hive ransomware group based on a 60% similarity
‘hacking back’ operation included the capture of decryption
of encryption code. All of the Hive source codes were sold
keys and helping over 300 victims to decrypt their data whilst
including the website and old Golang and C versions and we
still under attack by Hive, in addition to seizing control of the
are those who purchased them.
servers and websites that Hive used to communicate. The
subsequent announcement by the U.S . Department of Justice Unfortunately for us, we found a lot of mistakes that caused
(DOJ) emphasized prioritizing disruption and seizures over unavailability for decryption in some cases. All of them were
other, longer-lasting investigations[61]. fixed now. As you may see here, encryption is not our primary
goal, that's why we didn't do it by ourselves.”
This disruptive activity has shown some impact. For instance,
they took down the Hive operations and helped hundreds, if not Hunters International leak site, under “News”
thousands of victims afterwards by providing the decryption
keys. They also most likely learned a lot of the group's Tactics,
As a side note, what the Hive hack showed us besides the
Techniques and Procedures (TTP), given the fact that they
attempt to disrupt them was the amount of victims they had
had been in their network for several months before taking
compromised and encrypted. At the time of infiltration by the
them down in January 2023. However, no arrests were made.
FBI, 300 victims were still under attack and 1000 victims had
While this particular law enforcement action was unique and
already suffered from an attack. The FBI provided a total of
significant; if the individuals who ran this Cyber Extortion
1300 victims with a decryption key[65]. In our our records, we
Cy-X BEC Fraud DDoS Infrastructure, Hosting Services operation are still on the loose, chances are that they have re-
registered 208 organizations that had fallen victim to Hive,
Carding Phishing Crypto Dark web marketplace or sites Bots grouped and potentially begun operating under a new name.
which makes the actual number of victims 5x higher! This
Money Laundering Malware Hacking Other This is fairly common for this ecosystem and most likely one of
is an important insight into the problem of not knowing how big
the biggest challenges for law enforcement agencies and their
the problem actually is and gives us an indication of how high
efforts to disrupt this form of crime effectively. There are two
the 'dark number' of victims really is.
things to observe for the Hive operation and their takedown.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

98 Security Navigator 2024 Why aren’t we more effective in defending against Cyber Extortion? 99
Government efforts Fighting each other: Finally, we have ransomware / Cyber Extortion groups that
have turned from purely financially driven to more politically
a vigilante response?
In the last week of October 2023, the Biden administration directed activities. Examples include Conti, CoomingProject
hosted officials from 50 countries for its ‘International Counter and Stormous, who proclaimed their full support for Russia
Besides a direct response of law enforcement agencies and a
Ransomware Initiative’ (CRI) to discuss potential future policies in their war against Ukraine[71]. Ransomedvc posted publicly
collective effort of certain governments against the increasing
on regulating ransom payments and information sharing[66]. On in their Telegram channel that they want to buy access for
threat of Cyber Extortion and ransomware, we have seen other
November 1st, just in the final days of writing this report, the Iran or Palestine after the Hamas-Israel war broke out, which
types of responses.
White House announced that more than 40 countries had signed may indicate that the group might have picked its side and is
an agreement pledging not to use central government funds to One observation that we are making is a recent event where planning to attack organizations in Iran and Palestine.
pay ransoms to cybercriminals[67]. a hacktivist group has taken actions into their own hands and
took down a Cyber Extortion operation in October 2023. The
Countries want to lead by example by not paying the demanded
pro-Ukraine hacktivist group called Ukrainian Cyber Alliance
ransom and thus stopping the funding of this criminal
apparently took down the Trigona ransomware leak site and its
ecosystem. While this commitment has a big potential to disrupt
servers. This action was accompanied by the statement “[…]
the ecosystem, it still remains to be seen how effective it will be
disrupting Russian enterprises (both public and private) since
in the long-term. Denying ransom payments to Threat Actors
2014.”[68]
that are in the majority financially motivated, can potentially
have an enormous impact. Leading by example is a good start.
However, if we compare the proportion of public and private
organizations in our victim dataset; we see that the public sector
only represents 3%. Most of the impact of those attacks had to
be endured and dealt with by the private sector. And another example is Cuba ransomware, whose group
members began targeting government and military officials in
Nevertheless, a collective effort as we see with the CRI 2023
Ukraine for espionage[72][73].
is exactly what is needed. Besides the above-mentioned
agreement to not pay ransom demands, other efforts are equally The Trigona case is still slightly different, in the sense that one
important. Some of the key CRI deliverables of this year’s group took down another group in a vigilante-style operation.
meeting were: Like Law Enforcement activities that are similarly disruptive in
▪ Developing capabilities with the help of technology, e.g. nature, the challenge for them is that such takedowns might
Artificial Intelligence (AI) and training only be temporary. Additionally, it can always be an opportunity
▪ Sharing information via dedicated platforms for someone else to fill that void or for the same Threat Actors
to re-organize and re-brand. It’s important to highlight that the
▪ Developing fighting back capabilities, e.g. share blacklists of
Trigona take down was not an action against cybercrime but
wallets used by ransomware actors, assist any CRI member
was part of a politically driven effort to disrupt any Russian
with incident response if government or lifeline sectors are
cyber operation. Nevertheless, it was an action of disruption.
suffering a ransomware attack
Given the current geopolitical situation and the number
The CRI deliverables of 2023 are very important efforts that of individuals and groups taking part in geopolitical cyber
will hopefully show their potential in the long run. We are very operations; we anticipate seeing more of these actions
curious to see what effect it has on the current Cyber Extortion in the future.
ecosystem.
Reminding everyone on their
responsibilities during war
And then another final observation we made in terms of who
responds to the current threat landscape; we saw that the
This is not the first time we’ve seen “crossovers” between
International Committee of the Red Cross (ICRC) published a
hacktivist groups and ransomware / Cyber Extortion
guideline for anyone participating in hostilities by the means
operations. For example, hacktivist groups such as Anonymous
of cyber[74]. As we have stated in several places of this report,
Sudan have demanded ransoms to stop their ongoing DDoS
2023 has shown how messy cyber space has become. This
attacks[69]. Another hacktivist group, GhostSec, turned
is mostly due to the ongoing war against Ukraine, which
towards ransomware, and has released its own variant, called
mobilized many different Threat Actors to support either side
GhostLocker, as a self-proclaimed “next-gen Ransomware-
of the conflict, but we see similar activity in the most recent
as-a-Service” operation. GhostSec advertise their locker with
Hamas-Israel war.
the following capabilities: “robust military-grade encryption,
undetectable by major AVs, fast C-coded locker for rapid
execution, GhostMorph Polymorphic Engine for unmatched
stealth”, to mention a few. This makes GhostLocker a
service to be taken seriously and watched closely. GhostSec
belongs to the Anonymous hacktivist collective, and at least
one other hacktivist group, Stormous, who belongs to the
same collective, has announced that they also intend to use
GhostLocker[70].
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

100 Security Navigator 2024 Why aren’t we more effective in defending against Cyber Extortion? 101
In the context of Cy-X, we see how current geopolitical events Is it (im)possible to We gained three insights: However, while in the 2022 period, we saw more persistent
have politicized some actors[75], who until recently were groups than new ones; in 2023 that has changed. In fact, we
disrupt a dynamic ecosystem? 1. Groups that only started extorting in the past 12 months;
financially focused in their actions but have become more see the opposite proportion of activity. We see many more new
we called “new”.
politically driven. groups (which was our feeling all along) than we see persistent
We have explored the side of law enforcement and government
groups or groups that have closed down operations. But at the
Aa a result, the latest “crossovers” between Cyber Extortionists responses, highlighting how difficult it can be if the ecosystem 2. Groups that we have not seen active in the past 12 months;
same time, we observe less persistent groups in 2023; which
and hacktivists but also the intensification of hacktivist activity is so effective in causing such a high amount of victims yet at we called “gone”.
in itself does not change the fact that there are other active
generally in recent conflicts, did not remain unnoticed; others the same time still managing to remain so flexible. As we have
groups about, e.g. the new ones, extorting victims. In fact, it
observing the same concerning trends. argued previously, it’s an opportunistic crime. One’s takedown 3. Groups that we are still seeing active over a period of 12
increases the problem, since we see a higher number of active
and inability to participate in the criminal market of victimizing months and longer, we called “persistent”.
As a response, the ICRC has posted a guide of 8 rules for groups (2023: 54) than we saw in 2022 (48). And finally, similar
organizations for millions of USD; is another’s opportunity. We
“civilian hackers” during war, and 4 obligations for states to are long aware of this dynamic. It also does not help that many Below we show the results of this investigation into the to our argument of opportunity, we see many more new groups
restrain them, written by Tilman Rodenhäuser and Mauro operations are run as a cybercrime-as-a-service operation movements of Threat Actor Groups of the past 3 years. active in this criminal space than we see groups being closed
Vignati[76]. They are emphasizing the importance that even or choosing to close operations.
thus increasing their efficiency by outsourcing certain attack
in times of war, civilian hackers must respect the law of the Actor lifecycle changes
stages, e.g. Initial Access, to others who have specialized in Consequently, Cyber Extortion seems lucrative enough for new
countries they are in, or where the national laws are not
it. The adoption of affiliates who then help increase covering Persistent New Gone groups or slightly new groups (re-brands) wanting to join this
enforced, or being disregarded in times of armed conflict,
more 'victim ground', has certainly had an impact on the sheer ecosystem.
international humanitarian law (IHL) provides a set of rules to 60 2022 2023
number of victims. Through this, the ecosystem as such can be
safeguard civilians, soldiers and others from war. For the curious minds, below are some examples of groups we
perceived to be bigger than it actually is.
classified for the past 12 months.
Consequently, this is addressing two issues at hand, first of all 50
A good example of this is that we see almost the same number
we are witnessing civilian hackers execute cyber operations in
of Threat Actor Groups participating in Cyber Extortion in 2023 Examples of “New” (and re-brand) groups:
an armed conflict. Participating directly in hostilities[77] means
that participants have the potential to cause real harm against a th s e w v e ic s ti a m w n 2 u m ye b a e rs rs a h g a o v ( e in i n a c y re e a a s r e o d n s y o e a m r u c c o h m t p h a a r t i s it o s n e ). e H m o s w th e a ve t r, 40 22 31 Play, Royal, Akira, etc.
civilians, risk exposing themselves and people close to them
more individuals and groups of individuals have joined the Cy-X
Examples of “Gone” groups:
to military operations; and hence the risk for civilians grows. party. That is in fact not the case in our two-year comparison. 30
Secondly, civilian hackers do not live in cyber space and
But noteworthy, the Threat Actors that extorted victims two Conti, Pysa, Grief, etc.
should comply to national laws, states should not encourage or
years ago, are of course not the same constellation of Threat
20
tolerate hackers conducting cyber operations in armed conflict, Actor we now observe in 2023. By tracking Cyber Extortion Examples of “Persistent” groups:
say the authors.
operations as actively as we do, we do feel that the sheer 26
23 LockBit3, ALPHV(BlackCat), BlackBasta, etc.
They continue, stating: amount of new leak sites we had to add to our tracker has 10
exceeded anything we did in previous years.
New name, new threat profile
Therefore, we started to investigate this, tracking all the Threat 0
Actor Groups we have been collecting in the last 3 years to see Often re-branding helps threat actors to “start over” and/
if we can track the threat actor movements. For this we began or cover their tracks. In some cases, vulnerabilities in their
looking at groups we tracked between 1st of October 2020 -10 -23 -25 encryption or weak OpSec in their own operations will motivate
“Any State that is committed to the rule of law or
to 30th of September 2021 and called this time frame “2021”. Threat Actors to close operations and “come back” under a
a ‘rules-based international order’ must not close
We continued doing this for the next two years, which gave us -20 slightly different name/brand, sometimes in different settings
its eyes when people on its territory conduct cyber
an overview of which threat actor groups were active in each (new developer team, etc.).
operations in disregard of national or international
respective year (2021, 2022, 2023). We then compared 2021 to
law, even if directed against an adversary .” -30 One example that we have been tracking since 2020, both in
2022 to check whether or not the groups we observed in 2021
terms of victimology but also Threat Actor Group attribution[80],
Tilman Rodenhäuser and Mauro Vignati [78] were still active 12 months later. This gave us the 2022 actor Interestingly, we see different movements in both periods, as is the Cyber Extortion operation currently known under the
distribution. We repeated this calculation with 2022 to 2023, was our expectation (as can be seen above). In 2022, we saw
name ALPHV aka BlackCat. In 2020, this group was known
which resulted in the 2023 actor distribution 26 persistent threat actors that we had already observed and
as DarkSide, which re-branded and began victimizing
monitored the year before. A similar number of groups, 23,
organizations - most recognized victim being Colonial
closed operations during that time, and we tracked 22 new
Pipeline - under the DarkSide brand in 2021. And shortly after
groups that weren’t active the year before. It’s noteworthy that
DarkSide closed operations in July 2021, BlackMatter began
new groups don’t necessarily have to be entirely new but can
extorting victims between August 2021 and October 2021. Just
be a re-brand of an old group. Our CERT team tracks new
one month after, in November 2021, the new brand "ALPHV
groups and re-brands and other aspects in a cartography that
(BlackCat)" began extorting victims[81].
can be found on GitHub[79].
What does that mean for the actor movements between
2022 and 2023? The almost equal number of groups which
perished and groups that began their criminal operations
underlines an argument we have been making for some time:
It’s very opportunistic and gaps are very quickly filled by other
motivated Threat Actors.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

102 Security Navigator 2024 Why aren’t we more effective in defending against Cyber Extortion? 103
Frequency of posting victims
Victims posted by DarkSide, BlackMatter and ALPHV(BlackCat) over time
ALPHV (BlackCat) BlackMatter Darkside
60
2020 2021 2022 2023
50
40
30
20
10
0
Conclusion
Qtr1Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3 Qtr4 Qtr1 Qtr2 Qtr3
Lifespan of actor groups As we have shown, Cyber Extortion is a complex ecosystem that is under
constant evolution. At the same time, it is a serious problem, especially for
Amount of groups and their life-span in months private organizations globally. The volumes of victims do not seem to decrease,
in fact we see the opposite with significant increases in victim count that are
60%
unproportional to the increase of Threat Actors participating in the crime of
54% extortion. We therefore conclude that the ecosystem, as fast paced as it is, has
become much more effective than the defending entities. Even though we do see
50% increasing efforts by law enforcement agencies and local authorities, especially
in the fight against ransomware / Cyber Extortion; we don’t see any significant
effect yet.
40%
However, there are some promising trends that potentially could have an
impact in the near future. The most promising efforts are those that are
taken collectively, just as cybercriminals use and re-use their resources and
30%
capabilities, so should we as defenders. Witnessing the successful LE actions
and collaboration between different law enforcement agencies and countries
21%
shows that collectively we can have an impact. Additionally, we see governments
20% committing and joining the fight against Cyber Extortion, hopefully helping by
sharing information, training, and developing technologies that can assist with
this goal and positively impact the efforts.
10%
9%
10%
In the end, it still remains a big challenge, investigations can be lengthy and thus
4% disproportionate to the actual lifespan of criminal groups. Disruptive efforts and
1% 1% 1% takedown definitely have an impact but in cases where no arrests are made,
0% 1-6 7-12 13-18 19-24 25-30 31-36 37-42 43-48 individuals have the chance to re-organize themselves and continue extorting
victims. We have seen several arrests in the past 2,5 years which shows the effect
of efforts and at the same time can have a deterrent effect for future offenders.
Given the fact that we do see a lot of movements, what kind of This highlights the challenges for anyone defending against or
lifespan do these operations have, especially when we consider attempting to disrupt Cyber Extortion operations. By the time Alternatives, such as publishing guidelines and appealing to states and
their age (in months)? We looked at all Threat Actor Groups we one realizes that they have become a real problem, impacting individuals engaging in crime or even hostilities in times of armed conflicts, as we
have collected in our victim dataset since January 2020. We organizations around the world, half of the Threat Actor Groups are experiencing now, are also important to raise and remind.
tracked a total of 110 different operations since then. Of those, have closed operation within the first 6 months. The average
we wanted to know what their lifespan looked like, for this we age in months of all the tracked Cyber Extortion operations is 9 As we have studied the current threat landscape of Cyber Extortion, we
split the lifespan into 6 month intervals. months. Of the groups that have made it the longest, we in fact unfortunately need to admit that current efforts to disrupt the Cy-X ecosystem
only see one Threat Actor Group, which has been active more have not shown any effect when looking at the ever-high victim count.
Interestingly, half of all the Cyber Extortion operations only than 43 months and that is Cl0p – who at the time of writing are Nevertheless, the defender’s space has become at least as busy as the offenders
made it to the first 6 months. Another 21% had a lifespan of still active. The second oldest Threat Actor Group representing space; which hopefully means that in the (near) future those efforts will show
7-12 months. 10% of all operations made it to the age of 13-18 the 1% within the 37-42 months lifespan was RagnarLocker, effect.
months. As can be seen above, only a very few make it to 2
who at the time of writing had just been dismantled on the 20th
years and older.
of October 2023[82].
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

104 Security Navigator 2024 Expert voice: France 105
Once the OT is reached, the penetration tester first needs to identify its technical assets. She looks for
workstations and servers as she would do on IT, but also for industrial components. This includes soft-
Hacking a factory
ware, protocols, and devices such as programmable logic controllers (PLCs), HMIs, actuators, sensors,
and any type of equipment that is not an IT asset . This discovery phase is usually conducted with the
help of network scans.
A safe way to testing ICS/OT environments
However, as we discussed before, such an environment is likely to include old devices, and sending
them unexpected network traffic may have harmful side effects. For this reason, additional information is
required beforehand to locate critical or sensitive components. The auditor will still explore the network
as an attacker would, but she will exclude or be careful with assets that could become unstable and
take extra measures when contacting components (run restricted and targeted scans, use only genuine
The number of known malware targeting industrial systems keeps on increasing and was
tooling, etc.). It is also important that a technical contact is available at any time on site during the
intensified in 2022 due to the war against Ukraine[83]. These systems, also referred to as
assessment. This person is contacted immediately in case of a suspected issue.
Operational Technology (OT), differ from the Information Technology (IT) that we are familiar
with and can be described as hardware and software components used to control physical and
mechanical processes. It includes equipment, protocols, software, and processes specifically
used in manufacturing, energy, transportation, or even building management systems.
Claire Vacherot, Security Auditor, Orange Cyberdefense
The next step for the auditor is to search for vulnerabilities. The main
difference with penetration tests on IT is that, here, she does not do any
malicious operation nor action that may have side effects. For instance, it
is strictly forbidden to run a man-in-the-middle attack to intercept traffic in
Used to be an island Penetration tests on industrial systems industrial networks, while this is a common test on IT networks. So, how is a
must be carried out with utmost care, test conducted?
Historically, OT systems used to be closed, standalone preferably on environments under
systems. They eventually became interconnected and started maintenance or on a test bench. From our experience, we noticed that most of the time, an attacker who can
using IT standards in addition to their own, to simplify the reach an industrial component on the network is already able to misuse it or
processes of supervision, operation and maintenance. In other make it unavailable. Thus, the auditor first tries to reach as many components
When performed on a running environment, the assessment
words, the OT became reachable remotely to its authorized as possible. She may use the access she gains to find hosts with extended
requires an important preparatory phase. Sensitive
users, but also to illegitimate actors. network permissions that are used as "pivot" to access additional
components may be excluded from the tests to minimize the
components.
risks on availability and integrity while preserving the safety.
From safety to security
While industries have long been concerned about safety, How are
cybersecurity was not a priority until a few years ago. Some
thought that OT was not a relevant target, while others believed
penetration tests
that the cybersecurity controls that are commonly endorsed on
IT wouldn't cope with the technical and operational differences Once accessed, the auditor evaluates the attack surface of the components. Assessing the cybersecurity
on industrial
of OT systems. Consequently, the level of awareness and the of servers and workstations follows a similar process as on IT (namely, abusing Linux, Windows, and Active
technical measures available to enforce them is often far behind Directory weaknesses) . This is different for the other industrial components. Here, the aim is to gain as much
what we can find on information systems, while the means of systems information as possible on it: what type of device it is, what it is used for, what it is interconnected to, which
attackers have evolved. Fortunately, the situation has changed, version is used by each of its modules, what network services are enabled, what functions are available,
and OT cybersecurity has emerged, with measures either conducted? and how they are configured. As mentioned before, this is usually sufficient to show how damaging an
specific to OT, or borrowed from the IT and adapted to the attack could be. Indeed, many of them have not been designed or configured with cybersecurity concerns.
industrial world. Penetration testing is one of these measures. For instance, a lot of industrial network protocols are neither encrypted nor authenticated: sending the
appropriate network request may change a device's behavior. Also, it is common to find devices with unused
Assume it's insecure until it's tested services enabled, default credentials, or available security features disabled.
Finally, it is likely that some components are exposed to public vulnerabilities, as updating and applying
A penetration test is used to simulate malicious operations
security patches on industrial systems is difficult considering operational and availability constraints.
performed by a malware or an attacker, and this type of test is
Malware such as Pipedream[85] embed exploitation codes for several vulnerabilities targeting specific
quite common in organizations' internal networks (IT). During
versions of PLCs. The auditor does not exploit these flaws in production, but may ask for a test environment,
such assessments, security auditors explore the system,
if available, to provide proof of concept.
trying to find exploitable flaws that could be combined into The most common entry point to the OT is
realistic attack scenarios. The aim is to provide a prioritized through the IT, connected to the Internet.
mitigation plan for these vulnerabilities, based on real-world Several industrial malware such as the ones
attack techniques. It can also be used to raise awareness on from the BlackEnergy family were introduced
cybersecurity risks. using phishing and spread until they reached
the OT[84]. Therefore, most penetration testing Test successful!
Needless to say, unlike real attacks, the auditors will adapt their
processes start from the IT. The auditor tries
testing process to make sure that they don't disrupt the system.
to find a way to the OT, most likely by making
The last step is the reporting phase: all the findings are combined to
When applied to OT, this is probably the most important part
use of network segmentation issues such
build the attack scenarios, along with the remediation plan that will help
of the tests. Indeed, many OT components are not designed to
as authorized network flows or dual-homed
prevent them.
be exposed and may not handle invalid or superfluous network
stations between the two environments.
traffic and operations. Above all, involuntary disruptions may
Another scenario consists of simulating an Although every plan is unique to its context, the first improvement we
have disastrous consequences.
attack introduced directly in the OT, using a usually recommend is network segmentation between the IT and OT as
compromised device (maintenance station, well as between trust zones within the OT. As long as they are not secure,
USB drive, etc.), or via a device exposed on and even then, the best we can do is to ensure that no attacks reach
the Internet. industrial systems.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

106 Security Navigator 2024 Making Sense of Operational Technology Attacks 107
Dr. Ric Derbyshire
Senior Security Researcher
Orange Cyberdefense
Making Sense of Operational
Technology Attacks:
The Past,
Present
and Future
When you read reports about cyberattacks affecting operational
technology (OT), it’s easy to get caught up in the hype and assume
every single one is sophisticated. But are OT environments all
over the world really besieged by a constant barrage of complex
cyberattacks? Answering that would require breaking down the
different types of OT cyberattacks and then looking back on all the
historical attacks to see how those types compare. That’s exactly
what we’ve done for this chapter.
Over the next few pages, we want to demystify what is going on
with OT cyber security and what attacks we are facing. To do
this, we define 5 types of cyberattacks that can affect OT, which
are split between 2 categories. We then analyse 35 years of OT
cyberattacks and get further context by seeing how they stand up
when compared to our proposed types and categories. This leads
us to some findings that spark questions about the future of OT
cyberattacks and whether we’ll see a shift in type or category in the
medium to long term. We then conclude with an example of how we
think OT cyberattacks may evolve in the future.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

The types of OT cyberattacks How we’re defining OT However, level 2 is typically specific to a single cell or process Type 1c: OT targeted
and perhaps even physically close, whereas level 3 is
Before we define any types of OT cyberattack, we need to The third type in this category, 1c, is the most nuanced and the
Over the past few decades, there has been a growing generally centralized, particularly in geographically dispersed
define what we’re considering as OT. Most OT environments closest in nature to the next category. Here an adversary with
awareness of the need for improved cyber security practices organizations. Level 1 is the heart of OT, where devices such as
are unique due to several factors, such as the different little to no OT capability may deliberately target the Windows-
in IT's lesser-known counterpart, OT. This significantly programmable logic controllers (PLCs) will sense and actuate
applications and use cases, the numerous vendor ecosystems, based OT assets of an organization with IT TTPs. This may
accelerated at the turn of the 2010s with the discovery of the physical world according to the logic they have been
and the simple fact that there are multiple ways to engineer a be to trigger more of a response from the victim or to cause a
perhaps one of the world’s most advanced offensive cyber provided. Finally, we reach level 0, which for all intents and
physical process, to name a few. Because of this, it helps to more serious impact than from just affecting IT. This attack type
capabilities, in the form of malware embedded within the OT purposes is the physical world and contains the sensors and
turn to the Purdue Enterprise Reference Architecture (PERA), may deliberately target OT assets, but only those with which
of Iranian nuclear centrifuges. We are, of course, shamelessly actuators that the PLCs use to manipulate it.
commonly known as the Purdue Model, depicted below. an IT-focused adversary would be familiar. There is otherwise
starting a chapter about OT with a reference to no other
The different types of OT cyberattack aren’t necessarily no OT-specific intent or utilisation in such an attack, nor is
than the infamous Stuxnet. There is a good reason Stuxnet The Purdue Model describes the conceptual structure
defined by the assets that they impact, rather the assets that there any precision in the way production is impacted. As with
references are so commonplace, its discovery and ensuing and separation of various processes and networks in an
they target and how they are targeted. More specifically, the type 1b, the impact of this type of attack may include loss of
awareness has almost singlehandedly brought to fruition the organization that utilizes OT. It is important to note that the
precision, skillset, and intent with which they are targeted. configurability or control of the OT environment, and production
OT cyber security industry as we know it today. What made Purdue Model is only a reference architecture, meaning it is a
While that distinction may sound pedantic, it changes the is only likely to be affected by cascading effects or response
Stuxnet such a watershed moment in OT cyber security is the basic approximation and not something that should directly
threat landscape that defenders need to consider and makes and recovery efforts.
complexity and precision with which it targeted OT-specific define an implementation. However, we can use this model to
it challenging for traditional IT controls to keep up. There are 5
hardware and software. No known attacks before or after describe OT and its constituent devices, as well as provide a
types of OT cyberattack that can be grouped into two distinct
Stuxnet have achieved quite the same level of sophistication, reference point for the types of attack OT may experience. So,
categories, let’s explore them.
particularly in their specific targeting of OT. In fact, the lines this is an application where it is particularly useful. Category 2: OT TTPs
of what constitutes a cyberattack on OT have never been well
defined, and if anything, they have further blurred over time. From the top, it begins by outlining levels 4 and 5 as the Category 1: IT TTPs The second category includes the two types that likely spring
to mind whenever OT cyberattacks are mentioned. These are
Therefore, we’d like to begin this report with a discussion Enterprise Zone, where traditional IT is encountered. Next The first category of cyberattacks endured by OT is the most
characterized by the inclusion of OT-specific TTPs and have the
around the ways in which cyberattacks can either target or just is level 3.5, the Demilitarized Zone (DMZ), which acts as a frequent in public reports, such as Dragos[86] and Waterfall[87].
primary intention of directly affecting production in some way.
simply impact OT, and why it might be important for us to make separator between IT and OT and therefore the OT’s perimeter. They are characterized by the use of only IT tactics, techniques,
the distinction going forward. The remaining levels below the DMZ are all OT. Levels 2 and and procedures (TTPs) but still manage to affect production Type 2a: OT targeted, crude
3 are similar in that they both may monitor, control, and even in some way. There are 3 types of OT cyberattack in this first
configure the physical environment. category. The overall fourth type and first of the second category, 2a,
is sometimes known as the nuisance attack. This type of
Type 1a: IT targeted cyberattack is predicated on the adversary reaching the OT,
regardless of DMZ. It leverages rudimentary OT-specific
The first type, 1a, occurs when the OT environment isn’t
knowledge and TTPs, but in a blunt fashion with little precision
even reached by an adversary. So, as far as the adversary
or complexity. Rather than just disrupting Windows-based
is concerned, their attack does not target the victim’s OT.
assets such as in category 1 attacks, it may target OT assets
Instead, there are cascading impacts from an uncontained IT
in deeper levels of the Purdue Model, closer to the physical
cyberattack, such as Cyber Extortion (Cy-X) delaying shipping
process, such as PLCs and remote telemetry units (RTUs). The
systems that requires production to stop. Alternatively, the OT
OT-specific techniques leveraged are crude and frequently use
is disconnected or shut down by the victim as a precaution.
publicly known exploitation frameworks and tooling. The impact
Meaning in this type of attack, the OT may only be affected
from this type of OT cyberattack generally will involve stopping
indirectly as the victim attempts to maintain safety and integrity
PLCs cycling or imprecisely changing PLC outputs. This will
Level 5 Enterprise Network of the OT network. The OT impacts of this can range from a
undoubtedly affect production, but such blunt attacks are often
temporary loss of telemetry all the way to complete loss of
overt and trigger a swift response and recovery effort.
production and a complex, time consuming process to bring
Level 4 Business Planning/Logistic Network it back online. It is important to note that every OT cyberattack Type 2b: OT targeted, sophisticated
Enterprise type may also result in a disconnect or shutdown of the OT
environment as part of the response and recovery efforts, The final type, 2b, is the most advanced but also most rarely
which would ultimately cause similar affects. observed. By exercising advanced OT capability, these
cyberattacks are precise and complex in both their execution
Level 3.5 Demilitarized Zone (Historian, Jump Box, Patch/AV Server) Type 1b: IT/OT targeted and impact. They involve extensive process comprehension,
an OT-specific tactic of gathering information to understand
The second type, 1b, is when the OT is reached by an
the physical environment and how the OT interacts with it.
adversary either by accident or just because they could. Still
Adversaries will combine their advanced OT capability with
conducting IT TTPs, the adversary may deploy ransomware
process comprehension to craft an attack that is bespoke for
Operational or exfiltrate data for double extortion. However, perhaps
Level 3 Operations & Control (HMI, Engineering Workstation, Historian) the OT environment they have gained a foothold in and affect it
Technology due to a weak or non-existent DMZ, the adversary’s attack
in a very deliberate way. The possible impacts caused by this
may extend to some OT assets in levels 2 or 3 of the Purdue
type of OT cyberattack are near limitless but depend highly
Model. The affected OT assets may include devices such as
on the process under consideration. It is unlikely the impacts
Level 2 Supervisory Control (HMI, Engineering Workstation) engineering workstations, Windows-based human machine
would be overt or simple, such as stopping the process, unless
interfaces (HMIs), and other IT-based technology. Although
it was in an extreme and permanent way. Instead, the intended
the adversary has managed to directly affect OT assets, the
impacts are more likely to involve, for example, stealthily
Level 1 Basic Control (PLC) targeting is generally not deliberate. The impact of this attack
degrading the process or exfiltrating details of it to replicate it
type may include loss of configurability or even control of the
elsewhere.
OT environment, but it is unlikely to affect production on its own
Cell/Area Zone
unless there are cascading effects or until the victim begins
Level 0 Process (Sensor, Actuator)
response and recovery.
ZMD
108 Security Navigator 2024 Making Sense of Operational Technology Attacks 109
The Purdue Enterprise Reference Architecture
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

110 Security Navigator 2024 Making Sense of Operational Technology Attacks 111
Victims by sectors
Proportion of victims of OT attacks by industry sector
Why is this important? 35 years of OT cyberattacks
OT cyberattacks are frequently sensationalized in the news, Thanks to Miller et al. for providing the data behind their 17%
and it is important to know when the hype is real. When paper[90] that gave us a great head start in this section, as well 4% Manufacturing
distinguished by the two categories and further broken down as to Nicolas Pairoux and Carl Morris for their help in gathering 14% Transportation and Warehousing
into the five types between them, it becomes clear that not the remaining data.
Utilities
all OT cyberattacks are equal, and many are not worthy of
The types of OT cyberattack that we’ve defined and the
the hype. In fact, you might find that under this lens many Mining, Quarrying, and Oil
reasons for why they are important all rely on some bold
cyberattacks reported to have been against OT are relatively and Gas Extraction
claims. So, rather than expect you to take our word for it, we
unremarkable IT cyberattacks that lie in category 1. In fact, 2%
thought we’d put them to the test. To do this we’ve collected 11% Health Care and Social Assistance
the trend of category 1 attacks affecting OT appears to be
and analyzed every publicly reported OT cyberattack we could Information
growing with the ever-increasing interconnectivity between IT
find, from 1988 to 2023. Before we get into that analysis, let’s 2%
and OT. This is due to concepts such as the Industrial Internet Accommodation and Food Services
briefly talk about our data collection method for transparency.
of Things[88] and Industry 4.0[89] demanding more telemetry and Multiple
control, in turn increasing the size and complexity of the OT 1%
Wholesale Trade
perimeter and resulting attack surface. Method 1%
In the short term, the skew towards category 1 might be saving As is clear from our types of OT cyberattack, defining them 58% 1%
us from the much-vaunted OT apocalypse. Many current OT in the first place can be quite difficult. However, our primary
cyber security controls are borrowed from IT, and as such, criterion was that each incident must have affected OT, at
they are better at detecting and preventing category 1 attacks. minimum a type 1a scenario. If an organization uses OT but
However, as access to knowledge and equipment grows and only their IT was affected by a cyberattack, meaning their Analysis Warehousing was the second most frequently attacked sector
as adversaries develop OT modus operandi that are relevant production was not affected, we did not consider it to be an OT at 17% (21), followed by Utilities at 14% (17).
to their respective causes, there’s a real possibility that we’ll cyberattack. Despite being a relatively small data set for a Security Navigator
see a growing number of category 2 attacks. While we cannot article, there’s a surprising amount to unpack and discuss,
ignore the upstream category 1 attacks, we must consider the To further ensure that we had the richest data to work with, an particularly because OT cyberattacks have changed over 35 Country perspective
truly unique OT threats on the horizon and begin to develop incident was only recorded if we could find at least 4 of the 5 years. This means that we can pick out some other interesting
the relevant OT cyber security controls to detect and prevent following criteria: points from this data. The geographic distribution of the victims was quite broad
them. An early step in doing this, therefore, is distinguishing the and not entirely what we had expected. It wasn’t particularly
categories and types of attack to better understand how and 1. Year of incident surprising that the USA saw the most victims with 23% (27) of
when those category 2 attacks are on the rise. Overall demographics of OT incidents, this is consistent with other datasets. However, we
2. Country of incident
did see Russia as the 5th most targeted country with 4% (5) of
cyberattack victims and their
incidents, which is different from what we see in other datasets
3. Victim sector
adversaries – especially Cy-X. Although, this disparity is easily understood
given the unique shape of Cy-X victimology. Russia’s
4. Adversary type
To categorize our victims by sector we referred to the North prominence is due to 4 hacktivists attacks shortly after their
American Industry Classification System (NAICS). What we invasion of Ukraine in 2022. Germany saw 12% (14) of attacks,
5. Initial access vector
found was that, over the 35 years, Manufacturing was the which is an uncharacteristic prominence in comparison to
Collecting these minimum criteria did two things. First, it most frequently attacked sector and made up 58% (69) of other datasets. 11% (13) of attacks impacted victims in multiple
meant that each incident we recorded strongly contributed to all incidents. This is similar to our other datasets, such as countries and were therefore recorded as ‘multiple’.
our overall data. Second, it meant that the data sources were Cy-X, it’s just a little more exaggerated because there are a
usually verbose enough for us to confidently speculate on the limited number of sectors that use OT. Transportation and
category and type of the attack, as well as the depth of the
Purdue Model the adversary was able to target (not impact). If
we weren’t confident on that second point, the incident would
Count
also be discarded as this was crucial to our analysis.
What this means is that we were left with 119 recorded 27
incidents over 35 years. We’ll be the first to admit that it doesn’t
contain every OT cyberattack within that timeframe: it only
contains incidents that were publicly reported, it only contains
incidents that we could find, and it only contains incidents that
were well reported enough for us to find all the data required.
However, we do think that it provides us with a good insight into 1
how OT cyberattacks have progressed over time and lets us
put our categories and types to the test.
With all that said, let’s check out the data.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

When it comes to the types of adversaries conducting Adversaries The rise of double extortion didn’t just change the overall types of adversaries attacking OT, it also changed the
these OT cyberattacks, any nuance of individual groups overall victim sectors affected. When we break down the victim sectors by year, we also see a significant shift from
or organizations was lost due to the long time over which Proportion of different threat actors a diverse range of sectors to being heavily manufacturing focused. However, given that Cy-X tends to favor targeting
they occurred. Therefore, we decided to group them into manufacturing, this makes sense.
generalized categories for simplicity.
Shift in victim count per year
We found that criminals were the most frequent offender, 2%2%
6%
perpetrating 61% (73) of our recorded OT cyberattacks.
Victims in different sectors over time
These were all Cy-X incidents, most involving ransomware.
8%
This may come as a surprise to those who were under 40
the impression OT cyberattacks were all sophisticated
government attacks against critical national infrastructure. 35
However, nation-states were only the second most frequent 8%
offender, who conducted 13% (16) of OT cyberattacks.
30
These mostly consisted of the commonly discussed
attacks that typically spring to mind when one thinks of a
sophisticated OT cyberattack (…Stuxnet). 25
61%
13%
20 Everything changed in 2020
For those who have been paying close attention to recent 15
OT cyberattacks, the criminal adversary dominance
probably didn’t come as much of a surprise. However, those 10
who did not expect it can be forgiven for two reasons. First,
you’ve probably been bombarded by doomsaying marketing
Criminal Hacktivist 5
implying that critical national infrastructure the world over is Actor types over time
State Unknown on the brink of cyber apocalypse from hyper sophisticated
Unspecified Hacker Third party contractor 0
nation-state cyberattacks (we hope, if anything, this report Adversary count per year
provides you a more pragmatic outlook). Second, and most Insider
importantly, it hasn’t always been this way – at least not so 2023
publicly. 2022
2021
In 2020 we saw the advent of double extortion. Rather than
2020
stopping at using ransomware to encrypt everything they
2019 could on a victim’s estate, criminals began to exfiltrate
sensitive data too. Then regardless of whether the victim 2018
had paid their ransomware ransom, they’d be threatened 2017
with that exfiltrated data being leaked if a further ransom 2016
was not paid. What’s more, these threats would be made 2015
publicly. 2014
2013 With the rise of double extortion, we have seen a rise in
2012
cyberattacks impacting OT. This could be because there
are more attacks, or it could be because they’re now 2011
much more public with the second phase of extortion. It’s 2010
probably because of both, as well as a whole host of other 2009
small reasons all amalgamated together. Whatever the 2008
reason, a very distinct change happens around 2020 in our 2007
data. 2005
2004 Given that this is an issue caused by criminals, we’ll start
with adversary types. Once we look at what adversary types 2003
we witnessed by year, we begin to see the extent of the 2002
modern OT cyber security issue and the reason criminals 2001
dominate our data. Prior to 2020 there was a varied 2000
ecosystem of adversaries attacking OT, and notably fewer 1999
overall. We still find that variety in a post-double extortion 1997
world, it’s just drowned out by the overwhelming number of 1996
criminal attacks. 1994
1992
1988
0 5 10 15 20 25 30 35
Criminal Hacktivist
State Unknown
Unspecified Hacker Third party contractor
Insider
8891 2991 4991 6991 7991 9991 0002 1002 2002 3002 4002 5002 7002 8002 9002 0102 1102 2102 3102 4102 5102 6102 7102 8102 9102 0202 1202 2202 3202
112 Security Navigator 2024 Making Sense of Operational Technology Attacks 113
Wholesale Trade
Utilities
Transportation
and Warehousing
Multiple
Mining, Quarrying, and
Oil and Gas Extraction
Manufacturing
Information
Health Care and
Social Assistance
Types of OT cyberattacks in action
Before we look at how our data looks through the lens of our categories and types of OT cyberattack, let’s have a
very quick refresher about what they are.
Category 1 attacks are those which are for all intents and purposes IT attacks, due to the fact they do not utilize any
OT-specific knowledge or TTPs. However, whether through collateral damage, circumstance, or opportunity, these
attacks still manage to affect production, and therefore the OT. Category 2 attacks include the use of OT-specific
knowledge and TTPs. These may either be crude attacks that clumsily use exploitation frameworks and tooling, or
they may be sophisticated attacks that utilize process comprehension to expertly affect the OT and its processes.
1 2
Category IT TTPs OT TTPs
1a 1b 1c 2a 2b
Type
OT targeted, IT targeted IT/OT targeted OT targeted OT targeted, crude
sophisticated
IT attacked, Dedicated OT
IT attacked, Dedicated OT
Windows/Linux- Windows/Linux- devices attacked
production devices attacked
based OT attacked based OT attacked with OT-specific
Characteristics impacted indirectly with OT-specific
with IT TTPs with IT TTPs TTPs crudely,
as collateral TTPs with
directly or as directly little precision or damage sophistication
collateral complexity
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

114 Security Navigator 2024 Making Sense of Operational Technology Attacks 115
| Flow: Attack operations  |     |     |     |     |     |     | TTPs used over time |     |     |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
From year to adversary to category to type to Purdue depth    Comparison of categories 1 (IT TTPs) and 2 (OT TTPs) over time  1: IT TTPs 2: OT TTPs
35
30
Level 5: Enterprise Network
|     | Criminal |     |     |     | 1a: IT targeted |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2020
25
1: IT TTPs
|     |     |     |     |     | Level 4: Business Planning/Logistic Network |     | 20  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Third party contractor
1b: IT/OT targeted
| 2015 | Unspecified Hacker |     |     |     |                 |     | 15  |     |     |     |     |     |     |     |     |     |
| ---- | ------------------ | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2010 |                    |     |     |     | 1c: OT targeted |     |     |     |     |     |     |     |     |     |     |     |
State
|     |     |     |     |     |     | Level 3: Operations & Control | 10  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2005
| 2000 | Hacktivist |     |     |                        |     |                              |     |     |     |     |     |     |     |     |     |     |
| ---- | ---------- | --- | --- | ---------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1995 |            |     |     | 2a: OT targeted, crude |     | Level 2: Supervisory Control | 5   |     |     |     |     |     |     |     |     |     |
Insider
| 1990 |         |     | 2: OT TTPs |                                |     |                        |     |     |     |     |     |     |     |     |     |     |
| ---- | ------- | --- | ---------- | ------------------------------ | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1985 | Unknown |     |            | 2b: OT targeted, sophisticated |     | Level 1: Basic Control |     |     |     |     |     |     |     |     |     |     |
0
|                                                                   |     |     |                                                                 |     |     |     | 8891 2991                                                    | 4991 6991 7991 | 9991 0002 1002 | 2002 3002 4002 | 5002 7002 8002 | 9002 0102 1102                                                      | 2102 3102 4102 | 5102 6102 7102 | 8102 9102 0202 | 1202 2202 3202 |
| ----------------------------------------------------------------- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | ------------------------------------------------------------ | -------------- | -------------- | -------------- | -------------- | ------------------------------------------------------------------- | -------------- | -------------- | -------------- | -------------- |
| The above flow chart shows us flows of OT cyberattacks. The       |     |     | The immediate takeaway from this visualisation is the drastic   |     |     |     |                                                              |                |                |                |                |                                                                     |                |                |                |                |
| year of an attack, grouped into 5-year bins for clarity, flows    |     |     | increase in attack frequency in 2020, which overwhelmingly      |     |     |     |                                                              |                |                |                |                |                                                                     |                |                |                |                |
| from the left into the adversary that conducted the attack. The   |     |     | saw criminals committing IT TTPs against IT targets, resolving  |     |     |     |                                                              |                |                |                |                |                                                                     |                |                |                |                |
| attack flow continues from the adversary to the category of       |     |     | at levels 4 and 5 of the Purdue Model. Moreover, every          |     |     |     |                                                              |                |                |                |                |                                                                     |                |                |                |                |
|                                                                   |     |     |                                                                 |     |     |     | Delving into a deeper analysis of the categories and types,  |                |                |                |                | Breaking down the categories and types by year presents us          |                |                |                |                |
| OT cyberattack, through to the type. Finally, the type of attack  |     |     | flow prior to 2020 has a much more varied ecosystem of          |     |     |     |                                                              |                |                |                |                |                                                                     |                |                |                |                |
|                                                                   |     |     |                                                                 |     |     |     | it becomes clear that a significantly larger number of       |                |                |                |                | with a familiar story. Prior to the 2020 rise of double extortion,  |                |                |                |                |
flows into a representation of the deepest level of the Purdue  adversaries. While not a novel discovery, it reinforces the two  cyberattacks that cause OT impact are category 1 and use only  the attacks were an approximately even split of categories
Model the attack reached in terms of targeting (it may have  narratives we described occurring before and after the advent  IT TTPs at 83% (99) of the total. This is bolstered by the large  and types, but Cy-X has taken over. Since 2020, type 1a OT
impacted the OT completely even from Level 5). of double extortion in 2020. representation of type 1a attacks at 60% (71) of the total, which  cyberattacks (and therefore category 1) have erupted, which is
|     |     |     |     |     |     |     | specifically target the IT, meaning levels 4 and 5 of the Purdue  |     |     |     |     | to be expected as that is the type most likely to be associated  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | --- |
|     |     |     |     |     |     |     | Model. By comparison, attacks that included the use of OT         |     |     |     |     | with Cy-X attacks focusing on IT TTPs and targets.               |     |     |     |     |
Distribution of categories and types  TTPs were poorly represented at 17% (20) of the total.
Overall count of OT attack categories and types
All incident classifications over time
ta2
c rg a
8 r u : O
|     |     |   % | d e te |     |     |     | All type categories year by year  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | ------ | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2   e T 1a: IT targeted 1b: IT/OT targeted 1c: OT targeted 2a: OT targeted, crude 2b: OT targeted, sophisticated
|     |     | t a b | d   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
s o r g :  O
|     |     | p e T |     |     |     |     | 40  |     |     |     |     |     |     |     |     |     |
| --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
c a h i t e
|     |     | 9 t e s t d | 2   |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | % d i -     | :   |     |     |     |     |     |     |     |     |     |     |     |     |     |
O
|     |     | 1T  |     |     |     |     | 35  |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
7 T
|     |     |   %T     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     | 1 c :  O | P   |     |     |     |     |     |     |     |     |     |     |     |     |     |
|     |     | ta r g T | s   |     |     |     | 30  |     |     |     |     |     |     |     |     |     |
e t e
5 % d
25
20

1 a :  I
|     |     | /O T      |     |      | t ar T    |     | 15  |     |     |     |     |     |     |     |     |     |
| --- | --- | --------- | --- | ---- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |  :  I T d |     |      | g e t e d |     |     |     |     |     |     |     |     |     |     |     |
|     |     | 1 b e te  |     | 1    | 6 0 %     |     |     |     |     |     |     |     |     |     |     |     |
|     |     | t a r g % |     | : IT |           |     |     |     |     |     |     |     |     |     |     |     |
|     |     | 1 8       |     | 8    |           |     | 10  |     |     |     |     |     |     |     |     |     |
3  T
% T
P s
5
0
|                                 |     |     |     |     |     |     | 8891 2991 | 4991 6991 7991 | 9991 0002 1002 | 2002 3002 4002 | 5002 7002 8002 | 9002 0102 1102 | 2102 3102 4102 | 5102 6102 7102             | 8102 9102 0202 | 1202 2202 3202 |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------- | -------------------------- | -------------- | -------------- |
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |           |                |                |                |                |                |                | www.orangecyberdefense.com |                |                |

116 Security Navigator 2024 Making Sense of Operational Technology Attacks 117
Categories to types of ATT&CK impacts
T0828: Loss of Productivity and Revenue
1a: IT targeted
1: IT TTPs
T1486: Data Encrypted for Impact
1b: IT/OT targeted
Will criminals turn to OT TTPs?
1c: OT targeted T0829: Loss of View
T1499: Endpoint Denial of Service
T0826: Loss of Availability
Regardless of organizations that use OT, the current type 1a there is a growing base of OT cyber security knowledge in the
T0827: Loss of Control
Cy-X attacks appear to be relatively lucrative for criminals, and form of courses, books, talks, and even dedicated conferences
2a: OT targeted, crude T0882: Theft of Operational Information
the veritable pandemic may get worse before it gets better. from which they could learn. Moreover, OT devices such as
T1485: Data Destruction
2: OT TTPs However, all good (for them) things must come to an end at PLCs and HMIs are becoming less prohibitively expensive for
2b: OT targeted, sophisticated T1561: Disk Wipe some point. If organizations begin to build up a resilience to learning and eventual attack testing. All of this culminates in
contemporary Cy-X attacks, whether that is through good lowering barriers to entry from a technical perspective.
T0832: Manipulation of View
Impacts unique to T0813: Denial of Control backup processes or otherwise, it is logical that criminal modus The most fundamental point of this component is the suitability
category 2: OT TTPs operandi (MO) will change. Given the prevalence of OT-using
T0831: Manipulation of Control of the victim organisation itself. This suitability includes a large
organizations as Cy-X victims, could we see that change in
T0837: Loss of Protection attack surface, available time for the adversary to conduct the
MO be towards category 2 OT cyberattacks? Fortunately, to
T0879: Damage to Property attack, and the value specific assets may have to the victim. As
facilitate a discussion around that question, we can turn to
T0880: Loss of Safety we can see in historical Cy-X attacks, adversaries are already
routine activity theory (RAT)[91].
finding plenty of vulnerabilities to exploit in their victims and
Whenever an OT cyberattack report’s source described a specific impact, it was aligned to the MITRE ATT&CK® RAT is a criminological theory that states a crime will be likely clearly do not often encounter what would be described as best
and MITRE ATT&CK® for industrial control systems (ICS). T0828: Loss of Productivity and Revenue was a to take place given three elements are present: a motivated practice cyber security. Moreover, the uptime and efficiency of
prominent impact when production was affected and T1486: Data Encrypted for Impact was seen frequently due to offender, a suitable target, and the absence of a suitable an OT environment is often well quantified, meaning the value
2020’s rise in Cy-X. However, one interesting point is the cluster of towards the bottom right of the visualisation that guardian. Here we’ll provide a brief discussion on each point of OT impact is likely not as nebulous as encrypted or leaked
only occurred as a result of category 2 OT cyberattacks. Of these category 2-specific impacts, T0831: Manipulation based on what we have seen so far. data. This all presents a clearly suitable target in OT-using
of Control was seen most frequently. organizations.
Motivated offender
Absence of a suitable guardian
As can be seen from the OT cyberattack data we have
presented here and the wider Cy-X data in this report, for If criminals consider moving away from conducting category
whatever reason, criminals currently have a penchant for 1 Cy-X with IT TTPs, it will primarily be in response to effective
organizations that happen to use OT. What’s more, the way guardianship from IT cyber security controls. Therefore, they
current Cy-X attacks heedlessly affect their victims’ OT may move to exploit the challenge encountered in defending
environments makes it clear that criminals are not concerned against OT TTPs caused by a lack of available controls that are
about physical consequences. Either that or they are possibly specifically made for OT.
even intentionally causing threats to safety. Lastly, if we see
ransom payments for IT-focused Cy-X decline, that will likely Technical security controls are not the only form of
What does this all mean?
pressure criminals into changing their MO to something for suitable guardian, of course. RAT considers other forms
which their victims are less defensively prepared. of guardianship, such as informal (community) and formal
This analysis has explored the history of OT cyberattacks to understand the changing landscape and what we may
guardianship. The latter, formal guardianship, implies efforts
face in the imminent future. The most notable takeaway is that the landscape is shifting heavily towards type 1a OT Suitable target
made by law enforcement and governments, and it’s something
cyberattacks, those which use IT TTPs to target IT and only inadvertently affect OT. This trend provides fortunate
breathing room for OT defenders. With a dearth of OT cyber security controls that are built from the ground up for Criminals may already be specifically targeting organizations we explore the effectiveness of for IT Cy-X in another chapter
an OT environment, defenders are typically left with reappropriated IT cyber security tools. that use OT because they see the effect of impacting of this report. Ultimately, OT will face the same challenges in
production as valuable. If existing methods for doing this, such disrupting the criminal ecosystem and so the absence of a
By breaking down OT cyberattacks into categories and types we can track shifts in whether OT TTPs are included as type 1a Cy-X attacks, decline in reliability, criminals may capable guardian, or its effectiveness to disrupt crime, is a
in attacks, and how sophisticated they are. This allows us to understand what impacts adversaries are intending seek to target the OT directly instead. In our data, 40% (48) realistic outlook.
to achieve, which in turn allows us to better plan our defences and understand the areas of improvement for OT- of all OT cyberattacks and 16% (12 of 73) of those conducted
What this means
specific cyber security controls as they are developed. by criminals managed to reach the operational technology to
affect it. These were type 1b, 1c, 2a, or 2b OT cyberattacks. It wouldn’t be prudent to outright declare that criminals are
Conversely, the recent data from 2020 onwards, when split into its categories and types, shows that we shouldn’t going to begin attacking OT with novel Cy-X techniques in
Adversaries, and to a lesser extent criminals, are already
believe the hype of OT cyberattacks. Instead, we should be focusing on tackling the Cy-X issue in the short term. response to less reliable ransom payments. However, it also
accessing OT environments. Should they require access to
This means building operational resilience and confidence into our OT to withstand attacks on Levels 4 and 5 of the wouldn’t be prudent to say this is never going to happen,
deliberately target the OT, it isn’t inconceivable that criminals
Purdue Model. We are, however, aware that is easier said than done. either. At the risk of sitting on the fence, we’ll say that there is a
would be able to achieve it.
genuine possibility that we may see Cy-X evolve to target OT-
So, where do we go from here? What will the future hold? Are all OT cyberattacks just IT TTPs on IT targets and One important point regarding whether OT is a suitable target specific assets, it may just take a particularly innovative Cy-X
circumstantial OT impact? Or might we see the relentless onslaught from criminals turn towards category 2 attacks is its unfamiliar context to most criminals. However,while they group.
for greater brutality? would need to develop technical capability, has context menu,
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

Dead Man’s PLC Dead Man’s PLC takes advantage of this capability, as well as
existing OT functionality and seldom-used security controls, to
While we’ve been considering whether there may be a shift hold the victim’s entire operational process and, by proxy, the
to criminals targeting OT with category 2 cyberattacks, we’ve physical world to ransom.
been working on some interesting, speculative research.
Dead Man’s PLC works by adding to the legitimate, operational
It has culminated in a novel and pragmatic Cy-X technique
PLC code to create a covert monitoring network, whereby
specifically targeted against OT devices; in particular, PLCs and
all the PLCs remain functional but are constantly polling one
their accompanying engineering workstations. We call it Dead
another. If the polling network detects any attempt from the
Man’s PLC.
victim to respond to the attack, or the victim does not pay their
As we can see from the 35 years of historical attacks, there ransom in time, polling will cease, and Dead Man’s PLC will
hasn’t been a publicly reported Cy-X attack that deliberately trigger akin to a Dead Man’s switch and detonate. Detonation
targeted PLCs. That might be because traditional, encryption- involves deactivating the legitimate PLC code, responsible for
based ransomware isn’t quite effective (or perhaps even the control and automation of the operational process, and
achievable) against them. Firstly, the criminal would require activation of malicious code that causes physical damage to
specific vendor/device exploits to attain root level access on operational devices. This leaves the victim with no realistic
each device they want to target, which means attacks across option but to pay their ransom; their only other alternative
multiple organizations that utilize different vendor ecosystems recovery method is to gracelessly shut down and replace every
are hard to scale. Secondly, typical engineering response and affected PLC in their operational process, which will cost them
recovery practices involve replacing faulty devices with new in lost production time, damaged goods, and the cost of new
ones and flashing the configuration back to them, which would materials.
render encrypting individual devices ineffective. However, you
It has generally been believed that OT-specific Cy-X presents
don’t need to rely on IT TTPs or encrypt PLCs to perform Cy-X
an unlikely risk, due to the requirements placed on criminals
against OT, because in OT we have something that can be
from a technical perspective. The inability to easily recycle an
targeted that isn’t possible in IT Cy-X attacks – the physical
attack across multiple environments also acted as a deterrent,
world.
due to the time and effort required to attack each victim.
Dead Man’s PLC starts at the engineering workstation, the However, we think that Dead Man’s PLC is an effective and
asset where engineers will create configurations and load pragmatic technique for holding the entire operational process
them onto PLCs across the OT environment. Nozomi recently to ransom. Most importantly, Dead Man’s PLC acts as a
reported that 34.7% of attacks in OT environments are starting point for defenders to rethink the risk ransomware and
facilitated by engineering workstations[92]. Moreover, we’ve Cy-X could pose to OT, beyond the current surge of IT TTPs
seen in this report that there is no shortage of OT cyberattacks and type 1a Cy-X we see today.
reaching the depths of the Purdue Model where engineering
If you’d like to read more about Dead Man’s PLC and how it
workstations may reside – generally levels 2 or 3 depending on
works, its dedicated research paper[93].
numerous factors.
When the criminal is on the engineering workstation, they can
view existing ‘live’ PLC code in their project files, edit them, and
download new configurations to the PLCs.
PLC 2
alert
poll
Engineering
workstation
PLC 1 PLC 3
llop trela
llop trela
118 Security Navigator 2024 Making Sense of Operational Technology Attacks 119
The Dead Man's PLC process
alert
poll
alert
poll
alert
poll
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

120 Security Navigator 2024 Pentesting and CSIRT stories 121
Dominic White
Managing Director South Africa
Ethical Hacking Director
Orange Cyberdefense
Pentesting and CSIRT stories
Hack the Planet!
We love bringing you tales of fresh hacks in each Security Navigator,
and while we’ve got a new batch of interesting and unexpected
stories for you, I wanted to take a moment to talk about why we
do it.
There’s a strange dissonance to being a hacker - spending your
time finding strange and unexpected ways of manipulating systems
interactions and functionality to make them perform unauthorised
computations then making the jarring shift out of the rabbit hole
into an industry that proffers best practices you know would rarely
meaningfully impede your ability to manipulate these systems. This
is why we share these stories, to help you see what we see - how
systems fail when faced with a human adversary. Only by doing
this, will we ever conceptualise a real model for how to build resilient
systems.
There’s another reason too - it’s thrilling. One of the best things
about this work is that the people who do it only develop their
expertise through having spent far too much time sitting in front of
a computer. What drives them is the enduring thrill of the hack. And
while our industry continues to successfully embrace automation,
there remains something truly magical about watching an artisan
engage in this work - and the results are equally so. It’s rare to
be able to harness enjoyment into a public good when so often
it’s hidden from view. We hope you get a sense of what it’s like
crowding around the desk (or chat channels) of our peers as they
plumbed these depths.
I leave you with the enduring words of Dade Murphy:
Hack the Planet!
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

122 Security Navigator 2024 PPeenntteessttiinngg aanndd CCSSIIRRTT ssttoorriieess 123
CSIRT story: A close cut for Conti
As is often the case, the balloon went up late afternoon when a client called us to say they
had noticed some behavioural anomalies on one of their Domain Controllers (Group Policy
Objects had been deleted and the DC had unexpectedly rebooted). Fortunately, the client
exercised an impeccable response procedure by isolating the server and calling the Orange
4
I’m an admin,
Cyberdefense hotline!
let me through!
Gordon Brebner, Senior Incident Response Analyst, Orange Cyberdefense
The attackers enhanced their
persistence and elevated privileges
by creating their own highly privileged
accounts that allowed them to
move freely throughout the network,
deploying Sliver malware C2 payloads 5Restoring security
on various servers, eventually gaining
access to a Domain Administrator the very last minute
account. The attack culminated in the attackers
disabling firewall settings and deleting
Group Policy Objects on a Domain
1 Controller to deploy various malicious
They come out at sun-down
3 How did they get in? tools, including commercial software
By the early hours of the evening, the for remote access, a Sliver malware
CSIRT had deployed XDR to the client’s Having collected and analyzed a beacon for C2 and a Conti ransomware
network and gained real-time visibility plethora of digital forensic artefacts payload. Fortunately, the collective efforts
of the situation. from affected servers and network of the CSIRT and the client thwarted all
devices, the CSIRT discovered the
Quickly the CSIRT found the attackers attempts by the attackers to execute the
attackers (probably linked to the
were still active on several servers, ransomware payload and achieve their
infamous ‘Conti’ Ransomware-as-a-
including their initial foothold (an final objective.
Service group), gained initial access
internet facing webserver) and an
to the client’s network by exploiting
application server communicating to
a known vulnerability on an internet
the internet over a Sliver malware C2
facing webserver to deploy a publicly
channel.
available web shell script.
Lessons learned
An understanding of what abnormal network
behaviour looked like led to the fast isolation of a
server and the seeking of assistance from the Orange
Cyberdefense CSIRT. This is an important lesson and
stands to highlight how good preparation can lead to
fast containment actions – and ultimately limiting the
damage.
The rebuild of critical systems prior to CSIRT
2Working the night shift involvement is a risky move and often impairs an
investigation. Fortunately, in this case the client
CSIRT analysts worked throughout the night to effectively
had backed up copies of the affected systems in a
identify and contain the attackers, utilizing advanced AI tools to
known-compromised state, allowing us to collect the
isolate all compromised servers and to deploy prevention rules
necessary evidence from them.
to stop any further execution of malicious tools.
As dawn broke, the team were confident they had contained Due to the obscurity of the vulnerable webserver
the incident and could switch to a more forensic style of component, in this case it is likely standard
investigation. vulnerability scanners would not have identified the
outdated software. This highlights the importance of
penetration testing, in particular one using a black
box methodology, to show the organization how an
attacker would scope out an attack on the network.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

124 Security Navigator 2024 Pentesting and CSIRT stories 125
CSIRT story:
SEO-optimized compromise
Considering everyone’s favorite search engine is a common thing to do. That applies to 6 Security restored
home use as well as the work place. But attackers know this as well, and leverage this fact to
Shortly after that all
prey on the unwary. This example shows how manipulated search results set in motion
malicious traffic was
a chain of events that ended in a serious incident.
blocked at the perimeter
John Askew, CSIRT Analyst, Orange Cyberdefense firewall, and no further
malicious activity was
identified past this point.
5
Catch them
by the endpoint
Immediate deployment of EDR
monitoring and analysis tools revealed
4
I think I’m Rclone now the attack chain and initial attack
vector.
Within a few days data is removed
1
"Is a handwritten from the servers en masse by the The Cobalt Strike beacons could be
receipt legal?" attackers deploying the commercial extracted and compromised servers
file copying tool Rclone. were identified, isolated and cleaned.
That is a legit question, right? Pursuing
an answer the user asked Google At that point a third party alerted the
and was presented with a couple of customer’s IT that there was potential
answers. C&C traffic from 3 specific servers: 2
domain controllers and a file storage.
Among the top links presented
CSIRT is called in immediately.
happened to be a forum, which helpfully
offered a .zip file for download. Others
had already responded and found it
helpful, so what can go wrong?
3 Lessons learned
Dogs that don’t bark
may bite all the harder
Just 20 minutes after the initial infection ▪ Do not trust random search results. Google
the reconnaissance tool Bloodhound was is among the most powerful search engines
executed by the attackers. of the web, but hackers can and will use
it to spread malware via SEO poisoning
Following that some more tools like
techniques as shown here. Raising awareness
ADTimeline, PowerSploit and Advanced
and training employees to identify such
IP Scanner were installed to sniff out the
attempts is key in turning the human factor in
network and move laterally, identifying
cyber from a weakness into a strength.
critical servers...
2Lucky, lucky, ▪ Be aware of Cobalt Stike. While it is by far
not the only tool attackers use for first level
the answer is in the zip!
compromise, it is among the most commonly
The user downloaded the .zip and seen. About 80% of the C&C traffic that we
opened it. Unfortunately, instead track involves Cobalt Strike.
of the answer to the question it
contained the infamous hacking/ ▪ Endpoint detection and response capabilities
remote administration toolkit Cobalt are essential in identifying and containing
Strike. At this point the attackers incidents rapidly, hence minimizing the
could establish complete control over attacker’s time window for stealing data or
the users laptop. damaging critical systems.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

126 Security Navigator 2024 Pentesting and CSIRT stories 127
Pentesting story: In third parties we trust
This security assessment was focussed on an Android application and an administrative
web portal with the goal to identify security issues. From the administrative web portal, it
was possible to create users and a user would receive a QR code to log in to the Android
application.
Paul van der Haas, Security Specialist, Orange Cyberdefense
6The sum of all
vulnerabilities
Of all the findings, only one was
classified (according to CVSSv3) as
Critical.
Using CVSSv3 alone could give
a false impression of the overall
security as the attack chain
described led to a full compromise of
1
Credible QR
data and applications.
5
QR codes can be static and dynamic. 4 SQL injection, Full remote control admin The sum of a few non-critical
The QR code itself consisted of user The vulnerability gave access to multiple databases vulnerabilities can be as severe as a
anyone?
credentials and connection details containing Personally Identifiable Information single critical one.
and did not change. Dropping modified SQL commands (PII) and a way to escalate privileges to the
This meant that if this QR was is better known as SQL injection administrative web portal. The session tokens
leaked, lost or stolen it could be used and the vulnerability is older than of administrators were extracted leading to a full
multiple times to log in as the user some of our analysts are. The SQLi compromise of the application remotely.
resulting in a higher impact if the QR was quickly identified, but using
code is compromised. specific payloads for full database
compromise required the help of
some experts. Luckily, we have a lot
of knowledgeable colleagues!
Lessons learned:
2 3
Digging into the APK Meet our new app!
Moving to the Android application, which The modified application made it
The Android application was built by a third-party and they
was available for anyone, the first thing we easier to intercept (HTTP) traffic. The
were trusted to have the application developed with security
did was try to decompile the APK. We do analysis done on the decompiled
built in. In these cases, one should:
this to understand the application logic and APK and the intercepted traffic
to identify sensitive data like passwords, API resulted in the identification of both ▪ Include security as part of the requirements and design
keys, API endpoints, etc. an unauthenticated download of
▪ Evaluate third parties regarding their security
sensitive files and a possible way
The application did not have protections methodologies and standards
to inject SQL commands into the
to prevent us from modifying (patching)
the application with our mobile penetration underlying database. ▪ Verify if security is indeed built-in
testing tool Objection. (security assessments)
Mobile applications are not magic. They can most often be
reverse engineered and be tampered with. Make sure the
applications are securely developed and hardened.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

128 Security Navigator 2024 Pentesting and CSIRT stories 129
Pentesting story:
Intercepting Communication in the Flutter Framework
During a recent assessment, the South African ethical hacking team assessed an Android Point- 5I know what's
of-Sale (POS) application for a local bank. Generally, intercepting HTTPS communication from
on your memory!
mobile applications is easily performed. However, the client's application was not cooperating in
this particular case. We later learned that it was developed using the Flutter framework, Our research found that the Frida
notorious for making traffic intercepting difficult. However, not impossible! toolkit could indeed be used to map
to the function in memory while the
Jacques Coertze, Security Specialist, Orange Cyberdefense
mobile application was running.
However, we needed a signature
whereby the function could be
identified.
6
Full compromise
1
The Flutter Framework
Using a reverse-engineering tool
At its core, Flutter is an SDK. (Ghidra), we managed to track down
This SDK exposes UI and other the starting bytes of the function. We
common elements (i.e., HTTP/S ultimately wrote a custom Frida script
clients) that map behind the to dynamically hook into the function
scenes to native equivalents in and bypass the SSL verification logic.
the Android and iOS spheres. 4Penetration Thus, serving as yet another method
The SDK achieves this through a Patch whereby this could be achieved.
combination of Dart and C/C++
A public utility (reFlutter) exists
integrations.
that can patch any Flutter-
based client application to
bypass the SSL verification
logic. It works very well.
However, we wondered whether
one could achieve similar
results using the ever-popular
Frida instrumentation toolkit.
Lessons learned:
2
Diving into the
Some lessons that could be learned from this exercise:
Android SDK:
Shared Libraries ▪ While the Flutter framework does make traffic
interception difficult, it does not serve as a silver
Android Flutter-based applications are 3 Narrowing in on the SSL bullet solution for keeping attackers away.
primarily driven by two shared libraries:
Verification Logic
libapp.so and libflutter.so. The libflutter.so ▪ Developers should always work on the assumption
file contains the required functionality for We learned from the public that their applications’ network traffic is visible and
using the OS (network, file system, etc.) GitHub repositories that the Flutter could be tampered with.
and a stripped version of the DartVM. framework does not perform SSL
▪ Implement adequate anti-tampering and debug-
Meanwhile, the libapp.so file is a loader certificate verification. Instead, it
ging routines in mobile applications to prevent
for the libflutter.so file. Both files contain depends on a third-party SSL library
attackers from modifying the shared libraries or
an MD5 hash (the snapshot_hash), which known as BoringSSL. While scouring
memory contents at runtime.
uniquely maps back to the public GitHub the public source code of this library,
repositories of the Flutter framework and we identified that the SSL certificate ▪ Always ensure that sufficient server-side valida-
Dart SDK. verification logic resided in the /ssl/ tion is present for any client-supplied data – work
ssl_x509.cc file and the contained on the assumption that data originating from the
ssl_crypto_x509_session_verify_ mobile application is unsafe by default.
cert_chain function – a function that
returns a Boolean indicating whether
the SSL certificate is valid.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

130 Security Navigator 2024 Research: Fake News and False Positives 131
Charl van der Walt
Head of Security Research
Orange Cyberdefense
Research:
Fake News and
False Positives
Every year since we started the Navigator project, we’ve kept track of the
ratio between confirmed ‘True Positive’ findings, and ‘Other’ Incidents
statuses like False Positives, Unconfirmed, and others.
Over the years since, our CyberSOC teams have also been integrating
worldwide operations, upgrading platforms, introducing new detection
technologies, enhancing processes, and generally improving the depth
and breadth of our capability. This continuous internal evolution can
make tracking a single metric (like the True Positive / False Positive ratio)
tricky. Nevertheless, by normalizing our incident data as far possible over
time, some clear and compelling patterns emerge.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

Research: Fake News and False Positives
?
The Usual Suspects
Research Question:
The detection domains listed in the chart below are described It’s important to note however that the levels shown below are
How does the age of a customer in more detail later in this report. The chart shows Other’ correlated with high levels of visibility, but are not necessarily
(Unconfirmed) as a proportion of all Incidents for clients who caused by it. There are of course other factors that contribute
have 60% or higher coverage for the domain illustrated. the level of detection efficiency we deal with from client to
effect incident proportions?
client.
We note that Unconfirmed are the most frequent for customers
with significant coverage in the ‘Network’ and ‘Infrastructure’
detections domains. High levels of Endpoint detection coverage
also correlate with high levels of unconfirmed incidents, while
clients with high levels of ‘Cloud’ visibility experience the lowest
We find that Incident volumes grow rapidly as more security telemetry is added. False Positives levels of Unconfirmed incidents.
grow more quickly than Confirmed Incidents, but the longer our clients remain in our service, the
more efficient and effective becomes, until we reach highly optimized level of accuracy.
Incident type over time
True Positive vs False Positive incidents across all customers over time Tracked accounts Confirmed (TP) Other 100%
100%
95%
90%
80%
90%
70%
60% 85%
50%
80%
40% 45%
30% 33% 75%
20% 25%
19% 70%
10%
0% 65%
2020 2021 2022 2023
The chart above illustrates the increasing number of incidents Since April 2022, we have tightened up our definition of a
60%
and the changing ratio between Confirmed and Other incidents ‘Confirmed’ True Positive Incident, which requires us to Perimeter Internet Infrastructure Network Endpoint Cloud Internal
we’ve been observing over the years. We see clearly how receive specific confirmation from the Client. A high number Security Infrastructure Security Security Security
Incident volumes have increased (from 39,000 to 129,395 ) as of Incidents impacts the CyberSOC - not the client - as our
the clients in scope per year increased by 343% between our analysts review each Incident before it is raised. Automation
2020 and 2023 datasets. is used to reduce the load from common False Positives on
the CyberSOC analyst, and centralized tuning process identify
But we can also see how the proportion of True Positive
problematic use case to improve or remove.
(Confirmed) incidents has decreased from 45% to 19% of total
Incidents over the same period. Rigorous tuning is essential to both the client and the
Service Provider, and regular tuning noticeably improves
detection efficiency. But tuning to improve efficiency without
CyberSOC Operations
compromising effectiveness requires a close cooperative
Our CyberSOC teams note the same ratio of Confirmed working relationship with the client. We’ll show later in this Why so much?
Incidents that we do. They define a Security Incident as follows: section how clients who have retained our services over time
and are able to provide feedback on the Incidents we raise will
It’s natural to wonder about this apparently low proportion of Confirmed Incidents.
have dramatically improved detection efficiency.
So, we investigated further, and three observations present themselves.
“Any potential or proven, undesirable and/or unexpected The client only ever sees the small number of ‘Confirmed’
event, impacting (or presenting a capacity of impacting) Incidents reflected by the orange bars in the chart above.
information security in the criteria of Confidentiality, But the closer the relationship we have with our clients, the
Integrity, and/or Availability”. better we are able to tune and the more efficient the detection
systems become.
%47.38 %45.38
%43.68
%09.78
%99.58
%09.28 %62.38
132 Security Navigator 2024 133
False Positive level by detection domain
Proportion of incidents classified False Positive for different detection types
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

134 Security Navigator 2024 Research: Fake News and False Positives 135
We see again how the proportion of ‘Confirmed’ vs ‘Other’ Incidents has decreased over time.
1. Quantity vs Quality
However, by tracking ratio between High and Low priority incidents over the same time, we can
also see how the proportion of ‘Low Priority’ True Positives (level 3 & 4) has decreased, while the
The chart below once again shows how the proportion of ‘Confirmed’ vs ‘Other’ Incident Status from
proportion of ‘High Priority’ True Positives (level 1 and 2) has increased.
our dataset has decreased from 45% to 19% over the past four years.
While Low Priority Incidents have become less common (84.70% in 2020 vs 67.60% in 2023), the
Incident priority flow by year proportion of High Priority Incidents has grown from 15.30% to 32.40% over the same period.
A similar period emerges when we track the occurrence of ‘Medium Incidents’ (Priority 2 and 3)
Proportional criticality of True Positive incidents across all customers over time
versus ‘Extreme Incidents’ (Priority 1 and 4):
45% Confirmed
2020
55% Other
Priority1 Incident status and priority over time
33% Confirmed 0,9%
Priority2 Proportions of criticality and True Positive incidents over time
Confirmed % (TP) Extreme Priority Medium Priority
2021 19%
67% Other 100%
Priority3
75% 90% 96.67% 95.87%
93.19% 92.20%
25% Confirmed
Priority4 80%
5%
2022
70%
75% Other
60%
19% Confirmed
50%
40%
2023
80% Other
30%
20%
It’s clear from the Sankey Chart above that most Incidents are not considered Confirmed True 10% 3.33% 4.13% 6.81% 7.80%
Positives. Of those that are, most of them are assigned a level 2 or level 3 (‘Medium’) priority. The
chart also clearly illustrates how the proportion of True Positives has sunk over time. 0%
2020 2021 2022 2023
To better understand this dynamic, we grouped Incident Priorities into ‘High’ (Priority 1 and 2) and
‘Low’ (Priority 3 and 4). The chart below shows how the ratio between High and Low Priority Findings
has changed over the years.
Incident status and priority over time
Proportions of criticality and True Positive incidents over time Confirmed % (TP) Other High Priority Low Priority The prevalence of ‘Extreme’ priority Incidents has almost doubled over the last two years.
This reflects a more acute and considered prioritization process, with a lower tendency
100%
toward more generic ‘Medium’ priorities like 2 and 3.
90% 84.7%
82.1% This clearly shows that the volume of Confirmed incidents we report is shrinking, while the
80% Severity of the Incidents we report is increasing.
73.6%
70% 67.6% Seen together we believe that these two trends suggest a general maturing in the discipline
of Threat Detection. Despite increased security event data and visibility, competent Cyber
60% Security Operations Centers are becoming better at filtering out noise and bringing only
confirmed, relevant and urgent incidents to their customers’ attention.
50%
40%
30% 32.4%
26.4%
20%
17.9%
10% 15.3%
0%
2020 2021 2022 2023
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

136 Security Navigator 2024 Research: Fake News and False Positives 137
2. Age and Wisdom - The Threat Detection Maturity Wave
‘Waves’ and ‘Cycles’ are all the rage in the research and analyst worlds these days, and as it
happens a very compelling ‘wave’ with familiar properties emerges when we consider how
detection efficiency changes as our clients mature with us.
Threat Detection Maturity Wave
Percentage of confirmed incidents relative to customer age
45%
40%
40%
35%
30%
25%
22%
25%
20%
20% 16% 16%
15%
11%
9%
10%
5% Security Req. Peak of Trough of ‘Over Ramp of Slope of
Valley of Iteration
Trigger Initial Tuning Exuberance’ Refinement Enlightenment
0%
1 to 6 7 to 12 13 to 18 19 to 24 25 to 30 31 to 36 37 to 42 43 to 48
months months months months months months months months
Our engineers typically recommend starting with the larger 3. Trough of 'Over Exuberance' [Month 13-18]:
alert sources that may require more tuning effort, so we can
After the value proposition for the CyberSOC service becomes
maximize the time we have to do so - usually firewalls, AD,
clear, and service delivery has stabilized, additional data
Sysmon; leaving lower impact but high data sources like
sources are added. The initial efficiency of this new security
DNS until the end. The repeated processes of adopting and
event data is sub-optimal, dropping all the way back to 11%,but
tuning new data sources results in the cycle of waves we see
tuning commences and efficiency rapidly starts to improve.
illustrated in the chart above:
4. Ramp of Refinement [Month 19-24]:
1. Security Requirement Trigger [Month 1-6]
Over this 6-month period tuning on the increased set of event
A new client decides to engage with us because they consider
sources continues, immediately bringing improved efficiency.
Threat Detection to be a necessary security capability
At the end of this period False Positives are significantly
and consider a Managed Security Service to offer positive
reduced and efficiency reaches 26%.
ROI. Upon signing a contract, we commence a structured
onboarding process to deploy the required technology and 5. Valley of Iteration [Month 19-36]:
start collecting events from in-scope security event data. The
It appears that customers will go through an additional cycle
efficiency of these initial sources is low (around 9%), but quickly
of security event data onboarding and tuning. This results in
improves as the detection tuning process commences.
another efficiency dip to 20%, before tuning results in a new
efficiency high of 28%.
2. Peak of Initial Tuning [Month 7-12]:
As tuning efforts proceed, the value of the initial data sources 6. Slope of Enlightenment [Month 36 and beyond]:
improves, increasing to 16% within the 1st 12 months of
Although we may anticipate some further troughs and peaks
deployment. While this number is still quite low, the customer
as changes occur in our service offering or in the client’s
starts to receive high-value alerts, and gets excited by what the
environment, we note that detection efficiency rises to around
service can offer. The overhead associated with the remaining
40% after 3 years.
False Positives never impacts the client because our CyberSOC
analysts triage and vet every alert. As per the agreed schedule,
onboarding of additional data sources commences.
Over 60% of clients in the age group older than 3 years have an efficiency rating of over 30%.
Those that are four years old even have efficiency levels of 45% and above.
At this maturity, efficiency is much higher than the average of 19% over all customers in the
2023 report year. Achieving the optimal balance between Efficiency and Effectiveness in Threat
Detection is a journey that can take several years to complete. A healthy working relationship
with a capable security partner, whether in-house or external, is clearly essential to ensuring
optimal results over time.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

138 Security Navigator 2024 Research: Fake News and False Positives 139
3. The unknown Unknowns As it happens, this confirmation very often doesn’t come, and
so the Status remains ‘Unknown’ in our records. In the analyses
As mentioned earlier in this section, our distinction between presented in this section, such ‘Unknown’ incident outcomes
‘Confirmed’ and ‘Other’ Incidents masks a deep pool of fall under ‘Other’ and may therefore skew the true prevalence of
complexity. Aside from True Positives our analysts record Confirmed True Positive Incidents.
False Positives, True Legitimates, and ‘Unknown’ outcomes.
If Unknown incidents were simply classified along the same
The Unknown outcomes indicate tickets where we have not
proportions as the rest of our events, True Positive Incidents
received any feedback from the client, leaving us unable to
would increase to 22% of the total.
determine whether an Incident was legitimate or not. The
alerts we raise with our customers are carefully analyzed and Our CyberSOCs have noted that there is a strong correlation
vetted and only raised with the Client when we have high level between the detection efficiency of a client, and the degree of
of confidence in them. Still, we can often not be completely feedback we get from the client. This is clearly illustrated in the
certain until we have received confirmation from the client. chart below, which once again looks at Incident Status relative
to amount of time a client has been with us:
We only mark Incidents as ‘True Positive’ when we have
specific confirmation from the customer that a real security
Incident confirmed.
Distribution of Status vs. Client Age
Proportion of incidents classified as Unknown across age in months
Unknown True Positive True Legitimate False Positive
100% 3.66%
7.64%
15.33% 13.57% 11.36%
90%
80%
70%
60%
50%
Summary
40%
30%
It is clear that the efficiency of our detection operations (as expressed by the
20% proportion of potential Incidents that are labelled as ‘Confirmed’ by our analysts) is
decreasing over time, although we must emphasize that this categorization has a
10% huge blind spot in the form of Incidents we report but get no feedback on. We argue
that this is the natural and inevitable consequence of increased levels of visibility, as
0%
1-10 11-20 21-30 31-40 41-50 expressed by our rudimentary ‘Coverage’ metric.
We note, however, that a decrease in apparent efficiency is not a bad thing,
As this chart shows, the longer a customer has been with us, And it might be the level of feedback that drives the efficiency,
especially for Clients who don’t have to deal with growing volumes of unconfirmed
the lower the level of ‘Unknown’ Incident statuses becomes. rather than other way around: As our client’s ‘mature’ in their
Incidents. Indeed, we show that while the ‘quantity’ of incidents we report to our
We’ve noted previously that at this ‘Age’ the detection efficiency consumption of the service they improve their ability to act
clients has decreased proportionally over the years, the ‘quality’ (as expressed by
of client accounts could be twice as good as the average (45% on the Incidents we raise with them and refine the process of
the proportion of Confirmed High Priority Incidents) has actually increased. We
or higher). It seems to us therefore that the three variables are providing us with feedback. With sufficient feedback we are
argue that this is a function of detection tuning, more rigorous analysis, and other
correlated. able to perform intelligent tuning and thereby improve detection
service enhancements.
efficiency, in a repeating cycle.
It seems to us therefore that the three variables are correlated:
We illustrate how an overall ratio between Confirmed and Other Incidents is
▪ client ‘Maturity’ as reflected in the ‘Age’,
actually misleading, as this ratio varies greatly from Client to Client. Indeed, as
▪ the level of feedback on Unknowns, and we examine this variance, we observe that the efficiency of mature, established
▪ the detection efficiency. clients can be four times higher than that of new Clients who are just starting their
onboarding journey with us. We believe this client maturity is strongly expressed
in the frequency with which we receive feedback on the Incidents we raise. The
more regular and detailed feedback we receive, the better our tuning and analysis
becomes, and the more detection efficiency improves.
Our CyberSOC operations strongly emphasize how important it is that the Client works
Finally, we introduce the ‘Threat Detection Maturity Wave’, which captures the
together with their Security Service Provider in a mature, transparent and trusting manner.
repeating phases of data ingestion and tuning that ultimately lead to a plateau of
productivity where Confirmed Incidents constitute almost half of all processed
With strong bi-directional communications the service can improve much more rapidly,
events and appear to continue trending gradually upwards from there.
resulting in higher efficiencies and better security outcomes.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

140 Security Navigator 2024 Research: Fake News and False Positives 141
?
This immutable principle has varying impacts in different domains of detection, however, as the chart
below illustrates:
Research Question:
Detection efficiency vs. Coverage
Is more security visibility better?
Percentage increase from minimum to maximum detection coverage
|     |     |     |     |     |     |     |     |     |     |     |     |     |     | % Increase in Confirmed (TP) |     | % Increase in Other |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | ------------------- |
700%
600%
%106
Adding more telemetry to a detection capability undoubtedly increases the ‘effectiveness’ of the  %575
| program (the number of incidents that will be identified), but also decreases the ‘efficiency’ (the  |     |     |     |     |     |     |     |     | 500% |     |     |     |     |     |     |     |
| ---------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| ratio between Confirmed incidents and ‘noise’).                                                      |     |     |     |     |     |     |     |     | %694 |     |     |     |     |     |     |     |
%154
400%
Covering our Assets
|                                                                    |     |     |     |                                                                   |     |     |     |     | 300%      |      | %533 |     |      |      |      |     |
| ------------------------------------------------------------------ | --- | --- | --- | ----------------------------------------------------------------- | --- | --- | --- | --- | --------- | ---- | ---- | --- | ---- | ---- | ---- | --- |
| Since last year we have attempted to assess the level of           |     |     |     | This process is imperfect and incomplete, but we believe it is a  |     |     |     |     |           |      |      |     |      |      |      |     |
| coverage our clients have in terms of detection capabilities. The  |     |     |     | first step toward providing some essential context around our     |     |     |     |     |           |      |      |     |      |      |      |     |
|                                                                    |     |     |     |                                                                   |     |     |     |     | 200% %442 |      |      |     |      | %332 | %632 |     |
| idea is to get a sense of how much potential security telemetry    |     |     |     | CyberSOC incident data.                                           |     |     |     |     |           |      |      |     |      |      |      |     |
|                                                                    |     |     |     |                                                                   |     |     |     |     |           | %691 | %881 |     | %881 | %591 |      |     |
we are actually ‘seeing’. As we are an external provider to our  %381
|                                                              |     |     |     | Since each client can be assigned a maximum of 5 ‘points’ for  |     |     |     |     |      |     |     | %831 |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- |
| clients, the amount of security telemetry we have access to  |     |     |     |                                                                |     |     |     |     | 100% |     |     |      |     |     |     |     |
coverage in a given domain, we can assess how much visibility
varies greatly.
we have across our clients relative to the visibility we’d ‘like’ to
| Further detail on the extent of our coverage scores is provided  |     |     |     | have in each domain. |     |     |     |     | 0%        |          |                |         |          |     |       |           |
| ---------------------------------------------------------------- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --------- | -------- | -------------- | ------- | -------- | --- | ----- | --------- |
|                                                                  |     |     |     |                      |     |     |     |     | Permiter  | Internet | Infrastructure | Network | Endpoint |     | Cloud | Internal  |
in the research notes - Extent of our Threat Detection Coverage
Perhaps unsurprisingly, we assess that we have the highest  Security Infrasturcture Security Security Security
Assessments over time.
degree of visibility into our clients’ ‘endpoint’ telemetry,
As we can see from the chart above, ‘Confirmed’ Incidents generally increase more slowly than
which includes EDR, Sysmon and other endpoint security
What we can see solutions. The lowest degree of visibility is reported for ‘Internet  ‘Other’ incidents as Coverage increases.
Infrastructure’ on the other hand.
But in our dataset there are some exceptions, notably:
As there is no hard quantitative means of deriving the level of
▪
coverage, we rely on a manual assessment involving the people  ‘Network’ detection includes Internet traffic, Internal East/West Traffic and Network Traffic
who work directly with the client.  Analysis (NTA). As we increase detection in this domain, we observe Confirmed Incidents
increasing much faster than Others.
▪
‘Endpoint’ detection includes Anti-virus, EP/EDR, Sysmon and MS Defender. In this domain,
Insight per detection domain
Confirmed Incidents increase at 233% while Other incidents only increase at 195% as Coverage
increases from Minimum to Maximum levels.
Actual visibility as a proportion of total potential per detection domain
Getting more serious
| Cloud Security |     |     |     | 33% |     |     |     |     |     |     |     |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
How does the Priority assigned to Incidents change with Coverage? The chart below depicts
Endpoint Security 61% the proportion of Incidents at each Priority level for Confirmed Incidents, relative to the assessed
coverage score of customers on a scale of 1 to 35:
| Network |     |     |     |     | 42% |     |     |     |     |     |     |     |     |     |     |     |
| ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Criticality vs. Coverage
Infrastructure 41% Distribution of Incident Priorities relative to Coverage Level
|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     | Priority 1 Priority 2 | Priority 3 Priority 4 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --------------------- |
100%
| Internal Security |     |     |     |     | 43% |     |     |     |     |     |     |     |     | 5%  |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                   |     |     |     |     |     |     |     |     |     | 13% | 13% |     | 14% |     | 13% |     |
|                   |     |     |     |     |     |     |     |     | 17% |     |     | 14% |     |     |     | 16% |
90%
| Internet Infrastructure |     |     |     | 24% |     |     |     |     |     |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
80%
28%
| Perimeter Security |     |     |     |     | 35% |     |     |     |     | 31% |     |     |     |     |     |     |
| ------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|                    |     |     |     |     |     |     |     |     | 70% |     |     |     | 35% |     |     |     |
39%
|     | 0%  | 10% | 20% | 30% | 40% | 50% | 60% | 70% | 40% |     | 50% |     |     | 67% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     |     |     |     |     | 60% |     |     | 51% |     |     |     |     |
Is more less?
50%
| We’ve argued elsewhere in this report that adding more  |     |     |     | Detection efficiency can be improved with careful tuning over  |     |     |     |     | 40% |     |     |     |     |     |     |     |
| ------------------------------------------------------- | --- | --- | --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
44%
telemetry to a detection capability undoubtedly increases  time, but efficiency appears to drop as Coverage increases.  41%
| the ‘effectiveness’ of the program (the number of incidents  |     |     |     | Thus, the trade-off between effectiveness and efficiency in  |     |     |     |     | 30% |     |     |     |     |     |     |     |
| ------------------------------------------------------------ | --- | --- | --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
that will be identified), but also decreases the ‘efficiency’ (the  Threat Detection appears to present as another immutable law  51%
|     |     |     |     |     |     |     |     |     | 43% |     | 27% |     |     |     |     | 45% |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ratio between Confirmed incidents and ‘noise’). Obviously,  of cybersecurity. 20% 29%
the amount and type of telemetry we are monitoring for our  28%
10%
clients will have a significant impact on the volume and type of  15% 16%
9%
incidents we are reporting, including the ratio of ‘Confirmed’ to  6%
0%
| ‘Other’ incidents.              |     |     |     |     |     |     |     |     | 0   | 5   | 10  | 15  | 20  | 25                         | 30  | 35  |
| ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     |     |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |

142 Security Navigator 2024 Research: Fake News and False Positives 143
There is clearly some variance in the distribution of priorities as coverage changes. These peaks
and dips probably have more to do with specific attributes of the client then other factors. However,  Research Notes
when we look at the difference in each Priority level as coverage increases, we note that some Priority
levels vary more drastically than others:
|     |     |     |     |     | CyberSOC Data:   |     |     |     | Infrastructure, e.g. |     |     |
| --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | -------------------- | --- | --- |
Criticality delta vs. Coverage Defining Threat Detection ‘Coverage’ Scores ▪
DHCP Logs,
|     |     |     |     |     | To gain a sense of how much of our clients’ security telemetry  |     |     |     | ▪   |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- |
DNS Request Logs,
Change in the distribution of incident priority as coverage increases we have access to, we derive a simple metric that describes
▪  Web Server / Web Application Logs
6.0% the breadth and depth of detection coverage our clients in this
|     |     |     |     |     | dataset have. The ‘coverage rating’ scores are estimated by our  |     |     |     | Internet Infrastructure, e.g. |     |     |
| --- | --- | --- | --- | --- | ---------------------------------------------------------------- | --- | --- | --- | ----------------------------- | --- | --- |
+4.3%
Technical Managers closest to each client and range from 0-5
▪  Web Server / Web Application Logs,
| 4.0% |     |     |     |     | as explained below:  |     |     |     |     |     |     |
| ---- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- |
▪  Web Proxy Logs
|     | P1  |     |     |     | Coverage Rating Scores  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
n
| 2.0% | ge i |     |     |     |                  |     |     |     | N etw o r | k ,   e . g .       |     |
| ---- | ---- | --- | --- | --- | ---------------- | --- | --- | --- | --------- | ------------------- | --- |
|      | n    |     |     |     | 0.  No coverage  |     |     |     | ▪         |                     |     |
|      | ha   |     |     |     |                  |     |     |     | In te     | r n e t  t r a ffic |     |
C
|       |     |      |      |      | 1.  Minimal coverage  |                           |                           |                            | ▪                               |     |     |
| ----- | --- | ---- | ---- | ---- | --------------------- | ------------------------- | ------------------------- | -------------------------- | ------------------------------- | --- | --- |
| 0.0%  |     |      |      |      |                       |                           |                           |                            | Internal East/West Traffic      |     |     |
|       |     |      |      |      | 2 .   S o m           | e   c o v e r a g e ,  b  | u t  le s s  t h a n  r e | c o m m e n d e d          |                                 |     |     |
|       |     | P2   | P3   | P4   |                       |                           |                           |                            | ▪                               |     |     |
|       |     | n    | n    | n    |                       |                           |                           |                            | Network Traffic Analysis (NTA)  |     |     |
|       |     | ge i | ge i | ge i | 3.   A p pr           | o p r ia t e   c o v e ra | g e ,  in c l u d in g    |   a ll  th e  b a s ic s   |                                 |     |     |
| -2.0% |     | ha n | ha n | ha n |                       |                           |                           |                            |                                 |     |     |
C C C 4.  Good coverage, including the basics and more  Endpoint, e.g.
▪  Anti-virus,
5.  Complete coverage
| -4.0% |     |     |     |     |     |     |     |     | ▪  EP/EDR,  |     |     |
| ----- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
-5.2%
▪
|     |     |     |     |     | We assess the coverage level for the following detection  |     |     |     | Sysmon, |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------------------- | --- | --- | --- | ------- | --- | --- |
-6.2%
|       |     |     | -6.4% |     | domains: |     |     |     | ▪            |     |     |
| ----- | --- | --- | ----- | --- | -------- | --- | --- | --- | ------------ | --- | --- |
| -6.0% |     |     |       |     |          |     |     |     | MS Defender  |     |     |
Perimeter Security, e.g.
Cloud, PaaS & SaaS, e.g.
▪
| -8.0% |     |     |     |     | Firewall logs,  |     |     |     | ▪   |     |     |
| ----- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
Azure - AD, Audit,
▪
|     |     |     |     |     | WAF Logs,  |     |     |     | ▪  KeyVault & VM,  |     |     |
| --- | --- | --- | --- | --- | ---------- | --- | --- | --- | ------------------ | --- | --- |
▪  IDS/IPS Logs,
The chart above illustrates that, as our visibility into a client’s security telemetry increases, the  ▪  O365,
proportion of ‘Low’ Priority Incidents (Priority 2, 3 and 4) tends to decrease (by 6.2%, 6.4% and 5.2%  ▪  Email Gateway Logs,  ▪
Lacework and Mondoo,
| respectively), while the proportion of Priority 1 Incidents increases (4.3%). Note that we observe  |     |     |     |     | ▪                         |     |     |     |     |     |     |
| --------------------------------------------------------------------------------------------------- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |
|                                                                                                     |     |     |     |     | VPN / Remote Access Logs  |     |     |     | ▪   |     |     |
significant variation here from client to client, so these figures should be considered with some  Palo Alto Prisma Cloud,
▪
| caution.  |     |     |     |     | Internal Security, e.g. |     |     |     | Checkpoint Cloudguard,            |     |     |
| --------- | --- | --- | --- | --- | ----------------------- | --- | --- | --- | --------------------------------- | --- | --- |
|           |     |     |     |     | ▪                       |     |     |     | ▪  Platforms like Adaptive Shield |     |     |
AD / Authentication Logs,
▪
Firewall Logs
CCoovveerraaggee  AAsssseessssmmeenntt
Summary
|     |     |     |     |     | CPrlioepnotsr taiosns eosf scelide nfotsr  acsosveesrasgeed  pfoerr  cyoevaer r age per year   |     |     |     |     |     | AAsssseesssseedd NNoott  aasssseesssseedd |
| --- | --- | --- | --- | --- | ---------------------------------------------------------------------------------------------- | --- | --- | --- | --- | --- | ----------------------------------------- |
It’s interesting to assess how increased coverage impacts the quality and
10205%0
quantity of the Incidents we raise with clients. There’s no doubt that the volume
90%
of Incidents increases with coverage – including Confirmed True Positives and
Other.
2800%0
| It’s harder to assess whether increasing coverage also changes the quality of  |     |     |     |     | 70% |     |     |     |     |     |     |
| ------------------------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the Incidents raised, but it does seem clear that the number of False Positives
6105%0
or Unconfirmed Incidents increases more quickly than Confirmed Incidents as
| Coverage increases.                                                                |     |     |     |     | 50%    |     |     |     |     |     |     |
| ---------------------------------------------------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
| We also see some evidence that the ‘quality’ of Incidents (as reflected in by the  |     |     |     |     | 4100%0 |     |     |     |     |     |     |
severity of Incident Priorities) increases with coverage. We caution however that
| the data used in this assessment has limited solidity and so present this finding  |     |     |     |     | 30%   |     |     |     |     |     |     |
| ---------------------------------------------------------------------------------- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
| as a thinking point, rather than a confident assertion of reality.                 |     |     |     |     | 205%0 |     |     |     |     |     |     |
10%
0%0
|     |     |     |     |     |     | 22002200 |     | 22002211 |     | 22002222 | 22002233 |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------- | --- | -------- | -------- |
As coverage assessment is a manual process, not all clients have completed assessment scores at the
time of writing this report. For the 2023 year, 45% of clients were assessed for detection coverage.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

Expert voice: Netherlands
Attack timeline
Cyberwarfare Target Operation
What we know, what we predict
and what you should be prepared for
When envisioning cyberwarfare, one might think of another
Hollywood blockbuster movie, but it is in fact a concerning reality.
The growing sophistication of these acts of cyberwarfare, combined
with increasing aggressiveness by nation-state actors supported by
non-state actors, could heavily impact countries around the globe.
Tamara Hendriksen, Information Security Officer
Jort Kollerie, Strategic Advisor
Orange Cyberdefense
What is Cyberwarfare? This is something that we see more examples of in the current
world we live in. A good example is the war of Russia against
The concept of cyberwarfare is difficult to define, and no Ukraine, where cyber activities play a big part in the overall
absolute definition is widely agreed upon. There is an ongoing warfare.
debate among scholars, experts and governments on the
definition of cyberwarfare and the characteristics that should
Types of Cyberwarfare
be included. There is the same ongoing debate with the term
'terrorism’. Researchers, over the years, cannot agree on a Nowadays, cyberwarfare is almost always part of a hybrid
solid definition, also because tactics and technologies are
warfare, where it can pose a significant threat to a nation-state.
ever-changing. This impacts the way we can define such
cyberattacks can assist as a supporting means of traditional
concepts. Most definitions do consider the same elements to
warfare. There is a difference between 'hard’ and ‘soft’ threats,
explain what constitutes cyberwarfare: nation-states, non-state
where hard threats can be seen as attacks on, or tampering actors (organizations), cyberattacks, (vital) information systems
with, systems/networks and soft threats are threats focusing
and disruption. An example of a definition used is: “the use of
on propaganda or espionage. Often, a combination of tactics
cyberattacks against a nation-state, causing comparable harm
and techniques is used. Types of cyberwarfare that can be
to actual warfare and/or disrupting vital computer systems”.
identified are:
Sometimes you will see different terms used interchangeably:
Espionage
cyberwarfare, cyberwar and even cyberterrorism. Some
experts state that these terms describe the same situation. This refers to the act of spying on another nation-state to
However, there is controversy on the way these terms are used.
obtain confidential or secret information. Traditional forms of
According to our research, using the term ‘cyberwarfare’ is
espionage, as well as cyber-espionage, in and of itself are not
to be preferred, as ‘warfare’ includes the techniques, tactics an act of war, but these activities can be considered as an
and procedures that make up the complexity of this term. It ongoing, standing situation between nation-states. Tactics, like
includes the engagement and form of war, acknowledging the using a botnet or spear-phishing attack can be used to gain
fact that these cyber activities are often part of hybrid warfare.
access to systems.
The term ‘war’ refers to a specific situation: a state of armed
conflict between nation-states or groups within a country. A Disruption
pure cyberwar is very unlikely to ever occur, as this would be This refers to modern economic systems that rely on, often
a situation where conflict would be purely fought with “cyber
complex, computer systems and networks. Attacking
weapons.” Cyberterrorism consists of unlawful attacks on
systems of economic facilities like banks, stock markets, large
(critical) systems/networks that are politically, religiously or
multinationals or payment systems can give attackers access
socially motivated. It can result in severe violence, intimidation
to funds or negatively impact the operations of a company or
or aims to generate a level of fear in society.
nation-state.
Research, however, shows us that cyberattacks on critical
systems do happen, but are not yet conducted by terrorists Propaganda
or aiming at the damage and goals that would qualify as
The use of the cyber domain to control information in all cyberterrorism. Therefore, when researching cyberattacks
available forms to try to control the minds and hearts of people against nation-states, the term cyberwarfare is used preferably.
living or fighting in the nation-state that is being targeted. It can
The advancement of technology has increased attention on the be considered as a form of psychological warfare, using fake
topic and the use of cyber activities in the geopolitical sphere news and social media. Doing so can expose embarrassing
can eventually lead to actual harm of civilians and critical truths or spread lies that may cause people to lose their faith in
infrastructure. their own country, or even sympathize with the enemy.
1102 DigiNotar hack resulted in the
compromise of CA servers &
certificates.
3102 Operation Socialist was enforced
by GCHQ to breach the telco
infrastructure of Belgacom.
8102
Russians, with a car full of
electronic equipment, plotted
to hack the world's chemical
weapons watchdog (OPCW) in
the Hague.
0202
Intrusion of SolarWinds Orion
caused the boldest supply chain
attack ever. This attack set
thousands of organizations at
stake.
0102 Stuxnet began to infiltrate and
destroy the network of a nuclear
enrichment facility.
2102 Shamoon, nearly 30k systems
wiped and caused major
disruption.
4102 The network of Sony Pictures got
compromised and a vast amount
of data got leaked.
1202
Colonial Pipeline suffered
from a ransomware attack that
heavily impacted computerized
equipment and disrupted gas
supply.
5102
Russia triggered the first-
ever blackout induced by a
cyberattack, turning off the
power of Ukraine.
7102
WannaCry ransomware
cryptoworm attack affected +/-
300k of computers worldwide.
NotPetya, the data-destroying
worm targeted Ukraine but
caused havoc worldwide.
2202
144 Security Navigator 2024 145
Sabotage
Not all threats originate from foreign groups or other nation-
states. Third parties that you may work with, competitors or even
insider threats (disgruntled/negligent employees) can cause
serious damage by creating disadvantages or stealing confidential
information and sabotaging daily operations.
Surprise attack
These attacks can be seen as having the same impact and effect
on a nation-state as the events on 9/11 or Pearl Harbor. These
are massive attacks that will catch an enemy off guard and might
weaken their defences. It can be used to weaken the target and
to prepare for follow-up attacks in a hybrid form. This type of
cyberwarfare is debated among experts, as it is considered unlikely
that one cyberattack can cause the same impact on a state as 9/11.
Information Warfare
A crucial component that is supporting cyberwarfare is called
information warfare. With information warfare, it is the objective to
gain an advantage over the opponent. Unlike traditional analogue
warfare and analogue techniques, no large financial resources
are needed yet to initiate information warfare; the vast knowledge
of systems, networks, applications, and tooling are the only
requirements. Some of the possible types/methods and/or tactics to
gain an advantage over the opponent are:
▪ Datamining: from the early days of the internet, commercial
companies (like Facebook, Apple, Google and Microsoft)
offering online services have been able to collect huge amounts
of data on citizens and organizations. Some government
agencies are actually playing catch-up to collect that data as
well, to use it to monitor citizens and society. This is mainly
enforced by various regulations and legislation, with projects to
tap data on a large scale;
▪ Legal Arms Race: between the West and the ‘rest of the
world’, there can be considered to be a legal arms race. The
West is ‘bound’ by digital regulations that curb activities like
monitoring of citizens, and they must often deal with new or
modified rules and legislation that are often countered by
privacy activist groups. While some non-Western countries also
have certain rules and legislation in place, in most cases, it is
limited to the home country and does not focus on their foreign
activities;
▪ Spy Tech: the growth and rapid adoption of digital technology,
its solutions, products and applications have become
indispensable in today's society. The origins of suppliers
and manufacturers are from all over the world. They could
play a conscious and unconscious role in the intertwining of
technology between companies and governmental bodies;
▪ Weaponization: data on citizens, organizations and countries
is being collected on a large scale. This information is usually
publicly available (e.g., social media, search engines and other Prior to Russia's war against
platforms), but data captured in hacks and dumped online Ukraine, the country was under
also plays a crucial role. The effects of weaponizing data can digital pressure and attacks.
be seen in for instance, election fraud and interference or mis/
disinformation of news.
Surprise Attack on Espionage/ Disruption
Attack industry/OT intelligence attack
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com
dnegeL

146 Security Navigator 2024 Expert voice: Netherlands 147
The multi-domain battlefield The usual suspects
Over centuries, the battlefield has expanded from land, sea and To get a better understanding of cyberwarfare and how this is
the air, to now include the space and cyber domain. Related to perceived around the globe, we have gathered 93 publications
this, today’s world consists of the human landscape, physical and reports over the year 2022. These documents were
landscape and information landscape. Combined, a multi- released by several governmental bodies and security vendors.
domain battlefield has been created. Within the multi-domain The most profound finding is that 94% of the reports originated
battlefield, cyberwarfare has found its place; it has become the from western countries. The others (6%) originated from non-
most attractive domain for power projection in the world. This western countries. We can conclude that our perception on
Future
is indeed what we have seen in recent years and what can be the topic of cyberwarfare is clearly shaped by the fact that
considered to take dangerous forms. these reports mainly focus on the threats originating from non-
Attacks are borderless since IT (Information Technology) is distributed globally and we live
Western countries. Also, the majority of the reports that discuss
Examples of substantial catastrophic situations have in an interconnected world. IT/OT (Operational Technology) convergence and its associated
cyberwarfare, describe which nation-states they perceive as
not occurred yet, but they may arise in the near future. risks can affect organizations accross segments and countries. Geopolitics dynamics will
the actors that form the greatest risk. These Countries can be
Nation-states have always attempted to use new forms accelerate countries towards increased measures for digital resilience.
found in almost all sources referred to as "usual suspects".
of technology in their use of warfare, so the same applies
Countries that can be expected to be on such a list and can be Computers are scaling, they get faster and will permeate all aspects in our lives. New
to the use of cyberwarfare methods. The threat lies in the
found in almost all of the sources. However, we can say with techniques will also dramatically increase the impact of cyberwarfare on a global scale since
expanding belligerence that nation-states are willing to
certainty that the battlefield of cyberwarfare is also shared with there are limited obstacles in adopting it.
deploy to strengthen their position in the geopolitical sphere.
Western nation-states as well. When researching the cyber
The possible effects of collateral damage, regarding this So, to speak, the evolution of technology will be followed by the use of more sophisticated
strength and capabilities of nation-states, the United States
belligerence, will also greatly increase over time. attacks within the concept of cyberwarfare. Since there are no limits, the origin of the
will almost always be on top of the list, as they have extensive
perpetrators requires international awareness and knowledge gathering of these emerging
An important contributing factor here is that within the cyber offensive and defensive capabilities. An interesting fact is
threats from across the world.
domain, the defense does not know what the offence strategy, that we have seen an increase in more non-Western reports
strength and/or capabilities are. Moreover, activities within this year, albeit from their perspective of course. Whatever If cyberwarfare becomes the main mode of warfare of the future, we should be prepared for
cyberwarfare are often cost efficient and can be conducted nation-state is the source of such a report, we must take into a global scale of impact on society. This is what is called collateral damage and since we
almost in real-time. The added advantage on top of that is that account that there is always a form of bias that may affect the live in an interconnected world and we cannot eliminate or prevent cyberattacks, we must
these activities are often stealthy. information in the reports and the way we perceive it. focus on reducing the blast radius.
People's Republic Russian Federation
Conclusion
of China "Bear"
"Panda" With many different opinions and views on the concept, what can we take away
+/- 49 APTs identified, most
from research on cyberwarfare? There are a few things to consider within the cyber
notable: APT28 (Fancy Bear,
+/- 136 APTs identified, most domain that may be of impact to cyberwarfare. It is important to address the effects
Pawn Storm, Sofacy, Strontium),
notable: APT1, Comment of geopolitics; it is undeniable that political situations or changes in the geopolitical
CyberBerkut, CyberCaliphate,
Crew, Comment Panda, sphere between nation-states can impact cyber activities undertaken. Objectives
Sandworm, APT29 (Cozy Bear,
Byzantine Candor, APT2, Putter and the changes in threats from nation-states or (state-sponsored) threat actors can
Office Monkeys, Duke, CozyDuke,
Panda, Group 36, SearchFire, be influenced by those changes in geopolitics and negatively impact the world.
CozyCar, Nobellium), Turla APT
MSUpdater, 4HSCrew,
(Snake, White Bear, Uroburos,
SULPHUR, TG-6952, APT31, Cyber activities are often borderless and limitless. In our modern world, we live in
Waterbug, Energetic Bear, Berserk
Storm-0558 an interconnected world. It is often relatively cheap, anonymous, and stealthy to use
Bear, Venomous Bear)
cyberattacks to target other nation-states and create an impact. Organizations need
Threat level: to be aware and create an understanding that they sometimes can be the ultimate
Threat level:
gateway in the execution of an attack. To be aware of your own position in the cyber
domain and your relation to, for instance, governmental bodies, can aid in creating
an assessment of the posed risk and the steps you might need to take in making
yourself more cyber-resilient. Even though cyberwarfare activities are often aimed
Democratic People's Islamic
at nation-states, there might be collateral damage, when organizations and civilians
Republic of Korea Republic of Iran are impacted in the supply chain or fall victim to one of the cyberattacks that may be
"Chollima" "Kitten" part of a hybrid warfare.
+/- 12 APTs identified, most +/- 42 APTs identified, most
notable: Bureau 121, Lab 110, Unit notable: APT33, APT35 (Charming
180, Unit 91, 128 Liaison Office, Kitten), APT39, G0069, G0077,
413 Liaison Office APT34 (OilRig, Shamoon,
DarkHydrus, Helix Kitten)
Threat level:
Threat level:
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

148 Security Navigator 2024 Hacktivism: victims and impact 149
Diana Selck-Paulsson
Lead Seurity Researcher
Orange Cyberdefense
Victims & Impact:
Hacktivism
revisited
Hacktivist groups like Legions of the Underground, Anonymous
and the Syrian Electronic Army have been a feature of the threat
landscape for decades. Several individuals have also been
responsible for personally motivated Denial of Service attacks or
website defacements. Groups like Lulzsec caused mayhem in the
name of their own brand of naïve, pseudo-moralistic messaging and
groups like Guardians of the Peace are suspected to faux political
fronts for cynical state-backed actors. Hacking, crime, espionage,
politics and ideology have long been difficult to tease apart, and
hacktivism has always been a central, if somewhat benign element
of this complex mix.
But in the past 2 years we have seen an apparent increase of
activity in the hacktivism space. Hacktivism can be understood
as a form of computer hacking that is done to further the goals of
political or social activism. It therefore calls the public’s attention to
something the hacktivist believes is an important issue or cause[94].
Often the cause is religiously or politically driven, and the hacktivist’s
goal is to disrupt services or otherwise using hacking techniques
made visible to bring attention to a specific cause.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

Top 5 (pro-Russian) Hacktivist Groups
?
As observed in the past 12 months (data contributed by Intel471)
Research Question:
4%
5%
Have we experienced a big
hacktivism surge since the war 13%
NoName057(16)
against Ukraine began? Anonymous Sudan
CyberArmyRussia
Anonymous Russia
18% 60% KillNet
Hacktivism incidents in 2023 Since then, attacks from hacktivist groups involved in the
conflict, siding with either Russia or Ukraine[99], have reached
The majority of hacktivism we have observed in the past 12 unparalleled levels. But of course, hacktivist activity observed
months cannot be described as ‘major incidents’, although in the past 12 months is not only bound to the war against
this is of course a question of perspective. However, we are Ukraine, other geopolitical events have sparked the creation of
observing two significant trends. new groups that are not engaged with the ongoing war. Most
recently, new waves of hacktivist activity spurred after the First, we have observed a significant surge in hacktivism
Hamas-Israel war began anew. activity.
These hacking activities are significantly inter-connected with
Secondly, we see how individual hacktivist groups are joining
each other, and with events occurring in the real world. Not only
collectives that then enable them to tap into additional
do we witness cyber events that impact the physical world; but resources of this collective and hence increase their
we observe physical events that illicit a direct cyber response capabilities. Examples for this include recent #OpCountry
from Threat Actors, thus in turn causing an escalation of those operations such as #OpSweden, #OpAustralia and #OpFrance,
very same geopolitical tensions. We see a new levelling of in which hacktivists call out to their fellow hacktivists to join a
the physical and cyber battlefields, resulting in a very thin line campaign to attack targets in a certain country. Often sectors
between physical (war) and cyber (hacktivism) [100]. such as media, energy, governmental and telecommunications
are affected by these attacks.
Until recently (or until the beginning of the war against Ukraine), As Dr Vasileios Karagiannopoulos
hacktivism generally emerged in one of two extremes: truly and Professor Athina Karatzogianni put it [101]:
impactful attacks or low-level disruptions. With the beginning
“Contemporary events show us that hacktivism has become of the war, the line between these two extremes began to
mainstream and is now an inevitable dimension of political blur, and at the same time a massive surge in activity could
conflicts, even those that end up in kinetic clashes between be observed. This was especially apparent after the hacker
states, testing the virtual limits of symbolic, sensationalist collective Anonymous declared ‘war’ on Russia[95] and
hacks, vigilantism, cyberespionage, and the Ukrainian Minister of Digital Transformation Mykhailo
even cyberwarfare.” Fedorov asked individual hackers on the internet for help at
the beginning of the war[96][97], creating the first IT Army of
Ukraine[98]. Again, collective efforts were used to increase the
Hacktivist groups in
potential impact of hacktivist efforts.
support of Russia
Most of the hacktivist attacks that we are observing are
Distributed-Denial-of-Service (DDoS) attacks. Simply put,
DDoS attacks are when an attacker floods a server with
internet traffic to prevent users from accessing connected
online services and sites. Hacktivists target private and
government organizations alike, and we have seen that
hacktivist groups can take down even the biggest national or
international websites. Some hacktivist groups have developed
strong DDoS capabilities, while others are rather noisy about
their capabilities and impact, applying a language and narrative
that is disproportional to their actual action (and impact).
In both cases the result is Fear, Uncertainty and Doubt (FUD)
– the escalation of anxiety, distrust, and disharmony – in an
already tense and complex geopolitical context.
215
966
883
194
533
113
944 624 544
150 Security Navigator 2024 Hacktivism: victims and impact 151
Such FUD is emblematic of a continuous evolution towards In some cases, hacktivists use screenshots and links to
‘cognitive’ attacks, which seek to shape perception through prove responsibility for ongoing attacks, often using a ‘check
technical activity. The impact has less to do with the disruptive host’ link, which is a tool for checking availability of websites,
effect of the attack or the value of the data or systems that servers, hosts and IP addresses[102].
may be affected (e.g. stolen, leaked or destroyed), but with the
KillNet is an unusual case and should be understood as impact that the attacks have on societal perception, discourse
a hacker collective that shares common objectives with and policy.
like-minded hacktivist groups. Groups that are believed to
In the past 12 months, our research team has given special have joined the KillNet collective are: Anonymous Russia,
focus to tracking the patterns in these hacktivist operations, Anonymous Sudan, Infinity Hackers Group, BEAR.IT.ARMY,
specifically pro-Russian hacktivist groups targeting Western Akur Group, Passion Group, SARD and National Hackers of
organizations. Additionally, our team collaborated with Intel471, Russia[103]. KillNet is really known for producing content on
who have shared their data on current hacktivist activity with their social media channel. They don’t execute many attacks
us. We used this data for the analysis shown in the following themselves but work through members of their collective such
sections. as Anonymous Russia and Anonymous Sudan .
The chart above reflects all hacktivist groups that we observed The highest level of hacktivism activity we have seen was in
operating in this context during 2023. February 2023, as can be seen below. This corresponds with
the emergence of hacktivist group Anonymous Sudan at the
The tracking primarily relies on announcements these groups
end of January 2023, who heavily targeted countries such
are posting in their publicly available channels. They often use
as Sweden, Denmark, the Netherlands and Australia
messenger apps such as Telegram to either announce future
during February.
victims or claim current victims. Motivation can vary from group
to group.
Hacktivism Activity 2023 (Q1 - Q3)
800
700
600
500
400
300
200
100
0
Jan Feb Mar Apr May Jun Jul Aug Sep
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

152 Security Navigator 2024 Hacktivism: victims and impact 153
During 2023, countries that were impacted the most by pro- However, Sweden only emerged in our data between January Who are the hacktivist groups Later, Anonymous Sudan would change their purported
Russian hacktivist attacks were Ukraine, Poland and Sweden. and March 2023, when the hacktivist group Anonymous motivation to attacking anyone ‘opposing Islam’. Their Telegram
and what are their motivations?
Sudan heavily attacked Sweden and Denmark. We will dive channel was created 3 days before the burning of the Qur’an
The focus on Ukraine is simply understood as the use of
into the Nordics and our observations of Sweden’s geopolitical in Stockholm, Sweden on 21st of January. There is indeed an
hacktivism as a tool in the war by Russia. The second most Two hacktivist groups that we have been tracking closely are
situation in the cyber and physical world later in this chapter. interesting correlation between the creation of the group itself
impacted country was Poland, which most likely is due to its Anonymous Sudan and Noname057(16). Both are directly
and the first burnings in Sweden in 2023.
geographical location. As can be seen below, the hacktivist or indirectly engaged with the ongoing war against Ukraine.
group that attacked Poland the most is NoName057(16), NoName057(16) emerged as a direct response to the war The January burning was the beginning of a chain of events
which was responsible for up to 70% of all attacks against that and has been active since March 2022. They appear to be which would complicate the ongoing application by Sweden to
country. Sweden has been the third most impacted country politically motivated. To reach a broader international audience, join NATO, but also lead to a questioning of the fundamental,
since the beginning of 2022. the groups launched an English-speaking Telegram channel democratic right of freedom of speech in Sweden and its
in August 2022, which translates selected messages and tolerance for the burning of religious scripts. It would also
announcements from their Russian channel to English. increase the terror threat levels[108] in Sweden and spawn the
Active Hacktivist groups and their targets Anonymous Sudan is apparently religiously motivated, but introduction of a bill to ban the burning of scripts in Denmark.
The full chain of events can be seen in the timeline on the next
the group’s activity and motivation are highly controversial,
page.
resulting in differing opinions on their origin, sponsorship and
700 NoName057(16) motivation. NoName057(16), on the other hand, state clearly The name Anonymous Sudan first mislead observers into
Anonymous Sudan that they are pro-Russian, and this is supported by their choice believing the group was part of the notorious hacker collective
600
of language, narrative and hashtags such as [Russian flag] “Anonymous”. But that notion was quickly dispelled by the
CyberArmyRussia
“victory will be ours”. An interesting observation is that they’ve Anonymous collective themselves on the 19th of February,
500
Anonymous Russia stopped using this phrase since the beginning of August 2023. when they distanced themselves from Anonymous Sudan. This
400 KillNet Why they have removed the slogan is unclear at this point. happened on the same day that Anonymous Sudan announced
that they had joined the pro-Russian KillNet collective. One day
BLUENET RUSSIA
300 A brief look at Anonymous Sudan later, Anonymous Sudan commented to the public, stating:
PHOENIX
200 NET - WORKER ALLIANCE Although Anonymous Sudan seemingly started their hacktivist
“message to all the idiots who think that we are Russians,
activities in response to demonstrations addressing religion;
National Hackers Russia we are 100% from Sudan and regarding that we support
100 they seem to have been distracted during late summer by other
Russia, yes we support Russia and we will continue to
UserSec conflicts that appear closer to their base location.
support it and we will not stop because they supported us
0
U kr ai n e P ol a n d S we d e n Lit h u a ni a G er m a
U
n
n
y
it
e d St
C
a
z
t e
e
s
c h
R e p u bli c It aly S p ai n Est o ni a D e n
U
m
n
a
it
r
e
k
d
Ki n g d o m Fr a n c e Isr a el C a n a d a A o
b in
f
e
s
S
A
l i
w
e u
n
v
e
d
o
e a
n s
m n
t y a
.
m
a
t
H
e
n
o d
o y
u
w
s e
c e
a
l
S
u v
r u
e
l
e
ie
s
d
r,
r a ,
p t
n
h
t
o
h
a i
i e
n
s
t t d
o h
t o
i r
o
g ig
e
h
t s
i
h
l n y
e n
, c fi
o fa
o n
t c
n a
m t
t n r
e t
c o
h a
i v
a
a
n
e
t
l r
t
f
t
s
h
u
h
i
e
n a
e y
d l
y
[ 1 i
d
0
a
n 4
o r
g ][
e
1
n
0 a
i
5
n o
n ][
d t
1 d 0
s e
6 m ]
u e
[1
p d
0 o 7
p
t ]
l
. i
o o
v W
c
a
rt a
t e i
t
o
e
n
d
a Te n l d e g th ra e m y s m up e p ss o a rt g e e d o S n u 2 d 0 a / n 0 2 b / e 2 f 0 o 2 re 3 ” (sic)
Russia. In fact, in their early days of January and February
2023, we believe that their attacks were most likely aligned with
Russia’s objectives to exasperate geopolitical tensions.
We explore what we have observed since day one of
Anonymous Sudan’s activities.
Anonymous Sudan created their Telegram channel
Most affected regions @AnonymousSudan on the 18th of January 2023. Their first
post read like this:
Zooming out to a regional level, we 3%
see that Europe was impacted by
7%
85% of all attacks seen in 2023 (n= 85% Europe
4016), followed by North America
(n=297) and the Middle East 7% North America
(n=113).
3% Middle East
2% Multiple Regions
1% Asia
1% Oceania
1% Africa
85%
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

A timeline of recent geopolitical events,
154 Security Navigator 2024 showing pro-Russian hacktivist activity  25/08/2023 155
impacting the Nordics between January and  Denmark presents bill
20/07/2023 21/08/2023
August 2023  banning the burnings of
t
I r a q   e x p e l l e d   t h e   S w e d i s h   S e c u r i ty   S e rv i c es  scriptures [121]   -  b u
 h e r e of
S w e d i s h   a m b a s - ra is e s   te r r o r  t h r e a t  le v e l   s to p e rp t
|                |     |     |            |                 |                       |     |     |            | o n ’ t   e x c |
| -------------- | --- | --- | ---------- | --------------- | --------------------- | --- | --- | ---------- | --------------- |
|                |     |     |            | s a d o r   i n |   r e s p o n s e     |     |     | n t s   d  | a s  a n        |
| Physical world |     |     |            |                 |                       |     |     | E v e      | e a n t   .     |
|                |     |     |            |                 |                       |     |     | s   m      | e n ts          |
|                |     |     |            | t o   a n o t h | e r   p l a n n e d   |     |     | t h is   i | o f   e v       |
|                |     |     |            |                 |                       |     |     | h a        | i n             |
|                |     |     | 19/07/2023 | Q u r ' a n     | b u r n i n g   i n   |     |     | h e   c    |                 |
t
Stockholm[116]
Iraqi police officers
22/07/2023
|     |     |     | trying to disperse a  |     |     |     |     | 14/08/2023 |     |
| --- | --- | --- | --------------------- | --- | --- | --- | --- | ---------- | --- |
Several Qur’an
protest outside the  burnings took place  NoName057(16) condemns
|     |                    |     | Swedish Embassy  |     |     |               |     | the burning of the Qur’an in  |     |
| --- | ------------------ | --- | ---------------- | --- | --- | ------------- | --- | ----------------------------- | --- |
|     | After 29th of June |     |                  |     |     | in Denmark,   |     |                               |     |
in Baghdad
|     |     |     |     |     |     | Sweden[120]  |     | Sweden. |     |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ------- | --- |
The repercussions of the Qur’an burnings
have extended beyond Sweden, as sev-
eral countries, including Iraq, Kuwait, the
29/06/2023
United Arab Emirates, and Morocco, have
Several known and unknown hacker
summoned Swedish ambassadors in pro-
groups including AnonymousSudan, 1919
test[114][115]. Team, Islamic Hacker Army, Host Kill Crew,
US NEXUS HACKER, Mysterious Team
29/06/2023 Bangladesh, KEP TEAM, UserSec collec-
Turkey’s president con- tive, Team Heroxr, Electronic Tigers Unit,
demns Qur’an burning in  Team R70, GANOSEC TEAM, and Türk
Sweden, signaling that  28/06/2023 Hack Team executed DDoS attacks on
28/06/2023
27/01/2023 this would pose another  NoName057(16) reacts  several Swedish websites. Another #Op-
Rasmus Palludan,  obstacle to Sweden’s bid  Salwan Momika, an Iraqi  to the burning and  Sweden campaign begins[119].
refugee in Sweden burns
right-extremist, burns  for membership[113]  attacks Sweden as a
| the Qur’an in   |     |     | pages of the Qur’an  |     |     | direct consequence |     |     |     |
| --------------- | --- | --- | -------------------- | --- | --- | ------------------ | --- | --- | --- |
Copenhagen[117]
16/06/2023
Sweden releases
official press release
on the 12th regarding
a support package for
22/01/2023
Turkey’s president  Ukraine [112]
condemns the Qur’an
| burning and is not          |     |     |     | 19/02/2023       |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
| willing to support Swe-     |     |     |     | Anonymous        |     |     |     |     |     |
| den in it’s effort to join  |     |     |     | Sudan joins the  |     |     |     |     |     |
| NATO[109][110][111]         |     |     |     | pro-Russian      |     |     |     |     |     |
KillNet collective
| 22/01/2023               |     |     |     |     |     | 18/06/2023           |     |     |     |
| ------------------------ | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- |
| Right-wing politician    |     |     |     |     |     | NoName057(16) at-    |     |     |     |
| Edwin Wagensveld in      |     |     |     |     |     | tacks Sweden due to  |     |     |     |
| the Netherlands tore up  |     |     |     |     |     | aid given to         |     |     |     |
| and burned pages of      |     |     |     |     |     | Ukraine[118].        |     |     |     |
the Qur’an
28/06/2023
Anonymous Sudan attacks
30/01/2023
|            |     | Anonymous Sudan be- |     |     |     |     | Sweden after the burning of the  |     |     |
| ---------- | --- | ------------------- | --- | --- | --- | --- | -------------------------------- | --- | --- |
| 21/01/2023 |     |                     |     |     |     |     | Qur’an, they state:              |     |     |
gins DDoS-ing Danish
Rasmus Palludan,
institutions because
| right-extremist,  |     |     |     |     |     |     | “We missed Sweden very much.  |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- |
03/02/2023
|     |     | of the burning of the  |     |     |     |     | And today they burned the Quran  |     |     |
| --- | --- | ---------------------- | --- | --- | --- | --- | -------------------------------- | --- | --- |
burns the Qur’an in  During February & March
|     |     | Qur’an |     | Anonymous Sudan  |     |     | again. Well, from now on, we will  |     |     |
| --- | --- | ------ | --- | ---------------- | --- | --- | ---------------------------------- | --- | --- |
Stockholm Anonymous Sudan attacks
declares cyber war on
Swedish and Danish institu- attack Sweden continuously for
|     |     |     |     | Sweden because of the  |     |     | months.. We will target all vital  |     |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | ---------------------------------- | --- | --- |
tions because of the Qur’an
burning of the Qu'ran
burning by Palludan (who is  infrastructure.”
23/01/2023
Swedish and Danish citizen
Anonymous Sudan begins
& done similar demon-
DDoS-ing Swedish and
strations in Denmark and
|     | 18/01/2023 | Dutch institutions because  |     |     |     |     |     |     |     |
| --- | ---------- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
Sweden in the past)
|     | Anonymous Sudan  | of the burning of the Qur’an |     |     |     |     | Digital world |     |     |
| --- | ---------------- | ---------------------------- | --- | --- | --- | --- | ------------- | --- | --- |
creates their Tele-
gram channel
| © Orange Cyberdefense 2023/2024 |     |     |     |     |     |     | www.orangecyberdefense.com |     |     |
| ------------------------------- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- |

156 Security Navigator 2024 Hacktivism: victims and impact 157
By the end of January, Anonymous Sudan began attacking By extorting victims for money, the group had transitioned
Sweden, Denmark and the Netherlands with the apparent from being religious and politically driven to being financially Anonymous Sudan in Q3 2023
motive to punish the respective countries for supporting or motivated.
allowing anti-Islam demonstrations. Indeed, during the first Anonymous Sudan victim countries July-September 2023
Technically Anonymous Sudan cannot be simply categorized
quarter of 2023, Anonymous Sudan would attack a wide variety
as “hacktivists”, but have adopted a Cyber Extortion and 12 Kenya
of countries and institutions for religious reasons, as can be
cybercriminal label also.
seen in the chart below.
United States
And hence, the group also adopted a new form of DDoS 10
In May, however, something shifted. Anonymous Sudan
showed signs of becoming financially motivated, for example, attacks with a financial touch, referred to as Ransom DDoS Israel
(RDDoS). During June they continued the new modus operandi,
claiming in their Telegram channel they have data to sell, from 8
attacking Microsoft services on a large scale and demanding France
an attack on an airline[122] . They also demanded a ransom from
US$ 1 million to desist in their attack[124]. As far as we know,
the Scandinavian Airlines (SAS)[123] in order to stop their DDoS
however, no ransom was paid to them. 6 United Kingdom
attacks. This suggested a challenge to their hacktivist identity.
United Arab
Emirates
4
Anonymous Sudan in Q1 2023 Netherlands
Anonymous Sudan victim countries January-March 2023 2 Nigeria
35 Sweden Cyprus
0
Denmark July 2023 August 2023 September 2023 Canada
30
Australia
25
Netherlands Throughout the short life of the threat actor, we noted several This pronouncement is in line with external reports that
20 geopolitical events that Anonymous Sudan commented on, and Sudan experienced electricity outages, and that the
United States
that also matched the actual ongoings in Sudan. Here are some internet connectivity was at 2 percent of the usual level[130].
15 examples: Additionally, two days prior to the internet outage (21st
France
of April), Anonymous Sudan DDoS-ed the social media
10 Germany 1. Amnesty International reports that since the 15th of platform Twitter (now called X), with the reasoning that
April 2023, the Sudanese Armed Forces (SAF) and
“Twitter has been down .The reason for our attack, we
5 Poland the paramilitary Rapid Support Forces (RSF), who are want to send a message to Elon Musk [SOS emoji] - Open
rival factions of the military government of Sudan, have
Starlink [satellite internet service] in Sudan[…].” This could
0 Norway been fighting for control in Sudan. Extensive war crimes be a reference to the help Elon Musk and Starlink provided
are being committed in Sudan[128]. On the same day, to Ukraine[131], - asking for the same support in the ongoing
January 2023 Febuary 2023 March 2023 Finland Anonymous Sudan posts to their Telegram channel:
conflict in Sudan.
“Prayers for Sudan”, followed by the message “In the
event that they shut down the Internet from Sudan, we will 4. The group repeated their action on July, 1st, attacking the
At the end of June, another burning of the Qur’an took place in But despite the tension that was now quite visible to the be back, do not worry”. They continue with a warning to social media platform X and posting the following message
Sweden, which sparked a wide-spread international response international public, Anonymous Sudan seem to have been other countries: “message to all countries that are trying to on their Telegram channel: “Twitter been down for hours?
from diverse countries, but also lead to several hacktivist distracted by other events. During July and August, they show the world that they are the ones who carried out the Elon Musk, do you have intentions to open starlink in
groups calling out for attacks against Sweden. The campaign focused heavily on another real-world conflict, the ongoing cease-fire in Sudan. We only see you when something big Sudan?”. They repeated this action on 28th of August,
#OpSweden was launched anew[125]. Another month of fighting in Darfur, Sudan[126][127]. If we review the countries happens so that the world says, ‘Wow, look, this country trying to gain Elon Musk’s attention.
burnings in Sweden and Denmark began. where Anonymous Sudan claimed victims during July and has done this and this. We see everything. We warn any
July marked the escalation of geopolitical pressure against August, we note that they were shifting their geographical focus country that tries to interfere in Sudan's internal affairs. We 5. On June, 1st 2023, the United States took measures to
Scandinavian countries (namely Sweden and Denmark) for towards United States, Kenya and Israel. This is a very big shift will attack it immediately’”. #AnonymousSudan’, on the respond to the crisis in Sudan[132]. Anonymous Sudan
allowing the hostile burnings of the Qur’an. News coverage of impacted regions in comparison to Q1, as can be seen in 15th of April 2023. responded to this on the 3rd of June, warning the United
the chart on the next page. Their justification for attacking the
circulated about a Qur’an burning in Norway, which was States not to get involved or “invade again”.
respective countries has also shifted. During July and August, 2. On the 22nd of April 2023, Anonymous Sudan attacked
investigated by Orange Cyberdefense Norway and shown to
they apparently became politically focused, they concentrating the official website of the Rapid Support Forces, which is The examples above support the claim that the group might
be fake news. In fact, images used in the news coverage was
heavily on countries that appeared to interfere with the conflict a paramilitary force formerly operated by the Government be Sudanese and either originate, or are currently located in,
material from 2019, when an actual burning in Norway took
in Sudan. of Sudan. It grew out of, and is primarily composed of, the Sudan. However, we can only assess the narrative presented to
place. Still, the incident illustrates the power of misinformation
Janjaweed militias which fought on behalf of the Sudanese us by the Threat Actors themselves, along with their observable
campaigns, which add to the already tense geopolitical So the shape of their victimology also changed: it has moved
government during the War in Darfur, and was responsible impacts. In August, an interview between Anonymous Sudan,
situation in the Nordics. closer to their self-proclaimed ‘home’ – Sudan - and the group
for atrocities against civilians. Its actions in Darfur qualify IntelCocktail[133] and BBC cyber correspondent Joe Tidy[134] [135]
has moved from an agenda driven by religion towards more
Indeed, hacktivism and mis/disinformation have emerged as as crimes against humanity according to Human Rights surfaces, a group member called ‘Crush’ shared their live
politically motivated activities. In Q3 especially, we see that
two sides of the same coin, and have increasingly come to Watch[129]. location on Telegram as proof that they are based in Sudan.
Kenya was the most impacted country, correlating with the
characterize the use of cyber within geopolitical conflicts.
ongoing Sudan conflict, in which Kenya’s president offered to
3. On the 23rd of April, Anonymous Sudan stated that “The
More detailed chain of events can be seen in the timeline. play a mediation role.
internet has been closed by 90% of Sudan. We hope
Elon Musk open Starlink in Sudan as soon as possible
#AnonymousSudan”.
© Orange Cyberdefense 2023/2024 www.orangecyberdefense.com

158 Security Navigator 2024 Hacktivism: victims and impact 159
How politically Let’s do a quick Victims of NoName057(16)
consistent are these groups? dive into NoName057(16)
NoName057(16) victim countries in 2023
Disinformation is difficult to identify. In the end, the truth The other hacktivist group we have been observing during
350
remains elusive: Is Anonymous Sudan a group of skilled 2023 is NoName057(16). NoName057(16) might be more
Poland
Sudanese ‘cyber warriors’ as they claim to be? Or are they politically consistent than Anonymous Sudan has proven
distracting us with false claims, while actually operating to be. 300 Lithuania
in another nation’s interest and maintaining ‘plausible Czech Republic
NoName057(16) has been active since the war against
deniability[136]’ as defenders of Islam striking at the West?’[137].
Ukraine began and has been targeting countries that are Italy
250
Anonymous Sudan is not very consistent. Our observations members of the the North Atlantic Treaty Organization
Germany
show that they have attacked victims all around the world, (NATO) and countries that are considered to oppose
Spain
shifting their purported motivations and reasonings frequently. Russi

<!-- CONVERSION_METADATA: {"source": "https://github.com/jacobdjwilson/awesome-annual-security-reports", "date": "2026-08-02", "model": "gemini-3.5-flash-lite"} -->
