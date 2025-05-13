# DoD Enterprise DevSecOps Fundamentals
## Table of Contents
- [Introduction](#introduction)
  - [Assumptions](#assumptions)
- [Defining DevSecOps](#defining-devsecops)
  - [Definition](#definition)
  - [DevSecOps Lifecycle](#devsecops-lifecycle)
  - [Key Concepts](#key-concepts)
- [Implementing DevSecOps](#implementing-devsecops)
  - [DevSecOps Implementation Components](#devsecops-implementation-components)
    - [Software Supply Chain](#software-supply-chain)
    - [Software Factory](#software-factory)
    - [DevSecOps Platform](#devsecops-platform)
    - [CI/CD Pipelines](#ci/cd-pipelines)
    - [Infrastructure as Code (IaC)](#infrastructure-as-code-iac)
    - [Common Tools](#common-tools)
  - [DevSecOps Lifecycle Process](#devsecops-lifecycle-process)
    - [Plan](#plan)
    - [Continuous Integration](#continuous-integration)
    - [Continuous Delivery](#continuous-delivery)
    - [Continuous Deployment](#continuous-deployment)
    - [Monitor/Feedback](#monitorfeedback)
  - [Integration with Other DoD Processes](#integration-with-other-dod-processes)
    - [Security](#security)
    - [Test and Evaluation](#test-and-evaluation)
    - [Acquisition](#acquisition)
- [Institutionalizing DevSecOps](#institutionalizing-devsecops)
  - [DevSecOps Culture and Philosophy](#devsecops-culture-and-philosophy)
  - [A Whole-of-DoD Approach](#a-whole-of-dod-approach)
  - [Measuring Success with Performance Metrics](#measuring-success-with-performance-metrics)
    - [DORA and Google Metrics](#dora-and-google-metrics)
    - [Objectives and Key Results (OKRs)](#objectives-and-key-results-okrs)
    - [Flow Metrics](#flow-metrics)
  - [Workforce](#workforce)
  - [DevSecOps Community](#devsecops-community)
- [Getting Started](#getting-started)
- [Acronyms](#acronyms)
- [Glossary of Key Terms](#glossary-of-key-terms)

CLEARED 
For Open Publication 
 
Department of Defense 
OFFICE OF PREPUBLICATION AND SECURITY REVIEW 
 
Oct 23, 2024

This page is intentionally left blank. 
 
Document Approval 
Approved by the DoD Software Modernization Senior Steering Group on October 16, 2024. 
 
Trademark Information 
Names, products, and services referenced within this document may be the trade names, trademarks, 
or service marks of their respective owners. References to commercial vendors and their products or 
services are provided strictly as a convenience to our readers, and do not constitute or imply 
endorsement by the Department of any non-Federal entity, event, product, service, or enterprise. 
 
Foreword 
The Department of Defense (DoD) is embracing innovative software approaches to deliver resilient 
software capability at the speed of relevance. A shift toward Agile and DevSecOps and away from 
traditional waterfall approaches has been underway and is rapidly accelerating. This shift is crucial for 
maintaining our lethal force and building flexibility, security, and resiliency in our software delivery 
practices.  
Agile software methodology is the foundation of modern software development. Software developers 
frustrated with the pace and unpredictability of legacy processes realized there was a better way to 
deliver software faster and more predictably by breaking down silos, developing software incrementally, 
creating feedback loops, and quickly delivering a “minimum viable product” for fast feedback. The Agile 
revolution transformed commercial software development and led to a burst of innovation in automation 
and tools.  
The acceleration of software development led to the discipline of DevOps that focused on the need to 
both develop (Dev) and transition software into operations (Ops). 
DoD’s unique mission compels programs to raise security to an equal footing with development and 
operations. DevSecOps is a combination of software engineering methodologies, practices, and tools 
that unifies software development (Dev), security (Sec), and operations (Ops). It emphasizes 
collaboration across these disciplines, along with automation and continuous monitoring to support the 
delivery of secure, high-quality software. DevSecOps integrates security tools and practices into the 
development pipeline, emphasizes the automation of processes, and fosters a culture of shared 
responsibility for performance, security, and operational integrity throughout the entire software 
lifecycle, from development to deployment and beyond. The concepts build upon the modern 
technology trends of the past two decades:  
- The shift from waterfall software development methodology to Agile  
- The transition from tightly coupled monolithic systems to loosely coupled modular services  
- Integration of security across the lifecycle of technology  
- Incorporation of testing throughout the software lifecycle  
- Evolution from traditional data centers to cloud  
The DoD Enterprise DevSecOps Fundamentals, along with other supporting guidance available at 
https://dodcio.defense.gov/library/, provides education, best practices, and implementation and 
operational guidance for information technology (IT) capability providers, IT capability consumers, 
product teams, and Authorizing Officials (AO). It is intended to build a community that understands the 
realm of the possible and is motivated to pursue the possible to enable a warfighting force strengthened 
by software.  
 
## 1 Introduction 
The Department of Defense is on a multi-year journey to fundamentally transform how software is built, 
used, and managed across all aspects of the DOD enterprise. This includes business systems, 
weapons systems, embedded software, and essential command and control and warfighting support 
systems. This transformation is essential to maintain the technology advantage that underpins US 
military capability. The DoD Enterprise DevSecOps Fundamentals recognizes the importance of 
software. This document is an educational compendium of DevSecOps concepts and is intended to 
promote the adoption of modern software practices across the Department. Additional information is 
captured in corresponding guidance available at https://dodcio.defense.gov/library/.  
Each DoD organization is expected to tailor its culture and align DevSecOps practices to their own 
unique processes, products, security requirements, and operational procedures, while leveraging DoD 
Enterprise resources as a first preference, and making reasonable efforts to ensure developed 
solutions are re-usable across DoD organizations. Embracing DevSecOps requires organizations to 
shift their culture, evolve existing processes, adopt new technologies, and strengthen governance. 
The intended audience of this document includes novice and intermediate staff who have recently 
adopted or anticipate adopting DevSecOps as well as DoD managers and leadership who need to 
understand the software transformation underway and how it will impact their mission. Expert 
practitioners may find value in this material as a refresher. 
The document is organized in the following manner: 
Section 1.0:  
Introduction 
Provides a brief introduction and includes assumptions 
related to the concepts of DevSecOps. 
Section 2.0: 
Defining DevSecOps 
Provides the definition of DevSecOps and a description of 
the DevSecOps lifecycle and phases. 
Section 3.0:  
Implementing DevSecOps 
Provides in-depth information regarding the components of 
DevSecOps to include DevSecOps integration with other 
processes. 
Section 4.0: 
Institutionalizing DevSecOps 
Provides guidance regarding a DevSecOps culture and 
metrics. 
Section 5.0: 
Getting Started 
Provides next steps and identifies additional resources to 
support a DevSecOps journey. 
### 1.1 Assumptions 
The DoD Enterprise DevSecOps Fundamentals makes the following assumptions: 
- Agile/iterative software development practices have been implemented. The concepts in this 
document take those practices to the next step in maturity by implementing DevSecOps. 
- Organizations deploying new business solutions or modernizing existing software systems will 
use an approved or provisionally authorized (PA) cloud environment as their preferred solution. 
 
For weapons systems, the environment will leverage cloud along with on-premises capabilities 
that facilitate hardware-in-the-loop (HWIL) testing for embedded systems. 
- Cybersecurity elements will leverage cloud service provider (CSP) managed service capabilities 
where practicable. Teams will aggressively seek to integrate automated feedback, patching, 
alerting, and other authorized network security measures. 
- Rapidly changing technology dictates designing DevSecOps pipelines and patterns for flexibility 
as new development capabilities enter/exit the commercial product market. 
- DoD Components acknowledge a lock-in posture and recognize that vendor lock-in as well as 
product, version, architecture, platform, skills, legal, and mental lock-in also exist. Avoiding 
vendor lock-in without considering other types of lock-in is ill-advised.  
- DevSecOps may be leveraged for any type of operational requirement needing software 
capabilities. 
 
## 2 Defining DevSecOps 
### 2.1 Definition 
DevSecOps is a combination of software engineering methodologies, practices, and tools that 
unifies software development (Dev), security (Sec), and operations (Ops). 
DevSecOps emphasizes collaboration across these disciplines, along with automation and continuous 
monitoring to support the delivery of secure, high-quality software. DevSecOps integrates security tools 
and practices into the development pipeline, emphasizes the automation of processes, and fosters a 
culture of shared responsibility for performance, security, and operational integrity throughout the entire 
software lifecycle, from development to deployment and beyond. Figure 1 visually depicts the 
DevSecOps lifecycle as an iterative infinity loop divided into ten distinct phases. 
DevSecOps is iterative by design, recognizing that software is never done. The serial-style delivery of 
the waterfall process is replaced with small, frequent deliveries that make it easier to change course as 
necessary. Each small delivery is accomplished through a fully automated process or semi-automated 
process with minimal human intervention to accelerate continuous integration and continuous 
deployment. This lifecycle is adaptable and includes numerous feedback loops that drive continuous 
process improvements. 
 
![Figure 1: DevSecOps Lifecycle Phases (Infinity Loop)](Figure 1: DevSecOps Lifecycle Phases (Infinity Loop))
### 2.2 DevSecOps Lifecycle 
The DevSecOps lifecycle consists of ten phases. The ten phases group common activities and any 
quality gates that occur at that point in the lifecycle and proceed in a cyclical manner with the result of a 
cycle being a software product release. A software product release is an iteration of the product that 
includes new functionality, performance enhancements, and/or security improvements. Each cycle 
 
builds upon the results of previous cycles. The duration of the cycle is determined by the mission owner 
in response to the needs of the stakeholders. Some phase activities may start in one phase and 
continue throughout additional phases of the lifecycle. The ten phases are defined below with specific 
activities for each phase enumerated in the DevSecOps Fundamentals Guidebook: DevSecOps 
Activities & Tools.[^1]
1. Plan – Define the requirements and objectives of the product, with the greatest focus on the 
contents of the next release or version. 
2. Develop – Create the elements of the product based upon the requirements and objectives 
identified in the Plan phase. 
3. Build – Compile and/or integrate the new elements with any existing elements of the 
product. 
4. Test – Verify that the new elements meet requirements and objectives.  
5. Release – Package the product and create required documentation. 
6. Deliver – Make the product available to the operational environment. 
7. Deploy – Install and/or configure the product within the operational environment. 
8. Operate – Use the product in the operational environment. 
9. Monitor – Observe, measure, and monitor the product as it is used. 
10. Feedback – Transmit observed behavior and desired changes for consideration in the next 
iteration of the software product. 

### 2.3 Key Concepts 
There are fundamental concepts associated with adopting DevSecOps. These concepts are described 
in Table 1 and are detailed in the sections that follow. 
Table 1: DevSecOps Key Concepts 
Concept | Description
------- | --------
Software Supply Chain | A software supply chain is a collection of steps that create, transform, and assess the quality and policy conformance of software artifacts. These steps are often carried out by different actors who use and consume artifacts to produce new artifacts. (NIST SP 800-204D) 
Software Factory | In the DoD, a software factory is defined as a collection of people, tools, and processes that enables teams to continuously deliver value by deploying software to meet the needs of a specific community of end users. It leverages automation to replace manual processes. 
DevSecOps Platform | A DevSecOps platform is defined as a group of resources and capabilities that form a base upon which other capabilities or services are built and operated within the same technical framework. Use of a DevSecOps platform is necessary to accelerate development, delivery, and cybersecurity accreditation. 
Continuous Integration / Continuous Deployment (CI/CD) Pipeline | A CI/CD pipeline is the process workflows and associated tools to achieve the continuous integration and continuous delivery of software with maximum use of automation.  
Continuous Authorization to Operate (cATO) | cATO is the state achieved when the organization that develops, secures, and operates a system has demonstrated sufficient maturity in their ability to maintain a resilient cybersecurity posture that traditional risk assessments and authorizations become redundant. This organization must have implemented robust information security continuous monitoring capabilities, active cyber defense, and secure software supply chain requirements to enable continuous delivery of capabilities without adversely impacting the system’s cyber posture. 
 
## 3 Implementing DevSecOps 
### 3.1 DevSecOps Implementation Components 
There are several critical components in implementing DevSecOps. These components include the 
software supply chain, software factories, DevSecOps platforms, CI/CD pipelines, and Infrastructure as 
Code (IaC). The software supply chain provides the full context for software delivery, setting the stage 
for the other components. A software factory encompasses the entire set of software capabilities 
required to deliver resilient software capability at speed. The DevSecOps platform consists of those 
software capabilities that are common across all software factories and provides a standardized and 
secure foundation for software development. CI/CD pipelines include the tools, process workflows, 
scripts, and environments to produce a set of software deployable artifacts with minimal human 
intervention. IaC consists of code baselines that automatically establish common infrastructure or other 
service capability for faster, more consistent implementation. These components are described in the 
following sections. 
Note that a DevSecOps implementation does not require a specific architecture, containers, or even 
explicit use of cloud computing. However, the use of these components is strongly recommended, and 
in some cases mandated by specific DoD reference designs. Teams are encouraged to start small and 
build up their capabilities progressively, striving for continuous process improvement at each of the ten 
lifecycle phases. 

#### 3.1.1 Software Supply Chain 
The software supply chain is a logistical pathway that covers the entirety of all the hardware, 
Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS), and 
tools and practices that are brought together to deliver specific software capabilities. The software 
supply chain matters because the end software supporting the warfighter, from embedded software on 
the bridge of a Naval vessel to electronic warfare algorithms in an aircraft, is only possible due to the 
people, processes, and tools that create the end result. For example, a compiler is unlikely to be 
deployed onto a physical vessel, but without the compiler there would be no guidance system. For this 
reason, the software supply chain must be recognized, understood, secured, and monitored to ensure 
mission success.  
Software supply chains exist for business systems, weapons systems, and everywhere software is 
developed and deployed. It is easy, but naïve and incorrect, to dismiss an embedded system in a 
projectile as “isolated” and disconnected. The projectile includes embedded software that was compiled 
leveraging 3rd party libraries and links to hardware drivers and relies upon features of embedded 
firmware. Additionally, the very performance of the software was likely tested using modeling and 
simulation software executing within a high-performance computing cloud.  
DevSecOps methodologies span multiple links of the software supply chain. DevSecOps cannot exist 
without this logistical supply chain – Integrated Development Environments (IDEs), build tools, code 
repositories, artifact repositories, testing software suites, and many other pieces of software must work 
together in unison to effectively execute a DevSecOps powered software factory. The totality of these 
environments must be considered when evaluating the software supply chain. For example, the 
cybersecurity and risk postures of a specific artifact or application would be calculated using the 
product rule across the entirety of the software supply chain. If the compiler is 90% secure, the code 
repository is 90% secure, the artifact repository is 90% secure, and the container orchestrator is 90% 
secure – the overall system is not 90% secure. The cybersecurity level of the end-to-end ecosystem is 
actually .9 * .9 *.9 * .9, or roughly 65% secure.  
DevSecOps aims to harness the collective expertise and knowledge across the entire software supply 
chain to mitigate risk at each step. Only then can the overall cyber survivability of the ecosystem 
significantly increase. To further illustrate this point, if a DevSecOps team only increases security 5%, 
raising each level from 90% to 95%, then overall cyber survivability security jumps from 65% to 81%. 

#### 3.1.2 Software Factory 
A software factory is a collection of people, tools, and processes that enables teams to continuously 
deliver value by deploying software to meet the needs of a specific community of end users. It 
leverages automation to replace manual processes. Software factories are strongly linked to one or 
more specific software supply chains but the software factory itself is not an entire software supply 
chain. 
A software factory provides a structured and repeatable approach to software development, enabling 
organizations to streamline their processes, improve efficiency, and ensure consistent quality across 
products. It consists of the full set of software capabilities depicted in Figure 2, which organizes the 
software capabilities under Infrastructure, Digital Platform, and Applications. 
 
![Figure 2: Software Capabilities of a Software Factory](Figure 2: Software Capabilities of a Software Factory)
Infrastructure Capabilities supply the hosting environment for the software factory, explicitly providing 
compute, storage, network resources, and additional CSP managed services to enable function, 
cybersecurity, and non-functional capabilities. Typically, this is either an approved or DoD provisionally 
authorized environment provided by a CSP but is not limited to a CSP. 
Digital Platform Capabilities include the distinct development environments of the software factory, its 
CI/CD pipelines, a clearly implemented log aggregation and analysis strategy, and continuous 
monitoring operations. These capabilities should support multi-tenancy, enforce separation of duties for 
privileged users, and be considered part of the cyber survivability supply chain of the final software 
artifacts produced.  
The set of environments within this capability set rely upon CI/CD pipelines, each equipped with a 
purpose-driven set of tools and process workflows. The environmental boundaries are heavily 
automated with strict gates controlling promotion of software artifacts from development to test, and 
from test to integration. These capabilities also encompass planning and backlog functionality, 
configuration management (CM) repositories, and local and released artifact repositories. Access 
control for privileged users is expected to follow an environment-wide least privilege access model. 
Continuous monitoring assesses the state of compliance for all resources and services evaluated 
against NIST SP 800-53 controls.  Reference NIST Special Publication 800-137, Information Security 
Continuous Monitoring (ISCM) for Federal Information Systems and Organizations and (CUI) DoD 
Information Security Continuous Monitoring Strategy for more information.  
Application Capabilities include application frameworks, data stores such as relational or NoSQL 
databases and object stores, and other middleware unique to the application and outside the realm of 
the CI/CD pipeline. 
Software factories may contain multiple assembly lines, or in software parlance, CI/CD pipelines. Each 
pipeline contains and defines a complete set of tools, process workflows, scripts, and environments that 
co-exist to produce a set of production quality software artifacts with minimal human intervention. 
Figure 3 illustrates a generic software factory with multiple pipelines where the production environment 
is integrated within its defined security boundaries (e.g., software developed and delivered to a 
production environment within the boundaries of their DevSecOps platform). Figure 4 illustrates a 
second software factory use case where the production environment is external to the software factory 
security boundaries as defined in their Authorization to Operate (ATO) (e.g., software developed and 
delivered to a weapons system or afloat asset). 
 
![Figure 3: Generic Software Factory with Integrated Production Environment](Figure 3: Generic Software Factory with Integrated Production Environment)
 
![Figure 4: Generic Software Factory with a Separate Production Environment](Figure 4: Generic Software Factory with a Separate Production Environment)
In an ideal or very mature software factory, Free and Open Source Software  (FOSS), Commercial off 
the Shelf (COTS), Government off the Shelf (GOTS), and/or newly developed code and supporting 
scripts and configuration files are committed into the factory’s local artifact or code repository, 
respectively.  Assembly line-like automation moves software changes from one phase to the next. 
When starting, a best practice is to migrate into a software factory while sustaining legacy capability.  
The development environment contains the rawest form of source code. When a developer looks to 
merge their completed work into the main branch of the code repository, they encounter a control 
gate. As an example of this, if code is successfully compiled, it will forward with a pull/merge request 
for peer review, which includes a critical security step that is the software code equivalent of two-person 
integrity. If the peer review identifies security flaws, architectural concerns, a lack of appropriate 
documentation within the code itself, or other problems, the merge request can be rejected, and the 
code sent back to the software developer for rework. Once the merge request is approved and any 
other activities such as unit tests are completed, the continuous integration step is triggered. 
Continuous integration (CI) executes automated tests such as unit tests and Static Application Security 
Test (SAST), verifying the integrity of the work in the broader context of the artifact or application. The 
CI assembly line is solely responsible at this point for guiding the pipeline, including but not limited to 
dependency tracking, regression tests, code standards compliance, and pulling dependencies from the 
local artifact repository, as necessary. When the CI completes, the artifact is automatically promoted to 
the test environment. 
Usually, the test environment is where a more in-depth set of tests is executed. For example, hardware-
in-the-loop (HWIL) tests or software-in-the-loop (SWIL) tests may occur at this point. In addition, the 
test environment pipeline performs additional or more in-depth testing variants of static code analysis, 
functional tests, interface tests, and dynamic code analysis. If these tests complete without error, then 
the artifact is poised to pass through another control gate into the integration environment or be sent 
back to the development team to fix any issues discovered during the automated testing. 
Once the code and artifact(s) reach the integration environment, the continuous deployment (CD) 
assembly line is triggered. More tests and security scans are performed in this environment, including 
operational and performance tests, user acceptance tests, and additional security compliance scans. 
Once all tests complete without issue, the CD assembly line releases and delivers the final product 
package to the released artifact repository. 
Released is never equivalent to Deployed! This is a source of confusion for many. A released artifact 
is available for deployment. Deployment may or may not occur instantly. A laptop that is powered off 
when a security patch is pushed into production will not immediately receive the artifact. Larger updates 
or out-of-cycle refreshes like anti-virus definition refreshes often require the user to initiate. The 
deployment occurs later. While this is a trivialized example, it effectively illustrates that released is 
never equivalent to deployed. 
The CD acronym is often ambiguously used to mean either Continuous Delivery or 
Continuous Deployment, covered next. These are related but different concepts. This 
document will use CD to mean continuous deployment. In this document, Continuous 
Delivery is a software development practice that allows frequent releases of value to 
staging or various test environments once verified by automated testing. Continuous 
Deployment relies on a manual decision to deploy to production, though the deployment 
process itself should be automated. 
DoD needs multiple software factories tuned for specific types of software systems, such as web 
applications or embedded systems that may include significant amounts of HWIL for automated testing. 
It also requires software factories operating at varying classification levels in both cloud and on-
premises or disconnected environments. 
Under the shift to a cATO, each software factory will have its processes, teams, and storage reviewed, 
certified, and continuously monitored to allow them to deploy applications into a continuously monitored 
system. This shift greatly lessens the initial burden of achieving an ATO for each piece of software, as 
the process and roll out are certified and fed into a continuous monitoring architecture.  
An ideal DevSecOps software factory does the following: 
1. Standardization: Establishes standardized practices, processes, and tools for software 
development. It promotes consistency and reduces variability, allowing product teams to work 
more efficiently and effectively.  
2. Automation: Automates various activities of the software development lifecycle, including code 
compilation, testing, and deployment. This automation reduces manual effort, minimizes errors, 
and accelerates the delivery of software updates. 
3. CI/CD: Provides continuous integration and deployment, allowing developers to frequently 
integrate their code changes and deliver software updates in an automated and reliable manner. 
It moves Developmental and Operational Test and Evaluation activities earlier in the CI/CD 
pipelines instead of bolted on at the end, facilitating more rapid feedback to the development 
teams. This promotes agility, collaboration, and faster time-to-market.  
4. Scalability and Flexibility: Scales and adapts to the needs of the organization. It must be 
designed for multi-tenancy and accommodate different types of applications, technologies, and 
deployment environments, including on-premises, cloud, and hybrid infrastructures. 
5. Security and Compliance: Incorporates security practices throughout the development and 
delivery process. It provides a dynamically scalable set of pipelines with three distinct cyber 
survivability control gates and integrates security scanning tools, vulnerability assessments, and 
compliance checks to identify and address security issues early on. This helps ensure that 
software products meet security standards and regulatory requirements and provides assurance 
as an AO that functional, security, integration, operational, and all other tests are reliably 
performed and passed prior to formal release and delivery. 
6. Collaboration and Communication: Fosters collaboration and communication among teams, 
enabling them to work together seamlessly. It provides shared repositories, issue tracking 
systems, and collaboration tools to facilitate teamwork and information sharing. 
7. Continuous Improvement: Promotes a culture of continuous improvement by collecting 
metrics, analyzing performance, and identifying areas for enhancement. It enables teams to 
learn from past experiences, iterate on processes, and drive ongoing optimization. 
Every DoD organization is encouraged to seek out an existing managed PaaS to learn about and 
begin applying DevSecOps.  
DoD DevSecOps Platform and Software Factory Inventory (CAC-enabled) 
https://go.intelink.gov/ab7U5ad   

#### 3.1.3 DevSecOps Platform 
A DevSecOps platform is defined as a group of resources and capabilities that form a base upon which 
other capabilities or services are built and operated within the same technical framework. It provides a 
comprehensive set of common tools, services, and infrastructure to support the implementation and 
execution of DevSecOps practices within an organization and serves as a centralized hub for managing 
and automating various phases of the software development lifecycle, with a strong focus on security. It 
can be a multi-tenant environment that brings together a significant portion of a software supply chain, 
operating under cATO or a provisional ATO. Each DevSecOps platform may be composed of multiple 
software factories, multiple environments, multiple tools, and numerous cyber resiliency tools and 
techniques.  
Figure 5 illustrates a DevSecOps platform in support of a software factory. It identifies reference design 
interconnects which represent a unique set of tools and activities that exist within and/or at the 
boundaries between the digital platform capabilities. These unique toolsets or configurations to include 
proprietary tooling or specific architectural constructs connect various aspects of the DevSecOps 
platform together. Well-defined reference design interconnects as provided in DoD approved 
DevSecOps reference designs enable tailoring of the software factory design, while ensuring that core 
capabilities of the software factory remain intact. 
 
![Figure 5: DevSecOps Platform](Figure 5: DevSecOps Platform)
 
DevSecOps platforms provide rapid access to common software development infrastructure capabilities 
for use by a DevSecOps team. DevSecOps platforms employ automation at multiple levels and across 
multiple activities in the develop, build, test, release, and deliver phases of the DevSecOps lifecycle. 
Each environment in the process is automated to the maximum extent that is safely and securely 
possible, rehydrated using Infrastructure as Code (IaC) and Configuration as Code (CaC) that run 
on various tools. DevSecOps platforms are expected to be instantiated from hardened IaC code and 
scripts or DoD hardened containers from a DoD artifact repository like Iron Bank, a hardened container 
image repository and one of Platform One’s value streams. 
Platforms are necessary to implement software delivery through DevSecOps.  DevSecOps platforms 
represent a prime opportunity for the DoD software community to leverage reuse in the underlying 
infrastructure. DoD organizations are encouraged to leverage government-managed and curated 
platforms, such as Platform One’s tailorable Big Bang platform, and contribute modifications back to the 
baseline to provide the DoD-enterprise with a growing set of pre-configured integrations. 

#### 3.1.4 CI/CD Pipelines 
A critical part of a software factory are the Continuous Integration/Continuous Delivery (CI/CD) 
pipelines. The adoption of CI/CD pipelines reduce risk through the practice of making many small, 
incremental changes to software instead of one gigantic change. The incremental changes can be 
reviewed quickly. Mistakes that are introduced are easier to capture and isolate when only a few things 
have changed. 
As described previously, a software factory may contain multiple CI/CD pipelines which are equipped 
with a set of tools, process workflows, scripts, and environments, to produce a set of software 
deployable artifacts with minimal human intervention. It automates the activities in the develop, build, 
test, release, and deliver phases. Different pipelines are needed for different types of software such as 
web applications, business systems, command and control systems, embedded systems, or AI/ML.  
It is within each CI/CD pipeline that the software supply chain is actualized. Per NIST SP 800-204D, 
“Strategies for the Integration of Software Supply Chain Security in DevSecOps CI/CD Pipelines,” a 
software supply chain must not be reduced to merely a set of artifacts. Every software supply chain 
must explicitly address every link that exists between writing source code through production 
deployment: 
> While software composition (e.g., dependency management) is under the purview of software supply 
chain activities, other often overlooked activities are central to the software supply chain. This includes 
writing source code; building, packaging, and delivering an application; and repackaging and 
containerization.
Activities in the CI/CD pipeline empower stronger communication between developers and information 
security personnel. The creation of shared context by and between development teams and information 
security teams enables security controls to be discussed and expectations established for each 
individual link across the totality of the CI/CD pipeline. Figure 6 illustrates a generic CI/CD pipeline. 
 
![Figure 6: Example CI/CD Pipeline](Figure 6: Example CI/CD Pipeline)
As an actor initiates a series of steps within a CI/CD pipeline, resources and input artifacts are 
consumed, and one or more final artifacts result. It is crucial to monitor each step, or link, in the 
software supply chain across every segment of the CI/CD pipeline. This monitoring involves collecting 
and analyzing comprehensive metadata at each stage, providing visibility into the entire process. 
Effective observability allows teams to track the flow of data, identify potential bottlenecks, and ensure 
that each step is executed correctly and securely. 
Observability goes beyond simple monitoring; it enables teams to gain deep insights into the 
performance, security, and reliability of the pipeline. By aggregating logs, metrics, and traces from each 
step, teams can quickly diagnose issues, ensure compliance with security policies, and optimize the 
pipeline for efficiency. This level of observability is especially important in environments that have 
received a cATO, where continuous monitoring capabilities are in place to maintain the security and 
integrity of the system. 

#### 3.1.5 Infrastructure as Code (IaC) 
The shift to immutable infrastructure using IaC provides security and value in a number of ways. First, it 
removes lethargic and error-prone step-by-step deployment and configuration guides performed 
manually. In a legacy, manual driven approach, it is too easy to inadvertently skip a step or mistype a 
configuration command. Second, it confirms that the command will execute as expected, mitigating the 
risk of a change without any type of peer review before execution. Third, by providing a standard 
deployment model, a standard set of outputs can be auto-ingested into Defensive Cyber Operations 
(DCO) platforms and data collection/visualization mediums. This allows DCO to begin instantaneously 
and provides data analytics to identify necessary next innovations. 
IaC plays a critical role in automation for DevSecOps platforms.  For Platform teams, IaC streamlines 
infrastructure deployment, authorization, and security for customers leveraging cloud, shortening the 
time to stand up the typical infrastructure by months. IaC consists of baselines that automatically 
establish cloud environments in hours. It accelerates the authorization process with inheritable common 
controls and the use of PaaS services, which reduces the need for Security Technical Implementation 
Guides (STIGs), Assured Compliance Assessment Solution (ACAS), and Host-Based Security System 
(HBSS). If implemented correctly, it can shorten the deployment of networking, identity, and security 
policies for security compliance from the standard 30 weeks to hours. 
DoD provides approved IaC templates for use across DoD Components at 
https://www.hacc.mil/Portfolio/DOD-Cloud-IaC/. DoD IaCs leverage automation to generate 
preconfigured, preauthorized PaaS focused environments. These baselines exist in the form of IaC 
templates that organizations can deploy to establish their own decentralized cloud platform. Baselines 
significantly reduce mission owner security responsibilities by leveraging security control inheritance 
from CSP PaaS managed services, where host and middleware security is the responsibility of the CSP 
including hardening and patching. Each baseline documents its associated inheritable controls to 
expedite the Assessment and Authorization (A&A) process. DoD IaC baselines can be built into 
DevSecOps pipelines to rapidly deploy the entire environment and mission applications. 

#### 3.1.6 Common Tools 
Every DevSecOps software factory and platform must include a minimal set of common tooling. The 
use of the word common is indicative of a class of tooling; it does not, nor should it be construed that 
the same tool must be used across every implementation.  
The DevSecOps Fundamentals Guidebook: DevSecOps Activities & Tools provides a clean set of 
tables that captures both required and preferred tooling across DevSecOps lifecycle phase activities. 
DoD approved reference designs augment the DevSecOps Fundamentals Guidebook: DevSecOps 
Activities & Tools, adding in its environmentally specific required and preferred tooling. Reference 
designs do not remove a required tool or activity, only augment. The DevSecOps Fundamentals 
Guidebook: DevSecOps Activities & Tools and DoD approved reference designs are available at 
https://dodcio.defense.gov/Library/. 

### 3.2 DevSecOps Lifecycle Process 
Figure 7 visually depicts the DevSecOps phases, feedback loops, and control gates. The lifecycle is 
built around a series of iterations, with each iteration covering the Plan, Develop, Build, Test, Release, 
