August 2023The State of Supply Chain ThreatsWidely exploited vulnerabilities in open source software and malicious components 
being loaded in trusted public repositories have highlighted issues in the software 
supply chain. Heres what organizations are doing to mitigate their risk.Sponsored by3Mend Perspectives5About the Author6Executive Summary8Research Synopsis9High Concerns Over Supply Chain Risk 11Work in Progress: Software SupplyChain Security 13Profound Impact on Supply Chain Practices 14Conclusion 16AppendixThe State of Supply Chain ThreatsFiguresFigure 1:Priority Level of Supply
Chain SecurityFigure 2:Top Supply Chain IssuesFigure 3:Importance of Supply Chain RisksFigure 4:Response to a Supply Chain AttackFigure 5:Time to Mitigate Supply
Chain IssuesFigure 6:State of Software Supply ChainFigure 7:Concerns About Software
Supply ChainFigure 8:Managing Software Supply ChainFigure 9:Vendor ScorecardsFigure 10:Software Bills of MaterialsFigure 11:Build Practices to Prevent SoftwareSupply Chain AttacksFigure 12:Software Supply Chain StatementsFigure 13:Effect of Recent Attacks on
Organizations Approach to
Supply Chain SecurityFigure 14:Minimizing Third\-Party RiskFigure 15:Types of Information for Supply 
Chain AssessmentFigure 16:Securing the Supply ChainFigure 17:Supply Chain AttackFigure 18:Types of AttacksFigure 19:Current Protection AgainstSoftware Supply Chain ThreatsFigure 20:Insurance Partner for Reducing 
Third\-Party RiskFigure 21:Respondent Region of ResidenceFigure 22:Respondent Job TitleFigure 23:Respondent Company SizeFigure 24:Respondent IndustryS
TNETNO
CTABLE OFDark Reading ReportsAugust 20232Table of ContentsThe Rising Threat of Malicious PackagesSponsored Content
MEND 
PERSPECTIVESBy Carol HildebrandMalware has entered the software supply chain. Are you prepared?Open source code package repositories, such 
as npm and RubyGems, allow anyone to store 
orpublishpackages,andunfortunately,even 
thosecontainingmalware.Theseareknown 
asmaliciouspackagesthemalwareofthe 
software supply chain.Maliciouspackagesarentnew,buttheyre 
proliferating at an alarming pace. In our Special 
Report:SoftwareSupplyChainMalware, 
Mend.io identified a 315% increase in malicious 
packagespublishedtonpmandRubyGems 
from 2021 to 2022, and expects that trend to 
continue.Anatomy of a Malicious
Package AttackMaliciouspackagesareused 
tosteal 
credentials,exfiltratedata,turnapplications 
into botnets, or erase data. But first, attackers 
needtotricksomeoneorsomethinginto 
downloading the package.It can be as simple as hiding a malware payload 
inopensourcecodeandtrickingacareless 
developerintousingit,orelevatingbugsin 
package manager systems and then benefitingfrom the opportunities afforded by the scale of 
acorruptedsoftwaresupplychain.Makeno 
mistake: Like any malware, malicious packages 
can inflict significant damage.Organizational Impact: Malicious 
Packages Are More Dangerous 
Than VulnerabilitiesOnceadeveloperdownloadsamalicious 
package,howmuchdamageitdoeswill 
depend on the following factors:1\.Intent:Whenthreatactorsinfiltrateusing 
amaliciouspackage,theirintentsubstantially 
determinestheimpact.Athreatactortrying 
to inform people about a war or protest action 
withannoyingmessageshasaloweroverall 
impactthanonetryingtostealinformationor 
turn developers machines into cryptocurrency 
miners.2\.Organizationtype:Attacksdesignedto 
exfiltrate personal information will have a larger, 
potentiallylong\-termimpactoncompanies 
trustedwithsensitivedata.Ransomware 
attacksthatdisablesystemscanhavean 
outsizeimpactinorganizationslikehospitals,where lives depend on uptime.3\.Duration:Whenmaliciouspackagesare 
discoveredquicklyandremovedcompletely, 
thedamagetheycausecanbelimited.The 
greatest damage can be caused by packages 
thatremainundetectedformonthsoryears 
while quietly delivering their payloads.4\.Spread:Someofthemostdangerous 
maliciouspackagesaredesignedtoprovide 
initial access to a network, at which point the 
threat actor can move laterally through systems 
to steal passwords or protected information to 
gain even more access.Unlikevulnerabilities,whichcananddooften 
existformonthsoryearsinapplicationcode 
withoutbeingexploited,amaliciouspackage 
representsan 
toyour 
immediate 
organization.threatMalicious Package
Attack VectorsTodeliveramaliciouspayloadviaanopen 
sourcepackage,attackersmustfindaway 
togetthepackagedownloaded.ThefourDark Reading ReportsAugust 20233Table of Contentsbasicattackvectorsformaliciouspackages 
arebrandjacking,typosquatting,dependency 
hijacking, and dependency confusion.Brandjacking:Anattackeracquiresor 
otherwiseassumestheonline 
identityof 
anothercompanyoranownerofapackage 
andtheninsertsamaliciouscode.Itdoesnt 
necessarily mean he actively steals something, 
butjusttakesadvantageofanopportunityto 
take ownership related to the brand name.Typosquatting:Anattackerpublishesa 
maliciouspackagewithasimilarnametoa 
popular package, in the hope that a developer 
will misspell a package name and unintention\-
ally fetch the malicious version.Dependencyhijacking:Anattackerobtains 
control of a public repository in order to upload 
a new, malicious version.Dependencyconfusionattacks:Here,the 
threat actor creates a public repository package 
with the identical name of an internal packagewithin the intended target system. The intention 
is to trick the targets dependency management 
toolsintodownloadingthemaliciouspublic 
package instead of the safe internal one.Thebestdefenseagainstthegrowingthreat 
of malicious packages is a knowledgeable and 
alert developer community in and around open 
sourceregistries,combinedwithautomated 
detection and response solutions.ReadMend.iosSpecialReport:Software 
Supply Chain Malware for the latest research 
on the malware of the supply chain.AbouttheAuthor:AveteranofComputer\-
worldandCIOmagazine,CarolHildebrand 
isanaward\-winningtechnologywriterwho 
focuses on cybersecurity and how it impacts 
business innovation.Dark Reading ReportsAugust 20234Table of ContentsThe State of Supply Chain ThreatsAbout the AuthorFahmida Y. Rashid 
Dark ReadingFahmida Y. Rashid is Dark Readings managing editor for features. She has spent over a decade analyzing news 
events and demystifying security technology for IT professionals and business managers. Her work has appeared in 
various business and tech trade publications, including VentureBeat, CSO Online, InfoWorld, eWEEK, and CRN.Dark Reading ReportsAugust 20235Table of ContentsThe State of Supply Chain ThreatsY
RAMMU
SEXECUTIVEMany organizations changed or started making signicant changes to their supply chain security practices two years 
ago to address growing risks from vulnerable third\-party software and open source components. On the open source front, 
the growing number of malicious components being pushed into public code registries such as npm, PyPI, and Maven 
 highlights the necessity of these changes. More concerning for organizations is the fact that attackers have exploited zero\-
