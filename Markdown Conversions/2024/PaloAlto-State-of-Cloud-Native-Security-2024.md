# The State of Cloud-Native Security 2024

## Table of Contents
- [Executive Summary: A Retrospect on the Previous Year](#executive-summary-a-retrospect-on-the-previous-year)
- [Introduction: Time Favors the Prepared](#introduction-time-favors-the-prepared)
- [Highlights of 2024 Survey Findings](#highlights-of-2024-survey-findings)
- [The Cloud Economy: A Global Perspective](#the-cloud-economy-a-global-perspective)
- [From Exploration to Cloud-Native Innovation](#from-exploration-to-cloud-native-innovation)
- [Plan for Cost Optimization of Legacy Apps](#plan-for-cost-optimization-of-legacy-apps)
- [Balancing Tools, Vendors, and Organizational Needs](#balancing-tools-vendors-and-organizational-needs)
- [Top Concerns in Cloud Security](#top-concerns-in-cloud-security)
- [Incident Response: The Race Against Time](#incident-response-the-race-against-time)
- [Securing Sensitive Data in the Cloud](#securing-sensitive-data-in-the-cloud)
- [What Would You Do Differently?](#what-would-you-do-differently)
- [The Human Factor](#the-human-factor)
- [Risks, Realities, and Cloud Security Strategies](#risks-realities-and-cloud-security-strategies)
- [Embracing the Unknown: The Impact of AI on the Application Lifecycle](#embracing-the-unknown-the-impact-of-ai-on-the-application-lifecycle)
- [Recommendations for Securing the Cloud](#recommendations-for-securing-the-cloud)

# Executive Summary: A Retrospect on the Previous Year

We begin our exploration of the 2024 state of cloud-native security with a look back at the events and influences of 2023, each of which factors into our current postures, the challenges we confront, and the strategies we’ve chosen to achieve our desired outcomes.

While agile development, open-source software, and cloud-native technologies gained momentum in 2023, attacks targeting the application layer have become an established trend. The cloud-native ecosystem grappled with a surge in supply chain attacks, highlighting the prevalence of vulnerabilities in open-source software and third-party libraries. Real-world data analyzed by our Unit 42 team enhanced this picture, identifying the cloud as the dominant attack surface, with 80% of medium, high, and critical exposures found in cloud-hosted assets.[^1]

For some time, we’ve prioritized application and infrastructure security. But we mustn’t forget that third, all-important ball in the air. With the global datasphere reaching 120 zettabytes in 2023,[^2] securing sensitive data remains mission critical. The challenges of monitoring and controlling sensitive information, however, have escalated.

> Cloud security is as much a business goal as anything else we endeavor to achieve.

What’s more, generative AI emerged in 2023 as a groundbreaking force with the potential to halve development time and costs, ultimately redefining the application economy.[^3] But much like the cloud and its myriad benefits inextricably tied to challenges we must address, generative AI as a development tool comes counterweighted with concerns. We had no sooner begun to wonder about potential issues when OWASP released the Top 10 LLM Security Risks for security teams, alerting us to prompt injection, insecure output handling, and new avenues for supply chain vulnerabilities and sensitive information disclosure.

But challenges are not new to us. It’s safe to say that generative AI is as much a mainstay as the cloud. We will increasingly tap into its power with an awareness of responsibility and a priority of security.

Looking at the path ahead, as we move forward in the pursuit of our objectives, we are certain of one thing—cloud security is as much a business goal as anything else we endeavor to achieve.

[^1]: Cortex Xpanse ASM Threat Report 2023
[^2]: Data Created Worldwide 2010-2025
[^3]: Economic Potential of Generative AI | McKinsey

# Introduction: Time Favors the Prepared

> Anticipating threats and adapting strategies ensures resilience in complex cloud environments.

When readiness wins the race against time, it’s the name of the game. You’ll hardly hear cloud security practitioners talk about pain points apart from the constraints of time. They are, after all, inundated with alerts and manually collating data from satellite tools while racing against attackers moving at machine speed to identify vulnerabilities.

Understandably, 90% of respondents from this year’s State of Cloud-Native Security survey want better risk prioritization. Upwards of 90% say the number of point tools they use creates blind spots affecting their ability to prioritize risk and prevent threats. Sixty-two percent of security practitioners want easy-to-use security solutions, with 1 in 3 respondents citing rapid technology changes as the primary obstacle contributing to attack surface expansion.

How multi is multicloud? Organizations are leveraging an average of 12 cloud service providers (CSPs) across SaaS, IaaS, and PaaS for their deployed applications. This, coupled with an average use of 16 cloud security tools, underscores the intricate ecosystem security teams must navigate. A 98% consensus emphasizes the importance of reducing the number of security tools, defining readiness in terms of simplification and consolidation.

> Organizations are leveraging an average of 12 cloud service providers.

Emerging concerns, such as the security risks associated with AI-generated code and unmanaged APIs, alongside traditional challenges like inadequate access management and the expanding attack surface, underscore the evolving nature of cloud security threats. Organizations are rethinking their strategies, with many emphasizing the need for foundational changes to enhance cloud security from the outset. Understanding the landscape is central to equipping security and DevOps teams with the necessary resources.

- What steps are organizations taking to effectively navigate data security and the need for rapid deployment? 
- Where are organizations running into challenges? 
- How are they bridging security and development teams? 
- How ready are organizations to handle AI-related security risks? 
- How effectively are they integrating solutions into their operational frameworks?

Our annual multi-industry survey seeks to answer these questions and more to provide insights into the best practices shaping the future of cloud-native security.

# Highlights of 2024 Survey Findings

### People are rethinking their lift and shift deployments.
When asked what they would do differently if migrating to the cloud for the first time, **50%** of respondents said they would spend more time refactoring their applications instead of migrating with minimal changes.

Supporting this sentiment, our survey shows that organizations that moved workloads to the cloud without optimizing them for the cloud had higher total costs of ownership. What’s more, their applications didn’t gain the advantages of agility and scalability the cloud is renowned for.

### When security is seen as a hindrance, stress levels are high.
Security is a gating factor hindering software releases, according to **86%** of respondents.

- **71%**: Highlighting the risks associated with accelerated time-to-market schedules, 71% of respondents attribute rushed deployments to security vulnerabilities, underscoring the tension between the need for rapid development and the imperative of maintaining security.
- **48%**: Almost half of respondents experience major release delays all or most of the time.
- **52%**: Of respondents cite conflict between DevOps and SecOps as a significant source of stress.

### AI-generated code is more worrisome than AI-assisted attacks.
- **43%**: More than 2 in 5 security professionals (43%) predict AI-powered threats will evade traditional detection techniques to become a more common threat vector.
- **38%**: Of respondents rank AI-powered attacks as a top cloud security concern.
- **44%**: Are more apprehensive about risks introduced by AI-generated code.
- **100%**: Yes, all respondents are reportedly embracing AI-assisted coding.

# The Cloud Economy: A Global Perspective

> Across regions, cloud investment trends affirm the cloud’s strategic significance.

Organizations worldwide made substantial investments in cloud infrastructure, services, and operational efficiencies to drive digital transformation and expansion. The overall trend shows a surge in cloud spending with over 50% of organizations investing more than $10 million annually in cloud services. This integration of cloud technologies into various aspects of business operations suggests that investment trends will persist, if not accelerate, as organizations pursue greater agility, scalability, and innovation.

![Figure 1: Regional investment patterns showing cloud spending snapshot. The chart compares organizations spending less than $10 million vs. $10 million or more across 10 countries. High-investment leaders ($10M+) include US (70%), UK (69%), Singapore (73%), Australia (72%), and Mexico (72%). Lower investment brackets are more prevalent in Brazil (40%), India (41%), and Japan (43%).]

Among regions, we see slight but telling variations. Australia, Mexico, and Singapore exhibit strong cloud spending in higher investment brackets, while the United States and the United Kingdom continue to invest significantly in moderate ranges. Cloud spending patterns in France and Germany indicate a mature yet cautious approach, with the bulk of investments falling within the €9 million to €46 million range.

In contrast, emerging markets like Brazil and India, along with Japan, have a higher proportion of organizations investing below the $10 million mark, at 40%, 41%, and 43%, respectively. Beyond cloud maturity, this trend may reflect a greater presence of small to medium-sized organizations, as well as conservative spending strategies in these regions.

Organizations reporting “Extensive Integration” or “Fully Native Environment” tend to invest more in cloud technologies compared to those with “Basic Infrastructure”. In the U.K., for instance, 32% of organizations spending less than $10 million are at the initial stages of exploring the cloud, compared to 76% of those investing $10 million or more, having achieved extensive cloud integration. This pattern is consistent across regions, indicating that as organizations mature in their cloud journey, their cloud spend increases, likely due to the adoption of more advanced cloud services and architectures, in addition to scaling.

# From Exploration to Cloud-Native Innovation

> The cloud journey is not linear. It is a continuum of adaptation, learning, and transformation—one shaped by strategic investments, maturity levels, deployment methodologies, and operational efficiencies.

Cloud maturity extends beyond the adoption of technologies. It is both a reflection of and influence on an organization’s culture, processes, and the ability to harness cloud capabilities for business transformation. Among this year’s survey respondents, maturity levels range from using basic cloud infrastructure for select projects to extensive integration and fully native cloud environments.

Across this range, we see a correlation in application deployment methodologies.

> **50%** of respondents say they would spend more time refactoring their applications.

![Figure 2: Primary method of application deployment to the cloud. Total Average: Cloud-Native (33%), Lift and Shift (36%), Refactor (31%). Average for organizations with 3+ years: Cloud-Native (36%), Lift and Shift (33%), Refactor (31%).]

The deployment preference for lift and shift (35%) aligns with the pragmatic approach many organizations take toward cloud migration. While cloud-native and refactoring deployments offer long-term benefits, the initial focus on fast, low-disruption migration has been a historic approach.

Organizations that begin with lift and shift typically progress through refactoring to cloud-native development, maturing beyond seeking quick wins to embracing cloud-first strategies for gains in performance, scalability, and cost-efficiency. Our survey bears out this trend, with cloud-native deployments displacing lift and shift at 36% among organizations with 3 or more years in the cloud.

**Performance, scalability, cost-efficiency > Quick wins**

Across regions, maturity trends show Australia (26%), Singapore (26%), and the U.S. (24%) out front with roughly a quarter each having full cloud-native environments. France and Germany follow at 17% and 14%, respectively.

![Figure 3: Countries with the most all cloud-native environments: Australia (26%), Singapore (26%), United States (24%), France (17%), Germany (14%).]

# Plan for Cost Optimization of Legacy Apps

> Legacy app modernization consumes a significant portion of cloud TCO, emphasizing the importance of strategic cloud migration planning.

The majority of respondents (67% globally) reports spending between 10% to 30% of their cloud total cost of ownership (TCO) on legacy app modernization. For 24% of organizations, costs soar upwards of 30%, highlighting the need to balance operational continuity and the pursuit of innovation.

> **30%** of cloud costs go to overhauling legacy apps.

Among regional variations, Latin America and Japan and Asia-Pacific report a higher percentage (29% and 26%, respectively) of respondents spending 30% or more of their cloud TCO on legacy app optimization. India stands out with 42% of respondents indicating that 30% or more of their cloud TCO goes toward optimizing legacy apps for the cloud. When asked why developers’ time is diverted to resolving bugs and code vulnerabilities, 45% blame application architecture.

The significant spend on legacy app modernization underscores the need for strategic planning in cloud migration projects. Organizations should assess which applications are suitable for lift and shift versus those that require refactoring or complete redevelopment to optimize costs and benefits. Security and compliance challenges make this particularly important, in that older applications may not have been designed with cloud-native security in mind.

# Balancing Tools, Vendors, and Organizational Needs

> The cloud is, well, nebulous. Add a cloud service provider (CSP) here, a security tool there. The ecosystem extends. And extends. Complexity is a constant companion.

With an average of 16 cloud security tools on board, it’s no surprise that 98% of respondents consider it important to reduce this number. Almost as many (97%) want to reduce the average 14 vendors they work with.

Taking on complexity in one form or another is a recurrent theme in annual publications of the State of Cloud-Native Security Report. To date, we’ve not seen an indication of progress on this front. The number of tools dedicated to cloud security has, in fact, increased 60% from last year’s findings. The drive to address complexity, however, is visceral for those who routinely confront it.

> **98%** of respondents consider it important to reduce the average 16 cloud security tools they have on board.

In 2024, multicloud translates into approximately 12 cloud service providers across SaaS, IaaS, and PaaS per organization. Regional averages range from 16 in the U.S. to a no less impressive 9 in Latin America. And this represents only the public cloud portion of the ecosystem, accounting for little more than half (52%) of an organization’s cloud workloads. As organizations use more CSPs, maintaining visibility and ensuring consistent security policies, access controls, and data protection measures becomes taxing. Complexity and fragmentation of cloud environments, for more than half of survey respondents (54%), presents a major security challenge.

> **54%** of respondents agree that complexity and fragmentation of cloud environments presents a major challenge to security.

### Architecture-Hopping: Trend or Transition?

![Figure 4: Cloud architecture usage distribution: VM (21%), Self-hosted Containers (21%), CaaS (19%), PaaS (19%), Serverless (20%).]

Cloud architecture introduces another layer of complexity. The distribution of workloads among different architectures seen among 2024 survey respondents suggests a transitional cloud landscape with organizations navigating between traditional (VMs) and modern (serverless) architectures.

This diversity challenges security teams to create consistent policies and security solutions for these environments. Characterized by portability, granularity, ephemerality, and heterogeneity, modern workloads have expanded the attack surface. They require a different approach to security, one with actionable insights, monitoring, and incident response.

# Top Concerns in Cloud Security

> A range of threats poses serious security concerns, pointing to the importance of proactive measures that can outpace emerging and perennial risks.

When exploring top cloud security concerns, survey responses portray a global community acutely aware of the multifaceted threats facing cloud environments. From the nuanced challenges of securing AI-generated code and APIs to the universal threats posed by inadequate access management and insider risks, concerns are varied and far-reaching.

1. **AI-Generated Code**: Unforeseen vulnerabilities and exploits introduced by AI-generated code are worrisome to 44% of organizations. As algorithms autonomously create software, the lack of human oversight may lead to undetected security flaws.
2. **API Risks**: Close behind in top-ranked concerns, 43% of global respondents have their sights on API-associated risks. Regionally, concern for API risks peaks in Brazil (52%).
3. **AI-Powered Attacks**: A growing awareness of how AI might be weaponized has 38% of organizations concerned.
4. **Inadequate Access Management**: Cited by 35% of organizations, particularly acute in Latin America (44%).
5. **CI/CD’s Impact on the Attack Surface**: Concerns 34% of organizations, spiking in Japan and Asia-Pacific (40%).
6. **Insider Threats**: A concern for 32% of respondents, consistent across regions.
7. **Unknown, Unmanaged Assets**: 29% of respondents are concerned, with higher awareness in Europe.

# Incident Response: The Race Against Time

> Security incidents require organizations to continuously adapt and evolve their practices to stay ahead of the curve.

Cloud security incidents are on the rise, with increases in what is typically the most consequential incident—data breaches—reported by an alarming 64% of organizations. Another 48% of organizations report increases in compliance violations, followed by operational downtime due to misconfigurations (45%).

**The top three increases in security incidents are the most costly:**
1. Data breaches ($$$$)
2. Compliance violations ($$$)
3. Downtime due to misconfigs ($$$)

![Figure 5: Increases in security incidents over the last 12 months: Data breaches (64%), Compliance violations (48%), Insecure APIs (46%), Downtime due to misconfigurations (45%), Advanced persistent threats (45%), Secret exposures (43%), Identities with overly permissive access (42%), Vulnerable or poisoned workload images (42%), Unrestricted network access (41%), Data leaks (34%).]

Of the security incidents detailed above, increases in excessive permissions reported by 42% of respondents is troubling. Organizations understand that identity management is the perimeter of cloud environments, and yet the problem with permissions persists.

> The increasing incidence of advanced persistent threats (APTs) points to a gap in security posture.

Organizations are witnessing an increase in advanced persistent threats (APTs), known for their sophistication and ability to remain undetected. This scenario emphasizes the imperative of taking a proactive, rather than reactive, approach to security.

# Securing Sensitive Data in the Cloud

> Organizations face significant data security challenges, with many relying on insufficient methods to safeguard sensitive information.

Of the organizations we surveyed, 50% conduct manual reviews to identify and classify sensitive data within the cloud, which is a concerning indicator of the state of data security. Manual reviews are time-consuming and error-prone.

> **50%** of organizations review code manually to locate their sensitive data.

With 98% of organizations storing sensitive data across multiple locations—on-prem servers, the public cloud, SaaS applications, private clouds, and endpoints—we know that security challenges are high.

![Figure 6: Data storage distribution: Endpoint (17%), SaaS (19%), Private Cloud (19%), On-prem (23%), Public Cloud (22%).]

![Figure 7: Top challenges in data security: Complexity and fragmentation of cloud environments (54%), Lenient IAM practices (50%), Inadequate monitoring of sensitive data (48%), Poor secret management practices (38%).]

Interestingly, while only 38% of organizations flagged difficulties with secrets management, 43% saw an increase in secrets exposure.

# What Would You Do Differently?

> Hindsight offers 20/20 insights for improved cloud migration.

### Establishing a Governance Framework
A significant 53% of respondents stress the importance of investing in a governance framework to manage cloud resources. By defining clear roles, policies, and processes, organizations can ensure resources are used efficiently and securely.

### Refactoring Applications
Half of survey participants (50%) suggest spending more time on refactoring applications rather than migrating them with minimal changes. This strategy involves reimagining how applications are architected to fully leverage cloud-native features.

### Prioritizing Security and Compliance
50% of respondents advocate for prioritizing security and compliance from the beginning of the cloud migration process. This approach is particularly important to Latin American organizations (57%).

### Researching Tools and Vendors
Another 48% of respondents stress the importance of dedicating more time to researching tools and vendors. This perspective is particularly valued by those in DevOps roles.

# The Human Factor

> Security processes trigger delays, stress, and DevOps-SecOps conflict, suggesting the need for a people-first approach to secure application development.

The most telling data point is that 84% of respondents say that security processes cause delays to their project timelines.

- **83%** view security processes as a burden.
- **79%** say employees frequently ignore or work-around security processes.
- **71%** admit they don’t understand their security responsibilities.
- **92%** attribute conflicting priorities between DevOps and SecOps to inefficient development.

Stress levels are palpable, with 71% of respondents saying they and their teammates are stressed. Turnover rates are high, according to 93% of respondents.

![Figure 8: Sources of stress among DevOps and cloud SecOps professionals: Conflict between DevOps and SecOps (52%), Rapid pace of change and tight deadlines (48%), Being responsible for getting hacked (46%), Employee turnover (43%).]

# Risks, Realities, and Cloud Security Strategies

> Organizations seek efficient security tools with automation, centralized visibility, and easy-to-use features to reduce blind spots and streamline operations.

Tooling issues significantly contribute to delays for 40% of survey respondents. One in 3 security practitioners attribute legacy security tools to their inability to stay on top of threat vectors.

- **91%** say the number of point tools creates blind spots.
- **98%** want to reduce the number of cloud security tools.
- **88%** struggle to identify what security tools they need.
- **94%** want a solution that provides immediate remediation steps.

![Figure 9: No. 1 factor considered when choosing a cloud security tool: Easy for SecOps to learn and use (52%), Easy for DevOps to learn and use (23%), Competitive pricing (12%), Best-in-breed capabilities (8%), Supports broad variety of platforms (4%), Impact on performance (2%).]

# Embracing the Unknown: The Impact of AI on the Application Lifecycle

> Organizations demonstrate a forward-looking approach to the future of cloud and application security in an AI-driven world.

AI is here, and organizations are anxious yet committed. 89% of respondents are concerned about AI-powered attacks compromising sensitive data.

- **47%** anticipate AI-fueled supply chain attacks.
- **45%** expect personalized phishing or deepfakes.
- **100%** of survey respondents are embracing AI-assisted application development.

Organizations are at different stages: 50% use AI extensively to generate code (led by Singapore at 60%, India at 58%, and Brazil at 57%).

**Priorities for 2024:**
- **100%** committed to gaining visibility into the entire pipeline for AI deployments.
- **99%** will define policies for AI model access.
- **98%** plan to build an inventory of AI models.

# Recommendations for Securing the Cloud

### 1. Consolidation with Platformization
Consider using a centralized security management platform that follows the journey to cloud maturity. A holistic, architecture-agnostic approach is essential for optimal visibility and automation.

### 2. Adopting AI Securely
Regulate AI usage as AI-generated code can lead to faster proliferation of misconfigurations. Protect software supply chains and automate sensitive data discovery to ensure it isn't used in model training.

### 3. Intelligent Data Security
Implement a strategy that defines how sensitive data is protected regardless of storage location. Invest in automated data discovery (DSPM) and data detection and response (DDR).

### 4. Reduce Traffic Jams in Your DevOps Pipeline
Evaluate DevOps maturity and observe how frequently security becomes a gating factor. Implement a secure-by-design approach for improved efficiency.

### 5. Install Proactive Security Measures
Commit 100% to building a DevSecOps culture. Recognize that security and development teams have different workflows and must be strategically aligned to avoid risking business outcomes.

# How Palo Alto Networks Helps

Palo Alto Networks Prisma Cloud secures applications from code to cloud, across multicloud environments. The platform delivers continuous visibility and threat prevention throughout the application lifecycle. Prisma Cloud enables security and DevOps teams to effectively collaborate to accelerate secure cloud-native application development and deployment.

# Methodology

The fourth annual State of Cloud-Native Security survey was conducted between December 20, 2023, and January 17, 2024. The population comprised 2,800 executives and practitioners across four regions: NAM (36%), EMEA (21%), LATAM (14%), and APJ (29%). Results are subject to a sampling variation of +/- 1.9 percentage points for the Global Sample at a 95% confidence level.