GRIT
Ransomware
Report2023 ANNUAL REPORTContentsAnnual Ransomware Summary2023 Ransomware Activity 
by the numbers2023 Threat Group BreakdownRansomware in Depth: Major Events, 
Observations, and Trends in 2023Signposts of Ransomware Activity 
and 2024 OutlookFinal ThoughtsAppendixMethodologyData collected for this report was obtained from publicly available resources, includinginformation disclosed by threat groups themselves, and has not been validated by allalleged victims. As such, the number of publicly observed attacks and the actual number ofattacks conducted may not be equal. Some groups do not publicize all of their victims, andalmost all groups offer an option to withhold announcement if the victim pays a ransomwithin a specified timeframe or will remove posted details of the victims once a ransom hasbeen paid. Additionally, some groups include incomplete information about their victim orclaim an attack despite having successfully attacked only a small subset of their target. Forthese reasons, the data in this report is useful in aggregate, but should be evaluated as areport consisting of data sources that have variability. Despite this variability, we stillconsider this report as an accurate representation of the ransomware threat landscape.We note that this report includes data and analysis of several groups that may be betterdescribed as "extortion" groups rather than "ransomware" groups. These groups mayeschew encryption and instead focus only on data exfiltration and extortion, or may notperform intrusion operations of any kind, instead extorting or re\-extorting organizationsbased on historically compromised data. While these groups do not deploy ransomware,we are including them in our reporting due to their relationships with other ransomwaregroups and their impact on the extortion\-based cybercrime environment.In keeping with best practices in analytic tradecraft, we have we have made efforts toclearly distinguish between our assessments and the underlying factual evidence whichsupports it. Statements beginning with or containing the words we assess should beconsidered analytic judgments based on the expertise and experience of GRITs analystscoupled with the strength and corroboration of underlying sources. Statements ofprobability such as likely, almost certainly, and probably reflect levels ofconfidence in an analytic assessment based on the strength and corroboration ofunderlying sources. Unlikely and similar terms reflect low confidence, likely andprobably reflect moderate confidence, and almost certainly reflect high confidencewithin the scope of this report.ANNUAL
Ransomware SummaryIn last years Annual Ransomware Report, GRIT identified ransomware as "the most prolific andimpactful threat to our networks, data, and operational capabilities," with more than 2,500 publiclyposted victims observed in 2022\. While we predicted a continuing steady increase in ransomwareactivity, 2023 outpaced our expectations, with year\-over\-year victim volume nearly doubling,driven in part by multiple mass exploitation campaigns impacting hundreds of organizations.In total, we observed 63 distinct ransomware groups leverage encryption, data exfiltration, dataextortion, and other novel tactics to compromise and publicly post 4,519 victims across all 30 ofGRIT's tracked industries, and in 120 countries.Relative to the remainder of the year, Ransomwares operational tempo in 2023 began slowly, 
with a progressive increase in victim posting building up to a record high of 1,353 victim posts inQ3, followed by a comparatively mild 1,170 victim posts in Q4\. As Q4's drop\-off does not appearto correlate with any significant changes in the ransomware ecosystem, results from January2024 may yet show whether victim volume will decrease, remain constant, or return to form byincreasing in the new year.Key HighlightsThe United States was by far the most impacted country in 2023\. Among posted victims, 2,199were US\-based organizations, accounting for 49% of all observed ransomware attacks in 2023\.Eight out of the ten most impacted countries were within North America and Europe, with Braziland Australia as the sole outliers. The same "top ten" most impacted countries were home to76% of all observed victim organizations, of which 27% impacted non\-US countries.From an industry perspective, GRIT observed most impacts affecting a limited subset ofindustries. 62% of all observed victims belong to one of the "top ten" most\-impacted industries,with Manufacturing and Technology remaining the two most\-impacted industries; Manufacturingand Technology represented 12\.9% and 7\.9% of all victims, respectively.In line with GRIT's taxonomy for classifying ransomware groups, long\-term Established groupsaccounted for the overwhelming majority of observed victims (85%), followed by Developinggroups (10%). Ephemeral and Emerging groups, as the newest and shortest\-term entrants, laggedbehind their maturing counterparts but still posed a significant threat to worldwide organizations,exacerbated by less "reliable" actors and frequently recycled malware. We note that for 2023, wehave attributed only one Rebrand group in Black Suit, stemming from the now inactive Establishedgroup, Royal. Conversely, we have not definitively attributed any Splinter groups in 2023, thoughgroups that we currently classify as Emerging or Ephemeral may, in time, show indications ofhaving Splintered from other organizations.ANNUALRansomware Summary (contd)Tactically, 2023 presented repeated opportunities for new entrants in the ransomwareecosystem. This was achieved either through reduced technical barriers such as the recycling ofleaked ransomware builders and commodity malware, or the recycling of previously leaked data forre\-extortion and claims of attacks that never were. For those established groups with resourcesand technical expertise, exploitation of high\-severity and zero\-day vulnerabilities provided areliable means of exploiting victims at scale, a trend we assess as likely to continue into 2024 as ameans of overcoming improvements in security.Law enforcement disruptions and rumors thereof circulated the ransomware community in 
2023, culminating in a highly publicized takedown of Alphv's dark web leak site. Regrettably,Alphv chose not to go down without a fight, and its continued presence and operations highlight theresiliency of Ransomware's most entrenched groups. Targeting of victims previously considered"off limits, such as schools and hospitals, is expected to continue, as are attempts to attractadditional attention to high\-impact ransomware attacks. This brinksmanship, which aligns withseveral of the novel coercive techniques we observed in 2023, will likely attract the attention ofboth law enforcement and potential affiliates over time.Total Publicly Posted Ransomware VictimsNumber of Tracked Ransomware GroupsAverage Posting Rate (per day)4,5196312\.42023 Ransomware Activity 
by the NumbersActivity ramped up considerably throughout Q1 into Q2, then held steady at around 100\-
140 posted victims per week for the remainder of 2023, with the exception of observable 
decreases in early August and October. An observable increase in victim volume in early 
September stems from a large "dump" of victim postings by the groups RansomedVC 
and Cactus.Substantial increases in victim volume can be observed in March, June, and July following 
Clop's mass exploitation campaigns that impacted enterprise users of two distinct 
managed file transfer applications.302520151050200150100500JanFebMarAprMayJunJulAugSepOctNovDecTotal PostsAverage Posts WeekTotal GroupsAverage Groups Week4,51986\.96316\.6Victim Posting Rates per Quarter16001400120010008006004002000Q1Q2
202120222023Q3Q4Most Impactful Ransomware Threat Groups \- 2023NoEscapeRoyalMedusaAkiraBianlian8BasePlayClopAlphvLockBit0200400Q1Q2600
Q3Q480010001200A quarterly breakdown of 2023's data shows a consistent and significant uptick in the volume 
of victims posted relative to the two preceding years. Emblematic of this increase, Q3 of 2023 
resulted in a higher volume of victim postings than the Q3 totals of 2021 and 2022 combined.The rate of publicly posted ransomware victims from 2021 to 2022 saw a 4\.2% decrease in 
activity year over year. Comparatively, from 2022 to 2023, ransomware victim posting 
increased by a staggering 80\.1%. While mass exploitation campaigns contributed substantially 
to this large increase, such attacks contributed just over 5% of the total victims for 2023, 
demonstrating this year's significant increase in ransomware activity overall.Cumulative Victims by Threat Group \- 2023100%90%80%70%60%50%40%30%20%10%0%1\-Jan 1\-Feb 1\-Mar 1\-Apr 1\-May 1\-Jun 1\-Jul 1\-Aug 1\-Sep 1\-Oct 1\-Nov 1\-DecLockBitAlphvClopPlay8BaseBianlianAkira MedusaRoyal NoEscapeFollowing a slow close to 2022, LockBits activity surged considerably in the first quarter of 2023, and 
the group maintained a steady pace of operations throughout the year, even during periods when other 
groups were far less active. GRIT observed a slower summer from LockBit compared to their average, 
possibly indicating conflicts with affiliates, processes, or or infrastructure, consistent with problems 
described in open security reporting. This may have contributed to LockBits announcement in November, 
in which LockBit publicized a "policy" change that indicated the minimum acceptable ransom demand 
would be directly related to the victim organization revenue. Additionally, on November 15th, 2023, 
LockBit suffered an outage affecting all of its known Dark Web infrastructure. The issue was resolved 
later that day, with no indications as to what caused the outage.Including Clop's mass exploitation campaigns and the May 2023 bulk posting of victims by 8Base, 
LockBits share among the top 10 settled at 32% for the remainder of the year.The Established group Royal began the year with a high and consistent volume of victims before a 
precipitous drop in Q3, when their leak site went dark. The group is believed to have since Rebranded 
as "Black Suit", which began continuing operations in Q4\.Play, a group responsible for only around 1% of observed victims in 2022, quietly and significantly 
increased their operations to become the fourth\-most prolific group in 2023, in terms of observed victims.GRIT observed the 6th\- and 7th\-most victims from Bianlian and Akira, despite the publication of 
ransomware decryptors which would degrade the effectiveness of encryption as leverage. Both groups 
appear to have quickly pivoted to extortion based solely on exfiltrated data and have maintained a 
significant operational capacity.While retaining its place as the second\-most impactful ransomware group, Alphv earned significant media 
coverage this Fall after claiming breaches against MGM Resorts and Caesars International through an 
elaborate social engineering campaign conducted by the prominent threat group, Scattered Spider.Most Impacted Industries \- 2023
Interestingly, while Rhysida (Developing) was not a leading group in terms of total posted 
victims, coming in 13th amongst competing groups, the group caused disproportionate impacts 
on traditionally sensitive industries, including Education, Healthcare, and Government sectors. 
46 of Rhysida's 74 posted victims belong to one of these three industries.Among Manufacturing industry victims, the US was impacted five times as much as the next 
highest country, Germany. Specifically, the US saw 265 impacted Manufacturing victims, while 
Germany saw a significantly lower number of Manufacturing victims at 48\. Manufacturing was 
the most impacted industry for almost every month in 2023, excluding May, when it placed 
behind Technology by a single observed victim.The "top 10" most impacted industries accounted for 2,794 (62%) of all posted victims and 
were impacted by all but one of the groups tracked by GRIT Free Civilian, a group with only 
two posted Ukrainian victims in late January 2023\. Free Civilian, a self\-proclaimed pro\-Russian 
hacktivist group, has been reported as a Russian GRU persona by Microsoft and Mandiant. 
Given the typical diversity of impacted victims, limited victim diversity may serve as a future 
indicator for government\-sponsored faux\-ransomware operations.Alphv's status as one of the leading ransomware groups impacting the Healthcare industry may 
continue after their response to law enforcement efforts to shut down their operations. After 
restoring operations, Alphv announced a change to affiliate rules, allowing the targeting of 
critical infrastructure. This may lead less scrupulous affiliates to disproportionately target 
hospitals and other healthcare providers using Alphv's ransomware.7006005004003002001000M a n ufacturingT ec h n ologyH e althc areE d ucation
R etail \&W h olesaleB an king \& Fin a nceC onstructionLegalC onsultingTra nsp ortation1\- Manufacturing2\- Technology

