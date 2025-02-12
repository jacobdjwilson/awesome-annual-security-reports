```markdown
# 2023 State of the Cloud Whitepaper

## Table of Contents
- [Executive summary](#executive-summary)
- [The year in review](#the-year-in-review)
- [Current landscape](#current-landscape)
- [Cloud usage](#cloud-usage)
- [Data exposure](#data-exposure)

---

## Executive summary

With cloud technology constantly evolving and growing increasingly critical to business operations, the responsibility of security professionals to stay abreast of the state of the cloud has never been greater in order to proactively address potential threats and ensure the safe and secure deployment of cloud solutions.

Over the past year, we have observed how cloud adoption has continued to grow with more organizations increasing their footprint in the cloud. Many new capabilities were introduced, with the number of possible API calls increasing by 15% in AWS, 20% in Azure, and 45% in GCP.

Although new services and their corresponding APIs expand the possibilities of how the cloud can be utilized, they can also broaden attack surfaces and create more challenges for cloud defenders. According to our data, 57% of companies use more than one cloud platform and therefore require greater knowledge and expertise from their security teams who need visibility into multiple platforms as well as the interfaces between them.

Besides novel cloud risks, well-known prevalent risks such as data exposure are also of concern. For instance, our data shows that 47% of companies have at least one database or storage bucket publicly exposed to the internet, and an attacker can discover and access an exposed bucket with a guessable name (e.g. “wiz-backup”) in less than 13 hours.

In this data-driven report, based on our scanning of over 200,000 cloud accounts, including more than 30% of the Fortune 100 environments, we analyze the latest industry trends and developments, presenting a factual and data-based assessment of the current state and progression of cloud technology. We examine how the cloud has evolved over the past year and attempt to shed light on some of the complexity of cloud environments, including aspects such as organizational usage of multi-cloud and both managed and non-managed services. We hope this can help cloud builders and defenders ensure they have the visibility and tools that they need to continue their cloud growth and protect their company’s assets. In addition, we will review notable cloud threats from last year and provide insight into the speed of compromise of misconfigured environments.

## The year in review

cloudvulndb
AttachMe Hell's Keychain ExtraReplica
PEACH cloud isolation framework
guidance
instance metadata service
new detection
UNC2903 
targeting IMDSv1
discovered

The sudden upsurge in 2021 of researchers attacking cloud vendors continued into 2022. A project sponsored by Wiz called `cloudvulndb` has been collecting these incidents, in part to look for patterns. Wiz’s researchers found several critical cross-tenant vulnerabilities in multiple cloud providers (see `AttachMe`, `Hell's Keychain`, `ExtraReplica`, `PEACH cloud isolation framework`, and more). By using the insights from the past incidents and our researchers’ expertise, we developed the `guidance` to offer guidance on better securing not only the cloud providers, but any PaaS or SaaS solution running multi-tenant environments.

Threat actors are becoming more proficient at attacking cloud environments. LAPSUS$–one of the most brazen–used its access at companies to move laterally through their cloud environments. Our `guidance` on mitigating the risks from this group is based on existing industry best practices but tailored to this threat actor’s particular activity against cloud environments.

AWS’s `instance metadata service` version 2 (IMDSv2) gained traction in a few ways this past year. A default deployment of an EC2 uses an older version of this service (IMDSv1) which does not mitigate SSRF and related attacks when the host contains other vulnerabilities. Even though a more secure version was released in 2019, the default IMDSv1 is still common (most likely for legacy support). AWS’s GuardDuty received a `new detection` for when IAM role credentials are suspected to be stolen from an EC2 via this service. This risk is still relevant, as demonstrated by the threat actor `UNC2903` targeting IMDSv1. A number of vendors also made changes to allow customers to enforce IMDSv2. Finally, malware built to run specifically inside AWS Lambda functions was `discovered` in the wild. Although this concept has been known for years, threat actors only just started using it.

## Current landscape

AWS Azure
GCP

Cloud usage continues to grow. Companies are shifting more of their workloads from on-prem to the cloud and both adding and expanding new and existing workloads in the cloud. According to the 2022 Q3 earnings of the top three cloud providers (AWS, Azure, and GCP), revenue increased across each cloud provider by a minimum of 20% from Q3 in 2021.

