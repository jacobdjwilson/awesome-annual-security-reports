# Hacker-Powered Security Report 2024/2025

## Table of Contents
- [Executive Summary](#executive-summary)
- [The Impact of AI on Security Research and Vulnerability Management](#the-impact-of-ai-on-security-research-and-vulnerability-management)
- [Security Researchers Expand Their Expertise Into AI, APIs, and More](#security-researchers-expand-their-expertise-into-ai-apis-and-more)
- [Run a Top-Tier Program That Won’t Break the Bank](#run-a-top-tier-program-that-wont-break-the-bank)
- [The Top Ten Vulnerabilities Need to Change](#the-top-ten-vulnerabilities-need-to-change)
- [The Best Defense Has Layers of Depth](#the-best-defense-has-layers-of-depth)
- [Measuring Success: Invest in Return on Mitigation](#measuring-success-invest-in-return-on-mitigation)
- [Conclusion](#conclusion)

---

## Executive Summary

Cyberthreats are always evolving. So must your defenses. Faster, smarter, and always ahead.

Every organization is a technology organization. Car manufacturers, government agencies, and banks do very different things, but they all conduct business digitally. With AI deployments—as well as AI-powered threat actors—now mainstream, the digital threat landscape is growing and changing faster than ever.

Just a few years ago, organizations only had to worry about one OWASP Top 10 list. Now there are OWASP Top 10 lists for mobile security, LLMs and more. What's next? And how do you stay ahead of it all?

We've been watching these trends and reporting on them for over eight years now in the Hacker-Powered Security Report. Read on to learn about the impact of AI on security research, what the researchers themselves are thinking and seeing, industry trends, and more. We report on the top vulnerability types, and how the most resilient companies have adopted a defense-in-depth strategy, fortifying every layer of their security posture and using continuous vulnerability testing throughout the software development life cycle.

### From Compliance to Competitive Advantage

Human-powered, AI-enabled security testing remains vital in identifying vulnerabilities that automated scanners often miss, as the creativity and expertise of skilled researchers are unmatched by machines.

Since the first Hacker-Powered Security Report in 2017, the security researcher community has consistently been proven to keep pace with technological changes, deliver ongoing value, and gain the trust of even the most risk-averse organizations.

Over the past decade, we’ve seen significant progress for trust in good-faith research, including updated safe harbor guidelines from the Department of Justice, legislation requiring organizations to implement vulnerability reporting processes, and increasing adoption of vulnerability disclosure and bug bounty programs by leading enterprises. In fact, these programs are now cited in S1 filings as evidence of an organization's commitment to security.[^1] [^2]

[^1]: U.S. Department of Justice Office of Public Affairs. Department of Justice Announces New Policy for Charging Cases under the Computer Fraud and Abuse Act.
[^2]: CyberScoop. Vulnerability disclosure policies eyed for federal contractors in Senate bill.

### About the Hacker-Powered Security Report

This 8th Annual Hacker-Powered Security Report compiles insights, data, and analysis from customers, security researchers, and HackerOne’s comprehensive vulnerability database. The insights are gathered from:

- **Aggregated, anonymized data** from the HackerOne Platform, made up of over 500,000 valid vulnerability reports.
- **A survey**, conducted in partnership with Opinion Matters, of 500 security leaders globally about their approach to cybersecurity challenges.
- **Our annual survey** of 2,000+ highly skilled and active members of the security researcher community.
- **Our annual survey** of 50 customers, representing a range of organizational sizes, structures, and industries.

---

## The Impact of AI on Security Research and Vulnerability Management

Last year we introduced a dedicated AI section in the Hacker-Powered Security Report, recognizing the growing influence of GenAI on how organizations operate and plan ahead. This year we’re digging deeper into both security for AI (how organizations manage risks in AI deployments) and AI for security (how researchers and organizations use AI to improve vulnerability management).

> “The downside of AI is that it introduces more vulnerabilities. If a company uses it, we’ll find bugs in it. AI is even hacking other AI models. It’s going so fast and security is struggling to catch up.”
> — Jasmin Landry, @jr0ch17, Security Researcher and HackerOne Pentester

### Security for AI

We surveyed 500 security professionals to understand their experiences and opinions around AI adoption. Nearly half (48%) cited GenAI as one of the most significant risks facing their organizations. The top concerns included training-data leaks (35%), unauthorized AI usage (33%), and the hacking of AI models by external parties (32%).

![Chart: IT-related risks of concern]

64% of respondents believe GenAI will have a major impact on their organization, with 62% confident in their ability to secure its use. However, 51% are concerned about the reputational risks tied to AI, and another 51% highlight that basic security practices are being overlooked in the rush to implement GenAI.

### AI Safety vs. AI Security

- **AI Safety**: Focuses on preventing AI systems from generating harmful content, from instructions for creating weapons to offensive language and inappropriate imagery.
- **AI Security**: Involves testing AI systems with the goal of preventing bad actors from abusing the AI to, for example, compromise the confidentiality, integrity, or availability of the systems the AI is embedded in.

---

## Security Researchers Expand Their Expertise Into AI, APIs, and More

More of the security researcher community is choosing the flexibility of a full-time career as security researchers are dedicating more hours to developing their skills. 30% now hack full-time, up from 24% in 2023.

While 77% of researchers cite earning money as a key motivator, 64% view hacking as a valuable way to learn and develop their skills.

![Chart: What motivates you to hack?]

When HackerOne first launched, most hacking activity focused on web applications, and while 88% of researchers still specialize in this area, the landscape is shifting. 56% of researchers also specialize in APIs, while almost 10% now focus on AI and large language models (LLMs).

---

## Run a Top-Tier Program That Won’t Break the Bank

The most security-resilient customers on the HackerOne Platform share the following attributes:
- Thoughtfully designed rewards.
- Clear expectations set from the start.
- Excellent communication with researchers.
- Safe harbor legal protections.

### Perspectives From the Hacker Advisory Board

"Gather feedback from hackers to improve your program. Ask what they'd like to see, such as adding assets to scope—something I’ve requested in the past, which led to discovering additional vulnerabilities. Lower barriers to entry; extra policies or special requirements may discourage researchers from participating."
— Jim Green, @greenjam, Security Researcher

---

## The Top Ten Vulnerabilities Need to Change

HackerOne has been measuring the top ten vulnerabilities reported on our platform for eight years. Valid vulnerabilities on the HackerOne Platform have jumped 12% over the past year, with 78,042 valid issues found across 1,300+ customer programs.

### Industry Spotlights

- **Financial Services**: Featured vulnerability: Insecure direct object reference (IDOR) (up 47% from 2023).
- **Government**: Featured vulnerability: Cross-site scripting (XSS) (up 17% from 2023).
- **Telecoms**: Featured vulnerability: Improper authentication (up 55% from 2023).
- **Retail and E-commerce**: Featured vulnerability: Information disclosure (up 71% from 2023).
- **Transportation**: Featured vulnerability: SQL injection (up 93% from 2023).

---

## The Best Defense Has Layers of Depth

We believe the best security programs are built around a defense-in-depth strategy. HackerOne's approach to offensive security ensures continuous vulnerability detection throughout the SDLC, maximizing coverage from the earliest stages of development through deployment and beyond.

### Bug Bounties and Pentests

Pentest as a Service (PTaaS) is gaining momentum. At HackerOne, we’ve seen a 67% increase in pentesting over the past year. HackerOne pentests uncover an average of 12 vulnerabilities per engagement, with 16% classified as high or critical.

---

## Measuring Success: Invest in Return on Mitigation

Organizations that spend less on technology often see more severe vulnerabilities. The most security-resilient organizations are making the financial case for their bounty budgets using a return on mitigation (ROM) approach.

---

## Conclusion

As the digital landscape continues to evolve with the rapid integration of AI, the necessity for continuous, human-led security testing has never been greater. By fostering strong relationships with the researcher community, maintaining a broad and transparent testing scope, and integrating findings directly into the SDLC, organizations can stay ahead of emerging threats and build a more resilient security posture.

---

the deployment phase when pentests often reveal systemic issues. Together,
pentesting and bug bounties provide comprehensive security coverage,
reinforcing resilience across all development stages.

    |    8th Annual Hacker-Powered Security Report    |    58

At which stages of your software development
life cycle (SDLC) do you typically observe the
most critical bugs? (Select up to three.)

Recommendations

Define clear scopes for your PTaaS and bounty program so they complement each other rather
than overlap. Use PTaaS for scheduled, structured assessments of high-priority systems and
bug bounty for continuous, exploratory testing across a broader range of assets.

Centralize reporting and communication to track vulnerabilities from both programs and avoid
duplicate efforts by ensuring both sets of testers can see past reports and updates, making it
easier and more transparent for your internal teams, as well.

Rotate pentesters to bring fresh eyes and perspectives to each assessment. Keep bug bounty
always on to ensure 24x7, continuous testing by diverse security researchers.

59    |    8th Annual Hacker-Powered Security Report    |

Measuring Success: Invest
in Return on Mitigation

Data breach costs are more significant than ever, seeing a 10% year-over-year rise in
the global average, now at $4.88 million—the largest increase since the pandemic.  A
major driver of this is the growing shortage of security staff, with over half of breached
organizations reporting this issue—a 26% jump from last year. This shortage adds an
average of $1.76 million to the overall breach cost.

9

In contrast, even top-tier bounty payouts in the 95th percentile are relatively small
investments. However, many organizations still struggle to measure the ROI of proactive
security measures like bug bounty programs. Securing budget for these initiatives often
requires stakeholder buy-in, which means translating bug bounty success into clear
financial value.

9

IBM. Cost of a Data Breach Report 2024.

How does your organization
measure the ROI of its
security programs?

    |    8th Annual Hacker-Powered Security Report    |    60

“The bug bounty program is the highest ROI across all of our
spend. It’s really hard to show ROI, but with bug bounty, I have
a baseline. I can say, ‘This vulnerability was able to be found by
someone outside the organization. Someone that was not
authorized to access this system was able to access it.’ Even
with vulnerabilities that are not within our program, bug bounty
allows me to put a price tag on them. I can explain this business
case and our stakeholders are able to prioritize bug bounty
higher than other tools that also generate ROI.”

Eric Kieling
Head of Application Security, Booking.com

Introducing Return
on Mitigation

HackerOne recently introduced the concept of return on
mitigation (ROM), an extension of ROI that is specific to
cybersecurity. ROM compares the cost of mitigating risks
to the potential financial losses from cyber incidents,
providing a clear metric to measure how security efforts
protect businesses from costly breaches.

ROM’s nuanced view offers both the qualitative and
quantitative benefits of proactive security investments,
considering factors including:

Restoring compromised systems
Lost revenue due to downtime
Legal and regulatory penalties
Damage to public trust and reputation

61    |    8th Annual Hacker-Powered Security Report    |

ROM provides a practical framework for evaluating the true value of security
investments by substituting net profit for mitigated losses. It shifts the focus from
short-term cost savings to long-term resilience, highlighting the importance of risk
management and the overall business benefits of proactive security measures.

Read more about the concept in the SANS White Paper: Human-Powered Security Testing.

Recommendations

Track your response times, your ability to stay within your agreed SLAs to remediate
vulnerabilities, and your time to bounty payout to understand the health of your program and
efficacy of your processes.

Understand the goals and success metrics of your different stakeholders, from engineering
teams to the board, so you can align your reporting to their priorities and focus areas.

Adopt a return-on-mitigation strategy to effectively put an avoided incident into financial terms.

“Paying $15k for a critical vulnerability that could cost us millions in
the wild is the best discount."

Security Leader
Media & Entertainment Industry

    |    8th Annual Hacker-Powered Security Report    |    62

Conclusion

We’re seeing the maturation of human-powered security. The increasing trust that
traditionally conservative industries and organizations are placing in the security
researcher community is evident from the validation of government guidance, growing
adoption of the model, and public promotion as a signifier of security best practices.
The 8th Annual Hacker-Powered Security Report shows that as the security
researcher community is diversifying in skills and experience, organizations will need
to ensure they are maintaining researchers’ focus and enthusiasm via accurate bounty
tables, expanding scope, and a commitment to developing positive relationships.

The collaboration between researchers and organizations is resulting in more high and
critical vulnerabilities discovered than ever before. However, a successful reduction of
the most easily avoidable vulnerabilities is going to take a more concerted approach to
examine which vulnerabilities are most prevalent in your organization, their causes,
where they’re introduced, and the tactics to phase them out of development. AI will
likely play a significant role in elevating security teams’ ability to manage vulnerability
reports and fixes. Meanwhile, the researcher community will be crucial in ensuring the
safety and integrity of the AI tools we’re coming to rely on.

HackerOne is firmly behind these efforts and we strive for a safer internet where
cross-site scripting and improper authentication are things of the past and instead our
researchers are incentivized to maximize their human skill and creativity, finding the
most novel and exclusive vulnerabilities.

contact us
sales@hackerone.com

63    |    8th Annual Hacker-Powered Security Report    |

Data Sources

HackerOne’s annual community survey surveyed 2,321 security
researchers that were active on the platform in the 30 days prior
to the survey. The survey took place between June 24, 2024,
and August 4, 2024.

The data collected from HackerOne’s platform is from the period
between June 2023 and June 2024.

HackerOne’s customer survey was conducted via UserEvidence
and surveyed 50 HackerOne customers between July 15, 2024,
and August 15, 2024.

The survey of security professionals was conducted by Opinion
Matters and surveyed 500 security professionals across the US
and Europe. The survey was conducted between July 31, 2024,
and August 6, 2024.

About HackerOne

HackerOne is the global leader in human-powered, AI-enabled security, fueled by the
creativity of the world’s largest community of security researchers plus cutting-edge
AI to protect your digital assets. The HackerOne Platform combines the expertise of
our elite community and the most up-to-date vulnerability database to pinpoint
critical security flaws across your attack surface. Our integrated solutions—including
bug bounty, pentesting, code security audits, spot checks, and AI red teaming—
ensure continuous vulnerability discovery and management throughout the software
development life cycle. Trusted by industry leaders such as Coinbase, General
Motors, GitHub, Goldman Sachs, Hyatt, PayPal, Snap Inc., and the U.S. Department
of Defense, HackerOne was named a Best Workplace for Innovators by Fast
Company in 2023 and a Most Loved Workplace for Young Professionals in 2024.

    |    8th Annual Hacker-Powered Security Report    |    64

8th Edition–2024/2025

Hacker-Powered
Security Report

If you want to turn this data into real impact
for your organization, speak to our experts

sales@hackerone.com