LockBit
Alphv
Play

LockBit
Clop
Alphv3\- Healthcare


LockBit
Alphv
Bianlian4\- Education

LockBit

Rhysida

Akira5\- Retail \& Wholesale


LockBit
Play
AlphvGeographic Breakdown of 
Ransomware Victims (2023\)Most Impacted:1\. United States2\. United Kingdom3\. Canada4\. Germany5\. France6\. Italy7\. Australia8\. Spain9\. India10\. Brazil2023 Threat Group
BreakdownEstablished ransomware groups dominated the ransomware ecosystem when compared to 
less mature groups as classified in our taxonomy. Despite representing less than a third of 
all distinct observed groups operating during 2023, Established groups generated 
a disproportionately high victim volume.Established groups eventually ceded some of their dominant market share during Q4, with a 
greater portion of observed victims stemming from operations of Developing and Emerging 
groups. GRIT has previously observed a slight slowdown in the operations tempo of 
Established groups over the preceding two years. A portion of the decrease in activity could 
also potentially be attributed to law enforcement's temporary disruption of the Established 
group Alphv in December 2023\.Only one group, Black Suit, was classified as a Rebrand during 2023, whose victims account 
for a minute subset of the overall 2023 data. While other groups may be later determined by 
GRIT to be Rebrands or Splinter groups, only Black Suit's Rebrand was sufficiently attributable.Post Rates per Month6005004003002001000JanFebMarAprMayJunJulAugSepOctNovDecEstablishedDevelopingRebrandEmergingEphemeral2023 Activity by GRIT Taxonomy ClassificationGRIT Taxonomy
Group TypeDays Active in 2023 
(Across All Groups)EstablishedRebrandDevelopingEphemeralEmerging353141601019The number of days in which each group type was active in 2023 paints a clear picture ofthe distinction between them within GRIT's taxonomy. Days active was measured by thenumber of distinct dates on which each group type updated their data leak sites withadditional victims.Established groups, which most frequently follow the Ransomware\-as\-a\-Service model,generally have multiple affiliates acquiring victims at any given time, which allows them topost a near\-continuous flow of victims to their data leak sites. Such groups also possessgreater resources and staffing, which could support more timely and frequent updates.Ephemeral groups, by contrast, are short\-lived, resulting in minimal victim postings overshort periods of time, as indicated by their minimal activity on data leak sites.Developing groups defined by GRIT's taxonomy as nascent groups focused on evolution,improvement, and TTP refinement have demonstrated continuing operations and the abilityto generate a consistent stream of victims. While not as well\-resourced or entrenched asEstablished groups, we still expect to see higher levels of activity from these groups thanshort\-term Ephemeral groups or newly arrived Emerging groups. The observable days ofactivity for Developing groups support this definition, presenting a substantial level of activitysecond only to Established groups.Industry Victims by Taxonomy ClassificationEstablishedEmergingVictim IndustryNumber of Public VictimsVictim IndustryNumber of Public VictimsManufacturingTechnologyHealthcareBanking and FinanceRetail and WholesaleDeveloping440274158213205GovernmentManufacturingEntertainment, 
Hospitality, \& TourismHealthcareTechnologyEphemeral1311885Victim IndustryNumber of Public VictimsVictim IndustryNumber of Public Victims5337353025ManufacturingConsultingLegalConstructionEducation126655ManufacturingHealthcareEducationTechnologyConstructionRebrandVictim IndustryGovernmentManufacturingEntertainment, Hospitality, and TourismHealthcareRetail and WholesaleNumber of Public Victims131188205Emerging groups were the only group type with Government amongst their most victimized industries, 
and Government victims were, in turn, the most impacted by Emerging groups. Emerging groups may 
be entirely new to the ransomware ecosystem and select targets differently than more mature groups, 
who may avoid government targets to avoid undesired attention from law enforcement.Healthcare targets rose in popularity among both Established and Developing groups in 2023\. 
Healthcare victims often hold a large amount of PII data, rendering them a high\-value target for more 
mature ransomware groups capable of exploiting or extorting based on large volumes of data. While 
the Healthcare industry was once considered off\-limits and less frequent as targets by Established 
groups, we have witnessed this norm eroding in 2023\.Manufacturing remains one of the most highly victimized industries across most group categories. This 
is likely driven in part by cybersecurity challenges within manufacturing organizations, as well as the 
fact that these organizations often suffer significant costs from operational disruption of manufacturing 
processes, potentially rendering them more likely to pay ransoms in support of a fast recovery.Industry Victims by Taxonomy ClassificationRelative to their share of the ransomware ecosystem, Developing and Emerging groups 
disproportionately impacted Healthcare organizations more often than Established groups. 
Healthcare has historically been considered off limits for some ransomware programs as this 
brings negative press coverage and extra attention from law enforcement agencies. Despite 
this, Established groups saw a relative increase in Healthcare victims from the previous year.Emerging groups disproportionately victimized organizations within the Retail and Wholesale 
industry an industry whose market value increased from $71\.8 Billion to $77\.2 Billion, 
according to the Business Research Company. This 7% increase in market value, coupled 
with a propensity for weaker cybersecurity postures among mid\-size organizations, could 
make this industry a more appealing target for ransomware groups.Manufacturing consistently remains the most affected industry across all group classifications. 
Over 20% of victims belong to the manufacturing industry across all group classifications 
except Emerging groups.RebrandEphemeralEmergingDevelopingEstablished0%20%40%60%80%100%ManufacturingTechnologyHealthcareEducationRetail and WholesaleBanking and FinanceConstructionLegalConsultingTransportationGeographic Victims by Taxonomy ClassificationEstablishedDevelopingGeographic Victims by Taxonomy Classification (contd)EmergingEphemeralTop 5 Countries By Taxonomy ClassificationThe United States was the most impacted country across all group classifications, 
reflecting its status as an attractive target for ransomware groups from inception 
through maturity. This is likely due to the perception of victim organizations in 
the US as more likely to pay ransoms and the profit\-maximizing nature of 
ransomware operations.Emerging and Ephemeral groups appear to target more victims outside of the 
Global North, potentially limited by language barriers or technical proficiency, or 
to maintain a lower profile while beginning operations. As groups progress across 
the maturity spectrum, victim concentration appears to shift towards North 
American and Western European targets.Established1\. United States2\. United Kingdom3\. Canada4\. Germany5\. FranceRebrand1\. United States2\. Germany3\. CanadaEphemeral1\. United States2\. Italy3\. Canada4\. United Kingdom4\. Argentina5\. Australia5\. GermanyDeveloping1\. United States2\. United Kingdom3\. Germany4\. Italy5\. CanadaEmerging1\. United States2\. Canada3\. Italy4\. Jamaica5\. Netherlands5\. United KingdomRansomware in Depth: 
Major Events, Observations, and Trends in 2023Throughout 2023, GRIT hypothesized that the price of Bitcoin may correlate with ransomware 
victim posting rates. As we closed out the year, we examined the year's complete data to 
validate or refute this hypothesis.A cursory review of victim posts and Bitcoin prices across weekly intervals in 2023 reveals two 
possible focal points. The first is the general trend of an overall rise of Bitcoin value appearing to 
correlate with an increase in ransom victim posts during the first three months of the year, along 
with a steady increase in ransomware reports.The second is an observable and dramatic shift between the rise of Bitcoin value in contrast with 
a decline in victim reports from October until the end of the year.Rate of Posted Ransomware Victims vs Price of Bitcoin in USD (2023\)Rate of Posted Ransomware Victims vs Price 
of Bitcoin in USD, Outliers Removed (2023\)Methodically structuring our data painted a clearer picture and allowed us to better view 
trends with less noise. Firstly, Clops mass exploitation campaigns resulted in the posting of 
54 different victims at one time on March 18\. This mass exploitation campaign is abnormal 
and skews the data that would otherwise be indicative of overall operational tempo. Similarly, 
the Developing group 8Base debuted their data leak site on May 23rd, with 66 victims posted 
simultaneously. Those victims were almost certainly acquired throughout the preceding 
months, likewise, skewing our data. These victims were removed from the associated graph
to better demonstrate the overall trend in ransomware operational tempo during 2023\.We calculated a 4\-day period simple moving average to better normalize victim post data and 
account for variances between dates of initial compromise and the date of a victim's post to a 
group's site.Comparing this moving average with the price of Bitcoin, a much stronger correlation can be 
observed between posting rates and Bitcoin value. Supporting this observable correlation 
through data, we see a correlation coefficient of .565, demonstrating a moderate correlation. 
Limiting our focus to just the data from January through September before October's drop 
further yields a 0\.747 correlation coefficient, reflecting a strong correlative relationship 
between victim post rates and Bitcoin value over time.Rate of Posted Ransomware Victims vs Price 
Rate of Posted Ransomware Victims vs Price 
of Bitcoin in USD, Outliers Removed (2023\)
of Bitcoin in USD, Outliers Removed (2023\) (contd)In reviewing the decreased correlation from October through the end of the year, we 
considered the root cause and the drivers of our hypothesis, searching for potential 
explanations. While we cannot conclusively rule out other drivers, we note that Bitcoin value 
surged during this time period, driven by announcements that the US Securities and Exchange 
Commission (SEC) may approve Bitcoin futures exchange\-traded funds (ETF), which would 
provide a path for investors to purchase Bitcoin and Bitcoin derivatives through stock market 
exchange services.Although we cannot affirm the motivations and drivers of individual ransomware actors, we 
note our findings as potentially suggestive of ransomware group activity increasing with 
interest in Bitcoin procurement over time, with increased activity correlating a moderate to 
high amount during periods of value growth in the cryptocurrency. We observed a similar 
correlation between the price of Bitcoin and the posting rates of ransomware groups during 
our 2022 ransomware report, which strengthens our assessment of a relationship between 
the two data sets, as this now appears to be a year\-over\-year trend. The dataset in 2022 did 
not experience the end\-of\-the\-year separation between the trendlines as did 2023s data.We note and acknowledge that we lack insight into the number of ransomware victims that 
pay ransoms across the year and that the addition of such data may substantially impact or 
change our findings.Major Events in Ransomware:
2023 at a GlanceJanuary 16
Bianlian 
Decryptor 
ReleasedMarch 29
3CX Supply 
ChainAugust 29
Qakbot 
DisruptedOctober 7
Reignition of Israel \-
Palestine ConflictDecember 19
Alphv DisruptionFebruary 8
Clop's 
GoAnywhere 
CampaignJune 1
Clop's MOVEit 
CampaignSeptember 18
Scattered 
Spider Casino 
AttacksDecember 15
New SEC 8\-K 
Rules Take EffectMajor Events in Ransomware:
Clops MOVEit CampaignClop's mass exploitation of Progress Software's MOVEit managed file transfer software impactedhundreds of victims across multiple industries in a lightning campaign, with impacts continuingthroughout the Summer. The incident would go on to become one of the most reportedcybersecurity stories of the year, with reporting providing information ranging from technical detailsof the exploit through to the ensuing fallout and data publication. Notably, the campaign mirrorsearlier Clop mass exploitation campaigns, with the group executing an elaborate, coordinated planto exploit previously unknown vulnerabilities, resulting in data theft and extortion for profit.The patience and planning demonstrated by the group in this case and other mass exploitationcampaigns that rely on "zero\-day" vulnerabilities are crucial to maximizing impact and revenueextraction before an associated vulnerability can be discovered and patched. To support Clop's "allat once" approach to exploitation, the group automated and tested a process that would extract allavailable data held by victim companies that ran the impacted application exposed to the internet.As the operation came to light in early June, Clop updated their data leak site with a genericmessage inviting anyone who believed that they might have been affected to reach out to them toprevent the publication of sensitive data collected in the campaign. This approach likely reducedthe time burden of contacting individually impacted victims and initial communications unlikely tolead to settlement.While the group worked through any ensuing negotiations with victims and began posting the dataof non\-compliant organizations to their data leak site, they very likely encountered issues withhosting the substantial amount of exfiltrated data on their existing infrastructure, facing limitationsof the onion protocol, which hosted their site and the illegal nature of the data's possession. Withnecessity as the mother of invention, Clop would go on to experiment with alternative hostingstrategies with varying levels of success. The group tried uploading data on a per\-victim basis toclearnet sites hosted on domains directly naming the victim. This approach gained headlines, butthe process was likely deemed too resource\-intensive for Clop, who ultimately only used thisapproach on a handful of victims.As an alternative strategy, the group also hosted victim data in a series of Torrent files. Thisstrategy leveraged the inherently distributed nature of the Torrent protocol to make a morereliable, albeit significantly slower, solution to sharing stolen data. These actions by Clop 
demonstrate the difficulty of pulling off a true successful mass exploitation campaign, includingmanaging "long tail" logistical considerations such as data storage. In spite of early issues, theincident would go on to be considered one of if not the largest single incident of data theft inhistory. Should mass exploitation campaigns spread as a tactic to other threat groups, Clop mayprove to be a model for this style of attack and associated scale.Major Events in Ransomware:
Scattered Spider attacks Major CasinosIn September 2023, two of the largest entertainment companies in the country, MGM Resorts 
International and Caesars Entertainment, confirmed downtime caused by ransomware 
attacks. As details emerged, the two attacks seemed to share a common thread, a connection 
with a threat group and new affiliate of Alphv, referred to as Scattered Spider by security 
researchers. Alphv called public attention to the attack by posting a diatribe to their data leak 
site in an attempt to place pressure on MGM after they refused payment. After weeks of 
downtime, MGM reported that their losses in this single attack would exceed $100 million 
USD. Unconfirmed details also emerged about the method of ingress for both the MGM and 
Caesars attacks; both were said to be a result of social engineering by Scattered Spider, 
which is known for its skill in English\-language social engineering to circumvent Identity 
and Access Management.A frequent tactic in this space, and one employed by Scattered Spider in the past, is 
breaching network accounts via calls to an organizations help desk. Threat actors, armed 
with information about an employee obtained from LinkedIn and a convincing story, aim to 
exploit established account recovery processes to gain access to privileged user accounts at 
a target organization. Social engineering tactics are as effective as they are hard to detect, 
and the strongest prevention for such attacks is policy and training both human elements 
attempting to compensate for technological gaps. Of course, social engineering as a method 
of initial access is not new to ransomware actors. Phishing, which is also considered a form of 
social engineering, continues to pose a threat to every organization with an email presence. 
However, as email filtering technology improves and users become more knowledgeable, their 
impact is often limited. Ransomware groups seem to have adjusted to these headwinds, but 
actors like Scattered Spider show there is still a potential for large\-scale compromises via 
exploitation of the human attack surface.Major Events in Ransomware:
LockBits new Affiliate RulesIn September, LockBit, the most prolific ransomware group of 2023, announced a new setof affiliate rules regarding the negotiation of ransoms with future victims. These new rules,which the group presented in a poll earlier in the year to collect affiliate feedback,implemented significant guardrails around how individual affiliates may price and negotiateransoms. The new rules first define a sliding scale based on the victims revenue todetermine how high an affiliate must set their initial extortion demand. Furthermore, oncethe initial demand is calculated, the new rules forbid affiliates from negotiating discounts inexcess of 50%. These actions are seemingly motivated by a reduction in ransom payments,a trend that could ultimately affect LockBit leaderships revenue. LockBit seems to havemade these new rules effective starting October 1\.Major Events in Ransomware:
SEC Updates Guidance on incident notificationsOn July 26th, 2023, the US Securities and Exchange Commission (SEC) announced newrules regarding the disclosure of material cybersecurity incidents experienced by publiccompanies. The new rules, which were made effective December 18, 2023, provideguidance around how quickly a victimized organization must notify the public andshareholders of a cybersecurity incident. Specifically, public companies now must file anSEC Form 8\-K with details of the incidents nature, scope, and timing within four days of itbecoming material. These new rules have already significantly influenced howorganizations respond to ransomware and other forms of cybersecurity attacks.In the past, public companies have provided notice to shareholders about cyberattacks forthe purpose of informing them about potential impacts to the organizations bottom line.With the advent of the new SEC rule, companies are forced to provide notice on a shortertimeline and in greater detail. Ultimately, this puts added pressure on organizationsaffected by ransomware to identify materiality of a given breach; the new notificationrequirements provide protection for both shareholders and individuals who may havepersonal data compromised. By shedding light on incidents that might otherwise beconcealed, the new SEC rule aims to bring more accountability to organizations victimizedby ransomware.Major Events in Ransomware:
Law Enforcement Disruption of AlphvStarting as early as December 8th, 2023, and culminating in a seizure message posted to their 
data leak site on December 15th, several arms of United States and international law enforcement 
cooperated to disrupt the Alphv, also known as Black Cat, Ransomware\-as\-a\-Service (RaaS) 
operation. The main impact to the group was the seizure of private keys for over 900 Tor sites 
operated by Alphv, leading to their eventual shutdown and takeover. In addition, law enforcement 
was able to capture decryption keys for around 500 recent victims of the RaaS group, meaning 
that any organizations affected by the group in a several\-month timespan could potentially 
recover their encrypted data without cooperating with Alphv.The disruption immediately sent shockwaves throughout the cybersecurity industry. While many 
celebrated the apparent takedown, Alphv quickly attempted to restore their operations. The law 
enforcement actions against the group have not yet resulted in arrests ofAlphv affiliates or 
leadership, leaving Alphv operators to remain active. Several hours after the Alphv data leak site 
was changed to a law enforcement seizure notice, the site changed again, this time to a message 
from Alphv. This unseizure, appears to have occurred as a result of Alphv maintaining access to 
the keys needed to update the content served by the groups Onion URL. The resulting message 
from Alphv, written fully in Russian, taunted law enforcement and advised their affiliates that 
they remained unscathed.The group pointed visitors to a new Tor site, not under the control of law enforcement, and defined 
several new rules for operations going forward. Primarily, the group dramatically changed their 
payment structure for affiliates, who would now receive 90% of any ransom payments they 
generate. This change was likely motivated by the need to prevent a departure of affiliates who no 
longer trust the group following the law enforcement seizure. The 90% affiliate share offered by 
Alphv also contrasts with Lockbits stated shares of 60\-80% \- most likely an attempt to motivate 
affiliates to stay with the Alphv program instead of moving to their largest competitor. Alphv also 
announced that they would no longer be negotiating discounts with victims, and that they would 
be removing rules preventing the targeting of critical infrastructure. While law enforcement 
actions in this case had a noticeable impact on the ongoing operations of one of the most prolific 
ransomware groups, Alphv continues to maintain operations today.Major Events in Ransomware:
Published Decryptors impact Ransomware OperationsBesides law enforcement arrests, one of the biggest disruptors to ransomware operationscontinues to be the threat of a public decryptor, either from reverse engineering, because ofa cryptographic weakness, or intentional and unintentional leaks. The business model ofransomware groups depends on the group or affiliates being the only holders of decryptors,with the resulting victim need used as leverage to extort the victim for payment.Early in January 2023, a team at Avast released a free decryptor for BianLians ransomware.Their program leveraged a flaw in the groups encryption binary to ultimately guess andimplement the key for decryption in a reasonable amount of time, given access to theencrypting binary. After seeing success, Avast released another decryptor in June, this timefor the then\-Emerging group Akira. Both events led to obvious and immediate changes inthe threat actors operations. BianLian and Akira have both since appeared to changecourse towards data exfiltration in their attacks, often avoiding encryption on victimnetworks altogether.The threat of a public decryptor is existential to groups who build their own encryptionsoftware; this fact may even push some smaller groups towards joining RaaS outfits whoseencryption technology has proven resilient to security researchers' reverse engineeringefforts. Ultimately the efforts by Avast and other security researchers save victimssignificant time and money by avoiding ransom payment and reducing operationaldowntime. This, in turn, imposes costs on the ransomware operators, who must eitherdevelop a new encryptor or change their tactics entirely outcomes beneficial to defendersacross the board.Types of ransomware single, double, triple extortion
At the outset of 2023, the preponderance of ransomware operations could be described as follows:SINGLE EXTORTION Attackers encrypt victim data and extort victims in exchange for a decryptor to 
recover filesDOUBLE EXTORTION Attackers also exfiltrate data and use the threat of publishing sensitive information 
as a secondary form of leverageTRIPLE EXTORTION Attacker re\-attacks the victim, usually through an availability attack such as 
Distributed Denial of Service (DDoS), as a way to add increased pain points and disruption in a retaliatory 
manner against non\-compliant victims following encryption andor data exfiltration.Blurring of the RansomwareData\-Theft DivideThe Rise of Data Extortion OperationsOver the course of 2023, we observed multiple groups, including RansomedVC and Ransomhouse, 
which focused on data extortion and data leaks absent the deployment of ransomware. In some cases, 
such as RansomedVC, the group encouraged the idea that they were capable of deploying ransomware, 
likely as a way of encouraging compliance, intimidating victims, or introducing uncertainty.GRIT distinguishes this type of operation from exfiltration\-only ransomware operations, in which 
attackers apply initial access and exploitation tactics similar to those used in ransomware operations 
but opt to focus on data exfiltration while eschewing encryption. These operations are often performed 
by groups that have historically conducted single or double extortion ransomware operations, likely to 
reduce the signature of their operations, continue operations following builder leaks or compromise, or 
reduce technical requirements of nascent or continuing operations.Data Extortion Group ExamplesThe most recent example of data extortion group tactics can be seen 
in RansomedVC, a data extortion group that first emerged with a 
clearnet website and a wide range of claims in August 2023\. The 
group would go on to claim high\-profile victims, including Sony and 
Dragos, but further investigation by security researchers revealed 
that data posted by the group appeared to be recycled from previous 
breaches and repackaged to appear new or contained dated 
information, suggesting a distinct initial compromise point. Later 
statements from the group via Telegram laid bare the reasoning 
behind this: despite several claims of network intrusions and 
ransomware capabilities, the group had purchased data leaks 
and databases from brokers and other actors and attempted to 
re\- extort victims or attract attention with the purchased data as
deceptive evidence of breach. While we lack information indicating to what extent, if any, victims paid 
ransoms to the group, its perception and derision on dark web forums suggest that RansomedVCs 
deception did not remain a well\-kept secret. Following a short\-term hiatus for security reasons 
towards the end of 2023, the groups administrators have returned to Telegram, a dark web site, 
and a clearnet site while voicing their intent to resume selling compromised data.Ransomhouse, a similar data extortion group with no history or dependence on ransomware, could be 
considered an inspiration for RansomedVC, having begun its operations in 2022\. Ransomhouse claims 
to exploit unspecified vulnerabilities in victim networks to steal data from victims, though we note 
that this could range from historical and unpatched vulnerabilities to basic misconfigurations and that 
the data theft observed to date reflects smash and grab tactics more than targeted or deliberate 
intrusions. Ransomhouse is suspected of purchasing data from ransomware groups in order to re\-
extort victims, but simultaneously attempts to paint their operations as the responsibility of lazy 
victims who had failed to properly secure their networks. Unlike RansomedVC, Ransomhouse has not 
been noted for attention\-seeking behavior or the issuance of bombastic or self\-promoting claims.Lapsus, sometimes stylized as Lapsus$, was an extortion group that emerged in August 2021\. 
Lapsus conducted a number of high\-profile intrusions resulting in data theftextortion and site 
defacements, impacting the Brazilian Ministry of Health, Rockstar Games, and Okta. Though Lapsus 
exhibited seemingly more advanced and direct tactics relative to RansomedVC and Ransomhouse, 
they similarly focused on data extortion. While commonly referenced as a ransomware group, there 
are contradictory claims regarding the use or dearth of ransomware encryptor use by Lapsus in open 
reporting. The group was known in part for its childish and juvenile communications on Telegram and 
taunting remarks made to victims; behavior made more understandable when London Police arrested 
seven teenage Lapsus members in early 2022\. The group is believed to have disbanded in the wake of 
the arrests and is currently considered inactive, although intelligence reporting suggests that former 
members may have moved on to other groups.Incentives for deceitfabricationSimilar to ransomware groups, data extortion groups are motivated to extract the maximum possible 
ransom from their victims and often seek to do so by threatening consequences for non\-compliance 
with demands. Unlike ransomware groups, data extortion groups do not hold file encryption as 
additional leverage and, in many instances, may never have directly accessed a victims network. 
To compensate for this, we have observed posturing, exaggeration, and outright fabrication from 
some data extortion groups, likely to increase the probability of receiving payment. While ransomware 
groups are no strangers to embellishment and deceit, the root claim of network intrusion is generally 
verifiable forensically. Organizational teams facing data extortion groups are advised to practice due 
diligence in validating any claims made regarding the timing, scope, and impacts of an extortion 
groups alleged attack.The use of exaggeration and embellishment by extortion groups, particularly RansomedVC, highlights 
the need for scrutiny and corroboration in modern cyber threat intelligence operations and security 
research. Early posts from RansomedVC were taken at face value by some security researchers, 
resulting in a litany of reporting of RansomedVC as a Ransomware group and giving credence to 
allegations of high\-profile target impacts. This occurred despite a dearth of evidence supporting their 
claims, no observable ransomware encryptor or associated artifacts, and observed skepticism and 
hostility towards the group amongst personas on dark web hacker forums. Given RansomedVCs 
attention\-seeking behavior, such reporting inadvertently rewarded relatively low\-effort operations 
and, in doing so, could have encouraged victims to comply with ransom demands.Hacktivism and data extortionDistinct from data extortion and ransomware, hack and leak operations remain a frequent tactic 
of hacktivist groups and hacker collectives. Whereas hacktivist groups are ostensibly driven by 
ideological, religious, or political motivations, hacker collectives may conduct data theft for the 
lulz and often appear to consist of younger or more immature operators.We note that the distinction between these cybercrime groups, data extortion groups, and 
ransomware groups may be drawn in part by technical competency, with increasingly impactful 
intrusions and ransoms demanding increasing proficiency and experience. We assess that given 
reduced technical barriers to entry, such as leaked ransomware builders or proof\-of\-concept 
exploits, members of less experienced collectives or hacktivist groups may seek to progress to 
more advanced groups and explore more destructive operations.Ephemeral and No Name Groups definedIn keeping with GRITs taxonomy for ransomware groups, we define Ephemeral ransomware groups 
as short\-lived (flash\-in\-the\-pan) operations that generally terminate within three months of the first 
victim being posted. Ephemeral groups often employ underdeveloped or rudimentary communication 
methods and infrastructure and may recycle commodity malware andor leaked ransom builders in 
their operations. Ephemeral groups are unlikely to have operated under the RaaS model, as the time 
and development required to sustain such a model are incompatible with their short\-lived operations.Colloquially, the terms no\-name, immature, rudimentary, and commodity have all been 
applied to similar groups and "non\-branded" operations that do not appear to maintain long\-term 
operations or develop their own TTPs and malware.Use of Leaked Builders and Commodity 
Malware by Ephemeral GroupsObserved BehaviorIn 2023, GRIT staff directly observed an increasing number of ephemeral or commodity 
ransomware groups during incident response and threat actor communications cases. While this is 
anecdotal evidence, security reporting and industry colleagues continue to report the prevalence of 
these groups, particularly against Small to Medium Sized Businesses (SMBs).As ephemeral groups frequently rely on "second\-hand" malware and ransomware, technical 
barriers to entry for members of the group are reduced. However, this dependence also frequently 
prevents in\-depth understanding and the ability of group members to troubleshoot issues with 
malware or ransomware. This shallow understanding has led to unforeseen problems with 
encryption andor decryption and group members who are unable or unwilling to correct issues. 
When such groups encounter problems after receiving payment, there is little incentive to expend 
resources toward resolution for the victim.Ephemeral groups conducting negotiations often 
appear impatient, impulsive, and inconsistent 
throughout contact. We assess that this may stem 
from undefined or poorly defined processes for 
communications, a desire to quickly cycle through 
victims, or inexperienced operators.Ephemeral groups do not benefit from 
maintaining a reputation or brand awareness, 
which reduces the risk of continued operations 
from deceiving victims or failing to follow through 
on agreements. As Ephemeral groups are likely 
driven to cycle through smaller victims and 
extract ransoms as quickly as possible and lack 
sufficient technical prowess to conduct effective 
operations, we have observed an increased 
willingness to attempt deception of victims and 
exaggerate the impact of intrusions. This most 
often applies to data exfiltration, with groups that 
have exfiltrated little or no data attempting to 
create the impression of widespread data theft.RisksGRIT advises enterprise teams and defenders to consider Ephemeral or unbranded ransomware 
groups as unique threat models distinct from ransomware\-as\-a\-service and Established 
ransomware groups. We base this recommendation on the lower level of technical sophistication 
exhibited by such groups, the increased likelihood of deception in communications, and the 
reduced reliability and predictability of such groups in settlement and resolving decryption issues. 
While decisions to pay or not pay a ransom are those of individual victims, we advise that any 
organizations impacted by an Ephemeral group consider the increased risks of doing so, particularly 
in instances where recovery is feasible absent a decryptor.Based on the observed behavior of Ephemeral groups, victims that opt to pursue a settlement with 
an Ephemeral group face an increased risk of technical issues in the decryption process and 
abandonment by the group in seeking troubleshooting or follow\-on support to restore systems. 
Decryptors may be non\-functioning or partially functioning and based on open\-source encryption 
software or leaked builders from other ransomware groups. Partial but incomplete decryption and 
corrupted files are commonly observed during first attempts at resolution, though some groups 
have successfully resolved decryption issues.While rare in most modern ransomware operations, we have observed Ephemeral groups attempt 
to renege on agreements or extort victims for additional ransom payments, particularly in instances 
that require multiple decryptors or prolonged support. We do not know whether this is driven by a 
short\-term myopic approach to operations or as an excuse to break off communications in 
situations where the group cannot provide a working decryptor. We assess, based on this behavior, 
that the likelihood of re\-extortion and sale of victim data may be higher amongst Ephemeral groups, 
even in cases where a ransom is paid.Novel Coercive Techniques in 2023Intent and effectivenessWe have primarily observed novel coercive techniques deployed against larger targets likely to have 
been extorted for substantial ransoms as part of a so\-called big game hunting approach. While this 
may be due in part to the outsized media coverage that attacks against large organizations attracts, we 
assess that this trend likely also represents increased resource allocation by ransomware groups to 
extract disproportionately high ransoms from victims deemed able to pay.In addition to attempting to coerce non\-compliant victims, novel coercive techniques also likely serve a 
dual purpose of discouraging non\-compliance from future victims. In the same way that fear of sensitive 
data being posted may have historically encouraged compliance from victims, fear of reputational 
damage and negative press coverage presents an additional problem that may justify compliance on 
the client's part.As Ransomware\-as\-a\-Service groups compete for limited affiliates, highly publicized coercive tactics 
may also serve to burnish the brands of participating groups, creating an air of ruthlessness and 
effectiveness that affiliates may find desirable. The media coverage of these tactics almost certainly 
increases the name recognition of associated groups and may support recruitment in the future.Assessed future useWe have observed the increased use of novel coercive techniques by an increasing range of ransomware 
groups throughout 2023; although Alphv remains the most prolific in deploying these tactics, LockBit, 
Medusa, BlogXX, and Hunters International have done so as well. We assess that the use of novel 
coercive techniques by ransomware groups will increase and continue to evolve in 2024\.While we lack insight into the success of novel coercive techniques to date, we consider it unlikely that
novel coercive techniques will decrease the rates of payment from future victims, based on the observed 
continuing operational pace of the associated groups, continued use of these tactics, and our 
discussions with colleagues across the industry.While we continue to assess that the use of these techniques by ransomware groups will attract 
considerable law enforcement attention, Decembers takedown of Alphvs dark web blog and 
subsequent resurgence highlighted the resilience of established ransomware groups. Absent particularly 
successful and aggressive law enforcement efforts, we consider it unlikely that the risks of law 
enforcement disruption will outweigh the perceived benefits of novel coercive techniques in the 
form of ransom payments, increased compliance, or recruitment of affiliates over time.Novel Coercive Techniques DefinedGRIT first explored the topic of novel coercive techniques, and specifically selective public leaks, in Q1 
of 2023\. Today, we define novel coercive techniques as those exhortative actions taken by cybercrime 
groups outside of single, double, or triple extortion operations, designed to employ unique approaches 
to increase the perceived cost of non\-compliance by victims. Over the course of 2023, this has included 
selective public data leaks or direct extortion of and threats to a victim's customers, patients, or clients. 
Given the resources and time associated with these efforts, novel coercive techniques have been most 
frequently associated with larger, Established ransomware groups, which almost certainly benefit from 
substantial resource pools.Examples of Novel Coercive Techniques in 2023BlogXX releases patient informationIn a late 2022 attack against an Australian Health Insurer, potential REvil affiliated group BlogXX
leaked alleged lists of patients who had received abortions and mental health treatment after the 
victim refused to pay a $10 million dollar ransom demand. The lists were posted with accusations 
that the victim's CEO "refuses to pay for yours \[sic] data more, like 1 USD per person. So, probably 
customers data and extra efforts dont cost that.LockBit releases failed negotiation chatsIn early 2023, the LockBit ransomware group published "failed" negotiation chat logs with a 
ransomware victim, adding a comment that the victim "should have chosen better negotiators." 
Although this is not an inherently new extortion technique, this approach is likely intended to 
discourage aggressive negotiation approaches and increase the impact of "shaming" efforts by 
the threat group. Posts of ransomware negotiation chats appear to have become more common in 
2023, particularly in response to failed negotiations or instances where the TA believes they were 
"strung along.Alphv releases cancer patient photosIn an early 2023 ransomware attack against a U.S. healthcare network, Alphv leaked sensitive 
clinical photos of cancer patients after the network refused to pay a ransom. Alphv celebrated the 
leak, stating "Our blog is followed by a lot of world media, the case will be widely publicized and will 
cause significant damage to your business".Medusa publishes student dataIn a February 2023 attack against an urban school district, the Emerging ransomware group Medusa 
published screenshots of notes describing sexual assault allegations after the district refused to 
pay the group's ransom demands. The group also posted a video of their reviewing the exfiltrated 
data and provided an option on their data leak site for anyone to pay the ransom, a previously 
unobserved tactic.Additional Alphv publicity seeking behaviorIn November 2023, following an attack on a 
software company, Established ransomware 
group Alphv released a post and screenshots 
as proof that they had filed a complaint to the 
Securities and Exchange Commission (SEC) 
regarding the victims alleged material 
misstatement or omission. Specifically, Alphv 
sought to highlight the victims failure to report 
the breach within four business days in 
accordance with new SEC rules. The incident 
attracted demonstrable media attention, 
specifically within the security space.In September, Alphv claimed responsibility for a highly publicized attack against MGM Resorts. 
Following widespread media coverage detailing outages at MGM properties, Alphv released a 
statement detailing how the groups affiliate had allegedly gained access, while attempting to highlight 
repeated alleged failures to evict the group from MGMs networks. The group closed the statement 
by claiming continued access and threatening to carry out additional attacks if not contacted.LockBit's use of social media bot accounts in OctoberFrom October to November 2023, Established ransomware group LockBit attempted to extort a 
relocation services company. When negotiations broke down, LockBit amplified claims of the attack 
and tagged multiple corporate partners on the social media site X, formerly known as Twitter. The 
group used what appeared to be a series of bot accounts to repost, like, and otherwise share the 
posts, and later released copies of the negotiation messages.Hunters International Extorts Healthcare ClientIn December 2023, Emerging ransomware group 
Hunters International claimed responsibility for an 
attack against a cancer medical center. Likely following 
non\-payment of the groups ransom demands, the 
group contacted an unknown number of the centers 
patients, threatening the release of private informationand offering removal of individual data for $50\. A few weeks later, clients of a non\-profit health 
network received similar messages and offers to remove their data for $50\. While the secondary 
attack has not been attributed to Hunters International at the time of this report, we note the 
similarities in behaviors as a probable indicator of tactic reuse by Hunters International, or 
adaptation by another group.Signposts of Ransomware
Activity and 2024 OutlookSignpost analysis definedIn reviewing 2023s ransomware trends, GRIT analyzed and considered potential signposts orindicators contributing to increases or decreases in ransomware operations or ransom paymentrates. These indicators are anecdotal in nature but were reviewed critically for feasibility of impactand consistent observations over the preceding two years. In addition to evaluating the assessedpositive or negative impact on ransomware operations writ large, GRIT staff also assessed thedirection (likelihood increasing or decreasing) of each indicator moving into 2024\. The end result,presented here, is a consolidated signpost analysis of contributing factors and their assesseddirection in 2024\.Impact on 
RansomwareDiscourages 
Ransom 
Payments or 
Reduces 
Ransomware 
OperationsHas no Impact on 
Ransom Payments 
or Ransomware 
OperationsEncourages 
Ransom Payments 
or Increases 
Ransomware 
OperationsAssessed 
Direction of 
TrendLikely to Decrease 
in FrequencyUnlikely to Increase 
or Decrease in 
FrequencyLikely to Increase 
in FrequencyTrendImpact on 
RansomwareDirection
in 2024Posted ransomware victims continue to increase in volume
Increases in ransomware victim volume are expected to 
continue until the point of saturation, with additional actors 
seeking entry while prospects of revenue generation remain.Instances of novel coercive techniques increase 
in frequency and sophistication
Effective and novel coercive techniques are expected to 
continue, with fear of reputational impacts, news coverage, 
and clientcustomer extortion impacting willingness of 
some victims to pay.Additional ransomware builders of Established 
ransomware groups, andor commodity malware 
are released or leaked
Sporadic leaks of ransomware builders and commodity 
malware are expected, presenting new opportunities and 
reducing technical barriers to entry for new entrants.Law Enforcement operations to disrupt, arrest, 
and try ransomware operators increase
LE disruption of ransomware operations is expected to 
remain steady, with particularly impactful disruption 
likely to deter new entrants and discourage current 
ransomware operators.Inflation increases or currency value decreases 
in Russia and Central Asian states
Economic impacts of Russia's war on Ukraine are expected 
to continue, driving economic hardship that may encourage 
new entrants.US, UK, or EU governments adopt additional reporting 
requirements for ransomware victims
Increased reporting requirements are expected in the short\-
to\-medium term, increasing awareness of Ransomware's 
pervasiveness and discouraging payment by victims.US, UK, or EU governments adopt bans on 
ransom payments
Outright bans on ransom payments are not anticipated in 
the near term, though their implementation would almost 
certainly reduce ransomware operations and payments.TrendImpact on 
RansomwareDirection
in 2024"Zero\-Day" vulnerabilities in enterprise software increase
Ransomware operators are likely to continue seeking zero\-day 
vulnerabilities and developing or purchasing accompanying exploits 
as a means to gain initial access and overcome increasing security 
capabilities. Some vulnerabilities may become part of mass\-
exploitation campaigns, generating substantial victim volume.Publication or leaks of free ransomware decryptors increases
Publication or leaks of ransomware decryptors, from security 
organizations or law enforcement, is expected to continue, 
and serve as at least a temporary setback to double\-extortion 
operations.Cybersecurity liability insurance rates increase substantially, 
coverage options decrease, or ransom reimbursements decrease
Costs are expected to increase in the short\-to\-mid\-term, reducing 
ransom coverage and thereby the ability of victims to pay ransoms 
at current rates.Additional international sanctions are placed on named 
ransomware groups, restricting ransom payments to 
known established groups
Additional group\-specific sanctions are not anticipated, though 
implementation would deter and effectively criminalize many 
ransom payments.Substantial leak or compromise of internal group 
communications for prolific Established ransomware 
group ( la Conti Leaks)
Embarrassing revelations and leaks of prominent ransomware 
groups are not anticipated, but would likely lead to dissolution, 
splintering, or rebranding of impacted groups.Ransomware groups increasingly implement negotiation 
restrictions, such as minimum ransom amounts or "discount" 
percentages
Increased implementation of negotiation restrictions may occur 
in the short\-mid\-term following LockBit's model, though such 
restrictions could eliminate the ability of many victims to pay, 
reducing total revenue for affiliates.High\-impact, high\-visibility ransomware event resulting 
in physical damage or casualties
Severe, catastrophic physical impacts of ransomware may or 
may not occur but would more likely result from an accident than 
deliberate intent. Negative press and law enforcement attention 
from such an incident would likely lead some groups, affiliates, 
or individual operators to "go to ground" to avoid detention.2023 Final Remarks 
and SummaryIn 2023, ransomware continued to increase in terms of impact, sophistication, and the numberof participating actors, an indication that the ransomware ecosystem has not yet reached apoint of market saturation. As with any economic microcosm, this point will eventually bereached through continued increases or outside impacts on the market that drive the saturationpoint lower. Put another way, we can expect ransomware impacts to continue an upwardtrajectory into 2024 and beyond until such a point that ransomware groups' financial interestsconflict with one another or until law enforcement and regulatory pressures reduce theperceived attractiveness of the space and the risk calculus of its participants.In the same vein, the success of ransomware groups amidst other cybercriminals will continueto encourage impostors, shysters, and frauds eager to exploit society's fear of ransomware togenerate a profit by other means. Scrutiny of threat actor claims, both public and private, willbecome an increasing imperative for defenders in order to defend and deter against datare\-extortion and identify exaggerated claims. As is often said and often overlooked in ourcommunity of practice: ransomware operators, extortion groups, and hacker collectives arecriminals, and we trust or believe them at our own peril.Ransomwares heaviest hitters, as reflected in long\-term, Established and prolific groupssuch as LockBit, Alphv, and Clop, continue to account for not just the lions share of victimsbut also much of the innovation and tactical changes across the ransomware ecosystem. TTPsand behaviors exhibited by these groups inevitably trickle down to less mature ransomwaregroups seeking to increase effectiveness and revenue generation. This hierarchy reflects theimportance of law enforcement disruption and security research exposing the operations ofthese groups, with operational disruption against them likely to generate the greatest impactson the ransomware economy.As 2024 unfolds, Defenders and the security community are increasingly aware of andprepared for the threat of ransomware. Our future success will depend on our ability toadapt to and match the paces of a committed, resilient, and increasingly professionalizedadversary. To this end, industry best practices in threat intelligence, information sharing,and public\-private partnerships remain our most viable and effective options to forceadversaries to cede ground.Appendix: Q4 2023 Ransomware ObservationsOverview of Q4 2023 Victim Posts and Active Groupss
p
u
o
r
G
e
v
i
t
c
A302520151050140120100806040200s
t
s
o
P
mi
t
c
Vi2\-Oct9\-Octct16\-Oct23\-Oct30\-O6\-Novov
13\-Nov
20\-Nov
27\-N4\-Dec11\-Dec18\-DecTotal Posts
1,130Total Groups
46Overall, Q4 2023 was slower than preceding quarters, with the lowest volume of observed victims(1130\) since Q1 (859\). Additionally, October and December had the lowest volume of postedsingle\-month victims at 336 and 361, respectively, since February, which only saw 242 victims.In terms of group activity, the soft\-spoken Established group, Play, was an outlier, jumping fromfifth place with 71 victim posts in Q3 to second place with 113 victim posts in Q4, continuing anupward trend. This jump was the largest increase in victim volume among any Ransomware groupin Q4\.Conversely, GRIT observed the greatest drop in activity from Clop, which decreased from 171posted victims in Q3 to only 4 in Q4, despite maintaining an active leak site and an additional sitededicated to the sharing of torrents containing leaked victim data. We assess that this dropcorresponds with Clop's shift from "traditional" ransomware operations and towards a focus onmass\-exploitation of vulnerabilities and a campaign\-style approach to operations.Appendix: GRIT Ransomware TaxonomyBy subdividing ransomware groups, GRIT can obtain more detailed insights into how ransomware groups 
progress in their level of operational maturity and can classify and identify potential rebranding activity.We distinguish ransomware groups by placing them into these six categories:EMERGING
This category is reserved for new ransomware groups within their first three months of operations. These 
organizations may be short\-lived, resulting in an Ephemeral group; may be determined to have Splintered or 
Rebranded from an Established group; or may move on to further develop their operations and TTPs over time.EPHEMERAL
These groups are short\-lived, with varied but low victim rates. Observed victims are usually posted in a single 
or short series of large postings rather than a continuous flow over time. Ephemeral groups, by definition, 
terminate operations, spin\-off, or rebrand within three months of formation. These groups may or may not 
have dedicated infrastructure (i.e data leak sites and chat support) as part of their operations.DEVELOPING
These groups have conducted operations for three months or longer, resulting in a recurring flow of victims. 
Developing groups do not appear to be directly linked to other ransomware groups as a Splinter or Rebrand but 
may include some experienced ransomware operators. Developing groups generally improve their people, 
processes, or technology over time by recruiting additional members, refining TTPs, or improving the quality of 
their associated ransomware and encryption. These groups generally have dedicated infrastructure (i.e data 
leak sites and chat support) as part of their operations.SPLINTER
These groups consist of a plurality of members from previously Developing or Established groups and may have 
formed either by choice or due to exclusion. These groups may be identified by very similar or overlapping TTPs 
and tooling or through HUMINT gathered through interactions with personas on the deep and dark web. 
Splinter groups differ from Rebrands by the continued existence of the original organization as the Splinter 
group operates.REBRAND
These groups consist in whole, or in part, of former Developing or Established groups. Rebrands often maintain 
the same people, processes, and technology as the original group. Rebrands are generally undertaken in order 
to minimize attention from law enforcement or intelligence officials or to avoid negative publicity.ESTABLISHED
These groups have operated successfully for at least nine months and have well\-defined and consistent tactics, 
techniques, and procedures. Established groups often possess functional business units that enable sustained 
ransomware operations, with specialists focused on areas such as personnel, encryption, negotiations, etc. 
These organizations successfully employ technology and redundant infrastructure to support their operations.There are multiple routes a group can take through the various classifications, and no one route is standard. 
While one group may begin as Ephemeral and move their way through the ranks to Full\-time, another group 
may enter as a Rebrand as part of a larger obfuscation strategy to avoid attention from law enforcement.