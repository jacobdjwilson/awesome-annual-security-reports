# Secure-By-Design

**Organization:** CISA  
**Report Title:** Secure-By-Design  
**Year:** 2023  

## Table of Contents
- [Overview: Vulnerable By Design](#overview-vulnerable-by-design)
- [What's New](#whats-new)
- [How To Use This Document](#how-to-use-this-document)
- [Secure by Design](#secure-by-design)
- [Secure by Default](#secure-by-default)
- [Recommendations for Software Manufacturers](#recommendations-for-software-manufacturers)
- [Software Product Security Principles](#software-product-security-principles)
- [Principle 1: Take Ownership of Customer Security Outcomes](#principle-1-take-ownership-of-customer-security-outcomes)
- [Principle 2: Embrace Radical Transparency and Accountability](#principle-2-embrace-radical-transparency-and-accountability)
- [Principle 3: Lead from the Top](#principle-3-lead-from-the-top)
- [Secure by Design Tactics](#secure-by-design-tactics)
- [Secure by Default Tactics](#secure-by-default-tactics)
- [Hardening vs Loosening Guides](#hardening-vs-loosening-guides)
- [Recommendations for Customers](#recommendations-for-customers)
- [Disclaimer](#disclaimer)
- [Resources](#resources)
- [References](#references)

---

## Overview: Vulnerable By Design

Technology is integrated into nearly every facet of daily life, as internet-facing systems increasingly connect us to critical systems that directly impact our economic prosperity, livelihoods, and even health, ranging from personal identity management to medical care. One example of the disadvantage of such conveniences are the global cyber breaches resulting in hospitals canceling surgeries and diverting patient care. Insecure technology and vulnerabilities in critical systems may invite malicious cyber intrusions, leading to potential safety[^1] risks.

As a result, it is crucial for software manufacturers to make secure by design and secure by default the focal points of product design and development processes. Some vendors have made great strides driving the industry forward in software assurance, while others continue to lag behind. The authoring organizations strongly encourage every technology manufacturer to build their products based on reducing the burden of cybersecurity on customers, including preventing them from having to constantly perform monitoring, routine updates, and damage control on their systems to mitigate cyber intrusions. We also urge the software manufacturers to build their products in a way that facilitates automation of configuration, monitoring, and routine updates. Manufacturers are encouraged to take ownership of improving the security outcomes of their customers.

Historically, software manufacturers have relied on fixing vulnerabilities found after the customers have deployed the products, requiring the customers to apply those patches at their own expense. Only by incorporating secure by design practices will we break the vicious cycle of constantly creating and applying fixes. Note: The term “secure by design” encompasses both secure by design and secure by default.

To accomplish this high standard of software security, the authoring organizations encourage manufacturers to prioritize the integration of product security as a critical prerequisite to features and speed to market. Over time, engineering teams will be able to establish a new steady-state rhythm where security is truly designed-in and takes less effort to maintain.

Reflecting this perspective, the European Union reinforces the importance of product security in the Cyber Resilience Act, emphasizing that manufacturers should implement security throughout a product's life-cycle in order to prevent manufacturers from introducing vulnerable products into the market.

[^1]: The authoring organizations recognize that the term “safety” has multiple meanings depending on the context. For the purposes of this guide, “safety” will refer to raising technology security standards to protect customers from malicious cyber activity.

---

## What's New

The initial publication of this report generated a significant amount of conversation within the software industry. Daily news of organizations and individuals being compromised highlights the need for more conversation regarding how to address chronic and systemic problems in software products.

After the release in April 2023, the authoring organizations (henceforth referred to as “we” and “our”) received thoughtful feedback from hundreds of individuals, companies, and trade associations. The most common request in the feedback was to provide more detail on the three principles as they apply to both software manufacturers and their customers. In this document, we expand on the original report and touch on other themes such as manufacturer and customer size, customer maturity, and the scope of the principles.

This report applies to manufacturers of artificial intelligence (AI) software systems and models as well. While they might differ from traditional forms of software, fundamental security practices still apply to AI systems and models. Some secure by design practices may need modification to account for AI-specific considerations, but the three overarching secure by design principles apply to all AI systems.

---

## How To Use This Document

We urge software manufacturers to adhere to the principles within this document. Software manufacturers can demonstrate their commitment by publicly documenting their actions taken, in line with the steps listed below. We encourage software manufacturers to find tactics that meet the spirit of these principles and to create artifacts that will build a compelling case to even skeptical current and potential customers that they are embodying the secure by design philosophy.

In addition to actions software manufacturers should take, customers can also leverage this document. Companies buying software should ask hard questions of their vendors, drawing inspiration from the examples of adhering to the principles listed in this document. In doing so, customers can help to shift the market towards products that are more secure by design.

---

## Secure by Design

“Secure by design” means that technology products are built in a way that reasonably protects against malicious cyber actors successfully gaining access to devices, data, and connected infrastructure. Software manufacturers should perform a risk assessment to identify and enumerate prevalent cyber threats to critical systems, and then include protections in product blueprints that account for the evolving cyber threat landscape.

---

## Secure by Default

“Secure by default” means products are resilient against prevalent exploitation techniques out of the box without added charge. These products protect against the most prevalent threats and vulnerabilities without end-users having to take additional steps to secure them. Secure by default products are designed to make customers acutely aware that when they deviate from safe defaults, they are increasing the likelihood of compromise unless they implement additional compensatory controls.

---

## Software Product Security Principles

Software manufacturers are encouraged to adopt a strategic focus that prioritizes software security. The authoring organizations developed the following three core principles:

1. **Take ownership of customer security outcomes and evolve products accordingly.** The burden of security should not fall solely on the customer.
2. **Embrace radical transparency and accountability.** Software manufacturers should pride themselves in delivering safe and secure products.
3. **Build organizational structure and leadership to achieve these goals.** Senior executives are the primary decision makers for implementing change in an organization.

---

## Principle 1: Take Ownership of Customer Security Outcomes

Modern best practices dictate that software manufacturers invest in product security efforts that include application hardening, application features, and application default settings. Software manufacturers need to implement application hardening by using processes and technologies that raise the cost for a malicious actor wishing to compromise applications.

---

## Principle 2: Embrace Radical Transparency and Accountability

Software manufacturers should pride themselves in delivering safe and secure products, as well as differentiating themselves from the rest of the manufacturer community based on their ability to do so. Transparency helps the industry establish conventions—in other words, what “good” looks like. It helps those conventions change over time in response to customer needs, changes in threat actor tactics or economics, or technology evolution.

---

## Principle 3: Lead from the Top

While the overall philosophy is called “secure by design,” the incentives for customer safety begin well before the product design phase. They begin with business goals and implicit and explicit objectives and desired outcomes. Only when senior leaders make security a business priority, creating internal...

![Image: CISA/NSA/FBI/International Partner Logos]

---

l incentives and fostering an across-the-board culture to
make security a design requirement, will they achieve the best results
While technical subject mater expertise is critical to product security, it is
not a mater that can be solely lef to technical staf It is a business priority
that must start at the top
Some people have wondered if a sofware manufacturer is embracing the
first two principles and producing meaningful artifacts, is the third principle
necessary? How a company establishes its vision, mission, values, and
culture will afect the product, and those elements have a heavy component
at the top We see this in other industries that have made dramatic
improvements in safety and quality Noted quality expert J M Juran wrote:
Atainment of quality leadership requires that the
upper managers personally take charge of managing
for quality. In companies that did atain quality
leadership, the upper managers personally guided
the initiative. I am not aware of any exceptions. [3]
We believe that security is a sub-category of product quality. When
security and quality become business imperatives rather than technical
functions lef solely to technical staf, organizations will be able to respond
to the security needs of their customers more quickly and eficiently
Moreover, investing the necessary resources to ensure that sofware
security is a core business priority from the beginning will reduce the long-
term costs of addressing sofware defects–and in turn, lower the national
security risks
In the same way that leadership teams have implemented corporate social
responsibility (CSR) programs, there is growing awareness that corporate
boards, including those of sofware manufacturers, should take a more
active role in guiding cybersecurity programs The term corporate cyber
responsibility (CCR) is sometimes used to describe this emerging idea
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 26

TLP:CLEAR
DEMONSTRATING THIS PRINCIPLE
To demonstrate this principle, sofware manufacturers should take steps including the
following:
1. Include details of a secure by design 4. Create meaningful internal incentives. While
program in corporate financial reports. being mindful to not create perverse incentives,
If the manufacturer is a publicly traded align reward systems to improve customer
company, add a section in each annual security to match other valued behaviors and
report devoted to secure by design eforts outcomes From the secure by design executive
It is common for automobile annual financial to product management, sofware development,
reports to include sections on driver and support, sales, legal, and other organizations,
passenger safety, including information weave customer security incentives into hiring,
about centralized and distributed quality promotions, salaries, bonuses, stock options, and
and safety commitees Detailing the secure other common processes in the running of the
by design program in a financial report will business For example, when establishing criteria
demonstrate that the organization is linking for promoting sofware developers, include
customer security and corporate financial considerations for improving the security of the
outcomes and not simply adopting a term in product along with other criteria like uptime,
marketing materials because it is in vogue performance, and feature improvements
2. Provide regular reports to your board 5. Create a secure by design council. In some
of directors. Chief information security industries, it is common for organizations to
oficer (CISO) reports to corporate boards create a central quality council, and to embed
usually include information about current quality representatives in key divisions or
and planned security programs, threats, business units By including both centralized
suspected and confirmed security incidents, and distributed members, these groups work
and other updates centered on the security to improve quality against top level goals while
posture and health of the company In receiving telemetry from deep in the organization
addition to receiving information about the Similarly, a secure by design council would
security posture of the enterprise, boards improve security against secure by design goals
should request information about product throughout the organization
security and the impact it has on customer
6. Create and evolve customer councils. Many
security Boards should not look solely to
sofware manufacturers have customer councils
the CISO, but primarily to other members
comprised of customers from diferent regions,
of company management to drive customer
industries, and sizes These councils can provide
risk down
a great deal of information about customer
3. Empower the secure by design executive. successes and challenges in deploying the
There is a significant diference between an company’s products Structure the council agenda
organization where the technical teams have with dedicated topics addressing customer
“executive buy-in,” and those where business safety, even if it is not currently top of mind for
leaders personally manage the customer the participants Consider where the customer
security improvement process using council reports and how to tap participants for
standard business processes The term insights into the product’s security as deployed
“executive buy-in” implies that someone had For example, does the council have a bias towards
to sell the idea of a customer safety program marketing and sales purposes, or product
rather than it being a top-level business management? The secure by design executive
goal This executive must be empowered to should help steer these customer interactions and
influence product investments to achieve should link them with other elements in this paper,
customer security outcomes such as field studies
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 27

TLP:CLEAR
SECURE BY DESIGN TACTICS
The Secure Sofware Development Framework (SSDF), also known as the National
Institute of Standards and Technology’s (NIST’s) SP 800-218, is a core set of high-level
secure sofware development practices that can be integrated into each stage of the
sofware development lifecycle (SDLC) Following these practices can help sofware
producers become more efective at finding and removing vulnerabilities in released
sofware, mitigate the potential impact of the exploitation of vulnerabilities, and address
the root causes of vulnerabilities to prevent future recurrences
The authoring organizations encourage the use of secure by design tactics, including
principles that reference SSDF practices Sofware manufacturers should develop a
writen roadmap to adopt more secure by design sofware development practices across
their portfolio The following is a non-exhaustive illustrative list of roadmap best practices:
• Memory safe programming languages (SSDF PW.6.1). Prioritize the use of memory
safe languages wherever possible The authoring organizations acknowledge
that memory specific mitigations may be helpful shorter- term tactics for legacy
codebases Examples include C/C++ language improvements, hardware mitigations,
address space layout randomization (ASLR), control-flow integrity (CFI), and
fuzzing Nevertheless, there is a growing consensus that adoption of memory
safe programming languages can eliminate this class of defect, and sofware
manufacturers should explore ways to adopt them Some examples of modern
memory safe languages include C#, Rust, Ruby, Java, Go, and Swif Read NSA’s
memory safety information sheet for more
• Secure Hardware Foundation. Incorporate architectural features that enable
fine- grained memory protection, such as those described by Capability Hardware
Enhanced RISC Instructions (CHERI) that can extend conventional hardware
Instruction-Set Architectures (ISAs), as well as other features like Trusted Platform
Modules and Hardware Security Modules For more information visit, University of
Cambridge’sCHERI webpage
• Secure Sofware Components (SSDF PW 4.1). Acquire and maintain well-secured
sofware components (e g , sofware libraries, modules, middleware, frameworks)
from verified commercial, open source, and other third-party developers to ensure
robust security in consumer sofware products
• Web template frameworks (SSDF PW.5.1). Use web template frameworks that
implement automatic escaping of user input to avoid web atacks such as cross-site
scripting
• Parameterized queries (SSDF PW 5.1). Use parameterized queries rather than
including user input in queries, to avoid SQL injection atacks
• Static and dynamic application security testing (SAST/DAST) (SSDF PW 7 2,
PW 8 2) Use these tools to analyze product source code and application behavior
to detect error-prone practices These tools cover issues ranging from improper
management of memory to error prone database query construction (e g ,
unescaped user input leading to SQL injection) SAST and DAST tools can be
incorporated into development processes and run automatically as part of sofware
development SAST and DAST should complement other types of testing, such
as unit testing and integration testing, to ensure products comply with expected
security requirements When issues are identified, manufacturers should perform
root-cause analysis to systemically address vulnerabilities
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 28

TLP:CLEAR
• Code review (SSDF PW 7 1, PW 7 2) Strive to ensure that code submited into
products goes through quality control techniques such as peer review by other
developers or “error seeding ”
• Sofware Bill of Materials (SBOM) (SSDF PS 3 2, PW 4 1) Incorporate the creation
of SBOM4 to provide visibility into the set of sofware that goes into products
• Vulnerability disclosure programs (SSDF RV 1 3) Establish vulnerability disclosure
programs that allow security researchers to report vulnerabilities and receive
legal safe harbor in doing so As part of this, suppliers should establish processes
to determine root causes of discovered vulnerabilities Such processes should
include determining whether adopting any of the secure by design practices in this
document (or other similar practices) would have prevented the introduction of the
vulnerability
• CVE completeness. Ensure that published CVEs include root cause or common
weakness enumeration (CWE) to enable industry- wide analysis of sofware
security design flaws While ensuring that every CVE is correct and complete can
take extra time, it allows disparate entities to spot industry trends that benefit all
manufacturers and customers For more information on managing vulnerabilities,
see CISA’sStakeholder- Specific Vulnerability Categorization (SSVC) guidance
• Defense-in-Depth. Design infrastructure so that the compromise of a single
security control does not result in compromise of the entire system For example,
ensuring that user privileges are narrowly provisioned, and access control lists
are employed can reduce the impact of a compromised account Also, sofware
sandboxing techniques can quarantine a vulnerability to limit compromise of an
entire application
• Satisfy Cybersecurity Performance Goals (CPGs). Design products that meet basic
security practices CISA’s Cybersecurity Performance Goals outline fundamental,
baseline cybersecurity measures organizations should implement Additionally, for
more ways to strengthen your organization’s posture, see the NCSC–UK’s Cyber
Assessment Framework which shares similarities to CISA’s CPGs If a manufacturer
fails to meet the CPGs— such as not requiring phishing-resistant MFA for all
employees— then they cannot be seen as delivering secure by design products
The authoring organizations recognize that these changes are significant shifs in
an organization’s posture As such, their introduction should be prioritized based on
tailored threat modeling, criticality, complexity, and business impact These practices
can be introduced for new sofware and incrementally expanded to cover additional use
cases and products In some cases, the criticality and risk posture of a certain product
may merit an accelerated schedule to adopt these practices In others, practices can be
introduced into a legacy codebase and remediated over time
4 Some of the authoring organizations are exploring alternate approaches to gaining security assurances around the software
supply chain.
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 29

TLP:CLEAR
SECURE BY DEFAULT TACTICS
In addition to adopting secure by design development practices, the authoring
organizations recommend sofware manufacturers prioritize secure by default
configurations in their products These should strive to update products to conform to
these practices as they are refreshed For example:
• Eliminate default passwords. Products should not come with default passwords that
are universally shared To eliminate default passwords, the authoring organizations
recommend products require administrators to set a strong password during
installation and configuration or for the product to ship with a unique, strong password
for each device
• Mandate multifactor authentication (MFA) for privileged users. We observe that
many enterprise deployments are managed by administrators who have not protected
their accounts with MFA Given that administrators are high value targets, products
should make MFA opt-out rather than opt-in Further, the system should regularly
prompt the administrator to enroll in MFA until they have successfully enabled it on
their account Netherlands’ NCSC has guidance that parallels CISA’s, visit their Mature
Authentication Factsheet for more information
• Single sign-on (SSO). IT applications should implement single sign on support via
modern open standards Examples include Security Assertion Markup Language
(SAML) or OpenID Connect (OIDC ) This capability should be made available by default
at no additional cost
• Secure Logging. Provide high-quality audit logs to customers at no extra charge or
additional configuration Audit logs are crucial for detecting and escalating potential
security incidents They are also crucial during an investigation of a suspected or
confirmed security incident Consider best practices such as providing easy integration
with security information and event management (SIEM) systems with application
programming interface (API) access that uses coordinated universal time (UTC),
standard time zone formating, and robust documentation techniques
• Sofware Authorization Profile. Sofware suppliers should provide recommendations
on authorized profile roles and their designated use case Manufacturers should
include a visible warning that notifies customers of an increased risk if they deviate
from the recommended profile authorization For example, medical doctors can view all
patient records, but a medical scheduler has limited access to certain information that
is required for scheduling appointments
• Forward-looking security over backwards compatibility. Too ofen, backwards-
compatible legacy features are included, and ofen enabled, in products despite
causing risks to product security Prioritize security over backwards compatibility,
empowering security teams to remove insecure features even if it means causing
breaking changes
• Track and reduce “hardening guide” size. Reduce the size of “hardening guides”
that are included with products and strive to ensure that the size shrinks over time as
new versions of the sofware are released Integrate components of the “hardening
guide” as the default configuration of the product The authoring organizations
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 30

TLP:CLEAR
recognize that shortened hardening guides result from ongoing partnership with
existing customers and include eforts by many product teams, including user
experience (UX)
• Consider the user experience consequences of security setings. Each new seting
increases the cognitive burden on end users and should be assessed in conjunction
with the business benefit it derives Ideally, a seting should not exist; instead, the most
secure seting should be integrated into the product by default When configuration is
necessary, the default option should be broadly secure against common threats
The authoring organizations acknowledge these changes may have operational efects
on how the sofware is employed Thus, customer input is critical in balancing operational
and security considerations We believe that developing writen roadmaps and executive
support that prioritize these ideas into an organization’s most critical products is the first
step to shifing towards secure sofware development practices While customer input
is important, we have observed important cases where customers have been unwilling
or unable to adopt improved standards, ofen network protocols It is important for the
manufacturers to create meaningful incentives for customers to stay current and not
allow them to remain vulnerable indefinitely
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 31

TLP:CLEAR
HARDENING VS LOOSENING GUIDES
Hardening guides may result from the lack of product security controls being
embedded into a product’s architecture from the start of development Consequently,
hardening guides can also be a roadmap for adversaries to pinpoint and exploit
insecure features It is common for many organizations to be unaware of hardening
guides, thus they leave their device configuration setings in an insecure posture An
inverted model known as a loosening guide should replace such hardening guides
and explain which changes users should make while also listing the resulting security
risks These guides should be writen by security practitioners who can explain the
tradeofs in clear language to increase the chances of them being applied correctly
Rather than developing hardening guides that list methods for securing products,
the authoring organizations recommend sofware manufacturers shif to a secure by
default approach and providing "loosening guides " These guides explain the business
risk of decisions in plain, understandable language, and can raise organizational
awareness of risks to malicious cyber intrusions Security tradeofs should be
determined by the customers’ senior executives, balancing security with other
business requirements
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 32

TLP:CLEAR
RECOMMENDATIONS
FOR CUSTOMERS
The authoring organizations recommend organizations hold
their supplying sofware manufacturers accountable for the
security outcomes of their products As part of this, the authoring
organizations recommend that executives prioritize the importance
of purchasing secure by design and secure by default products
This can manifest through establishing policies requiring that IT
departments assess the security of sofware before it is purchased,
as well as empowering IT departments to push back if necessary IT
departments should be empowered to develop purchasing criteria
that emphasize the importance of secure by design and secure by
default practices (both those outlined in this document and others
developed by the organization) Furthermore, IT departments
should be supported by executive management when enforcing
these criteria in purchasing decisions Organizational decisions
to accept the risks associated with specific technology products
should be formally documented, approved by a senior business
executive, and regularly presented to the board of directors
Key enterprise IT services that support the organization’s security
posture, such as the enterprise network, enterprise identity and
access management, and security operations and response
capabilities, should be seen as critical business functions that are
funded to align with their importance to the organization’s mission
success Organizations should develop a plan to upgrade these
capabilities to leverage manufacturers that embrace secure by
design and secure by default practices
Where possible, organizations should strive to forge strategic
relationships with their key IT suppliers Such relationships include
trust at multiple levels of the organization and provide vehicles
to resolve issues and identify shared priorities Security should
be a critical element of such relationships and organizations
should strive to reinforce the importance of secure by design and
secure by default practices in both the formal (e g , contracts or
vendor agreements) and informal dimensions of the relationship
Organizations should expect transparency from their technology
suppliers about their internal control posture as well as their
roadmap towards adopting secure by design and secure by default
practices
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 33

TLP:CLEAR
In addition to making secure by default a priority within an organization, IT leaders
should collaborate with their industry peers to understand which products and
services best embody these design principles These leaders should coordinate
their requests to help manufacturers prioritize their upcoming security
initiatives By working together, customers can help provide meaningful input to
manufacturers and create incentives for them to prioritize security
When leveraging cloud systems, organizations should ensure they understand the
shared responsibility model with their technology supplier That is, organizations
should have clarity on the supplier's security responsibilities rather than just the
customer’s responsibilities
Organizations should prioritize cloud providers that are transparent about their
security posture, internal controls, and ability to live up to their obligations under
the shared responsibility model
DISCLAIMER
The information in this report is being provided “as is” for informational purposes only.
CISA and the authoring organizations do not endorse any commercial product or service,
including any subjects of analysis. Any reference to specifc commercial entities or
commercial products, processes, or services by service mark, trademark, manufacturer,
or otherwise does not constitute or imply endorsement, recommendation, or favoritism by
CISA and the authoring organizations. This document is a joint initiative by CISA that does
not automatically serve as a regulatory document.
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 34

TLP:CLEAR
CISA
» CISA’s SBOM Guidance
» CISA’s Cross -Sector Cybersecurity Performance Goals
» Guidelines on Technology Interoperability
» CISA and NIST’s Defending Against Software Supply Chain Attacks
» The Cost of Unsafe Technology and What We Can Do About It | CISA
» Stop Passing the Buck on Cybersecurity: Why Companies Must Build
Safety Into Tech Products (foreignafairs.com)
» CISA’s Stakeholder- Specifc Vulnerability Categorization (SSVC) Guidance
» CISA’s Phishing Resistant MFA Fact Sheets
» Cyber Guidance for Small Businesses | CISA
NSA
» NSA’s Cybersecurity Information Sheet on Memory Safety
» NSA’s ESF Securing the Software Supply Chain: Best Practices for
Suppliers
FBI
» Understanding and Responding to the SolarWinds Supply Chain Attack:
The Federal Perspective
» The Cyber Threat - Response and Reporting
» FBI’s Cyber Strategy
National Institute of Standards and Technology (NIST)
» NIST’s Digital Identity Guidelines
» NIST’s Cybersecurity Framework
» NIST’s Secure Software Development Framework (SSDF)
Australian Cyber Security Centre (ACSC)
» ACSC’s IoT Secure-by-Design Guidance for Manufacturers
The United Kingdom’s National Cyber Security Centre (UK)
» The NCSC–UK’s Cyber Assessment Framework
» The NCSC–UK’s Secure Development and Deployment guidance
» The NCSC–UK’s Vulnerability Management guidance
» The NCSC–UK’s Vulnerability Disclosure Toolkit
» University of Cambridge’s CHERI
» So long and thanks for all the bits - NCSC.GOV.UK
Canadian Centre for Cyber Security (CCCS)
» CCCS’s Guidance on Protecting Against Software Supply Chain Attacks
» Cyber supply chain: An approach to assessing risks
» Canadian Centre for Cyber Security’s CONTI ransomware guidance
secruoseR
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 35

TLP:CLEAR
Germany’s Federal Office for Information Security (BSI)
» BSI IT Baseline Protection Compendium Edition 2022
» The international standard IEC 62443, part 4-1
» The state of IT security in Germany in 2022
» Web Application Security: Catalog of Measures and Best Practices
Netherland’s National Cyber Security Centre
» NCSC-NL’s Mature Authentication Factsheet
Japan’s National Center of Incident Readiness and Strategy
for Cybersecurity (NISC)
» Japan’s National Cybersecurity Strategy
Japan’s Ministry of Economy, Trade and Industry (METI)
» Guide of Introduction of Software Bill of Materials (SBOM) for Software
Management
» Collection of Use Case Examples Regarding Management Methods for
Utilizing OSS and Ensuring Its Security
Cyber Security Agency of Singapore
» Technical Advisory on Secure API Development
» CSA SingCERT Vulnerability Disclosure Policy
» CSA SingCERT Incident Response Checklist
» CSA SingCERT Incident Response Playbooks
» CSA Security by Design Framework
» CSA Security by Design Framework Checklist
» CSA Guide to Cyber Threat Modelling
» CSA Cybersecurity Labelling Scheme
Other
» How Complex Systems Fail
» The New Look in complex system failure
REFERENCES
[1] https://csrc.nist.rip/publications/history/ande72.pdf
[2] https://www.cisa.gov/sbom and SBOMs references in TR 03183-2 https://www.bsi.bund.de/dok/TR-03183
[3] Juran on Quality by Design by J.M. Juran, 1992.
CISA | NSA | FBI | ACSC | CCCS | CERT NZ | NCSC-NZ | NCSC-UK | BSI | NCSC-NL
TLP:CLEAR
NCSC-NO | NÚKIB | INCD | KISA | NISC-JP | JPCERT/CC | CSA | CSIRTAMERICAS 36