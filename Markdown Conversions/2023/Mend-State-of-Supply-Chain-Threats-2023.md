# The State of Supply Chain Threats

August 2023  
Sponsored by Mend  

## Table of Contents
- [Executive Summary](#executive-summary)
- [Research Synopsis](#research-synopsis)
- [High Concerns Over Supply Chain Risk](#high-concerns-over-supply-chain-risk)
- [Work in Progress: Software Supply Chain Security](#work-in-progress-software-supply-chain-security)
- [Profound Impact on Supply Chain Practices](#profound-impact-on-supply-chain-practices)
- [Conclusion](#conclusion)
- [Appendix](#appendix)

---

## Executive Summary

Many organizations changed — or started making significant changes to — their supply chain security practices two years ago to address growing risks from vulnerable third-party software and open source components. On the open source front, the growing number of malicious components being pushed into public code registries — such as npm, PyPI, and Maven — highlights the necessity of these changes. More concerning for organizations is the fact that attackers have exploited zero-day vulnerabilities in multiple, widely used software products, including Microsoft Exchange, Kaseya, and Accellion, to breach numerous government and private entities worldwide.

Dark Reading’s 2023 Supply Chain Threat Survey of 242 IT and cybersecurity professionals shows that a lot has stayed the same in regard to supply chain risk. A relatively high percentage of organizations have implemented processes for mitigating risk from vulnerabilities in the partner ecosystem, and there is strong awareness of what needs to be done to strengthen the security of the software supply chain. Most organizations, for instance, maintain a software bill of materials repository, and more than one-third of respondents expect their organizations to increase their use of SBOMs in the coming year.

More than half the organizations in Dark Reading’s survey require their software suppliers to adhere to stipulated security standards, and nearly one in four want their vendors to submit independent audits or assessments indicating they meet security requirements. Others request ad hoc, point-in-time assessments of their suppliers’ security posture.

What is striking about this report is that different occurrences have affected responses this year versus last. The attacks against Kaseya and Accellion were fresh in the minds of the respondents last year; this year’s respondents were asked to assess their ability to detect and mitigate supply chain attacks while being confronted with the attacks that exploited multiple vulnerabilities in the MOVEit file transfer utility.

While many organizations have implemented multiple processes for managing supply chain risks, a sizable percentage of organizations have not done so and remain at heightened exposure to attacks via the supply chain. Even so, most IT and cybersecurity professionals in the survey appear confident in their organizations’ ability to defend against a supply chain attack and to detect and respond to any incidents that might get past their defenses.

The following are some of the key takeaways from the survey:
- 71% of respondents describe third-party risk and supply chain security as one of their top five security initiatives for the coming year.
- 71% of organizations in the survey say their current security programs cover software supply chain threats, but only 28% explicitly state that their program covers the software supply chain.
- Just 24% of organizations consider their software supply chain secure. For 55% of organizations, software supply chain security is still a work in progress.
- 50% maintain a software bill of materials repository, but just 36% claim to create complete SBOMs for all their software. Just 41% regularly request SBOMs from vendors and suppliers.
- 40% say vulnerabilities in open source software components is their biggest supply chain-related worry; 24% point to developers being tricked into malicious components, via methods such as typosquatting and dependency confusion.
- 34% of respondents who had experienced a supply chain attack over the past year say developers accidentally downloaded malicious components from public code registries, such as PyPI and npm.
- 49% of IT and cybersecurity professionals in the survey say they are most concerned about attackers targeting their organizations via vulnerabilities in widely used commercial platforms.

---

## Research Synopsis

- **Survey Name**: Dark Reading 2023 Supply Chain Threat Survey
- **Survey Date**: June 2023
- **Number of Respondents**: 242 IT and cybersecurity professionals at companies of all sizes, based primarily in North America. The margin of error for the total respondent base ($N=242$) is +/-6.3 percentage points.
- **Purpose**: Dark Reading surveyed information technology and cybersecurity professionals on the supply chain threat landscape; their biggest current concerns; the practices they have implemented to manage supply chain risk; and their capabilities for preventing, detecting, and responding to supply chain-related security issues.
- **Methodology**: The survey queried decision-makers with job titles that involved IT or IT security (cybersecurity) at organizations across more than a dozen industry sectors. It asked them about a wide range of supply chain threats and risk mitigation practices. The survey was conducted online. Respondents were recruited via an email invitation containing an embedded link to the survey. The email invitation was sent to a select group of Informa Tech’s qualified database; Informa is the parent company of Dark Reading. Informa Tech was responsible for all survey design, administration, data collection, and data analysis. These procedures were carried out in strict accordance with standard market research practices and existing US privacy laws.

> ### About Us
> Dark Reading Reports offer original data and insights on the latest trends and practices in IT security. Compiled and written by experts, Dark Reading Reports illustrate the plans and directions of the cybersecurity community and provide advice on the steps enterprises can take to protect their most critical data.

---

## High Concerns Over Supply Chain Risk

Supply chain security was in the headlines for most of 2022 — as well as the first half of 2023 — and it became increasingly clear that "supply chain risk" does not mean the same thing to everyone. Supply chain is one item under application security as organizations worry about the security and provenance of software components used in application development. 

Supply chain is also an item under security operations and cloud security as organizations scrutinize the security preparedness of cloud providers and third-party service providers. Supply chain is also top of mind for organizations that are seeing their data stolen and networks compromised because a business application they rely on has been compromised.

These varied incidents highlight the damage supply chain attacks could cause and heightened concerns about enterprise exposure to different types of supply chain risks. But there are also signs to be optimistic about, such as industrywide efforts to strengthen the security of the software supply chain. Last year’s executive order from the Biden administration requiring federal agencies to adopt a number of software security best practices — such as maintaining a software bill of materials for all software in use, implementing controls to protect build environments, and documenting all software dependencies in use — has pushed organizations to include those conversations as they make their security plans.

Dark Reading’s 2023 Supply Chain Security Survey reflects this heightened sense of awareness. Supply chain security remains a major concern for IT and security professionals, with 71% of all organizations listing supply chain security among their top five security priorities for 2023. It tops the list of security priorities for 12% of organizations. What’s noteworthy is that priorities don’t seem to have shifted at all since last year, when 70% listed supply chain security among their top five (**Figure 1**).

![Figure 1: Priority Level of Supply Chain Security](https://example.com/figure1.png)

There is no clear consensus among security and IT decision-makers on which supply chain security issue concerns them most. Almost half (49%) of respondents cite attacks targeting vulnerabilities in commercial platforms as their biggest supply chain security issue, which is a significant increase from last year (36%) (**Figure 2**). Some of the jump could be directly related to the fact that the survey was conducted around the time when researchers warned that attack groups were actively exploiting a critical zero-day vulnerability in Progress Software’s MOVEit Transfer managed file transfer utility to steal data from organizations. Recent analysis from Brett Callow, a threat analyst at Emsisoft, suggests that 347 organizations have been affected and more than 18.6 million individuals had their data compromised.

![Figure 2: Top Supply Chain Issues](https://example.com/figure2.png)

Perhaps influenced by the attacks targeting MOVEit, respondents to the Dark Reading survey also list concerns that attackers would target their organizations after compromising suppliers and partners (42%), ransomware attacks originating from a supply chain compromise (41%), and disruptions to business processes because the supplier was hit by a cyberattack (38%).

Respondents are also concerned about their exposure to insecure open source components, tools, and frameworks. Forty percent of the respondents say their biggest supply chain security issue has to do with vulnerabilities in open source software components, and 34% say the same about flaws in frameworks and other tools developers use to create applications. About a quarter of respondents (24%) are concerned about their developers being tricked into downloading malicious components.

Typosquatting names and dependency poisoning are types of attacks in which a threat actor introduces malicious components into widely used public software repositories, such as npm, and then tries to trick users into downloading it by, for instance, using the local phone number from a legitimate package.

Enterprise supply chain security also goes beyond software: 13% cite firmware-based attacks as a major concern, and an equal number worry about backdoored hardware components used in devices.

From a risk prioritization standpoint, IT and security leaders are less focused on attacks targeting the partner ecosystem and more focused on mitigating exposure from vulnerable software. The respondents identify software as the most important issue when asked to rank supply chain risks by order of importance. Survey respondents rank risks associated with third-party vendors and contractors third, and other risks associated with open source software fourth, in order of importance (**Figure 3**).

![Figure 3: Importance of Supply Chain Risks](https://example.com/figure3.png)

Third-party libraries are widely used in software development because they give developers a way to quickly add specific functionality to their code. But because the components can nest several layers in the code, sometimes it can be hard to find vulnerabilities in applications.

---

## Work in Progress: Software Supply Chain Security

Dark Reading’s survey shows most respondents are confident about the controls they have in place to mitigate supply chain security risks. Survey respondents express some level of confidence in how their organization would respond to a supply chain attack. Seventy percent indicate their organizations have designated staff to respond to supply chain issues or know whom to call in case of a supply chain attack, and 67% say their organizations have clear processes on how to handle (**Figure 4**). Respondents also suggest they have all the pieces in place to be able to address and mitigate supply chain issues within one to three days (35%). There are roughly equal numbers of respondents with the confidence in their processes to be able to handle an incident in less than 24 hours (22%) and those requiring four days to approximately a week (19%) (**Figure 5**). This suggests some variability remains in the kind of controls in place.

![Figure 4: Response to a Supply Chain Attack](https://example.com/figure4.png)

The confidence these results reflect did not carry over into the respondents’ perception of the overall state of their organizations’ software supply chain security. Less than a quarter (24%) perceive their software supply chain to be fully secure, and almost an equal number (23%) say they have “a ways to go” to secure the software supply chain (**Figure 6**). A third (33%) describe their efforts as a work in progress, either almost or halfway finished.

When asked to rank issues in software supply chain security, respondents say they are worried about vulnerabilities in third-party libraries, followed by developers downloading and importing malicious packages and their components, and attackers tampering with existing libraries and repositories to include malicious code (**Figure 7**). What’s troubling is that despite these concerns, many organizations have not implemented controls to protect their software supply chain and to limit damage. Forty percent restrict their developers in using dependencies only from trusted repositories and registries, and just 36% regularly check container images for vulnerabilities as part of their processes for managing supply chain risk (**Figure 8**). Security analysts consider such scanning — before a container is deployed into production — a fundamental practice for early risk detection and remediation.

The use of vendor scorecards or rating scores from industry consortiums to assess the security of open source components remains an open question. While a plurality, 47%, say they do use some kind of scorecard system to assess software components, the fact that 20% are unsure if their organizations rely on vendor scorecards or rating scores to determine the security of open source components suggests the idea is still in the early stages (**Figure 9**).

![Figure 5: Time to Mitigate Supply Chain Issues](https://example.com/figure5.png)

On the other hand, Dark Reading’s 2023 Supply Chain Threats Survey reveals relatively high awareness and adoption of one supply chain best practice: the software bill of materials.

Half (50%) of organizations maintain a software bill of materials repository, and 48% plan on increasing SBOM use over the next year (**Figure 10**). An SBOM, an inventory of all open source and third-party components used in a particular piece of software, typically includes information such as the license of the software component, its version, and list of known vulnerabilities that may be present. Security experts see SBOMs as key to an organization’s ability to quickly identify and remediate vulnerabilities in open source components in their software. However, the use of SBOMs still seems limited, as only 41% regularly request SBOMs from vendors and suppliers, and the same percentage of respondents uses SBOMs as part of their vulnerability management efforts.

Just a third (33%) have deployed automated tools to minimize human input and reduce the attack surface, and another third (32%) accept only signed components and verify signatures before deployment. Other processes for managing the software supply chain include verifying the changelog and commit history for a particular code component or software project before downloading it (26%), and signature verification before deployment and executing application builds in ephemeral, sealed, or isolated environments (25%).

Respondents were also asked to share their perceptions of how difficult it is to implement build practices and methods for preventing, mitigating, and remediating software supply chain security attacks. The results suggest there is some work left to do. While the respondents tend to be neutral (rating three on a five-point scale), a significant number consider the practices difficult. Forty-three percent say using a hermetic build with all inputs declared with immutable references is difficult (**Figure 11**). Making provenance information — when, where, and how the software was produced — available is one way to ensure the application hasn’t been tampered with, but 32% report that this action is difficult to implement. While respondents agree that shifting left is necessary to secure the software supply chain (55%), the mechanism for doing so remains a daunting process for many of them (**Figure 12**).

---

## Profound Impact on Supply Chain Practices

Breaches resulting from recent vulnerabilities in widely used third-party software and open source components are having a profound effect on enterprise supply chain security practices. The incidents have pushed many organizations over the past year to change — or start making changes to — their approach to managing supply chain risks. Fifty-six percent of organizations surveyed have made some kind of changes to address risks from third-party suppliers and partners; 17% are in the process of making major changes (**Figure 13**). Last year, 65% made changes of some sort (including major ones). What’s more, supply chain concerns in the wake of the attacks against MOVEit would likely push organizations to revamp their practices again on how they handle third-party software and open source risk.

More than half (51%) of responding organizations have stipulated security practices that vendors must adhere to as part of their business relationship (**Figure 16**). Nearly half (49%) enforce least-privilege access rules (**Figure 16**). Nearly half (49%) have segmented their networks to limit lateral movement; 34% require vulnerability scanning of vendor systems; and 22% rely on code analysis, including binary analysis.

The survey shows that concerns about supply chain attacks may be theoretical for many enterprises. Just a quarter (24%) of organizations perceive their software supply chain to be secure, and almost an equal number (23%) say they have "a ways to go" to secure the software supply chain.

![Figure 6: State of Software Supply Chain Security](https://example.com/figure6.png)

---

## Conclusion

*(Note: The conclusion and appendix sections contain supplementary figures and author details as extracted from the source material.)*

---

## Appendix

- **Figure 7**: Concerns About Software Supply Chain
- **Figure 8**: Managing Software Supply Chain
- **Figure 9**: Vendor Scorecards
- **Figure 10**: Software Bills of Materials
- **Figure 11**: Build Practices to Prevent Software Supply Chain Attacks
- **Figure 12**: Software Supply Chain Statements
- **Figure 13**: Effect of Recent Attacks on Organizations’ Approach to Supply Chain Security
- **Figure 14**: Minimizing Third-Party Risk
- **Figure 15**: Types of Information for Supply Chain Assessment
- **Figure 16**: Securing the Supply Chain
- **Figure 17**: Supply Chain Attack
- **Figure 18**: Types of Attacks
- **Figure 19**: Current Protection Against Software Supply Chain Threats
- **Figure 20**: Insurance Partner for Reducing Third-Party Risk
- **Figure 21**: Respondent Region of Residence
- **Figure 22**: Respondent Job Title
- **Figure 23**: Respondent Company Size
- **Figure 24**: Respondent Industry

### About the Authors

**Carol Hildebrand**  
A veteran of Computerworld and CIO magazine, Carol Hildebrand is an award-winning technology writer who focuses on cybersecurity and how it impacts business innovation.

**Fahmida Y. Rashid**  
Dark Reading  
Fahmida Y. Rashid is Dark Reading’s managing editor for features. She has spent over a decade analyzing news events and demystifying security technology for IT professionals and business managers. Her work has appeared in various business and tech trade publications, including VentureBeat, CSO Online, InfoWorld, eWEEK, and CRN.

---

e have not started to secure our   |     |     |     |                                               |               |       |     |          |        |     |
|     |     |     |     |     |     |     |     | software supply chain, but we plan  |     |     |     | respondents say they have experienced supply  |               |       |     |          |        |     |
to  do so
chain attacks over the past year, but 60% state
|     |     | 21% |     |     |     |     |     | We have no plans to secure our  |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|     |     |     |     |     | 20% |     |     | software supply chain           |     |     |     |     |     |     |     |     |     |     |
they have not (Figure 17). Among the victims,
Don’t know
|     |     | 2023 |     |     | 2022 |     |     |     |     |     |     | the  two  | most  | common  | types  |     | of  attacks  |     |
| --- | --- | ---- | --- | --- | ---- | --- | --- | --- | --- | --- | --- | --------- | ----- | ------- | ------ | --- | ------------ | --- |
Data: Dark Reading survey of 242 cybersecurity and IT professionals in   were  those  targeting  the  partner  ecosystem
June 2023 and 115 in June 2022
|     |                                                 |     |     |     |     |                                             |     |               |                 |     |     | (43%)       | and  those  | exploiting  |                | vulnerabilities  |     | in     |
| --- | ----------------------------------------------- | --- | --- | --- | --- | ------------------------------------------- | --- | ------------- | --------------- | --- | --- | ----------- | ----------- | ----------- | -------------- | ---------------- | --- | ------ |
|     |                                                 |     |     |     |     |                                             |     |               |                 |     |     | software    | components  |             | (41%)          | (Figure          |     | 18).   |
|     | contract, and 39% require vendor security self- |     |     |     |     | The use of vendor security risk assessment  |     |               |                 |     |     |             |             |             |                |                  |     |        |
|     |                                                 |     |     |     |     |                                             |     |               |                 |     |     | Despite     | concerns    | about       | typosquatting  |                  |     | and    |
|     | assessments (Figure 14). When organizations     |     |     |     |     | questionnaires has become more widespread,  |     |               |                 |     |     |             |             |             |                |                  |     |        |
|     |                                                 |     |     |     |     |                                             |     |               |                 |     |     | dependency  |             | confusion,  | only           | about            | a   | third  |
|     | ask vendors to conduct self-assessments, they   |     |     |     |     | and  numerous                               |     | standardized  | questionnaires  |     |     |             |             |             |                |                  |     |        |
(34%) of respondents who had experienced
|     | are looking for information such as vulnerability  |     |     |     |     | are readily available for organizations to adapt  |     |     |     |     |     |            |        |         |      |        |             |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | ------------------------------------------------- | --- | --- | --- | --- | --- | ---------- | ------ | ------- | ---- | ------ | ----------- | --- |
|     |                                                    |     |     |     |     |                                                   |     |     |     |     |     | a  supply  | chain  | attack  | say  | their  | developers  |     |
|     | management information (68%), data security        |     |     |     |     | for their use. Among the most widely used are     |     |     |     |     |     |            |        |         |      |        |             |     |
had accidentally downloaded malicious com-
|     | controls  being  | used  | (60%),  | documentation  |     | the Shared Assessment Group’s Standardized  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------- | ----- | ------- | -------------- | --- | ------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ponents from public repositories, such as npm,
|     | on the vendor’s design and testing process  |     |     |     |     | Information Gathering (SIG) questionnaire, the  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ------------------------------------------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
PyPI, and Maven.
|     | (44%), and the vendor’s asset inventory and  |     |     |     |     | National Institute of Standards and Technology  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | -------------------------------------------- | --- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
user  management  practices  (41%)  (Figure  (NIST) vendor questionnaire, and the Vendor  Conclusion
|     | 15). About a third of respondents (35%)  want  |     |     |     |     | Security Alliance questionnaire.  |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | ---------------------------------------------- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Many companies have worked to overhaul their
answers to questions pertaining to the vendor’s
|     |     |     |     |     |     | Nearly three-quarters, or 74%, of organizations  |     |     |     |     |     | supply chain management practices to address  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- |
supply chain levels for software artifacts (SLSA),
|     |     |     |     |     |     | require  multifactor  |     | authentication  |     | for  | third- | risk from vulnerable open source components  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --------------- | --- | ---- | ------ | -------------------------------------------- | --- | --- | --- | --- | --- | --- |
and 38% want a list of vulnerable packages.
and third-party commercial software over the
|                      |     |     |     |     |     | party  access  | to  | secure  | environments,  |     | and  |     |     |     |     |              |     |     |
| -------------------- | --- | --- | --- | --- | --- | -------------- | --- | ------- | -------------- | --- | ---- | --- | --- | --- | --- | ------------ | --- | --- |
| Dark Reading Reports |     |     |     |     |     |                |     |         |                |     |      |     |     |     |     | August 2023  |     | 14  |

The State of Supply Chain Threats
Table of Contents
past two years. Recent vulnerabilities in widely  Figure 7.
|     | used  software  | products  | and  open  | source  |     |     |     |
| --- | --------------- | --------- | ---------- | ------- | --- | --- | --- |
Concerns About Software Supply Chain
components appear to be fueling a lot of the  Thinking specifically about the software supply chain, please rank the following issues that cause you the
change.  most worry from high to low.
A substantial number of organizations in Dark  Overall rank Score
Reading’s 2023 Supply Chain Threats Survey
Vulnerabilities in third-party libraries affecting the security of our
|     |     |     |     |     | 1   | 800 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
application
|     | have  implemented  | comprehensive  |     | controls  |     |     |     |
| --- | ------------------ | -------------- | --- | --------- | --- | --- | --- |
Developers downloading and importing malicious packages and
|     | and recommended best practices — such as  |     |     |     | 2   | 724 |     |
| --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
components
|     | maintaining  | SBOMs  and  | conducting  | vendor  |     |     |     |
| --- | ------------ | ----------- | ----------- | ------- | --- | --- | --- |
Attackers tampering with libraries and code repositories to include
|     |     |     |     |     | 3   | 602 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
questionnaires — for mitigating supply chain  malicious code
risk. But many more have not implemented  Software components used in our code, which is no longer being
|     |     |     |     |     | 4   | 590 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
maintained
these practices and, by their own admission,
Vulnerabilities in build tools and development frameworks used in
|     |     |     |     |     | 5   | 552 |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
are a long way from securing their software  software development
supply chain. Even so, most IT and security
Note: Rank is based on a weighted score. Responses are weighted, and scores represent the sum of all weighted counts.
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023
|     | leaders  view  | their  organizations  | as  | ready  to  |     |     |     |
| --- | -------------- | --------------------- | --- | ---------- | --- | --- | --- |
prevent, detect, and respond to supply chain
breaches – suggesting a potential disconnect
between perception and reality.
| Dark Reading Reports |     |     |     |     |     | August 2023  | 15  |
| -------------------- | --- | --- | --- | --- | --- | ------------ | --- |

The State of Supply Chain Threats
Table of Contents
| Figure 8. |     |     | Figure 9. |     |     |
| --------- | --- | --- | --------- | --- | --- |
Vendor Scorecards
Managing Software Supply Chain
XIDNEPPA How does your organization manage the software supply chain?     2022  Does your organization rely on vendor
  2023
scorecards or rating scores to assess the
We use dependencies that come from only trusted repositories    ....................................................40%  security of open source components?
and registries   .......................................................37%
|     | We regularly check container images for high or critical  |  ........................................................36%  |     |     |     |
| --- | --------------------------------------------------------- | ------------------------------------------------------------- | --- | --- | --- |
|     |                                                           |  ....................................................40%      | 20% |     |     |
vulnerabilities
We rely on third-party tools to manage dependencies and   ........................................................36%  Yes
vulnerabilities  ...........................................................32%
No
47%
Don’t know
|     | We rely on automation to minimize inputs and reduce the   |  ..........................................................33%  |     |     |     |
| --- | --------------------------------------------------------- | --------------------------------------------------------------- | --- | --- | --- |
 .....................................................39%
attack surface
|     | We accept signed components and verify signatures   |  ...........................................................32%  | 33% |     |     |
| --- | --------------------------------------------------- | ---------------------------------------------------------------- | --- | --- | --- |
 ...............................................................27%
before deployment
 ...........................................................32%
We require administrator access for build processes and tools
 ...............................................................27%
Data: Dark Reading survey of 242 cybersecurity and IT professionals,
|     | We verify code components and build binaries from source code  |  ..............................................................28%  | June 2023  |     |     |
| --- | -------------------------------------------------------------- | ------------------------------------------------------------------- | ---------- | --- | --- |
before importing  ...................................................................24%
 ................................................................26%
We require all code to be reviewed by at least one other person ........................................................................................N/A
|     | We verify the changelog and commit history for the code  |  ................................................................26%  |     |     |     |
| --- | -------------------------------------------------------- | --------------------------------------------------------------------- | --- | --- | --- |
component and project before importing  ..............................................................28%
|     | For application builds, we execute the steps in ephemeral, isolated,  |  .................................................................25%  |     |     |     |
| --- | --------------------------------------------------------------------- | ---------------------------------------------------------------------- | --- | --- | --- |
or hermetically sealed environments  .................................................................25%
 .....................................................................20%
We are currently defining and developing our process ........................................................................................N/A
 ...........................................................................15%
|     | We only accept commits signed with a developer’s GPG key  .................................................................................9% |     |     |     |     |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------- | --- | --- | --- | --- |
 ...........................................................................14%
We verify provenance attestation of source code
........................................................................................N/A
Note: Multiple responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022
| Dark Reading Reports |     |     |     | August 2023  | 16  |
| -------------------- | --- | --- | --- | ------------ | --- |

The State of Supply Chain Threats
Table of Contents
Figure 10.
Software Bills of Materials
Please tell us how strongly you agree or disagree with the following statements about the software bill of
materials.
Neither
|     | Strongly  | Somewhat  |     | Somewhat  | Strongly  |     |     |
| --- | --------- | --------- | --- | --------- | --------- | --- | --- |
  agree nor
|     | agree      | agree      |     | disagree  | disagree  |     |     |
| --- | ---------- | ---------- | --- | --------- | --------- | --- | --- |
disagree
My organization maintains a software bill of materials
|     | 16% | 34% | 33% |   9% |   8% |     |     |
| --- | --- | --- | --- | ---- | ---- | --- | --- |
(SBOM) repository
I believe my organization will increase the use of SBOMs
|     | 18% | 30% | 41% |   8%  |   3% |     |     |
| --- | --- | --- | --- | ----- | ---- | --- | --- |
in the next 12 months
My organization uses the SBOM for vulnerability
|     | 13% | 28% | 37% | 12% | 10% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
management
My organization regularly requests SBOMs from vendors
|     | 12% | 29% | 34% | 15% | 10% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
and suppliers
My organization creates complete SBOMs for all software
|     | 14% | 22% | 40% | 13% | 11% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
we build
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023
Figure 11.
Build Practices to Prevent Software Supply Chain Attacks
How difficult is it to implement the following build practices and methods for preventing, mitigating, and/or
remediating software supply chain security attacks?
|     | 1 - Not    |     |     |     | 5 -        |     |     |
| --- | ---------- | --- | --- | --- | ---------- | --- | --- |
|     | difficult  | 2   | 3   | 4   | Extremely  |     |     |
|     | at all     |     |     |     | difficult  |     |     |
Using a hermetic build with all inputs declared with
|     | 2%  | 10% | 45% | 27% | 16% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
immutable references
Making provenance information (when/where/how the
|     | 3%  | 19% | 46% | 19% | 13% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
software was produced) available
All build steps must be run on a build service — not locally on
|     | 8%  | 14% | 51% | 20% |   7% |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
a developer’s workstation
Re-running builds with the same input artifacts must result in
|     | 6%  | 15% | 52% | 19% |   8% |     |     |
| --- | --- | --- | --- | --- | ---- | --- | --- |
bit-by-bit identical output
Running builds in an ephemeral environment, such as a
|     | 6%  | 23% | 47% | 14% | 10% |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- |
container or virtual machine, or in an isolated environment
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023
| Dark Reading Reports |     |     |     |     |     | August 2023  | 17  |
| -------------------- | --- | --- | --- | --- | --- | ------------ | --- |

The State of Supply Chain Threats
Table of Contents
Figure 12.
|     | Software Supply Chain Statements  |     |     |     |     |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Please tell us how strongly you agree or disagree with the following statements about the software
supply chain.
Neither
|     |     |     | Strongly  | Somewhat  |            | Somewhat  | Strongly  |     |     |
| --- | --- | --- | --------- | --------- | ---------- | --------- | --------- | --- | --- |
|     |     |     |           |           | agree nor  |           |           |     |     |
|     |     |     | agree     | agree     |            | disagree  | disagree  |     |     |
disagree
My organization will be able to detect and respond to a
|     |     |     | 18% | 46% | 27% |   8% |   1% |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- |
software supply chain compromise
“Shifting left” is necessary to secure the software
|     |     |     | 20% | 35% | 40% |   4% |   1% |     |     |
| --- | --- | --- | --- | --- | --- | ---- | ---- | --- | --- |
supply chain
I believe our architects and developers have the
|     | necessary knowledge and expertise to ensure a secure  |     | 23% | 30% | 31% | 13% | 3%  |     |     |
| --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
software supply chain
My organization has a way to detect software tampering
|     |     |     | 19% | 32% | 31% | 12% | 6%  |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
across the software supply chain
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023
Figure 13.
Effect of Recent Attacks on Organizations’ Approach to Supply Chain Security
How have attacks against trusted third-party software — such as Microsoft Exchange, Kaseya, and
Accellion — changed your organization’s approach to supply chain security?
10% 7%
We are making major changes to
|     |     | 17% | 6%  | 21% | address supply chain threats from  |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
third-party suppliers and partners
10%
We have made a few changes to
address supply chain threats from
|     |     | 22% |     |     | third-party suppliers and partners  |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- |
We have not made any changes,
but we plan to do so this year
24%
|     |     | 39% |     |     | We have not made any changes,  |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
and we have no plans to look at
|     |     |     |     | 44% | supply chain this year |     |     |     |     |
| --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
Don’t know
|     | 2023 |     | 2022 |     |     |     |     |     |     |
| --- | ---- | --- | ---- | --- | --- | --- | --- | --- | --- |
Data: Dark Reading survey of 242 cybersecurity and IT professionals in
June 2023 and 115 in June 2022
| Dark Reading Reports |     |     |     |     |     |     |     | August 2023  | 18  |
| -------------------- | --- | --- | --- | --- | --- | --- | --- | ------------ | --- |

The State of Supply Chain Threats
Table of Contents
Figure 14.
Minimizing Third-Party Risk
Thinking about supplier risk, which of the following do you do to establish or validate trust in your suppliers and minimize third-party risk? 2023 2022
............................................51%
We stipulate security standards that suppliers must adhere to as part of the contract .......................................55%
We regularly monitor and assess suppliers’ security practices .................................................44%
.......................................................37%
We ask suppliers to complete self-assessments describing their security controls .....................................................39%
............................................50%
Our suppliers have to submit independent audits or assessments indicating they meet security
...........................................................32%
requirements .....................................................39%
We generate our own supply chain information about our security processes and provide ........................................................................18%
them to our partners
..........................................................................16%
.....................................................................20%
We request point-in time assessments to understand the supplier’s security posture ..............................................................29%
........................................................35%
We require continuous validation to ensure suppliers have the necessary security controls ..........................................................33%
..............................................................29%
We verify the results of the supplier’s risk assessment ...................................................................23%
.................................................................................9%
We currently do not validate trust in suppliers or do anything to minimize third-party risk ...................................................................................6%
Note: Multiple responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022
Dark Reading Reports August 2023 19

The State of Supply Chain Threats
Table of Contents
Figure 15.
Types of Information for Supply Chain Assessment
When you ask for a supply chain assessment, what types of information are you looking for? 2023 2022
............................68%
Vulnerability management information ...................................61%
...................................60%
Data security controls being used ...............................................47%
.................................................44%
Documenting the design and testing process ............................................50%
....................................................41%
Asset inventory and user management information ........................................54%
List of vulnerable packages ......................................................38%
....................................................40%
........................................................35%
Supply chain levels for software artifacts (SLSA) ................................................45%
.............................................................31%
Description of process flows ...........................................................32%
..................................................................................7%
Other .......................................................................................2%
Note: Multiple responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022
Figure 16.
Securing the Supply Chain
What security controls and processes do you rely on to secure the supply chain? 2023 2022
We use multifactor authentication to secure accounts ........................74%
.................................62%
We require using least-privilege access control ......................................57%
.............................................48%
We require data to be encrypted ........................................54%
............................................51%
We segment the network to prevent lateral movement ............................................49%
......................................................38%
................................................45%
We rely on zero trust to manage authentication and access control .....................................................39%
........................................................35%
We conduct penetration testing engagements involving our suppliers ..............................................................29%
.........................................................34%
We require vulnerability scanning for our suppliers’ systems .........................................................34%
.........................................................34%
We are automating as much as possible and moving away from manual processes ......................................................38%
....................................................................22%
We rely on code analysis, including binary analysis .............................................................30%
......................................................................................4%
We currently do not have any security controls or processes to secure the supply chain ......................................................................................3%
Note: Multiple responses allowed
Data: Dark Reading survey of 242 cybersecurity and IT professionals in June 2023 and 115 in June 2022
Dark Reading Reports August 2023 20

The State of Supply Chain Threats
Table of Contents
Figure 17.
Supply Chain Attack
Has your organization experienced any kind of supply chain attacks over the past year?
6% 11% 9%
16% Yes, we have experienced
many supply chain attacks
18%
Yes, we have experienced
some such attacks
No, we have not experienced
32%
such attacks
Don’t know
48%
Data: Dark Reading survey of 242 cybersecurity and
60% IT professionals in June 2023 and 115 in June 2022
2023 2022
Figure 18.
Types of Attacks
Which types of supply chain attacks did your organization experience over the past year?
Attackers targeted my organization after compromising a
..................................................43%
third-party partner
Attackers exploited a software vulnerability in a component ....................................................41%
used by an application
An attack on our supplier disrupted our business processes .....................................................39%
Our developers accidentally downloaded malicious
.........................................................34%
components from npm, PyPI, Maven, or other code registries
Attackers exploited vulnerabilities in frameworks and other ...............................................................27%
developer tools used to create applications
There was a backdoored component in hardware devices .....................................................................20%
used by my organization
Attackers stole secrets, such as credentials and tokens, from
.....................................................................20%
one source and used them to gain unauthorized access to my
organization’s systems
Other ..................................................................................7%
Note: Multiple responses allowed
Base: 58 respondents who have experienced supply chain attacks
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023
Dark Reading Reports August 2023 21

The State of Supply Chain Threats
Table of Contents
Figure 19. Figure 21.
Current Protection Against Software Supply Chain Threats Respondent Region of Residence
Does your organization’s current security program cover software supply In what region do you live?
chain threats?
3%3%
3% 10% Our security program covers
software supply chain threats 4%
North America
4%
28% Our security program covers
East Asia or Pacific
supply chain threats but 6%
doesn’t explicitly specify Latin America, South America,
16%
software supply chain or Caraibbean (including
Mexico)
No, our security program does 11%
Europe or Central Asia
not cover any kind of supply
chain threats 69% South Asia
Middle East or North Africa
We do not have a security
program Sub-Saharan Africa
43%
Don’t know
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023 Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023
Figure 20.
Insurance Partner for Reducing Third-Party Risk
Do you consider your insurance carrier an effective partner in reducing third-party risk?
26%
26%
37% Yes
No
44%
Don’t know
30% Data: Dark Reading survey of 242 cybersecurity and
37% IT professionals in June 2023 and 115 in June 2022
2023 2022
Dark Reading Reports August 2023 22

The State of Supply Chain Threats
Table of Contents
Figure 22. Figure 23.
Respondent Job Title Respondent Company Size
Which of the following best describes your job title? How many employees are in your company in total?
IT executive (CIO, CTO)
Cybersecurity executive (CSO/CISO)
22%
|     | 2%  |     |     | Chief privacy officer  |     | 27% |     |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
7% 5,000 or more
|     |     | 13% |     | VP of IT/VP of security  |     |     |     |     |
| --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- |
1,000 to 4,999
|     | 7%  |     |     | IT director/head  |     |     |     |     |
| --- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
100 to 999
|     |     | 9%  |     | Cybersecurity director/head  |     |     |     |     |
| --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- |
6% Fewer than 100
|     |     |     | 1%  | IT manager  |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
3%
|     |     |     | 3%  | Cybersecurity manager  |     |     |     |     |
| --- | --- | --- | --- | ---------------------- | --- | --- | --- | --- |
| 4%  |     |     |     |                        |     | 19% |     |     |
IT staff  32%
8%
Cybersecurity staff
10%
|     |     | 5%  |     | Engineer                |     |     |     |     |
| --- | --- | --- | --- | ----------------------- | --- | --- | --- | --- |
|     | 7%  | 7%  |     | Software/Web developer  |     |     |     |     |
Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023
8%
Network/system administrator
Corporate executive (CEO/President/COO)
Architect
Data: Dark Reading survey of 242 cybersecurity
and IT professionals, June 2023 Other
Figure 24.
Respondent Industry
What is your organization’s primary industry?
|     |     |     | 13% | 14% | Computer or technology manufacturer/tech vendor  | Communications carrier/service provider  |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------ | ---------------------------------------- | --- | --- |
3%
|     |     |     |     |     | Banking/financial services/VC/accounting  | Insurance/HMOs  |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------- | --------------- | --- | --- |
3%
|     |     |     |     |     | Consulting/business services                  | Aerospace                              |     |     |
| --- | --- | --- | --- | --- | --------------------------------------------- | -------------------------------------- | --- | --- |
|     |     | 3%  |     | 11% |                                               |                                        |     |     |
|     |     |     |     |     | Healthcare/pharmaceutical/biotech/biomedical  | Construction/architecture/engineering  |     |     |
3%
|     |     |     |     |     | Government  | Media/marketing/advertising  |     |     |
| --- | --- | --- | --- | --- | ----------- | ---------------------------- | --- | --- |
3%
|     |     |     |     | 9%  | Manufacturing, industrial, process (noncomputer)  | Utilities  |     |     |
| --- | --- | --- | --- | --- | ------------------------------------------------- | ---------- | --- | --- |
3%
|     |     |     |     |     | Solutions provider/value-added reseller (VAR)  | Wholesale/trade/distribution/retail  |     |     |
| --- | --- | --- | --- | --- | ---------------------------------------------- | ------------------------------------ | --- | --- |
3%
|     |     |     | 5%  |     | Education  | Other  |     |     |
| --- | --- | --- | --- | --- | ---------- | ------ | --- | --- |
8%
6%
|                      |     |     | 6%  | 7%  | Data: Dark Reading survey of 242 cybersecurity and IT professionals, June 2023 |     |              |     |
| -------------------- | --- | --- | --- | --- | ------------------------------------------------------------------------------ | --- | ------------ | --- |
| Dark Reading Reports |     |     |     |     |                                                                                |     | August 2023  | 23  |