Cloud providers keep increasing their offerings and their complexity. In addition to growing in size, cloud providers are also becoming more complex. AWS has added APIs at a steady pace, with about 40 new services and 1600 new actions per year for the past 6 years[^1]. The yearly spikes are due to the annual AWS re:Invent conference where they release large numbers of new features.

[^1]: The API counts data was obtained by walking the commits of botocore.

![Feature explosion: AWS API count in constant growth. A line chart showing the number of AWS APIs from 2016 to 2022, steadily increasing each year. The Y-axis is labeled "AWS" and ranges from 0 to 14,000. The X-axis represents the years from 2016 to 2022.]

![Even in this market, cloud is winning. A bar chart comparing Q3 Cloud Revenue for 2021 and 2022 for AWS, Azure, and GCP. The Y-axis is labeled "Q3 Cloud Revenue" and ranges from $0B to $25B. The X-axis represents the cloud providers.]

Additionally, the privileges available to control API access have increased in the past year across the top three cloud providers by 15% for AWS, 20% for Azure, and 45% for GCP[^2].

[^2]: Privilege counts were acquired from https://github.com/iann0036/iam-dataset.

### Our data set

This report is based on our scanning of over 200,000 cloud accounts (AWS, OCI, Alibaba cloud accounts, GCP projects, Azure subscriptions) including more than 30% of the Fortune 100 as customers.

## Cloud usage

Is this the year of Linux on the desktop multi-cloud? According to our data, the idea of multi-cloud as a single architecture that spans multiple cloud providers is uncommon.

Most companies are only on one cloud and in cases where they are using multiple clouds, the majority of their workloads are on one cloud provider. In fact, about 43% of customers operate entirely on one cloud.

![The feature arms race. A line chart showing the privilege count per cloud provider (AWS, Azure, GCP) from January to December 2022. The Y-axis is labeled "Privilege count per cloud provider (2022)" and ranges from 5,000 to 17,000. The X-axis represents the months from January to December.]

![How many clouds does it take to run a company? A pie chart showing the distribution of companies using one, two, or three or more cloud platforms. 43% of companies use one platform, 35% use two platforms, and 22% use three or more platforms.]

When examining how many workloads each customer is placing in each cloud provider, our data shows that about 78% of customers have over 80% of their workloads in a single cloud provider. In the following diagram we have sorted our tenants by the percent of their workloads in their largest cloud provider, and then bucketed these into deciles.

Most cloud customers concentrate their workloads in a few large accounts. Nearly all companies running on AWS have multiple AWS accounts, but the vast majority of these companies have a few disproportionately large accounts alongside many smaller ones. For over 97% of customers using AWS, the largest 5% of their accounts contain over 50% of their workloads.

In other words, although most AWS customers do not maintain a single monolithic account in the strictest sense, they do use a handful of what might be considered monolithic accounts.

AWS is the most common platform, Azure the 2nd, and GCP the 3rd. Most workloads (in this case, virtual machines) across all companies are running on AWS (72%), and the majority of companies (62%) choose to place more of their workloads on AWS than on other cloud providers. In other words, no matter how we look at it, AWS is the most common primary platform among cloud customers.

![How real is multi-cloud? A stacked bar chart representing the percent of workloads in primary platforms. Each building represents 10% of all companies, ranked from left to right by the size of their primary platform. The chart shows that 8 out of 10 companies have over 80% of their workloads in a single cloud provider, and 4 out of 10 companies use a single cloud provider.]

![VMs per platform across all customers. A pie chart showing the distribution of virtual machines across AWS (72%), Azure (13%), GCP (12%), and Other (3%).]

