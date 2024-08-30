The State of Open Source Security
VulnerabilitiesWhiteSource Annual Report 20212020 presented us all with a set of challenges no one could have expected.The pandemic initially raised a lot of uncertainty in the software developmentindustry. Companies pivoted to remote work practically overnight and faceda series of issues encompassing everything from application security toemployee well\-being.Shifting to work from home introduced new security threats. Early on many 
Shifting to work from home introduced new security threats. Early on manyorganizations budgets were put under scrutiny, and many worried thatinvestment plans for application security strategies would be put on the backburner while many industries went into survival mode.In this report, we analyzed WhiteSources open source vulnerabilities 
In this report, we analyzed WhiteSources open source vulnerabilitiesdatabase to gain insights on the state of open source security and learn howto best address the challenge of developing secure software products at thespeed of DevOps.The Number of Open Source 
Vulnerabilities Continues to RiseAccording to the WhiteSource database, aggregated from the NVD, dozens ofsecurity advisories, peer\-reviewed vulnerability databases, and popular opensource issue trackers, the number of published open source softwarevulnerabilities in 2020 rose once again, by over 50%.Open Source Vulnerabilities per Year: 2009\-202010000750050002500096586111409242177008001012500123514261213142120092010201120122013201420152016201720182019 2020The Open Source Development and Security 
Communities: More Active Than EverThere are a few possible explanations to the sharp increase in the 
number of known open source vulnerabilities in 2020\.First is First is increased activity in the open source community. While 
no one was sure how shifting to remote work would eect 
developers, it appears that in the rst months of the pandemic 
open source developers were working harder than ever. GitHub 
reported a sharp increase in open source project creation in 
March and April 2020\. This rise in activity most probably extended 
to more open source security research.The addition of CVE Numbering Authorities (CNAs) also 
The addition of CVE Numbering Authorities (CNAs)
contributed to the increase in published vulnerabilities. GitHub 
Security Labs, launched over a year ago, invested a lot of eort in 
detecting, xing, and publishing vulnerabilities in open source 
components. Since then more software development 
organizations have joined the open source communitys eorts to 
ensure issues are analyzed, xed, and published as soon as 
possible. 
possible.In addition to the many hands on deck, automation also explains 
the high number of open source vulnerabilities discovered this 
year. Security researchers are using automated scanning and 
detection tools to nd vulnerabilities, enabling them to nd and x 
security issues quickly, and at a greater volume.In some cases, researchers found multiple CVEs where a common 
In some cases, researchers found multiple CVEs where a common 
problem aected many projects. Sometimes a single CVE was 
applied to many projects but other times it was correct for them 
to each have their own CVE.Most Common CWEs 
in Open Source ComponentsAs AppSec continues to shift left into the design and 
development phases and responsibility over security is 
shared with developers, secure coding practices and tools 
become an important part of the DevSecOps pipeline.In order to gain insights on secure coding with open source 
In order to gain insights on secure coding with open source 
components, we decided to dive deep into the data on the 
most common CWEs in vulnerable open source components 
detected in 2020\.CWE\-79CWE\-200CWE\-20CWE\-787CWE\-125Open Source Vulnerabilities 
in 2020: Top CWEs201520162017201820192020CWE\-79CWE\-119CWE\-119CWE\-79CWE\-79CWE\-79XSSBuer OverowBuer OverowXSSXSSXSSCWE\-119CWE\-264CWE\-79CWE\-190CWE\-20CWE\-787Buer OverowPermissions, 
Privileges, and 
Access ControlsXSSInteger OverowImproper Input 
ValidationOut\-of\-bounds 
WriteCWE\-264CWE\-20CWE\-125CWE\-119CWE\-125CWE\-125Permissions, 
Privileges, and 
Access ControlsImproper Input 
ValidationOut\-of\-bounds 
ReadBuer OverowOut\-of\-bounds 
ReadOut\-of\-bounds 
ReadCWE\-200CWE\-200CWE\-200CWE\-20CWE\-89CWE\-20Buer Errors
Information 
ExposureInformation 
ExposureInformation 
ExposureImproper Input 
ValidationSQL InjectionImproper Input 
Improper Input 
Validation
ValidationCWE\-20CWE\-79CWE\-20CWE\-125CWE\-352CWE\-200Improper Input 
ValidationXSSImproper Input 
ValidationOut\-of\-bounds 
ReadCSRFInformation 
Exposure12345Buer ErrorsOpen Source Vulnerabilities 
in 2020: Top CWEsTop CWEs in 2020123456789CWE\-79XSSCWE\-787Out\-of\-bounds WriteCWE\-125Out\-of\-bounds ReadCWE\-20Improper Input ValidationCWE\-200Information ExposureCWE\-416Use After FreeCWE\-89SQL InjectionCWE\-22Path TraversalCWE\-352CSRF10CWE\-190Integer OverowWhile CWE\-79 (Cross\-site scripting) has 
been at the top of the list for the past 
few years, CWE\-787 is a new arrival to 
the top ve.It might seem like CWE\-787 came out 
of nowhere, but its actually a 
of nowhere, but its actually a 
descendent of the common CWE\-119 
(Buer overow), which saw a decrease 
this year.We can also see that 
CWE\-125, another child of CWE\-119, is 
also a prominent issue.It appears there was an eort to map 
It appears there was an eort to map 
CVEs directly to weaknesses like 
CWE\-787 and CWE\-125 instead of 
categories like CWE\-119\. This included a 
large remapping eort of over 10,000 
CVE entries.Improper Input Validation and 
Improper Input Validation and 
Information Exposure are other 
examples of categories that are being 
remapped into the more precise 
weaknesses.Open Source Vulnerabilities 
in Top Programming LanguagesContinuing our research into secure coding, we also looked 
at some of the top programming languages, including how 
many and what type of open source security vulnerabilities 
were disclosed per language.Top CWEs per Programming 
Language 2020123We checked which CWEs weremost prominent in some of theCWE\-79CWE\-862CWE\-502most popular programmingXSSMissing 
AuthorizationDeserialization of 
Untrusted Datalanguages.CWE\-79CWE\-20CWE\-787XSSImproper Input 
ValidationOut\-of\-bounds 
WriteCWE\-79CWE\-89CWE\-352XSSSQL InjectionCross\-Site Request 
ForgeryCWE\-79CWE\-20CWE\-200XSS Improper Input 
Validation Information 
ExposureCWE\-200CWE\-79CWE\-863Information 
ExposureXSS Improper Input 
ValidationCWE\-787CWE\-125CWE\-476Out\-of\-bounds 
WriteOut\-of\-bounds 
Read NULL Pointer 
DereferenceCWE\-732CWE\-200CWE\-20Incorrect 
Permission 
Assignment for 
Critical ResourceInformation 
ExposureImproper Input 
ValidationCross\-site scripting (CWE\-79\) 
Cross\-site scripting (CWE\-79\)continues to dominate in mostof the programming languagesthat we looked at, especiallythose used for webdevelopment. Another reasonfor how common XSS issues areis that they are very easy to 
is that they are very easy todetect using automated tools.We also see that many of thenewly discovered CWE\-787Out\-of\-bounds writevulnerabilities were discoveredin C.Vulnerabilities in Top Programming 
Languages: 2020 vs. 20192020201930%20%10%0%CC\+\+The increase in Buer overow related issues is one of the reasons that C saw 
so many new vulnerabilities in 2020\.According to GitHubs 2020 Octoverse, PHPs popularity is decreasing in the 
open source community. The decrease in the number of vulnerabilities in PHP 
is probably a result of decreased community interest.Go, on the other hand, is gaining popularity along with increased security 
Go, on the other hand, is gaining popularity along with increased security 
research. Last year Go vulnerabilities amounted to only 1% of vulnerabilities in 
all programming languages, compared to 5% in 2020\.Go is a relatively young language, and the rising number of vulnerabilities 
discovered in Go might also be because many of the Go projects are written 
from scratch, rather that using open source libraries and components that have 
been under the security microscope for years.Open Source Vulnerabilities: 
Severity BreakdownAddressing the sharp rise in the number of open source 
vulnerabilities published this year is a major challenge for 
software development organizations. As security debt 
continues to rise for most, its important to nd a way to 
prioritize vulnerabilities remediation. 
One parameter that many organizations look to when 
One parameter that many organizations look to when 
attempting to decide what to remediate rst is the 
vulnerabilities severity score.We checked the breakdown of open source vulnerabilities 
severity scores to see if this is an eective technique.Open Source Vulnerabilities in 2020: 
Severity BreakdownThe fact that over 50% of new open source security vulnerabilities are ratedhigh or critical doesnt help security and development teams that rely onseverity scores when considering which issues to address rst.Fixing all issues, or even only high and critical issues, is an unrealistic plan forteams that want to keep up with the rapid pace of development.Organizations need to leverage prioritization and remedian tools that target the 
Organizations need to leverage prioritization and remedian tools that target thevulnerabilities that will most impact their systems and business if they want tomanage their security debt wisely.Medium:
45%Critical:
15%Low:
3%High:
38%Final ThoughtsDespite how tumultuous 2020 turned out to be, it turns out 
application security and open source security in 
particular remains a top concern and priority for both the 
software development industry and the open source 
community.The sharp increase in the overall number of open source 
The sharp increase in the overall number of open source 
vulnerabilities published in 2020 is another reminder that 
open source security must be addressed as an integral part 
of an organization's AppSec strategy, and requires 
organizations adopt a set of security practices. These 
include auto\-remediation and a vulnerabilities 
prioritization strategy, ensuring that the issues that pose 
the biggest threat are addressed rst.
the biggest threat are addressed rst.