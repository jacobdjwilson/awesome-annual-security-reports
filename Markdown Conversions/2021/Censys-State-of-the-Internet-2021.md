# The State of Cloud
AUGUST 2021
DARK READING RESEARCH | THE STATE OF CLOUD

## Table of Contents
- [Executive Summary](#executive-summary)
- [Visibility and Tracking of Cloud Assets Remain Lackluster](#visibility-and-tracking-of-cloud-assets-remain-lackluster)
- [Respondents Exhibit Manage Cloud Exposures](#respondents-exhibit-manage-cloud-exposures)
- [Rogue Cloud Assets are More Common Than Respondents Realize](#rogue-cloud-assets-are-more-common-than-respondents-realize)
- [Cloud Security Tooling Still Needs Work](#cloud-security-tooling-still-needs-work)
- [Key Findings](#key-findings)
- [The Perception vs. Realities of Cloud Sprawl](#the-perception-vs-realities-of-cloud-sprawl)
- [The Hidden Cloud Service Exposures and Risks](#the-hidden-cloud-service-exposures-and-risks)
- [The Tools and Teams Currently in Place](#the-tools-and-teams-currently-in-place)
- [DevSecOps and Cloud Visibility](#devsecops-and-cloud-visibility)
- [Survey Methodology](#survey-methodology)
- [Conclusion/Recommendations](#conclusionrecommendations)

## Executive Summary
Recent tech headlines tell a clear story that cloud governance and security issues are getting worse. Cloud-originated breaches and data exposures continue to mount, and it is clear that adversaries are increasingly targeting cloud assets to their criminal ambitions.

There are number of reasons that cloud risks are growing, but data from Dark Reading’s The State of Cloud Survey 2021 indicates that one of the biggest is a persistent lack of in their capability to keep track of cloud assets and their risk levels.

utilized by organizations today and the tools they use to track and manage their cloud security afforded by these tools. We then validated those perceptions against an existing body of research data from Censys security experts across real-world cloud deployments.

This comparison uncovers what appears to be a perception gap between organizations’ affairs.

## Visibility and Tracking of Cloud Assets Remain Lackluster
The study found that:
- 52% of respondents say they either don’t know what they use to track their cloud assets, don’t track them at all, or use manual means of tracking such as spreadsheets.
- Fewer than one-third of tooling to track cloud assets.
- The most commonly named obstacles that keep them from tracking cloud inventory are time, budget, and lack of headcount.

## Respondents Exhibit Manage Cloud Exposures
- Despite low rates of consistent tracking and high rates of 57% of respondents are “very visibility their organizations have into their cloud assets.
- 58% of respondents say they are their assets and deployments are cloud exposures.
- This contrasts with the high incidence of exposed services and resources in Fortune 500 cloud deployments; data from Censys found 1.9 million Remote Desktop Protocol (RDP) exposures in just a dozen common cloud providers.

## Rogue Cloud Assets are More Common Than Respondents Realize
- 82% of respondents say they use four or fewer public cloud providers.
- Only 2% of organizations indicate they use more than seven providers.
- Deployment statistics show Fortune 500 cloud environments use an average of 25 different cloud providers.

## Cloud Security Tooling Still Needs Work
- 83% of organizations say identifying top cloud security priority.
- Yet only 57% say maintaining a comprehensive inventory is a top concern, meaning many organizations can’t identify risks in assets they don’t know about.
- The top security tool respondents use to control cloud assets is vulnerability management, and only 43% of organizations use it.

## Key Findings
![Figure 1]
Image description: A pie chart showing the perceived cloud visibility. The slices represent: Very Good (15%), Good (42%), Okay (34%), Poor (8%), and Very Poor (1%).

![Figure 2]
Image description: A bar graph showing the obstacles to cloud asset tracking. The bars represent: Time (54%), Budget (27%), Lack of Headcount (41%), Lack of Expertise (21%), Too Complex (50%), Lack of Automation (26%), Lack of Buy-In (28%), and Other (8%).

## The Perception vs. Realities of Cloud Sprawl
Despite a steady stream of very public cloud exposures in the news and increasing evidence that organizations struggle with cloud visibility and control, remain chipper about the state of affairs within their respective environments. Approximately 57% of organizations are visibility their organizations have into their cloud assets (Figure 1). This appears to evidence to the contrary.

For example, almost the same proportion cloud visibility admit they don’t have very good means to actually track that visibility. Some 52% say they either don’t know what they use to track their cloud assets, don’t track them at all, or use manual means of tracking such as spreadsheets to keep tabs on their cloud asset portfolio. The obstacles that keep them from achieving a are unsurprising: time, budget, and lack of headcount top the list (Figure 2).

for keeping tabs on cloud assets, the exhibit translates to a perceived surety that unauthorized cloud assets are not a problem in their environments. Only about 25% of respondents admit that their organization struggles with rogue cloud say they do not have rogue cloud assets in their organization.

When we think about this in light of the high rates of manual or non-existent tracking, the picture starts to crystallize: Organizations are counting on their policies to shield them from rogue assets and untracked cloud sprawl. Our survey shows that 75% of organizations have corporate policies around how and by whom cloud services are provisioned and managed.

![Figure 3]
Image description: A pie chart showing the cloud deployment models. The slices represent: Fully Public Cloud (18%), Hybrid Cloud (49%), Private Cloud (25%), Multi-Cloud (8%).

![Figure 4]
Image description: A bar graph showing the number of public cloud providers used. The bars represent: 1 (57%), 2 (6%), 3 (10%), 4 (2%), 5-7 (10%), 7+ (2%).

We can show incontrovertibly that these leaders think, though. We’ve accomplished this by comparing the average volume of cloud provider relationships reported by this survey’s respondents to the volume infrastructure.

Approximately 67% of respondents say they work with public cloud providers, with 18% stating they utilize a fully public cloud deployment model and 49% saying they rely on a hybrid model (Figure 3). The majority of our survey respondents say they limit the number of relationships they have with public cloud providers, with 82% stating they use four or fewer providers. A slim 2% of organizations report using more than seven providers (Figure 4).

And yet, when you compare these statistics with data gleaned from readily recent research report on Fortune 500 cloud that organizations are using, on average, 25 different cloud providers in their ecosystems.

Even accounting for some sample bias and differences between each data set — which are likely minimal since the organizations in this survey were primarily large ones with more than 1,000 employees — the difference between what respondents think their cloud environments look like compared to what’s observably lurking is extreme.

This is likely due to the inherent nature of cloud and the ability of individuals throughout an organization to easily create environment and its security controls.

## The Hidden Cloud Service Exposures and Risks
Of course, it isn’t just cloud sprawl that organizations appear to have distorted perceptions about. Comparing the survey results to measurable observations from security exposure resulting from those non-visible cloud assets is much worse than Again, more than half of organizations believe their teams are doing a good job securing cloud assets. Some 58% of at risk for exposure (Figures 5 and 6).

![Figure 5]
Image description: A pie chart showing the perceived risk of cloud exposures. The slices represent: Very Low (15%), Low (43%), Moderate (32%), High (8%), and Very High (2%).

![Figure 6]
Image description: A pie chart showing the confidence in preventing cloud exposures. The slices represent: Very Confident (13%), Confident (32%), Somewhat Confident (39%), Not Very Confident (14%), and Not at All Confident (2%).

misplaced, as real-world data shows that many organizations have hidden cloud probably don’t know about. When Censys examined common infrastructure elements using public cloud providers, it discovered uncommonly high numbers of exposures of sensitive services and resources.

Real-world deployment data from Censys found 1.9 million RDP exposures in just a dozen common cloud providers, as well as millions of database exposures from MySQL, Postgres, Redis, Elasticsearch, and others.

| Queries        | Results   | Date        | Source |
| -------------- | --------- | ----------- | ------ |
| MySQL Query    | 4,430,729 | May 14, 2021 |        |
| Postgres Query | 811,091   | May 14, 2021 |        |
| Redis Query    | 193,190   | May 14, 2021 |        |
| RDP Query      | 3,773,357 | May 14, 2021 |        |

This is particularly problematic considering that other studies have shown that in the cloud are the of cloud-based data breaches.

While many respondents clearly still don’t organizations, results from other questions show that the realities of cloud risks do produce at least some prickle of anxiety at many organizations. A resounding 68% of respondents admit that the worry of exposed services within cloud assets keeps them up at night. Other common worries include unnecessary functionality enabled, publicly accessible cloud stores, and default passwords in use.

## The Tools and Teams Currently in Place
So why do risks remain hidden at so many organizations, and does the gap linger when it comes to perceived and actual risk of cloud exposure? Organizations are clearly struggling to gain visibility over the full portfolio of cloud assets, and a lot of this likely comes down to the tools they’re using.

As mentioned above, more than half of organizations don’t have an automated method for gaining visibility of their cloud environment in its entirety. Among those who do have tooling, the most commonly used tools are asset management tools (used by 38% of organizations) and cloud security posture management tools (30%), which are almost neck and neck in prevalence.

equipped to control those assets they do know about. Disconcertingly, the most cloud assets is not a cloud-centric tool at all. When asked about the security controls they have in place, the most common answer (endorsed by 43% of respondents) was vulnerability management tooling, followed by cloud-enabled identity and access management (39%), and cloud latter of which does not do a good job of managing a portfolio, especially when dealing with dozens of different providers (Figure 7).

![Figure 7]
Image description: A bar graph showing the security tools used to control cloud assets. The bars represent: Vulnerability Management (43%), Cloud-Enabled IAM (39%), Cloud Security Posture Management (35%), Cloud Workload Protection Platform (19%), Container Security (23%), Network Security (17%), Data Loss Prevention (26%), Encryption (11%), and Other (3%).

Other frequently used tools include cloud security posture management and cloud workload protection platforms. When looking at funding priorities for cloud controls, we shouldn’t expect any big shakeups in these percentages, as vulnerability management again leads the pack at 42%, followed by cloud-enabled identity and access management (33%) (Figure 8).

![Figure 8]
Image description: A bar graph showing the funding priorities for cloud controls. The bars represent: Vulnerability Management (42%), Cloud-Enabled IAM (33%), Cloud Security Posture Management (26%), Cloud Workload Protection Platform (19%), Container Security (19%), Network Security (18%), Data Loss Prevention (17%), Encryption (8%), and Other (5%).

The use of attack surface management, which continuously discovers, manages, and remediates exposures in cloud assets, organizations say this is a line item in their budget, with the rest saying they don’t use it or don’t know about it.

When queried about the priority areas of risk that concern their security teams about cloud assets, survey respondents resoundingly named identifying and — this was named by 83% of organizations. a comprehensive inventory of assets — named by 57% of respondents. This hints that many organizations don’t recognize they may be putting the cart before the to identify or remediate risks in assets they don’t know about.

These teams say their top three cloud security concerns among cloud assets (in priority order) are securing user access, computing services, and exposed hosts. Other concerns include storage buckets and, to a lesser degree, containers and When it comes to discovering and securing cloud assets, the team in charge tends and the broader security team, rather cybersecurity pros) were named by 66% of respondents as the main responsible party for both discovering and securing assets. Meanwhile, just under a third of as the team responsible for each (Figure 9).

![Figure 9]
Image description: A bar graph showing the teams responsible for discovering and securing cloud assets. The bars represent: Security Team (66%), IT Operations (26%), DevOps (16%), Cloud Team (10%), and Other (8%).

At the programmatic level, the majority of organizations say they do have some kind of third-party risk management program to manage cybersecurity risks from cloud and other vendors. However, among those that have a program, fewer than half are staffed by dedicated cybersecurity professionals to run them. About a third of these programs are shouldered by cybersecurity pros with other duties, which could be a sign they may be programs in name only for the sake of compliance.

Overall, the teams tasked with cloud security are most likely to be governed Framework (CSF), which 58% name as the most used compliance framework in use at their organization.

## DevSecOps and Cloud Visibility
As DevOps and self-service precepts increasingly take hold within enterprise organizations, the role of developers spinning up and down their own cloud resources for test, dev, and production environments continues to grow.

As enterprise security teams try to stay aligned with these trends through DevSecOps practices, many are grappling with how they can control and monitor and containers leveraged by developers without impeding their autonomy.

Enterprises are gaining steam with this, with about 40% claiming they have built developer guardrails into the self-service toolchain to govern how they set up cloud storage buckets, containers, and other cloud infrastructure.

## Survey Methodology
than 1,000 employees, and respondents come from more than 18 industries.
The survey was conducted online. Respondents were recruited via emailed invitations containing an embedded link to the survey. The emails were practices and existing US privacy laws.
report, with data based on analysis of the States, Europe, and Asia.

## Conclusion/Recommendations
Organizations clearly operate with a false sense of security about their exposure to cloud vulnerabilities, and this survey indicates they’ll need to get back to the basics in how they identify and monitor their cloud assets as they sprawl over the You can’t protect what you can’t see, and cloud visibility is particularly challenging given its ephemeral nature and companies’ rogue cloud assets aren’t a problem at control is gaining visibility into the assets that aren’t supposed to exist.

Censys Attack Surface Management (ASM) continually uncovers unknown assets storage buckets and comprehensively checks all your public-facing assets for security and compliance problems regardless of where they’re hosted. Censys ASM provides easy routes to creating the disposition of known assets through integration with major providers like Qualys, Tenable, ServiceNow, Jira, and Splunk.