day vulnerabilities in multiple, widely used software products, including Microsoft Exchange, Kaseya, and Accellion, to breach 
numerous government and private entities worldwide.Dark Readings 2023 Supply Chain Threat Survey of 242 IT and cybersecurity professionals shows that a lot has stayed the 
same in regard to supply chain risk. A relatively high percentage of organizations have implemented processes for mitigating 
risk from vulnerabilities in the partner ecosystem, and there is strong awareness of what needs to be done to strengthen the 
security of the software supply chain. Most organizations, for instance, maintain a software bill of materials repository, and 
more than one\-third of respondents expect their organizations to increase their use of SBOMs in the coming year.More than half the organizations in Dark Readings survey require their software suppliers to adhere to stipulated security stan\-
dards, and nearly one in four want their vendors to submit independent audits or assessments indicating they meet security 
requirements. Others request ad hoc, point\-in\-time assessments of their suppliers security posture.Whatisstrikingaboutthisreportisthatdifferentoccurrenceshaveaffectedresponsesthisyearversuslast.Theattacks 
against Kaseya and Accellion were fresh in the minds of the respondents last year; this years respondents were asked to 
assess their ability to detect and mitigate supply chain attacks while being confronted with the attacks that exploited multiple 
vulnerabilities in the MOVEit le transfer utility.While many organizations have implemented multiple processes for managing supply chain risks, a sizable percentage of 
organizations have not done so and remain at heightened exposure to attacks via the supply chain. Even so, most IT and
cybersecurity professionals in the survey appear condent in their organizations ability to defend against a supply chain attack 
and to detect and respond to any incidents that might get past their defenses.Dark Reading ReportsAugust 20236Table of ContentsThe following are some of the key takeaways from the survey:The State of Supply Chain Threats71% of respondents describe third\-party risk and supply chain security as one of their top ve security initiatives for the coming year.71% of organizations in the survey say their current security programs cover software supply chain threats, but only 28% explicitly state thattheir program covers the software supply chain.Just 24% of organizations consider their software supply chain secure. For 55% of organizations, software supply chain security is still a workin progress.50% maintain a software bill of materials repository, but just 36% claim to create complete SBOMs for all their software. Just 41% regularlyrequest SBOMs from vendors and suppliers.40%sayvulnerabilitiesinopensourcesoftwarecomponentsistheirbiggestsupplychain\-relatedworry;24%pointtodevelopersbeingtricked into malicious components, via methods such as typosquatting and dependency confusion.34%ofrespondentswhohadexperiencedasupplychainattackoverthepastyearsaydevelopersaccidentallydownloadedmaliciouscomponents from public code registries, such as PyPI and npm.49%ofITandcybersecurityprofessionalsinthesurveysaytheyaremostconcernedaboutattackerstargetingtheirorganizationsviavulnerabilities in widely used commercial platforms.Dark Reading ReportsAugust 20237The State of Supply Chain ThreatsSurvey Name: Dark Reading 2023 Supply Chain Threat SurveySurvey Date: June 2023NumberofRespondents:242ITandcybersecurityprofessionalsatcompaniesofallsizes,basedprimarilyinNorth
America. The margin of error for the total respondent base (N\=242\) is \+\-6\.3 percentage points.Purpose: Dark Reading surveyed information technology and cybersecurity professionals on the supply chain threat land\-
scape; their biggest current concerns; the practices they have implemented to manage supply chain risk; and their capabilities 
for preventing, detecting, and responding to supply chain\-related security issues.Methodology: The survey queried decision\-makers with job titles that involved IT or IT security (cybersecurity) at organiza\-
tions across more than a dozen industry sectors. It asked them about a wide range of supply chain threats and risk mitigation 
practices. The survey was conducted online. Respondents were recruited via an email invitation containing an embedded link 
to the survey. The email invitation was sent to a select group of Informa Techs qualied database; Informa is the parent com\-
pany of Dark Reading. Informa Tech was responsible for all survey design, administration, data collection, and data analysis. 
These procedures were carried out in strict accordance with standard market research practices and existing US privacy laws.Table of ContentsABOUT USDark Reading Reports
offer original data and insights on 
the latest trends and practices in 
IT security. Compiled and written 
by experts, Dark Reading Reports 
illustrate the plans and directions 
of the cybersecurity community 
and provide advice on the steps 
enterprises can take to protect their 
most critical data.Dark Reading ReportsIS
SPONY
SRESEARCHDark Reading ReportsAugust 20238Table of ContentsThe State of Supply Chain ThreatsHigh Concerns Over Supply 
Chain Risk
Supplychainsecuritywasintheheadlinesfor 
most of 2022 as well as the first half of 2023 
 and it became increasingly clear that supply 
