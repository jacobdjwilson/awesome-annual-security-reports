Organization: Censys
Report Title: State-of-the-Internet
Year: 2021

# The State of Cloud

AUGUST 2021

## Table of Contents
- [Executive Summary](#executive-summary)
- [Key Findings](#key-findings)
- [The Perception vs. Realities of Cloud Sprawl](#the-perception-vs-realities-of-cloud-sprawl)
- [The Hidden Cloud Service Exposures and Risks](#the-hidden-cloud-service-exposures-and-risks)
- [The Tools and Teams Currently in Place](#the-tools-and-teams-currently-in-place)
- [DevSecOps and Cloud Visibility](#devsecops-and-cloud-visibility)
- [Conclusion/Recommendations](#conclusion-recommendations)
- [Survey Methodology](#survey-methodology)

## Executive Summary

Recent tech headlines tell a clear story that cloud governance and security issues are getting worse. Cloud-originated breaches and data exposures continue to mount, and it is clear that adversaries are increasingly targeting cloud assets to their criminal ambitions.

There are number of reasons that cloud risks are growing, but data from Dark Reading’s The State of Cloud Survey 2021 indicates that one of the biggest is a persistent lack of in their capability to keep track of cloud assets and their risk levels.

This report examines the perceptions of IT and security professionals regarding the cloud assets utilized by organizations today and the tools they use to track and manage their cloud inventory. It also looks at how much confidence these professionals have in the visibility and security afforded by these tools. We then validated those perceptions against an existing body of research data from Censys security experts across real-world cloud deployments to see how well those perceptions match reality.

This comparison uncovers what appears to be a perception gap between organizations’ confidence in their cloud security and the actual, observable state of their cloud security affairs.

## Key Findings

The study found that:

**Visibility and Tracking of Cloud Assets Remain Lackluster**
- 82% of respondents say they use four or fewer public cloud providers.
- Only 2% of organizations indicate they use more than seven providers.
- Deployment statistics show Fortune 500 cloud environments use an average of 25 different cloud providers.

**Cloud Security Tooling Still Needs Work**
- 83% of organizations say identifying and remediating cloud risks is their top cloud security priority.
- Yet only 57% say maintaining a comprehensive inventory is a top concern, meaning many organizations can’t identify risks in assets they don’t know about.
- The top security tool respondents use to control cloud assets is vulnerability management, and only 43% of organizations use it.

**Rogue Cloud Assets are More Common Than Respondents Realize**
- 52% of respondents say they either don’t know what they use to track their cloud assets, don’t track them at all, or use manual means of tracking such as spreadsheets.
- Fewer than one-third of organizations use automated tooling to track cloud assets.
- The most commonly named obstacles that keep them from tracking cloud inventory are time, budget, and lack of headcount.

**Respondents Exhibit Overconfidence in Ability to Manage Cloud Exposures**
- Despite low rates of consistent tracking and high rates of manual inventory management, 57% of respondents are “very confident” or “confident” in the visibility their organizations have into their cloud assets.
- 58% of respondents say they are “very confident” or “confident” their assets and deployments are not at risk for exposure to hidden cloud exposures.
- This contrasts with the high incidence of exposed services and resources in Fortune 500 cloud deployments; data from Censys found 1.9 million Remote Desktop Protocol (RDP) exposures in just a dozen common cloud providers.

## The Perception vs. Realities of Cloud Sprawl

Despite a steady stream of very public cloud exposures in the news and increasing evidence that organizations struggle with cloud visibility and control, IT and security professionals largely remain chipper about the state of affairs within their respective environments. Approximately 57% of organizations are “very confident” or “confident” in the visibility their organizations have into their cloud assets (Figure 1). This appears to be a case of overconfidence in light of evidence to the contrary.

![Figure 1: Chart showing levels of confidence in cloud asset visibility. Data points: 42%, 34%, 15%, 8%, 1%.]

For example, almost the same proportion of respondents who are confident in their cloud visibility admit they don’t have very good means to actually track that visibility. Some 52% say they either don’t know what they use to track their cloud assets, don’t track them at all, or use manual means of tracking such as spreadsheets to keep tabs on their cloud asset portfolio. The obstacles that keep them from achieving a more automated and comprehensive view are unsurprising: time, budget, and lack of headcount top the list (Figure 2).

![Figure 2: Chart showing obstacles to tracking cloud inventory. Data points: 54%, 50%, 41%, 28%, 27%, 26%, 21%, 8%.]

Despite the lack of automated means for keeping tabs on cloud assets, the confidence that many organizations exhibit translates to a perceived surety that unauthorized cloud assets are not a problem in their environments. Only about 25% of respondents admit that their organization struggles with rogue cloud assets, while a combined 67% of respondents say they do not have rogue cloud assets in their organization.

When we think about this in light of the high rates of manual or non-existent tracking, the picture starts to crystallize: Organizations are counting on their policies to shield them from rogue assets and untracked cloud sprawl. Our survey shows that 75% of organizations have corporate policies around how and by whom cloud services are provisioned and managed.

![Figure 3: Chart showing cloud deployment models (Public, Hybrid, etc.). Data points: 49%, 25%, 18%, 8%.]

We can show incontrovertibly that these policies aren’t working as well as security leaders think, though. We’ve accomplished this by comparing the average volume of cloud provider relationships reported by this survey’s respondents to the volume of providers actually found in enterprise infrastructure.

Approximately 67% of respondents say they work with public cloud providers, with 18% stating they utilize a fully public cloud deployment model and 49% saying they rely on a hybrid model (Figure 3). The majority of our survey respondents say they limit the number of relationships they have with public cloud providers, with 82% stating they use four or fewer providers. A slim 2% of organizations report using more than seven providers (Figure 4).

![Figure 4: Chart showing the number of public cloud providers used. Data points: 57%, 25%, 10%, 6%, 2%.]

And yet, when you compare these statistics with data gleaned from readily observable cloud assets, a different story emerges. Censys’ recent research report on Fortune 500 cloud footprints found that organizations are using, on average, 25 different cloud providers in their ecosystems.

Even accounting for some sample bias and differences between each data set — which are likely minimal since the organizations in this survey were primarily large ones with more than 1,000 employees — the difference between what respondents think their cloud environments look like compared to what’s observably lurking is extreme.

This is likely due to the inherent nature of cloud and the ability of individuals throughout an organization to easily create assets that live outside the corporate environment and its security controls.

## The Hidden Cloud Service Exposures and Risks

Of course, it isn’t just cloud sprawl that organizations appear to have distorted perceptions about. Comparing the survey results to measurable observations from Censys, it appears that the actual security exposure resulting from those non-visible cloud assets is much worse than organizations realize.

Again, more than half of organizations believe their teams are doing a good job securing cloud assets. Some 58% of respondents say they are “very confident” or “confident” their assets are not at risk for exposure (Figures 5 and 6).

![Figure 5: Chart showing confidence in cloud asset security. Data points: 43%, 32%, 15%, 8%, 2%.]

![Figure 6: Chart showing perceived risk of exposure. Data points: 39%, 32%, 14%, 13%, 2%.]

This confidence appears to be misplaced, as real-world data shows that many organizations have hidden cloud exposures that their security teams probably don’t know about. When Censys examined common infrastructure elements using public cloud providers, it discovered uncommonly high numbers of exposures of sensitive services and resources.

| Queries | Results | Source | Date |
| :--- | :--- | :--- | :--- |
| MySQL Query | 4,430,729 | Real-world deployment data from Censys | May 14, 2021 |
| Postgres Query | 811,091 | Real-world deployment data from Censys | May 14, 2021 |
| Redis Query | 193,190 | Real-world deployment data from Censys | May 14, 2021 |
| RDP Query | 3,773,357 | Real-world deployment data from Censys | May 14, 2021 |

Real-world deployment data from Censys found 1.9 million RDP exposures in just a dozen common cloud providers, as well as millions of database exposures from MySQL, Postgres, Redis, Elasticsearch, and others.

This is particularly problematic considering that other studies have shown that misconfigured services in the cloud are the number one cause of cloud-based data breaches.

While many respondents clearly still don’t see the full extent of the risk in their organizations, results from other questions show that the realities of cloud risks do produce at least some prickle of anxiety at many organizations. A resounding 68% of respondents admit that the worry of exposed services within cloud assets keeps them up at night. Other common worries include unnecessary functionality enabled, publicly accessible cloud stores, and default passwords in use.

## The Tools and Teams Currently in Place

So why do risks remain hidden at so many organizations, and does the gap linger when it comes to perceived and actual risk of cloud exposure? Organizations are clearly struggling to gain visibility over the full portfolio of cloud assets, and a lot of this likely comes down to the tools they’re using.

As mentioned above, more than half of organizations don’t have an automated method for gaining visibility of their cloud environment in its entirety. Among those who do have tooling, the most commonly used tools are asset management tools (used by 38% of organizations) and cloud security posture management tools (30%), which are almost neck and neck in prevalence.

Organizations also appear to be ill-equipped to control those assets they do know about. Disconcertingly, the most common tool used to secure and control cloud assets is not a cloud-centric tool at all.

When asked about the security controls they have in place, the most common answer (endorsed by 43% of respondents) was vulnerability management tooling, followed by cloud-enabled identity and access management (39%), and cloud provider native security tools (35%), the latter of which does not do a good job of managing a portfolio, especially when dealing with dozens of different providers (Figure 7).

![Figure 7: Chart showing security controls currently in place. Data points: 43%, 39%, 35%, 23%, 19%, 17%, 11%, 3%.]

Other frequently used tools include cloud security posture management and cloud workload protection platforms. When looking at funding priorities for cloud controls, we shouldn’t expect any big shakeups in these percentages, as vulnerability management again leads the pack at 42%, followed by cloud-enabled identity and access management (33%) (Figure 8).

![Figure 8: Chart showing funding priorities for cloud controls. Data points: 42%, 33%, 26%, 19%, 19%, 18%, 17%, 8%, 5%.]

The use of attack surface management, which continuously discovers, manages, and remediates exposures in cloud assets, is still in its infancy. Only 17% of organizations say this is a line item in their budget, with the rest saying they don’t use it or don’t know about it.

When queried about the priority areas of risk that concern their security teams about cloud assets, survey respondents resoundingly named identifying and remediating risks as their top priority — this was named by 83% of organizations.

Compare that to the priority of maintaining a comprehensive inventory of assets — named by 57% of respondents. This hints that many organizations don’t recognize they may be putting the cart before the horse, as it is impossible for a team to identify or remediate risks in assets they don’t know about.

These teams say their top three cloud security concerns among cloud assets (in priority order) are securing user access, computing services, and exposed hosts. Other concerns include storage buckets and, to a lesser degree, containers and serverless functions.

When it comes to discovering and securing cloud assets, the team in charge tends to be the centralized IT organization and the broader security team, rather than DevOps. IT and security teams (non-cybersecurity pros) were named by 66% of respondents as the main responsible party for both discovering and securing assets. Meanwhile, just under a third of respondents named the DevOps team as the team responsible for each (Figure 9).

![Figure 9: Comparison chart showing responsibility for discovering vs. securing cloud assets between IT, Security, and DevOps teams. Data points: 66%, 66%, 37%, 31%, 27%, 26%, 24%, 23%, 16%, 16%, 10%, 9%, 8%, 7%.]

Overall, the teams tasked with cloud security are most likely to be governed by the NIST Cybersecurity Framework (CSF), which 58% name as the most used compliance framework in use at their organization.

## DevSecOps and Cloud Visibility

As DevOps and self-service precepts increasingly take hold within enterprise organizations, the role of developers spinning up and down their own cloud resources for test, dev, and production environments continues to grow.

As enterprise security teams try to stay aligned with these trends through DevSecOps practices, many are grappling with how they can control and monitor the sprawl of storage buckets, hosts, and containers leveraged by developers without impeding their autonomy.

Enterprises are gaining steam with this, with about 40% claiming they have built developer guardrails into the self-service toolchain to govern how they set up cloud storage buckets, containers, and other cloud infrastructure.

At the programmatic level, the majority of organizations say they do have some kind of third-party risk management program to manage cybersecurity risks from cloud and other vendors. However, among those that have a program, fewer than half are staffed by dedicated cybersecurity professionals to run them. About a third of these programs are shouldered by cybersecurity pros with other duties, which could be a sign they may be programs in name only for the sake of compliance.

## Conclusion/Recommendations

Organizations clearly operate with a false sense of security about their exposure to cloud vulnerabilities, and this survey indicates they’ll need to get back to the basics in how they identify and monitor their cloud assets as they sprawl over the coming years.

You can’t protect what you can’t see, and cloud visibility is particularly challenging given its ephemeral nature and companies’ reliance on dozens of cloud providers.

Censys Attack Surface Management (ASM) continually uncovers unknown assets like rogue instances and forgotten storage buckets and comprehensively checks all your public-facing assets for security and compliance problems regardless of where they’re hosted. Censys ASM provides easy routes to creating a comprehensive inventory and tracking the disposition of known assets through integration with major providers like Qualys, Tenable, ServiceNow, Jira, and Splunk.

While many organizations believe that rogue cloud assets aren’t a problem at their company, the only way to be in control is gaining visibility into the assets that aren’t supposed to exist.

## Survey Methodology

**The State of Cloud Survey** was conducted by Dark Reading and sponsored by Censys. The survey was conducted in early 2021. The survey includes 118 respondents. All respondents are IT and security professionals. All respondents work at organizations with more than 1,000 employees, and respondents come from more than 18 industries.

The survey was conducted online. Respondents were recruited via emailed invitations containing an embedded link to the survey. The emails were sent to a select group of Dark Reading’s audience. The survey was conducted by Informa Engage on behalf of Dark Reading, in accordance with standard research practices and existing US privacy laws.

Respondents represent a global audience, with the majority of respondents located in the United States, Europe, and Asia.

**The Censys data** was pulled from the Censys 2021 State of the Internet report, with data based on analysis of the Fortune 500.