![Breakdown of all customers' primary platforms. A pie chart showing the distribution of primary platforms among customers: AWS (62%), Azure (27%), GCP (10%), and Other (1%).]

We can also break this down further and examine which cloud providers our customers are using as their secondary and tertiary platforms (i.e. their 2nd largest and 3rd largest platforms, respectively). We can then observe that among companies using more than one platform, Azure is the most common secondary platform (41%), whereas among customers using more than two platforms, GCP is the most common tertiary platform (44%).

Another way we can analyze how customers are using multi-cloud is by checking combinations or pairings of different platforms.

The following Sankey diagram breaks down primary platform usage on the left side and secondary platform usage on the right side, while the middle section shows the percentage of companies using each combination of two platforms. For example, while 27% of customers have most of their workloads in Azure (as mentioned above), 47% of this group are using AWS as their secondary platform, and 8% are using GCP.

![Breakdown of multi-cloud customers' secondary platforms. A pie chart showing the distribution of secondary platforms among multi-cloud customers: AWS (32%), Azure (41%), GCP (16%), and Other (10%).]

![Breakdown of multi-cloud customers' tertiary platforms. A pie chart showing the distribution of tertiary platforms among multi-cloud customers: AWS (25%), Azure (30%), GCP (44%), and Other (2%).]

![Percentage of customers using various combinations of AWS, Azure, and GCP as their primary and secondary platforms. A Sankey diagram showing the flow of customers from primary platforms (AWS, Azure, GCP) to secondary platforms (AWS, Azure, GCP). The percentages indicate the proportion of customers using each combination.]

Companies are using a healthy mix of managed and non-managed databases. Over 90% of AWS customers use managed database servers (for example PostgreSQL running on RDS), while that number is 87% in GCP and 82% in Azure. However, over 91% of companies have non-managed database servers running on IaaS (for example MySQL manually installed on an EC2), with only 6% of companies using managed database servers exclusively, and 90% using a mix of managed and non-managed.

As to which database flavors are being used, PostgreSQL, Redis, and MySQL are the most prevalent, with over 90% of companies having at least one instance of a PostgreSQL server (whether managed or non-managed).

Looking at the top 5 most prevalent database flavors, we can see that each of their managed and non-managed offerings are more or less evenly represented. For example, 76% of companies have at least one managed instance of a Redis database, while 80% have at least one non-managed instance. There doesn’t appear to be any clear preference for managed or non-managed databases in terms of usage.

![PostgreSQL for the win. A bar chart showing the percent of environments with each database flavor (managed + non-managed) for the Top 20 databases. The Y-axis is labeled "Percent of environments with each database flavor - Top 20 (managed + non-managed)" and ranges from 0 to 100%. The X-axis represents the database flavors.]

![Managed DBs + Unmanaged DBs = Percent of environments with each database flavor: managed vs. non-managed - Top 5. A bar chart comparing the percentage of managed and non-managed instances for the Top 5 database flavors (PostgreSQL, Redis, MySQL, MSSQL, ElasticSearch). The Y-axis is labeled "Percent of environments with each database flavor: managed vs. non-managed - Top 5" and ranges from 0 to 1. The X-axis represents the database flavors.]

## Data exposure

Cost of a Data Breach 2022 Report

The risk of data exposure is shockingly common. Data leaks are reported in the news every week. Attackers are aware of the value of sensitive data and the increasing difficulties in securing it. They continuously scan the internet for exposed databases and buckets. With the average cost of a data breach now over $5 million according to IBM’s `Cost of a Data Breach 2022 Report`, eliminating this risk should be a top priority.

47% of companies have at least one database or storage bucket exposed to the internet (either managed or non-managed), and over 20% of those cloud environments with publicly accessible buckets have buckets that contain sensitive data.

Moreover, 13% of cloud environments have at least one publicly exposed non-managed database server, whereas for managed databases that number is 32%.

Exposed resources are compromised within hours. In experiments we ran where we created S3 buckets with names we assumed attackers might be targeting – taking well-known company names and adding “-backup”, “_logs”, etc. – we spotted attempts to list the contents of the S3 buckets in as little as 13 hours. In a similar test, we created an S3 bucket with an unguessable name, but referenced it in a commit to a public GitHub repo. Attempts at listing it occurred within 7 hours. This indicates to us the speed with which attackers could potentially find and exfil a publicly exposed S3 bucket.

![Attackers are searching for exposed resources. A graphic illustrating the time it takes for attackers to discover exposed S3 buckets. Exposed buckets with common names are discovered within 13 hours, while exposed buckets referenced in GitHub repos are found within 7 hours.]
```