chainriskdoesnotmeanthesamething 
toeveryone.Supplychainisoneitemunder 
applicationsecurityasorganizationsworry 
about the security and provenance of software 
componentsusedinapplicationdevelopment. 
Supplychainisalsoanitemundersecurity 
operations and cloud security as organizations 
scrutinizethesecuritypreparednessoftheir 
cloudprovidersandthird\-partyserviceprovid\-
ers.Supplychainisalsotopofmindfor 
organizationsthatareseeingtheirdatastolen 
and networks compromised because a business 
application they rely on has been compromised.Thesevariedincidentshighlightthedamage 
supply chain attacks could cause and height\-
enedconcernsaboutenterpriseexposureto 
different types of supply chain risks. But there 
are also signs to be optimistic about, such as 
industrywide efforts to strengthen the security 
ofthesoftwaresupplychain.Lastyears 
executive order from the Biden administration 
requiringfederalagenciestoadoptanumber 
ofsoftwaresecuritybestpracticessuch 
asmaintainingasoftwarebillofmaterialsforFigure 1\.Priority Level of Supply Chain Security
Compared with all of your organizations security initiatives for the coming year, how high a priority is 
third\-party risk and supply chain security?1%5%12%10%1%3%9%12%13%17%34%25%202330%2022Its our top priorityIts among our top 3 prioritiesIts among our top 5 priorities28%Its among our top 10 prioritiesIts important, but not part of our top 10Its not a priority at this timeDont knowData: Dark Reading survey of 242 
cybersecurity and IT professionals in
June 2023 and 115 in June 2022allsoftwareinuse,implementingcontrolsto 
protect build environments, and documenting 
all software dependencies in use has pushed 
organizationstoincludethoseconversations 
as they make their security plans.DarkReadings2023SupplyChainSecurity 
Surveyreflectsthisheightenedsenseof 
awareness.Supplychainsecurityremainsa 
major concern for IT and security professionals, 
with 71% of all organizations listing supply chain 
security among their top five security priorities 
for 2023\. It tops the list of security priorities for 
12%oforganizations.Whatsnoteworthyisthat priorities dont seem to have shifted at all 
since last year, when 70% listed supply chain 
security among their top five (Figure 1\).Thereisnoclearconsensusamongsecurity 
and IT decision\-makers on which supply chain 
securityissueconcernsthemmost.Almost 
half (49%) of respondents cite attacks targeting 
vulnerabilities in commercial platforms as their 
biggestsupplychainsecurityissue,whichis
asignificantincreasefromlastyear(36%) 
(Figure 2\). Some of the jump could be directly 
related to the fact that the survey was conducted 
around the time when researchers warned thatDark Reading ReportsAugust 20239Table of ContentsFigure 2\.Top Supply Chain Issues
When it comes to the supply chain, which of these issues worries you the most?20232022Attacks targeting vulnerabilities in commercial platformsAttackers targeting my organization after compromising my 
suppliers and partnersRansomware attacks that originated from a supply chain 
compromise 49% 
 36% 42% 
 44% 41% 
 40%Vulnerabilities in open source software components that are 
used by commercial applications 40% 
 51%Business processes being disrupted because the supplier is 
offline after a cyberattack 38% 
 20%Vulnerabilities in frameworks and other developer tools used to 
create applications 34% 
 49%Being tricked into downloading malicious components 24% 
 27%Adversaries steal secrets, such as tokens, and gain 
