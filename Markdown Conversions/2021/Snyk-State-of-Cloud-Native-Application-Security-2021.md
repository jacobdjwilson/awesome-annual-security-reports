State of Cloud Native Application SecurityHow cloud native adoption transforms the way organizations defend against security threats99% of companies recognized security as important to their cloud native strategySuccess in the cloud native era is defined by an organization's ability to deliver new versions of software faster and more efficiently, which is reinforced by our survey results. Being able to deploy code to production faster and more easily manage those applications were the primary reasons for moving towards containerized infrastructure. However, as companies embrace cloud native technologies as part of their digital transformation, security is seen as a key factor to building successful platforms. While only 36% of respondents stated that security was one of the main reasons for moving their production applications into containers, 99% of respondents recognized security as an important element in their cloud native strategy. In addition, over 80% stated security is very important to them.Snyk Report: State of Cloud Native Application Security \| 01
What are the main reasons for moving your applications into containers?How important is security to your cloud native strategy?Deploymentvelocity%68Ease ofmanagement%67Reducecosts%43ImprovedsecurityAttracting talent%11%36Very
important83%Somewhat
important16%Not important1%As cloud native adoption increases, security needs to be built in as standardOver 78% of production workloadsare deployed as containers orserverless applicationsIn total over 78% of production workloads are deployed ascontainers or serverless applications. Containers continue tobe the dominant mechanism for cloud native applicationdeployment, with nearly 60% of production workloads deployedin containers. Penetration of serverless technologies is nowsignificant across all company sizes, and makes up more thana fifth (mean average) of all production workloads. Usage ofcloud native technologies is strongacross all company sizes,indicating that adoption is becoming mainstream. With over50% of respondents workloads also being deployed with someform of Infrastructure As Code, use of software\-driveninfrastructure has increased alongside the container andserverless growth trends. Usage of these core technologies isone of the key indicators of cloud native transformation ingeneral, and so we use these metrics throughout this report asindicative of the level of adoption within an organization.58%21%51%ContainersServerlessIaCSnyk Report: State of Cloud Native Application Security \| 02While 95% of respondents useAre your application deployments manualautomation, only 33% fullyautomate their deploymentpipelineDeployment automation is one of the key tenets ofcloud native practices, enabling developmentvelocity. Our survey showed that over 95% ofrespondents were using some level of automationwith almost a third having an entirely automateddeployment pipeline. By comparing the upper andlower quartiles of cloud native production usage(high levels of adoption vs low levels of adoption),we can see that organizations that show high levelsof cloud native adoption are over twice as likely tohave an entirely automated deployment processthan organizations with low cloud native adoption.or automated?1\.7% \- Not 
automated at 
all56%
Partiallyautomated18%Entirelyautomated6% \- Not 
automated at 
allHigh adoption42%EntirelyautomatedLow adoption76%
PartiallyautomatedSnyk Report: State of Cloud Native Application Security \| 03Download Snyks Infrastructure asCode Security Insights report for thetrends on how companies are usingand securing IaC today and commonroadblocks to its wide spread useDownload now Misconfiguration and known unpatched vulnerabilities were responsible for the greatest number of security incidents in cloud native environmentsIn contrast to where organizations are most concerned, we also asked about previous incidents that occured in production. The top two incident types by a distance were misconfiguration and known unpatched vulnerabilities, at 45% and 38% respectively. Over 56% experienced a misconfiguration or known unpatched vulnerability incident involving their cloud native applications.
Data leaks by insiders were more than twice as likely to have occurred in organizations with high levels of cloud native adoption, reinforcing that adopting zero trust principles becomes increasingly important in fully automated cloud based environments.Snyk Report: State of Cloud Native Application Security \| 04
Over half of respondents suffered from a misconfiguration or known vulnerabilities incidentMalwareMisconfigurationKnown unpatched vulnerabilitiesFailed auditSecret leaksData leaks by insiderHavent experienced any security incidents
Prefer not to answer10%14%50%43%45%33%21%14%18%17%18%7%14%21%18%21%High adoptionLow adoption12Incidents
12Nearly 60% have increasedsecurity concerns sinceadopting cloud nativeAdoption of cloud native technologies willundoubtedly change the security postureof your overall application. While the coresecurity principles remain constant, aswith all emerging ecosystems the bestpractice is still being defined, driving freshconcern as teams navigate throughunfamiliar landscapes. Our survey showsorganizations are nearly 4x more likely tohave increased rather than decreasedconcerns over their security posture sinceadopting cloud native.Decreased15%Hasntchanged20%Dontknow7%Increased58%Snyk Report: State of Cloud Native Application Security \| 05Misconfiguration is the area of most concern when moving to cloud native 
Cloud native platforms utilizing automated tooling will rely on credentials such as secrets and API tokens in order to operate, and necessitates a more decentralized approach to managing such access. The need for effective management of these kinds of artifacts is a key differentiator from the more centralized pre\-cloud era, and a major area of concern for operations teams transforming their infrastructure. Our survey showed that misconfigurations were the biggest area of increased concern, with over half of respondents stating its a bigger problem for them since moving to a cloud native platform. Despite secret leaks and data leaks not showing up highly in the actual incidents data, they feature strongly as areas of increased worry particularly among high adopters of cloud native technologies.Snyk Report: State of Cloud Native Application Security \| 06
MalwareKnown unpatched vulnerabilitiesData leaks by insiderSecret leaksInsecure APIsMisconfigurationOwnership to handlefixImpact of security on deployment velocityAbility to respond quickly to risks34%23%45%44%38%17%45%35%50%53%52%57%16%18%22%30%20%29%High adoptionLow adoptionAreas of concern
12Highly automated pipelines are twice as 
likely to be incorporate security testing 
throughout their development lifecycleDeployment automation unlocks scalable security controlsWhile building fully automated deployment pipelines can be challenging, once automation andprocesses are in place, they can create a virtuous cycle providing multiple integration points toenable further automation This is a key enabler for security testing. Companies with high levels ofdeployment automation were more than twice as likely to have adopted security testing at allpoints throughout the software development lifecycle, when compared to organizations with noautomation. While companies of all sizes showed a clear preference to test in CI and earlier,enterprises were more likely to also be testing during later deployment and production stages.Despite testing in local development environments, such as an IDE, being a developer driven task,more automated organizations were nearly twice as likely to see their development teams adoptsecurity early on in their workflows.Snyk Report: State of Cloud Native Application Security \| 07When do you do security testing?Entirely kutomatedNot kutomatedkll44%24%
24%40%43%16%
16%45%74%28%
28%60%38%32%
32%33%26%8%
8%22%Local development eg 
Local development eg 
IDEs and CLI tools
IDEs and CLI toolsSource Code 
Source Code 
repositories
repositoriesCI system
CI systemDeployment time
Deployment timeProduction
ProductionWhen do you do security testing?EnterpriseMediumSmall40%
40%34
3442%
42%39%
39%45%
45%50%
50%65%
64%56%
56%58%
58%36%
36%37%
37%22%
22%26%
25%19%
19%15%
15%Local development eg 
IDEs and CLI toolsSource Code 
repositoriesCI systemDeployment timeProductionSnyk Report: State of Cloud Native Application Security \| 08Continuous deploymentempowers continuous testingOnce the use of security tooling is integrated throughoutthe software development lifecycle, this dramaticallyexpands the possibilities for more regular security testing.Nearly 70% of respondents with high levels of deploymentautomation were able to test their security daily or morefrequently. This was 17x more than respondents who hadno deployment automation, and 60% of those only testedtheir security monthly or less frequently. This was 3x morethan respondents who had full deployment automation.Snyk Report: State of Cloud Native Application Security \| 09How often do you do securitytesting?When do you do security testing?69%
40%4%
24%47%
43%12%
44%36%
16%18%
42%19%
60%28%
60%35%
73%Local development eg 
Continuously or 
daily
IDEs and CLI toolsWeekly
Source Code 
repositoriesCI system
Monthly or less 
frequentlyHow often do you do securitytesting?
When do you do security testing?Entirely AutomatedNot AutomatedAllEnterpriseMediumSmall54%
40%44%
3434%
42%17%
39%12%
45%20%
50%29%
64%44%
56%46%
58%Local development eg 
Continuously or
daily
IDEs and CLI toolsWeekly
Source Code 
repositoriesCI system
Monthly or less 
frequentlySnyk Report: State of Cloud Native Application Security \| 10Snyk Report: State of Cloud Native Application Security \| 01Over 72% of fully automated teams find and fix critical vulnerabilities in under 1 weekSnyk Report: State of Cloud Native Application Security \| 11
Testing faster leads to fixing faster. Over 72% of respondents with high levels of automation had an average time to fix vulnerabilities of less than one week, with 36% having an average of one day or less. Those with full automation were over 4x more likely to fix security issues in a day and over twice as likely to fix within a week. Automated testing is also a key enabler of visibility \- you cant fix what you cant see. This was reinforced by the 28% of organizations with low levels of automation who responded that they didnt know how long it takes them to fix issues.1 day or less1 week2 weeks1 monthLonger than 1 monthDon't know8%36%24%45%20%6%12%10%8%28%3%8%Time fo fix critical sec issues37%Not automatedEntirely AutomatedNot AutomatedAutomation empowers 
shift left securityCompanies who automate are twice as likely to implement security testingAdoptijg a broad ajd deep approach to security practices throughout the software developmejt life cycle is key to asuccessful Cloud Native Applicatioj Security program. Our survey shows that compajies with higher levels of cloudjative automatioj have a greater adoptioj of security testijg techjiques. They tejd to focus more oj Static ApplicatiojSecurity Testijg (SAST), scajjijg for vuljerabilities ij applicatioj depejdejcies with Software Compositioj Ajalysis(SCA), cojtaijer image testijg, ajd scajjijg ijfrastructure as code which are all techjiques which fit well ijto theparadigm of automatioj. Orgajizatiojs with fully automated deploymejt pipelijes are twice as likely to adopt SAST ajdSCA toolijg ijto their SDLC, ajd almost 3x as likely to add Dyjamic Applicatioj Security Testijg (DAST), although ijgejeral, dyjamic testijg isjt as well adopted whej compared with static testijg. Policy compliajce testijg is still ajemergijg field, with ojly 23% of respojdejts havijg adopted it.Enterprises are more likely to adopt security practices, yet smallercompanies with less established security practices are keeping upLarger compajies ajd ejterprises are, of course, more likely to have the resources to ruj dedicated security teamsso it shouldjt come as a surprise to see ejterprises havijg the support to adopt formal Cloud Native ApplicatiojSecurity Practices. While ij smaller orgajizatiojs the security fujctioj may be wholly owjed by ajother org, suchas the ejgijeerijg teams, our survey shows that they are still able to keep up, particularly ij the static testijgspace with over half of small orgajizatiojs adoptijg SAST, SCA ajd cojtaijer image scajjijg.Snyk Report: State of Cloud Native Application Security \| 1270%60%50%40%30%20%10%0%70%60%50%40%30%20%10%0%Watch this on\-demand webinar tolearn tips for implementing securityautomation into modern developmentenvironmentsWatch NowWhich software development life cyclesecurity practices are you following?Entirely AutomatedNot AutomatedAllStatic codeCode scanning forDynamicanalysis(SAST)package dependencyApplicationvulnerabilitiesSecurityInteractiveApplicationSecurityScanningContainerPolicy complianceinfrastructure asimage scanningtools (Open Policycode (Terraform,AgentGatekeeper)(SCA)Testing (DAST)Testing (IAST)Kubernetes)Which Software Development Life Cyclesecurity practices are you following?EnterpriseMediumSmallStatic codeCode scanning forDynamicanalysis(SAST)package dependencyApplicationvulnerabilitiesSecurityInteractiveApplicationSecurityScanningContainerPolicy complianceinfrastructure asimage scanningtools (Open Policycode (Terraform,AgentGatekeeper)(SCA)Testing (DAST)Testing (IAST)Kubernetes)Snyk Report: State of Cloud Native Application Security \| 13Securitj isn't just for the 
securitj teamDevelopers are adding security to their stack of hatsThe move towards the concept of DevSecOps has accelerated in conjunction withadoption of cloud native technologies, as security shifts left in the softwaredevelopment lifecycle. Developers now have a pivotal role in ensuring that cloudnative applications and infrastructure are secure since they increasingly contributeto the application, the infrastructure code, and workload deployment technologies.With this in mind, perception of security ownership provided interesting results inour survey set. While less than 10% of respondents in security roles believeddevelopers were responsible for the security of their cloud native environment andapplications, over 36% of developers stated that they were responsible.Traditionally, in a more siloed organization, the ownership of security would havesat firmly with the security team. Respondents in security roles are almost 3xmore likely to attribute security ownership to the IT security team thanrespondents in development teams are. These indicators suggest that thisownership is being accepted by the development teams faster than the securityteams are willing to let go of it. Security teams are still adjusting to the shiftingresponsibilities which transitioning to cloud native brings, and development teamsare increasingly aware of their growing role in Cloud Native Application Security.Snyk Report: State of Cloud Native Application Security \| 14Who is primarily responsible for the security ofyour cloud native environment and applications?Developer responseSecurity responseApplicationsecurity team14%DevOps
DevSecOps31%DevOps
DevSecOps33%Developers37%No\-one 3%No\-one 2%ITsecurity team13%ITsecurity team31%Applicationsecurity team23%Developers10%Snyk Report: State of Cloud Native Application Security \| 15Developers and security both understand the importance of Cloud NativeApplication SecurityThe increased awareness of security in development teams was also reinforced by the survey results around security exposureconcerns. Both developers and security professionals alike shared that switching to cloud native technologies had increased theirsecurity concerns. Developers were just as likely to be invested in good security outcomes as the security team \- good news for theadoption of DevSecOps principles which relies on shared security goals across the organization.Has switchijg to Cloud Native techjologies ijcreasedor decreased your security exposure cojcerjs?Developer respojseSecurity respojseIjcreased61%Ijcreased58%Decreased13%DecreasedDecreased13%
13%Learn how Twilios Head of ProductSecurity scaled through dev\-firstsecurity and devsecops in a cloudnative environmentWatch NowHasjt chajged18%Hasjt chajged21%Snyk Report: State of Cloud Native Application Security \| 16Snyks CNAS report shows clear movement in a positive direction.99% of respondents recognize that security is important to their business strategy.Thats a world I want to live in
Curious how Snyk can help?
Snyk is a developer\-first platform for building software securely. Learn more about how Snyk can help you secure cloud native applications across your IDEs, repos, containers, and pipelines.Learn more