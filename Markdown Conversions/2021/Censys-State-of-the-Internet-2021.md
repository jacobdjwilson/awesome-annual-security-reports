# State of the Internet: The State of Cloud (2021)

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [The Perception vs. Realities of Cloud Sprawl](#the-perception-vs-realities-of-cloud-sprawl)
- [The Hidden Cloud Service Exposures and Risks](#the-hidden-cloud-service-exposures-and-risks)
- [The Tools and Teams Currently in Place](#the-tools-and-teams-currently-in-place)
- [DevSecOps and Cloud Visibility](#devsecops-and-cloud-visibility)
- [Conclusion/Recommendations](#conclusionrecommendations)
- [Survey Methodology](#survey-methodology)

---

## Executive Summary
Recent tech headlines tell a clear story that cloud governance and security issues are getting worse. Cloud-originated breaches and data exposures continue to mount, and it is clear that adversaries are increasingly targeting cloud assets to their criminal ambitions. There are a number of reasons that cloud risks are growing, but data from Dark Reading’s The State of Cloud Survey 2021 indicates that one of the biggest is a persistent lack of visibility in their capability to keep track of cloud assets and their risk levels.

This report examines the cloud infrastructure utilized by organizations today and the tools they use to track and manage their cloud security. We then validated those perceptions against an existing body of research data from Censys security experts across real-world cloud deployments. This comparison uncovers what appears to be a perception gap between organizations’ perceived security and the actual state of affairs.

## Key Findings
The study found that:

**Visibility and Tracking of Cloud Assets Remain Lackluster**
- 52% of respondents say they either don’t know what they use to track their cloud assets, don’t track them at all, or use manual means of tracking such as spreadsheets.
- Fewer than one-third of organizations use automated tooling to track cloud assets.
- The most commonly named obstacles that keep them from tracking cloud inventory are time, budget, and lack of headcount.

**Respondents Exhibit Overconfidence in Ability to Manage Cloud Exposures**
- Despite low rates of consistent tracking and high rates of manual tracking, 57% of respondents are “very confident” in the visibility their organizations have into their cloud assets.
- 58% of respondents say they are confident their assets and deployments are secure from cloud exposures.
- This contrasts with the high incidence of exposed services and resources in Fortune 500 cloud deployments; data from Censys found 1.9 million Remote Desktop Protocol (RDP) exposures in just a dozen common cloud providers.

**Rogue Cloud Assets are More Common Than Respondents Realize**
- 82% of respondents say they use four or fewer public cloud providers.
- Only 2% of organizations indicate they use more than seven providers.
- Deployment statistics show Fortune 500 cloud environments use an average of 25 different cloud providers.

**Cloud Security Tooling Still Needs Work**
- 83% of organizations say identifying cloud assets is a top cloud security priority.
- Yet only 57% say maintaining a comprehensive inventory is a top concern, meaning many organizations can’t identify risks in assets they don’t know about.
- The top security tool respondents use to control cloud assets is vulnerability management, and only 43% of organizations use it.

## The Perception vs. Realities of Cloud Sprawl
Despite a steady stream of very public cloud exposures in the news and increasing evidence that organizations struggle with cloud visibility and control, many leaders remain chipper about the state of affairs within their respective environments. Approximately 57% of organizations are “very confident” in the visibility their organizations have into their cloud assets (Figure 1). This appears to be a misplaced confidence, given the evidence to the contrary.

![Figure 1: Chart showing confidence levels in cloud visibility]

For example, almost the same proportion of respondents who claim high cloud visibility admit they don’t have very good means to actually track that visibility. Some 52% say they either don’t know what they use to track their cloud assets, don’t track them at all, or use manual means of tracking such as spreadsheets to keep tabs on their cloud asset portfolio. The obstacles that keep them from achieving a better handle on their environment are unsurprising: time, budget, and lack of headcount top the list (Figure 2).

![Figure 2: Chart showing obstacles to cloud asset tracking]

We can show incontrovertibly that these leaders think, though. We’ve accomplished this by comparing the average volume of cloud provider relationships reported by this survey’s respondents to the volume of cloud providers actually in use.

Approximately 67% of respondents say they work with public cloud providers, with 18% stating they utilize a fully public cloud deployment model and 49% saying they rely on a hybrid model (Figure 3). The majority of our survey respondents say they limit the number of relationships they have with public cloud providers, with 82% stating they use four or fewer providers. A slim 2% of organizations report using more than seven providers (Figure 4).

![Figure 3: Chart showing cloud deployment models]
![Figure 4: Chart showing number of cloud providers used]

## The Hidden Cloud Service Exposures and Risks
And yet, when you compare these statistics with data gleaned from readily available sources, the reality is stark. A recent research report on Fortune 500 cloud environments shows that organizations are using, on average, 25 different cloud providers in their ecosystems.

Even accounting for some sample bias and differences between each data set—which are likely minimal since the organizations in this survey were primarily large ones with more than 1,000 employees—the difference between what respondents think their cloud environments look like compared to what’s observably lurking is extreme.

This is likely due to the inherent nature of cloud and the ability of individuals throughout an organization to easily create infrastructure, often bypassing the environment and its security controls.

![Figure 5: Chart showing confidence in security of assets]
![Figure 6: Chart showing risk of exposure]

Real-world deployment data from Censys found 1.9 million RDP exposures in just a dozen common cloud providers, as well as millions of database exposures from MySQL, Postgres, Redis, Elasticsearch, and others.

| Queries | Results | Date |
| :--- | :--- | :--- |
| MySQL Query | 4,430,729 | May 14, 2021 |
| Postgres Query | 811,091 | May 14, 2021 |
| Redis Query | 193,190 | May 14, 2021 |
| RDP Query | 3,773,357 | May 14, 2021 |

## The Tools and Teams Currently in Place
So why do risks remain hidden at so many organizations? Organizations are clearly struggling to gain visibility over the full portfolio of cloud assets, and a lot of this likely comes down to the tools they’re using.

As mentioned above, more than half of organizations don’t have an automated method for gaining visibility of their cloud environment in its entirety. Among those who do have tooling, the most commonly used tools are asset management tools (used by 38% of organizations) and cloud security posture management tools (30%).

When asked about the security controls they have in place, the most common answer (endorsed by 43% of respondents) was vulnerability management tooling, followed by cloud-enabled identity and access management (39%), and cloud security posture management (35%).

![Figure 7: Chart showing security controls in place]

When looking at funding priorities for cloud controls, vulnerability management again leads the pack at 42%, followed by cloud-enabled identity and access management (33%) (Figure 8).

![Figure 8: Chart showing funding priorities for cloud controls]

When it comes to discovering and securing cloud assets, the team in charge tends to be the IT team and the broader security team, rather than a dedicated cloud security team. IT (including cybersecurity pros) were named by 66% of respondents as the main responsible party for both discovering and securing assets.

![Figure 9: Chart showing teams responsible for cloud security]

Overall, the teams tasked with cloud security are most likely to be governed by the NIST Cybersecurity Framework (CSF), which 58% name as the most used compliance framework in use at their organization.

## DevSecOps and Cloud Visibility
As DevOps and self-service precepts increasingly take hold within enterprise organizations, the role of developers spinning up and down their own cloud resources for test, dev, and production environments continues to grow.

Enterprises are gaining steam with this, with about 40% claiming they have built developer guardrails into the self-service toolchain to govern how they set up cloud storage buckets, containers, and other cloud infrastructure.

At the programmatic level, the majority of organizations say they do have some kind of third-party risk management program to manage cybersecurity risks from cloud and other vendors. However, among those that have a program, fewer than half are staffed by dedicated cybersecurity professionals to run them.

## Conclusion/Recommendations
Organizations clearly operate with a false sense of security about their exposure to cloud vulnerabilities, and this survey indicates they’ll need to get back to the basics in how they identify and monitor their cloud assets as they sprawl over the internet.

You can’t protect what you can’t see, and cloud visibility is particularly challenging given its ephemeral nature and companies’ reliance on manual tracking. The first step to control is gaining visibility into the assets that aren’t supposed to exist.

Censys Attack Surface Management (ASM) continually uncovers unknown assets like storage buckets and comprehensively checks all your public-facing assets for security and compliance problems regardless of where they’re hosted. Censys ASM provides easy routes to creating a comprehensive inventory and monitoring the disposition of known assets through integration with major providers like Qualys, Tenable, ServiceNow, Jira, and Splunk.

## Survey Methodology
The survey was conducted online. Respondents were recruited via emailed invitations containing an embedded link to the survey. The emails were sent to a list of IT and security professionals. The survey was conducted in accordance with standard research practices and existing US privacy laws. The report includes data based on analysis of the Censys search engine, which scans the entire IPv4 space across the United States, Europe, and Asia. The survey included 100+ respondents from organizations with more than 1,000 employees, and respondents come from more than 18 industries.