unauthorized access to our systems 24% 
 16%Scanning and remediating vulnerabilities in containers 22%
 NADownstream attacks after adversaries compromised a code 
repository and inserted malicious packages 21% 
 25%Firmware\-based attacks 13% 
 20%Backdoored hardware components incorporated in devices 
used by my organization 13% 
 25%Securing open source software in containers 12%
 NAI do not have visibility over my supply chain to accurately 
assess risk 12% 
 10%Attackers intercept my digital keys and certificates to sign 
malicious code 11% 
 10%Note: Maximum of ve responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022The State of Supply Chain Threatsattack groups were actively exploiting a critical 
zero\-dayvulnerabilityinProgressSoftwares 
MOVEitTransfermanagedfiletransferutility 
fromorganizations.Recent 
tostealdata 
analysisfromBrettCallow,athreatanalyst 
atEmsisoft,suggeststhat347organizations 
have been affected and more than 18\.6 million 
theirdatacompromised.
individualshadPerhapsinfluencedbytheattackstargeting 
MOVEit,respondentstotheDarkReading 
survey also list concerns that attackers would 
targettheirorganizationsaftercompromising 
suppliersandpartners(42%),ransomware 
attacksoriginating 
fromasupplychain 
compromise (41%), and disruptions to business 
processesbecausethesupplierwashitbya 
cyberattack (38%).Respondentsarealsoconcernedabouttheir 
exposure to insecure open source components, 
tools,andframeworks.Fortypercentofthe 
respondentssaytheirbiggestsupplychain 
securityissuehastodowithvulnerabilitiesin 
opensourcesoftwarecomponents,and34% 
saythesameaboutflawsinframeworksand 
other tools developers use to create applications. 
Aboutaquarterofrespondents(24%)are 
concerned about their developers being tricked 
into downloading malicious components.Dark Reading ReportsAugust 202310Table of ContentsThe State of Supply Chain ThreatsTyposquatting names and dependency poison\-
ing are types of attacks in which a threat actor 
introducesmaliciouscomponentsintowidely 
used public software repositories, such as npm, 
and then tries to trick users into downloading it 
by, for instance, using the local phone number 
from a legitimate package.Enterprisesupplychainsecurityalsogoes 
beyondsoftware:13%citefirmware\-based 
attacksasamajorconcern,andanequal 
numberworryaboutbackdooredhardware 
components used in devices.Fromariskprioritizationstandpoint,ITand 
securityleadersarelessfocusedonattacks 
targetingthepartnerecosystemandmore 
focused on mitigating exposure from vulnerable 
software. The respondents identify software as 
themostimportantissuewhenaskedtorank 
supplychainrisksbyorderofimportance. 
Survey respondents rank risks associated with 
third\-partyvendorsandcontractorsthird,and 
other risks associated with open source software 
fourth, in order of importance (Figure 3\).Third\-party libraries are widely used in software 
developmentbecausetheygivedevelopersa 
way to quickly add specific functionality to their 
code. But because the components can nestseveral layers in the code, sometimes it can be 
hard to find vulnerabilities in applications.Work in Progress: Software 
Supply Chain SecurityDark Readings survey shows most respondents 
are confident about the controls they have in place 
tomitigatesupplychainsecurityrisks.Survey 
respondents express some level of confidencesaytheirorganizationshaveclearprocesses 
onhowtorespond(Figure4\).Respondents 
alsosuggesttheyhaveallthepiecesinplace 
to be able to address and mitigate supply chain 
issueswithinonetothreedays(35%).There 
are roughly equal numbers of respondents with 
the confidence in their processes to be able to 
handle an incident in less than 24 hours (22%) 
and those requiring four days to approximatelyFigure 3\.Importance of Supply Chain Risks
Rank the following types of third\-party and supplier risk to your organization in order of importance.SoftwareDigital supply chainThird\-party vendors and contractorsOpen source softwareFirmwareContainer securityHardware componentsOverall Rank1234567Score1,1011,020993943665596580Note: Rank is based on a weighted score. Responses are weighted, and scores represent the sum of all weighted counts.
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023inhowtheirorganizationwouldrespondtoa 
supplychainattack.Seventypercentindicate 
theirorganizationshavedesignatedstaffto 
respond to supply chain issues or know whom 
to call in case of a supply chain attack, and 67%a week (19%) (Figure 5\). This suggests some 
variability remains in the kind of controls in place.Theconfidencetheseresultsreflectdidnot 
carry over into the respondents perception of 
the overall state of their organizations softwareDark Reading ReportsAugust 202311Table of ContentsFigure 4\.Response to a Supply Chain Attack
Please tell us how much you agree or disagree as to how your organization would respond to a supply 
chain attack.Strongly
agreeSomewhat 
agreeNeither 
agree nor 
disagreeSomewhat 
disagreeStrongly 
disagreeMy organization has clear processes for how to handle 
a supply chain incident28%39%24%We have designated staff to respond to supply chain 
issues, or we know whom to call in case of a supply 
chain attackMy organization will need to hire an outside team or 
consultant to deal with a supply chain incidentMy organization will need to shut down operations
business processes to deal with an attack31%39%20%16%10%27%20%31%32% 7% 8%16%24% 2%2%10%14%Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023supply chain security. Less than a quarter (24%) 
perceive their software supply chain to be fully 
secure, and almost an equal number (23%) say 
they have a ways to go to secure the software 
supply chain (Figure 6\). A third (33%) describe 
their efforts as a work in progress, either almost 
or halfway finished.When asked to rank issues in software supply 
chainsecurity,respondentssaytheyare 
worriedaboutvulnerabilities 
inthird\-party 
libraries,followedbydevelopersdownloading 
importingmaliciouspackagesand 
and 
components,andattackerstamperingwith 
existinglibrariesandrepositoriestoinclude 
malicious code (Figure 7\). Whats troubling isthatdespitetheseconcerns,manyorganiza\-
tions have not implemented controls to protect 
their software supply chain and to limit damage. 
Forty percent restrict their developers in using 
dependenciesonlyfromtrustedrepositories 
andregistries,andjust36%regularlycheck 
containerimagesforvulnerabilitiesaspartof 
their processes for managing supply chain risk 
(Figure8\).Securityanalystsconsidersuch 
scanning before a container is deployed into 
production a fundamental practice for early 
risk detection and remediation.The use of vendor scorecards or rating scores 
from 
industryconsortiumstoassessthe 
securityofopensourcecomponentsremainsThe State of Supply Chain Threatsanopenquestion.Whileaplurality,47%,say 
they do use some kind of scorecard system to 
assess software components, the fact that 20% 
are unsure if their organizations rely on vendor 
scorecardsorratingscorestodeterminethe 
security of open source components suggests 
the idea is still in the early stages (Figure 9\).On the other hand, Dark Readings 2023 Supply 
ChainThreatsSurveyrevealsrelativelyhigh 
awarenessandadoptionofonesupplychain 
bestpractice:thesoftwarebillofmaterials. 
Half (50%) of organizations maintain a software 
billofmaterialsrepository,and48%planon 
increasing SBOM use over the next year (Figure 
10\). An SBOM, an inventory of all open source 
and third\-party components used in a particular 
piece of software, typically includes information 
such as the license of the software component, 
itsversion,andlistofknownvulnerabilities 
thatmaybepresent.Securityexpertssee 
SBOMsaskeytoanorganizationsabilityto 
quicklyidentifyandremediatevulnerabilities 
in open source components in their software. 
However, the use of SBOMs still seems limited, 
asonly41%regularlyrequestSBOMsfrom 
theirvendorsandsuppliers,andthesame 
percentageofrespondentsusesSBOMsas 
part of their vulnerability management efforts.Dark Reading ReportsAugust 202312Table of ContentsThe State of Supply Chain ThreatsJustathird(33%)havedeployedautomated 
tools to minimize human input and reduce the 
attack surface, and another third (32%) accept 
only signed components and verify signatures 
beforedeployment.Otherprocesses 
for 
managingthesoftwaresupplychaininclude 
verifying the changelog and commit history for a 
particular code component or software project 
beforedownloadingit(26%),andsignature 
verificationbeforedeploymentandexecuting 
applicationbuildsinephemeral,sealed,or 
isolated environments (25%).Respondentswerealsoaskedtosharetheir 
perceptionsofhowdifficultitistoimplement 
buildpracticesandmethodsforpreventing, 
mitigating,andremediatingsoftwaresupply 
chain security attacks. The results suggest there 
is some work left to do. While the respondents 
tend to be neutral (rating three on a five\-point 
scale),asignificantnumberconsiderthe 
practicesdifficult.Forty\-threepercentsay 
using a hermetic build with all inputs declared 
withimmutablereferencesisdifficult(Figure 
11\). Making provenance information when, 
where, and how the software was produced 
available is one way to ensure the application 
hasntbeentamperedwith,but32%report 
that this action is difficult to implement. While 
respondents agree that shifting left is necessary 
to secure the software supply chain (55%), theFigure 5\.Time to Mitigate Supply Chain Issues
About how long would it take your organization to address and mitigate a supply chain issue?14%22%10%15%4%6%19%8%12%35%24%Less than a 24 hours1 to 3 days4 days to approximately 1 week31%2 to 3 weeksMore than a monthDont know20232022Data: Dark Reading survey of 242 
cybersecurity and IT professionals in
June 2023 and 115 in June 2022mechanismfordoingsoremainsadaunting 
process for many of them (Figure 12\).Profound Impact on Supply 
Chain PracticesBreachesresultingfromrecentvulnerabilities 
inwidelyusedthird\-partysoftwareandopen 
sourcecomponentsarehavingaprofound 
effectonenterprisesupplychainsecurity 
practices.Theincidentshavepushedmany 
organizations over the past year to change 
or start making changes to their approach to 
managing supply chain risks. Fifty\-six percent 
oforganizationssurveyedhavemadesomekindofchangestoaddressrisksfromthird\-
partysuppliersandpartners;17%areinthe 
process of making major changes (Figure 13\). 
Lastyear,65%madechangesofsomesort 
(includingmajorones).Whatsmore,supply 
chainconcernsinthewakeoftheattacks 
against MOVEit would likely push organizations 
torevamptheirpracticesagainonhow
theyhandlethird\-partysoftwareandopen 
source risk.More than half (51%) of responding organiza\-
tionshavestipulatedsecuritypracticesthat 
vendorsmustadheretoaspartoftheirDark Reading ReportsAugust 202313Table of ContentsFigure 6\.State of Software Supply Chain
What is the state of your organizations software supply chain security?3%10%24%1%11%6%19%8%23%11%21%22%21%202320%2022Data: Dark Reading survey of 242 cybersecurity and IT professionals in
June 2023 and 115 in June 2022Our software supply chain is secureWe are almost nished securing our 
software supply chainWe are about halfway nished with 
the process of securing our software 
supply chainWe have a ways to go to secure our 
software supply chainWe have not started to secure our 
software supply chain, but we plan 
todo soWe have no plans to secure our 
software supply chainDont knowcontract, and 39% require vendor security self\-
assessments (Figure 14\). When organizations 
ask vendors to conduct self\-assessments, they 
are looking for information such as vulnerability 
managementinformation(68%),datasecurity 
controlsbeingused(60%),documentation 
onthevendorsdesignandtestingprocess 
(44%),andthevendorsassetinventoryand 
usermanagementpractices(41%)(Figure 
15\). About a third of respondents (35%)want 
answers to questions pertaining to the vendors 
supply chain levels for software artifacts (SLSA), 
and 38% want a list of vulnerable packages.Theuseofvendorsecurityriskassessment 
questionnaires has become more widespread, 
andnumerousstandardizedquestionnaires 
are readily available for organizations to adapt 
for their use. Among the most widely used are 
the Shared Assessment Groups Standardized 
InformationGathering(SIG)questionnaire,the 
National Institute of Standards and Technology 
(NIST)vendorquestionnaire,andtheVendor 
Security Alliance questionnaire.Nearly three\-quarters, or 74%, of organizations 
requiremultifactorauthenticationforthird\-
partyaccesstosecureenvironments,andThe State of Supply Chain Threatsleast\-privilegeaccessrules 
57%enforce 
(Figure 16\). Nearly half (49%) of organizations 
have segmented their networks to limit lateral 
movement; 34% require vulnerability scanning 
ofvendorsystems;and22%relyoncode 
analysis, including binary analysis.thatconcernsabout 
Thesurveyshows 
supplychainattacksmaybetheoreticalfor 
manyenterprises.Justaquarter(24%)of 
respondents say they have experienced supply 
chain attacks over the past year, but 60% state 
they have not (Figure 17\). Among the victims, 
thetwomostcommontypesofattacks 
werethosetargetingthepartnerecosystem 
(43%)andthoseexploitingvulnerabilitiesin 
(41%)(Figure18\). 
softwarecomponents 
Despiteconcernsabouttyposquattingand 
dependencyconfusion,onlyaboutathird 
(34%)ofrespondentswhohadexperienced 
asupplychainattacksaytheirdevelopers 
hadaccidentallydownloadedmaliciouscom\-
ponents from public repositories, such as npm, 
PyPI, and Maven.ConclusionMany companies have worked to overhaul their 
supply chain management practices to address 
risk from vulnerable open source components 
andthird\-partycommercialsoftwareovertheDark Reading ReportsAugust 202314Table of ContentsThe State of Supply Chain ThreatsFigure 7\.Concerns About Software Supply Chain
Thinking specifically about the software supply chain, please rank the following issues that cause you the 
most worry from high to low.Overall rankScoreVulnerabilities in third\-party libraries affecting the security of our 
applicationDevelopers downloading and importing malicious packages and 
componentsAttackers tampering with libraries and code repositories to include 
malicious codeSoftware components used in our code, which is no longer being 
maintainedVulnerabilities in build tools and development frameworks used in 
software development12345Note: Rank is based on a weighted score. Responses are weighted, and scores represent the sum of all weighted counts. 
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023800724602590552past two years. Recent vulnerabilities in widely 
usedsoftwareproductsandopensource 
componentsappeartobefuelingalotofthe 
change.A substantial number of organizations in Dark 
Readings2023SupplyChainThreatsSurvey 
haveimplementedcomprehensivecontrols 
and recommended best practices such as 
maintainingSBOMsandconductingvendor 
questionnairesformitigatingsupplychain 
risk.Butmanymorehavenotimplemented 
thesepracticesand,bytheirownadmission, 
arealongwayfromsecuringtheirsoftware 
supplychain.Evenso,mostITandsecurity 
leadersviewtheirorganizationsasreadyto 
prevent,detect,andrespondtosupplychain 
breachessuggestingapotentialdisconnect 
between perception and reality.Dark Reading ReportsAugust 202315Table of ContentsFigure 8\.IX
DNEPP
AThe State of Supply Chain ThreatsFigure 9\.Vendor Scorecards
Does your organization rely on vendor 
scorecards or rating scores to assess the 
security of open source components?Managing Software Supply Chain
How does your organization manage the software supply chain?20232022We use dependencies that come from only trusted repositories
and registries 40% 
 37%We regularly check container images for high or critical 
