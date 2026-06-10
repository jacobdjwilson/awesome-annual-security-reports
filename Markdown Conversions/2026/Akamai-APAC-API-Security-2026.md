# API Security Impact Study: How AI Innovation Amplifies API Risk in APAC

## Table of Contents
- [Introduction](#introduction)
- [About the study](#about-the-study)
- [Regional overview: APAC’s strengths and weaknesses and the financial impact of weak API security](#regional-overview-apacs-strengths-and-weaknesses-and-the-financial-impact-of-weak-api-security)
- [Top 5 API security incident types in APAC](#top-5-api-security-incident-types-in-apac)
- [API security strengths in China, Japan, India, and Singapore](#api-security-strengths-in-china-japan-india-and-singapore)
- [APAC’s API visibility and governance gaps](#apacs-api-visibility-and-governance-gaps)
- [When API security becomes an AI risk](#when-api-security-becomes-an-ai-risk)
- [The API resilience gap in China, Japan, India, and Singapore](#the-api-resilience-gap-in-china-japan-india-and-singapore)
- [Featured insights: API security in four APAC countries](#featured-insights-api-security-in-four-apac-countries)
- [The financial cost of weak API security](#the-financial-cost-of-weak-api-security)
- [Three key regional insights](#three-key-regional-insights)
- [Conclusion](#conclusion)
- [Credits](#credits)

---

## Introduction
For four years, Akamai has studied the state of API security across successive eras of business innovation — digitization, cloud adoption, and now AI development — each accompanied by rapid API growth.

In 2026, the average global enterprise has nearly 6,000 APIs, with the top quartile exceeding 29,000. As these environments expand, it becomes even harder to track APIs, identify their risks, and understand whether they’ve been tested for resiliency against attacks — especially as AI adoption increases the rate of new API connections and dependencies.

Our latest API Security Impact Study survey shows that API security gaps have been increasing year-on-year. This study of 640 cybersecurity decision-makers across four APAC markets points to a clear inflection point: API growth is outpacing organizations’ ability to secure these business-critical connectors, while AI adoption is further increasing risk exposure.

The findings suggest this API security gap is being shaped by four structural leadership challenges:
- **Unfinished business securing existing APIs, as new risks emerge**: 81% of APAC organizations experienced an API security incident in the past 12 months.
- **A perception gap between leadership and technical teams**: C-suite leaders are more confident about their enterprises’ API security testing processes than the teams responsible for implementing them.
- **Overreliance on traditional security approaches**: Manual inventory processes and legacy tools fail to keep pace with API sprawl, particularly as AI accelerates development and integration.
- **Limited preparedness for emerging API threats**: Without robust discovery and inventory capabilities, organizations lack visibility into AI-linked APIs and the high-risk actions they can take.

These challenges place enterprises on a path to more attacks and wider business impact. This report examines how those pressures are playing out in the key APAC markets of China, India, Japan, and Singapore, and what they reveal about API security in a fast-moving regional context.

## About the study
In November 2025, Akamai commissioned Phronesis Partners to survey 1,840 cybersecurity decision-makers on the current state of API security across 10 countries and six industries globally. This region-specific report, which accompanies the wider global study, features responses from 640 leaders across C-level, AppSec, and DevSecOps roles based in China, India, Japan, and Singapore. It reveals the latest leader and team thinking, identifies key region-specific trends, and pinpoints structural API security weaknesses. It also quantifies the cost of maintaining the status quo.

## Regional overview: APAC’s strengths and weaknesses and the financial impact of weak API security
The four APAC countries featured in our survey may be global leaders in API security, but their ability to track APIs and defend against attacks has failed to keep pace with the growth of large, business-critical, and increasingly AI-connected API estates.

![Chart showing percentage of organizations that experienced API security incidents in the past 12 months: China 63%, Japan 84%, India 93%, Singapore 90%, APAC average 81%]

As shown on the next page, the most common forms of security incidents in China, India, Japan, and Singapore are attacks on APIs linked to enterprise AI applications and LLMs. This is also the type of API security incident that APAC firms say they are least prepared to address.

## Top 5 API security incident types in APAC
Q. Which of the following types of API security incidents has your organization experienced in the past 12 months?

| Rank | Incident type | APAC average | China | Japan | Singapore | India |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Attack involving APIs linked to AI technologies (e.g., apps, agents, LLMs) | 43% | 39% | 48% | 48% | 40% |
| 2 | Exploitation of missing or insufficient access controls | 37% | 36% | 32% | 43% | 39% |
| 3 | Data breach and/or data leaks via APIs | 36% | 43% | 31% | 40% | 35% |
| 4 | Exploitation of unmanaged APIs (e.g., shadow or zombie APIs) | 34% | 22% | 36% | 36% | 40% |
| 5 | Exploitation of API misconfigurations | 34% | 19% | 45% | 32% | 37% |

This shortfall in API visibility and security becomes more critical as organizations deploy more AI-enabled applications because APIs connect the models, data, services, and workflows those applications rely on. Behind the scenes, AI-linked APIs also retrieve data and execute actions, including responding to prompts that may come from an attacker rather than a legitimate user. As those dependencies grow, API weaknesses are more likely to disrupt core business processes rather than remain isolated technical issues.

## API security strengths in China, Japan, India, and Singapore
APAC organizations in the four markets surveyed are ahead of the global average on API security focus, ownership, and advanced testing. Nearly three-quarters of respondents say their focus on API security has increased, often driven by rapid API proliferation stemming from AI innovation, cloud adoption, and other key business initiatives.

![Graphic showing APAC's investment in API security: 72% say focus increased, 58% have personnel responsible for API security, 40% report advanced testing]

The constant demand for APIs means they are often released hastily, with misconfigurations or missing protections, and without being tested against real-world attack scenarios. Testing that is security-focused, SDLC-wide, and CI/CD-integrated is critical to ensure resilience against attacks for both APIs and the AI applications that depend on them.

## APAC’s API visibility and governance gaps
Across the four markets surveyed, many organizations still do not have a complete picture of their API estate as it grows in size and complexity. That gap increases risk because teams cannot assess or protect APIs they have not fully identified. Many teams still lack a full view of which APIs return sensitive data, even as AI applications make those APIs more exposed and more important to protect.

![Chart showing percentage of organizations that have a full API inventory and know which of their APIs return sensitive data: APAC average 22%, China 34%, India 21%, Singapore 21%, Japan 11%]

In Japan, for example, just 11% of respondents say they have a full API inventory and know which APIs return sensitive data. That is around half the regional average and makes Japan the lowest-ranked country globally in the study. It is also a significant drop from 2025, when more than three times as many (37%) Japanese respondents said they had full visibility across both measures.

## When API security becomes an AI risk
As AI adoption expands, prompting an increase in API estates, the API visibility problem becomes more acute because APIs determine what AI applications can access, return, and trigger. If teams do not know which AI-linked APIs expose sensitive data, they are less able to spot weak points, test for misuse, or plan for and contain the impact of attacks. At a time when organizations worldwide are expected to spend US$37 billion on generative AI in 2025, including $19 billion at the application layer[^1], stronger visibility into AI-linked APIs is becoming a basic requirement for protecting that investment.

[^1]: Tim Tully, Joff Redfer, Deey Das, and Derek Xiao, 2025: The state of generative AI in the enterprise Menlo Ventures, December 9, 2025.

## The API resilience gap in China, Japan, India, and Singapore
![Graphic highlighting: 22% have full inventory/sensitive data knowledge; 43% hit by attacks on AI/LLM APIs; 40% cite poor visibility as biggest worry]

### API attacks viewed as a top threat to APAC enterprises’ cyber resilience
Q: What are the top 5 cyberthreats that are most important to your organization from the perspective of achieving cyber resilience?
- Data breaches/exfiltration: 55%
- API security incidents: 52%
- Ransomware/malware: 48%
- Malicious bot attacks: 34%
- Attacks on our organization’s AI technologies: 33%

## Featured insights: API security in four APAC countries

### China
- **Incident rate**: 63%
- **Average cost per incident**: US$818,000
- **#1 incident type**: Data breaches and/or data leaks via APIs (43%)
- **Increased focus**: 85%
- **Interesting finding**: In China, the most frequently cited cause of API security incidents was that WAFs help, but additional protections are still needed. And yet, 80% of Chinese enterprises use WAFs, and only 27% use dedicated API security solutions.

### Japan
- **Incident rate**: 84%
- **Average cost per incident**: US$1.59 million
- **#1 incident type**: Attacks involving APIs linked to AI (48%)
- **Increased focus**: 64%
- **Interesting finding**: Japan combines relatively high incident exposure with weak visibility. Only 11% of respondents say they have a full API inventory and know which APIs return sensitive data, down sharply from 37% in 2025.

### India
- **Incident rate**: 93%
- **Average cost per incident**: US$497,000
- **#1 incident type**: AI-linked API attacks (40%) and incidents involving unmanaged APIs (40%)
- **Increased focus**: 76%
- **Interesting finding**: 81% of respondents say their organization has personnel specifically responsible for API security, the highest figure among the four markets. Yet 93% still report incidents, suggesting that ownership alone is not enough without stronger visibility and day-to-day protection.

### Singapore
- **Incident rate**: 90%
- **Average cost per incident**: US$1.33 million
- **#1 incident type**: Attacks involving APIs linked to AI (48%)
- **Increased focus**: 57%
- **Interesting finding**: Singapore combines very high incident exposure with some of the largest API estates in the four surveyed markets. While the typical organization sits in the range of 5,000 to less-than 10,000 APIs, the mean inventory is much higher at 46,639.

## The financial cost of weak API security
The dedication to API security in China, Japan, India, and Singapore is clear, but organizations in these markets have not yet consistently protected themselves from repeat attacks or their financial impact. An average API security incident in the region costs more than US$1 million. The financial impact is greatest in Japan and Singapore. The average incident cost in Japan is particularly notable because it has increased by nearly 200% (196.8%) year-on-year, reaching more than US$1.5 million in 2026.

### Average financial impact of API security incidents by country
![Bar chart showing average financial impact: Japan $1.59M, Singapore $1.33M, Brazil $1.12M, China $817K, UK $782K, Germany $713K, India $540K, US $497K, France $470K, Mexico $458K]

### Average financial cost of API security incidents in 2025 vs. 2026
| Country | 2025 Avg. cost | 2026 Avg. cost | Change |
| :--- | :--- | :--- | :--- |
| China | $780,236 | $817,940 | $37,704 |
| India | $708,617 | $497,499 | ($211,118) |
| Japan | $537,127 | $1,594,385 | $1,057,258 |
| Singapore | - | $1,328,844 | - |

### Top six impacts of API security incidents in APAC
1. Loss of customer goodwill and churned accounts: 37%
2. Loss of trust and reputation: 34%
3. Loss of productivity: 33%
4. Costs incurred to help fix the security issue: 30%
5. Service downtime/outage: 24%
6. Negative impact on department’s reputation with senior leaders/board: 24%

## Three key regional insights

### Regional insight 1: Visibility is getting harder to sustain as APAC’s API estates grow
Across the four surveyed APAC markets, the typical organization now has about 5,700 APIs in its inventory, while the largest estates in the top quartile exceed 32,300 APIs. While nearly all (95%) of respondents say their organization factors APIs into regulatory compliance requirements, far fewer are taking the practical steps needed to support that claim:
- 40% factor APIs into regulator-required reporting
- 59% factor APIs into security plans
- 63% factor APIs into risk assessments

### Regional insight 2: Repeated incidents reveal where API security is inadequate
Four-fifths of respondents say their organization experienced an API security incident in the past 12 months, and repeat attacks remain common. The average number of incidents in APAC is 3.6. Among incident-hit organizations, over half (56%) say they experienced four or more API-related incidents.

### Regional insight 3: The region is making progress on API security, but not all markets are equal
China and India are helping pull APAC forward, while Japan and Singapore show that progress is still inconsistent.

| Measure | APAC | China | India | Japan | Singapore |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Focus increased over past year | 72% | 85% | 76% | 64% | 57% |
| Personnel responsible for API security | 58% | 56% | 81% | 44% | 49% |
| Advanced, security-focused testing | 40% | 58% | 29% | 33% | 40% |
| Testing fully embedded in SDLC/CI/CD | 19% | 28% | 17% | 15% | 14% |

## Conclusion
The four APAC countries we surveyed are making real progress on API security. More organizations are increasing focus, assigning clearer responsibility, and strengthening testing. But that progress has not yet translated into consistent protection. Many organizations still do not have a clear view of which APIs expose sensitive data, and repeated incidents suggest those gaps are not being closed fast enough. The task now is to transfer that momentum into everyday security practice, especially across the APIs that are hardest to track, govern, and secure.

## Credits
- **Editorial and writing**: John Natale, Phronesis Partners
- **Review and subject matter contribution**: Barney Beal, Stas Neyman, Yariv Shivek
- **Promotional materials**: Ellen O’Brien
- **Marketing and publishing**: Georgina Morales Hampe