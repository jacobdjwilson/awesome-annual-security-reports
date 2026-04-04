# 2021 State of DevSecOps

**Organization:** Checkmarx  
**Year:** 2021  
**Source:** Cyber Security Hub

## Table of Contents
- [Introduction](#introduction)
- [Methodology](#methodology)
- [Application Security Team Size](#application-security-team-size)
- [Measuring Success](#measuring-success)
- [Reporting to the CISO](#reporting-to-the-ciso)
- [Frustrations with Testing](#frustrations-with-testing)
- [Automation Strategies](#automation-strategies)
- [Consuming Security Results](#consuming-security-results)
- [Types of Security Testing](#types-of-security-testing)
- [Open Source Tooling](#open-source-tooling)
- [Desired Improvements](#desired-improvements)
- [Communication with Developers](#communication-with-developers)
- [Security Champions](#security-champions)
- [Security Awareness](#security-awareness)
- [Future Skills](#future-skills)
- [Speed vs. Quality](#speed-vs-quality)
- [Conclusion](#conclusion)
- [About Cyber Security Hub](#about-cyber-security-hub)

---

## Introduction
Today, DevOps teams are embracing new approaches of embedding application security testing (AST) into their development pipelines to truly achieve DevSecOps. Developer and security teams agree that a single vulnerability scan late in the software development life cycle (SDLC) is insufficient, can result in delayed software releases, and often becomes unnecessarily expensive. As with any type of security testing, discovering vulnerabilities late in the pipeline means it takes more time and effort to remediate them. Hence, it’s highly desirable to shift AST as far left as possible by integrating security into the tooling developers use.

However, DevSecOps is still in its early stages, as evidenced by our 2021 survey, which indicates that the security portion of DevSecOps is maturing in pieces. Part of the problem is budget, and part of it has to do with a talent shortage. Smaller companies especially lack the security expertise and tools larger companies have.

**Key findings from our 2021 survey:**
- Half of respondents plan to add more application security staff in the next year.
- 43% say their biggest frustration is security testing done late in the SDLC because it delays launches.
- Of all the application security types, API testing is the most popular among two-thirds of respondents.
- Two-thirds lack a security champion.

## Methodology
This report is based on a global online survey of application security professionals that took place during late May and June 2021. Sixty percent are located in EMEA, followed by APAC and the Americas. Forty-five percent hold director, VP, or C-level titles.

## Application Security Team Size
There are always far fewer application security team members than developers. Developers outnumber security professionals 100 to 1 in large organizations. More than half of respondents (53%) said they employ one to five application security team members.

![Chart showing team size distribution: 53% (1-5), 23% (6-10), 17% (11-20), 7% (21+)]

**Staffing Plans:**
Half of respondents plan to add more security staff, with the majority (38%) adding just one to five more. A non-trivial factor is the shortage of security talent.

## Measuring Success
Nearly three-quarters (72%) view vulnerability reduction as the key measure of success. 44% measure success based on security vulnerability identification, not remediation. 42% are achieving release speed and quality by integrating security testing and automation.

![Chart showing success metrics: 72% (Overall reduction), 46% (Specific reduction), 44% (Number identified), 42% (Increased velocity), 30% (Decrease in bug bounty)]

## Reporting to the CISO
Half of respondents are providing the CISO with a PDF report of security scan findings.

![Chart showing reporting types: 50% (PDF report), 34% (Custom charts), 32% (No report), 4% (Other)]

## Frustrations with Testing
The most prominent frustration is testing too late in the life cycle (43%). An equal number (43%) are frustrated by their inability to interpret scan findings.

![Chart showing frustrations: 43% (Too late), 43% (Understanding findings), 36% (Too many false positives), 36% (Tracking status), 29% (Prioritizing remediation), 25% (Finding who performs remediation)]

## Automation Strategies
Those with CI/CD pipelines (36%) are automating or plan to automate security testing as part of a larger automation strategy. 31% do not have automation.

![Chart showing automation methods: 36% (CI/CD), 31% (None), 18% (SCM integration), 15% (Cronjobs)]

## Consuming Security Results
Half the respondent base (49%) considers a bug tracking tool like Jira the best place to consume application security results.

![Chart showing consumption methods: 49% (Bug tracking tool), 20% (IDE), 19% (Pull/merge request), 12% (PDF report)]

## Types of Security Testing
Two-thirds of survey participants (67%) are doing API testing.

![Chart showing testing types: 67% (API), 44% (SAST), 36% (Container scanning), 31% (SCA), 21% (DAST), 14% (IAST), 11% (Fuzzing)]

## Open Source Tooling
Despite the increased use of open source code, 58% said they’re not using open source security testing tools.

## Desired Improvements
Most respondents (62%) chose better integrations as the top improvement they’d like to see.

![Chart showing desired improvements: 62% (Better integrations), 65% (User interface/experience), 52% (Faster scans), 50% (Less false positives), 45% (More offerings), 39% (More accurate queries)]

## Communication with Developers
Jira tickets are the top means of communicating with developers (48%).

![Chart showing communication methods: 48% (Jira), 31% (Emails), 13% (Meetings), 6% (Slack), 2% (Other)]

## Security Champions
Two-thirds of respondents (66%) lack a security champion.

## Security Awareness
Nearly half of survey participants (47%) are using a wiki as the primary vehicle for security awareness.

![Chart showing awareness methods: 47% (Wiki), 44% (Videos), 39% (OWASP), 34% (Just-in-time training), 6% (Other)]

## Future Skills
Subject matter expertise tops the list (61%) of what respondents think security professionals will need to have in the future.

![Chart showing future skills: 61% (Subject matter expertise), 56% (Soft skills), 52% (Advanced programming), 48% (AI/ML), 35% (IoT/blockchain)]

## Speed vs. Quality
64% of respondents consider the quality of application testing more important than speed.

## Conclusion
Application security continues to rise in importance because it represents legal, regulatory, and brand issues. Speed and quality must go hand in hand. Moving from DevOps to DevSecOps helps.

## About Cyber Security Hub
The Cyber Security Hub is an online news source for global cyber security professionals and business leaders. We’re dedicated to providing the latest industry news, thought leadership and analysis in the cyber security space.

[^1]: "There’s always a shortage of experienced people, and that’s the challenge," said Stephen Gates, security evangelist and senior solutions specialist at Checkmarx.