vulnerabilities 36% 
 40%20%We rely on third\-party tools to manage dependencies and 
vulnerabilities 36% 
 32%We rely on automation to minimize inputs and reduce the
attack surface 33% 
 39%47%YesNoDont knowWe accept signed components and verify signatures
before deployment 32% 
 27%33%We require administrator access for build processes and tools 32% 
 27%We verify code components and build binaries from source code 
before importing 28% 
 24%We require all code to be reviewed by at least one other person 26%
 NAWe verify the changelog and commit history for the code 
component and project before importing 26% 
 28%For application builds, we execute the steps in ephemeral, isolated, 
or hermetically sealed environments 25% 
 25%We are currently defining and developing our process 20%
 NAWe only accept commits signed with a developers GPG key 15% 
 9%We verify provenance attestation of source code 14%
 NANote: Multiple responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022Data: Dark Reading survey of 242 cybersecurity and IT professionals, 
June 2023Dark Reading ReportsAugust 202316Table of ContentsFigure 10\.The State of Supply Chain ThreatsSoftware Bills of Materials
Please tell us how strongly you agree or disagree with the following statements about the software bill of 
materials.Strongly 
agreeSomewhat 
agreeNeither 
agree nor 
disagreeSomewhat 
disagreeStrongly 
disagreeMy organization maintains a software bill of materials 
(SBOM) repositoryI believe my organization will increase the use of SBOMs 
in the next 12 monthsMy organization uses the SBOM for vulnerability 
managementMy organization regularly requests SBOMs from vendors 
and suppliersMy organization creates complete SBOMs for all software 
we build16%18%13%12%14%Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 202334%30%28%29%22%33%41%37%34%40%9%8%12%15%13%8%3%10%10%11%Figure 11\.Build Practices to Prevent Software Supply Chain Attacks
How difficult is it to implement the following build practices and methods for preventing, mitigating, andor 
remediating software supply chain security attacks?Using a hermetic build with all inputs declared with
immutable referencesMaking provenance information (whenwherehow the 
software was produced) availableAll build steps must be run on a build service not locally on 
a developers workstationRe\-running builds with the same input artifacts must result in 
bit\-by\-bit identical outputRunning builds in an ephemeral environment, such as a 
container or virtual machine, or in an isolated environmentData: Dark Reading survey of 242 cybersecurity and IT professionals, June 20231 \- Not 
difcult 
at all2%3%8%6%6%2345 \- 
Extremely 
difcult45%27%46%19%16%13%51%20%7%10%19%14%15%52%23%47%19%14%8%10%Dark Reading ReportsAugust 202317Table of ContentsFigure 12\.The State of Supply Chain ThreatsSoftware Supply Chain Statements 
Please tell us how strongly you agree or disagree with the following statements about the software 
supply chain.My organization will be able to detect and respond to a 
software supply chain compromiseShifting left is necessary to secure the software
supply chainI believe our architects and developers have the 
necessary knowledge and expertise to ensure a secure 
software supply chainMy organization has a way to detect software tampering 
across the software supply chainData: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023Strongly 
agreeSomewhat 
agreeNeither 
agree nor 
disagreeSomewhat 
disagreeStrongly 
disagree18%20%46%35%27%40%8%4%23%30%31%13%19%32%31%12%1%1%3%6%Figure 13\.Effect of Recent Attacks on Organizations Approach to Supply Chain Security
How have attacks against trusted third\-party software such as Microsoft Exchange, Kaseya, and 
Accellion changed your organizations approach to supply chain security?10%17%7%6%21%10%24%22%39%44%20232022Data: Dark Reading survey of 242 cybersecurity and IT professionals in
June 2023 and 115 in June 2022We are making major changes to 
address supply chain threats from 
third\-party suppliers and partnersWe have made a few changes to 
address supply chain threats from 
third\-party suppliers and partnersWe have not made any changes, 
but we plan to do so this yearWe have not made any changes, 
and we have no plans to look at 
supply chain this yearDont knowDark Reading ReportsAugust 202318Table of ContentsFigure 14\.The State of Supply Chain ThreatsMinimizing Third\-Party Risk
Thinking about supplier risk, which of the following do you do to establish or validate trust in your suppliers and minimize third\-party risk?20232022We stipulate security standards that suppliers must adhere to as part of the contractWe regularly monitor and assess suppliers security practicesWe ask suppliers to complete self\-assessments describing their security controlsOur suppliers have to submit independent audits or assessments indicating they meet security 
requirements 51% 
 55% 44% 
 37% 39% 
 50% 32% 
 39%We generate our own supply chain information about our security processes and provide
