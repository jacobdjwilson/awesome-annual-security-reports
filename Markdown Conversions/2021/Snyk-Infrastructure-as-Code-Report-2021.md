SNYK RESEARCH REPORTInfrastructure 
as Code Security 
InsightsFebruary 2021IntroductionCloud native applications are more than just thecode developers create \- todays applications includeKEY TAKE AWAYinfrastructure as code (IaC) that dictate how theRespondents performing automatedapplications are setup on cloud infrastructure and howsecurity testing as part of their releasecontainerized applications will run on Kubernetes. Thepipelines were faster to find and fixuse of IaC allows for faster, repeatable deployments,vulnerabilitiesCan you fix an issue in under 1 day?76%Teams with fully 
automated security 
checks59%Teams with no or only 
partially automated 
security checks38%Teams that only 
check security 
after deploymentbut its usage also increases the burden on developersto secure not only their code, but also the infrastructureconfiguration, in addition to code dependencies andcontainers.In this survey, Snyk sought to take stock of how IaC isbeing deployed by companies both large and small.Feedback from a wide range of roles in these companieswent into our outlook on the state of IaC, highlightingthe value of IaC, as well as also roadblocks to itswidespread use and what we can do to overcome them.While our survey shows that many organizations havenot coalesced on one right way to use IaC or whoshould be responsible for writing and maintaining it, wedid find that respondents who are taking advantage ofautomated security testing for their IaC definitions arefinding and fixing misconfigurations faster than theirpeers. The high performers in our survey are finding andfixing issues in their IaC definitions within a single day;whereas the lower performers take more than a weekto realize there is a security issue and then then upto 2 more days to fix it.SEE SNYK IAC IN ACTIONCurrent IaC PracticesThe benefits to speed and reliability when everything is in codeand automated can be immense. But the benefits do come witha cost, namely an increasing burden on developers to securenot just their own code but its dependencies, containers, andnow, the infrastructure configuration. To start our research, wefirst explored what companies were taking on the challenge ofimplementing IaC and which tools theyre currently using as theydevelop best practices.We found that many companies are only starting out on their IaCjourney, with 63% just beginning to explore the technology andonly 7% stating theyve implemented IaC to the best of currentindustry capabilities. While there are many tools either in use or63%of companies are juststarting out7%of companies arebeing considered, 71% would prefer to standardize on a commonimplementing the best oftoolset workflow across all IaC configuration types and formats.current industry capabilitiesIn use todayAWS CloudFormationAzure Resource 
ManagerConsidering for the future36%Cloud SDKs (AWS CDK, 
Azure SDKs)30%AWS CloudFormationKubernetes (incl. YAML, 
JSON and Helm)25%AnsibleTerraformDocker ComposeGoogle Could 
Deployment Manager17%14%14%14%Kubernetes (incl. YAML, 
JSON and Helm)Azure Resource ManagerGoogle Could 
Deployment ManagerOther Kubernetes toolsServerless Framework26%24%22%18%18%16%14%The opportunity is still wide open for most organizations to lay a firm foundation and implement the right tools andpractices before widely adopting IaC.3SNYK RESEARCH REPORTInfrastructure as Code Security Insights We looked at how three different clusters ofIt may come as no surprise that the fully automatedrespondents to our survey fared when it comes togroup outperformed both of the other groups atfinding and fixing configuration issues that ariseboth discovering and fixing issues. When it comes tofrom using infrastructure as code:finding issues, the high performers were able to dis\-Full automation:
These respondents said they always performedcover issues in less than a day roughly twice as oftenas respondents in the other two groups. And the fullyautomated cluster was able to fix issues quickly, inautomated security testing as part of their releaseless than half a day, over 60% more often than eitherpipelines.of the other clusters.Less than full automation:
This cluster includes respondents who have no auto\-There were differences at the other end of theresponses, too. The two lower performing clustersmation up to those who have partial automation oftook 1 week or more to discover IaC issues in oversecurity checks.Only post\-deployment checks:
This cluster may use some automation, but theyhalf their cases, where the fully automated clusteronly took that long 30% of the time. Fixing the issuesis where the cluster that only runs post\-deploymentchecks really suffered. They were only able to fixonly perform checks after infrastructure is deployed,these IaC issues in less than a day half as often as theeither via audit tools, pen testing, or investigatingfully automated respondents, and in 62% of the casessecurity incidentsit took longer than a day to implement the fix.Can you detect an issue in less than 1 day?Can you fix an issue in less than 1 day?34%14%18%76%59%38%How often do you go 1 week or 
longer before finding an issue?How often does it take you over a 
day to fix an issue?30%54%60%25%41%62%4Fully automatedFully automatedFully automatedFully automatedNot automatedNot automatedNot automatedNot automatedChecks after deploymentChecks after deploymentChecks after deploymentChecks after deploymentBy 2025Does SpeedEquate to Safety? 70%Currently, modern applications deployof attacks against containers will be from 
known vulnerabilities and misconfigurations 
that could have been remediated.
Gartner, 2020Do you include IaC security 
tests in your CI pipeline24%Always40%No CI testing7%Sometimes27%Usuallyautomatically on infrastructure created andconfigured via code. As a result, security so oftentakes a back seat to a speedy deployment, meaningconfiguration issues are not uncovered until afterthese applications have been deployed. EvenGartner\* states, By 2025, 70% of attacks againstcontainers will be from known vulnerabilitiesand misconfigurations that could have beenremediated.Yet, all this does not necessarily mean speed isinherently risky when it comes to IaC. In fact, theautomated testing and release gates that are inplace for other forms of code can be used withIaC and help make security best practices part ofthe development and release process. The highestperformers in this survey \- those who are bothfinding and fixing configuration issues fastest \- are already doing exactly thatGartner Magic Quadrant for Application 
Security Testing; April 2020SNYK RESEARCH REPORT
Infrastructure as Code Security Insights5Current IaC 
Security PracticesWhile the highest performers are finding and fixing security issues as part of their releasepipelines, this type of automated testing is still nascent when it comes to security testing.Of those surveyed, 60% said their current workflow for IaC and configuration code doesgo through continuous integration (CI) testing, but security checks are not always part ofthose tests. Only 32% of respondents include security checks in their pipelines. In fact, mostsecurity issues are still being discovered after deployment, through pen testing, audits, andinvestigating security incidents. For those who are only using these post\-deployment checks,it takes a week or more to discover a security issue in half the cases and over a day to fixthose issues in nearly 23 of the cases. All in all, thats potentially 9 days of running with asecurity vulnerability versus less than one day for the highest performers.How do you find out about security 
issues in your configurations and IaC?45%43%35%33%32%Audit running 
environments 
after deploymentPen testingManual code 
scansFrom investigating 
incidentsAutomated 
testingCI21%Tools from our 
IaC or public 
cloud provider6SNYK RESEARCH REPORTInfrastructure as Code Security Insights 41%said their barrier was 
unclear benchmarks for 
securitySo what is standing in the way 
of making a change?For those who said their IaC and configuration code goesthrough CI testing, the biggest barrier to integrating securitychecks is a lack of standardized best practices on what to check,with each of their separate teams making their own decisionabout what to test. When you couple that with the 41% whosaid their barrier was unclear benchmarks for security, theshortest path to improved IaC security can bepaved withbetter tools that offer clearer guidance, while still providingteams with the freedom to determine whats most importantfor their needs.62%What is limiting you from always integrating 
security checks into the IaC testing process?41%22%22%16%11%Each team 
makes their 
own decisions 
about what to 
testWo do not have 
a clear set of 
benchmarks on 
what to test 
againstWe do not 
have the right 
testing toolsWe have not 
decided what 
is important for 
us to testConcerned it 
would slow us 
down too muchThere is no clear 
owner to address 
issues that are 
discovered7SNYK RESEARCH REPORTInfrastructure as Code Security Insights Infrastructure 
RemediationFinding the issue is just one piece of thepuzzle \- once an issue is discovered somebodyhas to fix it. When faced with a choice, 52%of respondents claim they usually remediatea security issue by directly tweaking theinfrastructure instead of addressing it bymodifying the IaC source code. This opensup the possibility for a number of issues inthe long\-term because the infrastructureand the codified definitions used to create itwill start to drift; either that or the modifiedinfrastructure will be reset to its misconfiguredstate on the next deployment. For thosethat choose this manual remediationpath, their reasoning is split between alack of standardization, knowledge, andcommunication, along with a desire to speedup the fixes as much as possible.52%remediate a security issue
by directly tweaking the
infrastructure instead of
addressing it by modifying 
the IaC source codeHow often do you directly 
modify infrastructure, rather 
than fixing the configuration 
in your IaC code?13%Never \- we always 
fix the code first34%
Often18%Most of the time \- 
we usually change 
the infrastructure 
directlyinstead 
of modifying the 
cource code35%RarelyWhy do you directly modify the 
infrastructure instead of fixing 
the code?39%38%38%23%23%22%Lack of standardized 
workflow and 
practicesConcern that
redeploying from code 
will create new issuesFastereasier 
to tweak the 
infrastructureTracing infrastructure 
issues back to code is 
complexslowLack of communication 
between developers 
and operatorsLack of security 
knowledge in the team 
responsible for the code9%No automated tests 
to ensure the IaC 
changes work beforeSNYK RESEARCH REPORT
Infrastructure as Code Security Insights861%said speed\-related issues were 
the reason they remediate a 
security issue manuallyWhile a lack of standardized workflow and prac\-tices was the leading reason respondents chose toremediate a security issue manually, a total of 61%of respondents also pointed to speed\-related issues.Namely that its faster andor easier to tweak theinfrastructure because tracking issues back to the IaCdefinitions is too complex andor slow. Again, thispoints to two underlying issues:First, when security checks are only performed afterinfrastructure has been deployed, its too late in theprocess. It separates the security checks from thecode and its likely that pen test reports and audittools dont provide data thats directly actionable bythe owners of the IaC code.Second, for teams that are stretched thin, a lack ofbandwidth could lead to the decision (consciouslyor not) to overlook some security in favor of speed.For those teams that are at their limit, the right toolscan make a world of difference to equip developerswith what they need to prioritize security. But beforea tool can be decided on, teams must first determinewho holds final responsibility for IaC.SNYK RESEARCH REPORT
Infrastructure as Code Security Insights9Who Holds 
Responsibility for 
IaC Security?One of the barriers to shifting IaC security leftwas that teams struggled to standardize prac\-tices across their organization, leaving eachteam to audit IaC as they see fit. In additionto the obvious security issues this presents, itspeaks to a larger disconnect on responsibility.A common theme of this survey is the diffi\-culty to pin down security ownership whenit comes to IaC \- so where does the industrycurrently stand?Today it seems there is no consensus on whois responsible for the security within IaC.Developers and DevOps roles have a slightlybigger role than other individual teams and agood number say its a shared responsibility,potentially fitting in to the newer DevSecOpsmodels. When asked which team should beresponsible for IaC security, if it is not a sharedresponsibility, the answers shifted heavily tothe developers DevOps groups.So whats stopping these security responsibili\-ties from shifting further left? Mostly, its con\-fidence in the broader organizations ability toreadily spot and fix issues in the code.Who is responsible for
configuration security in IaC 
today?29%28%23%20%Developers
DevOpsIt is a shared 
responsibilitySecurityInfrastructure52%Who should be 
responsible?24%24%Developers
DevOpsInfrastructureSecuritySNYK RESEARCH REPORT
Infrastructure as Code Security Insights10Snyk Infrastructure as Code: Find and fix configuration 
security issues the way cloud native experts do.A clear and scalable solution to IaC security challenges is to invest in the tools and training needed to drive upconfidence and help with bandwidth for these teams, allowing them to deploy code quickly and securely. In thesame report cited above, Gartner also sees the potential for these automated tools and predicts that, by 2025,organizations will speed up their remediation of coding vulnerabilities by 30% with code suggestions appliedfrom automated solutions, reducing time spent fixing bugs by 50%.How confident are you 
in your ability to spot 
configuration issues in IaC?4%Greatly 
confident22%Fairly 
confident25%49%Not 
confidentSomewhat 
confidentSnyks long\-standing developer\-first approach led tothe creation of Snyk Infrastructure as Code (Snyk IaC)to help solve these problems. This latest tool moves thesecurity controls for infrastructure and configurationsto the beginning of the development lifecycle, so devel\-opers can proactively determine whether their applica\-tion and infrastructure specifications are safe. Designedto fit a developers workflow, Snyk IaC helps pinpointhow to write secure Kubernetes and Terraform config\-urations, and even provides automated fixes as codein your choice of source code management systems.Together with Snyk Container and Snyk Open Source,you can finally embed your security expertise acrossyour entire development organization.To secure your organization and learn more aboutSynk IaC visit snyk.ioproductinfrastructure\-as\-code\-security.67%What would make you more confident in your 
organisations ability to spot IaC misconfigurations?48%42%37%29%26%22%Professional 
trainingAutomated code 
testing for IaC 
in CICDAudit tools 
specific to 
IaC and 
configurationPlaybooks to 
followTools built\-in 
to IDEsPeer
mentoringIndustry or 
infrastructure 
vendor 
benchmarks11SNYK RESEARCH REPORTInfrastructure as Code Security Insights Survey 
MethodologyThis vendor neutral research wasindependently conducted by VirtualIntelligence Briefing (ViB). ViB is an interactiveon\-line community focused on emergingthrough rapid growth stage technologies. ViBscommunity is comprised of more than 2\.2M ITpractitioners and decision makers who sharetheir opinions by engaging in sophisticatedsurveys across multiple IT domains.The survey methodology incorporatedextensive quality control mechanisms at 3levels: targeting, in\-survey behavior, and post\-survey analysis. The Calculated Margin of errorat a 95% confidence level is 3\.9%.After receiving 543 responses from members ofour opted\-in 2M\+ IT community, we screenedout about 120 respondents who met the role,level and company size requirements, butwho indicated they were not currently using,or considering using, the IaC Configurationtools listed in the survey. This extensiveprocess led to a survey pool of 481 qualifiedindividuals in order to present the mostaccurate look at the current state of IaC.Survey respondents 
by role11%30%Cloud \&
PlatformDevelopers 
and DecOps31%Infrastructure12%Architects16%Security \& 
ComplianceSurvey respondents by 
company size28%1 \- 500 
employees23%500 \- 100015%2000 \- 500014%1000 \- 20008%5000 \- 10,0008%15,000\+4%10,000 \- 
15,00012SNYK RESEARCH REPORTInfrastructure as Code Security Insights SEE SNYK IAC IN ACTION