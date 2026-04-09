# State of the Software Supply Chain 2021

## Table of Contents
- [Introduction](#introduction)
- [Chapter 1: Open Source Supply, Demand, and Security](#chapter-1-open-source-supply-demand-and-security)
- [Chapter 2: Understanding Exemplary and Non-Exemplary Open Source Projects](#chapter-2-understanding-exemplary-and-non-exemplary-open-source-projects)
- [Chapter 3: Peer Practices Associated With Micro and Macro Dependency Management](#chapter-3-peer-practices-associated-with-micro-and-macro-dependency-management)
- [Chapter 4: Software Supply Chain Maturity](#chapter-4-software-supply-chain-maturity)
- [Chapter 5: Emergence of Software Supply Chain Regulation and Standards](#chapter-5-emergence-of-software-supply-chain-regulation-and-standards)
- [About the Analysis](#about-the-analysis)
- [Acknowledgments](#acknowledgments)

---

## Introduction

In 1849, French writer Jean-Baptiste Alphonse Karr famously said, “the more things change, the more they stay the same.” While he obviously wasn’t talking about open source software (OSS), digital supply chains, or application innovation during a global pandemic, he might as well have been. Indeed, in the year since we last published our State of the Software Supply Chain research, so much has changed in the world of software development, and yet, so much has stayed the same.

My oh my, how things have changed. COVID-19 fundamentally transformed how people live and work, how companies interact with customers, how customers shop and buy, and how physical and digital supply chains function. As the economic importance of digital innovation accelerated during the global pandemic, so too did the number of cyber-attacks aimed at exploiting software supply chains.

And yet, much has stayed the same. Top-performing companies like Apple, Goldman Sachs, and Amazon — and more recently, Zoom, Peloton, and Wayfair have mastered three key competitive advantages: knowing how to use open source and third-party innovation at scale, integrating security and risk controls into multiple phases of the software supply chain, and releasing higher quality code faster than their competitors.

Now in its seventh year, Sonatype’s 2021 State of the Software Supply Chain Report blends a broad set of public and proprietary data to reveal important findings.

Together with our partners, we are proud to share this research. We hope that you find it valuable.

---

## Chapter 1: Open Source Supply, Demand, and Security

The universal desire for faster innovation fundamentally requires that software developers reuse code frequently and efficiently. This, in turn, has led to a critical dependence on OSS libraries borrowed from third-party ecosystems. These third-party components and packages represent the building blocks of modern software development. But, what does open source supply look like? What are the demand dynamics? What is the relative quality and security of third-party code borrowed from open source suppliers?

![Figure 1.1: 2021 Software Supply Chain Statistics]

### Open Source Supply
The global supply of open source libraries continues to grow exponentially, fueled by new versions of existing projects constantly being released, and by the creation of altogether new projects. Currently, the top four open source ecosystems contain a combined 37,451,682 components and packages. These same communities released a combined 6,302,733 new versions of components / packages over the past year and have introduced 723,570 brand new projects in support of 27 million developers worldwide.

### Software Supply Chain Attacks Increase 650%
Members of the world’s open source community are facing a novel and rapidly expanding threat that has nothing to do with passive adversaries exploiting known vulnerabilities in the wild — and everything to do with aggressive attackers implanting malware directly into open source projects to infiltrate the commercial supply chain.

From February 2015 to June 2019, 216 software supply chain attacks were recorded. Then, from July 2019 to May 2020, the number of attacks increased to 929 attacks. However, in the past year, such attacks represented a 650% YoY increase.

---

## Chapter 2: Understanding Exemplary and Non-Exemplary Open Source Projects

Given its prominence in modern software development, the quality of open source libraries used from third-party suppliers has a fundamental impact on digital innovation. But how should engineering leaders go about choosing the best open source projects? Which ones are optimal? Which ones are suboptimal? Further, how should engineering teams think about project hygiene, not only as it pertains to direct dependencies, but also transitive?

### Open Source Project Quality Metrics
**Sonatype Mean Time to Update (MTTU)**
MTTU is the average time required for a project to respond to new versions of its dependencies. MTTU provides visibility into an open source projects’ dependency management practices — Lower is better.

---

## Chapter 3: Peer Practices Associated With Micro and Macro Dependency Management

In today’s world, a wide variety of bits are flowing rapidly through our software supply chains. Because of this, an equally wide variety of decisions must be made by engineering team members across every phase of the DevSecOps value stream. What you will see in the following research is that software developers make suboptimal choices 69% of the time with respect to updating third-party dependencies.

### To Update or Not: An Empirical View of Micro Dependency Management
There are three reasons why dependency management is rapidly becoming an increasingly important practice for software engineering teams:
1. The enormous volume of open source dependencies present in production applications.
2. The incredible velocity at which new versions of dependencies are being released.
3. The fact that open source dependencies age like milk, and not like wine.

---

## Chapter 4: Software Supply Chain Maturity

*(Content regarding maturity levels and industry benchmarks)*

---

## Chapter 5: Emergence of Software Supply Chain Regulation and Standards

*(Content regarding global regulatory trends in the US, UK, Germany, and EU)*

---

## About the Analysis
100,000 anonymized, validated applications scanned by publicly available and commercial vulnerability analysis tools.

---

## Acknowledgments
*(List of contributors and partners)*

[^1]: 100,000 anonymized, validated applications scanned by publicly available and commercial vulnerability analysis tools.

---

ependencies are automatically recom-
mended for updating, but only when optimal. This

28

2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTCHAPTER 3: PEER PRACTICES ASSOCIATED WITH MICRO AND MACRO DEPENDENCY MANAGEMENTengineering leaders should embrace intelligent
automation. Chosen tools should remove the
current error-prone micro decision making
from day-to-day developer workflows.

 ⊲ Engineering leaders should also embrace
tools to guide macro decisions made by
architects and developers with respect
to initial technology selection.

type of intelligent automation keeps software fresh
without inadvertently introducing wasted effort or
increased security risk. This approach is proactive,
scalable, and optimal in terms of cost efficiency
and quality outcomes.

non-vulnerable dependencies. This aids with
micro dependency decisions and helps with
never getting stuck with “no path forward” traps.

3.  Reduce technology bloat associated with

non-standard decision making.

Selecting the Best Projects:
Reflections on Macro
Architectural Decisions
When developing applications in the context of
a modern software supply chain, it is critical that
engineering leaders define clear policies. These
help their developers make sound architectural
decisions as to which open source projects are
acceptable (optimal exemplars), and which ones
are unacceptable (suboptimal non-exemplars).

If developers made dependency update decisions
based on a structured system of guidance, we
would expect to see a correlation between optimal
update decisions and exemplary projects, as well
as suboptimal update decisions and non-exemplary
projects. The fact that these correlations DO NOT
EXIST, reveals a clear opportunity for engineering
leaders to benefit by standardizing open source
architectural guidance at scale.

Establishing and enforcing intelligent architectural
policy is important for several reasons:

Conclusions and Practical
Recommendations

1.  Save time and money by standardizing which
projects are best for you, and eliminating
inconsistent diligence efforts associated with
component selection.

2. Improve application security and quality by

 ⊲ Based on the research, it’s clear that material

inefficiencies exist along with significant
avoidable risk. Software engineering teams
have considerable room for improvement with
respect to dependency management practices.

standardizing on projects that are most likely
to provide reliable access to new versions of

 ⊲ To improve efficiencies, save money, and

optimize dependency management at scale,

29

2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTCHAPTER 3: PEER PRACTICES ASSOCIATED WITH MICRO AND MACRO DEPENDENCY MANAGEMENT Software Supply Chain Maturity

CHAPTER 4

For this year’s report, we surveyed 702 engi-
neering professionals about their software
supply chain management practices, including
approaches and philosophies to utilizing open
source components, organizational design,
governance, approval processes, and tooling. The
survey also inquired about engineering outcomes
including deployment frequency, security, engi-
neering productivity, and job satisfaction. The
responses came from IT professionals represent-
ing a variety of roles and industries.

The survey itself consisted of 41 questions:

 ⊲ Ten questions were focused on understanding

the relative quality of software outcomes
(dependent variables).

 ⊲ 24 questions were focused on understanding

patterns and practices embraced by engineering
teams (independent variables).

 ⊲ Seven questions were focused on understanding

job satisfaction.

The objective of the survey was twofold:

1.  Determine if certain software supply

chain practices correlate to successful
engineering outcomes.

2. Develop a benchmark and maturity model

so organizations can evaluate themselves in
comparison to their peers.

Responses to all 41 questions were assessed
against the following eight elements of software
supply chain management practices:

1.  Application inventory (Inventory) – Do you know

all the applications your organization has in
development/production, and who the stake-
holders/owners are? Do you know the details
about them, including how they are built, and

the Software Bill of Materials (SBOM) for the OSS
components they include?

2. Supplier hygiene (Suppliers) – Do you know

if your OSS components come from a trusted,
quality supplier?

3.  Build & release – Do you understand how your

software "parts" and processes come together to
build and release applications into production?

4.  Project consumption (Consumption) – Do you

govern OSS component selection?

5. Giving back (Contribution) – Do you contribute

to the OSS community?

6. Policy control (Risk Management) – What is

your tolerance for risk? Do you have automated
policy enforcement?

7.  Digital transformation (Execution Plan) – What
plans, resources, and training do you have to
help institutionalize new processes and tools?

FIGURE 4.1
FIVE STAGES OF SOFTWARE SUPPLY CHAIN MANAGEMENT MATURITY

Less Mature

 More Mature

UNMANAGED

EXPLORATION

AD HOC

CONTROL

MONITOR & MEASURE

This first stage is referred to as the
Unmanaged stage because organi-
zations are often operating with an
"anything goes" mindset, are often
reactive, and have minimal process/
oversight related to the themes.

A realization of some sort is usually the
impetus for thrusting an organization
into the Exploration stage. This is often
triggered by an "event" that causes an
"all hands on deck" reaction to uncover
necessary information/solutions, or
a champion of some sort leading an
improvement effort. This stage is often
focused on identifying the perceived
problem/inefficiency, learning about
current implementations, and starting
to explore potential solutions.

In the midst of starting to define
processes and implement tooling
to improve the identified problem,
Ad Hoc solutions reign as the teams
work toward institutionalization
and socialization of new tooling
and processes.

In the Control stage, ad hoc solutions
give way to more formalized
governance processes across
the enterprise. Socialization and insti-
tutionalization of these processes
and tools is ongoing, but for the most
part, stakeholders are bought in to
the need for improvement measures
and are working towards compliance.

The Monitor and Measure stage
occurs once new processes and
tools have been institutionalized,
and organizations have reached a
phase of being able to proactively
address OSS component risk. In
addition, a healthy amount of ROI
is realized, and measurements to
demonstrate success are available.

31

CHAPTER 4: SOFTWARE SUPPLY CHAIN MATURITY2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTFIGURE 4.2
SOFTWARE SUPPLY CHAIN
MATURITY SCORE BY THEME
 5th, 50th, and 95th Percentile

8. Remediation – How do you implement fixes to

address identified OSS component risk?

Aggregate responses were then scored and
mapped into five different stages of software supply
chain management maturity, as defined
in Figure 4.1.

How Mature are Today’s
Software Supply Chains?
Based on the survey results, it’s a bit of a mixed
bag. Let us explain.

In Figure 4.2, we’ve plotted the 702 responses
against the five different stages of maturity. We
see that, across the various themes, the majority of
respondents were graded less than the “Control”
level of maturity. Further, based on the definitions
above, we can assert that the “Control” level of
maturity is the point at which an organization
transitions from “figuring it out” to a minimal level of
maturity that will enable high-quality outcomes. The
three levels of maturity (Unmanaged, Exploration,
Ad Hoc) prior to the “Control” level of maturity are
suboptimal; this is where most of survey responses
were scored.

Reality vs. Perception on Software
Supply Chain Maturity
The majority of respondents demonstrate an “Ad
Hoc” approach to software supply chain manage-
ment for all themes except two: Remediation and
Inventory. Respondents indicate they are remediat-
ing risky components and they understand where
the risk resides. This is true even though they have
an “Ad Hoc” approach to Build & Release and Risk
Management processes.

The survey suggests that
respondents have talked
themselves into believing
that they’re doing a good
job, leading at the least to
a false sense of security
and at worst to huge
inefficiencies in the
engineering process.

We also compared the objective analysis done in
chapters 2 and 3, which analyzed 100,000 applica-
tions, to the subjective survey responses. The data
shows a clear disconnect between what is actually
happening, and what people think is happening:
70% of remediations are suboptimal, which aligns
with the “Ad Hoc” maturity rating for both Risk
Management and Execution practices.

In summary, the survey suggests that respondents
have talked themselves into believing that they’re
doing a good job, leading at the least to a false
sense of security and at worst to huge inefficiencies
in the engineering process. Objectively, however, the
data from Chapters 2 and 3 indicates that develop-
ment teams are not following structured guidance,
and do not have intelligent tooling to ensure quality
outcomes. Reconciling this perception with reality
will help organizations in achieving the promised
efficiency gains in dependency management.

32

CHAPTER 4: SOFTWARE SUPPLY CHAIN MATURITY2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTCHAPTER 5

Emergence of Software Supply
Chain Regulation and Standards

What’s Happening in
the United States?
Following the multitude of attacks in 2020 aimed at
software supply chains, the United States Federal
Government took notice and began to take action.

February
Starting in February 2021 — President Biden
issued an Executive Order (EO) laying out changes
to secure all supply chains, including software. The
order called upon the Secretaries of Commerce
and Homeland Security to coordinate with heads of
appropriate agencies to report on the security and
integrity of critical information and communications
technology software supply chains.

Also in February, the CIO for the Department of
Defense (DoD CIO) rolled out a new reference
architecture called Department of Defense (DOD),
Zero Trust Reference Architecture (ZTA). Within the
ZTA the DoD CIO outlined various Zero Trust Pillars
and Capabilities including a section centered on
protecting applications and software supply chains.

The Executive Order
“on Improving the
Nation’s Cybersecurity”
is a milestone for the
U.S. government.

and enforcement points. Developed Source
Code and common libraries are vetted
through DevSecOps development practices
to secure applications from inception.

The document further defines software supply
chain protection as:

The reference architecture specifically calls for
protection of Applications and Workloads, defined as:

The ability to validate the security on a
binary, library, or source code used to build
an application.

Applications and workloads include tasks
on systems or services on-premises, as
well as applications or services running in
a cloud environment. Zero Trust workloads
span the complete application stack from
application layer to hypervisor. Securing
and properly managing the application
layer, as well as compute containers and
virtual machines is central to Zero Trust
adoption. Application delivery methods such
as proxy technologies, enable additional
protections to include Zero Trust decision

April
In April 2021, the United States saw the formaliza-
tion of software supply chain standards begin to
take shape when the CISA and National Institute
of Standards and Technology (NIST) released
their paper “Defending Against Software Supply
Chain Attacks”

In it, the two agencies highlighted that software
compromised in supply chain attacks could have
“widespread consequences for government,
critical infrastructure, and private sector software

customers.” They also noted how these types of
attacks can easily allow bad actors to get around
other cyber defenses to carry out cyber espionage.

The document provides in-depth guidance for
both governments and companies to implement
reasonable safeguards to secure their software
supply chains.

Suggestions include:

 ⊲ Developing a written program to address

software supply chain risk.

 ⊲ Inventorying organizational reliance on
external software and code across all
operational departments.

 ⊲ Assessing risk from these vendors and adopting
appropriate contractual and other safeguards.

 ⊲ Coordinating efforts across management, IT,
personnel, compliance, product development
and operational departments.

 ⊲ Monitoring the threats and vulnerabilities to the
software supply chain, including through techni-
cal measures and threat analysis, on an ongoing
basis.

May
In May 2021, Biden signed a second Executive
Order for software supply chains, this time, as part of
a critical look at the nation’s cybersecurity posture.
The EO “on Improving the Nation’s Cybersecurity” is
a milestone for the U.S. government.

The EO prescribed a number of technologies,
including multi-factor encryption and endpoint
detection as critical to protecting the nation's cyber
assets. Further, the EO established a detailed plan
for taking steps to secure the federal software

34

2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTCHAPTER 5: EMERGENCE OF SOFTWARE SUPPLY CHAIN REGULATION AND STANDARDSsupply chain. The order called for NIST to publish
guidelines for establishing best practices to detect
vulnerabilities, and requirements that all critical
software delivered to government customers
including an SBOM. It also included milestones
that agencies must meet to demonstrate progress
toward the goals.

June
In June 2021, as directed by the EO, NIST released
their definition of “critical software” defining it as:

[...] any software that has, or has direct
software dependencies upon, one or more
components with at least one of these
attributes:
 ⊲ is designed to run with elevated privilege or

manage privileges;

 ⊲ has direct or privileged access to networking

or computing resources;

 ⊲ is designed to control access to data or

operational technology;

 ⊲ performs a function critical to trust; or,
 ⊲ operates outside of normal trust boundaries

with privileged access.

The definition applies to software of all forms (e.g.,
standalone software, software integral to specific
devices or hardware components, cloud-based
software) purchased for, or deployed in, production
systems and used for operational purposes.

July
In July 2021, NIST published guidance for outlining
security measures for critical software use and
minimum standards for vendors’ testing of their
software source code.

Also in July, the National Telecommunications
and Information Administration (NTIA) released a
minimum definition of an SBOM. This was a critical
step toward improving transparency for software
supply chains for both technology vendors and
government customers.

The NTIA describes an SBOM as “effectively a
nested inventory, a list of ingredients that make
up software components, and provides those who
produce, purchase, and operate software with infor-
mation that enhances their understanding of the
supply chain. SBOMs are a formal, machine-read-
able inventory of software components and
dependencies. SBOMs contain information
about those components, and their hierarchical
relationships. SBOMs may include open source or
proprietary software and can be widely available or
access-restricted.”

Further, NTIA defined the minimum elements for a
SBOM as three broad, interrelated areas:

1.  Data Fields: Documenting baseline information
about each component that should be tracked.

2. Automation Support: Allowing for scaling across

the software ecosystem through automatic
generation and machine-readability.

3.  Practices and Processes: Defining the opera-
tions of SBOM requests, generation, and use.

strictly on strengthening cybersecurity, including
a “Pipeline Security Act,” and “Cybersecurity
Vulnerability Remediation Act.”

The Senate’s Homeland Security and Governmental
Affairs Committee introduced The Supply Chain
Security Training Act, calling it, “bipartisan legisla-
tion to help protect against cybersecurity threats and
other technological supply chain security vulner-
abilities that arise when the federal government
purchases services, equipment or products.

“As supply chains
become interconnected,
vulnerabilities in suppliers’
products and services ...
become more attractive
targets for attackers.”
— U.K. government’s request for advice on
   defending against digital supply chain attacks

Furthermore in July, both the House of
Representatives and the Senate began drafting
legislation in two separate committees.

The House’s Homeland Security Committee intro-
duced seven bipartisan bills, five of which focused

What’s Happening in the
United Kingdom?
In May 2021, the U.K. government announced that
it was seeking advice on defending against digital
supply chain attacks from organizations that either
consume IT services, or MSPs that provide software
and services.

35

2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTCHAPTER 5: EMERGENCE OF SOFTWARE SUPPLY CHAIN REGULATION AND STANDARDSThe request noted:

"As supply chains become interconnected,
vulnerabilities in suppliers' products and
services correspondingly become more
attractive targets for attackers who want
to gain access to the organisations. Recent
high-profile cyber incidents where attackers
have used MSPs as a means to attack
companies are a stark reminder that cyber
threat actors are more than capable of
exploiting vulnerabilities in supply chain
security, and seemingly small players in an
organisation's supply chain can introduce
disproportionately high levels of cyber risk."

Also in May, the Department for Digital, Culture,
Media, and Sport (DCMS) opened up a survey that
closed in early July, and invited comments from
industry experts and tech organizations on step-
ping up supply chain security across the UK.

The initiative is a part of the U.K.’s nationwide
"cyber resilience" efforts set out in its National
Cyber Security Strategy to safeguard businesses
and organizations that increasingly rely on technol-
ogy from cyber-attacks, and to strengthen overall
digital supply chain security.

While the feedback has not been released to the
public yet, the U.K. government has noted that it
will result in the re-evaluation of supply chain risks,
reviewing policies, and likely implementing new
guidelines and frameworks to strengthen specific
areas of digital supply chain security. It could also
mean the introduction of new, country-wide legisla-
tion for software firms and IT service providers.

What’s Happening in Germany?
In May 2021, Germany passed the Information
Technology Security Act 2.0 as an update to the
First Act to “increase cyber and information security
against the backdrop of increasingly frequent and
complex cyber-attacks and the continued digital-
isation of everyday life.” While this Act influences
many areas of the IT industry in Germany, it spe-
cifically states that suppliers, i.e. manufacturers of
critical components, will also be subject to certain
obligations to safeguard the entire supply chain.

Critical components are defined as IT products:

1.  that are used in critical infrastructures;

2. for which disruptions to availability, integrity,
authenticity, and confidentiality may lead to a
failure or a significant impairment of the func-
tionality of critical infrastructures or to threats to
public safety; and

3.  that on the basis of a law regarding this provision

are designated as a critical component, or
realize a function designated as critical on the
basis of a law.

“Attackers focused
on the suppliers’ code
in about 66% of the
reported incidents.”

— ENOSA report, “Understanding the Increase
   in Supply Chain Security Attacks”

 ⊲ “For 58% of the supply chain incidents analysed,

the customer assets targeted were predominantly
customer data, including Personally Identifiable
Information (PII) data and intellectual property.”

 ⊲ “For 66% of the supply chain attacks analysed,

suppliers did not know, or failed to report on how
they were compromised. However, less than 9% of
the customers compromised through supply chain
attacks did not know how the attacks occurred.”

What’s Happening in the
European Union?
In July 2021, the ENISA issued a report titled
“Understanding the increase in Supply Chain
Security Attacks” that reviewed 24 different
software supply chain attacks and how they came
to fruition.

It found that:

 ⊲ “In order to compromise the targeted customers,
attackers focused on the suppliers’ code in about
66% of the reported incidents.”

More importantly, the report shared recommen-
dations that organizations should put in place.
While more guidance than regulation, it does
foreshadow what could come down the road.

Suggestions include:

 ⊲ identifying and documenting suppliers and

service providers;

 ⊲ defining risk criteria for different types of suppli-
ers and services such as supplier and customer
dependencies, critical software dependencies,
single points of failure;

36

2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTCHAPTER 5: EMERGENCE OF SOFTWARE SUPPLY CHAIN REGULATION AND STANDARDS(c) Increased attention in national policy
and in dialogue with States and relevant
actors at the United Nations and other fora
on how to ensure all States can compete
and innovate on an equal footing, so as to
enable the full realization of ICTs to increase
global social and economic development and
contribute to the maintenance of international
peace and security, while also safeguarding
national security and the public interest.

You can read the full list of guidance provided by
the United Nations.

June
In June 2021, the United States and the European
Union formed a Trade and Technology Council
(TTC). This was in part developed to work together
on the fight to secure critical technology and
software supply chains. According to the White
House, the TTC “will be composed of working
groups focused on advancing cooperation on tech
standards on artificial intelligence, the internet
of things and other emerging technologies, ICT
security, data governance, investment screening
and semiconductors.”

 ⊲ monitoring of supply chain risks and threats;

 ⊲ managing suppliers over the whole lifecycle of
a product or service, including procedures to
handle end-of-life products or components;

 ⊲ classifying of assets and information shared with
or accessible to suppliers, and defining relevant
procedures for accessing and handling them.

The report also suggests possible actions to assure
that the development of products and services
comply with security practices. Suppliers are
advised to implement better policies for vulnerabil-
ity and patch management.

Recommendations for suppliers include:

 ⊲ ensuring that the infrastructure used to design,

develop, manufacture, and deliver products, compo-
nents and services follows cybersecurity practices;

 ⊲ implementing a product development, maintenance,

and support process that is consistent with com-
monly accepted product development processes;

 ⊲ monitoring of security vulnerabilities reported by
internal and external sources that includes used
third-party components;

 ⊲ maintaining an inventory of assets that includes

patch-relevant information.

Similar to actions at the national and regional
levels, the report touches on several areas of
cybersecurity, and provides guidance on the
“reasonable steps States should take to ensure the
integrity of the supply chain so that end users can
have confidence in the security of information and
communication technology (ICT) products.”

The report notes:

Ensuring the integrity of the ICT supply
chain and the security of ICT products, and
preventing the proliferation of malicious ICT
tools and techniques and the use of harmful
hidden functions are increasingly critical in that
regard, as well as to international security, and
digital and broader economic development.

Global ICT supply chains are extensive,
increasingly complex and interdependent,
and involve many different parties.
Reasonable steps to promote openness
and ensure the integrity, stability and
security of the supply chain can include:

(a) Putting in place at the national level
comprehensive, transparent, objective and
impartial frameworks and mechanisms for
supply chain risk management, consistent
with a State’s international obligations.

What’s Happening Globally?
May
In May 2021, the United Nations released a
report two years in the making from “the Group of
Governmental Experts on Advancing responsible
State behaviour in cyberspace in the context of
international security.”

(b) Establishing policies and programmes to
objectively promote the adoption of good
practices by suppliers and vendors of ICT
equipment and systems in order to build
international confidence in the integrity
and security of ICT products and services,
enhance quality and promote choice.

37

2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTCHAPTER 5: EMERGENCE OF SOFTWARE SUPPLY CHAIN REGULATION AND STANDARDSAbout the Analysis

The authors have taken great care to present statistically significant sample sizes with regard to
component versions, downloads, vulnerability counts, and other data surfaced in this year’s report.
While Sonatype has direct access to primary data for Java, JavaScript, Python, .NET and other
component formats, we also reference third-party data sources as documented. Further, Sonatype’s
research analyzed scan data from 100,000 anonymized, validated applications.

38

2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTAcknowledgments

Each year, the State of the Software Supply Chain report is a labor of love. It is produced to shed light on
the patterns and practices associated with OSS development and the evolution of software supply chain
management practices.

The report is made possible thanks to a tremendous effort put forth by many team members at Sonatype,
including: Bruce Mayhew, Dr. Stephen Magill, Matt Howard, Ax Sharma, Sal Kimmich, Elissa Walters,
Alli VanKanegan, Juan Morales, Moncef Ben-Soula, Cody Nash, Andrew Yorra, Brian Fox, Mike Hansen,
Joel Orlina, Melissa Schmidt, Ember DeBoer, Ilkka Turunen, Luke Mcbride.

We would also like to offer thanks for contributions big and small and for sharing perspective to our many
colleagues across the DevOps and open source development community.

A very special thanks goes out to Alli VanKanegan who created the incredible design for this year’s report.

39

2021 STATE OF THE SOFTWARE SUPPLY CHAIN REPORTSonatype is the leader in developer-friendly, full-spectrum software supply chain management providing organizations total control of their
cloud-native development life cycles, including third-party open source code, first-party source code, infrastructure as code, and containerized
code. The company supports 70% of the Fortune 100 and its commercial and open source tools are trusted by 15 million developers around the
world. With a vision to transform the way the world innovates, Sonatype helps organizations of all sizes build higher quality software that’s more
aligned with business needs, more maintainable, and more secure. For more information, please visit Sonatype.com, or connect with us on
Facebook, Twitter, or LinkedIn.

Headquarters

European Office

APAC Office

Sonatype Inc.

8161 Maple Lawn Blvd, Suite 250

199 Bishopsgate

5 Martin Place, Level 14

www.sonatype.com

Fulton, MD 20759

London EC2M 3TY

Sydney 2000, NSW

Copyright 2021

USA • 1.877.866.2836

United Kingdom

Australia

All Rights Reserved.