them to our partners 18% 
 16%We request point\-in time assessments to understand the suppliers security postureWe require continuous validation to ensure suppliers have the necessary security controlsWe verify the results of the suppliers risk assessment 20% 
 29% 35% 
 33% 29% 
 23%We currently do not validate trust in suppliers or do anything to minimize third\-party risk 9% 
 6%Note: Multiple responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022Dark Reading ReportsAugust 202319Table of ContentsFigure 15\.Types of Information for Supply Chain Assessment
When you ask for a supply chain assessment, what types of information are you looking for?20232022The State of Supply Chain ThreatsVulnerability management informationData security controls being usedDocumenting the design and testing processAsset inventory and user management informationList of vulnerable packagesSupply chain levels for software artifacts (SLSA)Description of process flowsOther 68% 
 61%
 60% 
 47% 44% 
 50% 41% 
 54% 38% 
 40%
 35% 
 45% 31% 
 32%
 7% 
 2%Note: Multiple responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022Figure 16\.Securing the Supply Chain
What security controls and processes do you rely on to secure the supply chain?20232022We use multifactor authentication to secure accountsWe require using least\-privilege access controlWe require data to be encryptedWe segment the network to prevent lateral movementWe rely on zero trust to manage authentication and access controlWe conduct penetration testing engagements involving our suppliersWe require vulnerability scanning for our suppliers systemsWe are automating as much as possible and moving away from manual processesWe rely on code analysis, including binary analysisWe currently do not have any security controls or processes to secure the supply chainNote: Multiple responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022 74% 
 62%
 57% 
 48%
 54% 
 51%
 49% 
 38%
 45% 
 39%
 35% 
 29%
 34% 
 34%
 34% 
 38%
 22% 
 30%
 4% 
 3%Dark Reading ReportsAugust 202320Table of ContentsFigure 17\.The State of Supply Chain ThreatsSupply Chain Attack
