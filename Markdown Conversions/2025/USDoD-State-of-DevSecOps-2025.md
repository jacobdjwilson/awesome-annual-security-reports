# The State of DevSecOps

## Table of Contents
- [Purpose](#purpose)
- [Goals](#goals)
- [Conversion Instructions](#conversion-instructions)
- [Content](#content)
- [Images](#images)
- [Table of Contents](#table-of-contents)
- [Footnotes and References](#footnotes-and-references)
- [Verification and Quality Assurance](#verification-and-quality-assurance)
- [Report Content Below](#report-content-below)
- [1  Introduction: Studying the Current State of DevSecOps to Chart the Way Forward](#1-introduction-studying-the-current-state-of-devsecops-to-chart-the-way-forward)
  - [1.1  DevSecOps for Modernization and DoD Mission Success](#11-devsecops-for-modernization-and-dod-mission-success)
  - [1.2  The Need for a State of DevSecOps Study](#12-the-need-for-a-state-of-devsecops-study)
  - [1.3  Our Approach to this Study](#13-our-approach-to-this-study)
  - [1.4  A Reader’s Guide to this Report](#14-a-readers-guide-to-this-report)
- [2  Celebrating Successes So Far](#2-celebrating-successes-so-far)
- [3  Software Factories Constitute the Digital Arsenal for Modern Warfare](#3-software-factories-constitute-the-digital-arsenal-for-modern-warfare)
  - [3.1  Understanding Software Factories](#31-understanding-software-factories)
  - [3.2  Support, Not Control](#32-support-not-control)
  - [3.3  Understanding DoD’s DevSecOps Culture](#33-understanding-dods-devsecops-culture)
- [4  Optimizing the Software Factory Ecosystem Enables Enterprise Software Modernization](#4-optimizing-the-software-factory-ecosystem-enables-enterprise-software-modernization)
  - [4.1  Inventorying the DevSecOps Software Factory Portfolio](#41-inventorying-the-devsecops-software-factory-portfolio)
  - [4.2  Improving and Automating Inventory Data Collection](#42-improving-and-automating-inventory-data-collection)
  - [4.3  Managing the Software Factory Portfolio](#43-managing-the-software-factory-portfolio)
  - [4.4  Managing the Software Factory Workforce](#44-managing-the-software-factory-workforce)
  - [4.5  Acquiring Software Factory Services](#45-acquiring-software-factory-services)
  - [4.6  Improving Financial Transparency](#46-improving-financial-transparency)
  - [4.7  Baseline and Moving Forward](#47-baseline-and-moving-forward)
- [5  DevSecOps Enables a Cybersecurity Transformation from Point-in-Time Risk Assessment to Continuous Authority to Operate](#5-devsecops-enables-a-cybersecurity-transformation-from-point-in-time-risk-assessment-to-continuous-authority-to-operate)
  - [5.1  The Importance of cATO](#51-the-importance-of-cato)
  - [5.2  The cATO Process](#52-the-cato-process)
  - [5.3  The cATO Assessment Method](#53-the-cato-assessment-method)
  - [5.4  Barriers and Challenges to cATO](#54-barriers-and-challenges-to-cato)
  - [5.5  Reciprocity Challenges](#55-reciprocity-challenges)
  - [5.6  Baseline and Moving Forward](#56-baseline-and-moving-forward)
- [6  Policy and Guidance Enables Change](#6-policy-and-guidance-enables-change)
  - [6.1  Scaling Grass Roots Innovation](#61-scaling-grass-roots-innovation)
  - [6.2  Policy at the Speed of Relevance](#62-policy-at-the-speed-of-relevance)
  - [6.3  Culture Interprets Policy](#63-culture-interprets-policy)
  - [6.4  Understanding and Aligning Culture](#64-understanding-and-aligning-culture)
  - [6.5  Integrating Cultures to Achieve Transformational Value](#65-integrating-cultures-to-achieve-transformational-value)
  - [6.6  Baseline and Moving Forward](#66-baseline-and-moving-forward)
- [7  Forging a Mission-Ready DevSecOps Workforce](#7-forging-a-mission-ready-devsecops-workforce)
  - [7.1  Current State of the DevSecOps Workforce: Empirical Evidence](#71-current-state-of-the-devsecops-workforce-empirical-evidence)
  - [7.2  Strategic Workforce Modernization Initiatives](#72-strategic-workforce-modernization-initiatives)
  - [7.3  Baseline and Moving Forward](#73-baseline-and-moving-forward)
- [8  A Playbook for Moving Forward](#8-a-playbook-for-moving-forward)
  - [8.1  Getting Insight Into Performance Across the Ecosystem](#81-getting-insight-into-performance-across-the-ecosystem)
  - [8.2  Using Data Every Day](#82-using-data-every-day)
  - [8.3  Conclusion](#83-conclusion)
- [9  Works Cited and Further Reading](#9-works-cited-and-further-reading)
- [Glossary](#glossary)

---
# Report Content Below
The State of 
DevSecOps
March 2025
Distribution Statement A 
Approved for public release: 
distribution is unlimited.
 
                                   CLEARED 
For Open Publication 
 
 
Department of Defense 
OFFICE OF PREPUBLICATION AND SECURITY REVIEW 
 
Apr 14, 2025
The State of DevSecOps within the Department of Defense | 2
Names, products, and services referenced within this document may be the trade names, 
trademarks, or service marks of their respective owners. References to commercial vendors 
and their products or services are provided strictly as a convenience to our readers, and don’t 
constitute or imply endorsement by the Department of any non-Federal entity, event, product, 
service, or enterprise.
The State of DevSecOps within the Department of Defense | 3
Executive Summary
Since the release of the DIB SWAP report in 2019, _Software Is Never Done: Refactoring the 
Acquisition Code for Competitive Advantage_, the Department of Defense (DoD) has focused on 
transforming our software development and acquisition practices.  The core of this transformation 
is DevSecOps, a process that breaks down silos, inculcates security, and rapidly delivers software 
into production following the best practices of modern technology companies.  Over the past 
5 years, DoD has made significant strides in adopting DevSecOps practices.  There are over 50 
software factories using DevSecOps to deliver code into production, learning how to incorporate 
these practices into the high-stakes DoD environment and providing templates and patterns for 
generalized transition.       
Pockets of excellence have emerged across DoD in which DevSecOps practices have been 
successfully implemented, resulting in faster deployment cycles, enhanced security, higher 
software quality, greater operational efficiency, and improved end user value.  This is why the Office 
of the DoD Chief Information Officer (CIO) is sponsoring this first “State of DoD DevSecOps Report” 
– to examine how far we have come, celebrate the wins, and gain insight to transition the entire
Department to modern software practices.
DoD views DevSecOps as a critical enabler to protecting warfighters by driving modernization that 
adapts to future challenges and enhances overall mission success. DoD operates in a high-stakes 
environment where security, efficiency, and speed are paramount, and DevSecOps offers a pathway 
to achieve these objectives simultaneously. We know this because industry has demonstrated 
the value of rapid software delivery into production.  Leading technology companies, commercial 
companies we hold in high regard, and even our adversaries are implementing this approach. 
DevSecOps enables DoD to continue to deliver advanced warfighting capabilities, such as Project 
Overmatch, the F-16, the F-35, and a broad range of other key weapons systems.     
This study focused on the current state of DoD practices.  We used quantitative metrics, although 
at this point in our journey, it was necessary to augment them with qualitative information via user 
surveys.  Overall, the Department found that DevSecOps is a powerful tool for accelerating software 
delivery.  When fully implemented, it changes the paradigm for delivering mission capability into 
warfighter hands at a speed that provides them with an asymmetric advantage.  
DevSecOps is a process change that must be introduced with leadership commitment. To be 
successful it must overcome bureaucratic inertia aligned to traditional approaches that are 
intertwined across all facets of our delivery process.  Figure 0-1 shows the DevSecOps infinity loop 
surrounded by traditional processes with existing equities that must be satisfied to deliver software 
into operations.
![Image description: SOFTWARE FACTORY/PRODUCTION BOUNDARY]
The State of DevSecOps within the Department of Defense | 4
Existing Cyber practices, Test and Evaluation practices, Acquisition, and others including 
Requirements, AI, and Accounting all need to be realigned towards rapid, incremental delivery and 
operationalization of minimal mission capability. All of those authorities have proven capable of an 
agile transformation.   
Over the course of the study, we interviewed more than 75 leaders and practitioners across DoD, 
representing 19 different software organizations of all types and test organizations representing 
Cyber, Developmental Test, and Operational Test. These leaders and practitioners demonstrated an 
impressive passion for the work and dedication to the mission. We encouraged them to share both 
their wins and opportunities for improvement. We used the insights we developed to present an 
approach for measuring and monitoring the progress of our transformation efforts and the health of 
our DevSecOps ecosystem as we move to the future.  The following themes are expanded in the full 
report: 
- DevSecOps Achieves Success Amid Rapid Change:  DoD has made significant
progress in adopting DevSecOps principles resulting in a more agile, resilient, and lethal
force. DevSecOps validated the path forward by improving implementations, enhancing
interoperability, and accelerating deployments.
- Software Factories Are Our Digital Arsenal: Software factories have revolutionized
software delivery by applying continuous integration and continuous deployment workflows,
and it’s time to scale and formalize their capabilities to modernize DoD’s IT and weapons
systems environment. In DoD, a software factory is defined as a collection of people, tools,
and processes that enables teams to continuously deliver value by deploying software to
meet the needs of a specific community of end users. It leverages automation to replace
manual processes.
- Software Factories Enable Modernization: Expanding and optimizing the software factory
ecosystem accelerates enterprise modernization.  Software factories face challenges with
consistent funding and business models that limit large scale expansion. DoD is collecting
data, including costs and productivity, to inform future investments in people, processes,
and technology and to drive more effective modernization.
- DevSecOps Enables Continuous Authority to Operate: DevSecOps enables a
cybersecurity transformation from a point-in-time risk assessment to a continuous
authorization to operate (cATO).  cATO is a significant shift in DoD cybersecurity practices
that incorporates real-time assessment, Zero Trust principles, and DevSecOps to secure our
supply chain against emerging threats and improve our overall cybersecurity posture.
- Policy and Guidance Enable Change: Policy and guidance need to keep pace with the
speed of software delivery enabled by DevSecOps and associated cultural changes to adopt
new software. DoD is applying an agile mindset to drive policy based on grassroots success
with DevSecOps.  Examples of grassroots activities are the Software Factory Coalition and
the DoD DevSecOps Community of Practice.  Understanding cultural context enables DoD to
deliberately align policy and guidance to effective practices.
- Success Rests on Forging a Mission-Ready DevSecOps Workforce: A skilled and
motivated workforce is essential for DevSecOps, and DoD is making progress in building a
robust workforce through initiatives like the Cyber Workforce Strategy Implementation Plan.
Programs have reported that delivering capability into DoD mission is a significant incentive
to drive recruiting and retention and can offset challenges of financial compensation.
Effective leadership and a culture that prioritizes innovation, collaboration, and continuous
learning are essential for fostering a workforce that can deliver DevSecOps capabilities at
scale.
- The Path Forward Relies on Data and Effective Measurement: To ensure DevSecOps
continues to enable mission value, DoD needs to measure progress against objectives,
using data to inform decision-making, drive improvement, and remove barriers to
progress. A combination of quantitative data, rigorous methodology, strategic thinking, and
understanding of organizational goals is essential for effective decision-making.
The Office of the DoD CIO welcomes your feedback to improve the state of DevSecOps across the 
Department. 
The State of DevSecOps within the Department of Defense | 5
## Table of Contents
- [1  Introduction: Studying the Current State of DevSecOps to Chart the Way Forward](#1-introduction-studying-the-current-state-of-devsecops-to-chart-the-way-forward)
- [1.1  DevSecOps for Modernization and DoD Mission Success](#11-devsecops-for-modernization-and-dod-mission-success)
- [1.2  The Need for a State of DevSecOps Study](#12-the-need-for-a-state-of-devsecops-study)
- [1.3  Our Approach to this Study](#13-our-approach-to-this-study)
- [1.4  A Reader’s Guide to this Report](#14-a-readers-guide-to-this-report)
- [2  Celebrating Successes So Far](#2-celebrating-successes-so-far)
- [3  Software Factories Constitute the Digital Arsenal for Modern Warfare](#3-software-factories-constitute-the-digital-arsenal-for-modern-warfare)
- [3.2  Support, Not Control](#32-support-not-control)
- [3.3  Understanding DoD’s DevSecOps Culture](#33-understanding-dods-devsecops-culture)
- [4  Optimizing the Software Factory Ecosystem Enables Enterprise Software Modernization](#4-optimizing-the-software-factory-ecosystem-enables-enterprise-software-modernization)
- [4.1  Inventorying the DevSecOps Software Factory Portfolio](#41-inventorying-the-devsecops-software-factory-portfolio)
- [4.2  Improving and Automating Inventory Data Collection](#42-improving-and-automating-inventory-data-collection)
- [4.3  Managing the Software Factory Portfolio](#43-managing-the-software-factory-portfolio)
- [4.4  Managing the Software Factory Workforce](#44-managing-the-software-factory-workforce)
- [4.5  Acquiring Software Factory Services](#45-acquiring-software-factory-services)
- [4.6  Improving Financial Transparency](#46-improving-financial-transparency)
- [4.7  Baseline and Moving Forward](#47-baseline-and-moving-forward)
- [5  DevSecOps Enables a Cybersecurity Transformation from Point-in-Time Risk Assessment to Continuous Authority to Operate](#5-devsecops-enables-a-cybersecurity-transformation-from-point-in-time-risk-assessment-to-continuous-authority-to-operate)
- [5.1  The Importance of cATO](#51-the-importance-of-cato)
- [5.2  The cATO Process](#52-the-cato-process)
- [5.3  The cATO Assessment Method](#53-the-cato-assessment-method)
- [5.4  Barriers and Challenges to cATO](#54-barriers-and-challenges-to-cato)
- [5.5  Reciprocity Challenges](#55-reciprocity-challenges)
- [5.6  Baseline and Moving Forward](#56-baseline-and-moving-forward)
- [6  Policy and Guidance Enables Change](#6-policy-and-guidance-enables-change)
- [6.1  Scaling Grass Roots Innovation](#61-scaling-grass-roots-innovation)
- [6.2  Policy at the Speed of Relevance](#62-policy-at-the-speed-of-relevance)
- [6.3  Culture Interprets Policy](#63-culture-interprets-policy)
- [6.4  Understanding and Aligning Culture](#64-understanding-and-aligning-culture)
- [6.5  Integrating Cultures to Achieve Transformational Value](#65-integrating-cultures-to-achieve-transformational-value)
- [6.6  Baseline and Moving Forward](#66-baseline-and-moving-forward)
- [7  Forging a Mission-Ready DevSecOps Workforce](#7-forging-a-mission-ready-devsecops-workforce)
- [7.1  Current State of the DevSecOps Workforce: Empirical Evidence](#71-current-state-of-the-devsecops-workforce-empirical-evidence)
- [7.2  Strategic Workforce Modernization Initiatives](#72-strategic-workforce-modernization-initiatives)
- [7.3  Baseline and Moving Forward](#73-baseline-and-moving-forward)
- [8  A Playbook for Moving Forward](#8-a-playbook-for-moving-forward)
- [8.1  Getting Insight Into Performance Across the Ecosystem](#81-getting-insight-into-performance-across-the-ecosystem)
- [8.2  Using Data Every Day](#82-using-data-every-day)
- [8.3  Conclusion](#83-conclusion)
- [9  Works Cited and Further Reading](#9-works-cited-and-further-reading)
- [Glossary](#glossary)

The State of DevSecOps within the Department of Defense | 6
# 1  Introduction: Studying the Current State of 
DevSecOps to Chart the Way Forward
DevSecOps is a cultural and technical movement aimed at fostering collaboration between 
development, security, and operations teams to build, test, and release software more rapidly and 
reliably. DevSecOps integrates critical security measures from the start, ensuring they’re baked into 
the development process, not tacked on at the end. The newly revised “DoD Enterprise DevSecOps 
Fundamentals” states the following:   
>DevSecOps is a combination of software engineering methodologies, practices, and tools 
that unifies software development (Dev), security (Sec), and operations (Ops). It emphasizes 
collaboration across these disciplines, along with automation and continuous monitoring to support 
the delivery of secure, high-quality software. DevSecOps integrates security tools and practices into 
the development pipeline, emphasizes the automation of processes, and fosters a culture of shared 
responsibility for performance, security, and operational integrity throughout the entire software life 
cycle, from development to deployment and beyond.[^1]
# 1.1  DevSecOps for Modernization and DoD Mission Success
DoD operates in a high-stakes environment where security, efficiency, and speed are paramount. 
DevSecOps offers a pathway to achieve these objectives simultaneously. DoD has its own specific 
needs and context, which don’t always overlap and align with commercial software efforts.    
The landscape of DevSecOps within DoD is undergoing significant transformation. This 
transformation extends beyond tools and technologies, encompassing culture, skillsets, processes, 
funding mechanisms, and inter-organizational dynamics. DoD has actively embraced DevSecOps 
by adopting a collaborative and agile approach to software development, thereby enhancing its 
software development practices.     
DoD has recognized that DevSecOps and the transformation of software development is crucial 
for mission success. We know this because industry has demonstrated the value of rapid software 
delivery into production.  Leading technology companies, commercial companies we hold in high 
regard, and even our adversaries are implementing this approach. DevSecOps enables DoD to 
continue to deliver advanced warfighting capabilities, such as Project Overmatch, the F-16, the 
F-35, and a broad range of other key weapons systems.  
The conflicts in Ukraine demonstrate how quickly modern warfare is changing. The war started as 
cyber warfare, then moved to kinetic missile attacks on critical command and control as well as 
data centers, then to trench warfare, then to drone warfare, and now to electromagnetic warfare. 
All of these changes are happening in the modern battlespace, where the traditionally separate 
domains of air, land, sea, space, and cyberspace are merged in ways not previously imagined.     
We need to make sure that DoD, as a warfighting force, has the IT resiliency and IT agility to adapt 
to those changes—in our weapons systems, command and control, intelligence, and battlefield 
prepping—faster than our adversaries. Since software increasingly enables almost all of these 
capabilities, DoD must not only continue implementing DevSecOps, recognizing and addressing the 
challenges and barriers, but also accelerate progress on this path.
# 1.2  The Need for a State of DevSecOps Study
The state of DevSecOps within DoD is evolving rapidly as we recognize its critical importance to our 
mission readiness and security posture. DoD has made significant strides in adopting DevSecOps 
practices, investing in recruiting and training, creating new work roles within the cyber and software 
communities, and integrating security into every stage of our software development life cycle. This 
transformation is driven by a need to deliver secure, resilient, and adaptable solutions in response 

[^1]: DoD Chief Information Officer, “DoD Enterprise DevSecOps Fundamentals,” Version 2, DoD October 23, 2024. https://
dodcio.defense.gov/Portals/0/Documents/Library/DoD%20Enterprise%20DevSecOps%20Fundamentals%20v2.5.pdf.
The State of DevSecOps within the Department of Defense | 7
to an increasingly complex threat landscape.    
The Defense Innovation Board report, “Software Acquisition and Practices (SWAP) Study,” served 
as a critical trigger for this transformation, leading to the development and implementation of 
key policies and initiatives. Central to these efforts is DoD Instruction 5000.87, “Operation of the 
Software Acquisition Pathway,” which provides a comprehensive framework for agile, iterative 
software acquisition. Additionally, platforms and services such as Platform One, Iron Bank, and Big 
Bang have been instrumental in validating, standardizing, and securing our DevSecOps practices.   
The Office of the DoD CIO has also provided foundational elements like DoD DevSecOps Reference 
Designs, which offer guidelines for integrating security into development, leveraging cloud-native 
technologies, and automating workflows. Other key initiatives include the DoD Cloud Computing 
Security Requirements Guide, the Container Platform Security Technical Implementation Guide, and 
the Cloud Native Access Point, which ensures secure access to cloud resources.    
Pockets of excellence have emerged across various DoD organizations in which DevSecOps 
practices have been successfully implemented, resulting in faster deployment cycles, enhanced 
security, and greater operational efficiency. However, this journey isn’t without its challenges. DoD 
is actively addressing cultural resistance, skill gaps, and the complexities of integrating modern 
DevSecOps practices with our legacy systems.    
DoD is committed to fostering a collaborative culture that prioritizes security and continuous 
improvement. By leveraging lessons learned from the private sector and investing in training and 
automated tools, we are building a robust DevSecOps ecosystem that supports our strategic 
objectives. While there is still work to be done, the progress we have made thus far is promising, 
and we are well on our way to achieving a fully integrated, agile, and secure set of DevSecOps 
environments across DoD.    
The Office of the DoD CIO is sponsoring this first “State of DoD DevSecOps Report” to examine how 
far we’ve come, celebrate the wins, and gain insight to help plan our next steps.     
# 1.3  Our Approach to this Study
Our approach to assessing the state of DevSecOps focused on high-priority aspects that provide 
insight into the overall transformation underway at DoD. Managing the portfolio of DevSecOps 
capabilities is not centralized, rather it is distributed across DoD Components. The state of portfolio 
management provides insight into the maturity and distribution of DevSecOps capabilities. 
Coordination across these distributed activities is the responsibility of the Software Modernization 
Senior Steering Group (SSG).   
Over the past four years, both policy and general and detailed technical guidance have been 
published to move the software modernization forward. The impact and adoption of that policy and 
guidance provide insight into the overall state of DevSecOps and the effectiveness of advancing 
the transformation. Finally, the state of the DevSecOps workforce and culture provides insight 
into the ability of DoD to accelerate that transformation rate.  We developed these priorities in a 
collaborative, cross-DoD workshop and organized the study along three lines of effort: 
Portfolio Management
- How are DevSecOps activities aligned to mission and/or capability needs?
- How well do we understand the DevSecOps enterprise portfolio (people, process, and
technology) from a DoD or Military Department-level perspective?
Policy and Guidance
- What policy or guidance changes have enabled DoD software entities under Software
Modernization to improve the ability to deliver capabilities to the warfighter?
- What gaps or barriers exist in the current policies that prevent organizations from achieving
the goal of speeding up capability delivery to the warfighter?
The State of DevSecOps within the Department of Defense | 8
Workforce and Culture
- How conducive is the workforce and culture created by DoD and Military Departments to
achieving the goals of DevSecOps?
In this first State of DevSecOps study, we worked to establish an initial quantitative baseline of 
progress on our ongoing DevSecOps transformation, then we worked to augment the quantitative 
data with qualitative insights. We collected the data to characterize our baseline progress in the 
following ways:
- We sought data from DoD and the Military Department-level inventories, assessments, and
existing automated collection mechanisms.
- We met with practitioners a non-attribution basis to collect quantitative data about the
implementation of technical and team practices associated with characteristics of healthy
DevSecOps organizational cultures.
- We held workshops to map technical practices, processes, and implementations to related
policy and guidance issues to identify accelerators, barriers, and gaps.
- We observed reporting from and engaged with practitioners in multiple DoD DevSecOps and
software forums.
- We captured short success stories from members of the community that capture real
experiences of teams on our journey.
- We leveraged insights developed from extensive bodies of work of two Federally Funded
Research and Development Centers (FFRDC).
- We augmented these efforts with analysis of various DoD policy, guidance, strategies, and
implementation plans, many of which have been issued during the course of our activities.
Over the course of the study, we interviewed more than 75 leaders and practitioners across DoD, 
representing 19 different software organizations of all types and test organizations representing 
cyber, developmental, and operational test. These leaders and practitioners demonstrated an 
impressive passion for the work and dedication to the mission. That passion and dedication to 
the mission encouraged everyone we talked with to share both their wins and opportunities for 
improvement. We used the insights developed to present an approach for measuring and monitoring 
the progress of our transformation efforts and the health of our DevSecOps ecosystem as we move 
to the future.    
Describing the data strictly along these lines of effort independently misses important 
interdependencies. We can’t describe the culture and workforce independently of the mission and 
organizational structure. The effectiveness of policy and its implementation depends upon the 
workforce culture and the specific mission. Policy is always interpreted through the lens of culture. 
The existing portfolio and policies affect how the workforce is built.    
The Office of the DoD CIO welcomes your feedback on the ways in which you have used this report 
to understand and address ongoing DevSecOps challenges, and any other feedback or information 
that could improve the state of DevSecOps across DoD.
# 1.4  A Reader’s Guide to this Report
Here’s a quick navigation guide and section summary to help you get the most out of this report:
Section 2: We celebrate wins along the journey all across DoD – and there are many of them!  This 
section also features (with permission) the story of the MEPCOM Integrated Resource System 
modernization. It is an inspiring software modernization success story that touches on every aspect 
of our transformation: innovation, creativity, tools and technologies, culture, skillsets, processes, 
funding mechanisms, and inter-organizational dynamics.
Section 3: DoD’s software factory innovation ecosystem grew up organically. In this section, 
we set the stage by highlighting the evolution and entrepreneurial nature of DoD’s software 
factory ecosystem, the importance of effectively equipping our thriving Digital Arsenal, and the 
need to maintain its highly collaborative culture to accelerate the transition to modern software 
development practices. 
The State of DevSecOps within the Department of Defense | 9
Section 4: Acquisition program managers and enterprise IT leaders will gain new insights from 
important efforts underway to establish a clear enterprise inventory of DoD’s software factory and 
DevSecOps portfolio, and the complexities in the funding and business environments that drive the 
need for strategic governance to enable optimization of the software factory ecosystem.  
Section 5: Continuous ATO (cATO) represents a significant shift in the management of cybersecurity 
risk from point-in-time to continuous risk management. This section highlights ongoing efforts 
between DoD CIO and DoD Components to provide resources that support this transformation.
Section 6: Transformational leadership is required to help everyone “get to yes.” In this section, we 
discuss developing policy and guidance at all levels in a way that enables the cultural shift across 
DoD toward a DevSecOps mindset. 
Section 7: Software team leads, stop here! DoD is working on comprehensive strategic initiatives 
aimed at building a robust DevSecOps workforce. This section takes the pulse of leaders in software 
teams and provides updates on important strategic initiatives underway to address challenges in 
recruiting, retention, and workforce development.
Section 8: Pull this section out to build action plans. It offers goal-oriented guidance for collecting 
and using data to gain continuous insight into progress toward strategic objectives, to identify and 
understand barriers and challenges, and to adapt rapidly and responsibly to changes in our ever-
evolving landscape. We discuss data as a strategic asset and ways in which it can be captured to 
explicitly link DevSecOps organizations with mission outcomes.
Section 9: This handy reference section contains a list of all public sources cited and consulted.
Throughout this report, important information is highlighted in various ways:
- Key takeaways for each report section appear in blue sidebars at the beginning of each
section.
- Quotes from leadership and key quotes from the report text are presented in green sidebars.
- Success stories appear in sections in the body of the section in which they appear.
The State of DevSecOps within the Department of Defense | 10
# 2  Celebrating Successes So Far 
>Five years have passed since the Defense Innovation Board issued its SWAP 
report, and in that period, DoD has tallied numerous accomplishments and 
successes. The Office of the Secretary of Defense (OSD) has laid a solid foundation 
for DevSecOps development based on industry guidance, and many pockets of 
excellence have been established across various DoD organizations. These have 
included a combination of significant initiatives as well as smaller, fast-moving 
efforts, showing that it’s possible to implement DevSecOps and demonstrate how 
DoD as a whole should move forward.

There are many indications of progress. For instance, the Iron Bank container 
repository has experienced an explosion of new containers and now holds over 
1,200 hardened container images with approximately 400 commercial and 800 
open-source images. In addition, the repository has launched a new Core Image 
Program to help focus resources on maintaining the most critical and highest 
utilized images across its user base. The Military Department CIOs have issued 
continuing guidance and updates to implement these practices and accelerate 
adoption. Perhaps most importantly, however, many programs have adopted the 
Software Acquisition Pathway (SWP). The Office of the Under Secretary of Defense 
for Acquisition and Sustainment (OUSD(A&S)) has been collecting data on the 
growing number of programs adopting DoDI 5000.87. At present, approximately 
78 DoD acquisition programs have adopted the software acquisition pathway. 
Seventy-five percent of those programs are delivering software in less than six 
months.[^2]  
In its most recent Weapon Systems Annual Assessment, the Government 
Accountability Office (GAO) reported that 75 to 80 percent of the 40 Major Defense 
Acquisition Programs (MDAP) it monitors have adopted modern development 
practices, including Agile and DevSecOps.[^3] GAO found that almost half of those 
MDAPs deliver software capability in less than four months.  
DoD Components, Program Executive Offices, Programs of Record, and even the 
defense industrial base have taken the SWAP report’s guidance to heart and have 
begun to implement and use that guidance to deliver using modern practices. 
We’ve highlighted below a few Military Service-level efforts and an inspiring 
vignette from a program on its software modernization journey. Look for many more 
success stories in subsequent sections. 
We are moving quickly – this section captures only a small number of the stories 
and indicators of progress along DoD’s DevSecOps transformation journey. 

[^2]: Department of Defense. “Structuring Change to Last: An Update on Innovation at the Department 
of Defense.” U.S. Department of Defense. August 2024. https://media.defense.gov/2024/
Aug/07/2003519333/-1/-1/0/DoD-INNOVATION-FACT-SHEET-AUGUST-2024.PD
[^3]: Government Accountability Office. “Weapon Systems Annual Assessment: DoD Is Not Yet Well-
Positioned to Field Systems with Speed.” GAO-24-106831. Government Accountability Office. June 17, 
2024. https://www.gao.gov/products/gao-24-106831

>DoD has made 
substantial progress 
on our DevSecOps 
journey, and change 
is happening fast. 
A combination of significant 
strategic initiatives and 
smaller, fast-moving efforts 
continue to demonstrate 
successful DevSecOps 
implementations and point 
the way forward for the DoD.

The State of DevSecOps within the Department of Defense | 11
Throughout the remaining sections of this report, you’ll see additional 
success stories called out in highlighted sections below.  
>Success Story: Air Force Launches New Software Directorate
In July 2023,