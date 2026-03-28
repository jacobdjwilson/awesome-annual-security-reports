# OT-Cyber-Threat-Report 2026

## Table of Contents
- [Key Takeaways](#key-takeaways)
- [Introduction & Methodology](#introduction--methodology)
- [OT Incident Macro Trends](#ot-incident-macro-trends)
- [Nation States & Hacktivists](#nation-states--hacktivists)
- [Geographies and Industries](#geographies-and-industries)
- [How Operations Were Impacted](#how-operations-were-impacted)
- [Noteworthy Incidents & Near Misses](#noteworthy-incidents--near-misses)
- [Polish Energy Sector Attack](#polish-energy-sector-attack)
- [Broader Attack Trends](#broader-attack-trends)
- [Analysis – Where Did the Attacks Go?](#analysis--where-did-the-attacks-go)
- [Defensive Developments](#defensive-developments)
- [CIE Engineered Controls Database](#cie-engineered-controls-database)
- [Secure Connectivity Principles](#secure-connectivity-principles)
- [Looking Forward](#looking-forward)
- [Appendix A – 2025 Data Set](#appendix-a--2025-data-set)
- [Appendix B – Sources](#appendix-b--sources)

---

## Key Takeaways

- **Cyber incidents causing physical impacts in heavy industry and critical infrastructure dropped by 25% in 2025**, falling from 76 publicly recorded cases in 2024 to 57. Most of this decline appears due to an overall reduction in ransomware attacks because of a number of factors that are not likely to continue to “hold back the tide” – expect consequential breaches to start increasing again in 2026-2027.
- **Nation-state and hacktivist attacks doubled**, with most such attacks targeting critical infrastructures. Particularly noteworthy attacks in 2025 included:
    - **Jaguar / LandRover**: The most costly production shutdown in almost a decade.
    - **Collins Aerospace**: A crippled software-based system caused flight cancellations and delays for weeks – highlighting the need for rapid recovery or manual fall-backs for critical systems operated and managed by third parties.
    - **Grounded and mis-directed ships**: Highlighted the need for multiple independent checks on important external inputs, such as GPS signals.
    - **Polish distributed generation**: A near miss, because the lights stayed on, an example of the Russian nation state targeting European critical infrastructures, and a cautionary tale about “bricking” control equipment.
- **Database of “unhackable” mitigations**: The Cyber-Informed Engineering (CIE) initiative released a database of engineering-grade mitigations for cyber attacks, many of which deserve the title “unhackable,” and Secure OT connectivity principles.
- **The UK NCSC and partners released innovative guidance** that recognizes network segmentation and especially “unhackable” hardware-enforced segmentation as a key part of OT security, not just a compensating measure. These tools are powerful ways to address today’s automation and cyber realities.
- **Reality is that we continue deploying more automation** and increasingly connect that automation to the Internet and to cloud-based services, steadily increasing our risk profile. All this is in the context of legal and ethical obligations to make reasonable decisions when those decisions affect other people’s safety, critical infrastructures, or large amounts of shareholders’ money.
- **Experts and authorities increasingly recommend** that reasonable defenses include engineering-grade, hardware-enforced, deterministic protections such as unidirectional gateway technology and hardware-enforced remote access, in addition to IT-grade software protections.

In this time of costly breaches and nation states targeting critical infrastructures, OT security teams cannot assume that cyber attacks with physical consequences will somehow simply go away, nor that software-only defenses are adequate, given the sophistication of today’s ransomware, hacktivist and nation-state attacks. To this end, noteworthy developments in cybersecurity practice include:
- New advice from multiple agencies that encourages hardware-enforced protection and hardware-enforced remote access for OT systems.
- An update on Cyber-Informed Engineering, the most important new development in OT security in 20 years.

---

## Introduction & Methodology

This report documents cyber attacks with physical consequences. Security teams seeking funding for cybersecurity initiatives and business decision makers responsible for allocating such funding each need accurate data as to what breaches have occurred in the past, because those failures of security programs influence what attacks should be considered credible threats in the future. Planning for the future is especially important and especially challenging for industrial operations where every change poses a threat of errors and omissions that might materially impair safe, reliable or efficient/profitable physical operations. Given that changes to such operations can take place only at long intervals, it is especially important to use today’s threat data and trends to anticipate the threat environment our defenses will face towards the end of their deployment life cycle.

In 2025, there were 57 breaches that met the strict inclusion criteria for this report: a surprising 25% decline over 2024.

In support of understanding today’s threats and projecting tomorrow’s, this report documents attacks that breached cybersecurity defenses targeting physical operations and infrastructure that:
- Are deliberate in nature – not errors and omissions, and neither equipment nor software failures.
- Produce physical consequences including production delays or outages, equipment damage, environmental disasters, injuries, or casualties – not just data theft or computer system clean-up costs.
- Impact manufacturing, building automation, heavy industry, and critical industrial infrastructures, including the transportation of people and goods.
- Are found in public – not private – disclosures.
- Which the research team agrees meet the above criteria with a high degree of confidence.

This report’s data is therefore a conservative estimate, certainly under-reporting actual attack activity. Many incidents were excluded due to disclosure restrictions, insufficient confidence in authenticity, or lack of access to reports in certain languages or regions. Additionally, numerous attacks very likely went unreported or were deemed unreliable in censored conflict zones.

*The incident database and numbers in this report regarding breaches and outages are certain to be an underestimate.*

Any reader wishing to verify the year’s data can consult Appendix A, which contains the full data set of all incidents the research team counted in 2025. Readers interested in data from previous years should consult Appendix A in the 2025 Waterfall / ICS STRIVE OT Cyber Threat Report.

**Note – why include IT incidents?** A large fraction of ransomware attacks impair only IT assets, and still delay, shut down, or otherwise impact physical industrial operations. Businesses with physical operations need to know what cyber threats can impact their industrial operations, no matter which kinds of computers are targeted. To this end, this report documents all cyber attacks/breaches that impacted physical operations, no matter which cyber assets were compromised or impaired in the attack. For interested readers, the Section *How Operations Were Impacted* details how IT breaches most often impair physical operations.

---

## OT Incident Macro Trends

In 2025, there were 57 breaches that met the strict inclusion criteria for this report. As can be seen in Figure 1, this is a 25% reduction over the 76 comparable breaches in 2024. In the sections and discussion that follow, we explore aspects of these attacks and pull these aspects together into conclusions in Section *Analysis – Where Did the Attacks Go?*

![Breaches with physical consequences (2010-2025)]

As is evident in the figure, cyber breaches with physical consequences increased markedly at the turn of the decade. The single biggest reason for the step function change was ransomware. Figure 2 shows that the single type of adversary responsible for a clear majority of attacks in the years 2019-2024 is ransomware criminal groups. It is also the conclusion of the research team that in the years 2022-2025, the majority of “Unknown” incidents are also ransomware, because:
- Hacktivists generally mean to make a point with the victim and with the public, and so generally make public claims about their attacks, successful or not. No such claims were made for attacks in the “Unknown” category.
- Nation state attacks are still comparatively infrequent.
- For most “Unknown” attacks, there are no details in the public record contradicting the ransomware theory.

It is therefore reasonable to conclude the distribution of attack types in the “Unknown” category is similar to the distribution of known attacks, the majority of which are ransomware. In the remainder of this report, we dive deeper into these numbers, looking at what they mean for industrial defenses.

*A clear majority of cyber attacks with physical consequences are the result of ransomware criminal groups.*

**Summary**: Attacks that meet our inclusion criteria are down 25% in 2025 over 2024. Most of these breaches, as in previous years, are ransomware. It is reasonable to expect that even most of the “unknown” threat actor attacks are ransomware. That said, hacktivist and nation-state attacks that deliberately bring about physical consequences increased in 2025 over 2024, despite the overall breach reduction.

---

## Nation States & Hacktivists

![Nation-state and hacktivist attacks doubled in 2025]

Nation-state and hacktivist attacks doubled in 2025 over 2024, with 5 of the 14 attacks clearly linked to the kinetic conflict which is the Russian invasion of Ukraine. This report tracks hacktivists and nation states together, because unlike many ransomware criminals, both hacktivists and nation states deliberately try to bring about physical consequences. In addition, distinguishing between hacktivists and nation states has become difficult. In principle:
- **Hacktivists** – are amateurs. Hacktivists are not paid to carry out attacks, nor do they profit financially from such attacks. Hacktivists thus generally have no money to buy, nor the organization nor infrastructure needed to build their own sophisticated tools, and again, have no organization that can coordinate the efforts of large numbers of attackers.
- **Nation States** – are professional attackers, employed by armies, intelligence agencies and other government agencies. These adversaries generally have the money to buy powerful tools, have development teams able to create their own powerful attack tools, and have a strict organizational structure able to coordinate the activities of large numbers of attackers.

These distinctions have blurred in recent years. Increasingly, hacktivist groups with limited organizations or budgets have at least the blessing, if not other support from nation states, when those hacktivists act to support nation-state goals and objectives in a physical/kinetic conflict.

**Significant breaches by hacktivists and nation states in 2025 included:**
- **Iran’s air defenses** – an American military cyber attack prevented Iran from launching surface-to-air missiles when American warplanes entered Iranian airspace, as part of a mission to bomb nuclear weapons development sites.
- **Russia’s Mercury / VetIS / Saturn systems** – for tracking the movement of animal products for human consumption were twice crippled by DDoS attacks. Some Russian meat-packing plants that needed these raw products to continue receiving meat products had automated their operations to the degree that a manual fall-back was impossible. Processing animal products stopped at many Russian plants for the multi-day duration of the attack.
- **Drones** – could not be converted by the Russian military from consumer firmware to military firmware for use in the invasion of Ukraine for several days because a Ukrainian cyber attack impaired the computers used to reprogram the drones at over 400 military sites.
- **MSC Antonia** – a container ship, ran aground in the Red Sea due to nation state GPS jamming.

**Recommendation (1)**: When nation-state attacks on a facility are credible threats, from nation-state-backed hacktivists to more sophisticated and well-resourced adversaries, defenders should include a large margin for error in the strength of defensive capabilities, because nation states are almost certainly more capable than their historic attacks indicate.

**Summary**: Nation-state and hacktivist attacks that caused physical consequences doubled in 2025. Victims included Iranian air defense, Russian civilian infrastructure, Russian military infrastructure, as well as shipping infrastructure. Given that nation-state adversaries try to be efficient, we should expect them to use the least costly attack tools in their arsenal that will achieve each mission objective. Recommendation summary:
1. Defenders should include a large margin for error when estimating nation-state adversary attack capabilities.

*Nation states can be cost conscious, using as little of their attack capabilities as needed to achieve a specific mission objective – be confident they have materially greater capabilities in reserve than they have yet revealed in public.*

---

## Geographies and Industries

Historically, the USA, Germany and Canada have rotated through the “top 3” victim geographies. In part this is due to these regions and economies being heavily automated and comparatively wealthy, thus hosting more targets and more lucrative targets for ransomware attacks. In part it is due to these nations serving as head offices of industrial businesses – when cyber attacks target multiple geographies, this report records the impacted geography as the country hosting the head office for the affected business.

![Impacted Industries]

In Figure (5) we see that in 2025, discrete manufacturing and transportation were tied.

---

-- | --- | ------------- | --- | ---- | --------------- | --- | --- | ------------ | --- |
USA
|        |     |     |     |     |     |     |     | for the most    | -affected           |              |  industries |             | . In a sense    |       |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | --------------- | ------------------- | ------------ | ----------- | ----------- | --------------- | ----- | --- |
|        |     |     |     |     |     |     |     | however,        |  this is a misnomer |              |             | . We define |                 | :     |     |
|        |     |     |     |     |     |     |     | • Discrete      |   manufacturing     |              |             |             |   –  assembling |       |     |
| France |     |     |     |     |     |     |     | small           |  widgets            |  into larger |             |             |  products,      |  such |     |
|        |     |     |     |     |     |     |     | as  automobiles |                     |              |   and       |   laptop    |   computers,    |       |     |
Norway
|     |     |     |     |     |     | Germany |     | and |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
UK
|     |     |     |     |     |     |     |     | • Process |     | industries |     |     | –  production |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | --- | --- | ------------- | --- | --- |
Japan
|     |     |        |     |     |        |     |     | processes  |              | where |   at  | some |   point     |   in    | its  |
| --- | --- | ------ | --- | --- | ------ | --- | --- | ---------- | ------------ | ----- | ----- | ---- | ----------- | ------- | ---- |
|     |     | Canada |     |     | Russia |     |     |            |              |       |       |      |             |         |      |
|     |     |        |     |     |        |     |     | lifecycle, |  the product |       |       |  can |  be modeled |         |  as  |
|     |     |        |     |     |        |     |     | a  fluid,  | such         |       | as    | oil  | refining,   |   water |      |
Figure 4: Impacted Geographies
|     |     |     |     |     |     |     |     | treatment, |     |   and            |   –  stretching |     |              | the  point |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------------- | --------------- | --- | ------------ | ---------- | --- |
|     |     |     |     |     |     |     |     | somewhat   |     |   –  electricity |                 |     | distribution |   and      |     |
In 2025 , the USA and  Germany  were  #1 and   printing  (turning  large  continuous  sheets
#2 targets,  which  is not surprising . This year,   of paper  into books  and  magazines) .
| for the first time however, |        |     |           |  Russia |     |  placed   |  in  |     |     |     |     |     |     |     |     |
| --------------------------- | ------ | --- | --------- | ------- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| the  top                    | three, |     | primarily |   due   | to  | Ukrainian |      |     |     |     |     |     |     |     |     |
nation -state  and  hacktivist  attacks . All automated industrial
operations in all geographies are
| The  | “other”  | category |     |   in  | the  | figure |   is  |     |     |     |     |     |     |     |     |
| ---- | -------- | -------- | --- | ----- | ---- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
potential targets and should
| important |  as well – “other” includes |     |     |     |     |  all the  |     |     |     |     |     |     |     |     |     |
| --------- | --------------------------- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
deploy defensive measures
| nations |  that |  suffered |  only a single |     |     |  industrial |     |     |     |     |     |     |     |     |     |
| ------- | ----- | --------- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
proportional to credible threats
| outage |  in the public |     |  record |     |  in 2025. In total, |     |     |     |     |     |     |     |     |     |     |
| ------ | -------------- | --- | ------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
21 nations  are represented  in the data  set,  and credible consequences.
| both     | developed |         |   /      | heavily |   industrialized |     |     |                |           |                   |        |     |            |            |      |
| -------- | --------- | ------- | -------- | ------- | ---------------- | --- | --- | -------------- | --------- | ----------------- | ------ | --- | ---------- | ---------- | ---- |
| nations, |  and      |  poorer |  nations |         | .                |     |     |                |           |                   |        |     |            |            |      |
|          |           |         |          |         |                  |     |     | Transportation |           |   is              | widely |     | considered |            |   a  |
|          |           |         |          |         |                  |     |     | process        |  industry |  as well, because |        |     |            |  in a real |      |
Essentially every automated  sense  what  we “put into the pipeline,”  such
industrial operation can be a  as people  boarding  a train or aircraft,  had
|                 |     |     |                    |     |     |     |     | better                 | “come |   out  | of  the    | pipeline” |          |   on  | the  |
| --------------- | --- | --- | ------------------ | --- | --- | --- | --- | ---------------------- | ----- | ------ | ---------- | --------- | -------- | ----- | ---- |
| target of cyber |     |     | -sabotage attacks  |     |     |     |     |                        |       |        |            |           |          |       |      |
|                 |     |     |                    |     |     |     |     | other  end, or we have |       |        |  a serious |           |  problem | .     |      |
that impair physical operations.

2026 OT Cyber Threat Report
9

That   discrete   manufacturing   tied  for  first  Recommendation   (2):  All  automated
place   is  a  somewhat   misleading,   because   industrial  operations  in all geographies  are
discrete   manufacturing   is  no  more   one  potential   targets   and   should   deploy
industry  than  is process  manufacturing . We  defensive  measures  proportional  to credible
produce   large   trucks   very  differently   than   threats  and  credible  consequences .
| we produce         |        |  shoes      |  or plastic    |                |  children’s |             |  toys .  |              |                 |               |          |               |              |            |     |
| ------------------ | ------ | ----------- | -------------- | -------------- | ----------- | ----------- | -------- | ------------ | --------------- | ------------- | -------- | ------------- | ------------ | ---------- | --- |
|                    |        |             |                |                |             |             |          | Summary      | : The top three |               |          |  victim       |  geographies |            |     |
| All the process    |        |  industries |                |  in the figure |             |  added      |          |              |                 |               |          |               |              |            |     |
|                    |        |             |                |                |             |             |          | in 2025 were |                 |  USA, Germany |          |  and          |  Russia      |  – the     |     |
| together           |   are  | a           | much           | larger         |   set       | of  victims |          |              |                 |               |          |               |              |            |     |
|                    |        |             |                |                |             |             |          | latter       | primarily       |               | due      | to  Ukrainian |              | hacktivist |     |
| than  the discrete |        |             |  manufacturing |                |  fraction   |             | .        |              |                 |               |          |               |              |            |     |
|                    |        |             |                |                |             |             |          | and  nation  | -state          |               |  attacks | . The single  |              |  biggest   |     |
Critical   infrastructures   were   impacted   as  industry   vertical   was   discrete
well, for a total  of 7 breaches  (12%) across   manufacturing .  Critical   infrastructures
Oil  &  Gas,   Water   &  Wastewater,   Electric   breached   with  physical   consequences
Power   and   Metals   &  Mining .  This  is  in  included  Oil & Gas,  Water  Systems,  Power,
addition   to  the  14  breaches   (25%)  in  Metals   &  Mining,  and   Pharmaceutical
transportation,   many   of  which   counted   as  Manufacturing . Recommendations  summary :
| critical      |   infrastructure |              |     | outages,   |   including |       |   a       |                    |         |           |      |               |               |     |     |
| ------------- | ---------------- | ------------ | --- | ---------- | ----------- | ----- | --------- | ------------------ | ------- | --------- | ---- | ------------- | ------------- | --- | --- |
|               |                  |              |     |            |             |       |           | 2. All geographies |         |           |  and |  industries   |  are at risk  |     |     |
| ship  running |                  |   aground,   |     |   hundreds |             |   of  | flights   |                    |         |           |      |               |               |     |     |
|               |                  |              |     |            |             |       |           | and                |  should |  deploy   |      |  reasonable   |  defenses     |     |     |
| cancelled     |                  | or  delayed, |     |   and      |   thousands |       |   of      |                    |         |           |      |               |               |     |     |
|               |                  |              |     |            |             |       |           | to prevent         |         |  credible |      |  consequences |               | .   |     |
| trucks        |  idled           |  for days    | .   |            |             |       |           |                    |         |           |      |               |               |     |     |
How Operations Were Impacted
•
In past  years,  this report  documented  how   Supply  chain  – an operation  – most  often
cyber  attacks  affected  physical  operations .  in  manufacturing   –  had   to  shut   down,
In  2025,  as  Figure (6)  illustrates,   65%  of  because   a  cyber   attack   impaired   the
public   incident   reports   did  not  provide   supply   of  critical   components,   or  the
enough   detail   to  conclude   how  the  cyber   attack   shut   down   so  many   of  the
attack   impaired   physical   operations .  operation’s   customers   that   production
Historically,   there   were   four  ways   cyber   could   not  continue   until  customer
| attacks |  caused    |  physical |      |  consequences |       |          | :   | demand |  returned |     | .   |     |     |     |     |
| ------- | ---------- | --------- | ---- | ------------- | ----- | -------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- |
| • OT    | compromise |           |   –  | the           | cyber |   attack |     |        |           |     |     |     |     |     |     |
Reason for Physical Consequence
| compromised, |     |       |   mis-operated, |     |            | rendered |        |     |     |     |     |     |     |     |     |
| ------------ | --- | ----- | --------------- | --- | ---------- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| inoperable   |     |   or  | otherwise       |     |   impaired |          | OT  /  |     |     |     |     |     |     |     |     |
Abundance of Caution
| industrial |     |  automation |     |  cyber |  assets, |     |     |     |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | ------ | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
OT Compromise
| • Abundance |             |   of       | caution |           | –  safety   | -critical |          |     |     |     |     |     |     |         |     |
| ----------- | ----------- | ---------- | ------- | --------- | ----------- | --------- | -------- | --- | --- | --- | --- | --- | --- | ------- | --- |
| physical    |  operations |            |  were   |           |  shut  down |           |  as a    |     |     |     |     |     |     |         |     |
| preventive  |             |   measure, |         |   because |             | the       | victim   |     |     |     |     |     |     | Unknown |     |
IT Dependency
| organization |              |  did not trust |               |              |  operating |          |  those   |     |     |     |     |     |     |     |     |
| ------------ | ------------ | -------------- | ------------- | ------------ | ---------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
| assets       |   while      |                | a  cyber      |              | attack     |   was    |   in     |     |     |     |     |     |     |     |     |
| progress,    |              |   even         |   if  there   |              | was        |   not    | (yet)    |     |     |     |     |     |     |     |     |
| evidence     |              |  of the attack |               |  propagating |            |          |  into    |     |     |     |     |     |     |     |     |
| industrial   |              |  automation    |               |  equipment,  |            |          |          |     |     |     |     |     |     |     |     |
| • IT         | dependencies |                |               | –            | one        | or       | more     |     |     |     |     |     |     |     |     |
| compromised  |              |                | IT  computers |              |   or       | services |          |     |     |     |     |     |     |     |     |
were   essential   to  physical   operations,   Figure  6: How cyber attacks
impacted physical operations
| and   |   those |   assets        |     | were   | impaired |                        | by  a  |     |     |     |     |     |     |     |     |
| ----- | ------- | --------------- | --- | ------ | -------- | ---------------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| cyber |  attack |  on IT systems, |     |        |  or      |                        |        |     |     |     |     |     |     |     |     |
|       |         |                 |     |        | 2026     | OT Cyber Threat Report |        |     |     |     |     |     |     |     |     |
10

As a result, the research team has stopped
There are four ways ransomware tracking and reporting on the reason the
affects physical operations: direct cyber attack caused the physical
consequence – the data is simply not
compromise of OT automation,
available for 2025.
“abundance of caution ” shutdowns,
OT dependencies on IT systems Recommendation (3): To prevent cyber -
crippled in an IT ransomware sabotage attack information from entering
OT networks, strengthen the security at
attack, and external supply chain
network connections – see Section
dependencies – where ransomware
Defensive Developments . To prevent
shuts down a key supplier, or key
“abundance of caution” shutdowns, increase
customer of a n industrial the strength of security at the IT/OT
operation. interface to be confident of operating
safety -critical physical processes even
when IT networks are dealing with a
Historically, the breakdown between these
sophisticated compromise . To prevent
causes of physical outages was roughly 30%
“dependency” shutdowns, understand and
/ 30% / 30% / 10%, but the available data
address OT dependencies on IT systems and
from 2025 is neither detailed nor
services in cybersecurity planning . For
comprehensive enough to draw useful
examples, see Engineering -Grade OT
conclusions about trends as to how attacks
Security – A manager’s guide .
are affecting physical operations .
Summary : Incident reports are becoming
The majority of public reports of industrial
much less detailed on average . It is no
breaches in 2025 described little more than
longer feasible to report on how cyber
the minimum required by Security and
attacks caused physical consequences –
Exchange Commission 8-K or comparable
the details are not available in the public
filings : victim’s name, attack date, whether
record . Historically, physical consequences
the attack was “material” or not, whether
were caused by “abundance of caution”
“operations” were affected, and whether
shutdowns, OT dependencies on IT systems,
there was confidential information stolen .
direct OT equipment compromise, and
Often the reports did not contain enough supply chain effects . Recommendation
detail to determine even whether affected summary :
“operations” were business operations or
physical / manufacturing / production 3. Increase OT security program strength
operations, much less how those physical to avoid OT targeting and “abundance of
effects came about, what was the initial caution” shutdowns, and analyze and
attack vector, nor how the attack plan for OT dependencies on IT systems .
propagated within the victim’s networks .
2026 OT Cyber Threat Report 11

Noteworthy Incidents & Near Misses
2025 saw  a wide  variety  of kinds  of attacks   vulnerable,  so much  so that  the compromise
and  impacts . In this section  we summarize   of  such   systems   should   be  seen   as
incidents  that  teach  important  lessons . inevitable .  When  important   operations
|                    |              |               |                      |               |             |            |       | depend   |   on         | these       |               | exposed,   |              | distributed |          |
| ------------------ | ------------ | ------------- | -------------------- | ------------- | ----------- | ---------- | ----- | -------- | ------------ | ----------- | ------------- | ---------- | ------------ | ----------- | -------- |
| Jaguar             |  / LandRover |               |  – What appears      |               |             |  to be     |       |          |              |             |               |            |              |             |          |
|                    |              |               |                      |               |             |            |       | systems, |              | especially  |               | systems    |              | owned       |   or     |
| ransomware         |              |  shut         |  down  JLR           |  UK factories |             |            |  for  |          |              |             |               |            |              |             |          |
|                    |              |               |                      |               |             |            |       | managed  |              | by  another |               |   vendor   |              | (ie:        | supply   |
| over a month       |              | . The company |                      |  reported     |             |  direct    |       |          |              |             |               |            |              |             |          |
|                    |              |               |                      |               |             |            |       | chain    | risk),       |   it        | is  important |            |              | to  demand  |          |
| costs  of recovery |              |               |  at USD $258M. Total |               |             |  losses    |       |          |              |             |               |            |              |             |          |
|                    |              |               |                      |               |             |            |       | evidence |   of         | a  rapid    |               | recovery   |   capability |             |   or     |
| for the company    |              |               |  are estimated       |               |  at roughly |            |       |          |              |             |               |            |              |             |          |
|                    |              |               |                      |               |             |            |       | have     | practiced    |             |   procedures  |            |   in         | place       |   for    |
| USD  $1B,          | with         | a             | total                | impact        |   on        | the        | UK    |          |              |             |               |            |              |             |          |
|                    |              |               |                      |               |             |            |       | manual   |   fallbacks  |             |               | to  assure |              |   continued |          |
| economy,           |   including  |               |   Jaguar             | ’s            | suppliers,  |            |   at  |          |              |             |               |            |              |             |          |
|                    |              |               |                      |               |             |            |       | physical |  operations, |             |  even         |  if those  |              |  fall-backs |          |
| USD  $2.5B.        |              | The           | next -most           | -costly       |             |   incident |       |          |              |             |               |            |              |             |          |
|                    |              |               |                      |               |             |            |       | somewhat |  increase    |             |  costs        | .          |              |             |          |
| before             |   JLR        | was           | the  NotPetya        |               |   attack    |   that     |       |          |              |             |               |            |              |             |          |
impaired  many  targets  and  for which  Maerk   United   Natural   Foods   –  A  cyber   attack
Pharmaceutical   won  USD  $1.4B  from   their  widely  thought  to be ransomware  impaired
insurer,  Zurich . order   processing   and   distribution   by  the
|     |     |     |     |     |     |     |     | food    | wholesaler |               |   for   | 30,000  | retailers |              | .  The  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ------------- | ------- | ------- | --------- | ------------ | ------- |
|     |     |     |     |     |     |     |     | company |            | is  estimated |         |   to    | have      |   lost       |   USD   |
|     |     |     |     |     |     |     |     | $400M   | in         | sales,        |   spent |   $25M  |           | in  incident |         |
The Jaguar / LandRover incident
|     |     |     |     |     |     |     |     | mitigation |  costs |     |  and  lost |  $160M overall |     |     |  due  |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | --- | ---------- | -------------- | --- | --- | ----- |
was the most expensive physical
|     |     |     |     |     |     |     |     | to  the  | event, |   reporting |     |   a  | net  loss |   of  | over  |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ----------- | --- | ---- | --------- | ----- | ----- |
consequence of a cyber attack in  $50M  on  the  quarter .  This,  again,   is  an
2025 (USD $2.5B), comparable to  example  of a very expensive  breach .
the NotPetya impact on Maerk
|     |     |     |     |     |     |     |     | Ships  ran |  aground |     |  – The containership |     |     |     |  MSC   |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------- | --- | -------------------- | --- | --- | --- | ------ |
Pharmaceutical in 2017 (USD $1.4B)
|     |     |     |     |     |     |     |     | Antonia |  ran aground |     |  in the Red Sea, |     |     |  and |  the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ---------------- | --- | --- | ---- | ----- |
and the Stuxnet attack on Iran’s  bulker  Meghna  Princess  ran up on rocks  near
nuclear weapons program in 2010
|     |     |     |     |     |     |     |     | the  Russian |     |   port |   of  | Ust-Luga |   (occurred |     |   in  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------ | ----- | -------- | ----------- | --- | ----- |
(USD $2 -3B) 2024  but  was   disclosed   in  2025 )  –  both
|     |     |     |     |     |     |     |     | groundings     |     |  due to position |         |  system |       |  spoofing | .       |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ---------------- | ------- | ------- | ----- | --------- | ------- |
|     |     |     |     |     |     |     |     | Recommendation |     |                  |   (6):  |         | GPS   | and       | other   |
Recommendation   (4):  It  is  reasonable   to  position  system  jamming  is commonplace  in
expect  that  JLR  executives  are wishing  they   conflict   zones,   including   Russian   waters
had  deployed  a stronger  security  program   adjoining   Europe,   throughout   Ukraine,   and
to (a)  prevent  this kind of consequence,  or  throughout   the  Red  Sea   and   surrounding
(b)   dramatically   speed   up  recovery   from   areas .  Vessels,   aircraft   and   others
this  kind  of  attack,   or  (c)   both   of  the  navigating   these   areas   should   be  aware
|                |     |         |          |     |      |           |     | that   | positioning |     |   information |     |     |   is  | often   |
| -------------- | --- | ------- | -------- | --- | ---- | --------- | --- | ------ | ----------- | --- | ------------- | --- | --- | ----- | ------- |
| aforementioned |     | . Cyber |  attacks |     |  can |  be very  |     |        |             |     |               |     |     |       |         |
expensive .  Owners   and   operators   should   deliberately   inaccurate   and   should   have
|        |              |     |           |           |     |       |     | compensating |     |  measures |     |  and |  practiced |     |  fall- |
| ------ | ------------ | --- | --------- | --------- | --- | ----- | --- | ------------ | --- | --------- | --- | ---- | ---------- | --- | ------ |
| deploy |  very strong |     |  security |  programs |     |  when |     |              |     |           |     |      |            |     |        |
the cost  of outages  can  be unacceptable . backs  in place .
Collins  Aerospace  – Ransomware  crippled   More  generally,   when   industrial   /  physical
|              |     |           |          |     |        |        |     | operations |     |  rely on external |     |     |  inputs, |  we must |     |
| ------------ | --- | --------- | -------- | --- | ------ | ------ | --- | ---------- | --- | ----------------- | --- | --- | -------- | -------- | --- |
| the  Collins |     | Aerospace |   vMUSE  |     | system |   that |     |            |     |                   |     |     |          |          |     |
many  airports  use at check -in counters  and   anticipate   the  failure   or  spoofing   of  those
|             |              |     |           |     |              |     |      | inputs | . For example |     |  – again |     |  in the maritime |     |     |
| ----------- | ------------ | --- | --------- | --- | ------------ | --- | ---- | ------ | ------------- | --- | -------- | --- | ---------------- | --- | --- |
| gates  used |  by multiple |     |  airlines |     | . The attack |     |  is  |        |               |     |          |     |                  |     |     |
said   to  have   encrypted   over  1000  space  – a 15-year -old hacker  gained  access
|           |              |     |         |     |          |         |     | to an Italian |     |  system |  that |  establishes |     |     |  routes   |
| --------- | ------------ | --- | ------- | --- | -------- | ------- | --- | ------------- | --- | ------- | ----- | ------------ | --- | --- | --------- |
| computers | . The outage |     |  caused |     |  flights |  to be  |     |               |     |         |       |              |     |     |           |
cancelled   and   delayed   for  as  much   as  16  for ships  in the Mediterranean  Sea,  changed
|               |     |           |     |     |     |     |     | a number |  of ships |         | ’ courses, |      |  and  |  took |  those   |
| ------------- | --- | --------- | --- | --- | --- | --- | --- | -------- | --------- | ------- | ---------- | ---- | ----- | ----- | -------- |
| days  at some |     |  airports | .   |     |     |     |     |          |           |         |            |      |       |       |          |
|               |     |           |     |     |     |     |     | ships    | off       | course, |   with     | some |   of  | the   | ships    |
Recommendation   (5):  Highly   distributed   being  oil tankers .
| and   | cloud -based |     |   systems |     |   are  | highly |     |     |     |     |     |     |     |     |     |
| ----- | ------------ | --- | --------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
2026 OT Cyber Threat Report
12

Hacktivists  – opened  floodgates  at a dam   exposed   OT  equipment .  Recommendation
| in  Norway     |   and     |   stopped         |             | production     |             |   at  a  | summary    | :         |              |              |            |               |            |        |
| -------------- | --------- | ----------------- | ----------- | -------------- | ----------- | -------- | ---------- | --------- | ------------ | ------------ | ---------- | ------------- | ---------- | ------ |
| small  hydro   | -power    |  plant            |  in Poland, |                |  both       |  by      |            |           |              |              |            |               |            |        |
|                |           |                   |             |                |             |          | 4. When    | credible  |              | consequences |            |               | are  very  |        |
| accessing      |  Internet | -exposed          |             |  elements      |  of the     |          |            |           |              |              |            |               |            |        |
|                |           |                   |             |                |             |          | expensive, |           |   deploy     |              | very       | strong        |            | OT     |
| respective     |  control  |  systems          |             | .              |             |          |            |           |              |              |            |               |            |        |
|                |           |                   |             |                |             |          | security   |  programs |              | .            |            |               |            |        |
| Recommendation |           |  (7): Anyone      |             |  with Internet |             | -        |            |           |              |              |            |               |            |        |
|                |           |                   |             |                |             |          | 5. For     | highly    |   vulnerable |              |   systems, |               |   such     |   as   |
| exposed        |  elements |  of their control |             |                |  systems    |          |            |           |              |              |            |               |            |        |
|                |           |                   |             |                |             |          | cloud      | -based    |              | or           | highly     |   distributed |            |        |
| should         |   sever   |                   | those       |                | connections |          |            |           |              |              |            |               |            |        |
immediately,  on an emergency  basis . systems,   design   for  rapid   recovery   and
|          |              |         |              |                 |         |      | to control    |     |  consequences  |     | .    |          |     |      |
| -------- | ------------ | ------- | ------------ | --------------- | ------- | ---- | ------------- | --- | -------------- | --- | ---- | -------- | --- | ---- |
| Summary  | : The Jaguar |         |  / LandRover |                 |  breach |  is  |               |     |                |     |      |          |     |      |
|          |              |         |              |                 |         |      | 6. Anticipate |     |  GPS  spoofing |     |  and |  jamming |     |  in  |
| one  of  | the          | top  3  | most         |   consequential |         |      |               |     |                |     |      |          |     |      |
breaches   in  all  OT  security   history .  The  conflict   zones   and   more   generally,
|            |              |         |                 |        |           |           | design      |  systems  |          |  to be deeply |                |  suspicious |        |     |
| ---------- | ------------ | ------- | --------------- | ------ | --------- | --------- | ----------- | --------- | -------- | ------------- | -------------- | ----------- | ------ | --- |
| Collins    |  Aerospace   |  breach |  is an example  |        |           |  of       |             |           |          |               |                |             |        |     |
|            |              |         |                 |        |           |           | of external |           |  inputs  |  – all such   |                |  inputs     |  are   |     |
| physical   |   operations |         | depending       |        |   on      | very      |             |           |          |               |                |             |        |     |
|            |              |         |                 |        |           |           | more        |   likely  | to       | be            | compromised    |             |   than |     |
| vulnerable |   designs    | .       | The             | United |   Natural |           |             |           |          |               |                |             |        |     |
|            |              |         |                 |        |           |           | internal    |  data     |  sources |               |  and  services |             | .      |     |
| Foods      |  breach  was |  also   |  very expensive |        |           | . Ships   |             |           |          |               |                |             |        |     |
ran aground  because  of GPS  jamming  and   7. Disconnect   all  OT  assets   from  the
| spoofing | .  Hacktivists |     |   interfered |        |   with     | small   |          |                            |     |     |     |     |        |     |
| -------- | -------------- | --- | ------------ | ------ | ---------- | ------- | -------- | -------------------------- | --- | --- | --- | --- | ------ | --- |
|          |                |     |              |        |            |         | Internet |  – do this on an emergency |     |     |     |     |  basis | .   |
| dams     | and   power    |     | plants       |   from |   Internet | -       |          |                            |     |     |     |     |        |     |
Polish Energy Sector Attack
The  Polish   CERT   reports   that   in  December   The  attackers   gained   access   to  the
2025, Russian  attackers  broke  into over 30  networks  in the months  that  preceded  the
small  Polish  wind and  solar  generators . The  attack   on  the  generators   and   used   that
attack  also  impacted  control  equipment  in  access   on  December   29,  2025 .  In  post -
an  un-named   private   manufacturing   attack  forensics,  it was  determined  that  at
business  and  a combined  heat   and  power   the time of the Dec  29 attack,  the attackers
(CHP)  plant  supplying  heat  to nearly  a half   had  administrative  privileges  on the firewalls
million  customers  in Poland . The result  was  a  deployed  at each  of the affected  sites . The
near   miss   and   was   not  counted   in  this  attackers   used   the  privileges   they   had
report ’s  statistics .  Power   continued   to  be  acquired   to  attack   monitoring   and   control
generated  and  heat  continued  to flow,  but  equipment   at  each   of  the  DER  sites .  The
the  attackers   erased   the  firmware   in  an  attack  affected  many  kinds  of devices :
| undisclosed |  number |  of automation |     |     |  devices,   |     |             |          |         |         |        |         |           |      |
| ----------- | ------- | -------------- | --- | --- | ----------- | --- | ----------- | -------- | ------- | ------- | ------ | ------- | --------- | ---- |
|             |         |                |     |     |             |     | • Hitachi   |   RTU560 |         |   –     | loaded |         | corrupted |      |
| rendering   |   the   | devices        |     |     | permanently |     |             |          |         |         |        |         |           |      |
|             |         |                |     |     |             |     | firmware,   |          | sending |   these |        | devices |   into    | a    |
| unbootable  | .       |                |     |     |             |     |             |          |         |         |        |         |           |      |
|             |         |                |     |     |             |     | reboot      |  loop,   |         |         |        |         |           |      |
|             |         |                |     |     |             |     | • Mikronika |          |   RTUs  |   –     | logged |         | into      | the  |
Russia’s attack on Polish
|     |     |     |     |     |     |     | underlying |     |   Linux  | operating |     |   system |   and |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | --------- | --- | -------- | ----- | --- |
distributed generation was a near
|                |                            |                     |     |     |     |     | attempted   |     |  to remove |     |  all files in the Linux  |         |       |      |
| -------------- | -------------------------- | ------------------- | --- | --- | --- | --- | ----------- | --- | ---------- | --- | ------------------------ | ------- | ----- | ---- |
| miss           | – power continued to flow  |                     |     |     |     |     |             |     |            |     |                          |         |       |      |
|                |                            |                     |     |     |     |     | filesystem, |     |   causing  |     | the                      | failure |   of  | the  |
| uninterrupted  |                            | – but demonstrated  |     |     |     |     |             |     |            |     |                          |         |       |      |
devices,
that critical infrastructures are in
| scope for Russia |     | -backed nation |     |     |     | -   |     |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
state attacks.
2026 OT Cyber Threat Report
13

• Hitachi   Relion   650   Protection   and   Polish   CERT’s   report   to  search   their  own
Control  Relays  – logged  into the devices   networks   for  evidence   of  a  Russian
via  a  default   FTP  account   and   deleted   adversary’s  long -term  presence,  and  should
essential  files, preventing  the device  from   adopt   the  most   recent,   most   powerful
restarting, innovations   in  OT  cybersecurity   to  bolster
|             |           |                |             |     |           |           |        | those     | sites’        |   defenses |   –  see |   the  | section |     |
| ----------- | --------- | -------------- | ----------- | --- | --------- | --------- | ------ | --------- | ------------- | ---------- | -------- | ------ | ------- | --- |
| • Mikronika |           |  HMI Computers |             |     |  – logged |           |  into  |           |               |            |          |        |         |     |
|             |           |                |             |     |           |           |        | Defensive |  Developments |            |  below   | .      |         |     |
| these       |   Windows |                |   computers |     |           | via  RDP  | and    |           |               |            |          |        |         |     |
ran a “wiper” program  to first corrupt  non- The attack  is noteworthy  in a third respect  –
operating -system   files   and   in  a  second   industrial   firmware   was   corrupted   and
pass,   delete   all  files   that   could   be  erased,  and  devices  were  sent  into reboot
| deleted      | .      |         |           |             |         |             |             | loops . The CERT’s |        |             |  report  does    |  not indicate |              |       |
| ------------ | ------ | ------- | --------- | ----------- | ------- | ----------- | ----------- | ------------------ | ------ | ----------- | ---------------- | ------------- | ------------ | ----- |
|              |        |         |           |             |         |             |             | whether            |   the  | industrial  |                  | equipment     |   was        |       |
| • Moxa       |  NPort |  6xxx   |  Serial   |             |  Device |  Servers    |  –          |                    |        |             |                  |               |              |       |
|              |        |         |           |             |         |             |             | rendered           |        | permanently |                  | unbootable    |              | /     |
| logged       |        | into    | the       | devices     |         | with        | default     |                    |        |             |                  |               |              |       |
|              |        |         |           |             |         |             |             | “bricked,”         |   or   | if  there   |   still  existed |               |   a  way     |   to  |
| credentials, |        |  reset  |  them     |  to factory |         |             |  default,   |                    |        |             |                  |               |              |       |
|              |        |         |           |             |         |             |             | restore            |   good |   firmware  |                  | to  the       | devices      |       |
| changed      |        |   the   | password, |             |   and   |             | set  the    |                    |        |             |                  |               |              |       |
|              |        |         |           |             |         |             |             | somehow            | .      | The  risk   | of  “bricking”   |               |   industrial |       |
| device       |   IP   | address |           |   to        | an      | unreachable |             |                    |        |             |                  |               |              |       |
devices  is real.
| value      | .              |     |        |             |        |           |            |                        |     |     |               |     |     |     |
| ---------- | -------------- | --- | ------ | ----------- | ------ | --------- | ---------- | ---------------------- | --- | --- | ------------- | --- | --- | --- |
| The attack |  is noteworthy |     |        |  in several |        |  respects | .          |                        |     |     |               |     |     |     |
|            |                |     |        |             |        |           |            | If an attack “bricks”  |     |     | the majority  |     |     |     |
| This       | was            | an  | attack |   on        | Polish |           | critical   |                        |     |     |               |     |     |     |
infrastructure,  even  if the infrastructure  was   of a certain model of PLC’s or
on the small  side . The Polish  CERT  concluded   other automation equipment at
| that   | the  | sum   | of  | generation |     |   at  | all  30  |     |     |     |     |     |     |     |
| ------ | ---- | ----- | --- | ---------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
a site, can replacement
| generation |     | sites |   was |   not  | large |   enough |   to  |     |     |     |     |     |     |     |
| ---------- | --- | ----- | ----- | ------ | ----- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
equipment still be purchased from
| have   | an  impact |     |   on  | the  Polish |     |   power |   grid,  |     |     |     |     |     |     |     |
| ------ | ---------- | --- | ----- | ----------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
reliable sources, or must
| even  if all the sites’ |     |     |  power |     |  generation |     |  were   |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ------ | --- | ----------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
the site carry out an emergency
| taken  down |     |  simultaneously |     |     | . None |  the less, |     |     |     |     |     |     |     |     |
| ----------- | --- | --------------- | --- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
upgrade, with associated
| this was |  an attack |     |  on industrial |     |     |  automation |     |     |     |     |     |     |     |     |
| -------- | ---------- | --- | -------------- | --- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
in  the  Polish   electric   sector .  There   is  also   development, testing, certification
evidence  the adversaries  had  a presence  in  and deployment costs?
| the Polish                |  power           |     |  networks |            |  for some       |             |  months   |     |     |     |     |     |     |     |
| ------------------------- | ---------------- | --- | --------- | ---------- | --------------- | ----------- | --------- | --- | --- | --- | --- | --- | --- | --- |
| before                    |  the attack      |     |  was      |  triggered |                 | .           |           |     |     |     |     |     |     |     |
| Recommendation            |                  |     |   (8):    | At         | least           |   Polish    |   and     |     |     |     |     |     |     |     |
| more  likely all European |                  |     |           |  critical  |  infrastructure |             |           |     |     |     |     |     |     |     |
| is in scope               |  for nation      |     |           | -state     |  attacks        |  from       |  at       |     |     |     |     |     |     |     |
| least                     | Russian          |     | threat    |   actors   |                 | .  European |           |     |     |     |     |     |     |     |
| critical                  |   infrastructure |     |           |   sites    |   should        |             | use  the  |     |     |     |     |     |     |     |
2026 OT Cyber Threat Report
14

Many  industrial  operations  use devices  that   automation   to  use  only  still-supported,
are  so  old,  the  manufacturer   is  no  longer   easily   replaced   equipment,   or  deploy
able  to produce  the devices,  nor sell them .  defenses  strong  enough  defeat  with a high
Most   industrial   sites,   as  a  result,   have   a  degree   of  confidence   all  credible   threats
modest  supply  of spare  devices  in stock,  to   and  attacks  able  to bring  about  large -scale
| replace        |   units            | that       |   fail                      | in         | the          | course       |   of      | “bricking          | .”             |            |             |                 |                  |         |
| -------------- | ------------------ | ---------- | --------------------------- | ---------- | ------------ | ------------ | --------- | ------------------ | -------------- | ---------- | ----------- | --------------- | ---------------- | ------- |
| normal         |  use. If most      |            |  or all of one kind of old  |            |              |              |           |                    |                |            |             |                 |                  |         |
|                |                    |            |                             |            |              |              |           | Summary            | : The Polish   |            |  DER attack |                 |  was  a near     |         |
| device         |  in an industrial  |            |                             |  operation |              |  is bricked, |           |                    |                |            |             |                 |                  |         |
|                |                    |            |                             |            |              |              |           | miss  – the lights |                |  stayed    |             |  on. That       |  said,           |  some   |
| there          | will               | not  be    | enough                      |            |   spares     |   in         | the       |                    |                |            |             |                 |                  |         |
|                |                    |            |                             |            |              |              |           | kinds              |  of automation |            |  equipment  |                 |  were            |  most   |
| organization   |                    |   to       | replace                     |   the      | failed       |   devices,   |           |                    |                |            |             |                 |                  |         |
|                |                    |            |                             |            |              |              |           | likely             | bricked        |   in       | the         | attack,         |   necessitating  |         |
| and   few      | other              |   reliable |                             |   sources  |              |   of  spares | .         |                    |                |            |             |                 |                  |         |
|                |                    |            |                             |            |              |              |           | their              | replacement    |            | .           | Recommendations |                  |         |
| Such   attacks |                    |   risk     | rendering                   |            |   industrial |              |   sites   |                    |                |            |             |                 |                  |         |
|                |                    |            |                             |            |              |              |           | summary            | :              |            |             |                 |                  |         |
| inoperable     |  until engineering |            |                             |            |  teams       |  can         |  carry    |                    |                |            |             |                 |                  |         |
| out            | emergency          |            |   upgrades                  |            | :            | upgrading    |           |                    |                |            |             |                 |                  |         |
|                |                    |            |                             |            |              |              |           | 8. At              | least          |   European |             | critical        |   infrastructure |         |
programming,   configuring,   testing   and   sites  should  use the Polish  CERT’s  report
| commissioning |     |   modern |     |   replacements |     |     |   for  |     |        |      |     |        |          |        |
| ------------- | --- | -------- | --- | -------------- | --- | --- | ------ | --- | ------ | ---- | --- | ------ | -------- | ------ |
|               |     |          |     |                |     |     |        | and |   the  | most |     | recent |   advice |   for  |
the bricked   equipment . This  risks  weeks  or  deterministic   defenses   to  bolster   their
| months      |   of  | downtime  |        |          | for  | production |     |           |     |                 |     |         |             |     |
| ----------- | ----- | --------- | ------ | -------- | ---- | ---------- | --- | --------- | --- | --------------- | --- | ------- | ----------- | --- |
|             |       |           |        |          |      |            |     | defenses  |     | .               |     |         |             |     |
| operations, |       |  not mere |  hours |  or days |      | .          |     |           |     |                 |     |         |             |     |
|             |       |           |        |          |      |            |     | 9. Owners |     |  and  operators |     |  should |  anticipate |     |
Recommendation   (9):  All  owners   and   attacks  that  brick  large  fractions  of their
| operators |     | of  industrial |     |   facilities |     |   that |   use  |             |     |             |     |      |                |     |
| --------- | --- | -------------- | --- | ------------ | --- | ------ | ------ | ----------- | --- | ----------- | --- | ---- | -------------- | --- |
|           |     |                |     |              |     |        |        | out-of-sale |     |   equipment |     |   –  | such   attacks |     |
control   equipment   for  which   like-for-like  risk  months -long   downtime   due  to
| replacements |        |  can     |  no longer |         |  be purchased     |            |     |           |     |           |     |     |     |     |
| ------------ | ------ | -------- | ---------- | ------- | ----------------- | ---------- | --- | --------- | --- | --------- | --- | --- | --- | --- |
|              |        |          |            |         |                   |            |     | emergency |     |  upgrades |     | .   |     |     |
| should       |   take |   action |   to       | address |                   | the  risk  | of  |           |     |           |     |     |     |     |
| large -scale |        |  device  |  “bricking |         | .” Either upgrade |            |     |           |     |           |     |     |     |     |
Broader Attack Trends
Ransomware   attacks   more   FBI Reports of Ransomware Victims
| generally     |   showed   |                |   signs       |   of   | leveling |      |      |     |     |     |     |     |     |     |
| ------------- | ---------- | -------------- | ------------- | ------ | -------- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
| off  or       | decreasing |                |   in          | 2025.  | While    |      | 4000 |     |     |     |     |     |     |     |
| there         | are        | no             | comprehensive |        |          | or   | 3500 |     |     |     |     |     |     |     |
| authoritative |            |   repositories |               |        | of       | all  |      |     |     |     |     |     |     |     |
3000
| cyber   | attacks        |   nor        | all          | ransomware    |       |     |      |     |     |     |     |     |     |     |
| ------- | -------------- | ------------ | ------------ | ------------- | ----- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
| attacks |   in           | 2025,        | there        |   are         | data  |     | 2500 |     |     |     |     |     |     |     |
| points  |  that  suggest |              |  a levelling |               |  off. |     | 2000 |     |     |     |     |     |     |     |
| Figure  | (7)            | for  example |              |   illustrates |       |     | 1500 |     |     |     |     |     |     |     |
| reports |   to           | the  FBI     | of           | ransomware    |       |     |      |     |     |     |     |     |     |     |
1000
| attacks |   from |     | victims |     | in  their  |     |     |     |     |     |     |     |     |     |
| ------- | ------ | --- | ------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
500
| jurisdiction | . The 2025   |     |  data  |     |  has  not  |     |     |     |     |     |     |     |     |     |
| ------------ | ------------ | --- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| yet  been    |   published, |     |   but  | it  | is  clear  |     | 0   |     |     |     |     |     |     |     |
the  number   of  reported   8102 9102 0202 1202 2202 3202 4202
| ransomware |       |   attacks |     |   can |   vary   |     |     |                                                   |     |     |     |     |     |     |
| ---------- | ----- | --------- | --- | ----- | -------- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- |
| upwards    |   or  | downwards |     |   in  | a  given |     |     |                                                   |     |     |     |     |     |     |
|            |       |           |     |       |          |     |     | Figure  7: Ransomware attacks reported to the FBI |     |     |     |     |     |     |
year .
2026 OT Cyber Threat Report
15

The NCC Group tracks alleged ransomware 400
attacks that ransomware criminals
350
themselves publish . The group ’s November
2025 data in Figure (8) shows ransomware 300
attacks were mostly flat from 2024 through
250
2025. While ransomware and other criminals
often over-state their prowess, their impact 200
and their victims, it is worth considering that
150
in aggregate, this unreliable over-statement
is flat year over year, even if individual 100
allegations are suspect .
50
0
2022 2023 2024 2025
Outside of the OT domain, there is
evidence of a leveling -off in 2025 of
ransomware attacks and encrypting
ransomware attacks. Other data points include Coalition
insurance reporting a 3% reduction in
ransomware claims in 2024 over 2023 , and
Cyber Resilience insurance reporting a 53%
1000 reduction in cyber claims in 2025 H1 over
800 2024 H1. The Microsoft Digital Defense
600 Report 2025 does not report how total
400
ransomware attacks in their data set
200
changed year over year, but the report does
show that from July 1, 2024 through June 30,
2025 ransomware attacks reaching the
encryption stage increased only 7%,
compared to a 102% increase in the
preceding 12 months .
That ransomware attacks overall appear to
be flat or declining in 2025, with encrypting
The German BSI also publishes data about
ransomware attacks mostly flat, is a
cyber attacks – Germany requires critical
significant development . All ransomware
infrastructures to report all attacks that
attacks on IT networks risk triggering
could impact critical infrastructures,
“abundance of caution ” OT shutdowns, and
including for example information -stealing
encrypting attacks can either directly impair
attacks, such as an attack that steals all of
OT systems, or impair IT systems essential to
a power utility’s employees ’ personal data .
continuous OT operations .
Adding up the German data for industries
this report tracks, we get Figure (9). The Summary : FBI, BSI and other data suggests
data for each indicated year includes that ransomware attacks, and to an extent
reports from June or July of the previous other attacks on critical infrastructure,
year, to May or June of the indicated year . increased less in 2025 than was the trend in
As is evident in the figure, mandatory previous years . Encrypting ransomware
incident reports increased by 40% and 52% attacks also increased very little. This may
in 2023 and 2024 , respectively, but increased be a proximate cause of reduced attacks
by only 6% in the year ending half -way with physical consequences in 2025.
through 2025.
2026 OT Cyber Threat Report 16
yraunaJ yraurbaF hcraM lirpA yaM
2024 2025
enuJ yluJ tsuguA rebmetpeS rebotcO rebmevoN rebmeceD
Figure 9: BSI KRITIS incident report
counts in industries we track
0
Figure 8: Criminal -reported alleged
ransomware attacks (NCC Group)

| Analysis  |     |     | –  Where Did the Attacks Go? |     |     |     |     |     |     |     |     |     |     |     |     |
| --------- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Given  the hyperbole  that  is commonplace  in  fraction   of  would -be  criminals .  All  these
the  media,   vendor   threat   reports   and   factors  suggest  that  in the absence  of any
sometimes   even   in  government   threat   other  change,  ransomware  activity  will again
reports,  most  readers  expect  the number  of  start  to increase  at near -historic  30-60% per
OT breaches  with physical  consequences  to  annum  rates  in 2026 -2027. Teams  defending
increase  steadily . In this section  we look at  industrial   operations   should   not  rely  on  a
what   happened   in  2025  –  why  were   fewer   prolonged  decline  in cyber  threat  activity,  nor
breaches  reported  than  in 2024? a  prolonged   decline   in  breaches   with
|     |     |     |     |     |     |     |     |     | physical  consequences |     |     | .   |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- |
Hypothesis: Fewer ransomware
attacks mean fewer breaches.
The reasons for ransomware
| In the section |      |  “Broader |               |  Attack |  Trends |              | ” above, |     |                          |     |     |       |         |     |     |
| -------------- | ---- | --------- | ------------- | ------- | ------- | ------------ | -------- | --- | ------------------------ | --- | --- | ----- | ------- | --- | --- |
|                |      |           |               |         |         |              |          |     | attacks leveling out in  |     |     | 2025  | reduce  |     |     |
| there          | are  | strong    |   indications |         |         |   ransomware |          |     |                          |     |     |       |         |     |     |
attacks by constant percentages.
| attacks |  overall |  plateaued |     |  or even |     |  dropped |     |  in  |     |     |     |     |     |     |     |
| ------- | -------- | ---------- | --- | -------- | --- | -------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
2025 over 2024 . Microsoft  data  also  indicates   In the absence of new reasons
encrypting   ransomware   attacks   plateaued .  emerging or percentages changing,
| Reasons |  for this effect |     |     |  include | :   |     |     |     |     |     |     |     |     |     |     |
| ------- | ---------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ransomware attacks are expected
• Ransomware  criminals  no longer  universally   to resume increasing  in  2026 -2027 .
| encrypt  |  their victims |           |     | ’ systems |     |  – a material |        |     |     |     |     |     |     |     |     |
| -------- | -------------- | --------- | --- | --------- | --- | ------------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| fraction |                | of  those |     | criminals |     |   now         | merely |     |     |     |     |     |     |     |     |
steal   data   and   extort   ransoms   for  Hypothesis: Fewer attacks are being
| promises |     |  of not disclosing |     |     |  the data, |     |     |     | reported in public |     |     |     |     |     |     |
| -------- | --- | ------------------ | --- | --- | ---------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- |
• The  global   ransomware   ecosystem re- Given  steadily  increasing  legal  mandates  to
| organized |     |   mid-2025  |     | as  | a  major |     |   provider |     |               |             |            |     |         |       |     |
| --------- | --- | ----------- | --- | --- | -------- | --- | ---------- | --- | ------------- | ----------- | ---------- | --- | ------- | ----- | --- |
|           |     |             |     |     |          |     |            |     | report  cyber |  incidents, |  one might |     |  expect |  that |     |
closed   down   and   other   criminal   groups   a steadily  greater  fraction  of all incidents  is
competed   to  take   the  place   of  that   reported   to  the  public .  There   are  some
| provider, |       |  and |            |     |        |       |      |     | concerns    |  that  this is not the case |           |     | :       |     |     |
| --------- | ----- | ---- | ---------- | --- | ------ | ----- | ---- | --- | ----------- | --------------------------- | --------- | --- | ------- | --- | --- |
| • There   |   is  | some |   evidence |     |   that |   C2  | take | -   | •           |                             |           |     |         |     |     |
|           |       |      |            |     |        |       |      |     | Regulations |                             | requiring |     | reports |     | to  |
downs,   sanctions   and   prosecution   of  government   authorities,   such   as  NERC,
| ransomware |     |     | criminals |     |   is  | somewhat |     |     |            |        |                |     |               |     |     |
| ---------- | --- | --- | --------- | --- | ----- | -------- | --- | --- | ---------- | ------ | -------------- | --- | ------------- | --- | --- |
|            |     |     |           |     |       |          |     |     | KRITIS and |  other |  NIS2-inspired |     |  regulations, |     |     |
reducing   the  population   of  ransomware   assure   reporting   organizations   of
| criminals,  |     |  because |          |  of concern |                |  over being |     |     |            |                  |     |          |      |             |     |
| ----------- | --- | -------- | -------- | ----------- | -------------- | ----------- | --- | --- | ---------- | ---------------- | --- | -------- | ---- | ----------- | --- |
|             |     |          |          |             |                |             |     |     | anonymity  |   –  essentially |     |          | none |   of  these |     |
| apprehended |     | .        |          |             |                |             |     |     | regulatory |   reports        |     |   become |      |   public    |     |
|             |     |          |          |             |                |             |     |     | knowledge  | .                |     |          |      |             |     |
| A somewhat  |     |  clearer |  picture |             |  of ransomware |             |     |     |            |                  |     |          |      |             |     |
trends  should  emerge  in the months  ahead,   • It  is  reasonable   to  believe high-profile
| as  additional |            |   data         |   sets          |             | are            | analyzed   |   and       |       |                  |                   |          |               |                |             |      |
| -------------- | ---------- | -------------- | --------------- | ----------- | -------------- | ---------- | ----------- | ----- | ---------------- | ----------------- | -------- | ------------- | -------------- | ----------- | ---- |
|                |            |                |                 |             |                |            |             |       | prosecutions     |   and             |   fines  |   for         | organizations  |             |      |
| documented     |            | .              |                 |             |                |            |             |       | disclosing       |   incorrect       |          |   information |                |   to        | the  |
|                |            |                |                 |             |                |            |             |       | public           | is  causing       |   legal  |   teams       |                | to  advise  |      |
| Recommendation |            |                |   (10):         |             | Disarray       |            | in          | the   |                  |                   |          |               |                |             |      |
|                |            |                |                 |             |                |            |             |       | disclosing       |  only the minimum |          |               | . The minimum  |             |      |
| ransomware     |            |   criminal     |                 |   ecosystem |                |   is       | likely      | to    |                  |                   |          |               |                |             |      |
|                |            |                |                 |             |                |            |             |       | in most          |  jurisdictions    |  is any  |  information  |                |  that       |      |
| stabilize      |  in 2026   |                |  and  beyond    |             | . The fraction |            |             |  of   |                  |                   |          |               |                |             |      |
|                |            |                |                 |             |                |            |             |       | might  cause     |  a reasonable     |          |  investor     |                |  to buy,    |      |
| criminal       |  groups    |  encrypting    |                 |             |  data          |  is also   |  likely     |       |                  |                   |          |               |                |             |      |
|                |            |                |                 |             |                |            |             |       | sell or assign   |  a value          |          |  to shares    |                | . Incidents |      |
| to stabilize   |            | . Improved     |                 |  law        |  enforcement   |            |  is a       |       |                  |                   |          |               |                |             |      |
|                |            |                |                 |             |                |            |             |       | that   do        | not  meet         |   this   | threshold     |                |   do        | not  |
| deterrent      |  but given |                |  the persistent |             |                |  increases |             |       |                  |                   |          |               |                |             |      |
|                |            |                |                 |             |                |            |             |       | need             | to  be  reported  |          |   and         |   increasingly |             |      |
| in  ransomware |            |                |   attacks       |             | in  the        |            | last   half |       |                  |                   |          |               |                |             |      |
|                |            |                |                 |             |                |            |             |       | appear           |   not to be       | reported |               |  to            | authorities |      |
| decade,        |   it       | is  reasonable |                 |             | to  expect     |            |   that      |   a   |                  |                   |          |               |                |             |      |
|                |            |                |                 |             |                |            |             |       | nor to the press |                   | .        |               |                |             |      |
| consistent     |            | enforcement    |                 |             |   posture      |            |             | will  |                  |                   |          |               |                |             |      |
| consistently   |            |   deter        |   a             | reasonably  |                |            | constant    |       |                  |                   |          |               |                |             |      |
2026 OT Cyber Threat Report
17

• There  are few legal  mandates  for public   attacks   with  material   physical
incident   disclosures   in  authoritarian   consequences   are  much   more   difficult   to
regimes,  nor in kinetic  conflict  zones . It is  hide. The sky is not falling .
| reasonable |           |   to  | expect |   governments |     |          |   in  |                |     |                |     |              |     |     |
| ---------- | --------- | ----- | ------ | ------------- | --- | -------- | ----- | -------------- | --- | -------------- | --- | ------------ | --- | --- |
|            |           |       |        |               |     |          |       | Recommendation |     |  (11): Despite |     |  the decline |     |     |
| these      |   regions |   to  | order  |   victims     |     | to  deny |       |                |     |                |     |              |     |     |
they  were  targets  of a cyber  attack . in  OT  consequences,   the  2025  data   set
|     |     |     |     |     |     |     |     | includes |   consequences |     |   that |   are  | material | .   |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------ | ------ | -------- | --- |
On  the  other   hand,   this  report   tracks   Owners   and   operators   should   continue
breaches   with  physical   consequences .  anticipate   cyber   attacks   that   are  able   to
Significant   physical   consequences   are  bring  about  significant  consequences .
| harder |   to  hide  | than |   stolen |     | information |     |   or  |     |     |     |     |     |     |     |
| ------ | ----------- | ---- | -------- | --- | ----------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
encrypted   IT  systems,   no  matter   what   Hypothesis : Defenses  are  becoming
|                            |           |             |          |     |         |           |      | more               |  capable       | .     |           |               |     |      |
| -------------------------- | --------- | ----------- | -------- | --- | ------- | --------- | ---- | ------------------ | -------------- | ----- | --------- | ------------- | --- | ---- |
| governments                |           |   or  legal |   teams  |     |   order | .  If     | the  |                    |                |       |           |               |     |      |
| lights                     | go  out,  | for         | example, |     | people  |   notice, |      |                    |                |       |           |               |     |      |
|                            |           |             |          |     |         |           |      | It  is  reasonable |                |   to  | believe   | that,   given |     | the  |
| and  very likely the press |           |             |  notices |     | .       |           |      |                    |                |       |           |               |     |      |
|                            |           |             |          |     |         |           |      | constant           |   exhortations |       |   from    |   governments |     |      |
“Back  of the envelope  calculations ” suggest   and   others,   industrial   enterprises   are  on
there   are  not  huge   numbers   of  incidents   average   and   at  least   to  some   degree
being   withheld .  For  example,   in  the  recent   increasing   the  strength   of  their  defenses
SANS  State  of ICS/OT  Security  2025  survey,   over time. There  are few objective  measures
330  respondents   indicated   that   22%  had   of the average  strength  of OT cybersecurity,
suffered   a  “security   incident ”  in  the  world -wide,  however .  While  of  this  year ’s
preceding   12  months,   and   15%  of  those   incidents   betray   woefully   inadequate
resulted   in  an  “engineering   system   defenses   –  hacktivists   exploiting   Internet -
degradation   or  outage ”  (10  respondents   /  facing  OT infrastructure  and  Internet -facing
incidents) . These  ten incidents  were  due to  IT  infrastructure   which   is  essential   to
all causes,  including  insider  error, such  as an  physical  operations,  there  are also  a small
insider  inadvertently  doing  something  on a  number  of breaches  impacting  what  should
computer   in  violation   of  company   policy .  have   been   heavily -defended   OT
This is a small  number,  and  even  this small   infrastructures,   such   as  the  Jaguar   /
number   includes   kinds   of  events   and   LandRover  breach,  and  the attack  that  shut
industries   that   are  out  of  scope   for  this  down   Venezuelan   oil  terminals   for  several
| report | .   |     |     |     |     |     |     | days . |     |     |     |     |     |     |
| ------ | --- | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Furthermore,   our  research   team   interacts   In  addition,   stronger   defenses   only  mean
routinely   with  many   experts   and   incident   fewer   breaches   when   attack   volume   and
responders  in OT security .  There  is  no hint  sophistication   remain   constant .  Attack
| from  that |  community |     |  that |  there |  is a material |     |     |        |                 |     |          |                  |     |     |
| ---------- | ---------- | --- | ----- | ------ | -------------- | --- | --- | ------ | --------------- | --- | -------- | ---------------- | --- | --- |
|            |            |     |       |        |                |     |     | volume |  was  addressed |     |  earlier |  in this section |     |     |
world -wide   conspiracy   that   is  effectively   –  it  appears   to  be  mostly   constant .  As  to
covering   up  “huge ”  numbers   of  incidents   attack   sophistication,   while  there   are  few
with material  physical  consequences . objective  measures  of the capabilities  of all
|     |     |     |     |     |     |     |     | the  world  | ’s        | adversaries,  |   there          |   are  | some |       |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ------------- | ---------------- | ------ | ---- | ----- |
|     |     |     |     |     |     |     |     | indications |           | that   attack |   sophistication |        |      |   is  |
|     |     |     |     |     |     |     |     | holding     |  constant | .             |                  |        |      |       |
Conspiracy theories postulating
| “huge    | ” numbers of unreported high |     |     |     |     | -   |     |     |     |     |     |     |     |     |
| -------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| physical | -consequence attacks are     |     |     |     |     |     |     |     |     |     |     |     |     |     |
not credible.
| Thus,        | there   are  | no          | reasonable     |                |   grounds      |          |   to  |     |     |     |     |     |     |     |
| ------------ | ------------ | ----------- | -------------- | -------------- | -------------- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
| believe      |  there       |  is a large |  body          |                |  of unreported |          |       |     |     |     |     |     |     |     |
| incidents    |   in         | 2025        | with           | material       |                | physical |       |     |     |     |     |     |     |     |
| consequences |              | .  It       | is  reasonable |                |   to           | believe  |       |     |     |     |     |     |     |     |
| the  numbers |              |   in  this  | report         |                | are  somewhat  |          |       |     |     |     |     |     |     |     |
| understated  |              | –  cyber    |   attacks      |                |   with         | minor    |       |     |     |     |     |     |     |     |
| physical     |   effects    |             | might          |   be           | successfully   |          |       |     |     |     |     |     |     |     |
| covered      |   up         | by  victim  |                | organizations, |                |          | but   |     |     |     |     |     |     |     |
2026 OT Cyber Threat Report
18

For  example,   Google/Mandiant   data   in  • AIs are starting  to be used  to automate
Figure   (10)  shows   the  number   of  zero -day   attacks .  For  example,   Promptlock   data
vulnerabilities  exploited  in the wild is largely   exfiltration   malware   appears   to  be  a
constant  since  the turn of the decade . Zero - proof -of-concept  still under  development .
day   exploits   are  used   by  the  most   The  malware   includes   functions   for
sophisticated   of  threat   actors,   including   automatically   generating   new  attack
high-end  ransomware   toolkits   and   nation - code  to evade  anti-virus, deciding  which
state  adversaries . The number  of exploited   data   to  exfiltrate,   and   (not   yet  active)
zero -days   suggests   the  sophistication   of  encrypting   valuable   targets .  Another
high-end attacks  is more  constant  than  not. example :  Anthropic   reported   detecting
|     |     |     |     |     |     |     | and |   defeating |     |   a  | Chinese |     | exfiltration |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | ------- | --- | ------------ | --- |
Zero Days Exploited in the Wild attack   campaign   that   used   Anthropic’s
|     |     |     |     |     |     |     | Claud    |   Code |              | AI  to  | automate    |     |   an  | attack   |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------------ | ------- | ----------- | --- | ----- | -------- |
|     |     |     |     |     |     |     | campaign |        | .  Anthropic |         |   estimates |     |       | the  AI  |
120
|     |     |     |     |     |     |     | carried     |   out  | 80-90%     |     | of         | the  attack |            |   steps,   |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------ | ---------- | --- | ---------- | ----------- | ---------- | ---------- |
| 100 |     |     |     |     |     |     | with humans |        |  providing |     |  strategic |             |  oversight |            |
100
96
|     |     |     |     |     | 90  |     | of the campaign |     |     | .   |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- |
80
78
| 60  |     |     |     |     |     |     | • On  | the  | other |   hand, |     | security |   product |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---- | ----- | ------- | --- | -------- | --------- | --- |
63
|     |     |     |     |     |     |     | vendors |     | also |   use  | LLMs |   to  | develop |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | --- | ---- | ------ | ---- | ----- | ------- | --- |
40
|     |     |     |     |     |     |     | marketing |               |   messages |              |            | to    | encourage  |      |
| --- | --- | --- | --- | --- | --- | --- | --------- | ------------- | ---------- | ------------ | ---------- | ----- | ---------- | ---- |
|     |     |     |     |     |     |     | prospects |               |   to       | deploy       |   stronger |       |   defenses |      |
| 20  | 32  | 31  |     |     |     |     |           |               |            |              |            |       |            |      |
|     |     |     |     |     |     |     | and       |  use software |            |  development |            |       |  models    |  to  |
| 0   |     |     |     |     |     |     | speed     |   up          | the        | development  |            |   of  | defensive  |      |
tools .
|     |                 |     |                       |     |     |     | • AIs    | are  | also      | built  | into         | more |   and       |   more   |
| --- | --------------- | --- | --------------------- | --- | --- | --- | -------- | ---- | --------- | ------ | ------------ | ---- | ----------- | -------- |
|     | Figure 10: Zero |     | -day vulnerabilities  |     |     |     |          |      |           |        |              |      |             |          |
|     |                 |     |                       |     |     |     | security |      | products, |        |   especially |      |   intrusion |          |
exploited in the wild (Google / Mandiant)
|              |        |            |       |          |          |      | detection  |         |   and      |     | automatic  |     |   intrusion |         |
| ------------ | ------ | ---------- | ----- | -------- | -------- | ---- | ---------- | ------- | ---------- | --- | ---------- | --- | ----------- | ------- |
|              |        |            |       |          |          |      | prevention |         |  products  |     | .          |     |             |         |
| Furthermore, |        |   no  new  | ICS   | -capable |   attack |      |            |         |            |     |            |     |             |         |
| tools        | were   | disclosed  |   in  | 2025.    | While    | the  |            |         |            |     |            |     |             |         |
|              |        |            |       |          |          |      | There      | is  no  | compelling |     |   evidence |     |   that      |   this  |
Dragos   report   on  the  Russian   attack   on  year’s   reduction   in  breaches   is  due  to
Polish   energy   infrastructure   identified   the  materially  improved  cyber  defenses . Current
| Russian |  ELECTRUM |     |  group |  as the adversary, |     |     |             |                |     |     |         |           |     |         |
| ------- | --------- | --- | ------ | ------------------ | --- | --- | ----------- | -------------- | --- | --- | ------- | --------- | --- | ------- |
|         |           |     |        |                    |     |     | indications |  in the public |     |     |  record |  are that |     |  both   |
and   this  group   has   produced   new  ICS - offensive   and   defensive   designs   and
| specific |  malware |  in the past, |     |  it did not do so  |     |     |               |     |            |     |     |       |            |     |
| -------- | -------- | ------------- | --- | ------------------ | --- | --- | ------------- | --- | ---------- | --- | --- | ----- | ---------- | --- |
|          |          |               |     |                    |     |     | technologies, |     |   AI-based |     |     | and   | otherwise, |     |
for the attack  on Poland . continue   to  improve   incrementally .  In  the
|     |     |     |     |     |     |     | absence     |   of    | a              | disruptive |     |   new         | criminal |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | -------------- | ---------- | --- | ------------- | -------- | --- |
|     |     |     |     |     |     |     | business    |  model, |  new offensive |            |     |  or defensive |          |     |
|     |     |     |     |     |     |     | technology, |         |  or other      |  dramatic  |     |  development, |          |     |
Both attacker and defender tools  this  incremental   improvement   seems   likely
and techniques continue to improve
|     |     |     |     |     |     |     | to  continue |     |   in  | the  | medium |     | term,  | with  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----- | ---- | ------ | --- | ------ | ----- |
incrementally.  material   OT  breach   frequency   tracking
|     |     |     |     |     |     |     | overall        |   global |   cyber   |     | attack |   frequencies |     |   as   |
| --- | --- | --- | --- | --- | --- | --- | -------------- | -------- | --------- | --- | ------ | ------------- | --- | ------ |
|     |     |     |     |     |     |     | those  attacks |          |  increase |     | .      |               |     |        |
Artificial   intelligence -based   (AI-based)   Recommendation  (12): All defenders  should
attacks   were   again   in  the  news   in  2025 .  plan    for incrementally  more  sophisticated
Artificial  Intelligence  is being  used  by both   cyber  attacks  in the near  future .
| attackers   |  and      |  defenders        | . For example |           | :               |     |     |     |     |     |     |     |     |     |
| ----------- | --------- | ----------------- | ------------- | --------- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| • Large     |  language |  models           |               |  (LLMs)   |  are used       |     |     |     |     |     |     |     |     |     |
| to          | speed     |   up  development |               |           |   of  effective |     |     |     |     |     |     |     |     |     |
| phishing    |           | emails,           |               | and       |   software      |     |     |     |     |     |     |     |     |     |
| development |           |   models          |               | are  used |   to  speed     |     |     |     |     |     |     |     |     |     |
| development |           |  of attack        |               |  tools    | .               |     |     |     |     |     |     |     |     |     |
2026 OT Cyber Threat Report
19

While, to date there are no public report of record that attacker capabilities are also
truly independent AI-automated attacks increasing incrementally, even taking
specifically targeting industrial automation, current offensive and defensive AI usage
there is concern that if a truly AI-driven into account . In the future however, fully
autonomous attack were designed and automated AI attacks are more credible
released inside OT networks, it would have than fully automated AI defenses in change -
an advantage over truly AI-driven controlled automation systems . The
autonomous defenses, at least in change - emergence of fully automated AI attacks
controlled environments . Engineering teams targeting OT risks triggering another step -
are legitimately unwilling to deploy change in breach counts, analogous to the
automatic intrusion prevention systems, ransomware step change that occurred at
much less AI-driven systems, because of the the turn of the decade . Recommendation
risk of those systems misdiagnosing summary :
legitimate activity and acting to impair
10. Teams defending industrial operations
safety -critical or reliability -critical functions .
should not rely on a prolonged decline in
Autonomous AI attacks have no such
cyber threat activity, nor a prolonged
compunctions .
decline in breaches with physical
Recommendation (13): AI-based attacks consequences .
are an emerging threat that bears tracking .
11. The decline in OT breaches is real .
A shift by attackers to highly automated,
Despite the decline however, the 2025
highly targeted, higher -volume and higher -
data set includes consequences that are
success -rate AI-based attacks on critical
significant . Owners and operators should
infrastructure could trigger a new step -
continue anticipate cyber attacks that
function increase in OT breaches, similar to
are able to bring about material
the step that occurred in the 2019-2021
consequences .
timeframe . OT defenders are advised to
continue improving defenses, for example
12. Defenders should plan for incrementally
by implementing the latest insights and
more sophisticated cyber attacks in the
approaches in Section Defensive
near future .
Developments in anticipation of the next
innovation in attack techniques and 13. Since autonomous AI attacks on OT
technologies, most likely involving AI. automation confers an advantage on
defenders that cannot be matched by
Summary : Ransomware attacks appear to
autonomous AI defenses in change -
have plateaued or marginally declined in
controlled environments, defenders
2025 due to fewer criminals using encryption
should closely track the development of
tactics, disarray in the ransomware criminal
autonomous attack capabilities and
economy, and increased success in law
invest in deterministic defenses .
enforcement efforts . These effects are
expected to stabilize, resulting in a resumed
increase in OT breaches with physical
consequences due to ransomware in 2026 - Defensive
2027. Concerns about lawsuits are likely
Developments
reducing the reporting of the lowest -
consequence OT events and limiting the
amount of detail available in the public Tools, techniques and perspectives for
record for other events . It is not however, defending industrial control systems
reasonable to believe that there is a large continue to evolve as well. In the sections
body of material events going unreported . below, we sample highlights of 2025 , and
one highlight of very early 2026.
While defenses should be somewhat more
capable on average in 2025 than they were
in 2024 , there is evidence in the public
2026 OT Cyber Threat Report 20

CIE Engineered Controls Database
The Cyber -Informed   Engineering   (CIE)   body   This is the first time anyone  has  collected  into
of  knowledge   is  the  most   important   a  single   body   of  knowledge   this  many   and
innovation  in 20 years  for OT Security . Idaho   this  varied   a  set  of  engineering -grade
National  Laboratory  is assembling  the body   controls  for addressing  cyber  threats . Many
of  knowledge   with  funding   from   the  US  of  these   controls   are  in  a  real   sense
Department   of  Energy   (US  DoE) .  CIE   is  “unhackable .” Overpressure  relief valves,  for
focused   resilience   by  design :  ensuring   that   example,  contain  no CPU ’s nor software  and
even   if  cyber   protections   fail,  physical   thus   carry   out  their  safety -preserving
systems  remain  safe,  reliable  and  capable  of  functions   independent   of  the  sophistication
| recovery     | .             |          |      |            |          |            | of  any      |   advanced |          |   ransomware |     |   or  | nation - |
| ------------ | ------------- | -------- | ---- | ---------- | -------- | ---------- | ------------ | ---------- | -------- | ------------ | --- | ----- | -------- |
|              |               |          |      |            |          |            | state -grade |  cyber     |  assault |              | .   |       |          |
| The  latest  |   development |          |      | in  CIE    |   is     | the  CIE   |              |            |          |              |     |       |          |
| Controls     |   Database    |          |   –  | a          | database |   of       |              |            |          |              |     |       |          |
| technologies |   and         |   design |      |   patterns |   that   |   can      |              |            |          |              |     |       |          |
be  applied   to  address   specific   threats   and   Many tools and techniques in the
needs,  in a wide  spectrum  of industries . For  CIE body of knowledge are in a real
example,   the  database   sorts   controls   into  sense “unhackable”  – they carry
| seven  categories |     | :   |     |     |     |     |     |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
out their protective functions
• Physical   logic   mechanisms   –  such   as  reliably, even in the face of the
electro -mechanical   relief  valves   and   most sophisticated -imaginable
governors,   physically   prevent   unsafe   nation -state -grade cyber assaults.
| operations  | .      |               |      |        |              |           |     |     |     |     |     |     |     |
| ----------- | ------ | ------------- | ---- | ------ | ------------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| • Redundant |        | designs       |   –  | such   |   as         | circuit   |     |     |     |     |     |     |     |
| breakers    |   that |   incorporate |      |   both |   electrical |           |     |     |     |     |     |     |     |
and  mechanical  elements,  so the failure  of  Recommendation   (14):  OT  security   teams
|          |                |     |             |     |     |     | should    |  adopt  CIE, track |     |  the emerging |            |      |  body  of  |
| -------- | -------------- | --- | ----------- | --- | --- | --- | --------- | ------------------ | --- | ------------- | ---------- | ---- | ---------- |
| one does |  not eliminate |     |  protection |     | .   |     |           |                    |     |               |            |      |            |
|          |                |     |             |     |     |     | knowledge |  as it grows       |     |  and          |  develops, |  and |  join      |
• Physical   constraints   and   material   the CIE  Community  of Practice  to contribute
properties  – such  as plugs  that  melt  when   actively   to  the  development   of  the
| a vessel  |  temperature |     |  becomes   |     |  too high. |           |             |         |     |       |          |            |     |
| --------- | ------------ | --- | ---------- | --- | ---------- | --------- | ----------- | ------- | --- | ----- | -------- | ---------- | --- |
|           |              |     |            |     |            |           | methodology | .       |     |       |          |            |     |
| • Digital |   engineered |     |   controls |     |   –        | digital   |             |         |     |       |          |            |     |
|           |              |     |            |     |            |           | Summary     | :  The  |     | CIE   | Controls |   Database |     |
designs   that   maintain   process   stability   documents   engineering -grade   tools   and
even  in the face  of compromised,  failed  or  techniques  for addressing  cyber  risk – many
inconsistent  inputs . of  them   in  a  real   sense   “unhackable .”
|           |            |     |            |     |           |       | Recommendation |     |  summary |     | :   |     |     |
| --------- | ---------- | --- | ---------- | --- | --------- | ----- | -------------- | --- | -------- | --- | --- | --- | --- |
| • Passive |   physical |     |   dynamics |     |   –  such |   as  |                |     |          |     |     |     |     |
flywheels  and  hydraulic  accumulators  that   14. Use  CIE,  use  the  techniques   in  the  new
| physically |   buffer |     |   unsafe |     | variations |   in  |           |      |             |     |             |     |        |
| ---------- | -------- | --- | -------- | --- | ---------- | ----- | --------- | ---- | ----------- | --- | ----------- | --- | ------ |
|            |          |     |          |     |            |       | database, |  and |  contribute |     |  experience |     |  and   |
physical  processes . expertise   to  the  emerging   CIE   body   of
|           |                    |      |             |            |                |          | knowledge |     | .   |     |     |     |     |
| --------- | ------------------ | ---- | ----------- | ---------- | -------------- | -------- | --------- | --- | --- | --- | --- | --- | --- |
| • One     | -way   enforcement |      |             |   and      |   irreversible |          |           |     |     |     |     |     |     |
| actions   |  – such            |  as  | (physical)  |            |  ratchets      |   or     |           |     |     |     |     |     |     |
| (digital) |   unidirectional   |      |             |   gateways |                |   that   |           |     |     |     |     |     |     |
| make      |   “backwards       |      | ”  flows    |            | of  materials, |          |           |     |     |     |     |     |     |
| movement  |  or data           |      |  physically |            |  impossible    | .        |           |     |     |     |     |     |     |
•
| Fail -safe |   defaults |     |   –       | such            |   as             | spring - |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | --------- | --------------- | ---------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| loaded     |   brakes   |     | that      |   engage        |                  |   when   |     |     |     |     |     |     |     |
| pneumatic  |  pressure  |     |  or power |                 |  is lost, return |          |     |     |     |     |     |     |     |
| processes  |  to safe   |     |  states   |  in emergencies |                  | .        |     |     |     |     |     |     |     |
2026 OT Cyber Threat Report
21

Secure Connectivity Principles
| The  UK  | National |                          |   Cyber |   Security |     |   Center  |   (UK  |     |     |     |     |     |     |     |     |
| -------- | -------- | ------------------------ | ------- | ---------- | --- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| NCSC)    |  along   |  with nine international |         |            |     |  partners |        |     |     |     |     |     |     |     |     |
The new UK NCSC et al. advice
| published          |  Secure |              |  connectivity |        |  principles |         |  for  |                             |     |     |     |     |            |     |     |
| ------------------ | ------- | ------------ | ------------- | ------ | ----------- | ------- | ----- | --------------------------- | --- | --- | --- | --- | ---------- | --- | --- |
|                    |         |              |               |        |             |         |       | recommends hardware         |     |     |     |     | -enforced  |     |     |
| Operational        |         |   Technology |               |   (OT) |   in        | January |   of  |                             |     |     |     |     |            |     |     |
|                    |         |              |               |        |             |         |       | unidirectional protections  |     |     |     |     | –          |     |     |
| 2026 . The 33-page |         |              |  document     |        |  is focused |         |  on   |                             |     |     |     |     |            |     |     |
protections that, when deployed
| securing       |   networks |            |   and |   connectivity, |     |     |   rather   |                        |     |     |     |         |     |     |     |
| -------------- | ---------- | ---------- | ----- | --------------- | --- | --- | ---------- | ---------------------- | --- | --- | --- | ------- | --- | --- | --- |
|                |            |            |       |                 |     |     |            | correctly, even nation |     |     |     | -state  |     |     |     |
| than  securing |            |  endpoints |       | .               |     |     |            |                        |     |     |     |         |     |     |     |
adversaries struggle to overcome.
| The focus |  on connectivity |     |     |  is refreshing |       |          |  – too  |     |     |     |     |     |     |     |     |
| --------- | ---------------- | --- | --- | -------------- | ----- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
| much      | first-generation |     |     | -style         |   OT  | security |         |     |     |     |     |     |     |     |     |
advice  positions  network  segmentation  as a  The  new  advice   from   the  UK  NCSC   et  al
compensating   measure   rather   than   a  highlights   this.  The  advice   contains   much
primary   protective   measure .  Such   advice   that   is  unique   –  that   has   never   been   said
ignores  50-year -old cybersecurity  theory : before   in  any   government ’s  OT  security
|     |     |     |     |     |     |     |     | guidelines |  nor recommendations |     |     |     | . Very briefly, |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | -------------------- | --- | --- | --- | --------------- | --- | --- |
•
| Bell / Lapadula |     |          |  – showed    |     |  that |  to prevent  |     |              |     |           |     |                    |     |     |     |
| --------------- | --- | -------- | ------------ | --- | ----- | ------------ | --- | ------------ | --- | --------- | --- | ------------------ | --- | --- | --- |
|                 |     |          |              |     |       |              |     | the document |     |  explores |     |  eight  principles |     | :   |     |
| espionage       |     |  – theft |  of valuable |     |       |  information |     |              |     |           |     |                    |     |     |     |
–  we  must   prevent   lower -security   actors   1. Balance  the risks  and  opportunities  – a
reading  from higher -security  sources,  and   conventional  discussion  of risk manage -
| prevent         |     | high-security |           |   actors |     | from   | writing   | ment     |               |     |     |          |               |     |     |
| --------------- | --- | ------------- | --------- | -------- | --- | ------ | --------- | -------- | ------------- | --- | --- | -------- | ------------- | --- | --- |
| to low-security |     |               |  sources, |  while   |     |        |           |          |               |     |     |          |               |     |     |
|                 |     |               |           |          |     |        |           | 2. Limit |  the exposure |     |     |  of your |  connectivity |     |     |
• Biba  – showed  that  to prevent  sabotage  –  –  when   we  must   connect   automation
mis-operation   of  important   assets,   we  assets  to IT computers,  or worse  to the
must  prevent  lower -security  actors  writing   Internet,   keep   the   affected   OT  assets
to  high-security   operations   and   prevent   patched ,  scan   regularly   for  Internet -
actors   in  high -security   operations   from   exposed  IP addresses  and  services,  and
reading  potentially  compromised   informa - be  paranoid   about   wireless   commun -
tion from low-security  sources . ications .  While  none   of  the  individual
|     |     |     |     |     |     |     |     | pieces       |   of  | advice |   are  | new,  | some |   of        | the  |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------ | ----- | ------ | ------ | ----- | ---- | ----------- | ---- |
|     |     |     |     |     |     |     |     | combinations |       |        | are    | new   | and  |   unusually |      |
|     |     |     |     |     |     |     |     | useful       | .     |        |        |       |      |             |      |
Controlling the flow of attack
information is essential to  3. Centralise   and   standardise   network
| preventing cyber |                        |              | -sabotage and is  |               |          |          |       |                     |                   |            |             |              |                |             |          |
| ---------------- | ---------------------- | ------------ | ----------------- | ------------- | -------- | -------- | ----- | ------------------- | ----------------- | ---------- | ----------- | ------------ | -------------- | ----------- | -------- |
|                  |                        |              |                   |               |          |          |       | connections         |                   |            | –  minimise |              |   our          | external    |          |
| not a            | “compensating measure. |              |                   |               |          | ”        |       |                     |                   |            |             |              |                |             |          |
|                  |                        |              |                   |               |          |          |       | connectivity        |                   |   and      |             | ideally      |   route        |             | it  all  |
|                  |                        |              |                   |               |          |          |       | through             |                   | a  central |             | facility     |   for          | intrusion   |          |
|                  |                        |              |                   |               |          |          |       | detection           |                   |   and      |   active    |   management |                |             |   of     |
|                  |                        |              |                   |               |          |          |       | rules,              |  vulnerabilities, |            |             |  actionable  |                |  intel, etc | .        |
| In other         |  words,                |  to prevent  |                   |  sabotage,    |          |  which   |  is   |                     |                   |            |             |              |                |             |          |
| the  most        |   important            |              |                   | cybersecurity |          |   goal   |   at  |                     |                   |            |             |              |                |             |          |
|                  |                        |              |                   |               |          |          |       | 4. Use standardised |                   |            |  and        |  secure      |                |  protocols  |          |
| most  industrial |                        |  operations, |                   |               |  we must |  prevent |       |                     |                   |            |             |              |                |             |          |
|                  |                        |              |                   |               |          |          |       | –                   | use               | encryption |             |   and        | authentication |             |          |
the  movement   of  attack   information   into  inside   our  ICS   as  much   as  is  practical,
| those    | operations |          |   from |                | less   | trustworthy |     |                |          |           |          |       |                |     |         |
| -------- | ---------- | -------- | ------ | -------------- | ------ | ----------- | --- | -------------- | -------- | --------- | -------- | ----- | -------------- | --- | ------- |
|          |            |          |        |                |        |             |     | and            |   always |   encrypt |          |   and |   authenticate |     |         |
| sources, |  such      |  as from |        |  the Internet, |        |  or from    |     |                |          |           |          |       |                |     |         |
|          |            |          |        |                |        |             |     | communications |          |           |   across |       | IT,  Internet  |     |   and   |
Internet -exposed  IT networks . Controlling  the  other  external  networks .
| flow         | of  information, |          |              | particularly |               |   but     | not  |     |     |     |     |     |     |     |     |
| ------------ | ---------------- | -------- | ------------ | ------------ | ------------- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
| exclusively  |  online          |          |  / networked |              |  information, |           |  is  |     |     |     |     |     |     |     |     |
| a  primary   |                  | security |   goal,      |              | not  a        | secondary |      |     |     |     |     |     |     |     |     |
| compensating |                  |  measure |              | .            |               |           |      |     |     |     |     |     |     |     |     |
2026 OT Cyber Threat Report
22

5. Harden   your   OT  boundary   –  lots   of  Again,   the  document   is  a  refreshing   new
good   advice   for  the  important   IT  /  OT  look at network  segmentation  options,  with
consequence   boundary,   including   some  all-new advice,  and  a perspective  that
hardware -enforced   unidirectional   recognizes   the  importance   of  controlling
communications,   hardware -enforced   and   managing   connectivity   as  a  primary
remote  access  and  military -grade  cross - protective  measure  for physical  operations .
| domain   |  solutions   |     |  for vetting |  information |     |     |                |          |       |          |           |      |         |
| -------- | ------------ | --- | ------------ | ------------ | --- | --- | -------------- | -------- | ----- | -------- | --------- | ---- | ------- |
|          |              |     |              |              |     |     | Recommendation |          |       |   (15):  | Defensive |      | teams   |
| entering |  OT networks |     | .            |              |     |     |                |          |       |          |           |      |         |
|          |              |     |              |              |     |     | should         |   review |   and |   adopt  |   the     | new  | OT      |
6. Limit  the impact  of compromise  – some   connectivity   guidelines,   recognizing   that
older   advice   coupled   with  a  newer   controlling  the flow  of attack  information  to
discussion   of  options   for  micro - prevent  cyber -sabotage  is a primary  goal  of
segmentation   to  control   lateral   OT security  programs,  not a compensating
| movement |  / pivoting |     |  attacks | .   |     |     | measure | .   |     |     |     |     |     |
| -------- | ----------- | --- | -------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- |
7. Ensure   all  connectivity   is  logged   and   Summary : The new multi-agency  advice  on
monitored  – the usual  advice  to monitor   OT connectivity  highlights  the importance  of
network   traffic,   especially   remote   controlling   the  flow   of  attacks   through
access   from   IT  networks   and   the  connections   into  and   out  of  OT  networks .
Internet,   with  new   advice   for  “break   The  advice   is  ground -breaking   in  some
glass”  emergency  connections . respects,   including   recommending
|              |               |             |          |            |           |     | hardware | -based      |             | unidirectional |                | protections, |         |
| ------------ | ------------- | ----------- | -------- | ---------- | --------- | --- | -------- | ----------- | ----------- | -------------- | -------------- | ------------ | ------- |
| 8. Establish |  an isolation |             |  plan    |  – talks   |  about    |     |          |             |             |                |                |              |         |
|              |               |             |          |            |           |     | cross    | domain      |   systems,  |                |   “browse      |              | down”   |
| different    |  kinds        |  of site    |  and/or  |  subsystem |           |     |          |             |             |                |                |              |         |
|              |               |             |          |            |           |     | policies |   for       | engineering |                |   workstations |              |   and   |
| emergency    |               |   isolation |          | /          | islanding |     |          |             |             |                |                |              |         |
|              |               |             |          |            |           |     | other    | innovations |             | .              | Recommendation |              |         |
| approaches,  |               |   including |          | a  brand   | -new      |     |          |             |             |                |                |              |         |
|              |               |             |          |            |           |     | summary  | :           |             |                |                |              |         |
| discussion   |               | of  the     | business |            | value     | of  |          |             |             |                |                |              |         |
hardware -enforced   unidirectional   15. Review  and  adopt  the new connectivity
| communications |     |            | as    | part   | of  | the  | guidelines |     | .   |     |     |     |     |
| -------------- | --- | ---------- | ----- | ------ | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- |
| emergency      |     |  islanding |  plan | .      |     |      |            |     |     |     |     |     |     |
2026 OT Cyber Threat Report
23

Looking Forward
For 50 years, industry has deployed and recommend deterministic, hardware -
automation systems to increase productivity enforced protections .
and reduce production costs . All modern
It is not reasonable for workers at industrial
automation uses computers, all computers
sites to increasingly fear for their lives as
use software, all software has defects, and
their workplace becomes increasingly
some of those defects are cyber
automated and thus increasingly vulnerable .
vulnerabilities . Thus, for 50 years, we have
We need to start deploying “unhackable ”
deployed more and more targets for cyber
deterministic defenses, in addition to
attacks . In addition, data in motion is the
software / cybersecurity defenses .
lifeblood of modern automation, all cyber -
sabotage is by definition attack information,
To this end, key questions defenders should
and all information flows can encode
ask going forward include :
attacks . Thus, for 50 years, we have deployed
more and more opportunities to attack the • Detecting, responding to and recovering
ever-increasing number of targets . Neither of from attacks all take time, during which
these trends is reversing in the next 25 years . time adversaries have control of some or
all of our industrial automation systems .
What is an acceptable amount of time for
adversaries to control or operate safety -
It is not reasonable for workers at critical, critical infrastructure, or otherwise
industrial sites to increasingly fear important or valuable physical processes?
for their lives as their workplace
• What credible cyber attacks and
becomes increasingly automated,
credible consequences are not defeated
increasing both cyber targets and
with a high degree of confidence by the
cyber attack vectors. To protect current defensive posture, and are those
workers, we must deploy credible consequences acceptable?
deterministic “unhackable ”
• Is it reasonable to protect industrial
defenses, in addition to software /
operations with only software, given the
cybersecurity defenses. attack capabilities it is reasonable to
attribute to credible threats, including the
track record of zero -day software
exploits?
The majority of today ’s OT networks are
protected from cyber attacks exclusively by Critical infrastructures especially, anyone for
software protections, and software fails whom a nation -state -grade attack is a
predictably . If a given exploit can take credible threat, and enterprises whose worst
advantage of a vulnerability, launching that credible consequences are very expensive
exploit against the vulnerable target always should all consider deterministic, hardware -
produces the same result . Modelling this kind enforced defenses including hardware -
of design failure as a probability is a mistake enforced remote access, in addition to
– in engineering safety terms, cyber attacks conventional software defenses .
most often represent design failures rather
than random equipment failures or human
error.
The CIE initiative, the latest UK NCSC
guidance, CISA secure remote access
guidance , and many others recognize the
intrinsic limitations of software protections
2026 OT Cyber Threat Report 24

| Appendix A  |     | –   |  2025 Data Set |     |     |     |     |     |
| ----------- | --- | --- | -------------- | --- | --- | --- | --- | --- |
Attacker
| Date | Victim | Region | Industry |     | Consequence |     | Summary | References |
| ---- | ------ | ------ | -------- | --- | ----------- | --- | ------- | ---------- |
Type
|     |     |     |     |     |     | A 15-year | -old logged into a  |     |
| --- | --- | --- | --- | --- | --- | --------- | ------------------- | --- |
portal that controls the
|     |     |     |     |     | Several ships,  | routes of oil tankers and  |     |     |
| --- | --- | --- | --- | --- | --------------- | -------------------------- | --- | --- |
Mediter -
|     |     |     |     |     | including oil tankers,  | transport ships in the  |     | icsstrive.com |
| --- | --- | --- | --- | --- | ----------------------- | ----------------------- | --- | ------------- |
2025 -01-19 Many ranean Transport Hacktivist diverted off course in  Mediterranean Sea, changing  corriere.it
Sea
|     |     |     |     |     | the Mediterranean Sea | some routes. The teenager  |     |     |
| --- | --- | --- | --- | --- | --------------------- | -------------------------- | --- | --- |
was referred to youth justice
in Italy.
More than 79 print
|     |      |     |         |     | newspapers cancelled,  | Qilin ransomware criminals  |     | icsstrive.com |
| --- | ---- | --- | ------- | --- | ---------------------- | --------------------------- | --- | ------------- |
|     | Lee  |     | Pulp &  |     |                        |                             |     |               |
2025 -02-03 Enterprises USA Paper Ransomware delayed or forced to  attacked a large newspaper  pressfreedomtracker.us
|     |     |     |     |     | print smaller versions  | printer |     | cybersecuritydive.com |
| --- | --- | --- | --- | --- | ----------------------- | ------- | --- | --------------------- |
for over 10 days
Production at 8
factories shut down
for over 12 days.
icsstrive.com
|             |     |     | Pulp &  |            | Customers reported  | Cyber attack hits CPI printing  |     |                   |
| ----------- | --- | --- | ------- | ---------- | ------------------- | ------------------------------- | --- | ----------------- |
| 2025 -02-07 | CPI | UK  |         | Ransomware |                     |                                 |     | thebookseller.com |
Paper delays in printing their  - UK's largest book printer reddit.com
books as long as 18
days after the initial
attack.
|     |     |     |     |     | Gas stations & other  | Ransomware attack on IT  |     | icsstrive.com |
| --- | --- | --- | --- | --- | --------------------- | ------------------------ | --- | ------------- |
2025 -02-09 Sault Tribe USA Oil & Gas Ransomware facilities closed for 2  impacted numerous  myupnow.com
|     |     |     |     |     | weeks | computer and phone systems |     | therecord.media |
| --- | --- | --- | --- | --- | ----- | -------------------------- | --- | --------------- |
Ransomware encrypted
equipment on the IT network.
Initially it was thought that
|     |     |     |     |     | Two factories shut  |     |     | icsstrive.com |
| --- | --- | --- | --- | --- | ------------------- | --- | --- | ------------- |
2025 -02-11 Alf DaFrè Italy Discrete  Ransomware down and 350 people  enough info was cached in  decripto.org
|     |     |     | Mfg |     |                     | production to continue  |     |                 |
| --- | --- | --- | --- | --- | ------------------- | ----------------------- | --- | --------------- |
|     |     |     |     |     | laid off for 8 days |                         |     | comparitech.com |
operating up to 36 hours,
suggesting OT was not
breached.
Operations at St.
|     |     |     | Food &  |     |     |     |     | icsstrive.com |
| --- | --- | --- | ------- | --- | --- | --- | --- | ------------- |
2025 -02-22 Ganong Canada Ransomware Stephen facility were  Very few details released
|     |     |     | Beverage |     | affected temporarily |     |     | fipa.bc.ca |
| --- | --- | --- | -------- | --- | -------------------- | --- | --- | ---------- |
Lynx ransomware group
|     | Stürmer  |     |     |     | Deliveries delayed  | -   |     | icsstrive.com |
| --- | -------- | --- | --- | --- | ------------------- | --- | --- | ------------- |
2025 -02-25 Germany Transport Ransomware compromised the machine
|     | Maschinen |     |     |     | not specified how long |     |     | csoonline.com |
| --- | --------- | --- | --- | --- | ---------------------- | --- | --- | ------------- |
wholesaler
Few details. A ransomware
Temporarily impacted
group later took credit for the
|             | National  |     |           |            | shipping and receiving  |                           |     |               |
| ----------- | --------- | --- | --------- | ---------- | ----------------------- | ------------------------- | --- | ------------- |
|             |           |     | Discrete  |            |                         | attack. The company says  |     | icsstrive.com |
| 2025 -03-01 | Presto    | USA |           | Ransomware | and some                |                           |     |               |
Industries Mfg manufacturing  temporary work -arounds  securityweek.com
were put in place for critical
processes.
processes.
|     |     |     |     |     | "Production losses  | Few details released, but  |     | icsstrive.com |
| --- | --- | --- | --- | --- | ------------------- | -------------------------- | --- | ------------- |
2025 -03-02 Adval Tech Switzerland Discrete  Ransomware could occur at various  criminal charges against a  cybermaterial.com
Mfg
|     |     |     |     |     | locations" | ransomware group were filed |     | inside -it.ch |
| --- | --- | --- | --- | --- | ---------- | --------------------------- | --- | ------------- |
A cyber attack on the crystal
|     |     |     |     |     | Approximately 3% of  | awards and gifts  |     |     |
| --- | --- | --- | --- | --- | -------------------- | ----------------- | --- | --- |
Discrete  orders delayed during  manufacturer shut down  icsstrive.com
| 2025 -03-07 | Crystal D | USA |     | Unknown |     |     |     |     |
| ----------- | --------- | --- | --- | ------- | --- | --- | --- | --- |
Mfg a multi -day production  order processing and  asicentral.com
|     |     |     |     |     | shutdown | production for a number of  |     |     |
| --- | --- | --- | --- | --- | -------- | --------------------------- | --- | --- |
days
Company issued a profit
Chicken processing
Astral  South  Food &  warning due to costs and  icsstrive.com
2025 -03-16 Foods Africa Beverage Unknown plants shut down for  revenue delays from cleaning  therecord.media
one week
up after cyber attack
Airport displays,
|     | Kuala   |     |     |     |                        | Few details were released.    |     |               |
| --- | ------- | --- | --- | --- | ---------------------- | ----------------------------- | --- | ------------- |
|     | Lumpur  |     |     |     | check -in and baggage  | Authorities initially denied  |     |               |
|     |         |     |     |     | handling became        |                               |     | icsstrive.com |
2025 -03-23 Inter- Malaysia Transport Unknown impacts on flights, but
|     |           |     |     |     | inoperable for 1 | -2                       |     | jobstore.com |
| --- | --------- | --- | --- | --- | ---------------- | ------------------------ | --- | ------------ |
|     | national  |     |     |     |                  | reports from travellers  |     |              |
days, leading to flight
|     | Airport |     |     |     | delays | contradicted these denials. |     |     |
| --- | ------- | --- | --- | --- | ------ | --------------------------- | --- | --- |
22002266  OOT TC yCbyebre rT hTrheraeta tR eRpeoprotrt

Attacker
| Date | Victim | Region | Industry |     | Consequence | Summary |     | References |
| ---- | ------ | ------ | -------- | --- | ----------- | ------- | --- | ---------- |
Type
|     |     |     |     |     | Partial halt in fuel  | Few details beyond that          |     |               |
| --- | --- | --- | --- | --- | --------------------- | -------------------------------- | --- | ------------- |
|     |     |     |     |     | distribution to gas   | workers were told not to log in  |     | icsstrive.com |
2025 -03-26 Lukoil Russia Oil & Gas Unknown stations & other  to their accounts after an  newsukraine.bc.ua
|     |     |     |     |     | consumers for several  | unusual error message showed  |     | united24media.com |
| --- | --- | --- | --- | --- | ---------------------- | ----------------------------- | --- | ----------------- |
|     |     |     |     |     | days                   | on many computers             |     |                   |
DDOS attack crippled Platon
|             |        |        |           |            | Over one thousand     | system that provides drivers  |     | icsstrive.com   |
| ----------- | ------ | ------ | --------- | ---------- | --------------------- | ----------------------------- | --- | --------------- |
| 2025 -03-27 | Platon | Russia | Transport | Hacktivist |                       |                               |     |                 |
|             |        |        |           |            | trucks could not move | with destinations and route   |     | obozrevatel.com |
maps
|     | Instituto de  |     |     |     |     | Few details beyond that the  |     |     |
| --- | ------------- | --- | --- | --- | --- | ---------------------------- | --- | --- |
Production of
|     | Pesquisas  |     |     |     |     | plant was scheduled to restart  |     |     |
| --- | ---------- | --- | --- | --- | --- | ------------------------------- | --- | --- |
2025 -03-28 Energéticas  Brazil Pharma - Unknown radioisotopes used in  Mar 31, with resumed  icsstrive.com
|     |              |     | ceuticals |     | medicine stopped for  |                        |     | gov.br |
| --- | ------------ | --- | --------- | --- | --------------------- | ---------------------- | --- | ------ |
|     | e Nucleares  |     |           |     |                       | shipments of medicine  |     |        |
13 days
|     | (IPEN/CNEN) |     |     |     |     | expected Apr 10 |     |     |
| --- | ----------- | --- | --- | --- | --- | --------------- | --- | --- |
Temporarily impacted
Sensata's operations,
Discrete  including shipping,  No details released beyond 8 -K  icsstrive.com
| 2025 -04-06 | Sensata | USA |     | Ransomware |                 |           |     |                |
| ----------- | ------- | --- | --- | ---------- | --------------- | --------- | --- | -------------- |
|             |         |     | Mfg |            | receiving, and  | statement |     | cloudfront.net |
manufacturing
production.
Exploited a weak password on
Lake  Water &  Water flows at 497 l/s  a web -accessible control  icsstrive.com
| 2025 -04-07 | Risevatnet  | Norway |            | Hacktivist | above normal for 4  |                           |          |              |
| ----------- | ----------- | ------ | ---------- | ---------- | ------------------- | ------------------------- | -------- | ------------ |
|             |             |        | Wastewater |            |                     | panel. No risk to public  | - river  | hackread.com |
|             | Dam         |        |            |            | hours               |                           |          |              |
capacity is 20,000 l/s
|     |     |     |     |     | Incorrect messages  | "Hackers" accessed crossing  |         |     |
| --- | --- | --- | --- | --- | ------------------- | ---------------------------- | ------- | --- |
|     |     |     |     |     |                     | button control systems       | - most  |     |
coming out of
|             | City in Silicon  |     |           |            |                       | likely using Bluetooth and a  |     | icsstrive.com |
| ----------- | ---------------- | --- | --------- | ---------- | --------------------- | ----------------------------- | --- | ------------- |
| 2025 -04-19 |                  | USA | Transport | Hacktivist | handicap -accessible  |                               |     |               |
Valley pedestrian crossing  default password  - and  theregister.com
substituted "funny" / political
buttons
recordings
|     |        |     |           |     | Some factories  |                               |     | icsstrive.com |
| --- | ------ | --- | --------- | --- | --------------- | ----------------------------- | --- | ------------- |
|     | Masimo |     | Discrete  |     |                 | Few details disclosed beyond  |     |               |
2025 -04-27 Corporation USA Mfg Unknown working at reduced  8-K filing sec.gov
|     |     |     |     |     | capacity |     |     | hipaajournal.com |
| --- | --- | --- | --- | --- | -------- | --- | --- | ---------------- |
Halted certain
Nucor  Metals &  No details released beyond 8 -K  icsstrive.com
| 2025 -05-14 |     | USA |     | Unknown | production operations  |     |     |     |
| ----------- | --- | --- | --- | ------- | ---------------------- | --- | --- | --- |
Corporation Mining at various locations. statement cloudfront.net
Customer shipments
|     | Peter Green  |     |     |     |               | Ransomware disrupted new  |     |               |
| --- | ------------ | --- | --- | --- | ------------- | ------------------------- | --- | ------------- |
|     |              |     |     |     | could not be  |                           |     | icsstrive.com |
2025 -05-14 Chilled  UK Transport Ransomware order processing and some
Logistics processed for up to 5  existing orders therecord.media
days
GPS spoofing is widespread in
the region, usually attributed
Pole Star  Saudi  Containership MSC  to Houti rebels, Iran and / or  icsstrive.com
| 2025 -05-15 |        |        | Transport | Nation State | Antonia ran aground in  |                               |     |              |
| ----------- | ------ | ------ | --------- | ------------ | ----------------------- | ----------------------------- | --- | ------------ |
|             | Global | Arabia |           |              |                         | Israel. The ship ran aground  |     | gcaptain.com |
Red Sea
because its AIS system was
confused by spoofed GPS data
Few details beyond that a
|     |     |     |     |     | Uphal Germany plant  | cyber attack impacted at least  |     | icsstrive.com |
| --- | --- | --- | --- | --- | -------------------- | ------------------------------- | --- | ------------- |
Food &
2025 -05-16 Arla Foods Germany Beverage Unknown halted & reduced  IT systems leading to a  food.com
|     |     |     |     |     | production for 6 days | shutdown + delayed or  |     | yahoo.com |
| --- | --- | --- | --- | --- | --------------------- | ---------------------- | --- | --------- |
cancelled orders
Napkin manufacturer hit by
|     |     |     |         |     | Factory employing 240   | ransomware was forced to  |     |               |
| --- | --- | --- | ------- | --- | ----------------------- | ------------------------- | --- | ------------- |
|     |     |     | Pulp &  |     | people shut down for 3  |                           |     | icsstrive.com |
2025 -05-19 Fasana Germany Ransomware declare bankruptcy after
|     |     |     | Paper |     | weeks, business  |     |     | securityaffairs.com |
| --- | --- | --- | ----- | --- | ---------------- | --- | --- | ------------------- |
factory was shut down for 3
declared bankruptcy
weeks.
|     |     |     |         |     | Three factories  |                                |     | icsstrive.com |
| --- | --- | --- | ------- | --- | ---------------- | ------------------------------ | --- | ------------- |
|     |     |     | Pulp &  |     |                  | Cardboard manufacturer hit by  |     |               |
2025 -05-23 Wellteam Germany Unknown stopped production  security.de
|     |     |     | Paper |     |                    | cyber attack |     |               |
| --- | --- | --- | ----- | --- | ------------------ | ------------ | --- | ------------- |
|     |     |     |       |     | for about one week |              |     | csoonline.com |
Ransomware impacted
Mediehuset  Pulp &  Unable to print one  business systems & print  icsstrive.com
| 2025 -05-27 |     | Norway |     | Ransomware |     |     |     |     |
| ----------- | --- | ------ | --- | ---------- | --- | --- | --- | --- |
Altaposten Paper edition of newspaper edition of newspaper. Online  altaposten.no
editions were still available
22002266  OOT TC yCbyebre rT hTrheraeta tR eRpeoprotrt

Attacker
| Date | Victim | Region | Industry |     | Consequence | Summary | References |
| ---- | ------ | ------ | -------- | --- | ----------- | ------- | ---------- |
Type
The company reports
|             |          |     |         |         | Unable to fulfill    | approximately $400M in lost    |               |
| ----------- | -------- | --- | ------- | ------- | -------------------- | ------------------------------ | ------------- |
|             |          |     |         |         | wholesale food       | sales, $25M in incident        |               |
|             | United   |     |         |         |                      |                                | icsstrive.com |
|             |          |     | Food &  |         | orders for 10 days.  | mitigation costs, for a net /  |               |
| 2025 -06-05 | Natural  | USA |         | Unknown |                      |                                | youtube.com   |
Foods Beverage Retailers like Whole  profit loss of $50 -60M. A cyber  cpomagazine.com
|     |     |     |     |     | Foods suffered   | attack took down IT systems        |     |
| --- | --- | --- | --- | --- | ---------------- | ---------------------------------- | --- |
|     |     |     |     |     | supply shortages | resulting in an inability to take  |     |
orders to deliver foods.
DDoS attack took down one
|             | Roularta    |         | Pulp &  |         | Printing stopped for  |                               | icsstrive.com     |
| ----------- | ----------- | ------- | ------- | ------- | --------------------- | ----------------------------- | ----------------- |
| 2025 -06-10 |             | Belgium |         | Unknown |                       | printing facility + business  |                   |
|             | Media Group |         | Paper   |         | 1 day                 |                               | cybermaterial.com |
systems
|     | Dairy  |     |     |     | Multiple plants were  | Ransomware hit the milk  |     |
| --- | ------ | --- | --- | --- | --------------------- | ------------------------ | --- |
Food &  unable to receive or  processor, stealing information  icsstrive.com
| 2025 -06-11 | Farmers of  | USA |     | Ransomware |     |     |     |
| ----------- | ----------- | --- | --- | ---------- | --- | --- | --- |
Beverage process milk for a  and leading to a shutdown of  farms.com
America
|     |     |     |           |     | short period        | some IT systems                |               |
| --- | --- | --- | --------- | --- | ------------------- | ------------------------------ | ------------- |
|     |     |     |           |     |                     | Production was able to resume  | icsstrive.com |
|     |     |     | Discrete  |     | Production stopped  |                                |               |
2025 -06-15 Siloking Germany Ransomware in "emergency mode" after 5  csoonline.com
|     |     |     | Mfg |     | for 5 days            |                                   |                       |
| --- | --- | --- | --- | --- | --------------------- | --------------------------------- | --------------------- |
|     |     |     |     |     |                       | days                              | agrartechnikonline.de |
|     |     |     |     |     | Meat, dairy, egg and  | "IT Army of Ukraine" took credit  |                       |
|     |     |     |     |     | other animal -based   | for a DDoS attack halted          |                       |
|     |     |     |     |     | products could not    | access to Russia's Mercury        |                       |
Federal State
|     |     |     |     |     | be delivered to  | system for certifying human | -   |
| --- | --- | --- | --- | --- | ---------------- | --------------------------- | --- |
Information  Food &  processing plants  consumable animal products.  icsstrive.com
| 2025 -06-18 | System for   | Russia |          | Hacktivist |                      |                                 | bitdefender.com |
| ----------- | ------------ | ------ | -------- | ---------- | -------------------- | ------------------------------- | --------------- |
|             |              |        | Beverage |            | nor consumers for    | Producers were encouraged to    |                 |
|             | Veterinary   |        |          |            |                      |                                 | therecord.media |
|             |              |        |          |            | several hours, some  | switch to manual processing,    |                 |
|             | Surveillance |        |          |            | perishable goods     | but not all processors had      |                 |
|             |              |        |          |            | discarded as a       | procedures that could accept    |                 |
|             |              |        |          |            | result               | paper certificates anymore.     |                 |
|             |              |        |          |            | Prevented Iran from  | The US military bombed Iranian  |                 |
|             |              |        |          |            | launching surface    | - nuclear weapons development   |                 |
Iranian
|     |     |     |     |     | to-air missiles at  | sites, and "digitally disrupted"  |     |
| --- | --- | --- | --- | --- | ------------------- | --------------------------------- | --- |
2025 -06-22 nuclear  Iran Military Nation State therecord.media
|     | program |     |     |     | American warplanes  | Iranian air missile defense     |     |
| --- | ------- | --- | --- | --- | ------------------- | ------------------------------- | --- |
|     |         |     |     |     | that had entered    | systems. Few other details are  |     |
|     |         |     |     |     | Iranian airspace.   | released at this writing.       |     |
Building supply manufacturer
Discrete  Production and  was hit by a "cyber attack"  icsstrive.com
2025 -06-24 Heim & Haus Germany Unknown shipments stopped  heimhaus.de
|     |     |     | Mfg |     |              | that impaired production &  |                  |
| --- | --- | --- | --- | --- | ------------ | --------------------------- | ---------------- |
|     |     |     |     |     | for one week |                             | com borncity.com |
order processing
Production and
Food &  logistics operation  A cyber attack shut down one  icsstrive.com
| 2025 -06-30 | Hero | Spain |          | Unknown |                        |                |              |
| ----------- | ---- | ----- | -------- | ------- | ---------------------- | -------------- | ------------ |
|             |      |       | Beverage |         | stopped for "several"  | plant in Spain | democrata.es |
days
|             |              |     |           |            | Shipments were       | Wholesaler suffered            |               |
| ----------- | ------------ | --- | --------- | ---------- | -------------------- | ------------------------------ | ------------- |
|             |              |     |           |            | delayed and new      | ransomware attack that         | icsstrive.com |
| 2025 -07-03 | Ingram Micro | USA | Transport | Ransomware |                      |                                |               |
|             |              |     |           |            | orders could not be  | affected order processing and  | blackfog.com  |
|             |              |     |           |            | processed            | other systems                  |               |
RH produces and distributes
commercial drone firmware
Русские Хакеры  Russian army could  hacked / modified for Russian
– Фронту /  Discrete  not configure ~500  military use. The attack  icsstrive.com
| 2025 -07-04 |     | Russia |     | Nation State |     |     |     |
| ----------- | --- | ------ | --- | ------------ | --- | --- | --- |
Gaskar  Mfg new drones / day for  impaired servers & terminals  tufts.edu
|     | Group / RH |     |     |     | several days | used to install the modified  |     |
| --- | ---------- | --- | --- | --- | ------------ | ----------------------------- | --- |
firmware at ~400 sites, not the
firmware itself.
|     |           |     |           |     | Shut down factory  | Qilin ransomware shut down  | icsstrive.com |
| --- | --------- | --- | --------- | --- | ------------------ | --------------------------- | ------------- |
|     | Wibaie à  |     | Discrete  |     |                    |                             |               |
2025 -07-09 Cholet France Mfg Ransomware with 600 employees  the window & door  france.fr
|     |     |     |     |     | for 10 days | manufacturer | france.fr |
| --- | --- | --- | --- | --- | ----------- | ------------ | --------- |
NovaBev announced that
Food &  Customer shipments  ransomware had hit its IT  icsstrive.com
2025 -07-16 NovaBev Russia Beverage Ransomware delayed 2 days network delaying shipments  scmagazineuk.com
but not affecting production.
|     |     |     |     |     |     | A cyber attack on the food &  | icsstrive.com |
| --- | --- | --- | --- | --- | --- | ----------------------------- | ------------- |
Suspended food &
|             | Colabor  |        | Food &  |         |                     | other goods wholesaler  | colabor.com |
| ----------- | -------- | ------ | ------- | ------- | ------------------- | ----------------------- | ----------- |
| 2025 -07-20 |          | Canada |         | Unknown | other shipments up  |                         |             |
Foods Beverage to 2 weeks disrupted order processing and  lapresse.ca
|     |     |     |     |     |     | impaired ability to ship product | reddit.com |
| --- | --- | --- | --- | --- | --- | -------------------------------- | ---------- |
22002266  OOT TC yCbyebre rT hTrheraeta tR eRpeoprotrt

Attacker
| Date | Victim | Region | Industry |     | Consequence | Summary | References |
| ---- | ------ | ------ | -------- | --- | ----------- | ------- | ---------- |
Type
"Silent Crow" pro -Ukrainian
|     |     |     |     |     | 50 flights cancelled  |     | icsstrive.com |
| --- | --- | --- | --- | --- | --------------------- | --- | ------------- |
2025 -07-28 Aeroflot Russia Transport Hacktivist and 10 delayed hackers claim to have erased  reuters.com
7,000 IT servers
Delays clearing
imported containers
and increased
An attack on the ICT platform
|     | Nigeria  |     |     |     | demurrage charges  |     | icsstrive.com |
| --- | -------- | --- | --- | --- | ------------------ | --- | ------------- |
of Nigeria customs service
2025 -08-14 Customs  Nigeria Transport Unknown for shippers for  maritimecybersecurity.nl
Service storing containers  delayed cargo clearance  vanguardngr.com
operations.
during customs
clearance
operations.
Attackers gained control of an
Shut down power
HMI - not clear if it was main
|     | Tczew Hydro  |     | Electric  |     | production at a  |     | icsstrive.com |
| --- | ------------ | --- | --------- | --- | ---------------- | --- | ------------- |
2025 -08-19 Poland Hacktivist HMI or engineering tool  - and
Plant Power small hydro power  changed settings causing  cybernews.com
plant
turbine and generator to stop.
All plants shut down
|     |     |     |     |     | for up to 5 weeks     | Social engineering & phishing  |     |
| --- | --- | --- | --- | --- | --------------------- | ------------------------------ | --- |
|     |     |     |     |     | and full production   | stole credentials to           |     |
|     |     |     |     |     | did not resume until  | compromise IT network. With    |     |
icsstrive.com
2025 -08-31 Jaguar /  UK Discrete  Ransomware mid-November.  SAP shut down, everything  bbc.com
LandRover Mfg Reported $900B  stopped  - could not auto -order
hackers4u.com
|     |     |     |     |     | direct losses with up  | parts, etc. Attributed to  |     |
| --- | --- | --- | --- | --- | ---------------------- | -------------------------- | --- |
|     |     |     |     |     | to $2.5B estimated     | "Scattered Lapsus"         |     |
|     |     |     |     |     | losses for the entire  | ransomware group.          |     |
UK economy.
Few details beyond that a
Process  All NA & SA plants  cyber attack shut down  icsstrive.com
2025 -09-02 Bridgestone Japan Unknown shut down for 16  industrialcyber.co
|     |     |     | Mfg |     |      | operations at NA & Latin  |                |
| --- | --- | --- | --- | --- | ---- | ------------------------- | -------------- |
|     |     |     |     |     | days |                           | cyberpress.org |
American plants
Shipping, receiving,
|     |     |     |     |     | manufacturing,  | Attackers accessed the firm  | icsstrive.com |
| --- | --- | --- | --- | --- | --------------- | ---------------------------- | ------------- |
Discrete
2025 -09-16 Data I/O USA Unknown production and  via a vulnerability in a third - sec.gov
Mfg
|     |     |     |     |     | other functions  | party firewall service provider. | yahoo.com |
| --- | --- | --- | --- | --- | ---------------- | -------------------------------- | --------- |
down for 3 weeks
Flights delayed and
|     |          |     |     |     |                       | Ransomware crippled vMUSE  | icsstrive.com |
| --- | -------- | --- | --- | --- | --------------------- | -------------------------- | ------------- |
|     | Collins  |     |     |     | cancelled in several  |                            |               |
2025 -09-19 USA Transport Ransomware check -in and boarding  bbc.com
|     | Aerospace |     |     |     | European airports  | software | airport.de |
| --- | --------- | --- | --- | --- | ------------------ | -------- | ---------- |
for 10-16 days
German production
A cyber attack shut down at
|     |     |     | Food &  |     | reduced or shut  |     | icsstrive.com |
| --- | --- | --- | ------- | --- | ---------------- | --- | ------------- |
2025 -09-24 Refresco Germany Beverage Unknown down at least two  least German plants of the  lebensmittelzeitung.net
beverage bottler
days
Most of 30 plants
|     |     |     |     |     | shut down for a  | Asahi recovery was slowed by  | icsstrive.com |
| --- | --- | --- | --- | --- | ---------------- | ----------------------------- | ------------- |
Asahi Group  Food &  week. Shipments  large numbers of very old
| 2025 -09-30 |     | Japan |     | Ransomware |     |     | securityweek.com |
| ----------- | --- | ----- | --- | ---------- | --- | --- | ---------------- |
Holdings Beverage only at 10% of  systems  - both IT and OT  - left
japantimes.co.jp
|     |     |     |     |     | normal a month  | over from years of acquisitions. |     |
| --- | --- | --- | --- | --- | --------------- | -------------------------------- | --- |
after the incident
Hacktivists compromised PA
systems in a number of
|     |          |     |     |     | Two flights were  | Canadian and US airports with  |               |
| --- | -------- | --- | --- | --- | ----------------- | ------------------------------ | ------------- |
|     | Kelowna  |     |     |     |                   |                                | icsstrive.com |
2025 -10-14 Canada Transport Hacktivist delayed by several  political messages praising
|     | Airport |     |     |     |       |                          | ctvnews.ca |
| --- | ------- | --- | --- | --- | ----- | ------------------------ | ---------- |
|     |         |     |     |     | hours | Hamas. Only one airport  |            |
reported associated flight
delays.
"IT Army of Ukraine" took credit
|     |     |     |     |     |     | for a DDoS attack halted VetIS  | icsstrive.com |
| --- | --- | --- | --- | --- | --- | ------------------------------- | ------------- |
2025 -10-22 Rossel - Russia Food &  Hacktivist Food shipments  (Mercury) and Saturn tracking  securityaffairs.com
|     | khoznadzor |     | Beverage |     | halted for one day |                               |                    |
| --- | ---------- | --- | -------- | --- | ------------------ | ----------------------------- | ------------------ |
|     |            |     |          |     |                    | systems used to register the  | beyondmachines.net |
movement of animal products
|     | Unspecified  |     |     |     |     | Canadian government alert  |     |
| --- | ------------ | --- | --- | --- | --- | -------------------------- | --- |
does not give details, but
|             | Canadian  |        | Water &    |            | "Degraded service"  |                                | icsstrive.com |
| ----------- | --------- | ------ | ---------- | ---------- | ------------------- | ------------------------------ | ------------- |
| 2025 -10-29 |           | Canada |            | Hacktivist |                     | states a cyber attack          |               |
|             | Water     |        | Wastewater |            | for the community   |                                | cyber.gc.ca   |
|             | Utility   |        |            |            |                     | tampered with water pressures  |               |
resulting in degraded service
22002266  OOT TC yCbyebre rT hTrheraeta tR eRpeoprotrt

Attacker
| Date | Victim | Region Industry |     | Consequence | Summary | References |
| ---- | ------ | --------------- | --- | ----------- | ------- | ---------- |
Type
The automotive suspension
manufacturer reported two
|     |     |     |     | Factory in Japan   | factory outages due to     |               |
| --- | --- | --- | --- | ------------------ | -------------------------- | ------------- |
|     |     |     |     | shut down for one  | ransomware but noted that  | icsstrive.com |
2025 -10-31 Tein Inc. Japan Discrete Mfg Ransomware day, Chinese factory  backlogs would be cleared  tein.co.jp
|     |     |     |     | shut down for one  | by using overtime and holiday  | linkedin.com |
| --- | --- | --- | --- | ------------------ | ------------------------------ | ------------ |
|     |     |     |     | week               | work. The "Warlock"            |              |
ransomware group claimed
credit for the attack.
Criminals encrypted parts of
the IT environment. An
2025 -11-28 Gerd Bär  Germany Discrete Mfg Ransomware 2 factories shut  announcement 7 days later  icsstrive.com
GmbH down for 7 days indicated that "production is  cargolift.com
back up and running". Few
other details were released.
Aras Kargo's press release
|     |     |     |     |     | said that there were short - |     |
| --- | --- | --- | --- | --- | ---------------------------- | --- |
term delays and service
|             |            |                  |         | All parcel pick -up  | interruptions. Independent  | icsstrive.com    |
| ----------- | ---------- | ---------------- | ------- | -------------------- | --------------------------- | ---------------- |
| 2025 -11-30 | Aras Kargo | Turkey Transport | Unknown | and delivery were    |                             |                  |
|             |            |                  |         |                      | press reported a complete   | araskargo.com.tr |
halted for one day
cessation of pick -ups and
deliveries for roughly one
day.
The state -run oil firm
detected a ransomware
attack days earlier, but the
AV software it used to try to
Stopped loading oil
|     |     |     |     |     | fix the problem "affected" its  | icsstrive.com |
| --- | --- | --- | --- | --- | ------------------------------- | ------------- |
2025 -12-14 PDVSA Venezuela Oil & Gas Ransomware on to tankers at 10+  entire administrative system.  marinelink.com
ports
By Dec 17 ports had started
making manual records of
deliveries to avoid a longer
suspension of exports.
Customers of Evergreen
Printing Company in Belmawr,
NJ reported that the
Evergreen  Suspended printing  company had suspended  icsstrive.com
2025 -12-19 Printing  USA Pup & Paper Ransomware operations for 4+  printing because of a  theretrospect.com
|     | Company |     |     | days | ransomware attack. There is  | dysruptionhub.com |
| --- | ------- | --- | --- | ---- | ---------------------------- | ----------------- |
no record of a public
statement by the company
about the attack.
Pro-Russian group
Noname057 claimed credit
|     |     |     |     | Home delivery of  | for a DDOS attack that  | icsstrive.com |
| --- | --- | --- | --- | ----------------- | ----------------------- | ------------- |
2025 -12-22 La Poste France Transport Hacktivist parcels was  affected deliveries. Deliveries  therecord.media
|     |     |     |     | disrupted for 4 days | were slowed because of an  | lapostegroupe.com |
| --- | --- | --- | --- | -------------------- | -------------------------- | ----------------- |
impaired parcel tracking
capability.
22002266  OOT TC yCbyebre rT hTrheraeta tR eRpeoprotrt

| Appendix B  | –   |  Sources |     |     |     |     |     |
| ----------- | --- | -------- | --- | --- | --- | --- | --- |
The  authors  thank  and  acknowledge  the  many  incident  repositories  and  reports  we
searched  to find  the  incidents  reported  in the  2025  data  set .
| ICS STRIVE |     |     | https://icsstrive.com                 |            |     |         |              |
| ---------- | --- | --- | ------------------------------------- | ---------- | --- | ------- | ------------ |
|            |     |     | https://cow                           | -prod -www | -   |         |              |
| CERT -EU   |     |     | v3.azurewebsites.net/publications     |            |     |         |              |
|            |     |     | /threat -intelligence/2025            |            |     |         |              |
| Checkpoint |     |     | https://research.checkpoint.com/2025/ |            |     |         |              |
|            |     |     | https://cloudian.com/ransomware       |            |     | -attack | -list -and - |
Cloudian
alerts/
|     |     |     | https://cybersecurityventures.com/ransomware |     |     |     | -   |
| --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
Cybercrime Magazine
report
CyberEvents Global Cyber Threat
https://cybereventsdatabase.org/dashboard
Landscape
| Cyber Security Incident Database |     |     | https://www.csidb.net/    |     |     |     |     |
| -------------------------------- | --- | --- | ------------------------- | --- | --- | --- | --- |
| DysruptionHub                    |     |     | https://dysruptionhub.com |     |     |     |     |
European Repository of Cyber
https://eurepoc.eu
Incidents
|     |     |     | https://konbriefing.com/en |     | -topics/cyber | -   |     |
| --- | --- | --- | -------------------------- | --- | ------------- | --- | --- |
KonBriefing
attacks.html
Security & Exchange Commission https://www.sec.gov/edgar/search/
NHL Stenden University of Applied
Sciences, MCAD Maritime Cyber  https://maritimecybersecurity.nl/listview
Attack Database
| TI Safe          |                                            |     | https://hub.tisafe.com/base |     | -de-dados/ |     |     |
| ---------------- | ------------------------------------------ | --- | --------------------------- | --- | ---------- | --- | --- |
| Published March  | 2026                                       |     |                             |     |            |     |     |
| Copyright ©      | 2026  by Waterfall Security Solutions Ltd. |     |                             |     |            |     |     |
Disclaimer : While  we endeavor  to ensure  that  the information  in this  report  is correct,  neither  Waterfall
Security  Solutions  Ltd,  nor ISSSource,  nor the individual  authors  (all  collectively  referred  to hereinafter
as the PROVIDERS  of this  report)  make  any  warranties  nor representations  about  the accuracy  nor
completeness  of the material  in this  report . The PROVIDERS  expressly  disclaim  liability  for errors  and
omissions  in the contents  of this  report . Readers  should  seek  appropriate  advice  before  proceeding  on
| the basis  of any |  information |  presented  here | .   |     |     |     |     |
| ----------------- | ------------ | ---------------- | --- | --- | --- | --- | --- |
22002266  OOT TC yCbyebre rT hTrheraeta tR eRpeoprotrt