Has your organization experienced any kind of supply chain attacks over the past year?6%16%11%9%18%48%202260%2023Figure 18\.Yes, we have experienced 
many supply chain attacksYes, we have experienced 
some such attacks32%No, we have not experienced 
such attacksDont knowData: Dark Reading survey of 242 cybersecurity and 
IT professionals in June 2023 and 115 in June 2022Types of Attacks
Which types of supply chain attacks did your organization experience over the past year?Attackers targeted my organization after compromising a 
third\-party partnerAttackers exploited a software vulnerability in a component 
used by an application 43% 41%An attack on our supplier disrupted our business processes 39%Our developers accidentally downloaded malicious 
components from npm, PyPI, Maven, or other code registriesAttackers exploited vulnerabilities in frameworks and other 
developer tools used to create applicationsThere was a backdoored component in hardware devices 
used by my organizationAttackers stole secrets, such as credentials and tokens, from 
one source and used them to gain unauthorized access to my 
organizations systemsNote: Multiple responses allowed
Base: 58 respondents who have experienced supply chain attacks 
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023Other 34% 27% 20% 20% 7%Dark Reading ReportsAugust 202321Table of ContentsFigure 19\.Figure 21\.The State of Supply Chain ThreatsCurrent Protection Against Software Supply Chain Threats
Does your organizations current security program cover software supply 
chain threats?3%10%16%28%Our security program covers 
software supply chain threatsOur security program covers 
supply chain threats but 
doesnt explicitly specify 
software supply chainNo, our security program does 
not cover any kind of supply 
chain threatsWe do not have a security 
program43%Dont knowRespondent Region of Residence
In what region do you live?
3%3%4%4%6%11%North AmericaEast Asia or PacicLatin America, South America, 
or Caraibbean (including 
Mexico)Europe or Central Asia69%South AsiaMiddle East or North AfricaSub\-Saharan AfricaData: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023Figure 20\.Insurance Partner for Reducing Third\-Party Risk
Do you consider your insurance carrier an effective partner in reducing third\-party risk?26%37%26%44%YesNoDont know30%2023Data: Dark Reading survey of 242 cybersecurity and 
IT professionals in June 2023 and 115 in June 202237%2022Dark Reading ReportsAugust 202322Table of ContentsFigure 22\.Figure 23\.Respondent Job Title
Which of the following best describes your job title?Respondent Company Size
How many employees are in your company in total?The State of Supply Chain Threats2%7%13%7%IT executive (CIO, CTO)Cybersecurity executive (CSOCISO)Chief privacy ofcerVP of ITVP of securityIT directorhead3%6%4%10%9%Cybersecurity directorhead1%3%IT managerCybersecurity manager8%5%IT staffCybersecurity staffEngineer7%8%7%SoftwareWeb developerNetworksystem administratorCorporate executive (CEOPresidentCOO)Data: Dark Reading survey of 242 cybersecurity 
and IT professionals, June 2023ArchitectOtherFigure 24\.Respondent Industry
What is your organizations primary industry?22%27%32%19%5,000 or more1,000 to 4,999100 to 999Fewer than 100Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 20233%13%14%Computer or technology manufacturertech vendorCommunications carrierservice provider3%3%3%3%3%3%11%Bankingnancial servicesVCaccountingConsultingbusiness servicesInsuranceHMOsAerospaceHealthcarepharmaceuticalbiotechbiomedicalConstructionarchitectureengineeringGovernmentMediamarketingadvertising9%Manufacturing, industrial, process (noncomputer)UtilitiesSolutions providervalue\-added reseller (VAR)Wholesaletradedistributionretail5%6%8%EducationOther6% 7%Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023Dark Reading ReportsAugust 202323